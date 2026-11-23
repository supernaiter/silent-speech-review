# Triage of the independent evaluation

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | Verdict relies on calibrated numbers; Sec. II.A gives 500-ms windows with 50-ms shift and Sec. II.B gives no trial-level split (notes t2, t70) | Verdict: leakage sentence marked (inference); verdict.json position |
| 2 | applied | Table I compares (5,6) and (3,10) at strict LOSO and three calibration levels (t23-t54); "one comparison" was wrong | Verdict and M03: "only two settings are compared, with no pooled baseline and seeds not reported"; M03 names the strict-LOSO (5, 6) to (3, 10) move |
| 3 | applied (partly) | Three false-positive snippets checked (alternating LOSO folds, trials shuffled within a subject, a section heading); deciding priors read: Panachakel 2021, Park 2025 | Appendix describes the three false positives; M03 states the verdict rests on effect, not novelty. MAML-style prior: unverified (no locator) |
| 4 | applied | "not shown" is the reviewer's inference from Soroush Sec. II.E (r1, r3) | Verdict: "(inference)" |
| 5 | applied | t6/t7: "All the parameters and kernel settings were kept identical to the original implementation" (Sec. II.A) | Verdict wording "its own earlier ... detector, kept unchanged (§II.A)"; claim row 1 maps t6, t7 |
| 6 | applied (partly) | Belfrouh: five-class (r9); Attar: eight words (r16); Sharon is a detection task (r4) | M03 SOTA "five-class decoding, not detection"; M12 SOTA "(classification, not detection)"; table rows unchanged (body length limit) |
| 7 | applied | t41 quote: "0.358 ± 0.791 0.791 ± 0.101" | Claims-outrun bullet: ± equals the row's AUC, likely a transcription error |
| 8 | applied | t62 (Abstract, "scalable, user-adaptive"), t63 (Sec. I, "preliminary evidence") | Claim table row 40 |
| 9 | applied | Extended quotes: r7 (Panachakel Sec. I, "... on a new (target) subject."), r3 (Soroush, "... of the overt mode of the corresponding participant"), r6 (Sharon, "The accuracy of the activity detection classifier is ≈76%"); new b1 (Bhadra Abstract, binary BCI through syllable imagery), b2 ("On each day ... BCI-control session") | notes.json; M12 now says "activity-detection accuracy"; M13 SOTA says "offline calibration then control each day" instead of "daily recalibration" and drops "closed-loop" |
| 10 | applied | Table I rows (t23, t27, t29, t45) | M03: "moving from (5, 6) to (3, 10)"; "gap from strict LOSO (3, 10)" |
| 11 | applied | t66: seeds and the meaning of ± not stated | "seeds not reported" in Verdict, M03 and claims-outrun |
| 12 | applied | build_refs abbreviates given names to initials | Header changed to "Ko, B., Kim, S., Lee, S." to match reference [1] |
| - | applied | Evaluator note: "implies" stronger than evidence | M12: "suggests a dominant idle class (inference)" |

Counts: 12 required fixes; 12 applied (2 of them partly); 0 rejected; 1 sub-item unverified (MAML-style prior, item 3).
