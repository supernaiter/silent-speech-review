# Evaluation: Updating the Silent Speech Challenge benchmark with deep learning

Date: 2026-11-18. Independent evaluator, single pass over the review and its claim table only; no sources re-opened. The claim table was filled by the writer, so a row counts as support only when its quote contains the number and condition stated.

## Claim check

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper replaces recognizer with Kaldi DNN-HMM + DAE; 17.4% to 6.45% WER | Row 1, 3 (Table 2) | correct | Quote "WER 17.4% 17.4% 6.45%". |
| 2 | "The same group had already run a DNN-HMM on the SSC (38% WER)" | Row 2 (Sec. 1.2, ref [59]) | insufficient evidence | Quote supports a 38% DNN-HMM in [59]; nothing shows it is the same group. [59] is not in the reference list. |
| 3 | Multimodal DAE on tongue and lips predates the target [2] | Row 2 (Abstract, p7) | insufficient evidence | The quoted DAE sentence reads like the target's abstract, not [2]. |
| 4 | Paper's LDA+MLLT triphone GMM reaches 12.71% | Row 3, 11 (Table 3) | correct, with caveat | Table 3 row "Triphone2b 17.40 12.71": 12.71 is WSJ and 17.40 is CSR. Table 2's Kaldi GMM 17.4% matches the CSR triphone2b value exactly. The review does not mention this. |
| 5 | "DNN's share is about half the error" | Row 3 | wrong wording | 12.71 to 6.45 is a halving of the GMM WER (ratio 1.97), not "half the error". |
| 6 | DCT systems at K=5: 98.24% to 100% | Row 5, 13 (Table 4) | correct for the rows quoted | Triphone1 is not quoted, so "every DCT system" is not fully covered. |
| 7 | "Broken run rather than lost information" | Row 5 | insufficient evidence | Inference only. Five DCT coefficients may simply carry little information. |
| 8 | DCT beats DAE at K=30 (6.45 vs 7.72, 13 words) | Row 12 | correct | 1.27% × 1023 = 13 words. |
| 9 | DAE rise 7.72% to 10.07% (30% relative) | Row 24 | correct | 2.35/7.72 = 30.4%. |
| 10 | Triphone2b K=30 differs: Table 3 vs Tables 4–5 | Row 23 | correct | 12.71/17.40 vs 13.00/17.79. |
| 11 | Of 8 DNN-HMM ultrasound studies, "none of the latter before the target" | Row 7 (Appendix audit) | wrong | Contradicts the Verdict and §1.2: [59] ran a DNN-HMM on SSC data before the target. |
| 12 | Benchmark reports 84.16% word accuracy, Table 2 lists 84.26% correct | Row 22 | insufficient evidence / metric mismatch | "Accuracy" (counts insertions) and "correct" (does not) are different HTK measures. An accuracy of 84.16% implies WER 15.84%, not 17.4%. The review compares unlike metrics. |
| 13 | Cai et al.: 79.08% to 43.50% when the WSJ bigram becomes a word-loop bigram | Row 19 | insufficient evidence | 43.50 is not in the quote. The same source gives 84.16% (Table 4) for the WSJ0 bigram, so its Table 1 is a different condition, and the review does not say which. |
| 14 | DNN 6.45% to 11.44% with CSR bigram | Row 12, 19 | correct | Quote "DNN 11.44 6.45". |
| 15 | Both LMs are closed 5k bigrams | Row 20 | insufficient evidence | No quote shows that the CSR bigram is closed or has 5k words. |
| 16 | SOTA 6.17% (Li et al. 2019) in the target's setting | Row 9, 14, 16 | correct | Quotes support 6.17% and the same setting. "Reproduced 6.45%" is cut off in the quote. 0.28 points ≈ 3 words, correct. |
| 17 | Kimura et al. 2020: 20.5% WER, 65k LM | Row 4, 10 | correct | |
| 18 | Kimura et al. 2022: 37.6% WER after 7,484 utterances | Row 10 | insufficient evidence | Neither number is in the quote. |
| 19 | TaL: 37.94% speaker-dependent, 69.84% multi-speaker, TDNN-HMM, 82 speakers | Row 17, 26 | insufficient evidence | No number is in the quote. |
| 20 | "6.45% became the reference that later SSC work reproduces [5] [3]" | Row 18 | wrong for [3] | The [3] quote gives only its own 20.5%. Nothing shows that it reproduces 6.45%. |
| 21 | 3 of 8 SSC studies use the exact condition | Row 15 | insufficient evidence | Appendix tally only; the Appendix is not in the compact. |
| 22 | Ultrasound feature tallies 32/13/13 of 39 | Row 8 | insufficient evidence | Ledger tally; not audited, per brief. |
| 23 | No seeds, repeated runs or significance tests | Row 27 | plausible absence | The quotes do not contradict it. |
| 24 | M03 verdict "not reported" while the cell lists one speaker, DAE on 12 lists, 90/10 split | Summary table | wrong | The verdict contradicts the filled cell. |
| 25 | M07 usual approach "pattern match 3" | Summary table | wrong source | The count belongs to the M12 SSC tally, not to an LM tally. |

Strongest confound: the 17.4% baseline. Table 2's Kaldi GMM number equals Table 3's triphone2b result under the CSR LM, while the DNN's 6.45% uses the WSJ LM. If so, Table 2 mixes language models, and the "factor of 3" partly reflects an LM change. The review instead says the stage is "unnamed" and compares 12.71 vs 6.45. That comparison is the right one, but the review misses the more likely explanation of 17.4.

Fairness: later works are labelled [later] and not treated as missed prior work. The review reports the 98–100% collapse and the Table 3/4 mismatch as its own findings, which is fair because the authors do not discuss either.

## Required fixes (ordered by impact)

1. Sentence: "Of 38 unique ultrasound recognition studies (pattern match, Appendix), 15 use GMM-HMMs and 8 DNN-HMMs, none of the latter before the target; ..."
   Wrong: this contradicts the Verdict and §1.2, where [59] applied a DNN-HMM to the SSC data (38% WER) before the target.
   Fix: drop "none of the latter before the target", or write "one of the latter, [59] (38% WER), before the target", and add [59] to the reference list.

2. Sentence: "Table 2's Kaldi GMM-HMM reproduces 17.4% without naming its stage, while the paper's triphone2b gives 12.71% with the same features and language model (Table 3)."
   Wrong: Table 3's triphone2b gives 17.40% with the CSR bigram. Table 2's 17.4% probably is that system under the CSR LM, not an unnamed stage under the same LM.
   Fix: "Table 2's Kaldi GMM-HMM 17.4% equals Table 3's triphone2b under the CSR bigram (17.40%), while the DNN's 6.45% uses the WSJ bigram; with the WSJ bigram the same triphone2b gives 12.71%." Carry the same correction into the Verdict and the "factor of 3" bullet.

3. Sentence: "The cited benchmark reports 84.16% word accuracy (Table 4) [4], while Table 2 lists 84.26% correct."
   Wrong: HTK word accuracy and percent correct are different measures. An accuracy of 84.16% would mean WER 15.84%, which also does not match the 17.4% baseline.
   Fix: name the measures: "The benchmark reports 84.16% word accuracy (Table 4) [4], i.e. 15.84% WER, while Table 2 gives the HTK baseline as 17.4% WER (84.26% correct)." Quote the benchmark's metric definition.

4. Sentence: "Holding features and decoding fixed is the paper's strength: 6.45% became the reference that later SSC work reproduces [5] [3]."
   Wrong: the [3] quote shows only its own 20.5%, not a reproduction of 6.45%.
   Fix: cite only [5] for the reproduction, or add a quote from [3] that cites 6.45% as its baseline.

5. Sentence: "Both are standard: the same group had already run a DNN-HMM on the SSC (38% WER, §1.2), and a multimodal DAE on tongue and lip images predates it [2]."
   Wrong: no quote shows that [59] is by the same group, and the DAE quote seems to come from the target's abstract, not from [2].
   Fix: say "a DNN-HMM had already been run on the SSC data ([59] in the paper, 38% WER, §1.2)", unless authorship is confirmed, and replace the claim-table quote for [2] with one from [2] itself.

6. Sentence: "... so the DNN's share is about half the error, not "almost a factor of 3" (inference)."
   Wrong: ambiguous and arithmetically loose. 12.71% to 6.45% halves the WER (ratio 1.97). It is not "half the error".
   Fix: "so against the paper's best GMM the DNN halves the WER (12.71% to 6.45%), rather than cutting it by almost a factor of 3."

7. Sentence: "The DAE's advantage at 5 dimensions rests on DCT systems that fail outright (98.24% to 100% WER), a broken run rather than lost information (inference)."
   Wrong: this position goes beyond the evidence. Near-total failure fits a broken pipeline, but it also fits five DCT coefficients carrying too little information. The paper gives no data to tell these apart.
   Fix: "... DCT systems that fail outright (98.24% to 100% WER), a collapse the paper does not examine and that may reflect a broken run rather than lost information." Repeat that wording in the M06 section.

8. Sentence: "In the benchmark source, word accuracy falls from 79.08% to 43.50% when the WSJ bigram becomes a word-loop bigram (Table 1) [4]; ..."
   Wrong: 43.50 is not in the quote. The same source's Table 4 gives 84.16% for the WSJ0 bigram, so Table 1 is a different condition, and the review does not name it.
   Fix: add the quote with 43.50 and name the Table 1 condition (feature set or system), e.g. "with <condition>, word accuracy falls ...".

9. Sentence: "On TaL, the multi-speaker ultrasound-plus-lip corpus, the best silent-speech WER is 37.94% speaker-dependent and 69.84% multi-speaker with a Kaldi TDNN-HMM (2021) [7]." Also: "'A highly attractive SSI modality' (§6) rests on one speaker; across 82 speakers silent-speech WER is 69.84% [7]."
   Wrong: no quote contains 37.94, 69.84, TDNN or 82 speakers. The second sentence also sets a different corpus, LM and vocabulary against the target's single-speaker SSC result.
   Fix: add the quotes from [7]. Rephrase the bullet as "rests on one speaker; on a different, multi-speaker corpus with an in-domain bigram, silent-speech WER is 69.84% [7]."

10. Sentence: "... and 37.6% on the same 100 sentences after training on 7,484 new utterances (2022) [6]."
    Wrong: neither 37.6% nor 7,484 is in the quote.
    Fix: add the quote and location from [6] for both numbers, or drop them.

11. Summary table row: "M03 Training and adaptation | One speaker; DAE on 12 lists; 90/10 split | ... | not reported".
    Wrong: the verdict contradicts the filled cell.
    Fix: change it to "standard", or say which item is not reported, e.g. "validation use not reported".

12. Summary table row: "M07 Lexicon and LM | ... | Closed WSJ0 5k bigram (pattern match 3)".
    Wrong: the count of 3 is the M12 SSC-condition tally, not an LM-design tally.
    Fix: label it "(3 of 8 SSC studies, M12 tally)", or give the LM tally.

13. Sentence: "... yet both language models are closed 5k bigrams, so the acoustic model's share cannot be isolated."
    Wrong: no quote shows that the CSR bigram is closed or has 5k words.
    Fix: add the quote describing the CSR LM, or write "both language models are bigrams over the same closed task vocabulary" if that is what the source says.

## Scores

- Procedure: 6/10. Every row has a location, but several key numbers (TaL, SSR7000, the benchmark's 43.50) have no supporting quote, and the claim table was filled by the writer.
- Final text: 6/10. The position is clear and the tables were read closely. The baseline/LM confound is misread, there is one internal contradiction (DNN-HMM priors), and one metric mismatch.

Brief praise: the review gets the most out of the paper's own tables. It finds the Table 3/4 inconsistency and the K=5 collapse, and it puts the 6.45% result back in the context of the language model.
