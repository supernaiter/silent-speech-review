# Independent evaluation: Ultrasensitive Textile Strain Sensors Redefine Wearable Silent Speech Interfaces with High Machine Learning Efficiency

Date: 2026-11-20. Fallback evaluator (claim table only): the claim table and the review's positions were checked; sources were not re-opened. Bibliographic and state-of-the-art remarks come from general knowledge of the literature and are marked as such.

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target uses one strain channel; 0.09 GFLOPs; 95.25% on 20 words (Verdict, M06) | Claim rows 1, 11 (t10, t11) | correct | t10 "This Work 95.25% 0.09G 1 20 Strain Sensor" supports channel count, FLOPs, accuracy and vocabulary. |
| 2 | 1D CNN with residual blocks and noise-injection augmentation (Verdict) | Row 1 (t22, t30) | correct | |
| 3 | No sensor, channel or augmentation ablation on the same words; no chance level or repeated runs (Verdict) | Rows 1, 2, 23 | insufficient evidence | Absence claims with no locator for where they were searched; acceptable as a reading, but say "the paper reports none" with the sections checked. |
| 4 | Paper never states mouthed or voiced (Verdict, M04) | Row 20 | insufficient evidence | The quote for row 20 is only the table title "Detailed information of the participants."; the dB values 54, 47, 42, 46 are not quoted. |
| 5 | Supp. Table 2 has four speaking levels; elsewhere "three participants" (M03 row, last section) | Rows 20, 21 | internal inconsistency | Four dB values against three participants is unexplained, and no row quotes the participant count. |
| 6 | Gauge factor 317 (M05) | Row 5 (t2) | correct, condition dropped | Source says "within 5% strain"; the review omits the range. |
| 7 | 420% gain is over materials-literature sensors, not speech sensors (M05) | Row 6 (t3, t59) | insufficient evidence | t3 frames the gain "in silent speech scenarios"; t59 says "other reported strain sensors". Neither quote shows the comparators are non-speech sensors. |
| 8 | Prior same-group work: 15 words at 54.6%, one subject, one sitting [2] | Row 5 (r1, r3) | wrong (condition missing) | r1: "The noise dataset produced a mean prediction accuracy of 54.6%". The figure is for the noise dataset; the review states it as the general result. |
| 9 | [4]: 49.87% (2 ch) to 87.53% (8 ch) on 100 words | Row 7 (k1, k2) | correct | |
| 10 | [4] "measured" the link from sensitivity to accuracy | Row 7 (k2, k4) | wrong (overstated) | k2 measures channel count against accuracy; k4 is a qualitative signal comparison ("almost indistinguishable changes"). Neither is an accuracy-vs-sensitivity measurement. "almost" is also dropped. |
| 11 | Tightness robustness read from DC offsets (Fig. 4c) | Row 8 (t35) | insufficient evidence | t35 does not mention DC offsets. Fig. 4c is also cited for R-CAM maps in the last section; one panel cannot be both without a locator. |
| 12 | R-CAM maps (Fig. 4c) read as attention without quantitative test | none | no quote | No claim-table row. |
| 13 | [3]: 85.8% on 26 NATO words, subject-independent folds; 100% to 29.41% across tightness and vocal effort | Rows 4, 14 (c1, c2, c3) | correct | "neck-worn choker" is not in any quote. |
| 14 | [3]: re-test 2 weeks after re-attachment | Row 14 (c6) | correct | |
| 15 | [5]: 99.6% on 50 words on day one, 2024 | Row 10 | insufficient evidence in table; correct from general knowledge | Only a ledger reference, no source quote. Card et al. (NEJM 2024) do report 99.6% with a 50-word vocabulary on the first day. Published after the target (May 2024), so [later] is right. |
| 16 | 0.09 vs 1 GFLOPs is a 91% cut, matching the stated 90% | Row 11 (t9, t10, t21) | correct | 1 - 0.09 = 0.91. |
| 17 | Rows of Supp. Table 1 differ in vocabulary, channels, protocol; same-data comparison only in Supp. Fig. 10 | Row 12 | correct | |
| 18 | 80/20 split of 100 samples per word | Row 15 (t14) | correct | |
| 19 | Grouping of the split "matches its lineage, one sitting [2] and randomly mixed folds [4]" | Row 16 | wrong (attribution) | [4] (Kim et al., Nat. Commun. 2022) is from a different group, not the authors' lineage. Only [2] is lineage. |
| 20 | Transfer: 80% with 15 to 20 samples per class for new words and users | Row 17 (t31) | correct | |
| 21 | New-user task has 5 words (chance 20%) | Row 17 | no quote | t34 says the new-word task uses ten words from Dataset 2; nothing quoted gives 5 words for the new-user task. |
| 22 | [3] reaches 80% with 20 per class on 26 words | Row 17 (c5) | insufficient evidence | c5 "an accuracy of 80% compared to 76% with 20 samples per class" is ambiguous about which condition gives 80%, and "26 words" is not in the quote. |
| 23 | "100% unresponsive" rests on one 100 dB demonstration (Fig. 3a) | Rows 18, 19 (t7, t8) | correct | |
| 24 | Accuracy not saturated with training size (Supp. Fig. 11), credited to authors | Row 22 (t37) | correct | Fairly attributed to the authors. |
| 25 | Usual approaches: M05 multi-channel 18/27; M06 "other" 82 of 355, CNN 35; M12 speaker-disjoint 65/143 vs 58 random and 44 session | Rows 3, 9, 13, 27-41 | correct as ledger counts; framing weak | M06: "other" is not a design, so it cannot serve as the usual approach. M12: 65 + 58 + 44 = 167 > 143, so the categories overlap and "against" reads as exclusive. 65/143 is a plurality, not a majority. |

Central confound: the review handles both main confounds, different vocabularies (95.25% on 20 words against 87.53% on 100) and FLOPs compared across different tasks. The verdict that sensitivity drives accuracy is untested is backed by the stated absence of ablations. Fairness: [3] and [5] are labelled [later] and are used as state of the art, not as missed citations; correct. No "first / only" claims. Non-standard verdicts (M04, M12 not reported; M07, M09, M10 not applicable) are consistent with the evidence given.

State of the art: [5] is an intracortical speech neuroprosthesis. Using it as the state of the art for a wearable-strain 1D CNN decoder compares across modalities, so it says little about this decoder. A wearable-sensor closed-vocabulary result would be a more useful comparator, or the line should say why a cross-modality figure is used.

## Required fixes (ordered by impact)

1. M05: add the noise-dataset condition to [2]'s 54.6% (r1 says "noise dataset"), or give [2]'s clean-condition result as well. Without it the lineage comparison understates the prior work.
2. M05: replace "[4] measured it" with what [4] measured: accuracy against channel count (49.87% to 87.53%) and a qualitative signal comparison with a metal gauge ("almost indistinguishable changes"). Neither is accuracy against sensitivity.
3. M12: remove [4] from "its lineage". [4] is another group's work. Only [2] is the authors' lineage.
4. Fig. 4c is cited both for DC-offset tightness robustness and for R-CAM maps. Check the panel for each, add a quote showing DC offsets (t35 does not show them), and add a claim-table row for the R-CAM statement.
5. Participants and speaking levels: quote the 54/47/42/46 dB values from Supp. Table 2 and the participant count, then resolve four values against "three participants". Row 20 currently quotes only the table title.
6. Transfer: give a source for "new-user task has 5 words" (t34 gives ten words for the new-word task) or drop the 5-word and 20% chance statement.
7. [3] transfer comparison: restate c5 exactly (80% against 76%, and under which condition) and quote the 26-word vocabulary for that experiment.
8. M06 usual approach: "other" is not a design. Name the most common identifiable family (CNN, 35) or explain what "other" contains. Add a source quote for [5]'s 99.6% instead of the ledger-only row, and note that it is intracortical.
9. M12 usual approach: say the split categories overlap (65 + 58 + 44 > 143) and call 65 a plurality, not "the usual" design without qualification.
10. Restore dropped conditions: gauge factor 317 "within 5% strain"; 420% gain framed by the authors "in silent speech scenarios, within small strain ranges". Either quote the Fig. 1c comparators to show they are not speech sensors or soften the "not speech sensors" claim.

## Scores

- Procedure: 7/10. Every numeric claim has a claim-table row except the R-CAM statement and the [5] figure. Several quotes do not carry the condition the text attaches.
- Final text: 6/10. The position is clear and the main confounds are handled. One prior result loses its condition, one comparator is misattributed to the lineage, and one sentence overstates what [4] measured.
