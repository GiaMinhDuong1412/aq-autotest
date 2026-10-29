# AQ Autotest – hướng dẫn cho Claude Code

Console quản lý kịch bản test Edusoft.NET / Netweb của AQTech, chạy trên **localhost**, kèm **bộ test** (Python + pywinauto)
chạy kịch bản thật trên Edusoft ở máy Windows. Người dùng nói tiếng Việt – trả lời tiếng Việt, ngắn gọn.

## Cấu trúc
- `server.py` – server Python **chỉ thư viện chuẩn** (không thêm dependency). Phục vụ `web/index.html`, API dữ liệu,
  ảnh (`/_blob/<id>`) và thao tác thư mục bộ test (`/api/kit/<tool>`: status, send, list_results, read_result,
  read_file, set_kit_dir, install). Chỉ nghe `127.0.0.1`; POST/PUT/PATCH/DELETE phải có header `X-AQ: 1`.
- `web/index.html` – trang console (một file, cũng là bản artifact trên claude.ai). Mã JS nằm trong `<script>` cuối file.
  Các khối `<script type="text/plain" id="kit-…">` là bản nhúng của `kit/*`; server tự nhúng lại khi phục vụ,
  trước khi commit chạy `python tools/embed_kit.py` để file luôn khớp.
- `web/claude-shim.js` – thay `window.claude` của claude.ai: db (Firestore-like: collection/doc/get/set/update/delete/add/
  orderBy/where/limit/onSnapshot), user, assets, downloads, permissions, mcp (`host:aq-autotest` → `/api/kit`).
  Biến `window.AQ_LOCAL` có nghĩa đang chạy localhost.
- `kit/` – bộ test cài trên máy chạy test: `aqrun.py` (chạy kịch bản, `KIT_VERSION` ở đầu file – **tăng mỗi lần sửa kit**),
  `aq-agent.py` (chạy nền quyền admin, nhận file lệnh `aq-autotest-update-run.json` trong thư mục bộ test),
  `cai-dat.bat`, `chay-test.bat`, `quen-mat-khau.bat`, `HUONG-DAN.txt`.
- `data/` – dữ liệu dùng chung, đồng bộ qua git: `scenarios/`, `runs/`, `bugs/`, `runners/`, `releases/`, `releaseItems/`,
  `testPlans/`, `settings/`, `assets/` (ảnh). Mỗi bản ghi = `data/<collection>/<doc_id>.json`.
- `local/` – riêng từng máy, **gitignore**: `config.json` (`port`, `kitDir`, `userId`, `userName`), `users/<id>/secrets.json`.
- `.claude/skills/tailieu-edusoft/` – kiến thức nghiệp vụ: tài liệu Edusoft, cách dựng kịch bản, schema dữ liệu, release.

## Chạy & kiểm tra
- Chạy console: `python server.py` (hoặc `chay-console.bat`) → http://localhost:8787. `--port`, `--no-browser`.
- Kiểm tra cú pháp: `python -m py_compile server.py kit/aqrun.py kit/aq-agent.py`; JS: tách khối `<script>` cuối
  `web/index.html` ra file rồi `node --check`.
- Đồng bộ 2 máy: `dong-bo.bat` (commit tất cả → `git pull --rebase --autostash` → `git push`). Gặp xung đột trong
  `data/*.json`: giữ bản có `updatedAt` mới hơn, hoặc gộp trường nếu hai máy sửa trường khác nhau.

## Kịch bản chạy bằng script
- Kịch bản có `scriptReady: true` (và CHUNG-001) mới hiện ở mục "Kịch bản chạy bằng script" trên trang Máy chạy thử.
- `vars` – biến dùng trong bước, vd `{"MSSV": "AUTO{ddHHMM}"}` (có sẵn `{ddHHMM}`, `{yymmdd}`, `{HHMMSS}`, `{ddmmyyyy}`).
- `auto[i]` – danh sách lệnh cho bước i (xem docstring `Run.do_actions` trong `kit/aqrun.py`): `menu:`, `click:`, `type:`,
  `select:`, `date:`, `save:`, `expect:`, `expect_dialog:`, `find_row:`, `delete_row:`, `cancel`, `dump:`, `key:`, `wait:`;
  thêm `?` sau tên lệnh (vd `select?:`) để bỏ qua khi không thấy phần tử. Nhiều tên thay thế cách nhau `|`.
- Luồng thay thế: `auto`, `needs: "main"` (chỉ chạy khi luồng chính đạt), `always: true`, `after: [lệnh dọn]`.
- Giao diện Edusoft HVNG: ribbon (TabItem "Sinh viên"…) → nút ribbon (vd "Sinh viên học kỳ") → cây "Danh mục chức năng"
  bên trái (TreeItem tên `NodeN`, chữ nằm ở Value) → màn hình mở trong tab MDI. Khi script dừng, nó ghi `ui-*.txt`
  (cây UI Automation) vào thư mục lượt chạy – đọc file đó để sửa tên ô/nút trong `auto`.
- Ô nhập DevExpress: phải gõ phím thật sau khi đặt focus bằng UIA (`set_field`); xóa bằng End + Backspace (Ctrl+A không chạy);
  không dùng Invoke cho nút mở hộp thoại; Edusoft chạy quyền admin nên bộ test phải chạy quyền admin (Agent lo việc này).

## Quy tắc an toàn (bắt buộc)
- Tài khoản test `admindh` chỉ dùng cho môi trường demo/test. **Không** ghi mật khẩu vào `data/`, kịch bản, log hay commit;
  mật khẩu Edusoft nằm trong Windows Credential Manager trên máy chạy test (do `aqrun.py` hỏi), mật khẩu Netweb ở `local/`.
- Không đọc/hiển thị mật khẩu email SMTP trong `client.config` của Edusoft.
- Chỉ thao tác bản **EDUSOFT - HVNG - Copy** (`E:\AQ - Works\EDUSOFT_ALL_ENV\EDUSOFT - HVNG - Copy\Edusoft.NET.exe`), không đụng
  các môi trường Edusoft khác. Dữ liệu test có tiền tố rõ ràng (`AUTO…`, `TEST_…`) và có luồng dọn dữ liệu; xóa chỉ khi hộp
  thoại xác nhận nêu đúng mã dữ liệu test.
- Hỏi người dùng trước khi thêm thao tác làm thay đổi dữ liệu ngoài phạm vi kịch bản. Không sửa file Excel gốc trừ khi được yêu cầu.
- Gõ phím thật nên chuỗi nhập tránh tổ hợp Telex (dd, aa, s/f/r/x/j sau nguyên âm…) và nhắc tắt Unikey/EVKey khi chạy.
