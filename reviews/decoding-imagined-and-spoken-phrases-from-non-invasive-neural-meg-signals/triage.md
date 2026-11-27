# Triage of the independent evaluation

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| F1 (H1) | applied, recount differs | Dash et al. 2018 (pmc-6876632-megtrials) is a prior MEG decoder on the same paradigm: ANN on wavelet RMS, 70/15/15, 4 subjects, 78.35% imagination; pre-stimulus rise attributed to memorisation (Results; Discussion). Broadened stage-term rescan found no other on-population prior. Population is 16, not 18, because F5 and F11 remove two items. | Population and counts in all audits; M06 usual approach (deciding prior); M12 pre-stimulus paragraph; Appendix; "no MEG-only" removed |
| F2 (H2) | applied | IEEE Access 2020 also uses within-subject 5-fold CV, an SVM, 60 trials per phrase and 7 subjects (Sec. II). | 45.46 vs 80.83 removed from Verdict and verdict.json; 43.8% sentence removed; M12 state of the art now Jhilal 2026 LOSO (Tables 1, 3) |
| F3 (H3) | applied | Target Sec. 1 (baseline inspired by Rezazadeh Sereshkeh 2017); Sec. 5.1 ("did not intend to compare the features"). | M06 paragraph; Verdict reason rewritten |
| F4 | applied | EMBC 2019 paper is unread. | Citation removed; Appendix names it only as the counting date; "first CNN" quote dropped; verification_status |
| F5 | applied | arxiv-1705.07771 uses synthetic EEG (Abstract). | Excluded from population; CNN priors 1 pattern match, 0 design-confirmed; reference removed |
| F6 | applied | Table 1 AlexNet 43.77%; 30% and 20% in Sec. 4.2; methods equal at pre-stimulus (Sec. 4.1). | Verdict, M12, slots, verdict.json |
| F7 | applied | Perception decoded at 86.83-90.38% (Sec. 4.1); preparation follows text offset (Sec. 2.2). | Verdict last sentence; claims bullet 1; verdict.short |
| F8 | applied in part | "About 50" is training images; Table 2 note says 1,382 total while each row sums to 1,382. The "three runs of 15% of 3,046" explanation is not adopted: it is a guess the paper does not support. | Claims bullets 3 and 4 |
| F9 | applied | Jhilal Table 4: RandomInit + full FT 80.2 / 69.1 (imagery vs silence), 51.9 / 44.8 (vowels). | M03 state of the art, slots, audit |
| F10 | applied | Audit tiers separate pattern match and read-confirmed counts. | Appendix; M12 usual approach |
| F11 | applied | Sarmah and Kennedy (2013) records inner-speech attempts from an implanted electrode, the same signal class as the excluded Brumberg 2011. | Excluded from population |
| F12 | applied | No audit count supports the absence; forward-selection nesting is unstated in the passages read. | M06 state of the art reworded as closest later comparator with 60 trials and forward selection; nesting moved to verification_status |
| F13 | applied | Sec. 3.2.4.1: ST-CNN trained with each scalogram image as a sample. | Questions; split-reporting bullet |
| F14 | applied | Sec. 2.1: jaw-motion air bladder recorded during articulation. | Claims bullet 1 |
| F15 | applied | Restatement and placement. | Verdict sentence 1 shortened; repeated sentence removed; "none earlier than the target" |
| F16 | applied | Sec. 5.1 statements are the authors'. | M06 paragraph credits the authors |

Counts: 16 findings; 14 applied in full, 2 applied in part (F1 recount, F8 explanation); 0 rejected outright. Verdicts unchanged: M03, M06, M12 standard.
