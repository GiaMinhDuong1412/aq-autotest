@echo off
chcp 65001 >nul
cd /d "%~dp0"
rem Đồng bộ mã nguồn + dữ liệu (data/) với GitHub: lấy thay đổi từ máy kia rồi đẩy thay đổi của máy này.
where git >nul 2>nul
if errorlevel 1 (
  echo Chua co Git. Cai tu https://git-scm.com/download/win roi chay lai.
  pause
  exit /b 1
)
git add -A
git diff --cached --quiet
if errorlevel 1 git commit -m "Cap nhat tu %COMPUTERNAME% %DATE% %TIME%"
git pull --rebase --autostash
if errorlevel 1 (
  echo.
  echo Co xung dot khi gop thay doi. Mo Claude Code trong thu muc nay va nho "giai quyet xung dot git".
  pause
  exit /b 1
)
git push
echo.
echo Da dong bo xong.
timeout /t 3 >nul
