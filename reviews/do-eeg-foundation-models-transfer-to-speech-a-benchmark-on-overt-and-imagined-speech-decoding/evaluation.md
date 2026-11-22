# Evaluation: Do EEG Foundation Models Transfer to Speech? A Benchmark on Overt and Imagined Speech Decoding

Date: 2026-11-22. Independent evaluation pass; inputs were the compact review and its claim table only. Sources were not re-opened; judgments rest on the quotes and locations in the claim table, internal consistency, and knowledge of the field (marked as such).

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper fine-tunes LaBraM and EEGMamba against compact CNNs (Verdict) | Claim 1, t3, t13 | correct, with a wording issue | t3: two foundation models against "three established baselines"; EEGConformer (named as a baseline in t49) is a convolution-transformer, not a compact CNN. |
| 2 | M06 table row: "Four CNNs and two foundation models" | t3, t51 ("all five models") | wrong | The target's own text gives three baselines and five models in total. Internal contradiction in the review. |
| 3 | LaBraM below EEGNet on 24-word silent speech, 20.6% vs 30.5%, "worst baseline" [2] | l1, l2, l4 | correct | Quote matches number and condition. |
| 4 | LaBraM "near 25% balanced accuracy within subject" on BCIC2020-T3 [3] | n1, n2 | insufficient evidence / missing condition | n1 is the linear-probe row (0.2529 read as the LaBraM column); n2 is the test-time-training row and is truncated (four of six values). Column headers are not quoted. The Verdict drops the linear-head condition. |
| 5 | Both checkpoints at chance across subjects [3] | n4 | correct | "that scenario" is not identified in the quote; assumed cross-subject. |
| 6 | CBraMod 0.3976 with a linear head "on the same split", above every model here | n1, n3, t49 | correct on the number; contradiction on the split | M06 says "Splits differ" for the same set of comparators. The target's within-subject split (M11: "BCIC validation split") is not shown to equal the official test split used in [3]. |
| 7 | 30.2% best within-subject; 52.4 points below 82.6% | t49, b1 | correct arithmetic | 82.6 - 30.2 = 52.4. Comparability depends on row 8. |
| 8 | 82.6% was scored on the released test set (M06 SOTA; "Where the claims outrun" bullet) | b1, b2 | insufficient evidence | b2 is a general Introduction sentence about the competition, not a statement that the 82.6% figure is a test-set score. The target (t9) says the opposite. The review overrules the authors without a quote that settles it. |
| 9 | Test subject decides early stopping (M12, Sec. 2.4) | t23, t63 | correct | |
| 10 | "Held-out-subject testing is the usual design" | Appendix tally (46 of 153; fixed held-out 41) | partly correct | 30% plurality, close to the next design; "most frequent" is accurate, "usual" overstates. |
| 11 | M03 usual approach: 28 of 40 use a general checkpoint | Ledger tally | not checkable here | Ledger-derived; outside this check. |
| 12 | M03 SOTA: CBraMod with test-time training 0.5898, LaBraM-Base 0.2742 [3] | n2 | correct number; condition incomplete | 0.5898 uses test-time adaptation on unlabelled test data; the table row states it without that condition. The LaBraM column of a truncated row is not shown by header. |
| 13 | M03 SOTA is the best work | Field knowledge | insufficient / likely incomplete | The CBraMod paper (Wang et al., ICLR 2025, arXiv:2412.07236) reports full fine-tuning on BCIC2020-3 with CBraMod about 0.537 balanced accuracy and, to my recollection, LaBraM about 0.506, above EEGNet (medium confidence; verify Table on BCIC2020-3). If confirmed, prior evidence on LaBraM for this corpus is mixed, not uniformly negative. |
| 14 | Target LaBraM 27.7% "level with" 0.2742 | t44, n2 | correct | Fine-tuned target vs TTT LaBraM in [3]; conditions differ and should be stated. |
| 15 | Speech-specific pretraining remedy proposed in Sec. 4 | t61 | insufficient evidence | t61 is cut before the remedy; the quote shows only multi-seed future work. |
| 16 | [2] speech-pretrained model 39.6% vs EEGNet 30.5% | l6, l2 | correct | |
| 17 | M06 usual approach: other (48) or CNN (37, slot-filled) among 167 pattern-match studies | Appendix tally | inconsistent presentation | Mixes the pattern-match set (167) with slot-filled counts (out of 7,345). Table row assigns "slot-filled 48" to "other or CNN". "Model family other" carries no design information. |
| 18 | "The paper trains every model with one recipe" | t21, t22 | wrong as written | t22: baselines use lr 1e-3, foundation models 1e-4. Same loss, batch and stopping rule, different learning rate. |
| 19 | Deep metric learning 48.10% with 5-fold CV on the same corpus [5] | k1, k2 | insufficient evidence | k2 (56/14 trials) is consistent with 70 trials per class but does not name BCIC2020-T3. "subjects, classes and recordings do not [differ]" needs a dataset quote. |
| 20 | Validation subjects in [3] (subjects 1-28 train, 29-32 validation) | n5 | wrong as a speech comparator | BCIC2020-T3 has 15 subjects; the quoted split must belong to another dataset in [3]. |
| 21 | [2] uses a separate validation session | l5 | correct | Within-subject session split, not a held-out-subject design; the M12 comparison should say so. |
| 22 | Kappa below 0.04; word accuracy at most 2.9% vs 1.7% chance | t38, t31, t32 | correct if 60 classes | If Table 1's 30 word classes is right, chance is 3.3% and 2.9% is below chance. The review flags the 30/60 conflict but not this consequence. |
| 23 | Above-chance lexical results "come from" test-subject early stopping | t33, t23 | judgment beyond evidence | Early stopping on the test subject can inflate scores; the quotes do not show that the significance depends on it. |
| 24 | "first systematic benchmark" and "remains untested" (Abstract) | t1 | quote mismatch | t1 says "first controlled benchmark ... specifically for speech" (Sec. 1). "Remains untested" has no quote. "Neither is cited" rests on no quote from the target's reference list. |
| 25 | Chronology of [2] (arXiv 2504) and [3] (arXiv 2509) as prior | Reference list | correct | Both more than 6 months before the target (arXiv 2607); fair to treat as prior and as missed citations. |

## Central claim and confounds

The strongest confound is the starting point: the target's within-subject numbers (27.7-30.2%) sit far below published same-corpus results for the same model classes. The review uses this to call M06 "behind", which is reasonable, but its comparators differ in protocol (linear probe, test-time training, 5-fold CV, and a competition figure the target says is a validation score). The review notes "Splits differ" in one place and "same split" in another; it should state one protocol per comparator. The M06 "behind" verdict is defensible on the CBraMod and LaBraM fine-tuning numbers alone; it should not rest on the disputed 82.6%.

## Required fixes (ordered by impact)

1. Check the CBraMod paper (Wang et al., ICLR 2025, arXiv:2412.07236) BCIC2020-3 results. If fine-tuned LaBraM reaches about 0.50 there, revise "near 25% within subject" and "not new" in the Verdict: prior evidence on LaBraM for this corpus is mixed, and the target's 27.7% then points to its own training recipe. Cite it as a deciding prior and consider it for the M03 state of the art.
2. Resolve the split contradiction: Verdict says CBraMod 0.3976 is "on the same split"; M06 says "Splits differ". State the protocol of each comparator (linear probe, test-time training, 5-fold CV, competition split) and of the target.
3. Add the linear-probe condition to "near 25%" in the Verdict, and the test-time-training condition to 0.5898 in the M03 text and table row; quote the column headers of the [3] table so the LaBraM column is verifiable.
4. Either quote the passage of [4] that ties 82.6% to the test set or soften the "Where the claims outrun" bullet and the M06 state-of-the-art line; do not rest the M06 verdict on that figure.
5. Correct "Four CNNs" in the M06 row to three baselines (EEGNet, ShallowFBCSP, EEGConformer) and two foundation models, and drop "compact CNNs" for EEGConformer.
6. Correct "one recipe": the learning rate differs between baselines and foundation models (t22).
7. Replace the [3] validation-subject example (subjects 1-28/29-32, not BCIC2020-T3) or name its dataset; note that [2]'s validation session is a within-subject design.
8. Rephrase "Above-chance lexical results come from test-subject early stopping" to "may be inflated by"; the evidence shows the protocol, not the effect size.
9. In the 30/60-class bullet, add the consequence: with 30 classes, chance is 3.3% and the best word accuracy (2.9%) is below chance.
10. Quote the target's exact wording ("first controlled benchmark", Sec. 1) and add quotes for "remains untested" and for the target's reference list supporting "neither is cited".
11. Add a quote naming BCIC2020-T3 for [5] or drop "subjects, classes and recordings do not [differ]".
12. Add the quote from Sec. 4 that proposes speech-specific pretraining (t61 is truncated before it).
13. Label "under-trained models are being compared" and "cannot separate pretrained from compact models" as inference, or support them with a same-corpus fine-tuned result (see fix 1).
14. Fix the M06 usual-approach counts: do not mix the 167 pattern-match set with slot-filled counts; give one denominator, and correct the table row "slot-filled 48".
15. M12: say "most frequent (46 of 153; fixed held-out subjects 41)" rather than "usual design".
16. M13: the verdict "not reported" conflicts with the column "Laboratory"; make them agree.

## Scores

- Procedure: 6/10. Claim table is complete and most quotes match, but several comparator conditions (linear probe, test-time training, dataset identity) are not quoted, and one likely deciding prior on the same corpus is missing.
- Final text: 6/10. Clear position and correct arithmetic; weakened by an internal split contradiction, the model-count error, the "one recipe" error and a reversal of the authors' 82.6% statement without a decisive quote.

The review correctly identifies uncited prior benchmarks of LaBraM on speech EEG, the test-subject early-stopping issue, and the 30/60 class inconsistency.
