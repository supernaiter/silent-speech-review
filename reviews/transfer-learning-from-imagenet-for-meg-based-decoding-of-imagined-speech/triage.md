# Triage: Transfer Learning from ImageNet for MEG-Based Decoding of Imagined Speech

Date: 2026-11-22. Round 1 of the independent evaluation (fallback evaluator, claim table only; 15 required fixes). Each fix was checked against `notes.json`, the audits and the source passages it concerns (target text, Dash et al. 2020, Panachakel and Ganesan 2021, Orpella et al. 2022). Counts: 9 correct, 4 partly correct, 2 wrong, 0 unverifiable; 13 applied.

| # | Verdict (applied / rejected / unverified) | Evidence | Where applied |
|---|---|---|---|
| 1 | Applied (partly correct) | The range 5.7 to 8.9 is right: 8.9 is imagery vs silent reading pooled, 81.0 to 72.1 (Table 4), not imagery vs silence (8.8). The pretrained baseline rows had no quote. | Verdict sentence now says "across the three tasks and both splits of Table 4 (inference)"; notes t66, t67 (Table 4 baseline rows); claim table rows 3, 10 |
| 2 | Applied (partly correct) | 93.24% is in d4: the mosaic network (SST-CNN) in the preparation (imagination) stage, so the value stands. "Random split" has no support; the split is 70/15/15 (d5) and subject-dependent (new d10, Discussion). | M03 state of the art: "93.24% in the imagination stage, within subject on a 70/15/15 split"; notes d10; claim row 8 |
| 3 | Applied (correct) | Table 4 caption: "Balanced accuracy (mean ± 95% CI)"; 90.4 ± 2.5 and 87.4 ± 2.7 overlap. The claim stands; the quote was missing. | notes t65; claim row 15 |
| 4 | Applied (correct) | 3.9 (90.4 to 86.5) and 3.0 (90.4 to 87.4) are pooled; 3.5 holds pooled (60.6 to 57.1) and held-out (51.7 to 48.2). | M06 paragraph and "Where the claims" bullet now name the split |
| 5 | Rejected (wrong) | d4 gives both networks: mosaic (SST-CNN) 90.38 / 93.24 / 96.65 vs per-sensor (ST-CNN) 86.83 / 91.71 / 93.56 across perception, preparation and production, so the mosaic is higher in each stage. The evaluator read only the ST-CNN half. "Every stage" was narrowed to "all three task stages" so it does not include the pre-stimulus stage. | Wording only (M06 state of the art) |
| 6 | Applied (correct) | Orpella et al. Methods: "electromyographic (EMG) data from the upper lip and jaw (Fig 1) was also acquired". | notes o6; claim rows 5, 20, 26 |
| 7 | Applied (correct) | Dash et al. Results: accuracy in "all the four stages (pre-stimuli, perception, preparation/imagination, articulation)" was above the 30% chance level. | notes d9; claim row 20 |
| 8 | Applied (correct) | The target cites Dash et al. ([10]) once, in Sec. 1: "... typed characters [9], and imagined sentences [10] from MEG". | notes t63; claim rows 2, 21 |
| 9 | Applied (correct) | Dash et al. Abstract: "Two machine learning algorithms were used. One was an artificial neural network (ANN) with statistical features as the baseline approach." This supports "only" and "statistical features"; text kept. | notes d11; claim row 11 |
| 10 | Applied (correct) | Sec. 2.4: "the 248-channel MEG scalograms were concatenated into a tensor of shape (248, F, T)" followed by the learnable 1×1 projection. | notes t64; claim rows 1, 13 (t15 replaced) |
| 11 | Applied (partly correct) | The 400 ms quote was missing (Sec. 2.1, "at 400 ms per syllable"). The second half is wrong: "imagery-locked intervals" is verbatim in Sec. 5 (Conclusion), and t4 carries that location. | notes t68; claim row 24 |
| 12 | Applied (correct) | Panachakel and Ganesan Sec. IV.D: "A ResNet50 [35] based deep neural network model, pre-trained on ImageNet [56], is used as the base model". | notes p4; claim row 2 |
| 13 | Applied (correct) | Rows 6 and 12 carried unrelated target quotes for ledger counts; row 23 repeated t43 / t44. | Claim table: rows 6 and 12 marked tally; t44 dropped from row 23; t28 kept once in row 9 |
| 14 | Rejected (wrong) | SAP uses "stratified 10-fold cross-validation grouped by trial to avoid within-trial leakage" (Sec. 2.5, t45), so overlapping epochs of one trial cannot sit in both training and test. Participant overlap in SAP is already a question to the authors. | None |
| 15 | Applied (correct) | M13 matches the usual approach (laboratory, slot-filled 6,721), which the rules call standard; the M06 cell printed the count twice. | slots M06 field "Raw time-series CNN"; M13 verdict standard; extra.json verdicts |

Reruns after the changes: render_review, build_refs, fill_row (then fix_row.py, unchanged), check_review 0 FAIL / 0 WARN (body 6,609 characters), verify_quotes 79 found / 0 missing, audit_tally passes for all three audits; the reused M12 tally equals the published table. Claim table regenerated and refilled (37 rows); compact text regenerated.

Open after this round: the evaluator could not confirm that no later ImageNet-pretrained MEG imagined-speech work exists; none appears in the M03 or M06 ledger tallies. Recorded in `verification_status.evaluation`.
