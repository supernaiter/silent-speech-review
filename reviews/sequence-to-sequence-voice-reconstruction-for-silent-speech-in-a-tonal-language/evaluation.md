# Evaluation: Sequence-to-Sequence Voice Reconstruction for Silent Speech in a Tonal Language

Date: 2026-11-19. Fallback evaluator (claim table only). Input: the compact review and its claim table. No source was re-opened; items marked "background" rely on the evaluator's own knowledge of the literature and are not verified against the source in this pass.

## Claim checks

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Two components changed: duration predictor with length regulator (M06), toneme supervision discarded at inference (M02) | Claim 1; Abstract, §III-D, §IV-A | correct | Quotes support both. |
| 2 | Duration-regulated model fails without the auxiliary loss | Claim 2/10; Table VI | correct | Row (λtm=0) gives +132.75 and §IV-C.1 explanation is quoted. |
| 3 | Headline 21.99% CER, "24.63 points better" than baseline | Claim 3; §IV-B.1 | insufficient evidence | Source says "outperforms the baseline by 24.63%". Absolute vs relative is not shown; no baseline ASR CER is quoted. |
| 4 | Tone adds 6.51 CER points, single run | Claims 4, 15, 25; Table VI | insufficient evidence | +6.51 is quoted, but the review itself says Table VI may be relative (claim 23). "Points" and "single run" are unquoted. |
| 5 | Removing toneme loss raises CER to about 154.74%, over three times the baseline | Claim 10 | insufficient evidence | Holds only if +132.75 and 24.63 are absolute. If relative, the value is about 51%. Contradicts the review's own question about +81.18. |
| 6 | Toneless phonemes give about 28.50% CER | Claim 15 | insufficient evidence | Same absolute/relative dependency (about 23.4% if relative). |
| 7 | Five silent repetitions per prompt, 8:1:1 split by silent utterance | Claim 5; §II-B | correct | Both quotes present. |
| 8 | Speaker 2 test set of 64 is not a multiple of five, so split is not grouped by prompt | Claim 22; Table II | wrong (inference does not follow) | Speaker 2 total is 516+64+64 = 644, also not a multiple of five, so some prompts already have fewer than five repetitions. A prompt-grouped split can give 64. The grouping is unreported, not disproved. |
| 9 | "likely in-sentence Mandarin voicing" (Verdict) | Verdict | wrong (overstated) | Rests on item 8. Evidence supports "grouping not reported; overlap possible". |
| 10 | Baseline [3] has no auxiliary loss | Claim 20 | correct (background), no quote | The quoted passage is about the vocoder swap. Add a quote from [3] or the target. |
| 11 | [6]: removing the phoneme loss moves WER 42.2% to 51.7% | Claim 11; [6] Table 1 | correct | 51.7 quoted; 42.2 matches the full-model figure in [6] (background), but it is not in the quote. |
| 12 | [6] labelled [concurrent] | Reference 6 | correct | arXiv June 2021 vs target arXiv August 2021, inside six months; used as evidence, not as a missed citation. |
| 13 | [3] 76.5% WER without audio alignment, 68.0% with it | Claim 24; [3] Table 5 | partly supported | 76.5 quoted; 68.0 matches [3]'s headline (background) but is not quoted. |
| 14 | Table VI +81.18 vs prose "relative reduction of over 81.18%" | Claim 23; §IV-C.4 | insufficient evidence | Only the table cell is quoted; add the prose quote. |
| 15 | M06 usual approach: DTW in 28 of 76 synthesis studies | Claim 6; Appendix | correct | Consistent between text, table and Appendix. Usual approach is plausible. |
| 16 | M06 state of the art: [4] 10.52% CER from sEMG alone, keeps the length regulator, eight speakers | Claim 7; [4] Table 3 | partly supported | 10.52 quoted. "Keeps the length regulator" and "eight Mandarin speakers" have no quote. |
| 17 | English best 11.89% WER (2026), frame-synchronous [5] | Claim 8; [5] Abstract | partly supported | Value quoted; "frame-synchronous" unquoted. |
| 18 | M02 state of the art: 25.14 ± 0.90% WER over 10 seeds [7] | Claim 13; [7] Table 1 | insufficient evidence | Quote shows two numbers (12.88 ± 0.49, 25.14 ± 0.90) with no column labels; "10 seeds" unquoted. [5] reports 11.89% WER on the same English silent test set while being guided by silent speech recognition during training, so 25.14% is not clearly the best training-only-supervision result. |
| 19 | [2] multi-task ultrasound synthesis, about 7% relative gain | Claim 14; [2] Abstract | correct | Quote matches. Prior work (2018). "HMM-state targets" consistent with the paper (background). |
| 20 | M02 usual approach: auxiliary loss in 10 of 34 studies | Claim 12; Appendix | correct | Consistent with table and Appendix. |
| 21 | M12 usual approach: crowd workers in "15 of 79 listener studies" | Claim 16; table; Appendix | wrong (internal contradiction) | Table and Appendix give pattern match 37, the text says 79. |
| 22 | 10 listeners, 60 samples each | Claim 16; §IV-B.2 | correct | Quote supports. |
| 23 | Listener CER 6.41% below ASR CER of ground truth 11.30%, so MASR is weak | Claim 18 | numbers correct, conclusion overstated | Alternatives not excluded: listeners hear a small, repeated prompt set and samples were selected (sample allocation is itself an open question in the review). |
| 24 | Per-speaker listener SDs reach 41.62 points, no significance test | Claim 19; Table V | partly supported | 41.62 is the baseline's speaker-1 SD, not SSRNet's; say so. "No significance test" is an absence claim without a locator. The second quote (tone accuracy 96.07%) is unrelated. |
| 25 | M12 state of the art: 43.75% median open-transcription WER, intracortical interface [8] | Claim 17; [8] Results | correct value, weak relevance | Value matches (background). An intracortical attempted-speech system is not a like-for-like state of the art for listener tests of silent-EMG voicing; the review flags "a harder task" but should justify the choice or give an EMG-domain listener result. |

Step 4 (central claim): the strongest confound, a baseline without the auxiliary phonetic loss, is named and supported by [6]. The vocoder difference is controlled by the authors (PWG in both). The absolute-vs-relative ambiguity in Table VI is the next largest confound and is not handled consistently (items 3 to 6).

Step 6 (absence/novelty): "3 of 76 studies mention a duration predictor or length regulator" names the three studies; no "first/only" claim is made. No earlier silent-EMG work with an explicit duration predictor and length regulator is known to the evaluator.

Step 7 (verdicts): no `ahead` verdict. M11 is marked "not reported" while the review reports the 8:1:1 utterance split; the label should say what is not reported (prompt grouping).

## Required fixes (ordered by impact)

1. Resolve absolute vs relative in Table VI and the headline. The review flags +81.18 as ambiguous but then treats +132.75, +6.51 and 24.63 as absolute points to derive 154.74%, "over three times the baseline" and 28.50%. Quote the baseline ASR CER from the results table; if the unit cannot be settled, drop the derived values and say "points" only where established.
2. Withdraw the split inference from speaker 2's 64 test utterances (644 total is also not a multiple of five) and soften the Verdict from "likely in-sentence" to "prompt grouping not reported; test prompts may occur in training". Align the M11 verdict label with this.
3. Fix the M12 count contradiction: "15 of 79 listener studies" vs pattern match 37 in the table and Appendix.
4. M02 state of the art: explain why [5] (11.89% WER with recognition guidance) does not count as training-only supervision, or replace [7]; quote the column header showing 25.14 is WER and the source of "10 seeds".
5. Hedge "the MASR scorer is weak" or name the alternatives (repeated prompt set, sample selection).
6. Add missing quotes: [3] lacks an auxiliary loss; 68.0% WER in [3]; 42.2% in [6]; the §IV-C.4 prose "relative reduction of over 81.18%"; [4] length regulator and eight speakers; [5] frame-synchronous; absence of significance testing.
7. State that the 41.62-point SD is the baseline's, and replace the unrelated tone-accuracy quote in claim 19.
8. Justify [8] as the M12 state of the art for silent-EMG listener evaluation or add an EMG-domain comparator.
9. State that section and table locators refer to arXiv v3, since the cited Brain Sciences version numbers sections differently, and add pages 175–181 to [6].

## Scores

Procedure: 7/10. Final text: 6/10.

The confound on the auxiliary loss is well found and supported by a concurrent ablation, and the counts are mostly consistent.
