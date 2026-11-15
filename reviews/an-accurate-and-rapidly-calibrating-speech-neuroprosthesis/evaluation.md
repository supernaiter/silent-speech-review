Evaluator: a language model separate from the writer

Date: 2026-11-15. Input: evaluator brief and `reader/compact.md` only (review body, references, claim table). No sources reopened, no search. Scope: (a) does each claim match its quoted source line, (b) does any position go beyond its evidence.

## Claim check

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | T12 23.8% WER at 125k words [1]; target 2.5% WER in final 5 Copy Task sessions | Row 1 (w1, t8) | correct | Numbers match. But the causal framing "together they move ... from 23.8% to 2.5%" goes beyond the evidence (see Fix 1). |
| 2 | 9.8% WER on 125k after about 473 sentences (213+260); comparable to one T12 day | Row 2 (t6, c1, c2, w3) | correct | Sum and 260–480 range match; inference is labelled. |
| 3 | Abstract 97.5% "for conversations" equals 100 − 2.5 (inference); conversation WER 3.7% in "selected" sessions; references partly reconstructed afterwards | Row 3 (t3, t8, t11, t49) | correct | All quotes match. The equivalence is labelled inference; the "strongest overreach" label is reasonable given 3.7% ≠ 2.5%. |
| 4 | 8.4 months, 248.3 h, 22,679 sentences; single participant caveat | Rows 4, 15 (t13, t45) | correct | Quote also says 72 of 84 sessions; fine. |
| 5 | T12 260–480 sentences/day, 10,850 by last day; ECoG about 1.6 h/day over 13 days | Row 5 (w3, w4, m1, m3) | correct | Matches. "Daily recalibration" as the default for [2] is not in the quote, but is a minor framing. |
| 6 | "This paper shrinks it to 213 sentences (30 min), then 260 more (1.4 h)" | Row 6 (c1, c2, t2) | wrong (framing) | Counts match, but 473 sentences sits inside T12's 260–480 per day, which the Verdict itself calls "comparable to one day". The data quantity is not shrunk; the WER reached at that quantity is lower (Fix 2). |
| 7 | 9.8% (95% CI 4.1–16.0) vs 23.8%, 59% lower; recalibrations 7.5 min, 20 sentences | Row 7 (t6, w1, t15) | correct | (23.8 − 9.8)/23.8 = 58.8% → 59%. Session-2 value vs T12's multi-day average; the confound is stated in the next paragraph. |
| 8 | [3] recalibrated a handwriting iBCI from pseudo-labels over 403 days; [4] six commands, 3 months, no open vocabulary | Row 8 (p1, p2, l1–l3) | insufficient evidence | 403 days, CORP, six commands, 3 months match. "Handwriting" is not in any quoted line (Fix 8). |
| 9 | Half of T12's arrays in Broca's area; authors' data-reduction claim is cross-study | Row 9 (w6, t37) | correct | Area 44 is part of Broca's area; quote supports. |
| 10 | Intracortical in 67 of 72 slot-filled studies (75 unique, pattern match) | Row 10 (tally only) | insufficient evidence | No quote. Mixes slot-filled and pattern-match denominators; Appendix row 29 gives slot-filled 7,329, so "72 slot-filled" needs explaining. Also near-circular for an intracortical-speech topic (Fix 10). |
| 11 | Keeps T12's four arrays but puts all 256 electrodes on precentral gyrus, incl. area 4 and 55b | Row 11 (t23, t23b, c4, t38, w6) | insufficient evidence | Four arrays, 256 sites, area 4 supported. "55b" and "all on precentral gyrus" are not in any quoted line (Fix 7). |
| 12 | 2.5% online WER is the lowest large-vocabulary value among ledger candidates | Row 12 (t8, audit) | correct as scoped | Scoped to the ledger; acceptable. |
| 13 | [later] ensemble lowers offline WER on T15 by 35.0% relative across seeds; "later gains come from the decoder" | Row 13 (y1, y4, y5) | number correct; position wrong | 35.0% (T15) matches; T15 = this participant is labelled inference. "Later gains come from the decoder" generalises from one offline study whose own Discussion says ensembles were not tested in real time; a relative offline reduction is not comparable to the online 2.5% (Fix 3). |
| 14 | 39 unique; 21 of 31 implemented and evaluated; 2 deployed | Row 14 (tally) | correct as tally | No quote needed beyond Appendix. |
| 15 | Researcher launched every session | Row 15 (t47) | correct | "Every" is a mild extrapolation of "assistance was required to connect and launch". |
| 16 | [4] 90.59% median, six commands, 3 months; "this paper extends it to open vocabulary" | Row 16 (l1–l3, t47) | partly wrong | Numbers match. "Extends" omits that [4] ran without recalibration while this paper recalibrated (7.5-min calibrations, row 7). It extends vocabulary and duration, not recalibration-free stability (Fix 4). |
| 17 | Usual evaluation: online WER on prompted held-out sentences [1], [2] | Row 17 (w1, m2) | correct | Metzger 25% median WER at 78 wpm matches. |
| 18 | [5] reports WER across training seeds; main text reports no training seeds | Row 18 (y3, t55) | insufficient evidence | y3 supports seeds in [5]. The absence in the target is asserted; t55 (bootstrap CIs) does not demonstrate it. Plausible, but unquoted. |
| 19 | Day-1 99.6% is a 50-word result vs T12 9.1% at 50 words | Row 19 (t1, t4, w2) | correct | 100 − 0.44 = 99.56 ≈ 99.6. |
| 20 | M12 verdict "not reported" for evaluation-set sizes and session selection | Row 19 (t54, t57), row 20 (t11) | partly insufficient | "Selected" sessions supported by t11. No quote shows that evaluation-set sizes are absent (Fix 9). |
| 21 | Participant rated only 52.9% of Conversation sentences fully correct | Row 20 (t12) | correct, one-sided | Same quote gives 32.3% "mostly correct"; omitting it tilts the point (Fix 13). |
| 22 | References partly from asking afterwards; "errors he does not recall leave the WER" | Row 3 (t49) | position beyond evidence | First half supported; the bias mechanism is unlabelled inference (Fix 5). |
| 23 | ~5% WER commercial ASR, 1–2% able-bodied; comparisons cross tasks | Row 21 (t41, t42) | correct | Quotes match. |
| 24 | Authors caution about one participant; "title and conclusion read more generally" | No claim-table row for the second half | insufficient evidence | Caution is supported (t45). Title/conclusion wording is neither quoted nor located (Fix 6). |
| 25 | Reference list labels | References | wrong | [6] is the target itself yet carries "[concurrent]" (Fix 11). [3] (NeurIPS Dec 2023) and [4] (Adv. Sci. 2023) as [concurrent] against an April 2024 preprint are consistent, and neither is treated as prior work. |

Central claim and strongest confound: the move from 23.8% [1] to 2.5% crosses participant (T12 vs T15), array placement, language-model stack (M07) and, above all, training-data quantity: the 2.5% comes from the final sessions after months of accumulated data, not from the 473-sentence calibration. The M03 paragraph names the participant, placement and LM confounds. The Verdict's "together they move" does not name accumulated data and credits M13 (home use) with a WER change it cannot cause.

## Required fixes (by impact)

1. Verdict: replace "together they move online large-vocabulary decoding from 23.8% to 2.5%" with a non-causal statement. Name accumulated training data and the LM stack as confounds next to participant and placement. Home use (M13) does not lower WER.
2. M03 usual approach: drop "shrinks it". 473 sentences falls within one T12 day (260–480), as the Verdict says. The advance is the lower WER at a similar quantity, and that comparison crosses participants.
3. M05 state of the art: remove or hedge "later gains come from the decoder". [5] is one offline study, untested in real time (y5), and reports a relative reduction that cannot be ranked against an online absolute WER. Give [5]'s absolute WER, or state that it is not comparable.
4. M13 state of the art: "extends it to open vocabulary" should add that [4] needed no recalibration for 3 months, while this paper recalibrated (7.5 min, 20 sentences). The extension is in vocabulary and duration, not in recalibration-free stability.
5. "Errors he does not recall leave the WER": label as inference, or rephrase as "may bias WER downward".
6. "Title and conclusion read more generally": add a claim-table row quoting the title and conclusion wording, or cut the clause.
7. M05: "including area 4 and 55b" and "all 256 electrodes on precentral gyrus" need quoted support (55b and the precentral location of each array are not in rows 11 or 22).
8. M03 state of the art: "handwriting iBCI" for [3] needs a quoted line.
9. M12 verdict: add a quote or location showing that evaluation-set sizes are not reported, or narrow the verdict to session selection, which is supported.
10. M05 usual approach: reconcile "67 of 72 slot-filled" with Appendix "slot-filled 7,329". Note that intracortical dominance is near-tautological for an intracortical speech topic; array count or placement would be the informative usual design.
11. References: remove "[concurrent]" from [6], which is the target.
12. Component table: M13 lists [4] as the state of the art, while the text calls this paper's home use the main advance and says it extends [4]. Align the two.
13. Overreach bullet 1: report 52.9% correct and 32.3% mostly correct together.
14. M08 (state of the art "–"): consider [later] Wairagkar et al. 2025, *Nature*, an instantaneous voice-synthesis neuroprosthesis in the same participant. This is from the evaluator's own knowledge, unverified here, low-medium confidence.

## Scores

- Procedure: 7/10. Each number has a quote and location, inferences are mostly labelled, and the arithmetic is correct. Several locator-level claims (55b, handwriting, title/conclusion, absence of set sizes) lack quotes.
- Final text: 6/10. Numbers are accurate. The Verdict's causal sentence, "shrinks", "later gains come from the decoder" and "extends" each state more than the cited evidence carries.

Brief note on strengths: comparator numbers are faithfully quoted, the 59% calculation is right, the 97.5% vs 3.7% point is well supported, and chronology labels for [3] to [5] are consistent.
