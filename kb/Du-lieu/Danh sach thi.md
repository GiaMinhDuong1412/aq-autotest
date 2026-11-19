---
loai: du-lieu
ten: Danh sách thi – lịch thi
tang: 9
tao_o: "[[LTHI]]"
dung_o:
  - "[[DIEM]]"
can_co:
  - "[[KQ DKMH]]"
  - "[[Nhom hoc]]"
  - "[[Phong hoc]]"
  - "[[Vien chuc]]"
la_dieu_kien_cho:
  - "[[Diem mon hoc]]"
tu_khoa: "lịch thi|nhóm thi|đợt thi|tổ thi|danh sách thi|coi thi|số báo danh|hoãn thi|trùng lịch"
tu_khoa_ph:
  - LTHI
nguon: luu-do
trang_thai: tu-tai-lieu
---
# Danh sách thi – lịch thi

**Tạo ở** [[LTHI]] – `Tổ chức thi/ … nhóm thi → đợt thi → tổ thi → Xếp lịch thi theo đợt thi` · tầng 9 trong [[00 Logic nghiệp vụ]] (cần 17 loại dữ liệu có trước)

## Muốn có Danh sách thi thì phải có trước
- [[KQ DKMH|Kết quả đăng ký môn học]] – SV dự thi = SV đã đăng ký môn
- [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]] – nhóm thi tạo từ nhóm học
- [[Phong hoc|Phòng học kỳ]] – phòng thi
- [[Vien chuc|Viên chức / cán bộ giảng dạy]] – phân công coi thi

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
18. **Danh sách thi – lịch thi** – tạo ở [[LTHI]]

## Là điều kiện cho (có dữ liệu này mới có)
- [[Diem mon hoc|Điểm môn học]]

## Dùng ở
- [[DIEM]] – tạo phách, bảng ghi điểm theo tổ thi

## Menu Edusoft
- [[Menu/Xếp lịch thi theo đợt thi (L39.03)|Tổ chức thi/ Xếp lịch thi/ Xếp lịch thi theo đợt thi]]
- Còn 103 menu khác có dùng / xem dữ liệu này – xem danh sách menu của phân hệ.

## Trên web
SV + GV xem lịch thi; GV xem lịch coi thi.

## Khi dữ liệu này bị sửa / lỗi
Kiểm lại: [[DIEM]] và trang web liên quan.
Dữ liệu sinh ra từ nó (kiểm lại nếu số liệu đổi): [[Diem mon hoc|Điểm môn học]], [[Diem trung binh|Điểm trung bình – tích lũy]], [[Ket qua hoc vu|Kết quả xét học vụ]], [[Ket qua tot nghiep|Kết quả xét tốt nghiệp]].
