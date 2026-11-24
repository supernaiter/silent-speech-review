# Triage of the independent evaluation (11 findings)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | Only Katsamanis 2011 is a continuous rtMRI sequence recognizer; Prasad 2014 is voice-activity detection, van Leeuwen 2019 static phoneme classification (notes c18-c20). No other earlier rtMRI recognizer with repeated tests is in the 88-study population (Appendix tally; Saha 2018 uses one split). The behind rule (3 comparable earlier papers) is unmet. | M12 verdict changed to standard (Verdict, M12 section, slots, verdict.json, extra.json); the other two named as different tasks. |
| 2 | applied | Katsamanis uses one speaker (c35); the target tests two unseen speakers (t6). | Verdict and M12 verdict sentence: ahead of the 2011 prior on speakers, behind on repetition and sentence-disjointness. |
| 3 | applied | Otani 2026 reports one random 43/4/4 split, no repeats or seeds stated (c21, c34). | M12 state-of-the-art line: "also use one split". |
| 4 | applied | 11 of 88 is a minority (Appendix). | M12 usual approach now "a single split; only 11 name repeats..."; table cell "Single split; repeated splits"; M08 usual approach worded as the most common output (16 of 75). |
| 5 | applied | Ahead rule needs repetition (SKILL.md step 4); the output is new among 88 studies. | Verdict and M08 text: new, rated standard only because the ahead rule is unmet; slots note. |
| 6 | applied | Auto-AVSR (2023): LRS3 visual-only WER 19.1%, confirmed in source (c32); in the published M06 ctc-vs-attention table. | M06 state of the art adds lip reading; table cell; refs.json entry ma2023autoavsr; Appendix. |
| 7 | applied | Quotes added: Fig. 3 caption (t100), Csapo "10 sentences for testing" (c33), Tongue2Speech single-speaker WER and Whisper ASR (c30, c31). | M06 state of the art reworded ("ASR on synthesized speech, one speaker"); claim table. |
| 8 | applied | Target reference list [10] is Kim et al. 2014 (t101); not in the wiki. | M05 text: "the paper's reference 10, Kim et al. 2014". |
| 9 | applied | Table cell ambiguous. | M12 choice: "One 8/2 speaker-disjoint split, no repeats". |
| 10 | no action | Fairness check passed. | – |
| 11 | applied | LM ablation 44.1 to 40.6 PER (t26, t29); 3.5 points is the reviewer's subtraction. | Claims section, LM bullet, marked (inference). |

Applied 10, rejected 0, unverified 0, no action 1. To stay within 7,000 characters, three lower-priority items were removed: the M04 next step, two author questions (75-frame truncation of references, hyperparameter selection data) and the explicit 17-speaker detail. The removed points stay in notes.json (t95, t19) and in the table (M03 not reported).
