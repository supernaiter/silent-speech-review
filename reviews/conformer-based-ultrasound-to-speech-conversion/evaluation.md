# Evaluation: Conformer-based Ultrasound-to-Speech Conversion

Date: 2026-11-21. Fallback evaluator (claim table only): no sources opened; each claim checked against the claim-table quote and location, and each position checked against the evidence cited for it.

## Claim checks

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target changes one component (M06): Conformer, alone or with bi-LSTM, replaces a 2D-CNN | Row 1 (Sec. 1, 3.2, 3.4) | correct | Quotes support all three parts. |
| 2 | Conformer "attends over the 64 beam lines of one frame" | Rows 2, 6 (Sec. 3.3) | insufficient evidence | Quote shows frame-level learning (one frame per output step). It does not show the 64 beam lines as the attention sequence. M05 gives 64x128 scanlines, but no row quotes this. |
| 3 | Conformer new to UTS (0 of 51); 8 prior multi-frame studies | Row 2, rows 27-28 (tally) | insufficient evidence | Tally only. No nearest prior (for example, earlier Transformer or attention mappers for ultrasound) is named as deciding the "0 prior". |
| 4 | [2] cut test MSE about 21% relative to a 2D CNN | Row 2, row 5 (Sec. 5 of [2]) | correct (quote) / contradiction | Quote supports 21%. But the M06 body says 0.366 to 0.315, which is a 13.9% relative reduction, not 21%. Either 0.366 is a different baseline row from the one behind the 21%, or one of the figures is wrong. |
| 5 | [2]: test MSE 0.366 to 0.315 | Row 10 (Table 2 of [2]) | insufficient evidence | Only 0.315 (3D CNN s=6) is quoted. The 0.366 value and its row label are not quoted. |
| 6 | Neither Conformer beats the baseline on MSE or MCD | Rows 3, 9, 17 | correct for MCD; insufficient for MSE | MCD: both variants are numerically worse for all four speakers (baseline 3.221/3.009/3.641/3.172). The baseline MSE row is not quoted. |
| 7 | Conformer Base is worse on MCD for three of four speakers | Rows 9, 17, 18 | wrong as worded | It is numerically worse for all four. The likely intended claim is "significantly worse for three (01fi, 03mn, 04me)". Significance is quoted only for 04me, not for 01fi and 03mn. |
| 8 | 03mn: 4.133 vs 3.641 dB, 13.5% relative | Rows 9, 17 | correct | 4.133/3.641 = 1.135. |
| 9 | Base MSE significantly worse for 03mn (p = 0.026) | Row 18 (Sec. 4.2) | correct | |
| 10 | bi-LSTM is level except MCD 04me (p = 0.002) | Rows 9, 18 | insufficient evidence | No quote has p = 0.002. Significance for 04me is quoted without a value. |
| 11 | Later re-implementation: 99.26% WER on TaL1 | Rows 3, 7, 11 | insufficient evidence | 99.26 appears only in the location note ("Overall row"), not in a quote. The TaL1 / single-speaker condition is not quoted. |
| 12 | 3D front end + Transformer: 15.93% WER | Rows 3, 7 | correct (number) | The design description ("3D front end", "multi-layer Transformer") is not in the quote. |
| 13 | 2D-CNN+BiLSTM 60.29% vs 3D-CNN+BiLSTM 36.46% | Row 7 | correct | |
| 14 | The later study found no public code, although the target points to Zenodo | Row 11 | partly correct | Both halves are quoted. "Zenodo" is not in the quote, which breaks off at "available at". |
| 15 | MUSHRA 32 vs 28; natural 96; p = 0.037; 14% relative | Rows 4, 15, 16 | correct | 32/28 = 1.143. |
| 16 | "its MCD does not move" (bi-LSTM) | Rows 9, 15 | wrong as worded | bi-LSTM MCD is higher for all four speakers and significantly higher for 04me (stated elsewhere in the review). Its own sentence in M06 contradicts this. |
| 17 | Spectral distortion is a weak indicator of lexical accuracy [3] | Row 13 | correct | |
| 18 | 31.64% WER "for 81 pooled TaL80 speakers" | Row 13 | insufficient evidence | The quote gives 31.64% only. The 81-speaker pooled condition is not quoted. |
| 19 | Listener transcription tests "date back to 2016" [4] | Row 14 | insufficient evidence | [4] supports a 2016 transcription test, not that the practice started then. Earlier ultrasound/optical SSI work reported intelligibility tests (inference, low confidence; for example, Hueber et al., Speech Communication 2010). |
| 20 | [5] baseline mean 2.148 dB on the same four speakers, custom MCD | Row 17 | insufficient evidence | No quote gives the column header showing 2.148 is the baseline, or that [5] used the same four speakers. |
| 21 | Abstract: no significant objective improvement | Row 18 | correct | |
| 22 | "Matched the performance of the baseline" (Abstract) | Row 18 | insufficient evidence | The phrase is not in any quote. |
| 23 | "Fewer parameters" false for bi-LSTM: 5.35M vs 4.09M | Row 19 | correct | |
| 24 | Real-time claim rests on training time only (30% / 80%) | Row 20 | correct | |
| 25 | Usual M06 approach: CNN regression, 31 of 51 | Row 5, rows 27, 29 | contradiction | The Appendix tally lists fully connected DNN 37 against CNN 31. DNN is the more frequent design, so "usual = CNN" needs a reason (for example, the post-2017 subset) or a change. Row 12 also carries a mismatched quote (test-set split) for the M12 counts. M12 "MCD plus MUSHRA, 21" counts MCD alone, not the combination. |

## Central claim and confounds

- Strongest confound: the M06 "behind" verdict rests partly on cross-paper comparisons. [2] reports MSE on a different corpus and speaker, with its own baseline. [3] [later] is a re-implementation evaluated on one TaL1 speaker, whereas the target uses four TaL80 speakers. The M06 body does mark the 99.26% figure as "one failed reproduction", but the Verdict states it with no caveat. The review never says that [2]'s data differ. The within-paper evidence (no win against its own baseline, significant MCD losses) is enough for "behind" by itself. The cross-paper numbers should be framed as context, not as head-to-head results.
- "Inter-frame context matters, and this Conformer lacks it": the evidence (Sec. 3.3) covers the Base model. Nothing is quoted from Sec. 3.4 to show that the bi-LSTM variant also runs within one frame rather than across frames. This position is stronger than its evidence for the bi-LSTM model.
- Fairness: [3] is correctly labelled [later] and is not presented as prior work. The significant degradations are reported by the authors in Sec. 4.2-4.3, and the review attributes them to "the results" rather than claiming them as its own finding. This is acceptable.
- Verdicts: M06 `behind` follows from the evidence once the confound wording is fixed. M12 `standard` and M13 `not reported` are consistent with the review's own evidence. No slot is marked `ahead`.

## Required fixes (ordered by impact)

1. Resolve the [2] contradiction: 21% relative (Verdict, M06 usual approach) against 0.366 to 0.315 (13.9%, M06 body). Quote the row that gives 0.366 and the baseline behind the 21%, and use one consistent figure. State that [2] used a different corpus.
2. Justify or correct "usual approach: CNN regression, 31 of 51" when the Appendix tally counts fully connected DNN in 37.
3. Change "Conformer Base is worse on MCD for three of four speakers" to "numerically worse for all four, significantly for three (01fi, 03mn, 04me)". Add quotes for the 01fi and 03mn significance and for p = 0.002 (04me, bi-LSTM).
4. In the Verdict, attach the condition to 99.26% / 15.93%: a re-implementation, a single TaL1 speaker, a different setup from the target's four TaL80 speakers. Add a quote that contains 99.26.
5. Support "this Conformer lacks inter-frame context" for the bi-LSTM variant with a Sec. 3.4 quote, or limit the claim to Conformer Base.
6. Replace "its MCD does not move" (M12): bi-LSTM MCD is higher for all speakers and significantly higher for 04me.
7. [5] comparison: quote the column header showing that 2.148 dB is the baseline mean, and the passage showing that the same four speakers were used.
8. Quote the "81 pooled TaL80 speakers" condition for 31.64%, or drop the condition.
9. Novelty ("0 prior studies among 51"): name the nearest prior attention or Transformer-based ultrasound-to-speech mappers that the audit checked.
10. Soften "Listener transcription tests date back to 2016 [4]" to "were in use by 2016 [4]", or cite an earlier ultrasound SSI intelligibility test.
11. M12 usual approach: the count of 21 is MCD alone. Give the MCD-plus-MUSHRA co-occurrence count, or reword. Replace the mismatched quote in claim row 12.
12. Close the remaining claim-table quote gaps: the 64 beam lines (Sec. 3.3), "matched the performance of the baseline" (Abstract), "Zenodo" (Sec. 5), the baseline MSE row (Table 1), and the 3D front end + Transformer design of [3].

## Scores

- Procedure: 6/10
- Final text: 6/10

The position is clear, and the within-paper findings (no objective gain, the parameter-count contradiction, the training-time-only real-time claim) are well supported. Most of the defects are unquoted conditions, plus one numeric contradiction.
