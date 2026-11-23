#!/usr/bin/env python3
"""Mechanical quality gates for a component review (English format, see pipeline/SKILL.md step 5). Exit 1 on FAIL.

  check_review.py --md SLUG.md --json SLUG.json --slots SLUG.slots.json --bib SLUG.bib --notes notes.json \
      [--audit T1.audit.json T2.audit.json ...] [--verdict verdict.json] [--wiki WIKI] \
      [--min-chars 4000] [--max-chars 7000] [--max-read 8] [--strict]

FAIL: Japanese characters; anything but "# Title" and one bibliographic line (year + DOI/arXiv link) before the
first heading; a Status line; fixed headings missing or out of order; process disclaimers ("could not be
verified", "within the wiki search", "recall not measured", "cannot be judged here", "not checked", ...);
unresolved or uncited reference numbers, numbering not in first-appearance order, links into source/, missing wiki
page, a reference without DOI/arXiv/URL, md/bib/json reference mismatch; missing JSON fields (the reviews.jsonl
row from fill_row.py plus component_review, verification_status, human_verified, references); bad slots.json or a
13-components table that disagrees with it; a component section not opening with **Usual approach:** /
**State of the art:**; a 13-components table without Component | This paper | Usual approach (count) | State of the
art | Verdict; an audit with neither usual_approach nor a ledger tally; an audited topic whose inclusion rule or
ledger count (slot-filled / pattern match, unique studies) is not in the Appendix; "ahead" without an audit for
that slot whose Appendix entry gives the ledger count and whose read_fulltext lists the deciding prior(s) as read,
each cited in the review; novelty / absence wording that does not point to the Appendix; a number in the review
(title line, 13-components table and References excluded) that is in no notes.json entry, audit, slots.json or
verdict.json and not in a sentence marked "(inference)" (years and integers 0-13 are exempt); verdict.json "short"
missing or over 200 characters; body length outside --min-chars..--max-chars.
WARN: [concurrent] / [later] works never labelled where cited; hedging or more than 6 sentences in Verdict;
"What the field needs next" not 2-4 items tied to a component; claims-outrun items without citation or location;
unknown extra ## headings; an audit without state_of_the_art or sota candidates; known-item recall computed but not
in the Appendix; more than --max-read papers read in full besides the target. --strict turns WARN into FAIL.
No gate depends on confirmed counts, recall estimates or include decisions with quotes (legacy audits still pass).

Body length = characters from the first "## " heading up to "## Appendix: literature search", fenced blocks
excluded, [[n]](#ref-n) counted as [n].
"""
import argparse, json, os, re, sys

SECTIONS = ['Verdict', 'Against the field, component by component', 'The 13 components',
            'Where the claims outrun the evidence', 'What the field needs next', 'Questions for the authors',
            'Appendix: literature search', 'References']
APPX, REFS, TABLE = 'Appendix: literature search', 'References', 'The 13 components'
FIELDS = ['paper_id', 'slug', 'title', 'year', 'authors', 'review_state', 'review_basis', 'expert_take_short',
          'en', 'component_review', 'verification_status', 'human_verified', 'references']
EN_FIELDS = ['summary', 'sensor', 'task', 'vocabulary', 'speaker', 'session', 'mode', 'key_result', 'limitations']
VERDICTS = {'ahead', 'standard', 'behind', 'not_reported', 'not_applicable'}
TIERS = ('slot_filled', 'slot-filled', 'pattern', 'regex', 'fulltext', 'confirmed')
JA = re.compile('[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uff01-\uff60\u3000-\u303f]')
BANNED = re.compile(r'could(?: not|n\'t) (?:be )?(?:verif|confirm|check|determin|judg|assess)\w*|unable to (?:verify|confirm|check)'
                    r'|cannot be (?:judged|assessed|determined|verified|checked)(?: here)?|can\'t be (?:judged|assessed)'
                    r'|not (?:yet )?(?:been )?checked|did not check|were not able to|within (?:the|our|this) (?:wiki|search)'
                    r'|(?:in|from|by) (?:the|our|this) wiki(?: search)?|wiki search|recall (?:was |is )?not measured'
                    r'|recall unmeasured|\bdraft\b|human (?:check|verification)|not (?:yet )?verified by|\bunverified\b'
                    r'|we (?:did not|could not|have not) (?:read|verify|check)', re.I)
FIRST = re.compile(r'\b(?:the first (?:to|study|work|paper|system|report|demonstration|method|approach|time)|first ever'
                   r'|for the first time|the only (?:study|work|paper|system|one|method|approach|example|other|report)'
                   r'|no other|none of the|no (?:prior|previous|earlier|published) (?:study|studies|work|works|paper|papers|example|report)'
                   r'|unique(?:ly)?\b(?! (?:stud|paper|work|folder))|unprecedented|novel(?:ty)?|has never been|never (?:been )?(?:reported|shown|done))', re.I)
ABSOLUTE = re.compile(r"\b(?:does not hold|nothing|never|no (?:prior|earlier|other) (?:work|study|paper)s?|none of|first to|the first (?:to|work|study|paper|system|demonstration)|the only|only (?:work|study|paper)|already|always|cannot|fails? to)\b", re.I)
GROUND = re.compile(r'\[\[\d+\]\]\(#ref-\d+\)|\[\d+\]|§\s?\d|\b(?:Table|Fig\.|Figure|Sec\.|Section|Eq\.|p\.)\s?[\dA-Z]|Appendix|\(inference\)', re.I)
HEDGE = re.compile(r'\b(?:may|might|possibly|perhaps|arguably|somewhat|it is possible|on the other hand|on balance)\b', re.I)
CIT = re.compile(r'\[\[(\d+)\]\]\(#ref-(\d+)\)')
LOC = re.compile(r'\[\[\d+\]\]|§|\b(?:Table|Tab\.|Fig\.|Figure|Sec\.|Section|Eq\.|p\.)\s?\d|\bAppendix\b')

fails, warns = [], []


def floats(s):
    return [float(x) for x in re.findall(r'(?<![\w.])\d+(?:\.\d+)?', s)]


def has_num(seg, v):
    return any(abs(x - v) < 0.006 or abs(x - 100 * v) < 0.6 for x in floats(seg))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    for x in ('--md', '--json', '--slots', '--bib'):
        p.add_argument(x, required=True)
    p.add_argument('--audit', nargs='*', default=[]); p.add_argument('--wiki', default=os.environ.get('WIKI_DIR'), help='wiki clone (default: $WIKI_DIR)')
    p.add_argument('--min-chars', type=int, default=4000); p.add_argument('--max-chars', type=int, default=7000)
    p.add_argument('--notes', required=True, help='notes.json from the reader')
    p.add_argument('--verdict'); p.add_argument('--max-read', type=int, default=8)
    p.add_argument('--strict', action='store_true')
    a = p.parse_args()
    md = open(a.md).read()
    lines, fence = [], False
    for l in md.split('\n'):  # fenced blocks (Mermaid, code) are kept as blank lines so line numbers stay true
        if l.startswith('```'):
            fence = not fence
            lines.append(''); continue
        lines.append('' if fence else l)
    full = md.split('\n')
    J = json.load(open(a.json)); S = json.load(open(a.slots)); bib = open(a.bib).read()

    # --- English only
    for name, txt in (('md', md), ('bib', bib), ('json', json.dumps(J, ensure_ascii=False)), ('slots.json', json.dumps(S, ensure_ascii=False))):
        m = JA.search(txt)
        if m:
            ln = txt[:m.start()].count('\n') + 1
            fails.append('%s contains Japanese characters (first at line %d: %r)' % (name, ln, txt[max(0, m.start() - 15):m.end() + 15]))

    # --- header: "# Title" + one bibliographic line, nothing else
    h2 = [i for i, l in enumerate(lines) if l.startswith('## ')]
    first_h2 = h2[0] if h2 else len(lines)
    pre = [(i, l.strip()) for i, l in enumerate(full[:first_h2]) if l.strip()]
    if not pre or not re.match(r'^# \S', pre[0][1]):
        fails.append('review must start with "# <Title>"')
    else:
        rest = pre[1:]
        if len(rest) != 1:
            fails.append('exactly one bibliographic line must follow the title before the first heading (found %d non-empty lines)' % len(rest))
        if rest:
            b = rest[0][1]
            if not re.search(r'\b(?:19|20)\d\d\b', b) or not re.search(r'doi\.org/|arxiv\.org/abs/', b):
                fails.append('line %d: bibliographic line needs a year and a DOI or arXiv link' % (rest[0][0] + 1))
    if re.search(r'\*\*\s*Status\s*\*\*|^\s*Status\s*:', md, re.M | re.I):
        fails.append('a Status line is present (not allowed)')

    # --- sections, in order
    heads = [lines[i][3:].strip() for i in h2]
    pos = {}
    for s in SECTIONS:
        hit = [k for k, h in enumerate(heads) if h.lower() == s.lower()]
        if not hit:
            fails.append('section heading missing: ## ' + s)
        else:
            pos[s] = hit[0]
            if len(hit) > 1:
                fails.append('section heading repeated: ## ' + s)
    seen = [pos[s] for s in SECTIONS if s in pos]
    if seen != sorted(seen):
        fails.append('section headings out of order (required: %s)' % ' / '.join(SECTIONS))
    for h in heads:
        if h.lower() not in [s.lower() for s in SECTIONS]:
            warns.append('extra ## heading not in the format: ' + h)

    def sec(name):
        if name not in pos:
            return None, None
        i = h2[pos[name]]
        j = next((x for x in h2 if x > i), len(lines))
        return i, j
    for f in FIELDS:
        if f not in J or J[f] in ('', None, []):
            if f != 'human_verified' or f not in J:
                fails.append('json field missing or empty: ' + f)
    for f in EN_FIELDS:
        if not isinstance(J.get('en'), dict) or f not in J['en']:
            fails.append('json en.%s missing (build.py needs it; run fill_row.py)' % f)

    ref_i = sec(REFS)[0] if REFS in pos else len(lines)
    app_i = sec(APPX)[0] if APPX in pos else ref_i
    app_lines = lines[app_i:ref_i]
    appx = '\n'.join(app_lines)

    # --- process disclaimers (everywhere except the reference list)
    for i, l in enumerate(full[:ref_i]):
        for m in BANNED.finditer(l):
            fails.append('line %d: process disclaimer not allowed: "%s"' % (i + 1, m.group(0)))

    # --- references
    body, reflines = lines[:ref_i], lines[ref_i:]
    defs = {}
    for l in reflines:
        m = re.match(r'^(\d+)\. <a id="ref-(\d+)"></a>(.*)$', l)
        if m:
            if m.group(1) != m.group(2):
                fails.append('reference %s has anchor ref-%s' % m.group(1, 2))
            defs[int(m.group(1))] = m.group(3)
    cited = []
    for l in body:
        for m in CIT.finditer(l):
            if m.group(1) != m.group(2):
                fails.append('citation [%s] links to #ref-%s' % m.group(1, 2))
            n = int(m.group(1))
            if n not in defs:
                fails.append('citation [%d] has no reference entry' % n)
            if n not in cited:
                cited.append(n)
    if re.search(r'(?<!\[)\[\d+\](?!\]|\()', '\n'.join(body)):
        warns.append('bare [n] citation without anchor link found in body')
    for l in full[:ref_i]:  # numbers inside Mermaid count as cited, but cannot carry links
        for n in re.findall(r'\[(\d+)\]', l):
            if int(n) in defs and int(n) not in cited:
                cited.append(int(n))
    order = [int(n) for l in full[:ref_i] for n in re.findall(r'\[(\d+)\](?:\]\(#ref-\d+\))?', l)]
    first = list(dict.fromkeys(n for n in order if n in defs))
    for n in defs:
        if n not in cited:
            fails.append('reference %d is never cited in the body' % n)
    if first != sorted(first):
        k = next(i for i, n in enumerate(first) if n != sorted(first)[i])
        fails.append('reference numbers are not in order of first appearance (from [%d], found where [%d] is expected)' % (first[k], sorted(first)[k]))
    if sorted(defs) != list(range(1, len(defs) + 1)):
        fails.append('reference numbers are not 1..N without gaps')
    for n, t in defs.items():
        if '/source/' in t:
            fails.append('reference %d links into source/' % n)
        if not re.search(r'doi\.org/|arxiv\.org/abs/|https?://', t):
            fails.append('reference %d has no DOI/arXiv/URL link' % n)
        for pid in re.findall(r'/papers/([^/]+)/article\.md', t):
            if a.wiki and not os.path.exists(os.path.join(a.wiki, 'papers', pid, 'article.md')):
                fails.append('reference %d: wiki page papers/%s/article.md does not exist' % (n, pid))
    if re.search(r'\]\([^)]*/source/', md):
        fails.append('a link points into source/')
    bibkeys = re.findall(r'^@\w+\{([^,]+),', bib, re.M)
    jkeys = [r['key'] for r in J.get('references', [])]
    if len(bibkeys) != len(defs):
        fails.append('bib has %d entries, reference list has %d' % (len(bibkeys), len(defs)))
    if jkeys and bibkeys != jkeys:
        fails.append('bib keys and json references differ in content or order')
    if len(set(bibkeys)) != len(bibkeys):
        fails.append('duplicate bib keys')

    # --- slots.json and the 13-components table
    ti, tj = sec(TABLE)
    tbl = lines[ti:tj] if ti is not None else []
    rows = {}
    hdr = None
    for l in tbl:
        if not l.startswith('|'):
            continue
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if hdr is None:
            hdr = [c.lower() for c in cells]; continue
        if re.match(r'^[\s:|-]+$', l.strip().strip('|')):
            continue
        m = re.search(r'\bM(\d{2})\b', cells[0])
        if m:
            rows['M' + m.group(1)] = cells
    if ti is not None:
        for col in ('component', 'this paper', 'usual approach', 'state of the art', 'verdict'):
            if not hdr or not any(col in c for c in hdr):
                fails.append('"## The 13 components" table lacks the column "%s" (Component | This paper | Usual approach (count) | State of the art | Verdict)' % col)
    vcol = next((k for k, c in enumerate(hdr or []) if 'verdict' in c), None)
    audits = [json.load(open(x)) for x in a.audit]
    ahead = []
    for i in range(1, 14):
        m = 'M%02d' % i
        s = S.get(m)
        if not s:
            fails.append('slots.json lacks ' + m); continue
        for k in ('choice', 'field', 'n', 'matched', 'matched_tier', 'verdict', 'note'):
            if k not in s:
                fails.append('%s lacks key %s' % (m, k))
        v = s.get('verdict')
        if v == 'missing':
            warns.append('%s verdict "missing" is legacy: use not_reported or not_applicable' % m)
        elif v not in VERDICTS:
            fails.append('%s verdict %r not in %s' % (m, v, sorted(VERDICTS)))
        tier = str(s.get('matched_tier', ''))
        if not tier.startswith(TIERS):
            fails.append('%s matched_tier must start with one of %s' % (m, TIERS))
        if v == 'ahead':
            ahead.append(m)
        if ti is not None:
            if m not in rows:
                fails.append('%s has no row in "## The 13 components"' % m)
            elif vcol is not None and v in VERDICTS:
                cell = rows[m][vcol].lower() if vcol < len(rows[m]) else ''
                if v.replace('_', ' ') not in cell.replace('_', ' '):
                    fails.append('%s: table verdict "%s" differs from slots.json "%s"' % (m, cell, v))

    # --- audits: counts agree, and the Appendix states rule, counts and recall per topic
    def norm(x):
        return re.sub(r'[\s_/-]+', ' ', x.lower()).strip()
    appn = norm(appx)
    starts = {}
    for au in audits:
        k = appn.find(norm(au['topic']))
        if k >= 0:
            starts[au['topic']] = k
    refpids = set()
    for r in J.get('references', []):
        x = r.get('pid')
        refpids.update(x if isinstance(x, list) else [x] if x else [])
    def ledger_counts(au):
        c = au.get('counts') or {}
        ua = au.get('usual_approach') or {}
        lt = au.get('ledger_tally') or {}
        xs = [c.get('slot_filled_unique'), c.get('string_match_unique'), ua.get('n'), ua.get('n_confirmed'), ua.get('population_unique')]
        xs += [d.get('n') for d in (lt.get('design_values') or []) + (lt.get('pattern_counts') or [])]
        return [x for x in xs if isinstance(x, (int, float))]
    segs = {}
    for au in audits:
        if not au.get('wiki_commit'):
            warns.append('audit %s has no wiki_commit' % au['topic'])
        ua, sota, lt = au.get('usual_approach') or {}, au.get('state_of_the_art') or {}, au.get('ledger_tally') or {}
        if not ((ua.get('design') and (ua.get('n') is not None or ua.get('n_confirmed') is not None))
                or lt.get('design_values') or lt.get('pattern_counts')):
            fails.append('audit "%s": no usual_approach {design, n, tier, pids} and no ledger tally (run slot_candidates.py)' % au['topic'])
        if ua.get('tier') and not str(ua['tier']).startswith(('slot-filled', 'slot_filled', 'pattern', 'confirmed')):
            fails.append('audit "%s": usual_approach tier %r is not slot-filled / pattern match' % (au['topic'], ua['tier']))
        if not (sota.get('value') or au.get('sota_candidates')):
            warns.append('audit "%s": no state_of_the_art and no sota_candidates (give --metric-pattern)' % au['topic'])
        if au['topic'] not in starts:
            fails.append('Appendix does not name audited topic "%s"' % au['topic']); continue
        k = starts[au['topic']]
        nxt = min([v for v in starts.values() if v > k] + [len(appn)])
        seg = appn[k:nxt]
        segs.setdefault(au['slot'], []).append((au, seg))
        if 'inclusion rule' not in seg:
            fails.append('Appendix, topic "%s": no inclusion rule' % au['topic'])
        if not any(has_num(seg, x) for x in ledger_counts(au)):
            fails.append('Appendix, topic "%s": no ledger count from the audit (slot-filled / pattern match, unique studies)' % au['topic'])
        kr = (au.get('known_item_recall') or {}).get('recall')
        if isinstance(kr, (int, float)) and not has_num(seg, kr):
            warns.append('Appendix, topic "%s": known-item recall %s from the audit not stated' % (au['topic'], kr))
    for m in ahead:
        mine = segs.get(m, [])
        if not mine:
            fails.append('%s is "ahead" without an audit for that slot named in the Appendix' % m); continue
        priors = {r['pid'] for au, _ in mine for r in (au.get('read_fulltext') or []) if r.get('role') == 'prior' and r.get('loc')}
        if not priors:
            fails.append('%s is "ahead" but the audit lists no deciding prior read in full (read_fulltext, role "prior")' % m)
        for x in sorted(priors - refpids):
            fails.append('%s is "ahead": deciding prior %s was read but is not cited in the review' % (m, x))
    reads = {r['pid'] for au in audits for r in (au.get('read_fulltext') or []) if r.get('role') != 'target'}
    if len(reads) > a.max_read:
        warns.append('%d papers read in full besides the target (budget %d)' % (len(reads), a.max_read))
    if app_i < ref_i:
        if 'inclusion rule' not in appn:
            fails.append('Appendix states no inclusion rule')
        if not re.search(r'slot filled|pattern match', appn):
            fails.append('Appendix states no ledger counts (slot-filled / pattern match)')

    # --- novelty / absence wording must point to the Appendix
    for i, l in enumerate(lines[:app_i]):
        if l.startswith('#'):
            continue
        m = FIRST.search(l)
        if m and not re.search(r'\bAppendix\b', l):
            fails.append('line %d: novelty / absence wording ("%s") without reference to the Appendix' % (i + 1, m.group(0)))

    # --- each component section opens with **Usual approach:** and **State of the art:**
    gi, gj = sec('Against the field, component by component')
    if gi is not None:
        h3 = [k for k in range(gi + 1, gj) if lines[k].startswith('### ')]
        if not h3:
            fails.append('"## Against the field, component by component" has no ### component section')
        for x, k in enumerate(h3):
            end = h3[x + 1] if x + 1 < len(h3) else gj
            if not re.search(r'\bM\d{2}\b', lines[k]):
                warns.append('line %d: component section heading does not name its slot (Mxx)' % (k + 1))
            ne = [(q, lines[q].strip()) for q in range(k + 1, end) if lines[q].strip()]
            if len(ne) < 2 or not ne[0][1].startswith('**Usual approach:**') or not ne[1][1].startswith('**State of the art:**'):
                fails.append('line %d: component section must open with "**Usual approach:**" then "**State of the art:**"' % (k + 1))
            elif not re.search(r'\b(?:19|20)\d\d\b', ne[1][1]):
                warns.append('line %d: State of the art line gives no year' % (ne[1][0] + 1))

    # --- section-level checks (warnings)
    vi, vj = sec('Verdict')
    if vi is not None:
        vt = ' '.join(l for l in lines[vi + 1:vj] if l.strip())
        nsent = len([x for x in re.split(r'(?<=[.!?])\s+(?=[A-Z\[])', vt) if x.strip()])
        if nsent > 6:
            warns.append('Verdict has %d sentences (at most 6)' % nsent)
        for m in HEDGE.finditer(vt):
            warns.append('Verdict hedges ("%s"): state the position plainly' % m.group(0))
    ni, nj = sec('What the field needs next')
    if ni is not None:
        items = [l for l in lines[ni + 1:nj] if re.match(r'^\s*(?:[-*]|\d+\.)\s', l)]
        if not 2 <= len(items) <= 4:
            warns.append('"What the field needs next" has %d list items (2-4)' % len(items))
        for l in items:
            if not re.search(r'\bM\d{2}\b', l):
                warns.append('"What the field needs next" item not tied to a component (Mxx): %s' % l.strip()[:60])
    ci, cj = sec('Where the claims outrun the evidence')
    if ci is not None:
        for k, l in enumerate(lines[ci + 1:cj]):
            if l.strip() and not l.startswith('#') and not LOC.search(l):
                warns.append('line %d: claims-outrun item without citation or location in the paper' % (ci + k + 2))

    # --- chronology labels
    for r in J.get('references', []):
        t = str(r.get('timing') or '').strip('[]')
        if t in ('concurrent', 'later'):
            n = r['n']
            if not any(('[[%d]]' % n) in l and re.search(r'\b' + t + r'\b', l, re.I) for l in body):
                warns.append('reference %d is [%s] but no citing line says so' % (n, t))

    # --- every number traceable to notes.json, an audit, slots.json or verdict.json
    N = json.load(open(a.notes))
    if not isinstance(N.get('entries'), list) or not N['entries']:
        fails.append('notes.json has no entries')
    src = [json.dumps(N, ensure_ascii=False), json.dumps(S, ensure_ascii=False)]
    for au in audits:
        src.append(json.dumps({k: v for k, v in au.items() if k != 'candidates'}, ensure_ascii=False))
    Vd = {}
    if a.verdict:
        Vd = json.load(open(a.verdict))
        src.append(json.dumps(Vd, ensure_ascii=False))
        if not Vd.get('short') or len(Vd['short']) > 200:
            fails.append('verdict.json "short" missing or over 200 characters')
    def nums(x):
        x = re.sub(r'\[\[\d+\]\]\(#ref-\d+\)', ' ', x)
        x = re.sub(r'\bM\d{2}\b|\[\d+\]|https?://\S+|doi:\S+|arXiv:\S+', ' ', x)
        return [float(y.replace(',', '')) for y in re.findall(r'(?<![\w.])(\d{1,3}(?:,\d{3})+|\d+(?:\.\d+)?)(?![\w])', x)]
    known = set()
    for t_ in src:
        for y in nums(t_):
            known.add(round(y, 6))
    ti2, tj2 = sec(TABLE)
    untr = []
    for i, l in enumerate(lines[:ref_i]):
        if i <= first_h2 - 1 or (ti2 is not None and ti2 <= i < tj2) or l.startswith('#'):
            continue
        for snt in re.split(r'(?<=[.!?])\s+', l):
            if '(inference)' in snt:
                continue
            for y in nums(snt):
                if (y == int(y) and (y <= 13 or 1900 <= y <= 2099)) or round(y, 6) in known:
                    continue
                untr.append((i + 1, y))
    for ln, y in untr:
        fails.append('line %d: number %g is in no notes.json entry, audit or slots.json (mark it "(inference)" if it is the reviewer\'s calculation)' % (ln, y))

    # --- length
    start = h2[0] if h2 else 0
    nchar = len(re.sub(r'\[\[(\d+)\]\]\(#ref-\d+\)', r'[\1]', '\n'.join(l for l in lines[start:app_i])))
    if nchar < a.min_chars or nchar > a.max_chars:
        fails.append('body (first heading to Appendix) is %d characters (allowed %d-%d)' % (nchar, a.min_chars, a.max_chars))

    # --- overreach (audit of 971 evaluator fixes: 60 overreach + 52 absence/novelty fixes): absolute wording needs a
    # citation, a paper location, an Appendix number or "(inference)" in the same sentence
    for i, l in enumerate(lines[:ref_i]):
        if i <= first_h2 - 1 or (ti2 is not None and ti2 <= i < tj2) or l.startswith('#') or l.startswith('|'):
            continue
        for snt in re.split(r'(?<=[.!?])\s+', l):
            m = ABSOLUTE.search(snt)
            if m and not GROUND.search(snt):
                warns.append('line %d: absolute wording "%s" with no citation, location or Appendix number in the sentence' % (i + 1, m.group(0)))
    if a.strict:
        fails.extend(warns); warns.clear()
    for w in warns:
        print('WARN', w)
    for f in fails:
        print('FAIL', f)
    print('summary: %d FAIL, %d WARN, references %d, body chars %d' % (len(fails), len(warns), len(defs), nchar))
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
