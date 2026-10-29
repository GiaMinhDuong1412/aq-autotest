@echo off
chcp 65001 >nul
cd /d "%~dp0"
title AQ Autotest - doi mat khau Edusoft da luu
call :findpy
if not defined PY (
  echo Chua co Python. Hay chay cai-dat.bat truoc.
  pause
  exit /b 1
)
"%PY%" aqrun.py --quen-mat-khau & exit /b

:findpy
set "PY="
if exist "%~dp0python-path.txt" set /p PY=<"%~dp0python-path.txt"
if defined PY if not exist "%PY%" set "PY="
if not defined PY for %%P in ("%LOCALAPPDATA%\Programs\Python\Python313\python.exe" "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" "%LOCALAPPDATA%\Programs\Python\Python310\python.exe" "%ProgramFiles%\Python313\python.exe" "%ProgramFiles%\Python312\python.exe" "%ProgramFiles%\Python311\python.exe" "%ProgramFiles%\Python310\python.exe") do if not defined PY if exist "%%~P" set "PY=%%~P"
if not defined PY (
  py -3 --version >nul 2>&1
  if not errorlevel 1 for /f "delims=" %%i in ('py -3 -c "import sys;print(sys.executable)"') do set "PY=%%i"
)
if not defined PY (
  python --version >nul 2>&1
  if not errorlevel 1 for /f "delims=" %%i in ('python -c "import sys;print(sys.executable)"') do set "PY=%%i"
)
if defined PY (echo %PY%)>"%~dp0python-path.txt"
exit /b 0
