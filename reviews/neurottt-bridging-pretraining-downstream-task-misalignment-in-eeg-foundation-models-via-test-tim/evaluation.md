# Evaluation: NeuroTTT review

Date: 2026-11-23
Evaluator: a language model separate from the writer

Scope: I had only the evaluator brief and compact.md (the review, references and claim table). I opened no sources and did no web search. Outside knowledge is marked "unverified".

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | NeuroTTT changes M02 (added SSL losses) and M03 (test-time updates) | CT 1 (Sec. 1) | correct | The contributions quote is thin, but CT 6 and CT 8 back up the two-stage design. |
| 2 | The M02 effect appears only in a CBraMod figure with no numbers in the text | CT 2, 8, 25 (Fig. 3, Sec. 4.3) | insufficient quote | The quotes support "CBraMod only". They do not show that the text gives no numbers. |
| 3 | The SSL test-time step never beats Tent on balanced accuracy (Tables 1–3) | CT 3, 12 | partly correct; insufficient quote | The Table 1 CBraMod and LaBraM values and the Table 2 Tent row are quoted. The Table 2 SSL row (0.7196, 0.7161) and every Table 3 value (0.5674, 0.5435, 0.45110, 0.43835) are not quoted. The "as the authors note (Sec. 4.2)" quote (w4) is not shown. All the gaps lie inside the reported ± (for example 0.5898±0.0148 vs 0.5887±0.0170). |
| 4 | 0.5898 is 23.6 points, or 29% relative, below 82.6% [2] | CT 4, 15 | arithmetic correct; comparability not shown | 82.6 − 58.98 = 23.62, and 23.62/82.6 = 28.6%. [2] says the test data were released. [4] says the official test labels are not public and reports on the validation split (CT 11). The review also asks the authors which trials are their test set (Questions). So the comparison may not be on the same test set. |
| 5 | M02 usual approach: 37 of 40 have no added loss, and the pretext tasks match only the target | CT 5, 26, 27; Appendix | correct (internally consistent) | 37 + 3 = 40, which matches the Appendix. |
| 6 | 150 vs 100 epochs, so training length and objective are confounded, for imagined-speech runs | CT 9 (Sec. 4.1) | correct in substance; insufficient quote for "imagined-speech" | The quote does not name the dataset. |
| 7 | M02 SOTA: the MLP row is 0.4733 (Table 1) | CT 7 | correct | The two [later] studies are not named. That is acceptable because they postdate the target, but it leaves the SOTA line without a cited work. |
| 8 | M03 usual approach: "38 unique studies (pattern match)" | CT 10 vs CT 28 | wrong (internal inconsistency) | The Appendix gives 26 unique pattern-match studies in the ledger and 38 with full-text hits, an upper bound. The body uses the upper bound as if it were the ledger count. "Both counts including the target and [3]" is ambiguous, because [3] uses entropy minimization only. |
| 9 | M03 SOTA: [4] fine-tunes LaBraM-Base to 27.7% BAcc, "30.2% at best" | CT 11 | wrong attribution | The quoted row shows 30.2±4.4 for EEGConformer, not LaBraM-Base. The column header is not quoted, so "balanced accuracy" is not shown. [4] is also a fine-tuning benchmark with no test-time adaptation, so it is not the state of the art for an adaptation component. The M03 summary row repeats this ("30.2% BAcc"). |
| 10 | The 11.7-point lead over the MLP row is mostly Stage I (inference) | CT 13 | arithmetic correct; position too strong | 58.98 − 47.33 = 11.65. M02 says length and objective are confounded, so the residual is "Stage I objective plus 50 extra epochs", not Stage I. "Modest" (Sec. 4.3) gives no numbers to apportion the lead. |
| 11 | SHOT starts from a classifier trained on a fixed backbone (Appendix B.4) | none | no claim-table row | This is a baseline-strength claim with no quote. |
| 12 | M12 usual approach: 10 of 16 use a subject-independent term, 4 use cross-validation | CT 14, 32, 33 | correct as a tally; plausibility questionable | The Track 3 competition protocol is subject-specific. A term count is not a design count. Stated as "the usual approach", it may mislead. |
| 13 | Cross-subject runs are at chance; tests use subjects 8–9 and 33–36 | CT 14, 16 | correct | |
| 14 | No seed count, no definition of ±, no significance test | CT 16, 23 | insufficient quote (absence claim) | This is plausible, and the Questions section carries it. |
| 15 | M13: Stage I is called free at deployment; one Adam step per sample "through the whole model" (Table 7) | CT 18 | correct, except "whole model", which is not quoted | The quote "adding no additional deployment cost" does not show which stage it refers to. |
| 16 | [5]: under 1% of parameters updated, about 2.44 ms per chunk "on a CPU" | CT 19 | partly insufficient | The "<1%" quote matches. The 2.44 ms quote says "respectively" but gives no hardware, so "on a CPU" is not shown. [5] covers intracortical decoding with session-specific retraining of a few parameters on new-session data, not unlabeled per-sample EEG adaptation. It is not like-for-like and needs a caveat. |
| 17 | "State-of-the-art performance" (Abstract; Sec. 5) | CT 20 | insufficient quote | The quoted t6 text says "outperforming conventional fine-tuning and adaptation methods". It does not contain the phrase "state-of-the-art". |
| 18 | "Markedly higher" fails for LaBraM on speech, 0.2742 vs 20% chance | CT 21 | judgment misframed | "Markedly higher" in the abstract most likely refers to the gain over the models' own fine-tuning baseline, not to chance. The LaBraM supervised row from Table 1 should be the comparison, and it is not quoted. |
| 19 | Public code: validation is built from the test subjects, checkpoints are selected on validation kappa, and the test-time script uses SGD with five steps | CT 22, 24 | insufficient evidence | Only file:line locators are given. No code excerpt or commit hash is quoted, and the paper quotes (t90, t108) state the opposite design. This is the most serious charge in the review. |
| 20 | Chronology labels: [3] concurrent (2509.24700), [5] concurrent (2506.05320, about 3 months before), [4] later (2026), [2] prior (2022) | references | correct | No later work is treated as prior or as a missed citation. |
| 21 | 82.6% is the best result on BCIC2020 Track 3 | CT 15; outside knowledge | unverified | I cannot confirm whether a later same-corpus result exceeds it. |
| 22 | M03 SOTA candidates | outside knowledge | unverified | EEG-specific unlabeled test-time adaptation work, such as T-TIME (Li, Wang, Wu; IEEE TBME, around 2023/2024), would be a closer state-of-the-art reference for M03 than the fine-tuning benchmark [4]. The year and values are unverified. |

## Central claim and strongest confound

The central position is that the state-of-the-art claim is internal, 23.6 points below the competition winner. The strongest confound is the evaluation split. [2] reports scores on released test data. [4] says the official test labels are unavailable and reports validation-split results, where its best model reaches only 30.2%. The review itself asks which trials the authors used. The Verdict nonetheless states the 23.6-point gap as a same-corpus fact. A second confound, training length (150 vs 100 epochs), is named in M02, but M03 then ignores it when it assigns the lead to Stage I.

## Required fixes (ordered by impact)

1. **Code-based leakage and optimizer claim (CT 22, 24).** Quote the relevant code lines and record the repository commit hash in the claim table, or move the claim to Questions only. As written, a test-subject leakage charge rests on locators alone.
2. **82.6% comparison (Verdict, M12, Where-claims bullet 1).** State that the competition score is on the released test set. State that [4] reports the official test labels as unavailable and uses the validation split. State that the paper's split is unknown. Say what the 23.6-point gap is conditional on. Reconcile [2] ("test data were released") with [4] ("test labels not publicly available").
3. **M03 state of the art (body and summary row).** 30.2% belongs to EEGConformer, not LaBraM-Base. Quote the column header to support "balanced accuracy". Replace [4] as the M03 state of the art with an unlabeled test-time adaptation work, or relabel it as a same-corpus fine-tuning reference.
4. **M03 usual-approach count.** Use 26 ledger pattern matches, matching the Appendix, and give 38 only as the full-text upper bound. Make clear that [3] counts under entropy minimization only.
5. **Tent vs SSL (Verdict, M03).** Quote the missing Table 2 SSL and Table 3 rows and the Sec. 4.2 author statement. Say the differences lie within the reported ± and are untested, for example "never higher than Tent; all gaps within one reported ±".
6. **Attribution of the 11.7-point lead.** Assign it to "Stage I objective plus 50 extra epochs", in line with the M02 confound.
7. **"Markedly higher".** Compare LaBraM's NeuroTTT speech result with LaBraM's own fine-tuning row (quote it), not with chance. Otherwise drop the bullet.
8. **[5] comparator.** Quote the hardware for 2.44 ms or remove "on a CPU". Note that [5] uses a different modality (intracortical) and a session-retraining setting.
9. **SHOT claim (Appendix B.4).** Add a claim-table row with a quote, or remove the claim.
10. **"State-of-the-art performance".** Quote the passage that actually uses the phrase (Abstract or Sec. 5).
11. **M12 usual approach.** State that the tally counts term mentions. Note that the Track 3 protocol itself is subject-specific, so "subject-independent" is not shown to be the typical design.
12. **Epoch confound scope.** Quote the dataset that gets 150 epochs, or drop "imagined-speech".
13. **M02 labels.** Explain why a design that is unique in the ledger receives `standard`, for example "effect not shown in numbers". The SOTA line cites no work, so say plainly that no prior comparator exists.

## Scores

- Procedure: 7/10. The claim table is thorough and arithmetic is marked as inference. The weak points are missing quotes for several decisive numbers, the code claim and SHOT.
- Final text: 6/10. The position is clear, but there is a misattributed comparator value, a count inconsistent with the Appendix, and the central 82.6% comparison is stated without its split caveat.

The review correctly flags the epoch confound, missing seeds and significance tests, the unreported test-time cost, and the absence of any external comparison.
