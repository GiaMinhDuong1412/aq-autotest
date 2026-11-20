---
loai: phan-he
ma: QLTV
ten: Thu / chi học phí
san_pham: "[[Edusoft]]"
test_tren:
  - edusoft
  - web
tab_edusoft: Thu/chi HP
nhan_tu:
  - "[[CSHP]]"
  - "[[QLTS]]"
dua_sang:
  - "[[CSHP]]"
dau_hieu: thu học phí, phiếu thu, import phiếu thu, thu vãng lai, bảng kê, in học phí
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Thu / chi học phí"
  - "Thu chi học phí"
  - "Thu/chi HP"
quy_trinh:
  - "[[02 Tuyen sinh - nhap hoc]]"
  - "[[05 Hoc phi - thu - thanh toan]]"
tags: [phan-he]
---
# QLTV – Thu / chi học phí

## Là gì
Thu học phí (1 SV, import phiếu thu, ngân hàng), DS phiếu thu, thu vãng lai, in chi tiết học phí, bảng kê thu/chi (lưu đồ CSHP bước 14–15).

## Nhận dữ liệu từ
- [[DS trung tuyen|Danh sách trúng tuyển]] từ [[QLTS]] – thí sinh đã đóng học phí nhập học → Thu/chi HP
- [[Hoc phi|Học phí phải thu (đã tính)]] từ [[CSHP]] – thu học phí
- [[No hoc phi|Nợ học phí]] từ [[CSHP]] – thu nợ

## Tạo ra
- [[Phieu thu|Phiếu thu học phí]]

## Đưa sang
- [[Phieu thu|Phiếu thu học phí]] → [[CSHP]]

## Sửa ở đây → kiểm lại
Các phân hệ nhận dữ liệu của QLTV: [[CSHP]].
Lỗi có thể do dữ liệu đầu vào từ: [[CSHP]], [[QLTS]] – kiểm dữ liệu đó trước khi kết luận.

## Phần trên Edusoft
`Thu/chi HP/ Hoạt động thu/chi/ …`, `Thu/chi HP/ Khai thác báo biểu/ …`.
Menu: [[Menu/QLTV|101 menu của QLTV]] – menu tạo dữ liệu: [[Menu/Import phiếu thu (V04)|Import phiếu thu]], [[Menu/Thu học phí 1 SV (V05)|Thu học phí 1 SV]].

## Phần trên web / app
NetWEB SV: xem học phí; đóng học phí trực tuyến ([[EDUBILL]], tuỳ trường).


## Dạng case thường gặp
[[Mau in bao cao]], [[So lieu tinh sai]], [[Tich hop thanh toan]]
Đọc case theo [[00 Cách phân tích case]]: trường → phân hệ → yêu cầu KH → BA → Dev → đối chiếu → dạng case → dữ liệu → case liên quan.

## Test ở đâu
Tuỳ yêu cầu: edusoft / web – xem KH nói về màn hình Edusoft hay trang web.

## Chuỗi phân hệ (bắc cầu)
**Muốn làm được QLTV phải có trước** (theo tầng dữ liệu – trên xuống dưới):
1. [[KHGD]] – [[Danh muc dao tao|Bậc – hệ – ngành đào tạo]], [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]], [[Mon hoc|Môn học]], [[Phong hoc|Phòng học kỳ]], [[CTDT|Chương trình đào tạo (chuẩn → kế hoạch → thực hiện)]], [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]], [[Thoi khoa bieu|Thời khóa biểu]]
2. [[QLHT]] – [[Hoc ky|Năm học – học kỳ]]
3. [[QLNS]] – [[Vien chuc|Viên chức / cán bộ giảng dạy]]
4. [[QLTS]] – [[Ky tuyen sinh|Kỳ / đợt tuyển sinh (ngành, khối, phương thức)]], [[Ho so thi sinh|Hồ sơ thí sinh]], [[DS trung tuyen|Danh sách trúng tuyển]]
5. [[QLSV]] – [[Lop sinh vien|Lớp sinh viên]], [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]], [[DS SV hoc ky|Danh sách sinh viên học kỳ]], [[Dien chinh sach|Diện chính sách / miễn giảm]]
6. [[DKMH]] – [[Rang buoc DKMH|Ràng buộc & thời gian đăng ký]], [[KQ DKMH|Kết quả đăng ký môn học]]
7. [[CSHP]] – [[Hoc phi|Học phí phải thu (đã tính)]]
8. **QLTV** – [[Phieu thu|Phiếu thu học phí]]

**Ràng buộc quay ngược** (dữ liệu sinh ra *sau* QLTV nhưng quay lại chặn / ảnh hưởng nó, thường từ kỳ trước): [[No hoc phi|Nợ học phí]] (CSHP)

**Sửa dữ liệu của QLTV → kiểm lại:** phân hệ dùng trực tiếp [[CSHP]]; dữ liệu sinh ra từ đó (theo thứ tự): [[No hoc phi|Nợ học phí]] (CSHP).

## Nằm trong quy trình
- [[02 Tuyen sinh - nhap hoc|Tuyển sinh → nhập học → có sinh viên]]
- [[05 Hoc phi - thu - thanh toan|Học phí: tính → nợ → thu → thanh toán online]]

## Tài liệu
- [[HDSD EDUBILL]]
- [[HDSD QLTV]]
- Case thực tế theo trường: [[00 Mô hình trường]]

## Lưu ý
Dữ liệu tiền – chỉ SV test, có luồng hủy phiếu.

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.
