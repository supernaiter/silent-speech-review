# Independent evaluation: Affect Decoding in Phonated and Silent Speech Production from Surface EMG

Date: 2026-11-21. Independent evaluator, claim table only. The sources were not re-opened. Each judgement rests on the quote and location in the claim table. Where general knowledge of the field is used, it is marked as inference.

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper changes one component, the output (M08): affect from silent articulation | Row 1, t1 (Sec. 2) | correct | t1 states the aim (affect in motor execution across articulation modes). |
| 2 | Within-subject AUC 0.845 | Row 3, t15 (Table 5) | correct | TD-0, second column. This assumes the column order is BAC intra, AUC intra, BAC inter, AUC inter. The quote does not show the headers. |
| 3 | Unseen speakers EMG AUC 0.567 to 0.574 | Row 3, t14–t16 (Table 5) | correct | 0.567 (TD-0), 0.568 (structural) and 0.574 (BioCodec) match. |
| 4 | Decoding "does not work" for unseen speakers | Verdict vs "Chance level" bullet | wrong (internal) | The review faults the authors for calling values near chance without a test. It then makes the same untested call itself. |
| 5 | "The claim that affect rides on speech-motor activity does not hold" | Rows 15, t68/t53 (§6.1, §7) | insufficient evidence | The authors say they *cannot disentangle* the two. That leaves the claim not established; it does not refute it. The review also presents the authors' own §6.1/§7 concession as its finding. |
| 6 | Most discriminative site is the brow electrode E6 | Row 15, t71 (Table 3) | insufficient evidence | t71 only gives E6's anatomical location. No quote from Figs. 4–5 shows that E6 ranks highest. |
| 7 | Spontaneous affect decoded better from audio (Vox-Profile 0.743 vs 0.630) | Row 19, t40/t38 (Table 9) | correct | The numbers match. |
| 8 | "...whichever training set was used" | Row 19 vs row 18 | insufficient evidence | Table 9 reports one set of results. It cannot show that the result holds under both of the training descriptions in §5.3 and §6.3. |
| 9 | Closest prior [3] "describes emotional articulation without a classifier" | Row 2, p3 | wrong (likely) | [3] is titled "...Emotion Recognition from Vocal Tract Shape Dynamics in Real-Time MRI", which describes a recognition system. The quote ("clock"/"dock") does not support "without a classifier". |
| 10 | [3] analyses phonated articulation | Row 6, p3 | insufficient evidence | This is plausible (inference: the rtMRI emotion corpora are phonated), but no quote says it. |
| 11 | [2]: speaker ID 73% UAR, 12.5% chance, held-out sessions | Row 7, p2 | partly correct | 73% UAR is quoted. The quote supports neither the 12.5% chance level nor "held-out sessions". |
| 12 | [5] decodes emotion from carotid pulse, not the speech-muscle channel | Row 8, p5 | correct | The quote matches. However, [5] is a silent-speech wearable that decodes emotion at the neck. It is a direct prior for the M08 output and undercuts "none ... decodes affect from silent articulation" (see #20). |
| 13 | Effect repeats over 12 speakers and two blocks | Row 9, t3/t4/t14 | insufficient evidence | No quote gives the number 12. Also, the effect repeats only within subject; the inter-subject results are near 0.57. |
| 14 | Within subject in both directions (Table 8) | Row 11, t45/t29 | correct | |
| 15 | Structural 0.829 → 0.707 (14.7%, 37% of margin); BioCodec 0.792 → 0.763 (3.7%, 10%) | Row 13, t29/t31 | correct arithmetic, column order unverified | The arithmetic checks out (0.122/0.829 = 14.7%, 0.122/0.329 = 37.1%, 0.029/0.792 = 3.7%, 0.029/0.292 = 9.9%). The quotes do not show which Table 8 column is S→S and which is P→S. |
| 16 | Janke & Diener 2017: MCD 5.54 → 6.81, 23% | Row 12 | insufficient evidence | There is no source quote (only "audit"). The arithmetic is correct (22.9%). |
| 17 | Vox-Profile 0.889 → 0.469; structural 0.856 → 0.720 | Row 16, t23/t19 | correct | The review omits that the authors make the same point themselves (t46: EMG AUC > 0.7 on repeated sentences). |
| 18 | Silent trials always follow phonated; inter-subject structural 0.527 → 0.613, p = 0.038 | Row 17, t69/t24 | correct | The Task 1 vs Task 3 difference also confounds sentence content with order. The review attributes it to order and practice only. |
| 19 | McNemar p < 0.001 conflicts with "no significant differences between modalities" | Row 18, t62/t63 | likely wrong | t63 reads "TD achieves the highest performance (AUC = 0.845), however all three modalities performed similarly". The "three modalities" are most plausibly the three EMG representations (TD, structural, BioCodec), not speech vs EMG. If so, there is no contradiction. |
| 20 | §5.3 vs §6.3 training-set inconsistency | Row 18, t72/t73 | correct | |
| 21 | No permutation or binomial test | Row 20, t57 | insufficient evidence | t57 quotes a value only. A claim that something is absent needs a statement that the whole paper was checked. |
| 22 | Task 2 is phonated only | Row 21, t4/t51 | insufficient evidence | Neither quote says this. |
| 23 | "none of the 99 ledger studies decodes affect from silent articulation" | Rows 2, 5, 27 | insufficient evidence | 28 of the 99 mention affect in full text, but the recall sample covers 13 snippets. [5] (emotion in a silent-speech wearable) and the 2025 survey [4] are not named as deciding priors. |
| 24 | M08 state of the art = speaker ID 73% UAR [2] | Component section | judgment questionable | This is not an affect result. The best prior affect decoding from speech-production signals ([3], [5]) has no metric or value given. |
| 25 | M04 state of the art = Janke & Diener 2017 | Component section | outdated (inference) | Later overt-to-silent EMG transfer work is stronger and more recent: Gaddy & Klein, "Digital Voicing of Silent Speech", EMNLP 2020, and its 2021 follow-up (ACL 2021); later large-vocabulary silent-EMG work reports lower silent WER. A 2017 MCD result is not the state of the art. |

## Other checks

- **Central confound.** The strongest confound is facial expression versus articulation, because the brow electrode dominates. The review raises it, but its wording overstates the conclusion (#5). On transfer, the review correctly notes that the metric and starting point differ from [6]. On cross-subject results, the review uses absolute AUCs and gives no chance-level test (#4).
- **Fairness.** No later work is treated as prior. [4] (2025) and [5] (2024) both predate the target (2026). Several "outrun the evidence" points repeat the authors' own caveats (§6.1 facial attribution, §7 disentanglement, t46 repeated-sentence discussion) without saying that the authors raise them.
- **Novelty.** Inference: affect recognition from facial EMG without speech (corrugator, zygomaticus and depressor supercilii sites) is a long-established line of work. Because E6 dominates, this line is a deciding prior for the "ahead" verdict and should be named.
- **Verdict rule (ahead, M08).** The ledger count (99) and the Appendix are given, and priors are named. The "effect repeated" condition holds only within subject. The deciding priors are mischaracterized ([3]) or omitted ([5], facial-EMG affect work).
- **Internal consistency.** The components table gives M04 as "(23) (confirmed 23)", while the text gives 33 pattern-match and 23 confirmed. Claim-table rows 22–23 cite a "Questions for the authors" section that does not appear in the review.
- **Bibliography.** [3] has venue "SIGGRAPH 2021 (arXiv preprint)", which is ambiguous. Give the actual venue (inference: a SIGGRAPH 2021 poster) or list it as an arXiv preprint only.

## Required fixes (ordered by impact)

1. Correct the description of [3]: it is an emotion recognition system from rtMRI articulation, not a classifier-free description. Restate the novelty boundary accordingly (silent, non-phonated articulation, via speech-muscle EMG).
2. Narrow the absence claim. Name [5] (emotion decoded in a silent-speech neck wearable), [4] and facial-EMG affect recognition as deciding priors. State that the absence rests on a 13-snippet sample of the 28 affect mentions.
3. Change "does not hold" in the Verdict to "is not established". Attribute the facial-expression concession to the authors (§6.1, §7) instead of presenting it as the review's finding.
4. Remove or re-verify the McNemar "inconsistency". "All three modalities" in t63 most likely refers to the three EMG representations, not speech vs EMG.
5. Replace "but not for unseen speakers" with a statement that does not assume an untested chance level, such as "close to chance (AUC 0.567 to 0.574), with no chance-level test". This keeps the text consistent with the "Chance level" bullet.
6. Delete "whichever training set was used". Table 9 does not support it.
7. Update the M04 state of the art to more recent overt-to-silent EMG transfer work (Gaddy & Klein 2020/2021 or later), with year, metric and value, and add a source quote for the Janke & Diener MCD values.
8. Give an affect metric and value for the M08 state of the art ([5] or [3]) instead of, or in addition to, speaker-ID UAR. Support "12.5% chance" and "held-out sessions" with a quote, or drop them.
9. Add quotes for the unsupported specifics: 12 speakers, E6 as most discriminative (Figs. 4–5), absence of a permutation test, Task 2 being phonated only, and the Table 8 column order behind the 0.829/0.707 comparison.
10. In the "Order and practice" bullet, note that Task 1 vs Task 3 also differ in content, not only in order.
11. Make the M04 count in the components table match the text (33 pattern match, 23 confirmed).
12. Remove claim-table rows 22–23, or restore the "Questions for the authors" section they cite.
13. Fix the venue of [3].

## Scores

- Procedure: 6/10
- Final text: 5/10
