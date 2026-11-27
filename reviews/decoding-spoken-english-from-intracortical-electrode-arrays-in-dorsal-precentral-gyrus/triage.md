# Triage: decoding-spoken-english-from-intracortical-electrode-arrays-in-dorsal-precentral-gyrus

Evaluation of 2026-11-27 (15 required fixes). Each finding checked against the target text and, where needed, the named prior.

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| H1 | applied | Sec. 2.7: logistic regression "in a leave-one-out cross-validation setup" (notes t66); Sec. 2.8: RNN folds over phoneme utterances (t50); Sec. 3.2: the 420-word dictionary lets longer windows exploit adjacent phonemes (t67). The original wording ("utterance-level folds") was wrong. | Verdict sentence 4 restated, with the Sec. 3.2 concession credited; claims bullet now "Overlapping windows", Sec. 2.7; Questions bullet 1 |
| H2 | applied | Appendix mention counts include pre-onset windows (5) and a condition-invariant signal (1); Anumanchipalli 2019 tested on silently mimed speech against auditory feedback (c33, quote verified). Absence restricted to "contamination test or artifact removal, 0 of 20". | Verdict sentence 3; M12 usual approach; Appendix M12; audit read_fulltext; reference added. Verdict unchanged (standard). |
| M1 | applied | Sec. 2.2: 256 plus "the remaining 64 words" = 320 (t68); Sec. 3.2: 232 plus 80 = 312 (t62). | Inconsistencies bullet |
| M2 | applied | Sec. 4.1 "ballpark estimates" (t38); Mugler hand-labelled onsets (c31), target audio-derived onsets (t69); comparator is Mugler's best subject (c10, c11). | M06: "closest matched test", caveat and onset difference added |
| M3 | applied | M06 prior_tally: small unit subset 12, full inventory 8, deep network 8 mentions over 20 decoders with full text. | M06 usual approach; table cells now give "of 20" and "mention"; slots matched set to null (mention counts, not design counts) |
| M4 | applied | Sec. 4 "novel use of a decontamination procedure" (t70); Sec. 1 "little prior attention" (t71); LRR concession is Sec. 3.5 (t72). | M12 usual approach paragraph; claim-table row for the Peterson line now quotes the Sec. 3.5 sentence |
| L1 | applied | Headings: "Decoding English phonemes using neural population activity" (Sec. 3.2) holds both 36.8% and 33.4%. | Inconsistencies bullet; claim table |
| L2 | applied | 6% exceeds uniform 2.6%, so it is conservative. | Chance bullet removed from claims; kept as a question |
| L3 | applied | DenseNet re-test covers Subjects A–C (c27); 54 patients is the denoising application (c23). | M12 state of the art line; slots sota cell; audit metric |
| L4 | applied | Sec. 3.5: centred window 54.9% (t73) against pre-voice 34.8% (t25). | M12 paragraph, with the note that the window moves |
| L5 | applied | No matched test in T11; 11.22% is the 39-class HLFP value (t12). | M06 paragraph |
| L6 | applied | Livezey used deep networks, not an RNN. | M06: "after deep networks [Livezey]" |
| L7 | applied | Headline 29.3% is leave-one-out (deterministic); sweeps report s.d. (t56). | Variability bullet: no interval, no repeated RNN runs |
| L8 | applied | Kellis 2010 (doi-10.1088-1741-2560-7-5-056007 / pmc-2970568-lfpwords) is a prior spoken-word decoder cited by the target; Herff 2015 sibling doi-10.3389-fnins.2015.00217 merged. Recount: 29 decoders, 20 with full text; mention counts unchanged (Kellis has no hits). | Appendix; both audits' prior tallies; reference added |
| L9 | applied | Process wording in published text. | Herff reference note shortened; Appendix "from the published table" removed |

Counts: 15 applied, 0 rejected, 0 unverified. Verdicts unchanged (M06 standard, M12 standard). Herff 2015 leave-one-phrase-out (optional suggestion in H1) not added; noted in verification_status.
