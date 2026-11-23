# Triage: NasoVoce component review

Date: 2026-11-23. Input: `nasovoce.eval.md` (24 claim rows, 10 required fixes). Each fix was checked against `notes.json` and, where a number, quote or bibliographic fact was at stake, against the source passage in the wiki. Claim-check rows are covered under the fix that addresses them.

Counts: 2 correct, 7 partly correct, 1 wrong, 0 unverifiable as a whole (parts of fixes 3, 4, 7 and 9 that rest on works outside the wiki are unverified and were not adopted). Applied: 9 of 10.

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | partly correct; applied | [2] is not digital mixing: its Experiment 2 played tank noise in the recording booth during speech production (Sec. 4; new entry g7), and its vehicle task recorded at about 100 dB SPL (Sec. 1). [4] recorded noise through both microphones and superimposed it on each channel (Secs. 3, 4.1; n2, n6), so the conducted channel sees noise, but not during speech. "Usually" overstated a 44 against 15 split of 123 (pattern match). | Verdict last sentence now gives the split and says the closest works expose the conducted sensor to noise; verdict.json position; row fields position_in_field and canon_before via fix_row.py. |
| 2 | partly correct; applied | "typical of the field" named the yardstick required by the verdict rule, not a description of the paper; the label read as a contradiction. | M12 closing line: "Verdict: behind typical practice in the field (44 against 15, Appendix)." |
| 3 | partly correct; applied in part | "Date from 2004" asserted an origin the ledger does not establish. The suggested 2003 letter and 2003 workshop paper are not in the wiki and were not read, so they are not cited. | Verdict now says such pairs "were in use by 2004"; same in verdict.json and canon_before. The 2003 works are listed under open items in verification_status. |
| 4 | partly correct; applied in part | The 2004 figure is the best fusion-for-recognition result confirmed in its source (audit state of the art, unchanged), not the best fusion work today. The 2020 and 2022 deep fusion enhancers are cited by the target (Sec. 2; t87, t88) but are not in the wiki, so no metric or value is taken from them. | M06 State of the art: the 2004 result is labelled the best confirmed recognition result; deep fusion beating single-sensor enhancement is added with two new references (bibliographic data from the target's reference list). Audit and topic tally untouched. |
| 5 | wrong; not applied | Sec. 4.1 states that the recognizer's encoder and decoder are frozen and used solely as an evaluator during enhancement training (t12), alongside the distillation losses (t11). The claim table had not mapped t12. | Locator "(§4.1)" added to the Verdict sentence; claim row 1 now maps t12. |
| 6 | partly correct; applied | Several quotes already existed but were unmapped (Fig. 7 axis t76; MUSHRA comparator t67). Added and verified: g5 ([2] Table 1, 52.6% WER at 0 dB, combined microphones with compensation), g6 ([2] Sec. 1, vehicle at about 100 dB SPL; a new result of [2], not an earlier study), n5 ([4] Table 1 headers 1ch-BC, 1ch-AC, 2ch; 32.9 is the two-channel U/V error rate and is unrelated to the 32.9% WER of [3]), p3 ([3] Sec. 2.2, four speakers). | notes.json (8 new entries, all quotes found); claim table rows 9, 12, 15, 19, 24, 25; MUSHRA bullet now names the comparator as "the microphone signal with added noise (Fig. 9 caption)". |
| 7 | partly correct; applied in part | [3] supports the throat only. The suggested behind-the-ear counterexample was not read and is not cited. | Verdict: "untested, and for the throat it is contradicted by soft-whisper recognition with a throat microphone [3]". |
| 8 | correct; applied | M09 and M10 are filled in 82 ledger papers, too few for a usual approach (slot notes); the 82 is not copied from M05. M11 has no field-practice count, and the paper states the clean reference but not the test transcripts (t75, t60). | slots.json M09, M10, M11 field, choice and note; verdict values unchanged. |
| 9 | partly correct; applied in part | V-Speech is in the target's reference list (Proc. ACM IMWUT 2(4), Art. 180, 2018) and is described there as a vibration sensor that improves SNR over an air microphone (Sec. 2; t89). Whether it also used a co-located microphone cannot be checked: it is not in the wiki. | M05 Usual approach cites V-Speech and states the departure as fusing it with a co-located microphone, as the target describes it. |
| 10 | correct; applied | Sec. 5.2 reports that the vibration channel alone beats the fused output under very strong noise (t39). The 1,000 against 800 gap has no stated explanation in the paper (t30). | M06 single-input control sentence cites §5.2; the claims bullet now says the 1,000 items "are not reconciled with" the 800 utterances. |

## Reruns

- Steps 6 to 8 rerun with `reviews.jsonl` taken from origin/main: render_review, build_refs (8 references; 3 WARN for bibliographic data taken from the target's reference list), fill_row, then fix_row.py.
- check_review: 0 FAIL, 0 WARN; body 6,952 characters. verify_quotes: 93 found, 0 missing, 16 unchecked. audit_tally: 0 FAIL on all three audits; audits and published tallies unchanged.
- claims.md regenerated and every mapping refilled (40 rows, no unresolved mapping); compact.md regenerated.
- Row fields rewritten through fix_row.py: canon_before, position_in_field, technical_limits, evaluation_limits. No Japanese or Chinese characters in any output.

## Still open

- The two 2003 priors suggested by the evaluator, and the metrics of the 2020 and 2022 deep fusion enhancers, need sources in the wiki before they can be cited with values.
- Whether V-Speech used an air microphone alongside its vibration sensor.
