#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
知识库 · 维护工具

子命令：
    audit                 体检：找重复、矛盾、失效、错位、孤岛
    review                写知识体系综述
    merge A B [C...]      合并：把 B（及后续）并入 A
    prune 词条 [词条...]   下架：移到 _废弃（不真删）
    ask "问题"            问答：检索相关卡片后作答
    rebuild               重建索引 / MOC / 首页

审计只出报告不动文件；合并和下架会改库，执行前会打印方案并等待确认。
"""
import sys
import re
import json
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

sys.path.insert(0, str(Path(__file__).resolve().parent))
import curator as C

BASE = C.BASE
CONCEPTS = C.CONCEPTS
OFFICE = C.OFFICE
CONFIG = C.CONFIG
TRASH = BASE / "_废弃"
ANALYSIS = BASE / "分析"
REPORTS = OFFICE / "报告"
QA_LOG = OFFICE / "问答记录.md"

AUDIT_PROMPT = """你是知识库的维护员，负责体检。给你一批概念卡的摘要，找出需要处理的问题。

判断标准：
1. 重复（duplicate）：两个词条指同一个东西（同义词、中英文、缩写全称、近义表述）。给出一条保留、其余合并的建议。
2. 矛盾（conflict）：两条概念的说法互相打架，或某条已被新结论推翻。指出冲突点。
3. 失效（obsolete）：内容明显过时（版本已被取代、事实已改变）、或只是一次性信息不值得长期保留。
4. 错位（misplaced）：领域归属明显不对，或同一概念被拆到多个领域。
5. 孤岛（orphan）：没有任何关联也不属于任何领域主干的边缘卡片。
6. 缺链（missing_link）：明显相关但彼此没建立关联的概念对。

严格一点：不确定就不要报。宁缺毋滥，误报会让人白删东西。

只输出 JSON：
{
  "duplicates": [{"keep": "保留的词条", "merge": ["被并入的词条"], "reason": "为什么是同一个"}],
  "conflicts": [{"terms": ["词条A", "词条B"], "issue": "冲突在哪", "suggest": "建议怎么处理"}],
  "obsolete": [{"term": "词条", "reason": "为什么该下架"}],
  "misplaced": [{"term": "词条", "from": "现在的领域", "to": "建议的领域", "reason": ""}],
  "orphans": [{"term": "词条", "reason": ""}],
  "missing_links": [{"pair": ["词条A", "词条B"], "relation": "关系"}]
}"""


# ---------- 卡片读写 ----------

def load_cards():
    cards = []
    if not CONCEPTS.is_dir():
        return cards
    for f in sorted(CONCEPTS.glob("*.md")):
        text = f.read_text(encoding="utf-8", errors="ignore")
        def g(k):
            m = re.search(rf"^{k}:\s*(.+)$", text, re.M)
            return m.group(1).strip() if m else ""
        am = re.search(r"^aliases:\s*\[(.*?)\]", text, re.M)
        aliases = [x.strip() for x in am.group(1).split(",") if x.strip()] if am else []
        links = re.findall(r"\[\[([^\]|#]+)", text)
        cards.append({
            "stem": f.stem,
            "path": f,
            "term": g("term") or f.stem,
            "domain": g("domain"),
            "kind": g("kind"),
            "aliases": aliases,
            "updated": g("updated") or g("created"),
            "links": [x.strip() for x in links],
            "text": text,
            "size": len(text),
        })
    return cards


def one_liner(text, n=70):
    body = re.sub(r"^---[\s\S]*?---\s*", "", text)
    for line in body.splitlines():
        s = line.strip("# >\t ")
        if s and not s.startswith("---"):
            return s[:n]
    return ""


def ask_confirm(msg):
    try:
        r = input(msg + " [y/N] ").strip().lower()
    except EOFError:
        return False
    return r in ("y", "yes", "是")


def llm(cfg, system, user, max_tokens=3000):
    from openai import OpenAI
    c = OpenAI(api_key=cfg["api_key"], base_url=cfg.get("base_url") or "https://api.deepseek.com")
    r = c.chat.completions.create(
        model=cfg.get("model") or "deepseek-chat",
        messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
        temperature=0.2, max_tokens=max_tokens)
    return r.choices[0].message.content.strip()


def parse_json(raw):
    raw = re.sub(r"^```(?:json)?\s*", "", raw.strip())
    raw = re.sub(r"\s*```$", "", raw)
    m = re.search(r"\{[\s\S]*\}", raw)
    if not m:
        raise ValueError("模型未返回 JSON")
    return json.loads(m.group(0))


# ---------- audit ----------

def cmd_audit(cfg):
    cards = load_cards()
    if len(cards) < 2:
        print("[i] 卡片太少（%d 张），先积累一些再体检" % len(cards))
        return 0

    rows = "\n".join(
        f"- {c['term']} | 领域 {c['domain'] or '未分类'} | 别名 {'、'.join(c['aliases']) or '无'} | "
        f"链接 {len(c['links'])} | {one_liner(c['text'])}"
        for c in cards)

    print(f"[i] 共 {len(cards)} 张卡片，正在体检…")
    report = parse_json(llm(cfg, AUDIT_PROMPT, f"概念清单：\n{rows}\n\n请输出 JSON。"))

    REPORTS.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M")
    out = REPORTS / f"体检-{stamp}.md"

    L = [f"# 体检报告 {datetime.now().strftime('%Y-%m-%d %H:%M')}", "",
         f"> 共 {len(cards)} 张卡片", ""]

    def sec(title, key, fmt):
        items = report.get(key) or []
        L.append(f"## {title}（{len(items)}）")
        L.append("")
        if not items:
            L.append("_无_")
        for it in items:
            L.append(fmt(it))
        L.append("")

    sec("重复可合并", "duplicates",
        lambda x: f"- 保留 **{x.get('keep')}**，并入 {'、'.join(x.get('merge') or [])} — {x.get('reason','')}")
    sec("矛盾或失效", "conflicts",
        lambda x: f"- {'、'.join(x.get('terms') or [])}：{x.get('issue','')} → 建议：{x.get('suggest','')}")
    sec("建议下架", "obsolete",
        lambda x: f"- **{x.get('term')}** — {x.get('reason','')}")
    sec("领域错位", "misplaced",
        lambda x: f"- **{x.get('term')}**：{x.get('from','')} → {x.get('to','')} — {x.get('reason','')}")
    sec("孤岛卡片", "orphans",
        lambda x: f"- **{x.get('term')}** — {x.get('reason','')}")
    sec("缺失关联", "missing_links",
        lambda x: f"- {x['pair'][0]} ↔ {x['pair'][1]}（{x.get('relation','')}）" if x.get("pair") else "")

    L += ["## 怎么处理", "",
          "```bat",
          "维护.bat merge 保留的词条 被并入的词条",
          "维护.bat prune 词条",
          "```", "",
          "体检只出报告，不动文件。确认后再执行上面的命令。"]

    out.write_text("\n".join(L), encoding="utf-8")
    print(f"[✓] 报告已生成：{out}")
    for k, name in [("duplicates", "重复可合并"), ("conflicts", "矛盾或失效"),
                    ("obsolete", "建议下架"), ("misplaced", "领域错位"),
                    ("orphans", "孤岛"), ("missing_links", "缺失关联")]:
        n = len(report.get(k) or [])
        if n:
            print(f"    {name}：{n} 处")
    return 0


# ---------- merge ----------

def find_card(cards, name):
    name = name.strip()
    for c in cards:
        if c["stem"] == name or c["term"] == name:
            return c
    for c in cards:
        if name in c["aliases"] or name.lower() in [a.lower() for a in c["aliases"]]:
            return c
    return None


def cmd_merge(cfg, names):
    if len(names) < 2:
        print("[!] 用法：维护.bat merge 保留的词条 被并入的词条 [更多]")
        return 1
    cards = load_cards()
    keep = find_card(cards, names[0])
    if not keep:
        print(f"[!] 找不到：{names[0]}")
        return 1
    drops = []
    for n in names[1:]:
        c = find_card(cards, n)
        if c and c["stem"] != keep["stem"]:
            drops.append(c)
    if not drops:
        print("[!] 没有可并入的卡片")
        return 1

    print(f"保留：{keep['term']}（{keep['stem']}）")
    for d in drops:
        print(f"并入：{d['term']}（{d['stem']}）")

    merged_body = ""
    for d in drops:
        body = re.sub(r"^---[\s\S]*?---\s*", "", d["text"]).strip()
        merged_body += f"\n\n<!-- 原卡片 {d['stem']} -->\n" + body

    prompt = f"""把下面几张概念卡合并成一张。保留主卡的框架，把其他卡里**独有的信息**并进来，重复的删掉，不要机械拼接。

主卡（{keep['term']}）：
{keep['text'][:4000]}

需要并入的内容：
{merged_body[:6000]}

输出合并后的完整 markdown（含 frontmatter），aliases 要把被合并的词条名加进去，domain 取更准确的那个。只输出 markdown，不要解释。"""

    print("\n[i] 正在合并…")
    merged = llm(cfg, "你是知识库维护员，负责合并重复概念卡，保证信息不丢、不重复。", prompt, 4000)
    merged = re.sub(r"^```(?:markdown)?\s*", "", merged)
    merged = re.sub(r"\s*```$", "", merged)

    if not ask_confirm("确认写入？原卡片会移到 _废弃"):
        print("已取消")
        return 1

    keep["path"].write_text(merged, encoding="utf-8")
    TRASH.mkdir(exist_ok=True)
    day = TRASH / datetime.now().strftime("%Y-%m")
    day.mkdir(parents=True, exist_ok=True)
    for d in drops:
        shutil.move(str(d["path"]), str(day / d["path"].name))

    # 全库替换双链
    replaced = 0
    for f in CONCEPTS.glob("*.md"):
        t = f.read_text(encoding="utf-8", errors="ignore")
        new = t
        for d in drops:
            new = new.replace(f"[[{d['stem']}]]", f"[[{keep['stem']}]]")
        if new != t:
            f.write_text(new, encoding="utf-8")
            replaced += 1

    print(f"[✓] 已合并，{replaced} 张卡片里的双链已改指主卡")
    return 0


# ---------- prune ----------

def cmd_prune(names):
    cards = load_cards()
    todo = [c for c in (find_card(cards, n) for n in names) if c]
    if not todo:
        print("[!] 没有找到要下架的卡片")
        return 1
    for c in todo:
        print(f"下架：{c['term']}（{c['stem']}）")
    if not ask_confirm("确认下架？文件会移到 _废弃，可随时找回"):
        print("已取消")
        return 1
    day = TRASH / datetime.now().strftime("%Y-%m")
    day.mkdir(parents=True, exist_ok=True)
    for c in todo:
        shutil.move(str(c["path"]), str(day / c["path"].name))
    print(f"[✓] 已下架 {len(todo)} 张，移到 {day}")
    return 0


# ---------- ask ----------

def cmd_ask(cfg, question, save=True):
    cards = load_cards()
    if not cards:
        print("[i] 库里还没有卡片")
        return 0
    q = question.lower()
    scored = []
    for c in cards:
        score = 0
        if c["term"].lower() in q:
            score += 10
        for a in c["aliases"]:
            if a.lower() in q:
                score += 8
        for w in re.findall(r"[\u4e00-\u9fa5]{2,}|[a-zA-Z]{3,}", q):
            if w in c["text"]:
                score += 1
        scored.append((score, c))
    scored.sort(key=lambda x: -x[0])
    ctx = [c for s, c in scored[:5] if s > 0] or [c for s, c in scored[:3]]

    context = "\n\n".join(f"### {c['term']}\n{c['text'][:2500]}" for c in ctx)
    print(f"[i] 参照 {len(ctx)} 张卡片：{'、'.join(c['term'] for c in ctx)}\n")
    ans = llm(cfg,
              "你是用户的个人知识库助手。只根据给定卡片回答，卡片里没有的信息要明说没有，不要编。回答简洁，中文，必要时列出相关概念名。",
              f"知识库卡片：\n{context}\n\n问题：{question}", 1500)
    print(ans)

    old = QA_LOG.read_text(encoding="utf-8", errors="ignore") if QA_LOG.exists() else "# 问答记录\n"
    block = (f"\n## {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n**问：** {question}\n\n"
             f"**答：** {ans}\n\n_参照：{'、'.join('[[' + c['stem'] + ']]' for c in ctx)}_\n")
    QA_LOG.write_text(old + block, encoding="utf-8")
    print("\n[i] 已存入 问答记录.md")

    if save:
        ANALYSIS.mkdir(exist_ok=True)
        title = re.sub(r"[？?。！!]+$", "", question).strip()[:28] or "问答沉淀"
        safe = re.sub(r'[\\/:*?"<>|]', "-", title)
        f = ANALYSIS / f"{safe}.md"
        n = 2
        while f.exists():
            f = ANALYSIS / f"{safe}-{n}.md"
            n += 1
        links = "\n".join(f"- [[{c['stem']}]] — {c['domain'] or '相关'}" for c in ctx)
        card = (f"---\ntitle: {title}\nkind: analysis\ndomain: {ctx[0]['domain'] if ctx else ''}\n"
                f"created: {datetime.now().strftime('%Y-%m-%d')}\nsource: 问答沉淀\n---\n\n"
                f"# {title}\n\n> 问题：{question}\n\n## 结论\n\n{ans}\n\n## 依据\n\n{links}\n")
        f.write_text(card, encoding="utf-8")
        print(f"[i] 已沉淀为分析卡片：分析/{f.name}")
    return 0


REVIEW_PROMPT = """你是知识库的综述撰写者。给定当前全部概念（含领域、一句话说明），写一份知识体系综述。

要求：
1. 先给出体系全貌：现在主要覆盖哪几个领域，各自的重心是什么。
2. 按领域讲清核心概念之间的结构关系（谁是谁的前置、谁和谁互补）。
3. 指出明显的空白：某个领域概念过少、只有孤立术语没有方法、缺少实践类内容等。
4. 指出可能的冗余或重叠。
5. 不要罗列所有概念名，要抽象出结构。

用 markdown，不超过 1200 字，标题层级用 ##，不要写一级标题。"""


def cmd_review(cfg):
    cards = load_cards()
    if len(cards) < 3:
        print(f"[i] 只有 {len(cards)} 张卡片，先积累一些再写综述")
        return 0
    rows = "\n".join(f"- [{c['domain'] or '未分类'}] {c['term']}：{one_liner(c['text'], 60)}"
                     for c in cards)
    print(f"[i] 基于 {len(cards)} 张卡片撰写综述…")
    body = llm(cfg, REVIEW_PROMPT, f"概念清单：\n{rows}", 2500)

    ANALYSIS.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m")
    out = ANALYSIS / f"综述-{stamp}.md"
    content = (f"---\ntitle: 知识体系综述 {stamp}\nkind: review\ncreated: "
               f"{datetime.now().strftime('%Y-%m-%d')}\nsource: 自动生成\n---\n\n"
               f"# 知识体系综述 · {stamp}\n\n> 基于 {len(cards)} 个概念生成，"
               f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n{body}\n")
    out.write_text(content, encoding="utf-8")
    print(f"[✓] 已生成：分析/{out.name}")
    return 0


# ---------- rebuild ----------

def cmd_rebuild():
    by_dom = C.rebuild_index()
    C.rebuild_moc(by_dom)
    C.rebuild_home(by_dom)
    total = sum(len(v) for v in by_dom.values())
    print(f"[✓] 索引已重建，{total} 个概念")
    return 0


# ---------- 交互菜单 ----------

def need_key(cfg, hint=""):
    if not cfg.get("api_key"):
        print("\n[!] 还没配置 api_key")
        print("    编辑：" + str(CONFIG))
        print('    内容：{"api_key": "sk-xxx", "base_url": "https://api.deepseek.com", "model": "deepseek-chat"}')
        return False
    return True


def cmd_menu():
    while True:
        cfg = C.load_json(CONFIG, {})
        print("\n" + "=" * 46)
        print("  知识库  " + ("（已配模型）" if cfg.get("api_key") else "（未配模型）"))
        print("=" * 46)
        print("  1  整理新素材（从 _在编 抽概念）")
        print("  2  体检（查重复 / 矛盾 / 失效 / 错位）")
        print("  3  合并概念")
        print("  4  下架概念")
        print("  5  问知识库")
        print("  6  重建索引")
        print("  7  写知识综述")
        print("  0  退出")
        try:
            ch = input("\n选择：").strip()
        except EOFError:
            return 0

        if ch == "0":
            return 0
        elif ch == "1":
            if not need_key(cfg):
                continue
            subprocess.run([sys.executable, str(OFFICE / "curator.py")], cwd=str(OFFICE))
        elif ch == "2":
            if not need_key(cfg):
                continue
            cmd_audit(cfg)
        elif ch == "3":
            if not need_key(cfg):
                continue
            a = input("保留哪个词条：").strip()
            b = input("并入哪个（可多个，空格分隔）：").strip().split()
            if a and b:
                cmd_merge(cfg, [a] + b)
        elif ch == "4":
            names = input("下架哪些词条（空格分隔）：").strip().split()
            if names:
                cmd_prune(names)
        elif ch == "5":
            if not need_key(cfg):
                continue
            q = input("问题：").strip()
            if q:
                cmd_ask(cfg, q)
        elif ch == "6":
            cmd_rebuild()
        elif ch == "7":
            if not need_key(cfg):
                continue
            cmd_review(cfg)


# ---------- main ----------

def main():
    args = sys.argv[1:]
    if args and args[0] == "menu":
        return cmd_menu()
    if not args:
        print(__doc__)
        return 1
    cmd, rest = args[0], args[1:]

    if cmd == "rebuild":
        return cmd_rebuild()

    cfg = C.load_json(CONFIG, {})
    if not cfg.get("api_key"):
        print("[!] 未配置 api_key：", CONFIG)
        if cmd in ("merge", "prune"):
            print("    （合并与下架也依赖模型做内容合并）")
        return 2

    if cmd == "audit":
        return cmd_audit(cfg)
    if cmd == "merge":
        return cmd_merge(cfg, rest)
    if cmd == "prune":
        return cmd_prune(rest)
    if cmd == "ask":
        if not rest:
            print("[!] 用法：维护.bat ask \"你的问题\"")
            return 1
        return cmd_ask(cfg, " ".join(rest))
    if cmd == "review":
        return cmd_review(cfg)

    print(f"[!] 未知命令：{cmd}")
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main())
