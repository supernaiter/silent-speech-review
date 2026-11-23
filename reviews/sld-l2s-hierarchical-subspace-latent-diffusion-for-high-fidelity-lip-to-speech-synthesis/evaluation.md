# Evaluation: SLD-L2S review

Date: 2026-11-23. Fallback evaluator (claim table only). Input: compact review with its claim table; sources were not reopened. "No quote" means the claim-table quote does not contain the stated value, not that the value is wrong.

## Claim check

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | SLD-L2S maps lips to continuous codec latents with a DiCB backbone (M06) | Claim row 1 (t1, t2) | correct | Quotes support it. |
| 2 | Continuous codec latents in 1 of 165 studies; priors [2], [3] generate discrete tokens | Row 2 (c10, c12, t75) | insufficient evidence | Quote for ImaginTalk [3] says "masked speech features are obtained via the codec encoder and forward diffusion process". That describes diffusion over codec-encoder features and does not show discrete tokens. If they are continuous, the "discrete" contrast and the n=1 count are wrong. |
| 3 | UTMOS 4.2096 vs ground truth 3.5721 (Table 1); noise in LRS3 audio explains the gap [4], [5] | Row 3 (t38, t32, c13, c3) | correct | Values are in the quotes. Column headers are not quoted, so the assignment to UTMOS is assumed. |
| 4 | Faces-to-Voices UTMOS 4.031 at 10 steps, video speaker embedding; cited by target but missing from Table 1 | Row 4 (c1, c14, t74) | partly correct | 4.031 and 10 are in c1, but the dataset (LRS3 vs LRS2) and the column are not quoted. t74 is about V2SFlow, so it does not show that the target cites Faces-to-Voices. |
| 5 | WER 30.22 vs V2SFlow 27.55 and LipVoicer 20.62 | Row 5 (t38, t37, t35) | no quote for 27.55 and 20.62 | t37 (3.6939) and t35 (2.4540) are other cells. 30.22 matches. |
| 6 | Second-best SECS depends on a reference embedding that three of five baselines lack | Row 5 (t71) | insufficient evidence | The caption says that "∗" marks reference embeddings. Which rows are starred, and the count "three of five", are not quoted. |
| 7 | M06 usual approach counts (54 / 22 / 19; 8 codec) | Row 6 | correct | Matches the ledger tally. |
| 8 | 4.2096 − 4.031 ≈ 0.18 | Row 8 | correct | 0.1786. |
| 9 | HiCoDiT [concurrent] 29.41% WER from video alone at 64 steps | Row 9 (c8, c9) | partly correct | 29.41 and 64 steps are in the quotes. The column, the dataset and "video alone" are not. The [concurrent] label is right because arXiv 2604 comes about 2 months after 2602. |
| 10 | DiCB 57.7M vs DiT 57.8M; SECS 0.804→0.618, WER 30.70; velocity UTMOS 3.9540, WER 29.70 | Row 11 (t47, t48, t46) | partly correct | The parameter counts and 3.9540 are quoted. There is no quote for 0.618, 30.70 or 29.70, or for "single runs". |
| 11 | M12 counts (83 / 38 / 51 / 21 / 40) | Row 12 | correct | Matches the tally. |
| 12 | 15 listeners, 30 clips; unseen-speaker status not stated | Row 13 (t31, t58) | partly correct | 15 and 30 are quoted. The absence claim gives no section where it was checked, and t58 is unrelated. |
| 13 | V2SFlow 28.5% WER for both variants, SECS 0.851 vs 0.664 | Row 14 (c5–c7) | correct | The review says "(2024)" in the text and table but gives 2025 in reference 4. The years are inconsistent. |
| 14 | DiffV2S, LipVoicer, NaturalL2S SECS 0.627, 0.588, 0.628 | Row 15 (t34–t36) | no quote | The quoted cells (3.0681, 2.4540, 3.6598) are not these values. |
| 15 | Listeners rate output 4.17 vs ground truth 4.36 | Row 16 (t64, t39) | partly correct | 4.17 is quoted. 4.36 is not, and t44 (3.88) is another cell. |
| 16 | Listener intelligibility 3.65 and similarity 3.77 vs V2SFlow 3.69 and 3.90 | Row 17 | no quote | None of the four values is in the quotes. |
| 17 | Efficiency claim omits Faces-to-Voices (10 steps); NaturalL2S and Intelligible use 1 NFE | Row 18 (t73, t18, c1, c4) | partly correct | The omission of Faces-to-Voices is supported. "1 NFE" is not quoted. If those two systems are not diffusion-based, they do not contradict the authors' claim about "other diffusion-based methods". |
| 18 | Table 3 prints "w/o Lsem" twice | Row 19 (t72, t49, t51) | insufficient evidence | Only one "w/o Lsem" label is quoted. |
| 19 | Without SLM loss, UTMOS is 4.2885 and WER 29.99, while D-BERT and SECS drop | Row 20 (t50, t25) | partly correct | The direction for D-BERT is quoted, but the numbers are not. The claim is correctly attributed to the authors. |
| 20 | M13 "not reported", step count only | Row 22 (t67) | partly correct | Training hardware is reported (one H100, about five days). Only inference runtime is missing. |
| 21 | M07 slot = reference-audio speaker embedding | Component table | wrong slot | M07 is "Lexicon and LM". A speaker embedding is conditioning, not a lexicon or language model. |
| 22 | M12 verdict | Section text vs component table | contradiction | The text says "standard in protocol, not in the conclusions drawn" and the table says "standard". |

## Central claim and confounds

The review handles the main confound: reference-free predictors that score output above the recordings, together with unequal speaker conditioning. It misses two others:
- **Fixed pretrained decoder.** The pretrained X-Codec decoder may raise UTMOS whatever the generator does, because the output is always decoded by a clean-speech codec. This belongs in the Verdict next to "no ablation trains DiCB on mel".
- **Re-scored baselines.** V2SFlow's WER is 27.55 in the target's Table 1 but 28.5 in its own paper. The baselines were therefore re-scored, probably with a different ASR, and the review should say so before it compares WER across papers.

Fairness: HiCoDiT is correctly labeled concurrent and is not used as a missed prior. The SLM-loss trade-off is credited to the authors.

On the novelty context: continuous codec latents with diffusion have a known precedent in TTS, NaturalSpeech 2 (Shen et al., 2023, arXiv:2304.09116). The review does not claim "first", but naming this precedent would show that only the task is new, not the design.

## Required fixes (ordered by impact)

1. **Replace the wrong or missing quotes in the claim table.** Rows 5, 11, 15, 16, 17 and 20 need quotes for 27.55, 20.62, 0.618, 30.70, 29.70, 0.627/0.588/0.628, 4.36, 3.65/3.77/3.69/3.90, 4.2885/29.99 and "1 NFE". The cells cited now (t34–t37, t44) hold other values.
2. **Re-check how [3] ImaginTalk is described.** The quote describes diffusion over codec-encoder features. If those features are continuous, revise "discrete codec features", the n=1 count and the Verdict sentence.
3. **Quote the context for the Faces-to-Voices and HiCoDiT numbers.** For Faces-to-Voices 4.031 / 30.45 and HiCoDiT 29.41, quote the dataset (LRS3) and the column header. For HiCoDiT, also quote the "video alone" condition.
4. **Support "cited but missing from Table 1".** Quote the target's citation of Faces-to-Voices; t74 is about V2SFlow.
5. **Fix the M07 slot.** Move the reference-audio speaker embedding out of "Lexicon and LM", or relabel the slot.
6. **Make the M12 verdict consistent.** Use one allowed verdict value in both the section and the table.
7. **Add the two missing confounds to the Verdict.** Name the X-Codec decoder as a possible cause of the UTMOS gain. Also say that V2SFlow's WER differs between the target's table (27.55) and its own paper (28.5), so cross-paper WER uses different ASR setups.
8. **Rephrase the efficiency bullet.** NaturalL2S and Intelligible do not contradict a claim about diffusion-based methods unless they are diffusion-based themselves. Keep the Faces-to-Voices point.
9. **Quote both Table 3 rows** that carry the "w/o Lsem" label.
10. **Locate the absence claims.** Give the section checked for "does not say whether test speakers are unseen" and for "does not comment" on output exceeding ground truth.
11. **Use one year for V2SFlow** in the text, the component table and reference 4.
12. **Revise M13.** Training hardware is reported (H100, about five days), so change "Step count only" to say that inference runtime is missing.

## Scores

- Procedure: 6/10
- Final text: 6/10

The review takes a clear position, attributes the authors' own findings fairly, and labels HiCoDiT correctly as concurrent. Its weakness is traceability: many numbers have no supporting quote.
