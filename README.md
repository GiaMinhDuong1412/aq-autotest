# AQ Autotest Console (localhost)

Console quản lý kịch bản test Edusoft.NET / Netweb của AQTech + bộ test chạy kịch bản thật trên Edusoft.
Chạy trên máy bằng Python, dữ liệu là file JSON trong `data/`, đồng bộ giữa các máy bằng GitHub.

## Cài lần đầu trên mỗi máy (laptop, PC)
1. Cài **Python 3.10+** (https://www.python.org/downloads/ – tick *Add python.exe to PATH*) và **Git** (https://git-scm.com/download/win).
2. Lấy mã nguồn:
   ```
   git clone https://github.com/<tài-khoản>/aq-autotest.git
   cd aq-autotest
   ```
3. Mở console: chạy **`chay-console.bat`** (hoặc `python server.py`) → trình duyệt mở http://localhost:8787.

Không cần cài thư viện nào cho console. Claude Code: mở thư mục `aq-autotest` rồi chạy `claude` – Claude đọc `CLAUDE.md`
và skill `tailieu-edusoft` trong `.claude/skills/`.

## Máy chạy test (máy có Edusoft)
1. Trên console → **Máy chạy thử** → khung *Kết nối trực tiếp máy chạy test*: nhập thư mục bộ test
   (vd `D:\AQ-Autotest-DangNhap-20261029\AQ-Autotest`) → **Lưu thư mục**. Máy mới chưa có bộ test thì nhập thư mục trống
   và bấm **Cài bộ test vào đây**, rồi chạy `cai-dat.bat` trong thư mục đó một lần (quyền admin: cài thư viện + Agent).
2. Bấm **Chạy** ở kịch bản (CHUNG-001, QLSV-001…). Lệnh và bản bộ test mới nhất được ghi thẳng vào thư mục bộ test,
   AQ Autotest Agent mở cửa sổ test sau vài giây; chạy xong kết quả (ảnh, lỗi, cây giao diện) tự về console.
3. Tắt Unikey/EVKey khi chạy test (script gõ phím thật).

Máy không có Edusoft (vd laptop) vẫn xem / sửa kịch bản, xem kết quả bình thường.

## Đồng bộ laptop ↔ PC
- Trước và sau mỗi buổi làm việc chạy **`dong-bo.bat`**: lưu thay đổi của máy này, lấy thay đổi của máy kia, đẩy lên GitHub.
  Console đang mở sẽ tự cập nhật sau vài giây khi dữ liệu đổi.
- `local/` (thư mục bộ test của từng máy, mật khẩu Netweb) không đồng bộ.

## Thư mục
| | |
|---|---|
| `server.py` | server localhost (chỉ thư viện chuẩn Python) |
| `web/index.html` | giao diện console |
| `web/claude-shim.js` | lớp thay thế API của claude.ai khi chạy localhost |
| `kit/` | bộ test cài trên máy chạy test (`aqrun.py`, `aq-agent.py`, `cai-dat.bat`…) |
| `data/` | kịch bản, lượt chạy, lỗi, release, danh mục kế hoạch, ảnh |
| `tools/embed_kit.py` | nhúng lại `kit/` vào `web/index.html` trước khi commit |

## Giới hạn so với bản trên claude.ai
- Nút *Đồng bộ tài liệu* (đọc SharePoint) và các chức năng nhờ Claude viết kịch bản trên trang không chạy ở localhost –
  làm việc đó bằng Claude Code hoặc Claude app rồi lưu vào `data/`.
- Màn hình đăng nhập đầu trang là màn hình minh hoạ: bấm *Vào console*.
