# Dữ liệu LOGIC nghiệp vụ cho tools/kb_lien_ket.py (exec trong đó, sau khi có E và PH).
# Nguồn: lưu đồ LuuDo_NEW, nghiệp vụ QLSV (skill tailieu-edusoft), danh mục menu web/edusoft-catalog.json.

# ---- dữ liệu thêm (cùng khuôn E: tên file, tiêu đề, phân hệ tạo, menu tạo, [(phân hệ dùng, việc)], trên web) ----
E_ADD = [
 ('Ky tuyen sinh', 'Kỳ / đợt tuyển sinh (ngành, khối, phương thức)', 'QLTS',
  'Tuyển sinh/ Chuẩn bị/ Danh sách kỳ tuyển sinh · Danh sách đợt tuyển sinh · Danh sách ngành tuyển sinh · Danh sách khối tuyển sinh · Định nghĩa phương thức hồ sơ XT',
  [('QLTS', 'nhập hồ sơ, xét tuyển theo đợt')], 'Thí sinh đăng ký xét tuyển theo đợt / phương thức đang mở.'),
]
TITLE_FIX = {'Nhom hoc': 'Nhóm học – kế hoạch giảng dạy học kỳ (nhóm tổ)'}

# ---- MUỐN CÓ X THÌ PHẢI CÓ TRƯỚC Y (vì sao) ----
REQ = {
 'Hoc ky': [],
 'Tai khoan va phan quyen': [],
 'Danh muc dao tao': [],
 'Cau hinh NetWEB': [('Tai khoan va phan quyen', 'người dùng quản trị NetWEB')],
 'Ky tuyen sinh': [('Danh muc dao tao', 'ngành tuyển sinh lấy từ ngành đào tạo')],
 'Ho so thi sinh': [('Ky tuyen sinh', 'hồ sơ nhập theo kỳ / đợt, ngành, phương thức')],
 'DS trung tuyen': [('Ho so thi sinh', 'xét tuyển trên hồ sơ + điểm chuẩn')],
 'Khoi lop': [('Danh muc dao tao', 'khối lớp = khóa của một ngành / bậc hệ')],
 'Lop sinh vien': [('Khoi lop', 'lớp thuộc một khối lớp')],
 'Mon hoc': [('Danh muc dao tao', 'môn học thuộc khoa / ngành quản lý')],
 'CTDT': [('Mon hoc', 'chương trình gồm các môn học'), ('Khoi lop', 'CTĐT kế hoạch / thực hiện theo khối lớp')],
 'Quyet dinh sinh vien': [('DS trung tuyen', 'QĐ vào mới cho thí sinh trúng tuyển'), ('Lop sinh vien', 'SV được xếp vào lớp'), ('Hoc ky', 'quyết định có hiệu lực từ học kỳ')],
 'Danh muc sinh vien': [('Quyet dinh sinh vien', 'QĐ vào mới tạo hồ sơ sinh viên')],
 'DS SV hoc ky': [('Quyet dinh sinh vien', 'tổng hợp tự động từ quyết định vào / ra'), ('Hoc ky', 'danh sách theo từng học kỳ')],
 'Dien chinh sach': [('DS SV hoc ky', 'diện chính sách gán cho SV trong học kỳ')],
 'Vien chuc': [('Hoc ky', 'danh sách viên chức học kỳ')],
 'Phong hoc': [('Hoc ky', 'danh sách phòng học kỳ')],
 'Nhom hoc': [('CTDT', 'biểu đồ kế hoạch học tập của lớp → môn mở trong học kỳ'), ('Lop sinh vien', 'lớp học kỳ cần học môn'),
              ('DS SV hoc ky', 'sĩ số lớp → số nhóm'), ('Vien chuc', 'phân công giảng viên cho nhóm'), ('Hoc ky', 'nhóm học thuộc học kỳ')],
 'Thoi khoa bieu': [('Nhom hoc', 'xếp lịch cho từng nhóm học'), ('Phong hoc', 'tìm phòng trống'), ('Vien chuc', 'không trùng lịch giảng viên')],
 'Rang buoc DKMH': [('Mon hoc', 'môn tiên quyết / học trước / song hành'), ('Lop sinh vien', 'thời gian đăng ký theo lớp'), ('Hoc ky', 'đợt đăng ký của học kỳ')],
 'KQ DKMH': [('DS SV hoc ky', 'chỉ SV có trong DS SV học kỳ mới đăng ký được'), ('Nhom hoc', 'chọn nhóm học còn chỗ'),
             ('Thoi khoa bieu', 'nhóm có lịch, không trùng TKB'), ('Rang buoc DKMH', 'được phép đăng ký (thời gian, tiên quyết, tín chỉ, nợ học phí)')],
 'Hoc phi': [('KQ DKMH', 'học phí tính trên môn đã đăng ký'), ('Mon hoc', 'đơn giá / số tín chỉ học phí'), ('Dien chinh sach', 'miễn giảm')],
 'Phieu thu': [('Hoc phi', 'thu trên số học phí phải thu')],
 'No hoc phi': [('Hoc phi', 'phải thu'), ('Phieu thu', 'đã thu')],
 'Danh sach thi': [('KQ DKMH', 'SV dự thi = SV đã đăng ký môn'), ('Nhom hoc', 'nhóm thi tạo từ nhóm học'), ('Phong hoc', 'phòng thi'), ('Vien chuc', 'phân công coi thi')],
 'Diem mon hoc': [('KQ DKMH', 'bảng ghi điểm theo SV đã đăng ký'), ('Danh sach thi', 'phách / tổ thi khi thi tập trung')],
 'Diem luan van': [('DS SV hoc ky', 'SV bảo vệ luận văn'), ('Vien chuc', 'hội đồng, giảng viên hướng dẫn')],
 'Diem trung binh': [('Diem mon hoc', 'cộng điểm trung bình từ điểm môn học')],
 'Diem ren luyen': [('DS SV hoc ky', 'đánh giá rèn luyện SV trong học kỳ')],
 'Ket qua hoc vu': [('Diem trung binh', 'xét theo điểm TB / tích lũy'), ('DS SV hoc ky', 'danh sách SV xét')],
 'Ket qua tot nghiep': [('Diem trung binh', 'điểm TB tích lũy, số tín chỉ'), ('CTDT', 'tiêu chuẩn theo chương trình'), ('DS SV hoc ky', 'danh sách SV xét')],
 'Ket qua khao sat': [('Nhom hoc', 'đánh giá theo nhóm học / giảng viên'), ('Vien chuc', 'giảng viên được đánh giá'), ('DS SV hoc ky', 'đáp viên')],
 'Khoi luong giang day': [('Nhom hoc', 'chốt dữ liệu từ kế hoạch'), ('Thoi khoa bieu', 'số tiết theo lịch'), ('Vien chuc', 'giảng viên được tính')],
 'Hop dong KTX': [('Danh muc sinh vien', 'hợp đồng lập cho sinh viên')],
}

# ---- nhận ra dữ liệu trong menu Edusoft / lời KH: (phân hệ menu được tính – trống = mọi phân hệ, regex) ----
KW = {
 'Hoc ky': (['HTQL'], r'thông tin học kỳ|năm học học kỳ|khởi tạo dữ liệu học kỳ|khóa sổ'),
 'Tai khoan va phan quyen': (['HTQL'], r'người dùng|phân quyền|nhóm quyền|tài khoản|đăng nhập|mật khẩu'),
 'Cau hinh NetWEB': (['HTQL'], r'netweb|chỉnh định menu|cấm sv xem'),
 'Danh muc dao tao': (['KHGD', 'HTQL'], r'danh mục (bậc|hệ|ngành|chuyên ngành|khoa)|bậc hệ'),
 'Ky tuyen sinh': (['QLTS'], r'kỳ tuyển sinh|đợt tuyển sinh|ngành tuyển sinh|khối tuyển sinh|phương thức'),
 'Ho so thi sinh': (['QLTS'], r'hồ sơ (thí sinh|xét tuyển|đăng ký)|nhập liệu hồ sơ|nguyện vọng|thí sinh'),
 'DS trung tuyen': (['QLTS'], r'trúng tuyển|điểm chuẩn|xét tuyển|tiếp sinh|nhập học'),
 'Khoi lop': ([], r'khối lớp'),
 'Lop sinh vien': (['QLSV', 'KHGD'], r'danh mục lớp|danh sách lớp|lớp sinh viên|đổi lớp'),
 'Mon hoc': ([], r'danh mục môn học|thông tin môn học|môn (học )?(tương đương|thay thế|tiên quyết|học trước|song hành)'),
 'CTDT': ([], r'chương trình đào tạo|ctđt|kế hoạch học tập|khung chương trình'),
 'Quyet dinh sinh vien': (['QLSV'], r'quyết định|qđ (vào|ra)|tạm dừng|nghỉ học|học lại|thôi học'),
 'Danh muc sinh vien': (['QLSV'], r'danh mục sinh viên|lý lịch|hồ sơ (sinh viên|sv)|thông tin sinh viên|văn bằng'),
 'DS SV hoc ky': ([], r'(danh sách )?sinh viên học kỳ|ds sv học kỳ'),
 'Dien chinh sach': ([], r'diện chính sách|miễn giảm|học bổng'),
 'Vien chuc': ([], r'viên chức|cbcnv|cán bộ|cbgd|giảng viên'),
 'Phong hoc': (['KHGD', 'LTHI'], r'phòng học|danh sách phòng|phòng thi|phòng ưu tiên'),
 'Nhom hoc': ([], r'nhóm học|nhóm tổ|nhóm môn|lớp môn học|lớp học phần|phân công (cbgd|giảng)|kế hoạch giảng dạy'),
 'Thoi khoa bieu': ([], r'thời khóa biểu|thời khoá biểu|tkb|lịch học|dạy bù|nghỉ dạy'),
 'Rang buoc DKMH': (['DKMH'], r'ràng buộc|thời gian (đăng ký|rút)|chỉnh định chung|tài nguyên'),
 'KQ DKMH': ([], r'đăng ký môn|kết quả đăng ký|kq đkmh|đkmh|môn học đã đăng ký|hủy kq|rút môn|đăng ký học phần'),
 'Hoc phi': (['CSHP', 'QLTV'], r'học phí|đơn giá|công thức thu|loại hình thu|phụ thu|khoản thu'),
 'Phieu thu': (['QLTV'], r'phiếu thu|thu học phí|bảng kê|thu vãng lai|đóng học phí|thanh toán'),
 'No hoc phi': ([], r'nợ học phí|tồn nợ|công nợ|nợ hp'),
 'Danh sach thi': (['LTHI'], r'lịch thi|nhóm thi|đợt thi|tổ thi|danh sách thi|coi thi|số báo danh|hoãn thi|trùng lịch'),
 'Diem mon hoc': (['DIEM', 'DMKT'], r'nhập điểm|bảng ghi điểm|phách|phúc khảo|phúc tra|bảo lưu|điểm thi|điểm (môn|thành phần|quá trình)|xem điểm|bảng điểm'),
 'Diem luan van': (['QLTN'], r'luận văn|đề tài|đề cương|hội đồng'),
 'Diem trung binh': (['DIEM'], r'điểm trung bình|điểm tb|tích lũy|phiếu điểm|tổng kết|xếp loại'),
 'Diem ren luyen': ([], r'rèn luyện|điểm danh'),
 'Ket qua hoc vu': ([], r'học vụ|cảnh báo học tập|buộc thôi học'),
 'Ket qua tot nghiep': (['QLTN'], r'tốt nghiệp|xét tn'),
 'Ket qua khao sat': (['KSDG', 'DGGD'], r'khảo sát|đánh giá|câu hỏi|form|đáp viên|thang đo'),
 'Khoi luong giang day': (['KLGD'], r'khối lượng|thù lao|hệ số|giờ chuẩn|thanh toán giảng'),
 'Hop dong KTX': (['QKTX'], r'ký túc xá|ktx|lưu trú|hợp đồng|phòng ở|điện nước'),
}
# mã phân hệ trong danh mục menu Edusoft → mã phân hệ trong kb
CAT_PH = {'HTQL': 'QLHT', 'DMKT': 'DIEM', 'DGGD': 'KSDG'}
# menu TẠO dữ liệu ghi rõ theo mã menu (bổ sung khi tên menu khác tên trong lưu đồ)
KEYMA = {
 'Tai khoan va phan quyen': ['H62', 'H67'],
 'Ho so thi sinh': ['T2.03.00A', 'T2.03.01'],
 'KQ DKMH': ['M13', 'M11.01'],
 'Hoc phi': ['P21.01', 'P21.03'],
 'Diem mon hoc': ['D21.03', 'D21.01'],
 'Diem trung binh': ['D52.03', 'D52.06'],
 'Diem luan van': ['QLV04.04', 'QLV04.06'],
 'Diem ren luyen': ['S83.05', 'S83.06'],
 'Ket qua hoc vu': ['D73.01', 'D73.03'],
 'Ket qua khao sat': ['Z3.01.02', 'Z4.01.01'],
 'Khoi luong giang day': ['G4.02.1'],
}
