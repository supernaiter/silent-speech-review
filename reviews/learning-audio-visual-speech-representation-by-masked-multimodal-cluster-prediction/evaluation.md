# Evaluation: Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction (review)

Date: 2026-11-17. Independent evaluator, a language model separate from the writer, single pass. Input: the compact review and its claim table. External facts come from the evaluator's own knowledge and are marked as inference.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper changes M03 (masked AV cluster prediction) and M02 (audio training-only, video at test) | Claim row 1; t20, t21 | correct | Quotes support it. |
| 2 | Scratch baseline 92.3% to 32.5% at 30 h | Row 2; t6 | correct | Number and condition match. |
| 3 | 59.8% for cross-modal distillation [2], "334 h against 1,759 h" | Rows 2, 9; p3, t68 | insufficient evidence | 59.8% is quoted, but its label budget, model size and decoder are not given; the confound is wider than unlabelled hours. |
| 4 | 1,759 h unlabelled (LRS3 433 h + VoxCeleb2-en) | Row 9; t40 | correct | |
| 5 | No repeated runs in Table 1 | Rows 3, 11; t49 | correct | t49 is a notes entry, not a quote, but the paper reports single numbers. |
| 6 | Headline "1/1000 of the labels" overreaches: 32.5 vs 33.6 | Rows 5, 17; t1, t2 | correct but incomplete | The paper's abstract also reports 26.9% at 433 h with self-training; the review never mentions it. |
| 7 | 1.1 points = 3.3% relative; 8.8/32.5 = 27% relative | Rows 8, 17 | correct | Arithmetic checks. |
| 8 | [3] 23.7% at 30 h, 21.5% at 433 h, same model size and unlabelled data | Rows 4, 8; s2, s3, s6 | correct as quoted | 21.5 is set against 28.6, not against the paper's own pseudo-label result (26.9). |
| 9 | M03 usual approach: 6 of 141 LRS3 papers self-supervised; text labels 18 and paired audio 17 dominate | Rows 6, 27, 31 | wrong / contradictory | Row 27 gives the usual design as self_supervised (31 of 75); row 31 calls the 18 "text_prompt", not text labels; 18 + 17 + 6 = 41 of 141, so "dominate" is unsupported. Table count 6 belongs to the minority design. |
| 10 | M02: paired audio in 258 "folders" | Row 12 | wrong / contradictory | M03 section gives paired audio 17 of 141 LRS3 papers; 258 is also the M12 LRS3 pattern-match count. "Folders" is internal jargon. |
| 11 | Earlier routes: distillation [2] and audio-feature regression [5] [concurrent] | Row 7 | contradiction | A work tagged concurrent is called "earlier". |
| 12 | LiRA LRS2 39.1 to 38.8 | Row 10; p4, p2 | correct | |
| 13 | NMI 44.2 vs 39.7 (Table E.1) | Row 11; t17 | correct as noted | Notes entry, not a quote. |
| 14 | [3] lower in "every matched size and data group" of its Table 2 | Row 13; s2, s3, s7 | insufficient evidence | Three [3] values quoted; the group of 26.4 and the matched values from this paper are not given. |
| 15 | Audio-only 1.3% (no LM) vs 2.3% (with LM) | Row 14; t11, t71, t72 | correct | |
| 16 | M12 state of the art 17.6% in 2026 [3] | Row 16; s1 | wrong as stated | Not the best LRS3 VSR result: Chang et al., "Conformers are all you need for visual speech recognition" (LP Conformer; arXiv 2023, ICASSP 2024) report 12.8% WER on LRS3 with about 100k h of transcribed YouTube video (inference, evaluator knowledge). 17.6% lacks its data condition. |
| 17 | Makino et al. 33.6% from 31,000 h | Row 16; t2 | correct | |
| 18 | Sec. C.2: 18.0% seen vs 30.5% unseen; no Table 1 row gives 30.5% | Row 19; t67, t10 | correct | Fair question. |
| 19 | LiRA comparison is a re-implementation | Row 20; t69 | correct | It is the authors' own disclosure; should be presented as such. |
| 20 | S2S "LM-free" but carries in-domain text knowledge (B.4) | none | no quote | No claim-table row; judgement weak (fix 9). |
| 21 | Self-training alone > 50% WER | Row 21; t30 | correct | The "not given" part rests on a notes entry (t56). |
| 22 | M05 96x96 ROI; M07 4-gram LM (CTC); M13 32-64 V100 GPUs | none | no quote | Component-table cells without claim rows. |
| 23 | Claim rows 23-33 cite "Questions for the authors" and "Appendix" | Rows 23-33 | insufficient evidence | Those sections are absent from the review text, yet the body cites "(slot-filled, Appendix)". |

Central confound: the 92.3% to 32.5% (and 62.3% to 28.6%) gain is measured against the paper's own from-scratch baseline, which is much weaker than published supervised LRS3 systems of the time (e.g. Ma et al., ICASSP 2021, conformer, 43.3% LRS3 VSR; inference, evaluator knowledge). The review says "on the paper's own terms" but does not quantify it. Second confound: [3] is a pseudo-labelling method compared with this paper's result without self-training.

Fairness: [3] is correctly tagged later and not treated as a missed citation. LiRA is tagged concurrent but called "earlier"; the authors did compare with it.

Verdicts: all slots are `standard` or `not applicable`; no `ahead` verdict to audit.

## Required fixes (ordered by impact)

1. **Sentence:** "Later work now beats the design at the same budget: 23.7% against 32.5% with the same model size, unlabelled data and 30 h of labels [3] [later]." and "at 433 h it is 21.5% against 28.6%." (M03 State of the art), together with the Verdict's headline-overreach sentence.
   **What is wrong:** The review never mentions the paper's own best result, 26.9% WER at 433 h with pre-training plus self-training (Abstract). [3] is a pseudo-labelling method, so its 433 h number should be set against 26.9%, not 28.6%. Omitting 26.9% also makes the "1.1-point gap" critique look more decisive than it is: at 433 h the paper beats the 31K-hour system by 6.7 points.
   **Fix:** Add "with self-training the paper reaches 26.9% at 433 h (Abstract; Table 1)", compare [3]'s 21.5% with 26.9% (or give both), and in the Verdict restrict the overreach claim to the 30 h headline while noting the 433 h self-training result.

2. **Sentence:** "**State of the art:** 17.6% in 2026 [3] [later]; 33.6% in 2019 from 31,000 h of transcribed video [4]." (M12) and the table cell "[3] 17.6%".
   **What is wrong:** 17.6% is not the best LRS3 visual-only WER. Chang et al., "Conformers are all you need for visual speech recognition" (arXiv 2023, ICASSP 2024) report 12.8% on LRS3 with large-scale transcribed YouTube data. 17.6% is given without its training-data condition.
   **Fix:** State 17.6% with its data and label condition from [3], and either name 12.8% (LP Conformer, large non-public transcribed data) as the overall best or restrict the claim explicitly to "with public data only".

3. **Sentence:** "Of the 141 LRS3 papers with a recorded training slot, 6 use self-supervised pre-training; text labels (18) and paired audio (17) dominate (slot-filled, Appendix)." and the table cell "Transcribed-video training; self-supervised in 6 of 141 LRS3 papers (slot-filled 6)".
   **What is wrong:** The Appendix rows contradict it: row 27 gives the usual M03 design as self_supervised in 31 of 75 studies, and row 31 labels the 18 "text_prompt", not text labels. 18 + 17 + 6 covers only 41 of 141, so "dominate" is unsupported. The table count (6) is the count of the minority design, not of the stated usual approach.
   **Fix:** Use one population and one label consistently, e.g. "Of 141 LRS3 papers with M03 recorded, 18 are tagged text_prompt, 17 paired_audio and 6 self-supervised; the remaining 100 are ...". Reconcile with the 31-of-75 figure or name the different population. Put the usual-approach count, not 6, in the table.

4. **Sentence:** "paired audio is the recorded supervision kind in 258 folders (slot-filled, M03 field; M02 is sparse)" (M02 Usual approach) and table cell "(slot-filled 258)".
   **What is wrong:** Contradicts the M03 section (paired audio 17 of 141 LRS3 papers). 258 is also exactly the M12 LRS3 pattern-match count, suggesting a copied number. "Folders" is internal jargon.
   **Fix:** Re-check the paired_audio tally; state the population and use "studies", e.g. "paired audio is recorded as supervision in N of M studies (slot-filled, M03 field)".

5. **Sentence:** "The M03 gain is large on the paper's own terms: its scratch baseline falls from 92.3% to 32.5% WER at 30 h of labels" (Verdict).
   **What is wrong:** The strongest confound is baseline strength. The from-scratch baselines (92.3% at 30 h, 62.3% at 433 h) are far weaker than published supervised LRS3 systems of the time (e.g. Ma et al., ICASSP 2021, conformer, 43.3%), so the gain over the own baseline overstates the gain over a tuned supervised system. The review hints at this but does not quantify it.
   **Fix:** Add: "the 433 h scratch baseline (62.3%) is far weaker than the published supervised result of 43.3% [Ma et al. 2021], so the 33.7-point gain overstates the gain over a tuned supervised system." Add the reference.

6. **Sentence:** "it is far below the 59.8% of cross-modal distillation [2], although that margin also mixes 334 h against 1,759 h of unlabelled video." (Verdict; repeated in the M03 body).
   **What is wrong:** Only unlabelled hours are named. The comparison also mixes labelled budget, model size (325M LARGE vs a smaller CTC model in [2]) and decoder; none is stated with the 59.8%.
   **Fix:** Give [2]'s labelled data, model and decoder from its Table 3, e.g. "... mixes unlabelled data (334 h vs 1,759 h), labelled data, model size and decoder."

7. **Sentence:** "its visual-only WER is lower than this paper's in every matched size and data group of its Table 2 [3] [later]." (M02 State of the art).
   **What is wrong:** The claim table quotes three [3] values (23.7, 21.5, 26.4), does not identify the group of 26.4, and gives no matched values from this paper beyond 32.5 / 28.6; "every" is not shown.
   **Fix:** List each group with both numbers (e.g. "Large 30 h: 23.7 vs 32.5; Large 433 h: 21.5 vs 28.6, or 26.9 with self-training; Base ...: 26.4 vs X"), or narrow the claim to the groups quoted.

8. **Sentence:** "The earlier unlabelled-video routes were distillation from an audio recogniser [2] and regression of audio features [5] [concurrent]." and "The LiRA comparison uses the authors' re-implementation of its objective (Table 1 note), not the published system [5]."
   **What is wrong:** A work tagged concurrent is called earlier. The re-implementation point is the authors' own disclosure, presented as a finding of the review.
   **Fix:** "The prior route was distillation from an audio recogniser [2]; regression of audio features [5] is concurrent." and "As the authors state (Table 1 note), their LiRA row re-implements the objective, not the published system [5]."

9. **Sentence:** "The S2S decoder is called LM-free but is trained on LRS3 transcripts, so it carries in-domain text knowledge (Appendix B.4)."
   **What is wrong:** No claim-table row supports it, and the point applies to every supervised attention decoder (it learns from its own fine-tuning transcripts); it does not show an overclaim. It also sits uneasily with the review's own use of the no-LM contrast in M02 (1.3% vs 2.3%).
   **Fix:** Drop the bullet, or reframe with a quote: "The S2S result uses no external LM (B.4: 'No language model is used for S2S decoding'); like any attention decoder, it still learns text statistics from the LRS3 fine-tuning transcripts."

10. **Sentence:** Component-table cells "Mouth ROI 96x96, 25 Hz; filterbank audio" (M05), "4-gram LM (CTC); none (S2S)" (M07), "32-64 V100 GPUs" (M13), and every "(slot-filled, Appendix)" / "(pattern match, Appendix)" pointer.
    **What is wrong:** These cells have no claim-table rows, and the Appendix and "Questions for the authors" sections that claim rows 23-33 cite are not in the review text, so the counts cannot be checked.
    **Fix:** Add claim rows with location and quote for the M05, M07 and M13 cells, and include the Appendix (ledger counts, usual-design tallies, read-in-full list) in the published review, or remove the "Appendix" pointers.

## Scores

- Procedure: 6/10. Target numbers and arithmetic are well sourced; ledger counts are internally inconsistent, several table cells lack evidence rows, and the M12 state of the art misses a better result.
- Final text: 5/10. Clear position and good awareness of the unlabelled-data confound, but omitting the paper's 26.9% result skews both the headline critique and the later-work comparison.
