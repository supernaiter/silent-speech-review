#!/usr/bin/env python3
"""Check that every notes.json quote occurs in its paper's source text (whitespace/case/hyphenation normalized).
Usage: verify_quotes.py notes.json [--wiki WIKI] [--code-dir DIR] [--drop]   (--wiki defaults to $WIKI_DIR)
Entries from figures/PDF-only or code are checked against --code-dir files when loc looks like a path; else reported as 'unchecked'.
Exit 1 if any checkable quote is missing. --drop writes notes.json without the failing entries (backup notes.json.bak)."""
import argparse, json, re, os, glob, shutil, sys
def norm(s):
    s = s.replace('­', '').replace('-\n', '')
    s = re.sub(r'[‐-―−]', '-', s)
    s = re.sub(r'[‘’“”"\'`]', '', s)
    return re.sub(r'\s+', ' ', s).strip().lower()
ap = argparse.ArgumentParser(); ap.add_argument('notes'); ap.add_argument('--wiki', default=os.environ.get('WIKI_DIR'), required=not os.environ.get('WIKI_DIR'), help='wiki clone (default: $WIKI_DIR)')
ap.add_argument('--code-dir'); ap.add_argument('--drop', action='store_true'); a = ap.parse_args()
n = json.load(open(a.notes)); cache = {}; bad = []; unchecked = 0; ok = 0
code = ''
if a.code_dir:
    for f in glob.glob(os.path.join(a.code_dir, '**', '*'), recursive=True):
        if os.path.isfile(f) and os.path.getsize(f) < 2_000_000:
            try: code += '\n' + open(f, errors='ignore').read()
            except Exception: pass
    code = norm(code)
for e in n.get('entries', []):
    q = (e.get('quote') or '').strip(); pid = e.get('paper')
    if not q or e.get('kind') == 'unstated': unchecked += 1; continue
    if pid not in cache:
        p = os.path.join(a.wiki, 'papers', str(pid), 'source', 'text.txt')
        if not os.path.exists(p): p = os.path.join(a.wiki, 'papers', str(pid), 'source', 'sc_text.txt')
        cache[pid] = norm(open(p, errors='ignore').read()) if os.path.exists(p) else None
    hay = cache[pid]
    if e.get('kind') == 'code_condition': hay = code or None
    if hay is None: unchecked += 1; continue
    if norm(q) in hay: ok += 1
    else: bad.append(e)
for e in bad: print(f"MISSING {e.get('id')} [{e.get('paper')} {e.get('loc')}]: {e.get('quote')[:120]}")
print(f"summary: {ok} found, {len(bad)} missing, {unchecked} unchecked (unstated, figure-only or no source)")
if a.drop and bad:
    shutil.copy(a.notes, a.notes + '.bak'); ids = {e.get('id') for e in bad}
    n['entries'] = [e for e in n['entries'] if e.get('id') not in ids]
    json.dump(n, open(a.notes, 'w'), ensure_ascii=False, indent=1)
sys.exit(1 if bad else 0)
