#!/usr/bin/env python3
"""Insert the "## The 13 components" table into a draft, built from slots.json (the writer does not write it).

  render_review.py --draft draft.md --slots SLUG.slots.json --out draft.full.md

Run before build_refs.py: [@key] citations inside slots.json "sota" (or "usual") cells are numbered with the rest.
The table goes right after "## Against the field, component by component" (before "## Where the claims outrun
the evidence"). An existing "## The 13 components" section in the draft is replaced.
Columns: Component | This paper | Usual approach (count) | State of the art | Verdict
  This paper            = "; ".join(choice)
  Usual approach (count)= usual (if given) else field, then "(<tier> <matched>)" from matched_tier / matched
  State of the art      = sota, or "–"
  Verdict               = verdict with "_" -> " "
"""
import argparse, json, re, sys

NAMES = {'M01': 'Training-time action', 'M02': 'Training-only supervision', 'M03': 'Training and adaptation',
         'M04': 'Use-time action', 'M05': 'Sensors', 'M06': 'Processing and decoding', 'M07': 'Lexicon and LM',
         'M08': 'Output', 'M09': 'Confirmation', 'M10': 'Correction', 'M11': 'Reference construction',
         'M12': 'Evaluation', 'M13': 'Device and cost'}
TIER = [('slot_filled', 'slot-filled'), ('slot-filled', 'slot-filled'), ('pattern', 'pattern match'),
        ('regex', 'pattern match'), ('fulltext', 'pattern match'), ('confirmed', 'confirmed')]
HEAD = 'The 13 components'


def cell(x):
    return re.sub(r'\s+', ' ', str(x if x not in (None, '') else '–')).replace('|', '/').strip()


def tier(s):
    t = str(s.get('matched_tier') or '')
    lab = next((v for k, v in TIER if t.startswith(k)), None)
    m = s.get('matched')
    if lab is None or m in (None, ''):
        return ''
    return ' (%s %s)' % (lab, '{:,}'.format(m) if isinstance(m, int) else m)


def table(S):
    out = ['## ' + HEAD, '', '| Component | This paper | Usual approach (count) | State of the art | Verdict |',
           '|---|---|---|---|---|']
    for i in range(1, 14):
        m = 'M%02d' % i
        s = S.get(m)
        if not s:
            sys.exit('slots.json lacks ' + m)
        ch = s.get('choice') or []
        this = '; '.join(ch) if isinstance(ch, list) else ch
        usual = s.get('usual') or s.get('field') or '–'
        out.append('| %s %s | %s | %s | %s | %s |' % (m, s.get('name') or NAMES[m], cell(this), cell(usual) + tier(s),
                                                       cell(s.get('sota')), cell(str(s.get('verdict', '')).replace('_', ' '))))
    return out + ['']


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--draft', required=True); p.add_argument('--slots', required=True); p.add_argument('--out', required=True)
    a = p.parse_args()
    L = open(a.draft).read().rstrip('\n').split('\n')
    S = json.load(open(a.slots))
    h2 = [i for i, l in enumerate(L) if l.startswith('## ')]
    old = [i for i in h2 if L[i][3:].strip().lower() == HEAD.lower()]
    if old:  # replace an existing table section
        i = old[0]; j = next((x for x in h2 if x > i), len(L))
        L = L[:i] + L[j:]
        h2 = [i for i, l in enumerate(L) if l.startswith('## ')]
    after = [i for i in h2 if L[i][3:].strip().lower() == 'against the field, component by component']
    if not after:
        sys.exit('draft has no "## Against the field, component by component"')
    j = next((x for x in h2 if x > after[0]), len(L))
    L = L[:j] + table(S) + L[j:]
    open(a.out, 'w').write('\n'.join(L) + '\n')
    print('wrote', a.out)


if __name__ == '__main__':
    main()
