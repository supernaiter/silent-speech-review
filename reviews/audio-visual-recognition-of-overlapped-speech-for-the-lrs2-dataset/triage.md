# Triage of the evaluation

| # | Finding | Verdict | Evidence | Where applied |
|---|---|---|---|---|
| 1 | Fig. 2 depth confound misread (eval #10, H1) | applied | Fig. 2 labels: RecogNet TDNN-F 1-15 / 1-12 / 1-9 (notes t74-t76); AudioNet and VisualNet 6 layers each (t14), FusionNet 3 (t13): audio path 15/18/15, total 15/24/24 (inference) | Verdict; M06 gated section; claims-outrun item 2; next-steps item 1; slots M06 note; notes t66 text |
| 2 | M12 "behind" overreaches; rule not stated; best prior not named; Chao one SNR; credit what is stated; M11/M12 double count (eval #17, #18, H2) | applied | Own check: Shao 2006 (s3, s4), Barker 2007 (b3, b4) and Chao 2016 (c5, c6) state interferer source and test size; target states test-set references, truncation and four SNRs (t65, t78, t52) but not interferer source or count. Verdict kept behind, scoped to test-mixture reporting, best prior Barker and Shao 2007 named | Verdict; M12 section; slots M12; M11 changed from not reported to standard (gap counted once, under M12) |
| 3 | "V⊗A vs AV⊗A repeats Shao's contrast" wrong (eval #6) | applied | Shao compares audio-only vs audio-visual weight estimators (s2); the target compares visual vs audio-visual gates | Sentence removed from M06 gated section |
| 4 | Quote the authors' "only previous work" statement in full with its hedge; Chao is cited (eval #7) | applied | t77 ("To the best of our knowledge, ...") and t72 | M06 gated section; Verdict ("which the authors cite") |
| 5 | Name same-group Liu et al. 2019; "holds only for neural gates" inaccurate (Shao's weights from an MLP) (eval #23) | applied | Target ref [26]; Crossref 10.21437/Interspeech.2019-1536; Shao Sec. 2 MLP | M06 gated section reworded to "learned feature-level gating"; reference added ([concurrent]) |
| 6 | Afouras LM 26M words vs target's >2M words (eval #14) | applied | Afouras Sec. 4 (a6); target Sec. 4.1 (t9) | M06 back-end section |
| 7 | Yu 2020 ~13% gap is for multi-channel audio-only systems (eval #21) | applied | y3 | M12 state-of-the-art line |
| 8 | "no clean row" should be "no clean-test column" (eval #12) | applied | Table 3 has clean-trained rows, no clean test column (t71) | Verdict; slots M12 |
| 9 | "one run per system" not stated by the paper (eval #13) | applied | No seeds, runs or variance stated (t80) | Verdict; M06 and M12 sections; claims-outrun; verdict.short; en.limitations |
| 10 | Nguyen AVYT size, LM not stated (eval #19) | applied | n4, n5 (1449 h talking-face, 77 h silent-face), n6 (no LM stated) | M06 gated state-of-the-art line |
| 11 | Auto-AVSR 1.7% is Nguyen's re-evaluation; LM (eval #20) | applied | n3, n6 | M06 back-end state-of-the-art line |
| 12 | Add Nguyen V1 15.7% for the lip-reading half (eval #20) | rejected | The slot's state-of-the-art line is set on the audio-visual step; adding a visual-only value would exceed the length limit and is not needed for the 48.3 vs 48.86 finding | - |
| 13 | Claim-table quote t29 lacks "significantly" (eval #25) | applied | t79 quote "methods significantly outperform the feature concatenation based method" | claims.md row 27 |
| 14 | Process notes in the reference list; author-name consistency (eval #26, low 12) | applied | Ref 1 note now "Target."; ref 5 note without the layout remark; header author list matches reference 1 ("Zhang, S.") | refs.json; header line |
| 15 | Speaker-disjointness question: LRS2 has no speaker labels (eval low 13) | applied | t51 | Question reworded to programme overlap |
| 16 | Borderline rows in the 188-study prior pool (eval #2) | rejected | They lie outside the AVSR-89 and LRS2-6 subsets used for every count in the review; no number changes | - |

Counts: 14 applied, 2 rejected, 0 unverified. Verdict changes: M11 not reported -> standard (to avoid counting the test-mixture gap twice); M12 stays behind with the rule and the best prior stated; M06 stays standard.
