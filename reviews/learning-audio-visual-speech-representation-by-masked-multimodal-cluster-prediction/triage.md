# Triage of the fallback evaluation

Evaluation: fallback language model over the claim table and positions (ChatGPT pending). Round 1.

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | "Five iterations" is in Sec. 4.1 / B.4 (notes t42); the quote was missing from the claim row only | claims.md row 1 now maps t42 |
| 2 | applied | The 334 h vs 1,759 h confound (Sec. 4.2 footnote 2, t68) belongs next to the gain claim | Verdict sentence 2 rewritten; the gain is now stated against the paper's own baseline, with the data-size confound beside the 59.8% |
| 3 | applied | The match is in the source: Table 2 groups rows by "Large, LRS3+Vox2", and low-resource means "the 30-hour trainval partition of LRS3" (arxiv-2602.19316 Sec. 5) | Quotes s6 added to notes and claim rows 4 and 8; "identical" changed to "the same" |
| 4 | applied | Only Sec. C.2 reports a spread (18.0 ± 0.5%); Table 1 reports no repeated runs | "single runs" changed to "no repeated runs in Table 1"; the C.2 spread is acknowledged in Questions |
| 5 | rejected | Arithmetic checked, correct | none |
| 6 | applied (wording) | The rules make M02/M03 standard because the effect is not repeated (seeds, subjects, datasets), not because of later work; later work only sets the state of the art | Verdict separates the two: standard on repetition, then a separate [later] sentence |
| 7 | applied | The two counts cover different populations (141 LRS3 papers vs 75 papers selected by a self-supervision pattern) | M03 usual approach now gives text labels 18 and paired audio 17 of 141 instead of "normally trained on transcribed video" |
| 8 | applied | Footnote 2: "different parameters and ASR model used for filtering non-English data" | "different filter" changed to "different filtering parameters and ASR model" |
| 9 | applied | LiRA Table 2: "LiRA-Supervised [16] Supervised (CL) 39.1" (p4) | Quote added; text states that LRS2 and LRS3 differ so only each gain over its own baseline compares |
| 10 | applied | The absence rests on candidate titles, and only two of the earlier studies were read | Sentence "None of the earlier studies among the 123 ..." removed; logged in verification_status |
| 11 | rejected | Correct | none |
| 12 | rejected | Two different counts that happen to be equal: paired_audio supervision is 258 folders (slot notes, M03 field), and LRS3 mentions are 258 unique studies (M12 audit counts). Each tier is named | none (claim rows now name the two sources) |
| 13 | applied | arxiv-2602.19316 Sec. 3: the student matches "the teacher's outputs on unmasked audiovisual inputs" (s5); its VSR is lower in every size/data group of Table 2 (51.8 vs 36.2, 46.1 vs 26.4, 32.5 vs 23.7, 34.8 vs 24.8, 28.6 vs 21.5; s2, s3, s7) | M02 state-of-the-art line reworded to the teacher's audio-visual input and "every matched size and data group" |
| 14 | applied (location) | Table 4 marks the LM for Ma et al. (2021b) at 2.3 (t71); Sec. B.4: "No language model is used for S2S decoding" (t72) | Location narrowed to Table 4; quotes added to claim row 14 |
| 15 | rejected | The count comes from the M12 audit counts (pattern match, unique studies), not from a quote; [6] is cited for the benchmark's definition, and the count carries the field claim | none |
| 16 | rejected | Correct; 17.6% is the best LRS3 visual-only value among the M12 audit candidates and is confirmed in its source | none |
| 17 | rejected | 1,759 h is in t1's condition and Sec. 4.2 | none |
| 18 | applied | LRS3-only pre-training uses all 433 h (Sec. 4.2, t70), and the 433 h comprises pretrain 403 h plus trainval 30 h (t40) | Location (Sec. 4.2) added; quote t70 added |
| 19 | applied | Table 1 note and Appendix: "We re-implemented the LiRA (Ma et al., 2021a) training objective in our framework" (t69) | Wording and location corrected; claim row 20 maps t69 |
| 20 | rejected | Correct | none |
| 21 | rejected | The table values come from slots.json and notes t39, t42 and t43, which the gate traces | none |
| 22 | rejected | The compact format drops Questions and Appendix; this is not an error in the review | none |
| 23 | unverified | arxiv-2602.19316 bibliographic data are taken from its first page (ICLR 2026, arXiv v1 22 Feb 2026); the evaluator could not confirm them independently | verification_status |

Counts: applied 14, rejected 8, unverified 1.
