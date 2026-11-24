# Triage: LipLearner (evaluation of 2026-11-24, 15 required fixes)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | SKILL.md rule for ahead: the effect of the design must be shown with repetition. The 1,000 draws and 11 speakers show few-shot accuracy, but the only comparison is the from-scratch counterpart (q3a, q2f). No ablation of the head or the encoder exists (q2e). The logistic head is adopted from the cited few-shot literature (n6). The rule is not met, so the verdict is downgraded to standard. | Verdict; M03 section; slots M03; verdict.short |
| 2 | applied | The published table's inclusion rule excludes overt-only training tested on silent speech (Appendix). Voice2Lip is that case at one shot and then pools silent shots (t7, q6e). | M01 usual approach |
| 3 | applied | The 3 of 183 count shows KWS activation is new for interfaces. Benefit over mouth-opening activation is never tested (n7), so the verdict stays standard under "difference not supported". [3] (wake words) now leads the state-of-the-art line. | M06 state of the art and closing sentence |
| 4 | applied | The rows are different variants: cl−r is a plain classifier on real data and ve−r+s+aug uses VE with real, synthetic and augmented data (p9, p10). | M03 usual approach |
| 5 | applied | Sec. 4.4 "trained the model solely on normal speech" (n2) and the Table 1 header (n3). The 9.97% model uses silent data, and the task is 10 phrases (c4). | M01 state of the art |
| 6 | applied | The protocol is test-then-update (q7a–q7c). Rephrased as a same-session loop, not held-out sessions; the leakage implication is removed. | M12 |
| 7 | applied | Sec. 5.4 "forming a 6-shot training dataset" (n1). | M12 |
| 8 | applied | t48 quote (≈422 ms, iPhone 13 Pro). Claim-table row 52 added. | claims.md |
| 9 | applied | Transpotter Table 1 header (n4): the value is mAPCls on LRS2. Stafylakis Table 1 is titled Equal-Error Rates (n5), and LRS2 is quoted in k3. "LRS2" was dropped for [3] because its quote does not state it. | M06 state of the art |
| 10 | applied | The target's EER is one-vs-rest within a closed enrolled set (q5c). The "same order" comparison is replaced by "not comparable". | M06 |
| 11 | applied | t4 (claim limited to interfaces); t68 (authors concede the threshold limit). | M06 |
| 12 | applied | Within-user training: t16, t42. No chance level: t20 (unstated). | M12; claims row 24 |
| 13 | applied | t7 is Sec. 1. Voice2Lip is now defined in the M01 usual approach, cited to §1. | M01 |
| 14 | applied | "One participant" is not in a quote, so it was dropped. "Recorded in a one-shot manner" is quoted (n8). | Where the claims outrun the evidence |
| 15 | applied | The noun was added ("[concurrent] [8]"). "LRW" was dropped for Feng et al.'s weights (q2a). The 8.5% is now attributed as reported by [9] for [10] (c2). | M01; M03 |
| A | rejected (part of 1) | The evaluator's alternative of narrowing the verdict to "ahead for on-device" is not taken: on-device speed alone is not a design difference measured against the field. | – |
| B | unverified | Linear evaluation is standard in self-supervised learning (SimCLR). This is outside the notes and is not stated; the review says only that the head comes from the cited few-shot literature. | verification_status |
| C | unverified | Later visual or audio-visual KWS work may exceed Transpotter. No such paper was read; it stays in verification_status. | verification_status |

Counts: 15 applied, 1 rejected (alternative wording in finding 1), 2 unverified (outside-knowledge remarks).
