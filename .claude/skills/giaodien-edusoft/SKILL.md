---
name: "giaodien-edusoft"
description: "Nhận diện giao diện Edusoft.NET (HVNG): phân biệt phân hệ, menu, chức năng, ô tìm kiếm, button, lưới dữ liệu, popup, thanh học kỳ… theo cách người dùng dạy; dùng khi viết/sửa lệnh `auto` của kịch bản, đọc file ui-*.txt hay ảnh chụp màn hình Edusoft, hoặc khi người dùng dạy thêm về giao diện. Kiểu màn hình và thao tác theo tài liệu HDSD từng phân hệ ở thao-tac.md."
---

# Giao diện Edusoft – cách nhận diện phần tử

Skill này là **sổ tay do người dùng dạy**. Mọi điều người dùng chỉ về màn hình Edusoft được ghi vào đây và
**bắt buộc áp dụng** cho các lần sau (viết `auto` trong kịch bản, sửa `kit/aqrun.py`, đọc `ui-*.txt`, xem ảnh chụp).

Thứ tự ưu tiên khi có mâu thuẫn: **Bài học người dùng dạy (mục 4)** > bảng phần tử (mục 2) > suy đoán từ tài liệu.
Ảnh minh hoạ người dùng gửi nằm ở `anh/` cạnh file này – mở bằng Read khi cần so lại.

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

## 5. Quy trình khi được dạy

1. Nhận ảnh chụp / mô tả / file `ui-*.txt`; hỏi lại nếu chưa rõ phần tử nằm ở đâu. Lưu ảnh vào `anh/`.
2. Ghi bài học vào mục 4, cập nhật bảng mục 2 (và sơ đồ mục 1 nếu là vùng mới).
3. Nếu bộ test phải nhận diện khác đi → sửa `kit/aqrun.py` (tăng `KIT_VERSION`), cập nhật docstring `Run.do_actions`.
4. Rà các kịch bản `scriptReady` (`data/scenarios/`) có dùng phần tử đó → sửa `auto` (cả `data/` và DB artifact).
5. Commit + push, cập nhật artifact nếu console thay đổi (theo CLAUDE.md).
