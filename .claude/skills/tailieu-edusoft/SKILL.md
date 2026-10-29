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
Kịch bản **bắt buộc** thuộc một phân hệ (trường `module`). Chỉ dùng các mã dưới đây (mã khác rơi vào nhóm "Chưa xếp phân hệ"). Trang **Kịch bản test · Release** hiện danh sách phân hệ thu gọn được; mở một phân hệ thấy thẻ tóm tắt (menu release đã test, kịch bản, độ phủ danh mục) và hai tab **Menu release** / **Kịch bản test**. Danh mục kịch bản nằm ở trang riêng **Danh mục kịch bản**.
- **Edusoft** (`product: "edusoft"`): `CHUNG` (khởi động & đăng nhập), `QLHT`, `QLNS`, `KHGD`, `KLGD`, `QLTS`, `QLSV`, `QKTX`, `DKMH`, `LTHI`, `QLTV`, `DIEM`, `QLTN`, `KSDG`, `NCKH`, `SAE`, `DTNH`, `PVLD` — trùng mã thư mục tài liệu (HTLĐ xếp vào `PVLD`).
- **Netweb** (`product: "netweb"`): `CHUNG`, `QTRI` (Quản trị chung), `SV`, `GV`, `PH` (Phụ huynh), `KHACH` (Khách – tra cứu), `TS` (Tuyển sinh & nhập học online). Tài liệu nguồn trong thư mục NETWEB (và QLTS/NhapHocOnline cho `TS`): SinhVien* → SV, GiangVien*/DiemDanh* → GV, PhuHuynh → PH, Guest_* → KHACH, QuanTriChung → QTRI.
- **Mã kịch bản**: `<PHÂN HỆ>-<STT 3 số>`, vd `KLGD-001`, `DKMH-005` (không tiền tố sản phẩm; sản phẩm nằm ở trường `product`). Đánh số riêng trong từng phân hệ theo trình tự quy trình của tài liệu (trang chạy thử theo thứ tự mã).
- Kịch bản cơ bản mở app + đăng nhập Edusoft là **CHUNG-001**, đồng thời là bước kiểm tra khởi động của máy chạy thử. Đã có: KLGD-001 → 026 (từ chỉnh định thông số đến dọn dữ liệu test) và DKMH-001 → 010 (chỉnh định, ràng buộc, đăng ký từng SV / tự động / theo file, thống kê rảnh bận, dọn dữ liệu) — dùng làm mẫu khi dựng phân hệ khác.

## Danh mục kịch bản test (kế hoạch test theo tài liệu)
- Mỗi phân hệ có một kế hoạch test: collection `testPlans`, `doc_id` = `<product>-<MÃ PHÂN HỆ>` (vd `edusoft-DKMH`): `{product, module, status: "draft"|"requested"|"approved", objective, docs: [{name, url}], items: [{title, menu, docRef, kind: "setup"|"main"|"alt"|"clean", priority: "cao"|"trung bình"|"thấp", scenarioCode}], createdAt, updatedAt, updatedBy}`. Thêm khi đồng bộ: `syncedAt`, `syncedBy`, `docs[].size` / `docs[].syncedAt` (kích thước file lúc đọc), `lastSync: {at, by, tier, added, docs: [{name, st: "ok"|"skip"|"err", items, note}]}` — xem `lastSync` khi người dùng báo lỗi đồng bộ. Trên console là trang riêng **Danh mục kịch bản** (menu THIẾT KẾ): tổng quan các phân hệ (số hạng mục, độ phủ kịch bản, trạng thái, lần đồng bộ) và danh mục từng phân hệ (thêm/sửa/xóa hạng mục, "Dựng kịch bản", "Duyệt kế hoạch").
- **Nút "Đồng bộ từ tài liệu"** (từng phân hệ, hoặc "Đồng bộ tất cả"): trang tự gọi connector Microsoft 365 (`read_resource`, trang 1–45) của người bấm để liệt kê thư mục tài liệu, đọc song song 3 tài liệu (file Word > 6 MB đọc bản PDF trước; Word bị "took too long" thì chuyển sang PDF; lỗi tạm thời thử lại 1 lần), rồi nhờ Claude lập hạng mục ở mức **một hạng mục = một kịch bản** (không tách thao tác nhỏ), có danh sách hạng mục đã có để không lặp. Tài liệu có kích thước không đổi so với lần đồng bộ trước thì bỏ qua (nút "Đọc lại toàn bộ tài liệu" để ép đọc lại); tài liệu lỗi được đọc lại ở lần sau. Chế độ "Claude: nhanh / kỹ" chọn ở thanh lọc. Đồng bộ một phân hệ thì người dùng chọn hạng mục mới để áp dụng; đồng bộ tất cả thì tự thêm và lưu từng phân hệ ngay khi xong. Hạng mục trùng hoặc gần trùng tên không thêm lại; kết quả về `status: "draft"`. Người dùng cần connector Microsoft 365 và bấm Cho phép (Microsoft 365 + Claude) lần đầu.
- **Nút "Claude dựng kịch bản"** (trang danh mục, tab Kịch bản test của phân hệ, chip "n DM" trên menu release): người dùng chọn hạng mục chưa có kịch bản (mặc định các hạng mục thuộc menu release), trang đọc lại tài liệu nguồn và nhờ Claude viết kịch bản đầy đủ (bước, luồng thay thế, luồng dữ liệu, kết quả mong muốn) theo quy tắc ở mục "Dựng kịch bản test từ tài liệu"; ghi `scenarios/<es-|nw-><mã viết thường>` với mã tiếp theo của phân hệ, `source: {plan, docRef}`, trạng thái `notrun`, rồi điền `scenarioCode` vào danh mục và gắn `scenarioIds` cho menu release trùng menu.
- Danh mục cũ (trước bản đồng bộ mới) có nhiều hạng mục trùng / quá chi tiết; khi người dùng nhờ dọn, gộp theo nghĩa, giữ hạng mục đã có `scenarioCode`, ghi bằng `update` có `if_version`.
- Khi người dùng nhắn "lập kế hoạch test phân hệ X" trong cuộc trò chuyện (hoặc `query` thấy `status: "requested"` từ bản cũ), làm tay theo cùng quy tắc (dùng khi cần đọc sâu hơn nút đồng bộ, vd kèm `*_menu.pdf`):
  1. Đọc tài liệu của phân hệ theo mục "Cách đọc" (MỤC LỤC → từng mục III, kèm `*_menu.pdf`).
  2. Mỗi mục quy trình có thao tác kiểm chứng được → một hạng mục (`kind` setup cho chỉnh định/danh mục, main cho nghiệp vụ, clean cho dọn dữ liệu); mỗi ràng buộc "Cấm…/Cho phép… khi…" → hạng mục `alt`. `docRef` = `<tài liệu>, mục <số>`.
  3. Đối chiếu menu của phân hệ trong release đang test (`releaseItems`): menu chưa có hạng mục thì thêm hạng mục; không có tài liệu thì `docRef` ghi "Menu release <phiên bản> (cần bổ sung tài liệu)".
  4. `scenarioCode` = mã kịch bản đã có (vd `DKMH-005`), để trống nếu chưa dựng. `objective` 1–3 câu về phạm vi; `docs` = tên tài liệu đã dùng.
  5. Ghi bằng `set` (doc mới) hoặc `update` có `if_version`, để `status: "draft"`; người dùng tự bấm "Duyệt kế hoạch". Giữ nguyên hạng mục người dùng đã thêm tay.
- Hạng mục chưa có kịch bản: dựng kịch bản theo mục dưới rồi điền `scenarioCode` (trên trang, nút "Dựng kịch bản" tạo kịch bản điền sẵn và tự gắn).
- Đã có (29/10/2026): danh mục cho 16 phân hệ Edusoft (~1.250 hạng mục, từ lần "Đồng bộ tất cả" đầu tiên, còn trùng lặp); QLTS và QLSV lỗi ở lần đó (file .doc lớn), Netweb chưa đồng bộ. Kịch bản thật: CHUNG-001, KLGD-001 → 026, DKMH-001 → 010.

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
- Trên console: trang **Kịch bản test · Release** (gộp chung với kịch bản; chọn phiên bản và lần test ở thanh trên, mỗi phân hệ thu gọn được). Phần Netweb nhóm menu `NetWEB …` theo SV / GV / QTRI / KHACH / TS / CHUNG. Collection `releases`, `releaseItems`.
  - `releases/<rel-id>` (`rel-` + phiên bản, ký tự khác chữ/số thành `-`, vd `rel-2026-10G-00`): `{version, status: "planning"|"testing"|"released", currentRound: 1|2, sheetUrl, sheetName, testers: [tên], createdAt, updatedAt}` (trường `plan` cũ không còn dùng).
  - `releaseItems/<rel-id>--<idx 3 số>`: `{releaseId, idx, group (mã phân hệ của khối; khối toàn NetWEB = "NETWEB"), stt, product, module, menu (bỏ ngoặc, chuẩn hóa " / "), menuRaw, paren, scenarioIds: [doc_id kịch bản], r1: {assignee, res: "x"|"o"|null, note, caseNo, ex, at, by, runId}, r2: {…}}`.
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