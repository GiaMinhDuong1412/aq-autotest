@echo off
setlocal
title AQ Autotest Console - CAI DAT TREN IIS
cd /d "%~dp0"
echo AQ Autotest Console - cai dat tren IIS (chay mot lan, sau do tu cap nhat tu GitHub)
echo.
"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -ExecutionPolicy Bypass -File "%~dp0Cai-Dat.ps1"
set "aq_exit=%errorlevel%"
echo.
if "%aq_exit%"=="0" (echo CAI DAT XONG.) else (echo CAI DAT THAT BAI. Xem thong bao o tren hoac file cai-dat-log.txt)
echo Bam phim bat ky de dong cua so.
pause >nul
exit /b %aq_exit%
