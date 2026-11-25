# Triage of the independent evaluation (2026-11-25)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | Brief rule on table counts; slot-fill totals (e.g. M05 7,329, M13 6,075) are not design counts. | slots.json: matched and n set to null for M01-M05, M08-M11, M13; audited slots show design counts (M06 82 of 142, M07 341 of 1,280, M12 18 of 134). |
| 2 | applied | Target §Methods describes the real-time computer and rtNSR (notes t77) and states "negligible latency" (t73). | M13 is now standard, with the system described; online accuracy and latency gaps are kept under M12 and in the claims section. |
| 3 | applied | The dialogue_context_prior regex over the population reproduces 36 unique studies; 7 are dated 2019 or earlier, and none of those besides the target has the design. | M07 audit: dialogue_context_inspection holds the regex and 36 items with a note each; the text says "inspected as snippets"; Appendix points to the audit. |
| 4 | applied | pmc-5495144-lmbci Sec. 2 (notes s1): speller priors come from the user's own previous selections. This is a linguistic prior on the same user's output, not a decoded partner utterance, so ahead stands. | M07 usual-approach line names it [5]; added to the M07 audit read_fulltext (prior) and the references. |
| 5 | applied | Target §Methods, Real-time decoding (t72, t74). | The Verdict reports the authors' offline disclosure and their argument, then says what is missing; the claims bullet is reworded. |
| 6 | applied | Target §Discussion (t76): hard restriction gave no improvement; the paper has no ablation separating restriction from weighting. | The Verdict states set restriction as an untested confound, not as fact; verdict.json updated. |
| 7 | applied | M12 audit: no online-accuracy hit is dated 2019 or earlier, and the regex misses Moses 2018. | "(upper bounds)" removed; "no reporting practice dominates"; the table field is "Online accuracy figure, all later"; Appendix and audit count_note added. |
| 8 | applied | M06 audit: 360 population, 355 with a recorded M06, 142 with model_family; deep_network 183, hmm_viterbi 142. | M06 usual-approach line and Appendix now use stated bases; deep networks 183 reported; the table uses 82 of 142. |
| 9 | no action | "Below the group's 2018 practice" is a one-paper comparison inside a standard verdict, not a behind. | – |
| 10 | applied in part | The repetition is across subjects only (one dataset, no seeds), which meets the ahead rule. | No text change; the seed question stays in Questions for the authors. |
| 11 | applied | Target §Discussion (t75, t76). | "did not help" becomes "restricting answers by the predicted question gave no improvement"; the visible-options sentence now reports the authors' "no evidence" and the proposed test; the M07 heading uses the table label "Lexicon and LM". |
| 12 | applied | Known-item recall 0.5 misses only the target's second wiki version (pmc-6667454-qa), a duplicate. | Recorded in extra.json open items; no text change needed. |
