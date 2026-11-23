# Triage: Soft Active EMG Interface for Machine Learning-Enabled Silent Speech Recognition

Date: 2026-11-23. Input: the fallback evaluation (claim table only, 13 required fixes). Each finding was checked against the cited passage of the source text, and against the PDF page images for values that the text layer does not carry (Supplementary Tables 1 and 3). One round. Result: 12 applied (6 correct, 6 partly correct), 1 rejected (wrong), 0 unverifiable.

| # | Finding | Verdict | Evidence | Where applied |
|---|---|---|---|---|
| 1 | Test split is 360, not 300 | Applied (partly correct) | The paper itself gives both figures: "exactly 12 samples per class" (12 x 30 = 360) and "the test set (N = 300)" (Results). So the review's 300 was the paper's own number, but the inconsistency was understated. The training-only augmentation statement (Methods) is now addressed: for S02 and S03, 12 unaugmented test trials per word are 40% of 30 raw trials, not 20%. | Where the claims outrun the evidence, bullet 2; Questions, bullet 1; notes t57; row evaluation_limits |
| 2 | Quote t50 in full; quotes for 1.000 and .916; credit the authors | Applied (partly correct) | Full t50 sentence: the authors read the gap as "test sets were representative and ... did not overfit". That is their claim, not the review's critique, which is that the split is easier than the folds. "Training accuracy reached 1.000 for all conditions" (Supp. Fig. 9). CV mean 0.916 and N = 1,800 for S02 and S03 confirmed in Supp. Table 3 (image). | Bullet 1 now states the authors' reading first; notes t50, t14, t12 |
| 3 | Base the M12 "behind" on [4] and [5], not typical practice | Applied (correct) | Tally: speaker-disjoint 65, random or k-fold 58, session-disjoint 44 of 143, overlapping. No split is a majority. | Verdict; M12 usual approach and verdict line; slots M12 field and note; row position_in_field |
| 4 | Quote "placement varies" (§ Discussion) | Applied (correct) | "noise and signal variability arising from electrode placement and hand movement" (Discussion), which the authors concede. | Verdict now reports it as the authors' concession; notes t26 |
| 5 | "Four dry fingertip electrodes" | Applied (partly correct) | The paper says "four electrodes placed from the thumb to the ring finger" (Discussion). Each is a bipolar pair (Results), so there are four channels. | Verdict: "dry electrodes on four fingertips (one channel each)"; notes t56; row expert_true_value |
| 6 | [3] uses silver paste, so it is not adhesive-free | Rejected (wrong) | The silver paste joins the textile electrodes to the earmuff during fabrication (Sec. V). The electrodes are dry and "do not have adhesive fixation" (Sec. III). | No change to the text; notes c15 reworded, c30 added |
| 7 | Quotes for "unseen day" and 63.9 µJ in [5] | Applied (correct) | "evaluating on an unseen recording day (excluded from training)" (Sec. I); "energy consumption of 63.9 µJ per" inference (Abstract). | notes c26, c27; claim rows 3, 10, 14 |
| 8 | Quote for "10 dry neck electrodes" in [2] | Applied (correct) | "With only the 10 neck electrodes, we achieve a mean accuracy of 92.7%" (Sec. 4.1). | notes c28; claim row 6 |
| 9 | Is [6]'s 98.7% from phase alone or fused with sEMG | Applied (partly correct) | Phase variations feed the CNN, and wet sEMG is only a correlation reference (Results; Methods). The review's "not sEMG" holds. Only the wording and quote were added. | M05 state of the art and slots M05 sota: "sEMG only as a reference"; notes c29 |
| 10 | [7]: strain sensor; "subject-independent"; re-attachment | Applied (partly correct) | The text already said "strain choker". Re-attachment is reported as "high inference accuracy was maintained", with no figure in that passage. | M12 state of the art: "not EMG", 5-fold CV named, re-attachment claim dropped; slots M12 sota; notes c31 |
| 11 | Quotes for "top three tuned" and the Conformer's 91.1% | Applied (correct) | Supp. Table 1 footnote (image): hyperparameter optimization "only for the top three channel combinations"; others used defaults. "Conformer and DNN models achieved classification accuracies of 91.1% and 97.2%" (Supp. Fig. 14). | Bullet 4 cites the footnote; notes t41 location, t55 |
| 12 | Quote the third-party triggering claim | Applied (correct) | "external attempts to trigger sensing by third-party attacks are prevented" (Results, Design for Intent-Driven SSR). | notes t58; claim table |
| 13 | [4] is an 8-class task; [5]'s 13.7-point drop | Applied (correct) | [4] and [5] both use 8 words or commands. The review's range uses [4]'s 23 and 14 points and [5]'s silent drop of 18.2 points, so the 13.7-point vocalized drop is not used. | Verdict and M12: "on 8-word tasks", "on 8 commands" |

Not adopted from the evaluator's field notes: the suggested older session-independent EMG works are not in the reading budget. The M12 verdict now rests on [4] and the ledger count.

## Gates after revision

- check_review: 0 FAIL, 1 WARN (10 papers read in full besides the target, over the budget of 8; unchanged from the first run, since the three reused topic tables list the papers read in earlier reviews).
- verify_quotes: 69 found, 0 missing, 20 unchecked (unstated or figure-only).
- audit_tally: 3 audits pass; the published tallies are restored exactly, and only read_fulltext entries are appended.
- Body: 6,967 characters. The claim table was regenerated and every mapping refilled. compact.md was regenerated.

## Open items

- The full independent evaluation is pending; this round used the claim-table fallback.
- The Supplementary Table 1 footnote and the Supplementary Table 3 values come from PDF images (figure-only, so they are not checked by verify_quotes).
