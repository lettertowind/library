@echo off
chcp 65001 >nul
title Process Bilibili Link
set "PYTHONUTF8=1"
set "PY=python"
where python >nul 2>&1 || set "PY=C:\Users\Sean\WorkBuddy\spaces\2026_11_16_19-04-52\BiliNote\backend\.venv\Scripts\python.exe"

echo.
echo Paste a Bilibili link (b23.tv or full URL), then press Enter.
echo Leave empty to cancel.
echo.
set /p LINK=Link: 
if "%LINK%"=="" (
    echo Cancelled.
    timeout /t 2 >nul
    exit /b 0
)

echo.
"%PY%" "%~dp0pipeline.py" "%LINK%"
echo.
pause
