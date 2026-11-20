---
loai: quy-trinh
ten: "Hoạt động trên lớp: điểm danh, nghỉ dạy – dạy bù, khảo sát"
thu_tu: 9
phan_he:
  - "[[KHGD]]"
  - "[[NETWEB-UI]]"
  - "[[EDUGO]]"
  - "[[KSDG]]"
  - "[[QLSV]]"
du_lieu:
  - "[[Thoi khoa bieu]]"
  - "[[Nhom hoc]]"
  - "[[Diem danh]]"
  - "[[Ket qua khao sat]]"
truoc:
  - "[[03 CTDT - TKB]]"
  - "[[04 Dang ky mon hoc]]"
sau: []
nguon: luu-do + hdsd
trang_thai: tu-tai-lieu
tags: [quy-trinh]
aliases:
  - "Hoạt động trên lớp: điểm danh, nghỉ dạy – dạy bù, khảo sát"
---
# Hoạt động trên lớp: điểm danh, nghỉ dạy – dạy bù, khảo sát

*← [[03 CTDT - TKB]], [[04 Dang ky mon hoc]]*

Dựa trên **TKB + danh sách lớp học phần (KQ ĐKMH)** của học kỳ. Phần lớn thao tác ở **web / app** (GV, SV).

| Việc | Phân hệ / nơi làm | Phải có trước | Luồng test |
|---|---|---|---|
| Điểm danh trực tuyến / **bằng mã QR** (GV hiện mã, SV trong lớp quét) | [[NETWEB-UI]], [[EDUGO]] | [[Thoi khoa bieu]], [[KQ DKMH]] | [[Diem danh QR]] |
| Nghỉ dạy – dạy bù (GV đăng ký online, phòng đào tạo duyệt) | [[KHGD]], [[NETWEB-UI]] | [[Thoi khoa bieu]], [[Phong hoc]] | |
| Khảo sát đánh giá (form → kỳ ĐG → DS được ĐG, đáp viên → SV đánh giá trên web → kết quả) | [[KSDG]], [[NETWEB-UI]] | [[Nhom hoc]], [[Vien chuc]] | |
| Điểm rèn luyện trực tuyến | [[QLSV]], [[NETWEB-UI]] | [[DS SV hoc ky]] | |

> [!warning] Hay gây case
> - Case sửa **giao diện web** (ô bị khoá / làm mờ, nút ẩn) → test trên web theo đúng vai trò (GV / SV), không gán kịch bản Edusoft ([[Hien thi web]]).
> - Điểm danh cần tài khoản GV có lớp đang dạy + SV thuộc lớp đó – hỏi người dùng (plan test).

Tài liệu: [[HDSD NETWEB]], [[HDSD KHGD]], [[HDSD KSDG]], [[HDSD EDUGO]].

---
Đọc cùng: [[00 Quy trình xuyên phân hệ]] · [[00 Cách phân tích case]]
