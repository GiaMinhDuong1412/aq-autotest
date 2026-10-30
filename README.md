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

## Chạy trên server công ty (gắn domain)
Chỉ cần **một file `aq-console-server.py`** (cần Python 3.8+ trên server, không cần git):
1. Chép file vào một thư mục trống trên server, chạy `python aq-console-server.py`.
   Lần đầu file tạo `aq-console-server.json`. Repo GitHub riêng tư nên phải điền `"token"`: token chỉ-đọc
   (github.com → Settings → Developer settings → Fine-grained tokens, chỉ chọn repo này, Contents = Read-only).
   Lưu file; trong vòng 2 phút console tự tải code và chạy ở cổng `port` (mặc định 8787).
2. Mở trang, đăng nhập `admin`, mật khẩu trong `aq-console/rieng/mat-khau-admin-lan-dau.txt`. Vào **Hồ sơ**
   (trang `/quan-tri`) để đổi mật khẩu và thêm tài khoản cho từng người.
3. Windows: chạy `python aq-console-server.py --tu-chay` bằng quyền admin để console tự chạy nền mỗi khi bật máy và mở cổng
   trên tường lửa. Trỏ domain về server, mở cổng. Muốn https: điền `cert`/`key` (.pem) và đặt `port` 443, hoặc để
   IIS/nginx/Cloudflare lo https.

Sau đó không cần làm gì trên server: cứ 2 phút file hỏi GitHub nhánh `branch` (mặc định `main`), có commit mới thì tự tải,
kiểm tra, thay và khởi động lại (bản lỗi thì quay về bản cũ). Chính file này cũng tự cập nhật.
Dữ liệu ở `aq-console/du-lieu` (không bị ghi đè khi cập nhật code; kịch bản sửa trong repo chỉ được đưa vào khi mới hơn theo
`updatedAt`), sao lưu mỗi ngày ở `aq-console/sao-luu`, nhật ký ở `aq-console/nhat-ky.txt`.
Console trên server không nối trực tiếp máy chạy test: nút **Chạy** tải file lệnh về máy người bấm, Agent trên máy test nhận từ
thư mục Tải về (mở console trên chính máy test); kết quả nhập bằng **Nhập kết quả…**.

### Cài dưới IIS (cùng kiểu AQBuild – dùng chung domain/https của IIS)
`python tools/dong_goi_iis.py` tạo `AQAutotest-IIS-cai-dat.zip`; giải nén trên server, sửa `CaiDat.settings.json`
(thư mục con của site có sẵn như `demo.aqtech.vn/aqautotest/`, hoặc site riêng theo domain), chạy `CAI-DAT.cmd` một lần.
IIS chạy `aq-console-server.py --iis` qua AspNetCoreModuleV2 (có sẵn khi đã cài .NET Hosting Bundle), Python nhúng nằm trong
thư mục đích. Chi tiết: `server-iis/HUONG-DAN.md`.

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
| `aq-console-server.py` | bản chạy trên server: tự tải code từ GitHub, tự cập nhật, bắt đăng nhập |
| `server-iis/` | gói cài dưới IIS (`CAI-DAT.cmd`, `Cai-Dat.ps1`, `CaiDat.settings.json`, `HUONG-DAN.md`) |
| `tools/embed_kit.py` | nhúng lại `kit/` vào `web/index.html` trước khi commit |

## Giới hạn so với bản trên claude.ai
- Nút *Đồng bộ tài liệu* (đọc SharePoint) và các chức năng nhờ Claude viết kịch bản trên trang không chạy ở localhost –
  làm việc đó bằng Claude Code hoặc Claude app rồi lưu vào `data/`.
- Màn hình đăng nhập đầu trang là màn hình minh hoạ: bấm *Vào console*.
