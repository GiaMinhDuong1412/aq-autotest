# -*- coding: utf-8 -*-
"""
AQ Autotest Agent – chạy nền trên máy chạy test (khởi động cùng Windows, quyền admin, do cai-dat.bat cài).
Nhận lệnh từ AQ Autotest Console qua file trong thư mục Tải về (Downloads) hoặc thư mục bộ test:
  - aq-autotest-update-run*.json (nút "Chạy test đăng nhập") → cập nhật bộ test lên bản mới nhất RỒI chạy test
  - aq-autotest-update*.json      (bản cập nhật không kèm lệnh chạy) → chỉ cập nhật
  - aq-autotest-run*.json         (lệnh chạy kiểu cũ)                → chỉ chạy
Mỗi file lệnh được nhận ngay (chuyển vào lenh-da-xu-ly/, tên kèm thời gian) rồi xử lý lần lượt: mỗi lần bấm Chạy
là một lượt chạy; đang có lượt chạy thì lệnh mới xếp hàng.
Nhật ký: agent.log trong thư mục bộ test.
"""
import os, sys, time, json, subprocess, datetime, ctypes
from pathlib import Path

BASE = Path(__file__).resolve().parent
LOG = BASE / "agent.log"
CREATE_NEW_CONSOLE = 0x00000010
MAX_AGE = 30 * 60            # bỏ qua lệnh cũ hơn 30 phút


def log(msg):
    try:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S  ") + msg + "\n")
    except Exception:
        pass


def single_instance(wait=0):
    end = time.time() + wait
    while True:
        h = ctypes.windll.kernel32.CreateMutexW(None, False, "AQAutotestAgentMutex")
        if ctypes.windll.kernel32.GetLastError() != 183:
            return h
        ctypes.windll.kernel32.CloseHandle(h)
        if time.time() > end:
            return None
        time.sleep(1)


def watch_dirs():
    ds = [BASE, Path(os.path.expanduser("~")) / "Downloads"]
    try:
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders") as k:
            ds.append(Path(os.path.expandvars(winreg.QueryValueEx(k, "{374DE290-123F-4565-9164-39C4925E467B}")[0])))
    except Exception:
        pass
    out = []
    for d in ds:
        if d not in out and d.is_dir():
            out.append(d)
    return out


def python_exe():
    exe = sys.executable
    if exe.lower().endswith("pythonw.exe"):
        c = exe[:-len("pythonw.exe")] + "python.exe"
        if os.path.exists(c):
            return c
    return exe


RUNNING = {"p": None}
DONE = BASE / "lenh-da-xu-ly"          # file lệnh đã nhận, tên kèm thời gian nên không bao giờ trùng
WAIT_F = BASE / "lenh-cho.json"        # hàng chờ, giữ lại khi Agent tự khởi động lại sau cập nhật
PENDING = []                            # file lệnh đã nhận, chờ tới lượt (mỗi lần bấm Chạy là một lượt)
BAD = {}                                # file chưa đọc được (đang ghi dở) → số lần thử


def archive(f, tag):
    """Chuyển file lệnh vào lenh-da-xu-ly/ với tên không trùng. Trước đây đổi sang tên cố định
    (*.da-ap-dung.json / *.da-xu-ly.json): lần sau trùng tên → đổi tên lỗi → lệnh chạy bị bỏ, các lần sau kẹt."""
    import shutil
    DONE.mkdir(exist_ok=True)
    dest = DONE / ("%s-%s-%s" % (datetime.datetime.now().strftime("%Y%m%d-%H%M%S-%f"), tag, f.name))
    shutil.move(str(f), str(dest))      # Tải về và thư mục bộ test có thể khác ổ đĩa
    try:
        old = sorted(DONE.glob("*.json"), key=lambda x: x.stat().st_mtime)
        for x in old[:-40]:
            x.unlink()
    except Exception:
        pass
    return dest


def run_busy():
    """Đang có lượt test chạy: do Agent này mở, hoặc aqrun.py đang giữ mutex (VD mở từ chay-test.bat)."""
    p = RUNNING["p"]
    if p is not None and p.poll() is None:
        return True
    try:
        h = ctypes.windll.kernel32.OpenMutexW(0x00100000, False, "AQAutotestRunMutex")
        if h:
            ctypes.windll.kernel32.CloseHandle(h)
            return True
    except Exception:
        pass
    return False


def start_run(codes, why=""):
    codes = [str(c).upper() for c in (codes or []) if str(c).replace("-", "").isalnum()]
    log("Chạy test %s %s" % (", ".join(codes) or "tất cả", why))
    env = dict(os.environ, AQ_UPDATED="1")      # đã cập nhật ở bước trước – aqrun không tự tìm file lệnh (tránh "ăn" lệnh mới)
    RUNNING["p"] = subprocess.Popen([python_exe(), str(BASE / "aqrun.py")] + codes, cwd=str(BASE), creationflags=CREATE_NEW_CONSOLE, env=env)


def process(g):
    """Xử lý một file lệnh đã nhận: cập nhật bộ test theo đúng file đó rồi chạy test đi kèm."""
    try:
        data = json.loads(g.read_text("utf-8"))
    except Exception as e:
        log("Không đọc được %s: %s" % (g.name, e))
        return
    fmt = data.get("format", "")
    if fmt == "aq-autotest-update/1":
        log("Cập nhật bộ test %s từ %s" % (data.get("kitVersion", "?"), g.name))
        r = subprocess.call([python_exe(), str(BASE / "aqrun.py"), "--cap-nhat", "--file", str(g)], cwd=str(BASE), creationflags=0x08000000)
        log("Cập nhật xong (mã %s)" % r)
        run = data.get("run") or {}
        if run:
            start_run(run.get("codes"), "(yêu cầu lúc %s, bộ test %s)" % (run.get("requestedAt", "?"), data.get("kitVersion", "?")))
    elif fmt == "aq-autotest-run-request/1":
        start_run(data.get("codes"), "(yêu cầu lúc %s)" % data.get("requestedAt", "?"))


def receive(f):
    """File lệnh mới trong thư mục bộ test / Tải về: nhận ngay (chuyển đi) rồi đưa vào hàng chờ."""
    try:
        age = time.time() - f.stat().st_mtime
        data = json.loads(f.read_text("utf-8"))
    except Exception:
        BAD[str(f)] = BAD.get(str(f), 0) + 1          # có thể đang ghi dở – thử lại vòng sau
        if BAD[str(f)] >= 15:
            archive(f, "hong")
            log("Bỏ file lệnh hỏng %s" % f.name)
        return
    BAD.pop(str(f), None)
    if data.get("format") not in ("aq-autotest-update/1", "aq-autotest-run-request/1"):
        return
    if age > MAX_AGE:
        archive(f, "qua-han")
        log("Bỏ lệnh cũ hơn 30 phút: %s" % f.name)
        return
    g = archive(f, "nhan")
    PENDING.append(g)
    log("Nhận lệnh %s%s" % (f.name, " – đang có lượt test chạy, xếp hàng (%d)" % len(PENDING) if run_busy() else ""))


def cleanup_old():
    """Dọn file đánh dấu kiểu cũ (*.da-ap-dung.json, *.da-xu-ly.json) để không còn gây trùng tên."""
    for d in watch_dirs():
        for f in list(d.glob("aq-autotest-*.da-*.json")):
            try:
                archive(f, "cu")
            except Exception:
                pass


def main():
    if single_instance(wait=15 if "--restart" in sys.argv else 0) is None:
        return
    me = Path(__file__).resolve()
    import hashlib
    digest = lambda: hashlib.md5(me.read_bytes()).hexdigest()
    mtime, mine = me.stat().st_mtime, digest()
    log("Agent bắt đầu (%s) – theo dõi: %s" % (python_exe(), ", ".join(str(d) for d in watch_dirs())))
    cleanup_old()
    try:
        PENDING.extend(Path(x) for x in json.loads(WAIT_F.read_text("utf-8")) if Path(x).exists())
        WAIT_F.unlink()
    except Exception:
        pass
    while True:
        try:
            for d in watch_dirs():
                for pat in ("aq-autotest-update*.json", "aq-autotest-run*.json"):
                    for f in sorted(d.glob(pat), key=lambda x: x.stat().st_mtime):
                        if ".da-" not in f.name:
                            receive(f)
            if PENDING and not run_busy():
                process(PENDING.pop(0))
            if me.stat().st_mtime != mtime and digest() == mine:   # chép lại y nguyên – không cần khởi động lại
                mtime = me.stat().st_mtime
            elif me.stat().st_mtime != mtime:       # agent vừa được cập nhật → khởi động lại bản mới
                log("Agent có bản mới – khởi động lại")
                if PENDING:
                    WAIT_F.write_text(json.dumps([str(x) for x in PENDING]), "utf-8")
                subprocess.Popen([sys.executable, str(me), "--restart"], cwd=str(BASE))
                return
        except Exception as e:
            log("Lỗi: %s" % e)
        time.sleep(2)


if __name__ == "__main__":
    main()
