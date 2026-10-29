# -*- coding: utf-8 -*-
"""
AQ Autotest Agent – chạy nền trên máy chạy test (khởi động cùng Windows, quyền admin, do cai-dat.bat cài).
Nhận lệnh từ AQ Autotest Console qua file trong thư mục Tải về (Downloads) hoặc thư mục bộ test:
  - aq-autotest-update-run*.json (nút "Chạy test đăng nhập") → cập nhật bộ test lên bản mới nhất RỒI chạy test
  - aq-autotest-update*.json      (bản cập nhật không kèm lệnh chạy) → chỉ cập nhật
  - aq-autotest-run*.json         (lệnh chạy kiểu cũ)                → chỉ chạy
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
SEEN = set()


def start_run(codes, why=""):
    p = RUNNING["p"]
    if p is not None and p.poll() is None:
        log("Bỏ qua lệnh chạy – đang có lượt test chạy")
        return
    codes = [str(c).upper() for c in (codes or []) if str(c).replace("-", "").isalnum()]
    log("Chạy test %s %s" % (", ".join(codes) or "tất cả", why))
    RUNNING["p"] = subprocess.Popen([python_exe(), str(BASE / "aqrun.py")] + codes, cwd=str(BASE), creationflags=CREATE_NEW_CONSOLE)


def run_after_update(applied, data):
    """File cập nhật có kèm lệnh chạy: chạy test rồi đánh dấu đã xử lý (để không chạy lại)."""
    run = data.get("run") or {}
    if not run:
        return
    try:
        applied.rename(applied.with_name(applied.name.replace(".da-ap-dung.json", ".da-xu-ly.json")))
    except Exception:
        return
    start_run(run.get("codes"), "(yêu cầu lúc %s, bộ test %s)" % (run.get("requestedAt", "?"), data.get("kitVersion", "?")))


def pending_after_restart():
    """Agent vừa được thay bản mới trong lúc cập nhật: chạy nốt lệnh chạy đi kèm bản cập nhật đó."""
    for d in watch_dirs():
        for f in d.glob("aq-autotest-update*.da-ap-dung.json"):
            try:
                if time.time() - f.stat().st_mtime > 300:
                    continue
                data = json.loads(f.read_text("utf-8"))
            except Exception:
                continue
            run_after_update(f, data)


def handle(f):
    try:
        if time.time() - f.stat().st_mtime > MAX_AGE:
            return
        data = json.loads(f.read_text("utf-8"))
    except Exception:
        return
    fmt = data.get("format", "")
    if fmt == "aq-autotest-update/1":
        log("Nhận bản cập nhật %s từ %s" % (data.get("kitVersion", "?"), f))
        r = subprocess.call([python_exe(), str(BASE / "aqrun.py"), "--cap-nhat"], cwd=str(BASE), creationflags=0x08000000)
        log("Cập nhật xong (mã %s)" % r)
        applied = f.with_name(f.stem + ".da-ap-dung.json")
        if applied.exists():
            run_after_update(applied, data)
        elif data.get("run") and f.exists():       # không áp dụng được (VD đã áp dụng trước đó) – vẫn chạy test
            try:
                f.rename(f.with_name(f.stem + ".da-xu-ly.json"))
            except Exception:
                return
            start_run((data.get("run") or {}).get("codes"), "(không cần cập nhật)")
        return
    if fmt != "aq-autotest-run-request/1":
        return
    try:
        f.rename(f.with_name(f.stem + ".da-xu-ly.json"))
    except Exception:
        return
    start_run(data.get("codes"), "(yêu cầu lúc %s)" % data.get("requestedAt", "?"))


def main():
    if single_instance(wait=15 if "--restart" in sys.argv else 0) is None:
        return
    me = Path(__file__).resolve()
    import hashlib
    digest = lambda: hashlib.md5(me.read_bytes()).hexdigest()
    mtime, mine = me.stat().st_mtime, digest()
    log("Agent bắt đầu (%s) – theo dõi: %s" % (python_exe(), ", ".join(str(d) for d in watch_dirs())))
    if "--restart" in sys.argv:
        pending_after_restart()
    while True:
        try:
            for d in watch_dirs():
                for pat in ("aq-autotest-update*.json", "aq-autotest-run*.json"):
                    for f in sorted(d.glob(pat), key=lambda x: x.stat().st_mtime):
                        if ".da-" in f.name:
                            continue
                        key = (str(f), f.stat().st_mtime)
                        if key in SEEN:
                            continue
                        SEEN.add(key)
                        handle(f)
            if me.stat().st_mtime != mtime and digest() == mine:   # chép lại y nguyên – không cần khởi động lại
                mtime = me.stat().st_mtime
            elif me.stat().st_mtime != mtime:       # agent vừa được cập nhật → khởi động lại bản mới
                log("Agent có bản mới – khởi động lại")
                subprocess.Popen([sys.executable, str(me), "--restart"], cwd=str(BASE))
                return
        except Exception as e:
            log("Lỗi: %s" % e)
        time.sleep(2)


if __name__ == "__main__":
    main()
