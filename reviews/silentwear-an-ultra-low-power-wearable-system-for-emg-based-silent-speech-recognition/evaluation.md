# Independent evaluation: SilentWear (arXiv:2603.02847)

Date: 2026-11-23. Fallback evaluator (claim table only). Input: the claim table, the Verdict and the component sections of the compact review. No sources were opened; every "correct" below means "the quoted passage supports the claim as written", not "verified against the original".

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | 15,489-parameter CNN runs on the neckband, one inference per 100 ms | Row 1 (t27, t58) | correct | Both numbers in the quotes. |
| 2 | Sensor is the authors' 2025 neckband [2], reused unchanged | Row 2 (t73, c1) | correct | t73 supports reuse. "Unchanged" goes slightly past the quote. The M05 text says the wet reference was already removed in the 2025 version, but the table gives no quote for that. |
| 3 | 20.5 mW including inference is below every read raw-streaming wearable [2], [3], [4] | Rows 3, 8 (t61, c4, c7) | insufficient evidence | 20.5, 22.2 and 46 mW are quoted. No quote is shown for 76.5 mW [4] (c10). [2] is the same hardware, so the gap is 1.7 mW from sending labels instead of raw data. Channel count and sampling rate are not normalised across [3] and [4]. |
| 4 | Supervised recovery after repositioning dates from 2005 [5] | Rows 4, 14 (c11) | insufficient evidence | c11 gives only the 76.2% drop. 97.3%, 87.1%, "seven-channel" and "digits" have no quote. Nothing quoted shows the 2005 adaptation used labels. t41 is from the target, not [5]. |
| 5 | Headline 77.5% tests days already in training; an unseen day gives 59.3% | Rows 5, 21 (t29, t33) | insufficient evidence | Both numbers are quoted. No quote shows that an inter-session fold is a different day rather than a different session on the same day (t12 is cited but not quoted). |
| 6 | Quantized on-device model has no accuracy figure; accuracy comes from a GPU | Row 10 (t71, t72) | correct | Absence is recorded as unstated. This is the authors' own setup, not a hidden caveat. |
| 7 | 63.9 µJ per inference, 2.47 ms, 0.639 mW for inference | Rows 7, 9 (t62; t59, t60 not shown) | correct (arithmetic) / insufficient evidence (source) | 63.9 µJ every 100 ms = 0.639 mW, which is consistent with t62. 63.9 µJ and 2.47 ms have no quote. |
| 8 | 27.1 h battery from 20.5 mW and 150 mAh | Row 3 (t61) | correct | Consistent at about 3.7 V nominal. |
| 9 | M13 usual: 24 of 30 studies "with an embedded processor" decode off the body | Row 6 (audit, c8) | insufficient evidence | The audit row has no "embedded processor" qualifier. c8 supports [6] for off-body decoding. |
| 10 | M13 state of the art is the target itself | Row 7 | wrong (procedure) | Naming the target as state of the art is circular. It also sits badly with "strongest part" and the `standard` verdict. Either name the best external work or say that no read prior reports on-body inference power. |
| 11 | Novelty claim (§IV-F) holds; other energy-per-inference matches decode handwriting from EEG | Row 30 | insufficient evidence | §IV-F is not quoted. The EEG studies are not named. |
| 12 | M03 usual: 11 of 41 label-free; 5 fine-tune on labeled new-session data | Rows 11, 34 | insufficient evidence | The audit row gives 11 only. Row 34 is cut off before the 5. 11 of 41 is a plurality at most, not a usual design. |
| 13 | [7] reaches 92.24% across days without calibration (25 sentences, three seeds) | Row 12 (c13) | correct / insufficient evidence | c13 supports 92.24%. "25 sentences" and "three seeds" have no quote. |
| 14 | One labeled round lifts silent accuracy 58% to 72% | Row 13 (t46) | correct, condition missing | The quote applies to the 1400 ms window. The review leaves this out. 58% differs from the 59.3% inter-session figure. |
| 15 | Silent drop 77.5 to 59.3 = 18.2 points, 23.5% relative | Row 15 | correct | 18.2 / 77.5 = 23.5%. The "(inference)" tag is unneeded. Four subjects, 9 classes, three speakers and 10 digits have no quote (t4, t6). |
| 16 | One round = 20 repetitions per command, about 10 minutes | Row 16 (t49) | correct | |
| 17 | M05 usual: 16 of 21 use patches; 7 use a collar or neckband | Rows 17, 38 | wrong (internal) | 16 + 7 = 23 > 21. The overlap or double counting is not explained. |
| 18 | [8] 98.7% on five phrases, textile scarf; [3] 92.7% on 11 voiced words with wet reference; [6] 96% on 10 words, silver paste, random splits | Row 18 (c14, c6) | insufficient evidence | 98.7% and 92.7% are quoted. "Five phrases", "scarf", "11 words", "wet reference", "random splits" and the whole [6] figure (c9) have no quote. Nothing shows that [8] senses EMG; it may be another modality. Accuracies on 5, 10 and 11 classes are not comparable. |
| 19 | M12 usual: 143 studies, 65 speaker-disjoint, 44 session-disjoint, 58 random | Rows 19, 42 | correct, wording | 65 + 44 + 58 = 167 > 143, so the categories overlap. Say so. 65 of 143 is a plurality. "None speaker-disjoint" is supported by t15. |
| 20 | [9] reaches 85.8% on 26 words, subject-independent | Row 20 (c16, c15) | correct | Stratified 5-fold "under a subject-independent setting". The quote does not say whether this means leave-subject-out. |
| 21 | Abstract leads with within-session 84.8 / 77.5; unseen-day 71.1 / 59.3 | Row 21 | correct (numbers) | Same caveat as #5 on "day". |
| 22 | "Superior to our prior solution" compares the target's 9-class leave-one-batch-out with [2]'s 8-class shuffled 5-fold on one subject | Row 22 (t74, c2) | wrong | c2 shows that [2] reported leave-one-session-out accuracies of 64±18% (vocalized) and 54±7% (silent). The like-for-like comparison is the target's inter-session 71.1% and 59.3%, which supports the authors' claim (+7.1 and +5.3 points, with different subjects and class counts). The "shuffled 5-fold on one subject" description has no quote (c3 not shown). |
| 23 | Random Forest baseline: 62.9% vs 77.5% within session; 48.7% vs 59.3% across sessions | Row 23 (t31) | insufficient evidence | 62.9 appears in t31, but the quote does not say which column. 48.7 (t35) has no quote. |
| 24 | "less than 10 minutes" (Abstract) conflicts with about 10 minutes (§IV-D) | Row 24 (t48, t49) | overstated | "Less than 10 min" against "corresponding to 10 min" is imprecise, not a conflict. The review misses the sharper point: the vocalized recovery is exactly 10 points (70 to 80, t46), not "more than 10%", unless the abstract means relative change. |
| 25 | ITR 92.7 and 69.2 bit/min are calculated, not measured in closed loop; no chance level; one seed, 42 | Rows 25, 26 | correct / insufficient evidence | The ITR values and the 800 ms window are quoted. The §V closed-loop statement (t53) and seed 42 have no quote (code locations only). The non-closed-loop limit may be the authors' own statement; if so, attribute it to them. Chance level for 9 balanced classes is 11.1%; the review could give it. |

## Central claim and confounds

- The within-session vs. inter-session confound is handled well (Verdict; "Where the claims outrun the evidence").
- The comparison with the prior work [2] is mishandled: see #22. The review rejects a claim that the quoted source evidence partly supports.
- The power comparison does not separate the same-hardware saving (22.2 to 20.5 mW, [2]) from differences in channel count and radio across [3] and [4].
- The 2005 vs. 2026 repositioning comparison names its different starting points, but it does not give the 2005 drop (21.1 points, 21.7% relative) that the reader is invited to compare.

## Fairness and chronology

- [7] is arXiv:2609.21436 (September 2026), about six months after the target (arXiv:2603, March 2026). Label it [later], not [concurrent]. It is used as state of the art, not as a missed citation, which is fair.
- [2] is listed as "Prior" and also tagged [concurrent]. The authors cite it as their own prior work. Use one label.
- "Accuracy comes from a GPU" and the ITR closed-loop limit restate the authors' own disclosures. Present them as such, not as findings of the review.

## Verdicts

All slot verdicts are `standard` or `not applicable`, so the `ahead` rules are not triggered. M13 names the target itself as state of the art while marking it `standard`. Resolve this with an external state of the art or an explicit statement, so the verdict follows the rules.

## Required fixes (ordered by impact)

1. Rewrite the "superior performance compared to our prior solution" bullet. [2] reported leave-one-session-out 64±18% / 54±7% (c2), which compares directly with the target's inter-session 71.1% / 59.3%. Drop or quote the "8-class shuffled 5-fold on one subject" description, and say that the like-for-like gap favours the target.
2. Replace the M13 state of the art "the target itself" with the best external work, or state that no read prior reports on-body inference power. Reconcile this with "strongest part" and the `standard` verdict.
3. Add quotes for every unquoted number or condition: 76.5 mW [4]; 97.3%, 87.1%, seven channels and digits [5]; 63.9 µJ and 2.47 ms; 48.7% and the RF column for 62.9%; five phrases and scarf [8]; 11 words, wet reference and random splits [3]; 96%, 10 words and silver paste [6]; 25 sentences and three seeds [7]; four subjects; seed 42; the §V closed-loop statement; the §IV-F novelty claim.
4. Fix the M05 counts (16 + 7 > 21) or explain the overlap.
5. Relabel [7] as [later], and give [2] a single label (prior).
6. Confirm that [8] is sEMG. If it is not, label the modality or replace it as the M05 state of the art. State that 5-, 10- and 11-class accuracies are not comparable.
7. Show that "unseen day" equals an inter-session fold, or say "unseen session".
8. Soften "conflicts" on the 10-minute claim. Add that the vocalized recovery is exactly 10 points (70 to 80), not more than 10.
9. Add the 1400 ms window condition to the 58% to 72% figure, and note that it differs from the 59.3% inter-session figure.
10. Describe the M03 (11 of 41) and M12 (65 of 143) "usual approach" figures as the most common category, not a majority. State that the M12 categories overlap (167 > 143).
11. Align the M13 usual approach with the ledger row: drop "with an embedded processor" or source it.
12. Name the EEG handwriting studies behind the novelty sentence, or remove the sentence.
13. Separate the 1.7 mW same-hardware saving from the cross-system comparison with [3] and [4], and note the channel-count differences.
14. Remove the "(inference)" tag on the exact 23.5% calculation. Either give the 2005 drop (21.1 points, 21.7%) or drop the implied comparison.
15. Attribute the GPU-only accuracy and the non-closed-loop ITR to the authors' own statements. Fix the reference notes: "truncated to the first twelve" while six names are shown for [4] and [8]; no DOI for [4].

## Scores

- Procedure: 6/10. Strong claim table with locations, but many numbers carry no quote, and there are two chronology labels to fix and one circular state-of-the-art entry.
- Final text: 6/10. Clear positions and good handling of the within- vs. cross-session gap. The prior-work comparison misreads its own quoted evidence, and several counts are internally inconsistent.

The review separates within-session from inter-session accuracy and flags the missing on-device accuracy figure; both are the right central points.
