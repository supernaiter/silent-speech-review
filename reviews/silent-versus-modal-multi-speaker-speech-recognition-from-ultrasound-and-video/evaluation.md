# Evaluation: Silent versus modal multi-speaker speech recognition from ultrasound and video

Date: 2026-11-20. Independent evaluation over the compact review and its claim table only; sources were not re-opened. "Insufficient evidence" means the claim-table quote does not carry the claim as written, not that the claim is wrong.

## 1. Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target trains on modal speech, tests on silent, 82 speakers; applies fMLLR and unsupervised adaptation | Claim rows 1, 19 (Sec. 3.1, Abstract) | correct | 82 = TaL80 (81) + TaL1; consistent with the 81 speakers in Fig. 5. |
| 2 | Silent WER 76% above modal on TaL80 | Row 3 (Table 1) | correct, but column-dependent | 70.21/39.79 = 1.76 uses the fMLLR column. Baseline column gives 77.79/39.34 = 1.98; fMLLR+adapt gives 69.84/41.37 = 1.69. The review does not say which column it picked or why. |
| 3 | Later system on same corpus lowers both errors and leaves gap at 75% [3] | Row 3, 7, 10 ([3] Table 2) | insufficient evidence | Column headers of [3] Table 2 are not quoted; reading 26.87 as modal and 47.15 as silent is an assumption. Same-speaker/same-split comparability with the target is not shown. Absolute gap falls from 30.42 to 20.28 points (a third), which the review does not state. |
| 4 | Adaptation gains 0.37 to 3.36 points, single runs, no test | Rows 4, 20 (Table 1) | correct | Deltas check: 77.79-75.83 = 1.96, 70.21-69.84 = 0.37, 52.64-49.28 = 3.36, 38.42-37.94 = 0.48. |
| 5 | Missed caveat in Table 1 | Row 3, 10 (modal row) | wrong by omission | Same table shows unsupervised adaptation raises modal WER (+2.42, +1.58) and fMLLR raises modal WER (39.34 to 39.79). This is the authors' own data and bears directly on the adaptation claim. |
| 6 | Every test speaker is in training; speaker-independent remark unsupported | Row 19 (Sec. 3.1, Sec. 4) | correct | |
| 7 | Bigram LM on a prompt superset | Row 21 (Sec. 3.3) | correct | Affects both modes, so it inflates absolute WERs more than the ratio; worth one clause. |
| 8 | "Do not directly correlate": r = -0.009, r = -0.1682, no intervals | Row 22 (Sec. 4, Fig. 5) | correct | |
| 9 | [3] relates trajectory distance to WER (R² 0.060), "as predicted" by the authors' missed-target suggestion | Row 22 ([3] Sec. 5.1) | position too strong | R² 0.060 (r about 0.24) is itself weak, not far from the target's r = -0.17 (R² 0.03). It does not confirm the prediction; it is a weak association in a later paper. |
| 10 | M04 usual approach: overt-trained decoder applied to silent speech, 23 confirmed (7 prior) | Row 5 | plausible | Matches the typical design. Count is a ledger tally; not audited. |
| 11 | M04 state of the art: 47.15% silent WER on TaL with modal-only training [3] | Row 7 | insufficient evidence | "Modal-only training" is not in the quote; column semantics unquoted. Scope is TaL only, while the usual-approach line spans neural, EMG, video and ultrasound. |
| 12 | Florescu et al. [2]: 4 speakers, isolated words, 75.3% to 45.7% correct; 39% relative loss | Row 8 | partly correct | 75.3% and 4 speakers quoted; 45.7% given as "Table 2 value" without a quote; "isolated words" and "word templates" unquoted. Calculation 29.6/75.3 = 39% correct. |
| 13 | Target cites [2] for the degradation (Sec. 3.3) | Row 9 | insufficient evidence | Quote cites the target's own "[7]"; that [7] = Florescu et al. 2010 is not shown. |
| 14 | M03 usual approach: fMLLR/SAT, 27 of 48 (pattern match), as in [4] | Row 11 | plausible | Typical for HMM-based non-acoustic recognizers of that era. |
| 15 | M03 state of the art: fMLLR lowered silent WER by up to 15.45% [3] | Row 12 | insufficient evidence; internal tension | Quote has no "up to" and does not say relative or absolute. If [3] Table 2 columns were no-fMLLR / fMLLR, 62.60 to 47.15 would be a 24.7% relative drop, not 15.45%; so either the columns or the 15.45% reading is wrong. Resolve. |
| 16 | fMLLR: 77.79 to 70.21, 9.7% relative; unsupervised adds 0.37 | Row 13 | correct (arithmetic) | Column identity (baseline vs fMLLR) is inferred, not quoted. |
| 17 | Wand and Schultz [5]: lattice-confidence weighting, disjoint adaptation sentences, paired t-test, 34.9% to 30.2% | Row 14 | partly correct | WER and t-test quoted. Confidence weighting and disjointness from test are not in the quotes ("40 SPEC sentences of the target session" alone does not show disjointness). |
| 18 | Target adapts all parameters on each test set and scores that set | Row 15 | correct | "Scores that same set" is a reasonable reading of Sec. 3.3. |
| 19 | Wang and Hahm [4]: leave-one-subject-out on 5 silent speakers | Row 16 | partly correct | Leave-one-subject-out and five speakers quoted; "silent" is not in the quote. |
| 20 | M06 usual approach: GMM-HMM 15 of 38 | Row 17 | plausible but dated | Tally spans all years; current ultrasound recognizers are mostly DNN-HMM or end-to-end. Say the count is cumulative. |
| 21 | M06 state of the art: 6.17% WER on single-speaker SSC, 2019 [6] | Row 18 | correct as quoted; ranking unverified | Earlier DNN result on the same benchmark (Ji et al., 2018, about 6.4% WER) is consistent; whether a later result beats 6.17% is not shown. |
| 22 | "Better features cut both errors without narrowing the gap: the problem lies in the speaking mode, not the front end" | Rows 3, 10 | position too strong | Two systems, one ratio each, comparability not shown, and the absolute gap did narrow. The causal conclusion goes beyond the evidence. |
| 23 | Fairness: [3] (2023) labelled [later] and used only as later state of the art, not as a missed citation | References, M03/M04 | correct | |
| 24 | Absence/novelty: modal-to-silent degradation "dates from 2010 [2]" | Verdict, M04 | incomplete | For ultrasound, fine. Since the M04 slot spans modalities, the cross-modal deciding prior should be named: Janke, Wand, Schultz, "Impact of lack of acoustic feedback in EMG-based silent speech recognition," Interspeech 2010 (audible-trained vs silent-tested EMG mismatch). |
| 25 | Verdicts: all `standard` or `not applicable` | 13-component table | correct | No `ahead` verdict, so the ahead rules are not triggered. Claim table rows 25-38 refer to a "Questions for the authors" section and an Appendix that the compact review does not contain. |

## 2. Required fixes (ordered by impact)

1. Gap/ratio claim (Verdict, M04): state that the absolute gap narrows from 30.42 to 20.28 points while the ratio stays near 1.75; give the ratio for every Table 1 column (1.98 baseline, 1.76 fMLLR, 1.69 fMLLR+adapt) and the [3] baseline (62.60/33.64 = 1.86); show [3] uses the same speakers/splits or say it does not; replace "the problem lies in the speaking mode, not the front end" with an inference from two systems.
2. [3] numbers (M03, M04, table): quote the column headers of [3] Table 2 and the passage showing modal-only training; reconcile the 15.45% fMLLR figure with 62.60 to 47.15 (24.7% relative); drop "up to" unless the source says it and state whether 15.45% is relative.
3. Add the missed caveat from Table 1: unsupervised adaptation raises modal WER (+2.42, +1.58) and fMLLR raises modal WER (39.34 to 39.79). It strengthens the adaptation critique and should appear in "Where the claims outrun the evidence".
4. Correlation bullet: present R² 0.060 in [3] as a weak association of similar size to the target's r = -0.17, not as confirmation of the authors' prediction.
5. M04 prior: name Janke, Wand, Schultz (Interspeech 2010) as the cross-modal deciding prior for audible-trained, silent-tested recognition, alongside Florescu et al.
6. Florescu et al. [2]: quote the 45.7% silent value and the isolated-word/template design; show that the target's reference [7] is Florescu et al. 2010.
7. Wand and Schultz [5] and Wang and Hahm [4]: quote the confidence weighting and test-disjoint adaptation data for [5], and the silent condition for [4], or remove those attributes.
8. M06: say the GMM-HMM count is cumulative across years and that DNN-HMM or end-to-end is the current typical design; confirm no later SSC result beats 6.17% (Ji et al. 2018 is earlier and worse).
9. Claim table: remove or restore the rows that cite the missing "Questions for the authors" section and Appendix so that table and text match.

## 3. Scores

- Procedure: 7/10. Claims are traced to locations and arithmetic is right; the weak points are unquoted column headers in the main comparator and attributes of priors without quotes.
- Final text: 6/10. Clear position and fair handling of later work, but the central "gap does not narrow" point leans on one column choice and a relative measure, and a caveat visible in the target's own Table 1 is missing.
