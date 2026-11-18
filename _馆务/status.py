# -*- coding: utf-8 -*-
"""知识库链路自查：监听是否在跑、在编区有没有积压、站点与 git 状态。"""
import subprocess
import sys
import time
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

OFFICE = Path(__file__).resolve().parent
BASE = OFFICE.parent
INBOX = BASE / "_在编"
LOCK_PATH = OFFICE / ".watcher.lock"
LOG = OFFICE / "监听日志.txt"
SITE = BASE / "docs" / "index.html"


def watcher_running():
    """能拿到锁文件第 0 字节的独占锁 → 没有实例在跑；拿不到 → 有实例持锁。

    注意必须 seek(0)：锁有偏移，不定位就锁不到同一区间，会误判为「未运行」。
    """
    if not LOCK_PATH.exists():
        return False
    try:
        f = open(LOCK_PATH, "r+")
    except Exception:
        return None
    try:
        import msvcrt
        f.seek(0)
        msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
    except OSError:
        f.close()
        return True                      # 锁被占用 → 正在运行
    else:
        try:
            msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
        except Exception:
            pass
        f.close()
        return False


def ago(ts):
    d = int(time.time() - ts)
    if d < 60:
        return f"{d} 秒前"
    if d < 3600:
        return f"{d // 60} 分钟前"
    if d < 86400:
        return f"{d // 3600} 小时前"
    return f"{d // 86400} 天前"


def main():
    print("知识库链路状态")
    print("=" * 34)

    running = watcher_running()
    mark = {True: "运行中", False: "未运行", None: "无法判断"}[running]
    print(f"监听进程    {mark}")

    pending = sorted(INBOX.glob("*_markdown.md")) if INBOX.is_dir() else []
    if pending:
        print(f"在编区      {len(pending)} 篇待处理")
        for p in pending[:5]:
            print(f"              {p.name[:8]}…  {ago(p.stat().st_mtime)}")
    else:
        print("在编区      空")

    if SITE.is_file():
        print(f"站点生成    {time.strftime('%m-%d %H:%M', time.localtime(SITE.stat().st_mtime))}"
              f"（{ago(SITE.stat().st_mtime)}）")
    else:
        print("站点生成    尚未生成")

    try:
        r = subprocess.run(["git", "status", "--porcelain"], cwd=str(BASE),
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        dirty = [l for l in (r.stdout or "").splitlines() if l.strip() and "_在编" not in l]
        print(f"未提交      {len(dirty)} 个文件" if dirty else "未提交      无（已全部推送）")
    except Exception:
        print("未提交      无法检查（git 不可用）")

    print("-" * 34)
    if LOG.is_file():
        lines = LOG.read_text(encoding="utf-8", errors="ignore").strip().splitlines()
        for line in lines[-8:]:
            print(line)
    else:
        print("（还没有监听日志）")

    print("-" * 34)
    if not running and pending:
        print("处理办法：双击 _馆务\\后台整理.bat，启动后会自动处理积压并推送。")
    elif not running:
        print("监听未运行。想恢复自动整理，双击 _馆务\\后台整理.bat（窗口可最小化）。")
        print("开机自启项：%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\知识库监听.lnk")
    elif pending:
        print("监听在运行，积压会在素材静止 25 秒后自动处理，稍等即可。")
    else:
        print("一切正常，没有积压。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
