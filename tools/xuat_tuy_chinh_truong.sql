-- Xuất phần TRƯỜNG tự chỉnh giao diện Edusoft (bảng H… trong CSDL trường) – CHỈ ĐỌC, không có dữ liệu sinh viên/nhân viên.
-- Bỏ cột MaUser/NgayThem. Chạy (PowerShell, trong thư mục repo):
--   sqlcmd -S GIAMINH-PC -E -d Edusoft.HVNG -i tools\xuat_tuy_chinh_truong.sql -o tuy-chinh-truong.txt -u -s "|" -W
-- rồi gửi file tuy-chinh-truong.txt cho Claude. Mỗi bảng bắt đầu bằng dòng ##BANG=<tên>.
SET NOCOUNT ON;

SELECT '##BANG=HMenuCustom' AS x;
SELECT IDMenuCustom, IDChucNang, IDChucNangP, IDChucNangBF, LoaiCustom, kieudtbf, kieudt, kieudtp, HideWeb, IDDVPC,
       REPLACE(REPLACE(TenChucNang, CHAR(13), ' '), CHAR(10), ' ') AS TenChucNang
FROM dbo.HMenuCustom;

SELECT '##BANG=HValSetV' AS x;
SELECT v.IDValSetV, v.IDView, v.IDFieldView, v.CapUser, v1.Index1, v1.Index2,
       REPLACE(REPLACE(LEFT(v1.GiaTri, 200), CHAR(13), ' '), CHAR(10), ' ') AS GiaTri
FROM dbo.HValSetV v JOIN dbo.HValSetV1 v1 ON v1.IDValSetV = v.IDValSetV;

SELECT '##BANG=HFieldView2' AS x;
SELECT IDFieldView, IDSubView, UserLevel, IsGroup, TabOrder, IsLock FROM dbo.HFieldView2;

SELECT '##BANG=HFieldEdit' AS x;
SELECT IDFieldView, IDSubView, UserLevel, TabForm, RowIndex, ColIndex, MergeRow, MergeCol, ShowLine,
       REPLACE(REPLACE(LineText, CHAR(13), ' '), CHAR(10), ' ') AS LineText
FROM dbo.HFieldEdit;

SELECT '##BANG=HOrderView' AS x;
SELECT IDFieldView, IDSubView, UserLevel, OrderIndex, IsDesc FROM dbo.HOrderView;

SELECT '##BANG=HViewSpliter' AS x;
SELECT IDView1, STTSpliter, UserLevel, IDView FROM dbo.HViewSpliter;

SELECT '##BANG=HTabView' AS x;
SELECT IDView, TabNo, UserLevel, REPLACE(REPLACE(TabDesc, CHAR(13), ' '), CHAR(10), ' ') AS TabDesc, ColumnNo FROM dbo.HTabView;

SELECT '##BANG=HValSetField' AS x;
SELECT f.IDField, f.CapUser, f1.Index1, f1.Index2, f1.LoaiSetting,
       REPLACE(REPLACE(LEFT(f1.GiaTri, 200), CHAR(13), ' '), CHAR(10), ' ') AS GiaTri
FROM dbo.HValSetField f JOIN dbo.HValSetField1 f1 ON f1.IDValSetField = f.IDValSetField;
