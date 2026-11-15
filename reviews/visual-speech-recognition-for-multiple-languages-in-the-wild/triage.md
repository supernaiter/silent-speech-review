# Triage of the independent evaluation (2026-11-15)

Source: visual-speech-recognition-for-multiple-languages-in-the-wild.eval.md (25 claim checks, 14 required fixes, 2 state-of-the-art notes). Each item was checked against short reads of the target text (Table 2, Table 5, Table S2, Table S9, Table S26, Tables 4 and S13-S17, Sec. 1.4, Sec. 1.5, Sec. 1.7, Sec. 2.2, Sec. 3.3, Sec. 3.5, Supp. Sec. S9.8-S9.9), the USR 2.0 text (Table 2, Sec. 4) and the SynthVSR text (Abstract). Numbering follows the required-fix list; F-items are the state-of-the-art notes; C-items are claim checks not covered by a fix.

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | The 2.1-point gain over the 31,000 h RNN-T belongs to the 1,459 h model: "our best model, trained on 1 453 h of video, leads to a 2.1 % absolute improvement over [16] which uses 31 000 hours" (Sec. 1.5); 33.6-31.5=2.1 | M12 evidence, split into two sentences |
| 2 | applied | "380 h" is in the source ("trained using the LRW and LRS2 datasets, in a total of 380 hours", Supp. Sec. S9.9). The cross-test-set point is right: Table 5's LRS3 column (LRW+LRS3, 595 h) gives 35.8 vs 37.8 without both auxiliary losses, 2.0 points (5.6%), against 1.5 points (4.7%) at 1,459 h (Table S26). On the same test set the effect barely shrinks, so "fades" was dropped | Verdict; M02 evidence and verdict line; slots M02 note |
| 3 | applied | 57.9 and 67.0 are the paper's own models (MTit 57.9±0.7, CMfr 67.0±0.6), not CM-seq2seq. CM-seq2seq means are 58.9/66.4 (Es), 71.5 (It), 70.2/65.7 (Pt), 84.0/79.9 (Fr). Retraining is stated: "there are no results from previous works, we trained the end-to-end model presented in [10] to serve as the baseline" (Sec. 1.7) | Claims-outrun bullet now gives 58.9-84.0 and names Spanish; notes t114 |
| 4 | applied | The same Sec. 1.7 quote shows Spanish (CMes) also has only the authors' retrained baseline; Mandarin (CMLR) has published systems in Table 3 | Verdict last sentence (English and Mandarin only); verdict.short "4 of 6" |
| 5 | applied in part | Table S9 labels the 39.1 row "+ Improved LM" (LRS3 44.9 -> 40.6 -> 39.1) and Sec. 3.5 describes the larger LM and beam 40; Table 5's last row (no auxiliary losses, no masking) is also 39.1 on LRS3, so the chain is consistent and the LM point stands. The "as much as" framing was imprecise: on LRS3 tuning+LM (5.8) and time masking (2.7) each exceed both losses (2.0); on LRS2 both losses (3.7) exceed masking (3.1) | Verdict sentence 3 restated with LRS3 numbers; M03 evidence gives both test sets; notes t116 |
| 6 | applied | USR 2.0 Table 2: Large, LRS3+Vox2 unlabelled, 30 h low-resource setting, 23.7; abstract: "~2500 hours of unlabelled data", pseudo-labelling throughout. SynthVSR (in the M12 ledger) gives 16.9% "using publicly available data only", lower than both 17.0% and 17.6%, so the state of the art moved to 16.9% [later] | M02 and M12 State of the art; M03 State of the art condition; slots M02/M12; M12 audit state_of_the_art and read_fulltext; refs.json (liu2023synthvsr); notes s2, s3 |
| 7 | applied | Normalization by "the overall mean and variance of the training set" is in Sec. 3.3, and the 88x88 input is in Supp. Table S2. Only the decoding length penalty remains undisclosed (paper gives the LM and beam size 40 only) | Claims-outrun code bullet; crop question replaced by length penalty; notes t83 corrected, t115 added |
| 8 | applied in part | Sec. 2.2: subject-independent VSR "is another area that deserves further attention", a future-direction statement; wording now quotes it. No speaker-disjointness statement found for any corpus | Claims-outrun bullet rephrased |
| 9 | applied | "Not reported" refers to the token set / OOV policy and speaker overlap (slot notes); the table entries now say so | slots M08 and M11 "This paper" entries |
| 10 | applied in part | The M12 topic is the LRS3 benchmark and its tally is by supervision kind; kept as the usual design for systems evaluated there, but 18 vs 17 is now called "barely ahead" | M12 Usual approach |
| 11 | rejected | Sec. 1.4: "we used the models trained on LRW + LRS3 and LRW + LRS2 as initialization and fine-tuned them further on LRS2 and LRS3"; wording made explicit | M03 Usual approach |
| 12 | rejected | The Appendix M02 line lists "audio feature regression 5 (pattern match)"; the evaluator saw a truncated row | none |
| 13 | applied | Sec. 1.5: "it performs worse than [6], which presents a model trained on 90 000 hours" | M12 evidence: "(disclosed in Sec. 1.5)" |
| 14 | applied | The changed slot is M02 only, but the Verdict now states that the gain rests more on the M03 recipe | Verdict sentences 1 and 3 |
| F1 | unverified | LP-Conformer (ICASSP 2024, 12.8% LRS3, non-public data) is not in the wiki ledger; not checked against its source. The review's non-public comparator stays 17.0% [concurrent] | verification_status |
| F2 | rejected | Auto-AVSR 19.1% does not beat 16.9% or 17.6%; no change needed | none |
| C5 | rejected | Not an error: Table 2 lists two 90,000 h systems, ViT3D-TM [6] (25.9) and ViT3D-CM [17] (17.0); Sec. 1.5 cites [6]. Both beat 31.5%, so the review's statements hold | none |
| C17 | rejected | Sec. 1.8 confirms mean and best over ten runs in Tables 1-4; no best-run selection split is stated (absence finding kept) | none |

Claim checks 2, 7, 8, 11, 12, 15, 16, 18, 19, 21, 22, 23 and 25 are covered by the fixes above; the remaining checks were marked correct and needed no change.

Counts: applied 12 (fixes 1, 2, 3, 4, 6, 7, 9, 13, 14; fixes 5, 8, 10 in part), rejected 5 (fixes 11, 12; F2; C5; C17), unverified 1 (F1).

Unverified items recorded in reader/extra.json verification_status: the released-code length penalty (t84; repository not re-opened), the Serdyuk 17.0% (read from target Table 2 only) and LP-Conformer (F1).

Rerun of steps 6-8: render_review, build_refs, fill_row, check_review (0 FAIL, 0 WARN, body 6,994 characters, 9 references), claim_table with every body row mapped to a notes entry, a tally or an inference. The Verdict changed and verdict.json was updated.
