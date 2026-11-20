---
loai: phan-he
ma: QLTS
ten: Tuyển sinh
san_pham: "[[Edusoft]]"
test_tren:
  - edusoft
  - web
tab_edusoft: Tuyển sinh
nhan_tu:
  - "[[QLSV]]"
dua_sang:
  - "[[QLSV]]"
  - "[[QLTV]]"
dau_hieu: kỳ/đợt tuyển sinh, hồ sơ thí sinh, xét tuyển, điểm chuẩn, trúng tuyển, nhập học online, tiếp sinh
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Tuyển sinh"
  - "Tuyển sinh"
quy_trinh:
  - "[[02 Tuyen sinh - nhap hoc]]"
tags: [phan-he]
---
# QLTS – Tuyển sinh

## Là gì
Chuẩn bị kỳ/đợt, danh mục ngành – phương thức – khối; nhập hồ sơ; điểm chuẩn; xét trúng tuyển; gán lớp / mã SV; xác nhận nhập học; tiếp sinh (hồ sơ + học phí nhập học) → chuyển sang QLSV (lưu đồ QLTS).

## Nhận dữ liệu từ
- [[Lop sinh vien|Lớp sinh viên]] từ [[QLSV]] – gán tên lớp cho thí sinh trúng tuyển

## Tạo ra
- [[Ho so thi sinh|Hồ sơ thí sinh]]
- [[DS trung tuyen|Danh sách trúng tuyển]]
- [[Ky tuyen sinh|Kỳ / đợt tuyển sinh (ngành, khối, phương thức)]]

## Đưa sang
- [[DS trung tuyen|Danh sách trúng tuyển]] → [[QLSV]], [[QLTV]]

## Sửa ở đây → kiểm lại
Các phân hệ nhận dữ liệu của QLTS: [[QLSV]], [[QLTV]].
Lỗi có thể do dữ liệu đầu vào từ: [[QLSV]] – kiểm dữ liệu đó trước khi kết luận.

## Phần trên Edusoft
`Tuyển sinh/ Chuẩn bị/ …`, `Tuyển sinh/ Nhập liệu hồ sơ/ …`, `Tuyển sinh/ Xét tuyển/ …`, `Tuyển sinh/ Tiếp sinh/ …`.
Menu: [[Menu/QLTS|234 menu của QLTS]] – menu tạo dữ liệu: [[Menu/Danh sách khối tuyển sinh (T1.02)|Danh sách khối tuyển sinh]], [[Menu/Danh sách kỳ tuyển sinh (T1.01)|Danh sách kỳ tuyển sinh]], [[Menu/Danh sách ngành tuyển sinh (T1.03)|Danh sách ngành tuyển sinh]], [[Menu/Danh sách đợt tuyển sinh (T1.09)|Danh sách đợt tuyển sinh]], [[Menu/Định nghĩa phương thức hồ sơ XT (T1.12)|Định nghĩa phương thức hồ sơ XT]], [[Menu/Danh sách trúng tuyển (T9.00)|Danh sách trúng tuyển]], [[Menu/Nhập hồ sơ đăng ký thi tuyển (T2.03.01)|Nhập hồ sơ đăng ký thi tuyển]], [[Menu/Nhập hồ sơ đăng ký xét tuyển (T2.03.00A)|Nhập hồ sơ đăng ký xét tuyển]], [[Menu/Chuyển danh sách trúng tuyển sang phân hệ QLSV (T10.06)|Chuyển danh sách trúng tuyển sang phân hệ QLSV]].

## Phần trên web / app
NetWEB: Đăng ký xét tuyển, Tra cứu thông tin xét tuyển, Nhập học online (thí sinh), Chăm sóc thí sinh xét tuyển.


## Dạng case thường gặp
[[Loi EX Edusoft]], [[Luu cap nhat khong duoc]], [[Xu ly du lieu]]
Đọc case theo [[00 Cách phân tích case]]: trường → phân hệ → yêu cầu KH → BA → Dev → đối chiếu → dạng case → dữ liệu → case liên quan.

## Test ở đâu
Tuỳ yêu cầu: edusoft / web – xem KH nói về màn hình Edusoft hay trang web.

## Chuỗi phân hệ (bắc cầu)
**Muốn làm được QLTS phải có trước** (theo tầng dữ liệu – trên xuống dưới):
1. [[KHGD]] – [[Danh muc dao tao|Bậc – hệ – ngành đào tạo]], [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]]
2. [[QLSV]] – [[Lop sinh vien|Lớp sinh viên]]
3. **QLTS** – [[Ky tuyen sinh|Kỳ / đợt tuyển sinh (ngành, khối, phương thức)]], [[Ho so thi sinh|Hồ sơ thí sinh]], [[DS trung tuyen|Danh sách trúng tuyển]]

**Sửa dữ liệu của QLTS → kiểm lại:** phân hệ dùng trực tiếp [[QLSV]], [[QLTV]]; dữ liệu sinh ra từ đó (theo thứ tự): [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]] (QLSV), [[DS SV hoc ky|Danh sách sinh viên học kỳ]] (QLSV), [[Danh muc sinh vien|Danh mục sinh viên (mọi SV của trường)]] (QLSV), [[Diem luan van|Điểm luận văn]] (BVLV), [[Diem ren luyen|Điểm rèn luyện]] (QLSV), [[Dien chinh sach|Diện chính sách / miễn giảm]] (QLSV), [[Hop dong KTX|Hợp đồng ký túc xá]] (QKTX), [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]] (KHGD), [[Ket qua khao sat|Kết quả khảo sát]] (KSDG), [[Thoi khoa bieu|Thời khóa biểu]] (KHGD), [[KQ DKMH|Kết quả đăng ký môn học]] (DKMH), [[Khoi luong giang day|Khối lượng giảng dạy]] (KLGD), [[Danh sach thi|Danh sách thi – lịch thi]] (LTHI), [[Diem danh|Điểm danh (chuyên cần)]] (NETWEB-UI), [[Hoc phi|Học phí phải thu (đã tính)]] (CSHP), [[Diem mon hoc|Điểm môn học]] (DIEM), [[Phieu thu|Phiếu thu học phí]] (QLTV), [[Diem trung binh|Điểm trung bình – tích lũy]] (DIEM), [[No hoc phi|Nợ học phí]] (CSHP), [[Ket qua hoc vu|Kết quả xét học vụ]] (QXHV), [[Ket qua tot nghiep|Kết quả xét tốt nghiệp]] (QLTN).

## Nằm trong quy trình
- [[02 Tuyen sinh - nhap hoc|Tuyển sinh → nhập học → có sinh viên]]

## Tài liệu
- [[HDSD NhapHocOnline]]
- [[HDSD QLTS]]
- Case thực tế theo trường: [[00 Mô hình trường]]

## Lưu ý
Kết thúc tuyển sinh là bước **chuyển** sang QLSV và Thu/chi HP – kiểm dữ liệu đã sang đủ.

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.
