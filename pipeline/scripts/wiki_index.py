#!/usr/bin/env python3
"""Build a one-line-per-paper index of the wiki (run once per wiki commit), or print slot fill rates.

  wiki_index.py build [--wiki WIKI] --out index.jsonl    # --wiki defaults to $WIKI_DIR; also writes index.jsonl.meta.json (commit SHA, counts)
  wiki_index.py fill  --index index.jsonl                # M01-M13 fill rates, folders and unique papers

Each row: id, key (version-dedup key), title, year, doi, arxiv, modalities, has_text,
slots{Mxx:{state, text}} where text is the slot's ledger facts as "field=value", and ledger_text = all textual facts
and observation labels of the paper (regex search runs on either; a topic often sits outside its slot's own facts).
Reads only; never writes inside the wiki.
"""
import argparse, collections, glob, json, os, re, subprocess, sys, datetime

CAP = 4000  # max characters of ledger text kept per slot
CAP_ALL = 12000  # max characters of whole-ledger text kept per paper


def norm_title(t):
    return re.sub(r'[^a-z0-9]+', '', (t or '').lower())[:80]


def dedup_key(doi, arxiv, title, pid):
    """Same key = same study. Title first so preprint and published versions merge."""
    nt = norm_title(title)
    if len(nt) >= 20:
        return 't:' + nt
    if doi:
        return 'd:' + doi.lower()
    if arxiv:
        return 'a:' + re.sub(r'v\d+$', '', str(arxiv))
    return 'p:' + pid


def sval(v):
    if isinstance(v, list):
        return ', '.join(map(str, v))
    return '' if v is None else str(v)


def row(wiki, pid):
    base = os.path.join(wiki, 'papers', pid)
    led = json.load(open(os.path.join(base, 'ledger.json')))
    views = json.load(open(os.path.join(base, 'views.json')))
    facts = {f['id']: f for f in led.get('facts', [])}
    first = {}
    for f in led.get('facts', []):
        first.setdefault(f.get('field_id'), f.get('value'))
    labels = collections.defaultdict(list)  # source labels of observations, by value fact
    for o in led.get('observations', []):
        lab = (o.get('metric_mapping') or {}).get('source_label')
        if lab and o.get('value_fact_id'):
            labels[o['value_fact_id']].append(lab)
    slots = {}
    for s in views['graphs']['mechanism_template']['slots']:
        parts = []
        for fid in s.get('fact_ids', []):
            f = facts.get(fid)
            if not f:
                continue
            parts.append('%s=%s' % (f.get('field_id'), sval(f.get('value'))))
            parts.extend(labels.get(fid, []))
        slots[s['id']] = {'state': s.get('state'), 'text': ' | '.join(parts)[:CAP]}
    seen, allp = set(), []
    for f in led.get('facts', []):
        v = sval(f.get('value'))
        if len(v) >= 12 and not v.replace('.', '').isdigit() and v not in seen:
            seen.add(v); allp.append('%s=%s' % (f.get('field_id'), v))
    for labs in labels.values():
        allp.extend(l for l in labs if l not in seen and not seen.add(l))
    year = first.get('year') or first.get('publication_year')
    doi, arxiv, title = first.get('doi'), first.get('arxiv_id'), first.get('title')
    return {'id': pid, 'key': dedup_key(doi, arxiv, title, pid), 'title': title, 'year': year,
            'doi': doi, 'arxiv': arxiv, 'modalities': first.get('modalities') or [],
            'has_text': bool(glob.glob(os.path.join(base, 'source', '*text*.txt'))), 'slots': slots, 'ledger_text': ' | '.join(allp)[:CAP_ALL]}


def build(a):
    pids = sorted(os.listdir(os.path.join(a.wiki, 'papers')))
    ok = bad = 0
    with open(a.out, 'w') as out:
        for pid in pids:
            try:
                out.write(json.dumps(row(a.wiki, pid), ensure_ascii=False) + '\n')
                ok += 1
            except Exception:
                bad += 1
    try:
        sha = subprocess.check_output(['git', '-C', a.wiki, 'rev-parse', 'HEAD'], text=True).strip()
    except Exception:
        sha = None
    meta = {'wiki_commit': sha, 'folders': len(pids), 'readable': ok, 'unreadable': bad,
            'built': datetime.date.today().isoformat()}
    json.dump(meta, open(a.out + '.meta.json', 'w'), indent=1)
    print(json.dumps(meta))


def load(index):
    return [json.loads(l) for l in open(index)]


def fill(a):
    rows = load(a.index)
    keys = {r['key'] for r in rows}
    print('folders %d, unique papers %d' % (len(rows), len(keys)))
    print('| slot | filled (folders) | % | filled (unique) | % |\n|---|---:|---:|---:|---:|')
    for i in range(1, 14):
        m = 'M%02d' % i
        f = [r for r in rows if r['slots'].get(m, {}).get('state') == 'recorded']
        u = {r['key'] for r in f}
        print('| %s | %d | %.0f%% | %d | %.0f%% |' % (m, len(f), 100 * len(f) / len(rows), len(u), 100 * len(u) / len(keys)))


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest='cmd', required=True)
    b = sub.add_parser('build'); b.add_argument('--wiki', default=os.environ.get('WIKI_DIR'), required=not os.environ.get('WIKI_DIR'), help='wiki clone (default: $WIKI_DIR)'); b.add_argument('--out', required=True)
    f = sub.add_parser('fill'); f.add_argument('--index', required=True)
    a = p.parse_args()
    build(a) if a.cmd == 'build' else fill(a)
