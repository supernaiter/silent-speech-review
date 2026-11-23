# Independent evaluation: emg2speech (Gowda, Comstock, Miller, arXiv:2510.23969)

Date: 2026-11-23. Independent evaluator; input was the compact review and its claim table only. Sources were not re-opened. Outside knowledge that could not be located is marked "unverified".

## Claim checks

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Pipeline ported from [2]: HuBERT units from TTS audio, "learned with CTC and voiced by a pretrained vocoder" (Verdict) | Claim table row 1 (t95, c2, t101) | insufficient evidence | t95 and c2 support adoption and HuBERT units from TTS waveforms. No quote shows CTC for the unit model. t101 names "a pretrained Tacotron", which is a text/unit-to-spectrogram model, not a vocoder. The quote does not support "pretrained vocoder" (also used in the M08 table row). |
| 2 | Own changes: phoneme CTC head with consistency loss (M02), covariance input from [3] (M06); auxiliary phoneme loss for EMG voicing dates from 2021 [4] (Verdict) | Row 2 (t61, c16, c8) | correct | λ_unit/λ_phone/λ_cons, 31×31 SPD matrices and Gaddy & Klein's auxiliary phoneme loss are all quoted. I know of no earlier EMG-voicing study with a phoneme loss (Gaddy & Klein 2020, EMNLP, did not use one, as far as I know; unverified). |
| 3 | Table 6: text route 51.17% WER vs 61.02% direct synthesis "on the 460 evaluated sentences"; "more fluid, natural interaction" untested (Verdict) | Row 3 (t98, t43, t84) | correct numbers; insufficient quote for the phrase | 51.17% and 61.02% are quoted. 61.02% equals the sentence-weighted pool of 62.55% (400 sentences) and 50.82% (60 sentences): (400×62.55 + 60×50.82)/460 = 61.02 (inference). So 61.02% is a listener WER and 51.17% is a decoder-output WER: the scoring differs. The phrase "more fluid, natural interaction" is not in any quote (t84 says only "remains important"). |
| 4 | Listener WERs 62.55% (healthy, vocalized) and 50.82% (ALS, silent) vs 11.89%–12.2% on Gaddy [5], [6] (Verdict) | Row 4 (t31, c14, c15) | correct numbers; "silent" for ALS insufficient | Values match. No quote shows that the ALS corpus was silent (t6 says only "small-vocabulary corpus … from a participant with ALS"). The caveat "other corpora and scoring" is present. |
| 5 | M02 usual approach: "Of 34 studies matching … 10 are synthesis studies" | Row 5, Appendix M02 auxiliary-loss entry | wrong (internal contradiction) | The Appendix says the 34 are already synthesis studies and that 10 of 34 *use* the auxiliary loss ("acoustic targets only, with an auxiliary … loss in 10 of 34"). The section turns this into "10 are synthesis studies". The table row then lists the minority design ("Auxiliary phoneme loss (minority)") as the usual approach. |
| 6 | M02 state of the art: 5.24% listener WER, intracortical, one ALS participant, 2026 [8] [later] | Row 6 (c5, c7) | correct value; insufficient for "one ALS participant" | 5.24% is quoted. "One ALS participant" and "benchmark" are not in the quotes. The DOI prefix 10.64898 is unverified. |
| 7 | M02: best silent-EMG result with an added training loss is 25.14% WER, 10 seeds [9] | Row 7 (c11, c13) | correct value; position contradicts M06 | M06 cites GETS [5] at 11.89% on the same benchmark. Its title says it guides synthesis "via Silent Speech Recognition", which reads as an added recognition loss. If so, 25.14% is not the best with an added loss. The review must reconcile the two or say why [5] does not qualify. |
| 8 | Synthetic targets are prior practice [2], [7] | Row 8 (c1, c2, c5, c6) | correct | [7] is bioRxiv 2024 / Nature 2025, before the target (Oct 2025). |
| 9 | [4] used forced-aligned frame labels; CTC removes alignment | Row 9 (c8, c9) | correct | Montreal Forced Aligner is quoted. |
| 10 | 56.08→51.81 and 52.29→46.98 UER; 4.27 / 5.31 points; 7.6% / 10.2% relative; five seeds; p < 10^-6 (healthy) | Row 10 (t22, t23, t26, t27, t71) | correct arithmetic; p-value attribution insufficient | 4.27/56.08 = 7.61%; 5.31/52.29 = 10.16%. t23 does not show which corpus the p-value belongs to. |
| 11 | Healthy participant vocalized; no own-audio vs TTS-unit comparison | Row 11 (t97, t3) | correct | t3 states that subject audio is not used. |
| 12 | Units map to phonemes at 0% PER (App. B) | Row 12 (t85) | correct (inference marked) | — |
| 13 | M06 usual: 37 of 54 spectral, 19 units | Row 13, Appendix | correct | Matches the Appendix tally. |
| 14 | M06 state of the art: 11.89% WER, GETS 2026 [later] | Row 14 (c14) | correct | Labelled later, not treated as prior. Venue/DOI unverified. |
| 15 | [9]: soft units 26.55% vs mel 25.14% over 10 seeds | Row 15 (c12, c11, c13) | insufficient quote | c12 ("27.78% to 26.55%") and c11 ("to 25.14%") are both before→after improvements. Neither quote names the target type (soft units vs mel) or the row. A Table 1 row label is needed before "units are not shown to help" can rest on it. |
| 16 | Covariance input 56.08% vs spectrogram 62.71% UER (Table 1) | Row 16 (t17, t15, t102) | correct | — |
| 17 | M12 usual: 13 sentence-disjoint, 9 closed of 64 | Row 17, Appendix | correct counts; framing misleading | The Appendix shows held-out speaker (21) as the most-named protocol. The table row gives "Sentence-disjoint test (13)" as the usual approach, although 13 of 64 is a minority. |
| 18 | M12 state of the art: 12.2% WER [6], 2024; here 50.82% on 60 ALS sentences | Row 18 (c15, t35, t40) | correct | 60-sentence test set appears in t40 (row 24). |
| 19 | [3]: 73.53% WER on 1,970 unseen sentences | Row 19 (c17, c19, c18) | insufficient quote | c17 "48.47 73.53" has no column header, and the quote does not show whether 73.53 is WER. No quote shows that the 1,970 test sentences are unseen. |
| 20 | Vocabulary size may explain 50.82 vs 62.55 (inference) | Row 20 | correct | Marked inference. |
| 21 | One participant per corpus; sessions unstated; no seed named for listener audio | Row 21 | correct (absence claim) | — |
| 22 | Phoneme-guidance claim rests on UER; listeners heard only the guided model (Table 5) | Row 22 (t64, t92) | insufficient quote | t92 does not name which model's audio the raters heard. |
| 23 | EMG2TEXT trained "on all 460 sentences" = number of test sentences | Row 23 (t75) | correct | 400 + 60 = 460. The conditional wording is appropriate. |
| 24 | MOS 3.79 over 35 sentences; authors note moderate MOS at high WER | Row 24 (t38, t40, t65) | correct | 25 + 10 = 35. The review credits the authors. |
| 25 | Limitations in §7 (one ALS participant, no long-term test) | Row 25 (t66, t67) | correct | Credited to the authors, not presented as the review's finding. |

## Central claim, confound and fairness

- The strongest confound for Table 6 is scoring plus possible leakage, not only route choice. The 61.02% figure is the pooled human-listener WER on synthesized audio (inference, row 3 arithmetic). The 51.17% figure is an automatic decoder's text output, from a model reportedly trained "on all 460 sentences". The Verdict states the 51.17 vs 61.02 gap as the strongest point against the paper. However, the review's own "Where the claims outrun the evidence" section says the same table may compare unlike conditions. The Verdict must carry both caveats.
- Healthy (vocalized, 6,800 words) and ALS (about 300 words) corpora are compared with the Gaddy silent benchmark. The "other corpora and scoring" caveat is present, which is adequate.
- Chronology: [5], [8] and [9] are labelled later and used only as state of the art. [3], [6] and [7] predate the target. No fairness violation was found.
- Novelty/absence: there is no "first/only" claim. The "date from 2021 [4]" priority is plausible. I know of no earlier counterexample (unverified).
- Verdicts: all are `standard` or `not applicable`. No `ahead` verdict needs checking.

## Required fixes (ordered by impact)

1. Verdict, Table 6: state that 61.02% is the pooled listener WER on audio and 51.17% is decoder-output WER (different scoring). Carry the possible training-on-test caveat (App. D.4, "all 460 sentences") into the Verdict, or stop calling this the strongest point. Add a quote for "460 evaluated sentences".
2. Verdict, M12: add a quote that shows the ALS corpus was silent (or mouthed). Otherwise drop "silent" from the 50.82% label and from the "silent speech is tested only at about 300 words" sentence.
3. M02 usual approach: correct "10 are synthesis studies" to match the Appendix (10 of 34 use the auxiliary loss). Name the typical design (acoustic targets only) in the line and in the component table row, instead of the minority design.
4. M02 state of the art: reconcile "the best is 25.14% with an added training loss" [9] with GETS at 11.89% [5] on the same benchmark. Either state why [5] is not an added-loss method or replace the value.
5. M06: add [9] quotes with Table 1 row labels showing that 26.55% is the soft-unit target and 25.14% the mel target. The current quotes show only before→after values.
6. Verdict / M08 row: the quote names "a pretrained Tacotron", not a vocoder, and no quote supports "learned with CTC". Add the correct quotes or correct the wording.
7. M12 usual approach and table row: say that sentence-disjoint testing (13 of 64) is a minority and that held-out speaker (21) is the most-named protocol. Do not label 13 as the usual approach.
8. M12, [3]: add the Table 1 column header showing 73.53 is WER, and a quote showing the 1,970 test sentences are unseen.
9. "Where the claims outrun the evidence", first bullet: add a quote showing that the Table 5 listener audio came only from the phoneme-guided model.
10. Verdict: quote the "more fluid, natural interaction" phrase from App. D.4. The current quote (t84) does not contain it.
11. M02 state of the art: add a quote for "one ALS participant" and "benchmark" in [8].
12. M02: add the location that ties p < 10^-6 to the healthy corpus.

## Scores

- Procedure: 7/10. Every number has a quote and location, inference is marked, and the later-work labels are correct. Several load-bearing quotes are too thin to show the column or condition (rows 1, 15, 19, 22).
- Final text: 6/10. The position is clear and fair to the authors. However, the M02 usual-approach sentence contradicts the Appendix, the two state-of-the-art lines conflict, and the Verdict's headline comparison omits the scoring and leakage caveats that the review itself raises later.
