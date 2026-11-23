# Independent evaluation: Physiological Noise Augmentation Improves Non-Invasive Brain-to-Speech

Date: 2026-11-23. Fallback evaluator (claim table only): checked against the review text and its claim table (quotes and locations). Original sources were not re-opened. Notes on state of the art and earlier designs come from the evaluator's own knowledge and are marked as such.

## Claim check

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Re-injecting recorded artifact signals from other trials was done two years earlier for EEG speech decoding [2]; the paper does not cite it | Claim rows 1, 5, 6; ref list | correct (partly insufficient) | arXiv 2407.07595 (Jul 2024) vs 2607.05165 (Jul 2026): two years, not concurrent, so flagging the missing citation is fair. The quote shows only EMG mixing ("mixing EMG scaled by a factor of α from different ..."); EOG mixing rests on a Table 4 row label with no column headers quoted. |
| 2 | At single trial PNA does not beat raw training (Table 1) | Claim rows 2, 11 | partly wrong | True for EEGNet (0.332 vs 0.337). For MLP, PNA is nominally higher (0.262 vs 0.255). Both differences are within one standard error. The sentence should name EEGNet or say "no difference beyond seed error". |
| 3 | At 10 trials EEGNet rises from 73.0% to 76.3% | Claim row 3 | correct | Sec. 4.1 quote matches. |
| 4 | Abstract and Sec. 1 claim +4.7 points and 77.6% | Claim rows 3, 13, 21 | correct (quotes) | Both numbers are in the quotes. |
| 5 | +3.3 points = 4.5% relative, 12% fewer errors | Claim row 13 | correct | 3.3/73.0 = 4.5%; 3.3/27.0 = 12.2%. Labeled as inference. |
| 6 | "No table contains 77.6%" | Claim row 14 | insufficient evidence | The support is a note on Tables 1–2 only ("Tables 1-2 top EEGNet value is 0.763"). Appendix tables and figures are not covered, and the review does not check whether 4.7 points is measured against another baseline row (for example Clean Only with averaging). |
| 7 | White noise 0.747 vs PNA 0.763 (EEGNet, Table 2); lead 0.016 with SE 0.011 / 0.012 | Claim rows 3, 16 | correct | Arithmetic is right. The absence of a test is labeled as inference. |
| 8 | MLP 10-trial: frequency shift 0.596, temporal shift 0.584, white noise 0.578 all beat Raw+PNA 0.574; Clean Only with averaging 0.581 | Claim row 8 | correct | All five numbers are in the quotes. |
| 9 | Baselines tuned on single-trial validation and applied after averaging, PNA before | Claim row 15 | correct | The Table 5 caption and Table 2 caption quotes support this. It is the strongest confound, and the review handles it. |
| 10 | The Sec. 5 conclusion says PNA reduces the repetition burden, with no accuracy-versus-repetitions comparison | Claim row 12 | wrong / no supporting quote | The Sec. 5 quote (t70) is about "the associated anisotropic Jacobian penalty substantially reduces the ...", not about repetitions. The claim about the authors' conclusion has no quote behind it. |
| 11 | Invariance is the stated goal (Sec. 3) and is never tested directly | Claim row 17 | insufficient evidence | There is no quote for the Sec. 3 goal. The absence claim is reasonable. The Verdict's "never measured" is stronger than the body text, which grants indirect evidence (embeddings, Fig. 4, Appendix C). |
| 12 | One subject and ten digits; the authors concede it (Sec. 5) | Claim row 18 | correct | Quotes match. |
| 13 | M03 usual approach: 45 studies; masking 12, additive noise 10, time shift 10; 4 artifact injection, two of which re-inject recorded artifacts | Claim rows 4, 24 | correct (counts) | Counts match the audit. The claim that two of the four re-inject recorded artifacts has no row of its own. A sixth design category (6) appears in the appendix but is not named. This is acceptable for a "commonest" statement. |
| 14 | M03 state of the art: Sato et al. EOG-only top-10 accuracy 28.8% to 5.02% (chance 2%), EEG 76.0% to 72.3% | Claim row 6 | correct, with column labels insufficient | The numbers are in the Table 4 rows and the chance level is in Sec. 4.4. The quote does not show which columns are EOG input, EEG input or top-10. |
| 15 | Related Work (Sec. 2) says neural augmentations lack draws from the empirical noise distribution | Claim row 7 | correct | The t36 quote supports this paraphrase. |
| 16 | M04 usual approach: 9 of 68 state single-trial decoding, and only this paper averages test trials | Claim rows 9, 28 | wrong / contradictory | The audit lists multi_trial_averaging = 3 (this paper, doi 10.3389/fnhum.2020.00290, and doi 10.3389/fnins.2020.00290). The last one is [3], which the review cites as the single-trial state of the art. "Only this paper" conflicts with the appendix, and [3] cannot be both an averaging match and the single-trial yardstick unless the review says the match was a false positive. |
| 17 | M04 state of the art: 93.24% single-trial on five imagined phrases, eight subjects [3]; chance 30% | Claim row 10 | insufficient evidence | The quote gives "90.38 ± 2.28%, 93.24 ± 2.87%" without saying which is imagined and which is spoken. The review must show that 93.24% is the imagined-phrase figure. 30% is the paper's empirical significance level, not the theoretical 20% for five classes; this is worth one clause. |
| 18 | M04 state of the art is current | Evaluator knowledge | insufficient evidence | The source is from 2020. The review does not say whether later single-trial imagined-speech MEG/EEG results were looked for. Either name a later result or say that none comparable was found in the ledger. |
| 19 | M04 verdict "behind" | Review text; brief item 7 | insufficient evidence | The review admits there is no like-for-like gap and bases "behind" on typical practice (9/68 single-trial). That is defensible, but it depends on fixing row 16. |
| 20 | M03 verdict "standard" | Review text | correct | A deciding prior is named and read in full (Appendix row 25). |
| 21 | M12 verdict "not reported" (unnamed split) | Claim row 20 | insufficient evidence | The support is a note ("split behind tables unnamed"), not a quote. The authors say validation and test sets are recorded separately, so the verdict depends on what the tables are scored on. Keep the verdict only if the text never says. |
| 22 | Component-table numbers (12,000 trials, 10:1:1, 5 seeds, slot-filled counts 4,015 / 31 / 8,898 / ...) | Claim table | no quote | These numbers have no claim-table rows. |
| 23 | Fairness: chronology of [2] and [3] | Ref list | correct | Both are well over 6 months before the target. |
| 24 | Fairness: the single-trial limitation is the authors' own point | Claim row 12 | partly | The M04 section credits the authors (Sec. 4.1). The Verdict presents it without attribution. |
| 25 | Earlier designs that mix recorded artifacts into neural data | Evaluator knowledge | note | EEGdenoiseNet (Zhang et al., 2021, J. Neural Eng. 18, 056057) builds semi-synthetic contaminated EEG by mixing recorded EOG/EMG into clean EEG at controlled SNR. It does this for denoising, not decoder augmentation, so it does not displace [2] as the deciding prior. It does show that recorded-artifact mixing predates both papers (medium confidence). |

## Required fixes (ordered by impact)

1. M04 usual approach: reconcile "only this paper averages test trials" with the appendix count of 3 multi-trial-averaging matches, which include [3]. Either state that the other two matches were checked and do not average test trials, or revise the sentence. Confirm that [3] is single-trial before using it as the single-trial state of the art.
2. 4.7 points / 77.6%: before calling the abstract inconsistent with the tables, check whether 4.7 points is measured against another row (such as Clean Only with averaging) or reported in an appendix table or figure. Limit "No table contains 77.6%" to the tables actually checked, or check all of them.
3. Sec. 5 "PNA reduces the repetition burden": the supporting quote (t70) concerns the Jacobian penalty. Supply the correct quote or drop the claim from M04.
4. "At single trial PNA does not beat raw training" (Verdict): limit it to EEGNet, or say that neither model differs beyond seed error. MLP is nominally higher with PNA (0.262 vs 0.255).
5. [3] 93.24%: show from the source that this is the imagined-phrase accuracy and name the model. Note that 30% is an empirical chance threshold.
6. [2] EOG mixing and Table 4: add a quote showing that EOG (not only EMG) was mixed, and quote the Table 4 column headers (input modality, top-10).
7. Verdict "is never measured": change to "is not directly tested", to match the body, which cites embedding evidence (Fig. 4, Appendix C). Add a Sec. 3 quote for the invariance goal.
8. M04 state of the art: say whether post-2020 single-trial imagined-speech MEG/EEG results were searched, and cite one if a stronger or more recent one exists.
9. Add claim-table rows for the component-table numbers (12,000 trials, 10:1:1 split, 5 seeds, slot-filled counts) and for "two of the four re-inject recorded artifacts".
10. M12 "not reported": back it with a quote, or with a location showing that the split behind Tables 1–2 is never named.
11. Verdict: attribute the single-trial limitation to the authors (Sec. 4.1), as the M04 section does.
12. Optional, M03: mention that mixing recorded EOG/EMG into clean EEG was already used to build denoising benchmarks (EEGdenoiseNet, 2021), so the novelty boundary is clear: decoder augmentation from the recording's own ICA components, not artifact mixing as such.

## Scores

- Procedure: 7/10. The claim table covers the central numbers, the main confound (baseline tuning and ordering relative to averaging) is handled, and the deciding priors are read in full. Points are lost to one mismatched quote, the M04 count contradiction, and unquoted table numbers.
- Final text: 6/10. The position is clear and mostly well supported. The M04 section rests on a self-contradiction, and two Verdict sentences go slightly beyond their evidence.

Strengths: arithmetic is correct throughout, inferences are labeled, the confound from tuning and averaging order is identified and backed by quotes, and the missing citation of an earlier prior is fairly dated.
