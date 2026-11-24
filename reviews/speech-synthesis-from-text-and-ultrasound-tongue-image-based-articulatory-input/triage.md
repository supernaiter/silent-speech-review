# Triage of the evaluation (16 required fixes)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | Table 4 test F0-CORR rises for 6 of 8 speakers (t59-t66); t24 full sentence includes "and in some of the F0 measures" | Verdict (excitation mixed); M06 "spectrum only" removed; claims-outrun bullet 1 quotes the full sentence |
| 2 | partly applied | Sec. 5 does say the system "is not suitable for direct TTS or for a Silent Speech Interface" because both inputs are required (t100, t29, quotes extended). The concession is the authors'; wording now repeats it exactly | Verdict last sentence |
| 3 | applied | t14: durations not modelled, so all systems share reference timing (inference); timing removed from the leak argument, confound narrowed to within-frame articulation of the scored token | claims-outrun bullet 4 |
| 4 | applied | Table 1 group means 0.099 dB (flagged 01fi, 04me, 05ms, 07me) vs 0.152 dB (others) (inference); 04me-only sentence dropped | M05 section |
| 5 | applied | Same standard for small MCD and BAP differences; MCD claim rests on sign consistency across 8 speakers | claims-outrun bullet 2 |
| 6 | applied | Comparison set stated as ultrasound-to-speech mapping (the ult2wav branch), not the fusion; Tongue2Speech labelled ultrasound-only; no text-plus-ultrasound comparator in the Appendix tallies; EMA predecessors named from Sec. 5 (t98, t99) since Cao et al. and Ling et al. are not in the wiki (unverified beyond the paper's own account) | M06 Usual approach / State of the art; slots M06 field and sota |
| 7 | applied | t34: runs and seeds not reported | Verdict "runs not reported"; M03 cell |
| 8 | applied | Dev BAP lower for 6 of 8 (06fe, 07me rise) | claims-outrun bullet 1 |
| 9 | applied | Sec. 5 (t98): earlier EMA works used articulatory data "as the input [18]"; the claim that measured input at synthesis is the paper's own choice was wrong and is removed | Verdict sentence 2; M06 evidence paragraph |
| 10 | applied | Audit: MCD 21, MUSHRA 14 | M12 table cell |
| 11 | applied / partly | Quotes extended or added: c26 (81.67 fps), c27 (23 raters, 2019), audit quotes for 23 (2017) and 24 (2018) listeners, t23 full "did not help" sentence, t5 split, c28 (2D CNN baseline). The 2020 count (22) has no quote in the WaveGlow text and was dropped. "Tied to no outcome" for [7] rephrased to what c24 says (flag corrupted recordings). Single-frame input marked (inference) | M05, M06, M12 sections; notes.json |
| 12 | applied | t23 says "did not help"; review now says the effect was harmful without "in fact" | claims-outrun bullet 3 |
| 13 | applied | t92 hedge "may increase the naturalness" quoted | Verdict |
| 14 | applied | M05 Usual approach now labelled inherited, State of the art describes the 2020 measure's use (c24) | M05 section |
| 15 | applied | c28: reduction relative to the 2D CNN | M06 evidence paragraph |
| 16 | applied | "significantly lower" located at Sec. 3 (t18, t93) | Questions |
| C6 | applied (coordinator) | M12 behind required >=3 earlier comparable papers in the same setting; the group's listening tests are ultrasound-to-speech, not text-plus-articulatory TTS, so the rule is not met | M12 verdict downgraded to standard (slots, text, extra.json) |

Counts: 16 findings: 14 applied, 2 partly applied (#2: the concession is the authors own, wording aligned; #11: the 2020 listener count has no quote and was dropped), 0 rejected; the Cao/Ling part of #6 stays unverified (not in the wiki). Coordinator item 6 applied (M12 behind -> standard).
