# Evaluation: Lightweight Diffusion-based Framework for Online Imagined Speech Decoding in Aphasia

Date: 2026-11-23. Independent evaluator, claim table and review text only (no sources re-read).

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | One participant with aphasia, online decoding (Verdict) | Claim table row 1, t4 | correct | Quote supports single participant with chronic anomic aphasia. |
| 2 | Diff-E lineage classifies without reverse sampling [2], [3], [4] | Rows 2, 9; c1, c9, c8 | correct | All three quotes say inference uses only encoder and classifier (or averaged classifiers). |
| 3 | 14.11 M parameters, larger than Diff-E; about 20 times (inference) | Rows 2, 10; c2, t21 | correct | 14.11 M / 0.7 M = 20.2. |
| 4 | 112 of 167 offline; [5] 20 participants, two sessions, at least 3 weeks apart | Rows 3, 12, 13; c14, c12 | correct | Appendix tally accepted as given. |
| 5 | All row 65% / 70% does not follow from class rows | Row 18; t28-t32 | correct | Class rows: top-1 80/60/20/40, top-2 100/80/80/60. Each class gains at least 20 points top-1 to top-2, so the overall gain is at least 20; the All row shows 5. |
| 6 | Per-class top-2 gains "20, 60, 20 and 20" | Row 18; Table I row order Water, Clock, Toilet, Resting | wrong (order) | In Table I row order the gains are 20, 20, 60, 20 (Toilet is the 60-point class). The conclusion is unaffected. |
| 7 | With five trials per class: 50% top-1, 80% top-2 (inference) | Row 18 | correct | Arithmetic holds. The split is in fact forced: 20%, 40%, 60% and 80% each need a class size that is a multiple of 5, and four non-empty classes summing to 20 leaves 5 each. The conditional wording can become a plain statement. |
| 8 | 10 of 20 against 25% chance, one-sided binomial p about 0.014 (inference) | Row 19 | correct | P(X >= 10, n = 20, p = 0.25) is about 0.0139. |
| 9 | About 30 minutes calibration, about 20 s fit (§III-A) | Row 5; t9, t26 | correct | |
| 10 | Conditioned U-Net, one forward pass at noise level 0.5 (§II-D) | Row 7; t18, t58 | insufficient evidence | Quotes support the U-Net and tau = 0.5; no quote shows "one forward pass". |
| 11 | Diff-E 60.63%, 13 classes, 22 healthy participants, within-subject [2] | Row 8; c3, c5, c13, c6 | correct | |
| 12 | "Both lineage studies ablated": 60.63 to 46.59 [2]; 85.47 to 68.12 on spoken-speech EEG [3] | Row 11; c3, c4, c16, c7, c17 | correct numbers, wrong wording | The lineage is three studies ([2], [3], [4]); "both" implies two. Say two of the three, and state whether [4] ablated. |
| 13 | [5] 55.7% adaptive vs 52.3% static, 500-ms windows | Row 13; c10, c15 | correct | |
| 14 | Online evidence 20 trials, about 5 minutes (§III-B) | Row 14; t33, t27 | insufficient evidence | t27 "approximately 5 minutes" has no context showing what it measures. |
| 15 | 2 ms per 2-s window on Titan XP; 3 s feedback | Row 15; t22, t11 | correct | |
| 16 | "Stable online decoding" (§IV) rests on one session | Row 15 | insufficient evidence | No quote for the phrase "stable online decoding" in §IV. |
| 17 | 95 of 167 no chance term, 63 state one; "the paper follows the majority" | Row 16 | insufficient evidence | Tally accepted. No quote shows the target lacks a chance reference. |
| 18 | [5] scores against a stated 50% chance; effect in 15 of 20 | Row 17; c11, c10 | correct | |
| 19 | Authors concede one participant, calibration, four classes (§III-C) | Row 20; t41-t43 | correct | |
| 20 | Abstract's 65% / 70% | Row 20 | insufficient evidence | Only the Table I All row (t28) and §I "over 60%" (t34) are quoted; no abstract quote. |
| 21 | Stop rule: training accuracy > 75% or validation > 40% | Row 21; t25 | correct | |
| 22 | M03: Diff-E dataset's 13 classes include the three target words | Row 22; c5 | insufficient evidence | c5 lists "clock", "toilet", "water" in English; the target task is Korean-language (t3). No quote establishes that the two datasets use the same language or prompts, so "include the three target words" is stronger than the evidence. |
| 23 | M02 verdict standard: cue class labels vs usual "Text or audio targets" | Component table | wrong (internal) | The paper's design differs from the stated usual approach, yet the verdict is standard. |
| 24 | M07 verdict standard: no language model vs usual "Language model" | Component table | wrong (internal) | Same inconsistency as M02. |
| 25 | M13 label | Component table vs section heading | wrong (internal) | Table calls M13 "Device and cost"; the section calls it "Operation: online closed-loop decoding". |

## Usual approach and state of the art

- M06: the Diff-E lineage as the usual diffusion-in-decoder design is plausible given the tally. Diff-E (2023) as state of the art for imagined-speech EEG is acceptable; [3] reports higher but on spoken-speech EEG, which the review notes. Later diffusion-based imagined-speech EEG decoders may exist; none located here (unverified).
- M13: Wu et al. (2024) serves as a design benchmark (multi-session, stated chance) rather than a best-performing online system, and the review says the gap is not measurable. Earlier online covert-speech EEG work exists (for example, online yes/no covert speech classification, Sereshkeh et al., around 2017); year and values unverified, so not a required fix.
- M12: Wu et al. as a reference for stated chance is fair.

## Central claim, fairness, novelty, verdicts

- Strongest confound: no baseline or ablation, and 20 online trials from one participant. The review handles both (Verdict, M06, M13) and correctly notes the target's 65% is not comparable with Diff-E's 60.63% (different classes, cohort, offline vs online).
- Positions are backed by section locations, citations or the Appendix. The M12 All-row argument is the strongest point and is correct; it can be stated more plainly (claim 7).
- Fairness: [3] and [4] predate the target by more than 6 months; no later work is treated as prior. [3] shares all three authors with the target, which the review could note when it says the design is "inherited". The limitations the authors concede are credited to them (§III-C).
- No "first / only" or "none of the N" claims. No `ahead` verdicts. The two `not reported` verdicts (M10, M12) are consistent with the text.

## Required fixes (ordered by impact)

1. M02 and M07 rows: the verdict `standard` contradicts the stated usual approach (text or audio targets; language model). Either restate the usual approach for few-class imagined-speech classification (class labels; no language model) or change the verdict.
2. M12: state plainly that the class percentages force five trials per class, so the class rows give 50% top-1 and 80% top-2 (inference), and drop the conditional "with five trials per class".
3. M12: correct the order of per-class top-2 gains to 20, 20, 60 and 20 (Water, Clock, Toilet, Resting).
4. M06: replace "Both lineage studies ablated" with "Two of the three lineage studies ablated" and say whether [4] did.
5. Add claim-table quotes for: the abstract's 65% / 70%, "stable online decoding" in §IV, "one forward pass", the context of "approximately 5 minutes", and the absence of a chance reference in the target (M12 "follows the majority"); otherwise soften those statements.
6. "What the field needs next", M03: qualify "include the three target words"; the Diff-E prompts are English words and the target task is Korean, so same-word overlap is not shown.
7. Component table: rename M13 consistently with its section ("Operation: online closed-loop decoding").

## Scores

- Procedure: 8/10
- Final text: 7/10

The central finding (the Table I All row cannot follow from its class rows) is correct and well argued, and the parameter and binomial arithmetic checks out.
