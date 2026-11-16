@echo off
chcp 65001 >nul
title 知识库
set "PY=C:\Users\Sean\WorkBuddy\spaces\2026_11_16_19-04-52\BiliNote\backend\.venv\Scripts\python.exe"
set "PYTHONUTF8=1"
"%PY%" "%~dp0maintain.py" menu
echo.
pause
