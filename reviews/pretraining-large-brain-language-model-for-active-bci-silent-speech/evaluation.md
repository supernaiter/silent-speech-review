# Independent evaluation: Pretraining Large Brain Language Model for Active BCI: Silent Speech

Date: 2026-11-20. Fallback evaluator (claim table only, no source access). Input: the compact review and its claim table. Arithmetic was recomputed from the Table 1 and Table 2 rows quoted in the claim table. Statements about outside work come from the evaluator's own knowledge and are marked with their confidence.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | 22.61M-parameter model, about 105 h of unlabeled EEG (Verdict) | Claim rows 1, 5; Table 1 row | correct | "22-million-parameter" and "22.61 M" are both quoted. The quote does not say the 105 h come only from the 12 participants; that rests on Sec. 4.2.1 as located, with no quote. |
| 2 | Du-IN: in-domain masked pretraining with a from-scratch control and six seeds; 56.29% to 62.70% on 61 words [2] | Rows 2, 6 | correct | Both values and "six different random seeds" are quoted. The row without pretraining is taken as the from-scratch control, which is a reasonable reading. |
| 3 | Gain from scratch: 35.3% to 39.6% (Table 1) | Rows 8, 13 | correct | The row means recompute to 35.28 and 39.58. |
| 4 | "No seeds" (Verdict, M12 row, outrun list) | Row 14 | insufficient evidence | The quote says only that results come from the test session. An absence claim needs a location showing that no seed statement exists. |
| 5 | 7.3-point margin = 4.3 (pretraining) + 3.0 (backbone vs TCNet); model about 288 times larger | Rows 3, 13 | correct | 39.6 − 32.3 = 7.3; 35.3 − 32.3 = 3.0; 22.61M / 78.62K = 287.6. |
| 6 | Participants mouth the words (Appendix B.1) | Row 17 | correct | "articulation attempts without emitting sounds" is quoted. |
| 7 | No EMG control; 1–75 Hz band; ICA rejection at 90% confidence (Appendix B.2) | Row 17 | insufficient evidence | The only B.2 quote is about average re-referencing. Neither the band, the ICA threshold nor the missing EMG channel is quoted. |
| 8 | 6.4 points (11.4% relative) vs 4.3 points (12.2% relative) | Row 7 | correct (arithmetic) | 6.41 / 56.29 = 11.4%; 4.3 / 35.3 = 12.2%. "The same effect size" is too strong: the tasks are 61-word sEEG and 24-word EEG with different chance levels. |
| 9 | Four of 12 participants fall (S01, S03, S04, S06); S09 +18.4, S10 +14.5; mean gain without them 1.9 | Row 8 | correct | Differences: −2.0, +3.6, −0.3, −1.0, +1.8, −0.2, +2.1, +2.6, +18.4, +14.5, +4.9, +7.3. The mean of the other ten is 1.88. |
| 10 | ASTP adds 2.7 word points over MSTP alone | Row 9 | correct | 35.3 + 1.6 = 36.9, and 39.6 − 36.9 = 2.7. |
| 11 | ASTP adds 2.2 semantic points | Row 9 | insufficient evidence | No from-scratch semantic baseline is quoted, and it is unclear whether the 2.2 uses 42.8 or 47.0. The quote names the objective "FSTP", but the review calls it ASTP without saying they are the same. |
| 12 | LaBraM 20.6% here, 11.53% in Du-IN | Row 10 | correct | Both values are quoted. |
| 13 | [3]: LaBraM no better than compact CNNs on speech EEG; all five models at chance on unseen subjects (five-class imagined) | Row 10 | insufficient evidence | No quote from [3] is given; the row only cites c10. |
| 14 | "Generic pretraining fails in both" | Row 10 | wrong as stated | Two LaBraM results and one later benchmark do not show that generic pretraining fails. From memory (medium confidence), CBraMod (ICLR 2025) reported a gain over LaBraM and from-scratch baselines on the BCI Competition 2020-3 five-class imagined-speech set. |
| 15 | M06 usual approach: other 48, CNN 37, transformer 12 | Rows 11, 26 | wrong as stated (ordering) | The Appendix lists other 48, then CNN 37, then SVM 17, then linear, and so on. Listing transformer 12 third leaves out higher-ranked families. |
| 16 | M06 state of the art: 96.4%, four covert syllables, 64-channel EEG, 10 participants, 2019 [4] | Row 12 | no quote / mismatch | The quote in the row is "Subjects 12", which matches the target, not [4]. None of 96.4%, four syllables, 64 channels or 10 participants is supported. A 2019 value is also unlikely to be the current best without a check of later work. |
| 17 | From scratch: 35.3 vs EEGNet 30.5 (8.54K) and TCNet 32.3 (78.62K) | Row 13 | correct | All values are quoted. |
| 18 | "Significant improvement of +7.3%" with no test; per-participant range 11.7% to 73.8% | Row 14 | correct | The quote is exact, and 11.7 (S06) and 73.8 (S01) are the minimum and maximum of the row. |
| 19 | Semantic mean 42.8% (§5.1) vs 47.0% (Abstract, Table 2) | Row 15 | correct | The Table 2 per-participant row averages to exactly 47.0 (564.0 / 12), so 42.8 is the inconsistent value. The review can say this plainly. |
| 20 | "Large brain language model": pretraining only on the 12 test participants; cross-subject pretraining "has failed so far" [3] | Row 16 | partly supported | Within-dataset pretraining is plausible from the quotes. "Has failed so far" rests on one later preprint and is too strong. The review does not say whether the 105 h include the held-out test sessions (possible leakage), and the quotes do not settle it. |
| 21 | Future-prediction priority claim (§3.3.4); forecasts diverge beyond 120 ms (§5.3) | Row 18 | correct | Both are quoted. The review does not name prior forecasting or autoregressive EEG/iEEG pretraining that would test the "first" claim (see fixes). |
| 22 | Hardware savings untested (§5.3) | Row 18 | insufficient evidence | No quote is given. |
| 23 | M05: 128-channel Neuroscan, 122 EEG, 1000 Hz | Row 17 | partly supported | 122 channels is quoted; 1000 Hz and the Neuroscan device are not. |
| 24 | Appendix M03 state of the art: 23.7% WER [5] [later] | Rows 22, 27 | contradiction | The body gives Du-IN [2] as the M03 state of the art. [5] is an audio-visual/lip-reading recognition paper, is not cited in the body, and does not fit M03 for neural decoding. |
| 25 | Claim row 19 "Questions for the authors" | Row 19 | contradiction | The review has no such section, so the claim table has a stale row. |

Central claim and position: the review identifies articulatory EMG as the main confound and separates the 7.3-point headline into its pretraining and backbone parts, which is the right decomposition. It does not handle two further confounds: (a) whether the test sessions' unlabeled EEG is inside the 105 h pretraining set, and (b) baseline strength, since every baseline is a single run with no tuning information. Fairness: Du-IN (arXiv May 2024) is more than 6 months before the target (arXiv April 2025), so "does not cite Du-IN" is fair. [3] and [5] are correctly labelled [later], and [3] is not treated as prior work. Verdicts: none are `ahead`. Using "not reported" for M12 is consistent with the table's own vocabulary.

## Required fixes (by impact)

1. M06 state of the art [4]: the quote in the claim table ("Subjects 12") belongs to the target. Add the quote and location for 96.4%, four covert syllables, 64 channels and 10 participants, or drop the line. Check for later work that beats a 2019 value.
2. Say whether the about 105 h of unlabeled pretraining EEG include the held-out test sessions (Sec. 4.2.1). If they do, or if this is unclear, name it as a confound of the 35.3 to 39.6 gain alongside EMG.
3. Remove "Generic pretraining fails in both" and "has failed so far", or narrow them to the cited LaBraM results. Add quotes and locations from [3] for "no better than compact CNNs" and "all five at chance on unseen subjects". Consider CBraMod (ICLR 2025, BCI Competition 2020-3 imagined speech) as counter-evidence (medium confidence).
4. Reconcile the Appendix M03 state of the art (23.7% WER [5], an audio-visual recognition paper) with the body's Du-IN [2], or drop [5] from M03.
5. The "first to predict future EEG" priority claim (§3.3.4): name earlier forecasting or autoregressive neural-signal pretraining, for example Brant (NeurIPS 2023, intracranial forecasting) and Neuro-GPT (ISBI 2024, EEG next-chunk prediction). Do not rest the rebuttal only on the 120 ms divergence.
6. ASTP +2.2 semantic points: give the from-scratch semantic baseline and say which semantic mean (42.8 or 47.0) it uses. Note that §5.1 calls the objective FSTP.
7. M06 usual approach: follow the Appendix order (other 48, CNN 37, SVM 17, linear ...). Do not present transformer 12 as the third family.
8. Add quotes and locations for the unquoted details and absence claims: no seeds, no EMG channel, the 1–75 Hz band, the 90% ICA threshold, 1000 Hz sampling, the Neuroscan device, and untested hardware savings.
9. Semantic mean: say plainly that the Table 2 per-participant values average to 47.0, so 42.8 in §5.1 is the inconsistent figure.
10. Replace "the same effect size" (Du-IN vs target) with a plain comparison of the relative changes. The tasks, class counts and chance levels differ.
11. Remove claim-table row 19 ("Questions for the authors"), or restore that section in the review.

## Scores

- Procedure: 7/10. The arithmetic and decompositions check out. Several citations and details have no quote, and one quote is the wrong one (row 12).
- Final text: 7/10. The position is clear and well decomposed. A few overreaching statements (generic pretraining "fails", "same effect size") and an internal inconsistency (M03 state of the art in the Appendix) remain.
