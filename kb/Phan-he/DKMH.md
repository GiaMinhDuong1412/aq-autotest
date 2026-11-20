---
loai: phan-he
ma: DKMH
ten: Đăng ký môn học
san_pham: "[[Edusoft]]"
test_tren:
  - edusoft
  - web
tab_edusoft: Đăng ký MH
nhan_tu:
  - "[[CSHP]]"
  - "[[KHGD]]"
  - "[[QLHT]]"
  - "[[QLSV]]"
dua_sang:
  - "[[CSHP]]"
  - "[[DIEM]]"
  - "[[DKMHUI]]"
  - "[[LTHI]]"
  - "[[QLSV]]"
dau_hieu: môn tiên quyết, thời gian đăng ký, đăng ký online/offline, rút môn, hủy kết quả, nguyện vọng, CVHT duyệt
nguon: tai-lieu
trang_thai: tu-tai-lieu
---
# DKMH – Đăng ký môn học

## Là gì
Ràng buộc (tiên quyết / học trước / song hành, tín chỉ tối đa, cải thiện, nợ học phí) + thời gian đăng ký theo lớp → **offline** (phòng đào tạo đăng ký thay: tự động / theo file / từng SV) hoặc **online** (SV đăng ký trên web) → kết quả ĐKMH → hiệu chỉnh / hủy / phục hồi (lưu đồ DKMH).

## Nhận dữ liệu từ
- [[Hoc ky|Năm học – học kỳ]] từ [[QLHT]] – đăng ký theo học kỳ
- [[Mon hoc|Môn học]] từ [[KHGD]] – môn tiên quyết / học trước / song hành
- [[Lop sinh vien|Lớp sinh viên]] từ [[QLSV]] – thời gian / đối tượng đăng ký theo lớp
- [[CTDT|Chương trình đào tạo (chuẩn → kế hoạch → thực hiện)]] từ [[KHGD]] – môn được đăng ký theo chương trình
- [[DS SV hoc ky|Danh sách sinh viên học kỳ]] từ [[QLSV]] – SV được đăng ký môn học (phải có trong DS SV học kỳ)
- [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]] từ [[KHGD]] – nhóm học + số chỗ để đăng ký
- [[Thoi khoa bieu|Thời khóa biểu]] từ [[KHGD]] – nhóm học có lịch để SV chọn
- [[No hoc phi|Nợ học phí]] từ [[CSHP]] – ràng buộc: SV nợ HP không được đăng ký

## Tạo ra
- [[Rang buoc DKMH|Ràng buộc & thời gian đăng ký]]
- [[KQ DKMH|Kết quả đăng ký môn học]]

## Đưa sang
- [[Rang buoc DKMH|Ràng buộc & thời gian đăng ký]] → [[DKMHUI]]
- [[KQ DKMH|Kết quả đăng ký môn học]] → [[CSHP]], [[LTHI]], [[DIEM]], [[QLSV]]

## Sửa ở đây → kiểm lại
Các phân hệ nhận dữ liệu của DKMH: [[CSHP]], [[DIEM]], [[DKMHUI]], [[LTHI]], [[QLSV]].
Lỗi có thể do dữ liệu đầu vào từ: [[CSHP]], [[KHGD]], [[QLHT]], [[QLSV]] – kiểm dữ liệu đó trước khi kết luận.

## Phần trên Edusoft
Khai báo & đăng ký offline: `Đăng ký MH/ Đăng ký môn học/ …`, `Đăng ký MH/ Ràng buộc đăng ký online/ …`, `Đăng ký MH/ Rút môn học online/ Thời gian rút môn học theo lớp`, `Đăng ký MH/ Hủy KQ ĐKMH/ …`.
Menu: [[Menu/DKMH|131 menu của DKMH]] – menu tạo dữ liệu: [[Menu/Chỉnh định chung (M10.50)|Chỉnh định chung]], [[Menu/Thời gian đăng ký theo lớp (M10.21)|Thời gian đăng ký theo lớp]], [[Menu/ĐKMH từng sinh viên (M13)|ĐKMH từng sinh viên]], [[Menu/Theo lớp (M11.01)|Theo lớp]].

## Phần trên web / app
NetWEB SV: đăng ký môn học, rút môn học; NetWEB GV (CVHT): duyệt đăng ký môn học. Nhiều trường dùng **trang ĐKMH riêng** (vd dkmh.hitu.edu.vn, dkmh.tdmu.edu.vn) – xem [[DKMHUI]].


## Dạng case thường gặp
[[Hieu nang]], [[Loi EX Edusoft]], [[Thiet lap khong hieu luc]], [[Xu ly du lieu]]
Đọc case theo [[00 Cách phân tích case]]: trường → phân hệ → yêu cầu KH → BA → Dev → đối chiếu → dạng case → dữ liệu → case liên quan.

## Test ở đâu
Tuỳ yêu cầu: edusoft / web – xem KH nói về màn hình Edusoft hay trang web.

## Lưu ý
Sửa về **cài đặt** (thời gian, ràng buộc) → kiểm cả nơi cài (Edusoft) và nơi SV thấy (web). Đợt ĐKMH có tải rất lớn (sheet NetWeb_DKMH: hàng nghìn SV cùng lúc) – sửa hiệu năng cần test riêng.

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.
