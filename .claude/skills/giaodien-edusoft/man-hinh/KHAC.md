# KHAC – Chưa gán phân hệ

## Menu (đường dẫn → lớp màn hình)

- `B33.01` Danh mục nhóm lương

## Màn hình (view) và lưới

### AA – aa
- Lưới 1 (bảng EEDMMinhChung); tắt: Xuất, Nạp lại, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Mã user [MaUser]; Mã khối [IDKhoi]; Tên lớp [TenLop]; Không quản lý [HuyLop]
  - Cột ẩn: Lớp mặc định [DfLop]; Ghi chú [GcLop]; Lớp sinh viên [IDLop]; ID trường liên kết [IDTruongLT]; Ngày thêm [NgayThem]; Thứ tự [TTLop]; Tên tiếng anh [TenLopEg]; Tên viết tắt [VTLop]
### AQ10.10 – File hướng dẫn AQ
- Lưới 1 «Tài liệu/ Video hướng dẫn sử dụng EdusoftNET» (bảng AQFileHuongDan); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Thứ tự [TTFileHuongDan]; Tên chức năng, nghiệp vụ [TenFileHuongDan]; Link file video youbute [LinkVideo]; LinkFileQuyTrinh [LinkFileQuyTrinh]; Ghi chú hướng dẫn [GcFileHuongDan]; Xem chi tiết [XemChiTiet]
### AQ_ChonField – View chon fiel
- Lưới 1 «Danh sách field thông tin sinh viên»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã field [MaField](chỉ đọc); Tên Field [TenField](chỉ đọc)
### AQ_ViewChon1DB – View chọn 1 địa bàn
- Lưới 1 «Danh sách địa bàn» (bảng NDMDB); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã địa bàn [MaDB]; Tên địa bàn [TenDB]
### AQADDINMIN – Giao diện nhập addin tối thiểu
- Lưới 1 «Danh sách addin tối thiểu» (bảng AQADDINMIN); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã phân hệ [IDPhanHe]; Tên phân hệ [TenPhanHe]; Mã addin [IDAddin]; Tên addin [TenAddin]
  - Ô trên form sửa: #IDPhanHe, #IDAddin
### AQADDINREQUIRE – Giao diện nhập addin tiên quyết
- Lưới 1 «Danh sách addin tiên quyết» (bảng AQADDINREQUIRE); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã addin [IDAddin]; Tên addin [TenAddin]; Tên addin tiên quyết [TenAddinRQ]; Mã addin tiên quyết [IDADDINRQ]
  - Ô trên form sửa: #IDAddin, #IDADDINRQ
### AQADDINTRUONG – Danh sách addin của các trường
- Lưới 1 (bảng AQAddinTruong); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã addin [MaAddin]; Mã trường tổ chức thi [MaTruong]; Kinh phí [KinhPhi]; Tên addin [TenAddin]
  - Cột ẩn: Mã addin [IDAddin]; Mã trường [IDTruong]
  - Ô trên form sửa: #IDAddin, #IDTruong
### AQBGQD – Bảng qui đổi hệ điểm
- Lưới 1; tắt: Import, Xuất, In, Nạp lại, Gộp mã, Sửa trên lưới, Sửa bên phải
- Lưới 2 (bảng AQBgQDCT); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### AQCAYCHUCNAND – Danh muc cay chu nang
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Nút btnUpdate: "Sửa" (F2)
### AQDELETE – Giao diện file log delete
- Lưới 1 (bảng AQDmFile); tắt: Thêm, Xóa, Import, In, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã file [MaFile](chỉ đọc); Tên file [TenFile](chỉ đọc); Số lượng [SoLuong]; Field dữ liệu bị update rỗng [SetNull](chỉ đọc)
### AQDHCDNG – Danh sách DHCD - Ngành khối
- Lưới 1 «Danh mục đại học cao đẳng ngành» (bảng AQDHCDNg); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Đại học CD [IDDHCD]; Tên DHCD ngành [TenDHCDNg]; Mã ngành BGD [MaNgBGD]; Khối thi [KhoiThi]; Loại ngành [LoaiNganh]
  - Cột ẩn: Tên tiếng anh [TenDHCDNgEg]; Tổ chức thi ngành [ToChucThiNg]
  - Ô trên form sửa: #IDDHCD, #TenDHCDNg, #MaNgBGD, #KhoiThi, #LoaiNganh, #TenDHCDNgEg, #ToChucThiNg
### AQDMADDIN_OLD – Danh mục Addin
- Lưới 1 (bảng AQDMAddin); tắt: Import, In, Nạp lại, Gộp mã, Sửa trên lưới
  - Cột: Mã addin [MaAddin]; Tên phân hệ [TenPhanHe]; Tên addin [TenAddin]
  - Cột ẩn: Hình phân hệ [AvatarPhanHe]; Addin mặc định [DfAddin]; Phân hệ mặc định [DfPhanHe]; Điều kiện [DieuKien]; Dieu kiện (2) [DieuKien1]; Ghi chú [GcAddin]; Ghi chú [GcPhanHe]; Không quản lý [HuyAddin]; Không quản lý [HuyPhanHe]; Kinh phí [KinhPhi]; Mã phân hệ [MaPhanHe]; Nhóm công việc [NhomCongViec]; Phiên bản [PhienBan]; Phiên bản mặc định [PhienBanMacDinhSD]; Tên tiếng anh [TenAddinEg]; Tên tiếng anh [TenPhanHeEg]; Thứ tự [TtAddin]; Thứ tự [TtPhanhe]; Vai trò [UserRole]; Tên viết tắt [VtAddin]; Tên viết tắt [VtPhanHe]; Tên viết tắt [VtPhanHe2]
  - Ô trên form sửa: #MaAddin, #TenAddin, #MaPhanHe, #PhienBan, #VtAddin
### AQDMBAC – Danh mục bậc đào tạo (AQ)
- Lưới 1 «Danh mục bậc» (bảng AQDMBac); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã bậc [MaBac]; Tên bậc đào tạo [TenBac]; Tên viết tắt [VtBac]
  - Cột ẩn: Ghi chú [GcBac]; Tên tiếng anh [TenBacEg]
  - Ô trên form sửa: #MaBac, #TenBac, #VtBac, #GcBac, #TenBacEg
### AQDMCAPKKSV – Danh mục cấp khen thưởng kỷ luật sinh viên
- Lưới 1 «Danh mục cấp khen thưởng kỷ luật sv» (bảng AQDMCAPKKSV); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã cấp KTKL [MaCapKKSV]; Tên cấp KTKL [TenCapKKSV]; Viết tắt KTKL [VtCapKKSV]
  - Cột ẩn: Ghi chú KTKL [GcCapKKSV]; Tên tiếng anh [TenCapKKSVEg]
  - Ô trên form sửa: #MaCapKKSV, #TenCapKKSV, #VtCapKKSV, #GcCapKKSV, #TenCapKKSVEg
### AQDMCC – Danh mục chứng chỉ (AQ)
- Lưới 1 «Danh mục chứng chỉ» (bảng AQDMCC); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã chứng chỉ [MaCC]; Tên chứng chỉ [TenCC]; Tên viết tắt [VtCC]
  - Cột ẩn: Ghi chú [GcCC]; Tên tiếng anh [TenCCEg]
  - Ô trên form sửa: #MaCC, #TenCC, #VtCC, #GcCC, #TenCCEg
### AQDMCHUCNANG_OLD – Danh mục chức năng
- Lưới 1 (bảng AQDMChucNang); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã chức năng [MaChucNang]; Tên chức năng [TenChucNang]; Mã View [MAVIEW1]
  - Cột ẩn: Hình chức năng [AvatarChucNang]; Hình view [AvatarView]; Refresh [DblClickRefresh]; Chức năng mặc định [DfChucNang]; View mặc định [DfView1]; Điều kiện [DieuKien]; Dieu kiện (2) [DieuKien1]; Ghi chú [GcChucNang]; Ghi chú [GcView1]; ẩn spliter [HideSpliter]; Không quản lý [HuyChucNang]; Không quản lý [HuyView1]; ID chức năng [IDChucNang]; ID chức năng cha [IDChucNangParent]; ID Form [IDForm]; ID phận hệ chính [IDPHChinh]; ID Report [IDReport1]; ID nhóm View [IDView0]; ID View 1 [IDView1]; Mã user [MaUser]; Mã view công bố [MaView1CB]; Ngày thêm [NgayThemC]; Không lên menu [NoShowMenu]; Para 1 [Param1]; Para 2 [Param2]; Para 3 [Param3]; Para 4 [Param4]; Quyển admin [QynAdmin]; Thứ tự [TTView1]; Tên tiếng anh [TenChucNangEg]; Tên trường thông tin [TenView1]; Tên tiếng anh [TenView1Eg]; Thứ tự [TtChucNang]; Kiểu Spliter [TypeSpliter]; Vai trò [UserRole]; Tên viết tắt [VtChucNang]; Tên viết tắt [VtChucNang1]; Tên viết tắt [VtView1]; Tên viết tắt [VtView2]
  - Ô trên form sửa: #MaChucNang, #TenChucNang, #MAVIEW1, #DieuKien, #GcChucNang, #VtChucNang1
### AQDMCHUCVU – Danh mục chức vụ (AQ)
- Lưới 1 «Danh mục chức vụ» (bảng AQDMChucVu); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã chức vụ [MaChucVu]; Tên chức vụ [TenChucVu]; Tên viết tắt [VtChucVu]
  - Cột ẩn: Ghi chú [GcChucVu]; Tên tiếng anh [TenChucVuEg]
  - Ô trên form sửa: #MaChucVu, #TenChucVu, #VtChucVu, #GcChucVu, #TenChucVuEg
### AQDMDB – Danh mục địa bàn (AQ)
- Lưới 1 «Danh mục địa bàn» (bảng AQDmDB); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã địa bàn [MaDB]; Tên địa bàn [TenDB]; Tên viết tắt [VTDB]; ID địa bàn cha [IDDBC]
  - Cột ẩn: Ghi chú [GCDB]; Loại hình [LoaiHinh]{chọn}; Tên tiếng anh [TenDBEg]
  - Ô trên form sửa: #MaDB, #TenDB, #VTDB, #GCDB, #LoaiHinh, #TenDBEg
### AQDMDCS – Danh mục diện chính sách sinh viên (AQ)
- Lưới 1 «Danh mục diện chính sách sinh viên» (bảng AQDMDCS); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã diện chính sách [MaDCS]; Tên diện chính sách [TenDCS]; Tên viết tắt [VtDCS]; Ghi chú [GcDCS]
  - Cột ẩn: Tên tiếng anh [TenDCSEg]
  - Ô trên form sửa: #MaDCS, #TenDCS, #VtDCS, #GcDCS, #TenDCSEg
### AQDMDHCD – Danh mục trường ĐHCD (AQ)
- Lưới 1 «Danh mục đại học cao đẳng» (bảng AQDmDHCD); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã đại học cd [MaDHCD]; Tên đại học CD [TenDHCD]; Viết tắt DHCD [VTDHCD]
  - Cột ẩn: Ghi chú [GCDHCD]; Tên tiếng anh [TenDHCDEg]
  - Ô trên form sửa: #MaDHCD, #TenDHCD, #VTDHCD, #GCDHCD, #TenDHCDEg
### AQDMDLK – Giao diện dữ liệu khoa
### AQDMDT – Danh mục dân tộc (AQ)
- Lưới 1 «Danh mục dân tộc» (bảng AQDMDT); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã dân tộc [MaDT]; Tên dân tộc [TenDT]; Tên viết tắt [VTDT]
  - Cột ẩn: Ghi chú [GCDT]; Tên tiếng anh [TenDTEg]
  - Ô trên form sửa: #MaDT, #TenDT, #VTDT, #GCDT, #TenDTEg
### AQDMENUM – Danh mục Enum (AQ)
- Lưới 1 «Danh sách giá trị enum» (bảng AQEnumCT); tắt: Xuất, In, Nạp lại, Gộp mã, Sửa trên lưới
  - Cột: Giá trị enum [TTEnumCT]{số}; Tên giá trị enum [ConstEnum]; Ghi chú [GCENumCT]; Mã Enum [MaEnum]; Viết tắt (AQ) [VTENumCT]
  - Cột ẩn: Điều kiện [DieuKien]; Dieu kiện (2) [DieuKien1]; Tên tiếng anh [GCEnumCTEg]; ID Enum [IDEnum]; ID Enum CT [IDEnumCT]; Vai trò [UserRole]
  - Ô trên form sửa: #TTEnumCT, #ConstEnum, #GCENumCT, #VTENumCT, #DieuKien, #DieuKien1, #GCEnumCTEg
- Lưới 2 «Danh sách enum» (bảng AQDmENum); tắt: Import, Xuất, In, Nạp lại, Gộp mã, Sửa trên lưới
  - Cột: Mã Enum [MaEnum]; Tên Enum [TenEnum]; ID Enum [IDEnum]; Mã phân hệ [MaPhanHe]; Mã phân hệ [IDPhanHe]
  - Cột ẩn: Ghi chú [GCENum]; Nhóm enum [NhomENum]; STT [TTEnum]{số}; Tên viết tắt [VtEnum]
  - Ô trên form sửa: #MaEnum, #TenEnum, #IDPhanHe, #GCENum, #VtEnum
### AQDMFIELD – Danh mục field (AQ)
- Lưới 1 «Danh sách field» (bảng AQDmField); tắt: Xuất, Gộp mã, Sửa trên lưới
  - Cột: Mã field [MaField]; Tiêu đề hiển thị trên view [VtField]; Tên Field [TenField]; Phân loại field [plfield]{chọn}; Độ dài field [DoDaiField]{số}; Độ dài DB [LenDB]{số}; Kiểu field view [SpecType0]; Field ảo khác [FieldAoKh]; Map To [MapTo]; ID Field [IDField]; Ghi chú [GcField]; Mã user [MaUser]; Ngày thêm [NgayThemC]
  - Cột ẩn: Điều kiện [DieuKien]; Dieu kiện (2) [DieuKien1]; Field Alias [FieldAlias]; ID Enum [IDEnum]; Kiểu field DB [SpecType]{chọn}; Tên label [Tenlabel]; Tooltip [TextBoxToolTip]
  - Ô trên form sửa: #MaField, #VtField, #TenField, #plfield, #DoDaiField, #LenDB, #SpecType0, #MapTo, #GcField, #DieuKien, #DieuKien1, #FieldAlias, #IDEnum, #SpecType, #Tenlabel, #TextBoxToolTip
### AQDMFILE – Danh mục file (AQ)
- Lưới 1 «Danh mục file» (bảng AQDmFile); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã file [MaFile]; Tên file [TenFile]; Tên viết tắt [VtFile]; Nhóm file [MaFile0]; Phân hệ chính [PHChinh]; Mã addin [IDAddin]; ID Addin 2 [idaddin2]; Phân loại file [PlFile1]{chọn}; Thứ tự [TtFile]; AQ alias [AQAlias]; Invalid key phụ [InvalidKeyPhu]; Allway? [IsAlway]; Tên tiếng anh [TenFileEg]; Điều kiện [DieuKien]; ID view danh mục [IDViewDM]; Dieu kiện (2) [DieuKien1]; Ghi log [NotLog]{chọn}; Danh mục? [IsDM]; File mã [FileMapp]; Alias file [Alias]; Ngoài db [NotInDB]; Quản lý file [Owned]; File hệ thống? [IsFileHeThong]; File tree [IsFileTree]; Prefix [Fprefix]; File quan trọng [FileQT]; Loại DVQL [LoaiDVQL]{chọn}; WarnAltKey [WarnAltKey]
  - Cột ẩn: Ghi chú [GcFile]; Nhóm file [IDFile0]; Mã phân hệ [MaPhanHe]
  - Ô trên form sửa: #MaFile, #TenFile, #VtFile, #PHChinh, #IDAddin, #idaddin2, #PlFile1, #TtFile, #AQAlias, #DieuKien, #IDViewDM, #DieuKien1, #NotLog, #IsDM, #Alias, #NotInDB, #Owned, #IsFileHeThong, #FileQT, #LoaiDVQL, #WarnAltKey, #GcFile, #IDFile0
  - Nút btnTaoFileSQL: "Tạo file sql" (F7)
### AQDMFILE0 – Danh mục nhóm file (AQ)
- Lưới 1 (bảng AQDmFile0); tắt: Import, Nạp lại, Gộp mã, Sửa trên lưới
  - Cột: Tên phân hệ [TenPhanHe]; Thứ tự [TtFile0]; Mã nhóm [MaFile0]; Tên nhóm [TenFile0]; Tên tiếng Anh [TenFile0Eg]; Mã phân hệ [MaPhanHe]
  - Cột ẩn: Hình phân hệ [AvatarPhanHe]; Nhóm file mặc định [DfFile0]; Phân hệ mặc định [DfPhanHe]; Điều kiện [DieuKien]; Ghi chú [GcFile0]; Ghi chú [GcPhanHe]; Không quản lý [HuyFile0]; Không quản lý [HuyPhanHe]; ID Nhóm file [IDFile0]; Mã phân hệ [IDPhanHe]; Mã user [MaUser]; Tên tiếng anh [TenPhanHeEg]; Thứ tự [TtPhanhe]; Tên viết tắt [VtFile0]; Tên viết tắt [VtPhanHe]; Tên viết tắt [VtPhanHe2]
  - Ô trên form sửa: #TtFile0, #MaFile0, #TenFile0, #TenFile0Eg, #IDPhanHe
### AQDMFILE00 – Danh mục nhóm file
- Lưới 1; tắt: Nạp lại, Sửa trên lưới
### AQDMFORM – Danh mục form (AQ)
- Lưới 1 «Danh sách form» (bảng AQDMForm); tắt: Import, Nạp lại, Gộp mã, Sửa trên lưới
  - Cột: Mã form [MaForm]; Tên viết tắt [VtForm]; Phân loại form [PhanLoaiForm]{chọn}; Form run [FormRun]; Thứ tự hiển thị [TtForm]; ID Form [IDForm]; Điều kiện [DieuKien]; Thứ tự [TTForm0]; Tham số 1 [Param1]; Tên nhóm form [TenForm0]; Không lên menu [NoShowMenu]; Mã addin [IDAddin]; PVLD [PVLD]; Mã phân hệ [IDPhanHe]; ID nhóm form [IDForm0]
  - Cột ẩn: Form mặc định [DfForm]; File DLL [FileDLL]; Ghi chú form [GcForm]; Không quản lý [HuyForm]; Tham số 2 [Param2]; Tham số 3 [Param3]; Tham số 4 [Param4]; Tên Form [TenForm]; Tên tiếng anh [TenFormEg]; Tên phân hệ [TenPhanHe]; Tên viết tắt [VtForm1]
  - Ô trên form sửa: #MaForm, #VtForm, #PhanLoaiForm, #FormRun, #TtForm, #DieuKien, #Param1, #NoShowMenu, #IDAddin, #PVLD, #IDPhanHe, #IDForm0, #GcForm, #Param2, #Param3, #Param4, #TenForm
### AQDMFORM0 – Danh mục nhóm form (AQ)
- Lưới 1 «Danh mục form 0» (bảng AQDmForm0); tắt: Nạp lại, Sửa trên lưới
  - Cột: ID nhóm form [IDForm0]; Mã phân hệ [IDPhanHe]; Mã nhóm form [MaForm0]; Tên nhóm form [TenForm0]; Thứ tự [TTForm0]; Mã phân hệ [MaPhanHe]
  - Cột ẩn: Ghi chú [GCForm0]; Tên tiếng anh [TenForm0Eg]; Tên viết tắt [VTForm0]
  - Ô trên form sửa: #IDPhanHe, #MaForm0, #TenForm0, #TTForm0, #GCForm0, #TenForm0Eg, #VTForm0
### AQDMGCNSV – Danh mục giấy chứng nhận
- Lưới 1 «Danh mục giấy chứng nhận sinh viên» (bảng AQDMGCNSV); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã GCN [MaGCN]; Tên giấy CN [TenGCN]; Tên viết tắt [VtGCN]
  - Cột ẩn: Ghi chú [GcGCN]; Tên tiếng anh [TenGCNEg]
  - Ô trên form sửa: #MaGCN, #TenGCN, #VtGCN, #GcGCN, #TenGCNEg
### AQDMHC – Danh mục học chế (AQ)
- Lưới 1 «Danh sách học chế» (bảng AQDMHC); tắt: Thêm, Import, In, Nạp lại, Sửa trên lưới
  - Cột: Mã học chế [MaHC]; Tên học chế [TenHC]; Tên viết tắt [VtHC]; Ghi chú [GcHC]
  - Cột ẩn: Học chế mặc định [DfHC]; Không quản lý [HuyHC]; ID học chế [IDHC]; Mã user [MaUser]; Ngày thêm [NgayThemC]; Tên tiếng anh [TenHCEg]; Tên HC VB [TenHCVB]; Tên tiếng anh [TenHCVBEg]; Thứ tự [TtHC]
  - Ô trên form sửa: #MaHC, #TenHC, #VtHC, #GcHC, #TenHCEg, #TenHCVB, #TenHCVBEg
### AQDMHE – Danh mục hệ đào tạo (AQ)
- Lưới 1 «Danh mục hệ» (bảng AQDMHe); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã hệ đào tạo [MaHe]; Tên viết tắt [VtHe]; Tên hệ [TenHe]
  - Cột ẩn: Ghi chú [GcHe]; Tên hệ VB [TenHeVB]
  - Ô trên form sửa: #MaHe, #VtHe, #TenHe, #GcHe, #TenHeVB
### AQDMHOCHAM – Danh mục học hàm (AQ)
- Lưới 1 «Danh mục học hàm» (bảng AQDMHocHam); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã học hàm [MaHocHam]; Tên học hàm [TenHocHam]; Tên viết tắt [VtHocHam]
  - Cột ẩn: Ghi chú [GcHocHam]; Tên tiếng anh [TenHocHamEg]
  - Ô trên form sửa: #MaHocHam, #TenHocHam, #VtHocHam, #GcHocHam, #TenHocHamEg
### AQDMHTTHI – Danh mục hình thức thi (AQ)
- Lưới 1 «Danh mục hình thức thi» (bảng AQDMHTTHI); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã hình thức thi [MaHTThi]; Tên hình thức thi [TenHTThi]; Tên viết tắt [VtHTThi]
  - Cột ẩn: Ghi chú [GcHTThi]; Tên tiếng anh [TenHTThiEg]
  - Ô trên form sửa: #MaHTThi, #TenHTThi, #VtHTThi, #GcHTThi, #TenHTThiEg
### AQDMKKSV – Danh mục khen thưởng kỷ luật sinh viên
- Lưới 1 «Danh mục khen thưởng kỷ luật sv» (bảng AQDMKKSV); tắt: Nạp lại, Sửa trên lưới
  - Cột: Loại lý do [LoaiKKSV]{chọn}; Mã KTKL [MaKKSV]; Tên khen thưởng kỷ luật [TenKKSV]; Tên viết tắt [VtKKSV]
  - Cột ẩn: Ghi chú [GcKKSV]; Tên tiếng anh [TenKKSVEg]
  - Ô trên form sửa: #LoaiKKSV, #MaKKSV, #TenKKSV, #VtKKSV, #GcKKSV, #TenKKSVEg
### AQDMLDQD – Danh mục loại quyết đình vào ra nhân viên (AQ)
- Lưới 1 «Danh mục lý do quyết định» (bảng AQDMLDQD); tắt: Nạp lại, Sửa trên lưới
  - Cột: Loại quyết định [LoaiLDQDNS]{chọn}; Mã lý do [MaLDQDNV]; Tên lý do [TenLDQDNV]; Viết tắt [VtLDQDNV]
  - Cột ẩn: Ghi chú [GcLDQDNV]; Tên tiếng anh [TenLDQDNVEg]
  - Ô trên form sửa: #LoaiLDQDNS, #MaLDQDNV, #TenLDQDNV, #VtLDQDNV, #GcLDQDNV, #TenLDQDNVEg
### AQDMLDQDSV – Danh mục loại quyết đình vào ra sinh viên (AQ)
- Lưới 1 «Danh mục lý do quyết định sinh viên» (bảng AQDMLDQDSV); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã lý do [MaLDQDSV]; Tên lý do [TenLDQDSV]; Tên viết tắt [VtLDQDSV]; Loại lý do [LoaiLDQDSV]{chọn}
  - Cột ẩn: Ghi chú [GcLDQDSV]; Tên tiếng anh [TenLDQDSVEg]
  - Ô trên form sửa: #MaLDQDSV, #TenLDQDSV, #VtLDQDSV, #LoaiLDQDSV, #GcLDQDSV, #TenLDQDSVEg
### AQDMLDSDPH – Danh mục loại hình sử dụng phòng (AQ)
- Lưới 1 «Danh mục lý do sứ dụng phòng» (bảng AQDMLDSDPH); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã lý do [MaLDSDPH]; Tên lý do [TenLDSDPH]; Tên viết tắt [VtLDSDPH]
  - Cột ẩn: Ghi chú [GcLDSDPH]; Tên tiếng anh [TenLDSDPHEg]
  - Ô trên form sửa: #MaLDSDPH, #TenLDSDPH, #VtLDSDPH, #GcLDSDPH, #TenLDSDPHEg
### AQDMLHD – Danh mục loại hợp đồng (AQ)
- Lưới 1 «Danh mục loại hợp đồng» (bảng AQDMLHD); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã loại HĐ [MaLHD]; Tên loại HĐ [TenLHD]; Tên viết tắt [VtLHD]
  - Cột ẩn: Có hạn kết thúc hợp đồng [CoHanHD]; Hạn thử việc [CoHanTV]; Có tập sự [CoTS]; Có thực tập [CoTT]; Ghi chú [GCLHD]; Lương ngạch [LUONGNGACH]; Tên tiếng anh [TenLHDEg]
  - Ô trên form sửa: #MaLHD, #TenLHD, #VtLHD, #CoHanHD, #CoHanTV, #CoTS, #CoTT, #GCLHD, #LUONGNGACH, #TenLHDEg
### AQDMLKH – Danh mục loại kế hoạch (AQ)
- Lưới 1 «Danh mục loại kế hoạch» (bảng AQDMLKH); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã loại kế hoạch [MaLKH]; Tên loại kế hoạch [TenLKH]; Tên viết tắt [VtLKH]
  - Cột ẩn: Ghi chú [GCLKH]; Tên tiếng anh [TenLKHEg]
  - Ô trên form sửa: #MaLKH, #TenLKH, #VtLKH, #GCLKH, #TenLKHEg
### AQDMLLCT – Danh mục lý luận chính trị (AQ)
- Lưới 1 «Danh múc lý luận chính trị» (bảng AQDMLLCT); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã lý luận chính trị [MaLLCT]; Tên lý luận chính trị [TenLLCT]; Tên viết tắt [VtLLCT]
  - Cột ẩn: Ghi chú [GcLLCT]; Tên tiếng anh [TenLLCTEg]
  - Ô trên form sửa: #MaLLCT, #TenLLCT, #VtLLCT, #GcLLCT, #TenLLCTEg
### AQDMLLL – Danh mục loại hình lên lương (AQ)
- Lưới 1 «Danh mục loại lên lương» (bảng AQDMLLL); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã loại lên lương [MaLLL]; Tên loại lên lương [TenLLL]; Tên viết tắt [VtLLL]; Mã file word mẫu [IDTmpWord]
  - Cột ẩn: Đổi bậc [DoiBac]; Đổi ngạch [DoiNgach]; Đổi nhóm ngạch [DoiNhNgach]; Ghi chú [GCLLL]; Tên tiếng anh [TenLLLEg]
  - Ô trên form sửa: #MaLLL, #TenLLL, #VtLLL, #IDTmpWord, #DoiBac, #DoiNgach, #DoiNhNgach, #GCLLL, #TenLLLEg
### AQDMLOAICT – Danh mục loại công tác (AQ)
- Lưới 1 «Danh mục loại công tác» (bảng AQDMLoaiCT); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã loại công tác [MaLoaiCT]; Tên loại công tác [TenLoaiCT]; Tên viết tắt [VtLoaiCT]
  - Cột ẩn: Ghi chú [GcLoaiCT]; Tên tiếng anh [TenLoaiCTEg]
  - Ô trên form sửa: #MaLoaiCT, #TenLoaiCT, #VtLoaiCT, #GcLoaiCT, #TenLoaiCTEg
### AQDMLOAIPC – Danh mục cây phân cấp (AQ)
- Lưới 1 (bảng AQDMLoaiPC); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã loại phân cấp [MaLoaiPhanCap]; Tên loại phân cấp [TenLoaiPhanCap]; Không quản lý [HuyLoaiPhanCap]; Thứ tự [TtLoaiPhanCap]; Loai pc mặc định [DfLoaiPhanCap]
  - Cột ẩn: Ghi chú [GCLoaiPhanCap]; Mã user [MaUser]; Tên tiếng anh [TenLoaiPhanCapEg]; Tên viết tắt [VtLoaiPhanCap]
  - Ô trên form sửa: #MaLoaiPhanCap, #TenLoaiPhanCap, #GCLoaiPhanCap, #TenLoaiPhanCapEg, #VtLoaiPhanCap
### AQDMLOAIPHEP – Danh mục loại nghỉ phép (AQ)
- Lưới 1 «Danh mục loại nghỉ phép» (bảng AQDMLoaiPhep); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã loại nghỉ phép [MaLoaiPhep]; Tên loại nghỉ phép [TenLoaiPhep]; Tên viết tắt [VtLoaiPhep]
  - Cột ẩn: Ghi chú [GcLoaiPhep]; Tên tiếng anh [TenLoaiPhepEg]
  - Ô trên form sửa: #MaLoaiPhep, #TenLoaiPhep, #VtLoaiPhep, #GcLoaiPhep, #TenLoaiPhepEg
### AQDMLOAITG – Danh mục loại thời gian
### AQDMMSCAN – Danh mục mẫu scan (AQ)
- Lưới 1 «Danh mục mẫu scan» (bảng AQDMMSCAN); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã Mãu scan [MaMSCAN]; Tên Mãu scan [TenMSCAN]; Viết tắt Mãu scan [VtMSCAN]
  - Cột ẩn: Ghi chú Mãu scan [GcMSCAN]; Tên tiếng anh [TenMSCANEg]
  - Ô trên form sửa: #MaMSCAN, #TenMSCAN, #VtMSCAN, #GcMSCAN, #TenMSCANEg
### AQDMNGACH – Danh mục ngạch (AQ)
- Lưới 1 «Giá trị ngạch» (bảng AQDMNgachCT); tắt: Import, Xuất, In, Nạp lại, Sửa trên lưới
  - Cột: Hệ số lương [HSL]; Bậc lương [BacLuong]; PCVK [PCVK]
  - Ô trên form sửa: #HSL, #BacLuong, #PCVK
- Lưới 2 «Danh mục ngạch» (bảng AQDMNgach); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã ngạch [MaNgach]; Tên ngạch [TenNgach]; Tên viết tắt [VtNgach]
  - Cột ẩn: Ghi chú [GcNgach]; Tên tiếng anh [TenNgachEg]
  - Ô trên form sửa: #MaNgach, #TenNgach, #VtNgach, #GcNgach, #TenNgachEg
### AQDMNgonNgu – Danh mục ngôn ngữ
- Lưới 1 «Danh sách ngôn ngữ» (bảng AQDMNgonNgu); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã [MaNgonNgu]; Tên [TenNgonNgu]; Viết tắt [VtNgonNgu]
  - Cột ẩn: Ghi chú [GcNgonNgu]; Tên tiếng anh [TenNgonNguEg]
  - Ô trên form sửa: #GcNgonNgu, #MaNgonNgu, #TenNgonNgu, #TenNgonNguEg, #VtNgonNgu
### AQDMNH – Danh mục ngân hàng (AQ)
- Lưới 1 «Danh mục ngân hàng» (bảng AQDMNH); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã ngân hàng [MaNH]; Tên ngân hàng [TenNH]; Tên viết tắt [VTNH]; Ghi chú [GCNH]
  - Cột ẩn: Tên tiếng anh [TenNHEg]
  - Ô trên form sửa: #MaNH, #TenNH, #VTNH, #GCNH, #TenNHEg
### AQDMNHNGACH – Danh mục nhóm ngạch nhân viên (AQ)
- Lưới 1 «Danh mục nhóm ngạch» (bảng AQDMNhNgach); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã nhóm ngạch [MaNhNgach]; Tên nhóm ngạch [TenNhNgach]; Tên viết tắt [VtNhNgach]
  - Cột ẩn: Ghi chú [GcNhNgach]; Tên tiếng anh [TenNhNgachEg]
  - Ô trên form sửa: #MaNhNgach, #TenNhNgach, #VtNhNgach, #GcNhNgach, #TenNhNgachEg
### AQDMNHOMPHANHE – Nhóm file theo phân hệ
- Lưới 1 (bảng AQDmFile); tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã file [MaFile]; Tên file [TenFile]; Ghi chú [GcFile]
  - Cột ẩn: Alias file [Alias]; File mặc định [DfFile]; Điều kiện [DieuKien]; Không quản lý [HuyFile]; ID File [IDFile]; ID Nhóm file [IDFile0]; Invalid key phụ [InvalidKeyPhu]; Allway? [IsAlway]; Danh mục? [IsDM]; File hệ thống? [IsFileHeThong]; Mã user [MaUser]; Ngày thêm [NgayThemC]; Quản lý file [Owned]; ID phân hệ chính [PHChinh]; Phân loại file [PlFile]; Tên tiếng anh [TenFileEg]; Thứ tự [TtFile]; Tên viết tắt [VtFile]
  - Ô trên form sửa: #MaFile, #TenFile, #GcFile, #TenFileEg, #VtFile
### AQDMNhomSetting – AQDMNhomSetting
- Lưới 1 (bảng AQDMNhomSetting); tắt: Nạp lại, Sửa trên lưới
  - Cột: TTNhomSetting [TTNhomSetting]; MaNhomSetting [MaNhomSetting]; TenNhomSetting [TenNhomSetting]; VtNhomSetting [VtNhomSetting]; Mã phân hệ [MaPhanHe]; Tên phân hệ [TenPhanHe]
  - Cột ẩn: GcNhomSetting [GcNhomSetting]; Mã phân hệ [IDPhanHe]; Tên tiếng anh [TenNhomSettingEg]
  - Ô trên form sửa: #TTNhomSetting, #MaNhomSetting, #TenNhomSetting, #VtNhomSetting, #GcNhomSetting, #IDPhanHe, #TenNhomSettingEg
### AQDMNODE – Danh mục node của cây phân cấp (AQ)
- Lưới 1 (bảng AQDMNode); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã node [MaNode]; Tên node [TenNode]; Mã file [MaFile]; Mã field [MaField]; Field lọc [FieldLoc]; Điều kiện [DieuKien]; Thứ tự [TtNode]; ID File Field [IDFileField]
  - Cột ẩn: Field mặc định [DfField]; Node mặc định [DfNode]; Dieu kiện (2) [DieuKien1]; Độ dài field [DoDaiField]; Field Alias [FieldAlias]; Field mã [FieldMapp]; Ghi chú [GCNode]; Ghi chú [GcField]; Không quản lý [HuyField]; Không quản lý [HuyNode]; ID Enum [IDEnum]; ID Field [IDField]; Độ dài DB [LenDB]; Mã user [MaUser]; Ngoài db [NotInDB]; Chỉ đọc (View) [ReadOnly]; Kiểu field DB [SpecType]; Tên Field [TenField]; Tên tiếng anh [TenFieldEg]; Tên tiếng anh [TenNodeEg]; Tên label [Tenlabel]; Tên tiếng anh [TenlabelEg]; Tooltip [TextBoxToolTip]; Thứ tự [TtField]; Vai trò [UserRole]; Tên tiếng anh [VTFieldEg]; Tên viết tắt [VtField]; Tên viết tắt [VtNode]; Phân loại field [plfield]
  - Ô trên form sửa: #MaNode, #TenNode, #FieldLoc, #IDFileField, #GCNode, #TenNodeEg
### AQDMPHANHE – Danh mục phân hệ (AQ)
- Lưới 1 «Danh sách phân hệ» (bảng AQDMPhanHe); tắt: Xóa, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Sửa bên phải
  - Cột: Mã phân hệ [MaPhanHe]; Tên phân hệ [TenPhanHe]; Thứ tự [TtPhanhe]; Mã phân hệ [IDPhanHe]; Mã addin [IDAddin]
  - Cột ẩn: Hình phân hệ [AvatarPhanHe]; Chu kỳ con [ChuKyCon]{chọn}; Chy kỳ dữ liệu [ChuKyDL]{chọn}; Ghi chú [GcPhanHe]; Ghi chú [GhiChu]; PDFQuyTrinh [PDFQuyTrinh]; Tên tiếng Anh [TenPhanHeEg]; Tên trên mẫu in [TenTrenMauIn]; Tên viết tắt [VtPhanHe]; Viết tắt 2 [VtPhanHe2]
  - Ô trên form sửa: #MaPhanHe, #TenPhanHe, #TtPhanhe, #IDAddin, #AvatarPhanHe, #ChuKyCon, #ChuKyDL, #GcPhanHe, #GhiChu, #PDFQuyTrinh, #TenPhanHeEg, #TenTrenMauIn, #VtPhanHe, #VtPhanHe2
### AQDMPLCC – Danh mục phân loại chứng chỉ (AQ)
- Lưới 1 «Danh mục phân loại chứng chỉ» (bảng AQDMPLCC); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã phân loại chứng chỉ [MaPLCC]; Tên phân loại chứng chỉ [TenPLCC]; Tên viết tắt [VTPLCC]
  - Cột ẩn: Ghi chú [GCPLCC]; Tên tiếng anh [TenPLCCEg]
  - Ô trên form sửa: #MaPLCC, #TenPLCC, #VTPLCC, #GCPLCC, #TenPLCCEg
### AQDMPLGV – Danh mục phân loại giảng viên (AQ)
- Lưới 1 «Danh mục phân loại giảng viên» (bảng AQDMPLGV); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã phân loại GV [MaPLGV]; Tên phân loại GV [TenPLGV]; Tên viết tắt [VtPLGV]
  - Cột ẩn: Ghi chú [GcPLGV]; Tên tiếng anh [TenPLGVEg]
  - Ô trên form sửa: #MaPLGV, #TenPLGV, #VtPLGV, #GcPLGV, #TenPLGVEg
### AQDMPLNV – Danh mục phân loại nhân viên (AQ)
- Lưới 1 «Danh mục phân loại nghiệp vụ» (bảng AQDMPLNV); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã nghiệp vụ [MaPLNV]; Tên nghiệp vụ [TenPLNV]; Tên viết tắt [VtPLNV]
  - Cột ẩn: Ghi chú [GcPLNV]; Tên tiếng anh [TenPLNVEg]
  - Ô trên form sửa: #MaPLNV, #TenPLNV, #VtPLNV, #GcPLNV, #TenPLNVEg
### AQDMPLTCHI – Danh mục phân loại tiêu chí (AQ)
- Lưới 1 «Danh mục phân loại tiêu chí» (bảng AQDMPLTCHI); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã PL Tiêu chí [MaPLTCHI]; Tên PL Tiêu chí [TenPLTCHI]; Viết tắt PL Tiêu chí [VtPLTCHI]
  - Cột ẩn: Ghi chú PL Tiêu chí [GcPLTCHI]; Tên tiếng anh [TenPLTCHIEg]
  - Ô trên form sửa: #MaPLTCHI, #TenPLTCHI, #VtPLTCHI, #GcPLTCHI, #TenPLTCHIEg
### AQDMQC – Danh mục quy chế (AQ)
- Lưới 1 «Danh mục qui chế» (bảng AQDMQC); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã qui chế [MaQC]; Tên qui chế [TenQC]; Mã học chế [MaHC]
  - Cột ẩn: Học chế mặc định [DfHC]; Qui chế mặc định [DfQC]; Ghi chú [GcHC]; Ghi chú [GcQC]; Không quản lý [HuyHC]; Không quản lý [HuyQC]; ID học chế [IDHC]; ID qui chế [IDQC]; Mã user [MaUser]; Tên học chế [TenHC]; Tên tiếng anh [TenHCEg]; Tên HC VB [TenHCVB]; Tên tiếng anh [TenHCVBEg]; Tên tiếng anh [TenQCEg]; Tên qui chế VB [TenQCVB]; Tên tiếng anh [TenQCVBEg]; Thứ tự [TtHC]; Thứ tự [TtQC]; Tên viết tắt [VtHC]; Tên viết tắt [VtQC]
  - Ô trên form sửa: #MaQC, #TenQC, #MaHC, #GcQC, #TenQCEg, #TenQCVB, #TenQCVBEg
### AQDMREPORT0 – Danh mục nhóm giao diện (AQ)
- Lưới 1 (bảng AQDmReport0); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã nhóm Report [MaReport0]; Tên nh report [TenReport0]; Mã phân hệ [MaPhanHe]
  - Cột ẩn: Hình phân hệ [AvatarPhanHe]; Phân hệ mặc định [DfPhanHe]; Điều kiện [DieuKien]; Dieu kiện (2) [DieuKien1]; Ghi chú [GcPhanHe]; Ghi chú [GcReport0]; Không quản lý [HuyPhanHe]; Tên phân hệ [TenPhanHe]; Tên tiếng anh [TenPhanHeEg]; Tên tiếng anh [TenReport0Eg]; Thứ tự [TtPhanhe]; Vai trò [UserRole]; Tên viết tắt [VtPhanHe]; Tên viết tắt [VtPhanHe2]; Tên viết tắt [VtReport0]
  - Ô trên form sửa: #MaReport0, #TenReport0, #MaPhanHe, #GcReport0, #TenReport0Eg, #VtReport0
### AQDMREPORT1 – Danh mục báo biểu (AQ)
- Lưới 1 «Danh sách report» (bảng AQDMReport1); tắt: Import, Xuất, Nạp lại, Gộp mã, Sửa trên lưới
  - Cột: Mã report [MaReport1]; Mã report công bố [MaReport1CB]; Tên report [TenReport1]; Phân loại report [PhanLoaiReport]{chọn}; Hoc kỳ? [IsHocKy]; ID Report [IDReport1]; ID phận hệ chính [IDPHChinh]
  - Cột ẩn: Dạng in [DangIn]{chọn}; Report mặc định [DfReport1]; Dieu kiện (2) [DieuKien1]; Ghi chú [GcReport1]; Chiều cao report [HeightRP]{số}; Hình thức bgd [HinhThucBGD]{chọn}; Không quản lý [HuyReport1]; In địa điểm ký tên [InDiaDiemKyTen]; In mã user [InMaUser]; In môn TN [InMonTN]{chọn}; In ngày trong ngày ký [InNgayTrgNgayKy]; In tổng số trang [InTongSoTrang]; In theo phách [IsPhachBGD]; Cuối trang [KTCuoiTrang]{số}; Đầu trang [KTDauTrang]{số}; Lề trái [KTLeTrai]{số}; Khổ giấy [KhoGiayIn]{chọn}; Làm tròn [LamTronBGD]{chọn}; Loại BGD [LoaiBGD]{chọn}; Loại bgd [LoaiBgDiem]{chọn}; Mã kỳ thi BGD [MaKyThiBGD]; Không show menu [NoShowMenu]; Chi tiết padding [PaddingDetails]; Nhóm đếm lại trang [PageCountGroup]; Scan ngang [ScanNgangBGD]; Chỉnh đếm trang [SetPageCount]; Số dòng sang trang [SoDongSangGroup]{số}; Số sv/trang [SoSVTrang]{số}; Tên tiếng anh [TenReport1Eg]; Tên viết tắt [VtReport1]; Độ rộng report [WidthRP]{số}
  - Ô trên form sửa: #MaReport1, #MaReport1CB, #TenReport1, #PhanLoaiReport, #IsHocKy, #IDReport1, #IDPHChinh, #DangIn, #DfReport1, #GcReport1, #HeightRP, #HinhThucBGD, #InDiaDiemKyTen, #InMaUser, #InMonTN, #InNgayTrgNgayKy, #InTongSoTrang, #IsPhachBGD, #KTCuoiTrang, #KTDauTrang, #KTLeTrai, #KhoGiayIn, #LamTronBGD, #LoaiBGD, #LoaiBgDiem, #MaKyThiBGD, #NoShowMenu, #PaddingDetails, #ScanNgangBGD, #SoDongSangGroup, #SoSVTrang, #VtReport1, #WidthRP
  - Nút btnCopy: "Copy report" (F8)
  - Nút btnAdd: "Thêm" (a)
  - Nút btnChinhDinh: "Chỉnh định report" (r)
  - Nút btnPrint: "In" (p)
  - Nút btnUpdate: "Sửa" (u)
- Lưới 2 «Danh sách source» (bảng AQReport); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: ID Detail Key [IDDetailKey]; Cấu trúc source [RecordResource]{chọn}; Nguồn [Source]{số}; Gộp họ và tên chung cột [MergeHoTen]
  - Cột ẩn: ID Report [IDReport]; ID Report [IDReport1]; In group footer? [IsGroupFooter]; Nhiều hàng detail? [IsMulDetail]; Link source [LinkSource]; Mã user [MaUser]
  - Ô trên form sửa: #IDDetailKey, #RecordResource, #Source, #MergeHoTen, #IsMulDetail, #LinkSource
  - Nút btnUpdate: "Cập nhật" (F10)
### AQDMREPORT1_ – Danh mục báo biểu
### AQDMTCPHONG – Danh mục tính chất phòng (AQ)
- Lưới 1 «Danh mục tính chất phòng» (bảng AQDMTCPhong); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã tính chất phòng [MaTCPhong]; Tên tính chất phòng [TenTCPhong]; Tên viết tắt [VtTCPhong]
  - Cột ẩn: Ghi chú [GcTCPhong]; Tên tiếng anh [TenTCPhongEg]
  - Ô trên form sửa: #MaTCPhong, #TenTCPhong, #VtTCPhong, #GcTCPhong, #TenTCPhongEg
### AQDMTCXH – Danh mục trợ cấp xã hội (AQ)
- Lưới 1 «Danh mục trợ cấp xã hội» (bảng AQDMTCXH); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã trợ cấp xã hội [MaTCXH]; Tên trợ cấp xã hội [TenTCXH]; Tên viết tắt [VtTCXH]; Ghi chú [GcTCXH]
  - Cột ẩn: Tên tiếng anh [TenTCXHEg]
  - Ô trên form sửa: #MaTCXH, #TenTCXH, #VtTCXH, #GcTCXH, #TenTCXHEg
### AQDMTG – Danh mục tôn giáo (AQ)
- Lưới 1 «Danh mục tôn giáo» (bảng AQDMTG); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã tôn giáo [MaTG]; Tên tôn giáo [TenTG]; Viết tắt [VTTG]
  - Cột ẩn: Ghi chú [GCTG]; Tên tiếng anh [TenTGEg]
  - Ô trên form sửa: #MaTG, #TenTG, #VTTG, #GCTG, #TenTGEg
### AQDMTREE – Danh mục tree
- Lưới 1 «Chi tiết cây» (bảng AQTreeCT); tắt: In, Nạp lại, Gộp mã, Sửa trên lưới
  - Cột: Cấp tree [CapTree]{số}; ID File [IDFile]; ID Field [IDField]
- Lưới 2 «Danh mục cây» (bảng AQDMTREE); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã tree [MaTree]; Tên tree [TenTree]; Viết tắt tree [VtTree]; Cây nguồn [SourceTree]
  - Cột ẩn: Ghi chú tree [GcTree]; Tên tiếng anh [TenTreeEg]
  - Ô trên form sửa: #MaTree, #TenTree, #VtTree, #GcTree, #TenTreeEg
### AQDMTRUONG – Danh mục trường sử dụng (AQ)
- Lưới 1 «Danh sách trường sử dụng EdusoftNET» (bảng AQDMTruong); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã trường tổ chức thi [MaTruong]; Tên trường [TenTruong]; Ngày hết hạn bảo trì [NgaySudung]
  - Ô trên form sửa: #MaTruong, #TenTruong, #NgaySudung
### AQDMVBCC – Danh mục văn bằng chứng chỉ (AQ)
- Lưới 1 «Danh mục văn bằng chứng chỉ» (bảng AQDMVBCC); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã VBCC [MaVBCC]; Tên VBCC [TenVBCC]; Viết tắt VBCC [VtVBCC]
  - Cột ẩn: Ghi chú [GcVBCC]; Tên tiếng anh [TenVBCCEg]
  - Ô trên form sửa: #MaVBCC, #TenVBCC, #VtVBCC, #GcVBCC, #TenVBCCEg
### AQDMVERSION – Danh sách phiên bản
- Lưới 1; tắt: Thêm, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Sửa bên phải
  - Cột: Mã phiên bản [MaVersion](chỉ đọc); Tên phiên bản [TenVersion](chỉ đọc); Tên viết tắt [VtVersion](chỉ đọc); Tên tiếng anh [TenVersionEg](chỉ đọc)
  - Cột ẩn: Phiên bản mặc định [DfVersion](chỉ đọc); Ghi chú [GcVersion](chỉ đọc); Không quản lý [HuyVersion](chỉ đọc); ID phiên bản [IDVersion](chỉ đọc); Thứ tự [TTVersion](chỉ đọc)
  - Ô trên form sửa: #MaVersion, #TenVersion, #VtVersion, #TenVersionEg, #DfVersion, #GcVersion, #HuyVersion, #TTVersion
  - Nút btnSave: "Save" (F10)
  - Nút btnXemField: "Xem field phiên bản" (F3)
  - Nút btnXemRelation: "Xem relation phiên bản" (F4)
  - Nút btnSoSanhVersion: "So sánh"
### AQDMVIEW0 – Danh mục nhóm giao diện (AQ)
- Lưới 1 (bảng AQDmView0); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã nhóm View [MaView0]; Tên nhóm View [TenView0]; Mã phân hệ [MaPhanHe]
  - Cột ẩn: Hình phân hệ [AvatarPhanHe]; Phân hệ mặc định [DfPhanHe]; Nhóm view mặc định [DfView0]; Điều kiện [DieuKien]; Dieu kiện (2) [DieuKien1]; Ghi chú [GCView0]; Ghi chú [GcPhanHe]; Không quản lý [HuyPhanHe]; Không quản lý [HuyView0]; Mã phân hệ [IDPhanHe]; ID nhóm View [IDView0]; Mã user [MaUser]; Ngày thêm [NgayThemC]; Thứ tự [TTView0]; Tên phân hệ [TenPhanHe]; Tên tiếng anh [TenPhanHeEg]; Tên tiếng anh [TenView0Eg]; Thứ tự [TtPhanhe]; Vai trò [UserRole]; Tên viết tắt [VTView0]; Tên viết tắt [VtPhanHe]; Tên viết tắt [VtPhanHe2]
  - Ô trên form sửa: #MaView0, #TenView0, #MaPhanHe, #GCView0, #TenView0Eg, #VTView0
### AQDMVIEW1 – Danh mục giao diện (AQ)
- Lưới 1 «Danh sách» (bảng AQView); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Là danh mục [IsDanhMuc]; Bảng chính [MainTable]; Là học kỳ [IsHocKy]{chọn}; Nguồn [Source]{số}; ID file import1 [IDFileImp1]; ID file import 2 [IDFileImp2]; Thêm mới liên tục [IsNewLoop]
  - Cột ẩn: ID View [IDView]; ID View 1 [IDView1]; Multi-check [IsMulCheck]; Có tính tổng [IsTotal]; Tính tổng theo nhóm [IsTotalGrp]; Loại view [IsTree]{chọn}; Bar manager? [IsUseBarManager]; Key relation [KeyRelation]; Link source [LinkSource]; Không delete [NoneDelete]; Không delete file [NoneDeleteFile]; Không đổi mã [NoneDoiMa]; Không sửa view [NoneEditL]; Không sửa edit [NoneEditR]; Không export [NoneExport]; Không gộp mã [NoneGopMa]; Không import [NoneImport]; Không thêm mới [NoneInsert]; Không in [NonePrint]; Không thoát [NoneQuit]; Không refresh [NoneRefresh]; NoneSua [NoneSua]; Nguồn source [RecordSource]{chọn}; Left spliter [SLeft]{số}; Top Spliter [STop]{số}; Wheight spliter [SWidthHeight]{số}; Kiểu VerHor [TypeVerHor]{chọn}; Loại view [TypeView]{chọn}
  - Ô trên form sửa: #IsDanhMuc, #MainTable, #IsHocKy, #Source, #IDFileImp1, #IDFileImp2, #IsNewLoop, #IsMulCheck, #IsTotal, #IsTotalGrp, #IsTree, #IsUseBarManager, #KeyRelation, #LinkSource, #NoneDelete, #NoneDeleteFile, #NoneDoiMa, #NoneEditL, #NoneEditR, #NoneExport, #NoneGopMa, #NoneImport, #NoneInsert, #NonePrint, #NoneQuit, #NoneRefresh, #NoneSua, #RecordSource, #SLeft, #STop, #SWidthHeight, #TypeVerHor, #TypeView
- Lưới 2 «Danh mục view» (bảng AQDMView1); tắt: Import, Xuất, In, Nạp lại, Gộp mã, Sửa trên lưới
  - Cột: Mã view [MAVIEW1](chỉ đọc); Tên view [TenView1]; IDView [IDView1](chỉ đọc)
  - Cột ẩn: Hình view [AvatarView]; Có sub view [CoSubView]; Refresh [DblClickRefresh]; View mặc định [DfView1]; Điều kiện [DieuKien]; Dieu kiện (2) [DieuKien1]; Ghi chú [GcView1]; ẩn spliter [HideSpliter]; Không quản lý [HuyView1]; ID phận hệ chính [IDPHChinh]; Loại BGD [LoaiBGD]{chọn}; Mã view công bố [MaView1CB]; Không lên menu [NoShowMenu]; Thứ tự [TTView1]; Tên tiếng anh [TenView1Eg]; Kiểu Spliter [TypeSpliter]; Vai trò [UserRole]; Tên viết tắt [VtView1]; Tên viết tắt [VtView2]
  - Ô trên form sửa: #MAVIEW1, #TenView1, #IDView1, #CoSubView, #DblClickRefresh, #GcView1, #HideSpliter, #IDPHChinh, #LoaiBGD, #MaView1CB, #NoShowMenu, #TypeSpliter
  - Nút btnSave: "Save" (F10)
  - Nút btnRunView: "Định nghĩa field view" (F1)
  - Nút btncopy: "Copy View" (F3)
### AQFIELDREPORT – Thuộc tính báo biểu
- Lưới 1 «Danh sách field trong report» (bảng AQFieldReport); tắt: Thêm, Xóa, Import, Xuất, Nạp lại, Đổi mã, Sửa bên phải
  - Cột: Field Alias [FieldAlias](chỉ đọc); Tên Field [TenField](chỉ đọc); Không group [NoneGrp]; Là group chọn [IsGroupChon]; Khg ẩn [NoneHide]; Loại tính tổng [CalType]{chọn}
  - Cột ẩn: Group chọn [GroupChon]; ẩn [Hide]; ID Field [IDField]; ID field report [IDFieldReport]; ID field report 2 [IDFieldReport2]; ID Report [IDReport]; Loại [IsGroup]; Mã user [MaUser]; Ngày thêm [NgayThemC]; Row order [RowOrder]; Thứ tự tab [TabOrder]
### AQFilePTSL – Danh sách file phân tích dữ liệu
- Lưới 1 (bảng AQFilePTSL); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### AQNGGIOCT – View nhập ngoài giờ
- Lưới 1; tắt: Import, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
- Lưới 2; tắt: Import, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### AQRELATION – Danh sách relation
- Lưới 1 «Danh sách relation» (bảng AQRelation); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: File Cha [IDFileP]; File con [IDFileC]; Field table cha [IDFieldP]; Field table con [IDFieldC]; phamvirel [Phamvirel]; Loại relation [RelationType]{chọn}; Ràng buộc xóa [DeleteRule]{chọn}; Relation vòng [RelationLoop]; Relation ảo [RelationVirtual]; Bộ relation [BoRelation]{số}; Mã tree [MaTree]; Update [UpdateRule]{chọn}; Cha chính là con nếu null [PAsCIsNull]; Khóa kép [KeyKep]; Không import [NOTIMPORT]; Loại quan hệ [LoaiQH]{chọn}; Thứ tự relation [ThuTuRel]{số}
  - Cột ẩn: Mã user [MaUser]
  - Ô trên form sửa: #IDFileP, #IDFileC, #IDFieldP, #IDFieldC, #Phamvirel, #RelationType, #DeleteRule, #RelationLoop, #RelationVirtual, #BoRelation, #MaTree, #UpdateRule, #PAsCIsNull, #KeyKep, #NOTIMPORT, #LoaiQH, #ThuTuRel
### AQTREELINK – Tree link
- Lưới 1 (bảng AQTreeLink); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã tree [MaTree]; Tên tree [TenTree]; ID File child [IDFileC]; ID Fileld chile [IDFieldC]
  - Cột ẩn: ID tree [IDTree]
  - Ô trên form sửa: #IDFileC, #IDFieldC, #IDTree
### AQVALUESETTINGDF – Danh sách giá trì chỉnh định mặc nhiên
- Lưới 1 (bảng AQValueSettingDF); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã phân cấp [MaPhanCap]; Mã Setting [MaSetting]; Giá trị [GiaTri]; ID setting df [IDValueSettingDF]; IsLite [IsLite]
  - Cột ẩn: ID cấp đối tượng KLGD [IDCap]; Phân cấp đối tượng tính KLGD (Ví dụ lớp, Bậc hệ) [IDPhanCap]; Mã setting [IDSetting]; Niên học học kỳ [NHHK]; Kỳ thi [NHHKCon]
  - Ô trên form sửa: #GiaTri, #IDValueSettingDF, #IsLite, #IDCap, #IDPhanCap, #IDSetting, #NHHK, #NHHKCon
### AQVIEWADDCTRL – Định nghĩa các sự kiên button cho giao diện
- Lưới 1 «Danh sách view» (bảng AQView); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã view [MAVIEW1]; Tên view [TenView1]; Source [Source]; Bảng chính [MainTable]; ID View [IDView]; ID View 1 [IDView1]
  - Cột ẩn: Hình view [AvatarView]; Refresh [DblClickRefresh]; View mặc định [DfView1]; Điều kiện [DieuKien]; Dieu kiện (2) [DieuKien1]; Ghi chú [GcView1]; ẩn spliter [HideSpliter]; Không quản lý [HuyView1]; ID phận hệ chính [IDPHChinh]; ID nhóm View [IDView0]; Mã view công bố [MaView1CB]; Không lên menu [NoShowMenu]; Thứ tự [TTView1]; Tên tiếng anh [TenView1Eg]; Kiểu Spliter [TypeSpliter]; Vai trò [UserRole]; Tên viết tắt [VtView1]; Tên viết tắt [VtView2]
- Lưới 2 «Danh sách sự kiện button» (bảng AQViewAddCtrl); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Tên button [CommandName]; Hot key [HotKey]; Tool tip [ToolTip]; IDViewLink [IDViewLink]
  - Cột ẩn: Hình view [AvatarView]; Refresh [DblClickRefresh]; View mặc định [DfView1]; Điều kiện [DieuKien]; Dieu kiện (2) [DieuKien1]; Ghi chú [GcView1]; ẩn spliter [HideSpliter]; Không quản lý [HuyView1]; ID add Ctrl [IDAddCtrl]; ID phận hệ chính [IDPHChinh]; ID View [IDView]; ID nhóm View [IDView0]; ID View 1 [IDView1]; Hình Control [ImageCtrl]; Key hệ thống? [IsSysKey]; Vi trí hiển thĩ [LocationDisplay]{chọn}; Mã View [MAVIEW1]; Mã user [MaUser]; Mã view công bố [MaView1CB]; Hàm [Method]; Key method [MethodSyskey]{chọn}; Ngày thêm [NgayThemC]; Không lên menu [NoShowMenu]; Order Index [OrderIndex]; Thứ tự [TTView1]; Tên trường thông tin [TenView1]; Tên tiếng anh [TenView1Eg]; Kiểu Spliter [TypeSpliter]; Vai trò [UserRole]; Tên viết tắt [VtView1]; Tên viết tắt [VtView2]
  - Ô trên form sửa: #CommandName, #HotKey, #ToolTip, #IDViewLink, #ImageCtrl, #IsSysKey, #LocationDisplay, #Method, #MethodSyskey, #OrderIndex
### AQVIEWCHINHDINHREPORT – Chỉnh định báo biểu chung
- Lưới 1 (bảng AQValSetR); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
### BOCHUKY – Bộ chữ ký
- Lưới 1 «Danh mục chữ ký» (bảng HNhChuKyCT); tắt: Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã chữ ký [MaChuKy]; Tên chữ ký [TenChuKy]; Người ký [NguoiKy]; Chức vụ 1 [Chucvu1]
  - Cột ẩn: Hình chữ ký số [ChuKySo]; Chức vụ 2 [Chucvu2]; Chức vụ 3 [Chucvu3]; Chữ ký mặc định [DfChuKy]; Ghi chú [GCChuKy]; Không quản lý [HuyChuKy]; Người ký [IDChuKy]; Nhóm chữ ký [IDNhChuKy]; ID ds nhóm chữ ký [IDNhChuKyCT]; Thứ tự [TTChuKy]; Cấp độ user [UserLevel]; Tên viết tắt [VtChuKy]
  - Ô trên form sửa: #IDChuKy
- Lưới 2 «Danh mục bộ chữ ký» (bảng HDmNhChuKy); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã nhóm chữ ký [MaNhChuky]; Tên nhóm chữ ký [TenNhChuky]; Tên viết tắt [VtNhChuKy]; Ghi chú nhóm chữ ký [GCNhChuKy]
  - Cột ẩn: Cho phép sửa [Chophepsua]; Nh chữ ký mặc định [DfNhChuKy]; Không quản lý [HuyNhChuKy]; Nhóm chữ ký [IDNhChuKy]; Thứ tự [TTNhChuKy]; Tên tiếng anh [TenNhChuKyEg]
  - Ô trên form sửa: #MaNhChuky, #TenNhChuky, #VtNhChuKy, #GCNhChuKy, #TenNhChuKyEg
### CAYPHANCAP – Cây phân cấp
- Lưới 1 «Thông tin cây phân cấp»; tắt: Thêm, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Cấp full [StrCapFull]; Tên [Name]
  - Cột ẩn: Đối tượng tree [DoiTuongTree]; Giá trị [GiaTri]; ID [ID]; ID cấp đối tượng KLGD [IDCap]; Cây phân cấp [IDLoaiPhanCap]; Phân cấp đối tượng tính KLGD (Ví dụ lớp, Bậc hệ) [IDPhanCap]; ID Parent [ParentID]; Tên Node Full [TenNodeFull]
### CAYPHANCAP_EDIT – Cây phân cấp có edit
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Cấp full [StrCapFull]; Tên [Name](chỉ đọc); Ngày đăng ký [NGAYDKTD]{ngày}
  - Cột ẩn: Đối tượng tree [DoiTuongTree]; Giá trị [GiaTri]; ID [ID]; ID cấp đối tượng KLGD [IDCap]; Cây phân cấp [IDLoaiPhanCap]; Phân cấp đối tượng tính KLGD (Ví dụ lớp, Bậc hệ) [IDPhanCap]; ID Parent [ParentID]; Tên Node Full [TenNodeFull]
### CHINHDINHFIELDDONG – Chỉnh định field động
- Lưới 1 «Danh sách field động» (bảng AQFieldReport2); tắt: Nạp lại
  - Cột: Field Alias [FieldAlias](chỉ đọc); Tên Field [TenField](chỉ đọc); Kiểu Footer [TypeFooterMCol]{chọn}; Source tạo sub [SourceMCol]; Tiêu đề [HeaderColumn]; Source tạo cột động (nRow = nColumn) [SourceMCol2]
### CHOICEFILEIMP – Danh sách các cột trong file import
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Sửa bên phải
### Chon_MauTin – Danh sách các mẫu tin
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm học [NhomHoc]; Đợt tính KL [IDDSDOTKL]
  - Cột ẩn: id tổ học [IDToHoc]
### CHONKHOI – Danh mục khối lớp
- Lưới 1 «Chọn khối» (bảng KDMKHOI); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; Tên viết tắt [VtKhoi]; Ghi chú [GcKhoi]
### CTDT_ViewChonMHTD – View chon mon tuong duong
- Lưới 1 «Danh sách môn học tương đương»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Mã MH tương đương [MaMHTD]; Tên MH tương đương [TenMHTD]
### CTDT_ViewChonMonCopy – Chon mon hoc copy
- Lưới 1 «Danh sách môn học»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Niên học học kỳ [NHHK]; Xét học kỳ thứ [HKThu]; Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Nhóm TC [NhomTC]
### CTDT_ViewNhapMHBS – View nhap mon hoc bo sung
- Lưới 1 «Danh sách môn học bổ sung kiến thức ngành»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Mã ngành [MaNganh]{nút …}; Tên ngành [TenNganh](chỉ đọc)
### CTDT_ViewNhapNgMHBS – View nhap nganh mon hoc bo sung
- Lưới 1 «Danh sách khối»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]
  - Cột ẩn: Ghi chú dùng bên detailright [GhiChuView1]
  - Ô trên form sửa: #MaKhoi, #TenKhoi, #GhiChuView1
### CTDT_ViewXemChuan – View xem ctdt chuẩn
- Lưới 1 «Chương trình đào tạo chuẩn» (bảng KCTDTCH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã PB [MaPB]; Mã bậc hệ [MaBH]; Mã Ng/CNg [MaNgChng]; Xét học kỳ thứ [HKThu]; Môn bắt buộc [IsMHBB]; Môn tốt nghiệp? [IsMHTN]; STT [TTCTDTCH]; Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Lý thuyêt [LT]; Thực hành [TH]; Bài tập [BT]; Đề án [DA]; Luận án [LA]; Tốt nghiệp [TN]; Thực tập [TT]; Bài tập lớn [BTL]; Tự học [TUH]; TTLT [TTLT]; TTTH [TTTH]; LMS [LMS]
### CTDT_ViewXemKeHoach – View xem ctdt kế hoạch
- Lưới 1 «Chương trình đào tạo kế hoạch» (bảng KCTDTKH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Mã Ng/CNg [MaNgChng]; Mã khối [MaKhoi]; Niên học học kỳ [NHHK]; Môn bắt buộc [IsMHBB]; Môn tốt nghiệp? [IsMHTN]; STT [TTCTDTKH]; Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Nhóm TC [NhomTC]; Nhánh TC [NhanhTC]; STCMax [STCMax]; STCMin [STCMin]; Lý thuyêt [LT]; Thực hành [TH]; Bài tập [BT]; Đề án [DA]; Luận án [LA]; Tốt nghiệp [TN]; Thực tập [TT]; Bài tập lớn [BTL]; Tự học [TUH]; TTLT [TTLT]; TTTH [TTTH]; LMS [LMS]
### CTDT_ViewXemThucHien – View xem ctdt thực hiện
- Lưới 1 «Chương trình đào tạo thực hiện» (bảng KCTDTKH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Mã Ng/CNg [MaNgChng]; Mã khối [MaKhoi]; Niên học học kỳ [NHHK]; Môn bắt buộc [IsMHBB]; Môn tốt nghiệp? [IsMHTN]; STT [TTCTDTTH]; Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Lý thuyêt [LT]; Thực hành [TH]; Bài tập [BT]; Đề án [DA]; Luận án [LA]; Tốt nghiệp [TN]; Thực tập [TT]; Bài tập lớn [BTL]; Tự học [TUH]; TTLT [TTLT]; TTTH [TTTH]; LMS [LMS]
### D3106 – View hủy điểm bảo lưu
- Lưới 1 «Danh sách điểm bảo lưu» (bảng DDiemBL); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Điểm thành phần [DiemTP]; Niên học học kỳ [NHHK]; Ngày hết hạn [NgayHetHan]{ngày}; Ngày QĐ [NgayQDBL]; Số QĐ [SoQDBL]; GCHuyBL [GCHuyBL]
### D6303 – Tổng hợp điểm năm học
- Lưới 1 «Xem bảng điểm tổng hợp TB các năm học» (bảng DDTBNH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Mã lớp [MaLop]; Năm học [NamHoc]; ĐTBNHL1 [DTBNHL1]; ĐTBNH [DTBNH]; Số TC đạt [SoTCDatNH]; Điểm TB NH H4 Lần 1 [DTBNHH4L1]; Điểm NH 4 [DTBNHH4]; ĐTB NH các môn [DTBNHFU]; ĐTB NH hệ 4 các môn [DTBNHH4FU]; ĐTBNH (3 HK) [DTBNH3HK]; ĐTBNH (3HK) các môn [DTBNH3HKFU]; ĐTBNH (3HK) hệ 4 [DTBNH3HKH4]; ĐTBNH (3HK) hệ 4 các môn [DTBNH3HKH4FU]; Điểm TBNH HK chính [DTBNHHKCH]; Điểm TBNH HK chính hệ 4 [DTBNHHKCHH4]; Số TC đạt NH HK chính [STCDATHKCH]
### D704.11 – In thống kê kết quả theo lớp
- Lưới 1 «Danh sách lớp - ngành - khoa»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Tên lớp [TenLop]; Khóa học [KhoaHoc]; Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]; Mã đơn vị [MaDV]; Tên đơn vị [TenDV]
### D9202 – Danh sách lớp xét chứng chỉ
- Lưới 1 «Danh sách lớp xét chứng chỉ» (bảng DLOPTN); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Lớp sinh viên [IDLop]; Tên lớp [TenLop]; Mã khối [MaKhoi]; Tên khối [TenKhoi]; Tiêu chuẩn [IDTChuan]; Tên tiêu chuẩn [TenTChuan]; Tên chứng chỉ [TenCC]; Đợt xét [IDDotTN]
  - Ô trên form sửa: #IDLop, #TenLop, #MaKhoi, #TenKhoi, #IDTChuan, #TenTChuan, #TenCC, #IDDotTN
  - Nút btnSave: "Lưu" (F10)
### DANHMUCREPORT – Danh mục report
- Lưới 1 «Danh sách report» (bảng AQDMReport1); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã Report [MaReport1]; Tên Report [TenReport1]; Tên viết tắt [VtReport1]; Ghi chú [GcReport1]
### DANHSACHDKTHANHCONG – Danh sách đăng ký thành công
- Lưới 1 «Danh sách đăng ký thành công»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Hiện diện SV [HienDienSV]{chọn}; Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm/tổ [NhomTo]; Tổ TH [ToTH]; Ưu tiên buổi [UUTIENBUOI]; Tên [TenSV2]; Mã lớp [MaLop]; Tên lớp [TenLop]; Ưu tiên dòng [UuTienDong]
### DANHSACHDKTHATBAI – Danh sách đăng ký thất bại
- Lưới 1 «Danh sách đăng ký lỗi»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Hiện diện SV [HienDienSV]{chọn}; Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm/tổ [NhomTo]; Tổ TH [ToTH]; Ưu tiên buổi [UUTIENBUOI]; Tên [TenSV2]; Mã lớp [MaLop]; Tên lớp [TenLop]; Lỗi ràng buộc [ERRORTYPE]{chọn}; Lý do lỗi [LyDoError]; Ưu tiên dòng [UuTienDong]
### DANHSACHLOPDK – Danh sách lớp đăng ký
- Lưới 1 «Danh sách thống kê»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Tên lớp [TenLop]; Số sinh viên [SoSV]; Số môn học đăng ký [SoMHDK]; Số lượng đăng ký [SoLDK]; Số lượng đăng ký thành công [SoLDKTC]; Số lượng đăng ký lỗi [SoLDKLoi]
### DDMDG – Danh mục đánh giá
- Lưới 1 «Danh mục đánh giá» (bảng DDmDG); tắt: In, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã đánh giá [MaDG]; Tên đánh giá [TenDG]; Tên viết tắt [VtDG]; Tên tiếng anh [TenDGEg]; Ghi chú [GCDG]; Thứ tự đạt <= [NgDat]; Nhóm [NhomDG]{chọn}; Tốt nghiệp [IsTOTNG]
  - Ô trên form sửa: #MaDG, #TenDG, #VtDG, #TenDGEg, #GCDG, #NgDat, #NhomDG, #IsTOTNG
  - Nút btnDelete: "Xóa" (F2)
- Lưới 2 «Đánh giá» (bảng DDGCT); tắt: In, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Thứ tự [TTDGCT]; Tên xếp loại [TenDGCT]; Tên tiếng anh [TenDGCTEg]; Tên viết tắt [VtDGCT]; Tên tiếng anh [VtDGCTEg]; Loại ĐG học vụ [LoaiDGHV]{chọn}; Mức cảnh báo [MucCanhBao]
  - Ô trên form sửa: #TTDGCT, #TenDGCT, #TenDGCTEg, #VtDGCT, #VtDGCTEg, #LoaiDGHV, #MucCanhBao
  - Nút btnDelete: "Xóa" (F1)
### DDMPLND1 – Danh mục phân loại nhập điểm 1
- Lưới 1 (bảng DDMPLND); tắt: Xuất, Nạp lại, Gộp mã, Sửa trên lưới
  - Cột: Mã phân loại nhập điểm [MaPLND]; Tên phân loại [TenPLND]; Tên tiếng anh [TenPLNDEg]; Viết tắt phân loại [VtPLND]; Ghi chú phân loại [GcPLND]; Phân loại mặc định [DfPLND]; Hủy phân loại [HuyPLND]; Thứ tự phân loại [TTPLND]; Mã user [MaUser]; Ngày thêm [NgayThem]
  - Ô trên form sửa: #MaPLND, #TenPLND, #TenPLNDEg, #VtPLND, #GcPLND, #DfPLND, #HuyPLND, #TTPLND, #MaUser, #NgayThem
- Lưới 2 (bảng DPLNDCT); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: KH điểm TP [KyHieuTP]; Phân cấp user [PhanCapUser]{chọn}
  - Ô trên form sửa: #KyHieuTP, #PhanCapUser
### DDMXH – Danh mục xếp hạng chung
- Lưới 1 «Danh mục bảng xếp hạng» (bảng DDmXH); tắt: In, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Bảng ĐG [IDDG]; Mã PL [MaXH]; Tên bảng phân loại [TenXH]; Nhóm [NhomXH]{chọn}; Hệ điểm [HeDiem]{chọn}; Thứ tự đạt <= [NgDat]; Số mục xếp loại [Somucxh]; Hạ bậc TK [HaBac]; Mức hạ bậc tích lũy [MucHaBac]; % thi lại tổng kết [KLHPThiLai]; Không HB thi lại TN [KhgHBTLTN]; Xếp loại thi lại TN [XLTNThiLaiTN]; Hạ bậc HK [HaBacHK]; Hạ bậc NH [HaBacNH]; Hạ bậc TN [HaBacTN]; Mức bắt đầu hạ bậc HK [MucBDHBHK]; Mức bắt đầu hạ bậc NH [MucBDHBNH]; Mức bắt đầu hạ bậc TN [MucBDHBTN]; % thi lại học kỳ [PTrTLHBHK]; % thi lại năm học [PTrTLHBNH]; % thi lại tốt nghiệp [PTrTLHBTN]; Có 1 môn TN thi lại 1 lần [XLTNTL1M1L]; Có 1 môn TN thi lại 2 lần [XLTNTL1M2L]; Có 2 môn TN lthi lại 1 lần [XLTNTL2M1L]; Có hạ bậc vượt thời gian ĐT [CoHBQTGDT]; Có hạ bậc vi phạm kỹ luật [CoHBVPKL]; % chỉ xét HP BB trong kế hoạch [HBChiXetHPBB]; Thi lại tốt nghiệp hạ 1 bậc [Ha1BacTLTN]; Mức BHTN cấp 2 [MucBDHBTN2]; % học phần thi lại cấp 2 [PTrTLHBTN2]; Mức HBTN cấp 3 [MucBDHBTN3]; Số môn học lại bị hạ bậc cấp 3 [SoMonHLHBTN3]; Mức hạ bậc tích lũy cấp 3 [MucHaBac3]; Số MH HL HB tích lũy [SoMonHLHB3]; Số MH HL HBHK cấp 3 [SoMonHLHBHK3]; Số MH HL HBNH cấp 3 [SoMonHLHBNH3]; Mức HBNH 3 [MucBDHBNH3]; Mức HBHK cấp 3 [MucBDHBHK3]; Bỏ MH không tính ĐTB HBTN cấp 3 [BoMHKhgTinhDiemTBHBTN3]; Bỏ MH Không tính ĐTB HB cấp 3 [BoMHKhgTinhDiemTBHB3]; Bỏ MH không tính ĐTB HBHK cấp 3 [BoMHKhgTinhDiemTBHBHK3]; Bỏ MH không tính ĐTB HBNH cấp 3 [BoMHKhgTinhDiemTBHBNH3]; % Hạ bậc không xét thi lại [HBXetHLKgXetTL]
  - Ô trên form sửa: #IDDG, #MaXH, #TenXH, #NhomXH, #HeDiem, #NgDat, #Somucxh, #HaBac, #MucHaBac, #KLHPThiLai, #XLTNThiLaiTN, #HaBacHK, #HaBacNH, #HaBacTN, #MucBDHBHK, #MucBDHBNH, #MucBDHBTN, #PTrTLHBHK, #PTrTLHBNH, #PTrTLHBTN, #XLTNTL1M1L, #XLTNTL1M2L, #XLTNTL2M1L, #CoHBVPKL, #HBChiXetHPBB, #Ha1BacTLTN, #MucBDHBTN2, #PTrTLHBTN2, #MucBDHBTN3, #SoMonHLHBTN3, #MucHaBac3, #SoMonHLHB3, #SoMonHLHBHK3, #SoMonHLHBNH3, #MucBDHBNH3, #MucBDHBHK3, #BoMHKhgTinhDiemTBHBTN3, #BoMHKhgTinhDiemTBHB3, #BoMHKhgTinhDiemTBHBHK3, #BoMHKhgTinhDiemTBHBNH3, #HBXetHLKgXetTL
  - Nút btnDelete: "Xóa" (F1)
- Lưới 2 «Ngưỡng xếp hạng» (bảng DXHCT); tắt: In, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Thứ tự xếp loại [TTXHCT]; Ngưỡng xếp loại [NguongXH]; Ngưỡng ĐTB [NguongDTB]; Tên xếp loại [TenDGCT]
  - Ô trên form sửa: #TTXHCT, #NguongXH
  - Nút btnDelete: "Xóa" (F1)
### DIEM_ViewChonNhomHoc_PD – View chon nhon hoc cho ben pho diem
- Lưới 1 «Danh sách môn học»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Nhóm/tổ [NhomTo]
### DIEM_VIewDSDOT_CC – Danh sách đợt xét chứng chỉ
- Lưới 1 «Danh sách đợt xét chứng chỉ» (bảng DDOTTN); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đợt [MaDotTN]; Số QĐ [SoQD]; Ngày ký [NgayKy]{ngày}; Người ký [NguoiKy]; Văn bằng [VanBang]{chọn}; Số sinh viên [SoSV]; Mã chứng chỉ [MaCC]; Tên chứng chỉ [TenCC]
### DIEM_ViewKhoaNhomOline – View khóa/mở khóa nhóm học online
- Lưới 1 «Danh sách nhóm học»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Nhóm/tổ [NhomTo](chỉ đọc); Khóa [IsLock]; Khóa B1 1 [B11LOCK]; Khóa B1 2 [B12LOCK]; Khóa B1 3 [B13LOCK]; Khóa B1 [B1LOCK]; Khóa B2 [B2LOCK]; Khóa B3 [B3LOCK]; Khóa B4 [B4LOCK]; Khóa K1 1 [K11LOCK]; Khóa K1 2 [K12LOCK]; Khóa K1 3 [K13LOCK]; Khóa K1 [K1LOCK]; Khóa K2 [K2LOCK]; Khóa K3 [K3LOCK]; Khóa K4 [K4LOCK]; Khóa C1 [C1LOCK]; Khóa C2 [C2LOCK]; Khóa C3 [C3LOCK]; Khóa C4 [C4LOCK]; Khóa C5 [C5LOCK]; Khóa C6 [C6LOCK]; Khóa Thi [T1LOCK]; Khóa T2 [T2LOCK]; Khóa t3 [T3LOCK]
### DIEM_ViewXemDiem – View xem diem
- Lưới 1 «Danh sách môn học»; tắt: Thêm, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Niên học học kỳ [NHHK]; Tên môn học [TenMH]; Số TC [SoTinChi]; Nhóm/tổ [NhomTo]; Phần trăm B1 [B1PT]; Điểm B1 [B1]; Phần trăm B2 [B2PT]; Điểm B2 [B2]; Phần trăm K1 [K1PT]; Điểm K1 [K1]; Phần trăm K2 [K2PT]; Điểm K2 [K2]; Điểm thi [T1]; Điểm T2 [T2]; Điểm TKHP [DiemHP]; HK hồi tố [HKHoiTo]
### DIEM_XEMSOLANCAP – Xem số lần cấp
- Lưới 1 «Danh sách sinh viên»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Mã lớp [MaLop]; Số lần cấp [SoLanCap]
### DIMPORTTHANHCONG – Dữ liệu import thanh công
- Lưới 1 «Danh sách sinh viên» (bảng KDMMH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Mã môn học [MaMHDK]; Mã môn học thay thế [MaMHTT]
### DIMPORTTHANHCONGCOPY – Dữ liệu import thất bại
- Lưới 1 «Danh sách sinh viên» (bảng KDMMH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Mã môn học [MaMHDK]; Mã môn học thay thế [MaMHTT]
### DIMPORTTHANHCONGCOPYCOPY – Dữ liệu import tồn tại
- Lưới 1 «Danh sách sinh viên» (bảng KDMMH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Mã môn học [MaMHDK]; Mã môn học thay thế [MaMHTT]
### DK0201 – Chọn sinh viên kiểm tra điểm
- Lưới 1 (bảng SSVHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Sinh viên [IDSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Tên lớp [TenLop]; Niên học học kỳ [NHHK]; Sinh viên ngành [SVNganh]
  - Ô trên form sửa: #IDSV, #TenDayDu, #NgaySinhC, #TenLop, #NHHK, #SVNganh
### DKMH_ViewCamDSSVDKMH – View cấm sinh viên đăng ký theo MH
- Lưới 1 «Danh sách sinh viên cấm đăng ký môn học» (bảng MDSLopSVCamDKMH); tắt: Thêm, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV]{nút …}; Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Mã môn học [MaMH]{nút …}; Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc)
### DKMH_ViewChonKhoiDK – View chon khoi dang ky mon hoc
- Lưới 1 «Danh sách khối»; tắt: Thêm, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; Niên khóa [NienKhoa]; Mã khoa [MaKhoa]
### DKMH_ViewNhapDoiTuongDKMH – View nhap doi tuong dang ky mon hoc
- Lưới 1 (bảng MMHDKR); tắt: Thêm, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Nhóm/tổ [NhomTo]; Ghi chú dùng bên detailright [GhiChuView1]; Đã gán [IsDaGan]
  - Cột ẩn: ID [ID]; ID Parent [ParentID]
  - Ô trên form sửa: #MaMH, #TenMH, #SoTinChi, #NhomTo, #GhiChuView1
### DKMH_ViewNhapLopKG_DKONLINE – View nhap lop kg dang ky online
- Lưới 1 «Danh sách lớp»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã lớp [MaLop](chỉ đọc); Tên lớp [TenLop](chỉ đọc); Không đăng ký online [IsKgDKOnline]
### DKMH_ViewXemMHTTSV – View xem mon hoc dksv all hoc ky
- Lưới 1 «Môn học thay thế trước khi đăng ký»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Mã môn học [MaMH]; Mã môn học thay thế [MaMHTT]; Tên môn học [TenMH]; Tên môn học thay thế [TenMHTT]
### DKT3_04 – DSBDDC
- Lưới 1 «Danh Sách Nhật Ký Cấp Bảng In»; tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Phái [Phai]; Ngày sinh [NgaySinhC]; Mã NK IN [MaNKBGIN]; NHHK in [NHHKIn]; Mã report con [SubCode]; Tên Sub report [TenSubReport]; Người in [UserIn]; Ngày in [NgayIn]
### DMCVHT – Danh mục CVHT
- Lưới 1 «Danh sách cố vấn học tập» (bảng NDMNV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Mã cố vấn [MaNV]; Họ lót [HoLotNV]; Tên nhân viên [TenNV]; Phái [PhaiNV]; Ngày sinh [NgSinhNVC]; Số sinh viên [SoSV]
### DQT706 – Danh mục bảng qui đổi 2
- Lưới 1 «Danh mục bảng qui đổi 2»; tắt: Import, Xuất, In, Nạp lại, Gộp mã, Sửa trên lưới
  - Cột: Mã bảng qui đổi [MaBgQD2]; Tên bảng qui đổi [TenBgQD2]; Tên viết tắt [VtBgQD2]; Ghi chú [GCBgQD2]
  - Ô trên form sửa: #MaBgQD2, #TenBgQD2, #VtBgQD2, #GCBgQD2
  - Nút btnDelete: "Xoa" (F1)
### DSCBHDKLTN – Danh sách chọn cán bộ hướng dẫn khóa luận tốt nghiệp
- Lưới 1 «Danh sách giảng viên»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Ngày sinh [NgaySinhNV]; Phái [PhaiNV]{chọn}; Trạng thái [HienDienNV]{chọn}
### DSSVDKKhoaLuanTN – Danh sách sinh viên xét đăng kí khóa luận
- Lưới 1 «Danh sách sinh viên»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Phái [Phai](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Hiện diện SV [HienDienSV]{chọn}(chỉ đọc); Mã lớp [MaLop](chỉ đọc); Tên lớp [TenLop](chỉ đọc); Mã khối [MaKhoi](chỉ đọc); Tên khối [TenKhoi](chỉ đọc); Niên khóa [NienKhoa](chỉ đọc); NHHK vào [NHHKVao](chỉ đọc); NHHK ra [NHHKRa](chỉ đọc); Mã Ng/CNg [MaNgChng](chỉ đọc); Tên ng/chng [TenNgChng](chỉ đọc)
### EEDMToChucKiemDinh – Danh mục tổ chức điểm định
- Lưới 1 «Danh sách tổ chức» (bảng EEDMToChucKiemDinh); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã tổ chức kiểm định [MaToChucKiemDinh]; Tên tổ chức kiểm định [TenToChucKiemDinh]; Tên tiếng anh [TenToChucKiemDinhEg]; Viết tắt [VtToChucKiemDinh]; Ghi chú [GcToChucKiemDinh]
  - Ô trên form sửa: #MaToChucKiemDinh, #TenToChucKiemDinh, #TenToChucKiemDinhEg, #VtToChucKiemDinh, #GcToChucKiemDinh
### EMPTY – View rỗng, chứa data động
- Lưới 1 «Xem thông tin tổng hợp giảng dạy»; tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Từ tháng [TuThang]; Mã trường liên kết [MaDP]; Tên trường liên kết [TenDP]; Mã lớp [MaLop]; Khóa học [KhoaHocTC]; Mã Ng/CNg [MaNgChng]; Mã bậc hệ [MaBH]; Xét học kỳ thứ [HKThu]; Mã bộ môn [MaBOMON]; Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Số tiết môn học [SoTietMH]; Nhóm/tổ [NhomTo]; Công thức học [TENDNTGHOC]; Số lượng buổi [STIETSBUOI]; Sĩ số đã đăng ký [SiSoDDK]; Thời gian học [ThoiGianHoc]; Mã viên chức [MaNV]; Họ lót [HoLotNV]; Tên nhân viên [TenNV]; Số điện thoại [DC_DT1LLNV]; Email [DC_Eml1LLNV]; Mã phân loại GV [MaPLGV]; Mã học hàm [MaHocHam]; Mã trình độ [MaBacNV]; Mã PH [MaPhHK]; Tên phòng [TenPHHK]; Địa chỉ cơ sở [DiaChiCoSo]; Họ tên QLV [TenDayDuQLV]; Điện thoại QLV [SDTQLV]; Họ tên CTV [TenDayDuCTV]; Điện thoại CTV [SDTCTV]; Ngày bắt đầu [NgayBD]{ngày}; Tháng bắt đầu [THANGBD]; Đến ngày [NGAYCT]{ngày}; Đến tháng [THANGCT]; Ngày thi [NgayThi]{ngày}; Tháng thi [THANGTHI]; Ca thi [TietBD]; Số tiết thi [SoTiet]; Mã phòng thi [MaPH]; Ghi chú [GCToHop]
### Export_KqGV – Export kết quả giảng viên dạng data thô
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### FIELDCHANGE – Danh sách field thay đổi
- Lưới 1 (bảng AQDmField); tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Sửa bên phải
  - Cột: Mã file [MaFile]; Mã field [MaField]; Kiểu field view [SpecType0]{chọn}; Cho rỗng [AllowNull]; Độ dài DB [LenDB]; Khóa chính [IsKhoa]; Khóa phụ [IsKhoaPhu]; Mã field so sánh [MaFieldSS]; Mã file so sánh [MaFileSS]; Kiểu field ss [SpecType0SS]; Độ dài DB SS [LenDBSS]; Khóa chính SS [IsKhoaSS]
  - Cột ẩn: Cột điểm động [*DIEM]; *Loại điểm [*LoaiDiem]; Thứ tự môn học đăng ký [*TTMHDK]; Tuần [*TUAN]; Giá trị mặc nhiên (DVPC) [AQDefaultValDVPC]; Giá trị mặc nhiên (Trường) [AQDefaultValTruong]; Điểm B1 [B1]; Điểm B2 [B2]; Giá trị mặc định [Biding]; Điểm C1 [C1]; Điểm C2 [C2]; Số sv chưa nhập điểm [ChuaNhap]; Số sv đã nhập điểm [DaNhap]; Ràng buộc xóa SS [DeleteRuleSS]; Điểm chữ [DiemChu]; Điểm khác [DiemKhac]; Ghi chú [GhiChu]; Hoãn thi [HoanThi]; Điểm K1 [K1]; Điểm K2 [K2]; Điểm K3 [K3]; Điểm K4 [K4]; Lý do thất bại [LyDoError]; Mã loại điểm [MaLoaiDiem]; Mặc định [MacDinh]; Điểm P1 [P1]; Điểm P2 [P2]; Điểm P3 [P3]; Điểm P4 [P4]; Điểm P5 [P5]; Điểm P6 [P6]; Điểm Q1 [Q1]; Điểm Q1 [Q2]; Điểm Q2 mới [Q3]; Điểm Q4 [Q4]; Điểm Q5 [Q5]; Điểm Q6 [Q6]; Số thứ tự trong Report [STTReport]; Số lần đăng ký [SoLDK]; Số lần đăng ký thất bại [SoLDKLoi]; Số lần đăng ký thành công [SoLDKTC]; Số môn học đăng ký [SoMHDK]; Số mẫu tin [SoMauTin]; Số mẫu tin hk cũ [SoRecordHKCu]; Số mẫu tin hk mới [SoRecordHKMoi]; Số sinh viên [SoSV]; Điểm thi [T1]; Điểm T2 [T2]; Điểm T3 [T3]; Điểm tổng kết học phần [TK]; Điểm tổng kết kiểm tra [TKK]; Điểm tổng kết thi [TKT]; Thứ tự [TTFileField]; Thứ tự tuần [TTTuan]; Tuần 1 [TUAN1]; Tuần 3 [TUAN3]; Bảng phụ SS [TableCSS]; Bảng chính SS [TablePSS]; Tên loại điểm [TenLoaiDiem]; Tên tuần [TenTuan]; Thông tin [ThongTin]; Tổ TH [ToTH]; Tổng cộng [TongCong]; Ràng buộc sửa SS [UpdateRuleSS]; Tên viết tắt [VTTuan]
### FIELDOFFILE – Danh sách field của file
- Lưới 1 (bảng AQFileField); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa bên phải
  - Cột: TT file field [TTFileField]; ID Field [IDField]; Kiểu field view [SpecType0]{chọn}; Độ dài DB [LenDB]; Cho rỗng [AllowNull]; Khóa chính [IsKhoa]; Khóa phụ [IsKhoaPhu]; Giá trị mặc định [Biding]
  - Cột ẩn: ID File [IDFile]; ID File Field [IDFileField]; Mã user [MaUser]; Ngày thêm [NgayThemC]
### FIELDVERSION – Danh sách phiên bản field
- Lưới 1 «Danh sách field version»; tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Sửa bên phải
  - Cột: Mã file [MaFile]; Mã field [MaField]; Kiểu field view [SpecType0]{chọn}; Độ dài DB [LenDB]; Khóa chính [IsKhoa]; Khóa phụ [IsKhoaPhu]; Cho rỗng [AllowNull]
  - Cột ẩn: Ràng buộc xóa [DeleteRule]; Field phụ [FieldC]; Field chính [FieldP]; ID field version [IDFieldVersion]; ID Relation [IDRelation]; ID phiên bản [IDVersion]; Mã user [MaUser]; Ngày thêm [NgayThemC]; Loại relation [RelationType]; Bảng phụ [TableC]; Bảng chính [TableP]
### FILE – Danh mục file (AQ)
- Lưới 1 (bảng AQDmFile); tắt: Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã file [MaFile]; Tên file [TenFile]; Tên viết tắt [VtFile]; Quản lý file [Owned]
  - Cột ẩn: Alias file [Alias]; File mặc định [DfFile]; Điều kiện [DieuKien]; Ghi chú [GcFile]; Không quản lý [HuyFile]; ID Nhóm file [IDFile0]; Invalid key phụ [InvalidKeyPhu]; Allway? [IsAlway]; Danh mục? [IsDM]; File hệ thống? [IsFileHeThong]; Mã user [MaUser]; Ngày thêm [NgayThemC]; ID phân hệ chính [PHChinh]; Phân loại file [PlFile]; Tên tiếng anh [TenFileEg]; Thứ tự [TtFile]
  - Ô trên form sửa: #MaFile, #TenFile, #VtFile, #Owned, #Alias, #DieuKien, #GcFile, #IDFile0, #InvalidKeyPhu, #IsAlway, #IsDM, #IsFileHeThong, #PlFile, #TenFileEg
### FILECHANGE – Danh sách file thay đổi
- Lưới 1 (bảng AQDmFile); tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Sửa bên phải
  - Cột: Mã file [MaFile]; Mã file so sánh [MaFileSS]
  - Cột ẩn: Cột điểm động [*DIEM]; *Loại điểm [*LoaiDiem]; Thứ tự môn học đăng ký [*TTMHDK]; Tuần [*TUAN]; Giá trị mặc nhiên (DVPC) [AQDefaultValDVPC]; Giá trị mặc nhiên (Trường) [AQDefaultValTruong]; Điểm B1 [B1]; Điểm B2 [B2]; Điểm C1 [C1]; Điểm C2 [C2]; Số sv chưa nhập điểm [ChuaNhap]; Số sv đã nhập điểm [DaNhap]; Ràng buộc xóa SS [DeleteRuleSS]; Điểm chữ [DiemChu]; Điểm khác [DiemKhac]; Ghi chú [GhiChu]; Hoãn thi [HoanThi]; Khóa chính SS [IsKhoaSS]; Điểm K1 [K1]; Điểm K2 [K2]; Điểm K3 [K3]; Điểm K4 [K4]; Độ dài DB SS [LenDBSS]; Lý do thất bại [LyDoError]; Mã field so sánh [MaFieldSS]; Mã loại điểm [MaLoaiDiem]; Mặc định [MacDinh]; Điểm P1 [P1]; Điểm P2 [P2]; Điểm P3 [P3]; Điểm P4 [P4]; Điểm P5 [P5]; Điểm P6 [P6]; Điểm Q1 [Q1]; Điểm Q1 [Q2]; Điểm Q2 mới [Q3]; Điểm Q4 [Q4]; Điểm Q5 [Q5]; Điểm Q6 [Q6]; Số thứ tự trong Report [STTReport]; Số lần đăng ký [SoLDK]; Số lần đăng ký thất bại [SoLDKLoi]; Số lần đăng ký thành công [SoLDKTC]; Số môn học đăng ký [SoMHDK]; Số mẫu tin [SoMauTin]; Số mẫu tin hk cũ [SoRecordHKCu]; Số mẫu tin hk mới [SoRecordHKMoi]; Số sinh viên [SoSV]; Kiểu field ss [SpecType0SS]; Điểm thi [T1]; Điểm T2 [T2]; Điểm T3 [T3]; Điểm tổng kết học phần [TK]; Điểm tổng kết kiểm tra [TKK]; Điểm tổng kết thi [TKT]; Thứ tự tuần [TTTuan]; Tuần 1 [TUAN1]; Tuần 3 [TUAN3]; Bảng phụ SS [TableCSS]; Bảng chính SS [TablePSS]; Tên loại điểm [TenLoaiDiem]; Tên tuần [TenTuan]; Thông tin [ThongTin]; Tổ TH [ToTH]; Tổng cộng [TongCong]; Ràng buộc sửa SS [UpdateRuleSS]; Tên viết tắt [VTTuan]
### FKQDKDTNH – Kết quả đăng ký đào tạo ngắn hạn
- Lưới 1 «Danh sách sinh viên đăng ký môn học» (bảng FKQDKDTNH); tắt: Sửa, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Thứ tự [TTKQDKDTNH]; Mã môn học [MaMonDTNH]; Tên môn [TenMonDTNH]; Mã SV [MaSV]; Họ và tên [TenDayDu]; Phân loại sinh viên [LoaiDTDKDTNH]{chọn}; % học phí miễn giảm [MienGiamDTNH]; Thành tiền [ThanhTienVL]
  - Cột ẩn: Điện thoại 1 [DC_DT1LLSV]; Email 1 [DC_EML1LLSV]; Ghi chú 1 [GhiChu1]; Dân tộc [IDDT]; ID Đối tượng đăng ký đào tạo ngắn hạn [IDDTDKDTNH]{nút …}; Môn học trong khóa [IDMonKhoa]; Ngày sinh [NgaySinhC]; Nơi sinh [NoiSinh]; Phái [Phai]; Số CMND [SoCMND]
  - Ô trên form sửa: #TTKQDKDTNH, #TenDayDu, #LoaiDTDKDTNH, #MienGiamDTNH, #DC_DT1LLSV, #DC_EML1LLSV, #GhiChu1, #IDDT, #IDDTDKDTNH, #IDMonKhoa, #NgaySinhC, #NoiSinh, #Phai, #SoCMND
### FMONKHOA – Danh sách môn học theo khóa
- Lưới 1 «Danh sách môn học trong khóa học» (bảng FMonKhoa); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Thứ tự [TTKQDKDTNH](chỉ đọc); Mã môn học [MaMonDTNH](chỉ đọc); Tên môn [TenMonDTNH](chỉ đọc); Mã lớp [MaLopMonKhoa]; Số tiết môn học [SoTietMH]; Học phí [HocPhi]; Ngày khai giảng dự kiến [NgayKhaiGiangDK]{ngày}
  - Cột ẩn: Khóa học [IDKhoaHoc](chỉ đọc); Môn học [IDMonDTNH](chỉ đọc); Môn học trong khóa [IDMonKhoa](chỉ đọc)
### FMonkhoa_Thi – Nhập lịch dự thi môn học
- Lưới 1 «Nhập lịch dự thi môn học» (bảng FMonKhoa); tắt: Thêm, Sửa, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn [MaMonDTNH](chỉ đọc); Tên môn [TenMonDTNH](chỉ đọc); Ngày làm thủ tục [NgayGioThuTucThi]{ngày}; Giờ làm thủ tục [GhiChu1]; Phòng làm thủ tục [IDPHThuTucThi]; Ngày thi 1 [NgayGioThi1]{ngày}; Giờ thi 1 [GhiChu2]; Phòng thi 1 [IDPHThi1]; Ngày thi 2 [NgayGioThi2]{ngày}; Giờ thi 2 [GhiChu3]; Phái [Phai]; Phòng thi 2 [IDPHThi2]
  - Cột ẩn: Môn học [IDMonDTNH]; Môn học trong khóa [IDMonKhoa]
### FNhapDiemMHNhieuTP – Nhập điểm môn học nhiều thành phần
- Lưới 1 «Danh sách thí sinh thi môn học nhiều thành phần» (bảng FKQDKDTNH); tắt: Thêm, Sửa, Xóa, Xuất, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ và tên [TenDayDu](chỉ đọc); Ngày nhập điểm [NgayNhapDiem]{ngày}; Ghi chú 1 [GhiChu1]{số}; Ghi chú 2 [GhiChu2]{số}; Ghi chú 3 [GhiChu3]{số}; Ghi chú 4 [GhiChu4]{số}; Ghi chú 5 [GhiChu5]{số}
  - Cột ẩn: Điểm số [DiemSo]; IDKQDKDTNH [IDKQDKDTNH]; Điểm thành phần môn ĐTNH [IDKQThanhPhanMonDTNH]; Môn học [IDMonDTNH]; Sinh viên [IDSV]; Thành phần môn DTNH [IDThanhPhanMonDTNH]; Tên thành phần [TenThanhPhanMonDTNH]
### FPHKhoaHoc – Danh sách phòng trong khóa học
- Lưới 1 «Nhập phòng học trong khóa học» (bảng FPHKhoaHoc); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã phòng [MaPH]; Tên phòng [TenPH]; Tên cơ sở [TenCoSo]; Tên tính chất phòng [TenTCPhong]; Sức chứa [SucChuaPH]
  - Cột ẩn: Mã phòng học [IDPH]; IDPHKhoaHoc [IDPHKhoaHoc]
### FTKBMonDTNH – Nhập lịch khai giảng dự kiến
- Lưới 1 «Thời Khóa Biểu Khóa Học» (bảng FTKBMonDTNH); tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMonDTNH](chỉ đọc); Tên môn [TenMonDTNH](chỉ đọc); Tổng số tiết [SoTietMH](chỉ đọc); Ngày bắt đầu học [NgayBDHoc]{ngày}; Ngày kết thúc học [NgayKTHoc]{ngày}; Số tiết [SoTiet]{số}; Tiết BĐ [TietBD]{số}; Thứ hai [TKBThu2]; Thứ ba [TKBThu3]; Thứ tư [TKBThu4]; Thứ năm [TKBThu5]; Thứ sáu [TKBThu6]; Thứ bảy [TKBThu7]; Chủ nhật [TKBThu8]
  - Cột ẩn: IDTKBMonDTNH [IDTKBMonDTNH]; Thứ [Thu]
### FXetLaiKQThi – Xét lại kết quả thi
- Lưới 1 «Danh sách phúc khảo chưa xét KQ» (bảng FPhuckhao); tắt: Thêm, Xóa, Xuất, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Tên khóa học [TenKhoaHoc]; Họ và tên [TenDayDu]; Tên môn [TenMonDTNH]; Điểm số cũ [DiemSoCu]; Điểm chữ cũ [DiemChuCu]; Điểm số phúc khảo [DiemSoPhucKhao]; Điểm chữ phúc khảo [DiemChuPhucKhao]; Ngày xin phúc khảo [NgayXinPhucKhao]{ngày}; Ngày xét phúc khảo [NgayXetPhucKhao]{ngày}; Đạt [IsDatMonDTNHPhucKhao]
  - Cột ẩn: IDKQDKDTNH [IDKQDKDTNH]; ID phúc khảo [IDPhucKhao]; Đồng bộ kết quả [IsDongBoKQ]
### GanDotHocChoNhomTo – View sua si so to hoc
- Lưới 1 «Gán đợt học học cho nhóm tổ» (bảng KToHoc); tắt: Thêm, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm/tổ [NhomTo](chỉ đọc); Nhóm TC [NhomTC](chỉ đọc); Tổ TH [ToTH](chỉ đọc); Ngày bắt đầu [NgayBD]; Sĩ số đã đăng ký [SiSoDDK](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Mã PH [MaPhHK](chỉ đọc); Mã khoa quản lý bộ môn [MaKhoaBM](chỉ đọc); DSCBGD [DSCBGD](chỉ đọc); Tên đầy đủ [TenDayDuNV](chỉ đọc); SL trung bình nhóm [SiSoTKB]{số}; Sĩ số cho phép đk [SiSoCPDK]{số}; Mã đợt học [IDDOTHOC]
  - Cột ẩn: Đề án [DA](chỉ đọc); Luận án [LA](chỉ đọc); Lý thuyêt [LT](chỉ đọc); Sĩ số phòng [SiSoPH]{số}(chỉ đọc); Sức chứa [SucChuaPH](chỉ đọc); Thực hành [TH](chỉ đọc); Thực tập [TT](chỉ đọc); Tên khoa quản lý bộ môn [TenKhoaBM](chỉ đọc)
### GChotKLDXHK – Chốt và tính chi phí đi xa
- Lưới 1 «Danh sách dữ liệu đã chốt ở kế hoạch» (bảng GChotKLDXHK); tắt: Thêm, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm/tổ [NhomTo]; Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Tên trường liên kết [TenDP]; Số ngày giảng dạy [SoNgayGD]; Số cụm GD liên tiếp [SoCumGDLienTiep]; Số buổi GD ngày [SoBuoiDayNgay]; Số buổi GD tối [SoBuoiDayToi]; Danh sách ngày dạy [DSNgayDay]
### GCHUANDM – Chuẩn định mức
- Lưới 1 «Định nghĩa chuẩn định mức theo trình độ» (bảng GChuanDM); tắt: Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Ngạch [TenNgach]; Đơn vị [TenDV]; Học hàm [TenHocHam]; Học vị [TenBacNV]; Số giờ nghĩa vụ [sogiochuan]; Số điểm chuẩn [SoDiem]; Ngày hiệu lực [NgayHLDM]{ngày}
  - Cột ẩn: Trình độ [IDBacNV]; IDChuanDM [IDChuanDM]; Đơn vị [IDDV]; Học hàm [IDHocHam]; Ngạch [IDNgach]; Mã trình độ [MaBacNV]; Mã học hàm [MaHocHam]; Mã ngạch [MaNgach]; Thâm niên [ThamNien]
  - Ô trên form sửa: #sogiochuan, #SoDiem, #NgayHLDM, #IDBacNV, #IDDV, #IDHocHam, #IDNgach
### GCHUANDM_NCKH – Chuẩn định mức nghiên cứu khoa học
- Lưới 1 «Chuẩn định mức nghiên cứu khoa học» (bảng GChuanDM); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Thâm niên [ThamNien]{số}; Ngạch [TenNgach]; Tên học hàm [TenHocHam]; Tên trình độ [TenBacNV]; Số điểm chuẩn [SoDiem]; Qui đổi giờ chuẩn [SoQuiDoiGioChuanNCKH]{số}; Thâm niên từ [ThamNienTu]{số}; Thâm niên đến [ThamNienDen]{số}
  - Cột ẩn: Ghi chú [GCChuanDM]; Trình độ [IDBacNV]; IDChuanDM [IDChuanDM]; Học hàm [IDHocHam]; Ngạch [IDNgach]; Mã trình độ [MaBacNV]; Mã học hàm [MaHocHam]; Mã ngạch [MaNgach]; Ngày hiệu lực [NgayHLDM]{ngày}; Số giờ nghĩa vụ [sogiochuan]
  - Ô trên form sửa: #SoDiem, #SoQuiDoiGioChuanNCKH, #ThamNienTu, #ThamNienDen, #GCChuanDM, #IDBacNV, #IDHocHam, #IDNgach
### GPHANTRAMDM – Phần trăm hưởng định mức
- Lưới 1 «Định nghĩa phần trăm tính định mức theo chức vụ» (bảng GPhanTramDM); tắt: Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Tên chức vụ [TenChucVu]; % giảng dạy [PTSOGIO]; % nghiên cứu [PTSODIEM]; Ngày hiệu lực [NgayHLDM]{ngày}
  - Cột ẩn: Chức vụ [IDChucVu]; ID phần trăm định mức [IDPhanTramDM]; Mã chức vụ [MaChucVu]
  - Ô trên form sửa: #PTSOGIO, #PTSODIEM, #NgayHLDM, #IDChucVu
### GPHANTRAMDM_NCKH – Phần trăm hưởng định mức
- Lưới 1 «Định nghĩa phần trăm định mức thực hiện nghiên cứu khoa học theo chức vụ» (bảng GPhanTramDM); tắt: Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Tên chức vụ [TenChucVu]; % định mức cần thực hiện [PTSODIEM]
  - Cột ẩn: Chức vụ [IDChucVu]; ID phần trăm định mức [IDPhanTramDM]; Mã chức vụ [MaChucVu]; Ngày hiệu lực [NgayHLDM]{ngày}; % giảng dạy [PTSOGIO]
  - Ô trên form sửa: #PTSODIEM, #IDChucVu
### HADMINPH – Phân quyền quản trị phân hệ
- Lưới 1 (bảng HAdminPH); tắt: Thêm, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Hình chức năng [AvatarChucNang]; Tên tiếng anh [TenChucNangEg]; Hình user [AvatarUser]; Tên đầy đủ [HotenTK]
### HB_ViewDSDKHB – View nhap danh sach dang ky hoc bong
- Lưới 1 «Danh sách sinh viên đăng ký xét học bổng» (bảng MDKHB); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Loại HB [LoaiHB]{chọn}; Ghi chú [GhiChu]
  - Cột ẩn: Sinh viên [IDSV]
  - Ô trên form sửa: #NHHK, #HoLotSV, #TenSV, #LoaiHB, #GhiChu, #IDSV
### HB_ViewKhoiXETHB – View khoi xet hoc bong
- Lưới 1 «Danh sách khối xét học bổng» (bảng MKHHBHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; Mã đơn vị [MaDV]; Tên đơn vị [TenDV]
### HB_ViewNhapDSHBKhac – View nhap danh sach hoc hong tuyen sinh
- Lưới 1 «Danh sách học bổng khác» (bảng MMGHB); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Số tiền HB [SoTienHB]; Ghi chú [GhiChu]
  - Cột ẩn: Sinh viên [IDSV]
  - Ô trên form sửa: #NHHK, #HoLotSV, #TenSV, #SoTienHB, #GhiChu, #IDSV
### HB_ViewNhapDSHBTS – View nhap danh sach hoc hong tuyen sinh
- Lưới 1 «Danh sách học bổng tuyển sinh» (bảng MHBTS); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Loại HB [LoaiHBTS]{chọn}; % MG [PTramMG]; Số TC MG [SoTCMG]; Số tiền MG [STienHBMG]
  - Cột ẩn: Ghi chú [GhiChuHBTS]; Sinh viên [IDSV]
  - Ô trên form sửa: #NHHK, #HoLotSV, #TenSV, #LoaiHBTS, #PTramMG, #SoTCMG, #STienHBMG, #GhiChuHBTS, #IDSV
### HB_ViewNhapDSNhanHB – View nhap danh sach nhan hoc bong
- Lưới 1 «Danh sách sinh viên nộp voucher» (bảng MNHANHB); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Loại HB [LoaiHB]{chọn}; % MG [PTramMG]; Số tiền HB [SoTienHB]; Số voucher [SoVouCher]; Ngày nộp [NgayNopHB]{ngày}; NHHK hoãn [NHHKHoan]; Khóa học bổng? [IsLockHB]
  - Cột ẩn: Sinh viên [IDSV]
  - Ô trên form sửa: #HoLotSV, #TenSV, #LoaiHB, #PTramMG, #SoTienHB, #SoVouCher, #NgayNopHB, #NHHKHoan, #IsLockHB, #IDSV
### HB_ViewNhapDSNhanHB_Imp – View nhap danh sach nhan hoc bong
- Lưới 1 (bảng MNHANHB); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Loại HB [LoaiHB]{chọn}; % MG [PTramMG]; Số tiền HB [SoTienHB]; Số voucher [SoVouCher]; Ngày nộp [NgayNopHB]{ngày}; NHHK hoãn [NHHKHoan]
  - Cột ẩn: Sinh viên [IDSV]
  - Ô trên form sửa: #HoLotSV, #TenSV, #LoaiHB, #PTramMG, #SoTienHB, #SoVouCher, #NgayNopHB, #NHHKHoan, #IDSV
### HB_ViewNhapDuyTriHB – View nhap duy tri hoc bong
- Lưới 1 «Danh sách học bổng học kỳ trước ( Cần nhập duy trì)» (bảng MDSHB); tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Phái [Phai](chỉ đọc); Loại HB [LoaiHB]{chọn}(chỉ đọc); % MG [PTramMG](chỉ đọc); Số TC MG [SoTCMG](chỉ đọc); Số TC MGHK [SoTCMGHK](chỉ đọc); Số tiền HB [SoTienHB](chỉ đọc); Có duy trì [IsDuyTriHB]
### HB_ViewNhapHoanHB – View nhap sv hoan nhan hoc bong
- Lưới 1 «Danh sách học bổng học kỳ( Cần nhập hoãn nhận)» (bảng MDSHB); tắt: Thêm, Xóa, Nạp lại, Đổi mã, Gộp mã
  - Cột: Niên học học kỳ [NHHK](chỉ đọc); Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Phái [Phai](chỉ đọc); Loại HB [LoaiHB]{chọn}(chỉ đọc); ĐTB HB [DiemTBHB](chỉ đọc); % MG [PTramMG](chỉ đọc); Số TC MG [SoTCMG](chỉ đọc); Số TC MGHK [SoTCMGHK](chỉ đọc); Số tiền HB [SoTienHB](chỉ đọc); Có hoãn HB [IsHoanHB]
### HB_ViewThongSoHB – View nhap thong so hoc bong theo kh
- Lưới 1 «Danh sách khối học bổng» (bảng MKHHBHK); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; Mã đơn vị [MaDV]; Loại xét [LoaiXetHB]{chọn}; Số tín chỉ DL [SoTCDL]; Số tín chỉ PRES [SoTCPRL]; ĐTB dean list [DTBDL]; ĐTB president list [DTBPRL]
  - Cột ẩn: DTBTKH [DTBTKH]; ĐTB trúng tuyển [DTBTT]; Mã khối [IDKhoi]; Nguồn điểm TK [NguonTK]{chọn}; Nguồn điểm TS [NguonTS]{chọn}; Tên đơn vị [TenDV]
  - Ô trên form sửa: #TenKhoi, #LoaiXetHB, #SoTCDL, #SoTCPRL, #DTBDL, #DTBPRL, #IDKhoi
### HB_ViewXemSuaHocBong – View nhap danh sach dang ky hoc bong
- Lưới 1 «Danh sách sinh viên nhận học bổng» (bảng MDSHB); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Loại HB [LoaiHB]{chọn}; % MG [PTramMG]; Tên [TenSV]; Số TC MG [SoTCMG]; Số TC MGHK [SoTCMGHK]; ĐTB HB [DiemTBHB]; Số tiền HB [SoTienHB]; Đạt học bổng [IsHB]; Lý do [LoaiLyDoHB]{chọn}
  - Cột ẩn: Ghi chú [GcDSHB]; Sinh viên [IDSV]; Số TC đăng ký [SoTCDK]; Số tín chỉ xét học bổng [SoTCXetHB]; Số voucher [SoVouCher]
  - Ô trên form sửa: #HoLotSV, #LoaiHB, #PTramMG, #TenSV, #SoTCMG, #SoTCMGHK, #DiemTBHB, #SoTienHB, #IsHB, #LoaiLyDoHB, #GcDSHB, #IDSV, #SoVouCher
### HB_ViewXemSuaHocBong_Imp – View nhap danh sach dang ky hoc bong
- Lưới 1 (bảng MDSHB); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Loại HB [LoaiHB]{chọn}; % MG [PTramMG]; Số TC MG [SoTCMG]; Số TC MGHK [SoTCMGHK]; ĐTB HB [DiemTBHB]; Số tiền HB [SoTienHB]; Đạt học bổng [IsHB]; Lý do [LoaiLyDoHB]{chọn}
  - Cột ẩn: Sinh viên [IDSV]
  - Ô trên form sửa: #HoLotSV, #TenSV, #LoaiHB, #PTramMG, #SoTCMG, #SoTCMGHK, #DiemTBHB, #SoTienHB, #IsHB, #LoaiLyDoHB, #IDSV
### HDMBODEM – Định nghĩa bộ đếm
- Lưới 1 «Danh sách bộ đếm» (bảng HDmBoDem); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bộ đếm [MaBoDem]; Tên bộ đếm [TenBoDem]; Tên viết tắt [VtBoDem]; Loại đối tượng [LoaiDoiTuong]{chọn}
  - Cột ẩn: Chiều dài [ChieuDai]{số}; Có SD số 0 [CoFillZero]; ĐT sử dụng [DTSuDung]{chọn}; Ghi chú [GcBoDem]; HK sử dụng [HKSuDung]{chọn}; Ký tự cuối [KyTuCuoi]; Ký tự đầu [KyTuDau]; Có lấy lại số khuyết [LayLaiSoKhuyet]
  - Ô trên form sửa: #MaBoDem, #TenBoDem, #VtBoDem, #LoaiDoiTuong, #ChieuDai, #CoFillZero, #DTSuDung, #GcBoDem, #HKSuDung, #KyTuCuoi, #KyTuDau, #LayLaiSoKhuyet
### HDMCHUKY – Danh mục chữ ký
- Lưới 1 «Danh mục người ký tên» (bảng HDmChuky); tắt: Sửa trên lưới
  - Cột: Mã chữ ký [MaChuKy]; Tên chữ ký [TenChuKy]; Chức vụ 1 [Chucvu1]; Người ký [NguoiKy]
  - Cột ẩn: Hình chữ ký số [ChuKySo]; Tên tiếng anh [Chucvu1Eg]; Chức vụ 2 [Chucvu2]; Tên tiếng anh [Chucvu2Eg]; Chức vụ 3 [Chucvu3]; Tên tiếng anh [Chucvu3Eg]; Danh xưng [DanhXung]; Ghi chú [GCChuKy]; Không quản lý [HuyChuKy]; Trình độ [IDBacNV]; Chức vụ [IDChucVu]; Học hàm [IDHocHam]; Mã viên chức [IDNV]; Nơi ký [NoiKy]; Tên tiếng anh [TenChuKyEg]; Tên viết tắt [VtChuKy]
  - Ô trên form sửa: #MaChuKy, #TenChuKy, #Chucvu1, #ChuKySo, #Chucvu1Eg, #Chucvu2, #Chucvu2Eg, #Chucvu3, #Chucvu3Eg, #DanhXung, #GCChuKy, #IDChucVu, #TenChuKyEg, #VtChuKy
### HDMNHCHUKY – Danh mục nhóm chữ ký
- Lưới 1 «Danh mục bộ chữ ký» (bảng HDmNhChuKy); tắt: Sửa trên lưới
  - Cột: Mã nhóm chữ ký [MaNhChuky]; Tên nhóm chữ ký [TenNhChuky]; Viết tắt nhóm chữ ký [VtNhChuKy]; Ghi chú nhóm chữ ký [GCNhChuKy]; Bộ chữ ký [BOCHUKY]
  - Cột ẩn: Nh chữ ký mặc định [DfNhChuKy]; Không quản lý [HuyNhChuKy]; Tên tiếng anh [TenNhChuKyEg]
  - Ô trên form sửa: #MaNhChuky, #TenNhChuky, #VtNhChuKy, #GCNhChuKy, #BOCHUKY, #DfNhChuKy, #HuyNhChuKy, #TenNhChuKyEg
  - Nút btnUpdate: "su" (F5)
  - Nút SAve: "" (F5)
  - Nút barBtnHuy: "huy" (F4)
  - Nút btnAdd: "them" (f1)
  - Nút btnThem: "Sửa DS bộ chữ ký" (F2)
### HDMSUBREPORT – Danh muc báo biểu con (subreport)
- Lưới 1 «Danh sách phiên bản mẫu in» (bảng HDMSubReport); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã phiên bản [SubCode]; Tên phiên bản [TenSubReport]; Mã user [MaUser]; Ngày thêm [NgayThem]; Tên viết tắt [VtSubReport]; Gc phiên bản [GcSubReport]; File report [DocReport]; Hiển thị sub report [HienThiInBGD]{chọn}; NHHKBDSD [NHHKBDSD]; NHHK ngưng sử dụng [NHHKNgungSD]; Cố định số dòng [FixSoDong]; Có in ở web [IsDfWeb]
  - Cột ẩn: Dạng in [DangIn]{chọn}; Sub report mặc định [DfSubReport]; Chiều cao report [HeightRP]{số}; Hình thức bgd [HinhThucBGD]{chọn}; In địa điểm ký tên [InDiaDiemKyTen]; In mã user [InMaUser]; In môn TN [InMonTN]{chọn}; In ngày trong ngày ký [InNgayTrgNgayKy]; In SV không thi [InSVKhgThi]{chọn}; In tổng số trang [InTongSoTrang]; In theo phách [IsPhachBGD]; Cuối trang [KTCuoiTrang]{số}; Đầu trang [KTDauTrang]{số}; Lề trái [KTLeTrai]{số}; Khổ giấy [KhoGiayIn]{chọn}; Làm tròn [LamTronBGD]{chọn}; Loại bgd [LoaiBgDiem]{chọn}; Mã kỳ thi BGD [MaKyThiBGD]; Chi tiết padding [PaddingDetails]; Nhóm đếm lại trang [PageCountGroup]; Scan ngang [ScanNgangBGD]; Chỉnh đếm trang [SetPageCount]; Số dòng sang trang [SoDongSangGroup]{số}; Số sv/trang [SoSVTrang]{số}; TT sub report [TTSubReport]; Tên tiếng anh [TenSubReportEg]; Độ rộng report [WidthRP]{số}; Ẩn đối với user [isHideUser]
  - Ô trên form sửa: #SubCode, #TenSubReport, #VtSubReport, #GcSubReport, #DocReport, #HienThiInBGD, #NHHKBDSD, #NHHKNgungSD, #FixSoDong, #IsDfWeb, #DangIn, #DfSubReport, #HeightRP, #HinhThucBGD, #InDiaDiemKyTen, #InMaUser, #InMonTN, #InNgayTrgNgayKy, #InSVKhgThi, #InTongSoTrang, #IsPhachBGD, #KTCuoiTrang, #KTDauTrang, #KTLeTrai, #KhoGiayIn, #LamTronBGD, #LoaiBgDiem, #MaKyThiBGD, #PaddingDetails, #ScanNgangBGD, #SoDongSangGroup, #SoSVTrang, #TTSubReport, #WidthRP, #isHideUser
  - Nút btnSave: "Save" (F10)
  - Nút btnDelete: "Xóa" (D)
  - Nút btnAdd: "Thêm" (F5)
  - Nút btnQuit: "Đóng" (Q)
  - Nút btnUpdate: "Sửa" (F11)
### HDmTempMail – Danh mục template
- Lưới 1 «Danh sách các bộ nội dung mẫu gửi email cho sinh viên» (bảng HDmTempMail); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã Template Mail [MaTempMail]; Tên Template Mail [TenTempMail]; Loại template mail [LoaiTempMail]{chọn}; Nội dung [NoiDungTempMail]
  - Ô trên form sửa: #MaTempMail, #TenTempMail, #LoaiTempMail, #NoiDungTempMail
### HDSNHCHUKY – Danh sách chữ ký/nhóm chữ ký
- Lưới 1 «Danh sách  bộ chữ ký» (bảng HNhChuKyCT); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã chữ ký [MaChuKy]; Mã nhóm chữ ký [MaNhChuky]; Tên chữ ký [TenChuKy]; Chức vụ 1 [Chucvu1]; Tên nhóm chữ ký [TenNhChuky]; Người ký [NguoiKy]; Tên viết tắt [VtNhChuKy]; Ghi chú [GCNhChuKy]
  - Cột ẩn: Cho phép sửa [Chophepsua]; Hình chữ ký số [ChuKySo]; Chức vụ 2 [Chucvu2]; Chức vụ 3 [Chucvu3]; Chữ ký mặc định [DfChuKy]; Nh chữ ký mặc định [DfNhChuKy]; Ghi chú [GCChuKy]; Không quản lý [HuyChuKy]; Không quản lý [HuyNhChuKy]; Người ký [IDChuKy]; Nhóm chữ ký [IDNhChuKy]; ID ds nhóm chữ ký [IDNhChuKyCT]; Mã user [MaUser]; Ngày thêm [NgayThem]; Thứ tự [TTChuKy]; Thứ tự [TTNhChuKy]; Tên tiếng anh [TenChuKyEg]; Tên tiếng anh [TenNhChuKyEg]; Cấp độ user [UserLevel]; Tên viết tắt [VtChuKy]
  - Ô trên form sửa: #IDChuKy, #IDNhChuKy
### HIMPORTTPL – Danh sách mẫu import
- Lưới 1 «Chi tiết mẫu import» (bảng HImportDefine); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Cột Import [FieldAlias](chỉ đọc); Diễn giải [TenFieldImport](chỉ đọc)
  - Cột ẩn: Chọn [CheckChon]; ID import define [IDImportDefine]; ID Import template [IDImportTpl]; Thứ tự [ThuTuImp]
  - Nút btnSetting: "Chọn File" (F)
- Lưới 2 «Danh sách mẫu import» (bảng HImportTpl); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Tên mẫu import [TenImportTpl]; Mã user [MaUser]; Phiên bản import [VersionImp]
  - Cột ẩn: ID Import template [IDImportTpl]; ID View [IDView]; Ngày thêm [NgayThem]
### HMESS – Thông Tin Ngôn Ngữ
- Lưới 1 «Chỉnh định từ khóa sử dụng» (bảng HMess); tắt: Thêm, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa bên phải
  - Cột: Nội dung AQ [TenMessAQ](chỉ đọc); Tên thông báo [TenMess]
  - Ô trên form sửa: #TenMess
  - Nút btnSave: "Luu" (F5)
  - Nút barBtnHuy: "Huy" (F2)
### HPQUSERSETTING – Danh sách ủy quyền user chỉnh đinh
- Lưới 1 «Danh sách ủy quyền user chỉnh định biến» (bảng HPQUserSetting); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã Setting [MaSetting]; Tên phân hệ [TenPhanHe]; Tên Setting [TenSetting]; Tên đầy đủ [HotenTK]
  - Cột ẩn: Mã setting [IDSetting]; ID user [IDUser]
  - Ô trên form sửa: #IDSetting, #IDUser
### HRIGHT – Phân quyền
- Lưới 1 (bảng AQDMChucNang); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã chức năng [MaChucNang]; Tên chức năng [VtChucNang]; Ghi chú [GhiChu]
  - Cột ẩn: ID chức năng cha [IDChucNangParent]
  - Ô trên form sửa: #MaChucNang, #VtChucNang, #GhiChu
### HRIGHTREAD – Danh sach phan quyen theo user
- Lưới 1 (bảng HUser); tắt: Thêm, Sửa, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Sửa bên phải
  - Cột: Tên đầy đủ [HotenTK]; Nhóm tài khoản [NhomTK]; Hình user [AvatarUser]
  - Cột ẩn: Ghi chú [GhiChu]
  - Ô trên form sửa: #GhiChu
### HSERVERLOG – Log server
- Lưới 1 (bảng HServerLog); tắt: Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Thông báo lỗi [ErrMessage]
  - Cột ẩn: Chi tiết [Chitiet]; ID Server Log [IDServerLog]; Ngày thêm [NgayThem]
  - Ô trên form sửa: #ErrMessage, #Chitiet
### HSETMAIL – Cấu hình thông số gửi mail phân hệ
- Lưới 1 «Danh sách cấu hình gửi mail» (bảng HSETMAIL); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Phân hệ [LoaiPH]{chọn}; Host mail server [HostMailSV]; Outgoing server port [OutgoingSVPort]; SSL [SSLSV]; Mail username [MailUSer]; Incoming server port [IncomingSVport]
  - Cột ẩn: Mail password [MailPass]
  - Ô trên form sửa: #LoaiPH, #HostMailSV, #OutgoingSVPort, #SSLSV, #MailUSer, #IncomingSVport, #MailPass
### HTTKHACHHANG – Giao diện thông tin khách hàng
- Lưới 1 (bảng HTTKhachHang); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã trường tổ chức thi [MaTruong]; Tên trường [TenTruong]; Ghi chú [GCTruong]; Tên viết tắt [VTTruong]; Đơn vị chủ quản [DVCQ]; Địa chỉ [DiaChi]; Email trường [Email]; Fax trường [Fax]; NHHK giới hạn [NHHKGioiHan]{số}; Số lượng sv [SoLuongSV]{số}; Hình logo trường [LogoTruong]; Banner trường [BannerTruong]; Ngày sử dụng [NgaySudung]{ngày}; NHHK sử dụng [NHHKSuDung]{số}; Phiên bản [PVersion]; Phiên bản [DVersion]; Phiển bản cũ [OVersion]; Tel trường [Tel1]; Tel trường (2) [Tel2]; Website [WebSite]; Số tài khoản [SoTK]; Ngân hàng [NganHang]; Tên cán bộ ban giám [TenHT]; Chức vụ CB BGH [Cvht]; Phòng ban cb BGH [PhongHT]; Email CB BGH [Email1HT]; Email cb BGH (2 [Email2HT]; Tel CB BGH [Tel1HT]; Tel CB BGH (2) [Tel2HT]; Tên cán bộ phòng tà [TenPTC]; Chức vụ CB PTC [CVPTC]; Phòng ban cb PTC [PhongPTC]; Email CB PTC [Email1PTC]; Email cb PTC (2 [Email2PTC]; Tên admin [TenAd]; Chức vụ admin [CVAD]; Phòng ban admin [PhongAd]; Email admin [Email1Ad]; Email admin (2) [Email2Ad]; Tel admin [Tel1Ad]; Tel admin (2) [Tel2Ad]; Mở chinh định [MoChinhDinh]; Quyền chỉnh định [QuyenChinhDinh]{chọn}; Phiên bản [PhienBan]{chọn}
  - Cột ẩn: Banner EduWeb [BannerWeb]; Favicon Eduweb [LogoWeb]
  - Ô trên form sửa: #MaTruong, #TenTruong, #GCTruong, #VTTruong, #DVCQ, #DiaChi, #Email, #Fax, #LogoTruong, #BannerTruong, #Tel1, #Tel2, #WebSite, #SoTK, #NganHang, #TenHT, #Cvht, #PhongHT, #Email1HT, #Email2HT, #Tel1HT, #TenPTC, #CVPTC, #PhongPTC, #Email1PTC, #Email2PTC, #TenAd, #CVAD, #PhongAd, #Email1Ad, #Email2Ad, #Tel1Ad, #BannerWeb, #LogoWeb
  - Nút btnSave: "Lưu" (F5)
### HTTLOGIN – Nhật ký đăng nhập
- Lưới 1 «Danh sách nhật ký đăng nhập»; tắt: Thêm, Sửa, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: UserName [UserName]; Mã View [MAVIEW1]; Tên trường thông tin [TenView1]; Ngày thêm [NgayThem]; Ngày đăng nhập [NgayDN]{ngày}; Giờ đăng nhập [GioDN]; Địa chỉ logic [LAddress]; Số lượng đăng nhập [SoLuongDN]; Số lượng dữ liệu [SoLuongDuLieu]
### HUSER – Danh mục user và nhóm
- Lưới 1 «Danh sách người dùng hệ thống» (bảng HUser); tắt: Nạp lại, Gộp mã, Sửa trên lưới
  - Cột: UserName [UserName]; Tên đầy đủ [HotenTK](chỉ đọc); Nhóm tài khoản [NhomTK](chỉ đọc); Khóa tài khoản [TrangThai]{chọn}; Mã đơn vị phân cấp [MaDVPC]; Phân cấp user [PhanCapUser]{chọn}; Đa đơn vị phân cấp [IsUseAllDVPC]
  - Cột ẩn: Hình user [AvatarUser](chỉ đọc); Email [EmailUser]; Ghi chú [GCTK](chỉ đọc); Ghi chú [GhiChu](chỉ đọc); Ghi chú dùng bên detailright [GhiChuView1]; Đơn vị phân cấp [IDDVPC]; Mã khoa [IDPCUser]; Admin phân cấp [IsAdminDVPC]; Password [Password](chỉ đọc); Nhập lại mật khẩu [RePassword](chỉ đọc)
  - Ô trên form sửa: #UserName, #HotenTK, #TrangThai, #PhanCapUser, #IsUseAllDVPC, #AvatarUser, #EmailUser, #GCTK, #GhiChu, #GhiChuView1, #IDDVPC, #IDPCUser, #IsAdminDVPC, #Password, #RePassword
### HUSERMEMBER – Danh sách thành viên
- Lưới 1 «Danh sách» (bảng HUserGroup); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Nhóm [IsAccGroup]; UserName [UserName]; Tên đầy đủ [HotenTK]; Hình user [AvatarUser]
  - Cột ẩn: Ghi chú [GCTK]
### HUSERPQ – Danh sách thành viên
- Lưới 1 «Danh sách người dùng hệ thống» (bảng HUserGroup); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: UserName [UserName]; Nhóm [IsAccGroup]; Tên đầy đủ [HotenTK]; Nhóm tài khoản [NhomTK]
  - Cột ẩn: Hình user [AvatarUser]; Ghi chú [GCTK]
  - Ô trên form sửa: #GCTK
### HUSERRIGHT – Danh sách user
- Lưới 1 «Danh sách tài khoản» (bảng HUser); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Nhóm tài khoản [NhomTK](chỉ đọc); Tên đầy đủ [HotenTK](chỉ đọc); Quyền [PhanQuyen](chỉ đọc); Thừa kế [ThuaKeTree](chỉ đọc)
  - Cột ẩn: Hình user [AvatarUser](chỉ đọc); Quyền [Quyen]{chọn}(chỉ đọc)
### HVALUESETTING – Giao diện xem dữ liệu chỉnh định
- Lưới 1 (bảng AQDMSetting); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã Setting [MaSetting]; Nhóm chức năng [NhomChucNang]; Tên Setting [TenSetting]
  - Cột ẩn: Admin sửa [AdminEdit]; Hình phân hệ [AvatarPhanHe]; Có phân cấp? [CoPhanCap]; Kiểu dữ liệu [DataType]; Phân hệ mặc định [DfPhanHe]; Setting mặc định [DfSetting]; Ghi chú [GcPhanHe]; Ghi chú [GcSetting]; Không quản lý [HuyPhanHe]; Không quản lý [HuySetting]; ID phân cấp min [IDPhanCapBegin]; ID phân cấp max [IDPhanCapEnd]; Mã phân hệ [IDPhanHe]; Mã setting [IDSetting]; Index 1 [Index1]; Index 2 [Index2]; Bien HK? [IsBienHK]; Bien HK con? [IsBienHKCon]; Bien User? [IsBienUser]; Bit? [IsBit]; Hằng số? [IsConst]; Tạo cờ? [IsTaoCo]; Key source [KeySource]; Mã phân hệ [MaPhanHe]; Biến mapping [MappingArray]; Tên phân hệ [TenPhanHe]; Tên tiếng anh [TenPhanHeEg]; Tên tiếng anh [TenSettingEg]; Thứ tự [TtPhanhe]; Thứ tự [TtSetting]; Tên viết tắt [VtPhanHe]; Tên viết tắt [VtPhanHe2]; Tên viết tắt [VtSetting]
### IMP_DKMH_FILESV – Import đăng ký môn học theo file sinh viên
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### IMP_DKMH_SV_VA_MH – Import đăng ký môn học file sinh viên và môn học
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### IMP_DMDB – Import địa bàn theo file
- Lưới 1 (bảng NDMDB); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã địa bàn [MaDB]; Mã địa bàn trực thuộc [MADBTT]; ID địa bàn cha [IDDBC]; Tên địa bàn [TenDB]; Tên tiếng anh [TenDBEg]; Loại hình [LoaiHinh]; Tên viết tắt [VTDB]; Địa bàn mặc định [DFDB]; Ghi chú [GCDB]; Mã địa bàn 2 [MaDB2]
### IMP_DMMH – View import KDMMH
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Mã đơn vị [MaDV]; Tên đơn vị [TenDV]; Số tiết môn học [SoTietMH]; Lý thuyêt [LT]; Thực hành [TH]; Bài tập [BT]; Thực hành khác [THK]; Bài tập lớn [BTL]; Đề án [DA]; Luận án [LA]; Tốt nghiệp [TN]; Thực tập [TT]; TTLT [TTLT]; TTTH [TTTH]; LMS [LMS]; Lâm sàng [LS]; Môn tốt nghiệp? [IsMHTN]; Không tính ĐTB [KhgTinhDTB]; Sỉ số max SV LT [SiSoMaxLT]; Sỉ số mã SV TH [SiSoMaxTH]; Không xét trùng lịch thi khi đăng ký môn học [IsKgXetTrungLThiKhiDKMH]; Mức đơn giá LT [MucDGLT]; Mức đơn giá TH [MucDGTH]; Cho học vượt [IsMHChoVuot]; Số TC EU [SoTinChiEU]; Tên tiếng anh [TenMHEg]; NHHK bắt đầu [NHHKBD]; Tỷ lệ cấm thi TH [PTVangTHCamThi]; Môn IELTS [MHTOEIC]; Ghi chú [GcMH]; Môn kiểm tra [IsMonKT]; Phân loại thực hành [PhanLoaiTH]; GC môn học 1 [GCMH2]; Khối kiến thức [KhoiKTGD]; Tên MH tiếng pháp [TenMHFr]; Số TC học phí [SoTinChiHP]; Không xếp thời khóa biểu [IsKhgXepTKB]; Tính chất môn học [TinhChatMH]; Số tiết/tuần [SoTietTuan]; Xếp lịch thi SS [XepLichThiSS]; Không tính vào số tín chỉ tối đa khi ĐKMH [IsKghXetTCDK]; Tỷ lệ cấm thi LT [PTVangLTCamThi]; Không xếp lịch thi [IsKgXepLThi]; Sĩ số min [SiSoMin]; Không xếp phòng TKB [IsKgXepPh]; Số sv tối đa [SiSoMax]; Số CBGD tối đa [SoCBMax]; Tên viết tắt [VtMH]; Kiểm tra [KT]; Số tiết 2 [SoTiet2]; Tự học [TUH]
### IMP_DTSVVC – Import đề tài sinh viên viên chức
- Lưới 1 (bảng ODeTaiNCKH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đề tài [MaDeTaiNCKH]; Mã SV [MaSV]; Mã viên chức [MaNV]; Tên đề tài [TenDeTaiNCKH]; Ngày bắt đầu [NgayBDDeTai]; Niên học học kỳ [NHHK]; Tình trạng đề tài [TinhTrangDeTai]; Đối tượng thực hiện đề tài [DoiTuongThucHienDeTai]
### IMP_GNHCBGD – Import
- Lưới 1 «Import» (bảng GNHCBGD); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Mã viên chức [MaNV]; Nhóm học [NhomHoc]; Tổ TH [ToTH]; Tháng tính khối lượng [ThangKL]; Năm tính khối lượng [NamKL]; Tống tiết TKB [TONGTIETTKB]; Loại tiết lấy tính KL [LoaiThoiGianTinhKL]; Sỉ số TKB [SoSVTKB]; Số SV đăng ký [SOSVDK]; Không HSLD [IsKgHSLopDong]; Mã cơ sở [MaCoSo]; Mã hệ đào tạo [MaHe]; ST ngoài giờ tối [TietNgGio1]; ST ngoài giờ thứ 7 [TietNgGio2]; ST ngoài giờ CN [TietNgGio3]; ST ngoài giờ tối thứ 7 [TietNgGio4]; ST ngoài giờ tối CN [TietNgGio5]; ST ngoài giờ 6,7 [TietNgGio6]; ST ngoài giờ lễ [TietNgGioLe]; Số giờ nghĩa vụ [sogiochuan]
### IMP_KLHieuChinh – Import
- Lưới 1 (bảng GKLHC); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Nhóm/tổ [NhomTo]; Tổ TH [ToTH]; Mã viên chức [MaNV]; Mã CBGD HC [MaCBGDHC]; Tháng tính khối lượng [ThangKL]; Năm tính khối lượng [NamKL]; Mã loại hình [MaLH]; SL sinh viên hiệu chỉnh [SOLGSVHC]; Số lượng TG hiệu chỉnh [SOLGTGHC]; Số tiết tối HC [SLNGHC1]; Số tiết thứ 7 HC [SLNGHC2]; Số tiết chủ nhật HC [SLNGHC3]; Số tiết tối thứ 7 HC [SLNGHC4]; Số tiết tối CN HC [SLNGHC5]; Số giờ nghĩa vụ [sogiochuan]; Hệ số ngoài giờ tối [HSNGHC1]; Hệ số ngoài giờ thứ 7 [HSNGHC2]; Hệ số ngoài giờ chủ nhật [HSNGHC3]; Hệ số ngoài giờ tiết thứ 7 [HSNGHC4]; Hệ số ngoài giờ tiết chủ nhật [HSNGHC5]; Đơn giá hiệu chỉnh [DONGIAKLHC]; Số lượng khối lượng HC [SOLGKLHC]; Ghi chú hiệu chỉnh [GCKLHC]
### IMP_LDMLOAITGCT – Import
- Lưới 1 (bảng LDMLoaiTGCT); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Giờ bắt đầu [GioBD]; Số phút [SoPhut]; Thứ tự thời gian [ThuTuTG]; Mã loại thời gian [MaLoaiTG]
### IMP_NDMNV – Import danh mục nhân viên
- Lưới 1 (bảng NDMNV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Ngày sinh [NgSinhNVCNV]; Trạng thái [HienDienNV]; Bí danh [BiDanh]; Tình trạng hôn nhân [TTHonNhan]; Phái [PhaiNV]; Nơi sinh [NoiSinhNV]; Quê quán [QueQuanNV]; Tạm trú [TAMTRU]; Hộ khẩu [HoKhauNV]; Địa chỉ liên lạc [DC_DCLLNV]; Mã diện chính sách [MaDCS]; Mã dân tộc [MaDT]; Mã tôn giáo [MaTG]; Email [DC_Eml1LLNV]; Email 2 [DC_Eml2LLNV]; Số điện thoại [DC_DT1LLNV]; Số điện thoại (2) [DC_DT2LLNV]; Số tài khoản [SoTK]; Chi nhánh [CHINHANHNH]; Số tài khoản 2 [SoTK2]; Chi nhánh [CHINHANHNH2]; Sở trường [SoTruong]; Cơ quan công tác [CoQuanCongTac]; Lịch sử bản thân (từ 12 tuổi đến nay) [DDLS1]; Lịch sử bản thân 2 [DDLS2]; Lịch sử bản thân 3 [DDLS3]; Phát hiện địa phương [PhatHienDP]; Ý kiến công an khu vực [YKienCS]; Mã đơn vị [MaDV]; Ngày tham gia công tác [NgayCongTac]; Ngày về trường [NgayVeTruong]; Năm vào ngành [NamVaoNganh]; Trình độ học vấn [TDHV]; Biên chế [ISBIENCHE]; PC ngành (%) [MucPCNganh]; Ngày vào BC [NgayBienChe]; Năm vào đoàn [NamDoan]; Số thẻ đoàn [SoDoan]; Nơi kết nạp đoàn [NoiDoan]; Ngày vào đảng dự bị [NamDang]; Số thẻ đảng [SoDang]; Nơi kết nạp [NoiDang]; Số CNCT Đảng [GCNDang]; Ngày CNCT Đảng [NgayGCNDang]; Ngày chính thức [NamDangCT]; Ngày tham gia TCCT-XH [NgayTGTCCTXH]; Ngày nhập ngũ [NgayNhapNgu]; Ngày xuất ngũ [NgayXuatNgu]; Quân hàm [QuanHam]; Thương binh [ThuongBinh]; Loại đối tượng CBGD [loaidtcbgd]; Số CMND [SoCMNDNV]; Ngày cấp [NgayCapCMNDNV]; Số passport [Passport]; Ngày cấp [NgayCapPassport]; Nơi cấp [NoiCapPassport]; Ngày hết hạn Passport [NgayHHPassport]; Số sổ LĐ [SoSLD]; Ngày cấp [NgCapSLD]; Nơi cấp SLĐ [NoiCapSLD]; Ngày hết hạn SLĐ [NgayHHSLD]; Số thẻ tạm trú [SoTamTru]; Ngày cấp thẻ tạm trú [NgCapTamTru]; Nơi cấp thẻ tạm trú [NoiCapTamTru]; Ngày hết hạn thẻ tạm trú [NgayHHTamTru]; Số lý lịch tư pháp [SoLLTP]; Ngày cấp [NgCapLLTP]; Nơi cấp [NoiCapLLTP]; Số thuế TNCN [SoTNCN]; Ngày cấp [NgayCapTNCN]; Nơi cấp [NoiCapTNCN]; Số phụ thuộc [SoNguoiPT]; Số khám sức khỏe [SoKSK]; Ngày khám sức khỏe [NgKSK]; Loại sức khỏe [LoaiKSK]; Nhóm máu [NhomMau]; Chiều cao [ChieuCaoNV]; Căn nặng [CanNangNV]; Có SBH [CoSBH]; Số bảo hiểm [SoSBH]; Ngày cấp [NgCapSBH]; Nơi cấp [NoiCapSBH]; Số sổ BHYT [SoSBHYT]; Ngày cập nhật HS [NgayNhapHoSo]; Ngày cấp mã GV [NgayCapMaNV]; Ngày cấp tiến sĩ [NgayTSi]; SL Th.Si hướng dẫn [SLThSiHD]; SL sách viết [SLSachViet]; SL đề tài cấp bộ [SLDTBo]; SL đề tài cấp cơ sở [SLDTCoSo]; Ngày cấp PGS [NgayPGS]; SL sách viết (sau PGS) [SLSachViet1]; SL đề tài cấp bộ(sau PGS) [SLDTBo1]; SL đề tài cấp cơ sở(sau PGS) [SLDTCoSo1]; Mã trình độ [MaBacNV]; Năm BĐGD [NamBDGD1]; Năm BĐGD ĐH Mở [NamBDGD2]; Văn bằng 1 [VanBang1]; Năm TN 1 [NamTN1]; Nơi TN 1 [NoiTN1]; Ngành TN 1 [NganhTN1]; Văn bằng 2 [VanBang2]; Năm TN 2 [NamTN2]; Nơi TN 2 [NoiTN2]; Ngành TN 2 [NganhTN2]; Văn bằng 3 [VanBang3]; Năm TN 3 [NamTN3]; Nơi TN 3 [NoiTN3]; Ngành TN 3 [NganhTN3]; Ghi chú [GhiChuTN]; Họ lót [HoLotNV]; Tên nhân viên [TenNV]; Tên đầy đủ [TenDayDuNV]; Mã phân loại GV [MaPLGV]; Mã Nhóm CB-GV-NV [MaLoaiDTCBGD]; Mã Bệnh viện [MABENHVIEN]; Mã ĐB quốc tịch [MADBQUOCTICH]; Mã ĐB quê quán [MADBQUEQUAN]; Mã ĐB nơi sinh [MADBNOISINH]; Mã ĐB tam trú [MADBTAMTRU]; Mã ĐB LL NV [MADBLLNV]; Ngân hàng [IDNH]; Mã ngân hàng 2 [IDNH2]
### Imp_PhanToThi – Phân tổ thi theo file
- Lưới 1 (bảng LToThi); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Nhóm thi [NhomThi]; Tổ thi [ToThi]; Mã SV [MaSV]
### IMP_SVDKMonDTNH – Import sinh viên đăng ký môn ĐTNH
- Lưới 1 «Danh sách SV» (bảng FKQDKDTNH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Phân loại sinh viên [LoaiDTDKDTNH]; Mã SV [MaSV]; Mã môn học [MaMonDTNH]; % học phí miễn giảm [MienGiamDTNH]
  - Cột ẩn: Sinh viên [IDSV]
### IMP_TKB_NGAY – Import thời khóa biểu ngày
- Lưới 1 (bảng KToHoc); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Nhóm học [NhomHoc]; Tổ TH [ToTH]; Tên tổ hợp [TenToHop]; Thứ tự xếp [TTToHop]; Mã lớp [MaLop]; Mã viên chức [MaNV]; Mã tính chất phòng [MaTCPhong]; Sức chứa [SucChuaPH]; Tổng số tiết xếp TKB [SoTietTKB]; Số tiết thi [SoTietThi]; Mã công thức TG [MADNTGHOC]; Mã công thức TG thi [MADNTGTHI]; Thứ tự đợt học [DOTHOCLOP]
### IMP_TMIENTHI – View import TMIENTHI
- Lưới 1 (bảng TMIENTHI); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã DS thí sinh [MADSTS]; Mã môn [MAMONTS]; Lý do miễn thi [GCMIENTHI]
### IMP_TSCoDinh – Import tài sản cố định
- Lưới 1 «Import tài sản cố định» (bảng JDmTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã tài sản/vật tư [MaTS]; Mã vạch [MaVachTS]; Tên tài sản/ vật tư [TenTS]; Mã nhóm tài sản [MaNhomTS]; Số hiệu tài sản [SoHieuTS]; Qui cách tài sản [QuiCachTS]; Mã Đơn vị tính [MaDVTinh]; Nước sản xuất [NuocSX]; Hãng sản xuất [HangSX]; Năm sản xuất [NamSanXuat]; Mã dự án [MaDuAn]; Loại hình phục vụ [LoaiHinhPVTS]; Hình thức hình thành tài sản [HinhThucHTTS]; Nguồn vốn tài sản [NguonVonTS]; Đơn giá [DonGiaTS]; Thuế VAT (%) [ThueVAT]; Nguyên giá [NguyenGiaTS]; Loại tài sản [LoaiTS]; Phục vụ học tập [IsTSHocTap]; Bồi thường hư hỏng [IsTSBoiThuong]; Ngày bắt đầu sử dụng [NgayBDSD]; Số năm sử dụng [SoNamSD]; Ngày hết hạn sử dụng [NgayHHSD]; Chất lượng tài sản [ChatLuongTS]; Ngày bắt đầu khấu hao [NgayBDKH]; Tỉ lệ khấu hao [TiLeKhauHao]; Định kỳ bảo dưỡng tài sản [DKBDTS]; Mua [SoLuongNhapMua]; ID đơn vị quản lý tài sản [IDDVQuanLyTS]
### IMP_TSCongCu – Import tài sản công cụ
- Lưới 1 «Import tài sản công cụ» (bảng JDmTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã tài sản/vật tư [MaTS]; Mã vạch [MaVachTS]; Tên tài sản/ vật tư [TenTS]; Mã nhóm tài sản [MaNhomTS]; Số hiệu tài sản [SoHieuTS]; Qui cách tài sản [QuiCachTS]; Mã Đơn vị tính [MaDVTinh]; Nước sản xuất [NuocSX]; Hãng sản xuất [HangSX]; Năm sản xuất [NamSanXuat]; Mã dự án [MaDuAn]; Loại hình phục vụ [LoaiHinhPVTS]; Hình thức hình thành tài sản [HinhThucHTTS]; Nguồn vốn tài sản [NguonVonTS]; Đơn giá [DonGiaTS]; Thuế VAT (%) [ThueVAT]; Nguyên giá [NguyenGiaTS]; Ghi chú [GcTS]; Phục vụ học tập [IsTSHocTap]; Bồi thường hư hỏng [IsTSBoiThuong]; Ngày bắt đầu sử dụng [NgayBDSD]; Số năm sử dụng [SoNamSD]; Ngày hết hạn sử dụng [NgayHHSD]; Chất lượng tài sản [ChatLuongTS]; Ngày bắt đầu khấu hao [NgayBDKH]; Tỉ lệ khấu hao [TiLeKhauHao]; Định kỳ bảo dưỡng tài sản [DKBDTS]; Mua [SoLuongNhapMua]{số}
### IMP_TSVatTu – Import tài sản vật tư
- Lưới 1 «Import tài sản vật tư» (bảng JDmTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã tài sản/vật tư [MaTS]; Mã vạch [MaVachTS]; Tên tài sản/ vật tư [TenTS]; Tên tiếng anh [TenTSEg]; Loại vật tư [LoaiVatTu]; Qui cách tài sản [QuiCachTS]; Mã nhóm tài sản [MaNhomTS]; Mã Đơn vị tính [MaDVTinh]; Phục vụ học tập [IsTSHocTap]; Bồi thường hư hỏng [IsTSBoiThuong]; Ghi chú [GcTS]; Đơn giá [DonGiaTS](chỉ đọc)
### IMP_VCNCKH – Import đề tài viên chức
- Lưới 1 (bảng ODeTaiNCKH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đề tài [MaDeTaiNCKH]; Tên đề tài [TenDeTaiNCKH]; Mã loại đề tài NCKH [MaLoaiDeTaiNCKH]; Mã viên chức [MaNV]; Ngày bắt đầu [NgayBDDeTai]; Ngày kết thúc [NgayKTDT]; Nội dung kinh phí [NoiDungKP]; Số tiền đề nghị [SoTienDNKP]
### IMPORT01 – Chọn danh sách import
- Lưới 1 (bảng HImportTpl); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Tên mẫu import [TenImportTpl]; Phiên bản import [VersionImp]; ID Import template [IDImportTpl]
  - Cột ẩn: ID View [IDView]; Ngày thêm [NgayThem]
  - Ô trên form sửa: #TenImportTpl, #VersionImp, #NgayThem
### IMPORT02 – Danh sách chi tiết mẫu import
- Lưới 1 (bảng HImportDefine); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Sửa bên phải
### IMPORT_CAUHOI – Danh sách câu hỏi
- Lưới 1 (bảng ZCauHoi); tắt: Import, Nạp lại, Đổi mã, Sửa trên lưới
  - Cột: Thứ tự câu hỏi [TTCauHoi]; Thứ tự ghi trên form [TTCHForm]; Nội dung câu hỏi [NoiDungCauHoi]; Kiểu trả lời [KieuTraLoi]{chọn}; Mã enum đánh giá [MaEnumDG]; Loại thống kê đánh giá [LoaiTKDG]{chọn}; Có ý kiến khác [IsYKienKhac]; Có gán giá trị từ hệ thống [IsGanTTHT]; Bắt buộc trả lời [IsBatBuocTraLoi]; Mã nhóm câu hỏi [MaNhomCauHoi]; Nội dung nhóm câu hỏi [NoiDungNhomCauHoi]
  - Ô trên form sửa: #TTCauHoi, #TTCHForm, #NoiDungCauHoi, #KieuTraLoi, #LoaiTKDG, #IsYKienKhac, #IsGanTTHT
### Import_MSTTTToiThieu – Import số tiền đóng tối thiểu
- Lưới 1 «Import số tiền đóng tối thiểu» (bảng MSTTTToiThieu); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: STTTToiThieu [STTTToiThieu]
### IMPORT_SELECT_SV – Import select danh mục sinh viên
- Lưới 1 (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]
### IMPORT_SV_QD_MAKHONGTT – Sinh viên không tồn tại mã
- Lưới 1 «Danh sách không hợp lệ» (bảng SSVHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Phái [Phai]{chọn}; Hiện diện [HienDienSV2]{chọn}; Mã lớp (cũ) [MaLopCu]
### IMPORT_SV_QD_TONTAI – Sinh viên đã tồn tại
- Lưới 1 «Danh sách sinh viên đã tồn tại» (bảng SSVHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Phái [Phai]{chọn}; Hiện diện SV [HienDienSV]{chọn}; Mã lớp (cũ) [MaLopCu]
### IMPORT_SV_QUYETDINH – Import sinh viên  QD thành công
- Lưới 1 «Danh sách sinh viên hợp lệ» (bảng SSVHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Phái [Phai]{chọn}; Hiện diện [HienDienSV2]{chọn}; Mã lớp (cũ) [MaLopCu]
### IMPORT_SVDIEMDANH – Import sinh viên điểm danh
- Lưới 1 «Import sinh viên điểm danh» (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Trạng thái điểm danh [TrangThaiDiemDanh]; Ngày giờ vào lớp [NgayGioVaoLop]; Số phút về sớm [SoPhutVeSom]; Số phút vào trể [SoPhutVaoTre]; Ghi chú [GCSVDiemDanh]
### IMPORTCHUANTHANHCONG – Dữ liệu import thành công
- Lưới 1 «Danh sách import hợp lệ» (bảng KCTDTCH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Mã Ng/CNg [MaNgChng]; Mã PB [MaPB]; Xét học kỳ thứ [HKThu]; Mã môn học [MaMH]; Môn bắt buộc [IsMHBB]; Môn tốt nghiệp? [IsMHTN]
### IMPORTCHUANTHATBAI – Dữ liệu import thất bại
- Lưới 1 «Danh sách import không hợp lệ» (bảng KCTDTCH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Mã Ng/CNg [MaNgChng]; Mã PB [MaPB]; Xét học kỳ thứ [HKThu]; Mã môn học [MaMH]; Môn bắt buộc [IsMHBB]; Môn tốt nghiệp? [IsMHTN]
### IMPORTCHUANTONTAI – Dữ liệu đã tồn tại
- Lưới 1 «Danh sách dữ liệu đã tồn tại» (bảng KCTDTCH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Mã Ng/CNg [MaNgChng]; Mã PB [MaPB]; Xét học kỳ thứ [HKThu]; Mã môn học [MaMH]; Môn bắt buộc [IsMHBB]; Môn tốt nghiệp? [IsMHTN]
### ImportDCSChungTC – Danh sách import hợp lệ
- Lưới 1 «Danh sách import hợp lệ» (bảng SDCSSVC); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Mã trợ cấp xã hội [MaTCXH]; Mã diện chính sách [MaDCS]; NHHK bắt đầu [NHHKBD]; NHHK kết thúc [NHHKKT]
### ImportDCSChungTCCopy – Danh sách import thất bại
- Lưới 1 «Danh sách import lỗi» (bảng SDCSSVC); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Mã diện chính sách [MaDCS]; Mã trợ cấp xã hội [MaTCXH]; NHHK bắt đầu [NHHKBD]; NHHK kết thúc [NHHKKT]
### ImportDCSChungTCCopyCopy – Danh sach import ton tai
- Lưới 1 «Danh sách sinh import tồn tại» (bảng SDCSSVC); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Mã diện chính sách [MaDCS]; Mã trợ cấp xã hội [MaTCXH]; NHHK bắt đầu [NHHKBD]; NHHK kết thúc [NHHKKT]
### IMPORTDSHSTC – Danh sách import HS hợp lệ
- Lưới 1 «Danh sách hồ sơ sinh viên» (bảng SHSSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Phái [Phai]; Mã hồ sơ [MaHS]; Tên hồ sơ [TenHS]
### IMPORTDSHSTCCopy – Danh sách import HS thất bại
- Lưới 1 «Danh sách sinh viên» (bảng SHSSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Phái [Phai]; Mã hồ sơ [MaHS]; Tên hồ sơ [TenHS]
### IMPORTDSHSTCCopyCopy – Danh sách import HS ton tại
- Lưới 1 «Danh sách hồ sơ sinh viên» (bảng SHSSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Phái [Phai]; Mã hồ sơ [MaHS]; Tên hồ sơ [TenHS]
### ImportFileMaSV – Import MaSV để in danh sách khen thưởng kỷ luật
- Lưới 1 (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]
### ImportHopLeChng – Danh sach import thanh công
- Lưới 1 «Danh sách sinh viên» (bảng SDCSSVC); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Mã Ng/CNg [MaNgChng]; Tên ng/chng [TenNgChng]
### ImportHopLeChngCopy – Danh sach import loi
- Lưới 1 «Danh sách sinh viên» (bảng SDCSSVC); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Mã Ng/CNg [MaNgChng]; Tên ng/chng [TenNgChng]
### IMPORTMHTHANHCONG – Dữ liệu import thành công
- Lưới 1 «Danh sách môn học» (bảng KDMMH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Số TC học phí [SoTinChiHP]; Mã đơn vị [MaDV]; Lý thuyêt [LT]; Thực hành [TH]; Đề án [DA]; Luận án [LA]; Thực tập [TT]
### IMPORTMHTHATBAI – Dữ liệu import thất bại
- Lưới 1 (bảng KDMMH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Số TC học phí [SoTinChiHP]; Mã đơn vị [MaDV]; Lý thuyêt [LT]; Thực hành [TH]; Đề án [DA]; Luận án [LA]; Thực tập [TT]
### IMPORTMHTONTAI – Dữ liệu import tồn tại
- Lưới 1 (bảng KDMMH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Số TC học phí [SoTinChiHP]; Mã đơn vị [MaDV]; Lý thuyêt [LT]; Thực hành [TH]; Đề án [DA]; Luận án [LA]; Thực tập [TT]
### KCTDTTH – Chương trinh dao tao thực hiện
- Lưới 1 «Chương trình đào tạo thực hiện» (bảng KCTDTTH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]
  - Cột ẩn: Bài tập [BT]; Ghi chú [GhiChu]; Mã khối [IDKhoi]; Niên học học kỳ [NHHK]
  - Ô trên form sửa: #BT, #GhiChu, #IDKhoi, #NHHK
  - Nút btnSave: "save" (F2)
  - Nút barBtnHuy: "huy" (F5)
  - Nút btnAdd: "add" (F1)
  - Nút btnDelete: "Xoa" (F4)
  - Nút btnUpdate: "sua" (F3)
### KCTDTTH_FIX – Chương trinh dao tao thực hiện
- Lưới 1 «Danh sách khối đã có chương trình đào tạo» (bảng KCTDTTH); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; Mã bậc hệ [MaBH]; Mã Ng/CNg [MaNgChng]; Khóa [LockCTDTTH]
  - Cột ẩn: Ghi chú [GcKhoi]; Ghi chú [GhiChu]; Mã khối [IDKhoi]; Niên học học kỳ [NHHK]; Nội dung [NoiDungTH]
  - Ô trên form sửa: #TenKhoi, #GhiChu, #IDKhoi
### KCTDTTHCOPY – Chương trinh dao tao thực hiện
- Lưới 1 «Danh sách khối» (bảng KCTDTTH); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; Mã bậc hệ [MaBH]; Mã Ng/CNg [MaNgChng]
  - Cột ẩn: Bài tập [BT]; Ghi chú [GhiChu]; Mã khối [IDKhoi]; Niên học học kỳ [NHHK]
  - Ô trên form sửa: #TenKhoi, #BT, #GhiChu, #IDKhoi
### KDeCuongMHCT – Gán đề cương môn học cụ thể
- Lưới 1 «Danh sách đề cương» (bảng KDeCuongMH); tắt: Thêm, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đề cương [MaDeCuong](chỉ đọc); Tên đề cương [TenDeCuong](chỉ đọc); Ghi chú đề cương [GCDeCuong](chỉ đọc); Người biên soạn [NguoiBienSoan](chỉ đọc); Xem chi tiết [XemChiTiet]
  - Cột ẩn: IDDeCuong [IDDeCuong]; IDDeCuongMH [IDDeCuongMH]; Môn học [IDMH]
### KDMBACCHON – Danh mục chọn bậc
- Lưới 1 «Danh sách bậc» (bảng KDMBac); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc [MaBac]; Tên bậc đào tạo [TenBac]; Tên viết tắt [VtBac]
### KDMBHNHHK – Danh mục bậc hệ năm vào (~)
- Lưới 1 «Danh mục bậc hệ năm vào» (bảng KDmBHNHHK); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã bậc hệ NHHK [MaBHNHHK]; Tên bậc hệ NHHK [TenBHNHHK]; NHHK vào [NHHKVao]{số}; Bậc hệ [IDBH]
  - Cột ẩn: BH năm mặc định [DfBHNHHK]; Ghi chú [GCBHNHHK]; Không quản lý [HuyBHNHHK]; ID BH NHHK [IdBHNHHK]; Mã user [MaUser]; Ngày thêm [NgayThem]; Thứ tự [TTBHNHHK]; Tên viết tắt [VTBHNHHK]
  - Ô trên form sửa: #MaBHNHHK, #TenBHNHHK, #NHHKVao, #IDBH, #GCBHNHHK, #VTBHNHHK
### KDMBHTK – Danh mục bậc hệ thống kê
- Lưới 1 «Danh mục bậc hệ thống kê» (bảng KDMBHTK); tắt: Sửa trên lưới
  - Cột: Mã bậc hệ thống kê [MaBHTK]; Tên bậc hệ thống kê [TenBHTK]; Viết tắt bậc hệ thống kê [VtBHTK]
  - Cột ẩn: Ghi chú bậc hệ thống kê [GcBHTK]; Tên tiếng anh [TenBHTKEg]
  - Ô trên form sửa: #MaBHTK, #TenBHTK, #VtBHTK, #GcBHTK, #TenBHTKEg
  - Nút barUctrlDongBo: "Khởi tạo DS tự động" (F0)
### KDMLDSDPH – Danh mục loại hình sử dụng phòng
- Lưới 1 «Danh mục lý do sử dụng» (bảng KDMLDSDPH); tắt: Sửa trên lưới
  - Cột: Mã lý do [MaLDSDPH]; Tên lý do [TenLDSDPH]; Tên viết tắt [VtLDSDPH]; Mặc định [DfLDSDPH]
  - Cột ẩn: Ghi chú [GcLDSDPH]; Không quản lý [HuyLDSDPH]; Tên tiếng anh [TenLDSDPHEg]
  - Ô trên form sửa: #MaLDSDPH, #TenLDSDPH, #VtLDSDPH, #DfLDSDPH, #GcLDSDPH, #TenLDSDPHEg
### KDMMH – Danh mục môn học
- Lưới 1 «Danh mục môn học» (bảng KDMMH); tắt: Sửa trên lưới
  - Cột: Đơn vị phân cấp [IDDVPC]; Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]{số}; Mã đơn vị [MaDV]; Tên đơn vị [TenDV]; Số tiết môn học [SoTietMH]{số}; Lý thuyêt [LT]; Thực hành [TH]; Bài tập [BT]; Thực hành khác [THK]; Bài tập lớn [BTL]; Đề án [DA]; Luận án [LA]; Tốt nghiệp [TN]; Thực tập [TT]; TTLT [TTLT]; TTTH [TTTH]; LMS [LMS]; Lâm sàng [LS]; Môn tốt nghiệp? [IsMHTN]; Không tính ĐTB [KhgTinhDTB]; Sỉ số max SV LT [SiSoMaxLT]; Sỉ số mã SV TH [SiSoMaxTH]; Trường liên kết [IDDP]; Không xét trùng lịch thi khi đăng ký môn học [IsKgXetTrungLThiKhiDKMH]; Mức đơn giá LT [MucDGLT]{số}; Mức đơn giá TH [MucDGTH]{số}; Nhóm MH [IDNhomMH]; Cho học vượt [IsMHChoVuot]; Môn học đặt thù [IsMHDacThu]
  - Cột ẩn: GC môn học 1 [GCMH2]; Ghi chú [GcMH]; Ghi chú [GhiChu]; Đơn vị [IDDV]; Hình thức thi [IDHTThi]; Loại bệnh án [IDLoaiBenhAn]; Không xếp lịch thi [IsKgXepLThi]; Không xếp phòng TKB [IsKgXepPh]; Không tính vào số tín chỉ tối đa khi ĐKMH [IsKghXetTCDK]; Không xếp thời khóa biểu [IsKhgXepTKB]; Môn kiểm tra [IsMonKT]; Kiểm tra [KT]; Khối kiến thức [KhoiKTGD]{chọn}; Môn IELTS [MHTOEIC]; Mã loại bệnh án [MaLoaiBenhAn]; NHHK bắt đầu [NHHKBD]; Tỷ lệ cấm thi LT [PTVangLTCamThi]; Tỷ lệ cấm thi TH [PTVangTHCamThi]; Phân loại thực hành [PhanLoaiTH]{chọn}; Số sv tối đa [SiSoMax]{số}; Sĩ số min [SiSoMin]{số}; Số CBGD tối đa [SoCBMax]{số}; Số tiết 2 [SoTiet2]; ST lý thuyết [SoTietMHLT]; ST thực hành [SoTietMHTH]; Số tiết/tuần [SoTietTuan]{số}; Số TC EU [SoTinChiEU]{số}; Số TC học phí [SoTinChiHP]{số}; Tự học [TUH]; Tên loại bệnh án [TenLoaiBenhAn]; Tên tiếng anh [TenMHEg]; Tên MH tiếng pháp [TenMHFr]; Tính chất môn học [TinhChatMH]{chọn}; Tên viết tắt [VtMH]; Xếp lịch thi SS [XepLichThiSS]
  - Ô trên form sửa: #IDDVPC, #MaMH, #TenMH, #SoTinChi, #TH, #BT, #LS, #IsMHTN, #KhgTinhDTB, #IDDP, #IsKgXetTrungLThiKhiDKMH, #MucDGLT, #MucDGTH, #IDNhomMH, #IsMHChoVuot, #IsMHDacThu, #GCMH2, #GcMH, #GhiChu, #IDDV, #IDHTThi, #IDLoaiBenhAn, #IsKgXepLThi, #IsKgXepPh, #IsKghXetTCDK, #IsKhgXepTKB, #IsMonKT, #KhoiKTGD, #MHTOEIC, #NHHKBD, #SoCBMax, #SoTiet2, #SoTinChiEU, #SoTinChiHP, #TenMHEg, #TenMHFr, #TinhChatMH, #VtMH, #XepLichThiSS
### KDMPB – Danh mục phiên bản CTĐT
- Lưới 1 «Danh mục phiên bản chương trình đào tạo» (bảng KDMPB); tắt: Sửa trên lưới
  - Cột: Đơn vị phân cấp [IDDVPC]; Mã PB [MaPB]; Tên phiên bản [TenPB]; Tên viết tắt [VtPB]; Năm học học kỳ bắt đầu [NHHK]; NHHK ra [NHHKRa]
  - Cột ẩn: Ghi chú [GcPB]; Không quản lý [HuyPB]; Nội dung [NoiDung]
  - Ô trên form sửa: #IDDVPC, #MaPB, #TenPB, #VtPB, #NHHK, #NHHKRa, #GcPB, #NoiDung
### KDMPH – Danh mục phòng học
- Lưới 1 «Danh mục phòng học» (bảng KDMPH); tắt: Sửa trên lưới
  - Cột: Mã phòng [MaPH]; Tên phòng [TenPH]; Sức chứa [SucChuaPH]{số}; Sức chứa thi [SucChuaThi]{số}; Mã tính chất phòng [MaTCPhong]; Tên tính chất phòng [TenTCPhong]; Tên cơ sở [TenCoSo]; Mã cơ sở [MaCoSo]; Diện tích sử dụng [DienTichSD]; Đơn vị phân cấp quản lý [IDDVPCQL]; Mã đơn vị phân cấp [MaDVPC]
  - Cột ẩn: Dãy phòng [DayPH]; Ghi chú [GcPH]; Không quản lý [HuyPH]; Cơ sở [IDCoso]; TC Phòng [IDTCPhong]; Phòng trực [PhongTT]; Tên viết tắt [VTPH]
  - Ô trên form sửa: #MaPH, #TenPH, #SucChuaPH, #SucChuaThi, #DienTichSD, #IDDVPCQL, #DayPH, #GcPH, #HuyPH, #IDCoso, #IDTCPhong, #PhongTT
  - Nút btnSave: "Save" (F3)
### kdmqctest – kdmqctest
- Lưới 1 (bảng KDMQC); tắt: Nạp lại, Sửa trên lưới
  - Cột: ID qui chế [IDQC]; Tên qui chế VB [TenQCVB]; Mã qui chế [MaQC]; ID qui chế cha [IDQCP]
  - Ô trên form sửa: #TenQCVB, #MaQC, #IDQCP
### KDmThietBi – KDmThietBi
- Lưới 1 «Danh mục thiết bị phòng» (bảng KDmThietBi); tắt: Sửa trên lưới
  - Cột: Mã thiết bị [MaThietBi]; Tên thiết bị [TenThietBi]; Quy cách thiết bị [QuyCachThietBi]; Hãng sản xuất [HangSX]; Nước sản xuất [NuocSX]
  - Cột ẩn: Đơn vị tính [IDDVTinh]
  - Ô trên form sửa: #MaThietBi, #TenThietBi, #QuyCachThietBi, #HangSX, #NuocSX, #IDDVTinh
### KDMThietBiHocTap – Danh mục thiết bị học tập
- Lưới 1 «Danh sách thiết bị»; tắt: Nạp lại, Sửa trên lưới
### KDMTRUONGLT – Danh mục trường liên kết
- Lưới 1 «Danh mục trường liên kết» (bảng KDMTRUONGLT); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã trường liên kết [MaTruongLT]; Tên trường liên kết [TenTruongLT]; Tên viết tắt [VTTruongLT]
  - Cột ẩn: Chức vụ người LL [ChucVuLL]; Địa chỉ liên lạc [DC_DCLLSV]; Địa chỉ [DC_DCLT]; Điện thoại nhà riêng [DC_DT1LT]; Điện thoại di động [DC_DT2LT]; Email 1 [DC_EM1LT]; Email 2 [DC_EM2LT]; Ghi chú [DC_GCLT]; Quận/huyện [DC_IDDBLT]; Trường lk mặc định [DfTruongLT]; Ghi chú [GcTruongLT]; Không quản lý [HuyTruongLT]; Người liên lạc [NguoiLL]; Số phòng mul [SOPHMUL]; Số lượng phòng [SOPHONG]; Thứ tự [TTTruongLT]; Tên tiếng anh [TenTruongLTEg]
  - Ô trên form sửa: #MaTruongLT, #TenTruongLT, #VTTruongLT, #ChucVuLL, #DC_DCLLSV, #DC_DCLT, #DC_DT1LT, #DC_DT2LT, #DC_EM1LT, #DC_EM2LT, #DC_IDDBLT, #GcTruongLT, #HuyTruongLT, #NguoiLL, #SOPHMUL, #SOPHONG, #TenTruongLTEg
### KDNTGHOC – Định nghĩa thời gian học
- Lưới 1 «Danh sách thời gian học chi tiết» (bảng KDNTGHOCCT); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Thứ [Thu]; Tiết BĐ [TietBD]; Số tiết [SoTiet]; Cụm xen kẽ [CumXenKe]{số}
  - Ô trên form sửa: #Thu, #TietBD, #SoTiet, #CumXenKe
- Lưới 2 «Danh sách định nghĩa công thức thời gian học» (bảng KDNTGHOC); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã công thức TG [MADNTGHOC]; Tên công thức TG [TENDNTGHOC]; Vắt tắt [VTDNTGHOC]; Mã loại thời gian [MaLoaiTG]
  - Cột ẩn: Loại thời gian [IDLoaiTG]; Học xen kẻ [IsHocXenKe]; Xếp tối thiểu tuần [IsXepToiThieuTuan]; Tên tiếng anh [TENDNTGHOCEG]; Thứ xếp đầu tiên [ThuXepDau]{số}
  - Ô trên form sửa: #MADNTGHOC, #TENDNTGHOC, #VTDNTGHOC, #IDLoaiTG, #IsHocXenKe, #IsXepToiThieuTuan, #TENDNTGHOCEG, #ThuXepDau
### KDuyetKQDK – Danh sách dữ liệu duyệt kết quả đăng ký
- Lưới 1 «Dữ liệu duyệt kết quả đăng ký sinh viên trong học kỳ» (bảng KDuyetKQDK); tắt: Thêm, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Trạng thái duyệt [IsDuyetKQDK]{chọn}; Mã SV [MaSV]; Họ và tên [TenDayDu]; Ngày lưu [NgayThem]{ngày}; Mã giảng viên [MaNV]; Ghi chú [GhiChu]
  - Cột ẩn: Sinh viên [IDSV]
### KH_CapNhatKTTPMH – Cap nhat tiet thanh phan mon hoc
- Lưới 1 (bảng KDMMH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Bài tập [BT]; Bài tập lớn [BTL]; Thực hành [TH]; Thực hành khác [THK]; Đề án [DA]; Tốt nghiệp [TN]; Thực tập [TT]; Kiểm tra [KT]; Lý thuyêt [LT]; Luận án [LA]; Tự học [TUH]; TTLT [TTLT]; TTTH [TTTH]; LMS [LMS]; Lâm sàng [LS]; Sỉ số max SV LT [SiSoMaxLT]; Sỉ số mã SV TH [SiSoMaxTH]; Số TC LT [SoTCTPMHLT]; Số TC TH [SoTCTPMHTH]; SoTCTPMHLT [SoTCTPMHLS]
### KHGD_ViewCapNhatMH_KG_DTB – View cap nhat kg tinh diem trung binh
- Lưới 1 «Danh sách môn học» (bảng KDMMH); tắt: Thêm, Xóa, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Không tính ĐTB [KhgTinhDTB]{số}
### KHGD_ViewCapNhatMH_LUAN – View cap nhat mon hoc luan an
- Lưới 1 «Danh sách môn học» (bảng KDMMH); tắt: Thêm, Xóa, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Môn luận án [IsMHLA]
### KHGD_ViewDinhNghiaMHMoDun – View định nghĩa môn học mô đun
- Lưới 1 «Danh sách môn học mô đun» (bảng KMHMODUN); tắt: Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Trọng số điểm [TrongSoMonModun]; Cách tính điểm [CachTinhMonModun]{chọn}; Tính học phí môn Mô-đun [IsTinhHPModun]; Không đạt khi ĐTK 1 MH < [KhgDatKhiDTKMonCon]{số}
  - Cột ẩn: Ghi chú dùng bên detailright [GhiChuView1]; Môn học cha [IDMHCha]
  - Ô trên form sửa: #TenMH, #SoTinChi, #CachTinhMonModun, #IsTinhHPModun, #KhgDatKhiDTKMonCon, #GhiChuView1, #IDMHCha
### KHGD_ViewDKMonTN – View cap nhat mon hoc điều kiện tốt nghiệp
- Lưới 1 «Danh sách môn học(Môn học điều kiện xét TN chỉ sử dụng trên mẫu in bảng điểm 1 SV)» (bảng KDMMH); tắt: Thêm, Xóa, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Môn học ĐK xét TN [IsMHDKTN]
### KHGD_VieweCapNhat_MH_TQHB – View cap nhat mon hoc luan an
- Lưới 1 «Danh sách môn học» (bảng KDMMH); tắt: Thêm, Xóa, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Môn T.Quyết HB [IsMHTQHB]
### KHGD_ViewImportMHMoDun – View import mon hoc mo dun
- Lưới 1 (bảng KMHMODUN); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Môn học cha [IDMHCha]; Môn học con [IDMHCon]
### KHGD_ViewKhoaMHTQHB – View dinh nghia khoa mhtq hb
- Lưới 1 «Danh sách khoa»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khoa [MaKhoa]; Tên khoa [TenKhoa]
  - Cột ẩn: Ghi chú dùng bên detailright [GhiChuView1]; Mã khoa [IDKHOATQ]
  - Ô trên form sửa: #TenKhoa, #GhiChuView1, #IDKHOATQ
### KHGD_ViewMHCon – Định nghĩa môn học con
- Lưới 1 «Danh sách môn học thuộc mô đun»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Trọng số điểm [TrongSoMonModun]
### KHGD_ViewTCDKMin – View cap nhat tin chi dK min
- Lưới 1 «Xem sửa  TC đạt/ĐK Min cho phép đăng ký theo MH» (bảng KDMMH); tắt: Thêm, Xóa, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); TC đạt Min [GCTCDat]{số}; TC ĐK min [GHTCDK]{số}
### KHGD_ViewXemTCKhoi – View xem tong so tin chi theo khoi
- Lưới 1 «Danh sách khối»; tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; Số tín chỉ [TongTC]
### KK – kk
- Lưới 1 (bảng HUser); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### KPHHK – Danh sách phòng học kỳ
- Lưới 1 «Danh sách phòng được sử dụng trong học kỳ» (bảng KPHHK); tắt: Xuất, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã phòng học kỳ [MaPhHK]; Mã phòng(danh mục) [MaPH](chỉ đọc); Tên phòng [TenPHHK]; Sức chứa [SucChuaPH]; Sức chứa thi [SucChuaThi]; Dãy phòng [DayPHHK]; Phòng trực [PhongTTHK]; Tính chất phòng [TCPhongHK]; Cơ sở [IDCoso]; Diện tích sử dụng [DienTichSD](chỉ đọc); Đơn vị phân cấp quản lý [IDDVPCQL]; Mã đơn vị phân cấp [MaDVPC]; Tên đơn vị phân cấp [TenDVPC]
  - Cột ẩn: ID phòng hk [IDPHHK]; TC Phòng [IDTCPhong]; Che phòng [IsChe]; Phòng giả [IsPhongGia]; Mã tính chất phòng [MaTCPhong]; Niên học học kỳ [NHHK]
### KSDG_ViewBangXepHang – Bang xep hang danh gia doi tuong
- Lưới 1 «Danh sách đối tượng được đánh giá»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã ĐT được đánh giá [MaDTDG0]; Tên ĐT được đánh giá [TenDTDG0]; Số lượng [SoLuong]; Tổng điểm TK chính [Tong1]; Tổng điểm TK phụ [Tong2]; Trung bình 1 [TrungBinh1]; Trung bình 2 [TrungBinh2]
### KTuanKHHK – Tuần kế hoạch học kỳ
- Lưới 1 «Bảng tham chiếu tuần lễ» (bảng KTuanKHHK); tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa bên phải
  - Cột: Tuần năm học [TuanBD](chỉ đọc); Tuần học kỳ [TuanBDHK](chỉ đọc); Từ ngày [NgayBDH]{ngày}(chỉ đọc); Đến ngày [NgayKTH]{ngày}(chỉ đọc); Ghi chú [KeHoach]; Đợt trong học kỳ [DotHK]
### LCAPNHATCANBOCOITHI – Cập nhật phòng thi
- Lưới 1 «Danh sách tổ thi đã xếp lịch thi» (bảng LToThi); tắt: Thêm, Xóa, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Nhóm thi [NhomThi](chỉ đọc); Tổ thi [ToThi](chỉ đọc); Sĩ số tổ thi [SiSoToThi](chỉ đọc); Số tiết thi [SoTietThi](chỉ đọc); Ngày thi [NgayThi]{ngày}(chỉ đọc); Tiết BĐ [TietThiBD](chỉ đọc); Mã phòng [MaPH]{nút …}(chỉ đọc); SL coi thi [SLCanBoCoiThi]{số}
  - Cột ẩn: ID phòng thi [IDPThi]; Loại đối tượng [LoaiDTuong](chỉ đọc); Mã đối tượng [MaDoiTuong](chỉ đọc); Phòng đợi [MaPHDoi]{nút …}(chỉ đọc); Mã tính chất phòng [MaTCPhong](chỉ đọc); Môn thi [MonThi](chỉ đọc); Ngày thi dự kiến [NgayThiDuKien]{ngày}(chỉ đọc); Sĩ số tổ thi [SiSoDuKien](chỉ đọc); Tiết thi dự kiến [TietThiDuKien](chỉ đọc)
### LCAPNHATPHONG – Phân công coi thi
- Lưới 1 «Hiệu chỉnh lịch thi cho danh sách tổ thi ( LƯU Ý: CHƯƠNG TRÌNH LƯU DỮ LIỆU NGAY KHI  THAY ĐỔI DỮ LIỆU)» (bảng LToThi); tắt: Thêm, Xóa, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Lớp tín chỉ [NhomTo](trường đổi nhãn)(chỉ đọc); Mã lớp [MaLop](chỉ đọc); Mã viên chức [MaNV](chỉ đọc); Tên đầy đủ [TenDayDuNV](chỉ đọc); Nhóm thi [NhomThi](chỉ đọc); Tổ thi [ToThi](chỉ đọc); Số tiết nhóm thi [SoTietThi](chỉ đọc); Ngày thi [NgayThi]{ngày}; Tiết BĐ [TietThiBD]; Chọn phòng thi [MaPH]{nút …}; Mã tính chất phòng [MaTCPhong](chỉ đọc); Mã hình thức thi [MaHTThi](chỉ đọc); Ghi chú tổ thi [GCToThi]; Mã bộ môn [MaBOMON](chỉ đọc); Tên bộ môn [TenBOMON](chỉ đọc)
  - Cột ẩn: ID phòng thi [IDPThi]; Loại ĐT [LoaiDTuong](chỉ đọc); Mã BM QL MH [MaBmQLMH](chỉ đọc); Mã ĐT [MaDoiTuong](chỉ đọc); Mã khoa quản lý bộ môn [MaKhoaBM](chỉ đọc); Chọn phòng đợi [MaPHDoi]{nút …}; Môn thi [MonThi](chỉ đọc); Ngày kết thúc [NgayKT]{ngày}(chỉ đọc); Ngày thi dự kiến [NgayThiDuKien]{ngày}(chỉ đọc); SL trạm thi [SLTramMax]; Sĩ số đã đăng ký [SiSoDDK](chỉ đọc); Sỉ số [SiSoDuKien](chỉ đọc); Sĩ số tổ thi [SiSoToThi](chỉ đọc); Số tiết tổ thi [SoTiet]; Tên BM QL MH [TenBmQLMH](chỉ đọc); Tên hình thức thi [TenHTThi](chỉ đọc); Tên khoa quản lý bộ môn [TenKhoaBM](chỉ đọc); Tiết thi dự kiến [TietThiDuKien](chỉ đọc)
### LCAPNHATPHONGCopy – Nhập thời gian nộp điểm
- Lưới 1 «Danh sách tổ thi trong đợt thi» (bảng LToThi); tắt: Thêm, Xóa, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Nhóm thi [NhomThi](chỉ đọc); Tổ thi [ToThi](chỉ đọc); Số tiết [SoTiet](chỉ đọc); Số tiết thi [SoTietThi](chỉ đọc); Ngày thi [NgayThi]{ngày}(chỉ đọc); Tiết bắt đầu [TietThiBD](chỉ đọc); Mã phòng [MaPH]{nút …}(chỉ đọc); Phòng đợi [MaPHDoi]{nút …}(chỉ đọc); Ngày nộp điểm [NgayNopDiem]{ngày}; Mã hình thức thi [MaHTThi](chỉ đọc)
  - Cột ẩn: ID phòng thi [IDPThi](chỉ đọc); Loại đối tượng [LoaiDTuong](chỉ đọc); Mã đối tượng [MaDoiTuong](chỉ đọc); Mã tính chất phòng [MaTCPhong](chỉ đọc); Môn thi [MonThi](chỉ đọc); Ngày thi dự kiến [NgayThiDuKien]{ngày}(chỉ đọc); SL trạm tối đa [SLTramMax](chỉ đọc); Sỉ số [SiSoDuKien](chỉ đọc); Sĩ số tổ thi [SiSoToThi](chỉ đọc); Tiết thi dự kiến [TietThiDuKien](chỉ đọc)
### LCBTramThi – Nhập cán bộ trạm thi
- Lưới 1 «Nhập cán bộ trạm thi cho tổ thi» (bảng LCBTramThi); tắt: Thêm, Xóa, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm thi [NhomThi](chỉ đọc); Tổ thi [ToThi](chỉ đọc); Ngày thi [NgayThi]{ngày}(chỉ đọc); Tiết BĐ [TietThiBD](chỉ đọc); Mã phòng [MaPH]{nút …}(chỉ đọc); Thứ tự trạm [TTTram]; Mã viên chức [MaNV]{nút …}; Loại CB trạm [LoaiCBTramThi]{chọn}; Cấp CB trạm [CapCBTramThi]
  - Cột ẩn: Mã cán bộ giám sát [MaNVGiamSat](chỉ đọc); Mã cán bộ thư ký [MaNVThuKy](chỉ đọc); Sĩ số tổ thi [SiSoToThi](chỉ đọc); Tên đầy đủ [TenDayDuNV](chỉ đọc); Tên cán bộ giám sát [TenDayDuNVGiamSat](chỉ đọc); Tên cán bộ thư ký [TenDayDuNVThuKy](chỉ đọc)
### LDMLDInGiayVPT – Danh mục lý do in giấy vào phòng thi
- Lưới 1 «Danh mục lý do in giấy vào phòng thi» (bảng LDMLDInGiayVPT); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã lý do [MaLDInGiayVPT]; Tên lý do [TenLDInGiayVPT]; Viết tắt [VtLDInGiayVPT]
  - Cột ẩn: Ghi chú [GcLDInGiayVPT]; Tên tiếng anh [TenLDInGiayVPTEg]
  - Ô trên form sửa: #MaLDInGiayVPT, #TenLDInGiayVPT, #VtLDInGiayVPT, #GcLDInGiayVPT, #TenLDInGiayVPTEg
### LDmVPQCThi – Danh mục vi phạm quy chế thi
- Lưới 1 «Danh mục vi phạm quy chế thi» (bảng LDmVPQCThi); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã vi phạm [MaVPQCThi]; Tên vi phạm [TenVPQCThi]; Tên vi phạm (Eg) [TenVPQCThiEg]; Viết tắt [VtVPQCThi]; Ghi chú [GcVPQCThi]
  - Ô trên form sửa: #MaVPQCThi, #TenVPQCThi, #TenVPQCThiEg, #VtVPQCThi, #GcVPQCThi
### LKQDKDTHI – Đồng bộ danh sách thi
- Lưới 1 «Chỉ đồng bộ các nhóm thi chưa khóa + chưa phân tổ thi + chưa bị tách nhóm theo lớp + sv đang học hoặc tạm dừng. Nguồn dữ liệu: đăng ký môn học học kỳ + ghép hoãn thi + ghép cải thiện - rút môn học - đk hoãn thi»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Nhóm thi [NhomThi]; Sỉ số học [SiSoDDK]; Sỉ số dự thi đã đồng bộ [SoDuThi]; Sỉ số bị cấm thi [SLConLai]; Mã đợt thi [MaDotThi]
### LPHANCONGCHAMTHI – Cập nhật phòng thi
- Lưới 1 «Phân công chấm thi trên danh sách tổ thi đã xếp lịch thi» (bảng LToThi); tắt: Thêm, Xóa, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm thi [NhomThi](chỉ đọc); Tổ thi [ToThi](chỉ đọc); Sĩ số tổ thi [SiSoToThi](chỉ đọc); Ngày thi [NgayThi]{ngày}(chỉ đọc); Tiết bắt đầu [TietThiBD](chỉ đọc); Mã phòng [MaPH](chỉ đọc); Mã chấm thi [MaNV]{nút …}; Họ và tên chấm thi [TenDayDuNV](chỉ đọc)
### LPHANCONGCOITHI – Cập nhật phòng thi
- Lưới 1 «Phân công coi thi trên danh sách tổ thi đã xếp lịch thi» (bảng LDKCoiThi); tắt: Thêm, Xóa, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm thi [NhomThi](chỉ đọc); Tổ thi [ToThi](chỉ đọc); Sĩ số tổ thi [SiSoToThi](chỉ đọc); Ngày thi [NgayThi]{ngày}(chỉ đọc); Tiết BĐ [TietThiBD](chỉ đọc); Mã phòng [MaPH]{nút …}(chỉ đọc); SL coi thi [SLCanBoCoiThi](chỉ đọc); Mã CB coi thi 1 [MaNVCap1]{nút …}; Tên đầy đủ 1 [TenDayDuNVCap1](chỉ đọc); Mã CB coi thi 2 [MaNVCap2]{nút …}; Tên đầy đủ 2 [TenDayDuNVCap2](chỉ đọc); Mã CB coi thi 3 [MaNVCap3]{nút …}; Tên đầy đủ 3 [TenDayDuNVCap3](chỉ đọc)
### LTenGoiCaThi – Định nghĩa tên gọi ca thi
- Lưới 1 «Danh sách ca thi» (bảng LTenGoiCaThi); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Ca Thi [TenGoiCaThi]; Tiết bắt đầu ca [TietBDCa]; Số tiết ca thi [SoTietCa]; Niên học học kỳ [NHHK]
  - Cột ẩn: Tên gọi ca thi [IDTenGoiCaThi]
  - Ô trên form sửa: #TenGoiCaThi, #TietBDCa, #SoTietCa
### LTGNgoaiGio – Quy định thời gian ngoài giờ
- Lưới 1 «Danh sách thời gian Thứ - giờ bắt đầu tính là ngoài giờ» (bảng LTGNgoaiGio); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Danh sách thứ [DSThu]; Giờ bắt đầu [GioBDNgoaiGio]; Giờ kết thúc [GioKTNgoaiGio]
  - Ô trên form sửa: #DSThu, #GioBDNgoaiGio, #GioKTNgoaiGio
### LTHI_ViewKhoaNhomThi – View khoa nhom thi
- Lưới 1 «Danh sách nhóm thi» (bảng LNhomThi); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm/tổ [NhomTo](chỉ đọc); Sĩ số đã đăng ký [SiSoDDK](chỉ đọc); Điểm K1 [K1](chỉ đọc); Điểm C1 [C1](chỉ đọc); Nhóm thi [NhomThi](chỉ đọc); Tuần kết thúc [TuanktHoc](chỉ đọc); Ngày kết thúc [NgayKT]{ngày}; Ký hiệu ghép [GhepCaThi](chỉ đọc); KH điểm TP [KyHieuTP](chỉ đọc); Sĩ số tổ thi [SiSoToThi](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Mã hình thức thi [MaHTThi](chỉ đọc); Khóa [IsLock]
### LTHI_ViewNhapTGNhDi – Nhập thời gian nhập điểm thi
- Lưới 1 «Danh sách nhóm thi» (bảng LToThi); tắt: Thêm, Xóa, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Nhóm thi [NhomThi](chỉ đọc); Tổ thi [ToThi](chỉ đọc); Số tiết [SoTiet](chỉ đọc); Số tiết thi [SoTietThi](chỉ đọc); Ngày thi [NgayThi]{ngày}(chỉ đọc); Tiết bắt đầu [TietThiBD](chỉ đọc); Mã phòng [MaPH]{nút …}(chỉ đọc); Phòng đợi [MaPHDoi]{nút …}(chỉ đọc); Mã hình thức thi [MaHTThi](chỉ đọc); Ngày bắt đầu nhập điểm [NgayBDNhapDiem]{ngày}; Ngày kết thúc nhập điểm [NgayKTNhapDiem]{ngày}
### LThuLaoCoiThi – Định mức thù lao coi thi
- Lưới 1 «Danh sách định mức thù lao coi thi» (bảng LThuLaoCoiThi); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số phút thi [SoPhutThi]; Thù lao trong giờ [ThuLaoTrongGio]; Thù lao ngoài giờ [ThuLaoNgoaiGio]
  - Ô trên form sửa: #SoPhutThi, #ThuLaoTrongGio, #ThuLaoNgoaiGio
### M10.13 – Môn chỉ được phép chọn 1 khi đăng ký
- Lưới 1 «Môn chỉ được phép chọn 1 khi đăng ký» (bảng MMHC1DK); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]
  - Cột ẩn: Môn học [IDMH]
  - Ô trên form sửa: #TenMH, #SoTinChi, #IDMH
### MAPPFILEIMPORT – Danh sách các cột đã sánh đôi
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Sửa bên phải
### MBODEM – Dinh nghia bo dem
- Lưới 1 «Định nghĩa bộ đếm phiếu thu»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Loại phiếu thu [LoaiPThu]{chọn}(chỉ đọc); Bộ đếm toàn trường [BoDemToanTruong]{số}; Bộ đếm user [BoDemUser]{số}; Tiếp đầu ngữ [TiepDauNgu]; Tiếp vị ngữ [TiepViNgu]
### MKHOAMOPTHUHK – Khóa/mở phiếu thu theo học kỳ
- Lưới 1 «Danh sách năm học học kỳ»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Ngày khóa [NgayLockHK]{ngày}; Ghi chú [GCLockHK]
### MMHHT – danh muc mon hoc truoc
- Lưới 1 «Danh mục môn học học trước» (bảng MMHTQ); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Mã khối [MaKhoi]; Mã Ng/CNg [MaNgChng]; Mã bậc hệ [MaBH]; Ký hiệu OR [KhtqOR]
  - Cột ẩn: Ghi chú [GhiChu]; Bậc hệ [IDBH]; Mã khối [IDKhoi]; Môn học [IDMH]; Ngành [IDNgChNg]
  - Ô trên form sửa: #TenMH, #KhtqOR, #GhiChu, #IDBH, #IDKhoi, #IDMH, #IDNgChNg
  - Nút btnAdd: "them" (F1)
  - Nút btnDelete: "Xoa" (F2)
  - Nút btnPrint: "in" (F4)
  - Nút btnSave: "save" (F3)
### MMHSH – Danh muc mon hoc song hanh
- Lưới 1 «Danh sách môn học song hành» (bảng MMHTQ); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Mã khối [MaKhoi]; Mã bậc hệ [MaBH]; Mã Ng/CNg [MaNgChng]; Ký hiệu OR [KhtqOR]; Ghi chú [GhiChu]
  - Cột ẩn: Bậc hệ [IDBH]; Mã khối [IDKhoi]; Môn học [IDMH]; Ngành [IDNgChNg]
  - Ô trên form sửa: #TenMH, #KhtqOR, #GhiChu, #IDBH, #IDKhoi, #IDMH, #IDNgChNg
  - Nút btnPrint: "in" (F4)
  - Nút btnAdd: "them" (F2)
  - Nút btnDelete: "xoa" (F3)
  - Nút btnSave: "save" (F1)
### MMHTQ – Mon hoc tien quyet
- Lưới 1 «Danh mục môn học tiên quyết» (bảng MMHTQ); tắt: Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Mã bậc hệ [MaBH]; Mã Ng/CNg [MaNgChng]; Mã khối [MaKhoi]; Ký hiệu OR [KhtqOR]; Ghi chú [GhiChu]; Mã khối [IDKhoi]
  - Cột ẩn: Bậc hệ [IDBH]; Môn học [IDMH]{nút …}; Ngành [IDNgChNg]
  - Ô trên form sửa: #TenMH, #KhtqOR, #GhiChu, #IDKhoi, #IDBH, #IDMH, #IDNgChNg
  - Nút btnPrint: "In" (F4)
  - Nút btnAdd: "them" (F2)
  - Nút btnDelete: "Xoa" (F3)
### MONTQ – View xem danh sách môn học TQ/HT/SH
- Lưới 1 «Danh sách môn học tiên quyết - học trước - song hành» (bảng MMONTQ); tắt: Thêm, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã bậc hệ [MaBH]{nút …}; Nhóm tiên quyết [NhomTQ]; Mã Ng/CNg [MaNgChng]{nút …}; Mã khối [MaKhoi]{nút …}; Niên khóa [NienKhoaSV]; Mã môn học [MaMH]{nút …}; Tên môn học [TenMH](chỉ đọc); Mã mhtq [MaMHTQ]{nút …}; Tên mh tiên quyết [TenMHTQ](chỉ đọc); Loại tiên quyết [LoaiTQ]{chọn}; Điểm chữ tối thiểu [DiemChuMin]; Ký hiệu Or [KyHieuOr]; Nhánh điều kiện [NhanhDKTQ]; Ngày thêm [NgayThem]{ngày}(chỉ đọc)
### MPThuHB – Danh sách hóa đơn học bổng
- Lưới 1 «Danh sách hóa đơn học bổng» (bảng MPThuHB); tắt: In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Mã lớp [MaLop]; Số chứng từ [SoCTu]; Ngày thu/chi [NgayTChi]{ngày}; Số tiền [SoTien]{số}; Thu ngân hàng [THUNH]; Ghi chú [GHICHUPT]
  - Cột ẩn: Sinh viên [IDSV]{nút …}
  - Ô trên form sửa: #HoLotSV, #TenSV, #MaLop, #SoCTu, #NgayTChi, #SoTien, #THUNH, #GHICHUPT, #IDSV
### MRBKHAC – MRBKHAC
- Lưới 1 «Danh mục ràng buộc khác» (bảng MRBKHAC); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã ràng buộc khác [MaRBKhac]; Tên ràng buộc khác [TenRBKhac]; Viết tắt ràng buộc khác [VtRBKhac]
  - Cột ẩn: Ghi chú ràng buộc khác [GcRBKhac]; Tên tiếng anh [TenRBKhacEg]
  - Ô trên form sửa: #MaRBKhac, #TenRBKhac, #VtRBKhac, #GcRBKhac, #TenRBKhacEg
### N_DSQDNV – Danh sách quyết định một nhân viên
- Lưới 1 «Danh sách quyết định của nhân viên» (bảng NDSQDVR); tắt: Thêm, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Trạng thái [HienDienNV]{chọn}; Số quyết định [SoQDVR]; Tên quyết định [TenQDVR]; Lý do quyết định [IDLDQDNV]; Ngày lập [NgayLapQDVR]{ngày}; Loại quyết định [LoaiLDQDNS]{chọn}; Lý do [LyDoVRCT]
  - Ô trên form sửa: #NHHK, #HienDienNV, #SoQDVR, #TenQDVR, #IDLDQDNV, #NgayLapQDVR, #LoaiLDQDNS
### NCKH_ViewCapNhatDeTaiDuThuong – View cập nhật đề tài dự thưởng
- Lưới 1 (bảng ODeTaiNCKH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đề tài [MaDeTaiNCKH]; Tên đề tài [TenDeTaiNCKH]; Ngày bắt đầu [NgayBDDeTai]; Số tháng thực hiện [SoThangDeTai]; Niên học học kỳ [NHHK]; Ngày quyết định cấp giấy chứng nhận [NgayQDCapGiayChungNhan]
### NDMBenhVien – Danh mục bệnh viện
- Lưới 1 «Danh mục bệnh viện» (bảng NDMBENHVIEN); tắt: Sửa trên lưới
  - Cột: Mã Bệnh viện [MABENHVIEN]; Tên Bệnh viện [TENBENHVIEN]; Viết tắt Bệnh viện [VtBenhVien]
  - Cột ẩn: Ghi chú Bệnh viện [GcBenhVien]; Tên tiếng anh [TENBENHVIENEG]
  - Ô trên form sửa: #MABENHVIEN, #TENBENHVIEN, #VtBenhVien, #GcBenhVien, #TENBENHVIENEG
### NDMDT – Danh mục dân tộc
- Lưới 1 «Danh mục dân tộc» (bảng NDMDT); tắt: Sửa trên lưới
  - Cột: Mã dân tộc [MaDT]; Tên dân tộc [TenDT]; Tên viết tắt [VTDT]
  - Cột ẩn: Đối tượng mặc định [DFDT]; Ghi chú [GCDT]; Không quản lý [HuyDT]; Tên tiếng anh [TenDTEg]
  - Ô trên form sửa: #MaDT, #TenDT, #VTDT, #DFDT, #GCDT, #TenDTEg
### NDMDV – Danh mục đơn vị
- Lưới 1 «Danh sách đơn vị» (bảng NDMDV); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã đơn vị [MaDV]; Tên đơn vị [TenDV]; Thứ tự [TTDV]; Số QĐ thành lập [SoQDTLDV]; Ngày thành lập [NgayQDTLDV]; Đã giải thể [HuyDV]
  - Cột ẩn: Địa chỉ [DiaChiDV]; Điện thoại [DienThoaiDV]; Email [EmailDV]; Ghi chú [GcDV]; Đơn vị cấp trên [IDDVP]; Hình lý do QĐ thành lập [ImageQDTLDV]; Loại đơn vị [LoaiDV]{chọn}; Chức năng thành lập [LyDoThanhLap]; Chức năng nhiệm vụ [NhiemVu]; Tên tiếng anh [TenDVEg]; Tên đơn vị VB [TenDVVB]; Tên tiếng anh [TenDVVBEg]; Tên viết tắt [VtDV]
  - Ô trên form sửa: #MaDV, #TenDV, #TTDV, #SoQDTLDV, #NgayQDTLDV, #DiaChiDV, #DienThoaiDV, #EmailDV, #GcDV, #IDDVP, #ImageQDTLDV, #LoaiDV, #LyDoThanhLap, #NhiemVu, #TenDVEg, #TenDVVB, #VtDV
### NDMDV_Tree_Chon – Chọn đơn vị dạng tree
- Lưới 1 (bảng NDMDV); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đơn vị [MaDV]; Tên đơn vị [TenDV]; Thứ tự [TTDV]
  - Cột ẩn: Địa chỉ [DiaChiDV]; Điện thoại [DienThoaiDV]; Email [EmailDV]; Ghi chú [GcDV]; Đã giải thể [HuyDV]; Đơn vị cấp trên [IDDVP]; Loại đơn vị [LoaiDV]{chọn}; Tên đơn vị VB [TenDVVB]; Tên viết tắt [VtDV]
  - Ô trên form sửa: #MaDV, #TenDV, #TTDV, #DiaChiDV, #DienThoaiDV, #EmailDV, #HuyDV, #IDDVP, #LoaiDV, #TenDVVB, #VtDV
### NDMDVTINH – Danh mục đơn vị tính
- Lưới 1 «Danh sách đơn vị tính» (bảng NDMDVTinh); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã Đơn vị tính [MaDVTinh]; Tên Đơn vị tính [TenDVTinh]; Viết tắt [VtDVTinh]; Ghi chú [GcDVTinh]
  - Cột ẩn: Mặc định [DfDVTinh]; Không quản lý [HuyDVTinh]; Tên tiếng anh [TenDVTinhEg]
  - Ô trên form sửa: #MaDVTinh, #TenDVTinh, #VtDVTinh, #GcDVTinh, #TenDVTinhEg
### NDMKHOAHOC – Danh mục khóa đào tạo
- Lưới 1 «Danh mục khóa học đào tạo» (bảng NDMKhoaHoc); tắt: Sửa trên lưới
  - Cột: Mã khóa học [MaKhoaHoc]; Tên khóa học [TenKhoaHoc]; Viết tắt [VtKhoaHoc]
  - Cột ẩn: Ghi chú [GCKhoaHoc]; Tên tiếng anh [TenKhoaHocEg]
  - Ô trên form sửa: #MaKhoaHoc, #TenKhoaHoc, #VtKhoaHoc, #GCKhoaHoc, #TenKhoaHocEg
### NDMLDKgLKK – Danh mục lý do không hưởng lương khuyến khích
- Lưới 1 «Danh sách lý do không hưởng lương khuyến khích» (bảng NDMLDKgLKK); tắt: Sửa trên lưới
  - Cột: Mã lý do không hưởng lương [MaLDKgLKK]; Tên lý do không hưởng lương [TenLDKgLKK]
  - Cột ẩn: Ghi chú lý do không hưởng lương [GcLDKgLKK]; Tên lý do không hưởng lương Eg [TenLDKgLKKEg]; Viết tắt LDKgLKK [VtLDKgLKK]
  - Ô trên form sửa: #MaLDKgLKK, #TenLDKgLKK
### NDMLLL – Danh mục loại hình lên lương
- Lưới 1 «Danh mục loại lên lương» (bảng NDMLLL); tắt: Thêm, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã loại lên lương [MaLLL]; Tên loại lên lương [TenLLL]; Đổi nhóm ngạch [DoiNhNgach]; Đổi ngạch [DoiNgach]; Đổi bậc [DoiBac]
  - Cột ẩn: Ghi chú [GCLLL]; Mã file word mẫu [IDTmpWord]; Tên tiếng anh [TenLLLEg]; Tên viết tắt [VtLLL]; Xem file [XemFile]
  - Ô trên form sửa: #MaLLL, #TenLLL, #IDTmpWord, #XemFile
### NDMNH – Danh mục ngân hàng
- Lưới 1 «Danh sách ngân hàng» (bảng NDMNH); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã ngân hàng [MaNH]; Tên ngân hàng [TenNH]; Tên viết tắt [VTNH]; Terminal Code [TerminalCode]
  - Cột ẩn: Ghi chú [GCNH]; Không quản lý [HuyNH]
  - Ô trên form sửa: #MaNH, #TenNH, #VTNH, #TerminalCode, #GCNH, #HuyNH
### NDMNSVL – Danh mục nhân viên vãng lai
- Lưới 1 «Danh sách nhân viên vãng lai» (bảng NDMNSVL); tắt: Xóa, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã nhân sự vãng lai [MaNSVL]; Họ lót nhân sự [HoLotNSVL]; Tên nhân sự [TenNSVL]; Phái [PhaiNSVL]{chọn}; Ngày sinh [NgaySinhCNSVL]; Số CMND/hộ chiếu [SoCMNSVL]; Điện thoại [DienThoaiNSVL]
  - Cột ẩn: Mã địa bàn [DC_IDDCNSVL]; Địa chỉ [DiaChiNSVL]; Tên đầy đủ nhân sự [TenDayDuNSVL]
  - Ô trên form sửa: #MaNSVL, #HoLotNSVL, #TenNSVL, #PhaiNSVL, #NgaySinhCNSVL, #SoCMNSVL, #DienThoaiNSVL, #DC_IDDCNSVL, #DiaChiNSVL, #TenDayDuNSVL
### NDMNV – Danh mục nhân viên
- Lưới 1 «Danh mục cán bộ nhân viên» (bảng NDMNV); tắt: Sửa trên lưới
  - Cột: Nội dung minh chứng [NoiDungMC]; Tên đơn vị [TenDV]; Mã viên chức [MaNV]; Họ lót [HoLotNV]; Tên nhân viên [TenNV]; Ngày sinh [NgSinhNVCNV]; Phái [PhaiNV]{chọn}; Trạng thái [HienDienNV]{chọn}; Loại nhân viên [LoaiNhanVien]{chọn}; Tên ngành [TenNganh]; Tình trạng hôn nhân [TTHonNhan]{chọn}; Tên trình độ [TenBacNV]; Năm vào đoàn [NamDoan]; Số thẻ đoàn [SoDoan]; Nơi kết nạp đoàn [NoiDoan]; Năm vào ngành [NamVaoNganh]; Ngày về trường [NgayVeTruong]; Ngày tham gia công tác [NgayCongTac]; Số thẻ đảng [SoDang]; Nơi kết nạp [NoiDang]; Ngày CNCT Đảng [NgayGCNDang]; Số CNCT Đảng [GCNDang]; Ngày chính thức [NamDangCT]; Ngân hàng [TenNH]; Số tài khoản [SoTK]; Dân tộc [TenDT]; Tôn giáo [TenTG]; Số sổ LĐ [SoSLD]; Số bảo hiểm [SoSBH]; Ngày cấp SBH [NgCapSBH]; Nơi cấp SBH [NoiCapSBH]; Đã có SBH [CoSBH]; Số thẻ tạm trú [SoTamTru]; Số khám sức khỏe [SoKSK]; Loại sức khỏe [LoaiKSK]; Nhóm máu [NhomMau]; Số CMND [SoCMNDNV]; Ngày cấp CMND [NgayCapCMNDNV]; Nơi cấp CMND [NoiCapCMNDNV]; Quê quán [QueQuanNV]; Chiều cao [ChieuCao]; Email [DC_Eml1LLNV]; Nơi sinh [NoiSinhNV]; Ngày cấp tiến sĩ [NgayTSi]; SL Th.Si hướng dẫn [SLThSiHD]; SL sách viết [SLSachViet]; Cân nặng [CanNang]; SL đề tài cấp bộ [SLDTBo]; SL đề tài cấp cơ sở [SLDTCoSo]; Ngày cấp PGS [NgayPGS]; SL TSi hướng dẫn [SLTSiHD]; SL sách viết (sau PGS) [SLSachViet1]; SL đề tài cấp bộ(sau PGS) [SLDTBo1]; SL đề tài cấp cơ sở(sau PGS) [SLDTCoSo1]; Mã đơn vị [MaDV]; Viên chức ngoài trường [IsNVNgoai]; Thứ tự [TTNV]
  - Cột ẩn: Hình nhân viên [AvatarNV]; Bí danh [BiDanh]; Địa chỉ liên lạc [DC_DCLLNV]; Số điện thoại [DC_DT1LLNV]; Ghi chú [GCNV]; Không quản lý [HUYNV]; Họ lót [HoLotNV2]; Trình độ [IDBacNV]; Dân tộc [IDDT]; Đơn vị [IDDV]; Nhóm CB-GV-NV [IDLoaiDTCBGD]; Ngân hàng [IDNH]; Ngành [IDNgChNg]; Ngành [IDNganhNV]; PL giảng viên [IDPLGV]; Quốc tịch [IDQuocTich]; Tôn giáo [IDTG]; Thỉnh giảng [IsThinhGiang]; Mã phân loại GV [MaPLGV]; Tên đầy đủ [TenDayDuNV]; Tên nhân viên [TenNV2]; Tên phân loại GV [TenPLGV]; Tỉnh cấp CMND [TinhCapCMNDNV]; Tên viết tắt [VTNV]
  - Ô trên form sửa: #NoiDungMC, #MaNV, #HoLotNV, #TenNV, #NgSinhNVCNV, #PhaiNV, #HienDienNV, #LoaiNhanVien, #SoCMNDNV, #DC_Eml1LLNV, #NoiSinhNV, #IsNVNgoai, #TTNV, #AvatarNV, #DC_DCLLNV, #DC_DT1LLNV, #GCNV, #IDBacNV, #IDDV, #IDNganhNV, #IsThinhGiang, #TenDayDuNV
### NDMNV_IN – Danh mục nhân viên
- Lưới 1 «Chọn viên chức» (bảng NDMNV); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Họ lót [HoLotNV]; Tên nhân viên [TenNV]; Ngày sinh [NgSinhNVCNV]; Phái [PhaiNV]{chọn}; Trạng thái [HienDienNV]{chọn}; Mã đơn vị [MaDV]; Tên đơn vị [TenDV]
  - Ô trên form sửa: #MaNV, #HoLotNV, #TenNV, #NgSinhNVCNV, #PhaiNV
### NDMNV_InBaoHiem – Danh mục nhân viên
- Lưới 1 «Chọn viên chức cần in» (bảng NDMNV); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Phái [PhaiNV]{chọn}; Ngày sinh [NgSinhNVCNV]; Số bảo hiểm [SoSBH]; BVKCBBD [BVKCBBD]; Số CMND [SoCMNDNV]
  - Ô trên form sửa: #MaNV, #TenDayDuNV, #PhaiNV, #NgSinhNVCNV
### NDMNV_QLLUONG – Danh mục nhân viên
- Lưới 1 «Danh sách viên chức» (bảng NDMNV); tắt: Import, Xuất, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Đơn vị [TenKhoaNV]; Họ lót [HoLotNV]; Tên nhân viên [TenNV]; Trạng thái [HienDienNV]{chọn}; Chức vụ [TenChucVu]; Học hàm [TenHocHam]; Ngày sinh [NgSinhNVCNV]; Phái [PhaiNV]{chọn}; Tình trạng hôn nhân [TTHonNhan]{chọn}; Tên ngành [TenNganh]; Năm vào đoàn [NamDoan]; Số thẻ đoàn [SoDoan]; Tên trình độ [TenBacNV]; Nơi kết nạp đoàn [NoiDoan]; Năm vào ngành [NamVaoNganh]; Ngày về trường [NgayVeTruong]; Ngày tham gia công tác [NgayCongTac]; Số thẻ đảng [SoDang]; Nơi kết nạp [NoiDang]; Số CNCT Đảng [GCNDang]; Ngày CNCT Đảng [NgayGCNDang]; Ngày chính thức [NamDangCT]; Số tài khoản [SoTK]; Số bảo hiểm [SoSBH]; Tên ngân hàng [TenNH]; Số sổ LĐ [SoSLD]; Số thẻ tạm trú [SoTamTru]; Số khám sức khỏe [SoKSK]; Loại sức khỏe [LoaiKSK]; Nhóm máu [NhomMau]; Tên dân tộc [TenDT]; Số CMND [SoCMNDNV]; Quê quán [QueQuanNV]; Tên tôn giáo [TenTG]; Email [DC_Eml1LLNV]; Nơi sinh [NoiSinhNV]; Thứ tự [TTDV]; Thứ tự [TTChucVu]
  - Cột ẩn: Hình nhân viên [AvatarNV]; Bí danh [BiDanh]; Cân nặng [CanNang]; Chiều cao [ChieuCao]; Ghi chú [GCNV]; Không quản lý [HUYNV]; Họ lót [HoLotNV2]; Dân tộc [IDDT]; Đơn vị [IDDV]; Ngành [IDNgChNg]; Quốc tịch [IDQuocTich]; Tôn giáo [IDTG]; Mã bộ môn [MaBMNV]; Mã chức vụ [MaChucVu]; Mã học hàm [MaHocHam]; Mã khoa [MaKhoaNV]; Ngày cấp PGS [NgayPGS]; Ngày cấp tiến sĩ [NgayTSi]; SL đề tài cấp bộ [SLDTBo]; SL đề tài cấp bộ(sau PGS) [SLDTBo1]; SL đề tài cấp cơ sở [SLDTCoSo]; SL đề tài cấp cơ sở(sau PGS) [SLDTCoSo1]; SL sách viết [SLSachViet]; SL sách viết (sau PGS) [SLSachViet1]; SL TSi hướng dẫn [SLTSiHD]; SL Th.Si hướng dẫn [SLThSiHD]; Thứ tự [TTNV]; Tên đầy đủ [TenDayDuNV]; Tên nhân viên [TenNV2]; Tên viết tắt [VTNV]
  - Ô trên form sửa: #MaNV, #HoLotNV, #TenNV, #NgSinhNVCNV, #PhaiNV, #NgayVeTruong, #NoiSinhNV, #AvatarNV, #GCNV, #IDDV, #TTNV, #TenDayDuNV
### NDMNV_TROCAPDV – Danh mục nhân viên
- Lưới 1 «Danh sách viên chức được trợ cấp theo đơn vị» (bảng NDMNV); tắt: Thêm, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Tên đơn vị [TenDV]; Họ lót [HoLotNV](chỉ đọc); Tên nhân viên [TenNV](chỉ đọc); Trạng thái [HienDienNV]{chọn}(chỉ đọc); Ngày sinh [NgSinhNVCNV](chỉ đọc); Có hưởng trợ cấp đơn vị [CoTroCapDV]
  - Ô trên form sửa: #MaNV, #HoLotNV, #TenNV, #CoTroCapDV
### NDMPLBacNV – Danh mục phân loại trình độ - học vị
- Lưới 1 «Danh mục phân loại bậc» (bảng NDMPLBacNV); tắt: Sửa trên lưới
  - Cột: Thứ tự [TTPLBacNV]; Mã phân loại [MaPLBacNV]; Tên phân loại [TenPLBacNV]
  - Cột ẩn: Ghi chú [GcPLBacNV]; Tên tiếng anh [TenPLBacNVEg]; Tên viết tắt [VtPLBacNV]
  - Ô trên form sửa: #TTPLBacNV, #MaPLBacNV, #TenPLBacNV, #GcPLBacNV, #TenPLBacNVEg, #VtPLBacNV
### NDMPLNgach – Danh mục phân loại ngạch
- Lưới 1 «Danh sách phân loại ngạch» (bảng NDMPLNgach); tắt: Sửa trên lưới
  - Cột: Thứ tự [TTPLNgach]; Mã phân loại ngạch [MaPLNgach]; Tên phân loại ngạch [TenPLNgach]
  - Cột ẩn: Ghi chú phân loại ngạch [GcPLNgach]; Tên tiếng anh [TenPLNgachEg]; Viết tắt phân loại ngạch [VtPLNgach]
  - Ô trên form sửa: #TTPLNgach, #MaPLNgach, #TenPLNgach, #GcPLNgach, #TenPLNgachEg, #VtPLNgach
### NDMPLNV – Danh mục phân loại nghiệp vụ
- Lưới 1 «Danh mục phân loại nghiệp vụ» (bảng NDMPLNV); tắt: Sửa trên lưới
  - Cột: Mã nghiệp vụ [MaPLNV]; Tên nghiệp vụ [TenPLNV]; Tên viết tắt [VtPLNV]
  - Cột ẩn: Ghi chú [GcPLNV]; Không quản lý [HuyPLNV]; Thứ tự PLNV [TTPLNV]; Tên tiếng anh [TenPLNVEg]
  - Ô trên form sửa: #MaPLNV, #TenPLNV, #VtPLNV, #GcPLNV, #HuyPLNV, #TTPLNV, #TenPLNVEg
### NLapQDDSThamNienLamViec – Lập quyết định danh sách cán bộ thâm niên làm việc
- Lưới 1 «Danh sách quyết định nâng phụ cấp thâm niên làm việc» (bảng NDSCBNPCTNLamViec); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã viên chức [MaNV](chỉ đọc); Tên đầy đủ [TenDayDuNV](chỉ đọc); Mốc nâng quyết định cũ [MocNangQDTNLamViecCu]{ngày}(chỉ đọc); Mức phụ cấp cũ [MucPCTNLamViecCu](chỉ đọc); Mốc nâng quyết định  mới [MocNangQDTNLamViecMoi]{ngày}; Mức phụ cấp mới [MucPCTNLamViecMoi](chỉ đọc); Số quyết định [SoQDTNLamViec]; Ngày quyết định [NgayQDTNLamViec]{ngày}; Ngày hiệu lực [NgayHLQDTNLamViec]{ngày}
  - Cột ẩn: IDNDSCBNPCTNLamViec [IDNDSCBNPCTNLamViec]; Mã viên chức [IDNV]; ID phụ cấp thâm niên làm việc [IDQTPCTNLamViec]
### NNKTINHLUONG – Nhật ký thực hiện tính lương
- Lưới 1 «Danh sách nhật ký tính lương» (bảng NNKTinhLuong); tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã user tính lương [MaUserTT]; Năm [Nam]{số}; Ngày tính lương [NgayDeNghiTT]; Tháng [Thang]{số}
### NQTPLGV – Quá trình phân loại giảng viên
- Lưới 1 «Danh sách phân loại giảng viên» (bảng NQTPLGV); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Phân loại giảng viên [IDPLGVMoi]; % PC mới [PCGVMoi]; Phân loại giảng viên [IDPLGVCu]; % PC cũ [PCGVCu]; Ngày hiệu lực [NgayHLPLGV]{ngày}; Ngày quyết định [NgayQDNS]{ngày}; Số quyết định [SoQDNS]; Hình quyết định phân loại giảng viên [ImageQTPLGV]
  - Cột ẩn: Mã viên chức [IDNV]
  - Ô trên form sửa: #TenDayDuNV, #IDPLGVMoi, #PCGVMoi, #IDPLGVCu, #PCGVCu, #NgayHLPLGV, #NgayQDNS, #SoQDNS, #ImageQTPLGV, #IDNV
### NQTPLGV_DHQT – Quá trình phân loại giảng viên
- Lưới 1 «Danh sách quyết định phân loại giảng viên viên chức» (bảng NQTPLGV); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Phân loại giảng viên [IDPLGVMoi]; % PC mới [PCGVMoi]; Ngày hiệu lực [NgayHLPLGV]{ngày}; Ngày quyết định [NgayQDNS]{ngày}; Số quyết định [SoQDNS]; Phân loại giảng viên [IDPLGVCu]; % PC cũ [PCGVCu]
  - Cột ẩn: Mã viên chức [IDNV]
  - Ô trên form sửa: #TenDayDuNV, #IDPLGVMoi, #PCGVMoi, #NgayHLPLGV, #NgayQDNS, #SoQDNS, #IDPLGVCu, #PCGVCu, #IDNV
### NTLHDLV – Truy lãnh lương khi thay đổi loại hợp đồng
- Lưới 1 «Danh sách truy lãnh lương khi thay đổi loại hợp đồng» (bảng NTLHDLV); tắt: Thêm, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Năm truy lãnh [NAMTL]{số}; Mã viên chức [MaNV]; Tháng truy lãnh [ThangTL]; Tên đầy đủ [TenDayDuNV]; Tên đơn vị [TenDV]; Số tháng truy lãnh [SoThangTL]; % lương chênh lệch [PTLuongChLch]
  - Ô trên form sửa: #NAMTL, #MaNV, #ThangTL, #TenDayDuNV, #TenDV, #SoThangTL
### NTLPCCV – Truy lãnh khi thay đổi chức vụ
- Lưới 1 «Danh sách truy lãnh khi thay đổi chức vụ» (bảng NTLPCCV); tắt: Thêm, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Năm truy lãnh [NAMTL]{số}; Tên đầy đủ [TenDayDuNV]; Tháng truy lãnh [ThangTL]; Tên đơn vị [TenDV]; Số tháng truy lãnh [SoThangTL]; Số ngày được truy lãnh [SoNgayTL]; PCCV chênh lệch [PCCVChLch]
  - Ô trên form sửa: #MaNV, #NAMTL, #TenDayDuNV, #ThangTL, #TenDV, #SoThangTL, #SoNgayTL
### NTLPCTNNG – Truy lãnh khi thay đổi phụ cấp thâm niên nhà giáo
- Lưới 1 «Danh sách truy lãnh khi thay đổi phụ cấp thâm niên nhà giáo» (bảng NTLPCTNNG); tắt: Thêm, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Năm truy lãnh [NAMTL]{số}; Tên đầy đủ [TenDayDuNV]; Tháng truy lãnh [ThangTL]; Tên đơn vị [TenDV]; Số tháng truy lãnh [SoThangTL]; Số ngày được truy lãnh [SoNgayTL]; % PCTNNG cũ [MucPCTNNGCu]; % PCTNNG mới [MucPCTNNGMoi]; Chênh lệch [MucPCTNNGChLch]
  - Ô trên form sửa: #MaNV, #NAMTL, #TenDayDuNV, #ThangTL, #TenDV, #SoThangTL, #SoNgayTL
### NTLPLGV – Truy lãnh khi thay đổi mức phụ cấp giảng viên
- Lưới 1 «Danh sách truy lãnh khi thay đổi mức phụ cấp giảng viên» (bảng NTLPLGV); tắt: Thêm, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Năm truy lãnh [NAMTL]{số}; Tên đầy đủ [TenDayDuNV]; Tháng truy lãnh [ThangTL]; Tên đơn vị [TenDV]; Số tháng truy lãnh [SoThangTL]; % PC cũ [PCGVCu]; % PC mới [PCGVMoi]; % PC chênh lệch [PCGVChLch]
  - Ô trên form sửa: #MaNV, #NAMTL, #TenDayDuNV, #ThangTL, #TenDV, #SoThangTL
### ODMCVHDXT – Danh mục chức vụ hội đồng xét thưởng
- Lưới 1 «Danh sách chức vụ» (bảng ODMCVHDXT); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã chức vụ xét thưởng [MaCVHDXT]; Tên chức vụ xét thưởng [TenCVHDXT]
  - Cột ẩn: Ghi chú [GcCVHDXT]; Tên tiếng anh [TenCVHDXTEg]; Viết tắt [VtCVHDXT]
  - Ô trên form sửa: #MaCVHDXT, #TenCVHDXT, #GcCVHDXT
### ODMHDXetGiaiThuongNCKH1 – Danh mục hội đồng xét giải thường
- Lưới 1 «Danh sách hội đồng» (bảng ODMHDXetGiaiThuongNCKH); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã [MaDMHDXetGiaiThuongNCKH]; Tên [TenDMHDXetGiaiThuongNCKH]; Viết tắt [VtDMHDXetGiaiThuongNCKH]; Ghi chú 1 [GhiChu1]
  - Cột ẩn: Ghi chú [GcDMHDXetGiaiThuongNCKH]; Tên tiếng anh [TenDMHDXetGiaiThuongNCKHEg]
  - Ô trên form sửa: #MaDMHDXetGiaiThuongNCKH, #TenDMHDXetGiaiThuongNCKH, #VtDMHDXetGiaiThuongNCKH, #GhiChu1, #GcDMHDXetGiaiThuongNCKH, #TenDMHDXetGiaiThuongNCKHEg
### ODMMaPLBaiBao – Danh mục mã phân loại bài báo
- Lưới 1 «Danh sách mã phân loại bài báo» (bảng ODMMaPLBaiBao); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã PL bài báo [MaPLBaiBao]; Tên PL bài báo [TenPLBaiBao]; Viết tắt PL bài báo [VtPLBaiBao]
  - Cột ẩn: Ghi chú PL bài báo [GcPLBaiBao]; Tên PL bài báo Eg [TenPLBaiBaoEg]
  - Ô trên form sửa: #GcPLBaiBao, #MaPLBaiBao, #TenPLBaiBao, #TenPLBaiBaoEg, #VtPLBaiBao
### ODMPhanLoaiDeTaiNCKH – Danh mục phân loại đề tài
- Lưới 1 «Danh sách loại đề tài» (bảng ODMPhanLoaiDeTaiNCKH); tắt: Sửa trên lưới
  - Cột: Mã phân loại đề tài [MaPhanLoaiDeTaiNCKH]; Tên loại đề tài [TenPhanLoaiDeTaiNCKH]
  - Ô trên form sửa: #MaPhanLoaiDeTaiNCKH, #TenPhanLoaiDeTaiNCKH
### ODMPLSach – Danh mục phân loại sách
- Lưới 1 «Danh sách phân loại sách» (bảng ODMPLSach); tắt: Sửa trên lưới
  - Cột: Mã Phân loại sách [MaPLSach]; Tên Phân loại sách [TenPLSach]; Số giờ chủ biên [SoGioChuBien]{số}; Số giờ trên một trang tác giả [SoGioMoiTrang]{số}; Số lượng năm được tính giờ [SoNamTinhGio]{số}; Hệ số tiếng nước ngoài [HeSoTiengNN]; Không nhập online [IsKgOnline]
  - Cột ẩn: Ghi chú Phân loại sách [GcPLSach]; Tên Phân loại sách Eg [TenPLSachEg]; Viết tắt Phân loại sách [VtPLSach]
  - Ô trên form sửa: #MaPLSach, #TenPLSach, #SoGioChuBien, #SoGioMoiTrang, #SoNamTinhGio, #HeSoTiengNN, #IsKgOnline, #GcPLSach
### ODMPLSach_TDDM – Danh mục phân loại sách
- Lưới 1 «Danh sách phân loại sách» (bảng ODMPLSach); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã Phân loại sách [MaPLSach]; Tên Phân loại sách [TenPLSach]; Số điểm chủ biên [HSGioGiangTGChinh]; Số điểm tác giả các chương [HSGioGiangTGPhu]
  - Ô trên form sửa: #MaPLSach, #TenPLSach, #HSGioGiangTGChinh, #HSGioGiangTGPhu
### ODSNamNCKH – Định nghĩa năm tính khối lượng
- Lưới 1 «Danh sách năm tính khối lượng» (bảng ODSNamNCKH); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Năm thực hiện [NamNCKH]; Ngày bắt đầu năm tài chính [NgayBDNamTaiChinh]{ngày}; Ngày kết thúc năm tài chính [NgayKTNamTaiChinh]{ngày}; Ngày bắt đầu năm học [NgayBDNamHoc]{ngày}; Ngày kết thúc năm học [NgayKTNamHoc]{ngày}
  - Ô trên form sửa: #NamNCKH, #NgayBDNamTaiChinh, #NgayKTNamTaiChinh, #NgayBDNamHoc, #NgayKTNamHoc
### P09F02 – Danh sách phiếu thu vãng lai đã thu
- Lưới 1 «Danh sách phiếu thu vãng lai» (bảng MPThuVL); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: NHHK thu [NHHKThu]; Số chứng từ [SoCTu]; Số tiền [SoTienThu]; Ghi chú thu [GCThuVL]; Quyển số [QUYENSO]; User thu [UserThu]; Ngày thu/chi [NgayTChi]
### Q31.01 – Danh sách đợt xét TN
- Lưới 1 «Danh sách đợt» (bảng DDOTTN); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đợt [MaDotTN]; Số quyết định [SoQDSV]; Số QĐ [SoQD]; Ngày ký [NgayKy]{ngày}; Người ký [NguoiKy]; Văn bằng [VanBang]{chọn}; Số sinh viên [SoSV]
### Q58.01.01 – Danh sách lớp in
- Lưới 1 «Danh sách lớp in»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Tên lớp [TenLop]; Mã ngành [MaNganh]; Mã khoa [MaKhoa]; Niên khóa [NienKhoa]; Mã học chế [MaHC]
### QLHT_CHONKHOA – View chon khoa cua User
- Lưới 1 «Danh sách khoa»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã đơn vị [MaDV]; Tên đơn vị [TenDV]
### QLHT_DoiMaTheoFile – Doi ma theo file
- Lưới 1 (bảng HMess); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã cũ [MACU]; Mã mới [MAMOI]
### QLHT_HUYQUYEN – View ủy quyền user
- Lưới 1 «Danh sách user ủy quyền» (bảng HUyquyen); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã user ủy quyền [MAUSERCHO]{nút …}; Tên user ủy quyền [TenUserCho](chỉ đọc); Mã user nhận [MAUSERNHAN]{nút …}; Tên user nhận [TenUserNhan](chỉ đọc); Từ ngày [TuNgay]{ngày}; Đến ngày [DenNgay]{ngày}
### QLHT_ViewChonCTHOC – View chọn chương trình học
- Lưới 1 «Chọn chương trình học» (bảng HDMDVPC); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đơn vị phân cấp [MaDVPC]; Chương trình học [TenDVPC]
### QLHT_ViewChonLoupUp – View chon LoupUp động
- Lưới 1 «Danh sách dữ liệu chọn»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đối tượng [MaDoiTuong]; Tên đối tượng [TenDoiTuong]; Tên đối tượng 2 [TenDoiTuong2]
### QLHT_ViewChonUser – View chonj user (Soure truyền vào)
- Lưới 1 «Danh sách user»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: UserName [UserName]; Tên đầy đủ [HotenTK]; Mã user ủy quyền [MAUSERCHO]; Tên user ủy quyền [TenUserCho]; Mã user nhận [MAUSERNHAN]; Tên user nhận [TenUserNhan]; Ghi chú [GCTK]
### QLHT_ViewChonUser_Mul – View chonj user (Soure truyền vào)
- Lưới 1 «Danh sách User»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: UserName [UserName](chỉ đọc); Tên đầy đủ [HotenTK](chỉ đọc)
### QLHT_VIEWDAHK – View định nghĩa đa học kỳ
- Lưới 1 «Danh sách đa học kỳ» (bảng HDMDVPC); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đơn vị phân cấp [MaDVPC]; Tên viết tắt [VtDVPC]; Tên đơn vị phân cấp [TenDVPC]
  - Ô trên form sửa: #MaDVPC, #VtDVPC, #TenDVPC
### QLHT_ViewHoLotTenSV – View danh sach ho lot ten sv không khớp dữ liệu
- Lưới 1 «Danh sách sinh viên có dữ liệu không khớp»; tắt: Thêm, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Họ và tên [TenDayDu]
### QLHT_ViewPhanQuyenGCN – Phan quyền user ql cấp bảng điểm GCN
- Lưới 1 «Danh sách người dùng» (bảng HUser); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: UserName [UserName](chỉ đọc); Tên đầy đủ [HotenTK](chỉ đọc); Có QL bảng điểm [IsQLBD]; Có QL giấy CN [IsQLGCN]
### QLHT_ViewPQ_BH – View xử lý chọn bậc hệ phân quyên
- Lưới 1 «Danh sách bậc hệ»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã đối tượng [MaBH](chỉ đọc); Tên đối tượng [TenBH](chỉ đọc)
### QLHT_ViewQP_DVQL – View chọn đươn vị quản lý
- Lưới 1 «Danh sách đơn vị phân cấp»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã đơn vị phân cấp [MaDVPC](chỉ đọc); Tên đơn vị phân cấp [TenDVPC](chỉ đọc)
### QLHT_ViewQP_GCN – View chọn giấy chứng nhận
- Lưới 1 «Danh sách giấy chứng nhận»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã GCN [MaGCN](chỉ đọc); Tên giấy CN [TenGCN](chỉ đọc)
### QLHT_ViewUSerPH – Gán user quản trị phân hệ
- Lưới 1 «Danh sách user»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: UserName [UserName]; Tên đầy đủ [HotenTK]; Ghi chú dùng bên detailright [GhiChuView1]
  - Ô trên form sửa: #UserName, #HotenTK, #GhiChuView1
### QLHT_ViewUserPQ_BH – Phân quyền user theo bậc hệ
- Lưới 1 «Danh sách tài khoản»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: UserName [UserName]; Tên đầy đủ [HotenTK]; Ghi chú dùng bên detailright [GhiChuView1]
  - Cột ẩn: Đối tượng [DoiTuongPQ]
  - Ô trên form sửa: #UserName, #HotenTK, #GhiChuView1, #DoiTuongPQ
### QLHT_ViewUserPQ_DVQL – Phân quyền user theo đơn vị ql
- Lưới 1 «Danh sách user»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: UserName [UserName]; Tên đầy đủ [HotenTK]; Ghi chú dùng bên detailright [GhiChuView1]
  - Ô trên form sửa: #UserName, #HotenTK, #GhiChuView1
### QLHT_ViewUserPQ_GCN – Phân quyền user theo giấy CN
- Lưới 1 «Danh sách User»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: UserName [UserName]; Tên đầy đủ [HotenTK]; Ghi chú dùng bên detailright [GhiChuView1]
  - Ô trên form sửa: #UserName, #HotenTK, #GhiChuView1
### QLHT_ViewXemFileFiled – Xem file field
- Lưới 1 «Danh sách filefied» (bảng AQFileField); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã file [MaFile]; Tên file [TenFile]; Mã field [MaField]; Tên Field [TenField]; ID Field [IDField]; ID File Field [IDFileField]; Phân loại field [plfield]{chọn}; Khóa chính [IsKhoa]; Khóa phụ [IsKhoaPhu]; Cho rỗng [AllowNull]; Mã Enum [MaEnum]
### QLNS_ViewChonNVVL – View chon nhan su vang lai
- Lưới 1 «Danh sách nhân sự vãng lai»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã nhân sự vãng lai [MaNSVL]; Họ lót nhân sự [HoLotNSVL]; Tên nhân sự [TenNSVL]; Ngày sinh [NgaySinhCNSVL]; Phái [PhaiNSVL]{chọn}
### QLNS_ViewNSVLHK – View nhan su van lai học kt
- Lưới 1 «Danh sách nhân sự vãng lai học kỳ» (bảng NNSVLHK); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã nhân sự vãng lai [MaNSVL](chỉ đọc); Họ lót nhân sự [HoLotNSVL](chỉ đọc); Tên nhân sự [TenNSVL](chỉ đọc); Phái [PhaiNSVL]{chọn}(chỉ đọc); Ngày sinh [NgaySinhCNSVL](chỉ đọc); Lưu trú ký túc xá [IsLuuTruKTX]; Coi thi [IsCoiThi]; Có đánh giá khảo sát [IsDanhGia]
### QLSV_CheckNgaySinh – View hien thi loi ngay sinh
- Lưới 1 «Danh sách sinh viên có ngày sinh không hợp lệ»; tắt: Thêm, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]
### QLSV_CHONLOP1 – Giao diện chọn lớp 1 record
- Lưới 1 «Danh sách lớp» (bảng SDMLOP); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Tên lớp [TenLop]; Số sinh viên [SoSV]; Tên viết tắt [VTLop]; Ghi chú [GcLop]; Mã đơn vị [MaDV]; Mã khoa [MaKhoa]; Niên khóa [NienKhoa]; Mã bậc hệ [MaBH]
### QLSV_ImpDoiLop – Import quyet dinh doi lop
- Lưới 1 (bảng SDSQD); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số quyết định [SoQDSV]; Tên quyết định [TenQDSV]; Ngày lập QĐ [NgayLapQDSV]; Mã lý do [MaLDQDSV]; Mã lớp (mới) [MaLopMoi]; Mã lớp [MaLop]
### QLSV_ImpDSNghi – Import danh sach nghi hoc
- Lưới 1 (bảng SDSQD); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số quyết định [SoQDSV]; Tên quyết định [TenQDSV]; Ngày lập QĐ [NgayLapQDSV]; Mã lý do [MaLDQDSV]; Mã SV [MaSV]
### QLSV_ImpDSTamDung – Import danh sach qd tam dừng
- Lưới 1 (bảng SDSQD); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số quyết định [SoQDSV]; Tên quyết định [TenQDSV]; Ngày lập QĐ [NgayLapQDSV]; Mã lý do [MaLDQDSV]; Mã SV [MaSV]; Số học kỳ nghỉ [SoHKNghi]; Ghi chú [GcDSSVQD]
### QLSV_ImportAvatarErr – Dữ liệu import ảnh thất bại
- Lưới 1 «Danh sách import ảnh thất bại»; tắt: Thêm, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Mã viên chức [MaNV]; Mã DS thí sinh [MADSTS]; Ghi chú [GhiChu]; Số CCCD [SoCCCD]; Số CMND [SoCMND]
### QLSV_ImportAvatarSucc – Dữ liệu import ảnh thành công
- Lưới 1 «Danh sách import ảnh thành công»; tắt: Thêm, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Mã viên chức [MaNV]; Mã DS thí sinh [MADSTS]; Số CMND [SoCMND]; Số CCCD [SoCCCD]
### QLSV_ImpSDSQD – Import danh sach quyet dinh vao moi
- Lưới 1 (bảng SDSQD); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lý do [MaLDQDSV]; Số quyết định [SoQDSV]; Tên quyết định [TenQDSV]; Ngày lập QĐ [NgayLapQDSV]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Phái [Phai]; Mã lớp [MaLop]; Mã diện sinh viên [MaDSV]
### QLSV_ImpSDTSV – Import đoàn thể sinh viên
- Lưới 1 (bảng SDTSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Loại đoàn thể [LoaiDThe]; Ngày vào [NgayVao]; Nơi kết nạp [NoiKetNap]; Số kết nạp [SoKetNap]; Chức vụ [ChucVu]; Ngày ra [NgayRa]; Thứ tự [TTDTSV]; Ghi chú [GcDTSV]
### QLSV_NhapTTSV – Nhap Thong Tin Ly Lich SV theo lop
- Lưới 1 «Danh sách sinh viên» (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Thứ tự [TTSV]; Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Cân nặng [CanNang]; Chiều cao [ChieuCao]; Chi nhánh [CHINHANHNH]; Hình sinh viên [AvatarSV]; Có nghề [CoNghe]; Cơ quan công tác [CQCT]; Chức vụ công tác [CVCQCT]; Địa chỉ [DC_DCHK]; Địa chỉ 2 [DC_DCHK2]; Địa chỉ liên lạc [DC_DCLLSV]; Địa chỉ [DC_DCTT]; Địa chỉ [DC_DCVC]; Số ĐT cha [DC_DT1Cha]; Điện thoại 1 [DC_DT1HK]; Điện thoại 1 [DC_DT1LLSV]; Số ĐT mẹ [DC_DT1Me]; Điện thoại 1 [DC_DT1TT]; Điện thoại 1 [DC_DT1VC]; Điện thoại 2 [DC_DT2HK]; Điện thoại 2 [DC_DT2LLSV]; Điện thoại 2 [DC_DT2TT]; Điện thoại 2 [DC_DT2VC]; Điện thoại NgLL [DC_DTNgLL]; Email 1 [DC_Eml1HK]; Email 1 [DC_EML1LLSV]; Email 1 [DC_Eml1TT]; Email 1 [DC_Eml1VC]; Email 2 [DC_Eml2HK]; Email 2 [DC_EML2LLSV]; Email 2 [DC_Eml2TT]; Email 2 [DC_Eml2VC]; Email NgLL [DC_EmlNgLL]; GC hộ khẩu [DC_GcHK]; GC liên lạc [DC_GcLL]; GC thường trú [DC_GcTT]; GC vợ chồng [DC_GcVC]; Tỉnh/thành [DC_IDDBHK]; Tỉnh/thành [DC_IDDBLL]; Tỉnh/thành [DC_IDDBTT]; Tỉnh/thành [DC_IDDBVC]; Địa chỉ CQCT [DCCQCT]; Điểm 1 [Diem1]; Điểm 2 [Diem2]; Điểm 3 [Diem3]; ĐK kinh tế [DKKinhTe]{chọn}; Ghi chú [GcSV]; Ghi chú [GcThPhanGD]; Tỉnh/thành [IDDB_CQCT]; Dân tộc [IDDT]; Ngân hàng [IDNgHang]; Tôn giáo [IDTG]; Loại cư trú [LoaiCuTru]{chọn}; Lớp 10 [LOP10]; Lớp 11 [LOP11]; Lớp 12 [LOP12]; Mã lớp [MaLopSV]; Mã số thuế [MaSoThue]; Cha mất [MatCha]; Mẹ mất [MatMe]; Ngày ngoại trú [NgayNgTru]{ngày}; Ngày sinh [NgaySinhC]; Ngày cấp [NgCapCMND]{ngày}; Nghề ng vợ/chồng [NgNghiepVC]; Ngày sinh [NgSinhCha]; Ngày sinh [NgSinhMe]; Người liên lạc [NguoiLL]; Nghề nghiệp [NNgCha]; Nghề nghiệp [NNgMe]; Nơi cấp [NoiCapCMND]; Nơi sinh [NoiSinh]; Phái [Phai]{chọn}; Phòng ký túc xá [PhongKTX]; Quê quán [QueQuan]; Quốc tịch [QuocTich]; Số anh chị em [SoAnhChiEm]; Số CMND [SoCMND]; Số năm bộ đội [SoNamBD]; Số năm TNXP [SoNamTNXP]; Số tài khoản [SoTaiKhoan]; Tên cha [TenCha]; Tên chủ hộ [TenChuHo]; Tên chủ hộ (HK) [TenChuHoHK]; Họ và tên [TenDayDu]; Tên đầy đủ trên VB [TenDayDuVB]; Tên hộ [TenHo]; Tên mẹ [TenMe]; Tên [TenSV2]; Tên vợ/chồng [TenVC]; Thẻ thư viện [TheThuVien]; Thành phần GĐ [ThPhanGD]{chọn}; ThPhanGDC [ThPhanGDC]; Trường chuyển [TrChuyen]; Tên viết tắt [VtSV]; Tên trường THPT 12 [TenTRPT12]; Tỉnh trường THPT 12 [TenTinhPT12]
### QLSV_ViewAddHB – View thêm danh sach hoc bong
- Lưới 1 «Danh sách sinh viên»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Mã khối học bổng [MaKhHBHK]; Mã lớp [MaLop]; Điểm rèn luyện học bổng [DiemRLHB]; ĐTB HB [DiemTBHB]
### QLSV_ViewBac_Test – Danh sach bac
- Lưới 1 (bảng KDMBac); tắt: Xóa, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc [MaBac]; Tên bậc đào tạo [TenBac]; Tên viết tắt [VtBac]
  - Ô trên form sửa: #MaBac, #TenBac, #VtBac
### QLSV_ViewBH_Test – Bac he
- Lưới 1 (bảng KDMBH); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]; Mã bậc [MaBac]; Liên thông [LoaiLT]
  - Cột ẩn: Bậc [IDBac]
  - Ô trên form sửa: #MaBH, #TenBH, #LoaiLT, #IDBac
### QLSV_ViewCapNhatBanCanSu – View cap nhat ban can su
- Lưới 1 «Danh sách chức vụ sinh viên» (bảng SCVSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Phái [Phai]{chọn}(chỉ đọc); Chức vụ BCS [IDCVBCS]
### QLSV_ViewCapNhatDSDonTu – View cap nhat danh sach don tu
- Lưới 1 «Danh sách cập nhật đơn từ sinh viên» (bảng SDSDTUSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Tên đơn từ SV [TenDTuSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên đơn vị [TenDV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Mã đơn từ SV [MaDTuSV](chỉ đọc); Ngày nhận đơn [NgayNhanDTU]{ngày}(chỉ đọc); Ngày trả đơn [NgayTraDTU]{ngày}(chỉ đọc); Nội dung đơn [NoiDungDTU](chỉ đọc); Mã đơn vị [MaDV](chỉ đọc); Trạng thái đơn [TrangThaiDTU]{chọn}; Ghi chú [GhiChuDTU]
  - Cột ẩn: Còn Nợ [ConNo](chỉ đọc); Số TCDKHK [SOTCDKHK](chỉ đọc); TCTLHK [SoTCTLHK](chỉ đọc)
### QLSV_ViewCapNhatSoQD – View cập nhật số QĐ
- Lưới 1 (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Số quyết định [SoQDSV]; Ngày lập QĐ [NgayLapQDSV]
### QLSV_ViewCapPhatBSao – View cấp phát bản sao sinh viên
- Lưới 1 «Danh sách sinh viên cấp phát bản sao TN» (bảng STTCAPBS); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Phái [Phai]; Tên ng/chng [TenNgChng]; Tên bậc hệ [TenBH]; Xếp loại tốt nghiệp [XepLoaiTN]; Ngày cấp [NgayCap]{ngày}; Số vào sổ cấp bản sao [SoVaoSoBS]; Số lượng cấp bản sao [SoLuongBS]; Ngày cấp bản sao [NgayCapBS]{ngày}; Người ký bản sao [NguoiKyBS]; Người ký bằng TN gốc [NguoiKyBanGoc]
  - Cột ẩn: Sinh viên [IDSV]
  - Ô trên form sửa: #HoLotSV, #TenSV, #NgaySinhC, #Phai, #SoVaoSoBS, #SoLuongBS, #NgayCapBS, #NguoiKyBS, #NguoiKyBanGoc, #IDSV
### QLSV_ViewCheckQD – View check qd hợp lệ
- Lưới 1 «Danh sách sinh viên»; tắt: Thêm, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Phái [Phai]; Mã lớp (cũ) [MaLopCu]
### QLSV_ViewCheckQD_HL – View check qd hợp lệ
- Lưới 1; tắt: Thêm, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Phái [Phai]; Mã lớp (cũ) [MaLopCu]
### QLSV_ViewChon1Lop – View chon 1 lop
- Lưới 1 «Danh sách lớp»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Tên lớp [TenLop]; Sí số hiện diện [SiSoHD]
### QLSV_ViewChonDB – View chon dia ban (View thuong)
- Lưới 1 «Danh sách địa bàn»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã địa bàn [MaDB]; Tên địa bàn [TenDB]
### QLSV_ViewChonDoanThe – View cap nhat doan the
- Lưới 1 «Danh sách đoàn thể»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Thứ tự [TTDTSV]; Loại đoàn thể [LoaiDThe]{chọn}(chỉ đọc); Ngày vào [NgayVao]{ngày}; Nơi kết nạp [NoiKetNap]; Chức vụ [ChucVu]; Số kết nạp [SoKetNap]; Ngày ra [NgayRa]{ngày}; Ghi chú [GcDTSV]
### QLSV_ViewChonDoanTheNhieu – View chon doan the chon nhieu
- Lưới 1 «Danh sách đoàn thể»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Loại đoàn thể [LoaiDThe]{chọn}
### QLSV_ViewChonDotTTVB – View chon dot tham tra van bang
- Lưới 1 «Danh sách đợt thẩm tra văn bằng»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Đợt TTVB [DotTTVB]; Số lượng [SoLuong]
### QLSV_ViewChonDSDatHB – View chon ds dat hoc bong
- Lưới 1 «Danh sách sinh viên đạt học bổng»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Loại HB [LoaiHB]{chọn}; % MG [PTramMG]; Số TC MG [SoTCMG]; Số TC MGHK [SoTCMGHK]; Số tiền HB [SoTienHB]; ĐTB HB [DiemTBHB]; Ghi chú [GhiChuHBTS]
### QLSV_ViewChonDSXetHB – View chon ds xet HB
- Lưới 1 «Danh sách sinh viên»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Mã lớp [MaLop]; Mã khối học bổng [MaKhHBHK]; Tên khối học bổng [TenKhHBHK]
### QLSV_ViewChonDVQL – View chọn đơn vị quản lý lớp
- Lưới 1 «Danh sách đơn vị quản lý» (bảng NDMDVQL); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đơn vị QL [MaDVQL]; Tên đơn vị QL [TenDVQL]; Viết tắt [VtDVQL]
### QLSV_VIEWCHONGCN – View chọn giấy CN nhiều
- Lưới 1 «Danh sách giấy chứng nhận» (bảng SDMGCN); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã GCN [MaGCN]; Tên giấy CN [TenGCN]
### QLSV_ViewChonLoaiVB – View chon loai van bang
- Lưới 1 «Danh sách loại văn bằng» (bảng NDMLVB); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã loại VB [MaLoaiVB]; Tên loại VB [TenLoaiVB]; Viết tắt [VtLoaiVB]
### QLSV_ViewChonNoiTTVB – View chon noi tham tra van bang
- Lưới 1 «Danh sách nơi cấp văn bằng»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã nơi cấp VB [MaNCVB]; Tên nơi cấp VB [TenNCVB]; Viết tắt [VtNCVB]
### QLSV_ViewChonSVHK – View chon sinh vien hoc ky
- Lưới 1 «Danh sách sinh viên»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Phái [Phai]{chọn}; Hiện diện SV [HienDienSV]{chọn}; Mã lớp [MaLop]; ĐTBTN [DTBTN]; Xếp loại [XLTNTC]; Mã đợt [MaDotTN]; Số QĐ [SoQD]; ĐTBTL HK [DTBTLHK]
### QLSV_ViewChonSVTachQD – View chọn SV tách QD
- Lưới 1 «Danh sách sinh viên cần tách quyết định»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Mã lớp (mới) [MaLopMoi]; Số quyết định [SoQDSV]; Ngày lập QĐ [NgayLapQDSV]{ngày}
### QLSV_ViewChonTieuChuanRL – View chon tieu chuan ren luyen
- Lưới 1 «Danh sách tiêu chuẩn»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã tiêu chuẩn [MaTChuan]; Tên tiêu chuẩn [TenTChuan]; Tên viết tắt [VTTChuan]
### QLSV_ViewChonVB – View chon van bang
- Lưới 1 «Chọn hệ đào tạo văn bằng»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Hệ đào tạo [HeDTVB]{chọn}
### QLSV_ViewChonVB_DHQT – View chon van bang
- Lưới 1 «Chọn hệ đào tạo văn bằng»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: VB hệ đào tạo TS [HeDTVBTS]{chọn}
### QLSV_ViewChuyenHB – Danh sach sv đạt hoc bong duy tri
- Lưới 1 «Danh sách sinh viên đạt học bổng» (bảng MDSHB); tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Phái [Phai](chỉ đọc); Loại HB [LoaiHB]{chọn}(chỉ đọc); % MG [PTramMG](chỉ đọc); Số TC MG [SoTCMG](chỉ đọc); Số TC MGHK [SoTCMGHK](chỉ đọc)
### QLSV_ViewCuuSVNew – View nhap thong tin cuu sinh vien
- Lưới 1 «Danh sách thông tin cựu sinh viên» (bảng SHSTN); tắt: Thêm, Xóa, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Phái [Phai](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Số CMND [SoCMND](chỉ đọc); Mã lớp [MaLop](chỉ đọc); NHHK ra [NHHKRa](chỉ đọc); Mã Ng/CNg [MaNgChng](chỉ đọc); Tên ng/chng [TenNgChng](chỉ đọc); Hình thức khảo sát [HinhThucKS]; Có phản hồi [IsPhanHoi]; Đúng ngành đào tạo [IsDungNganh]; Liên quan đến ngành đào tạo [IsLienQuanNganh]; Không liên quan đến ngành đào tạo [IsNotLienQuanNganh]; Tiếp tục học [IsTiepTucHoc]; Chưa có việc làm [IsChuaCoViec]; Khu vực làm việc [KhuVucLamViec]{chọn}; Hình thức khảo sát [HinhThucKhaoSat]{chọn}; Tình trạng việc làm [TinhTrangViecLam]{chọn}; Thời gian tìm được việc [ThoiGianTimViec]{chọn}; Việc làm phù hợp [ViecLamHopLe]{chọn}; Mức TN [MucTN]{chọn}; Chưa có việc làm [ChuaViecLam]{chọn}; Cơ quan công tác [CQCT]; Email [DC_EmlCQCT]; Điện thoại [DC_DTCQCT]; Địa chỉ CQCT [DCCQCT]; Tỉnh/thành [IDDB_CQCT]; Facebook [Facebook]; Instagram [Instagram]; Ghi chú [GCHSTN]
### QLSV_ViewDanhSachTTVB – View danh sách thẩm tra văn bằng
- Lưới 1 «Danh sách thẩm tra văn bằng» (bảng SDSTTVB); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Văn bằng [LoaiVB]{chọn}; Số văn bằng [SoVB]; Ngày cấp [NgayCapVB]{ngày}; Ngày TTVB [NgayTTVB]{ngày}; Số HSTTVB [SoHSTTVB]; Năm tốt nghiệp [NAMTN]; Niên học học kỳ [NHHK]; Nơi cấp VB [IDNCVB]; Khóa thi [KhoaThiVB]
  - Cột ẩn: Đợt TTVB [DotTTVB]; Sinh viên [IDSV]; Kết quả TTVB [IsKetQuaTTVB]; Kết quả TTVB [KetQuaTTVB]{chọn}; Ngày kết quả [NgayKQTTVB]{ngày}; Họ và tên [TenDayDu]
  - Ô trên form sửa: #NgaySinhC, #LoaiVB, #SoVB, #NgayCapVB, #NgayTTVB, #SoHSTTVB, #NAMTN, #IDNCVB, #KhoaThiVB, #DotTTVB, #IDSV, #IsKetQuaTTVB, #KetQuaTTVB, #NgayKQTTVB, #TenDayDu
### QLSV_ViewDNKhoiHBHK – View dn khoi hoc bong HK DQQT
- Lưới 1 «Danh sách khối học bổng học kỳ»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối học bổng [MaKhHBHK]; Tên khối học bổng [TenKhHBHK]; Không xét học bổng [IsKhgXet]
  - Cột ẩn: Ghi chú dùng bên detailright [GhiChuView1]
  - Ô trên form sửa: #MaKhHBHK, #TenKhHBHK, #IsKhgXet, #GhiChuView1
### QLSV_ViewDotSVTN – View danh sach dot tn sinh vien
- Lưới 1 «Danh sách đợt tốt nghiệp»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đợt [MaDotTN]; Ngày ký [NgayKy]{ngày}; Số QĐ [SoQD]; Số sinh viên [SoSV]; Đã có QĐ [DaCoQD]; Chưa có QĐ [ChuaCoQD]
### QLSV_ViewDSAV_TQ – View xem danh sach anh văn tiên quyêt
- Lưới 1 «Danh sách môn học anh văn tiên quyết» (bảng SDATAVTQ); tắt: Thêm, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Mã môn học [MaMH]; Tên môn học [TenMH]; Đạt [IsDatTQ]; Điểm [DiemMHTQ]
### QLSV_ViewDSBVHK – Danh sách bênh viện theo học kỳ
- Lưới 1 «Danh sách bệnh viện khám chữa bệnh» (bảng SBVKCBHK); tắt: Import, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã BVKCB [MaBVKCB](chỉ đọc); Tên BVKCB [TenBVKCB](chỉ đọc); Ghi chú BVKCB [GCBVKCBHK]
### QLSV_ViewDSCapDonTu – View xu ly ds ma tuy
- Lưới 1 «Danh sách đơn từ sinh viên» (bảng SDSDTUSV); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Đơn từ SV [IDDTuSV]; Ngày nhận đơn [NgayNhanDTU]{ngày}; Ngày trả đơn [NgayTraDTU]{ngày}; Đơn vị xử lý [IDDVXL]
  - Cột ẩn: Còn Nợ [ConNo]; Sinh viên [IDSV]; Mã lớp [MaLop]; Nội dung đơn [NoiDungDTU]; Số TCDKHK [SOTCDKHK]; TCTLHK [SoTCTLHK]
  - Ô trên form sửa: #HoLotSV, #TenSV, #IDDTuSV, #NgayNhanDTU, #NgayTraDTU, #IDDVXL, #IDSV, #MaLop, #NoiDungDTU
### QLSV_ViewDSCapTheSV – View DS cap the sinh vien
- Lưới 1 «Danh sách sinh viên cấp thẻ» (bảng STHESV); tắt: In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Mã lớp [MaLop]; Tên lớp [TenLop]; Mã khối [MaKhoi]; Tên khối [TenKhoi]; Niên khóa [NienKhoa]; Mã Ng/CNg [MaNgChng]; Tên ng/chng [TenNgChng]; Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]; Mã bậc [MaBac]; Tên bậc [TenBac]; Mã hệ đào tạo [MaHe]; Tên hệ [TenHe]; Lệ phí [LePhiThe]; Ngày cấp [NgCapTheSV]{ngày}; Cấp lại [CapLaiThe]
  - Cột ẩn: Ghi chú [GcTheSV]; Sinh viên [IDSV]; Thời hạn sử dụng [ThoiHanSuDung]{ngày}
  - Ô trên form sửa: #HoLotSV, #TenSV, #LePhiThe, #NgCapTheSV, #CapLaiThe, #GcTheSV, #IDSV, #ThoiHanSuDung
### QLSV_ViewDSHB1SV – View danh sach HB
- Lưới 1 «Danh sách thông tin học bổng SV»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Mã lớp [MaLop]; Số TC đăng ký [SoTCDK]; ĐTB HB [DiemTBHB]; Điểm trung bình học bổng tương đương [DiemTBHBTD]; Tiền học bổng [TienHB]
  - Cột ẩn: Lý do [LyDoHB]{chọn}; Mức học bổng [MucHB]
### QLSV_ViewDSHBTT – View danh sach hoc bong tai tro
- Lưới 1 «Danh sách sinh viên nhận học bổng tài trợ» (bảng SDSHB); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Phái [Phai]{chọn}; Mã lớp [MaLop]; Nhà tài trợ [IDTAITRO]; Tiền học bổng [TienHB]
  - Cột ẩn: Sinh viên [IDSV]
  - Ô trên form sửa: #HoLotSV, #TenSV, #NgaySinhC, #Phai, #MaLop, #IDTAITRO, #TienHB, #IDSV
### QLSV_ViewDSHSSVThieu – Danh sach sv nop HS thieu
- Lưới 1 «Danh sách sinh viên»; tắt: Thêm, Xóa, Import, In, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Mã lớp [MaLop]; Mã hồ sơ [MaHS]; Tên hồ sơ [TenHS]
### QLSV_ViewDSSV_TCMin – View DS sv lam them
- Lưới 1 «Danh sách sinh viên» (bảng SDSLNTCMIN); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Số TC min [SoTCMin]; Mã lớp [MaLop]
  - Cột ẩn: Sinh viên [IDSV]
  - Ô trên form sửa: #HoLotSV, #TenSV, #SoTCMin, #MaLop, #IDSV
### QLSV_ViewDSSVLThem – View DS sv lam them
- Lưới 1 «Danh sách sinh viên làm thêm» (bảng SDSSVLT); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Chuyên môn [PhuHop]{chọn}; Ngày bắt đầu làm thêm [NgayBDLTH]{ngày}
  - Cột ẩn: Ghi chú [GcBDLTH]; Sinh viên [IDSV]; Mã lớp [MaLop]
  - Ô trên form sửa: #HoLotSV, #TenSV, #PhuHop, #NgayBDLTH, #GcBDLTH, #IDSV, #MaLop
### QLSV_ViewDSSVNGhien – View DS sv nghien
- Lưới 1 «Danh sách sinh viên nghiện» (bảng SDSNG); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Rượu [NghienRu]; Thuốc lá [NghienTL]; Biểu hiện ma túy [NghienBH]; Ma túy [NghienMT]; Ngày ghi nhận [NgayGhiNhan]{ngày}
  - Cột ẩn: Ghi chú [GcDSNG]; Sinh viên [IDSV]; Mã lớp [MaLop]
  - Ô trên form sửa: #HoLotSV, #TenSV, #NghienRu, #NghienTL, #NghienBH, #NghienMT, #NgayGhiNhan, #GcDSNG, #IDSV, #MaLop
### QLSV_ViewDSXetHB – View danh sách SV xét HB
- Lưới 1 «Danh sách SV xét học bổng» (bảng SSVXETHB); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Mã lớp [MaLop]; Mã khối học bổng [MaKhHBHK]
  - Cột ẩn: Khối HBHK [IDKHHBHK]; Sinh viên [IDSV]
  - Ô trên form sửa: #HoLotSV, #TenSV, #MaLop, #IDKHHBHK, #IDSV
### QLSV_ViewDTSV – View cap nhat doan the sinh vien
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Sinh viên [IDSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Phái [Phai]; Mã lớp [MaLop]; Tên lớp [TenLop]; Ghi chú dùng bên detailright [GhiChuView1]
  - Ô trên form sửa: #IDSV, #HoLotSV, #TenSV, #NgaySinhC, #Phai, #MaLop, #TenLop, #GhiChuView1
### QLSV_ViewGanCVHTNg2 – View gán CVHT lop sinh vien nganh 2
- Lưới 1 «Danh sách sinh viên ngành 2» (bảng SSVHKN2); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Mã lớp [MaLop](chỉ đọc); ID CVHT [IDCVHT]; Tên đầy đủ [TenDayDuNV](chỉ đọc)
### QLSV_VIEWHDXH – View nhập ds hoạt động XH
- Lưới 1 «Danh sách hoạt động xã hội» (bảng SHDXH); tắt: Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã hoạt động XH [MaHDXH]; Tên hoạt động XH [TenHDXH]; Địa điểm tổ chức [DiaDiemHDXH]; Từ ngày [TuNgayHDXH]{ngày}; Đến ngày [DenNgayHDXH]{ngày}
  - Cột ẩn: Ghi chú HĐXH [GcHDXH]; Ghi chú dùng bên detailright [GhiChuView1]
  - Ô trên form sửa: #MaHDXH, #TenHDXH, #DiaDiemHDXH, #TuNgayHDXH, #DenNgayHDXH, #GcHDXH, #GhiChuView1
### QLSV_ViewHSSVNew – View cap nhat ho so sinh vien
- Lưới 1 «Cập nhật lý lịch sinh viên»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Sinh viên [IDSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Phái [Phai]; Mã lớp [MaLop]; Tên lớp [TenLop]; Ghi chú dùng bên detailright [GhiChuView1]; Tên phương thức [TenPTXT]; Nhóm khu vực [NhomKVTS]; Ngành thi [NganhThi]; Đối tượng TS [DOITUONGTS]
  - Ô trên form sửa: #IDSV, #HoLotSV, #TenSV, #NgaySinhC, #Phai, #MaLop, #TenLop, #GhiChuView1
### QLSV_ViewImport_CVHT – View import CVHT theo lop
- Lưới 1 (bảng SDMLOP); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Mã viên chức [MaNV]
### QLSV_ViewImportLop – View import lop
- Lưới 1 (bảng SDMLOP); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]
### QLSV_ViewImpSDSHB – Import DS học bổng
- Lưới 1 (bảng SDSHB); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Mã khối học bổng [MaKhHBHK]; Mức học bổng [MucHB]; Điểm rèn luyện học bổng [DiemRLHB]; Xếp loại rèn luyện [XLRL]; ĐTB HB [DiemTBHB]; Xếp loại học tập [XLHT]; Tiền học bổng [TienHB]
### QLSV_ViewImpSVBSV – Import van bang sinh vien
- Lưới 1 (bảng SVBSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Tên bậc đào tạo [BacDTVB]; Hệ đào tạo [HeDTVB]; Xếp loại [XepLoaiVB]; Nơi cấp [TruongVB]; Số văn bằng [SOVBSV]; Ngày cấp [NgayCapVB]; Th/gian học (tháng) [SoThangVB]; Năm BĐ [NamBDVB]; Ngành nghề [NganhNgheVB]; Khóa thi [KhoaThiVB]
### QLSV_ViewInCapBanSaoBangTN – View cấp phát bản sao sinh viên
- Lưới 1 (bảng STTCAPBS); tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Phái [Phai]; Tên ng/chng [TenNgChng]; Tên bậc hệ [TenBH]; Xếp loại tốt nghiệp [XepLoaiTN]; Ngày cấp [NgayCap]{ngày}; Số vào sổ cấp bản sao [SoVaoSoBS]; Số lượng cấp bản sao [SoLuongBS]; Ngày cấp bản sao [NgayCapBS]{ngày}; Người ký bản sao [NguoiKyBS]; Người ký bằng TN gốc [NguoiKyBanGoc]
  - Ô trên form sửa: #HoLotSV, #TenSV, #NgaySinhC, #Phai, #SoVaoSoBS, #SoLuongBS, #NgayCapBS, #NguoiKyBS, #NguoiKyBanGoc
### QLSV_ViewInCapPhatBSao – View cấp phát bản sao sinh viên
- Lưới 1 «Danh sách sinh viên cấp phát bản sao bằng TN» (bảng STTCAPBS); tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Phái [Phai]; Tên ng/chng [TenNgChng]; Tên bậc hệ [TenBH]; Xếp loại tốt nghiệp [XepLoaiTN]; Ngày cấp [NgayCap]{ngày}; Số vào sổ cấp bản sao [SoVaoSoBS]; Số lượng cấp bản sao [SoLuongBS]; Ngày cấp bản sao [NgayCapBS]{ngày}; Người ký bản sao [NguoiKyBS]; Người ký bằng TN gốc [NguoiKyBanGoc]
  - Ô trên form sửa: #HoLotSV, #TenSV, #NgaySinhC, #Phai, #SoVaoSoBS, #SoLuongBS, #NgayCapBS, #NguoiKyBS, #NguoiKyBanGoc
### QLSV_ViewKhoaDiemRL – View khóa điểm rèn luyện
- Lưới 1 «Danh sách lớp»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Tên lớp [TenLop]; Tên viết tắt [VTLop]; Niên khóa [NienKhoa]; Mã đơn vị [MaDV]; Đã khóa điểm [IsLockDiemRL]
### QLSV_ViewKhoiHB – View dinh nghia khop
- Lưới 1 «Danh sách khối»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; NHHK vào [NHHKVao]
### QLSV_ViewKQHBDV – View kết quả danh sách học bổng đầu vào
- Lưới 1 «Danh sách sinh viên» (bảng SDSHBSVDV); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; ĐTBNH [DTBNHTS]; Mức HB [MucDatHBMG]{chọn}; % MG [PTramMG]; Mã lớp [MaLop]; Ghi chú HB [GcDSHBTSDV]
  - Cột ẩn: Sinh viên [IDSV]; Niên khóa [NienKhoa]; Tên khoa [TenKhoa]; Tên ngành [TenNganh]
  - Ô trên form sửa: #HoLotSV, #TenSV, #DTBNHTS, #MucDatHBMG, #PTramMG, #GcDSHBTSDV, #IDSV
### QLSV_ViewNganhKhoaHB – View chon nganh khoa hoc bong
- Lưới 1 «Danh sách ngành»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã ngành [MaNganh]; Tên ngành [TenNganh]; Khóa học [KhoaHoc]; Số lượng [SoLuong]
### QLSV_VIEWNHAPCHNG2SV – View nhap chuyen nganh2  sinh vien
- Lưới 1 «Danh sách sinh viên nhập chuyên ngành 2» (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Mã ch/ngành SV [IDChNgSV2]; Tên ng/chng [TenNgChng](chỉ đọc)
### QLSV_ViewNhapCuuSV – View nhap thong tin cuu sinh vien
- Lưới 1 «Danh sách thông tin cựu sinh viên» (bảng SHSTN); tắt: Thêm, Xóa, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Phái [Phai](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Số CMND [SoCMND](chỉ đọc); Mã lớp [MaLop](chỉ đọc); NHHK ra [NHHKRa](chỉ đọc); Mã Ng/CNg [MaNgChng](chỉ đọc); Tên ng/chng [TenNgChng](chỉ đọc); Hình thức khảo sát [HinhThucKS]; Có phản hồi [IsPhanHoi]; Đúng ngành đào tạo [IsDungNganh]; Liên quan đến ngành đào tạo [IsLienQuanNganh]; Không liên quan đến ngành đào tạo [IsNotLienQuanNganh]; Tiếp tục học [IsTiepTucHoc]; Chưa có việc làm [IsChuaCoViec]; Khu vực làm việc [KhuVucLamViec]{chọn}; Cơ quan công tác [CQCT]; Email cơ quan công tác [DC_EmlCQCT]; Điện thoại cơ quan công tác [DC_DTCQCT]; Địa chỉ CQCT [DCCQCT]; Tỉnh/thành [IDDB_CQCT]; Facebook [Facebook]; Instagram [Instagram]; Ghi chú [GCHSTN]
### QLSV_ViewNhapDatHBTS – View nhap danh sach dat hb tuyen sinh
- Lưới 1 «Danh sách sinh viên đạt học bổng tuyển sinh» (bảng SDSHBTS); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Tỷ lệ % [TyLeHB]; Số Tiền HB [SoTienHBTS]; Loại HB [LoaiHBTSDV]{chọn}; Số tiền HPHK [SoTienHP]
  - Cột ẩn: Ghi chú HB [GCDSHBTS]; Sinh viên [IDSV]
  - Ô trên form sửa: #NHHK, #HoLotSV, #TenSV, #TyLeHB, #SoTienHBTS, #LoaiHBTSDV, #SoTienHP, #GCDSHBTS, #IDSV
### QLSV_ViewNhapDoiTuongTN – View nhap doi tuong sv xet tot nghiep
- Lưới 1 «Danh sách sinh viên» (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Phái [Phai]{chọn}(chỉ đọc); Mã lớp [MaLop](chỉ đọc); Đối tượng SV xét TN [DoiTuongXetTN]{chọn}; Ghi chú [GcSV]
### QLSV_ViewNhapDSKgDatHB – View nhap danh sach khong dat hb tuyen sinh
- Lưới 1 «Danh sách sinh viên không đạt duy trì học bổng tuyển sinh» (bảng SKDHBTS); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Lý do [LyDoKDHB]{chọn}; Ghi chú kg đạt [GCKDHB]; Mã môn học [MaMH]
  - Cột ẩn: Môn học [IDMH]; Sinh viên [IDSV]
  - Ô trên form sửa: #NHHK, #HoLotSV, #TenSV, #LyDoKDHB, #GCKDHB, #IDMH, #IDSV
### QLSV_ViewNhapGiaHanDaoTao – View nhap gia han dao tao sinh vien
- Lưới 1 «Danh sách sinh viên gia hạn đào tạo» (bảng SSVGHHK); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Mã lớp [MaLop]; NHHK xin gia hạn [NHHK]; NHHK kết thúc [NHHKKT]; Số HK gia hạn [SoHKGH](chỉ đọc); Ngày gia hạn [NgayGHHK]{ngày}
  - Cột ẩn: Ghi chú [GcGHHK]; Sinh viên [IDSV]
  - Ô trên form sửa: #HoLotSV, #TenSV, #MaLop, #NHHKKT, #SoHKGH, #NgayGHHK, #GcGHHK, #IDSV
### QLSV_ViewNhapHBDV – View nhập danh sách học bổng đầu vào
- Lưới 1 «Danh sách sinh viên đạt học bổng học kỳ đầu» (bảng SHBSVDV); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Mức HB [MucHBMG]{chọn}; Tỷ lệ % [TyLeHB]; Hiện diện [HienDienSV2]{chọn}
  - Cột ẩn: Ghi chú [GcHBSVDV]; Sinh viên [IDSV]
  - Ô trên form sửa: #NHHK, #HoLotSV, #TenSV, #MucHBMG, #TyLeHB, #GcHBSVDV, #IDSV
### QLSV_ViewNhapHBTSDV – View nhập danh sách học bổng tuyển sinh đầu vào
- Lưới 1 «Danh sách sinh viên đạt học bổng tuyển sinh học kỳ đầu» (bảng SHBTSDV); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Tỉnh trường THPT 12 [TenTinhPT12]; Tên trường THPT 12 [TenTRPT12]; Loại HB [LoaiHBTSDV]{chọn}; Tỷ lệ % [TyLeHB]; Số HK chính [SoHKCh]; Số HK hè [SoHKPh]; SV trao đổi [IsSVTDoi]
  - Cột ẩn: Ghi chú HBTS [GCHBTSDV]; Sinh viên [IDSV]
  - Ô trên form sửa: #NHHK, #HoLotSV, #TenSV, #TenTinhPT12, #TenTRPT12, #LoaiHBTSDV, #TyLeHB, #SoHKCh, #SoHKPh, #IsSVTDoi, #GCHBTSDV, #IDSV
### QLSV_ViewNhapHTCTHOC – View nhap sv hoàn thành chương trình học
- Lưới 1 «Danh sách sinh viên hoàn thành chương trình» (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Phái [Phai]{chọn}(chỉ đọc); Hiện diện SV [HienDienSV]{chọn}(chỉ đọc); Mã lớp [MaLop](chỉ đọc); Đã hoàn thành CTĐT [IsHTCTHOC]
### QLSV_ViewNhapKQDKNCS – View nhap ket qua dang ky nghien cuu sinh
- Lưới 1 «Danh sách sinh viên có kết quả đăng ký nghiên cứu» (bảng SKQNCS); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Hoàn thành NV khoa [IsHTNVKH]; Ghi chú [GCHTNVKH]
  - Cột ẩn: Sinh viên [IDSV]
  - Ô trên form sửa: #NHHK, #HoLotSV, #TenSV, #IsHTNVKH, #GCHTNVKH, #IDSV
### QLSV_ViewNhapNganh2 – View nhap chuyen nganh sinh vien toan truong
- Lưới 1 «Danh sách sinh viên» (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Hiện diện SV [HienDienSV]{chọn}(chỉ đọc); Mã lớp [MaLop](chỉ đọc); Ngành 2 [IDNganh2]; Tên ng/chng [TenNgChng](chỉ đọc)
### QLSV_ViewNhapNganhBoSungSinhVien – View nhap nganh bo sung sinh vien
- Lưới 1 «Danh sách sinh viên» (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Phái [Phai](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Ngành bổ sung [IDNganhBS]; Tên ng/chng [TenNgChng](chỉ đọc)
### QLSV_ViewNhapSVKgThKe – View nhap sv khong thong ke
- Lưới 1 «Danh sách sinh viên» (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Phái [Phai]{chọn}(chỉ đọc); Mã lớp [MaLop](chỉ đọc); Không thống kê [IsThKe]
### QLSV_ViewNhapTen_BacVBSV – View nhap ten bac van bang tot nghiep sinh vien
- Lưới 1 «Danh sách sinh viên» (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Phái [Phai]{chọn}(chỉ đọc); Mã lớp [MaLop](chỉ đọc); Tên văn bằng [TenVanBang]; Tên bậc văn bằng [TenBacVanBang]
### QLSV_ViewNhapThongTinVB_BHN – View nhap thong tin van bang cho bac he nganh
- Lưới 1 «Danh sách thông tin văn bằng bậc hệ ngành» (bảng KDMBHNgChNg); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã bậc hệ [MaBH](chỉ đọc); Mã Ng/CNg [MaNgChng](chỉ đọc); Tên ng/chng [TenNgChng](chỉ đọc); Mã loại VB [MaLoaiVB]{nút …}; Tên loại VB [TenLoaiVB](chỉ đọc)
  - Cột ẩn: Loại văn bằng [IDLoaiVB]; Tên bậc hệ [TenBH](chỉ đọc)
### QLSV_ViewNhapVBSV – View nhap van bang sinh vien
- Lưới 1 «Danh sách văn bằng»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Hệ đào tạo [HeDTVB]{chọn}; Tên bậc đào tạo [BacDTVB]{chọn}; Xếp loại [XepLoaiVB]; Ngành nghề [NganhNgheVB]; Số văn bằng [SOVBSV]; Ngày cấp [NgayCapVB]{ngày}; Th/gian học (tháng) [SoThangVB]; Năm BĐ [NamBDVB]{số}; ID nơi cấp VB [IDDBVB]; Nơi cấp [TruongVB]; Khóa thi [KhoaThiVB]; Điểm TBC [DiemTBC]
### QLSV_ViewNhapVBSV_DHQT – View nhap van bang sinh vien
- Lưới 1 «Danh sách văn bằng»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: VB hệ đào tạo TS [HeDTVBTS]{chọn}; Tên bậc đào tạo [BacDTVB]{chọn}; Xếp loại [XepLoaiVB]; Ngành nghề [NganhNgheVB]; Nơi cấp [TruongVB]; Chuyên ngành [ChNganhNgheVB]; Năm TN [NamTNVB]; Điểm [DiemVB]; Số liệu đơn vị học trình [SoLDVHT]{số}; Số tín chỉ [SoTCCTHoc]{số}
### QLSV_ViewNhapXNTN – View nhap sv xác nhận tốt nghiệp
- Lưới 1 «Danh sách sinh viên xác nhận thông tin tốt nghiệp» (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Phái [Phai]{chọn}(chỉ đọc); Mã lớp [MaLop](chỉ đọc); Xác nhận tốt nghiệp [IsXNTN]
### QLSV_ViewPhanHe_mul – View xử lý chọn phân hệ
- Lưới 1 «Danh sách phân hệ»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã phân hệ [MaPhanHe](chỉ đọc); Tên phân hệ [TenPhanHe](chỉ đọc)
### QLSV_ViewQDTT – Xem quyết định tồn tại
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Số quyết định [SoQDSV]; Ngày lập QĐ [NgayLapQDSV]; Niên học học kỳ [NHHK]; Tên lý do [TenLDQDSV]
### QLSV_ViewQDVAOMoi – View nhap qd vao moi
- Lưới 1 «Danh sách sinh viên»; tắt: Thêm, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Số quyết định [SoQDSV]; Ngày lập QĐ [NgayLapQDSV]{ngày}; Tên quyết định [TenQDSV]; Lý do QĐ [IDLDQDSV]; ID lớp cũ [IDLopCu]; ID lớp mới [IDLopMoi]; Số học kỳ nghỉ [SoHKNghi]
### QLSV_ViewSVHDXH – View nhập sinh viên hoạt động XH
- Lưới 1 «Danh sách sinh viên tham gia»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Mã lớp [MaLop]
### QLSV_ViewThem1SV_NganHan – Thêm mới 1sv ngắn hạn
- Lưới 1 (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Lớp sinh viên [IDLop]; Mã SV [MaSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Phái [Phai]; Quốc tịch [QuocTich]; Số CMND [SoCMND]; Điện thoại 1 [DC_DT1LLSV]; Ghi chú [GcSV]; Diện sinh viên [IDDSV]; Thời gian thâm niên ct [TGianCT]
  - Ô trên form sửa: #IDLop, #MaSV, #TenDayDu, #NgaySinhC, #Phai, #QuocTich, #SoCMND, #DC_DT1LLSV, #GcSV, #IDDSV, #TGianCT
### QLSV_ViewTraHSSV – View cap nhat ho so sinh vien
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Sinh viên [IDSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Phái [Phai]; Mã lớp [MaLop]; Tên lớp [TenLop]; Ghi chú dùng bên detailright [GhiChuView1]
  - Ô trên form sửa: #IDSV, #HoLotSV, #TenSV, #NgaySinhC, #Phai, #MaLop, #TenLop, #GhiChuView1
### QLSV_VIEWTRUYVET – View truy vết đổi mã SV
- Lưới 1 «Thông tin thay đổi mã SV»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Ngày thực hiện [NGAYTHUCHIEN]; User thực hiện [USERTHUCHIEN]; Mã SV [MaSV]
### QLSV_ViewVBSVNew – View cap nhat van bang sinh vien
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Sinh viên [IDSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Phái [Phai]; Mã lớp [MaLop]; Tên lớp [TenLop]; Ghi chú dùng bên detailright [GhiChuView1]
  - Ô trên form sửa: #IDSV, #HoLotSV, #TenSV, #NgaySinhC, #Phai, #MaLop, #TenLop, #GhiChuView1
### QLSV_ViewXemCHHT_Lop – View gán CVHT lop sinh vien
- Lưới 1 «Danh sách sinh viên» (bảng SSVHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Mã viên chức [MaNV](chỉ đọc); Tên đầy đủ [TenDayDuNV](chỉ đọc)
### QLSV_ViewXemDSHB_QTSG – View xem  in danh sach hoc bong
- Lưới 1 «Danh sách sinh viên học bổng»; tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Mã lớp [MaLop]; ĐTB HB [DiemTBHB]; Xếp loại học tập [XLHT]; Điểm rèn luyện học bổng [DiemRLHB]; Xếp loại rèn luyện [XLRL]; Tiền học bổng [TienHB]; Ghi chú HB [GcHBSV]
  - Cột ẩn: Số TC đăng ký [SoTCDK]
### QLSV_ViewXemHDXHSV – View xem cac hoat dong XHSV
- Lưới 1 «Danh sách các hoạt động tham gia»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Mã hoạt động XH [MaHDXH]; Tên hoạt động XH [TenHDXH]; Từ ngày [TuNgayHDXH]{ngày}; Đến ngày [DenNgayHDXH]{ngày}; Địa điểm tổ chức [DiaDiemHDXH]
### QLSV_ViewXemKQXet – View xem ket qua xet ren luyen
- Lưới 1 «Danh sách kết quả xét rèn luyện» (bảng DTOTNG); tắt: Thêm, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã tiêu chuẩn [MaTChuan]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Phái [Phai]; Ngày sinh [NgaySinhC]; Mã lớp [MaLop]; Mã khoa [MaKhoa]; Điểm rèn luyện học kỳ [DiemRLHK]; Xếp loại rèn luyện [XLRL]; Kết quả [KetQuaXet]
### QLSV_ViewXemQDEmpty – View xem quyết định rỗng
- Lưới 1 «Danh sách SV có số quyết định rỗng»; tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Mã lớp [MaLop]; Niên học học kỳ [NHHK]
### QLSV_ViewXemSV – View Xem sinh vien
- Lưới 1 «Danh sách sinh viên» (bảng SSVHK); tắt: Nạp lại, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Phái [Phai]; Mã lớp [MaLop]; Tên lớp [TenLop]; Lớp sinh viên [IDLop]
  - Cột ẩn: Sinh viên [IDSV]
  - Ô trên form sửa: #HoLotSV, #TenSV, #NgaySinhC, #Phai, #IDLop, #IDSV
### QLSV_ViewXuLyMTuy – View xu ly ds ma tuy
- Lưới 1 «Danh sách sinh viên liên quan đến ma túy» (bảng SDSMT); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Hình thức vi phạm [HTVPMT]{chọn}; Hình thức xử lý [HTXLMT]{chọn}; Ngày xử lý [NgayXLMT]{ngày}
  - Cột ẩn: Ghi chú [GcXLMT]; Sinh viên [IDSV]; Mã lớp [MaLop]
  - Ô trên form sửa: #HoLotSV, #TenSV, #HTVPMT, #HTXLMT, #NgayXLMT, #GcXLMT, #IDSV, #MaLop
### QLSV_XuatThongTinSV_Full – View xuat thong tin sv full
- Lưới 1 «Thông tin sinh viên»; tắt: Thêm, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Mã khối [MaKhoi]; Mã lớp [MaLop]; Họ lót [HoLotSV]; Tên [TenSV]; Tên đầy đủ trên VB [TenDayDuVB]; Ngày sinh [NgaySinhC]; Phái [Phai]; Nơi sinh [NoiSinh]; Mã ngân hàng [MaNH]; Tên ngân hàng [TenNH]; Số tài khoản [SoTaiKhoan]; Chi nhánh [CHINHANHNH]; Mã khoa [MaKhoa]; Tên khoa [TenKhoa]; Mã ngành [MaNganh]; Mã Ng/CNg [MaNgChng]; Tên ngành [TenNganh]; Mã bậc hệ [MaBH]; Tên ng/chng [TenNgChng]; Tên bậc hệ [TenBH]; NHHK vào [NHHKVao]; NHHK ra [NHHKRa]; Số quyết định [SoQDSV]; Ngày lập QĐ [NgayLapQDSV]; Tên lý do [TenLDQDSV]; Niên khóa [NienKhoa]; Hiện diện [HienDienSV2]{chọn}; Địa chỉ [DC_DCHK]; Tên dân tộc [TenDT]; Tên tôn giáo [TenTG]; Tên Tỉnh/TP (Hộ khẩu) [TenTPHKh]; Số CMND [SoCMND]; Tên Quận/Huyện [TenQHHKh]; Ngày cấp [NgCapCMND]; Tên Phường/Xã [TenPXHKh]; Nơi cấp [NoiCapCMND]; Số năm bộ đội [SoNamBD]; Số năm TNXP [SoNamTNXP]; Tên cha [TenCha]; Ngày sinh [NgSinhCha]; Số ĐT cha [DC_DT1Cha]; Tên mẹ [TenMe]; Ngày sinh [NgSinhMe]; Số ĐT mẹ [DC_DT1Me]; Số anh chị em [SoAnhChiEm]; Địa chỉ liên lạc [DC_DCLLSV]; Người liên lạc [NguoiLL]; Điện thoại 1 [DC_DT1HK]; Điện thoại 1 [DC_DT1LLSV]; Địa chỉ [DC_DCTT]; Tên chủ hộ [TenChuHo]; Điện thoại 1 [DC_DT1TT]; Phòng ký túc xá [PhongKTX]; Loại cư trú [LoaiCuTru]{chọn}; Thành phần GĐ [ThPhanGD]{chọn}; Nhóm khu vực [NhomKVTS]{chọn}; Đối tượng TS [DOITUONGTS]{chọn}; Số báo danh [SoBD]; Điểm 1 [Diem1]; Điểm 3 [Diem3]; Điểm 2 [Diem2]; Năm tốt nghiệp [NAMTN]; Điểm tổng [DiemTong]; Khối thi [KhoiThi]; Ngành thi [NganhThi]; Email 1 [DC_EML1LLSV]; Email 2 [DC_EML2LLSV]; Loại đoàn thể [LoaiDThe]{chọn}; Hệ đào tạo [HeDTVB]{chọn}; Số văn bằng [SOVBSV]; Điểm TBTN ngoài [DTBTNNG]; Quốc tịch [TenQuocTich]; Ngày nhập học [NgayNHOC]{ngày}; Tên trường THPT 12 [TenTRPT12]; Số vào sổ [SoVaoSOSV]; Tỉnh trường THPT 12 [TenTinhPT12]; Điểm TB Lớp 10 [DMLP10]; Điểm TB Lớp 11 [DMLP11]; Điểm TB Lớp 12 [DMLP12]; Xét tuyển [LoaiPTXT]{chọn}; Thi KTNL [ThiKTNL]; Mã còng [MaCong]; ID SV text [IDSVText]; Mã trường liên kết [MaDP]; Tên trường liên kết [TenDP]
  - Cột ẩn: GC hộ khẩu [DC_GcHK]; GC liên lạc [DC_GcLL]; GC thường trú [DC_GcTT]; GC vợ chồng [DC_GcVC]; Đơn vị đăng ký dự thi [DVDKDTHI]; Học phí đã đóng [DaDongHPHK]; Diem4 [Diem4]; Diem5 [Diem5]; Điểm CCNN [DiemCCNN]; Điểm ưu tiên [DiemUT]; Ghi chú TS [GCTSINH]; Ghi chú [GcSV]; Ghi chú [GcThPhanGD]; Ghi chú HS [GhiChuHS]; Mã Phường/Xã [MaPXHKh]; Mã Quận/Huyện [MaQHHKh]; Mã Tỉnh/TP [MaTPHKh]; NHHKKK [NHHKKK]; Ngày ký [NgayKyKK]; Ngày quyết định vào [NgayQDV]{ngày}; Ngày vào đảng [NgayVDang]{ngày}; Ngày vào đoàn [NgayVDoan]{ngày}; Số quyết định [SoQDKK]; Số QĐ [SoQDV]; Chứng chỉ ngoại ngữ (CCNN) [TenCCNN]; Họ và tên [TenDayDu]
### QLTN_ViewNhapChuyenDe – View nhập chuyên đề tiểu luận tốt nghiệp
- Lưới 1 «Danh sách tiểu luận và chuyên đề NCS» (bảng DChDeNCS); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Số TC [SoTinChi]; Điểm [DiemChDe]; Đạt [DatChDNCS]; Tiểu luận/chuyên đề [LoaiChDe]{chọn}
  - Cột ẩn: Ghi chú [GCChDe]; Sinh viên [IDSV]; Tên chuyên đề [TenChDeNCS]
  - Ô trên form sửa: #HoLotSV, #TenSV, #SoTinChi, #DiemChDe, #DatChDNCS, #LoaiChDe, #GCChDe, #IDSV, #TenChDeNCS
### QLTN_ViewNhapLA – View Show thông tin luân án trước khi lưu
- Lưới 1 «Danh sách dữ liệu thay đổi»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Tên luận văn [TenLNAN]; Ngày bảo vệ [NgayBV]; Điểm luận văn [DiemLNAN]; Phản biện 1 [PhanBien1]; Hướng dẫn 1 [HuongDan1]
  - Cột ẩn: Chủ tịch [ChuTich]; Ngày ký QĐ điều chỉnh ĐT [NgayKyQDDC]; Quyết định điều chỉnh tên đề tài [QDDCTDTLV]; QĐ giao ĐT [QDGiaoDeTai]; Quyết định hội đồng chấm luận văn [QDHDChamLV]; Quyết định thay đổi người hướng dẫn [QDTDNHDLV]; Tình trạng [TinhTrang]
### QLTS_CapNhatMaSV – Cap nhat ten lop tuyen sinh
- Lưới 1 «Thông tin gán mã sinh viên» (bảng TDSTRTUYEN); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV]; Mã lớp [MaLop]{nút …}(chỉ đọc); Mã DS thí sinh [MADSTS](chỉ đọc); Phiếu số (C) [PHIEUSOBGD](chỉ đọc); Phiếu số (code) [PHIEUSO](chỉ đọc); SBD [SBD](chỉ đọc); Mã đợt [MADOTNVTS](chỉ đọc); KV [KV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Phái [Phai]{chọn}(chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Địa chỉ [DC_DCHK](chỉ đọc); Mã ngành [MANGTS](chỉ đọc); Mã khối [MAKHOITS](chỉ đọc); Mã bậc hệ [MaBH]; Điểm 1 [Diem1](chỉ đọc); Điểm 2 [Diem2](chỉ đọc); Điểm 3 [Diem3](chỉ đọc); Mã TP (Hộ khẩu) [MaTPHKh](chỉ đọc); Mã Quận/Huyện (Hộ khẩu) [MaQHHKh](chỉ đọc)
  - Cột ẩn: Số BD trường nộp đơn [SBDCUMPT](chỉ đọc)
### QLTS_CapNhatTenLopTS – Cap nhat ten lop tuyen sinh
- Lưới 1 «Danh sách thí sinh trúng tuyển» (bảng TDSTRTUYEN); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã lớp [MaLop]{nút …}; Phiếu số (C) [PHIEUSOBGD](chỉ đọc); Phiếu số (code) [PHIEUSO](chỉ đọc); SBD [SBD](chỉ đọc); Mã đợt [MADOTNVTS](chỉ đọc); KV [KV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Phái [Phai]{chọn}(chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Địa chỉ [DC_DCHK](chỉ đọc); Mã ngành [MANGTS](chỉ đọc); Mã khối [MAKHOITS](chỉ đọc); Mã TP (Hộ khẩu) [MaTPHKh](chỉ đọc); Mã Quận/Huyện (Hộ khẩu) [MaQHHKh](chỉ đọc); Điểm 1 [Diem1](chỉ đọc); Điểm 3 [Diem3](chỉ đọc); Điểm 2 [Diem2](chỉ đọc)
  - Cột ẩn: Mã DS thí sinh [MADSTS](chỉ đọc); Nguyện vọng [NGUYENVONG]{chọn}(chỉ đọc)
### QLTS_CapNhatThiSinhNhapHoc – Cap nhat thi sinh nhap hoc
- Lưới 1 «Danh sách thí sinh trúng tuyển» (bảng TDSTRTUYEN); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Xác nhận nhập học [IsXNNH]; Số BD trường nộp đơn [SBDCUMPT](chỉ đọc); Ghi chú [GCNHAPHOC]; Mã SV [MaSV](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Phiếu số (code) [PHIEUSO](chỉ đọc); Phiếu số (C) [PHIEUSOBGD](chỉ đọc); Mã đợt [MADOTNVTS](chỉ đọc); KV [KV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Phái [Phai]{chọn}(chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Địa chỉ [DC_DCHK](chỉ đọc); Mã ngành [MANGTS](chỉ đọc); Mã khối [MAKHOITS](chỉ đọc); Mã bậc hệ [MaBH](chỉ đọc); Điểm 1 [Diem1](chỉ đọc); Điểm 2 [Diem2](chỉ đọc); Điểm 3 [Diem3](chỉ đọc); Mã TP (Hộ khẩu) [MaTPHKh](chỉ đọc); Mã Quận/Huyện (Hộ khẩu) [MaQHHKh](chỉ đọc); Email 1 [DC_EML1LLSV](chỉ đọc); Số CMND [SoCMND](chỉ đọc); Đã gửi mail [DaGuiMail](chỉ đọc)
  - Cột ẩn: Đã chuyển vào qlsv [CHUYENQLSV](chỉ đọc); TN THPT [CO_TN](chỉ đọc); Mã DS thí sinh [MADSTS](chỉ đọc); Từ ngày nhập học [NGAYGIONH]{ngày}(chỉ đọc); Nguyện vọng [NGUYENVONG]{chọn}(chỉ đọc); SBD [SBD](chỉ đọc)
### QLTS_Import_TDSTS – View dung de lay thong danh sach thi sinh
- Lưới 1 (bảng TDSTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã DS thí sinh [MADSTS]; Phiếu số (C) [PHIEUSOBGD]
### QLTS_NhapDiemThi – Nhập điểm thi tuyển sinh
- Lưới 1 «Danh sách môn» (bảng TDSTSMON); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn [MAMONTS](chỉ đọc); Tên môn [TENMONTS](chỉ đọc); Điểm môn thi [DIEMMON]{số}; Điểm QG [IsDiemQG]
### QLTS_NhapNhanh_CTTD – view nhap thong tin ho so thi sinh
- Lưới 1 (bảng TDSTS); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Phiếu số (C) [PHIEUSOBGD]; Họ lót [HoLotSV]; Tên [TenSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Phái [Phai]; Đối tượng TS [DOITUONGTS]; Nhóm khu vực [NhomKVTS]; Nơi sinh [NoiSinh]; Số CMND [SoCMND]; Ngày cấp [NgayCap]; Nơi cấp [NoiCapCMND]; Chương trình giảng dạy [LoaiCTGD]{chọn}; Thiếu học bạ [IsNotHB]; Thiếu phiếu điểm [IsNotDiem]; Thiểu giấy CN TN [IsNotCNTN]
  - Cột ẩn: Địa chỉ [DC_DCHK]; Địa chỉ 2 [DC_DCHK2]; Địa chỉ liên lạc [DC_DCLLSV]; Địa chỉ 2 [DC_DCLLSV2]; Số ĐT cha [DC_DT1Cha]; Điện thoại 1 [DC_DT1LLSV]; Số ĐT mẹ [DC_DT1Me]; Điện thoại 2 [DC_DT2LLSV]; Email 1 [DC_EML1LLSV]; Email 2 [DC_EML2LLSV]; Tỉnh/thành [DC_IDDBHK]; Tỉnh/thành [DC_IDDBLL]; Điểm HK1 lớp 10 [DMHK1LP10]; Điểm HK1 lớp 11 [DMHK1LP11]; Điểm HK1 lớp 12 [DMHK1LP12]; Điểm HK2 lớp 10 [DMHK2LP10]; Điểm HK2  lớp 11 [DMHK2LP11]; Điểm HK2  lớp 12 [DMHK2LP12]; Điểm TB Lớp 10 [DMLP10]; Điểm TB Lớp 11 [DMLP11]; Điểm TB Lớp 12 [DMLP12]; Ghi chú hồ sơ [GCDSTS]; Ghi chú dùng bên detailright [GhiChuView1]; Ghi chú dùng bên detailright 2 [GhiChuView2]; Hạnh kiểm HK1L12 [HKiemHK1LP12]{chọn}; Hạnh kiểm [HanhKiem]{chọn}; Học lực [HocLuc]{chọn}; Đợt XT [IDDOTNVTS]; Dân tộc [IDDT]; Phương thức [IDPTXT]; Tôn giáo [IDTG]; Lớp 10 [LOP10]; Lớp 11 [LOP11]; Lớp 12 [LOP12]; Mã DS thí sinh [MADSTS]; Năm tốt nghiệp [NAMTN]; Ngày cấp [NgayCapVB]; Ngày thêm [NgayThem]{ngày}; Người liên lạc [NguoiLL]; Nhóm ưu tiên [NhomUT]; Nơi cấp VBSV [NoiCapVBSV]; SBD [SBD]; Số văn bằng [SOVBSV]; Tên trường tự do [TENLOP10]; Tên trường tự do [TENLOP11]; Tên trường tự do [TENLOP12]; Tên trường PT [TENTRPT]; Tên trường PT [TENTRPT2]; Tên trường PT [TENTRPT3]
  - Ô trên form sửa: #PHIEUSOBGD, #TenDayDu, #NgaySinhC, #Phai, #DOITUONGTS, #NhomKVTS, #IsNotHB, #IsNotDiem, #IsNotCNTN, #DC_DCHK, #DC_DCLLSV, #DC_DT1LLSV, #DC_EML1LLSV, #DC_IDDBHK, #DC_IDDBLL, #GhiChuView1, #GhiChuView2, #IDDOTNVTS, #IDPTXT, #LOP10, #LOP11, #LOP12, #TENTRPT, #TENTRPT2, #TENTRPT3
### QLTS_NhapNV – View danh sach nhap nguyen vong
- Lưới 1 «Danh sách thí sinh» (bảng TDSTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã DS thí sinh [MADSTS]; Phiếu số (C) [PHIEUSOBGD]; Họ lót [HoLotSV]; Tên [TenSV]; Phái [Phai]{chọn}; Ngày sinh [NgaySinhC]; Số CMND [SoCMND]; Điểm TB Lớp 10 [DMLP10]; Điểm TB Lớp 11 [DMLP11]; Điểm TB Lớp 12 [DMLP12]; Số BD trường nộp đơn [SBDCUMPT]; Phiếu số (code) [PHIEUSO]; Ghi chú dùng bên detailright [GhiChuView1]
  - Ô trên form sửa: #GhiChuView1
### QLTS_ViewCapNhatNhapHocBo – Cap nhat thi sinh nhap hoc cua bo
- Lưới 1 «Danh sách xác nhân nhập học của bộ» (bảng TDSTRTUYEN); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: xác nhận NH bộ [IsXNNHBO]; Mã SV [MaSV](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Phiếu số (C) [PHIEUSOBGD](chỉ đọc); Số CMND [SoCMND](chỉ đọc); Mã đợt [MADOTNVTS](chỉ đọc); KV [KV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Phái [Phai]{chọn}(chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Email 1 [DC_EML1LLSV](chỉ đọc); Địa chỉ [DC_DCHK](chỉ đọc); Mã ngành [MANGTS](chỉ đọc); Mã khối [MAKHOITS](chỉ đọc); Mã bậc hệ [MaBH](chỉ đọc); Điểm 1 [Diem1](chỉ đọc); Điểm 2 [Diem2](chỉ đọc); Điểm 3 [Diem3](chỉ đọc); Mã Quận/Huyện (Hộ khẩu) [MaQHHKh](chỉ đọc); Mã TP (Hộ khẩu) [MaTPHKh](chỉ đọc)
### QLTS_ViewChonCumPT – View chon cum pho thong
- Lưới 1 «Danh sách cụm thi phổ thông» (bảng TDMCUMPT); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã cụm thi PT [MACUMPT]; Tên cụm thi PT [TENCUMPT]; Viết tắt [VTCUMPT]; Nhóm khu vực [NhomKVTS]{chọn}
### QLTS_ViewChonCumThi – View chon cum thi
- Lưới 1 «Danh sách cụm thi» (bảng TDSCUMTHI); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã cụm thi [MACUMTHI]; Tên cụm thi [TENCUMTHI]
### QLTS_ViewChonHoiDong – View chon hoi dong
- Lưới 1 «Danh sách hội đồng» (bảng THDGK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã hội đồng [MAHDGK]; Tên hội đồng giám khảo [TENHDGK]
### QLTS_ViewChonHSMul – View chon ho so nhieu
- Lưới 1 «Danh sách hồ sơ»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã hồ sơ [MaHS]; Tên hồ sơ [TenHS]; Thứ tự [TTHs]
### QLTS_ViewChonHSMul_A – View chon ho so nhieu có ảnh hồ sơ
- Lưới 1 «Danh sách hồ sơ»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã hồ sơ [MaHS](chỉ đọc); Tên hồ sơ [TenHS](chỉ đọc); Thứ tự [TTHs](chỉ đọc); Đã nộp bản chính [IsBanGoc]; Xem ảnh [XemFile](chỉ đọc)
### QLTS_ViewChonHSMul_N – View chon ho so nhieu co hiên thi ngày nop HS
- Lưới 1 «Danh sách hồ sơ»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã hồ sơ [MaHS]; Tên hồ sơ [TenHS]; Thứ tự [TTHs]; Ngày nộp hồ sơ [NgayNopHS]{ngày}
### QLTS_ViewChonKhoanThuMul – View chon khoan thu mul
- Lưới 1 «Danh sách khoản đóng»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khoản thu [MaKhThu]; Tên khoản thu [TenKhThu]; Số tiền [SoTien]
### QLTS_VIEWCHONKYTS – View chon ky tuyển sinh
- Lưới 1 «Chọn danh sách kỳ tuyển sinh đồng bộ của học kỳ trước»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã kỳ TS [MaKyTS]; Tên kỳ TS [TenKyTS]
### QLTS_ViewChonMonHoc – View chọn môn học
- Lưới 1 «Danh sách môn thi» (bảng TDMMONTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn [MAMONTS]; Tên môn [TENMONTS]; Ngày thi [NGAYTHITS]{ngày}; Số sinh viên [SoSV]; Mã phòng thi [MAPHTHI]
### QLTS_ViewChonMonTS – Chọn môn tuyển sinh
- Lưới 1 (bảng TDSMONTS); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn [MAMONTS](chỉ đọc); Tên môn TS [TENMONDS](chỉ đọc); Điểm môn thi [DIEMMON]
### QLTS_ViewChonNgayThi – View chon ngay thi
- Lưới 1 «Danh sách ngày thi»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Ký hiệu ghép [MAGRPTS]; Ghi chú nội dung thi [GCGRPTSCT]; Ngày thi [NGAYTHITS]{ngày}; Buổi thi thứ [BUOITHITHU]
### QLTS_ViewChonNgKh – View chon nganh khoi tuyen sinh
- Lưới 1 «Danh sách ngành khối»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã ngành [MANGTS]; Tên ngành [TENNGTS]; Mã khối [MAKHOITS]
### QLTS_ViewChonNhomThi – View chon nhom thi chung
- Lưới 1 «Danh sách nhóm thi» (bảng TGRPTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Ký hiệu ghép [MAGRPTS]; Tên nhóm môn thi chung [TENGRPTS]; Hình thức thi [HTTHITS]{chọn}; Mã môn [MAMONTS]; Tên môn [TENMONTS]
### QLTS_ViewchonPhongThi – View chon phong thi
- Lưới 1 «Danh sách phòng thi» (bảng TPHTHI); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã phòng thi [MAPHTHI]; Tên phòng thi [TENPHTHI]
### QLTS_VIEWCHONPT1 – Chon phuong thuc 1
- Lưới 1 «Danh sách phương thức»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã phương thức [MaPTXT]; Viết tắt [VTPTXT]; Tên phương thức [TenPTXT]; Ghi chú [GCPTXT]
### QLTS_ViewChonTrungTamThi – View chon trung tam thi
- Lưới 1 «Danh sách trung tâm thi» (bảng TDSTTTHI); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã trung tâm [MATTTHI]; Tên trung tâm [TENTTTHI]
### QLTS_ViewChonTruongPT – View chon truong pho thong
- Lưới 1 «Danh sách trường phổ thông»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã trường PT [MATRPT]; Tên trường PT [TENTRPT]; Mã địa bàn [MaDB]; Tên địa bàn [TenDB]
### QLTS_ViewchonTS – View chon thi sinh
- Lưới 1 «Danh sách thí sinh» (bảng TDSTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: SBD [SBD]; Mã DS thí sinh [MADSTS]; Họ lót [HoLotSV]; Tên [TenSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Phái [Phai]{chọn}
### QLTS_ViewChonTSTT – View chon thi sinh trung tuyen
- Lưới 1 «Danh sách thí sinh trúng tuyển»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Phiếu số (C) [PHIEUSOBGD]; Mã DS thí sinh [MADSTS]; Số BD trường nộp đơn [SBDCUMPT]; Phiếu số (code) [PHIEUSO]; Mã lớp [MaLop]; Mã SV [MaSV]; Số GBTT [SOGBTT]; Họ lót [HoLotSV]; Tên [TenSV]; Phái [Phai]{chọn}; Ngày sinh [NgaySinhC]; Mã ngành [MANGTS]; Tên ngành [TENNGTS]; Mã khối [MAKHOITS]; Tên khối [TENKHOITS]; NV ưu tiên [UUTIENNV]; TN THPT [CO_TN]; Mã đợt [MADOTNVTS]; Ghi chú [GCNHAPHOC]
### QLTS_ViewChuyenDsTrungTuyen – Danh sách sinh viên trúng tuyển chuyển QLSV
- Lưới 1 «Danh sách thí sinh trúng tuyển» (bảng TDSTRTUYEN); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV](chỉ đọc); Phiếu số (C) [PHIEUSOBGD](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Phái [Phai](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Tên lớp [TenLop](chỉ đọc); Loại HP và có in trên Phiếu thu [LoaiHP](chỉ đọc); Tổng tiền [TongTien](chỉ đọc); Đã chuyển [DaChuyen](chỉ đọc); Đã chuyển vào qlsv [CHUYENQLSV](chỉ đọc)
### QLTS_ViewDMNgTS – View danh mục ngành TS dạng cậy
- Lưới 1 «Danh mục ngành tuyển sinh» (bảng TDMNGTS); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã ngành [MANGTS]; Tên ngành [TENNGTS]; Tên tiếng anh [TENNGTSEG]; Viết tắt [VTNGTS]
  - Cột ẩn: Ghi chú [GCNGTS]; GCNGTSEg [GCNGTSEg]; Ngành TS cha [IDNGTSP](chỉ đọc); Mã số NgTS [MASONGTS]
  - Ô trên form sửa: #MANGTS, #TENNGTS, #TENNGTSEG, #VTNGTS, #GCNGTS, #GCNGTSEg, #IDNGTSP
### QLTS_ViewDSCumPT – View danh sach cum pho thong
- Lưới 1 «Danh sách cụm phổ thông» (bảng TDSCUMPT); tắt: Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã cụm thi PT [MACUMPT](chỉ đọc); Tên cụm thi PT [TENCUMPTDS]; Viết tắt [VTDSCUMPT]; Ghi chú [GCDSCUMPT]
### QLTS_ViewDSNotHL – View danh sách thí sinh không hợp lệ
- Lưới 1 «Danh sách thí sinh không hợp lệ» (bảng TDSKGHL); tắt: Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: SBD [SBD]; Số CMND [SoCMND]; Họ và tên [TenDayDu]; Phái [Phai]; Lý do [GCKGHL]; Ngày sinh [NgaySinhC]
  - Ô trên form sửa: #SBD, #TenDayDu, #Phai, #GCKGHL, #NgaySinhC
### QLTS_ViewDSNVong_TuDong – Danh sach dang ky thi sinh nguyen vong tu dong
- Lưới 1 «Danh sách thí sinh» (bảng TDSTSNV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã DS thí sinh [MADSTS]; Họ lót [HoLotSV]; Tên [TenSV]; Phái [Phai]; Ngày sinh [NgaySinhC]; Nhóm khu vực [NhomKVTS]{chọn}; Đối tượng TS [DOITUONGTS]{chọn}; Loại hồ sơ tuyển sinh [LOAIHOSOTS]{chọn}; Mã ngành [MANGTS]; Mã khối [MAKHOITS]; Mã bậc hệ [MaBH]; Điểm tổng các môn [DIEMTCNV]; Điểm ưu tiên [DIEMUTKVDT]; Điểm cộng XT [DIEMCONGXT]
### QLTS_ViewEditTrungTuyen – view nhap thong tin trung tuyen
- Lưới 1 (bảng TDSTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Phiếu số (C) [PHIEUSOBGD]; Họ lót [HoLotSV]; Tên [TenSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Phái [Phai]; Đối tượng TS [DOITUONGTS]; Nhóm khu vực [NhomKVTS]; Nơi sinh [NoiSinh]; Loại đoàn thể [LoaiDThe]; Nguồn tuyển [NguonTuyen]; Dân tộc [IDDT]; Số CMND [SoCMND]; Ngày cấp [NgayCap]; Nơi cấp [NoiCapCMND]; Địa chỉ [DC_DCHK]; Địa chỉ 2 [DC_DCHK2]; Tỉnh/thành [DC_IDDBHK]; Địa chỉ liên lạc [DC_DCLLSV]; Tỉnh/thành [DC_IDDBLL]; Email 1 [DC_EML1LLSV]; Điện thoại 1 [DC_DT1LLSV]; Tên mẹ [TenMe]; Tên cha [TenCha]; Nghề nghiệp [NNgMe]; Nghề nghiệp [NNgCha]; Điểm tổng [DiemTong]; Ghi chú hồ sơ [GCDSTS]; Tôn giáo [IDTG]; Người liên lạc [NguoiLL]; Tên ngành [TENNGTS]; Ghi chú hồ sơ 2 [GCDSTS2]; Điểm 1 [Diem1]; Điểm 2 [Diem2]; Điểm 3 [Diem3]; Lớp 10 [LOP10]; Lớp 11 [LOP11]; Lớp 12 [LOP12]; Ngành tuyển sinh [IDNGTS]; Khối tuyển sinh [IDKHOITS]; Học bạ THPT [CO_HB]; TN THPT [CO_TN]; Tên trường PT [TENTRPT]; Tên trường PT [TENTRPT2]; Tên trường PT [TENTRPT3]; Mã DS thí sinh [MADSTS]; Nhóm ưu tiên [NhomUT]; Tên trường tự do [TENLOP10]; Tên trường tự do [TENLOP11]; Tên trường tự do [TENLOP12]; Đã Kiểm dò TT [DaInKiemDoThanhTra]; Diện trúng tuyển [DienTT]; Bậc hệ [IDBH]; Mã SV [MaSV]; Lớp sinh viên [IDLop]; THPT [THPT]; Đã chuyển vào qlsv [CHUYENQLSV]
  - Ô trên form sửa: #PHIEUSOBGD, #HoLotSV, #TenSV, #TenDayDu, #NgaySinhC, #Phai, #DOITUONGTS, #NhomKVTS, #NoiSinh, #IDDT, #SoCMND, #NgayCap, #NoiCapCMND, #DC_DCHK, #DC_IDDBHK, #DC_DCLLSV, #DC_IDDBLL, #DC_DT1LLSV, #Diem1, #Diem2, #Diem3, #LOP10, #LOP11, #LOP12, #IDNGTS, #IDKHOITS, #CO_HB, #CO_TN, #TENTRPT, #TENTRPT2, #TENTRPT3, #IDBH, #MaSV, #IDLop, #THPT, #CHUYENQLSV
### QLTS_ViewGanDBTT – Gan giay bao trung tuyen
- Lưới 1 «Danh sách thí sinh trúng tuyển» (bảng TDSTRTUYEN); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số GBTT [SOGBTT](chỉ đọc); Mã SV [MaSV](chỉ đọc); Mã lớp [MaLop]{nút …}(chỉ đọc); Mã DS thí sinh [MADSTS](chỉ đọc); SBD [SBD](chỉ đọc); Phiếu số (C) [PHIEUSOBGD](chỉ đọc); Phiếu số (code) [PHIEUSO](chỉ đọc); Mã đợt [MADOTNVTS](chỉ đọc); KV [KV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Phái [Phai]{chọn}(chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Địa chỉ [DC_DCHK](chỉ đọc); Mã ngành [MANGTS](chỉ đọc); Mã khối [MAKHOITS](chỉ đọc); Mã bậc hệ [MaBH](chỉ đọc); Ghi chú [GCNHAPHOC]; Điểm 1 [Diem1](chỉ đọc); Điểm 2 [Diem2](chỉ đọc); Điểm 3 [Diem3](chỉ đọc); Mã TP (Hộ khẩu) [MaTPHKh](chỉ đọc); Mã Quận/Huyện (Hộ khẩu) [MaQHHKh](chỉ đọc); Từ ngày nhập học [NGAYGIONH]{ngày}(chỉ đọc); Đến ngày nhập học [DENNGAYGIONH]{ngày}(chỉ đọc); TN THPT [CO_TN](chỉ đọc)
  - Cột ẩn: Nguyện vọng [NGUYENVONG]{chọn}(chỉ đọc); Số BD trường nộp đơn [SBDCUMPT](chỉ đọc)
### QLTS_ViewGanMaSV – View gan ma sv
- Lưới 1 «Danh sách đối tượng gán»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã bậc hệ [MaBH](chỉ đọc); Tên bậc hệ [TenBH](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Mã khối [MaKhoi](chỉ đọc); Tên lớp [TenLop](chỉ đọc); Tên khối [TenKhoi](chỉ đọc); Mã ngành [MANGTS](chỉ đọc); Tên ngành [TENNGTS](chỉ đọc); Số lượng [SoLuong](chỉ đọc); SL đã gán [SoLuongDGan](chỉ đọc); SL chưa gán [SoLuongCGan](chỉ đọc); Mã SV gán tiếp theo [MaSVDT]
### QLTS_ViewGanTenLop – View gan ten lop
- Lưới 1 «Danh sách lớp»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]; Mã ngành [MANGTS]; Tên ngành [TENNGTS]; Mã lớp [MaLop]; SL trúng tuyển [SoLuongTT]; Số SV dự kiến phân bổ [SOSVDKPB]; SL đã gán [SoLuongDGan]; SL chưa gán [SoLuongCGan]
  - Cột ẩn: Tên lớp [TenLop]
### QLTS_ViewHuyTenLop – View huy ten lop
- Lưới 1 «Danh lớp hủy»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Mã ngành [MANGTS]; Tên ngành [TENNGTS]; Mã lớp [MaLop]; Tên lớp [TenLop]; Số lượng [SoLuong]
### QLTS_ViewImpHoSo – Import ho so
- Lưới 1 (bảng TDSTRTUYEN); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]
### QLTS_ViewImpHS_PhSo – Import ho so theo PhieuSoBGD
- Lưới 1 (bảng TDSTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Phiếu số (C) [PHIEUSOBGD]
### QLTS_ViewImpKTHU_TN – Import khoan thu tu nguyen
- Lưới 1 (bảng TDSTRTUYEN); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Số phiếu [SoPhieu]; Ngày đóng [NgayDong]; Thu ngân hàng [THUNH]
### QLTS_ViewImpKTHUNH – Import khoan thu tu ngan hang
- Lưới 1 (bảng TDSTRTUYEN); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Số phiếu [SoPhieu]; Số phiếu 2 [SoPhieu2]; Số phiếu 3 [SoPhieu3]; Số tiền [SoTien]; Ngày đóng [NgayDong]; Thu ngân hàng [THUNH]
### QLTS_ViewImpLePhiXT – Import lệ phí xét tuyển
- Lưới 1 (bảng TDSTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số CMND [SoCMND]; Mã phương thức [MaPTXT]; Ngày đóng [NgayDong]
### QLTS_ViewImpNganhHPMon – Import danh sach ngành hp môn hoc
- Lưới 1 (bảng TNGHPMH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã ngành [MANGTS]; Mã môn học [MaMH]; Hệ số [HeSoMH]; Đơn giá [DonGiaMH]; Phí tài liệu [PhiTaiLieu]
### QLTS_ViewImPortDiemOnThi – View import diem on thi
- Lưới 1 (bảng TONTHI); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### QLTS_ViewImportLopDTT – Import lop dien trung tuyen
- Lưới 1 (bảng SDMLOP); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]
### QLTS_ViewImportNgKhMon – Import nganh khoi mon
- Lưới 1 (bảng TNGKH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã ngành [MANGTS]; Mã khối [MAKHOITS]
### QLTS_ViewImtKhoMon – Import khoi mon
- Lưới 1 (bảng TDMKHOITS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MAKHOITS]
### QLTS_ViewMonHocPhucTra – Danh sách môn học phúc tra
- Lưới 1 «Danh sách môn học phúc tra»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn [MAMONTS]; Tên môn [TENMONTS]
### QLTS_ViewNganhHocPhi – View nhap nganh hoc phi mh
- Lưới 1 «Danh sách ngành» (bảng TNGHPMH); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã ngành [MANGTS]; Tên ngành [TENNGTS]
  - Cột ẩn: Ghi chú dùng bên detailright [GhiChuView1]; Ngành tuyển sinh [IDNGTS]
  - Ô trên form sửa: #TENNGTS, #GhiChuView1, #IDNGTS
### QLTS_ViewNhapBoSungTT – view nhap thong tin ho so thi sinh
- Lưới 1 (bảng TDSTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Phiếu số (C) [PHIEUSOBGD]; Họ lót [HoLotSV]; Tên [TenSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Phái [Phai]; Đối tượng TS [DOITUONGTS]; Nhóm khu vực [NhomKVTS]; Nơi sinh [NoiSinh]; Loại đoàn thể [LoaiDThe]; Nguồn tuyển [NguonTuyen]; Dân tộc [IDDT]; Số CMND [SoCMND]; Ngày cấp [NgayCap]; Nơi cấp [NoiCapCMND]; Địa chỉ [DC_DCHK]; Địa chỉ 2 [DC_DCHK2]; Tỉnh/thành [DC_IDDBHK]; Địa chỉ liên lạc [DC_DCLLSV]; Tỉnh/thành [DC_IDDBLL]; Email 1 [DC_EML1LLSV]; Điện thoại 1 [DC_DT1LLSV]; Tên mẹ [TenMe]; Tên cha [TenCha]; Nghề nghiệp [NNgMe]; Nghề nghiệp [NNgCha]; Điểm tổng [DiemTong]; Ghi chú hồ sơ [GCDSTS]; Tôn giáo [IDTG]; Người liên lạc [NguoiLL]; Tên ngành [TENNGTS]; Ghi chú hồ sơ 2 [GCDSTS2]; Điểm 1 [Diem1]; Điểm 2 [Diem2]; Điểm 3 [Diem3]; Lớp 10 [LOP10]; Lớp 11 [LOP11]; Lớp 12 [LOP12]; Ngành tuyển sinh [IDNGTS]; Khối tuyển sinh [IDKHOITS]; Học bạ THPT [CO_HB]; TN THPT [CO_TN]; Tên trường PT [TENTRPT]; Tên trường PT [TENTRPT2]; Tên trường PT [TENTRPT3]; Mã DS thí sinh [MADSTS]; Nhóm ưu tiên [NhomUT]; Tên trường tự do [TENLOP10]; Tên trường tự do [TENLOP11]; Tên trường tự do [TENLOP12]; Đã Kiểm dò TT [DaInKiemDoThanhTra]; Diện trúng tuyển [DienTT]; Mã SV [MaSV]; Từ ngày nhập học [NGAYGIONH]; Đến ngày nhập học [DENNGAYGIONH]; Ngày bổ sung [NgayBSTN]
  - Ô trên form sửa: #PHIEUSOBGD, #TenDayDu, #NgaySinhC, #Phai, #NoiSinh, #IDDT, #SoCMND, #NgayCap, #NoiCapCMND, #DC_DCHK, #DC_IDDBHK, #GCDSTS, #Diem1, #Diem2, #Diem3, #IDNGTS, #IDKHOITS, #CO_TN, #DaInKiemDoThanhTra, #MaSV, #NGAYGIONH, #DENNGAYGIONH, #NgayBSTN
### QLTS_ViewNhapDiemMonOnThi – View nhập  diem môn học thi
- Lưới 1 «Danh sách môn ôn thi» (bảng TDMMONTS); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn [MAMONTS](chỉ đọc); Tên môn [TENMONTS](chỉ đọc); Điểm ôn thi [DIEMONTHI]
### QLTS_ViewNhapDiemOnThi – View nhap ho so on thi
- Lưới 1 «Danh sách thí sinh» (bảng TONTHI); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã DS thí sinh [MADSTS]; SBD [SBD]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày nộp hs [NGAYGIOHSOT]{ngày}; Ghi chú dùng bên detailright [GhiChuView1]
  - Cột ẩn: Ghi chú [GCHSONTHI]; Họ và tên [TenDayDu]
  - Ô trên form sửa: #MADSTS, #SBD, #HoLotSV, #TenSV, #NGAYGIOHSOT, #GhiChuView1, #GCHSONTHI, #TenDayDu
### QLTS_ViewNhapDiemThiXetTuyen – View nhap diem thi xet tuyen
- Lưới 1 «Danh sách môn học»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn [MAMONTS](chỉ đọc); Điểm HK1_10 [K1_10]; Điểm HK1_11 [K1_11]; Điểm HK1_12 [K1_12]; Điểm HK2_10 [K2_10]; Điểm HK2_11 [K2_11]; Điểm HK2_12 [K2_12]; Lớp 10 [T_10]; Lớp 11 [T_11]; Lớp 12 [T_12]; Điểm THPTQG [THPTQG]; Điểm ĐH/Ths [DHTHS]
### QLTS_ViewNhapDotNVong – Nhap nguyen vong dang danh sach
- Lưới 1 «Danh sách thi sinh nguyện vọng» (bảng TDSTSNV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Phiếu số (C) [PHIEUSOBGD](chỉ đọc); Số CMND [SoCMND](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Phái [Phai]{chọn}(chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); NV ưu tiên [UUTIENNV](chỉ đọc); Mã khối [MAKHOITS]{nút …}(chỉ đọc); Mã ngành [MANGTS]{nút …}(chỉ đọc); Mã đợt [MADOTNVTS]{nút …}; Điểm tổng các môn [DIEMTCNV](chỉ đọc); Điểm ưu tiên [DIEMUTKVDT](chỉ đọc); Điểm cộng XT [DIEMCONGXT](chỉ đọc)
  - Cột ẩn: Điểm công [DIEMCONG](chỉ đọc); Điểm cụm thi [DIEMCUMTHI](chỉ đọc); Điểm trừ [DIEMTRU](chỉ đọc); Mã DS thí sinh [MADSTS](chỉ đọc); Mã bậc hệ [MaBH](chỉ đọc); Mã phương thức [MaPTXT](chỉ đọc); Ngày nộp hồ sơ [NGAYNOPTS]{ngày}(chỉ đọc); Ngày rút hồ sơ [NGAYRUTTS]{ngày}(chỉ đọc); Nguyện vọng [NGUYENVONG]{chọn}(chỉ đọc); SBD [SBD](chỉ đọc)
### QLTS_ViewNhapGanMaSV – View nhap gan ma sv
- Lưới 1 «Danh sách đối tượng gán» (bảng TGANMASV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã lớp [MaLop](chỉ đọc); Tên lớp [TenLop](chỉ đọc); Mã khối [MaKhoi](chỉ đọc); Tên khối [TenKhoi](chỉ đọc); Mã SV đầu tiên [MaSVDT]{số}; Mã SV tiếp theo [MaSVTT]{số}(chỉ đọc)
### QLTS_ViewNhapHoSoOnThi – View nhap ho so on thi
- Lưới 1 «Danh sách hồ sơ ôn thi» (bảng THSONTHI); tắt: Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã DS thí sinh [MADSTS]; SBD [SBD]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày nộp hs [NGAYGIOHSOT]{ngày}; Ghi chú dùng bên detailright [GhiChuView1]
  - Cột ẩn: Ghi chú [GCHSONTHI]; Mã thí sinh [IDDSTS]; Họ và tên [TenDayDu]
  - Ô trên form sửa: #SBD, #HoLotSV, #TenSV, #NGAYGIOHSOT, #GhiChuView1, #GCHSONTHI, #IDDSTS, #TenDayDu
### QLTS_ViewNhapHPMH – Nhap hoc phi mon hoc
- Lưới 1 «Danh sách môn học» (bảng TNGHPMH); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Hệ số [HeSoMH]; Đơn giá [DonGiaMH]; Học phí [HocPhiMH](chỉ đọc); Phí tài liệu [PhiTaiLieu]
### QLTS_ViewNhapHPTS – View nhap hoc phi tuyen sinh
- Lưới 1 (bảng TDONGHPTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Số phiếu 2 [SoPhieu2]; Họ và tên [TenDayDu]; Mã lớp [MaLop]; Số phiếu [SoPhieu]; Ngày đóng [NgayDong]; Tổng tiền [TongTien]; Ghi chú dùng bên detailright 2 [GhiChuView2]; Số phiếu 3 [SoPhieu3]
  - Ô trên form sửa: #MaSV, #SoPhieu2, #TenDayDu, #MaLop, #SoPhieu, #NgayDong, #TongTien, #GhiChuView2, #SoPhieu3
### QLTS_ViewNhapHPTSCopy – View nhap hoc phi tuyen sinh
- Lưới 1 (bảng TDONGHPTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Số phiếu 2 [SoPhieu2]; Họ và tên [TenDayDu]; Mã lớp [MaLop]; Số phiếu [SoPhieu]; Ngày đóng [NgayDong]; Tổng tiền [TongTien]; Ghi chú dùng bên detailright 2 [GhiChuView2]; Số phiếu 3 [SoPhieu3]; Số CMND [SoCMND]; Phái [Phai]{chọn}
  - Ô trên form sửa: #TenDayDu, #SoPhieu, #NgayDong, #TongTien, #GhiChuView2, #SoCMND, #Phai
### QLTS_ViewNhapHSTS – View nhap ho so tuyen sinh
- Lưới 1 (bảng THOSOTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Mã lớp [MaLop]; Ngày nộp hồ sơ [NgayNopHS]; Ghi chú dùng bên detailright 2 [GhiChuView2]; Số HS [SoHoSo]
  - Ô trên form sửa: #MaSV, #TenDayDu, #NgaySinhC, #MaLop, #NgayNopHS, #GhiChuView2, #SoHoSo
### QLTS_ViewNhapMHRut – View nhập  môn học rút
- Lưới 1 «Danh sách môn thi» (bảng TDMMONTS); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn [MAMONTS](chỉ đọc); Tên môn [TENMONTS](chỉ đọc); Rút [NHAPRUTOT]
### QLTS_ViewNhapNganhKhoiNV – View nhap nganh khoi nguyen vong
- Lưới 1 «Danh sách ngành đăng ký»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: NV ưu tiên [UUTIENNV]; Mã ngành [MANGTS]{nút …}; Mã khối [MAKHOITS]{nút …}; Tên ngành [TENNGTS](chỉ đọc)
### QLTS_ViewNhapNganhKhoiNVDot – View nhap nganh khoi nguyen vong Dot
- Lưới 1 «Danh sách nguyện vọng»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: NV ưu tiên [UUTIENNV]; Mã ngành [MANGTS]{nút …}; Mã khối [MAKHOITS]{nút …}; Tên ngành [TENNGTS](chỉ đọc); Mã đợt [MADOTNVTS]{nút …}
### QLTS_ViewNhapNganhKhoiXT – View nhap nganh khoi xet tuyen
- Lưới 1 «Danh sách ngành khối xét tuyển» (bảng TNGKHTD); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Nguyện vọng TS [NVTS]{chọn}; Mã ngành [MANGTS]; Tên ngành [TENNGTS]; Mã khối [MAKHOITS]; Tên khối [TENKHOITS]; Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]; NV ưu tiên [UUTIENNV]; Nguyện vọng XT [NVXT]{chọn}; Ghi chú [GCNGKHTD]; Mã ngành XT [MANGXT]; Tên ngành XT [TENNGXT]; Mã khối XT [MAKHOIXT]; Tên khối XT [TENKHOIXT]; Mã BH XT [MaBHXT]; Tên BH XT [TenBHXT]
  - Cột ẩn: Bậc hệ [IDBHTS]; Bậc hệ [IDBHXT]; Khối tuyển sinh [IDKHOITS]; Mã khối XT [IDKHOIXT]; Ngành tuyển sinh [IDNGTS]; Mã ngành XT [IDNGXT]
  - Ô trên form sửa: #NVTS, #TENNGTS, #TENKHOITS, #TenBH, #UUTIENNV, #NVXT, #GCNGKHTD, #TENNGXT, #TENKHOIXT, #TenBHXT, #IDBHTS, #IDBHXT, #IDKHOITS, #IDKHOIXT, #IDNGTS, #IDNGXT
### QLTS_ViewNhapNVDS – Nhap nguyen vong dang danh sach
- Lưới 1 «Danh sách thí sinh đăng ký nguyện vọng» (bảng TDSTSNV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Phiếu số (C) [PHIEUSOBGD](chỉ đọc); Phiếu số (code) [PHIEUSO](chỉ đọc); Số CMND [SoCMND](chỉ đọc); SBD [SBD](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Phái [Phai]{chọn}(chỉ đọc); Mã dân tộc [MaDT](chỉ đọc); Tên dân tộc [TenDT](chỉ đọc); Mã tôn giáo [MaTG](chỉ đọc); Tên tôn giáo [TenTG](chỉ đọc); Mã địa bàn [MaDB](chỉ đọc); Tên địa bàn [TenDB](chỉ đọc); Mã TP (Hộ khẩu) [MaTPHKh](chỉ đọc); Tên Tỉnh/TP (Hộ khẩu) [TenTPHKh](chỉ đọc); NV ưu tiên [UUTIENNV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Mã khối [MAKHOITS]{nút …}(chỉ đọc); Mã ngành [MANGTS]{nút …}(chỉ đọc); Điểm 1 [Diem1](chỉ đọc); Điểm 2 [Diem2](chỉ đọc); Điểm 3 [Diem3](chỉ đọc); Điểm tổng các môn [DIEMTCNV](chỉ đọc); Điểm ưu tiên [DIEMUTKVDT](chỉ đọc); Điểm cộng XT [DIEMCONGXT](chỉ đọc); NgTT [MaNGTT](chỉ đọc); HTT [MaBHTT](chỉ đọc); Đối tượng TS [DOITUONGTS]{chọn}(chỉ đọc); Nhóm khu vực [NhomKVTS]{chọn}(chỉ đọc); Mã đợt [MADOTNVTS]{nút …}(chỉ đọc)
  - Cột ẩn: Mã DS thí sinh [MADSTS](chỉ đọc); Mã hồ sơ [MAHOSVNV](chỉ đọc); Mã bậc hệ [MaBH]{nút …}(chỉ đọc); Nguyện vọng [NGUYENVONG]{chọn}(chỉ đọc); NVTT [NGUYENVONGTT]{chọn}(chỉ đọc); Tên phương thức [TenPTXT](chỉ đọc)
### QLTS_ViewNhapSoPBLOP – View nhap so phan bo sv cho lop
- Lưới 1 «Danh sách lớp» (bảng TPBLOP); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã lớp [MaLop](chỉ đọc); Số lượng [SoLuongTT](chỉ đọc); Tên lớp [TenLop](chỉ đọc); SL chưa gán [SoLuongCGan](chỉ đọc); Mã bậc hệ [MaBH](chỉ đọc); SL đã gán [SoLuongDGan](chỉ đọc); Mã ngành [MANGTS]{nút …}; Tên ngành [TENNGTS](chỉ đọc); THPT [THPT]; Số SV dự kiến phân bổ [SOSVDKPB]
### QLTS_ViewNhapSoPhieuBD – View nhap so phieu bo dem
- Lưới 1 «Danh sách bộ đếm số phiếu» (bảng TSOPHIEUBD); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Số phiếu [SoPhieu](chỉ đọc); Bộ đếm [IDBoDem]
### QLTS_ViewNhapThongTinTS – view nhap thong tin ho so thi sinh
- Lưới 1 (bảng TDSTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Phiếu số (C) [PHIEUSOBGD]; SBD [SBD]; Họ lót [HoLotSV]; Tên [TenSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Phái [Phai]; Đối tượng TS [DOITUONGTS]; Nhóm khu vực [NhomKVTS]; Nơi sinh [NoiSinh]; Loại đoàn thể [LoaiDThe]; Nguồn tuyển [NguonTuyen]; Dân tộc [IDDT]; Số CMND [SoCMND]; Ngày cấp [NgayCap]; Nơi cấp [NoiCapCMND]; Địa chỉ [DC_DCHK]; Địa chỉ 2 [DC_DCHK2]; Tỉnh/thành [DC_IDDBHK]; Địa chỉ liên lạc [DC_DCLLSV]; Tỉnh/thành [DC_IDDBLL]; Email 1 [DC_EML1LLSV]; Điện thoại 1 [DC_DT1LLSV]; Tên mẹ [TenMe]; Tên cha [TenCha]; Nghề nghiệp [NNgMe]; Nghề nghiệp [NNgCha]; Điểm tổng [DiemTong]; Ghi chú hồ sơ [GCDSTS]; Tôn giáo [IDTG]; Người liên lạc [NguoiLL]; Tên ngành [TENNGTS]; Ghi chú hồ sơ 2 [GCDSTS2]; Điểm 1 [Diem1]; Điểm 2 [Diem2]; Điểm 3 [Diem3]; Lớp 10 [LOP10]; Lớp 11 [LOP11]; Lớp 12 [LOP12]; Ngành tuyển sinh [IDNGTS]; Khối tuyển sinh [IDKHOITS]; Học bạ THPT [CO_HB]; TN THPT [CO_TN]; Tên trường PT [TENTRPT]; Tên trường PT [TENTRPT2]; Tên trường PT [TENTRPT3]; Mã DS thí sinh [MADSTS]; Nhóm ưu tiên [NhomUT]; Tên trường tự do [TENLOP10]; Tên trường tự do [TENLOP11]; Tên trường tự do [TENLOP12]; Đã Kiểm dò TT [DaInKiemDoThanhTra]; Diện trúng tuyển [DienTT]
  - Ô trên form sửa: #PHIEUSOBGD, #TenDayDu, #NgaySinhC, #Phai, #DOITUONGTS, #NhomKVTS, #NoiSinh, #IDDT, #SoCMND, #NgayCap, #NoiCapCMND, #DC_DCHK, #DC_IDDBHK, #DC_DCLLSV, #DC_IDDBLL, #DC_DT1LLSV, #Diem1, #Diem2, #Diem3, #LOP10, #LOP11, #LOP12, #IDNGTS, #IDKHOITS, #CO_HB, #CO_TN, #TENTRPT, #TENTRPT2, #TENTRPT3, #DaInKiemDoThanhTra
### QLTS_ViewNhapThongTinTSNew – view nhap thong tin ho so thi sinh
- Lưới 1 «Danh sách thí sinh» (bảng TDSTS); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Phiếu số (C) [PHIEUSOBGD]; Họ lót [HoLotSV]; Tên [TenSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Phái [Phai]; Đối tượng TS [DOITUONGTS]; Nhóm khu vực [NhomKVTS]; Nơi sinh [NoiSinh]; Số CMND [SoCMND]; Ngày cấp [NgayCap]; Nơi cấp [NoiCapCMND]; Chương trình giảng dạy [LoaiCTGD]{chọn}
  - Cột ẩn: Địa chỉ [DC_DCHK]; Địa chỉ 2 [DC_DCHK2]; Địa chỉ liên lạc [DC_DCLLSV]; Địa chỉ 2 [DC_DCLLSV2]; Số ĐT cha [DC_DT1Cha]; Điện thoại 1 [DC_DT1LLSV]; Số ĐT mẹ [DC_DT1Me]; Điện thoại 2 [DC_DT2LLSV]; Email 1 [DC_EML1LLSV]; Email 2 [DC_EML2LLSV]; Tỉnh/thành [DC_IDDBHK]; Tỉnh/thành [DC_IDDBLL]; Điểm HK1 lớp 10 [DMHK1LP10]; Điểm HK1 lớp 11 [DMHK1LP11]; Điểm HK1 lớp 12 [DMHK1LP12]; Điểm HK2 lớp 10 [DMHK2LP10]; Điểm HK2  lớp 11 [DMHK2LP11]; Điểm HK2  lớp 12 [DMHK2LP12]; Điểm TB Lớp 10 [DMLP10]; Điểm TB Lớp 11 [DMLP11]; Điểm TB Lớp 12 [DMLP12]; Ghi chú hồ sơ [GCDSTS]; Ghi chú dùng bên detailright [GhiChuView1]; Ghi chú dùng bên detailright 2 [GhiChuView2]; Hạnh kiểm HK1L12 [HKiemHK1LP12]{chọn}; Hạnh kiểm [HanhKiem]{chọn}; Học lực [HocLuc]{chọn}; Đợt XT [IDDOTNVTS]; Dân tộc [IDDT]; Phương thức [IDPTXT]; Tôn giáo [IDTG]; Lớp 10 [LOP10]; Lớp 11 [LOP11]; Lớp 12 [LOP12]; Mã DS thí sinh [MADSTS]; Năm tốt nghiệp [NAMTN]; Ngày cấp [NgayCapVB]; Ngày thêm [NgayThem]{ngày}; Người liên lạc [NguoiLL]; Nhóm ưu tiên [NhomUT]; Nơi cấp VBSV [NoiCapVBSV]; SBD [SBD]; Số văn bằng [SOVBSV]; Tên trường tự do [TENLOP10]; Tên trường tự do [TENLOP11]; Tên trường tự do [TENLOP12]; Tên trường PT [TENTRPT]; Tên trường PT [TENTRPT2]; Tên trường PT [TENTRPT3]
  - Ô trên form sửa: #PHIEUSOBGD, #TenDayDu, #NgaySinhC, #Phai, #DOITUONGTS, #NhomKVTS, #NoiSinh, #SoCMND, #NgayCap, #NoiCapCMND, #DC_DCHK, #DC_DCLLSV, #DC_DT1LLSV, #DC_EML1LLSV, #DC_EML2LLSV, #DC_IDDBHK, #DC_IDDBLL, #GhiChuView1, #GhiChuView2, #IDDOTNVTS, #IDDT, #IDPTXT, #IDTG, #LOP10, #LOP11, #LOP12, #TENTRPT, #TENTRPT2, #TENTRPT3
### QLTS_ViewNhapThongTinTSNew_QTSG – view nhap thong tin ho so thi sinh
- Lưới 1 «Danh sách thí sinh» (bảng TDSTS); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Phiếu số (C) [PHIEUSOBGD]; Họ lót [HoLotSV]; Tên [TenSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Phái [Phai]; Đối tượng TS [DOITUONGTS]; Nhóm khu vực [NhomKVTS]; Nơi sinh [NoiSinh]; Số CMND [SoCMND]; Ngày cấp [NgayCap]; Nơi cấp [NoiCapCMND]; Chương trình giảng dạy [LoaiCTGD]{chọn}; Nơi học [NoiHocTS]{chọn}
  - Cột ẩn: TN THPT [CO_TN]; Địa chỉ [DC_DCHK]; Địa chỉ 2 [DC_DCHK2]; Địa chỉ liên lạc [DC_DCLLSV]; Địa chỉ 2 [DC_DCLLSV2]; Số ĐT cha [DC_DT1Cha]; Điện thoại 1 [DC_DT1LLSV]; Số ĐT mẹ [DC_DT1Me]; Điện thoại 2 [DC_DT2LLSV]; Email 1 [DC_EML1LLSV]; Email 2 [DC_EML2LLSV]; Tỉnh/thành [DC_IDDBHK]; Tỉnh/thành [DC_IDDBLL]; Điểm HK1 lớp 10 [DMHK1LP10]; Điểm HK1 lớp 11 [DMHK1LP11]; Điểm HK1 lớp 12 [DMHK1LP12]; Điểm HK2 lớp 10 [DMHK2LP10]; Điểm HK2  lớp 11 [DMHK2LP11]; Điểm HK2  lớp 12 [DMHK2LP12]; Điểm TB Lớp 10 [DMLP10]; Điểm TB Lớp 11 [DMLP11]; Điểm TB Lớp 12 [DMLP12]; Điểm tổng [DiemTong]; Ghi chú hồ sơ [GCDSTS]; Ghi chú hồ sơ 2 [GCDSTS2]; Ghi chú hồ sơ 3 [GCDSTS3]; Ghi chú dùng bên detailright [GhiChuView1]; Ghi chú dùng bên detailright 2 [GhiChuView2]; Hạnh kiểm HK1L12 [HKiemHK1LP12]{chọn}; Hạnh kiểm [HanhKiem]{chọn}; Học lực [HocLuc]{chọn}; Đợt XT [IDDOTNVTS]; Dân tộc [IDDT]; Phương thức [IDPTXT]; Tôn giáo [IDTG]; Đăng ký online [IsDKOnline]; Lớp 10 [LOP10]; Lớp 11 [LOP11]; Lớp 12 [LOP12]; Mã DS thí sinh [MADSTS]; Năm tốt nghiệp [NAMTN]; Ngày cấp [NgayCapVB]; Ngày thêm [NgayThem]{ngày}; NgayXacNhan [NgayXacNhan]; Người liên lạc [NguoiLL]; Nhóm ưu tiên [NhomUT]; Nơi cấp VBSV [NoiCapVBSV]; SBD [SBD]; Số văn bằng [SOVBSV]; Tên trường tự do [TENLOP10]; Tên trường tự do [TENLOP11]; Tên trường tự do [TENLOP12]; Tên trường PT [TENTRPT]; Tên trường PT [TENTRPT2]; Tên trường PT [TENTRPT3]
  - Ô trên form sửa: #PHIEUSOBGD, #TenDayDu, #NgaySinhC, #Phai, #DOITUONGTS, #NhomKVTS, #NoiSinh, #SoCMND, #NgayCap, #NoiCapCMND, #NoiHocTS, #CO_TN, #DC_DCHK, #DC_DCLLSV, #DC_DT1LLSV, #DC_EML1LLSV, #DC_IDDBHK, #DC_IDDBLL, #DMHK1LP10, #DMHK1LP11, #DMHK1LP12, #DMHK2LP10, #DMHK2LP11, #DMLP12, #DiemTong, #GhiChuView1, #GhiChuView2, #HKiemHK1LP12, #HanhKiem, #HocLuc, #IDDOTNVTS, #IDDT, #IDPTXT, #IDTG, #LOP10, #LOP11, #LOP12, #TENTRPT, #TENTRPT2, #TENTRPT3
### QLTS_ViewNhapTT_CTTD – view nhap thong tin ho so thi sinh
- Lưới 1 «Danh sách thí sinh» (bảng TDSTS); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Phiếu số (C) [PHIEUSOBGD]; Họ lót [HoLotSV]; Tên [TenSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Phái [Phai]; Đối tượng TS [DOITUONGTS]; Nhóm khu vực [NhomKVTS]; Nơi sinh [NoiSinh]; Số CMND [SoCMND]; Ngày cấp [NgayCap]; Nơi cấp [NoiCapCMND]; Chương trình giảng dạy [LoaiCTGD]{chọn}; Thiếu học bạ [IsNotHB]; Thiếu phiếu điểm [IsNotDiem]; Thiểu giấy CN TN [IsNotCNTN]
  - Cột ẩn: TN THPT [CO_TN]; Địa chỉ [DC_DCHK]; Địa chỉ 2 [DC_DCHK2]; Địa chỉ liên lạc [DC_DCLLSV]; Địa chỉ 2 [DC_DCLLSV2]; Số ĐT cha [DC_DT1Cha]; Điện thoại 1 [DC_DT1LLSV]; Số ĐT mẹ [DC_DT1Me]; Điện thoại 2 [DC_DT2LLSV]; Email 1 [DC_EML1LLSV]; Email 2 [DC_EML2LLSV]; Tỉnh/thành [DC_IDDBHK]; Tỉnh/thành [DC_IDDBLL]; Điểm HK1 lớp 10 [DMHK1LP10]; Điểm HK1 lớp 11 [DMHK1LP11]; Điểm HK1 lớp 12 [DMHK1LP12]; Điểm HK2 lớp 10 [DMHK2LP10]; Điểm HK2  lớp 11 [DMHK2LP11]; Điểm HK2  lớp 12 [DMHK2LP12]; Điểm TB Lớp 10 [DMLP10]; Điểm TB Lớp 11 [DMLP11]; Điểm TB Lớp 12 [DMLP12]; Ghi chú hồ sơ [GCDSTS]; Ghi chú dùng bên detailright [GhiChuView1]; Ghi chú dùng bên detailright 2 [GhiChuView2]; Hạnh kiểm HK1L12 [HKiemHK1LP12]{chọn}; Hạnh kiểm [HanhKiem]{chọn}; Học lực [HocLuc]{chọn}; Đợt XT [IDDOTNVTS]; Dân tộc [IDDT]; Phương thức [IDPTXT]; Tôn giáo [IDTG]; Lớp 10 [LOP10]; Lớp 11 [LOP11]; Lớp 12 [LOP12]; Mã DS thí sinh [MADSTS]; Năm tốt nghiệp [NAMTN]; Ngày cấp [NgayCapVB]; Ngày thêm [NgayThem]{ngày}; Người liên lạc [NguoiLL]; Nhóm ưu tiên [NhomUT]; Nơi cấp VBSV [NoiCapVBSV]; SBD [SBD]; Số văn bằng [SOVBSV]; Tên trường tự do [TENLOP10]; Tên trường tự do [TENLOP11]; Tên trường tự do [TENLOP12]; Tên trường PT [TENTRPT]; Tên trường PT [TENTRPT2]; Tên trường PT [TENTRPT3]
  - Ô trên form sửa: #PHIEUSOBGD, #TenDayDu, #NgaySinhC, #Phai, #DOITUONGTS, #NhomKVTS, #IsNotHB, #IsNotDiem, #IsNotCNTN, #DC_DCHK, #DC_DCLLSV, #DC_DT1LLSV, #DC_EML1LLSV, #DC_IDDBHK, #DC_IDDBLL, #GhiChuView1, #GhiChuView2, #IDDOTNVTS, #IDPTXT, #LOP10, #LOP11, #LOP12, #TENTRPT, #TENTRPT2, #TENTRPT3
### QLTS_ViewNhapTTNhapHoc – view nhap thong tin nhap hoc
- Lưới 1 (bảng TDSTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Phiếu số (C) [PHIEUSOBGD]; Họ lót [HoLotSV]; Tên [TenSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Phái [Phai]; Đối tượng TS [DOITUONGTS]; Nhóm khu vực [NhomKVTS]; Nơi sinh [NoiSinh]; Loại đoàn thể [LoaiDThe]; Nguồn tuyển [NguonTuyen]; Dân tộc [IDDT]; Số CMND [SoCMND]; Ngày cấp [NgayCap]; Nơi cấp [NoiCapCMND]; Địa chỉ [DC_DCHK]; Địa chỉ 2 [DC_DCHK2]; Tỉnh/thành [DC_IDDBHK]; Địa chỉ liên lạc [DC_DCLLSV]; Tỉnh/thành [DC_IDDBLL]; Email 1 [DC_EML1LLSV]; Điện thoại 1 [DC_DT1LLSV]; Tên mẹ [TenMe]; Tên cha [TenCha]; Nghề nghiệp [NNgMe]; Nghề nghiệp [NNgCha]; Điểm tổng [DiemTong]; Ghi chú hồ sơ [GCDSTS]; Tôn giáo [IDTG]; Người liên lạc [NguoiLL]; Tên ngành [TENNGTS]; Ghi chú hồ sơ 2 [GCDSTS2]; Điểm 1 [Diem1]; Điểm 2 [Diem2]; Điểm 3 [Diem3]; Mã SV [MaSV]; Mã dân tộc [MaDT]; Quê quán [QueQuan]; Điện thoại NgLL [DC_DTNgLL]
  - Ô trên form sửa: #PHIEUSOBGD, #HoLotSV, #TenSV, #TenDayDu, #NgaySinhC, #Phai, #DOITUONGTS, #NhomKVTS, #NoiSinh, #LoaiDThe, #NguonTuyen, #IDDT, #SoCMND, #NgayCap, #NoiCapCMND, #DC_DCHK, #DC_DCHK2, #DC_IDDBHK, #DC_EML1LLSV, #DC_DT1LLSV, #TenMe, #TenCha, #NNgMe, #NNgCha, #DiemTong, #GCDSTS, #IDTG, #TENNGTS, #GCDSTS2, #Diem1, #Diem2, #Diem3, #QueQuan, #DC_DTNgLL
### QLTS_ViewNhapTTNhapHoc_HVSG – view nhap thong tin nhap hoc
- Lưới 1 (bảng TDSTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Phiếu số (C) [PHIEUSOBGD]; Họ lót [HoLotSV]; Tên [TenSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Phái [Phai]; Đối tượng TS [DOITUONGTS]; Nhóm khu vực [NhomKVTS]; Nơi sinh [NoiSinh]; Loại đoàn thể [LoaiDThe]; Nguồn tuyển [NguonTuyen]; Dân tộc [IDDT]; Số CMND [SoCMND]; Ngày cấp [NgayCap]; Nơi cấp [NoiCapCMND]; Địa chỉ [DC_DCHK]; Địa chỉ 2 [DC_DCHK2]; Tỉnh/thành [DC_IDDBHK]; Địa chỉ liên lạc [DC_DCLLSV]; Tỉnh/thành [DC_IDDBLL]; Email 1 [DC_EML1LLSV]; Điện thoại 1 [DC_DT1LLSV]; Tên mẹ [TenMe]; Tên cha [TenCha]; Nghề nghiệp [NNgMe]; Nghề nghiệp [NNgCha]; Điểm tổng [DiemTong]; Ghi chú hồ sơ [GCDSTS]; Tôn giáo [IDTG]; Người liên lạc [NguoiLL]; Tên ngành [TENNGTS]; Ghi chú hồ sơ 2 [GCDSTS2]; Điểm 1 [Diem1]; Điểm 2 [Diem2]; Điểm 3 [Diem3]; Số ĐT cha [DC_DT1Cha]; Số ĐT mẹ [DC_DT1Me]; Phương thức [IDPTXT]; Ngày bổ sung [NgayBSTN]; Năm tốt nghiệp [NAMTN]; Số văn bằng [SOVBSV]; Ngày cấp [NgayCapVB]; Nơi cấp VBSV [NoiCapVBSV]; Lớp 12 [LOP12]; Điểm TB Lớp 10 [DMLP10]; Điểm TB Lớp 11 [DMLP11]; Điểm TB Lớp 12 [DMLP12]
  - Ô trên form sửa: #PHIEUSOBGD, #HoLotSV, #TenSV, #TenDayDu, #NgaySinhC, #Phai, #DOITUONGTS, #NhomKVTS, #NoiSinh, #LoaiDThe, #IDDT, #SoCMND, #NgayCap, #NoiCapCMND, #DC_DCHK, #DC_DCHK2, #DC_IDDBHK, #DC_EML1LLSV, #DC_DT1LLSV, #TenMe, #TenCha, #NNgMe, #NNgCha, #DiemTong, #GCDSTS, #IDTG, #TENNGTS, #GCDSTS2, #Diem1, #Diem2, #Diem3, #DC_DT1Cha, #DC_DT1Me, #IDPTXT, #NgayBSTN, #NAMTN, #SOVBSV, #NgayCapVB, #NoiCapVBSV, #LOP12, #DMLP10, #DMLP11, #DMLP12
### QLTS_ViewNhapTTNhapHoc_Mul – view nhap thong tin nhap hoc
- Lưới 1 (bảng TDSTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Phiếu số (C) [PHIEUSOBGD]; Họ lót [HoLotSV]; Tên [TenSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Phái [Phai]; Đối tượng TS [DOITUONGTS]; Nhóm khu vực [NhomKVTS]; Nơi sinh [NoiSinh]; Loại đoàn thể [LoaiDThe]; Nguồn tuyển [NguonTuyen]; Dân tộc [IDDT]; Số CMND [SoCMND]; Ngày cấp [NgayCap]; Nơi cấp [NoiCapCMND]; Địa chỉ [DC_DCHK]; Địa chỉ 2 [DC_DCHK2]; Tỉnh/thành [DC_IDDBHK]; Địa chỉ liên lạc [DC_DCLLSV]; Tỉnh/thành [DC_IDDBLL]; Email 1 [DC_EML1LLSV]; Điện thoại 1 [DC_DT1LLSV]; Tên mẹ [TenMe]; Tên cha [TenCha]; Nghề nghiệp [NNgMe]; Nghề nghiệp [NNgCha]; Điểm tổng [DiemTong]; Ghi chú hồ sơ [GCDSTS]; Tôn giáo [IDTG]; Người liên lạc [NguoiLL]; Tên ngành [TENNGTS]; Ghi chú hồ sơ 2 [GCDSTS2]; Điểm 1 [Diem1]; Điểm 2 [Diem2]; Điểm 3 [Diem3]; Số ĐT cha [DC_DT1Cha]; Số ĐT mẹ [DC_DT1Me]; Phương thức [IDPTXT]; Ngày bổ sung [NgayBSTN]; Năm tốt nghiệp [NAMTN]; Số văn bằng [SOVBSV]; Ngày cấp [NgayCapVB]; Nơi cấp VBSV [NoiCapVBSV]; Lớp 12 [LOP12]
  - Ô trên form sửa: #PHIEUSOBGD, #HoLotSV, #TenSV, #TenDayDu, #NgaySinhC, #Phai, #DOITUONGTS, #NhomKVTS, #NoiSinh, #LoaiDThe, #IDDT, #SoCMND, #NgayCap, #NoiCapCMND, #DC_DCHK, #DC_DCHK2, #DC_IDDBHK, #DC_EML1LLSV, #DC_DT1LLSV, #TenMe, #TenCha, #NNgMe, #NNgCha, #DiemTong, #GCDSTS, #IDTG, #TENNGTS, #GCDSTS2, #Diem1, #Diem2, #Diem3, #DC_DT1Cha, #DC_DT1Me, #IDPTXT, #NgayBSTN, #NAMTN, #SOVBSV, #NgayCapVB, #NoiCapVBSV, #LOP12
### QLTS_ViewSaveDiemTS – Điểm thí sinh
- Lưới 1 (bảng TDSTSMON); tắt: Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã thí sinh [IDDSTS]; Môn thi [IDMONTS]; Điểm môn thi [DIEMMON]; Điểm thưởng [DIEMTHUONG]; Điểm phạt [DIEMPHAT]
### QLTS_ViewTrungTuyen – Cap nhat ten lop tuyen sinh
- Lưới 1 «Danh sách thí sinh trúng tuyển» (bảng TDSTRTUYEN); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Mã lớp [MaLop]{nút …}; Phiếu số (C) [PHIEUSOBGD](chỉ đọc); Mã DS thí sinh [MADSTS](chỉ đọc); Số CMND [SoCMND](chỉ đọc); SBD [SBD](chỉ đọc); Phiếu số (code) [PHIEUSO](chỉ đọc); Mã đợt [MADOTNVTS]{nút …}(chỉ đọc); ĐT [DT](chỉ đọc); Đối tượng TS [DOITUONGTS]{chọn}(chỉ đọc); KV [KV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Phái [Phai]{chọn}(chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Địa chỉ [DC_DCHK](chỉ đọc); Mã ngành [MANGTS]{nút …}(chỉ đọc); Mã khối [MAKHOITS]{nút …}(chỉ đọc); Mã bậc hệ [MaBH]{nút …}(chỉ đọc); Điểm 1 [Diem1](chỉ đọc); Điểm 2 [Diem2](chỉ đọc); Điểm 3 [Diem3](chỉ đọc); Mã Quận/Huyện (Hộ khẩu) [MaQHHKh](chỉ đọc); Mã TP (Hộ khẩu) [MaTPHKh](chỉ đọc); Đã chuyển vào qlsv [CHUYENQLSV](chỉ đọc); Ghi chú [GhiChu](chỉ đọc)
  - Cột ẩn: Điện thoại 1 [DC_DT1LLSV](chỉ đọc); Email 1 [DC_EML1LLSV](chỉ đọc); Điểm cộng XT [DIEMCONGXT](chỉ đọc); Điểm tổng các môn [DIEMTCNV](chỉ đọc); Điểm ưu tiên [DIEMUTKVDT](chỉ đọc); Điểm tổng [DiemTong](chỉ đọc); Điểm ưu tiên [DiemUT](chỉ đọc); Mã phương thức [MaPTXT](chỉ đọc); Ngày xét [NgayXet](chỉ đọc); Số BD trường nộp đơn [SBDCUMPT](chỉ đọc); Số GBTT [SOGBTT](chỉ đọc); THPT [THPT](chỉ đọc); Tổng [TONG](chỉ đọc); Tổng xét [TongXet](chỉ đọc); NV ưu tiên [UUTIENNV](chỉ đọc)
### QLTS_ViewTuyenThang – View nhap ds tuyen thang
- Lưới 1 «Danh sách thí sinh tuyển thẳng» (bảng TDSTS); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Họ lót [HoLotSV]; Tên [TenSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Phái [Phai]{chọn}; Số CMND [SoCMND]; Nơi cấp [NoiCapCMND]; Ngày cấp [NgayCap]; Mã ngành [MANGTS]; Đợt XT [IDDOTNVTS]
  - Cột ẩn: Địa chỉ liên lạc [DC_DCLLSV]; Điện thoại 1 [DC_DT1LLSV]; Email 1 [DC_EML1LLSV]; Tỉnh/thành [DC_IDDBLL]; Lý do tuyển thẳng [GCTUYENTHG]; Ngành tuyển sinh [IDNGTS]; Tên ngành [TENNGTS]
  - Ô trên form sửa: #TenDayDu, #NgaySinhC, #Phai, #SoCMND, #NoiCapCMND, #NgayCap, #IDDOTNVTS, #DC_DCLLSV, #DC_DT1LLSV, #DC_EML1LLSV, #DC_IDDBLL, #GCTUYENTHG, #IDNGTS, #TENNGTS
### QLTS_ViewXacNhanTT – View chon thi sinh trung tuyen
- Lưới 1 «Danh sách thí sinh đã xác nhận nhập học»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Số BD trường nộp đơn [SBDCUMPT]; Mã lớp [MaLop]; HS [IsHoSo]; Tổng tiền [TongTien]; Mã DS thí sinh [MADSTS]; Phiếu số (code) [PHIEUSO]; Phiếu số (C) [PHIEUSOBGD]; Số GBTT [SOGBTT]; Họ lót [HoLotSV]; Tên [TenSV]; Phái [Phai]{chọn}; Ngày sinh [NgaySinhC]; Mã bậc hệ [MaBH]; Mã ngành [MANGTS]; Tên ngành [TENNGTS]; Mã khối [MAKHOITS]; Tên khối [TENKHOITS]; Đã chuyển vào qlsv [CHUYENQLSV]
  - Cột ẩn: Địa chỉ liên lạc [DC_DCLLSV]; Điện thoại 1 [DC_DT1LLSV]; Điện thoại 2 [DC_DT2LLSV]; Điểm ưu tiên [DIEMUTKVDT]; Điểm 1 [Diem1]; Điểm 2 [Diem2]; Điểm 3 [Diem3]; Điểm tổng [DiemTong]; Ghi chú [GCDOTNVTS]; Hạnh kiểm [HanhKiem]{chọn}; Học lực [HocLuc]{chọn}; Mã đợt [MADOTNVTS]; NV [NV]; Ngày nộp hồ sơ [NgayNopHS]{ngày}; SBD [SBD]; Số HS [SoHoSo]
### QLTS_ViewXemDiemThi – View xem điểm thi
- Lưới 1 «Danh sách thí sinh»; tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: SBD [SBD]; Mã DS thí sinh [MADSTS]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Phái [Phai]; Nhóm khu vực [NhomKVTS]{chọn}; Đối tượng TS [DOITUONGTS]{chọn}; Mã ngành [MANGTS]; Mã khối [MAKHOITS]; Điểm 1 [Diem1]; Điểm 2 [Diem2]; Điểm 3 [Diem3]; Tổng [TONG]
### QLTS_ViewXemFileHS – View xem ho so
- Lưới 1 «Danh sách hồ sơ chi tiết»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã hồ sơ [MaHS]; Tên hồ sơ [TenHS]; Thứ tự [TTHs]; Nội dung file [NoiDungFile]; Tên file [FileName]; Xem file [XemFile]
### QLTSViewChonNV – view chon nguyen vong
- Lưới 1 «Danh sách nguyện vọng» (bảng TDSTSNV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Nguyện vọng [NGUYENVONG]{chọn}; Số lượng [SoLuong]; NV ưu tiên [UUTIENNV]; Tên thứ tự [TenNVong]
### QLTV_ViewCapNhatDSTS_MASV – View cap nhat thi sinh theo masv
- Lưới 1 (bảng TDSTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Phái [Phai]; Ngày sinh [NgaySinhC]; Nơi sinh [NoiSinh]; Đối tượng TS [DOITUONGTS]; Nhóm khu vực [NhomKVTS]; Nguồn tuyển [NguonTuyen]; Loại đoàn thể [LoaiDThe]; Dân tộc [IDDT]; Tôn giáo [IDTG]; Quê quán [QueQuan]; Số CMND [SoCMND]; Ngày cấp [NgayCap]; Nơi cấp [NoiCapCMND]; Điện thoại 1 [DC_DT1LLSV]; Email 1 [DC_EML1LLSV]; Điện thoại NgLL [DC_DTNgLL]; Địa chỉ [DC_DCHK]; Địa chỉ 2 [DC_DCHK2]; Tỉnh/thành [DC_IDDBHK]; Tên cha [TenCha]; Tên mẹ [TenMe]; Nghề nghiệp [NNgCha]; Nghề nghiệp [NNgMe]; Ghi chú hồ sơ [GCDSTS]; Ghi chú hồ sơ 2 [GCDSTS2]
### RELATIONVERSION – Danh sách phiên bản relation
- Lưới 1; tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Sửa bên phải
  - Cột: Bảng chính [TableP]; Field chính [FieldP]; Field phụ [FieldC]; Loại relation [RelationType]{chọn}; Bảng phụ [TableC]
  - Cột ẩn: Ràng buộc xóa [DeleteRule]; ID Relation [IDRelation]
### RELATIONVERSION1 – Danh sách phiên bản relation
- Lưới 1 (bảng AQRelation); tắt: Thêm, Xóa, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Sửa bên phải
  - Cột: Bảng chính [TableP]; Bảng phụ [TableC]; Field chính [FieldP]; Field phụ [FieldC]; Ràng buộc xóa [DeleteRule]{chọn}; Update [UpdateRule]; Bảng chính SS [TablePSS]; Bảng phụ SS [TableCSS]; Ràng buộc xóa SS [DeleteRuleSS]; Ràng buộc sửa SS [UpdateRuleSS]
  - Cột ẩn: Bộ relation [BoRelation]; Điều kiện [DieuKien]; Dieu kiện (2) [DieuKien1]; ID Relation [IDRelation]; Mã user [MaUser]; Ngày thêm [NgayThemC]; Relation vòng [RelationLoop]; Loại relation [RelationType]{chọn}; Relation ảo [RelationVirtual]; Vai trò [UserRole]
### REPORTKCTDTKH – Ke hoach
- Lưới 1 «Danh sách khối» (bảng KDMKHOI); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; NHHK vào [NHHKVao]; NHHK ra [NHHKRa]; Mã bậc hệ [MaBH]; Mã Ng/CNg [MaNgChng]; Tên ng/chng [TenNgChng]
  - Cột ẩn: Tên bậc hệ [TenBH]
### RPORT – Chỉnh định
- Lưới 1 (bảng HDMSubReport); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã report con [SubCode]; Tên Sub report [TenSubReport]; Tên viết tắt [VtSubReport]; Không quản lý [HuySubReport]; Sub report mặc định [DfSubReport]; Ghi chú [GcSubReport]; Mã Report [MaReport1]
  - Cột ẩn: Report mặc định [DfReport1]; Điều kiện [DieuKien]; Dieu kiện (2) [DieuKien1]; Ghi chú [GcReport1]; Không quản lý [HuyReport1]; ID phận hệ chính [IDPHChinh]; ID Report [IDReport]; ID nhóm Report [IDReport0]; ID Report [IDReport1]; Mã mẫu in [IDSubReport]; Hoc kỳ? [IsHocKy]; Mã report công bố [MaReport1CB]; Không lên menu [NoShowMenu]; TT sub report [TTSubReport]; Tên Report [TenReport1]; Tên tiếng anh [TenReport1Eg]; Thứ tự [TtReport1]; Vai trò [UserRole]; Tên viết tắt [VtReport1]
  - Ô trên form sửa: #SubCode, #TenSubReport, #VtSubReport, #HuySubReport, #DfSubReport, #GcSubReport, #MaReport1
### S-DSQD1SV – Danh sách quyết định của 1 sinh viên
- Lưới 1 «Danh sách quyết định của sinh viên» (bảng SDSQD); tắt: Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Hiện diện SV [HienDienSV]{chọn}; Số quyết định [SoQDSV]; Tên quyết định [TenQDSV]; Lý do QĐ [IDLDQDSV]; Ngày lập QĐ [NgayLapQDSV]{ngày}; Loại lý do [LoaiLDQDSV]{chọn}; Mã lớp (cũ) [IDLopCu]; Mã lớp (mới) [IDLopMoi]; Số học kỳ nghỉ [SoHKNghi]
  - Cột ẩn: Ghi chú [GcDSSVQD]; Ghi chú 2 [GcDSSVQD2]; Ghi chú [GcSVHK]; Ghi chú KTKL [GcSVKK]; Mã lớp [IDLop]; Mã bậc hệ [MaBH]; Mã khối [MaKhoi]; Mã Ng/CNg [MaNgChng]; Ngày cấp [NgayCap]{ngày}; Số văn bằng [SOVBSV]; Số vào sổ [SoVaoSo]; Xếp loại tốt nghiệp [XepLoaiTN]
  - Ô trên form sửa: #NHHK, #HienDienSV, #SoQDSV, #IDLDQDSV, #NgayLapQDSV, #IDLopCu, #IDLopMoi, #SoHKNghi, #GcDSSVQD, #GcDSSVQD2
### S_CHON_BACHE – Giao diện chọn bậc hệ cho Sinh Viên
- Lưới 1 «Danh sách bậc hệ» (bảng KDMBH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]
### S_CHONNGANHANG – View chọn ngân hàng bên sv
- Lưới 1 «Danh sách ngân hàng» (bảng NDMNH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã ngân hàng [MaNH]; Tên ngân hàng [TenNH]; Tên viết tắt [VTNH]
### SCH_ViewNhapDotLopTKB – View nhap lop doi tkb ngay
- Lưới 1 «Danh sách các đợt thời gian học của lớp» (bảng KLOPDOT); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Tên lớp [TenLop]; Thứ tự đợt học [DOTHOCLOP]{số}; Ngày bắt đầu [NGAYBDLOP]{ngày}; Ngày kết thúc [NGAYKTLOP]{ngày}
  - Cột ẩn: Lớp sinh viên [IDLop]
  - Ô trên form sửa: #TenLop, #DOTHOCLOP, #NGAYBDLOP, #NGAYKTLOP, #IDLop
### SDKKhoaLuanTN2 – Sinh viên được phép đăng ký khóa luận
- Lưới 1 (bảng SDKKhoaLuanTN); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Phái [Phai]; Hiện diện [HienDienSV2]; Ghi chú [GCDKKhoaLuanTN]; Mã lớp [MaLop]
### SDMCTHOC – Danh mục chương trình học
- Lưới 1 «Danh mục chương trình học» (bảng SDMCTHOC); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã chương trình học [MaCTHOC]; Tên chương trình học [TenCTHOC]; Viết tắt chương trình học [VtCTHOC]
  - Cột ẩn: Ghi chú chương trình học [GcCTHOC]; Tên tiếng anh [TenCTHOCEg]
  - Ô trên form sửa: #MaCTHOC, #TenCTHOC, #VtCTHOC, #GcCTHOC, #TenCTHOCEg
### SDMCTYBH – Danh mục công ty bảo hiểm
- Lưới 1 «Danh sách công ty bảo hiểm» (bảng SDMCTYBH); tắt: Sửa trên lưới
  - Cột: Mã Cty BH [MaCTyBH]; Tên Cty BH [TenCTyBH]; Viết tắt [VtCTyBH]; Ghi chú [GcCTyBH]
  - Cột ẩn: Mặc định [DfCTyBH]; Không quản lý [HuyCTyBH]; Tên tiếng anh [TenCTyBHEg]
  - Ô trên form sửa: #MaCTyBH, #TenCTyBH, #VtCTyBH, #GcCTyBH, #TenCTyBHEg
### SDMLDBH – Danh mục lý do bảo hiểm chi trả
- Lưới 1 «Danh mục lý do chi trả bảo hiểm» (bảng SDMLDBH); tắt: Sửa trên lưới
  - Cột: Mã lý do bảo hiểm [MaLDBH]; Tên lý do bảo hiểm [TenLDBH]; Viết tắt lý do bảo hiểm [VtLDBH]
  - Cột ẩn: Ghi chú lý do bảo hiểm [GcLDBH]; Tên tiếng anh [TenLDBHEg]
  - Ô trên form sửa: #MaLDBH, #TenLDBH, #VtLDBH, #GcLDBH, #TenLDBHEg
### SMUCBH – Định nghĩa mức bảo hiểm
- Lưới 1 «Danh sách mức bảo hiểm» (bảng SMucBH); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mức bảo hiểm [MucBH]{số}; Loại BHSV [LoaiBHSV]{chọn}; Số tiền đóng [STienDongBH]{số}; Ghi chú [GcBHSV]
  - Ô trên form sửa: #MucBH, #LoaiBHSV, #STienDongBH, #GcBHSV
### SNhomKhHB – Danh sách nhóm khối HBHK
- Lưới 1 «Danh sách nhóm khối HBHK» (bảng SNhomKhHB); tắt: Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã nhóm khối HBHK [MaNhomKhHB]; Tên nhóm khối HBHK [TenNhomKhHB]; Viết tắt [VtNhomKhHB]
  - Cột ẩn: Ghi chú [GcNhomKhHB]; Tiêu chuẩn [IDTChuan]
  - Ô trên form sửa: #MaNhomKhHB, #TenNhomKhHB, #VtNhomKhHB, #GcNhomKhHB, #IDTChuan
### SOSANHFILE – So sánh file
- Lưới 1; tắt: Nạp lại
### SVDongBo – Danh sách sinh viên được đồng bộ
- Lưới 1 «Danh sách sinh viên chọn»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Phái [Phai]; Ngày sinh [NgaySinhC]
### T1 – Test
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### T22_NhapKhoanThuLePhi – Nhập khoản thu lệ phí
- Lưới 1 «Chuẩn bị khoản thu lệ phí» (bảng TKHTHUTS); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khoản thu [MaKhThu]; Tên khoản thu [TenKhThu]; Viết tắt [VTKhThu]; Số tiền [SoTien]; Ghi chú [GhiChu]
  - Ô trên form sửa: #MaKhThu, #TenKhThu, #VTKhThu, #SoTien, #GhiChu
### T22_NhapLePhiXetTuyen – Nhập lệ phí xét tuyển
- Lưới 1 «Nhập lệ phí xét tuyển» (bảng TDSTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Nơi sinh [NoiSinh]; Đã thu [DaThu]; Tổng tiền [TongTien]; Phiếu số (C) [PHIEUSOBGD]; Phái [Phai]; Số CMND [SoCMND]; Điện thoại 1 [DC_DT1LLSV]; Mã phương thức [MaPTXT]
### TEST – Test
- Lưới 1 «Danh sach bac» (bảng SDSQD); tắt: Nạp lại, Gộp mã, Sửa trên lưới
  - Cột: Số quyết định [SoQDSV]; Tên quyết định [TenQDSV]; Người ký QD [NguoiKyQDSV]
  - Ô trên form sửa: #SoQDSV, #TenQDSV, #NguoiKyQDSV
### TEST 2 – Sinh vien
- Lưới 1 (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Hình sinh viên [AvatarSV]
  - Cột ẩn: Chi nhánh [CHINHANHNH]; Cơ quan công tác [CQCT]; Chức vụ công tác [CVCQCT]; Cân nặng [CanNang]; Chiều cao [ChieuCao]; Có nghề [CoNghe]; Địa chỉ CQCT [DCCQCT]; Địa chỉ [DC_DCHK]; Địa chỉ liên lạc [DC_DCLLSV]; Địa chỉ [DC_DCTT]; Địa chỉ [DC_DCVC]; Điện thoại 1 [DC_DT1HK]; Điện thoại 1 [DC_DT1LLSV]; Điện thoại 1 [DC_DT1TT]; Điện thoại 1 [DC_DT1VC]; Điện thoại 2 [DC_DT2HK]; Điện thoại 2 [DC_DT2LLSV]; Điện thoại 2 [DC_DT2TT]; Điện thoại 2 [DC_DT2VC]; Email 1 [DC_EML1LLSV]; Email liên lạc (2) [DC_EML2LL]; Email 1 [DC_Eml1HK]; Email 1 [DC_Eml1TT]; Email 1 [DC_Eml1VC]; Email 2 [DC_Eml2HK]; Email 2 [DC_Eml2TT]; Email 2 [DC_Eml2VC]; GC hộ khẩu [DC_GcHK]; GC liên lạc [DC_GcLL]; GC thường trú [DC_GcTT]; GC vợ chồng [DC_GcVC]; Tỉnh/thành [DC_IDDBHK]; Tỉnh/thành [DC_IDDBLL]; Tỉnh/thành [DC_IDDBTT]; Tỉnh/thành [DC_IDDBVC]; ĐK kinh tế [DKKinhTe]; Đang học [DangHoc]; Sinh viên mặc định [DfSV]; Ghi chú [GcLyLich]; Ghi chú [GcSV]; Ghi chú [GcThPhanGD]; Họ lót [HoLotSV]; Họ lót [HoLotSV2]; Họ SV (Index) [HoSVIdx]; Không quản lý [HuySV]; ID ch/ngành SV [IDChNgSV]; Tỉnh/thành [IDDB_CQCT]; Dân tộc [IDDT]; Ngân hàng [IDNgHang]; Sinh viên [IDSV]; Tôn giáo [IDTG]; Loại cư trú [LoaiCuTru]; Mã user [MaUser]; Cha mất [MatCha]; Mẹ mất [MatMe]; Nghề nghiệp [NNgCha]; Nghề nghiệp [NNgMe]; Nghề ng vợ/chồng [NgNghiepVC]; Ngày sinh [NgSinhCha]; Ngày sinh [NgSinhMe]; Ngày ngoại trú [NgayNgTru]; Ngày sinh [NgaySinh]; Ngày sinh [NgaySinhC]; Ngày thêm [NgayThem]; Người liên lạc [NguoiLL]; Nguồn tuyển [NguonTuyen]; Nơi cấp [NoiCapCMND]; Nơi sinh [NoiSinh]; Phái [Phai]; Phòng ký túc xá [PhongKTX]; Quê quán [QueQuan]; Quốc tịch [QuocTich]; Số anh chị em [SoAnhChiEm]; Số CMND [SoCMND]; Số năm bộ đội [SoNamBD]; Số năm TNXP [SoNamTNXP]; Số tài khoản [SoTaiKhoan]; Thứ tự [TTSV]; Tên cha [TenCha]; Tên chủ hộ [TenChuHo]; Tên chủ hộ (HK) [TenChuHoHK]; Tên mẹ [TenMe]; Tên [TenSV]; Tên [TenSV2]; Tên sv (Index) [TenSVIdx]; Tên vợ/chồng [TenVC]; Thành phần GĐ [ThPhanGD]; Thẻ thư viện [TheThuVien]; Trường chuyển [TrChuyen]; Tên viết tắt [VtSV]
  - Ô trên form sửa: #MaSV, #TenDayDu
### TEST SETTING – Test
- Lưới 1 (bảng AQDMSetting); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã Setting [MaSetting]; Tên Setting [TenSetting]
  - Cột ẩn: Admin sửa [AdminEdit]; Cho sửa node [AllowChangeNode]; Cho sửa cấy [AllowChangeTree]; Có phân cấp? [CoPhanCap]; Kiểu dữ liệu [DataType]; Setting mặc định [DfSetting]; Điều kiện [DieuKien]; Dieu kiện (2) [DieuKien1]; Đơn vị tính [DonViTinh]; Ghi chú [GcSetting]; Không quản lý [HuySetting]; ID Form [IDForm]; ID phân cấp min [IDPhanCapBegin]; ID phân cấp max [IDPhanCapEnd]; ID phấn cấp cuối (AQ) [IDPhanCapEndAQ]; Mã phân hệ [IDPhanHe]; ID Report [IDReport1]; Mã setting [IDSetting]; ID View 1 [IDView1]; Bien HK? [IsBienHK]; Bien HK con? [IsBienHKCon]; Bien User? [IsBienUser]; Bit? [IsBit]; Hằng số? [IsConst]; Full Enum 1? [IsFullEnumIdx1]; Full Enum 2? [IsFullEnumIdx2]; Tạo cờ? [IsTaoCo]; Key source [KeySource]; Mã Enum học kỳ con [MaEnumHKC]; Mã Enum index 1 [MaEnumIdx1]; Mã Enum index 2 [MaEnumIdx2]; Mã Enum kết quả [MaEnumKQ]; Mã user [MaUser]; Biến mapping [MappingArray]; Max value [MaxVal]; Min value [MinVal]; Ngày thêm [NgayThemC]; Nhóm chức năng [NhomChucNang]; Phiên bản [PhienBan]; Kiểu field DB [SpecType]; Thứ tự [TtSetting]; Vai trò [UserRole]; Tên viết tắt [VtSetting]
### TEST_KYTS – Test view ku tuyen sinh
- Lưới 1 (bảng TKYTS); tắt: Import, Xuất, In, Nạp lại, Gộp mã, Sửa trên lưới
  - Cột: Mã kỳ TS [MaKyTS]; Tên kỳ TS [TenKyTS]; Viết tắt [VTKYTS]; Chỉ tuyển 1 bậc hệ [ISTUYEN1BH]; Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]
### TESTDM – Test
- Lưới 1 (bảng NDMNV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Họ lót [HoLotNV]; Tên nhân viên [TenNV]; Mã khoa [MaKhoa]; Tên khoa [TenKhoa]
### TESTNV – Test Nv
- Lưới 1 (bảng SDMSV); tắt: Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Địa chỉ [DC_DCHK]
  - Ô trên form sửa: #MaSV, #HoLotSV, #TenSV, #DC_DCHK
### TESTVIEW3 – Test view dang 11
- Lưới 1 (bảng SHSSV); tắt: Import, Đổi mã, Gộp mã
  - Cột: Ngày nộp hồ sơ [NgayNopHS]; Hình hồ sơ [AvatarHS]; Ghi chú [GcHSSV]; Mã user [MaUser]
- Lưới 2 (bảng SSVHK); tắt: Import, Đổi mã, Gộp mã
  - Cột: Niên học học kỳ [NHHK]; Mã user [MaUser]; Hiện diện SV [HienDienSV]; Ghi chú [GcSVHK]; Lớp sinh viên [IDLop]
- Lưới 3 (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]
### TESTVIEWTHEMSUORCE – Test
### THOIGIANDKMH – Thời gian đăng ký môn học
- Lưới 1 «Thời gian cho phép đăng ký» (bảng MTGDK); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Ngày bắt đầu đăng ký [NgayBDDKMH]{ngày}; Ngày kết thúc đăng ký [NgayKTDKMH]{ngày}
### TOOL_AQDMREPORT1 – Danh mục report
- Lưới 1 (bảng AQReport); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Nguồn [Source]; Link source [LinkSource]; Nguồn source [RecordResource]
  - Cột ẩn: ID Detail Key [IDDetailKey]; ID Report [IDReport]; ID Report [IDReport1]; In group footer? [IsGroupFooter]; Nhiều hàng detail? [IsMulDetail]; Mã user [MaUser]; Ngày thêm [NgayThemC]
- Lưới 2 (bảng AQDMReport1); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã Report [MaReport1]; Tên Report [TenReport1]
  - Cột ẩn: Report mặc định [DfReport1]; Điều kiện [DieuKien]; Dieu kiện (2) [DieuKien1]; Ghi chú [GcReport1]; Không quản lý [HuyReport1]; ID phận hệ chính [IDPHChinh]; ID nhóm Report [IDReport0]; ID Report [IDReport1]; Hoc kỳ? [IsHocKy]; Mã report công bố [MaReport1CB]; Mã user [MaUser]; Ngày thêm [NgayThemC]; Không lên menu [NoShowMenu]; Tên tiếng anh [TenReport1Eg]; Thứ tự [TtReport1]; Vai trò [UserRole]; Tên viết tắt [VtReport1]
### TPM_TRUYVET – Truy vet chuong trinh dao tao thực hiện
- Lưới 1 «Nhật ký thay đổi chương trình đào tạo thực hiện»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; Niên học học kỳ [NHHK]; Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; User thực hiện [USERTHUCHIEN]; Ngày thực hiện [NGAYTHUCHIEN]; Tên Field [TenField]; Tác vụ [Action]{chọn}; Mã field [MaField]; Giá trị cũ [OldValue]; Giá trị mới [NewValue]
### TPM_TRUYVETCTDTCH – Truy vết chương trình đào tạo chuẩn
- Lưới 1 «Nhật ký thay đổi chương trình đào tạo chuẩn»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ ngành [MaBHNgChNg]; Tên bậc hệ ngành [TenBHNgChNg]; Tên phiên bản [TenPB]; Niên học học kỳ [NHHK]; Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; User thực hiện [USERTHUCHIEN]; Ngày thực hiện [NGAYTHUCHIEN]; Tên Field [TenField]; Tác vụ [Action]{chọn}; Mã field [MaField]; Giá trị cũ [OldValue]; Giá trị mới [NewValue]
### TPM_TRUYVETCTDTKH – Truy vết chương trình đào tạo kế hoạch
- Lưới 1 «Nhật ký thay đổi chương trình đào tạo kế hoạch»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; Niên học học kỳ [NHHK]; Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; User thực hiện [USERTHUCHIEN]; Ngày thực hiện [NGAYTHUCHIEN]; Tên Field [TenField]; Tác vụ [Action]{chọn}; Mã field [MaField]; Giá trị cũ [OldValue]; Giá trị mới [NewValue]
### TruyVet_DMSubReport – Truy vet report
- Lưới 1 «Nhật ký thay đổi report»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã report con [SubCode]; Tên Sub report [TenSubReport]; User thực hiện [USERTHUCHIEN]; Ngày thực hiện [NGAYTHUCHIEN]
### UpdateBoDemCT – Cập nhật bộ đếm học phí chi tiết
- Lưới 1 «Danh sách bộ đếm» (bảng HBoDemCT); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã bộ đếm [MaBoDem](chỉ đọc); Tên bộ đếm [TenBoDem](chỉ đọc); ĐT sử dụng [DTSuDung]{chọn}(chỉ đọc); Loại đối tượng [LoaiDoiTuong]{chọn}(chỉ đọc); Giá trị [GiaTriBoDem]; Học kỳ [HocKy](chỉ đọc); User SD [UserSD](chỉ đọc)
### V_ViewDNLopNhang – View định nghĩa ngân hàng cho lớp
- Lưới 1 «Danh sách lớp» (bảng SDMLOP); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Tên lớp [TenLop]; Niên khóa [NienKhoa]; Ngân hàng [IDNH]; Tên ngân hàng [TenNH]
### VCHUYEN_NHOM_DKMH – Chuyển nhóm đăng ký môn học
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### VCONGDIEM1SV – Cộng điểm 1 sinh viên
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### VDKMH_ONLINE – Đăng ký môn học online
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### VDKMH_THEO_LOP – Đăng ký môn học theo lớp
- Lưới 1 «Danh sách lớp»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Tên lớp [TenLop]; Tên viết tắt [VTLop]; Số sinh viên [SoSV]; Mã khối [MaKhoi]; Mã khoa [MaDV]; Tên khoa [TenDV]; Ghi chú [GcLop]
### VDKMH_THEO_LOP_1SOMH – Đăng ký môn học theo lớp và 1 số môn học
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### VHUY_DKMH_VP_TCMIN – Hủy đăng ký vi phạm tín chỉ min
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### View_25328_HocPhi – Danh sách học phí sinh viên
- Lưới 1 «Danh sách học phí sinh viên»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Học kỳ [NHHKThuHP]; Số HĐ [SoCTu]; Hủy [HUYPT]; Số tiền [TienThuGoc]; Đã đóng [TienPTCT]; Ngày đóng [NgayThem]{ngày}
  - Cột ẩn: Ghi chú 1 [GhiChu1]
  - Ô trên form sửa: #GhiChu1
### View_25328_QuyetDinh – Danh sách quyết định sinh viên
- Lưới 1 «Danh sách quyết định sinh viên»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Mã lý do [MaLDQDSV]; Loại lý do [LoaiLDQDSV]{chọn}; Số quyết định [SoQDSV]; Ngày lập QĐ [NgayLapQDSV]{ngày}
### View_25364 – Danh sách sinh viên đóng học phí theo môn học
- Lưới 1 «Danh sách SV đóng HP theo MH»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã KH [MaDV]; Mã Ng [MaNgChng]; Lớp [MaLop]; Mã môn học [MaMH]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Phái [Phai]; Ngày đóng [NgayTChi]{ngày}; Ngày nhập [NgayThem]{ngày}; Số CT [SoCTu]; Số tiền PT [TienThuGoc]; Số tiền MH [TienPTCT]; Số PNT [SoInvoice]
### View_CapNhatBaiHoc – View cập nhật bài học
- Lưới 1 (bảng KBaiHocCBGD); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Nhóm/tổ [NhomTo]; Tổ TH [ToTH]; Mã viên chức [MaNV]; Tên bài học [TenBaiHoc]
### VIEW_CAPNHATBH – Giao diện cập nhật bảo hiểm
- Lưới 1 (bảng NDongBH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [IDNV]; Tên đầy đủ [TenDayDuNV]; Loại thay đổi [LoaiThayDoi]; Bậc lương [BacLuong]; Lương cơ bản [LuongCB]; BHTN [BHTN]; BHYT [BHYT]; Hệ số lương [HSL]; Phụ cấp cv cũ [PCCVCu]; HSL cũ [HSLCu]; PCCV [PCCV]; PCVK cũ [HSTNVKCu]; Tỉ lệ BH đóng(%) [SoTienDong]; Mã ngạch cũ [IDNgachCu]; BHXH [BHXH]; Từ tháng [DongTuThang]; Bậc lương cũ [BacCu]; Từ năm [DongTuNam]; Ngạch [IDNgach]; PCVK [PCVK]
  - Ô trên form sửa: #IDNV, #TenDayDuNV, #LoaiThayDoi, #BacLuong, #LuongCB, #BHTN, #BHYT, #HSL, #HSLCu, #PCCV, #SoTienDong, #BHXH, #DongTuThang, #DongTuNam, #IDNgach, #PCVK
### View_CapNhatLopKDK – View cập nhật lớp không đăng ký online
- Lưới 1 (bảng SDMLOP); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Không đăng ký online [IsKgDKOnline]
### View_CapNhatTKBNgay – View cập nhật thời khóa biểu ngày
- Lưới 1 (bảng KTKBNG); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Nhóm/tổ [NhomTo]; Tổ TH [ToTH]; Tên tổ hợp [TenToHop]; Từ ngày [TUNGAYTKB]; Mã phòng [MaPH]
### View_CapNhatTKBNgayThi – View cập nhật thời khóa biểu ngày thi
- Lưới 1 (bảng KTKBTHI); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Nhóm/tổ [NhomTo]; Tổ TH [ToTH]; Tên tổ hợp [TenToHop]; Ngày thi [NgayThi]; Mã phòng [MaPH]; Tiết BĐ [TietBD]
### View_CapNhatTKBNgayThiL2 – View cập nhật thời khóa biểu ngày thi lần 2
- Lưới 1 (bảng KTKBTHI); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Nhóm/tổ [NhomTo]; Tổ TH [ToTH]; Tên tổ hợp [TenToHop]; Ngày thi lần 2 [NGAYTHIL2]; Mã phòng [MaPH]; Tiết BĐ thi lần 2 [TIETBDL2]; Số tiết thi lần 2 [SOTIETL2]
### View_CapNhatTKBNgayTKBThi – View cập nhật thời khóa biểu ngày và thi
- Lưới 1 (bảng KTKBNG); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Nhóm/tổ [NhomTo]; Tổ TH [ToTH]; Tên tổ hợp [TenToHop]; Từ ngày [TUNGAYTKB]; Đến ngày [DENNGAYTKB]; Mã phòng [MaPH]; Ngày thi [NgayThi]; Mã phòng thi [MAPHTHI]; Tiết BĐ [TietBD]; Số tiết [SoTiet]
### View_CBBVDC – Cán bộ/giảng viên bảo vệ-phản biện
- Lưới 1 «Cán bộ/giảng viên bảo vệ-phản biện» (bảng DCBBVDC); tắt: Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Nhóm [NhomBVDC]{chọn}; STT [TTCBBV]; Mã NV [MaNV](chỉ đọc); Họ lót [HoLotNV](chỉ đọc); Tên nhân viên [TenNV](chỉ đọc); Mã khoa [MaDV](chỉ đọc); Tên khoa [TenDV](chỉ đọc); Học hàm [IDHocHam](chỉ đọc); Mã học hàm [MaHocHam](chỉ đọc); Cơ quan công tác [CoQuanCT]
### View_CBHDLV – Cán/bộ giảng viên bảo vệ-phản biện
- Lưới 1 «Cán bộ/giảng viên bảo vệ-phản biện» (bảng DCBBVLV); tắt: Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Nhóm [NhomBVLV]{chọn}; STT [TTCBBV]; Mã NV [MaNV](chỉ đọc); Họ lót [HoLotNV](chỉ đọc); Tên nhân viên [TenNV](chỉ đọc); Mã khoa [MaDV](chỉ đọc); Tên khoa [TenDV](chỉ đọc)
### VIEW_CHON_BHNGANH – View chọn bậc hệ ngành
- Lưới 1 «Danh sách bậc hệ ngành»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã BH Ngành [MaBHN]; Mã PB [MaPB]; Tên BH Ngành [TenBHN]; Tên phiên bản [TenPB]
### VIEW_CHON_BO_DEM – Chọn bộ đếm
- Lưới 1 «Chọn bộ đếm»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bộ đếm [MaBoDem](chỉ đọc); Tên bộ đếm [TenBoDem](chỉ đọc); ĐT sử dụng [DTSuDung]{chọn}(chỉ đọc); Loại đối tượng [LoaiDoiTuong]{chọn}(chỉ đọc); Giá trị [GiaTriBoDem]; Học kỳ [HocKy](chỉ đọc); Tháng [Thang]; Năm [Nam]; User SD [UserSD](chỉ đọc); Ký tự đầu [KyTuDau]; Chiều dài [ChieuDai]; Ký tự cuối [KyTuCuoi]
### VIEW_CHON_DT – Chọn dân tộc
- Lưới 1 «Danh sách dân tộc» (bảng NDMDT); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã dân tộc [MaDT]; Tên dân tộc [TenDT]
### VIEW_CHON_DT_1 – Chọn dân tộc
- Lưới 1 «Danh sách dân tộc» (bảng NDMDT); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã dân tộc [MaDT]; Tên dân tộc [TenDT]
### View_Chon_DV_Mul – View chọn đơn vị multi
- Lưới 1 «Danh sách đơn vị»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đơn vị [MaDV]; Tên đơn vị [TenDV]
### VIEW_CHON_DVTKKS – Danh sách đơn vị
- Lưới 1 «Danh sách đơn vị»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đơn vị thống kê [MaDVTKKS]; Tên đơn vị thống kê [TenDVTKKS]
### VIEW_CHON_KHOA_BH – Chọn khoa có bậc hệ
- Lưới 1 «Danh sách khoa»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khoa [MaKhoa]; Tên khoa [TenKhoa]; Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]
### VIEW_CHON_KHOI_CHUNG – View chọn khối
- Lưới 1 «Danh sách khối»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; NHHK vào [NHHKVao]; NHHK ra [NHHKRa]; Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]; Mã Ng/CNg [MaNgChng]; Tên ng/chng [TenNgChng]
### VIEW_CHON_KHOI_DOT – View chọn khối đợt tốt nghiệp
- Lưới 1 «Danh sách đợt và khối» (bảng KDMKHOI); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; NHHK vào [NHHKVao]; NHHK ra [NHHKRa]; Niên khóa [NienKhoa]; Mã đợt [MaDotTN]
### VIEW_CHON_NDMPLNGACH – Danh mục phân loại ngạch
- Lưới 1 «Chọn phân loại ngạch cần in. (LƯU Ý: SỐ LƯỢNG VIÊN CHỨC KHÔNG NẰM TRONG PHÂN LOẠI NGẠCH ĐƯỢC CHỌN SẼ ĐƯỢC ĐẾM VÀO [KHỐI HÀNH CHÍNH] )» (bảng NDMPLNgach); tắt: Nạp lại
  - Cột: Thứ tự [TTPLNgach]; Mã phân loại ngạch [MaPLNgach]; Tên phân loại ngạch [TenPLNgach]; Đếm thêm % từ trình độ trở lên [IDBacNV]
  - Cột ẩn: Ghi chú phân loại ngạch [GcPLNgach]; Tên tiếng anh [TenPLNgachEg]; Viết tắt phân loại ngạch [VtPLNgach]
  - Ô trên form sửa: #TTPLNgach, #MaPLNgach, #TenPLNgach, #GcPLNgach, #TenPLNgachEg, #VtPLNgach
### View_Chon_Nganh_Mul – View chon ngành Mul
- Lưới 1 «Danh sách ngành»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã Ng/CNg [MaNgChng]; Tên ng/chng [TenNgChng]
### VIEW_CHON_PHANLOAINCKH – Chọn phân loại NCKH
- Lưới 1 «Phân loại nghiên cứu khoa học» (bảng ODMPhanLoaiNVNCKH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã phân loại [MaPhanLoaiNVNCKH]; Tên phân loại [TenPhanLoaiNVNCKH]; Số điểm tích lũy [SoDiemChuanTichLuy]; Ghi chú [GCPhanLoaiNVNCKH]
### View_ChonCaLamViec – View chọn ca làm việc
- Lưới 1 «Danh sách ca làm việc» (bảng NCaLamViec); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã ca làm việc [MaCaLamViec]; Tên ca làm việc [TenCaLamViec]; Ghi chú ca làm việc [GCCaLamViec]
### VIEW_CHONDOITUONGKTKTX – Chọn đối tượng khen thưởng ktx
- Lưới 1 (bảng XDTKTX); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã người lưu trú [MADTKTX]; Họ lót [HoLotDT]; Tên [TenDTug]; Phái [PhaiDT]{chọn}; Ngày sinh [NGAYSINHCDT]; Điểm rèn luyện [DIEMRLKTX]; Kết quả xếp loại [KQXLRLKTX]
### VIEW_CHONDOITUONGKTX – Chọn đối tượng ktx
- Lưới 1 «Danh sách nhân viên» (bảng XDTKTX); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã người lưu trú [MADTKTX]; Họ lót [HoLotDT]; Tên [TenDTug]; Phái [PhaiDT]{chọn}; Ngày sinh [NGAYSINHCDT]
### View_ChonHSSV – View chọn hồ sơ sinh viên
- Lưới 1 «Danh sách hồ sơ» (bảng SHSSV); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã hồ sơ [MaHS](chỉ đọc); Tên hồ sơ [TenHS](chỉ đọc); Hình hồ sơ [AvatarHS]; Xem file [XemFile](chỉ đọc); Bản sao` [IsBanSao]; Photo [IsPhoto]; Tạm thời [IsTamThoi]
  - Cột ẩn: Ghi chú [GcHSSV]; Ngày nộp hồ sơ [NgayNopHS]{ngày}
### View_ChonHSSVCopy – View chọn hồ sơ sinh viên
- Lưới 1 «Danh sách hồ sơ» (bảng SHSSV); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã hồ sơ [MaHS](chỉ đọc); Tên hồ sơ [TenHS](chỉ đọc); Ngày nộp hồ sơ [NgayNopHS]{ngày}
  - Cột ẩn: F_FLDHOSO [F_FLDHOSO]
### View_ChonPhaiThuVL – Phải thu vãng lai
- Lưới 1 «Phải thu vãng lai» (bảng MPTVL); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã số [SoGBPTVL]; Đơn vị tính [DonViTinh]; Số lượng [SoLuongPT]; Đơn giá [DonGiaPT]; Số tiền [SOTIENPT]; Thuế VAT (%) [ThueVAT]; Tiền thuế [VATAmount]; Số tiền đã thu [SoTienDaThu]; Số tiền còn nợ [SoTienConNo]; Ghi chú [GCPTVL]
### View_DangKySVNgoai – Đăng ký trực tiếp sinh viên ngoài trường
- Lưới 1 (bảng FKQDKDTNH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Khóa học [IDKhoaHoc]; Mã SV Ngoài [MaSVNgoai]; Tên đầy đủ [TenDayDuSVNgoai]; Ngày sinh [NgaySinhCSVNgoai]; Phái SV ngoài [PhaiSVNgoai]; Số CMND [SoCMND]; Nơi sinh SV ngoài [NoiSinhSVNgoai]; Dân tộc [IDDT]; Số điện thoại sinh viên ngoài [DC_DTSVNgoai]; Địa chỉ email SV ngoài [DC_EmlSVNgoai]; Đơn vị công tác [DC_DCCT]; % học phí miễn giảm [MienGiamDTNH]; Số tiền học phí [SoTienHocPhi]; Ghi chú 1 [GhiChu1]; Diện sinh viên [IDDSV]; Quốc tịch [QuocTich]; Ghi chú 2 [GhiChu2]; Ngày bắt đầu [NgayBD]; Ngày kết thúc [NgayKT]
  - Ô trên form sửa: #IDKhoaHoc, #MaSVNgoai, #TenDayDuSVNgoai, #NgaySinhCSVNgoai, #PhaiSVNgoai, #SoCMND, #NoiSinhSVNgoai, #IDDT, #DC_DTSVNgoai, #DC_EmlSVNgoai, #DC_DCCT, #MienGiamDTNH, #SoTienHocPhi, #GhiChu1, #IDDSV, #QuocTich, #GhiChu2, #NgayBD, #NgayKT
### View_DiemRLCVHTSV – View danh sách điểm rèn luyện CVHT
- Lưới 1 «Danh sách sinh viên»; tắt: Thêm, Sửa, Xóa, Import, In, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã cố vấn học tập [MaCVHT]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Phái [Phai]; Hiện diện SV [HienDienSV]{chọn}; Tổng điểm CVHT [TongDiemCVHT]; Ngày bắt đầu ĐG [NgayBDDKLop]{ngày}; Ngày kết thúc ĐG [NgayKTDKLop]{ngày}; Mã lớp [MaLop]; Mã khối [MaKhoi]; NHHK vào [NHHKVao]; NHHK ra [NHHKRa]; Niên khóa [NienKhoa]; Mã Ng/CNg [MaNgChng]; Mã bậc hệ [MaBH]; Mã bậc [MaBac]; Mã hệ đào tạo [MaHe]; Mã qui chế [MaQC]
  - Cột ẩn: Ngày CVHT cập nhật điểm [NgayCVHTCapNhatDiem]{ngày}; Ngày CVHT đánh giá [NgayCVHTDanhGia]{ngày}; Tên bậc hệ [TenBH]; Tên bậc đào tạo [TenBac]; Tên hệ [TenHe]; Tên khối [TenKhoi]; Tên lớp [TenLop]; Tên ng/chng [TenNgChng]; Tên qui chế [TenQC]
### View_DMSV – Danh Mục Sinh Viên
- Lưới 1 (bảng SSVHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Phái [Phai]; Ngày sinh [NgaySinhC]; Lớp sinh viên [IDLop]
  - Cột ẩn: Sinh viên [IDSV]
  - Ô trên form sửa: #HoLotSV, #TenSV, #Phai, #NgaySinhC, #IDLop, #IDSV
### VIEW_DOITUONGKHENTHG – View hiển thị đối tượng khen thưởng kl ktx
- Lưới 1 «Danh sách đối tượng» (bảng XDTKTX); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã người lưu trú [MADTKTX]; Họ lót [HoLotDT]; Tên [TenDTug]; Phái [PhaiDT]{chọn}; Ngày sinh [NGAYSINHCDT]; Điểm rèn luyện [DIEMRLKTX]; Kết quả xếp loại [KQXLRLKTX]
### View_DoiTuongKTX – Danh sách đối tượng ký túc xá
- Lưới 1 «Chọn đối tượng cần in» (bảng XDMDTLuuTru); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đối tượng [MaDTLuuTru]; Tên đối tượng [TenDTLuuTru]
### View_DSCBChuyenKhoan – Nhập Thông Tin Tổng Hợp Đề Nghị Thanh Toán
- Lưới 1 «Nhập Thông Tin Tổng Hợp Đề Nghị Thanh Toán»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã viên chức [MaNV](chỉ đọc); Họ lót [HoLotNV](chỉ đọc); Tên nhân viên [TenNV](chỉ đọc); Mã đơn vị [MaDV](chỉ đọc); Tên đơn vị [TenDV](chỉ đọc); Số tài khoản [SoTK](chỉ đọc); Số tài khoản 2 [SoTK2](chỉ đọc); Mã ngân hàng [MaNH](chỉ đọc); Tên ngân hàng [TenNH](chỉ đọc); Số tiền [SoTien]{số}; Ghi chú [GHICHUPT]
### View_DSDeCuongMH – View danh sách đề cương môn học
- Lưới 1 «Danh sách đề cương» (bảng KDeCuong); tắt: Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đề cương [MaDeCuong]; Tên đề cương [TenDeCuong]; Ghi chú dùng bên detailright [GhiChuView1]; Người biên soạn [NguoiBienSoan]
  - Ô trên form sửa: #MaDeCuong, #TenDeCuong, #GhiChuView1, #NguoiBienSoan
### View_DSFileDeCuongMH – View danh sách file của đề cương
- Lưới 1 «Danh sách file đề cương» (bảng KFileDeCuong); tắt: Thêm, Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Thứ tự [TTFileDeCuong]; Ghi chú File [GCFileDeCuong]; Tên file [TenFileChiTiet]; Xem file [XemFile]
### View_DSMHPhieuThuHK – Xem chi tiết phiếu thu các học kỳ
- Lưới 1 «Xem chi tiết phiếu thu các học kỳ» (bảng MInVoiceCT); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]{số}; Tổng hp phải đóng [PhaiThu]{số}
  - Cột ẩn: Nhóm học [NhomHoc]
### View_DSMonHocSVVang – Danh sách môn học vắng của sinh viên
- Lưới 1 «Danh sách môn học vắng của sinh viên» (bảng SSVDiemDanh); tắt: Thêm, Sửa, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm/tổ [NhomTo](chỉ đọc); Tổ TH [ToTH](chỉ đọc); Ngày học [NgayHoc]{ngày}(chỉ đọc); Thứ [Thu](chỉ đọc); Tiết BĐ [TietBD](chỉ đọc); Số tiết [SoTiet](chỉ đọc); Ghi chú [GCSVDiemDanh]
### View_DSPhieuNhap – Danh sách phiếu nhập vật tư
- Lưới 1 «Danh sách phiếu nhập»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số biên bản [SoBB]; Ngày lập biên bản [NgayLapBB]{ngày}; Tên đơn vị [TenDV]; Lô nhập [LoNhap]; Ghi chú biên bản [GhiChuBB]
### View_DSSVCapNhatHoSo – Danh sách sinh viên cập nhật hồ sơ
- Lưới 1 «Danh sách sinh viên cập nhật hồ sơ»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Phái [Phai]{chọn}; Ngày sinh [NgaySinhC]; Nhập [IsNhap]; Mã lớp [MaLop]; Mã khối [MaKhoi]; Ngày nhập TTOL [NgayNhapTTOL]{ngày}
### View_DSSVCoVangHocKy – Danh sách sinh viên có vắng học kỳ
- Lưới 1 «Danh sách sinh viên có vắng học kỳ» (bảng SSVHK); tắt: Thêm, Sửa, Xóa, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ và tên [TenDayDu](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Mã Ng/CNg [MaNgChng](chỉ đọc); Hiện diện SV [HienDienSV]{chọn}(chỉ đọc); Mã đơn vị [MaDV](chỉ đọc); Niên khóa [NienKhoa](chỉ đọc); Điện thoại 1 [DC_DT1LLSV](chỉ đọc); Số lượt vắng [SoLuotNguoi](chỉ đọc); Ghi chú [GCSVHKDiemDanh]; Email 1 [DC_EML1LLSV](chỉ đọc); Ghi chú 1 [GhiChu1]
  - Cột ẩn: Điện thoại 1 [DC_DT1HK]
  - Ô trên form sửa: #GhiChu1
### VIEW_DSTBPHDS – Trang thiết bị phòng dạng danh sách
- Lưới 1 «Danh sách phòng» (bảng XPHGKTXThietBi); tắt: Sửa, Xóa, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã phòng [MAPHGKTX]; Tên dãy/tòa nhà [TenDayKtx]; Tên phòng [TENPHGKTX]; Tầng [TangPhong]
  - Cột ẩn: Ghi chú 1 [GhiChu1]
  - Ô trên form sửa: #GhiChu1
### View_DSThoiGianDKLop – Danh sách thời gian đăng ký
- Lưới 1 «Danh sách thời gian» (bảng MTGDKNgayGio); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Ngày bắt đầu đăng ký [NgayBDDKMH]{ngày}; Ngày kết thúc đăng ký [NgayKTDKMH]{ngày}; Giờ bắt đầu [GioBDDK]; Giờ kết thúc [GioKTDK]
### VIEW_DUYETEKQDG – Duyệt danh sách viên chức chưa đạt điểm tối thiểu
- Lưới 1 «Danh sách viên chức chưa đạt điểm tối thiểu» (bảng EKQDG); tắt: Thêm, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Tên chức vụ [TenChucVu]; Tên đơn vị [TenDV]; Tổng điểm [TongDiem]
### VIEW_DUYETEKQDGCOPY – Duyệt danh sách viên chức vượt điểm thưởng đánh gâ
- Lưới 1 «Danh sách viên chức vượt điểm thưởng đánh giá» (bảng EKQDG); tắt: Thêm, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Tên chức vụ [TenChucVu]; Tên đơn vị [TenDV]; Giá trị [GiaTriTL]
### VIEW_ENVNTTHTDG – Danh sách nhân viên nhập hỗ trợ đánh giá
- Lưới 1 «Danh sách nhân viên» (bảng ENVNTTHTDG); tắt: Thêm, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Thứ tự [TTNVNTTHTDG]; Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV](chỉ đọc); Mã đơn vị [MaDV](chỉ đọc); Đơn vị [IDDV](chỉ đọc)
### View_EXport_KQ_GIANGVIEN – Xuất kết quả đánh giá trường
- Lưới 1 «Kết quả đánh giá»; tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Mã môn học [MaMH]; Nhóm/tổ [NhomTo]; Tổ TH [ToTH]; Mã viên chức [MaNV]; Mã đơn vị [MaDV]; TC1 [__TCDG01]; TC2 [__TCDG02]; TC3 [__TCDG03]; TC4 [__TCDG04]; TC5 [__TCDG05]; TC6 [__TCDG06]; TC7 [__TCDG07]; TC8 [__TCDG08]; TC9 [__TCDG09]; TC10 [__TCDG10]; TC11 [__TCDG11]; TC12 [__TCDG12]; TC13 [__TCDG13]; TC14 [__TCDG14]; TC15 [__TCDG15]; TC16 [__TCDG16]; TC17 [__TCDG17]; TC18 [__TCDG18]; TC19 [__TCDG19]; TC20 [__TCDG20]; TC21 [__TCDG21]; TC22 [__TCDG22]; TC23 [__TCDG23]; TC24 [__TCDG24]; TC25 [__TCDG25]; TC26 [__TCDG26]; TC27 [__TCDG27]; TC28 [__TCDG28]; TC29 [__TCDG29]; TC30 [__TCDG30]
### View_EXport_KQ_Truong – Xuất kết quả đánh giá trường
- Lưới 1 «Kết quả đánh giá»; tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Mã lớp [MaLop]; Mã đơn vị [MaDV]; TC1 [__TCDG01]; Tên [TenSV2]; TC2 [__TCDG02]; TC3 [__TCDG03]; TC4 [__TCDG04]; TC5 [__TCDG05]; TC6 [__TCDG06]; TC7 [__TCDG07]; TC8 [__TCDG08]; TC9 [__TCDG09]; TC10 [__TCDG10]; TC11 [__TCDG11]; TC12 [__TCDG12]; TC13 [__TCDG13]; TC14 [__TCDG14]; TC15 [__TCDG15]; TC16 [__TCDG16]; TC17 [__TCDG17]; TC18 [__TCDG18]; TC19 [__TCDG19]; TC20 [__TCDG20]; TC21 [__TCDG21]; TC22 [__TCDG22]; TC23 [__TCDG23]; TC24 [__TCDG24]; TC25 [__TCDG25]; TC26 [__TCDG26]; TC27 [__TCDG27]; TC28 [__TCDG28]; TC29 [__TCDG29]; TC30 [__TCDG30]
### View_FSVLTVL – Danh sách loại thu
- Lưới 1 «Danh sách loại thu» (bảng FSVLTVL); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Mã loại thu vãng lai [MaLTVL](chỉ đọc); Tên loại thu vãng lai [TenLTVL](chỉ đọc); Đơn giá vãng lai [DonGiaVL](chỉ đọc); Số lượng [SoLuongVL]; Thành tiền [ThanhTienVL](chỉ đọc)
### View_GanSVCoDKMHVaoToThi – Gán sinh viên có đăng ký môn học vào tổ thi
- Lưới 1 «Danh sách môn học»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Mã môn học [MaMH](chỉ đọc); Nhóm/tổ [NhomTo](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm thi [IDNhomThi]; Tổ thi [IDToThi]
### View_GanSVCoDKMHVaoToThi_DangDS – Gán sinh viên có đăng ký môn học vào tổ thi
- Lưới 1 «Danh sách môn học của sinh viên»; tắt: Thêm, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Nhóm/tổ [NhomTo](chỉ đọc); Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm thi [IDNhomThi]; Tổ thi [IDToThi]
### View_GanTGBaoVeDeCuong – Gán thời gian bảo vệ đề cương
- Lưới 1 «Gán thời gian bảo vệ đề cương» (bảng DDKDeTaiLV); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Tên đề tài [TenDeTaiLV](chỉ đọc); Thời gian bắt đầu bảo vệ [TGBDBVDC]{ngày}; Mã HĐBV đề cương [MaHDBVDC](chỉ đọc); Tên HĐBV đề cương [TenHDBVDC](chỉ đọc); Ngày BVĐC [NgayBVDC]{ngày}(chỉ đọc); Số phút/1 đề tài [SoPhutBV1LV](chỉ đọc)
### View_GanTGBaoVeLuanVan – Gán thời gian bảo vệ luận văn
- Lưới 1 «Gán thời gian bảo vệ luận văn» (bảng DSVBVLV); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Tên đề tài [TenDeTaiLV](chỉ đọc); Thời gian bắt đầu bảo vệ [TGBDBVLV]{ngày}; Mã HĐBV luận văn [MaHDBVLV](chỉ đọc); Tên HĐBV luận văn [TenHDBVLV](chỉ đọc); Ngày bảo vệ [NgayBVLV]{ngày}(chỉ đọc); Số phút/1 đề tài [SoPhutBV1LV](chỉ đọc)
### VIEW_GMUCLPHK – View nhập các mức hệ số lớp cho từng học kỳ
- Lưới 1 «Danh sách mức hệ số theo đối tượng» (bảng GMUCLPHK); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã mức [MaMucLP]; Tên mức [TenMucLP]; Hệ số [HSMUCLP]{số}; Diễn giải [DGLPHK]
  - Cột ẩn: Mã mức [IDMucLP]
  - Ô trên form sửa: #TenMucLP, #HSMUCLP, #DGLPHK, #IDMucLP
### VIEW_GQuiDoiDM – View nhập qui đổi định mức
- Lưới 1 «Nhập qui đổi định mức» (bảng GQuiDoiDM); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã loại học hàm [MaLHH]; Tên loại học hàm [TenLHH]; Giờ qui đổi [SoGioQD]{số}
  - Cột ẩn: Loại học hàm [IDLHH]
  - Ô trên form sửa: #TenLHH, #SoGioQD, #IDLHH
### View_HDBVDC – Danh sách hội đồng bảo vệ đề cương
- Lưới 1 «Danh sách hội đồng bảo vệ đề cương» (bảng DHDBVDC); tắt: In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã hội đồng [MaHDBVDC]; Tên hội đồng [TenHDBVDC]; Ngày BVĐC [NgayBVDC]; Số phút/1 đề tài [SoPhutBV1LV]; Số quyết định [SoQDBVDC]; Ngày quyết định [NgayQDBVDC]; Ghi chú [GCHDBVDC]
  - Cột ẩn: Ghi chú 1 [GhiChu1]; Đợt bảo vệ luận văn [IDDotBVLV]; Nhóm HĐBV luận văn [IDNhHDBVLV]; Mã phòng học [IDPH]; Hình quyết định [ImageQDBVDC]
  - Ô trên form sửa: #MaHDBVDC, #TenHDBVDC, #NgayBVDC, #SoPhutBV1LV, #SoQDBVDC, #NgayQDBVDC, #GCHDBVDC, #GhiChu1, #IDDotBVLV, #IDNhHDBVLV, #IDPH, #ImageQDBVDC
### View_HDBVLV – Danh sách hội đồng bảo vệ luận văn
- Lưới 1 «Danh sách hội đồng bảo vệ» (bảng DHDBVLV); tắt: In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã hội đồng [MaHDBVLV]; Tên hội đồng [TenHDBVLV]; Ngày bảo vệ [NgayBVLV]; Số phút/1 đề tài [SoPhutBV1LV]; Số quyết định [SoQDBVLV]; Ngày quyết định [NgayQDBVLV]
  - Cột ẩn: Địa chỉ [DiaChiHDBVLV]; Ghi chú HĐBVLV [GCHDBVLV]; Ghi chú 1 [GhiChu1]; Đợt bảo vệ luận văn [IDDotBVLV]; Nhóm HĐBV luận văn [IDNhHDBVLV]; Mã phòng học [IDPH]; Hình quyết định [ImageQDBVLV]; Tên người ký [TenNguoiKy]
  - Ô trên form sửa: #MaHDBVLV, #TenHDBVLV, #NgayBVLV, #SoPhutBV1LV, #SoQDBVLV, #NgayQDBVLV, #DiaChiHDBVLV, #GCHDBVLV, #GhiChu1, #IDDotBVLV, #IDNhHDBVLV, #IDPH, #ImageQDBVLV, #TenNguoiKy
### View_HDDT_KTX – Danh sách thu ký túc xá
- Lưới 1 «Danh sách thu ký túc xá»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Tìm [ButtonView_Tim](chỉ đọc); Mẫu số HDDT [MauSoHDDT]; Ký hiệu hóa đơn [KyHieuHDDT]; Số HDDT [SoHDDT]; Ngày lập HDDT [NgayLapHDDT]; Mã người lưu trú [MADTKTX](chỉ đọc); Họ lót [HoLotDT](chỉ đọc); Tên [TenDTug](chỉ đọc); Phái [PhaiDT]{chọn}(chỉ đọc); Ngày sinh [NGAYSINHCDT](chỉ đọc); Xuất HDDT [IsXuatHDDT](chỉ đọc); Ngày thu/chi [NgayTChi]{ngày}(chỉ đọc); Số chứng từ [SoCTu](chỉ đọc); Số tiền thu [SOTIENTHUKTX](chỉ đọc); Thu ngân hàng [THUNH](chỉ đọc); Tiền phân bổ sử dụng [TIENPBKTXSD](chỉ đọc); Quyển số [QUYENSO](chỉ đọc); Số C.Từ ngân hàng [SoCTuNH](chỉ đọc); Ghi chú [GHICHUPT](chỉ đọc); Ngày thêm [NgayThem]{ngày}(chỉ đọc)
### View_HideMenu_NETWeb – View ẩn chức năng Net WEB
- Lưới 1 (bảng AQDMChucNang); tắt: Thêm, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã chức năng [MaChucNang](chỉ đọc); Tên chức năng [TenChucNang](chỉ đọc); Ẩn menu [HideWeb]; Tên chức năng custom [TenChucNangCustom]; ID chức năng cha [IDChucNangParent]
### View_HieuChinhNgayNgoaiLe – Danh sách thời khóa biểu ngày ngoại lệ
- Lưới 1 «Danh sách thời khóa biểu» (bảng KTKBNGNgoaiLe); tắt: Thêm, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Số thứ tự [Stt]{số}; Ngày học [NgayHoc]{ngày}; Tiết BĐ [TietBD]{số}; Số tiết [SoTiet]{số}
### VIEW_HieuChinhPhiKTX – Hiệu chỉnh phí ký túc xá
- Lưới 1 «Danh sách hóa đơn»; tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã người lưu trú [MADTKTX](chỉ đọc); Họ lót [HoLotDT](chỉ đọc); Tên [TenDTug](chỉ đọc); Phái [PhaiDT]{chọn}(chỉ đọc); Mã phòng [MAPHGKTX](chỉ đọc); Tên dịch vụ [TenDICHVUKTX](chỉ đọc); Số tiền tự tính [SoTienInvKTX](chỉ đọc); Số tiền hiệu chỉnh [SoTienInvKTXGoc]; Ghi chú hiệu chỉnh [GCHieuChinh]; User hiệu chỉnh [UserHieuChinhKTX](chỉ đọc)
  - Cột ẩn: Năm [NamInvKTX](chỉ đọc); Số Invoice [SoInvKTX](chỉ đọc); Tháng [ThangInvKTX](chỉ đọc)
### View_HieuChinhSVNhom – Hiệu chỉnh sinh viên trong nhóm thi
- Lưới 1 «Danh sách sinh viên dự thi» (bảng LKQDKDThi); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Mã SV [MaSV](chỉ đọc); Họ và tên [TenDayDu](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Nhóm/tổ [NhomTo](chỉ đọc); Tổ TH [ToTH](chỉ đọc); Nhóm thi hiện tại [NhomTC](chỉ đọc); Nhóm thi hiệu chỉnh [IDToThi]; Ghi chú kết quả đăng ký dự thi [GCKQDKDThi]
  - Cột ẩn: Nhóm thi [NhomThi]; Tên hình thức thi [TenHTThi](chỉ đọc)
### View_HieuChinhSVTrongToThi – Hiệu chỉnh sinh viên trong tổ thi
- Lưới 1 «Danh sách môn học» (bảng LKQDKDThi); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm thi ban đầu [NhomBD](chỉ đọc); Nhóm thi [NhomToCT](chỉ đọc); Tổ thi [ToTH1](chỉ đọc); Sỉ số [SiSoDuKien](chỉ đọc); Tổ thi con [ToThiCon](chỉ đọc); Ngày thi [NgayThi]{ngày}(chỉ đọc); Giờ bắt đầu [GioBD](chỉ đọc); Giờ thi [GioThi](chỉ đọc); Mã phòng [MaPH](chỉ đọc); Nhóm thi chuyển [IDNhomThi]; Tổ thi chuyển [IDToThi]; Ghi chú chuyển [GCKQDKDThi]; Số phút thi [SoPhutThi](chỉ đọc); Tên hình thức thi [TenHTThi](chỉ đọc)
### View_HMenuCustom – View dời vị trí Menu
- Lưới 1 (bảng AQDMChucNang); tắt: Thêm, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã chức năng [MaChucNang](chỉ đọc); Tên chức năng [TenChucNang](chỉ đọc); ID chức năng cha [IDChucNangParent]; Ẩn menu [HideWeb]; Tên chức năng custom [TenChucNangCustom]; Tên tiếng anh [TenChucNangCustomEg]
### View_HMenuCustom_HideWeb – View ẩn chức năng web
- Lưới 1 (bảng AQDMChucNang); tắt: Thêm, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã chức năng [MaChucNang](chỉ đọc); Tên chức năng [TenChucNang](chỉ đọc); Ẩn menu [HideWeb]; ID chức năng cha [IDChucNangParent]
### VIEW_IMP_SELECT_SVN2 – Import select sinh viên ngành 2
- Lưới 1 (bảng SSVHKN2); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### View_ImpDiemRLSV – Import điểm rèn luyện sinh viên
- Lưới 1 (bảng SKetQuaDGRLCT); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Thứ tự [TTNhomCauHoiDGRL]; Thứ tự câu hỏi DGRL [TTCauHoiDGRL]; Điểm số sinh viên [DiemSoSV]; Điểm số CVHT [DiemSoCVHT]; Điểm số khoa [DiemSoKhoa]
### View_ImpDSSVVang – Import danh sách sinh viên vắng
- Lưới 1 (bảng SDiemDanh); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Mã SV [MaSV]; Mã môn học [MaMH]; Mã nhóm học [MaNhomHoc]; Tên tổ hợp [TenToHop]; Ngày điểm danh [NgayDiemDanh]; Ngày nhập [NgayNhapVaoLop]; Tiết BĐ [TietBD]; Số tiết [SoTiet]; Key tổ hợp [KeyToHop]
### View_ImpGCSVDiemDanh – Import ghi chú sinh viên vắng
- Lưới 1 (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Mã môn học [MaMH]; Ngày học [NgayHoc]; Tiết BĐ [TietBD]; Ghi chú [GCSVDiemDanh]
### View_ImpGhiChuSVVang – Import ghi chú sinh viên vắng học kỳ
- Lưới 1 (bảng SSVHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Ghi chú sinh viên HK điểm danh [GCSVHKDiemDanh]
### View_Import_GCToHoc – View_Import_GCToHoc
- Lưới 1 (bảng KToHoc); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Nhóm học [NhomHoc]; Tổ TH [ToTH]; Ghi chú [GCToHoc]
### View_Import_LDKCoiThiKhac – View_Import_LDKCoiThiKhac
- Lưới 1 (bảng LDKCoiThiKhac); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Nhóm thi [NhomThi]; Tổ thi [ToThi]; KH điểm TP [KyHieuTP]; Mã quyền coi thi [MaQuyenCoiThi]; Mã viên chức [MaNV]; Ngày giờ đăng ký [NgayGioDKCoiThi]
### VIEW_IMPORT_NHOMHOC – View_Import_NhomHoc
- Lưới 1 (bảng KToHoc); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Nhóm học [NhomHoc]; Tổ TH [ToTH]; Mã mới [MAMOI]
### View_Import_VanBang – Import theo file van banng tot nghiep
- Lưới 1 (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]
### View_ImportHDDT – Import hóa đơn điện tử
- Lưới 1 «Import hóa đơn điện tử» (bảng MPTHU); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã SV [MaSV](chỉ đọc); Họ và tên [TenDayDu](chỉ đọc); Quyển số [QUYENSO](chỉ đọc); Số chứng từ [SoCTu](chỉ đọc); Mã nhóm [MaNhCT](chỉ đọc); Nhóm vãng lai [IsNhomVL](chỉ đọc); Số HDDT [SoHDDT]; Ngày lập HDDT [NgayLapHDDT]{ngày}; Mẫu số HDDT [MauSoHDDT]; Ký hiệu hóa đơn [KyHieuHDDT]
### View_ImportSVChuyenNhomThi – View import sinh viên chuyển nhóm thi
- Lưới 1 (bảng LKQDKDThi); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Mã SV [MaSV]; Nhóm thi [NhomThi]; Tổ thi [ToThi]; Ghi chú kết quả đăng ký dự thi [GCKQDKDThi]
### View_ImpSDPhongDotXuat – Import sử dụng phòng đột xuất
- Lưới 1 (bảng KSDPHHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lý do [MaLDSDPH]; Thứ [Thu]; Tiết BĐ [TietBD]; Số tiết [SoTiet]; Mã phòng [MaPH]; Mã viên chức [MaNV]; Mã lớp [MaLop]; Mã môn học [MaMH]; Mã đơn vị [MaDV]; Diễn giải [DienGiaiSD]
### View_ImpTGNhapDiem – Danh sách nhóm thi
- Lưới 1 (bảng LToThi); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: KH điểm TP [KyHieuTP]; Tổ thi [ToThi]; Nhóm thi [NhomThi]; Mã môn học [MaMH]; IDNVChamThi [IDNVChamThi]; Ngày bắt đầu nhập điểm [NgayBDNhapDiem]; Ngày kết thúc nhập điểm [NgayKTNhapDiem]
### View_ImpVatTu – View import vật tư
- Lưới 1 (bảng JDmTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã tài sản/vật tư [MaTS]; Số lượng chứng từ [SoLuongChungTu]; Mã Đơn vị tính [MaDVTinh]; Số lượng nhập [SoLuongNhap]; Đơn giá [DonGiaTS]; Thuế VAT (%) [ThueVAT]
### View_ImpVatTuKK – View import vật tư kiểm kê
- Lưới 1 (bảng JDmTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã tài sản/vật tư [MaTS]; Số lượng kiểm kê [SoLuongKK]
### View_KhoaMucSoTCHPMonHoc – Khóa mức đơn giá và số TCHP môn học
- Lưới 1 «Khóa mức đơn giá và số TCHP môn học»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Số TC học phí [SoTinChiHP](chỉ đọc); Mức đơn giá LT [MucDGLT](chỉ đọc); Mức ĐGLT học lại [MucDGLTHL](chỉ đọc); Mức ĐGTH học lại [MucDGTHHL](chỉ đọc); Khóa sổ [IsKhoaSo]
### View_KiemTraKQDKWeb – Danh sách kết quả đăng ký
- Lưới 1 «Danh sách kết quả đăng ký»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Nhóm/tổ [NhomTo]; Mã lớp [MaLop]; Ngày đăng ký [NgayDK]{ngày}; Ngày in [NgayIn]{ngày}
### VIEW_LOG_MONBB – Nhật ký môn bắt buộc
- Lưới 1 «Nhật ký môn bắt buộc»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Mã MH cũ [MaMHCu]; User thực hiện [USERTHUCHIEN]; Ngày thực hiện [NGAYTHUCHIEN]{ngày}
### VIEW_MH_KHG_PHI_TAI_LIEU – Môn học không tính phí tài liệu
- Lưới 1 «Danh sách môn học không tính tài liệu» (bảng MMHMGTaiLieu); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Số TC [SoTinChi]; Tên môn học [TenMH]
  - Cột ẩn: Đối tượng [IDDoiTuong]
  - Ô trên form sửa: #SoTinChi, #TenMH, #IDDoiTuong
### VIEW_MH_KHOA – View môn học khoa
- Lưới 1 «Danh sách môn học»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Mã khoa quản lý bộ môn [MaKhoaBM]; Tên khoa quản lý bộ môn [TenKhoaBM]
### VIEW_MHTD – Định nghĩa môn học tương đương.
- Lưới 1 «Danh sách môn học tương đương» (bảng DMHTD); tắt: Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Mã MH tương đương [MaMHTD]; Tên MH tương đương [TenMHTD]; Số TCTĐ [SoTinChiTT]
  - Cột ẩn: Mã MH [IDMH1]; Mã MH tương đương [IDMH2]
  - Ô trên form sửa: #TenMH, #SoTinChi, #TenMHTD, #SoTinChiTT, #IDMH1, #IDMH2
### View_NhapDiemRL1SV – Nhập điểm rèn luyện 1 sinh viên
- Lưới 1 «Thông tin điểm rèn luyện» (bảng SDRLHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Niên học học kỳ [NHHK](chỉ đọc); Điểm rèn luyện học kỳ [DiemRLHK]{số}
### VIEW_NHAPQDKTX – View nhập quyết định ktx
- Lưới 1 «Danh sách quyết định» (bảng XQDRLKTX); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số QĐ [SoQDRLKTX]; Tên quyết định [TenQDRLKTX]; Ngày lập QĐ [NgayQDRLKTX]{ngày}; Người ký QĐ [NguoiKyQDKTX]
  - Cột ẩn: Ghi chú [GCQDRLKTX]; Ghi chú dùng bên detailright [GhiChuView1]
  - Ô trên form sửa: #SoQDRLKTX, #TenQDRLKTX, #NgayQDRLKTX, #NguoiKyQDKTX, #GCQDRLKTX, #GhiChuView1
### View_NhatKyTraVeMacDinh – Nhật ký view trả về mặc định
- Lưới 1 «Nhật ký view trả về mặc định»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã View [MAVIEW1]; Tên trường thông tin [TenView1]; Ghi chú [GcView1]; Mã user [MaUser]; Ngày thực hiện [CreatedTime]
### VIEW_NHOM_KHONG_TINH_TAI_LIEU – View nhóm không tính phí tài liệu
- Lưới 1 «Danh sách nhóm không tính phí tài liệu» (bảng MMHMGTaiLieu); tắt: In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm/tổ [NhomTo]
  - Cột ẩn: Đối tượng [IDDoiTuong]
  - Ô trên form sửa: #MaMH, #TenMH, #NhomTo, #IDDoiTuong
### VIEW_NQTHTUV – Giao diện quá trình học tập ứng viên
- Lưới 1 «Quá trình học tập ứng viên» (bảng NQTHTUV); tắt: Thêm, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Trình độ [IDBacNV]; Ngành [IDNganhNV]; Trường [IDTruongHoc]; Ngày tốt nghiệp [NgayTotNghiep]{ngày}; Ngày bắt đầu học [BDHocUV]; Ngày kết thúc học [KTHocUV]
### VIEW_NQTVBCCUV – Giao diện quá trình văn bằng chứng chỉ ứng viên
- Lưới 1 «Danh sách văn bằng chứng chỉ» (bảng NQTVBCCUV); tắt: Thêm, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Loại văn bằng/ chứng chỉ [IDVBCC]; Số VBCC [SoVBCC]; Ngày bắt đầu học [NgayBDH]{ngày}; Ngày hoàn tất [NgayKTH]{ngày}; Xếp loại [XepLoai]{chọn}; Ngày nhận [NgayNhan]{ngày}; Trường đào tạo [TruongDT]; Nơi cấp CMND [NoiCap]
### View_PhaiThuVL – Phải thu vãng lai
- Lưới 1 «Phải thu vãng lai» (bảng MPTVL); tắt: In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Mã loại thu vãng lai [MaLTVL]; Tên loại thu vãng lai [TenLTVL]; Mã số [SoGBPTVL]; Đơn vị tính [DonViTinh]; Số lượng [SoLuongPT]; Đơn giá [DonGiaPT]; Số tiền [SOTIENPT]; Thuế VAT (%) [ThueVAT]; Tiền thuế [VATAmount]; Ghi chú [GCPTVL]
  - Cột ẩn: Loại thu [IDLTVL]; Sinh viên [IDSV]
  - Ô trên form sửa: #SoGBPTVL, #DonViTinh, #SoLuongPT, #DonGiaPT, #SOTIENPT, #ThueVAT, #VATAmount, #GCPTVL, #IDLTVL, #IDSV
### VIEW_QLKTX – View quản lý ký túc xá
- Lưới 1 «Danh sách thành viên ban tự quản» (bảng XQLKTX); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Cấp quản lý [CapTruongKTX]{chọn}; Mã người lưu trú [MADTKTX]; Họ và tên [HoTenDT]; Là cấp phó [CapPhoKTX]{chọn}; Mã đối tượng [MaDoiTuong]; Từ ngày [TuNgayCVKTX]{ngày}; Đến ngày [DenNgayCVKTX]{ngày}
  - Cột ẩn: Đối tượng QLKTX [IDDTQLKTX]; Quản lý [IDQuanLy]
  - Ô trên form sửa: #CapTruongKTX, #HoTenDT, #CapPhoKTX, #TuNgayCVKTX, #DenNgayCVKTX, #IDDTQLKTX, #IDQuanLy
### VIEW_SDMBVKCB – Danh mục bệnh viện khám chữa bệnh
- Lưới 1 «Danh sách bệnh viện khám chữa bệnh» (bảng SDMBVKCB); tắt: Thêm, Xóa, Import, Xuất, In, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã BVKCB [MaBVKCB]; Tên BVKCB [TenBVKCB]; Viết tắt [VtBVKCB]; Ghi chú [GcBVKCB]
### View_SettingLyLichSV – Setting thông tin lý lịch sinh viên
- Lưới 1 «Danh sách field»; tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Loại thông tin [ThongTin](chỉ đọc); Không hiển thị [IsNotVisible]; Không hiệu chỉnh [IsNoEdit]; Bắt buộc nhập [IsBatBuoc]; Không cho sửa khi đã lưu thông tin [IsEnableNotNull]
### View_SGCNOnline – View cập nhật giấy chứng nhận online
- Lưới 1 «Danh sách sinh viên đăng ký giấy chứng nhận online» (bảng SGCNSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên giấy CN [TenGCN](chỉ đọc); Mã SV [MaSV](chỉ đọc); Nơi sinh [NoiSinh](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Phái [Phai]{chọn}(chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Số chứng nhận [SOCNSV](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Ngày đăng ký [NgayDKGCN](chỉ đọc); Ghi chú [GCGCNSV]; Trạng thái GCN [TrangThaiGCNSV]{chọn}; Phản hồi [GCGCNSV2]
  - Cột ẩn: Còn Nợ [ConNo](chỉ đọc); GC giấy CNSV 2 [GCGCNSV1]; GCSurvey [GCSurvey](chỉ đọc); Trạng thái [IsDaDuyet]{chọn}; Ngày cấp GCN [NgayCapGCN]{ngày}; RateSurvey [RateSurvey](chỉ đọc); Số TCDKHK [SOTCDKHK](chỉ đọc); TCTLHK [SoTCTLHK](chỉ đọc)
### VIEW_SUASISOTHOC – View sua si so to hoc
- Lưới 1 «Xem sửa nhanh giá trị các sỉ số của nhóm tổ học» (bảng KToHoc); tắt: Thêm, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm/tổ [NhomTo](chỉ đọc); Nhóm TC [NhomTC](chỉ đọc); Tổ TH [ToTH](chỉ đọc); Ngày bắt đầu [NgayBD]; Sĩ số đã đăng ký [SiSoDDK](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Mã PH [MaPhHK](chỉ đọc); Mã Khoa/BM [MaKhoaBM](chỉ đọc); DSCBGD [DSCBGD](chỉ đọc); Tên đầy đủ [TenDayDuNV](chỉ đọc); Sỉ số TKB [SiSoTKB]{số}; Sỉ số cho ĐK [SiSoCPDK]{số}
  - Cột ẩn: Đề án [DA](chỉ đọc); Luận án [LA](chỉ đọc); Lý thuyêt [LT](chỉ đọc); Sĩ số phòng [SiSoPH]{số}(chỉ đọc); Sức chứa [SucChuaPH](chỉ đọc); Thực hành [TH](chỉ đọc); Thực tập [TT](chỉ đọc); Tên Khoa/BM [TenKhoaBM](chỉ đọc)
### VIEW_SVVNH – Danh sách sinh viên vay vốn ngân hàng
- Lưới 1 «Danh sách sinh viên vay vốn» (bảng SSVVV); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Mã lớp [MaLop]; Mã ngân hàng [MaNH]; Số tiền vay [SoTienVay]{số}; Ngày ký [NgayKy]{ngày}
  - Cột ẩn: Ghi chú [GhiChu]; Ngân hàng [IDNH]; Sinh viên [IDSV]; Họ và tên [TenDayDu]; Tên ngân hàng [TenNH]
  - Ô trên form sửa: #MaLop, #SoTienVay, #NgayKy, #GhiChu, #IDNH, #IDSV, #TenDayDu, #TenNH
### View_TestChonDMSVACB – Chọn SV ACB
- Lưới 1 (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Phái [Phai]
### VIEW_TGDONGHPONLINE_SV – Thời gian đóng học phí online theo sv
- Lưới 1 «Danh sách sinh viên» (bảng MTGDongHPOnline); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ và tên [TenDayDu](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Phái [Phai](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Tên lớp [TenLop](chỉ đọc); Niên khóa [NienKhoa](chỉ đọc); Ngày bắt đầu [NgayBDDong]{ngày}; Ngày kết thúc [NgayKTDong]{ngày}
### VIEW_THEMDSSVH – Thêm danh sách sinh  viên  học kỳ
- Lưới 1 (bảng SSVHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột ẩn: Hiện diện SV [HienDienSV]; Lớp sinh viên [IDLop]; Niên học học kỳ [NHHK]
  - Ô trên form sửa: #HienDienSV, #IDLop, #NHHK
### View_ThemMHTQHB – View thêm mh tqHB
- Lưới 1 «Danh sách môn học tiên quyết»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc)
### VIEW_THEMNV – Thêm nhân viên từ quyết định vào mới
- Lưới 1 (bảng NDMNV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Ngày sinh [NgSinhNVCNV]
  - Cột ẩn: Hình nhân viên [AvatarNV]; Ghi chú [GCNV]; Họ lót [HoLotNV]; Mã viên chức [MaNV]; Nơi sinh [NoiSinhNV]; Phái [PhaiNV]; Tên đầy đủ [TenDayDuNV]; Tên nhân viên [TenNV]
  - Ô trên form sửa: #AvatarNV, #GCNV, #HoLotNV, #MaNV, #NoiSinhNV, #PhaiNV, #TenDayDuNV, #TenNV
### VIEW_THEMSV – Thêm sinh viên từ qd vào mới
- Lưới 1 (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Phái [Phai]; Nơi sinh [NoiSinh]; Ghi chú [GcSV]; Hình sinh viên [AvatarSV]
  - Ô trên form sửa: #MaSV, #HoLotSV, #TenSV, #TenDayDu, #NgaySinhC, #Phai, #NoiSinh, #GcSV, #AvatarSV
### VIEW_ThongKeGioGV – View thống kê giờ giảng của giảng viên
- Lưới 1 «Danh sách nhóm môn học» (bảng KToHoc); tắt: Thêm, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm/tổ [NhomTo](chỉ đọc); Nhóm TC [NhomTC](chỉ đọc); Tổ TH [ToTH](chỉ đọc); Ngày bắt đầu [NgayBD]; Sĩ số phòng [SiSoPH]{số}(chỉ đọc); Sĩ số đã đăng ký [SiSoDDK](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Mã PH [MaPhHK](chỉ đọc); Mã khoa quản lý bộ môn [MaKhoaBM](chỉ đọc); DSCBGD [DSCBGD](chỉ đọc); Tên đầy đủ [TenDayDuNV](chỉ đọc); SL trung bình nhóm [SiSoTKB]{số}; Sĩ số cho phép đk [SiSoCPDK]{số}
  - Cột ẩn: Đề án [DA](chỉ đọc); Luận án [LA](chỉ đọc); Lý thuyêt [LT](chỉ đọc); Sức chứa [SucChuaPH](chỉ đọc); Thực hành [TH](chỉ đọc); Thực tập [TT](chỉ đọc); Tên khoa quản lý bộ môn [TenKhoaBM](chỉ đọc); Tên tổ hợp [TenToHop]
### View_ThongTinChiTietKK – View xem chi tiết khen thưởng kỷ luật
- Lưới 1 «Danh sách kỷ luật» (bảng SDSQDKK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Loại lý do [LoaiKKSV]{chọn}; Tên khen thưởng kỷ luật [TenKKSV]; Niên học học kỳ [NHHK]; Số quyết định [SoQDKK]; Ngày ký [NgayKyKK]{ngày}
### View_ThongTinChiTietKKCopy – View xem chi tiết khen thưởng
- Lưới 1 «Danh sách khen thưởng» (bảng SDSQDKK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Loại lý do [LoaiKKSV]{chọn}; Tên khen thưởng kỷ luật [TenKKSV]; Niên học học kỳ [NHHK]; Số quyết định [SoQDKK]; Ngày ký [NgayKyKK]{ngày}
### View_ThongTinChiTietQD – Thong tin xem chi tiet quyet dinh
- Lưới 1 «Danh sách quyết định» (bảng SDSQD); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Loại lý do [LoaiLDQDSV]{chọn}; Tên lý do [TenLDQDSV]; Niên học học kỳ [NHHK]; Số quyết định [SoQDSV]; Ngày lập QĐ [NgayLapQDSV]{ngày}; Ghi chú [GcQDSV]; Số học kỳ nghỉ [SoHKNghi]; Mã lớp (cũ) [MaLopCu]; Mã lớp (mới) [MaLopMoi]
### View_ThongTinChiTietQDCopy – Thong tin xem chi tiet quyet dinh
- Lưới 1 (bảng SDSQD); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Loại lý do [LoaiLDQDSV]{chọn}; Tên lý do [TenLDQDSV]; Niên học học kỳ [NHHK]; Số quyết định [SoQDSV]; Ngày lập QĐ [NgayLapQDSV]{ngày}; Số học kỳ nghỉ [SoHKNghi]
### View_ThongTinTraHS – View thông tin trả hồ sơ
- Lưới 1 «Danh sách hồ sơ»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã hồ sơ [MaHS](chỉ đọc); Tên hồ sơ [TenHS](chỉ đọc); Trả HS [IsTraHS]; Ngày trả HS [NgayTraHS]{ngày}; Tên người nhận [TenNguoiNhanHS]; Tên người trả [TenNguoiTraHS]; Ghi chú [GcTraHoSo]
### View_TimKiemSV – View tìm kiếm sinh viên
- Lưới 1 «Danh sách sinh viên» (bảng SSVHK); tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Phái [Phai]; Mã lớp [MaLop]; Hiện diện SV [HienDienSV]{chọn}; Số vào sổ [SoVaoSo]; Ngày vào sổ [NGAYVAOSO]{ngày}; Số văn bằng [SOVBSV]; Ngày thanh toán [NgayTT]{ngày}; Ngày cấp [NgayCap]{ngày}; Số QĐ [SoQD]; Ghi chú [GhiChuTN]; ĐTK [DTBTK]{số}; Xếp loại toàn khóa [XepLoaiTK]; ĐTBTN [DTBTN]{số}; Xếp loại tốt nghiệp [XepLoaiTN]; Số quyết định [SoQDSV]; Ngày lập QĐ [NgayLapQDSV]{ngày}
  - Cột ẩn: Khóa học [KhoaHocTC]; Ngày thêm [NgayThem]
### VIEW_TINH_HAO_MON – Tính hao mòn tài sản
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### View_TTNCKH – Thông tin Nghiên cứu Khoa học
- Lưới 1 «Thông tin Nghiên cứu Khoa học» (bảng DNCKHOAHOC); tắt: Thêm, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Mã SV [MaSV](chỉ đọc); Ghi chú [GCNKHHOC]; Tên đề tài [DeTaiNCKH]; Tên đề tài tiếng anh [DeTaiNCKHEg]
### VIEW_XEMBIENDONGSV – View xem danh sách sinh viên biến động
- Lưới 1 «Danh sách sinh viên» (bảng SDSSVQD); tắt: Thêm, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Số quyết định [SoQDSV]; Ngày lập QĐ [NgayLapQDSV]{ngày}; Ngày hiệu lực [NGAYHLQDSV]{ngày}; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Phái [Phai]; Loại lý do [LoaiLDQDSV]{chọn}; Mã lý do [MaLDQDSV]; Mã lớp (cũ) [MaLopCu]; Mã lớp (mới) [MaLopMoi]; Số học kỳ nghỉ [SoHKNghi]; Ngày thêm [NgayThem]{ngày}; Mã user [MaUser]; Ghi chú [GcDSSVQD]
  - Cột ẩn: Mã dân tộc [MaDT]; Mã khoa [MaKhoa]; Mã ngành [MaNganh]; Mã tôn giáo [MaTG]; Ngày sinh [NgaySinhC]; Tên dân tộc [TenDT]; Tên tôn giáo [TenTG]
### View_XemCTPhieuThuHK – Xem chi tiết phiếu thu các học kỳ
- Lưới 1 «Xem chi tiết phiếu thu các học kỳ»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Số chứng từ [SoCTu]; Ngày thu/chi [NgayTChi]{ngày}; Số tiền thu [TienPT]{số}; SoInvoice [SoInvoice]; Hủy [IsHuyInvoice]; Tổng hp phải đóng [PhaiThu]{số}; NHHK thu HP [NHHKThuHP]
  - Cột ẩn: Ghi chú 1 [GhiChu1]
  - Ô trên form sửa: #GhiChu1
### View_XemHDSinhHoatSV – Xem hoạt động sinh hoạt sinh viên
- Lưới 1 «Danh sách hoạt động sinh viên»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Buổi sinh hoạt [DienGiaiSD]; Nội dung [LyDoSDPHHK]; Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Tiết BĐ [TietBD]; Số tiết [SoTiet]; Từ ngày [TuNgay]{ngày}; Đến ngày [DenNgay]{ngày}; Mã phòng [MaPH]
### View_XemKTKL – View xem quyết định khen thưởng
- Lưới 1 (bảng SSVHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Mã lớp [MaLop]; Ghi chú dùng bên detailright [GhiChuView1]; Bài tập [BT]
  - Ô trên form sửa: #MaSV, #TenDayDu, #MaLop, #GhiChuView1, #BT
### View_XemQuyetDinh – View xem quyết định vao ra SV
- Lưới 1 (bảng SSVHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Mã lớp [MaLop]; Ghi chú dùng bên detailright [GhiChuView1]
  - Ô trên form sửa: #MaSV, #TenDayDu, #MaLop, #GhiChuView1
### View_XoaPhieuBaoHP – Danh sách phiếu báo học phí
- Lưới 1 «Danh sách phiếu báo học phí» (bảng MINVOICE); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Mã lớp [MaLop]; Mã khối [MaKhoi]; Mã đơn vị [MaDV]; Mã Ng/CNg [MaNgChng]; Niên khóa [NienKhoa]; Số chứng từ [SoCTu]; Ngày thu/chi [NgayTChi]{ngày}; Số tiền thu [TienPT]{số}; SoInvoice [SoInvoice]; Hủy [IsHuyInvoice]; Tổng hp phải đóng [PhaiThu]{số}
### ViewBacHeNamVao – View chon bac he nao vao
- Lưới 1 «Danh sách bậc hệ» (bảng KDMBH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Năm BĐ [NamBDVB]{số}; Học kỳ [HK]; Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]; Niên khóa [NienKhoa]; Số sinh viên [SoSV]
### VIEWBACHERE – Giao diện bậc hệ cho báo biểu
- Lưới 1 «Danh sách bậc hệ» (bảng KDMBH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]; Số sinh viên [SoSV]
### VIEWBHRE209X – Giao diện chọn bậc hệ cho báo biểu
- Lưới 1 «Danh sách bậc hệ» (bảng KDMBH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]
### VIEWBHYT – Giao diện nhập bảo hiểm y tế
- Lưới 1 «Danh sách bảo hiểm y tế» (bảng NBHYT); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Số sổ BHYT [SoSBHYT]; Ngày đăng ký [NgayBDBHYT]{ngày}; Ngày hết hạn [NgayKTBHYT]{ngày}; Bệnh viện đăng ký [BVBHYT]
  - Cột ẩn: Mã viên chức [IDNV]
  - Ô trên form sửa: #TenDayDuNV, #SoSBHYT, #NgayBDBHYT, #NgayKTBHYT, #BVBHYT, #IDNV
### VIEWBOMON – Giao diện bộ môn
- Lưới 1 «Danh sách bộ môn» (bảng NDMDV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đơn vị [MaDV]; Tên đơn vị [TenDV]
### ViewCaLamViecChiTiet – Thời gian làm việc trong tuần
- Lưới 1 «Thời gian làm việc trong tuần» (bảng NCaLamViecCT); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Thứ [GhiChu2](chỉ đọc); Giờ bắt đầu ca [GioBDCa]; Giờ kết thúc ca [GioKTCa]; Giờ bắt đầu nghỉ trưa [GioBDNghiTrua]; Giờ kết thúc nghỉ trưa [GioKTNghiTrua]; Giờ bắt đầu vào hợp lệ [GioBDVaoHL]; Giờ kết thúc vào hợp lệ [GioKTVaoHL]; Giờ bắt đầu ra hợp lệ [GioBDRaHL]; Giờ kết thúc ra hợp lệ [GioKTRaHL]; Số phút được phép vào trể [SoPhutMaxVaoTre]{số}; Số phút max được phép về sớm [SoPhutMaxVeSom]{số}
### ViewCamXemMenu – Cấm xem menu khi chưa nhập đủ thông tin sinh viên
- Lưới 1 «Danh sách đối tượng» (bảng HKhoaSoPhanHe); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Đối tượng kiểm tra nhập thông tin [LoaiDTMenu]{chọn}(chỉ đọc)
### VIEWCAPNHATDOTTHI – Cập nhật đợt thi
- Lưới 1 «Danh sách đợt thi» (bảng LDotThi); tắt: Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đợt thi [MaDotThi]; Tên đợt thi [TenDotThi]; Tên viết tắt [VtDotThi]; Điểm B2 [B2]; Ngày bắt đầu [NgayThiBD]{ngày}; Ngày kết thúc [NgayThiKT]{ngày}; Công bố dữ liệu [IsCongBo]
  - Cột ẩn: Điểm B1 [B1]; Ghi chú [GcDotThi]; Ghi chú [GhiChu]
  - Ô trên form sửa: #MaDotThi, #TenDotThi, #VtDotThi, #NgayThiBD, #NgayThiKT, #IsCongBo, #GcDotThi, #GhiChu
  - Nút btnDelete: "Xóa" (F3)
  - Nút btnAdd: "Thêm" (F5)
  - Nút btnPrint: "In" (F9)
  - Nút btnSave: "Lưu" (F4)
  - Nút btnCapNhat: "Cập nhật thời gian thi" (F6)
### VIEWCAPNHATLICHTHI – Cập nhật lịch thi
- Lưới 1 «Danh sách lịch thi» (bảng LToThi); tắt: Thêm, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH](chỉ đọc); Tổ thi [ToThi](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Tổ thi con [ToThiCon](chỉ đọc); Nhóm thi [NhomThi](chỉ đọc); Số SV tổ thi [SoSVToThi](chỉ đọc); Mã PH [MaPhHK]; Tổng số thí sinh [SoThiSinh](chỉ đọc); Tên phòng [TenPHHK]; Dãy phòng [DayPHHK]; Ngày thi [NgayThi](chỉ đọc); Tiết bắt đầu [TietThiBD](chỉ đọc); Số tiết thi [SoTietThi](chỉ đọc)
  - Cột ẩn: ID phòng hk [IDPHHK](chỉ đọc)
  - Ô trên form sửa: #MaMH, #ToThi, #TenMH, #ToThiCon, #NhomThi, #SoSVToThi, #SoThiSinh, #DayPHHK, #NgayThi, #TietThiBD, #SoTietThi, #IDPHHK
  - Nút btnSave: "Lưu" (F2)
  - Nút btnGhepPhong: "Ghép phòng thi" (F4)
### ViewCapNhatNgoaiTru – View cập nhật ngoại trú SV
- Lưới 1 (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Tên hộ [TenHo]; Tên chủ hộ [TenChuHo]; Loại cư trú [LoaiCuTru]; Ngày ngoại trú [NgayNgTru]; Địa chỉ [DC_DCTT]; Tỉnh/thành [DC_IDDBTT]; Điện thoại 1 [DC_DT1TT]; Email 1 [DC_Eml1TT]; Phòng ký túc xá [PhongKTX]
### ViewCapNhatSoCT – Cập nhật số chứng từ
- Lưới 1 (bảng MPTHU); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Số chứng từ [SoCTu]; Quyển số [QUYENSO]; Mã nhóm [MaNhCT]
### ViewCapNhatTCTotNghiep – Cập nhật số tín chỉ tốt nghiệp
- Lưới 1 «Danh mục lớp» (bảng SDMLOP); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã lớp [MaLop](chỉ đọc); Tên lớp [TenLop](chỉ đọc); NHHK vào [NHHKVao](chỉ đọc); Mã đơn vị QL [MaDVQL](chỉ đọc); Số Quyết định KHĐT [SoQDKHDT]; Số QĐ CTĐT [SoQDCTDT]; Tổng số tín chỉ CTĐT CQ [SoTinChiCTDT]{số}; Tờ trình [ToTrinh]; Đề nghị [DeNghi]; Ghi chú [GCSOQD]
### ViewCauHoiCoDA – View xem câu hỏi có đáp án theo lớp
- Lưới 1 (bảng YKQDGGV); tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Tên nhân viên [TenNV]; Mã môn học [MaMH]; Giá trị trả lời tiêu chí [GiaTriTC]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]
### ViewCauHoiKGDA – View xem câu hỏi không đáp án theo lớp
- Lưới 1 «Danh sách tiêu chíi không đáp án» (bảng YKQDGGV); tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Tên lớp [TenLop]; Tên nhân viên [TenNV]; Tên tiêu chí đánh giá [TenTCDG]; Mã môn học [MaMH]; Giá trị trả lời tiêu chí [GiaTriTC]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Điểm số [DiemDapAn]; Tên đáp án đánh giá chi tiết [TenDapAnDGCT]; Mã lớp [MaLop]
### ViewCauHoiKGDACopy – View xem câu hỏi không đáp án theo lớp
- Lưới 1 (bảng YKQDGGV); tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Tên lớp [TenLop]; Tên nhân viên [TenNV]; Tên tiêu chí đánh giá [TenTCDG]; Mã môn học [MaMH]; Giá trị trả lời tiêu chí [GiaTriTC]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Mã lớp [MaLop]
### ViewCauHoiKGDATruong – View xem câu hỏi không đáp án theo lớp
- Lưới 1 «Danh sách tiêu chí» (bảng YKQDGGV); tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Giá trị trả lời tiêu chí [GiaTriTC]; Tên lớp [TenLop]; Mã SV [MaSV]; Tên tiêu chí đánh giá [TenTCDG]; Họ lót [HoLotSV]; Tên [TenSV]; Mã lớp [MaLop]
### VIEWCAYPHANCAPDOTTHI – Cây phân cấp đợt thi
- Lưới 1; tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Đối tượng [DoiTuongTree](chỉ đọc); Có thi [PHAMVI]
  - Nút btnSave: "Lưu" (F4)
### ViewCBHDLV – Cán bộ hướng dẫn
- Lưới 1 «Cán bộ hướng dẫn» (bảng DCBHDLV); tắt: Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: TT [TTCBHDLV](chỉ đọc); Mã NV [MaNV](chỉ đọc); Họ lót [HoLotNV](chỉ đọc); Tên NV [TenNV](chỉ đọc); Tên đầy đủ [TenDayDuNV](chỉ đọc); Mã khoa [MaDV](chỉ đọc); Tên khoa [TenDV](chỉ đọc)
### VIEWCCXEMDSSV – Chọn cc xem danh sách sinh viên
- Lưới 1 (bảng DDMCC); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Chứng chỉ [IDCC]; Tên chứng chỉ [TenCC]; Loại chứng chỉ [LoaiCC]; Ghi chú [GcCC]
  - Ô trên form sửa: #IDCC, #TenCC, #LoaiCC, #GcCC
### VIEWCHINHDINHMATENBB – Giao diện chỉnh định mã tên báo biểu
- Lưới 1 «Danh sách mã báo biểu»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã báo biểu AQ [MaBaoBieuAQ](chỉ đọc); Tên báo biểu AQ [TenBaoBieuAQ](chỉ đọc); Mã báo biểu user [MaBaoBieuUser]; Tên báo biểu user [TenBaoBieuUser]
  - Nút btnSave: "Lưu" (F9)
  - Nút barBtnHuy: "Hủy thay đổi" (F10)
### VIEWCHINHDINHMATENVIEW – Giao diện chỉnh định mã tên giao diện dạng danh sách
- Lưới 1 «Danh sách mã giao diện»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã giao diện AQ [MaViewAQ](chỉ đọc); Phân loại view [PhanLoaiView]; Tên giao diện AQ [TenViewAQ](chỉ đọc); Mã giao diện user [MaViewUser]; Tên giao diện user [TenViewUser]; Giữ giá trị cũ [IsCarryOn]; Thêm mới liên tục [IsNewLoop]
  - Nút btnSave: "Lưu" (F9)
  - Nút barBtnHuy: "Hủy thay đổi" (F10)
### VIEWCHOMUV – Giao diện chọn ứng viên
- Lưới 1 «Danh sách ứng viên» (bảng NDMUV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã ứng viên [MaUV]; Họ lót ứng viên [HoLotUV]; Tên ứng viên [TenUV]; Phái [PhaiUV]{chọn}; Ngày sinh [NgSinhNVC]; Nơi sinh [NoiSinhUV]
### VIEWCHON1NIENKHOA – Danh sách niên khóa
- Lưới 1 «Danh sách niên khóa»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên khóa [NienKhoa]; NHHK vào [NHHKVao]; NHHK ra [NHHKRa]; Mã lớp [MaLop]
### VIEWCHONADDIN – Giao diện dùng để chọn addin
- Lưới 1 (bảng AQDMAddin); tắt: Thêm, Xóa, Import, In, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã addin [MaAddin](chỉ đọc); Tên addin [TenAddin](chỉ đọc); Mã DVPC hiệu lực [DSMaDVPC]; Phí addin [KinhPhi](chỉ đọc); Mô tả adddin [GcAddin](chỉ đọc); Ghi chú cấp addin [GCAddinTruong]; Ngày thêm [NgayThemC]
  - Cột ẩn: Ấn bản core [CoreVer]; Mã addin [IDAddin]; ID addin cha [IDAddinParent]; Ân bản lite [LiteVer]; Mã addin tiên quyết [MaAddinRQ]; Ân bản pro [ProVer]; Ân bản standard [StdVer]; Tên tiếng anh [TenAddinEg]; Thứ tự [TtAddin]
### VIEWCHONADDINANBAN – Giao diện chọn add theo ấn bản
- Lưới 1 (bảng AQDMAddin); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã addin [MaAddin](chỉ đọc); Tên addin [TenAddin](chỉ đọc); ID addin cha [IDAddinParent]; Ấn bản core [CoreVer]; Ân bản lite [LiteVer]; Ân bản standard [StdVer]; Ân bản pro [ProVer]
### VIEWCHONBACHE – Chọn bậc hệ
- Lưới 1 «Danh mục bậc - hệ» (bảng KDMBH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]; Số học kỳ [SoHK]; Mã bậc [MaBac]; Mã hệ đào tạo [MaHe]
### VIEWCHONBGQD – Chọn bảng qui đổi
- Lưới 1 «Chọn bảng qui đổi»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã qui đổi phụ [MaBgQDC]; Tên qui đổi phụ [TenBgQDC]; Thứ tự [TTBgQDC]; Hệ điểm qui đổi [HeDiemQD]{chọn}
  - Cột ẩn: Bảng qui đổi [IDBgQDC]; Qui đổi cha [IDBgQDCP]
### VIEWCHONBGQD2 – Chọn bảng qui đổi
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bảng qui đổi [MaBgQD2]; Tên bảng qui đổi [TenBgQD2]; Tên viết tắt [VtBgQD2]; Ghi chú [GCBgQD2]
### VIEWCHONBHN – View chọn bậc hệ ngành
- Lưới 1 «Danh sách bậc hệ ngành» (bảng KDMBHNgChNg); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã BH Ngành [MaBHN]; Tên BH Ngành [TenBHN]; Mã BH Ng/ChNg [MaBHNgChNg]; Tên BH Ng/ChNg [TenBHNgChNg]
### ViewChonBHNTheoPB – View chọn bậc hệ ngành theo phiên bản
- Lưới 1 «Danh sách bậc hệ ngành» (bảng KDMBHNgChNg); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã BH Ngành [MaBHN]; Tên BH Ngành [TenBHN]; Mã BH Ng/ChNg [MaBHNgChNg]; Mã PB [MaPB]; Tên BH Ng/ChNg [TenBHNgChNg]; Tên phiên bản [TenPB]
### VIEWCHONCHNGANH – View chọn ngành/Chuyên ngành
- Lưới 1 «Danh sách ngành/ chuyên ngành»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã Ng/CNg [MaNgChng]; Tên ng/chng [TenNgChng]
### VIEWCHONCHUKY – Danh mục chữ ký
- Lưới 1 «Danh sách chữ ký» (bảng HDmChuky); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã chữ ký [MaChuKy]; Tên chữ ký [TenChuKy]; Chức vụ 1 [Chucvu1]; Người ký [NguoiKy]
  - Cột ẩn: Hình chữ ký số [ChuKySo]; Chức vụ 2 [Chucvu2]; Chức vụ 3 [Chucvu3]; Chữ ký mặc định [DfChuKy]; Ghi chú [GCChuKy]; Không quản lý [HuyChuKy]; Người ký [IDChuKy]; Thứ tự [TTChuKy]; Tên tiếng anh [TenChuKyEg]; Cấp độ user [UserLevel]; Tên viết tắt [VtChuKy]
  - Nút Chọn: "Chọn chữ ký" (F4)
### VIEWCHONCHUKYTHEOBOCHUKY – Chon chu ky theo bo chu ky
- Lưới 1 «Danh sách chữ ký»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã chữ ký [MaChuKy]; Tên chữ ký [TenChuKy]; Chức vụ 1 [Chucvu1]; Người ký [NguoiKy]
  - Cột ẩn: Hình chữ ký số [ChuKySo]; Chức vụ 2 [Chucvu2]; Chức vụ 3 [Chucvu3]; Chữ ký mặc định [DfChuKy]; Ghi chú [GCChuKy]; Không quản lý [HuyChuKy]; Người ký [IDChuKy]; Mã user [MaUser]; Ngày thêm [NgayThem]; Thứ tự [TTChuKy]; Tên tiếng anh [TenChuKyEg]; Cấp độ user [UserLevel]; Tên viết tắt [VtChuKy]
  - Nút btnSave: "Lưu" (F5)
### ViewChonCKCV – View chọn chữ ký chức vụ
- Lưới 1 «Danh sách người ký» (bảng HDmChuky); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã chữ ký [MaChuKy]; Tên chữ ký [TenChuKy]; Tên tiếng anh [TenChuKyEg]; Chức vụ 1 [Chucvu1]; Chức vụ 2 [Chucvu2]; Chức vụ 3 [Chucvu3]; Tên tiếng anh [Chucvu1Eg]; Tên tiếng anh [Chucvu2Eg]; Tên tiếng anh [Chucvu3Eg]
### ViewChonCoVanHT – View chọn cố vấn học tập
- Lưới 1 «Danh sách cố vấn học tập» (bảng NDMNV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Họ lót [HoLotNV]; Tên nhân viên [TenNV]; Phái [PhaiNV]{chọn}
### ViewChonCumThi – View Chon Cụm Thi
- Lưới 1 «Danh sách cụm thi» (bảng TDMCUMTHI); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã cụm thi [MACUMTHI]; Tên cụm thi [TENCUMTHI]; Viết tắt [VTCUMTHI]; Ghi chú [GCCUMTHI]
### VIEWCHONDIEM – Giao diện để chọn mã loại điểm
- Lưới 1 «Chọn điểm»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã loại điểm [MaLoaiDiem]; Tên loại điểm [TenLoaiDiem]
  - Cột ẩn: Cột điểm động [*DIEM]; Tuần [*TUAN]; Điểm bảo lưu [BL]; Điểm C1 [C1]; Số sv chưa nhập điểm [ChuaNhap]; Số sv đã nhập điểm [DaNhap]; Ràng buộc xóa SS [DeleteRuleSS]; Điểm chữ [DiemChu]; Điểm khác [DiemKhac]; Ghi chú [GhiChu]; Hoãn thi [HoanThi]; Khóa chính SS [IsKhoaSS]; Điểm K1 [K1]; Điểm K2 [K2]; Điểm K3 [K3]; Điểm K4 [K4]; Độ dài DB SS [LenDBSS]; Lý do thất bại [LyDoError]; Mã field so sánh [MaFieldSS]; Mã file so sánh [MaFileSS]; Điểm P1 [P1]; Điểm P2 [P2]; Điểm P3 [P3]; Điểm P4 [P4]; Điểm P5 [P5]; Điểm P6 [P6]; Điểm Q1 [Q1]; Điểm Q1 [Q2]; Điểm Q2 mới [Q3]; Điểm Q4 [Q4]; Điểm Q5 [Q5]; Điểm Q6 [Q6]; Số lần đăng ký [SoLDK]; Số lần đăng ký thất bại [SoLDKLoi]; Số lần đăng ký thành công [SoLDKTC]; Số môn học đăng ký [SoMHDK]; Số sinh viên [SoSV]; Kiểu field ss [SpecType0SS]; Điểm thi [T1]; Điểm T2 [T2]; Điểm T3 [T3]; Điểm tổng kết học phần [TK]; Điểm tổng kết kiểm tra [TKK]; Điểm tổng kết thi [TKT]; Tuần 1 [TUAN1]; Tuần 3 [TUAN3]; Bảng phụ SS [TableCSS]; Bảng chính SS [TablePSS]; Tổng cộng [TongCong]; Ràng buộc sửa SS [UpdateRuleSS]; Tên viết tắt [VTTuan]
### ViewChonDienChinhSach – View chọn dữ liệu diện chính sách
- Lưới 1 «Danh sách diện chính sách» (bảng SDMDCS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã diện chính sách [MaDCS]; Tên diện chính sách [TenDCS]; Tên viết tắt [VtDCS]; Ghi chú [GcDCS]
### VIEWCHONDMMH – Giao diện chọn môn học cho danh mục
- Lưới 1 «Danh sách môn học» (bảng KDMMH); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Số tiết môn học [SoTietMH]; Nhóm/tổ [NhomTo]; Niên học học kỳ [NHHK]
### VIEWCHONDMTCXH – Danh mục trợ cấp xã hội
- Lưới 1 «Danh sách trợ cấp xã hội»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Loại trợ cấp [LoaiTroCap]{chọn}; Mã trợ cấp xã hội [MaTCXH]; Tên trợ cấp xã hội [TenTCXH]; Tên viết tắt [VtTCXH]; Ghi chú [GcTCXH]
### VIEWCHONDNNHOMHOC – Giao diện chọn nhóm tự chọn
- Lưới 1 «Danh sách nhóm» (bảng KDMNhomTC); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã nhóm [MaNhomTC]; Tên nhóm tự chọn [TenNhomTC]; Số tín chỉ đạt [SoTCDat]; Phân loại tự chọn [PhanLoaiTC]{chọn}
### ViewChonDotTS – View chọn đợt tuyển sinh
- Lưới 1 «Danh sách đợt tuyển sinh» (bảng TDOTNVTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đợt [MADOTNVTS]; Ngày khóa đợt XT [NGAYLOCKNVTS]{ngày}; Khóa đợt xét tuyển [ISLOCKNVTS]; Số lượng [SoLuong]
### ViewChonDVPC – View chọn đơn vị phân cấp
- Lưới 1 «Danh sách đơn vị phân cấp» (bảng HDMDVPC); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đơn vị phân cấp [MaDVPC]; Tên đơn vị phân cấp [TenDVPC]
### VIEWCHONFULLLOP – Giao diện chọn lớp
- Lưới 1 «Danh sách lớp» (bảng SDMLOP); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Tên lớp [TenLop]; Số sinh viên [SoSV]; Tên viết tắt [VTLop]; Ghi chú [GcLop]
### ViewChonGVMHDG – Chọn giảng viên môn học đánh giá
- Lưới 1 «Danh sách giảng viên đánh giá» (bảng YKQDGGV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Họ lót [HoLotNV]; Tên nhân viên [TenNV]; Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm/tổ [NhomTo]; Tổ TH [ToTH]
### ViewChonGVNHMHDG – Chọn giảng viên nhóm môn học đánh giá
- Lưới 1 «Danh sách giảng viên đánh giá» (bảng YKQDGGV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Họ lót [HoLotNV]; Tên nhân viên [TenNV]; Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm/tổ [NhomTo]; Tổ TH [ToTH]
### VIEWCHONHK – View chon hoc ky thu
- Lưới 1 «Chọn học kỳ thứ cần đồng bộ dữ liệu» (bảng KCTDTCH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Xét học kỳ thứ [HKThu]
### VIEWCHONHONGNGOAINHHK – Giao diện chọn font
- Lưới 1 «Danh sách phòng» (bảng KDMPH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã phòng [MaPH]; Tên phòng [TenPH]; Sức chứa thi [SucChuaThi]; Sức chứa [SucChuaPH]; Dãy phòng [DayPH]
### VIEWCHONHS – View chọn hs tự tạo
- Lưới 1 «Chọn hồ sơ» (bảng SDMHS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã hồ sơ [MaHS]; Tên hồ sơ [TenHS]; Tên viết tắt [VtHS]
### ViewChonHUSERMEMBER – Danh sách thành viên
- Lưới 1 «Danh sách» (bảng HUserGroup); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Nhóm [IsAccGroup]; UserName [UserName]; Tên đầy đủ [HotenTK]
  - Cột ẩn: Ghi chú [GCTK]
### VIEWCHONKDMBH – Giao diện chọn bậc hệ
- Lưới 1 «Danh sách bậc hệ» (bảng KDMBH); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]
### ViewChonKhenThuong – View chọn khen thưởng bên sinh viên
- Lưới 1 «Chọn danh sách khen thưởng» (bảng SDMKK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã KTKL [MaKKSV]; Tên khen thưởng kỷ luật [TenKKSV]; Tên viết tắt [VtKKSV]
  - Cột ẩn: Mã cấp KTKL [IDCapKTKL]
### ViewChonKhoanThuDN – Danh sách khoản thu
- Lưới 1 «Danh sách khoản thu» (bảng MDmKhTuDN); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khoản thu [MaKhTuDN]; Tên khoản tự ĐN [TenKhTuDN]
### VIEWCHONKHOICTDT – Chon khoi chuong trinh dao tao
- Lưới 1 «Chọn khối cần xử lý» (bảng KDMKHOI); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; NHHK vào [NHHKVao]; NHHK ra [NHHKRa]
### VIEWCHONKHOICTDTCopy – Chon khoi khối copy ke hoach
- Lưới 1 «Chọn khối muốn copy đến» (bảng KDMKHOI); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; NHHK vào [NHHKVao]; NHHK ra [NHHKRa]
### VIEWCHONKHOIDK – View chọn khối đăng ký môn học
- Lưới 1 «Danh sách khối»; tắt: Thêm, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; Niên khóa [NienKhoa]; Mã khoa [MaKhoa]; Tên khoa [TenKhoa]; Mã Ng/CNg [MaNgChng]; Tên ng/chng [TenNgChng]; Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]
### VIEWCHONKHOIRE – Giao diện chọn khối cho báo biểu
- Lưới 1 «Danh sách khối» (bảng KDMKHOI); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Tên phiên bản [TenPB]; Mã khối [MaKhoi]; Tên khối [TenKhoi]; Mã bậc hệ [MaBH]; Mã Ng/CNg [MaNgChng]; NHHK vào [NHHKVao]; NHHK ra [NHHKRa]; Mã PB [MaPB]
  - Cột ẩn: Tên ng/chng [TenNgChng]
### ViewChonKhoiTS – View chọn khối tuyển sinh
- Lưới 1 «Danh sách khối tuyển sinh» (bảng TDMKHOITS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MAKHOITS]; Tên khối [TENKHOITS]; Viết tắt [VTKHOITS]; Ghi chú [GCKHOITS]; Mã khối XT [MAKHOIXT]; Tên khối XT [TENKHOIXT]
### ViewChonKyLuat – View chọn kỷ luật bên sinh viên
- Lưới 1 «Danh sách kỷ luật» (bảng SDMKK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã KTKL [MaKKSV]; Tên khen thưởng kỷ luật [TenKKSV]; Tên viết tắt [VtKKSV]
### VIEWCHONLoaiPAND – Chọn loại phương án
- Lưới 1 «Danh sách loại phương án»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Loại phương án nhập điểm [LoaiPAND]; Tên loại phương án nhập điểm [GhiChu1]
### VIEWCHONLOP – Giao diện chọn lớp
- Lưới 1 «Danh sách lớp» (bảng SDMLOP); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Tốt nghiệp [IsTOTNG]; Tên lớp [TenLop]; Tên tiếng anh 2 [TenLopEg2]; Niên khóa [NienKhoa]; Số sinh viên [SoSV]; Tên viết tắt [VTLop]; Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]; Ghi chú [GcLop]; Mã khoa [MaKhoa]; Mã đơn vị [MaDV]; Mã khối [MaKhoi]; Tên đơn vị [TenDV]; Tên khối [TenKhoi]; Mã Ng/CNg [MaNgChng]; Tên ng/chng [TenNgChng]; Đã khóa [IsLockSV]; SL đã khóa [SLDaLock]; SL chưa khóa [SLChuaLock]; Đã khóa điểm [IsLockDiemRL]; Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Sinh viên tự đánh giá [IsSVTuDanhGia]; Cố vấn học tập đánh giá [IsCVHTDanhGia]; Khoa đánh giá [IsKhoaDanhGia]
  - Cột ẩn: Ch.Ng [MaChNg]; Mã ngành [MaNganh]; NHHK ra [NHHKRa]; NHHK vào [NHHKVao]
### VIEWCHONLOPNGOAINHHK – Chon lớp ngoài NNHK
- Lưới 1 «Danh sách lớp»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Tên lớp [TenLop]; Tên viết tắt [VTLop]; Mã khối [MaKhoi]; NHHK vào [NHHKVao]; NHHK ra [NHHKRa]
  - Cột ẩn: Ghi chú [GcLop]
### ViewChonLV – View chọn lĩnh vực
- Lưới 1 «Danh sách lĩnh vực đào tạo» (bảng SDMLVDT); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lĩnh vực đt [MaLVDT]; Tên lĩnh vực đt [TenLVDT]; Viết tắt lĩnh vực đt [VtLVDT]
### VIEWCHONMHHT – Giao diện cho môn học hoc trước
- Lưới 1 «Danh sách môn học điều kiện» (bảng KDMMH); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Số tiết môn học [SoTietMH]
  - Nút btnDelete: "xoa" (F2)
  - Nút btnAdd: "them" (F1)
### VIEWCHONMHMHTQ – Giao diện chọn môn học tiên quyết
- Lưới 1 «Danh sách môn học điều kiện» (bảng KDMMH); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Số tiết môn học [SoTietMH](chỉ đọc)
  - Nút btnAdd: "them" (F1)
  - Nút btnDelete: "Xoa" (F2)
### VIEWCHONMHSH – Giao diện chọn môn học song hành
- Lưới 1 «Danh sách môn học điều kiện» (bảng KDMMH); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Số tiết môn học [SoTietMH]
  - Nút btnAdd: "them" (F1)
  - Nút btnDelete: "Xoa" (F2)
### VIEWCHONMONCHUNG – View chọn môn học
- Lưới 1 «Danh sách môn học»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]
### ViewChonMonTS – View Chọm Môn Tuyển Sinh
- Lưới 1 «Danh sách môn tuyển sinh» (bảng TDMMONTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn [MAMONTS]; Tên môn [TENMONTS]; Viết tắt [VTMONTS]; Ghi chú [GCMONTS]
### ViewChonNganh – Giao diện chọn ngành
- Lưới 1 «Danh sách ngành» (bảng KDMNgChNg); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã ngành [MaNganh]; Tên ngành [TenNganh]
### ViewChonNganhTS – View chọn Ngành tuyển Sinh
- Lưới 1 «Danh sách ngành tuyển sinh» (bảng TDMNGTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã ngành [MANGTS]; Tên ngành [TENNGTS]; Viết tắt [VTNGTS]; Ghi chú [GCNGTS]; Mã ngành XT [MANGXT]; Tên ngành XT [TENNGXT]
### ViewChonNhieuTC – View danh sach chon nhieu tieu chuan
- Lưới 1 «Danh sách tiêu chuẩn» (bảng DDmTChuan); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã tiêu chuẩn [MaTChuan]
### VIEWCHONNHOMTHI – Chọn nhóm thi xếp lịch thi
- Lưới 1 «Danh sách nhóm thi» (bảng LNhomThi); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Nhóm thi [NhomThi](chỉ đọc); Số sinh viên [SoSV](chỉ đọc); Nhóm thi [NhomThiDK]
### ViewChonNhomVangThi – Chọn môn học
- Lưới 1 «Chọn môn học»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm thi [NhomThi]; Tổ thi [ToThi]; Ngày thi [NgayThi]{ngày}; SV vắng thi [SoSV]{số}
### VIEWCHONNV – Giao diện chọn nhân viên
- Lưới 1 «Danh sách nhân viên» (bảng NDMNV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Ngày sinh [NgSinhNVC]; Phái [PhaiNV]{chọn}
### ViewchonNVDG – View chọn nv đánh giá
- Lưới 1 «Danh sách giảng viên đánh giá» (bảng YKQDGGV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Họ lót [HoLotNV]; Tên nhân viên [TenNV]
### VIEWCHONNVHD – View chọn nhân viên
- Lưới 1 «Danh sách nhân viên»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Tên đơn vị [TenDV]; Họ lót [HoLotNV]; Tên nhân viên [TenNV]; Tên đầy đủ [TenDayDuNV]; Ngày sinh [NgSinhNVCNV]; Phái [PhaiNV]{chọn}; Mã đơn vị [MaDV]
### VIEWCHONNVHK – Chọn nhân viên học kỳ
- Lưới 1 «Danh sách cán bộ nhân viên» (bảng NDMNV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV](chỉ đọc); Họ lót [HoLotNV](chỉ đọc); Tên nhân viên [TenNV](chỉ đọc); Phái [PhaiNV]{chọn}(chỉ đọc); Ngày sinh [NgSinhNVC](chỉ đọc); Nơi sinh [NoiSinhNV](chỉ đọc); Loại đối tượng CBGD [loaidtcbgd]{chọn}; Khoa/ đơn vị [TenDVEg]; Tên chức vụ [TenChucVu]; Đơn vị/bộ môn [TenDV]; Số tài khoản [SoTK]; Số tài khoản 2 [SoTK2]; Tên ngân hàng [TenNH]; Email [DC_Eml1LLNV]
  - Cột ẩn: Đơn vị [IDDV]
### VIEWCHONNVHKADD – Chọn nhân viên học kỳ
- Lưới 1 «Chọn giảng viên cho khóa học» (bảng NDMNV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã viên chức [MaNV](chỉ đọc); Tên đầy đủ [TenDayDuNV](chỉ đọc); Số điện thoại [DC_DT1LLNV](chỉ đọc); Phái [PhaiNV]{chọn}(chỉ đọc); Đơn vị [IDDV]; Ngày sinh [NgSinhNVC](chỉ đọc); Email [DC_Eml1LLNV](chỉ đọc); Trạng thái [HienDienNV]{chọn}(chỉ đọc)
### VIEWCHONNVHKNEW – Giao diện chọn nhân viên
- Lưới 1 «Danh sách viên chức học kỳ» (bảng NDMNV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; NgaySinhNV [NgaySinhNV]; Phái [PhaiNV]{chọn}; Trạng thái [HienDienNV]{chọn}; Viên chức ngoài trường [IsNVNgoai]
### ViewChonPhanHe – View chọn phân hệ
- Lưới 1 «Danh sách phân hệ» (bảng AQDMPhanHe); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã phân hệ [MaPhanHe]; Tên phân hệ [TenPhanHe]; Tên viết tắt [VtPhanHe]
### ViewChonPLGV – View chọn phân loại giảng viên
- Lưới 1 «Danh sách phân loại giảng viên»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã phân loại GV [MaPLGV]; Tên phân loại GV [TenPLGV]
### VIEWCHONPTXT – Giao diện chọn phương thức xét tuyển
- Lưới 1 «Danh sách phương thức» (bảng TPTXT); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã phương thức [MaPTXT]; Tên phương thức [TenPTXT]
### VIEWCHONSDMHS – Chọn danh mục hồ sơ
- Lưới 1 «Danh mục hồ sơ» (bảng SDMHS); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã hồ sơ [MaHS]; Tên hồ sơ [TenHS]
### VIEWCHONSV – Chọn sinh viên (Nhập mã)
- Lưới 1 (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Ngày sinh [NgaySinhC]; Hình sinh viên [AvatarSV]
  - Ô trên form sửa: #MaSV, #TenDayDu, #NgaySinhC, #AvatarSV
### ViewChonSVDuThiRutMonHoc – DS sinh viên dự thi đã rút môn học
- Lưới 1 «Danh sách sinh viên có trong danh sách dự thi đã rút môn học» (bảng LNhomThi); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Mã lớp [MaLop]; Tên lớp [TenLop]; Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm thi [NhomThi]
### ViewChonTDSTSMONCT – Chọn hội đồng cần in
- Lưới 1 «Chọn hội đồng cần in»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã ngành [MANGTS]; Tên ngành [TENNGTS]; Mã trung tâm [MATTTHI]; Mã phòng thi [MAPHTHI]; Mã hội đồng [MAHDGK]; Số sinh viên [SoSV]
### VIEWCHONTKHTHUTS – View chọn khoản thu
- Lưới 1 «Danh sách khoản thu» (bảng TKHTHUTS); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã khoản thu [MaKhThu]; Tên khoản thu [TenKhThu]; Số tiền [SoTien]; Ghi chú [GhiChu]
### VIEWCHONTOHOC – Chọn tổ học đã nhập điểm
- Lưới 1 «Chọn nhóm/ tổ môn học»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm/tổ [NhomTo]; Số TC [SoTinChi]
  - Cột ẩn: Hình thức thi [HTThi]; Cơ sở [IDCoso]; Môn học [IDMH]; ID nhóm kèm [IDNhomKem]; id tổ học [IDToHoc]; ID tổ học cha [IDToHocP]; Không được đăng ký [IsKgDK]; Khóa chính [IsKhoa]; Qui hoạch? [IsQuyHoach]; Không Xét TKB CB [KgXetTKBCB]; Không xét trùng [KhgXetTKB]; Loại thành phần [KyHieuTTP]; Niên học học kỳ [NHHK]; Nhóm học lại [NhomHL]; Sĩ số cho phép đk [SiSoCPDK]; Sĩ số đã đăng ký [SiSoDDK]; Sĩ số phòng [SiSoPH]; SL trung bình nhóm [SiSoTKB]; Số lần thi [SoLanThi]; Số phút thi [SoPhutThi]; Số tiết/tuần [SoTietTuan]; Tổ hợp [tphop]
- Lưới 2; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: KH điểm TP [KyHieuTP]; Tên loại điểm [TenLoaiDiem]
  - Cột ẩn: Cột điểm động [*DIEM]; Tuần [*TUAN]; Điểm bảo lưu [BL]; Điểm C1 [C1]; Số sv chưa nhập điểm [ChuaNhap]; Số sv đã nhập điểm [DaNhap]; Ràng buộc xóa SS [DeleteRuleSS]; Xét học vụ mặc định [DfXetHV]; Điểm chữ [DiemChu]; Điểm khác [DiemKhac]; Ghi chú [GcXetHV]; Ghi chú [GhiChu]; Hoãn thi [HoanThi]; Không quản lý [HuyXetHV]; ID bộ kết quả [IDBoKQXet]; ID Xét học vụ [IDXetHV]; Khóa chính SS [IsKhoaSS]; Điểm K1 [K1]; Điểm K2 [K2]; Điểm K3 [K3]; Điểm K4 [K4]; Độ dài DB SS [LenDBSS]; Loại xét học vụ [LoaiXetHV]; Loại xét học vụ [LoaiXetHVN]; Lý do thất bại [LyDoError]; Mã field so sánh [MaFieldSS]; Mã file so sánh [MaFileSS]; Mã loại điểm [MaLoaiDiem]; Mã user [MaUser]; Mã xét học vụ [MaXetHV]; Niên học học kỳ [NHHK]; Ngày thêm [NgayThem]; Điểm P1 [P1]; Điểm P2 [P2]; Điểm P3 [P3]; Điểm P4 [P4]; Điểm P5 [P5]; Điểm P6 [P6]; Phân loại xét hv [PLXetHV]; Điểm Q1 [Q1]; Điểm Q1 [Q2]; Điểm Q2 mới [Q3]; Điểm Q4 [Q4]; Điểm Q5 [Q5]; Điểm Q6 [Q6]; Số lần đăng ký [SoLDK]; Số lần đăng ký thất bại [SoLDKLoi]; Số lần đăng ký thành công [SoLDKTC]; Số môn học đăng ký [SoMHDK]; Số sinh viên [SoSV]; Kiểu field ss [SpecType0SS]; Điểm thi [T1]; Điểm T2 [T2]; Điểm T3 [T3]; Điểm tổng kết học phần [TK]; Điểm tổng kết kiểm tra [TKK]; Điểm tổng kết thi [TKT]; Thứ tự [TTXetHV]; Tuần 1 [TUAN1]; Tuần 3 [TUAN3]; Bảng phụ SS [TableCSS]; Bảng chính SS [TablePSS]; Tên xét học vụ [TenXetHV]; Tên tiếng anh [TenXetHVEg]; Tổng cộng [TongCong]; Ràng buộc sửa SS [UpdateRuleSS]; Tên viết tắt [VTTuan]; Tên viết tắt [VtXetHV]
### VIEWCHONTONGIAO – Danh sách tôn giáo
- Lưới 1 «Danh sách tôn giáo»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã tôn giáo [MaTG]; Tên tôn giáo [TenTG]
### VIEWCHONTRUONG – Giao diện dùng để chọn trường
- Lưới 1 «Danh sách trường» (bảng AQDMTruong); tắt: Thêm, Xóa, Import, Xuất, In, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã trường tổ chức thi [MaTruong]; Tên trường [TenTruong]
### ViewChonTTThi – View chọn trung tâm thi
- Lưới 1 «Danh sách trung tâm thi» (bảng TDMTTTHI); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã trung tâm [MATTTHI]; Tên trung tâm [TENTTTHI]; Viết tắt [VTTTTHI]
### VIEWCHONTUAN – Tuần kế hoạch học kỳ
- Lưới 1 «Danh sách tuần học kỳ» (bảng KTuanKHHK); tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Sửa bên phải
  - Cột: Tuần bắt đầu [TuanBD](chỉ đọc); Tuần bắt đầu học kỳ [TuanBDHK](chỉ đọc); Ngày bắt đầu học [NgayBDH]{ngày}(chỉ đọc); Ngày hoàn tất [NgayKTH]{ngày}(chỉ đọc)
### ViewChonYeuCauTD – View chọn yêu cầu tuyển dụng
- Lưới 1 «Chọn yêu cầu tuyển dụng ứng viên dự tuyển» (bảng NYeuCauTDCT); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã yêu cầu [MaYeuCau]; Đơn vị gửi yêu cầu [TenDV]; Ngày đơn vị gửi yêu cầu [NgayDVGuiTD]{ngày}; Mô tả yêu cầu [MoTaTD]
### VIEWCONVERTUNICODE – Chuyển đổi chuỗi Unicode tổ hợp qua dựng sẵn
- Lưới 1 «Danh sách dữ liệu chuyển đổi» (bảng AQFileField); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã file [MaFile]; Mã field [MaField]; Ghi chú [GhiChu]; Giá trị [VNPrecompo]
### VIEWCTDTCHREPORT – Giao diện chọn CTDT chuẩn cho báo biểu
- Lưới 1 «Danh sách bậc hệ ngành»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]; Mã Ng/CNg [MaNgChng]; Tên ng/chng [TenNgChng]; Mã khoa [MaKhoa]; Mã PB [MaPB]
  - Cột ẩn: Tên phiên bản [TenPB]
### VIEWCTDTCHREPORT_1 – Giao diện chọn CTDT chuẩn cho báo biểu
- Lưới 1 «Danh sách bậc ngành»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]; Mã Ng/CNg [MaNgChng]; Tên ng/chng [TenNgChng]; Mã khoa [MaKhoa]; Mã PB [MaPB]
  - Cột ẩn: Tên phiên bản [TenPB]
### VIEWCTDTCHREPORT_Edit – Giao diện chọn CTDT chuẩn cho báo biểu
- Lưới 1 «Danh sách bậc hệ ngành» (bảng KCTDTCH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Mã PB [MaPB]; Tên bậc hệ [TenBH]; Tên viết tắt [VtPB]; Mã Ng/CNg [MaNgChng]; Tên phiên bản [TenPB]; Tên ng/chng [TenNgChng]; Mã khoa [MaKhoa]; Tên khoa [TenKhoa]
  - Cột ẩn: Bậc hệ ngành [IDBHNGCHNG]; Phiên bản [IDPB]
### VIEWDANGKYHOANTHI – Đăng ký hoãn thi
- Lưới 1 «Danh sách sinh viên nhập đăng ký hoãn thi ở học kỳ hiện tại» (bảng LSVHT); tắt: Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc)
  - Cột ẩn: Ghi chú [GhiChu]; Sinh viên [IDSV]; Mã môn học [MaMH]; Tên lớp [TenLop](chỉ đọc)
  - Ô trên form sửa: #HoLotSV, #TenSV, #MaLop, #GhiChu, #IDSV, #TenLop
### VIEWDANGKYTHICAITHIEN – Đăng ký thi cải thiện
- Lưới 1 «Danh sách sinh viên đăng ký thi cải thiện trong học kỳ» (bảng LSVCaiThien); tắt: Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Mã lớp [MaLop](chỉ đọc)
  - Cột ẩn: Ghi chú [GhiChu]; Sinh viên [IDSV]; Tên lớp [TenLop](chỉ đọc)
  - Ô trên form sửa: #HoLotSV, #TenSV, #MaLop, #GhiChu, #IDSV, #TenLop
### VIEWDANHSACHDOTTHI – Danh sách đợt thi
- Lưới 1 «Danh sách đợt thi» (bảng LDotThi); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đợt thi [MaDotThi]; Tên đợt thi [TenDotThi]; Số sinh viên [SoSV]; Số môn thi [SoMonThi]
  - Cột ẩn: KH điểm TP [KyHieuTP]
### VIEWDANHSACHTHI – Danh sách thi xếp lịch thi
- Lưới 1 «Danh sách sinh viên» (bảng LKQDKDThi); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Mã lớp [MaLop]; Tên lớp [TenLop]; Họ và tên [TenDayDu]
### ViewData – Dữ liệu in
- Lưới 1 «Dữ liệu in»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
### VIEWDATADETAILDELETE – Giao diện kết quả chi tiết khi xoá dữ liệu
- Lưới 1 «Danh sách các mẫu tin liên quan»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mẫu tin [MaDm]; Sô mẫu tin [SoRecord]; Phân hệ [PhanHe]; Danh mục [TenFileChiTiet]
### ViewDDotBVLV – Danh sách đợt bảo vệ luận văn
- Lưới 1 «Danh sách đợt bảo vệ luận văn» (bảng DDotBVLV); tắt: In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Đợt BVLV [MaDotBVLV]; Từ ngày [BVLVTuNgay]{ngày}; Đến ngày [BVLVDenNgay]{ngày}; Ghi chú [GcDotBVLV]
  - Ô trên form sửa: #MaDotBVLV, #BVLVTuNgay, #BVLVDenNgay, #GcDotBVLV
### VIEWDELETEFILE – Giao diện dùng để xóa file đính kèm
- Lưới 1 «Danh sách file được xóa mà không cần quyền khi xóa file chính» (bảng HDeleteKem); tắt: Thêm, Xóa, Import, Xuất, In, Đổi mã, Gộp mã
  - Cột: Mã file con [MAFILEC](chỉ đọc); Mã file cha [MAFILEP](chỉ đọc); Tên file con [TenFileC](chỉ đọc); Tên file cha [TenFileP](chỉ đọc); Chọn [CheckChon]
### ViewDGTheoMH – Thống kê đánh giá theo môn học
- Lưới 1 «Thống kê đánh giá theo môn học»; tắt: Thêm, Sửa, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Họ lót [HoLotNV]; Tên nhân viên [TenNV]; Mã môn học [MaMH]; Tên môn học [TenMH]; TC1 [__TCDG01]; TC2 [__TCDG02]; TC3 [__TCDG03]; TC4 [__TCDG04]; TC5 [__TCDG05]; TC6 [__TCDG06]; TC7 [__TCDG07]; TC8 [__TCDG08]; TC9 [__TCDG09]; TC10 [__TCDG10]; TC11 [__TCDG11]; TC12 [__TCDG12]; TC13 [__TCDG13]; TC14 [__TCDG14]; TC15 [__TCDG15]; TC16 [__TCDG16]; TC17 [__TCDG17]; TC18 [__TCDG18]; TC19 [__TCDG19]; TC20 [__TCDG20]; TC21 [__TCDG21]; TC22 [__TCDG22]; TC23 [__TCDG23]; TC24 [__TCDG24]; TC25 [__TCDG25]; TC26 [__TCDG26]; TC27 [__TCDG27]; TC28 [__TCDG28]; TC29 [__TCDG29]; TC30 [__TCDG30]; DTB [DTB]; DTBC [DTBC]
### ViewDGTheoNHOMMH – Thống kê đánh giá theo nhóm môn học
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Họ lót [HoLotNV]; Tên nhân viên [TenNV]; Nhóm HP [NhomHP]; TC1 [__TCDG01]; TC2 [__TCDG02]; TC3 [__TCDG03]; TC4 [__TCDG04]; TC5 [__TCDG05]; TC6 [__TCDG06]; TC7 [__TCDG07]; DTB [DTB]; TC8 [__TCDG08]; DTBC [DTBC]; TC9 [__TCDG09]; TC10 [__TCDG10]; TC11 [__TCDG11]; TC12 [__TCDG12]; TC13 [__TCDG13]; TC14 [__TCDG14]; TC15 [__TCDG15]; TC16 [__TCDG16]; TC17 [__TCDG17]; TC18 [__TCDG18]; TC19 [__TCDG19]; TC20 [__TCDG20]; TC21 [__TCDG21]; TC22 [__TCDG22]; TC23 [__TCDG23]; TC24 [__TCDG24]; TC25 [__TCDG25]; TC26 [__TCDG26]; TC27 [__TCDG27]; TC28 [__TCDG28]; TC29 [__TCDG29]; TC30 [__TCDG30]
### ViewDiemBLDS – Nhập điểm bảo lưu dạng danh sách
- Lưới 1 «Danh sách sinh viên» (bảng DDiemBL); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV]{nút …}; Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Mã môn học [MaMH]{nút …}; Tên môn học [TenMH](chỉ đọc); Điểm TP [DiemHP]; Ngày hết hạn [NgayHetHan]{ngày}; Niên học học kỳ [NHHK]{số}; Ghi chú [GCDiemBL]
### VIEWDIEUCHINHHOCPHIMONHOC – Điều chỉnh học phí môn học
- Lưới 1 «Danh sách sinh viên phụ thu» (bảng MPThuMH); tắt: Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Tên lớp [TenLop](chỉ đọc)
  - Cột ẩn: Ghi chú [GhiChu]; Sinh viên [IDSV]
  - Ô trên form sửa: #HoLotSV, #TenSV, #MaLop, #TenLop, #GhiChu, #IDSV
  - Nút btnAdd: "Thêm" (F4)
  - Nút btnDelete: "Xóa" (F7)
  - Nút btnSave: "Lưu" (F6)
  - Nút btnPrint: "In" (F10)
  - Nút btnImport: "Import" (F11)
### VIEWDIEUCHINHLEPHITHIHK – Điều chỉnh lệ phí thi học kỳ
- Lưới 1 «Danh sách sinh viên - Thông tin điều chỉnh lệ phí thi»; tắt: Thêm, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Số tiền phụ thu [TienPhuThu]; % phụ thu [PhThamPT]; Lý do phụ thu [LyDoPhuThu]
  - Cột ẩn: Lệ phí/học phí [isLPThi]
  - Nút barBtnHuy: "Hủy" (F3)
  - Nút btnSave: "Lưu" (F8)
### VIEWDIEUCHINHLEPHITHIMONHOC – Điều chỉnh lệ phí thi môn học
- Lưới 1 «Danh sách sinh viên» (bảng MPThuMH); tắt: Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên lớp [TenLop]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Sinh viên [IDSV]; Ghi chú [GhiChu]
  - Ô trên form sửa: #MaLop, #HoLotSV, #TenLop, #TenSV, #NgaySinhC, #IDSV, #GhiChu
  - Nút btnImport: "Import" (F11)
  - Nút btnSave: "Lưu" (F6)
  - Nút btnDelete: "Xóa" (F7)
  - Nút btnAdd: "Thêm" (F4)
### ViewDKDeTaiLV – Danh sách sinh viên đăng ký đề cương
- Lưới 1 «Danh sách sinh viên đăng ký đề cương» (bảng DDKDeTaiLV); tắt: In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên SV [TenSV]; Mã lớp [MaLop]; Số quyết định [SoQDDeTai]; Tên đề tài [TenDeTaiLV]; Tên đề tài (2) [TenDeTaiLVEg]; Mã môn học [MaMH]; Tên môn học [TenMH]; Ngày dự kiến [NgayDuKienDeTai]{ngày}
  - Cột ẩn: Địa điểm tố chức [DiaDiemDeTaiLV]; Ghi chú đề tài [GCDeTaiLV]; Ghi chú 1 [GhiChu1]; Môn học [IDMH]; Sinh viên [IDSV]; Nội dung 2 [NoiDungDeTaiLV]; Tên người ký [TenNguoiKy]
  - Ô trên form sửa: #HoLotSV, #TenSV, #MaLop, #SoQDDeTai, #TenDeTaiLV, #TenDeTaiLVEg, #NgayDuKienDeTai, #DiaDiemDeTaiLV, #GCDeTaiLV, #GhiChu1, #IDMH, #IDSV, #NoiDungDeTaiLV, #TenNguoiKy
### VIEWDKHOANTHI – Đăng ký hoãn thi
- Lưới 1 «Danh sách sinh viên hoãn thi» (bảng LSVHT); tắt: Xuất, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Tên lớp [TenLop](chỉ đọc)
  - Cột ẩn: Ghi chú [GhiChu]; Sinh viên [IDSV]
  - Ô trên form sửa: #HoLotSV, #TenSV, #NgaySinhC, #MaLop, #TenLop, #GhiChu, #IDSV
### VIEWDMMHHT – Danh mục môn học chọn hoãn thi
- Lưới 1 «Danh sách môn học»; tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]
  - Cột ẩn: Điểm B1 [B1]; Điểm B2 [B2]; Điểm B3 [B3]; Điểm C1 [C1]; Điểm C2 [C2]; Điểm K1 [K1]; Điểm K2 [K2]; Điểm K3 [K3]; Điểm thi [T1]; Điểm T2 [T2]; Điểm T3 [T3]
### VIEWDMMONDTNH – Danh sách môn học đào tạo ngắn hạn
- Lưới 1 «Danh mục môn đào tạo ngắn hạn» (bảng FDMMonDTNH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMonDTNH]; Tên môn [TenMonDTNH]; Số tiết môn học [SoTietMH]; Học phí [HocPhi]
  - Cột ẩn: Môn học [IDMonDTNH]
### VIEWDMNGANH – Giao diện chọn ngành
- Lưới 1 «Danh sách ngành chuyên ngành» (bảng KDMNgChNg); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã Ng/CNg [MaNgChng]; Mã ngành bộ [MaNgChngBo]; Tên ng/chng [TenNgChng]; Tên viết tắt [VtNgChNg]; Ghi chú [GcNgChng]
### VIEWDNDOTTHI – Dinh nghia dot thi theo nhom thi
- Lưới 1 «Gán đợt thi cho nhóm thi» (bảng LNhomThi); tắt: Thêm, Xóa, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm/tổ [NhomTo](chỉ đọc); Sĩ số đã đăng ký [SiSoDDK](chỉ đọc); Nhóm thi [NhomThi](chỉ đọc); Tuần kết thúc [TuanktHoc](chỉ đọc); Ngày kết thúc [NgayKT]{ngày}; Ký hiệu ghép [GhepCaThi](chỉ đọc); Không xếp lý thuyết [KgXepLT](chỉ đọc); KH điểm TP [KyHieuTP](chỉ đọc); Sĩ số tổ thi [SiSoToThi](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Mã hình thức thi [MaHTThi](chỉ đọc); Đợt thi [IDDotThi]
  - Cột ẩn: Mã BM QL MH [MaBmQLMH](chỉ đọc); Mã đợt thi [MaDotThi]; Mã khoa quản lý bộ môn [MaKhoaBM](chỉ đọc); Ngày thi ưu tiên [NThiUTien]{ngày}(chỉ đọc); Thi khác TG [TKhacTG](chỉ đọc); Tên BM QL MH [TenBmQLMH](chỉ đọc); Tên khoa quản lý bộ môn [TenKhoaBM](chỉ đọc); TBD ưu tiên [TietBDUT](chỉ đọc)
### ViewDNhHDBVLV – Danh sách nhóm hội đồng bảo vệ luận văn
- Lưới 1 «Danh sách nhóm hội đồng bảo vệ luận văn» (bảng DNhHDBVLV); tắt: In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Nhóm HĐ BVLV [MaNhHDBVLV]; Ghi chú [GCNhHDBVLV]; Đợt BVLV [MaDotBVLV]
  - Cột ẩn: Ghi chú 1 [GhiChu1]; Đợt bảo vệ luận văn [IDDotBVLV]
  - Ô trên form sửa: #MaNhHDBVLV, #GCNhHDBVLV, #GhiChu1, #IDDotBVLV
### VIEWDNTHOIGIANTHI – Dinh nghia thoi gian thi cho dot thi
- Lưới 1 «Danh sách đợt thi» (bảng LDotThi); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đợt thi [MaDotThi]; Tên đợt thi [TenDotThi]; Ghi chú [GhiChu]; Ngày bắt đầu [NgayThiBD]{ngày}; Ngày kết thúc [NgayThiKT]{ngày}
  - Ô trên form sửa: #GhiChu, #NgayThiBD, #NgayThiKT
### ViewDNVHDBVLV – Cán bộ hướng dẫn
- Lưới 1 «Danh sách thành viên hội đồng trong đợt» (bảng DNVHDBVLV); tắt: Thêm, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Đợt bảo vệ luận văn [IDDotBVLV]; Mã viên chức [MaNV]{nút …}; Tên đầy đủ [TenDayDuNV](chỉ đọc); Số TT [STTTrongDot]; Ghi chú [GCNVHDBVLV]
### ViewDNVNhHDBVLV – Danh sách cán bộ
- Lưới 1 «Danh sách cán bộ»; tắt: Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Số TT [STTTrongNh]; Mã viên chức [MaNV](chỉ đọc); Tên đầy đủ [TenDayDuNV](chỉ đọc); Ghi chú [GCNVNhHDBVLV]
### ViewDoiCBHD – Danh sách cán bộ hướng dẫn
- Lưới 1 «Danh sách cán bộ» (bảng DDoiCBHDLV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã cán bộ cũ [GhiChu1](chỉ đọc); Tên cán bộ cũ [GhiChu2](chỉ đọc); Mã viên chức mới [MaNV]{nút …}; Tên cán bộ mới [TenDayDuNV]
  - Cột ẩn: Cán bộ cũ [IDCBCu]; Cán bộ mới [IDCBMoi]; ID đổi CBHD [IDDoiCBHDLV]; ID quyết định thay đổi luận văn [IDQDDoiLV]
### ViewDongBoHTDaNhap – Danh sách sinh viên trả điểm hoãn thi
- Lưới 1 «Danh sách sinh viên trả điểm hoãn thi»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Mã môn học [MaMH]; Tên môn học [TenMH]; Điểm thành phần [DiemTP]; Điểm nhập [DiemTPCu]; Ngày nhập [NgayEdit]{ngày}; UserEdit [UserEdit]; KH điểm TP [KyHieuTP]
### VIEWDONGDANHMUC – Dung de chọn mẫu tin của danh mục
- Lưới 1 «Danh sách đối tượng»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Sửa bên phải
  - Cột: Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]; Tên viết tắt [VtBH]; Mã BH tổ học [MaBHTH]; Tên BH tổ học [TenBHTH]; Mã khối [MaKhoi]; Tên khối [TenKhoi]; Tên viết tắt [VtKhoi]; Mã lớp [MaLop]; Tên lớp [TenLop]; Tên viết tắt [VTLop]; Ghi chú [GcLop]; Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Nhóm/tổ [NhomTo]; Mã lớp [MaLopTH]; Tên lớp [TenLopTH]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Phái [Phai]; Ngày sinh [NgaySinhC]; Số sinh viên [SoSV]; Mã lớp thi [MaLopToThi]; Nhóm thi [NhomThi]; Tổ thi [ToThi]; Ngày thi [NgayThi]; Mã phòng [MaPH]; Tên phòng [TenPH]; Mã cố vấn học tập [MaCVHT]; Họ lót CVHT [HoLotCVHT]; Tên cố vấn học tập [TenCVHT]; Tên cố vấn học tập [TenDayDuCVHT]; Mã đợt [MaDotTN]; Số quyết định [SoQDSV]; Ngày ký [NgayKy]; Người ký [NguoiKy]; Mã khoa [MaKhoa]; Tên khoa [TenKhoa]; Họ lót CBGD [HoLotCBGD]; Tên CB [TenCBGD]; Mã Ng/CNg [MaNgChng]; Tên ng/chng [TenNgChng]; Mã khoa quản lý bộ môn [MaKhoaBM]; Tên khoa quản lý bộ môn [TenKhoaBM]
  - Nút btnChon: "Chọn" (F10)
### VIEWDONGIMPORTMAU – Giao diện dòng import mẫu
- Lưới 1 «Danh sách mẫu tin import»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### viewDotNVTS – View nhap dot nguyen vong tuyen sinh
- Lưới 1 «Danh sách đợt xét nguyện vọng» (bảng TDOTNVTS); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đợt [MADOTNVTS]; Nguyện vọng [NGUYENVONG]{chọn}; Ngày dự kiến xét tuyển [NGAYDKXT]{ngày}; Ngày quyết định trúng tuyển [NgQDTT]{ngày}; Số quyết định trúng tuyển [SoQDTT]; Khóa đợt xét tuyển [ISLOCKNVTS]; Ngày khóa đợt XT [NGAYLOCKNVTS]{ngày}; User khóa đợt XT [USERLOCKNVTS]
  - Cột ẩn: Đến ngày ĐKXT [DenNgayDKXT]{ngày}; Ghi chú [GCDOTNVTS]; Thứ tự [TTDOTNVTS]{số}; Từ ngày ĐKXT [TuNgayDKXT]{ngày}
  - Ô trên form sửa: #MADOTNVTS, #NGUYENVONG, #NGAYDKXT, #NgQDTT, #SoQDTT, #GCDOTNVTS
### VIEWDS_NG_KH_MH_TS – View danh sách ngành khối và môn tuyển sinh
- Lưới 1; tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã ngành [MANGTS]; Tên ngành [TENNGTS]; Mã môn [MAMONTS]; Tên môn [TENMONTS]; Tên khối [TENKHOITS]; Hệ số môn thi [HESOTS]; ID nhóm môn thi chung [IDGPTTS]; Môn điều kiện [ISMONTSTQ]; Mã khối [MAKHOITS]; Ngưỡng điểm liệt môn thi [MGLIETTS]; Ngưỡng điểm đạt môn ĐK [NGDATTS]
  - Cột ẩn: Khối tuyển sinh [IDKHOITS]; Môn thi [IDMONTS]; ID ngành khối [IDNGKH]
  - Ô trên form sửa: #TENNGTS, #TENMONTS, #TENKHOITS, #HESOTS, #IDGPTTS, #ISMONTSTQ, #MGLIETTS, #NGDATTS, #IDKHOITS, #IDMONTS, #IDNGKH
### VIEWDSCHONNHOMTHI – DANH SÁCH NHÓM THI
- Lưới 1 «Danh sách nhóm thi» (bảng LNhomThi); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Nhóm thi [NhomThi]; Mã môn học [MaMH]; Tên môn học [TenMH]; Số tổ thi [SoToThi]; Số TC [SoTinChi]; Nhóm/tổ [NhomTo]; Lý thuyêt [LT]; Thực hành [TH]; Tốt nghiệp [TN]; Luận án [LA]; Đề án [DA]; Bài tập lớn [BTL]; Bài tập [BT]; Thực tập [TT]; Tuần kết thúc [TuanktHoc]; Tuần kết thúc dạy bù [TuanKT]
### ViewDSCumThi – View Danh Sách Cụm Thi
- Lưới 1 «Danh sách cụm thi» (bảng TDSCUMTHI); tắt: Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã cụm thi [MACUMTHI](chỉ đọc); Tên cụm thi [TENCUMTHI](chỉ đọc); Viết tắt [VTCUMTHI]; Ghi Chú [GCDSCUMTHI]
### ViewDSDonVi – Danh sách khoa/bộ môn quản lý môn học
- Lưới 1 «Danh sách khoa/ bộ môn» (bảng NDMDV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đơn vị [MaDV](chỉ đọc); Tên đơn vị [TenDV](chỉ đọc)
### VIEWDSDOTTHI – Danh sách đợt thi
- Lưới 1 «Danh sách đợt thi» (bảng LDotThi); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã đợt thi [MaDotThi]; Tên đợt thi [TenDotThi]; KH điểm TP [KyHieuTP]; Ngày bắt đầu [NgayThiBD]; Ngày kết thúc [NgayThiKT]
### VIEWDSDOTTHISVCHUAPHANTO – Danh sách đợt thi
- Lưới 1 «Danh sách đợt thi» (bảng LDotThi); tắt: Thêm, Sửa, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đợt thi [MaDotThi]; Tên đợt thi [TenDotThi]; KH điểm TP [KyHieuTP]; Số sinh viên [SoSV]; Số môn thi [SoMonThi]
  - Nút btnPrint: "In" (F10)
### ViewDSEnum – View enum dạng danh sách
- Lưới 1 «Danh sách enum» (bảng AQEnumCT); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã Enum [MaEnum]; Tên Enum [TenEnum]; Biến constant [ConstEnum]; TT EnumCT [TTEnumCT]; Viết tắt (AQ) [VTENumCT]; Ghi chú [GCENumCT]
### VIEWDSFILECONGVAN – Danh sách file
- Lưới 1; tắt: Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Sửa bên phải, Thoát
  - Cột: Thứ tự [TTFCVanCT]; Tên file [TenFileCT]
### ViewDSFileDeTai – Danh sách file đề tài
- Lưới 1 «DS file để tài» (bảng OFileDeTai); tắt: Thêm, Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Hình ảnh [ImageFileDeTai]; Thứ tự [TTFileDeTai]; Nhan đề file [NhanDeFile](chỉ đọc); Loại file đề tài [LoaiFileDeTai]{chọn}(chỉ đọc); Ghi chú [GCFileDeTai]; Tên file [TenFileChiTiet](chỉ đọc); Xem chi tiết [XemChiTiet](chỉ đọc)
  - Cột ẩn: File Extension [FileExtension]; Đề tài [IDDeTaiNCKH]; IDFileDeTai [IDFileDeTai]
### ViewDSFileSach – Danh sách file sách
- Lưới 1 «Danh sách file sách» (bảng OFileSach); tắt: Thêm, Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: File minh chứng [ImageFileSach]; Thứ tự [TTFileSach]; Nhan đề file [NhanDeFile](chỉ đọc); Nơi lưu bản gốc [NoiLuuBanGoc]; Loại file [LoaiFileSach]{chọn}(chỉ đọc); Ghi chú [GCFileSach](chỉ đọc); Ngày upload [NgayUpLoad](chỉ đọc); Tên file [TenFileChiTiet](chỉ đọc); Xem chi tiết [XemChiTiet](chỉ đọc)
  - Cột ẩn: File Extension [FileExtension](chỉ đọc); IDFileSach [IDFileSach]; ID sách lý lịch khoa học [IDSachLyLichKH]
### VIEWDSMONHOCDANGKY – Danh sách môn học đăng ký
- Lưới 1 «Danh sách môn học đăng ký» (bảng MKQDK); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm/tổ [NhomTo]; Tổ TH [ToTH]; Số TC [SoTinChi]; Sĩ số đã đăng ký [SiSoDDK]; Sĩ số cho phép đk [SiSoCPDK]; SL trung bình nhóm [SiSoTKB]; Sĩ số phòng [SiSoPH]
### VIEWDSMONHOCDKTHI – Danh sách môn học đăng ký thi
- Lưới 1 «Danh sách môn học đăng ký thi» (bảng LKQDKDThi); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm thi [NhomThi]; Tổ thi [ToThi]; Số TC [SoTinChi]
### ViewDSMonHocXemKQDG – Chọn môn học xem kết quả đánh giá
- Lưới 1 «Chọn môn học xem kết quả đánh giá»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số sinh viên [SoSV]
### ViewDSMonTS – View Danh Sách Môn Tuyển Sinh
- Lưới 1 «Danh Sách môn thi tuyển sinh» (bảng TDSMONTS); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn [MAMONTS]; Tên môn TS [TENMONDS]; Viết tắt [VTMONDS]
  - Cột ẩn: Ghi Chú [GCDSMONTS]
  - Ô trên form sửa: #MAMONTS, #TENMONDS, #VTMONDS, #GCDSMONTS
### ViewDSMPTHUXemHDDT – Danh sách hóa đơn
- Lưới 1 «Danh sách hóa đơn»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Mã lớp [MaLop]; Ngày sinh [NgaySinhC]; Số HDDT [SoHDDT]; Tiền thu [TienThuGoc]; Ngày thu/chi [NgayTChi]; Ngày lập HDDT [NgayLapHDDT]
### ViewDSNganhTS – View Danh Sách Ngành Tuyển Sinh
- Lưới 1 «Danh sách ngành tuyển sinh» (bảng TDSNGTS); tắt: Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã ngành [MANGTS](chỉ đọc); Tên ngành [TENNGTS](chỉ đọc); Thứ tự [TTDSNGTS]; Viết tắt ngành [VTDSNGTS]; Ghi chú [GCDSNGTS]; Điểm tổng [DiemTong]; Điểm ĐK1 [MonDK1]; Điểm ĐK2 [MonDK2]; Xếp loại [LoaiBangTN]{chọn}; Độ tuổi [DoTuoi]; Mã số NgTS [MASONGTS]
### VIEWDSNGKHTS – View Danh Sách Ngành Khối Tuyển Sinh
- Lưới 1 «Danh sách ngành/khối tuyển sinh» (bảng TNGKH); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã ngành [MANGTS]; Tên ngành [TENNGTS]; Mã khối [MAKHOITS]; Tên khối [TENKHOITS]
  - Cột ẩn: Ghi chú [GCNGKH]; Khối tuyển sinh [IDKHOITS]; Ngành tuyển sinh [IDNGTS]
  - Ô trên form sửa: #TENNGTS, #TENKHOITS, #GCNGKH, #IDKHOITS, #IDNGTS
### VIEWDSNHOMTHI – Danh sách nhóm thi
- Lưới 1 «Danh sách nhóm thi» (bảng LNhomThi); tắt: Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm thi [NhomThi](chỉ đọc); Tên hình thức thi [TenHTThi](chỉ đọc)
  - Cột ẩn: Số tổ thi [SoToThi](chỉ đọc)
  - Nút btnAdd: "Thêm" (F4)
  - Nút btnDelete: "Xóa" (F3)
### VIEWDSNHOMTHILOI – Danh sách nhóm thi lỗi
- Lưới 1 «Danh sách nhóm thi» (bảng LNhomThi); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm thi [NhomThi]; Sĩ số đã đăng ký [SiSoDDK]; Sĩ số sv tối đa [SSoTDa]; Sổ tổ thi tối đa/nhóm [SSoTDaNh]
### VIEWDSPVDOTTHIPHANCAP – Danh sách phạm vi đợt thi
- Lưới 1 «Danh sách đợt thi»; tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đợt thi [MaDotThi]; Tên đợt thi [TenDotThi]
### ViewDSRBKhac – Danh sách ràng buộc khác
- Lưới 1 «Danh sách ràng buộc khác» (bảng MRBKHAC); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã ràng buộc khác [MaRBKhac]; Tên ràng buộc khác [TenRBKhac]; Thứ tự ràng buộc khác [TTRBKhac]; Viết tắt ràng buộc khác [VtRBKhac]; Ghi chú ràng buộc khác [GcRBKhac]
  - Cột ẩn: ID ràng buộc khác [IDRBKhac]
### ViewDSSVBHYTCT – Danh sách hộ gia đình sinh viên
- Lưới 1 «Danh sách thông tin hộ gia đình» (bảng SThongTinGDSV); tắt: Thêm, Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Số CMND [SoCMNDGD]; Họ tên [HoTenGD]; Ngày sinh [NgaySinhGD]{ngày}; Phái [Phai]{chọn}; Số bảo hiểm xã hội [SoBHXHGD]; Mối quan hệ [MoiQuanHe]
### VIEWDSSVTINHHP – Danh sách sinh viên có thể tính học phí
- Lưới 1 «Danh sách sinh viên» (bảng SSVHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Mã lớp [MaLop]; Tên lớp [TenLop]
### VIEWDSSVTINHHPLOI – Danh sách sinh viên không thể tính học phí
- Lưới 1 «Danh sách sinh viên» (bảng SSVHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Lý do [LyDoLoi]
### ViewDSTacGiaVietPhu – View danh sách tác giả người viết phụ
- Lưới 1 «Danh sách tác giả người viết phụ»; tắt: Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Mã viên chức [MaNV](chỉ đọc); Tên đầy đủ [TenDayDuNV](chỉ đọc); Tới trang [ToiTrang]; Từ trang [TuTrang]; Chủ biên [IsNguoiVietChinh]; Phần trăm đóng góp chủ biên [PhanTramDongGop]{số}; Số từ công trình [SoTu]{số}; Số từ công trình năm 2 [SoTuNam2]; Số lượng chương [SoChuong]{số}; Số lượng chương năm 2 [SoChuongNam2]{số}
  - Cột ẩn: Mã viên chức [IDNV](chỉ đọc); ID sách lý lịch khoa học [IDSachLyLichKH](chỉ đọc); ID sách lý lịch khoa học viết phụ [IDSachLyLichKHVietPhu](chỉ đọc); Qui đổi tiết chuẩn [QDTietChuan]{số}
### VIEWDSTCHUAN – Danh sách tiêu chuẩn
- Lưới 1 «Danh sách tiêu chuẩn» (bảng DDmTChuan); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Sửa bên phải
  - Cột: Đơn vị phân cấp [IDDVPC]; Mã tiêu chuẩn [MaTChuan]; Tên tiêu chuẩn [TenTChuan]; Mã bậc hệ [MaBH]; Mã ngành [MaNganh]; Mã khoa [MaKhoa]; Mã khối [MaKhoi]; Đối tượng SV xét TN [DoiTuongXetTN]{chọn}; Số TC chung [SoTCChung]; ĐTBTL [DTBRT]; Số TCTL [SoTCTL]; Tên tiếng anh [TenTChuanEg]; Mã đơn vị phân cấp [MaDVPC]; Tên đơn vị phân cấp [TenDVPC]
### VIEWDSTCHUAN_NOT – Danh sách tiêu chuẩn not check
- Lưới 1 «Danh sách tiêu chuẩn» (bảng DDmTChuan); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Gộp mã, Sửa trên lưới, Sửa bên phải
  - Cột: Đơn vị phân cấp [IDDVPC]; Mã tiêu chuẩn [MaTChuan]; Tên tiêu chuẩn [TenTChuan]; Mã bậc hệ [MaBH]; Mã ngành [MaNganh]; Ch.Ng [MaChNg]; Ch. Ngành [IDChNg]; Mã khoa [MaKhoa]; Mã khối [MaKhoi]; ĐTBTL [DTBRT]; Số TCTL [SoTCTL]; Tên tiếng anh [TenTChuanEg]; Ghi chú [GCTChuan]; Mã đơn vị phân cấp [MaDVPC]; Tên đơn vị phân cấp [TenDVPC]
  - Cột ẩn: Đối tượng SV xét TN [DoiTuongXetTN]{chọn}; Số TC chung [SoTCChung]
### VIEWDSTTTHI – View Danh Sách Trung Tâm Thi
- Lưới 1 «Danh sách trung tâm thi» (bảng TDSTTTHI); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã trung tâm [MATTTHI]; Tên trung tâm [TENTTTHI]; Mã cụm thi [MACUMTHI]; Tên cụm thi [TENCUMTHI]
  - Cột ẩn: Địa chỉ trung tâm thi [DIACHITTTHI]; Số điện thoại trung tâm [DIENTHOAITT]; Email phó trung tâm [EMAILPHOTT]; Email trưởng trung tâm [EMAILTRUONGTT]; Email trung tâm [EMAILTTT]; Ghi Chú [GCDSTTTHI]; Mã cụm thi [IDCUMTHI]; Tỉnh/thành [IDDBTTTHI]; Trung tâm thi [IDTTTHI]; ĐT phó trung tâm [TELPHOTT]; ĐT trưởng trung tâm [TELTRUONGTT]; Tên hiệu trưởng [TENHIEUTRUONG]; Tên phó trung tâm [TENPHOTT]; Tên trưởng trung tâm [TENTRUONGTT]; Tên địa bàn [TenDB]
  - Ô trên form sửa: #TENTTTHI, #TENCUMTHI, #DIACHITTTHI, #DIENTHOAITT, #EMAILPHOTT, #EMAILTRUONGTT, #EMAILTTT, #GCDSTTTHI, #IDCUMTHI, #IDDBTTTHI, #IDTTTHI, #TELPHOTT, #TELTRUONGTT, #TENHIEUTRUONG, #TENPHOTT, #TENTRUONGTT, #TenDB
### ViewDSVienChuc – Danh sách viên chức
- Lưới 1 «Danh sách bộ môn viên chức» (bảng NDMNV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Mã đơn vị [MaDV]; Tên đơn vị [TenDV]
### ViewExportSubRp – View xuat file sub report
- Lưới 1 «Danh sách sub report» (bảng HDMSubReport); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã report con [SubCode]; Tên Sub report [TenSubReport]; Tên viết tắt [VtSubReport]
### VIEWFILEHK – Danh sách file cần khởi tạo lên danh sách chọn file
- Lưới 1 «Check chọn file học kỳ muốn khởi tạo ( dữ liệu file sẽ được copy qua học kỳ khởi tạo từ học kỳ liền trước)»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Thứ tự [TTKTHK]; File dữ liệu [TenFile]; Số mẫu tin hk liền trước [SoRecordHKCu]; Số mẫu tin hk đang chọn [SoRecordHKMoi]; Phân hệ [TenPhanHe]
  - Cột ẩn: Mã file [Alias]; kiểu thừa kế [KieuThuaKe]; Mã file [MaFile]; Sql command [SqlCommand]
### ViewFilePhanHe – View xem file của phân hệ
- Lưới 1 «Danh sách file» (bảng AQDmFile); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã phân hệ [MaPhanHe]; Mã file [MaFile]; Tên file [TenFile]; Tên viết tắt [VtFile]
### ViewGanCaLamViecVC – Gán ca làm việc cho viên chức
- Lưới 1 «Danh sách nhân viên» (bảng NDMNV); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Đổi mã, Gộp mã
  - Cột: Mã viên chức [MaNV](chỉ đọc); Họ lót [HoLotNV](chỉ đọc); Tên nhân viên [TenNV](chỉ đọc); Phái [PhaiNV]{chọn}(chỉ đọc); NgaySinhNV [NgaySinhNV]{ngày}(chỉ đọc); Ca làm việc [IDCaLamViec]
  - Cột ẩn: Ghi chú [GCNV](chỉ đọc)
### ViewGanCoVanHTTheoLop – View gán cố vấn học tập theo lớp
- Lưới 1 «Danh sách lớp chưa gán cố vấn học tập» (bảng SSVHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã lớp [MaLop](chỉ đọc); Tên lớp [TenLop](chỉ đọc); Số sinh viên [SoSV](chỉ đọc); Mã cố vấn học tập [MaNV]{nút …}; Tên đầy đủ [TenDayDuNV](chỉ đọc)
  - Cột ẩn: Số điện thoại [DC_DT1LLNV](chỉ đọc); Email [DC_Eml1LLNV](chỉ đọc); ID CVHT [IDCVHT]
### ViewGanCoVanHTTheoLopCopy – View Hủy cố vấn học tập theo lớp
- Lưới 1 «Danh sách lớp có gán mã cố học tập» (bảng SSVHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã lớp [MaLop](chỉ đọc); Tên lớp [TenLop](chỉ đọc); Số sinh viên [SoSV](chỉ đọc)
### ViewGanCVHTToanTruong – View gán CVHT toàn trường
- Lưới 1 «Danh sách sinh viên» (bảng SSVHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Hiện diện SV [HienDienSV]{chọn}(chỉ đọc); Mã lớp [MaLop](chỉ đọc); ID CVHT [IDCVHT]; Tên đầy đủ [TenDayDuNV](chỉ đọc)
  - Cột ẩn: Số điện thoại [DC_DT1LLNV](chỉ đọc); Email [DC_Eml1LLNV](chỉ đọc)
### ViewGanCVHTToanTruongCopy – View gán CVHT lop sinh vien
- Lưới 1 «Danh sách sinh viên» (bảng SSVHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Mã lớp [MaLop](chỉ đọc); ID CVHT [IDCVHT]; Tên đầy đủ [TenDayDuNV](chỉ đọc)
### VIEWGD_BANGGHIDIEM – Loại bảng ghi điểm có sử dụng
- Lưới 1 «Loại bảng ghi điểm có sử dụng»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa bên phải
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Giá trị cấp cha [*ColNameP](chỉ đọc); Giá trị [GiaTriTreeLogic]
### VIEWGD_BOXEPHANG – Bộ xếp hạng
- Lưới 1 «Bộ xếp hạng cho qui chế»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Giá trị [GiaTriTreeString]
### VIEWGD_BOXEPHANG_EU – Bộ xếp hạng
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Giá trị [GiaTriTreeString]
### VIEWGD_COSUDUNGDIEMTP – Có sử dụng điểm thành phần
- Lưới 1 «Loại điểm thành phần có sử dụng»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Giá trị cấp cha [*ColNameP](chỉ đọc); Giá trị [GiaTriTreeLogic]
### VIEWGD_COSUDUNGHEDIEM – Hệ điểm sử dụng
- Lưới 1 «Hệ điểm sử dụng»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Giá trị cấp cha [*ColNameP](chỉ đọc); Giá trị [GiaTriTreeLogic]
### VIEWGD_DIEMDACBIET – Định nghĩa điểm đặt biệt
- Lưới 1 «Định nghĩa điểm đặt biệt»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Giá trị cấp cha [*ColNameP](chỉ đọc); Tên đầy đủ [*TENDAYDU]; Tên ngắn [*TENNGAN]; Ký hiệu nhập liệu [*TENVT]; Phân hệ [PhanHe]; Thứ tự [*THUTU]{số}
### VIEWGD_ISPQNHAPLOPKH – Phân quyền nhập điểm theo lớp kế hoạch
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Giá trị [*GIATRIQBD]{chọn}
  - Cột ẩn: Cột điểm động [*DIEM]; Điểm bài tập,thực hành (B) [*DIEM_B]; Điểm chuyên cần (C) [*DIEM_C]; Điểm kiểm tra (K) [*DIEM_K]; Điểm hệ số 1 (P) [*DIEM_P]; Điểm hệ số 2 (Q) [*DIEM_Q]; Điểm thi (T) [*DIEM_T]; Giá trị [*GIATRILTBGD]; Điểm hệ 10 [*HE_10]; Điểm hệ 100 [*HE_100]; Điểm hệ 1000 [*HE_1000]; Điểm hệ 4 [*HE_4]; HK1 [*HK1]; HK2 [*HK2]; HK3 [*HK3]; *Loại điểm [*LoaiDiem]; Môn học & loại điểm [*MHDiems]; Tên đầy đủ [*TENDAYDU]; Tên ngắn [*TENNGAN]; Tên viết tắt [*TENVT]; Thứ tự [*THUTU]; Thứ tự môn học đăng ký [*TTMHDK]; Tuần [*TUAN]; Giá trị mặc nhiên (DVPC) [AQDefaultValDVPC]; Giá trị mặc nhiên [AQDefaultValTM]; Giá trị mặc nhiên (Trường) [AQDefaultValTruong]; Cho rỗng 1 [AllowNullSS]; Điểm B1 [B1]; Điểm B2 [B2]; Bảng điểm học lại học vượt [BANGDIEM_HOCLAI]; Bảng điểm theo lớp SV [BANGDIEM_LOP]; Bảng ghi điểm theo mã BGD [BANGDIEM_MAGHIDIEM]; Bảng điểm toàn môn học [BANGDIEM_MONHOC]; Bảng điểm theo nhóm/tổ học [BANGDIEM_NHOMTOHOC]; Bảng điểm theo nhóm/tổ thi [BANGDIEM_NHOMTOTHI]; Điểm C1 [C1]; Điểm C2 [C2]; Cấm thi [CH]; Chỉnh định chung [CHINHDINHCHUNG]; Chưa hoàn tất [CHUA_HOAN_TAT]; Chữ ký [CHUKY]; Chung cho report [CHUNGCHOREPORT]; Control disable [CONTROLDISABLE]; Control [CONTROLNORMAL]; Control readonly [CONTROLREADONLY]; Cấm thi nợ học phí [CTHP]; Cuối nhóm nội dung [CUOINHOMNOIDUNG]; Cuối nhóm phân trang [CUOINHOMPHANTRANG]; Số sv chưa nhập điểm [ChuaNhap]; Đình chỉ [DC]; Điểm bài tập, thực hành (B) [DIEM_B]; Điểm bảo lưu [DIEM_BL]; Điểm chuyên cần (C) [DIEM_C]; Điểm tổng kết học phần [DIEM_HP]; Điểm kiểm tra (K) [DIEM_K]; Điểm tổng kết kiểm tra [DIEM_KT]; Điểm hệ số 1 (P) [DIEM_P]; Điểm hệ số 2 (Q) [DIEM_Q]; Điểm thi (T) [DIEM_T]; Điểm tổng kết thi [DIEM_TH]; Đăng ký thêm [DKThem]; Điểm số đạt [DS_DAT]; Điểm số không đạt [DS_KHONG_DAT]; ĐTB học kỳ 1 [DTBHK1]; ĐTB học kỳ 2 [DTBHK2]; ĐTB học kỳ 3 [DTBHK3]; Đã đăng ký [DaDK]; Số sv đã nhập điểm [DaNhap]; Đạt [Dat]; Ràng buộc xóa SS [DeleteRuleSS]; Điểm chữ [DiemChu]; Điểm khác [DiemKhac]; Độ rộng [DoRong]; Độ rộng edit [DoRongEdit]; Độ rộng field report [DoRongFieldReport]; Độ rộng field view [DoRongFieldView]; Đối tượng tree [DoiTuongTree]; Dòng chẵn [EVENROW]; Dòng đang chọn [FOCUSROW]; Field phụ 1 [FieldCSS]; Field chính 1 [FieldPSS]; Nhóm tiêu đề [GROUPHEADER]; Ghi chú [GhiChu]; Giá trị [GiaTri]; Giá trị [GiaTriTreeArray]; Giá trị [GiaTriTreeDecimal]; Giá trị [GiaTriTreeEnum]; Giá trị [GiaTriTreeInt]; Giá trị [GiaTriTreeLogic]; Giá trị [GiaTriTreeString]; Điểm hệ 10 [HE_10]; Điểm hệ 100 [HE_100]; Điểm hệ 1000 [HE_1000]; Điểm hệ 4 [HE_4]; Điểm hệ 4 (chữ) [HE_4_CHU]; Hoãn thi [HT]; Hoãn thi [HoanThi]; ID value set Report [IDValSetR]; ID set report 1 [IDValSetR1]; Index 1 [Index1]; Index 2 [Index2]; Index 3 [Index3]; Index 4 [Index4]; Khóa phụ 1 [IsKhoaPhuSS]; Khóa chính SS [IsKhoaSS]; Điểm K1 [K1]; Điểm K2 [K2]; Điểm K3 [K3]; Điểm K4 [K4]; Không đạt [KHONG_DAT]; Tên nhãn [LABEL]; Tên đầy đủ [LABEL_FULL]; Tên viết tắt [LABEL_SHORT]; Tên đầy đủ [LOAILABEL]; Logo [LOGO]; Độ dài DB SS [LenDBSS]; Lý do thất bại [LyDoError]; Miễn thi [MT]; Mã báo biểu AQ [MaBaoBieuAQ]; Mã báo biểu user [MaBaoBieuUser]; Mã field so sánh [MaFieldSS]; Mã file so sánh [MaFileSS]; Mã loại điểm [MaLoaiDiem]; Mã user [MaUser]; Mã view AQ [MaViewAQ]; Mã view user [MaViewUser]; Mặc định [MacDinh]; Ngày tháng năm mẫu in [NGAYTHANGNAMMAUIN]; Ngày và user giờ in [NGAYVAUSERGIOIN]; Nhóm nội dung [NHOMNOIDUNG]; Nhóm phân trang [NHOMPHANTRANG]; Ngày thêm [NgayThemC]; Nội dung [NoiDung]; Dòng lẻ [ODDROW]; Điểm P1 [P1]; Điểm P2 [P2]; Điểm P3 [P3]; Điểm P4 [P4]; Điểm P5 [P5]; Điểm P6 [P6]; Phân hệ [PhanHe]; Điểm Q1 [Q1]; Điểm Q1 [Q2]; Điểm Q2 mới [Q3]; Điểm Q4 [Q4]; Điểm Q5 [Q5]; Điểm Q6 [Q6]; Quốc hiệu [QUOCHIEU]; Quyền in bảng điểm [QUYEN_INBANGDIEM]{chọn}; Quyền nhập điểm [QUYEN_NHAPBANGDIEM]{chọn}; Rút môn học [RMH]; Dòng [ROW]; Dòng đã chọn [SELECTEDROW]; Số trang [SOTRANG]; Số thứ tự trong Report [STTReport]; Biểu in con [SUBREPORT]; Sum footer [SUMFOOTER]; Dòng tổng kết [SUMMARY]; Sinh viên ký tên [SVKyTen]; Setting [Setting]; Setting report [SettingReport]; Setting view [SettingView]; Số lần đăng ký [SoLDK]; Số lần đăng ký thất bại [SoLDKLoi]; Số lần đăng ký thành công [SoLDKTC]; Số môn học đăng ký [SoMHDK]; Số mẫu tin [SoMauTin]; Số mẫu tin hk cũ [SoRecordHKCu]; Số mẫu tin hk mới [SoRecordHKMoi]; Số sinh viên [SoSV]; Kiểu field ss [SpecType0SS]; Điểm thi [T1]; Điểm T2 [T2]; Điểm T3 [T3]; Tên mẫu in [TENMAUIN]; Tiêu đề [TIEUDE]; Tiêu đề cột [TITLECOLUMN]; Tiêu đề view [TITLEVIEW]; Điểm tổng kết học phần [TK]; Điểm tổng kết kiểm tra [TKK]; Điểm tổng kết thi [TKT]; Thứ tự tuần [TTTuan]; Tuần 1 [TUAN1]; Tuần 3 [TUAN3]; Bảng phụ SS [TableCSS]; Bảng chính SS [TablePSS]; Tên báo biểu AQ [TenBaoBieuAQ]; Tên báo biểu user [TenBaoBieuUser]; Tên field edit [TenFieldEdit]; Tên field view [TenFieldView]; Tên label edit [TenLabelEdit]; Tên label view [TenLabelView]; Tên loại điểm [TenLoaiDiem]; Tên tuần [TenTuan]; Tên view AQ [TenViewAQ]; Tên view user [TenViewUser]; Thông tin [ThongTin]; Thừa kế tree [ThuaKeTree]; Tiêu đề cột [TieuDeCot]; Tiêu đề cột edit [TieuDeCotEdit]; Tiêu đề cột report [TieuDeCotReport]; Tiêu đề cột view [TieuDeCotView]; Tổ TH [ToTH]; Tổng cộng [TongCong]; Ràng buộc sửa SS [UpdateRuleSS]; Tên viết tắt [VT]; Tên viết tắt [VTTuan]
### VIEWGD_ISPQNHAPMH – Phân quyền nhập điểm theo khoa/bộ môn ql môn học
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Giá trị [*GIATRIQBD]{chọn}
  - Cột ẩn: Cột điểm động [*DIEM]; Điểm bài tập,thực hành (B) [*DIEM_B]; Điểm chuyên cần (C) [*DIEM_C]; Điểm kiểm tra (K) [*DIEM_K]; Điểm hệ số 1 (P) [*DIEM_P]; Điểm hệ số 2 (Q) [*DIEM_Q]; Điểm thi (T) [*DIEM_T]; Giá trị [*GIATRILTBGD]; Điểm hệ 10 [*HE_10]; Điểm hệ 100 [*HE_100]; Điểm hệ 1000 [*HE_1000]; Điểm hệ 4 [*HE_4]; HK1 [*HK1]; HK2 [*HK2]; HK3 [*HK3]; *Loại điểm [*LoaiDiem]; Môn học & loại điểm [*MHDiems]; Tên đầy đủ [*TENDAYDU]; Tên ngắn [*TENNGAN]; Tên viết tắt [*TENVT]; Thứ tự [*THUTU]; Thứ tự môn học đăng ký [*TTMHDK]; Tuần [*TUAN]; Giá trị mặc nhiên (DVPC) [AQDefaultValDVPC]; Giá trị mặc nhiên [AQDefaultValTM]; Giá trị mặc nhiên (Trường) [AQDefaultValTruong]; Cho rỗng 1 [AllowNullSS]; Điểm B1 [B1]; Điểm B2 [B2]; Bảng điểm học lại học vượt [BANGDIEM_HOCLAI]; Bảng điểm theo lớp SV [BANGDIEM_LOP]; Bảng ghi điểm theo mã BGD [BANGDIEM_MAGHIDIEM]; Bảng điểm toàn môn học [BANGDIEM_MONHOC]; Bảng điểm theo nhóm/tổ học [BANGDIEM_NHOMTOHOC]; Bảng điểm theo nhóm/tổ thi [BANGDIEM_NHOMTOTHI]; Điểm C1 [C1]; Điểm C2 [C2]; Cấm thi [CH]; Chỉnh định chung [CHINHDINHCHUNG]; Chưa hoàn tất [CHUA_HOAN_TAT]; Chữ ký [CHUKY]; Chung cho report [CHUNGCHOREPORT]; Control disable [CONTROLDISABLE]; Control [CONTROLNORMAL]; Control readonly [CONTROLREADONLY]; Cấm thi nợ học phí [CTHP]; Cuối nhóm nội dung [CUOINHOMNOIDUNG]; Cuối nhóm phân trang [CUOINHOMPHANTRANG]; Số sv chưa nhập điểm [ChuaNhap]; Đình chỉ [DC]; Điểm bài tập, thực hành (B) [DIEM_B]; Điểm bảo lưu [DIEM_BL]; Điểm chuyên cần (C) [DIEM_C]; Điểm tổng kết học phần [DIEM_HP]; Điểm kiểm tra (K) [DIEM_K]; Điểm tổng kết kiểm tra [DIEM_KT]; Điểm hệ số 1 (P) [DIEM_P]; Điểm hệ số 2 (Q) [DIEM_Q]; Điểm thi (T) [DIEM_T]; Điểm tổng kết thi [DIEM_TH]; Đăng ký thêm [DKThem]; Điểm số đạt [DS_DAT]; Điểm số không đạt [DS_KHONG_DAT]; ĐTB học kỳ 1 [DTBHK1]; ĐTB học kỳ 2 [DTBHK2]; ĐTB học kỳ 3 [DTBHK3]; Đã đăng ký [DaDK]; Số sv đã nhập điểm [DaNhap]; Đạt [Dat]; Ràng buộc xóa SS [DeleteRuleSS]; Điểm chữ [DiemChu]; Điểm khác [DiemKhac]; Độ rộng [DoRong]; Độ rộng edit [DoRongEdit]; Độ rộng field report [DoRongFieldReport]; Độ rộng field view [DoRongFieldView]; Đối tượng tree [DoiTuongTree]; Dòng chẵn [EVENROW]; Dòng đang chọn [FOCUSROW]; Field phụ 1 [FieldCSS]; Field chính 1 [FieldPSS]; Nhóm tiêu đề [GROUPHEADER]; Ghi chú [GhiChu]; Giá trị [GiaTri]; Giá trị [GiaTriTreeArray]; Giá trị [GiaTriTreeDecimal]; Giá trị [GiaTriTreeEnum]; Giá trị [GiaTriTreeInt]; Giá trị [GiaTriTreeLogic]; Giá trị [GiaTriTreeString]; Điểm hệ 10 [HE_10]; Điểm hệ 100 [HE_100]; Điểm hệ 1000 [HE_1000]; Điểm hệ 4 [HE_4]; Điểm hệ 4 (chữ) [HE_4_CHU]; Hoãn thi [HT]; Hoãn thi [HoanThi]; ID value set Report [IDValSetR]; ID set report 1 [IDValSetR1]; Index 1 [Index1]; Index 2 [Index2]; Index 3 [Index3]; Index 4 [Index4]; Khóa phụ 1 [IsKhoaPhuSS]; Khóa chính SS [IsKhoaSS]; Điểm K1 [K1]; Điểm K2 [K2]; Điểm K3 [K3]; Điểm K4 [K4]; Không đạt [KHONG_DAT]; Tên nhãn [LABEL]; Tên đầy đủ [LABEL_FULL]; Tên viết tắt [LABEL_SHORT]; Tên đầy đủ [LOAILABEL]; Logo [LOGO]; Độ dài DB SS [LenDBSS]; Lý do thất bại [LyDoError]; Miễn thi [MT]; Mã báo biểu AQ [MaBaoBieuAQ]; Mã báo biểu user [MaBaoBieuUser]; Mã field so sánh [MaFieldSS]; Mã file so sánh [MaFileSS]; Mã loại điểm [MaLoaiDiem]; Mã user [MaUser]; Mã view AQ [MaViewAQ]; Mã view user [MaViewUser]; Mặc định [MacDinh]; Ngày tháng năm mẫu in [NGAYTHANGNAMMAUIN]; Ngày và user giờ in [NGAYVAUSERGIOIN]; Nhóm nội dung [NHOMNOIDUNG]; Nhóm phân trang [NHOMPHANTRANG]; Ngày thêm [NgayThemC]; Nội dung [NoiDung]; Dòng lẻ [ODDROW]; Điểm P1 [P1]; Điểm P2 [P2]; Điểm P3 [P3]; Điểm P4 [P4]; Điểm P5 [P5]; Điểm P6 [P6]; Phân hệ [PhanHe]; Điểm Q1 [Q1]; Điểm Q1 [Q2]; Điểm Q2 mới [Q3]; Điểm Q4 [Q4]; Điểm Q5 [Q5]; Điểm Q6 [Q6]; Quốc hiệu [QUOCHIEU]; Quyền in bảng điểm [QUYEN_INBANGDIEM]{chọn}; Quyền nhập điểm [QUYEN_NHAPBANGDIEM]{chọn}; Rút môn học [RMH]; Dòng [ROW]; Dòng đã chọn [SELECTEDROW]; Số trang [SOTRANG]; Số thứ tự trong Report [STTReport]; Biểu in con [SUBREPORT]; Sum footer [SUMFOOTER]; Dòng tổng kết [SUMMARY]; Sinh viên ký tên [SVKyTen]; Setting [Setting]; Setting report [SettingReport]; Setting view [SettingView]; Số lần đăng ký [SoLDK]; Số lần đăng ký thất bại [SoLDKLoi]; Số lần đăng ký thành công [SoLDKTC]; Số môn học đăng ký [SoMHDK]; Số mẫu tin [SoMauTin]; Số mẫu tin hk cũ [SoRecordHKCu]; Số mẫu tin hk mới [SoRecordHKMoi]; Số sinh viên [SoSV]; Kiểu field ss [SpecType0SS]; Điểm thi [T1]; Điểm T2 [T2]; Điểm T3 [T3]; Tên mẫu in [TENMAUIN]; Tiêu đề [TIEUDE]; Tiêu đề cột [TITLECOLUMN]; Tiêu đề view [TITLEVIEW]; Điểm tổng kết học phần [TK]; Điểm tổng kết kiểm tra [TKK]; Điểm tổng kết thi [TKT]; Thứ tự tuần [TTTuan]; Tuần 1 [TUAN1]; Tuần 3 [TUAN3]; Bảng phụ SS [TableCSS]; Bảng chính SS [TablePSS]; Tên báo biểu AQ [TenBaoBieuAQ]; Tên báo biểu user [TenBaoBieuUser]; Tên field edit [TenFieldEdit]; Tên field view [TenFieldView]; Tên label edit [TenLabelEdit]; Tên label view [TenLabelView]; Tên loại điểm [TenLoaiDiem]; Tên tuần [TenTuan]; Tên view AQ [TenViewAQ]; Tên view user [TenViewUser]; Thông tin [ThongTin]; Thừa kế tree [ThuaKeTree]; Tiêu đề cột [TieuDeCot]; Tiêu đề cột edit [TieuDeCotEdit]; Tiêu đề cột report [TieuDeCotReport]; Tiêu đề cột view [TieuDeCotView]; Tổ TH [ToTH]; Tổng cộng [TongCong]; Ràng buộc sửa SS [UpdateRuleSS]; Tên viết tắt [VT]; Tên viết tắt [VTTuan]
### VIEWGD_ISPQNHAPNHOM – Phân quyền nhập điểm theo theo nhóm/tổ học
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Giá trị [*GIATRIQBD]{chọn}
  - Cột ẩn: Cột điểm động [*DIEM]; Điểm bài tập,thực hành (B) [*DIEM_B]; Điểm chuyên cần (C) [*DIEM_C]; Điểm kiểm tra (K) [*DIEM_K]; Điểm hệ số 1 (P) [*DIEM_P]; Điểm hệ số 2 (Q) [*DIEM_Q]; Điểm thi (T) [*DIEM_T]; Giá trị [*GIATRILTBGD]; Điểm hệ 10 [*HE_10]; Điểm hệ 100 [*HE_100]; Điểm hệ 1000 [*HE_1000]; Điểm hệ 4 [*HE_4]; HK1 [*HK1]; HK2 [*HK2]; HK3 [*HK3]; *Loại điểm [*LoaiDiem]; Môn học & loại điểm [*MHDiems]; Tên đầy đủ [*TENDAYDU]; Tên ngắn [*TENNGAN]; Tên viết tắt [*TENVT]; Thứ tự [*THUTU]; Thứ tự môn học đăng ký [*TTMHDK]; Tuần [*TUAN]; Giá trị mặc nhiên (DVPC) [AQDefaultValDVPC]; Giá trị mặc nhiên [AQDefaultValTM]; Giá trị mặc nhiên (Trường) [AQDefaultValTruong]; Cho rỗng 1 [AllowNullSS]; Điểm B1 [B1]; Điểm B2 [B2]; Bảng điểm học lại học vượt [BANGDIEM_HOCLAI]; Bảng điểm theo lớp SV [BANGDIEM_LOP]; Bảng ghi điểm theo mã BGD [BANGDIEM_MAGHIDIEM]; Bảng điểm toàn môn học [BANGDIEM_MONHOC]; Bảng điểm theo nhóm/tổ học [BANGDIEM_NHOMTOHOC]; Bảng điểm theo nhóm/tổ thi [BANGDIEM_NHOMTOTHI]; Điểm C1 [C1]; Điểm C2 [C2]; Cấm thi [CH]; Chỉnh định chung [CHINHDINHCHUNG]; Chưa hoàn tất [CHUA_HOAN_TAT]; Chữ ký [CHUKY]; Chung cho report [CHUNGCHOREPORT]; Control disable [CONTROLDISABLE]; Control [CONTROLNORMAL]; Control readonly [CONTROLREADONLY]; Cấm thi nợ học phí [CTHP]; Cuối nhóm nội dung [CUOINHOMNOIDUNG]; Cuối nhóm phân trang [CUOINHOMPHANTRANG]; Số sv chưa nhập điểm [ChuaNhap]; Đình chỉ [DC]; Điểm bài tập, thực hành (B) [DIEM_B]; Điểm bảo lưu [DIEM_BL]; Điểm chuyên cần (C) [DIEM_C]; Điểm tổng kết học phần [DIEM_HP]; Điểm kiểm tra (K) [DIEM_K]; Điểm tổng kết kiểm tra [DIEM_KT]; Điểm hệ số 1 (P) [DIEM_P]; Điểm hệ số 2 (Q) [DIEM_Q]; Điểm thi (T) [DIEM_T]; Điểm tổng kết thi [DIEM_TH]; Đăng ký thêm [DKThem]; Điểm số đạt [DS_DAT]; Điểm số không đạt [DS_KHONG_DAT]; ĐTB học kỳ 1 [DTBHK1]; ĐTB học kỳ 2 [DTBHK2]; ĐTB học kỳ 3 [DTBHK3]; Đã đăng ký [DaDK]; Số sv đã nhập điểm [DaNhap]; Đạt [Dat]; Ràng buộc xóa SS [DeleteRuleSS]; Điểm chữ [DiemChu]; Điểm khác [DiemKhac]; Độ rộng [DoRong]; Độ rộng edit [DoRongEdit]; Độ rộng field report [DoRongFieldReport]; Độ rộng field view [DoRongFieldView]; Đối tượng tree [DoiTuongTree]; Dòng chẵn [EVENROW]; Dòng đang chọn [FOCUSROW]; Field phụ 1 [FieldCSS]; Field chính 1 [FieldPSS]; Nhóm tiêu đề [GROUPHEADER]; Ghi chú [GhiChu]; Giá trị [GiaTri]; Giá trị [GiaTriTreeArray]; Giá trị [GiaTriTreeDecimal]; Giá trị [GiaTriTreeEnum]; Giá trị [GiaTriTreeInt]; Giá trị [GiaTriTreeLogic]; Giá trị [GiaTriTreeString]; Điểm hệ 10 [HE_10]; Điểm hệ 100 [HE_100]; Điểm hệ 1000 [HE_1000]; Điểm hệ 4 [HE_4]; Điểm hệ 4 (chữ) [HE_4_CHU]; Hoãn thi [HT]; Hoãn thi [HoanThi]; ID value set Report [IDValSetR]; ID set report 1 [IDValSetR1]; Index 1 [Index1]; Index 2 [Index2]; Index 3 [Index3]; Index 4 [Index4]; Khóa phụ 1 [IsKhoaPhuSS]; Khóa chính SS [IsKhoaSS]; Điểm K1 [K1]; Điểm K2 [K2]; Điểm K3 [K3]; Điểm K4 [K4]; Không đạt [KHONG_DAT]; Tên nhãn [LABEL]; Tên đầy đủ [LABEL_FULL]; Tên viết tắt [LABEL_SHORT]; Tên đầy đủ [LOAILABEL]; Logo [LOGO]; Độ dài DB SS [LenDBSS]; Lý do thất bại [LyDoError]; Miễn thi [MT]; Mã báo biểu AQ [MaBaoBieuAQ]; Mã báo biểu user [MaBaoBieuUser]; Mã field so sánh [MaFieldSS]; Mã file so sánh [MaFileSS]; Mã loại điểm [MaLoaiDiem]; Mã user [MaUser]; Mã view AQ [MaViewAQ]; Mã view user [MaViewUser]; Mặc định [MacDinh]; Ngày tháng năm mẫu in [NGAYTHANGNAMMAUIN]; Ngày và user giờ in [NGAYVAUSERGIOIN]; Nhóm nội dung [NHOMNOIDUNG]; Nhóm phân trang [NHOMPHANTRANG]; Ngày thêm [NgayThemC]; Nội dung [NoiDung]; Dòng lẻ [ODDROW]; Điểm P1 [P1]; Điểm P2 [P2]; Điểm P3 [P3]; Điểm P4 [P4]; Điểm P5 [P5]; Điểm P6 [P6]; Phân hệ [PhanHe]; Điểm Q1 [Q1]; Điểm Q1 [Q2]; Điểm Q2 mới [Q3]; Điểm Q4 [Q4]; Điểm Q5 [Q5]; Điểm Q6 [Q6]; Quốc hiệu [QUOCHIEU]; Quyền in bảng điểm [QUYEN_INBANGDIEM]{chọn}; Quyền nhập điểm [QUYEN_NHAPBANGDIEM]{chọn}; Rút môn học [RMH]; Dòng [ROW]; Dòng đã chọn [SELECTEDROW]; Số trang [SOTRANG]; Số thứ tự trong Report [STTReport]; Biểu in con [SUBREPORT]; Sum footer [SUMFOOTER]; Dòng tổng kết [SUMMARY]; Sinh viên ký tên [SVKyTen]; Setting [Setting]; Setting report [SettingReport]; Setting view [SettingView]; Số lần đăng ký [SoLDK]; Số lần đăng ký thất bại [SoLDKLoi]; Số lần đăng ký thành công [SoLDKTC]; Số môn học đăng ký [SoMHDK]; Số mẫu tin [SoMauTin]; Số mẫu tin hk cũ [SoRecordHKCu]; Số mẫu tin hk mới [SoRecordHKMoi]; Số sinh viên [SoSV]; Kiểu field ss [SpecType0SS]; Điểm thi [T1]; Điểm T2 [T2]; Điểm T3 [T3]; Tên mẫu in [TENMAUIN]; Tiêu đề [TIEUDE]; Tiêu đề cột [TITLECOLUMN]; Tiêu đề view [TITLEVIEW]; Điểm tổng kết học phần [TK]; Điểm tổng kết kiểm tra [TKK]; Điểm tổng kết thi [TKT]; Thứ tự tuần [TTTuan]; Tuần 1 [TUAN1]; Tuần 3 [TUAN3]; Bảng phụ SS [TableCSS]; Bảng chính SS [TablePSS]; Tên báo biểu AQ [TenBaoBieuAQ]; Tên báo biểu user [TenBaoBieuUser]; Tên field edit [TenFieldEdit]; Tên field view [TenFieldView]; Tên label edit [TenLabelEdit]; Tên label view [TenLabelView]; Tên loại điểm [TenLoaiDiem]; Tên tuần [TenTuan]; Tên view AQ [TenViewAQ]; Tên view user [TenViewUser]; Thông tin [ThongTin]; Thừa kế tree [ThuaKeTree]; Tiêu đề cột [TieuDeCot]; Tiêu đề cột edit [TieuDeCotEdit]; Tiêu đề cột report [TieuDeCotReport]; Tiêu đề cột view [TieuDeCotView]; Tổ TH [ToTH]; Tổng cộng [TongCong]; Ràng buộc sửa SS [UpdateRuleSS]; Tên viết tắt [VT]; Tên viết tắt [VTTuan]
### VIEWGD_ISPQNHAPNHOMTHI – Phân quyền nhập điểm theo theo nhóm/tổ thi
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Giá trị [*GIATRIQBD]{chọn}
  - Cột ẩn: Cột điểm động [*DIEM]; Điểm bài tập,thực hành (B) [*DIEM_B]; Điểm chuyên cần (C) [*DIEM_C]; Điểm kiểm tra (K) [*DIEM_K]; Điểm hệ số 1 (P) [*DIEM_P]; Điểm hệ số 2 (Q) [*DIEM_Q]; Điểm thi (T) [*DIEM_T]; Giá trị [*GIATRILTBGD]; Điểm hệ 10 [*HE_10]; Điểm hệ 100 [*HE_100]; Điểm hệ 1000 [*HE_1000]; Điểm hệ 4 [*HE_4]; HK1 [*HK1]; HK2 [*HK2]; HK3 [*HK3]; *Loại điểm [*LoaiDiem]; Môn học & loại điểm [*MHDiems]; Tên đầy đủ [*TENDAYDU]; Tên ngắn [*TENNGAN]; Tên viết tắt [*TENVT]; Thứ tự [*THUTU]; Thứ tự môn học đăng ký [*TTMHDK]; Tuần [*TUAN]; Giá trị mặc nhiên (DVPC) [AQDefaultValDVPC]; Giá trị mặc nhiên [AQDefaultValTM]; Giá trị mặc nhiên (Trường) [AQDefaultValTruong]; Cho rỗng 1 [AllowNullSS]; Điểm B1 [B1]; Điểm B2 [B2]; Bảng điểm học lại học vượt [BANGDIEM_HOCLAI]; Bảng điểm theo lớp SV [BANGDIEM_LOP]; Bảng ghi điểm theo mã BGD [BANGDIEM_MAGHIDIEM]; Bảng điểm toàn môn học [BANGDIEM_MONHOC]; Bảng điểm theo nhóm/tổ học [BANGDIEM_NHOMTOHOC]; Bảng điểm theo nhóm/tổ thi [BANGDIEM_NHOMTOTHI]; Điểm C1 [C1]; Điểm C2 [C2]; Cấm thi [CH]; Chỉnh định chung [CHINHDINHCHUNG]; Chưa hoàn tất [CHUA_HOAN_TAT]; Chữ ký [CHUKY]; Chung cho report [CHUNGCHOREPORT]; Control disable [CONTROLDISABLE]; Control [CONTROLNORMAL]; Control readonly [CONTROLREADONLY]; Cấm thi nợ học phí [CTHP]; Cuối nhóm nội dung [CUOINHOMNOIDUNG]; Cuối nhóm phân trang [CUOINHOMPHANTRANG]; Số sv chưa nhập điểm [ChuaNhap]; Đình chỉ [DC]; Điểm bài tập, thực hành (B) [DIEM_B]; Điểm bảo lưu [DIEM_BL]; Điểm chuyên cần (C) [DIEM_C]; Điểm tổng kết học phần [DIEM_HP]; Điểm kiểm tra (K) [DIEM_K]; Điểm tổng kết kiểm tra [DIEM_KT]; Điểm hệ số 1 (P) [DIEM_P]; Điểm hệ số 2 (Q) [DIEM_Q]; Điểm thi (T) [DIEM_T]; Điểm tổng kết thi [DIEM_TH]; Đăng ký thêm [DKThem]; Điểm số đạt [DS_DAT]; Điểm số không đạt [DS_KHONG_DAT]; ĐTB học kỳ 1 [DTBHK1]; ĐTB học kỳ 2 [DTBHK2]; ĐTB học kỳ 3 [DTBHK3]; Đã đăng ký [DaDK]; Số sv đã nhập điểm [DaNhap]; Đạt [Dat]; Ràng buộc xóa SS [DeleteRuleSS]; Điểm chữ [DiemChu]; Điểm khác [DiemKhac]; Độ rộng [DoRong]; Độ rộng edit [DoRongEdit]; Độ rộng field report [DoRongFieldReport]; Độ rộng field view [DoRongFieldView]; Đối tượng tree [DoiTuongTree]; Dòng chẵn [EVENROW]; Dòng đang chọn [FOCUSROW]; Field phụ 1 [FieldCSS]; Field chính 1 [FieldPSS]; Nhóm tiêu đề [GROUPHEADER]; Ghi chú [GhiChu]; Giá trị [GiaTri]; Giá trị [GiaTriTreeArray]; Giá trị [GiaTriTreeDecimal]; Giá trị [GiaTriTreeEnum]; Giá trị [GiaTriTreeInt]; Giá trị [GiaTriTreeLogic]; Giá trị [GiaTriTreeString]; Điểm hệ 10 [HE_10]; Điểm hệ 100 [HE_100]; Điểm hệ 1000 [HE_1000]; Điểm hệ 4 [HE_4]; Điểm hệ 4 (chữ) [HE_4_CHU]; Hoãn thi [HT]; Hoãn thi [HoanThi]; ID value set Report [IDValSetR]; ID set report 1 [IDValSetR1]; Index 1 [Index1]; Index 2 [Index2]; Index 3 [Index3]; Index 4 [Index4]; Khóa phụ 1 [IsKhoaPhuSS]; Khóa chính SS [IsKhoaSS]; Điểm K1 [K1]; Điểm K2 [K2]; Điểm K3 [K3]; Điểm K4 [K4]; Không đạt [KHONG_DAT]; Tên nhãn [LABEL]; Tên đầy đủ [LABEL_FULL]; Tên viết tắt [LABEL_SHORT]; Tên đầy đủ [LOAILABEL]; Logo [LOGO]; Độ dài DB SS [LenDBSS]; Lý do thất bại [LyDoError]; Miễn thi [MT]; Mã báo biểu AQ [MaBaoBieuAQ]; Mã báo biểu user [MaBaoBieuUser]; Mã field so sánh [MaFieldSS]; Mã file so sánh [MaFileSS]; Mã loại điểm [MaLoaiDiem]; Mã user [MaUser]; Mã view AQ [MaViewAQ]; Mã view user [MaViewUser]; Mặc định [MacDinh]; Ngày tháng năm mẫu in [NGAYTHANGNAMMAUIN]; Ngày và user giờ in [NGAYVAUSERGIOIN]; Nhóm nội dung [NHOMNOIDUNG]; Nhóm phân trang [NHOMPHANTRANG]; Ngày thêm [NgayThemC]; Nội dung [NoiDung]; Dòng lẻ [ODDROW]; Điểm P1 [P1]; Điểm P2 [P2]; Điểm P3 [P3]; Điểm P4 [P4]; Điểm P5 [P5]; Điểm P6 [P6]; Phân hệ [PhanHe]; Điểm Q1 [Q1]; Điểm Q1 [Q2]; Điểm Q2 mới [Q3]; Điểm Q4 [Q4]; Điểm Q5 [Q5]; Điểm Q6 [Q6]; Quốc hiệu [QUOCHIEU]; Quyền in bảng điểm [QUYEN_INBANGDIEM]{chọn}; Quyền nhập điểm [QUYEN_NHAPBANGDIEM]{chọn}; Rút môn học [RMH]; Dòng [ROW]; Dòng đã chọn [SELECTEDROW]; Số trang [SOTRANG]; Số thứ tự trong Report [STTReport]; Biểu in con [SUBREPORT]; Sum footer [SUMFOOTER]; Dòng tổng kết [SUMMARY]; Sinh viên ký tên [SVKyTen]; Setting [Setting]; Setting report [SettingReport]; Setting view [SettingView]; Số lần đăng ký [SoLDK]; Số lần đăng ký thất bại [SoLDKLoi]; Số lần đăng ký thành công [SoLDKTC]; Số môn học đăng ký [SoMHDK]; Số mẫu tin [SoMauTin]; Số mẫu tin hk cũ [SoRecordHKCu]; Số mẫu tin hk mới [SoRecordHKMoi]; Số sinh viên [SoSV]; Kiểu field ss [SpecType0SS]; Điểm thi [T1]; Điểm T2 [T2]; Điểm T3 [T3]; Tên mẫu in [TENMAUIN]; Tiêu đề [TIEUDE]; Tiêu đề cột [TITLECOLUMN]; Tiêu đề view [TITLEVIEW]; Điểm tổng kết học phần [TK]; Điểm tổng kết kiểm tra [TKK]; Điểm tổng kết thi [TKT]; Thứ tự tuần [TTTuan]; Tuần 1 [TUAN1]; Tuần 3 [TUAN3]; Bảng phụ SS [TableCSS]; Bảng chính SS [TablePSS]; Tên báo biểu AQ [TenBaoBieuAQ]; Tên báo biểu user [TenBaoBieuUser]; Tên field edit [TenFieldEdit]; Tên field view [TenFieldView]; Tên label edit [TenLabelEdit]; Tên label view [TenLabelView]; Tên loại điểm [TenLoaiDiem]; Tên tuần [TenTuan]; Tên view AQ [TenViewAQ]; Tên view user [TenViewUser]; Thông tin [ThongTin]; Thừa kế tree [ThuaKeTree]; Tiêu đề cột [TieuDeCot]; Tiêu đề cột edit [TieuDeCotEdit]; Tiêu đề cột report [TieuDeCotReport]; Tiêu đề cột view [TieuDeCotView]; Tổ TH [ToTH]; Tổng cộng [TongCong]; Ràng buộc sửa SS [UpdateRuleSS]; Tên viết tắt [VT]; Tên viết tắt [VTTuan]
### VIEWGD_ISPQNHAPSV – Phân quyền nhập điểm theo diện sinh viên
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Giá trị [*GIATRILTBGD]{chọn}
  - Cột ẩn: Cột điểm động [*DIEM]; Điểm bài tập,thực hành (B) [*DIEM_B]; Điểm chuyên cần (C) [*DIEM_C]; Điểm kiểm tra (K) [*DIEM_K]; Điểm hệ số 1 (P) [*DIEM_P]; Điểm hệ số 2 (Q) [*DIEM_Q]; Điểm thi (T) [*DIEM_T]; Giá trị [*GIATRIQBD]; Điểm hệ 10 [*HE_10]; Điểm hệ 100 [*HE_100]; Điểm hệ 1000 [*HE_1000]; Điểm hệ 4 [*HE_4]; HK1 [*HK1]; HK2 [*HK2]; HK3 [*HK3]; *Loại điểm [*LoaiDiem]; Môn học & loại điểm [*MHDiems]; Tên đầy đủ [*TENDAYDU]; Tên ngắn [*TENNGAN]; Tên viết tắt [*TENVT]; Thứ tự [*THUTU]; Thứ tự môn học đăng ký [*TTMHDK]; Tuần [*TUAN]; Giá trị mặc nhiên (DVPC) [AQDefaultValDVPC]; Giá trị mặc nhiên [AQDefaultValTM]; Giá trị mặc nhiên (Trường) [AQDefaultValTruong]; Cho rỗng 1 [AllowNullSS]; Điểm B1 [B1]; Điểm B2 [B2]; Bảng điểm học lại học vượt [BANGDIEM_HOCLAI]; Bảng điểm theo lớp SV [BANGDIEM_LOP]; Bảng ghi điểm theo mã BGD [BANGDIEM_MAGHIDIEM]; Bảng điểm toàn môn học [BANGDIEM_MONHOC]; Bảng điểm theo nhóm/tổ học [BANGDIEM_NHOMTOHOC]; Bảng điểm theo nhóm/tổ thi [BANGDIEM_NHOMTOTHI]; Điểm C1 [C1]; Điểm C2 [C2]; Cấm thi [CH]; Chỉnh định chung [CHINHDINHCHUNG]; Chưa hoàn tất [CHUA_HOAN_TAT]; Chữ ký [CHUKY]; Chung cho report [CHUNGCHOREPORT]; Control disable [CONTROLDISABLE]; Control [CONTROLNORMAL]; Control readonly [CONTROLREADONLY]; Cấm thi nợ học phí [CTHP]; Cuối nhóm nội dung [CUOINHOMNOIDUNG]; Cuối nhóm phân trang [CUOINHOMPHANTRANG]; Số sv chưa nhập điểm [ChuaNhap]; Đình chỉ [DC]; Điểm bài tập, thực hành (B) [DIEM_B]; Điểm bảo lưu [DIEM_BL]; Điểm chuyên cần (C) [DIEM_C]; Điểm tổng kết học phần [DIEM_HP]; Điểm kiểm tra (K) [DIEM_K]; Điểm tổng kết kiểm tra [DIEM_KT]; Điểm hệ số 1 (P) [DIEM_P]; Điểm hệ số 2 (Q) [DIEM_Q]; Điểm thi (T) [DIEM_T]; Điểm tổng kết thi [DIEM_TH]; Đăng ký thêm [DKThem]; Điểm số đạt [DS_DAT]; Điểm số không đạt [DS_KHONG_DAT]; ĐTB học kỳ 1 [DTBHK1]; ĐTB học kỳ 2 [DTBHK2]; ĐTB học kỳ 3 [DTBHK3]; Đã đăng ký [DaDK]; Số sv đã nhập điểm [DaNhap]; Đạt [Dat]; Ràng buộc xóa SS [DeleteRuleSS]; Điểm chữ [DiemChu]; Điểm khác [DiemKhac]; Độ rộng [DoRong]; Độ rộng edit [DoRongEdit]; Độ rộng field report [DoRongFieldReport]; Độ rộng field view [DoRongFieldView]; Đối tượng tree [DoiTuongTree]; Dòng chẵn [EVENROW]; Dòng đang chọn [FOCUSROW]; Field phụ 1 [FieldCSS]; Field chính 1 [FieldPSS]; Nhóm tiêu đề [GROUPHEADER]; Ghi chú [GhiChu]; Giá trị [GiaTri]; Giá trị [GiaTriTreeArray]; Giá trị [GiaTriTreeDecimal]; Giá trị [GiaTriTreeEnum]; Giá trị [GiaTriTreeInt]; Giá trị [GiaTriTreeLogic]; Giá trị [GiaTriTreeString]; Điểm hệ 10 [HE_10]; Điểm hệ 100 [HE_100]; Điểm hệ 1000 [HE_1000]; Điểm hệ 4 [HE_4]; Điểm hệ 4 (chữ) [HE_4_CHU]; Hoãn thi [HT]; Hoãn thi [HoanThi]; ID value set Report [IDValSetR]; ID set report 1 [IDValSetR1]; Index 1 [Index1]; Index 2 [Index2]; Index 3 [Index3]; Index 4 [Index4]; Khóa phụ 1 [IsKhoaPhuSS]; Khóa chính SS [IsKhoaSS]; Điểm K1 [K1]; Điểm K2 [K2]; Điểm K3 [K3]; Điểm K4 [K4]; Không đạt [KHONG_DAT]; Tên nhãn [LABEL]; Tên đầy đủ [LABEL_FULL]; Tên viết tắt [LABEL_SHORT]; Tên đầy đủ [LOAILABEL]; Logo [LOGO]; Độ dài DB SS [LenDBSS]; Lý do thất bại [LyDoError]; Miễn thi [MT]; Mã báo biểu AQ [MaBaoBieuAQ]; Mã báo biểu user [MaBaoBieuUser]; Mã field so sánh [MaFieldSS]; Mã file so sánh [MaFileSS]; Mã loại điểm [MaLoaiDiem]; Mã user [MaUser]; Mã view AQ [MaViewAQ]; Mã view user [MaViewUser]; Mặc định [MacDinh]; Ngày tháng năm mẫu in [NGAYTHANGNAMMAUIN]; Ngày và user giờ in [NGAYVAUSERGIOIN]; Nhóm nội dung [NHOMNOIDUNG]; Nhóm phân trang [NHOMPHANTRANG]; Ngày thêm [NgayThemC]; Nội dung [NoiDung]; Dòng lẻ [ODDROW]; Điểm P1 [P1]; Điểm P2 [P2]; Điểm P3 [P3]; Điểm P4 [P4]; Điểm P5 [P5]; Điểm P6 [P6]; Phân hệ [PhanHe]; Điểm Q1 [Q1]; Điểm Q1 [Q2]; Điểm Q2 mới [Q3]; Điểm Q4 [Q4]; Điểm Q5 [Q5]; Điểm Q6 [Q6]; Quốc hiệu [QUOCHIEU]; Quyền in bảng điểm [QUYEN_INBANGDIEM]{chọn}; Quyền nhập điểm [QUYEN_NHAPBANGDIEM]{chọn}; Rút môn học [RMH]; Dòng [ROW]; Dòng đã chọn [SELECTEDROW]; Số trang [SOTRANG]; Số thứ tự trong Report [STTReport]; Biểu in con [SUBREPORT]; Sum footer [SUMFOOTER]; Dòng tổng kết [SUMMARY]; Sinh viên ký tên [SVKyTen]; Setting [Setting]; Setting report [SettingReport]; Setting view [SettingView]; Số lần đăng ký [SoLDK]; Số lần đăng ký thất bại [SoLDKLoi]; Số lần đăng ký thành công [SoLDKTC]; Số môn học đăng ký [SoMHDK]; Số mẫu tin [SoMauTin]; Số mẫu tin hk cũ [SoRecordHKCu]; Số mẫu tin hk mới [SoRecordHKMoi]; Số sinh viên [SoSV]; Kiểu field ss [SpecType0SS]; Điểm thi [T1]; Điểm T2 [T2]; Điểm T3 [T3]; Tên mẫu in [TENMAUIN]; Tiêu đề [TIEUDE]; Tiêu đề cột [TITLECOLUMN]; Tiêu đề view [TITLEVIEW]; Điểm tổng kết học phần [TK]; Điểm tổng kết kiểm tra [TKK]; Điểm tổng kết thi [TKT]; Thứ tự tuần [TTTuan]; Tuần 1 [TUAN1]; Tuần 3 [TUAN3]; Bảng phụ SS [TableCSS]; Bảng chính SS [TablePSS]; Tên báo biểu AQ [TenBaoBieuAQ]; Tên báo biểu user [TenBaoBieuUser]; Tên field edit [TenFieldEdit]; Tên field view [TenFieldView]; Tên label edit [TenLabelEdit]; Tên label view [TenLabelView]; Tên loại điểm [TenLoaiDiem]; Tên tuần [TenTuan]; Tên view AQ [TenViewAQ]; Tên view user [TenViewUser]; Thông tin [ThongTin]; Thừa kế tree [ThuaKeTree]; Tiêu đề cột [TieuDeCot]; Tiêu đề cột edit [TieuDeCotEdit]; Tiêu đề cột report [TieuDeCotReport]; Tiêu đề cột view [TieuDeCotView]; Tổ TH [ToTH]; Tổng cộng [TongCong]; Ràng buộc sửa SS [UpdateRuleSS]; Tên viết tắt [VT]; Tên viết tắt [VTTuan]
### VIEWGD_LABELDVHT – Định nghĩa nhãn cho từ khóa tín chỉ/DVHT
- Lưới 1 «Định nghĩa nhãn cụm từ "Đơn vị học tập"»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Giá trị cấp cha [*ColNameP](chỉ đọc); Giá trị [GiaTriTreeString]
### VIEWGD_LAMTRONDIEMTB – Làm tròn điểm trung bình
- Lưới 1 «Qui định làm tròn điểm trung bình các hệ điểm»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Giá trị cấp cha [*ColNameP](chỉ đọc); Điểm hệ 4 [*HE_4]{chọn}; Điểm hệ 10 [*HE_10]; Điểm hệ 100 [*HE_100]; Điểm hệ 1000 [*HE_1000]
### VIEWGD_LAMTRONDIEMTHANHPHAN – Qui định cách làm tròn điểm thành phần các hệ điểm
- Lưới 1 «Qui định cách làm tròn điểm thành phần các hệ điểm»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Giá trị cấp cha [*ColNameP](chỉ đọc); Điểm hệ 4 [*HE_4]{chọn}; Điểm hệ 10 [*HE_10]{chọn}; Điểm hệ 100 [*HE_100]{chọn}; Điểm hệ 1000 [*HE_1000]{chọn}
### VIEWGD_MUCDIEMDATHEDIEM – Mức điểm đạt chung các hệ điểm
- Lưới 1 «Mức điểm đạt chung các hệ điểm»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Giá trị [GiaTriTreeDecimal]{số}
### VIEWGD_SODIEMMAX – Số cột điểm max từng loại điểm (AQ Max)
- Lưới 1 «-»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Giá trị [GiaTriTreeInt]
### VIEWGD_SODIEMMAXTUNGQUICHEDIEM – Số cột điểm max từng loại điểm
- Lưới 1 «Số cột điểm max từng loại điểm»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Giá trị cấp cha [*ColNameP](chỉ đọc); Giá trị [GiaTriTreeInt]{số}
### VIEWGD_TENNHANDIEM – Tên nhãn điểm của điểm thành phần
- Lưới 1 «Tên nhãn điểm của điểm thành phần»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Giá trị cấp cha [*ColNameP](chỉ đọc); Giá trị [GiaTriTreeString]
### ViewGetWiFI – ViewGetWiFI
- Lưới 1 «Danh sách wifi»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã đối tượng [MaDoiTuong]; Password [Password]
### VIEWGH_CHINHDINHFONT – Chỉnh định giao diện
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Tên Enum [ColNameEnum]; Chỉnh định chung [CHINHDINHCHUNG]; Tiêu đề view [TITLEVIEW]; Tiêu đề cột [TITLECOLUMN]; Nhóm tiêu đề [GROUPHEADER]; Dòng [ROW]; Dòng đang chọn [FOCUSROW]; Dòng đã chọn [SELECTEDROW]; Dòng chẵn [EVENROW]; Dòng lẻ [ODDROW]; Sum footer [SUMFOOTER]; Dòng tổng kết [SUMMARY]; Tên nhãn [LABEL]; Control [CONTROLNORMAL]; Control readonly [CONTROLREADONLY]; Control disable [CONTROLDISABLE]
  - Cột ẩn: Cột điểm động [*DIEM]; Điểm bài tập,thực hành (B) [*DIEM_B]; Điểm chuyên cần (C) [*DIEM_C]; Điểm kiểm tra (K) [*DIEM_K]; Điểm hệ số 1 (P) [*DIEM_P]; Điểm hệ số 2 (Q) [*DIEM_Q]; Điểm thi (T) [*DIEM_T]; Điểm hệ 10 [*HE_10]; Điểm hệ 100 [*HE_100]; Điểm hệ 1000 [*HE_1000]; Điểm hệ 4 [*HE_4]; HK1 [*HK1]; HK2 [*HK2]; HK3 [*HK3]; *Loại điểm [*LoaiDiem]; Thứ tự môn học đăng ký [*TTMHDK]; Tuần [*TUAN]; Giá trị mặc nhiên (DVPC) [AQDefaultValDVPC]; Giá trị mặc nhiên [AQDefaultValTM]; Giá trị mặc nhiên (Trường) [AQDefaultValTruong]; Cho rỗng 1 [AllowNullSS]; Điểm B1 [B1]; Điểm B2 [B2]; Bảng điểm học lại học vượt [BANGDIEM_HOCLAI]; Bảng điểm theo lớp SV [BANGDIEM_LOP]; Bảng ghi điểm theo mã BGD [BANGDIEM_MAGHIDIEM]; Bảng điểm toàn môn học [BANGDIEM_MONHOC]; Bảng điểm theo nhóm/tổ học [BANGDIEM_NHOMTOHOC]; Bảng điểm theo nhóm/tổ thi [BANGDIEM_NHOMTOTHI]; Điểm C1 [C1]; Điểm C2 [C2]; Cấm thi [CH]; Chưa hoàn tất [CHUA_HOAN_TAT]; Chữ ký [CHUKY]; Chung cho report [CHUNGCHOREPORT]; Cấm thi nợ học phí [CTHP]; Cuối nhóm nội dung [CUOINHOMNOIDUNG]; Cuối nhóm phân trang [CUOINHOMPHANTRANG]; Số sv chưa nhập điểm [ChuaNhap]; Đình chỉ [DC]; Điểm bài tập, thực hành (B) [DIEM_B]; Điểm bảo lưu [DIEM_BL]; Điểm chuyên cần (C) [DIEM_C]; Điểm tổng kết học phần [DIEM_HP]; Điểm kiểm tra (K) [DIEM_K]; Điểm tổng kết kiểm tra [DIEM_KT]; Điểm hệ số 1 (P) [DIEM_P]; Điểm hệ số 2 (Q) [DIEM_Q]; Điểm thi (T) [DIEM_T]; Điểm tổng kết thi [DIEM_TH]; Đăng ký thêm [DKThem]; Điểm số đạt [DS_DAT]; Điểm số không đạt [DS_KHONG_DAT]; ĐTB học kỳ 1 [DTBHK1]; ĐTB học kỳ 2 [DTBHK2]; ĐTB học kỳ 3 [DTBHK3]; Đã đăng ký [DaDK]; Số sv đã nhập điểm [DaNhap]; Đạt [Dat]; Ràng buộc xóa SS [DeleteRuleSS]; Điểm chữ [DiemChu]; Điểm khác [DiemKhac]; Độ rộng [DoRong]; Độ rộng edit [DoRongEdit]; Độ rộng field report [DoRongFieldReport]; Độ rộng field view [DoRongFieldView]; Đối tượng tree [DoiTuongTree]; Field phụ 1 [FieldCSS]; Field chính 1 [FieldPSS]; Ghi chú [GhiChu]; Giá trị [GiaTriTreeArray]; Giá trị [GiaTriTreeDecimal]; Giá trị [GiaTriTreeEnum]; Giá trị [GiaTriTreeInt]; Giá trị [GiaTriTreeLogic]; Giá trị [GiaTriTreeString]; Điểm hệ 10 [HE_10]; Điểm hệ 100 [HE_100]; Điểm hệ 1000 [HE_1000]; Điểm hệ 4 [HE_4]; Điểm hệ 4 (chữ) [HE_4_CHU]; Hoãn thi [HT]; Hoãn thi [HoanThi]; Khóa phụ 1 [IsKhoaPhuSS]; Khóa chính SS [IsKhoaSS]; Điểm K1 [K1]; Điểm K2 [K2]; Điểm K3 [K3]; Điểm K4 [K4]; Không đạt [KHONG_DAT]; Tên đầy đủ [LABEL_FULL]; Tên viết tắt [LABEL_SHORT]; Tên đầy đủ [LOAILABEL]; Logo [LOGO]; Độ dài DB SS [LenDBSS]; Lý do thất bại [LyDoError]; Miễn thi [MT]; Mã báo biểu AQ [MaBaoBieuAQ]; Mã báo biểu user [MaBaoBieuUser]; Mã field so sánh [MaFieldSS]; Mã file so sánh [MaFileSS]; Mã loại điểm [MaLoaiDiem]; Mã view AQ [MaViewAQ]; Mã view user [MaViewUser]; Mặc định [MacDinh]; Ngày tháng năm mẫu in [NGAYTHANGNAMMAUIN]; Ngày và user giờ in [NGAYVAUSERGIOIN]; Nhóm nội dung [NHOMNOIDUNG]; Nhóm phân trang [NHOMPHANTRANG]; Nội dung [NoiDung]; Điểm P1 [P1]; Điểm P2 [P2]; Điểm P3 [P3]; Điểm P4 [P4]; Điểm P5 [P5]; Điểm P6 [P6]; Điểm Q1 [Q1]; Điểm Q1 [Q2]; Điểm Q2 mới [Q3]; Điểm Q4 [Q4]; Điểm Q5 [Q5]; Điểm Q6 [Q6]; Quốc hiệu [QUOCHIEU]; Quyền in bảng điểm [QUYEN_INBANGDIEM]; Quyền nhập điểm [QUYEN_NHAPBANGDIEM]; Rút môn học [RMH]; Số trang [SOTRANG]; Số thứ tự trong Report [STTReport]; Biểu in con [SUBREPORT]; Sinh viên ký tên [SVKyTen]; Setting [Setting]; Setting report [SettingReport]; Setting view [SettingView]; Số lần đăng ký [SoLDK]; Số lần đăng ký thất bại [SoLDKLoi]; Số lần đăng ký thành công [SoLDKTC]; Số môn học đăng ký [SoMHDK]; Số mẫu tin [SoMauTin]; Số mẫu tin hk cũ [SoRecordHKCu]; Số mẫu tin hk mới [SoRecordHKMoi]; Số sinh viên [SoSV]; Kiểu field ss [SpecType0SS]; Điểm thi [T1]; Điểm T2 [T2]; Điểm T3 [T3]; Tên mẫu in [TENMAUIN]; Tiêu đề [TIEUDE]; Điểm tổng kết học phần [TK]; Điểm tổng kết kiểm tra [TKK]; Điểm tổng kết thi [TKT]; Thứ tự tuần [TTTuan]; Tuần 1 [TUAN1]; Tuần 3 [TUAN3]; Bảng phụ SS [TableCSS]; Bảng chính SS [TablePSS]; Tên báo biểu AQ [TenBaoBieuAQ]; Tên báo biểu user [TenBaoBieuUser]; Tên field edit [TenFieldEdit]; Tên field view [TenFieldView]; Tên label edit [TenLabelEdit]; Tên label view [TenLabelView]; Tên loại điểm [TenLoaiDiem]; Tên tuần [TenTuan]; Tên view AQ [TenViewAQ]; Tên view user [TenViewUser]; Thông tin [ThongTin]; Thừa kế tree [ThuaKeTree]; Tiêu đề cột [TieuDeCot]; Tiêu đề cột edit [TieuDeCotEdit]; Tiêu đề cột report [TieuDeCotReport]; Tiêu đề cột view [TieuDeCotView]; Tổ TH [ToTH]; Tổng cộng [TongCong]; Ràng buộc sửa SS [UpdateRuleSS]; Tên viết tắt [VT]; Tên viết tắt [VTTuan]
### VIEWGH_CHINHDINHTHONGSOREPORT – Chỉnh định báo biểu
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Tên Enum [ColNameEnum]; Chung cho report [CHUNGCHOREPORT]; Logo [LOGO]; Quốc hiệu [QUOCHIEU]; Tiêu đề [TIEUDE]; Nhóm phân trang [NHOMPHANTRANG]; Tiêu đề cột [TieuDeCot]; Nhóm nội dung [NHOMNOIDUNG]; Nội dung [NoiDung]; Cuối nhóm nội dung [CUOINHOMNOIDUNG]; Cuối nhóm phân trang [CUOINHOMPHANTRANG]; Ghi chú [GhiChu]; Chữ ký [CHUKY]; Tên mẫu in [TENMAUIN]; Số trang [SOTRANG]; Ngày và user giờ in [NGAYVAUSERGIOIN]; Ngày tháng năm mẫu in [NGAYTHANGNAMMAUIN]; Biểu in con [SUBREPORT]
  - Cột ẩn: Cột điểm động [*DIEM]; Điểm bài tập,thực hành (B) [*DIEM_B]; Điểm chuyên cần (C) [*DIEM_C]; Điểm kiểm tra (K) [*DIEM_K]; Điểm hệ số 1 (P) [*DIEM_P]; Điểm hệ số 2 (Q) [*DIEM_Q]; Điểm thi (T) [*DIEM_T]; Điểm hệ 10 [*HE_10]; Điểm hệ 100 [*HE_100]; Điểm hệ 1000 [*HE_1000]; Điểm hệ 4 [*HE_4]; HK1 [*HK1]; HK2 [*HK2]; HK3 [*HK3]; *Loại điểm [*LoaiDiem]; Thứ tự môn học đăng ký [*TTMHDK]; Tuần [*TUAN]; Giá trị mặc nhiên (DVPC) [AQDefaultValDVPC]; Giá trị mặc nhiên [AQDefaultValTM]; Giá trị mặc nhiên (Trường) [AQDefaultValTruong]; Cho rỗng 1 [AllowNullSS]; Điểm B1 [B1]; Điểm B2 [B2]; Bảng điểm học lại học vượt [BANGDIEM_HOCLAI]; Bảng điểm theo lớp SV [BANGDIEM_LOP]; Bảng ghi điểm theo mã BGD [BANGDIEM_MAGHIDIEM]; Bảng điểm toàn môn học [BANGDIEM_MONHOC]; Bảng điểm theo nhóm/tổ học [BANGDIEM_NHOMTOHOC]; Bảng điểm theo nhóm/tổ thi [BANGDIEM_NHOMTOTHI]; Điểm C1 [C1]; Điểm C2 [C2]; Cấm thi [CH]; Chỉnh định chung [CHINHDINHCHUNG]; Chưa hoàn tất [CHUA_HOAN_TAT]; Control disable [CONTROLDISABLE]; Control [CONTROLNORMAL]; Control readonly [CONTROLREADONLY]; Cấm thi nợ học phí [CTHP]; Số sv chưa nhập điểm [ChuaNhap]; Đình chỉ [DC]; Điểm bài tập, thực hành (B) [DIEM_B]; Điểm bảo lưu [DIEM_BL]; Điểm chuyên cần (C) [DIEM_C]; Điểm tổng kết học phần [DIEM_HP]; Điểm kiểm tra (K) [DIEM_K]; Điểm tổng kết kiểm tra [DIEM_KT]; Điểm hệ số 1 (P) [DIEM_P]; Điểm hệ số 2 (Q) [DIEM_Q]; Điểm thi (T) [DIEM_T]; Điểm tổng kết thi [DIEM_TH]; Đăng ký thêm [DKThem]; Điểm số đạt [DS_DAT]; Điểm số không đạt [DS_KHONG_DAT]; ĐTB học kỳ 1 [DTBHK1]; ĐTB học kỳ 2 [DTBHK2]; ĐTB học kỳ 3 [DTBHK3]; Đã đăng ký [DaDK]; Số sv đã nhập điểm [DaNhap]; Đạt [Dat]; Ràng buộc xóa SS [DeleteRuleSS]; Điểm chữ [DiemChu]; Điểm khác [DiemKhac]; Độ rộng [DoRong]; Độ rộng edit [DoRongEdit]; Độ rộng field report [DoRongFieldReport]; Độ rộng field view [DoRongFieldView]; Đối tượng tree [DoiTuongTree]; Dòng chẵn [EVENROW]; Dòng đang chọn [FOCUSROW]; Field phụ 1 [FieldCSS]; Field chính 1 [FieldPSS]; Nhóm tiêu đề [GROUPHEADER]; Giá trị [GiaTriTreeArray]; Giá trị [GiaTriTreeDecimal]; Giá trị [GiaTriTreeEnum]; Giá trị [GiaTriTreeInt]; Giá trị [GiaTriTreeLogic]; Giá trị [GiaTriTreeString]; Điểm hệ 10 [HE_10]; Điểm hệ 100 [HE_100]; Điểm hệ 1000 [HE_1000]; Điểm hệ 4 [HE_4]; Điểm hệ 4 (chữ) [HE_4_CHU]; Hoãn thi [HT]; Hoãn thi [HoanThi]; Khóa phụ 1 [IsKhoaPhuSS]; Khóa chính SS [IsKhoaSS]; Điểm K1 [K1]; Điểm K2 [K2]; Điểm K3 [K3]; Điểm K4 [K4]; Không đạt [KHONG_DAT]; Tên nhãn [LABEL]; Tên đầy đủ [LABEL_FULL]; Tên viết tắt [LABEL_SHORT]; Tên đầy đủ [LOAILABEL]; Độ dài DB SS [LenDBSS]; Lý do thất bại [LyDoError]; Miễn thi [MT]; Mã báo biểu AQ [MaBaoBieuAQ]; Mã báo biểu user [MaBaoBieuUser]; Mã field so sánh [MaFieldSS]; Mã file so sánh [MaFileSS]; Mã loại điểm [MaLoaiDiem]; Mã view AQ [MaViewAQ]; Mã view user [MaViewUser]; Mặc định [MacDinh]; Dòng lẻ [ODDROW]; Điểm P1 [P1]; Điểm P2 [P2]; Điểm P3 [P3]; Điểm P4 [P4]; Điểm P5 [P5]; Điểm P6 [P6]; Điểm Q1 [Q1]; Điểm Q1 [Q2]; Điểm Q2 mới [Q3]; Điểm Q4 [Q4]; Điểm Q5 [Q5]; Điểm Q6 [Q6]; Quyền in bảng điểm [QUYEN_INBANGDIEM]; Quyền nhập điểm [QUYEN_NHAPBANGDIEM]; Rút môn học [RMH]; Dòng [ROW]; Dòng đã chọn [SELECTEDROW]; Số thứ tự trong Report [STTReport]; Sum footer [SUMFOOTER]; Dòng tổng kết [SUMMARY]; Sinh viên ký tên [SVKyTen]; Setting [Setting]; Setting report [SettingReport]; Setting view [SettingView]; Số lần đăng ký [SoLDK]; Số lần đăng ký thất bại [SoLDKLoi]; Số lần đăng ký thành công [SoLDKTC]; Số môn học đăng ký [SoMHDK]; Số mẫu tin [SoMauTin]; Số mẫu tin hk cũ [SoRecordHKCu]; Số mẫu tin hk mới [SoRecordHKMoi]; Số sinh viên [SoSV]; Kiểu field ss [SpecType0SS]; Điểm thi [T1]; Điểm T2 [T2]; Điểm T3 [T3]; Tiêu đề cột [TITLECOLUMN]; Tiêu đề view [TITLEVIEW]; Điểm tổng kết học phần [TK]; Điểm tổng kết kiểm tra [TKK]; Điểm tổng kết thi [TKT]; Thứ tự tuần [TTTuan]; Tuần 1 [TUAN1]; Tuần 3 [TUAN3]; Bảng phụ SS [TableCSS]; Bảng chính SS [TablePSS]; Tên báo biểu AQ [TenBaoBieuAQ]; Tên báo biểu user [TenBaoBieuUser]; Tên field edit [TenFieldEdit]; Tên field view [TenFieldView]; Tên label edit [TenLabelEdit]; Tên label view [TenLabelView]; Tên loại điểm [TenLoaiDiem]; Tên tuần [TenTuan]; Tên view AQ [TenViewAQ]; Tên view user [TenViewUser]; Thông tin [ThongTin]; Thừa kế tree [ThuaKeTree]; Tiêu đề cột edit [TieuDeCotEdit]; Tiêu đề cột report [TieuDeCotReport]; Tiêu đề cột view [TieuDeCotView]; Tổ TH [ToTH]; Tổng cộng [TongCong]; Ràng buộc sửa SS [UpdateRuleSS]; Tên viết tắt [VT]; Tên viết tắt [VTTuan]
### VIEWGH_THONGTINVIEWDKMH – Thông tin giao diện đăng ký môn học
- Lưới 1 «Chọn đối tượng hiển thị ở trang đăng ký»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa bên phải
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Giá trị cấp cha [*ColNameP](chỉ đọc); Giá trị [GiaTriTreeLogic]
### VIEWGHEPCAITHIEN – Ghép cải thiện vào danh sách thi
- Lưới 1 «Danh sách đăng ký cải thiện chưa ghép vào danh sách thi học kỳ đang xử lý» (bảng LSVCaiThien); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Điểm cũ [DiemCu](chỉ đọc); Kỳ thi [KyHieuTP](chỉ đọc)
  - Nút btnSave: "Lưu" (F3)
### VIEWGHEPHOANTHI – Ghép hoãn thi vào danh sách thi
- Lưới 1 «Danh sách sinh viên hoãn thi chưa được ghép thi (ở tất cả học kỳ)» (bảng LSVHT); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Chọn kỳ thi ghép thi trong học kỳ [KyHieuTP]; Học kỳ học [NHHK]
  - Nút btnSave: "Lưu" (F6)
### VIEWGHEPPHONGTHI – Ghép phòng thi
- Lưới 1 «Danh sách phòng thi đã ghép»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã phòng [MaPH](chỉ đọc); Mã phòng [MaPHP]; Tên phòng [TenPH](chỉ đọc); Tên phòng [TenPHP]; Mã môn học [MaMH](chỉ đọc); Ngày thi [NgayThiP]; Tên môn học [TenMH](chỉ đọc); Tiết thi bắt đầu [TietThiBDP]; Số SV tổ thi [SoSVToThi](chỉ đọc); Tổng số thí sinh [SoThiSinh](chỉ đọc); Tiết bắt đầu [TietThiBD]
### ViewGS_BOXHDiemRL – Bộ xếp hạng rèn luyện
- Lưới 1 «Bộ xếp hạng qui chế»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Giá trị [GiaTriTreeString]
### ViewHDataFlag – View dinh nghia file bat co
- Lưới 1 «Danh sách file» (bảng HDataFlag); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã file [MaFile]; Tên file [TenFile]; Tạo cờ? [IsTaoCo]
  - Ô trên form sửa: #MaFile, #TenFile, #IsTaoCo
### VIEWHIEUCHINHSSOTOTHI – Hiệu chỉnh sỉ số tổ thi
- Lưới 1 «Danh sách thí sinh» (bảng SDMSV); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]
### ViewHKhoaSoPhanHe – Khóa dữ liệu phát sinh từng phân hệ trong học kỳ
- Lưới 1 «Khóa dữ liệu phát sinh từng phân hệ trong học kỳ» (bảng HKhoaSoPhanHe); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Niên học học kỳ [NHHK]{số}(chỉ đọc)
### VIEWHUYDANHSACHDOTTHI – Hủy danh sách đợt thi
- Lưới 1 «Danh sách thống kê số thí sinh và số nhóm trong từng đợt thi»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đợt thi [MaDotThi](chỉ đọc); Tên đợt thi [TenDotThi](chỉ đọc); Tổng số thí sinh [SoThiSinh](chỉ đọc); Số nhóm thi [SoNhom](chỉ đọc)
### VIEWHUYDANHSACHTHITHEOMH – Hủy danh sách thi theo môn học
- Lưới 1 «Danh sách môn học»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Nhóm thi [NhomThi]; Mã đợt thi [MaDotThi]; Tên môn học [TenMH]; Số TC [SoTinChi]; Tên đợt thi [TenDotThi]; Tổng số thí sinh [SoThiSinh]; Số sinh viên [SoSV]
### VIEWHUYGHEPCAITHIEN – Hủy ghép cải thiện vào danh sách thi
- Lưới 1 «Danh sách đăng ký thi cãi thiện đã ghép vào danh sách thi học kỳ đang xử lý» (bảng LSVCaiThien); tắt: Thêm, Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Điểm cũ [DiemCu](chỉ đọc); Kỳ thi [KyHieuTP](chỉ đọc)
  - Nút btnDelete: "Xóa" (F4)
### VIEWHUYGHEPHOANTHI – Hủy ghép hoãn thi vào danh sách thi
- Lưới 1 «Danh sách sinh viên hoãn thi đã ghép thi ở học kỳ đang xử lý» (bảng LSVHT); tắt: Thêm, Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Kỳ thi đã ghép [KyHieuTP]
  - Nút btnDelete: "Xóa" (F7)
### VIEWHUYLICHTHITHEODOT – Hủy lịch thi theo đợt
- Lưới 1 «Danh sách đợt thi»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã đợt thi [MaDotThi](chỉ đọc); Tên đợt thi [TenDotThi](chỉ đọc); Tổng số thí sinh [SoThiSinh](chỉ đọc); Số môn thi [SoMonThi](chỉ đọc); Lịch thi [DSLichThi]; Danh sách thí sinh [DSThiSinh]; Danh sách môn thi [DSMonThi]
### VIEWHUYLICHTHITHEOMONHOC – Hủy lịch thi theo môn học
- Lưới 1 «Danh sách môn thi»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Tổng số thí sinh [SoThiSinh](chỉ đọc); Lịch thi [DSLichThi](chỉ đọc); Danh sách thí sinh [DSThiSinh](chỉ đọc)
  - Cột ẩn: Nhóm thi [NhomThi]; Tổ thi [ToThi]
### VIEWHUYLICHTHITHEOTO – Hủy lịch thi theo môn học
- Lưới 1 «Danh sách nhóm thi»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Tổng số thí sinh [SoThiSinh](chỉ đọc); Lịch thi [DSLichThi](chỉ đọc); Danh sách thí sinh [DSThiSinh](chỉ đọc)
  - Cột ẩn: Nhóm thi [NhomThi](chỉ đọc); Tổ thi [ToThi](chỉ đọc)
### ViewImpMHBH – Danh sách môn học bậc hệ
- Lưới 1 (bảng KBacHeMH); tắt: Sửa, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]; Mã môn học [MaMH]; Tên môn học [TenMH]; Số tiết [SoTietF]{số}; Bậc hệ [IDBH]{nút …}; Môn học [IDMH]{nút …}; IDBacHeMH [IDBacHeMH]
  - Ô trên form sửa: #TenBH, #TenMH, #IDBH, #IDMH
### ViewImportDKCT – Dung import dang ky cai thien
- Lưới 1 (bảng LSVCaiThien); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Ngày nhập [NgayNhapThiCT]; Ghi chú [GCSVCaiThien]
### VIEWIMPORTGCN – Import giay chung nhan thanh cong
- Lưới 1 «danh sách sinh viên hợp lệ» (bảng SGCNSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Mã GCN [MaGCN]; Tên giấy CN [TenGCN]
### VIEWIMPORTGCNCopy – Import giay chung nhan trung
- Lưới 1 (bảng SGCNSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Mã GCN [MaGCN]; Tên giấy CN [TenGCN]
### VIEWIMPORTGCNCopyCopy – Import giay chung nhan that bai
- Lưới 1 (bảng SGCNSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Mã GCN [MaGCN]; Tên giấy CN [TenGCN]
### ViewImportHSHK – View import he so hk
- Lưới 1 (bảng SDMLOP); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Mã mức [MaMucCV]; Mã mức [MaMucLP]; Mã mức [MaMucDX]
### ViewImportHSSV – Import ho so sinh vien
- Lưới 1 (bảng SHSSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Ngày nộp hồ sơ [NgayNopHS]
### ViewImportKCTDTCH – View import chương trình đào tạo kế hoạch
- Lưới 1 (bảng KCTDTCH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Mã Ng/CNg [MaNgChng]; Mã PB [MaPB]; Xét học kỳ thứ [HKThu]; Thứ tự [TTCTDTCH]; Mã môn học [MaMH]; Môn tốt nghiệp? [IsMHTN]; Môn bắt buộc [IsMHBB]; Đối tượng [DoiTuongSV]
### ViewImportKCTDTKH – View import chương trình đào tạo kế hoạch
- Lưới 1 (bảng KCTDTKH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Thứ tự [TTCTDTKH]; Mã khối [MaKhoi]; Mã môn học [MaMH]; Niên học học kỳ [NHHK]; Môn tốt nghiệp? [IsMHTN]; Môn bắt buộc [IsMHBB]; Đối tượng [DoiTuongSV]
### ViewImportKCTDTTH – View import chương trình đào tạo thực hiện
- Lưới 1 (bảng KCTDTTH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Thứ tự [TTCTDTTH]; Mã khối [MaKhoi]; Mã môn học [MaMH]; Niên học học kỳ [NHHK]; Môn tốt nghiệp? [IsMHTN]; Môn bắt buộc [IsMHBB]; Đối tượng [DoiTuongSV]
### ViewImportKuutienLop – View import file kuutienlop
- Lưới 1 (bảng KLOPHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Mã phòng [MaPH]; Buổi [Buoi]
### VIEWIMPORTLOP – Import lớp - nhóm học mở trong học kỳ
- Lưới 1 «Danh sách lớp - nhóm học» (bảng KToLop); tắt: Thêm, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Mã lớp [MaLop]; Tên môn học [TenMH]; Số TC [SoTinChi]; Tên lớp [TenLop]; Tên viết tắt [VTLop]; Ghi chú [GcLop]
  - Cột ẩn: Hình thức thi [HTThi]; Loại thành phần [KyHieuTTP]; Niên học học kỳ [NHHK]; Nhóm/tổ [NhomTo]; Sĩ số cho phép đk [SiSoCPDK]; SL trung bình nhóm [SiSoTKB]; Số lần thi [SoLanThi]; Số tiết môn học [SoTietMH]; Số tiết/tuần [SoTietTuan]; Tổ hợp [tphop]
  - Nút btnImport: "Import" (F11)
  - Nút btnDel: "Hủy lớp nhóm học" (F12)
### ViewImportMHTQ – Import cay phan cap
- Lưới 1 (bảng MMHTQCT); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Mã mhtq [MaMHTQ]; Loại tiên quyết [LoaiTQ]; Nhánh ĐK [NHANHDK]; Ký hiệu OR [NHOMDK]; Niên khóa [NienKhoaSV]
### ViewIMportMMHTQ – View import  mon học tiên quyết  thành công
- Lưới 1 «Danh sách môn học» (bảng MMHTQ); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Mã môn học [MaMHDK]; Tên MH điều kiện [TenMHDK]
### ViewIMportMMHTQCopy – View import  mon học tiên quyết  that bai
- Lưới 1 «Danh sách môn học» (bảng MMHTQ); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Mã môn học [MaMHDK]; Tên MH điều kiện [TenMHDK]
### ViewIMportMMHTQCopyCopy – View import  mon học tiên quyết  tồn tại
- Lưới 1 «Danh sách môn học» (bảng MMHTQ); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Mã môn học [MaMHDK]; Tên MH điều kiện [TenMHDK]
### ViewInBangTongHopKQXD – In bảng tổng hợp kết quả xét duyệt
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### ViewInBienBanXetDuyet – Danh sách đề tài nghiên cứu khoa học đã xét duyệt
- Lưới 1 «Danh sách đề tài đã được xét duyệt» (bảng OXetDuyetDeTai); tắt: Thêm, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đề tài [MaDeTaiNCKH]; Tên đề tài [TenDeTaiNCKH]; Học kỳ đăng ký [NHHK]; Mã chủ nhiệm đề tài [MaNV]; Tên chủ nhiệm đề tài [TenDayDuNV]; Số quyết định [SoQDXetDuyet]; Ngày quyết định [NgayQDXetDuyet]{ngày}; Ngày giờ xét duyệt [NgayGioXetDuyet]; Địa điểm xét duyệt [DiaDiemXetDuyet]; Đạt xét duyệt [IsDatXetDuyet]; Điểm trung bình [DiemTBXetDuyet]; Xếp loại xét duyệt [TenXEPLOAIXD]
  - Cột ẩn: Ghi chú 1 [GhiChu1]; Đề tài [IDDeTaiNCKH]; ID xếp loại [IDXepLoaiXD]; ID xét duyệt [IDXetDuyetDeTai]; Hình biên bản [ImageBienBan]; Ý kiến xét duyệt [YKienXetDuyet]
  - Ô trên form sửa: #IsDatXetDuyet, #DiemTBXetDuyet, #GhiChu1, #IDXepLoaiXD, #ImageBienBan, #YKienXetDuyet
### VIEWINFOSV – View thông tin chung sinh viên
- Lưới 1 «Danh sách sinh viên»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Phái [Phai]; Mã lớp [MaLop]; Tên lớp [TenLop]; Mã khối [MaKhoi]; Tên khối [TenKhoi]; Niên khóa [NienKhoa]; NHHK vào [NHHKVao]; NHHK ra [NHHKRa]; Mã Ng/CNg [MaNgChng]; Tên ng/chng [TenNgChng]; Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]
### VIEWINLICHTHI1SV – In lich thi 1 sinh vien
- Lưới 1 «Danh sách môn học»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Sỉ số [SiSoDuKien](chỉ đọc); Nhóm thi [NhomThi](chỉ đọc); Tổ thi [ToThi](chỉ đọc); Tổ thi con [ToThiCon](chỉ đọc); Ngày thi [NgayThi]{ngày}(chỉ đọc); Giờ bắt đầu [GioBD](chỉ đọc); Giờ thi [GioThi](chỉ đọc); Mã phòng [MaPH](chỉ đọc); Số phút thi [SoPhutThi](chỉ đọc); Tên hình thức thi [TenHTThi](chỉ đọc); Tiết bắt đầu [TietThiBD](chỉ đọc); Số tiết thi [SoTietThi](chỉ đọc)
### VIEWINLICHTHILOP – In lich thi theo lop
- Lưới 1 «Danh sách lớp» (bảng LKQDKDThi); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã lớp [MaLop]; Tên lớp [TenLop]; Số sinh viên [SoSV]; Số môn thi [SoMonThi]
### ViewInPhieuNhapKhoTheoSoHD – Danh sách nhập kho để in phiếu nhập kho theo số hóa đơn
- Lưới 1 «Danh sách phiếu nhập kho» (bảng UNhapKhoMoi); tắt: Thêm, Sửa, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số phiếu nhập kho [SoHoaDon]; Học kỳ nhập kho [NHHK]; Mã nhà cung cấp [MaNhaCCHL]; Tên nhà cung cấp [TenNhaCCHL]; Tên kho [TenKho]; Ngày nhập thay đổi [NgayNhapKho]{ngày}
  - Cột ẩn: Loại nhập kho [LoaiNhapKho]{chọn}
  - Ô trên form sửa: #NgayNhapKho
### ViewInPhieuNhapKhoTheoSoPhieu – In phiếu nhập kho trả theo số phiếu
- Lưới 1 «Danh sách phiếu nhập kho theo số phiếu xuất» (bảng UNhapKhoTra); tắt: Thêm, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số phiếu nhập trả [SoPhieuNhapTra](chỉ đọc); Ngày nhập thay đổi [NgayNhapKho]{ngày}; Số đăng ký học liệu [SoDangKyHL]; Số phiếu xuất kho [SoPhieuXuatKho](chỉ đọc); Ngày trả [NgayTraHL]{ngày}; Họ tên người trả [HoTenNguoiTra]; Lý do trả học liệu [LyDoTraHL]
### ViewInPhieuXuatKho – In phiếu xuất kho theo số phiếu xuất
- Lưới 1 «In phiếu xuất kho theo số phiếu xuất» (bảng UXuatKho); tắt: Thêm, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số phiếu xuất kho [SoPhieuXuatKho]; Ngày xuất kho [NgayXuatKho]{ngày}; Ghi chú [GCXuatKho]
### VIEWINVOICE – Danh sách phiếu báo học phí
- Lưới 1 «Danh sách phiếu báo học phí» (bảng MINVOICE); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Loại thu [TenNhCT]; SoInvoice [SoInvoice]; Số tiền [PhaiThu]; Ngày tạo [NgayKhTao]; Mã đợt học [MaDotHc]
### ViewJDSDonViNgoai – Danh sách đơn vị ngoài
- Lưới 1 «Danh sách đơn vị ngoài» (bảng JDmDVNgoai); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã đơn vị ngoài [MaDVNgoai]; Tên đơn vị ngoài [TenDVNgoai]; Viết tắt đơn vị ngoài [VtDVNgoai]; Ghi chú đơn vị ngoài [GcDVNgoai]
  - Cột ẩn: ID đơn vị ngoài [IDDVNgoai]
### ViewJDSTaiSanThuocDonVi – Danh sách tài sản thuộc đơn vị
- Lưới 1 «Danh sách tài sản thuộc đơn vị»; tắt: Thêm, Sửa, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số thứ tự trong Report [STTReport]; Mã đơn vị [MaDVSD]; Đơn vị sử dụng [DonViSD]; Mã tài sản [MaTS]; Tên tài sản/ vật tư [TenTS]; Phân loại TS [PhanLoaiTS]{chọn}; Trạng thái tài sản [TrangThaiTS]{chọn}; Mã vạch [MaVachTS]; Số hiệu tài sản [SoHieuTS]; Qui cách tài sản [QuiCachTS]; Nước sản xuất [NuocSX]; Hãng sản xuất [HangSX]; Chất lượng tài sản [ChatLuongTS]; Ngày bắt đầu sử dụng [NgayBDSD]{ngày}; Ngày hết hạn sử dụng [NgayHHSD]{ngày}; Nguyên giá [NguyenGiaTS]; Giá trị còn lại [GiaTriConLai]; Hao mòn lũy kế [HaoMonLuyKe]
### VIEWKETQUAKTHK – Hiển thị kết quả khởi tạo học kỳ
- Lưới 1 «Danh sách kết quả khởi tạo học kỳ»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Thông tin [ThongTin]; Số mẫu tin [SoMauTin]
  - Cột ẩn: Cột điểm động [*DIEM]; *Loại điểm [*LoaiDiem]; Tuần [*TUAN]; Giá trị mặc nhiên (DVPC) [AQDefaultValDVPC]; Giá trị mặc nhiên (Trường) [AQDefaultValTruong]; Điểm B1 [B1]; Điểm B2 [B2]; Điểm C1 [C1]; Điểm C2 [C2]; Số sv chưa nhập điểm [ChuaNhap]; Số sv đã nhập điểm [DaNhap]; Ràng buộc xóa SS [DeleteRuleSS]; Điểm chữ [DiemChu]; Điểm khác [DiemKhac]; Ghi chú [GhiChu]; Hoãn thi [HoanThi]; Khóa chính SS [IsKhoaSS]; Điểm K1 [K1]; Điểm K2 [K2]; Điểm K3 [K3]; Điểm K4 [K4]; Độ dài DB SS [LenDBSS]; Lý do thất bại [LyDoError]; Mã field so sánh [MaFieldSS]; Mã file so sánh [MaFileSS]; Mã loại điểm [MaLoaiDiem]; Mặc định [MacDinh]; Điểm P1 [P1]; Điểm P2 [P2]; Điểm P3 [P3]; Điểm P4 [P4]; Điểm P5 [P5]; Điểm P6 [P6]; Điểm Q1 [Q1]; Điểm Q1 [Q2]; Điểm Q2 mới [Q3]; Điểm Q4 [Q4]; Điểm Q5 [Q5]; Điểm Q6 [Q6]; Số thứ tự trong Report [STTReport]; Số lần đăng ký [SoLDK]; Số lần đăng ký thất bại [SoLDKLoi]; Số lần đăng ký thành công [SoLDKTC]; Số môn học đăng ký [SoMHDK]; Số mẫu tin hk cũ [SoRecordHKCu]; Số mẫu tin hk mới [SoRecordHKMoi]; Số sinh viên [SoSV]; Kiểu field ss [SpecType0SS]; Điểm thi [T1]; Điểm T2 [T2]; Điểm T3 [T3]; Điểm tổng kết học phần [TK]; Điểm tổng kết kiểm tra [TKK]; Điểm tổng kết thi [TKT]; Thứ tự tuần [TTTuan]; Tuần 1 [TUAN1]; Tuần 3 [TUAN3]; Bảng phụ SS [TableCSS]; Bảng chính SS [TablePSS]; Tên loại điểm [TenLoaiDiem]; Tên tuần [TenTuan]; Tổ TH [ToTH]; Tổng cộng [TongCong]; Ràng buộc sửa SS [UpdateRuleSS]; Tên viết tắt [VTTuan]
### VIEWKETQUATINHHPTB – Danh sách kết quả tính học phí thất bại
- Lưới 1 «Danh sách sinh viên tính học phí thất bại»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên lớp [TenLop]; Số sinh viên [SoSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Lý do [LyDoLoi]
### VIEWKETQUATINHHPTC – Danh sách kết quả tính học phí thành công
- Lưới 1 «Danh sách sinh viên tính học phí thành công»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên lớp [TenLop]; Số sinh viên [SoSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]
### VIEWKETQUAXEPLICHTHI – Kêt quả xếp lịch thi
- Lưới 1 «Kết quả xếp lịch thi»; tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Kết quả xếp [KetQuaXep](chỉ đọc); Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm thi [NhomThi](chỉ đọc); Ngày thi [NgayThi]{ngày}; Tiết bắt đầu [TietThiBD]; Mã PH [MaPhHK]{nút …}; Tên phòng [TenPHHK]
  - Cột ẩn: Phòng học [IDPH]
### VIEWKETQUAXEPLICHTHINHIEUNHOM – Kết quả xếp lịch thi nhiều nhóm thi
- Lưới 1 «Kết quả xếp lịch thi»; tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Tổ thi [ToThi]; Nhóm thi [NhomThi]; Mã môn học [MaMH]; Tên môn học [TenMH]; Ngày thi [NgayThi]{ngày}; Tiết bắt đầu [TietThiBD]; Số tiết thi [SoTietThi]; Mã PH [MaPhHK]; Tên phòng [TenPHHK]
### VIEWKHOARE – Giao diện chọn khoa báo biểu
- Lưới 1 «Danh sách bậc hệ» (bảng KDMKHOI); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Mã đơn vị [MaDV]; Tên bậc hệ [TenBH]; Tên đơn vị [TenDV]; Số sinh viên [SoSV]
### VIEWKHOILOPTINHHP – Danh sách khối lớp
- Lưới 1 «Dah sách lớp tính học phí» (bảng SDMLOP); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Mã khối [MaKhoi]; Tên lớp [TenLop]; Số sinh viên [SoSV]; Tên khối [TenKhoi]; Mã học chế [MaHC]; Tên học chế [TenHC]
### VIEWKHOIPB – Giao diện chọn khối - phiên bản
- Lưới 1 «Danh mục khối» (bảng KCTDTCH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; Mã bậc hệ [MaBH]; Mã Ng/CNg [MaNgChng]; NHHK vào [NHHKVao]; NHHK ra [NHHKRa]; Mã PB [MaPB]
### VIEWKHOITAOHK – Load danh sách học ký đã khởi tạo
- Lưới 1 «Danh sách học kỳ đã khởi tạo»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Ngày bắt đầu [NgayBDHK]{ngày}; Tuần bắt đầu [TuanBDHKNam]; Số tuần học kỳ [SoTuanHK]
  - Cột ẩn: NHHK mặc định [DfNHHK]; Ghi chú [GCNHHK]; Không quản lý [HuyNHHK]; ID NHHK [IDNHHK]; Khởi tạo? [IsKhoiTao]; Mã năm học hk [MaNHHK]; Mã user [MaUser]; Ngày thêm [NgayThem]; Thứ tự [TTNHHK]; Tên NHHK [TenNHHK]; Tuần bắt đầu học kỳ [TuanBDHK]; Tên viết tắt [VTNHHK]
### ViewKhoiTS – Danh sách khối tuyển sinh
- Lưới 1 «Danh sách khối tuyển sinh» (bảng TDSKHOITS); tắt: Nạp lại, Đổi mã, Gộp mã
  - Cột: Điểm sàn [DiemSan]; Mã khối [MAKHOITS](chỉ đọc); Tên khối [TENKHOITS](chỉ đọc); Thứ tự [TTDSKHOITS]; Viết tắt [VTDSKHOITS]; Ghi chú [GCDSKHOITS]
### ViewKiemDinh – View kiểm định chất lượng
- Lưới 1 «Danh sách câu hỏi không đạt tiêu chuẩn để đo lường (không phân biệt giữa những nhóm trả lời, có thể loại bỏ)» (bảng YDMTCDG); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã tiêu chí đánh giá [MaTCDG]; Tên tiêu chí đánh giá [TenTCDG]
### ViewKQDG – View kết quả đánh giá
- Lưới 1 (bảng KDMMH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số thứ tự [Stt]; Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm/tổ [NhomTo]; Tổ TH [ToTH]; Mã giảng viên [MaNV]; Họ tên giảng viên [TenDayDuNV]; Điểm đã ĐG [DiemDG]
### ViewKQDKDTNH – View KQDK môn DTNH
- Lưới 1 «Danh sách môn học đã chọn»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMonDTNH]; Tên môn [TenMonDTNH]; Mã lớp [MaLopMonKhoa]
### VIEWKQIMPORTERR – Kết quả import thất bại
- Lưới 1 (bảng KToLop); tắt: Thêm, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Mã môn học [MaMH]; Tên lớp [TenLop]; Tên môn học [TenMH]; Số TC [SoTinChi]; Lý do thất bại [LyDoError]
### VIEWKQIMPORTSUCC – Kết quả import lớp thành công
- Lưới 1 (bảng KToLop); tắt: Thêm, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Mã môn học [MaMH]; Tên lớp [TenLop]; Tên môn học [TenMH]; Số TC [SoTinChi]
### ViewKTCKhoiMon_Khoi – Danh sách khối tín chỉ ĐKMH
- Lưới 1 «Danh sách khối tín chỉ ĐKMH» (bảng KTCKhoiMon); tắt: Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; Niên học học kỳ [NHHK]
  - Cột ẩn: Ghi chú dùng bên detailright [GhiChuView1]; Mã khối [IDKhoi]
  - Ô trên form sửa: #NHHK, #GhiChuView1, #IDKhoi
### ViewKTCKhoiMon_MH – Danh sách môn học tín chỉ ĐKMH
- Lưới 1 «Danh sách môn học tín chỉ ĐKMH» (bảng KTCKhoiMon); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); TC đạt Min [GCTCDat]; TC ĐK min [GHTCDK]; Niên học học kỳ [NHHK]
  - Cột ẩn: Mã khối [IDKhoi]; Môn học [IDMH]
### VIEWKTTPMH – Danh sách tiết thành phần môn học
- Lưới 1 «Danh sách tiết thành phần» (bảng KTietTPMH); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Loại thành phần [KyHieuTTP]{chọn}(chỉ đọc); Tổng số tiết/học kỳ [SoTietF]; Tổng số tiết/ học kỳ [SoTiet]{số}; Số TC TPMH [SoTCTPMH]; Từ học kỳ [TuNHHK]; Số SV/ nhóm tổ [SiSoMax]{số}; Thứ tự xếp TKB [TTXepTKB]; TC Phòng [IDTCPhong]
### VIEWKTTPMHCopy – Danh sách tiết thành phần môn học Update
- Lưới 1 «Danh sách môn học» (bảng KTietTPMH); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Loại thành phần [KyHieuTTP]{chọn}(chỉ đọc); Số tiết [SoTiet]{số}; Số sv tối đa [SiSoMax]{số}
### VIEWKTTPMHCopyCopy – Danh sách tiết thành phần môn học Update them vao
- Lưới 1 «Danh sách môn học» (bảng KTietTPMH); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Loại thành phần [KyHieuTTP]{chọn}(chỉ đọc); Số tiết [SoTiet]{số}; Số sv tối đa [SiSoMax]{số}
### ViewL404001 – Danh sách tổ thi
- Lưới 1 «Danh sách tổ thi» (bảng LToThi); tắt: Thêm, Xóa, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Nhóm thi [NhomThi](chỉ đọc); Tổ thi [ToThi](chỉ đọc); Sĩ số tổ thi [SiSoToThi](chỉ đọc); Số tiết thi [SoTietThi](chỉ đọc); Mã tính chất phòng [MaTCPhong](chỉ đọc); Ngày thi [NgayThi]{ngày}(chỉ đọc); Tiết bắt đầu [TietThiBD](chỉ đọc); Mã phòng [MaPH]{nút …}(chỉ đọc); Phòng đợi [MaPHDoi]{nút …}(chỉ đọc); SL coi thi [SLCanBoCoiThi](chỉ đọc); Mã viên chức [MaNVCap1]{nút …}; Tên đầy đủ CBCT 1 [TenDayDuNVCap1](chỉ đọc); Mã viên chức [MaNVCap2]{nút …}; Tên đầy đủ CBCT 2 [TenDayDuNVCap2](chỉ đọc); Mã viên chức [MaNVCap3]{nút …}; Tên đầy đủ CBCT 3 [TenDayDuNVCap3](chỉ đọc)
  - Cột ẩn: ID phòng thi [IDPThi]; Loại đối tượng [LoaiDTuong](chỉ đọc); Mã đối tượng [MaDoiTuong](chỉ đọc); Môn thi [MonThi](chỉ đọc); Ngày thi dự kiến [NgayThiDuKien]{ngày}(chỉ đọc); Sỉ số [SiSoDuKien](chỉ đọc); Tiết thi dự kiến [TietThiDuKien](chỉ đọc)
### ViewLDSVangThiTam – Chọn sinh viên vắng thi
- Lưới 1 «Chọn sinh viên vằng thi» (bảng LDSVangThiTam); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ và tên [TenDayDu](chỉ đọc); Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm thi [NhomThi](chỉ đọc); Tổ thi [ToThi](chỉ đọc); Ngày thi [NgayThi]{ngày}(chỉ đọc); Ghi chú [GCVangThiTam]
### VIEWLL1002001 – Sinh viên in giấy vào phòng thi
- Lưới 1 «Danh sách môn sinh viên thi trong ngày hiện tại»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã Môn [MaMH]; Tên môn [TenMH]; Nhóm thi [NhomThi]; Ngày thi [NgayThi]{ngày}; Giờ bắt đầu [GioBD]; Phòng thi [MaPH]
  - Cột ẩn: Sỉ số [SiSoDuKien]; Số tiết thi [SoTietThi]; Tên hình thức thi [TenHTThi]; Tiết bắt đầu [TietThiBD]; Tổ thi [ToThi]; Tổ thi con [ToThiCon]
### VIEWLOAIBG – Giao diện danh muc loại bận giờ
- Lưới 1 (bảng KDMLBG); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã loại bận giờ [MaLBG]; Tên loại bận giờ [TenLBG]; Tên viết tắt [VTLBG]; Ghi chú [GCLBG]
  - Ô trên form sửa: #MaLBG, #TenLBG, #VTLBG, #GCLBG
- Lưới 2 (bảng KDMLBGCT); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Thứ [Thu]{chọn}; Tiết BĐ [TietBD]; Số tiết [SoTiet]
### VIEWLOCKCTDT – Danh sách chương trình đào tạo
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; Niên khóa [NienKhoa]; Mã bậc hệ [MaBH]; Mã Ng/CNg [MaNgChng]; Khóa? [Col21]; User khóa [UserKhoaSo]
### VIEWLOCKDKMH – Khóa mở dữ liệu đăng ký môn học
- Lưới 1 «Danh sách kết quả đăng ký môn học» (bảng MKQDK); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Mã lớp [MaLop]; Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm/tổ [NhomTo]; Tổ TH [ToTH]; Mã khoa [MaKhoa]; Mã khoa quản lý bộ môn [MaKhoaBM]; Tên khoa [TenKhoa]; Tên khoa quản lý bộ môn [TenKhoaBM]; Ngày bắt đầu [NgayBD]{ngày}; Ngày kết thúc [NgayKT]{ngày}; Người khóa [USERLOCK]; Ngày khóa [NgayLock]{ngày}
### VIEWLOCNHOMTHITHOIKHOABIEU – Tổng hợp thời khóa biểu thi của nhóm sinh viên
- Lưới 1 «Danh sách tổng hợp thời khóa biểu thi của nhóm sinh viên»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm thi [NhomThi]
### VIEWLOPHK_TKBNGAY – Thông Tin Lớp Học Kỳ
- Lưới 1 «Nhập thông tin cho lớp xếp thời khóa biểu theo ngày» (bảng KLOPHK); tắt: Import, Xuất, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã lớp [MaLop](chỉ đọc); Tên lớp [TenLop](chỉ đọc); Mã khối [MaKhoi](chỉ đọc); Tên ng/chng [TenNgChng](chỉ đọc); Mã bậc hệ [MaBH](chỉ đọc); NHHK vào [NHHKVao](chỉ đọc); Sỉ số lớp [SiSoTKB](chỉ đọc); Ngày BĐ học [NGAYHOCBD]{ngày}; Công thức học [IDDNTGHOC]; Không xếp phòng TKB [IsKgXepPh]; Công thức thời gian thi [IDDNTGTHI]; Số tiết thi [SoTietThi]; Ngày bắt đầu thi [NgayThiBD]{ngày}; Ngày kết thúc thi [NgayThiKT]{ngày}
  - Cột ẩn: Ghi chú [GCLopHK](chỉ đọc); ID lớp học kỳ [IDLOPHK](chỉ đọc); Lớp sinh viên [IDLop](chỉ đọc); Xếp TKB theo ngày [ISTKBNGAY](chỉ đọc); Lớp TC [LopTkbTC](chỉ đọc); Niên học học kỳ [NHHK]{số}(chỉ đọc); Tên lớp HK [TenLopHK](chỉ đọc)
### VIEWLOPHUYDK – Giao diện lớp hủy đăng ký
- Lưới 1 «Danh sách lớp» (bảng SDMLOP); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop](chỉ đọc); Tên lớp [TenLop](chỉ đọc); Tên viết tắt [VTLop](chỉ đọc); Số sinh viên [SoSV](chỉ đọc)
### VIEWLOPHUYLOI – Giao diện hủy lớp
- Lưới 1 «Danh sách lớp không hợp lệ» (bảng SDMLOP); tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Tên lớp [TenLop]; Tên viết tắt [VTLop]; Lỗi ràng buộc [ERRORTYPE]{chọn}
  - Cột ẩn: Lý do [LyDoLoi]
### VIEWLOPRE – Giao diện chọn lớp cho báo biểu
- Lưới 1 «Danh sách khối» (bảng SDMLOP); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Tên lớp [TenLop]; Số sinh viên [SoSV]; Mã khối [MaKhoi]; Tên khối [TenKhoi]; Niên khóa [NienKhoa]; Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]; Mã đơn vị [MaDV]; Tên đơn vị [TenDV]; Mã Ng/CNg [MaNgChng]; Tên ng/chng [TenNgChng]
### ViewLopSVCoVan – Danh sách lớp gán cố vấn
- Lưới 1 «Danh sách lớp» (bảng SSVHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã lớp [MaLop]; Tên lớp [TenLop]; Số sinh viên [SoSV]
### VIEWMDGMGNHOM – View nhập đơn giá miễn giảm chung cho nhóm
- Lưới 1 «Đơn giá miễn giảm của nhóm» (bảng MDGMG); tắt: In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm/tổ [NhomTo]; Loại HP [LoaiDTHP]; Loai đơn giá học phí [LoaiDGHP]{chọn}; Đơn giá miễn giảm [DonGiaMG]
  - Cột ẩn: Đối tượng [IDDoiTuong]
  - Ô trên form sửa: #MaMH, #TenMH, #NhomTo, #DonGiaMG, #IDDoiTuong
### VIEWMDGNHMH – View nhập đơn giá đặc biệt cho nhóm tổ học
- Lưới 1 «Danh sách nhóm học có đơn giá đặc biệt» (bảng MDGNHMH); tắt: In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Nhóm/tổ [NhomTo]; Đơn giá ĐB [DonGiaDB]; Số SV nhóm [SoSVNhom]; Loại HP [LoaiDTHP]; Loai đơn giá học phí [LoaiDGHP]{chọn}
  - Cột ẩn: Ghi chú [GCDGNHMH]; Đối tượng [IDDoiTuong]
  - Ô trên form sửa: #MaMH, #TenMH, #NhomTo, #DonGiaDB, #SoSVNhom, #LoaiDTHP, #LoaiDGHP, #GCDGNHMH, #IDDoiTuong
### VIEWMDGNHMHTHEOMH – View nhập đơn giá đặc biệt cho môn học
- Lưới 1 «Danh sách môn học có đơn giá đặc biệt» (bảng MDGNHMH); tắt: In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Mã khối [MaKhoi]; Loai đơn giá học phí [LoaiDGHP]{chọn}; Đơn giá ĐB [DonGiaDB]; Loại HP [LoaiDTHP]
  - Cột ẩn: Ghi chú [GCDGNHMH]; Đối tượng [IDDoiTuong]; Mã khối [IDKhoi]
  - Ô trên form sửa: #TenMH, #LoaiDGHP, #DonGiaDB, #LoaiDTHP, #GCDGNHMH, #IDDoiTuong, #IDKhoi
### VIEWMGHPTHEONHOM – Miễn giảm học phí theo nhóm học
- Lưới 1 «Danh sách nhón học miễn giảm» (bảng MMGHPMH); tắt: In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm/tổ [NhomTo]; Phần trăm MG [PhanTramMG]; Ghi chú [GCMGHPMH]
  - Cột ẩn: Đối tượng [IDDoiTuong]
  - Ô trên form sửa: #MaMH, #TenMH, #NhomTo, #PhanTramMG, #GCMGHPMH, #IDDoiTuong
### ViewMHBH – Danh sách môn học bậc hệ
- Lưới 1 «Danh sách môn học bậc hệ» (bảng KBacHeMH); tắt: Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Tên bậc hệ [TenBH]; Mã hệ đào tạo [MaHe]; Tên hệ [TenHe]; Mã bậc hệ [MaBH]; Mã môn học [MaMH]; Tên môn học [TenMH]; Số tiết [SoTietF]{số}; Lý thuyêt [LT]; Thực hành [TH]; LMS [LMS]
  - Cột ẩn: Bậc hệ [IDBH]; ID hệ đào tạo [IDHe]; Môn học [IDMH]{nút …}; ST lý thuyết [SoTietMHLT]; ST thực hành [SoTietMHTH]; ST thực tập [SoTietMHTT]
  - Ô trên form sửa: #TenMH, #IDBH, #IDHe, #IDMH, #SoTietMHLT, #SoTietMHTH, #SoTietMHTT
### VIEWMHCTDTCHUAN – Mon Hoc cho chuong trinh dao tao chuan
- Lưới 1 «Danh sách môn học» (bảng KDMMH); tắt: Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Xét học kỳ thứ [HKThu]; Thứ tự [TTCTDTCH]; Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi]{số}(chỉ đọc); Tiết kế hoạch [TietKH]{số}; Môn bắt buộc [IsMHBB]; Môn tốt nghiệp? [IsMHTN]; Mã Ng/CNg [MaNgChng]{nút …}; Nhóm TC [NhomTC]; Nhánh TC [NhanhTC]
  - Nút btnDelete: "Xoa" (F1)
  - Nút btnAdd: "Add" (F2)
### VIEWMHCTDTCHUANCOPY – Mon Hoc cho chuong trinh dao tao chuan
- Lưới 1 «Danh sách môn học» (bảng KDMMH); tắt: Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Xét học kỳ thứ [HKThu]; Thứ tự [TTCTDTCH]; Mã môn học [MaMH]{nút …}; Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi]{số}(chỉ đọc); Khối KT [KhoiKT]{chọn}; Tính chất MH [LoaiMH]{chọn}; Đối tượng [DoiTuongSV]{chọn}; Tiết kế hoạch [TietKH]{số}; Môn bắt buộc [IsMHBB]; Môn tốt nghiệp? [IsMHTN]; Môn ưu tiên [MonUuTien]{chọn}; Không tính ĐTB [KhgTinhDTB]; Không in trên CTĐT [IsKhongInCTDT]; Mã Ng/CNg [MaNgChng]{nút …}; KgH.KgT [IsKgHKgT]; Nộp CC [IsNopCC]; Miễn VB2 [IsMienVB2]; Miễn LTCĐ [IsMienLTCD]; Miễn LTTC [IsMienLTTC]; Ghi chú [GcCTDTCH]; Nhóm TC [NhomTC]; Nhánh TC [NhanhTC]; Đạt tất cả [DatAll]; STCMin [STCMin]; STCMax [STCMax]; Xem chi tiết [XemChiTiet]; ST lý thuyết [SoTietMHLT]{số}; ST thực hành [SoTietMHTH]{số}; Số tiết LMS [SoTietMHLMS]{số}
  - Cột ẩn: Tiết kế hoạch [TietKHF]
### VIEWMHCTDTKH – Giao diện môn hoc chương trình đào tạo kế hoạch
- Lưới 1 «Danh sách môn học» (bảng KDMMH); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Thứ tự [TTCTDTKH]; Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi]{số}(chỉ đọc); Tiết kế hoạch [TietKH]{số}; Môn bắt buộc [IsMHBB]; Môn tốt nghiệp? [IsMHTN]; Mã Ng/CNg [MaNgChng]{nút …}; Nhóm TC [NhomTC]; Nhánh TC [NhanhTC]; Xem chi tiết [XemChiTiet]
  - Nút btnAdd: "them" (F1)
  - Nút btnDelete: "Xoa" (F2)
### VIEWMHCTDTKHCOPY – Giao diện môn hoc chương trình đào tạo kế hoạch
- Lưới 1 «Danh sách môn học» (bảng KDMMH); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Niên học học kỳ [NHHK]; Thứ tự [TTCTDTKH]; Mã môn học [MaMH]{nút …}; Tên môn học [TenMH](chỉ đọc); Ký hiệu tiền tố [KHTienTo]; Ký hiệu hậu tố [KHHauTo]; Lý thuyêt [LT](chỉ đọc); Thực hành [TH](chỉ đọc); Số TC [SoTinChi]{số}(chỉ đọc); Khối KT [KhoiKT]{chọn}; Số sv/nhóm [SiSoTKB]; Tính chất MH [LoaiMH]{chọn}; Đối tượng [DoiTuongSV]{chọn}; Môn ưu tiên [MonUuTien]{chọn}; Không in trên CTĐT [IsKhongInCTDT]; Tiết kế hoạch [TietKH]{số}; Môn bắt buộc [IsMHBB]; Môn tốt nghiệp? [IsMHTN]; Không tính ĐTB [KhgTinhDTB]; Mã Ng/CNg [MaNgChng]{nút …}; KgH.KgT [IsKgHKgT]; Nộp CC [IsNopCC]; Miễn VB2 [IsMienVB2]; Miễn LTCĐ [IsMienLTCD]; Miễn LTTC [IsMienLTTC]; Nhóm TC [NhomTC]; Nhánh TC [NhanhTC]; Ghi chú [GcCTDTTKH]; Xem chi tiết [XemChiTiet]; ST lý thuyết [SoTietMHLT]{số}; ST thực hành [SoTietMHTH]{số}; Số tiết LMS [SoTietMHLMS]{số}
  - Cột ẩn: Tiết kế hoạch [TietKHF]
### VIEWMHCTDTKHCOPYCopy – Giao diện môn hoc chương trình đào tạo kế hoạch
- Lưới 1 (bảng KDMMH); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Niên học học kỳ [NHHK]; Thứ tự [TTCTDTKH]; Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi]{số}(chỉ đọc); Tiết kế hoạch [TietKH]{số}; Môn tốt nghiệp? [IsMHTN]; Môn bắt buộc [IsMHBB]; Mã Ng/CNg [MaNgChng]{nút …}; Nhóm TC [NhomTC]; Nhánh TC [NhanhTC]
### VIEWMHDKTMP – Giao diện môn học đăng ký
- Lưới 1 «Danh sách sinh viên đăng ký» (bảng MKQDK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV](chỉ đọc); Họ và tên [TenDayDu](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Phái [Phai](chỉ đọc); Mã lớp [MaLop](chỉ đọc)
  - Cột ẩn: Bài tập [BT]; Tên lớp [TenLop](chỉ đọc)
  - Ô trên form sửa: #MaSV, #TenDayDu, #NgaySinhC, #Phai, #MaLop, #BT, #TenLop
### VIEWMHKCTDTTH – Giao diện môn học cho CTDT thực hiện
- Lưới 1 «Danh sách môn học» (bảng KDMMH); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Thứ tự [TTCTDTTH]; Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi]{số}(chỉ đọc); Tiết kế hoạch [TietKH]{số}; Môn tốt nghiệp? [IsMHTN]; Môn bắt buộc [IsMHBB]; Mã Ng/CNg [MaNgChng]{nút …}; Nhóm TC [NhomTC]; Nhánh TC [NhanhTC]; Xem chi tiết [XemChiTiet]
  - Nút btnAdd: "them" (F1)
  - Nút btnDelete: "xoa" (F2)
### VIEWMHKCTDTTHCOPY – Giao diện môn học cho CTDT thực hiện
- Lưới 1 «Danh sách môn học» (bảng KDMMH); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Học kỳ [NHHK]; Thứ tự [TTCTDTTH]; Mã môn học [MaMH]{nút …}; Tên môn học [TenMH](chỉ đọc); Ký hiệu tiền tố [KHTienTo]; Ký hiệu hậu tố [KHHauTo]; Lý thuyêt [LT](chỉ đọc); Thực hành [TH](chỉ đọc); Số TC [SoTinChi]{số}(chỉ đọc); Khối KT [KhoiKT]{chọn}; Số sv/nhóm [SiSoTKB]; Đối tượng [DoiTuongSV]{chọn}; Môn ưu tiên [MonUuTien]{chọn}; Không in trên CTĐT [IsKhongInCTDT]; Tính chất MH [LoaiMH]{chọn}; Môn tốt nghiệp? [IsMHTN]; Môn bắt buộc [IsMHBB]; Không tạo nhóm [IsKgTaoNhom]; Không tính ĐTB [KhgTinhDTB]; Mã Ng/CNg [MaNgChng]{nút …}; Nhóm TC [NhomTC]; Nhánh TC [NhanhTC]; Xem chi tiết [XemChiTiet]; Nộp CC [IsNopCC]; Miễn LTCĐ [IsMienLTCD]; Miễn VB2 [IsMienVB2]; KgH.KgT [IsKgHKgT]; Miễn LTTC [IsMienLTTC]; Ghi chú [GcCTDTTTH]; ST lý thuyết [SoTietMHLT]{số}; ST thực hành [SoTietMHTH]{số}; Số tiết LMS [SoTietMHLMS]{số}
  - Cột ẩn: Tiết kế hoạch [TietKH]{số}; Tiết kế hoạch [TietKHF]
### VIEWMHTC – Giao diện chọn môn học theo nhánh
- Lưới 1 «Danh sách môn học thuộc nhánh tự chọn» (bảng KDMMH); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Số tiết môn học [SoTietMH]
  - Nút btnAdd: "Thêm" (F2)
  - Nút btnDelete: "Xóa" (F1)
### VIEWMHTMP – Giao diện sửa môn học đăng ký
- Lưới 1 «Danh sách môn học đã đăng ký» (bảng MKQDK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Phân loại đk ngành [TCNganh]{chọn}; PL đăng ký MH [TChatDK]{chọn}
### VIEWMHTPMH – Giao diện danh mục môn hoc
- Lưới 1 (bảng KDMMHTT); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### ViewMHTT_LK – View mon hoc thay the lin ket
- Lưới 1 «Danh sách sinh viên có môn học thay thế»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; NHHK ĐK [NHHKDK]; Mã môn học [MaMHDK]; Mã MH thay thế cũ [MaMHTTCu]; Mã MH thay thế mới [MaMHTTMoi]; Mã môn học gốc cũ [MaMHSVCu]
  - Cột ẩn: Mã lớp [MaLop]
### VIEWMIENGIAMDIENCHINHSACH – Miễn giảm diện chính sách
- Lưới 1 «Danh sách miễn giảm chính sách» (bảng MMGCS); tắt: Thêm, Sửa, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã diện chính sách [MaDCS](chỉ đọc); Tên diện chính sách [TenDCS](chỉ đọc); Phần trăm miễn giảm [PhTramMGCS]{số}; Ghi chú [GcDCS](chỉ đọc)
  - Cột ẩn: Diện chính sách [IDDCS]
  - Nút btnImport: "Import" (F11)
  - Nút barBtnHuy: "Hủy" (F3)
  - Nút btnSave: "Lưu" (F9)
  - Nút barUctrlDongBo: "Đồng bộ từ học kỳ trước" (F2)
### ViewMoKhoaNhapDiemTP – Mở khóa nhập điểm thành phần
- Lưới 1 «Mở khóa nhập điểm thành phần» (bảng DMKDIEMTP); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Điểm B1 [B1]; Điểm B2 [B2]; Điểm B3 [B3]; Điểm B4 [B4]; Điểm K1 [K1]; Điểm K2 [K2]; Điểm K3 [K3]; Điểm K4 [K4]; Điểm C1 [C1]; Điểm C2 [C2]; Điểm C3 [C3]; Điểm C4 [C4]; Điểm C5 [C5]; Điểm C6 [C6]; Điểm thi [T1]; Điểm T2 [T2]; Mở khóa B1 [B1UNLOCK]; Mở khóa B2 [B2UNLOCK]; Mở khóa B3 [B3UNLOCK]; Mở khóa B4 [B4UNLOCK]; Mở khóa C1 [C1UNLOCK]; Mở khóa C2 [C2UNLOCK]; Mở khóa C3 [C3UNLOCK]; Mở khóa C4 [C4UNLOCK]; Mở khóa C5 [C5UNLOCK]; Mở khóa C6 [C6UNLOCK]; Mở khóa K1 [K1UNLOCK]; Mở khóa K2 [K2UNLOCK]; Mở khóa K3 [K3UNLOCK]; Mở khóa K4 [K4UNLOCK]; Mở khóa T1 [T1UNLOCK]; Mở khóa T2 [T2UNLOCK]; Mở khóa T3 [T3UNLOCK]
### VIEWMONHOCDIEUCHINH – Danh sách môn học điều chỉnh học phí
- Lưới 1 «Danh sách môn học điều chỉnh»; tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm/tổ [NhomTo](chỉ đọc); Tổ TH [ToTH](chỉ đọc); Số tiền thu MH [TienPTMH]; % môn học [PhTramPTMH]; Lý do thu MH [LyDoThuMH]
### VIEWMONHOCDIEUCHINHLEPHITHI – Danh sách môn học điều chỉnh lệ phí thi
- Lưới 1 «Danh sách môn học điều chỉnh»; tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm thi [NhomThi]; Tổ thi [ToThi]; Số tiền thu MH [TienPTMH]; % môn học [PhTramPTMH]; Lý do thu MH [LyDoThuMH]
### VIEWMONHOCDKCAITHIEN – Danh sách môn học đăng ký thi cải thiện
- Lưới 1 «Danh sách môn học đã đăng ký thi cải thiện» (bảng LSVCaiThien); tắt: Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Kỳ thi [KyHieuTP]; Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); NHHK học [NHHK]{số}(chỉ đọc); Điểm cũ [DiemCu](chỉ đọc); Ngày nhập [NgayNhapThiCT]{ngày}
  - Cột ẩn: Ghi chú [GCSVCaiThien]; Số TC [SoTinChi](chỉ đọc)
  - Nút btnDelete: "Xóa" (F3)
### VIEWMONHOCHOANTHI – Danh sách môn học hoãn thi
- Lưới 1 «Danh sách môn học sinh viên đã đăng ký hoãn thi» (bảng LSVHT); tắt: Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); NHHK học [NHHK](chỉ đọc); Ngày đk hoãn thi [NgayHT]{ngày}; Điểm B1 [B1](chỉ đọc); Điểm K1 [K1](chỉ đọc); Điểm B2 [B2](chỉ đọc); Điểm K2 [K2](chỉ đọc); Điểm C1 [C1](chỉ đọc); Điểm C2 [C2](chỉ đọc); Điểm thi [T1](chỉ đọc); Ghi chú [GCSVHT]
  - Cột ẩn: Kỳ thi [KyHieuTP]; Mã SV [MaSV]; Nhóm/tổ [NhomTo]; Số TC [SoTinChi](chỉ đọc); Tổ TH [ToTH]
### VIEWMONHOCHUYLOP – Giao diện môn học hủy lớp
- Lưới 1 (bảng KDMMH); tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Lỗi ràng buộc [ERRORTYPE]{chọn}
  - Cột ẩn: Lý do [LyDoLoi]
### ViewMonKhoa – View danh sách môn học trong khóa
- Lưới 1 «Danh sách môn học trong khóa»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMonDTNH]; Tên môn [TenMonDTNH]; Mã lớp [MaLopMonKhoa]; Số tiết môn học [SoTietMH]; Ngày khai giảng dự kiến [NgayKhaiGiangDK]
### VIEWMTCNHMH – View nhập tín chỉ đặc biệt cho nhóm tổ học
- Lưới 1 «Số tín chỉ học phí đặc biệt theo nhóm môn học» (bảng MTCHPNhomDB); tắt: Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Nhóm/tổ [NhomTo]; Số TC học phí [SoTCHP]
  - Cột ẩn: id tổ học [IDToHoc]
  - Ô trên form sửa: #TenMH, #NhomTo, #SoTCHP, #IDToHoc
### VIEWNCHAMCONGTHANG – Chấm công nhân viên theo tháng năm
- Lưới 1 «Chấm công nhân viên trong tháng» (bảng NChamCongThang); tắt: In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Năm [Nam]{số}; Tên đầy đủ [TenDayDuNV]; Tháng [Thang]; Nghỉ hộ sản [HoSan]; Học nước ngoài [HocTapNN]; Ngày nghỉ không lương [NgayPhepKgLg]{số}; Ngày nghỉ chăm vợ sinh [NghiChamVoSinh]; Số ngày làm việc [PTLuongHTNN]; Số ngày làm việc thai sản [SoNgayLamViecTS]
  - Cột ẩn: Mã viên chức [IDNV]; Phần trăm lương được hưởng khi học tập nước ngoài [PTLuongDuocHuongHTNN]; Tổng ngày nghỉ phép [TongNgayPhep]{số}
  - Ô trên form sửa: #TenDayDuNV, #HoSan, #HocTapNN, #NgayPhepKgLg, #NghiChamVoSinh, #PTLuongHTNN, #IDNV, #PTLuongDuocHuongHTNN
### ViewNganhTS – View Danh Sach Nganh Tuyen Sinh
- Lưới 1 (bảng TDSNGTS); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### ViewNhapCopyTC – View nhập copy tieu chuan danh sach
- Lưới 1 «Danh sách tiêu chuẩn» (bảng DDmTChuan); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã tiêu chuẩn [MaTChuan](chỉ đọc); Tên tiêu chuẩn [TenTChuan](chỉ đọc); Mã tiêu chuẩn mới [MaTChuanMoi]; Tên tiêu chuẩn mới [TenTChuanMoi]; Lý do [LyDoLoi](chỉ đọc)
### VIEWNHAPDONVINV – Nhập đơn vị cho nhân viên
- Lưới 1 (bảng NNVHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã viên chức [MaNV](chỉ đọc); Tên đầy đủ [TenDayDuNV](chỉ đọc); Phái [PhaiNV]{chọn}(chỉ đọc); Đơn vị [IDDV]
### ViewNhapNVTS – View nhap nguyen vong tuyen sinh
- Lưới 1 «Danh sách nguyện vọng» (bảng TDSTSNV); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã hồ sơ [MAHOSVNV]; Họ lót [HoLotSV]; Tên [TenSV]; Phái [Phai]; Mã khối [MAKHOITS]; Ngày sinh [NgaySinhC]; Mã ngành [MANGTS]; Mã bậc hệ [MaBH]; Mã đợt [MADOTNVTS]; Nguyện vọng [NGUYENVONG]{chọn}; Ngày nộp hồ sơ [NGAYNOPTS]{ngày}; Ngày rút hồ sơ [NGAYRUTTS]{ngày}; Điểm công [DIEMCONG]; Điểm tổng các môn [DIEMTCNV]; Điểm trừ [DIEMTRU]; Điểm cộng XT [DIEMCONGXT]; Điểm ưu tiên khu vực đố tượng [DIEMUUKVDT]; Điểm ưu tiên [DIEMUTKVDT]; Điểm cụm thi [DIEMCUMTHI]; NV ưu tiên [UUTIENNV]; NV tạo tự động [NVTAOTD]
  - Cột ẩn: Ghi chú cộng [GCCONG]; Ghi chú trừ [GCTRU]; Bậc hệ [IDBH]; Đợt XT [IDDOTNVTS]; Khối tuyển sinh [IDKHOITS]; Ngành tuyển sinh [IDNGTS]
  - Ô trên form sửa: #MAHOSVNV, #UUTIENNV, #IDBH, #IDDOTNVTS, #IDKHOITS, #IDNGTS
### ViewNhapNVTS_CT – View nhap nguyen vong tuyen sinh
- Lưới 1 «Danh sách nguyện vọng» (bảng TDSTSNV); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã hồ sơ [MAHOSVNV]; Họ lót [HoLotSV]; Tên [TenSV]; Phái [Phai]; Ngày sinh [NgaySinhC]; Mã khối [MAKHOITS]; Mã ngành [MANGTS]; Mã bậc hệ [MaBH]; Mã đợt [MADOTNVTS]; Nguyện vọng [NGUYENVONG]{chọn}; Ngày nộp hồ sơ [NGAYNOPTS]{ngày}; Ngày rút hồ sơ [NGAYRUTTS]{ngày}; Điểm công [DIEMCONG]; Điểm tổng các môn [DIEMTCNV]; Điểm trừ [DIEMTRU]; Điểm ưu tiên khu vực đố tượng [DIEMUUKVDT]; Điểm cộng XT [DIEMCONGXT]; Điểm ưu tiên [DIEMUTKVDT]; Điểm cụm thi [DIEMCUMTHI]; NV ưu tiên [UUTIENNV]; NV tạo tự động [NVTAOTD]
  - Cột ẩn: Ghi chú cộng [GCCONG]; Ghi chú trừ [GCTRU]; Bậc hệ [IDBH]; Đợt XT [IDDOTNVTS]; Khối tuyển sinh [IDKHOITS]; Ngành tuyển sinh [IDNGTS]
  - Ô trên form sửa: #MAHOSVNV, #NGUYENVONG, #NGAYNOPTS, #NGAYRUTTS, #DIEMTCNV, #DIEMCONGXT, #DIEMUTKVDT, #UUTIENNV, #IDBH, #IDDOTNVTS, #IDKHOITS, #IDNGTS
### ViewNhapPhanHieu – View danh sách nhập phân hiêu cho lớp
- Lưới 1 «Danh sách lớp» (bảng SDMLOP); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã lớp [MaLop](chỉ đọc); Tên lớp [TenLop](chỉ đọc); Phân hiệu [MaDB]{nút …}; Tên phân hiệu [TenDB](chỉ đọc)
### ViewNhapPHForNhomMon – Nhập phòng thi cho nhóm môn
- Lưới 1 «Nhập phòng thi cho nhóm môn» (bảng TGRPTS); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn [MAMONTS](chỉ đọc); Tên môn [TENMONTS](chỉ đọc); Ngày thi [NGAYTHITS]{ngày}(chỉ đọc); Giờ thi [GIOTHITS]{số}(chỉ đọc); Số phút thi [SOPHUTTS]{số}(chỉ đọc); Mã phòng thi [IDPHTHI]
### VIEWNHAPPTDOTTHI – Nhập phòng thi sử dụng cho đợt thi
- Lưới 1 «Danh sách đợt thi» (bảng LDotThi); tắt: Thêm, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đợt thi [MaDotThi]; Tên đợt thi [TenDotThi]
  - Cột ẩn: Ghi chú [GhiChu]; KH điểm TP [KyHieuTP]; Ngày bắt đầu [NgayThiBD]; Ngày kết thúc [NgayThiKT]
  - Ô trên form sửa: #MaDotThi, #TenDotThi, #GhiChu, #NgayThiBD, #NgayThiKT
  - Nút btnSave: "Lưu" (F6)
### ViewNhapThongTinMH – Dữ liệu xuất có chứa viết tắt môn học rỗng
- Lưới 1 «Dữ liệu xuất có chứa viết tắt môn học rỗng» (bảng KDMMH); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Tên viết tắt [VtMH]
### ViewNHHK – View hiển thị NHHK
- Lưới 1 «Danh sách năm học học kỳ» (bảng HDMNHHK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Tên NHHK [TenNHHK]
### ViewNHHKVao – View chon nam hoc hoc ky vao
- Lưới 1 «Danh sách năm học học kỳ vào»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Năm BĐ [NamBDVB]{số}; Học kỳ [HK]
### VIEWNHOMHOCKCTDTTH – Giao diện nhóm học cho CTDT thực hiện
- Lưới 1 «Danh sách nhóm học» (bảng KNHOMHOC); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Mã nhóm [MaNhomTC](chỉ đọc); Tên nhóm tự chọn [TenNhomTC](chỉ đọc); Số tín chỉ đạt [SoTCDat]{số}; Mã Ng/CNg [MaNgChng]{nút …}; Xem chi tiết [XemChiTiet]
  - Nút btnDelete: "xoa" (F2)
  - Nút btnAdd: "them" (F1)
### VIEWNHOMHOCKCTDTTHCOPY – Giao diện nhóm học cho CTDT thực hiện
- Lưới 1 «Danh sách nhóm tự chọn» (bảng KNHOMHOC); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Niên học học kỳ [NHHK]; Mã nhóm [MaNhomTC](chỉ đọc); Tên nhóm tự chọn [TenNhomTC](chỉ đọc); Số TC [SoTinChi]; Mã Ng/CNg [MaNgChng]{nút …}; Xem chi tiết [XemChiTiet]
### VIEWNHOMHOCKCTDTTHCOPYCopy – Giao diện nhóm học cho CTDT thực hiện
- Lưới 1 (bảng KNHOMHOC); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Niên học học kỳ [NHHK]; Mã nhóm [MaNhomTC](chỉ đọc); Tên nhóm tự chọn [TenNhomTC](chỉ đọc); Số TC [SoTinChi]; Mã Ng/CNg [MaNgChng]{nút …}
### VIEWNHOMMHKCTDTKH – Giao diện nhóm môn học CTDT kế hoạch
- Lưới 1 «Danh sách nhóm học» (bảng KDMNhomTC); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Mã nhóm [MaNhomTC](chỉ đọc); Tên nhóm tự chọn [TenNhomTC](chỉ đọc); Số tín chỉ đạt [SoTCDat]{số}; Mã Ng/CNg [MaNgChng]{nút …}; Xem chi tiết [XemChiTiet]
  - Nút btnAdd: "them" (F1)
  - Nút btnDelete: "Xoa" (F2)
### VIEWNHOMMHKCTDTKHCOPY – Giao diện nhóm môn học CTDT kế hoạch
- Lưới 1 «Danh sách nhóm tự chọn» (bảng KDMNhomTC); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Niên học học kỳ [NHHK]; Mã nhóm [MaNhomTC](chỉ đọc); Tên nhóm tự chọn [TenNhomTC](chỉ đọc); Số TC [SoTinChi]; Mã Ng/CNg [MaNgChng]{nút …}; Xem chi tiết [XemChiTiet]
### VIEWNHOMMHTC – Giao diện môn học tự chọn CTDT chuẩn
- Lưới 1 «Danh sách nhóm học» (bảng KDMNhomTC); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Mã nhóm [MaNhomTC](chỉ đọc); Tên nhóm tự chọn [TenNhomTC](chỉ đọc); Số tín chỉ đạt [SoTCDat]{số}; Mã Ng/CNg [MaNgChng]{nút …}; Xem chi tiết [XemChiTiet]
  - Nút btnAdd: "add" (F2)
  - Nút btnDelete: "Xoa" (F1)
### VIEWNHOMMHTCCOPY – Giao diện môn học tự chọn CTDT chuẩn
- Lưới 1 «Danh sách nhóm môn học» (bảng KDMNhomTC); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Xét học kỳ thứ [HKThu]; Mã nhóm [MaNhomTC](chỉ đọc); Tên nhóm tự chọn [TenNhomTC](chỉ đọc); Số TC [SoTinChi]; Mã Ng/CNg [MaNgChng]{nút …}; Xem chi tiết [XemChiTiet]
### VIEWNHOMMHTCCOPYCopy – Giao diện môn học tự chọn CTDT chuẩn
- Lưới 1 (bảng KDMNhomTC); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Xét học kỳ thứ [HKThu]; Mã nhóm [MaNhomTC](chỉ đọc); Tên nhóm tự chọn [TenNhomTC](chỉ đọc); Số TC [SoTinChi]; Mã Ng/CNg [MaNgChng]{nút …}
### VIEWNHOMTHI – Thống Kế Số Lượng Nhóm Thi
- Lưới 1 «Thống kê số lượng sinh viên theo nhóm thi» (bảng LKQDKDThi); tắt: Thêm, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm thi [NhomThi]; Số sinh viên [SoSV]
### VIEWNHOMTHI1 – Danh Sách Thí Sinh Theo Nhóm Thi
- Lưới 1 «Danh sách nhóm thi» (bảng LKQDKDThi); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm thi [NhomThi]; Số sinh viên [SoSV]
### VIEWNHOMTHIXEPLICHTHI – Danh sách nhóm thi xếp lịch thi
- Lưới 1 «Danh sách tổ thi (Lưu ý: chương trình chỉ xếp lịch thi cho tổ thi của nhóm có HÌNH THỨC THI và SỐ TIẾT THI)» (bảng LNhomThi); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Nhóm thi [NhomThi](chỉ đọc); KH ghép song song [GhepCaThi]; Tổ thi [ToThi](chỉ đọc); Số tổ thi [SiSoToThi]; Số tổ thi đã xếp [SiSoTuChon]; Mã hình thức thi [MaHTThi](chỉ đọc); Sỉ số [SiSoDuKien]; Số SV dự thi [SoDuThi]; Tổng SV dự thi ghép song song [TongSoSVXet](chỉ đọc); Nhóm thi [NhomThiDK](chỉ đọc); Ngày thi dự kiến [NgayThiDuKien]{ngày}(chỉ đọc); Tuần thi [TuanThi](chỉ đọc); Ngày thi đã xếp [NgayThi]{ngày}(chỉ đọc); Tiết thi đã xếp [TietThiBD](chỉ đọc); Phòng thi đã xếp [MaPH](chỉ đọc)
  - Cột ẩn: SL trạm thi [SLTramMax]; Số sinh viên [SoSV](chỉ đọc); Số tiết thi [SoTietThi]
### VIEWNKNHAPDIEM1SV – Nhật ký nhập điểm 1 sinh viên
- Lưới 1 «Nhật ký nhập»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Tên [TenSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Điểm B1 [B1]; Điểm B2 [B2]; Điểm K1 [K1]; Điểm K2 [K2]; Điểm K3 [K3]; Điểm K4 [K4]; Điểm thi [T1]; Điểm T2 [T2]; Điểm T3 [T3]
### VIEWNNGOAILE – Danh sách nhân viên ngoại lệ
- Lưới 1 «Danh sách ngoại lệ viên chức» (bảng NNgoaiLe); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Từ tháng [TuThang]{số}; Từ năm [TuNam]{số}; Đến tháng [DenThang]{số}; Đến năm [DenNam]{số}
  - Cột ẩn: Giá trị ngoại lệ [GiaTriNgoaiLe]; Mã viên chức [IDNV]; Lý do [LyDoNgoaiLe]; Tên đơn vị [TenDV]
  - Ô trên form sửa: #TenDayDuNV, #TuThang, #TuNam, #DenThang, #DenNam, #GiaTriNgoaiLe, #IDNV, #LyDoNgoaiLe, #TenDV
### VIEWNNGOAILE_PhanTruongLuongKy2 – Viên chức hưởng mức lương kỳ 2 ngoại lệ
- Lưới 1 «Danh sách viên chức ngoại lệ» (bảng NNgoaiLe); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Từ tháng [TuThang]{số}; Từ năm [TuNam]{số}; Đến tháng [DenThang]{số}; Đến năm [DenNam]{số}; Giá trị ngoại lệ [GiaTriNgoaiLe]
  - Cột ẩn: Mã viên chức [IDNV]; Lý do [LyDoNgoaiLe]; Tên đơn vị [TenDV]
  - Ô trên form sửa: #TenDayDuNV, #TuThang, #TuNam, #DenThang, #DenNam, #GiaTriNgoaiLe, #IDNV, #LyDoNgoaiLe, #TenDV
### VIEWNNGOAILEDV – Danh sách đơn vị ngoại lệ
- Lưới 1 «Danh sách đơn vị hưởng lương ngoại lệ» (bảng NNgoaiLeDV); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Từ năm [TuNam]{số}; Từ tháng [TuThang]{số}; Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Tên đơn vị [TenDV]; % lương theo đơn vị [PTLuongDV]{số}; Đến tháng [DenThang]{số}; Đến năm [DenNam]{số}; Có PC đắt đỏ [CoPCDatDo]; KPCD [KPCD]; BHXH [BHXH]; BHYT [BHYT]; BHTN [BHTN]
  - Cột ẩn: Đơn vị [IDDV]; Mã viên chức [IDNV]
  - Ô trên form sửa: #TuNam, #TuThang, #TenDayDuNV, #TenDV, #PTLuongDV, #DenThang, #DenNam, #CoPCDatDo, #KPCD, #BHXH, #BHYT, #BHTN, #IDDV, #IDNV
### VIEWNPCCBQL – Danh sách phụ cấp cán bộ quản lý
- Lưới 1 «Danh sách viên chức hưởng phụ cấp» (bảng NPCCBQL); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Tên đơn vị [TenDV]; Mức phụ cấp(%) [MucPCCBQL]{số}; Từ tháng [TuThang]{số}; Từ năm [TuNam]{số}
  - Cột ẩn: Mã viên chức [IDNV]; Chênh lệch [MucPCCBQLChLch]; Năm truy lãnh [NAMTL]; Số tháng truy lãnh [SoThangTL]; Tháng truy lãnh [ThangTL]; TL lương [TienTLLuong]
  - Ô trên form sửa: #TenDayDuNV, #TenDV, #MucPCCBQL, #TuThang, #TuNam, #IDNV
### VIEWNPCDATDOTHANG – Danh sách không hưởng phụ cấp đắt đỏ tháng
- Lưới 1 «Danh sách nhân viên không hưởng phụ cấp đắt đỏ trong tháng» (bảng NPCDatDoThang); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Năm [Nam]{số}; Tên đầy đủ [TenDayDuNV]; Tháng [Thang]; Lý do không hưởng [LyDoKgPCDatDo]
  - Cột ẩn: Mã viên chức [IDNV]
  - Ô trên form sửa: #TenDayDuNV, #LyDoKgPCDatDo, #IDNV
### VIEWNQTBIENDONGTS – Danh sách quá trình biến động thông số
- Lưới 1 «Quá trình biến động thông số» (bảng NQTBienDongTS); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Từ tháng [TuThang]{số}; Từ năm [TuNam]{số}; Mức biến động [MucBienDong]{số}
  - Cột ẩn: Làm tròn số tiền [LamTronTien]{chọn}; Loại biến động [LoaiBienDong]{chọn}; Mức biến động [MucBienDongInt]
  - Ô trên form sửa: #TuThang, #TuNam, #MucBienDong
### VIEWNQTBIENDONGTS_Check – Danh sách quá trình biến động thông số
- Lưới 1 «Chỉnh định học tập nước ngoài có đóng bảo hiểm y tế» (bảng NQTBienDongTS); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Từ tháng [TuThang]{số}; Từ năm [TuNam]{số}; Giá trị [LoaiNhap]{chọn}
  - Cột ẩn: Loại biến động [LoaiBienDong]{chọn}
  - Ô trên form sửa: #TuThang, #TuNam, #LoaiNhap
### VIEWNQTBIENDONGTS_Enum – Danh sách quá trình biến động thông số
- Lưới 1 «Quá trình biến động thông số» (bảng NQTBienDongTS); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Từ tháng [TuThang]{số}; Từ năm [TuNam]{số}; Giá trị [LamTronTien]{chọn}
  - Cột ẩn: Loại biến động [LoaiBienDong]{chọn}
  - Ô trên form sửa: #TuThang, #TuNam, #LamTronTien
### VIEWNQTBIENDONGTS_Int – Danh sách quá trình biến động thông số
- Lưới 1 (bảng NQTBienDongTS); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Từ tháng [TuThang]{số}; Từ năm [TuNam]{số}; Mức biến động [MucBienDongInt]{số}
  - Cột ẩn: Loại biến động [LoaiBienDong]{chọn}
  - Ô trên form sửa: #TuThang, #TuNam, #MucBienDongInt
### VIEWNQTBIENDONGTS_LuongCoBan – Danh sách quá trình biến động thông số
- Lưới 1 «biến động» (bảng NQTBienDongTS); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Từ tháng [TuThang]{số}; Từ năm [TuNam]{số}; Số tiền [MucBienDongInt]
  - Cột ẩn: Làm tròn số tiền [LamTronTien]{chọn}; Loại biến động [LoaiBienDong]{chọn}; Năm truy lãnh [NAMTL]{số}; Số tháng truy lãnh [SoThangTL]{số}; Tháng truy lãnh [ThangTL]{số}
  - Ô trên form sửa: #TuThang, #TuNam, #MucBienDongInt, #NAMTL, #SoThangTL, #ThangTL
### VIEWNQTBIENDONGTS_Ngay – Danh sách quá trình biến động thông số
- Lưới 1 (bảng NQTBienDongTS); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Từ tháng [TuThang]{số}; Từ năm [TuNam]{số}; Ngày [MucBienDongInt]{số}
  - Cột ẩn: Loại biến động [LoaiBienDong]{chọn}
  - Ô trên form sửa: #TuThang, #TuNam, #MucBienDongInt
### VIEWNQTBIENDONGTS_SoTien – Danh sách quá trình biến động thông số
- Lưới 1 (bảng NQTBienDongTS); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Từ tháng [TuThang]{số}; Từ năm [TuNam]{số}; Số tiền [MucBienDongInt]{số}
  - Cột ẩn: Làm tròn số tiền [LamTronTien]{chọn}; Loại biến động [LoaiBienDong]{chọn}
  - Ô trên form sửa: #TuThang, #TuNam, #MucBienDongInt
### VIEWNTSLGTHANG – Xem các thông số tính lương
- Lưới 1 «Danh sách thông số tính lương» (bảng NTSLgThang); tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Loại biến động [LoaiBienDong]{chọn}; Năm [Nam]{số}; Giá trị [MucBienDongString]; Tháng [Thang]{số}
  - Cột ẩn: Giá trị [MucBienDong]{số}
### ViewODiemDanhGia – Danh sách điểm đánh giá của hội đồng xét duyệt đề tài
- Lưới 1 «Điểm xét duyệt của danh sách viên chức trong hội đồng xét duyệt»; tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã viên chức [MaNV](chỉ đọc); Tên đầy đủ [TenDayDuNV](chỉ đọc); Chức vụ HDXD [IDCVHDXD](chỉ đọc); HS xét duyệt [HeSoXetDuyet](chỉ đọc); Hiện diện xét Duyệt [HienDienXetDuyet]{chọn}; Điểm trung bình [DiemTBXetDuyet]; Đạt xét duyệt [IsDatXetDuyet]; Xếp loại xét duyệt [IDXepLoaiXD]; Ý kiến xét duyệt [YKienXetDuyet]
  - Cột ẩn: Mã viên chức [IDNV]; Tên chức vụ [TenCVHDXD]; Tên chức vụ [TenChucVu]; Tên xếp loại [TenXEPLOAIXD]
### ViewODSChonNhaXB – Danh sách NXB
- Lưới 1 «Danh sách nhà xuất bản» (bảng UDMNhaXB); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã nhà xuất bản [MaNhaXB]; Tên nhà xuất bản [TenNhaXB]; Tên tiếng anh [TenNhaXBEg]; Địa chỉ [DiaChiNhaXB]; Email [EmailNhaXB]; Tên viết tắt [VtNhaXB]; Số điện thoại [TellNhaXB]; Số Fax [FaxNhaXB]
### ViewODSDeTaiNCKH – Danh sách tự điển đề tài nghiên cứu khoa học
- Lưới 1 «Danh sách đề tài»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đề tài [MaDeTaiNCKH]; Tên đề tài [TenDeTaiNCKH]; Chủ nhiệm đề tài [TenDayDuNV]; Tên cấp đề tài [TenCAPDETAI]
  - Cột ẩn: Đề tài [IDDeTaiNCKH]
### ViewOHDXetDuyet – Danh sách hội đồng xét duyệt đề tài
- Lưới 1 «Danh sách viên chức hội đồng xét duyệt»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Thứ tự [ThuTuNVXetDuyet]; Mã viên chức [MaNV](chỉ đọc); Tên đầy đủ [TenDayDuNV](chỉ đọc); Chức vụ hành chánh [IDChucVu]; Chức vụ hội đồng XD [IDCVHDXD]; ID xếp loại [IDXepLoaiXD]; Đơn vị [IDDV]; HS xét duyệt [HeSoXetDuyet]
  - Cột ẩn: ID hội đồng xét duyệt [IDHDXetDuyet]; Mã viên chức [IDNV]; ID xét duyệt [IDXetDuyetDeTai]; Tên chức vụ trong HDXD [TenCVHDXD]
### ViewONhapDiemDanhGiaDeTai – Danh sách đề tài nghiên cứu khoa học nhập điểm đánh giá
- Lưới 1 «Danh sách đề tài xét duyệt» (bảng OXetDuyetDeTai); tắt: Thêm, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đề tài [MaDeTaiNCKH]; Tên đề tài [TenDeTaiNCKH]; Học kỳ đăng ký [NHHK]; Mã chủ nhiệm đề tài [MaNV]; Tên chủ nhiệm đề tài [TenDayDuNV]; Số quyết định [SoQDXetDuyet]; Ngày quyết định [NgayQDXetDuyet]{ngày}; Ngày giờ xét duyệt [NgayGioXetDuyet]; Đạt xét duyệt [IsDatXetDuyet]; Điểm trung bình [DiemTBXetDuyet]; Tên xếp loại [TenXEPLOAIXD]; Ý kiến xét duyệt [YKienXetDuyet]
  - Cột ẩn: Địa điểm xét duyệt [DiaDiemXetDuyet]; Ghi chú 1 [GhiChu1]; Đề tài [IDDeTaiNCKH]; ID xếp loại [IDXepLoaiXD]; ID xét duyệt [IDXetDuyetDeTai]; Hình biên bản [ImageBienBan]
  - Ô trên form sửa: #IsDatXetDuyet, #DiemTBXetDuyet, #YKienXetDuyet, #GhiChu1, #IDXepLoaiXD
### ViewOXetDuyetDeTai – Danh sách đề tài nghiên cứu khoa học xét duyệt
- Lưới 1 «Danh sách đề tài đã xét duyệt» (bảng OXetDuyetDeTai); tắt: Xuất, Nạp lại, Đổi mã, Sửa trên lưới
  - Cột: Mã đề tài [MaDeTaiNCKH]; Tên đề tài [TenDeTaiNCKH]; Mã chủ nhiệm đề tài [MaNV]; Tên chủ nhiệm đề tài [TenDayDuNV]; Cấp đề tài [TenCAPDETAI]; Số quyết định [SoQDXetDuyet]; Ngày quyết định [NgayQDXetDuyet]{ngày}; Ngày giờ xét duyệt [NgayGioXetDuyet]; Địa điểm xét duyệt [DiaDiemXetDuyet]; Ghi chú 2 [GhiChu2]; Học kỳ đăng ký [NHHK]
  - Cột ẩn: Ghi chú 1 [GhiChu1]; Đề tài [IDDeTaiNCKH]; ID xét duyệt [IDXetDuyetDeTai]
  - Ô trên form sửa: #TenDeTaiNCKH, #TenDayDuNV, #TenCAPDETAI, #SoQDXetDuyet, #NgayQDXetDuyet, #NgayGioXetDuyet, #DiaDiemXetDuyet, #GhiChu2, #GhiChu1, #IDDeTaiNCKH
### VIEWPHAMVITOCHUCTHI – Phạm vi tổ chức thi
- Lưới 1 «Phạm vi tổ chức thi» (bảng LPVDotThi); tắt: Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Loại phân cấp [LoaiPC]; Mã loại phân cấp [MaLoaiPhanCap]; Tên loại phân cấp [TenLoaiPhanCap]
### VIEWPHANHEFILEFIELD – cay phan he
- Lưới 1 (bảng NDMDV); tắt: Thêm, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đơn vị [MaDV]; Tên đơn vị [TenDV]; Field Alias [FieldAlias]; Mã phân hệ [MaPhanHe]; Độ dài field [DoDaiField]; Tên viết tắt [VtField]; Phân loại field [plfield]{chọn}; Độ dài DB [LenDB]; Tên label [Tenlabel]; Tooltip [TextBoxToolTip]; Kiểu field DB [SpecType]{chọn}; ID Enum [IDEnum]; Điều kiện [DieuKien]; Map To [MapTo]
  - Cột ẩn: Đơn vị [IDDV]; Đơn vị cấp trên [IDDVP]
### VIEWPHANQUYENNHAPDIEM – Phân quyền nhập điểm cho người dùng
- Lưới 1 (bảng AQDMSetting); tắt: Thêm, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa bên phải
  - Cột: Tên [Name](chỉ đọc); Loại quyền [LoaiQuyen]{chọn}
  - Cột ẩn: Phân quyền [PhanQuyen]{chọn}
### VIEWPHANTOTHIBUOC1 – Phân tổ thi bước 1
- Lưới 1 «Danh sách nhóm thi chưa phân tổ. LƯU Ý: chương trình chỉ hiển thị các nhóm thi có hình thức thi» (bảng LHThiMH); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm thi [NhomThi](chỉ đọc); CBGD [MaNV](chỉ đọc); Sĩ số đã đăng ký [SiSoDDK](chỉ đọc); Sổ tổ thi tối đa/nhóm [SSoTDaNh](chỉ đọc); Sĩ số sv tối đa [SSoTDa](chỉ đọc)
  - Cột ẩn: Sỉ số nhóm thi [SSoTB](chỉ đọc); Số sinh viên tổ thi [SoSVToThi](chỉ đọc); Số tổ thi đã tạo [SoToThi](chỉ đọc)
### VIEWPHONGDOTTHI – Danh sách phòng đợt thi
- Lưới 1 «Danh sách phòng thi trong đợt» (bảng LPTDotThi); tắt: Sửa, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Mã phòng [MaPH](chỉ đọc); Tên phòng [TenPH](chỉ đọc); Sức chứa thi [SucChuaThi]{số}; Tính chất phòng [IDTCPhong]; SL trạm tối đa [SLTramMax]{số}
  - Cột ẩn: Sức chứa [SucChuaPH](chỉ đọc)
  - Nút btnDelete: "Xóa" (F4)
  - Nút btnAdd: "Thêm" (F3)
### VIEWPQADMIN – Giao diện phân quyền admin
- Lưới 1 «Danh sách phân hệ»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã phân hệ [MaPhanHe]; Tên phân hệ [TenPhanHe]; Ghi chú dùng bên detailright [GhiChuView1]
  - Ô trên form sửa: #MaPhanHe, #TenPhanHe, #GhiChuView1
### VIEWPQADMINDVPC – Giao diện phân quyền admin
- Lưới 1 «Danh sách đơn vị phân cấp» (bảng HUser); tắt: Thêm, Xóa, Import, Xuất, In, Đổi mã, Gộp mã
  - Cột: Mã đơn vị phân cấp [MaDVPC]; Tên đơn vị phân cấp [TenDVPC]; UserName [UserName]{nút …}; Tên đầy đủ [HotenTK](chỉ đọc)
  - Cột ẩn: Mã phân hệ [IDPhanHe]; ID user [IDUser]
### VIEWPTMH – Danh sách % môn học
- Lưới 1 «Danh sách phân tiết môn học trong tuần» (bảng KPTMH); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Loại thành phần [KyHieuTTP]{chọn}(chỉ đọc); Số thứ tự [Stt]; Số tiết [SoTiet]{số}; ID tính chất phong [IDCTPhong]; Mã môn học [MaMH]
### ViewQDChuyenChucNangDV – QĐ chuyển chức năng đơn vị
- Lưới 1 «Quyết định chuyển chức năng đơn vị» (bảng NQTQDDV); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đơn vị [IDDV]; Tên đơn vị [TenDV]; Số QĐ [SoQD]; Ngày quyết định [NgayQD]{ngày}; Ngày hiệu lực [NgayHLQDDV]{ngày}; Chức năng cũ [ChucNangCuDV]; Chức năng mới [ChucNangMoiDV]
  - Cột ẩn: Ghi chú [GCQTQDDV]; Hình QĐ đơn vị [ImageQD]
  - Ô trên form sửa: #IDDV, #SoQD, #NgayQD, #NgayHLQDDV, #ChucNangCuDV, #ChucNangMoiDV, #GCQTQDDV, #ImageQD
### ViewQDChuyenDVTrucThuoc – Quyết định chuyển đơn vị trực thuộc
- Lưới 1 «Quyết định chuyển đơn vị trực thuộc» (bảng NQTQDDV); tắt: Sửa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Đơn vị [IDDV]; Đơn vị trực thuộc cũ [IDDVPCu]; Đơn vị trực thuộc mới [IDDVPMoi]; Số QĐ [SoQD]; Ngày quyết định [NgayQD]{ngày}; Ngày hiệu lực [NgayHLQDDV]{ngày}
  - Cột ẩn: Hình QĐ đơn vị [ImageQD]
  - Ô trên form sửa: #IDDV, #IDDVPCu, #IDDVPMoi, #SoQD, #NgayQD, #NgayHLQDDV, #ImageQD
### ViewQDDoiLuanVan – Quyết định đổi luận văn/ người hướng dẫn
- Lưới 1 «Danh sách quyết định» (bảng DQDDoiLV); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Họ và tên [TenDayDu]; Tên đề tài cũ [TenDeTaiCu]; Tên đề tài mới [TenDeTaiMoi]; Ngày quyết định [NgayQDDoiLV]; Ngày ký quyết định [NgayKyQDDoiLV]; Loại quyết định [LoaiQDDoiLV]
  - Cột ẩn: Ghi chú 1 [GhiChu1]; ID quyết định thay đổi luận văn [IDQDDoiLV]; Sinh viên [IDSV]; Ảnh quyết định [ImageQDDoiLV]; Loại luận văn [LoaiLuanVan]; Ngày quyết định cũ [NgayQDCu]; Số quyết định cũ [SoQDCu]; Số QĐ đổi [SoQDDoiLV]
  - Ô trên form sửa: #TenDayDu, #TenDeTaiCu, #TenDeTaiMoi, #NgayQDDoiLV, #NgayKyQDDoiLV, #LoaiQDDoiLV, #GhiChu1, #IDSV, #ImageQDDoiLV, #SoQDDoiLV
### ViewQDDTDV – Quyết định đổi tên đơn vị
- Lưới 1 «Danh sách quyết định đổi tên đơn vị» (bảng NQTQDDV); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đơn vị [IDDV]; Tên Đơn Vị Cũ [TenDVCu]; Tên Đơn Vị Mới [TenDVMoi]; Số QĐ [SoQD]; Ngày quyết định [NgayQD]{ngày}; Ngày hiệu lực [NgayHLQDDV]{ngày}; Tên đơn vị hiện tại [TenDV]; Hình QĐ đơn vị [ImageQD]
  - Ô trên form sửa: #IDDV, #TenDVMoi, #SoQD, #NgayQD, #NgayHLQDDV, #ImageQD
### ViewQDGTDV – Quyết định giải thế đơn vị
- Lưới 1 «Danh sách quyết định giải thể đơn vị» (bảng NQTQDDV); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đơn vị [IDDV]; Tên đơn vị [TenDV]; Số QĐ [SoQD]; Ngày quyết định [NgayQD]{ngày}; Ngày giải thể [NgayGiaiTheDV]{ngày}; Ngày hiệu lực [NgayHLQDDV]{ngày}
  - Cột ẩn: Ghi chú [GCQTQDDV]; Ghi chú 1 [GhiChu1]; Hình QĐ đơn vị [ImageQD]; Lý do [LyDoQTQDDV]
  - Ô trên form sửa: #IDDV, #SoQD, #NgayQD, #NgayGiaiTheDV, #NgayHLQDDV, #GCQTQDDV, #GhiChu1, #ImageQD, #LyDoQTQDDV
### ViewQDSNDV – Quyết định sáp nhập đơn vị
- Lưới 1 «Danh sách quyết định sát nhập đơn vị» (bảng NQTQDDV); tắt: Sửa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Đơn vị cũ [IDDV]; Đơn vị sáp nhập đến [IDDVMoi]; Số QĐ [SoQD]; Ngày quyết định [NgayQD]{ngày}; Ngày hiệu lực [NgayHLQDDV]{ngày}
  - Cột ẩn: Hình QĐ đơn vị [ImageQD]
  - Ô trên form sửa: #IDDV, #IDDVMoi, #SoQD, #NgayQD, #NgayHLQDDV, #ImageQD
### ViewQuaTrinhTaiSan – Danh sách quá trình tài sản
- Lưới 1 «Danh sách quá trình tài sản»; tắt: Thêm, Sửa, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số thứ tự trong Report [STTReport]; Mã vạch [MaVachTS]; Mã tài sản/vật tư [MaTS]; Tên tài sản/ vật tư [TenTS]; Phân loại TS [PhanLoaiTS]{chọn}; Trạng thái tài sản [TrangThaiTS]{chọn}; Số biên bản [SoBB]; Ngày lập biên bản [NgayLapBB]{ngày}; Tên loại biên bản [TenLoaiBB]; Đơn bị giao [GhiChu1]; Đơn vị nhận [GhiChu2]; Địa điểm [DiaDiemBB]
### VIEWRESULTIMPORT – Kết quả import
- Lưới 1 «Danh sách các mẫu tin đã phân tích»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Nút btnDangKyMHSV: "Import đăng ký MH" (F2)
  - Nút btnImport: "import" (F24)
  - Nút btnXuLyImp: "Import" (F9)
  - Nút btnXuLyImp: "Import" (F8)
  - Nút btnImport: "Xử lý import lý lịch sv" (F4)
  - Nút btnXetHocVu: "Xét học vụ" (F9)
  - Nút btnImportSVHK: "Import SVHK" (F9)
  - Nút btnDangKyMH: "Import đăng ký MH" (F7)
  - Nút btnImportSVKK: "Thêm sinh viên QĐ" (FF)
  - Nút btnXuLyImp: "Import" (F25)
  - Nút btnXuLyImp: "Import" (F12)
  - Nút btnImport: "0" (f23)
  - Nút btnXuLyImp: "import" (f21)
  - Nút btnImportLopNhomHoc: "Import lớp nhóm học" (F10)
  - Nút btnImportTKB: "Import TKB" (F22)
  - Nút btnXuLyImp: "Import" (F11)
  - Nút btnImportSVQD: "Import SVQD" (F5)
  - Nút btnXuLyImp: "import" (F18)
  - Nút btnXuLyImp: "Import" (F3)
  - Nút Import: "Import" (F14)
  - Nút btnImportDiemTP: "Import điểm" (F6)
  - Nút btnImportDiemTP2: "Import điểm" (FFFFF)
  - Nút btnImportKhoi: "Import" (F1)
### VIEWSELECTUSER – Giao diện chọn user theo nhóm
- Lưới 1 «Danh sách người dùng» (bảng HUser); tắt: Thêm, Xóa, Import, Xuất, In, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: UserName [UserName]; Tên đầy đủ [HotenTK]; Ghi chú [GCTK]
### VIEWSHOWADDIN – Giao diện dùng để hiển thị addin
- Lưới 1 «Danh sách addin» (bảng AQDMAddin); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã addin [MaAddin]; Tên addin [TenAddin]
### ViewSLDGGV – View số lượng giảng viên được đánh giá
- Lưới 1 «Danh sách giảng viên được đánh giá»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã viên chức [MaNV](chỉ đọc); Họ lót [HoLotNV](chỉ đọc); Tên nhân viên [TenNV](chỉ đọc); SLSV được phép đánh giá [SLSVDuocPhep](chỉ đọc); SLSV được phép đã đánh giá [SLSVDaDG](chỉ đọc); Điểm TB [DiemsoDG_AVG]; Xem chi tiết [XemChiTiet]
### ViewSLDGGV_CT – View SLGV được đánh giá chi tiết
- Lưới 1 «Danh sách môn học»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Ký hiệu nhóm [NhomMH]; Tổ TH [ToTH1]; SLSV được phép đánh giá [SLSVDuocPhep]; SLSV được phép đã đánh giá [SLSVDaDG]; Điểm TB [DiemsoDG_AVG]
### ViewSLSVDG – View số lượng sinh viên đánh giá
- Lưới 1 «Danh sách sinh viên»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Mã lớp [MaLop]; Tên lớp [TenLop]; SL cần đánh giá [SLCanDG]; SL đã đánh giá [SLDaDG]
### VIEWSOSANHDKMHVADKTHI – Danh sách sự khác biệt giữa DKMH và đăng ký thi
- Lưới 1 «Danh sách môn học đã tạo nhóm thi trong học kỳ ( loại trừ môn nếu các  nhóm thi của môn được quy định không phân tổ thi)» (bảng KDMMH); tắt: Thêm, Sửa, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Nhóm thi [NhomThi]; Mã đợt thi [MaDotThi]
### VIEWSS_MUCDIEMRL – Giao diện mức điểm rèn luyện
- Lưới 1 «Mức điểm rèn luyện để xét học bổng»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum]; Giá trị cấp cha [*ColNameP]; Giá trị [GiaTriTreeDecimal]
### ViewSS_MUCHB – Nhập số suất cho mức học bổng
- Lưới 1 «Nhập số suất cho mức học bổng»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum]; Giá trị cấp cha [*ColNameP]; Giá trị [GiaTriTreeInt]
### ViewSVChuyenNGanh – View nhap chuyen nganh sinh vien
- Lưới 1 «Danh sách sinh viên» (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Hiện diện SV [HienDienSV]{chọn}(chỉ đọc); Mã lớp [MaLop]; ID ch/ngành SV [IDChNgSV]; Tên ng/chng [TenNgChng](chỉ đọc)
### ViewSVChuyenNGanhCopy – View nhap chuyen nganh sinh vien toan truong
- Lưới 1 «Danh sách sinh viên» (bảng SDMSV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Hiện diện [HienDienSV2]{chọn}(chỉ đọc); Mã lớp [MaLop](chỉ đọc); ID ch/ngành SV [IDChNgSV]; Tên ng/chng [TenNgChng](chỉ đọc)
### ViewSVDatRangBuocKhac – Danh sách sinh viên đạt ràng buộc khác
- Lưới 1 «Danh sách sinh viên đạt ràng buộc khác» (bảng MDatRBKhac); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã sinh viên [MaSV]; Họ và tên [TenDayDu]; Mã ràng buộc khác [MaRBKhac]; Tên ràng buộc khác [TenRBKhac]; Ghi chú [GcDatRBKhac]
  - Cột ẩn: Đơn vị phân cấp [IDDVPC]; IDDatRBKhac [IDDatRBKhac]; ID ràng buộc khác [IDRBKhac]; Sinh viên [IDSV]
  - Ô trên form sửa: #TenDayDu, #TenRBKhac, #GcDatRBKhac, #IDRBKhac, #IDSV
### VIEWSVHUYLOI – Giao diện sinh viên hủy lỗi
- Lưới 1 «Danh sách sinh viên không hợp lệ» (bảng SDMSV); tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Lỗi ràng buộc [ERRORTYPE]{chọn}
### VIEWSVMONHOCHUYLOI – Giao diện sinh viên môn học
- Lưới 1 «Dữ liệu lỗi»; tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Lỗi ràng buộc [ERRORTYPE]{chọn}
### VIEWSY_BoThongSoDG_GV – Đối tượng và bộ câu hỏi/bộ đáp án đánh giá giảng v
- Lưới 1 «Đối tượng và bộ câu hỏi/bộ đáp án đánh giá giảng viên»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Bộ tiêu chí ĐG GV [*BO_TCDG_GIANGVIEN]; Bộ đáp án ĐG GV [*BO_DAPAN_GIANGVIEN]
### VIEWSY_BoThongSoDG_TR – Đối tượng và bộ câu hỏi/bộ đáp án đánh giá trường
- Lưới 1 «Đối tượng và bộ câu hỏi/bộ đáp án đánh giá trường»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Tên Enum [ColNameEnum](chỉ đọc); Bộ tiêu chí ĐG trường [*BO_TCDG_TRUONG]; Bộ đáp án ĐG trường [*BO_DAPAN_TRUONG]
### VIEWTACHGHEPTOTHI – Tách ghép tổ thi xếp lịch thi
- Lưới 1 «Danh sách nhóm tổ thi» (bảng LToThi); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm thi [NhomThi](chỉ đọc); Tổ thi [ToThi](chỉ đọc); Sĩ số tổ thi [SiSoToThi](chỉ đọc); Số sinh viên [SoSV]; Ký hiệu tách [KyHieuTach]; Ký hiệu ghép [KyHieuGhep]
### VIEWTEMPLATE – Giao diện mẫu
- Lưới 1 «Danh sách lớp - sinh viên» (bảng AQDuLieuMau); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khoa [MaKhoa]; Tên khoa [TenKhoa]; Mã lớp [MaLop]; Tên lớp [TenLop]; Mã SV [MaSV]; Họ và tên [TenDayDu]; Phái [Phai]; Ngày sinh [NgaySinhC]; Ngày nhập học [NgayNhapHoc]; Số tiền [SoTien]
  - Cột ẩn: Ghi chú [GcSV]; Họ lót [HoLotSV]; ID Dữ liệu mẫu [IDDuLieuMau]; Tên [TenSV]
### VIEWTGKTCT – Thời gian không tổ chức thi
- Lưới 1 «Thời gian không tổ chức thi» (bảng LTGKgTCT); tắt: Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Ngày thi [NgayThi]; Số tiết thi [TietThi]; Số tiết thi [SoTietThi]
  - Nút btnAdd: "Thêm" (F4)
  - Nút btnDelete: "Xóa" (F3)
### VIEWTH209X – Giao diện chọn tổng hợp
- Lưới 1 «Danh sách bậc hệ» (bảng KDMKHOI); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Mã đơn vị [MaDV]; Tên bậc hệ [TenBH]; Tên đơn vị [TenDV]
### ViewThanhVienDGLVThS – Danh sách thành viên hội đồng
- Lưới 1 «Danh sách thành viên hội đồng»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã HĐBV luận văn [MaHDBVLV]; Tên HĐBV luận văn [TenHDBVLV]; Ngày bảo vệ [NgayBVLV]{ngày}; Số phút/1 đề tài [SoPhutBV1LV]{số}; Nhóm cán bộ [NhomBVLV]{chọn}; Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Cơ quan công tác [CoQuanCT]; Số TT [STTTrongDot]; Đợt BVLV [MaDotBVLV]
### VIEWTHONGBAODKMHLOI – Thông báo đăng ký môn học lỗi
- Lưới 1 «Danh sách môn học không thể đăng ký»; tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm/tổ [NhomTo]; Tổ TH [ToTH]; Lý do [LyDoLoi]{chọn}; Lỗi ràng buộc [ERRORTYPE]{chọn}
### VIEWTHONGKECHITIETMONTHI – Thống kê chi tiết theo môn thi
- Lưới 1 «Thống kê chi tiết theo môn thi»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã học phần [MaMH]; Tên học phần [TenMH]; Số lượng tổ thi [ToThi]; Tổng số thí sinh [SoThiSinh]
### VIEWTHONGKENHOMTHI – Giao diện nhóm thi trong trạm thi
- Lưới 1 «Danh sách nhóm thi» (bảng LKQDKDThi); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã môn học [MaMH]; Mã đơn vị [MaDV]; Tên môn học [TenMH]; Tên đơn vị [TenDV]; Mã lớp [MaLop]; Nhóm thi [NhomThi]; Tổ thi [ToThi]; Tổ thi con [ToThiCon]; Số sinh viên [SoSV]; Mã phòng [MaPH]; Ngày thi [NgayThi]{ngày}; Tiết bắt đầu [TietThiBD]; Số tiết thi [SoTietThi]; SL trạm thi [SLTramThi]
### VIEWTHONGKETOTHI – Giao diện thống kê số lượng theo tổ thi
- Lưới 1 «Danh sách môn thi» (bảng LKQDKDThi); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Mã lớp [MaLop]; Nhóm thi [NhomThi]; Tổ thi [ToThi]; Tổ thi con [ToThiCon]; Số sinh viên [SoSV]; Mã phòng [MaPH]; Ngày thi [NgayThi]{ngày}; Tiết bắt đầu [TietThiBD]; Số tiết thi [SoTietThi]
  - Cột ẩn: Mã đơn vị [MaDV]; Tên đơn vị [TenDV]
### ViewThongTinChiTietGiangDay – Thông tin giảng dạy chi tiết
- Lưới 1 «Xem thông tin chi tiết giảng dạy»; tắt: Thêm, Xóa, Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Từ tháng [TuThang]; Mã trường liên kết [MaDP]; Tên trường liên kết [TenDP]; Mã lớp [MaLop]; Khóa học [KhoaHocTC]; Mã Ng/CNg [MaNgChng]; Mã bậc hệ [MaBH]; Xét học kỳ thứ [HKThu]; Mã bộ môn [MaBOMON]; Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Số tiết môn học [SoTietMH]; Nhóm/tổ [NhomTo]; Tên công thức TG [TENDNTGHOC]; Số lượng buổi [STIETSBUOI]; Sĩ số đã đăng ký [SiSoDDK]; Thời gian học [ThoiGianHoc]; Buổi [KyHieuSo]; Mã viên chức [MaNV]; Họ lót [HoLotNV]; Tên nhân viên [TenNV]; Số điện thoại [DC_DT1LLNV]; Email [DC_Eml1LLNV]; Mã phân loại GV [MaPLGV]; Mã học hàm [MaHocHam]; Mã trình độ [MaBacNV]; Địa chỉ cơ sở [DiaChiCoSo]; Họ tên QLV [TenDayDuQLV]; Điện thoại QLV [SDTQLV]; Họ tên CTV [TenDayDuCTV]; Điện thoại CTV [SDTCTV]; Ngày bắt đầu [NgayBD]{ngày}; Tháng bắt đầu [THANGBD]; Đến ngày [NGAYCT]{ngày}; Đến tháng [THANGCT]; Ngày thi [NgayThi]{ngày}; Tháng thi [THANGTHI]; Tiết BĐ [TietBD]; Số tiết [SoTiet]; Mã phòng học [MaPHHoc]; Mã phòng thi [MAPHTHI]
  - Cột ẩn: Tên phòng thi [TENPHTHI]; Tên phòng học [TenPHHoc]
### VIEWTHONGTINHVIEW – Thông tin thuộc tính giao diện
- Lưới 1 «Chỉnh định danh mục view» (bảng HView); tắt: Thêm, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã view công bố [MaView1CB](chỉ đọc); Tên trường thông tin [TenView1](chỉ đọc); Nguồn [Source](chỉ đọc); Giữ giá trị cũ [IsCarryOn]; Thêm mới liên tục [IsNewLoop]; Có tính tổng [IsTotal]; Tính tổng theo nhóm [IsTotalGrp]
  - Nút barBtnHuy: "Huy" (F1)
### ViewThongTinSV – View thông tin sinh viên
- Lưới 1 «Thông tin sinh viên» (bảng SDMSV); tắt: Thêm, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã SV [MaSV](chỉ đọc); Họ lót [HoLotSV](chỉ đọc); Tên [TenSV](chỉ đọc); Phái [Phai]{chọn}(chỉ đọc); Ngày sinh [NgaySinhC](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Mã khoa [MaKhoa](chỉ đọc); Mã Ng/CNg [MaNgChng](chỉ đọc); Hiện diện SV [HienDienSV]{chọn}(chỉ đọc)
  - Cột ẩn: Ghi chú [GhiChu]
### VIEWTIETTHI – Nhap tiet thi
- Lưới 1 «Danh sách ngày thi & tiết không xếp lịch thi» (bảng LTGKgTCT); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Thoát
  - Cột: Ngày thi [NgayThi]{ngày}(chỉ đọc); Danh sách tiết không xếp lịch thi [ChuoiTT]; Chọn hết tiết/ngày [CheckChon]; T1 [TKBT1]; T2 [TKBT2]; T3 [TKBT3]; T4 [TKBT4]; T5 [TKBT5]; T6 [TKBT6]; T7 [TKBT7]; T8 [TKBT8]; T9 [TKBT9]; T10 [TKBT10]; T11 [TKBT11]; T12 [TKBT12]; T13 [TKBT13]; T14 [TKBT14]; T15 [TKBT15]; T16 [TKBT16]; T17 [TKBT17]; T18 [TKBT18]; T19 [TKBT19]; T20 [TKBT20]; T21 [TKBT21]; T22 [TKBT22]; T23 [TKBT23]; T24 [TKBT24]; T25 [TKBT25]; T26 [TKBT26]; T27 [TKBT27]; T28 [TKBT28]; T29 [TKBT29]; T30 [TKBT30]; T31 [TKBT31]; T32 [TKBT32]; T33 [TKBT33]; T34 [TKBT34]; T35 [TKBT35]; T36 [TKBT36]; T37 [TKBT37]; T38 [TKBT38]; T39 [TKBT39]; T40 [TKBT40]; T41 [TKBT41]; T42 [TKBT42]; T43 [TKBT43]; T44 [TKBT44]; T45 [TKBT45]; T46 [TKBT46]; T47 [TKBT47]; T48 [TKBT48]; T49 [TKBT49]; T50 [TKBT50]; T51 [TKBT51]; T52 [TKBT52]; T53 [TKBT53]; T54 [TKBT54]; Tuần 55 [TKBT55]; Tuần 56 [TKBT56]; Tuần 57 [TKBT57]; Tuần 58 [TKBT58]; Tuần 59 [TKBT59]; Tuần 60 [TKBT60]
### ViewTieuChuanCTDT – View tieu chuan chuong trinh dao tao
- Lưới 1 «Danh sách tiêu chuẩn CTĐT»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Xét học kỳ thứ [HKThu]; Mã tiêu chuẩn [MaTChuan]; Tên tiêu chuẩn [TenTChuan](chỉ đọc); Mã Ng/CNg [MaNgChng]{nút …}; TCTC [SoTinChi]
### ViewTieuChuanCTDTKH – View tieu chuan chuong trinh dao tao
- Lưới 1 «Danh sách tiêu chuẩn CTĐT»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Niên học học kỳ [NHHK]; Mã tiêu chuẩn [MaTChuan]; Tên tiêu chuẩn [TenTChuan](chỉ đọc); Mã Ng/CNg [MaNgChng]{nút …}; TCTC [SoTinChi]
### ViewTieuChuanCTDTTH – View tieu chuan chuong trinh dao tao
- Lưới 1 «Danh sách tiêu chuẩn CTĐT»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Niên học học kỳ [NHHK]; Mã tiêu chuẩn [MaTChuan]; Tên tiêu chuẩn [TenTChuan](chỉ đọc); Mã Ng/CNg [MaNgChng]{nút …}; TCTC [SoTinChi]
### VIEWTRUONGADDIN – Giao diện nhập addin cho trường
- Lưới 1 «Danh sách trường» (bảng AQAddinTruong); tắt: Thêm, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã trường tổ chức thi [MaTruong]; Tên trường [TenTruong]
  - Cột ẩn: Ghi chú [GhiChu]; Mã trường [IDTruong]; Kinh phí [KinhPhi]; Phiên bản [PhienBan]
  - Ô trên form sửa: #TenTruong, #GhiChu, #IDTruong, #KinhPhi, #PhienBan
### VIEWTRUYLANHPCDD – Danh sách truy lảnh phụ cấp đắt đỏ
- Lưới 1 «Danh sách nhân viên truy lãnh phụ cấp đắt đỏ trong tháng» (bảng NPCDatDoThang); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Năm [Nam]{số}; Tên đầy đủ [TenDayDuNV]; Tháng [Thang]; Số tiền truy lãnh [TLPCDatDo]{số}; Lý do [LyDoKgPCDatDo]
  - Cột ẩn: Mã viên chức [IDNV]
  - Ô trên form sửa: #TenDayDuNV, #TLPCDatDo, #LyDoKgPCDatDo, #IDNV
### VIEWTRUYTHUPCDD – Danh sách truy thu phụ cấp đắt đỏ
- Lưới 1 «Danh sách nhân viên truy thu phụ cấp đắt đỏ trong tháng» (bảng NPCDatDoThang); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Năm [Nam]{số}; Tên đầy đủ [TenDayDuNV]; Tháng [Thang]; Số tiền truy thu [TTPCDatDo]{số}; Lý do [LyDoKgPCDatDo]
  - Cột ẩn: Mã viên chức [IDNV]
  - Ô trên form sửa: #TenDayDuNV, #TTPCDatDo, #LyDoKgPCDatDo, #IDNV
### ViewTruyVetDTChi – Danh sách truy vết
- Lưới 1 «Danh sách truy vết»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Tác vụ [Action]{chọn}; Ngày thực hiện [CreatedTime]{ngày}; Tên máy tính [PCName]; Địa chỉ vật lý [PAddress]; Người thực hiện [CreatedBy]; Mã field [MaField]; Mã View [MAVIEW1]; Tên trường thông tin [TenView1]; Mã tiêu chí [MaBoTChi]; Giá trị (min) [GiaTriMin]; Giá trị cũ [OldValue]; Giá trị mới [NewValue]
### ViewTruyVetKCTDTKH – Danh sách truy vết
- Lưới 1 «Danh sách truy vết»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Tác vụ [Action]{chọn}; Ngày thực hiện [CreatedTime]{ngày}; Tên máy tính [PCName]; Địa chỉ vật lý [PAddress]; Người thực hiện [CreatedBy]; Mã field [MaField]; Mã View [MAVIEW1]; Tên trường thông tin [TenView1]; Niên học học kỳ [NHHK]; Mã môn học [MaMH]; Giá trị cũ [OldValue]; Giá trị mới [NewValue]
### ViewTruyVetSDMSV – Danh sách truy vết
- Lưới 1 «Danh sách truy vết»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Tác vụ [Action]{chọn}; Ngày thực hiện [CreatedTime]{ngày}; Tên máy tính [PCName]; Địa chỉ vật lý [PAddress]; Người thực hiện [CreatedBy]; Mã field [MaField]; Mã View [MAVIEW1]; Tên trường thông tin [TenView1]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Phái [Phai]; Nơi sinh [NoiSinh]; Email 1 [DC_EML1LLSV]; Điện thoại 1 [DC_DT1LLSV]; Giá trị cũ [OldValue]; Giá trị mới [NewValue]
### ViewUDatHL – Danh sách đặt học liệu yêu cầu
- Lưới 1 «Danh sách đặt học liệu» (bảng UDatHL); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số phiếu đặt [SoQDDHL](chỉ đọc); Mã viên chức [MaNV](chỉ đọc); Họ và tên viên chức [TenDayDuNV](chỉ đọc); Ngày đặt học liệu [NgayDatHL]{ngày}; Ghi chú [GCDatHL]; Ghi chú 1 [GhiChu1]
  - Cột ẩn: ID đặt học liệu [IDDatHL]; Viên chức gửi yêu cầu [IDNVDatHL]
  - Ô trên form sửa: #SoQDDHL, #NgayDatHL, #GCDatHL, #GhiChu1, #IDNVDatHL
### ViewUDMDatHocLieu – Danh sách danh mục đặt học liệu
- Lưới 1 «Danh sách học liệu»; tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Học kỳ đăng ký [NHHK]; Ngày nhập yêu cầu [NgayNhapYeuCauHL]{ngày}; Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Mã học liệu [MaHocLieu]; Tên học liệu [TenHocLieu]; Số trang [SOTRANG]; Số lượng [SoLuongYeuCauHL]; Trạng thái [TrangThaiYeuCauHL]{chọn}; Ghi chú [GCYeuCauHL]; Danh sách id yêu cầu chi tiết [DSIDYeuCauCT]
  - Cột ẩn: Mã học liệu [IDHocLieu]; ID Yêu cầu đặt học liệu từ phòng đào tạo [IDYeuCauHLCT]
### ViewUDMNhaCCHL – Danh sách nhà cung cấp học liệu
- Lưới 1 «Danh sách nhà cung cấp học liệu» (bảng UDMNhaCCHL); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã nhà cung cấp [MaNhaCCHL]; Tên nhà cung cấp [TenNhaCCHL]; Số điện thoại [TellNhaCCHL]
  - Cột ẩn: Nhà cung cấp [IDNhaCCHL]
### ViewUDongBangHocLieu – Danh sách đóng băng học liệu
- Lưới 1 «Hủy đóng băng học liệu» (bảng UDongBangHocLieu); tắt: Thêm, Xóa, Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Sửa bên phải
  - Cột: Mã học liệu [MaHocLieu]; Tên học liệu [TenHocLieu]; Số trang [SOTRANG]; Mã vị trí [MaViTriDatHocLieu]; Ngày đóng băng [NgayDongBang]{ngày}; Lý do đóng băng [LyDoDongBang]; Ngày hủy đóng băng [NgayHuyDongBang]{ngày}; Ghi chú hủy đóng băng [GCHuyDongBang]; Ghi chú 1 [GhiChu1]
  - Ô trên form sửa: #NgayHuyDongBang, #GCHuyDongBang, #GhiChu1
### ViewUDSDatHL – Danh sách đặt học liệu
- Lưới 1 «Danh sách phiếu đặt học liệu» (bảng UDatHL); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Sửa bên phải
  - Cột: Số quyết định đặt học liệu [SoQDDHL]; Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Ngày đặt học liệu [NgayDatHL]{ngày}; Ghi chú [GCDatHL]
  - Cột ẩn: ID đặt học liệu [IDDatHL]; Viên chức gửi yêu cầu [IDNVDatHL]
### ViewUDSDatHocLieu – Danh sách đặt học liệu chi tiết
- Lưới 1 «Danh sách học liệu đặt mua»; tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã học liệu [MaHocLieu](chỉ đọc); Tên học liệu [TenHocLieu](chỉ đọc); Số lượng [SoLuongYeuCauHL](chỉ đọc); Trạng thái đặt học liệu [TrangThaiDatHL]{chọn}(chỉ đọc); Ghi chú [GCDatHLCT]
  - Cột ẩn: ID đặt học liệu [IDDatHL]; ID đặt học liệu [IDDatHLCT]; Tên học liệu [IDHocLieu](chỉ đọc); ID Yêu cầu đặt học liệu từ phòng đào tạo [IDYeuCauHLCT]
### ViewUDSHocLieu – Danh sách yêu cầu học liệu chi tiết
- Lưới 1 «Danh sách học liệu yêu cầu»; tắt: Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã học liệu [MaHocLieu](chỉ đọc); Tên học liệu [TenHocLieu](chỉ đọc); Số lượng [SoLuongYeuCauHL]; Trạng thái [TrangThaiYeuCauHL]{chọn}(chỉ đọc); Ghi chú [GCYeuCauHLCT]
  - Cột ẩn: Id học liệu [IDHocLieu]; ID Yêu cầu đặt học liệu từ phòng đào tạo [IDYeuCauHLCT]
### ViewUDSHocLieuNhapKhoVatLy – Danh sách học liệu hiển thị để nhập kho vật lý
- Lưới 1 «Danh sách vị trí»; tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Tên kho [IDKho]; Tên phòng kho [IDPhongKho]; Dãy kệ [DayKe]; Kệ [Ke]; Tầng kệ [TangKe]; Vị trí [ViTri]; Vị trí phụ [ViTriPhu]; Mã vị trí [MaViTriDatHocLieu]
  - Cột ẩn: Mã học liệu [IDHocLieu]; ID vị trí đặt học liệu [IDViTriDatHocLieu]
### ViewUDSHuyPhieuNhapKho – Danh sách hủy phiếu nhập kho
- Lưới 1 «Danh sách hủy phiếu nhập kho» (bảng UHuyPhieuNhapKho); tắt: Import, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số phiếu nhập [SoHoaDon]; Tên nhà cung cấp [TenNhaCCHL]; Tên kho [TenKho]; Ngày nhập thay đổi [NgayNhapKho]{ngày}; Lý do hủy phiếu [LyDoHuyPhieuNhapKho]; Ngày hủy phiếu [NgayHuyPhieuNhapKho]{ngày}
  - Cột ẩn: ID hủy phiếu nhập kho [IDHuyPhieuNhapKho]; ID Nhập kho học liệu mua mới [IDNhapKhoMoi]; Loại nhập kho [LoaiNhapKho]{chọn}
  - Ô trên form sửa: #TenNhaCCHL, #TenKho, #NgayNhapKho, #LyDoHuyPhieuNhapKho, #NgayHuyPhieuNhapKho, #IDNhapKhoMoi
### ViewUDSNhanVien – Danh sách nhân viên yêu cầu học liệu
- Lưới 1 (bảng NDMNV); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]
  - Cột ẩn: Mã viên chức [IDNV]
### ViewUDSNhapKhoDatHLCT – Danh sách nhập kho từ yêu cầu đặt học liệu chi tiết
- Lưới 1 «Danh sách chi tiết nhập kho từ yêu cầu đặt học liệu»; tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã học liệu [MaHocLieu](chỉ đọc); Tên học liệu [TenHocLieu](chỉ đọc); SL yêu cầu [SoLuongYeuCauHL](chỉ đọc); Trạng thái đặt học liệu [TrangThaiDatHL]{chọn}(chỉ đọc); Mã vạch [MaVach]; SL nhập [SoLuongNhap]; Giá nhập [GiaNhap]; Thành tiền nhập [ThanhTien](chỉ đọc); Lần xuất bản [LanXB]; Năm xuất bản [NamXB]{số}; Ghi chú [GhiChu]
  - Cột ẩn: Tên học liệu [IDHocLieu]; ID Nhập kho học liệu mua mới [IDNhapKhoMoi]; ID Chi tiết vị trí học liệu nhập kho chi tiết [IDNhapKhoMoiCT]
### ViewUDSNhapKhoTuDoCT – Danh sách nhập kho tự do chi tiết
- Lưới 1 «Danh sách học liệu nhập kho» (bảng UNhapKhoMoiCT); tắt: Sửa, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã học liệu [MaHocLieu](chỉ đọc); Tên học liệu [TenHocLieu](chỉ đọc); Mã vạch [MaVach]; Số lượng nhập [SoLuongNhap]; Giá nhập [GiaNhap]; Thành tiền [ThanhTien](chỉ đọc); Năm xuất bản [NamXB]{số}; Lần xuất bản [LanXB]
  - Cột ẩn: Mã học liệu [IDHocLieu]; ID Nhập kho học liệu mua mới [IDNhapKhoMoi]; ID Chi tiết vị trí học liệu nhập kho chi tiết [IDNhapKhoMoiCT]
### ViewUDSNhapKhoVatLyCT – Danh sách nhập kho vật lý chi tiết
- Lưới 1 «Danh sách nhập kho vật lý chi tiết của học liệu» (bảng UViTriDatHocLieu); tắt: Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Tên kho [TenKho](chỉ đọc); Tên phòng kho [TenPhongKho](chỉ đọc); Mã vị trí [MaViTriDatHocLieu](chỉ đọc); Dãy kệ [DayKe](chỉ đọc); Kệ [Ke](chỉ đọc); Tầng kệ [TangKe](chỉ đọc); Ngăn [Ngan](chỉ đọc); Vị trí [ViTri](chỉ đọc); Vị trí phụ [ViTriPhu](chỉ đọc); Trạng thái [TrangThaiHocLieu]{chọn}(chỉ đọc)
  - Cột ẩn: ID Chi tiết vị trí học liệu nhập kho chi tiết [IDNhapKhoMoiCT](chỉ đọc); ID vị trí đặt học liệu [IDViTriDatHocLieu](chỉ đọc)
### ViewUDSPhieuNhapKhoDaKy – Danh sách phiếu nhập kho đã ký
- Lưới 1 «Danh sách phiếu nhập kho đã ký» (bảng UNhapKhoMoi); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số hóa đơn [SoHoaDon]; Niên học học kỳ [NHHK]; Ngày nhập thay đổi [NgayNhapKho]{ngày}; Tên nhà cung cấp [TenNhaCCHL]; Tên kho [TenKho]
  - Cột ẩn: ID Nhập kho học liệu mua mới [IDNhapKhoMoi]; Loại nhập kho [LoaiNhapKho]{chọn}
### ViewUDSYCHocLieuCT – Danh sách học liệu yêu cầu chi tiết
- Lưới 1; tắt: Thêm, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
### ViewUNhapKho – Danh sách nhập kho
- Lưới 1 «Danh sách nhập kho» (bảng UNhapKhoMoi); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số phiếu nhập [SoHoaDon]; Học kỳ đăng ký [NHHK]; Mã nhà cung cấp [MaNhaCCHL]; Tên nhà cung cấp [TenNhaCCHL]; Tên kho [TenKho]; Ngày nhập thay đổi [NgayNhapKho]{ngày}
  - Cột ẩn: ID Nhập kho học liệu mua mới [IDNhapKhoMoi]; Hóa đơn [ImageHoaDon]; Phiếu nhập kho [ImageNhapKho]; Loại nhập kho [LoaiNhapKho]{chọn}
  - Ô trên form sửa: #SoHoaDon, #NHHK, #TenNhaCCHL, #NgayNhapKho, #ImageHoaDon, #ImageNhapKho
### ViewUNhapKhoDatHL – Danh sách nhập kho từ yêu cầu đặt học liệu
- Lưới 1 «Danh sách nhập kho từ yêu cầu đặt học liệu» (bảng UNhapKhoMoi); tắt: Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số phiếu nhập [SoHoaDon]; Học kỳ nhập kho [NHHK]; Ngày nhập thay đổi [NgayNhapKho]{ngày}; Số QĐ đặt học liệu [SoQDDHL]; Ngày đặt học liệu [NgayDatHL]{ngày}; Mã nhà cung cấp [MaNhaCCHL]; Tên nhà cung cấp [TenNhaCCHL]; Tên kho [TenKho]
  - Cột ẩn: Ghi chú 1 [GhiChu1]; ID đặt học liệu [IDDatHL]; Mã kho [IDKho]; Nhà cung cấp [IDNhaCCHL]; ID Nhập kho học liệu mua mới [IDNhapKhoMoi]; Hóa đơn [ImageHoaDon]; Loại nhập kho [LoaiNhapKho]{chọn}
  - Ô trên form sửa: #SoHoaDon, #NHHK, #NgayNhapKho, #GhiChu1, #IDDatHL, #IDKho, #IDNhaCCHL, #ImageHoaDon
### ViewUNhapKhoTuDo – Danh sách nhập kho tự do
- Lưới 1 «Danh sách nhập kho tự do» (bảng UNhapKhoMoi); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số hóa đơn [SoHoaDon]; Học kỳ nhập kho [NHHK]; Mã nhà cung cấp [MaNhaCCHL]; Tên nhà cung cấp [TenNhaCCHL]; Tên kho [TenKho]; Ngày nhập thay đổi [NgayNhapKho]{ngày}; ID nhà xuất bản [IDNhaXB]; Mã nhà xuất bản [MaNhaXB]
  - Cột ẩn: Ghi chú 1 [GhiChu1]; Mã kho [IDKho]; Nhà cung cấp [IDNhaCCHL]; ID Nhập kho học liệu mua mới [IDNhapKhoMoi]; Hóa đơn [ImageHoaDon]; Loại nhập kho [LoaiNhapKho]{chọn}
  - Ô trên form sửa: #SoHoaDon, #NHHK, #NgayNhapKho, #GhiChu1, #IDKho, #IDNhaCCHL, #ImageHoaDon
### ViewUNhapKhoVatLy – Danh sách nhập kho vật lý
- Lưới 1 «Danh sách học liệu nhập kho vật lý»; tắt: Thêm, Xóa, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số phiếu nhập [SoHoaDon](chỉ đọc); Mã học liệu [MaHocLieu]; Tên học liệu [TenHocLieu]; Số lượng nhập kho [SoLuongNhap]; Số lượng đã nhập kho vật lý [SoLuongDaNhapKhoVatLy]; Ngày nhập thay đổi [NgayNhapKho]{ngày}; Học kỳ nhập kho [NHHK]; Tên nhà cung cấp [TenNhaCCHL]
  - Cột ẩn: Ghi chú 1 [GhiChu1]; Mã học liệu [IDHocLieu]; ID Nhập kho học liệu mua mới [IDNhapKhoMoi]
  - Ô trên form sửa: #GhiChu1
### ViewUSVXuatKhoTraCT – Danh sách chi tiết xuất học liệu cho sinh viên
- Lưới 1 «Danh sách học liệu đã xuất kho chưa trả» (bảng UXuatKhoCT); tắt: Thêm, Sửa, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Sửa bên phải, Thoát
  - Cột: Mã học liệu [MaHocLieu]; Tên học liệu [TenHocLieu]; Số trang [SOTRANG]; Ngày xuất kho [NgayXuatKho]{ngày}; Số phiếu xuất kho [SoPhieuXuatKho]; Ghi chú [GCXuatKho]; Mã vị trí [MaViTriDatHocLieu]; Trạng thái [TrangThaiHocLieu]{chọn}
### VIEWUU504003 – Danh sách vị trí đặt học liệu
- Lưới 1 «Danh sách vị trí đặt học liệu» (bảng UViTriDatHocLieu); tắt: Sửa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Trạng thái [TrangThaiHocLieu]{chọn}(chỉ đọc); Tên học liệu [IDHocLieu]; Mã kho [IDKho]; Mã phòng kho [IDPhongKho]; Mã học liệu [MaHocLieu]; Mã vị trí [MaViTriDatHocLieu]; Dãy kệ [DayKe](chỉ đọc); Kệ [Ke](chỉ đọc); Tầng kệ [TangKe](chỉ đọc); Ngăn [Ngan](chỉ đọc); Vị trí [ViTri](chỉ đọc); Vị trí phụ [ViTriPhu](chỉ đọc)
### ViewUYeuCauHL – Danh sách học liệu yêu cầu
- Lưới 1 «Danh sách yêu cầu học liệu từ các phòng ban» (bảng UYeuCauHL); tắt: Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Học kỳ đăng ký [NHHK]; Mã viên chức [MaNV](chỉ đọc); Tên đầy đủ [TenDayDuNV](chỉ đọc); Ngày nhập yêu cầu [NgayNhapYeuCauHL]{ngày}; Ghi chú [GCYeuCauHL]; Ghi chú 1 [GhiChu1]
  - Cột ẩn: Viên chức gửi yêu cầu [IDNVYeuCauHL]; ID Yêu cầu đặt học liệu từ phòng đào tạo [IDYeuCauHL]
  - Ô trên form sửa: #NHHK, #NgayNhapYeuCauHL, #GCYeuCauHL, #GhiChu1, #IDNVYeuCauHL
### ViewXemBacHeNganh – View xem danh sách bậc hệ ngành
- Lưới 1 «Danh sách bậc hệ ngành/chuyên ngành» (bảng KDMBHNgChNg); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Tên bậc hệ [TenBH]; Mã Ng/CNg [MaNgChng]; Tên ng/chng [TenNgChng]
### ViewXemCTDTChuan – Xem chương trình đào tạo chuẩn
- Lưới 1 «Danh sách môn học» (bảng KCTDTCH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã bậc hệ [MaBH]; Mã Ng/CNg [MaNgChng]; Xét học kỳ thứ [HKThu]; Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]
### ViewXemCTDTKH – View xem CTDT kế hoạch
- Lưới 1 «Danh sách môn học» (bảng KCTDTKH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; Niên học học kỳ [NHHK]; Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]
### ViewXemCTDTKHCopy – View xem CTDT thực hiện
- Lưới 1 «Danh sách môn học» (bảng KCTDTKH); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi]; Tên khối [TenKhoi]; Niên học học kỳ [NHHK]; Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]
### ViewXemDSDiemSinhVien – Xem danh sách điểm sinh viên
- Lưới 1 «Danh sách điểm sinh viên»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Niên học học kỳ [NHHK]; Mã SV [MaSV]; Họ và tên [TenDayDu]; Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm/tổ [NhomTo]; Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Mã bộ môn [MaBOMON]; Tên bộ môn [TenBOMON]; Mã khoa quản lý bộ môn [MaKhoaBM]; Tên khoa quản lý bộ môn [TenKhoaBM]; Mã lớp [MaLop]; Tên lớp [TenLop]; Điểm B1 [B1]; Điểm B2 [B2]; Điểm B3 [B3]; Điểm K1 [K1]; Điểm K2 [K2]; Điểm K3 [K3]; Điểm C1 [C1]; Điểm C2 [C2]; Điểm thi [T1]; Điểm T2 [T2]; Điểm T3 [T3]; Điểm số (Hệ 4) [DiemSoHP]; Hệ chữ [DiemChuHP]; Điểm TKHP [DiemHP]; Ghi chú điểm [GcNhapDiem]
### VIEWXEMDSLICHTHI – Xem danh sách lịch thi
- Lưới 1 «Danh sách lịch thi»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Nhóm thi [NhomThi]; Tổ thi [ToThi]; Mã phòng [MaPH]; Tên phòng [TenPHHK]; Dãy phòng [DayPHHK]; Ngày thi [NgayThi]{ngày}; Tiết bắt đầu [TietThiBD]; Số tiết thi [SoTietThi]
  - Cột ẩn: Mã môn học [MaMH]; Tên môn học [TenMH]
### VIEWXEMDSMONTHI – Xem danh sach mon thi
- Lưới 1 «Danh sách môn thi»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]
### VIEWXEMDSTHISINH – Xem danh sách thí sinh
- Lưới 1 «Danh sách thí sinh»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Tổ thi [ToThi]
### ViewXemKetQuaRutMonHoc – Xem kết quả Rút môn học
- Lưới 1 «Danh sách sinh viên Rút môn học»; tắt: Thêm, Xóa, Import, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã đơn vị [MaDV]; Tên đơn vị [TenDV]; Mã lớp [MaLop]; Tên lớp [TenLop]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm/tổ [NhomTo]; Số TC [SoTinChi]; Ngày thực hiện [CreatedTime]
### ViewXemMHTQ – View xem danh sách môn học TQ/HT/SH
- Lưới 1 «Danh sách Các MH Tiên Quyết, Song Hành, Học Trước» (bảng MMHTQ); tắt: Thêm, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã bậc hệ [MaBH]{nút …}; Mã Ng/CNg [MaNgChng]{nút …}; Mã khối [MaKhoi]{nút …}; Từ niên khóa [NienKhoaSV]; Mã môn đăng ký [MaMH]{nút …}; Tên môn đăng ký [TenMH](chỉ đọc); Mã môn yêu cầu [MaMHTQ]{nút …}; Tên môn yêu cầu [TenMHTQ](chỉ đọc); Loại tiên quyết [LoaiTQ]{chọn}; Điểm chữ tối thiểu [DiemChuMin]; Ký hiệu OR [NHOMDK]
  - Cột ẩn: Nhánh ĐK [NHANHDK]; Nhóm tiên quyết [NhomTQ]
### VIEWXEMNHANHMH – Giao diện xem nhánh theo nhóm môn học
- Lưới 1 «Danh sách nhánh môn học» (bảng KNhanhTC); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Ký hiệu nhánh [KHieuNhanh]; Mã môn học [MaMH]; Tên môn học [TenMH]; Tên nhánh tự chọn [TenNhanhTC]; Số TC [SoTinChi]
### VIEWXEMTIETTHI – Xem chon tiet thi
- Lưới 1 «Chọn tiết thi» (bảng LTGKgTCT); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Số tiết thi [TietThi]
### ViewXoaKQGV – View xóa kqdg giảng viên
- Lưới 1 «Danh sách kết quả đánh giá giảng viên» (bảng YKQDGGV); tắt: Thêm, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã viên chức [MaNV]; Tên đầy đủ [TenDayDuNV]; Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm/tổ [NhomTo]; Tổ TH [ToTH]
### ViewXoaKQTruong – View xóa kqdg giảng viên
- Lưới 1 «Danh sách kết quả đánh giá trường» (bảng YKQDGTR); tắt: Thêm, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Họ và tên [TenDayDu]
### VW_DIEMDATKHOI – Điểm đạt môn học theo khối
- Lưới 1 «Nhập điểm đạt theo khối»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã khối [MaKhoi](chỉ đọc); Tên khối [TenKhoi](chỉ đọc); Mã bậc hệ [MaBH](chỉ đọc); Tên bậc hệ [TenBH]; Mã Ng/CNg [MaNgChng](chỉ đọc); Tên ng/chng [TenNgChng](chỉ đọc); Điểm đạt MH [DiemDatMH]{số}
### VW_DSSV_KHONG_XET – Danh sách sinh viên không xét
- Lưới 1 «Danh sách sinh viên không xét»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ lót [HoLotSV]; Tên [TenSV]; Ngày sinh [NgaySinhC]; Hiện diện SV [HienDienSV]{chọn}; Mã lớp [MaLop]
### VW_DSSVVIPHAM_TINCHIMIEN – Danh sách bảo lưu sinh viên vi phạm tín chỉ tối đa
- Lưới 1 «Danh sách điểm bảo lưu sinh viên vi phạm tín chỉ tối đa» (bảng DDiemBL); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Trường cũ [TenTruongCu]; Mã SV [MaSV]; Họ lót [HoLotSV]; Không tính ĐTB [KhgTinhDTB]; Tên [TenSV]; Ghi chú [GCDiemBL]; Phái [Phai]{chọn}; Không in lên bảng điểm [IsKhgInBDBL]; Ngày sinh [NgaySinhC]; Tên MH chuyển đổi [TenMHCS]; Mã môn học [MaMH]; Ngày hết hạn [NgayHetHan]; Tên môn học [TenMH]; Số TC [SoTinChi]; Số QĐ [SoQDBL]; Số đếm bảo lưu [SoDemBL]; Ngày QĐ [NgayQDBL]; Niên học học kỳ [NHHK]; Điểm thành phần [DiemTP]; NHHK học phí [NHHKHP]; % học phí [PhTramThuHP]; Số tiền HPHK [SoTienHP]; Tổng TC CTĐT [TongTCCTDT]; Số tín chỉ miễn [TongTCMien]; Phần trăm miễn [PhanTramMiem]; Hệ đào tạo [HeDTVB]{chọn}
### VW_NHOMTHI_KHGIN_BGD – Nhóm thi không in bảng ghi điểm
- Lưới 1 «Danh sách nhóm thi» (bảng LNhomThi); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Nhóm/tổ [NhomTo](chỉ đọc); Sĩ số đã đăng ký [SiSoDDK](chỉ đọc); Điểm K1 [K1](chỉ đọc); Điểm C1 [C1](chỉ đọc); Nhóm thi [NhomThi](chỉ đọc); Không in BGĐ [IsKhgInBGD]; Tuần kết thúc [TuanktHoc](chỉ đọc); Ngày kết thúc [NgayKT]{ngày}(chỉ đọc); Ký hiệu ghép [GhepCaThi](chỉ đọc); KH điểm TP [KyHieuTP](chỉ đọc); Sĩ số tổ thi [SiSoToThi](chỉ đọc); Mã lớp [MaLop](chỉ đọc); Mã hình thức thi [MaHTThi](chỉ đọc)
### WCXTTWVNHP – Cấm sinh viên xem thông tin trên web vì nợ học phí
- Lưới 1 «Danh sách chức năng trên web không được xem vì nợ học phí» (bảng WCXTTWVNHP); tắt: Import, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Loại thông tin trên web [LOAITTWEB]{chọn}; Loại học phí xét nợ [LOAIHOCPHI]{chọn}; NHHK lấy học phí xét nợ [NHHKNOHOCPHI]
  - Ô trên form sửa: #LOAITTWEB, #LOAIHOCPHI, #NHHKNOHOCPHI
### WEB_DSTHONGBAO – Danh sách thông báo
- Lưới 1 (bảng WThongBaoND); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Chủ đề [ChuDeTB]; Ngày tạo [NgayTao]
### WEB_GetDmFormDG – Xem danh sách danh mục form đánh giá
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã form đánh giá [MaFormDG]; Tên form đánh giá [TenFormDG]
### WEB_GetFormDGHK – Xem danh sách form đánh giá học kỳ
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Đã trả lời [DaTraLoiDG]; Mã kỳ đánh giá [KEYGCDGHK]; Ngày bắt đầu đánh giá [NgayBDDG]; Ngày kết thúc đánh giá [NgayKTDG]; Mã ĐT được đánh giá [MaDTDG0]; Tên ĐT được đánh giá [TenDTDG0]; Mã môn học [MaMH]; Tên môn học [TenMH]; Tên CBGD [TenDayDuCBGD]
### WEB_LichSuDKMH – WEB_LichSuDKMH
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Nhóm/tổ [NhomTo]; Tổ TH [ToTH]; Ngày thêm [NgayThem]; Mã user [MaUser]
### WEB_XEMCOVAN – Xem danh sach sinh viên cố vấn
- Lưới 1; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Mã lớp [MaLop]; Điện thoại 1 [DC_DT1LLSV]; Email 1 [DC_EML1LLSV]; Số lượng [SoLuong]; Số TCTL [SoTCTL]; ĐTB4 [DTBTKH4]
### WEB_XemMHuyDK – Xem danh sách những môn bị hủy
- Lưới 1 «Xem danh sách những môn bị hủy»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMH]; Tên môn học [TenMH]; Số TC [SoTinChi]; Nhóm/tổ [NhomTo]; Lý do [LyDoHuyDK]
### WebDangKyNV – View đăng ký nguyện vọng
- Lưới 1 (bảng MNVDK); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã môn học [MaMHDK]; Nhóm học [NhomHoc]; Tên môn học [TenMH]; Ngày xét đăng ký [NgayXetDK]; Số TC [SoTinChi]
### WHoTroOnline – Admin lập danh sách thông tin bộ phận hổ trợ onlin
- Lưới 1 «Danh sách hỗ trợ online» (bảng WHoTroOnline); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Tên user/ bộ phận hổ trợ [TenHoTroOnline]; Loại hỗ trợ [TypeHoTroOnline]{chọn}; Nick user/ bộ phận hổ trợ [MaHoTroOnline]
  - Ô trên form sửa: #TenHoTroOnline, #TypeHoTroOnline, #MaHoTroOnline
### WSVKhongBaoNoHP – Danh sách không báo nợ học phí
- Lưới 1 «Danh sách không báo nợ học phí» (bảng WSVKhongBaoNoHP); tắt: Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Niên học học kỳ [NHHK]; Họ và tên [TenDayDu]; Ghi chú [GCKhongBaoNoHP]
  - Cột ẩn: Sinh viên [IDSV]
  - Ô trên form sửa: #NHHK, #TenDayDu, #GCKhongBaoNoHP, #IDSV
### WSVKhongXemTT – Cấm sinh viên xem thông tin trên web
- Lưới 1 «Cấm sinh viên xem thông tin trên web» (bảng WSVKhongXemTT); tắt: In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã SV [MaSV]; Họ và tên [TenDayDu]; Menu cấm xem [LoaiKhongXemWeb]{chọn}; Lý do cấm xem [GCKhongXemWeb]; Số tiền nợ [SoTienNo]; Số Tiền đã đóng [SoTienDaDong]
  - Cột ẩn: Sinh viên [IDSV]
  - Ô trên form sửa: #LoaiKhongXemWeb, #GCKhongXemWeb, #SoTienNo, #SoTienDaDong, #IDSV
### WWebLienKet – Admin lập danh sách website liên kết sẽ được hiển
- Lưới 1 «Danh sách web liên kết» (bảng WWebLienKet); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Tên web liên kết [TenWebLienKet]; URL web liên kết [URLWebLienKet]
  - Cột ẩn: Image web liên kết [ImageWebLienKet]
  - Ô trên form sửa: #TenWebLienKet, #URLWebLienKet, #ImageWebLienKet
### X02.03.01A – Chi tiết hóa đơn
- Lưới 1 «Báo giá chi tiết»; tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Mã dịch vụ [MaDICHVUKTX]; Tên dịch vụ [TenDICHVUKTX]; Tiền thu [SOTIENTHUKTXCT]; Từ ngày [TUNGAYPT]{ngày}; Đến ngày [DENNGAYPT]{ngày}
### XDMCONGKTX – Danh mục cổng ký túc xá
- Lưới 1 «Danh mục cổng ký túc xá» (bảng XDMCONGKTX); tắt: Sửa trên lưới
  - Cột: Mã cổng KTX [MaCONGKTX]; Tên cổng KTX [TenCONGKTX]; Ký túc xá [IDKTX]; Ghi chú [GcCONGKTX]
  - Cột ẩn: Mặc định [DfCONGKTX]; Không quản lý [HuyCONGKTX]; Tên tiếng anh [TenCONGKTXEg]; Viết tắt [VtCONGKTX]
  - Ô trên form sửa: #MaCONGKTX, #TenCONGKTX, #IDKTX, #GcCONGKTX
### XDMDICHVUKTX – Danh mục dịch vụ ký túc xá
- Lưới 1 «Danh sách dịch vụ ký túc xá» (bảng XDMDICHVUKTX); tắt: Sửa trên lưới
  - Cột: Cách tính phí [CACHTINHPHIDVKTX]{chọn}; Mã dịch vụ [MaDICHVUKTX]; Tên dịch vụ [TenDICHVUKTX]; Phân loại [PLDICHVU]{chọn}
  - Cột ẩn: Mặc định [DfDICHVUKTX]; Ghi chú [GcDICHVUKTX]; Không quản lý [HuyDICHVUKTX]; Thứ tự [TTDICHVUKTX]; Tên tiếng anh [TenDICHVUKTXEg]; Viết tắt [VtDICHVUKTX]
  - Ô trên form sửa: #CACHTINHPHIDVKTX, #MaDICHVUKTX, #TenDICHVUKTX, #PLDICHVU, #GcDICHVUKTX, #TenDICHVUKTXEg
### XDMDTLuuTru – Danh mục đối tượng lưu trú
- Lưới 1 «Danh sách đối tượng lưu trú ký túc xá» (bảng XDMDTLuuTru); tắt: Sửa trên lưới
  - Cột: Thứ tự [TTDTLuuTru]; Mã đối tượng [MaDTLuuTru]; Tên đối tượng [TenDTLuuTru]; Tăng % giá phòng [PTTangGia]; Tiền cọc HĐ [TienCocKTX]; Số giờ giữ chỗ [SoGioGiuCho]{số}; Đối tượng đăng ký [LOAIDTKTX]{chọn}; Mặc định [DfDTLuuTru]
  - Cột ẩn: Ghi chú [GcDTLuuTru]; Tên tiếng anh [TenDTLuuTruEg]
  - Ô trên form sửa: #MaDTLuuTru, #TenDTLuuTru, #PTTangGia, #TienCocKTX, #SoGioGiuCho, #LOAIDTKTX, #DfDTLuuTru, #GcDTLuuTru
### XDMLoaiCLgPhg – Danh mục loại chất lượng phòng
- Lưới 1 «Danh mục loại chất lượng phòng» (bảng XDMLoaiCLgPhg); tắt: Sửa trên lưới
  - Cột: Thứ tự [TTLoaiCLgPhg]; Mã loại [MaLoaiCLgPhg]; Tên loại [TenLoaiCLgPhg]; Ghi chú [GcLoaiCLgPhg]
  - Cột ẩn: Tên tiếng anh [TenLoaiCLgPhgEg]; Viết tắt chất lượng phòng [VtLoaiCLgPhg]
  - Ô trên form sửa: #MaLoaiCLgPhg, #TenLoaiCLgPhg, #GcLoaiCLgPhg
### XDMNHTHUKTX – Danh mục nhóm thu ký túc xá
- Lưới 1 «Danh mục nhóm thu» (bảng XDMNHTHUKTX); tắt: Xuất, Nạp lại, Sửa trên lưới, Thoát
  - Cột: Mã nhóm thu [MaNHThuKTX]; Tên nhóm thu [TenNHThuKTX]; Viết tắt [VtNHThuKTX]; Thứ tự [TTNHThuKTX]; Ghi chú [GcNHThuKTX]
  - Cột ẩn: Tên tiếng anh [TenNHThuKTXEg]
  - Ô trên form sửa: #MaNHThuKTX, #TenNHThuKTX, #TTNHThuKTX, #GcNHThuKTX
### XDMTCHIRLKTX – Danh mục tiêu chí rèn luyện ký túc xá
- Lưới 1 «Danh mục tiêu chí rèn luyện» (bảng XDMTCHIRLKTX); tắt: Nạp lại, Sửa trên lưới
  - Cột: Mã tiêu chí rèn luyện [MaTCHIRLKTX]; Tên tiêu chí [TenTCHIRLKTX]; Viết tắt tiêu chí rèn luyện [VtTCHIRLKTX]
  - Cột ẩn: Ghi chú tiêu chí rèn luyện [GcTCHIRLKTX]; Tên tiếng anh [TenTCHIRLKTXEg]
  - Ô trên form sửa: #MaTCHIRLKTX, #TenTCHIRLKTX, #VtTCHIRLKTX, #GcTCHIRLKTX, #TenTCHIRLKTXEg
### XDMTCRLKTX – Danh mục tiêu chuẩn rèn luyện ký túc xá
- Lưới 1 «Danh mục tiêu chuẩn rèn luyện» (bảng XDMTCRLKTX); tắt: Sửa trên lưới
  - Cột: Mã tiêu chuẩn rèn luyện [MaTCRLKTX]; Tên tiêu chuẩn [TenTCRLKTX]; Viết tắt tiêu chuẩn rèn luyện [VtTCRLKTX]; Mã xếp loại rèn luyện [MaXLRLKTX]
  - Cột ẩn: Ghi chú tiêu chuẩn rèn luyện [GcTCRLKTX]; Xếp loại RL KTX [IDXLRLKTX]; Tên tiếng anh [TenTCRLKTXEg]
  - Ô trên form sửa: #MaTCRLKTX, #TenTCRLKTX, #VtTCRLKTX, #GcTCRLKTX, #IDXLRLKTX, #TenTCRLKTXEg
### XDMTruongHoc – Danh mục trường học
- Lưới 1 «Danh mục trường» (bảng XDMTRUONGHOC); tắt: Sửa trên lưới
  - Cột: Mã trường học [MATRUONGHOC]; Tên trường học [TENTRUONGHOC]; Viết tắt trường học [VtTruongHoc]; Mặc định trường học [DfTruongHoc]
  - Cột ẩn: Ghi chú trường học [GcTruongHoc]; Tên tiếng anh [TENTRUONGHOCEG]
  - Ô trên form sửa: #MATRUONGHOC, #TENTRUONGHOC, #VtTruongHoc, #GcTruongHoc, #TENTRUONGHOCEG
### XDMTruongHoc_Chon – Danh mục trường học
- Lưới 1 «Danh sách trường» (bảng XDMTRUONGHOC); tắt: Xóa, Import, Nạp lại, Đổi mã, Sửa trên lưới
  - Cột: Mã trường học [MATRUONGHOC]; Tên trường học [TENTRUONGHOC]; Viết tắt trường học [VtTruongHoc]
  - Cột ẩn: Mặc định trường học [DfTruongHoc]; Ghi chú trường học [GcTruongHoc]; Tên tiếng anh [TENTRUONGHOCEG]
  - Ô trên form sửa: #MATRUONGHOC, #TENTRUONGHOC, #VtTruongHoc, #GcTruongHoc, #TENTRUONGHOCEG
### XDMXLRLXTX – Danh mục xếp loại rèn luyện ký túc xá
- Lưới 1 «Danh mục xếp loại rèn luyện» (bảng XDMXLRLXTX); tắt: Import, Xuất, Gộp mã, Sửa trên lưới, Thoát
  - Cột: Mã xếp loại rèn luyện [MaXLRLKTX]; Tên xếp loại rèn luyện [TenXLRLKTX]; Viết tắt xếp loại rèn luyện [VtXLRLKTX]
  - Cột ẩn: Ghi chú xếp loại rèn luyện [GcXLRLKTX]; Tên tiếng anh [TenXLRLKTXEg]
  - Ô trên form sửa: #MaXLRLKTX, #TenXLRLKTX, #VtXLRLKTX, #GcXLRLKTX, #TenXLRLKTXEg
- Lưới 2 «Danh mục chi tiết xếp loại rèn luyện» (bảng XXLRLKTXCT); tắt: Import, Xuất, In, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Thứ tự [TTXLRLKTXCT]{số}; Ký hiệu rèn luyện [KyHieuXLRLKTX]; Ngưởng điểm min [DiemMinXLKTX]{số}
  - Cột ẩn: Ghi chú xử lý [HThucXuLyXLKTX]; Kết quả xếp loại [KQXLRLKTX]
  - Ô trên form sửa: #TTXLRLKTXCT, #KyHieuXLRLKTX, #DiemMinXLKTX, #HThucXuLyXLKTX, #KQXLRLKTX
### XemDKTN – Điều Kiện Tốt Nghiệp
- Lưới 1 «Danh sách điều kiện xét tốt nghiệp»; tắt: Thêm, Xóa, Xuất, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Thứ tự [TTDKXetTN]; Mã Điều kiện xét tốt nghiệp [MaDKXetTN]; Tên Điều kiện xét tốt nghiệp [TenDKXetTN]; Đã có [GhiChu3]
### XIMPORT_CHISO_DV_PHONG – Import chỉ số dịch vụ phòng ký túc xá
- Lưới 1 (bảng XCHISO); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Dịch vụ [IDDICHVUKTX]; Phòng [IDPHGKTX]; Chỉ số mới [ChiSoMoi]
  - Ô trên form sửa: #IDDICHVUKTX, #IDPHGKTX, #ChiSoMoi
### XNHTCHIRLKTX – Danh mục nhóm tiêu chí rèn luyện KTX
- Lưới 1 «Danh mục tiêu chí rèn luyện» (bảng XTChiRLKTX); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Thứ tự [TTTCHIRLKTX]{số}; Ký hiệu [KyHieuTChiRLKTX]; Tên tiêu chí [TenTCHIRLKTX]; Điểm tối thiểu [DiemMinRLKTX]{số}; Điểm tối đa [DiemMaxRLKTX]{số}
  - Ô trên form sửa: #TTTCHIRLKTX, #KyHieuTChiRLKTX, #TenTCHIRLKTX, #DiemMinRLKTX, #DiemMaxRLKTX
- Lưới 2 «Danh mục nhóm tiêu chí rèn luyện» (bảng XNhTChiRLKTX); tắt: Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã, Sửa trên lưới
  - Cột: Tiêu chuẩn rèn luyện [IDTCRLKTX]; Thứ tự [TTNhTChiRLKTX]{số}; Ký hiệu nhóm [KyHieuNhTCRLKTX]; Tên nhóm [TenNhTChiRLKTX]; Điểm tối đa [DiemMaxRLKTX]{số}
  - Ô trên form sửa: #IDTCRLKTX, #TTNhTChiRLKTX, #KyHieuNhTCRLKTX, #TenNhTChiRLKTX, #DiemMaxRLKTX
### YDMDAPANDG – Danh mục bộ đáp án đánh giá
- Lưới 1 «Đáp án đánh giá» (bảng YDAPANDGCT); tắt: In, Nạp lại, Sửa trên lưới
  - Cột: Tên đáp án đánh giá chi tiết [TenDapAnDGCT]; Tên viết tắt [VtDapAnDGCT]; Điểm số [DiemDapAn]; Trọng số đáp áp [TrongSoDA]; Thứ tự đánh giá chi tiết [TtDapAnDGCT]
  - Cột ẩn: Ghi chú [GcDapAnDGCT]; Tên tiếng anh [TenDapAnDGCTEg]
  - Ô trên form sửa: #TenDapAnDGCT, #VtDapAnDGCT, #DiemDapAn, #TrongSoDA, #TtDapAnDGCT, #GcDapAnDGCT, #TenDapAnDGCTEg
- Lưới 2 «Danh mục bộ đáp án đánh giá» (bảng YDMDAPANDG); tắt: In, Sửa trên lưới, Thoát
  - Cột: Mã bộ đáp án đánh giá [MaDapAnDG]; Tên bộ đáp án đánh giá [TenDapAnDG]; Tên tiếng anh [TenDapAnDGEg]; Phân loại bộ tiêu chí đánh giá [PhanLoaiTCDG]{chọn}; Thứ tự [TtDapAnDG]; Ghi chú [GcDapAnDG]
  - Ô trên form sửa: #MaDapAnDG, #TenDapAnDG, #TenDapAnDGEg, #GcDapAnDG
### ZCauHoi – Danh sách câu hỏi
- Lưới 1 «Danh sách câu hỏi» (bảng ZCauHoi); tắt: Import, Nạp lại, Đổi mã, Sửa trên lưới
  - Cột: Mã form đánh giá [MaFormDG]; Thứ tự câu hỏi [TTCauHoi]; Nội dung nhóm câu hỏi [NoiDungNhomCauHoi]; Nội dung câu hỏi [NoiDungCauHoi]; Tên tiếng anh [NoiDungCauHoiEg]; Nội dung thống kê [NoiDungThongKe]; Kiểu trả lời [KieuTraLoi]{chọn}; Có ý kiến khác [IsYKienKhac]; Thứ tự ghi trên form [TTCHForm]; Loại thống kê đánh giá [LoaiTKDG]{chọn}; Có gán giá trị từ hệ thống [IsGanTTHT]; Bắt buộc trả lời [IsBatBuocTraLoi]
  - Cột ẩn: Ghi chú [GCCauHoi]; Ghi chú 1 [GhiChu1]; Hệ số điểm [HeSoDiem]; ID enum đánh giá [IDEnumDG]; ID Form đánh gía [IDFormDG]; ID nhóm câu hỏi [IDNhomCauHoi]; In đậm [IsBold]; In nghiêng [IsItalic]; Gạch dưới [IsUnderline]
  - Ô trên form sửa: #TTCauHoi, #NoiDungCauHoi, #NoiDungCauHoiEg, #NoiDungThongKe, #KieuTraLoi, #IsYKienKhac, #TTCHForm, #LoaiTKDG, #IsGanTTHT, #IsBatBuocTraLoi, #GCCauHoi, #GhiChu1, #HeSoDiem, #IDEnumDG, #IDNhomCauHoi, #IsBold, #IsItalic, #IsUnderline
### ZNhomCauHoi – Nhóm câu hỏi
- Lưới 1 «Nhóm câu hỏi» (bảng ZNhomCauHoi); tắt: Nạp lại, Sửa trên lưới
  - Cột: Thứ tự ghi trên form [TTNCHForm]; Mã nhóm câu hỏi [MaNhomCauHoi]; Nội dung nhóm câu hỏi [NoiDungNhomCauHoi]; Nội dung tiếng anh [NoiDungNhomCauHoiEg]
  - Cột ẩn: ID nhóm câu hỏi cha [IDNhomCauHoiP]; In đậm [IsBold]; In nghiêng [IsItalic]; Gạch dưới [IsUnderline]; Kiểu kiểm tra [KieuKiemTra]
  - Ô trên form sửa: #TTNCHForm, #MaNhomCauHoi, #NoiDungNhomCauHoi, #NoiDungNhomCauHoiEg, #IDNhomCauHoiP, #IsBold, #IsItalic, #IsUnderline, #KieuKiemTra
### ZVIEWDSMHDanhGia – Danh sách môn học đánh giá
- Lưới 1 «Danh sách môn học đánh giá» (bảng ZDSDTDG0); tắt: Thêm, Xóa, Import, Xuất, In, Nạp lại, Đổi mã, Gộp mã
  - Cột: Mã môn học [MaMH](chỉ đọc); Tên môn học [TenMH](chỉ đọc); Số TC [SoTinChi](chỉ đọc); Nhóm/tổ [NhomTo](chỉ đọc); Tổ TH [ToTH](chỉ đọc); Mã viên chức [MaNV](chỉ đọc); Tên đầy đủ [TenDayDuNV](chỉ đọc); Mã đơn vị [MaDV](chỉ đọc); Đơn vị thống kê [IDDVTKKS]; Không thống kê [IsKhongTKKS]
