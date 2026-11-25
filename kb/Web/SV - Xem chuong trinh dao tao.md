---
loai: trang-web
ten: "Xem chương trình đào tạo, môn tiên quyết"
vai_tro:
  - "sv"
menu_web: "Xem chương trình đào tạo · Xem môn học tiên quyết"
du_lieu:
  - "[[CTDT]]"
  - "[[Mon hoc]]"
  - "[[Diem mon hoc]]"
ghi: []
phan_he:
  - "[[KHGD]]"
chinh_dinh: []
tu_khoa: "chương trình đào tạo|ctđt|ctdt|tiên quyết|học trước|song hành"
tai_lieu: "[[HDSD NETWEB]]"
file_tai_lieu: "NetWEB_SinhVienXemThongTinCaNhan"
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Xem chương trình đào tạo, môn tiên quyết"
tags: [trang-web]
---
# Xem chương trình đào tạo, môn tiên quyết

**Vai trò:** Sinh viên · **Menu trên web:** Xem chương trình đào tạo · Xem môn học tiên quyết · Tài liệu: [[HDSD NETWEB]] (`NetWEB_SinhVienXemThongTinCaNhan`)

## Trên web
SV xem học phần theo CTĐT của mình (số tín chỉ, tiết LT/TH, môn đã hoàn thành) và các môn tiên quyết / học trước / song hành.

## Lấy dữ liệu từ Edusoft
- [[CTDT]]
- [[Mon hoc]]
- [[Diem mon hoc]]
- CTĐT của khối lớp SV (chuẩn → kế hoạch → thực hiện) ở [[KHGD]]; quan hệ tiên quyết / học trước / song hành của môn học

## Ghi ngược về Edusoft
—

## Chỉnh định quyết định trang này
— (chỉ phụ thuộc dữ liệu)

## Kiểm tra liên kết khi test
- Sửa CTĐT / môn tiên quyết trên Edusoft → SV thuộc khối lớp đó thấy thay đổi trên web.
- "Đã hoàn thành" dựa vào điểm – sửa điểm cũng làm đổi trang này.
- Đổi chỉnh định / dữ liệu trên Edusoft xong: người dùng web **đăng xuất rồi đăng nhập lại** (Netweb giữ cache); nếu trường chưa khai `url_netweb` / BaseUrl ở `Hệ thống / Quản trị NetWEB / Chỉnh định chung` thì phải **Clear cache** ở trang quản trị (`/admin` → Quản lý App → Clear data App).
