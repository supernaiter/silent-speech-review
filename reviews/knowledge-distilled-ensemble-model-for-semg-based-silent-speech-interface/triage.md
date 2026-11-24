# Triage of the independent evaluation (12 required fixes)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied (partly) | Hinton et al. 2015 is not in the wiki and was not read, so it is not cited. w1/w3: Ma et al. use born-again (single-teacher) distillation; the M02 tally finds an ensemble teacher in 2 of 131 studies. The text now says only the ensemble teacher is new and why that does not make the slot ahead (one split, no repeats). | Verdict; M02 body; M02 slot note |
| 2 | applied | t103: student architecture not stated (Fig. 4 caption). Conditional statement: if ResNet1D, the 81.2% row is the no-teacher control. | Verdict; M02 body |
| 3 | applied | t106 (Table II caption, N = 6); 147.9/21.1 = 7.0 vs 2.50/0.12 = 20.8. "Most of it" now limited to size. | Verdict |
| 4 | applied | t81, t98, t99: 2.50/6 = 0.42 ms vs 0.12 ms (inference). | M13 body |
| 5 | applied | New entries z1, z2 (Zhu: ten optimal electrodes, ten digits), wa1 (Walliczek Table 1 header, 27 ms TDC word models), t107 (Table III header), c17 (Tang: four electrodes; c16's "4" is subjects); h3 already contains 82%, quote was only truncated in the table; Ma Table 3 with/without stays tied to row order and w9, noted in verification_status. Claim table quotes no longer truncated. | notes.json; claims.md |
| 6 | applied | Audit pattern_counts: label is audio_or_asr_teacher; ensemble_teacher pids = target and arxiv-2502.05766 (audio-visual). "cross-modal" dropped; full-text basis stated. | M02 usual approach; Appendix |
| 7 | applied | Audit: channel_count 8 and 4, n = 2 each of 17. | M05 usual approach; slots field |
| 8 | applied | t32 (authors report 4.8% loss), t45 (authors propose domain adaptation for inter-subject/gender shift). | Claims outrun; What the field needs next |
| 9 | applied | c14-c16: 96%, 10 words, random 80/20 split; h1/h2. M06 state of the art now Tang 2025 with CVOS as same-vocabulary reference. | M06 State of the art; slots M06 sota |
| 10 | applied | refs.json: first_public 2020-07, ICASSP 2021. | M02 State of the art |
| 11 | applied | t83 quote is Sec. V.A; Table IV holds the values (t70-t76). | M05 body |
| 12 | applied (partly) | "unseeded" replaced by "no seed or repeats reported" (t50). MUTE author list rejected: the paper's first page lists Meltzner, Heaton, Deng only. | Verdict |

Counts: 10 applied, 2 partly applied (one part rejected each: Hinton not citable, MUTE author list correct), 0 unverified.
