---
name: ghi-ket-qua-acs
description: Quy trình điền kết quả test vào case ACS (tên cũ CST) sau khi test – Đạt (Nội dung Tester test → Gửi, Kết quả test = Đúng → Save, link merge, Complete PR rồi gửi ảnh) và Không đạt (Mở lại case → tiepnhanadmin → Mở Case → Save). Dùng khi soạn / kiểm nội dung test, sửa luồng ghi ACS của trang Test case ACS, hoặc hướng dẫn người test điền case.
---

# Ghi kết quả test vào case ACS (CST)

> CST là tên cũ của ACS (người dùng quen gọi). Màn hình case: `KB4CS / CS Case / Work items / #<mã>` – khối **4 Kiểm thử** (Tester, Kết quả test, Số lần mở lại, Hashtag, **Nội dung Tester test**).
> Người dùng dạy ngày 25/11 (case mẫu #64900). Ghi chú KB: `kb/Cach-test/Test - Ghi ket qua vao ACS.md`.

## Case ĐẠT – 4 bước
1. **Nội dung Tester test**: ô soạn thảo dưới khối Kiểm thử → điền **hình ảnh + nội dung đã test + quy trình test** → bấm **Gửi** (Ctrl+Enter). Mỗi lần Gửi là một mục nội dung riêng.
2. **Kết quả test = Đúng** (danh sách: Trống / Đúng / Mở lại case) → bấm **Save** (góc trên phải; có dấu "Có thay đổi chưa lưu" khi chưa Save).
3. **Link merge**: nằm ở **Nội dung TechLead phân tích** (tab Xử lý case, phần Dev / TechLead) – dạng `https://portal.aqtech.vn:1443/tfs/AQ/Source.NET/_git/Source.NET/pullrequest/<số>` kèm bản build (vd 2026.11K.42).
4. Mở link → trên Azure DevOps bấm **Complete** (người test tự bấm) → chụp màn hình PR đã Complete → dán vào **Nội dung Tester test** → **Gửi**.

## Case KHÔNG ĐẠT
1. **Kết quả test = Mở lại case** (ACS: case về Đang xử lý, phân công về hàng đợi tiepnhanadmin, Số lần mở lại +1).
2. **Phân công = tiepnhanadmin**.
3. **Trạng thái = Mở Case** → **Save**.
4. Nội dung Tester test: ảnh + bước lỗi + kết quả thực tế → Gửi (để coder biết lỗi gì).

## Ràng buộc trên ACS
- Case cần kiểm thử phải có **Tester** và **Kết quả test = Đúng** mới gửi được mail (tab Gửi mail, bước 05 Gửi email & Đóng).
- Tester có thể để trống khi lưu; case CV chưa gán Tester được miễn kiểm thử.

## Nội dung tester – mẫu (app tự soạn ở bước 4, `rtDraft2`)
```
[AQ Auto Test] Test lại lần <n> – ĐẠT
Nền tảng: <Edusoft/Web> · Bản: <build> · Trường <mã>
Môi trường: <exe / URL test>
Quy trình test:
1. <bước chuẩn bị / thao tác>
Kết quả kiểm tra:
- [Đạt] <đầu ra cần đạt> → <ghi chú>
Link merge: <url pullrequest>
Người test: <tên> · <giờ>
```
Kèm ảnh chụp từng bước. **Đạt mà còn mục lỗi / bước kịch bản chưa đạt** (vd "1/2 bước đạt") → xem lại, không ghi Đạt cho qua.

## Trong app AQ Auto Test (trang Test case ACS, bước 4 Kết luận)
- Danh sách "Điền vào ACS" theo 4 bước / 3 bước ở trên, tick khi xong.
- Ghi tự động chỉ khi quản trị đã **xác nhận** ở tab Thiết lập ACS (`settings/acs.write`):
  `n` = lời gọi **Gửi** nội dung tester (method, path `{id}`, trường, HTML, nhúng ảnh), `method/path/f` = lời gọi **Save** (`f.state` = trường Kết quả test, `f.assignee`, `f.status`; `full` = Save gửi cả case → app GET rồi ghép), `v` = Đúng / Mở lại case / Mở Case / tiepnhanadmin.
- **API thật của ACS** (đọc từ mã giao diện ACS 25/11 – app dùng mặc định, không cần khảo sát / xác nhận):
  - Gửi nội dung test: `POST /cs/cases/{id}/comments` body `{"html": "<p>…</p>", "kenh": "test"}` (`kenh` mặc định `binh_luan` = Bình luận – phải là `test`).
    Thiếu `html` → ACS trả **422** (lỗi "trả về mã 422 – [object Object]" ngày 25/11 do app gửi trường `content`).
  - Ảnh: tải trước `POST /cs/attachments?name=<tên>` (body nhị phân, `Content-Type: application/octet-stream`) → `{id}` → chèn `<img src="/cs/att/<id>"/>`; app: `aqDesktop.acs.upload`.
  - Lưu case: `PATCH /cs/cases/{id}` body `{"rev": <rev từ GET>, "fields": {"test_state": "Đúng" | "Mở lại case", "assignee_raw": "AQ\\tiepnhanadmin"}, "state": "Mở Case", "reason": "<lý do>"}` –
    đổi Trạng thái bắt buộc `reason` lấy trong `transitions["Mở Case"]` của GET case (vd "Case chưa đạt, cần thực hiện lại"); sai `rev` (người khác vừa lưu) → đọc lại rồi gửi lại.
- Lấy cấu hình bằng **Khảo sát ACS**: app cho mã `AQTEST-xxxxx` → người dùng dán mã vào Nội dung Tester test → Gửi → Kết quả test = Đúng → Save → Dừng; app nhận lời gọi chứa mã = Gửi, lời gọi lưu case = Save (`rtSuggest`).
- Chưa xác nhận: app chép nội dung + mở case để dán tay.
- Bước merge: app chỉ hiện / mở **link merge** và nhận ảnh (Ctrl+V) rồi gửi vào nội dung tester. **Không** bấm Approve / Complete hay gọi API ghi trên TFS (TFS chỉ đọc với Claude / app).

## Không làm
- Không ghi lên ACS từ MCP / Claude Desktop (MCP chỉ đọc ACS).
- Không tự Complete PR trên TFS; không đổi trạng thái case khác những trường ở trên.
- Không ghi mật khẩu / token vào nội dung test.
