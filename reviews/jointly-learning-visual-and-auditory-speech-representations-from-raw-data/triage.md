# Triage of the independent evaluation

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | [2] Sec. 4 and App. B.4: a fine-tuned HuBERT pseudo-labels the same unlabelled data, "no additional data is used"; target Table 1: 32.5 to 28.6 (AV-HuBERT) and 32.5 to 24.8 (RAVEn); Sec. 3.2 describes one pass. | Verdict; M02 section rewritten around the matched route (7.7 against 3.9 points, 3.8 ahead); "round count" replaced by pseudo-label decoding; "no extra data" now credited to [2] as the deciding prior; question revised. |
| 2 | applied in part | Target Sec. 2 cites BYOL/DINO and data2vec and states its differences (verified). Rejected part: Pan et al. 2022 (arXiv 2203.07996) re-uses an ImageNet MoCo v2 checkpoint as a visual front end (its Sec. 3); it trains no momentum-teacher objective and falls under the rule's checkpoint-reuse exclusion. data2vec and BYOL are not in the wiki, so they are named through the target's Sec. 2. Recall sample deduplicated: 9 unique studies besides the target. | M03 section: novelty scoped to cross-modal asymmetric use; authors' Sec. 2 differentiation credited; Appendix M03. |
| 3 | applied | Recount with arXiv months: prior before 2022-06, [concurrent] 2022-06 to 2023-06. | All three Usual approach lines, table cells, Appendix; audits (counts_<slug>.screened_v2). |
| 4 | applied | Full text and titles screened against the inclusion rules: separation, enhancement, deepfake, sync, VAD, KWS, surveys, pre-2015 and checkpoint-reuse papers removed. M03: 7 prior + 3 concurrent; M12: 20 prior systems. | Usual approach lines, Appendix, audits. |
| 5 | applied | 2007.06504 self-distils lip readers; FastLR (2008.02516) states it uses no distillation; SimulLR mentions it only in related work; 2108.03543 does distil from audio (its abstract). Screened design count: 5 of 9 prior distil from an audio or speech model. | M02 Usual approach, table cell, audit usual_approach_<slug>. |
| 6 | applied | LP-Conformer Table 2: 12.8% with ~100k h (arXiv 2023-02, [concurrent]); USR 2.0 Huge 17.6% public data. | M12 State of the art, table cell. |
| 7 | applied | [3] Table 2: BRAVEn 30.8 (Large, 30 h, separate models, 2024); AV-data2vec 30.8. USR 2.0 moved to M02. | M03 State of the art, table cell, audit. |
| 8 | applied | Table 1 (PDF LM column): RAVEn 24.8 without LM < 25.9; Serdyuk 2022 at 19.3 in the same table. | M12 paragraph and Verdict reframed: table honest, abstract and Sec. 4.2 overstate. |
| 9 | applied | M02 audit: published seed set recall 1.0; this review's seeds 0.5 (LiRA missed). | Appendix M02 gives both. |
| 10 | applied | Table 3: cross-modal only 40.8 vs 32.9. | M03 section. |
| 11 | applied | [2] Sec. 4: S2S models use no external LM; RAVEn hybrid CTC/attention (Sec. 3.2). | M03 section. |
| 12 | applied | Base-to-Large gain is also 7.7 (Sec. 4.2); paper gives no run count. | "Largest gain" sentence removed; "one run" replaced by "no repeat runs". |
| 13 | applied | Sec. 1: "by a large margin in most settings". | First claims-outrun bullet. |
| 14 | applied | App. A.1: LRS3 test speakers separate from training speakers; VoxCeleb2 overlap not discussed. | Overlap bullet and M11 next step removed; question narrowed to VoxCeleb2 speakers; M11 table note. |
| 15 | applied | [2] full text has no LRS2 result. | M12 paragraph: no LRS2 comparison with the closest prior. |
| 16 | applied | Method restatements and "(sparse slot)" removed. | M03/M02 sections; M07 cell. |
| 17 | applied | Values match [2]; decoder difference stated as a fact. | Question removed. |
| 18 | applied | Mention count replaced by screened design count (3 of 7). | M03 table cell. |
| 19 | applied | [3] Table 2 lists RAVEn Large/433 h at 28.2. | Claims-outrun bullet (0.4 points, inference). |
| 20 | rejected | Neither first page states a venue; bibliographic data are taken from the paper itself (meta_source paper_text). arXiv ids are correct. | – |
| 21 | applied | The 13 folders include the target and duplicates. | Appendix M03: 9 unique studies besides the target. |

Verdict changes: none (M03, M02, M12 stay standard).
