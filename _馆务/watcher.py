#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""_在编 监听器：新素材静止后自动抽取概念 → 重建站点 → 推送 GitHub。Ctrl+C 停止。"""
import sys
import json
import os
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
SITE = OFFICE / "site.py"
SYNC = OFFICE / "sync.py"
CONFIG = OFFICE / "config.json"

STABLE = 25
POLL = 20
MAX_RETRY = 3
AUDIT_INTERVAL = 7 * 86400          # 每 7 天自动体检一次
LAST_AUDIT = OFFICE / ".last_audit"
CONCEPTS = BASE / "概念"
TASK_LOG = OFFICE / "整理日志.md"
WATCH_LOG = OFFICE / "监听日志.txt"
LOCK_PATH = OFFICE / ".watcher.lock"


def acquire_lock():
    """单实例锁：开机自启和手动双击同时存在时，只允许一个监听进程。
    用文件独占锁，进程退出（含崩溃）时由系统自动释放。"""
    f = open(LOCK_PATH, "a+")
    try:
        import msvcrt
        msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
        f.seek(0)
        f.truncate()
        f.write(str(os.getpid()))
        f.flush()
        return f
    except OSError:
        try:
            f.close()
        except Exception:
            pass
        return None


def run(script, *args):
    """跑一个子脚本，把它的输出带缩进转发到监听窗口"""
    r = subprocess.run([sys.executable, str(script), *args],
                       cwd=str(OFFICE), capture_output=True, text=True,
                       encoding="utf-8", errors="ignore")
    for line in (r.stdout or "").strip().splitlines()[-12:]:
        stamp("    " + line)
    return r


def publish(source_name):
    """抽完概念后，重建站点并推送。任何一步失败都不影响继续监听。"""
    stamp("  重建站点…")
    r = run(SITE)
    if r.returncode != 0:
        err = (r.stderr or "").strip().splitlines()
        stamp("    [!] 建站失败" + (f"：{err[-1]}" if err else ""))
        return

    stamp("  推送到 GitHub…")
    r = run(SYNC, f"自动入库 {Path(source_name).stem}")
    if r.returncode != 0:
        err = (r.stderr or "").strip().splitlines()
        stamp("    [!] 推送失败，卡片已在本地，稍后手动发布即可" + (f"：{err[-1]}" if err else ""))
        return
    stamp("  已上线，约 30 秒后手机可见")


def maybe_audit():
    """定期生成体检报告：只出报告，不动卡片，也不自动修复。
    放到独立进程里跑，避免几百张卡的体检把监听循环卡住。"""
    if not CONCEPTS.is_dir() or len(list(CONCEPTS.glob("*.md"))) < 5:
        return
    try:
        last = LAST_AUDIT.stat().st_mtime if LAST_AUDIT.exists() else 0
    except Exception:
        last = 0
    if time.time() - last < AUDIT_INTERVAL:
        return

    try:
        LAST_AUDIT.touch()          # 先打标记，避免每轮都重复触发
    except Exception:
        pass

    stamp("距上次体检超过 7 天，后台生成体检报告（不阻塞监听）…")
    flags = 0
    if os.name == "nt":
        flags = 0x00000008 | 0x00000200     # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
    try:
        subprocess.Popen(
            [sys.executable, str(OFFICE / "maintain.py"), "audit"],
            cwd=str(OFFICE),
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            creationflags=flags,
        )
    except Exception as e:
        stamp(f"  体检启动失败：{type(e).__name__}: {e}")


def stamp(m):
    line = f"[{time.strftime('%m-%d %H:%M:%S')}] {m}"
    try:                                   # pythonw 无控制台，print 会失败，不能让它中断监听
        print(line, flush=True)
    except Exception:
        pass
    try:                                   # 后台无窗口运行时也能留痕
        if WATCH_LOG.exists() and WATCH_LOG.stat().st_size > 2_000_000:
            WATCH_LOG.write_text("", encoding="utf-8")
        with WATCH_LOG.open("a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass


def has_key():
    try:
        return bool(json.loads(CONFIG.read_text(encoding="utf-8")).get("api_key"))
    except Exception:
        return False


def main():
    if not has_key():
        stamp("config.json 未配置 api_key，监听不启动")
        return 2
    lock = acquire_lock()
    if lock is None:
        stamp("已有一个监听在运行，本次退出（避免重复处理同一批素材）")
        return 3
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
                    publish(f.name)          # 自动建站 + 推送
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
