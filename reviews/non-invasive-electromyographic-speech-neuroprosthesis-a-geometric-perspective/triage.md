# Triage: Non-invasive electromyographic speech neuroprosthesis: a geometric perspective

Date: 2026-11-21. Input: the evaluation in `non-invasive-electromyographic-speech-neuroprosthesis-a-geometric-perspective.eval.md` (claim-table fallback, 11 required fixes). Each finding was checked against the source text of the target and the named papers, and against the target's public code (emg2speech, commit 7659eeff).

| # | Classification | Reason | Where applied |
|---|---|---|---|
| 1 | partly correct | Meltzner et al. Table 2 shows that the four data sets together make up Corpus 3 (2,200-word vocabulary, about 1,200 phrases) and lists five subjects, so the original condition was right; only the supporting quotes were missing. | Verdict, M02 state of the art ("8.9% mean WER over four phrase sets"), verdict.json, row; notes c1 (condition), c10, c11 |
| 2 | partly correct | The 31 sites, 5,000 Hz, 31×31 SPD matrices and the fixed common eigenbasis are all in the paper (Sec. 4.1, Sec. 5, Sec. 3.1); the existing quotes did not show them. | Notes t6, t10, t11 requoted, t86 added; M06 location "Sec. 3.1, Sec. 5" |
| 3 | partly correct | The notebook fits the Fréchet mean over `range(9000)` ("Use only TRAIN-VAL data"), and the split cell sets train [:8000], validation [8000:9000]. The point stands; the earlier quote was paper text, not code. | Notes t69 requoted from code; code locations 241-253 and 307-323 in the text |
| 4 | partly correct | "67 unique words" is stated in Appendix C.1 (it was in notes t42); the review cited only Table 3. | Location changed to "Appendix C.1, Table 3"; notes t91 |
| 5 | correct | GETS states 11.89% WER on the silent EMG test set (Sec. 1, Table 1, Whisper-medium) but no notes entry existed. | Notes c12 added |
| 6 | correct | The SpecAugment omission (Sec. 5.1) and the VAL/TEST CER column headers (Table 2) had no quotes. The authors also note that dropping SpecAugment works against their method, so the review now reports that, and names weight decay as a second added change. | M06 paragraph; notes t89, t90; row evaluation_limits |
| 7 | partly correct | 1,970 is stated in Sec. 5 ("8000, 1000, and 1970 sentences"); the existing quote missed the number. "Not reported" refers to seeds and repeats, not the test set, and the table did not say so. | Notes t12 requoted; M12 table cell "1,970 held-out sentences; no seeds reported" |
| 8 | correct | The paper reports no seeds or repeat count, which is an absence of reporting, not proof that one run was made. | Verdict, M06 paragraph, verdict.json, en.limitations, row evaluation_limits |
| 9 | partly correct | "Approximately 8 hours" and "over 6500 unique words" are both the paper's own words (Sec. 2.1), so "over" stays; the quote and section were missing. | Notes t87, t88; location changed from Sec. 4 to Sec. 2.1 |
| 10 | partly correct | The review never claims Meltzner et al. 2018 is the earliest silent-only label training, but "in 2018" could read as a first date. The earlier works the evaluator names were not read, so they are not cited. | Verdict and verdict.json now say "by 2018"; open item in verification_status |
| 11 | correct | Benster et al. Table 1 lists Gaddy silent examples as (EMG, text label) pairs; the earlier quote was about missing audio. | Claims bullet reworded; notes c13 added |

Totals: 11 findings; 4 correct, 7 partly correct, 0 wrong, 0 unverifiable. All 11 were applied in full or in part. After the fixes, steps 6–8 were rerun: verify_quotes reported 0 missing, check_review reported 0 FAIL and 0 WARN, and the body is 6,723 characters.
