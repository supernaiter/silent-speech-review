# Evaluator: a language model separate from the writer

Date: 2026-11-24. Inputs: `references/evaluator-brief.md` and `compact.md` (review plus claim table). No other writer files and no source text were opened. Every check below rests on the claim-table quotes and locations. Where a quote is thin, the finding says "insufficient quote", not "wrong" (brief, rules 2 and 6).

## Claim table

| No | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Test MSE 0.293 / 0.282 / 0.276; 5.8% and 2.1% relative (Verdict) | Claim rows 1, 11 (Table 2 quotes) | correct | The quotes give the test column. (0.293-0.276)/0.293 = 5.8%; (0.282-0.276)/0.282 = 2.1%. Marked (inference). |
| 2 | "unidirectional" ConvLSTM (Verdict, M06) | Claim row 1 | insufficient quote | No quote shows the direction. It matters because the review's M13 streaming point (row 25) depends on it. |
| 3 | Dropout raised 0.3 to 0.35 and a different pooling window (Verdict, M06, Claims section) | Claim rows 2, 11, 19, 28 | insufficient quote | Only `Dropout(0.35)` is quoted. No quote gives the baseline's 0.3 or either pooling window. This confound carries the M06 position, so it needs quotes. |
| 4 | Two Conv3D plus two ConvLSTM give 0.35, worse than 0.293 (M06) | Claim row 12 | correct, with a caveat | The numbers match. The comparison spans Table 3 (2 decimals) and Table 2 (3 decimals). Same training setup is assumed but not shown. |
| 5 | "Placement matters more than layer type" (M06) | Claim rows 12, 28 | judgment stronger than evidence | It rests on single-run Table 3 cells that differ by 0.01–0.08. Under the review's own single-run objection, this ranking is no firmer than the 0.006 gain it rejects. |
| 6 | 9 ConvLSTM matches among 148; none an earlier speech-output study (Verdict, Appendix) | Appendix M06 table 2 | correct as an internal tally | The deciding prior [6] is named. The 2022 review is not named. The target and its thesis are listed as two hits, which fits poorly with "versions counted once". |
| 7 | Usual approach M06: "Frame-wise regression with DNN (37) or CNN (31)" | Appendix M06 table 1 | partly unsupported | The Appendix counts architecture names. It does not count frame-wise regression. "Frame-wise" is the reviewer's interpretation and should be labelled that way or dropped. |
| 8 | SOTA M06: Tongue2Speech, 3D front end plus multi-layer Transformer, 15.93% vs 24.15%, single-speaker TaL1 [3] | Claim row 8 | numbers correct; design and corpus have insufficient quote | 15.93% and 24.15% are quoted. "3D front end", "multi-layer", "single-speaker" and "TaL1" are not. |
| 9 | [2] lists ConvLSTM but applies the 3D-CNN (M06) | Claim rows 3, 13 | insufficient quote | The quote "CNN architecture introduced by" is cut off before the cited work. It does not show that [2] mentions ConvLSTM. |
| 10 | Tongue2Speech mentions "ConvLSTM hybrids" only in related work (M06) | Claim row 13 | insufficient quote | The phrase "ConvLSTM hybrids" is not in any quote. The quote "six baselines" does not show that none of them is a ConvLSTM. |
| 11 | Usual approach M12: MCD 21/51, "often with MUSHRA (14)" | Appendix M12 table | count correct; wording unsupported | The tally gives no co-occurrence of MCD and MUSHRA. "Often with" claims a co-occurrence the counts do not show. |
| 12 | [7] 23 listeners, [8] 24 listeners on the same 310/41/87 split (M12) | Claim row 15 | partly supported | 23, 24, 41 and 87 are quoted. 310 is not quoted for [8], and the target's own split (M11) has no quote at all. |
| 13 | [4] MUSHRA "over four speakers"; "the same mel-plus-WaveGlow pipeline" (Verdict, M12) | Claim rows 4, 17 | insufficient quote | Only "online MUSHRA-like test" is quoted. Four speakers and a mel-to-WaveGlow setup in [4] are not quoted. [4] uses a different network, so "the same pipeline" applies to the synthesis stage only. |
| 14 | SOTA M12: 31.64% multi-speaker; MSE-type metrics are "weak indicators" [3] | Claim row 16 | 31.64% has insufficient quote | "Weak indicators of lexical accuracy" is quoted. No quote gives 31.64%. |
| 15 | Tongue2Speech: 3D-CNN without temporal aggregation 99.26 to BiLSTM 36.46 WER; session spread 9 points (M12) | Claim row 18 | insufficient quote | The quoted row is "Overall 99.26 1.819 99.08 1.877 60.29 1.417 99.26 3.155 36.46". It has no column headers, and 99.26 occurs twice. Which column is "3D-CNN without temporal aggregation" cannot be checked. The 9-point spread is quoted. |
| 16 | Sec. 2 "much fewer parameters" vs Sec. 5 "much more trainable parameters" (Claims section) | Claim row 20 | likely misread (insufficient quote) | The Sec. 2 phrase sits in related work and most likely compares ConvLSTM with a fully connected LSTM. Sec. 5 compares ConvLSTM with Conv3D. These are two different baselines, so the two statements may not contradict each other. |
| 17 | "No count or time is reported"; "no parameter count" (Verdict, M06, Claims section) | Claim rows 11, 27 | correct, with an omission | The review leaves out the authors' statement (row 27, t64, Sec. 5) that layer sizes were "chosen so that the global count of the free parameters stayed similar". This partly answers the parameter confound and works against "smaller". The review should mention it. |
| 18 | The authors' own caveat: the variant "tremendously increased the number of parameters while yielding only a marginal improvement" (Sec. 5) | Claim rows 1, 25 | missed caveat; quote misused | The authors state this caveat themselves, and the review never names it. Row 25 cites this quote for the streaming suggestion, but the quote does not support that suggestion. |
| 19 | Intro promises a 2D-CNN+LSTM comparison; Table 2 has none (Claims section) | Claim row 21 | insufficient quote | The quoted phrase may describe earlier work rather than promise a comparison in this paper. More context is needed. |
| 20 | Baseline retrained with Adam instead of SGD; [5] predicted vocoder parameters (Claims section) | Claim row 22 | partly supported | The Adam switch is quoted. That [5] predicted vocoder parameters is not quoted. |
| 21 | Scan line 946 vs 964 (Questions section) | Claim row 29 | correct | Both numbers are quoted from Sec. 3. This is a valid internal inconsistency. |

## Numbered findings (ordered by impact)

1. **The M12 "behind" verdict only partly meets the rule as the brief states it.** The brief states the rule only for `ahead`: a ledger count in the Appendix, the deciding priors named, and the effect repeated. Applied by analogy to `behind`:
   - (a) Ledger count: met. The Appendix M12 table gives 51 studies, 14 with MUSHRA, and 10 of 31 dated before 2021-12.
   - (b) Deciding priors named: met. [7], [8] and [4] are named, and all predate the target, so the verdict does not lean on the later [3].
   - (c) Effect repeated: not met. Nothing shows that the missing listening test changes a conclusion. The only support is a cross-paper analogy from [3]: a column-ambiguous WER row (finding 6) comparing a 3D-CNN with and without any temporal layer. That is a far larger change than ConvLSTM vs BiLSTM.
   - (d) Two counter-points are not addressed. MUSHRA appears in only 14 of 51 studies (10 of 31 before 2021-12). So listener testing is a minority practice, and the target trails it, not the usual approach. Also, the target's closest comparable study, its own predecessor [5], appears from claim row 7 to report only MSE and R² as well. The review does not say whether [5] ran a listening test.
   - Required fix: (i) say "behind the group's own listener-tested studies [7][8][4]" and drop "best comparable work", or justify why vocoder and DNN papers are the comparable set for an architecture ablation; (ii) state the [5] counter-example; (iii) note that MUSHRA is a minority practice (14/51) and that the target also lacks MCD, the usual measure (21/51). With these changes "behind" can stand. As written, it is stronger than its evidence.

2. **The central confound for M06 is not supported by quotes.** Dropout 0.3 vs 0.35 and the pooling change appear three times and drive the M06 position. Only `Dropout(0.35)` is quoted. Add the Table 1 baseline cells, or soften the claim.

3. **The authors' own caveat is missed and its quote is misused (finding 18).** Sec. 5 reports that a ConvLSTM variant "tremendously increased the number of parameters while yielding only a marginal improvement". This is the authors' own limitation, and the review should name it. It is not evidence for the streaming suggestion (row 25).

4. **The parameter "contradiction" in the Claims section may be a misreading (finding 16).** Check whether the Sec. 2 "much fewer parameters" compares ConvLSTM with a fully connected LSTM. If it does, delete the contradiction. Keep only the point that "smaller and faster" (Abstract) has no measurement.

5. **The authors' statement that parameter counts were kept similar (Sec. 5) is left out (finding 17).** "No parameter count" is literally true, but the review should mention the authors' statement, which partly answers the confound.

6. **The Tongue2Speech 99.26 to 36.46 WER comparison cannot be checked (finding 15).** Quote the column headers of [3] Table 1. As written, the M12 argument rests on an unlabelled row in which 99.26 appears twice.

7. **The "placement matters more than layer type" claim is stronger than its evidence (finding 5).** It rests on single-run cells with 2-decimal precision, which is the same weakness the review uses to reject the authors' claim. Hedge it, or move it to Questions.

8. **The later-work claims are thinly quoted (findings 9, 10).** No quote shows that [2] mentions ConvLSTM, or that [3] mentions "ConvLSTM hybrids" only in related work. The Verdict sentence "did not carry forward" rests on these.

9. **The M12 table cell and the M06 state of the art use different headline values from [3].** M06 uses 15.93% single-speaker; the M12 row uses 31.64% multi-speaker, which has no quote (finding 14). Pick one with a reason and quote it.

10. **The usual-approach wording goes beyond the counts (findings 7, 11).** "Frame-wise regression" and "often with MUSHRA" describe what the tallies do not count. Label them as inference or drop them.

11. **The [4] details have insufficient quotes (finding 13).** "Over four speakers" and "the same mel-plus-WaveGlow pipeline" need quotes. [4] used a different network, so say "the same WaveGlow synthesis stage".

12. **The split and the [5] output type are not quoted (findings 12, 20).** 310/41/87 for the target and for [8], and "vocoder parameters" for [5], need quotes.

13. **The novelty claim "new to ultrasound-to-speech mapping" is unverified from outside knowledge.** I cannot name an earlier ultrasound-to-speech study that uses ConvLSTM. The 2022 review counted among the ConvLSTM hits should be named, so readers can see that it is not prior work. Counting the target and its thesis version as two hits fits poorly with "versions counted once" (finding 6).

14. **The M06 "standard" verdict follows the rule.** The layer is new, but the effect is a single run, single speaker and confounded, and no later work repeats it. Withholding `ahead` is correct. No fix needed.

15. **Fairness is handled correctly.** [2] and [3] are tagged [later]. They are used only as later context and as the state of the art, never as missed prior work. The relative changes are marked (inference). No fix needed.

## Scores

- Procedure: 7/10. The ledger counts, named priors and chronology labels are in place. Several decisive claims have missing or thin quotes.
- Final text: 6/10. The position is clear and mostly fair. The M12 "behind" verdict and two M06 sentences go beyond their evidence, and one claimed contradiction may be a misreading.

Strengths, briefly: the review gives a clear single-component position. It uses relative-change arithmetic correctly, catches the 946/964 inconsistency, and keeps later work out of the prior-work judgment.
