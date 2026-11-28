# Triage of the independent evaluation (2026-11-28)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 (Medium) | applied | Crossref record for doi:10.1109/ICASSP.2019.8682868: created 2019-04-17, issued 2019-05, so prior. Afouras et al. §1.1 describe it as ASR-teacher distillation into an audio-visual student. The 0-of-76 count holds for video-input students, the audit's same-design boundary. M02 verdict kept as ahead, now stated for a video-only student. | Verdict sentence 2; M02 verdict line; ref [2] first_public 2019-04, labelled prior, "date unresolved" removed; Appendix; slots M02 note; audit counts_hearing-lips… li2019_outside_wiki |
| 2 (Medium) | applied | Target §1: "This is to our best knowledge the first attempt along this line" (notes t2). | Verdict sentence 1 |
| 3 (Medium) | applied | isca-kolossa12_avenh is "Inventory-Based Audio-Visual Speech Enhancement" (title, first page), an enhancement paper under the stated exclusion. Population 77 -> 76, forced-alignment hits 21 -> 20, training-target uses 13 -> 12 (8 visual stream, 4 audio-visual models). The remaining 12 pids were rechecked against their snippets. | Verdict; M02 Usual approach; Appendix; slots M02; audit counts_hearing-lips… and usual_approach_hearing-lips…; extra.json |
| 4 (Medium) | applied | The cell put the minority forced-alignment design forward as the usual approach and attached "pattern match 13" to the distillation count. | slots M02 field "Transcript only; forced-alignment targets; distillation 0 of 76", matched 12, n 76 |
| 5 (Medium) | applied | Ma et al. 2022, Suppl. S5: "The Mandarin language model is trained by combining the CMLR [8] and news2016zh" (notes c30). | M12 State of the art: LM condition added, and the gaps stated as mixing LM and data; ref [9] note |
| 6 (Low) | applied | USR Table 6 lists Auto-AVSR at 14.6% (3,448 labelled h, with LM) and USR at 15.4% (with LM) (notes c33, c20). | M12 State of the art now names both conditions; ref [8] note now reads "without an LM, 223 labelled hours"; slots M12 sota |
| 7 (Low) | applied | Ren Table 1 gives single values and no teacher sizes; the video-teacher advantage is 0.8 points (54.2 against 53.4). | M02 State of the art ("single values, teacher sizes not stated"); Verdict "about as useful"; audit SOTA metric |
| 8 (Low) | applied | Afouras Table 3 caption ("fine-tuning with a small fraction of the ground truth ones") and §4.1 (6-gram LibriSpeech LM) (notes c31, c32). | M02 [concurrent] sentence |
| 9 (Low) | applied | The speaker overlap follows from the random 7:1:2 split over eleven hosts [CSSMCM §3]; it is an inference. | slots M11 note |
| 10 (Low) | applied | The target's own reference list cites Hinton et al., Romero et al. (FitNets), Kim and Rush, Gupta et al. and Hou et al. as KD precedents (Related Work, notes t3). These are outside speech decoding. Claim row 35 now points to the M02 audit (known-item recall 4 of 4). | Appendix M02; claims.md row 35 |

Counts: 10 applied, 0 rejected, 0 unverified. No verdict changed; the M02 "ahead" verdict is now scoped to a video-only student.
