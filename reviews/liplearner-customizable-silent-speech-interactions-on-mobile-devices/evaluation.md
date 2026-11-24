# Evaluation: LipLearner (Su, Fang, Rekimoto, CHI '23)

2026-11-24
Evaluator: a language model separate from the writer

Scope: the compact review and its claim table only. No sources were opened; quotes and locations were taken as given. Outside knowledge that I cannot locate is marked "unverified".

## Claim checks

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target changes M03, M01, M06 | CT 1 (Secs. 1, 5.2, 6.1) | correct | All four quotes support it. |
| 2 | Only the target fits a linear classifier on a frozen encoder "on the device", one-shot 25-command F1 0.8947 over 1,000 draws | CT 2, Appendix M03 | correct with caveat | Number, shot count, command count and 1,000 repeats match. The Appendix design is "frozen encoder with linear or logistic classifier"; "on the device" is an extra restriction the tally does not record. |
| 3 | 87.29% vs 81.67%, voiced vs unvocalized, one-shot (§8.2.2) | CT 3 | correct | Difference 5.62 points matches the paper's "approximately 5.6%". |
| 4 | Visual-only KWS predates the paper and the paper cites none of it | CT 3, CT 19 | correct (unstated note) | Supported by the writer's "unstated" check of Secs. 2.1-2.2, 6.1 and the reference list. |
| 5 | 0.9895 vs 0.7147 F1, counterpart trained from scratch (§5.4) | CT 4, 26, 29 | correct, condition missing | Numbers and "train-from-scratch" match. The number of shots behind the target's 0.9895 is not given; the paper says the counterpart used "four times more training data", so the target condition (shots, conditions) should be stated. |
| 6 | Contrastive stage never ablated against Feng et al. weights | CT 4, 9 | correct (unstated note) | "LRW weights" is not in any quote: insufficient quote for "LRW". |
| 7 | Sen et al.: 68.1% top-1, 49.3% from the real sample alone (Table 2) [5] | CT 6 | insufficient evidence | Rows "ve−r+s+aug" (68.1) and "cl−r" (49.3) appear to be different model variants (ve vs cl), so 49.3 may not be "the same model from the real sample alone". Column header (which subject / which metric) is not quoted; "for an ALS patient" is not shown for column 1. |
| 8 | Jeon et al. 82.85% / 90.17%, 20-way, held-out sessions [6] | CT 7, 25 | correct | Labelled [later]; used as state of the art only, not as a prior. |
| 9 | 2,217 ms for 30 commands × 5 shots (§6.2.3) | CT 8 | correct | |
| 10 | Usual approach M03: 7 / 6 / 3 / 1 of 30 | Appendix M03 | correct (tally) | Consistent with Appendix. |
| 11 | M01 usual approach: 27 / 12 / 11 / 5 of 354 [7], [8] | Appendix M01, CT 11 | correct as tally, but mis-framed | The Appendix inclusion rule excludes "overt-only training applied to silent test data", which is exactly the target's design. The usual approach line therefore compares against a set that by rule cannot contain the target; "Voice2Lip uses none" is true by construction. Also "as in the [concurrent] [8]" is missing a noun. CT 11 location (target Sec. 1) does not support the counts. |
| 12 | "Voice2Lip" enrolls by a voiced take labelled by ASR (§7.2) | CT 12 | insufficient quote | Quote is from Sec. 1, not §7.2, and the name "Voice2Lip" is not in it; the name is never introduced in the review. |
| 13 | Kashiwagi et al.: silent WER 22.55% (normal-only training) to 9.97% on 11 held-out speakers (Table 1) [9] | CT 13 | insufficient evidence | Speaker count supported. Column header for the last column is not quoted, and nothing in the quote says the LNCE row is "normal-only training". The 9.97% row adds a silent-speech loss (LSKL), so it uses silent data in training. |
| 14 | One-shot loss 5.6 points "in line with" 8.5% [10], [9] | CT 14 | correct with caveat | 8.5% is quoted second-hand from [9] Sec. 2.1, not from [10] itself, although [10] is listed as read. Different tasks (30-command one-shot vs Petridis' dataset); "in line with" is a judgment, acceptable. |
| 15 | No silent one-shot enrollment under the same protocol | CT 15 | correct (unstated note) | |
| 16 | M06 usual approach: 20 / 9 / 7 / 3 of 183 | Appendix M06 | correct (tally) | Known-item recall 0.5 is reported; not audited per brief. |
| 17 | Transpotter 72.5% mAP on LRS2 (Table 1) [11] | CT 18 | insufficient quote | 72.5 is the third number of the row; the column header (dataset, metric) is not quoted. |
| 18 | EER 6.46% (2018, 635 unseen words) on LRS2 [2]; 5.7% (2020) on LRS2 [3] | CT 18 | insufficient quote | For [2] the quoted row does not show which column is EER, and LRS2 is not in either quote. 5.7% EER for [3] is supported; LRS2 is not. |
| 19 | 6.75% EER "of the same order", enrolled phrases instead of text queries | CT 20 | correct number; weak comparison | Target EER is one command vs the other enrolled commands in a closed set; [2], [3] are open-vocabulary search in continuous video. "Same order" invites a comparison of incommensurable numbers. |
| 20 | Per-user optimal thresholds 0.649 and 0.805; one fixed threshold | CT 21 | correct | |
| 21 | FPR 0.26% to 0.07% after about 7 misactivations (§8.2.1) | CT 22 | correct | "No test compares KWS with mouth-opening activation" has no quote or unstated note. |
| 22 | M12: within-speaker test, leave-one-condition-out, no chance level | CT 24 | insufficient quote | No quote says the test is within-speaker, and no "unstated" note backs "no chance level". |
| 23 | Live accuracy 96.04% / 98.75% scored on prompts the model then learns from | CT 27 | number correct; judgment overstated | The quotes describe a test-then-update protocol: each trial is scored before the sample is added. That is a valid sequential evaluation, not leakage; the sentence implies a flaw the quotes do not show. The real limit is that later shots come from the same session and user. |
| 24 | Condition-disjoint three-shot F1 ≥ 0.9391 (Table 2) | CT 28 | correct | |
| 25 | "Non-verbal lip gestures": one participant, 9 of 11 (§8.1) | CT 30 | insufficient quote | 9 of 11 supported; "one participant" is not in the quote. |
| — | M13 "On-phone, about 422 ms" (component table) | not in claim table | no quote | A number with no claim-table row, source quote or location. |

## Usual approach and state of the art

- M03: The usual-approach tally is reasonable. Frozen encoder plus linear probe is the standard evaluation protocol in self-supervised representation learning (e.g. SimCLR-style linear evaluation, 2020; unverified locator), so the novelty is in applying it to on-device lip command registration, not in the design itself. The review should say so. State of the art is an EMG paper with accuracy on a different vocabulary; the review states the mismatch. No later camera-based few-shot lip command work is named; I know of none I can locate (unverified).
- M01: Kashiwagi et al. is sentence-level VSR WER with silent data in training. It is not the best result for voice-only enrollment of silent commands, and its metric and task differ from the target. The state-of-the-art line should state these differences, as the M03 line does.
- M06: Transpotter (2021) is a reasonable visual-only KWS state of the art as of the target. Later visual or audio-visual KWS work may exceed it (unverified). The component is activation; [3] (wake words) is the closest prior and should lead.
- M12: "State of the art" for an evaluation split is a protocol, not a result; acceptable.

## Central claim and confounds

- Strongest confound: the target's superiority over "the conventional user-dependent approach" is pretrained vs un-pretrained, with different amounts of user data (CT 26, 29). The review handles this well (Verdict, M12, "Where the claims outrun the evidence"). It should also state the target's shot count for the 0.9895.
- The M03 "ahead" verdict rests on a design count (1 of 30) and an absolute F1, but the review itself says no result compares the linear head with prototypes or fine-tuning and no ablation removes the contrastive stage. The effect therefore shows "pretrained encoder beats training from scratch", which is not specific to the M03 design. The position is stronger than the evidence. Either downgrade to standard (design novel, advantage untested) or state the narrower claim: ahead only for being on-device in one to five shots, with the effect being against the from-scratch counterpart.
- "Ahead" rules: Appendix count present (30, 1); deciding prior [5] named; the effect is in the Verdict but not repeated in the M03 section, which gives only the 2,217 ms update time. Repeat the 0.8947 one-shot F1 (and its comparator) in M03.

## Fairness

- No work after the target is treated as a prior. [8], [9] correctly [concurrent]; [6] correctly [later].
- The paper's novelty sentence is narrow ("not yet applied in lipreading-based interfaces", §6.1). [2] and [11] are retrieval in video, not interface activation; only [3] (wake words) is close. "Without citing these works" is fair, but the review should say the paper's claim is limited to interfaces and that the counter-evidence is mainly [3].
- The threshold limitation (CT 21) is stated by the authors themselves as future work; the review presents it as its own finding without saying so.

## Absence and novelty claims

- "Only the target fits a linear classifier on a frozen encoder" (Verdict, M03): names the deciding prior [5]; no earlier lip work with the same design is known to me (unverified). See the linear-probe note above.
- M06: the Appendix says 3 studies use an enrolled example query but two of them ([3], [11]) use phoneme text queries when read, leaving at most one. Example-enrolled visual KWS as activation is thus nearly unique in the tally, while the 183-study tally shows KWS activation in 3 studies vs 20 manual triggers. The review's "standard" rests on visual KWS existing at all; it should reconcile it with its own counts or state why the enrollment-by-example difference does not count.

## Required fixes, by impact

1. M03 verdict: "ahead" is stronger than the evidence (no head comparison, no encoder ablation, the only effect is vs a from-scratch model). Downgrade or narrow, and repeat the effect with its comparator in the M03 section.
2. M01 usual approach compares against a tally whose inclusion rule excludes the target's own design (overt-only training applied to silent test). Reframe: say the target's design falls outside the counted cross-mode designs and give the count for overt-only training if available.
3. M06 "standard" vs the review's own counts (3 of 183 KWS activation; at most 1 enrolled-example query). Reconcile, and lead with [3] as the deciding prior for activation.
4. Sen et al. 49.3% vs 68.1%: the two rows are different model variants (cl−r vs ve−r+s+aug); either quote the ve−r row or rephrase. Quote the column header to support "ALS patient" and "top-1".
5. Kashiwagi et al.: quote the column header for 22.55 / 9.97 and support "normal-only training"; note that the 9.97% model uses silent data in training and is sentence WER, unlike the target's task.
6. Live-accuracy sentence (M12): the quoted protocol is test-then-update; remove the implied leakage or state the precise concern.
7. State the target's shot count behind the 0.9895 F1 (§5.4).
8. M13 "about 422 ms" has no claim-table row; add source quote and location or remove.
9. Visual KWS numbers: quote column headers for Transpotter 72.5 mAP and Stafylakis 6.46% EER, and support "LRS2" for [2], [3].
10. "6.75% EER is of the same order": state that the target's EER is closed-set discrimination among enrolled commands and not comparable to open-vocabulary video search, or drop the comparison.
11. Fairness: say the paper's KWS novelty claim is limited to lipreading interfaces, and that the fixed-threshold limitation is stated by the authors (§8.2.1).
12. M12: add quote or unstated note for "within-speaker" and "no chance level".
13. "Voice2Lip" is not introduced and its quote is from Sec. 1, not §7.2; define it and fix the location.
14. "One participant" (non-verbal gestures, §8.1) is not in the quote; add the quote.
15. Minor: "as in the [concurrent] [8]" lacks a noun; "LRW" for Feng et al. weights has no quote; 8.5% is cited to [10] but quoted from [9].

## Scores

- Procedure: 7/10. Claim table is complete for most numbers, unstated checks are used where absence is claimed, chronology labels are right. Gaps: one number without a row, several quotes without column headers, a tally whose inclusion rule excludes the target.
- Final text: 6/10. Clear positions and good handling of the from-scratch confound; the M03 "ahead" verdict and the M01 / M06 framing are stronger or less consistent than the evidence and the review's own counts allow.
