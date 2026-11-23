# Triage: SilentWear (arXiv:2603.02847)

Date: 2026-11-23. Input: `<slug>.eval.md` (fallback evaluation, 15 required fixes). Source passages were opened only where a finding turned on a number, a quote or a bibliographic fact. One round; gates rerun afterwards.

Result: 14 of 15 applied (8 correct, 6 partly correct), 1 rejected (wrong), 0 unverifiable.

| # | Finding (short) | Classification | Verdict | Evidence | Where applied |
|---|---|---|---|---|---|
| 1 | "Superior to our prior solution" bullet misreads [2] | partly correct | applied | §V ties the claim to the cross-validated 84.8% / 77.5%; [2] reports 87% / 68% cross-validated for 8 classes on one subject with shuffled 5-fold (c2b, c3, c5), so the protocol mismatch stands and vocalized accuracy is in fact lower. The evaluator is right that leave-one-session-out (64% / 54% in [2], c2) favours the target (71.1% / 59.3%). | Where the claims outrun the evidence, bullet 2; notes c2b, t74b |
| 2 | M13 state of the art is the target itself | correct | applied | No read prior decodes on the body (c4, c7, c8, c10). | M13 State of the art line now names the lowest read raw-streaming figure (22.2 mW [2]); slots.json M13 sota and field; M13 audit value left as recorded, noted in verification_status |
| 3 | Unquoted numbers and conditions | partly correct | applied | Most values already had notes entries with quotes (t35, t59, t60, t17, t53, t55, c10, c13); the old claim table did not show them. Missing quotes were added from the sources: c11b-c11d (97.3%, 87.1%, seven channels, ten digits), c6b-c6d (wet mastoid reference, 11 words, 10 random 80/20 splits), c9b-c9c (silver paste, random 80/20 split), c13b (three seeds, 25 classes), c14b-c14c (scarf modality, five phrases), t13b, t74b. verify_quotes: 93 found, 0 missing. | notes.json; claims.md refilled with every mapping |
| 4 | M05 counts 16 + 7 > 21 | correct | applied | The M05 table note says a study can match several patterns and the patch count is an upper bound. | M05 Usual approach; Appendix M05 |
| 5 | Relabel [7] as [later]; single label for [2] | partly correct | applied in part | The fixed rule makes works within +-6 months [concurrent]: [7] (2026-09) and [2] (2025-09) both sit at 6 months, so both stay [concurrent]. The double label on [2] was real: its reference note said "Prior". | refs.json note for [2]; relabelling rejected and logged in verification_status |
| 6 | Confirm [8] is sEMG; class counts not comparable | correct | applied | The scarf senses muscle activity through the phase of a radio-frequency surface wave and uses surface EMG only as a validation reference (c14b). | M05 State of the art names the modality and gives the read sEMG figures; slots.json M05 sota; refs.json note for [8]; published M05 table unchanged |
| 7 | "Unseen day" may be an unseen session on the same day | wrong | rejected | §III-D: the held-out fold is "collected on a different day and after sensor repositioning" (t13b); §V: three sessions on three different days. | none (notes t13b added for the claim table) |
| 8 | "Conflicts" on 10 minutes is overstated; vocalized recovery is exactly 10 points | correct | applied | t46 (70% to 80%, 58% to 72%), t48, t49. | Where the claims outrun the evidence, bullet 3 |
| 9 | 58% to 72% needs the 1.4 s window | correct | applied | t46 is stated for the 1400 ms window. The 58% is the pre-adaptation point of the fine-tuning sequence, a different protocol from the 59.3% leave-one-session-out mean; not added to the text for length. | M03 State of the art |
| 10 | M03 and M12 counts are pluralities; M12 categories overlap | correct | applied | M03 usual n = 11 of 41; M12 inclusion rule counts a paper under every split it reports. | M03 and M12 Usual approach; Appendix M12 |
| 11 | "With an embedded processor" not in the audit row | correct | applied | The M13 usual approach is off-body decoding; the qualifier contradicted it. | M13 Usual approach |
| 12 | EEG handwriting studies unnamed | correct | applied | The audit counts them without names; the sentence was removed from the body. The priority claim is now tested only against the read priors. | M13 body; open item in verification_status |
| 13 | Separate the same-hardware saving from cross-system gaps | correct | applied | 22.2 mW (c4) against 20.5 mW (t61): 1.7 mW; [3] and [4] differ in front end, radio and sensor type (c6c, c7, c10). | M13 body |
| 14 | Drop "(inference)" on 23.5%; give the 2005 drop | partly correct | applied | The skill requires "(inference)" on reviewer calculations, so the tag stays. The 2005 drop (21.1 points, 21.7% relative) was added. | M03 body |
| 15 | Attribute GPU accuracy and non-closed-loop ITR to the authors; fix reference notes; DOI for [4] | partly correct | applied | §III-E "We run all experiments on a single GPU" (t71); §V leaves online validation to future work (t53). The missing on-device accuracy is a finding, not an author disclosure (t72). DOI 10.1038/s41467-025-68228-9 taken from the wiki copy of the published article. | M13 body; ITR bullet; refs.json notes for [4] and [8], DOI for [4] |

## Other changes

- Verdict: "reused unchanged" became "with its hardware reused" (t73 supports reuse only); verdict.json position updated to match.
- Length: the Random Forest sentence in the "superior" bullet and the duplicate question on on-device accuracy were cut to keep the body under 7,000 characters.
- Row: fill_row.py rerun, then fix_row.py; no legacy field contradicted the revised review, so fix_row.py was left unchanged.

## Gates after triage

- check_review.py: 0 FAIL, 1 WARN (11 papers read in full besides the target, budget 8; unchanged from the first pass, as the reused M05 and M12 tables carry their own read papers). Body 6,939 characters.
- verify_quotes.py: 93 found, 0 missing, 15 unchecked.
- audit_tally.py: 0 FAIL on all four audits. No audit file was rewritten; the M05 and M12 tables keep the published tally exactly and are only appended.
- claims.md: 42 rows, every row mapped, no "?" left. compact.md regenerated.
