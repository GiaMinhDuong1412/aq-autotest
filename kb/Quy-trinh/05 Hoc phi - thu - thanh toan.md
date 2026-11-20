---
loai: quy-trinh
ten: "Học phí: tính → nợ → thu → thanh toán online"
thu_tu: 5
phan_he:
  - "[[CSHP]]"
  - "[[QLTV]]"
  - "[[EDUBILL]]"
  - "[[QKTX]]"
  - "[[QLSV]]"
  - "[[DKMH]]"
  - "[[QLHT]]"
  - "[[NETWEB-UI]]"
du_lieu:
  - "[[KQ DKMH]]"
  - "[[Dien chinh sach]]"
  - "[[Hop dong KTX]]"
  - "[[Hoc phi]]"
  - "[[No hoc phi]]"
  - "[[Phieu thu]]"
  - "[[Cau hinh NetWEB]]"
truoc:
  - "[[04 Dang ky mon hoc]]"
  - "[[02 Tuyen sinh - nhap hoc]]"
sau:
  - "[[04 Dang ky mon hoc]]"
nguon: luu-do + hdsd
trang_thai: tu-tai-lieu
tags: [quy-trinh]
aliases:
  - "Học phí: tính → nợ → thu → thanh toán online"
---
# Học phí: tính → nợ → thu → thanh toán online

*← [[04 Dang ky mon hoc]], [[02 Tuyen sinh - nhap hoc]]   ·   → [[04 Dang ky mon hoc]]*

**ĐKMH xong mới tính tiền.** Học phí = kết quả ĐKMH × đơn giá (theo chính sách) – miễn giảm (diện chính sách ở QLSV) + phụ thu (KTX…). Nợ học phí quay lại **chặn ĐKMH** và chặn xem web.

| # | Bước | Phân hệ | Menu | Phải có trước |
|---|---|---|---|---|
| 1 | Khai báo: loại hình thu, công thức, nhóm công thức, đơn giá (thường / đặc biệt), hình thức thu theo đối tượng | [[CSHP]] | `Chính sách HP/ Chính sách học phí/ Qui hoạch học phí/ …` | [[Hoc ky]] |
| 2 | Miễn giảm chính sách | [[QLSV]] → [[CSHP]] | `…/ Diện chính sách sinh viên học kỳ` | [[Dien chinh sach]] |
| 3 | Phụ thu (KTX, khoản khác) | [[CSHP]], [[QKTX]] | `Chính sách HP/ Chính sách học phí/ Phụ thu học phí/ …` | [[Hop dong KTX]] |
| 4 | **Tính học phí** | [[CSHP]] | `Chính sách HP/ Tính và In học phí/ Tính học phí/ …` | [[KQ DKMH]] |
| 5 | → DS SV nợ học phí | [[CSHP]] | `Chính sách HP/ Chính sách học phí/ Nợ học phí/ Danh sách SV tồn nợ HP` | |
| 6 | **Thu**: trực tiếp 1 SV, ngân hàng, import chuyển khoản, theo phiếu báo | [[QLTV]] | `Thu/chi HP/ Hoạt động thu/chi/ Thu học phí/ …` | [[Hoc phi]] |
| 7 | **Online qua EduBILL**: SV Xem học phí → [Đóng học phí] → trang EduBILL → phiếu thu tự về | [[NETWEB-UI]], [[EDUBILL]] → [[QLTV]] | web | xem cấu hình dưới |
| 8 | Bảng kê, danh sách phiếu thu học kỳ / tổng hợp | [[QLTV]] | `Thu/chi HP/ Hoạt động thu/chi/ Thu học phí/ Danh sách phiếu thu học kỳ` | [[Phieu thu]] |

> [!important] EduBILL – 3 chỗ phải khớp ([[HDSD EDUBILL]])
> 1. `skyline_apikey` ở `Hệ thống/ Quản trị NetWEB/ Chỉnh định chung` = khoá trên trang quản trị EduBILL (chỉ kiểm có khớp, **không** chép giá trị vào KB / plan).
> 2. Thời gian thanh toán: `Đăng ký MH/ Đăng ký môn học/ Thời hạn đóng hp/ Thời gian đóng học phí ngân hàng theo sv`.
> 3. **Học kỳ ở (2) phải trùng học kỳ thu học phí trong Chỉnh định chung** – khác thì nút [Đóng học phí] **bị ẩn** dù đang trong thời gian.
> Phiếu thu từ kênh EduBILL **không xoá / huỷ được** – test chỉ dùng SV test, số tiền nhỏ, môi trường test.

> [!warning] Hay gây case
> - "Học phí tính sai": kiểm KQ ĐKMH (môn, số TC học phí), đơn giá theo nhóm môn, diện chính sách, phụ thu – trước khi nghi công thức ([[So lieu tinh sai]]).
> - "SV đã đóng vẫn bị chặn ĐKMH / web": phiếu thu đã về chưa, đã tính lại nợ chưa ([[Tich hop thanh toan]]).
> - "Hiển thị miễn giảm / tổng tiền trên web lệch Edusoft" → [[Hien thi web]]; đối chiếu số liệu Edusoft trước.

**Sửa ở đây → kiểm lại:** [[04 Dang ky mon hoc]] (chặn nợ), web xem học phí, EduBILL, báo cáo thu. Tài liệu: [[HDSD QLTV]], [[HDSD EDUBILL]], [[HDSD QKTX]], [[Luu do LuuDo_NEW]].

---
Đọc cùng: [[00 Quy trình xuyên phân hệ]] · [[00 Cách phân tích case]]
