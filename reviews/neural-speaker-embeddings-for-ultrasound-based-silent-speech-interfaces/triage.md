# Triage: Neural Speaker Embeddings for Ultrasound-based Silent Speech Interfaces

Date: 2026-11-20. Each fix checked against notes.json, the source text and the topic tables. 13 of 14 applied; check_review 0 FAIL, 0 WARN, body 6,957 characters.

| # | Class | What was done |
|---|---|---|
| 1 | partly correct | Verdict kept: three earlier works ([7], [8], [3]) test across sessions and [3] was read, so the rule for behind holds. Text and table now say the verdict concerns the test protocol; [3] added to the M06 state-of-the-art cell. |
| 2 | correct | TaL Sec. 3.2 (c1, c2, c3): 75 speakers train the decoder; x-vectors come from Kaldi. Sentence rewritten without "pre-trained on 75 speakers". |
| 3 | correct | Verdict and verdict.json credit the seen-speaker condition to the authors (Sec. 5.3); "one run" restated as "no repeated runs" (unstated in the paper); "one recording session per speaker" marked (inference). |
| 4 | partly correct | Source check: both rows (V2SFlow-V and "w/o cs") are in Table III, and Sec. II-B defines cs as the speaker embedding. Added notes c24-c26; numbers unchanged; text says "in one ablation table". |
| 5 | correct | Kojima now reports 0.04% (male) and 1.1% (female) EER and notes EER is not comparable with identification error. |
| 6 | partly correct | Sec. 4 shows the 3,800 blocks (1,145 test) come from the 50-speaker subset; added t58; sentence kept, now says "of the 50-speaker set". |
| 7 | partly correct | Sec. 5.2 states the layer and activation were compared on the same pool; added t59; location now "Sec. 5.2, Table 2". |
| 8 | correct | Sec. 5.3 says "consistent improvement ... marginal"; added t60 and attributed both words; the irrelevant t39 quote removed from all claim rows. |
| 9 | partly correct | "not reported" is in the rule vocabulary, so the verdict stays; the M12 note now says MSE and error rates are reported but seeds, chance level and test-block score are not. |
| 10 | correct | Added c23 (16,639 utterances, TaL Table 1); claim rows for 82 fps (t3) and 80-dim mel and WaveGlow (t22, t49); c8 quote now includes "On GRID corpus". |
| 11 | correct | Single-speaker baseline is TaL1 (t61), so test speakers differ; the 2.5-fold sentence says so. |
| 12 | wrong | The section covers internal inconsistencies; a figure cited for table values is one. Kept. |
| 13 | partly correct | Departure reconciled with standard ([2] made it for lip video); [5] labelled video-to-speech. No search for a later ultrasound result; logged as an open item in verification_status. |
| 14 | correct | Reference [6] container now "ICPR 2020, held 2021"; text dates it 2020; "about 2%" replaced by 2.3% and 2.4% relative (inference) in the review, verdict and row. |
