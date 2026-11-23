# AQ Auto Test – mô tả ứng dụng

Công cụ quản lý và **chạy test tự động** cho phần mềm **Edusoft.NET** (bản Windows) và **Netweb** (cổng web) của AQTech.
Người test lấy case đã xử lý từ ACS, soạn plan test, cho máy tự thao tác trên Edusoft, chụp ảnh từng bước rồi kết luận Đạt / Không đạt.

---

## 1. Tổng quan kiến trúc

```
┌────────────────────────── App AQ Auto Test (Electron, Windows) ──────────────────────────┐
│  Cửa sổ app (Chromium)  ──HTTP──▶  server.py (Python nhúng 3.12, chỉ 127.0.0.1)          │
│  web/index.html (HTML+JS)          ├─ API dữ liệu  → thư mục JSON (%APPDATA%\AQ Auto Test) │
│                                     ├─ /api/kit/*   → điều khiển bộ test trên máy          │
│  acs.js  ── phiên đăng nhập ACS ──▶ ├─ /api/mcp     → mcp_server.py (cho Claude Desktop)   │
│  updater.js ── cập nhật app        └─ /api/kb/*    → KB nghiệp vụ (vault Obsidian)         │
└───────────────────────────────────────────────────────────────────────────────────────────┘
            │ file lệnh .json                                  ▲ kết quả + ảnh (.zip)
            ▼                                                  │
┌──────── Bộ test trên máy chạy test (Python 3.12 cài riêng, quyền admin) ────────┐
│  aq-agent.py (chạy nền, Task Scheduler) → aqrun.py (pywinauto) → Edusoft.NET.exe │
└──────────────────────────────────────────────────────────────────────────────────┘
```

Gồm 3 phần chính: **app desktop** (vỏ Electron), **server + trang console** (Python + HTML/JS), **bộ test** (Python + pywinauto).

---

## 2. Ngôn ngữ & công nghệ

| Phần | Ngôn ngữ / nền tảng | Ghi chú |
|---|---|---|
| Vỏ app desktop | **JavaScript (Node.js) – Electron 38** | `desktop/src/main.js`, `preload.js`, `acs.js`, `mcp-relay.js`, `updater.js` |
| Đóng gói, cập nhật | **electron-builder 26**, **electron-updater 6** | Bản cài NSIS + bản Portable (Windows x64) |
| Server nội bộ | **Python 3.12** – chỉ dùng **thư viện chuẩn** | `server.py` (`http.server`), không cài thêm gói |
| Python đi kèm app | **Python 3.12.10 embeddable** (amd64) | Nằm trong `resources/python`, người dùng không cần cài Python |
| Giao diện (console) | **HTML + CSS + JavaScript thuần** (không framework) | Một file `web/index.html` (~12.000 dòng) |
| Thư viện web | JSZip 3.10 (đọc/ghi .zip), SheetJS xlsx 0.18 (Excel) | Tải từ cdnjs khi cần |
| Lớp dữ liệu | `web/claude-shim.js` – API kiểu Firestore | Cùng một trang chạy được trên app, localhost và claude.ai |
| Bộ test tự động | **Python 3.12** + **pywinauto** (UI Automation) | `kit/aqrun.py` (~4.900 dòng), `kit/aq-agent.py` |
| Thư viện bộ test | pywinauto, Pillow (chụp ảnh), keyboard (phím tắt), keyring (mật khẩu trong Windows Credential Manager), openpyxl (xuất Excel), obsws-python (quay video OBS), tkinter (popup tiến trình) | Cài bằng `cai-dat.bat` |
| Script cài/chạy | **Windows Batch** (`.bat`), **Task Scheduler** | `cai-dat.bat`, `chay-test.bat`; Agent tự chạy khi đăng nhập Windows |
| Kết nối Claude Desktop | **MCP** (Model Context Protocol, stdio) | `aq_mcp.py` → `mcp_server.py` |
| Kho kiến thức nghiệp vụ | **Markdown + Obsidian** (Properties, Canvas, Bases) | Thư mục `kb/` |
| CI / phát hành | **GitHub Actions** (Windows runner) | Merge vào `main` = phát hành bản mới |
| Bản server dùng chung | Python (`aq-console-server.py`), chạy được dưới **IIS** | Tự cập nhật theo nhánh `main` |

---

## 3. Các thành phần

### 3.1 App desktop – `desktop/`
- Electron mở cửa sổ riêng, khởi động `server.py` bằng Python nhúng, hiện màn hình chờ.
- **Đăng nhập app** (mặc định `admin` / `1234`, quản lý ở `/quan-tri`).
- **Kết nối ACS**: mở cửa sổ ACS để người dùng tự đăng nhập, app gọi API ACS trong cùng phiên (chỉ đọc case, query…).
- **Tự cập nhật**: đọc repo public `aq-autotest-releases`, có hộp "Có phiên bản mới" + thanh tiến trình, "Có gì mới" sau khi cập nhật.
- Dữ liệu lưu ở `%APPDATA%\AQ Auto Test\` (`du-lieu`, `rieng`, `kb`).

### 3.2 Server – `server.py`
- Web server nhỏ chỉ nghe `127.0.0.1`; yêu cầu ghi phải có header `X-AQ: 1`.
- Lưu dữ liệu dạng **mỗi bản ghi một file JSON**: `<collection>/<id>.json` (kịch bản, lượt chạy, lỗi, phiếu test case ACS…), ảnh ở `/_blob/`.
- `/api/kit/*`: gửi lệnh chạy cho bộ test, đọc kết quả, kiểm tra / tự bật Agent, cài bộ test tự động.
- Nhập / xuất dữ liệu bằng gói `.zip`.

### 3.3 Trang console – `web/index.html`
Các trang chính:
- **Tổng quan**, **Kịch bản test** (bước, lệnh tự động), **Lượt chạy / Lỗi**, **Release** (test menu theo phiên bản).
- **Máy chạy thử**: khai báo file `Edusoft.NET.exe` bản test, tài khoản, cài bộ test, chạy kịch bản.
- **Test case ACS** – 4 bước:
  1. *Hiểu yêu cầu*: phiếu case ACS (KH yêu cầu → BA → Dev xử lý), trường / phân hệ, đầu ra cần đạt.
  2. *Plan test*: môi trường → tài khoản → thao tác → đầu ra cần đạt.
  3. *Test*: bấm **Chạy test** → bộ test tự làm trên Edusoft, ảnh và kết quả tự điền vào từng mục.
  4. *Kết luận*: Đạt / Không đạt, soạn nội dung test để ghi về ACS.
- **Màn hình Edusoft**: tra menu → lưới → cột / ô / nút (từ `web/edusoft-catalog.json`).

### 3.4 Bộ test – `kit/`
- `aq-agent.py`: chạy nền quyền admin, nhận file lệnh, chạy lần lượt (xếp hàng), ghi nhịp tim để app biết Agent còn sống.
- `aqrun.py`: mở Edusoft, đăng nhập, thao tác theo lệnh như người dùng. Một số lệnh:
  - `menu:` mở menu; `click:` bấm nút; `type:`, `select:`, `choose:` nhập / chọn ô.
  - `find_row:`, `delete_row:`, `pick:` làm việc với lưới.
  - `save:`, `expect:`, `shot:` lưu, kiểm tra, chụp ảnh.
  - `menu_time:`, `fieldbtn:`, `time_click:`, `time_check:`: đo thời gian cho case chậm. Bộ test nhấn **Ctrl+Shift+T** rồi đọc "Thời gian mở form" ở thanh dưới đáy Edusoft.
- Chạy xong gói kết quả `AQ-ket-qua-<giờ>.zip` (ảnh từng bước, `result.json`, Excel), app tự nhập hoặc người dùng chọn file.
- Mỗi lần sửa bộ test thì tăng `KIT_VERSION`. Bộ test trên máy tự cập nhật ở lần chạy kế tiếp.

### 3.5 Claude Desktop (MCP) – `aq_mcp.py`, `mcp_server.py`
Cho Claude Desktop dùng: tra KB (`kb_tim`, `kb_doc`, `kb_ghi`…), đọc case ACS (**chỉ đọc**), xem ảnh trong case, soạn plan test nháp, học mô hình trường từ case cũ.

### 3.6 Kho kiến thức – `kb/` (Obsidian)
- `Phan-he/`: từng phân hệ, nhận dữ liệu từ đâu, đưa sang đâu.
- `Du-lieu/`: "muốn có X phải có Y".
- `Quy-trinh/`: 12 quy trình xuyên phân hệ.
- `Dang-case/`: các dạng case hay gặp.
- `Truong/`, `Case-truong/`: mô hình từng trường.
- `Tai-lieu/`: nguồn tài liệu.
- `Luong-test/`: luồng test mẫu.

`kb_graph.py` dựng bản đồ từ các ghi chú này cho app dùng ở phía sau.

---

## 4. Luồng làm việc chính (test case ACS)

1. Chọn Query ACS → danh sách case Dev đã xử lý.
2. Chọn case → đọc yêu cầu KH / BA / Dev, xác định trường, phân hệ, **đầu ra cần đạt**.
3. Plan test: file Edusoft bản test + tài khoản → **Bắt đầu test**.
4. **Chạy test** → app gửi lệnh → Agent chạy `aqrun.py` trên Edusoft → chụp ảnh, ghi kết quả.
5. Kết quả tự về plan → người test xem ảnh → kết luận → ghi nội dung test về ACS.

---

## 5. Cấu trúc thư mục repo

```
desktop/        App Electron (main.js, preload.js, acs.js, updater.js, mcp-relay.js)
web/            index.html (console), claude-shim.js, edusoft-catalog.json
kit/            Bộ test: aqrun.py, aq-agent.py, cai-dat.bat, chay-test.bat…
kb/             Kho kiến thức Obsidian
data/           Dữ liệu mẫu (JSON): scenarios, runs, bugs, releases…
tools/          Script: đóng gói app, nhúng kit, kiểm tra, lập danh mục màn hình…
server.py       Server nội bộ (Python thư viện chuẩn)
mcp_server.py   Công cụ MCP cho Claude Desktop
kb_graph.py     Dựng bản đồ KB
aq-console-server.py, server-iis/   Bản server dùng chung (IIS)
.github/workflows/  kiem-tra.yml (PR), release.yml (phát hành)
```

---

## 6. Build & phát hành

- Kiểm tra trước khi merge: `python tools/kiem_tra.py` (cú pháp Python, JS trang, kit đã nhúng).
- `tools/embed_kit.py`: nhúng bộ test vào trang.
- `tools/dong_goi_app.py`: chuẩn bị Python nhúng + mã cho Electron.
- **Merge vào `main`** → GitHub Actions build `AQ-AutoTest-Setup-<phiên bản>.exe` + `AQ-AutoTest-Portable-<phiên bản>.exe`, chạy thử `--smoke`, tạo Release `v<năm>.<tháng>.<số>`. App trên máy người dùng tự cập nhật.

---

## 7. Quy tắc an toàn

- Chỉ chạy trên **Edusoft bản test/demo** người dùng khai báo, không đụng môi trường thật.
- Không lưu mật khẩu trong dữ liệu / kịch bản / log. Mật khẩu Edusoft nằm trong Windows Credential Manager.
- ACS và source TFS: **chỉ đọc**.
- Dữ liệu test có tiền tố rõ ràng (`AUTO…`, `TEST_…`). Chỉ xóa khi hộp xác nhận nêu đúng mã dữ liệu test.
- Không gửi phím Esc lên Edusoft. Tắt Unikey / EVKey khi chạy test.
