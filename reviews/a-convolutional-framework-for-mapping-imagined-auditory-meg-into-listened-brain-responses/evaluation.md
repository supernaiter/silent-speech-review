# Evaluation: A Convolutional Framework for Mapping Imagined Auditory MEG into Listened Brain Responses

Date: 2026-11-21. Fallback evaluator (claim table only): the review text and its claim table were checked; the original sources were not reopened. Points from outside knowledge are marked as such.

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target maps imagined MEG to listened MEG with a CNN and a subject-specific calibration layer (Verdict, M06) | Claim 1, 8; Sec. V-B | correct | The quotes support the design. |
| 2 | Null shuffles trial order and channel assignments; r = 0.0113 vs 0.0063 | Claim 2, 16; Sec. V-B | correct | The numbers and the null description match the quote. |
| 3 | Cross-subject linear result has no number | Claim 15; Sec. I, V-A | correct | The quote gives only "poor performance". |
| 4 | Held-out subject's data train the calibration layer; no ablation isolates it | Claims 8, 21; Sec. V-B | insufficient evidence | The absence of an ablation is plausible, but the claim table has no quote showing calibration fitted on held-out-subject data. |
| 5 | "Nothing is decoded from the predicted responses here" | none | insufficient evidence | No location given. |
| 6 | [2]: 17 participants, linear mapping beats pairing-only null on unseen subjects without calibration | Claim 3; Sec. 2.1, 2.3, 2.5, Table 2 of [2] | correct | All three parts are in the quotes. |
| 7 | [2] "removes the motivation for the CNN" | Claims 3, 5 | wrong (overreach) | [2] uses a different task (speech, 76 words, 17 participants) from the target (11 musicians, 4 stimuli). In [2] the nonlinear RNN beats the linear model (t = 9.59 vs 5.63), so the result does not show that a nonlinear model is unnecessary. |
| 8 | M06 SOTA: six models above null; RNN t = 9.59, linear t = 5.63 | Claim 5; Table 2 of [2] | insufficient evidence | The quote gives three t values per model (RNN 13.02 / 7.68 / 9.59; LinearLag 10.29 / 2.58 / 5.63). The review takes the third value without naming the condition. The quote shows only two models, not six, and does not say the test is paired. |
| 9 | M06 usual approach: cross-condition 8, perception-to-imagery 6 of 112; [3], [4] as examples | Claim 4; Appendix tally | correct | The quotes from [3] and [4] support the examples. |
| 10 | No prior pattern-match study maps imagined into perceived responses; other hits are concurrent or later | Claim 6 | insufficient evidence | The concurrent hit (arXiv 2604.15374) is not named in the text. Two lines of prior work need a check (outside knowledge): DTW alignment of covert to overt speech (Martin et al., 2014, Front. Neuroeng.) and EEG imagery-perception work on melodies (Marion et al., 2021, J. Neurosci.; Di Liberto et al., 2021). Neither may map neural responses neural-to-neural, but the review should say whether they decide the claim. |
| 11 | M06 verdict ahead: Appendix count, deciding priors, repeated effect | Claims 6, 22–24 | correct with caveat | The count and the priors are present. "Repeated" means within one study across held-out subjects. With the central claim unsupported, call it ahead on design only, which the text nearly does. |
| 12 | M03 usual approach: 90 of 379 | Claim 7, 26, 27; table | wrong (inconsistent) | The text and Appendix line 27 give 379. The table and Appendix line 26 give 370. |
| 13 | Calibration layer = per-subject 1x1 subject layer of [5], cited but not related | Claims 8, 9 | correct | The quotes match. |
| 14 | M03 SOTA: 61.3% Top-10, MEG speech, pre-training plus fine-tuning [6] | Claim 10 | insufficient evidence | The quote lists 61.3%, 43.0% and 39.9% "respectively" without the datasets or conditions. The MEG assignment and the fine-tuning condition are not shown, and neither is the candidate pool size for Top-10. |
| 15 | M11: speech 83, music 9, MEG 26 of 112 | Claim 11 | correct | — |
| 16 | M11 SOTA: [3] MEG, 71 participants vs 11 here | Claim 12 | correct | The numbers match. Participant count is a weak SOTA metric. |
| 17 | M12 usual approach: 45 of 132; channel shuffle 10 | Claim 13 | correct | — |
| 18 | M12 SOTA: pairing-only null in [2] | Claim 14 | correct but weak | A pairing-only shuffle falls inside the usual "label or trial permutation" category, so it is the usual approach, not an advance. |
| 19 | M12 verdict "not reported" | Sec. V-B | correct | The null is described, but the shuffle count, seeds and calibration size are missing. |
| 20 | M02 verdict "not reported" while the entry reads "Listened MEG of the same stimulus" | Table | wrong (inconsistent) | The supervision is reported. The verdict should be standard, or the review should say which detail is missing. |
| 21 | Exact two-sided Wilcoxon p cannot fall below about 0.005 with n = 11 and two negatives | Claim 17 (inference) | correct | The minimum is p = 5/1024 ≈ 0.0049 (negative ranks 1 and 2). State it plainly. This only holds if the test unit is subjects, and the paper does not confirm that. p ≈ 0.005 is still below 0.01, so "p ≪ 0.01" is loose rather than false. |
| 22 | 155 channels in the CNN vs 157 recorded | Claims 18, 19 | correct | Present it as an unexplained discrepancy. The text does not show whether the paper excludes channels elsewhere. |
| 23 | Chronology: [2] (arXiv 2605) and [6] (arXiv 2608) labelled later; 2604.15374 labelled concurrent | References | correct | The target appeared at Asilomar (Oct 2025) and on arXiv (Dec 2025), so the labels hold. |
| 24 | [3] cited as bioRxiv 2023 | References | insufficient evidence | Outside knowledge, low to medium confidence: a peer-reviewed version may exist (PLOS Biology, 2024). Check and cite it if it does. |
| 25 | [5] Nat. Mach. Intell. 5, 1097–1107 (2023); [4] Sci. Rep. 14, 11491 (2024) | References | correct (outside knowledge) | — |

## Required fixes (by impact)

1. Verdict: drop or qualify "removes the motivation for the CNN". [2] uses a different task and stimulus set, and in [2] the nonlinear RNN outperforms the linear mapping (t = 9.59 vs 5.63).
2. M06 State of the art: name the Table 2 column (condition) that the t values come from. Quote the support for "six mapping models" and for "paired t", or drop them.
3. M06 absence claim: name the concurrent hit (arXiv 2604.15374). Say whether earlier imagery-perception alignment work decides the novelty claim: Martin et al. 2014 (DTW covert-overt) and Marion et al. 2021 / Di Liberto et al. 2021 (EEG melody imagery).
4. M03: reconcile 379 vs 370 across the text, the table and the Appendix.
5. M03 State of the art: tie 61.3% to its dataset and condition in Table III of [6], and give the Top-10 candidate pool.
6. Verdict: give a location for "the held-out subject's own data train the calibration layer" and for "nothing is decoded from the predicted responses".
7. M02: fix the verdict "not reported", which contradicts the reported supervision entry.
8. M12 State of the art: a pairing-only shuffle is within the usual permutation category. Either present it as the usual approach the target departed from, or name a stronger null (for example, repeated permutations with a reported count).
9. Wilcoxon point: state the bound plainly (p ≥ 5/1024 ≈ 0.0049 with subjects as the unit). Note that "p ≪ 0.01" is loose rather than wrong, and that the test unit is unconfirmed.
10. 155 vs 157 channels: describe it as unexplained unless the paper is checked for a channel-exclusion step.
11. Reference [3]: check for the peer-reviewed version and update the citation.

## Scores

- Procedure: 7/10
- Final text: 6/10
