# Evaluator: a language model separate from the writer

Date: 2026-11-25. Target: Makin, Moses, Chang, Nature Neuroscience 23, 575–582 (2020), doi:10.1038/s41593-020-0608-8.
Input: compact.md only (review, references, claim table). I did not open the sources. I checked the claims against the claim-table quotes and against what I know of the field. I mark outside knowledge I could not locate as "unverified".

## Claim table

| No | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Four components changed: encoder–decoder, word output, MFCC targets, transfer (Verdict) | claims row 1 (t1, t11, t13, t27, t28) | correct | The quotes support all four. |
| 2 | "matched held-out blocks" (Verdict) | row 3, t36 | insufficient evidence | t36 says the held-out blocks were "randomly chosen". No quote supports "matched". |
| 3 | 30 models per condition, Holm–Bonferroni, length-only control (Verdict) | row 3, t34/t37/t23 | correct | |
| 4 | 3% on held-out repeats of the same 50 sentences (Verdict) | rows 4 and 28, t17/t26 | correct | |
| 5 | The cited 60% baseline is [4] Herff 2015 (Verdict, "Where the claims…") | row 4/26, t19 | insufficient evidence | t19 cites "ref. 9". No quote shows that ref. 9 is Herff et al. 2015. |
| 6 | Herff's 25% vs Makin's quoted 60% "mixes protocols" | row 26, h1/h3 | wrong framing (judgment) | 25% is Herff's best case ("as low as"). The 60% figure is tied to a 100-word vocabulary. That is a best-case vs vocabulary-size difference, not a protocol difference. |
| 7 | Krishna [2]: 9 or 30 repeated sentences, two electrodes, 70% WER (M06) | row 8, k1–k4 | insufficient quote | The 70% WER is quoted. "9 or 30 sentences" and "two electrodes" have no quote. |
| 8 | 33% to 3%, 91% relative (inference) (M06) | row 9, t18/t17 | correct | (33−3)/33 = 0.909. |
| 9 | "Without MFCCs, errors rise several-fold (Results)" (M02) | row 17 only quotes Brain2Char | insufficient quote | The claim table has no Makin quote for the no-MFCC ablation. |
| 10 | "combining them did not beat task transfer alone" (M03) | row 20, t29 | insufficient evidence / likely imprecise | t29 gives 36% for dual transfer vs 31% for task transfer. Numerically it did beat it. The text needs "not significantly" with a quote, or it should give both numbers. |
| 11 | Cross-participant transfer did not help the picture-description participants (M03) | row 20, t32 | correct | |
| 12 | Held-out blocks are "about 10% of data" (M12) | row 22, t36 | insufficient quote | t36 gives no proportion. |
| 13 | A word softmax emits only words seen in training; whole sentences substituted (M08) | row 14, t13/t42 | insufficient quote / internal tension | t13 says the output layer has 1,806 classes even for MOCHA-1-only training, so the layer can emit words that were never trained on. t42 does not mention sentence substitution. |
| 14 | "250-word closed task" (M08 verdict, M12) | row 14 | insufficient quote | No quote gives the MOCHA-1 vocabulary size. |
| 15 | Ablations: fourfold for "64 channels", eightfold for no convolution (Where…) | row 27, t20/t22 | partly supported | The fourfold and eightfold factors are quoted. "64 channels" is not. |
| 16 | Participant a starts at about 53% (Where…) | row 28, t62 | insufficient quote | t62 is "which is about 53%" with no subject. |
| 17 | "The tuning block stayed in the final tests … no seeds … public code sets none" (Where…) | no claim-table row | unsupported | This is a serious charge with no quote, no location and no record of a code inspection. |
| 18 | Card [6]: 2.5% WER, final 5 sessions, phoneme every 80 ms, 125k words (M06/M08 SoA) | row 7, c2–c4 | correct | |
| 19 | Willett [5]: 23.8% on never-duplicated sentences, 125k words (Verdict/M12 SoA) | rows 5/23, w4/w9 | correct number; questionable as "today's reference" | See finding 3. |
| 20 | Metzger [7]: 25.5% WER, 249 untrained sentences, 1,024 words, g2p labels (M02 SoA) | row 16, z2/z4/z9/z10 | correct | |
| 21 | Singh [8]: 25 patients, PER from 57% to 49%, 45% with four sources (M03 SoA) | row 19, l1–l3 | correct per quotes | The bibliographic details (Nat Commun 16, 8749) are unverified. |
| 22 | Brain2Char [3] [concurrent], same MFCC loss | row 17, b1 | correct | arXiv 2019-09 falls within 6 months of the target. Same lab (Chang), so it is not independent support. |
| 23 | Krishna [2] (2019-08) is prior ("The design is prior") | row 8 | unverified chronology | It appeared about 7 months before the March 2020 publication. If Makin et al. was submitted before August 2019, [2] is concurrent, not prior. Check the received date. |
| 24 | Ledger counts (M06/M08/M02/M03/M12) | Appendix | taken as exact | Not checked, per the brief. |
| 25 | Bibliography [1]–[7] | references | correct as far as known | The volume, pages and DOIs of [1] and [4]–[7] match my knowledge. [8] is unverified. |

## Findings (numbered, ordered by impact)

1. **Unsupported reproducibility charge.** "The tuning block stayed in the final tests, and no seeds are given; the public code sets none (Methods)" has no claim-table row, quote or code locator. It is a strong charge against the target's protocol. Either quote the Methods passage and give the repository file or commit inspected, or delete it.
2. **The non-`standard` question is answered with today's counts, not 2020's (M06, M02, M12, M07).** The verdicts rest on ledger counts that are dominated by later work. 82 of the 145 M06 studies are from 2023 onward, so at most 16 encoder–decoder studies predate 2023, and many of those likely follow Makin et al. The only named encoder–decoder prior is the EEG paper [2], which is close to concurrent (finding 5). The only MFCC-loss prior is concurrent and from the same lab [3]. The review therefore does not show that these designs were standard in 2020. Give pre-2020 counts, or name more than one independent earlier work per slot, before calling them `standard`. Otherwise reconsider the verdict under the SKILL.md rules. M12 is inconsistent on its own terms: the stated usual approach is sentence-disjoint (21 vs 10 repeated), and the review calls repeats "the paper's main limit", yet the verdict is `standard` (for 2020) with no 2020 tally. M07 has the same problem: the usual approach is an LM (slot-filled 119) and the paper uses none, yet the verdict is `standard`.
3. **The state-of-the-art values for unseen sentences contradict each other.** The Verdict and M12 call 23.8% [5] "today's reference" on never-repeated sentences. M06 and M08 cite 2.5% [6] (2024, same vocabulary) as the state of the art. The review never states whether Card et al.'s evaluation sentences were held out from training. If they were (my recollection, unverified), the M12 state of the art and the Verdict sentence are out of date. If they were not, M06 and M08 compare unlike tests. Either way, state [6]'s test condition. Also consider the Brain-to-Text '24 benchmark results on the Willett data, which report single-digit WER offline (unverified).
4. **The "mixes protocols" bullet misattributes the gap.** Herff's "as low as 25%" is a best case. Makin's 60% is tied to a 100-word vocabulary. The quotes show a best-case vs vocabulary-size contrast, not a protocol mix. The protocol point (repeats vs leave-one-phrase-out) is correct and already made in the Verdict. Also add a quote showing that Makin's ref. 9 is Herff et al. 2015; otherwise the [4] attribution of the 60% figure is an inference.
5. **Krishna [2] as "prior" is unchecked chronology.** The arXiv date is 2019-08, about 7 months before publication. The brief's fairness rule turns on whether the authors could have read it. Check the target's received date. If submission came before or near August 2019, relabel [2] [concurrent] and soften "The design is prior".
6. **"Combining them did not beat task transfer alone" conflicts with the quote.** t29 gives 36% for dual transfer vs 31% for task transfer. Quote the non-significance statement if the paper makes one, or report both numbers.
7. **"Matched held-out blocks" (Verdict) is unsupported.** t36 says "randomly chosen". Use "random held-out blocks".
8. **The M08 statements conflict with t13 and with the review's own question.** With 1,806 output classes even when training on MOCHA-1 only, the decoder can in principle emit words never trained on. That is why the review asks whether it does. "Emits only words seen in training" should be reworded to "can emit only the fixed 1,806-word MOCHA-TIMIT vocabulary". Add a quote for "whole training sentences substituted" and for the 250-word MOCHA-1 vocabulary.
9. **Several numbers lack a supporting quote:** "about 10% of data" (M12), "errors rise several-fold without MFCCs" (M02), "64 channels" (ablation), the subject of "about 53%" (participant a baseline), and "9 or 30 sentences" and "two electrodes" for Krishna. Add the passages, or drop the specifics.
10. **The M03 usual approach is weak.** A per-subject model in 90 of 379 studies (24%) is not shown to be the majority design. Say what the other 289 do, or phrase it as "the most frequent single design" if it is.
11. **Same-lab dependence is not stated.** Brain2Char [3] and Metzger [7] come from the target's lab (Chang). The review should say so where [3] is the deciding prior for M02.
12. **M05 label.** "Clinical ECoG" may understate the setup: t20 credits "high-density grids", and at least some participants had them. Check and relabel if needed (low impact).
13. **The central confound is handled.** The main confound (repeats of 50 sentences vs leave-one-phrase-out, with a different vocabulary and different participants) is identified in the Verdict and M12. The single-participant basis of the 3% figure and the ablations is also flagged. No fix needed beyond finding 4.

## Required fixes, by impact

1. Support or remove the tuning-block and seed charge (finding 1).
2. Give the 2020-era basis for the `standard` verdicts in M06, M02, M12 and M07, or revise them (finding 2).
3. Reconcile the 23.8% [5] and 2.5% [6] state-of-the-art values by stating each test condition (finding 3).
4. Reframe the "mixes protocols" bullet and confirm that ref. 9 is Herff et al. 2015 (finding 4).
5. Verify the target's received date and relabel [2] if needed (finding 5).
6. Correct "did not beat" and "matched" (findings 6 and 7).
7. Fix the M08 vocabulary wording (finding 8), and add the missing quotes or drop the unquoted numbers (finding 9).
8. Address findings 10–12.

## Scores

- Procedure: 6/10. The claim table is mostly complete and the quotes are accurate. However, one serious charge has no row, several numbers lack a quote, and the verdicts use present-day counts for a 2020 paper.
- Final text: 6/10. The position is clear and the central confound is identified. However, the state-of-the-art values contradict each other, and several wordings go beyond their quotes.

The quotes for the target's internal protocol (30 models, Holm–Bonferroni, length-only control) and for the comparator numbers ([5], [6], [7], [8]) check out.
