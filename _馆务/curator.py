#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
知识库 · 概念整理员

把 _在编 里的一篇笔记拆成若干概念卡片：一个名词一张卡，含定义、用处、要点、关联、自测。

用法:
    python curator.py              整理 _在编 全部
    python curator.py --dry-run    只打印要建/要补的概念，不写文件
    python curator.py --file x.md  只处理某一篇
"""
import sys
import re
import json
import shutil
from pathlib import Path
from datetime import datetime

try:
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
except Exception:
    pass

BASE = Path(__file__).resolve().parent.parent
INBOX = BASE / "_在编"
ARCHIVE = BASE / "_典藏"
OFFICE = BASE / "_馆务"
CONCEPTS = BASE / "概念"
MOC_DIR = BASE / "MOC"
CONFIG = OFFICE / "config.json"
INDEX_MD = BASE / "概念索引.md"
HOME_MD = BASE / "首页.md"
LOG_MD = OFFICE / "整理日志.md"

SYSTEM_PROMPT = """你是个人知识库的概念整理员。用户在看视频、读资料时积累素材，你负责把它拆成可复用的概念卡片。

抽取规则：
1. 只抽「值得单独查阅的概念」，不是所有词。优先抽：专门术语、方法、工具、框架、模型、指标、关键人物/产品。
2. 一个概念 = 一个名词。不要把一句话、一个观点当成概念。观点写进概念的「要点」里。
3. 一篇笔记通常抽 3-8 个概念。宁可少而准，不要凑数。
4. **不要给单个函数参数或单个 API 调用建卡**。像「sep 参数」「ignore_index 参数」这类，写进所属函数或主题卡的「关键要点」里；「np.exp」「head()」「dtypes 属性」这类单个调用也并入主题卡（如「Numpy 通用函数」「Pandas 数据查看」）。只有当一个函数本身就是一整套方法体系时（如 groupby、pivot_table、merge、loc/iloc），才单独建卡。
5. 概念之间要有真实关联（上下位、前置、对比、组合），不要硬拉。
6. 定义必须一句话说清，不要"XX是指……的一个过程"这种空转。
7. 自测题要能检验是否真懂，不要考记忆性细节。

领域用层级路径，如 "计算机/AI/大模型"、"商业/产品/增长"。层级不要超过 3 段。

只输出 JSON：
{
  "concepts": [
    {
      "term": "概念名（尽量用通用叫法）",
      "aliases": ["英文名或别名"],
      "kind": "concept | method | tool | model | metric | person | product",
      "domain": "一级/二级/三级",
      "definition": "一句话定义，40 字以内",
      "explain": "2-4 句展开，说清它是什么、解决什么问题",
      "usage": ["什么场景用", "解决什么问题"],
      "points": ["关键要点，3-5 条，每条 40 字内"],
      "boundary": "适用边界或易混淆点，没有就留空字符串",
      "related": [{"term": "关联概念名", "relation": "上位概念|下位概念|前置知识|对比项|组合使用"}],
      "quiz": [{"q": "问题", "a": "答案"}]
    }
  ]
}"""


# ---------- 基础 ----------

def load_json(p, d):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return d


def norm_name(term):
    t = re.sub(r'[\\/:*?"<>|#^\[\]]', "", term).strip()
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"\.md$", "", t, flags=re.I)  # 避免 AGENTS.md 变成 AGENTS.md.md
    return t[:40]


def scan_concepts():
    """返回 {规范化名: {path, term, domain, aliases}}"""
    out = {}
    if not CONCEPTS.is_dir():
        return out
    for f in CONCEPTS.glob("*.md"):
        head = ""
        try:
            head = f.read_text(encoding="utf-8", errors="ignore")[:800]
        except Exception:
            pass
        term = f.stem
        m = re.search(r"^term:\s*(.+)$", head, re.M)
        if m:
            term = m.group(1).strip()
        dm = re.search(r"^domain:\s*(.+)$", head, re.M)
        am = re.search(r"^aliases:\s*\[(.*?)\]", head, re.M)
        aliases = [x.strip() for x in am.group(1).split(",") if x.strip()] if am else []
        out[f.stem] = {"path": f, "term": term, "domain": (dm.group(1).strip() if dm else ""),
                       "aliases": aliases}
    return out


def pick_meta(md_path):
    """取这篇笔记的来源标题与链接。

    BiliNote 的产物是 <task>.json + <task>_audio.json：
    标题在 audio_meta.title，BV号与分P在 audio_meta.video_id（形如 BVxxx_p7），
    正文首行还有「> 来源链接：…」。三处依次兜底，别再让卡片写成「来源未知」。
    """
    stem = md_path.stem.replace("_markdown", "")
    for cand in (md_path.with_suffix(".json"), md_path.parent / (stem + ".json"),
                 md_path.parent / (stem + "_audio.json")):
        if not cand.exists():
            continue
        try:
            d = json.loads(cand.read_text(encoding="utf-8", errors="ignore"))
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        title = d.get("video_title") or d.get("title") or ""
        url = d.get("video_url") or d.get("url") or ""
        am = d.get("audio_meta") or {}
        if isinstance(am, dict):
            title = title or am.get("title") or ""
            vid = am.get("video_id") or ""
            if not url and vid:
                bv, _, page = vid.partition("_p")
                url = f"https://www.bilibili.com/video/{bv}"
                if page.isdigit():
                    url += f"?p={page}"
        if title or url:
            return title, url

    # 最后兜底：正文首行的「> 来源链接：https://…」
    try:
        head = md_path.read_text(encoding="utf-8", errors="ignore")[:600]
        m = re.search(r"来源链接[:：]\s*(https?://\S+)", head)
        if m:
            return "", m.group(1)
    except Exception:
        pass
    return "", ""


def call_llm(cfg, prompt):
    from openai import OpenAI
    # timeout 必须设：机器休眠会断掉连接，不设时 SDK 会永久挂起
    c = OpenAI(api_key=cfg["api_key"],
               base_url=cfg.get("base_url") or "https://api.deepseek.com",
               timeout=180.0, max_retries=2)
    r = c.chat.completions.create(
        model=cfg.get("model") or "deepseek-chat",
        messages=[{"role": "system", "content": SYSTEM_PROMPT},
                  {"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=8000,
    )
    return r.choices[0].message.content.strip()


def parse_json(raw):
    """容错解析：模型输出被截断时，仍然把已完整的 concept 对象捞出来。"""
    raw = re.sub(r"^```(?:json)?\s*", "", raw.strip())
    raw = re.sub(r"\s*```$", "", raw)
    m = re.search(r"\{[\s\S]*\}", raw)
    text = m.group(0) if m else raw
    try:
        return json.loads(text)
    except Exception:
        pass

    # 退化路径：逐个 raw_decode 数组里的对象
    idx = text.find('"concepts"')
    start = text.find("[", idx) if idx >= 0 else text.find("[")
    if start < 0:
        raise ValueError("模型未返回可解析的 JSON")
    dec = json.JSONDecoder()
    items = []
    i = start + 1
    while i < len(text):
        while i < len(text) and text[i] in " \t\r\n,":
            i += 1
        if i >= len(text) or text[i] == "]":
            break
        try:
            obj, end = dec.raw_decode(text, i)
        except Exception:
            break
        items.append(obj)
        i = end
    if not items:
        raise ValueError("JSON 截断且无可恢复的对象")
    return {"concepts": items}



# ---------- 卡片 ----------

def build_card(c, meta, existing=False):
    today = datetime.now().strftime("%Y-%m-%d")
    title, url = meta
    tags = ["概念/" + (c.get("kind") or "concept")]
    d = c.get("domain") or ""
    if d:
        tags.append("领域/" + d.split("/")[0])
    L = ["---",
         f"term: {c['term']}",
         f"aliases: [{', '.join(c.get('aliases') or [])}]",
         f"kind: {c.get('kind') or 'concept'}",
         f"domain: {d}",
         f"tags: [{', '.join(tags)}]",
         f"created: {today}",
         f"updated: {today}",
         "---", "",
         f"# {c['term']}", ""]
    if c.get("aliases"):
        L += [f"> 别名：{'、'.join(c['aliases'])}", ""]
    L += [f"**{c.get('definition','')}**", ""]
    if c.get("explain"):
        L += ["## 解释", "", c["explain"], ""]
    if c.get("usage"):
        L += ["## 有什么用", ""] + [f"- {u}" for u in c["usage"]] + [""]
    if c.get("points"):
        L += ["## 关键要点", ""] + [f"- {p}" for p in c["points"]] + [""]
    if c.get("boundary"):
        L += ["## 边界与易混淆", "", c["boundary"], ""]
    rel = c.get("related") or []
    if rel:
        L += ["## 关联", ""]
        for r in rel:
            t = norm_name(r.get("term", ""))
            if t:
                L.append(f"- [[{t}]] — {r.get('relation','相关')}")
        L.append("")
    quiz = c.get("quiz") or []
    if quiz:
        L += ["## 自测", ""]
        for q in quiz:
            if q.get("q"):
                L.append(f"{q['q']}::{q.get('a','')}")
        L.append("")
    L += ["## 出处", ""]
    if url:
        L.append(f"- [{title or '来源'}]({url}) · {today}")
    else:
        L.append(f"- {title or '来源未知'} · {today}")
    L.append("")
    return "\n".join(L)


def append_to_card(path, c, meta):
    """已有概念：追加新来源和补充要点，不改原有定义

    同一天多次补充会合并进同一个「### 补充 · 日期」小节，
    否则批量整理时同一张卡会出现十几个同名标题。
    """
    today = datetime.now().strftime("%Y-%m-%d")
    title, url = meta
    text = path.read_text(encoding="utf-8", errors="ignore")
    text = re.sub(r"(?m)^updated:.*$", f"updated: {today}", text, count=1)

    body = []
    if c.get("explain"):
        body.append(c["explain"])
        body.append("")
    for p in (c.get("points") or [])[:3]:
        body.append(f"- {p}")
    for q in (c.get("quiz") or [])[:2]:
        if q.get("q"):
            body.append(f"{q['q']}::{q.get('a','')}")
    if url:
        body.append(f"- 出处：[{title or '来源'}]({url}) · {today}")

    heading = f"### 补充 · {today}"
    chunk = "\n".join(body).strip("\n")

    if heading in text:
        # 已有今天的补充小节：插到该小节末尾
        start = text.index(heading) + len(heading)
        m = re.search(r"(?m)^#{2,3} ", text[start:])
        end = start + m.start() if m else len(text)
        text = text[:end].rstrip("\n") + "\n\n" + chunk + "\n\n" + text[end:].lstrip("\n")
    else:
        block = "\n".join(["", heading, ""] + body + [""])
        if "## 出处" in text:
            text = text.replace("## 出处", block + "\n## 出处", 1)
        else:
            text = text + "\n" + block
    path.write_text(text, encoding="utf-8")


# ---------- 索引 ----------

def rebuild_index():
    items = []
    for stem, info in scan_concepts().items():
        items.append((info["domain"] or "未分类", info["term"], stem))
    items.sort()
    by_dom = {}
    for dom, term, stem in items:
        by_dom.setdefault(dom, []).append((term, stem))

    L = ["# 概念索引", "",
         f"> 共 {len(items)} 个概念 · 更新于 {datetime.now().strftime('%Y-%m-%d %H:%M')}", ""]
    for dom in sorted(by_dom):
        L.append(f"## {dom}（{len(by_dom[dom])}）")
        L.append("")
        for term, stem in sorted(by_dom[dom]):
            L.append(f"- [[{stem}]]" + ("" if stem == term else f" — {term}"))
        L.append("")
    INDEX_MD.write_text("\n".join(L) + "\n", encoding="utf-8")
    return by_dom


def rebuild_moc(by_dom):
    MOC_DIR.mkdir(exist_ok=True)
    tops = {}
    for dom, arr in by_dom.items():
        top = dom.split("/")[0] if dom and dom != "未分类" else "未分类"
        tops.setdefault(top, []).extend([(dom, a) for a in arr])

    for top, arr in tops.items():
        L = [f"# {top}", "",
             f"> 本领域 {len(arr)} 个概念 · 更新于 {datetime.now().strftime('%Y-%m-%d')}", ""]
        sub = {}
        for dom, (term, stem) in arr:
            sub.setdefault(dom, []).append((term, stem))
        for dom in sorted(sub):
            if dom != top:
                L += [f"## {dom}", ""]
            for term, stem in sorted(sub[dom]):
                L.append(f"- [[{stem}]]" + ("" if stem == term else f" — {term}"))
            L.append("")
        (MOC_DIR / f"{top}.md").write_text("\n".join(L), encoding="utf-8")
    return tops


def pending_links():
    """被双链引用但还没有卡片的概念名。别名和 MOC 文件名也算已存在。"""
    cards = scan_concepts()
    exist = set(cards.keys())
    for info in cards.values():
        exist.add(info["term"])
        exist.update(info["aliases"])
    if MOC_DIR.is_dir():
        exist.update(f.stem for f in MOC_DIR.glob("*.md"))
    exist.update(f.stem for f in BASE.glob("*.md"))  # 首页、概念索引等
    exist.discard("")

    refs = {}
    for f in list(CONCEPTS.glob("*.md")) + [INDEX_MD, HOME_MD]:
        if not f.exists():
            continue
        try:
            t = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for m in re.finditer(r"\[\[([^\]|#]+)", t):
            name = m.group(1).strip()
            if name and name not in exist:
                refs[name] = refs.get(name, 0) + 1
    return sorted(refs.items(), key=lambda x: -x[1])


def rebuild_home(by_dom):
    total = sum(len(v) for v in by_dom.values())
    tops = {}
    for dom, arr in by_dom.items():
        t = dom.split("/")[0] if dom and dom != "未分类" else "未分类"
        tops[t] = tops.get(t, 0) + len(arr)
    L = ["# 首页", "",
         f"> 概念 **{total}** 个 · 领域 **{len(tops)}** 个",
         f"> 更新于 {datetime.now().strftime('%Y-%m-%d %H:%M')}", "",
         "## 入口", "",
         "- [[概念索引]] — 按领域排列的全部概念",
         "- [[AGENTS]] — 操作规则（AI 按这个干活）",
         "- `MOC/` — 各领域地图",
         "- `_在编/` — 待整理的新素材",
         ""]
    if tops:
        L += ["## 领域", ""]
        for t in sorted(tops):
            L.append(f"- [[{t}]] — {tops[t]} 个概念")
        L.append("")

    ana = BASE / "分析"
    if ana.is_dir():
        items = sorted(ana.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)[:6]
        if items:
            L += ["## 分析与综述", ""]
            for p in items:
                L.append(f"- [[{p.stem}]]")
            L.append("")
    pend = pending_links()
    if pend:
        L += ["## 待补全词条", "",
              "_这些概念被其他卡片引用，但还没有自己的卡片：_", ""]
        for name, n in pend[:20]:
            L.append(f"- [[{name}]]（被引用 {n} 次）")
        L.append("")
    else:
        L += ["## 待补全词条", "", "_暂无_", ""]
    HOME_MD.write_text("\n".join(L), encoding="utf-8")


def write_log(rows):
    if not rows:
        return
    old = LOG_MD.read_text(encoding="utf-8", errors="ignore") if LOG_MD.exists() else "# 整理日志\n"
    old = re.sub(r"^# 整理日志\s*\n+", "", old)
    new = "".join(f"- {datetime.now().strftime('%Y-%m-%d %H:%M')} | {r}\n" for r in rows)
    LOG_MD.write_text("# 整理日志\n\n" + new + old, encoding="utf-8")


# ---------- 主流程 ----------

def process(cfg, md_path, known, dry_run=False):
    body = md_path.read_text(encoding="utf-8", errors="ignore")
    meta = pick_meta(md_path)

    exist_lines = "\n".join(
        f"- {v['term']}（{v['domain']}）{' 别名:' + '、'.join(v['aliases']) if v['aliases'] else ''}"
        for v in known.values()) or "_（空库）_"

    prompt = f"""已有概念（用于判断哪些是新的、哪些要补充）：
{exist_lines}

素材来源：{md_path.name}
视频标题：{meta[0] or '（未知）'}
链接：{meta[1] or '（未知）'}

正文：
---
{body[:9000]}
---

请抽取概念并输出 JSON。已有概念如果这次有新信息，也要一并输出（会走补充流程）。"""

    data = parse_json(call_llm(cfg, prompt))
    concepts = data.get("concepts") or []
    rows, created, updated = [], [], []

    for c in concepts:
        term = norm_name(c.get("term", ""))
        if not term:
            continue
        c["term"] = term
        hit = None
        for stem, info in known.items():
            if stem == term or term == info["term"] or term in info["aliases"]:
                hit = info
                break

        if hit:
            if not dry_run:
                append_to_card(hit["path"], c, meta)
            updated.append(term)
        else:
            path = CONCEPTS / f"{term}.md"
            if not dry_run:
                path.write_text(build_card(c, meta), encoding="utf-8")
            created.append(term)
            known[term] = {"path": path, "term": term,
                           "domain": c.get("domain", ""), "aliases": c.get("aliases") or []}

    if created or updated:
        rows.append(f"{md_path.name} → 新建 {len(created)}（{'、'.join(created) or '—'}）"
                    f" · 补充 {len(updated)}（{'、'.join(updated) or '—'}）")
    return created, updated, rows


def archive(md_path):
    """把这一批任务的所有产物一起归档：正文、元数据、转写、状态文件。"""
    day = ARCHIVE / datetime.now().strftime("%Y-%m")
    day.mkdir(parents=True, exist_ok=True)
    task_id = md_path.stem.replace("_markdown", "")
    for p in md_path.parent.glob(task_id + "*"):
        if p.is_file():
            try:
                shutil.move(str(p), str(day / p.name))
            except Exception:
                pass


def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    only = args[args.index("--file") + 1] if "--file" in args else None

    cfg = load_json(CONFIG, {})
    if not cfg.get("api_key"):
        print("[!] 未配置 api_key：", CONFIG)
        print('    {"api_key": "sk-xxx", "base_url": "https://api.deepseek.com", "model": "deepseek-chat"}')
        return 2

    CONCEPTS.mkdir(exist_ok=True)
    targets = sorted(INBOX.glob("*.md")) if not only else [INBOX / only]
    targets = [t for t in targets if t.exists()]
    if not targets:
        print("[i] _在编 为空")
        return 0

    print(f"[i] 待整理 {len(targets)} 篇{'（预览）' if dry_run else ''}")
    known = scan_concepts()
    all_rows = []
    for md in targets:
        print(f"\n-> {md.name}")
        try:
            created, updated, rows = process(cfg, md, known, dry_run)
            if created:
                print(f"   新建 {len(created)}：{'、'.join(created)}")
            if updated:
                print(f"   补充 {len(updated)}：{'、'.join(updated)}")
            if not created and not updated:
                print("   没有抽到概念")
            all_rows += rows
            if not dry_run:
                archive(md)
                known = scan_concepts()
        except Exception as e:
            print(f"   [!] 失败：{type(e).__name__}: {e}")

    if not dry_run:
        by_dom = rebuild_index()
        rebuild_moc(by_dom)
        rebuild_home(by_dom)
        write_log(all_rows)
        total = sum(len(v) for v in by_dom.values())
        print(f"\n[i] 索引已刷新：{total} 个概念，见 首页.md / 概念索引.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
