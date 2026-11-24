# Evaluator: a language model separate from the writer

Target: Shandiz and Tóth, "Voice Activity Detection for Ultrasound-based Silent Speech Interfaces using Convolutional Neural Networks", arXiv:2105.13718 (2021).
Date: 2026-11-24. Input: compact.md only (review text and claim table). No sources were reopened, so this pass works like the fallback: it checks each claim against its claim-table quote and location, and adds outside knowledge marked "unverified" where it cannot be traced to a source.

## Claim check

| No | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Two components changed: a single-frame CNN on ultrasound frames (M06), with WebRTC labels from the audio (M02) (Verdict) | Claim rows 1, 7, 11 (Sec. 1, 4.2, 5.1, 5.3) | correct | The quotes support the description. |
| 2 | Accuracy 0.852 is about 11 points above the majority class; 43% of silence frames are kept (Verdict) | Rows 4, 22, 23 (Tables 5–6) | correct | The arithmetic checks: 8514/11453 = 74.3%; (1671+8096)/11453 = 0.853; 1268/2939 = 43.1%; kappa recomputed from the matrix = 0.574, which matches 0.57. The review assumes the "Negative/Positive" rows are true labels. That reading fits recall 0.95 = 8096/8514. Under the transposed reading, recall would be 0.865. So the orientation is consistent, but it is not confirmed by a quoted header. |
| 3 | MCD changes of 0.01 to 0.05 (Verdict) | Row 5 (Tables 4, 7) | correct | 3.20→3.15, 3.29→3.28, 3.08→3.05, 3.13→3.12. Every change is a decrease, toward the ultrasound VAD. See finding 4. |
| 4 | "Slightly better MSE", 0.26 against 0.29 with 180 ms kept (Where the claims outrun) | Row 24 (Tables 4, 7) | insufficient quote | No column headers are quoted. The rows have two MSE-like columns per condition. With 180 ms kept, the first column worsens (0.259 → 0.35 for BiLSTM; 0.30 → 0.38 for Conv3d) while the second improves (0.29 → 0.26; 0.33 → 0.27). The review cites only the improving column. |
| 5 | Specificity 57%; speech is the positive class (Where the claims outrun) | Rows 23, 26 | correct | 1671/2939 = 56.9%; 8096/8514 = 0.951. Both are marked as inference. |
| 6 | Single-frame CNN, no temporal context (M06) | Row 7 (Sec. 4.2) | correct | The quote "single" is cut off, but Sec. 4.2 is cited. |
| 7 | [2]: 96.99% speaker-dependent, 74.07% on held-out speakers, 24% relative drop (M06, M12) | Rows 9, 17 (Cornu Tables 1, 3) | insufficient quote | The values are in the quoted rows, but the headers that show which column is VAD (as opposed to voicing) are not quoted. In Table 3, STATIC and STACK3 both score 59.02 in the first column, which suggests a majority-class floor. The arithmetic (22.92/96.99 = 23.6%) is right. Sharma [4] Table 1 lists the same 2015 CNN as 96.7 / 72, close to but not the same as [2]'s own numbers. |
| 8 | [4]: CNN-LSTM, 14-frame smoothing, 92.2% on unseen GRID speakers, 96.5% speaker-dependent (M06 SOTA) | Row 8 (Sharma Sec. 3.3, Table 1) | insufficient quote | The Table 1 row has four numbers (96.5, 99, 92.2, 97), and no headers are quoted. "Frame accuracy" and the split into speaker-dependent and speaker-independent columns need the header. It is also not shown that the 92.2 figure includes the 14-frame smoothing. |
| 9 | [4] split: 27 / 3 / 2 speakers (M12 SOTA) | Row 15 | correct | |
| 10 | One TaL1 speaker; 1015 / 50 / 24 files; TaL1 has six sessions; the corpus paper leaves one session out (M12) | Row 16 | correct | The paper lists the split as train / test / validation = 1015 / 24 / 50. The review's order 1015 / 50 / 24 is train / validation / test but is unlabelled. The labels should be added. |
| 11 | [7]: "MUSHRA naturalness 1.19" (M12) | Row 17 (Gosztolya Sec. 4.1.2) | insufficient quote | The quote says "mean naturalness score of only 1.19". MUSHRA is normally 0–100, so 1.19 looks like a 1–5 MOS-type scale. The test name is not in the quote. [7] also covers a different task (synthesis) on different (Hungarian) data. |
| 12 | MCD is the usual metric (21 of 51); SOTA [8] reports ASR WER (M12 synthesis) | Rows 19, 20 | correct, but incomplete | [8] is correctly labelled [later] and is not treated as prior work. The SOTA line gives no value. The claim table holds WER 31.64%, but whether that was measured on TaL is not in the quote. |
| 13 | Retained silence raises MCD (Table 3) and lowers MSE (Sec. 5.2) | Rows 21, 24 | correct | The quotes support both directions. |
| 14 | M02 table row: "Audio-derived labels (pattern match 22)" | Component table vs M02 text and Appendix | wrong | In the text and Appendix, 22 is the count for manual annotation. Audio-derived labels are forced alignment (17) plus acoustic VAD (6). The table contradicts the section. |
| 15 | M02 verdict "standard" | M02 section, Appendix | judgment not carried | An acoustic VAD as the label source is the least common design (6 of 119). The two deciding priors used alignment labels, not a VAD. "Standard" holds only if the slot is read as "audio-derived". If so, the review should say that, and fix finding 14. |
| 16 | "Six earlier non-acoustic VAD studies tested held-out speakers" (Verdict) vs "46 mention a held-out-speaker test" (M12) | Verdict, M12, Appendix | internally confusing, not wrong | The Appendix explains that 6 is the number of studies whose snippets were checked and 46 is the pattern-match count. The Verdict should say "six checked" so the reader does not see a contradiction. |
| 17 | M12 verdict "behind the best comparable work [4]" | M12 section, Appendix | partly carried | The ledger count (6) and the deciding priors ([4], [2]) are named, and the effect is restated. The comparison crosses modalities: lip video on GRID with 33 speakers versus ultrasound with one speaker. A held-out-speaker ultrasound corpus (TaL80) had been released only about six months earlier ([concurrent]). See finding 3. |
| 18 | "Only the tongue image as input is new" (M06) | Rows 2, 9 | plausible, unverified | I know of no earlier image-based ultrasound-tongue VAD. [3] uses raw echo variance, not images. Unverified. |
| 19 | Reference [4] authors "A. K., P." | Reference list | likely wrong (bibliographic) | The author list appears to be Sharma, Aralikatti, Margam, Thanda, Roy, Kandala (Pujitha Appan), Venkatesan. "A. K., P." looks like a mis-parsed "Kandala, P. A." Medium confidence. |
| 20 | Reference [1] as an arXiv preprint only | Reference list | incomplete (unverified) | To my knowledge the paper was published at TSD 2021 (Text, Speech, and Dialogue, LNCS). If so, the published version should be cited next to the arXiv one. |
| 21 | Reference [8] carries "[later]" twice | Reference list | formatting | The label appears twice. Keep one. |
| 22 | M05 "82 fps"; M08 "mel to WaveGlow" | Component table | no quote | Neither has a claim-table row. Add a quote and location, or drop the detail. |

## Required fixes, ordered by impact

1. **M02 table count is wrong (row 14).** "Audio-derived labels (pattern match 22)" uses the manual-annotation count. Change it to forced alignment 17 and acoustic VAD 6, or name manual annotation (22) as the usual approach. Then reconsider whether "standard" fits, since the acoustic VAD design is the rarest of the three (row 15).
2. **MSE comparison picks one column (row 4).** Quote the Table 4 and Table 7 column headers. Report that the other MSE column with 180 ms kept moves the opposite way (0.259 → 0.35; 0.30 → 0.38). This supports the review's own "confounded equivalence" point.
3. **The strongest confound in the M12 "behind" verdict is the modality and corpus gap.** [4] tests lip video on GRID. The target tests ultrasound on one TaL1 speaker, and the only multi-speaker ultrasound corpus (TaL80) was [concurrent]. The verdict should state this. It should also make the session-split question (TaL1's six sessions) the like-for-like criticism, instead of implying that a GRID-style speaker-independent protocol was readily available.
4. **MCD direction is not worked out (rows 3 and 13).** The review argues that the ultrasound VAD keeps more silence and that more silence raises MCD (Table 3). Yet every MCD in Table 7 is lower than in Table 4. Either explain this (for example, the test data were trimmed differently, which is the question to the authors) or state it plainly. As written, the confound argument predicts the wrong direction for MCD.
5. **Headers for comparator numbers (rows 7, 8).** Quote the column headers of [4] Table 1 and [2] Tables 1 and 3, and confirm that 92.2% includes the smoothing. The SOTA number that carries the M12 verdict rests on an unlabelled row.
6. **[7] scale (row 11).** Drop "MUSHRA" unless the source names it, or give the scale (1.19 on a 1–5 scale is plausible).
7. **SOTA value for synthesis evaluation (row 12).** Add the WER value from [8] (31.64%) and its test set to the SOTA line, as the brief requires a year, metric and value.
8. **Verdict wording, "six" versus "46" (row 16).** Write "six checked studies (of 46 pattern matches)".
9. **Label the split (row 10).** Write train 1015 / validation 50 / test 24.
10. **Bibliography (rows 19–21).** Fix the [4] author string, add the TSD 2021 version of [1] if confirmed, and remove the duplicate "[later]" on [8].
11. **Unquoted details (row 22).** Add sources for 82 fps and WaveGlow.

Possibly stronger or more recent visual-VAD state of the art before the target (all unverified; for the writer to check, not required fixes): Tao and Busso, bimodal recurrent end-to-end audiovisual speech activity detection (Speech Communication, 2019), which reports visual-only speaker-independent results; Guy et al., "Learning Visual Voice Activity Detection with an Automatically Annotated Dataset" (arXiv 2020, ICPR 2021), which falls within six months of the target and should not be treated as missed prior work.

## Scores

- Procedure: 7/10. The claim table is complete, the inference is marked, and the arithmetic checks. Column headers are missing for the key comparators, and one count is carried over wrongly.
- Final text: 7/10. The confusion-matrix analysis and the majority-baseline point hold up. The M02 table error, the one-sided MSE column and the MCD-direction gap weaken the "where the claims outrun the evidence" section.

The confusion-matrix arithmetic (accuracy, kappa, recall, specificity) was recomputed and agrees with the review.
