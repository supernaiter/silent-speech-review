# Evaluation: Deep Audio-Visual Speech Recognition (review)

Date: 2026-11-16. Independent evaluator, one pass. No claim table was supplied, so claims were checked against the review's own internal consistency and the evaluator's knowledge of the target and the cited works. No sources were re-read.

## Claim table

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | LRS2-BBC test: 1,243 utterances, 0.5 h, 6,663 words | Target Table 1 (from knowledge) | correct | Matches the target's dataset table. |
| 2 | Video-only gap 15.2 points without LM, 6.4 with LM (Table 2) | Target Table 2 (65.0/49.8; 54.7/48.3) | correct | Arithmetic consistent. |
| 3 | Clean AV: CTC 8.2% vs seq2seq 8.5% | Target Table 2 | correct | |
| 4 | "Over 22%" gain from 70.4% baseline (48.3%) | Target §1, Table 2 | correct | 70.4 − 48.3 = 22.1. |
| 5 | Gain over the group's own Transformer (50.0%) is 1.7 points | Internal arithmetic | insufficient evidence | Arithmetic correct; the 50.0% figure in [2] could not be confirmed without a quote. |
| 6 | LM-free like-for-like gap 20.6 points, −29% relative | Internal arithmetic | correct | 20.6 / 70.4 = 29.3%. |
| 7 | Noisy: CTC 23.6% vs seq2seq 34.2%; Google S2T 86.3% | Target noisy-audio table | insufficient evidence | Values not confirmable from memory; no quote supplied. Verify against the table before publication. |
| 8 | Beam 100 vs 35, α 0.5 vs 0.1 (Appendices C–D); beam 6 without LM | Target appendices | insufficient evidence | Plausible; the beam-6 inconsistency is a strong claim and needs the quoted location. |
| 9 | GPU: GTX 1080 Ti (§5.4) vs Titan X (§6.4) | Target §5.4, §6.4 | insufficient evidence | Plausible; needs quote. |
| 10 | Training noise is 0 dB babble, same as the test noise | Target §5.3 | correct | |
| 11 | Speaker column in Table 1 is "-" | Target Table 1 | correct | |
| 12 | LRS3 paper says LRS2 people likely recur [3] | [3] | insufficient evidence | Plausible; needs quote. |
| 13 | Binomial SE near 8.5% on 6,663 words ≈ ±0.34 points | Arithmetic | correct, but approximate | sqrt(0.085·0.915/6663) = 0.0034. Ignores utterance-level clustering and insertions; the paired difference has its own SE. |
| 14 | "The group's concurrent paper had already compared CTC with a Transformer" | Chronology | wrong (framing) | [2] (arXiv June 2018) is within 6 months of the target (Sept 2018) and is labelled [concurrent]; "had already" treats it as prior. |
| 15 | M06 state of the art: joint CTC/attention [7], "named as state of the art in 2024 [8]" | SOTA check | insufficient | No year/metric/value; [8] is a personalisation paper, not a benchmark source. |
| 16 | M11 state of the art: ViCocktail [9], VoxLRS-SA [8] | SOTA check | insufficient | No metric/value; a Vietnamese dataset is a weak reference point for English speaker-disjoint evaluation. |
| 17 | M12 state of the art: concurrent LSVSR bootstrap SDs [12] | SOTA check | insufficient | A 2018 concurrent paper is not "the best work today". |
| 18 | Curriculum wording "almost identical to WLAS §3.1" | Fairness | correct but framed unfairly | Same authors; reuse of own wording, not borrowing. |
| 19 | Reference list completeness | References | wrong | [14] is never cited in the text. |
| 20 | Reference [1] bibliographic data | References | incomplete | Published in TPAMI vol. 44, no. 12, pp. 8717–8727 (2022); 2018 is early access. |
| 21 | M09/M10 both "slot-filled 82" | Table | insufficient evidence | Identical counts for two slots; confirm this is not a copy error. |

## Required fixes (ordered by impact)

1. **Sentence:** "Its CTC vs seq2seq study on one Transformer encoder (M06) is standard: the group's concurrent paper had already compared CTC with a Transformer on LRS2 [2], ..."
   **Wrong:** [2] is concurrent (within 6 months) and is labelled so in the references; "had already" treats it as prior work. The M06 count also says "0 prior", so the "standard" verdict rests on concurrent work only.
   **Fix:** "...is standard: the same group's concurrent paper compares CTC with a Transformer on LRS2 [2], and no prior work in the ledger does so; ..." and keep the verdict justified by the confounds (beam, LM weight, fusion) rather than by priority.

2. **Sentence:** "**State of the art:** joint CTC/attention training, introduced for in-the-wild AVSR by the concurrent [7] and named as the state-of-the-art recipe in 2024 [8] and used in 2025 [9], removes the either/or question this paper asks."
   **Wrong:** No year, metric or value for a current best system; [8] (personalised lip reading) and [9] (Vietnamese data collection) are not benchmark sources.
   **Fix:** Cite a current hybrid CTC/attention system with its reported numbers, e.g. Ma et al., "Auto-AVSR" (ICASSP 2023): LRS3 WER 19.1% visual-only and about 0.9% audio-visual, LRS2 visual-only about 14.6% (verify values), all trained with joint CTC/attention.

3. **Sentence:** "**State of the art:** speaker-disjoint tests: concurrent LRS3-TED [3] says TED speakers rarely repeat whereas LRS2-BBC people likely recur; ViCocktail (2025) [9] picks test speakers absent from training; VoxLRS-SA (2024) [8] targets unseen-speaker adaptation."
   **Wrong:** No metric/value; ViCocktail is Vietnamese and not comparable for English benchmarks; the strongest point (LRS3's speaker-disjoint split) is concurrent, not later.
   **Fix:** Lead with LRS3-TED as the concurrent speaker-disjoint benchmark that became the field standard, state the speaker-disjoint split property as the reported design, and drop or demote ViCocktail to a supporting example. Mirror this in the table cell "speaker-disjoint test [9]" (change to [3]).

4. **Sentence:** "**State of the art:** the concurrent LSVSR reports bootstrap standard deviations on every WER [12]."
   **Wrong:** A concurrent 2018 paper is not the current state of the art in reporting practice.
   **Fix:** Either label it "an early exception, concurrent" and say current practice is still single runs, or cite a later work that reports seeds or confidence intervals on LRS2/LRS3.

5. **Sentence:** "On 6,663 test words the binomial error near 8.5% is about ±0.34 points (one SE), so the clean AV CTC vs seq2seq ordering is unresolved."
   **Wrong:** The binomial model ignores utterance clustering and insertions, and the two systems are evaluated on the same utterances (paired); the stated SE is an approximation, not a property of the paper.
   **Fix:** "Under a simple binomial approximation over 6,663 words (ignoring utterance clustering), one SE near 8.5% is about 0.34 points; the 0.3-point gap is below that, so the ordering is unresolved."

6. **Sentence:** Reference "14. Sterpu, G., Saam, C., Harte, N. 'Can DNNs Learn to Lipread Full Sentences?' ..."
   **Wrong:** Never cited in the text.
   **Fix:** Cite it where it carries a claim (e.g. as a concurrent sentence-level lip reading comparison in M06) or remove it from the list and refs.bib.

7. **Sentence:** Reference "1. Afouras, T., ... *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 2018. doi:10.1109/TPAMI.2018.2889052."
   **Wrong:** Incomplete; 2018 is the early-access date.
   **Fix:** Add "vol. 44, no. 12, pp. 8717–8727, 2022 (early access 2018)".

8. **Sentence:** "The curriculum (§5.2) is called 'a new strategy' in wording almost identical to WLAS §3.1 [5]."
   **Wrong:** WLAS shares authors with the target; as written it reads like an accusation of borrowing.
   **Fix:** "The curriculum (§5.2), called 'a new strategy', repeats the authors' own WLAS curriculum (§3.1 of [5])."

Also verify before publication (not counted as fixes, no quote available): noisy-condition values 23.6% / 34.2% / 86.3%; beam 6 in Appendix C; GPU models in §5.4 and §6.4; identical "82" counts for M09 and M10.

## Scores

- Procedure: 7/10 (positions are tied to locations in the paper; state-of-the-art lines lack year/metric/value; one concurrent work treated as prior).
- Final text: 7/10.
