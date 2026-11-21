# Triage of the independent evaluation

Date: 2026-11-21. Each required fix was checked against notes.json, the target source text (Sec. II-A, II-B, III-B, IV-A, IV-B, V-E, Tables II and V, reference list [1]-[53]), the passages of the named papers and the three topic audits.

| # | Class | Reason and what was done |
|---|---|---|
| 1 | partly correct | The target quotes already existed in notes.json (t3, t4: 128/10 channels; t9, u2: 0.5-200 Hz, no regression; t22-t37: Fig. 3 values; t41-t44: Table II CER; t45: 145/10 patient split; t84: mode order; t87: no seeds), but the claim table showed one quote per row. Added t100 (Table V title, "from a representative subject") and t101; the claim table now lists every supporting entry and quote per row. Review text unchanged for this item. |
| 2 | partly correct | The 2024 intracortical result (2.5% WER, final five sessions, 125,000-word vocabulary, one participant) is in its main text (p22, p23) and predates the target, so M12 state of the art now names it [8], with [9] kept for the never-duplicated held-out condition; that the 2024 evaluation sentences are absent from training is not stated in its main text (verification_status). The 2021 silent-EMG result is now named as the nearest non-invasive yardstick. Topic table state_of_the_art left as published; read_fulltext appended. |
| 3 | partly correct | The ledger tally does not count whole-test-set WER/CER reporting, so "typical practice" was unsupported; the rule for `behind` is met on the best-comparable-work yardstick (four earlier works read and named that report an error rate over every test sentence). Verdict and M12 now say "behind the best comparable work"; slots note updated. |
| 4 | correct | Willett et al. 2023 is Nature 620, 1031-1036 (confirmed by the PMC copy's citation line and by citing papers in the wiki; the manifest's 621 was wrong). refs.json corrected. |
| 5 | partly correct | 11.89% is quoted in the M02 audit but had no notes entry; the source shows it is synthesized audio scored by Whisper-medium (21.32% by DeepSpeech), guided by a pre-trained silent-EMG text recognizer. Added p18-p21; M02 state of the art now gives both scorers and names the 2024 recognizer (12.2% WER with language-model rescoring) [7] as the prior bar. |
| 6 | correct | Added p11 (Table 3, only sEMG 10.52), p12 (57 EEG and 5 EMG channels), p13 (decision-level fusion), p15 (eight subjects). Text unchanged. |
| 7 | correct | Added u5 (reference list [1]-[53] read; no EEG+EMG fusion study cited) and the Verdict now says "not among the paper's 53 references"; M05 now locates the EEG vs EEG+EMG comparison at Fig. 3 and §IV-A (t101, u1). |
| 8 | correct | Sec. IV-A gives whispered MCD 4.73 for EEG+EMG and 4.71 for EEG alone; text now says "4.73 with EMG vs 4.71 without". |
| 9 | correct | Added p14 (3.30-point drop vs sEMG only); M05 now gives 10.52% to 7.22%, 3.30 points or 31% relative (inference), and says [2]'s own "31.63% reduction" is the drop from EEG only. |
| 10 | correct | Added p16 (reconstruction, adversarial and CTC losses) and p17 (twelve words/phrases) for [4]. Text unchanged. |

Applied 10 of 10 (4 partly correct, 6 correct; fixes 1, 6 and 10 changed notes and the claim table only). Steps 6-8 rerun: check_review 0 FAIL, 1 WARN (14 papers read in full besides the target, budget 8: the M02 and M12 topic tables carry reads from earlier reviews, and this round added the 2024 intracortical study and the 2024 silent-EMG recognizer to settle fixes 2 and 5); body 6,962 characters.
