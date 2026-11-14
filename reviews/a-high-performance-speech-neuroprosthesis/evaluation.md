# Evaluation: A high-performance speech neuroprosthesis

Date: 2026-11-14. Evaluator: fallback pass over the claim table (`claims.md`) and the review's Verdict and component positions, no source re-reading. ChatGPT evaluation: pending (chatgpt_pending). The free-model fallback run returned no output, so this pass was made by the writer as a self-check; it is not independent and the ChatGPT pass should replace it.

| No | Claim (short) | Check | Note |
|---|---|---|---|
| 1 | Three changed components (M05, M06, M07) | wording | "recurrent decoder with CTC taken from the handwriting BCI" overstates the borrowing: the handwriting BCI shares the GRU and day-specific layers, not CTC (t52, t55). |
| 2 | [later] 2.5% WER on the same vocabulary | match | s1; vocabulary size is in the entry text, not in the quote. |
| 3 | 23.8% at 62 words/min, one participant | match | t2, t4, u4. |
| 4 | ECoG reached a similar error at a higher rate | match, qualified | s6 (25%, 78 wpm, 1,024 words, silent attempts); the component section states the vocabulary gap. |
| 5 | Ratios untested; no seeds or selection data | match | t3, t5, u6, u1, u2. |
| 8 | about a tenth of 23.8%; half of 62 wpm | match | 2.5/23.8 = 0.105; 31.6/62 = 0.51 (inference, marked). |
| 9 | 32% to 21%; 0.57 per doubling; ten seeds | match | t26, t27, t39. |
| 10 | 253 channels, 25%, 1,024 words, 78 wpm | match | s6, s7, s8. |
| 13 | PER 19.7/21.4 vs WER 23.8/9.1; 2.6-fold | match | t45, t47; 23.8/9.1 = 2.62 (inference, marked). |
| 14 | Moses no-LM 60.5% vs 25.6% | match | s10. |
| 17 | 23.8 to 17.4 (27% relative); 11.8% | match | t49, t50; (23.8-17.4)/23.8 = 0.27. |
| 19 | 30 minutes on day one; session 84 | match | s4, s5. |
| 20 | 260–480 sentences; 140 min; 30% WER | match, missed point | t16, t18, t30; the target gives 260–440 sentences per day in Sec. 4 (t85), an internal inconsistency the review should state. |
| 22 | 2.7x vs another participant and sensor; 3.4x vs handwriting | match | t3, t5, s9, s11. |
| 23 | Checkpoint chosen on the "test" partition in released code | match | q1, q2, q3; scope limited to offline code, online selection unstated (u2). |

Positions: M05, M06, M07 standard are carried by the Appendix counts and the [later] state of the art; M12 not reported is carried by u1, u2, u4. The Verdict's "overreach" on spiking resolution is carried by s6 with the vocabulary qualification in M05.

Required fixes, by impact:
1. State the 260–480 vs 260–440 sentences-per-day inconsistency (Sec. 3 vs Sec. 4).
2. Reword the M06 line of the Verdict so CTC is not attributed to the handwriting BCI.
