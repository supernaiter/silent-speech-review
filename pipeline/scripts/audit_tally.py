#!/usr/bin/env python3
"""Tally a topic audit from its ledger counts (no candidate reading). Prints the tiers and the reference points.

  audit_tally.py topic.audit.json [--write]

Reports: slot-filled and pattern-match counts (unique studies), usual_approach (design, n, tier), the chosen
state_of_the_art (or the top ledger sota candidate), the papers read in full for this topic (read_fulltext), and
optional known-item recall. Legacy audits with include decisions also report confirmed_unique; quotes on legacy
includes are not required.
Fails (exit 1) when: no inclusion_rule (the topic boundary); no usual_approach and no ledger_tally; a
read_fulltext entry without pid / role / loc / quote (role: target | sota | prior); a state_of_the_art that is
not backed by a read_fulltext entry of role "sota" with the same pid.
"""
import json, sys

UA_TIERS = ('slot-filled', 'pattern match', 'confirmed')
ROLES = ('target', 'sota', 'prior')


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
        print(__doc__); sys.exit(0 if len(sys.argv) > 1 else 2)
    path = sys.argv[1]
    a = json.load(open(path))
    cs = a.get('candidates', [])
    errs = []
    if not a.get('inclusion_rule'):
        errs.append('inclusion_rule is empty (write the topic boundary and its boundary cases)')
    ua = a.get('usual_approach') or {}
    lt = a.get('ledger_tally') or {}
    if not ua and not (lt.get('design_values') or lt.get('pattern_counts')):
        errs.append('no usual_approach and no ledger_tally (run slot_candidates.py)')
    if ua and ua.get('tier', 'confirmed' if 'n_confirmed' in ua else None) not in UA_TIERS:
        errs.append('usual_approach tier %r not in %s' % (ua.get('tier'), UA_TIERS))
    reads = a.get('read_fulltext') or []
    for r in reads:
        if not (r.get('pid') and r.get('role') in ROLES and r.get('loc') and r.get('quote')):
            errs.append('read_fulltext entry %r lacks pid / role (%s) / loc / quote' % (r.get('pid'), '|'.join(ROLES)))
    sota = a.get('state_of_the_art') or {}
    if sota.get('pid') and not any(r.get('pid') == sota['pid'] and r.get('role') == 'sota' for r in reads):
        if not sota.get('confirmed_in_text'):
            errs.append('state_of_the_art %s is not confirmed in source text (add a read_fulltext entry, role "sota")' % sota['pid'])
    inc = [c for c in cs if c.get('decision') == 'include']
    sc = (a.get('ledger_tally') or {}).get('sota_candidates') or a.get('sota_candidates') or []
    t = {'slot_filled_unique': a['counts']['slot_filled_unique'],
         'string_match_unique': a['counts']['string_match_unique'],
         'fulltext_only_folders': a['counts'].get('fulltext_only_folders', 0),
         'usual_approach': {k: ua.get(k) for k in ('design', 'n', 'tier', 'population_unique')} if ua else None,
         'state_of_the_art': sota or (dict(sc[0], source='ledger candidate, not yet confirmed') if sc else None),
         'read': len({r['pid'] for r in reads}),
         'read_prior': sorted({r['pid'] for r in reads if r.get('role') == 'prior'}),
         'unread': sum(1 for c in cs if c.get('decision') not in ('include', 'exclude')),
         'confirmed_unique': len({c['key'] for c in inc}),
         'known_item_recall': (a.get('known_item_recall') or {}).get('recall')}
    print(json.dumps(t, ensure_ascii=False, indent=1))
    if '--write' in sys.argv:
        a['tally'] = t
        json.dump(a, open(path, 'w'), ensure_ascii=False, indent=1)
    for e in errs:
        print('FAIL', e)
    sys.exit(1 if errs else 0)


if __name__ == '__main__':
    main()
