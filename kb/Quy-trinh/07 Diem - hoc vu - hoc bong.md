---
loai: quy-trinh
ten: "Điểm → điểm TB → học vụ, học bổng"
thu_tu: 7
phan_he:
  - "[[DIEM]]"
  - "[[QXHV]]"
  - "[[QLSV]]"
  - "[[NETWEB-UI]]"
  - "[[BVLV]]"
  - "[[KSDG]]"
du_lieu:
  - "[[KQ DKMH]]"
  - "[[Danh sach thi]]"
  - "[[Diem mon hoc]]"
  - "[[Diem trung binh]]"
  - "[[Ket qua hoc vu]]"
  - "[[Diem ren luyen]]"
truoc:
  - "[[04 Dang ky mon hoc]]"
  - "[[06 To chuc thi]]"
sau:
  - "[[08 Tot nghiep - luan van]]"
nguon: luu-do + hdsd
trang_thai: tu-tai-lieu
tags: [quy-trinh]
aliases:
  - "Điểm → điểm TB → học vụ, học bổng"
---
# Điểm → điểm TB → học vụ, học bổng

*← [[04 Dang ky mon hoc]], [[06 To chuc thi]]   ·   → [[08 Tot nghiep - luan van]]*

**Có KQ ĐKMH mới có danh sách ghi điểm.** Điểm TB là đầu vào của học vụ, học bổng, tốt nghiệp.

| # | Bước | Phân hệ | Menu | Phải có trước |
|---|---|---|---|---|
| 1 | In bảng ghi điểm (theo danh sách học) | [[DIEM]] | `Quản lý điểm/ Bảng ghi điểm/ In bảng ghi điểm/ …` | [[KQ DKMH]] |
| 2 | Nhập điểm: Edusoft / import Excel / **GV nhập online** / từ phách / bảo lưu / phúc khảo | [[DIEM]], [[NETWEB-UI]] | `Quản lý nhập điểm/ …` | phân quyền nhập điểm |
| 3 | Chỉnh định: biến tính điểm, công thức, không quản lý điểm, môn thay thế | [[DIEM]] | `Quản lý điểm/ Quản trị phân hệ/ Chỉnh định thông số toàn cục`, `…/ Công thức tính điểm/ …` | |
| 4 | **Tính điểm TB** → phiếu điểm | [[DIEM]] | `Quản lý điểm/ Quản lý điểm tổng kết học phần/ Tổng kết điểm thi/ …` | [[Diem mon hoc]] |
| 5 | **Xét học vụ** (tiêu chuẩn → đợt → lớp → SV xét → kết quả) | [[QXHV]] | `Quản lý điểm/ Xử lý học vụ học kỳ/ …` | [[Diem trung binh]] |
| 6 | Điểm rèn luyện (SV tự đánh giá, GV/CVHT duyệt trên web) | [[QLSV]], [[NETWEB-UI]] | `Sinh viên/ Điểm danh và Điểm rèn luyện/ …` | [[DS SV hoc ky]] |
| 7 | Học bổng khuyến khích (điểm TB + DRL) | [[QLSV]] | (`QLSV_XetHocBongKhuyenKhich`) | [[Diem trung binh]], [[Diem ren luyen]] |

> [!warning] Hay gây case
> - "GV không nhập được điểm": phân quyền nhập điểm, trạng thái khoá điểm, hạn nhập ([[Tai khoan phan quyen]], [[HDSD DIEM]] `DIEM_PhanQuyenNhapDiem`).
> - "Điểm TB sai": biến tính điểm / công thức / môn không tích luỹ / môn thay thế – theo **quy chế của trường** (TT56 hay quy chế riêng) → [[00 Mô hình trường|mô hình trường]] ([[So lieu tinh sai]]).
> - Điểm trên web lệch Edusoft → chưa tính lại TB hoặc web lọc theo học kỳ / trạng thái công bố ([[Hien thi web]]).

**Sửa ở đây → kiểm lại:** [[QXHV]], học bổng, [[08 Tot nghiep - luan van]], phiếu điểm / bảng điểm (mẫu in), web xem điểm. Tài liệu: [[HDSD DIEM]], [[HDSD NETWEB]].

---
Đọc cùng: [[00 Quy trình xuyên phân hệ]] · [[00 Cách phân tích case]]
