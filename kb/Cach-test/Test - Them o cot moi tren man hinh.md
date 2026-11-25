---
loai: cach-test
ten: "Test - Thêm ô / cột mới trên màn hình Edusoft"
ap_dung: case bổ sung ô nhập, combobox, cột trên lưới (thêm thông tin cần lưu riêng)
test_tren: edusoft
trang_thai: tu-nguoi-dung
tags: [cach-test, them-o, combobox, cot]
thu_tu: 1
dau_hieu: "bổ sung (thêm )?(thông tin|ô|trường|cột)|thêm (ô|trường|cột|field)|combobox"
buoc:
  - "Mở {Menu}, chọn 1 hồ sơ test (đã có {Ô cũ}) → kiểm có ô {Ô mới} (vị trí như dev ghi)."
  - "Bấm ô {Ô mới}: danh sách giá trị lấy từ {Danh mục} (so với menu danh mục đó)."
  - "Chọn {Ô mới} khác {Ô cũ} → Lưu → đóng màn hình, mở lại hồ sơ."
  - "Hồ sơ chưa nhập {Ô mới}: mở, sửa ô khác → Lưu – không báo lỗi, {Ô mới} vẫn trống."
  - "Trên lưới tìm cột của {Ô mới} (không thấy: chuột phải tiêu đề cột → Column Chooser → kéo cột vào → lưu giao diện) → Xuất Excel."
kiem_tra:
  - "{Ô mới} lưu đúng giá trị đã chọn; {Ô cũ} giữ nguyên – hai ô không ghi đè nhau."
  - "File Excel có cột của {Ô mới} đúng giá trị (cả 2 kiểu xuất: theo database / như trên màn hình)."
khong_anh_huong:
  - "Hồ sơ cũ (lưu trước bản sửa) mở lại vẫn giữ nguyên dữ liệu."
  - "Mọi đường ghi khác vào cùng cột (Import, Cập nhật theo file, Đồng bộ, màn hình nhập kết quả) không làm mất / tự điền {Ô mới} hoặc {Ô cũ}."
---
# Test – Thêm ô / cột mới trên màn hình Edusoft

Dùng cho case **bổ sung một thông tin cần lưu riêng** (ô nhập / combobox / cột trên lưới) – vd #64781 DHMOTX thêm
**Nơi cấp VB trước sáp nhập** cạnh **Nơi cấp VB** ở *Sinh viên › Thẩm tra văn bằng › Xem/sửa thẩm tra văn bằng*.

## Nguyên tắc
- Plan là **bước người test / bộ test làm**, không chép lại yêu cầu KH. Lấy từ *Chi tiết xử lý* (dev ghi "Nội dung: …"),
  *Trả lời KH* (mô tả chức năng sau khi sửa) và **các lần test trước báo lỗi** (mở lại case).
- Ô mới hay "dính" vào ô cũ cùng danh mục: kiểm **mọi đường ghi** – sửa tay, Import, Cập nhật theo file ([[Test - Import va cap nhat theo file Excel]]),
  Đồng bộ (tất cả / chưa có), màn hình nhập kết quả.
- Cột thêm sau **bị ẩn** khi lưới đã *Lưu giao diện* riêng → Column Chooser (không phải lỗi code, nhưng phải có trong trả lời KH).
- Case theo **phân cấp** (view riêng, vd DHMOTX): mở cùng menu ở trường gốc (DHMO) để chắc không lỗi.

## Chữ trong `buoc` / `kiem_tra`
`{Menu}`, `{Ô mới}`, `{Ô cũ}` (ô liên quan / cạnh ô mới), `{Danh mục}` – app thay bằng tên lấy từ ghi chú dev / trả lời KH.
