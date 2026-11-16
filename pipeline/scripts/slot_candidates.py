#!/usr/bin/env python3
"""Field comparison for one topic inside one slot, straight from the wiki ledgers (no LLM, no candidate reading).

  slot_candidates.py --index index.jsonl --wiki WIKI --slot M05 --topic sensor-subset \
      --pattern 'channel (subset|selection)|fewer (channels|electrodes)' \
      [--design-field 'channel_count|sensor_geometry'] [--design-slot M05] \
      [--design-regex 'lm=language model|beam search' ...] [--design-scope candidates|all] \
      [--metric-pattern '\\bWER\\b|word error rate'] [--unit-pattern '%|percent'] [--better lower|higher] [--top 10] \
      [--fulltext-pattern '...'] [--sample 30 --seed 1] [--seeds ids] [--reuse components/M05/sensor-subset.json] \
      --out topic.audit.json

Population  : papers whose ledger text (--scope ledger, default) or own slot facts (--scope slot) match --pattern
              (tier "pattern match"); slot_filled counts papers whose --slot state is "recorded".
usual_approach (written once; kept on re-runs):
  slot-filled  : the most common fact values of --design-slot (default --slot; fields filtered by --design-field)
                 among population papers whose design slot is recorded, counted in unique studies.
  pattern match: for sparse slots (design slot recorded in <5% of papers; M02, M07, M11; not M09/M10) each
                 --design-regex NAME=REGEX is counted over source full text (reference list removed) of the
                 population (--design-scope candidates) or of every paper with text (--design-scope all).
  -> {"design", "n" (unique ledger papers), "tier": "slot-filled" | "pattern match", "pids": top examples}
sota_candidates (refreshed every run): ranked best reported values from ledger metric facts of the population
  (observations whose source label or unit match --metric-pattern; the raw value only when there is no label), one per study (differences / gains and negative values skipped, fractions shown as %):
  {"metric", "value", "unit", "year", "pid", "raw"}. Ledger values are candidates only: the writer confirms the
  chosen one in the source text and then writes "state_of_the_art" (kept on re-runs).
Recall check (optional): --fulltext-pattern finds papers the ledger search missed (via=fulltext);
  --sample draws a fixed random sample of them. Read it only when the review claims `ahead` or an absence.
Known-item recall (optional): --seeds -> share of known ids the patterns recover.

Re-use: if --out exists (or --reuse gives the published topic table), every key already in it is kept
(inclusion_rule, usual_approach, state_of_the_art, read_fulltext, candidate decisions); only new candidates and
the refreshed ledger_tally / sota_candidates / counts are added. Prints a compact summary: read that, not the file.
"""
import argparse, collections, glob, json, os, random, re

SPARSE_OK = {'M09', 'M10'}  # sparse, but the slot count is meaningful (mostly truly absent)
DIFF = re.compile(r'\b(?:minus|difference|delta|improvement|reduction|gain|relative|p-value|p value|wilcoxon|permutation|perm)\b', re.I)  # not an absolute result
KEEP = ('decision', 'quote', 'loc', 'provenance', 'reason')


def fulltext(wiki, pid):
    t = ''
    for f in sorted(glob.glob(os.path.join(wiki, 'papers', pid, 'source', '*text*.txt'))):
        t += open(f, errors='ignore').read()
    m = None
    for m in re.finditer(r'\n\s*(References|REFERENCES|Bibliography|BIBLIOGRAPHY)\s*\n', t):
        pass
    if m and m.start() > len(t) * 0.4:
        t = t[:m.start()]
    return re.sub(r'\s+', ' ', t)


def snippet(text, m, w=120):
    return text[max(0, m.start() - w):m.end() + w].strip()


def slot_pairs(text, field_re):
    """'field=value | label | field=value' -> [(field, value)] with short values; list values split."""
    out = []
    for part in (text or '').split(' | '):
        if '=' not in part:
            continue
        f, v = part.split('=', 1)
        f, v = f.strip(), v.strip()
        if not v or (field_re and not field_re.search(f)):
            continue
        vals = [x.strip() for x in v.split(', ')]
        vals = vals if all(len(x) <= 40 for x in vals) else [v]
        out += [(f, x.lower()) for x in vals if 0 < len(x) <= 80]
    return out


def metrics(wiki, pid, mpat, upat=None):
    try:
        led = json.load(open(os.path.join(wiki, 'papers', pid, 'ledger.json')))
    except Exception:
        return []
    labels = {}
    for o in led.get('observations', []):
        lab = (o.get('metric_mapping') or {}).get('source_label')
        if o.get('value_fact_id'):
            labels[o['value_fact_id']] = lab or ''
    out = []
    for f in led.get('facts', []):
        if f.get('field_id') != 'metric_value' or not isinstance(f.get('value'), (int, float)) or isinstance(f.get('value'), bool):
            continue
        lab = labels.get(f['id'], '')
        hay = ' '.join(str(x) for x in ((lab, f.get('unit')) if lab else (f.get('unit'), f.get('raw_value'))) if x)
        if mpat.search(hay) and not DIFF.search(lab or '') and f['value'] >= 0:
            v, u = f['value'], f.get('unit')
            if u and 'fraction' in str(u).lower() and v <= 1:
                v, u = round(100 * v, 4), '% (from fraction)'
            if upat and not upat.search(str(u or '')):
                continue
            out.append({'metric': lab or str(f.get('raw_value') or '')[:80], 'value': v, 'unit': u,
                        'raw': str(f.get('raw_value') or '')[:160]})
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--index', required=True); p.add_argument('--slot', required=True)
    p.add_argument('--topic', required=True); p.add_argument('--pattern', required=True)
    p.add_argument('--wiki', default=os.environ.get('WIKI_DIR'), help='wiki clone (default: $WIKI_DIR)')
    p.add_argument('--scope', choices=['ledger', 'slot'], default='ledger')
    p.add_argument('--design-slot'); p.add_argument('--design-field')
    p.add_argument('--design-regex', action='append', default=[], help='NAME=REGEX, repeatable (full-text pattern counts)')
    p.add_argument('--design-scope', choices=['candidates', 'all'], default='candidates')
    p.add_argument('--metric-pattern'); p.add_argument('--unit-pattern', help="keep only these units, e.g. '%%|percent'"); p.add_argument('--better', choices=['lower', 'higher'], default='lower')
    p.add_argument('--top', type=int, default=10)
    p.add_argument('--fulltext-pattern')
    p.add_argument('--sample', type=int, default=30); p.add_argument('--seed', type=int, default=1)
    p.add_argument('--seeds', help='comma-separated wiki ids, or a file with one id per line')
    p.add_argument('--reuse', help='published topic table (components/<Mxx>/<topic>.json) to start from')
    p.add_argument('--out', required=True)
    a = p.parse_args()
    if (a.fulltext_pattern or a.design_regex or a.metric_pattern) and not a.wiki:
        p.error('--fulltext-pattern, --design-regex and --metric-pattern need --wiki')
    rows = [json.loads(l) for l in open(a.index)]
    meta = json.load(open(a.index + '.meta.json')) if os.path.exists(a.index + '.meta.json') else {}
    prev = {}
    if os.path.exists(a.out):
        prev = json.load(open(a.out))
    elif a.reuse and os.path.exists(a.reuse):
        prev = json.load(open(a.reuse))
    old = {c['pid']: c for c in prev.get('candidates', [])}
    pat = re.compile(a.pattern, re.I)
    fpat = re.compile(a.fulltext_pattern, re.I) if a.fulltext_pattern else None
    uniq = lambda xs: len({x['key'] for x in xs})
    byid = {r['id']: r for r in rows}

    cands, filled = {}, []
    for r in rows:
        s = r['slots'].get(a.slot, {})
        if s.get('state') == 'recorded':
            filled.append(r)
        text = (r.get('ledger_text') if a.scope == 'ledger' else s.get('text')) or ''
        m = pat.search(text)
        if m:
            cands[r['id']] = {'pid': r['id'], 'key': r['key'], 'title': r['title'], 'year': r['year'],
                              'via': ['ledger'], 'snippet': snippet(text, m)}
        if fpat and r.get('has_text'):
            t = fulltext(a.wiki, r['id'])
            m = fpat.search(t)
            if m:
                c = cands.setdefault(r['id'], {'pid': r['id'], 'key': r['key'], 'title': r['title'],
                                               'year': r['year'], 'via': [], 'snippet': ''})
                c['via'].append('fulltext'); c['fulltext_snippet'] = snippet(t, m)
    for pid, o in old.items():  # keep earlier candidates even if the patterns changed (append only)
        if pid not in cands:
            cands[pid] = dict(o)
    for c in cands.values():
        o = old.get(c['pid'], {})
        for k in KEEP:
            if o.get(k) is not None:
                c[k] = o[k]
    led = [c for c in cands.values() if 'ledger' in c.get('via', [])]
    ft_only = sorted(c['pid'] for c in cands.values() if c.get('via') == ['fulltext'])
    random.Random(a.seed).shuffle(ft_only)

    # --- usual approach from slot fact values (slot-filled) or full-text pattern counts (pattern match)
    dslot = a.design_slot or a.slot
    dfill = sum(1 for r in rows if r['slots'].get(dslot, {}).get('state') == 'recorded') / max(1, len(rows))
    sparse = dfill < 0.05 and dslot not in SPARSE_OK
    fre = re.compile(a.design_field, re.I) if a.design_field else None
    popl = [byid[c['pid']] for c in led if c['pid'] in byid]
    vals = collections.defaultdict(dict)  # design -> key -> pid
    rec = [r for r in popl if r['slots'].get(dslot, {}).get('state') == 'recorded']
    for r in rec:
        for f, v in slot_pairs(r['slots'][dslot].get('text'), fre):
            vals['%s=%s' % (f, v)].setdefault(r['key'], r['id'])
    yr = lambda pid: -(int(byid[pid]['year']) if str(byid.get(pid, {}).get('year') or '').isdigit() else 0)
    ranked = sorted(vals.items(), key=lambda kv: -len(kv[1]))
    design_values = [{'design': d, 'n': len(ks), 'tier': 'slot-filled', 'pids': sorted(ks.values(), key=yr)[:5]}
                     for d, ks in ranked[:a.top]]
    pattern_counts = []
    if a.design_regex:
        scope = [r for r in rows if r.get('has_text')] if a.design_scope == 'all' else \
            [byid[c['pid']] for c in cands.values() if c['pid'] in byid and byid[c['pid']].get('has_text')]
        regs = []
        for x in a.design_regex:
            name, _, rx = x.partition('=')
            regs.append((name.strip(), re.compile(rx, re.I)))
        hits = collections.defaultdict(dict)
        for r in scope:
            t = fulltext(a.wiki, r['id'])
            for name, rx in regs:
                if rx.search(t):
                    hits[name].setdefault(r['key'], r['id'])
        pattern_counts = sorted(({'design': n, 'n': len(hits[n]), 'tier': 'pattern match',
                                  'pids': sorted(hits[n].values(), key=yr)[:5]} for n, _ in regs), key=lambda d: -d['n'])
        pattern_scope_unique = len({r['key'] for r in scope})
    if sparse and pattern_counts:
        ua = dict(pattern_counts[0])
    elif design_values:
        ua = dict(design_values[0])
    else:
        ua = dict(pattern_counts[0]) if pattern_counts else None
    if ua is not None:
        ua['population_unique'] = len({r['key'] for r in rec}) if ua['tier'] == 'slot-filled' else pattern_scope_unique

    # --- state-of-the-art candidates from ledger metric facts
    sota = []
    if a.metric_pattern:
        mpat = re.compile(a.metric_pattern, re.I)
        best = {}
        for c in cands.values():
            r = byid.get(c['pid'])
            if not r:
                continue
            for m in metrics(a.wiki, c['pid'], mpat, re.compile(a.unit_pattern, re.I) if a.unit_pattern else None):
                m.update({'pid': c['pid'], 'year': r['year'], 'tier': 'ledger only'})
                cur = best.get(r['key'])
                if cur is None or (m['value'] < cur['value'] if a.better == 'lower' else m['value'] > cur['value']):
                    best[r['key']] = m
        sota = sorted(best.values(), key=lambda m: m['value'], reverse=(a.better == 'higher'))[:a.top]

    out = dict(prev)  # keep everything already decided (inclusion_rule, usual_approach, state_of_the_art, read_fulltext, used_by ...)
    out.update({'topic': a.topic, 'slot': a.slot, 'wiki_commit': meta.get('wiki_commit') or prev.get('wiki_commit'),
                'pattern': a.pattern, 'scope': a.scope, 'fulltext_pattern': a.fulltext_pattern,
                'inclusion_rule': prev.get('inclusion_rule'),
                'counts': {'scanned_folders': len(rows), 'scanned_unique': uniq(rows),
                           'slot_filled_folders': len(filled), 'slot_filled_unique': uniq(filled),
                           'string_match_folders': len(led), 'string_match_unique': uniq(led),
                           'fulltext_only_folders': len(ft_only)},
                'ledger_tally': {'design_slot': dslot, 'design_slot_fill': round(dfill, 3), 'sparse': sparse,
                                 'design_values': design_values, 'pattern_counts': pattern_counts,
                                 'metric_pattern': a.metric_pattern, 'better': a.better},
                'sota_candidates': sota,
                'recall_sample': prev.get('recall_sample') or ft_only[:a.sample], 'recall_sample_seed': a.seed,
                'candidates': sorted(cands.values(), key=lambda c: c['pid'])})
    if not prev.get('usual_approach') and ua:
        out['usual_approach'] = ua
    out.setdefault('read_fulltext', [])
    if a.seeds:
        seeds = [x.strip() for x in (open(a.seeds).read().split() if os.path.exists(a.seeds) else a.seeds.split(',')) if x.strip()]
        known = [x for x in seeds if x in byid]
        found = [x for x in known if x in cands]
        out['known_item_recall'] = {'seeds_in_wiki': len(known), 'found': len(found),
                                    'recall': round(len(found) / len(known), 2) if known else None,
                                    'missed': sorted(set(known) - set(found))}
    json.dump(out, open(a.out, 'w'), ensure_ascii=False, indent=1)
    # compact summary (this is what the writer reads)
    print(json.dumps({'topic': a.topic, 'slot': a.slot, 'counts': out['counts']}, ensure_ascii=False))
    if sparse and not pattern_counts:
        print('WARN design slot %s is sparse (%.1f%% filled): give --design-regex for pattern-match counts' % (dslot, 100 * dfill))
    print('usual_approach:', json.dumps(out.get('usual_approach'), ensure_ascii=False))
    for d in (design_values[:5] + pattern_counts[:5]):
        print('  design %-60s n=%d %s' % (d['design'][:60], d['n'], d['tier']))
    for m in sota:
        print('  sota %s %s %s | %s | %s' % (m['value'], m['unit'] or '', m['year'], m['pid'], m['metric'][:70]))
    if 'known_item_recall' in out:
        k = out['known_item_recall']; print('known-item recall', k['recall'], 'missed', k['missed'][:8])


if __name__ == '__main__':
    main()
