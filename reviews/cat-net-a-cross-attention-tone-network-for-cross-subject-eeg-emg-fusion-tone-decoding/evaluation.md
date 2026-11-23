# Evaluation: CAT-Net (arXiv:2511.10935)

Date: 2026-11-23. Independent evaluation, claim table and review text only (no sources re-read). Outside knowledge that could not be located is marked unverified.

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper changes M06, M05, M03 for four-class Mandarin tone decoding | Claim 1; t7, t12, t52 | correct | Quotes support all three components. |
| 2 | Every ablated network falls below DeepConvNet on concatenated EEG+EMG | Claims 2, 10; t66-t68, t60, t21 | correct (numbers); insufficient evidence (condition) | 77.63, 78.42, 76.60, 76.46 all < 86.56. No quote shows Table 6 is the silent-condition five-fold setting with the same metric as Table 3, nor that its column is precision. "One five-fold ablation" is not quoted. |
| 3 | No result separates EEG from EMG; paper does not show EEG carries tone information | Claims 3, 9; t65; t68; t32 | insufficient evidence / possible contradiction | t68 lists "w/o fusionEMG" (76.60) and "w/o fusionEEG" (76.46) with one fewer check mark: these may be single-modality runs. Appendix D SHAP (t32) states EEG contributes more than EMG for Tone 2 silent. The review quotes both and does not reconcile them. |
| 4 | Discriminator lifts mean 84.69% to 85.10% | Claims 4, 20; t27, t22 | correct | Arithmetic 0.41/84.69 = 0.5% correct. |
| 5 | LOSO mean of 85.10% stands | Claim 5; t22, t23, t44 | insufficient evidence | Table 4 sits under "Cross-Subject Calibration"; Table C2 gives CATNet 83.27% cross-subject. The review does not say which is pure leave-one-subject-out or whether calibration uses test-subject data. Its own questions (channel ranking data, early stopping) bear on whether the figure stands. |
| 6 | Authors call the DD gain "slight" | Claim 20; t30 | insufficient quote | t30 ("DD may yield greater benefits") does not contain "slight". |
| 7 | "single runs" / "from one run" | Claims 11, 20 | insufficient evidence | No quote states run or seed count; the review itself asks how many seeds. |
| 8 | M06 usual approach: EMG as EEG artifact (8 of 30) | Claim 6, 31; Appendix M06 | correct as tally; wrong as usual fusion form | The Appendix inclusion rule says artifact-only studies are "counted separately", yet the usual design is drawn from them. Among fused decoders the tie is concatenation 4 / late fusion 4. |
| 9 | M06 SOTA: [2] 95.3%, 64 silent words, session split | Claim 7; c20, c44, c21 | insufficient quote | Quotes give 95.3% for healthy controls and a 64-word vocabulary separately; no quote ties them, nor supports "pooled EEG+EMG pretraining". Concurrent label right (June 2025 arXiv). |
| 10 | [3]: sEMG 10.52% CER, EEG 38.85%, concatenation 13.14% | Claim 8; c2 | correct (values); insufficient quote (unit) | Column header showing CER not quoted. |
| 11 | Gain 1.52 points, 1.8% relative | Claim 11 | correct | 1.52/86.56 = 1.76%. |
| 12 | [4]: anatomical 6-electrode subset 80.1% on four imagined tones | Claim 13; c5, c43 | insufficient evidence | Row is "Combined audio-visual" cue condition, omitted in the review. Header quote names two columns, the row has four values; which column is "All 6 electrodes" is not shown. "Anatomical" unquoted. |
| 13 | [5]: 50% of 64 channels removable, positions differ | Claim 14; c30, c42, c31 | correct | Concurrent label right (Jul 2025). |
| 14 | Full 88.45% to 20 channels costs 0.37; 5 channels 86.92%, EMG always present | Claim 15; t70, t13, t69 | correct (numbers); insufficient quote (EMG present) | t4 (sampling rate) does not support EMG presence or 64 channels. Missed: Table 1 20-channel row reads 87.29 in column 3, Table 3 CATNet row 87.27, same average 88.08: an internal inconsistency in the target. |
| 15 | 1.53-point spread "fits EMG carrying the decision" | Claim 16; t32 | judgment beyond evidence | The quoted SHAP passage (t32) partly runs against this; the review cites it but does not mention it. |
| 16 | 69% of channels removed; one pooled subset | Claim 17 | correct arithmetic; insufficient quote | 44/64 = 68.75%. 64-channel montage and pooled ranking not quoted. |
| 17 | M03 usual approach 6 of 18, as in [6] | Claim 18 | correct | Quote from [6] supports gradient-reversal design. |
| 18 | M03 SOTA: [7] 26.30% to 31.95% PER, 4 seeds | Claim 19; c14, c40 | correct (numbers); wrong label | arXiv 2603 (March 2026) is after the target (Nov 2025): label should be [later], not [concurrent]. Not treated as prior. |
| 19 | M12 SOTA: [8] 82.4%, 8 words, LOSO over 4 participants | Claim 22; c8, c41, c9 | insufficient quote | LOSO protocol not quoted. A four-participant pilot on EEG-fMRI data is a weak "state of the art" anchor; stronger cross-subject EEG speech results may exist (unverified). |
| 20 | Per-subject range 53.33-95.00% | Claim 23; t22 | correct | |
| 21 | Ablations lose 9.66-11.62 points | Claim 24 | correct | 88.08-78.42 and 88.08-76.46 verified; same caveat on Table 6 condition as row 2. |
| 22 | Appendix C "highest on all 10 subjects" contradicted on S10 (GAT) and S9 (DeepConvNet, Table 4) | Claim 26; t26, t23, t63 | correct (S10); insufficient quote (S9) | S10: 89.17 < 90.00 verified. No DeepConvNet Table 4 row quoted. |
| 23 | 88.08% is accuracy in text, average precision in Table 3; "significant margin" untested | Claim 27; t14, t71, t44 | correct (metric); insufficient quote ("significant margin") | t44 does not contain the phrase. |
| 24 | Novelty: cross-attention fusion new among EEG-EMG decoders | Claim 2; Appendix M06 | insufficient evidence | 0 of 30 by pattern match; deciding priors ([3], [2]) not named in the sentence; the audit notes the target is outside the 30. No earlier speech EEG-EMG cross-attention decoder known to this evaluator (unverified). |
| 25 | Verdicts: M06, M05, M03, M12 all `standard` | Component sections | correct per rules, but under-explained for M06 | A design called "new" receiving `standard` needs one clause saying why (effect not separated, not repeated). |

Central confound: baseline strength and comparison setting. The 1.52-point margin over a concatenation DeepConvNet is the real test of the fusion form; the review handles this well. Not handled: whether the cross-subject figure (85.10% vs 83.27%, "calibration") is calibrated transfer, and whether channel ranking used held-out subjects.

Fairness: no later work is treated as prior; the "slight" gain is credited to the authors. No issue beyond the [7] label.

## Required fixes (ordered by impact)

1. Reconcile "No result separates EEG from EMG" (Verdict; M06; claim 9) with Table 6 rows "w/o fusionEMG" / "w/o fusionEEG" (t68) and the Appendix D SHAP statement (t32). Either show these are not single-modality runs or revise the claim.
2. Qualify "The leave-one-subject-out mean of 85.10% stands": address Table 4's "Cross-Subject Calibration" heading, Table C2's 83.27% CATNet cross-subject mean, and the open questions on channel-ranking data and early stopping.
3. Replace "from one run" / "in single runs" / "one five-fold ablation" with "seed count not stated" unless a quote supports single runs.
4. Fix the M06 usual approach (text and table row): artifact-only studies are excluded from fusion by the Appendix inclusion rule; the usual fusion form is concatenation or late fusion (4 each).
5. In the M06 novelty sentence, name the deciding priors ([3], [2]) and state why a new design still gets `standard`.
6. Drop or qualify "fits EMG carrying the decision" (M05) given t32.
7. Relabel [7] as [later] (March 2026, after the Nov 2025 target).
8. Add supporting quotes or soften: "slight" (claim 20), "significant margin" (claim 27), Table 4 DeepConvNet S9 row (claim 26), 64-channel montage and EMG present in Table 1 (claims 15, 17, 25), CER unit for [3], LOSO protocol for [8], and the 95.3% / 64-word / pooled-pretraining link for [2].
9. [4]: add the "combined audio-visual" cue condition, confirm the column for 80.1%, and quote or drop "anatomical".
10. Confirm Table 6 uses the same condition and metric (silent, five-fold, average precision) before subtracting from 88.08 and comparing with 86.56; label the 77.63 column correctly.
11. Add the missed target inconsistency: Table 1 (20 channels) 87.29 vs Table 3 (CATNet) 87.27 in the same column, same average.
12. M12 state of the art: justify [8] (four-participant pilot, EEG-fMRI data) as the anchor or label it as the nearest comparable result.

## Scores

- Procedure: 7/10
- Final text: 6/10

Arithmetic is clean throughout, and the concatenation-baseline critique of the ablation is the strongest point of the review.
