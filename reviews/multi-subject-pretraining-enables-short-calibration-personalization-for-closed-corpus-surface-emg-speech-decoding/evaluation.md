# Independent evaluation: Multi-Subject Pretraining Enables Short-Calibration Personalization for Closed-Corpus Surface EMG Speech Decoding

Date: 2026-11-22
Evaluator: fallback evaluator (claim table only). Input was the compact review with its claim table. No sources were opened; "insufficient evidence" means the claim-table quote does not carry the number or condition, not that the claim is wrong.

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | 27-person cohort, 21.3 min per participant (Verdict, M12) | Row 1, 19, Abstract quote | correct | Quote gives 27 and 21.3 min. |
| 2 | Evaluation-sentence repetitions from other participants remain in pretraining (§3.2) | Row 3 quote | correct | Quote says "all other usable ... trials were retained, including the remaining repetitions of the five evaluation sentences". It does not say these are only other participants' trials. If the held-out participant's own calibration trials also include those sentences, "already seen from other people" understates the leak. |
| 3 | Unseen-sentence CER 78.6%, WER 99.9% (Table 3) | Rows 18, 21 | correct | Matches quote. |
| 4 | Closed-corpus baseline WER 31.9% (Verdict) | Rows 3–4 | insufficient evidence | No quote has 31.9. Table 2 gives 31.7 WER for 3 min. The full-pool WER needs its own quote. |
| 5 | "3-minute result measures how fast a model recognizes sentences already seen" | Rows 3, 4, 18 | correct, with a caveat | This is an inference from §3.2 and Table 3. The wording is acceptable, but see check 2. |
| 6 | Zero-shot 49.3% to 21.7% CER, 27.6 points, 56% relative | Row 13, 15 | correct | 49.3 − 21.7 = 27.6. 27.6 / 49.3 = 56.0%. This is arithmetic, not inference, so the "(inference)" label is not needed. |
| 7 | Direct checkpoint fine-tuning 68.0% CER; about 282 vs 263 target trials | Row 14 | insufficient evidence | The quote confirms the control "was not strictly matched in calibration data". It does not give 68.0, 282 or 263. |
| 8 | Pool-size curve 74.4% to 21.7% CER, 1 to 26 participants | Row 15 | correct | Matches quote. |
| 9 | Only 16 of 27 improved at every step (§4.4) | Row 15 | insufficient evidence | Not in quote. |
| 10 | 3 min vs full pool p = 0.27; authors call it no equivalence result | Row 22, 27 | correct | p value matches. The quote says "no statistically significant difference". |
| 11 | 10 min 18.6% CER, p = 0.030 | Row 23 | correct | Matches quote. |
| 12 | "consistent with fixed epochs changing update counts (Table 2 note)" | Row 23 | insufficient evidence | No quote shows a fixed-epoch schedule. |
| 13 | "One unreported seed is used (§3.5)" | Row 24 | wrong as worded | The quote is about the seed that selects the pretraining pool ("randomly selected ... using a fixed seed"). It does not show a single training seed or say the value is unreported. |
| 14 | Checkpoint-vs-random gap 23.2 points; 9.7 on converged folds | Row 25 | insufficient evidence | The quote supports 5 of 27 non-converged folds at 100% CER only. Neither 23.2 nor 9.7 is quoted. |
| 15 | Adapter −0.8 points, tested only with 26 in pretraining | Row 26 | insufficient evidence | The quote supports "no detectable benefit". It does not give −0.8 or the 26-only condition. |
| 16 | Nearest-template baseline 60.3% CER | Row 20 | insufficient evidence | The quote says only "well above chance". |
| 17 | Wand & Schultz [2]: leave-test-speaker-out training plus MLLR beat zero-shot; no gain beyond 120 words | Row 9 | insufficient evidence | The quote supports the leave-speaker-out training design and is cut off at "beyond 120 words does not". The MLLR-over-zero-shot result is not quoted. |
| 18 | Wu et al. [3]: 28 subjects pretrained, 4 new fine-tuned, 1–8 sessions, 100 phrases | Row 10 | insufficient evidence | The cut-off quote does not carry any of these four numbers. |
| 19 | Scheck [4]: cross-speaker pretraining fine-tuned on one session beat scratch (p < 0.01), four speakers, "In 2026" | Row 8 | partly wrong | p < 0.01 matches. The located experiment is Scheck et al. 2024 (EMBC), so the year of the result is 2024, not 2026. "Four speakers" and "one session" are not quoted. |
| 20 | "2023 work the target cites [4]": more training speakers raised accuracy | Row 11 | wrong citation | The quote is the dissertation describing someone else's work ("They saw..."). Cite the 2023 primary work, not [4]. |
| 21 | Benster et al. [6] 12.2% WER, open vocabulary, one speaker, 2024 | Row 17 | correct | Matches quote (Gaddy benchmark, single speaker). |
| 22 | Gaddy & Klein [5] 42.2% WER, 2021 | Row 17 | insufficient evidence | The claim table quotes only [6]. The value matches the published result as far as the evaluator knows, but it needs its own row. |
| 23 | M03 usual approach: per-participant models are "the default" (90 of 379) | Rows 6, 33, 34 | insufficient evidence / inconsistent | 90/379 = 24%. That supports "most common" only if no other design is larger. Row 33 gives 370 pattern-match studies and row 34 gives 379. |
| 24 | M03 sEMG subset: 76 studies, 40 / 13 / 13 | Rows 7, 29, 30 | inconsistent | Row 29 says the M03 ledger has "64 unique studies pattern match", but the body says 76. 64 is also the M12 count (row 36). One of the two numbers is wrong. |
| 25 | "training-pool-size sweep, which only the target matches" | Rows 7, 11 | wrong / contradicted | The review cites 2023 work in which more training speakers raised cross-speaker accuracy. That is a training-pool variation. The absence claim names no deciding priors for this design. |

## Central claim and confound

The strongest confound is the closed corpus. The test sentences are repeated in training, so the 3-minute result does not show decoding of new sentences. The review handles this well: it puts this confound first, quotes §3.2, and gives the collapse on unseen sentences (Table 3). Two other confounds are handled correctly: the direct fine-tuning control has a different starting point and amount of data, and the M12 comparison with [5] and [6] has different data volumes. The sentence calling the 3-minute point a "plateau the target finds" contradicts the review's own statement that 3 min is not shown to be equivalent and that 10 min beats the full pool. It also gives the target a finding the authors explicitly decline to claim.

"Nearer sentence identification than decoding" goes further than the evidence. The decoder (21.7% CER) is far better than the template baseline (60.3%). The baseline shows that sentences are partly separable from EMG alone; it does not show that the decoder is doing identification.

## Fairness and chronology

[4] is a 2026 dissertation, labelled "Prior", for a September 2026 target. If it appeared within six months of the target, it is concurrent and cannot serve as state of the art the authors should have known. The underlying 2024 EMBC paper should be cited directly. The review correctly credits the authors with disclaiming the paradigm (§1).

## Verdicts

M03 `standard` follows from the named priors [2] and [3]. M12 `behind` rests on the design count: sentence-disjoint tests (13) outnumber closed-set tests (9), and the review cites [5] and [6]. The review states the different starting point. This is acceptable. M11 has the verdict `not reported` while the row describes the reference set (50 TIMIT sentences, 45/5 split). The verdict label does not fit the content.

## Required fixes (ordered by impact)

1. Delete "the plateau the target finds at 3 minutes". It contradicts §4.2 and Table 2 (10 min beats the full pool, and the authors make no equivalence claim).
2. Remove or support "a training-pool-size sweep, which only the target matches". The review's own 2023 citation varies the number of training speakers. Name the deciding priors, or limit the claim to calibration budgets in minutes combined with a 1–26 pool sweep.
3. M03 state of the art: cite Scheck et al. 2024 (EMBC) directly with year 2024. Check the dissertation's date against the target and label it [concurrent] if it is within six months.
4. Cite the 2023 primary work for "more training speakers raised cross-speaker phrase accuracy" instead of [4].
5. Reconcile the Appendix counts: 370 vs 379 pattern-match studies for the per-participant tally, and 64 (row 29) vs 76 (body) for the M03 sEMG subset.
6. Reword "One unreported seed is used". The quoted fixed seed selects the pretraining pool. State what is actually single-seed, with a quote.
7. Add claim-table quotes for the unquoted numbers: 31.9% WER, 68.0% CER and 282/263 trials, 16 of 27, 23.2 and 9.7 points, −0.8 points and the 26-only condition, 60.3% template CER, 42.2% WER [5], Wu et al. 28/4/1–8 sessions/100 phrases, Wand & Schultz MLLR over zero-shot, Scheck four speakers / one session, and the fixed-epoch Table 2 note.
8. Check whether the held-out participant's own calibration trials include the evaluation sentences. If they do, say so in the Verdict instead of "already seen from other people".
9. Soften "nearer sentence identification than decoding". The decoder is far below the template baseline, which shows only partial separability.
10. Replace "remain the default" for per-participant models (24% of the tally) with "most common design", or with the share, unless the Appendix shows it is the plurality.
11. Fix the M11 verdict `not reported`, which conflicts with the reported reference set in the same row.
12. Drop "(inference)" after the 27.6-point / 56% figure. It is a calculation from Table 1.

## Scores

Procedure: 6/10. The claim table carries the main numbers, but many quotes are cut off or omit the cited figure, and the Appendix counts disagree.
Final text: 6/10. The central confound is identified and argued well. One internal contradiction (the plateau), one unsupported absence claim and one misdated state of the art need fixing.
