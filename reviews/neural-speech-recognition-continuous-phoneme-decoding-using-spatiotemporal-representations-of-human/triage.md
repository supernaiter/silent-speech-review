# Triage of the independent evaluation

Evaluation: neural-speech-recognition-continuous-phoneme-decoding-using-spatiotemporal-representations-of-human.eval.md (12 required fixes). Each finding was checked against notes.json and the specific source passage.

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| H1 | applied | Abdelaziz et al. 2019 Table 1: NSR single-speaker PER 56.75 (SD 1.10), mixed 64.54; heard TIMIT/CRM, one subject, 3-state HMMs, biphone LM (s7, s8). Moses 2018 Sec. 3 (l1), Moses 2019 Abstract (l2) confirmed. The absence sentence was false. | M06 and M07 State of the art lines; M06 evidence (Moses 2018); table rows M06, M07; iPhoneme labelled attempted-speech intracortical, not like-for-like; Willett 2023 dropped |
| H2 | applied | Target Sec. 1 cites ref [10] (same group, heard multi-speaker); Abdelaziz 2019 calls its HMM system an enhancement of "our recently published framework" (s9). | Verdict (priority rests on "perceived" and "single-speaker", credited to the authors' own citations); "the real step" changed to open-vocabulary phoneme output; M06 evidence with inference label; "in the ledger" qualifier; Appendix same-group priors |
| H3 | applied | Sec. 2.2.3 grid includes L = 0; Table 4 chose L = 2 or 3 for every feature set (t83, t23). | Verdict, M07 evidence, What the field needs next (Gump PER at L = 0 and uniform prior) |
| H4 | applied | All reported evaluations use the 10 Gump folds (t26); HGW and Viterbi tuning used TIMIT only (t60, t22). | TIMIT tuning bullet removed; M12 states TIMIT is a separate tuning set |
| M1 | applied in part | Sec. 3.1.1: estimation PERs "primarily included ... for completeness" (t88); electrode selection uses speech/silence labels and one set serves all comparisons (t59). | Verdict names the estimation baseline as main confound; M07 adds confusion and posteriogram accuracy changes (Table 5, t43); new claims bullet; electrode overlap kept as a limitation on absolute PER (inference) |
| M2 | applied | Sec. 3.4 cross-speaker train/test in both directions (t93); Sec. 4 conclusion without a two-speaker caveat (t92). | M12 State of the art; claims bullet now the reviewer's point, "the authors note it" removed; field-needs item now held-out subjects and sessions |
| M3 | applied in part | Herff 2015 and Heger 2015 share authors and recordings: merged. Chang 2010 trains a heard-syllable classifier with in-loop selection (p9); Bouchard 2014 has an "acoustic feature decoding model"; Mesgarani and Chang 2012 reconstructs heard speech. All added; population 20; recounts in audits. | Verdict, M06/M07/M12 counts, Appendix, slots.json; usual-approach direction unchanged |
| M4 | applied | Sec. 4: Kellis and Mugler "did not perform continuous speech decoding" (t89); sub-phone/RNN (t84); reconstruction comparison (t90). | M06 usual approach ("The authors draw the closed-set contrast"); field-needs M06 credits the authors |
| M5 | applied | M06 audit: 12 of 20 have a recorded decoder route. | M06 usual approach and Verdict give the 12-route denominator; Appendix gives ledger-text counts for all 20 |
| M6 | applied | Rules require deciding conditions in SOTA cells. | Table rows M06, M07, M12 |
| L1 | applied | Process note in reference 1. | refs.json note now "Target." |
| L2 | applied | Sec. 2.2.2: only exactly matching sequences removed (t91). | M07 usual approach; table row M07 |

Verdict changes: none (M06, M07, M12 remain standard). Reads besides the target: 8 in this review's own audits (Herff 2015, Heger 2015, Pasley 2012, Chang 2010, Abdelaziz 2019, Moses 2018, Moses 2019, iPhoneme 2026); the read-budget warning comes from the reused M12 table.
