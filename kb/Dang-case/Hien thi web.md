---
loai: dang-case
ten: Hiển thị trên web sai / thiếu
dau_hieu_kh: "trang|web|cổng|portal|summary|hiển thị|giao diện|cột|bảng|tab|popup|nút|menu web|màn hình (sinh viên|giảng viên)|trình duyệt"
dau_hieu_ba: "giao diện|hiển thị|front ?end|trang"
dau_hieu_dev: "VersionSchool|netweb|\\.cshtml|\\.js|\\.vue|angular|frontend|css"
noi_hay_gap:
  - web
phan_he_hay_gap:
  - "[[NETWEB-UI]]"
  - "[[DKMHUI]]"
  - "[[CSHP]]"
  - "[[DIEM]]"
  - "[[KSDG]]"
  - "[[QLSV]]"
trang_thai: tu-tai-lieu
---
# Hiển thị trên web sai / thiếu

KH (thường là SV / GV / phòng đào tạo xem trên cổng) thấy **trên trang web** dữ liệu hiển thị sai chỗ, thiếu, lặp, sai thứ tự, sai định dạng. Dev sửa repo web (VersionSchool/<trường> hoặc Netweb).

## Nhận biết
- **Lời KH**: `trang|web|cổng|portal|summary|hiển thị|giao diện|cột|bảng|tab|popup|nút|menu web|màn hình (sinh viên|giảng viên)|trình duyệt`
- **BA**: `giao diện|hiển thị|front ?end|trang`
- **Dev**: `VersionSchool|netweb|\.cshtml|\.js|\.vue|angular|frontend|css`
(biểu thức để app gợi ý dạng case – sửa ở Properties `dau_hieu_*`)

## Phải trả lời khi phân tích
- Trang nào, vai trò nào (SV / GV / quản trị), trường nào (trang riêng của trường?)
- Sai là **cách hiển thị** hay **số liệu gốc** sai? Số liệu gốc sai → thêm dạng [[So lieu tinh sai]] và xem dữ liệu trên Edusoft
- Quy tắc hiển thị đúng do BA chốt (thứ tự, vị trí, định dạng)
- Dev sửa bản riêng trường (VersionSchool) hay phần dùng chung?

## Case liên quan với dạng này là
Cùng trang ở cùng trường; cùng trang ở trường khác (nếu phần dùng chung); case lần trước của cùng trang.

## Hay nhầm
Không suy ra Edusoft chỉ vì mã phân hệ là phân hệ Edusoft (CSHP, DIEM có trang web). Không gán kịch bản Edusoft.

## Phân hệ hay gặp
[[NETWEB-UI]], [[DKMHUI]], [[CSHP]], [[DIEM]], [[KSDG]], [[QLSV]]

## Case mẫu (tiêu đề từ danh sách ACS – cần đọc nội dung đầy đủ)
- 64457 (KTTC – miễn giảm trên trang học phí)
- 64852 (NNHN – UI rút môn)
- 64705, 63697

Xem cách đọc case: [[00 Cách phân tích case]].
