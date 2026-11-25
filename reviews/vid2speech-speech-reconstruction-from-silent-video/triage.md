# Triage of the evaluation (round 1)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | Lip2Wav Table 2 and Sec. 6.1: its own runs, mean of 4 GRID speakers, Google Speech-to-Text API (notes l1, l2, l5, l7) | Verdict: Lip2Wav sentence now reads "As a whole system under Lip2Wav's protocol (Google ASR, mean of 4 GRID speakers)"; verdict.short updated |
| 2 | applied | Le Cornu and Milner Table 4: "DNN UNV DNN + 2D-DCT + Filterbank Unvoiced" (new note c12) | M06: the inference "pixel input alone does not explain the gain" dropped; the sentence now states only "DNN on 2D-DCT features scored 26.9% (Tables 4–5)"; the M05 usual-approach line names mouth-centred DCT |
| 3 | applied | Kefalas Table IV: WGAN (2022) 4.07 is the lowest; best own row 4.54 (k5); Lip2Wav row footnoted "Reported using Google speech-to-text API" (k7). Table VII: WGAN 16.05 lowest, best own row 17.08 (k6) | M06 and M12 state-of-the-art lines now say "lowest WER ... WGAN (2022) row", give the authors' best own row, and state that the recognizers differ so the WER scales are not comparable. Later GRID systems the evaluator named (SVTS, VCA-GAN, unit-based) were not checked beyond Table IV/VII, where SVTS-S (17.84) and VCA-GAN (5.62/24.52) are above the WGAN rows; other later work unverified |
| 4 | applied | SKILL.md rule: ahead needs no ledger paper with the same design plus repetition; 15 studies name the full face (M05 audit), and the paper's evidence is one unrepeated figure (t73, t28) | M05 verdict sentence now gives the reason for standard |
| 5 | applied | 19% chance in [2]: c13 (Sec. 5.2); K = 9: t73 (Sec. 3.1, "both at K = 9"); 8th-order LPC: t74 (Sec. 2); Lip2Wav raters: l8 (Sec. 6.3.2, 15 participants) | M12 (19% citing both), M05 ("both at K = 9"), M12 state of the art (15 raters); claim table remapped |
| 6 | applied (first part); rejected (second part) | Pooled counts only (t31); the 79% in the t36 row is the separately retrained S2 column (t37), not part of the S4 comparison | Outrun bullet 2: "pooled counts give no way to show the two differ" |
| 7 | applied | t73, t74 | As in 5 |
| 8 | applied | Le Cornu and Milner Table 5: GMM ORIG 48.6 with original voicing (c4); target calls GMM UNV "the best results of [10]" (t38) | Outrun bullet 3: added "Its 'best results' are the unvoiced row; oracle voicing gave 48.6% (Table 5)" |
| 9 | applied | l8 | M12 state of the art |
| 10 | applied | k3 (one ASR, 0.1% WER on real audio), k2, l8 | M12 state of the art now names the protocol first, then the value |
| 11 | no action | Confirmation of chronology and fairness | – |
| 12 | applied | Pages of [3] and [4] are not in the wiki sources or manifests (arXiv versions read) | Pages removed from refs.json for [3] and [4]; DOIs kept |

Central-confound note (listener pool MTurk vs 20 laboratory listeners): not added to the text for length; the response-format confound is stated and the 23 vs 20 listener counts are in notes (t31, c9).
