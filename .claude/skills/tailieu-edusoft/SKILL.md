---
name: "tailieu-edusoft"
description: "Tra cứu tài liệu Edusoft.NET/Netweb trên SharePoint AQTech, lập danh mục kế hoạch test theo phân hệ, dựng kịch bản test, chạy test qua máy chạy thử và quản lý test menu theo phiên bản release."
---

> **Trong dự án aq-autotest (Claude Code / localhost):** dữ liệu console nằm ở `data/<collection>/<doc_id>.json`
> (mỗi bản ghi một file, JSON sắp xếp khoá) thay cho tool `ArtifactData`. Đọc/sửa trực tiếp các file đó
> (hoặc qua API `server.py` khi server đang chạy); ảnh ở `data/assets/<id>.<đuôi>`; dữ liệu riêng
> (mật khẩu Netweb) ở `local/` – không bao giờ đưa lên git. Đọc tài liệu SharePoint cần connector
> Microsoft 365 (có trong Claude app); trong Claude Code không có thì nhờ người dùng tải tài liệu về
> thư mục `docs/` hoặc làm phần đó trong Claude app.


# Tài liệu Edusoft

Kho tài liệu hướng dẫn sử dụng chính thức của AQTech (Anh Quân Technology) cho Edusoft.NET, Netweb và các sản phẩm liên quan. Dùng skill này để: (1) tìm và đọc đúng tài liệu, (2) trả lời câu hỏi nghiệp vụ/menu, (3) dựng kịch bản test từ tài liệu, chia theo phân hệ, kèm luồng dữ liệu, và lưu vào AQ Autotest Console, (4) kiểm tra khởi động trên máy chạy thử, ghi lượt chạy (ảnh từng bước), kết quả và lỗi khi chạy test thật, (5) lập danh mục kế hoạch test cho từng phân hệ và quản lý test menu theo phiên bản release.

## Nguồn
- SharePoint site `sp`, thư mục: `ALL DOCS/1. Tài liệu Edusoft`
- Link người dùng: https://aqtechltd.sharepoint.com/:f:/s/sp/IgCVWy-N4j4TRZgKax9lIX2EAfCZWGr61gqVBiSBTMmPKXM?e=jIrm51
- Đọc qua connector **Microsoft 365** (`mcp__Microsoft_365__read_resource`, nạp bằng ToolSearch nếu đang deferred). Không dùng WebFetch cho link SharePoint.
- Drive ID: `b!iaQbxnpRT0SXpVqLO5GlLFFAMzDJfJpFlptKuWOfRPGHrbxW2p9BS5IdeX3dHprv`
- URI thư mục gốc: `file:///b!iaQbxnpRT0SXpVqLO5GlLFFAMzDJfJpFlptKuWOfRPGHrbxW2p9BS5IdeX3dHprv/ALL DOCS/1. Tài liệu Edusoft`
- Lưu ý: site `aq` có một bản cũ khác (`1. Tài liệu EduSoft/DOC`, `/PDF`). Mặc định dùng bản site `sp` ở trên.

## Cách đọc
1. Liệt kê thư mục phân hệ: `read_resource` với `file:///<driveId>/<folderId>` (bảng dưới). Kết quả trả về tên file + URI từng file. Danh sách có thể đã thay đổi, luôn liệt kê lại trước khi đọc.
2. **Ưu tiên bản .docx / .doc**: bản PDF khi trích xuất hay bị tách dấu tiếng Việt (vd "Kh ố i lư ợ ng"). Chỉ dùng PDF khi không có bản Word, hoặc khi file Word lớn (> ~6 MB, nhất là `.doc`) trả về "Reading this file's text took too long" — khi đó đọc bản PDF cùng tên (vẫn đọc hiểu được dù dấu bị tách).
3. Tài liệu dài: đọc theo trang bằng `startPage`/`endPage` (trang 2–3 thường là MỤC LỤC, đọc trước để nhảy đúng mục).
4. Loại file:
   - `<PH>_<TenChucNang>.docx/.pdf`: hướng dẫn quy trình.
   - `*_LuuDo.pdf`: lưu đồ quy trình của tài liệu cùng tên.
   - Thư mục `QuiTrinhMotTrangViSio`: sơ đồ quy trình 1 trang và **cây menu theo phân hệ** (`*_menu.pdf`, vd `KLGD_menu.pdf`, `DIEM_menu.pdf`, `TKB_menu.pdf`) — dùng để lấy đúng đường dẫn menu và thứ tự luồng dữ liệu.

## Cấu trúc chuẩn mỗi tài liệu
- Bìa: "TÀI LIỆU HƯỚNG DẪN SỬ DỤNG – ANH QUÂN Technology", tên quy trình, câu mô tả "…trên hệ thống EDUSOFT.NET".
- MỤC LỤC.
- **I. PHÂN TÍCH**: mục đích nghiệp vụ.
- **II. TÓM TẮT QUY TRÌNH CHÍNH**: danh sách bước lớn.
- **III. QUY TRÌNH CHÍNH**: từng bước đánh số, mỗi bước có dòng `Menu: A/ B/ C/ D` (đường dẫn menu trong app), thao tác (Thêm / Sửa / Xóa / Lưu / Import / Thực hiện), các trường bắt buộc và ý nghĩa, kết quả chương trình trả về.
- Nhiều quy trình yêu cầu **chỉnh định thông số** trước (biến dạng `SG_...`/`SM00_...` tại `<Phân hệ>/ Quản trị phân hệ/ Chỉnh định thông số toàn cục|học kỳ`) và **danh mục** (`<Phân hệ>/ Quản trị phân hệ/ Quản lý danh mục/ …`). Đây là điều kiện đầu vào của kịch bản test, và các biến dạng "Cấm…/ Cho phép… khi…" là nguồn luồng thay thế.

## Mục lục 23 phân hệ
URI thư mục = `file:///b!iaQbxnpRT0SXpVqLO5GlLFFAMzDJfJpFlptKuWOfRPGHrbxW2p9BS5IdeX3dHprv/<folderId>`. Cột "Menu app" là tab trên thanh menu Edusoft.NET.

| Mã | Phân hệ | Menu app | folderId | Tài liệu chính |
|---|---|---|---|---|
| QLHT | Quản lý hệ thống | Hệ thống | 017YGNGYQVILLRYB7ZBJEYGBGCOPP3BKB3 | TaoTaiKhoanVaPhanQuyenNguoiDung, PhanQuyenQuanTriTrenWeb, HuongDanNghiepVuPhanQuyenDuLieuTheoKhoa, ThongTinHocKy, KhoaSoDuLieu, ThaoTacDanhMuc, ThaoTacBieuIn, HuongDanImport, HuongDanChinhDinhView, ChinhDinhTienTrinhTuDong, SongNguAnh-VietTrenBaoBieu, TruyVetDuLieu, NETWEB-QuanTriChung |
| QLNS | Quản lý nhân sự | Nhân sự | 017YGNGYUBT5D6TV7MDZFKSS7M6QU2PES4 | QuanLyLyLichCBCNV, CapNhatQuyetDinhVaoRaCBCNV, QuyTrinhTuyenDungHopDong, QuanLyHocHamHocVi, QuanLyTrinhDoChuyenMon, QuanLyVanBangChungChi, QuanLyDoanTheChucVu, QuanLyCongTacPhep, QuanLyDanhSachNghiThaiSan, QuanLyDaoTaoVienChuc, QuanLyThongTinBaoHiem, QuanLyThongTinYTe, ThucHienKhenThuongKyLuat, ThucHienPhanLoaiGiangVienNghiepVu, KhoiLuongGiangDay |
| KHGD | Kế hoạch giảng dạy / TKB | Kế hoạch | 017YGNGYS6JIT66SMRLJGIZJ4TDZR2WXBJ | QuanLyCTDT3Cap, KhoaDuLieuCTDT, CacBuocXepTKB, DinhNghiaThoiGianDungTrongTKB, PhanQuyenXepTKBTheoKhoa, QuanLySuDungPhongHocVaGiangDuong, SuDungPhongDotXuatVaTimKiemPhongRanh, QuanLyNghiDayVaDayBu, HuongDanDangKyNghiDayVaDayBuOnline, ChamCongGiangDay, QuanLyNhanSuCoBan |
| KLGD | Khối lượng giảng dạy | Khối lượng | 017YGNGYRL4KM2YUU46RHIMG7DIBNLPFIZ | QuanLyKhoiLuongGiangDay (36 trang) |
| QLTS | Quản lý tuyển sinh (+ thư mục con NhapHocOnline) | Tuyển sinh | 017YGNGYVFDKFBT4VQCJCK5ABPHG77XV7K | 1_ChuanBiDuLieuTuyenSinh, 2_ChuanBiCacDanhMucTuyenSinh, 2_GanMaLop_GanMaSV, 3_ChamSocThiSinhXetTuyenTrucTuyen, 4_GanMaLop_GanMaSV_InGiayBaoTrungTuyen, QuyTrinhThucHienToChucThi, QuyTrinhXetTuyenVaTiepSinh, NetWEB_NhapHocOnline, ThiSinh_NhapHocOnline |
| QLSV | Quản lý sinh viên | Sinh viên | 017YGNGYSDGLUNSCJ34NAJCLQXFJBMJJSD | CapNhatLyLichSinhVien, CapNhatQuyetDinhVaoRa, CoVanHocTap, KhenThuongKyLuatSV, QuanLyDiemRenLuyen, QuanLyDoanThe, BaoHiemSinhVien, TroCapXaHoi&MienGiamChinhSach, XetHocBongKhuyenKhich, MoHinhNganhHai, CapVaInGiayChungNhan, CapNhatThongTinTotNghiepVaInBangCNTotNghiepSV, QuanLyHoSoVanBangSinhVien, QuanLyThongTinKhac, CNTN_CapNhatDiaChiDiaBanMoi |
| QKTX | Quản lý ký túc xá | Ký túc xá | 017YGNGYXXSHDXZ4MRSJBLGPS3XTT5QLUJ | QuanLyPhongTang, DangKyTrucTuyen_GiaHan, XetDuyetHopDongKTX, ThongTinLuuTru, ThongTinVaoRa_CapTheKTX, ChiSoDienNuocTheoPhong, ThanhToanKTX |
| DKMH | Đăng ký môn học | Đăng ký MH | 017YGNGYTCX3BDY2AYQNGKH3NYLLW65TM4 | DinhNghiaMonTienQuyet, ChinhDinhThoiGianDangKyOnline, HuongDanDangKyMonHocOnline, DangKyMonHocOFFLINE (docx 017YGNGYSVKKVIAFH6VRH2KZDUGC5FVOBP), DangKyMonHocTuFileSV-MH, RutMonHoc |
| LTHI | Lịch thi / tổ chức thi | Tổ chức thi | 017YGNGYTQLZB3CXJTQFFZBB5ALAS3D2LX | ToChucThi, PhanCongCoiThi |
| QLTV | Quản lý thu học phí | Chính sách HP, Thu/chi HP | 017YGNGYRRM3LDC263IJDZDV67FTBAYC22 | KhaiBaoChinhSachThuHocPhi, QuanLyCacKhoanThuTuDinhNghia, PhanBoHocPhiTuDinhNghia, ThuHocPhiTheoPhieuBao, QuanLyDuNoThoiDiemCanThiet |
| DIEM | Quản lý điểm | Quản lý điểm, Quản lý nhập điểm | 017YGNGYQPTS26ZBMGKREZBW3VLDN7WZDP | ChinhDinhQuanLyDiem (+ bản TT56), QuanLyMonModun, DinhNghia&InBangDiem, DinhNghiaBangThanhTichHocTap, PhanQuyenNhapDiem, QuanLyNhapDiem, KiemDoDiemTaiManHinhNhapDiem, ImportDiemDangExcel, QuanLyPhach, QuanLyPhucKhao, QuanLyHoSoDiem, XuLyHocVu, XetChungChi, QuanLyTotNghiep_XetDuThi_LuanVan_TienTotNghiep |
| QLTN | Quản lý tốt nghiệp | Tốt nghiệp | 017YGNGYREF4C6NAVNDRBIXCB7YCYP57DB | QuanLyQuaTrinhThucHienLuanVanTN, DIEM_QuanLyTotNghiep |
| KSDG | Khảo sát đánh giá | Khảo sát đánh giá | 017YGNGYQ2R33VS6ILH5B36JVJIOEKETEU | QuyTrinhKhaoSat |
| NCKH | Nghiên cứu khoa học | NC khoa học | 017YGNGYRFFNKVE5BFDVEK6GHKCKCSQF2Y | NhapDuLieuCuaGiangVien |
| SAE | Hoạt động ngoại khóa / điểm rèn luyện | Hoạt động cộng đồng | 017YGNGYS6RRJLPTYGSNF2BQ6H6ER5IJUS | Hoạt động ngoại khóa-SAE, Hướng Dẫn Sử Dụng SAE, Hướng Dẫn Tính Tự Động Điểm Rèn Luyện-DHNT |
| DTNH | Đào tạo ngắn hạn | — | 017YGNGYT4WG32RENCSJEJLG6Y7LXPCMK4 | QuanLyDaoTaoNganHan |
| PVLD | Thông tin quản lý hỗ trợ lãnh đạo | — | 017YGNGYXYDSGK7DZPHRC2SR63RGNSCOQE | ThongTinQuanLyHoTroLanhDao |
| HTLĐ | Hỗ trợ lãnh đạo (bản PDF) | — | 017YGNGYTHSK7FWDPO35F2F4RBZGPXSKGI | PVLD_ThongTinQuanLyHoTroLanhDao.pdf |
| NETWEB | Cổng Netweb (SV, GV, phụ huynh, khách, quản trị) | web | 017YGNGYSOX4YE7N5RLZF25JHS6LYR6UD4 | QuanTriChung, TaiLieuHuongDanSinhVien, SinhVienXemThongTinCaNhan, SinhVienQuenMatKhau, SinhVienKhaoSatDanhGia, NhapLyLichSVTrucTuyen, HuongDanUploadHoSoLyLichSV, NhapDRLTrucTuyen, QuanLyDonTuTrucTuyen, XemKetQuaXetTotNghiep, GiangVienXemThongTinCaNhan, GiangVienNhapDiemOnline, GiangVienDuyetKQDK, GiangVienDiemDanhSVTrucTuyen, DiemDanhBangQr, GiangVienXemKhaoSatDanhGia, HuongDanDangKyNghiDay_DayBuOnline, PhuHuynh, Guest_TraCuuLuanVan_VanBangChungChi, ChamSocThiSinhXetTuyen |
| EDUGO | App di động AQ EduGO | app | 017YGNGYQMA2EJANORLBH3YTFYXUN5GCX3 | EDUGO_HuongDanSuDungChung, AQ EduGO_HuongDanSuDung_GiangVien, AQ EduGO_HuongDanSuDung_SinhVien, HƯỚNG DẪN XÓA BỘ NHỚ ĐỆM, video giới thiệu (.mp4) |
| EDUBILL | Thanh toán học phí kết nối Bill | — | 017YGNGYS5HBUL7XAAYZDIKKNO24FCCF5S | MoTaQuyTrinhDongHocPhi_KetNoiBill, AQ EduBILL_HD thao tác demo theo quy trình, QUY TRÌNH KHỞI TẠO MÔI TRƯỜNG TEST EDUBILL |
| GAM | Hệ thống phúc tra điểm trực tuyến | web | 017YGNGYX2B26ZSMPJWZFLW6YLF7Q6VDDJ | TÀI LIỆU SỬ DỤNG - HỆ THỐNG PHÚC TRA ĐIỂM TRỰC TUYẾN.pdf |
| (sơ đồ) | QuiTrinhMotTrangViSio (+ thư mục con LuuDo_NEW) | — | 017YGNGYVQGZL7REE6DRGKPSFJSF5LGEME | *_menu.pdf/.vsdx cho BVLV, CSHP, CTDT, CThi, DIEM, KLGD, KSDG, LTHI, QLSV, QLTN, QLTSTS, QLTSXT, TKB, XetCC, XetHV, XHB; dongchay.pdf, LuuDoHeThong.pdf |

## Phân hệ trong AQ Autotest Console
Kịch bản **bắt buộc** thuộc một phân hệ (trường `module`). Chỉ dùng các mã dưới đây (mã khác rơi vào nhóm "Chưa xếp phân hệ"). Trang **Phân công release** (menu con Edusoft / Netweb) hiện các phân hệ đang được phân công, thu gọn được; mở một phân hệ thấy thẻ tóm tắt (menu release đã test, kịch bản, độ phủ danh mục) và hai tab **Menu release** / **Kịch bản test**. Danh mục kịch bản nằm ở trang riêng **Danh mục kịch bản**.
- **Edusoft** (`product: "edusoft"`): `CHUNG` (khởi động & đăng nhập), `QLHT`, `QLNS`, `KHGD`, `KLGD`, `QLTS`, `QLSV`, `QKTX`, `DKMH`, `LTHI`, `QLTV`, `DIEM`, `QLTN`, `KSDG`, `NCKH`, `SAE`, `DTNH`, `PVLD` — trùng mã thư mục tài liệu (HTLĐ xếp vào `PVLD`).
- **Netweb** (`product: "netweb"`): `CHUNG`, `QTRI` (Quản trị chung), `SV`, `GV`, `PH` (Phụ huynh), `KHACH` (Khách – tra cứu), `TS` (Tuyển sinh & nhập học online). Tài liệu nguồn trong thư mục NETWEB (và QLTS/NhapHocOnline cho `TS`): SinhVien* → SV, GiangVien*/DiemDanh* → GV, PhuHuynh → PH, Guest_* → KHACH, QuanTriChung → QTRI.
- **Mã kịch bản**: `<PHÂN HỆ>-<STT 3 số>`, vd `KLGD-001`, `DKMH-005` (không tiền tố sản phẩm; sản phẩm nằm ở trường `product`). Đánh số riêng trong từng phân hệ theo trình tự quy trình của tài liệu (trang chạy thử theo thứ tự mã).
- Kịch bản cơ bản mở app + đăng nhập Edusoft là **CHUNG-001**, đồng thời là bước kiểm tra khởi động của máy chạy thử. Kịch bản còn giữ (30/10/2026): **CHUNG-001** (`es-tc-001`) và **QLSV-001** (`es-qlsv-001`, Quyết định vào mới: thêm – sửa – xóa, mẫu cho kịch bản ghi dữ liệu). Các kịch bản KLGD/DKMH cũ đã bị xoá; dựng lại từ danh mục theo sheet.

## Danh mục kịch bản test (theo sheet release + đối chiếu tài liệu)
- **Nguồn chính là sheet release `Menu_NEW`** (file `Release(TestMenu).xlsx`, xem mục Release): người dùng ghi sẵn quy trình từng phân hệ theo thứ tự từ bước đầu đến bước cuối, **mỗi dòng menu = một hạng mục**, giữ đúng thứ tự sheet. Tài liệu SharePoint chỉ dùng để **đối chiếu** và viết các bước thao tác. Không lập danh mục từ mục lục tài liệu nữa (cách cũ sinh ~1.250 hạng mục trùng lặp, đã xoá ngày 30/10/2026).
- Mỗi phân hệ một document `testPlans/<product>-<MÃ>` (vd `edusoft-KLGD`): `{product, module, status: "draft"|"requested"|"approved", basis: "sheet", objective, docs: [{name, url}], items: [...], createdAt, createdBy, updatedAt, updatedBy}`. Mỗi hạng mục:
  - `stt` – số thứ tự toàn sheet (1…219), trang hiện ở cột #; `title` – đoạn cuối của menu (đoạn quá ngắn / "Theo…" / "Dạng…" ghép với đoạn trước; dòng Netweb lấy phần sau dấu `:` + "(Netweb <vai trò>)"); `menu` – dòng sheet bỏ ngoặc, chuẩn hoá " / " (trùng cách trang Phân công release chuẩn hoá để khớp menu release).
  - `kind` (setup cho Khai báo/Định nghĩa/Danh mục/Chỉnh định/Đơn giá…, còn lại main), `priority` (thấp cho In/Xem/Tra cứu, trung bình cho setup, cao cho nghiệp vụ), `scenarioCode`, `source: "sheet"`.
  - `docRef` = `<tài liệu>, mục <số> <tên mục>` (nhiều tài liệu cách nhau `;`); `docCheck` = `ok` (tài liệu mô tả đúng menu này) | `partial` (tài liệu có nhưng khác menu / thiếu bước) | `none` (không có tài liệu — bước dựng theo tên menu); `docNote` – chỗ lệch giữa sheet và tài liệu, rủi ro dữ liệu, "cần xác nhận".
  - `steps` – các bước thao tác để người dùng kiểm tra: mở menu → thao tác (dữ liệu `TEST_…`) → `KIỂM TRA: …` sau mỗi lần ghi → `Dọn: …`; chỉnh định dùng chung ghi "chỉ xem (không sửa)". Trang hiện "Thao tác n bước" (bấm mở), lọc "Mọi mức đối chiếu", sửa được trong form hạng mục (mỗi dòng một bước). Nút "Claude dựng kịch bản" đưa `steps`/`docNote` vào prompt.
  - Dòng `NetWEB …` nằm trong khối phân hệ Edusoft giữ ở kế hoạch Edusoft đó, thêm `product: "netweb"` (thẻ "Netweb"); khi thêm vào release thành menu Netweb (`product: "netweb"`, `group` = phân hệ). Khối `#NETWEB` cuối sheet vào kế hoạch Netweb theo vai trò: `netweb-QTRI` (ADMIN), `netweb-CHUNG` (góp ý, thông báo, quên/đổi mật khẩu, quy chế), `netweb-KHACH` (GUEST tra cứu văn bằng).
- Kế hoạch `basis: "sheet"` bị **khóa nút "Đọc lại tài liệu"** (và bỏ qua khi "Đọc lại tất cả") để không ghi đè. `edusoft-CHUNG` (CHUNG-001 + luồng thay thế) không thuộc sheet, giữ nguyên.
- **Nút "Claude dựng kịch bản"** (trang danh mục, tab Kịch bản test của phân hệ, chip "n DM" trên menu release): chọn hạng mục chưa có kịch bản, trang đọc lại tài liệu nguồn và nhờ Claude viết kịch bản đầy đủ (bước, luồng thay thế, luồng dữ liệu, kết quả mong muốn) theo mục "Dựng kịch bản test từ tài liệu", bám `steps` đã đối chiếu; ghi `scenarios/<es-|nw-><mã viết thường>` với mã tiếp theo của phân hệ, `source: {plan, docRef}`, `status: "notrun"`, điền `scenarioCode` và gắn `scenarioIds` cho menu release trùng menu.
- Nút "Đọc lại tài liệu" (lập danh mục từ mục lục tài liệu, ghi `lastSync`) chỉ còn dùng cho kế hoạch không có `basis: "sheet"` (vd phân hệ chưa có trong sheet).
- Cập nhật khi sheet đổi: đọc lại sheet 4 → so theo `menu` chuẩn hoá: menu mới thì thêm hạng mục (đối chiếu tài liệu, viết `steps`), menu bị bỏ thì hỏi người dùng trước khi xoá, giữ `scenarioCode` và phần người dùng đã sửa tay; đánh lại `stt`. Ghi cả `data/testPlans/` và DB artifact (`batch` có `if_version`).
- Cách đối chiếu (làm tay trong cuộc trò chuyện): với từng dòng sheet tìm tài liệu cùng phân hệ (bảng trên; tài liệu Netweb ở thư mục NETWEB, `Netweb_TaiLieuHuongDanSinhVien` phủ hầu hết menu SV, `NetWEB_GiangVienXemThongTinCaNhan` phủ menu GV), đọc mục có dòng `Menu:` trùng → ghi bước theo tài liệu; menu tài liệu khác sheet thì `partial` + `docNote` nêu cả hai đường dẫn.
- Kết quả đối chiếu 30/10/2026 (219 menu): 154 khớp, 34 khớp một phần, 31 chưa có tài liệu. Chênh lệch đáng chú ý:
  - KLGD: sheet "Hệ số lớp đông / Mức hệ số lớp đông" ↔ tài liệu "Hệ số lớp đông theo đối tượng"; "Công thức loại hình" ↔ "Định nghĩa loại hình học kỳ"; "Tính khối lượng / Tính khối lượng theo đợt" ↔ "Tính KLGD / Tính khối lượng giảng dạy".
  - QKTX: sheet "Quản lý hợp đồng / Quản lý vào|ra" (Hợp đồng theo phòng, Thanh lý hợp đồng) không có trong tài liệu (tài liệu còn menu cũ "Lưu trú / Quyết định vào|ra KTX"); "Thu tiền lưu trú tháng" ↔ tài liệu "Thu phí lưu trú".
  - QLSV: tài liệu văn bằng ghi nhầm menu (Quyết định nghỉ học); không có mục riêng cho Quyết định vào mới (dùng QLSV-001). DIEM: tài liệu Xét chứng chỉ đặt menu dưới nhánh Tốt nghiệp. DKMH: thời gian ĐK nguyện vọng, hiệu chỉnh/hủy/phục hồi KQĐK chưa có tài liệu.
  - Chưa có tài liệu: QLHT Cấm SV xem vì nợ học phí; QLSV Danh mục SV, DSSV học kỳ, thời gian cập nhật online, điểm danh (in vắng, tạo ngày, xóa KQ SV hủy ĐK), nhập/hủy điểm rèn luyện 1 SV; KHGD DS lớp học kỳ, Netweb CTĐT & môn tiên quyết; DKMH 103, 108–113; LTHI ghép phòng, đánh số báo danh, phân công coi thi khác; DIEM 145, 146, 148, 149, 162, 163; QLTV import phiếu thu, thu vãng lai; QKTX xem hợp đồng từng đối tượng.

## Nghiệp vụ theo phân hệ (`nghiep-vu/<PH>.md`) – đọc trước khi dựng/sửa kịch bản
Người dùng không muốn dạy thủ công → Claude tự rút nghiệp vụ, gộp 3 nguồn:
1. **Tài liệu HDSD + lưu đồ** trên SharePoint (đọc bằng connector) → vòng đời, thứ tự, danh mục phải có trước, cách dọn dữ liệu.
   Lưu đồ Visio `QuiTrinhMotTrangViSio/*.vsdx` (66 file) connector KHÔNG đọc được – cần người dùng tải thư mục (.zip) gửi vào chat.
2. **Bản trích source** (`tools/trich_source.py --tat-ca`, từ 16/11 có mục "Ràng buộc": ô bị kiểm tra rỗng / so sánh / trùng + câu báo)
   → `tools/gan_form_tay.py` ghép vào danh mục (`forms[].rb`, ô bắt buộc = phần tử thứ 4 của `o`) → luồng thay thế "bỏ trống ô bắt buộc".
3. **Lần chạy thật** (`ui-*.txt`, ảnh) → hành vi runtime; dump cũ nằm ở asset artifact (Artifact read `path` = id trong `dumps`).
Đã có: `nghiep-vu/QLSV.md` (QĐ vào/ra, DS SV học kỳ, dọn dữ liệu – nguyên nhân bước 12 QLSV-001).

## Dựng kịch bản test từ tài liệu
1. Xác định chức năng cần test → tìm phân hệ trong bảng → liệt kê thư mục → đọc bản Word của tài liệu (MỤC LỤC trước, rồi đúng mục). Đối chiếu `*_menu.pdf` để lấy đúng cây menu.
2. Dựng cả phân hệ "từ đầu đến chân": đi đúng thứ tự tài liệu (chỉnh định thông số → danh mục → khai báo → chuẩn bị dữ liệu → tính/xử lý → xem/khóa/in), mỗi mục có thao tác kiểm chứng được → một kịch bản (gộp các mục tài liệu ghi "tương tự"), cuối cùng thêm một kịch bản **dọn dữ liệu test** và khôi phục cấu hình. Kiểm tra kịch bản đã có để không tạo trùng. Khi có release đang chạy, ưu tiên dựng kịch bản cho các menu trong phân công release và gắn `scenarioIds` vào menu release tương ứng; hạng mục trong danh mục kế hoạch thì điền `scenarioCode`.
3. **Bước cơ bản không viết lại**: bước đầu tiên ghi `Điều kiện đầu vào: đã mở Edusoft và đăng nhập theo CHUNG-001; đang chọn <năm học/học kỳ test>; <kịch bản/dữ liệu cần có trước>`. Không ghi đường dẫn Edusoft cố định — mỗi người chạy khai báo đường dẫn riêng ở trang Máy chạy thử.
4. An toàn dữ liệu: chỉnh định thông số dùng chung chỉ kiểm tra & ghi nhận, không sửa (trừ khi đặt cho đối tượng test hẹp, có ghi giá trị cũ để hoàn tác); chọn biến thể thao tác phạm vi hẹp (vd gán theo 1 CBGD, 1 SV test); dữ liệu test có tiền tố `TEST_`.
5. Ánh xạ sang các trường:
   - **Phân hệ**, **Menu test** (đường dẫn `Menu:` giữ nguyên), **Phiên bản** (mặc định `v2026.101.00-HVNG`).
   - **Các bước test (luồng chính)**: mỗi bước một thao tác kiểm chứng được (người chạy đánh dấu Đạt/Lỗi/Bỏ qua và đính ảnh từng bước).
   - **Luồng thay thế / ngoại lệ** (`altFlows`): mỗi tình huống tài liệu có ràng buộc, chặn, cảnh báo hoặc lựa chọn khác thì thêm một luồng `{name, condition, steps: [..], expected}`. Nguồn gợi ý: biến chỉnh định dạng "Cấm …/ Cho phép … khi …" (vd ĐKMH: trùng TKB sinh viên, vi phạm tiên quyết, vượt tín chỉ max, môn bị cấm, chưa đủ tín chỉ min, SV ngoài DSSV học kỳ, cùng môn khác nhóm), trùng mã, bỏ trống trường bắt buộc, xóa dữ liệu đang được dùng, thao tác khi sổ đã khóa, file import sai cấu trúc. `condition` nêu dữ liệu/cấu hình gây ra tình huống (ghi mã kịch bản tạo ra nó); `expected` là phản ứng của chương trình (chặn + thông báo, dữ liệu không đổi). Tài liệu không nói rõ thì thêm "Cần xác nhận".
   - **Luồng dữ liệu** (bắt buộc): `dataFlow.in` = dữ liệu cần có trước và lấy từ đâu (ghi mã kịch bản nguồn trong ngoặc); `dataFlow.out` = dữ liệu được tạo/thay đổi, có giá trị test cụ thể; `dataFlow.next` = mảng mã kịch bản dùng tiếp dữ liệu này (trang tự vẽ chiều ngược "nhận từ").
   - **Kết quả mong muốn**: hành vi tài liệu mô tả, kèm `(Theo <tài liệu>, mục <số>.)`; chỗ tài liệu mơ hồ ghi "Cần xác nhận". Khi tài liệu có công thức, tính sẵn giá trị mong đợi bằng dữ liệu test.
   - **Quá trình test**, **Kết quả thực tế**: để trống; trạng thái `notrun`.
6. Không bịa chi tiết tài liệu không nói.
7. Nghĩ như tester **và** người dùng thật: đi đúng luồng nghiệp vụ của tài liệu và lưu đồ phân hệ (`QuiTrinhMotTrangViSio/<phân hệ>.pdf`), không đi tắt. Ví dụ: sinh viên mới vào hệ thống qua **Quyết định vào mới** (`Sinh viên/ Sinh viên học kỳ/ QĐ vào/ra sinh viên/ Quyết định vào mới`), không thêm thẳng vào Danh mục sinh viên. Kiểm tra danh mục / màn hình tiền đề trước khi thao tác.
8. Nghiệp vụ menu: sau **mỗi** thao tác ghi dữ liệu có một bước `KIỂM TRA …` riêng — Thêm → dữ liệu hiển thị trên màn hình (và màn hình nhận dữ liệu); Sửa → mở lại thấy giá trị mới, không còn giá trị cũ; Xóa → dữ liệu không còn trên màn hình. Kịch bản đi đủ Thêm → kiểm tra → Sửa → kiểm tra → Xóa → kiểm tra (mẫu: QLSV-001).

### Quy trình chuẩn kịch bản thêm – sửa – xóa (bắt buộc, người dùng chốt; mẫu QLSV-001)
Chạy **đúng thứ tự bước**, mỗi bước tự mở menu của chính nó (lệnh `menu:` trong `auto` của bước); không mở trước menu
của bước sau. Trình tự:
1. **Điều kiện đầu vào** – đã vào Edusoft (đăng nhập theo CHUNG-001), đúng năm học/học kỳ test.
2. **Kiểm tra trùng dữ liệu định thêm** ở mọi màn hình chứa dữ liệu đó (vd sinh viên: `Danh mục sinh viên` rồi
   `Danh sách sinh viên học kỳ`): tìm mã và tên test **bằng ô tìm kiếm của cột** (dòng lọc có icon phễu – skill `giaodien-edusoft` #5) → **đã có thì tự chọn
   mã/tên test khác** (`unique: MSSV @ Mã sinh viên|Mã SV`, `unique: TEN @ Tên`),
   không dừng test. Tên test chọn trong danh sách không dính tổ hợp Telex (Mot, Hai, Ba, Bon, Nam, Sau, Bay, Tam…).
3. **Thu thập dữ liệu danh mục tiền đề** (chỉ xem, không sửa): mở danh mục, lấy các dòng đúng loại, **chọn ngẫu nhiên một
   dòng và ghi nhớ** vào biến (`pick: BIẾN = lọc @ cột`). Vd `Sinh viên/ Sinh viên học kỳ/ QĐ vào/ra sinh viên/ Danh mục lý do quyết định`
   → một lý do thuộc loại quyết định vào mới → `{LYDO}`; lớp của học kỳ lấy từ Danh sách sinh viên học kỳ → `{LOP}`.
4. **Sau đó mới thêm** dữ liệu ở menu chính, dùng các giá trị đã kiểm tra/ghi nhớ ở bước 2–3.
5. **KIỂM TRA THÊM** trên màn hình đó và màn hình nhận dữ liệu → **Sửa** → **KIỂM TRA SỬA** → **Xóa** (chỉ xác nhận khi hộp
   thoại nêu đúng mã test) → **KIỂM TRA XÓA** (`absent:`).
Biến lấy ở bước trước ghi trong `vars` dạng `"(lấy ở bước N)"`. Bước kiểm tra/thu thập lỗi thì luồng dừng (không thêm dữ liệu
với giá trị chưa kiểm tra); người chạy thấy popup lỗi và chọn Tạo lỗi / Không phải lỗi / Dừng test.

## Lỗi trong Edusoft (2 loại)
1. **Lỗi chức năng / dữ liệu** (`type: "func"`): thực hiện chức năng (lưu, xóa, sửa, import, tính…) nhưng dữ liệu sau thao tác không được lưu hoặc sai. Ghi: `action`, `expectedData` (dữ liệu đã nhập/mong đợi), `actualData` (dữ liệu thực tế sau khi mở lại màn hình), ảnh.
2. **Lỗi EX – hệ thống** (`type: "ex"`): trong Edusoft nhấn **Ctrl+Shift+E** để hiện chi tiết lỗi → chụp ảnh menu đang thao tác (kèm cửa sổ chi tiết) → nhấn **Ctrl+Shift+F** để hiện menu code. Ghi: `exDetail` (nguyên văn chi tiết lỗi), `menuCode`, ảnh (bắt buộc). Kịch bản có lỗi EX đang mở hiển thị đỏ trên trang.
Một luồng thay thế cho kết quả khác `expected` (vd chương trình không chặn trùng TKB) cũng là lỗi chức năng, ghi `kind: "alt"`. Lỗi có mã case hỗ trợ (ACS) thì ghi `caseNo`; Claude cập nhật `caseStatus`, `caseCheckedAt` sau khi đọc case trên ACS bằng phiên đăng nhập của người dùng trong trình duyệt app. Link case dựng từ `settings/acs` (`{baseUrl, caseUrl chứa {case}, newCaseUrl}`).

## Máy chạy thử & kiểm tra khởi động (bắt buộc trước khi test)
- Mỗi người chạy khai báo trên trang **Máy chạy thử**: collection `runners`, `doc_id` = id người dùng (`u_…`): `{path (đường dẫn đầy đủ tới Edusoft.NET.exe trên máy họ), machine, env, account (tài khoản Edusoft test), alias (tên trong bảng phân công release), hasPw: {edusoft, sv, gv}, netweb: {url, defaultRole: "sv"|"gv", sv: {code}, gv: {code}, check: {status, at, message, role, account, shots}}, check: {status: "none"|"pending"|"ok"|"fail", at, message, version, shots: [assetId]}, updatedAt}`.
- **Mật khẩu test** nằm trong vùng riêng của từng người: `ArtifactData` `get` collection `data/users/me`, doc `secrets` → `{edusoft: {password}, netweb: {sv: {password}, gv: {password}}}` (chỉ đọc được của chính người đang trò chuyện). Không bao giờ ghi mật khẩu ra cuộc trò chuyện, `process`, mô tả lỗi hay document dùng chung nào.
- Chỉ nhập mật khẩu này vào **khung đăng nhập của môi trường test** người dùng đã khai báo (Edusoft bản test trên máy họ; Netweb có địa chỉ là môi trường test). Nếu địa chỉ Netweb trông như môi trường thật / production, không tự đăng nhập: mở trang và nhờ người dùng tự đăng nhập trong trình duyệt của app (phiên đăng nhập được giữ lại).
- Khi người dùng nhắn "kiểm tra khởi động Edusoft" (hoặc trước lượt chạy đầu tiên): `query` collection `runners` lấy document có `check.status = "pending"` (hoặc của người đang trò chuyện) → mở **đúng** `path` đó trên máy họ qua computer use (cấp quyền app theo đường dẫn exe, vd `computer_request_access` với bundleId là đường dẫn exe viết thường) → chờ khung đăng nhập → đăng nhập bằng `account` và mật khẩu Edusoft trong `secrets` → chụp ảnh từng bước, đưa lên làm asset.
  - Thành công (thấy màn hình chính, đọc được phiên bản trên tiêu đề): `update` runner `check = {status: "ok", at, message: "Mở và đăng nhập thành công", version, shots}`. Ghi thêm một document `runs` cho CHUNG-001 (`mode: "auto"`).
  - Lỗi (không tìm thấy file, app không mở, khung đăng nhập không hiện, sai đăng nhập, lỗi EX…): `check = {status: "fail", at, message: <lý do cụ thể>, shots}` và báo người dùng; **không** chạy kịch bản nào cho tới khi kiểm tra lại thành công.
- **Netweb**: khi người dùng nhắn "kiểm tra đăng nhập Netweb" (`netweb.check.status = "pending"`): mở `netweb.url` trong trình duyệt tích hợp của app (skill built-in-browser), đăng nhập bằng `netweb[defaultRole].code` và mật khẩu tương ứng trong `secrets`, chụp ảnh, rồi `update` runner `netweb.check` = `{status: "ok"|"fail", at, message, role, account: <mã>, shots}`. Kịch bản Netweb chỉ chạy được khi `netweb.check.status = "ok"`.
- Đổi đường dẫn, tài khoản hoặc mật khẩu → trang tự đặt lại `check.status = "none"`; phải kiểm tra lại.
- Máy chưa liên kết (không có tool `mcp__remote-devices__*`) thì báo người dùng mở cuộc trò chuyện trong app desktop trên máy có Edusoft.

## Khi Claude chạy test thật trên app (computer use)
- Chỉ chạy khi runner của người yêu cầu có `check.status = "ok"` (Netweb: `netweb.check.status = "ok"`); mở app theo `path` của runner (Netweb: `netweb.url`), không dùng đường dẫn cố định, đăng nhập theo CHUNG-001, rồi đi từng bước.
- **Lượt chạy hiển thị trực tiếp**: lúc bắt đầu `set` một document mới trong collection `runs` với `status: "running"`, `current: 0`; sau **mỗi bước** chụp màn hình, đưa ảnh lên (tool `Artifact`, `url` của console, `asset: true`, `file_path`/`file_paths` → `id`) và `update` document đó (`steps[i]`, `current: i+1`, hoặc `current: {k: "a", i}` khi đang ở luồng thay thế). Trang vẽ ảnh của bước đã/đang chạy ngay khi document đổi. Kết thúc: `status` = "pass"|"fail"|"blocked", `current: null`, `finishedAt`, `actual`, `process`.
- Schema `runs`: `product`, `module`, `scenarioId`, `scenarioCode`, `scenarioTitle`, `mode` ("auto" khi Claude chạy | "manual"), `executor` ("claude"|"user"), `runnerId` (id người yêu cầu chạy — "người chạy thử"), `machine`, `path`, `version`, `status` ("running"|"pass"|"fail"|"blocked"|"error"), `current`, `startedAt`, `finishedAt`, `steps` (mảng cùng độ dài `steps` của kịch bản: `{res: "ok"|"bad"|"skip"|null, shots: [assetId], at, note}`), `alts` (cùng độ dài `altFlows`, cùng dạng), `process` (log `dd/mm/yyyy HH:MM  Bước n: ĐẠT — …`), `actual`, `createdAt`; chạy trong release thì thêm `releaseId`, `releaseVersion`, `round`, `releaseItemId`.
- Ảnh: chỉ lưu `id` asset, không lưu URL. Không chụp/đưa lên ảnh có mật khẩu hiện rõ.
- Gặp lỗi EX: nhấn Ctrl+Shift+E, chụp và đọc chi tiết lỗi, nhấn Ctrl+Shift+F đọc menu code, đóng cửa sổ lỗi; không bấm thêm nút ghi/xóa nào. Gặp lỗi chức năng: mở lại màn hình, chụp dữ liệu thực tế.
- Sau khi kết thúc: `update` kịch bản với `status`, `version`, `process`, `actual`, `lastRun` (`{runId, at, by: runnerId, mode: "auto", status, version, hasEx}`), `updatedAt`.
- Mỗi bước / luồng lỗi tạo một document trong `bugs`: `product`, `module`, `scenarioId`, `scenarioCode`, `scenarioTitle`, `runId`, `kind` ("step"|"alt"|"release"), `stepIndex` (từ 0), `stepText`, `type` ("func"|"ex"), `action`, `expectedData`, `actualData`, `exDetail`, `menu`, `menuCode`, `caseNo`, `shots`, `version`, `status` ("open" khi mới tạo; "sent"|"fixed"|"invalid"), `createdAt`, `createdBy` (runnerId), `updatedAt`, `updatedBy`; trong release thêm `releaseId`, `releaseVersion`, `round`, `releaseItemId`.
- Hỏi người dùng trước khi bấm nút có thể làm thay đổi dữ liệu ngoài phạm vi kịch bản.

## Release (phiên bản phát hành)
- Quy trình: mỗi phiên bản release (vd `2026.10G.00`) → merge code → build bản release → Support test menu **2 lần** → release. Phân công nằm ở file OneDrive `support@aqtech.vn` › `All Docs/2. Tài liệu nội bộ Support/Release(TestMenu).xlsx` (drive `b!fGvoS7Slz0Cz5N8KVd7PLacfDvgTQgVEsjpb5mlSYURjv4OX0wHcQ59hhQkDHKjq`, item `01MKZ3PSTNDVN6HZJ6SFEJ62SF2SPQOX4K`; đọc sheet bằng `read_resource` với `startPage`/`endPage` = số thứ tự sheet).
  - Sheet **Menu_NEW** (sheet 4): menu theo khối phân hệ, cột A STT, B Menu, E Phân công lần 1, F Kết quả (x = Pass, o = Fail), G Mô tả (mã case, `EX: <case>`), H cờ EX, I/J/K = phân công / kết quả / mô tả lần 2. Dòng `NetWEB …:` là menu Netweb nằm trong khối phân hệ.
  - Sheet **TestMenu_NEW** (sheet 3): tổng hợp theo người test — PC (phân công), X, O, Chưa, EX.
- Trên console: menu **Phân công release** có 2 menu con **Edusoft** và **Netweb** (tách riêng, không trộn menu hai sản phẩm). Mỗi kỳ release bắt đầu **trống**: thêm menu bằng "Thêm kịch bản" → chọn phân hệ → tick hạng mục trong Danh mục kịch bản của phân hệ đó (cùng menu thì gộp một dòng), hoặc "Đồng bộ menu test từ release trước". Mặc định **test 1 lần** (không còn Lần 1/Lần 2); menu bị O tự vào tab **Theo dõi sửa lỗi** với trạng thái `fix.st`: `wait` (Chờ dev sửa) → `dev` (Dev đã sửa – chờ test lại) → `pass` (Test lại đạt, đóng các `bugs` gắn `releaseItemId`) / `fail`. Phiên bản đổi được (sau khi dev sửa có bản build mới; bản cũ lưu ở `versions`), nút **Chốt phiên bản release** ở góc trên phải ghi bản cuối (`finalVersion`, `releaseDate`, `status: "released"`). Menu **Danh sách Release** liệt kê release cả năm theo tháng 1→12: ngày chốt, trạng thái, menu, đạt, lỗi, đã sửa. Collection `releases`, `releaseItems`.
  - `releases/<rel-id>` (`rel-` + phiên bản lúc tạo, ký tự khác chữ/số thành `-`, vd `rel-2026-10G-00`; id giữ nguyên khi đổi phiên bản): `{version, versions: [{v, until, by}], status: "planning"|"testing"|"released", rounds: 1, currentRound, releaseDate (YYYY-MM-DD, ngày chốt), finalVersion, releasedAt, releasedBy, sheetUrl, sheetName, testers: [tên], createdAt, updatedAt}` (trường `plan` cũ không còn dùng).
  - `releaseItems/<rel-id>--<idx 3 số>`: `{releaseId, idx, group (mã phân hệ; menu Netweb thêm từ danh mục = "NETWEB"), stt, product, module, menu (bỏ ngoặc, chuẩn hóa " / "), menuRaw, paren, title (tên hạng mục danh mục), source: {plan, idx}, scenarioIds: [doc_id kịch bản], r1: {assignee, res: "x"|"o"|null, note, caseNo, ex, at, by, runId}, fix: {st, at, by}}`. Release cũ nhập từ sheet có thể còn `r2` – trang dùng lần có dữ liệu mới nhất.
  - Người test dán vùng A3:K của Menu_NEW vào "Nhập phân công từ sheet" (khớp theo menu + phân hệ). Khi Claude nhập thay: đọc sheet, tạo document theo schema trên bằng `batch` (≤ 50/lần).
  - Mỗi người khai báo "Tên trong bảng phân công" ở Máy chạy thử (`runners.alias`) để lọc "Của tôi".
- Gắn kịch bản cho menu: điền `scenarioIds` (trang còn tự khớp khi `menu` của kịch bản trùng chuẩn hóa với menu release). Chạy kịch bản từ menu release: run/bug mang `releaseId`, `releaseVersion`, `round`, `releaseItemId`; Đạt → menu = x, Không đạt → o.
- Khi Claude chạy test release qua computer use: ghi `runs` kèm 4 trường release, rồi `update` `releaseItems/<id>` field `r<lần>` = `{res, ex, note, caseNo, runId, at, by: runnerId}`; menu lỗi tạo `bugs` với `kind: "release"` (không có kịch bản thì `scenarioId: null`, `stepText` = menu).
- Không sửa file Excel gốc trừ khi người dùng yêu cầu.

## Lưu kịch bản vào AQ Autotest Console
- Artifact: https://claude.ai/artifact/7pKLZXYm4eqELvrqs8P6QG — cơ sở dữ liệu, collection `scenarios`, `testPlans`, `runs`, `runners`, `bugs`, `releases`, `releaseItems`, `settings` (tool `ArtifactData`); mật khẩu test ở `data/users/<id>/secrets` (riêng từng người); ảnh là asset của artifact.
- Trước khi ghi: `list`/`query` để lấy số lớn nhất của phân hệ; `doc_id` mới = `es-` + mã viết thường (vd `es-dkmh-011`, Netweb dùng `nw-`). Hai kịch bản đầu có `doc_id` cũ (`es-tc-001` = CHUNG-001, `es-tc-002` = KLGD-015); giữ nguyên.
- Schema kịch bản: `product`, `module`, `code`, `title`, `menu`, `version`, `steps` (mảng chuỗi), `altFlows` (`[{name, condition, steps: [..], expected}]`), `dataFlow` (`{in, out, next: [mã]}`), `process`, `expected`, `actual`, `status` ("notrun"|"pass"|"fail"|"blocked"), `createdAt`, `updatedAt` (ISO), `createdBy`, `updatedBy` (null khi Claude tạo), `lastRun` (do lần chạy ghi).
- Nhiều document: dùng `batch` (tối đa 50; nội dung dài thì ghi ra file JSON và truyền `file_path`). Sửa document đã có: đọc trước và truyền `if_version`.
- Không ghi mật khẩu hoặc thông tin nhạy cảm vào dữ liệu dùng chung (mật khẩu chỉ nằm trong `data/users/<id>/secrets` do chính người dùng nhập trên trang).
- Sau khi ghi, báo người dùng mã kịch bản/lỗi, phân hệ và tài liệu nguồn đã dùng.