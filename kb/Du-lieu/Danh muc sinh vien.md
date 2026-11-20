---
loai: du-lieu
ten: Danh mục sinh viên (mọi SV của trường)
tang: 5
tao_o: "[[QLSV]]"
dung_o:
  - "[[NETWEB-API]]"
can_co:
  - "[[Quyet dinh sinh vien]]"
la_dieu_kien_cho:
  - "[[Hop dong KTX]]"
tu_khoa: "danh mục sinh viên|lý lịch|hồ sơ (sinh viên|sv)|thông tin sinh viên|văn bằng"
tu_khoa_ph:
  - QLSV
nguon: luu-do
trang_thai: tu-tai-lieu
aliases:
  - "Danh mục sinh viên (mọi SV của trường)"
---
# Danh mục sinh viên (mọi SV của trường)

**Tạo ở** [[QLSV]] – `Sinh viên/ Sinh viên học kỳ/ Danh mục sinh viên` · tầng 5 trong [[00 Logic nghiệp vụ]] (cần 8 loại dữ liệu có trước)

## Muốn có Danh mục sinh viên thì phải có trước
- [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]] – QĐ vào mới tạo hồ sơ sinh viên

## Chuẩn bị dữ liệu test (theo thứ tự)
1. [[Danh muc dao tao|Bậc – hệ – ngành đào tạo]] – tạo ở [[KHGD]]
2. [[Hoc ky|Năm học – học kỳ]] – tạo ở [[QLHT]] · menu [[Menu/Danh mục năm học học kỳ (H31)|Danh mục năm học học kỳ]]
3. [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]] – tạo ở [[KHGD]]
4. [[Ky tuyen sinh|Kỳ / đợt tuyển sinh (ngành, khối, phương thức)]] – tạo ở [[QLTS]] · menu [[Menu/Danh sách kỳ tuyển sinh (T1.01)|Danh sách kỳ tuyển sinh]]
5. [[Ho so thi sinh|Hồ sơ thí sinh]] – tạo ở [[QLTS]] · menu [[Menu/Nhập hồ sơ đăng ký xét tuyển (T2.03.00A)|Nhập hồ sơ đăng ký xét tuyển]]
6. [[Lop sinh vien|Lớp sinh viên]] – tạo ở [[QLSV]] · menu [[Menu/Danh mục lớp (S13)|Danh mục lớp]]
7. [[DS trung tuyen|Danh sách trúng tuyển]] – tạo ở [[QLTS]] · menu [[Menu/Danh sách trúng tuyển (T9.00)|Danh sách trúng tuyển]]
8. [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]] – tạo ở [[QLSV]] · menu [[Menu/Quyết định vào mới (S15.04)|Quyết định vào mới]]
9. **Danh mục sinh viên (mọi SV của trường)** – tạo ở [[QLSV]]

## Là điều kiện cho (có dữ liệu này mới có)
- [[Hop dong KTX|Hợp đồng ký túc xá]]

## Dùng ở
- [[QLSV]] – lý lịch, hồ sơ – văn bằng
- [[NETWEB-API]] – tài khoản SV đăng nhập web

## Menu Edusoft
- [[Menu/Danh mục sinh viên (S11)|Sinh viên/ Sinh viên học kỳ/ Danh mục sinh viên]]
- Còn 56 menu khác có dùng / xem dữ liệu này – xem danh sách menu của phân hệ.

## Trên web
SV xem / cập nhật lý lịch.

## Khi dữ liệu này bị sửa / lỗi
Kiểm lại: [[NETWEB-API]] và trang web liên quan.
Dữ liệu sinh ra từ nó (kiểm lại nếu số liệu đổi): [[Hop dong KTX|Hợp đồng ký túc xá]].
