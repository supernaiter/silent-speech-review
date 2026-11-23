# Independent evaluation: Soft Active EMG Interface for Machine Learning-Enabled Silent Speech Recognition

Date: 2026-11-23. Fallback evaluator (claim table only). Input: the compact review and its claim table. I did not open the sources, so each check is against the quote and location in the claim table. Statements from my own knowledge of the field are marked as inference.

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target uses "four dry fingertip electrodes" on a hand-worn package, pressed to the face only during input | Row 1 (t1, t2); row 17 (t41) | Insufficient evidence | t1 supports a hand-worn package and use only when needed. t2 describes a "bipolar pair", and t41 refers to four input *channels*. Four bipolar channels would need more than four electrodes. No quote gives the electrode count. |
| 2 | Neck- and ear-worn dry electrodes [2], [3] also avoid facial adhesives | Row 2 (c8, c13, c15) | Insufficient evidence | c8 supports dry neck electrodes for [2]. For [3], c15 reads "method relies on silver paste adhesion", which seems to conflict with "dry". The claim table does not say whether c15 describes [3] or a work that [3] cites. |
| 3 | Privacy and noise benefits are argued, not measured | Row 2 (t20, t22) | Correct | Both quotes are assertions with no measurement attached. |
| 4 | The 97.2% headline comes from a random class-stratified split within each participant | Rows 3, 8 (t8, t9) | Correct | The quotes support a stratified 20% split and a mean over three subjects. |
| 5 | Worn sEMG systems lose 14 to 23 points on a held-out session [4], [5] | Row 10 (c2, c3, c4, c24, c25) | Correct, with a caveat | [4] drops 87 to 64 (23 points) and 68 to 54 (14 points). [5] drops 77.5 to 59.3 (18.2 points) and 84.8 to 71.1 (13.7 points). [4] is an 8-class task and the target has 30 classes. The review does not state this task difference. |
| 6 | Hand-pressed placement varies from input to input (§ Discussion) | No row | No quote | This sentence supports the strongest confound in the Verdict, but the claim table has no quote for it. |
| 7 | Relative drops of 26% and 21% | Row 10 | Correct | 23/87 = 26.4% and 14/68 = 20.6%. |
| 8 | SilentWear drops to 59.3% on an "unseen day" [5] | Row 10 (c24) | Insufficient evidence | The number matches the quote, but the quote does not state the unseen-day condition. |
| 9 | M05 usual approach: 16 of 21 studies use adhesive or tattoo-like patches (upper bound); 7 ear-worn, 7 neck-worn | Row 4 | Correct as a tally | The quote matches. Known-item recall for this table is 0.5 (row 25), so this count is weak support for calling patches "usual". The population is "dry or worn-object" studies, yet the usual design is given as adhesive patches. That needs a short explanation. |
| 10 | M05 state of the art: 98.7% on five phrases from an RF-phase textile scarf [6] | Row 5 (c17, c18, c19) | Insufficient evidence | c18 says sEMG and phase were acquired at the same time. No quote shows whether 98.7% comes from phase alone or from fused input. |
| 11 | [3]: 96% on 10 words; [2]: 92.7% on 11 voiced words with 10 dry neck electrodes, both on random splits | Row 6 (c10, c11, c13, c16) | Partly correct | The accuracies, vocabulary sizes and random splits match the quotes. No quote supports "10 dry neck electrodes". |
| 12 | Target's 97.2% on 30 words "leads" under the same split (inference) | Row 7 | Correct as labeled | It is marked as inference and qualified by per-participant models. The vocabularies differ (5 phrases, 10 words, 11 words and 30 words), so the ranking is loose. |
| 13 | The third-party triggering claim (§ Results, Design for Intent-Driven SSR) has no trigger test | Row 7 / row 2 (t22) | No quote | t22 covers privacy, not third-party triggering. Quote the target's sentence. |
| 14 | M12 usual approach: of 143 studies, 65 speaker-disjoint, 44 session-disjoint, 58 random or k-fold | Row 8 | Correct as a tally | The counts overlap, and 65 is not a majority. Random or k-fold splits (58) are almost as common. |
| 15 | M12 state of the art: [7] 85.8% on 26 words, subject-independent, re-tested after re-attachment | Row 9 (c20, c21, c22) | Partly correct | 85.8% and 26 words match. "Stratified 5-fold CV under a subject-independent setting" is ambiguous. c22 confirms a re-test after re-attachment but gives no accuracy for it. [7] uses a strain sensor, not EMG, and the review does not say so here. |
| 16 | The pooled 92.1% model mixes the same three participants | Row 11 (t11) | Correct | The authors call it "cross-subject" and claim "robust generalization". The review's correction is fair. |
| 17 | M13 usual approach: 24 of 30 studies decode off the body with no power figure; target decodes on a PC | Row 12 (c14, t51) | Correct | |
| 18 | M13 state of the art: 2.47 ms, 63.9 µJ, 20.5 mW [5] | Row 13 (c23) | Partly correct | 2.47 ms and 20.5 mW are in the quote. 63.9 µJ is not. |
| 19 | The drone demonstration reports no success, false-trigger or latency figures; silent-speech drone control is earlier work (ref. 47) | Row 14 (t44, t53) | Correct | The absence cannot be checked from the quotes, but nothing contradicts it. The credit to ref. 47 is the authors' own and is attributed to them. |
| 20 | Training accuracy is 1.000 (Supp. Fig. 9) and the CV mean is .916 (Supp. Table 3) | Row 15 (t12, t14, t50) | No quote | Neither number appears in any quote. t50 is cut off at "indicating that the test sets". The authors may themselves attribute the gap to the test sets, in which case the review restates the authors' point as its own critique. |
| 21 | For S02 and S03: 900 raw trials, a 300-sample test split and 1,800 samples do not reconcile | Row 16 (t7, t8, t13) | Wrong | t8 gives exactly 12 test samples per class, so the test split has 12 × 30 = 360 samples, not 300. 360 is 20% of 1,800, while 20% of 900 is 180. The inconsistency is real, but the number is wrong. t13 says augmentation was applied only to the training sets, and the review should respond to that statement instead of only speculating. |
| 22 | "Unaffected even in noisy environments" has no noise test | Row 2 (t20) | Correct | |
| 23 | Four channels win, but only the top three combinations were tuned; the Conformer (91.1%) had no matched tuning | Row 17 (t15, t16, t41) | Partly correct | The four-channel result is supported. No quote supports "only the top three combinations were tuned" or the 91.1% figure. |
| 24 | M12 verdict "behind, against typical field practice" | Rows 8, 10, 27 | Position stronger than the evidence | The deciding priors [4] and [5] are named and the effect is repeated. The ledger counts (65 speaker-disjoint against 58 random, overlapping, by pattern match) do not show that random splits are atypical. The verdict rests on [4] and [5], not on field practice. |
| 25 | Chronology: [5], [6] and [7] marked [concurrent]; [4] used as a prior | References | Correct | [4] (arXiv 2509) is about 11 months before the target (arXiv 2608). [5] (arXiv 2603) is about 5 months before it. [5] supports the size of the drop but is not treated as prior work the authors missed. |

## State of the art (inference, from field knowledge)

- **M12:** the session-independent EMG work of Wand and Schultz (2011–2014) and the silent-speech EMG corpora of Gaddy and Klein (2020, 2021) are earlier references for session-disjoint testing. Checking whether they report a comparable word-level accuracy is worth more than citing [7], which uses a strain sensor, as the EMG evaluation benchmark.
- **M05:** AlterEgo (Kapur et al., 2018, IUI) is an earlier worn-object facial sEMG interface with a fixed mount, reporting about 92% on a digit vocabulary. Consider naming it next to [2] and [3].

## Required fixes, ordered by impact

1. Correct "300-sample test split" to 360 samples (12 per class × 30, t8). Restate the inconsistency as 360 = 20% of 1,800 against 900 raw trials, and respond to the authors' statement that augmentation was applied only to training (t13).
2. Quote the full t50 sentence. Add quotes for training accuracy 1.000 (Supp. Fig. 9) and the CV mean .916 (Supp. Table 3). If the authors already attribute the test-above-CV gap to the test sets, credit them instead of presenting it as the review's finding.
3. Base the M12 "behind" verdict on [4] and [5], not on "typical field practice". The ledger shows 65 speaker-disjoint against 58 random or k-fold, overlapping and by pattern match, so it does not show that random splits are atypical. Also revise "Usual approach: speaker-disjoint test" in the summary table.
4. Add a quote and location for "hand-pressed placement varies from input to input (§ Discussion)". It carries the strongest confound in the Verdict.
5. Fix "four dry fingertip electrodes". The quotes support four channels built from bipolar pairs, so give the correct electrode count or say "four channels".
6. Resolve the c15 conflict ("relies on silver paste adhesion") with the claim that [3] uses dry electrodes. If [3] uses adhesion, drop [3] from "also avoid facial adhesives".
7. Supply quotes for the unseen-day condition of 59.3% and for 63.9 µJ in [5], or remove them.
8. Supply a quote for "10 dry neck electrodes" in [2], or remove the count.
9. Say whether [6]'s 98.7% comes from phase alone or from phase fused with sEMG (c18). If fused, "not sEMG" is wrong.
10. For [7], say that it is a strain sensor and not EMG. Clarify what "subject-independent stratified 5-fold" means, and either give the accuracy after re-attachment or drop "re-tested after re-attachment" from the state-of-the-art line.
11. Add quotes for "only the top three combinations were tuned" and for the Conformer's 91.1%, or remove them.
12. Quote the target's third-party triggering claim. t22 covers privacy only.
13. In the Verdict and in M12, say that [4] is an 8-class task against the target's 30 classes when using the 14 to 23 point drop. Note that [5]'s vocalized drop is 13.7 points, which is inside the range only after rounding.

## Scores

- Procedure: 6/10. Every row has a quote and location, and the deciding priors are named. Several load-bearing numbers have no quote (rows 6, 20 and 23, plus the 63.9 µJ figure and the electrode counts), and one number is wrong.
- Final text: 6/10. The position is clear and the M12 confound is the right one. The M12 verdict leans on ledger counts that do not carry it, and the reconciliation bullet uses the wrong test-set size.

What holds: the reading of the pooled "cross-subject" model, the session-disjoint confound, and the relative-change arithmetic are correct and well targeted.
