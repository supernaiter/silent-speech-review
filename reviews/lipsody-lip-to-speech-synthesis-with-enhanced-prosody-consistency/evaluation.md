# Evaluation: LipSody (arXiv:2602.01908) review

Date: 2026-11-22. Fallback evaluator (claim table only). Input: the compact review with its claim table. No sources were reopened. Where a note says "from knowledge", it comes from the evaluator's background knowledge and needs a locator check.

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | LipSody changes the decoder: pitch and energy are predicted from lip content, face identity and emotion, and they condition a DDPM model with CFG | Claim table rows 1 and 9 (t1, t2, t7) | correct | t1 and t2 name all three cues. "LipVoicer-style" is supported by the baseline lineage (t46). |
| 2 | GF0 goes from 28.87 to 25.15 (Table 2) | Row 3 (t24, t25) | correct | Gain 3.72, as row 9 uses. |
| 3 | WER is 22.5% against 22.1% (recon) and 21.9% (official) | Rows 3 and 16 (t21–t23) | correct | Values are fractions in Table 1 (0.225, 0.221, 0.219). |
| 4 | Without the emotion embedding, 93% of the energy-consistency gain remains | Rows 4 and 9 (t24, t30, t31) | correct (arithmetic); judgment wrong | (1.2667 − 0.9402) / (1.2667 − 0.9141) = 92.6%. The w/o-emotion row still has the pitch and energy predictors, so this number does not separate normalization from the predictors. It cannot carry the "strongest confound" claim. |
| 5 | The third prosody column in Tables 2 and 4 is energy consistency (EC), and lower is better | Rows 3, 4 and 13 | insufficient evidence | The quotes give the numbers but not the column headers. t55 defines only GF0. The direction is consistent with t53, "outperforms in all five". |
| 6 | Emotion accounts for 1.96 of 3.72 (GF0), 0.20 of 4.20 (LF0) and 0.026 of 0.353 (EC); WER is 22.0% without it | Row 9 (t24, t30, t31) | correct | All arithmetic checks. This is plain computation, so the "(inference)" tag hedges it needlessly. |
| 7 | The SOTA-intelligibility claim (§1) rests on LipVoicer alone and on one ASR scorer | Rows 5, 12 and 16 (t5, t45, t46, c11) | correct | The authors themselves report no significant difference (§5.1), and the review attributes that finding to them. |
| 8 | No repeated runs | Rows 5 and 15 (t48) | insufficient evidence | t48 gives the training steps only. This is an absence claim with no location for "no seeds or variance reported". |
| 9 | Speaker-wise normalization (§3.2) is never ablated | Rows 4 and 17 (t10) | insufficient evidence | t10 confirms the switch. No quote says how the LipVoicer_recon baseline was normalized. If the baseline was trained with clip-wise normalization, the confound is real. If it was speaker-wise too, the confound disappears. |
| 10 | Usual approach M06: of 165 studies, 54 use adversarial training, 22 use a diffusion decoder and 15 use prosody predictors, 8 of them prior | Rows 6, 21–23 (audit) | insufficient evidence (ledger) | Plausible as the typical design. These counts come from the ledger and are outside this check. |
| 11 | VCVTS has a pitch predictor, and Let There Be Sound has pitch and energy predictors trained against GT contours | Row 6 (c4–c6) | correct | The quotes support both. |
| 12 | Faces-to-Voices feeds facial expression into pitch and energy predictors | Rows 2, 7 and 8 (c1, c2) | correct | — |
| 13 | Faces-to-Voices reports F0 RMSE 39.013 and WER 30.45% on LRS3 (Table 2) | Row 7 (c3) | insufficient evidence | The numbers appear in the quote, but the column headers (F0 RMSE, WER) and the LRS3 condition are not quoted. |
| 14 | Faces-to-Voices and V2SFlow use ASR models different from LipSody's | Rows 7 and 12 | insufficient evidence | Only LipSody's ASR is quoted (c11). There is no quote for the comparators' ASR. |
| 15 | Faces-to-Voices is the M06 state of the art | Row 7 | wrong as labelled | Its 30.45% WER is worse than LipVoicer's 21.9% and LipSody's 22.5% on the same task, although with different ASR models. It is the closest prior design, not the best result. |
| 16 | ImaginTalk aligns speech with content, identity and emotion from face video | Row 8 (c9) | correct | It is arXiv 2503.14928 (March 2025), more than 6 months before the target, so it is fairly treated as prior work. |
| 17 | 5 studies route a face emotion cue into prosody: 2 prior and 2 concurrent | Row 8 | insufficient evidence | The fifth study is not identified (presumably the target), and the two concurrent works are not named. |
| 18 | The three-cue estimator is not new | Rows 2 and 8 | correct within video-to-speech | From knowledge: HPMDubbing (Cong et al., "Learning to Dub Movies via Hierarchical Prosody Models", CVPR 2023) predicts pitch and energy from facial expression (valence and arousal) alongside lip motion. It is text-conditioned dubbing, so it is outside video-to-speech, but it is an earlier instance of the design. |
| 19 | V2SFlow gets 28.5% WER on unseen LRS3 and uses normalized-F0 MAE | Row 11 (c7, c8) | correct | It matches the target's own citation of 28.5% (t45). |
| 20 | V2SFlow is the M12 state of the art | Row 11 | wrong as labelled | A 28.5% WER is not the best on unseen LRS3. The target reports 21.9% for LipVoicer. A more recent multimodal diffusion transformer, AlignDiT (Choi et al., 2025, arXiv 2504.20629, from knowledge), should be checked as a candidate. |
| 21 | An F0 or energy error metric appears in 10 of 165 studies, and GF0, LF0 and EC have no units | Row 13 (t55) | insufficient evidence for the units | t55 defines GF0 as an L1 pitch difference, so the unit is Hz implicitly. The quotes do not show the table headers. |
| 22 | Naturalness 3.47 vs 3.36 (n.s.) and ABX 54.22% vs 45.78% | Row 14 (t27, t28, t37, t39) | correct | 4.22 points above chance is right. The review does not say whether the authors report the ABX result as significant. |
| 23 | Oracle row: 21.0% WER | Row 18 (t32) | correct | — |
| 24 | Other pitch extractors are omitted, and only "p < 0.01" is given | Row 19 (t36, t53) | correct | — |
| 25 | Reference list: authors, venues and years | References | mostly correct | From knowledge: V2SFlow (arXiv:2411.19486) appeared at ICASSP 2025. If that is confirmed, the "arXiv preprint, 2024" entry should be updated. The other entries are consistent. |

**Central confound.** The strongest confound is identified: speaker-wise normalization versus the baseline's normalization. However, the review gives no quote for the baseline's setting. The 93% energy figure also does not isolate normalization (rows 4 and 9). Baseline strength (a reimplemented LipVoicer at 22.1% against the official 21.9%) is handled.

**Verdicts.** All slot verdicts are `standard`, `not applicable` or `not reported`, so no `ahead` rules apply.

**Fairness.** No later work is treated as prior work, and the review does not present an author-reported finding as its own.

## Required fixes (ordered by impact)

1. Add the location where the paper states the normalization used for LipVoicer_recon. Drop the 93% energy figure as support for the normalization confound, or restate it as "the gain does not depend on the emotion cue". The predictors remain in that ablation row.
2. Relabel the M06 and M12 "State of the art" lines. Faces-to-Voices (30.45% WER) and V2SFlow (28.5%) are the closest designs, not the best results. Either name the best reported system for each metric with its ASR model, or call the lines "closest prior design". Check AlignDiT (2025) as a more recent candidate.
3. Add quotes for the Faces-to-Voices Table 2 column headers and LRS3 condition, and for the ASR models used by Faces-to-Voices and V2SFlow. The "different ASR, cannot be ranked" statements depend on them.
4. Name all 5 face-emotion-cue studies: the 2 prior, the 2 concurrent, and the fifth (presumably the target).
5. Either scope the novelty rebuttal to video-to-speech or cite HPMDubbing (CVPR 2023) as an earlier facial-expression-to-pitch/energy design in dubbing.
6. Give a location for "no repeated runs" (for example, "no seeds or variance reported in §4.3 or the tables"), or drop the claim.
7. Quote the Table 2 and Table 4 column headers so that the EC naming, its direction and the missing units are verifiable.
8. Say whether the authors report the ABX preference as significant before calling the listener effects small.
9. Remove the "(inference)" tag from direct arithmetic (the Table 4 ablation shares) and keep it only for interpretive statements. Update the V2SFlow venue to ICASSP 2025 if confirmed.

## Scores

- Procedure: 7/10
- Final text: 7/10
