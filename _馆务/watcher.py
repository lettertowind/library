#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""_在编 监听器：新素材静止后自动抽取概念。Ctrl+C 停止。"""
import sys
import json
import time
import subprocess
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

OFFICE = Path(__file__).resolve().parent
BASE = OFFICE.parent
INBOX = BASE / "_在编"
CURATOR = OFFICE / "curator.py"
CONFIG = OFFICE / "config.json"

STABLE = 25
POLL = 20
MAX_RETRY = 3
AUDIT_INTERVAL = 7 * 86400          # 每 7 天自动体检一次
LAST_AUDIT = OFFICE / ".last_audit"
CONCEPTS = BASE / "概念"


def maybe_audit():
    """定期生成体检报告：只出报告，不动卡片，也不自动修复。"""
    if not CONCEPTS.is_dir() or len(list(CONCEPTS.glob("*.md"))) < 5:
        return
    try:
        last = LAST_AUDIT.stat().st_mtime if LAST_AUDIT.exists() else 0
    except Exception:
        last = 0
    if time.time() - last < AUDIT_INTERVAL:
        return
    stamp("距上次体检超过 7 天，生成体检报告…")
    r = subprocess.run([sys.executable, str(OFFICE / "maintain.py"), "audit"],
                       cwd=str(OFFICE), capture_output=True, text=True,
                       encoding="utf-8", errors="ignore")
    for line in (r.stdout or "").strip().splitlines():
        stamp("  " + line)
    try:
        LAST_AUDIT.touch()
    except Exception:
        pass


def stamp(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


def has_key():
    try:
        return bool(json.loads(CONFIG.read_text(encoding="utf-8")).get("api_key"))
    except Exception:
        return False


def main():
    if not has_key():
        stamp("config.json 未配置 api_key，监听不启动")
        return 2
    stamp(f"监听中：{INBOX}")
    fails = {}
    while True:
        try:
            for f in sorted(INBOX.glob("*.md")):
                try:
                    age = time.time() - f.stat().st_mtime
                except FileNotFoundError:
                    continue
                if age < STABLE or fails.get(f.name, 0) >= MAX_RETRY:
                    continue
                stamp(f"新素材：{f.name}")
                r = subprocess.run([sys.executable, str(CURATOR), "--file", f.name],
                                   cwd=str(OFFICE), capture_output=True, text=True,
                                   encoding="utf-8", errors="ignore")
                for line in (r.stdout or "").strip().splitlines():
                    stamp("  " + line)
                if r.returncode == 0 and not f.exists():
                    stamp("  完成")
                    fails.pop(f.name, None)
                else:
                    fails[f.name] = fails.get(f.name, 0) + 1
                    err = (r.stderr or "").strip().splitlines()
                    stamp(f"  失败（第 {fails[f.name]} 次）" + (f"：{err[-1]}" if err else ""))
            maybe_audit()
            time.sleep(POLL)
        except KeyboardInterrupt:
            stamp("已停止")
            return 0
        except Exception as e:
            stamp(f"异常：{type(e).__name__}: {e}")
            time.sleep(POLL)


if __name__ == "__main__":
    sys.exit(main())
