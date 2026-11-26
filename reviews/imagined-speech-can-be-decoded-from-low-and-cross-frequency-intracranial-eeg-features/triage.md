# Triage of the evaluation (round 1, 2026-11-26)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | "Comparable" occurs only for spatial power patterns (Results); the authors' wording is "equally good using e.g., theta or beta power" (Results) and "could equally well be decoded" (Introduction) (notes e1, e2). | Verdict sentence 5; claims-outrun bullet 1 |
| 2 | applied | Target reference list includes Pei 2011; Ikeda 2014 and Leuthardt 2011 absent. The Discussion sentence refers to studies that used only BHA (notes q5). | M06 evidence paragraph; claims-outrun bullet on omitted priors removed; Verdict |
| 3 | applied | Preprint Fig. 7 (p. 12) plots one dot per participant x representation x band and counts above-chance dots over bands; released code tests 8 participants x 3 representations x 6 CFC combinations (covert_MI/svmClassifier.py:20,30,39; notes z2-z4). Counts are tests: CFC 12/144 (expected 7.2 at 5%, P about 0.06), power 10 over at least 72 (P about 0.003) (inference). | Verdict sentence 3; M06 verdict paragraph; claims-outrun bullet 2 |
| 4 | applied | Kept "standard" with protocol reasons: uncorrected per-participant thresholds over 144 tests (Methods, Decoding; q3), pass rate near nominal and below power, no CFC-versus-power test, pre-fold z-scoring of CFC features only (verified in code, z1, z7). Equal-medians argument removed. | M06 verdict paragraph; slots M06 note |
| 5 | applied | Martin 2014 covert decoding used a model trained on overt data (notes c26). Recount: 3 within-participant covert splits, 1 overt-to-covert transfer, 1 online test. | M12 usual approach; Appendix; audit M12; slots M12 matched 3 |
| 6 | applied | Inclusion rule now excludes attempted speech decoded from unit firing (Guenther 2009, Brumberg 2011); counts unchanged. | Appendix M06/M12; audits |
| 7 | applied | Kunz T15 decoder retrained online during evaluation (notes u3); T12 24%, T16 33%. | M12 state of the art; slots M12 sota |
| 8 | applied | Released code fetched (Zenodo 10.5281/zenodo.5702872, zip sha256 b9998f7c...); z-scoring at covert_MI/svmClassifier.py:34, absent from the power script; n_surr = 200 at clustering_fisher_grouping.py:54 against 1000 permutations in the Methods for feature distances; 200 MI shuffles are the text's own (e3). Hard-coded classes dropped from the body; effect of z-scoring marked (inference). | M06 verdict; M12 paragraph; claims-outrun bullet 4; Questions |
| 9 | applied | Cutoff stated as first public before 2020-07; no 2020 candidate in the population. | M06 usual approach; Appendix |
| 10 | applied | Binary decoding excluded study 3 (notes e5). | M06 usual approach |
| 11 | applied | Ikeda values are best single electrodes with per-electrode binomial p-values (notes k8). | M06 evidence paragraph |
| 12 | applied | Livezey 2019 named as nearest coupling work (overt, coupling analysed beside the classifier, c19); novelty scoped to imagined/covert decoders. | M06 novelty paragraph |
| 13 | applied | Process wording ("all wiki papers") removed; absence stated with Appendix reference. | M06 novelty paragraph |
| 14 | applied | 4.8 vs 1.2 ratio dropped; Zhao median over all 9 participants; beta1 input credited as supporting the paper's direction. Trial counts not added (no notes entry). | M06 state of the art |
| 15 | applied | Authors' concession on binary classification (notes e4) credited in the Verdict. | Verdict sentence 5 |
| 16 | applied | "Low-frequency power has precedent (2 of 5)". | Verdict sentence 2; slots M06 note |
| 17 | applied | Claim-table rows now cite e1, e2, t42, z2-z4, q3 instead of the derivation q1; denominators marked (inference). | claims.md |
