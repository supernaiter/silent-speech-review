# Triage: End-to-end Silent Speech Recognition with Acoustic Sensing

Date: 2026-11-20. Each required fix from the evaluation was checked against notes.json, the source texts (target arXiv v1 text and PDF p. 5; named papers) and the topic tables. 12 of 13 applied; gate rerun: check_review 0 FAIL, 0 WARN; verify_quotes 0 missing; audit_tally 3 topics pass.

| # | Class | What was done |
|---|---|---|
| 1 | partly correct | The quote was already in notes (t56, Abstract). Sec. 4.3 defines a domain as users and environments, and the domain-independent test holds out both users and positions, so the Verdict sentence stands. Added t87 (domain definition). The Verdict now cites the Abstract and states the domain definition. |
| 2 | correct | M06 "State of the art" now gives Auto-AVSR (2023, joint CTC/attention, 14.6% visual-only WER on LRS2) [later], checked in its Sec. 4.3 and Table 3 (c23, c24). [2] is relabelled as the closest controlled comparison. Updated the slots, the M06 audit and extra.json, and added the reference. |
| 3 | partly correct | The values were not read off bar heights. Fig. 4(c) prints them as data labels (3.7/2.6, 10.5/8.4, 8.8/8.1), checked on PDF p. 5. Replaced the six duplicate generic quotes (t49–t54) with figure-value entries. The text now says "bar labels, Fig. 4(c)". |
| 4 | partly correct | The target itself cites device-free acoustic gesture tracking (Wang, Liu, Sun, MobiCom 2016; its ref. 18, Sec. 1; t88). Added that reference, limited the M05 novelty to speech in the Verdict and the M05 section, and updated the row's position_in_field. Strata is not cited by the target and is not in the wiki, so it was not added. |
| 5 | partly correct | The contradiction is real, but the paper does not state that no external LM is used (it states beam search and an internal LM, Sec. 3 and 4.4). The M07 row now reads "Beam search; beam width and any external language model not stated", and the verdict stays not reported. |
| 6 | correct | The audits show that the M05 and M06 populations (28 and 132) are ledger pattern matches (22 and 114) plus full-text recall, and that M12 uses the 22 ledger matches. The text now states each denominator. "Mostly combine them" is now a count of mentions, not of use. |
| 7 | correct | Added c17 (Table 1, row FC-15, WER T2 = 55.0%). The text points to Table 1. |
| 8 | correct | Confirmed that the baseline input is the FMCW echo-profile channel alone (Sec. 3.5, c20) and that the result is a dataset baseline (Sec. 5.1, c21). Reworded the M05 state of the art accordingly. |
| 9 | correct | Added c19 (Table 1 header: 70.5 is in the ultrasonic-only column) and c18 (40 kHz transmitter). Reworded to "ultrasonic-only column (Table 1)" and "40 kHz ultrasonic emitter". |
| 10 | correct | Added c22 ("WER-w and WER-c represent the error rates within and across users"). The text names WER-w and WER-c. |
| 11 | partly correct | Kept "standard" and added the reason: the test holds out users and environments, which matches the usual user-held-out approach. The leak is in tuning, and the review treats it as overreach, not as a component difference. |
| 12 | correct | Added t86 with the exact Sec. 4.2 sentence. Claim-table row 24 now maps to it. |
| 13 | wrong | "Our method can be deployed on existing smart devices" is in Sec. 1 (PDF p. 2, before Sec. 2), as t74 records. The Sec. 1 locator stays. Claim-table row 26 now leads with t74. |

Regenerated: the review and bib, refs.json, row and json (fix_row.py updated and rerun), the verdict copy, claims.md (43 rows, all mapped) and compact.md. Body: 6,963 characters.
