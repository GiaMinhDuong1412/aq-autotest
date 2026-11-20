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
aliases:
  - "Quản lý hệ thống"
  - "Hệ thống"
quy_trinh:
  - "[[01 Mo hoc ky moi]]"
  - "[[04 Dang ky mon hoc]]"
  - "[[05 Hoc phi - thu - thanh toan]]"
  - "[[12 Tai khoan - phan quyen - web]]"
tags: [phan-he]
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


## Dạng case thường gặp
[[Tai khoan phan quyen]], [[Thiet lap khong hieu luc]]
Đọc case theo [[00 Cách phân tích case]]: trường → phân hệ → yêu cầu KH → BA → Dev → đối chiếu → dạng case → dữ liệu → case liên quan.

## Test ở đâu
Tuỳ yêu cầu: edusoft / web – xem KH nói về màn hình Edusoft hay trang web.

## Chuỗi phân hệ (bắc cầu)

**Ràng buộc quay ngược** (dữ liệu sinh ra *sau* QLHT nhưng quay lại chặn / ảnh hưởng nó, thường từ kỳ trước): [[No hoc phi|Nợ học phí]] (CSHP)

**Sửa dữ liệu của QLHT → kiểm lại:** phân hệ dùng trực tiếp [[CSHP]], [[DIEM]], [[DKMH]], [[KHGD]], [[KLGD]], [[KSDG]], [[LTHI]], [[NETWEB-API]], [[NETWEB-UI]], [[QLSV]]; dữ liệu sinh ra từ đó (theo thứ tự): [[Phong hoc|Phòng học kỳ]] (KHGD), [[Vien chuc|Viên chức / cán bộ giảng dạy]] (QLNS), [[Rang buoc DKMH|Ràng buộc & thời gian đăng ký]] (DKMH), [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]] (QLSV), [[DS SV hoc ky|Danh sách sinh viên học kỳ]] (QLSV), [[Danh muc sinh vien|Danh mục sinh viên (mọi SV của trường)]] (QLSV), [[Diem luan van|Điểm luận văn]] (BVLV), [[Diem ren luyen|Điểm rèn luyện]] (QLSV), [[Dien chinh sach|Diện chính sách / miễn giảm]] (QLSV), [[Hop dong KTX|Hợp đồng ký túc xá]] (QKTX), [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]] (KHGD), [[Ket qua khao sat|Kết quả khảo sát]] (KSDG), [[Thoi khoa bieu|Thời khóa biểu]] (KHGD), [[KQ DKMH|Kết quả đăng ký môn học]] (DKMH), [[Khoi luong giang day|Khối lượng giảng dạy]] (KLGD), [[Danh sach thi|Danh sách thi – lịch thi]] (LTHI), [[Diem danh|Điểm danh (chuyên cần)]] (NETWEB-UI), [[Hoc phi|Học phí phải thu (đã tính)]] (CSHP), [[Diem mon hoc|Điểm môn học]] (DIEM), [[Phieu thu|Phiếu thu học phí]] (QLTV), [[Diem trung binh|Điểm trung bình – tích lũy]] (DIEM), [[No hoc phi|Nợ học phí]] (CSHP), [[Ket qua hoc vu|Kết quả xét học vụ]] (QXHV), [[Ket qua tot nghiep|Kết quả xét tốt nghiệp]] (QLTN).

## Nằm trong quy trình
- [[01 Mo hoc ky moi|Mở học kỳ mới]]
- [[04 Dang ky mon hoc|Đăng ký môn học]]
- [[05 Hoc phi - thu - thanh toan|Học phí: tính → nợ → thu → thanh toán online]]
- [[12 Tai khoan - phan quyen - web|Tài khoản, phân quyền, cấu hình web (dùng chung)]]

## Tài liệu
- [[HDSD QLHT]]
- Case thực tế theo trường: [[00 Mô hình trường]]

## Lưu ý
Thông tin học kỳ, khóa sổ và phân quyền ảnh hưởng **mọi phân hệ** – sửa ở đây phải kiểm lại phân hệ dùng học kỳ đó. Case bảo mật / đăng nhập thường là web + hệ thống – đọc kỹ KH nói trang nào. Không đổi phân quyền tài khoản thật.

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.
