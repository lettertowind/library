#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把知识库同步到 GitHub。

用法：
    双击 _馆务/同步GitHub.bat
    或在命令行：python sync.py [提交说明]

行为：
    1. 检查是否有改动，没有就什么都不做
    2. 有改动则提交
    3. 推送到 GitHub

只做纯 git 操作，不碰卡片内容，不会自动合并冲突。
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(args, check=True):
    r = subprocess.run(args, cwd=ROOT, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if check and r.returncode != 0:
        raise RuntimeError(f"{' '.join(args)}\n{r.stdout}\n{r.stderr}")
    return r


def main():
    if not (ROOT / ".git").is_dir():
        print(f"[!] {ROOT} 不是 git 仓库")
        return 1

    remote = run(["git", "remote"], check=False).stdout.strip()
    if not remote:
        print("[!] 还没有配置远程仓库")
        print("    先执行：git remote add origin git@github.com:lettertowind/xxx.git")
        return 1

    branch = run(["git", "branch", "--show-current"], check=False).stdout.strip() or "main"

    status = run(["git", "status", "--porcelain"]).stdout.strip()
    if not status:
        print("[i] 没有改动，无需同步")
        ahead = run(["git", "rev-list", "--count", f"origin/{branch}..{branch}"],
                    check=False).stdout.strip()
        if ahead and ahead != "0":
            print(f"[i] 但有 {ahead} 个提交未推送，继续推送")
        else:
            return 0
    else:
        changed = len([l for l in status.splitlines() if l.strip()])
        print(f"[i] 检测到 {changed} 处改动")

        msg = " ".join(sys.argv[1:]).strip()
        if not msg:
            msg = f"同步 {datetime.now().strftime('%Y-%m-%d %H:%M')}"

        # 分类统计，让提交信息有内容
        added = len([l for l in status.splitlines() if l.startswith("??") or l.startswith("A ")])
        modified = len([l for l in status.splitlines() if l.startswith(" M") or l.startswith("M ")])
        deleted = len([l for l in status.splitlines() if l.startswith(" D") or l.startswith("D ")])
        detail = []
        if added:
            detail.append(f"新增 {added}")
        if modified:
            detail.append(f"修改 {modified}")
        if deleted:
            detail.append(f"删除 {deleted}")
        if detail:
            msg = f"{msg}（{'，'.join(detail)}）"

        run(["git", "add", "-A"])
        run(["git", "commit", "-m", msg])
        print(f"[√] 已提交：{msg}")

    print(f"[i] 推送到 {remote} / {branch} ...")
    push = run(["git", "push", "-u", "origin", branch], check=False)
    if push.returncode != 0:
        err = (push.stderr or push.stdout).strip()
        print("[!] 推送失败")
        print(err[-800:])
        if "rejected" in err or "non-fast-forward" in err:
            print("\n远端有本地没有的提交（可能是手机上改过）。")
            print("先执行：git pull --rebase origin " + branch)
        return 1

    print("[√] 已推送到 GitHub")
    total = run(["git", "rev-list", "--count", "HEAD"], check=False).stdout.strip()
    print(f"[i] 当前共 {total} 个提交")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[!] {e}")
        sys.exit(1)
