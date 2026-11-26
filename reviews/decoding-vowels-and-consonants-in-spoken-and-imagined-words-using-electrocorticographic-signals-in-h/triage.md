# Triage of the independent evaluation (2026-11-26)

Findings are the evaluator's 12 required fixes plus the claim-table rows it flagged. Each was checked against notes.json and only the needed source passage.

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | M04 audit candidates: the 39 prior hits are mostly audiovisual and lip-reading papers; EEG 10 is a full-text term count, and only Deng 2010 decodes imagined speech. No clean design count of adequate size exists. | M04 usual approach rewritten; table `matched` and `n` set to null; cell now names the design: "EEG imagined-speech decoding without overt condition"; audit `usual_approach` relabelled with `note_triage`; Appendix lists "Imagined-speech decoders among them: 1". |
| 2 | applied | Table 3 z-scores (t50, t51); one-sided Bonferroni bound over 47–64 electrodes gives z of about 3.07–3.16: covert vowels A, D (2/6); covert consonants A (1/6). | Verdict and M04 report both the uncorrected (5/6, 4/6) and corrected (2/6, 1/6, inference) counts. "Ahead" is kept because corrected vowel repetition is 2 or more, and it is stated as a protocol verdict (paired covert and overt discrimination within patients on ECoG). |
| 3 | applied | Same as #2. | Verdict and M04 say "ahead as a protocol, not for accuracy". |
| 4 | applied | Leuthardt header "2011 Apr 7" (c38) vs target "2011 Jul 13" (t55); "imagined phoneme vs. rest (patients 3 & 4)" (c37). Brumberg 2011 (pmc-3096823-phonintent) is in the wiki; read in the passages quoted (b1–b3); epub May 2011, so concurrent. | M04 concurrent paragraph gives both dates, the vs-rest task (detection, not discrimination), and cites Brumberg 2011 [concurrent]; added to refs, the M04 audit `read_fulltext` (timing concurrent) and the Appendix. |
| 5 | applied | t27 ("for the first time", Sec. 1); t28 (Sec. 4). | The Verdict states the review confirms the authors' own "for the first time" claim. |
| 6 | applied | c16 (Deng: 22.10% vs 16.67% chance, not significant). | M04 usual approach: rhythm decoded; joint syllable-by-rhythm classification not significant. |
| 7 | applied | Sec. 2.5 reports per-patient MRMR training with fixed feature counts; only nesting is unstated (t36). Rule: no not_reported with a filled cell. | M03 changed to standard; nesting concern kept in claims-outrun and questions. |
| 8 | applied | t52 ("for the best location", Sec. 2.5); t53 (Sec. 4). | Selection bullet now states best-location reporting as fact; the MRMR nesting is the only stated unknown. |
| 9 | applied | Table 1 lists "I 44 M" (t54); Table 3 lists H. | Added to the inconsistencies bullet. |
| 10 | applied | s4: 1/6 chance for S1–S5, 1/8 for S6–S9. | M04 state of the art gives both chance levels; the 63.7-point figure is "about … over the six-class chance (inference)". |
| 11 | applied | t10 (47–64 channels); decoded classes, not words (t4). | verdict.short rewritten: "vowel and consonant-class decoding", "best-of-47–64-electrode selection". |
| 12 | applied | Chen 2024 quote is present in the wiki source (verify_quotes passes). | notes entry ch1; claim rows for Chen mapped. |
| 7b (table denominators) | applied | Audit tallies. | Table cells name the base: M06 "base 3 prior studies" (2), M12 "base 13 prior studies" (3); M04 has no count. |
| 7c (M12 base 13) | applied | pmc-3342676-gammaev and pmc-3321121-revspeech are 2012 papers carried with index year 2010 (evaluator's epub dates; consistent with the 2012 Leuthardt et al. title in the index). | M12 audit `prior_tally_<slug>` corrected to 13 with `correction_triage`; text, table and Appendix use 3 of 13. |
| R22 (M06 base composition) | partly applied | Evaluator: the 3 are Flinker 2010, Brumberg 2009 and Guenther 2009. Blakely 2008 is not in the wiki; Chang 2010 is a perception study outside the topic rule. | No text change beyond keeping "the 2011 base is thin"; verdict stays standard (fewer than 3 comparable priors, so "behind" is excluded). |
| Outside knowledge (Martin 2016, Proix 2022, Wandelt 2024, Blakely 2008) | rejected | Not read, or not in the wiki. | Not cited; noted in verification_status. |

Side effects: to stay within 7,000 characters, the Kunz 2025 citation and the overt-versus-covert-denominator bullet were removed. Kunz stays recorded in the M04 audit as `read_not_cited`.

Gate after triage: verify_quotes 99 found and 0 missing; audit_tally OK on 3 audits; check_review 0 FAIL, 0 WARN, body 6,988 characters, 8 references.
