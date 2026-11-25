# Evaluator: a language model separate from the writer

Date: 2026-11-25. Target: Kumar et al., "Lipper: Synthesizing Thy Speech using Multi-View Lipreading", AAAI-19, arXiv:1907.01367.
Inputs: `compact.md` (review plus claim table), checked against `notes.json` entries (target t*, comparators k*/p*) and `prep/audit/M06-video-to-speech-synthesis.audit.json` (Table IV rows of [7]). Web sources were not re-opened; outside knowledge I could not locate is marked "unverified".

## Claim table

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper changes M05 (up to 5 views, pose classifier) and M06 (STCNN+BiGRU to LPC/LSP) (Verdict) | t7, t12, t13, t14 | correct | |
| 2 | LPC/LSP target is "the Vid2speech route [3]" (Verdict) | claim row 2 quote p11 | insufficient quote | Claim-table quote for [3] is "23 different MTurk workers"; the LPC/LSP fact sits in the p11 note text (8th-order LPC/LSP), not in a quote. |
| 3 | [2] labelled [concurrent] yet used as the prior that makes M05 `standard` (Verdict, M05) | t130, k1, reference list | wrong label / inconsistency | The target cites [2] as Kumar et al. 2018a in Related Work (t130); same authors. It is the authors' own read prior, not concurrent work. |
| 4 | +15.6% speaker-dependent, +2.1% / +5.7% held-out (Verdict) | t29, t47, t77, t111 | correct | 2.315/2.002 = 1.156; 1.94/1.90 = 1.021; 1.86/1.76 = 1.057 (inference, matches). |
| 5 | Best combination chosen on the speaker-dependent results it is reported on; no validation set (Verdict, Overreach) | t101, t131, t17 | correct | Supported as stated, and correctly marked as inference for "optimistic". |
| 6 | "real-time ... claims are unsupported" (Verdict) and "a delay constant over length is per-window, not end-to-end (inference)" (Overreach) | t4, t82–t86, t107, t133 | judgment exceeds evidence | Notes record Table 11 as end-to-end phrase delays. A constant latency is what a streaming system that "begins to produce audio as soon as it detects lip movement" (t4) would show, so the per-window reading is one possibility, not a finding. Evidence supports "not established (hardware and timing end points unstated, t107)", not "unsupported". |
| 7 | Speaker-independence claim conceded as weak; two speakers, one per gender (Verdict, Overreach) | t80, t81, t97, t18 | correct | |
| 8 | M05 usual approach 693 of 787; 20 of 165 multi-view (M05) | Appendix, row 29–30 | correct (internally consistent) | 787 − 94 = 693. |
| 9 | 2.315 vs 2.002 frontal, speaker-dependent (M05 SOTA) | t47, t29 | correct | |
| 10 | Hush-Hush Speak 1.964 vs 1.920, +2.3%, 85:10:5 split (M05 SOTA) | p20, p22, p7, p24 | correct with caveat | Arithmetic right. Hush-Hush uses digits and phrases and does not state speaker separation of the split (p24); the review's table cell "held-out" is right, but neither number is directly comparable to Lipper's 2.315. |
| 11 | Held-out: 0°+45° (2.03, 1.85) matches or beats triple (1.94, 1.86) (M05) | t78, t111 | correct | Female speaker: triple 1.86 > 1.85, so "matches or beats" is accurate; "does not transfer" is strong for a 0.01–0.09 PESQ difference on two speakers with no repeats. |
| 12 | All five views 2.086, below the triple (Table 8) (M05) | t64, t65 | correct number, misplaced | This is a speaker-dependent result and the authors' own statement (t65); it does not support "does not transfer". The held-out five-view row (1.91, 1.83; t113) is the relevant one. |
| 13 | [4] ran 10 repetitions with significance tests; target reports no repeats (M05) | p9, p17, t99, t104 | correct | |
| 14 | M06 usual approach: 49 neural, 41 parametric of 165 (M06) | Appendix, row 34 | correct (as tally) | 49 vs 41 is near parity; "usual" is weak but stated with counts. |
| 15 | Regression from video predates the target [3][6] (M06) | t1, t31, t105 | correct, fairness note | The target itself compares with Ephrat and Peleg in Table 4 and frames regression against text lipreading, not against video-to-speech; the review should not present the precedence as an overlooked fact. |
| 16 | GRID seen speakers: lowest ASR WER 4.07% at PESQ 1.76, end-to-end WGAN (2022) (M06 SOTA) | p27; M06 audit Table IV rows (VCA-GAN 5.62, "+ basic fine-tuning" 4.54, Vid2Voc 9.29) | correct | Lowest among the rows available to me. Reference [7] says "Read as arXiv v1; Table VII" while this number is Table IV: locator note incomplete. Whether a later GRID-4 result is below 4.07% is unverified. |
| 17 | M12 usual approach: 83 listener test, 51 unseen-speaker, 38 ASR WER (M12) | Appendix, row 38 | correct (as tally) | |
| 18 | Listener test: 4 options, chance 25%, 80.25% (M12) | t87, t89, t91, t126 | correct but incomplete | The audio-visual study (10 classes, chance 10%, 81.25%; t88, t90, t125) is omitted. |
| 19 | PESQ misjudged noisy samples (M12) | t92; claim row 15 | correct; insufficient quote | Claim row 15 is a truncated fragment ("User-Study) [1].") with the quote "not always perfect."; the t92 note carries the meaning. |
| 20 | GRID unseen: 16.05% WER (M12 SOTA) | p14 | correct | Different corpus (GRID vs OuluVS2); review does not claim a gap, which is fair. |
| 21 | "Four earlier systems measured intelligibility directly ... None of these measures appears in the paper" (M12) | p29–p32, p13, t87–t93 | partly wrong | Vid2speech [3] used closed-set word classification by listeners (p29), the same family as Lipper's closed-set phrase identification (t126), which the authors present as their intelligibility evidence (t93). A listener intelligibility measure does appear in the paper. Only STOI/ESTOI, ASR WER and open transcription are absent. |
| 22 | Verdict M12 `behind` against Lip2AudSpec [8] (M12) | SKILL.md `behind` rule; p30, p32, p13 | rule met only narrowly | Rule needs ≥3 earlier ledger papers meeting a condition the target does not. With [3] excluded (finding 21), [8], [9], [6] remain; [6]'s listener protocol (open vs closed) is not quoted. The condition must be stated precisely (e.g. "open transcription, STOI/ESTOI or ASR WER"). Also, on a 10-phrase corpus open transcription is nearly closed-set, which weakens the practical gap. |
| 23 | Text accuracy 97.0 vs 95.6 random split; 78.5 speaker split; authors concede (Overreach) | t23–t26, t102 | correct | Review correctly credits the concession. |
| 24 | Language independence only via speaker-dependent demos (Overreach) | t94 | correct | |
| 25 | M13 `not reported` (13-components table) | t96, t107, Table 11 | acceptable | A delay is reported (0.169 s) but its hardware and end points are not; "not reported" is defensible for hardware/cost, but the cell could say "0.169 s delay, hardware unstated". |

## Numbered findings, ordered by impact

1. **M12 "None of these measures appears" is partly wrong and the `behind` verdict is fragile (claims 21, 22).** Lipper's audio-only and audio-visual phrase-identification studies are listener intelligibility tests of the same closed-set family as Vid2speech's word classification [3]. Fix: drop [3] from the list of measures the paper lacks, name the missing measures exactly (open transcription, STOI/ESTOI, ASR WER), confirm that [8], [9], [6] meet that condition (quote [6]'s listener protocol), and say the yardstick is "best comparable work".
2. **"Real-time ... unsupported" overstates the evidence (claim 6).** A constant 0.169 s delay is consistent with the streaming behaviour the authors describe (t4); the per-window reading is inference. Fix: "real time is not established: Table 11 gives no hardware or timing end points (t107), and the comparator delays were not measured under stated common conditions". Keep the per-window point only as a question.
3. **[2] labelled [concurrent] while serving as the deciding prior for M05 `standard` (claim 3).** The target cites it in Related Work (t130) and shares authors. Fix: label it as prior (the authors' own 2018 system), or, if it stays concurrent, do not use it to make the M05 contribution standard.
4. **The audio-visual user study is omitted (claim 18).** Table 12 also reports 81.25% with 10 choices (chance 10%). Add it; it is the harder of the two tests and bears on the M12 judgment.
5. **Table 8 (2.086) is cited as evidence of non-transfer (claim 12).** It is speaker-dependent and the authors state it themselves (t65). Replace it with the held-out five-view row (1.91, 1.83; Table 10), which still sits below the triple, and soften "does not transfer" to "is not clearly best on the two held-out speakers".
6. **Hush-Hush Speak comparison condition (claim 10).** State in the M05 text that Hush-Hush uses digits plus phrases and does not describe speaker separation (p24), so 1.964 and 2.315 are not on one protocol.
7. **Fairness on regression precedence (claim 15).** The authors compare with Ephrat and Peleg in Table 4; rephrase so the review does not imply they hid the precedent (their "departure" is from text lipreading).
8. **Claim-table quality (claims 2, 19).** Row 2 needs a quote for Vid2speech's LPC/LSP target; row 15 is a truncated sentence fragment with a thin quote. Insufficient quote, not wrong.
9. **Reference [7] locator (claim 16).** The note says "Table VII" only, but the M06 number is from Table IV. Add Table IV.
10. **M13 cell (claim 25).** Consider noting the reported 0.169 s delay with hardware unstated, so the cell is not read as "no timing given".

## Strongest confound
Speaker-dependent vs held-out evaluation (different starting points, 2.002 vs 1.90/1.76 frontal), compounded by view selection on the reporting split. The review handles it well (Verdict, M05, Overreach). The second confound, corpus mismatch for the M06/M12 state of the art (GRID vs OuluVS2), is acknowledged ("the gap is unknown").

## Absence and novelty claims
No "first / only" claims. The one absence claim (finding 1) is the weak point.

## Scores
- Procedure: 7/10 (numbers trace to notes, arithmetic correct, inference marked; claim-table rows 2 and 15 weak).
- Final text: 6/10 (sound central critique of view selection and speaker independence; the M12 `behind` and the real-time judgment go beyond their evidence).

Strengths (brief): the Verdict arithmetic on held-out gains is correct and makes the main point concisely; the selection-on-test critique is well grounded (t101, t131); the text-accuracy overreach correctly credits the authors' own concession.
