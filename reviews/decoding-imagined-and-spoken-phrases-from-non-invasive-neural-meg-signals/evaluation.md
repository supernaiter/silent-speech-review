# Evaluation: Decoding Imagined and Spoken Phrases From Non-invasive Neural (MEG) Signals

Evaluator: a language model separate from the writer

Date: 2026-11-27. Inputs: compact.md, the review draft (.md), slots.json, verdict.json, claims.md, the three topic audits, and these source texts in the wiki (read-only): target `pmc-7154084-megphrases/source/text.txt`; `pmc-7668411-megsel` [2]; `arxiv-1705.07771` [3]; `arxiv-2601.15909-imgmeg` [4]; `pmc-6876632-megtrials` (not cited by the review); `isca-dash19_interspeech`; `pmc-12379578-spont-intend`; `pmc-4437274-silentvoc`; `pmc-6210443-mccnn`. I also ran a full-text scan of the wiki for imagined, covert or inner speech decoders up to 2019.

## 1. Claim check

| # | Claim (location in review) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | ST-CNN 91.71%, SST-CNN 93.24% for imagination, p = 0.2135 (M06) | Target Sec. 4.1 | correct | Both quotes match. p = 0.2135 is the ST vs SST comparison in the preparation stage. |
| 2 | Augmentation (100/200-ms shift) only for SST-CNN, which the authors concede (M06) | Target Sec. 3.2.4.2, 5.1 | correct | |
| 3 | ANN has 1,176 inputs for about 250 training trials (M06, Verdict) | Target Sec. 5.1 | correct | This is the authors' own point ("A dimension reduction strategy ... may improve the performance"). The review does not say so. |
| 4 | ANN imagination 80.83% (Verdict, M06) | Target Sec. 4.1 | correct | |
| 5 | "SST-CNN classifies the pre-stimulus window at 42.96% against the authors' 30% chance (Table 1)" (Verdict) | Target Table 1, Sec. 4.1, 4.2 | partly wrong | 42.96% is the **Mean** row over three SST-CNN architectures. AlexNet, the network behind 93.24%, gives 43.77%. The 30% is in Sec. 4.2, not Table 1, and it is a finite-sample significance threshold (N ≈ 300). Sec. 4.1 also says all three methods (ANN included) were above chance before the stimulus and did not differ from each other. |
| 6 | "22.96 above the 20% of their later study" (M12) | Target Sec. 4.2 | wrong attribution | The target itself gives 20% as the theoretical chance ("20% is for ideal population size"). |
| 7 | "the authors raise carryover (Sec. 5.3)" (M12) | Target Sec. 5.3 | correct | The authors write that previous trials "could possibly corrupt the current trial's signals at least during the pre-stimuli". The Verdict presents the floor as the reviewer's finding without this credit. |
| 8 | [2]: 45.46% (196 sensors) and 54.34% (9 sensors) for imagination, 76.62% for articulation; SVM, 5-fold CV, 7 subjects, 20% chance | [2] Sec. II, III.B | correct, conditions incomplete | Two conditions are missing: [2] keeps only 60 trials per phrase, and its 5-fold CV is also a within-subject trial split of the same session. |
| 9 | "The same features drop 43.8% relative between the two protocols" (M12) | arithmetic | correct arithmetic, invalid finding | (80.83 − 45.46)/80.83 = 43.8%. But both "protocols" are within-session trial-level splits. Classifier, trial subsample, cohort and fold scheme all change together, so this is not a protocol comparison (see F2). |
| 10 | Jhilal: removing ImageNet weights lowers imagery vs silence from 90.4 to 81.6 and LOSO three-vowel from 51.7 to 46.0; relative drops 9.7% and 11.0% (M03) | [4] Table 4 | numbers correct, conditions missing | 90.4→81.6 is SAP (subject-agnostic pooled 10-fold), binary, 50% chance; 51.7→46.0 is LOSO, 33% chance. The cited RandomInit row uses *partial* fine-tuning: early and mid layers stay frozen at random weights. RandomInit + full FT (80.2 SAP / 69.1 LOSO for imagery vs silence) is the fairer from-scratch arm. |
| 11 | "To our knowledge, this is the first study using CNNs to explore neural speech decoding with MEG", same paragraph cites Dash et al. 2019a (M03) | Target Sec. 1 | quote correct, inference weak | The quote is exact and complete, and Dash 2019a is cited in the same paragraph. But the review treats [5] as the target's own earlier version, so this is a self-citation, not a contradiction (see F4). |
| 12 | Trial counts disagree: about 75 / about 50 / about 60 per phrase per subject | Target Sec. 2.3, 3.2.4.2, 4.2, 5.1 | mostly wrong | "about 50 per phrase per subject" refers to training images. That matches 70% of about 75 and Sec. 5.1's "about 250 per subject across 5 phrases" for training (inference). Only "~60" (Sec. 4.2) is loose. |
| 13 | Table 2 rows each sum to 1,382 with 40–51 errors, while the text reports about 12 per phrase | Target Table 2, Sec. 4.1 | sums right, contrast wrong | Row sums are 1,382 and row errors are 50/44/51/45/40. The text's "about 12" is the mean per off-diagonal cell (230/20 = 11.5; 12/1,382 = 0.9%), which agrees with the table. The real inconsistency is the footnote "A total of 1,382 test trials" against five rows of 1,382 each (6,910). |
| 14 | Pairwise t-tests uncorrected; seeds and splits unreported | Target Sec. 3.1, 4.1 | correct in part | No correction is stated. Split proportions (70/15/15, three runs) *are* reported; what is missing is split indices, stratification and seeds. |
| 15 | No EMG recorded; timing claim (Sec. 5.3) not measured | Target Sec. 2.1, 5.3 | correct, incomplete | EOG, ECG, microphone and a jaw-motion air bladder were recorded (Sec. 2.1). Jaw motion during the preparation window is never reported, and that is the checkable omission. |
| 16 | 17 prior, "no MEG-only" prior; 12 shallow, 2 any CNN, 0 TF-image CNN (Appendix, M06) | audits; wiki full-text | wrong | Misses Dash et al. 2018 (see F1). Includes a synthetic-data study (see F5). |
| 17 | 13 of 17 test on held-out trials "of the same recording" (M12) | M12 audit | insufficient evidence | The pattern covers k-fold, LOO or random splits. "Same recording" was not confirmed, and the 13 likely include the across-day thesis [7]. |
| 18 | EMG during covert speech [6], across-day [7] in 1 of 17 each | [6], [7] quotes; audit | correct | These counts were read-confirmed, yet the Appendix labels them "pattern match" (see F8). |
| 19 | [5] labelled [concurrent] and "earlier version" (M03, refs, Appendix) | refs, Appendix | contradictory | See F4. |
| 20 | M06 State of the art: "No later imagined-speech MEG study reports a higher five-class score" | M06 audit | insufficient evidence | No Appendix count supports this absence. Later MEG studies in the wiki that I checked are binary or three-class ([4]; Dash et al. 2024 JSLHR, 67.19% binary intended speech). I found no counterexample (unverified). |

## 2. Required fixes, ordered by impact

**F1. High. Appendix (population); M06 Usual approach; Verdict "17 earlier ... decoders"; Appendix "no MEG-only".**
Evidence: the same group's Brain Informatics 2018 paper, "Determining the Optimal Number of MEG Trials: A Machine Learning and Speech Decoding Perspective" (wiki `pmc-6876632-megtrials` and `doi-10.1007-978-3-030-05587-5_16`, year 2018, cited by the target as Dash et al. 2018c), is a prior MEG imagined-speech decoder. It uses the same five-phrase paradigm, an ANN on wavelet RMS features, a 70/15/15 split and 4 subjects, and reports "the imagined speech information can be extracted with an accuracy of 78.35%". The population pattern missed it: "imagination stage" does not match `imagin\w* (speech|...)`, so it has 2 hits, below the 3-hit threshold. The paper also reports a pre-stimulus accuracy that rises with trial count, and the authors explain it this way: "the subjects may have started to memorize the stimulus with time, as in total 5 number of stimuli were used".
Fix: add it as a prior (18 prior unique studies; one MEG-only; shallow classifier 13/18; within-subject trial split 14/18). Name it as the deciding prior for the ANN comparator in M06. Cite its pre-stimulus observation and the authors' explanation in M12, next to the question about the pseudo-randomised order. Delete "no MEG-only" and "No MEG imagined-speech decoder is among the priors". Also add "imagination stage|imagination segment" to the topic pattern and rerun the recall check.

**F2. High. Verdict sentence 4 ("The same laboratory's [later] study ... 45.46% ... against 80.83% here"); M12 State of the art; M12 "drop 43.8% relative between the two protocols"; 13-components table M12 cell.**
Evidence: [2] also uses within-subject trial-level 5-fold CV of the same single session ([2] Sec. II.B: "4 folds (48 trials per phrase) for training and 1-fold (12 trials per phrase) for validation/test"). It also changes the classifier (SVM vs ANN with early stopping), keeps only 60 trials per phrase, and has 7 subjects against 8. So the gap is not an evaluation-protocol effect, and [2] is not a stronger evaluation design. SKILL.md says that when starting points differ, the comparison is not evidence of a difference.
Fix: remove the 45.46 vs 80.83 sentence from the Verdict and the 43.8% sentence from M12, or keep one clause saying the same features gave 45.46% under a different classifier and trial subsample, with no causal reading. For M12 State of the art, pick a study that evaluates on held-out participants. For example, [4] gives LOSO 77.5% for imagery vs silence (50% chance) and 51.7% for three vowels (33% chance), and its pre-cue window stays near chance (ResNet-18 pre-cue 35.9% SAP / 34.8% LOSO at 33%, Table 3), which is a direct contrast to the target's 43.77%. The same group's concurrent speaker-independent study (`isca-dash19_interspeech`, Interspeech 2019) can be named as [concurrent].

**F3. High. M06 paragraph 2 ("so the margin over its 80.83% is not a margin over the field's shallow decoders") and Verdict ("the comparator is an in-house network with more inputs than training trials").**
Evidence: the authors say the ANN baseline reproduces the prior approach they judged strongest: "ANN with wavelet-transform based statistical features (Rezazadeh Sereshkeh et al., 2017) has shown comparatively better decoding performance which inspired our pilot studies and baseline" (Sec. 1). It is also the lab's own 2018 design (F1, 78.35%). The over-parameterisation is the authors' own observation (Sec. 5.1). The confound the authors themselves concede is different: input representation (time-resolved scalograms vs time-integrated RMS) changes together with the classifier ("a clear interpretation ... is not straight forward, because of the inherent differences in the feature sets", "we did not intend to compare the features", Sec. 5.1).
Fix: report the authors' rationale and concession first. Base the `standard` verdict on the representation–classifier confound, plus mosaic vs per-sensor being n.s. for imagination, plus augmentation applied only to SST. Drop the claim that the baseline is not a field-typical shallow decoder.

**F4. Medium. Target time and the [concurrent] label of [5] (Appendix; M03 last paragraph; reference 5).**
Evidence: the Appendix sets target time to 2019-07 from [5] as "the EMBC 2019 version". Reference 5 calls it "Earlier conference version by the same group" but labels it [concurrent]. The Appendix's 8 [concurrent] studies do not include it. Its title says "transfer learning", yet M03 says 0 of 8 [concurrent] use ImageNet. Using a 2019-07 date is acceptable: it moves the windows by about one month against the 2019-08 journal submission and changes no count I could find. But [5] is unread, so the review cannot say that [5] contains the imagined-speech stage, the sensor mosaic or the ImageNet initialisation.
Fix: label [5] "earlier version of the target (date 2019-07)", not [concurrent]. Word the Appendix as "target time 2019-07, the date of the same group's EMBC 2019 conference paper on CNN transfer learning for MEG speech decoding [5]" and move the open point (contents of [5] unread) to verification_status. Then the "first study" sentence is a self-citation of the same work, not evidence against the claim. Drop it from M03, or move it to "Where the claims outrun the evidence" only if the point is that the journal cites its own conference paper as prior CNN work without saying it is the same study.

**F5. Medium. Deciding prior [3] and "2 any CNN" (M06 Usual approach; Appendix).**
Evidence: arxiv-1705.07771 states it "simulated decoding imagined speech EEG using synthetic EEG data" (Abstract). The inclusion rule requires "human electrophysiological recordings", so this is an off-population hit. The M06 audit note says the second "any CNN" hit (Rezazadeh Sereshkeh 2018 thesis) "names CNNs only as future work".
Fix: exclude [3] from the population, or label it outside the inclusion rule. Report CNN decoders among real-recording priors as 0 (pattern match 1, design-confirmed 0). Rewrite "the closest prior CNN convolves raw synthetic EEG [3]" as "the only earlier CNN in the wiki is a simulation on synthetic EEG [3], outside the population".

**F6. Medium. Verdict sentence 3 and M12 paragraph on the pre-stimulus floor.**
Evidence: see claim rows 5–7. 42.96% is the mean of three SST-CNN architectures; AlexNet gives 43.77%. The 30% is a finite-sample threshold (Sec. 4.2), and the target itself states 20% theoretical chance. The pre-stimulus accuracy does not differ across ANN, ST-CNN and SST-CNN (Sec. 4.1). The authors report the floor and offer carryover (Sec. 4.2, 5.3).
Fix: write "AlexNet SST-CNN classifies the 0.5-s pre-stimulus window at 43.77% (Table 1; mean of three networks 42.96%), against the authors' 30% finite-sample threshold and 20% theoretical chance (Sec. 4.2); all three methods are above chance and equal there (Sec. 4.1)". Credit the authors in the Verdict ("the authors report this and attribute it to carryover, Sec. 5.3"). Then say why carryover cannot predict the current label under unconstrained pseudo-random order (inference). Because the floor is method-independent, say that it does not explain the CNN–ANN gap.

**F7. Medium. Verdict last sentence ("not evidence of decodable imagined speech") and verdict.short ("inflates every stage").**
Evidence: imagination is 93.24% against a 43.77% floor, so about 49 points remain above the floor (inference). The review shows no additive inflation. The stronger, unnamed confound for "imagined" is that the preparation window starts at text offset, right after covert reading that is itself decodable at 87–90% (Sec. 4.2). Visual-offset and reading carryover, and phrase length, are the obvious sources. The authors raise duration only for articulation (Sec. 5.3).
Fix: state that the 93% shows phrase information in a post-reading preparation window, on top of a non-task floor of about 44%, and that it does not isolate imagery from visual and reading carryover or preparation. Add the visual-offset/length confound to "Where the claims outrun the evidence". In verdict.short, replace "inflates every stage" with "a 43% pre-stimulus floor (Table 1)".

**F8. Medium. Trial-count bullet and Table 2 bullet ("Where the claims outrun the evidence"); question about 1,382.**
Evidence: claim rows 12 and 13.
Fix (trial counts): "Sec. 2.3 gives about 75 trials per phrase per subject; Sec. 4.2 computes chance for ~60; the ~50 in Sec. 3.2.4.2 matches the training share (inference)."
Fix (Table 2): "Table 2's note gives 1,382 test trials in total, but each of the five rows sums to 1,382 (6,910 in all); 1,382 is close to three runs of the 15% test share of 3,046 trials (inference)". Delete the contrast with "about 12 per phrase", which equals the mean off-diagonal cell.

**F9. Medium. Jhilal comparison (M03 State of the art; 13-components M03 cell; "What the field needs next").**
Evidence: claim row 10.
Fix: add "SAP, binary, 50% chance" and "LOSO, 33% chance". Either use the RandomInit + full FT row (80.2 SAP, 69.1 LOSO for imagery vs silence) or say that the RandomInit row keeps randomly initialised layers frozen. Optionally add the drop in accuracy above chance (inference).

**F10. Medium. Count tiers (Appendix M06/M12; M12 Usual approach).**
Evidence: the M12 audit tier is "pattern match (unique studies); checked items read in body text", but the Appendix prints every sub-count as "(pattern match)". "13 ... held-out trials of the same recording" is stronger than a k-fold/LOO/random-split pattern supports.
Fix: give read-confirmed counts with their own tier ("EMG during covert speech 1, across-day evaluation 1, design-confirmed"). Give "any CNN" as pattern match and confirmed separately (F5). Write "13 of 17 use within-subject k-fold, leave-one-out or random trial splits (pattern match)".

**F11. Low. Population triage consistency (Appendix).**
Evidence: `pmc-4437274-silentvoc` (Sarmah and Kennedy) is included. It covers "attempts at inner speech in a mute and paralyzed subject" recorded with an implanted intracortical electrode, and it was published 2013-11 (the audit lists it as 2015). Brumberg 2011, the same lab and the same signal type (attempted speech from unit firing), is excluded.
Fix: apply one rule to both, and correct the year to 2013.

**F12. Low. M06 State of the art line.**
Evidence: claim row 20. [2]'s 54.34% comes from forward sensor selection; whether selection was nested inside the CV folds is not stated in the passages I read (unverified). It is a lower, later re-benchmark, not a better decoder.
Fix: write "The target's 93.24% remains the highest five-class imagined-phrase score among later MEG studies in the wiki (Appendix count needed); the closest later comparator is [2] ...", and add "60 trials per phrase, sensors chosen by forward selection". Otherwise drop the absence claim.

**F13. Low. Evaluation leakage question (Questions for the authors).**
Evidence: for ST-CNN, "trained with each scalogram image as a sample" and evaluated by averaging over the 196 sensor images of a trial (Sec. 3.2.4.1). The paper does not say whether the split kept all 196 images of a trial together. The review's questions omit this, and it is the most direct trial-level leakage risk besides temporal adjacency.
Fix: add "For ST-CNN, were the 196 sensor images of each trial assigned to the same partition?". Replace "splits are unreported" with "split indices, stratification and seeds are unreported".

**F14. Low. EMG point ("Where the claims outrun the evidence", first bullet).**
Evidence: the jaw-motion sensor and microphone were recorded (Sec. 2.1) but are not reported for the preparation window. This criticism is stronger than "no EMG". EMG absence is otherwise weighted correctly: it is listed as a claim issue, not used to call M12 `behind` (1 of 17 priors).
Fix: add "the jaw-motion channel recorded in Sec. 2.1 is not reported for the preparation window".

**F15. Low. Placement and restatement.**
Evidence: the "first study" quote sits in M03, but it is a claim issue, not a training-component comparison. "The paper replaces this with scalogram CNNs (Sec. 3)" repeats the Verdict. Verdict sentence 1 describes the pipeline in more detail than the comparison needs. Appendix "Read: ..." lines and "Known-item recall" are process notes; keep them only if the Appendix template requires them.
Fix: move or drop the quote (F4), delete the repeated sentence, and shorten Verdict sentence 1 to the two changed components. M03 Appendix: replace "none before 2020 other than the target" with "none earlier than the target" (the target is itself 2020).

**F16. Low. Fairness wording (M06, Verdict).**
Evidence: "more inputs than training trials" and the augmentation confound are both the authors' own statements (Sec. 5.1).
Fix: introduce them as "the authors note ...", per the SKILL fairness rule.

## 3. Answers to the specific questions

- **Counting date 2019-07.** Acceptable as the date of the same group's conference paper. It shifts no count against the 2019-08 submission. But [5] is unread, so the review must not claim what [5] contains, and [5] is mislabelled [concurrent] (F4).
- **Population of 17.** It misses a direct same-lab MEG prior (F1, a pattern recall gap). It includes one off-population synthetic-data study (F5) and treats the Kennedy-lab attempted-speech studies inconsistently (F11). Version duplicates were collapsed correctly (`pmc-3945950-covertvowel`/`-covertvowl`, `fneng.2014.00014`/`pmc-4034498`, `srep25803`/`pmc-4863149`, `s10916-018-1137-9`/`pmc-6299054`, `2016-2618265`/`pmc-5206788`). Pattern counts and design counts are not kept apart (F5, F10).
- **M06.** [3] is the wrong deciding prior: it is off-population, and the right one is the lab's 2018 ANN study. `standard` is defensible under the rule "difference not supported well enough to call", but the stated reason is wrong (F3). The 45.46%/54.34% study is later and from the same lab. It is not a state of the art; at most it is a closest later comparator under a different classifier and trial subsample (F2, F12). The 43.8% comparison is confounded and should not appear as a finding (F2).
- **M03.** 0/17 ImageNet initialisation would not make it `ahead`, because the effect of pretraining is never shown. "No from-scratch arm" is enough to call it `standard` under the rule. Jhilal 2026 is cited with the right numbers, but its conditions are missing and the from-scratch arm cited is the weaker one (F9).
- **M12.** The pre-stimulus control is read slightly wrong: wrong row (mean vs AlexNet), wrong source for the 30% (Sec. 4.2, not Table 1), and the 20% misattributed. The authors are credited only in M12, not in the Verdict (F6). Leakage risk is raised only through the floor; the per-sensor-image split question is missing (F13). EMG absence is weighted correctly (F14). The SOTA is mis-chosen (F2).
- **Paper claims.** Table 1 and the Sec. 4.1 numbers, 93.24 vs 91.71 with p = 0.2135, and the "first CNN" quote are all exact. The trial-count and Table 2 inconsistencies are partly misdiagnosed (F8).
- **Restatement or disclaimers in the body.** There are minor restatements (F15) and no methodological disclaimers in the body.

## 4. Scores

- Procedure: 5/10. A same-lab MEG prior is missing from the population, an off-population item is used as the deciding prior, and the evaluation SOTA is mis-chosen.
- Final text: 6/10. The core critique (floor, preparation window, no from-scratch arm) is sound and well located. Several numbers carry the wrong condition or attribution, and one confounded comparison carries the Verdict.

Counts by severity: High 3, Medium 7, Low 6.
