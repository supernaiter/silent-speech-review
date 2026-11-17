# Evaluation: Digital Voicing of Silent Speech (Gaddy and Klein, EMNLP 2020)

Date: 2026-11-17. Independent evaluator, one pass, no tools beyond the review text. Inputs: the compact review and its claim table, nothing else. The writer filled the claim table, not a separate checker, so each "correct" means the quote as given supports the claim; it does not mean the quote was checked against the source. Ledger counts and the Appendix were not available (the compact review has no Appendix or Questions section, but the claim table has rows for both). Every position that cites "Appendix, Mxx" therefore stays unverified.

## Claim table

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Two changed components; 18.6-hour open corpus (Verdict) | Claim row 1, Table 2 quote | correct | |
| 2 | Janke 2016 trained silent EMG on DTW-aligned audible targets; priority claim fails (Verdict, M02) | Rows 2, 22; Sec. 6.3.1 quote vs target Abstract quote | correct | The quote supports DTW alignment of acoustic data to silent EMG. The target says it is "the first to train from EMG collected during silently articulated speech". The contradiction is real. |
| 3 | 68.0% to 42.2% on the same split and recognizer [3] (Verdict, M12) | Rows 3, 15 | correct | |
| 4 | 11.89% WER with Whisper [4]; 5.7 times lower (M12) | Rows 3, 16 | correct | 68.0 / 11.89 = 5.72. The review states that the recognizer differs. |
| 5 | 94% headline is a 67-word task, 20 clips per system, one transcriber (Verdict, §4.1) | Rows 4, 23, 30 | insufficient evidence | "67 words" and "370 utterances" are quoted. No quote gives "20 clips" or "one transcriber". The App. B quote says only that the files were shuffled. |
| 6 | Open vocabulary is 22.7% relative (Verdict) | Row 4: 88.0 vs 68.0 | correct arithmetic, inconsistent | (88.0 − 68.0) / 88.0 = 22.7% is automatic WER. The 94% headline is human WER, and the like-for-like human open-vocabulary figure (row 24) is 21.3%. The Verdict and "Where the claims outrun" use different numbers for the same point. |
| 7 | 95.1% to 74.8%, 21% relative (§4.2.1) | Row 24 | correct | 21.3% |
| 8 | CCA and electrode ranking "within later seed variance" [5]; removing CCA (1.8 points) is "inside the 1-point seed SD" (Verdict, M02) | Rows 5, 12 | wrong | 69.8 − 68.0 = 1.8, which is about 1.8 times the SD of 0.99 that [5] reports, not inside it. That SD also belongs to the 2021 model, scored by a different recognizer on 98 utterances at about 27% WER. It does not transfer directly to a DeepSpeech regime near 68%. |
| 9 | [5]: 26.75 ± 0.99 to 25.14 ± 0.90 WER over 10 seeds (M02 SotA) | Rows 9, 12 | insufficient evidence | The quoted row has three columns (14.16, 26.75, 6.48), and no header is quoted. Which column is WER, which recognizer was used, and how large the test set is are not shown in the quote. |
| 10 | Janke: about 7 minutes of silent data per session; LSTM MCD 7.14 to 6.65; feed-forward 6.81 vs 6.6 (M02) | Row 10 | wrong / insufficient evidence | The quote says "DNN", not LSTM, and 7.14 is not in any quote. The "per session" claim rests on one row (S1-1), and the quote does not say which column is silent. In this paragraph 6.81 is Sil Train–Sil Test, but in M04 (row 18) 6.81 is Aud Train–Sil Test. The direct-transfer value is 6.6 in M02 and 6.81 in M04. |
| 11 | 3.6 h parallel silent data (M02) | Row 11 | correct | |
| 12 | Without audio alignment 76.5% (M02) | Row 12 | correct | |
| 13 | Earlier work scored silent output by DTW-aligned MCD (M12 usual) | Row 13 | correct for [2] | Janke's dissertation also reports listening tests, so "scored by MCD" alone may understate earlier practice (low confidence). |
| 14 | 16 studies: 9 Whisper, 7 DeepSpeech, 3 listener (M12 usual) | Row 14 | insufficient evidence | 9 + 7 + 3 = 19 > 16. If some studies use more than one method, the review should say so. |
| 15 | Recognizer floor 9.5% (§4.2.2) | Row 17 | correct | |
| 16 | Release uses DeepSpeech v0.7.0 with an external scorer (M12) | Rows 17, 29 | insufficient evidence | The rows for README.md and asr.py repeat the paper's sentence and do not quote the code, so the version and scorer have no quote behind them. |
| 17 | [5] uses Whisper and 98 test utterances (M12) | Row 17 | correct | |
| 18 | Distortion 5.54 to 6.81 under direct transfer [2] (M04) | Row 18 | correct per quote | It conflicts with M02's direct-transfer value of 6.6 (see #10). |
| 19 | "Since 2021, systems on this corpus train on silent EMG (14 confirmed studies in the M02 table)" (M04 SotA) | Rows 7, 19 | contradiction | M02 says one of the 14 is prior (Janke 2016), which is not on this corpus. At most 13 are on this corpus since 2021. |
| 20 | 88.0% vs 68.0% open vocabulary; 64.6% vs 3.6% closed (M04) | Row 20 | correct values, incomplete condition | 88.0 is the "without throat electrode" variant, not the plain direct-transfer baseline. |
| 21 | Baseline is a reimplementation; 88.8 to 64.6 by dropping one electrode, "so it was not tuned" (M04) | Row 21 | judgment beyond evidence | The authors report the no-throat variant themselves as their strongest baseline. The numbers show that the baseline is sensitive to one choice. They do not show that it was untuned. |
| 22 | 10 of 70 four-electrode removals, each trained once; 75.3 vs 76.8 (§4.3.2) | Row 25 | correct values; fairness issue | The authors themselves report that removing only 5, 7 and 8 performs "substantially worse" (75.3%). The review presents the caveat as its own finding. |
| 23 | Released test split comes from one book (Verdict, §2.2) | Rows 5, 26 | insufficient evidence | Both quotes repeat the §2.2 sentence. Nothing quoted from testset.json or read_emg.py shows where the test utterances come from. |
| 24 | No seeds or repeated runs; "no plateau" rests on one run per size | Rows 5, 27 | correct as an absence claim | It is supported only because App. D says nothing about seeds. |
| 25 | M12 verdict "standard" vs "the paper's lasting contribution" and "became the benchmark" | Verdict, M12 body | contradiction | See fix 2. |

Novelty and absence: "Of 14 confirmed studies ... one is prior: Janke [2]". There is earlier work by the same group, around 2009–2011, that aligned silent EMG to audible EMG by DTW to transfer labels for silent-EMG recognition (Wand, Janke, Schultz and colleagues, speaking-mode work, around Interspeech 2010 and BIOSIGNALS 2010). It may count as prior target transfer, though for recognition targets rather than audio targets. This is from memory with low confidence. The writer should check it before stating "one is prior".

Chronology: [3], [4] and [5] are correctly marked [later] and are not treated as prior work or as missed citations.

Strongest confound: baseline strength. The direct-transfer baseline is the authors' own reimplementation (no prior code), the comparison uses a 67-word closed vocabulary, and human scoring is thin. The review handles this well: it moves from 94% relative to the open-vocabulary figure and notes the reimplementation. The handling is weakened by the inconsistent open-vocabulary figure (#6) and by the overreach in #21.

## Required fixes (ordered by impact)

1. **Sentence:** "Removing CCA costs 1.8 points (inference) in one run (69.8% against 68.0%, Table 5), inside the 1-point seed SD later measured here [5]". Also in the Verdict: "CCA and the electrode ranking rest on single runs within later seed variance [5]".
   **Problem:** 1.8 points is about 1.8 SD, not inside a 1-point SD. The SD comes from a different model (the 2021 model), a different recognizer and a different test set (98 utterances), at a much lower WER.
   **Fix:** "Removing CCA costs 1.8 points in a single run (69.8% against 68.0%, Table 5). With no seeds reported, this cannot be separated from run-to-run noise. For comparison, [5] measured a seed SD of about 1 point for the 2021 model under a different recognizer." In the Verdict, replace "within later seed variance" with "are single runs with no reported seed spread".

2. **Sentence:** "M12 is standard and became the benchmark". Also in the M12 section: "Moving the field from spectral distance to WER is the paper's lasting contribution. ... Verdict: standard."
   **Problem:** The review names the component the paper's lasting contribution and the field's benchmark, then grades it `standard`. The verdict and the text contradict each other.
   **Fix:** Either grade M12 `ahead` and meet the rule (give the ledger count in the Appendix, name the deciding priors that used MCD or listening tests only, and repeat the effect: open corpus and WER adopted by the 16 later studies), or keep `standard` and say why: for example, ASR- or listener-based intelligibility scoring already existed in earlier EMG-to-speech work, and the new elements are the corpus and the release.

3. **Sentence:** "With about 7 minutes of silent data per session, Janke's silent training lowered LSTM mel-cepstral distortion from 7.14 to 6.65 but left feed-forward mapping worse than direct transfer (6.81 against 6.6) [2]."
   **Problem:** The quote says DNN, not LSTM. The value 7.14 is not quoted. "Per session" rests on one session row. In this sentence 6.81 is Sil Train–Sil Test, but in M04 ("distortion rises from 5.54 to 6.81") 6.81 is Aud Train–Sil Test, so the direct-transfer MCD is 6.6 in one section and 6.81 in the other.
   **Fix:** Quote the source of 7.14 and the model type for each figure, with chapter and figure numbers. State the session durations as a range across sessions. Label the 6.6 and 6.81 figures with their chapter and setup (Ch. 6 vs Ch. 8, model type) so the two direct-transfer values do not look contradictory.

4. **Sentence:** "Since 2021, systems on this corpus train on silent EMG (14 confirmed studies in the M02 table, Appendix)."
   **Problem:** M02 counts Janke 2016 among the 14, and Janke 2016 is neither on this corpus nor from 2021 or later.
   **Fix:** "Since 2021, systems on this corpus train on silent EMG (13 of the 14 confirmed studies in the M02 table; the other is [2])". Use the correct figure from the Appendix.

5. **Sentence:** "The headline 94% reduction is a 67-word task with 20 clips per system and one transcriber (§4.1)". Also: "and 20 clips per system with no stated selection (App. B)".
   **Problem:** The claim table has no quote for "20 clips" or "one transcriber". The App. B quote says only that the files were shuffled and that the evaluator was blind to the system.
   **Fix:** Add the source passages with their locations for the clip count and the number of transcribers, or delete both details.

6. **Sentence:** "the released test split comes from one book, not the random draw of §2.2". Also: "the released testset.json takes them all from one book, so the test measures one text."
   **Problem:** The claim-table rows for testset.json and read_emg.py repeat the §2.2 sentence and contain no evidence from the files.
   **Fix:** Quote the file evidence: the book or session identifiers of the 100 test utterances, and the lines that select them. Without that evidence, remove the claim or move it to Questions for the authors.

7. **Sentence:** "the paper names neither the DeepSpeech model nor its scorer (the release uses v0.7.0 with an external scorer)".
   **Problem:** No quote from README.md or asr.py supports the version or the scorer. The rows repeat the paper's sentence.
   **Fix:** Quote the README and code lines that give the version and the scorer, or drop the parenthesis.

8. **Sentence:** "a 2026 alignment loss moves the 2021 Gaddy encoder from 26.75 ± 0.99 to 25.14 ± 0.90 WER over 10 seeds [5]".
   **Problem:** The quoted table row has three columns and no quoted header, so it is not shown which column is WER. The recognizer (Whisper) and the test set size (98) are not attached to the number.
   **Fix:** Quote the column header. Write: "25.14 ± 0.90 against 26.75 ± 0.99 Whisper WER on 98 test utterances, 10 seeds [5]".

9. **Sentence:** "on open vocabulary it is 22.7% relative (inference)" (Verdict).
   **Problem:** The 94% headline is human-transcribed. The 22.7% figure is automatic WER against the no-throat variant. The body uses the human figure of 21%. The same point appears with two numbers under two metrics.
   **Fix:** "on open vocabulary, human-transcribed WER falls 21% relative (95.1% to 74.8%, §4.2.1; inference)". Alternatively, keep 22.7% and label it "automatic WER against the strongest baseline".

10. **Sentence:** "dropping one throat electrode moves it from 88.8% to 64.6% (Table 4), so it was not tuned."
    **Problem:** The authors report the no-throat variant themselves as the strongest baseline. A large effect from one choice shows sensitivity, not an untuned baseline.
    **Fix:** "dropping one throat electrode moves it from 88.8% to 64.6% (Table 4), so the baseline is sensitive to untested design choices, and no other variants are reported."

11. **Sentence:** "75.3% against 76.8% does not show that electrodes 5, 7 and 8 matter less."
    **Problem:** The authors themselves report that removing only 5, 7 and 8 is "substantially worse" (75.3%, §4.3.2). The review presents the authors' own caveat as its own finding.
    **Fix:** "The authors note that removing 5, 7 and 8 alone already gives 75.3% (§4.3.2). With single runs, the ranking of the 10 sampled removals (of 70) is not established."

12. **Sentence:** "Scored as intelligibility, the gap is stark: 88.0% against 68.0% open-vocabulary WER".
    **Problem:** 88.0% is the "without throat electrode" direct-transfer variant, not the plain baseline. The condition is missing.
    **Fix:** "88.0% (direct transfer without the throat electrode, the strongest baseline) against 68.0%".

13. **Sentence:** "16 unique studies report silent-EMG voicing (pattern match, Appendix): 9 score with Whisper, 7 with DeepSpeech, 3 with listener transcription."
    **Problem:** 9 + 7 + 3 = 19, which exceeds 16, and the overlap is not stated.
    **Fix:** Add "(some use more than one)" or give the counts as studies per method with the overlap.

14. **Sentence:** "Of 14 confirmed studies that train silent signals on targets moved from a vocalized repetition ..., one is prior: Janke aligned silent to audible EMG by DTW [2]."
    **Problem:** This is an absence claim with a single named prior. Earlier speaking-mode work from the same group (around 2009–2011) used DTW alignment of silent to audible EMG to transfer targets for recognition. The review does not name or exclude it. This is evaluator recollection, low confidence.
    **Fix:** Check the Wand/Janke/Schultz speaking-mode papers from around 2010. Either name them as deciding priors (for recognition targets) or state why they are out of scope (text labels rather than audio targets). Otherwise write "the earliest prior read in full is [2]".

## Scores

- Procedure: 6/10. The claim table is thorough, but several rows repeat the paper's sentence in place of quoting the code or file evidence they cite. The writer filled the table, and the Appendix is missing from the compact text.
- Final text: 6/10. The position is clear and the central confound is handled. However, one numeric claim is wrong (seed SD), the M12 verdict contradicts its own text, Janke's figures are inconsistent across sections, and several specifics have no quote.

Strengths (brief): the review shows that the target's priority claim is contradicted by the dissertation it identifies, separates the closed-vocabulary headline from open-vocabulary results, gives absolute and relative figures, and labels later work correctly.
