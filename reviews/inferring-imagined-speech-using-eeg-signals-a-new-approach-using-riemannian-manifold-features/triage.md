# Triage of the independent evaluation

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| H1 | applied | M06 inclusion rule excludes motor-imagery-only studies; within the setting the design is absent in 0 of 7 priors and repeated over 6–8 subjects, so "standard" now rests on at-chance baselines, uncorrected tests and accuracy-based tuning (Table 3a, Table 4 caption, §5.2). Motor-imagery origin kept as context only (§6.2). | Verdict; M06 section; slots M06 note |
| H2 | applied | Table 3a per-subject means: log-variance+LDA 29.3–40.3%, DaSalla 31.0–41.7% vs 33% chance; §6.1 "even below the chance level" and the instruction-set explanation. | M06 section; Verdict |
| H3 | applied | Target §5.2 splits by trials (270/30, 160/40); Tates §II-D uses its own 1.4 s / 0.1 s stride segments; Tates grouped short-versus-long ~0.75 vs target 73.3%; Tates §IV reads the post-imagery drop as confirming task-related decoding. Epoch-leakage concern removed; first Question rewritten. | Verdict; M12 section; Questions |
| H4 | applied | Panachakel & Ganesan 2021 (wiki doi-10.1109-access.2021.3116196): vowels κ 0.78 ± 0.06, minimum 79.7%, per-subject 10-fold CV, training-only augmentation. Singh & Gumaste: [900, 60, 256] per subject, stratified 10-fold; own baselines 49.2% and 49.3%. | M06 state of the art; slots; audit state_of_the_art; refs |
| M1 | applied | Body-text check of the priors: hand-crafted features + shallow classifier 6 of 7; SVM/LDA/ELM 4 of 7; CSP+CRNN 1. matched=6, n=7. | M06 usual approach; slots; audit; Appendix |
| M2 | applied (partly) | Torres-García 2012 (scalp EEG, unspoken words, chance stated) added; Suppes 1997 included (EEG and MEG, internal speech condition, test vs chance); population now 7 prior. DaSalla is no longer named in the text except as a Table 3 comparator label of the target; it is not in the wiki, so no reference entry was added. Recall wording fixed. | Appendix; audits; Verdict |
| M3 | applied | 12 Tangent+RVM p-values; Bonferroni α = 0.05/12: 5 survive (inference); Table 4 caption "at the 5% significance level". | M06 section |
| M4 | applied | §6.1 "quite equivalent", p = 0.16. | M06 section |
| M5 | applied | Margin arithmetic removed; κ gap untested, subject sets, window 4.5 vs 4 s (§5.2), class count. | Claims list |
| M6 | applied | §4.1 states the visual-cue-only window and its reason. | Verdict; slots M04 note |
| M7 | applied | §5.2 choices driven by observed accuracy ("did not provide any improvement"; "highest accuracy ... 12–14 CSP components"); Yoshimura 2016 nested CV is 1 of 7, fewer than 3 for behind. M03 → standard. | slots M03; Claims list; Field-needs |
| M8 | applied, verdict changed | Body-text check: tests against chance in Suppes 1997 (significance), Deng 2010 (binomial, read), Yoshimura 2016 (significance); stated only in 3; none in 1. 3 earlier comparable papers meet a condition the target does not, best (Deng) read and named → M12 behind (yardstick: best comparable work). | M12 section; slots M12; audit; Appendix |
| M9 | applied | Jahangiri 96.4% is not the top ledger value; the sentence and reference were dropped for length. | M12 section |
| L1 | applied | Pairwise pooled medians; only short versus long clearly above chance under grouped CV (Tates Sec. III-A). | M12 state of the art |
| L2 | applied | The 0.609 single-feature sentence was removed; the muscle-tension link is kept with the EMG point. | Claims list |
| L3 | applied | "20 splits" claim removed; comparators described as best grid means only. | Claims list |
| L4 | applied | "single-fold maxima within one subject (Table 3)". | Claims list |
| L5 | applied (no change of date) | Paper states Published 1 December 2017, accepted 26 July 2017; accepted-manuscript posting date unverified. Date basis recorded; arxiv-1705.07771 would become [concurrent] under a 2017-07 date, changing no verdict. | Appendix; extra.json |
| L6 | applied | Method walkthrough cut from Verdict; Table 4 p-value list replaced by the Bonferroni count and baseline levels. | Verdict; M06 |
| L7 | applied | Dataset release cited to the Abstract and later reuse. | Verdict |
| L8 | applied | Robustness credited to the authors' stability meaning (§6.1). | Claims list |
| L9 | applied | §4.2 EMG statement with "(inference)" on the retained range. | Claims list |

Counts: 22 findings; 22 applied (M2 partly: no DaSalla reference since it is not named as a cited work); 0 rejected. Verdict changes: M12 standard → behind; M03 not_reported → standard; M06 unchanged (standard, new reason).
