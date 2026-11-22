# Evaluation: Wireless Silent Speech Interface Using Multi-Channel Textile EMG Sensors Integrated into Headphones

Date: 2026-11-22. Fallback evaluator (claim table only). Input: the compact review (Verdict, component sections, 13-component table, "Where the claims outrun the evidence", references) and its claim table. Sources were not re-opened. Statements marked "evaluator knowledge" draw on general familiarity with the literature and were not re-checked against sources.

## Claim checks

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target uses four dry textile EMG electrodes in a headphone earmuff | Claim row 1 (Abstract; Fig. 1) | correct | Quote gives four graphene/PEDOT:PSS-coated textile electrodes; "dry" and "earmuff" come from the title and figure, not from the quote. |
| 2 | Moving dry electrodes into a worn object follows the necklace of [2] | Claim rows 2, 8; ref. [2] | correct | Quote supports dry electrodes around the neck. [2] (arXiv July 2024, Interspeech Sept 2024) is 7 to 9 months before the target, so treating it as prior work is fair. |
| 3 | No condition compares earmuff with conventional electrodes on the same words; electrode evidence is impedance vs wet electrodes (Sec. II.A.1) | M05 section | insufficient evidence | No claim-table row or quote for Sec. II.A.1. The absence claim is plausible but has no quote. |
| 4 | Authors concede earmuff contact pressure varies more than with adhesive electrodes (Sec. IV) | M05 section | insufficient evidence | No quote in the claim table. |
| 5 | SE-ResNet adaptation to contact quality rests on one example (Fig. 5) | Claim rows 3, 11, 12 | insufficient evidence | Quote supports the channel 1–2 vs 3–4 reading. "One example" cannot be checked from the quote. The point that SE weights act on feature maps rather than electrodes is correctly marked as inference. |
| 6 | 96% on ten words from one random 80/20 sample split pooled over four people | Claim row 4 | correct | All three elements are quoted. "Without seeds, repeated runs or stated speaker separation" is an absence claim consistent with the quotes. |
| 7 | About 200 test samples (inference) | Claim rows 4, 16, 23 | correct (as inference) | 8 off-diagonal errors out of 200 gives 96%, which is consistent. But "100 times among the 4 subjects" is ambiguous (the review's own question 23 says so): with 100 per subject, the test set would be 800. The Verdict states 200 without citing Fig. 4 or giving the alternative. |
| 8 | "Real-time" and "low-power" are not measured | Claim rows 5, 21 | correct | Latency is a FLOPs estimate at an assumed 10 GFLOPs/ms; no power figure is quoted. |
| 9 | M05 usual approach: 16 of 21 mention adhesive or tattoo-like patches; neck 7, ear 7, glasses/mask 5 | Claim rows 6, 26, 27 | insufficient evidence | Ledger tally; the row 26 text is truncated, so the neck/ear/glasses counts cannot be seen. The sub-counts sum to 35, more than 21, and the overlap is not explained. The population was selected for dry, textile or worn electrodes, yet its "usual design" is adhesive patches. This needs one sentence of explanation. |
| 10 | M05 state of the art: [3] reaches 98.7% on five silent phrases and adds leave-one-subject-out tests on 10 subjects | Claim row 7 | wrong / insufficient | The quote gives 98.7% for a configuration "used as the baseline", with a 3.7-s training time. It does not show "five phrases", and it does not show that 98.7% is the subject-independent result. Read as written, the sentence pairs the within-subject figure with the LOSO design. Five classes vs ten is also not flagged. |
| 11 | [2]: 93.9% on 11 words, two speakers, 10 random splits, 95% CI | Claim rows 8, 17 | partly correct | 93.9% and the CI [92.7, 95.0] are quoted, and so are 11 words (from the chance sentence) and the cross-speaker test. "10 random splits" is not in any quote. The quote says 93.9% uses all 13 electrodes, against 4 in the target; the review does not mention this. The speech mode in [2] (silent vs vocalized) is not stated. |
| 12 | M06 usual approach: 355 classifiers, "other" 82, CNN 35; a 1D residual CNN is common practice | Claim rows 9, 31, 32 | wrong (last clause) | The counts match the Appendix rows, but the Appendix gives 360 pattern-matched studies against 355 in the text, and the difference is not explained. "A 1D residual CNN is common practice" has no support: CNNs are 35 of 355 (~10%) and residual nets are not counted. |
| 13 | M06 state of the art: [4] 99.6% on 50 words on day one, intracortical | Claim row 10; ref. [4] | correct number, wrong category | The value and year match evaluator knowledge of Card et al. 2024 (NEJM 391:609–618). But that figure is word accuracy from sentence decoding with a language model and a 50-word vocabulary, not closed-set isolated-word classification, the slot the review defines. There is no source quote (only "ledger tally"). |
| 14 | SE-ResNet vs ResNet gap (Fig. 6) comes from one split without spread | Claim row 13 | correct | Consistent with the single-split quotes. |
| 15 | M12 usual approach: speaker-disjoint 65 of 143; random/k-fold 58; session/day 44 | Claim rows 14, 36–38 | insufficient evidence for "usual" | 65 of 143 is under half, and the pattern counts overlap. These counts do not show a dominant protocol, so "usual" is stronger than the counts allow. |
| 16 | M12 state of the art: [5] 85.8% on 26 words, subject-independent folds, re-test after re-attachment | Claim row 15 | insufficient evidence | No source quote. [5] is a strain-sensor interface; it fits "wearable-sensor" but is not EMG. |
| 17 | Fig. 4 rates move in 5% steps; off-diagonal cells sum to eight errors | Claim row 16 | correct (as inference) | Internally consistent with 96% over 200. |
| 18 | [2] reports chance ~9% and a cross-speaker one-shot test; the target reports neither; chance here is 10% | Claim row 17 | correct | Quotes support both features of [2]. |
| 19 | Superiority over single-channel and non-adaptive baselines rests on one split with unstated baseline settings | Claim row 18 | correct | |
| 20 | Removing the 20–450 Hz filter: 96% to 76.5%, 19.5 points, 20.3% relative | Claim row 19 | partly correct | The arithmetic is correct (19.5/96 = 20.3%). The quote reads "ResNet drops from 96% to 76.5%" and does not name the filter condition; check whether the model is the SE-ResNet or the plain ResNet. |
| 21 | Single-channel drop "nearly 40%" does not say points or relative | Claim row 20 | correct | |
| 22 | Decoding on external PC/phone via Wi-Fi; FLOPs-based latency at 10 GFLOPs/ms | Claim row 21 | correct | |
| 23 | Authors name small vocabulary, small participant pool and silver-paste adhesion as limits (Sec. IV) | Limits bullet | insufficient evidence | No quote. Correctly attributed to the authors, not presented as the review's own finding. |
| 24 | M04 usual "offline decoding of produced speech", verdict standard | Component table | inconsistent | The target is silent articulation. If "produced speech" means voiced speech, "standard" does not follow. |
| 25 | M09 and M10 usual-approach counts (slot-filled 82) | Component table | insufficient evidence | Identical to the M06 "other" count of 82. Check that they were not copied. |

Fairness: [3] and [5] are labelled [later] and used only as state of the art, not as missed citations. [2] is outside the 6-month window. No author-reported finding is presented as the review's own.

Strongest confound for the central claim: the 96% comes from a sample-level random split pooled across four subjects. Repetitions from the same subject and session sit on both sides of the split, which inflates accuracy relative to [2]'s cross-speaker test and [5]'s subject-independent folds. The review handles this (M12, Verdict). It does not handle the comparator differences: [2] has 13 electrodes against 4, and [3] has 5 classes against 10.

Novelty and absence: there is no "first / only" sentence. The M05 "standard" verdict names only [2] as the deciding prior, although the Appendix counts 7 ear-worn studies. Evaluator knowledge: worn-object facial and jaw EMG for silent speech predates [2]. One example is the AlterEgo headset (Kapur et al., ACM IUI 2018, electrodes held by a worn frame). Naming an ear-worn EMG prior from the 7 counted would make the verdict hold on its own.

Within-modality comparator (evaluator knowledge, medium confidence): tattoo-like EMG silent speech with machine learning, Wang et al., npj Flexible Electronics 2021, reports about 92.6% on 110 words. This is a closer EMG closed-set reference point than [4].

## Required fixes (ordered by impact)

1. M06 state of the art: [4]'s 99.6% is word accuracy from language-model-assisted sentence decoding with a 50-word vocabulary, not a closed-set word classifier. State the metric and condition, add a source quote, and add a surface-EMG closed-set comparator, so the slot is not compared only against an intracortical, different-task figure.
2. M05 state of the art: separate [3]'s 98.7% (the baseline configuration) from its leave-one-subject-out result and give the LOSO accuracy. Add a quote for "five phrases" and note five classes vs ten.
3. [2] comparison (M05, M12): add a quote for "10 random splits" and "two speakers". State that 93.9% uses 13 electrodes (the target uses 4) and state [2]'s speech mode, so the reader sees how unlike the two setups are.
4. M05 verdict: name at least one of the 7 ear-worn EMG studies, and an earlier worn-object system (e.g., Kapur et al., IUI 2018), as deciding priors. Right now "standard" rests on [2] alone.
5. M06 usual approach: delete "a 1D residual CNN is common practice" or support it with a count. Reconcile 355 (text) with 360 (Appendix).
6. M12 usual approach and table row: 65 of 143 is not a majority and the counts overlap. Say that no split protocol dominates instead of calling speaker-disjoint "usual".
7. Add source quotes for the uncited positions: impedance vs wet electrodes (Sec. II.A.1), the contact-pressure concession and the stated limits (Sec. IV), "one example" (Fig. 5), and the [5] figures.
8. Filter ablation: the quote names "ResNet" and no filter condition. Confirm the model and the condition behind 96% → 76.5% before attributing the drop to filter removal.
9. Verdict: cite Fig. 4 for the ~200 test-sample estimate and give the alternative of 800 if "100 times" is per subject, matching the review's own question.
10. M05 usual approach: explain why a population selected for dry, textile or worn electrodes has adhesive patches as its usual design, and why the sub-counts (7 + 7 + 5 + 16) exceed 21.
11. Component table M04: reconcile "offline decoding of produced speech" with silent articulation and the "standard" verdict.
12. Component table M09/M10 (82) and M02 (31): verify that these counts are not copied from M06's "other" (82) or mis-tallied.
13. M13 verdict: the text cites a FLOPs-based latency estimate, so write "measured latency and power not reported" instead of a bare "not reported".

## Scores

- Procedure: 6/10. The target claims are well quoted and the inferences are marked, but several comparator figures and positions have no source quote, and two state-of-the-art entries mismatch their slot or condition.
- Final text: 6/10. The position is clear and mostly backed, but the M06 state of the art, the M05 comparator pairing and the "usual approach" wording for M06 and M12 overstate the evidence.

The review's handling of the target's evaluation design (single pooled random split, the inferred test size, missing chance level and spread) is careful and correctly marked as inference.
