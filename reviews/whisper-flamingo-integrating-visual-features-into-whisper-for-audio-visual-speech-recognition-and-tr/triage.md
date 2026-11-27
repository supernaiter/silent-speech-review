# Triage of the independent evaluation

Evaluation: `whisper-flamingo-integrating-visual-features-into-whisper-for-audio-visual-speech-recognition-and-tr.eval.md` (15 required fixes). Each finding was checked against notes.json and the cited source passage. Verdicts per slot are unchanged (M03, M06, M08, M12 standard); M13 stays standard.

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| H1 | applied | Interspeech Sec. 3.3 has "improves the clean WER from 2.3% to 1.5%" (t73); the v3 text has no such sentence and gives 49.5% (v8) and beam-1 rows 1.1% vs 1.0% (v1, v3). | Verdict: the clean gain is now credited as withdrawn by the authors' revision. Where-claims bullet 1 rewritten the same way. Beam-15 question replaced by a question v3 leaves open (unfrozen gated vs early fusion). |
| H2 | applied | DoubleHelix Table 2: AVGER 3.7% at 0 dB (s8); 3B LLM decoder (s9); v3 Whisper-Flamingo 5.6% at 1,759 h (v11). The babble file is not named in DoubleHelix. | M06 State of the art lists the decoder, hours, unspecified babble file, single runs and AVGER 3.7%; "more training hours" removed; table cell marks the other noise file. DoubleHelix kept as reference (best clean and average WER among read works). |
| H3 | applied | Simic and Bocklet (arxiv-2312.13873, 2023-12, [concurrent]): frozen Whisper, 13M fusion module with cross-modal attention enhancing the ASR input, LRS3, babble (p7, p8). FAVA via target Sec. 2 (t65); not in the wiki. | Added as reference [3], [concurrent], read and listed in the M06 and M03 audits and Appendix. M06 novelty narrowed to "gated attention inside the frozen decoder"; M03 now "follows AVFormer and the [concurrent] Adaptive AV"; FAVA described through the target. |
| M1 | applied | Sec. 3.2: early and late fusion fine-tune all of Whisper (t71); audio-visual gain over audio-only repeats over three sizes (t48) and two datasets. | M06: design and freezing named as confounded; verdict reason now "gain over audio-only repeats, gain over other fusions does not". M03: "no unfrozen gated variant". |
| M2 | applied | Both decodes use the same beam for both models (v1, v2, v3); v3 revises to 49.5% (v8). | 52.1% overreach bullet dropped. |
| M3 | applied | Audit notes: 552 = 570 - 18 and 125 = 159 - 34 are complements. | M08 now "name no speech translation or BLEU (pattern match, lower bound)"; M12 "lower bound"; Appendix says positive counts are upper bounds, complements lower bounds. |
| M4 | applied | u-HuBERT weights not public (t72); MuAViC noise-file caveat by the authors (t46, t63); released noise files in the repository (c1). | u-HuBERT bullet credited to the authors with the reason; MuAViC noise bullet dropped as an author caveat (kept as "non-identical noise" in Verdict); M12 next-step asks others to test on the released noise files. |
| M5 | applied | MTC-AVSR Sec. 3.1 MUSAN babble (s10); Sec. 3.3 says the files are not released; Spanish 25.2 vs 25.4 (s4, s6). | M08 State of the art: four directions, trained with MUSAN babble, non-identical noise, "ahead except Spanish"; table cell no longer cites the Spanish value. |
| M6 | applied | DoubleHelix p. 1 lists Ziwei Cheng, Zhenhua Tan, Zhuomin Zhu. | refs.json authors corrected; kept as arXiv preprint (venue not confirmed). |
| L1 | partly applied | USR 2.0 appendix Table 13: Base, low-resource runs. | Conditions added to M12 State of the art. Kept USR 2.0 rather than the prior CI exemplars: it is the later best on the slot's own step; the prior exemplars stay in the published table. |
| L2 | applied | v3: audio-only fine-tuned Whisper-Large 0.68% (v10). | M03 State of the art: clean LRS3 does not rank training regimes; the 0.76% sentence removed. |
| L3 | applied | t46, t63. | Verdict: "non-identical noise". |
| L4 | applied | Sec. 2 (t74); Sec. 3.4 (t75). | M06 usual approach credits the authors; M08 clean-lead sentence credits the authors. |
| L5 | applied | Bins are month-level. | Appendix: "at month level". |
| L6 | applied | t76 (per pair, Sec. 3.4); t54 and c1 (code). | Notes entries added; claim table refilled. |

Counts: 14 applied, 1 partly applied, 0 rejected.
