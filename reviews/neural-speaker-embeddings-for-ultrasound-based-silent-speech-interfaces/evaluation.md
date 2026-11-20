# Evaluation: Neural Speaker Embeddings for Ultrasound-based Silent Speech Interfaces

Date: 2026-11-20. Independent evaluation of the review text and its claim table. The sources were not re-read; any check against outside knowledge is marked.

## Claim checks

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target trains an x-vector extractor on ultrasound and injects it into the multi-speaker estimator | Claim rows 1, 12 (t1, t37) | correct | The quotes support both steps and the transfer-learned initialisation. |
| 2 | Conditioning gain is 0.014 dev and 0.016 test MSE, "about 2%" relative | Row 3 (t28 to t32) | correct | 0.014/0.603 = 2.3%, 0.016/0.669 = 2.4%. "About 2%" slightly understates; "about 2.4%" is exact. |
| 3 | "from one run on speakers seen in training (inference)" | Row 3 (t35) | wrong label | The authors state the seen-speaker condition themselves (Sec. 5.3, t35). Only "one run" is inference. As written, the marker makes an author statement look like the review's own inference. |
| 4 | 0.70% error pools segments "from one recording per speaker" (Verdict) | Rows 4, 19 (t19, c5) | insufficient evidence | One session per speaker is inference from corpus totals (row 19 says so). The M06 section marks it as inference; the Verdict states it as fact. |
| 5 | [3] holds out sessions | Row 4, 18 (c17) | correct | The quote supports it. |
| 6 | TaL conditioned its decoder on audio x-vectors "pre-trained on 75 speakers" [4] | Row 6 (c1, c2) | wrong | c2 says the multi-speaker decoder uses data from 75 TaL80 speakers. Nothing quoted says the x-vector extractor was pre-trained on 75 speakers. The extractor comes from the Kaldi toolkit (c1); its training data is not given. |
| 7 | Target departs by computing x-vectors from ultrasound (Sec. 1) | Row 7 (t54) | correct | |
| 8 | V2SFlow: removing the speaker embedding lowers SECS 0.664 to 0.587, WER 28.5 to 28.7 [5] | Row 8 (c9 to c12) | insufficient evidence | The numbers match the quotes. No quote shows that "w/o cs" is the speaker-embedding ablation. The full-model row comes from Table I and the ablation row from Table III. Same-table rows and the definition of "cs" are needed. |
| 9 | [2] i-vectors from lip video, fed to hidden layers, 15% and 10% relative gains on unseen GRID speakers | Row 10 (c6 to c8) | partly supported | Mechanism and gains match c6 to c8. No quote names GRID. |
| 10 | Target gain rests on one run, same 31 speakers, MSE 0.603 to 0.589 and 0.669 to 0.653 | Row 11 | correct | |
| 11 | Extra training is not separated from speaker information (inference) | Row 12 (t37) | correct as inference | This is a fair confound, and it is labelled as inference. |
| 12 | Target scores closed-set identification on 50 speakers and 1-NN leave-one-out on 31 speakers | Row 15 (t5, t19) | correct | |
| 13 | Wang [6] 95.22% identification on 68 speakers; 4.78% error | Row 16, 17 (c21, c22) | correct | 100 − 95.22 = 4.78. |
| 14 | Kojima [7] NAM verification 0.04% EER (2006) | Row 16 (c13) | incomplete | The quote gives 0.04% (male) and 1.1% (female). The review reports only the male figure. EER also does not measure the same thing as identification error. |
| 15 | [3] EMG held-out session, 83% and 84% accuracy against 55% chance | Row 18 (c17 to c19) | correct | |
| 16 | TaL80 has 81 speakers, 16,639 utterances, about 205 per session | Row 19 (c5, t2) | insufficient evidence | 81 and 205 are quoted. 16,639 has no quote. |
| 17 | TaL did not normalise probe position; authors note misalignment | Row 20 (c4, t55) | correct | |
| 18 | The embedding layer was chosen on the same pool (Table 2) | Row 21 | insufficient evidence | No quote shows layer selection. t18 lists four error rates without saying how the reported one was chosen. |
| 19 | "Below 3%" is a development-set figure, 1.96% to 3.16% | Row 22 (t10, t13, t40) | correct | |
| 20 | The 1,145 test blocks are never scored | Row 22 (t6) | insufficient evidence | t6 does not show whether these blocks belong to the 50-speaker recognition data or to the SSI data. |
| 21 | Authors call the gain "consistent but marginal" | Row 23 (t33, t39) | partly supported | t33 supports "marginal" only. t39 (swish nonlinearity) is irrelevant here; it also appears without reason in row 3. |
| 22 | Single-speaker MSE about 0.26 is attributed to Fig. 3 although the values are in Table 3 | Row 24 | correct but misplaced | This is a citation slip in the paper, not a claim that outruns the evidence. |
| 23 | Test MSE rises 2.5-fold from single- to multi-speaker training | Row 25 | correct with a caveat | 0.669/0.265 = 2.52. The two test sets may differ in speaker composition, and the review does not state that condition. |
| 24 | M05 "82 fps", M08 "80-dim mel, WaveGlow" (component table) | Claim table | no quote | No claim rows. |
| 25 | Chronology: [2], [3], [4], [6], [7], [8] are prior; [5] is labelled [later] | References | correct | [6] is ICPR 2020 (held January 2021, arXiv October 2020). The label "ICPR 2021" should read "ICPR 2020 (2021)". Page ranges and DOIs were not checked against outside sources. |

## Central claim, confounds and verdicts

- **M03.** The strongest confounds are fine-tuning from transfer-learned weights versus speaker information, and evaluation on seen speakers. The review handles both. The "standard" verdict is defensible because [2] is a deciding prior. However, signal-derived vectors are a minority design (8 of 42) and the review itself says the paper "departs" from the usual approach. One sentence should reconcile "departs" with "standard".
- **M06.** The strongest confound is speaker versus recording session or probe placement. The review handles it well. The "behind" verdict, however, does not follow from the named state of the art. [6] and [7] are the cited state of the art, and the target's error is numerically better than [6]. The basis for "behind" is protocol (cross-session testing in [3]), and [3]'s numbers are far lower. Either say plainly that the verdict concerns the test protocol and put [3] in the table's state-of-the-art column, or change the verdict.
- **State of the art.** For M03, V2SFlow is a cross-modal (video-to-speech) work. The review should say whether any later ultrasound-to-speech work tests speaker conditioning on unseen speakers. If none does, it should label [5] as cross-modal. For M06, I cannot name a specific later articulatory speaker-recognition result with confidence (insufficient evidence).
- **Fairness.** No later work is treated as prior work or as a missed citation. The seen-speaker limitation is credited partly to the review (the "(inference)" marker in the Verdict); the authors state it themselves.
- **M12 verdict.** "not reported" is not apt: MSE and error rates are reported. Use the verdict vocabulary from the rules, or explain the label.

## Required fixes (ordered by impact)

1. M06: align the "behind" verdict with its evidence. State that it concerns the cross-session protocol, name [3] as the comparator in the section and the table, or change the verdict.
2. M03 / TaL [4]: remove "pre-trained on 75 speakers". The 75 speakers are the decoder's training data (c2); the source of the x-vector extractor is Kaldi (c1).
3. Verdict: credit the seen-speaker condition to the authors (Sec. 5.3). Keep "(inference)" only on "one run", and add an inference marker to "one recording per speaker".
4. V2SFlow [5]: quote the definition of "w/o cs" and take the full-model and ablation rows from the same table. Otherwise the SECS 0.664 to 0.587 effect is not shown.
5. Kojima [7]: report both 0.04% (male) and 1.1% (female) EER, and note that EER is not comparable with identification error.
6. "The 1,145 test blocks are never scored": add a quote showing that these blocks belong to the 50-speaker recognition set, or soften the sentence.
7. "Embedding layer chosen on that same pool": add the location showing layer selection, or drop the clause.
8. "Consistent": add the quote, or attribute only "marginal". Remove the irrelevant t39 quote from claim rows 3 and 23.
9. M12: replace "not reported" with a verdict the rules allow.
10. Add claim rows for 16,639 utterances, 82 fps, 80-dim mel and WaveGlow, and add the GRID locator for [2].
11. 2.5-fold MSE rise: state whether the single- and multi-speaker test sets contain the same speakers.
12. Move the Fig. 3 / Table 3 slip out of "Where the claims outrun the evidence", or drop it.
13. M03: reconcile "departs" with "standard", and label [5] as cross-modal unless an ultrasound-specific later result exists.
14. Reference [6]: change "ICPR 2021" to "ICPR 2020 (held 2021)". Change "about 2%" to "about 2.4%".

## Scores

- Procedure: 7/10
- Final text: 6/10

The review identifies the main confound in each component (session versus speaker for M06; fine-tuning and seen speakers for M03), and most numbers trace to quotes.
