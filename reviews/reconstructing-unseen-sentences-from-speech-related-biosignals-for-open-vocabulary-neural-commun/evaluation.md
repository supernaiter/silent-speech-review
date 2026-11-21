# Independent evaluation: Reconstructing Unseen Sentences from Speech-related Biosignals (arXiv:2510.27247)

Date: 2026-11-21. Independent evaluator, claim table and review text only. No sources were reopened. Bibliographic and state-of-the-art notes come from the evaluator's own knowledge of the literature and are marked as such.

## Claim check

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target adds 10 face/neck EMG channels to 128-channel EEG (Verdict, M05, table) | Claim row 1 | insufficient evidence | The quote is about overt target audio. No quote gives 128 EEG or 10 EMG channels or their placement. |
| 2 | Whispered and imagined inputs are trained on overt audio of the same sentence through phoneme-weighted DTW (Verdict, M02) | Claim rows 1, 10 | partly correct | Row 1 supports overt audio as target. "Phoneme-weighted" is quoted only from [3] (row 10), not from the target §III-B. |
| 3 | Overt EEG kept at 0.5–200 Hz with no EMG regression (Verdict; "Where the claims outrun") | Claim rows 3, 17 | insufficient evidence | Both quotes are from [5]. There is no quote from the target §II-B for the band or for the missing regression. |
| 4 | No EMG-only arm; the comparison is EEG vs EEG+EMG (Fig. 3) | Claim row 7 | insufficient evidence | This is an absence claim about the target with no locator showing every condition tested. It is plausible from the Fig. 3 quote. |
| 5 | Overt phoneme accuracy 36.83% → 48.58%; whispered 30.54% → 40.97%; whispered RMSE 0.58; MCD 4.73 vs 4.71 | Claim row 7 | partly correct | Only 48.58% (overt, EEG+EMG) is in the quote. The other five values have no quote, and the order of "4.73 vs 4.71" is not stated. |
| 6 | 11% majority-class (sil) baseline | Claim row 14 | correct | The quote gives "sil" at 11%. |
| 7 | CER only for two sentences of one subject (0.18–0.50, Table II) | Claim row 14 | insufficient evidence | No quote for Table II, for the two sentences or for the range. |
| 8 | Table V (imagined, frequency bands) is one subject | Claim row 11 | insufficient evidence | The quote describes Table V but does not say it covers one subject. |
| 9 | Patient claim rests on one patient and 10 test sentences (§IV-B) | Claim row 18 | partly correct | The authors' sentence is quoted. "One patient, 10 test sentences" has no quote. |
| 10 | Authors concede that the fixed mode order may leak echoic traces (§V-E); no seeds or repeated runs (§III-C) | No claim row | insufficient evidence | No claim-table entry. |
| 11 | "Open-vocabulary" = 30 held-out of 474 sentences, 444/30 split | Claim rows 12, 16 | partly correct | The quote supports "unseen sentences", not the counts. |
| 12 | [2] is not cited by the target | No claim row | insufficient evidence | This absence claim needs a statement that the target's reference list was checked. |
| 13 | [2]: decision-level fusion, 57 EEG + 5 sEMG, eight speakers, 7.22% / 38.85% / 10.52% CER (Table 3) | Claim rows 2, 5 | partly correct | The quote "31.63% reduction in CER" vs EEG-only equals 38.85 − 7.22 = 31.63 points, so 7.22 and 38.85 are consistent. The fusion level, channel counts, speaker count and 10.52% are not quoted. |
| 14 | [2] tests on held-out repeats of training sentences | Claim row 5 | correct | The quote states this directly. |
| 15 | EEG cuts CER by 31% relative to sEMG alone (inference) | Claim row 6 | correct (calculation) | (10.52 − 7.22)/10.52 = 31.4%. A reader may confuse it with [2]'s own "31.63% reduction" vs EEG-only, which is an absolute point drop of a different contrast. |
| 16 | [6] (later, 2026): 11.89% silent-EMG WER with DTW-transferred targets | Claim row 9 | insufficient evidence | The row 9 quote is from [4]. Nothing in the claim table supports 11.89%. |
| 17 | NeuroTalk [4]: imagined EEG trained on DTW-aligned spoken audio with CTC, 12 words | Claim row 9 | partly correct | DTW is quoted. CTC and "12 words" are not. The 12-word set matches the evaluator's knowledge of [4]. |
| 18 | Phoneme term in the DTW cost and forced-aligner labels come from [3] | Claim row 10 | correct | Consistent with [3] §2.4 ("we modify the alignment and loss cost"). |
| 19 | [7]: 23.8% WER, 125,000-word vocabulary, never-duplicated held-out sentences (2023) | Claim row 13 | correct | The quote supports held-out sentences. 23.8% at 125k words matches [7]. |
| 20 | [3]: 42.2% WER with DeepSpeech over the whole test set | Claim row 15 | correct | The quote gives 68.0% → 42.2%. |
| 21 | M12 SOTA is [7] (2023) | Evaluator knowledge | wrong (outdated) | Card et al., "An accurate and rapidly calibrating speech neuroprosthesis," NEJM 2024, 391:609–618, reports about 2.5% WER with a 125,000-word vocabulary on held-out sentences. It predates the target. |
| 22 | M02 SOTA on silent EMG is [6] at 11.89% WER | Evaluator knowledge | insufficient evidence | Benster et al. 2024 (MONA LISA, arXiv:2403.05583) reported about 12.2% silent-EMG WER on the same corpus using LLM rescoring. The review should state the decoder and LM conditions under which [6] is better. |
| 23 | M12 verdict "behind the typical practice of transcribing the whole test set" | M12 section, table | wrong (unsupported as written) | The stated ledger counts (21 sentence-disjoint, 10 repeated, of 145) do not count whole-test-set WER/CER reporting. "Typical" is not backed by a count, and three cited works do not establish typicality. |
| 24 | [7] bibliographic: *Nature* 621, 1031–1036 | Reference list | wrong | Willett et al. 2023 is *Nature* **620**, 1031–1036. |
| 25 | M05 usual approach: 11 artifact vs 10 fusion of 30 | Claim row 4, 20 | not checkable (ledger) | Ledger tally. The Appendix itself is not in the compact file. |

## Central claim, confounds, fairness

- **Strongest confound:** myogenic contamination of overt EEG together with the missing EMG-only arm. The review names it and states it plainly. This is handled well.
- **Task difference to [2]:** [2] tests on repeated sentences and the target on unseen sentences. The review flags this. This is handled.
- **Chronology:** [6] is correctly labelled [later] and used only as state of the art, not as prior work. [2], [3], [4], [5] and [7] all predate the target by more than 6 months. No problems found.
- **Own-finding attribution:** the fixed-order leakage is attributed to the authors (§V-E). This is correct.
- **Absence claims:** "[2] is not cited", "no EMG-only arm" and "no cohort WER/CER" have no claim-table locator in the target.

## Required fixes (by impact)

1. Add target quotes and locations for every target number the review uses: 128/10 channels, 0.5–200 Hz and no EMG regression (§II-B), the Fig. 3 values (36.83, 30.54, 40.97, RMSE 0.58, MCD 4.73/4.71), the Table II CER of 0.18–0.50 on two sentences, Table V as one subject, one patient with 10 test sentences, and §V-E/§III-C (mode order, seeds).
2. Update the M12 state of the art. Card et al. (NEJM 2024; about 2.5% WER, 125k vocabulary) supersedes [7] at 23.8%. If intracortical work is kept as the reference, say why no non-invasive comparator is given.
3. Support or soften the M12 `behind` verdict. Give an Appendix ledger count of studies that report WER/CER over the full test set, or restate the verdict against the cited works only.
4. Correct reference [7] to *Nature* 620, 1031–1036.
5. Add a quote for [6]'s 11.89% WER with its decoder and LM condition. Name MONA LISA (2024, about 12.2% silent-EMG WER) as the prior bar it is compared against.
6. Add a [2] Table 3 quote for 10.52% (sEMG only), decision-level fusion, 57 EEG + 5 sEMG channels and eight speakers.
7. Add a locator for "[2] is not cited" (the target's reference list) and for "no EMG-only arm" (the list of conditions in Fig. 3 / §IV-A).
8. Say which value is EEG and which is EEG+EMG in "MCD 4.73 vs 4.71".
9. Make clear that the 31% relative CER cut (EEG+sEMG vs sEMG) is a different contrast from [2]'s own "31.63% reduction" (EEG+sEMG vs EEG-only, absolute points). This avoids a misreading.
10. Add quotes for NeuroTalk's CTC loss and 12-word vocabulary ([4]).

## Scores

- Procedure: 6/10. The confound analysis and chronology are sound, but many target numbers and absence claims lack quotes, and one state-of-the-art line is outdated.
- Final text: 7/10. The position is clear and well argued. It needs the M12 state of the art updated, the `behind` verdict supported, and one bibliographic correction.
