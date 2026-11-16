#!/usr/bin/env python3
"""Make a compact copy of a review for the evaluator model (a separate model from the writer).

usage: compact_for_chat.py REVIEW.md OUT.md [--claims claims.md] [--full]

Default (evaluation copy): the review up to "## References" without "## Questions for the authors" and without
"## Appendix: literature search" (wiki counts are outside the evaluator's check), then the References list, then the
claim table from claim_table.py (--claims). --full keeps the Appendix and Questions (old behaviour).
Strips anchors, [[n]](#ref-n) -> [n], drops [review] and wiki links, unwraps other links.
"""
import re, sys

args = [x for x in sys.argv[1:] if not x.startswith('--')]
if len(args) < 2 or '-h' in sys.argv or '--help' in sys.argv:
    print(__doc__); sys.exit(0 if '--help' in sys.argv else 2)
claims = None
if '--claims' in sys.argv:
    claims = sys.argv[sys.argv.index('--claims') + 1]
    args = [x for x in args if x != claims]
t = open(args[0]).read()
j = t.find('\n## References')
main = t[:j] if j > 0 else t; refs = t[j:] if j > 0 else ''
if '--full' not in sys.argv:
    for h in ('Questions for the authors', 'Appendix: literature search'):
        main = re.sub(r'\n## ' + re.escape(h) + r'\n.*?(?=\n## |\Z)', '\n', main, flags=re.S)
main = re.sub(r'\[\[(\d+)\]\]\(#ref-\d+\)', r'[\1]', main)
refs = re.sub(r'<a id="ref-\d+"></a>', '', refs)
refs = re.sub(r'\[(review|wiki:[^\]]*)\]\([^)]*\)', '', refs)
refs = re.sub(r'\[([^\]]+)\]\(https?://[^)]*\)', r'\1', refs)
refs = re.sub(r'\[([^\]]+\.bib)\]\([^)]*\)', r'\1', refs)
out = main.rstrip() + '\n\n' + refs.strip() + '\n'
def short_row(l):
    # in the chat copy the claim is cut to its first 12 words and refs to [n]: the full text and the
    # reference list are already above, so the table only adds the quote and location of each claim
    c = l.strip().strip('|').split('|')
    if len(c) < 7 or not c[0].strip().isdigit():
        return l
    w = c[2].split()
    c[2] = ' ' + ' '.join(w[:12]) + (' ...' if len(w) > 12 else '') + ' '
    c[3] = ' ' + ' '.join(re.findall(r'\[\d+\]', c[3])) + ' '
    return '|' + '|'.join(c) + '|'
if claims:
    rows = [short_row(l) for l in open(claims).read().split('\n')]
    out += '\n## Claim table (each number or citation in the review, with the source quote and location)\n\n' + '\n'.join(rows)
open(args[1], 'w').write(out); print(len(out), 'chars')
