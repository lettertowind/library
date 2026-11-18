# -*- coding: utf-8 -*-
"""在后台启动监听（无窗口），并给出中文提示。bat 只负责调用本脚本。"""
import subprocess
import sys
import time
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

OFFICE = Path(__file__).resolve().parent
PYW = Path(r"C:\Users\Sean\WorkBuddy\spaces\2026_11_16_19-04-52\BiliNote\backend\.venv\Scripts\pythonw.exe")
DETACHED = 0x00000008 | 0x00000200          # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP


def main():
    sys.path.insert(0, str(OFFICE))
    import status

    if status.watcher_running():
        print("监听已在后台运行，无需重复启动。")
        print("  查看它在做什么 → 状态.bat")
        print("  停掉它         → 停止监听.bat")
        return 0

    if not PYW.is_file():
        print(f"找不到 pythonw.exe：{PYW}")
        return 1

    subprocess.Popen([str(PYW), str(OFFICE / "watcher.py")], cwd=str(OFFICE),
                     creationflags=DETACHED, close_fds=True)
    time.sleep(2)

    if status.watcher_running():
        print("已在后台启动监听（无窗口、不占任务栏）。")
        print()
        print("  查看状态 → 状态.bat")
        print("  停止监听 → 停止监听.bat")
        print("  运行日志 → _馆务\\监听日志.txt")
        print()
        print("下次开机登录会自动启动，不用每次手动点。")
        return 0

    print("启动似乎没成功。请双击 状态.bat 看详情，或直接跑 后台整理.bat 观察报错。")
    return 1


if __name__ == "__main__":
    sys.exit(main())
