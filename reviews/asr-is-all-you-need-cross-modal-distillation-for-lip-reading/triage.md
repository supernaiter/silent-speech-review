# Triage of the evaluation (round 1)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | Wei/Li et al. 2019 is not in the wiki and was not read; target §1.1 states the difference (t73: teacher trained with ground truth on the student's dataset, "does not apply naturally to unlabelled audio-visual data"). M02 standard now rests on inconsistent effects across datasets (0.3 vs 3.2 points), one WER each, distillation not isolated (t65). Verdict unchanged (standard): with the effects inconsistent and unrepeated, ahead is not met. | Verdict s3-4; M02 evidence and closing verdict; slots M02 note |
| 2 | applied | Target §5: "similar performance on LRS2 (58.2%)" (t72). Parity now credited; the 0.3-point gap is no longer called a weakness. | Verdict s3; M02 evidence |
| 3 | applied | Audit: 77 = dated prior population with no regex hit. Relabelled "absence count"; self-supervision named as not searched for this review. | M02 usual approach; table M02; Appendix; audit usual_approach_<slug> |
| 4 | applied | Perfect Match (arxiv-1809.08001) abstract: "embeddings for visual speech recognition in self-supervision" (c15); word-level. Exclusion reason corrected; absence claim narrowed to ASR labels or distillation; named in the Appendix. | Verdict s2; M02 usual approach; Appendix; audit population |
| 5 | applied | Sari et al. 2018 Sec. 2 (c12, c13) and Tatulli and Hueber 2017 Sec. 3.1 (c14): audio forced-alignment frame targets on transcribed data. Named as closest earlier designs; design difference stated (no transcript, soft posteriors). | Verdict s2; M02 usual approach; Appendix; audit forced_alignment_class |
| 6 | applied | USR 2.0 Table 7: USR 2.0 no LM (c17); SynthVSR 16.9% with LM and synthetic video (c16). Condition stated, SynthVSR cited from Table 7. | M02 and M12 state of the art; slots |
| 7 | applied | 61.7% uses no human labels; USR 2.0 uses 656 h of human labels (c17). Mismatch labelled. | M02 state of the art |
| 8 | applied | Target gives one WER per row and no run count (t40). "Single run" replaced by "one WER, no run count". | Verdict; M12 heading and body; slots M03, M12 |
| 9 | applied | V2P ±0.9 is a test-resampling standard error of one system (c4, c11). Rescoped; the LRS2 sentence no longer uses it. | Verdict; M12 |
| 10 | applied | Audit exclusion list: siciliano03, talkerxmod and 1804.04121 are not among the 77. Hits given among the 118 raw and among the 77 separately. | Appendix; audit prior_hits_among_77 |
| 11 | applied | Abstract "on a large-scale audio-only corpus" (t71); §6 "Given resource constraints we only" (t74). Reported first; the fine-tuned-rows argument dropped. | Claims outrun, bullets 1-2 |
| 12 | applied | Target §2 (t7, t8, t64): valid-word share of teacher output, then teacher versus second-recognizer WER. | Claims outrun, bullet 2 |
| 13 | applied | t29: TM-seq2seq marked as trained on non-public data; Conv-seq2seq reference added (cvf-zhang19-stfcsl, ICCV 2019, [concurrent]). Its decoder is covered by "no comparator decoders or language models". | M12; Verdict; References |
| 14 | applied | Suzuki et al. 2019 abstract (c10): close-talk to throat-microphone acoustic model. Now called adjacent with an acoustic student; audit recount 1 same family + 1 adjacent. | M02; Appendix; KD audit |
| 15 | applied | Reference 8 is ICASSP 2024, arXiv 2023-02. Text now "arXiv 2023; ICASSP 2024". | M12; slots M12 |
| 16 | applied | "snippets read" and "corpus paper excluded" moved to the Appendix. | M02, M12 usual approach |
| 17 | applied | All-dates totals labelled "all dates, not used in the comparison", including slot-filled 31. | Appendix |
| 18 | applied | Wording now "no comparator decoders or language models (Table 3)". | M12 usual approach |
| 19 | applied | M03 is not audited; the "ASR-agreement filter" basis claim is removed (usual "–", note "Inherited; not audited"). | slots M03 |

Counts: 19 applied, 0 rejected, 0 unverified. Verdicts unchanged (M02 standard, M12 standard). Gates after triage: verify_quotes 0 missing; audit_tally 3/3 pass; check_review 0 FAIL, 1 WARN (read count from reused published tables plus four new reads: Sari 2018, Tatulli 2017, Perfect Match abstract, USR 2.0 Table 7).
