# Triage: Lightweight Diffusion-based Framework for Online Imagined Speech Decoding in Aphasia

Date: 2026-11-23. Round 1 of the independent evaluation (7 required fixes). Source passages were opened only where a finding needed them (target Table I and §II-D.3, §III-B, abstract; Diff-E §3.5.1; viseme decoder §III-A and Table I).

Result: 4 correct, 2 partly correct, 1 wrong, 0 unverifiable. 6 of 7 applied.

| # | Finding | Verdict | Evidence | Where applied |
|---|---|---|---|---|
| 1 | M02 and M07: verdict `standard` contradicts the stated usual approach (text or audio targets; language model) | partly correct (applied) | The contradiction is real, but the proposed remedy (restate the usual approach as class labels / no language model) has no ledger count: both slots are filled in under 5% of papers (31 and 119 unique studies), so they give no field-practice count (slot notes). The verdict `standard` stays (inherited, no defect). | slots.json M02 and M07 `field` set to "Mostly not recorded" with the same slot-filled counts; 13-components table and JSON regenerated |
| 2 | M12: the class percentages force five trials per class; drop the conditional wording | correct (applied) | Table I: Clock 60%, Toilet 20%, Water 80%, resting state 40% top-1; each needs a class size that is a multiple of 5, and four non-empty classes summing to 20 trials gives 5 each. | M12 section, second sentence of the evidence paragraph; row fields `metrics`, `evidence`, `en.key_result` via fix_row.py |
| 3 | M12: per-class top-2 gains should read 20, 20, 60, 20 (Water, Clock, Toilet, Resting) | wrong (rejected) | Table I lists rows in the order Clock, Toilet, Water, Resting state (target text, Table I). Gains in that order are 20, 60, 20, 20, as the review states. The evaluator assumed a different row order. | not applied |
| 4 | M06: "Both lineage studies ablated" should be "two of the three", and say whether [4] ablated | correct (applied) | The lineage is three studies [2], [3], [4]. The viseme decoder [4] reports only comparisons with EEGNet, DeepConvNet and ShallowConvNet (Sec. III-A, Table I); no variant without the DDPM. New notes entry c18. | M06 evidence paragraph; row field `canon_before` via fix_row.py |
| 5 | Add claim-table quotes for the abstract's 65% / 70%, "stable online decoding" (§IV), "one forward pass", the context of "approximately 5 minutes", and the target's lack of a chance reference | correct (applied) | All five are in the target text: abstract sentence (new entry t64); §IV sentence (existing t63); §II-D.3 "single noise-conditioned forward pass" (t58 quote extended); §III-B "approximately 5 minutes, achieved 65 % top-1 and 70 %" (new entry t65); no "chance" term anywhere in the target text (existing unstated entry t49). No review wording needed to change. | notes.json (t58 revised; t64, t65 added); claims.md rows 7, 14, 15, 16, 21 |
| 6 | "What the field needs next", M03: Diff-E prompts are English, the target's words Korean; "include the three target words" is too strong | correct (applied) | Diff-E names clock, toilet and water in English and its participants had more than 15 years of English education (Sec. 3.5.1, new entry c19); the target task is Korean (§II-A.1, t3). | M03 item rewritten as cross-language pretraining |
| 7 | Component table: M13 called "Device and cost", section "Operation: online closed-loop decoding" | partly correct (applied) | The table uses the fixed slot name from the renderer; section headings name slot label plus topic. The mismatch is real for M13 only because the heading's slot label is "Operation". | slots.json M13 `name` set to "Operation"; table now reads "M13 Operation" |

Not required by the evaluator and not applied: shared authorship of [3] with the target; possible later diffusion-based imagined-speech decoders and earlier online covert-speech studies (noted in `verification_status.open_items`).

## Reruns

- verify_quotes: 74 found, 0 missing, 10 unchecked (unstated entries).
- render_review, build_refs, fill_row, then fix_row.py (25 fields re-applied; fix_row.py updated so `metrics`, `evidence`, `canon_before` and `en.key_result` match the revised text).
- check_review: 0 FAIL, 0 WARN; body 6,800 characters.
- audit_tally: 0 FAIL on all three audits. M06 diffusion-model-eeg-decoding and M13 online-imagined-speech-eeg keep the published tally exactly; only appended entries differ.
- claims.md regenerated (37 rows) and refilled with no "?" in any mapping; compact.md regenerated.
