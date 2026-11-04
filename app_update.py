# -*- coding: utf-8 -*-
"""Phần server riêng cho app AQ Auto Test (desktop/, Electron). server.py nạp module này khi có biến môi trường AQ_APP_HOME
(thư mục dữ liệu của app). Cập nhật phiên bản do app Electron lo (electron-updater, repo public aq-autotest-releases) –
server chỉ báo số phiên bản cho trang. Chỉ thư viện chuẩn.
"""
import os
import threading
from pathlib import Path

HOME = Path(os.environ.get("AQ_APP_HOME") or ".").resolve()
VERSION = os.environ.get("AQ_APP_VERSION") or "dev"


def info():
    return {"app": True, "version": VERSION}


def quit_app():
    threading.Timer(0.5, lambda: os._exit(0)).start()
    return {"ok": True}
