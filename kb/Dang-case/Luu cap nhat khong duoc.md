---
loai: dang-case
ten: Lưu / cập nhật / xóa dữ liệu không được
dau_hieu_kh: "không lưu|lưu không được|không cập nhật|mở lại (thì|bị) (trống|mất)|bị mất|không xóa|xóa không được|không ghi nhận"
dau_hieu_ba: "không lưu|cập nhật"
dau_hieu_dev: "store|update|insert|lưu"
noi_hay_gap:
  - edusoft
  - web
phan_he_hay_gap:
  - "[[QLSV]]"
  - "[[KHGD]]"
  - "[[DIEM]]"
  - "[[QLTS]]"
trang_thai: tu-tai-lieu
---
# Lưu / cập nhật / xóa dữ liệu không được

Nhập / sửa rồi bấm Lưu nhưng mở lại không thấy, hoặc báo thành công mà dữ liệu không đổi; xóa không được.

## Nhận biết
- **Lời KH**: `không lưu|lưu không được|không cập nhật|mở lại (thì|bị) (trống|mất)|bị mất|không xóa|xóa không được|không ghi nhận`
- **BA**: `không lưu|cập nhật`
- **Dev**: `store|update|insert|lưu`
(biểu thức để app gợi ý dạng case – sửa ở Properties `dau_hieu_*`)

## Phải trả lời khi phân tích
- Màn hình nào, trường (cột) nào không lưu
- Mọi bản ghi hay một trường hợp
- Có ràng buộc dữ liệu chặn (ô bắt buộc, khóa sổ học kỳ, phân quyền) không – xem trang Màn hình Edusoft

## Case liên quan với dạng này là
Các màn hình khác ghi cùng bảng dữ liệu; nơi khác đọc dữ liệu này (web hiển thị lý lịch…).

## Hay nhầm
Không lưu vì **khóa sổ / phân quyền** là đúng thiết kế → [[Thiet lap khong hieu luc]] hoặc [[Tai khoan phan quyen]].

## Phân hệ hay gặp
[[QLSV]], [[KHGD]], [[DIEM]], [[QLTS]]

## Case mẫu (tiêu đề từ danh sách ACS – cần đọc nội dung đầy đủ)
- 63527 (Cập nhật hồ sơ SV)

Xem cách đọc case: [[00 Cách phân tích case]].
