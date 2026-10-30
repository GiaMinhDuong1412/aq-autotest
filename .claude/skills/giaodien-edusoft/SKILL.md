---
name: "giaodien-edusoft"
description: "Nhận diện giao diện Edusoft.NET (HVNG): phân biệt button, ô tìm kiếm, ô nhập, lưới, cây menu, ribbon, hộp thoại… theo cách người dùng dạy; dùng khi viết/sửa lệnh `auto` của kịch bản, đọc file ui-*.txt hay ảnh chụp màn hình Edusoft, hoặc khi người dùng dạy thêm về giao diện."
---

# Giao diện Edusoft – cách nhận diện phần tử

Skill này là **sổ tay do người dùng dạy**. Mọi điều người dùng chỉ về màn hình Edusoft được ghi vào đây và
**bắt buộc áp dụng** cho các lần sau (viết `auto` trong kịch bản, sửa `kit/aqrun.py`, đọc `ui-*.txt`, xem ảnh chụp).

Thứ tự ưu tiên khi có mâu thuẫn: **Bài học người dùng dạy (mục 4)** > bảng phần tử (mục 2) > suy đoán từ tài liệu.

## 1. Khung màn hình (đã biết)

| Vùng | Mô tả | Loại UIA | Cách bộ test thao tác |
|---|---|---|---|
| Cửa sổ đăng nhập | Ô tài khoản/mật khẩu, nút Đăng nhập | `Edit`, `Button` | `set_field` gõ phím thật |
| Ribbon | Thẻ trên cùng: Hệ thống, Sinh viên… | `TabItem` | `select()` |
| Nút ribbon | Nút lớn trong thẻ, vd "Sinh viên học kỳ" | `Button` / `SplitButton` | bấm |
| Cây "Danh mục chức năng" | Bên trái; nút tên `NodeN`, **chữ nằm ở Value** | `TreeItem` | nhóm: mở (ExpandCollapse / phím →); mục cuối: bấm đúp |
| Màn hình chức năng | Mở trong **tab MDI** ở giữa | `Pane` / `TabItem` | – |
| Hộp thoại | Cửa sổ riêng (xác nhận, thông báo, form con) | `Window` | tìm trên mọi cửa sổ, **không tự bấm Có/Yes** trừ lệnh xóa đúng mã test |

## 2. Bảng phần tử

Trạng thái: **✔ người dùng xác nhận** · **? suy đoán, chờ dạy**.

| Phần tử | Trạng thái | Loại UIA / lớp DevExpress | Dấu hiệu nhận biết | Lệnh `auto` |
|---|---|---|---|---|
| Button (Thêm, Sửa, Xóa, Lưu…) | ? | `Button` | – | `click:` / `save:` |
| Ô tìm kiếm (search bar) | ? | `Edit` | – | – |
| Ô nhập (text) | ? | `Edit` (DevExpress TextEdit) | nhãn bên trái hoặc phía trên | `type:` |
| Ô chọn (combobox / lookup) | ? | `ComboBox` / `Edit` | – | `select:` |
| Ô ngày | ? | `Edit` (DateEdit) | – | `date:` |
| Checkbox | ? | `CheckBox` | – | – |
| Lưới dữ liệu (grid) | ? | `Table` / `DataGrid`, ô `DataItem` | – | `find_row:`, `expect:`, `pick:`, `unique:` |
| Lưới dọc (nhãn trái – giá trị phải) | ? | nhãn `Text`/`DataItem`, ô chỉ hiện khi bấm | – | `type:` (gõ theo vị trí bên phải nhãn) |
| Thanh công cụ màn hình | ? | `ToolBar` / `Button` | – | `click:` |

Khi người dùng dạy một phần tử: đổi trạng thái sang ✔, điền dấu hiệu nhận biết, và ghi chi tiết ở mục 4.

## 3. Đọc `ui-*.txt` (cây UI Automation bộ test ghi khi dừng)

Mỗi cửa sổ bắt đầu bằng `=== CỬA SỔ: <tiêu đề> [<lớp>] <toạ độ>`, sau đó mỗi dòng một phần tử:

```
loại | tên (window_text) | automationId | lớp | toạ độ (L,T,R,B) | giá trị (Value)
```

- Tên trống mà có Value → bộ test vẫn tìm theo Value (cây chức năng, ô lưới).
- Lớp DevExpress (vd `TextEdit`, `LookUpEdit`, `DateEdit`, `GridControl`, `SimpleButton`) giúp phân biệt loại
  khi `loại` chung chung (`Pane`, `Custom`). Ghi lớp đã thấy vào mục 2/4.
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

_(chưa có bài học)_

## 5. Quy trình khi được dạy

1. Nhận ảnh chụp / mô tả / file `ui-*.txt`; hỏi lại nếu chưa rõ phần tử nằm ở đâu.
2. Ghi bài học vào mục 4, cập nhật bảng mục 2.
3. Nếu bộ test phải nhận diện khác đi → sửa `kit/aqrun.py` (tăng `KIT_VERSION`), cập nhật docstring `Run.do_actions`.
4. Rà các kịch bản `scriptReady` (`data/scenarios/`) có dùng phần tử đó → sửa `auto` (cả `data/` và DB artifact).
5. Commit + push, cập nhật artifact nếu console thay đổi (theo CLAUDE.md).
