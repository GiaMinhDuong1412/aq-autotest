---
loai: phan-he
ma: QLHT
ten: Quản lý hệ thống
san_pham: "[[Edusoft]]"
test_tren:
  - edusoft
  - web
tab_edusoft: Hệ thống
nhan_tu:
  - "[[CSHP]]"
dua_sang:
  - "[[CSHP]]"
  - "[[DIEM]]"
  - "[[DKMH]]"
  - "[[KHGD]]"
  - "[[KLGD]]"
  - "[[KSDG]]"
  - "[[LTHI]]"
  - "[[NETWEB-API]]"
  - "[[NETWEB-UI]]"
  - "[[QLSV]]"
dau_hieu: tài khoản, phân quyền, khóa sổ, học kỳ, biểu in, import, bảo mật, đăng nhập, chatbot, chỉnh định NetWEB
nguon: tai-lieu
trang_thai: tu-tai-lieu
---
# QLHT – Quản lý hệ thống

## Là gì
Tài khoản & phân quyền người dùng, thông tin học kỳ, khóa sổ dữ liệu, thao tác danh mục / biểu in / import, chỉnh định view, tiến trình tự động, truy vết dữ liệu; **quản trị NetWEB** (chỉnh định menu, chỉnh định chung, cấm SV xem vì nợ học phí).

## Nhận dữ liệu từ
- [[No hoc phi|Nợ học phí]] từ [[CSHP]] – Cấm SV xem vì nợ học phí (web)

## Tạo ra
- [[Hoc ky|Năm học – học kỳ]]
- [[Tai khoan va phan quyen|Tài khoản & phân quyền]]
- [[Cau hinh NetWEB|Cấu hình NetWEB]]

## Đưa sang
- [[Hoc ky|Năm học – học kỳ]] → [[QLSV]], [[KHGD]], [[DKMH]], [[CSHP]], [[LTHI]], [[DIEM]], [[KSDG]], [[KLGD]]
- [[Tai khoan va phan quyen|Tài khoản & phân quyền]] → [[NETWEB-UI]], [[NETWEB-API]]
- [[Cau hinh NetWEB|Cấu hình NetWEB]] → [[NETWEB-UI]]

## Sửa ở đây → kiểm lại
Các phân hệ nhận dữ liệu của QLHT: [[CSHP]], [[DIEM]], [[DKMH]], [[KHGD]], [[KLGD]], [[KSDG]], [[LTHI]], [[NETWEB-API]], [[NETWEB-UI]], [[QLSV]].
Lỗi có thể do dữ liệu đầu vào từ: [[CSHP]] – kiểm dữ liệu đó trước khi kết luận.

## Phần trên Edusoft
`Hệ thống/ Thông tin học kỳ/ …`, `Hệ thống/ Quản lý người dùng/ …`, `Hệ thống/ Quản trị hệ thống/ Chỉnh định thông số hệ thống`, `Hệ thống/ An toàn dữ liệu/ Khóa sổ phân hệ theo học kỳ`.
Menu: [[Menu/QLHT|75 menu của QLHT]] – menu tạo dữ liệu: [[Menu/Khóa sổ phân hệ theo học kỳ (H2.3)|Khóa sổ phân hệ theo học kỳ]], [[Menu/Phân quyền theo chức năng (H62)|Phân quyền theo chức năng]], [[Menu/Phân quyền theo người dùng (H67)|Phân quyền theo người dùng]], [[Menu/Chỉnh định chung (H101.3)|Chỉnh định chung]], [[Menu/Chỉnh định menu (H101.1)|Chỉnh định menu]], [[Menu/Cấm SV xem vì nợ học phí (H101.4)|Cấm SV xem vì nợ học phí]], [[Menu/Danh mục năm học học kỳ (H31)|Danh mục năm học học kỳ]], [[Menu/Khởi tạo dữ liệu học kỳ (H32)|Khởi tạo dữ liệu học kỳ]], [[Menu/Chỉnh định menu (HTI01)|Chỉnh định menu]].

## Phần trên web / app
`Hệ thống/ Quản trị NetWEB/ Chỉnh định menu | Chỉnh định chung | Cấm SV xem vì nợ học phí` – **chỉnh trên Edusoft, kiểm kết quả trên web** (menu/chức năng ẩn-hiện, SV nợ HP không xem được…). Phân quyền quản trị trên web (PhanQuyenQuanTriTrenWeb).

## Test ở đâu
Tuỳ yêu cầu: edusoft / web – xem KH nói về màn hình Edusoft hay trang web.

## Lưu ý
Thông tin học kỳ, khóa sổ và phân quyền ảnh hưởng **mọi phân hệ** – sửa ở đây phải kiểm lại phân hệ dùng học kỳ đó. Case bảo mật / đăng nhập thường là web + hệ thống – đọc kỹ KH nói trang nào. Không đổi phân quyền tài khoản thật.

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.
