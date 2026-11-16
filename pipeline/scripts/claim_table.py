#!/usr/bin/env python3
"""Pre-extract the claim table of a review: each sentence that carries a number or a citation (no LLM).

  claim_table.py SLUG.md [--refs SLUG.refs.json] [--notes notes.json] [--out claims.md] [--json claims.json]

Columns: No | Section | Claim | Cited ref | Location | Notes entry | Quote
- Claim: the sentence (citation links shortened to [n]); the 13-components table and References are skipped,
  Appendix lines are kept (their numbers trace to the topic audits: Notes entry "tally").
- Cited ref: [n] with the short citation from SLUG.refs.json.
- Location: section / Table / Fig. / Eq. / p. given in the sentence.
- Notes entry, Quote: pre-filled with candidate notes.json entries whose numbers match the claim's numbers
  (marked "?"); the claim-table pass (reader model) confirms or corrects each mapping from notes.json only.
The filled table goes to the evaluator model with the compact review (compact_for_chat.py --claims).
"""
import argparse, json, re

CIT = re.compile(r'\[\[(\d+)\]\]\(#ref-\d+\)')
LOC = re.compile(r'(?:§\s?[\d.]+|\b(?:Table|Tab\.|Fig\.|Figure|Sec\.|Section|Eq\.|p\.)\s?[\dA-Z][\w.]*)')
NUM = re.compile(r'(?<![\w.\[])(\d{1,3}(?:,\d{3})+|\d+(?:\.\d+)?)(?![\w\]])')


def nums(s):
    s = CIT.sub('', s)
    s = re.sub(r'\bM\d{2}\b', '', s)
    return [float(x.replace(',', '')) for x in NUM.findall(s)]


def sentences(par):
    return [x.strip() for x in re.split(r'(?<=[.!?])\s+(?=[A-Z\[(*])', par) if x.strip()]


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('md'); p.add_argument('--refs'); p.add_argument('--notes')
    p.add_argument('--out'); p.add_argument('--json')
    a = p.parse_args()
    refs = {}
    if a.refs:
        for r in json.load(open(a.refs)):
            refs[r['n']] = re.sub(r'\s*\[(?:concurrent|later)\]\s*$', '', r.get('citation', ''))[:90]
    notes = []
    if a.notes:
        notes = json.load(open(a.notes)).get('entries', [])
    rows, sec, fence, skip = [], None, False, False
    for l in open(a.md).read().split('\n'):
        if l.startswith('```'):
            fence = not fence; continue
        if fence or not l.strip():
            continue
        if l.startswith('## '):
            sec = l[3:].strip(); skip = sec in ('The 13 components', 'References'); continue
        if sec is None or skip or l.startswith('#') or l.startswith('|'):
            continue
        text = re.sub(r'^\s*(?:[-*]|\d+\.)\s+', '', l)
        for s in sentences(text):
            cites = [int(n) for n in CIT.findall(s)]
            ns = [n for n in nums(s) if not (1900 <= n <= 2099 and n == int(n))]
            if not cites and not ns:
                continue
            cand = []
            for e in notes:
                hay = ' '.join(str(e.get(k) or '') for k in ('value', 'text', 'quote', 'condition'))
                en = nums(hay)
                if ns and any(any(abs(x - y) < 1e-9 for y in en) for x in ns):
                    cand.append(e)
            rows.append({'no': len(rows) + 1, 'section': sec, 'claim': CIT.sub(r'[\1]', s),
                         'cited': ['[%d] %s' % (n, refs.get(n, '')) for n in dict.fromkeys(cites)],
                         'location': sorted(set(LOC.findall(s))),
                         'notes_entry': ('tally' if sec.startswith('Appendix') else
                                         ', '.join('%s?' % e.get('id') for e in cand[:3])),
                         'quote': (cand[0].get('quote', '') + ' (' + str(cand[0].get('loc', '')) + ')?') if cand and not sec.startswith('Appendix') else ''})
    md = ['| No | Section | Claim | Cited ref | Location | Notes entry | Quote |', '|---|---|---|---|---|---|---|']
    c = lambda x: re.sub(r'\s+', ' ', str(x)).replace('|', '/')
    for r in rows:
        md.append('| %d | %s | %s | %s | %s | %s | %s |' % (r['no'], c(r['section'][:30]), c(r['claim']), c('; '.join(r['cited'])),
                                                          c(', '.join(r['location'])), c(r['notes_entry']), c(r['quote'])))
    out = '\n'.join(md) + '\n'
    if a.out:
        open(a.out, 'w').write(out)
    else:
        print(out)
    if a.json:
        json.dump(rows, open(a.json, 'w'), ensure_ascii=False, indent=1)
    print('%d claims' % len(rows), '->', a.out or 'stdout')


if __name__ == '__main__':
    main()
