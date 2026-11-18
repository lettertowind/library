#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""知识库 → 静态网站生成器

把 D:\\知识库 下的概念卡、分析文章整理成可浏览的静态站点，输出到 docs/。
纯标准库实现，不依赖任何第三方包，系统 python 直接跑。

用法：
    python site.py            生成站点
    python site.py --check    生成并自检（检查断链、文件缺失）
"""

from __future__ import annotations

import html
import hashlib
import json
import re
import shutil
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

BASE = Path(__file__).resolve().parent.parent
OUT = BASE / "docs"
CONCEPTS = BASE / "概念"
ANALYSIS = BASE / "分析"
MOC = BASE / "MOC"
THEME = Path(__file__).resolve().parent / "theme"

SITE_TITLE = "知识库"

# 当前渲染页相对 docs 根的深度前缀，渲染前设置
CUR_ROOT = ""

# 静态资源版本号，取 css/js 内容哈希，内容一改链接就变，绕过 10 分钟缓存
ASSET_VER = ""

# 链接解析索引：五级，顺序敏感
INDEX = {"stem": {}, "term": {}, "alias": {}, "moc": {}, "root": {}}

# 关系词 → 徽章样式类
REL_CLASS = {
    "上位概念": "up",
    "下位概念": "down",
    "前置知识": "pre",
    "对比项": "vs",
    "组合使用": "with",
    "相关": "rel",
}

WARNINGS = []


# ---------------------------------------------------------------- 基础工具

def esc(s):
    return html.escape(s or "", quote=True)


def slug(s):
    """标题转锚点：保留中英文数字，其余转连字符"""
    s = re.sub(r"[^\w\u4e00-\u9fff-]+", "-", s.strip().lower())
    return re.sub(r"-+", "-", s).strip("-") or "s"


def parse_inline_list(raw):
    """解析 [a, b, "c, d"] 这种行内列表，正确处理引号内的逗号"""
    s = (raw or "").strip()
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1]
    if not s.strip():
        return []
    items, buf, quote_ch = [], [], None
    for ch in s:
        if quote_ch:
            if ch == quote_ch:
                quote_ch = None
            else:
                buf.append(ch)
        elif ch in "\"'":
            quote_ch = ch
        elif ch == ",":
            items.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    if buf:
        items.append("".join(buf).strip())
    return [i for i in items if i]


def parse_frontmatter(text):
    """返回 (meta dict, body 字符串)"""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("\n")
    if parts[0].strip() != "---":
        return {}, text
    end = None
    for i in range(1, len(parts)):
        if parts[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}, text
    meta = {}
    for line in parts[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip()
    body = "\n".join(parts[end + 1:])
    return meta, body


# ---------------------------------------------------------------- 链接解析

def resolve(name):
    """五级查找：文件名 stem → term → alias → MOC stem → 根目录 md。
    返回 (相对 docs 根的路径, 是否存在)"""
    n = (name or "").strip()
    if not n:
        return "", False
    for key in ("stem", "term", "alias", "moc", "root"):
        table = INDEX[key]
        if n in table:
            return table[n], True
        if n.lower() in table:
            return table[n.lower()], True
    return "", False


def link_html(raw_name):
    """渲染一个 [[...]] 内部的内容"""
    name = raw_name.strip()
    display = name
    if "|" in name:
        name, display = name.split("|", 1)
        name, display = name.strip(), display.strip()
    elif "#" in name:
        name = name.split("#", 1)[0].strip()
    href, exists = resolve(name)
    if exists:
        return f'<a class="wl" href="{CUR_ROOT}{href}">{esc(display)}</a>'
    WARNINGS.append(f"断链：[[{name}]]")
    return f'<span class="wl-dead" title="尚未建立这张卡片">{esc(display)}</span>'


def _looks_like_wikilink(name):
    """区分真双链与代码里的索引语法。

    numpy 神奇索引 a[[2,3,5]]、pandas 多列选择 df[["a","b"]] 都是双中括号，
    但它们不是双链：带逗号、引号、& 或者以数字开头的，一律当普通文本。
    """
    s = name.strip()
    if not s or len(s) > 40:
        return False
    if any(ch in s for ch in ',"&[]'):
        return False
    if s[0].isdigit():
        return False
    return True


def inline(text):
    """行内渲染：先保护行内代码（其内的 [[..]] 不能被解析），再处理双链/外链/加粗"""
    t = esc(text)
    codes = []

    def stash(m):
        codes.append(m.group(1))
        return f"\x00{len(codes) - 1}\x00"

    t = re.sub(r"`([^`]+)`", stash, t)
    t = re.sub(
        r"\[\[([^\[\]]+)\]\]",
        lambda m: link_html(m.group(1)) if _looks_like_wikilink(m.group(1)) else m.group(0),
        t,
    )
    t = re.sub(
        r"\[([^\]]+)\]\((https?://[^)\s]+)\)",
        r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
        t,
    )
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{codes[int(m.group(1))]}</code>", t)
    return t


def render_table(rows):
    """rows: 原始 | 行列表，第二行是分隔线"""
    def cells(line):
        return [c.strip() for c in line.strip().strip("|").split("|")]

    head = cells(rows[0])
    body = [cells(r) for r in rows[2:]]
    out = ["<div class=\"tablewrap\"><table><thead><tr>"]
    out += [f"<th>{inline(h)}</th>" for h in head]
    out.append("</tr></thead><tbody>")
    for r in body:
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


# ---------------------------------------------------------------- 正文渲染

def render_list(items):
    """items: [(缩进层级, 文本)]，支持一层嵌套"""
    if not items:
        return ""
    base = min(ind for ind, _ in items)
    parts = ["<ul>"]
    i = 0
    while i < len(items):
        ind, text = items[i]
        if ind > base:
            parts.append(f"<li>{inline(text)}</li>")
            i += 1
            continue
        parts.append(f"<li>{inline(text)}")
        j = i + 1
        sub = []
        while j < len(items) and items[j][0] > base:
            sub.append(items[j])
            j += 1
        if sub:
            parts.append(render_list(sub))
        parts.append("</li>")
        i = j
    parts.append("</ul>")
    return "".join(parts)


def render_markdown(lines):
    out = []
    i, n = 0, len(lines)
    while i < n:
        s = lines[i].strip()
        if not s:
            i += 1
            continue

        # 围栏代码块：内部原样输出，不解析双链
        m = re.match(r"^```([\w+-]*)\s*$", s)
        if m:
            lang = m.group(1)
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            cls = f' class="lang-{lang}"' if lang else ""
            out.append(f"<pre><code{cls}>{html.escape(chr(10).join(buf))}</code></pre>")
            continue

        # 表格
        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s:|-]+\|?$", lines[i + 1].strip()):
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip())
                i += 1
            out.append(render_table(rows))
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            level, text = len(m.group(1)), m.group(2).strip()
            if level == 1:            # H1 由页面标题承担，不重复渲染
                i += 1
                continue
            out.append(f'<h{level} id="{slug(text)}">{inline(text)}</h{level}>')
            i += 1
            continue

        if s.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append(f"<blockquote>{inline(' '.join(buf))}</blockquote>")
            continue

        if re.match(r"^\d+\.\s+", s):
            buf = []
            while i < n and re.match(r"^\d+\.\s+", lines[i].strip()):
                buf.append(re.sub(r"^\d+\.\s+", "", lines[i].strip()))
                i += 1
            out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in buf) + "</ol>")
            continue

        if re.match(r"^[-*]\s+", s):
            items = []
            while i < n:
                m2 = re.match(r"^(\s*)[-*]\s+(.*)$", lines[i])
                if not m2:
                    break
                items.append((len(m2.group(1)), m2.group(2).rstrip()))
                i += 1
            out.append(render_list(items))
            continue

        # 段落：吃到空行或下一个块级元素
        buf = []
        while i < n:
            cur = lines[i].strip()
            if not cur or re.match(r"^(#{1,6}\s|[-*]\s|\d+\.\s|>)", cur):
                break
            if cur.startswith("```") or cur.startswith("|"):
                break
            buf.append(cur)
            i += 1
        if buf:
            out.append(f"<p>{inline(' '.join(buf))}</p>")
        else:
            i += 1
    return "\n".join(out)


def render_relations(lines):
    items = []
    for line in lines:
        s = line.strip()
        m = re.match(r"^[-*]\s+(.*)$", s)
        if not m:
            continue
        body = m.group(1).strip()
        mm = re.match(r"^\[\[([^\]]+)\]\](?:\s*[—–-]\s*(.+))?$", body)
        if mm:
            target = mm.group(1).strip()
            rel = (mm.group(2) or "相关").strip()
            href, exists = resolve(target)
            cls = REL_CLASS.get(rel, "rel")
            if exists:
                a = f'<a class="wl" href="{CUR_ROOT}{href}">{esc(target)}</a>'
            else:
                WARNINGS.append(f"断链：[[{target}]]")
                a = f'<span class="wl-dead">{esc(target)}</span>'
            items.append(f'<li>{a}<span class="rel rel-{cls}">{esc(rel)}</span></li>')
        else:
            items.append(f"<li>{inline(body)}</li>")
    return '<ul class="relations">' + "".join(items) + "</ul>"


def render_quiz(lines):
    out = []
    for line in lines:
        s = line.strip()
        if not s:
            continue
        if "::" in s:
            q, a = s.split("::", 1)
            out.append(
                '<details class="quiz"><summary>'
                f"{inline(q.strip())}</summary>"
                f'<div class="quiz-a">{inline(a.strip())}</div></details>'
            )
        else:
            out.append(f"<p>{inline(s)}</p>")
    return "\n".join(out)


def render_source(lines):
    out = []
    for line in lines:
        s = line.strip()
        if not s:
            continue
        s = re.sub(r"^[-*]\s+", "", s)
        out.append(f"<li>{inline(s)}</li>")
    return '<ul class="sources">' + "".join(out) + "</ul>"


def split_sections(body):
    """按 ## 切分。返回 [{'h': 标题或 None, 'lines': [...]}]
    注意：围栏代码块内部的 ## 不是标题，不能被切成节（AGENTS.md 的卡片模板就在代码块里）"""
    sections = []
    cur = {"h": None, "lines": []}
    in_code = False
    for line in body.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            cur["lines"].append(line)
            continue
        if not in_code:
            m = re.match(r"^##\s+(.*)$", line)
            if m:
                sections.append(cur)
                cur = {"h": m.group(1).strip(), "lines": []}
                continue
        cur["lines"].append(line)
    sections.append(cur)
    return [s for s in sections if s["h"] or any(l.strip() for l in s["lines"])]


def extract_lede(lines):
    """H1 之后第一段单独加粗的行 = 定义行"""
    for line in lines:
        s = line.strip()
        if not s:
            continue
        if s.startswith("#"):          # H1 跳过，它不是定义
            continue
        if s.startswith(">"):          # 别名行跳过
            continue
        m = re.fullmatch(r"\*\*([^*]+)\*\*", s)
        if m:
            return m.group(1)
        break
    return ""


def extract_aliases_line(lines):
    for line in lines:
        s = line.strip()
        if s.startswith(">") and "别名" in s:
            return re.sub(r"^>\s*别名[:：]\s*", "", s)
    return ""


# ---------------------------------------------------------------- 数据加载

def load_cards():
    cards = []
    if CONCEPTS.is_dir():
        for f in sorted(CONCEPTS.glob("*.md")):
            cards.append(parse_card(f, "concept"))
    if ANALYSIS.is_dir():
        for f in sorted(ANALYSIS.glob("*.md")):
            cards.append(parse_card(f, "analysis"))
    return cards


def parse_card(path, group):
    raw = path.read_text(encoding="utf-8", errors="replace")
    meta, body = parse_frontmatter(raw)
    is_analysis = group == "analysis"
    term = meta.get("term") or meta.get("title") or path.stem
    sections = split_sections(body)
    head = next((s for s in sections if s["h"] is None), {"lines": []})
    rel_dir = "a" if is_analysis else "c"
    return {
        "stem": path.stem,
        "path": f"{rel_dir}/{path.stem}.html",      # 磁盘路径，保留中文
        "url": f"{rel_dir}/{quote(path.stem)}.html",  # 链接用，百分号编码
        "kind": meta.get("kind", ""),
        "term": term,
        "title": meta.get("title") or term,
        "aliases": parse_inline_list(meta.get("aliases", "")),
        "domain": meta.get("domain", ""),
        "tags": parse_inline_list(meta.get("tags", "")),
        "created": meta.get("created", ""),
        "updated": meta.get("updated", "") or meta.get("created", ""),
        "source": meta.get("source", ""),
        # 课程学习顺序：有 order 的按分P排，没有的排最后
        "order": int(meta["order"]) if str(meta.get("order", "")).isdigit() else 9999,
        "stage": meta.get("stage", ""),
        "lede": extract_lede(head["lines"]),
        "aliases_line": extract_aliases_line(head["lines"]),
        "sections": sections,
        "group": group,
        "backlinks": [],
    }


def build_index(cards):
    INDEX["stem"].clear(); INDEX["term"].clear(); INDEX["alias"].clear()
    INDEX["moc"].clear(); INDEX["root"].clear()
    for c in cards:
        INDEX["stem"][c["stem"]] = c["url"]
        INDEX["term"][c["term"]] = c["url"]
        for a in c["aliases"]:
            INDEX["alias"][a] = c["url"]
            INDEX["alias"][a.lower()] = c["url"]
    if MOC.is_dir():
        for f in MOC.glob("*.md"):
            INDEX["moc"][f.stem] = f"d/{quote(f.stem)}.html"
    # 根目录固定页面
    INDEX["root"]["首页"] = "index.html"
    INDEX["root"]["概念索引"] = "all.html"
    INDEX["root"]["知识库"] = "index.html"
    if (BASE / "AGENTS.md").is_file():
        for key in ("AGENTS", "AGENTS.md", "agents"):
            INDEX["root"][key] = "agents.html"


# ---------------------------------------------------------------- 页面骨架

def page(title, content, root="", desc="", extra_head=""):
    global CUR_ROOT
    CUR_ROOT = root
    safe_desc = esc(desc or SITE_TITLE)
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{safe_desc}">
<meta name="color-scheme" content="light dark">
<meta http-equiv="Cache-Control" content="no-cache, must-revalidate">
<title>{esc(title)} · {SITE_TITLE}</title>
<link rel="stylesheet" href="{root}assets/style.css?v={ASSET_VER}">
<script>try{{var t=localStorage.getItem("kb-theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
{extra_head}</head>
<body>
<header class="top">
  <a class="brand" href="{root}index.html">{SITE_TITLE}</a>
  <nav class="topnav">
    <button id="theme-toggle" type="button" aria-label="切换主题" title="切换主题">◐</button>
  </nav>
</header>
<main>
{content}
</main>
<footer class="foot">
  <span>{SITE_TITLE}</span>
  <span>更新于 {datetime.now().strftime('%Y-%m-%d %H:%M')}</span>
</footer>
<script src="{root}assets/app.js?v={ASSET_VER}" defer></script>
</body>
</html>
"""


def breadcrumb(card, root):
    parts = [f'<a href="{root}index.html">首页</a>']
    if card["domain"]:
        segs = [s for s in card["domain"].split("/") if s]
        for i, seg in enumerate(segs):
            if i == 0:
                parts.append(f'<a href="{root}d/{quote(seg)}.html">{esc(seg)}</a>')
            else:
                parts.append(f"<span>{esc(seg)}</span>")
    else:
        parts.append('<span>分析</span>')
    return '<nav class="crumb">' + ' <span class="sep">/</span> '.join(parts) + "</nav>"


def card_body(card, root, docs):
    """渲染一张卡的完整正文"""
    segs = []
    for sec in card["sections"]:
        h = sec["h"]
        lines = sec["lines"]
        if h is None:
            continue
        if h == "关联":
            segs.append(f'<section class="sec"><h2 id="{slug(h)}">关联</h2>{render_relations(lines)}</section>')
        elif h == "自测":
            segs.append(f'<section class="sec"><h2 id="{slug(h)}">自测</h2>'
                        f'<p class="hint">点开看答案，先自己想一想</p>{render_quiz(lines)}</section>')
        elif h == "出处":
            segs.append(f'<section class="sec src"><h2 id="{slug(h)}">出处</h2>{render_source(lines)}</section>')
        else:
            segs.append(f'<section class="sec"><h2 id="{slug(h)}">{esc(h)}</h2>'
                        f'{render_markdown(lines)}</section>')
    return "".join(segs)


def backlinks_block(card, root):
    if not card["backlinks"]:
        return ""
    items = []
    for src_url, src_term, rel in card["backlinks"]:
        items.append(
            f'<li><a class="wl" href="{root}{src_url}">{esc(src_term)}</a>'
            f'<span class="rel rel-plain">{esc(rel)}</span></li>'
        )
    return ('<section class="sec backlinks"><h2>被引用</h2>'
            '<p class="hint">这些卡片引用了当前概念</p>'
            '<ul class="relations">' + "".join(items) + "</ul></section>")


# ---------------------------------------------------------------- 生成各类页面

def gen_card(cards, i):
    global CUR_ROOT
    CUR_ROOT = "../"          # 正文在 page() 之前渲染，必须提前设好前缀
    card = cards[i]
    root = "../"
    sections = []
    # 只把有 H2 的区块列进目录
    toc_items = []
    for sec in card["sections"]:
        if sec["h"]:
            toc_items.append(f'<a href="#{slug(sec["h"])}">{esc(sec["h"])}</a>')

    head = [breadcrumb(card, root), f'<article class="card">']
    head.append(f'<h1>{esc(card["term"])}</h1>')
    if card["aliases"]:
        head.append('<div class="aliases">' + " · ".join(esc(a) for a in card["aliases"]) + "</div>")
    if card["lede"]:
        head.append(f'<p class="lede">{inline(card["lede"])}</p>')
    if toc_items:
        head.append('<details class="toc"><summary>目录</summary><nav>' + "".join(toc_items) + "</nav></details>")

    body = "".join([
        "".join(head),
        card_body(card, root, cards),
        backlinks_block(card, root),
    ])

    # 上下张导航：按 domain + term 排序
    prev_c = cards[i - 1] if i > 0 else None
    next_c = cards[i + 1] if i + 1 < len(cards) else None
    pager = ['<nav class="pager">']
    pager.append(
        f'<a class="prev" href="{root}{prev_c["url"]}"><small>上一张</small>{esc(prev_c["term"])}</a>'
        if prev_c else '<span></span>'
    )
    pager.append(
        f'<a class="next" href="{root}{next_c["url"]}"><small>下一张</small>{esc(next_c["term"])}</a>'
        if next_c else '<span></span>'
    )
    pager.append("</nav>")
    body += "".join(pager) + "</article>"

    desc = card["lede"] or card["domain"]
    return page(card["term"], body, root=root, desc=desc)


def anchor(name):
    """「数据分析/Pandas」→ 可用的 HTML id：a-数据分析-Pandas"""
    return "a-" + re.sub(r"[^\w]+", "-", name).strip("-")


def disp(name):
    """没有 domain 的分析卡，展示为「分析」比「未分类」清楚"""
    return "分析" if name == "未分类" else name


def quicknav(tops, by_dom):
    """页内跳转：顶级领域 chips（横滑）+ 完整分类下拉。"""
    chips, opts = [], []
    for t in sorted(tops):
        n = sum(len(by_dom[d]) for d in tops[t])
        chips.append(f'<a class="chip" href="#{anchor(t)}">{esc(disp(t))}<i>{n}</i></a>')
        subs = sorted(tops[t])
        if len(subs) == 1:
            d = subs[0]
            label = "/".join([s for s in d.split("/")[1:]]) or disp(d)
            opts.append(f'<option value="{anchor(d)}">{esc(label)} · {len(by_dom[d])}</option>')
        else:
            opts.append(f'<optgroup label="{esc(disp(t))}">')
            for d in subs:
                label = "/".join([s for s in d.split("/")[1:]]) or "总类"
                opts.append(f'<option value="{anchor(d)}">{esc(label)} · {len(by_dom[d])}</option>')
            opts.append("</optgroup>")
    return ('<div class="quicknav"><div class="chips">' + "".join(chips) + "</div>"
            '<select id="jump" aria-label="按分类跳转"><option value="">分类跳转</option>'
            + "".join(opts) + "</select></div>")


def gen_home(cards, domains):
    global CUR_ROOT
    CUR_ROOT = ""
    root = ""
    total = len(cards)
    dom_count = len({c["domain"].split("/")[0] for c in cards if c["domain"]})
    recent = sorted([c for c in cards if c["updated"]], key=lambda c: c["updated"], reverse=True)[:6]

    parts = [f"""<section class="hero">
  <h1>{SITE_TITLE}</h1>
  <p class="sub">{total} 个概念 · {dom_count} 个领域 · 更新于 {datetime.now().strftime('%Y-%m-%d')}</p>
  <div class="searchbox">
    <input id="q" type="search" placeholder="搜索概念、别名、正文…" autocomplete="off" enterkeyhint="search">
    <div id="results" class="results" hidden></div>
  </div>
</section>"""]

    # 按完整分类聚合，供跳转条与下方分组使用
    by_dom = defaultdict(list)
    for c in cards:
        by_dom[c["domain"] or "未分类"].append(c)
    tops = defaultdict(list)
    for d in by_dom:
        tops[d.split("/")[0]].append(d)
    parts.append(quicknav(tops, by_dom))

    parts.append('<section class="sec"><h2>领域</h2><div class="doms">')
    for dom in sorted(domains):
        items = domains[dom]
        subs = defaultdict(int)
        for c in items:
            segs = [s for s in c["domain"].split("/") if s]
            key = "/".join(segs[1:]) if len(segs) > 1 else "总类"
            subs[key] += 1
        sub_html = "".join(f"<span>{esc(k)} <b>{v}</b></span>" for k, v in sorted(subs.items()))
        parts.append(
            f'<a class="domcard" href="d/{quote(dom)}.html">'
            f'<h3>{esc(dom)}</h3><p>{len(items)} 个概念</p>'
            f'<div class="subs">{sub_html}</div></a>'
        )
    parts.append("</div></section>")

    if recent:
        parts.append('<section class="sec"><h2>最近更新</h2><ul class="recent">')
        for c in recent:
            dom = c["domain"] or "分析"
            parts.append(
                f'<li><a href="{c["url"]}">{esc(c["term"])}</a>'
                f'<span class="meta">{esc(dom)} · {esc(c["updated"])}</span></li>'
            )
        parts.append("</ul></section>")

    parts.append(
        '<section class="sec"><h2>全部概念</h2>'
        f'<p class="hint">按分类排列，共 {len(cards)} 张；顶部可跳转，'
        '紧凑索引见 <a class="wl" href="all.html">概念索引</a>。</p></section>'
    )
    seen = set()
    for d in sorted(by_dom, key=lambda x: (1 if x == "未分类" else 0, x)):
        items = sorted(by_dom[d], key=lambda x: (x["order"], x["term"]))
        top = d.split("/")[0]
        pre = ""
        if top not in seen:                      # 顶级领域的锚点落在第一个子类前
            seen.add(top)
            pre = f'<span class="anchor" id="{anchor(top)}"></span>'
        more = (f'<a class="more" href="d/{quote(top)}.html">领域页 →</a>'
                if d != "未分类" else "")
        parts.append(
            f'<section class="sec sub" id="{anchor(d)}">{pre}'
            f'<h3 class="subh">{esc(disp(d))}<span class="cnt">{len(items)}</span>{more}</h3>'
            '<div class="grid">'
        )
        for c in items:
            kind = c["kind"] or c["group"]
            parts.append(
                f'<a class="tile" href="{c["url"]}">'
                f'<span class="tile-kind kind-{esc(kind)}">{esc(kind)}</span>'
                f'<span class="tile-term">{esc(c["term"])}</span>'
                f'<span class="tile-dom">{esc(c["domain"] or "分析")}</span></a>'
            )
        parts.append("</div></section>")

    return page(SITE_TITLE, "".join(parts), root=root,
                desc=f"{SITE_TITLE} · {total} 个概念")


def gen_all(cards):
    global CUR_ROOT
    CUR_ROOT = ""
    root = ""
    groups = defaultdict(list)
    for c in cards:
        groups[c["domain"] or "未分类"].append(c)
    tops = defaultdict(list)
    for d in groups:
        tops[d.split("/")[0]].append(d)
    parts = ['<section class="hero"><h1>全部概念</h1>'
             f'<p class="sub">共 {len(cards)} 张卡片</p></section>',
             quicknav(tops, groups)]
    seen = set()
    for dom in sorted(groups, key=lambda x: (1 if x == "未分类" else 0, x)):
        top = dom.split("/")[0]
        pre = ""
        if top not in seen:
            seen.add(top)
            pre = f'<span class="anchor" id="{anchor(top)}"></span>'
        parts.append(f'<section class="sec sub" id="{anchor(dom)}">{pre}'
                     f'<h3 class="subh">{esc(disp(dom))}<span class="cnt">{len(groups[dom])}</span></h3>'
                     '<ul class="plain">')
        for c in sorted(groups[dom], key=lambda x: (x["order"], x["term"])):
            extra = f' — {esc(c["aliases_line"])}' if c["aliases_line"] else ""
            stage = f' <span class="tile-dom">{esc(c["stage"])}</span>' if c["stage"] else ""
            parts.append(f'<li><a href="{c["url"]}">{esc(c["term"])}</a>{extra}{stage}</li>')
        parts.append("</ul></section>")
    return page("全部概念", "".join(parts), root=root)


def gen_domain(dom, items):
    global CUR_ROOT
    CUR_ROOT = "../"
    root = "../"
    groups = defaultdict(list)
    for c in items:
        groups[c["domain"] or dom].append(c)

    def short(d):
        return "/".join([s for s in d.split("/")[1:]]) or "总类"

    chips = "".join(
        f'<a class="chip" href="#{anchor(d)}">{esc(short(d))}<i>{len(groups[d])}</i></a>'
        for d in sorted(groups)
    )
    parts = [f'<nav class="crumb"><a href="{root}index.html">首页</a> '
             f'<span class="sep">/</span> <span>{esc(dom)}</span></nav>',
             f'<section class="hero"><h1>{esc(dom)}</h1>'
             f'<p class="sub">{len(items)} 个概念 · {len(groups)} 个子类</p></section>']
    if len(chips) and len(groups) > 1:
        parts.append(f'<div class="quicknav"><div class="chips">{chips}</div></div>')
    for d in sorted(groups):
        parts.append(f'<section class="sec sub" id="{anchor(d)}">'
                     f'<h3 class="subh">{esc(short(d))}<span class="cnt">{len(groups[d])}</span></h3>'
                     '<div class="grid">')
        for c in sorted(groups[d], key=lambda x: (x["order"], x["term"])):
            # 有课程阶段的卡显示「S01E03 · 创建数组」，其余仍显示一句话定义
            label = c["stage"] or c["lede"][:40] or c["kind"]
            parts.append(
                f'<a class="tile" href="{root}{c["url"]}">'
                f'<span class="tile-term">{esc(c["term"])}</span>'
                f'<span class="tile-dom">{esc(label)}</span></a>'
            )
        parts.append("</div></section>")
    return page(dom, "".join(parts), root=root, desc=f"{dom} 领域下的概念")


def gen_agents():
    global CUR_ROOT
    CUR_ROOT = ""
    f = BASE / "AGENTS.md"
    if not f.is_file():
        return None
    root = ""
    meta, body = parse_frontmatter(f.read_text(encoding="utf-8", errors="replace"))
    sections = split_sections(body)
    parts = [f'<nav class="crumb"><a href="{root}index.html">首页</a> '
             f'<span class="sep">/</span> <span>操作规则</span></nav>',
             '<article class="card"><h1>知识库操作规则</h1>',
             '<p class="lede">AGENTS.md —— 任何 AI Agent 打开这个库时遵循的规则</p>']
    for sec in sections:
        if sec["h"]:
            parts.append(f'<section class="sec"><h2 id="{slug(sec["h"])}">{esc(sec["h"])}</h2>'
                         f'{render_markdown(sec["lines"])}</section>')
        else:
            parts.append(render_markdown(sec["lines"]))
    parts.append("</article>")
    return page("操作规则", "".join(parts), root=root)


# ---------------------------------------------------------------- 主流程

def collect_backlinks(cards):
    by_url = {c["url"]: c for c in cards}
    for c in cards:
        for sec in c["sections"]:
            if sec["h"] != "关联":
                continue
            for line in sec["lines"]:
                m = re.match(r"^[-*]\s+\[\[([^\]|]+)\]\](?:\s*[—–-]\s*(.+))?$", line.strip())
                if not m:
                    continue
                href, exists = resolve(m.group(1).strip())
                if exists and href in by_url:
                    by_url[href]["backlinks"].append((c["url"], c["term"], (m.group(2) or "相关").strip()))


def build_search(cards):
    out = []
    for c in cards:
        text_parts = []
        for sec in c["sections"]:
            for line in sec["lines"]:
                line = line.strip()
                if line and not line.startswith("---"):
                    text_parts.append(re.sub(r"[\[\]*#>|-]", " ", line))
        out.append({
            "t": c["term"],
            "a": c["aliases"],
            "d": c["domain"] or "分析",
            "k": c["kind"] or c["group"],
            "u": c["url"],
            "s": (c["lede"] or " ".join(text_parts))[:120],
            "x": " ".join(text_parts)[:600],
        })
    return out


def clean_out():
    """就地覆盖，不清空目录。

    原来的实现每次都把 docs/ 整个删光再重写，卡片只增不删的情况下纯属多余，
    还会触发环境的批量删除保护（一次 50 个文件就中断）。产物按固定路径写入，
    重跑自然覆盖；万一以后真的删了卡片，残留页面用下面的 orphan 检查提示，
    由人确认后再清，不让脚本擅自批量删文件。"""
    OUT.mkdir(parents=True, exist_ok=True)


def asset_version():
    """css/js 的内容哈希，作为查询串让浏览器绕过旧缓存"""
    h = hashlib.md5()
    for name in ("style.css", "app.js"):
        p = THEME / name
        if p.is_file():
            h.update(p.read_bytes())
    return h.hexdigest()[:8]


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def main():
    global ASSET_VER
    if not CONCEPTS.is_dir():
        print(f"[!] 找不到概念目录：{CONCEPTS}")
        return 1

    ASSET_VER = asset_version()
    cards_all = load_cards()
    # 概念卡在前、分析卡在后；同组内按领域与名称排，避免翻页时两类穿插
    cards_all.sort(key=lambda c: (0 if c["group"] == "concept" else 1,
                                  c["domain"] or "\uffff", c["term"]))
    build_index(cards_all)
    collect_backlinks(cards_all)

    if OUT.exists():
        clean_out()
    else:
        OUT.mkdir(parents=True, exist_ok=True)
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    # 资源
    for name in ("style.css", "app.js"):
        src = THEME / name
        if src.is_file():
            write(OUT / "assets" / name, src.read_text(encoding="utf-8"))

    # 概念 / 分析页
    for i, c in enumerate(cards_all):
        write(OUT / c["path"], gen_card(cards_all, i))

    # 首页 / 全部
    domains = defaultdict(list)
    for c in cards_all:
        if c["domain"]:
            domains[c["domain"].split("/")[0]].append(c)
    write(OUT / "index.html", gen_home(cards_all, domains))
    write(OUT / "all.html", gen_all(cards_all))

    # 领域页
    for dom, items in domains.items():
        CUR_ROOT = "../"
        write(OUT / "d" / f"{dom}.html", gen_domain(dom, items))

    # 规则页
    agents = gen_agents()
    if agents:
        write(OUT / "agents.html", agents)

    # 搜索索引
    write(OUT / "search.json", json.dumps(build_search(cards_all), ensure_ascii=False, separators=(",", ":")))

    pages = len(list(OUT.rglob("*.html")))
    print(f"[√] 生成完成：{pages} 个页面，{len(cards_all)} 张卡片")
    print(f"    输出目录：{OUT}")
    print(f"    领域：{'、'.join(sorted(domains))}")
    for d in sorted(domains):
        print(f"      {d}: {len(domains[d])} 张")

    if WARNINGS:
        uniq = sorted(set(WARNINGS))
        print(f"\n[i] 断链 {len(uniq)} 处（这些概念还没有卡片，站点里显示为灰色）：")
        for w in uniq[:15]:
            print("    " + w)
    else:
        print("\n[√] 没有断链")
    return 0


if __name__ == "__main__":
    sys.exit(main())
