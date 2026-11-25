---
loai: trang-web
ten: "Trang quản trị Netweb (/admin)"
vai_tro:
  - "admin"
menu_web: "https://<domain>/admin"
du_lieu:
  - "[[Cau hinh NetWEB]]"
  - "[[Tai khoan va phan quyen]]"
ghi:
  - "[[Cau hinh NetWEB]]"
  - "[[Tai khoan va phan quyen]]"
phan_he:
  - "[[NETWEB-UI]]"
  - "[[QLHT]]"
chinh_dinh:
  - "Hệ thống / Quản trị NetWEB / Chỉnh định menu – cột ẩn menu (mã chức năng tương ứng menu web)"
  - "Hệ thống / Quản trị NetWEB / Chỉnh định chung – url_netweb / BaseUrl (Edusoft tự gọi API clear cache), các biến NHHK của từng chức năng web"
  - "GH_MASTERPASSEDUWEB (Hệ thống / Quản trị hệ thống / Chỉnh định thông số hệ thống) – mật khẩu dùng chung để admin vào tài khoản user khác (chỉ nêu tên biến, **không ghi giá trị**)"
  - "GH_MAILSERVER (Hệ thống / Quản trị hệ thống / Chỉnh định thông số hệ thống) – mail tự động (góp ý, duyệt, phục hồi mật khẩu)"
tu_khoa: "trang quản trị|/admin|banner|header|footer|menu web|ẩn (hiện )?menu|clear cache|đồng bộ tài khoản|đặt lại mật khẩu"
tai_lieu: "[[HDSD NETWEB]]"
file_tai_lieu: "NETWEB-QuanTriChung"
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Trang quản trị Netweb (/admin)"
tags: [trang-web]
---
# Trang quản trị Netweb (/admin)

**Vai trò:** Quản trị · **Menu trên web:** https://<domain>/admin · Tài liệu: [[HDSD NETWEB]] (`NETWEB-QuanTriChung`)

## Trên web
Thiết lập chung (tên trường, logo, theme, ẩn / hiện khu vực trang chủ), Header (menu, bắt buộc đăng nhập mới thấy), Banner, bài viết, thư viện, đối tác, quảng cáo, footer, quy chế; Quản lý người dùng; Hỗ trợ người dùng; Quản lý App (Clear cache, file); Quản lý đăng nhập web.

## Lấy dữ liệu từ Edusoft
- [[Cau hinh NetWEB]]
- [[Tai khoan va phan quyen]]
- Đồng bộ tài khoản User lấy SV / GV / phụ huynh từ Edusoft; Danh sách đối tác (chỉ đối tác có trong danh sách mới gọi API dữ liệu Edusoft – [[NETWEB-API]])

## Ghi ngược về Edusoft
- [[Cau hinh NetWEB]]
- [[Tai khoan va phan quyen]]

## Chỉnh định quyết định trang này
- `Hệ thống / Quản trị NetWEB / Chỉnh định menu` – cột ẩn menu (mã chức năng tương ứng menu web)
- `Hệ thống / Quản trị NetWEB / Chỉnh định chung` – `url_netweb` / BaseUrl (Edusoft tự gọi API clear cache), các biến NHHK của từng chức năng web
- `GH_MASTERPASSEDUWEB` (`Hệ thống / Quản trị hệ thống / Chỉnh định thông số hệ thống`) – mật khẩu dùng chung để admin vào tài khoản user khác (chỉ nêu tên biến, **không ghi giá trị**)
- `GH_MAILSERVER` (`Hệ thống / Quản trị hệ thống / Chỉnh định thông số hệ thống`) – mail tự động (góp ý, duyệt, phục hồi mật khẩu)

## Kiểm tra liên kết khi test
- Ẩn menu ở Edusoft (Chỉnh định menu) → menu biến mất trên web (sau khi clear cache / đăng nhập lại).
- Netweb và Edusoft **chung 1 CSDL**: sửa trên Edusoft là dữ liệu web đổi ngay, chỉ có cache làm chậm hiển thị.
- Đổi chỉnh định / dữ liệu trên Edusoft xong: người dùng web **đăng xuất rồi đăng nhập lại** (Netweb giữ cache); nếu trường chưa khai `url_netweb` / BaseUrl ở `Hệ thống / Quản trị NetWEB / Chỉnh định chung` thì phải **Clear cache** ở trang quản trị (`/admin` → Quản lý App → Clear data App).
