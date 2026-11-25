# Triage, round 1 (evaluation: a language model separate from the writer)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | SynthVSR Sec. 4.6 "16.9% (18.2%" (c23); Whisper-Flamingo Sec. 4 "SOTA A VSR on LRS3 (0.76%)" (c22); Llama-AVSR Abstract 0.77% with 1,756 h (c20, c21). All three are in the wiki and were read at the passage. "Public data" defined once (public audio-visual corpora; Whisper initialisation and labellers trained on non-public audio allowed, as in Auto-AVSR). AVSR gap recomputed: 0.9 vs 0.76 = 0.14 points (inference). | M12 State of the art; slots M12 sota; audit M12 (read_fulltext, state_of_the_art_*); refs [7], [8]; row position_in_field |
| 2 | applied | Target §3.3 gives epochs and optimizer only (t61); no statement of a single run. Replaced with "no run count, seeds or spread reported". | Verdict; M12 usual approach; slots M03, M12; row fields |
| 3 | applied | §4.2 "An absolute improvement of 1.7 % ... This gain is likely due to the increase in model" (t84, t98); [3] Table 2 818 h best 34.7 (c08); 31.5 is best of ten (c06, c07). The 12.4-point / 39% sentence removed; the same-model effect 33.0 -> 19.1 (Table 2) kept as the scale effect. | M02 body |
| 4 | applied | [2] Sec. 4: "54.2% and 61.7% for LRS2 and LRS3" without ground truth (c18); 59.8% after full supervision (c03). Target §1 describes [9] as posterior matching (t94) although [2] Fig. 1 uses CTC on ASR transcripts (c01); text now says Auto-AVSR differs by dropping distillation. | M02 body |
| 5 | applied | 0.9 vs AV-HuBERT audio-only 1.3 (t47) = 31% (inference); headline weakness tied to unnamed baseline, not repetition. | Verdict; claims outrun bullet 1 |
| 6 | applied | Slot cell "Human transcripts only" changed to "Text transcripts"; "18 of these" now refers explicitly to the 148 pseudo-label hits. | slots M02; M02 usual approach; Appendix |
| 7 | applied | Table 1 gives labeller WER on LRS3 test (t25-t28); request narrowed to label WER on the added corpora. | What the field needs next, M02 |
| 8 | applied | Repository path and commit from t68/t69 (commit 182b628, train.py:91-101) added. | Questions for the authors |
| 9a | applied | Table 4 row "Ours 1 902 1.0" added as t99 and used in the claim table. The sum 157+438+1,307 not stated (LRW hours not in notes). | claims.md row 25; notes t99 |
| 9b | applied | LP Conformer venue ICASSP 2024, pp. 10136-10140, from the reference list of arXiv:2602.19316 (line 753-755). | refs.json |
| 9c | applied | Target's §1 contrast is with its refs. [3, 16]; sentence rewritten so [5] is cited only as the same pipeline. | M02 body |
| 9d | applied | USR 2.0 uses no external LM (c19) while Auto-AVSR VSR uses one (t21). | M02 State of the art; Verdict |
| 9e | applied | M12 usual approach now states the evaluation form (one test WER per row, inference) against the lineage's ten-run means. | M12 usual approach |
| 9f | applied | Whisper 19.0 vs CM-T 19.1 inside the noise band; "on average" undefined (t11). | M12 body |

Counts: 14 items (9 required fixes, fix 9 split into 6), 14 applied, 0 rejected, 0 unverified.
