#!/usr/bin/env python3
"""Build the data/reviews.jsonl row and <slug>.json from the writer's verdict.json, slots.json and refs (no LLM).

  fill_row.py --slug SLUG --refs refs.json --target-key KEY --refs-out SLUG.refs.json --verdict verdict.json \
      --slots SLUG.slots.json [--reviews-jsonl REVIEWS/data/reviews.jsonl] [--extra extra.json] \
      [--en '{"task": "...", "vocabulary": "..."}'] --out SLUG.json [--row-out row.json]

Row (fields scripts/build.py reads): paper_id, slug, title, year, venue, authors, doi, doi_url, arxiv_id,
arxiv_url, review_state, review_confidence, review_basis, tags, expert_take_short (= verdict.short),
expert_take_long (= verdict.position), en {summary (= verdict.short), sensor, task, vocabulary, speaker, session,
mode, key_result, limitations}. Bibliographic data come from the target's refs.json entry (taken from the paper).
An existing row with the same slug supplies paper_id, tags, the en fields other than summary (unless --en
overrides them) and the legacy narrative fields (canon_before, delta_from_canon, position_in_field,
practical_value, axes_*, *_limits, evidence, ...), copied unchanged. Without one, legacy fields are dropped,
en.sensor comes from the M05 choice, speaker / session / mode are "Not stated" and the rest are empty.
<slug>.json = row + extra.json (component_review, verification_status, ...) + human_verified (false unless
given) + references (from --refs-out).
"""
import argparse, json, os, sys

LEGACY = ['expert_true_value', 'canon_before', 'delta_from_canon', 'position_in_field', 'practical_value',
          'axes_moved', 'axes_unresolved', 'axes_regressed', 'technical_limits', 'evaluation_limits',
          'deployment_limits', 'scope_limits', 'task', 'input_modality', 'sensor_hardware', 'body_site',
          'output_type', 'vocabulary_type', 'vocabulary_size', 'metrics', 'evaluation_mode', 'evidence',
          'review_priority', 'source_coverage']
EN = ['summary', 'sensor', 'task', 'vocabulary', 'speaker', 'session', 'mode', 'key_result', 'limitations']


def person(a):
    if ',' in a:
        fam, giv = [x.strip() for x in a.split(',', 1)]
        return (giv + ' ' + fam).strip()
    return a.strip()


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    for x in ('--slug', '--refs', '--target-key', '--refs-out', '--verdict', '--slots', '--out'):
        p.add_argument(x, required=True)
    p.add_argument('--reviews-jsonl'); p.add_argument('--extra'); p.add_argument('--en'); p.add_argument('--row-out')
    a = p.parse_args()
    refs = json.load(open(a.refs))
    t = next((r for r in refs if r.get('key') == a.target_key), None)
    if not t:
        sys.exit('target key %s not in %s' % (a.target_key, a.refs))
    V = json.load(open(a.verdict)); S = json.load(open(a.slots))
    short, pos = (V.get('short') or '').strip(), (V.get('position') or '').strip()
    if not short or len(short) > 200:
        sys.exit('verdict.json "short" must be 1-200 characters (is %d)' % len(short))
    old = {}
    if a.reviews_jsonl and os.path.exists(a.reviews_jsonl):
        for l in open(a.reviews_jsonl, encoding='utf-8'):
            if l.strip():
                r = json.loads(l)
                if r.get('slug') == a.slug:
                    old = r
    doi, arx = t.get('doi') or '', t.get('arxiv') or ''
    pid = old.get('paper_id') or ('arxiv_' + arx.replace('.', '-') if arx else ('doi_' + doi.replace('/', '_') if doi else
                                                                                (t['pid'][0] if isinstance(t.get('pid'), list) else t.get('pid') or a.slug)))
    row = {'paper_id': pid, 'slug': a.slug, 'title': t['title'], 'year': int(t['year']),
           'venue': t.get('container') or '', 'authors': [person(x) for x in t.get('authors') or []],
           'doi': doi, 'doi_url': 'https://doi.org/' + doi if doi else '',
           'arxiv_id': arx, 'arxiv_url': 'https://arxiv.org/abs/' + arx if arx else '',
           'review_state': 'component_review', 'review_confidence': old.get('review_confidence') or 'medium',
           'review_basis': 'full_text', 'tags': old.get('tags') or [],
           'expert_take_short': short, 'expert_take_long': pos}
    for k in LEGACY:
        if old.get(k) not in (None, '', []):
            row[k] = old[k]
    oe = old.get('en') or {}
    m05 = (S.get('M05') or {}).get('choice') or []
    en = {'summary': short, 'sensor': oe.get('sensor') or ('; '.join(m05) if isinstance(m05, list) else str(m05)),
          'task': oe.get('task', ''), 'vocabulary': oe.get('vocabulary', ''),
          'speaker': oe.get('speaker') or 'Not stated', 'session': oe.get('session') or 'Not stated',
          'mode': oe.get('mode') or 'Not stated', 'key_result': oe.get('key_result', ''), 'limitations': oe.get('limitations', '')}
    if a.en:
        en.update(json.loads(a.en))
    row['en'] = {k: en.get(k, '') for k in EN}
    full = dict(row)
    if a.extra:
        full.update(json.load(open(a.extra)))
    full.setdefault('human_verified', False)
    full['references'] = json.load(open(a.refs_out))
    json.dump(full, open(a.out, 'w'), ensure_ascii=False, indent=1)
    if a.row_out:
        open(a.row_out, 'w').write(json.dumps(row, ensure_ascii=False) + '\n')
    print('wrote', a.out, '(existing row reused)' if old else '(new row)')


if __name__ == '__main__':
    main()
