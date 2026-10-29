@echo off
chcp 65001 >nul
net session >nul 2>&1
if errorlevel 1 (
  powershell -NoProfile -Command "Start-Process -FilePath '%~f0' -Verb RunAs"
  exit /b
)
cd /d "%~dp0"
echo === AQ Autotest - cai dat (chay lai moi khi tai bo test .zip moi) ===
call :findpy
if not defined PY (
  echo Chua co Python tren may. Dang cai Python 3.12 bang winget...
  where winget >nul 2>nul
  if errorlevel 1 goto :manual
  winget install -e --id Python.Python.3.12 --scope user --accept-package-agreements --accept-source-agreements
  call :findpy
)
if not defined PY goto :manual
echo Dung Python: %PY%
"%PY%" -m pip install --upgrade pip
"%PY%" -m pip install --upgrade pywinauto pillow keyboard keyring obsws-python openpyxl
if errorlevel 1 (
  echo.
  echo LOI: khong cai duoc thu vien. Kiem tra mang Internet roi chay lai cai-dat.bat.
  pause
  exit /b 1
)
set "PYW=%PY:python.exe=pythonw.exe%"
if not exist "%PYW%" set "PYW=%PY%"
echo.
echo Cai AQ Autotest Agent (chay nen, nhan lenh "Chay test" va "Cap nhat bo test" tu console)...
reg delete "HKCU\Software\Classes\aqautotest" /f >nul 2>&1
schtasks /end /tn "AQ Autotest Agent" >nul 2>&1
schtasks /create /tn "AQ Autotest Agent" /tr "\"%PYW%\" \"%~dp0aq-agent.py\"" /sc onlogon /rl highest /f >nul
if errorlevel 1 (
  echo Khong cai duoc Agent - van chay test bang chay-test.bat duoc.
) else (
  schtasks /run /tn "AQ Autotest Agent" >nul
  echo Da cai va bat Agent. Tu gio bam "Chay test dang nhap" tren console de chay test tren may nay.
)
echo.
"%PY%" "%~dp0aqrun.py" --cap-nhat >nul 2>&1
echo Mo console: chay chay-console.bat trong thu muc du an aq-autotest (http://localhost:8787).
echo.
echo Xong.
pause
exit /b 0

:manual
echo.
echo Khong tu cai duoc Python. Hay cai tay:
echo   1. Mo https://www.python.org/downloads/ va tai Python 3.12
echo   2. Khi cai, tick "Add python.exe to PATH"
echo   3. Chay lai cai-dat.bat
pause
exit /b 1

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
