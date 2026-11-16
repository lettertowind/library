#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""手机分享链接 → BiliNote 笔记 → 概念卡片 → 发布网站

一条命令跑完整条链路：

    python pipeline.py "https://b23.tv/xxxx"

可选参数：
    --note-only    只生成笔记，停在 _在编（不抽概念、不发布）
    --dry-run      只解析链接并检查环境，不提交任务
    --no-publish   抽概念但不推 GitHub
    --model xxx    指定模型，默认 deepseek-flash

依赖：BiliNote 桌面版必须在运行（BiliNote.exe），后端监听 127.0.0.1:8483。
"""

from __future__ import annotations

import json
import os
import re
import ssl
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent          # D:\知识库
OFFICE = BASE_DIR / "_馆务"
INBOX = BASE_DIR / "_在编"
API = "http://127.0.0.1:8483"

# BiliNote 后端（源码方式），没有它就无法生成笔记
BACKEND_DIR = Path(r"C:\Users\Sean\WorkBuddy\spaces\2026_11_16_19-04-52\BiliNote\backend")

POLL_INTERVAL = 8
MAX_WAIT = 60 * 45          # 长视频最多等 45 分钟

STATUS_CN = {
    "PENDING": "排队中",
    "PARSING": "解析链接",
    "DOWNLOADING": "下载中",
    "TRANSCRIBING": "转写中",
    "SUMMARIZING": "生成笔记",
    "FORMATTING": "整理格式",
    "SAVING": "保存中",
    "SUCCESS": "完成",
    "FAILED": "失败",
}

_OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def say(msg=""):
    print(msg, flush=True)


def http_json(path, method="GET", payload=None, timeout=60):
    url = API + path
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        url, data=data, method=method,
        headers={"Content-Type": "application/json"},
    )
    with _OPENER.open(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


# ---------------------------------------------------------------- 链接处理

def _follow(url):
    """跟随重定向拿到最终地址（本机证书链有问题，这里不校验证书）"""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)"})
    with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
        return r.geturl()


def normalize_link(text):
    """从手机分享文本里提取并规范成电脑可用的 B站地址。
    返回 (标准网址, BV号或av号, 原始输入)"""
    raw = text.strip()
    m = re.search(r"https?://[^\s，,。、）)\"']+", raw)
    url = m.group(0) if m else raw

    bv = re.search(r"(BV[0-9A-Za-z]{10})", url)
    if bv:
        return f"https://www.bilibili.com/video/{bv.group(1)}", bv.group(1), raw

    av = re.search(r"/av(\d+)", url, re.I)
    if av:
        return f"https://www.bilibili.com/video/av{av.group(1)}", f"av{av.group(1)}", raw

    if "b23.tv" in url or "bili2233" in url or "bili" in url:
        try:
            final = _follow(url)
        except Exception as e:
            raise RuntimeError(f"短链还原失败：{type(e).__name__} {e}")
        bv = re.search(r"(BV[0-9A-Za-z]{10})", final)
        if bv:
            return f"https://www.bilibili.com/video/{bv.group(1)}", bv.group(1), raw
        av = re.search(r"/av(\d+)", final, re.I)
        if av:
            return f"https://www.bilibili.com/video/av{av.group(1)}", f"av{av.group(1)}", raw
        raise RuntimeError(f"短链还原后没找到 BV 号：{final}")

    raise RuntimeError("没能从这段文字里认出 B站 链接")


# ---------------------------------------------------------------- 环境检查

def _health():
    """返回健康数据，后端没响应则返回 None"""
    try:
        return http_json("/api/sys_health", timeout=5).get("data") or {}
    except Exception:
        return None


def ensure_backend():
    """后端没起就自动拉起（源码方式），不需要用户开窗口"""
    d = _health()
    if d is not None:
        return d

    say("    后端未运行，自动启动中…")
    py = BACKEND_DIR / ".venv" / "Scripts" / "python.exe"
    if not py.is_file():
        raise RuntimeError(f"找不到后端解释器：{py}")

    env = os.environ.copy()
    for k in ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy", "ALL_PROXY", "all_proxy"):
        env.pop(k, None)          # 代理会干扰下载与 API 调用

    flags = 0
    if os.name == "nt":
        flags = 0x00000008 | 0x00000200     # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP

    subprocess.Popen(
        [str(py), "main.py"], cwd=str(BACKEND_DIR), env=env,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        creationflags=flags,
    )
    for i in range(24):
        time.sleep(5)
        d = _health()
        if d is not None:
            say(f"    后端已就绪（{5 * (i + 1)} 秒）")
            return d
    raise RuntimeError("后端启动超时。可手动在 BiliNote 界面里启动后重试")


def check_env():
    d = ensure_backend()
    say(f"    后端 {d.get('backend')} · 数据库 {d.get('db')} · ffmpeg {d.get('ffmpeg')}")

    try:
        ps = http_json("/api/get_all_providers", timeout=10).get("data") or []
    except Exception:
        ps = []
    ready = [p for p in ps if p.get("api_key")]
    if not ready:
        raise RuntimeError("没有可用的大模型供应商，请在 BiliNote 里填一个 API Key")
    say(f"    可用供应商：{'、'.join(p.get('id', '?') for p in ready)}")

    if d.get("ffmpeg") != "ok":
        say("    [!] ffmpeg 未就绪，下载高清视频可能失败；先试，失败再修")
    return ready[0].get("id") if ready else "deepseek"


# ---------------------------------------------------------------- 主流程

def submit(url, provider_id, model):
    payload = {
        "video_url": url,
        "platform": "bilibili",
        "quality": "fast",
        "screenshot": False,
        "link": True,
        "model_name": model,
        "provider_id": provider_id,
        "style": "detailed",
        "format": [],
        "extras": "",
    }
    r = http_json("/api/generate_note", "POST", payload, timeout=60)
    if r.get("code") != 0:
        raise RuntimeError(f"提交任务失败：{r}")
    tid = r.get("data", {}).get("task_id")
    if not tid:
        raise RuntimeError(f"没有拿到 task_id：{r}")
    return tid


def wait_task(tid):
    start = time.time()
    last = None
    while True:
        try:
            raw = http_json(f"/api/task_status/{tid}", timeout=30)
            d = raw.get("data") or {}
        except Exception as e:
            say(f"    [!] 查询状态出错：{e}")
            time.sleep(POLL_INTERVAL)
            continue
        st = d.get("status")
        if not st:                      # 状态文件还没落盘，静默继续等
            if time.time() - start > MAX_WAIT:
                raise RuntimeError(f"等待超过 {MAX_WAIT // 60} 分钟，放弃")
            time.sleep(POLL_INTERVAL)
            continue
        if st != last:
            cn = STATUS_CN.get(st, st)
            say(f"    [{int(time.time() - start):>4}s] {cn}")
            last = st
        if st == "SUCCESS":
            return d
        if st == "FAILED":
            msg = d.get("message") or "未知原因"
            raise RuntimeError(f"任务失败：{str(msg)[:300]}")
        if time.time() - start > MAX_WAIT:
            raise RuntimeError(f"等待超过 {MAX_WAIT // 60} 分钟，放弃（任务可能仍在后台跑）")
        time.sleep(POLL_INTERVAL)


def find_note(before):
    """在 _在编 里找出本次新生成的 markdown"""
    now = {p.name for p in INBOX.glob("*.md")} if INBOX.is_dir() else set()
    new = now - before
    if new:
        return INBOX / sorted(new)[0]
    md = sorted(INBOX.glob("*_markdown.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    return md[0] if md else None


def run_step(title, args, cwd):
    say(f"\n=== {title} ===")
    r = subprocess.run(args, cwd=str(cwd), capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    out = (r.stdout or "").strip()
    err = (r.stderr or "").strip()
    if out:
        for line in out.splitlines()[-14:]:
            say("  " + line)
    if r.returncode != 0:
        if err:
            for line in err.splitlines()[-10:]:
                say("  " + line)
        raise RuntimeError(f"{title} 失败（退出码 {r.returncode}）")
    return out


def main():
    args = [a for a in sys.argv[1:]]
    flags = {a for a in args if a.startswith("--")}
    model = "deepseek-flash"
    if "--model" in args:
        i = args.index("--model")
        if i + 1 < len(args):
            model = args[i + 1]
            args.pop(i + 1)
    text = " ".join(a for a in args if not a.startswith("--")).strip()

    if not text:
        say(__doc__)
        return 1

    say("=== 1/6 解析链接 ===")
    try:
        url, vid, raw = normalize_link(text)
    except Exception as e:
        say(f"  [!] {e}")
        return 1
    say(f"    {vid}")
    say(f"    {url}")

    say("\n=== 2/6 检查环境 ===")
    try:
        provider = check_env()
    except Exception as e:
        say(f"  [!] {e}")
        return 1

    if "--dry-run" in flags:
        say("\n[dry-run] 环境正常，链接可识别。去掉 --dry-run 即开始生成。")
        return 0

    before = {p.name for p in INBOX.glob("*.md")} if INBOX.is_dir() else set()

    say(f"\n=== 3/6 提交任务（模型 {model}）===")
    try:
        tid = submit(url, provider, model)
    except Exception as e:
        say(f"  [!] {e}")
        return 1
    say(f"    task_id {tid}")

    say("\n=== 4/6 等待生成 ===")
    try:
        wait_task(tid)
    except Exception as e:
        say(f"  [!] {e}")
        return 1

    note = find_note(before)
    if not note:
        say("  [!] 任务显示完成，但 _在编 里没找到笔记")
        return 1
    say(f"    笔记：{note.name}（{note.stat().st_size // 1024} KB）")

    if "--note-only" in flags:
        say("\n[note-only] 已停在笔记阶段，没有抽概念、没有发布。")
        return 0

    say("\n=== 5/6 抽取概念 ===")
    try:
        run_step("抽取概念", [sys.executable, "curator.py"], OFFICE)
    except Exception as e:
        say(f"  [!] {e}")
        return 1

    say("\n=== 6/6 生成站点并发布 ===")
    try:
        run_step("生成站点", [sys.executable, "site.py"], OFFICE)
        if "--no-publish" not in flags:
            run_step("推送 GitHub", [sys.executable, "sync.py", f"新增：{vid}"], OFFICE)
        else:
            say("  (--no-publish) 已跳过推送")
    except Exception as e:
        say(f"  [!] {e}")
        return 1

    say("\n[√] 完成。约 30 秒后线上生效（手机上拉刷新即可）：")
    say("    https://lettertowind.github.io/library/")
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        say("\n已中断")
        sys.exit(130)
