# Evaluation: Non-invasive electromyographic speech neuroprosthesis: a geometric perspective

Date: 2026-11-21. Fallback evaluator (claim table only). Input: the claim table, the Verdict and the component sections of the review. No sources were opened; anything marked "inference" or "evaluator knowledge" is not checked against a source.

## Claim check

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | [1] changes supervision (silent-only phoneme labels) and input (SPD) | Row 1, Sec. 2.1 quotes | correct | GRU + CTC itself is not quoted, but it is not disputed. |
| 2 | Subvocal-only models for continuous phrases reached 8.9% WER in 2018 [2] | Row 2, [2] Results/Table 2 | wrong (condition) | The quote gives 8.9% as the "average WER across all four data sets", not the 2,200-word phrase set alone. The review ties the figure to the 2,200-word phrases. |
| 3 | Baseline at 100% WER, 89.25% PER; chance PER 97.5% | Row 3, Table 1, Appendix B | correct | |
| 4 | 73.53% WER, one participant, no repeated runs; 12.2% on Gaddy | Row 4 | insufficient evidence | 73.53 and 12.2 match. The checkpoint-selection quote does not show that only one run was made; "without repeated runs" is an absence the quote does not establish. |
| 5 | 195 studies; HMM 46, CTC 44, DTW 34 | Row 5, Appendix tally | not checked | Ledger tally, outside this check. |
| 6 | No vocalized speech recorded | Row 6, Sec. 2.1 | correct | |
| 7 | 12.2% WER (2024), down from 28.8% [3] | Row 7, [3] Abstract | correct | |
| 8 | Five subjects averaged 8.9% on phrases from a 2,200-word vocabulary [2] | Row 8 | wrong / insufficient | Quote says "four data sets"; neither "five subjects" nor "2,200-word" appears in any quote. Same condition problem as row 2. |
| 9 | 73.53% is about six times 12.2% | Row 9 | correct | 73.53 / 12.2 = 6.03. Labelled inference; the two figures come from different data, speakers and LMs (see confound). |
| 10 | [2] recorded its large-vocabulary corpus in subvocal mode only | Row 10 | correct | Quotes support subvocal-mode recording. |
| 11 | [2]'s grammar is far tighter than a 4-gram LM | Row 11 | correct | NL Equivalence grammar vs 4-gram LM both quoted. |
| 12 | Target cites [2] only as ~200-word grammar recognition | Row 12, Appendix A | correct | |
| 13 | About 8 hours, over 6,500 words | Row 13, Sec. 4 | insufficient evidence | "6500 unique words" is quoted ("over" overstates it slightly); "about 8 hours" has no quote. |
| 14 | 83 studies; time-domain FF/recurrent 18; Transformer/Conformer 26 | Row 14 | not checked | Ledger tally. |
| 15 | 31×31 covariance on a shared eigenbasis; 31 sites at 5 kHz (table) | Row 15, Sec. 3.1 | no quote | The quotes are about η = 0.1 and a 20 ms timestep. Nothing quoted supports 31 channels, 31×31, the shared eigenbasis or 5 kHz. |
| 16 | 11.89% WER [later] [4] | Row 16 | no quote | Only [3]'s 12.2% is quoted; [4]'s figure has no quote or location. The [later] label is right for a 2026 paper. |
| 17 | SPD embedding from [5] [concurrent] | Row 17 | correct | arXiv 2411.02591 is within 6 months of the target, so [concurrent] fits, and it is not treated as missed prior work. |
| 18 | PER 89.25 to 48.47, WER 100 to 73.53; 46% relative | Row 18, Table 1 | correct | (89.25 − 48.47) / 89.25 = 45.7%. |
| 19 | EMG2QWERTY CER 15.38 to 14.03, 9.55 to 7.95; 250 vs 150 epochs; SpecAugment dropped; 8.8% and 16.8% relative | Row 19, Sec. 5.1, Table 2 | partly insufficient | Numbers and both relative gains check (8.78%, 16.75%). The epoch confound is quoted. The SpecAugment drop has no quote. The quoted Table 2 rows have two columns each (15.65/15.38, 14.33/14.03); nothing quoted shows that the second column is the test split. |
| 20 | Gaddy corpus has silent utterances with text labels | Row 20 | insufficient evidence | The quoted passage is about missing usable audio, not about text labels. The claim is very likely true (evaluator knowledge), but the quote does not show it. |
| 21 | Representation claim rests on a near-chance baseline | Row 21 | correct | |
| 22 | Notebook uses the first 9,000 sentences (train + validation) | Row 22 | no quote | The notebook "quote" repeats the paper's Fréchet-mean sentence. Neither "9,000" nor the train+validation split appears. |
| 23 | NATO appendix reuses the 416/104/1,968 split of [5] | Row 23 | correct | |
| 24 | "Minimum-viable" rests on a 67-word closed set | Row 24, Table 3 | no quote | The quote "13 14" does not support "67-word". |
| 25 | p<0.015 names no test; USER 6 does not improve | Row 25 | correct | |

## Central claim, confounds and positions

- Strongest confound: the review compares 73.53% WER with 12.2% (Gaddy, open vocabulary, different speakers, an LLM-enhanced decoder) and with 8.9% (grammar-constrained, four-set average). It states plainly that the 8.9% is not comparable and ends with "the cost ... stays unmeasured", which handles the confound. The "about six times" line should be read as context only. It is labelled inference, which is acceptable.
- The SPD ablation critique (a weak baseline near chance, one participant, no seeds reported) is well founded on rows 3, 18 and 21.
- The EMG2QWERTY confound (epochs) is quoted. The SpecAugment half of it is not.
- M12 is marked "not reported" while the same row lists "1,970 held-out sentences". The verdict and the row contradict each other, and 1,970 has no quote.

## Absence and novelty

- The priority argument (Sec. 7 claim rests on its qualifiers) depends on [2]'s condition, which rows 2 and 8 misattach. The point survives if it is restated as a four-set average.
- Possible earlier silent-only training (evaluator knowledge, low confidence, not checked): Meltzner et al., IEEE/ACM TASLP 2017 (laryngectomy, subvocal large vocabulary), and the Wand/Schultz silent-session EMG recognizers (2010–2014). The review should either name these as checked and dismissed or say that [2] is the earliest the search found.

## Verdicts

All slot verdicts are `standard`, `not applicable` or `not reported`. None is `ahead`, so the `ahead` rules do not apply. The `not reported` on M12 is inconsistent with the row content (see above).

## Required fixes (ordered by impact)

1. Rows 2 and 8: restate [2]'s 8.9% as the average across four data sets, or quote the 2,200-word-set figure and the five-subject count. Fix the Verdict and the M02 state-of-the-art line to match.
2. Row 15 and the M05/M06 table rows: add quotes for 31 channels, 31×31 covariance, the shared eigenbasis and 5 kHz, or drop them.
3. Row 22: quote the notebook lines that select the first 9,000 sentences and show that they are train + validation. Otherwise remove the "text and code differ" point.
4. Row 24: quote the 67-word vocabulary, or drop the number.
5. Row 16: add the quote and location for 11.89% WER in [4].
6. Row 19: quote the SpecAugment removal and confirm that 15.38/14.03 and 9.55/7.95 are the test columns.
7. M12: reconcile "not reported" with "1,970 held-out sentences", and quote the 1,970 figure.
8. Row 4: replace "without repeated runs" with "no repeated runs reported", or quote the paper's statement.
9. Row 13: quote "about 8 hours", and change "over 6,500" to "6,500".
10. Priority/absence: name the earlier silent-only trained EMG recognizers that were checked, or state that [2] is the earliest found.
11. Row 20: quote a passage showing that the Gaddy silent utterances carry text labels.

## Scores

Procedure: 6/10. Final text: 6/10.

Strengths: the arithmetic is correct throughout, the [later] and [concurrent] labels are correct, and the main ablation critique is well grounded.
