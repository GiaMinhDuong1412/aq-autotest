---
loai: quy-trinh
ten: "Đăng ký môn học"
thu_tu: 4
phan_he:
  - "[[DKMH]]"
  - "[[DKMHUI]]"
  - "[[NETWEB-UI]]"
  - "[[QLSV]]"
  - "[[KHGD]]"
  - "[[CSHP]]"
  - "[[QLHT]]"
du_lieu:
  - "[[DS SV hoc ky]]"
  - "[[CTDT]]"
  - "[[Nhom hoc]]"
  - "[[Thoi khoa bieu]]"
  - "[[Rang buoc DKMH]]"
  - "[[No hoc phi]]"
  - "[[KQ DKMH]]"
truoc:
  - "[[02 Tuyen sinh - nhap hoc]]"
  - "[[03 CTDT - TKB]]"
  - "[[01 Mo hoc ky moi]]"
sau:
  - "[[05 Hoc phi - thu - thanh toan]]"
  - "[[06 To chuc thi]]"
  - "[[07 Diem - hoc vu - hoc bong]]"
nguon: luu-do + hdsd
trang_thai: tu-tai-lieu
tags: [quy-trinh]
aliases:
  - "Đăng ký môn học"
---
# Đăng ký môn học

*← [[02 Tuyen sinh - nhap hoc]], [[03 CTDT - TKB]], [[01 Mo hoc ky moi]]   ·   → [[05 Hoc phi - thu - thanh toan]], [[06 To chuc thi]], [[07 Diem - hoc vu - hoc bong]]*

**Muốn ĐKMH được thì phải có:** SV trong [[DS SV hoc ky]] ([[QLSV]]) + nhóm học có TKB ([[KHGD]]) + CTĐT thực hiện + học kỳ ([[QLHT]]) + ràng buộc & thời gian đăng ký. **ĐKMH xong** → [[CSHP]] tính học phí, [[LTHI]] lập danh sách thi, [[DIEM]] có danh sách ghi điểm.

| # | Bước | Phân hệ | Menu | Phải có trước |
|---|---|---|---|---|
| 1 | Ràng buộc: tiên quyết / học trước / song hành, tín chỉ tối đa, cải thiện | [[DKMH]] | `Đăng ký MH/ Đăng ký môn học/ Tài nguyên và ràng buộc/ …` | [[Mon hoc]] |
| 2 | Chặn SV nợ học phí | [[CSHP]] → [[DKMH]] | `Chính sách HP/ Chính sách học phí/ Nợ học phí/ Danh sách SV tồn nợ HP` | [[No hoc phi]] |
| 3 | Đối tượng & **thời gian đăng ký** (offline: thông số học kỳ; online: lớp không ĐK, thời gian theo lớp, chỉnh định chung) | [[DKMH]], [[QLHT]] | xem "Thời gian online" dưới | [[Lop sinh vien]] |
| 4a | **Offline**: phòng đào tạo đăng ký thay (tự động / theo tập tin / từng SV) | [[DKMH]] | `Đăng ký MH/ Đăng ký môn học/ …` | [[Nhom hoc]], [[DS SV hoc ky]] |
| 4b | **Online**: SV đăng ký trên web (hoặc trang ĐKMH riêng) → CVHT duyệt | [[NETWEB-UI]], [[DKMHUI]] | web | như 4a + [[Rang buoc DKMH]] |
| 5 | Kết quả / KQĐK không hợp lệ; rút môn, huỷ – phục hồi KQ | [[DKMH]] | `Đăng ký MH/ Khai thác báo biểu/ Kết quả đăng ký/ Xem file MH đã đăng ký` | |

> [!important] Thời gian ĐKMH online – 4 chỗ phải khớp ([[HDSD DKMH]] `DKMH_ChinhDinhThoiGianDangKyOnline`)
> 1. `SM00_CAMDKTT_DIEN` (Chỉnh định thông số học kỳ của ĐKMH) = **Không** (không cấm ĐK online).
> 2. `SM00_TGCPDK` (Hệ thống/ Quản trị hệ thống/ Chỉnh định thông số hệ thống – phân hệ Edusoft.Web, biến theo học kỳ) = **Có giới hạn**.
> 3. `GH_THOIGIANDKTRONGNGAYEDUWEB` (cùng menu) = giờ bắt đầu – kết thúc trong ngày.
> 4. `Đăng ký MH/ Đăng ký môn học/ Tài nguyên và ràng buộc/ Chỉnh định thời gian đăng ký` theo đối tượng.
> Sau khi đặt: **restart IIS** máy chủ Edusoft.Web mới áp dụng. Case "đã cài thời gian mà SV vẫn không đăng ký được" → kiểm đủ 4 chỗ + IIS trước khi kết luận lỗi ([[Thiet lap khong hieu luc]]).

> [!warning] Hay gây case
> - SV không thấy môn / nhóm: SV chưa có trong DS SV học kỳ, nhóm chưa có TKB / hết chỗ, lớp SV nằm trong "Lớp sinh viên không đăng ký".
> - SV bị chặn vì nợ học phí ([[05 Hoc phi - thu - thanh toan]]) – kiểm phiếu thu đã ghi nhận chưa.
> - Đợt ĐKMH tải rất lớn → [[Hieu nang]].
> - Nhiều trường dùng trang ĐKMH riêng → [[DKMHUI]] + [[00 Mô hình trường|mô hình trường]].

**Sửa ở đây → kiểm lại:** học phí ([[CSHP]]), danh sách thi ([[LTHI]]), danh sách ghi điểm ([[DIEM]]), web xem KQĐK / TKB cá nhân. Tài liệu: [[HDSD DKMH]], [[HDSD NETWEB]] (`NetWEB_GiangVienDuyetKQDK`).

---
Đọc cùng: [[00 Quy trình xuyên phân hệ]] · [[00 Cách phân tích case]]
