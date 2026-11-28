# Triage of the independent evaluation (2026-11-28)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | Prior list re-read: 48 perception, neuroimaging and education rows, 17 non-decoder or off-task rows and 12 duplicate versions found; population rebuilt with explicit exclusion and merge lists; prior 221 -> 167, [concurrent] 21 -> 20, unresolved 20 -> 10; cvf-xu20-aemsr dated 2020-06 (prior) | Appendix population line; all "of 221" counts; audits; slots |
| 2 | applied | Target Sec. 3.3, Alg. 1 (temporary student update, then master update); Xiao et al. Abstract (bidirectional distillation); Meta Pseudo Labels and Learning to Teach abstracts read | Verdict, M02 usual approach and evidence, Appendix M02; refs added; verdict stays standard (single LRS2 values) |
| 3 | applied | Ma et al. Table 1 (87.9% top-1, no LM, 12.1% WER < 14.3%); V2P Sec. 4 (5-gram LM, 3,886 h) | Verdict last sentence; M12 slot note |
| 4 | applied | USR 2.0 table (LP Conf 12.8, ViT3D-CM 17.0); LP Conformer abstract (12.8%); USR Table 6 (Auto-AVSR 14.6%, 3,448 h, LM) | M12 state of the art; USR 2.0 reference dropped |
| 5 | applied | Snippets: 1806.06053 grows the number of words, 1904.04817 starts on subsequences of length 8, 1906.12170 adopts Chung's curriculum; 9 of 9 length-ordered | M03 usual approach, Appendix M03, M03 audit (n 9, all pids listed), slots |
| 6 | applied | Chung et al. Sec. 3.1 "we start training only on single word examples" | M03 evidence ("all three start on single words") |
| 7 | applied | Sec. 3.3 "a validation set" against Alg. 1 line 11 "Resample training audio, video, label pairs" | Outrun bullet (stated as inconsistency); question reworded |
| 8a | applied | Table 1 speech recognition 15.7 against Table 4 audio teacher 17.2; Sec. 1 same structure | Outrun bullet |
| 8b | applied | Table 6 "only LRW" against Sec. 4.2 pretraining on LRW plus LRS2/LRS3 pretrain sets; both 18.7 | Outrun bullet |
| 8c | applied | 24.3 sits in Table 6's "w/ CL" row | First outrun bullet |
| 9 | applied | SyncVSR Sec. 4: tokens from vq-wav2vec; Transformer in Table 1 | M02 state of the art; gap called not like-for-like; audit metric |
| 10 | applied | Crossref: 10.1109/ICCV.2019.00080 (pp. 713-722) and 10.1109/ICASSP40776.2020.9054253 (pp. 2143-2147) | refs.json, bib |
| 11 | applied | 4.1 of 7.9 points is the reviewer's arithmetic | Verdict "(inference)" |
| 12 | applied | The video-teacher result is the authors' own motivation (Sec. 1, Sec. 3.3) | Bullet dropped; replaced by the inconsistencies of 8a-8c |
| 13 | applied | Afouras quote does not say "fixed" for Li et al. | Wording removed from M02 |
| 14 | applied | Xiao counted in both teacher-source and jointly-trained classes | Appendix M02: fixed teacher 3 (ASR 2, video 1), video branches 1 |
| 15 | applied | Inclusion requires a lip-reading/VSR/LRS/LRW term | Appendix: "AVSR studies without such a term are outside"; "AVSR" dropped from the population name |
| 16 | applied | cvf-xu20-aemsr is CVPR 2020 | Date list in tools/exclude_reading.json |
| 17 | rejected | Audit read_fulltext role for the sub-word paper is "prior" with timing "concurrent": the audit schema allows only target, sota or prior; the text labels it [concurrent] | none |
| 18 | applied | Claim-table row 21: V2P beats the target by 3.9 points on LRS3 | M12 evidence |

Counts: 18 findings, 17 applied, 1 rejected. Verdict changes: none (M02, M03, M12 stay standard; M07 not reported).
Gates after triage: check_review 0 FAIL, 1 WARN (read budget from reused tables); verify_quotes 0 missing; audit_tally 0 FAIL.
