# Triage: A Convolutional Framework for Mapping Imagined Auditory MEG into Listened Brain Responses

Date: 2026-11-21. Each fix was checked against notes.json, the wiki source texts and the topic audits. Applied: 10 of 11 (6 correct, 4 partly correct); 1 unverifiable.

| # | Class | What was done |
|---|---|---|
| 1 | partly correct | Dropped "removes the motivation for the CNN". The evaluator's "different task" is wrong: [2] uses the same four-stimulus paradigm (Sec. 2.1 of [2], new entry r12). The RNN point is right: the Verdict now says the linear result contradicts the premise that linear mappings fail, while the RNN separates more strongly (LOSO t = 9.59 vs 5.63), which supports a nonlinear mapping but not the calibration layer. |
| 2 | correct | M06 state of the art now names the leave-one-subject-out column of Table 2 and the paired t-test (App. A.3 of [2]); "all six models" rests on Sec. 3.1 of [2]. New notes entries r10, r11. |
| 3 | partly correct | Named the [concurrent] hit (arXiv 2604.15374, fMRI visual imagery mapped into a decoder's conditioning space) and cited it. Read Martin et al. 2014 from the wiki as a deciding prior: the overt-trained ECoG decoder is aligned to the overt audio by time warping, not to neural responses, so the claim stands. Added to refs, audit read_fulltext, notes (p6, p7, q1). Marion et al. 2021 and Di Liberto et al. 2021 are not in the wiki; not named, logged in verification_status. |
| 4 | correct | 370 is the ledger-pattern count and 379 the design-count population once full-text hits are added (audit counts and usual_approach). The Appendix now states both; slots.json M03 matched set to 379 to match the text. |
| 5 | correct | 61.3% Top-10 tied to Armeni 2022 MEG (3 subjects), the full framework, and a 1024-sample retrieval set (Tables I and III of [8]). New notes entries s2, s3, s4; table cell updated. |
| 6 | correct | Verdict now gives §V-B for the calibration on held-out-subject data and the missing ablation, §V-A for the linear result, and Fig. 5 for the output being estimated listened MEG. |
| 7 | partly correct | The supervision is reported, but the rule pairing each imagined trial with a listened repeat is not (notes t64), so not reported stays. The M02 table note now names that missing detail. |
| 8 | correct | M12 now frames the pairing-only shuffle as the usual approach. The target departs from it by adding a channel shuffle, which weakens the null. The state of the art says no stronger null exists in this line. Table cell updated. |
| 9 | partly correct | Bound stated as p ≥ 5/1024 ≈ 0.0049 and "p ≪ 0.01" called loose rather than false. The evaluator's "test unit unconfirmed" is wrong: Sec. V-B states one matched true/null pair per held-out subject (new entry t75). |
| 10 | correct | Sec. III removes saturating or non-functioning channels without a count (new entry t74). The text now reports the 155 vs 157 gap as unexplained, and the row and M05 note match. |
| 11 | unverifiable | No peer-reviewed version is in the wiki. The wiki text is a later bioRxiv version with a different title, so the bioRxiv citation stays. Logged in verification_status. |

After the fixes, the gate passed with 0 FAIL and 0 WARN (body 6,997 characters). Quotes passed with 93 found and 0 missing. The claim table and compact text were regenerated, and the row was regenerated and corrected.
