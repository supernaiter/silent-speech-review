# Evaluator: a language model separate from the writer

Target review: compact.md for Ephrat & Peleg, "Vid2speech: Speech Reconstruction from Silent Video" (ICASSP 2017, arXiv:1701.00495).
Date: 2026-11-25. Inputs: the evaluator brief and compact.md only (review text plus its claim table). No sources were re-opened, so every check runs against the claim-table quotes and locations. Outside knowledge that I could not locate is marked "unverified".

## Claim table

| No | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Verdict: M05 full face with K = 9 frames; M06 CNN to LSP, keeps 8th-order LPC and unvoiced excitation | Claim rows 1, 11 (t9, t14, t72, c2) | Insufficient evidence | K in {1..9} and face crop are quoted. No quote gives "8th-order" or says that K = 9 was the configuration used. |
| 2 | Verdict: 82.6% vs 40.0% audio-only, GRID S4 (Table 2) | Row 2 (t35, c1) | Correct | The numbers match for both papers. |
| 3 | Verdict / M12: Vid2speech listeners chose from the GRID vocabulary, the comparator's listeners typed | Rows 2, 20 (t30, c3) | Correct | "entering the words they heard" supports free entry. |
| 4 | Verdict: the face-over-mouth claim rests on one figure with no split or metric | Rows 3, 9 (t8, t28, t70) | Correct | t28 says only "final network test error". |
| 5 | Verdict: "Re-run later, it scores 44.92% ... against 14.08%" | Row 4 (l1, l2) | Correct numbers, misleading placement | The sentence follows the face-over-mouth sentence, and "it" can be read as the face-input claim. The M05 section says that the gap compares whole systems, but the Verdict does not. |
| 6 | Verdict / Outrun: OOV 51.6% vs 10.0% chance vs 93.4% all-digits; 44.8% relative drop | Rows 5, 25 (t42, t47) | Correct | (93.4 - 51.6) / 93.4 = 44.75%, which rounds to 44.8%. The t47 caption supports the column reading. |
| 7 | M05: the comparator used a tracked mouth centre or a lip AAM | Row 7 (c7) | Correct | |
| 8 | M05 SOTA: Lip2Wav calls the architecture "very inadequate"; 14.08 vs 44.92, mean of 4 speakers | Row 8 (l6, l1, l2, l5) | Correct | |
| 9 | M05: "40% lower test error at K = 9" | Row 9 (t8) | Insufficient quote | The caption says "in the best configuration". No quote ties that configuration to K = 9. |
| 10 | M06: kept the comparator's LPC "to isolate the effect..." and its unvoiced excitation, matching GMM UNV | Row 11 (t72, t52, c2) | Correct | |
| 11 | M06 SOTA: Kefalas et al., best GRID row is an end-to-end WGAN at 4.07% WER | Row 12 (k1, k3) | Insufficient quote | Only the WGAN row is quoted. "Best GRID row" needs the other rows, including Kefalas's own model. |
| 12 | M06: 30.84 points (68.7% relative) on GRID; 44.26 points on TCD-TIMIT | Row 13 | Correct | Arithmetic checked: 44.92 - 14.08 = 30.84, 30.84 / 44.92 = 68.7%, and 75.52 - 31.26 = 44.26. |
| 13 | M06: the comparator's pixel-based DNN (2D-DCT input) scored 26.9%, so pixel input alone does not explain the gain | Row 15 (c6) | Insufficient quote; judgment too strong | c6 does not mention 2D-DCT. A 2D-DCT is a hand-crafted transform of the pixels, not raw-pixel input, and a DNN differs from a CNN, so the row does not isolate "pixel input". |
| 14 | M06: the comparator measured a 7.5-point gain from real voicing | Row 16 (c10) | Correct | |
| 15 | M12 SOTA: unseen GRID speakers at 16.05% WER (Table VII); Lip2Wav adds raters | Row 19 (k2, l7) | Partly insufficient | 16.05 matches the WGAN row. No quote supports "adds raters", since l7 is only the ASR footnote. |
| 16 | M12: "Both state 19% chance" | Row 21 (t39) | Insufficient quote | Only the target's 19% is quoted. No quote from [2] is given. |
| 17 | Outrun: "significantly more intelligible" has no test; 38 sequences pooled across three clip types | Row 22 (t38, t31, t29) | Correct | |
| 18 | Outrun: AV 79.9 vs AO 82.6 (-2.7); comparator +11.9; "not distinguishable" with pooled counts | Row 23 (t36, t35, c1) | Arithmetic correct; last clause too strong | The arithmetic is right. "Not distinguishable" is a statistical claim made without counts, so it should read "cannot be shown distinguishable from what is reported". The third value (79%) in the t36 Table 2 row is not explained. |
| 19 | Outrun: "as done there" holds for speaker and training size (800 of 1,000) | Row 24 (t24, c8) | Correct | |
| 20 | Ledger tallies M05, M06, M12 | Appendix | Not checked (exact tallies) | |
| 21 | References [1]–[4] bibliographic data | Reference list | Unverified | All four entries are plausible. The pages for [3] (13793–13802) and for [4] (vol. 32, 2255–2268) should be checked against the publisher records. |

## Findings (numbered, ordered by impact)

1. **The Verdict sentence about the Lip2Wav re-run is misleading.** "Re-run later, it scores 44.92% GRID WER against 14.08% for Lip2Wav" comes right after the face-over-mouth sentence, so a reader can take it as evidence against the face-input choice. The M05 section says correctly that "the gap compares whole systems, not inputs". Add that qualifier to the Verdict or move the sentence. Also say that the gap is measured with Lip2Wav's ASR (Google API) and on Lip2Wav's speakers, not on S4 only.
2. **The inference about the comparator's pixel DNN overreaches (M06).** The claim that the DNN takes 2D-DCT input has no quote (c6 shows only "DNN UNV 26.9 45.8"). If the input is 2D-DCT, it is a hand-crafted transform, so the row cannot show that "pixel input alone does not explain the gain". The review would need a raw-pixel arm with matched architecture. Either quote the input type from [2] (Table 4) and recast the claim as "a DNN on DCT pixel features scored 26.9%", or drop the conclusion.
3. **"Best GRID row" in Kefalas et al. has too thin a quote (M06 state of the art).** Only the WGAN row is quoted. Quote the rest of Table IV, including the authors' proposed model, or reword to "the end-to-end WGAN row". The same applies to the 16.05% unseen row (M12). Later GRID results may also beat 4.07% WER, but I could not locate their values, so they are unverified. Candidates to check are SVTS (Mira et al., 2022), VCA-GAN (Kim et al., NeurIPS 2021) and the speech-unit lip-to-speech work (Choi et al., Interspeech 2023). In any case, WERs from different ASR models (Kefalas's ASR vs Lip2Wav's Google API) are not comparable across rows. The review hints at this but should say it where it gives the 4.07% figure.
4. **The M05 verdict "standard" sits against the review's own tally.** The review counts 76 mouth or lip crops against 15 full face, so the target's full-face input is the minority design. Either explain why "standard" still applies (for example, that the input class is ordinary and only the crop differs) or reconsider the label under the SKILL.md verdict rules. Most of the 15 full-face studies probably post-date 2017 (inference), and the review does not discuss that either.
5. **"Both state 19% chance" (M12) has no quote from [2].** Add the comparator's chance statement, or attribute the 19% figure to the target only.
6. **The "not distinguishable" claim in "Where the claims outrun the evidence" is stated as fact.** No counts are available, so this is an inference about missing evidence and should be phrased that way. Also explain the third Table 2 value (79%) in the t36 row, or confirm that it does not affect the comparison.
7. **The K = 9 and 8th-order LPC details have insufficient quotes** (Verdict and M05). The Fig. 2 caption says "best configuration" without naming K. Add the sentence that fixes K = 9 and the LPC order.
8. **The authors' claim of "best results of [10]" was not checked against the voiced rows of [2].** The comparator reports a 7.5-point gain from real voicing (c10), so its best audio-only score is probably above 40.0% (inference). However, that gain uses a voicing source the target does not have. The review compares like with like (GMM UNV) and is correct to do so. It should still note that the authors' "best results" wording names the matched unvoiced row, not the comparator's best row.
9. **"Lip2Wav adds raters to ASR WER" (M12 state of the art) has no supporting quote.** l7 is only the ASR footnote. Add the passage on Lip2Wav's human evaluation.
10. **M12 state of the art gives a system score, not an evaluation protocol.** Because the component is the evaluation method, the state-of-the-art line should name the protocol: one fixed ASR model checked on real audio, unseen-speaker splits, objective metrics (STOI, ESTOI, PESQ) and a MOS with raters. The 16.05% WER figure is secondary to that.
11. **Fairness and chronology are handled correctly.** Lip2Wav (2020) and Kefalas et al. (2023/2024) are tagged [later] and are not treated as prior work or as missed citations. The review does not claim as its own anything the authors already report: it attributes the OOV concession to the authors (Sec. 4.4). No absence or novelty sentences need checking.
12. **The bibliographic details of [3] and [4] are unverified.** Confirm the pages and volume against the CVPR 2020 and IEEE/ACM TASLP 2024 records.

## Central claim and confound

The strongest confound is the change of response format: forced choice among the GRID options in the target, against free entry with replays in [2]. A different listener pool (MTurk against laboratory listeners) and different test sentences under a random 80/20 split add to it. The review handles the format confound well (Verdict, M12) and gives the speaker and training-size match its due. It should also name the listener-pool difference and the non-identical test sets.

## Required fixes (by impact)
1. Qualify the Verdict sentence on the Lip2Wav re-run as a whole-system, different-protocol comparison (finding 1).
2. Fix or drop the inference about the comparator's 2D-DCT DNN (finding 2).
3. Quote the full Kefalas Table IV and Table VII, or reword "best", and note that the ASR models differ (finding 3).
4. Justify or revisit the M05 "standard" verdict given the 76-to-15 tally (finding 4).
5. Add the missing quotes: 19% chance in [2], K = 9, LPC order, Lip2Wav raters (findings 5, 7, 9).
6. Recast "not distinguishable" as an inference (finding 6).

## Scores
- Procedure: 7/10. The claim table is complete and the arithmetic is correct, but several quotes are too thin for the claim they carry.
- Final text: 7/10. The review takes a clear position and handles the main confound, but the Verdict juxtaposition and the DCT inference overreach.

Strengths, briefly: the review identifies the format confound correctly, notes that the authors chose a matched unvoiced comparator row, and states the OOV ten-way-choice limitation precisely.
