# Independent evaluation: MultiDiffNet (arXiv:2511.18294)

Date: 2026-11-21. Fallback evaluator (claim table only). Input: the compact review and its claim table; sources were not reopened. "Correct" means the quote and location in the claim table support the claim as written, including number, unit and condition.

## Claim check

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target changes decoder (M06) and evaluation (M12), continuing Diff-E | Claim rows 1, 4; t1, t89, c1 | correct | Sec. 3.1 and Sec. 2 quotes support the Diff-E lineage. |
| 2 | No-diffusion unseen imagined speech 13.76% vs full model 11.62% (Table 17) | Row 2; t86 | insufficient evidence | 13.76 appears in a garbled Table 17 row ("n dp x u deco"); the row label does not show that it is the no-diffusion configuration. 11.62 appears in no quote. |
| 3 | Same ablation in Table 13: no-diffusion rows match or beat the full model on imagined speech | Row 8; t87 | wrong | The Table 13 no-diffusion row quoted (t87) ends "19.22±0.20 11.36±1.93", i.e. 11.36% unseen, below 11.62%. The body cites Table 13 for an imagined-speech value that comes from Table 17. The two tables give 11.36 and 13.76 for what the review treats as the same ablation. |
| 4 | SSVEP no-diffusion 85.58% vs full 84.72% unseen | Row 8; t87 | insufficient evidence | 85.58 is quoted; 84.72 is not. |
| 5 | P300 within 1 point; MI up to 2.8 points below | Row 8; t87 | correct / insufficient evidence | 79.46 vs 79.47 and 38.54 vs 39.24 are quoted. The 36.49 behind "2.8 points" is not. |
| 6 | Headline gain over EEGNet 1.51 points (12.12 − 10.61), about 3 points above 11-class chance | Row 3; t44, t46, t85 | correct, condition missing | Arithmetic is right (12.12 − 9.09 = 3.03). 12.12 is the "MultiDiffNet + Mixup" row (t85), not the base model, and the review does not say so. |
| 7 | Two held-out imagined-speech subjects | Rows 3, 11; t75 | insufficient evidence | "14 11" in Table 1 is subjects and classes, so "14 − 12" rests on code. The code quotes t72–t81 all repeat one sentence of paper prose, not code lines. |
| 8 | Diff-E 60.63% on 13-class imagined speech, 22 subjects, vs 32.78% EEGNet, one 20% split | Row 5; c2, c4 | correct in part | 60.63 and the 20% split are quoted; 13 classes, 22 subjects and 32.78 are not. |
| 9 | Diff-E ablation 60.63 → 46.59 (23% relative) | Row 7; c2, c3 | correct | 14.04 / 60.63 = 23.2%. |
| 10 | [3] ablation 85.47 → 68.12 on overt speech | Row 7; c5 | insufficient evidence | 68.12 is quoted; 85.47 and "overt speech" are not. |
| 11 | Imagined-speech relative gain of the ablation 18% | Row 8 | correct, but depends on claim 2 | 2.14 / 11.62 = 18.4%. |
| 12 | Target calls LOSO computationally expensive (Sec. 4.1) | Row 9; t88 | correct | |
| 13 | Attar 2025: 82.4%, 8 words, LOSO, 4 participants; small sample conceded | Row 10; c7, c8 | correct in part | 82.4% and n = 4 are quoted; "8 words" and "LOSO" are not. [concurrent] label fits (accepted 3 Sep 2025, target Nov 2025). |
| 14 | Unseen sets: 2 of 35 SSVEP, 2 of 9 MI, 2 of 14 imagined speech | Row 11 | insufficient evidence | No code text quoted (see 7). The M12 table row says "2 to 5 held-out subjects per task", but the text never gives a count of 5. The P300 count is missing. |
| 15 | Unseen normalization from "their own calibration trials", count not given | Row 15; t7 | correct | |
| 16 | Normalization uses first 104 SSVEP samples or first half of imagined-speech test samples, all then scored | Row 16; t79, t81 | insufficient evidence | No code text quoted. The review does not say whether only label-free statistics are used. If so, this is transductive normalization, not label leakage, and the risk should be stated at that level. |
| 17 | P300 unseen 79.47% vs 85.63–87.24% for all five baselines; MI 39.24% vs EEGNet 46.18% | Row 17; t30, t31, t37, t38, t47 | correct in part | 79.47, 87.24, 39.24 and 46.18 are quoted; 85.63 is not. No SSVEP figure is quoted for "holds for SSVEP". |
| 18 | Seen–unseen gap 5.45 vs 0.65 (imagined speech), 5.88 vs 1.55 (P300) | Row 18; t30, t31, t44, t46 | correct, confound unhandled | Arithmetic is right. The imagined-speech gap uses the Mixup variant. EEGNet is near chance (10.61% vs 9.09%), so its gap is small by construction. The P300 comparison holds without this confound and should lead. |
| 19 | No chance level given although baselines are said to be near chance | Row 19; t59, t63, t90 | correct | |
| 20 | Appendix Table 2 gives 76.26% unseen P300 vs 79.47% in Table 1; MI values differ | Row 20; t67, t69 | correct in part | t67 has no task label in the quote. Its column order (likely seen acc/F1/bal. acc/AUC, then unseen) is inferred. Seen accuracy also differs (85.24 vs 85.35), which suggests a separate run rather than a metric difference. The review should say which. |
| 21 | Claim row 22, "Questions for the authors" | Row 22 | no matching text | The review has no such section. |
| 22 | [4] [concurrent] and [5] [later] are used only as state of the art, not as missed prior work | References, rows 10, 14 | correct | No chronology fault. |
| 23 | M06 usual approach = conditional autoencoder (3 of 13) | Row 4; Appendix rows 24–25 | wrong as framed | The review's own tally gives generated-sample augmentation 6 against conditional autoencoder 3. A 3-of-13 design is not the usual approach. Only two of the three CAE studies are named. |
| 24 | "The latent and its losses, not diffusion, carry the result" | Row 8 | position beyond evidence | No ablation of the contrastive or reconstruction losses is quoted. With SDs of ±1.25–6.15 and two test subjects, the cited differences show at most that diffusion is not shown to help. |
| 25 | Verdict: main claim "contradicted" by the ablation | Rows 2, 8 | position beyond evidence | Given claims 2–3 and the SDs, "not supported by" is what the evidence carries. The authors themselves report in Sec. 4.4 (t50) that ablation variants reach 85.58 SSVEP and 80.93 P300 unseen. The review presents this as its own finding without crediting Sec. 4.4. |

State of the art: the M06 line gives a 2023 within-subject result (Diff-E) for a paper whose claim is cross-subject. Reference [3] (2024, same design family) is newer, and the review does not say whether it reports imagined-speech results on the Diff-E corpus. The M12 line (82.4%, 4 subjects, bimodal EEG-fMRI) is a weak benchmark for the field. Both lines should state the condition mismatch plainly. No absence or "first/only" claims need deciding priors. All non-standard verdicts ("not reported", "not applicable") are descriptive.

## Required fixes (by impact)

1. Fix the ablation evidence. Name the Table 17 configuration that gives 13.76, quote the source of 11.62, and explain why Table 13's no-diffusion row gives 11.36. Then change "contradicted" to "not supported". Drop or support "the latent and its losses carry the result" with a loss ablation.
2. Credit the authors' own Sec. 4.4 report that ablation variants match or exceed the full model. Do not present it as the review's finding.
3. Say that the 12.12% headline and the 5.45-point gap are from "MultiDiffNet + Mixup" and give the base-model values. For the gap claim, note that a near-chance EEGNet has a small gap by construction, and lead with P300.
4. Restate the M06 usual approach. Per the Appendix tally, generated-sample augmentation (6) outnumbers conditional autoencoders (3). Name all three CAE studies or drop the count.
5. M03: quote the main.py lines and state whether the normalization uses label-free statistics only (transductive) or labels. Pitch the risk accordingly, and give the imagined-speech calibration count.
6. Add quotes for the unquoted numbers: 11.62, 84.72, 85.47 and "overt speech" [3], 85.63, 36.49, 32.78, 13 classes and 22 subjects [2], 8 words and LOSO [4]. Replace the repeated prose placeholder in rows t72–t81 with the code lines.
7. M06 state of the art: mark it as within-subject versus the target's cross-subject claim. Check whether [3] reports imagined-speech results that supersede Diff-E.
8. M12 table row: support "2 to 5 held-out subjects" (give the P300 count) or correct it to the counts in the text.
9. Appendix Table 2 vs Table 1: the seen value also differs (85.24 vs 85.35). Say whether this is a separate run or a different metric before calling it unexplained.
10. Remove claim-table row 22 or add the "Questions for the authors" section it refers to.

## Scores

- Procedure: 6/10. The claim table is filled, but code-based claims have no code quotes and several key numbers have no quote.
- Final text: 6/10. The positions are clear and the arithmetic is right, but the central ablation argument rests on inconsistent tables and is overstated.

Strengths: arithmetic checks out throughout, chronology labels are correct, and the Table 1 vs Appendix Table 2 inconsistency and the unreported calibration count are useful catches.
