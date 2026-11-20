---
loai: dang-case
ten: Nhờ xử lý dữ liệu / dữ liệu sai do thao tác
dau_hieu_kh: "nhờ (xử lý|cập nhật|chuyển|xóa|sửa) (giúp|dữ liệu)|import|chuyển dữ liệu|dữ liệu (bị )?(sai|thiếu)|nhập nhầm|khôi phục|phục hồi"
dau_hieu_ba: "dữ liệu|không phải lỗi|thao tác|hướng dẫn"
dau_hieu_dev: "script|update dữ liệu|sql|xử lý dữ liệu"
noi_hay_gap:
  - edusoft
phan_he_hay_gap:
  - "[[QLSV]]"
  - "[[DIEM]]"
  - "[[DKMH]]"
  - "[[QLTS]]"
trang_thai: tu-tai-lieu
---
# Nhờ xử lý dữ liệu / dữ liệu sai do thao tác

Phần mềm đúng nhưng dữ liệu của trường sai / thiếu (do nhập nhầm, import thiếu) – AQ chạy script sửa dữ liệu hoặc hướng dẫn trường.

## Nhận biết
- **Lời KH**: `nhờ (xử lý|cập nhật|chuyển|xóa|sửa) (giúp|dữ liệu)|import|chuyển dữ liệu|dữ liệu (bị )?(sai|thiếu)|nhập nhầm|khôi phục|phục hồi`
- **BA**: `dữ liệu|không phải lỗi|thao tác|hướng dẫn`
- **Dev**: `script|update dữ liệu|sql|xử lý dữ liệu`
(biểu thức để app gợi ý dạng case – sửa ở Properties `dau_hieu_*`)

## Phải trả lời khi phân tích
- BA / Dev kết luận **không phải lỗi phần mềm**?
- Dữ liệu nào, của trường nào, đã sửa bằng gì (script) – test là kiểm dữ liệu sau xử lý
- Có cần hướng dẫn KH thao tác đúng không

## Case liên quan với dạng này là
Dữ liệu sinh ra từ dữ liệu đã sửa (vd sửa KQ ĐKMH → học phí, danh sách thi) phải được tính lại.

## Hay nhầm
Không mở case lỗi phần mềm cho trường hợp này; không thao tác dữ liệu thật của trường.

## Phân hệ hay gặp
[[QLSV]], [[DIEM]], [[DKMH]], [[QLTS]]

## Case mẫu (tiêu đề từ danh sách ACS – cần đọc nội dung đầy đủ)
- (chưa có)

Xem cách đọc case: [[00 Cách phân tích case]].
