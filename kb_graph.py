# -*- coding: utf-8 -*-
"""Bản đồ nghiệp vụ dựng TỪ GHI CHÚ Obsidian trong kb/ (ghi chú là nguồn – sửa trong Obsidian là app thấy).

    python kb_graph.py [kb]                      in tóm tắt
    python kb_graph.py kb --nhung web/index.html nhúng bản đồ vào trang (<script type="application/json" id="kb-graph">)
    python kb_graph.py kb --kiem web/index.html  báo nếu bản nhúng khác ghi chú

Đọc:
  Du-lieu/<tên>.md  Properties: ten, tao_o "[[PH]]", can_co ["[[Dữ liệu]]"…], dung_o, tu_khoa (regex nhận ra dữ liệu trong lời KH / menu),
                    tu_khoa_ph (mã phân hệ menu được tính); thân: "**Tạo ở** [[PH]] – `menu`", mục "## Muốn có … phải có trước"
                    (- [[X|…]] – vì sao), "## Dùng ở" (- [[PH]] – dùng vào việc gì), "## Trên web".
  Phan-he/<mã>.md   Properties: ma, ten, test_tren.
server.py dùng build() cho api/kb/graph và công cụ MCP kb_*. Chỉ thư viện chuẩn.
"""
import json, os, re, sys
from pathlib import Path

CAT_PH = {'HTQL': 'QLHT', 'DMKT': 'DIEM', 'DGGD': 'KSDG'}   # mã phân hệ trong danh mục menu Edusoft → mã kb
LINK = re.compile(r'\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]')
_CACHE = {}


def _val(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in '"\'':
        v = v[1:-1]
        if v and '\\' in v:
            v = v.replace('\\"', '"').replace('\\\\', '\\')
    return v


def parse_note(text):
    """→ (properties, thân). Hỗ trợ phần YAML Obsidian dùng: `khoá: giá trị`, `khoá:` + dòng `  - mục`, `khoá: []`."""
    text = text.replace('\r\n', '\n').lstrip('﻿')
    props, body = {}, text
    if text.startswith('---\n'):
        end = text.find('\n---', 4)
        if end > 0:
            head, body = text[4:end], text[end + 4:].lstrip('\n')
            key = None
            for ln in head.split('\n'):
                if not ln.strip():
                    continue
                m = re.match(r'^\s+-\s*(.*)$', ln)
                if m and key:
                    if not isinstance(props.get(key), list):
                        props[key] = []
                    props[key].append(_val(m.group(1)))
                    continue
                m = re.match(r'^([A-Za-z0-9_\-]+)\s*:\s*(.*)$', ln)
                if m:
                    key, v = m.group(1), m.group(2).strip()
                    if v == '[]':
                        props[key] = []
                    elif v.startswith('[') and v.endswith(']'):
                        props[key] = [_val(x) for x in v[1:-1].split(',') if x.strip()]
                    else:
                        props[key] = _val(v) if v else []
    return props, body


def link_of(s):
    m = LINK.search(str(s or ''))
    return (m.group(1) if m else str(s or '')).strip()


def links(v):
    v = v if isinstance(v, list) else ([v] if v else [])
    return [link_of(x) for x in v if link_of(x)]


def section(body, head_re):
    m = re.search(r'^##\s+' + head_re + r'.*$', body, re.M)
    if not m:
        return ''
    rest = body[m.end():]
    n = re.search(r'^##\s', rest, re.M)
    return rest[:n.start()] if n else rest


def why_map(sec):
    out = {}
    for ln in sec.split('\n'):
        m = re.match(r'^\s*-\s*\[\[([^\]|#]+)[^\]]*\]\]\s*(?:[–\-:]\s*(.*))?$', ln)
        if m:
            out.setdefault(m.group(1).strip(), (m.group(2) or '').strip())
    return out


def _sig(kb):
    s = []
    for sub in ('Du-lieu', 'Phan-he', 'Truong', 'Dang-case', 'Luong-test', 'Case-truong', 'Quy-trinh', 'Web', 'Cach-test'):
        d = kb / sub
        if d.is_dir():
            for f in d.glob('*.md'):
                try:
                    s.append((f.name, f.stat().st_mtime_ns))
                except OSError:
                    pass
    return tuple(sorted(s))


def build(kb):
    kb = Path(kb)
    sig = _sig(kb)
    c = _CACHE.get(str(kb))
    if c and c[0] == sig:
        return c[1]
    mods, data = {}, {}
    for f in sorted((kb / 'Phan-he').glob('*.md')) if (kb / 'Phan-he').is_dir() else []:
        p, _ = parse_note(f.read_text('utf-8', errors='replace'))
        ma = str(p.get('ma') or f.stem)
        tt = p.get('test_tren') or []
        mods[ma] = [str(p.get('ten') or ma), tt if isinstance(tt, list) else [tt]]
    for f in sorted((kb / 'Du-lieu').glob('*.md')) if (kb / 'Du-lieu').is_dir() else []:
        p, body = parse_note(f.read_text('utf-8', errors='replace'))
        if p.get('loai') not in (None, 'du-lieu'):
            continue
        fn = f.stem
        src = link_of(p.get('tao_o'))
        m = re.search(r'\*\*Tạo ở\*\*\s*\[\[[^\]]+\]\]\s*[–\-]\s*`([^`]*)`', body)
        rw = why_map(section(body, r'Muốn có'))
        uw = why_map(section(body, r'Dùng ở'))
        use = [[k, v] for k, v in uw.items()]
        for x in links(p.get('dung_o')):
            if x not in uw:
                use.append([x, ''])
        web = section(body, r'Trên web').strip()
        kwph = p.get('tu_khoa_ph') or []
        data[fn] = {'t': str(p.get('ten') or fn), 'src': src, 'menu': m.group(1) if m else '', 'use': use,
                    'web': '' if web in ('—', '-') else web.split('\n')[0].strip(),
                    'req': [[r, rw.get(r, '')] for r in links(p.get('can_co'))],
                    'kw': str(p.get('tu_khoa') or ''), 'kwph': kwph if isinstance(kwph, list) else [kwph], 'lv': 0}
    schools, pats = {}, {}
    for f in sorted((kb / 'Truong').glob('*.md')) if (kb / 'Truong').is_dir() else []:
        p, _ = parse_note(f.read_text('utf-8', errors='replace'))
        ma = str(p.get('ma') or f.stem)
        pc = {}
        for it in (p.get('phan_cap') or []) if isinstance(p.get('phan_cap'), list) else []:
            k, _, v = str(it).partition(':')
            if k.strip():
                pc[k.strip().upper()] = v.strip()
        schools[ma] = {'ten': str(p.get('ten') or ''), 'phan_cap': pc, 'xac_nhan': p.get('trang_thai') == 'da-xac-nhan',
                       'web_that': str(p.get('netweb_that') or ''), 'web_test': str(p.get('web_test') or '')}
    for f in sorted((kb / 'Case-truong').glob('*.md')) if (kb / 'Case-truong').is_dir() else []:
        p, _ = parse_note(f.read_text('utf-8', errors='replace'))
        ma = str(p.get('ma') or f.stem)
        if ma in schools and p.get('loai') == 'case-truong':
            L2 = lambda v: [str(x) for x in v][:5] if isinstance(v, list) else []
            schools[ma]['mh'] = {'n': int(str(p.get('tong_case') or 0)) if str(p.get('tong_case') or '0').isdigit() else 0,
                                 'ph': L2(p.get('phan_he_nhieu')), 'dang': L2(p.get('dang_nhieu')), 'den': str(p.get('den_ngay') or '')}
    qts = {}
    for f in sorted((kb / 'Quy-trinh').glob('[0-9][0-9] *.md')) if (kb / 'Quy-trinh').is_dir() else []:
        p, _ = parse_note(f.read_text('utf-8', errors='replace'))
        qts[f.stem] = {'ten': str(p.get('ten') or f.stem), 'ph': links(p.get('phan_he'))[:3]}
    for f in sorted((kb / 'Dang-case').glob('*.md')) if (kb / 'Dang-case').is_dir() else []:
        p, _ = parse_note(f.read_text('utf-8', errors='replace'))
        pats[f.stem] = {'ten': str(p.get('ten') or f.stem), 'kh': str(p.get('dau_hieu_kh') or ''), 'ba': str(p.get('dau_hieu_ba') or ''),
                        'dev': str(p.get('dau_hieu_dev') or ''), 'ph': links(p.get('phan_he_hay_gap'))}
    flows = {}
    L = lambda v: [str(x) for x in v] if isinstance(v, list) else ([str(v)] if v else [])
    for f in sorted((kb / 'Luong-test').glob('*.md')) if (kb / 'Luong-test').is_dir() else []:
        p, _ = parse_note(f.read_text('utf-8', errors='replace'))
        if p.get('loai') != 'luong-test' or not p.get('dau_hieu'):
            continue
        flows[f.stem] = {'ten': str(p.get('ten') or f.stem), 'dh': str(p.get('dau_hieu')), 'ph': links(p.get('phan_he')), 'pf': str(p.get('nen_tang') or ''),
                         'can': L(p.get('can_cung_cap')), 'buoc': L(p.get('buoc')), 'kt': L(p.get('kiem_tra')), 'kah': L(p.get('khong_anh_huong'))}
    tests = {}                                    # cách test (Cach-test/*.md có dau_hieu): bước thao tác cụ thể theo loại sửa
    for f in sorted((kb / 'Cach-test').glob('*.md')) if (kb / 'Cach-test').is_dir() else []:
        p, _ = parse_note(f.read_text('utf-8', errors='replace'))
        if p.get('loai') != 'cach-test' or not p.get('dau_hieu') or not p.get('buoc'):
            continue
        tests[f.stem] = {'ten': str(p.get('ten') or f.stem), 'dh': str(p.get('dau_hieu')), 'pf': str(p.get('test_tren') or ''),
                         'buoc': L(p.get('buoc')), 'kt': L(p.get('kiem_tra')), 'kah': L(p.get('khong_anh_huong')),
                         'tt': int(p.get('thu_tu') or 9) if str(p.get('thu_tu') or '9').isdigit() else 9}
    webs = {}                                     # trang Netweb (Web/*.md): đọc / ghi dữ liệu nào, chỉnh định Edusoft nào
    for f in sorted((kb / 'Web').glob('*.md')) if (kb / 'Web').is_dir() else []:
        p, _ = parse_note(f.read_text('utf-8', errors='replace'))
        if p.get('loai') != 'trang-web':
            continue
        webs[f.stem] = {'t': str(p.get('ten') or f.stem), 'vt': L(p.get('vai_tro')), 'menu': str(p.get('menu_web') or ''),
                        'doc': [x for x in links(p.get('du_lieu')) if x in data], 'ghi': [x for x in links(p.get('ghi')) if x in data],
                        'ph': links(p.get('phan_he')), 'cd': [x[:160] for x in L(p.get('chinh_dinh'))[:4]], 'kw': str(p.get('tu_khoa') or '')}
    for fn, d in data.items():
        d['wp'] = [w for w, x in webs.items() if fn in x['doc'] or fn in x['ghi']]
    for d in data.values():                       # bỏ liên kết tới dữ liệu không có ghi chú
        d['req'] = [r for r in d['req'] if r[0] in data]
    lv = {}

    def depth(fn, path=()):
        if fn in lv:
            return lv[fn]
        if fn in path:                            # vòng lặp do sửa tay – không treo
            return 0
        lv[fn] = 1 + max([depth(r[0], path + (fn,)) for r in data[fn]['req']] or [-1])
        return lv[fn]
    for fn in data:
        data[fn]['lv'] = depth(fn)
    g = {'ver': 3, 'src': 'ghi-chu', 'mods': mods, 'data': data, 'schools': schools, 'patterns': pats, 'flows': flows, 'tests': tests, 'qts': qts, 'webs': webs, 'catph': CAT_PH, 'tang': {'0': 'nền, khai báo đầu tiên'}}
    _CACHE[str(kb)] = (sig, g)
    return g


BLOCK = re.compile(r'<script type="application/json" id="kb-graph">.*?</script>', re.S)


def as_block(g):
    return '<script type="application/json" id="kb-graph">' + json.dumps(g, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + '</script>'


def embed(g, html):
    h = Path(html).read_text('utf-8')
    blk = as_block(g)
    h2, n = BLOCK.subn(lambda m: blk, h)
    if not n:
        h2 = h.replace('<script type="text/plain" id="kit-', blk + '\n<script type="text/plain" id="kit-', 1)
    if h2 != h:
        Path(html).write_text(h2, 'utf-8')
    return h2 != h


def embedded(html):
    m = BLOCK.search(Path(html).read_text('utf-8'))
    if not m:
        return None
    return json.loads(m.group(0)[m.group(0).index('>') + 1:-len('</script>')].replace('<\\/', '</'))


def query_text(g, text, mod=''):
    """Nhận ra dữ liệu trong một đoạn văn (lời KH, tiêu đề, menu) – như rtEnts trên trang. → [(tên, điểm, lý do)]"""
    low = re.sub(r'[^/\n.,;:]{2,40}/\s*(?=[^/\n]{2,60})', ' ', str(text or '').lower())
    out = []
    for fn, d in g['data'].items():
        if not d.get('kw'):
            continue
        try:
            hits = re.findall('(?:' + d['kw'] + ')', low, re.I)
        except re.error:
            continue
        if not hits:
            continue
        s = 3 * min(3, len(hits)) + (2 if mod and d['src'] == mod else 0)
        out.append((fn, s, hits[0] if isinstance(hits[0], str) else ''))
    out.sort(key=lambda x: (-x[1], -g['data'][x[0]]['lv']))
    return out


def school_of(g, code):
    """school_code trên ACS → (mã trường 4 ký tự, thông tin, mã phân cấp | None, tên phân cấp).
    Quy ước AQ: mã trường 4 ký tự; dài hơn = phân cấp (hệ / cơ sở) của trường đó, vd DHMOTX = DHMO – từ xa."""
    c = str(code or '').strip().upper()
    S = g.get('schools') or {}
    if not c:
        return None, None, None, ''
    for ma, x in S.items():
        if c == ma.upper():
            return ma, x, None, ''
    for ma, x in S.items():
        if len(ma) == 4 and c.startswith(ma.upper()):
            return ma, x, c, x.get('phan_cap', {}).get(c, '')
    return None, None, (c if len(c) > 4 else None), ''


def patterns_of(g, kh='', ba='', dev='', mod=''):
    """Gợi ý dạng case từ dấu hiệu trong lời KH / BA / Dev → [(tên, điểm, lý do)] (chỉ là gợi ý – người / Claude chốt)."""
    out = []
    for fn, p in (g.get('patterns') or {}).items():
        sc, why = 0, []
        for key, txt, w in (('kh', kh, 3), ('ba', ba, 2), ('dev', dev, 2)):
            if not p.get(key) or not txt:
                continue
            try:
                m = re.search(p[key], str(txt), re.I)
            except re.error:
                continue
            if m:
                sc += w
                why.append(key.upper() + ' "' + m.group(0)[:40] + '"')
        if sc and not any(w.startswith(('KH', 'BA')) for w in why):   # chỉ khớp ghi chú dev → quá yếu
            continue
        if sc and mod and mod in p.get('ph', []):
            sc += 1
        if sc:
            out.append((fn, sc, why))
    out.sort(key=lambda x: -x[1])
    return out


def webs_of(g, text, n=2):
    """trang Netweb (Web/) khớp tiêu đề + lời KH theo `tu_khoa` → [(tên file, trang)], nhiều lần khớp trước"""
    out = []
    for fn, x in (g.get('webs') or {}).items():
        try:
            k = len(re.findall(x['kw'], str(text or ''), re.I)) if x.get('kw') else 0
        except re.error:
            continue
        if k:
            out.append((k, fn, x))
    out.sort(key=lambda t: -t[0])
    return [(fn, x) for _, fn, x in out[:n]]


def flow_of(g, text, mod=''):
    """luồng test (Luong-test/) khớp với tiêu đề + lời KH → (tên file, luồng) hoặc (None, None)"""
    best = (None, None, 0)
    for fn, x in (g.get('flows') or {}).items():
        try:
            m = re.findall(x['dh'], str(text or ''), re.I)
        except re.error:
            continue
        sc = len(m) + (2 if mod and mod in x.get('ph', []) else 0) if m else 0
        if sc > best[2]:
            best = (fn, x, sc)
    return best[0], best[1]


def tests_of(g, text, n=3):
    """cách test (Cach-test/ có dau_hieu) khớp với case → [(tên file, cách test)], nhiều dấu hiệu trước"""
    out = []
    for fn, x in (g.get('tests') or {}).items():
        try:
            m = re.findall(x['dh'], str(text or ''), re.I)
        except re.error:
            continue
        if m:
            out.append((len(m), fn, x))
    return [(fn, x) for _, fn, x in sorted(out, key=lambda t: -t[0])[:n]]


def walk(g, fn, up):
    nxt = {}
    for k, d in g['data'].items():
        for r in d['req']:
            nxt.setdefault(r[0], []).append(k)
    seen, st = set(), [fn]
    while st:
        x = st.pop()
        for y in ([r[0] for r in g['data'][x]['req']] if up else nxt.get(x, [])):
            if y not in seen:
                seen.add(y)
                st.append(y)
    return sorted(seen, key=lambda x: (g['data'][x]['lv'], x))


def main():
    a = sys.argv[1:]
    kb = Path(a[0]) if a and not a[0].startswith('--') else Path(__file__).resolve().parent / 'kb'
    g = build(kb)
    if '--nhung' in a:
        html = a[a.index('--nhung') + 1]
        print('Đã nhúng' if embed(g, html) else 'Không đổi', '-', len(g['data']), 'dữ liệu,', len(g['mods']), 'phân hệ →', html)
    elif '--kiem' in a:
        e = embedded(a[a.index('--kiem') + 1])
        if e != g:
            print('Bản đồ nhúng trong trang KHÁC ghi chú kb/ – chạy: python kb_graph.py kb --nhung web/index.html')
            sys.exit(1)
        print('Bản đồ nhúng khớp ghi chú kb/')
    else:
        print(len(g['data']), 'dữ liệu,', len(g['mods']), 'phân hệ,', sum(len(d['req']) for d in g['data'].values()), 'điều kiện "phải có trước"')


if __name__ == '__main__':
    main()
