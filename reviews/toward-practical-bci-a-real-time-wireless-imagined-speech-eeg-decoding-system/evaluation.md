# Evaluation: Toward Practical BCI: A Real-time Wireless Imagined Speech EEG Decoding System

Date: 2026-11-20. Fallback evaluator, claim table only (no sources opened). Input: the compact review (Verdict, component sections, 13-component table, "Where the claims outrun the evidence", references) and its claim table. Ledger counts (pattern match, slot-filled, recall) are outside this check; only the claims made are checked. Items marked "general knowledge" come from the evaluator's own knowledge of the literature, not from the claim table, and should be confirmed against the source before use.

## Claim check

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Verdict: paper changes M05, M03, M13, M06; ahead on none; consumer headsets, imagined-speech identification and the group's framework came earlier [2], [3], [4] | Claim rows 1, 7, 9, 10 | correct | [2] (2018), [3] (arXiv Jan 2025) and [4] (arXiv Nov 2024) all precede the target (arXiv Nov 2025) by more than 6 months. |
| 2 | Verdict: M03 and M13 not reported (no identification accuracy, calibration result, latency, online accuracy) | Rows 2, 8, 12; t12, t13, t33 | correct (absence) | Absence claims rest on the full read of the target; no quote contradicts them. |
| 3 | Table I: 62.00% wired, 46.67% wireless, three participants, no stated split | Row 2; t17, t18, t2, t33 | correct | |
| 4 | 15.33-point drop, 24.7% relative | Row 3 | correct | 62.00 − 46.67 = 15.33; 15.33 / 62.00 = 24.73%. |
| 5 | Drop mixes device, channel count, EOG input and recordings; bridging claim (§IV) does not hold | Row 3; t6, t9, t54 | correct | 30 EEG + 2 EOG vs 12-channel headset supported. "Recordings" rests on the absence of EPOC X participant and trial details (M05 text); acceptable. |
| 6 | M05 usual approach: 61 of 167 research-grade amplifier, 21 consumer headset | Row 4 | correct as tally | Tally label is "research_grade_amplifier", not "wired"; the review adds "wired". 61 of 167 is a plurality only of studies that name a device. |
| 7 | Paper adds EPOC X to the predecessor's BrainAmp [4] | Row 5; t9, c3 | insufficient evidence | Quotes give 32 channels with gel in [4] and the 12-channel headset in the target; neither quote names BrainAmp. |
| 8 | [5]: 98.10%, four commands plus neutral, within 900 ms, random 80/20 split | Row 6; c14, c15, c16 | partly correct | 98.10%, 900 ms and 80/20 random split are quoted. "Four commands plus neutral" has no quote. "Windows of one recording on both sides" is inference from a random split and should be marked so. |
| 9 | "Neither it nor the paper's 46.67% holds out a session" | Row 6; t33 | wrong as worded | The target's split is unstated (t33), so the review cannot say it does not hold out a session; it can say neither reports a session hold-out. |
| 10 | Consumer headsets for imagined speech date to 2018 (14-channel EPOC, 27 subjects) [2] | Row 7; c10, c9 | wrong (date); partly wrong (count) | c9 says 20 of the 27 subjects were used. General knowledge: the 27-subject EPOC imagined-word dataset that [2] reuses was recorded and classified by Torres-García, Reyes-García, Villaseñor-Pineda and colleagues around 2012–2013 (five Spanish command words), so consumer-headset imagined speech predates 2018. |
| 11 | M03 usual approach: six studies identify the user (target included); 30 s resting EEG then ten trials per class | Row 8; t12, t13 | correct | |
| 12 | [3]: 2025, 11 subjects, 99.44%, last session held out | Row 9; c7, c8 | partly correct | 99.44 and session hold-out are quoted. "11 subjects" has no quote. Which column 99.44 is (accuracy vs another metric) is not given in the quote. Text says 2025, the reference list says 2026 (journal version); align. |
| 13 | [4] reports 0.995 with all trials permuted | Row 10; c1, c4 | correct | |
| 14 | Pretraining data not stated; predecessor shares amplifier and ethics approval | Row 11; c6, t53 | partly correct | Same IRB number is quoted. "Shares amplifier" has the same gap as No 7. |
| 15 | M13 usual approach: 112 of 167 have no online or real-time term | Row 12 | correct | 167 − 55 = 112. "Offline analysis is the default" is an inference from term absence; acceptable. |
| 16 | [6]: 55.7% adaptive, 52.3% static, two syllables, 20 participants, chance 50% | Row 13; c11 | partly correct | Percentages quoted. "20 participants" has no quote. |
| 17 | [7]: 65% top-1 over 20 online trials, one participant [concurrent] | Row 13; c19, c20 | partly correct | 65% and 20 trials quoted; "one participant" has no quote. Concurrent label right (same conference, arXiv id adjacent to the target). |
| 18 | "Against online results near chance [6], an unlabelled 46.67% in three users is not evidence of practical use" | Row 14 | judgment beyond evidence | [6] is 2-class (chance 50%), the target 4-class (chance 25%). Above-chance margin is 5.7 points in [6] vs 21.67 points in the target, so the comparison cuts against the review. The valid point is that Table I is not labelled online; [6] adds nothing to it. |
| 19 | M06 usual approach: other 48, CNN 37 of 165 | Row 15 | correct as tally; weak | "Other" is the largest family, so the usual approach names no design. Table row also stacks "(slot-filled, of 165) (pattern match 167)", which reads as two different bases. |
| 20 | [8]: 96.4%, four covert syllables, within-subject, 2019 | Row 16 | partly correct | Quote reads "dropped from 96.4% to 94.5%", so 96.4% is one condition (all processing stages included); the review must state that condition. "Within-subject" has no quote. |
| 21 | Predecessor's 0.47 [4] differs from 62.00% in words, participants and split | Row 17; c2, t17 | correct | 0.47 is the SI (speech imagery) mean in [4]. |
| 22 | "Significant and meaningful performance" untested against 25% chance | Row 18; t59, t19 | wrong as worded | The authors state the result is above the 25% chance level (t19). What is missing is a statistical test; say so. |
| 23 | Wireless average recall 0.47±0.00 vs per-class ± up to 0.26; ± undefined | Row 19; t18, t58 | correct | Additional internal inconsistency the review could use: with balanced classes macro recall equals accuracy, yet accuracy is 46.67±0.72 (±0.0072, which rounds to 0.01) while recall is ±0.00. |
| 24 | Only non-rest commands displayed, but decoder has no rest class; EOG enters with only a notch filter; §I cites handwriting and crowd-scene papers; §III.B caveat dropped in §IV | Claim table | no quote | Four positions in "Where the claims outrun the evidence" have no claim-table row. |
| 25 | Chronology and fairness | Rows 6, 13; references | correct | [5] and [7] are labelled concurrent and used only as reference points, not as missed prior work. The headset caveat is credited to the authors (§III.B). No author-reported finding is presented as the review's own. |

Strongest confound: the wired-to-wireless comparison changes device, channel count (30+2 vs 12), EOG input and possibly participants and sessions at once. The review handles it (Verdict, M05). A second confound, chance level across tasks (4-class vs 2-class), is not handled in M13 (No 18).

Verdicts (step 7): no slot is `ahead`. The `not reported` verdicts (M03, M09, M12, M13) follow from stated absences. M01 lists the usual approach as "overt or attempted speech" yet gives `standard` for cued speech imagery; the usual-approach cell and the verdict disagree.

General knowledge, not in the claim table: the Emotiv EPOC X is a 14-channel headset (AF3 and AF4 in addition to the 12 sites quoted in t9). The paper calls it a "12-channel wireless headset", so the two frontal-polar-adjacent channels were apparently dropped without comment. The review can note this alongside the channel-count confound once confirmed against the paper.

Possible stronger online state of the art for M13 (general knowledge, confirm the value): Sereshkeh et al., 2017, International Journal of Neural Systems, online EEG classification of covert "yes"/"no", reported online accuracy around 70% against 50% chance. If confirmed, it is a higher online imagined-speech EEG result than [6].

## Required fixes (ordered by impact)

1. M13: remove the comparison with [6] as support for "not evidence of practical use", or normalise for chance (2-class vs 4-class). Base the position on the absence of online labelling, latency and false-activation data (§II.C.3, Table I).
2. M05: "Consumer headsets for imagined speech date to 2018" is too late. Name the earlier EPOC imagined-word work that recorded the 27-subject dataset (around 2012–2013) and state that [2] used 20 of the 27 subjects.
3. M05: replace "neither it nor the paper's 46.67% holds out a session" with "neither reports a session hold-out"; the target's split is unstated.
4. Claim table: add quoted rows for every position in "Where the claims outrun the evidence" that lacks one (no rest class, notch-only EOG, §I citations, §III.B caveat dropped in §IV), and for the unquoted details: BrainAmp, "four commands plus neutral" [5], "11 subjects" [3], "20 participants" [6], "one participant" [7], "within-subject" [8].
5. M06 state of the art: state the condition behind 96.4% in [8] (the figure before stages were removed, falling to 94.5%).
6. "Untested against 25% chance": the authors compare with chance (§III.A); reword to "no statistical test against 25% chance".
7. [3]: align the year (text 2025, reference 2026) and state which metric 99.44 is.
8. M06 usual approach: "other" is not a design; name the commonest named family (CNN, 37) as the usual approach and give one basis (165 slot-filled), not two.
9. M01: the usual-approach cell (overt or attempted speech) contradicts the `standard` verdict for speech imagery; fix the cell or the verdict.
10. Claim table row 20 cites a "Questions for the authors" section that the review does not contain; remove the row or restore the section.
11. M13 naming: section says "Device and operation", table says "Device and cost"; use one name.

Optional: add the ±0.00 recall vs ±0.72 accuracy inconsistency (No 23) and, once confirmed, the 14-vs-12 EPOC X channel note.

## Scores

- Procedure: 6/10. Target quotes and arithmetic are sound; several comparator conditions and four outrun-the-evidence positions have no quote.
- Final text: 6/10. Clear position and correct core numbers; one cross-task comparison works against the review, and one dating claim is too late.

Strengths (brief): the wired/wireless confound is identified and decomposed; split leakage in [4] and [5] is flagged with quotes; concurrent works are labelled and not treated as prior.
