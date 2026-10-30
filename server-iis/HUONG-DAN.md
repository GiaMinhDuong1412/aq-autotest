# AQ Autotest Console – cài trên IIS (cùng kiểu AQBuild)

Cài **một lần**. Sau đó console tự cập nhật từ GitHub: mỗi 2 phút hỏi nhánh `Branch`, có commit mới thì tự tải, kiểm tra,
thay và chạy lại (gián đoạn vài giây, bản lỗi thì quay về bản cũ). Không cần gói UPDATE như AQBuild.

Yêu cầu: Windows x64, IIS, **.NET Hosting Bundle** (máy đã chạy AQBuild là có – cần AspNetCoreModuleV2), server ra được
Internet tới `api.github.com` và `python.org` (tải Python nhúng lần đầu, nằm gọn trong thư mục đích, không cài vào Windows).

## Cài
1. Giải nén `AQAutotest-IIS-cai-dat.zip` (tạo bằng `python tools/dong_goi_iis.py`) vào thư mục riêng trên server,
   vd `C:\Demo\AQAUTOTEST-cai-dat` – không giải nén vào thư mục đích.
2. Mở `CaiDat.settings.json`, chọn một trong hai cách:
   - **Thư mục con của site có sẵn** (như AQBuild `https://demo.aqtech.vn/aqbuild.netweb/`):
     `"Mode": "app"`, `"SiteName": "AQ"`, `"AppPath": "/aqautotest"` → `https://demo.aqtech.vn/aqautotest/`.
     Dùng luôn https/chứng chỉ của site.
   - **Domain riêng**: `"Mode": "site"`, `"SiteName": "AQ Autotest"`, `"HostName": "autotest.aqtech.vn"`.
     Script tạo site, gắn https nếu máy có chứng chỉ khớp domain (kể cả wildcard `*.aqtech.vn`); không có thì thêm
     binding https trong IIS Manager như các site khác. Nhớ trỏ DNS domain về server.

   `TargetPath` là nơi chứa chương trình và dữ liệu (mặc định `C:\Demo\AQAUTOTEST`).
3. Double-click **`CAI-DAT.cmd`**, chọn Yes khi Windows hỏi quyền Administrator. Khi được hỏi, dán **token GitHub chỉ-đọc**:
   github.com → Settings → Developer settings → Fine-grained tokens → Generate new token →
   Repository access = *Only select repositories* (chọn `aq-autotest`), Permissions → **Contents = Read-only**.
4. Chờ đến `CAI DAT THANH CONG`. Mở địa chỉ được in ra, đăng nhập `admin` – mật khẩu trong
   `<TargetPath>\aq-console\rieng\mat-khau-admin-lan-dau.txt`. Vào **Hồ sơ** để đổi mật khẩu, thêm tài khoản rồi xoá file đó.

## Script làm gì
- Kiểm tra IIS có AspNetCoreModuleV2, site đích có thật.
- Chép `aq-console-server.py`, tải Python nhúng 3.12 vào `<TargetPath>\python`, ghi `aq-console-server.json` (repo, nhánh, token)
  và `web.config` (IIS chạy Python qua AspNetCoreModuleV2, out-of-process).
- Tạo App Pool `AQAutotest` (No Managed Code, AlwaysRunning, không tắt khi rảnh), cấp quyền Modify thư mục đích cho App Pool,
  tạo/cập nhật ứng dụng hoặc site. Không đổi ExecutionPolicy hệ thống, DNS, chứng chỉ, các site/ứng dụng khác.
- Chạy lại `CAI-DAT.cmd` an toàn: giữ token, dữ liệu, tài khoản đã có.

## Thư mục trên server
| | |
|---|---|
| `aq-console-server.json` | cấu hình: `repo`, `branch`, `token`, `checkMinutes`. Sửa token/nhánh không cần khởi động lại |
| `aq-console\app` | code tải từ GitHub (bị thay khi có bản mới – đừng sửa tay) |
| `aq-console\du-lieu` | dữ liệu: kịch bản, lượt chạy, lỗi, release, ảnh. Không bị ghi đè khi cập nhật |
| `aq-console\rieng` | tài khoản (`auth.json`), cấu hình riêng |
| `aq-console\sao-luu` | sao lưu dữ liệu mỗi ngày (giữ 14 bản) |
| `aq-console\nhat-ky.txt` | nhật ký: cập nhật, lỗi tải code, khởi động lại |

## Khi có sự cố
- Trang báo "GitHub từ chối…": token sai/hết hạn → sửa `token` trong `aq-console-server.json`, đợi 2 phút.
- Lỗi IIS 502.5 / 500.30: xem `aq-console\nhat-ky.txt`; Recycle App Pool `AQAutotest`.
- Quay về bản trước: sao lưu dữ liệu ở `aq-console\sao-luu`; code luôn là bản mới nhất chạy được của nhánh.
- Gỡ: xoá ứng dụng/site và App Pool `AQAutotest` trong IIS Manager, xoá `TargetPath` (giữ `aq-console\du-lieu` nếu cần dữ liệu).

Console trên server không nối thẳng máy chạy test (máy có Edusoft): nút **Chạy** tải file lệnh về máy người bấm, AQ Autotest
Agent trên máy test nhận từ thư mục Tải về; chạy xong dùng **Nhập kết quả…**.
