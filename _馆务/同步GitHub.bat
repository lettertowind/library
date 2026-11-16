@echo off
chcp 65001 >nul
title KB Sync to GitHub
set "PYTHONUTF8=1"
set "PY=python"
where python >nul 2>&1 || set "PY=C:\Users\Sean\WorkBuddy\spaces\2026_11_16_19-04-52\BiliNote\backend\.venv\Scripts\python.exe"
"%PY%" "%~dp0sync.py" %*
echo.
pause
