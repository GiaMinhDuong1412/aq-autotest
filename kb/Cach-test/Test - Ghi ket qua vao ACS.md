---
loai: cach-test
ten: "Test - Ghi kết quả vào ACS (CST)"
trang_thai: da-xac-nhan
nguon: nguoi-dung
tags: [cach-test, acs]
aliases:
  - "Ghi kết quả test vào ACS"
  - "Điền case CST"
---
# Ghi kết quả test vào ACS (CST)

> [!info] CST = tên cũ của ACS. Người dùng dạy 25/11 (case mẫu #64900). Chi tiết thao tác + cấu hình app: skill `ghi-ket-qua-acs`.

## Đạt
1. **Nội dung Tester test** (khối 4 Kiểm thử): ảnh + nội dung đã test + quy trình test → **Gửi**.
2. **Kết quả test = Đúng** → **Save**.
3. **Link merge** ở *Nội dung TechLead phân tích* (pullrequest TFS + bản build).
4. Người test **Complete** PR trên TFS → chụp ảnh → dán vào Nội dung Tester test → **Gửi**.

## Không đạt
**Kết quả test = Mở lại case** → **Phân công = tiepnhanadmin** → **Trạng thái = Mở Case** → **Save**; Nội dung Tester test ghi lỗi + ảnh → Gửi.
ACS tự: case về Đang xử lý, Số lần mở lại +1.

## Vì sao quan trọng
- Không có Tester + Kết quả test = Đúng thì không gửi được mail đóng case (bước 05).
- Link merge là bằng chứng bản sửa đã vào nhánh của trường (VersionSchool/<trường>) – xem [[00 Cách phân tích case]] phần Dev xử lý.

## Hay sai
- Kết luận Đạt khi kịch bản còn bước lỗi / bỏ qua → app chặn, phải xác nhận lại.
- Quên Save sau khi chọn Đúng (ACS hiện "Có thay đổi chưa lưu").
- Complete merge mà chưa gửi ảnh vào nội dung tester.
