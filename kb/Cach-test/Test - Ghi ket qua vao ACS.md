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

## Lời gọi ACS (app tự ghi)
- **API thật của ACS** (đọc từ mã giao diện ACS 25/11 – app dùng mặc định, không cần khảo sát / xác nhận):
  - Gửi nội dung test: `POST /cs/cases/{id}/comments` body `{"html": "<p>…</p>", "kenh": "test"}` (`kenh` mặc định `binh_luan` = Bình luận – phải là `test`).
    Thiếu `html` → ACS trả **422** (lỗi "trả về mã 422 – [object Object]" ngày 25/11 do app gửi trường `content`).
  - Ảnh: tải trước `POST /cs/attachments?name=<tên>` (body nhị phân, `Content-Type: application/octet-stream`) → `{id}` → chèn `<img src="/cs/att/<id>"/>`; app: `aqDesktop.acs.upload`.
  - Lưu case: `PATCH /cs/cases/{id}` body `{"rev": <rev từ GET>, "fields": {"test_state": "Đúng" | "Mở lại case", "assignee_raw": "AQ\\tiepnhanadmin"}, "state": "Mở Case", "reason": "<lý do>"}` –
    đổi Trạng thái bắt buộc `reason` lấy trong `transitions["Mở Case"]` của GET case (vd "Case chưa đạt, cần thực hiện lại"); sai `rev` (người khác vừa lưu) → đọc lại rồi gửi lại.

## Merge trong app (Mức 1)
- **Merge – Mức 1 (người dùng chốt 25/11)**: nút **Mở PR trong app** (bước 4, case Đạt) → app mở PR trong cửa sổ riêng (`desktop/src/tfs.js`, phiên `persist:tfs`,
  đăng nhập Windows tự động, máy chủ hỏi thì hiện hộp nhập – không lưu mật khẩu) → **người test tự bấm Complete** → app chỉ đọc trạng thái PR (GET API TFS cùng phiên, 3 giây/lần)
  → `completed` thì tự chụp cửa sổ → ảnh merge của phiếu → tự gửi "Đã Complete merge <link> (Completed bởi …, commit …)" + ảnh vào Nội dung Tester test. App **không** bấm Approve / Complete.

## Vì sao quan trọng
- Không có Tester + Kết quả test = Đúng thì không gửi được mail đóng case (bước 05).
- Link merge là bằng chứng bản sửa đã vào nhánh của trường (VersionSchool/<trường>) – xem [[00 Cách phân tích case]] phần Dev xử lý.

## Hay sai
- Kết luận Đạt khi kịch bản còn bước lỗi / bỏ qua → app chặn, phải xác nhận lại.
- Quên Save sau khi chọn Đúng (ACS hiện "Có thay đổi chưa lưu").
- Complete merge mà chưa gửi ảnh vào nội dung tester.
