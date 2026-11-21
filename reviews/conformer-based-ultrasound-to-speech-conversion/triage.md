# Triage: Conformer-based Ultrasound-to-Speech Conversion

Date: 2026-11-21. Source: conformer-based-ultrasound-to-speech-conversion.eval.md (fallback evaluation, 12 required fixes). Each fix checked against the source texts of the target and named papers, notes.json and the topic audits.

| # | Classification | Reason | Where applied |
|---|---|---|---|
| 1 | correct | [2] Table 2 test MSE: FCN 0.400, 2D CNN 0.366, 3D CNN 0.315; "about 21%" matches the drop from the FCN, the 2D-CNN drop is 13.9%. | Verdict and M06 now give 0.366 to 0.315 (13.9% relative, inference) and say [2] used another single-speaker corpus with vocoder targets; notes p1, p2; fix_row.py canon_before |
| 2 | correct | The M06 audit counts fully connected DNN 37 against CNN 31, so "usual = CNN, 31" was not supported. | M06 usual approach restated as frame-wise DNN (37) or CNN (31) regression; slots.json M06 field and matched 37; audit usual_approach; extra.json; Appendix |
| 3 | correct | Table 2: Base MCD is higher for all four speakers, p = 0.001 for 01fi, 03mn, 04me; bi-LSTM 04me p = 0.002 is in Table 2. | M06 evidence paragraph and slots note; quotes added (t88, t89) |
| 4 | correct | 99.26% and 15.93% are single-speaker TaL1 results from a re-implementation, unlike the target's four TaL80 speakers. | Verdict frames them "as context only" with the setup difference; verdict.json position; quote with 99.26 added (c8) |
| 5 | correct | Sec. 3.4 states the rest of the bi-LSTM network is the same as Conformer Base, so its input is also one frame's beam lines. | M06 usual approach and evidence now cover both variants; quote added (t87) |
| 6 | correct | Table 2: bi-LSTM MCD is higher for all four speakers, significantly for 04me (p = 0.002). | M12 paragraph rewritten |
| 7 | correct | The 2023 SSW paper's Table 2 lists Baseline as the first column (mean 2.148 dB = mean of 2.175, 2.038, 2.218, 2.162) and Sec. 2 names the same four speakers. | Quotes added (p7, p8); text unchanged |
| 8 | correct | Sec. 6.2 of [3]: all 81 TaL80 speakers pooled, 95/5 utterance-level split. | Wording "with all 81 TaL80 speakers pooled"; quote added (c10) |
| 9 | partly correct | No prior attention-based ultrasound-to-speech mapper exists to name; the prior "transformer" hits are spatial transformer networks, which the review now names. | M06 sentence and Appendix cite the spatial transformer paper (new [4]); quote p9; audit read_fulltext and note |
| 10 | correct | The 2016 Hueber and Bailly paper supports a transcription test in 2016, not the start of the practice. | Softened to "were in use by 2016"; no earlier work added |
| 11 | correct | 21 counts MCD alone; no co-occurrence count exists in the audit. | M12 usual approach reworded to "MCD (21), often with MUSHRA (14)"; slots, audit, Appendix; claim table regenerated; co-occurrence logged in verification_status |
| 12 | partly correct | "Matched the performance of the baseline" (t19) and the baseline MSE row (t26) were already quoted in notes; the beam-line, Zenodo and Tongue2Speech design quotes were missing. | Quotes added (t86, t90, c9); claim table refilled with quotes per row |

Applied: 12 of 12 (10 correct, 2 partly correct, 0 wrong, 0 unverifiable). Steps 6-8 rerun: check_review 0 FAIL, 0 WARN; body 6,991 characters.
