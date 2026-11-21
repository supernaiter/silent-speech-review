# Triage: From Silent Signals to Natural Language (arXiv:2509.04507)

Date: 2026-11-21. Source of findings: the "Required fixes" list in the evaluation file. Each fix was checked against the target text (and the Fig. 2 image of the PDF), the texts of [3] and [6], and notes.json. Result: 12 of 12 applied (6 correct, 6 partly correct, 0 wrong, 0 unverifiable). Gate after the fixes: 0 FAIL, 0 WARN, body 6,950 characters.

| # | Fix | Classification | Reason | Where applied |
|---|---|---|---|---|
| 1 | M07 threshold contradiction | partly correct | The table was right: Sec. 2.5 states "A confidence threshold of 0.7"; the M07 text wrongly called it unstated, and what is missing is its selection data. | M07 text rewritten; notes t49 |
| 2 | Quote for 20.6% in [3]; say gains are about equal | correct | [3] Sec. 5 gives "a silent EMG validation WER of 20.6% as MONA"; absolute gains are 2.5 vs 2.6 points. | M07 text; notes c13; claim row 10 |
| 3 | Full sentence behind c5 | partly correct | Full sentence reads "a 36% WER when directly synthesizing audio", so it is the audio route and the review's reading stands; only the quote was truncated. | M06 text quotes the phrase; notes c5 |
| 4 | Name the source of 28.8% and its test set | partly correct | It is Gaddy's 2022 thesis model on the Gaddy 2020 benchmark test set ([3] Table 3); named in the text via [3]; no separate reference added, and the target's own split is not identified, which is already a finding. | Verdict; notes c10; fix_row.py |
| 5 | Quotes for GETS 21.32% and the 11.89% dataset | correct | [6] Table 1 caption names the silent EMG test set and lists GETS at 21.32% with DeepSpeech. | M06 text; notes c9, c12 |
| 6 | Replace "no split" | correct | Sec. 3 names "the complete test set (≈100 utterances)"; the split is used but not identified. | Verdict, verdict.json, en.json, slots M12, fix_row.py |
| 7 | Single hypothesis and N-best sentence | partly correct | Claim holds: Sec. 2.5 "the Transformer ASR provides the initial transcription", and the N-best sentence sits in the paragraph on the broader speech community; only the quotes were too short. | notes t47, t48; claim row 8 |
| 8 | Quotes for 1000 Hz and the convolutional front end | partly correct | 1000 Hz was already in notes t1 (Sec. 2.2) but not mapped; Fig. 2 in the PDF labels a "convolutional & transformer encoder" while Sec. 2.3 says Transformer encoder only, so the bullet stands. | Bullet reworded; claim row 20 |
| 9 | Quote the near-real-time wording | correct | Sec. 3: "making the system feasible for near real-time applications". | Real-time bullet; claim row 21 |
| 10 | Reason for "not reported" on M03, M12, M13 | correct | Rows showed reported content only; each now names the missing detail (selection data, split/seeds/intervals, timing endpoints). | slots.json M03, M12, M13 |
| 11 | Support "fixed its test model before testing" | partly correct | Supported by [3] Sec. 4.6 ("as chosen a priori to the first evaluation on the test set"), but the quote was missing; wording made precise. | M07 text; notes c11 |
| 12 | Claim-table fixes (row 3, row 11 location) | correct | c9 does not support row 3; row 11 mixed target and [3] locations. Claim table rebuilt with per-entry locations and paper ids. | claims.md, compact.md |
