#!/usr/bin/env python3
"""Number the citations of a draft and build the reference list, the .bib and the references JSON.

  build_refs.py --draft draft.md --refs refs.json --slug SLUG --out-dir DIR --target-date YYYY-MM \
      [--wiki WIKI] [--reviews-jsonl silent-speech-review/data/reviews.jsonl] \
      [--wiki-url URL_PREFIX] [--review-url URL_PREFIX]

Draft cites with [@key] or [@key1; @key2] (also inside Mermaid blocks, where plain [n] is written). Output SLUG.md has [[n]](#ref-n) in order of first appearance and
a "## References" section; SLUG.bib uses the same order and keys; SLUG.refs.json is the "references" array.
Each reference links DOI/arXiv, the public wiki page papers/<id>/article.md (never source/) and, when the paper
is in reviews.jsonl, its public review ("[review]"). Works first public within +-6 months of --target-date get [concurrent],
later ones [later]. Exit 1 on unknown keys, uncited entries, a wiki id with no article.md, or an entry with no DOI/arXiv/URL.

refs.json entry: {"key","pid" (str or list),"type","authors":["Family, Given"],"title","container","year",
 "volume","number","pages","doi","arxiv","url","first_public":"YYYY-MM[-DD]","note","meta_source"}
"""
import argparse, json, os, re, sys

WIKI_URL = 'https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/'
REVIEW_URL = 'https://github.com/supernaiter/silent-speech-review/tree/main/reviews/'
CITE = re.compile(r'\[@([^\]]+)\]')


def ym(d):
    m = re.match(r'(\d{4})(?:-(\d{2}))?', str(d or ''))
    return (int(m.group(1)), int(m.group(2)) if m.group(2) else None) if m else (None, None)


def timing(ref, target):
    """prior -> None; within +-6 months -> 'concurrent'; later -> 'later'; '?' (date unresolved) when the month is needed but missing."""
    (y, mo), (ty, tmo) = ym(ref.get('first_public')), ym(target)
    if y is None or ty is None:
        return '?'
    if mo is None or tmo is None:
        return 'later' if y > ty + 1 else (None if y < ty - 1 else '?')
    d = (y * 12 + mo) - (ty * 12 + tmo)
    return 'concurrent' if abs(d) <= 6 else ('later' if d > 0 else None)


def short_author(a):
    fam, _, giv = a.partition(',')
    ini = ' '.join(w[0] + '.' for w in re.split(r'[\s]+', giv.strip()) if w)
    return (fam.strip() + ', ' + ini).strip(', ')


def authors_md(au):
    s = [short_author(re.sub(r'[{}]', '', a)) for a in au[:6]]
    return ', '.join(s) + (', et al.' if len(au) > 6 else '')


def pids(r):
    p = r.get('pid') or []
    return [p] if isinstance(p, str) else list(p)


def md_entry(r, n, a, reviews, with_links=True):
    out = '%s “%s.” ' % (authors_md(r.get('authors', [])), r['title'].rstrip('.'))
    if r.get('container'):
        out += ('*%s*, ' if with_links else '%s, ') % r['container']
    out += str(r.get('year', 'n.d.'))
    if r.get('volume'):
        out += ', %s%s' % (r['volume'], '(%s)' % r['number'] if r.get('number') else '')
    if r.get('pages'):
        out += ', %s' % str(r['pages']).replace('--', '–')
    out += '.'
    if r.get('doi'):
        out += (' doi:[%s](https://doi.org/%s).' if with_links else ' doi:%s.') % ((r['doi'],) * (2 if with_links else 1))
    if r.get('arxiv'):
        out += (' arXiv:[%s](https://arxiv.org/abs/%s).' if with_links else ' arXiv:%s.') % ((r['arxiv'],) * (2 if with_links else 1))
    if r.get('url') and not r.get('doi') and not r.get('arxiv'):
        out += ' <%s>' % r['url'] if with_links else ' ' + r['url']
    if r.get('note'):
        out += ' ' + r['note']
    if r.get('_timing'):
        out += ' [%s]' % r['_timing']
    if with_links:
        slug = reviews.get((r.get('doi') or '').lower()) or reviews.get(re.sub(r'v\d+$', '', r.get('arxiv') or ''))
        if slug:
            out += ' [review](%s%s)' % (a.review_url, slug)
        for p in pids(r):
            out += ' [wiki: %s](%s%s/article.md)' % (p, a.wiki_url, p)
    return out


def bib_entry(r):
    f = [('author', ' and '.join(r.get('authors', []))), ('title', '{' + r['title'] + '}')]
    cont = {'article': 'journal', 'inproceedings': 'booktitle', 'phdthesis': 'school', 'book': 'publisher'}.get(r.get('type'))
    if cont and r.get('container'):
        f.append((cont, r['container']))
    elif r.get('container'):
        f.append(('howpublished', r['container']))
    for k in ('year', 'volume', 'number'):
        if r.get(k):
            f.append((k, str(r[k])))
    if r.get('pages'):
        f.append(('pages', str(r['pages']).replace('–', '--')))
    if r.get('doi'):
        f.append(('doi', r['doi']))
    if r.get('arxiv'):
        f += [('eprint', re.sub(r'v\d+$', '', r['arxiv'])), ('archivePrefix', 'arXiv')]
    if r.get('url') or (r.get('arxiv') and not r.get('doi')):
        f.append(('url', r.get('url') or 'https://arxiv.org/abs/' + r['arxiv']))
    if r.get('note'):
        f.append(('note', r['note']))
    body = ',\n'.join('  %s = {%s}' % (k, v) for k, v in f if v)
    return '@%s{%s,\n%s\n}\n' % (r.get('type') or 'misc', r['key'], body)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    for x in ('--draft', '--refs', '--slug', '--out-dir', '--target-date'):
        p.add_argument(x, required=True)
    p.add_argument('--wiki', default=os.environ.get('WIKI_DIR'), help='wiki clone (default: $WIKI_DIR)'); p.add_argument('--reviews-jsonl')
    p.add_argument('--wiki-url', default=WIKI_URL); p.add_argument('--review-url', default=REVIEW_URL)
    a = p.parse_args()
    refs = {r['key']: r for r in json.load(open(a.refs))}
    draft = open(a.draft).read()
    reviews = {}
    if a.reviews_jsonl:
        for l in open(a.reviews_jsonl):
            r = json.loads(l)
            for k in ((r.get('doi') or '').lower(), r.get('arxiv_id') or ''):
                if k:
                    reviews[re.sub(r'v\d+$', '', k)] = r['slug']
    order, errs = [], []

    def repl(m):
        ns = []
        for k in re.split(r'\s*;\s*', m.group(1)):
            k = k.strip().lstrip('@')
            if k not in refs:
                errs.append('unknown key: ' + k); continue
            if k not in order:
                order.append(k)
            n = order.index(k) + 1
            ns.append('[[%d]](#ref-%d)' % (n, n))
        return ', '.join(ns)

    def plain(m):  # inside fenced blocks (Mermaid) links do not render: write [n] only
        return re.sub(r'\[\[(\d+)\]\]\(#ref-\d+\)', r'[\1]', repl(m))

    parts = re.split(r'(^```.*?^```[^\n]*$)', draft, flags=re.S | re.M)
    body = ''.join(CITE.sub(plain if i % 2 else repl, x) for i, x in enumerate(parts))
    for r in refs.values():  # notes may cite other references
        if r.get('note'):
            r['note'] = CITE.sub(repl, r['note'])
    errs += ['never cited: ' + k for k in refs if k not in order]
    lines, bib, out = [], [], []
    for n, k in enumerate(order, 1):
        r = refs[k]
        r['_timing'] = None if n == 1 else timing(r, a.target_date)
        if r['_timing'] == '?':
            print('WARN %s: date unresolved: first_public needs YYYY-MM to tell prior / concurrent / later (no label written)' % k)
            r['_timing'] = None
        if r.get('meta_source') not in ('paper_text', None):
            print('WARN %s: bibliographic data from %s, not from the paper text' % (k, r['meta_source']))
        if not (r.get('doi') or r.get('arxiv') or r.get('url')):
            errs.append('%s: no doi/arxiv/url; add a locator (publisher page, proceedings URL)' % k)
        for pid in pids(r):
            if a.wiki and not os.path.exists(os.path.join(a.wiki, 'papers', pid, 'article.md')):
                errs.append('%s: no papers/%s/article.md in wiki' % (k, pid))
        lines.append('%d. <a id="ref-%d"></a>%s' % (n, n, md_entry(r, n, a, reviews)))
        bib.append(bib_entry(r))
        out.append({'n': n, 'key': k, 'pid': '; '.join(pids(r)), 'timing': r['_timing'],
                    'citation': md_entry(r, n, a, reviews, with_links=False)})
    if errs:
        print('\n'.join('FAIL ' + e for e in errs)); sys.exit(1)
    base = os.path.join(a.out_dir, a.slug)
    head = '\n\n## References\n\nNumbered by first citation. BibTeX in the same order and keys: [%s.bib](%s.bib).\n\n' % (a.slug, a.slug)
    open(base + '.md', 'w').write(body.rstrip() + head + '\n'.join(lines) + '\n')
    open(base + '.bib', 'w').write('%% Entry order = reference numbers [1]-[%d] in %s.md. UTF-8.\n\n' % (len(order), a.slug) + '\n'.join(bib))
    json.dump(out, open(base + '.refs.json', 'w'), ensure_ascii=False, indent=1)
    print('references %d, with review link %d, concurrent %d, later %d' % (
        len(order), sum('[review](' in l for l in lines), sum(o['timing'] == 'concurrent' for o in out), sum(o['timing'] == 'later' for o in out)))


if __name__ == '__main__':
    main()
