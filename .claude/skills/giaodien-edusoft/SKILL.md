---
name: "giaodien-edusoft"
description: "Nhận diện giao diện Edusoft.NET (HVNG): phân biệt phân hệ, menu, chức năng, ô tìm kiếm, button, lưới dữ liệu, popup, thanh học kỳ… theo cách người dùng dạy; dùng khi viết/sửa lệnh `auto` của kịch bản, đọc file ui-*.txt hay ảnh chụp màn hình Edusoft, hoặc khi người dùng dạy thêm về giao diện. Kiểu màn hình và thao tác theo tài liệu HDSD từng phân hệ ở thao-tac.md."
---

# Giao diện Edusoft – cách nhận diện phần tử

Skill này là **sổ tay do người dùng dạy**. Mọi điều người dùng chỉ về màn hình Edusoft được ghi vào đây và
**bắt buộc áp dụng** cho các lần sau (viết `auto` trong kịch bản, sửa `kit/aqrun.py`, đọc `ui-*.txt`, xem ảnh chụp).

Thứ tự ưu tiên khi có mâu thuẫn: **Bài học người dùng dạy (mục 4)** > bảng phần tử (mục 2) > suy đoán từ tài liệu.
Ảnh minh hoạ người dùng gửi nằm ở `anh/` cạnh file này – mở bằng Read khi cần so lại.

**Danh mục màn hình gốc** (`man-hinh/index.md`, mỗi phân hệ một file `man-hinh/<MaPhanHe>.md`, vd `QLSV.md` = ribbon "Sinh viên"):
đường dẫn menu đúng chữ trên ribbon/cây (viết thẳng vào `menu:`), lớp màn hình, các lưới (cột = nhãn [MaField], cột ẩn,
nút tắt Thêm/Sửa/Xóa…), ô trên form sửa (`#MaField` cho `type:`/`choose:`/`date:`), nút riêng (tooltip, phím tắt).
Tra bằng Grep theo tên menu/màn hình **trước khi viết `auto`**. Đây là cấu hình gốc AQ – HVNG có thể ẩn/đổi nhãn bằng bảng
`H…`; khi lệch với `ui-*.txt` thì tin `ui-*.txt` và ghi bài học.
**Nguyên tắc (người dùng dạy 2026-11-04):** Edusoft dùng chung cho **nhiều trường**; HVNG chỉ có một số code/cấu hình riêng.
Kịch bản và lệnh `auto` đi theo **hướng chung** (danh mục gốc AQ). Phần hiệu chỉnh riêng của từng trường phải đọc **case trên
ACS** để hiểu (lý do, phạm vi) – không tự suy từ chỗ lệch; khi gặp màn hình HVNG khác danh mục thì ghi lại và hỏi/tra case ACS.

## 1. Bố cục cửa sổ chính (người dùng dạy – tài liệu "Giao diện Edusoft", ảnh `anh/01-giao-dien-chinh.png`)

```
┌ Thanh tiêu đề: nút nhanh · Server Time · "EduSoft.NET [v2026.10L.00-HVNG] (2026-10-30 08:25)" ┐
├ PHÂN HỆ (thẻ ribbon): Hệ thống · Nhân sự · Kế hoạch · … · Hoạt động cộng đồng              ┤
├ MENU (nút lớn có icon trong thẻ, gom theo nhóm, vd nhóm "Quản lý hệ thống")                 ┤
├──────────────┬────────────────────────────────────────────────────────────────────────────┤
│ Danh mục     │ MÀN HÌNH CHỨC NĂNG (tab, có nút X)                                          │
│ chức năng    │   tab con "Dạng chi tiết" / "Dạng danh sách"                                │
│ (CHỨC NĂNG)  │   tiêu đề lưới · tiêu đề cột · DÒNG TÌM KIẾM (phễu) · các dòng dữ liệu      │
│              │   thanh điều hướng "Record 6 of 1766"                                        │
│──────────────│   (lưới chi tiết bên dưới, nếu có)                                           │
│ Thông tin    │   BUTTON ở đáy màn hình: Sửa(F2) · Thêm nhóm(F3) · … · Lưu(Ctrl+S) · Đóng   │
│ đơn vị       │                                                                              │
│──────────────│                                                                              │
│ HỌC KỲ: Năm  │                                                                              │
│ học · Học kỳ │                                                                              │
├──────────────┴────────────────────────────────────────────────────────────────────────────┤
└ Thanh trạng thái (phải): user đăng nhập "Quản trị Đại học (DH)" · Đăng xuất                 ┘
```

## 2. Bảng phần tử

Trạng thái: **✔ người dùng xác nhận** · **? suy đoán, chờ dạy**. Cột "Loại UIA" là suy đoán cho tới khi đối chiếu `ui-*.txt`.

| Phần tử | Trạng thái | Nhận biết | Loại UIA (dự kiến) | Lệnh `auto` |
|---|---|---|---|---|
| **Phân hệ** | ✔ #1 | Thẻ chữ trên cùng (Hệ thống, Nhân sự, Kế hoạch, Khối lượng, Tuyển sinh, Sinh viên, Ký túc xá, Đăng ký MH, Tổ chức thi, Chính sách HP, Thu/chi HP, Quản lý điểm, Quản lý nhập điểm, Tốt nghiệp, Đánh giá, NC khoa học, Khảo sát đánh giá, Quản lý lưu học sinh, Hoạt động cộng đồng) | `TabItem` | cấp 1 của `menu:` |
| **Menu** | ✔ #2 | Nút lớn có icon + chữ 2 dòng trong thẻ phân hệ; nút **mờ** = chưa dùng được | `Button` | cấp 2 của `menu:` |
| **Chức năng** | ✔ #3 | Mục trên cây "Danh mục chức năng" bên trái; dòng in đậm có nền = nhóm/đang chọn, mục con có đường kẻ, nhóm có dấu ⊟/⊞ | `TreeItem` (chữ ở Value) | cấp cuối của `menu:` (bấm đúp) |
| **Màn hình chức năng** | ✔ #4 | Tab ở vùng giữa, tiêu đề = tên chức năng, có nút X | tab MDI | – |
| **Ô tìm kiếm (search bar)** | ✔ #5 | **Dòng trống ngay dưới tiêu đề cột**, đầu dòng có **icon phễu**; mỗi cột một ô | ô của lưới (dòng lọc DevExpress) | `find_row: giá trị @ Cột`, `unique: BIẾN @ Cột`, `absent: giá trị @ Cột`, `delete_row: giá trị @ Cột` |
| **Button** | ✔ #6 | Dãy nút **ở đáy** màn hình chức năng, có icon nhỏ, nhiều nút kèm **phím tắt trong ngoặc**; mỗi menu một bộ khác nhau | `Button` | `click:` / `save:` / `key:` |
| **Lưới dữ liệu** | ✔ #7 | Bảng chính; **cột màu xám = sửa được**, **cột trắng = dữ liệu cứng** (chỉ đổi qua menu khác) | `Table`/`DataGrid`, ô `DataItem` | `find_row:`, `expect:`, `pick:` |
| **Popup** | ✔ #8 | Cửa sổ con "EduSoft.NET" mở khi bấm một số button; có tiêu đề nhóm, ô nhập, lưới con, nút **Lưu / Đóng** ở đáy | `Window` | `type:`/`select:` rồi `save:` |
| **Thanh học kỳ** | ✔ #9 | **Dưới cùng bên trái, dưới Thông tin đơn vị**: ô chọn "Năm học" (vd 2026-2027), "Học kỳ" (vd 1) và "ĐVPC: Đại học" | `Button` "Năm học" / "Học kỳ" trong `StatusBar` (đã thấy trong ui-*.txt) | – (không đổi khi test, trừ khi kịch bản yêu cầu) |
| **Thông tin đơn vị** | ✔ #10 | Khung dưới cây chức năng: logo + tên trường (vd DEMO HVNG) | – | dùng xác nhận đúng môi trường |
| **User / Đăng xuất** | ✔ #11 | Góc phải thanh trạng thái: tên user đăng nhập + nút Đăng xuất | `Button` | **không bấm Đăng xuất** khi đang test |
| **Phiên bản** | ✔ #12 | Thanh tiêu đề: `EduSoft.NET [v<phiên bản>-<môi trường>] (<ngày build>)` | tiêu đề cửa sổ | ghi vào kết quả lượt chạy |
| Ô nhập trong popup (text) | ? | ô trắng cạnh nhãn "Xxx:" bên trái | `Edit` (TextEdit) | `type:` |
| Ô chọn trong popup | ? | ô có mũi tên ▾ (vd Môn học) | `ComboBox` / LookUpEdit | `select:` |
| Ô chọn có nút "…" | ? | ô có nút … (vd Tính chất phòng, Phòng dự kiến) – mở hộp chọn | `Edit` + `Button` | – (chờ dạy) |
| Checkbox | ? | ô vuông cạnh chữ (vd Nhóm học lại, Khóa) | `CheckBox` | – |
| Ô ngày | ? | – | `Edit` (DateEdit) | `date:` |
| Tab con của màn hình | ? | "Dạng chi tiết" / "Dạng danh sách" | `TabItem` | `click:` |
| Thanh điều hướng lưới | ? | ⏮ ◀ "Record x of y" ▶ ⏭ dưới lưới – cho biết tổng số dòng | – | – |

## 3. Đọc `ui-*.txt` (cây UI Automation bộ test ghi khi dừng)

Mỗi cửa sổ bắt đầu bằng `=== CỬA SỔ: <tiêu đề> [<lớp>] <toạ độ>`, sau đó mỗi dòng một phần tử:

```
loại | tên (window_text) | automationId | lớp | toạ độ (L,T,R,B) | giá trị (Value)
```

- Tên trống mà có Value → bộ test vẫn tìm theo Value (cây chức năng, ô lưới).
- Lớp DevExpress (vd `TextEdit`, `LookUpEdit`, `DateEdit`, `GridControl`, `SimpleButton`) giúp phân biệt loại
  khi `loại` chung chung (`Pane`, `Custom`). Ghi lớp đã thấy vào mục 2/4.
- Vị trí giúp nhận vùng: button nằm sát đáy màn hình chức năng; dòng tìm kiếm ngay dưới tiêu đề cột; popup là cửa sổ riêng.
- Mật khẩu luôn hiện `***` – không cố đọc.

## 4. Bài học người dùng dạy

> Ghi mỗi bài học theo mẫu dưới, mới nhất ở cuối. Không xóa bài cũ; nếu bị thay thế thì ghi "thay bằng #n".

```
### #n – <phần tử / màn hình> (ngày yyyy-mm-dd)
- Nhận biết: <hình dạng, vị trí, chữ/icon, loại UIA, lớp DevExpress, automationId nếu có>
- Phân biệt với: <phần tử dễ nhầm và khác ở điểm nào>
- Thao tác đúng: <bấm / bấm đúp / gõ / Enter / phím tắt…>
- Lệnh auto: <ví dụ dòng auto>
- Áp dụng: <kịch bản / code đã sửa theo bài này>
```

Nguồn #1–#12: tài liệu "Giao diện Edusoft" (docx) người dùng gửi ngày 2026-10-30, ảnh trong `anh/`.

### #1 – Phân hệ (2026-10-30)
- Nhận biết: dãy thẻ chữ trên cùng, ngay dưới thanh tiêu đề; thẻ đang chọn nổi trắng. Mỗi thẻ = một phân hệ Edusoft. Ảnh `anh/02-phan-he.png`.
- Phân biệt với: Menu (nút có icon bên dưới) – phân hệ chỉ có chữ.
- Thao tác đúng: bấm chọn thẻ (TabItem → `select()`).
- Lệnh auto: `menu: Sinh viên/ …` – đoạn đầu là phân hệ.
- Áp dụng: khớp cách `Edusoft.open_menu` đang làm.

### #2 – Menu (2026-10-30)
- Nhận biết: nút lớn có icon, chữ 1–2 dòng, nằm trong thẻ phân hệ, gom theo nhóm (tên nhóm nhỏ ở dưới, vd "Quản lý hệ thống", "Quản lý kế hoạch giảng dạy"). Ảnh `anh/03-menu.png`.
- Phân biệt với: Button của màn hình chức năng (nằm ở đáy màn hình, icon nhỏ, có phím tắt). Nút menu **mờ** (vd "Thông tin học kỳ", "Thông tin nhóm học phần") là không bấm được.
- Thao tác đúng: bấm một lần → cây "Danh mục chức năng" bên trái đổi theo menu.
- Lệnh auto: `menu: Kế hoạch/ Qui hoạch nhóm học phần/ …` – đoạn thứ hai là menu. Chữ trên nút bị xuống dòng, khi tìm phải ghép lại thành một dòng.
- Áp dụng: `open_menu` cấp 2.

### #3 – Chức năng (2026-10-30)
- Nhận biết: mục trên cây "Danh mục chức năng" (khung trái). Dòng tiêu đề in đậm (vd "Thông tin học kỳ") là nhóm; mục đang chọn tô nền vàng, in đậm; nhóm con có ⊟/⊞ (vd "Cập nhật nhóm tổ từ file"). Ảnh `anh/04-chuc-nang.png`.
- Phân biệt với: Menu – chức năng thuộc **từng menu**, chỉ hiện sau khi bấm menu.
- Thao tác đúng: nhóm → mở ra; mục cuối → bấm đúp, màn hình mở thành tab ở giữa.
- Lệnh auto: đoạn cuối của `menu:`.
- Áp dụng: `open_menu` + `expand_node`.

### #4 – Màn hình chức năng (2026-10-30)
- Nhận biết: tab ở vùng giữa, tên tab = tên chức năng (vd "Danh sách nhóm tổ") kèm nút X; bên trong có thể có tab con "Dạng chi tiết"/"Dạng danh sách", lưới chính, lưới chi tiết phía dưới (vd "Thời khóa biểu môn: …"), thanh button ở đáy. Ảnh `anh/05-man-hinh-chuc-nang.png`.
- Thao tác đúng: mở nhiều chức năng sẽ thành nhiều tab – tìm phần tử trong tab đang chọn.

### #5 – Ô tìm kiếm / search bar (2026-10-30)
- Nhận biết: **dòng trống ngay dưới hàng tiêu đề cột của lưới**, ô đầu dòng có **icon phễu** (▽). Mỗi cột có ô riêng – gõ vào ô của cột nào thì lọc theo cột đó. Ảnh `anh/06-o-tim-kiem.png` (khung đỏ).
- Phân biệt với: dòng dữ liệu (có giá trị), ô nhập của popup. Không phải ô tìm Ctrl+F nổi phía trên lưới.
- Thao tác đúng: bấm vào ô của cột cần lọc (vd cột "Mã MH") → gõ giá trị → lưới chỉ còn dòng khớp; xóa chữ trong ô để bỏ lọc.
- Lệnh auto: luôn ghi cột sau `@`: `find_row: {SOQD} @ Số quyết định|Số QĐ`, `unique: MSSV @ Mã sinh viên|Mã SV`,
  `absent: {MSSV} @ Mã sinh viên`, `delete_row: {SOQD} @ Số quyết định`. Không ghi cột: `find_row` chỉ xem các dòng đang hiện, `unique`/`absent` báo lỗi thiếu cột.
  **Không dùng Ctrl+F / Esc** (xem #13).
- Áp dụng (người dùng đồng ý 2026-10-30, kit `2026.10.30-13`): `Run.column_header` tìm tiêu đề cột trong lưới (lưới trên cùng),
  `Run.filter_grid` bấm **ngay dưới** tiêu đề (không bấm vào tiêu đề – sẽ sắp xếp cột), End + Backspace, gõ, Enter;
  `locate_row` chỉ nhận ô nằm dưới dòng lọc; `row_exists`/`delete_row` xoá chữ trong ô lọc sau khi xong; lọc cột khác thì
  xoá ô lọc cũ trước. QLSV-001 đã ghi cột cho mọi lệnh tìm. Toạ độ dòng lọc là ước lượng (đáy tiêu đề + nửa chiều cao) –
  chạy thật mà bấm lệch thì đọc `ui-*.txt` để chỉnh.

### #6 – Button (2026-10-30)
- Nhận biết: thanh nút **ở đáy màn hình chức năng**, icon nhỏ + chữ, nhiều nút có phím tắt trong ngoặc. Mỗi menu có bộ nút khác nhau. Ví dụ màn hình "Danh sách nhóm tổ": Sửa(F2), Thêm nhóm(F3), Thêm tổ TH(F4), Thêm tổ hợp(F5), Chuyển tổ hợp thành tổ TH(F10), Import, Xuất danh sách, Đồng bộ SS TKB(F6), Refresh SS ĐK(F7), Xóa(Ctrl+T), Refresh, Sửa SS TKB(F8), Lưu(Ctrl+S), Đóng. Ảnh `anh/07-button.png`.
- Phân biệt với: Menu (trên ribbon, icon lớn).
- Thao tác đúng: bấm nút, hoặc dùng phím tắt ghi trong ngoặc khi bấm không ăn. Tên nút gồm cả phần "(F3)" → tìm theo phần chữ trước ngoặc.
- Lệnh auto: `click: Thêm nhóm` (hoặc `key: {F3}`); `save:` = Lưu(Ctrl+S); xóa ở màn hình này là Xóa(**Ctrl+T**), không phải phím Delete.
- Áp dụng: `find_any` so khớp tên đầy đủ hoặc tiền tố ≥3 ký tự nên "Thêm nhóm" khớp được "Thêm nhóm(F3)" – cần đối chiếu khi chạy thật.

### #7 – Lưới dữ liệu: cột xám / cột trắng (2026-10-30)
- Nhận biết: bảng dữ liệu chính, có ô chọn (checkbox) đầu dòng, dòng đang chọn tô xanh. **Cột màu xám = sửa được ngay trên lưới; cột màu trắng = dữ liệu cứng, đã có sẵn, chỉ thay đổi qua một số menu khác.** Ảnh `anh/08-luoi-du-lieu.png`.
- Thao tác đúng: chỉ gõ sửa vào cột xám; cột trắng chỉ đọc để kiểm tra.
- Lệnh auto: kịch bản sửa không được nhắm vào cột trắng – nếu cần đổi giá trị cột trắng thì tìm menu tương ứng (hỏi người dùng).

### #8 – Popup (2026-10-30)
- Nhận biết: một số button khi bấm mở cửa sổ con tiêu đề "EduSoft.NET", bên trong có tiêu đề nhóm (vd "Thông tin tổ hợp"), ô nhập/ô chọn/checkbox, lưới con, nút **Lưu** và **Đóng** ở đáy popup. "Các tài nguyên cũng tương tự". Ví dụ: Thêm nhóm(F3) → popup "Thông tin tổ hợp". Ảnh `anh/09-popup.png`.
- Thao tác đúng: nhập trong popup rồi bấm Lưu của **popup** (không phải Lưu của màn hình phía sau); Đóng để thoát.
- Lệnh auto: `click: Thêm nhóm` → `type:`/`select:` các ô của popup → `save:`. Bộ test tìm hộp thoại trước cửa sổ chính (`Edusoft.roots`) nên đúng thứ tự.

### #9 – Thanh học kỳ đang dùng (2026-10-30)
- Nhận biết: "Năm học [2026-2027 ▾]  Học kỳ [1 ▾]  ĐVPC: Đại học", nằm **dưới cùng phía bên trái, dưới khung Thông tin đơn vị**
  (người dùng bổ sung). Ảnh `anh/10-hoc-ky.png`.
- Thao tác đúng: dữ liệu các màn hình phụ thuộc học kỳ đang chọn. Không đổi khi test trừ khi kịch bản yêu cầu; ghi năm học/học kỳ vào kết quả để đối chiếu.

### #10 – Thông tin trường (2026-10-30)
- Nhận biết: khung "Thông tin đơn vị" dưới cây chức năng: logo + tên trường (vd **DEMO HVNG**). Ảnh `anh/11-thong-tin-truong.png`.
- Thao tác đúng: dùng xác nhận đang ở đúng môi trường test (HVNG) trước khi thao tác dữ liệu.

### #11 – User đăng nhập và Đăng xuất (2026-10-30)
- Nhận biết: góc phải thanh trạng thái dưới cùng: icon người + tên user (vd "Quản trị Đại học (DH)") và nút "Đăng xuất". Ảnh `anh/12-user-dang-xuat.png`.
- Thao tác đúng: không bấm Đăng xuất trong lúc chạy kịch bản (trừ kịch bản đăng nhập/đăng xuất).

### #12 – Thông tin phiên bản (2026-10-30)
- Nhận biết: giữa thanh tiêu đề: `EduSoft.NET [v2026.10L.00-HVNG] (2026-10-30 08:25)` = phiên bản – môi trường (ngày build). Ảnh `anh/13-phien-ban.png`.
- Thao tác đúng: đọc từ tiêu đề cửa sổ chính để ghi phiên bản vào lượt chạy / đối chiếu release.

### #13 – Phím Esc và cấu trúc UIA thật (rút ra từ lượt chạy QLSV-001 ngày 2026-10-31 01:12, kit -11)
- Hiện tượng: kit cũ tìm bằng Ctrl+F rồi Esc → báo nhầm "mã đã có" (ô tìm Ctrl+F nằm trong lưới, chứa đúng chữ vừa gõ),
  **Esc đóng màn hình chức năng**, Esc ở cửa sổ chính bật hộp **"Thoát khỏi chương trình?" (Có / Không)**; bước sau không còn
  lưới nên "0 dòng đang hiện"; người test bấm Dừng nhưng kết quả vẫn ghi "Đạt".
- Thao tác đúng: **không gửi Esc** để bỏ tìm kiếm/đóng gì trên màn hình chính; tìm bằng ô tìm kiếm của cột (#5) rồi xoá chữ.
  Gặp hộp "Thoát khỏi chương trình?" thì bấm **Không** (`Edusoft.keep_open`, chạy đầu mỗi bước và khi bước lỗi).
- Cấu trúc UIA đã thấy (`ui-buoc-3-loi.txt`): cây chức năng `Tree` automationId `treeChucNangC3`, có `Header` (tên menu) và
  cặp `TreeItem NodeN` + `DataItem "<cột> row N"` (chữ ở Value); vùng màn hình chức năng `Tab tabForm` → `Pane` lớp
  `MDICLIENT`; ribbon `Pane "Sinh viên"` → `ToolBar "Quản lý sinh viên"` → các `Button`; thanh dưới `StatusBar`: `Button "Năm học"`,
  `Button "Học kỳ"`, Text "ĐVPC:  Đại học", Text tên user, `Button "Đăng xuất"`; khung trường `Text lblTenTruong` ("DEMO HVNG").
  Lưới DevExpress dự kiến cùng kiểu: tiêu đề cột là `Header`, ô là `DataItem "<cột> row N"` – kit -13 gom ô theo hàng như vậy.
- Áp dụng: kit `2026.10.30-13` – bỏ Ctrl+F/Esc khi tìm, `keep_open`, kết quả chỉ "Đạt" khi mọi bước luồng chính đạt
  (dừng giữa chừng → "Bị chặn", ghi "Dừng ở bước N").

### #14 – Kiểu màn hình theo tài liệu HDSD (2026-10-30, người dùng gửi thư mục SharePoint site aq)
- Nhận biết: mỗi chức năng thuộc một kiểu – **Danh mục** (lưới + khung chi tiết bên phải "detailright"), **Quyết định**
  (đầu quyết định + view "Danh sách sinh viên quyết định" có nút Thêm/Import riêng), **Cập nhật theo mã SV** (gõ mã → tab),
  **Chọn lớp → Tiếp tục**, **Nhập trên lưới**, **Import** (Xuất cấu trúc), **Đồng bộ/Thực hiện** (nhiệm ý), **Báo biểu**
  (nhiệm ý → In → cửa sổ xem in), **Chỉnh định thông số** (GS_/SS_). Trường bắt buộc tô **đỏ**.
- Thao tác đúng / lệnh auto: bảng ở `thao-tac.md` mục 1. Đồng bộ/Thực hiện/Chỉnh định thông số làm thay đổi dữ liệu hàng loạt
  → hỏi người dùng trước khi đưa vào kịch bản; không bao giờ chọn nhiệm ý "Đồng bộ tất cả (xóa hết…)".
- Chi tiết từng phân hệ + tiến độ đọc: `thao-tac.md` (đọc tiếp phân hệ chưa ✔ khi có token). Ảnh trong tài liệu không lấy
  được qua connector → dùng kịch bản khảo sát chỉ-xem (`KS-QLSV-001`) để có ảnh + `ui-ks-*.txt` thật.
- Áp dụng: kit `2026.10.30-14` – lệnh `cancel` chỉ gửi Esc khi đang có cửa sổ con (theo #13).

### #15 – Khung nhập (detail) dùng TÊN CONTROL, không có nhãn (lượt chạy QLSV-001 ngày 2026-11-02 23:39, kit -14)
- Hiện tượng: bước 1–5 đạt (ô tìm kiếm, chọn ngẫu nhiên lớp/lý do chạy đúng); bước 6 "Không tìm thấy Lý do quyết định" vì
  **nhãn ô ("Số quyết định:", "Lý do quyết định:"…) KHÔNG có trong cây UIA**.
- Nhận biết (`ui-buoc-6-loi.txt`, màn hình mã `S15.04` Quyết định vào mới): màn hình = lưới trái `Table "Danh sách quyết định"`
  (automationId `viewDataCtrl`, nút đáy: In, Tách quyết định, Refresh, Thêm, Sửa, Xóa, Đóng – **mờ khi đang nhập**) + khung phải
  `Pane AQDetailRight` → `XtraLayoutControl` (tiêu đề "Chi tiết Danh sách quyết định") với nút đáy **Lưu / Hủy**.
  Mỗi ô là `Pane <Tên>_UC` → ô `<Tên>` (automationId = tên cột dữ liệu) → ô soạn thảo thật lớp `WindowsForms10.EDIT` (id là số
  handle, đổi mỗi lần – không dùng). Dấu bắt buộc là `Text "* "` cạnh ô. Lưới bố cục liệt kê `DataItem` tên đúng bằng tên control.
  Ánh xạ S15.04: Số quyết định* `SoQDSV` · Tên quyết định `TenQDSV` · Ngày lập QĐ* `NgayLapQDSV` (mặc định hôm nay) ·
  Lý do quyết định* `IDLDQDSV` (lookup: cột Mã loại / Tên loại quyết định, vd TT = Quyết định Trúng tuyển) · Ngày hiệu lực
  `NGAYHLQDSV` (mặc định hôm nay) · Người ký `IDChuKy` (Loại chữ ký: Chữ ký đơn ▾, Chọn chữ ký ▾ + ô chữ) · Ghi chú `GcQDSV` ·
  Hình quyết định `NoiDung`. Lưới con `Table "Danh sách sinh viên"` (cột Mã SV, Họ lót, Tên, Phái, Mã lớp (mới); có dòng lọc;
  nút đáy **Import, Thêm, Thêm mới 1 SV, Xóa**). Các khung thường gặp: `AQViewL` (lưới trái), `aqSplitContainer1`.
- Thao tác đúng: ô của khung nhập → `type: #SoQDSV = …`, `select: #IDLDQDSV = TT` (gõ mã rồi Enter), `date: #NGAYHLQDSV = …`;
  sinh viên mới vào quyết định → `click: Thêm mới 1 SV` (popup/ô chưa biết – kịch bản đã thêm `dump`).
- Áp dụng: kit `2026.11.02-1` – `field_for` nhận `#TênControl` (`Edusoft.by_id`, lấy ô EDIT bên trong); QLSV-001 bước 6, 10 dùng
  `#…`; bước 7 bấm Thêm mới 1 SV rồi chụp + `dump: them-moi-1-sv`.
- Mã nguồn client Edusoft (nếu người dùng đưa): đọc các form/`*.Designer.cs` để lấy bảng **tên control ↔ nhãn** và kiểu control
  cho từng màn hình (mã màn hình như `S15.04`), ghi thành bảng trong `thao-tac.md`; **không** commit mã nguồn vào repo
  (để ngoài git, vd `local/` hoặc scratchpad) – chỉ ghi bảng ánh xạ.

### #16 – Thư mục cài Edusoft và `Languages.xml` (2026-11-02, người dùng gửi từ `A:\EDUSOFT\aq.edusoft.all`)
- `A:\EDUSOFT\aq.edusoft.all` là **bản đã build** (539 dll, 212 mẫu báo biểu `.mrt` Stimulsoft, DevExpress **v16.2**),
  không có mã nguồn (`.cs`/`.sln`). Đừng gửi `*.config` (mật khẩu SMTP, chuỗi kết nối).
- Module Edusoft = `Edusoft.<MÃ>.dll` (+ `.WcfContracts`): SRM, RMS, SCH, SMS, CMS, DCM, TPM, EPM, HRM, PMS, MDS, ZMS, SRT,
  JMS, EMS, BSM, STM, EVA, DMS, TQM, ILS, EAU; nền: `Edusoft.Base`, `Edusoft.DataAccess/DataObjects`, `AQFramework`,
  `AQControls.Forms.UI.v3` (control AQ…), `AQViewers`, `AQData.*`.
- `Languages.xml` (một ngôn ngữ VN, ~14.000 `<Item ID="MA_HANG" Value="…">`) = **bảng thông báo/nhãn theo mã hằng**
  (vd `CHUA_NHAP_SO_QD` = "Chưa nhập số quyết định", `SO_QD_DA_TON_TAI_TRONG_HK` = "Số quyết định này đã tồn tại trong học kỳ").
  **Không** có ánh xạ tên control ↔ nhãn. Dùng để tra đúng chữ hộp thoại cho `expect_dialog:`/`expect:`; không commit cả file.
- Nhãn ô của khung nhập (vd S15.04) không nằm trong `Languages.xml` → lấy từ metadata trong dll (`AQControls…`, module) hoặc CSDL.

### #17 – Khung AQ dựng màn hình từ CSDL (đọc metadata dll 2026-11-02: AQViewers, AQControls.Forms.UI.v3, AQFramework, Edusoft.Base, Edusoft.SRM)
- Phần lớn màn hình là **màn hình chung theo metadata**: `AQViewL` (lưới trái, kế thừa `AQViewBase`) + `AQDetailRight`
  (khung nhập phải) đọc cấu hình **View/FieldView** trong CSDL rồi tự tạo control. Không có form riêng trong dll →
  không thể lấy bảng nhãn từ dll; nhãn = `TenLabel` (bảng `AQDmField`, ghi đè theo View ở FieldView), vị trí `RowIndex/ColIndex`,
  `TabOrder`, `AllowNull` (= dấu `*`), `ReadOnly`, `Hide/HideLbl`, `DefaultValField`, `CtrlType`. Bảng metadata thấy trong
  câu SQL: `AQDmFile` (MaFile = tên bảng), `AQFileField`, `AQDmField` (MaField, TenField, TenLabel, SpecType, DoDaiField).
- Control tạo ra: tên = `MaField` (cột CSDL), bọc trong `<MaField>_UC`; nhãn là **chữ của LayoutControlItem** (DevExpress
  vẽ, không có trong UIA) → kit chỉ tìm được ô bằng `#MaField`. Muốn gõ theo nhãn phải có bảng nhãn ↔ MaField lấy từ CSDL.
- Kiểu ô (`AQFramework.TypeControl`): TextBox, ComboEdit, CheckBoxEdit, SpinEdit, DateTimePicker, ImagePicture,
  **LockupEdit** (`AQLockUpEdit`: gõ mã rồi Enter, có cờ `KeyPressEnter`), ComboEnum, ComboImage, RichTextBox, ChooseImage;
  ngoài ra khung nhập có loại riêng: Ngày sinh, NHHK, Sinh viên (gõ mã SV), Chữ ký, Địa chỉ/Địa bàn, Mail, Số phiếu, Mật khẩu.
- Kiểu View (`TypeView`): ViewDoi (lưới + khung nhập), ViewOnly, EditOnly.
- **Hộp thoại**: `AQControls.AQMessageBox.MsgBox` (Form; nội dung ở `lblMessage`, nút `btn1`/`btn2`/`btn3` chữ Có/Không/OK…);
  **lỗi hệ thống** = `ErrorMsgBox` (`lblThongBao`, `rtxt_Error`, nút `btnViewErrorHelp…`, chữ "Đã xảy ra lỗi khi xử lý nghiệp vụ…
  [Gửi mail về Support]") → coi là **Lỗi** (bad), chụp ảnh, không bấm gửi mail. Kit `2026.11.02-2`: `Edusoft.dialog_info`/`is_error_dialog` nhận theo tên control, nội dung `lblMessage` lên đầu, lỗi hệ thống thêm "[Lỗi hệ thống Edusoft]".
- Lưu trùng mã: hộp thoại "`<mã>` đã có, có chấp nhận bị trùng không?" → không bấm Có (kit đã không bao giờ tự bấm Có).
- Màn hình **tùy biến** = lớp `UCT_*` kế thừa `AQViewCommonCtr` (control tên cố định: `btn…`, `txt…`, `look_…`, `rdo_…`, `chk…`,
  `spn…`, `dat_TuNgay/dat_DenNgay`, `lbl…`); nhập Excel = `UCImport_01/02/03` (Chọn file, Sheet, Dòng tiêu đề, Dòng dữ liệu;
  map cột; bảng lỗi). Dll theo phân hệ: `Edusoft.SRM` = điểm, tốt nghiệp, chứng chỉ, in điểm (namespace D1–D10, Q1–Q9, DKTBB…);
  QLSV nhiều khả năng ở `Edusoft.SMS` (chưa có) – chỉ cần nếu màn hình QLSV là `UCT_*` riêng.

### #18 – Ô tra cứu phải CHỌN, hai nút Thêm, chữ Unicode tổ hợp (lượt chạy QLSV-001 2026-11-03 00:12, kit 11.02-2; người dùng dạy)
- Ô tra cứu (vd Lý do quyết định `#IDLDQDSV`): gõ "TT" chỉ lọc/tô sáng dòng trong danh sách thả xuống (cột Mã loại | Tên loại
  quyết định) – **chưa chọn**; rời ô là mất giá trị (lượt này ô Lý do trống). Đúng: mở danh sách (nút ▾ `Button "Open"` của ô)
  rồi **bấm chọn dòng**; nếu gõ thì gõ xong phải bấm chọn dòng đang có. Kit `2026.11.03-1`: `choose: #Ô = giá trị` (mở rồi chọn),
  `select: #Ô = giá trị` (gõ rồi chọn); không đọc được danh sách thì ghi `ui-danh-sach-*.txt` rồi Enter; ô vẫn trống → bước Lỗi.
- Quyết định vào mới có **hai cụm nút Thêm**: thanh dưới danh sách quyết định trái (In, Tách quyết định, Refresh, Thêm, Sửa, Xóa,
  Đóng) và thanh dưới lưới con "Danh sách sinh viên" (**Import, Thêm, Thêm mới 1 SV, Xóa**). Lưới con: "Thêm" = chọn sinh viên
  có sẵn; "Thêm mới 1 SV" = thêm dòng sinh viên mới (cột Mã SV, Họ lót, Tên, Phái, Mã lớp (mới)). Ghi rõ vùng:
  `click: Thêm @ Danh sách quyết định`, `click: Thêm mới 1 SV @ Danh sách sinh viên` (tên vùng = tên `Table` trong ui-*.txt).
- Nhập trên lưới: `cell: Cột = giá trị @ Lưới` (bấm ô ở dòng dưới cùng, gõ; ô có danh sách thì chọn dòng khớp).
- Chữ Việt trong Edusoft có chỗ ở dạng **Unicode tổ hợp** (nút "Thêm mới 1 SV": "mới" = ơ + U+0301) → so khớp phải chuẩn hoá NFC
  (kit `norm()` đã làm); lượt 00:12 báo "Không tìm thấy Thêm mới 1 SV" dù nút có trên màn hình chính vì lý do này.

### #19 – "Thêm mới 1 SV" mở form, chọn lớp bằng nút "…", tắt màn hình bằng X (người dùng dạy 2026-11-03, lượt 00:29)
- "Thêm mới 1 SV" (lưới Danh sách sinh viên của Quyết định vào mới) mở **cửa sổ riêng** "Chi tiết lý lịch sinh viên"
  (`UC_CapNhatLyLich_Add`, khung `AQDetailRight`, tab Lý lịch / Liên lạc / Gia đình / Thông tin vợ-chồng / Hồ sơ sinh viên;
  nút đáy **Lưu, Đóng**). Nhập các ô dấu * đỏ: `#MaSV`, `#HoLotSV`, `#TenSV` + Ngày sinh (`NgaySinhC` gồm 3 ô `#txtDay`,
  `#txtMonth`, `#txtYear`, nút lịch `picCalendar`) → Lưu → form đóng, lưới có dòng sinh viên mới.
  Ô khác: `Phai`, `DC_IDNoiSinhSV` (nút …), `IDLop`, `IDDV`, `NguonTuyen`, `IDDT`, `IDTG`, `QuocTich`, `SoCMND`…
- Ô **Mã lớp (mới)** của dòng đó: bấm ô → hiện nút **"…"** ở mép phải → cửa sổ "EduSoft.NET" **Danh sách lớp** (cột Mã lớp,
  Tên lớp; có dòng lọc; ~500 lớp; nút Export, **Chọn**, Đóng): tìm lớp (dòng lọc Mã lớp) → bấm dòng → **Chọn**. Rồi Lưu quyết định.
  Kit: `cellbtn: Mã lớp (mới) @ Danh sách sinh viên`, `find_row: {LOP} @ Mã lớp`, `click: Chọn @ Danh sách lớp`.
- Mỗi màn hình chức năng có nút **X** trên tab MDI (TabItem tên màn hình + Button "Close"): **test xong chức năng nào tắt
  chức năng đó** → `close: Tên màn hình` (hỏi lưu thì bấm Không).
- Lỗi EX báo nhầm: ô ảnh có tên "System.Drawing.Bitmap" → kit 2026.11.03-2 bỏ mẫu "system." trơn khỏi `EX_PAT`.
- Ô nhập trong form con: `set_field` không còn đóng chính form chứa ô (trước đây `close_dialogs` đóng mọi cửa sổ con).
- Quy trình QLSV-001 người dùng chốt: thêm QĐ (thông tin + Thêm mới 1 SV + chọn lớp) → Lưu → kiểm tra QĐ → Danh sách sinh viên
  học kỳ có SV mới (có = Đạt) → Sửa Tên QĐ → Lưu → kiểm tra → Xóa QĐ → kiểm tra không còn. Xong.

### #20 – Form con (popup nhập/chọn) là cửa sổ riêng nhưng UIA xếp vào cửa sổ chính (lượt QLSV-001 03/11 01:05, kit 11.03-3)
- Rất nhiều menu Edusoft mở **form con**: Thêm mới 1 SV ("Chi tiết lý lịch sinh viên"), Danh sách lớp (nút …), Import, chọn
  sinh viên… Đó là cửa sổ Win32 cấp cao (thuộc cửa sổ chính) – UIA lại xếp nó **vào trong** cửa sổ chính, nên
  `top_level_parent()` của ô trong form trả về cửa sổ chính.
- Lỗi đã gặp: `set_field` đóng "hộp thoại" trước khi gõ, tưởng form là thông báo → bấm Đóng của form → ô `#MaSV` mất,
  "không nhận giá trị". Kit `2026.11.03-4`: tìm cửa sổ chứa ô bằng Win32 `GetAncestor(GA_ROOT)` (`root_handle`), và
  `close_dialogs` **chỉ đóng hộp thông báo**, bỏ qua form (`is_form`: có `AQDetailRight`/`AQViewL`/`viewDataCtrl` hoặc
  Table/DataGrid/Tab). Muốn đóng form thì dùng nút của form (`click: Đóng`, `save: Lưu`) hoặc `cancel`.
- Viết `auto` cho form con: bấm nút mở form → thao tác ô bằng `#TenControl` (kit tìm form con trước cửa sổ chính) →
  `save: Lưu` (nút Lưu của form) → form tự đóng, quay lại màn hình chính.

### #21 – Thanh nút của form chọn (Export / Chọn / Đóng) nằm xa lưới (lượt QLSV-001 03/11 01:14, kit 11.03-4)
- Form **Danh sách lớp** (`FormChonView`): lưới `viewDataCtrl` "Danh sách lớp" nằm sâu ~8 tầng (SourceViewBase → SplitControlView
  → … → AQViewL → Table), còn thanh nút (Group "Dock Bottom" → MenuBar "Main menu" → Button Export/**Chọn**/Đóng) là con
  trực tiếp của cửa sổ form. Kit cũ chỉ lên 4 tầng từ lưới nên báo "Không thấy nút Chọn trong vùng Danh sách lớp".
- Kit `2026.11.03-5`: `click: Nút @ Vùng` lên dần **tới tận cửa sổ chứa vùng** (form con hoặc cửa sổ chính), tầng gần
  nhất thắng – vẫn phân biệt được các nút trùng tên (Thêm của lưới con vẫn được tìm trước Thêm của danh sách trái).
- Mẫu chung cho mọi form chọn (FormChonView: chọn lớp, chọn sinh viên, chọn môn…): `find_row: {GIÁ_TRỊ} @ Cột` (dòng lọc) →
  `click: Chọn @ <tên lưới của form>`.

### #22 – Xóa có nhiều bước xác nhận (lượt QLSV-001 03/11 01:22, kit 11.03-6)
- Bấm **Xóa** trên danh sách (vd Quyết định vào mới) → cửa sổ "EduSoft.NET" chữ xanh **"Danh sách đang chọn để xóa, vui lòng
  kiểm tra và chọn xác thực lại"**: lưới (cùng tên lưới gốc, vd "Danh sách quyết định") có cột ô check `#` (DataItem
  "# row N" = Checked/Unchecked), nút Export / **Thực hiện** / Đóng. Phải **tick ô check** dòng cần xóa → **Thực hiện**.
- Tiếp theo hộp "**Xác nhận xóa dữ liệu đang chọn?**" (Có / Không – không nêu mã) → **Có** → thông báo kết quả → OK.
- Kit `delete_row` tự đi hết chuỗi này. An toàn: mọi dòng trong lưới xác nhận phải mang mã test (không thì Đóng, không xóa);
  hộp hỏi không nêu mã chỉ được bấm Có khi đã qua bước kiểm lưới đó; hộp hỏi khác → Không.
- Lượt cũ (kit ≤ 11.03-5) đọc lưới bằng tên phần tử (không có giá trị ô) nên tưởng hộp không nêu mã → bấm Đóng, dữ liệu test
  TEST_QD_030122 còn lại (xóa tay hoặc chạy lại – lượt sau mã khác nên không trùng).

### #23 – Kết quả Lưu/Xóa báo ở THANH TRẠNG THÁI; lưới không tự nạp lại (lượt QLSV-001 03/11 01:35, kit 11.03-7)
- Lưu / Xóa thành công thường **không bật hộp thoại**: chữ xanh hiện ở thanh trạng thái dưới đáy cửa sổ chính
  (StatusBar "Status bar" → Text, cạnh "Năm học", "Học kỳ", "ĐVPC: …"), vd **"Xóa dữ liệu thành công"**,
  "Cập nhật mẫu tin Chi tiết Danh sách quyết định thành công". Kit: `save:` và `delete_row:` chờ chữ này đổi
  (`status_msg`/`wait_status`), ghi vào ghi chú bước; chữ báo lỗi → bước Lỗi.
- Trong lúc xóa có cửa sổ "progressPanel1" (không có nút) – chờ nó tự tắt, không bấm gì.
- Xóa xong lưới **vẫn còn dòng** (chưa nạp lại) → người dùng dạy: tắt màn hình bằng X, mở lại menu, kiểm tra lại;
  không còn = Đạt. Kit: `absent:` tự làm việc này (menu lấy từ lần mở menu gần nhất / menu chính của kịch bản).
- QLSV-001 lượt này: bước 1–12 đạt (xóa thành công), bước 13 dừng vì lưới cũ. Người dùng bỏ các luồng thay thế, chỉ chạy luồng chính.
- Lượt 03/11 01:50 (kit 11.03-7): tắt rồi mở lại "Quyết định vào mới" ngay sau khi xóa → Edusoft bật **lỗi EX thật**
  (InvalidOperationException "This command is only applicable to WaitForms" tại SplashScreenManager.SetWaitFormDescription ←
  AQViewers.MainForm.CallFunction ← treeChucNangC3_DoubleClick; menu S15.04). Người dùng xác nhận "test là phải như này" –
  ghi lỗi EX (Ctrl+Shift+E chi tiết, Ctrl+Shift+F menu code), không né.

### #24 – Script xóa "thành công" nhưng Edusoft không xóa (lượt 03/11 01:35 + 01:50, kit 11.03-6/7)
- Dấu hiệu: ghi chú bước 12 "Đã tick 1 dòng … · Đã xóa …" nhưng ảnh `buoc-12.png` vẫn còn dòng, thanh trạng thái KHÔNG đổi
  sang "Xóa dữ liệu thành công" (vẫn "Cập nhật mẫu tin …"); người test làm tay thì xóa được.
- Nguyên nhân (suy từ bằng chứng): ô check `#` trong form "Danh sách đang chọn để xóa" không ở trạng thái tick lúc bấm
  Thực hiện – kit cũ có thể bấm ô 2 lần liền (tick rồi bỏ tick) vì đọc giá trị ô khi ô đang sửa chưa ghi vào lưới;
  Thực hiện → Có với 0 dòng chọn nên không xóa gì. Kit cũ còn không kiểm thanh trạng thái nên báo nhầm "Đã xóa".
- Kit `2026.11.03-9`: `tick_box` bấm ô 1 lần → chờ đọc → bấm sang ô khác cùng dòng (đẩy giá trị vào lưới) → đọc lại; chỉ bấm
  lần 2 khi đọc chắc chắn còn Unchecked; không tick được → không xóa, báo lỗi. Bấm Thực hiện / Có bằng chuột như người test.
  Ảnh `xoa-da-tick.png` (form trước Thực hiện). Sau Có **bắt buộc** thanh trạng thái báo "Xóa … thành công", không thì bước Lỗi
  ("Edusoft KHÔNG báo Xóa dữ liệu thành công") + ảnh `xoa-khong-bao.png`.

### #25 – Tốc độ nhận diện & lần xóa thứ 3 vẫn không xóa (lượt 03/11 02:09, kit 11.03-9 → 11.03-10)
- Chậm: bước 2 (Danh mục sinh viên) 3 phút. Nguyên nhân trong kit: mỗi lần tìm duyệt cây UIA nhiều lần (`descendants(control_type=…)`
  cho từng loại) và hỏi từng thuộc tính (hàng nghìn lần gọi chéo tiến trình); kiểm tra "chưa có" luôn chờ đủ 6 giây; tên test
  thử lần lượt Mot→Hai→… (các lượt trước đã dùng nên mỗi lượt thử 5–6 tên). Kit 11.03-10: `uia_scan` một lần
  `FindAllBuildCache` lấy tên/loại/id/lớp/toạ độ/giá trị cả cây; dùng cho find_any, by_id, element_with_text, column_header,
  grid_rows, is_form; lưới lọc xong không còn dòng → kết luận "chưa có" sau ~1,2 giây; tên test chọn ngẫu nhiên.
- Xóa lượt 02:09: ảnh `xoa-da-tick` cho thấy ô đã tick (cả ô nhóm, ô tiêu đề) → Thực hiện → Có, nhưng thanh trạng thái không đổi,
  dòng còn. Kit cũ bấm **Đóng form** khoảng 3–4 giây sau Có (khi chưa thấy gì) – có thể cắt ngang lúc Edusoft đang xóa.
  Kit 11.03-10: sau Có **không bấm gì**, chờ tới 40 giây cho thanh trạng thái báo "Xóa … thành công" / form tự đóng; ghi
  **nhật ký xóa** có mốc thời gian (bấm Xóa, form xác nhận, tick, Thực hiện, hỏi → Có, cửa sổ đang xử lý, thông báo, form tự
  đóng, thanh trạng thái) vào ghi chú / lỗi của bước. Người dùng đang thử xóa tay trên Edusoft để xem có phải lỗi phần mềm.

### #26 – Hộp hỏi Có/Không: con trỏ mặc định ở **Không** (người dùng phát hiện 03/11, kit 11.03-11)
- Hộp "Xác nhận xóa dữ liệu đang chọn?" (và các hộp hỏi AQ MsgBox khác) mở ra với con trỏ bàn phím ở **Không** (viền chấm).
  Ảnh lượt chạy cho thấy Có sáng (chuột đang trỏ) và Không có viền con trỏ – tức kit "vừa chọn Có vừa chọn Không".
- Kit cũ: bấm chuột Có, 0,8 giây sau hộp chưa đóng thì `press(Có)` = đặt con trỏ + gửi **Space**; `focus()` coi là đã đặt được con
  trỏ khi không kiểm được → Space rơi vào nút đang có con trỏ = **Không** → Edusoft không xóa (người dùng xóa tay vẫn được).
- Kit 11.03-11: `press_yes` – đưa hộp lên trước, ghi "nút đang chọn sẵn", chụp `xoa-hoi-xac-nhan.png`, bấm CHUỘT vào Có, chờ
  hộp đóng tới 3 giây; chưa đóng thì chỉ gửi Space khi ĐÃ KIỂM con trỏ ở Có, không thì Invoke nút Có; vẫn mở → báo lỗi
  (không xóa). `focus()` không kiểm được con trỏ → trả False (press bấm chuột, không gửi phím mù). Hộp "Bạn có muốn lưu…?"
  của `save:` cũng dùng `press_yes`.
- Quy tắc chung: **không bao giờ gửi Space/Enter vào hộp hỏi khi chưa chắc con trỏ ở đúng nút** – nút mặc định của Edusoft
  thường là nút an toàn (Không).

### #27 – Phải TICK ô chọn của dòng trên lưới chính trước khi bấm Xóa (người dùng chỉ 18/11, kit 11.18-02)
- Màn hình "Quyết định vào mới" (và lưới có cột ô check đầu dòng): Edusoft chỉ xóa **dòng đã tick ô chọn** ở lưới danh sách
  (cột check đầu dòng, cạnh "Ngày lập QĐ"). Chỉ bấm chọn dòng (dòng sáng) rồi bấm Xóa → form "Danh sách đang chọn để xóa" vẫn hiện
  và tick được ở form, Thực hiện → Có nhưng **không xóa** (thanh trạng thái không báo, lượt 18/11 hết 40 giây chờ).
- Thao tác đúng: lọc cột → thấy dòng → **tick ô chọn của dòng đó trên lưới chính** → Xóa → (form xác nhận: tick lại nếu cần) →
  Thực hiện → Có → thanh trạng thái "Xóa dữ liệu thành công".
- Kit 11.18-02: `delete_row` (không có `=> Nút`) tìm ô chọn cùng hàng, bên trái ô vừa tìm (`row_checkbox`: DataItem cùng "row N"
  có giá trị Checked/Unchecked hoặc CheckBox) → `tick_box`; không tick được → báo lỗi, không bấm Xóa; lưới không có cột check → như cũ.
  Form xác nhận vẫn kiểm mọi dòng phải mang mã test (dòng test cũ còn tick sót → không xóa).

## 5. Quy trình khi được dạy

1. Nhận ảnh chụp / mô tả / file `ui-*.txt`; hỏi lại nếu chưa rõ phần tử nằm ở đâu. Lưu ảnh vào `anh/`.
2. Ghi bài học vào mục 4, cập nhật bảng mục 2 (và sơ đồ mục 1 nếu là vùng mới).
3. Nếu bộ test phải nhận diện khác đi → sửa `kit/aqrun.py` (tăng `KIT_VERSION`), cập nhật docstring `Run.do_actions`.
4. Rà các kịch bản `scriptReady` (`data/scenarios/`) có dùng phần tử đó → sửa `auto` (cả `data/` và DB artifact).
5. Commit + push, cập nhật artifact nếu console thay đổi (theo CLAUDE.md).

## 6. Tra source Edusoft (`tools/trich_source.py`)

Source nằm trên TFS (chỉ đọc) hoặc file zip trên máy người dùng – **không đưa source vào repo/chat**. Người dùng chạy
`python tools\trich_source.py <zip> --liet-ke | "<từ khóa>" | --tim "<câu>" | --tat-ca` rồi gửi file `trich-*.txt` / `trich-tat-ca.zip`
(chỉ tên điều khiển, caption, cột lưới, câu thông báo). Ghi điều rút ra vào đây, không chép nguyên file trích.

Cấu trúc (bản trích 11/2026 – 4 665 file Designer): `trunk2/Edusoft.<MÃ>/Edusoft.<MÃ>/<nhóm>/<mục>/<Form>.Designer.cs`.
Mã module → nghiệp vụ (? suy từ tên form, chờ xác nhận): SMS sinh viên (QĐ vào/ra, học bổng, rèn luyện) · RMS đăng ký môn
học + học phí · SRM điểm/bảng ghi điểm, xét tốt nghiệp-luận văn · EPM lịch thi · SCH thời khóa biểu · TPM chương trình đào tạo/
môn học · DCM khối lượng giảng dạy, thù lao CBGD · TQM khảo sát đánh giá · MDS ký túc xá (nội trú) · CMS tuyển sinh ·
BSM kho học liệu · HRM nhân sự · PMS lương · JMS tài sản · DMS công văn · EMS kiểm định (minh chứng) · SRT NCKH ·
STM đào tạo ngắn hạn · EVA đánh giá viên chức · ILS lưu học sinh · NET lõi chung (phân quyền, nhập điểm…) ·
AQDataTools khung dùng chung (`AQControls.v3`, `AQViewers`).

**Bản trích 15/11/2026 (`trich-tat-ca.zip`, 4 504 form, 3 087 chỉ có `SourceViewBase`) đã ghép vào danh mục** bằng
`python tools/gan_form_tay.py <trich-tat-ca.zip>` → `web/edusoft-catalog.json` thêm `forms` + `menus[].fm`: 708 menu có phần
vẽ tay (565 trong đó không có lưới từ CSDL), 489 form · 1 373 ô · 228 nút. Trang Màn hình Edusoft hiện khối "Phần vẽ tay
trên form" (ô `#tên control`, kiểu, nhãn cạnh ô **đoán** theo vùng, nút, câu thông báo trong mã). Thường là thanh lọc phía
trên lưới (vd `#lockKhoaHoc` "Chọn khóa học", `#dat_TuNgay`/`#dat_DenNgay`, nút "Tìm"). Lập lại danh mục từ CSDL
(`lap_danh_muc.py --json`) thì chạy lại `gan_form_tay.py` sau đó.

**Điều quan trọng rút ra:**
- Màn hình chức năng phần lớn **dựng theo cấu hình trong CSDL**, không vẽ trong source: user control kế thừa
  `AQViewers.AQViewCommonCtr` chỉ chứa một `SourceViewBase` (3 087 chỗ dùng) → bên trong `SplitControlView` (AQSplitContainer)
  → lưới/nút/nhãn sinh lúc chạy (khớp `FormChonView`/`viewDataCtrl` ở mục 4). Ví dụ QĐ vào/ra SV: `Edusoft.SMS/S02/UCQDSV`
  chỉ có `grdQD | SourceViewBase`. ⇒ **Tên ô, nút, cột cho `auto` phải lấy từ `ui-*.txt`, không lấy được từ source.**
  Source chỉ có ích cho form vẽ tay, câu thông báo nghiệp vụ (vd UCQDSV: "Ngày về phải lớn hơn ngày đi") và tên lớp.
- Câu thông báo chung ("Xóa dữ liệu thành công", "Thoát khỏi chương trình?", "Danh sách đang chọn để xóa") **không có trong
  source** – nhiều khả năng lấy từ CSDL/thư viện biên dịch; cứ dùng đúng chữ quan sát trên màn hình.
- Cửa sổ chính `AQViewers/MainForm` (RibbonForm, tiêu đề "EduSoft.NET"): ribbon `ribonMain`; khung trái `dockLeft`
  "Danh mục chức năng" chứa cây `treeChucNangC3` (cột "Tên chức năng" [TenChucNang]) và `navBarControl1` nhóm "Thông tin đơn vị"
  (`lblTenTruong`); vùng tab màn hình `tabForm` (AQTabControl, trang "Phổ dụng"/"Các chức năng"); menu chuột phải tab:
  "Đóng tab hiện tại" (`btnDongHienTai`), "Đóng tất cả tab ngoại trừ hiện tại", "Đóng tất cả"; thanh trạng thái `bar3`:
  "Năm học" (`barNamHoc`), "Học kỳ" (`barListHocKy`), "Kỳ thi", "Năm", "Tháng", "Đợt đánh giá", "Kỳ tuyển sinh", "Kỳ đánh giá",
  `lblStatusMess` (**câu kết quả Lưu/Xóa hiện ở đây**), `lblUserName`, "Đăng xuất" (`btnBarDangXuat`).
- **Định nghĩa gốc màn hình chưa tìm thấy** (11/2026): CSDL trường (bản backup, 3 050 bảng) chỉ có phần chỉnh riêng –
  `HFieldEdit`, `HFieldView2`, `HOrderView`, `HValSetV`, `HViewSpliter`, `HMenuCustom` – trỏ tới `IDView`/`IDFieldView`/`IDChucNang`
  không có bảng gốc; `HMess` là câu chữ Netweb. Thư mục cài Edusoft cũng không có file định nghĩa (file không đuôi = cache
  WebView2, `.xml` = tài liệu DevExpress, `logs/webapi.log.*` = log, **không gửi**).
- **Bảng định nghĩa gốc** (theo `AQ.DatabaseShare/DatabaseAll.edmx` + `AQData.Business/Viewer/ViewServiceBL.cs`): nhóm `AQ…` –
  `AQDmChucNang` (menu/chức năng), `AQDmView1`/`AQDmView0`, `AQView`, `AQViewSpliter`, `AQFieldView`/`AQFieldView2`, `AQDmField`,
  `AQFieldEdit`, `AQTabView`/`AQTabColumn`, `AQOrderView`, `AQDmForm`, `AQDmMess`/`AQDmMessErr`, `AQMessNgonNgu`… Màn hình nạp qua
  `ViewServiceBL.GetViewParams(idView1, subview)` → `GetSpliter`/`GetDmView`/`GetView`, dùng cùng ngữ cảnh `db` với các bảng `H…`
  (phần trường chỉnh) – nhưng 175 bảng `AQ…` này **không có trong `sys.tables`** của bản backup trường → có thể là synonym/view
  trỏ sang CSDL khác (chưa kiểm).
- Bảng `AQ…` **không nằm trong CSDL trường**: được đóng thành file dữ liệu hệ thống `AQ.Data001…146.dll` (đuôi .dll nhưng là
  dữ liệu, có file 22 byte) ở **server** (`wcf/bin`, `web/bin` của gói `edusoft.server.zip`), vd 001 = AQDmFile, 002 = AQDmField,
  003 = AQFileField, 004 = AQRelation; công cụ `ReleaseTools/SysDataManager` (có KeyGen) tạo ra. Máy client không có các file
  này – Edusoft.NET lấy định nghĩa màn hình **qua WCF của server**. Không giải mã các file này; cần danh mục menu/cột thì xin
  nhóm phát triển AQTech xuất từ SysDataManager. Thực tế: tên ô/nút/cột cho `auto` lấy từ `ui-*.txt` khi chạy.
- **Chuỗi nguồn gốc định nghĩa màn hình** (đã xác minh từ source): CSDL gốc của AQTech (CSDL phát triển nội bộ, có đủ bảng `AQ…`)
  → `SysDataManager` ("System Data Management": *Export 148 file AQ System Data*, *Export system data (các file cách nhau dấu
  phẩy)*, *Import/Update from edusoft*) → 148 file `AQ.Data…` đóng vào gói server → server đọc bằng
  `SystemData.ReadResource<T>(sourceName)` / `SystemData.ReadAQResource(sourceName, Type) → DataTable` (lớp
  `AQData.Business/Common/SystemData.cs`, có `DataMap` ánh xạ tên ↔ file) → client nhận qua WCF → ghép phần chỉnh của trường
  (`H…`) → màn hình. Muốn có danh mục menu/view/cột đúng phiên bản: xin AQTech xuất (SELECT chỉ đọc) các bảng `AQDmChucNang`,
  `AQDmView1`, `AQView`, `AQFieldView(2)`, `AQDmField`, `AQFieldEdit`… hoặc dùng chính `AQData.Business.dll` của server trường đọc
  file `AQ.Data…` rồi xuất CSV (chạy trên máy người dùng, không đụng khóa).
  **Định dạng file** (`SystemData.ReadResource`): `AQ.DataNNN` = JSON danh sách bản ghi **nén gzip** (file 22 byte = `[]`),
  đọc từ thư mục bin của server; `DataMap` ánh xạ tên bảng → số file theo thứ tự (trunk: 001 AQDmFile, 002 AQDmField,
  027 AQDMChucNang, 030 AQFieldEdit, 046 AQDMView1, 055 AQFieldView, 059 AQView, 061 AQViewSpliter, 077 AQFieldView2,
  025 AQDmMess…; gói cũ đánh số 000–146 + `AQ.Data.Specs` nên có thể lệch – đối chiếu theo tên cột).
  Công cụ: `python tools\doc_aqdata.py D:\Source.NET.zip --trong edusoft.server.zip` (hoặc thư mục `wcf\bin` của server trường)
  → `aqdata\*.csv` + `tom-tat.txt` + `aqdata.zip`; chỉ giải nén, bỏ bảng người dùng/khách hàng, để trống cột mật khẩu/khóa.
  Gói server trong source khớp đúng thứ tự trunk (001 AQDmFile … 146 AQFileHuongDan; 000 không phải JSON). Quan hệ:
  `AQDMChucNang` (menu; `IDChucNangParent` → cha, gốc là `AQDMPhanHe`; chữ hiện = `VtChucNang`/`VtPhanHe`) –`iddoituong`→
  `AQDMForm` (`FormRun` = lớp màn hình, vd `Edusoft.SMS.S02.UCQDSV`; `Param1` của menu = loại, vd VAO_MOI/DOI_LOP) → lớp tự nạp
  `AQDMView1` (MaView1 ghi trong source) → `AQView` (lưới; cờ NoneInsert/NoneDelete/NoneSua…; `MainTable` → `AQDmFile`) →
  `AQFieldView` (cột; `IDField` → `AQDmField.Tenlabel` = nhãn, `MaField` = tên ô; `Hide`, `ReadOnly`, `CtrlType` 4=ngày,
  13=nút "…"), `AQFieldView2.TabOrder` (thứ tự), `AQFieldEdit` (ô trên form sửa), `AQViewAddCtrl` (nút riêng: CommandName,
  ToolTip, HotKey). Lập danh mục: `python tools/lap_danh_muc.py <aqdata> --lien-ket trich-ma-view.txt --ra
  .claude/skills/giaodien-edusoft/man-hinh`; `trich-ma-view.txt` từ `trich_source.py <source.zip> --ma-view
  aqdata\aq.data046-AQDMView1.csv` (lớp màn hình → MaView1).
  Tiêu đề lưới / nhãn cột: `AQValSetV`+`AQValSetV1` – (1,14) = tiêu đề lưới (chữ sau `@`), (2,14) = nhãn cột đã đổi, (2,16) = độ
  rộng. Phần trường tự chỉnh (bảng `H…`: HMenuCustom, HValSetV/1, HFieldView2, HFieldEdit…): `tools/xuat_tuy_chinh_truong.sql` (sqlcmd, chỉ đọc).
  Nối menu → lưới: `AQViewAddCtrl.Method` / `AQViewMethod.TenMethod` dạng "Assembly,Lớp,Hàm" chứa đúng lớp màn hình của lưới
  (vd btnSave "Lưu quyết định" của S-DS-QUYETDINH gọi `Edusoft.SMS.S02.UCQDSV`), cộng `trich-ma-view.txt` từ source; còn lại
  ghi "đoán theo tên" (TenView1 = tên menu) – phải kiểm lại bằng `ui-*.txt`.
  **HVNG tự chỉnh rất ít** (CSDL backup 11/2026): HMenuCustom 117 dòng chỉ cho menu Edusoft web (ẩn/hiện, đổi tên trên web);
  HValSetV ~1 070 dòng gần hết là độ rộng cột (2,16), chỉ 1 nhãn cột đổi (NhomTo → "Lớp tín chỉ"); HFieldView2/HOrderView = thứ
  tự/khóa cột theo cấp người dùng (UserLevel 512/1024/2048/65536). → Danh mục gốc AQ dùng được cho HVNG bản desktop.
  Xem một đoạn source: `trich_source.py … --dong "đường/dẫn/File.cs:đầu-cuối"` (dòng giống khóa/mật khẩu/máy chủ nội bộ bị che).
- **Câu thông báo thật** nằm ở `Resources\Languages.xml` của bản cài (~14 000 mục `ID → câu`, vd `XOA_DU_LIEU_THANH_CONG` =
  "Xóa dữ liệu thành công", `M_THOAT` = "Thoát khỏi chương trình?", `CAPNHAT_THONGTIN_THANHCONG` = "Cập nhật mẫu tin {0} thành công").
  Phần hay gặp đã trích ở **`thong-bao.md`** cạnh file này – dùng khi viết `expect:` và khi sửa `ERR_PAT`/`OK_PAT` của kit.
- Hộp chọn dùng chung (`AQViewers/Controls`): `F_ChonNHHK` (chọn năm học-học kỳ), `F_NhapNgay`/`F_Nhap2Ngay`, `F_NhapMa`,
  `F_NhapNumber`, `F_NhapTextDon`, `UCGridChon`; nhập Excel: `AQViewers/Import` (`FormXuLyImport`, `FormResultImport`…).

### Phím tắt Edusoft hay dùng khi test (người dùng dạy)
- **Ctrl+Shift+T** (nhấn TRƯỚC khi mở menu): Edusoft hiện **thời gian mở form** – dùng cho case "mở menu / form lâu". Kit: lệnh `menu_time:`
  tự nhấn, mở menu, đọc chữ thời gian (hộp thông báo / thanh trạng thái / tiêu đề), chụp `thoi-gian-mo-form.png`, đóng hộp bằng OK/Đóng.
- **Ctrl+Shift+E**: chi tiết lỗi EX · **Ctrl+Shift+F**: menu code.
