# -*- coding: utf-8 -*-
"""停止后台监听：按命令行精确匹配 watcher.py 的进程，避免误杀别的 python。"""
import subprocess
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

PS = (
    "Get-CimInstance Win32_Process -Filter \"name='python.exe' or name='pythonw.exe'\" | "
    "Where-Object { $_.CommandLine -like '*watcher.py*' } | "
    "Select-Object -ExpandProperty ProcessId"
)


def main():
    r = subprocess.run(["powershell", "-NoProfile", "-Command", PS],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    pids = [x.strip() for x in (r.stdout or "").split() if x.strip().isdigit()]
    if not pids:
        print("没有监听到在运行的监听进程。")
        return 0
    for pid in pids:
        k = subprocess.run(["taskkill", "/PID", pid, "/F"],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        ok = k.returncode == 0
        print(f"{'已停止' if ok else '停止失败'} PID {pid}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
