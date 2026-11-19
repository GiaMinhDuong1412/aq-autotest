"""python tools/kb_lien_ket.py kb  – DỰNG LẦN ĐẦU (bootstrap) – sau đó ghi chú Obsidian là nguồn, sửa trong Obsidian; script này GHI ĐÈ kb/Phan-he, kb/Du-lieu, kb/00 Bản đồ phân hệ.md (mất phần người test sửa tay: chạy rồi so git diff). Dựng KB liên kết phân hệ: Du-lieu/ (dữ liệu chảy giữa phân hệ) + Phan-he/ (nhận từ / đưa sang / sửa ở đây kiểm lại) + bản đồ."""
import json, os, re, sys
KB = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CATALOG = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, 'web', 'edusoft-catalog.json')
exec(open(os.path.join(HERE, 'kb_phan_he_data.py'), encoding='utf-8').read())   # PH: mã -> (tên, sp, test_tren, tab, dấu hiệu, là gì, edusoft, web, lưu ý)

def w(path, props, body):
    p = os.path.join(KB, path); os.makedirs(os.path.dirname(p), exist_ok=True)
    L = ['---']
    for k, v in props.items():
        if isinstance(v, list):
            L.append(k + ':' + ('' if v else ' []')); L += ['  - ' + str(x) for x in v]
        else:
            L.append(f'{k}: {v}')
    L.append('---')
    body = re.sub(r'^[ \t]+', '', body, flags=re.M).strip()
    body = re.sub(r'\n{3,}', '\n\n', body)
    open(p, 'w', encoding='utf-8').write('\n'.join(L) + '\n' + body + '\n')

# ---- bỏ nhắc tới case trong phần lưu ý ----
FIX = {
 'QLHT': 'Thông tin học kỳ, khóa sổ và phân quyền ảnh hưởng **mọi phân hệ** – sửa ở đây phải kiểm lại phân hệ dùng học kỳ đó. Case bảo mật / đăng nhập thường là web + hệ thống – đọc kỹ KH nói trang nào. Không đổi phân quyền tài khoản thật.',
 'KLGD': 'Biểu mẫu thanh toán / thù lao là **mẫu in** của KLGD – test bằng in/xuất trên Edusoft, đối chiếu số liệu đã tính.',
 'QLTS': 'Kết thúc tuyển sinh là bước **chuyển** sang QLSV và Thu/chi HP – kiểm dữ liệu đã sang đủ.',
 'QLSV': 'DS SV học kỳ là đầu vào của hầu hết phân hệ đào tạo. Mẫu kịch bản ghi dữ liệu: QLSV-001.',
 'DKMH': 'Sửa về **cài đặt** (thời gian, ràng buộc) → kiểm cả nơi cài (Edusoft) và nơi SV thấy (web). Đợt ĐKMH có tải rất lớn (sheet NetWeb_DKMH: hàng nghìn SV cùng lúc) – sửa hiệu năng cần test riêng.',
 'DKMHUI': 'Thông báo / lặp dòng / hiển thị → test web; nói tới "setting" thì kiểm thêm chỗ cài trên Edusoft ([[DKMH]]).',
 'DIEM': 'Điểm TB là đầu vào của xét học vụ, tốt nghiệp, học bổng – sửa cách tính điểm phải kiểm lại các phân hệ đó.',
 'KSDG': 'Phần form / mẫu in kết quả trên Edusoft, phần trả lời trên web; DHNT bắt khảo sát trước khi xem điểm (liên quan [[DIEM]] trên web).',
 'CSHP': 'Mã CSHP trên ACS gồm cả phần Edusoft lẫn phần SV xem trên web – **đọc lời KH**: nói "trang / summary / bảng hiển thị" → web; nói menu Chính sách HP / tính / đơn giá → Edusoft.',
 'NETWEB-UI': 'Không chạy kịch bản Edusoft cho sửa giao diện web.',
 'NETWEB-API': 'Đăng nhập / bảo mật: thử cả trường hợp sai (sai mật khẩu, hết phiên, không đủ quyền).',
 'EDUGO': '',
}
for k, v in FIX.items():
    t = list(PH[k]); t[8] = v; PH[k] = tuple(t)
t = list(PH['DKMHUI']); t[5] = 'Phần **giao diện web** của đăng ký môn học (trang ĐKMH – nhiều trường tách riêng khỏi cổng SV để chịu tải).'; PH['DKMHUI'] = tuple(t)
t = list(PH['NETWEB-API']); t[7] = 'Test **qua trang web** (thao tác đúng chức năng) + kiểm dữ liệu ghi xuống Edusoft.'; PH['NETWEB-API'] = tuple(t)
PH['QXHV'] = ('Xét học vụ', 'Edusoft', ['edusoft'], 'Quản lý điểm', 'học vụ, vi phạm, cảnh báo học tập, buộc thôi học',
  'Tiêu chuẩn xét + đợt xét → DS lớp xét → DS SV xét → xét học vụ → DS SV vi phạm (lưu đồ QXHV). Cùng khuôn với xét tốt nghiệp.',
  '`Quản lý điểm/ Xử lý học vụ học kỳ/ …`.', '', 'Nằm trong tab Quản lý điểm nhưng là quy trình riêng – mã ACS có thể là DIEM.')
PH['BVLV'] = ('Bảo vệ luận văn', 'Edusoft', ['edusoft', 'web'], 'Tốt nghiệp', 'đề tài, đề cương, hội đồng, bảo vệ luận văn, điểm luận văn',
  'Đợt bảo vệ, hội đồng → SV đăng ký đề tài → bảo vệ đề cương → DS SV bảo vệ luận văn → hội đồng luận văn → nhập điểm → **chuyển điểm luận văn vào môn học** (lưu đồ BVLV).',
  '`Tốt nghiệp/ Bảo vệ luận văn/ …`.', 'Đăng ký đề tài tốt nghiệp trực tuyến (tuỳ trường); khách tra cứu luận văn được công bố (DHNT).', 'Nằm trong tab Tốt nghiệp – mã ACS có thể là QLTN.')

# ---- DỮ LIỆU chảy giữa phân hệ: tên file, tiêu đề, phân hệ tạo, menu tạo, [(phân hệ dùng, dùng vào việc gì)], hiện trên web ----
E = [
 ('Hoc ky', 'Năm học – học kỳ', 'QLHT', 'Hệ thống/ Thông tin học kỳ/ Danh mục năm học học kỳ · Khởi tạo dữ liệu học kỳ · An toàn dữ liệu/ Khóa sổ phân hệ theo học kỳ',
   [('QLSV', 'DS SV học kỳ, quyết định theo học kỳ'), ('KHGD', 'lớp / phòng / viên chức / nhóm học / TKB học kỳ'), ('DKMH', 'đăng ký theo học kỳ'), ('CSHP', 'tính học phí học kỳ'),
    ('LTHI', 'đợt thi'), ('DIEM', 'điểm, xét học vụ học kỳ'), ('KSDG', 'kỳ đánh giá'), ('KLGD', 'khối lượng theo đợt')], 'Học kỳ hiện hành quyết định dữ liệu SV/GV thấy trên web.'),
 ('Tai khoan va phan quyen', 'Tài khoản & phân quyền', 'QLHT', 'Hệ thống/ Quản lý người dùng/ …', [('NETWEB-UI', 'phân quyền quản trị trên web'), ('NETWEB-API', 'đăng nhập web')], 'Đăng nhập / quyền trên web.'),
 ('Cau hinh NetWEB', 'Cấu hình NetWEB', 'QLHT', 'Hệ thống/ Quản trị NetWEB/ Chỉnh định menu · Chỉnh định chung · Cấm SV xem vì nợ học phí',
   [('NETWEB-UI', 'menu / chức năng ẩn-hiện, chặn SV nợ học phí')], 'Toàn bộ cổng web.'),
 ('Danh muc dao tao', 'Bậc – hệ – ngành đào tạo', 'KHGD', 'Kế hoạch/ Quản trị phân hệ/ Quản lý danh mục/ Danh mục bậc đào tạo · hệ đào tạo · bậc hệ · ngành/chuyên ngành',
   [('KHGD', 'dựng CTĐT')], ''),
 ('Mon hoc', 'Môn học', 'KHGD', 'Kế hoạch/ Chương trình đào tạo/ Thông tin môn học/ Danh mục môn học',
   [('KHGD', 'CTĐT, nhóm học'), ('DKMH', 'môn tiên quyết / học trước / song hành'), ('CSHP', 'mức đơn giá và số TCHP môn học'), ('DIEM', 'môn thay thế'), ('KLGD', 'loại hình cho môn học'), ('QLTN', 'môn bắt buộc / tự chọn trong tiêu chuẩn')], 'SV xem CTĐT, môn tiên quyết.'),
 ('Khoi lop', 'Khối lớp (khóa đào tạo của 1 ngành)', 'KHGD', 'Kế hoạch/ Quản trị phân hệ/ Quản lý danh mục/ Danh mục khối lớp',
   [('QLSV', 'lớp sinh viên thuộc khối'), ('KHGD', 'CTĐT kế hoạch theo khối'), ('DIEM', 'môn thay thế theo khối'), ('NETWEB-UI', 'điều hướng theo khối lớp / cơ sở (DHNT)')], ''),
 ('Lop sinh vien', 'Lớp sinh viên', 'QLSV', 'Sinh viên/ Quản trị phân hệ/ Quản lý danh mục/ Danh mục lớp',
   [('QLTS', 'gán tên lớp cho thí sinh trúng tuyển'), ('KHGD', 'DS lớp học kỳ, biểu đồ KHHT lớp'), ('DKMH', 'thời gian / đối tượng đăng ký theo lớp'), ('QXHV', 'DS lớp xét'), ('QLTN', 'DS lớp xét')], ''),
 ('CTDT', 'Chương trình đào tạo (chuẩn → kế hoạch → thực hiện)', 'KHGD', 'Kế hoạch/ Chương trình đào tạo/ Cập nhật chương trình đào tạo/ CTĐT chuẩn · CTĐT kế hoạch · CTĐT thực hiện',
   [('KHGD', 'biểu đồ KHHT lớp → quy hoạch nhóm học'), ('QLTN', 'tiêu chuẩn tốt nghiệp theo chương trình'), ('DKMH', 'môn được đăng ký theo chương trình')], 'SV xem chương trình đào tạo.'),
 ('Ho so thi sinh', 'Hồ sơ thí sinh', 'QLTS', 'Tuyển sinh/ Nhập liệu hồ sơ/ Nhập hồ sơ thí sinh/ … (hoặc thí sinh đăng ký trên web)',
   [('QLTS', 'xét tuyển theo đợt')], 'Thí sinh đăng ký xét tuyển, tra cứu xét tuyển, nhập học online.'),
 ('DS trung tuyen', 'Danh sách trúng tuyển', 'QLTS', 'Tuyển sinh/ Hồ sơ nhập học/ Danh sách trúng tuyển → Tiếp sinh/ Chuyển danh sách trúng tuyển sang phân hệ QLSV',
   [('QLSV', 'SV trúng tuyển → Quyết định vào mới'), ('QLTV', 'thí sinh đã đóng học phí nhập học → Thu/chi HP')], ''),
 ('Quyet dinh sinh vien', 'Quyết định vào / ra sinh viên', 'QLSV', 'Sinh viên/ Sinh viên học kỳ/ QĐ vào/ra sinh viên/ Quyết định vào mới · đổi lớp · tạm dừng · học lại · nghỉ học · tốt nghiệp',
   [('QLSV', 'tự tổng hợp DS SV học kỳ; tạm dừng / nghỉ / tốt nghiệp → xóa tên kỳ sau')], ''),
 ('Danh muc sinh vien', 'Danh mục sinh viên (mọi SV của trường)', 'QLSV', 'Sinh viên/ Sinh viên học kỳ/ Danh mục sinh viên',
   [('QLSV', 'lý lịch, hồ sơ – văn bằng'), ('NETWEB-API', 'tài khoản SV đăng nhập web')], 'SV xem / cập nhật lý lịch.'),
 ('DS SV hoc ky', 'Danh sách sinh viên học kỳ', 'QLSV', 'Sinh viên/ Sinh viên học kỳ/ Danh sách sinh viên học kỳ (tổng hợp tự động từ quyết định)',
   [('DKMH', 'SV được đăng ký môn học (phải có trong DS SV học kỳ)'), ('CSHP', 'SV tính học phí'), ('KSDG', 'đáp viên'), ('QXHV', 'DS SV xét'), ('QLTN', 'DS SV xét'), ('QKTX', 'SV ở ký túc xá')], 'Quyền dùng web của SV trong học kỳ.'),
 ('Dien chinh sach', 'Diện chính sách / miễn giảm', 'QLSV', 'Sinh viên/ Miễn giảm hoc phí và Học bổng/ Sinh viên diện chính sách/ Diện chính sách sinh viên học kỳ (CSHP: Chính sách HP/ … / Miễn giảm học phí/ Diện chính sách sinh viên học kỳ)',
   [('CSHP', 'miễn giảm khi tính học phí')], 'Miễn giảm hiện trong trang học phí của SV.'),
 ('Vien chuc', 'Viên chức / cán bộ giảng dạy', 'QLNS', 'Nhân sự/ … lý lịch CBCNV → Kế hoạch/ Thông tin viên chức/ Danh sách viên chức học kỳ',
   [('KHGD', 'gán giảng viên cho nhóm học'), ('KLGD', 'thông tin khối lượng cho cán bộ'), ('KSDG', 'giảng viên được đánh giá'), ('LTHI', 'phân công coi thi')], 'GV đăng nhập web (TKB, lịch coi thi, nhập điểm).'),
 ('Phong hoc', 'Phòng học kỳ', 'KHGD', 'Kế hoạch/ Danh sách dữ liệu học kỳ/ Danh sách phòng học kỳ',
   [('KHGD', 'xếp TKB tìm phòng'), ('LTHI', 'nhập phòng sử dụng trong đợt thi')], ''),
 ('Nhom hoc', 'Nhóm học (nhóm tổ)', 'KHGD', 'Kế hoạch/ Qui hoạch nhóm học phần/ … → Thông tin nhóm học phần/ Danh sách nhóm tổ',
   [('DKMH', 'nhóm học + số chỗ để đăng ký'), ('LTHI', 'tạo nhóm thi'), ('KSDG', 'dữ liệu đánh giá (nhóm tổ, GV)'), ('KLGD', 'chốt dữ liệu từ kế hoạch'), ('DIEM', 'bảng ghi điểm / nhập điểm theo nhóm học')], ''),
 ('Thoi khoa bieu', 'Thời khóa biểu', 'KHGD', 'Kế hoạch/ Thời khóa biểu/ Xếp thời khoá biểu/ Xếp thời khóa biểu tự động → Xem thời khóa biểu',
   [('DKMH', 'nhóm học có lịch để SV chọn'), ('LTHI', 'kiểm trùng TKB học với lịch thi'), ('KLGD', 'khối lượng giảng dạy')], 'SV + GV xem TKB tuần / học kỳ; GV nghỉ dạy – dạy bù.'),
 ('Rang buoc DKMH', 'Ràng buộc & thời gian đăng ký', 'DKMH', 'Đăng ký MH/ Đăng ký môn học/ Tài nguyên và ràng buộc/ … · Ràng buộc đăng ký online/ Thời gian đăng ký theo lớp · Chỉnh định chung',
   [('DKMHUI', 'web chặn / mở đăng ký theo ràng buộc')], 'SV bị chặn đăng ký (nợ HP, thiếu tiên quyết, vượt tín chỉ, hết chỗ, ngoài thời gian).'),
 ('KQ DKMH', 'Kết quả đăng ký môn học', 'DKMH', 'Đăng ký MH/ Đăng ký môn học/ … (offline) hoặc SV đăng ký trên web → Khai thác báo biểu/ Kết quả đăng ký/ Xem file MH đã đăng ký',
   [('CSHP', 'tính học phí'), ('LTHI', 'nguồn danh sách thi'), ('DIEM', 'bảng ghi điểm, nhập điểm'), ('QLSV', 'điểm danh; xóa kết quả SV đã hủy ĐKMH')], 'SV xem môn đã đăng ký, học phí tạm tính; CVHT duyệt.'),
 ('Hoc phi', 'Học phí phải thu (đã tính)', 'CSHP', 'Chính sách HP/ Tính và In học phí/ Tính học phí/ … (dùng đơn giá, công thức, miễn giảm, phụ thu)',
   [('QLTV', 'thu học phí'), ('EDUBILL', 'đóng học phí trực tuyến')], 'SV xem học phí (summary + bảng chi tiết, miễn giảm).'),
 ('No hoc phi', 'Nợ học phí', 'CSHP', 'Chính sách HP/ Chính sách học phí/ Nợ học phí/ Danh sách SV tồn nợ HP · Cập nhật tồn nợ',
   [('DKMH', 'ràng buộc: SV nợ HP không được đăng ký'), ('QLHT', 'Cấm SV xem vì nợ học phí (web)'), ('QLTV', 'thu nợ')], 'SV nợ bị chặn xem / đăng ký trên web.'),
 ('Phieu thu', 'Phiếu thu học phí', 'QLTV', 'Thu/chi HP/ Hoạt động thu/chi/ Thu học phí/ Thu học phí 1 SV · Import phiếu thu → Khai thác báo biểu/ In bảng kê thu/chi học phí',
   [('CSHP', 'giảm nợ học phí')], 'Đóng học phí trực tuyến ghi phiếu thu.'),
 ('Danh sach thi', 'Danh sách thi – lịch thi', 'LTHI', 'Tổ chức thi/ … nhóm thi → đợt thi → tổ thi → Xếp lịch thi theo đợt thi',
   [('DIEM', 'tạo phách, bảng ghi điểm theo tổ thi')], 'SV + GV xem lịch thi; GV xem lịch coi thi.'),
 ('Diem mon hoc', 'Điểm môn học', 'DIEM', 'Quản lý nhập điểm/ … (danh sách, import, phách, bảo lưu, phúc khảo) – GV nhập điểm trên web',
   [('DIEM', 'tính điểm trung bình')], 'GV nhập điểm online; SV xem điểm; phúc tra trực tuyến (GAM).'),
 ('Diem luan van', 'Điểm luận văn', 'BVLV', 'Tốt nghiệp/ Bảo vệ luận văn/ Bảo vệ luận văn/ Nhập điểm bảo vệ luận văn → Chuyển điểm luận văn vào môn học',
   [('DIEM', 'thành điểm môn học')], ''),
 ('Diem trung binh', 'Điểm trung bình – tích lũy', 'DIEM', 'Quản lý điểm/ Quản lý điểm tổng kết học phần/ Tổng kết điểm thi/ Cộng điểm TB → In phiếu điểm sinh viên',
   [('QXHV', 'xét học vụ'), ('QLTN', 'xét tốt nghiệp'), ('QLSV', 'xét học bổng')], 'SV xem điểm, phiếu điểm.'),
 ('Diem ren luyen', 'Điểm rèn luyện', 'QLSV', 'Sinh viên/ Điểm danh và Điểm rèn luyện/ Quản lý điểm rèn luyện/ … (SV + GV đánh giá trên web)',
   [('QLSV', 'xét học bổng / khen thưởng')], 'SV tự đánh giá, GV/CVHT duyệt trên web.'),
 ('Ket qua hoc vu', 'Kết quả xét học vụ', 'QXHV', 'Quản lý điểm/ Xử lý học vụ học kỳ/ Xem kết quả/ Kết quả xét học kỳ hiện tại',
   [('QLSV', 'SV vi phạm (cảnh báo / thôi học) – cần xác nhận cách đưa sang quyết định')], ''),
 ('Ket qua tot nghiep', 'Kết quả xét tốt nghiệp', 'QLTN', 'Tốt nghiệp/ Xét tốt nghiệp/ Xem kết quả tốt nghiệp/ Danh sách sinh viên tốt nghiệp',
   [('QLSV', 'Quyết định tốt nghiệp → xóa tên khỏi DS SV học kỳ kỳ sau, thông tin tốt nghiệp, in bằng')], 'SV xem kết quả xét tốt nghiệp / tiền tốt nghiệp; tra cứu văn bằng.'),
 ('Ket qua khao sat', 'Kết quả khảo sát', 'KSDG', 'Khảo sát đánh giá/ … DS đáp viên → đáp viên trả lời trên web → Khai thác báo biểu/ In kết quả',
   [('DIEM', 'DHNT: phải khảo sát xong mới xem điểm (web)')], 'SV / GV / khách trả lời; GV xem kết quả.'),
 ('Khoi luong giang day', 'Khối lượng giảng dạy', 'KLGD', 'Khối lượng/ Chuẩn bị dữ liệu/ Chốt dữ liệu từ kế hoạch → Tính khối lượng → In chi tiết thù lao',
   [], ''),
 ('Hop dong KTX', 'Hợp đồng ký túc xá', 'QKTX', 'Ký túc xá/ Quản lý hợp đồng/ Quản lý vào/ Hợp đồng theo phòng',
   [('QKTX', 'thu phí lưu trú, thanh lý')], 'SV đăng ký ký túc xá trên web.'),
]
# ---- lớp LOGIC: muốn có X phải có Y, menu Edusoft ↔ dữ liệu ----
exec(open(os.path.join(HERE, 'kb_logic_data.py'), encoding='utf-8').read())
E += E_ADD
E = [(fn, TITLE_FIX.get(fn, t), s, mn, u, wb) for fn, t, s, mn, u, wb in E]
ENT = {e[0]: e for e in E}
assert set(REQ) == set(ENT), set(REQ) ^ set(ENT)
LV = {}
def lv(fn, path=()):
    assert fn not in path, 'vòng lặp: ' + ' → '.join(path + (fn,))
    if fn not in LV:
        LV[fn] = 1 + max([lv(r, path + (fn,)) for r, _ in REQ[fn]] or [-1])
    return LV[fn]
for fn in ENT: lv(fn)
def anc(fn):  # mọi dữ liệu phải có trước, theo thứ tự chuẩn bị (tầng thấp trước)
    s, st = set(), [fn]
    while st:
        for r, _ in REQ[st.pop()]:
            if r not in s: s.add(r); st.append(r)
    return sorted(s, key=lambda x: (LV[x], x))
NEXT = {fn: sorted([x for x in ENT if any(r == fn for r, _ in REQ[x])], key=lambda x: (LV[x], x)) for fn in ENT}
def desc(fn):
    s, st = set(), [fn]
    while st:
        for x in NEXT[st.pop()]:
            if x not in s: s.add(x); st.append(x)
    return sorted(s, key=lambda x: (LV[x], x))
TANG = {0: 'nền, khai báo đầu tiên'}

# menu Edusoft (web/edusoft-catalog.json) → phân hệ kb + dữ liệu
CAT = json.load(open(CATALOG, encoding='utf-8'))
KWR = {fn: (ph, re.compile(rx, re.I)) for fn, (ph, rx) in KW.items()}
def segs(s): return {x.strip().lower() for x in re.split(r'/|·|→|\(|\)|…', s) if len(x.strip()) > 3}
KEYSEG = {fn: segs(ENT[fn][3]) for fn in ENT}
MENUS = []  # (ma, ph kb, path, [dữ liệu], [dữ liệu tạo ở menu này])
for m in CAT['menus']:
    ph = CAT_PH.get(m['ph'], m['ph'])
    if ph not in PH: continue
    p = m['path']; leaf = p.split('/')[-1].strip(); low = p.lower()
    hit = [fn for fn, (phs, rx) in KWR.items() if (not phs or m['ph'] in phs) and rx.search(low)]
    key = [fn for fn in hit if ENT[fn][2] == ph and leaf.lower() in KEYSEG[fn]] + [fn for fn, mas in KEYMA.items() if m['ma'] in mas]
    hit = hit + [fn for fn in key if fn not in hit]
    MENUS.append((m['ma'], ph, p, hit, key))
KEYM = {}
for ma, ph, p, hit, key in MENUS:
    for fn in key: KEYM.setdefault(fn, []).append((ma, ph, p))
def _ord(fn, x):
    mas = KEYMA.get(fn, [])
    if x[0] in mas: return mas.index(x[0]) - 100
    i = ENT[fn][3].lower().find(x[2].split('/')[-1].strip().lower())
    return i if i >= 0 else 999
for fn in KEYM: KEYM[fn].sort(key=lambda x: _ord(fn, x))
def mfile(ma, p): return 'Menu/' + re.sub(r'[\\/:*?"<>|#^\[\]]', ' ', p.split('/')[-1].strip()).strip() + f' ({ma})'

# module -> produced / consumed
prod, cons = {}, {}
for fn, title, src, menu, uses, web in E:
    prod.setdefault(src, []).append(fn)
    for m, why in uses:
        cons.setdefault(m, []).append((fn, why))
WEB_OF = {'DKMHUI': 'DKMH', 'NETWEB-UI': None, 'NETWEB-API': None}

# ---- ghi Du-lieu/ ----
for fn, title, src, menu, uses, web in E:
    users = sorted({m for m, _ in uses if m != src})
    need, a, nx = REQ[fn], anc(fn), NEXT[fn]
    km = KEYM.get(fn, [])
    prep = [f'{i + 1}. [[{x}|{ENT[x][1]}]] – tạo ở [[{ENT[x][2]}]]' + (f' · menu [[{mfile(*KEYM[x][0][:1], KEYM[x][0][2])}|{KEYM[x][0][2].split("/")[-1].strip()}]]' if KEYM.get(x) else '') for i, x in enumerate(a)]
    w(f'Du-lieu/{fn}.md', {'loai': 'du-lieu', 'ten': title, 'tang': LV[fn], 'tao_o': f'"[[{src}]]"', 'dung_o': [f'"[[{m}]]"' for m in users],
                          'can_co': [f'"[[{r}]]"' for r, _ in need], 'la_dieu_kien_cho': [f'"[[{x}]]"' for x in nx],
                          'tu_khoa': json.dumps(KW[fn][1], ensure_ascii=False), 'tu_khoa_ph': list(KW[fn][0]),
                          'nguon': 'luu-do', 'trang_thai': 'tu-tai-lieu'}, f"""
    # {title}

    **Tạo ở** [[{src}]] – `{menu}` · tầng {LV[fn]} trong [[00 Logic nghiệp vụ]] (cần {len(anc(fn))} loại dữ liệu có trước)

    ## Muốn có {title.split(' (')[0].split(' –')[0]} thì phải có trước
    {chr(10).join(f'- [[{r}|{ENT[r][1]}]] – {why}' for r, why in need) if need else '- Không cần dữ liệu nào trước – đây là dữ liệu **nền**, khai báo đầu tiên.'}

    ## Chuẩn bị dữ liệu test (theo thứ tự)
    {chr(10).join(prep) if prep else 'Không cần chuẩn bị gì trước.'}
    {len(prep) + 1 if prep else 1}. **{title}** – tạo ở [[{src}]]

    ## Là điều kiện cho (có dữ liệu này mới có)
    {chr(10).join(f'- [[{x}|{ENT[x][1]}]]' for x in nx) if nx else '- (không có dữ liệu nào phụ thuộc trực tiếp)'}

    ## Dùng ở
    {chr(10).join(f'- [[{m}]] – {why}' for m, why in uses) if uses else '- (chỉ dùng trong phân hệ tạo ra)'}

    ## Menu Edusoft
    {chr(10).join(f'- [[{mfile(ma, p)}|{p}]]' for ma, ph, p in km) if km else '- (chưa nối được menu tạo – xem `' + menu + '`)'}
    {f'- Còn {sum(1 for x in MENUS if fn in x[3]) - len(km)} menu khác có dùng / xem dữ liệu này – xem danh sách menu của phân hệ.' if sum(1 for x in MENUS if fn in x[3]) > len(km) else ''}

    ## Trên web
    {web or '—'}

    ## Khi dữ liệu này bị sửa / lỗi
    Kiểm lại: {', '.join(f'[[{m}]]' for m in users) if users else '[[' + src + ']]'}{' và trang web liên quan' if web else ''}.
    Dữ liệu sinh ra từ nó (kiểm lại nếu số liệu đổi): {', '.join(f'[[{x}|{ENT[x][1].split(" (")[0]}]]' for x in desc(fn)) or '—'}.
    """)

# ---- ghi Menu/: menu tạo dữ liệu (1 ghi chú / menu) + danh sách menu từng phân hệ ----
for fn, km in KEYM.items():
    for ma, ph, p in km:
        hit = next(x[3] for x in MENUS if x[0] == ma)
        need = REQ[fn]
        w(mfile(ma, p) + '.md', {'loai': 'menu', 'ma': ma, 'phan_he': f'"[[{ph}]]"', 'duong_dan': f'"{p}"', 'tao': [f'"[[{fn}]]"'],
                                 'nguon': 'danh-muc-menu', 'trang_thai': 'tu-tai-lieu'}, f"""
        # {p.split('/')[-1].strip()}

        `{p}` · mã `{ma}` · phân hệ [[{ph}]] · [[Menu/{ph}|các menu khác của {ph}]]

        ## Tạo dữ liệu
        - [[{fn}|{ENT[fn][1]}]]

        ## Trước khi dùng menu này phải có
        {chr(10).join(f'- [[{r}|{ENT[r][1]}]] – {why}' + (f' (menu [[{mfile(*KEYM[r][0][:1], KEYM[r][0][2])}|{KEYM[r][0][2].split("/")[-1].strip()}]])' if KEYM.get(r) else '') for r, why in need) if need else '- Không cần dữ liệu nào trước.'}

        ## Lưu ở đây → ảnh hưởng tới
        {chr(10).join(f'- [[{m}]] – {why}' for m, why in ENT[fn][4] if m != ph) or '- chỉ trong ' + ph}
        {('- Dữ liệu phụ thuộc: ' + ', '.join(f'[[{x}|{ENT[x][1].split(" (")[0]}]]' for x in NEXT[fn])) if NEXT[fn] else ''}

        ## Dữ liệu liên quan khác trên menu
        {', '.join(f'[[{x}]]' for x in hit if x != fn) or '—'}
        """)
for ph in PH:
    ms = [x for x in MENUS if x[1] == ph]
    if not ms: continue
    by = {}
    for ma, _, p, hit, key in ms:
        parts = [x.strip() for x in p.split('/')]
        by.setdefault(' / '.join(parts[1:2]) or parts[0], []).append((ma, p, hit, key, parts[-1]))
    L = []
    for g in sorted(by):
        L.append(f'\n## {g}')
        for ma, p, hit, key, leaf in sorted(by[g], key=lambda x: x[1]):
            mid = ' / '.join(x.strip() for x in p.split('/')[2:-1])
            name = f'[[{mfile(ma, p)}|{leaf}]]' if key else leaf
            L.append(f'- {name}' + (f' <small>({mid})</small>' if mid else '') + f' `{ma}`' + (' → ' + ', '.join(f'[[{x}]]' for x in hit) if hit else ''))
    w(f'Menu/{ph}.md', {'loai': 'danh-sach-menu', 'phan_he': f'"[[{ph}]]"', 'so_menu': len(ms), 'nguon': 'danh-muc-menu'}, f"""
    # Menu {ph} – {PH[ph][0]}

    {len(ms)} menu Edusoft (từ `web/edusoft-catalog.json`). Tên **có liên kết** = menu **tạo** dữ liệu (có ghi chú riêng); → [[…]] = dữ liệu menu đó đụng tới.
    Phân hệ: [[{ph}]].
    """ + '\n'.join(L))

# ---- ghi Phan-he/ ----
for ma, (ten, sp, tt, tab, dh, lagi, ed, web, luuy) in PH.items():
    mine = prod.get(ma, [])
    inn = [(fn, why) for fn, why in cons.get(ma, []) if ENT[fn][2] != ma]
    srcs = sorted({ENT[fn][2] for fn, _ in inn})
    outs = sorted({m for fn in mine for m, _ in ENT[fn][4] if m != ma})
    lines_in = [f'- [[{fn}|{ENT[fn][1]}]] từ [[{ENT[fn][2]}]] – {why}' for fn, why in inn]
    lines_out = [f'- [[{fn}|{ENT[fn][1]}]] → ' + ', '.join(f'[[{m}]]' for m, _ in ENT[fn][4] if m != ma) for fn in mine if any(m != ma for m, _ in ENT[fn][4])]
    lines_own = [f'- [[{fn}|{ENT[fn][1]}]]' for fn in mine]
    w(f'Phan-he/{ma}.md', {'loai': 'phan-he', 'ma': ma, 'ten': ten, 'san_pham': f'"[[{sp}]]"', 'test_tren': tt, 'tab_edusoft': tab,
                           'nhan_tu': [f'"[[{m}]]"' for m in srcs], 'dua_sang': [f'"[[{m}]]"' for m in outs],
                           'dau_hieu': dh, 'nguon': 'tai-lieu', 'trang_thai': 'tu-tai-lieu'}, f"""
    # {ma} – {ten}

    ## Là gì
    {lagi}

    ## Nhận dữ liệu từ
    {chr(10).join(lines_in) if lines_in else '—'}

    ## Tạo ra
    {chr(10).join(lines_own) if lines_own else '—'}

    ## Đưa sang
    {chr(10).join(lines_out) if lines_out else '—'}

    ## Sửa ở đây → kiểm lại
    {('Các phân hệ nhận dữ liệu của ' + ma + ': ' + ', '.join(f'[[{m}]]' for m in outs) + '.') if outs else 'Không có phân hệ nào nhận dữ liệu trực tiếp.'}
    {('Lỗi có thể do dữ liệu đầu vào từ: ' + ', '.join(f'[[{m}]]' for m in srcs) + ' – kiểm dữ liệu đó trước khi kết luận.') if srcs else ''}

    ## Phần trên Edusoft
    {ed or '—'}
    {('Menu: [[Menu/' + ma + '|' + str(sum(1 for x in MENUS if x[1] == ma)) + ' menu của ' + ma + ']]' + (' – menu tạo dữ liệu: ' + ', '.join(f'[[{mfile(x[0], x[2])}|{x[2].split("/")[-1].strip()}]]' for x in MENUS if x[1] == ma and x[4]) if any(x[1] == ma and x[4] for x in MENUS) else '') + '.') if any(x[1] == ma for x in MENUS) else ''}

    ## Phần trên web / app
    {web or '—'}

    ## Test ở đâu
    {'Chỉ ' + tt[0] + '.' if len(tt) == 1 else 'Tuỳ yêu cầu: ' + ' / '.join(tt) + ' – xem KH nói về màn hình Edusoft hay trang web.'}

    ## Lưu ý
    {luuy or '—'}

    ---
    Nguồn: tài liệu HDSD (SharePoint "1. Tài liệu Edusoft"), lưu đồ LuuDo_NEW (skill `tailieu-edusoft/luu-do`), sheet Release(TestMenu). Liên kết dữ liệu theo lưu đồ.
    """)

# ---- bản đồ ----
edges = {}
for fn, title, src, menu, uses, web in E:
    for m, _ in uses:
        if m != src: edges.setdefault((src, m), []).append(title.split(' (')[0].split(' –')[0])
ids = {m: re.sub(r'[^A-Za-z0-9]', '_', m) for m in PH}
mer = ['```mermaid', 'flowchart LR']
for (a, b), ts in sorted(edges.items()):
    lab = ', '.join(ts[:2]) + ('…' if len(ts) > 2 else '')
    mer.append(f'  {ids[a]}["{a}"] -->|{lab}| {ids[b]}["{b}"]')
mer.append('```')
chain = """
- [[QLTS]] xét tuyển → **DS trúng tuyển** → [[QLSV]] (QĐ vào mới → DS SV học kỳ) và [[QLTV]] (học phí nhập học).
- [[KHGD]] CTĐT → nhóm học → thời khóa biểu; cùng **DS SV học kỳ** ([[QLSV]]) → [[DKMH]] → **KQ ĐKMH**.
- KQ ĐKMH → [[CSHP]] tính học phí → nợ học phí → [[QLTV]] thu (web: [[EDUBILL]]).
- KQ ĐKMH → [[LTHI]] danh sách thi → lịch thi.
- KQ ĐKMH → [[DIEM]] nhập điểm → **điểm TB** → [[QXHV]] học vụ, [[QLTN]] tốt nghiệp (→ [[QLSV]] QĐ tốt nghiệp), [[QLSV]] học bổng.
- [[BVLV]] điểm luận văn → [[DIEM]]; [[KSDG]] khảo sát theo nhóm học / GV; [[KLGD]] khối lượng từ nhóm học + TKB + viên chức.
- Nợ học phí ([[CSHP]]) quay lại chặn [[DKMH]] và chặn xem web ([[QLHT]] cấu hình NetWEB).
- Web: [[NETWEB-UI]], [[NETWEB-API]], [[DKMHUI]] hiển thị / ghi dữ liệu của các phân hệ trên; năm học – học kỳ và phân quyền ở [[QLHT]] dùng cho tất cả.
"""
w('00 Bản đồ phân hệ.md', {'loai': 'ban-do'}, f"""
# Bản đồ phân hệ – dữ liệu chảy giữa các phân hệ

Đọc theo chiều mũi tên: phân hệ bên trái **tạo** dữ liệu, phân hệ bên phải **dùng**. Sửa một phân hệ → kiểm lại các phân hệ ở phía sau nó;
lỗi ở một phân hệ → kiểm dữ liệu đầu vào từ các phân hệ phía trước. Chi tiết từng dữ liệu ở thư mục `Du-lieu/`.

## Chuỗi chính (lưu đồ LuuDo_NEW)
{chain}

## Sơ đồ (Obsidian vẽ tự động)
{chr(10).join(mer)}

## Dữ liệu dùng chung
{chr(10).join(f'- [[{fn}|{t}]] – tạo ở [[{s}]], dùng ở ' + ', '.join(sorted({f'[[{m}]]' for m, _ in u if m != s})) for fn, t, s, _, u, _ in E if any(m != s for m, _ in u))}

Xem dạng mạng: mở **Graph view** (biểu tượng ở thanh trái) – mỗi chấm là một ghi chú, đường nối là liên kết.
""")

# ---- 00 Logic nghiệp vụ ----
byl = {}
for fn in ENT: byl.setdefault(LV[fn], []).append(fn)
ass = []
for l in sorted(byl):
    ass.append(f'\n### Tầng {l}' + (' – ' + TANG[l] if l in TANG else ''))
    for fn in sorted(byl[l]):
        t = ENT[fn][1]; need = REQ[fn]
        ass.append(f'- Muốn có **[[{fn}|{t}]]** ([[{ENT[fn][2]}]]) ' + ('thì phải có: ' + '; '.join(f'[[{r}|{ENT[r][1].split(" (")[0]}]] ({why})' for r, why in need) if need else '– không cần gì trước (dữ liệu nền).'))
idd = {fn: 'D' + str(i) for i, fn in enumerate(sorted(ENT))}
mer2 = ['```mermaid', 'flowchart TD']
for fn in sorted(ENT, key=lambda x: (LV[x], x)):
    mer2.append(f'  {idd[fn]}["{ENT[fn][1].split(" (")[0]}<br/><small>{ENT[fn][2]}</small>"]')
for fn in sorted(ENT):
    for r, _ in REQ[fn]: mer2.append(f'  {idd[r]} --> {idd[fn]}')
mer2.append('```')
w('00 Logic nghiệp vụ.md', {'loai': 'logic'}, f"""
# Logic nghiệp vụ – muốn có X thì phải có Y

Mọi dữ liệu trong Edusoft / Netweb nằm trên một **chuỗi điều kiện**: phải khai báo dữ liệu tầng dưới thì mới tạo được dữ liệu tầng trên.
Ví dụ: muốn có **sinh viên** thì phải **tuyển sinh** (hồ sơ → trúng tuyển → quyết định vào mới); có **sinh viên + giảng viên + CTĐT**
thì mới có **kế hoạch giảng dạy** (nhóm học) → **thời khóa biểu** → SV **đăng ký môn học** → **học phí, lịch thi, điểm** → **học vụ, tốt nghiệp**.

Tầng = số bước dữ liệu phải đi qua trước (tầng 0 khai báo đầu tiên). Dùng khi đọc case ACS:
1. Case nói tới menu / dữ liệu nào → tìm ghi chú dữ liệu đó (tầng mấy, phân hệ nào).
2. **Chuẩn bị dữ liệu test** = các dữ liệu tầng dưới nó (mục "Chuẩn bị dữ liệu test" trong ghi chú) – phải có sẵn trên môi trường test.
3. **Kiểm tra không ảnh hưởng** = dữ liệu tầng trên sinh ra từ nó + các phân hệ dùng nó.
4. Hai case cùng chạm một dữ liệu (hoặc dữ liệu cha – con) là **case liên quan** – test cùng nhau, dùng chung dữ liệu chuẩn bị.

## Khẳng định theo tầng
{chr(10).join(ass)}

## Sơ đồ điều kiện (mũi tên: phải có trước → mới có sau)
{chr(10).join(mer2)}

Menu Edusoft của từng phân hệ: thư mục `Menu/` (menu **tạo** dữ liệu có ghi chú riêng, nối tới dữ liệu cần có trước). Liên kết phân hệ: [[00 Bản đồ phân hệ]].
""")

# ---- đồ thị cho app: dựng lại TỪ GHI CHÚ vừa ghi (ghi chú là nguồn) rồi nhúng vào web/index.html ----
sys.path.insert(0, ROOT)
import kb_graph
G = kb_graph.build(KB)
kb_graph.embed(G, os.path.join(ROOT, 'web', 'index.html'))
print('menu', len(MENUS), 'menu tao', sum(len(v) for v in KEYM.values()), 'du lieu trong ban do', len(G['data']))

print('ok', len(E), 'du lieu,', len(PH), 'phan he,', len(edges), 'canh')
