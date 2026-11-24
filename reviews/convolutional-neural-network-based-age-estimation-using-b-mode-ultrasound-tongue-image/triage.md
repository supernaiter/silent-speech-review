# Triage: Convolutional Neural Network-Based Age Estimation Using B-Mode Ultrasound Tongue Image

Evaluation: language-model evaluator over compact.md and the claim table (18 findings, 8 required fixes). Triage by the writer against notes.json and the specific source passages.

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | §4.1 states a random 80/20 selection with no grouping by child (t16, t54); crossing of children is an inference | Verdict: "almost certainly fall on both sides (inference)" |
| 2 | applied | Shandiz 2021 Table 1 header "Segment length (frames & seconds) / Aggregated frames / Error rate (Dev Set)", row "21 (0.25 sec) 1 3.16%"; Sec. 5.1: 21 frames is the case with one frame-level output and no temporal pooling; 50 TaL80 speakers (Sec. 4). Not a single frame (notes c13, c25, c26) | Verdict: "a 0.25 s ultrasound segment identifies 50 speakers with 3.16% error" |
| 3 | applied | Fabre 2015 is tongue-contour tracking on 9 speakers, a different setting. Wiki UltraSuite papers before 2020-07: UltraSuite 2018 (dataset), Ribeiro 2019 diarization (no held-out-speaker design), Ribeiro 2019 classification (LOSO), Eshky 2019 synchronisation (held-out UXTD/UPX speakers, c27, c28). Only two same-corpus priors: the behind rule (3 papers) fails | M12 verdict downgraded to standard in text, slots, extra.json, audit deciding_priors_note; Verdict reworded; Appendix gives the same-corpus count (2) |
| 4 | applied | A [later] work cannot carry the verdict basis | Table cell M12 now names Ribeiro 2019 (same corpus, 59.42% vs 74.70%) first, Al Ani 2024 as later context; M12 state-of-the-art line leads with Ribeiro |
| 5 | applied | Ribeiro 2019 (c5) and Al Ani 2024 report pooled multi-speaker conditions beside held-out ones; the 0 count was a pattern artefact | Usual-approach line rewritten; "random frame split 0" removed from text, Appendix, audit and extra.json |
| 6 | applied | 48 vs 43, both upper bounds | Text "about equally common"; table field "Held-out (48) or speaker-dependent (43)"; audit usual_approach design |
| 7 | rejected | Notes c23 quote reads "we utilised data from nine speakers sourced from the UXTD dataset"; the evaluator saw a truncated excerpt | No change |
| 8 | confirmed | Arithmetic correct and marked (inference) | No change |
| 9 | applied | Eq. (1) is read from extracted text (t22); a lost superscript is possible | "the extracted Eq. (1), named MSE, shows no square"; open item in verification_status |
| 10 | confirmed | Nine Table 3 rows are t27-t35 | No change |
| 11 | confirmed | c2, c3, c18 | No change |
| 12 | confirmed | Diener 2020-10 is [concurrent] | No change |
| 13 | rejected | The M08 state of the art comes from the reused published table (append-only; kept); Diener holds out sessions, which is the control the review argues for, while Shandiz [2] is used in M12 as the mechanism of the confound | No change |
| 14 | applied | UPX has multiple sessions per child (t12) | "each UXTD child carries one label" |
| 15 | confirmed | t14, t15, t48, t63 | Clinical-linguist item removed for length; frame-count item kept |
| 16 | unverified | Tongue2Speech 15.93% from the published M06 table (read by an earlier review), not re-read here | No change; noted in verification_status |
| 17 | applied | t43, t44: 4.87 vs 5.35 | M08: "only 9% lower (inference) even before leakage" |
| 18 | confirmed | Appendix count 0 of 99 | No change |

Counts: applied 9 (1, 2, 3, 4, 5, 6, 9, 14, 17), confirmed without change 6 (8, 10, 11, 12, 15, 18), rejected 2 (7, 13), unverified 1 (16).
