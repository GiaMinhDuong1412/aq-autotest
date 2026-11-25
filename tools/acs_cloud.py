#!/usr/bin/env python3
"""Đọc ACS (AQ Support Hub) từ phiên Claude Code trên cloud – CHỈ ĐỌC.

ACS đăng nhập bằng Microsoft (SSO) nên không dùng mật khẩu: Claude tạo link đăng nhập, người dùng đăng nhập trên
trình duyệt của mình rồi dán lại mã `code` (bắt trong F12 › Network › `callback`, hoặc Lịch sử Ctrl+H), Claude đổi mã
lấy phiên (cookie `kb_token`, sống ~5 giờ). Cookie lưu ở ~/.aq-acs/ (ngoài repo, mất khi máy cloud bị thu hồi).

    python tools/acs_cloud.py start [email]         # in link đăng nhập (dùng trong 10 phút)
    python tools/acs_cloud.py finish <code|url>     # đổi mã lấy phiên, in /auth/me
    python tools/acs_cloud.py me
    python tools/acs_cloud.py case <id>             # nội dung case dạng chữ: thông tin, KH, BA, Dev, test, lịch sử
    python tools/acs_cloud.py get </cs/...>         # JSON thô (chỉ GET, chỉ /cs/… và /auth/me)
    python tools/acs_cloud.py att <id> [thư mục]    # tải ảnh / file đính kèm /cs/att/<id>

Không có lệnh ghi (POST/PUT/PATCH/DELETE) – giữ nguyên như vậy (quy tắc dự án: Claude không ghi lên ACS).
Không in cookie / mã ra màn hình. Mạng: môi trường cloud phải cho phép host acs.aqtech.io.vn.
"""
import html
import http.cookiejar
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE = 'https://acs.aqtech.io.vn'
DIR = Path(os.environ.get('AQ_ACS_DIR') or Path.home() / '.aq-acs')
JAR = DIR / 'cookies.txt'
STATE = DIR / 'state.txt'
PATH_OK = re.compile(r'^/(auth/me|cs/)[A-Za-z0-9_\-./?=&%,@:+~]*$')


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def opener(follow=True):
    DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(DIR, 0o700)
    jar = http.cookiejar.MozillaCookieJar(str(JAR))
    if JAR.exists():
        jar.load(ignore_discard=True, ignore_expires=True)
    hs = [urllib.request.HTTPCookieProcessor(jar)]
    if not follow:
        hs.append(NoRedirect())
    op = urllib.request.build_opener(*hs)
    op.addheaders = [('Origin', BASE), ('User-Agent', 'aq-autotest-acs-cloud')]
    return op, jar


def save(jar):
    jar.save(ignore_discard=True, ignore_expires=True)
    os.chmod(JAR, 0o600)


def fetch(path, raw=False):
    if not PATH_OK.match(path):
        sys.exit('Chỉ đọc /auth/me hoặc /cs/…: %s' % path)
    op, jar = opener()
    try:
        with op.open(BASE + path, timeout=60) as r:
            data = r.read()
            ct = r.headers.get('Content-Type', '')
    except urllib.error.HTTPError as e:
        body = e.read()[:300].decode('utf-8', 'replace')
        if e.code == 401:
            sys.exit('ACS: chưa đăng nhập hoặc phiên hết hạn – chạy `start` rồi `finish`. (%s)' % body)
        sys.exit('ACS %s %s: %s' % (e.code, path, body))
    save(jar)
    if raw:
        return data, ct
    if 'json' not in ct:
        sys.exit('ACS trả về không phải JSON (đường dẫn không có?): %s' % path)
    return json.loads(data)


def start(hint=None):
    op, jar = opener(follow=False)
    for c in list(jar):
        if c.name == 'kb_sso':
            jar.clear(c.domain, c.path, c.name)
    try:
        op.open(BASE + '/auth/microsoft/login', timeout=30)
        sys.exit('Không nhận được link chuyển sang Microsoft')
    except urllib.error.HTTPError as e:
        loc = e.headers.get('Location')
        if e.code not in (301, 302, 303, 307) or not loc:
            sys.exit('ACS %s khi bắt đầu đăng nhập' % e.code)
    save(jar)
    st = urllib.parse.parse_qs(urllib.parse.urlparse(loc).query).get('state', [''])[0]
    STATE.write_text(st)
    if hint:
        loc += '&login_hint=' + urllib.parse.quote(hint)
    print(loc)


def finish(arg):
    arg = arg.strip()
    q = urllib.parse.parse_qs(urllib.parse.urlparse(arg).query) if '://' in arg or arg.startswith('/') or 'code=' in arg else {}
    if 'code=' in arg and not q:
        q = urllib.parse.parse_qs(arg.split('?', 1)[-1])
    code = (q.get('code') or [arg])[0]
    state = (q.get('state') or [STATE.read_text().strip() if STATE.exists() else ''])[0]
    if not state:
        sys.exit('Thiếu state – chạy `start` trước')
    op, jar = opener(follow=False)
    url = BASE + '/auth/microsoft/callback?' + urllib.parse.urlencode({'code': code, 'state': state})
    try:
        op.open(url, timeout=60)
    except urllib.error.HTTPError as e:
        loc = e.headers.get('Location') or ''
        save(jar)
        if 'loi_dang_nhap' in loc:
            sys.exit('ACS từ chối: %s – link / mã đã hết hạn hoặc không khớp, chạy lại `start`' % loc.split('=')[-1])
    STATE.unlink(missing_ok=True)
    me()


def me():
    d = fetch('/auth/me')
    print('Đã đăng nhập ACS: %s (%s, vai trò %s)' % (d.get('display_name'), d.get('username'), d.get('role')))


def text(s):
    s = re.sub(r'<img[^>]*src="([^"]+)"[^>]*>', r'[ẢNH \1]', s or '')
    s = re.sub(r'</p>|<br\s*/?>|</li>|</tr>|</h\d>', '\n', s)
    s = re.sub(r'<td[^>]*>', ' | ', s)
    s = html.unescape(re.sub(r'<[^>]+>', '', s))
    return re.sub(r'\n{3,}', '\n\n', s).strip()


def case(cid):
    d = fetch('/cs/cases/%s' % int(cid))
    v = d.get('values') or d
    print('# Case %s – %s' % (cid, v.get('title')))
    keys = ['school_code', 'school_name', 'module', 'case_type', 'status', 'state_reason', 'assignee_raw', 'analyst_raw',
            'tester_raw', 'test_state', 'reopen_count', 'due_date', 'received_at', 'contract_type', 'priority']
    for k in keys:
        if v.get(k) not in (None, ''):
            print('- %s: %s' % (k, v[k]))
    for k, t in (('customer_html', 'Khách hàng yêu cầu'), ('symptom_html', 'Hiện tượng / BA'), ('dev_comment', 'Dev / phân tích'),
                 ('chi_tiet_xl_html', 'Chi tiết xử lý'), ('aq_solution_html', 'Giải pháp AQ'), ('company_response_html', 'Trả lời KH'),
                 ('user_guide_html', 'Hướng dẫn')):
        if v.get(k):
            print('\n## %s\n%s' % (t, text(v[k])))
    try:
        cm = fetch('/cs/cases/%s/comments' % int(cid)).get('comments') or []
    except SystemExit:
        cm = []
    for c in cm:
        h = (c.get('edits') or [{}])[-1].get('html') or c.get('html')
        print('\n## Trao đổi (%s) %s – %s\n%s' % (c.get('kenh') or '', c.get('author'), (c.get('created_at') or '')[:16], text(h)))
    try:
        hs = fetch('/cs/cases/%s/history' % int(cid)).get('history') or []
    except SystemExit:
        hs = []
    if hs:
        print('\n## Lịch sử')
        for x in hs:
            ch = x.get('changes') or {}
            sm = {k: v for k, v in ch.items() if not k.endswith('_html') and k != 'dev_comment'}
            ex = [k for k in ch if k.endswith('_html') or k == 'dev_comment']
            print('- %s %s: %s%s' % ((x.get('changed_at') or '')[:16], x.get('changed_by'), json.dumps(sm, ensure_ascii=False)[:240],
                                    (' (+ sửa %s)' % ', '.join(ex)) if ex else ''))


def att(aid, out='.'):
    data, ct = fetch('/cs/att/%s' % int(aid), raw=True)
    ext = {'image/webp': 'webp', 'image/png': 'png', 'image/jpeg': 'jpg', 'image/gif': 'gif'}.get(ct.split(';')[0], 'bin')
    p = Path(out) / ('%s.%s' % (aid, ext))
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data)
    print(p)


def main():
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    cmd = a[0]
    if cmd == 'start':
        start(a[1] if len(a) > 1 else None)
    elif cmd == 'finish' and len(a) > 1:
        finish(a[1])
    elif cmd == 'me':
        me()
    elif cmd == 'case' and len(a) > 1:
        case(a[1])
    elif cmd == 'get' and len(a) > 1:
        print(json.dumps(fetch(a[1]), ensure_ascii=False, indent=1))
    elif cmd == 'att' and len(a) > 1:
        att(a[1], a[2] if len(a) > 2 else '.')
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main()
