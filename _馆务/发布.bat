@echo off
chcp 65001 >nul
title Publish Knowledge Base
set "PYTHONUTF8=1"
set "PY=python"
where python >nul 2>&1 || set "PY=C:\Users\Sean\WorkBuddy\spaces\2026_11_16_19-04-52\BiliNote\backend\.venv\Scripts\python.exe"

echo.
echo === Building site ===
"%PY%" "%~dp0site.py"
if errorlevel 1 (
    echo.
    echo [!] Build failed, nothing published.
    pause
    exit /b 1
)

echo.
echo === Publishing to GitHub ===
"%PY%" "%~dp0sync.py" "publish site"
echo.
pause
