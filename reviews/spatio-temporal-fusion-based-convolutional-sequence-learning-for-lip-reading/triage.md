# Triage of the independent evaluation (2026-11-28)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| H1 | applied | Target §4.3: "not comparable" refers to the ResNet-50 two-stage attempt with LRS3 in place of MV-LRS(w); the final ResNet-18 end-to-end model is called "comparable" (t96, t101, t103). Table 4: 863 against 1,637.4 video duration (unit unstated). | Bullet removed from "Where the claims outrun"; Verdict sentence rewritten (within 1.9 and 0.2 points with about half the training video, supporting "comparable", not a better sequence model). |
| H2 | applied | SyncVSR uses vq-wav2vec quantized acoustic tokens as targets (s6); whole-system result. | M06 spatial-reduction State of the art line; audit state_of_the_art metric. |
| M1 | applied | V2P Table 1 caption: "Standard deviations are bootstrap estimates" (c17). | M12 Usual approach (none of 5), slots M12 matched 5, Appendix (run spread 0, bootstrap intervals 1), M12 audit. |
| M2 | applied | Target §4.2 and Fig. 4 caption: widths >100 match accuracy in the "only test" setting; 20% faster training with local attention, width not given (t59, t60). | M06 sequence-model section. |
| M3 | applied | USR Table 6: 223 labelled + 1,759 unlabelled h (s2); Auto-AVSR 14.6% with LM, 3,448 h (s5). | M06 sequence-model State of the art line; audits. |
| M4 | applied | Target §4.2: two kernel-1 convolutions added before GAP for models without STFM (t102); TM-CTC and Conv-seq2seq GAP rows identical across Tables 1 and 2. | Last bullet of "Where the claims outrun". |
| A1 | applied | Stafylakis et al. 2018 Table 3: V2 AP 24.71% vs V4 FC 22.51% MCR (c15). | M06 spatial-reduction evidence; Verdict; M06 audit read_fulltext. |
| A2 / L4 | applied | Afouras et al. 2018 Table 1 caption: front-end training (2 weeks) excluded (c16). | M06 sequence-model evidence. |
| A3 | applied | Target §1 gives 22 days for [1] (t97); Table 4 TM-CTC 19 d, ours 7 d. | 12-day bullet. |
| L1 | applied | LinProVSR Table 2: GRID 24,750 train / 8,250 test (s7). | M12 State of the art line; audit metric. |
| L2 | applied in part | Crossref: title "Conformer is All You Need for Visual Speech Recognition", doi 10.1109/ICASSP48485.2024.10446532; data mined from public YouTube (s8). "No external LM" not found in the LP Conformer text, so not stated. | refs.json; M06 sequence-model line. |
| L3 | applied | Crossref: TPAMI 44(12), 8717-8727, 2022; CVIU 176-177, 22-32, doi 10.1016/j.cviu.2018.10.003. | refs.json. |
| L5 | applied | Target §4.1: random division, 255 test utterances per speaker. | M12 evidence ("LipNet's random split"). |
| L6a | applied | doi-10.1109-access.2017.2761539 is cross audio-visual matching, not a decoder. | tools/exclude_reading.json; population 514, prior 120, recurrent mentions 42, LRW mentions 17; all counts and audits rebuilt. |
| L6b | rejected | arXiv 1503.06699 is a classifier whose experiments the evaluator itself describes as including a VSR application; removing it on its title alone would be a title screen, not a reading-based exclusion. It is not among the 13 reduction-stating rows. | none |
| L6c | rejected | Bear's thesis (1710.01288) and 1710.01351 are separate documents, not versions of one paper; the merge list holds only true versions. | none |
| L6d | applied | The population includes AVSR decoders. | Appendix and plan label "lip-reading, VSR and AVSR decoders". |
| L7 | applied in part | Ref. 9 is not in the wiki; described by its title only (visual speaker authentication with random prompt texts), without claims about its branches. | Appendix. |
| L8 | not applicable | Wiki-side manifest DOI error; already in verification_status open items. | none |

Counts: 19 items; applied 15 (2 in part), rejected 2, not applicable 1, unverified part noted in L2. No verdict changes.
