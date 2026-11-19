# Evaluation: AKVSR review

Date: 2026-11-19. Fallback evaluator (claim table only). Input: the compact review (Verdict, component sections, component table, "Where the claims outrun the evidence") and its claim table. No sources were opened. Points from the evaluator's own knowledge of the literature are marked "evaluator knowledge" and need checking against the source before they are applied.

## Claim checks

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Verdict: HuBERT features quantized into a 200-slot memory recalled from video; lip-reader training needs no audio | Claim row 1 (Sec. IV-B, II, III-C); row 9 (Table III "AKVSR (HuBERT [34])") | correct | "200 discrete units" and "only visual input ... training the VSR model" carry it. HuBERT appears only in row 9. |
| 2 | Recalling audio memory from video is the same group's earlier design [2], [3] | Row 2; reference list authors | correct | Quotes show audio saved to memory during training and visual-only inference. Authors overlap (Kim M., Ro Y. M.). |
| 3 | Gain over no-memory baseline repeats across LRS3, LRS2, two model sizes, second backbone | Rows 7, 9 | insufficient evidence | 46.1 and 41.6 (LRS3), 32.2 (LRS2) and 54.5 (TM-seq2seq) are quoted. 28.7 (LRS2) and 59.9 (TM-seq2seq) are not in any quote. The two model sizes rest on 46.1 to 41.6 (Base, Table III) and 32.5 to 29.1 (Large, Table I), but the claim does not cite row 7. |
| 4 | Edge over distillation is 2.0 points from one LRS3 run | Rows 3, 10 | correct | 43.6 - 41.6 = 2.0. "One run" is read from the absence of seeds, which is acceptable. |
| 5 | Memory carries transcripts of 656 h, 22 times the 30 h labels | Rows 3, 17 | correct | 656 / 30 = 21.9. The memory being applied to Table I rows is read from "in other experiments" (§V-H), and the review labels it as inference. |
| 6 | SynthVSR Large 18.2% without LM, 5.4 points below 23.6% | Row 4 | insufficient evidence | The arithmetic is right. The quote is cut at "16.9% (18.2%", so it does not show that 18.2% is the no-LM figure, or which model size and data it belongs to. |
| 7 | M02 usual approach: 40 of 54 KD, 12 memory recall | Rows 5, 23 to 25 | outside check | Ledger tallies. 40 + 12 + 1 = 53 of 54; one study is unassigned. [5] has no claim row. |
| 8 | Memory priors need paired audio while the lip reader trains; the paper indexes slots by k-means units (§III-B) | Rows 2, 6 | partly insufficient | The priors part matches. The §III-B statement has no claim row or quote. |
| 9 | 30 h Large: 29.1% vs AV-HuBERT and RAVEn at 32.5% [6], [7] (2022), 3.4 points | Row 7 | correct with one error | 32.5 - 29.1 = 3.4. Only one 32.5 row is quoted for two comparators. "(2022)" is wrong for RAVEn [7], which the reference list gives as ICLR 2023. |
| 10 | USR 2.0 reaches 23.7% "in that setting" (30 h, Large) | Row 8 | insufficient evidence | The quote "USR 2.0 ✓ 23.7 2.3 2.2" does not show the labelled hours, model size or unlabelled data. 29.1 - 23.7 = 5.4 is correct. |
| 11 | Baseline gains 46.1 to 41.6, 32.2 to 28.7, 59.9 to 54.5 | Rows 9, 19 | partly insufficient | 28.7 and 59.9 are not quoted (see 3). |
| 12 | KD vs AKVSR 43.6 to 41.6, 4.6% relative | Row 10 | correct | 2.0 / 43.6 = 4.59%. |
| 13 | Memory data alone: 44.7% (223 h) to 41.5% (656 h), larger than the KD edge | Row 11 | correct, but a confound and an inconsistency are missed | 3.2 > 2.0. The 656 h set adds in-domain LRS3, so the change is not only label quantity. Table IX gives 41.5% for the 656 h memory, while Tables III and IV give 41.6%. The review does not mention this 0.1-point inconsistency in the target. |
| 14 | M12 usual approach: 258 studies; 141 record supervision: 18 / 17 / 6 | Rows 12, 28, 29 | outside check; unclear | 18 + 17 + 6 = 41 of 141, and the other 100 are not explained. The line gives no usual evaluation design. |
| 15 | At release: 23.6% (433 h + 1,326 h pseudo-labelled) trailed SynthVSR 18.2% and Auto-AVSR 19.1% | Row 13 | insufficient evidence | 23.6% is quoted, but "pseudo-labelled" is not. The 18.2% condition is cut off (see 6). Neither comparator's training data is stated (see fix 1). |
| 16 | Best today 16.9% with LM [4]; USR 2.0 Huge 17.6% [8] | Row 14 | wrong or insufficient | The quotes do not show which SynthVSR figure is the LM figure, or whether USR 2.0's 17.6% uses an LM, so the two numbers may not share a condition. Evaluator knowledge: LP Conformer (Chang et al., "Conformer is All You Need for Visual Speech Recognition", ICASSP 2024, arXiv:2302.10915) reports about 12.8% LRS3 WER using large non-public data. "Best today" holds only for public data. |
| 17 | Table I lists only the Base rows of [4] (27.9% at 433 h) | Row 15 | insufficient evidence | The quote shows the Base row, but no quote can show that the Large row is absent. The location is acceptable. |
| 18 | Lead over RAVEn 24.4% is 0.8 points | Row 16 | correct | 24.4 - 23.6 = 0.8. |
| 19 | 656 h memory "applied to the VSR model in other experiments" | Row 17 | correct | The quote matches. |
| 20 | Comparator rows use no LM (§V-A); proposed rows do not say | none | no quote | There is no claim row. This bullet matters because it sets the condition for claims 6 and 15. |
| 21 | Memory said to serve "any VSR model" (§II); two backbones tested | none | no quote | There is no claim row. |
| 22 | Ablation gaps 0.1 to 0.5 points | Row 18 | partly supported | The quoted values give gaps of 0.2 and 0.3. The 0.1 and 0.5 ends are not quoted. |
| 23 | 54.5% (Table VI) vs 54.1% (§V-E) | Row 19 | correct | Both values are quoted. |
| 24 | §V-G swaps the 512 and 1024 WERs of Table VIII | Row 19 | insufficient evidence | Only the §V-G text (42.0, 41.7) is quoted. The Table VIII values are not. |
| 25 | Large adds 122M (§V-A) vs 325M - 103M = 222M (§IV-B) | Row 19 | insufficient evidence | The arithmetic is right, but neither figure is quoted. The "(inference)" label is not needed for a subtraction. |

Central claim and confound: the review handles the confound in the distillation comparison (label quantity, single run, the Table IX spread). It does not handle the strongest confound in the SOTA verdict. SynthVSR and Auto-AVSR train on far more labelled, synthetic or automatically labelled data than the target's 433 h + 1,326 h. Saying the claim "fails" therefore needs the data scale stated next to it. The LM condition is also unresolved: the proposed rows' LM use is "not reported" (M07), yet they are compared with a no-LM figure.

Fairness: the [concurrent] and [later] labels are consistent with the dates. SynthVSR and Auto-AVSR are about 5 months before the target's arXiv release, and the authors cite SynthVSR (Base rows). Faulting the abstract's SOTA claim against [4] is therefore fair. The review does not present the authors' own statements as its own findings.

Novelty and absence: the review makes no "first" or "only" claim. The prior memory work is named ([2], [3]). Evaluator knowledge: the same group's CroMM-VSR (Kim, Hong, Park, Ro, IEEE TMM 2021) is a further cross-modal memory prior for VSR and could be named. This is optional.

Verdicts: no component is rated `ahead`. The M07 and M13 ratings of "not reported" and the M09 and M10 ratings of "not applicable" are consistent with the table text.

## Required fixes (ordered by impact)

1. **SOTA verdict (Verdict and M12):** State the training data behind SynthVSR 18.2% and Auto-AVSR 19.1% next to the target's 433 h + 1,326 h, and add a quote that shows 18.2% is the no-LM Large figure. Since the target's LM use is unreported (M07), either say the LM condition is unmatched or limit the claim to "unqualified in the abstract".
2. **"Best today" (M12, row 14):** Restrict the claim to public data, or name LP Conformer (about 12.8%, non-public data; check this against the source). Quote the LM condition for both 16.9% and 17.6% so that the two figures are comparable.
3. **M02 state of the art (row 8):** Quote the USR 2.0 row's setting (30 h labelled, model size, unlabelled data) to support "in that setting". Also note that USR 2.0 uses audio during training.
4. **Missing claim rows:** Add quotes for the LM bullet (§V-A), "any VSR model" (§II), the §III-B slot indexing, 28.7% (Table II), 59.9% (Table VI), the Table VIII 512 and 1024 values, the 122M and 222M parameter figures, and the 0.1 and 0.5 ablation ends.
5. **Table IX vs Tables III and IV:** Note that Table IX gives 41.5% and Tables III and IV give 41.6% for the same 656 h memory. Also note that the 223 h to 656 h change adds in-domain LRS3, so the spread is not only label quantity.
6. **RAVEn year:** Change "(2022)" for [6], [7] to give each work its own year (RAVEn is ICLR 2023).
7. **M12 usual approach:** State the usual evaluation design. Explain that the supervision counts cover only 41 of the 141 studies.
8. **Over-hedging:** Remove "(inference)" from plain arithmetic: 5.4, 3.4, 4.6% relative, 0.8 and 222M.

## Scores

- Procedure: 7/10. Every position has a location or citation, and the arithmetic checks out. Several load-bearing numbers and conditions lack quotes.
- Final text: 6/10. The distillation analysis is sound. The SOTA verdict and the "best today" line state more than the quoted evidence supports about data and LM conditions.
