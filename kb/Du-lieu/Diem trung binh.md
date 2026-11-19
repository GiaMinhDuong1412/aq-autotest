---
loai: du-lieu
ten: Điểm trung bình – tích lũy
tang: 11
tao_o: "[[DIEM]]"
dung_o:
  - "[[QLSV]]"
  - "[[QLTN]]"
  - "[[QXHV]]"
can_co:
  - "[[Diem mon hoc]]"
la_dieu_kien_cho:
  - "[[Ket qua hoc vu]]"
  - "[[Ket qua tot nghiep]]"
tu_khoa: "điểm trung bình|điểm tb|tích lũy|phiếu điểm|tổng kết|xếp loại"
tu_khoa_ph:
  - DIEM
nguon: luu-do
trang_thai: tu-tai-lieu
---
# Điểm trung bình – tích lũy

**Tạo ở** [[DIEM]] – `Quản lý điểm/ Quản lý điểm tổng kết học phần/ Tổng kết điểm thi/ Cộng điểm TB → In phiếu điểm sinh viên` · tầng 11 trong [[00 Logic nghiệp vụ]] (cần 19 loại dữ liệu có trước)

## Muốn có Điểm trung bình thì phải có trước
- [[Diem mon hoc|Điểm môn học]] – cộng điểm trung bình từ điểm môn học

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
17. [[KQ DKMH|Kết quả đăng ký môn học]] – tạo ở [[DKMH]] · menu [[Menu/ĐKMH từng sinh viên (M13)|ĐKMH từng sinh viên]]
18. [[Danh sach thi|Danh sách thi – lịch thi]] – tạo ở [[LTHI]] · menu [[Menu/Xếp lịch thi theo đợt thi (L39.03)|Xếp lịch thi theo đợt thi]]
19. [[Diem mon hoc|Điểm môn học]] – tạo ở [[DIEM]] · menu [[Menu/Nhập điểm theo nhóm học (D21.03)|Nhập điểm theo nhóm học]]
20. **Điểm trung bình – tích lũy** – tạo ở [[DIEM]]

## Là điều kiện cho (có dữ liệu này mới có)
- [[Ket qua hoc vu|Kết quả xét học vụ]]
- [[Ket qua tot nghiep|Kết quả xét tốt nghiệp]]

## Dùng ở
- [[QXHV]] – xét học vụ
- [[QLTN]] – xét tốt nghiệp
- [[QLSV]] – xét học bổng

## Menu Edusoft
- [[Menu/Cộng điểm TB - từng sinh viên (D52.03)|Quản lý điểm/ Quản lý điểm tổng kết học phần/ Tổng kết điểm thi/ Cộng điểm TB - từng sinh viên]]
- [[Menu/Cộng điểm TB - theo lớp (D52.06)|Quản lý điểm/ Quản lý điểm tổng kết học phần/ Tổng kết điểm thi/ Cộng điểm TB - theo lớp]]
- Còn 71 menu khác có dùng / xem dữ liệu này – xem danh sách menu của phân hệ.

## Trên web
SV xem điểm, phiếu điểm.

## Khi dữ liệu này bị sửa / lỗi
Kiểm lại: [[QLSV]], [[QLTN]], [[QXHV]] và trang web liên quan.
Dữ liệu sinh ra từ nó (kiểm lại nếu số liệu đổi): [[Ket qua hoc vu|Kết quả xét học vụ]], [[Ket qua tot nghiep|Kết quả xét tốt nghiệp]].
