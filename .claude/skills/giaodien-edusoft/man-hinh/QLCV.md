# QLCV – Quản lý công văn (Công văn)

## Menu (đường dẫn → lớp màn hình)

- `CA` Công văn/ An toàn dữ liệu
- `CKT` Công văn/ An toàn dữ liệu/ Kiểm tra dữ liệu phân hệ
- `C30` Công văn/ Công văn nội bộ
- `C30.10.01` Công văn/ Công văn nội bộ/ Danh sách công văn nội bộ → `Edusoft.DMS.C30._10.C30_10_01_DSCVANNOIBO` – màn hình (đoán theo tên): C30.10.01
- `C10` Công văn/ Công văn đi
- `C10.10.01` Công văn/ Công văn đi/ Danh sách công văn đi → `Edusoft.DMS.C10._10.C10_10_01_DSCVANDI` – màn hình (đoán theo tên): C10.10.01
- `C20` Công văn/ Công văn đến
- `C20.10.01` Công văn/ Công văn đến/ Danh sách công văn đến → `Edusoft.DMS.C20._10.C20_10_01_DSCVANDEN` – màn hình (đoán theo tên): C20.10.01, DSCONGVANDEN
- `C20.10.05` Công văn/ Công văn đến/ Xem danh sách nhận và đọc mail → `Edusoft.DMS.C20._10.C20_10_05_XemNVNhanVaDocMail`
- `C90` Công văn/ Nhận và xử lý công văn
- `C90.10.01` Công văn/ Nhận và xử lý công văn/ Duyệt công văn → `Edusoft.DMS.C90._10.C90_10_01_DSCVAN_DUYET` – màn hình (đoán theo tên): CDUYETCONGVAN
- `C90.20.01` Công văn/ Nhận và xử lý công văn/ Xử lý công văn nhận → `Edusoft.DMS.C90._20.C90_20_01_DSCVAN_NHAN`
- `C40` Công văn/ Quyết định
- `C40.10.10` Công văn/ Quyết định/ Danh sách quyết định → `Edusoft.DMS.C40._10.C10_DSQuyetDinh` – màn hình (đoán theo tên): S-DS-QUYETDINH, S-DS-QUYETDINH2, C40.10.10
- `C40.10.12` Công văn/ Quyết định/ Quyết định IU → `Edusoft.DMS.C40._10.C10_QT_QDDHQuocTe`
- `C40.10.13` Công văn/ Quyết định/ Quyết định IU (ĐT) → `Edusoft.DMS.C40._10.C10_QT_QDDHQuocTeDaoTao`
- `C40.10.11` Công văn/ Quyết định/ Quyết định ĐHQG → `Edusoft.DMS.C40._10.C10_QT_QDDHQuocGia`
- `CBB` Công văn/ Quản lý báo biểu
- `CQT` Công văn/ Quản trị phân hệ
- `CQT2` Công văn/ Quản trị phân hệ/ Chỉnh định thông số toàn cục → `AQViewers.Settings.UC_SettingsTool1` (Param1=QLCV) – màn hình: VIEWSETTINGTREE, HVALUESETTING, VIEWSETTING
- `CQT0` Công văn/ Quản trị phân hệ/ Quản lý danh mục
- `C3` Công văn/ Thông tin chung
- `C3.01` Công văn/ Thông tin chung/ Danh mục
- `C3.10.03` Công văn/ Thông tin chung/ Danh mục/ Danh mục loại văn bản
- `C3.01.02` Công văn/ Thông tin chung/ Danh mục/ Danh mục đơn vị ngoài → `Edusoft.DMS.C2.C201.C201_01_DMCQNgoai` – màn hình: CDMCQNGOAI, NDMDVNGOAI
- `C3.01.01` Công văn/ Thông tin chung/ Danh mục/ Danh mục đơn vị nội bộ → `Edusoft.DMS.C2.C201.C201_02_DMCQNoiBo` – màn hình: CDMCQNOIBO
- `C3.02` Công văn/ Thông tin chung/ Người ký
- `C3.02.03` Công văn/ Thông tin chung/ Người ký/ Lãnh đạo duyệt → `Edusoft.DMS.CGD.C201.C201_05_DMNVDUYET`
- `C3.02.01` Công văn/ Thông tin chung/ Người ký/ Lãnh đạo ký chính → `Edusoft.DMS.CGD.C201.C201_03_DMNVKYCHINH`
- `C3.02.02` Công văn/ Thông tin chung/ Người ký/ Viên chức ký nháy → `Edusoft.DMS.CGD.C201.C201_04_DMNVKYNHAY`
- `C3.03` Công văn/ Thông tin chung/ Viên chức
- `C3.03.01` Công văn/ Thông tin chung/ Viên chức/ Viên chức nhận công văn → `Edusoft.DMS.C3._03.C3_03_01_NVNhanMail`
- `CHD` Công văn/ Xem file hướng dẫn
- `CHD1` Công văn/ Xem file hướng dẫn/ Tài liệu hướng dẫn EduSoft.NET → `Edusoft.STM._09.AQ_10_FileHuongDan` (Param1=-4940666520751191527)

## Màn hình (view) và lưới

### C10.10.01 – Danh sách công văn đi
- Lưới 1 «Danh sách công văn» (bảng CDSCVan); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số ký hiệu [KyHieuCVan]; Số lưu công văn [SoCVan]; Ngày đi [NgDiCVan]{ngày}; Ngày của QĐ [NgayQDCVan]{ngày}; Đơn vị gửi [IDDVDiCVan]; Nội dung [NDCVan]; Nơi nhận [NoiNhCVan]
### C20.10.01 – Danh sách công văn đến
- Lưới 1 «Danh sách công văn đến» (bảng CDSCVan); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số lưu công văn [SoCVan]; Số ký hiệu [KyHieuCVan]; Ngày nhận [NgNhCVan]{ngày}; Ngày của QĐ [NgayQDCVan]{ngày}; Đơn vị gửi [IDDVDiCVan]; Nơi gửi [NoiGuiCVan]; Đơn vị nhận [IDDVDenCVan]; Tiêu đề [TDCVan]; Trạng thái [StatusCVan]{chọn}
### C20.10.05 – Xem tình trạng gửi và đọc mail công văn đến
- Lưới 1 «Danh sách nhân viên xử lý công văn»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số lưu công văn [SoCVan]; Số ký hiệu [KyHieuCVan]; Ngày nhận [NgNhCVan]; Ngày của QĐ [NgayQDCVan]; Đơn vị gửi [IDDVDiCVan]; Nơi gửi [NoiGuiCVan]; Đơn vị nhận [IDDVDenCVan]; Tiêu đề [TDCVan]; Mã viên chức [MaNV]; Họ lót [HoLotNV]; Tên nhân viên [TenNV]; Mã đơn vị [MaDV]; Đã gửi mail [DaGuiMail]; Đã đọc mail [DaDocMail]; Địa chỉ mail gửi [DC_MailGui]; Ngày gửi mail [NgayGuiMail]; Ngày đọc mail [NgayDocMail]; Xác nhận [GcXacNhan]
  - Cột ẩn: Tên đơn vị [TenDV]
### C20.10.20 – Thông báo duyệt công văn
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### C3.03.01 – Thêm/Bỏ nhân viên nhận mail xử lý công văn
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### C30.10.01 – Danh sách công văn nội bộ
- Lưới 1 «Danh sách công văn» (bảng CDSCVan); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số lưu công văn [SoCVan]; Ngày nhận [NgNhCVan]{ngày}; Ngày của QĐ [NgayQDCVan]{ngày}; Số ký hiệu [KyHieuCVan]; Đơn vị gửi [IDDVDiCVan]; Đơn vị nhận [IDDVDenCVan]; Tiêu đề [TDCVan]; Trạng thái [StatusCVan]{chọn}
### C40.10.10 – Danh sách quyết định
- Lưới 1 «Danh sách quyết định» (bảng CDSCVan); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số lưu công văn [SoCVan]; Số ký hiệu [KyHieuCVan]; Ngày nhận QĐ [NgDiCVan]{ngày}; Ngày của QĐ [NgayQDCVan]{ngày}; Đơn vị gửi [IDDVDiCVan]; Nội dung [NDCVan]; Nơi nhận [NoiNhCVan]
### C90.10.01 – Danh sách công văn duyệt
- Lưới 1 «Danh sách công văn duyệt» (bảng CDSCVan); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số lưu công văn [SoCVan]; Số ký hiệu [KyHieuCVan]; Ngày nhận [NgNhCVan]{ngày}; Ngày của QĐ [NgayQDCVan]{ngày}; Tiêu đề [TDCVan]; Đơn vị gửi [IDDVDiCVan]; Nơi gửi [NoiGuiCVan]; Đơn vị nhận [IDDVDenCVan]; Nội dung [NDCVan]; Trạng thái [StatusCVan]{chọn}
### C90.20.01 – Danh sách công văn nhận
- Lưới 1 «Danh sách công văn nhận» (bảng CDSCVan); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số lưu công văn [SoCVan]; Số ký hiệu [KyHieuCVan]; Ngày của QĐ [NgayQDCVan]{ngày}; Ngày nhận [NgNhCVan]{ngày}; Nơi gửi [NoiGuiCVan]; Tiêu đề [TDCVan]; Đơn vị nhận [IDDVDenCVan]; Xác nhận [GcXacNhan]; Trạng thái [StatusCVan]{chọn}; Đơn vị gửi [IDDVDiCVan]
### CBB01.01 – Tổng hợp công văn đi
- Lưới 1 «Danh sách công văn» (bảng CTCCVan); tắt: Thêm, Xóa, Import, Xuất, In, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số lưu công văn [SoCVan]; Số công văn gốc [SoCVanGoc]; Tiêu đề [TDCVan]; Nội dung [NDCVan]
  - Cột ẩn: Ghi chú [GcCVan]; Đơn vị nhận [IDDVDenCVan]; Nhân viên ký nháy [IDNVKYNY]; Khóa [IsLockCVan]; Loại chữ ký chính [LOAICKKYCH]; Loại chữ ký [LOAICKKYNY]; Loại chữ ký soạn [LOAICKSOAN]; Loại công văn [LoaiCVan]; Tính chất [MucDoCVan]; Ngày hết hạn [NgBHCVan]; Ngày đi [NgDiCVan]; Ngày nhận [NgNhCVan]; Ngày soạn [NgaySoan]; Nơi nhận [NoiNhCVan]; Trạng thái [StatusCVan]; Số TT [TTCVan]; Trả lời văn bản số [TraLoiVBSo]
### CBB02.01 – Tổng hợp công văn đến
- Lưới 1 «Danh sách công văn» (bảng CDSCVan); tắt: Thêm, Xóa, Import, Xuất, In, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số lưu công văn [SoCVan]; Số công văn gốc [SoCVanGoc]; Tiêu đề [TDCVan]; Nội dung [NDCVan]
  - Cột ẩn: Ghi chú [GcCVan]; Đơn vị gửi [IDDVDiCVan]; Lưu trữ [IDLTHS]; Loại văn bản [IDLVB]; Lĩnh vực [IDLVuc]; Nhân viên ký chính [IDNVKYCH]; Nhân viên ký nháy [IDNVKYNY]; Khóa [IsLockCVan]; Loại chữ ký soạn [LOAICKSOAN]; Loại công văn [LoaiCVan]; Tính chất [MucDoCVan]; Ngày hết hạn [NgBHCVan]; Ngày đi [NgDiCVan]; Ngày nhận [NgNhCVan]; Ngày soạn [NgaySoan]; Nơi nhận [NoiNhCVan]; Trạng thái [StatusCVan]; Số TT [TTCVan]; Trả lời văn bản số [TraLoiVBSo]
### CDMCQ – Danh mục đơn vị ngoài
- Lưới 1 (bảng CDMCQ); tắt: In, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã cơ quan [MaCQ]; Tên cơ quan [TenCQ]; Viết tắt cơ quan [VtCQ]; Cơ quan cấp trên [IDCQP]; Địa chỉ [DiaChiCQ]; Email [EmailCQ]; Điện thoại [DienThoaiCQ]; Ghi chú cơ quan [GcCQ]
  - Ô trên form sửa: #MaCQ, #TenCQ, #VtCQ, #IDCQP, #DiaChiCQ, #EmailCQ, #DienThoaiCQ, #GcCQ
### CDMCQNGOAI – Cơ quan ngoài
- Lưới 1 (bảng CDMCQ); tắt: Import, Xuất, In, Nạp lại, Gộp mã, Sửa trên lưới
  - Cột: Mã cơ quan [MaCQ]; Tên cơ quan [TenCQ]; Viết tắt cơ quan [VtCQ]; Địa chỉ [DiaChiCQ]; Email [EmailCQ]; Điện thoại [DienThoaiCQ]; Ghi chú cơ quan [GcCQ]; Cơ quan cấp trên [IDCQP]
  - Ô trên form sửa: #MaCQ, #TenCQ, #VtCQ, #DiaChiCQ, #EmailCQ, #DienThoaiCQ, #IDCQP
  - Nút btnSave: "Lưu" (F10)
### CDMCQNOIBO – Danh mục cơ quan nội bộ
- Lưới 1 (bảng CDMCQ); tắt: Import, Xuất, In, Nạp lại, Gộp mã, Sửa trên lưới
  - Cột: Mã cơ quan [MaCQ]; Tên cơ quan [TenCQ]; Viết tắt cơ quan [VtCQ]; Địa chỉ [DiaChiCQ]; Điện thoại [DienThoaiCQ]; Email [EmailCQ]; Cơ quan cấp trên [IDCQP]
  - Ô trên form sửa: #MaCQ, #TenCQ, #VtCQ, #DiaChiCQ, #DienThoaiCQ, #EmailCQ, #IDCQP
  - Nút btnSave: "Lưu" (F10)
### CDMLTHS – Danh mục lưu trữ hồ sơ
- Lưới 1 (bảng CDMLTHS); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lưu trữ [MaLTHS]; Tên lưu trữ [TenLTHS]; Viết tắt lưu trữ [VtLTHS]; Ghi chú lưu trữ [GCLTHS]; Lưu trữ hồ sơ cha [IDLTHSP]
  - Ô trên form sửa: #MaLTHS, #TenLTHS, #VtLTHS, #GCLTHS, #IDLTHSP
### CDMLVB – Danh mục loại văn bản
- Lưới 1 «Danh mục loại văn bản» (bảng CDMLVB); tắt: In, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã loại văn bản [MaLVB]; Tên loại văn bản [TenLVB]; Viết tắt loại văn bản [VtLVB]; Nhóm [NhomLVB]{chọn}; Ghi chú loại văn bản [GcLVB]
  - Ô trên form sửa: #MaLVB, #TenLVB, #VtLVB, #NhomLVB, #GcLVB
### CDMLVUC – Danh mục lĩnh vực công văn
- Lưới 1 «Danh mục lĩnh vực» (bảng CDMLVuc); tắt: Import, Xuất, In, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lĩnh vực [MaLVuc]; Tên lĩnh vực [TenLVuc]; Viết tắt lĩnh vực [VtLVuc]; Ghi chú lĩnh vực [GcLVuc]
  - Ô trên form sửa: #MaLVuc, #TenLVuc, #VtLVuc, #GcLVuc
### CDMNVDYCVAN – Danh mục NV duyệt
- Lưới 1 «Danh mục nhân viên duyệt công văn»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [IDNV]; Mã NV duyệt [MANVDYCVAN]; Tên NV duyệt [TENNVDYCVAN]; Tên ngắn NV duyệt [TENNVDYCVAN2]
  - Ô trên form sửa: #IDNV, #MANVDYCVAN, #TENNVDYCVAN, #TENNVDYCVAN2
### CDMNVKYCH – Danh mục NV ký chính
- Lưới 1 «Danh mục nhân viên ký chính»; tắt: Import, Xuất, In, Nạp lại, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [IDNV]; Mã NV ký chính [MANVKYCH]; Tên VN ký [TENNVKYCH]; Tên ngắn NV ký [TENNVKYCH2]
  - Ô trên form sửa: #IDNV, #MANVKYCH, #TENNVKYCH, #TENNVKYCH2
### CDMNVKYNY – Danh mục nhân viên ký nháy
- Lưới 1 «Danh mục nhân viên ký nháy»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [IDNV]; Mã NV ký nháy [MANVKYNY]; Tên NV ký nháy [TENNVKYNY]; Tên ngắn NV ký nháy [TENNVKYNY2]
  - Ô trên form sửa: #IDNV, #MANVKYNY, #TENNVKYNY, #TENNVKYNY2
### CDMNVSNCVAN – Danh mục NV soạn
- Lưới 1 «Danh mục nhân viên soạn công văn»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [IDNV]; Mã NV soạn [MANVSNCVAN]; Tên NV soạn [TENNVSNCVAN]; Tên ngắn NV soạn [TENNVSNCVAN2]
  - Ô trên form sửa: #IDNV, #MANVSNCVAN, #TENNVSNCVAN, #TENNVSNCVAN2
### CDUYETCONGVAN – Duyệt công văn
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Người duyệt cấp 1 [IDNVDYCAP1]; Người duyệt cấp 2 [IDNVDYCAP2]; Người duyệt cấp 3 [IDNVDYCAP3]; Đã duyệt và bút phê trên giấy [DABUTPHECAP1]; Đã duyệt và bút phê trên giấy [DABUTPHECAP2]; Đã duyệt và bút phê trên giấy [DABUTPHECAP3]; Đã duyệt [DADYCAP1]; Đã duyệt [DADYCAP2]; Đã duyệt [DADYCAP3]; Nội dung duyệt [GCDUYETCAP1]; Nội dung duyệt [GCDUYETCAP2]; Nội dung duyệt [GCDUYETCAP3]
  - Ô trên form sửa: #IDNVDYCAP1, #IDNVDYCAP2, #IDNVDYCAP3, #DABUTPHECAP1, #DABUTPHECAP2, #DABUTPHECAP3, #DADYCAP1, #DADYCAP2, #DADYCAP3, #GCDUYETCAP1, #GCDUYETCAP2, #GCDUYETCAP3
### CHITIETCONGVANDEN – Chi tiết công văn đến
- Lưới 1 (bảng CDSCVan); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số lưu công văn [SoCVan]; Tiêu đề [TDCVan]; Nội dung [NDCVan]; Tính chất [MucDoCVan]; Loại văn bản [IDLVB]; Lĩnh vực [IDLVuc]; Trả lời văn bản số [TraLoiVBSo]; Đơn vị gửi [IDDVDiCVan]; Đơn vị nhận [IDDVDenCVan]; Lưu trữ [IDLTHS]; Nhân viên ký [IDNVKyCVan]; Ghi chú [GcCVan]; Tên ĐV đi [TenDVDiCVan]; Tên ĐV đến [TenDVDenCVan]; Tên lưu trữ [TenLTHS]; Họ tên NV ký [TenDayDuNVKyCVan]
  - Ô trên form sửa: #SoCVan, #TDCVan, #NDCVan, #MucDoCVan, #IDLVB, #IDLVuc, #TraLoiVBSo, #IDDVDiCVan, #IDDVDenCVan, #IDLTHS, #IDNVKyCVan, #GcCVan, #TenDVDiCVan, #TenDVDenCVan, #TenLTHS, #TenDayDuNVKyCVan
### CHITIETCONGVANDI – Chi tiết công văn
- Lưới 1 (bảng CDSCVan); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số lưu công văn [SoCVan]; Tiêu đề [TDCVan]; Nội dung [NDCVan]; Ngày soạn [NgaySoan]; Loại văn bản [IDLVB]; Tính chất [MucDoCVan]; Lĩnh vực [IDLVuc]; Trả lời văn bản số [TraLoiVBSo]; Ngày ban hành [NgayPhatHanh]; Ngày đi [NgDiCVan]; Lưu trữ [IDLTHS]; Ghi chú [GcCVan]; ID file công văn [IDFCVan]; Đơn vị nhận [IDDVDenCVan]; Đơn vị gửi [IDDVDiCVan]; Nhân viên ký [IDNVKyCVan]
  - Cột ẩn: Tên ĐV đến [TenDVDenCVan]; Tên ĐV đi [TenDVDiCVan]; Họ tên NV ký [TenDayDuNVKyCVan]; Tên lưu trữ [TenLTHS]
  - Ô trên form sửa: #SoCVan, #TDCVan, #NDCVan, #NgaySoan, #IDLVB, #MucDoCVan, #IDLVuc, #TraLoiVBSo, #NgDiCVan, #IDLTHS, #GcCVan, #IDDVDenCVan, #IDDVDiCVan, #IDNVKyCVan, #TenDVDenCVan, #TenDVDiCVan, #TenDayDuNVKyCVan, #TenLTHS
### CONGVANDI – Công văn đi
- Lưới 1 (bảng CDSCVan); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số lưu công văn [SoCVan]; Tiêu đề [TDCVan]; Nội dung [NDCVan]; Tính chất [MucDoCVan]; Lĩnh vực [IDLVuc]; Trả lời văn bản số [TraLoiVBSo]; Ngày soạn [NgaySoan]; Ngày đi [NgDiCVan]; Ngày ban hành [NgayPhatHanh]; Người ký [NguoiKyCVan]; Lưu trữ [IDLTHS]
### CTRINHXULYCONGVAN – Trình xử lý công văn
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Cơ quan nhận [IDCQNhanCVan]; Tên cơ quan [TenCQ]; Người nhận công văn [NguoiNhanCVan]
### DSCONGVANDANGXULY – Danh sách công văn đang xử lý
- Lưới 1 «Danh sách công văn»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số lưu công văn [SoCVan]; Tiêu đề [TDCVan]; Nội dung [NDCVan]; Tính chất [MucDoCVan]{chọn}; Ghi chú [GcTrinhCVan]; Ghi chú [GcDuyetCVan]; Duyệt [IsDuyetCVan]
### DSCONGVANDEN – Danh sách công văn đến
- Lưới 1 «Danh sách công văn» (bảng CDSCVan); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số lưu công văn [SoCVan]; Số công văn gốc [SoCVanGoc]; Tiêu đề [TDCVan]; Nội dung [NDCVan]; Ghi chú [GcCVan]; Loại văn bản [IDLVB]; Lĩnh vực [IDLVuc]; Lưu trữ [IDLTHS]; Tính chất [MucDoCVan]{chọn}; Trả lời văn bản số [TraLoiVBSo]; Trạng thái [StatusCVan]{chọn}; Đơn vị gửi [IDDVDiCVan]; Ngày nhận [NgNhCVan]{ngày}; Đã duyệt và bút phê trên giấy [DABUTPHECAP1]; Đã duyệt và bút phê trên giấy [DABUTPHECAP2]; Đã duyệt và bút phê trên giấy [DABUTPHECAP3]; Nội dung duyệt [GCDUYETCAP1]; Nội dung duyệt [GCDUYETCAP2]; Nội dung duyệt [GCDUYETCAP3]; Đã duyệt [DADYCAP2]; Đã duyệt [DADYCAP1]; Đã duyệt [DADYCAP3]
  - Cột ẩn: Ghi chú [GcTrinhCVan]; ID file công văn [IDFCVan]; Người duyệt cấp 1 [IDNVDYCAP1]; Người duyệt cấp 2 [IDNVDYCAP2]; Người duyệt cấp 3 [IDNVDYCAP3]; Tên lưu trữ [TenLTHS]
  - Ô trên form sửa: #SoCVan, #SoCVanGoc, #TDCVan, #NDCVan, #GcCVan, #IDLVB, #IDLVuc, #IDLTHS, #MucDoCVan, #TraLoiVBSo, #StatusCVan, #IDDVDiCVan, #NgNhCVan, #DABUTPHECAP1, #DABUTPHECAP2, #DABUTPHECAP3, #GCDUYETCAP1, #GCDUYETCAP2, #GCDUYETCAP3, #GcTrinhCVan, #IDFCVan, #IDNVDYCAP1, #IDNVDYCAP2, #IDNVDYCAP3
  - Nút btnAdd: "" (F5)
### DSCONGVANDI – Danh sách công văn
- Lưới 1 «Danh sách công văn» (bảng CDSCVan); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số lưu công văn [SoCVan]; Số công văn gốc [SoCVanGoc]; Tiêu đề [TDCVan]; Nội dung [NDCVan]; Ghi chú [GcCVan]; Ngày đi [NgDiCVan]{ngày}; Nơi nhận [NoiNhCVan]; Loại văn bản [IDLVB]; Lĩnh vực [IDLVuc]; Tính chất [MucDoCVan]{chọn}; Ngày soạn [NgaySoan]{ngày}; Trả lời văn bản số [TraLoiVBSo]; Lưu trữ [IDLTHS]; Ngày hết hạn [NgBHCVan]
  - Cột ẩn: ID file công văn [IDFCVan]; File văn bản gốc [IDFILEVBGOC]; Nhân viên ký chính [IDNVKYCH]; Nhân viên ký nháy [IDNVKYNY]; Loại công văn [LoaiCVan]{chọn}; Tên lưu trữ [TenLTHS]
  - Ô trên form sửa: #SoCVan, #SoCVanGoc, #TDCVan, #NDCVan, #GcCVan, #NgDiCVan, #IDLVB, #IDLVuc, #MucDoCVan, #NgaySoan, #TraLoiVBSo, #IDLTHS, #IDFCVan, #IDFILEVBGOC, #IDNVKYCH, #IDNVKYNY, #TenLTHS
  - Nút btnAdd: "Thêm" (F5)
  - Nút btnUpdate: "Sửa" (F2)
  - Nút btnSave: "Lưu" (F10)
### DSFILEVANBAN – Danh sách file văn bản
- Lưới 1 «Danh sách tập tin»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Thứ tự file [TTFCVan]; Tiêu đề tập tin [TDFCVan]; Xem tập tin [VIEWFILE]
### HDMDUYETCVAN – Danh mục chữ ký
- Lưới 1 «Danh sách cán bộ phê duyệt công văn» (bảng HDmChuky); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã duyệt CV [MaChuKy]; Tên duyệt CV [TenChuKy]; Chức vụ [IDChucVu]; Danh xưng [DanhXung]
  - Cột ẩn: Ghi chú [GCChuKy]; Mã viên chức [IDNV]
  - Ô trên form sửa: #MaChuKy, #TenChuKy, #IDChucVu, #DanhXung, #GCChuKy, #IDNV
### HDMKYCHINHCVAN – Danh mục chữ ký
- Lưới 1 «Danh sách cán bộ ký» (bảng HDmChuky); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã chữ ký [MaChuKy]; Tên chữ ký [TenChuKy]; Chức vụ [IDChucVu]; Danh xưng [DanhXung]; Mã viên chức [IDNV]
  - Cột ẩn: Ghi chú [GCChuKy]
  - Ô trên form sửa: #MaChuKy, #TenChuKy, #IDChucVu, #DanhXung, #IDNV, #GCChuKy
### NDMDVNGOAI – Danh mục đơn vị ngoài
- Lưới 1 (bảng NDMDV); tắt: Import, Xuất, In, Nạp lại, Gộp mã, Sửa trên lưới
  - Cột: Mã đơn vị [MaDV]; Tên đơn vị [TenDV]; Tên viết tắt [VtDV]; Ghi chú [GcDV]; Loại đơn vị [LoaiDV]{chọn}; Đơn vị cấp trên [IDDVP]; Địa chỉ [DiaChiDV]; Điện thoại [DienThoaiDV]; Email [EmailDV]
  - Ô trên form sửa: #MaDV, #TenDV, #VtDV, #GcDV, #LoaiDV, #IDDVP, #DiaChiDV, #DienThoaiDV, #EmailDV
  - Nút btnSave: "Lưu" (F10)
### VIEW_UC_CHON_DV – Control chọn đơn vị
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Đơn vị [IDDV]; Tên đơn vị [TenDV](chỉ đọc); Lưu trữ [IDLTHS]; Tên lưu trữ [TenLTHS]
  - Ô trên form sửa: #IDDV, #TenDV, #IDLTHS, #TenLTHS
### VIEWCHONCOQUAN – Chọn cơ quan
- Lưới 1 (bảng NDMDV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đơn vị [MaDV]; Tên đơn vị [TenDV]; Địa chỉ [DiaChiDV]
  - Cột ẩn: Đơn vị cấp trên [IDDVP]
### VIEWCHONCQ – Chọn danh mục cơ quan
- Lưới 1 «Cơ quan/Đơn vị» (bảng CDMCQ); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã cơ quan [MaCQ]; Tên cơ quan [TenCQ]; Địa chỉ [DiaChiCQ]; Điện thoại [DienThoaiCQ]
  - Cột ẩn: Cơ quan cấp trên [IDCQP]
### VIEWCHONCQDV – Chọn cơ quan/đơn vị
- Lưới 1 (bảng NDMDV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đơn vị [MaDV]; Tên đơn vị [TenDV]; Tên viết tắt [VtDV]; Địa chỉ [DiaChiCQ]; Điện thoại [DienThoaiCQ]
  - Cột ẩn: Đơn vị cấp trên [IDDVP]
### VIEWCHONCQNGOAI – Chọn cơ quan ngoài
- Lưới 1 (bảng NDMDV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đơn vị [MaDV]; Tên đơn vị [TenDV]; Địa chỉ [DiaChiDV]
  - Cột ẩn: Đơn vị cấp trên [IDDVP]
### VIEWCHONCQNOIBO – Chọn cơ quan nội bộ
- Lưới 1 (bảng NDMDV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đơn vị [MaDV]; Tên đơn vị [TenDV]; Địa chỉ [DiaChiDV]; Đơn vị cấp trên [IDDVP]
### VIEWCHONDVDENCVAN – Đơn vị đến công văn
- Lưới 1 (bảng CDMDVDEN); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã ĐV đến [MaDVDenCVan]; Tên ĐV đến [TenDVDenCVan]; Viết tắt ĐV đến [VtDVDenCVan]; Đơn vị đến trên [IDDVDenCVanP]
  - Cột ẩn: Đơn vị nhận [IDDVDenCVan]
### VIEWCHONDVDICVAN – Đơn vị đi công văn
- Lưới 1 (bảng CDMDVDI); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã ĐV đi [MaDVDiCVan]; Tên ĐV đi [TenDVDiCVan]; Viết tắt ĐV đi [VtDVDiCVan]
  - Cột ẩn: Đơn vị đi trên [IDDVDiCVanP]
### VIEWCHONLUUTRUHS – Chọn lưu trữ hồ sơ
- Lưới 1 (bảng CDMLTHS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lưu trữ [MaLTHS]; Tên lưu trữ [TenLTHS]; Viết tắt lưu trữ [VtLTHS]; Ghi chú lưu trữ [GCLTHS]; Lưu trữ hồ sơ cha [IDLTHSP]
### VIEWCHONNVKYCH – Chọn CBCNV ký chính
- Lưới 1 «Chọn nhân viên ký»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã NV ký chính [MANVKYCH]; Tên VN ký [TENNVKYCH]
### VIEWCHONNVKYCVAN – Chọn nhân viên ký công văn
- Lưới 1 «Danh sách nhân viên»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã NV ký [MaNVKyCVan]; Họ lót NV ký [HoLotNVKyCVan]; Tên NV ký [TenNVKyCVan]; Ngày sinh NV ký [NgaySinhNVKyCVanC]; Phái [PhaiNVKyCVan]{chọn}
### VIEWCHONNVKYNY – Chọn nhân viên ký nháy
- Lưới 1 «Chọn nhân viên ký»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã NV ký nháy [MANVKYNY]; Tên NV ký nháy [TENNVKYNY]; Tên ngắn NV ký nháy [TENNVKYNY2]
### VIEWCHONUSER – Chọn user
- Lưới 1 «Danh sách user» (bảng HUser); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: UserName [UserName]; Tên đầy đủ [HotenTK]; Mã nhóm [MaNhom]
  - Cột ẩn: Tên nhóm [TenNhom]
### VIEWCQDVNHCVAN – CQ/ĐV nhận công văn
- Lưới 1 (bảng NDMDV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đơn vị [MaDV]; Tên đơn vị [TenDV]; Tên viết tắt [VtDV]; Đã đọc công văn [DaDocCVan]; Đã gửi mail [DaGuiMail]
  - Cột ẩn: Đơn vị cấp trên [IDDVP]
### VIEWFILECONGVANCT – Chi tiết file công văn
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Thứ tự [TTFCVanCT]; File công văn [FileCVan]; Loại file công văn [LoaiFileCVan]
### VIEWMAPUSER – Map user và nhân viên
- Lưới 1 «Danh sách liên kết» (bảng HMapUser); tắt: Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Họ lót [HoLotNV]; Tên nhân viên [TenNV]; Tên đầy đủ [HotenTK]; Đơn vị [IDDV]; Tên đơn vị [TenDV]; Phân nhóm [PlUserMap]
  - Cột ẩn: Mã viên chức [IDNV]; ID user [IDUser]; Mã User [UserName]
  - Ô trên form sửa: #HoLotNV, #TenNV, #HotenTK, #IDNV, #IDUser
### VIEWTHEMFILECONGVAN – Thêm file công văn
- Lưới 1 «Danh sách file» (bảng CFCVan); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Thứ tự file [TTFCVan]; Tiêu đề tập tin [TDFCVan]; Xem tập tin [VIEWFILE]
  - Ô trên form sửa: #TTFCVan, #TDFCVan
