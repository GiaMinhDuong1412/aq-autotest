---
loai: phan-he
ma: EDUBILL
ten: Thanh toán học phí kết nối Bill
san_pham: "[[Netweb]]"
test_tren:
  - web
  - api
tab_edusoft: —
nhan_tu:
  - "[[CSHP]]"
dua_sang: []
dau_hieu: thanh toán, ngân hàng, hóa đơn, bill, đóng học phí trực tuyến
nguon: tai-lieu
trang_thai: tu-tai-lieu
aliases:
  - "Thanh toán học phí kết nối Bill"
  - "EduBILL"
quy_trinh:
  - "[[05 Hoc phi - thu - thanh toan]]"
  - "[[11 Ky tuc xa]]"
tags: [phan-he]
---
# EDUBILL – Thanh toán học phí kết nối Bill

## Là gì
Quy trình đóng học phí kết nối Bill (tài liệu MoTaQuyTrinhDongHocPhi_KetNoiBill, QUY TRÌNH KHỞI TẠO MÔI TRƯỜNG TEST EDUBILL).

## Nhận dữ liệu từ
- [[Hoc phi|Học phí phải thu (đã tính)]] từ [[CSHP]] – đóng học phí trực tuyến

## Tạo ra
—

## Đưa sang
—

## Sửa ở đây → kiểm lại
Không có phân hệ nào nhận dữ liệu trực tiếp.
Lỗi có thể do dữ liệu đầu vào từ: [[CSHP]] – kiểm dữ liệu đó trước khi kết luận.

## Phần trên Edusoft
Công nợ / phiếu thu ở [[QLTV]].

## Phần trên web / app
Có **môi trường test EduBILL riêng** (theo tài liệu khởi tạo môi trường test) – không thanh toán thật.


## Dạng case thường gặp
[[Tich hop thanh toan]]
Đọc case theo [[00 Cách phân tích case]]: trường → phân hệ → yêu cầu KH → BA → Dev → đối chiếu → dạng case → dữ liệu → case liên quan.

## Test ở đâu
Tuỳ yêu cầu: web / api – xem KH nói về màn hình Edusoft hay trang web.

## Chuỗi phân hệ (bắc cầu)
**Muốn làm được EDUBILL phải có trước** (theo tầng dữ liệu – trên xuống dưới):
1. [[KHGD]] – [[Danh muc dao tao|Bậc – hệ – ngành đào tạo]], [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]], [[Mon hoc|Môn học]], [[Phong hoc|Phòng học kỳ]], [[CTDT|Chương trình đào tạo (chuẩn → kế hoạch → thực hiện)]], [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]], [[Thoi khoa bieu|Thời khóa biểu]]
2. [[QLHT]] – [[Hoc ky|Năm học – học kỳ]]
3. [[QLNS]] – [[Vien chuc|Viên chức / cán bộ giảng dạy]]
4. [[QLTS]] – [[Ky tuyen sinh|Kỳ / đợt tuyển sinh (ngành, khối, phương thức)]], [[Ho so thi sinh|Hồ sơ thí sinh]], [[DS trung tuyen|Danh sách trúng tuyển]]
5. [[QLSV]] – [[Lop sinh vien|Lớp sinh viên]], [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]], [[DS SV hoc ky|Danh sách sinh viên học kỳ]], [[Dien chinh sach|Diện chính sách / miễn giảm]]
6. [[DKMH]] – [[Rang buoc DKMH|Ràng buộc & thời gian đăng ký]], [[KQ DKMH|Kết quả đăng ký môn học]]
7. [[CSHP]] – [[Hoc phi|Học phí phải thu (đã tính)]]
8. **EDUBILL** – dùng dữ liệu trên

## Nằm trong quy trình
- [[05 Hoc phi - thu - thanh toan|Học phí: tính → nợ → thu → thanh toán online]]
- [[11 Ky tuc xa|Ký túc xá]]

## Tài liệu
- [[HDSD EDUBILL]]
- Case thực tế theo trường: [[00 Mô hình trường]]

## Lưu ý
—

---
Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.
