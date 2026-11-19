---
loai: du-lieu
ten: Nợ học phí
tang: 11
tao_o: "[[CSHP]]"
dung_o:
  - "[[DKMH]]"
  - "[[QLHT]]"
  - "[[QLTV]]"
can_co:
  - "[[Hoc phi]]"
  - "[[Phieu thu]]"
la_dieu_kien_cho: []
nguon: luu-do
trang_thai: tu-tai-lieu
---
# Nợ học phí

**Tạo ở** [[CSHP]] – `Chính sách HP/ Chính sách học phí/ Nợ học phí/ Danh sách SV tồn nợ HP · Cập nhật tồn nợ` · tầng 11 trong [[00 Logic nghiệp vụ]] (cần 20 loại dữ liệu có trước)

## Muốn có Nợ học phí thì phải có trước
- [[Hoc phi|Học phí phải thu (đã tính)]] – phải thu
- [[Phieu thu|Phiếu thu học phí]] – đã thu

## Chuẩn bị dữ liệu test (theo thứ tự)
1. [[Danh muc dao tao|Bậc – hệ – ngành đào tạo]] – tạo ở [[KHGD]]
2. [[Hoc ky|Năm học – học kỳ]] – tạo ở [[QLHT]] · menu [[Menu/Danh mục năm học học kỳ (H31)|Danh mục năm học học kỳ]]
3. [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]] – tạo ở [[KHGD]]
4. [[Ky tuyen sinh|Kỳ / đợt tuyển sinh (ngành, khối, phương thức)]] – tạo ở [[QLTS]] · menu [[Menu/Danh sách kỳ tuyển sinh (T1.01)|Danh sách kỳ tuyển sinh]]
5. [[Mon hoc|Môn học]] – tạo ở [[KHGD]] · menu [[Menu/Danh mục môn học (K4_DMMH)|Danh mục môn học]]
6. [[Phong hoc|Phòng học kỳ]] – tạo ở [[KHGD]] · menu [[Menu/Danh sách phòng học kỳ (K0.2)|Danh sách phòng học kỳ]]
7. [[Vien chuc|Viên chức / cán bộ giảng dạy]] – tạo ở [[QLNS]] · menu [[Menu/Danh sách viên chức học kỳ (N02)|Danh sách viên chức học kỳ]]
8. [[CTDT|Chương trình đào tạo (chuẩn → kế hoạch → thực hiện)]] – tạo ở [[KHGD]] · menu [[Menu/CTĐT chuẩn (K41.02)|CTĐT chuẩn]]
9. [[Ho so thi sinh|Hồ sơ thí sinh]] – tạo ở [[QLTS]] · menu [[Menu/Nhập hồ sơ đăng ký xét tuyển (T2.03.00A)|Nhập hồ sơ đăng ký xét tuyển]]
10. [[Lop sinh vien|Lớp sinh viên]] – tạo ở [[QLSV]] · menu [[Menu/Danh mục lớp (S13)|Danh mục lớp]]
11. [[DS trung tuyen|Danh sách trúng tuyển]] – tạo ở [[QLTS]] · menu [[Menu/Danh sách trúng tuyển (T9.00)|Danh sách trúng tuyển]]
12. [[Rang buoc DKMH|Ràng buộc & thời gian đăng ký]] – tạo ở [[DKMH]] · menu [[Menu/Thời gian đăng ký theo lớp (M10.21)|Thời gian đăng ký theo lớp]]
13. [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]] – tạo ở [[QLSV]] · menu [[Menu/Quyết định vào mới (S15.04)|Quyết định vào mới]]
14. [[DS SV hoc ky|Danh sách sinh viên học kỳ]] – tạo ở [[QLSV]] · menu [[Menu/Danh sách sinh viên học kỳ (S12)|Danh sách sinh viên học kỳ]]
15. [[Dien chinh sach|Diện chính sách / miễn giảm]] – tạo ở [[QLSV]] · menu [[Menu/Diện chính sách sinh viên học kỳ (S163)|Diện chính sách sinh viên học kỳ]]
16. [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]] – tạo ở [[KHGD]] · menu [[Menu/Danh sách nhóm tổ (K81_1)|Danh sách nhóm tổ]]
17. [[Thoi khoa bieu|Thời khóa biểu]] – tạo ở [[KHGD]] · menu [[Menu/Xếp thời khóa biểu tự động (K112)|Xếp thời khóa biểu tự động]]
18. [[KQ DKMH|Kết quả đăng ký môn học]] – tạo ở [[DKMH]] · menu [[Menu/ĐKMH từng sinh viên (M13)|ĐKMH từng sinh viên]]
19. [[Hoc phi|Học phí phải thu (đã tính)]] – tạo ở [[CSHP]] · menu [[Menu/Tính theo từng sinh viên (P21.01)|Tính theo từng sinh viên]]
20. [[Phieu thu|Phiếu thu học phí]] – tạo ở [[QLTV]] · menu [[Menu/Thu học phí 1 SV (V05)|Thu học phí 1 SV]]
21. **Nợ học phí** – tạo ở [[CSHP]]

## Là điều kiện cho (có dữ liệu này mới có)
- (không có dữ liệu nào phụ thuộc trực tiếp)

## Dùng ở
- [[DKMH]] – ràng buộc: SV nợ HP không được đăng ký
- [[QLHT]] – Cấm SV xem vì nợ học phí (web)
- [[QLTV]] – thu nợ

## Menu Edusoft
- [[Menu/Danh sách SV tồn nợ HP (D27.03)|Chính sách HP/ Chính sách học phí/ Nợ học phí/ Danh sách SV tồn nợ HP]]
- [[Menu/Cập nhật tồn nợ (D27.01)|Chính sách HP/ Chính sách học phí/ Nợ học phí/ Cập nhật tồn nợ]]
- Còn 14 menu khác có dùng / xem dữ liệu này – xem danh sách menu của phân hệ.

## Trên web
SV nợ bị chặn xem / đăng ký trên web.

## Khi dữ liệu này bị sửa / lỗi
Kiểm lại: [[DKMH]], [[QLHT]], [[QLTV]] và trang web liên quan.
Dữ liệu sinh ra từ nó (kiểm lại nếu số liệu đổi): —.
