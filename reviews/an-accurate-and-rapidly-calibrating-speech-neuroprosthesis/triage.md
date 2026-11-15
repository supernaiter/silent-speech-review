# Triage of the ChatGPT evaluation (2026-11-15, round 1)

Source: an-accurate-and-rapidly-calibrating-speech-neuroprosthesis.eval-chatgpt.md. Checked by short passage searches in the target and named papers; new evidence entries c1-c4, w6, m3, p2, l3, y4, y5 added to notes.json (verify_quotes: 77 found, 0 missing).

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | "Best in the field" was wider than the evidence; 2.5% is final-session Copy Task WER (t8) | Verdict: "lowest online large-vocabulary WER among the topic's ledger candidates (Appendix)", Copy Task named |
| 2 | applied | 213 + 260 sentences confirmed (c1, c2); sentence count is not calibration time | Verdict: "comparable to one day of T12's calibration sentences (inference)" |
| 3 | rejected | 97.5% = 100 - 2.5 is already marked (inference); conversational measures already kept distinct | none |
| 4 | rejected | "real advance" / "main advance" is the reviewer's position, backed by t13 and the M13 tally | none |
| 5 | rejected | "over the course of 13 days of training-data collection" (m3, Metzger Results); counts are in the Appendix, absent from the compact only | claims.md mapping |
| 6 | rejected | "We recorded 213 sentences over 30" minutes (c1); "an additional 260 sentences of training data" (c2) | claims.md mapping |
| 7 | rejected | Arithmetic confirmed by the evaluator; the confound is already stated | none |
| 8 | rejected | CORP = "Continual Online Recalibration with Pseudo-labels" (p2); "without Recalibration for 3 Months" (l3, title) | claims.md mapping |
| 9 | rejected | "two in area 6v ... and two in area 44 (part of Broca's area)" (w6): half of T12's arrays | claims.md mapping |
| 10 | rejected | Ledger tally in Appendix and audit M05 | none |
| 11 | rejected | Area 4 targeted (c4); 55b named in the target's Discussion (t38); four arrays in T12 (w6) | claims.md mapping |
| 12 | applied | "best" narrowed to "lowest ... among the topic's ledger candidates (Appendix)" | M05 State of the art |
| 13 | applied | Offline confirmed (y5: ensembles "have not been tested in real-time settings"); T15 = this participant is not stated in the target | M05: "T15 data, this paper's participant (inference)"; "later gains come from the decoder" |
| 14 | applied | 39 unique vs 21 slot-filled records mixed bases; audit gives 31 with a recorded design | M13 Usual approach: "of the 31 with a recorded design, 21 ... and 2 deployed" |
| 15 | applied | Target wording is "self-paced"; a researcher launched the system (t47) | M13: "self-paced conversation" |
| 16 | rejected | Three months from Luo title (l3); [concurrent] by date (Luo online 2023-10-24, target medRxiv 2024-04-10) | none |
| 17 | rejected | Online prompted-sentence WER is the stated evaluation in both priors (w1, m2) | none |
| 18 | applied | t55 is an absence in the main text only | M12: "the main text reports no training seeds" |
| 19 | applied | Accuracy vs WER mixed in one comparison | M12: "99.6% accuracy ... to set against T12's 9.1% WER" |
| 20 | rejected | Evaluator marks it correct | none |
| 21 | rejected | Source: "1-2% word error rate when reading a paragraph" (target Discussion) | none |
| 22 | applied | "most plausible driver" ranked placement without evidence | M05: "one candidate driver of the gain over T12, untested within the participant" |
| 23 | rejected | Self-recalibration in [3] confirmed (p2); proposal tied to M13, handwriting stated in M03 | claims.md mapping |
| 24 | unverified | Appendix counts and verdict rules were not in the compact; they come from the audits | verification_status |
| F6 | rejected | Chronology: Fan 2023-11 and Luo 2023-10 are within 6 months of target first public 2024-04 (c3: NEJM text "based on a previously available preprint posted on medRxiv", April 10, 2024). Target's own [concurrent] label is a build artifact | verification_status |
| F2-T15 | unverified | T15 identity inferred from Yoon et al. (y4) and the trial context; target text does not use the label | verification_status |

Counts: 9 applied, 13 rejected, 2 unverified (plus F6 rejected, counted in 16). Verdict classes unchanged; short verdict unchanged.
