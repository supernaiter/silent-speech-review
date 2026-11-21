# Independent evaluation: Landmark Guided Visual Feature Extractor for Visual Speech Recognition with Limited Resource

Date: 2026-11-21. Fallback evaluator (claim table and review text only; no sources opened). Statements from background knowledge, not from the claim table, are marked "(background)".

## Claim checks

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper [1] fuses a 20-landmark lip graph into ResNet-18 + DC-TCN; design standard because [2] fused a graph over 20 lip key points with an image branch on LRW (2020) | Claim rows 1, 7 | correct | Both quotes support 20 lip points; [2] is 2020, so prior. |
| 2 | Central claim rests on +0.90 Acc (86.65 vs 85.75, Table 3) | Row 2, 17 | correct (arithmetic) | 86.65 − 85.75 = 0.90; mAcc 84.25 − 83.41 = 0.84. |
| 3 | 0.90 gain is "smaller than the 1.20-point spread across the paper's own fusion variants" | Row 2 | wrong as an argument | 86.65 − 85.45 = 1.20 is right, but a spread across different architectures is not run-to-run variance. It cannot tell whether 0.90 is noise. What the evidence supports: one run, no seed variance, so the gain's reliability is unknown. |
| 4 | Landmark corruption costs 0.20 points, "which shows the landmark stream carries little of the decision" | Rows 3, 18 | goes beyond the evidence | 86.65 → 86.45 is right. With the perturbation size unknown (row 23) and no ablation that drops the stream, a small drop fits both "robust" and "little used". The review's own "needs next" section asks for the test that would settle this. |
| 5 | Combined corruption: −0.85 for the proposed model vs −0.96 for DC-TCN | Row 18 | correct | 86.65 − 85.80 = 0.85; 85.75 − 84.79 = 0.96. |
| 6 | 91.69% on LRW stays below 95.0% with word boundaries [3] | Rows 4, 13 | correct, needs a qualifier | Numbers match. SyncVSR trains against audio tokens from a pretrained quantizer (background), so "LRW-only" means LRW clips only, not visual-only supervision without outside models. Say so. |
| 7 | "The released test script feeds word boundaries" | Rows 4, 15 | partly supported | The quote shows `use_boundary=True` as a default, not that the reported checkpoints used it. The M12 section says "defaults to", which is right. The Verdict's "feeds" is stronger. |
| 8 | M06 usual approach: pixel CNN in 368 of 1,116; landmark stream 64; graph conv 12 | Row 5 | correct (tally) | Taken from the ledger tally; not re-counted. 368/1,116 is a plurality, not a majority. |
| 9 | M06 SOTA: NestLipGNN 92.3% on LRW [4], [later], 0.6 points above the target | Row 6 | correct number, scope unclear | 92.3 − 91.69 = 0.61. The word-boundary condition of the 92.3% is not given, which is the gap the review faults the target for. It is the best landmark-graph result, not the LRW state of the art (95.0% in M12). Scope the line. |
| 10 | Landmark-only graphs reach 49.3% to 80.3% [3] | Row 6 | insufficient evidence | Only 80.3 (Pointcloud, WB) is quoted; 49.3 has no quote. |
| 11 | Landmarks alone, even 478 points, give "only 62.7%" [6] | Row 9 | correct, but contradicts claim 10 | Quote matches. The next line's 80.3% landmark-only figure undercuts "only 62.7%". Reconcile them, e.g. by training signal (SyncVSR audio-token supervision) or boundary input. |
| 12 | [2] raised visual-only LRW from 83.29% to 84.25% | Row 7, 11 | partly supported | 84.25 and "+0.96%" are quoted. 83.29 is only implied by them; quote the baseline row. |
| 13 | LipFormer fused lip-motion and landmark streams for unseen speakers [5] | Row 8 | correct | Abstract quote supports it. |
| 14 | Distance graph alone: 85.75 → 85.74 (Table 2); graphs added in a fixed order | Row 10 | correct | Quote "+DAG 0.8574" supports it. |
| 15 | Increment over pixel baseline 0.69 points, smaller than 0.96 of the 2020 design | Row 11 | wrong framing | 91.69 − 91.00 = 0.69 is right. But the baselines differ (91.00 vs 83.29). As relative error reduction, the target cuts 7.7% of errors (0.69/9.00) and [2] cuts 5.7% (0.96/16.71). The comparison reverses. |
| 16 | M12 usual approach: ResNet-18 + LRW top-1 in 90 of 155; WB 40; mixup 25 | Row 12 | correct (tally) | Not re-counted. |
| 17 | M12 SOTA: SyncVSR 93.2% / 95.0%, LRW only, three runs [3] | Row 13, 4 | correct | Quote gives 93.2 ± 0.1, 95.0 ± 0.0 and the three-run average. I know of no higher LRW-trained word accuracy (background, not certain). |
| 18 | DC-TCN 91.00% "without mixup" matches the with-boundary, no-mixup ablation of Ma et al. [7] | Row 14 | insufficient evidence | No quoted 91.0 figure from Ma et al. The quoted row (90.4 / 92.1, apparently from SyncVSR's table) reads as without / with word boundaries, not as "no-boundary vs full recipe". The original DC-TCN paper reports about 88.4% (background), so where 91.00 comes from is still open. |
| 19 | Target omits mixup (Sec. 4.2) and so sits below the 92.1% recipe | Row 15 | correct | "but omit MixUp" is quoted. |
| 20 | LRW-ID validation and test share 20 speakers, so model selection saw test identities | Rows 16, 24 | correct fact, unfair framing | Row 24 quotes the authors: "the complete adaptation set was used for validation and testing". They disclose it, so it is not a finding from the manifests. LRW-ID and its adaptation protocol come from earlier work (Kim et al., ECCV 2022, background), so say whether the overlap comes from the protocol or from this paper. |
| 21 | "No additional computational cost" holds for landmark detection, not the model; 52.55M → 62.48M (+18.9%) | Row 19 | arithmetic correct, framing unfair | 62.48/52.55 − 1 = 18.9%. The truncated quote suggests the authors' statement is about landmark detection, and they report the parameter counts themselves (Table 2). Present it as context, not an overclaim. |
| 22 | Text gives 96 × 96 crops, code 88 × 88 | Row 20 | likely wrong | The standard LRW pipeline crops a 96 × 96 mouth ROI and then takes an 88 × 88 random or center crop (background). Unless the code skips the 96 stage, this is not a contradiction. |
| 23 | Non-standard verdict "not reported" for M12 | Rows 22, 23, 15 | supported | Missing seeds, perturbation magnitudes and boundary condition are documented in rows 2, 15 and 23. |
| 24 | Chronology | References | correct | [2], [5], [6], [3], [7] are prior. [4] is labeled [later] and is used only as the state of the art, not as a missed citation. |
| 25 | Text integrity | Claim rows 22–24, Ref. 1 | wrong | Claim rows 22–24 cite a "Questions for the authors" section that is not in the review. Reference 1 includes process notes ("arXiv v1 read; the paper's ACM DOI is a placeholder"). |

## Required fixes (ordered by impact)

1. M06 verdict (claim 15): the claim that 0.69 points is smaller than 0.96 ignores the different baselines (91.00 vs 83.29). As relative error reduction, the target (7.7%) beats [2] (5.7%). Restate the comparison or drop it.
2. Verdict and "outrun the evidence" (claim 3): drop the comparison of the 0.90 gain with the 1.20 spread of Table 1. Architecture spread is not variance. Say plainly that one run with no seeds leaves the gain's reliability unknown.
3. Robustness (claim 4): replace "shows the landmark stream carries little of the decision" with the plain statement the evidence allows. A 0.20-point drop under perturbations of unknown size cannot tell robustness apart from low reliance on the stream.
4. Crop size (claim 22): remove the 96 vs 88 discrepancy unless the code shows no 96 × 96 stage. A 96 ROI followed by an 88 crop is the standard pipeline.
5. DC-TCN 91.00 (claim 18): give the Ma et al. location and quote that shows 91.0 with boundaries and without mixup, or drop the "matches" claim. Relabel 90.4 / 92.1 as without / with word boundaries, as the quoted table shows.
6. M06 state of the art (claims 9–11): scope NestLipGNN as the best landmark-graph result and state its boundary condition. Quote or drop the 49.3% figure. Reconcile "only 62.7%" with the 80.3% landmark-only figure.
7. LRW-ID overlap (claim 20): credit the authors' own Sec. 4.1 statement, and say whether the shared val/test speakers come from the LRW-ID protocol of earlier work or from this paper.
8. Computational cost (claim 21): the authors report the parameter growth themselves and their statement concerns landmark detection, so do not present it as an overclaim.
9. SyncVSR qualifier (claim 6): say that "LRW-only" includes audio-token supervision from a pretrained quantizer.
10. Word boundary (claim 7): in the Verdict, change "feeds word boundaries" to "defaults to word-boundary input", to match the evidence and the M12 section.
11. Liu baseline (claim 12): add the quote for 83.29%.
12. Text integrity (claim 25): remove the process notes from Reference 1, and either add the "Questions for the authors" section or drop claim rows 22–24.

## Scores

- Procedure: 7/10. Every number traces to a quote or an inference label, and the arithmetic is correct. The gaps are unquoted figures (49.3, 91.0, 83.29) and table rows for a section that is not in the review.
- Final text: 6/10. The position is clear and mostly backed by evidence. Two central arguments (the 0.69 vs 0.96 comparison and the use of variant spread as noise) do not hold, and three framings credit the review with points the authors state themselves or that follow standard practice.
