---
loai: ban-do
tags: [moc, case-truong]
aliases:
  - "Case theo trường"
---
# Mô hình trường – học từ case ACS đã làm

Mỗi trường dùng Edusoft / web theo cách riêng (quy chế, cách tính học phí – điểm, trang ĐKMH riêng, phân cấp, bản VersionSchool).
**Case cũ của chính trường là nguồn tốt nhất để hiểu yêu cầu mới**: trường này hay hỏi gì, BA thường chốt ra sao, Dev hay sửa ở đâu, case nào là tiếp nối của case nào.

## Ghi chú `Case-truong/<mã 4 ký tự>.md`
- **Nhận xét – mô hình trường**: người test / Claude viết tay (công cụ không ghi đè).
- **Phần tự động** (giữa hai dấu `tu-dong`): tổng quan theo phân hệ (số case, quy trình, dạng hay gặp), theo **phân cấp**, dữ liệu hay đụng tới,
  chủ đề lặp lại, **case tiếp nối** (`[mã]` trong tiêu đề), danh sách case mới nhất (tiêu đề đã che email / SĐT / mã ≥ 7 số / tên sau SV, GV).
- Ghi chú `Truong/<mã>.md` có mục **Mô hình trường (từ case ACS)** tóm tắt + liên kết; app hiện "Trường hay có case…" ở bước 1 Test case ACS.

## Cập nhật thế nào
1. **App AQ Auto Test** → Test case ACS → Thiết lập ACS → thẻ *Kết nối Claude Desktop* → **Học case → KB** (đọc N case mới nhất trên ACS – chỉ đọc – rồi ghi cho mọi trường).
2. Hoặc hỏi **Claude Desktop**: "học case của trường KTTC" → công cụ `truong_hoc_case`; sau đó Claude đọc vài case tiêu biểu và viết phần *Nhận xét*.
3. Chạy `dong-bo.bat` để chia sẻ.

## Khi đọc một case mới
Mở `Case-truong/<trường>` trước: case cùng phân hệ / cùng dạng / cùng chủ đề gần đây → đọc lại cách BA chốt và kết luận test; case có `[mã]` → đọc case gốc.
Xem thêm [[00 Cách phân tích case]] (bước 0b) và [[00 Quy trình xuyên phân hệ]].

## Các trường đã có mô hình
![[Case truong.base]]

> [!warning] Dữ liệu cá nhân
> KB nằm trong git. Chỉ ghi tiêu đề đã che và nhận xét nghiệp vụ – **không** chép nội dung email, họ tên, MSSV, số điện thoại của SV / GV / KH.
