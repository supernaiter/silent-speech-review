# Evaluation: Multi-modality Associative Bridging through Memory (ICCV 2021)

Date: 2026-11-18. Independent evaluator, single pass, review text and claim table only (no source re-reading). The claim table was filled by the writer, so a matching quote shows consistency with the writer's notes, not independent verification. Knowledge-based remarks are marked "(evaluator knowledge)".

## Claim check

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Audio features stored in memory, recalled from video (M02), fed before backend (M06) | CT1 | correct | Quote supports paired visual/audio memories. |
| 2 | Gain over own baseline repeats on LRW, LRW-1000 and GRID | CT2, CT12; "What the field needs next" M06 | insufficient evidence / internal contradiction | No GRID no-memory baseline is quoted, and the review itself asks for "a no-memory baseline" on the speech route. |
| 3 | 85.41% is 2.5 points below 87.9% single model [2] | CT3, CT8 | correct | 87.9 − 85.41 = 2.49. |
| 4 | LRW-1000 50.82% leads by 4.2 over best earlier ensemble (46.6%) | CT10, CT22 | arithmetic correct; claim of leadership doubtful | Feng et al., "Learn an Effective Lip Reading Model without Pains", arXiv 2011.07557 (Nov 2020) reports 55.7% on LRW-1000 (with word-boundary input) and 88.4% on LRW (evaluator knowledge, medium confidence). Condition must be stated. |
| 5 | Headline numbers are best memory size, one run, no validation rule | CT4, CT23 | correct as an absence claim | Supplement-only scores acknowledged. |
| 6 | GRID STOI lead 0.007 over Lip2Wav; 1% relative | CT5, CT17 | correct | 0.738/0.731 = 1.0096. |
| 7 | MOS 2.93 vs 2.83, WaveNet 4.37, 14-fold step | CT19 | insufficient evidence | Quote shows only "2.93 ± 0.21 3.56 ± 0.19"; the 2.83 and 4.37 rows and their column (naturalness vs intelligibility) are not quoted. Arithmetic (1.44/0.10) correct if the values hold. |
| 8 | Usual approach M02: distillation 40 of 54; priors [3], [4] | CT6, CT7 | plausible | Distillation is the typical audio-into-video design for 2020–2021 lip reading. |
| 9 | "The paper departs by never forcing the visual feature to resemble the audio feature" | none | insufficient evidence | Not in the claim table. The method trains the recalled value-memory output to reconstruct the audio feature (evaluator knowledge), which is a regression target on audio features through the memory. |
| 10 | M02 state of the art today: LipGen 92.8% [5] | CT9 | doubtful as "best" | Ma et al., "Training Strategies for Improved Lip-reading", ICASSP 2022 (arXiv 2209.01383) report 93.4% single and 94.1% ensemble on LRW with word boundaries (evaluator knowledge, medium-high confidence). Conditions (boundary, extra data) not stated for LipGen. |
| 11 | MVM [6] 88.5% LRW, 53.82% LRW-1000 [concurrent] | CT10, CT11 | correct | Note [2] also reports 88.5% (ensemble) on LRW; the review keeps them apart correctly. Concurrent label right (AAAI 2022). |
| 12 | Memory adds 1.27 points LRW, 5.89 LRW-1000; relative error −8%, −11% | CT12 | LRW correct; LRW-1000 insufficient evidence | No quote for the LRW-1000 baseline (implied 44.93%). 55.07→49.18 gives 10.7%, consistent. |
| 13 | 0.91 points over the authors' distillation build (84.50%, Table 5) | CT13 | insufficient evidence | Quote lists four numbers without column labels; which column is distillation (and what 84.20 is) is not shown. Arithmetic correct. |
| 14 | No memory-recall hit first public before the paper | CT11, Appendix | insufficient evidence | No deciding prior is named. The authors' own key-value "Visual Voice Memory" (Hong, Kim, Park, Ro, IEEE/ACM TASLP 2021) is cited in M06 but not placed in time against the target in M02. |
| 15 | M06 usual approach: neural vocoder 49 of 165; paper uses Tacotron2 decoder + Griffin-Lim, WaveNet in one MOS row | CT14, CT15 | plausible | |
| 16 | M06 state of the art: WGAN WER 4.07% on GRID-4 from [7] | CT16 | doubtful as "best" | This is a baseline row of [7], not [7]'s own system; the review does not say whether [7]'s proposed model scores better. Later GRID video-to-speech systems (e.g. diffusion and unit-based models, 2023–2024) not considered. |
| 17 | Visual Voice Memory re-scored at STOI 0.643, WER 6.08% [7] | CT18 | correct | Caveat on scorer effects is well handled. |
| 18 | "Highest accuracies ... on both datasets" omits [2] | CT20 | correct | [2] arXiv July 2020; ICCV deadline March 2021, so the authors could have read it. Fair. |
| 19 | 5.58-point lead measured against Face Cutout 45.24% (non-public full-face version) | CT21 | correct | 50.82 − 45.24 = 5.58. |
| 20 | Architecture-independence claim tested on Bi-GRU only | CT24 | correct | |
| 21 | MOS: no scale, no ± definition, 6 clips per speaker | CT25 | correct | "25 raters" (M12 row) has no quote. |
| 22 | Chronology of [5] [later], [7] [later], [6] [concurrent] | References | correct | |

## Required fixes (ordered by impact)

1. **Sentence:** "The recall design is ahead: no earlier study among the 54 on audio-to-video knowledge transfer records it (pattern match, Appendix), and the gain over its own baseline repeats on LRW, LRW-1000 and GRID." together with "Verdict: ahead as a design; its advantage over distillation is not yet shown."
   **What is wrong:** An `ahead` verdict needs the effect repeated against the usual approach; the review itself says the only comparison with distillation (the usual design) is a single run on LRW, 0.91 points. A gain over a plain baseline does not make a design ahead of the field's usual design. The verdict and its own caveat contradict each other.
   **Fix:** Downgrade M02 to a non-`ahead` verdict (e.g. "novel design, advantage unproven"), or keep `ahead` only if a repeated comparison with distillation exists; update the Verdict paragraph and the table row accordingly.

2. **Sentence:** "...the gain over its own baseline repeats on LRW, LRW-1000 and GRID."
   **What is wrong:** No GRID no-memory baseline is quoted, and "What the field needs next" asks for "a no-memory baseline" on the speech route, implying none exists. Internal contradiction.
   **Fix:** Quote the GRID ablation (table and values) if it exists; otherwise change to "repeats on LRW and LRW-1000; on GRID only the comparison with Lip2Wav is reported."

3. **Sentence:** "on public LRW-1000 the 50.82% result does lead, by 4.2 points over the best earlier ensemble (inference)." (also "Against the public-version ensemble the lead is 4.2 points (inference).")
   **What is wrong:** Feng et al., "Learn an Effective Lip Reading Model without Pains" (arXiv 2011.07557, November 2020) reports 55.7% on LRW-1000 and 88.4% on LRW using word-boundary input, months before the target. The "does lead" statement holds at most under a no-boundary condition.
   **Fix:** Check that paper and state the condition: "leads among models without word-boundary input; Feng et al. (2020) report 55.7% with boundaries". Also consider it as a second omitted comparator in "Where the claims outrun the evidence".

4. **Sentence:** "Today LipGen reports 92.8% (2025, [5] [later]), a 7.4-point gap (inference)." (and table cell "LRW 92.8% [5]")
   **What is wrong:** Not clearly the best LRW result: Ma et al., "Training Strategies for Improved Lip-reading" (ICASSP 2022) report 93.4% single and 94.1% ensemble with word boundaries. LipGen's conditions (boundaries, extra training data) are not stated.
   **Fix:** Give the best result with its condition, e.g. "93.4% single model with word boundaries (2022); without boundaries, <best value> (<work, year>)", and recompute the gap.

5. **Sentence:** "None of the 12 memory-recall hits in the Appendix count is first public before the paper; the hits are the paper itself and [concurrent] or [later] work, including [6]."
   **What is wrong:** Absence claim names no deciding prior. The authors' own key-value Visual Voice Memory (IEEE/ACM TASLP 2021), cited in M06, is the obvious candidate and its date relative to the target is not given.
   **Fix:** Name it with its publication date and state whether it precedes, is concurrent with, or follows the target; if it precedes, the M02 novelty claim must be narrowed (e.g. "first applied to word-level lip reading").

6. **Sentence:** "The paper departs by never forcing the visual feature to resemble the audio feature: video only addresses the memory."
   **What is wrong:** No claim-table entry. The recalled value-memory output is trained to reconstruct the audio feature, so audio-feature matching is enforced on the recalled feature; the sentence overstates the departure from regression/distillation.
   **Fix:** Add the quote for the training losses and rephrase: "the visual encoder output is not pushed toward the audio feature; instead a memory read-out, addressed by video, is trained to reconstruct it."

7. **Sentence:** "On the four seen GRID speakers a 2023 comparison scores an end-to-end WGAN at ASR WER 4.07% and lists Lip2Wav at STOI 0.731 [7] [later]."
   **What is wrong:** The state of the art is taken from a baseline row of [7], not from [7]'s own system or later GRID video-to-speech work; it is not shown to be the best today.
   **Fix:** Report [7]'s own best GRID-4 result (or say it is worse than the WGAN on WER), and name the best later GRID video-to-speech result with year, metric and value.

8. **Sentence:** "Table 3 makes the vocoder the dominant factor: naturalness is 2.93 against Lip2Wav's 2.83, while WaveNet lifts it to 4.37, a 14-fold larger step (inference)."
   **What is wrong:** The claim-table quote shows only "Proposed Method 2.93 ± 0.21 3.56 ± 0.19"; the 2.83 and 4.37 values and which column is naturalness are not supported. The same holds for the Verdict's "not from the memory".
   **Fix:** Add the Lip2Wav and WaveNet rows of Table 3 with column labels to the claim table; confirm 4.37 is the memory model with WaveNet, not ground truth.

9. **Sentence:** "Over its Bi-GRU baseline the memory adds 1.27 points on LRW (84.14% to 85.41%) and 5.89 points on LRW-1000..." and "Against the authors' distillation build on the same baseline the gain is 0.91 points (84.50% to 85.41%, Table 5)..."
   **What is wrong:** The LRW-1000 baseline value is not quoted, and the Table 5 quote gives four unlabeled numbers, so it is not shown that 84.50% is the distillation build (or what 84.20% is).
   **Fix:** Quote the Table 5 header and the LRW-1000 baseline row; if 84.20% is another audio-transfer variant (e.g. feature regression), name it.

10. **Sentence:** "...WaveNet in one opinion-score row (Sec. 4.2.3)... Verdict: standard." (M06)
    **What is wrong:** By the review's own count the usual design is a neural vocoder (49) and Griffin-Lim is a minority (16), yet the paper's objective scores all use Griffin-Lim; `standard` is asserted without explaining why a minority choice is standard.
    **Fix:** Either justify `standard` (e.g. Griffin-Lim was the norm in the Lip2Wav lineage in 2021, with a count for that period) or change the verdict.

11. **Sentence:** References 2 and 7.
    **What is wrong:** The DOI of [2] could not be confirmed here; [7] is cited as an arXiv preprint although a journal version may exist.
    **Fix:** Verify the DOI of [2] against the IEEE record and cite the published version of [7] if available.

## Scores

- Procedure: 7/10. Claim table is complete and most arithmetic checks out; several load-bearing numbers (Table 3, Table 5 columns, LRW-1000 baseline) lack quotes, and state-of-the-art lines miss stronger works.
- Final text: 6/10. Positions are clear and well caveated on scorer effects and memory-size selection, but the `ahead` verdict contradicts its own caveat and the LRW-1000 leadership claim is likely wrong without a condition.
