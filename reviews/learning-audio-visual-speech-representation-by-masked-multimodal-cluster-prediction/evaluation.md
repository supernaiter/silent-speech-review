Evaluator: a language model separate from the writer

Scope: the compact review and its claim table only. No sources were opened, no searches were run. "Insufficient" means the quoted passage does not carry the claim as written.

## Findings table

| # | Claim (section) | Where checked | Verdict | Note |
|---|---|---|---|---|
| 1 | Verdict: M03 is masked prediction of audio-visual clusters "refined over five iterations"; M02 is audio training-only, video alone at test | Claim 1 | Insufficient evidence | The quotes support the video-only test (t21) and masking (t20). "Five iterations" is in no quote. |
| 2 | Verdict: 59.8% [2] vs 92.3% -> 32.5% is a "large" M03 gain | Claims 2, 8 | Correct on numbers, weak as a comparison | Both numbers are quoted. They come from different models, label budgets and unlabelled data (334 h vs 1,759 h). The Verdict states the gain before that confound, which only appears in the M03 section. |
| 3 | Verdict and M03 SOTA: 23.7% [3] vs 32.5% "with identical model size, unlabelled data and labels"; 27% relative; 433 h 21.5 vs 28.6 | Claims 3, 7 | Numbers correct; condition insufficient | The quote "USR 2.0 23.7" and the arithmetic 8.8/32.5 = 27.1% are fine. Nothing quoted shows the match in model size, unlabelled pool (LRS3 plus English VoxCeleb2) or label hours. |
| 4 | Verdict: "single runs" and "no variance reported" | Claims 3, 4, 11 | Partly supported | t49 says the results "appear to be" single runs, and the review states it as fact. Appendix C.2 reports "18.0 ± 0.5%" for seen speakers (claim 19, t10), so some variance is reported. The wording should be scoped to Table 1. |
| 5 | Verdict: 32.5% vs 33.6% [4] is a 1.1-point gap, 3.3% relative, different training regimes | Claims 4, 17 | Correct | 33.6 - 32.5 = 1.1 and 1.1/33.6 = 3.3% both check. The 31K h and "thousand times" quotes support the regime difference. |
| 6 | Verdict: both components "standard" because "later work beats it at the same budget" | Claim 3 | Judgment issue | A 2026 work (the paper is from 2022) is used as the reason a 2022 contribution is only "standard". The review labels [3] as [later] but still lets it decide the verdict. I cannot check the SKILL.md verdict rules, but a later work cannot be a prior-art basis. |
| 7 | M03 usual approach: "normally trained on transcribed video"; 6 of 141 LRS3 papers use self-supervised | Claims 5, 25, 26, 30 | Insufficient evidence | The only counts shown are text_prompt 18, paired_audio 17 and self-supervised 6 of 141. They do not show that transcribed video is the norm. The table says "slot-filled 6" while the Appendix says "31 of 75", with no explanation of the different populations. |
| 8 | M03: distillation used ASR-transcribed VoxCeleb2 (334 h); the paper's 1,759 h is larger "because of a different filter" | Claim 8 | Mismatch | t32 says "different parameters and ASR model used", not a filter. The 334 h figure is quoted. The cause is mis-stated. |
| 9 | M03: audio-feature regression moved LRS2 WER from 39.1% to 38.8% [5] | Claim 9 | Insufficient evidence | Only 38.8 is quoted. 39.1 is not. The comparison is then set against LRS3 62.3% -> 28.6%, a different dataset and condition. |
| 10 | M03: "none of the earlier studies among the 123 ... predicts iteratively refined audio-visual clusters" | Claim 10 | Insufficient evidence | The deciding priors are named only as [2] and [5]. There is no quote for the other 121, so this is not an absence claim a reader can audit. |
| 11 | M03 verdict: NMI 44.2% vs 39.7% is a proxy, not a recognition result | Claim 11 | Correct | t17 supports both values. |
| 12 | M02 usual approach: "common"; paired audio is the recorded supervision kind in "258 folders" | Claim 12 vs claim 29 | Contradiction / insufficient | 258 is also the count of unique studies mentioning LRS3 in M12. The same number appears for two different quantities, with "folders" vs "unique studies". "Common" rests on two examples [5] and [2]. |
| 13 | M02 SOTA: [3] "keeps audio as a training-time teacher" and "beats this design at every matched budget in its Table 2" | Claim 13 | Insufficient evidence | Only two table rows are quoted (23.7 and 21.5). "Every matched budget" and "teacher" are not shown. |
| 14 | M02: audio-only 1.3% vs 2.3% "sets a model without a language model against one with it" | Claim 14 | Insufficient evidence | The quote gives the 40% relative figure and the SOTA statement. The LM asymmetry is not in it. The audio-only result is also not an M02 argument. |
| 15 | M12: 258 unique studies mention LRS3; [6] cited for the benchmark | Claims 15, 29 | Insufficient evidence | The count has no source quote. [6] is the dataset paper, which cannot show a field-wide usual approach. |
| 16 | M12 SOTA: 17.6% in 2026 [3]; 33.6% in 2019 [4] | Claim 16 | Correct on numbers | Both are quoted. I know of no better LRS3 VSR value, but I cannot confirm that 17.6% is the best in 2026. |
| 17 | Outrun list: "1/1000 of the labeled data" counts only transcribed hours; the 30 h model also uses 1,759 h unlabelled | Claim 18 | Correct, partly | The 1000x quote is present. The 1,759 h figure comes from claim 8, not from this row's quotes. |
| 18 | Outrun list: Sec. C.2 gives 18.0% seen vs 30.5% unseen; no Table 1 row gives 30.5%; seen groups come from trainval, which is also in the pre-training pool | Claim 19 | Numbers correct; last clause insufficient | Quotes t10 and t67 confirm 18.0 and 30.5. That trainval is in the unlabelled pool is not quoted (t40 only says 403 h + 30 h). |
| 19 | Outrun list: the LiRA comparison uses the authors' own re-implementation (Sec. 4.2) | Claim 20 | Mismatch | The quote (t27) is "17.5% lower absolute WER" and says nothing about a re-implementation. |
| 20 | Outrun list: self-training alone exceeds 50% WER; rounds and filtering not given | Claim 21 | Correct | t30 and t56 support it. |
| 21 | Components table numbers: 96x96 ROI, 25 Hz, 32-64 V100, 4-gram LM, counts 4,015 / 6,538 / 8,898 / 8,925 / 3,760 / 120 / 82 / 239 / 6,721 | Table | No quote | None of these appears in the claim table, so they are unchecked. |
| 22 | Claim table lists "Questions for the authors" and "Appendix: literature search" (claims 23-32), but the compact review has neither section | Claim table | Inconsistency | Claims 25-32 and 23-24 cannot be checked against review text. |
| 23 | References [1]-[6]: authors, venue, year, arXiv ids | Reference list | Plausible | [1], [2], [4], [5] and [6] are consistent with what I know. [3] (arXiv:2602.19316, ICLR 2026) is after my knowledge and I cannot confirm it. [5] [concurrent] and [3] [later] look right. |

## Required fixes, by impact

1. Remove the later work [3] as the basis for the "standard" verdicts in the Verdict and in M02/M03, or state plainly that the verdict follows from the evidence available to the authors.
2. Fix claim 19 (LiRA "re-implementation"): add the exact Sec. 4.2 quote or delete the point.
3. Correct "different filter" to what t32 says (different parameters and ASR model).
4. Add quotes for "identical model size, unlabelled data and labels" in [3] Table 2, or weaken the wording. Do the same for "every matched budget" and "teacher".
5. Add the missing 39.1% quote, and flag that LRS2 and LRS3 are different datasets.
6. Resolve the duplicate 258 count (M02 paired audio vs M12 LRS3 mentions) and the "folders" vs "unique studies" wording.
7. Reconcile 6/141 (table) with 31/75 (Appendix), and either support "normally trained on transcribed video" with a count or soften it.
8. State the "single runs" caveat as Table 1 only, and acknowledge the ± 0.5 in Appendix C.2.
9. Add a quote or a locator for "five iterations", for the LM asymmetry in the audio-only comparison, and for "trainval is in the pre-training pool".
10. Name more deciding priors, or drop the "none of the 123" sentence.
11. Add claim rows for the component table numbers, or move them to the Appendix with sources.
12. Move the 59.8% vs 32.5% caveat (different data, labels, 334 h vs 1,759 h) into the Verdict next to the "large" gain claim.

## Scores

Procedure: 6/10. Claim rows exist for the main numbers, but several rows carry quotes that do not match the claim they back.
Final text: 6/10. The core comparisons are sound and the central confound is handled in the body. Several conditions and counts are unsupported, and the verdict logic leans on later work.

Findings: 15 (rows with Mismatch, Insufficient, Contradiction or Judgment issue: 1, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 18, 19, 21; plus 2 and 22 as secondary)
