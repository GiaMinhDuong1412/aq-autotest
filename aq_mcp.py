# -*- coding: utf-8 -*-
"""Cầu nối MCP (stdio) cho Claude Desktop → app AQ Auto Test đang chạy trên máy này.

Claude Desktop chạy:  python.exe aq_mcp.py --cau-hinh "%APPDATA%\\AQ Auto Test\\rieng\\mcp.json"
(app tự ghi mục "aq-auto-test" vào claude_desktop_config.json khi bấm "Kết nối Claude Desktop").
Mỗi dòng JSON-RPC từ Claude được chuyển nguyên vẹn tới server.py (POST api/mcp, token trong mcp.json – app tạo lại mỗi lần mở).
App chưa mở: initialize / tools/list trả từ mcp-tools.json, gọi công cụ thì báo "mở app". Chỉ thư viện chuẩn, không ghi gì ra stdout ngoài JSON-RPC.
"""
import json, os, sys, urllib.request, urllib.error
from pathlib import Path


def conn_file():
    a = sys.argv[1:]
    if "--cau-hinh" in a and a.index("--cau-hinh") + 1 < len(a):
        return Path(a[a.index("--cau-hinh") + 1])
    for base in (os.environ.get("APPDATA"), str(Path.home() / ".config")):
        if base and (Path(base) / "AQ Auto Test" / "rieng" / "mcp.json").exists():
            return Path(base) / "AQ Auto Test" / "rieng" / "mcp.json"
    return Path(__file__).resolve().parent / "local" / "mcp.json"


CF = conn_file()
NOT_RUNNING = "App AQ Auto Test chưa mở (hoặc vừa mở lại). Mở app AQ Auto Test trên máy này rồi thử lại."


def offline(msg):
    mid, method = msg.get("id"), msg.get("method")
    try:
        cache = json.loads((CF.parent / "mcp-tools.json").read_text("utf-8"))
    except Exception:
        cache = {"tools": [], "instructions": ""}
    if method == "initialize":
        p = msg.get("params") or {}
        return {"jsonrpc": "2.0", "id": mid, "result": {"protocolVersion": p.get("protocolVersion") or "2025-06-18",
                "capabilities": {"tools": {"listChanged": False}}, "serverInfo": {"name": "aq-auto-test", "title": "AQ Auto Test", "version": "offline"},
                "instructions": cache.get("instructions") or ""}}
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": mid, "result": {"tools": cache.get("tools") or []}}
    if method == "ping":
        return {"jsonrpc": "2.0", "id": mid, "result": {}}
    if method == "tools/call":
        return {"jsonrpc": "2.0", "id": mid, "result": {"content": [{"type": "text", "text": NOT_RUNNING}], "isError": True}}
    return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32000, "message": NOT_RUNNING}}


def forward(raw, msg):
    try:
        c = json.loads(CF.read_text("utf-8"))
    except Exception:
        return offline(msg) if msg.get("id") is not None else None
    req = urllib.request.Request(c["url"], data=raw, method="POST", headers={
        "Content-Type": "application/json", "X-AQ": "1", "Authorization": "Bearer " + c["token"]})
    proxy = urllib.request.build_opener(urllib.request.ProxyHandler({}))       # 127.0.0.1: không đi qua proxy hệ thống
    try:
        with proxy.open(req, timeout=180) as r:
            body = r.read()
        return json.loads(body.decode("utf-8")) if body.strip() else None
    except urllib.error.HTTPError as e:
        if msg.get("id") is None:
            return None
        if e.code in (401, 403):
            return offline(msg) if msg.get("method") in ("initialize", "tools/list", "ping") else \
                {"jsonrpc": "2.0", "id": msg.get("id"), "result": {"content": [{"type": "text", "text": NOT_RUNNING}], "isError": True}}
        return {"jsonrpc": "2.0", "id": msg.get("id"), "error": {"code": -32000, "message": "App trả lỗi HTTP %d" % e.code}}
    except (OSError, ValueError):
        return offline(msg) if msg.get("id") is not None else None


def main():
    inp = sys.stdin.buffer
    out = sys.stdout.buffer
    for line in inp:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line.decode("utf-8"))
        except ValueError:
            res = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Parse error"}}
        else:
            if isinstance(msg, list):
                res = [r for r in (forward(json.dumps(m).encode("utf-8"), m) for m in msg) if r]
                res = res or None
            else:
                res = forward(line, msg)
        if res is not None:
            out.write(json.dumps(res, ensure_ascii=False).encode("utf-8") + b"\n")
            out.flush()


if __name__ == "__main__":
    main()
