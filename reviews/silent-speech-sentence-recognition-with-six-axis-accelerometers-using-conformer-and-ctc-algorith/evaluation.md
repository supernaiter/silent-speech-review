# Evaluation: Silent Speech Sentence Recognition with Six-Axis Accelerometers using Conformer and CTC Algorithm (arXiv:2502.17829)

Date: 2026-11-24
Evaluator: a language model separate from the writer

Inputs: the evaluator brief and compact.md (review, reference list, claim table). No sources were opened; outside knowledge is marked "unverified".

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target changes decoder (Conformer+CTC), training data (concatenation + noise), sensing (six IMUs) | Claim table 1, 12 (§1, §2.1.2, §2.1.1) | correct | Quotes support all three. |
| 2 | Novelty claim of §1 fails against [2] and [3] | Claim table 2, 28 | correct, but insufficient priors | Luo §4.4 quote shows a CTC comparison for silent sentences; the [2] CTC quote is from Sec. I (introduction) and may describe earlier work, not Chen et al.'s own model (see fix 3). Earlier continuous silent-speech recognizers are not named (fix 5). |
| 3 | Liu et al. trained on concatenated sentences and tested on spoken ones [4] | Claim table 3, 13 | insufficient evidence | Concatenation is quoted. "Spoken", "93 sentences" and "n = 7" are not in any quote. |
| 4 | Headline 97.17% is a word ratio on 4 participants with an unstated split | Claim table 4 | partly wrong | Word ratio and 4 participants are quoted. The split is stated (70:15:15, §2.1.2). Its unit (sample, session, participant) is what is unstated. |
| 5 | M06 usual approach: 54 studies, HMM 30, CTC 16, attention 9 | Claim table 5, 39; Appendix | correct (tally) | Upper-bound counting is disclosed. The tally is not split by year, so "usual" HMM reflects older work. That is acceptable but could be noted. |
| 6 | CTC + cross-entropy loss (§2.3) | Claim table 6 | correct | §2.3.2 quote. |
| 7 | Chen et al. 2023: CTC, four 64-channel arrays, 33 phrases, 15 subjects, 97.17 ± 1.53%, CER 3.11 ± 1.46% | Claim table 7 | partly insufficient | Phrases, subjects, accuracy and CER are quoted. "Four 64-channel arrays" is unquoted. The CTC attribution comes from the Sec. I quote (see row 2). |
| 8 | "The target matches the accuracy on 4 participants, with a word-ratio metric" | Claim table 8 | overstated | The numbers are equal (97.17) but the metrics differ: phrase classification vs. a word ratio that ignores insertions. Vocabularies also differ (33 phrases vs. 16 words plus a few sentences). "Matches" implies a comparability the review itself disclaims. |
| 9 | Luo et al.: CTC vs. attention, 54 sentences, 8.1% WER on unseen sentences | Claim table 9 | correct | Abstract quote. |
| 10 | Target trains a single decoder (§3.2), states no CTC search or LM (§2.3.1), tests no held-out combination | Claim table 10 | insufficient quote for "single decoder" | The §3.2 quote is about sentence length. The absence claims are plausible, but they should be marked as absences, not tied to §3.2. |
| 11 | M03 usual approach: 17 time masking/warping, 4 concatenation, one of which uses it | Claim table 11, 44 | internal inconsistency | The Appendix breakdown of the 4 lists three: one using it, one later study rejecting it, one false hit. The fourth is unaccounted for. |
| 12 | Liu et al. 92.0% / 96.4% / 25.1%; "25.1% without segmentation" | Claim table 13 | insufficient quote | The quote says "zero parameters", and the review reads that as "without segmentation". The quote does not show that zero parameters means no segmentation. |
| 13 | 66.9 points, 73% relative (inference) | Claim table 14 | arithmetic correct | 92.0 − 25.1 = 66.9; 66.9/92.0 = 72.7%. It depends on the reading in row 12. |
| 14 | [later] Satterlee 2025: concatenation misses coarticulation | Claim table 15 | correct | Quote supports it. Correctly labelled [later] and not used as a missed citation. |
| 15 | Lengths up to 19 exceed every recorded item in Table 1; Table 1 has 16 words, two sentences, eight phrases | Claim table 16, 29 | insufficient quote | Only the 16 words are quoted. "19", "two sentences" and "eight phrases" have no quote. The inference is labelled. |
| 16 | M05 counts: 20 studies (13 ledger + 8 full-text-only), 14 sensor-count, 9 gyroscope | Claim table 17, 47 | internal inconsistency | 13 + 8 = 21, not 20, and the overlap is not explained. "Axis comparison 4" counts the target and three records of one study [4], so it is not a count of unique studies. |
| 17 | Choi et al. use acceleration only; Liu et al. add gyroscopes and a head reference | Claim table 18 | correct | Quotes support it. |
| 18 | Target records accel + gyro at 50 Hz on the face (Fig. 1) | Claim table 19 | correct (face placement unquoted) | Minor. |
| 19 | Choi 2026: ten accelerometers, 100 words, 20 participants, plateau at five, 92.30 ± 4.64% | Claim table 20 | correct | Labelled [later]. |
| 20 | Fig. 4(c): gyro axes 92.39–93.39% vs accel 87.62–92.42%; motion handled only by a 2 Hz high-pass | Claim table 22 | correct | Correctly attributed to the authors' own figure. |
| 21 | M12 counts 65/58/44 of 143 | Claim table 23, 52 | correct (published tally) | — |
| 22 | "70:15:15 split without unit or speaker overlap (§2.1.2)" | Claim table 24 | wording wrong | As written, this says the target states there is no speaker overlap. The intended meaning is that it states neither the unit nor whether speakers overlap. |
| 23 | Hong et al. 2026: 85.8%, 26 words, subject-independent 5-fold CV, re-attachment after two weeks | Claim table 25 | no quote | The only location is "Appendix tally" and there is no source quote. |
| 24 | Repositioning cut EMG accuracy to 76.2% [8] | Claim table 27 | correct, incomplete | The baseline before repositioning is not given, so the size of the drop cannot be judged. |
| 25 | 97.17% vs 97.24% / 97.16%; 36 × window vs 30 channels; one laryngectomized participant | Claim table 30, 32, 33 | correct | These are good internal-inconsistency catches. For the first, the bullet does not say what is wrong: the plain mean is 97.20 and 97.17 is neither reported value (inference). |

## Strongest confound

The review compares a single headline number, 97.17%, with Chen et al.'s identical 97.17%. Two confounds sit under that comparison:

- **Different metric.** The target's word ratio does not penalise insertions and is not WER or exact-sentence accuracy.
- **Possible leakage from a sample-level split.** The dataset has 100 repetitions per word, and sentence samples are built by concatenating word recordings. A sample-level 70:15:15 split would let near-identical repetitions, and words reused inside concatenations, fall on both sides of the split.

The review raises both only as questions or side remarks. It should state the second confound plainly as the main reason the headline cannot be compared.

## Chronology and fairness

- [5], [6] and [7] are correctly labelled [later] and are not presented as missed citations.
- [4] (June 2024) is more than 6 months before the target (Feb 2025), so "not cited by the target" is fair.
- No author-reported result is presented as the review's own finding.

## State of the art and absence claims

- **M06 state of the art.** Chen et al. is a closed set of 33 phrases. For silent sentence recognition with wearable sensors, open-vocabulary work is the stronger reference, and earlier continuous silent recognition bears on the §1 novelty claim. All of the following are unverified; values must be checked before use:
  - Gaddy & Klein, EMG silent speech (EMNLP 2020; ACL 2021).
  - Benster et al., LLM-enhanced silent EMG recognition (arXiv 2024; reported WER around 28.8% on the Gaddy silent set).
  - Meltzner et al., sEMG continuous silent speech recognition (J. Neural Eng. 2018; large-vocabulary, roughly 90% word accuracy).
- **IMU sentence prior.** Srivastava et al., earable IMU unvoiced commands and sentences with an LLM ("Unvoiced", 2024; unverified) is a relevant inertial prior that the review does not name.
- **Verdicts.** No verdict is `ahead`, so the `ahead` rules are not triggered. The `not reported` and `not applicable` verdicts are consistent with the text.

## Required fixes (ordered by impact)

1. **Verdict, "with an unstated split".** Change to "with a 70:15:15 split of unstated unit".
2. **M12, "without unit or speaker overlap".** Rewrite as "without stating the split unit or whether speakers overlap". As written, it misstates the paper.
3. **M06 state of the art [2].** Give a quote from Chen et al.'s Methods or Abstract showing that their own model uses CTC; the Sec. I quote may describe prior work. Also quote "four 64-channel arrays".
4. **M06, "The target matches the accuracy".** Replace with "reports the same number on a different metric (word ratio, no insertion penalty)". Also say that 8.1% WER [3] is not comparable to it.
5. **Central confound.** State the sample-level split and concatenation leakage risk as the main caveat on 97.17%, not only as a question to the authors.
6. **Deciding priors for the novelty and state-of-the-art lines.** Either add earlier or open-vocabulary silent sentence recognizers (Meltzner 2018; Gaddy & Klein 2020/2021; Benster 2024; Srivastava 2024, all unverified), or say why a closed-set phrase study is the state of the art.
7. **Liu et al. [4] quotes.** Supply quotes for "93 sentences", "n = 7", "spoken", and for "zero parameters = without segmentation". The 66.9-point / 73% inference rests on the last of these.
8. **M03 Appendix.** Account for the fourth word-concatenation match; the breakdown lists three.
9. **M05 Appendix.** Reconcile 13 + 8 = 21 with "20 unique studies". Restate "axis comparison 4" as 2 unique studies, or explain that it counts records.
10. **Hong et al. [7].** Add a source quote for 85.8%, 26 words, 5-fold subject-independent CV and two-week re-attachment.
11. **Table 1 contents and "lengths up to 19".** Add quotes for the two sentences, the eight phrases and the maximum length in Fig. 3(a).
12. **"Single decoder (§3.2)".** The cited quote does not show this. Mark it as an absence, or cite the right location.
13. **97.17% bullet.** Say explicitly what is wrong: the plain mean of 97.24% and 97.16% is 97.20%, and 97.17% is neither reported value (inference).
14. **Maier-Hein [8].** Give the baseline before repositioning so the 76.2% figure has a reference.
15. **M06 usual approach.** Note that the HMM majority is an all-years upper bound. A recent-years split, if available, would likely show CTC or attention as typical. This one is minor.

## Scores

- Procedure: 7/10. Claim table, ledger tallies and chronology labels are present and mostly consistent. Two Appendix tallies do not add up, and several numbers lack quotes.
- Final text: 6/10. The position is clear and the internal-inconsistency catches are good. Two wording errors misstate the paper (split; speaker overlap), the 97.17% comparison is overstated, and the state of the art for M06 is a closed-set study.
