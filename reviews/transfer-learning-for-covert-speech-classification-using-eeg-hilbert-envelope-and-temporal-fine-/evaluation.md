# Evaluation: Transfer Learning for Covert Speech Classification Using EEG Hilbert Envelope and Temporal Fine Structure

Date: 2026-11-19. Fallback evaluator (claim table only). Input: the compact review (Verdict, component sections, component table, "Where the claims outrun the evidence", references) and its claim table. No sources were opened; each claim was checked only against the quote and location given in the claim table. Wiki-derived counts (ledger tallies, tiers, recall) are outside this check.

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target: 79.82% transferred BiLSTM vs 66.94% from scratch | Row 1, 7; Table II, Table III quotes | correct | Both values appear in the quoted average rows. |
| 2 | Target: gain 12.88 points, 19.2% relative | Row 3, 7 (inference) | correct | 79.82 - 66.94 = 12.88; 12.88 / 66.94 = 19.2%. |
| 3 | Target: fine-tuned on 15-30% of covert trials | Row 1, 21; §III.C quote | correct | Quote lists 15, 20, 25, 30%. |
| 4 | Target: "frozen" recurrent layers, only output layer re-trained; five commands | Row 1, M03 table row | insufficient evidence | No quote states which layers are frozen or the number of target commands. |
| 5 | Verdict: 79.82% results from re-training on 15-30% | Row 1 vs Row 8, 21, M12 | wrong (internal inconsistency) | The review itself says the fraction behind 79.82% is not stated and reads Fig. 3 as about 48% at 15%. The Verdict sentence implies the whole range gives 79.82%. |
| 6 | Target's "no research has yet attempted a direct transfer" is wrong; Lee et al. did so with five words [2] | Row 2, 16; §II, [2] §II.B.3 quotes | correct | Quotes support both the target's claim and the five-class transfer test in [2]. [2] predates the target (arXiv December 2022). |
| 7 | Target's data source [3] is titled as overt-to-silent transfer; Table IV lists it at 61.78% | Row 2, 16; target reference [13], Table IV | correct | Title and Table IV row are quoted. [3] was not read in full (Appendix lists [2], [4], target only). |
| 8 | "Lee et al. is the only prior scalp-EEG one" (M04 usual approach) | Row 4; reference [3] | wrong / insufficient evidence | [3] is scalp EEG, 2022, titled overt-to-silent transfer, and co-authored by a target author. The review neither counts it nor explains its exclusion (for example, if it fine-tunes rather than applies an overt model unchanged). |
| 9 | [2]: overt-trained model 26.8% vs 30.5% imagined-only | Row 5; [2] Abstract quote | insufficient evidence | Only 26.8% is quoted, and the quote does not say which training condition produced it. The 30.5% has no quote. |
| 10 | [4]: session-held-out transfer "at chance", 29.2% and 25.4% vs 25% | Row 6; [4] Summary table | wrong (judgment) | The quote gives 29.2% with p = 0.04, which is above chance at p < .05. Only 25.4% (p = 0.50) is at chance. "Holding out whole sessions" is not in the quote. |
| 11 | [4]: 6.7% vs 6.25% over 21 subjects | Row 6 | insufficient evidence | No quote. |
| 12 | [4]: trial pairing inflates transfer, 9.0% vs 6.7% | Row 9 | insufficient evidence | The quote supports the mechanism (trial identity) but not the numbers. Applying it to the target's dataset is inference and should be marked. |
| 13 | Fig. 3: about 48% at 15%, about 81% at 30% | Row 8 | insufficient evidence | Read from a figure (inference); only the caption is quoted. Acceptable when marked as inference. |
| 14 | Table III does not state the from-scratch covert data amount; test set is 20% of "unknown" data | Row 3, 8, 9; §IV.B quote | correct | Absence claim recorded as unstated; the 20% quote matches. |
| 15 | 1000 x 128 features into a BiLSTM | Row 12; §III.B quote | correct | |
| 16 | M06 usual approach: other 48, CNN 37, SVM 17, linear 16, recurrent 16 | Row 11, 27, 28 | insufficient evidence (outside scope) | Ledger counts. The text calls them slot-filled; the component table says "pattern match 167". Use one label. |
| 17 | [5]: 96.4% four covert syllables, 64-channel, 10 participants, subject-specific, 2018 | Row 13; [5] Abstract, Methods | partly correct | 96.4% four-class and the one-class-per-run block design are quoted. Channel count, participants, "syllables" and subject-specific are not. The year is 2018 in the text but 2019 in reference 5. |
| 18 | [6]: ENV+TFS BiLSTM, 64 channels, 30.63% pooled, 18.41% held-out subject | Row 14; [6] Tables 2, 3 | insufficient evidence | The quoted rows hold three values each (30.63 / 40.69 / 59.14; 18.41 / 22.63 / 27.15). No quote shows which column is ENV+TFS BiLSTM on 64 channels, or why the first column, not the higher ones, is the comparator. |
| 19 | Target asserts ENV/TFS beat wavelet, CSP and Riemannian features | Row 15; §III.B quote | insufficient evidence | The quote says only "enhanced capability for detecting subtle patterns" and names none of the three feature types. |
| 20 | Overt-covert envelope correlations 0.4791 to 0.6607 | Row 15; §IV.A quotes | insufficient evidence | Three of the five commands are quoted. The range assumes these are the minimum and maximum. |
| 21 | "20 points below" vs a 12.88-point gap | Row 17; §IV.B quote | correct | Quote matches. Note: 86.44 (overt BiLSTM) - 66.94 = 19.5, so the authors' "20 points" may compare against the overt model. Saying so would make the point sharper. |
| 22 | Table II row means are 79.07% and 86.07% vs printed 79.82% and 86.44% | Row 18 | insufficient evidence | Per-subject values are not quoted, so the recomputation cannot be checked from the claim table. |
| 23 | "Did not deviate significantly (p<.05)" | none | no quote | This bullet has no claim-table row. |
| 24 | "Outperforms previous methods" compares 5-, 8-, 12-class tasks, ECoG and EEG | Row 19; Table IV quotes | correct | |
| 25 | Overt speaking adds muscle activity to the 0.5-80 Hz band; ICA rule not given | Row 20; §III.B quotes | insufficient evidence | The quotes cover the notch filter and baseline correction only. Neither the 0.5-80 Hz band nor the ICA wording is quoted. |

## Central claim, positions and verdicts

- **Strongest confound.** The baseline's starting point is the strongest confound: the covert data amount for the from-scratch models is unstated, and Fig. 3 suggests transfer at 15% falls below from-scratch. The review handles this, as well as absolute vs relative change and the within-person split. It handles the confound well.
- **M04 verdict `behind`.** The verdict rests on a missing control (no overt-only condition), not on a worse result. The review's own evidence, [2] and [4], shows overt-only transfer performing below covert-only training or near chance. Leaving out that condition does not place the paper behind the field. The "typical" base is one prior scalp-EEG study, while the confirmed 23 span microphone, camera and other modalities (Appendix). The position goes beyond its evidence. A reporting verdict (missing control) fits better than `behind`.
- **M04 state of the art.** The table cell "Session-held-out transfer at chance, 29.2% vs 25% [4]" names a non-peer-reviewed linear-baseline report as state of the art, and its own quote shows p = 0.04. A null baseline is not the best work. Say that no stronger overt-to-covert EEG result is known to the review, or name one.
- **M06 verdict `standard`.** Supported by the ledger tally. The state-of-the-art line relies on a block-design result that the review itself treats as confounded; that caveat is stated.
- **Fairness.** [4] is labelled [later] and [6] [concurrent]. Neither is presented as a missed citation, and [2] predates the target. That is fair. The point that [3], the dataset source with a shared author, already frames overt-to-silent transfer is the review's strongest evidence against the novelty claim. It should rest on a reading of [3], not on its title alone.
- **Hedging.** "Its claim ... is wrong" is a plain statement, and [2] supports it. No over-hedged wording was found.

## Required fixes (ordered by impact)

1. Replace "at chance" for [4] in the M04 state-of-the-art line and component table. 29.2% has p = 0.04, so only 25.4% is at chance. Also reconsider presenting a non-peer-reviewed null baseline as state of the art.
2. Change or justify the M04 verdict `behind`. A missing overt-only control is a reporting gap, the cited evidence shows that condition performs poorly, and the scalp-EEG base is a single prior study.
3. Reconcile "Lee et al. is the only prior scalp-EEG one" with [3]: scalp EEG, 2022, overt-to-silent transfer, a target co-author. Read [3] in full or state why it is excluded.
4. Add quotes for the unquoted comparator numbers, or remove them: 30.5% imagined-only in [2]; 6.7% vs 6.25% over 21 subjects, 9.0% vs 6.7%, and "holding out whole sessions" in [4]. State which training condition gave 26.8% in [2].
5. For [6], quote the column headers that show 30.63% and 18.41% are ENV+TFS BiLSTM on 64 channels, and explain why the higher values in the same rows (40.69, 59.14) are not the comparator.
6. Make the Verdict consistent with M12: say that the fraction behind 79.82% is not stated, instead of implying that 15-30% gives 79.82%.
7. Add a claim-table row and quote for "Did not deviate significantly (p<.05)".
8. Quote the target's text on frozen recurrent layers with a re-trained output layer, and on the number of commands (five).
9. Quote the target's comparison with wavelet, CSP and Riemannian features (§III.B), or drop the names.
10. Quote the 0.5-80 Hz band-pass and the ICA wording (§III.B) behind the artefact point.
11. For [5], quote the channel count, participant count, syllable stimuli and subject-specific evaluation.
12. Give all five envelope correlations, or confirm that 0.4791 and 0.6607 are the minimum and maximum.
13. Quote the per-subject Table II values behind the recomputed means of 79.07% and 86.07%, or drop the bullet.
14. Mark the application of [4]'s trial-identity leakage to the target's dataset as inference, unless [4] covers that dataset.
15. Use one count label for M06 (slot-filled vs pattern match 167) in the text and the component table.
16. Make years consistent: [2] is "In 2022" in the text but 2023 in the reference (say arXiv 2022), and [5] is 2018 in the text but 2019 in the reference.

Optional: in the "20 points below" bullet, note that 86.44 - 66.94 = 19.5, so the authors may be comparing with the overt model.

## Scores

- Procedure: 6/10. The arithmetic and target quotes are sound, but many comparator numbers have no quote, and [3] carries a central point without being read.
- Final text: 6/10. The position is clear and well structured, but the M04 verdict and the "at chance" wording go beyond the cited evidence.
