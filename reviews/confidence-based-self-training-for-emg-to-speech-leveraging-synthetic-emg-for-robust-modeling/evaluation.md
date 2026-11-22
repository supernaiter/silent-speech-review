# Evaluation: Confidence-Based Self-Training for EMG-to-Speech (arXiv:2506.11862)

Date: 2026-11-22. Fallback evaluator (claim table only). Input: the compact review and its claim table. No sources were opened. Remarks marked "evaluator knowledge" are unverified background, not checked against sources.

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper changes one component (M03): STE-GAN EMG from LibriSpeech audio, phoneme-loss filter, 1:1 mix with real voiced EMG | Row 1 (Abstract, §I, §II-A, §II-B/C, §IV-B, Fig. 3) | correct, with a contradiction | Quotes support CoM2S, PL<0.5 and the 50/50 mix. But the review also says "15.2 hours of one speaker's voiced EMG plus 8.3 hours of synthetic EMG" (M03 state of the art), which is not 1:1. The review must say how the mix was balanced (subsampled real data? utterance count?). |
| 2 | Speech-driven generator is the usual approach (8 of 13); lip reading scaled it to 3,652 h two years earlier [3] | Rows 2, 5, 23 | correct | 8 of 13 is a majority. SynthVSR (CVPR 2023) precedes the target (June 2025) by two years. |
| 3 | Real-EMG benefit: 23.30% to 21.87% WER, 1.43 points, 6.1% relative | Row 3 (Table IV, §IV-C.1) | correct | 1.43 / 23.30 = 6.14%. The 23.30% carries the marker "[8]" in Table IV, so it may be a number reported by the earlier work rather than a re-run under the same ASR and scorer. The review does not say which. |
| 4 | "No seeds or repetitions (§IV-B)" | Row 3 | insufficient evidence | Absence claim; the §IV-B quote says nothing about seeds. State that §IV-B and Tables III-IV report single values with no spread. |
| 5 | 37.63% to 8.75% measured on synthetic EMG from the same generator | Row 4 (Table IV, §IV-C.2) | correct | The numbers match. "Agreement with the generator, not robustness" is an inference and is reasonable. |
| 6 | Paper is the only EMG decoder among the 13; generator paper had already proposed this use [2] | Row 6 ([2] §1) | correct | Quote "STE could also be explored to generate new, artificial EMG" supports it. The "only" claim is scoped to the ledger and names the deciding prior. |
| 7 | SynthVSR: 438 h real + 3,652 h synthetic, LRS3 WER 36.7% to 27.9%, 24.0% relative; synthetic alone 100.3% | Row 7 ([3] §4.1, §4.5, Tables 1-2) | correct | 8.8 / 36.7 = 23.98%. Evaluator knowledge: SynthVSR also reports a stronger LARGE configuration, and LRS3 VSR results have since improved well beyond 27.9%. The comparison is about the effect of synthetic data, not the best VSR WER, and the line should say so. |
| 8 | Filter: 0.5 h PL<0.5 subset gives 29.36% vs 42.75% for 5.0 h PL<0.8, on the raw synthetic test | Row 9 (§IV-A, Table I) | correct | Numbers match. Unreconciled in the target and in the review: Table I gives about 0.5 h at PL<0.5, but §IV-A says 8.3 h were generated at the same threshold. |
| 9 | A phoneme classifier trained on real EMG was the generator's quality measure; 10.29% round-trip WER on Gaddy test audio [2] | Row 10 ([2] Table 2) | insufficient evidence | The quote "STE-GAN (SU) 0.66 82.65 1.87 10.29" has no column headers, so it does not show that 10.29 is a round-trip WER, or that the measure was a phoneme classifier. |
| 10 | M12 usual approach: 11 of 23 use Whisper, 5 DeepSpeech, 3 synthetic tests | Rows 11, 26, 27, 29 | wrong as stated | Appendix row 29 reports known-item recall 0.0 for this tally: it missed the Gaddy papers and the generator paper. Those works score with DeepSpeech. Calling Whisper the usual approach on a tally that missed the defining works for this dataset is not supported. Evaluator knowledge: DeepSpeech scoring was the long-standing convention on the Gaddy corpus. |
| 11 | Paper uses DeepSpeech 0.7.0 with an external scorer (repository README) | Row 12 | insufficient evidence | The quote names only "Mozilla's DeepSpeech [34]". Neither the version nor the scorer appears in it. |
| 12 | State of the art: TAP-ETS (2026), silent WER 19.77% with Whisper-medium [4] [later] | Row 13 ([4] §5.1, Table 1, §4.2) | correct | Labelled [later] and used only as a loose bound, which is fair. Evaluator knowledge: EMG-to-text systems on the same corpus report lower silent WER. That is a different task and does not displace the EMG-to-speech bound. |
| 13 | Multi-speaker headline (15.90%, 8.75%) is on synthetic test EMG; loader splits without grouping by speaker; 1,532 are source voices | Row 14 | partly insufficient | The read_emg_sheldan.py quote shows only the 99/99 test split, not the absence of speaker grouping. The 15.90% quote is truncated ("baseline (15.90%) surpasses the baseline model") and does not clearly tie the number to self-training. |
| 14 | Generator does not distinguish speakers at the voice level (§II-A) | Row 4 / Row 1 (§II-A) | insufficient evidence | The quote says session indices are assigned randomly and evenly. That suggests no speaker conditioning but does not state it. Rephrase to match the quote. |
| 15 | Mix-ratio test set 99 real + 99 synthetic; 18.03% at about 16 h mixes levels differing by more than 2x | Row 15 (§IV-B, Tables III-IV) | correct | 21.87 / 8.75 = 2.5. |
| 16 | The 15.1% relative human-WER reduction does not follow from Table V: 27.35% to 23.58% is 13.8% | Row 16 (§IV-D.1, Table V) | correct | 3.77 / 27.35 = 13.78%. No other Table V pair gives 15.1%. This is a valid catch of an inconsistency in the target. |
| 17 | MOS 3.00 to 3.25, ten raters, no intervals; authors concede a vocoder bias | Row 17 (Table VI, §IV-D.2) | correct | The concession is credited to the authors, not claimed as the review's finding. |
| 18 | "Largely unexplored" contradicts the §I citation of a prior self- and active-learning study (their ref. 12) | Row 18 (§I) | insufficient evidence | The second quote ("corrections significantly enhanced model performance") does not show that the cited work is self- or active-learning in EMG-to-speech, or that it is ref. 12. |
| 19 | M11 Libri-EMG (synthetic corpus) rated standard against the usual "recorded EMG corpora" | Table row M11 | wrong (inconsistent) | The row's own usual approach differs from what the paper does, yet the verdict is standard. Either give a non-standard verdict under the rules, or state that the change is counted under M03. |
| 20 | Verdict and M03 cite "(Appendix)"; row 21 cites "Questions for the authors" | Rows 5, 21-29 | insufficient evidence | Neither section is in the compact text. If they are left out of the published page, several positions cite a location the reader cannot see. |

Central claim and strongest confound: the real-data gain is 1.43 points from a single run against a baseline that may be a number reported by the earlier work [8] rather than a re-run with the same ASR and scorer. The review handles absolute vs relative change and the lack of repetitions, and it correctly separates synthetic-test gains from real-test gains. It does not address whether the baseline was re-run or the size of the real test set (row 21 raises this only as a question).

Fairness: TAP-ETS [4] is labelled [later] and is not treated as a missed citation. SynthVSR [3] is genuine prior work. The 15.1% catch and the filter results are attributed correctly.

Verdicts: no slot is rated `ahead`. The M09/M10 "not applicable" and M13 "not reported" ratings follow from the stated evidence. M11 is inconsistent (row 19).

## Required fixes (by impact)

1. Reconcile "mixed 1:1" (Verdict) with "15.2 hours real plus 8.3 hours synthetic" (M03 state of the art): say what was balanced and how.
2. M12 usual approach: the tally has known-item recall 0.0 and missed the Gaddy papers and the generator paper, which use DeepSpeech. Either caveat the "Whisper 11 of 23" usual approach or restate it. Do not present Whisper as the usual design without that caveat.
3. State whether the 23.30% baseline (marked [8] in Table IV) was re-run under the same ASR and scorer or copied from the earlier work. Name this as the main confound next to the single-run caveat.
4. M11: the verdict "standard" contradicts the row's own usual approach (recorded corpora vs synthetic Libri-EMG). Fix the verdict or point to M03.
5. Add a quote and location for "the loader splits utterances without grouping by speaker", or drop the claim. Supply the full quote tying 15.90% to self-training.
6. Add the [2] Table 2 column headers to support "10.29% round-trip WER" and "phoneme classifier as quality measure", or drop the claim.
7. Add a quote showing "DeepSpeech 0.7.0 with an external scorer", or reduce it to "DeepSpeech [34]".
8. Add a quote showing that the target's ref. 12 is a prior self- or active-learning study in this domain, or soften the contradiction claim.
9. Rephrase "the generator does not distinguish speakers at the voice level (§II-A)" to match the quote (random, even session indices).
10. Give the basis for "no seeds or repetitions": single values without spread in §IV-B and Tables III-IV.
11. Note the unreconciled 0.5 h (Table I, PL<0.5) vs 8.3 h (§IV-A, same threshold) in the target.
12. Make sure the Appendix and "Questions for the authors" sections cited by the text appear in the published review, or remove the references to them.

## Scores

- Procedure: 6/10. The arithmetic is checked and target numbers are well quoted, but several claim-table quotes do not carry their claims, and the M12 tally is used despite recall 0.0.
- Final text: 7/10. The position is clear, real and synthetic test gains are separated, and the 15.1% catch is valid. One internal contradiction (the mix ratio) and one inconsistent verdict (M11) remain.
