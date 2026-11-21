# Independent evaluation: Improving the Gap in Visual Speech Recognition Between Normal and Silent Speech Based on Metric Learning

Date: 2026-11-21. Fallback evaluator (claim table only). Input: the compact review, its claim table and reference list. No sources were opened; arithmetic was recomputed from the quoted values, and bibliographic and state-of-the-art notes rely on the evaluator's own knowledge (marked).

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target changes training (M03) with KL terms on viseme posteriors across modes | CT 1 (Sec. 1, Secs. 3.2-3.3) | correct | Quotes support a metric-learning loss on viseme probability distributions. |
| 2 | Normal-to-silent WER gap: 10.97 (normal-only) -> 2.70 (two-mode CE) -> 1.77 (full loss) | CT 3, 15 (Table 1 rows t30, t31, t42) | correct | 22.55-11.58 = 10.97; 12.91-10.21 = 2.70; 9.97-8.20 = 1.77. |
| 3 | Two-mode CE baseline "does 75% of it"; metric terms add 0.93 points | CT 15 | correct but ambiguous | 8.27/10.97 = 75% of the original gap. Of the total gap closed by the full model (9.20 points), the baseline accounts for 90%. "It" must be specified. 0.93 is correct. |
| 4 | Headline silent WER 12.91% -> 9.97%; 2.94 points, 22.8% relative | CT 4, 9, 16 | correct | 2.94/12.91 = 22.8%. |
| 5 | "One run per row" in Table 1 | CT 4, 20, 23 | insufficient evidence | No quote states the run count; it is inferred from missing spreads. Fig. 3 caption (CT 18) says "VER over five experiments", so the authors did repeat runs elsewhere. The safe statement is "no run count or spread is reported for Table 1". |
| 6 | Loss weights chosen by a search whose selection data are not named | CT 4, 16 (Sec. 4.2) | correct | Quote "adopted the parameters that achieved the best performance" supports it. A 400-utterance validation split exists (CT 22), so the wording should say the paper does not state which split was used, not imply test-set selection. |
| 7 | Silent VER spans 6.66-7.77% over the 13 loss combinations | CT 9 | wrong or insufficient | The normal-only row (LNCE) has silent VER 12.49% (CT 12). If it is one of the 13 experiments, the range is 6.66-12.49%. Restrict to the two-mode rows or quote all 13 rows. |
| 8 | +LNKL alone: best normal WER 7.36%, worst two-mode silent WER 13.45% | CT 17 | insufficient evidence | Values match the quoted row; "best" and "worst" need the remaining rows quoted. |
| 9 | Adding LSKL to the KL loss: silent VER 7.17 -> 7.35, silent WER 11.06 -> 10.71 | CT 17 | correct (conditional) | Values match the quoted rows, assuming +LSKL is nested under the LKL row. Normal WER also worsens (8.12 -> 9.36), which strengthens the point. |
| 10 | "Nearly 3%" (Sec. 1) is 2.94 absolute points | CT 16 | correct | |
| 11 | Fig. 3 holds normal data at 1,000 utterances, plots VER only | CT 18 | partly supported | "VER over five experiments" supports VER only. The quote "from 1,000 to 200 by 200" describes the varied quantity, not the fixed normal amount; no quote states normal data held at 1,000. |
| 12 | Fine-tuning comparator (Sec. 4.4) has no number | CT 19 | insufficient evidence | Absence claim; the quote only names the approach. Plausible, cannot be confirmed from the table. |
| 13 | [4]: 26.75% -> 25.14% silent WER, 6.0% relative | CT 5, 7 | correct | 1.61 points; 1.61/26.75 = 6.0%. |
| 14 | [4]: mean of 10 seeds, p = 0.002 | CT 7 | no quote | Neither number appears in a quoted passage. |
| 15 | [4]: seed-to-seed WER spread about 1 point | CT 5 | partly supported | Source says "standard deviation ... approximately 1%". "Spread" and "standard deviation" are not the same; say standard deviation. |
| 16 | [3]: domain-adversarial training gains 8.1 points silent WER (51.199% -> 43.114%), one model per row | CT 10 | partly supported | 51.199 is quoted; 43.114 and "one model per row" are not. 51.199-43.114 = 8.085, rounds to 8.1. |
| 17 | [2]: dropping non-parallel vocalized data costs 3.6 points | CT 10 | correct (referent unquoted) | Quote gives 71.6% and 3.6 points; "this data" is not identified in the quote. |
| 18 | [5]: normal-trained 61.2% vs silent-trained 64.4% on silent phrases (SDs 1.6, 2.3) | CT 13 | correct | Matches Table 2 quotes. |
| 19 | [5] uses "a split with the same 20/8/11 speaker counts" | CT 13, 22 | wrong per quote | The quoted [5] Sec. 4.2 reads "30, 10, ...", which does not match 20/8/11. Remove or support with a quote. |
| 20 | Target cites an 8.5-point drop in [5]; 69.7 -> 61.2 | CT 14 | correct | 69.7-61.2 = 8.5. |
| 21 | Normal-only model "doubles" its WER on silent speech (11.58 -> 22.55) | CT 14 | approximately correct | Ratio 1.95; "nearly doubles". |
| 22 | Target is the earliest of 5 studies with a divergence/metric/contrastive loss between modes; "the route is new" | CT 8 | insufficient evidence | The other four studies and the deciding priors are not named. [3] (arXiv April 2023) uses domain-adversarial alignment between silent and vocalized data, a mode-alignment objective that precedes the target's arXiv posting; the review must say why it does not count. |
| 23 | Verdict: tying overt and silent recordings is "common in EMG and ultrasound [2], [3]" | CT 2 | fairness issue | [3] is labelled concurrent; it cannot show prior common practice. [2] alone carries the claim. |
| 24 | M03 verdict "standard" | Sec. M03 | inconsistent | The same section calls the route new and the target the earliest. Either the verdict or the novelty sentence must change. |
| 25 | M12 verdict "not reported" | Table, Sec. M12 | insufficient evidence | Rests on claim 5 and on [4] as a standard; [4] is later work on a different task (open-vocabulary EMG-to-speech, ~26% WER), so its seed spread is an analogy, not a norm the authors could meet. |

## Strongest confound

Baseline strength: the gain is measured against a baseline already trained on both modes, and the review handles this well (claims 2-4). The remaining unhandled confound is task and regime mismatch in the comparators: [3] is speech reconstruction scored by ASR WER on synthesized audio, [4] is EMG-to-speech, and the target is a 10-phrase closed set. The review sets these gains side by side (2.94 vs 8.1 vs 1.61 vs 3.6 points) without saying they do not rank.

## Required fixes (by impact)

1. Remove "on a split with the same 20/8/11 speaker counts" for [5], or quote a passage that supports it; the quoted [5] split reads 30/10.
2. Replace "one run per row" (Verdict, M03, M12, table) with "no run count or spread reported for Table 1", and note that Fig. 3 averages five runs.
3. Resolve the M03 contradiction: "the route is new" and "earliest of 5" against the verdict `standard`. Name the four other studies and say why [3]'s domain-adversarial alignment is not counted as an earlier mode-alignment loss.
4. Drop [3] as support for "common in EMG and ultrasound" in the Verdict; it is concurrent.
5. Fix the silent VER range: 6.66-7.77% holds only if the normal-only row (12.49%) is excluded from the 13 combinations; say "over the 12 two-mode rows" or correct the range.
6. Add quotes for unquoted numbers: [4] 10 seeds and p = 0.002; [3] 43.114% and one model per row; Fig. 3 normal data fixed at 1,000; the rows that make 7.36% the best normal WER and 13.45% the worst silent WER.
7. Make "75% of it" exact: 75% of the original 10.97-point gap; 90% of the gap closed by the full model.
8. Write "standard deviation of about 1 point" for [4], and state that its seed spread comes from a different task and error regime, so it is an analogy, not the standard behind the M12 verdict.
9. State that [3], [4] and [2] measure WER on different tasks (speech reconstruction or EMG-to-speech, open vocabulary) and that their point gains do not rank against the target's 10-phrase WER.
10. Soften "selection data are not named" to "the paper does not say which split selected the weights", since a validation split exists.
11. Write "nearly doubles" (1.95x) for 11.58% -> 22.55%.
12. Check the venue of [3]; to the evaluator's knowledge (inference, medium confidence) it appeared at ICASSP 2023, which should replace "arXiv preprint" and still fits the concurrent label.

## Scores

- Procedure: 6/10. Every number has a location and most have quotes, but several load-bearing values have none, and one comparator condition contradicts its own quote.
- Final text: 6/10. The central point (most gap closing comes from adding silent data) is correct and well argued. The M03 verdict contradicts the novelty sentence, and the single-run claim goes beyond the evidence.
