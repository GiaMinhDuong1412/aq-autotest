; Chạy trước khi cài / cập nhật: tắt AQ Auto Test đang chạy và server Python nhúng của nó (resources\python\pythonw.exe
; trong thư mục cài) để không bị khoá file. Không đụng tới Python khác trên máy (vd bộ test aqrun.py / aq-agent.py).
!macro customInit
  nsExec::Exec 'taskkill /f /im "AQ Auto Test.exe"'
  Pop $0
  nsExec::Exec `powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-Process pythonw,python -ErrorAction SilentlyContinue | Where-Object { $$_.Path -like '$LOCALAPPDATA\Programs\aq-auto-test\*' } | Stop-Process -Force"`
  Pop $0
!macroend
