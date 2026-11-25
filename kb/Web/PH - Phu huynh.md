---
loai: trang-web
ten: "Tài khoản phụ huynh"
vai_tro:
  - "ph"
menu_web: "Các menu xem thông tin SV được phân quyền cho phụ huynh"
du_lieu:
  - "[[Danh muc sinh vien]]"
  - "[[Diem mon hoc]]"
  - "[[Hoc phi]]"
  - "[[Thoi khoa bieu]]"
ghi: []
phan_he:
  - "[[NETWEB-UI]]"
  - "[[QLSV]]"
chinh_dinh:
  - "Trang quản trị /admin → Quản lý người dùng / Đồng bộ tài khoản User, chọn nhiệm ý **PHỤ HUYNH** (admin hoặc admin đơn vị phân cấp)"
tu_khoa: "phụ huynh"
tai_lieu: "[[HDSD NETWEB]]"
file_tai_lieu: "NetWEB_PhuHuynh"
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Tài khoản phụ huynh"
tags: [trang-web]
---
# Tài khoản phụ huynh

**Vai trò:** Phụ huynh · **Menu trên web:** Các menu xem thông tin SV được phân quyền cho phụ huynh · Tài liệu: [[HDSD NETWEB]] (`NetWEB_PhuHuynh`)

## Trên web
Phụ huynh đăng nhập xem thông tin SV như tài khoản SV (một số menu). Tên đăng nhập theo mã SV (mặc định) hoặc số CCCD; mật khẩu khởi tạo theo họ tên cha / mẹ không dấu, viết thường, liền.

## Lấy dữ liệu từ Edusoft
- [[Danh muc sinh vien]]
- [[Diem mon hoc]]
- [[Hoc phi]]
- [[Thoi khoa bieu]]
- Thông tin cha / mẹ trong lý lịch SV ([[QLSV]]) – quy tắc tên đăng nhập / mật khẩu lấy từ đây

## Ghi ngược về Edusoft
—

## Chỉnh định quyết định trang này
- Trang quản trị `/admin` → Quản lý người dùng / Đồng bộ tài khoản User, chọn nhiệm ý **PHỤ HUYNH** (admin hoặc admin đơn vị phân cấp)

## Kiểm tra liên kết khi test
- Phụ huynh không đăng nhập được → kiểm thông tin cha / mẹ của SV trên Edusoft rồi đồng bộ lại.
- Không ghi mật khẩu thật của tài khoản test vào KB / kịch bản.
- Đổi chỉnh định / dữ liệu trên Edusoft xong: người dùng web **đăng xuất rồi đăng nhập lại** (Netweb giữ cache); nếu trường chưa khai `url_netweb` / BaseUrl ở `Hệ thống / Quản trị NetWEB / Chỉnh định chung` thì phải **Clear cache** ở trang quản trị (`/admin` → Quản lý App → Clear data App).
