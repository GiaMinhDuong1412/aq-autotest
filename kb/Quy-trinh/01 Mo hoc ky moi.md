---
loai: quy-trinh
ten: "Mở học kỳ mới"
thu_tu: 1
phan_he:
  - "[[QLHT]]"
du_lieu:
  - "[[Hoc ky]]"
truoc: []
sau:
  - "[[03 CTDT - TKB]]"
  - "[[04 Dang ky mon hoc]]"
  - "[[05 Hoc phi - thu - thanh toan]]"
nguon: luu-do + hdsd
trang_thai: tu-tai-lieu
tags: [quy-trinh]
aliases:
  - "Mở học kỳ mới"
---
# Mở học kỳ mới

*→ [[03 CTDT - TKB]], [[04 Dang ky mon hoc]], [[05 Hoc phi - thu - thanh toan]]*

Mọi phân hệ làm việc **theo học kỳ**. Học kỳ mới chưa mở / chưa khởi tạo dữ liệu thì phân hệ phía sau "không có dữ liệu" – case trông như lỗi nhưng gốc ở đây.

| # | Bước | Phân hệ | Menu | Kết quả |
|---|---|---|---|---|
| 1 | Tạo năm học – học kỳ (ngày bắt đầu, tuần bắt đầu, số tuần) | [[QLHT]] | `Hệ thống/ Thông tin học kỳ/ Danh mục năm học học kỳ` | [[Hoc ky]] |
| 2 | **Khởi tạo dữ liệu học kỳ** – mang dữ liệu học kỳ trước sang | [[QLHT]] | `Hệ thống/ Thông tin học kỳ/ Khởi tạo dữ liệu học kỳ` | dữ liệu học kỳ mới |
| 3 | Bổ sung dữ liệu học kỳ (phần chưa mang sang) | [[QLHT]] | `Hệ thống/ Thông tin học kỳ/ Bổ sung dữ liệu học kỳ` | |
| 4 | Chỉnh định thông số học kỳ của từng phân hệ (biến theo học kỳ) | mỗi phân hệ | `<Phân hệ>/ Quản trị phân hệ/ Chỉnh định thông số học kỳ` | |
| 5 | Học kỳ hiện hành trên web, học kỳ thu học phí | [[QLHT]] → web | `Hệ thống/ Quản trị NetWEB/ Chỉnh định chung` | [[Cau hinh NetWEB]] |

> [!warning] Hay gây case
> - Quên khởi tạo / bổ sung dữ liệu học kỳ → lớp, nhóm học, SV học kỳ trống ở học kỳ mới.
> - **Biến theo học kỳ** (ĐKMH, học phí, web) phải đặt lại cho học kỳ mới – "tuần trước chạy, học kỳ này không chạy" thường do biến chưa đặt ([[Thiet lap khong hieu luc]]).
> - Học kỳ trong Chỉnh định chung (web) lệch học kỳ đang dùng → web hiện sai học kỳ / ẩn nút.

**Sửa ở đây → kiểm lại:** tất cả quy trình phía sau trong học kỳ đó. Tài liệu: [[HDSD QLHT]] (`QLHT_ThongTinHocKy`).

---
Đọc cùng: [[00 Quy trình xuyên phân hệ]] · [[00 Cách phân tích case]]
