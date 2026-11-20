# Evaluation: End-to-end Silent Speech Recognition with Acoustic Sensing

Date: 2026-11-20. Fallback evaluator (claim table only). Input: compact review, its claim table and the evaluator's own background knowledge. No sources were reopened, so items marked "insufficient evidence" mean the claim table does not carry the claim. They do not mean the claim is false.

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target uses carrier phase on 8 tones instead of Doppler (Verdict, M05) | Row 1, 5 (t8, t2, t7) | correct | 8 channels, 700 Hz spacing, 17–23 kHz and "instead of Doppler shift" are all quoted. |
| 2 | Attention decoder chosen over CTC, attention better (Verdict, M06) | Row 1 (t48) | correct | The authors themselves say the gap is largest in domain-independent tests. |
| 3 | "speaker-independent and environment-independent" 8.4% WER (Verdict) | Row 3 (t41) | insufficient evidence | 8.4% is quoted, but the quoted phrase is not in the claim table. The review never says what a "domain" is (user, environment or both). |
| 4 | Tuning used the random split, which includes held-out users (Verdict, M12) | Row 3, 18 (t85, t37) | correct (inference) | Validation was a random 10% of the whole dataset, so it covers every user. The inference holds. |
| 5 | 54 sentences, 29 words (Verdict, M11) | Row 3 (t19, t20) | correct | |
| 6 | Raw phase 32.1 worse than Doppler 29.4. Phase delta + double-delta 11.2. 62% relative (M05) | Row 9 (t29, t30, t32) | correct | (29.4 − 11.2) / 29.4 = 61.9%. |
| 7 | "only phase got deltas (Table 2)" (M05) | Row 9 | insufficient evidence | No quote lists all rows of Table 2. |
| 8 | Doppler usual, 16 of 28 studies (M05) | Row 4, 24–26 | insufficient evidence | The Appendix gives a pattern-match denominator of 22, and 28 appears only in a truncated line. M12 uses "of 22" for the same field, so the denominators need reconciling. |
| 9 | [4] used a 40 kHz emitter-receiver pair and reached 70.5% WER on clean digits from ultrasound alone (M05) | Row 4, 8 (c7) | insufficient evidence | c7 is a bare table row ("Clean 1.0 0.32 70.5 0.24"). The quote does not show that 70.5 is the ultrasound-only column. Nothing is quoted for 40 kHz. |
| 10 | SOTA M05: [5] reaches 26.3% WER open vocabulary, 5,356 word types, one speaker (M05) | Row 6 (c10, c12, c13) | partly correct | The numbers match the quotes. However, [5] is a tri-modal dataset paper, and the quote does not show that 26.3% comes from the acoustic FMCW channel alone. It is also a dataset baseline, not a tuned best system. |
| 11 | No other ledger study uses carrier phase; later work moved to FMCW (M05) | Row 7, 25 | insufficient evidence | The sentence names no deciding prior. Multi-carrier I/Q phase tracking at 17–23 kHz on phones predates the target in gesture sensing (LLAP, Wang et al., MobiCom 2016; Strata, Yun et al., MobiSys 2017). So the design is new for speech, not new as sensing. |
| 12 | Usual M06: hybrid CTC/attention, 79 of 132 (M06) | Row 10, 30–32 | insufficient evidence | The Appendix gives "pattern match 114" and "over 132 studies" for the same slot. Also, a pattern count of the phrase measures mentions, not use. "Studies that name both decoders mostly combine them" goes further than that. |
| 13 | Hybrid CTC/attention used for lip reading in 2018 [3] | Row 10 (c4) | correct | SLT 2018 comes before the target (arXiv Nov 2020). |
| 14 | [2] Transformer 50.0% vs best CTC 55.0% WER on LRS2, 9% relative | Row 11 (c1) | partly correct | 50% is quoted. 55.0% is not quoted. (55 − 50) / 55 = 9.1% is right if 55.0 holds. |
| 15 | [2] gives the same internal-LM explanation | Row 11, 13 (c2, t55) | correct | |
| 16 | Target gaps 3.7/2.6, 10.5/8.4, 8.8/8.1 → 30%, 20%, 8% relative | Row 12 (t49–t54) | insufficient evidence | The arithmetic is right (29.7%, 20.0%, 8.0%). All six "quotes" are the same generic sentence, and none carries a value. The CTC values must have been read off Fig. 4(c) bars, and the review should say so. |
| 17 | 3 studies make the attention-vs-CTC comparison (confirmed) | Row 13, 30 | outside check | This is a ledger count. |
| 18 | Usual M12: user held out, 7 of 22. [4] used 5 disjoint test speakers | Row 14 (c8) | correct | |
| 19 | Target splits: random 2.6%, leave-one-domain-out 8.4%, leave-one-sentence-out 8.1% | Row 15 (t37, t38, t41, t45) | correct | |
| 20 | SOTA M12: [6] within-user 4.56–8.96%, cross-user 14.22–19.05% after fine-tuning on 10 words | Row 16 (c14–c16) | partly correct | The numbers match. The quote does not define WER-w and WER-c as within-user and cross-user, so add the defining sentence. |
| 21 | "Generalizing very well across different domains" rests on unspecified folds and leaky tuning | Row 19 (t42, t62, t85) | correct | |
| 22 | Unseen-sentence test recombines seen words. "very impressive". Worst sentence 18.2% | Row 20 (t20, t43, t44, t46) | correct | |
| 23 | "Each component in our pipeline boosts the recognition performance" (Sec. 4.2) | Row 21 (t29, t30, t34) | insufficient evidence | The quoted phrase itself is not in the table. t34 is a different sentence. |
| 24 | Deployment on "existing smart devices" (Sec. 1), no latency or power | Row 23 (t5, t74, t28) | partly correct | The exact phrase is t74, which the table places in Sec. 5. t5 (Sec. 1) reads "existing voice-controlled smart devices". The locator in the review should be Sec. 5 or should quote t5. |
| 25 | M07 verdict "not reported" while the row says "Beam search, no external language model" | Table | wrong | The paper does report the design (no LM). The verdict contradicts the row. |

## Central claim, confounds and state of the art

- **M05.** The strongest confound in the phase-vs-Doppler result is that only phase received deltas. The review names it, which is good. Its "real departure" wording should be limited to speech, since phase tracking itself is prior art in acoustic gesture sensing.
- **M06.** The "State of the art" line is a 2018 comparison, not the best work today. Later hybrid CTC/attention and conformer systems are far better on LRS2/LRS3: Ma, Petridis, Pantic, ICASSP 2021, and Auto-AVSR (Ma et al., ICASSP 2023), whose visual-only WER on LRS3 is about 19–20%. Label [2] as the closest controlled comparison, or replace it with a current result.
- **M12.** The review makes the tuning leak the strongest overreach in the Verdict, yet gives M12 "standard" with no reason. Either justify that verdict under the rules or change it.
- **Fairness.** [5] and [6] are correctly marked [later] and used only as context. No later work is treated as prior work or as a missed citation. The authors' own finding (attention beats CTC, more so out of domain) is credited to them.
- **Hedging.** "the two do not rank" and "context, not evidence" fit the evidence. No position goes beyond its citation except items 3, 11 and 12 above.

## Required fixes (ordered by impact)

1. Add a quote for "speaker-independent and environment-independent", and state what a domain is in leave-one-domain-out (users, environments or both). If domains are not users, rewrite both the Verdict sentence and the M12 comparison with user-held-out studies.
2. Replace or relabel the M06 "State of the art". [2] (2018) is not today's best. Cite a current LRS2/LRS3 result with its year, metric and value, or call [2] "closest controlled comparison".
3. Give a source for the Fig. 4(c) CTC/attention values: say they were read from the figure and give the readout precision. Remove the six duplicate generic quotes.
4. Name the deciding priors for the M05 absence claim, and acknowledge prior multi-carrier phase tracking (LLAP 2016, Strata 2017). Keep "departure" limited to speech sensing.
5. Fix the M07 verdict. "not reported" contradicts "no external language model".
6. Reconcile the denominators: 16 of 28 vs pattern match 22 (M05), and 79 of 132 vs pattern match 114 (M06). Reword "mostly combine them" as a mention count.
7. Add the quote for [2]'s 55.0% CTC WER.
8. Confirm that [5]'s 26.3% WER is from the acoustic channel alone and say it is a dataset baseline. Otherwise drop "FMCW echo profiles" from the attribution.
9. Add [4]'s column header for 70.5% (ultrasound-only) and a quote for the 40 kHz emitter.
10. Add [6]'s definition of WER-w and WER-c.
11. Justify or change the M12 "standard" verdict in light of the tuning leak flagged in the Verdict.
12. Add the exact quote for "Each component in our pipeline boosts the recognition performance".
13. Fix the deployment locator. The phrase "existing smart devices" is in Sec. 5 (t74), not Sec. 1.

## Scores

- Procedure: 6/10. The claim table covers most numbers, but several rows carry placeholder or non-matching quotes (rows 3, 12, 21, 23) and the denominators are inconsistent.
- Final text: 7/10. Positions are clear, the confounds are named, and the arithmetic is correct. The M06 state-of-the-art line is out of date, and the "speaker-independent" framing is not sourced.
