# Independent evaluation: Adaptation of Tongue Ultrasound-Based Silent Speech Interfaces Using Spatial Transformer Networks

Date: 2026-11-21. Fallback evaluator (claim table only). The review text and its claim table were checked against each other. No sources were opened. Statements about other work rely on general knowledge of the field and are marked as such.

## Claim check

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target retrains only an affine STN placed before the CNN | Claim 1 (t2, t3) | correct | Both quotes support it. |
| 2 | STN changes matched-condition dev MSE by at most 0.021 | Claim 3 (t15, t16) | insufficient evidence | Only the "no STN" rows are quoted. The with-STN value 0.483 for session 5, which sets the maximum, has no quote. |
| 3 | Abstract credits "adapting just the STN module" with 88% | Claims 4, 20 (t61, t20, t24, t14) | partly correct | 88% is the third column of the Table 2 average (t20), and t14 shows these figures are gap closure. No quote names the third column as "STN plus output layer". Its identity rests only on the column order. |
| 4 | STN alone closes 75–76% | Claim 4 (t20, t24) | correct | Second-column averages are -76% and -75%. |
| 5 | Prior [2]: lower-layer adaptation "already removed the remounting loss" | Claims 2, 6 (c1, c4) | wrong (overstated) | c4 is cut off at "roughly the same averaged correl…". It supports "about matched" and says nothing of removing the loss. c1 says "sufficient". The statement that 10 sentences matched 20 sentences from scratch cannot be seen in the quote. |
| 6 | About 10% of the weights | Claim 7 (t29) | correct | |
| 7 | Lip reading [3]: 0.74M parameters, 40.9% vs 47.3% unadapted vs 39.6% full, 20 speakers, about 83% of the gain | Claim 8 (s1) | insufficient evidence | Only 40.9% is quoted. The 47.3%, 39.6%, 0.74M and 20-speaker figures have no quote. The arithmetic is right: 6.4/7.7 = 0.83. The text says "2024" but the reference gives AAAI 2025. Comparing 83% of a WER gain with 75–76% of an MSE gap crosses both modality and metric. |
| 8 | Misalignment documented without an automatic fix [4] | Claim 9 (c7) | correct | c7 supports the narrower point that no method auto-rotates within a session. |
| 9 | User-dependent padding [5] cut GRID WER from 11.12% to 6.80% with 1 min | Claim 10 (c8) | wrong / no quote | The only quote is "adapting on 5 minutes video achieves 5.67% WER". Neither the 11.12%, the 6.80% nor the 1-minute condition appears. |
| 10 | spk049 0.588 vs 0.400 (47% higher); ses-2 0.646 vs 0.503 (28% higher) | Claim 11 (t21, t25) | correct | 1.47 and 1.28 check out. |
| 11 | A mean θ closes only 11–42% | Claim 12 (t38) | insufficient evidence | The quote says "25-35% reduction". The averages are -35% and -26% (t20, t24), and the quoted rows give -25% and -34%. No quoted row supports the 11% or 42% end of the range. |
| 12 | No significant STN benefit in matched conditions; 3D model 0.275 vs 0.278 | Claim 15 (t17, t35) | correct | |
| 13 | Prior [2] used 1–50 adaptation sentences and MUSHRA | Claim 17 (c3, c5) | correct | A "held-out passage" is not in the quotes. |
| 14 | M06 SOTA: 15.93% ASR WER, one TaL speaker [6] | Claim 14 | insufficient evidence | The only source is the audit tally. No quote from [6] is given. |
| 15 | M12 SOTA: 31.64% ASR WER, TaL80 [6] | Claim 18 | insufficient evidence | Same problem: no quote. The review gives two different headline values from [6] in two slots without saying why each was chosen. |
| 16 | Target reports MSE only; dev set in Table 1, unnamed partition in Tables 2–3 | Claim 19 (t15, t42, t43) | correct | t43 confirms early stopping on the validation set. |
| 17 | Adaptation data amount per run not reported | Claim 22 (t47) | overstated | The paper gives the 3.5 min average session length and an 85-10-5 split, so the amount (about 85% of each target recording) can be inferred. A fairer wording is "implied, not stated". |
| 18 | 3.5 vs 15 min confound | Claim 23 (t6, t18, t53) | correct, but fairness issue | t18 shows the authors themselves point out the shorter sessions in §5. The review presents the confound as its own finding without crediting them. |
| 19 | Random 85:10:5 split may leak neighbouring frames | Claim 24 (t45) | correct as hedged | The unit of the split is not stated. "Can" is appropriate. |
| 20 | Scope: voiced read speech only; no synthesized speech evaluated | Claim 25 (t51, t49) | correct | |
| 21 | Usual approach M03: 93 studies; 17 input/feature transforms, 10 prompts/padding, 5 layer subsets | Claim 5 (tally) | plausible | Ledger-derived, so not audited. For ultrasound SSI, full or lower-layer fine-tuning is the typical design, which fits the cited prior [2]. |
| 22 | Usual approach M06: frame-wise DNN (37) / CNN (31) of 51 | Claim 13 (tally) | plausible | This fits the ultrasound-to-vocoder literature up to about 2023. |
| 23 | "No later ultrasound study adapts with fewer parameters" | M03 SOTA | insufficient evidence | This is an absence claim with no deciding later works and no ledger count named. |
| 24 | "No other study in the Appendix learns an image-space transform for adaptation" | M03 body | partly supported | [4] and [5] are named as nearest priors, which helps. STN front ends exist in visual speech recognition beyond [5], and the review should confirm that none of them were used for speaker adaptation (general knowledge; not checked). |
| 25 | M12 verdict "behind" | M12 section and table | insufficient evidence | The parenthetical "typical of the field and of its own prior" contradicts "behind". The ledger count of studies reporting only MSE or regression loss is not given, so the gap from usual practice is not quantified. |

## Central claim and confounds

The strongest confound is that the 75–76% and 88% figures are gap-closure ratios, and each condition has its own full-retraining endpoint. That endpoint was trained on 15 min of speaker data or 3.5 min of session data, from a single base speaker (spk048). The review names the data-length confound and the single base speaker (under "What the field needs next") and correctly separates gap closure from MSE reduction. It does not say that the ratio's denominator itself changes with the amount of adaptation data. The verdict's wording about [2] ("already removed the remounting loss") is stronger than the quoted evidence.

## Required fixes (ordered by impact)

1. Claim 10 / [5]: the figures 11.12% to 6.80% with 1 min of data have no supporting quote, and the quote that is given (5.67% at 5 min) is a different condition. Either quote the passage that gives the 1-minute result or restate the claim using the 5-minute figure.
2. Verdict and claims 2/6: "already removed the remounting loss [2]" overstates c1 and c4. Rewrite it to match the quote, for example "10 adaptation sentences roughly matched 20 sentences of training from scratch", and give the full c4 passage.
3. Claims 4/20: add the Table 2 column header that shows the third column is STN plus output layer. Without it, the headline criticism of the abstract has no quoted support.
4. Claim 12: "11–42%" is not supported, and the authors' own wording is "25–35%". Either quote the per-row extremes or use the averages (-35% and -26%).
5. Claim 8 / [3]: add quotes for 47.3%, 39.6%, 0.74M parameters and 20 speakers. Make the year agree with the reference (2024 arXiv vs AAAI 2025). Drop "close to the 75–76% here" or mark it as not comparable, since it sets a WER gain against an MSE gap across modalities.
6. M06 and M12 state of the art / [6]: add source quotes for 15.93% (one TaL speaker) and 31.64% (TaL80). Say why different figures from the same paper are used for the two slots.
7. M12 verdict: remove the contradiction between "behind" and "typical of the field". Give the ledger count for MSE-only or regression-loss evaluation, or change the verdict.
8. Claim 18 fairness: the authors state the 3.5 vs 15 min difference themselves (§5, t18). Credit them, and keep as the review's own point only the claim that this confounds the misalignment explanation.
9. Claim 22: replace "amount per run not reported" with "not stated; implied by the 85-10-5 split of 3.5 min sessions and 15 min speaker recordings".
10. Claim 3: quote the with-STN row of Table 1 (including 0.483 for session 5) so that the 0.021 maximum can be checked.
11. Absence claims in M03: for "No later ultrasound study adapts with fewer parameters" and "No other study ... learns an image-space transform", name the deciding works or the ledger query and count. Confirm that STN front ends in visual speech recognition were not used for speaker adaptation.

## Scores

- Procedure: 6/10. The claim table is complete and the inference steps are marked. Several key numbers rest on missing or mismatched quotes (rows 1, 3, 4, 5, 6 of the fixes).
- Final text: 6/10. The position is clear and the gap-closure critique is sound. One comparator is misquoted, one prior is overstated, and the M12 verdict contradicts itself.
