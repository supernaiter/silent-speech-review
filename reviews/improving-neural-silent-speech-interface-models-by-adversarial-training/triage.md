# Triage: Improving Neural Silent Speech Interface Models by Adversarial Training

Date: 2026-11-21. Evaluation: improving-neural-silent-speech-interface-models-by-adversarial-training.eval.md (fallback evaluator, 11 required fixes). Each fix was checked against the target text (arXiv v1), the cited source texts, notes.json and the two audits.

Result: 10 applied (9 correct, 1 partly correct), 1 wrong, 0 unverifiable. Gate after the fixes: 0 FAIL, 0 WARN, body 6,969 characters.

| # | Classification | Reason | Where applied |
|---|---|---|---|
| 1 | correct | The MSE-only model losing on MSE has several explanations (weak baseline, regularizing adversarial term, 1-to-5-frame output change in §4.2); the Verdict now lists them and marks the point "(inference)". | Verdict; verdict.json; "Where the claims outrun" MSE bullet |
| 2 | correct | No sentence in the paper states a single run; t86 records only that seeds, runs and variance are not reported. "One run" replaced by "no repeated runs or variance reported". | Verdict, M02, "Where the claims outrun", slots.json M02/M12 notes, verdict.json, en.json, fix_row.py |
| 3 | correct | §6 already limits the first-attempt claim to ultrasound-based SSIs (t2); the Verdict now reports this as the authors' own scope and keeps the video-to-speech precedent [2]. | Verdict; slots.json M02 note; verdict.json |
| 4 | correct | §4.1 gives only partition counts; the split procedure is not stated (t87), so "random utterance splits" was unsupported. Next step rewritten to ask for the split procedure. | "What the field needs next" M03; slots.json M03 note; en.json session |
| 5 | correct | Table 3 has STOI, ESTOI, PESQ, SISDR, SDR, PMSQE and MCD (the unnamed seventh column is PMSQE); Table 2 adds MSE and R2. Table cell and M12 text now list all nine. | M12 section; slots.json M12 choice |
| 6 | correct | The M12 audit records the four group studies as a pattern match of MUSHRA in the full text; the Verdict now says MUSHRA, adds "(pattern match, Appendix)" and rests "behind" on the group's own 2020 MUSHRA study [csapo2020waveglow]. | Verdict; verdict.json |
| 7 | correct | [wu2022deep] uses EMA input, so it cannot rank the target's loss design; Crossref confirms Proc. Interspeech 2022, pp. 779-783, doi 10.21437/Interspeech.2022-10892. | M02 state of the art; refs.json, refs JSON and .bib |
| 8 | partly correct | Patch-GAN, Wasserstein critic, "generation resulted in noise" and "16 sentences" are in the source texts and their quotes were added to notes.json (t13, c1, c2, c8; verify_quotes 0 missing); 82 fps, 25-frame and 80-band already had quotes (t31, t11, t10) and were added as claim rows; "perceptual and smoothness" rests on c1's text and the total-variation passage, not a separate quote. | notes.json; claims.md rows 1, 9, 18, 43-46 |
| 9 | correct | The Table 2 quotes lacked the column order; the Table 2 and Table 3 headers from the paper are now prefixed to the table quotes, so test MSE is columns 3 and 7. | claims.md rows 4, 14, 21 (and Table 3 rows) |
| 10 | wrong | The published review contains "Questions for the authors" and the Appendix; only the compact evaluator text omits them by design, so the claim rows point to real text. | not applied |
| 11 | correct | Table counts mix two populations (slot-filled over 7,388 wiki papers; pattern match over a topic's candidate set of 400 or 51); an Appendix line now states both. | Appendix (outside the body count); claims.md row 42 |
