# -*- coding: utf-8 -*-
"""MCP của app AQ Auto Test – Claude Desktop trên máy người dùng đọc KB, đọc case ACS, ghi plan test nháp vào app.

Đường đi:  Claude Desktop ──stdio──▶ aq_mcp.py ──HTTP 127.0.0.1──▶ server.py POST api/mcp (file này)
                                                                   └─▶ ACS qua cầu nối của app Electron (AQ_ACS_RELAY, chỉ đọc)
Công cụ:
  kb_tim, kb_doc, kb_ghi, kb_phan_tich, kb_du_lieu   – knowledge base (vault Obsidian, thư mục kbDir hoặc kb/ cạnh server.py)
  kb_anh, kb_luu_anh                                 – ảnh trong KB (xem / lưu ảnh case kèm mô tả để tra lại)
  truong_hoc_case                                    – học mô hình trường từ case ACS → kb/Case-truong/
  acs_toi, acs_tim_case, acs_case, acs_anh           – ACS CHỈ ĐỌC (phiên người dùng đã đăng nhập trong app); không có công cụ ghi lên ACS
  retest_ds, retest_doc_plan, retest_ghi_plan        – plan test NHÁP (collection retestDrafts) – người test duyệt trên trang Test case ACS
An toàn: chỉ nghe 127.0.0.1 + token trong <local>/mcp.json; kb_ghi chỉ ghi .md trong thư mục KB, từ chối nội dung giống mật khẩu / token / chuỗi kết nối.
Chỉ thư viện chuẩn.
"""
import base64, json, os, re, time, datetime, urllib.parse, urllib.request, urllib.error
from pathlib import Path

import kb_graph

PROTO = "2025-06-18"
RT_COLS = ['case_id', 'title', 'school_code', 'module', 'case_type', 'priority', 'status', 'assignee_raw', 'analyst_raw', 'req_state',
           'tester_raw', 'test_state', 'received_at', 'due_date', 'resolved_at', 'changed']
GROUPS = {'prep': 'Chuẩn bị', 'repro': 'Tái hiện như KH', 'check': 'Kiểm tra theo yêu cầu KH', 'reg': 'Kiểm tra không ảnh hưởng'}
PLATFORMS = ('web', 'edusoft', 'app', 'api', 'report')
KINDS = ('ui', 'data', 'report', 'perm', 'add')
SECRET = re.compile(r'(mật\s*khẩu|password|passwd|pwd|token|secret|api[_\- ]?key)\s*[:=]\s*\S{4,}|data source\s*=|initial catalog\s*=|;\s*password\s*=', re.I)

INSTRUCTIONS = """Bạn đang nối với app AQ Auto Test (máy người test của AQTech) – kiểm thử phần mềm Edusoft.NET (Windows) và Netweb (cổng web SV/GV).
VIỆC CHÍNH: phân tích case ACS cho ĐÚNG nghiệp vụ trước, test sau. Không đoán từ tiêu đề hay mã phân hệ.
Đọc kb_doc '00 Cách phân tích case.md' một lần, rồi làm theo thứ tự:
 PHIẾU ACS trước tiên: acs_case trả 'phieu_acs' (đầu case, quy trình 5 bước Tiếp nhận → BA → DEV → Kiểm thử → Gửi mail, khách hàng, loại hợp đồng, tab)
    và 'kiem_tra_du' – mục nào thiếu (BA chưa phân tích, chưa có bản sửa, chưa có hạn…) nói ngay cho người dùng.
 0. Trường: school_code 4 ký tự = trường (case chung của trường); dài hơn 4 ký tự = PHÂN CẤP của trường đó (vd DHMOTX = DHMO – từ xa, DHMODH = DHMO – đại học):
    case theo phân cấp chỉ hiệu lực trên phân cấp đó. 'AQ' = case nội bộ / sản phẩm chung. Mã chưa có ghi chú Truong/ → nói rõ, không đoán tên trường.
 0b. Mô hình trường: đọc Case-truong/<mã 4 ký tự>.md (nếu có) – trường này hay có case gì, dạng gì, case tiếp nối, nhận xét. Chưa có / cũ → truong_hoc_case.
 0c. Quy trình: đọc Quy-trinh/ của phân hệ (00 Quy trình xuyên phân hệ.md) – bước trước cung cấp gì, cài đặt nào hay gây case, bước sau phải kiểm.
     Cần cách thao tác / biến chỉnh định → Tai-lieu/ (HDSD theo phân hệ, nơi lưu trên SharePoint).
 1. Phân hệ: đọc Phan-he/<mã>.md (phần Edusoft / web, dạng case thường gặp). Mã phân hệ là nơi xếp case, không phải nơi lỗi xảy ra.
 2. Yêu cầu KH (yeu_cau_kh): hiện trạng (ở đâu, ai gặp), từng mong muốn, dữ liệu cụ thể (MSSV, lớp, học kỳ), loại (lỗi / yêu cầu mới / hỏi / xử lý dữ liệu).
    ẢNH: acs_case trả 'anh' (ảnh KH / BA / Dev chụp, '[ảnh]' trong lời KH là chỗ chèn ảnh) → LUÔN xem bằng acs_anh trước khi kết luận.
    Ảnh nói nhiều hơn lời: đúng màn hình / menu / trang web, cột, số liệu, câu báo lỗi, chỗ khoanh đỏ. Lời KH và ảnh khác nhau → tin ảnh, ghi rõ.
    Ghi điều thấy trong từng ảnh vào phiếu (case_ghi_phan_tich → anh: [{so, nguon, mo_ta}]) để lần sau tra được.
 3. BA (ba): BA chốt lỗi hay yêu cầu mới, phạm vi, quy tắc nghiệp vụ. BA khác KH → theo BA. Không có BA → ghi rõ, đánh dấu câu hỏi mở.
 4. Dev (dev): sửa ở đâu (VersionSchool/<trường> = bản riêng trường, Source.NET/store = Edusoft, report = mẫu in), bản build, sửa gì / không sửa gì.
 5. Đối chiếu từng ý KH ↔ BA ↔ Dev → ý thiếu / chưa rõ = câu hỏi mở.
 6. Dạng case: chọn trong Dang-case/ (gợi ý 'goi_y_dang_case' chỉ là gợi ý – đọc ghi chú dạng case để kiểm).
 7. Dữ liệu: kb_phan_tich → dữ liệu case đụng, phải có trước, ảnh hưởng tới.
 8. Case liên quan / tương tự: acs_case_lien_quan → case gốc ([mã] trong tiêu đề), cùng trường + phân hệ, cùng mô hình ở trường khác; nói VÌ SAO và NÊN LÀM GÌ.
 KB có ảnh (màn hình mẫu, ảnh case cũ): kb_doc trả kèm ảnh; kb_tim tìm cả ảnh và phiếu phân tích case cũ (kể cả mô tả ảnh).
 Ảnh case đáng giữ làm mẫu (không lộ thông tin cá nhân SV/GV) → kb_luu_anh kèm mô tả.
 Ghi kết quả bằng case_ghi_phan_tich (người test xem ở app). Trình bày cho người dùng theo đúng các mục trên, nêu câu hỏi mở.
 Chỉ khi người dùng yêu cầu mới soạn plan test (retest_ghi_plan) – và chỉ sau khi đã có phiếu phân tích.
 ĐẦU RA: đọc case + ảnh để chốt "đầu ra cần đạt sau khi Dev xử lý" (vd case chậm / mở lâu → plan làm NHƯ NGƯỜI DÙNG: nhấn Ctrl+Shift+T rồi mở menu, làm thao tác ra dữ liệu như KH – vd nút … cạnh Mã SV → chọn SV → Chọn – rồi đọc "Thời gian mở form: Ns" ở thanh dưới đáy Edusoft; dữ liệu hiện nhanh không treo – không cần kiểm ảnh hưởng).
 PLAN = BƯỚC THAO TÁC CỤ THỂ (người dùng chốt 25/11): KHÔNG chép yêu cầu KH thành bước, KHÔNG để "làm đúng thao tác KH nêu". Trước khi soạn: đọc KB liên quan
 (Phan-he, Du-lieu, Cach-test – acs_case trả 'cach_test' kèm bước mẫu {Menu}/{Ô mới}/{Ô cũ}/{Danh mục}), tra case gốc / liên quan (acs_case_lien_quan), đọc hết case:
 'dev' (Chi tiết xử lý: "Nội dung: …" từng LẦN = đã sửa gì → mỗi ý một bước kiểm), Trả lời KH (chức năng sau khi sửa), 'trao_doi_test' (lần test trước báo lỗi gì,
 SV / mã nào → làm lại đúng chỗ đó). Mỗi bước repro = menu cụ thể + thao tác (chọn hồ sơ / điền file / bấm nút) ; mỗi check = điều nhìn thấy được sau thao tác.
 PLAN TEST chỉ 4 phần: (1) môi trường test (Edusoft.NET.exe bản test / trang web TEST của trường + bản sửa) – moi_truong; (2) tài khoản đăng nhập – can_cung_cap
 (web: mã GV / MSSV… theo ngữ cảnh, KHÔNG hỏi mật khẩu; Edusoft dùng tài khoản test ở Máy chạy thử); (3) thao tác: nhom 'repro' – vào menu / trang nào, làm gì;
 (4) đầu ra: nhom 'check' – mỗi đầu ra một mục. Chỉ thêm 'prep' / 'reg' khi case thật sự cần. Dùng luồng kb/Luong-test (acs_case trả 'luong_test') nếu khớp.
 Case web hoặc dữ liệu có hiện trên web: acs_case trả 'trang_web' (kb/Web/) – đọc chỉnh định của trang, trang có 'ghi_nguoc' thì kiểm lại Edusoft; Netweb chung CSDL với Edusoft, web chưa đổi = cache (đăng xuất / đăng nhập lại).
 Bước dùng {Tên} (vd {Mã GV}) – app thay bằng giá trị người dùng nhập.
 Người dùng mô tả luồng test mới → ghi kb/Luong-test/<tên>.md (Properties: loai: luong-test, dau_hieu, phan_he, nen_tang, can_cung_cap, buoc, khong_anh_huong).
Quy tắc: KHÔNG ghi gì lên ACS (không có công cụ ghi). Chỉ môi trường test/demo, dữ liệu test có tiền tố AUTO… / TEST_….
Không ghi mật khẩu, token, chuỗi kết nối vào KB. Liên kết Netweb trong Truong/ là site THẬT – chỉ để nhận biết trường, không thao tác.
Khi người dùng sửa / dạy kiến thức (mã trường trên ACS, quy tắc nghiệp vụ, dấu hiệu dạng case): ghi vào KB bằng kb_ghi, giữ đúng Properties, viết tiếng Việt."""


def _s(o, n=None):
    return {"type": "string", "description": o} if n is None else {"type": "string", "description": o, "enum": n}


TOOLS = [
    {"name": "kb_tim", "description": "Tìm trong knowledge base nghiệp vụ (vault Obsidian) theo từ khoá – ghi chú (dòng khớp, ảnh trong ghi chú), "
                                      "file ảnh, và phiếu phân tích case cũ (kể cả mô tả ảnh của case).",
     "inputSchema": {"type": "object", "properties": {"tu_khoa": _s("từ khoá, vd 'học phí', 'đăng ký môn học', 'DHNT'"),
                                                      "gioi_han": {"type": "integer", "description": "số ghi chú tối đa (mặc định 12)"}}, "required": ["tu_khoa"]}},
    {"name": "kb_doc", "description": "Đọc nguyên văn một ghi chú KB, vd '00 Logic nghiệp vụ.md', 'Du-lieu/KQ DKMH.md', 'Phan-he/CSHP.md', 'Menu/DKMH.md'. "
                                      "Ghi chú có ảnh (![[…]]) thì trả kèm ảnh (tối đa 4).",
     "inputSchema": {"type": "object", "properties": {"duong_dan": _s("đường dẫn tương đối trong KB, đuôi .md")}, "required": ["duong_dan"]}},
    {"name": "kb_anh", "description": "Xem một ảnh trong KB (png/jpg/gif/webp) – đường dẫn lấy từ kb_tim / kb_doc.",
     "inputSchema": {"type": "object", "properties": {"duong_dan": _s("đường dẫn tương đối trong KB, vd 'Anh/64457-trang-hoc-phi.jpg'")}, "required": ["duong_dan"]}},
    {"name": "kb_luu_anh", "description": "Lưu một ảnh của case ACS vào KB kèm MÔ TẢ (điều ảnh cho thấy) để sau này tra được bằng kb_tim. "
                                          "Chỉ lưu ảnh không lộ thông tin cá nhân (tên, MSSV, số tiền của SV cụ thể) hoặc đã được người dùng đồng ý. "
                                          "Ảnh vào thư mục Anh/ (không đưa lên git), mô tả vào ghi chú .md.",
     "inputSchema": {"type": "object", "properties": {"ma_case": _s("mã case"), "so": {"type": "integer", "description": "số thứ tự ảnh trong acs_case.anh"},
                                                      "ten": _s("tên ngắn, vd 'trang-hoc-phi-mien-giam'"), "mo_ta": _s("ảnh cho thấy gì: màn hình/trang nào, chỗ nào, lỗi gì"),
                                                      "ghi_chu": _s("tuỳ chọn: thêm ảnh vào ghi chú có sẵn, vd 'Phan-he/CSHP.md'; trống = tạo Anh/<ten>.md")},
                     "required": ["ma_case", "so", "ten", "mo_ta"]}},
    {"name": "kb_ghi", "description": "Ghi / sửa một ghi chú KB (.md) – khi người dùng dạy kiến thức mới, xác nhận hoặc sửa liên kết. "
                                      "che_do 'thay' = thay toàn bộ nội dung, 'them' = thêm vào cuối. Giữ Properties ở đầu file. Không ghi mật khẩu/token.",
     "inputSchema": {"type": "object", "properties": {"duong_dan": _s("đường dẫn tương đối trong KB, đuôi .md"), "noi_dung": _s("nội dung Markdown"),
                                                      "che_do": _s("thay | them", ["thay", "them"])}, "required": ["duong_dan", "noi_dung"]}},
    {"name": "kb_phan_tich", "description": "Đọc một đoạn văn (tiêu đề + lời khách hàng + menu của case) theo bản đồ nghiệp vụ: dữ liệu case đụng tới, "
                                            "menu Edusoft khớp, dữ liệu PHẢI CÓ TRƯỚC (chuẩn bị test), dữ liệu / phân hệ BỊ ẢNH HƯỞNG (kiểm không ảnh hưởng).",
     "inputSchema": {"type": "object", "properties": {"van_ban": _s("tiêu đề + nội dung case"), "phan_he": _s("mã phân hệ của case trên ACS (vd CSHP) – tuỳ chọn")},
                     "required": ["van_ban"]}},
    {"name": "kb_du_lieu", "description": "Chi tiết một loại dữ liệu trong bản đồ (vd 'KQ DKMH', 'Học phí'): tạo ở đâu, phải có trước gì (cả chuỗi), là điều kiện cho gì, dùng ở phân hệ nào.",
     "inputSchema": {"type": "object", "properties": {"ten": _s("tên file trong Du-lieu/ hoặc tên dữ liệu")}, "required": ["ten"]}},
    {"name": "acs_toi", "description": "Tài khoản ACS (AQ Support Hub) đang đăng nhập trong app – kiểm tra kết nối.",
     "inputSchema": {"type": "object", "properties": {}}},
    {"name": "acs_tim_case", "description": "Tìm case trên ACS (chỉ đọc). Không truyền dieu_kien = case 'Đã xử lý', chưa test đạt. "
                                            "dieu_kien: [{truong, phep: eq|neq|in, gia_tri}], truong là một trong: " + ", ".join(RT_COLS) + ".",
     "inputSchema": {"type": "object", "properties": {
         "dieu_kien": {"type": "array", "items": {"type": "object", "properties": {"truong": {"type": "string"}, "phep": {"type": "string", "enum": ["eq", "neq", "in"]},
                                                                                   "gia_tri": {"type": "string"}}, "required": ["truong", "phep", "gia_tri"]}},
         "gioi_han": {"type": "integer", "description": "tối đa (mặc định 50, tối đa 200)"}}}},
    {"name": "acs_case", "description": "Đọc đầy đủ một case ACS (chỉ đọc), đã tách: trường (theo KB), phân hệ, YÊU CẦU KH, BA PHÂN TÍCH, DEV XỬ LÝ, bản sửa, case gốc, "
                                        "gợi ý dạng case, diễn biến. Bước đầu của mọi phân tích case.",
     "inputSchema": {"type": "object", "properties": {"ma_case": _s("mã case, vd 64501")}, "required": ["ma_case"]}},
    {"name": "acs_anh", "description": "XEM ảnh trong một case ACS (ảnh KH / BA / Dev chụp, chỉ đọc). so = số thứ tự trong acs_case.anh; "
                                       "không truyền = các ảnh đầu (tối đa 4). Ảnh thu nhỏ để đọc được chữ trên màn hình.",
     "inputSchema": {"type": "object", "properties": {"ma_case": _s("mã case"), "so": {"type": "array", "items": {"type": "integer"}, "description": "vd [1, 2]"}},
                     "required": ["ma_case"]}},
    {"name": "acs_case_lien_quan", "description": "Tìm case LIÊN QUAN / TƯƠNG TỰ với một case trên ACS (chỉ đọc): case gốc ([mã] trong tiêu đề, 'lần 2'), "
                                                  "cùng trường + cùng phân hệ, cùng phân hệ / cùng dữ liệu / cùng dạng case ở trường khác – kèm lý do và gợi ý nên làm gì.",
     "inputSchema": {"type": "object", "properties": {"ma_case": _s("mã case"), "gioi_han": {"type": "integer", "description": "số case trả về (mặc định 15)"}},
                     "required": ["ma_case"]}},
    {"name": "case_ghi_phan_tich", "description": "Lưu PHIẾU PHÂN TÍCH case vào app (người test xem ở bước 1 trang Test case ACS). Ghi theo 00 Cách phân tích case.md.",
     "inputSchema": {"type": "object", "properties": {
         "ma_case": _s("mã case"), "truong": _s("mã ACS → trường, hệ / cơ sở, có bản riêng không"), "phan_he": _s("mã → tên, phần Edusoft hay web"),
         "kh_thay": _s("hiện trạng KH thấy: ở đâu, ai gặp"), "kh_muon": {"type": "array", "items": {"type": "string"}, "description": "từng mong muốn của KH"},
         "du_lieu_kh": _s("dữ liệu cụ thể KH đưa (MSSV, lớp, học kỳ…)"), "loai": _s("loại yêu cầu", ["loi", "yeu-cau-moi", "hoi-dap", "xu-ly-du-lieu"]),
         "ba_chot": _s("BA chốt gì ('chưa có BA' nếu không có)"), "dev_da_lam": _s("Dev sửa ở đâu, bản nào, sửa gì"),
         "doi_chieu": {"type": "array", "items": {"type": "object", "properties": {"y": {"type": "string"}, "ba": {"type": "string"}, "dev": {"type": "string"},
                                                                                  "trang_thai": {"type": "string", "enum": ["du", "thieu", "chua-ro"]}}, "required": ["y", "trang_thai"]}},
         "dang_case": {"type": "array", "items": {"type": "string"}, "description": "tên ghi chú Dang-case/, vd 'Hien thi web'"},
         "du_lieu": _s("dữ liệu case đụng tới, phải có trước, ảnh hưởng tới"),
         "case_lien_quan": {"type": "array", "items": {"type": "object", "properties": {"ma": {"type": "string"}, "ly_do": {"type": "string"}, "nen": {"type": "string"}},
                                                     "required": ["ma", "ly_do"]}},
         "cau_hoi_mo": {"type": "array", "items": {"type": "string"}, "description": "điều chưa rõ cần hỏi BA / Dev / KH"},
         "anh": {"type": "array", "description": "điều thấy trong từng ảnh của case (acs_anh)",
                 "items": {"type": "object", "properties": {"so": {"type": "integer"}, "nguon": {"type": "string"}, "mo_ta": {"type": "string"}}, "required": ["so", "mo_ta"]}}},
         "required": ["ma_case", "truong", "phan_he", "kh_muon", "ba_chot", "dev_da_lam"]}},
    {"name": "case_doc_phan_tich", "description": "Đọc phiếu phân tích đã lưu của một case (nếu có).",
     "inputSchema": {"type": "object", "properties": {"ma_case": _s("mã case")}, "required": ["ma_case"]}},
    {"name": "retest_ds", "description": "Danh sách phiếu test sau sửa lỗi trong app (case, trạng thái, nền tảng, tiến độ) và các plan nháp Claude đã ghi.",
     "inputSchema": {"type": "object", "properties": {}}},
    {"name": "retest_doc_plan", "description": "Đọc plan test của một case trong app: plan nháp (Claude ghi) và phiếu đang test (nếu đã nhận test).",
     "inputSchema": {"type": "object", "properties": {"ma_case": _s("mã case")}, "required": ["ma_case"]}},
    {"name": "retest_ghi_plan", "description": "Ghi plan test NHÁP cho một case vào app (trang Test case ACS) – người test xem, sửa rồi bấm Nhận test. "
                                               "Không thay phiếu đã nhận test. Plan gọn: nhom repro (thao tác: vào menu / trang, làm gì) + check (ĐẦU RA cần đạt sau khi Dev xử lý, mỗi đầu ra một mục); "
                                               "prep / reg chỉ khi thật sự cần. Môi trường + tài khoản: moi_truong, can_cung_cap.",
     "inputSchema": {"type": "object", "properties": {
         "ma_case": _s("mã case"), "nen_tang": _s("nơi test", list(PLATFORMS)), "loai_sua": _s("ui=giao diện, data=xử lý/số liệu, report=mẫu in, perm=tài khoản/quyền, add=thêm chức năng", list(KINDS)),
         "moi_truong": _s("môi trường test, vd 'Edusoft bản test của trường KTTC – bản 2026.11J.18'"),
         "cac_muc": {"type": "array", "items": {"type": "object", "properties": {"nhom": {"type": "string", "enum": list(GROUPS)}, "noi_dung": {"type": "string"}},
                                                "required": ["nhom", "noi_dung"]}},
         "ly_do": _s("vì sao chọn nền tảng / các mục này (ngắn) – hiện cho người test"),
         "can_cung_cap": {"type": "array", "description": "tài khoản / dữ liệu test cần người dùng nhập (chỉ mã, không mật khẩu) – vd [{ten:'Mã GV', vi_sao:'GV có lớp đang dạy'}, {ten:'MSSV', vi_sao:'SV thuộc lớp đó'}]; bước dùng {ten}",
                          "items": {"type": "object", "properties": {"ten": {"type": "string"}, "vi_sao": {"type": "string"}}, "required": ["ten"]}}},
         "required": ["ma_case", "nen_tang", "cac_muc"]}},
    {"name": "truong_hoc_case", "description": "HỌC MÔ HÌNH TRƯỜNG từ case ACS (chỉ đọc ACS): đọc các case của một trường (mọi phân cấp) hoặc 'tat-ca', "
                                               "gom theo phân hệ / phân cấp / dạng case / dữ liệu / chủ đề lặp lại / case tiếp nối → ghi kb/Case-truong/<mã>.md "
                                               "(+ tóm tắt trong Truong/<mã>.md). Tiêu đề được che email, SĐT, mã ≥ 7 số. Sau đó đọc vài case tiêu biểu và viết mục 'Nhận xét'.",
     "inputSchema": {"type": "object", "properties": {"ma_truong": _s("mã trường 4 ký tự (vd KTTC, DHMO) hoặc 'tat-ca'"),
                                                      "gioi_han": {"type": "integer", "description": "số case mới nhất đọc tối đa (mặc định 600, tối đa 3000)"}},
                     "required": ["ma_truong"]}},
]


class ToolError(Exception):
    pass


# ------------------------------------------------------------------ KB
def kb_dir(S):
    d = (S.CFG.get("kbDir") or "").strip()
    if d and Path(d).is_dir():
        return Path(d).resolve(), True
    p = S.ROOT / "kb"
    if (S.ROOT / ".git").exists():                       # repo: ghi thẳng vào kb/ (lên git bằng dong-bo.bat)
        return p.resolve(), True
    ka = getattr(S, "KB_APP", None)                      # app chưa chọn vault: KB ghi được của app (server.app_kb)
    if ka and Path(ka).is_dir():
        return Path(ka).resolve(), True
    return p.resolve(), False


def kb_path(S, rel, must_exist=True):
    base, _ = kb_dir(S)
    rel = str(rel or "").replace("\\", "/").strip().lstrip("/")
    if not rel.lower().endswith(".md") or ".." in rel.split("/") or rel.split("/")[0].startswith("."):
        raise ToolError("Đường dẫn ghi chú phải là file .md trong KB, vd 'Du-lieu/KQ DKMH.md'")
    p = (base / rel).resolve()
    if base not in p.parents:
        raise ToolError("Đường dẫn ra ngoài thư mục KB")
    if must_exist and not p.is_file():
        raise ToolError("Không có ghi chú " + rel + " – dùng kb_tim để tìm")
    return p


def t_kb_tim(S, a):
    base, _ = kb_dir(S)
    words = [w for w in re.split(r'\s+', str(a.get("tu_khoa") or "").lower().strip()) if w]
    if not words:
        raise ToolError("Cần từ khoá")
    lim = max(1, min(40, int(a.get("gioi_han") or 12)))
    res = []
    for f in base.rglob("*.md"):
        if any(x.startswith(".") for x in f.relative_to(base).parts):
            continue
        try:
            t = f.read_text("utf-8", errors="replace")
        except OSError:
            continue
        low, name = t.lower(), f.stem.lower()
        sc = sum(low.count(w) for w in words) + sum(5 for w in words if w in name)
        if f.relative_to(base).parts[0] == "Menu":
            sc = sc * 0.3                      # danh sách menu dài – xếp sau ghi chú dữ liệu / phân hệ
        if not sc or not all(w in low or w in name for w in words):
            continue
        lines = [ln.strip() for ln in t.split("\n") if any(w in ln.lower() for w in words) and not ln.startswith("---")][:3]
        res.append((sc, f.relative_to(base).as_posix(), lines))
    res.sort(key=lambda x: -x[0])
    out = []
    for r in res[:lim]:
        it = {"duong_dan": r[1], "dong_khop": [x[:220] for x in r[2]]}
        try:
            ims = note_images(base, base / r[1], (base / r[1]).read_text("utf-8", errors="replace"))
        except OSError:
            ims = []
        if ims:
            it["anh"] = [{"duong_dan": i["duong_dan"], "chu_thich": i["chu_thich"]} for i in ims[:6]]
        out.append(it)
    imgs = []                                   # file ảnh có tên khớp
    for f in base.rglob("*"):
        if f.suffix.lower() in IMG_MIME and not any(x.startswith(".") for x in f.relative_to(base).parts):
            n = kb_graph_slug(f.stem).replace("-", " ").replace("_", " ")
            if all(kb_graph_slug(w) in n for w in words):
                imgs.append(f.relative_to(base).as_posix())
    cases = []                                  # phiếu phân tích case cũ (kể cả mô tả ảnh)
    for x in S.list_docs("caseAnalyses"):
        d = x["data"]
        low = json.dumps(d, ensure_ascii=False).lower()
        if all(w in low for w in words):
            hit = [a.get("mo_ta", "")[:200] for a in (d.get("anh") or []) if any(w in str(a.get("mo_ta", "")).lower() for w in words)]
            cases.append({"ma_case": d.get("caseId"), "truong": str(d.get("truong", ""))[:80], "phan_he": str(d.get("phan_he", ""))[:60],
                          "kh_muon": (d.get("kh_muon") or [])[:3], "anh_khop": hit[:3]})
    return {"ket_qua": out, "tong": len(res), "file_anh": imgs[:20], "phieu_case": cases[:15],
            "nhac": "Ảnh: kb_anh <đường dẫn> để xem. Phiếu case cũ: case_doc_phan_tich, acs_anh để xem lại ảnh của case đó."}


IMG_MIME = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".gif": "image/gif", ".webp": "image/webp", ".bmp": "image/bmp"}
IMG_RX = r'\.(png|jpe?g|gif|webp|bmp)'


def note_images(base, note, text):
    """ảnh nhúng trong ghi chú: ![[a.png|300]] (Obsidian, tìm theo tên trong cả vault) và ![chú thích](a.png)"""
    out, seen = [], set()
    cands = [(m.group(1).strip(), "") for m in re.finditer(r'!\[\[([^\]|#]+?' + IMG_RX + r')(?:[|#][^\]]*)?\]\]', text, re.I)]
    cands += [(urllib.parse.unquote(m.group(2).strip().strip('<>')), m.group(1)) for m in re.finditer(r'!\[([^\]]*)\]\(([^)]+?' + IMG_RX + r')\s*\)', text, re.I)]
    for ref, cap in cands:
        if re.match(r'^[a-z]+:', ref, re.I):
            continue
        f = None
        for c in (note.parent / ref, base / ref):
            try:
                c = c.resolve()
            except OSError:
                continue
            if c.is_file() and base in c.parents:
                f = c
                break
        if f is None:
            f = next((x for x in base.rglob(Path(ref).name) if x.is_file()), None)
        if f is None or f in seen:
            continue
        seen.add(f)
        if not cap:                              # chú thích = dòng ngay sau ảnh
            i = text.find(ref)
            nxt = text[i:].split("\n", 2)
            cap = nxt[1].strip() if len(nxt) > 1 and not nxt[1].strip().startswith("!") else ""
        out.append({"file": f, "duong_dan": f.relative_to(base).as_posix(), "chu_thich": cap[:200]})
    return out


def acs_image(path=None, data=None, mime=None, mx=1568):
    """ảnh qua cầu nối app: path = ảnh trong ACS; data = chỉ thu nhỏ ảnh có sẵn"""
    url, tok = os.environ.get("AQ_ACS_RELAY"), os.environ.get("AQ_ACS_TOKEN")
    if not url or not tok:
        raise ToolError("Xem ảnh ACS chỉ có khi chạy trong app AQ Auto Test (máy cá nhân).")
    body = {"image": True, "max": mx}
    body.update({"data": data, "mime": mime} if data else {"path": path})
    req = urllib.request.Request(url.rstrip("/") + "/acs", data=json.dumps(body).encode("utf-8"),
                                 headers={"Content-Type": "application/json", "X-AQ-Token": tok}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            res = json.loads(r.read().decode("utf-8") or "{}")
    except (OSError, ValueError) as e:
        raise ToolError("Không lấy được ảnh qua app: %s" % e)
    if res.get("status") in (401, 403):
        raise ToolError("Chưa đăng nhập ACS – mở app AQ Auto Test → Test case ACS → Đăng nhập ACS.")
    if res.get("status") != 200 or not res.get("b64"):
        raise ToolError(res.get("error") or "Không lấy được ảnh (mã %s)" % res.get("status"))
    return res


def img_block(raw, mime):
    """bytes ảnh → khối image của MCP (thu nhỏ qua app khi lớn)"""
    b64 = base64.b64encode(raw).decode("ascii")
    if len(raw) > 700000 and os.environ.get("AQ_ACS_RELAY"):
        try:
            r = acs_image(data=b64, mime=mime)
            b64, mime = r["b64"], r.get("mime") or mime
        except ToolError:
            pass
    if len(b64) > 5000000:
        raise ToolError("Ảnh quá lớn để gửi (%d KB) – thu nhỏ ảnh rồi thử lại." % (len(raw) // 1024))
    return {"type": "image", "data": b64, "mimeType": mime}


def t_kb_doc(S, a):
    p = kb_path(S, a.get("duong_dan"))
    t = p.read_text("utf-8", errors="replace")
    t = t if len(t) < 60000 else t[:60000] + "\n…(cắt bớt)"
    base, _ = kb_dir(S)
    ims = note_images(base, p, t)
    if not ims:
        return t
    content = [{"type": "text", "text": t}]
    for i in ims[:4]:
        try:
            content += [{"type": "text", "text": "Ảnh %s%s" % (i["duong_dan"], (" – " + i["chu_thich"]) if i["chu_thich"] else "")},
                        img_block(i["file"].read_bytes(), IMG_MIME.get(i["file"].suffix.lower(), "image/png"))]
        except (OSError, ToolError) as e:
            content.append({"type": "text", "text": "Không mở được ảnh %s: %s" % (i["duong_dan"], e)})
    if len(ims) > 4:
        content.append({"type": "text", "text": "Còn %d ảnh: %s – xem bằng kb_anh." % (len(ims) - 4, ", ".join(i["duong_dan"] for i in ims[4:]))})
    return {"_content": content}


def t_kb_anh(S, a):
    base, _ = kb_dir(S)
    rel = str(a.get("duong_dan") or "").replace("\\", "/").strip().lstrip("/")
    p = (base / rel).resolve()
    if base not in p.parents or p.suffix.lower() not in IMG_MIME or not p.is_file():
        raise ToolError("Không có ảnh " + rel + " trong KB (png/jpg/gif/webp/bmp) – dùng kb_tim để tìm")
    return {"_content": [{"type": "text", "text": "Ảnh " + p.relative_to(base).as_posix()}, img_block(p.read_bytes(), IMG_MIME[p.suffix.lower()])]}


def t_kb_luu_anh(S, a):
    base, writable = kb_dir(S)
    if not writable:
        raise ToolError("KB đang là bản chỉ đọc đi kèm app – người dùng chọn thư mục vault ở Thiết lập ACS → Kết nối Claude Desktop → Thư mục KB.")
    cid = str(a.get("ma_case") or "").strip()
    if not re.match(r'^\d{1,10}$', cid):
        raise ToolError("Mã case phải là số")
    desc = re.sub(r'\s+', ' ', str(a.get("mo_ta") or "")).strip()
    if len(desc) < 10:
        raise ToolError("Cần mô tả ảnh cho thấy gì (để sau này tra được)")
    if SECRET.search(desc):
        raise ToolError("Mô tả có vẻ chứa mật khẩu / token – bỏ ra rồi ghi lại.")
    det = get_case(S, cid)
    ims = [f for f in find_files({"case": det, "attachments": list_endpoint(cid, ("/cs/cases/%s/attachments", "/cs/cases/%s/files")) or [],
                                  "mails": list_endpoint(cid, ("/cs/cases/%s/mails", "/cs/cases/%s/emails")) or []}) if f["anh"]]
    try:
        im = ims[int(a.get("so")) - 1]
    except (ValueError, TypeError, IndexError):
        raise ToolError("Case #%s có %d ảnh – so phải từ 1 tới %d" % (cid, len(ims), len(ims)))
    raw, mime = fetch_case_image(im, 1600)
    slug = re.sub(r'[^A-Za-z0-9_-]+', '-', kb_graph_slug(str(a.get("ten") or "anh"))).strip('-')[:60] or "anh"
    ext = ".jpg" if mime == "image/jpeg" else (".png" if mime == "image/png" else IMG_MIME_EXT.get(mime, ".png"))
    d = base / "Anh"
    d.mkdir(parents=True, exist_ok=True)
    name, n = "%s-%s" % (cid, slug), 1
    while (d / (name + ext)).exists():
        n += 1
        name = "%s-%s-%d" % (cid, slug, n)
    (d / (name + ext)).write_bytes(raw)
    line = "![[%s%s]]\n%s _(case #%s, ảnh %s – %s)_\n" % (name, ext, desc, cid, a.get("so"), im["nguon"])
    gc = str(a.get("ghi_chu") or "").strip()
    if gc:
        p = kb_path(S, gc, must_exist=False)
        p.parent.mkdir(parents=True, exist_ok=True)
        cur = p.read_text("utf-8", errors="replace") if p.exists() else ""
        p.write_text(cur.rstrip("\n") + ("\n\n" if cur else "") + line, "utf-8")
    else:
        p = d / (name + ".md")
        p.write_text("---\nloai: anh\ncase: \"%s\"\nnguon: %s\n---\n# %s\n\n%s" % (cid, im["nguon"], re.sub(r'\s+', ' ', str(a.get("ten") or slug))[:80], line), "utf-8")
    return {"ok": True, "anh": "Anh/" + name + ext, "ghi_chu": p.relative_to(base).as_posix(),
            "nhac": "Ảnh nằm trong KB/Anh (không đưa lên git – có thể có dữ liệu thật); mô tả trong ghi chú .md thì đồng bộ được."}


def t_kb_ghi(S, a):
    base, writable = kb_dir(S)
    if not writable:
        raise ToolError("KB đang là bản chỉ đọc đi kèm app. Người dùng chọn thư mục vault Obsidian (thư mục kb của repo) ở app: "
                        "Test case ACS → Thiết lập ACS → Kết nối Claude Desktop → Thư mục KB.")
    body = str(a.get("noi_dung") or "")
    if not body.strip():
        raise ToolError("Nội dung trống")
    if len(body) > 200000:
        raise ToolError("Nội dung quá dài")
    if SECRET.search(body):
        raise ToolError("Nội dung có vẻ chứa mật khẩu / token / chuỗi kết nối – không ghi vào KB (KB nằm trong git).")
    p = kb_path(S, a.get("duong_dan"), must_exist=False)
    mode = a.get("che_do") or "thay"
    p.parent.mkdir(parents=True, exist_ok=True)
    if mode == "them" and p.exists():
        cur = p.read_text("utf-8", errors="replace")
        body = cur.rstrip("\n") + "\n\n" + body.strip("\n") + "\n"
    elif not body.endswith("\n"):
        body += "\n"
    existed = p.exists()
    p.write_text(body, "utf-8")
    return {"ok": True, "duong_dan": p.relative_to(base).as_posix(), "tao_moi": not existed,
            "nhac": "Người dùng chạy dong-bo.bat để đưa thay đổi KB lên git cho máy khác."}


def _catalog(S):
    c = getattr(S, "_CAT", None)
    if c is None:
        try:
            c = json.loads((S.WEB / "edusoft-catalog.json").read_text("utf-8"))["menus"]
        except Exception:
            c = []
        S._CAT = c
    return c


def find_menu(S, text, mod):
    low = str(text or "").lower()
    best = None
    for m in _catalog(S):
        leaf = m["path"].split("/")[-1].strip().lower()
        ph = kb_graph.CAT_PH.get(m["ph"], m["ph"])
        if len(leaf) < 8 or leaf not in low or (mod and ph != mod and len(leaf) < 18):
            continue
        s = len(leaf) + (20 if mod and ph == mod else 0)
        if not best or s > best[0]:
            best = (s, {"ma": m["ma"], "phan_he": ph, "duong_dan": m["path"]})
    return best[1] if best else None


def _node(g, fn):
    d = g["data"][fn]
    return {"ten_file": fn, "ten": d["t"], "tao_o": d["src"], "menu_tao": d["menu"], "ghi_chu": "Du-lieu/" + fn + ".md"}


def t_kb_phan_tich(S, a):
    base, _ = kb_dir(S)
    g = kb_graph.build(base)
    mod = str(a.get("phan_he") or "").upper().strip()
    mod = kb_graph.CAT_PH.get(mod, mod)
    text = str(a.get("van_ban") or "")
    menu = find_menu(S, text, mod)
    hits = kb_graph.query_text(g, text + ("\n" + menu["duong_dan"].split("/")[-1] if menu else ""), mod)
    top = hits[0][1] if hits else 0
    focus = [h for h in hits if h[1] >= max(3, top * 0.6)][:3]
    F = [h[0] for h in focus]
    F = [x for x in F if not any(o != x and x in kb_graph.walk(g, o, True) for o in F)]
    guess = False
    if not F and mod:
        own = sorted([k for k, d in g["data"].items() if d["src"] == mod], key=lambda k: -g["data"][k]["lv"])
        F, guess = own[:1], bool(own)
    req, seen = [], set()
    for fn in F:
        for r, why in g["data"][fn]["req"]:
            if r not in F and r not in seen:
                seen.add(r)
                req.append(dict(_node(g, r), vi_sao=why, cho=fn))
    chain = []
    for fn in F:
        for x in kb_graph.walk(g, fn, True):
            if x not in F and x not in chain:
                chain.append(x)
    chain.sort(key=lambda x: (g["data"][x]["lv"], x))
    nxt = []
    for fn in F:
        for x in kb_graph.walk(g, fn, False):
            if x not in F and x not in nxt and any(r[0] == fn for r in g["data"][x]["req"]):
                nxt.append(x)
    uses = []
    for fn in F:
        for m, why in g["data"][fn]["use"]:
            if m != g["data"][fn]["src"] and not any(u["phan_he"] == m for u in uses):
                uses.append({"phan_he": m, "viec": why, "du_lieu": fn})
    mods = g["mods"]
    return {
        "phan_he": {"ma": mod, "ten": mods.get(mod, [""])[0], "test_tren": mods.get(mod, ["", []])[1]} if mod else None,
        "menu_khop": menu,
        "du_lieu_case": [dict(_node(g, fn), web=g["data"][fn]["web"]) for fn in F],
        "doan_theo_phan_he": guess,
        "phai_co_truoc": req,
        "chuoi_chuan_bi": [dict(_node(g, x)) for x in chain],
        "anh_huong_du_lieu": [dict(_node(g, x), lay_tu=[r[0] for r in g["data"][x]["req"] if r[0] in F]) for x in nxt],
        "anh_huong_phan_he": uses,
        "goi_y": "prep = môi trường + phai_co_truoc (ghi menu_tao); reg = anh_huong_du_lieu (nếu sửa số liệu) hoặc các trang web hiện cùng dữ liệu (nếu sửa giao diện web). "
                 "Đọc thêm Phan-he/<mã>.md và Cach-test/ trước khi chốt.",
    }


def t_kb_du_lieu(S, a):
    base, _ = kb_dir(S)
    g = kb_graph.build(base)
    q = str(a.get("ten") or "").strip()
    fn = q if q in g["data"] else next((k for k, d in g["data"].items() if q.lower() in (k + " " + d["t"]).lower()), None)
    if not fn:
        raise ToolError("Không thấy dữ liệu '" + q + "'. Có: " + ", ".join(sorted(g["data"])))
    d = g["data"][fn]
    return dict(_node(g, fn), tang=d["lv"], tren_web=d["web"], phai_co_truoc=[{"ten_file": r, "vi_sao": w} for r, w in d["req"]],
                chuoi_chuan_bi=kb_graph.walk(g, fn, True), la_dieu_kien_cho=[k for k, x in g["data"].items() if any(r[0] == fn for r in x["req"])],
                sinh_ra_ve_sau=kb_graph.walk(g, fn, False), dung_o=[{"phan_he": m, "viec": w} for m, w in d["use"]])


# ------------------------------------------------------------------ ACS (chỉ đọc, qua cầu nối của app)
def acs(method, path, body=None):
    url, tok = os.environ.get("AQ_ACS_RELAY"), os.environ.get("AQ_ACS_TOKEN")
    if not url or not tok:
        raise ToolError("Đọc ACS chỉ có khi chạy trong app AQ Auto Test (máy cá nhân).")
    req = urllib.request.Request(url.rstrip("/") + "/acs", data=json.dumps({"method": method, "path": path, "body": body}).encode("utf-8"),
                                 headers={"Content-Type": "application/json", "X-AQ-Token": tok}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            res = json.loads(r.read().decode("utf-8") or "{}")
    except urllib.error.HTTPError as e:
        raise ToolError("Cầu nối ACS từ chối: " + e.read().decode("utf-8", errors="replace")[:300])
    except OSError as e:
        raise ToolError("Không gọi được cầu nối ACS của app: %s" % e)
    if res.get("error"):
        raise ToolError(res["error"])
    if res.get("status") in (401, 403):
        raise ToolError("Chưa đăng nhập ACS – mở app AQ Auto Test → Test case ACS → bấm Đăng nhập ACS, rồi thử lại.")
    return res


def html_text(v):
    v = str(v or "")
    if not re.search(r'<[a-z!/][^>]*>', v, re.I):
        return v.strip()
    v = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', v)
    v = re.sub(r'(?i)<img\b[^>]*>', ' [ảnh] ', v)
    v = re.sub(r'(?i)<br\s*/?>|</(p|div|li|tr|h\d)>', '\n', v)
    v = re.sub(r'<[^>]+>', ' ', v)
    for k, x in (("&nbsp;", " "), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&#39;", "'"), ("&amp;", "&")):
        v = v.replace(k, x)
    return re.sub(r'[ \t]+', ' ', re.sub(r'\n\s*\n+', '\n\n', v)).strip()


def _flat(o, pre="", dep=0, out=None):
    out = {} if out is None else out
    if isinstance(o, dict) and dep <= 2:
        for k, v in o.items():
            if re.search(r'pass|token|secret|cookie', k, re.I):
                continue
            _flat(v, (pre + "." + k) if pre else k, dep + 1, out)
    elif isinstance(o, list):
        if o and all(not isinstance(x, (dict, list)) for x in o):
            out[pre] = ", ".join(str(x) for x in o)
    elif o is not None and o != "":
        t = html_text(o) if isinstance(o, str) else str(o)
        if t:
            out[pre] = t[:8000]
    return out


def acs_settings(S):
    f = S.doc_file("settings", "acs")
    return (S.read_doc(f) if f.exists() else None) or {}


IMG_MIME_EXT = {v: k for k, v in IMG_MIME.items() if k != ".jpeg"}
ACS_ORIGIN = "https://acs.aqtech.io.vn"
NGUON = {"yeu_cau_kh": "KH", "ba": "BA", "dev": "Dev", "test_truoc": "Test trước", "khac": "Khác"}


def kb_graph_slug(t):
    import unicodedata
    t = str(t).replace("đ", "d").replace("Đ", "D")
    return unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode("ascii").lower()


def _sec_of(key):
    for part in reversed([x for x in key.split(".") if x and not x.isdigit()]):
        for name, rx in SEC:
            if rx.search(part):
                return name
    return "khac"


def _add_file(out, url, name, mime, key):
    url = str(url or "").strip()
    if not url or url.lower().startswith("cid:") or any(x["url"] == url for x in out):
        return
    if url.startswith("data:"):
        loai = "data"
        mime = mime or url[5:].split(";")[0]
    elif url.startswith(ACS_ORIGIN) or url.startswith("/"):
        loai = "acs"
    elif re.match(r'^https?://', url, re.I):
        loai = "ngoai"
    elif re.match(r'^[\w./-]+$', url) and "/" in url:
        loai, url = "acs", "/" + url.lstrip("./")
    else:
        return
    path = urllib.parse.urlparse(url).path if loai != "data" else ""
    is_img = mime.lower().startswith("image/") or bool(re.search(IMG_RX + r'$', path, re.I))
    ten = name or (Path(path).name if path else "ảnh dán") or "tệp"
    sec = _sec_of(key)
    nguon = "Đính kèm" if sec == "khac" and re.search(r'attach|file|dinh_?kem|upload', key, re.I) else NGUON[sec]
    out.append({"url": url, "ten": ten[:120], "mime": mime, "nguon": nguon, "anh": is_img, "loai": loai,
                "trong": key or ""})


def find_files(o, key="", dep=0, out=None):
    """ảnh / file đính kèm trong chi tiết case: <img src> trong nội dung HTML, ![](…), link ảnh, và các object đính kèm (url + tên + loại)"""
    out = [] if out is None else out
    if dep > 7:
        return out
    if isinstance(o, dict):
        ks = list(o.keys())
        url = next((o[k] for k in ks if isinstance(o[k], str) and o[k].strip() and re.search(r'url|path|href|link|src|download|location|uri', k, re.I)
                    and not re.search(r'avatar|icon|logo', k, re.I)), None)
        name = next((str(o[k]) for k in ks if isinstance(o[k], str) and re.match(r'^(file_?name|original_?name|name|title|ten|ten_?file)$', k, re.I)), "")
        mime = next((str(o[k]) for k in ks if isinstance(o[k], str) and re.search(r'content_?type|mime', k, re.I)), "")
        if not mime:
            mime = next((str(o[k]) for k in ks if k.lower() == "type" and isinstance(o[k], str) and "/" in o[k]), "")
        if url and (re.search(r'attach|file|image|img|anh|dinh_?kem|upload|media|photo|screenshot', key, re.I)
                    or re.search(IMG_RX, url, re.I) or mime.startswith("image/")):
            _add_file(out, url, name, mime, key)
        for k, v in o.items():
            if not re.search(r'pass|token|secret|cookie|avatar', k, re.I):
                find_files(v, (key + "." + k) if key else k, dep + 1, out)
    elif isinstance(o, list):
        for v in o:
            find_files(v, key, dep + 1, out)
    elif isinstance(o, str) and re.match(r'^/?[\w./%-]+' + IMG_RX + r'$', o.strip(), re.I) and re.search(r'attach|file|image|img|anh|dinh_?kem|upload|media|photo|screenshot', key, re.I):
        _add_file(out, o.strip(), "", "", key)
    elif isinstance(o, str) and len(o) > 8:
        for m in re.finditer(r'(?is)<img\b[^>]*?\bsrc\s*=\s*["\']([^"\']+)["\'][^>]*>', o):
            alt = re.search(r'(?i)\balt\s*=\s*["\']([^"\']*)', m.group(0))
            _add_file(out, m.group(1), alt.group(1) if alt else "", "", key)
        for m in re.finditer(r'!\[([^\]]*)\]\(([^)\s]+)', o):
            _add_file(out, m.group(2), m.group(1), "", key)
        for m in re.finditer(r'(?i)\bhttps?://[^\s"\'<>]+?' + IMG_RX + r'\b[^\s"\'<>]*', o):
            _add_file(out, m.group(0), "", "", key)
    return out


def fetch_case_image(im, mx=1568):
    """→ (bytes, mime)"""
    if im["loai"] == "data":
        try:
            head, b64 = im["url"].split(",", 1)
            raw = base64.b64decode(b64)
        except ValueError:
            raise ToolError("Ảnh dán trong nội dung bị hỏng")
        mime = head[5:].split(";")[0] or "image/png"
        if len(raw) > 700000 and os.environ.get("AQ_ACS_RELAY"):
            r = acs_image(data=b64, mime=mime, mx=mx)
            return base64.b64decode(r["b64"]), r.get("mime") or mime
        return raw, mime
    if im["loai"] == "ngoai":
        raise ToolError("Ảnh nằm ngoài ACS (%s) – không tải (MCP chỉ đọc ACS). Mở case trên ACS để xem." % urllib.parse.urlparse(im["url"]).netloc)
    r = acs_image(path=im["url"], mx=mx)
    return base64.b64decode(r["b64"]), r.get("mime") or "image/jpeg"


def t_acs_anh(S, a):
    cid = str(a.get("ma_case") or "").strip()
    if not re.match(r'^\d{1,10}$', cid):
        raise ToolError("Mã case phải là số")
    det = get_case(S, cid)
    ims = [f for f in find_files({"case": det, "attachments": list_endpoint(cid, ("/cs/cases/%s/attachments", "/cs/cases/%s/files")) or [],
                                  "mails": list_endpoint(cid, ("/cs/cases/%s/mails", "/cs/cases/%s/emails")) or []}) if f["anh"]]
    if not ims:
        return "Case #%s không có ảnh đọc được trong nội dung / đính kèm." % cid
    so = [int(x) for x in (a.get("so") or []) if str(x).isdigit()] or list(range(1, min(4, len(ims)) + 1))
    content = []
    for n in so[:4]:
        if not 1 <= n <= len(ims):
            content.append({"type": "text", "text": "Không có ảnh số %d (case có %d ảnh)." % (n, len(ims))})
            continue
        im = ims[n - 1]
        try:
            raw, mime = fetch_case_image(im)
            content += [{"type": "text", "text": "Ảnh %d/%d – %s – %s" % (n, len(ims), im["nguon"], im["ten"])}, img_block(raw, mime)]
        except ToolError as e:
            content.append({"type": "text", "text": "Ảnh %d (%s – %s): %s" % (n, im["nguon"], im["ten"], e)})
    rest = [i for i in range(1, len(ims) + 1) if i not in so[:4]]
    if rest:
        content.append({"type": "text", "text": "Còn ảnh %s – acs_anh với so=[…] để xem." % ", ".join(map(str, rest))})
    content.append({"type": "text", "text": "Ghi điều thấy trong ảnh vào phiếu (case_ghi_phan_tich, mục anh). Ảnh khác lời KH → tin ảnh, ghi rõ chỗ khác."})
    return {"_content": content}


def t_acs_toi(S, a):
    r = acs("GET", "/auth/me")
    d = r.get("data") or {}
    return {"ten": d.get("display_name") or d.get("username"), "tai_khoan": d.get("username")}


def t_acs_tim_case(S, a):
    cl = [{"op": c.get("phep"), "conj": "AND", "field": c.get("truong"), "value": c.get("gia_tri")} for c in (a.get("dieu_kien") or [])]
    for c in cl:
        if c["field"] not in RT_COLS or c["op"] not in ("eq", "neq", "in"):
            raise ToolError("Điều kiện không hợp lệ: %s" % c)
    if not cl:
        cl = [{"op": "eq", "conj": "AND", "field": "status", "value": "Đã xử lý"}, {"op": "neq", "conj": "AND", "field": "test_state", "value": "Đúng"}]
    lim = max(1, min(200, int(a.get("gioi_han") or 50)))
    r = acs("POST", "/cs/query", {"clauses": cl, "columns": RT_COLS, "sort": "case_id", "desc": True, "offset": 0, "limit": lim})
    d = r.get("data") or {}
    rows = d.get("rows") if isinstance(d, dict) else d
    if r.get("status") != 200 or not isinstance(rows, list):
        raise ToolError("ACS trả về mã %s" % r.get("status"))
    keep = ("case_id", "title", "school_code", "module", "status", "test_state", "assignee_raw", "tester_raw", "resolved_at", "due_date", "priority")
    return {"tong": d.get("total", len(rows)) if isinstance(d, dict) else len(rows), "case": [{k: x.get(k) for k in keep if x.get(k) not in (None, "")} for x in rows]}


SEC = [("yeu_cau_kh", re.compile(r'customer|request|yeu_?cau|khach|description|desc$|^content|noi_?dung|mo_?ta|problem|issue|question|body|message', re.I)),
       ("ba", re.compile(r'analy|phan_?tich|^ba_|_ba$|requirement|spec|nghiep_?vu|symptom|hien_?tuong', re.I)),
       ("dev", re.compile(r'dev|coder|chi_?tiet|_xl_|response|solution|resolution|resolve|fix|xu_?ly|giai_?phap|reply|answer|tra_?loi|change_?log|cach_?sua|assignee', re.I)),
       ("test_truoc", re.compile(r'test|kiem_?tra', re.I))]
META = ("case_id", "title", "school_code", "module", "case_type", "priority", "status", "assignee_raw", "analyst_raw", "req_state", "tester_raw",
        "test_state", "received_at", "due_date", "resolved_at", "changed")


def clean_mail(t):
    out = []
    for ln in str(t or "").replace("\r", "").split("\n"):
        l = ln.strip()
        if re.match(r'^(-{2,}\s*original message|-{2,}\s*thư gốc|_{6,}|from:|từ:|sent:|đã gửi:|on .{4,120} wrote:|vào .{4,120} đã viết:)', l, re.I) or re.match(r'^(--|—)\s*$', l):
            break
        if re.match(r'^(trân trọng|tran trong|thân ái|kính thư|best regards|kind regards|regards|sincerely)\b[^a-z0-9]{0,4}$', l, re.I):
            break
        out.append(l)
    while out and len(out[0]) < 80 and re.match(r'^(chào|kính gửi|kính chào|xin chào|dear|hi|hello)\b', out[0], re.I):
        out.pop(0)
    return re.sub(r'\n{3,}', '\n\n', "\n".join(out)).strip()


def get_case(S, cid):
    st = acs_settings(S)
    paths = [st["casePath"]] if st.get("casePath") else ["/cs/cases/{id}", "/cs/case/{id}", "/cs/cases/{id}/detail"]
    last = None
    for p in paths:
        r = acs("GET", p.replace("{id}", cid))
        last = r.get("status")
        if r.get("status") == 200 and isinstance(r.get("data"), dict):
            return r["data"]
    raise ToolError("Không đọc được chi tiết case %s (mã %s). Quản trị khai báo 'đường dẫn API chi tiết case' ở tab Thiết lập ACS." % (cid, last))


def split_case(det):
    """chi tiết case ACS → (meta, {yeu_cau_kh, ba, dev, test_truoc, khac})"""
    flat = _flat(det, dep=0)
    meta, sec = {}, {k: [] for k, _ in SEC}
    sec["khac"] = []
    for k, v in flat.items():
        b = k.split(".")[-1]
        if b in META or b.replace("_html", "") in META:
            meta.setdefault(b, v)
            continue
        if re.match(r'^(title|tieu_de|subject|name)$', b, re.I):
            meta.setdefault("title", v)
            continue
        if len(v) < 12 or re.match(r'^\d{4}-\d\d-\d\d', v) or re.match(r'^[\w.\\@-]+$', v):
            continue
        for name, rx in SEC:
            if rx.search(b):
                sec[name].append(("[%s]\n" % k if name != "yeu_cau_kh" else "") + v)
                break
        else:
            sec["khac"].append("[%s] %s" % (k, v[:600]))
    out = {k: "\n\n".join(v) for k, v in sec.items() if k != "khac"}
    out["khac"] = sec["khac"]
    out["yeu_cau_kh"] = clean_mail(out["yeu_cau_kh"])
    return meta, out



# ------------------------------------------------------------------ phiếu case ACS (đủ trường như màn hình case trên ACS)
ACS_FIELDS = [
    ("dau_case", "Trạng thái", r'^(status|trang_?thai|case_?status|state)$'), ("dau_case", "Phân công", r'^(assignee(_raw|_name)?|assigned_?to|phan_?cong|handler|owner(_name)?)$'),
    ("dau_case", "Hạn trả", r'^(due_?date|deadline|han(_?tra)?|due_?at)$'), ("dau_case", "Cổng CST", r'cst|portal|cong_?kh|show_?customer|public'),
    ("dau_case", "Liên quan", r'^(related|lien_?quan|linked?_?cases?|related_?cases?)$'), ("dau_case", "Cập nhật bởi", r'^(updated_?by|changed_?by|modified_?by|last_?editor)$'),
    ("dau_case", "Cập nhật lúc", r'^(changed|updated_?at|modified_?at|last_?modified)$'),
    ("quy_trinh", "Tiếp nhận", r'^(received_?by|creator|created_?by|receiver|tiep_?nhan(_by)?|nguoi_?tiep_?nhan)$'), ("quy_trinh", "Tiếp nhận lúc", r'^(received_?at|created_?at|ngay_?tiep_?nhan)$'),
    ("quy_trinh", "BA phân tích", r'^(analyst(_raw|_name)?|ba(_raw|_name)?|nguoi_?phan_?tich)$'), ("quy_trinh", "Trạng thái BA", r'^(req_?state|analysis_?state|ba_?state)$'),
    ("quy_trinh", "DEV xử lý", r'^(dev(eloper)?(_raw|_name)?|coder(_raw|_name)?|nguoi_?xu_?ly)$'), ("quy_trinh", "Xử lý xong", r'^(resolved_?at|fixed_?at|dev_?done_?at)$'),
    ("quy_trinh", "Kiểm thử", r'^(tester(_raw|_name)?|qa(_raw)?|nguoi_?test)$'), ("quy_trinh", "Kết quả test", r'^(test_?state|test_?result|ket_?qua_?test)$'),
    ("quy_trinh", "Gửi email & Đóng", r'^(mail_?state|email_?state|closed_?at|close_?state|sent_?at|mail_?sent(_at)?)$'),
    ("khach_hang", "Khách hàng", r'^(customer(_name)?|khach_?hang|school_?name|unit_?name|org(_name)?|don_?vi|customer_?label)$'),
    ("khach_hang", "Mã trường", r'^(school_?code|customer_?code|ma_?truong)$'), ("khach_hang", "Phân hệ", r'^(module|phan_?he|module_?code)$'),
    ("khach_hang", "Danh xưng", r'^(salutation|danh_?xung|honorific|prefix)$'), ("khach_hang", "Tên", r'^(contact_?name|requester(_name)?|ten(_?kh|_?lien_?he)?|customer_?contact)$'),
    ("khach_hang", "Mail To", r'^(mail_?to|email_?to|to|requester_?email|contact_?email)$'), ("khach_hang", "Mail CC", r'^(mail_?cc|email_?cc|cc)$'),
    ("khach_hang", "Loại hợp đồng", r'^(contract_?type|loai_?hop_?dong|loai_?hd)$'), ("khach_hang", "Số hợp đồng", r'^(contract_?(no|number|code)|so_?hop_?dong|so_?hd)$'),
    ("khach_hang", "Ngày hợp đồng", r'^(contract_?date|ngay_?hop_?dong|ngay_?hd)$'), ("khach_hang", "Loại case", r'^(case_?type|loai_?case|type)$'),
    ("khach_hang", "Mức ưu tiên", r'^(priority|uu_?tien|muc_?uu_?tien)$')]


def flat_all(o, pre="", dep=0, out=None):
    """mọi giá trị ngắn của case (kể cả số, ngày, đối tượng có name/label) → {đường dẫn: giá trị}; danh sách đối tượng → 'đường dẫn#': số mục"""
    out = {} if out is None else out
    if not isinstance(o, dict) or dep > 4:
        return out
    nm = lambda v: next((v[k] for k in ("display_name", "name", "label", "full_name", "username", "email", "code") if isinstance(v, dict) and v.get(k)), None)
    for k, v in o.items():
        if re.search(r'pass|token|secret|cookie', k, re.I) or v in (None, ""):
            continue
        key = (pre + "." + k) if pre else k
        if isinstance(v, list):
            if v and all(not isinstance(z, (dict, list)) for z in v):
                out[key] = ", ".join(str(z) for z in v)
            elif v and all(nm(z) for z in v):
                out[key] = ", ".join(str(nm(z)) for z in v)
            else:
                out[key + "#"] = len(v)
        elif isinstance(v, dict):
            n = nm(v)
            if n is not None and len(v) <= 6:
                out[key] = n
            else:
                flat_all(v, key, dep + 1, out)
        else:
            out[key] = v
    return out


def case_sheet(det, hist, att, mails):
    allv = flat_all(det)
    F, used = {}, set()
    for sec, lab, rx in ACS_FIELDS:
        ks = sorted([k for k in allv if re.search(rx, k.split(".")[-1].rstrip("#"), re.I)], key=lambda k: k.count("."))
        if ks and lab not in F:
            v = allv[ks[0]]
            F[lab] = ("%d mục" % v if v else "chưa có") if ks[0].endswith("#") else html_text(v)[:300] if isinstance(v, str) else v
            used.add(ks[0])
    out = {sec: {lab: F[lab] for s2, lab, _ in ACS_FIELDS if s2 == sec and lab in F} for sec in ("dau_case", "quy_trinh", "khach_hang")}
    cnt = lambda rx: next((v for k, v in allv.items() if k.endswith("#") and re.search(rx, k, re.I)), None)
    out["tab"] = {"gui_mail": len(mails) if mails is not None else cnt(r'mail|email'), "lich_su": len(hist),
                  "dinh_kem": len(att) if att is not None else cnt(r'attach|file|dinh_?kem')}
    out["truong_khac"] = {k: v for k, v in allv.items() if k not in used and not k.endswith("#") and not re.search(r'^(title|case_id|id|subject)$', k.split(".")[-1], re.I)
                          and len(str(v)) <= 80 and "\n" not in str(v)}
    return out, F


def list_endpoint(cid, paths):
    for p in paths:
        try:
            r = acs("GET", p % cid)
        except ToolError:
            continue
        d = r.get("data")
        L = d if isinstance(d, list) else next((d.get(k) for k in ("items", "rows", "data", "attachments", "files", "mails", "emails") if isinstance(d, dict) and isinstance(d.get(k), list)), None)
        if r.get("status") == 200 and isinstance(L, list):
            return L
    return None


def t_acs_case(S, a):
    cid = str(a.get("ma_case") or "").strip()
    if not re.match(r'^\d{1,10}$', cid):
        raise ToolError("Mã case phải là số")
    det = get_case(S, cid)
    meta, sec = split_case(det)
    hist = []
    try:
        h = acs("GET", "/cs/cases/%s/history" % cid)
        hd = h.get("data")
        hl = hd.get("history") if isinstance(hd, dict) else hd
        for x in (hl or [])[:40]:
            if isinstance(x, dict):
                hist.append({"luc": x.get("changed_at"), "boi": x.get("changed_by"), "thay_doi": _flat(x.get("changes") or {})})
    except ToolError:
        pass
    tdoi = []                                     # trao đổi trên case (kênh test = nội dung tester các lần trước – lỗi lần trước phải kiểm lại)
    try:
        r = acs("GET", "/cs/cases/%s/comments" % cid)
        cl = r.get("data").get("comments") if isinstance(r.get("data"), dict) else None
        for x in (cl or [])[-20:]:
            if isinstance(x, dict):
                h = ((x.get("edits") or [{}])[-1] or {}).get("html") or x.get("html") or ""
                t = re.sub(r'\n{3,}', '\n\n', re.sub(r'<[^>]+>', '\n', re.sub(r'<img[^>]*>', '[ảnh]', h))).strip()
                tdoi.append({"luc": x.get("created_at"), "boi": x.get("author"), "kenh": x.get("kenh"), "noi_dung": t[:1500]})
    except (ToolError, AttributeError):
        pass
    base, _ = kb_dir(S)
    g = kb_graph.build(base)
    sma, sx, pcc, pcn = kb_graph.school_of(g, meta.get("school_code"))
    mod = kb_graph.CAT_PH.get(str(meta.get("module") or "").upper(), str(meta.get("module") or "").upper())
    title = meta.get("title") or ""
    allt = title + "\n" + sec["yeu_cau_kh"] + "\n" + sec["ba"] + "\n" + sec["dev"]
    refs = sorted({x for x in re.findall(r'\[(\d{5,6})\]', title + " " + sec["yeu_cau_kh"]) if x != cid})
    build = re.search(r'\bv?(20\d\d\.\d{1,2}[A-Z]{0,2}\.\d{1,3})\b', sec["dev"] + "\n" + json.dumps(hist, ensure_ascii=False))
    repo = re.search(r'VersionSchool/[\w.-]+/[\w./-]+|Source\.NET[\w./-]*', allt)
    pats = kb_graph.patterns_of(g, title + "\n" + sec["yeu_cau_kh"], sec["ba"], sec["dev"], mod)
    att = list_endpoint(cid, ("/cs/cases/%s/attachments", "/cs/cases/%s/files"))
    mails = list_endpoint(cid, ("/cs/cases/%s/mails", "/cs/cases/%s/emails"))
    sheet, F = case_sheet(det, hist, att, mails)
    files = find_files({"case": det, "attachments": att or [], "mails": mails or []})
    ims = [f for f in files if f["anh"]]
    chk = [{"muc": "Trường / phân cấp", "du": bool(meta.get("school_code") or F.get("Mã trường"))},
           {"muc": "Phân hệ", "du": bool(meta.get("module") or F.get("Phân hệ"))},
           {"muc": "Yêu cầu khách hàng", "du": bool(sec["yeu_cau_kh"])},
           {"muc": "BA phân tích", "du": bool(sec["ba"]), "ghi_chu": "" if sec["ba"] else "chưa có – hỏi BA trước khi test"},
           {"muc": "Dev đã xử lý", "du": bool(sec["dev"])},
           {"muc": "Bản sửa (build)", "du": bool(build), "ghi_chu": "" if build else "hỏi Dev bản nào đã lên môi trường test"},
           {"muc": "Hạn trả", "du": bool(F.get("Hạn trả"))},
           {"muc": "Người test", "du": bool(F.get("Kiểm thử"))}]
    return {
        "ma_case": cid, "tieu_de": title,
        "truong": dict({"school_code": meta.get("school_code"), "truong": sma, "ghi_chu": "Truong/%s.md" % sma, "ten": sx["ten"], "xac_nhan": sx["xac_nhan"],
                       "mo_hinh": ({"ghi_chu": "Case-truong/%s.md" % sma, **sx["mh"]} if sx.get("mh") else
                                   "chưa có Case-truong/%s.md – chạy truong_hoc_case '%s' để học các case cũ của trường" % (sma, sma))},
                       **({"phan_cap": pcc, "ten_phan_cap": pcn or "(chưa có trong phan_cap – hỏi người dùng)",
                           "luu_y": "Case theo phân cấp – chỉ hiệu lực trên phân cấp này, test đúng site / dữ liệu của phân cấp."} if pcc else
                          {"luu_y": "Mã 4 ký tự = case chung của trường."})) if sma else
                  {"school_code": meta.get("school_code"), "ghi_chu": None,
                   "luu_y": "Chưa có ghi chú Truong/ cho mã này (4 ký tự đầu = mã trường) – không đoán tên trường; hỏi người dùng rồi thêm ghi chú."},
        "phan_he": {"ma": mod, "ten": g["mods"].get(mod, [""])[0], "ghi_chu": "Phan-he/%s.md" % mod if mod in g["mods"] else None},
        "thong_tin": {k: v for k, v in meta.items() if k not in ("title",)},
        "yeu_cau_kh": sec["yeu_cau_kh"] or "(không đọc được nội dung KH – xem 'khac')",
        "ba": sec["ba"] or "(chưa có phần BA phân tích)",
        "dev": sec["dev"] or "(chưa có ghi chú dev)",
        "ghi_chu_test_truoc": sec["test_truoc"], "khac": sec["khac"][:20],
        "ban_sua": build.group(1) if build else None, "repo": repo.group(0) if repo else None,
        "case_goc": refs, "goi_y_dang_case": [{"dang": p, "ghi_chu": "Dang-case/%s.md" % p, "vi": w} for p, _, w in pats[:3]],
        "phieu_acs": sheet, "kiem_tra_du": chk,
        "luong_test": (lambda fl: {"ghi_chu": "Luong-test/%s.md" % fl[0], "ten": fl[1]["ten"], "can_cung_cap": fl[1]["can"], "buoc": fl[1]["buoc"]} if fl[0] else None)(
            kb_graph.flow_of(g, title + "\n" + sec["yeu_cau_kh"], mod)),
        "trao_doi_test": tdoi,
        "cach_test": [{"ghi_chu": "Cach-test/%s.md" % fn, "ten": x["ten"], "buoc": x["buoc"], "kiem_tra": x["kt"], "khong_anh_huong": x["kah"]}
                      for fn, x in kb_graph.tests_of(g, allt)],
        "trang_web": [{"ghi_chu": "Web/%s.md" % fn, "ten": w["t"], "vai_tro": w["vt"], "doc": w["doc"], "ghi_nguoc": w["ghi"], "chinh_dinh": w["cd"]}
                      for fn, w in kb_graph.webs_of(g, title + "\n" + sec["yeu_cau_kh"])],   # liên kết Netweb ↔ Edusoft: kb/00 Liên kết Netweb - Edusoft.md
        "anh": [{"so": i + 1, "nguon": f["nguon"], "ten": f["ten"], "xem_duoc": f["loai"] != "ngoai"} for i, f in enumerate(ims)],
        "dinh_kem_khac": [{"ten": f["ten"], "nguon": f["nguon"]} for f in files if not f["anh"]][:20],
        "dien_bien": hist,
        "tiep_theo": ("Kiểm tra phiếu ACS: thiếu %s – nêu cho người dùng trước. " % ", ".join(x["muc"] for x in chk if not x["du"]) if any(not x["du"] for x in chk) else "") + ("Case có %d ảnh – XEM bằng acs_anh trước khi kết luận hiện trạng (ảnh cho thấy đúng màn hình / chỗ lỗi). " % len(ims) if ims else "") + "Phân tích theo '00 Cách phân tích case.md': trường → phân hệ → KH → BA → Dev → đối chiếu → dạng case → dữ liệu (kb_phan_tich) → acs_case_lien_quan → case_ghi_phan_tich.",
    }


def _query(cl, lim):
    r = acs("POST", "/cs/query", {"clauses": cl, "columns": list(META), "sort": "case_id", "desc": True, "offset": 0, "limit": lim})
    d = r.get("data") or {}
    rows = d.get("rows") if isinstance(d, dict) else d
    return rows if r.get("status") == 200 and isinstance(rows, list) else []


STOPW = set("các của cho trong không được hiển thị khi với những này đã đang theo từ một hai lần như vào thì nên phải cần bên trường sinh viên chức năng màn hình thông tin dữ liệu danh sách kiểm tra lỗi sửa xem thêm xóa lưu bấm mở chọn giúp nhờ sau trước menu bản cập nhật đúng sai vẫn nhưng rồi lại và hoặc là có bị ở".split())


def _words(t):
    return {w for w in re.findall(r'[0-9a-zà-ỹđ]{3,}', str(t or "").lower()) if w not in STOPW}


def t_acs_case_lien_quan(S, a):
    cid = str(a.get("ma_case") or "").strip()
    if not re.match(r'^\d{1,10}$', cid):
        raise ToolError("Mã case phải là số")
    lim = max(3, min(40, int(a.get("gioi_han") or 15)))
    det = get_case(S, cid)
    meta, sec = split_case(det)
    base, _ = kb_dir(S)
    g = kb_graph.build(base)
    title, sc, mod = meta.get("title") or "", str(meta.get("school_code") or ""), str(meta.get("module") or "")
    sma, sx, pcc, _ = kb_graph.school_of(g, sc)
    prefix = (sma or sc[:4]).upper() if sc else ""
    refs = sorted({x for x in re.findall(r'\[(\d{5,6})\]', title + " " + sec["yeu_cau_kh"]) if x != cid})
    me_w = _words(title + " " + sec["yeu_cau_kh"][:600])
    kmod = kb_graph.CAT_PH.get(mod.upper(), mod.upper())
    me_d = {x[0] for x in kb_graph.query_text(g, title + "\n" + sec["yeu_cau_kh"], kmod)[:3]}
    me_p = {x[0] for x in kb_graph.patterns_of(g, title + "\n" + sec["yeu_cau_kh"], sec["ba"], sec["dev"], kmod)[:2]}
    rows = {}
    def add(lst, tag):
        for x in lst:
            k = str(x.get("case_id"))
            if k and k != cid:
                rows.setdefault(k, (x, set()))[1].add(tag)
    if refs:
        add(_query([{"op": "in", "conj": "AND", "field": "case_id", "value": ", ".join(refs)}], 20), "goc")
    if sc and mod:
        add(_query([{"op": "eq", "conj": "AND", "field": "school_code", "value": sc}, {"op": "eq", "conj": "AND", "field": "module", "value": mod}], 100), "truong_ph")
    if mod:
        add(_query([{"op": "eq", "conj": "AND", "field": "module", "value": mod}], 200), "ph")
    out = []
    for k, (x, tags) in rows.items():
        t = str(x.get("title") or "")
        w = _words(t)
        sim = len(w & me_w) / max(1, len(w | me_w))
        xsc = str(x.get("school_code") or "").upper()
        same_unit = bool(sc) and xsc == sc.upper()                       # cùng mã ACS (cùng trường chung hoặc cùng phân cấp)
        same_school = bool(prefix) and xsc[:4] == prefix                 # cùng trường (có thể khác phân cấp)
        d = {y[0] for y in kb_graph.query_text(g, t, kmod)[:3]}
        p = {y[0] for y in kb_graph.patterns_of(g, t, "", "", kmod)[:2]}
        refd = cid in re.findall(r'\[(\d{5,6})\]', t)
        score = 10 * sim + (12 if "goc" in tags or refd else 0) + (3 if same_unit else 1 if same_school else 0) + 2 * len(d & me_d) + 2 * len(p & me_p)
        why, nen = [], ""
        if "goc" in tags:
            why.append("case gốc (tiêu đề case này có [%s])" % k); nen = "đọc trước: lần trước sửa gì, kết luận test thế nào"
        if refd:
            why.append("case tiếp nối của case này"); nen = nen or "xem lần sau còn yêu cầu gì"
        if same_unit:
            why.append(("cùng phân cấp " + xsc if len(xsc) > 4 else "cùng trường") + (" + cùng phân hệ" if str(x.get("module") or "") == mod else ""))
        elif same_school:
            why.append("cùng trường, KHÁC phân cấp (%s) – thường không ảnh hưởng nhau trừ khi sửa phần chung" % xsc)
        if d & me_d:
            why.append("cùng dữ liệu: " + ", ".join(sorted(d & me_d)))
        if p & me_p:
            why.append("cùng dạng: " + ", ".join(sorted(p & me_p)))
        if sim >= 0.2:
            why.append("tiêu đề giống %d%%" % round(sim * 100))
        if not nen:
            nen = ("test cùng lúc / dùng chung dữ liệu" if same_unit and str(x.get("status") or "") == "Đã xử lý" else
                   "xem cùng đợt KH gửi" if same_unit else
                   "tham khảo – phân cấp khác của cùng trường" if same_school else "tham khảo cách sửa; nếu sửa phần dùng chung thì kiểm ảnh hưởng trường này")
        if score < 3 and not same_unit:
            continue
        if score < 2:
            continue
        out.append({"ma": k, "tieu_de": t, "truong": x.get("school_code"), "phan_he": x.get("module"), "trang_thai": x.get("status"),
                    "test": x.get("test_state"), "xu_ly_luc": x.get("resolved_at"), "diem": round(score, 1), "vi": why or ["cùng phân hệ"], "nen": nen})
    out.sort(key=lambda o: -o["diem"])
    return {"case": {"ma": cid, "tieu_de": title, "truong": sc, "phan_he": mod}, "da_quet": len(rows), "lien_quan": out[:lim],
            "nhac": "Đây là xếp hạng theo dấu hiệu (tiêu đề, trường, phân hệ, dữ liệu, dạng case). Mở acs_case các case đầu danh sách để xác nhận trước khi gợi ý cho người dùng."}


def t_case_ghi_phan_tich(S, a):
    cid = str(a.get("ma_case") or "").strip()
    if not re.match(r'^\d{1,10}$', cid):
        raise ToolError("Mã case phải là số")
    if SECRET.search(json.dumps(a, ensure_ascii=False)):
        raise ToolError("Nội dung có vẻ chứa mật khẩu / token – bỏ ra rồi ghi lại.")
    keep = ("truong", "phan_he", "kh_thay", "kh_muon", "du_lieu_kh", "loai", "ba_chot", "dev_da_lam", "doi_chieu", "dang_case", "du_lieu", "case_lien_quan", "cau_hoi_mo", "anh")
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    doc = {k: a[k] for k in keep if a.get(k) not in (None, "", [])}
    doc.update({"caseId": cid, "by": "claude", "at": now, "updatedAt": now})
    if len(json.dumps(doc, ensure_ascii=False)) > 60000:
        raise ToolError("Phiếu quá dài – viết gọn lại.")
    with S.LOCK:
        S.write_doc(S.doc_file("caseAnalyses", "c" + cid), doc)
    return {"ok": True, "thong_bao": "Đã lưu phiếu phân tích case #%s – người test xem ở app: Test case ACS → case #%s → bước 1." % (cid, cid)}


def t_case_doc_phan_tich(S, a):
    cid = str(a.get("ma_case") or "").strip()
    f = S.doc_file("caseAnalyses", "c" + cid)
    return S.read_doc(f) if f.exists() else {"co": False, "nhac": "Chưa có phiếu phân tích – làm theo 00 Cách phân tích case.md rồi case_ghi_phan_tich."}


# ------------------------------------------------------------------ plan test nháp
def latest_retest(S, cid):
    best = None
    for x in S.list_docs("retests"):
        d = x["data"]
        if str(d.get("caseId")) == cid and (best is None or (d.get("round") or 1) > (best["data"].get("round") or 1)):
            best = x
    return best


def t_retest_ds(S, a):
    seen = {}
    for x in S.list_docs("retests"):
        d = x["data"]
        k = str(d.get("caseId"))
        if k not in seen or (d.get("round") or 1) > (seen[k].get("round") or 1):
            seen[k] = d
    items = []
    for k, d in sorted(seen.items(), key=lambda kv: str(kv[1].get("updatedAt") or ""), reverse=True)[:80]:
        it = (d.get("plan") or {}).get("items") or []
        items.append({"ma_case": k, "tieu_de": d.get("title"), "truong": d.get("school"), "phan_he": d.get("module"), "trang_thai": d.get("state"),
                      "nen_tang": d.get("platform"), "lan": d.get("round"), "da_test": sum(1 for i in it if i.get("res")), "so_muc": len(it)})
    drafts = [{"ma_case": str(x["data"].get("caseId")), "luc": x["data"].get("updatedAt"), "so_muc": len(x["data"].get("items") or [])}
              for x in S.list_docs("retestDrafts")]
    return {"phieu": items, "plan_nhap": drafts}


def t_retest_doc_plan(S, a):
    cid = str(a.get("ma_case") or "").strip()
    f = S.doc_file("retestDrafts", "c" + cid)
    cur = latest_retest(S, cid)
    return {"plan_nhap": S.read_doc(f) if f.exists() else None, "phieu": cur["data"] if cur else None}


def t_retest_ghi_plan(S, a):
    cid = str(a.get("ma_case") or "").strip()
    if not re.match(r'^\d{1,10}$', cid):
        raise ToolError("Mã case phải là số")
    pf, kind = a.get("nen_tang"), a.get("loai_sua") or ""
    if pf not in PLATFORMS:
        raise ToolError("nen_tang phải là một trong " + ", ".join(PLATFORMS))
    if kind and kind not in KINDS:
        raise ToolError("loai_sua phải là một trong " + ", ".join(KINDS))
    items = []
    for x in a.get("cac_muc") or []:
        g, t = x.get("nhom"), re.sub(r'\s+', ' ', str(x.get("noi_dung") or "")).strip()
        if g not in GROUPS or not t:
            continue
        items.append({"g": g, "t": t[:800]})
    if not any(i["g"] == "check" for i in items):
        raise ToolError("Plan cần ít nhất một mục nhom='check' (kiểm tra theo yêu cầu khách hàng).")
    if len(items) > 40:
        raise ToolError("Tối đa 40 mục")
    order = list(GROUPS)
    items.sort(key=lambda i: order.index(i["g"]))
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    doc = {"caseId": cid, "platform": pf, "kind": kind, "env": str(a.get("moi_truong") or "")[:400], "items": items,
           "why": str(a.get("ly_do") or "")[:1200], "by": "claude", "at": now, "updatedAt": now,
           "inputs": [{"k": str(x.get("ten") or "")[:40], "why": str(x.get("vi_sao") or "")[:200]} for x in (a.get("can_cung_cap") or []) if isinstance(x, dict) and x.get("ten")][:8]}
    if any(re.search(r'mật\s*khẩu|password', x["k"], re.I) for x in doc["inputs"]):
        raise ToolError("can_cung_cap chỉ hỏi mã tài khoản / dữ liệu – không hỏi mật khẩu.")
    with S.LOCK:
        S.write_doc(S.doc_file("retestDrafts", "c" + cid), doc)
    cur = latest_retest(S, cid)
    has_an = S.doc_file("caseAnalyses", "c" + cid).exists()
    note = "Đã ghi plan nháp cho case #%s (%d mục). Người test mở app → Test case ACS → chọn case #%s → bước 2 Plan test để duyệt rồi Nhận test." % (cid, len(items), cid)
    if cur and cur["data"].get("state") in ("testing", "queued", "running", "review"):
        note += " Lưu ý: case đang có phiếu test (" + str(cur["data"].get("state")) + ") – plan nháp không thay phiếu đang test; nói người test đối chiếu và sửa plan của phiếu nếu cần."
    if not has_an:
        note += " CHÚ Ý: chưa có phiếu phân tích case này – nên phân tích (case_ghi_phan_tich) trước để plan đúng nghiệp vụ."
    return {"ok": True, "thong_bao": note}


# ------------------------------------------------------------------ mô hình trường (học từ case ACS)
PII = [(re.compile(r'[\w.+-]+@[\w-]+(?:\.[\w-]+)+'), '[email]'), (re.compile(r'(?<!\d)(?:\+?84|0)\d{9,10}(?!\d)'), '[sđt]'),
       (re.compile(r'(?<!\d)\d{7,}(?!\d)'), '[mã]'), (re.compile(r'\b(?:SV|sinh viên|GV|giảng viên)\s*:?\s*([A-ZĐ][a-zà-ỹ]+(?:\s+[A-ZĐ][a-zà-ỹ]+){1,4})'), lambda m: m.group(0).replace(m.group(1), '[tên]'))]
MH_A, MH_B = "<!-- tu-dong:bat-dau – phần dưới do công cụ truong_hoc_case ghi lại mỗi lần học case, đừng sửa tay -->", "<!-- tu-dong:het -->"


def mask(t):
    """che dữ liệu cá nhân trong tiêu đề case trước khi ghi vào KB (KB lên git): email, số điện thoại, mã ≥ 7 số (MSSV…), tên sau SV/GV"""
    t = str(t or "").replace("|", "/").replace("\n", " ").strip()
    for rx, rep in PII:
        t = rx.sub(rep, t)
    return t[:160]


def _day(v):
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})', str(v or ""))
    return "%s-%s-%s" % m.groups() if m else ""


def _qt_of(base, g=None):
    """→ (phân hệ → quy trình, dữ liệu → quy trình). Dữ liệu thuộc quy trình có phân hệ chính là nơi TẠO dữ liệu đó."""
    by_mod, by_data, cand = {}, {}, {}
    d = Path(base) / "Quy-trinh"
    D = (g or {}).get("data") or {}
    for f in sorted(d.glob("[0-9][0-9] *.md")) if d.is_dir() else []:
        p, _ = kb_graph.parse_note(f.read_text("utf-8", errors="replace"))
        ph = kb_graph.links(p.get("phan_he"))
        for m in ph[:3]:                                    # 3 phân hệ đầu = phân hệ chính của quy trình
            by_mod.setdefault(m, f.stem)
        for x in kb_graph.links(p.get("du_lieu")):
            cand.setdefault(x, []).append((f.stem, ph[:3]))
    for x, lst in cand.items():
        src = (D.get(x) or {}).get("src")
        best = [q for q, ph in lst if src and src in ph]
        by_data[x] = (best or [lst[0][0]])[0]
    return by_mod, by_data


TERMS = ("học phí miễn giảm đăng ký môn học học kỳ điểm danh ghi chú tín chỉ thời gian nhập học tuyển sinh tốt nghiệp học vụ học bổng rèn luyện lịch thi "
         "khóa biểu thời khóa giảng viên nhóm học phân quyền tài khoản báo cáo mẫu in phiếu thu công nợ chính sách quét mã chương trình đào tạo "
         "kế hoạch giảng dạy khảo sát đánh giá ký túc cải thiện thi lại phúc khảo luận văn đề tài trúng tuyển xét tuyển hồ sơ học phần tiên quyết "
         "rút môn số liệu tổng kết trung bình tích lũy bảng điểm phiếu điểm ngân hàng thanh toán hóa đơn biên lai điểm thi nhập điểm cố vấn "
         "phụ huynh quyết định văn bằng chứng chỉ phòng học lớp học diện chính sách thu chi khối lượng thời hạn trang web").split()
TERMS = {TERMS[i] + " " + TERMS[i + 1] for i in range(0, len(TERMS) - 1, 2)}


def topics(titles):
    """chủ đề lặp lại trong tiêu đề: cụm nghiệp vụ quen (TERMS) trước, rồi cụm 2 tiếng khác không chồng lên cụm đã nhận"""
    cnt = {}
    for t in titles:
        toks = re.findall(r'[a-zà-ỹđ]+', re.sub(r'\[\d+\]|\d+', ' ', str(t or "").lower()).replace("khoá", "khóa").replace("hoá", "hóa"))
        used, seen = set(), set()
        for i in range(len(toks) - 1):
            k = toks[i] + " " + toks[i + 1]
            if k in TERMS and i not in used and k not in seen:
                used |= {i, i + 1}
                seen.add(k)
                cnt[k] = cnt.get(k, 0) + 1
        for i in range(len(toks) - 1):
            a, b = toks[i], toks[i + 1]
            if i in used or i + 1 in used or a in STOPW or b in STOPW or len(a) < 2 or len(b) < 2:
                continue
            k = a + " " + b
            if k not in seen:
                seen.add(k)
                cnt["~" + k] = cnt.get("~" + k, 0) + 1
    return {k.lstrip("~"): v for k, v in cnt.items() if not k.startswith("~") or v >= 3}


def school_key(g, code):
    sma, _, pcc, _ = kb_graph.school_of(g, code)
    c = str(code or "").strip().upper()
    return sma or (c[:4] if len(c) >= 4 else c), (pcc or (c if len(c) > 4 else ""))


def school_model(S, g, base, ma, rows, analyses=None, retests=None):
    """→ (nội dung ghi chú Case-truong/<ma>.md, tóm tắt). rows = case ACS của trường (mọi phân cấp)."""
    qt, qtd = _qt_of(base, g)
    sx = (g.get("schools") or {}).get(ma) or {}
    by_mod, by_pc, by_dang, by_data, chains = {}, {}, {}, {}, []
    items = []
    for x in rows:
        cid, t = str(x.get("case_id") or ""), str(x.get("title") or "")
        mod = str(x.get("module") or "").upper() or "?"
        kmod = kb_graph.CAT_PH.get(mod, mod)
        pc = str(x.get("school_code") or "").upper()
        dang = [p[0] for p in kb_graph.patterns_of(g, t, "", "", kmod)[:1]]
        an = (analyses or {}).get(cid) or {}
        if an.get("dang_case"):
            dang = [str(d) for d in an["dang_case"]][:2]
        data = [d[0] for d in kb_graph.query_text(g, t, kmod)[:2]]
        by_mod.setdefault(mod, []).append(cid)
        by_pc[pc] = by_pc.get(pc, 0) + 1
        for d in dang:
            by_dang[d] = by_dang.get(d, 0) + 1
        for d in data:
            by_data[d] = by_data.get(d, 0) + 1
        for r in re.findall(r'\[(\d{5,6})\]', t):
            chains.append((r, cid))
        rt = (retests or {}).get(cid) or {}
        q = qtd.get(data[0]) if data else None
        items.append({"q": q or qt.get(kmod), "id": cid, "ngay": _day(x.get("received_at") or x.get("resolved_at")), "pc": pc, "mod": mod, "t": mask(t),
                      "dang": dang, "data": data, "st": str(x.get("status") or ""), "test": str(x.get("test_state") or rt.get("state") or ""),
                      "an": bool(an)})
    items.sort(key=lambda o: (o["ngay"], o["id"]), reverse=True)
    ngay = [o["ngay"] for o in items if o["ngay"]]
    top = lambda d, n: sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))[:n]
    mods = sorted(by_mod.items(), key=lambda kv: -len(kv[1]))
    today = datetime.date.today().isoformat()
    L = lambda v: '"%s"' % str(v).replace('"', "'")
    fm = ["---", "loai: case-truong", "ma: " + ma, "truong: \"[[%s]]\"" % ma, "tong_case: %d" % len(items),
          "tu_ngay: " + (min(ngay) if ngay else ""), "den_ngay: " + (max(ngay) if ngay else ""),
          "phan_cap:"] + ["  - " + L("%s (%d)" % (k or ma, v)) for k, v in sorted(by_pc.items(), key=lambda kv: -kv[1])] + \
         ["phan_he_nhieu:"] + ["  - " + L("%s (%d)" % (k, len(v))) for k, v in mods[:6]] + \
         ["dang_nhieu:"] + (["  - " + L("%s (%d)" % kv) for kv in top(by_dang, 5)] or []) + \
         ["du_lieu_nhieu:"] + (["  - " + L("%s (%d)" % kv) for kv in top(by_data, 6)] or []) + \
         ["cap_nhat: " + today, "nguon: acs", "tags: [case-truong]", "---"]
    A = []
    A.append("## Tổng quan (%d case%s)" % (len(items), (" · %s → %s" % (min(ngay), max(ngay))) if ngay else ""))
    A.append("| Phân hệ | Số case | Quy trình | Dạng hay gặp | Case gần nhất |")
    A.append("|---|---|---|---|---|")
    for mod, ids in mods:
        dd = {}
        for o in items:
            if o["mod"] == mod:
                for d in o["dang"]:
                    dd[d] = dd.get(d, 0) + 1
        k = kb_graph.CAT_PH.get(mod, mod)
        qs = []
        for o in items:
            if o["mod"] == mod and o["q"] and o["q"] not in qs:
                qs.append(o["q"])
        A.append("| %s | %d | %s | %s | %s |" % ("[[%s]]" % k if k in (g.get("mods") or {}) else mod, len(ids), ", ".join("[[%s]]" % q for q in qs[:3]) or "—",
                                               ", ".join("[[%s]] (%d)" % kv for kv in top(dd, 3)) or "—", ", ".join("#" + i for i in ids[:4])))
    if len(by_pc) > 1 or any(k and k != ma for k in by_pc):
        A += ["", "**Theo phân cấp** (case theo phân cấp chỉ hiệu lực trên phân cấp đó): " +
              ", ".join("%s %d%s" % (k or ma, v, (" (%s)" % sx.get("phan_cap", {}).get(k)) if sx.get("phan_cap", {}).get(k) else "") for k, v in sorted(by_pc.items(), key=lambda kv: -kv[1]))]
    if by_data:
        A += ["", "**Dữ liệu hay đụng tới:** " + ", ".join("[[%s]] (%d)" % kv for kv in top(by_data, 8))]
    rep = [(w, n) for w, n in top(topics([x.get("title") for x in rows]), 14) if n >= 2]
    if rep:
        A += ["", "**Chủ đề lặp lại trong tiêu đề:** " + ", ".join("%s (%d)" % kv for kv in rep)]
    if chains:
        A += ["", "**Case tiếp nối** (case gốc → case sau): " + ", ".join("#%s → #%s" % c for c in chains[:20])]
    A += ["", "## Danh sách case (mới nhất trước, tối đa 150)", "| Case | Ngày | Phân cấp | Phân hệ | Tiêu đề | Dạng | Trạng thái | Test |", "|---|---|---|---|---|---|---|---|"]
    for o in items[:150]:
        A.append("| #%s%s | %s | %s | %s | %s | %s | %s | %s |" % (o["id"], " 📝" if o["an"] else "", o["ngay"], o["pc"] or ma, o["mod"], o["t"],
                                                                 ", ".join("[[%s]]" % d for d in o["dang"]) or "—", o["st"], o["test"] or ""))
    A += ["", "📝 = đã có phiếu phân tích trong app (MCP `case_doc_phan_tich`). Tiêu đề đã che email / số điện thoại / mã ≥ 7 số / tên sau SV, GV."]
    auto = "\n".join(A)
    summ = {"ma": ma, "tong_case": len(items), "phan_he_nhieu": ["%s (%d)" % (k, len(v)) for k, v in mods[:6]],
            "dang_nhieu": ["%s (%d)" % kv for kv in top(by_dang, 5)], "phan_cap": dict(by_pc), "den_ngay": max(ngay) if ngay else ""}
    return fm, auto, summ


def write_school_model(S, base, g, ma, rows, analyses=None, retests=None):
    fm, auto, summ = school_model(S, g, base, ma, rows, analyses, retests)
    d = Path(base) / "Case-truong"
    d.mkdir(parents=True, exist_ok=True)
    f = d / ("%s.md" % ma)
    keep = ""
    if f.exists():
        cur = f.read_text("utf-8", errors="replace")
        m = re.search(r'\n## Nhận xét.*?(?=\n' + re.escape(MH_A) + r'|\Z)', cur, re.S)
        keep = m.group(0).strip("\n") if m else ""
    if not keep:
        keep = ("## Nhận xét – mô hình trường (người test / Claude viết, công cụ không ghi đè)\n"
                "- Trường dùng phần mềm thế nào (quy chế, cách tính học phí / điểm, trang web riêng, phân cấp)…\n"
                "- Hay yêu cầu gì, BA thường chốt thế nào, Dev hay sửa ở đâu (VersionSchool/%s?)…\n"
                "- Điều dễ nhầm khi đọc case của trường này…" % ma)
    sx = (g.get("schools") or {}).get(ma) or {}
    head = "# %s – mô hình trường từ case ACS\n\nTrường: [[%s]]%s · quy trình: [[00 Quy trình xuyên phân hệ]] · cách đọc case: [[00 Cách phân tích case]]\n" % (
        ma, ma, (" – " + sx.get("ten")) if sx.get("ten") else "")
    if SECRET.search(auto):
        raise ToolError("Nội dung có vẻ chứa mật khẩu / token – không ghi.")
    f.write_text("\n".join(fm) + "\n\n" + head + "\n" + keep + "\n\n" + MH_A + "\n" + auto + "\n" + MH_B + "\n", "utf-8")
    # gắn tóm tắt vào ghi chú trường
    tf = Path(base) / "Truong" / ("%s.md" % ma)
    if tf.exists():
        t = tf.read_text("utf-8", errors="replace")
        blk = ("## Mô hình trường (từ case ACS)\n[[Case-truong/%s|%d case]]%s – phân hệ hay có case: %s; dạng hay gặp: %s.\n" %
               (ma, summ["tong_case"], (" tới " + summ["den_ngay"]) if summ["den_ngay"] else "", ", ".join(summ["phan_he_nhieu"][:4]) or "—",
                ", ".join(summ["dang_nhieu"][:3]) or "—"))
        if "## Mô hình trường (từ case ACS)" in t:
            t = re.sub(r'## Mô hình trường \(từ case ACS\)\n.*?(?=\n## |\n---\n|\Z)', lambda m: blk.rstrip("\n"), t, count=1, flags=re.S)
        else:
            k = t.find("\n## Khi đọc case")
            t = (t[:k] + "\n" + blk + t[k:]) if k > 0 else t.rstrip("\n") + "\n\n" + blk
        tf.write_text(t, "utf-8")
    return summ


def learn_cases(S, rows, only=None):
    """rows = case ACS (cột META) → ghi Case-truong/<trường>.md cho từng trường (gom mọi phân cấp)."""
    base, writable = kb_dir(S)
    if not writable:
        raise ToolError("KB đang là bản chỉ đọc – mở lại app AQ Auto Test bản mới (tự tạo KB ghi được) hoặc chọn thư mục vault ở Test case ACS → Thiết lập ACS → Thư mục KB.")
    g = kb_graph.build(base)
    groups = {}
    for x in rows or []:
        if not isinstance(x, dict) or not x.get("case_id"):
            continue
        ma, _ = school_key(g, x.get("school_code"))
        if not ma or not re.match(r'^[A-Z0-9]{2,12}$', ma) or (only and ma != only):
            continue
        groups.setdefault(ma, {})[str(x["case_id"])] = x
    an = {}
    for d in S.list_docs("caseAnalyses"):
        an[str(d["data"].get("caseId") or "")] = d["data"]
    rts = {}
    for d in S.list_docs("retests"):
        v = d["data"]
        k = str(v.get("caseId") or "")
        if k and (k not in rts or (v.get("round") or 1) > (rts[k].get("round") or 1)):
            rts[k] = v
    out = []
    for ma, cs in sorted(groups.items()):
        out.append(write_school_model(S, base, g, ma, list(cs.values()), an, rts))
    return out


def _codes_for(g, ma):
    codes = {ma}
    codes |= set(((g.get("schools") or {}).get(ma) or {}).get("phan_cap", {}).keys())
    try:
        lk = acs("GET", "/cs/lookups").get("data")
    except ToolError:
        lk = None
    def walk(o, dep=0):
        if dep > 4:
            return
        if isinstance(o, dict):
            for v in o.values():
                walk(v, dep + 1)
        elif isinstance(o, list):
            for v in o[:5000]:
                walk(v, dep + 1)
        elif isinstance(o, str) and re.match(r'^%s[A-Z0-9]{1,8}$' % re.escape(ma), o.strip().upper()):
            codes.add(o.strip().upper())
    walk(lk)
    return sorted(codes)


def t_truong_hoc_case(S, a):
    ma = str(a.get("ma_truong") or "").strip().upper()
    lim = max(20, min(3000, int(a.get("gioi_han") or 600)))
    base, _ = kb_dir(S)
    g = kb_graph.build(base)
    if ma in ("", "TAT-CA", "TATCA", "*"):
        cl, only = [{"op": "neq", "conj": "AND", "field": "case_id", "value": "0"}], None
    else:
        if not re.match(r'^[A-Z0-9]{2,12}$', ma):
            raise ToolError("Mã trường không hợp lệ")
        ma, _ = school_key(g, ma)
        codes = _codes_for(g, ma)
        cl, only = [{"op": "in", "conj": "AND", "field": "school_code", "value": ", ".join(codes)}], ma
    rows, off = [], 0
    while off < lim:
        n = min(200, lim - off)
        r = acs("POST", "/cs/query", {"clauses": cl, "columns": list(META), "sort": "case_id", "desc": True, "offset": off, "limit": n})
        d = r.get("data") or {}
        part = d.get("rows") if isinstance(d, dict) else d
        if r.get("status") != 200 or not isinstance(part, list):
            if not rows:
                raise ToolError("ACS trả về mã %s" % r.get("status"))
            break
        rows += part
        if len(part) < n:
            break
        off += n
    res = learn_cases(S, rows, only)
    return {"da_doc": len(rows), "truong": res,
            "nhac": "Đã ghi Case-truong/<mã>.md (+ mục 'Mô hình trường' trong Truong/<mã>.md). Đọc lại ghi chú, mở acs_case vài case tiêu biểu "
                    "(nhiều nhất / case tiếp nối) rồi viết mục 'Nhận xét – mô hình trường' bằng kb_ghi: trường dùng phần mềm thế nào, hay yêu cầu gì, "
                    "dễ nhầm gì. Không chép dữ liệu cá nhân SV/GV."}


HANDLERS = {"kb_tim": t_kb_tim, "kb_doc": t_kb_doc, "kb_anh": t_kb_anh, "kb_luu_anh": t_kb_luu_anh, "acs_anh": t_acs_anh, "kb_ghi": t_kb_ghi, "kb_phan_tich": t_kb_phan_tich, "kb_du_lieu": t_kb_du_lieu,
            "acs_toi": t_acs_toi, "acs_tim_case": t_acs_tim_case, "acs_case": t_acs_case, "acs_case_lien_quan": t_acs_case_lien_quan,
            "case_ghi_phan_tich": t_case_ghi_phan_tich, "case_doc_phan_tich": t_case_doc_phan_tich,
            "retest_ds": t_retest_ds, "retest_doc_plan": t_retest_doc_plan, "retest_ghi_plan": t_retest_ghi_plan,
            "truong_hoc_case": t_truong_hoc_case}


# ------------------------------------------------------------------ JSON-RPC
def handle(S, msg, version=""):
    if isinstance(msg, list):
        out = [r for r in (handle(S, m, version) for m in msg) if r is not None]
        return out or None
    if not isinstance(msg, dict):
        return {"jsonrpc": "2.0", "id": None, "error": {"code": -32600, "message": "Invalid Request"}}
    mid, method, p = msg.get("id"), msg.get("method"), msg.get("params") or {}
    if mid is None:                       # thông báo (notifications/initialized…)
        return None

    def ok(res):
        return {"jsonrpc": "2.0", "id": mid, "result": res}
    if method == "initialize":
        return ok({"protocolVersion": p.get("protocolVersion") or PROTO, "capabilities": {"tools": {"listChanged": False}},
                   "serverInfo": {"name": "aq-auto-test", "title": "AQ Auto Test", "version": version or "dev"}, "instructions": INSTRUCTIONS})
    if method == "ping":
        return ok({})
    if method == "tools/list":
        return ok({"tools": TOOLS})
    if method == "tools/call":
        name, args = p.get("name"), p.get("arguments") or {}
        fn = HANDLERS.get(name)
        if not fn:
            return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32602, "message": "Không có công cụ " + str(name)}}
        try:
            res = fn(S, args)
            if isinstance(res, dict) and "_content" in res:          # có ảnh
                return ok({"content": res["_content"], "isError": False})
            txt = res if isinstance(res, str) else json.dumps(res, ensure_ascii=False, indent=1)
            return ok({"content": [{"type": "text", "text": txt}], "isError": False})
        except ToolError as e:
            return ok({"content": [{"type": "text", "text": str(e)}], "isError": True})
        except Exception as e:            # lỗi bất ngờ: báo gọn, không lộ đường dẫn máy
            return ok({"content": [{"type": "text", "text": "Lỗi khi chạy %s: %s" % (name, type(e).__name__)}], "isError": True})
    return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32601, "message": "Method not found: " + str(method)}}


def write_conn_file(S, port):
    """<local>/mcp.json (địa chỉ + token cho aq_mcp.py) và mcp-tools.json (danh sách công cụ khi app chưa mở)."""
    import secrets
    tok = secrets.token_urlsafe(24)
    S.LOCAL.mkdir(parents=True, exist_ok=True)
    f = S.LOCAL / "mcp.json"
    f.write_text(json.dumps({"url": "http://127.0.0.1:%d%s/api/mcp" % (port, S.MODE["base"]), "token": tok, "pid": os.getpid(),
                             "at": time.strftime("%Y-%m-%d %H:%M:%S")}, ensure_ascii=False), "utf-8")
    try:
        os.chmod(f, 0o600)
    except OSError:
        pass
    (S.LOCAL / "mcp-tools.json").write_text(json.dumps({"tools": TOOLS, "instructions": INSTRUCTIONS}, ensure_ascii=False), "utf-8")
    return tok
