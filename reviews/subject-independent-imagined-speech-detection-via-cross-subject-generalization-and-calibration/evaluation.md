# Evaluation: Subject-Independent Imagined Speech Detection via Cross-Subject Generalization and Calibration

2026-11-24
Evaluator: a language model separate from the writer (claim table and review text only; no sources opened)

## Claim checks

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper changes "only" the training regime of an "inherited" detector; 5–15% calibration, 2-epoch fine-tune | Claim 1, t10, t11 | insufficient evidence | t10/t11 support calibration share and 2-epoch fine-tune. Nothing quoted shows that the model (MRF-EEGNet) and the pipeline are inherited, so "only" and "inherited" rest on no quote (t65 covers the dataset only). |
| 2 | Cyclic schedule "rests on one comparison of two settings, with no pooled baseline and no seeds" | Claims 2, 9, 20; Table I rows | partly wrong | Table I also compares (5,6) and (3,10) at 5/10/15% calibration (e.g. 10%: 0.778 vs 0.781 accuracy), so there are four paired comparisons of the same two settings, not one. "No pooled baseline" is consistent with the quotes. "No seeds" is stated as fact, but the review also asks what the ± values aggregate; it should say "seeds not reported". |
| 3 | Strict LOSO MCC 0.044 and 0.123 | t25, t29 | correct | Values match. "Barely separates" is consistent with AUC 0.562/0.619. |
| 4 | Target calibration after source training described by 2021 [2] | Claims 3, 10, r7 | insufficient quote | r7 ("source subjects and transfer learning is employed to improve") is a fragment and does not show fine-tuning on a new target subject's data. |
| 5 | Every label is an overt-timed surrogate, so detection of imagery itself is not shown | Claim 5, t3, r1 | correct quote; conclusion overstated | t3 supports overt-speech-based alignment. "Detection of imagery itself is not shown" is the reviewer's inference and is not marked as such. M11 marks the related cue-locking point "(inference)"; the Verdict should do the same. |
| 6 | M03 usual-approach tallies (141; 61/56/38/25) | Appendix | correct (tally) | Matches the Appendix. Not audited per brief. |
| 7 | Belfrouh 2026: 5 classes, 15 subjects, ~20% chance zero-shot, 53.71% at 60-shot, ~25 min, 5 seeds | r9–r13 | correct | Arithmetic is consistent: 60 × 5 classes × ~5 s = 25 min. Labelled [later] and not treated as prior. Caveat: this is five-class decoding, not binary speech/idle detection, and the review does not state that difference. |
| 8 | 4 cyclic hits, 3 false positives | Appendix | correct (tally) | See item 16: the three false positives are not named. |
| 9 | 5×6 = 3×10 = 30 epochs; accuracy 0.694→0.670, MCC 0.044→0.123, overlapping spreads | t13, t14 | correct | Values and arithmetic correct. The spreads overlap (±0.036/±0.092; ±0.143/±0.069). The text never says which row is the "cyclic" condition and which is the reference ("the switch" is undefined). |
| 10 | [5] fine-tunes on ten trials per class, concurrent, same institution | c14 | correct | Quote supports it. arXiv 2511.07936 is about one week before the target, so [concurrent] is right. |
| 11 | 59% of MCC gap and 76% of AUC gap closed at 10% (3,10) | t45, t21, t29 | correct | (0.382−0.123)/(0.561−0.123)=0.591; (0.801−0.619)/(0.860−0.619)=0.755. "From strict LOSO" means the (3,10) strict row, not the (5,6) row; say so. |
| 12 | M11 usual approach 10 of 49; [6] labels by cue and block | c23 | correct | |
| 13 | Soroush: onset/offset from the same participant's average overt timings, sEEG, 7 participants | r1–r3 | insufficient quote | r3 is truncated before "of …", so "same participant's" is not shown. Participant count and sEEG are supported. |
| 14 | Sharon & Murthy 2020: LOSO speech/non-speech detection, ≈76% | r5, r6 | insufficient quote | r6 ("siﬁer is ≈76%") does not show which classifier, task or condition the 76% belongs to. |
| 15 | Attar 2025: 82.4%, macro-F1 0.70, 8 words, LOSO over 4 participants | r15, r16 | correct numbers; questionable SOTA | The numbers match. A four-participant EEG–fMRI pilot on eight-word classification is weak as "state of the art" for a LOSO evaluation of binary detection; the task difference is not stated. |
| 16 | Strict LOSO 0.694 accuracy and MCC 0.044 imply a dominant idle class | t23, t69 | correct as inference | Labelled (inference). "Implies" is stronger than the evidence; "suggests" fits. |
| 17 | M13 tallies 445/110/15/4 | Appendix | correct (tally) | |
| 18 | Bhadra 2025: closed-loop binary syllable imagery, 100 ms delay, daily recalibration | c20, c18 | partly insufficient | c20 supports 100 ms. c18 says offline data calibrated the decoder; it shows neither "daily" nor "binary syllable". |
| 19 | "Consistent" gains vs accuracy 0.694→0.670 | t17, t23, t27 | correct | t17 ("modest yet consistent improvements") is quoted. The bullet would be fairer if it noted that MCC, F1 and AUC do rise. |
| 20 | "All metrics improved progressively": accuracy 0.778 at 10% vs 0.777 at 15% (5,6) | t59, t39, t47 | correct | Read the row labels and condition (SC-LOSO, (5,6)). The drop is 0.001, so this is a weak counterexample, but the factual point stands. |
| 21 | MCC 0.358 ± 0.791 is an "outlier spread" | t41 | correct value; framing weak | The ± equals the AUC value in the same row (0.791), which points to a transcription error in the paper rather than a real spread. Say "likely typo (± matches AUC 0.791)". |
| 22 | Fig. 2 caption assigns (5,6) to both curves | t82 | correct | |
| 23 | 90% overlap; no trial-level split stated | t2, t70 | correct | (500−50)/500 = 90%. |
| 24 | Authors call the evidence "preliminary" (§I); "scalable, user-adaptive" in the Abstract | none | insufficient evidence | The claim table has no row or quote for either phrase. |
| 25 | Bibliography: target author initials | Header vs ref [1] | inconsistent | Header gives "Ko, B.-K., … Lee, S.-H."; ref [1] gives "Ko, B., … Lee, S." Use one form. |

## Central claim, confound and positions

- **Strongest confound:** the surrogate labels (M11). The review names this as "the main confound" and handles it. The second confound is window leakage between calibration and test (90% overlap, no trial-level split). The review raises it under the claims and in the questions, but the Verdict does not say that the calibrated gains (MCC 0.382, AUC 0.801) may be inflated by it. It should, because the Verdict's "holds only with the target's labelled data" depends on those calibrated numbers.
- **Absolute vs relative:** the gap-closure percentages (59%/76%) are marked as inference and computed correctly.
- **Position strength:** "detection of imagery itself is not shown" (Verdict) and "implies a dominant idle class" (M12) are stronger than the evidence; mark the first as inference and soften the second.

## Absence, novelty and verdicts

- "No counterpart among 141" names neither the deciding prior works nor the three false positives. Episodic training over subjects in cross-subject EEG meta-learning (MAML-style, around 2020–2021) is a plausibly similar design, but I cannot give a locator for it (unverified). The review should name the closest priors it checked.
- M03 verdict `standard` sits next to "no counterpart among 141". The review explains this (the schedule's effect is not shown), but the verdict line should say so in one clause so the two statements do not read as contradictory.
- SOTA rows for M03 [4], M08 [7] and M12 [8] each address a different task (multi-class decoding, or a 2020 detection result) from binary speech/idle detection. The task mismatch should be stated in each row.
- Fairness: [4] is marked [later], and [5], [6] and [8] are marked [concurrent]. None is treated as prior work or as a missed citation. Correct.

## Required fixes (ordered by impact)

1. Verdict: add that the calibrated gains may be inflated by 90%-overlapping windows with no trial-level split, since "subject-independent only with labelled data" rests on those numbers.
2. Verdict and M03: "one comparison of two settings" is wrong; Table I compares the two settings at four calibration levels. Rephrase as "two settings only, compared without a pooled baseline".
3. Absence claim (cyclic schedule): name the deciding priors and the three false positives, or weaken to "no ledger hit".
4. Verdict: mark "detection of imagery itself is not shown" as (inference).
5. Claim 1: support "only" and "inherited" with a quote (model reused from prior work), or drop the two words.
6. Questionable SOTA choices: state the task mismatch for [4] (five-class decoding), [7] and [8] (eight-word, four-participant pilot), or choose binary-detection comparators.
7. MCC 0.358 ± 0.791: describe it as a likely transcription error (± equals the AUC in the same row).
8. "Authors call the evidence preliminary (§I)": add a quote to the claim table or remove the phrase.
9. Insufficient quotes: [2] target calibration (r7), [3] "same participant's" (r3), [7] the 76% condition (r6), [9] "daily recalibration" and "binary syllable" (c18). Extend the quotes or soften the wording.
10. M03: name which row (5,6) or (3,10) is the reference for "the switch", and say that the 59%/76% baseline is the (3,10) strict row.
11. "No seeds" → "seeds not reported", to match the authors' question.
12. Reference [1] vs header: make the author initials consistent.

## Scores

- Procedure: 7/10. The claim table covers every number, and the arithmetic and the chronology labels are correct. Several quotes are fragments too thin to carry the claim.
- Final text: 7/10. The position is clear and well targeted (surrogate labels, the near-chance strict LOSO result, the Fig. 2 caption error). It overstates "one comparison" and leaves leakage out of the Verdict.
