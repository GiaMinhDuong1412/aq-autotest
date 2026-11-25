#!/usr/bin/env python3
"""Kiểm tra liên kết trong KB (vault Obsidian kb/).

    python tools/kb_kiem_lien_ket.py kb            # in báo cáo
    python tools/kb_kiem_lien_ket.py kb --strict   # có lỗi liên kết ở Web/ hoặc trang 00 thì thoát mã 1

Kiểm:
1. Liên kết [[…]] trỏ tới ghi chú không có (theo tên file, đường dẫn hoặc aliases – như Obsidian, không phân biệt hoa thường).
2. Trang web (Web/*.md): `du_lieu` / `ghi` phải là ghi chú trong Du-lieu/, `phan_he` trong Phan-he/, phải có `tu_khoa`
   và mục "Chỉnh định quyết định trang này".
3. Hai chiều Netweb ↔ dữ liệu: dữ liệu có mục "Trên web" nhưng chưa trang Web/ nào đọc / ghi; dữ liệu được trang Web/ ghi ngược
   nhưng ghi chú dữ liệu không nhắc web.
Chỉ đọc, không sửa ghi chú.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from kb_graph import parse_note, section, links  # noqa: E402

LINK = re.compile(r'\[\[([^\]|#^]+)(?:[#^][^\]|]*)?(?:\|[^\]]*)?\]\]')
FENCE = re.compile(r'```.*?```', re.S)
CODE = re.compile(r'`[^`\n]*`')
SKIP_DIRS = {'.obsidian', '.trash', '_templates'}


def notes(kb):
    for f in sorted(kb.rglob('*')):
        rel = f.relative_to(kb)
        if f.is_file() and not (set(rel.parts[:-1]) & SKIP_DIRS):
            yield f, rel


def index(kb):
    """Tên → đường dẫn (tên file không đuôi, đường dẫn tương đối, aliases; file không phải .md theo tên đầy đủ)."""
    idx = {}
    for f, rel in notes(kb):
        keys = [rel.as_posix(), f.name]
        if f.suffix == '.md':
            keys += [f.stem, rel.with_suffix('').as_posix()]
            try:
                p, _ = parse_note(f.read_text('utf-8', errors='replace'))
            except Exception:
                p = {}
            al = p.get('aliases') or []
            keys += [str(a) for a in (al if isinstance(al, list) else [al])]
        for k in keys:
            idx.setdefault(k.strip().lower(), rel.as_posix())
    return idx


def broken(kb, idx):
    out = {}
    for f, rel in notes(kb):
        if f.suffix != '.md':
            continue
        text = CODE.sub('', FENCE.sub('', f.read_text('utf-8', errors='replace')))
        tg = {m.group(1).strip().rstrip('\\').strip() for m in LINK.finditer(text)}   # [[X\\|y]] trong bảng Markdown
        bad = sorted(t for t in tg if t and t not in ('…', '...') and t.lower() not in idx)
        if bad:
            out[rel.as_posix()] = bad
    return out


def web_checks(kb):
    probs, reads, writes = [], {}, {}
    dl = {f.stem for f in (kb / 'Du-lieu').glob('*.md')} if (kb / 'Du-lieu').is_dir() else set()
    ph = {f.stem for f in (kb / 'Phan-he').glob('*.md')} if (kb / 'Phan-he').is_dir() else set()
    for f in sorted((kb / 'Web').glob('*.md')) if (kb / 'Web').is_dir() else []:
        p, body = parse_note(f.read_text('utf-8', errors='replace'))
        if p.get('loai') != 'trang-web':
            probs.append((f.name, 'thiếu loai: trang-web'))
            continue
        for k, ok, where in (('du_lieu', dl, 'Du-lieu/'), ('ghi', dl, 'Du-lieu/'), ('phan_he', ph, 'Phan-he/')):
            for x in links(p.get(k)):
                if x not in ok:
                    probs.append((f.name, '%s: [[%s]] không có trong %s' % (k, x, where)))
        for x in links(p.get('du_lieu')):
            reads.setdefault(x, []).append(f.stem)
        for x in links(p.get('ghi')):
            writes.setdefault(x, []).append(f.stem)
        if not str(p.get('tu_khoa') or '').strip():
            probs.append((f.name, 'thiếu tu_khoa (app không nhận ra trang này trong lời KH)'))
        else:
            try:
                re.compile(str(p.get('tu_khoa')))
            except re.error as e:
                probs.append((f.name, 'tu_khoa không phải regex hợp lệ: %s' % e))
        if not section(body, r'Chỉnh định').strip():
            probs.append((f.name, 'thiếu mục "Chỉnh định quyết định trang này" (ghi — nếu không có)'))
    no_page, no_web = [], []
    for fn in sorted(dl):
        p, body = parse_note((kb / 'Du-lieu' / (fn + '.md')).read_text('utf-8', errors='replace'))
        web = section(body, r'Trên web').strip()
        has_web = bool(web) and web not in ('—', '-')
        if has_web and fn not in reads and fn not in writes:
            no_page.append(fn)
        if fn in writes and not has_web:
            no_web.append((fn, writes[fn]))
    return probs, reads, writes, no_page, no_web


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    strict = '--strict' in sys.argv
    kb = Path(args[0] if args else 'kb')
    if not kb.is_dir():
        sys.exit('Không thấy thư mục KB: %s' % kb)
    idx = index(kb)
    bad = broken(kb, idx)
    probs, reads, writes, no_page, no_web = web_checks(kb)
    n_bad = sum(len(v) for v in bad.values())
    print('KB: %s – %d ghi chú, %d liên kết hỏng ở %d ghi chú' % (kb, sum(1 for f, _ in notes(kb) if f.suffix == '.md'), n_bad, len(bad)))
    core = {k: v for k, v in bad.items() if k.startswith('Web/') or Path(k).name.startswith('00 ')}
    if bad:
        print('\n## Liên kết hỏng (trỏ tới ghi chú chưa có)')
        for k in sorted(bad, key=lambda k: (k not in core, k)):
            print('- %s: %s' % (k, ', '.join('[[%s]]' % x for x in bad[k][:12]) + (' …' if len(bad[k]) > 12 else '')))
    print('\n## Trang Netweb (Web/): %d trang, %d dữ liệu được đọc, %d dữ liệu được ghi ngược' % (
        len(list((kb / 'Web').glob('*.md'))) if (kb / 'Web').is_dir() else 0, len(reads), len(writes)))
    for f, m in probs:
        print('- %s: %s' % (f, m))
    if no_page:
        print('\n## Dữ liệu có mục "Trên web" nhưng chưa trang Web/ nào đọc / ghi (%d)' % len(no_page))
        print('- ' + ', '.join('[[%s]]' % x for x in no_page))
    if no_web:
        print('\n## Dữ liệu được web ghi ngược nhưng ghi chú dữ liệu chưa nhắc "Trên web"')
        for fn, w in no_web:
            print('- [[%s]] ← %s' % (fn, ', '.join(w)))
    if not (bad or probs or no_page or no_web):
        print('\nKhông có vấn đề.')
    if strict and (core or probs):
        sys.exit(1)


if __name__ == '__main__':
    main()
