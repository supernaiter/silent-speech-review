# Triage of the evaluation (2026-11-28)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 (major) heads 0.98 at four depths; depths part of homophene mechanism | applied | Target Table 2: h=1 87.53%, h=8 88.51% at four levels; levels 1 to 4 at h=8 87.22% to 88.51%; Sec. 3.3 "another key for distinguishing the homophenes" (t8, t33, t34) | Verdict; M06 paragraph rewritten (interaction stated, "gain away from the heads" dropped); slots M06 note; verdict.json. M06 verdict unchanged (standard): single runs on one dataset, no seeds |
| 2 Feng 55.7% uses word boundaries | applied | Feng Table 5: 48.0% without, 55.7% with word boundaries (c6, c7) | M12 State of the art now uses 48.0%; omission criticism removed from the LRW-1000 bullet |
| 3 LiRA missing from M02 prior count | applied | LiRA 2021-06 regresses PASE+ features (c31); pattern population of 3 misses it | M02 Usual approach "of 4 earlier decoders, 3 distil, LiRA regresses"; Appendix M02 recount (4: distillation 3, regression 1, memory 0); audit note; slots n=4, matched 3 |
| 4 ICCV memory as same-group precedent | applied | Target uses Kim et al. 2021b as single-memory baseline (Table 1, t29); ICCV 2021-10 inside the window | [concurrent] label kept; Verdict, M02 and Appendix M02 name it as the same group's design and the target's baseline |
| 5 M06 state of the art on the slot's own step | applied | SyncVSR Sec. 4 evaluates all word pairs by grapheme edit distance and notes the target examined a subset (c32); Fig. 3 caption (c33) | M06 State of the art and table row rewritten; overall accuracy kept as context only. Fig. 3 values are figure-only, so no number is given |
| 6 LRS2 baseline mismatch | applied | Target Sec. 4.2 "same architecture as the proposed method except for MVM" (t89); Table 5 label Afouras 2018 49.8 (t57); Hearing Lips lists TM-seq2seq at 49.8% (c35) | LRS2 bullet rewritten; new question to the authors; field-needs M12 item |
| 7 M06 population and selection bias | applied | Prior LM list contained cvf-prajwal20-lip2wav (video-to-speech), isca-liu18h_cuedspeech; arxiv-1611.06986 is audio-visual recognition | Removed all three; recount 41 decoders, viseme 24, LM 19; bias stated in text and Appendix; tier labelled mention count |
| 8 0.906 is same-sound addressing, not a homophene failure | applied | ICCV Sec. 4.3: about/amount share /aU/ (c13, c14) | Figure removed from M06 |
| 9 LiRA conditions | applied | SyncVSR Table 1 lists LiRA at 590 h (c34); LiRA pre-trains on LRS3 (c30) | M02 State of the art |
| 10 SyncVSR LRW-1000 word boundary | applied | SyncVSR caption defines WB for the LRW column only (c37) | M06 State of the art "word boundaries not stated" |
| 11 M12 usual approach and all-years count | applied | Tables 4-5 are LRW-1000 and LRS2; published count was all years | M12 Usual approach rewritten with a dated, filtered mention count (45 prior decoders, 16 mention repetition); "Tables 1-3, 6"; Appendix M12 dated counts |
| 12 Table 6 denominator "state plainly" | partly applied | The LRW paper guarantees only "at least 40" test occurrences per word (c36), so 50 cannot be stated plainly | Bullet cites [LRW] for at least 40 and keeps "about one clip (inference)"; Fig. 3 single-pair note dropped for length |
| 13 memory's own effect +0.8 | applied | Table 1: 86.1 to 86.9 single memory (t28, t29) | M02 paragraph: +0.8 (6% less error) single memory, 17% full MVM |
| 14 "remain similar"; process note in ref 1; bibliographic data | applied | Target Sec. 4.2 (t90); pages 1174-1182 from SyncVSR's reference list (c38); DOI not verifiable in the available sources | M13 slot note credits the authors; "Read as" note removed from reference 1; pages added, DOI not added |

Counts: 13 applied, 1 partly applied, 0 rejected. Verdict changes: none (M02, M06, M12 stay standard).
