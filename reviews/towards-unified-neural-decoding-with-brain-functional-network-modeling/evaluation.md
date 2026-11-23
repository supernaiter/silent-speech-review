# Evaluation: Towards Unified Neural Decoding with Brain Functional Network Modeling

2026-11-24
Evaluator: a language model separate from the writer

Inputs: the evaluator brief and the compact review (with its claim table) only. No sources were opened. Outside knowledge that I could not locate is marked "unverified".

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | MIBRAIN pools 11 sEEG participants, masked pretraining, region tokens with prototypes (Verdict) | Claim table row 1 (Methods: Study participants; Methods: Whole functional network prototyping) | correct | The 11 participants, masked autoencoding and unified space are quoted. "Subject-specific encoders" is not in the quote (insufficient quote), but the M06 note on majority voting through other participants' encoders is consistent with it. |
| 2 | The online test, "called free of subject-specific training", uses models trained on the test participants (Verdict; Where the claims outrun, bullet 1) | Rows 16, 22 (t67, t72, t62) | insufficient evidence | The quote is cut off: "even before the practice session, despite the absence of any subject". Because it mentions a *practice session*, the authors may mean that the user had no practice or calibration session, not that the model saw none of the user's data. In that case the review attacks a claim the authors did not make. The full sentence is needed. This is the review's central argument against the generalization claim. |
| 3 | The text gives no absolute accuracy or chance value (Verdict; bullet 2) | Rows 17, 21 (t68, unstated) | insufficient evidence (absence claim) | This is consistent with the gains being reported "without units" (row 9) and with the Fig. 2 caption naming a chance-level baseline. It is acceptable as an absence claim, and the question to the authors covers it. |
| 4 | Brant and BrainBERT "were already known to sit near chance on sEEG word decoding [2]" (Verdict) | Rows 3, 5 (Du-IN Table 2) | wrong as phrased | The task has 61 classes, so chance is about 1.6% (inference). Brant at 11.16% is about 7× chance and BrainBERT at 6.72% about 4×. Du-IN shows that they are far below Du-IN, not that they are near chance. The "barely exceeding chance" remark comes from MIBRAIN itself (p. 8) on its own 23-class task. |
| 5 | Du-IN 62.70% top-1, 61 Mandarin words, 12 subjects; Brant 11.16–12.42%, BrainBERT 6.72–7.50% | Row 5 | correct / insufficient quote | 62.70%, 12 subjects, 11.16 and 6.72 are quoted. The upper bounds 12.42 and 7.50 and "61 words" are not in the quotes. |
| 6 | Du-IN (poms) 59.18% vs 62.70%, a 5.6% relative loss (inference) | Row 8 | correct | (62.70 − 59.18) / 62.70 = 5.61%. The row label "Du-IN (poms)" fits pretraining on multiple subjects. The "(inference)" label is appropriate. |
| 7 | Singh et al.: 25 sEEG patients, PER 57% → 49% with one transfer subject → 45% after four | Row 6 | correct / insufficient quote | 25 patients, 57→49 and 45 after four subjects are quoted. "With one transfer subject" is not in the quote. The [concurrent] label is plausible: Nat Commun 2025, target June 2025. |
| 8 | Chen et al.: one transformer, ECoG and sEEG, PCC 0.765 on left-out participants | Rows 12, 15 | correct | Both the number and the leave-one-out condition are quoted. |
| 9 | Pooling gains for participants 10 and 11: 8.08/6.83 audible, 5.10/4.97 silent, without units | Row 9 | correct | The quote matches. |
| 10 | Adding fewer than three participants lowered audible accuracy for participant 11, and only one enrollment order was tested | Row 10 | insufficient quote | The "significant performance reduction" is quoted. "Fewer than three" and the single order are not shown. "Incrementally incorporating" does not by itself show that only one order was tested. |
| 11 | Imputation validated by correlation and by above-chance decoding, except participants 4 and 8 (audible) | Row 13 | correct | |
| 12 | The Discussion claims that imputation beats state-of-the-art direct-recording methods, with no number | No claim-table row | no quote | This statement has no row. Add the Discussion quote. |
| 13 | Unseen-subject decoding uses majority voting, "as the authors concede (Discussion)" | No claim-table row | no quote | Neither the Methods passage nor the Discussion concession is quoted. |
| 14 | The class set is called 23 initials but includes the finals i and u | Row 18 | wrong framing | The quoted passage is the authors' own disclosure ("Alongside the 21 distinct initial consonants, our analysis included two simple phonetic finals ... due to their frequent use as semi-consonants"). It is a labelling looseness that the authors explain, so it does not belong under "claims outrun the evidence" (fairness, check 5). |
| 15 | Channel selection precedes the split, with no stated exclusion of test samples | Row 19 | insufficient quote | The t-test selection is quoted. The order relative to the split is not shown. The question to the authors (row 23) is the right form for this point. |
| 16 | No seeds or repeated runs | Row 20 | insufficient evidence (absence) | This is acceptable as an absence claim. |
| 17 | M03 usual approach: "Of 379 unique studies ... pattern match" | Body vs Appendix | wrong (internal inconsistency) | The Appendix says "370 unique studies pattern match", then "Designs over 379 unique studies (pattern match)". One of the two numbers is wrong. |
| 18 | M06 and M12 usual-approach counts (98: 25/12/6; 618: 132/68/28/27) | Rows 11, 14, Appendix | correct | They match the Appendix. Known-item recall for M06 is 0.5, so the M06 tally is weaker. |
| 19 | M12: leave-one-subject-out "matches this uncommon design" | Rows 14, 15 | correct | 28 of 618 supports "uncommon". |
| 20 | Verdict: both components standard, with deciding priors [2] and [3] named | Verdict, M03, M06 | correct | The priors are named and dated before the target. "Not cited" rests on an unstated note (t69). It is plausible but cannot be checked here. |

## Usual approach and state of the art

- M03: The usual approach (a per-subject model, with general-checkpoint fine-tuning in the pretraining subset) is plausible. Du-IN as the state of the art for sEEG Mandarin word decoding with region-level masked pretraining fits. Its task differs from the target's (61 words vs 23 phoneme classes), and the review treats it as a design precedent, not as a number to beat. That is the right handling.
- M06: Chen et al. (2024) is a reasonable state of the art for layout-agnostic intracranial speech decoding. A possibly more directly relevant sEEG prior on pooling across arbitrary electrode layouts is the Population Transformer (Chau et al., 2024, arXiv:2406.03044; unverified locator). The review could weigh it.
- M12: Fine.

## Central claim and strongest confound

The strongest confound is the reading of "subject-specific training" (row 2). If the authors mean that the user did not practice or calibrate, the review's main objection does not apply. A second confound is the task: the near-chance baseline performance comes from MIBRAIN's own 23-class task, while Du-IN's 61-word numbers are well above chance. The review mixes the two (row 4). The relative-versus-absolute question is handled well (row 9 and the question to the authors).

## Required fixes (ordered by impact)

1. **Online claim (Verdict; bullet 1).** Quote the full p. 10 sentence. If "absence of any subject[-specific] ..." refers to a user practice session, rewrite: the model was trained on data that included the online participants, but the authors' claim is about user practice. Otherwise keep the objection, backed by the full quote.
2. **"Near chance [2]" (Verdict; M03 paragraph).** Du-IN shows Brant at 11.16% and BrainBERT at 6.72% on 61 classes, where chance is about 1.6% (inference). Rephrase to "far below Du-IN [2]" and keep "barely above chance" attributed to MIBRAIN's own result (p. 8).
3. **370 vs 379.** Reconcile the M03 pattern-match count between the body and the Appendix.
4. **23 initials including i and u.** The authors disclose and justify this themselves. Drop it from "claims outrun the evidence" or reword it as a labelling note.
5. **Missing claim-table rows.** Add rows for: the Discussion's state-of-the-art claim about imputation; the Discussion concession on majority voting; the Methods passage on unseen-subject voting; the per-subject input layers in M06.
6. **Insufficient quotes.** Extend the quotes for: Brant and BrainBERT upper values (12.42, 7.50) and "61 words"; Singh "one transfer subject"; participant 11 "fewer than three" and the single enrollment order; channel selection taking place before the split; "subject-specific encoders".
7. **M06 state of the art / priors.** Consider the Population Transformer (Chau et al., 2024; unverified) as an sEEG prior for pooling across arbitrary electrode layouts.
8. **Reference [3].** Check whether Chen et al. now has a peer-reviewed version (unverified) and cite it if so.
9. **M09 slot.** "Correct or top-3" reads as an evaluation metric, not a confirmation mechanism. Recheck the slot, or mark it not applicable.

## Scores

- Procedure: 7/10. The claim table is mostly well anchored, but rows are missing for two positions and several quotes are truncated.
- Final text: 6/10. The positions are clear and fair on relative-vs-absolute gains. The central online-test objection rests on an ambiguous truncated quote, and the "near chance [2]" attribution is wrong.

## Brief praise

The review asks the right questions about absolute accuracy, chance level and units. Its use of Du-IN's multi-subject versus per-subject comparison is a sharp, well-sourced point.
