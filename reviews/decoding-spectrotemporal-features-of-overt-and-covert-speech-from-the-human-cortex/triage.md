# Triage of the evaluation

Date: 2026-11-26. Input: decoding-spectrotemporal-features-of-overt-and-covert-speech-from-the-human-cortex.eval.md (16 findings). Each finding was checked against the target source text, the named source passages (Tran 2010 thesis Table 4.1, Pei 2011, Kim 2025), notes.json and the topic audits. Result: 15 applied, 1 rejected (partly: the author-name abbreviation is produced by the reference script). Gate after the changes: check_review 0 FAIL, 0 WARN (body 6,999 characters); verify_quotes 115 found, 0 missing; audit_tally 4 of 4 ok.

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | w-2246823171 Table 4.1: "Cepstral distortion (dB) between converted speech and target audible speech by using phonetic segmentation (seg) and by using DTW". Whispered/NAM output was scored against the DTW-aligned audible recording of the same utterance before 2013-11. Under the any-signal rule used for M04, M11 is standard. Toda and Shikano 2005 is not in the wiki and is not cited. | M11 verdict ahead to standard (slots.json, Verdict, M11 section, verdict.json). The neural novelty is stated as a finding with an Appendix reference. Tran 2010 added as a reference and notes entry r1. |
| 2 | applied | Target: 5/7 spectrogram (t29), 4/7 modulation (t35), 1/7 identification (t44). Baseline is "a separate resting state recording session" (t67). 0.30/0.34 = 88% (inference). | M11 section reports all three figures, the unmatched rest session and the missing matched null. |
| 3 | applied | The audit note lists the 10 prior hits: 2 decode speech, none covert. Pei 2011 (doi-10.1088-1741-2560-8-4-046028) was read: covert vowel decoding significant in 5/6 subjects, ten-fold within each dataset (p1, p2). | M11 usual approach gives no field-practice count (matched=null); Pei 2011 named and cited; Appendix description corrected; audit read_fulltext updated. |
| 4 | applied | The M04 priors are on mouthed speech; the target cites none of them and frames the transfer as a representational test (t70). | "borrowed" and "moves this design" removed; mouthed-vs-covert difference stated; authors' framing credited; Pei 2011 named as the neural covert decoder trained within condition. |
| 5 | applied | 23 and 15 are all-year counts. The tally confirmed_unique 25 counts version keys; usual_approach n 23 merges versions (recorded in the M04 audit basis). | Body: "3 of 3 prior", "1 of 1 prior"; the 122 of 173 sentence was removed from the M12 body and kept in the Appendix; table denominators added. |
| 6 | applied | Kim 2025 does not cite the target. | "later work reuses it" removed; Kim stays as state of the art. |
| 7 | applied | Covert neural data never enter training (t13); the issue is text overlap (t55). | Claims-outrun bullet rewritten; question to the authors updated. |
| 8 | applied | | verdict.json position now uses "most of the covert correlation is the DTW floor (rest 0.30 of covert 0.34)", matching the review. |
| 9 | applied | | "whole-wiki full-text check" and the verdict-rule sentence removed from the body. |
| 10 | applied | | M12 covert rank tied to Pasley's single-trial 0.76 (inference). |
| 11 | applied | t68 "there is no simple ground truth"; t69 "a major difficulty in this approach is the alignment". | M11 section credits the authors' own caveats. |
| 12 | applied | (0.46-0.42)/(0.66-0.42) = 0.17. | One fifth (spectrogram) and one sixth (modulation), marked (inference). |
| 13 | applied | Berezutskaya 2023 is a closed-set 12-word classifier. | M12 state of the art replaced by listener open transcription (Wairagkar 2025, already read); Berezutskaya removed. |
| 14 | not applied (optional) | Komeiji 2024 remains the matched comparator, as the evaluator notes. | none |
| 15 | applied | | Table: M04 3 of 3 prior, M08 1 of 1 prior, M12 1 of 5 prior, M11 no count. |
| 16 | rejected in part | refs.json and the .bib carry "Heinze, Hans-Jochen". build_refs.py abbreviates every given name to its first initial, so the rendered list shows "Heinze, H."; the header line gives the full name. | refs.json, .bib |

Final verdicts: M04 standard, M08 standard, M11 standard (was ahead), M12 standard; M01, M02, M03, M05, M06 standard; M07, M09, M10, M13 not_applicable.
