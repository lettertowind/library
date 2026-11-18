@echo off
chcp 65001 >nul
title Stop KB Watcher
cd /d "%~dp0"
set "PY=C:\Users\Sean\WorkBuddy\spaces\2026_11_16_19-04-52\BiliNote\backend\.venv\Scripts\python.exe"
set "PYTHONUTF8=1"
"%PY%" "%~dp0stop.py"
ping -n 4 127.0.0.1 >nul 2>&1
