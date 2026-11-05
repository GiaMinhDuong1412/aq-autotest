# -*- coding: utf-8 -*-
"""
AQ Autotest – bộ chạy kịch bản Edusoft ở CHẾ ĐỘ TRÌNH DIỄN.
Thao tác hiện rõ trên màn hình (chuột di chuyển thật, khung đỏ quanh ô/nút,
dòng chú thích bước đang chạy) để support quan sát; mỗi bước chụp ảnh,
có thể quay video bằng OBS. Kết quả ghi ra thư mục results\\<mã lượt chạy>\\,
sau đó vào AQ Autotest Console → Máy chạy thử → "Nhập kết quả chạy".

Cách chạy:  chay-test.bat              (chạy tất cả kịch bản trong thư mục scenarios)
            chay-test.bat KLGD-003     (chỉ chạy các mã được liệt kê)
            do-giao-dien.bat           (ghi cây giao diện Edusoft đang mở ra file dump-*.txt)
"""
import json, os, sys, time, datetime, threading, queue, re, traceback, getpass, shutil, base64, unicodedata

KIT_VERSION = "2026.11.05-01"
from pathlib import Path

BASE = Path(__file__).resolve().parent

# Toạ độ đúng trên máy nhiều màn hình / tỉ lệ hiển thị khác 100%: bật DPI-aware TRƯỚC khi nạp pywinauto, tkinter.
if os.name == "nt":
    import ctypes
    try:
        ctypes.windll.user32.SetProcessDpiAwarenessContext(ctypes.c_void_p(-4))
    except Exception:
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(2)
        except Exception:
            try:
                ctypes.windll.user32.SetProcessDPIAware()
            except Exception:
                pass
CFG = json.loads((BASE / "config.json").read_text("utf-8"))
DEMO = CFG.get("demo", {})
STEP_DELAY = float(DEMO.get("stepDelay", 1.0))         # nghỉ giữa các bước test (~1 giây, người dùng yêu cầu 03/11)
TYPE_PAUSE = float(DEMO.get("typePause", 0.03))
ACTION_DELAY = float(DEMO.get("actionDelay", 0.3))     # nghỉ ngắn giữa hai lệnh thao tác (các lệnh tìm phần tử đã tự chờ)

try:
    from pywinauto import Application, Desktop, keyboard as pkb
    from pywinauto.timings import TimeoutError as PwTimeout
    from PIL import ImageGrab
except Exception:  # pragma: no cover
    if "--chan-doan" not in sys.argv:      # kiểm tra cài đặt vẫn chạy được khi thiếu thư viện
        print("Thiếu thư viện. Hãy chạy cai-dat.bat trước (cài pywinauto, pillow, keyboard, keyring).")
        input("Nhấn Enter để thoát…")
        sys.exit(1)

try:
    import keyboard as hotkeys
except Exception:
    hotkeys = None
try:
    import keyring
except Exception:
    keyring = None


def now_iso():
    return datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")


def stamp():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M")


def esc_keys(s):
    """Thoát ký tự đặc biệt của pywinauto.send_keys để gõ đúng nguyên văn."""
    return "".join("{%s}" % c if c in "+^%~(){}[]" else c for c in str(s))


def nfc(s):
    """Edusoft có chỗ lưu chữ Việt dạng Unicode TỔ HỢP (vd nút "Thêm mới 1 SV": ơ + dấu sắc rời) – đưa về dạng dựng sẵn."""
    return unicodedata.normalize("NFC", str(s or ""))


def norm(s):
    return re.sub(r"\s+", " ", nfc(s)).strip().lower()


def norm_label(s):
    """Chuẩn hoá nhãn giao diện: bỏ &, dấu * bắt buộc, dấu : cuối, khoảng trắng thừa."""
    return norm(str(s or "").replace("&", "").replace("*", "")).rstrip(":").strip()


def split_col(arg):
    """"giá trị @ Cột|Cột" → ("giá trị", "Cột|Cột"); không có @ thì cột rỗng."""
    m = re.match(r"^(.*?)\s+@\s+(.+)$", str(arg or ""))
    return (m.group(1).strip(), m.group(2).strip()) if m else (str(arg or "").strip(), "")


def menu_segs(path):
    """Tách đường dẫn menu "A/ B/ C". Tài liệu ngăn cấp bằng "/ " (có khoảng trắng) nên tên có "/" liền như
    "QĐ vào/ra sinh viên" giữ nguyên; đường dẫn không có khoảng trắng quanh "/" thì tách ở mọi "/"."""
    p = str(path or "")
    parts = re.split(r"\s+/\s*|/\s+", p) if re.search(r"\s/|/\s", p) else p.split("/")
    return [x.strip() for x in parts if x.strip()]


def alts_of(text):
    return [x.strip() for x in str(text or "").split("|") if x.strip()]


# Câu lỗi lấy theo danh mục Resources\Languages.xml của Edusoft (skill giaodien-edusoft/thong-bao.md), vd "Import dữ liệu thất bại",
# "Ngày ra phải lớn hơn ngày vào", "Mã … không tồn tại trong danh mục", "Nhóm thi này đã bị khóa".
ERR_PAT = re.compile(r"lỗi|không (được|thể|hợp lệ|thành công|tồn tại|đúng|cho phép)|thất bại|trùng|đã tồn tại|đã có|bắt buộc|"
                     r"chưa nhập|chưa chọn|vui lòng|thiếu|phải (lớn|nhỏ) hơn|vượt quá|(đã|bị) khóa|sai định dạng|"
                     r"invalid|error|not allowed", re.I)
OK_PAT = re.compile(r"thành công|đã lưu|hoàn tất|successful", re.I)


# ---------------------------------------------------------------- chú thích trên màn hình
def alt_at(alt, n):
    """Bước của luồng chính nơi luồng con rẽ nhánh (tính từ 0): atStep, hoặc "bước N" trong điều kiện/tên, mặc định bước cuối."""
    if not n:
        return 0
    k = alt.get("atStep") if isinstance(alt, dict) else None
    if isinstance(k, int) and k >= 0:
        return min(k, n - 1)
    m = re.search(r"bước\s*(\d+)", "%s %s" % ((alt or {}).get("condition", ""), (alt or {}).get("name", "")), re.I)
    if m and 0 < int(m.group(1)) <= n:
        return int(m.group(1)) - 1
    return n - 1


class Caption:
    """Popup tiến trình nổi ở góc phải dưới màn hình (tkinter, chạy ở luồng chính): kịch bản, menu đang test,
    thao tác của bước đang chạy và danh sách bước kèm trạng thái. Người test trả lời ngay trên popup
    (bước làm tay, bước gặp lỗi, ghi lỗi) – không phải gõ vào cửa sổ đen. Không có tkinter thì chạy không popup."""
    C = dict(bg="#ffffff", line="#d5dce8", fg="#111726", dim="#4a5368", mute="#8a93a6", acc="#5b4cf0",
             ok="#1f9d55", bad="#d64545", skip="#8a93a6", soft="#f3f5fa", badbg="#fdeeee", okbg="#e9f7ef")
    W = 460
    W_WIDE = 720          # khi hiện khung lỗi / ghi lỗi: rộng hơn để đọc đủ chi tiết lỗi EX
    BORDER = 3            # viền màu làm nổi popup: tím = đang chạy · đỏ = gặp lỗi · xanh = xong
    HOLD = 0.6            # dòng trạng thái giữ ít nhất 0,6 giây rồi mới đổi chữ
    ROWS = 5

    def __init__(self):
        self.q = queue.Queue()
        self.root = None
        self.st = dict(code="", title="", menu="", text="", steps=[], alts=[], srec=[], arec=[], cur=None, status="",
                       t0=None, t_end=None, t_step=None, durs={})
        self.small = False
        self.wide = False
        self.bkey = None      # màu viền đang giữ (bad/ok khi có khung lỗi / kết quả), None = theo trạng thái chạy
        self.moved = None
        self._pending = None
        self._hold = 0.0

    # ---------- luồng chạy test gọi
    def start(self, worker):
        try:
            import tkinter as tk
        except Exception:
            worker()
            return
        self.tk = tk
        r = self.root = tk.Tk()
        r.overrideredirect(True)
        r.attributes("-topmost", True)
        r.configure(bg=self.C["acc"])
        self._build()

        def pump():
            try:
                while True:
                    a, b = self.q.get_nowait()
                    if a is None:
                        r.destroy()
                        return
                    if a == "__state__":
                        self._render()
                    elif a == "__close__":
                        self._act_clear()
                    elif a in ("__hide__", "__unhide__"):
                        r.attributes("-alpha", 0.0 if a == "__hide__" else 1.0)
                    elif a in ("__step__", "__bug__", "__err__"):
                        getattr(self, "_act" + a[1:-2])(*b)
                    else:
                        self._pending = (a, b)
            except queue.Empty:
                pass
            if self._pending and time.time() >= self._hold:
                a, b = self._pending
                self._pending = None
                self._hold = time.time() + self.HOLD
                self.st["status"] = (a + (": " + b if b else ""))[:150]
                self._render()
            r.after(120, pump)

        def tick():
            self._render()
            r.after(500, tick)

        r.after(120, pump)
        r.after(500, tick)
        r.after(60, lambda: self._style(False))
        threading.Thread(target=self._run, args=(worker,), daemon=True).start()
        r.mainloop()

    def _run(self, worker):
        try:
            worker()
        finally:
            self.q.put((None, None))

    def show(self, title, sub=""):
        print("»", title, ("— " + sub) if sub else "")
        self.q.put((title, sub))

    def begin(self, sc, srec, arec, texts=None):
        """Bắt đầu một kịch bản: popup hiện mã, tên, menu và danh sách bước (trạng thái đọc thẳng từ srec/arec)."""
        steps = texts or [str(x) for x in (sc.get("steps") or [])]
        self.st.update(code=sc.get("code", ""), title=sc.get("title", ""), menu=" › ".join(menu_segs(sc.get("menu", ""))),
                       steps=steps, alts=[a.get("name", "") for a in (sc.get("altFlows") or [])], srec=srec, arec=arec, cur=None, text="",
                       t0=time.time(), t_end=None, t_step=None, durs={})
        self.q.put(("__state__", None))

    def finish(self):
        """Kịch bản chạy xong: dừng đồng hồ (tổng thời gian giữ nguyên trên popup)."""
        s, now = self.st, time.time()
        if s["cur"] and s["t_step"]:
            s["durs"][s["cur"]] = now - s["t_step"]
        s.update(t_end=now, t_step=None)
        self.q.put(("__state__", None))

    def _border(self, key=None):
        """key = "bad"/"ok" giữ màu viền tới khi khung hỏi đóng; None = tím khi đang chạy, xanh khi xong."""
        if key is not None:
            self.bkey = key
        try:
            self.root.configure(bg=self.C[self.bkey or ("ok" if self.st["t_end"] else "acc")])
        except Exception:
            pass

    def at(self, kind, idx, text):
        """Bước / luồng con bắt đầu chạy – chỉ gọi khi bước trước đã xong, nên chữ "Thao tác" không nhảy giữa chừng."""
        s, now = self.st, time.time()
        if s["cur"] and s["t_step"] and s["cur"] != (kind, idx):
            s["durs"][s["cur"]] = now - s["t_step"]        # thời gian thực hiện bước vừa xong
        if s["cur"] != (kind, idx) or not s["t_step"]:
            s["t_step"] = now
        self.st.update(cur=(kind, idx), text=str(text or ""), status="")
        self._pending = None
        self.q.put(("__state__", None))

    def hidden(self, on):
        """Ẩn popup trong lúc chụp ảnh màn hình để ảnh Edusoft không bị che."""
        if self.root is not None:
            self.q.put(("__hide__" if on else "__unhide__", None))
            time.sleep(0.35 if on else 0)

    def ask(self, kind, label, payload):
        """Hỏi người test trên popup và chờ trả lời. kind: __step__ (Đạt/Lỗi/Bỏ qua), __bug__ (ghi lỗi),
        __err__ (bước gặp lỗi script chưa xác định). Không có popup → None."""
        if self.root is None:
            return None
        rq = queue.Queue()
        hk = []
        if kind == "__step__" and hotkeys is not None:
            for key, val in (("f8", "ok"), ("f9", "bad"), ("f10", "skip")):
                try:
                    hk.append(hotkeys.add_hotkey(key, lambda v=val: rq.put(v)))
                except Exception:
                    pass
        self.q.put((kind, (label, payload, rq)))
        try:
            return rq.get()
        finally:
            for h in hk:
                try:
                    hotkeys.remove_hotkey(h)
                except Exception:
                    pass
            self.q.put(("__close__", None))

    # ---------- giao diện (luồng tkinter)
    def _lbl(self, parent, text="", size=9, color=None, bold=False, wrap=0, bg=None):
        return self.tk.Label(parent, text=text, fg=color or self.C["fg"], bg=bg or self.C["bg"], anchor="w", justify="left",
                             font=("Segoe UI", size, "bold" if bold else "normal"), wraplength=wrap)

    def _btn(self, parent, text, cmd, color=None, solid=True):
        c = color or self.C["acc"]
        return self.tk.Button(parent, text=text, command=cmd, relief="flat", bd=0, cursor="hand2", padx=12, pady=4,
                              font=("Segoe UI", 9, "bold"), bg=c if solid else self.C["soft"], fg="#ffffff" if solid else self.C["dim"],
                              activebackground=c if solid else self.C["line"], activeforeground="#ffffff" if solid else self.C["fg"])

    def _build(self):
        tk, C, r = self.tk, self.C, self.root
        box = self.box = tk.Frame(r, bg=C["bg"])
        box.pack(fill="both", expand=True, padx=self.BORDER, pady=self.BORDER)
        hd = tk.Frame(box, bg=C["bg"])
        hd.pack(fill="x", padx=14, pady=(10, 0))
        self.l_app = self._lbl(hd, "AQ AUTOTEST", 8, C["mute"], True)
        self.l_app.pack(side="left")
        self.b_small = tk.Label(hd, text="–", fg=C["mute"], bg=C["bg"], font=("Segoe UI", 11, "bold"), cursor="hand2")
        self.b_small.pack(side="right")
        self.b_small.bind("<Button-1>", lambda e: self._toggle())
        self.l_count = self._lbl(hd, "", 9, C["acc"], True)
        self.l_count.pack(side="right", padx=(0, 10))
        for w in (hd, self.l_app):
            w.bind("<ButtonPress-1>", self._drag_start)
            w.bind("<B1-Motion>", self._drag)
        self.l_title = self._lbl(box, "Đang chuẩn bị…", 11, C["fg"], True, self.W - 30)
        self.l_title.pack(fill="x", padx=14, pady=(2, 2))
        self.l_timer = self._lbl(box, "", 9, C["acc"], True, self.W - 30)      # ⏱ tổng thời gian · thời gian bước đang chạy
        self.l_timer.pack(fill="x", padx=14, pady=(0, 6))
        self.info = tk.Frame(box, bg=C["bg"])
        self.info.pack(fill="x", padx=14)
        self._lbl(self.info, "Menu", 8, C["mute"], True).grid(row=0, column=0, sticky="nw", padx=(0, 10))
        self.l_menu = self._lbl(self.info, "—", 9, C["dim"], False, self.W - 100)
        self.l_menu.grid(row=0, column=1, sticky="w")
        self._lbl(self.info, "Thao tác", 8, C["mute"], True).grid(row=1, column=0, sticky="nw", padx=(0, 10), pady=(4, 0))
        self.l_text = self._lbl(self.info, "—", 10, C["fg"], False, self.W - 100)
        self.l_text.grid(row=1, column=1, sticky="w", pady=(4, 0))
        self.l_status = self._lbl(box, "", 8, C["mute"], False, self.W - 30)
        self.l_status.pack(fill="x", padx=14, pady=(6, 0))
        self.lst = tk.Frame(box, bg=C["soft"])
        self.lst.pack(fill="x", padx=14, pady=(8, 0))
        self.rows = [self._lbl(self.lst, "", 9, C["dim"], bg=C["soft"]) for _ in range(self.ROWS)]
        self.act = tk.Frame(box, bg=C["bg"])
        tk.Frame(box, bg=C["bg"], height=12).pack(fill="x", side="bottom")
        self._render()

    def _items(self):
        s = self.st
        out = [("step", i, "Bước %d" % (i + 1), t, s["srec"][i] if i < len(s["srec"]) else {}) for i, t in enumerate(s["steps"])]
        out += [("alt", j, "Luồng A%d" % (j + 1), n, s["arec"][j] if j < len(s["arec"]) else {}) for j, n in enumerate(s["alts"])]
        return out

    def _render(self):
        if self.root is None:
            return
        C, s = self.C, self.st
        items = self._items()
        cur = s["cur"]
        pos = next((k for k, it in enumerate(items) if cur and (it[0], it[1]) == cur), -1)
        n = len(s["steps"])
        self.l_count.config(text=("Bước %d/%d" % (cur[1] + 1, n)) if cur and cur[0] == "step" else ("Luồng con A%d" % (cur[1] + 1)) if cur else "")
        self.l_title.config(text=("%s · %s" % (s["code"], s["title"])) if s["code"] else "Đang chuẩn bị…")
        self.l_menu.config(text=s["menu"] or "—")
        t = s["text"] or "—"
        self.l_text.config(text=t if len(t) <= 260 else t[:257] + "…")
        self.l_status.config(text=s["status"])
        self.l_timer.config(text=self._timer_text())
        self._border()
        w = self.W_WIDE if self.wide else self.W
        self.l_title.config(wraplength=w - 30)
        self.l_text.config(wraplength=w - 100)
        self.l_menu.config(wraplength=w - 100)
        if self.small:
            self.lst.pack_forget()
        else:
            if not self.lst.winfo_ismapped():
                self.lst.pack(fill="x", padx=14, pady=(8, 0), before=self.act if self.act.winfo_ismapped() else None)
            start = max(0, min(pos - 2, len(items) - self.ROWS)) if pos >= 0 else 0
            vis = items[start:start + self.ROWS]
            for k, row in enumerate(self.rows):
                if k >= len(vis):
                    row.pack_forget()
                    continue
                kind, idx, lab, txt, rec = vis[k]
                res = (rec or {}).get("res")
                now = (kind, idx) == cur and res is None
                icon, color = ("●", C["acc"]) if now else {"ok": ("✓", C["ok"]), "bad": ("✗", C["bad"]), "skip": ("–", C["skip"])}.get(res, ("○", C["mute"]))
                short = " ".join(str(txt).split())
                short = short if len(short) <= 44 else short[:42] + "…"
                d = s["durs"].get((kind, idx))
                tail = ("  · " + self._fmt(d)) if (d is not None and res) else ""
                row.config(text="%s  %s · %s%s" % (icon, lab, short, tail), fg=color if (now or res) else C["dim"],
                           font=("Segoe UI", 9, "bold" if now else "normal"))
                if not row.winfo_ismapped():
                    row.pack(fill="x", padx=8, pady=1)
        self._place()

    @staticmethod
    def _fmt(sec):
        sec = int(round(sec or 0))
        h, m, x = sec // 3600, sec // 60 % 60, sec % 60
        return ("%d:%02d:%02d" % (h, m, x)) if h else ("%d:%02d" % (m, x))

    def _timer_text(self):
        s = self.st
        if not s["t0"]:
            return ""
        now = time.time()
        txt = "⏱ Tổng %s" % self._fmt((s["t_end"] or now) - s["t0"])
        if s["t_end"]:
            return txt + " · đã xong"
        if s["cur"] and s["t_step"]:
            lab = ("Bước %d" % (s["cur"][1] + 1)) if s["cur"][0] == "step" else ("Luồng A%d" % (s["cur"][1] + 1))
            txt += "  ·  %s: %s" % (lab, self._fmt(now - s["t_step"]))
        return txt

    def _place(self):
        r = self.root
        r.update_idletasks()
        w = self.W_WIDE if self.wide else self.W
        h = self.box.winfo_reqheight() + 2 * self.BORDER
        if self.moved:
            x, y = self.moved
            x = min(x, max(0, r.winfo_screenwidth() - w))
        else:
            x, y = r.winfo_screenwidth() - w - 18, max(0, r.winfo_screenheight() - h - 70)
        y = min(y, max(0, r.winfo_screenheight() - h - 40))
        r.geometry("%dx%d+%d+%d" % (w, h, x, y))

    def _toggle(self):
        self.small = not self.small
        self.b_small.config(text="+" if self.small else "–")
        self._render()

    def _drag_start(self, e):
        self._dx, self._dy = e.x_root - self.root.winfo_x(), e.y_root - self.root.winfo_y()

    def _drag(self, e):
        self.moved = (e.x_root - self._dx, e.y_root - self._dy)
        self._place()

    def _style(self, activate):
        """Bình thường popup không giành focus của Edusoft (bấm nút vẫn được); khi cần gõ (ghi lỗi) thì cho nhận focus."""
        try:
            import ctypes
            u = ctypes.windll.user32
            h = u.GetParent(self.root.winfo_id()) or self.root.winfo_id()
            ex = u.GetWindowLongW(h, -20) | 0x80                     # WS_EX_TOOLWINDOW: không hiện trên thanh tác vụ
            ex = (ex & ~0x08000000) if activate else (ex | 0x08000000)
            u.SetWindowLongW(h, -20, ex)
        except Exception:
            pass

    def _focus(self, entry):
        try:
            import ctypes
            u, k = ctypes.windll.user32, ctypes.windll.kernel32
            h = u.GetParent(self.root.winfo_id()) or self.root.winfo_id()
            self._prev = u.GetForegroundWindow()
            t1, t2 = u.GetWindowThreadProcessId(self._prev, None), k.GetCurrentThreadId()
            u.AttachThreadInput(t1, t2, True)
            u.BringWindowToTop(h)
            u.SetForegroundWindow(h)
            u.AttachThreadInput(t1, t2, False)
        except Exception:
            pass
        try:
            self.root.focus_force()
            entry.focus_set()
        except Exception:
            pass

    def _unfocus(self):
        self._style(False)
        try:
            import ctypes
            if getattr(self, "_prev", None):
                ctypes.windll.user32.SetForegroundWindow(self._prev)     # trả focus cho Edusoft
        except Exception:
            pass
        self._prev = None

    def _act_clear(self):
        for w in self.act.winfo_children():
            w.destroy()
        self.act.pack_forget()
        self.wide = False
        self.bkey = None
        self._border()
        self._place()

    def _textbox(self, parent, text="", height=6, bg=None, readonly=False):
        """Ô chữ nhiều dòng có thanh cuộn – chi tiết lỗi EX (stack trace) dài, ô một dòng không xem/dán đủ."""
        tk, C = self.tk, self.C
        fr = tk.Frame(parent, bg=bg or C["bg"])
        sb = tk.Scrollbar(fr, orient="vertical")
        t = tk.Text(fr, height=height, wrap="word", font=("Consolas", 9), relief="solid", bd=1, yscrollcommand=sb.set,
                    bg="#fbfbfd" if readonly else "#ffffff", fg=C["fg"], padx=4, pady=3)
        sb.config(command=t.yview)
        sb.pack(side="right", fill="y")
        t.pack(side="left", fill="both", expand=True)
        if text:
            t.insert("1.0", text)
        if readonly:
            t.config(state="disabled")
        return fr, t

    def _act_new(self, bg=None, wide=False):
        self._act_clear()
        self.wide = wide
        if self.small:
            self._toggle()
        self.act.config(bg=bg or self.C["bg"])
        self.act.pack(fill="x", padx=14, pady=(10, 0))
        return self.act

    def _act_step(self, label, text, rq):
        C = self.C
        a = self._act_new()
        self._lbl(a, "Bước này làm tay trên Edusoft, xong thì chọn kết quả:", 9, C["dim"]).pack(fill="x")
        f = self.tk.Frame(a, bg=C["bg"])
        f.pack(fill="x", pady=(6, 0))
        self._btn(f, "Đạt  F8", lambda: rq.put("ok"), C["ok"]).pack(side="left", padx=(0, 6))
        self._btn(f, "Lỗi  F9", lambda: rq.put("bad"), C["bad"]).pack(side="left", padx=(0, 6))
        self._btn(f, "Bỏ qua  F10", lambda: rq.put("skip"), solid=False).pack(side="left")
        self._place()

    def _act_err(self, label, payload, rq):
        C = self.C
        text, err = payload
        a = self._act_new(C["badbg"], wide=True)
        self._border("bad")
        self._lbl(a, "⚠  %s gặp lỗi – test đang tạm dừng" % label, 10, C["bad"], True, bg=C["badbg"]).pack(fill="x", padx=10, pady=(8, 2))
        fr, _ = self._textbox(a, err, height=min(12, max(3, err.count("\n") + len(err) // 90 + 1)), bg=C["badbg"], readonly=True)
        fr.pack(fill="x", padx=10)
        self._lbl(a, "Xem màn hình Edusoft rồi chọn. Luồng này sẽ dừng, các luồng khác vẫn test tiếp.", 8, C["dim"], False, self.W_WIDE - 60,
                  bg=C["badbg"]).pack(fill="x", padx=10, pady=(6, 0))
        f = self.tk.Frame(a, bg=C["badbg"])
        f.pack(fill="x", padx=10, pady=(8, 10))
        self._btn(f, "Tạo lỗi", lambda: self._act_bug(label, dict(type="func", exp=text, act=err), rq, True), C["bad"]).pack(side="left", padx=(0, 6))
        self._btn(f, "Không phải lỗi", lambda: self._act_done("Không ghi lỗi. Luồng này dừng lại.", rq, {}), solid=False).pack(side="left", padx=(0, 6))
        self._btn(f, "Dừng test", lambda: rq.put({"stop": True}), solid=False).pack(side="left")
        self._place()

    def _act_bug(self, label, prefill, rq, cont=False):
        tk, C = self.tk, self.C
        prefill = prefill if isinstance(prefill, dict) else dict(type="func", exp=str(prefill or ""))
        a = self._act_new(wide=True)
        self._border("bad")
        self._lbl(a, "Ghi lỗi · %s" % label, 10, C["fg"], True).pack(fill="x")
        kind = tk.StringVar(value=prefill.get("type", "func"))
        rf = tk.Frame(a, bg=C["bg"])
        rf.pack(fill="x", pady=(4, 2))
        body = tk.Frame(a, bg=C["bg"])
        body.pack(fill="x")
        ents = {}

        def row(key, lab, lines=0):
            fr = tk.Frame(body, bg=C["bg"])
            self._lbl(fr, lab, 8, C["mute"], True).pack(fill="x")
            if lines:                                   # chi tiết lỗi EX / menu code: dán nhiều dòng, có thanh cuộn
                tf, e = self._textbox(fr, str(prefill.get(key, "")), height=lines)
                tf.pack(fill="x", pady=(1, 5))
            else:
                e = tk.Entry(fr, font=("Segoe UI", 10), relief="solid", bd=1)
                e.insert(0, str(prefill.get(key, ""))[:1000])
                e.pack(fill="x", pady=(1, 5), ipady=2)
            ents[key] = (fr, e)

        def val(e):
            return e.get("1.0", "end-1c") if isinstance(e, tk.Text) else e.get()

        def swap():
            ex = kind.get() == "ex"
            for fr, e in ents.values():
                fr.pack_forget()
            for k in (("detail", "code") if ex else ("action", "exp", "act")):
                ents[k][0].pack(fill="x")
            self._place()
            ents["detail" if ex else "action"][1].focus_set()

        for t, v in (("Lỗi chức năng / dữ liệu", "func"), ("Lỗi EX – hệ thống", "ex")):
            tk.Radiobutton(rf, text=t, value=v, variable=kind, command=swap, bg=C["bg"], fg=C["fg"], activebackground=C["bg"],
                           selectcolor=C["bg"], font=("Segoe UI", 9)).pack(side="left", padx=(0, 10))
        row("action", "Thao tác (Lưu / Thêm / Sửa / Xóa / Import / …)")
        row("exp", "Dữ liệu mong đợi")
        row("act", "Dữ liệu thực tế")
        row("detail", "Chi tiết lỗi EX (Ctrl+Shift+E rồi dán – dán được nhiều dòng)", 12)
        row("code", "Menu code (Ctrl+Shift+F)", 4)

        def save():
            out = dict(type=kind.get(), **{k: val(e).strip() for k, (fr, e) in ents.items()})
            self._unfocus()
            if cont:
                self._act_done("Đã ghi lỗi – lỗi vào menu Lỗi khi kết quả về console. Luồng này dừng lại.", rq, out)
            else:
                rq.put(out)

        def back():
            self._unfocus()
            if cont:
                self._act_err(label, (prefill.get("exp", ""), prefill.get("act", "")), rq)
            else:
                rq.put(None)

        f = tk.Frame(a, bg=C["bg"])
        f.pack(fill="x", pady=(4, 0))
        self._btn(f, "Lưu lỗi", save, C["bad"]).pack(side="left", padx=(0, 6))
        self._btn(f, "Quay lại" if cont else "Không ghi chi tiết", back, solid=False).pack(side="left")
        for fr, e in ents.values():
            if not isinstance(e, tk.Text):              # ô nhiều dòng: Enter xuống dòng, không lưu
                e.bind("<Return>", lambda ev: save())
        swap()
        self._style(True)
        self.root.after(80, lambda: self._focus(ents["action"][1] if kind.get() != "ex" else ents["detail"][1]))

    def _act_done(self, msg, rq, result):
        C = self.C
        a = self._act_new(C["okbg"])
        self._border("ok")
        self._lbl(a, msg, 9, C["fg"], False, self.W - 60, bg=C["okbg"]).pack(fill="x", padx=10, pady=(8, 4))
        f = self.tk.Frame(a, bg=C["okbg"])
        f.pack(fill="x", padx=10, pady=(2, 10))
        self._btn(f, "Tiếp tục  ▸", lambda: rq.put(result), C["acc"]).pack(side="left")
        self._place()


CAP = Caption()


class Node:
    """Phần tử UIA đọc sẵn bằng MỘT lần gọi (CacheRequest): loại, tên, id, lớp, toạ độ, ẩn/hiện, giá trị.
    Duyệt cây kiểu cũ (descendants(control_type=…) nhiều lần + hỏi từng thuộc tính) tốn hàng nghìn lần gọi chéo tiến trình
    – mỗi lần tìm vài giây; bản này một lần quét cả cây. `wrap()` mới tạo wrapper pywinauto khi cần bấm/gõ."""
    __slots__ = ("ct", "name", "aid", "cls", "rect", "off", "val", "_e", "_w")

    def __init__(self, e, ct, name, aid, cls, rect, off, val):
        self._e, self.ct, self.name, self.aid, self.cls, self.rect, self.off, self.val, self._w = e, ct, name, aid, cls, rect, off, val, None

    @property
    def visible(self):
        l, t, r, b = self.rect
        return not self.off and r > l and b > t

    def inside(self, rc):
        l, t, r, b = self.rect
        cx, cy = (l + r) / 2, (t + b) / 2
        return rc[0] <= cx <= rc[2] and rc[1] <= cy <= rc[3]

    def wrap(self):
        if self._w is None:
            from pywinauto.controls.uiawrapper import UIAWrapper
            from pywinauto.uia_element_info import UIAElementInfo
            self._w = UIAWrapper(UIAElementInfo(self._e))
        return self._w


_SCAN = {}


def uia_scan(root):
    """Mọi phần tử con của `root` (wrapper UIA) dưới dạng Node – một lần FindAllBuildCache. Lỗi → None (dùng cách cũ)."""
    try:
        if "cr" not in _SCAN:
            from pywinauto.uia_defines import IUIA
            u = IUIA()
            cr = u.iuia.CreateCacheRequest()
            for pid in (30005, 30003, 30011, 30012, 30001, 30022, 30045):   # Name, ControlType, AutomationId, ClassName,
                cr.AddProperty(pid)                                       # BoundingRectangle, IsOffscreen, Value
            _SCAN.update(u=u, cr=cr, ids=dict(u.known_control_type_ids))
        u, cr, ids = _SCAN["u"], _SCAN["cr"], _SCAN["ids"]
        arr = root.element_info.element.FindAllBuildCache(4, u.true_condition, cr)     # 4 = TreeScope_Descendants
        out = []
        for i in range(arr.Length):
            e = arr.GetElement(i)
            try:
                rc = e.CachedBoundingRectangle
                rect = (rc.left, rc.top, rc.right, rc.bottom)
            except Exception:
                rect = (0, 0, 0, 0)
            try:
                val = e.GetCachedPropertyValue(30045)
                val = val if isinstance(val, str) else ""
            except Exception:
                val = ""
            try:
                out.append(Node(e, ids.get(e.CachedControlType, ""), nfc(e.CachedName or ""), e.CachedAutomationId or "",
                                e.CachedClassName or "", rect, bool(e.CachedIsOffscreen), nfc(val)))
            except Exception:
                continue
        return out
    except Exception as e:
        if not _SCAN.get("warned"):
            _SCAN["warned"] = True
            print("   (quét nhanh UIA không dùng được – tìm theo cách cũ: %s)" % e)
        return None


# ---------------------------------------------------------------- Edusoft
class Edusoft:
    def __init__(self):
        self.exe = CFG["exe"]
        self.app = None
        self.main = None
        self.login = None
        self.version = ""

    # --- tìm phần tử
    def pid(self):
        try:
            return self.app.process
        except Exception:
            return None

    def top_handles(self):
        """Mọi cửa sổ cấp cao nhất đang hiện của tiến trình Edusoft, kể cả hộp thoại thông báo
        (lấy qua Win32 – UI Automation hay xếp thông báo vào trong cửa sổ cha nên dễ bỏ sót)."""
        pid = self.pid()
        if not pid:
            return []
        out = []
        try:
            for w in Desktop(backend="win32").windows(process=pid, visible_only=True):
                try:
                    r = w.rectangle()
                    if r.width() >= 150 and r.height() >= 60:
                        out.append(w.handle)
                except Exception:
                    continue
        except Exception:
            pass
        return out

    def uia(self, handle):
        return Desktop(backend="uia").window(handle=handle).wrapper_object()

    def all_handles(self):
        """Mọi cửa sổ cấp cao đang hiện của Edusoft, kể cả danh sách thả xuống nhỏ (không lọc kích thước)."""
        pid = self.pid()
        try:
            return {w.handle for w in Desktop(backend="win32").windows(process=pid, visible_only=True)} if pid else set()
        except Exception:
            return set()

    def new_popups(self, before):
        """Cửa sổ mới hiện ra so với `before` (all_handles), gồm cả danh sách thả xuống của ô tra cứu / ô lưới."""
        main_h = getattr(self.main, "handle", None)
        out = []
        for h in self.all_handles() - set(before or ()):
            if h == main_h:
                continue
            try:
                w = self.uia(h)
                r = w.rectangle()
                if r.width() >= 20 and r.height() >= 15:
                    out.append(w)
            except Exception:
                continue
        return out

    def windows(self):
        hs = self.top_handles()
        if hs:
            out = []
            for h in hs:
                try:
                    out.append(self.uia(h))
                except Exception:
                    pass
            return out
        try:
            return self.app.windows()
        except Exception:
            return []

    def find(self, text, root=None, types=None, timeout=8, exact=False):
        root = root or self.main
        want = norm(text)
        end = time.time() + timeout
        while True:
            best = None
            for el in root.descendants():
                try:
                    if types and el.element_info.control_type not in types:
                        continue
                    name = norm(el.window_text())
                    if not name:
                        continue
                    if name == want or (not exact and (name.startswith(want) or (want.startswith(name.rstrip(".…")) and len(name) > 8))):
                        if el.is_visible():
                            best = el
                            if name == want:
                                break
                except Exception:
                    continue
            if best is not None:
                return best
            if time.time() > end:
                raise LookupError("Không tìm thấy \"%s\" trên màn hình" % text)
            time.sleep(0.5)

    def field_near(self, label):
        """Ô nhập nằm bên phải (hoặc ngay dưới) nhãn có chữ `label`."""
        lab = self.find(label, types=("Text", "Group", "Pane", "Custom"))
        lr = lab.rectangle()
        cands = []
        for el in self.main.descendants(control_type="Edit"):
            try:
                if not el.is_visible():
                    continue
                r = el.rectangle()
                same_row = abs((r.top + r.bottom) / 2 - (lr.top + lr.bottom) / 2) < 14 and r.left >= lr.left
                below = 0 <= r.top - lr.bottom < 40 and abs(r.left - lr.left) < 60
                if same_row or below:
                    cands.append((abs(r.left - lr.right) + abs(r.top - lr.top), el))
            except Exception:
                continue
        if not cands:
            raise LookupError("Không thấy ô nhập cạnh nhãn \"%s\"" % label)
        return sorted(cands, key=lambda x: x[0])[0][1]

    # --- thao tác hiện rõ
    def mark(self, el):
        try:
            el.draw_outline(colour="red", thickness=3)
        except Exception:
            pass
        time.sleep(ACTION_DELAY)

    def click(self, el, double=False):
        self.mark(el)
        (el.double_click_input if double else el.click_input)()
        time.sleep(ACTION_DELAY)

    def type_into(self, el, value):
        self.mark(el)
        el.click_input()
        pkb.send_keys("{END}" + "{BACKSPACE}" * 40, pause=0.005)
        pkb.send_keys(esc_keys(value), with_spaces=True, pause=TYPE_PAUSE)
        time.sleep(ACTION_DELAY)

    def field_value(self, el):
        for get in (lambda: el.get_value(), lambda: el.iface_value.CurrentValue, lambda: el.window_text()):
            try:
                v = get()
                if v is not None:
                    return nfc(v)
            except Exception:
                continue
        return None

    def root_handle(self, el):
        """Cửa sổ cấp cao THẬT chứa phần tử (Win32 GetAncestor GA_ROOT). Không dùng top_level_parent() của UIA:
        UIA xếp form con của Edusoft (vd "Chi tiết lý lịch sinh viên" khi bấm Thêm mới 1 SV, Danh sách lớp…) vào trong
        cửa sổ chính nên top_level_parent() trả về cửa sổ chính – lượt 03/11 01:05 vì thế đã tự đóng nhầm form."""
        e = el
        for _ in range(40):
            if e is None:
                return None
            try:
                h = e.element_info.handle
            except Exception:
                h = None
            if h:
                try:
                    import ctypes
                    return ctypes.windll.user32.GetAncestor(h, 2) or h
                except Exception:
                    return h
            try:
                e = e.parent()
            except Exception:
                return None
        return None

    def is_form(self, w):
        """Form nhập liệu / chọn (có khung nhập AQDetailRight, lưới, tab) – KHÁC hộp thông báo; kit không tự đóng form."""
        nodes = uia_scan(w)
        if nodes is not None:
            return any(nd.aid in ("AQDetailRight", "AQViewL", "viewDataCtrl") or nd.ct in ("Table", "DataGrid", "Tab") for nd in nodes)
        try:
            for el in w.descendants():
                ei = el.element_info
                if ei.automation_id in ("AQDetailRight", "AQViewL", "viewDataCtrl") or ei.control_type in ("Table", "DataGrid", "Tab"):
                    return True
        except Exception:
            pass
        return False

    def focus(self, el):
        """Đưa con trỏ bàn phím vào đúng phần tử qua UI Automation (không bấm theo toạ độ màn hình,
        vì toạ độ hay lệch khi máy có 2 màn hình / tỉ lệ hiển thị khác nhau)."""
        try:
            h = self.root_handle(el)
            (self.uia(h) if h else el.top_level_parent()).set_focus()
        except Exception:
            pass
        try:
            el.set_focus()
        except Exception:
            return False
        time.sleep(0.15)
        try:
            return bool(el.has_keyboard_focus())
        except Exception:
            # Không kiểm được con trỏ đang ở đâu → coi như CHƯA vào (press() sẽ bấm chuột). Trước đây coi là vào rồi
            # và gửi Space: ở hộp "Xác nhận xóa…?" con trỏ mặc định nằm ở Không → Space bấm nhầm Không (lượt 03/11).
            return False

    def set_field(self, el, value, secret=False):
        """Điền ô nhập bằng BÀN PHÍM THẬT (Edusoft/DevExpress chỉ ghi nhận giá trị khi được gõ):
        đưa con trỏ vào đúng ô qua UI Automation (không bấm theo toạ độ), xác nhận ô đang có con trỏ,
        xóa bằng End + Backspace rồi gõ. Ô thường được đọc lại để kiểm tra. Trả về True nếu đúng."""
        self.close_dialogs(3, keep=self.root_handle(el))   # chỉ đóng hộp thông báo, không đóng form chứa ô
        value = str(value)
        self.mark(el)
        for attempt in range(3):
            if not self.focus(el):
                if attempt < 2:
                    time.sleep(0.5)
                    continue
                try:
                    el.click_input()          # lần cuối: bấm thẳng vào ô
                    time.sleep(0.2)
                except Exception:
                    continue
            pkb.send_keys("{END}" + "{BACKSPACE}" * 60, pause=0.003)
            if not self.focus(el):
                continue
            if value:
                pkb.send_keys(esc_keys(value), with_spaces=True, pause=TYPE_PAUSE)
            time.sleep(0.3)
            if secret:
                return True
            got = self.field_value(el)
            if got is None or got.strip() == value:
                return True
        return False

    def press(self, el):
        """Bấm nút: hiện khung đỏ, đưa con trỏ vào nút rồi nhấn phím Space (không bấm theo toạ độ;
        không dùng Invoke vì Invoke có thể treo khi nút mở hộp thoại)."""
        self.mark(el)
        if self.focus(el):
            pkb.send_keys("{SPACE}")
        else:
            el.click_input()
        time.sleep(ACTION_DELAY)

    def dialogs_other(self):
        skip = {getattr(self.login, "handle", None), getattr(self.main, "handle", None)}
        return [d for d in self.windows() if d.handle not in skip]

    def wait_dialog(self, timeout=8):
        end = time.time() + timeout
        while time.time() < end:
            ds = self.dialogs_other()
            if ds:
                time.sleep(0.6)
                return ds
            if self.find_main() is not None:
                return []
            time.sleep(0.4)
        return []

    def close_dialogs(self, timeout=8, keep=None, forms=False):
        """Đóng THÔNG BÁO: bấm nút Đóng/OK NẰM TRONG hộp thoại (không đụng nút Đóng của khung đăng nhập);
        không có nút thì Enter; vẫn còn thì gửi lệnh đóng cửa sổ. Chờ tới khi không còn hộp thoại.
        Form nhập liệu / chọn (is_form) KHÔNG bị đóng trừ khi forms=True – các menu Edusoft hay mở form con
        (Thêm mới 1 SV, Danh sách lớp, Import…) và bước tiếp theo cần form đó."""
        end = time.time() + timeout
        tries = 0
        formc = {}

        def targets():
            out = []
            for d in self.dialogs_other():
                if d.handle == keep:
                    continue
                if not forms:
                    if d.handle not in formc:
                        formc[d.handle] = self.is_form(d)
                    if formc[d.handle]:
                        continue
                out.append(d)
            return out

        while time.time() < end:
            ds = targets()
            if not ds:
                if self.login is not None:
                    try:
                        self.login.set_focus()
                    except Exception:
                        pass
                time.sleep(0.4)
                return True
            tries += 1
            for d in ds:
                try:
                    d.set_focus()
                except Exception:
                    pass
                done = False
                if tries <= 2:
                    el = self.dialog_button(d, ("đóng", "ok", "close"), ("không", "no", "hủy", "cancel"), ("đồng ý",))
                    if el is not None:
                        self.press(el)
                        done = True
                if not done and tries <= 3:
                    pkb.send_keys("{ENTER}")
                elif not done:
                    try:
                        Desktop(backend="win32").window(handle=d.handle).wrapper_object().close()
                    except Exception:
                        pass
            time.sleep(0.8)
        return not targets()

    def kill(self):
        try:
            if self.app is not None:
                self.app.kill()
        except Exception:
            pass
        self.app = self.main = self.login = None
        time.sleep(2)

    def restart_to_login(self):
        self.kill()
        self.launch()
        return self.wait_login(60)

    # --- khởi động & đăng nhập (CHUNG-001)
    def launch(self):
        CAP.show("Mở Edusoft", self.exe)
        if not os.path.isfile(self.exe):
            raise FileNotFoundError("Không tìm thấy file: " + self.exe)
        self.app = Application(backend="uia").start('"%s"' % self.exe, work_dir=str(Path(self.exe).parent), timeout=90)

    def wait_login(self, timeout=90):
        end = time.time() + timeout
        while time.time() < end:
            for w in self.windows():
                try:
                    if self.main is None and w.descendants(control_type="Edit") and re.search(r"edusoft", w.window_text(), re.I):
                        time.sleep(2)
                        self.login = w
                        return w
                except Exception:
                    pass
            time.sleep(1)
        raise RuntimeError("Không thấy khung đăng nhập sau %d giây (khung có thể hiện đen – thử chạy lại)" % timeout)

    def login_fields(self):
        """Tìm ĐÚNG ô Tên đăng nhập và ô Mật khẩu. Ô DevExpress thường lộ ra 2 phần tử Edit lồng nhau
        (khung ngoài + ô gõ bên trong) cùng một hàng, nên không thể lấy "2 ô đầu tiên":
        gom theo hàng, ô mật khẩu là ô có thuộc tính IsPassword (hoặc hàng thứ 2), ô tên đăng nhập
        là hàng ngay phía trên ô mật khẩu; trong mỗi hàng lấy phần tử trong cùng (nhỏ nhất)."""
        eds = []
        for e in self.login.descendants(control_type="Edit"):
            try:
                if e.is_visible():
                    r = e.rectangle()
                    if r.width() > 40 and r.height() > 8:
                        eds.append(e)
            except Exception:
                continue

        def is_pw(e):
            try:
                return bool(e.element_info.element.CurrentIsPassword)
            except Exception:
                return False

        def inner(group):
            return sorted(group, key=lambda e: e.rectangle().width() * e.rectangle().height())[0]

        rows = []
        for e in sorted(eds, key=lambda e: e.rectangle().top):
            t = (e.rectangle().top + e.rectangle().bottom) / 2
            for g in rows:
                if abs(g["mid"] - t) < 10:
                    g["els"].append(e)
                    break
            else:
                rows.append({"mid": t, "els": [e]})
        if len(rows) < 2:
            raise RuntimeError("Khung đăng nhập không có đủ ô Tên đăng nhập / Mật khẩu")
        pw_row = None
        for i, g in enumerate(rows):
            if any(is_pw(e) for e in g["els"]):
                pw_row = i
                break
        if pw_row is None or pw_row == 0:
            pw_row = 1
        u = inner(rows[pw_row - 1]["els"])
        p = inner([e for e in rows[pw_row]["els"] if is_pw(e)] or rows[pw_row]["els"])
        if u.rectangle().top >= p.rectangle().top:
            raise RuntimeError("Không phân biệt được ô Tên đăng nhập và ô Mật khẩu")
        self.pw_el = p
        return u, p

    def login_reacted(self, timeout=5):
        """Sau khi bấm Đăng nhập: có thông báo / vào màn hình chính / khung đăng nhập đóng hoặc đang xử lý?"""
        end = time.time() + timeout
        while time.time() < end:
            if self.dialogs_other():
                return "có thông báo"
            if self.find_main() is not None:
                return "vào màn hình chính"
            try:
                if not self.login.exists(timeout=0) or not self.login.is_visible():
                    return "khung đăng nhập đã đóng"
                if not self.login.is_enabled():
                    return "khung đăng nhập đang xử lý"
            except Exception:
                return "khung đăng nhập đã đóng"
            time.sleep(0.3)
        return None

    def login_button(self):
        for el in self.login.descendants(control_type="Button"):
            try:
                if norm(el.window_text()).replace("&", "") == "đăng nhập" and el.is_visible():
                    return el
            except Exception:
                continue
        try:
            return self.find("Đăng nhập", root=self.login, timeout=5)
        except Exception:
            return None

    def click_login(self):
        """Bấm nút Đăng nhập và XÁC NHẬN Edusoft có phản hồi. Không phản hồi thì lần lượt thử:
        phím Space trên nút → phím Enter trong ô Mật khẩu → bấm chuột vào nút → lệnh Invoke (chạy nền, không treo script).
        Trả về chuỗi mô tả cách đã bấm; "khóa" nếu nút Đăng nhập đang bị vô hiệu hóa."""
        self.close_dialogs(3)
        btn = self.login_button()
        try:
            if btn is not None and not btn.is_enabled():
                self.mark(btn)
                return "khóa"
        except Exception:
            pass

        def space():
            self.mark(btn)
            if not self.focus(btn):
                raise RuntimeError("không đưa được con trỏ vào nút")
            pkb.send_keys("{SPACE}")

        def enter():
            pw = getattr(self, "pw_el", None)
            if pw is None or not self.focus(pw):
                raise RuntimeError("không đưa được con trỏ vào ô Mật khẩu")
            pkb.send_keys("{ENTER}")

        def mouse():
            self.mark(btn)
            btn.click_input()

        def invoke():
            threading.Thread(target=lambda: btn.invoke(), daemon=True).start()

        tried = []
        for label, fn in (("phím Space trên nút", space), ("phím Enter trong ô Mật khẩu", enter),
                          ("bấm chuột vào nút", mouse), ("lệnh Invoke", invoke)):
            if btn is None and fn is not enter:
                continue
            try:
                fn()
            except Exception as e:
                tried.append("%s (%s)" % (label, e))
                continue
            res = self.login_reacted(5)
            if res:
                self.last_click = "%s → %s" % (label, res)
                return self.last_click
            tried.append(label + " (không phản hồi)")
        raise RuntimeError("Bấm Đăng nhập không có phản hồi – đã thử: " + "; ".join(tried))

    def find_main(self):
        for w in self.windows():
            try:
                t = w.window_text()
            except Exception:
                continue
            if re.search(r"EduSoft\.NET\s*\[", t):
                return w
        return None

    def wait_main(self, timeout=90):
        end = time.time() + timeout
        while time.time() < end:
            w = self.find_main()
            if w is not None:
                self.main = w
                m = re.search(r"\[(v[^\]]+)\]", w.window_text())
                self.version = m.group(1) if m else ""
                try:
                    w.set_focus()
                except Exception:
                    pass
                time.sleep(3)
                return True
            time.sleep(1)
        return False

    def start_and_login(self, account, password):
        self.launch()
        self.wait_login()
        u, pw = self.login_fields()
        CAP.show("Đăng nhập", "Tài khoản " + account)
        if not self.set_field(u, account):
            raise RuntimeError("Không nhập được tên đăng nhập đúng")
        self.set_field(pw, password, secret=True)
        self.click_login()
        if not self.wait_main():
            raise RuntimeError("Đăng nhập không vào được màn hình chính (sai tài khoản/mật khẩu hoặc lỗi máy chủ)")

    # --- menu
    def open_menu(self, path):
        """Mở menu theo đường dẫn tài liệu "A/ B/ C": mỗi cấp tìm trên mọi cửa sổ của Edusoft
        (menu thả xuống là cửa sổ riêng), mục cuối là cây/danh sách thì bấm đúp."""
        segs = menu_segs(path)
        if not segs:
            return
        self.last_menu = path
        for i, s in enumerate(segs):
            last = i == len(segs) - 1
            el = self.find_any(s, roots=[self.main] if i == 0 else None, timeout=12,
                               types=("TabItem", "MenuItem", "Button", "SplitButton", "TreeItem", "DataItem", "ListItem", "Hyperlink", "Text", "Custom") if i == 0 else None)
            ct = el.element_info.control_type
            if ct == "TabItem":
                self.mark(el)
                try:
                    el.select()                   # tab ribbon (Hệ thống, Sinh viên…)
                except Exception:
                    el.click_input()
            elif ct == "TreeItem" and not last:
                self.expand_node(el)              # nhóm trên cây chức năng: mở nhóm để thấy mục con
            else:
                self.click(el, double=(last and ct in ("TreeItem", "DataItem", "ListItem")))
            time.sleep(0.8)
        time.sleep(1.5)                            # chờ màn hình chức năng mở xong

    def expand_node(self, el):
        """Bấm chọn nhóm trên cây rồi mở nhóm (ExpandCollapse); không được thì bấm đúp – chỉ khi nhóm đang đóng,
        vì bấm đúp nhóm đang mở sẽ đóng nó lại."""
        self.click(el)
        try:
            st = el.iface_expand_collapse.CurrentExpandCollapseState     # 0 đóng · 1 mở · 2 mở một phần · 3 lá
        except Exception:
            st = None
        if st in (1, 2, 3):
            return
        try:
            el.iface_expand_collapse.Expand()
            return
        except Exception:
            pass
        if st == 0:
            self.click(el, double=True)
        else:
            pkb.send_keys("{RIGHT}")             # cây DevExpress: phím phải mở nhóm đang chọn

    # --- hộp thoại / lỗi
    def keep_open(self):
        """Có hộp "Thoát khỏi chương trình?" (do phím Esc ở cửa sổ chính) thì bấm Không – không để Edusoft bị đóng."""
        for d in self.dialogs():
            try:
                if "thoát khỏi chương trình" in self.dialog_text(d).lower():
                    no = self.dialog_button(d, ("không", "no"))
                    if no is not None:
                        self.press(no)
                        time.sleep(0.8)
                        print("   Đã bấm Không ở hộp \"Thoát khỏi chương trình?\"")
            except Exception:
                continue

    def dialogs(self):
        main = getattr(self.main, "handle", None)
        return [w for w in self.windows() if w.handle != main]

    # Hộp thoại của khung AQ (AQControls.AQMessageBox): MsgBox – nội dung ở "lblMessage", nút btn1/btn2/btn3;
    # ErrorMsgBox – lỗi hệ thống ("Đã xảy ra lỗi khi xử lý nghiệp vụ… [Gửi mail về Support]"): lblThongBao, rtxt_Error.
    MSG_IDS = ("lblMessage",)
    ERR_IDS = ("rtxt_Error", "lblThongBao", "btnViewErrorHelp", "btnViewErrorHelpDetail", "btnViewErrorData")

    def dialog_info(self, w):
        """(loại, chữ): loại = "error" (ErrorMsgBox), "msg" (MsgBox) hoặc "" (cửa sổ khác); chữ đưa nội dung chính lên đầu."""
        kind, main, parts = "", [], []
        try:
            for el in w.descendants():
                try:
                    aid = el.element_info.automation_id or ""
                except Exception:
                    aid = ""
                try:
                    t = el.window_text()
                    if not t and aid == "rtxt_Error":
                        t = el.iface_value.CurrentValue
                except Exception:
                    t = ""
                if aid in self.ERR_IDS:
                    kind = "error"
                elif aid in self.MSG_IDS and kind != "error":
                    kind = "msg"
                if not t:
                    continue
                if aid in self.MSG_IDS or aid in ("lblThongBao", "rtxt_Error"):
                    main.append(t)
                elif t not in parts:
                    parts.append(t)
        except Exception:
            pass
        txt = nfc("\n".join(main + [p for p in parts if p not in main]))
        if kind == "error":
            txt = "[Lỗi hệ thống Edusoft] " + txt
        return kind, txt

    def dialog_text(self, w):
        return self.dialog_info(w)[1]

    def is_error_dialog(self, w, txt=None):
        """Hộp lỗi hệ thống: ErrorMsgBox của Edusoft hoặc chữ có dấu hiệu exception."""
        kind, t = self.dialog_info(w)
        return kind == "error" or bool(EX_PAT.search(txt if txt is not None else t))

    # --- tìm phần tử trên mọi cửa sổ của Edusoft (menu thả xuống, hộp thoại, form con…)
    def dialog_button(self, d, *groups):
        """Nút trong hộp thoại theo thứ tự ưu tiên của các nhóm tên; KHÔNG bao giờ tự bấm Có/Yes."""
        btns = []
        try:
            for el in d.descendants(control_type="Button"):
                try:
                    if el.is_visible():
                        btns.append((norm_label(el.window_text()), el))
                except Exception:
                    continue
        except Exception:
            return None
        names = {n for n, _ in btns}
        for g in groups:
            if g == ("đồng ý",) and names & {"không", "no"}:
                continue
            for n, el in btns:
                if n in g:
                    return el
        return None

    def handles(self):
        return set(self.top_handles())

    def new_windows(self, before):
        out = []
        for w in self.windows():
            try:
                if w.handle not in before and w.handle != getattr(self.main, "handle", None):
                    out.append(w)
            except Exception:
                continue
        return out

    def roots(self):
        """Cửa sổ để tìm phần tử: hộp thoại / form con đang mở trước, cửa sổ chính sau cùng."""
        main_h = getattr(self.main, "handle", None)
        ws = self.windows()
        others = [w for w in ws if w.handle != main_h]
        return others + ([self.main] if self.main is not None else [])

    MENU_TYPES = ("MenuItem", "TabItem", "Button", "SplitButton", "TreeItem", "ListItem", "Hyperlink", "Text", "Custom", "DataItem")

    def find_any(self, text, types=None, timeout=10, roots=None, exclude=None):
        wants = [norm_label(x) for x in alts_of(text)]
        types = types or self.MENU_TYPES
        end = time.time() + timeout
        while True:
            for root in (roots or self.roots()):
                nodes = uia_scan(root)
                if nodes is not None:                   # nhanh: một lần quét, so tên/giá trị trên dữ liệu đọc sẵn
                    best = None
                    ex = [getattr(x, "element_info", None) for x in (exclude or [])]
                    for t in types:
                        for nd in nodes:
                            if nd.ct != t or not nd.visible:
                                continue
                            names = [norm_label(nd.name)]
                            if t in ("TreeItem", "DataItem", "ListItem", "Custom", "Text") or not nd.name:
                                names.append(norm_label(nd.val))
                            names = [n for n in names if n]
                            if not names:
                                continue
                            hit = any(n == w for n in names for w in wants)
                            near = any(n.startswith(w) and len(w) >= 3 for n in names for w in wants)
                            if not (hit or near):
                                continue
                            w_ = nd.wrap()
                            if ex and w_.element_info in ex:
                                continue
                            if hit:
                                return w_
                            best = best or w_
                    if best is not None:
                        return best
                    continue
                best = None
                for t in types:
                    try:
                        els = root.descendants(control_type=t)
                    except Exception:
                        continue
                    for el in els:
                        try:
                            names = [norm_label(el.window_text())]
                            if t in ("TreeItem", "DataItem", "ListItem", "Custom", "Text"):
                                try:
                                    names.append(norm_label(el.iface_value.CurrentValue))   # cây chức năng: tên nằm ở Value
                                except Exception:
                                    pass
                            names = [n for n in names if n]
                            if not names or (exclude and el in exclude):
                                continue
                            hit = any(n == w for n in names for w in wants)
                            near = any(n.startswith(w) and len(w) >= 3 for n in names for w in wants)
                            if (hit or near) and el.is_visible():
                                if hit:
                                    return el
                                best = best or el
                        except Exception:
                            continue
                if best is not None:
                    return best
            if time.time() > end:
                raise LookupError("Không tìm thấy \"%s\" trên màn hình" % text)
            time.sleep(0.5)

    def field_for(self, label, timeout=8):
        """Ô nhập cho nhãn `label` (có thể nhiều tên cách nhau bằng |). Trả về (ô, nhãn); ô = None nếu
        giao diện là lưới dọc (ô chỉ hiện khi bấm vào dòng) – khi đó gõ theo vị trí bên phải nhãn."""
        ids = [x[1:].strip() for x in alts_of(label) if x.strip().startswith("#")]
        if ids:                                   # "#SoQDSV": tên control (automationId) – nhãn Edusoft không có trong UIA
            el = self.by_id(ids, timeout=timeout)
            return el, el
        lab = self.find_any(label, types=("Text", "Custom", "Pane", "Group", "TreeItem", "ListItem", "DataItem"), timeout=timeout)
        lr = lab.rectangle()
        lm = (lr.top + lr.bottom) / 2
        rh = self.root_handle(lab)
        root = self.uia(rh) if rh else lab.top_level_parent()
        cands = []
        for t in ("Edit", "ComboBox", "Spinner", "Document"):
            try:
                els = root.descendants(control_type=t)
            except Exception:
                continue
            for el in els:
                try:
                    if not el.is_visible():
                        continue
                    r = el.rectangle()
                    if r.width() < 15 or r.height() < 8:
                        continue
                    same_row = abs((r.top + r.bottom) / 2 - lm) < 14 and r.left >= lr.left + lr.width() * 0.5
                    below = 0 <= r.top - lr.bottom < 40 and abs(r.left - lr.left) < 60
                    if same_row or below:
                        cands.append((abs(r.left - lr.right) + abs(r.top - lr.top), r.width() * r.height(), el))
                except Exception:
                    continue
        if not cands:
            return None, lab
        cands.sort(key=lambda x: (round(x[0] / 25), x[1]))
        return cands[0][2], lab

    def by_id(self, ids, timeout=8):
        """Ô nhập theo tên control (automationId), vd SoQDSV, IDLDQDSV, NGAYHLQDSV: lấy ô soạn thảo thật bên trong
        (lớp WindowsForms10.EDIT) nếu có. Tìm hộp thoại / form con trước, cửa sổ chính sau."""
        end = time.time() + timeout
        while True:
            for root in self.roots():
                nodes = uia_scan(root)
                for i in ids:
                    if nodes is not None:
                        k = next((n for n, nd in enumerate(nodes) if nd.aid == i and nd.visible), None)
                        if k is None:
                            continue
                        self.last_outer = el = nodes[k].wrap()
                        ol, ot, or_, ob = nodes[k].rect
                        for nd in nodes[k + 1:k + 12]:      # ô soạn thảo thật nằm ngay sau trong cây, trong khung ô
                            if ".EDIT." in nd.cls and nd.visible and nd.inside((ol - 1, ot - 1, or_ + 1, ob + 1)):
                                return nd.wrap()
                        return el
                    try:
                        hits = [e for e in root.descendants() if e.element_info.automation_id == i and e.is_visible()]
                    except Exception:
                        continue
                    if not hits:
                        continue
                    el = hits[0]
                    self.last_outer = el                  # ô ngoài (có nút mở danh sách "Open" của ô tra cứu)
                    try:
                        inner = [e for e in el.descendants() if ".EDIT." in (e.element_info.class_name or "") and e.is_visible()]
                        if inner:
                            return inner[0]
                    except Exception:
                        pass
                    return el
            if time.time() > end:
                raise LookupError("Không tìm thấy ô #%s trên màn hình" % "|#".join(ids))
            time.sleep(0.5)

    # --- ô tra cứu (AQLockUpEdit / LookUpEdit), lưới nhập, nút theo vùng
    def popup_row(self, wins, value):
        """Dòng trong danh sách thả xuống có ô (tên hoặc giá trị) đúng bằng `value`; bỏ dòng lọc."""
        want = norm(value)
        best = None
        for w in wins:
            try:
                els = w.descendants()
            except Exception:
                continue
            for el in els:
                try:
                    if el.element_info.control_type not in ("DataItem", "ListItem", "Custom", "Text", "TreeItem", "Edit"):
                        continue
                    name = norm(el.window_text())
                    if "filter row" in name:
                        continue
                    vals = [name]
                    try:
                        vals.append(norm(el.iface_value.CurrentValue))
                    except Exception:
                        pass
                    if want in vals and el.is_visible():
                        if el.element_info.control_type in ("DataItem", "ListItem"):
                            return el
                        best = best or el
                except Exception:
                    continue
        return best

    def open_dropdown(self, outer, inner):
        """Mở danh sách của ô tra cứu: bấm nút "Open" của ô; không có thì Alt+↓ (không dùng Esc/F4)."""
        for base in [b for b in (outer, inner) if b is not None]:
            try:
                for b in base.descendants(control_type="Button"):
                    if norm(b.window_text()) in ("open", "mở", "") and b.is_visible():
                        self.mark(b)
                        b.click_input()
                        return True
            except Exception:
                continue
        if self.focus(inner):
            pkb.send_keys("%{DOWN}")
            return True
        return False

    def choose_lookup(self, outer, inner, value, typed=True, on_unknown=None):
        """CHỌN giá trị trong ô tra cứu (người dùng dạy: gõ xong phải chọn dòng đang có, không để danh sách mở):
        typed=True → gõ rồi chọn; typed=False → mở danh sách rồi chọn (không thấy dòng thì gõ để lọc rồi chọn).
        Chọn = bấm dòng khớp trong danh sách; danh sách không đọc được qua UIA → gọi on_unknown (ghi cây giao diện) rồi Enter.
        Trả về (giá trị ô sau khi chọn, cách chọn)."""
        before = self.all_handles()
        if typed:
            self.set_field(inner, value)
            time.sleep(1.0)
        pops = self.new_popups(before)
        if not pops:
            self.open_dropdown(outer, inner)
            time.sleep(1.2)
            pops = self.new_popups(before)
        row = self.popup_row(pops, value) if pops else None
        if row is None and pops and not typed:            # danh sách dài: gõ để lọc rồi tìm lại
            self.focus(inner)
            pkb.send_keys(esc_keys(value), with_spaces=True, pause=TYPE_PAUSE)
            time.sleep(1.0)
            pops = self.new_popups(before) or pops
            row = self.popup_row(pops, value)
        how = "bấm dòng %s" % value
        if row is not None:
            self.mark(row)
            row.click_input()
            time.sleep(0.8)
            if self.new_popups(before):
                try:
                    row.click_input(double=True)
                except Exception:
                    pass
                time.sleep(0.8)
        else:
            if pops and on_unknown:
                on_unknown()
            how = "Enter (không đọc được danh sách)" if pops else "Enter (không thấy danh sách)"
            self.focus(inner)
            pkb.send_keys("{ENTER}")
            time.sleep(0.8)
        if self.new_popups(before):
            how += " · danh sách vẫn mở"
        return self.field_value(inner), how

    def area_el(self, area, timeout=6):
        return self.find_any(area, types=("Table", "Group", "Pane", "Custom", "Tree", "List", "Text"), timeout=timeout)

    def find_in_area(self, text, area, timeout=10):
        """Nút `text` thuộc vùng `area` (tên lưới/khung, vd "Danh sách sinh viên"): tìm trong vùng rồi lên dần các
        khung cha (thanh nút nằm cạnh lưới) – phân biệt các nút trùng tên (Thêm của danh sách trái / của lưới con)."""
        wants = [norm_label(x) for x in alts_of(text)]
        end = time.time() + timeout
        while True:
            try:
                base = self.area_el(area, timeout=2)
            except LookupError:
                base = None
            # Lên dần tới tận cửa sổ chứa vùng (form popup "Danh sách lớp": lưới nằm sâu 8 tầng, thanh nút Export/Chọn/Đóng
            # là con trực tiếp của cửa sổ – lượt 03/11 01:14 chỉ lên 4 tầng nên không thấy nút "Chọn"). Tầng gần nhất thắng.
            top = self.root_handle(base) if base is not None else None
            for _ in range(30):
                if base is None:
                    break
                try:
                    for t in ("Button", "MenuItem", "SplitButton"):
                        for el in base.descendants(control_type=t):
                            if norm_label(el.window_text()) in wants and el.is_visible():
                                return el
                    try:
                        if top and base.element_info.handle == top:
                            break
                    except Exception:
                        pass
                    base = base.parent()
                except Exception:
                    break
            if time.time() > end:
                raise LookupError("Không thấy nút \"%s\" trong vùng \"%s\"" % (text, area))
            time.sleep(0.5)

    def grid_cell(self, col, area="", timeout=6):
        """Ô của lưới ở dòng dưới cùng (dòng vừa thêm) thuộc cột `col` (DataItem "<cột> row N"; bỏ dòng lọc)."""
        wants = [norm_label(x) for x in alts_of(col)]
        end = time.time() + timeout
        while True:
            roots = self.roots()
            if area:
                try:
                    roots = [self.area_el(area, timeout=2)]
                except LookupError:
                    pass
            for root in roots:
                cands = []
                try:
                    for el in root.descendants(control_type="DataItem"):
                        m = re.match(r"^(.*?) row (-?\d+)$", norm(el.window_text()))
                        if not m or "filter" in m.group(1) or norm_label(m.group(1)) not in wants:
                            continue
                        if el.is_visible():
                            cands.append((el.rectangle().top, el))
                except Exception:
                    continue
                if cands:
                    return max(cands, key=lambda x: x[0])[1]
            if time.time() > end:
                raise LookupError("Không thấy ô cột \"%s\" ở dòng đang nhập của lưới %s" % (col, area))
            time.sleep(0.5)

    STATUS_PAT = re.compile(r"thành công|thất bại|không thành|lỗi|không (được|thể)|đã (lưu|xóa|xoá|thêm|cập nhật)", re.I)

    def status_msg(self):
        """Thông báo trên THANH TRẠNG THÁI dưới đáy cửa sổ chính (StatusBar → Text, vd "Xóa dữ liệu thành công",
        "Cập nhật mẫu tin Chi tiết Danh sách quyết định thành công") – Edusoft báo kết quả Lưu/Xóa ở đây, không bật hộp thoại."""
        sb = getattr(self, "_sb", None)
        for attempt in range(2):
            if sb is None:
                try:
                    sb = next(iter(self.main.descendants(control_type="StatusBar")), None)
                except Exception:
                    sb = None
                self._sb = sb
            if sb is None:
                return ""
            try:
                out = [nfc(t.window_text()).strip() for t in sb.descendants(control_type="Text")]
                return " · ".join(t for t in out if t and self.STATUS_PAT.search(t))
            except Exception:
                sb = self._sb = None                      # thanh trạng thái cũ đã mất – tìm lại
        return ""

    def wait_status(self, before, timeout=8):
        """Chờ thanh trạng thái đổi khác `before` (thông báo mới sau Lưu/Xóa); trả chữ mới, hết giờ thì "" ."""
        end = time.time() + timeout
        while time.time() < end:
            m = self.status_msg()
            if m and m != before:
                return m
            time.sleep(0.5)
        return ""

    def close_screen(self, name, timeout=8):
        """Tắt màn hình chức năng bằng nút X trên tab MDI (TabItem tên màn hình → nút Close của tab)."""
        tab = self.find_any(name, types=("TabItem",), roots=[self.main], timeout=timeout)
        tr = tab.rectangle()
        btns = []
        try:
            btns = [b for b in tab.descendants(control_type="Button") if b.is_visible()]
        except Exception:
            pass
        if not btns:
            for b in self.main.descendants(control_type="Button"):
                try:
                    r = b.rectangle()
                    if norm(b.window_text()) in ("close", "đóng") and tr.left <= r.left and r.right <= tr.right + 2 \
                            and tr.top - 2 <= r.top and r.bottom <= tr.bottom + 2 and b.is_visible():
                        btns.append(b)
                except Exception:
                    continue
        if not btns:
            raise LookupError("Không thấy nút X của màn hình \"%s\"" % name)
        self.mark(btns[0])
        btns[0].click_input()
        return True

    def cell_button(self, cell, area=""):
        """Nút "…" của ô lưới (hiện khi ô đang soạn): bấm ô, tìm Button nằm trong ô; không có thì bấm mép phải ô."""
        cr = cell.rectangle()
        self.mark(cell)
        cell.click_input()
        time.sleep(0.5)
        cell.click_input()
        time.sleep(0.6)
        roots = [self.area_el(area, timeout=2)] if area else [self.main]
        for root in roots:
            try:
                for b in root.descendants(control_type="Button"):
                    r = b.rectangle()
                    if cr.left - 2 <= r.left and r.right <= cr.right + 24 and cr.top - 3 <= r.top and r.bottom <= cr.bottom + 3 \
                            and r.width() < 40 and b.is_visible():
                        self.mark(b)
                        b.click_input()
                        return "nút trong ô"
            except Exception:
                continue
        cell.click_input(coords=(max(cr.width() - 8, 1), cr.height() // 2))   # nút "…" vẽ ở mép phải ô
        return "mép phải ô"

    def type_at_label(self, lab, value):
        """Lưới dọc DevExpress: bấm vào ô giá trị bên phải nhãn rồi gõ."""
        from pywinauto import mouse
        r = lab.rectangle()
        self.mark(lab)
        mouse.click(coords=(int(r.right + 60), int((r.top + r.bottom) / 2)))
        time.sleep(0.4)
        pkb.send_keys("{END}" + "{BACKSPACE}" * 60, pause=0.003)
        if value:
            pkb.send_keys(esc_keys(value), with_spaces=True, pause=TYPE_PAUSE)
        time.sleep(0.3)

    def element_with_text(self, value, roots=None, below=None):
        """Ô trong LƯỚI DỮ LIỆU có giá trị đúng bằng `value` (không lấy ô nhập liệu của form).
        `below`: chỉ lấy ô nằm dưới toạ độ y này (bỏ qua dòng lọc vừa gõ giá trị)."""
        want = norm(value)
        for root in (roots or self.roots()):
            nodes = uia_scan(root)
            if nodes is not None:
                grids = [nd.rect for nd in nodes if nd.ct in ("Table", "DataGrid") and nd.visible]
                for nd in nodes:
                    if not nd.visible or not (nd.ct in ("DataItem", "ListItem", "TreeItem") or any(nd.inside(g) for g in grids)):
                        continue
                    if want and (want == norm(nd.name) or want == norm(nd.val)):
                        if below is not None and nd.rect[1] <= below:
                            continue
                        return nd.wrap()
                continue
            pools = []
            for g in ("Table", "DataGrid"):
                try:
                    for grid in root.descendants(control_type=g):
                        pools.append(grid.descendants())
                except Exception:
                    continue
            for t in ("DataItem", "ListItem", "TreeItem"):
                try:
                    pools.append(root.descendants(control_type=t))
                except Exception:
                    continue
            for els in pools:
                for el in els:
                    try:
                        vals = [el.window_text()]
                        try:
                            vals.append(el.iface_value.CurrentValue)
                        except Exception:
                            pass
                        if any(want and want == norm(v) for v in vals if v) and el.is_visible():
                            if below is not None and el.rectangle().top <= below:
                                continue
                            return el
                    except Exception:
                        continue
        return None

    def dump_ui(self, path, limit=6000):
        """Ghi cây giao diện mọi cửa sổ Edusoft đang mở (loại | tên | automationId | lớp | toạ độ | giá trị)."""
        lines, n = [], 0
        for w in self.windows():
            try:
                lines.append("=== CỬA SỔ: %s [%s] %s" % (w.window_text(), w.element_info.class_name, w.rectangle()))
                for el in w.descendants():
                    n += 1
                    if n > limit:
                        lines.append("... (dừng ở %d phần tử)" % limit)
                        break
                    try:
                        ei = el.element_info
                        v = ""
                        try:
                            v = el.iface_value.CurrentValue or ""
                        except Exception:
                            pass
                        if ei.control_type == "Edit" and getattr(ei.element, "CurrentIsPassword", False):
                            v = "***"
                        lines.append("%s | %s | %s | %s | %s | %s" % (ei.control_type, el.window_text()[:80], ei.automation_id, ei.class_name, el.rectangle(), str(v)[:80]))
                    except Exception:
                        continue
            except Exception as e:
                lines.append("(lỗi đọc cửa sổ: %s)" % e)
        Path(path).write_text("\n".join(lines), "utf-8")
        return n


# không bắt chữ "System." trơn: ô ảnh của Edusoft tên "System.Drawing.Bitmap" (báo nhầm lỗi EX lượt 03/11 00:29)
EX_PAT = re.compile(r"exception|object reference|stack ?trace|lỗi hệ thống|unhandled|\bat system\.[a-z]", re.I)


# ---------------------------------------------------------------- lượt chạy
class Run:
    def __init__(self, sc, es):
        self.sc = sc
        self.es = es
        ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        self.id = "sc-%s-%s" % (sc["code"].lower(), ts)
        self.dir = BASE / "results" / self.id
        self.dir.mkdir(parents=True, exist_ok=True)
        self.steps = [dict(res=None, shots=[], at=None, note="") for _ in sc.get("steps", [])]
        self.alts = [dict(res=None, shots=[], at=None, note="") for _ in sc.get("altFlows", [])]
        self._filter = None                             # ô tìm kiếm của lưới đang gõ (để xoá sau)
        self.bugs = []
        self.log = []
        self.halt = False          # người test đã xử lý bước lỗi → dừng luồng đang chạy, test tiếp luồng khác
        self.abort = False         # người test bấm "Dừng test"
        self.started = now_iso()
        self.video = None
        self.dumps = []
        self.notes = []
        t = datetime.datetime.now()
        base = {"ddHHMM": t.strftime("%d%H%M"), "yymmdd": t.strftime("%y%m%d"), "HHMMSS": t.strftime("%H%M%S"), "ddmmyyyy": t.strftime("%d/%m/%Y")}
        self.vars = dict(base)
        for k, v in (sc.get("vars") or {}).items():
            self.vars[k] = self.expand(str(v))

    def expand(self, text):
        return re.sub(r"\{([A-Za-z_][A-Za-z0-9_]*)\}", lambda m: str(self.vars.get(m.group(1), m.group(0))), str(text or ""))

    def dump(self, name):
        import unicodedata
        slug = unicodedata.normalize("NFD", name.lower().replace("đ", "d"))
        slug = "".join(c for c in slug if unicodedata.category(c) != "Mn")
        fn = "ui-%s.txt" % re.sub(r"[^a-z0-9-]+", "-", slug).strip("-")
        try:
            n = self.es.dump_ui(self.dir / fn)
            if fn not in self.dumps:
                self.dumps.append(fn)
            self.say("Đã ghi cây giao diện (%d phần tử) vào %s" % (n, fn))
        except Exception as e:
            self.say("Không ghi được cây giao diện: %s" % e)

    def say(self, line):
        self.log.append(stamp() + "  " + line)
        print("  ", line)

    def shot(self, name):
        try:
            box = None
            target = self.es.main if self.es.main is not None else self.es.login
            if target is not None:
                r = target.rectangle()
                pad = 0 if target is self.es.main else 220   # khung đăng nhập: chụp rộng ra để thấy cả thông báo
                box = (r.left - pad, r.top - pad // 2, r.right + pad, r.bottom + pad)
            CAP.hidden(True)
            try:
                img = ImageGrab.grab(bbox=box, all_screens=True)
            finally:
                CAP.hidden(False)
            import unicodedata
            slug = unicodedata.normalize("NFD", str(name).lower().replace("đ", "d"))
            slug = re.sub(r"[^a-z0-9-]+", "-", "".join(c for c in slug if unicodedata.category(c) != "Mn")).strip("-") or "anh"
            fn = slug + ".png"
            img.save(self.dir / fn)
            return fn
        except Exception as e:
            self.say("Không chụp được ảnh: %s" % e)
            return None

    def check_ex(self, rec, label, kind, idx, text):
        """Phát hiện hộp thoại lỗi EX sau thao tác; nếu có thì lấy chi tiết + menu code."""
        for d in self.es.dialogs():
            body = self.es.dialog_text(d)
            if not self.es.is_error_dialog(d, body):
                continue
            CAP.show("Phát hiện lỗi EX", label + " · lấy chi tiết (Ctrl+Shift+E) và menu code (Ctrl+Shift+F)")
            shots = []
            pkb.send_keys("^+e")
            time.sleep(2)
            detail = "\n".join(self.es.dialog_text(x) for x in self.es.dialogs()) or body
            s = self.shot("%s-ex" % label.lower())
            if s:
                shots.append(s)
            pkb.send_keys("{ESC}")
            time.sleep(1)
            pkb.send_keys("^+f")
            time.sleep(2)
            code_txt = "\n".join(self.es.dialog_text(x) for x in self.es.dialogs())
            m = re.search(r"([A-Za-z]{2,}[A-Za-z0-9_\.]*\d+[A-Za-z0-9_]*)", code_txt or "")
            s2 = self.shot("%s-menucode" % label.lower())
            if s2:
                shots.append(s2)
            pkb.send_keys("{ESC}")
            rec["res"] = "bad"
            rec["note"] = "Lỗi EX" + (" · menu code " + m.group(1) if m else "")
            rec["shots"] += shots
            self.bugs.append(dict(kind=kind, stepIndex=idx, stepText=text, type="ex", exDetail=detail[:4000], menuCode=m.group(1) if m else "", shots=shots))
            self.say("%s: LỖI EX%s" % (label, " (menu code %s)" % m.group(1) if m else ""))
            return True
        return False

    # --- thực hiện một bước
    def do_actions(self, actions, label=""):
        """Ngôn ngữ thao tác (mỗi dòng một lệnh, giá trị có thể dùng biến {TEN_BIEN} của kịch bản):
          menu: A/ B/ C                 mở menu
          click: Thêm|Thêm mới          bấm nút / mục (nhiều tên cách nhau |)
          type: Nhãn|Nhãn khác = giá trị   gõ vào ô cạnh nhãn (ô trống: "= ")
          type: #TenControl = giá trị     gõ vào ô theo tên control (automationId trong ui-*.txt, vd #SoQDSV) –
                                         dùng cho màn hình Edusoft vì nhãn ô không có trong cây giao diện
          select: Nhãn|#Ten = giá trị     ô tra cứu/danh sách: gõ giá trị rồi CHỌN dòng khớp trong danh sách thả xuống
                                         (ô theo #Ten; ô theo nhãn thì gõ rồi Enter như cũ)
          choose: #Ten = giá trị         mở danh sách của ô (nút ▾) rồi bấm chọn dòng khớp, không gõ trước
          cell: Cột = giá trị @ Lưới     gõ vào ô của cột ở dòng đang nhập (dòng dưới cùng) của lưới "Lưới"
          cellbtn: Cột @ Lưới            bấm nút "…" của ô (dòng dưới cùng) – mở cửa sổ chọn (vd Danh sách lớp → find_row → Chọn)
          close: Tên màn hình            tắt màn hình chức năng bằng nút X trên tab (test xong chức năng nào tắt chức năng đó)
          click: Nút @ Vùng              bấm nút thuộc vùng (vd "Thêm @ Danh sách sinh viên" ≠ Thêm của danh sách trái)
          save: Lưu                      bấm Lưu và kiểm tra thông báo (lỗi → bước Lỗi)
                                         + đọc THANH TRẠNG THÁI dưới đáy ("… thành công") – Edusoft báo kết quả ở đó
          expect: chữ                    chờ chữ xuất hiện trên màn hình
          expect_dialog: mẫu|mẫu         phải có thông báo khớp mẫu; ghi lại nội dung rồi đóng
          find_row: giá trị @ Cột|Cột    tìm dòng: gõ giá trị vào Ô TÌM KIẾM của cột (dòng lọc có icon phễu ngay dưới
                                         tiêu đề cột) rồi chọn dòng khớp; không ghi cột thì chỉ xem các dòng đang hiện
          delete_row: giá trị @ Cột      xóa dòng; form "Danh sách đang chọn để xóa" chỉ được có dòng mang giá trị → tick → Thực hiện;
                                         hộp "Xác nhận xóa…?" chỉ bấm Có khi nêu đúng giá trị hoặc đã kiểm form
          cancel                         hủy thao tác đang nhập (không lưu)
          dump: tên                      ghi cây giao diện ra file ui-tên.txt
          unique: BIẾN @ Cột             giá trị {BIẾN} không được có sẵn trong lưới đang mở – có thì tự đổi
                                         giá trị test khác (mã: đổi số cuối · tên: lấy tên test khác) rồi tìm lại
          pick: BIẾN = lọc|lọc @ cột     đọc các dòng của lưới đang mở, giữ dòng có chữ "lọc", chọn NGẪU NHIÊN
                                         một dòng: {BIẾN} = ô của cột (không ghi cột = ô đầu), {BIẾN_DONG} = cả dòng
          absent: giá trị @ Cột          giá trị KHÔNG còn trong lưới (kiểm tra sau khi xóa)
                                         vẫn thấy → tắt màn hình (X), mở lại menu, kiểm tra lần nữa
          shot: tên                      chụp ảnh màn hình vào bước
          key / wait / ok / note         như cũ"""
        es = self.es
        notes = []
        n = 0
        for a in actions:
            a = self.expand(a).strip()
            if not a:
                continue
            if n:
                time.sleep(ACTION_DELAY)
            n += 1
            verb, _, arg = a.partition(":")
            verb, arg = verb.strip().lower(), arg.strip()
            if verb.endswith("?"):                      # lệnh tuỳ chọn: không thấy thì bỏ qua
                try:
                    notes += self.do_actions([verb[:-1] + ": " + arg], label)
                except LookupError as e:
                    notes.append("(bỏ qua: %s)" % e)
                continue
            if verb == "menu":
                es.open_menu(arg)
            elif verb in ("click", "dclick"):
                es.snap = es.handles()
                arg, area = split_col(arg)
                el = es.find_in_area(arg, area, timeout=15) if area else es.find_any(arg, timeout=15)
                es.click(el, double=(verb == "dclick"))
                time.sleep(1)
            elif verb in ("select", "choose") and arg.lstrip().startswith("#") or verb == "choose":
                lab, _, val = arg.partition("=")
                lab, val = lab.strip(), val.strip()
                es.last_outer = None
                inner, _ = es.field_for(lab)
                if inner is None:
                    raise LookupError("Ô \"%s\" không chọn được (không có ô nhập)" % lab)
                outer = getattr(es, "last_outer", None)
                if outer is None:
                    try:
                        outer = inner.parent()
                    except Exception:
                        outer = None
                slug = re.sub(r"[^A-Za-z0-9]+", "-", lab.split("|")[0]).strip("-").lower() or "o"
                got, how = es.choose_lookup(outer, inner, val, typed=(verb == "select"),
                                            on_unknown=lambda: self.dump("danh-sach-" + slug))
                if not (got or "").strip() or "vẫn mở" in how:
                    self.shot_into(notes, "chon-" + slug)
                    raise RuntimeError("Ô \"%s\" chưa chọn được \"%s\" (%s; ô đang là \"%s\")" % (lab, val, how, got or ""))
                notes.append("%s = %s (%s)" % (lab.split("|")[0], got.strip()[:40], how))
            elif verb == "close":
                self.close_screen(arg)
                notes.append("Đã tắt " + arg)
            elif verb == "cellbtn":
                col, area = split_col(arg)
                el = es.grid_cell(col, area)
                es.snap = es.handles()
                how = es.cell_button(el, area)
                time.sleep(1.5)
                if not es.new_windows(es.snap):
                    raise RuntimeError("Bấm nút … của ô \"%s\" (%s) nhưng không mở cửa sổ chọn" % (col, how))
                notes.append("Mở danh sách chọn của " + col.split("|")[0])
            elif verb == "cell":
                spec, area = split_col(arg)
                col, _, val = spec.partition("=")
                col, val = col.strip(), val.strip()
                el = es.grid_cell(col, area)
                before = es.all_handles()
                es.mark(el)
                el.click_input()
                time.sleep(0.4)
                el.click_input()                        # lần 2: mở trình soạn của ô (DevExpress)
                time.sleep(0.4)
                pkb.send_keys("{END}" + "{BACKSPACE}" * 40, pause=0.003)
                if val:
                    pkb.send_keys(esc_keys(val), with_spaces=True, pause=TYPE_PAUSE)
                time.sleep(0.8)
                pops = es.new_popups(before)
                if pops:                                # ô có danh sách (Phái, Mã lớp…): chọn dòng khớp
                    row = es.popup_row(pops, val)
                    if row is not None:
                        row.click_input()
                    else:
                        self.dump("danh-sach-o-" + re.sub(r"[^a-z0-9]+", "-", norm(col)).strip("-"))
                        pkb.send_keys("{ENTER}")
                    time.sleep(0.8)
                notes.append("%s = %s" % (col.split("|")[0], val))
            elif verb in ("type", "select", "date"):
                lab, _, val = arg.partition("=")
                val = val.strip()
                el, lb = es.field_for(lab.strip())
                if el is not None:
                    ok = es.set_field(el, val)
                    if verb == "select":
                        pkb.send_keys("{ENTER}")
                        time.sleep(0.4)
                    elif not ok:
                        raise RuntimeError("Ô \"%s\" không nhận giá trị \"%s\" (đang là \"%s\")" % (lab.strip(), val, es.field_value(el)))
                else:
                    es.type_at_label(lb, val)
                    if verb == "select":
                        pkb.send_keys("{ENTER}")
                    notes.append("%s: gõ theo vị trí" % lab.strip().split("|")[0])
            elif verb == "save":
                es.snap = es.handles()
                st0 = es.status_msg()
                es.click(es.find_any(arg or "Lưu", types=("Button", "MenuItem", "SplitButton", "Custom", "Text", "ListItem"), timeout=10))
                time.sleep(2.5)
                ds = es.new_windows(es.snap)
                for d in ds:
                    txt = es.dialog_text(d).replace("\n", " ")
                    if es.is_error_dialog(d, txt):
                        raise RuntimeError("Lỗi hệ thống khi lưu: " + txt[:200])
                    yes = es.dialog_button(d, ("có", "yes"))
                    if yes is not None and re.search(r"lưu|cập nhật", txt, re.I) and not ERR_PAT.search(txt):
                        if not self.press_yes(d, yes, lambda m: None, notes, shot=None):   # "Bạn có muốn lưu…?"
                            raise RuntimeError("Không bấm được Có của hộp \"%s\"" % txt[:120])
                        time.sleep(2)
                        continue
                    if ERR_PAT.search(txt) and not OK_PAT.search(txt):
                        f = self.shot("%s-thong-bao" % (label or "luu").lower().replace(" ", "-"))
                        raise RuntimeError("Lưu không thành công: " + txt[:250])
                    notes.append("Thông báo: " + txt[:150])
                es.close_dialogs(5)
                st = es.wait_status(st0, 5)
                if st:
                    if ERR_PAT.search(st) and not OK_PAT.search(st):
                        self.shot_into(notes, "%s-trang-thai" % (label or "luu").lower().replace(" ", "-"))
                        raise RuntimeError("Lưu không thành công (thanh trạng thái): " + st[:200])
                    notes.append("Thanh trạng thái: " + st[:150])
            elif verb == "expect":
                es.find_any(arg, types=("Text", "Custom", "DataItem", "Edit", "TitleBar", "Window", "Pane", "Button"), timeout=12)
            elif verb == "expect_dialog":
                pat = re.compile("|".join(re.escape(x) for x in alts_of(arg)) or ".", re.I)
                before = getattr(es, "snap", set())
                end, txt, ds = time.time() + 10, "", []
                while time.time() < end:
                    ds = es.new_windows(before)
                    if ds:
                        time.sleep(0.6)
                        txt = " / ".join(es.dialog_text(d).replace("\n", " ") for d in ds)
                        break
                    time.sleep(0.4)
                if not ds:
                    raise RuntimeError("Không có thông báo nào (mong đợi: %s)" % arg)
                if EX_PAT.search(txt) or any(es.is_error_dialog(d, "") for d in ds):
                    raise RuntimeError("Lỗi hệ thống: " + txt[:200])
                if not pat.search(txt):
                    raise RuntimeError("Thông báo không như mong đợi (%s): %s" % (arg, txt[:250]))
                notes.append("Thông báo: " + txt[:200])
                self.shot_into(notes, "%s-thong-bao" % (label or "buoc").lower().replace(" ", "-"))
                es.close_dialogs(6)
            elif verb == "find_row":
                arg, col = split_col(arg)
                el = self.locate_row(arg, col)
                es.click(el)
                notes.append("Thấy dòng " + arg)
            elif verb == "delete_row":
                arg, col = split_col(arg)
                el = self.locate_row(arg, col)
                es.click(el)
                notes += self.delete_flow(arg)
                self.clear_filter()
            elif verb == "cancel":
                es.snap = es.handles()
                try:
                    es.click(es.find_any(arg or "Hủy|Huỷ|Không lưu|Bỏ qua", types=("Button", "MenuItem", "SplitButton"), timeout=2))
                except Exception:
                    if es.dialogs():                    # Esc chỉ khi đang có cửa sổ con; ở cửa sổ chính Esc đóng màn hình
                        pkb.send_keys("{ESC}")
                time.sleep(1.2)
                for d in es.new_windows(es.snap):
                    no = es.dialog_button(d, ("không", "no", "hủy", "cancel", "đóng"))
                    if no is not None:
                        es.press(no)
                time.sleep(0.8)
            elif verb == "dump":
                self.dump(arg or label or "man-hinh")
            elif verb == "key":
                pkb.send_keys(arg)
                time.sleep(ACTION_DELAY)
            elif verb == "wait":
                time.sleep(float(arg or 1))
            elif verb == "ok":
                for d in es.dialogs():
                    el = es.dialog_button(d, ("ok", "đóng", "close", "đồng ý"))
                    if el is not None:
                        es.press(el)
            elif verb == "unique":
                arg, col = split_col(arg)
                notes.append(self.make_unique(arg.strip().strip("{}"), col))
            elif verb == "pick":
                notes.append(self.pick_row(arg))
            elif verb == "absent":
                arg, col = split_col(arg)
                if self.row_exists(arg, col):
                    # Lưới chưa nạp lại sau Xóa (thanh trạng thái đã báo thành công mà dòng vẫn hiện) → tắt màn hình,
                    # mở lại menu rồi kiểm tra lần nữa (người dùng dạy 03/11).
                    path = getattr(es, "last_menu", "") or self.sc.get("menu") or ""
                    segs = menu_segs(path)
                    if not segs:
                        raise RuntimeError("Vẫn còn \"%s\" trong danh sách" % arg)
                    self.close_screen(segs[-1])
                    es.open_menu(path)
                    notes.append("Tắt và mở lại " + segs[-1])
                    if self.row_exists(arg, col):
                        raise RuntimeError("Vẫn còn \"%s\" trong danh sách (đã tắt, mở lại màn hình)" % arg)
                notes.append("Không còn " + arg)
            elif verb == "shot":
                self.shot_into(notes, arg or (label or "anh").lower().replace(" ", "-"))
            elif verb == "note":
                notes.append(arg)
            else:
                raise ValueError("Lệnh không hiểu: " + a)
        return notes

    SAFE_NAMES = ["Mot", "Hai", "Ba", "Bon", "Nam", "Sau", "Bay", "Tam", "Chin", "Muoi"]   # không dính tổ hợp Telex

    def row_exists(self, value, col=""):
        """Có dòng mang giá trị này trong lưới đang mở không – gõ vào ô tìm kiếm của cột rồi xoá ô tìm cho lưới hiện
        lại đủ dòng. Bắt buộc ghi cột: chỉ nhìn các dòng đang hiện thì không kết luận được là "chưa có".
        KHÔNG dùng phím Esc – Esc đóng màn hình chức năng, ở cửa sổ chính thì hỏi "Thoát khỏi chương trình?"."""
        if not col:
            raise RuntimeError("Lệnh kiểm tra \"%s\" thiếu cột – ghi thêm \"@ Tên cột\" để tìm bằng ô tìm kiếm của cột" % value)
        try:
            self.locate_row(value, col)
            found = True
        except LookupError:                             # không thấy CỘT thì là RuntimeError – không kết luận được
            found = False
        self.clear_filter()
        return found

    def make_unique(self, var, col=""):
        """Giá trị test {var} chưa có trong lưới đang mở; có rồi thì tự chọn giá trị khác (tối đa 8 lần)."""
        import random
        if var not in self.vars:
            raise RuntimeError("Kịch bản chưa khai báo biến %s" % var)
        first = cur = str(self.vars[var])
        tried = [cur]
        for _ in range(8):
            if not self.row_exists(cur, col):
                if cur != first:
                    self.say("%s = %s đã có sẵn → dùng %s" % (var, first, cur))
                    return "%s đã có, đổi thành %s" % (first, cur)
                return "%s = %s chưa có" % (var, cur)
            m = re.match(r"^(.*?)(\d+)$", cur)
            if m:                                   # mã: đổi các số cuối, giữ độ dài
                n = len(m.group(2))
                cur = m.group(1) + str(random.randint(10 ** (n - 1) if n > 1 else 0, 10 ** n - 1))
            else:                                   # tên: lấy tên test khác chưa thử
                left = [x for x in self.SAFE_NAMES if x not in tried]
                cur = random.choice(left) if left else first + random.choice("BCDGHK")
            tried.append(cur)
            self.vars[var] = cur
        raise RuntimeError("Không tìm được giá trị %s chưa có sẵn (đã thử %s)" % (var, ", ".join(tried)))

    def close_screen(self, name):
        """Tắt màn hình bằng nút X trên tab; hỏi lưu thay đổi → Không (bước đã lưu/không cần lưu)."""
        es = self.es
        es.snap = es.handles()
        es.close_screen(name)
        time.sleep(1.2)
        for d in es.new_windows(es.snap):
            no = es.dialog_button(d, ("không", "no"))
            if no is not None:
                es.press(no)

    def win_rows(self, root):
        """Các dòng dữ liệu của lưới trong một cửa sổ: {số dòng: [(tên cột, giá trị, phần tử)]} – lấy cả ô check
        ("#" = Checked/Unchecked); bỏ dòng lọc và dòng nhóm (số âm)."""
        rows = {}
        try:
            cells = root.descendants(control_type="DataItem")
        except Exception:
            cells = []
        for c in cells:
            try:
                m = re.match(r"^(.*?)\s+row\s*(-?\d+)$", norm(c.element_info.name or c.window_text() or ""))
                if not m or int(m.group(2)) < 0 or re.search(r"filter|lọc", m.group(1), re.I):
                    continue
                v = ""
                try:
                    v = c.iface_value.CurrentValue or ""
                except Exception:
                    pass
                rows.setdefault(int(m.group(2)), []).append((m.group(1).strip(), nfc(str(v or "")).strip(), c))
            except Exception:
                continue
        return rows

    def delete_flow(self, code):
        """Bấm Xóa rồi đi hết các bước xác nhận của Edusoft (lượt QLSV-001 03/11 01:22):
          1. form "Danh sách đang chọn để xóa, vui lòng kiểm tra và chọn xác thực lại" (lưới có ô check, nút Thực hiện):
             MỌI dòng trong lưới phải mang mã `code` (không thì Đóng, không xóa) → tick ô check các dòng đó → Thực hiện;
          2. hộp "Xác nhận xóa dữ liệu đang chọn?" Có/Không → Có khi hộp nêu đúng mã HOẶC đã kiểm ở bước 1;
          3. CHỜ Edusoft xử lý như người test: không bấm Đóng form khi đang xóa; xong khi thanh trạng thái báo
             "Xóa … thành công" (tối đa 40 giây). Thông báo kết quả → OK.
        Mọi việc ghi vào nhật ký có mốc thời gian (`trace`) – báo lỗi kèm nhật ký để biết Edusoft dừng ở đâu."""
        es = self.es
        es.snap = es.handles()
        st0 = es.status_msg()
        t0 = time.time()
        trace = []

        def log(msg):
            trace.append("+%.1fs %s" % (time.time() - t0, msg))

        es.click(es.find_any("Xóa|Xoá", types=("Button", "MenuItem", "SplitButton", "Custom", "Text", "ListItem"), timeout=10))
        log("bấm Xóa (thanh trạng thái trước: %s)" % (st0 or "trống"))
        time.sleep(1.5)
        notes, seen, forms = [], set(), []
        verified = confirmed = False
        t_conf = None
        key = norm(code)

        def alive(w):
            try:
                return bool(w.is_visible())
            except Exception:
                return False

        def close_forms():
            for f in forms:
                if not alive(f):
                    continue
                try:
                    b = es.dialog_button(f, ("đóng", "close", "hủy", "huỷ", "cancel"))
                    if b is not None:
                        log("bấm Đóng form xác nhận")
                        es.press(b)
                except Exception:
                    pass

        def refuse(msg):
            close_forms()
            raise RuntimeError(msg + "\nNhật ký xóa: " + " | ".join(trace))

        idle, st = 0, ""
        end = time.time() + 70
        while time.time() < end:
            ds = [d for d in es.new_windows(es.snap) if d.handle not in seen]
            if not ds:
                idle += 1
                if confirmed:
                    st = es.status_msg()
                    if st and st != st0:
                        log("thanh trạng thái: " + st)
                        break
                    if time.time() - t_conf > 40:
                        log("hết 40 giây chờ, thanh trạng thái vẫn: %s; form còn mở: %s" % (st or "trống", any(alive(f) for f in forms)))
                        break
                    if forms and not any(alive(f) for f in forms) and not getattr(self, "_form_gone", False):
                        self._form_gone = True
                        log("form xác nhận tự đóng")
                elif idle >= 8:
                    break
                time.sleep(0.5)
                continue
            idle = 0
            d = ds[-1]
            seen.add(d.handle)
            try:
                has_btn = any(b.is_visible() for b in d.descendants(control_type="Button"))
            except Exception:
                has_btn = False
            if not has_btn:                               # progressPanel "đang xử lý" – chờ nó tự tắt, không bấm gì
                log("cửa sổ đang xử lý (không có nút): " + (es.dialog_text(d).split("\n")[0][:60] or "?"))
                time.sleep(0.5)
                continue
            if es.is_form(d):
                forms.append(d)
                rows = self.win_rows(d)
                data = {k: r for k, r in rows.items() if any(v and n != "#" and v not in ("Checked", "Unchecked") for n, v, _ in r)}
                hit = {k: r for k, r in data.items() if any(key and key in norm(v) for _, v, _ in r)}
                log("form xác nhận: %d dòng, %d dòng mang mã" % (len(data), len(hit)))
                if not hit or len(hit) != len(data):
                    others = [" · ".join(v for _, v, _ in r if v and v not in ("Checked", "Unchecked")) for k, r in data.items() if k not in hit]
                    refuse("Danh sách xác nhận xóa không chỉ có %s (%s) nên KHÔNG xóa – hãy xóa tay" % (code, "; ".join(others)[:200] or "không đọc được dòng"))
                ticks = []
                for k, r in hit.items():
                    box = next((c for n, v, c in r if v in ("Unchecked", "Checked") or n == "#"), None)
                    if box is None:
                        continue
                    other = next((c for n, v, c in r if c is not box), None)
                    ticks.append(self.tick_box(box, other))
                log("tick ô chọn: " + (", ".join(t or "không đọc được" for t in ticks) or "không thấy ô chọn"))
                if any(t == "Unchecked" for t in ticks):
                    self.shot_into(notes, "xoa-chua-tick")
                    refuse("Không tick được ô chọn của dòng %s trong danh sách xác nhận xóa (ô vẫn Unchecked) – chưa xóa" % code)
                self.shot_into(notes, "xoa-da-tick")
                btn = es.dialog_button(d, ("thực hiện", "xóa", "xoá", "đồng ý", "ok", "chọn"))
                if btn is None:
                    refuse("Form xác nhận xóa không có nút Thực hiện")
                verified = True
                es.click(btn)                             # bấm chuột như người test (nút thanh công cụ DevExpress)
                log("bấm " + (btn.window_text() or "Thực hiện"))
                time.sleep(1.5)
                continue
            txt = es.dialog_text(d)
            head = (txt.split("\n") or [""])[0]
            if es.is_error_dialog(d, txt):
                log("LỖI: " + head[:120])
                self.shot_into(notes, "xoa-loi")
                ok = es.dialog_button(d, ("đóng", "ok", "close"))
                if ok is not None:
                    es.press(ok)
                refuse("Xóa bị lỗi: " + txt[:300])
            no = es.dialog_button(d, ("không", "no", "hủy", "huỷ", "cancel"))
            yes = es.dialog_button(d, ("có", "yes", "đồng ý", "ok", "xóa", "xoá"))
            if no is not None:                            # câu hỏi xác nhận
                if yes is not None and (key in norm(txt) or (verified and re.search(r"xóa|xoá|delete", norm(txt), re.I))):
                    log("hỏi \"%s\"" % head[:80])
                    if not self.press_yes(d, yes, log, notes):
                        refuse("Không bấm được nút Có của hộp \"%s\" (hộp vẫn mở) – chưa xóa" % head[:80])
                    if not confirmed:
                        confirmed, t_conf = True, time.time()
                    continue
                log("hỏi lạ \"%s\" → Không" % head[:80])
                es.press(no)
                refuse("Hộp thoại xác nhận xóa không nêu mã %s nên KHÔNG xóa – hãy xóa tay. Nội dung: %s" % (code, head[:200]))
            log("thông báo: " + (head[:120] or "?"))
            if txt:
                notes.append(head[:120])
            if OK_PAT.search(txt) and re.search(r"xóa|xoá", txt, re.I):
                st = st or head
            ok = es.dialog_button(d, ("ok", "đóng", "close", "đồng ý")) or yes
            if ok is not None:
                es.press(ok)
            else:
                pkb.send_keys("{ENTER}")
            time.sleep(0.8)
        self._form_gone = False
        if not confirmed:
            refuse("Bấm Xóa nhưng không thấy hộp thoại xác nhận xóa %s" % code)
        if st and ERR_PAT.search(st) and not OK_PAT.search(st):
            refuse("Xóa không thành công (thanh trạng thái): " + st[:200])
        if not (st and re.search(r"xóa|xoá", st, re.I) and OK_PAT.search(st)):
            # Lượt 01:35 / 01:50 / 02:09: Edusoft không xóa (thanh trạng thái không đổi, dòng còn) – có ảnh + nhật ký để xác định
            self.shot_into(notes, "xoa-khong-bao")
            refuse("Đã bấm Xóa → Thực hiện → Có nhưng Edusoft KHÔNG báo \"Xóa dữ liệu thành công\" (thanh trạng thái: %s) – "
                   "dữ liệu %s có thể chưa bị xóa" % (st or es.status_msg() or "không đổi", code))
        close_forms()                                     # đã xóa xong mà form còn mở → đóng
        es.close_dialogs(6)
        notes.append("Thanh trạng thái: " + st[:150])
        notes.append("Đã xóa " + code + " (" + "; ".join(trace[-3:]) + ")")
        return notes

    def press_yes(self, d, yes, log, notes, shot="xoa-hoi-xac-nhan"):
        """Bấm CHẮC CHẮN nút Có của hộp hỏi Có/Không. Hộp "Xác nhận xóa dữ liệu đang chọn?" để con trỏ sẵn ở **Không**:
        nếu chỉ gửi phím Space/Enter mà con trỏ chưa sang Có thì bấm nhầm Không (lượt 03/11: ảnh thấy Có sáng do chuột,
        Không có viền con trỏ – Edusoft không xóa). Cách làm: đưa hộp lên trước → bấm CHUỘT vào Có → chờ hộp đóng;
        chưa đóng thì chỉ gửi Space khi ĐÃ KIỂM con trỏ nằm ở Có, không kiểm được thì Invoke nút Có. Ghi nhật ký."""
        es = self.es

        def alive():
            try:
                return bool(d.is_visible())
            except Exception:
                return False

        def focused():
            try:
                for b in d.descendants(control_type="Button"):
                    try:
                        if b.has_keyboard_focus():
                            return b.window_text() or "?"
                    except Exception:
                        continue
            except Exception:
                pass
            return "không rõ"

        def gone(sec):
            for _ in range(int(sec / 0.3)):
                time.sleep(0.3)
                if not alive():
                    return True
            return False

        try:
            d.set_focus()                                 # hộp hỏi lên trước, nhận chuột/phím
        except Exception:
            pass
        log("nút đang chọn sẵn: " + focused())
        if shot:
            self.shot_into(notes, shot)
        es.mark(yes)
        yes.click_input()
        if gone(3):
            log("bấm chuột vào Có → hộp hỏi đóng")
            return True
        log("bấm chuột vào Có nhưng hộp hỏi chưa đóng (nút đang chọn: %s)" % focused())
        try:
            yes.set_focus()
        except Exception:
            pass
        time.sleep(0.2)
        try:
            on_yes = bool(yes.has_keyboard_focus())
        except Exception:
            on_yes = False
        if on_yes:
            pkb.send_keys("{SPACE}")
            log("con trỏ đã ở Có → Space")
        else:
            try:
                yes.iface_invoke.Invoke()
                log("con trỏ không ở Có → Invoke nút Có")
            except Exception as e:
                log("Invoke nút Có lỗi: %s" % e)
        if gone(4):
            log("hộp hỏi đóng")
            return True
        return False

    def tick_box(self, box, other=None):
        """Tick ô chọn (cột "#") của một dòng lưới DevExpress, CHẮC CHẮN ô thành Checked:
        bấm 1 lần → bấm sang ô khác cùng dòng (đẩy giá trị từ ô đang sửa vào lưới) → đọc lại; còn Unchecked thì bấm lần 2.
        Không bấm 2 lần liền nhau (lượt 01:35/01:50 bấm 2 lần → tick rồi bỏ tick, Thực hiện xóa không được dòng nào).
        Trả giá trị cuối ("Checked"/"Unchecked"/"" nếu không đọc được)."""
        es = self.es

        def read():
            v = es.field_value(box) or ""
            return v if v in ("Checked", "Unchecked") else ""

        if read() == "Checked":
            return "Checked"
        v = ""
        for _ in range(2):
            es.click(box)
            for _ in range(4):
                time.sleep(0.4)
                v = read()
                if v == "Checked":
                    return v
            if other is not None:
                try:
                    es.click(other)                       # rời ô check → giá trị được ghi vào lưới
                except Exception:
                    pass
                time.sleep(0.6)
                v = read()
                if v == "Checked":
                    return v
            if v != "Unchecked":
                return v                                  # không đọc được giá trị – không bấm thêm (tránh bỏ tick)
        return v

    def grid_rows(self):
        """Các dòng đang hiện trong lưới của màn hình: mỗi dòng là danh sách (tên cột, giá trị). Ô lưới DevExpress là
        DataItem tên "<cột> row N", giá trị ở Value; gom các ô cùng hàng theo toạ độ."""
        out = []
        for root in self.es.roots():
            nodes = uia_scan(root)
            if nodes is not None:
                grids = [nd.rect for nd in nodes if nd.ct in ("Table", "DataGrid") and nd.visible]
                byrow = {}
                for nd in nodes:
                    if nd.ct != "DataItem" or not nd.visible or not any(nd.inside(g) for g in grids):
                        continue
                    v = (nd.val or "").strip()
                    name = re.sub(r"\s+row\s*\d+$", "", nd.name, flags=re.I).strip()
                    if not v or re.search(r"filter|lọc", name, re.I):
                        continue
                    byrow.setdefault(nd.rect[1] // 6, []).append((nd.rect[0], name, v))
                for k in sorted(byrow):
                    out.append([(n, v) for _, n, v in sorted(byrow[k])])
                if out:
                    return out
                continue
            cells = []
            for g in ("Table", "DataGrid"):
                try:
                    for grid in root.descendants(control_type=g):
                        cells += grid.descendants(control_type="DataItem")
                except Exception:
                    continue
            byrow = {}
            for c in cells:
                try:
                    if not c.is_visible():
                        continue
                    v = ""
                    try:
                        v = c.iface_value.CurrentValue or ""
                    except Exception:
                        pass
                    v = str(v or c.window_text() or "").strip()
                    name = re.sub(r"\s+row\s*\d+$", "", str(c.element_info.name or ""), flags=re.I).strip()
                    if not v or re.search(r"filter|lọc", name, re.I):
                        continue
                    r = c.rectangle()
                    byrow.setdefault((r.top // 6), []).append((r.left, name, v))
                except Exception:
                    continue
            for k in sorted(byrow):
                out.append([(n, v) for _, n, v in sorted(byrow[k])])
            if out:
                return out                              # hộp thoại/form con có lưới thì lấy lưới đó trước
        return out

    def pick_row(self, arg):
        """pick: BIẾN = lọc|lọc @ cột – chọn ngẫu nhiên một dòng phù hợp trong lưới đang mở và ghi nhớ."""
        import random
        import unicodedata

        def fold(x):
            x = unicodedata.normalize("NFD", str(x or "").lower().replace("đ", "d"))
            return re.sub(r"\s+", " ", "".join(c for c in x if unicodedata.category(c) != "Mn")).strip()

        var, _, rest = arg.partition("=")
        var = var.strip().strip("{}")
        flt, _, col = rest.partition("@")
        alts = [fold(x) for x in flt.split("|") if x.strip()]
        rows = self.grid_rows()
        hits = [r for r in rows if not alts or any(a in fold(" ".join(v for _, v in r)) for a in alts)]
        if not hits:
            raise RuntimeError("Không có dòng nào khớp \"%s\" trong danh sách (%d dòng đang hiện)" % (flt.strip(), len(rows)))
        row = random.choice(hits)
        val = row[0][1]
        if col.strip():
            cols = [fold(x) for x in col.split("|") if x.strip()]
            found = [v for c in cols for name, v in row if fold(name) == c]
            found += [v for c in cols for name, v in row if c in fold(name)]
            if found:
                val = found[0]
        self.vars[var] = val
        self.vars[var + "_DONG"] = " · ".join(v for _, v in row)
        self.say("Chọn ngẫu nhiên %s = %s (trong %d dòng phù hợp)" % (var, val, len(hits)))
        return "%s = %s (%s)" % (var, val, self.vars[var + "_DONG"][:120])

    def column_header(self, col):
        """Tiêu đề cột `col` (nhiều tên cách nhau |) của lưới trên màn hình đang mở; nhiều lưới thì lấy lưới trên cùng."""
        wants = [norm_label(x) for x in alts_of(col)]
        for root in self.es.roots():
            nodes = uia_scan(root)
            if nodes is not None:
                grids = [nd.rect for nd in nodes if nd.ct in ("Table", "DataGrid") and nd.visible]
                trees = [nd.rect for nd in nodes if nd.ct == "Tree" and nd.aid.lower().startswith("treechucnang")]
                best = None
                for t in ("HeaderItem", "Header", "Custom", "Text"):
                    for nd in nodes:
                        if nd.ct != t or not nd.visible or norm_label(nd.name) not in wants:
                            continue
                        if any(nd.inside(g) for g in trees):
                            continue                    # cây "Danh mục chức năng" bên trái
                        if t not in ("HeaderItem", "Header") and not any(nd.inside(g) for g in grids):
                            continue
                        if best is None or nd.rect[1] < best.rect[1]:
                            best = nd
                    if best is not None:
                        self._hdr_grid = next((g for g in grids if best.inside(g)), None)
                        return best.wrap()
                continue
            grids, trees = [], []
            for g in ("Table", "DataGrid"):
                try:
                    grids += [x.rectangle() for x in root.descendants(control_type=g) if x.is_visible()]
                except Exception:
                    continue
            try:
                trees = [x.rectangle() for x in root.descendants(control_type="Tree")
                         if str(x.element_info.automation_id or "").lower().startswith("treechucnang")]
            except Exception:
                pass
            best = None
            for t in ("HeaderItem", "Header", "Custom", "Text"):
                try:
                    els = root.descendants(control_type=t)
                except Exception:
                    continue
                for el in els:
                    try:
                        if norm_label(el.window_text()) not in wants or not el.is_visible():
                            continue
                        r = el.rectangle()
                        cx, cy = (r.left + r.right) / 2, (r.top + r.bottom) / 2
                        inside = lambda rs: any(g.left <= cx <= g.right and g.top <= cy <= g.bottom for g in rs)
                        if inside(trees):
                            continue                    # cây "Danh mục chức năng" bên trái
                        if t not in ("HeaderItem", "Header") and not inside(grids):
                            continue                    # chữ trùng tên cột nhưng không nằm trong lưới
                        if best is None or r.top < best.rectangle().top:
                            best = el
                    except Exception:
                        continue
                if best is not None:
                    return best
        return None

    def filter_grid(self, hdr, value):
        """Ô tìm kiếm của lưới Edusoft = dòng lọc (icon phễu) ngay dưới tiêu đề cột: bấm vào ô của cột, gõ giá trị, Enter."""
        from pywinauto import mouse
        if self._filter is not None:
            try:
                same = self._filter[0] == hdr
            except Exception:
                same = False
            if not same:
                self.clear_filter()                     # bỏ lọc cột khác trước, tránh lọc chồng
        r = hdr.rectangle()
        x = int((r.left + r.right) / 2)
        y = int(r.bottom + max(9, r.height() / 2))
        self.es.mark(hdr)
        mouse.click(coords=(x, y))                      # bấm dưới tiêu đề – không bấm vào tiêu đề (sẽ sắp xếp cột)
        time.sleep(0.5)
        pkb.send_keys("{END}" + "{BACKSPACE}" * 40, pause=0.003)
        if value:
            pkb.send_keys(esc_keys(value), with_spaces=True, pause=TYPE_PAUSE)
        time.sleep(0.4)
        pkb.send_keys("{ENTER}")
        time.sleep(0.9)                                 # locate_row tự chờ tiếp tới khi lưới lọc xong
        self._filter = (hdr, x, y, r.top)
        return y

    def clear_filter(self):
        """Xoá chữ trong ô tìm kiếm đã gõ (chỉ khi cột đó vẫn đang hiện đúng chỗ cũ)."""
        f, self._filter = self._filter, None
        if f is None:
            return
        hdr, x, y, top = f
        try:
            if not hdr.is_visible() or hdr.rectangle().top != top:
                return
            from pywinauto import mouse
            mouse.click(coords=(x, y))
            time.sleep(0.4)
            pkb.send_keys("{END}" + "{BACKSPACE}" * 40 + "{ENTER}", pause=0.003)
            time.sleep(0.7)
        except Exception:
            pass

    def grid_empty(self, y):
        """Lưới vừa lọc (dòng lọc ở toạ độ y) không còn dòng dữ liệu nào (DataItem "<cột> row N" dưới dòng lọc)."""
        g = getattr(self, "_hdr_grid", None)
        for root in self.es.roots():
            nodes = uia_scan(root)
            if nodes is None:
                return False
            for nd in nodes:
                if nd.ct == "DataItem" and nd.visible and nd.rect[1] > y + 3 and re.search(r"\srow\s*\d+$", nd.name) \
                        and (g is None or nd.inside(g)):
                    return False
        return True

    def locate_row(self, value, col=""):
        """Dòng trong lưới có ô đúng bằng `value`. Có cột: gõ giá trị vào ô tìm kiếm (dòng lọc) của cột rồi tìm
        trong các dòng còn lại. Không ghi cột: chỉ tìm trong các dòng đang hiện."""
        es = self.es
        if col:
            hdr = self.column_header(col)
            if hdr is None:
                raise RuntimeError("Không thấy cột \"%s\" (ô tìm kiếm) trong danh sách đang mở" % col)
            y = self.filter_grid(hdr, value)
            t0 = time.time()
            end = t0 + 6
            while True:
                el = es.element_with_text(value, below=y + 3)
                if el is not None:
                    return el
                if time.time() - t0 > 1.2 and self.grid_empty(y):
                    # lưới đã lọc xong mà không còn dòng nào → chắc chắn "chưa có", khỏi chờ đủ 6 giây
                    raise LookupError("Không thấy dòng \"%s\" (cột %s) trong danh sách" % (value, col))
                if time.time() > end:
                    raise LookupError("Không thấy dòng \"%s\" (cột %s) trong danh sách" % (value, col))
                time.sleep(0.4)
        el = es.element_with_text(value)              # không ghi cột: chỉ tìm trong các dòng đang hiện
        if el is None:
            raise LookupError("Không thấy dòng \"%s\" trong các dòng đang hiện (ghi \"@ Tên cột\" để tìm bằng ô tìm kiếm)" % value)
        return el

    def summary(self):
        keys = [k for k in (self.sc.get("vars") or {})]
        return ("Dữ liệu test: " + ", ".join("%s = %s" % (k, self.vars[k]) for k in keys) + ".") if keys else ""

    def shot_into(self, notes, name):
        f = self.shot(name)
        if f:
            self._pending_shots.append(f)

    def ask_manual(self, label, text):
        print("» %s (thao tác tay) — F8 = Đạt · F9 = Lỗi · F10 = Bỏ qua" % label)
        res = CAP.ask("__step__", label, text)
        if res:
            time.sleep(ACTION_DELAY)
            return res
        if hotkeys is None:
            k = input("   %s – nhập 8 (Đạt) / 9 (Lỗi) / 0 (Bỏ qua): " % label).strip()
            return {"8": "ok", "9": "bad"}.get(k, "skip")
        while True:
            ev = hotkeys.read_event(suppress=False)
            if ev.event_type != "down":
                continue
            if ev.name == "f8":
                return "ok"
            if ev.name == "f9":
                return "bad"
            if ev.name == "f10":
                return "skip"

    def ask_error(self, rec, label, kind, idx, text):
        if CAP.root is not None:                     # form trên popup, tự đưa con trỏ vào – không gõ nhầm sang Edusoft
            self.add_bug(rec, kind, idx, text, CAP.ask("__bug__", label, self.expand(text)) or {})
            time.sleep(ACTION_DELAY)
            return
        try:                                          # không có tkinter: hỏi trong cửa sổ đen – đưa nó lên trước
            import ctypes
            h = ctypes.windll.kernel32.GetConsoleWindow()
            ctypes.windll.user32.ShowWindow(h, 9)
            ctypes.windll.user32.SetForegroundWindow(h)
        except Exception:
            pass
        print("\n   %s bị lỗi – nhập thông tin cho support:" % label)
        t = input("   Loại lỗi [1] chức năng/dữ liệu, [2] EX hệ thống: ").strip()
        if t == "2":
            detail = input("   Chi tiết lỗi (Ctrl+Shift+E, dán một dòng): ").strip()
            code = input("   Menu code (Ctrl+Shift+F): ").strip()
            self.bugs.append(dict(kind=kind, stepIndex=idx, stepText=text, type="ex", exDetail=detail, menuCode=code, shots=list(rec["shots"])))
            rec["note"] = "Lỗi EX" + (" · menu code " + code if code else "")
        else:
            action = input("   Thao tác (Lưu/Thêm/Sửa/Xóa/Import/…): ").strip() or "Khác"
            exp = input("   Dữ liệu mong đợi: ").strip()
            act = input("   Dữ liệu thực tế sau thao tác: ").strip()
            self.bugs.append(dict(kind=kind, stepIndex=idx, stepText=text, type="func", action=action, expectedData=exp, actualData=act, shots=list(rec["shots"])))
            rec["note"] = "Lỗi chức năng · " + action

    def add_bug(self, rec, kind, idx, text, f):
        """Ghi lỗi người test nhập trên popup (f trống = chưa ghi chi tiết) – về console thành lỗi trong menu Lỗi."""
        if f.get("type") == "ex":
            self.bugs.append(dict(kind=kind, stepIndex=idx, stepText=text, type="ex", exDetail=f.get("detail", ""), menuCode=f.get("code", ""), shots=list(rec["shots"])))
            rec["note"] = "Lỗi EX" + (" · menu code " + f["code"] if f.get("code") else "")
        else:
            action = f.get("action") or "Khác"
            self.bugs.append(dict(kind=kind, stepIndex=idx, stepText=text, type="func", action=action, expectedData=f.get("exp") or text,
                                  actualData=f.get("act") or "(người test chưa ghi chi tiết)", shots=list(rec["shots"])))
            rec["note"] = "Lỗi chức năng · " + action

    def run_block(self, kind, idx, label, text, actions, rec):
        t_start = time.time()
        CAP.at(kind, idx, self.expand(text))      # popup đổi "Thao tác" khi bước trước đã xong
        time.sleep(STEP_DELAY)
        self.es.keep_open()
        try:
            if text.lower().startswith("điều kiện đầu vào") and not actions:
                rec["res"] = "ok"
                rec["note"] = "Đã đăng nhập theo CHUNG-001"
            elif actions:
                self._pending_shots = []
                notes = self.do_actions(actions, label)
                rec["shots"] += self._pending_shots
                if not self.check_ex(rec, label, kind, idx, text):
                    rec["res"] = "ok"
                    rec["note"] = " · ".join(notes)[:300]
            else:
                res = self.ask_manual("%s · %s" % (self.sc["code"], label), self.expand(text))   # hiện giá trị thật thay cho {MSSV}…
                rec["res"] = res
                s = self.shot("%s" % label.lower())
                if s:
                    rec["shots"].append(s)
                if res == "bad":
                    self.ask_error(rec, label, kind, idx, text)
        except Exception as e:
            rec["shots"] += getattr(self, "_pending_shots", [])
            self.es.keep_open()
            s = self.shot("%s-loi" % label.lower().replace(" ", "-"))
            if s:
                rec["shots"].append(s)
            self.dump("%s-loi" % label)
            if not self.check_ex(rec, label, kind, idx, text):
                err = "Script không thực hiện được: %s" % e
                rec["res"] = "bad"
                rec["note"] = "Script dừng: %s" % e
                ans = CAP.ask("__err__", label, (self.expand(text), err))     # tạm dừng, hỏi người test
                if ans is None:                                                # không có popup: ghi lỗi như cũ
                    self.bugs.append(dict(kind=kind, stepIndex=idx, stepText=text, type="func", action="Khác",
                                          expectedData=text, actualData=err, shots=list(rec["shots"])))
                elif ans.get("stop"):
                    rec["res"], rec["note"] = "skip", "Người test dừng test tại đây (%s)" % str(e)[:150]
                    self.abort = True
                elif ans.get("type"):
                    self.add_bug(rec, kind, idx, text, ans)
                    self.halt = True
                else:
                    rec["res"], rec["note"] = "skip", "Script không làm được (%s) – người test xác nhận không phải lỗi" % str(e)[:150]
                    self.halt = True
        if rec["res"] == "ok" and not rec["shots"]:
            s = self.shot(label.lower().replace(" ", "-"))
            if s:
                rec["shots"].append(s)
        rec["at"] = now_iso()
        rec["sec"] = round(time.time() - t_start, 1)      # thời gian thực hiện bước (giây)
        self.say("%s: %s%s — %s" % (label, {"ok": "ĐẠT", "bad": "LỖI", "skip": "BỎ QUA"}.get(rec["res"], "?"), (" · " + rec["note"]) if rec["note"] else "", text[:120]))
        return rec["res"]

    def record_main(self, main_ok):
        """Ghi nhận kết quả luồng chính (file + ảnh màn hình) trước khi test luồng con trên cùng phiên Edusoft."""
        res = [x["res"] for x in self.steps]
        st = "Đạt" if main_ok else ("Lỗi" if "bad" in res else "Chưa xong")
        try:
            (self.dir / "ket-qua-luong-chinh.json").write_text(json.dumps(dict(
                scenarioCode=self.sc["code"], status=st, at=now_iso(), steps=self.steps), ensure_ascii=False, indent=1), "utf-8")
        except Exception as e:
            self.say("(Không ghi được kết quả luồng chính: %s)" % e)
        n_alt = len(self.sc.get("altFlows") or [])
        self.say("Đã ghi nhận luồng chính: %s%s" % (st, (" – tiếp theo %d luồng con, không mở lại Edusoft" % n_alt) if n_alt else ""))
        if n_alt:
            CAP.show("%s · Đã ghi nhận luồng chính: %s" % (self.sc["code"], st), "Tiếp theo: %d luồng con trên cùng phiên Edusoft" % n_alt)
            time.sleep(STEP_DELAY)

    def execute(self):
        sc = self.sc
        self.say("Bắt đầu %s – %s (script, chế độ trình diễn)" % (sc["code"], sc.get("title", "")))
        CAP.begin(sc, self.steps, self.alts, [self.expand(t) for t in sc.get("steps", [])])
        obs_start(self)
        try:
            # kịch bản tự mở menu ở từng bước thì KHÔNG mở menu chính trước bước 1 (để chạy đúng thứ tự bước)
            has_menu = any("menu:" in (";".join(x) if isinstance(x, list) else str(x or "")).lower() for x in (sc.get("auto") or []))
            if sc.get("menu") and not has_menu:
                try:
                    CAP.show("%s · Mở menu" % sc["code"], sc["menu"])
                    self.es.open_menu(sc["menu"])
                except Exception as e:
                    self.say("Không tự mở được menu \"%s\": %s" % (sc["menu"], e))
                    self.dump("menu-loi")         # ghi cây giao diện để sửa tên menu
            autos = sc.get("auto") or []
            stop = False
            for i, text in enumerate(sc.get("steps", [])):
                acts = autos[i] if i < len(autos) and autos[i] else []
                if isinstance(acts, str):
                    acts = [x for x in acts.split(";")]
                if stop or self.abort:
                    self.steps[i].update(res="skip", note=self.steps[i]["note"] or ("Người test đã dừng test" if self.abort else "Bỏ qua – bước trước lỗi"))
                    continue
                r = self.run_block("step", i, "Bước %d" % (i + 1), text, acts, self.steps[i])
                if (r == "bad" and CFG.get("stopOnError", True)) or self.halt:
                    stop, self.halt = True, False
            main_ok = all(x["res"] == "ok" for x in self.steps)
            self.record_main(main_ok)              # ghi nhận luồng chính xong rồi mới test luồng con
            alt_defs = sc.get("altFlows", []) or []
            n_steps = len(sc.get("steps", []))
            for j in sorted(range(len(alt_defs)), key=lambda k: (alt_at(alt_defs[k], n_steps), k)):
                alt = alt_defs[j]
                acts = alt.get("auto") or []
                if isinstance(acts, str):
                    acts = acts.split(";")
                text = "%s — %s (luồng con, rẽ từ bước %d)" % (alt.get("name", ""), alt.get("condition", ""), alt_at(alt, n_steps) + 1)
                if self.abort:
                    self.alts[j].update(res="skip", note="Người test đã dừng test", at=now_iso())
                    continue
                if alt.get("needs") == "main" and not main_ok:
                    self.alts[j].update(res="skip", note="Bỏ qua – luồng chính chưa đạt", at=now_iso())
                    self.say("Luồng A%d: BỎ QUA — luồng chính chưa đạt" % (j + 1))
                    continue
                if alt.get("always") or acts or CFG.get("manualAlts"):
                    self.run_block("alt", j, "Luồng A%d" % (j + 1), text, acts, self.alts[j])
                    self.halt = False
                    if alt.get("after"):
                        try:
                            self.do_actions(alt["after"], "Luồng A%d" % (j + 1))
                        except Exception as e:
                            self.say("Luồng A%d: dọn sau luồng chưa xong (%s)" % (j + 1, e))
                else:
                    self.alts[j].update(res="skip", note="Chưa tự động – kiểm tra tay khi cần", at=now_iso())
        finally:
            obs_stop(self)
        res = [s["res"] for s in self.steps + self.alts]
        main_res = [s["res"] for s in self.steps]
        status = "fail" if "bad" in res else ("pass" if main_res and all(x == "ok" for x in main_res) else "blocked")
        lines = []
        if status == "blocked":                        # dừng giữa chừng / bỏ qua bước: nêu bước đầu tiên chưa đạt
            for i, st in enumerate(self.steps):
                if st["res"] != "ok":
                    lines.append("Dừng ở bước %d: %s" % (i + 1, st.get("note") or "chưa chạy"))
                    break
        for b in self.bugs:
            lab = ("Bước %d" if b["kind"] == "step" else "Luồng A%d") % (b["stepIndex"] + 1)
            lines.append(lab + " — " + ("Lỗi EX" + (" (menu code %s)" % b.get("menuCode") if b.get("menuCode") else "") + ": " + (b.get("exDetail", "").split("\n")[0][:160]) if b["type"] == "ex" else "Lỗi chức năng: " + b.get("actualData", "")[:160]))
        CAP.finish()
        self.say("Kết thúc: %s" % {"pass": "Đạt", "fail": "Không đạt", "blocked": "Bị chặn"}[status])
        out = dict(format="aq-autotest-run/1", runId=self.id, scenarioId=sc["id"], scenarioCode=sc["code"], scenarioTitle=sc.get("title", ""),
                   product=sc.get("product", "edusoft"), module=sc.get("module", ""), runnerId=CFG.get("runnerId"), machine=CFG.get("machine", ""),
                   path=self.es.exe, version=self.es.version or CFG.get("version", ""), status=status, startedAt=self.started, finishedAt=now_iso(),
                   steps=self.steps, alts=self.alts, process="\n".join(self.log), actual="\n".join(lines + ([self.summary()] if self.summary() else [])) if lines else (("Tất cả bước đạt. " if status == "pass" else "") + self.summary()),
                   video=self.video, bugs=self.bugs, release=sc.get("release") or CFG.get("release"), dumps=self.dumps, vars=self.vars, kitVersion=KIT_VERSION)
        (self.dir / "result.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), "utf-8")
        try:
            write_excel(out, self.dir, sc)
        except Exception as e:
            print("   (Không xuất được Excel: %s)" % e)
        return status


# ---------------------------------------------------------------- test đăng nhập (CHUNG-001)
def run_login_test(sc, es, account, password):
    """Kịch bản CHUNG-001, mở Edusoft MỘT lần: Bước 1 → 3 (tới khung đăng nhập) → các luồng con ở khung đăng nhập
    (sai mật khẩu, bỏ trống tên, sai tên – đóng thông báo, vẫn ở khung đăng nhập) → Bước 4 → 6 (đăng nhập đúng)
    → luồng con còn lại (đường dẫn sai, khung đen). Chỉ mở lại Edusoft khi luồng con lỡ đăng nhập được.
    Dải chú thích hiển thị nguyên văn bước / luồng của kịch bản để support đối chiếu."""
    r = Run(sc, es)
    r.say("Bắt đầu %s – %s (script %s, chế độ trình diễn)" % (sc["code"], sc.get("title", ""), KIT_VERSION))
    obs_start(r)
    steps, alts = r.steps, r.alts
    st_text = sc.get("steps") or []
    alt_def = sc.get("altFlows") or []
    n = len(steps)
    black = {"seen": False}

    CAP.begin(sc, steps, alts)

    def cap(i, extra=""):
        CAP.at("step", i, st_text[i] if i < len(st_text) else "")
        if extra:
            CAP.show("Bước %d" % (i + 1), extra)
        time.sleep(STEP_DELAY)

    def ok(rec, note="", shot=None):
        rec["res"], rec["note"], rec["at"] = "ok", note, now_iso()
        if shot:
            f = r.shot(shot)
            if f:
                rec["shots"].append(f)

    def bad(rec, kind, idx, text, msg, shot=None, expected=""):
        rec["res"], rec["note"], rec["at"] = "bad", msg[:200], now_iso()
        if shot:
            f = r.shot(shot)
            if f:
                rec["shots"].append(f)
        r.bugs.append(dict(kind=kind, stepIndex=idx, stepText=text, type="func", action="Đăng nhập",
                           expectedData=expected or text, actualData=msg, shots=list(rec["shots"])))

    def open_login():
        """Mở Edusoft tới khung đăng nhập; lần mở đầu khung đen / không hiện thì đóng và mở lại."""
        es.launch()
        try:
            return es.wait_login(60)
        except Exception:
            black["seen"] = True
            r.say("Khung đăng nhập chưa hiện sau 60 giây (khung đen) – đóng và chạy lại Edusoft")
            return es.restart_to_login()

    # ================= LUỒNG THAY THẾ: A1, A2, … =================
    def alt_cap(j, text):
        CAP.at("alt", j, "%s — %s" % (alt_def[j].get("name", ""), text))
        time.sleep(STEP_DELAY)

    def do_alt(j, early=False):
        """early=True: đang ở khung đăng nhập của luồng chính – thử luồng con ngay đó, không mở lại Edusoft."""
        a = alt_def[j]
        name = norm(a.get("name", ""))
        rec = alts[j]
        a_steps = a.get("steps") or []
        try:
            if not CFG.get("loginNegatives", True):
                raise LookupError("tắt")
            if "đường dẫn" in name:
                bad_path = str(Path(es.exe).with_name("KhongTonTai_Edusoft.NET.exe"))
                alt_cap(j, (a_steps[0] if a_steps else "") + "   ▸ thử chạy " + bad_path)
                started = False
                try:
                    if os.path.isfile(bad_path):
                        started = True
                    else:
                        Application(backend="uia").start('"%s"' % bad_path, timeout=10)
                        started = True
                except Exception:
                    started = False
                if started:
                    rec["res"], rec["note"] = "bad", "Vẫn chạy được với đường dẫn sai"
                else:
                    ok(rec, "Không mở được Edusoft – không tìm thấy file (đúng như mong đợi)")
                    r.say("Luồng A%d: ĐẠT — đường dẫn sai thì không mở được Edusoft" % (j + 1))
                return
            wrong_user = "sai tên" in name or "sai tài khoản" in name
            if "trống" in name or "sai mật khẩu" in name or wrong_user:
                empty = "trống" in name
                u = p = None
                if early:
                    try:
                        es.close_dialogs(3)
                        u, p = es.login_fields()
                    except Exception:
                        u = p = None
                if u is None:                       # không còn ở khung đăng nhập: mới phải mở lại Edusoft
                    alt_cap(j, "Mở lại Edusoft tới khung đăng nhập")
                    es.kill()
                    open_login()
                    u, p = es.login_fields()
                if empty:
                    want_u = ""
                    alt_cap(j, a_steps[0] if a_steps else "Xóa sạch ô Tên đăng nhập")
                    es.set_field(u, "")
                    es.set_field(p, password, secret=True)
                elif wrong_user:
                    want_u = account + "_khongtontai"
                    alt_cap(j, (a_steps[0] if a_steps else "Nhập tên đăng nhập không tồn tại, mật khẩu đúng") + "   ▸ " + want_u + " / mật khẩu đúng")
                    es.set_field(u, want_u)
                    es.set_field(p, password, secret=True)
                else:
                    want_u = account
                    alt_cap(j, (a_steps[0] if a_steps else "Nhập tài khoản và mật khẩu sai") + "   ▸ " + account + " / mật khẩu sai")
                    es.set_field(u, account)
                    es.set_field(p, password + "_sai", secret=True)
                got_u = (es.field_value(u) or "").strip()
                if got_u != want_u:
                    raise RuntimeError("Ô Tên đăng nhập đang là \"%s\", không phải \"%s\" như luồng yêu cầu" % (got_u, want_u))
                alt_cap(j, a_steps[1] if len(a_steps) > 1 else "Bấm Đăng nhập")
                try:
                    how = es.click_login()
                except RuntimeError as e:
                    if not empty or es.find_main() is not None:
                        raise
                    how = "không thấy phản hồi"          # bỏ trống tên: Edusoft có thể chỉ báo ngay trên khung, không mở hộp thoại
                    r.say("Luồng A%d – %s" % (j + 1, e))
                r.say("Luồng A%d – bấm Đăng nhập: %s" % (j + 1, how))
                if how == "khóa":
                    f = r.shot("luong-a%d" % (j + 1))
                    if f:
                        rec["shots"].append(f)
                    rec["res"], rec["at"] = "ok", now_iso()
                    rec["note"] = "Bị chặn – nút Đăng nhập bị khóa, vẫn ở khung đăng nhập"
                    r.say("Luồng A%d: ĐẠT — nút Đăng nhập bị khóa" % (j + 1))
                    return
                ds = es.wait_dialog(10)
                if not ds and es.wait_main(30):      # không có thông báo: chờ thêm để chắc chắn không lọt vào màn hình chính
                    ds = []
                f = r.shot("luong-a%d" % (j + 1))
                if f:
                    rec["shots"].append(f)
                msg = " / ".join(es.dialog_text(d).replace("\n", " ")[:200] for d in ds)
                if es.find_main() is not None:
                    rec["res"], rec["note"], rec["at"] = "bad", "Vẫn vào được màn hình chính", now_iso()
                    r.bugs.append(dict(kind="alt", stepIndex=j, stepText=a.get("name", ""), type="func", action="Đăng nhập",
                                       expectedData=a.get("expected", "Bị chặn"), actualData="Đăng nhập được dù " + a.get("name", "").lower(), shots=list(rec["shots"])))
                    r.say("Luồng A%d: LỖI — vẫn đăng nhập được" % (j + 1))
                    if early:                       # đã lọt vào màn hình chính: buộc mở lại để chạy tiếp luồng chính
                        es.kill()
                        open_login()
                        rec["note"] += " · đã mở lại Edusoft để chạy tiếp luồng chính"
                    return
                alt_cap(j, "Thông báo: " + (msg or "(không có thông báo)") + "   ▸ đóng thông báo")
                closed = es.close_dialogs(10)
                f2 = r.shot("luong-a%d-sau" % (j + 1))
                if f2:
                    rec["shots"].append(f2)
                rec["res"], rec["at"] = "ok", now_iso()
                rec["note"] = ("Bị chặn – " + msg if msg else "Bị chặn, vẫn ở khung đăng nhập") + ("" if closed else " · KHÔNG đóng được thông báo")
                r.say("Luồng A%d: ĐẠT — bị chặn%s%s" % (j + 1, (" (" + msg[:120] + ")") if msg else "", "" if closed else " · không đóng được thông báo"))
                return
            if "đen" in name:
                if black["seen"]:
                    ok(rec, "Lần mở đầu khung đen / không hiện; chạy lại thì hiện bình thường")
                else:
                    rec["res"], rec["note"] = "skip", "Không xảy ra trong lần chạy này"
                return
            rec["res"], rec["note"] = "skip", "Chưa tự động – kiểm tra tay khi cần"
        except LookupError:
            rec["res"], rec["note"] = "skip", "Đã tắt kiểm tra luồng thay thế (config.json)"
        except Exception as e:
            f = r.shot("luong-a%d-loi" % (j + 1))
            if f:
                rec["shots"].append(f)
            rec["res"], rec["note"], rec["at"] = "bad", "Script dừng: %s" % e, now_iso()
            r.bugs.append(dict(kind="alt", stepIndex=j, stepText=a.get("name", ""), type="func", action="Đăng nhập",
                               expectedData=a.get("expected", ""), actualData="Script không thực hiện được: %s" % e, shots=list(rec["shots"])))
            r.say("Luồng A%d: LỖI — %s" % (j + 1, e))
        finally:
            if rec["res"] and not rec.get("at"):
                rec["at"] = now_iso()

    NEG = ("trống", "sai mật khẩu", "sai tên", "sai tài khoản")
    done = set()

    # ================= LUỒNG CHÍNH: Bước 1 → 6 =================
    cur = 0
    try:
        cap(0, es.exe)
        if not os.path.isfile(es.exe):
            raise FileNotFoundError("Không tìm thấy file " + es.exe)
        ok(steps[0], es.exe)
        r.say("Bước 1: ĐẠT — " + es.exe)

        cur = 1
        cap(1)
        es.launch()
        time.sleep(3)
        ok(steps[1], "Đã chạy Edusoft.NET.exe", "buoc-2")
        r.say("Bước 2: ĐẠT — đã chạy Edusoft.NET.exe")

        cur = 2
        cap(2)
        try:
            es.wait_login(60)
        except Exception:
            black["seen"] = True
            r.say("Khung đăng nhập chưa hiện sau 60 giây (khung đen) – đóng và chạy lại Edusoft")
            es.restart_to_login()
        ok(steps[2], "Khung đăng nhập hiển thị" + (" (sau khi chạy lại do khung đen)" if black["seen"] else ""), "buoc-3")
        r.say("Bước 3: ĐẠT — khung đăng nhập hiển thị")

        # luồng con ở khung đăng nhập (sai mật khẩu, bỏ trống tên…): thử ngay tại đây rồi mới đăng nhập đúng – không mở lại Edusoft
        early = [j for j, a in enumerate(alt_def) if any(k in norm(a.get("name", "")) for k in NEG)]
        if early and CFG.get("loginNegatives", True):
            r.say("Luồng con tại khung đăng nhập (trước khi đăng nhập đúng, cùng phiên Edusoft): " + ", ".join("A%d" % (j + 1) for j in early))
            for j in early:
                do_alt(j, early=True)
                done.add(j)
            es.close_dialogs(3)
            CAP.show("%s · Tiếp luồng chính" % sc["code"], "Xong luồng con ở khung đăng nhập – đăng nhập đúng (bước 4 → 6)")

        u, p = es.login_fields()
        ru, rp = u.rectangle(), p.rectangle()
        r.say("Ô Tên đăng nhập: (%d,%d)-(%d,%d) · ô Mật khẩu: (%d,%d)-(%d,%d)" % (ru.left, ru.top, ru.right, ru.bottom, rp.left, rp.top, rp.right, rp.bottom))
        cur = 3
        cap(3, account)
        if not es.set_field(u, account):
            raise RuntimeError("Ô Tên đăng nhập không nhận đúng \"%s\" (đang là \"%s\")" % (account, es.field_value(u)))
        ok(steps[3], account, "buoc-4")
        r.say("Bước 4: ĐẠT — nhập " + account)

        cur = 4
        cap(4, "•" * len(password))
        if not es.set_field(p, password, secret=True):
            raise RuntimeError("Không đưa được con trỏ vào ô Mật khẩu")
        if (es.field_value(u) or account).strip() != account:
            raise RuntimeError("Mật khẩu bị gõ vào ô Tên đăng nhập (ô này đang là \"%s\")" % es.field_value(u))
        ok(steps[4], "Đã nhập mật khẩu (%d ký tự) vào ô Mật khẩu" % len(password), "buoc-5")
        r.say("Bước 5: ĐẠT — nhập mật khẩu (%d ký tự)" % len(password))

        cur = 5
        cap(5)
        es.close_dialogs(5)
        if (es.field_value(u) or "").strip() != account:
            if not es.set_field(u, account):
                raise RuntimeError("Tên đăng nhập bị thay đổi trước khi bấm Đăng nhập (đang là \"%s\")" % es.field_value(u))
        how = es.click_login()
        r.say("Bấm Đăng nhập: " + how)
        entered = es.wait_main(90)
        if not entered:
            ds = es.dialogs_other()
            msg0 = " ".join(es.dialog_text(d) for d in ds)
            if re.search(r"không thành công|sai|incorrect|invalid", msg0, re.I) and sys.stdin and sys.stdin.isatty():
                f0 = r.shot("buoc-6-sai-mat-khau")
                if f0:
                    steps[5]["shots"].append(f0)
                es.close_dialogs(8)
                r.say("Đăng nhập không thành công với mật khẩu đã lưu (%d ký tự) – hỏi lại mật khẩu" % len(password))
                CAP.show("%s · Bước 6" % sc["code"], "Mật khẩu đã lưu không đúng – nhập lại mật khẩu ở cửa sổ đen")
                new_pw = ask_password("edusoft", account, reask=True)
                if new_pw:
                    password = new_pw
                    u, p = es.login_fields()
                    es.set_field(u, account)
                    es.set_field(p, password, secret=True)
                    es.click_login()
                    entered = es.wait_main(90)
        if entered:
            if not r.check_ex(steps[5], "Bước 6", "step", 5, st_text[5] if len(st_text) > 5 else ""):
                ok(steps[5], "Vào màn hình chính " + (es.version or ""), "buoc-6")
                r.say("Bước 6: ĐẠT — vào màn hình chính %s" % es.version)
        else:
            ds = es.dialogs_other()
            msg = " / ".join(es.dialog_text(d).replace("\n", " ")[:200] for d in ds)
            if not r.check_ex(steps[5], "Bước 6", "step", 5, st_text[5] if len(st_text) > 5 else ""):
                bad(steps[5], "step", 5, st_text[5] if len(st_text) > 5 else "", "Không vào được màn hình chính sau 90 giây" + (": " + msg if msg else ""), "buoc-6-loi",
                    expected=sc.get("expected", ""))
                r.say("Bước 6: LỖI — không vào được màn hình chính" + (" (" + msg[:120] + ")" if msg else ""))
            es.close_dialogs(6)
    except Exception as e:
        if cur < n and steps[cur]["res"] is None:
            bad(steps[cur], "step", cur, st_text[cur] if cur < len(st_text) else "", str(e), "buoc-%d-loi" % (cur + 1))
        r.say("Dừng ở bước %d: %s" % (cur + 1, e))
        for k in range(cur + 1, n):
            if steps[k]["res"] is None:
                steps[k]["res"], steps[k]["note"] = "skip", "Không chạy do bước %d lỗi" % (cur + 1)

    # luồng con còn lại (đường dẫn sai, khung đen…) – sau khi luồng chính đã ghi nhận
    for j in sorted(range(len(alt_def)), key=lambda k: (alt_at(alt_def[k], n), k)):
        if j not in done:
            do_alt(j)
            done.add(j)

    obs_stop(r)
    if CFG.get("closeAfter", True):
        CAP.show("%s · Kết thúc" % sc["code"], "Đóng Edusoft đã mở cho lần test")
        es.kill()
    main_res = [x["res"] for x in steps]
    status = "fail" if "bad" in main_res + [a["res"] for a in alts] else ("pass" if all(x == "ok" for x in main_res) else "blocked")
    CAP.finish()
    r.say("Kết thúc: %s" % {"pass": "Đạt", "fail": "Không đạt", "blocked": "Bị chặn"}[status])
    lines = [("Bước %d" if b["kind"] == "step" else "Luồng A%d") % (b["stepIndex"] + 1) + " — " + b.get("actualData", "") for b in r.bugs]
    out = dict(format="aq-autotest-run/1", kitVersion=KIT_VERSION, runId=r.id, scenarioId=sc["id"], scenarioCode=sc["code"], scenarioTitle=sc.get("title", ""),
               product="edusoft", module=sc.get("module", "CHUNG"), runnerId=CFG.get("runnerId"), machine=CFG.get("machine", ""), path=es.exe,
               version=es.version or CFG.get("version", ""), status=status, startedAt=r.started, finishedAt=now_iso(), steps=steps, alts=alts,
               process="\n".join(r.log), actual=("Đăng nhập thành công, vào màn hình chính %s." % es.version if status == "pass" else "\n".join(lines)),
               video=r.video, bugs=r.bugs, release=sc.get("release"), account=account, kind="login")
    (r.dir / "result.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), "utf-8")
    try:
        write_excel(out, r.dir, sc)
    except Exception as e:
        print("   (Không xuất được Excel: %s)" % e)
    return status, False


# ---------------------------------------------------------------- xuất Excel
RES_VN = {"ok": "Đạt", "bad": "Lỗi", "skip": "Bỏ qua", None: "Chưa chạy"}
ST_VN = {"pass": "Đạt", "fail": "Không đạt", "blocked": "Bị chặn"}


def _openpyxl():
    try:
        import openpyxl
        return openpyxl
    except Exception:
        try:
            import subprocess
            print("   (Cài thư viện openpyxl để xuất Excel…)")
            subprocess.call([sys.executable, "-m", "pip", "install", "-q", "openpyxl"])
            import openpyxl
            return openpyxl
        except Exception:
            return None


def write_excel(out, run_dir, sc):
    """Ghi ket-qua.xlsx trong thư mục lượt chạy (có ảnh từng bước) và thêm dòng vào results/tong-hop.xlsx."""
    xl = _openpyxl()
    if xl is None:
        print("   (Không xuất được Excel – thiếu openpyxl)")
        return
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.drawing.image import Image as XImg
    head = Font(bold=True, color="FFFFFF")
    fill = PatternFill("solid", fgColor="4F46E5")
    col = {"Đạt": "DCFCE7", "Lỗi": "FEE2E2", "Bỏ qua": "F1F5F9", "Chưa chạy": "F1F5F9"}
    wb = xl.Workbook()
    ws = wb.active
    ws.title = "Tổng quan"
    info = [("Mã kịch bản", out["scenarioCode"]), ("Tên kịch bản", out["scenarioTitle"]), ("Kết quả", ST_VN.get(out["status"], out["status"])),
            ("Mã lượt chạy", out["runId"]), ("Bắt đầu", out["startedAt"]), ("Kết thúc", out["finishedAt"]), ("Máy", out.get("machine", "")),
            ("Đường dẫn Edusoft", out.get("path", "")), ("Phiên bản Edusoft", out.get("version", "")), ("Tài khoản", out.get("account", "")),
            ("Bộ test", out.get("kitVersion", "")), ("Kết quả thực tế", out.get("actual", ""))]
    for i, (k, v) in enumerate(info, 1):
        ws.cell(i, 1, k).font = Font(bold=True)
        ws.cell(i, 2, v).alignment = Alignment(wrap_text=True, vertical="top")
    ws.column_dimensions["A"].width = 22
    ws.column_dimensions["B"].width = 90
    d = wb.create_sheet("Chi tiết")
    cols = ["Loại", "STT", "Nội dung bước / luồng", "Kết quả mong muốn", "Kết quả", "Ghi chú", "Thời điểm", "Ảnh"]
    for j, c in enumerate(cols, 1):
        cell = d.cell(1, j, c)
        cell.font, cell.fill = head, fill
    widths = [10, 6, 60, 40, 10, 50, 22, 48]
    for j, w in enumerate(widths, 1):
        d.column_dimensions[chr(64 + j)].width = w
    rows = []
    for i, st in enumerate(out["steps"]):
        rows.append(("Bước", i + 1, (sc.get("steps") or [""] * 99)[i] if i < len(sc.get("steps") or []) else "", sc.get("expected", "") if i == len(out["steps"]) - 1 else "", st))
    for i, st in enumerate(out["alts"]):
        a = (sc.get("altFlows") or [{}] * 99)[i] if i < len(sc.get("altFlows") or []) else {}
        rows.append(("Luồng", "A%d" % (i + 1), "%s — %s" % (a.get("name", ""), a.get("condition", "")), a.get("expected", ""), st))
    r = 2
    for kind, no, text, exp, st in rows:
        res = RES_VN.get(st.get("res"), st.get("res") or "")
        vals = [kind, no, text, exp, res, st.get("note", ""), st.get("at") or ""]
        for j, v in enumerate(vals, 1):
            c = d.cell(r, j, v)
            c.alignment = Alignment(wrap_text=True, vertical="top")
        d.cell(r, 5).fill = PatternFill("solid", fgColor=col.get(res, "FFFFFF"))
        shots = [x for x in (st.get("shots") or []) if (run_dir / x).exists()]
        if shots:
            try:
                img = XImg(str(run_dir / shots[0]))
                ratio = 330.0 / max(1, img.width)
                img.width, img.height = int(img.width * ratio), int(img.height * ratio)
                d.add_image(img, "H%d" % r)
                d.row_dimensions[r].height = img.height * 0.75 + 6
                if len(shots) > 1:
                    d.cell(r, 6).value = (st.get("note", "") + "  (thêm ảnh: " + ", ".join(shots[1:]) + ")").strip()
            except Exception:
                d.cell(r, 8, ", ".join(shots))
        else:
            d.row_dimensions[r].height = 32
        r += 1
    d.freeze_panes = "A2"
    wb.save(run_dir / "ket-qua.xlsx")
    # tổng hợp
    tf = BASE / "results" / "tong-hop.xlsx"
    try:
        tw = xl.load_workbook(tf) if tf.exists() else None
    except Exception:
        tw = None
    if tw is None:
        tw = xl.Workbook()
        t = tw.active
        t.title = "Tổng hợp"
        for j, c in enumerate(["Thời điểm", "Mã KB", "Tên kịch bản", "Kết quả", "Bước đạt", "Bước lỗi", "Luồng đạt", "Luồng lỗi", "Phiên bản Edusoft", "Máy", "Kết quả thực tế", "Mã lượt chạy"], 1):
            cell = t.cell(1, j, c)
            cell.font, cell.fill = head, fill
        for j, w in enumerate([20, 12, 40, 12, 10, 10, 10, 10, 20, 14, 60, 34], 1):
            t.column_dimensions[chr(64 + j)].width = w
    t = tw["Tổng hợp"] if "Tổng hợp" in tw.sheetnames else tw.active
    cnt = lambda lst, k: sum(1 for x in lst if x.get("res") == k)
    t.append([out["finishedAt"], out["scenarioCode"], out["scenarioTitle"], ST_VN.get(out["status"], out["status"]), cnt(out["steps"], "ok"), cnt(out["steps"], "bad"),
              cnt(out["alts"], "ok"), cnt(out["alts"], "bad"), out.get("version", ""), out.get("machine", ""), out.get("actual", ""), out["runId"]])
    try:
        tw.save(tf)
    except Exception as e:
        print("   (Không ghi được tong-hop.xlsx – có thể file đang mở trong Excel: %s)" % e)


# ---------------------------------------------------------------- OBS (tùy chọn)
def obs_client():
    o = CFG.get("obs") or {}
    if not o.get("enabled"):
        return None
    try:
        import obsws_python as obs
        pw = get_secret("obs", o.get("host", "localhost"), ask="Mật khẩu OBS WebSocket (Tools → WebSocket Server Settings, bỏ trống nếu không đặt): ")
        return obs.ReqClient(host=o.get("host", "localhost"), port=int(o.get("port", 4455)), password=pw or "", timeout=5)
    except Exception as e:
        print("   (Không kết nối được OBS – bỏ qua quay video: %s)" % e)
        o["enabled"] = False
        return None


OBS = None


def obs_start(run):
    global OBS
    if OBS is None:
        OBS = obs_client()
    if OBS:
        try:
            OBS.start_record()
            time.sleep(1)
        except Exception as e:
            run.say("Không bật được quay video OBS: %s" % e)


def obs_stop(run):
    if not OBS:
        return
    try:
        time.sleep(1)
        r = OBS.stop_record()
        src = getattr(r, "output_path", None)
        time.sleep(2)
        if src and os.path.exists(src):
            dst = run.dir / ("video" + Path(src).suffix)
            shutil.copy2(src, dst)
            run.video = dst.name
    except Exception as e:
        run.say("Không lưu được video OBS: %s" % e)


# ---------------------------------------------------------------- bí mật
def get_secret(kind, user, ask):
    key = "AQ-Autotest:" + kind
    if keyring:
        try:
            v = keyring.get_password(key, user)
            if v is not None:
                return v
        except Exception:
            pass
    v = getpass.getpass("   " + ask)
    if keyring and v:
        try:
            keyring.set_password(key, user, v)
            print("   (Đã lưu vào Windows Credential Manager – lần sau không hỏi lại. Xóa: chay-test.bat --quen-mat-khau)")
        except Exception:
            pass
    return v


def ask_password(kind, user, reask=False):
    """Mật khẩu Edusoft: lấy từ Windows Credential Manager; chưa có (hoặc reask) thì hỏi 2 lần cho khớp."""
    key = "AQ-Autotest:" + kind
    if keyring and not reask:
        try:
            v = keyring.get_password(key, user)
            if v:
                print("   Dùng mật khẩu đã lưu cho %s (%d ký tự). Sai thì chạy quen-mat-khau.bat." % (user, len(v)))
                return v
        except Exception:
            pass
    for _ in range(3):
        a = getpass.getpass("   Mật khẩu Edusoft của tài khoản %s (môi trường test, gõ không hiện chữ): " % user)
        b = getpass.getpass("   Nhập lại mật khẩu để xác nhận: ")
        if a and a == b:
            print("   Mật khẩu có %d ký tự." % len(a))
            if keyring:
                try:
                    keyring.set_password(key, user, a)
                    print("   (Đã lưu vào Windows Credential Manager – lần sau không hỏi lại.)")
                except Exception:
                    pass
            return a
        print("   Hai lần nhập không khớp hoặc để trống – nhập lại.")
    return ""


def forget():
    if keyring:
        for kind, user in (("edusoft", CFG.get("account", "")), ("obs", (CFG.get("obs") or {}).get("host", "localhost"))):
            try:
                keyring.delete_password("AQ-Autotest:" + kind, user)
            except Exception:
                pass
    print("Đã xóa mật khẩu đã lưu.")


# ---------------------------------------------------------------- kiểm tra cài đặt
def user_env(name):
    """Biến môi trường của người đang dùng máy. cai-dat.bat xin quyền admin nên truyền APPDATA /
    LOCALAPPDATA / USERPROFILE gốc qua AQ_USER_* (tài khoản admin khác có hồ sơ khác)."""
    return os.environ.get("AQ_USER_" + name) or os.environ.get(name) or ""


def claude_cfg_dirs():
    """Thư mục cấu hình Claude app (bản cài thường và bản Microsoft Store) của người dùng."""
    dirs = []
    ad, la = user_env("APPDATA"), user_env("LOCALAPPDATA")
    if ad and (Path(ad) / "Claude").is_dir():
        dirs.append(Path(ad) / "Claude")
    if la:
        dirs += [d for d in (Path(la) / "Packages").glob("Claude*/LocalCache/Roaming/Claude") if d.is_dir()]
    return dirs


def ps(cmd, timeout=20):
    import subprocess
    try:
        r = subprocess.run(["powershell", "-NoProfile", "-Command", cmd], capture_output=True, text=True, timeout=timeout)
        return (r.stdout or "").strip()
    except Exception:
        return ""


def agent_running():
    try:
        import ctypes
        h = ctypes.windll.kernel32.OpenMutexW(0x00100000, False, "AQAutotestAgentMutex")
        if h:
            ctypes.windll.kernel32.CloseHandle(h)
            return True
    except Exception:
        pass
    return False


def diagnose():
    """In bảng kiểm tra cài đặt (cai-dat.bat gọi ở cuối; chạy tay: chay-test.bat --chan-doan) và lưu chan-doan.txt."""
    import importlib.util
    rows = []

    def add(st, name, detail=""):
        rows.append("%s %s%s" % ({"ok": "[ OK ]", "warn": "[ !! ]", "fail": "[LỖI]"}[st], name, (" – " + detail) if detail else ""))
        print(rows[-1])

    print()
    print("=== Kiểm tra cài đặt AQ Autotest – bộ test %s – %s ===" % (KIT_VERSION, datetime.datetime.now().strftime("%d/%m/%Y %H:%M")))
    base, tmp = str(BASE), (user_env("TEMP") or os.environ.get("TEMP") or "").lower()
    if (tmp and base.lower().startswith(tmp)) or ".zip" in base.lower():
        add("fail", "Thư mục bộ test", base + " là thư mục tạm / nằm trong file .zip – giải nén rồi chạy cai-dat.bat để cài vào thư mục cố định")
    else:
        add("ok", "Thư mục bộ test", base)
    add("ok", "Python", sys.executable)
    miss = [m for m in ("pywinauto", "PIL", "keyboard", "keyring", "openpyxl") if importlib.util.find_spec(m) is None]
    add("fail" if miss else "ok", "Thư viện", ("thiếu " + ", ".join(miss) + " – chạy lại cai-dat.bat, kiểm tra mạng") if miss else "đủ")
    exe = CFG.get("exe") or ""
    add("ok" if exe and Path(exe).exists() else "fail", "Edusoft.NET.exe",
        exe if exe and Path(exe).exists() else (exe or "chưa khai báo") + " – không thấy file; sửa đường dẫn ở bước 1 trên console rồi tải lại bộ cài")
    add("ok" if agent_running() else "warn", "AQ Autotest Agent",
        "đang chạy" if agent_running() else "chưa chạy – chạy lại cai-dat.bat (chọn Yes khi hỏi quyền admin)")
    try:
        bridge_diag(add)
    except Exception as e:
        add("warn", "Cầu nối Claude app", "không kiểm tra được: %s" % e)
    try:
        (BASE / "chan-doan.txt").write_text("\n".join(rows) + "\n", "utf-8")
    except Exception:
        pass
    return rows


# ---------------------------------------------------------------- dò giao diện
def dump():
    from pywinauto import Desktop
    wins = [w for w in Desktop(backend="uia").windows() if re.search(r"EduSoft", w.window_text(), re.I)]
    if not wins:
        print("Không thấy cửa sổ Edusoft nào đang mở. Hãy mở Edusoft (đúng bản cần test), vào màn hình cần dò rồi chạy lại.")
        return
    fn = BASE / ("dump-%s.txt" % datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
    with open(fn, "w", encoding="utf-8") as f:
        for w in wins:
            f.write("=== %s ===\n" % w.window_text())
            for el in w.descendants():
                try:
                    if not el.is_visible():
                        continue
                    r = el.rectangle()
                    f.write("%-12s | %-40s | id=%s | %d,%d,%d,%d\n" % (el.element_info.control_type, el.window_text()[:80], el.element_info.automation_id, r.left, r.top, r.right, r.bottom))
                except Exception:
                    continue
    print("Đã ghi", fn, "— gửi file này cho Claude để viết lệnh tự động cho từng bước.")


# ---------------------------------------------------------------- tự cập nhật bộ test
def update_dirs():
    ds = [BASE, Path(os.path.expanduser("~")) / "Downloads"]
    try:
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders") as k:
            v = winreg.QueryValueEx(k, "{374DE290-123F-4565-9164-39C4925E467B}")[0]
            ds.append(Path(os.path.expandvars(v)))
    except Exception:
        pass
    out = []
    for d in ds:
        if d not in out and d.is_dir():
            out.append(d)
    return out


def pack_results(since):
    """Gói các lượt vừa chạy thành một file .zip trong thư mục Tải về – dùng khi console không nối thẳng
    máy chạy test: trên console bấm Nhập kết quả… và chọn file này."""
    import zipfile
    runs = [d for d in (BASE / "results").glob("*") if (d / "result.json").is_file() and (d / "result.json").stat().st_mtime >= since - 1]
    if not runs:
        return None
    ds = [d for d in update_dirs() if d != BASE]
    out = (ds[-1] if ds else BASE / "results") / ("AQ-ket-qua-%s.zip" % time.strftime("%y%m%d-%H%M%S"))
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for d in runs:
            for f in d.rglob("*"):
                if f.is_file() and not (f.suffix.lower() in (".mp4", ".mkv") and f.stat().st_size > 20 * 1024 * 1024):
                    z.write(f, d.name + "/" + f.relative_to(d).as_posix())
    return out


def archive_cmd(f, tag):
    """Chuyển file lệnh đã dùng vào lenh-da-xu-ly/ với tên kèm thời gian (không bao giờ trùng tên)."""
    import shutil
    d = BASE / "lenh-da-xu-ly"
    d.mkdir(exist_ok=True)
    shutil.move(str(f), str(d / ("%s-%s-%s" % (datetime.datetime.now().strftime("%Y%m%d-%H%M%S-%f"), tag, f.name))))


def apply_update(path=None):
    """Áp dụng file aq-autotest-update*.json: `path` do Agent đưa (đã nhận sẵn), hoặc tìm bản mới nhất chưa áp dụng
    trong thư mục bộ test / Tải về (khi chạy chay-test.bat). Trả về True nếu đã cập nhật."""
    cands = []
    if path:
        cands = [Path(path)]
    else:
        for d in update_dirs():
            try:
                cands += [p for p in d.glob("aq-autotest-update*.json") if ".da-" not in p.name]
            except Exception:
                pass
    cands.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    stamp_f = BASE / ".update-stamp"
    last = stamp_f.read_text("utf-8").strip() if stamp_f.exists() else ""
    for f in cands:
        try:
            data = json.loads(f.read_text("utf-8"))
        except Exception:
            continue
        if data.get("format") != "aq-autotest-update/1":
            continue
        gen = str(data.get("generatedAt", ""))
        if gen and last and gen <= last:
            if not path:
                try:
                    archive_cmd(f, "da-ap-dung")
                except Exception:
                    pass
            continue
        files = data.get("files") or {}
        for name, content in files.items():
            name = name.replace("\\", "/")
            if ".." in name or name.startswith("/") or ":" in name:
                continue
            dest = BASE / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            if name.lower().endswith(".bat"):
                dest.write_bytes(content.replace("\r\n", "\n").replace("\n", "\r\n").encode("utf-8"))
            elif name.lower().endswith(".txt"):
                dest.write_text("\ufeff" + content.lstrip("\ufeff"), "utf-8")
            else:
                dest.write_text(content, "utf-8")
        if data.get("replaceScenarios"):
            keep = {n.split("/")[-1] for n in files if n.startswith("scenarios/")}
            for old in (BASE / "scenarios").glob("*.json"):
                if old.name not in keep:
                    old.unlink()
        cfg = data.get("config") or {}
        if cfg:
            cur = json.loads((BASE / "config.json").read_text("utf-8"))
            cur.update(cfg)
            (BASE / "config.json").write_text(json.dumps(cur, ensure_ascii=False, indent=2), "utf-8")
        stamp_f.write_text(gen or now_iso(), "utf-8")
        # chạy tay (chay-test.bat) thì lệnh chạy đi kèm coi như đã dùng – Agent không chạy thêm lần nữa
        if not path:
            try:
                archive_cmd(f, "chay-tay" if data.get("run") else "da-ap-dung")
            except Exception:
                pass
        print("Đã cập nhật bộ test lên phiên bản %s (%d file) từ %s" % (data.get("kitVersion", "?"), len(files), f))
        return True
    return False


def unregister_claude_bridge():
    """Gỡ cầu nối "aq-autotest" đã đăng ký vào Claude app ở bản 2026.10.29-10 (nay console chạy trên
    localhost, server.py làm việc này trực tiếp). Chỉ xoá đúng mục của mình, giữ nguyên cấu hình khác."""
    if os.name != "nt":
        return []
    dirs = claude_cfg_dirs()
    done = []
    for d in dirs:
        f = d / "claude_desktop_config.json"
        try:
            if not f.exists():
                continue
            cur = json.loads(f.read_text("utf-8") or "{}")
            if "aq-autotest" not in (cur.get("mcpServers") or {}):
                continue
            del cur["mcpServers"]["aq-autotest"]
            f.write_text(json.dumps(cur, ensure_ascii=False, indent=2), "utf-8")
            done.append(str(f))
        except Exception:
            continue
    return done


def bridge_diag(add):
    add("ok", "Cầu nối Claude app", "không cần – console chạy trên localhost (server.py nối thẳng thư mục bộ test)")


# ---------------------------------------------------------------- main
# ---------------------------------------------------------------- thử chạy trên desktop ẩn (chay-test.bat --thu-desktop-an)
# Bước thử trước khi chuyển cả bộ test sang desktop ẩn: tạo desktop "AQTest" (CreateDesktop, không hiện lên màn hình người dùng),
# chạy chính aqrun.py trên đó, mở Edusoft, thử từng cách gõ / bấm KHÔNG dùng bàn phím, chuột thật, chụp ảnh bằng PrintWindow.
# Chỉ đăng nhập rồi mở một tab ribbon – không thêm/sửa/xóa dữ liệu. Không ghi mật khẩu vào báo cáo.
HD_NAME = "AQTest"


def _w32():
    import ctypes
    from ctypes import wintypes as W
    u32, k32, g32 = ctypes.windll.user32, ctypes.windll.kernel32, ctypes.windll.gdi32
    P = ctypes.c_void_p
    u32.CreateDesktopW.restype = P
    u32.CreateDesktopW.argtypes = [W.LPCWSTR, W.LPCWSTR, P, W.DWORD, W.DWORD, P]
    u32.CloseDesktop.argtypes = [P]
    u32.GetThreadDesktop.restype = P
    u32.GetThreadDesktop.argtypes = [W.DWORD]
    u32.OpenInputDesktop.restype = P
    u32.OpenInputDesktop.argtypes = [W.DWORD, W.BOOL, W.DWORD]
    u32.GetUserObjectInformationW.argtypes = [P, ctypes.c_int, P, W.DWORD, ctypes.POINTER(W.DWORD)]
    u32.SendMessageTimeoutW.restype = P
    u32.SendMessageTimeoutW.argtypes = [W.HWND, W.UINT, P, P, W.UINT, W.UINT, ctypes.POINTER(P)]
    u32.PostMessageW.argtypes = [W.HWND, W.UINT, P, P]
    u32.GetDC.restype = P
    u32.GetDC.argtypes = [W.HWND]
    u32.ReleaseDC.argtypes = [W.HWND, P]
    u32.PrintWindow.argtypes = [W.HWND, P, W.UINT]
    u32.GetWindowRect.argtypes = [W.HWND, ctypes.POINTER(W.RECT)]
    u32.GetClientRect.argtypes = [W.HWND, ctypes.POINTER(W.RECT)]
    u32.VkKeyScanW.restype = ctypes.c_short
    u32.VkKeyScanW.argtypes = [ctypes.c_wchar]
    u32.MapVirtualKeyW.argtypes = [W.UINT, W.UINT]
    g32.CreateCompatibleDC.restype = P
    g32.CreateCompatibleDC.argtypes = [P]
    g32.CreateCompatibleBitmap.restype = P
    g32.CreateCompatibleBitmap.argtypes = [P, ctypes.c_int, ctypes.c_int]
    g32.SelectObject.restype = P
    g32.SelectObject.argtypes = [P, P]
    g32.DeleteObject.argtypes = [P]
    g32.DeleteDC.argtypes = [P]
    g32.GetDIBits.argtypes = [P, P, W.UINT, W.UINT, P, P, W.UINT]
    k32.WaitForSingleObject.argtypes = [W.HANDLE, W.DWORD]
    k32.CloseHandle.argtypes = [W.HANDLE]
    k32.TerminateProcess.argtypes = [W.HANDLE, W.UINT]
    return ctypes, W, u32, k32, g32


def desk_name(h):
    ctypes, W, u32, k32, g32 = _w32()
    buf = ctypes.create_unicode_buffer(256)
    n = W.DWORD()
    if h and u32.GetUserObjectInformationW(h, 2, buf, ctypes.sizeof(buf), ctypes.byref(n)):   # UOI_NAME
        return buf.value
    return ""


def pw_shot(hwnd, path):
    """Chụp một cửa sổ bằng PrintWindow (chạy được cả khi cửa sổ nằm trên desktop không hiển thị).
    Trả về (đã chụp, ảnh toàn đen)."""
    ctypes, W, u32, k32, g32 = _w32()
    from PIL import Image
    r = W.RECT()
    u32.GetWindowRect(hwnd, ctypes.byref(r))
    w, h = r.right - r.left, r.bottom - r.top
    if w <= 0 or h <= 0:
        return False, True
    sdc = u32.GetDC(None)
    mdc = g32.CreateCompatibleDC(sdc)
    bmp = g32.CreateCompatibleBitmap(sdc, w, h)
    old = g32.SelectObject(mdc, bmp)
    try:
        ok = bool(u32.PrintWindow(hwnd, mdc, 2))        # PW_RENDERFULLCONTENT
        bi = (ctypes.c_uint32 * 10)(40, w, (-h) & 0xFFFFFFFF, 1 | (32 << 16), 0, 0, 0, 0, 0, 0)  # BITMAPINFOHEADER
        buf = ctypes.create_string_buffer(w * h * 4)
        g32.GetDIBits(mdc, bmp, 0, h, buf, bi, 0)
    finally:
        g32.SelectObject(mdc, old)
        g32.DeleteObject(bmp)
        g32.DeleteDC(mdc)
        u32.ReleaseDC(None, sdc)
    img = Image.frombuffer("RGB", (w, h), buf.raw, "raw", "BGRX", 0, 1)
    img.save(path)
    black = all(mx <= 12 for _, mx in img.getextrema())
    return ok, black


def hd_msg(h, m, wp=0, lp=0):
    ctypes, W, u32, k32, g32 = _w32()
    res = ctypes.c_void_p()
    return u32.SendMessageTimeoutW(h, m, wp, lp, 0x0002, 3000, ctypes.byref(res)), res.value   # SMTO_ABORTIFHUNG


def el_hwnd(el):
    e = el
    for _ in range(5):
        try:
            h = e.handle
            if h:
                return h
            e = e.parent()
        except Exception:
            break
    return None


WM_SETTEXT, WM_KEYDOWN, WM_KEYUP, WM_CHAR = 0x000C, 0x0100, 0x0101, 0x0102
EM_SETSEL, WM_LBUTTONDOWN, WM_LBUTTONUP, WM_CLOSE = 0x00B1, 0x0201, 0x0202, 0x0010


def hd_key(h, vk, ch=None):
    """Một lần nhấn phím gửi thẳng vào cửa sổ: WM_KEYDOWN (+ WM_CHAR) + WM_KEYUP, kèm mã quét như phím thật."""
    ctypes, W, u32, k32, g32 = _w32()
    sc = u32.MapVirtualKeyW(vk, 0) & 0xFF
    hd_msg(h, WM_KEYDOWN, vk, 1 | (sc << 16))
    if ch is not None:
        hd_msg(h, WM_CHAR, ord(ch), 1 | (sc << 16))
    hd_msg(h, WM_KEYUP, vk, 1 | (sc << 16) | (3 << 30))


def hd_clear(el, h):
    if h:
        hd_msg(h, EM_SETSEL, 0, -1 & 0xFFFFFFFF)
        hd_key(h, 0x2E)                                    # Delete
        hd_msg(h, EM_SETSEL, 0, -1 & 0xFFFFFFFF)
        hd_key(h, 0x08, "\b")                              # Backspace
    try:
        if (el.get_value() or "").strip():
            el.iface_value.SetValue("")
    except Exception:
        pass


def hd_fill(how, el, h, value):
    ctypes, W, u32, k32, g32 = _w32()
    if how == "uia":
        el.iface_value.SetValue(value)
    elif how == "settext":
        b = ctypes.create_unicode_buffer(value)
        hd_msg(h, WM_SETTEXT, 0, ctypes.addressof(b))
    elif how == "char":
        for c in value:
            hd_msg(h, WM_CHAR, ord(c), 1)
    elif how == "keys":
        for c in value:
            vk = u32.VkKeyScanW(c)
            if vk == -1:
                hd_msg(h, WM_CHAR, ord(c), 1)
            else:
                hd_key(h, vk & 0xFF, c)
    time.sleep(0.4)


HD_METHODS = [("keys", "Gửi phím vào cửa sổ (WM_KEYDOWN + WM_CHAR + WM_KEYUP)"), ("char", "Gửi ký tự (WM_CHAR)"),
              ("settext", "Đặt chữ (WM_SETTEXT)"), ("uia", "UI Automation ValuePattern.SetValue")]


def probe_inside(out):
    """Chạy TRÊN desktop ẩn (tiến trình con do probe_hidden_desktop tạo)."""
    out = Path(out)
    log = open(out / "nhat-ky.txt", "a", encoding="utf-8", buffering=1)
    sys.stdout = sys.stderr = log
    ctypes, W, u32, k32, g32 = _w32()
    rows, rep = [], {"kit": KIT_VERSION, "batDau": now_iso(), "ketQua": []}

    def rec(st, name, detail=""):
        rows.append("%s %s%s" % ({"ok": "[ OK ]", "warn": "[ !! ]", "fail": "[LỖI]", "info": "[ -- ]"}[st], name, (" – " + detail) if detail else ""))
        rep["ketQua"].append({"trangThai": st, "muc": name, "chiTiet": detail})
        print(rows[-1])
        (out / "bao-cao.txt").write_text("\n".join(rows) + "\n", "utf-8")
        (out / "bao-cao.json").write_text(json.dumps(rep, ensure_ascii=False, indent=1), "utf-8")

    def shot(hwnd, name, what):
        try:
            ok, black = pw_shot(hwnd, out / name)
            rec("ok" if ok and not black else "fail", "Chụp ảnh " + what + " (PrintWindow)",
                name + (" – ảnh toàn đen" if black else "") + ("" if ok else " – PrintWindow báo lỗi"))
            return ok and not black
        except Exception as e:
            rec("fail", "Chụp ảnh " + what + " (PrintWindow)", str(e))
            return False

    es = Edusoft()
    try:
        me = desk_name(u32.GetThreadDesktop(k32.GetCurrentThreadId()))
        inp = desk_name(u32.OpenInputDesktop(0, False, 0x0001))
        rec("ok" if me.lower() == HD_NAME.lower() else "fail", "Chạy trên desktop ẩn",
            "desktop của bộ test: %s, desktop đang hiện trên màn hình: %s" % (me or "?", inp or "không đọc được"))
        try:
            adm = bool(ctypes.windll.shell32.IsUserAnAdmin())
        except Exception:
            adm = False
        rec("ok" if adm else "warn", "Quyền admin", "có" if adm else "không – Edusoft cần quyền admin, hãy chạy qua chay-test.bat")
        t = time.time()
        es.launch()
        (out / "edusoft-pid.txt").write_text(str(es.pid() or ""), "utf-8")
        es.wait_login(120)
        rec("ok", "Mở Edusoft tới khung đăng nhập", "%s – %.0f giây" % (es.exe, time.time() - t))
        shot(es.login.handle, "1-dang-nhap.png", "khung đăng nhập")
        try:
            from PIL import ImageGrab
            r = es.login.rectangle()
            g = ImageGrab.grab(bbox=(r.left, r.top, r.right, r.bottom), all_screens=True)
            g.save(out / "1-dang-nhap-imagegrab.png")
            rec("info", "Chụp kiểu cũ (ImageGrab, để so sánh)",
                "ảnh toàn đen" if all(mx <= 12 for _, mx in g.getextrema()) else "có hình")
        except Exception as e:
            rec("info", "Chụp kiểu cũ (ImageGrab, để so sánh)", "lỗi: %s" % e)
        es.dump_ui(out / "ui-dang-nhap.txt")
        u, p = es.login_fields()
        hu, hp = el_hwnd(u), el_hwnd(p)
        rec("ok" if hu and hp else "warn", "Ô đăng nhập có cửa sổ Win32 riêng",
            "ô tên: %s, ô mật khẩu: %s" % (hex(hu) if hu else "không", hex(hp) if hp else "không"))
        try:
            u.set_focus()
            time.sleep(0.3)
            rec("ok" if u.has_keyboard_focus() else "warn", "Đưa con trỏ vào ô bằng UI Automation",
                "ô Tên đăng nhập đang có con trỏ" if u.has_keyboard_focus() else "ô chưa nhận con trỏ")
        except Exception as e:
            rec("warn", "Đưa con trỏ vào ô bằng UI Automation", str(e))
        acc = CFG["account"]
        good = []
        for how, label in HD_METHODS:
            if how != "uia" and not hu:
                rec("fail", "Gõ: " + label, "ô không có cửa sổ Win32")
                continue
            try:
                hd_clear(u, hu)
                before = (es.field_value(u) or "").strip()
                hd_fill(how, u, hu, acc)
                got = (es.field_value(u) or "").strip()
                okk = got == acc
                if okk:
                    good.append(how)
                rec("ok" if okk else "fail", "Gõ: " + label,
                    "đọc lại \"%s\"%s" % (got, "" if not before else " (xóa trước chưa sạch: \"%s\")" % before))
            except Exception as e:
                rec("fail", "Gõ: " + label, str(e))
        pw = None
        if keyring:
            try:
                pw = keyring.get_password("AQ-Autotest:edusoft", acc)
            except Exception:
                pw = None
        if not good:
            rec("fail", "Đăng nhập", "bỏ qua – không cách gõ nào điền được ô Tên đăng nhập")
        elif not pw:
            rec("warn", "Đăng nhập", "bỏ qua – chưa lưu mật khẩu Edusoft; chạy chay-test.bat một lần (nhập mật khẩu) rồi thử lại")
        else:
            how = good[0]
            hd_clear(u, hu)
            hd_fill(how, u, hu, acc)
            hd_clear(p, hp)
            hd_fill(how, p, hp, pw)
            rec("info", "Điền tài khoản %s + mật khẩu đã lưu" % acc, "bằng cách: " + dict(HD_METHODS)[how])
            btn = es.login_button()
            hb = el_hwnd(btn) if btn is not None else None

            def enter():
                hd_key(hp, 0x0D, "\r")

            def invoke():
                threading.Thread(target=lambda: btn.invoke(), daemon=True).start()

            def lclick():
                rc = W.RECT()
                u32.GetClientRect(hb, ctypes.byref(rc))
                xy = ((rc.bottom // 2) << 16) | (rc.right // 2)
                u32.PostMessageW(hb, WM_LBUTTONDOWN, 1, xy)
                time.sleep(0.05)
                u32.PostMessageW(hb, WM_LBUTTONUP, 0, xy)

            res, used = None, ""
            for label, fn, can in (("phím Enter gửi vào ô Mật khẩu", enter, bool(hp)),
                                   ("UI Automation Invoke nút Đăng nhập", invoke, btn is not None),
                                   ("gửi cú bấm chuột vào nút (WM_LBUTTONDOWN/UP)", lclick, bool(hb))):
                if not can:
                    continue
                try:
                    fn()
                except Exception as e:
                    rec("warn", "Bấm Đăng nhập: " + label, str(e))
                    continue
                res = es.login_reacted(8)
                rec("ok" if res else "warn", "Bấm Đăng nhập: " + label, res or "Edusoft không phản hồi")
                if res:
                    used = label
                    break
            if res == "có thông báo":
                ds = es.dialogs_other()
                txt = ""
                try:
                    txt = es.dialog_text(ds[0])[:200]
                    shot(ds[0].handle, "2-thong-bao.png", "thông báo")
                except Exception:
                    pass
                rec("fail", "Vào màn hình chính", "Edusoft báo: " + (txt or "?"))
            elif res:
                if es.wait_main(90):
                    rec("ok", "Vào màn hình chính", "%s (bấm bằng %s)" % (es.version or es.main.window_text(), used))
                    shot(es.main.handle, "3-man-hinh-chinh.png", "màn hình chính")
                    es.dump_ui(out / "ui-man-hinh-chinh.txt")
                    tab = None
                    for el in es.main.descendants(control_type="TabItem"):
                        try:
                            if norm(el.window_text()) == "sinh viên":
                                tab = el
                                break
                        except Exception:
                            continue
                    if tab is None:
                        rec("warn", "Chọn tab ribbon \"Sinh viên\"", "không thấy tab")
                    else:
                        try:
                            try:
                                tab.select()
                            except Exception:
                                tab.invoke()
                            time.sleep(2)
                            sel = False
                            try:
                                sel = bool(tab.is_selected())
                            except Exception:
                                pass
                            rec("ok" if sel else "warn", "Chọn tab ribbon \"Sinh viên\" (UI Automation)", "đã chọn" if sel else "chưa thấy đổi tab")
                            shot(es.main.handle, "4-tab-sinh-vien.png", "sau khi chọn tab")
                        except Exception as e:
                            rec("fail", "Chọn tab ribbon \"Sinh viên\" (UI Automation)", str(e))
                else:
                    rec("fail", "Vào màn hình chính", "không thấy màn hình chính sau 90 giây")
    except Exception as e:
        rec("fail", "Dừng giữa chừng", "%s: %s" % (type(e).__name__, e))
        traceback.print_exc()
        try:
            es.dump_ui(out / "ui-loi.txt")
        except Exception:
            pass
    finally:
        es.kill()
        rep["ketThuc"] = now_iso()
        (out / "bao-cao.json").write_text(json.dumps(rep, ensure_ascii=False, indent=1), "utf-8")
        sys.stdout, sys.stderr = sys.__stdout__, sys.__stderr__
        log.close()


def edusoft_running():
    try:
        import subprocess
        o = subprocess.run(["tasklist", "/FI", "IMAGENAME eq " + Path(CFG.get("exe") or "Edusoft.NET.exe").name, "/NH"],
                           capture_output=True, text=True, timeout=15).stdout
        return Path(CFG.get("exe") or "Edusoft.NET.exe").name.lower() in o.lower()
    except Exception:
        return False


def probe_hidden_desktop():
    """chay-test.bat --thu-desktop-an: tạo desktop ẩn, chạy phần thử (probe_inside) trên đó, in báo cáo, gói .zip vào Tải về."""
    import subprocess, zipfile
    ctypes, W, u32, k32, g32 = _w32()
    print("=== Thử chạy Edusoft trên desktop ẩn \"%s\" – bộ test %s ===" % (HD_NAME, KIT_VERSION))
    print("Edusoft sẽ chạy trên một màn hình riêng không hiện ra; bạn vẫn dùng máy bình thường trong lúc thử (~2–4 phút).")
    print("Chỉ mở Edusoft, đăng nhập và chọn tab Sinh viên – không thêm/sửa/xóa dữ liệu.")
    while edusoft_running():
        input("Edusoft đang mở trên máy (bản nào cũng tính). Hãy đóng Edusoft rồi nhấn Enter để tiếp tục (Ctrl+C để thôi)… ")
    out = BASE / "results" / ("desktop-an-%s" % time.strftime("%y%m%d-%H%M%S"))
    out.mkdir(parents=True, exist_ok=True)
    hdesk = u32.CreateDesktopW(HD_NAME, None, None, 0, 0x10000000, None)      # GENERIC_ALL
    if not hdesk:
        print("[LỖI] Không tạo được desktop ẩn (mã lỗi Windows %d)." % k32.GetLastError())
        return

    class SI(ctypes.Structure):
        _fields_ = [("cb", W.DWORD), ("lpReserved", W.LPWSTR), ("lpDesktop", W.LPWSTR), ("lpTitle", W.LPWSTR),
                    ("dwX", W.DWORD), ("dwY", W.DWORD), ("dwXSize", W.DWORD), ("dwYSize", W.DWORD),
                    ("dwXCountChars", W.DWORD), ("dwYCountChars", W.DWORD), ("dwFillAttribute", W.DWORD),
                    ("dwFlags", W.DWORD), ("wShowWindow", W.WORD), ("cbReserved2", W.WORD),
                    ("lpReserved2", ctypes.c_void_p), ("hStdInput", W.HANDLE), ("hStdOutput", W.HANDLE), ("hStdError", W.HANDLE)]

    class PI(ctypes.Structure):
        _fields_ = [("hProcess", W.HANDLE), ("hThread", W.HANDLE), ("dwProcessId", W.DWORD), ("dwThreadId", W.DWORD)]

    si, pi = SI(), PI()
    si.cb = ctypes.sizeof(si)
    si.lpDesktop = "WinSta0\\" + HD_NAME
    cmd = subprocess.list2cmdline([sys.executable, str(Path(__file__).resolve()), "--thu-desktop-an", "--ben-trong", str(out)])
    os.environ["AQ_UPDATED"] = "1"
    k32.CreateProcessW.argtypes = [W.LPCWSTR, W.LPWSTR, ctypes.c_void_p, ctypes.c_void_p, W.BOOL, W.DWORD,
                                   ctypes.c_void_p, W.LPCWSTR, ctypes.POINTER(SI), ctypes.POINTER(PI)]
    if not k32.CreateProcessW(None, ctypes.create_unicode_buffer(cmd), None, None, False, 0x08000000,   # CREATE_NO_WINDOW
                              None, str(BASE), ctypes.byref(si), ctypes.byref(pi)):
        print("[LỖI] Không chạy được bộ test trên desktop ẩn (mã lỗi Windows %d)." % k32.GetLastError())
        u32.CloseDesktop(hdesk)
        return
    seen, t0, limit = 0, time.time(), 8 * 60
    rep_f = out / "bao-cao.txt"
    while True:
        done = k32.WaitForSingleObject(pi.hProcess, 1000) == 0
        try:
            lines = rep_f.read_text("utf-8").splitlines() if rep_f.exists() else []
        except Exception:
            lines = []
        for ln in lines[seen:]:
            print(ln)
        seen = len(lines)
        if done:
            break
        if time.time() - t0 > limit:
            print("[LỖI] Quá %d phút chưa xong – dừng phần thử." % (limit // 60))
            k32.TerminateProcess(pi.hProcess, 1)
            try:
                pid = (out / "edusoft-pid.txt").read_text("utf-8").strip()
                if pid:
                    subprocess.run(["taskkill", "/PID", pid, "/T", "/F"], capture_output=True, timeout=20)
            except Exception:
                pass
            break
    k32.CloseHandle(pi.hThread)
    k32.CloseHandle(pi.hProcess)
    time.sleep(1)
    u32.CloseDesktop(hdesk)
    ds = [d for d in update_dirs() if d != BASE]
    zp = (ds[-1] if ds else BASE / "results") / ("AQ-desktop-an-%s.zip" % time.strftime("%y%m%d-%H%M%S"))
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for f in out.rglob("*"):
            if f.is_file():
                z.write(f, out.name + "/" + f.relative_to(out).as_posix())
    print()
    print("Đã xong. File kết quả:", zp)
    print("Gửi file .zip này cho Claude (có ảnh chụp và cây giao diện, không có mật khẩu) để quyết định chuyển bộ test sang desktop ẩn.")
    try:
        subprocess.Popen(["explorer", "/select,", str(zp)])
    except Exception:
        pass


def main():
    args = [a for a in sys.argv[1:]]
    upd_file = None
    if "--file" in args:                       # Agent đưa đúng file lệnh vừa nhận
        k = args.index("--file")
        upd_file = args[k + 1] if k + 1 < len(args) else None
        del args[k:k + 2]
    if os.environ.get("AQ_UPDATED") != "1":
        try:
            if apply_update(upd_file):
                import subprocess
                env = dict(os.environ, AQ_UPDATED="1")
                sys.exit(subprocess.call([sys.executable, str(Path(__file__).resolve())] + args, env=env))
        except SystemExit:
            raise
        except Exception as e:
            print("(Không áp dụng được bản cập nhật: %s)" % e)
    print("AQ Autotest – bộ test phiên bản", KIT_VERSION)
    if "--dump" in args:
        dump()
        return
    if "--quen-mat-khau" in args:
        forget()
        ask_password("edusoft", CFG["account"], reask=True)
        input("Nhấn Enter để đóng…")
        return
    if "--chan-doan" in args:
        diagnose()
        return
    if "--thu-desktop-an" in args:
        if "--ben-trong" in args:
            probe_inside(args[args.index("--ben-trong") + 1])
        else:
            probe_hidden_desktop()
            input("Nhấn Enter để đóng…")
        return
    try:
        unregister_claude_bridge()
    except Exception:
        pass
    if "--cap-nhat" in args:
        return
    try:                                        # báo cho Agent: đang có lượt test chạy (lệnh mới sẽ xếp hàng)
        import ctypes
        _run_mutex = ctypes.windll.kernel32.CreateMutexW(None, False, "AQAutotestRunMutex")  # noqa: F841 – giữ tới khi thoát
    except Exception:
        pass
    want = set()
    for a in args:
        if a.lower().startswith("aqautotest:"):          # chạy từ nút trên AQ Autotest Console
            rest = re.sub(r"^aqautotest:/*", "", a, flags=re.I).strip("/")
            parts = [x for x in rest.split("/") if x]
            want |= {x.upper() for x in parts[1:]} if parts and parts[0].lower() == "run" else set()
        elif not a.startswith("-"):
            want.add(a.upper())
    files = sorted((BASE / "scenarios").glob("*.json"))
    scs = [json.loads(p.read_text("utf-8")) for p in files]
    scs = [s for s in scs if not want or s["code"].upper() in want]
    if not scs:
        print("Không có kịch bản nào để chạy.")
        return
    print("AQ Autotest – %d kịch bản · %s" % (len(scs), CFG["exe"]))
    pw = ask_password("edusoft", CFG["account"])
    try:                                    # thu nhỏ cửa sổ đen để không che Edusoft khi script thao tác
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
    except Exception:
        pass
    summary = []
    t0 = time.time()

    def worker():
        es = Edusoft()
        login_sc = [s for s in scs if s["code"].upper() == "CHUNG-001"]
        others = [s for s in scs if s["code"].upper() != "CHUNG-001"]
        logged = False
        try:
            if login_sc:
                st, logged = run_login_test(login_sc[0], es, CFG["account"], pw)
                summary.append(("CHUNG-001", st))
            elif others:
                es.start_and_login(CFG["account"], pw)
                logged = True
        except Exception as e:
            traceback.print_exc()
            summary.append(("CHUNG-001", "error: %s" % e))
        for sc in others:
            if not logged:
                summary.append((sc["code"], "bỏ qua – chưa đăng nhập được"))
                continue
            try:
                summary.append((sc["code"], Run(sc, es).execute()))
            except Exception as e:
                traceback.print_exc()
                summary.append((sc["code"], "error: %s" % e))
        if others and logged and CFG.get("closeAfter", True):
            es.kill()
        CAP.show("Xong %d kịch bản" % len(summary), " · ".join("%s %s" % x for x in summary)[:180])
        time.sleep(4)

    CAP.start(worker)
    print("\nKẾT QUẢ:")
    for c, s in summary:
        print("  %-10s %s" % (c, s))
    print("\nThư mục kết quả:", BASE / "results")
    zp = None
    try:
        zp = pack_results(t0)
    except Exception as e:
        print("(Không gói được file kết quả: %s)" % e)
    if zp:
        print("File kết quả:", zp)
        print("Console chưa nối thẳng máy này? Vào AQ Autotest Console → Máy chạy thử → \"Nhập kết quả…\" và chọn file trên.")
    else:
        print("Vào AQ Autotest Console → Máy chạy thử → \"Nhập kết quả…\" và chọn thư mục results.")
    if CFG.get("openResults", True):
        try:
            if zp:
                import subprocess
                subprocess.Popen(["explorer", "/select,", str(zp)])
            else:
                os.startfile(str(BASE / "results"))
        except Exception:
            pass
    input("Nhấn Enter để đóng…")


if __name__ == "__main__":
    main()
