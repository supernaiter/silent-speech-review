#!/usr/bin/env python3
"""Reproducibility: compare two independent runs of the same review.

  diff_runs.py A.slots.json B.slots.json [--audit A.topic.audit.json B.topic.audit.json]

Prints verdict agreement over M01-M13 and, per audit pair, agreement of include/exclude decisions
(raw agreement, Cohen's kappa on candidates both runs read, Jaccard of the confirmed sets).
"""
import json, sys


def main():
    if len(sys.argv) < 3 or sys.argv[1] in ('-h', '--help'):
        print(__doc__); sys.exit(0 if len(sys.argv) > 1 else 2)
    args = sys.argv[1:]
    aud = []
    if '--audit' in args:
        i = args.index('--audit'); aud = args[i + 1:i + 3]; args = args[:i]
    A, B = json.load(open(args[0])), json.load(open(args[1]))
    slots = ['M%02d' % i for i in range(1, 14)]
    same = [s for s in slots if A.get(s, {}).get('verdict') == B.get(s, {}).get('verdict')]
    print('verdict agreement %d/13' % len(same))
    for s in slots:
        if s not in same:
            print('  %s: %s | %s' % (s, A.get(s, {}).get('verdict'), B.get(s, {}).get('verdict')))
    if aud:
        da = {c['pid']: c.get('decision') for c in json.load(open(aud[0]))['candidates']}
        db = {c['pid']: c.get('decision') for c in json.load(open(aud[1]))['candidates']}
        both = [p for p in da if db.get(p) in ('include', 'exclude') and da[p] in ('include', 'exclude')]
        ia, ib = {p for p in da if da[p] == 'include'}, {p for p in db if db[p] == 'include'}
        print('candidates A %d, B %d, shared %d, read by both %d' % (len(da), len(db), len(set(da) & set(db)), len(both)))
        if both:
            po = sum(da[p] == db[p] for p in both) / len(both)
            pa, pb = sum(da[p] == 'include' for p in both) / len(both), sum(db[p] == 'include' for p in both) / len(both)
            pe = pa * pb + (1 - pa) * (1 - pb)
            print('decision agreement %.2f, kappa %s' % (po, 'n/a' if pe == 1 else '%.2f' % ((po - pe) / (1 - pe))))
        if ia | ib:
            print('confirmed-set Jaccard %.2f (A %d, B %d, both %d)' % (len(ia & ib) / len(ia | ib), len(ia), len(ib), len(ia & ib)))
            for p in sorted(ia ^ ib):
                print('  only in %s: %s' % ('A' if p in ia else 'B', p))


if __name__ == '__main__':
    main()
