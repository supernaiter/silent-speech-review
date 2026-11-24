# Evaluation: Knowledge Distilled Ensemble Model for sEMG-based Silent Speech Interface

Date: 2026-11-24
Evaluator: a language model separate from the writer

Input: the evaluator brief and `compact.md` only. No sources, web or wiki were opened. Outside knowledge is marked "unverified" where I cannot locate it.

## Claim checks

| # | Claim (location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Three changed components M02/M06/M13 (Verdict) | Claim row 1, t10, t12, t13, t81, t98 | correct | The quotes support KL+CE distillation from an ensemble, independently trained ResNet1D estimators, and the reported time and size. |
| 2 | "All three are standard: same-modality distillation ... three years earlier [2]" (Verdict) | Row 2; Appendix M02 | insufficient evidence | [2] is born-again (same-architecture) distillation, not an ensemble teacher (w1). The review's own Appendix counts an ensemble teacher in only 2 of 131 studies, one being the target. The deciding prior for distilling an ensemble into one model is not named. See fix 1. |
| 3 | "7.0x smaller, 20.8x faster ... most of it follows from N = 6" (Verdict) | Row 3, t81, t82, t98, t99 | partly wrong | 147.9/21.1 = 7.0 and 2.50/0.12 = 20.8 check out. N = 6 explains about 6x of the size ratio, but only 6x of the 20.8x speed ratio. The remaining ~3.5x is unexplained, so "most of it" holds for size and not clearly for speed. No row quotes N = 6 (insufficient quote). |
| 4 | 85.9% vs 81.2% (Table II), one split, unit unstated, no student without a teacher (Verdict) | Row 4, t22, t24, t14 | correct numbers; wording issue | The numbers match the last column of both rows. "Unseeded" claims more than the evidence, which is only that no seed is reported. "No student trained without a teacher" depends on the student's architecture, which the review says is unknown (Questions). If the student is a ResNet1D, the 81.2% row is that control. See fix 2. |
| 5 | 85.9% not comparable with later subject-independent 85.8% [3]; no device measurement (Verdict) | Row 5, h1, h2, t59, t61 | correct | [3] is correctly labelled later. The confound (different sensor and different split) is handled. |
| 6 | M02 usual approach: 131 studies, audio/ASR/cross-modal teacher 46, compression 20, ensemble 2 "one being the target" | Row 6; Appendix M02 | insufficient evidence | The Appendix label is "audio or ASR teacher 46", with no "cross-modal". Nothing in the Appendix supports "one being the target". The counts are labelled "pattern match", but 46 > 22 (the pattern-match total), so they must come from the 131 full-text set. The label should say so. |
| 7 | [2]: 85.3% teacher to 87.9% student, LRW 500 words; Table 3 84.4% / 85.3% at 9.3 M with and without distillation | Row 7, w2, w3, w5, w8, w10 | correct / insufficient quote | Table 1 values and LRW size match. The Table 3 quotes do not show which row is distilled (insufficient quote for the with/without labels). |
| 8 | 4.7-point gain over ResNet1D (inference) | Row 8 | correct | 85.9 − 81.2 = 4.7. |
| 9 | 82.9% on 32 sEMG words with word HMMs [4] | Row 9, c31, c32 | insufficient quote | The quote is a bare row ("Words 64.8 78.1 71.2 82.9") with no column header. The condition behind 82.9 (best setup, speaker or session) is not shown. c32 says "32 English expressions", not words. |
| 10 | M06 state of the art: CVOS [3] 85.8% on 26 NATO words | Row 10, h1 | correct number; framing issue | The number matches. It is a neck strain sensor under a different protocol, so it is a same-vocabulary reference rather than the best decoder for closed-vocabulary word classification. Higher closed-vocabulary sEMG figures exist, for example [8] at 96% on 10 words, though under a random split. |
| 11 | N sweep: N = 4 best teacher 88.0%, worst student 83.2% at T = 5 (Table III) | Row 11, t26 | insufficient quote | The quote "4 88.0 83.2 84.5" gives no column headers, so neither T = 5 nor the other N rows that "best" and "worst" need are shown. 88.0 − 83.2 = 4.8 is consistent with the authors' t32. |
| 12 | M13 usual: 24 of 30 off-body with no latency or power figure | Row 12; Appendix | correct (tally) | Accepted as an exact tally. |
| 13 | SilentWear [5]: 15k params, 2.47 ms, 63.9 µJ, 20.5 mW total | Row 13, s1–s3 | correct | All values are in the quotes. [later] is correct (arXiv 2603). |
| 14 | CVOS 12.4 MB to 3.6 MB, "at a cost of 85.8% to 82%" | Row 13, h3 | insufficient quote | The quote is truncated at "(85.8%", so 82% is not shown. The source frames the result as "maintaining model performance". |
| 15 | 147.9/6 ≈ 24.7 MB per estimator, student "roughly one backbone" | Row 14, t98, t99 | arithmetic correct; internal tension | Per backbone, the time is 2.50/6 ≈ 0.42 ms (inference), but the student takes 0.12 ms. A model of about backbone size running 3.5x faster than one backbone contradicts "roughly one backbone", or points to a timing artefact (batch or voting overhead). The review should say this. |
| 16 | sEMG recognition on Android in 2013 [6] | Row 14, c27 | correct | — |
| 17 | M05 usual approach: 8 and 4 channels, 2 studies each of 17 | Row 15; Appendix | correct tally; weak as "usual" | Four of 17 studies do not make a usual approach. The plain statement is "no dominant channel count". |
| 18 | Zhu [7]: ten electrodes from 120, 86%, ten English digits | Row 16, c6, c9, c10 | insufficient quote | 120 channels and 86% are quoted. "Ten electrodes" and "ten digits" are not. |
| 19 | Tang [8]: four textile electrodes, 96%, ten words, random split | Row 16, c14–c16 | insufficient quote / possible misread | 96%, 10 words and the 80/20 random split are quoted. c16 mentions "4 subjects", not 4 electrodes, so check that subjects were not read as electrodes. |
| 20 | Seven classes below F1 0.80 (Table IV); three muscles concession (§V.B) | Row 17, t42, t83 | correct, wrong locator | Seven words are listed (Charlie, Delta, Golf, India, Quebec, Romeo, Zulu). The quote is §V.A text, not Table IV. |
| 21 | M12 usual: 65 speaker-disjoint, 58 random/k-fold of 143; Lu [9] 80/20 per category | Row 18, c1 | correct | — |
| 22 | 3,900 samples, five male speakers, 4:1:1, ten repetitions per trial | Row 20, t1, t2, t5, t14 | correct | 30 × 26 × 5 = 3,900. "Consecutive" is a mild inference from t5. |
| 23 | "Negligible 0.1%" is one pair; N = 4 loses 4.8 points | Row 21, t32, t33 | correct; attribution | The authors report the 4.8% loss themselves (t32). The review should credit them rather than present it as its own counterpoint. |
| 24 | Spelling any word untested; fuzzy matching is future work | Row 22, t8, t46, t55 | correct | — |
| 25 | Needs next M12: cross-speaker, female speakers | Row 23, t45 | correct; attribution | The authors name inter-subject and inter-gender domain shift as future work (t45). Credit it. |

Chronology: [3], [5] and [8] are labelled later and are used only as later references, not as missed citations. That is fair. [2] is given as "(prior, 2020)" in the text and as ICASSP 2021 in the reference list. Both dates precede the target, but the text should use one year or say "arXiv 2020, ICASSP 2021".

Strongest confound: the student's architecture and capacity are not stated, and no seeds or repeats are reported. The review handles this in M02 and in the Questions, but contradicts itself (see fix 2). A second confound is the GPU timing basis of the 20.8x figure, which is only half handled (fixes 3 and 4).

## Required fixes (by impact)

1. **M02 verdict and Verdict paragraph.** The "standard" verdict rests on [2], which is born-again single-teacher distillation, while the review's own Appendix finds an ensemble teacher in 2 of 131 studies. Name the deciding prior for ensemble-to-single-model distillation: Hinton, Vinyals and Dean, "Distilling the Knowledge in a Neural Network", arXiv:1503.02531, 2015, which distils an ensemble, including a speech acoustic model, into one network (unverified locator). Alternatively, explain why the ensemble aspect does not change the verdict.
2. **Student without a teacher.** The review says no such control exists, yet treats the student as "roughly one backbone" and asks for its architecture. State instead that the student's architecture is not reported. If it is a ResNet1D, the 81.2% row is the no-teacher control and the 4.7-point gain is a distillation effect on one split.
3. **"Most of it follows from N = 6."** Limit this to size. For speed, 6x of 20.8x leaves about 3.5x unexplained. Quote the passage that gives N = 6.
4. **Timing inconsistency.** 0.12 ms for the student against about 0.42 ms per backbone (inference) undercuts "roughly one backbone". Say so, and link it to the device, batch and precision question.
5. **Insufficient quotes.** Replace or extend the quotes for: Zhu [7] (ten electrodes, ten digits); Tang [8] (four electrodes, since the quote says 4 subjects); CVOS 82%; Walliczek 82.9% (column and condition); Table III (T = 5 column, best and worst rows); Ma Table 3 (which row is distilled).
6. **M02 usual-approach line.** Drop "cross-modal" or add it to the Appendix label. Support or drop "one being the target". Label the 46/27/20/2 counts as coming from the 131 full-text set.
7. **M05 usual approach.** Two plus two studies of 17 is not a usual approach. Write "no dominant channel count among 17 studies".
8. **Attribution.** Credit the authors for the 4.8-point loss (t32) and for inter-subject and inter-gender shift as future work (t45).
9. **M06 state of the art.** Relabel CVOS as a same-vocabulary reference under a different sensor and protocol, or name the best closed-vocabulary sEMG word result with its protocol.
10. **[2] year.** Make the text (2020) and the reference (ICASSP 2021) agree.
11. **Locator.** "Seven classes below F1 0.80" points to Table IV; the quote is §V.A.
12. **Wording.** Change "unseeded split" to "a single split with no seed or repeats reported". [6] lists three authors without "et al."; check the author list (unverified: I recall a longer list).

## Scores

- Procedure: 7/10. The claim table is complete and the numbers check out, but several quotes lack column headers or conditions, and the M02 deciding prior is mis-chosen.
- Final text: 7/10. The position is clear and the comparability argument is sound, but the M02 verdict and the student-control argument contradict the review's own evidence.

Strengths (brief): the arithmetic is right, the later works are labelled correctly and not used against the authors, and the review is plain about the split-unit problem and the gap between the spelling claim and the 26-class output.
