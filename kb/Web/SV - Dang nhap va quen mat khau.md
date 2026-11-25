---
loai: trang-web
ten: "Đăng nhập & quên mật khẩu"
vai_tro:
  - "sv"
  - "gv"
menu_web: "Đăng nhập · Quên mật khẩu"
du_lieu:
  - "[[Tai khoan va phan quyen]]"
  - "[[Danh muc sinh vien]]"
  - "[[Vien chuc]]"
ghi:
  - "[[Tai khoan va phan quyen]]"
phan_he:
  - "[[NETWEB-UI]]"
  - "[[QLHT]]"
chinh_dinh:
  - "Trang quản trị /admin → Quản lý đăng nhập web: Yêu cầu đăng nhập khi vào Web, Captcha, **Cấm sinh viên ngoài thời gian đăng ký được đăng nhập**, Số phút logout nếu không tương tác, Bắt buộc SV đổi mật khẩu mặc định (nếu mật khẩu là ngày sinh)"
  - "GH_MAILSERVER (Hệ thống / Quản trị hệ thống / Chỉnh định thông số hệ thống) – máy chủ mail gửi mã xác nhận quên mật khẩu"
tu_khoa: "đăng nhập|quên mật khẩu|lấy lại mật khẩu|mã xác nhận|đổi mật khẩu|captcha|tự (động )?logout"
tai_lieu: "[[HDSD NETWEB]]"
file_tai_lieu: "NETWEB_SinhVienQuenMatKhau"
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Đăng nhập & quên mật khẩu"
tags: [trang-web]
---
# Đăng nhập & quên mật khẩu

**Vai trò:** Sinh viên, Giảng viên · **Menu trên web:** Đăng nhập · Quên mật khẩu · Tài liệu: [[HDSD NETWEB]] (`NETWEB_SinhVienQuenMatKhau`)

## Trên web
SV / GV đăng nhập bằng mã + mật khẩu. Quên mật khẩu: nhập mã tài khoản + email đã khai trong hệ thống → nhận mã xác nhận qua email → đặt mật khẩu mới.

## Lấy dữ liệu từ Edusoft
- [[Tai khoan va phan quyen]]
- [[Danh muc sinh vien]]
- [[Vien chuc]]
- Trang quản trị Netweb: Quản lý người dùng / Đồng bộ tài khoản User (lấy SV, GV từ Edusoft; mật khẩu Tạo tự động hoặc Ngày sinh) · Đặt lại mật khẩu User (theo file / theo mã)

## Ghi ngược về Edusoft
- [[Tai khoan va phan quyen]]

## Chỉnh định quyết định trang này
- Trang quản trị `/admin` → Quản lý đăng nhập web: Yêu cầu đăng nhập khi vào Web, Captcha, **Cấm sinh viên ngoài thời gian đăng ký được đăng nhập**, Số phút logout nếu không tương tác, Bắt buộc SV đổi mật khẩu mặc định (nếu mật khẩu là ngày sinh)
- `GH_MAILSERVER` (`Hệ thống / Quản trị hệ thống / Chỉnh định thông số hệ thống`) – máy chủ mail gửi mã xác nhận quên mật khẩu

## Kiểm tra liên kết khi test
- Tài khoản phải được **Đồng bộ** từ Edusoft trước (SV mới nhập học chưa đồng bộ thì không đăng nhập được).
- Quên mật khẩu dùng **email của SV khai trên Edusoft** (lý lịch) – email sai / trống thì không nhận được mã.
- Thiết lập "cấm SV ngoài thời gian đăng ký đăng nhập" bật trong đợt ĐKMH → SV ngoài đợt bị chặn ngay ở màn hình đăng nhập (dễ nhầm là lỗi đăng nhập).
- Đổi chỉnh định / dữ liệu trên Edusoft xong: người dùng web **đăng xuất rồi đăng nhập lại** (Netweb giữ cache); nếu trường chưa khai `url_netweb` / BaseUrl ở `Hệ thống / Quản trị NetWEB / Chỉnh định chung` thì phải **Clear cache** ở trang quản trị (`/admin` → Quản lý App → Clear data App).
