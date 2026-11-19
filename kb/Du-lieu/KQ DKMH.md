---
loai: du-lieu
ten: Kết quả đăng ký môn học
tang: 8
tao_o: "[[DKMH]]"
dung_o:
  - "[[CSHP]]"
  - "[[DIEM]]"
  - "[[LTHI]]"
  - "[[QLSV]]"
can_co:
  - "[[DS SV hoc ky]]"
  - "[[Nhom hoc]]"
  - "[[Thoi khoa bieu]]"
  - "[[Rang buoc DKMH]]"
la_dieu_kien_cho:
  - "[[Danh sach thi]]"
  - "[[Hoc phi]]"
  - "[[Diem mon hoc]]"
nguon: luu-do
trang_thai: tu-tai-lieu
---
# Kết quả đăng ký môn học

**Tạo ở** [[DKMH]] – `Đăng ký MH/ Đăng ký môn học/ … (offline) hoặc SV đăng ký trên web → Khai thác báo biểu/ Kết quả đăng ký/ Xem file MH đã đăng ký` · tầng 8 trong [[00 Logic nghiệp vụ]] (cần 16 loại dữ liệu có trước)

## Muốn có Kết quả đăng ký môn học thì phải có trước
- [[DS SV hoc ky|Danh sách sinh viên học kỳ]] – chỉ SV có trong DS SV học kỳ mới đăng ký được
- [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]] – chọn nhóm học còn chỗ
- [[Thoi khoa bieu|Thời khóa biểu]] – nhóm có lịch, không trùng TKB
- [[Rang buoc DKMH|Ràng buộc & thời gian đăng ký]] – được phép đăng ký (thời gian, tiên quyết, tín chỉ, nợ học phí)

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
15. [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]] – tạo ở [[KHGD]] · menu [[Menu/Danh sách nhóm tổ (K81_1)|Danh sách nhóm tổ]]
16. [[Thoi khoa bieu|Thời khóa biểu]] – tạo ở [[KHGD]] · menu [[Menu/Xếp thời khóa biểu tự động (K112)|Xếp thời khóa biểu tự động]]
17. **Kết quả đăng ký môn học** – tạo ở [[DKMH]]

## Là điều kiện cho (có dữ liệu này mới có)
- [[Danh sach thi|Danh sách thi – lịch thi]]
- [[Hoc phi|Học phí phải thu (đã tính)]]
- [[Diem mon hoc|Điểm môn học]]

## Dùng ở
- [[CSHP]] – tính học phí
- [[LTHI]] – nguồn danh sách thi
- [[DIEM]] – bảng ghi điểm, nhập điểm
- [[QLSV]] – điểm danh; xóa kết quả SV đã hủy ĐKMH

## Menu Edusoft
- [[Menu/ĐKMH từng sinh viên (M13)|Đăng ký MH/ Đăng ký môn học/ ĐKMH từng sinh viên]]
- [[Menu/Theo lớp (M11.01)|Đăng ký MH/ Đăng ký môn học/ Đăng ký tự động/ Theo lớp]]
- Còn 118 menu khác có dùng / xem dữ liệu này – xem danh sách menu của phân hệ.

## Trên web
SV xem môn đã đăng ký, học phí tạm tính; CVHT duyệt.

## Khi dữ liệu này bị sửa / lỗi
Kiểm lại: [[CSHP]], [[DIEM]], [[LTHI]], [[QLSV]] và trang web liên quan.
Dữ liệu sinh ra từ nó (kiểm lại nếu số liệu đổi): [[Danh sach thi|Danh sách thi – lịch thi]], [[Hoc phi|Học phí phải thu]], [[Diem mon hoc|Điểm môn học]], [[Phieu thu|Phiếu thu học phí]], [[Diem trung binh|Điểm trung bình – tích lũy]], [[No hoc phi|Nợ học phí]], [[Ket qua hoc vu|Kết quả xét học vụ]], [[Ket qua tot nghiep|Kết quả xét tốt nghiệp]].
