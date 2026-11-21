# Independent evaluation: A First Exploration of Neuromorphic OT-CFM for Multi-Speaker VSR

Date: 2026-11-21. Fallback evaluator (claim table only). Input: the compact review with its claim table. No sources were opened. Statements about outside work come from the evaluator's own knowledge and are marked as such.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | M06 gain is 0.2 WER over the diffusion variant (22.3 vs 22.5) | Claim rows 1, 11 (Table 3 and Table 4 quotes) | correct | The diffusion row reads 22.5, and the two-step row reads 22.3. 0.2/22.5 = 0.9% and 2.2/24.5 = 9.0% check out. The 24.5 autoregressive value has no quote. |
| 2 | "One run" / "without seeds or intervals" | Claim rows 1, 11 | insufficient evidence | No quote shows that seeds are absent. It is a plausible absence claim, but it needs a location (for example the experimental setup in Sec. 5.1). |
| 3 | DVS-Lip is a 100-word isolated-word set | Claim row 2 ([2] Sec. 3.1) | correct | The quote supports it. |
| 4 | Speaker-disjoint 30/10 split | Claim row 12 ([2] Sec. 3.1), row 15 (40 speakers) | correct | 30 training speakers are quoted and 40 in total, so 10 test speakers follow. |
| 5 | The paper "reports WER and VER without a split" / "names no split" | Claim row 22 (target Sec. 5.1) | wrong as written | The review's own quote says: "We strictly follow the official train/test protocols of the DVS-Lip [47] and AVA [44] datasets". The paper claims the official split, so the review contradicts its own evidence. The defensible point is that the paper states the protocol without describing it and reports WER where the protocol defines word accuracy. |
| 6 | Six methods have identical Table 1 DVS-Lip and Table 2 "Clean" WERs | Claim rows 3, 16 | insufficient evidence | Only the Auto-AVSR Table 1 row and the LipsFlow Table 2 row are quoted. The value 26.1 in the list of six matches Auto-AVSR's second Table 1 column (VER), not a WER. Confirm that 26.1 is another method's WER and quote all six row pairs. |
| 7 | Low-light +0.6 WER (2.7%) for LipsFlow vs +23.7 (83%) for Auto-AVSR | Claim row 7 (Table 2 LipsFlow row) | insufficient evidence | The LipsFlow row has three deltas (+1.8, +0.6, +4.2), and no column header is quoted to show which one is low-light. The Auto-AVSR Table 2 row is not quoted. The arithmetic is right (0.6/22.3 = 2.7%, 23.7/28.4 = 83%). |
| 8 | AVA events are converted from RGB (Sec. 5.1) | Claim row 7 | insufficient evidence | No quote is given, yet this carries the low-light position. |
| 9 | TVTA 77.49% on DVS-Lip [3] | Claim rows 5, 13 | correct | The quote supports it. TVTA (arXiv 2607) postdates the target's v2 (1 Jul 2026) and is correctly used only as a concurrent reference point, not as missed prior work. |
| 10 | Prior best 75.3% [4], 75.08% [5] | Claim rows 5, 20 | partly correct | 75.3% is quoted. 75.08% for MTGA has no quote. |
| 11 | 22.3 WER implies 77.7% accuracy, level with TVTA, 2.4 above the prior best | Claim row 6 | correct (conditional) | The arithmetic holds, and the claim is properly marked as inference. |
| 12 | MSTP reports 72.10% accuracy, while the paper lists it at 30.5 WER | Claim rows 4, 14 | correct | Both quotes support it. 100 − 72.10 = 27.9. |
| 13 | 26× acceleration over SynthVSR (Sec. 5.2) | Claim rows 11, 17 | insufficient evidence / possible target inconsistency | The Sec. 5.2 quote does not contain "26×". The Table 4 quote gives "25.0×". 6000/240 = 25.0 (latency), while 4.80/0.18 ≈ 26.7 (RTF). The target may state two different factors, and the review does not note this. |
| 14 | The SynthVSR row equals the diffusion variant (RTF 4.80, 6000 ms, 185.6 M) | Claim rows 1, 17, 23 | partly correct | 185.6 M is quoted in both places. The diffusion variant's RTF and latency (Table 4, t39) are not quoted. |
| 15 | SynthVSR is a Conformer CTC/attention recognizer whose synthetic video serves only training [7] | Claim row 17 | insufficient evidence | The target's table shows "Conformer". The CTC/attention and training-only parts have no quote from [7]. This matches the evaluator's knowledge of SynthVSR (CVPR 2023). |
| 16 | Two steps called optimal, but 10 steps give 22.0 | Claim row 18 | partly correct | "Optimal" is quoted. The 10-step 22.0 row is not quoted. |
| 17 | Multi-speaker is a mislabel; clips are single-speaker (Sec. 3.1) | Claim row 15 | partly correct | 40 speakers are quoted from [2]. The target's Sec. 3.1 single-speaker cropping and the Sec. 5.2 "multi-speaker" wording are not quoted. |
| 18 | The Sentence-BERT homophene claim is never tested on a word-level set | Claim row 19 | correct | The quote states the motivation, and [2] gives a 100-word vocabulary. |
| 19 | M06 usual approach: hybrid CTC/attention 131 of 740 | Claim row 8 (ledger) | plausible | This is the typical VSR decoder design. |
| 20 | M06 state of the art: DLLM-VSR 19.4% WER on LRS3 [6] | Claim row 10 | wrong as state of the art | The quote does not show that the column is LRS3 WER. Even granting that, 19.4% is not the best LRS3 VSR result. From the evaluator's knowledge: Auto-AVSR (Ma et al., ICASSP 2023, arXiv:2303.14307) reports 19.1% WER on LRS3, and the LP Conformer (Chang et al., "Conformers are All You Need for Visual Speech Recognition", ICASSP 2024, arXiv:2302.09146) reports 12.8% WER on LRS3. 19.4% can be presented only as the best generative or diffusion text decoder. |
| 21 | Only this paper and DLLM-VSR generate text by diffusion or flow, among 11 ledger matches | Claim rows 9, 29 | insufficient evidence | The absence claim does not name the nine excluded studies or any deciding prior work. The evaluator knows of no earlier flow-matching text decoder for VSR, but does not know enough to confirm none exists. |
| 22 | M12 ledger counts | Claim rows 12, 32, 33; component table | internal contradiction | The text says "the 5 other DVS-Lip ledger studies". The Appendix gives 6 unique studies with "word accuracy 6; WER 1 (this paper)", which adds up to 7 in a ledger of 6. The table says "(6) (pattern match 6)". The M05 section counts 7 DVS-Lip event studies, but M12 has only 6. |
| 23 | M12 verdict "behind, typical of the field" | M12 section vs component table | internal contradiction | The section argues that the field reports word accuracy on the official split and this paper does not. "Typical of the field" undercuts the "behind" verdict. |
| 24 | Strongest confound: baseline strength | Claim rows 12, 14 | partly handled | The review notes MSTP at 30.5 vs 27.9 published, but not the consequence. LipsFlow's margin over MSTP falls from 8.2 to 5.6 WER points if the published figure is used. Re-run or weakened baselines are the main confound for the headline accuracy claim. |
| 25 | Process sentence at the end of the claim table | Final line | wrong for the published text | "All 35 claims map to a notes entry ... no claim was flagged for rewriting" is a process statement. The format forbids these in published text. |

## Required fixes, ordered by impact

1. **Split claim (Verdict, M12, component table).** Remove "without a split" and "names no split". The paper states that it follows the official DVS-Lip protocol (Sec. 5.1). Rewrite the point as: the paper claims the official protocol but reports WER/VER rather than the protocol's word accuracy, and it gives no split details, seeds or intervals.
2. **M06 state of the art.** 19.4% on LRS3 is not the best LRS3 VSR result. Auto-AVSR reports 19.1% (2023) and the LP Conformer reports 12.8% WER (2024). Either cite the best result, or relabel the line "best generative text decoder" and add a quote that shows the column is LRS3 WER.
3. **Baseline-strength confound.** State that the paper's MSTP figure (30.5 WER) is 2.6 points worse than MSTP's published 72.10% accuracy (27.9 error), so the margin shrinks from 8.2 to 5.6 points. Ask whether the baselines were re-run or copied, and check the other baselines the same way.
4. **Six identical rows.** Quote all six Table 1 / Table 2 row pairs. Confirm that 26.1 is a distinct method's WER and not Auto-AVSR's VER column. If it is a VER, correct the list and the count.
5. **M12 ledger counts.** Reconcile "5 other studies", "word accuracy 6; WER 1" in a 6-study ledger, and "(6) (pattern match 6)". Also reconcile the 6 studies in M12 with the 7 DVS-Lip event studies in M05.
6. **26× vs 25.0×.** Quote the Sec. 5.2 sentence that contains "26×". Note that Table 4 gives 25.0× (6000/240 ms), while the RTF ratio is about 26.7, so the paper states inconsistent factors.
7. **Low-light evidence.** Quote the Table 2 column headers that identify the +0.6 column as low-light, the Auto-AVSR Table 2 row (+23.7), and the Sec. 5.1 sentence on RGB-to-event conversion for AVA.
8. **Seed-level variation.** Replace "the accuracy gain is within seed-level variation (inference)" with the plain statement the evidence allows: a single run with no seeds or intervals cannot distinguish a 0.2-point difference. Give the location that shows no seeds are reported.
9. **M12 verdict wording.** Drop "typical of the field" from the "behind" verdict, or explain how it can be both.
10. **Remaining unquoted claims.** Add quotes for the diffusion variant's RTF and latency (Table 4), the 10-step 22.0 WER (Table 4), the single-speaker clip cropping (Sec. 3.1), the "multi-speaker" wording (Sec. 5.2), 75.08% for MTGA [5], and SynthVSR's CTC/attention design [7].
11. **Absence claim (M06).** Name the deciding works behind "two that generate text" and list the nine excluded studies in the Appendix.
12. **Process sentence.** Remove the closing "All 35 claims map ..." sentence from the published text.

## Scores

- Procedure: 6/10. Most numbers trace to quotes and the arithmetic is right. However, several load-bearing claims (low-light column, RGB conversion, six-row equality, 26×) lack quotes. The split claim contradicts the review's own quoted evidence.
- Final text: 6/10. The positions are clear and mostly well aimed: the evaluation-protocol mismatch, the baseline timing reuse, and the RGB-derived events. Fix the split contradiction, the M06 state of the art and the count inconsistencies before publication.

The review's strongest points are the SynthVSR timing reuse, the WER-vs-accuracy conversion against the DVS-Lip state of the art, and the observation that converted events cannot show a sensor dynamic-range benefit.
