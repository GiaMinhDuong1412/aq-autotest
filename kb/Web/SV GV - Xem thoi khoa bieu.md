---
loai: trang-web
ten: "Xem thời khóa biểu (tuần, học kỳ)"
vai_tro:
  - "sv"
  - "gv"
menu_web: "Xem thời khóa biểu tuần · Xem thời khóa biểu học kỳ (kèm TKB lớp SV, TKB lớp, TKB môn học)"
du_lieu:
  - "[[Thoi khoa bieu]]"
  - "[[Nhom hoc]]"
  - "[[KQ DKMH]]"
ghi: []
phan_he:
  - "[[KHGD]]"
  - "[[DKMH]]"
chinh_dinh: []
tu_khoa: "thời khóa biểu|thời khoá biểu|tkb|lịch học|lịch (giảng )?dạy"
tai_lieu: "[[HDSD NETWEB]]"
file_tai_lieu: "NetWEB_SinhVienXemThongTinCaNhan"
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Xem thời khóa biểu (tuần, học kỳ)"
tags: [trang-web]
---
# Xem thời khóa biểu (tuần, học kỳ)

**Vai trò:** Sinh viên, Giảng viên · **Menu trên web:** Xem thời khóa biểu tuần · Xem thời khóa biểu học kỳ (kèm TKB lớp SV, TKB lớp, TKB môn học) · Tài liệu: [[HDSD NETWEB]] (`NetWEB_SinhVienXemThongTinCaNhan`)

## Trên web
SV xem lịch học theo tuần / học kỳ, các học kỳ khác. GV xem lịch dạy; từ cụm TKB tuần GV mở DS sinh viên, Điểm danh, Upload bài giảng, Đăng ký nghỉ dạy.

## Lấy dữ liệu từ Edusoft
- [[Thoi khoa bieu]]
- [[Nhom hoc]]
- [[KQ DKMH]]
- Xếp TKB, nhóm tổ ở [[KHGD]]; SV thấy TKB theo kết quả ĐKMH ([[DKMH]]); nghỉ dạy / dạy bù đã duyệt ở Kế hoạch / Nghỉ dạy và dạy bù

## Ghi ngược về Edusoft
—

## Chỉnh định quyết định trang này
— (chỉ phụ thuộc dữ liệu)

## Kiểm tra liên kết khi test
- Đổi phòng / tiết / GV của nhóm học trên Edusoft → kiểm TKB của **cả SV đã đăng ký nhóm đó và GV**.
- Lịch nghỉ dạy được duyệt làm **ẩn** buổi đó; dạy bù được duyệt làm **hiện** buổi bù (xem [[GV - Dang ky nghi day va day bu]]).
- Đổi chỉnh định / dữ liệu trên Edusoft xong: người dùng web **đăng xuất rồi đăng nhập lại** (Netweb giữ cache); nếu trường chưa khai `url_netweb` / BaseUrl ở `Hệ thống / Quản trị NetWEB / Chỉnh định chung` thì phải **Clear cache** ở trang quản trị (`/admin` → Quản lý App → Clear data App).
