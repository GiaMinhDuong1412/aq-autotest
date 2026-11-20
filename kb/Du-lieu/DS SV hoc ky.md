---
loai: du-lieu
ten: Danh sách sinh viên học kỳ
tang: 5
tao_o: "[[QLSV]]"
dung_o:
  - "[[CSHP]]"
  - "[[DKMH]]"
  - "[[KSDG]]"
  - "[[QKTX]]"
  - "[[QLTN]]"
  - "[[QXHV]]"
can_co:
  - "[[Quyet dinh sinh vien]]"
  - "[[Hoc ky]]"
la_dieu_kien_cho:
  - "[[Diem luan van]]"
  - "[[Diem ren luyen]]"
  - "[[Dien chinh sach]]"
  - "[[Nhom hoc]]"
  - "[[Ket qua khao sat]]"
  - "[[KQ DKMH]]"
  - "[[Ket qua hoc vu]]"
  - "[[Ket qua tot nghiep]]"
tu_khoa: "(danh sách )?sinh viên học kỳ|ds sv học kỳ"
tu_khoa_ph: []
nguon: luu-do
trang_thai: tu-tai-lieu
aliases:
  - "Danh sách sinh viên học kỳ"
---
# Danh sách sinh viên học kỳ

**Tạo ở** [[QLSV]] – `Sinh viên/ Sinh viên học kỳ/ Danh sách sinh viên học kỳ (tổng hợp tự động từ quyết định)` · tầng 5 trong [[00 Logic nghiệp vụ]] (cần 8 loại dữ liệu có trước)

## Muốn có Danh sách sinh viên học kỳ thì phải có trước
- [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]] – tổng hợp tự động từ quyết định vào / ra
- [[Hoc ky|Năm học – học kỳ]] – danh sách theo từng học kỳ

## Chuẩn bị dữ liệu test (theo thứ tự)
1. [[Danh muc dao tao|Bậc – hệ – ngành đào tạo]] – tạo ở [[KHGD]]
2. [[Hoc ky|Năm học – học kỳ]] – tạo ở [[QLHT]] · menu [[Menu/Danh mục năm học học kỳ (H31)|Danh mục năm học học kỳ]]
3. [[Khoi lop|Khối lớp (khóa đào tạo của 1 ngành)]] – tạo ở [[KHGD]]
4. [[Ky tuyen sinh|Kỳ / đợt tuyển sinh (ngành, khối, phương thức)]] – tạo ở [[QLTS]] · menu [[Menu/Danh sách kỳ tuyển sinh (T1.01)|Danh sách kỳ tuyển sinh]]
5. [[Ho so thi sinh|Hồ sơ thí sinh]] – tạo ở [[QLTS]] · menu [[Menu/Nhập hồ sơ đăng ký xét tuyển (T2.03.00A)|Nhập hồ sơ đăng ký xét tuyển]]
6. [[Lop sinh vien|Lớp sinh viên]] – tạo ở [[QLSV]] · menu [[Menu/Danh mục lớp (S13)|Danh mục lớp]]
7. [[DS trung tuyen|Danh sách trúng tuyển]] – tạo ở [[QLTS]] · menu [[Menu/Danh sách trúng tuyển (T9.00)|Danh sách trúng tuyển]]
8. [[Quyet dinh sinh vien|Quyết định vào / ra sinh viên]] – tạo ở [[QLSV]] · menu [[Menu/Quyết định vào mới (S15.04)|Quyết định vào mới]]
9. **Danh sách sinh viên học kỳ** – tạo ở [[QLSV]]

## Là điều kiện cho (có dữ liệu này mới có)
- [[Diem luan van|Điểm luận văn]]
- [[Diem ren luyen|Điểm rèn luyện]]
- [[Dien chinh sach|Diện chính sách / miễn giảm]]
- [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)]]
- [[Ket qua khao sat|Kết quả khảo sát]]
- [[KQ DKMH|Kết quả đăng ký môn học]]
- [[Ket qua hoc vu|Kết quả xét học vụ]]
- [[Ket qua tot nghiep|Kết quả xét tốt nghiệp]]

## Dùng ở
- [[DKMH]] – SV được đăng ký môn học (phải có trong DS SV học kỳ)
- [[CSHP]] – SV tính học phí
- [[KSDG]] – đáp viên
- [[QXHV]] – DS SV xét
- [[QLTN]] – DS SV xét
- [[QKTX]] – SV ở ký túc xá

## Menu Edusoft
- [[Menu/Danh sách sinh viên học kỳ (S12)|Sinh viên/ Sinh viên học kỳ/ Danh sách sinh viên học kỳ]]
- Còn 52 menu khác có dùng / xem dữ liệu này – xem danh sách menu của phân hệ.

## Trên web
Quyền dùng web của SV trong học kỳ.

## Khi dữ liệu này bị sửa / lỗi
Kiểm lại: [[CSHP]], [[DKMH]], [[KSDG]], [[QKTX]], [[QLTN]], [[QXHV]] và trang web liên quan.
Dữ liệu sinh ra từ nó (kiểm lại nếu số liệu đổi): [[Diem luan van|Điểm luận văn]], [[Diem ren luyen|Điểm rèn luyện]], [[Dien chinh sach|Diện chính sách / miễn giảm]], [[Nhom hoc|Nhóm học – kế hoạch giảng dạy học kỳ]], [[Ket qua khao sat|Kết quả khảo sát]], [[Thoi khoa bieu|Thời khóa biểu]], [[KQ DKMH|Kết quả đăng ký môn học]], [[Khoi luong giang day|Khối lượng giảng dạy]], [[Danh sach thi|Danh sách thi – lịch thi]], [[Hoc phi|Học phí phải thu]], [[Diem mon hoc|Điểm môn học]], [[Phieu thu|Phiếu thu học phí]], [[Diem trung binh|Điểm trung bình – tích lũy]], [[No hoc phi|Nợ học phí]], [[Ket qua hoc vu|Kết quả xét học vụ]], [[Ket qua tot nghiep|Kết quả xét tốt nghiệp]].
