# Independent evaluation: A Silent Speech Decoding System from EEG and EMG with Heterogenous Electrode Configurations

Date: 2026-11-21. Fallback evaluation, claim table only: the review's Verdict, component sections and claim table were checked against the quotes and locations given. No source was re-opened. Points from general knowledge of the literature are marked (knowledge, not re-checked).

## Claim checks

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | The paper changes the input layer for EEG/EMG from five electrode configurations | Claim rows 1, 11 (t1, t2, t14) | correct | "novel on-the-fly kernel" (Sec. 1) and "configurations (220 hours)" support it. |
| 2 | The coordinate kernel loses to a fixed per-subject layer (Sec. 4.1) | Row 2 (t70) | insufficient evidence | t70 is cut before it names the tokenizer: "achieved the highest mean accuracy when trained on the". The quote does not show which tokenizer won. |
| 3 | 70.1% to 95.3% (eight healthy); 13.2% to 54.5% (patient) | Row 3 (t22–t25) | correct on the numbers | The quotes do not name the pretraining set that gives 95.3/54.5 ("dataset, reaching…"). Name it ("word all" or "all"). |
| 4 | Pretraining contains every subject's word-task sessions, the patient's included | Rows 3, 17 (t69) | correct | Supported by "all data of word utterance tasks from all subjects" (Sec. 3.2). The Verdict does not say whether the patient's and healthy participants' test sessions (17–20) are in "all". The claim table shows this is still an open question (row 25). If they are, the problem is leakage, not only a lack of transfer, and it belongs in the Verdict. |
| 5 | "pretrained on large-scale data from healthy participants" (Sec. 5) | Row 14 (t72) | wrong (quote mismatch) | The quoted phrase is not in t72 ("healthy participants achieved a substantial improvement in"). A direct quotation must match the source quote. |
| 6 | Patient calibration adds new-day sessions to the 16 used in pretraining (Sec. 3.3) | Row 14 (t73) | insufficient evidence | No quote gives "16" or "new-day". |
| 7 | Other patients untested (Sec. 5); one patient (Sec. 2.1) | Rows 4, 17 (t44, t4) | correct | |
| 8 | M06 usual approach: 98 decoders, spatial attention 25, per-subject/per-dataset 12 | Rows 5, 28, 29 | correct (ledger tally) | Consistent with the Appendix rows. |
| 9 | Défossez et al. remap onto 270 channels and add a per-subject layer [2] | Row 5 (c1) | correct | 270 is quoted. The subject layer is not quoted, but it is well established for [2] (knowledge, not re-checked). |
| 10 | Chen et al. (2024): MNI coordinates, any layout, 15 participants, PCC 0.765 on left-out participants [3] | Row 7 (c4, c5, c13) | correct, with a caveat | The numbers match. "Trained on 15 participants' grids" goes beyond c13, which says "data from 15 participants" without saying grids. |
| 11 | Défossez et al. lost 2.5 top-10 points without spatial attention and 14.4 without the subject layer (Table 3) | Row 8 (c3) | partly insufficient | 2.5 appears in c3. No quote shows the 14.4 subject-layer row. "The paper finds the same ordering" is loose: [2] removes components one at a time, while the target compares alternative tokenizers. |
| 12 | English transfer: kernel 55.8% PER vs 49.5% and 50.0%; GAP 100% (Table 2) | Rows 9, 20 (t36–t39) | insufficient evidence | The quoted row "61.5 100 49.5 50.0 55.8" has no column header in the claim table. The mapping to tokenizers, and what 61.5 is, cannot be verified. "Best on neither task" depends on this mapping. |
| 13 | M03 usual approach: per-subject model, 90 of 379 | Rows 10, 32, 33; component table | wrong (internal inconsistency) | The text and row 33 say 379. Row 32 and the component table say "pattern match 370". |
| 14 | 220 hours from five configurations with per-subject layers | Row 11 (t14) | correct | |
| 15 | [4]: LOSO over 27 participants, 20.5% CER after 3 min vs 49.3% without | Row 12 (c8, c9, c11) | correct except the 27 | No quote gives 27 participants. |
| 16 | [5]: cross-subject perceived speech 61.3% top-10; keeps test subject out | Row 12 (c12) | insufficient evidence | c12 ("of 61.3%, 43.0%, and 39.9%, respectively") shows neither the metric (top-10), the condition nor the held-out design. |
| 17 | Gains 25.2 points (36% relative), 4.1-fold | Row 13 | correct | 95.3 − 70.1 = 25.2; 25.2/70.1 = 35.9%; 54.5/13.2 = 4.13. |
| 18 | Pretraining sets change device and task (Table 1), so Fig. 2 is not a pure volume effect | Row 15 (t8, t11, t12) | correct | g.Pangolin 128 ch vs eego 63 ch, and open vocabulary vs 64 words, are quoted. |
| 19 | [4] found no benefit from a subject-specific adapter; here it wins, without seeds | Row 16 (c10, t47) | partly correct | c10 supports the [4] half. "Here it wins" rests on the truncated t70. "Without seeds" is an absence claim, and the AdamW quote does not support it. |
| 20 | The group earlier removed the EMG-predicted part of EEG [6]; no single-modality model here | Row 18 (c6) | correct | c6 (adaptive filter for EMG contamination) supports it. The absence claim is not contradicted. |
| 21 | Cross-language claim rests on one English speaker "without split or uncertainty" (Sec. 3.4) | Row 20 (t33, t52) | partly insufficient | One speaker fits a 19-hour, 8-channel single-speaker EMG corpus. That corpus has a published fixed split (knowledge, not re-checked), and no quote supports "without split". Also note that this test is EMG-only, so it says nothing about EEG. |
| 22 | "eego all" 76.9 h vs Table 1 rows summing to 78.9 | Row 21 (t15) | insufficient evidence | The arithmetic (16.1 + 13.6 + 49.2 = 78.9) is correct, but no quote shows the 49.2-hour row. The only 49.x row quoted (t8) is the g.Pangolin VS set at 49.1 h, which is not an eego row. Quote the row or drop the claim. |
| 23 | Component table: M05 "not reported", M13 "not reported" | Component table | wrong (internal inconsistency) | The same rows give the paper's sensors (63-ch EEG plus 5 bipolar EMG) and its timing (57 ms per 3.3 s sample). The verdict label contradicts the cell. |
| 24 | M06 state of the art is Chen et al. [3] | Component section | questionable | [3] is invasive ECoG/sEEG spectrogram regression (PCC), which is not comparable with non-invasive EEG/EMG word classification. Non-invasive EEG models that work across montages are closer (see fix 5). |
| 25 | Chronology labels [4], [5] as [later] | References | correct | Both are 2026 preprints labelled [later]. They are used as state of the art, not as prior work the authors missed. |

## Central claim and confounds

The strongest confound is that the pretraining set "word all" contains the same task and the same subjects, the patient included. The review handles this well. The open point is whether the test sessions are also inside "all". If they are, this is leakage and should lead the Verdict, not appear only as a question. The baseline is weak: per-subject data only, ±17.1 across subjects. The review gives both absolute and relative change. The changes in device and task across pretraining sets are handled.

## Absence and novelty claims

"Coordinate-conditioned mapping exists [2], [3]" names deciding prior work. Earlier non-invasive EEG work with the same design is closer than [3] (knowledge, not re-checked): Yi et al., "Learning Topology-Agnostic EEG Representations with Geometry-Aware Modeling", NeurIPS 2023, which uses electrode coordinates to unify montages; Yang et al., BIOT, NeurIPS 2023 (heterogeneous channel sets); Jiang et al., LaBraM, ICLR 2024 (cross-montage EEG with spatial embeddings). All appeared more than six months before the target, so citing them as prior work is fair.

## Verdicts

Every slot verdict is `standard`, `not reported` or `not applicable`, and none is `ahead`. The two `not reported` labels for M05 and M13 conflict with the cell contents (row 23).

## Required fixes (ordered by impact)

1. Replace or verify the quotation "pretrained on large-scale data from healthy participants" (Sec. 5). The claim-table quote does not contain it.
2. Settle whether the test sessions 17–20 (healthy and patient) are in "all" or "word all". If they are, state the leakage in the Verdict. Add a quote for "16 sessions" and for "new-day" calibration (Sec. 3.3).
3. Quote the Table 2 header, so that the kernel = 55.8, GAP = 100 and 49.5/50.0 mapping can be checked and 61.5 is identified. Quote Sec. 4.1 in full where it names the best tokenizer. Both "loses to a fixed per-subject layer" and "best on neither task" depend on these quotes.
4. Fix the 370 vs 379 inconsistency for M03 (text and Appendix row 33 against Appendix row 32 and the component table).
5. For M06, add the earlier non-invasive coordinate- or montage-agnostic EEG models (Yi et al., NeurIPS 2023; BIOT, NeurIPS 2023; LaBraM, ICLR 2024) as deciding priors. Either justify why invasive [3] is the state of the art for this task or replace it, and state the modality and task mismatch.
6. Quote the 49.2-hour eego row behind the 78.9 vs 76.9 inconsistency, or drop the claim.
7. Add the [2] Table 3 subject-layer row for 14.4. Soften "the paper finds the same ordering", because [2] runs one-at-a-time ablations and the target compares tokenizers.
8. Add quotes for [4] "27 participants" and for the metric, condition and held-out design behind [5] 61.3% top-10.
9. Correct the M05 and M13 verdict labels, which say "not reported" although the cells give the paper's sensors and timing.
10. Support "without split" for the English EMG corpus or remove it. Add that the cross-language test is EMG-only and so says nothing about EEG.
11. Change "trained on 15 participants' grids" to what c13 supports ("data from 15 participants"), unless a quote shows grids only.
12. Back "without seeds" with a quote showing that no seed or run count is reported, or phrase it as "no seed count is reported".

## Scores

- Procedure: 6/10. The claim table is thorough, but several load-bearing quotes are truncated (t70, Table 2 header), one direct quotation does not match its quote, and two ledger counts disagree.
- Final text: 7/10. The position is clear and the main confound (the patient in pretraining) is correctly identified. The state-of-the-art choice for M06 and a few unquoted numbers weaken it.
