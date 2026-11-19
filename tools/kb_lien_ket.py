"""python tools/kb_lien_ket.py kb  – GHI ĐÈ kb/Phan-he, kb/Du-lieu, kb/00 Bản đồ phân hệ.md (mất phần người test sửa tay: chạy rồi so git diff). Dựng KB liên kết phân hệ: Du-lieu/ (dữ liệu chảy giữa phân hệ) + Phan-he/ (nhận từ / đưa sang / sửa ở đây kiểm lại) + bản đồ."""
import os, re, sys
KB = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
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
ENT = {e[0]: e for e in E}
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
    w(f'Du-lieu/{fn}.md', {'loai': 'du-lieu', 'ten': title, 'tao_o': f'"[[{src}]]"', 'dung_o': [f'"[[{m}]]"' for m in users],
                          'nguon': 'luu-do', 'trang_thai': 'tu-tai-lieu'}, f"""
    # {title}

    **Tạo ở** [[{src}]] – `{menu}`

    ## Dùng ở
    {chr(10).join(f'- [[{m}]] – {why}' for m, why in uses) if uses else '- (chỉ dùng trong phân hệ tạo ra)'}

    ## Trên web
    {web or '—'}

    ## Khi dữ liệu này bị sửa / lỗi
    Kiểm lại: {', '.join(f'[[{m}]]' for m in users) if users else '[[' + src + ']]'}{' và trang web liên quan' if web else ''}.
    """)

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
print('ok', len(E), 'du lieu,', len(PH), 'phan he,', len(edges), 'canh')
