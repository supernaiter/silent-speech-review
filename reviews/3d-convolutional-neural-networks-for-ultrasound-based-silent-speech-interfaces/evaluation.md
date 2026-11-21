# Independent evaluation: 3D Convolutional Neural Networks for Ultrasound-Based Silent Speech Interfaces

Date: 2026-11-21. Fallback evaluator (claim table only): one pass over the compact review and its claim table, with no sources reopened. Knowledge of the wider literature comes from memory and is marked as such.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | (2+1)D network over 5 frames, stride 6, 25-frame span | Row 1 (t1, t18) | correct | w = 4·6+1 = 25 matches. |
| 2 | 25 frames ≈ 300 ms | Row 1; M05 table cell | insufficient evidence | No quote gives 82 frames/s. 25/82 = 305 ms if each frame counts as a full period; 24 intervals give 293 ms. Either way "about 300 ms" holds. |
| 3 | Test MSE 0.336 → 0.315, 6.3% relative | Row 3 (t28, t24) | correct | (0.336−0.315)/0.336 = 6.25%. |
| 4 | Baseline retrained with changed input/output sizes | Row 3 (t61) | correct | The quote supports it. |
| 5 | FCN and 2D CNN see one frame; no 2D model gets 25 frames | Rows 4, 20 (t13, t18) | insufficient evidence | t13 describes FCN layer sizes, not the input span. No quote shows single-frame input. The CNN+LSTM input span is never stated, yet it is the headline comparator. |
| 6 | No seeds, run counts or checkpoint selection | Row 21 (t42) | insufficient evidence | This is an absence claim, and the quote does not bear on it. It is plausible, but it needs a statement that the paper was checked in full for this. |
| 7 | Stride chosen on 41 development sentences | Row 21 (t19, t5) | correct | |
| 8 | "14% absolute" R² is really +0.085, about 14% relative | Row 18 (t31, t21, t25) | correct | 0.085/0.598 = 14.2%. |
| 9 | 21% MSE cut is against the FCN; 13.9% against the 2D CNN | Row 19 (t30, t22) | correct (numbers); insufficient (attribution) | (0.400−0.315)/0.400 = 21.3% and (0.366−0.315)/0.366 = 13.9%. The paper's own "21%" sentence is not quoted. |
| 10 | Conclusion concedes that more comparison is needed | Row 17 (t37) | correct | |
| 11 | 946 vs 964 inconsistency | Row 22 (t6, t7) | correct | |
| 12 | Target omits F0; metrics do not track perceived quality | Row 15 (t10, t38) | correct | |
| 13 | One speaker reading aloud; no silent articulation | Row 23 (t2) | correct | |
| 14 | Lip reading used spatiotemporal convolution since 2016 [2], [3] | Row 2 (c8, c9); Appendix row 36 | insufficient evidence / internal tension | The quotes show that [2] and [3] use spatiotemporal convolution. They do not show that it was the usual front end. Appendix row 36 gives 63 of 576 pre-2020-04 studies (about 11%) with 3D convolution, which does not support "usual" at the target's date. |
| 15 | [concurrent] Ultra2Speech "already" split 3D convolution into 2D + 1D | Row 2 (c10), row 9 (c11) | wording wrong | c10 says "parallel decomposition of a chunk". That is not clearly the same as a (2+1)D factorization. "Already" claims priority over a work the review itself labels concurrent. |
| 16 | 380 of 1,342 articulator-video studies use 3D convolution, against 255 CNN+RNN | Row 7 (Appendix) | correct (tally); wording overstated | 28% is the largest share, not a majority. "Most common" is accurate; "the usual front end" overstates it. |
| 17 | Frame-wise DNN (37) or CNN (31) of 51 ultrasound-to-speech studies | Row 6 (Appendix) | correct (tally) | Plausible usual approach. |
| 18 | Tongue2Speech 15.93% WER; 3D-CNN+BiLSTM baseline 24.15% | Row 8 (c12, c13) | correct | Not directly comparable with the target: different data, metric and language. The review does not say so. |
| 19 | Tongue2Speech 31.64% multi-speaker; MSE called "weak evidence of lexical accuracy" | Row 14 (c14, c15) | partly insufficient | The quote is cut off at "are weak". The words "of lexical accuracy" are not quoted. |
| 20 | Tongue2Speech bibliographic entry (Interspeech 2026, pp. 6856–6860) | Reference 7 | insufficient evidence | Not verifiable without sources. |
| 21 | None of 140 ultrasound studies uses 3D convolution before 2020-06 | Row 9; Appendix row 37 | insufficient evidence / inconsistency | The cutoff is 2020-06 here but 2020-04 in M12 and Appendix row 36. I know of no earlier ultrasound-to-speech work with 3D convolution (memory; low confidence). Ultrasound tongue-tracking work around 2019 used ConvLSTM, not 3D convolution. |
| 22 | Development MSE 0.380 (2017, five frames) → 0.321, 15.5% | Row 10 (c3, t24) | arithmetic correct; comparison unsound | This is a cross-paper comparison. The target's own single-frame FCN (dev 0.408) is worse than the 2017 single-frame DNN (0.384). That shows the preprocessing or targets differ, so the 15.5% is not a like-for-like gain. The review states it without a caveat. |
| 23 | Stacking 5 frames gained 1% (0.384 → 0.380); span about 61 ms | Row 11 (c2, c3, t64) | number correct; span insufficient | No quote shows that the 2017 frames were consecutive at 82 frames/s. 5 frames span 49 ms between centres or 61 ms as frame periods, so the convention needs stating. |
| 24 | [5] 23 listeners; [6] 24 listeners on the same 310/41/87 split; same speaker | Rows 5, 13 (c4, c6, c7) | partly insufficient | Listener counts are supported. The c6 quote shows only "310". Neither 41/87 nor the same speaker is quoted for [5] or [6]. |
| 25 | M12 "behind": MCD 21/51, MUSHRA 14/51; four pre-2020-04 MUSHRA studies | Rows 12, 13, 41 | insufficient evidence | No count is given for MSE/R²-only studies, and the four MUSHRA studies have no dated denominator. So "behind typical practice" cannot be weighed against how common MSE-only evaluation was. |

## Central claim and confounds

The strongest confound is input context. The 3D network sees 25 frames and the 2D baselines see one. The review handles this well for the FCN and 2D CNN. It leaves open the context of the CNN+LSTM, the one comparator the abstract's claim rests on. The baseline-strength confound (a retrained CNN+LSTM, with no MSE in its original study) is handled. Absolute versus relative change is handled (6.3%, the 14% R² correction). One confound is not handled: the cross-paper starting point in claim 22.

The target's authors present the (2+1)D structure as borrowed from video ("a similar (2+1)D network structure"). The review's "not new" therefore repeats the authors' own framing and should credit it rather than present it as the review's own finding.

## Required fixes, ordered by impact

1. M06: qualify or drop the 0.380 → 0.321 (15.5%) comparison with the 2017 study. The target's own single-frame FCN (0.408) is worse than the 2017 single-frame DNN (0.384), so the setups differ.
2. Verdict and M06: "usual lip-reading front end since 2016" conflicts with Appendix row 36 (63 of 576 pre-2020-04 studies). Restate as "established in lip reading by 2017 [2], [3]", give the dated CNN+RNN count beside it, and call 380/1,342 "most common", not "usual".
3. Verdict: remove "already" for the [concurrent] Ultra2Speech [4], and check that its "parallel decomposition" really is a 2D-spatial plus 1D-temporal split.
4. Context confound: state the CNN+LSTM's input span, and add a quote that shows the FCN and 2D CNN take a single frame (t13 does not).
5. M12 "behind": give the ledger count of studies that report only MSE/R² and the dated denominator for the four MUSHRA studies. Otherwise soften to "below the group's own earlier practice".
6. Use one date cutoff (2020-04 or 2020-06) across M06, M12 and the Appendix, and justify it against the target's submission date.
7. Fill the claim-table gaps: 82 frames/s; the same speaker and the 41/87 split for [5] and [6]; "of lexical accuracy" for [7]; the paper's own "21%" sentence; "training speed claimed, not measured" (M13); and a full-text check for the no-seeds absence claim.
8. State the span convention for 61 ms and 300 ms (frame periods or intervals), and confirm that the 2017 five frames were consecutive at the same frame rate.
9. M06 state of the art: note that Tongue2Speech's WER comes from different data and a different metric, so it is not directly comparable to the target's MSE.
10. Fairness: credit the authors with presenting (2+1)D as adapted from video work, rather than presenting "not new" as the review's own finding.

## Scores

- Procedure: 7/10. The claim table is mapped row by row and the arithmetic is shown. Several quotes are truncated or do not reach the claimed condition, and the date cutoffs disagree.
- Final text: 7/10. The position is clear, the confounds are mostly named and the overclaims in the paper are well caught. Two positions run ahead of the evidence: the cross-paper 15.5% and "usual since 2016".
