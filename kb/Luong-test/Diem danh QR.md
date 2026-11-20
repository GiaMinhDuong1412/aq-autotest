---
loai: luong-test
ten: Điểm danh bằng mã QR (GV hiện mã – SV quét)
dau_hieu: "điểm danh|quét mã|mã qr|qr code"
phan_he:
  - "[[NETWEB-UI]]"
nen_tang: web
can_cung_cap:
  - "Mã GV: giảng viên có lớp đang dạy (để mở mã QR điểm danh)"
  - "MSSV: một sinh viên thuộc lớp của GV đó (để quét mã)"
buoc:
  - "Đăng nhập web bằng GV {Mã GV}, mở lớp đang dạy, bật điểm danh – mã QR hiển thị."
  - "Đăng nhập bằng SV {MSSV} (thuộc lớp đó), quét mã QR của GV."
  - "Kết quả: SV {MSSV} được điểm danh đúng buổi học của lớp."
khong_anh_huong:
  - "SV không thuộc lớp quét mã thì không được điểm danh."
trang_thai: tu-nguoi-dung
---
# Điểm danh bằng mã QR

Luồng do người dùng mô tả: cần **mã GV** → GV hiện mã QR → lấy **1 SV trong lớp đó** quét → kết quả điểm danh đúng → kiểm theo yêu cầu KH
(vd hộp ghi chú sau khi SV điểm danh **không bị làm mờ**, vẫn sửa được nội dung) là xong.

- Dữ liệu: [[Diem danh]] · cần có [[Thoi khoa bieu]], [[KQ DKMH]].
- Không cần tạo dữ liệu Edusoft – dùng tài khoản test người dùng cung cấp.
