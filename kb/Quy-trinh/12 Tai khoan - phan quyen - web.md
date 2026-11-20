---
loai: quy-trinh
ten: "Tài khoản, phân quyền, cấu hình web (dùng chung)"
thu_tu: 12
phan_he:
  - "[[QLHT]]"
  - "[[NETWEB-UI]]"
  - "[[NETWEB-API]]"
  - "[[EDUGO]]"
du_lieu:
  - "[[Tai khoan va phan quyen]]"
  - "[[Cau hinh NetWEB]]"
  - "[[Hoc ky]]"
truoc: []
sau: []
nguon: luu-do + hdsd
trang_thai: tu-tai-lieu
tags: [quy-trinh]
aliases:
  - "Tài khoản, phân quyền, cấu hình web (dùng chung)"
---
# Tài khoản, phân quyền, cấu hình web (dùng chung)



Cắt ngang mọi quy trình: **ai** được làm gì, **trên web hiện gì**.

| Việc | Nơi làm | Ảnh hưởng |
|---|---|---|
| Tạo tài khoản, phân quyền chức năng | [[QLHT]] `QLHT_TaoTaiKhoanVaPhanQuyenNguoiDung` | mọi menu Edusoft |
| Phân quyền dữ liệu theo khoa | [[QLHT]] | người dùng khoa chỉ thấy dữ liệu khoa mình |
| Phân quyền quản trị trên web | [[QLHT]] | trang quản trị NetWEB |
| **Chỉnh định chung NetWEB** (học kỳ web, học kỳ thu học phí, skyline_apikey, bật / tắt chức năng) | `Hệ thống/ Quản trị NetWEB/ Chỉnh định chung` | mọi trang web, EduBILL |
| Biến Edusoft.Web theo học kỳ (vd thời gian ĐKMH) | `Hệ thống/ Quản trị hệ thống/ Chỉnh định thông số hệ thống` (phân hệ Edusoft.Web) | cần **restart IIS** |
| Khoá sổ dữ liệu | [[QLHT]] `QLHT_KhoaSoDuLieu` | khoá rồi không sửa được |
| Truy vết dữ liệu | [[QLHT]] `QLHT_TruyVetDuLieu` | biết ai sửa gì – dùng khi đối chiếu case |

> [!warning] Hay gây case
> - "Không thấy menu / nút", "không lưu được" → quyền, khoá sổ trước khi nghi lỗi ([[Tai khoan phan quyen]], [[Luu cap nhat khong duoc]]).
> - "Đã chỉnh mà web không đổi" → biến Edusoft.Web cần restart IIS, học kỳ web lệch ([[Thiet lap khong hieu luc]]).

Tài liệu: [[HDSD QLHT]], [[HDSD NETWEB]] (`NETWEB_QuanTriChung`).

---
Đọc cùng: [[00 Quy trình xuyên phân hệ]] · [[00 Cách phân tích case]]
