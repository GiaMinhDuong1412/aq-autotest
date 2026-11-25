---
loai: trang-web
ten: "Đăng ký nghỉ dạy, dạy bù"
vai_tro:
  - "gv"
  - "sv"
menu_web: "Thời khóa biểu dạng tuần → Đăng ký nghỉ dạy · Lịch đăng ký nghỉ dạy → Đăng ký (dạy bù)"
du_lieu:
  - "[[Thoi khoa bieu]]"
  - "[[Phong hoc]]"
ghi:
  - "[[Thoi khoa bieu]]"
phan_he:
  - "[[KHGD]]"
chinh_dinh: []
tu_khoa: "nghỉ dạy|dạy bù|lịch bù|đăng ký nghỉ"
tai_lieu: "[[HDSD NETWEB]]"
file_tai_lieu: "NETWEB_HuongDanDangKyNghiDay_DayBuOnline"
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Đăng ký nghỉ dạy, dạy bù"
tags: [trang-web]
---
# Đăng ký nghỉ dạy, dạy bù

**Vai trò:** Giảng viên, Sinh viên · **Menu trên web:** Thời khóa biểu dạng tuần → Đăng ký nghỉ dạy · Lịch đăng ký nghỉ dạy → Đăng ký (dạy bù) · Tài liệu: [[HDSD NETWEB]] (`NETWEB_HuongDanDangKyNghiDay_DayBuOnline`)

## Trên web
GV đăng ký nghỉ ở cụm TKB tuần (minh chứng, lý do không bắt buộc) → user Edusoft duyệt → GV đăng ký dạy bù (ngày, tiết, phòng theo sĩ số / tính chất phòng) → user Edusoft duyệt.

## Lấy dữ liệu từ Edusoft
- [[Thoi khoa bieu]]
- [[Phong hoc]]
- Kế hoạch / Nghỉ dạy và dạy bù / Lịch nghỉ dạy và dạy bù – Sửa → Trạng thái đơn = Duyệt / Không duyệt; nút "Duyệt lịch dạy bù"

## Ghi ngược về Edusoft
- [[Thoi khoa bieu]]

## Chỉnh định quyết định trang này
— (chỉ phụ thuộc dữ liệu)

## Kiểm tra liên kết khi test
- Duyệt nghỉ → buổi đó **ẩn** trên TKB GV và SV; Không duyệt → không ẩn, GV xóa được đơn.
- Chỉ xóa được lịch nghỉ ở trạng thái Chưa duyệt / Không duyệt.
- Dạy bù trùng TKB phòng / lớp phải bị chặn; dạy bù được duyệt mới hiện trên TKB, Không duyệt = xóa lịch bù để đăng ký lại.
- Đổi chỉnh định / dữ liệu trên Edusoft xong: người dùng web **đăng xuất rồi đăng nhập lại** (Netweb giữ cache); nếu trường chưa khai `url_netweb` / BaseUrl ở `Hệ thống / Quản trị NetWEB / Chỉnh định chung` thì phải **Clear cache** ở trang quản trị (`/admin` → Quản lý App → Clear data App).
