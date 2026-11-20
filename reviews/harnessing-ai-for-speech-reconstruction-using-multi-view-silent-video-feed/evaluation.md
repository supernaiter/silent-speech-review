# Independent evaluation: Harnessing AI for Speech Reconstruction using Multi-view Silent Video Feed

Date: 2026-11-20. Scope: the compact review and its claim table only. Sources were not re-opened. Each claim was checked against the quote and location in the claim table, the review's own arithmetic, and the evaluator's knowledge of the field. "Insufficient evidence" means that the quote in the claim table does not carry the claim as written. It does not mean the claim is false.

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | The target claims the first multi-view speech reading and reconstruction system | Claim row 1 (Abstract) | correct | The quote supports it. |
| 2 | Two speakers (1 and 10), chosen at random | Rows 2, 13 (Sec. 4.3) | correct | The quote supports it. |
| 3 | "One run, no stated split" | Row 2 | insufficient evidence | No quote shows a single run. "No stated split" is an absence claim and is plausible, but the row cites only the speaker-choice quote. |
| 4 | 0°+30° over 0°: +11.4% / +12.2%, absolute +0.20 / +0.22 | Rows 3, 18 (Table 1) | correct | 1.7674 × 0.114 = 0.20 and 1.7812 × 0.122 = 0.22. The arithmetic is consistent, but the quote shows only the V1 values and not the V1+V2 values. |
| 5 | 0°+60° over 60°: +24.6% / +27.1%, absolute +0.37 / +0.42 | Row 18 | insufficient evidence | The V4 and V1+V4 values are not in any quote. |
| 6 | The authors state 26%, 27% and 80% | Row 17 (Sec. 4.3) | correct for 26%. 27% and 80% are not quoted | Only the male 26% sentence is quoted. |
| 7 | "The text overstates every gain" | Rows 17, 18, 26 | wording stronger than the evidence | The review also asks the authors how the figures were computed (row 26). Without the source of the authors' baseline, "cannot be reproduced from Table 1" is what the evidence supports. |
| 8 | Only the best pairs are shown | Row 19 (Sec. 4.3) | correct | The quote supports it. |
| 9 | Capacity confound: the two-view model gets twice the input (Sec. 3.2) | Row 20 | insufficient evidence | The quote says that training needs multiple views. It says nothing about input size or architecture. The confound is a reasonable inference and should be marked as one. |
| 10 | Headroom: LPC resynthesis gives 2.5291 / 2.6255. Gap 0.56 / 0.63 | Row 21 (Table 2) | correct | 2.5291 − 1.969 = 0.56 and 2.6255 − 1.998 = 0.63, which matches row 4. |
| 11 | PESQ is used for both quality and intelligibility (Sec. 4.2) | Row 16 | insufficient evidence | The quote gives only the PESQ range. No quote shows PESQ being used as an intelligibility measure. |
| 12 | Language independence is claimed and untested. Lexicon left to future work | Row 23 | correct | The quote supports the claim of independence. |
| 13 | The authors call the results "preliminary" and say model size exceeds on-camera deployment | Row 24 | insufficient evidence | The quote attached is the "paucity of space" sentence. Neither "preliminary" nor model size appears in it. |
| 14 | Usual M05 approach is one camera, 693 of 787. 20 of 165 video-to-speech studies are multi-view, none before the target | Rows 5, 28, 30 | consistent | 787 − 94 = 693 and 165 − 20 = 145, which matches the table. These are ledger counts and are outside this check. |
| 15 | Petridis et al. [4]: frontal + profile gains 3% absolute | Row 6 | insufficient evidence | The quote names the best views but gives no 3% figure. A value of about 3% absolute over the frontal view is plausible from memory. |
| 16 | [4] ran 10 runs, subject-independent, with significance tests | Row 8 | insufficient evidence | Neither 10 runs nor significance tests appear in the quote. |
| 17 | Lipper [2]: 2.130 for 0°+45°, 2.315 for 0°+45°+60° | Rows 7, 10 | correct | Both values are quoted. |
| 18 | Lipper: 2.002 frontal, 1.952 for 0°+60°, 1.982 for 0°+90°. +6.4% | Rows 7, 10 | arithmetic correct, values unquoted | 2.130 / 2.002 = 1.064. None of the three values has a quote. |
| 19 | Lipper is [concurrent] | Reference 2 | correct | AAAI 2019 (Jan–Feb 2019) is within 6 months of MM '18 (Oct 2018). The review does not treat it as prior work. |
| 20 | Hush-Hush Speak [3]: 0°+30° 1.920 to 1.941 (+1.1%), 0°+60° 1.847, unseen speakers | Rows 10, 15 | values unquoted. "Unseen speakers" not shown | +1.1% follows from the numbers. An 85:10:5 split does not by itself make a speaker-disjoint split, so the speaker-independence statement needs its own quote. Labelling [3] as [later] is correct. |
| 21 | Hush-Hush adds a five-judge listener test | Row 15 | insufficient evidence | The quote covers only the split. |
| 22 | Vid2speech used 23 MTurk workers [5] | Row 12 | correct | Quoted. |
| 23 | Lip2AudSpec used 20 workers per sample [6]. Le Cornu and Milner report 85% listener word accuracy [7] | Row 12 | insufficient evidence | Neither value is quoted. |
| 24 | M12 state of the art: 16.05% WER and PESQ 1.37, the best raw-waveform system on GRID unseen speakers [8] | Row 14 (Table VII) | wrong attribution / doubtful | The quoted row is "End-to-end WGAN (2022) [20]". That is a baseline cited inside [8], not [8]'s own system. Calling it "best" is not shown, and [8]'s own model or later systems may score better. |
| 25 | M12 is behind "what was typical of the field in 2018" | Section M12 | stronger than the evidence | The 83 of 165 count covers all years, and is about 50%, not a clear norm. Only the three named earlier systems carry the 2018 comparison. |

## Usual approach and state of the art

- **M05, usual approach.** A single camera is plausible as the typical design. The closest earlier design is cited as [4] (2017), but multi-view lip reading to text is older. Examples include Lucey and Potamianos (2006, IEEE MMSP, frontal versus profile lip reading) and multi-view OuluVS2 entries from 2016 (ACCV 2016 workshop on multi-view lip reading, e.g. Lee, Lee and Kim). Naming one of these makes the rebuttal of "first" complete.
- **M05, state of the art.** Lipper (2019) is the best multi-view video-to-speech result the review names. For a 2026 review, a 2019 result from the same group needs a stated reason, for example that none of the 20 multi-view video-to-speech ledger hits reports a better OuluVS2 PESQ. Without that, "state of the art" is not established. I know of no later multi-view video-to-speech result on OuluVS2 that clearly beats 2.315 PESQ, but the review should not leave this to the reader.
- **M06.** "Neural vocoder (49 of 165)" is labelled the usual approach, but it is a minority, and it does not describe the field in 2018. This should be reworded, or the most frequent design should be given.
- **M12, state of the art.** See row 24. There is also a domain mismatch: a WER on GRID is given as the state of the art for an OuluVS2 evaluation practice. The state-of-the-art line should name the evaluation practice (listener test plus ASR WER on unseen speakers) and cite the system that reports it. It should not cite a baseline row.

## Central claim and confounds

The strongest confound, input capacity (two views against one, with no duplicated-view control), is raised, but it is inferred and not quoted (row 9). The review handles the difference in starting point between the target and Lipper (2.002 against 1.7674) correctly. It also correctly treats Lipper and Hush-Hush as concurrent or later, not as missed prior work. The authors' own caveats are presented as theirs. The absence claim ("none before the target") rests on ledger counts and names [4] as the deciding prior. That is acceptable, but older multi-view lip reading should be named as well (see above). The M05 verdict of `standard` is a cautious reading of thin evidence and is defensible. The M12 verdict of `behind` rests on three named earlier systems. It is acceptable once the "typical in 2018" wording is fixed.

## Required fixes (ordered by impact)

1. M12 state of the art: replace the "End-to-end WGAN (2022) [20]" baseline row from [8] Table VII with [8]'s own best system, or cite the original 2022 work. Drop "best" unless the table shows it.
2. Add claim-table quotes for every unquoted comparator value: Lipper 2.002 / 1.952 / 1.982; Hush-Hush 1.920 / 1.941 / 1.847 and the five-judge test; [4]'s 3% absolute, 10 runs and significance tests; Lip2AudSpec's 20 workers; Le Cornu and Milner's 85%.
3. Hush-Hush "held-out / unseen speakers": quote the statement that establishes a speaker-independent split. An 85:10:5 split alone does not show it.
4. Target claims without matching quotes: "one run" (Verdict), "twice the input" (Sec. 3.2), "PESQ used for intelligibility" (Sec. 4.2), "preliminary" and model size (Sec. 4.3, Sec. 6). Add quotes, or mark these as inference.
5. "The text overstates every gain": add quotes for the V1+V2, V4 and V1+V4 values in Table 1 and for the 27% and 80% sentences. Then either keep the claim, or soften it to "cannot be reproduced from Table 1", which fits better with the question to the authors.
6. M12 verdict: replace "typical of the field in 2018" with a count limited to studies up to 2018, or rest the verdict explicitly on [5], [6] and [7].
7. M05 state of the art: state why a 2019 result is still the best multi-view video-to-speech result (ledger check of the 20 multi-view hits), or name a later one.
8. Rebuttal of "first": name an earlier multi-view lip-reading work than [4] (e.g. Lucey and Potamianos 2006, or the 2016 OuluVS2 multi-view entries).
9. M06 usual approach: 49 of 165 is not a majority and is anachronistic for a 2018 LPC-based system. Reword it, or give the most frequent design.
10. M13 "not reported" conflicts with the authors' Sec. 6 statement on model size and deployment. Reconcile the two.

## Scores

- Procedure: 6/10. The arithmetic is consistent, and the chronology labels and the handling of the authors' own caveats are sound. However, many comparator values and several statements about the target have no supporting quote.
- Final text: 6/10. The positions are clear, but the M12 state of the art cites the wrong row, and two positions ("overstates every gain" and "typical in 2018") go beyond their evidence.
