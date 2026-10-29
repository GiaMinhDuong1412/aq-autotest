@echo off
chcp 65001 >nul
net session >nul 2>&1
if errorlevel 1 (
  if "%~1"=="" (
    powershell -NoProfile -Command "Start-Process -FilePath '%~f0' -Verb RunAs"
  ) else (
    powershell -NoProfile -Command "Start-Process -FilePath '%~f0' -ArgumentList '%*' -Verb RunAs"
  )
  exit /b
)
cd /d "%~dp0"
title AQ Autotest - test dang nhap Edusoft
call :findpy
if not defined PY (
  echo Chua co Python. Hay chay cai-dat.bat truoc.
  pause
  exit /b 1
)
rem Dong duoi phai nam tren MOT dong: aqrun.py co the tu cap nhat chinh file .bat nay khi dang chay.
"%PY%" aqrun.py %* & (if errorlevel 1 pause) & exit /b

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
