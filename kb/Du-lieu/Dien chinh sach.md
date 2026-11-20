---
loai: du-lieu
ten: Diện chính sách / miễn giảm
tang: 6
tao_o: "[[QLSV]]"
dung_o:
  - "[[CSHP]]"
can_co:
  - "[[DS SV hoc ky]]"
la_dieu_kien_cho:
  - "[[Hoc phi]]"
tu_khoa: "diện chính sách|miễn giảm|học bổng"
tu_khoa_ph: []
nguon: luu-do
trang_thai: tu-tai-lieu
aliases:
  - "Diện chính sách / miễn giảm"
---
# Diện chính sách / miễn giảm

**Tạo ở** [[QLSV]] – `Sinh viên/ Miễn giảm hoc phí và Học bổng/ Sinh viên diện chính sách/ Diện chính sách sinh viên học kỳ (CSHP: Chính sách HP/ … / Miễn giảm học phí/ Diện chính sách sinh viên học kỳ)` · tầng 6 trong [[00 Logic nghiệp vụ]] (cần 9 loại dữ liệu có trước)

## Muốn có Diện chính sách / miễn giảm thì phải có trước
- [[DS SV hoc ky|Danh sách sinh viên học kỳ]] – diện chính sách gán cho SV trong học kỳ

## Chuẩn bị dữ liệu test (theo thứ tự)
1. [[Danh muc dao tao|Bậc – hệ – ngành đào tạo]] – tạo ở [[KHGD]]
2. [[Hoc ky|Năm học – học kỳ]] – tạo ở [[QLHT]] · menu [[Menu/Danh mục năm học học kỳ (H31)|Danh mục năm học học kỳ]]
3. [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]] – tạo ở [[KHGD]]
4. [[Ky tuyen sinh|Kỳ / đợt tuyển sinh (ngành, khối, phương thức)]] – tạo ở [[QLTS]] · menu [[Menu/Danh sách kỳ tuyển sinh (T1.01)|Danh sách kỳ tuyển sinh]]
5. [[Ho so thi sinh|Hồ sơ thí sinh]] – tạo ở [[QLTS]] · menu [[Menu/Nhập hồ sơ đăng ký xét tuyển (T2.03.00A)|Nhập hồ sơ đăng ký xét tuyển]]
6. [[Lop sinh vien|Lớp sinh viên]] – tạo ở [[QLSV]] · menu [[Menu/Danh mục lớp (S13)|Danh mục lớp]]
7. [[DS trung tuyen|Danh sách trúng tuyển]] – tạo ở [[QLTS]] · menu [[Menu/Danh sách trúng tuyển (T9.00)|Danh sách trúng tuyển]]
8. [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]] – tạo ở [[QLSV]] · menu [[Menu/Quyết định vào mới (S15.04)|Quyết định vào mới]]
9. [[DS SV hoc ky|Danh sách sinh viên học kỳ]] – tạo ở [[QLSV]] · menu [[Menu/Danh sách sinh viên học kỳ (S12)|Danh sách sinh viên học kỳ]]
10. **Diện chính sách / miễn giảm** – tạo ở [[QLSV]]

## Là điều kiện cho (có dữ liệu này mới có)
- [[Hoc phi|Học phí phải thu (đã tính)]]

## Dùng ở
- [[CSHP]] – miễn giảm khi tính học phí

## Menu Edusoft
- [[Menu/Diện chính sách sinh viên học kỳ (S163)|Sinh viên/ Miễn giảm hoc phí và Học bổng/ Sinh viên diện chính sách/ Diện chính sách sinh viên học kỳ]]
- Còn 87 menu khác có dùng / xem dữ liệu này – xem danh sách menu của phân hệ.

## Trên web
Miễn giảm hiện trong trang học phí của SV.

## Khi dữ liệu này bị sửa / lỗi
Kiểm lại: [[CSHP]] và trang web liên quan.
Dữ liệu sinh ra từ nó (kiểm lại nếu số liệu đổi): [[Hoc phi|Học phí phải thu]], [[Phieu thu|Phiếu thu học phí]], [[No hoc phi|Nợ học phí]].
