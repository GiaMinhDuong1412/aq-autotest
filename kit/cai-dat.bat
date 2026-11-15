@echo off
chcp 65001 >nul
rem --tu-dong: app AQ Auto Test goi (nut "Cai tu dong") - khong hoi, khong dung cho, ghi tien do vao cai-dat-trang-thai.txt
set "AUTO="
if /i "%~1"=="--tu-dong" set "AUTO=1"
set "STF=%~dp0cai-dat-trang-thai.txt"
net session >nul 2>&1
if not errorlevel 1 goto :admin
if defined AUTO (>"%STF%" echo 0^|uac)
rem Chua co quyen admin: ghi lai ho so nguoi dang dung may roi tu mo lai voi quyen admin
> "%PUBLIC%\aq-autotest-user.txt" echo %APPDATA%
>> "%PUBLIC%\aq-autotest-user.txt" echo %LOCALAPPDATA%
>> "%PUBLIC%\aq-autotest-user.txt" echo %USERPROFILE%
echo Dang xin quyen admin - chon Yes khi Windows hoi...
if defined AUTO (
  powershell -NoProfile -ExecutionPolicy Bypass -Command "Start-Process -FilePath '%~f0' -ArgumentList '--tu-dong' -Verb RunAs -WindowStyle Minimized"
) else (
  powershell -NoProfile -ExecutionPolicy Bypass -Command "Start-Process -FilePath '%~f0' -Verb RunAs"
)
if errorlevel 1 goto :noadmin
exit /b 0

:noadmin
if defined AUTO (
  >>"%STF%" echo loi^|uac
  exit /b 1
)
echo.
echo Khong tu xin duoc quyen admin.
echo Hay chuot phai vao cai-dat.bat, chon "Run as administrator".
pause
exit /b 1

:admin
set "AQ_USER_APPDATA="
set "AQ_USER_LOCALAPPDATA="
set "AQ_USER_USERPROFILE="
if exist "%PUBLIC%\aq-autotest-user.txt" call :readuser
if not defined AQ_USER_APPDATA set "AQ_USER_APPDATA=%APPDATA%"
if not defined AQ_USER_LOCALAPPDATA set "AQ_USER_LOCALAPPDATA=%LOCALAPPDATA%"
if not defined AQ_USER_USERPROFILE set "AQ_USER_USERPROFILE=%USERPROFILE%"
echo === AQ Autotest - cai dat (chay lai moi khi tai bo test .zip moi) ===

rem ---- 1. Chon thu muc cai co dinh (mac dinh %USERPROFILE%\AQ-Autotest, doi duoc tren console hoac go o day)
set "SRC=%~dp0"
if "%SRC:~-1%"=="\" set "SRC=%SRC:~0,-1%"
set "DEST="
if exist "%SRC%\thu-muc-cai.txt" set /p DEST=<"%SRC%\thu-muc-cai.txt"
if not defined DEST set "DEST=%AQ_USER_USERPROFILE%\AQ-Autotest"
if defined AUTO set "DEST=%SRC%"
call :st 1 chep
echo.
echo Thu muc cai bo test: %DEST%
set "ANS="
if not defined AUTO set /p "ANS=Nhan Enter de dong y, hoac go thu muc khac (vd D:\AQ-Autotest): "
if defined ANS set "DEST=%ANS:"=%"
if "%DEST:~-1%"=="\" set "DEST=%DEST:~0,-1%"
if /i not "%SRC%"=="%DEST%" (
  if not exist "%DEST%" mkdir "%DEST%"
  if not exist "%DEST%" (
    echo LOI: khong tao duoc thu muc %DEST%
    call :st loi thu-muc
    if not defined AUTO pause
    exit /b 1
  )
  echo Chep bo test vao %DEST% ...
  robocopy "%SRC%" "%DEST%" /E /XD results /XF python-path.txt /NFL /NDL /NJH /NJS /NP >nul
  if errorlevel 8 (
    echo LOI: khong chep duoc bo test vao %DEST%
    call :st loi thu-muc
    if not defined AUTO pause
    exit /b 1
  )
)
if not exist "%DEST%\results" mkdir "%DEST%\results"
(echo %DEST%)>"%DEST%\thu-muc-cai.txt"
set "K=%DEST%\"
set "STF=%K%cai-dat-trang-thai.txt"
cd /d "%DEST%"
echo Da cai vao: %DEST%   (tu gio chi dung thu muc nay; thu muc giai nen .zip xoa duoc)

rem ---- 2. Python va thu vien
call :st 2 python
call :findpy
if not defined PY (
  echo Chua co Python tren may. Dang cai Python 3.12...
  where winget >nul 2>nul
  if not errorlevel 1 winget install -e --id Python.Python.3.12 --scope user --silent --accept-package-agreements --accept-source-agreements
  call :findpy
)
if not defined PY (
  echo Tai bo cai Python 3.12 tu python.org...
  powershell -NoProfile -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol='Tls12';Invoke-WebRequest 'https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe' -OutFile '%TEMP%\aq-python-setup.exe' -UseBasicParsing"
  if exist "%TEMP%\aq-python-setup.exe" "%TEMP%\aq-python-setup.exe" /quiet InstallAllUsers=0 PrependPath=0 Include_test=0 Include_launcher=0 Shortcuts=0
  del "%TEMP%\aq-python-setup.exe" >nul 2>&1
  call :findpy
)
if not defined PY goto :manual
echo Dung Python: %PY%
call :st 3 thu-vien
if defined AUTO (
  "%PY%" -m pip install --upgrade pip >>"%K%cai-dat.log" 2>&1
  "%PY%" -m pip install --upgrade pywinauto pillow keyboard keyring obsws-python openpyxl >>"%K%cai-dat.log" 2>&1
) else (
  "%PY%" -m pip install --upgrade pip
  "%PY%" -m pip install --upgrade pywinauto pillow keyboard keyring obsws-python openpyxl
)
if errorlevel 1 (
  echo.
  echo LOI: khong cai duoc thu vien. Kiem tra mang Internet roi chay lai cai-dat.bat.
  call :st loi thu-vien
  if not defined AUTO pause
  exit /b 1
)
set "PYW=%PY:python.exe=pythonw.exe%"
if not exist "%PYW%" set "PYW=%PY%"

rem ---- 3. Agent chay nen
call :st 4 agent
echo.
echo Cai AQ Autotest Agent (chay nen, nhan lenh "Chay test" va "Cap nhat bo test" tu console)...
reg delete "HKCU\Software\Classes\aqautotest" /f >nul 2>&1
schtasks /end /tn "AQ Autotest Agent" >nul 2>&1
schtasks /create /tn "AQ Autotest Agent" /tr "\"%PYW%\" \"%K%aq-agent.py\"" /sc onlogon /rl highest /f >nul
if errorlevel 1 (
  echo Khong cai duoc Agent - van chay test bang chay-test.bat duoc.
) else (
  schtasks /run /tn "AQ Autotest Agent" >nul
  echo Da cai va bat Agent.
)

rem ---- 4. Cau noi + kiem tra cai dat (bang ket qua o cuoi; neu can se hoi khoi dong lai Claude app)
call :st 5 kiem-tra
echo.
"%PY%" "%K%aqrun.py" --cap-nhat
if defined AUTO (
  "%PY%" "%K%aqrun.py" --chan-doan
) else (
  "%PY%" "%K%aqrun.py" --chan-doan --khoi-dong-claude
)
call :st 9 xong
echo.
echo Xong. Ket qua kiem tra luu o %K%chan-doan.txt
if not defined AUTO pause
exit /b 0

:st
rem ghi tien do cho app: <buoc>|<ma>
>>"%STF%" echo %~1^|%~2
exit /b 0

:manual
call :st loi python
if defined AUTO exit /b 1
echo.
echo Khong tu cai duoc Python. Hay cai tay:
echo   1. Mo https://www.python.org/downloads/ va tai Python 3.12
echo   2. Khi cai, tick "Add python.exe to PATH"
echo   3. Chay lai cai-dat.bat
pause
exit /b 1

:findpy
set "PY="
if exist "%K%python-path.txt" set /p PY=<"%K%python-path.txt"
if defined PY if not exist "%PY%" set "PY="
if not defined PY for %%P in ("%AQ_USER_LOCALAPPDATA%\Programs\Python\Python313\python.exe" "%AQ_USER_LOCALAPPDATA%\Programs\Python\Python312\python.exe" "%AQ_USER_LOCALAPPDATA%\Programs\Python\Python311\python.exe" "%AQ_USER_LOCALAPPDATA%\Programs\Python\Python310\python.exe" "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" "%ProgramFiles%\Python313\python.exe" "%ProgramFiles%\Python312\python.exe" "%ProgramFiles%\Python311\python.exe" "%ProgramFiles%\Python310\python.exe") do if not defined PY if exist "%%~P" set "PY=%%~P"
if not defined PY (
  py -3 --version >nul 2>&1
  if not errorlevel 1 for /f "delims=" %%i in ('py -3 -c "import sys;print(sys.executable)"') do set "PY=%%i"
)
if not defined PY (
  python --version >nul 2>&1
  if not errorlevel 1 for /f "delims=" %%i in ('python -c "import sys;print(sys.executable)"') do set "PY=%%i"
)
if defined PY (echo %PY%)>"%K%python-path.txt"
exit /b 0

:readuser
< "%PUBLIC%\aq-autotest-user.txt" (
  set /p AQ_USER_APPDATA=
  set /p AQ_USER_LOCALAPPDATA=
  set /p AQ_USER_USERPROFILE=
)
del "%PUBLIC%\aq-autotest-user.txt" >nul 2>&1
exit /b 0
