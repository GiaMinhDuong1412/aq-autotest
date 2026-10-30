# Thao tác Edusoft theo tài liệu hướng dẫn sử dụng (HDSD)

Nguồn: thư mục người dùng gửi 2026-10-30 – SharePoint site **aq** › `Shared Documents/1. Tài liệu EduSoft`
(drive `b!_q43g_7qMkCtqPMMMYGO7sBXTyNP3u1OplVIrVvsLn6LvWDMxyCqS6GtCAzLxjBx`). Đọc bằng `read_resource`
`file:///<drive>/<itemId>`, giới hạn `startPage`/`endPage` (file .doc lớn tới 13 MB). Connector chỉ trả **chữ** –
ảnh chụp màn hình trong tài liệu không lấy được; muốn thấy giao diện thật thì chạy kịch bản khảo sát (mục 3).

Thư mục con: `DOC` (tài liệu theo phân hệ, ~575 MB), `PDF`, `Video HDSD` (video .mp4 – không đọc được),
`QuiTrinhMotTrangViSio`, `aq.edusoft.net` (zip mã nguồn – không đọc), `LuuDo_Lark`.

## 1. Kiểu màn hình và thao tác chuẩn (rút ra từ tài liệu, đối chiếu skill mục 1–2)

| Kiểu | Nhận biết trong tài liệu | Thao tác chuẩn | Lệnh `auto` gợi ý |
|---|---|---|---|
| **Danh mục** (lưới + khung chi tiết) | "chọn **Thêm** và nhập thông tin tại **detailright**", "import từ file" | Thêm → nhập ở khung chi tiết **bên phải** lưới → Lưu; hoặc Import | `click: Thêm` → `type:`… → `save: Lưu` |
| **Quyết định** (đầu quyết định + danh sách SV) | "nhập thông tin Số quyết định, Lý do, Ngày lập/ký, Ngày hiệu lực, **Người ký**"; "tại view **Danh sách sinh viên quyết định** chọn Thêm để chọn từng sinh viên hoặc Import" | Thêm (quyết định) → nhập đầu QĐ → Thêm (sinh viên, nút thứ hai ở view danh sách) hoặc Import → Lưu. Lý do lấy từ danh mục lý do, người ký từ danh sách người ký | `click: Thêm` … `click: Thêm` (lần 2, trong view danh sách SV) |
| **Cập nhật theo mã SV** | "nhập mã sinh viên, sau đó cập nhật các thông tin… trong các **tab** Lý lịch, Liên lạc, Gia đình…" | Gõ mã SV (Enter) → thông tin tải lên → sửa trong từng tab → Lưu | `type: Mã sinh viên = …` → `key: {ENTER}` |
| **Chọn lớp → Tiếp tục** | "Chọn lớp cần gán và chọn **Tiếp tục**" | Chọn lớp → Tiếp tục → danh sách SV tải lên → nhập trên lưới → Lưu | `select: Lớp = …` → `click: Tiếp tục` |
| **Nhập trên lưới** | "nhập trực tiếp tại các dòng dữ liệu", "chọn tại cột Mã CVHT", "click vào cột giá trị (hoặc dấu …)" | Bấm ô của **cột xám** (skill #7) → gõ/chọn → Lưu | (chờ dạy: lệnh gõ vào ô lưới) |
| **Import từ file** | "tool import mở lên… chọn **Xuất cấu trúc**" (ra Excel mẫu) → chuẩn bị dữ liệu → đưa file vào | Không tự động hoá (cần file ngoài) – chỉ kiểm tra màn hình mở và nút Xuất cấu trúc có | `expect: Xuất cấu trúc` |
| **Đồng bộ / Thực hiện** | "thực hiện chức năng **Đồng bộ**", "chọn khối và chọn **Thực hiện**", các **nhiệm ý** (lựa chọn) như "Đồng bộ SV có thay đổi" / "Đồng bộ tất cả (xóa hết…)" | Chọn nhiệm ý + bộ lọc (bậc hệ, đợt, khối) → Thực hiện/Đồng bộ → thông báo | ⚠ thay đổi dữ liệu hàng loạt – **hỏi người dùng** trước khi đưa vào kịch bản; tuyệt đối không chọn nhiệm ý "xóa hết" |
| **Báo biểu / In** | "chọn **nhiệm ý**: in từng SV / theo lớp / theo file… chọn **In**, chương trình xuất mẫu in ra màn hình" | Chọn nhiệm ý + dữ liệu → In → cửa sổ xem in (report) → kiểm tra rồi đóng cửa sổ in | `click: In` → `expect_dialog:` / `shot:` |
| **Chỉnh định thông số** | "Quản trị phân hệ / Chỉnh định thông số học kỳ/toàn cục", "tìm và chọn nhiệm ý `GS_…`/`SS_…`", "click cột giá trị hoặc dấu …" | Lưới tham số: tìm mã tham số bằng ô tìm kiếm → sửa cột Giá trị → Lưu | ⚠ ảnh hưởng toàn hệ thống – chỉ xem, không sửa khi test |
| **Hộp chọn thư mục/file Windows** | "bấm **Chọn**, trỏ đường dẫn… chọn OK" (Import ảnh) | Hộp thoại Windows – ngoài Edusoft | không tự động hoá |

Quy ước chung trong tài liệu: đường dẫn menu viết `Phân hệ / Menu / Nhóm / Chức năng` (đúng cách `menu:` dùng);
đầu quy trình luôn là **Đăng nhập → chỉnh "Niên học học kỳ"** (thanh học kỳ, skill #9); trường bắt buộc **tô đỏ**
("thuộc tính đã đánh dấu đỏ"); nút lưu luôn tên **Lưu**.

## 2. Ghi chú theo phân hệ

### QLSV (`DOC/QLSV`, đã đọc 2026-10-30)
- **QĐ vào/ra** (`QLSV_CapNhatQuyetDinhVaoRa`): danh mục tiền đề ở `Sinh viên/Sinh viên học kỳ/QĐ vào/ra sinh viên/`:
  *Danh mục lý do quyết định*, *Danh mục tên quyết định*, *Danh sách người ký quyết định*. Các quyết định: học lại, đổi lớp,
  nghỉ học, tạm dừng (nhập thêm **số học kỳ tạm dừng**), tốt nghiệp – cùng mẫu "Quyết định" (mục 1). Import SV: cột
  `Masv`, `MaLopMoi`, `MaLopCu`. Đổi lớp: chọn **Mã lớp mới** (cột đỏ) trên danh sách SV.
  → QLSV-001 có thể thiếu **Người ký** và **Tên quyết định**; khung nhập SV là *view Danh sách sinh viên quyết định*
  (nút Thêm thứ hai) – xác nhận bằng KS-QLSV-001 trước khi sửa `auto`.
- **Lý lịch** (`QLSV_CapNhatLyLichSinhVien`): `Sinh viên/ Thông tin sinh viên/ Cập nhật lý lịch sinh viên` (gõ mã SV, tab
  Lý lịch/Liên lạc/Thông tin vợ chồng/Hồ sơ, Lưu); *Cập nhật lý lịch SV từ file* (Xuất cấu trúc); *Import ảnh sinh viên*
  (Chọn thư mục, tên ảnh = mã SV, ≤200 KB); *Cập nhật thông tin nội trú/ngoại trú* (mã SV → loại cư trú → chủ hộ → Lưu);
  báo biểu *In lý lịch sinh viên* (nhiệm ý: từng SV / lớp / file), *In thông tin ngoại trú*, *In DSSV theo loại cư trú*.
- **Hồ sơ – văn bằng** (`QLSV_QuanLyHoSoVanBangSinhVien`): `Sinh viên/ Hồ sơ và văn bằng/ Hồ sơ sinh viên/` *Danh mục hồ sơ*
  (Thêm + detailright), *Cập nhật hồ sơ sinh viên* (mã SV → loại hồ sơ → **Thêm hồ sơ** → Lưu), *Cập nhật hồ sơ SV từ file*,
  *In DSSV theo tình trạng hồ sơ*, *Thống kê tình trạng hồ sơ theo lớp*.
- **Thông tin khác** (`QLSV_QuanLyThongTinKhac`): `Sinh viên/ Thông tin sinh viên/ Thông tin khác của sinh viên/ Danh sách
  sinh viên làm thêm`; `…/ Sinh viên vi phạm pháp luật/ Danh sách sinh viên nghiện`, `Xử lý sinh viên liên quan ma túy` – Import hoặc Thêm từng SV.
- **Tốt nghiệp – in bằng** (`QLSV_CapNhatThongTinTotNghiepVaInBangCNTotNghiepSV`): `Sinh viên/ Thông tin tốt nghiệp/ Thông tin
  tốt nghiệp/ Đồng bộ danh sách tốt nghiệp` (nhiệm ý *Đồng bộ SV có thay đổi* / ⚠ *Đồng bộ tất cả – xóa hết*; lọc bậc hệ, đợt),
  *Cập nhật thông tin tốt nghiệp* (nhập trên lưới: Số vào sổ, Ngày vào sổ, Ngày cấp…; "Cập nhật theo file"); *In chứng nhận /
  In bằng tốt nghiệp*: 1 SV (chọn mã SV → In), 1 số SV trong lớp, theo lớp, theo đợt, từ danh sách, theo file.
- **Cố vấn – chủ nhiệm** (`QLSV_CoVanHocTap`): `Sinh viên/ Cố vấn và Chủ nhiệm/ Cố vấn học tập/` *Gán mã CVHT cho toàn lớp*
  (chọn lớp, chọn ở cột **Mã CVHT**, Lưu), *Gán CVHT theo lớp* (chọn lớp → **Tiếp tục** → chọn SV → chọn cố vấn → Lưu),
  *Hủy mã CVHT cho toàn lớp*, *Gán CVHT cho toàn trường*, báo biểu *In DSSV theo CVHT*, *In thống kê theo CVHT mẫu 1/2*;
  *Chủ nhiệm lớp/ Thông tin chủ nhiệm lớp* (nhập cột **Mã viên chức**, nút In trên cùng màn hình).
- **Trợ cấp – miễn giảm** (`QLSV_TroCapXaHoi&MienGiamChinhSach`): `Sinh viên/ Miễn giảm học phí và Học bổng/ Sinh viên trợ cấp/`
  Danh mục trợ cấp (Thêm, Lưu) → Nhập tiền trợ cấp → Trợ cấp SV chung (NHHK bắt đầu/kết thúc) → Trợ cấp SV học kỳ (**Đồng bộ**)
  → In DSSV hưởng trợ cấp / In thống kê; tương tự `Sinh viên diện chính sách/` (Danh mục diện CS → Nhập % miễn giảm DCS →
  Diện CS SV chung → Diện CS SV học kỳ (Đồng bộ) → In).
- **Học bổng KK** (`QLSV_XetHocBongKhuyenKhich`): thông số `Sinh viên/ Quản trị phân hệ/ Chỉnh định thông số học kỳ`
  (`SS_SOTINCHIHBMIN`, `SS_KHOIHB`, `SS_NGUONGHB`…); `…/ Học bổng/` Danh sách khối HB học kỳ (Đồng bộ) → Định nghĩa khối HB
  (Sửa/Thêm) → Danh sách không xét HB → Kiểm tra và in SL xét HB (chọn khối → **Thực hiện**) → Xét học bổng (chọn khối →
  Thực hiện) → kiểm tra/sửa kết quả → In bảng tổng hợp.
- **Điểm rèn luyện** (`QLSV_QuanLyDiemRenLuyen`, đọc trang 1–10/14): thông số `GS_HESOTBRLNH` (Chỉnh định thông số toàn cục,
  nhóm "Điểm rèn luyện"); `Sinh viên/ Điểm danh và Điểm rèn luyện/ Quản lý điểm rèn luyện/` Danh mục phân loại, Danh sách nhóm
  câu hỏi (Mã, Tên, Thứ tự, Điểm tối đa), Danh sách câu hỏi (+ tuỳ chọn Vi phạm / Không cần minh chứng / Điểm cộng),
  Điểm rèn luyện thành phần/ Thời gian đánh giá online (theo lớp/CVHT/khoa, **Gán chung**), Thời gian đánh giá SV online,
  Kết quả đánh giá rèn luyện; `…/ Điểm rèn luyện/ Nhập điểm rèn luyện` (chọn lớp, nhập, Lưu), Import điểm rèn luyện.
- **Khen thưởng – kỷ luật** (`QLSV_KhenThuongKyLuatSV`, đọc trang 1–10/24): `Sinh viên/ Khen thưởng và kỷ luật/` Danh mục cấp
  KT/KL (Mã cấp, Tên cấp), Danh mục lý do KT/KL (Mã KT, Tên, **phân loại**: khen thưởng SV / tập thể lớp / kỷ luật / cảnh báo
  học vụ, Mã cấp), Quyết định kỷ luật / cảnh báo học vụ / khen thưởng (mẫu "Quyết định": Thêm → Số QĐ, lý do, ngày ký →
  view *Danh sách sinh viên quyết định*: Thêm từng SV hoặc Import → Lưu).

## 3. Kịch bản khảo sát giao diện (chỉ xem)

`KS-QLSV-001` (`data/scenarios/es-ks-qlsv-001.json`): mở lần lượt các màn hình của QLSV-001, mỗi màn hình `wait` → `shot` →
`dump` (ảnh + `ui-ks-*.txt`), cuối cùng bấm Thêm ở Quyết định vào mới để xem khung nhập rồi `cancel` (không lưu). Người dùng
chạy như kịch bản thường, nhập file kết quả vào console → đọc ảnh/`ui-ks-*.txt` để ghi bài học vào SKILL.md và sửa `auto`.
Dùng cùng mẫu cho phân hệ khác (KS-<PHÂN HỆ>-nnn) – chỉ các lệnh `menu/wait/shot/dump/click Thêm/cancel`.

## 4. Tiến độ đọc (đọc tiếp từ dòng chưa ✔ khi được cấp lại token)

Thư mục `DOC/<phân hệ>` – URI `file:///b!_q43g_7qMkCtqPMMMYGO7sBXTyNP3u1OplVIrVvsLn6LvWDMxyCqS6GtCAzLxjBx/<id>`:

| Phân hệ | id thư mục | Trạng thái |
|---|---|---|
| QLSV | 01JIVIL26IDOTNMXB6R5AK2RFX7CBKPE7P | ✔ 10/15 file (chưa: CNTN địa chỉ địa bàn, BaoHiemSinhVien, CapVaInGiayChungNhan, MoHinhNganhHai, QuanLyDoanThe; KTKL & ĐRL mới đọc 10 trang đầu) |
| DIEM | 01JIVIL263FQ5TKUJF7VALQIEOIRFOUEOP | chưa |
| DKMH | 01JIVIL23FVN6KAQGK5BFKVXAO5L3HJQAM | chưa |
| DKPH | 01JIVIL26OUD65NPMAARDZT3VRFOQPONV6 | (trống) |
| DTNH | 01JIVIL2Y75MTWEHIJBVDY7KSFQGDY3TEJ | chưa |
| EDUBILL | 01JIVIL27SUQIV46TQXRFI6TJTOZEWIRZC | chưa |
| EDUGO | 01JIVIL24POBSOMZ4DXRBJZULF6QMVPWCG | chưa |
| HDCD | 01JIVIL26QDBVJOBQ7IBGZDVLIZG467V7I | chưa |
| KLGD | 01JIVIL23SIWF6FVUSB5DYICVDC76FM6LK | chưa |
| KSDG | 01JIVIL23VTP5RTLEXN5DIQXRBEO5MY754 | chưa |
| KHGD | 01JIVIL27FYXEJ7WKK2RGLD6BQFQXZONE6 | chưa |
| LTHI | 01JIVIL27JNTQNSLUICVGZAMQIEGFFPMIV | chưa |
| NCKH | 01JIVIL23TYE5WMCTTAJDJTUISTTAED5S5 | chưa |
| NETWEB | 01JIVIL27XZPAGII4UNZB32ICOMQAT5QR3 | chưa |
| NhapHocOnline | 01JIVIL26PKOJKV4IRFRC3FBYQU6HRRF37 | chưa |
| PVLD | 01JIVIL277JCFDE6XD4FD3DOHIKVLZT43W | chưa |
| QKTX | 01JIVIL23UP4VLXDVFNZA34YCAAIETI72R | chưa |
| QLHT | 01JIVIL2YBBBHJR5VOZVEJISJQBDNDUIQH | chưa |
| QLNS | 01JIVIL27SGGNAPANWCJEYAOKOLTSU6MJC | chưa |
| QLTN | 01JIVIL27KH3CQCJANQVCIZ5WQBMEAQQQT | chưa |
| QLTS | 01JIVIL27LMGH6MASHVZBJ75MLQ3N6B5QT | chưa |
| QLTV | 01JIVIL26KV7EA5BJFNFCZKVXLJ2UZOHMU | chưa |
