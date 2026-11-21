# Triage of the independent evaluation

Date: 2026-11-21. Each required fix was checked against notes.json, the target source text (Sec. 3.2–3.4, 4.1, 5, Tables 1–2, reference list), the named papers' passages and the two topic tables.

| # | Class | What was done |
|---|---|---|
| 1 | partly correct | The quoted phrase is in the source (Sec. 5) but split across a column break; t72 now quotes "Notably, our model pretrained on large-scale data from" and t78 the continuation. Review text unchanged. |
| 2 | partly correct | Sec. 3.3 ("the 16 sessions used for pretraining") and 16.1 h against 1.9 h per healthy split plus 1 h for the patient indicate the silent test sessions are excluded, so leakage is not supported. t73 quote fixed; Verdict, M03 and the patient bullet now say "training sessions"; M03 adds that the issue is within-subject pretraining, not leakage (inference); the authors' question now asks about sessions 17–20 and their paired vocalized sessions; open item in verification_status. |
| 3 | correct | Added t77 (Table 2 header: scratch, GAP, ES, SS, OTFK) and t76 ("The model incorporating SS", the start of the best-tokenizer sentence in Sec. 4.1); the mapping 61.5 / 100 / 49.5 / 50.0 / 55.8 is confirmed. Review wording kept. |
| 4 | partly correct | Both counts are real: 370 is the ledger pattern match, 379 the design-tally population including full-text hits. M03 text, table cell and Appendix now state the tier of each. |
| 5 | partly correct | [3] kept as the yardstick for an unseen layout and user; M06 now says it is invasive spectrogram regression, not comparable in value with EEG/EMG word accuracy. Non-speech EEG montage models fall outside the M06 inclusion rule and no ahead or absence claim rests on them; noted in verification_status. |
| 6 | wrong | The 49.2 h eego row is quoted in t13 (Table 1); the claim table now maps it. No text change. |
| 7 | correct | Added c18 (Table 3 subject-layer row, 14.4); "the same ordering" replaced by "one at a time; the paper compares alternative tokenizers, and its subject-specific layer also wins". |
| 8 | correct | Added c16 ("LOSO evaluation (n = 27)") for [4], and c17 (pre-training on I−1 subjects) plus an extended c12 quote ("Top-10 accuracies of 61.3%") for [5]. Text unchanged. |
| 9 | partly correct | Labels kept (the missing items are single-modality results and inference hardware); the M05 and M13 cells now name what is not reported. |
| 10 | correct | Wording changed to "with no reported split or uncertainty"; added that the English data are EMG only, so the test says nothing about EEG (t80). |
| 11 | partly correct | c14 already states the multi-subject model used ECoG grid data only; c13 quote extended to "using only data on 8x8 grids"; text now says "8x8 ECoG grids of 15 participants". |
| 12 | correct | "Without seeds" replaced by "with no seed count" (t47); row limitations updated. |

Applied 11 of 12 (fix 6 wrong; fixes 1, 3 and 8 changed notes and the claim table only). Steps 6–8 rerun: check_review 0 FAIL, 0 WARN; body 6,975 characters.
