---
loai: dang-case
ten: Lỗi chương trình (EX) khi thao tác trên Edusoft
dau_hieu_kh: "báo lỗi|lỗi ex|exception|object reference|không mở được|văng|thoát ra|error|lỗi khi (bấm|lưu|mở|in)|hộp thoại lỗi"
dau_hieu_ba: "lỗi chương trình|exception|tái hiện được"
dau_hieu_dev: "Source\\.NET|\\.cs\\b|null ?reference|exception|try ?catch"
noi_hay_gap:
  - edusoft
phan_he_hay_gap:
  - "[[QLSV]]"
  - "[[DIEM]]"
  - "[[QLTS]]"
  - "[[KHGD]]"
  - "[[DKMH]]"
trang_thai: tu-tai-lieu
---
# Lỗi chương trình (EX) khi thao tác trên Edusoft

Thao tác trên **một menu Edusoft cụ thể** thì hiện hộp lỗi (EX, Object reference…) hoặc chương trình thoát. Thường phát hiện khi KH dùng hoặc khi AQ test release.

## Nhận biết
- **Lời KH**: `báo lỗi|lỗi ex|exception|object reference|không mở được|văng|thoát ra|error|lỗi khi (bấm|lưu|mở|in)|hộp thoại lỗi`
- **BA**: `lỗi chương trình|exception|tái hiện được`
- **Dev**: `Source\.NET|\.cs\b|null ?reference|exception|try ?catch`
(biểu thức để app gợi ý dạng case – sửa ở Properties `dau_hieu_*`)

## Phải trả lời khi phân tích
- Menu nào (đường dẫn đủ), thao tác nào (bấm nút gì, với dữ liệu nào)
- Lỗi xảy ra với mọi dữ liệu hay một trường hợp (SV, lớp cụ thể)?
- Ảnh chụp chi tiết lỗi (Ctrl+Shift+E) và mã menu (Ctrl+Shift+F) có trong case không?
- Dev sửa code màn hình hay store / dữ liệu?

## Case liên quan với dạng này là
Cùng menu (mọi trường); các menu cùng nhóm dùng chung màn hình / store; case lỗi EX trước đó của menu này.

## Hay nhầm
Lỗi do **dữ liệu** của trường (thiếu danh mục, dữ liệu bẩn) → là [[Xu ly du lieu]], không phải lỗi code.

## Phân hệ hay gặp
[[QLSV]], [[DIEM]], [[QLTS]], [[KHGD]], [[DKMH]]

## Case mẫu (tiêu đề từ danh sách ACS – cần đọc nội dung đầy đủ)
- 63520 (In phiếu điểm – từng SV)
- 63525 (Xét học vụ theo lớp)
- 64361 (Nhập hồ sơ đăng ký xét tuyển)

Xem cách đọc case: [[00 Cách phân tích case]].
