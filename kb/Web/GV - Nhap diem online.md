---
loai: trang-web
ten: "Nhập điểm online (theo nhóm học, theo tổ thi)"
vai_tro:
  - "gv"
menu_web: "Nhập điểm theo nhóm học · Nhập điểm theo tổ thi"
du_lieu:
  - "[[Hoc ky]]"
  - "[[Vien chuc]]"
  - "[[Nhom hoc]]"
  - "[[Danh sach thi]]"
  - "[[KQ DKMH]]"
ghi:
  - "[[Diem mon hoc]]"
phan_he:
  - "[[DIEM]]"
  - "[[LTHI]]"
chinh_dinh:
  - "Hệ thống / Quản trị NetWEB / Chỉnh định chung: hk_cho_phep_nhap_diem (cột Giá trị setting EduWEB; nhiều NHHK cách nhau dấu phẩy)"
  - "Quản lý nhập điểm / Quản lý nhập điểm / Nhập điểm online / Phân công cán bộ nhập điểm nhóm học (mặc định GV dạy; nút … để ủy quyền) · Gán thời gian nhập điểm nhóm học"
  - "Quản lý nhập điểm / Quản lý nhập điểm / Nhập điểm online / Phân công cán bộ nhập điểm thi · Gán thời gian nhập điểm thi"
  - "'Nhập ngày chung': Trường hợp chung / Từ ngày đến ngày (cần Ngày thi) / Thủ công; 'Có gán lại những mẫu tin đã nhập'"
  - "Quản lý nhập điểm / Quản lý nhập điểm / Khóa dữ liệu điểm / Khóa theo nhóm học · Mở khóa theo nhóm học"
  - "Tổ chức thi / Quản lý nhóm thi / Tạo nhóm thi / Nhóm môn học không tổ chức thi (cột Không thi) – môn không thi mới nhập được"
tu_khoa: "nhập điểm|điểm online|khóa điểm|khoá điểm|mở khóa|thời gian nhập điểm|tổ thi|phân công.*nhập điểm"
tai_lieu: "[[HDSD NETWEB]]"
file_tai_lieu: "NetWEB_GiangVienNhapDiemOnline"
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Nhập điểm online (theo nhóm học, theo tổ thi)"
tags: [trang-web]
---
# Nhập điểm online (theo nhóm học, theo tổ thi)

**Vai trò:** Giảng viên · **Menu trên web:** Nhập điểm theo nhóm học · Nhập điểm theo tổ thi · Tài liệu: [[HDSD NETWEB]] (`NetWEB_GiangVienNhapDiemOnline`)

## Trên web
GV chọn học kỳ → môn: cột Nhập điểm hiện "Nhập" (còn thời gian) hoặc "Xem" (hết thời gian); tick cột điểm → Nhập → gõ điểm số / điểm đặc biệt → Lưu; hoặc Import danh sách.

## Lấy dữ liệu từ Edusoft
- [[Hoc ky]]
- [[Vien chuc]]
- [[Nhom hoc]]
- [[Danh sach thi]]
- [[KQ DKMH]]
- Điểm GV nhập vào thẳng CSDL điểm ([[DIEM]]) – xem ở Quản lý nhập điểm

## Ghi ngược về Edusoft
- [[Diem mon hoc]]

## Chỉnh định quyết định trang này
- `Hệ thống / Quản trị NetWEB / Chỉnh định chung`: `hk_cho_phep_nhap_diem` (cột Giá trị setting EduWEB; nhiều NHHK cách nhau dấu phẩy)
- `Quản lý nhập điểm / Quản lý nhập điểm` / Nhập điểm online / Phân công cán bộ nhập điểm nhóm học (mặc định GV dạy; nút … để ủy quyền) · Gán thời gian nhập điểm nhóm học
- `Quản lý nhập điểm / Quản lý nhập điểm` / Nhập điểm online / Phân công cán bộ nhập điểm thi · Gán thời gian nhập điểm thi
- "Nhập ngày chung": Trường hợp chung / Từ ngày đến ngày (cần Ngày thi) / Thủ công; "Có gán lại những mẫu tin đã nhập"
- `Quản lý nhập điểm / Quản lý nhập điểm` / Khóa dữ liệu điểm / Khóa theo nhóm học · Mở khóa theo nhóm học
- Tổ chức thi / Quản lý nhóm thi / Tạo nhóm thi / Nhóm môn học không tổ chức thi (cột Không thi) – môn không thi mới nhập được

## Kiểm tra liên kết khi test
- Ngoài thời gian / cột đã khóa → chỉ "Xem", không nhập được.
- Học kỳ không có trong `hk_cho_phep_nhap_diem` → GV không thấy để nhập.
- Lưu trên web → kiểm điểm trên Edusoft và "Xem điểm" của SV.
- Môn không tổ chức thi phải tick Không thi, nếu không GV không nhập được.
- Đổi chỉnh định / dữ liệu trên Edusoft xong: người dùng web **đăng xuất rồi đăng nhập lại** (Netweb giữ cache); nếu trường chưa khai `url_netweb` / BaseUrl ở `Hệ thống / Quản trị NetWEB / Chỉnh định chung` thì phải **Clear cache** ở trang quản trị (`/admin` → Quản lý App → Clear data App).
