---
loai: dang-case
ten: Case tiếp nối / mở lại (lần 2, case gốc)
dau_hieu_kh: "\\[\\d{5,6}\\]|lần [2-9]\\b|lần (hai|ba)|tiếp theo case|case (trước|cũ)|vẫn chưa (được )?(xử lý|sửa|khắc phục)|tái diễn|mở lại case"
dau_hieu_ba: "case (gốc|trước)|lần trước"
dau_hieu_dev: "lan-\\d|lần \\d"
noi_hay_gap: []
phan_he_hay_gap: []
trang_thai: tu-tai-lieu
---
# Case tiếp nối / mở lại (lần 2, case gốc)

Tiêu đề có `[mã case]` hoặc "lần 2", lời KH nói "vẫn còn / vẫn chưa" → đây là phần tiếp của một case trước.

## Nhận biết
- **Lời KH**: `\[\d{5,6}\]|lần [2-9]\b|lần (hai|ba)|tiếp theo case|case (trước|cũ)|vẫn chưa (được )?(xử lý|sửa|khắc phục)|tái diễn|mở lại case`
- **BA**: `case (gốc|trước)|lần trước`
- **Dev**: `lan-\d|lần \d`
(biểu thức để app gợi ý dạng case – sửa ở Properties `dau_hieu_*`)

## Phải trả lời khi phân tích
- Case gốc là gì, lần trước sửa gì, test lần trước kết luận gì
- Lần này còn thiếu gì so với lần trước (chỉ phần đó là mới)
- Phần lần trước đã đạt có bị hỏng lại không

## Case liên quan với dạng này là
**Case gốc** (đọc trước) và các case cùng mã gốc.

## Hay nhầm
Không test lại từ đầu như case mới mà bỏ qua kết quả lần trước.

## Phân hệ hay gặp
mọi phân hệ

## Case mẫu (tiêu đề từ danh sách ACS – cần đọc nội dung đầy đủ)
- 64457 ([64184] – lần 2)
- 64656 ([64504])

Xem cách đọc case: [[00 Cách phân tích case]].
