# Nghiệp vụ QLSV – Quản lý sinh viên (rút từ tài liệu HDSD + lưu đồ, 16/11/2026)

Nguồn đã đọc (SharePoint, connector Microsoft 365):
- `ALL DOCS/1. Tài liệu Edusoft/QLSV/QLSV_CapNhatQuyetDinhVaoRa.pdf` (7 trang, 2014 – sơ sài, nhiều chỗ "tương tự").
- `5. Con rùa - TortoiseSVN/QuickGuide/PDF/QLSV/QLSV_QuanLyDanhSachSinhVienHocKy.pdf` (32 trang, 2016 – **đầy đủ nhất**).
- `ALL DOCS/1. Tài liệu Edusoft/QuiTrinhMotTrangViSio/QLSV.pdf` – lưu đồ (chỉ đọc được chữ trong ô, mất mũi tên;
  cần file `.vsdx` gốc để có quan hệ). `QLSV_CapNhatQuyetDinhVaoRa_LuuDo.pdf` là ảnh – không đọc được chữ.
Chưa đọc: Bảo hiểm SV, Lý lịch, Tốt nghiệp & in bằng, Cố vấn học tập, Khen thưởng KL, Ngành hai, Điểm rèn luyện, Đoàn thể,
Hồ sơ văn bằng, Thông tin khác, Trợ cấp/miễn giảm, Xét học bổng (thư mục `ALL DOCS/1. Tài liệu Edusoft/QLSV`).

## Vòng đời sinh viên (lưu đồ QLSV)
```
DS trúng tuyển ─┐
Chuyển trường ──┴─► QĐ vào mới ──► DS SV học kỳ ◄── QĐ học lại (sau tạm dừng / nghỉ hết hiệu lực)
                                     │
                                     ├─ QĐ đổi lớp      (chuyển lớp / chuyển ngành – chọn "Mã lớp mới", ô đỏ)
                                     ├─ QĐ tạm dừng     (bảo lưu, tạm nghỉ – nhập thêm SỐ HỌC KỲ tạm dừng)
                                     ├─ QĐ nghỉ học     (thôi học, rút hồ sơ, buộc thôi học → xóa khỏi DS SV học kỳ)
                                     └─ QĐ tốt nghiệp   (sau xét tốt nghiệp → xóa khỏi DS SV học kỳ các học kỳ sau)
```
- **Danh mục sinh viên** = toàn bộ SV trường quản lý, *không theo học kỳ*. **DS SV học kỳ** = SV có hiệu lực trong học kỳ
  (đang học, có QĐ tạm dừng / nghỉ / tốt nghiệp trong học kỳ). SV chỉ vào DS SV học kỳ qua **quyết định** (vào mới / học lại).
- Mọi QĐ vào/ra: Menu `Sinh viên/ Sinh viên học kỳ/ QĐ vào/ra sinh viên/ Quyết định <loại>`; cùng khuôn:
  Thêm → nhập thông tin QĐ (Số QĐ, Lý do, Ngày lập, Ngày hiệu lực, Người ký…) → Thêm SV vào lưới hoặc Import → Lưu.
  Loại QĐ phân biệt bằng **lý do** (danh mục lý do có cột loại: vào mới / ra / …) – chọn lý do đúng loại.
- QĐ phải nhập **đúng học kỳ** (học kỳ vào của SV) – kịch bản chọn năm học/học kỳ test trước.

## Danh mục phải có trước (điều kiện đầu vào)
| Danh mục | Menu |
|---|---|
| Khối lớp | Kế hoạch/ Quản trị phân hệ/ Quản lý danh mục/ Danh mục khối lớp |
| Lớp | Sinh viên/ Quản trị phân hệ/ Quản lý danh mục/ Danh mục lớp |
| Lý do quyết định | Sinh viên/ Sinh viên học kỳ/ QĐ vào/ra sinh viên/ Danh mục lý do quyết định |
| Tên quyết định | Sinh viên/ Sinh viên học kỳ/ QĐ vào/ra sinh viên/ Danh mục tên quyết định |
| Người ký quyết định | Sinh viên/ Sinh viên học kỳ/ QĐ vào/ra sinh viên/ Danh sách người ký quyết định |
Kịch bản chỉ **đọc** các danh mục này (`pick:`), không thêm – trừ khi kịch bản test chính danh mục đó.

## Quyết định vào mới (QLSV-001)
Hai cách đưa SV mới vào:
1. **Từng SV** – (a) Danh mục sinh viên → Thêm: nhập SV *tạm* (ô có * đỏ là bắt buộc; Mã lớp, Số QĐ, Lý do QĐ **để trống**,
   sẽ được điền khi lập QĐ). (b) Quyết định vào mới → Thêm → nhập thông tin QĐ → "Thêm" SV vừa nhập vào lưới → Lưu.
   Màn hình QĐ vào mới cũng có "Thêm mới 1 SV" (mở "Chi tiết lý lịch sinh viên") – gộp (a) vào (b) – QLSV-001 dùng cách này.
2. **Theo file** (luồng thay thế) – Thêm QĐ → nhập thông tin QĐ → Import file DBF/Excel, cột bắt buộc:
   `MaSV, HolotSV, TenSV, Phai (1 Nam / 0 Nữ), NoiSinh, NgaySinhC (chuỗi dd/mm/yyyy, thiếu ngày/tháng thì để trống), MaLopMoi`
   → làm theo các bước kiểm tra của tool import → chờ "lưu thành công".
- **Kiểm tra kết quả**: SV có trong DS SV học kỳ của học kỳ đó; xem nhanh QĐ của SV: chọn SV → "Xem QĐ vào – ra sinh viên".
  Báo cáo đối chiếu: `Sinh viên/ Sinh viên học kỳ/ In kiểm tra sinh viên/ Có trong danh sách & không có q/định`.

## Xóa / dọn dữ liệu test (ảnh hưởng bước xóa của QLSV-001)
- Xóa SV khỏi **Danh mục sinh viên**: chương trình *truy vấn toàn bộ dữ liệu liên quan* rồi hỏi xác nhận → SV còn nằm trong QĐ /
  DS SV học kỳ thì phải gỡ các chỗ đó trước (thứ tự dọn: SV khỏi QĐ → QĐ → SV khỏi danh mục).
- **Hủy SV trong DSSV học kỳ** (khi chưa có QĐ ra): `Sinh viên/ Danh sách sinh viên/ Hủy sinh viên trong DSSV học kỳ` –
  chọn SV → Hủy → kiểm tra dữ liệu liên quan → xác nhận.
- QLSV-001 (03/11, bộ test 2026.11.03-9) dừng ở bước 12: Xóa QĐ → Thực hiện → Có nhưng **không** báo "Xóa dữ liệu thành công".
  Giả thuyết theo tài liệu: QĐ đang chứa SV (đã sinh dữ liệu DS SV học kỳ) → cần gỡ SV khỏi lưới QĐ (Lưu) rồi mới xóa QĐ;
  sau đó xóa SV `TEST…` khỏi Danh mục sinh viên (hiện kịch bản **chưa dọn SV tạm** – để lại rác).
  Bằng chứng (`ui-buoc-12-loi.txt`, asset e3745dbe… trên artifact): sau khi Xóa → Có, QĐ `TEST_QD_030209` vẫn trong lưới và
  lưới "Danh sách sinh viên" của QĐ vẫn còn `TEST030209` (Mã lớp mới HKH49B1); không có hộp thoại lỗi.
  Danh mục màn hình (S15.04, lớp `Edusoft.SMS.S02.UCQDSV`): lưới SV của QĐ có nút riêng **"Xóa sinh viên"** (btnDelete),
  danh sách QĐ có **"Xóa quyết định"** (btnDelete) / **"Lưu quyết định"** (btnSave) – khác nút "Xóa" chung trên thanh dưới.
  Đề xuất luồng dọn: Sửa QĐ → chọn SV TEST… → "Xóa sinh viên" → Lưu → Xóa QĐ → mở Danh mục sinh viên xóa SV TEST…
  (chưa chạy thử – xác nhận bằng lần chạy tới).

## Danh mục sinh viên – chức năng trên màn hình
In · In lý lịch SV (tick SV) · Import / Cập nhật từ file (excel, dbf, clipboard) · Xem khen thưởng – KL · Export (tick dòng
nào xuất dòng đó, không tick = tất cả) · Cập nhật lý lịch · Thêm (SV tạm, detail bên phải, * đỏ bắt buộc) · Thêm chi tiết SV ·
Sửa (chỉ Họ lót, Tên, Ngày sinh, Phái, Nơi sinh, Điện thoại) · Xóa · Xem QĐ vào – ra sinh viên.
DS SV học kỳ có: In, In lý lịch, Export, Cập nhật lý lịch, Xem QĐ vào – ra.

## In / thống kê / kiểm tra (chỉ xem – kịch bản "in" chọn điều kiện → In → có kết quả trên màn hình)
- In danh sách SV: Theo lớp · Làm bằng tốt nghiệp · Quản lý đầu ra · Theo hộ khẩu · NVQS theo hộ khẩu.
- In thống kê SV: Theo bậc hệ đào tạo · Theo năm sinh · Theo hộ khẩu · Theo tình trạng sinh viên.
- In kiểm tra SV: So với học kỳ trước · Có trong danh sách & không có q/định.
