# Triage: LiRA review, independent evaluation (11 findings)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 (major) | applied | [2] Sec. 5 and Table 3: "In case, we use the pre-trained LRW model for initialisation the WER drops further to 37.9 %" (notes c21); target Sec. 4.2 qualifier "when no external labelled datasets are used" (t67); Table 2 has no 37.9 row. | Verdict; M03 table note; verdict.json |
| 2 (moderate) | applied | [5] Sec. 5: 51.3% is "training on each dataset with full supervision after unsupervised pre-training", Table 3 row CTC + KD / ASR / GT / ASR (c23); target Table 2 labels it "KD-seq2seq [3] Unsupervised" (t73). | M02 body |
| 3 (moderate) | applied | Crossref: 10.1109/ICASSP39728.2021.9414567 is "End-To-End Audio-Visual Speech Recognition with Conformers"; 10.1109/ICASSP39728.2021.9413459 is another paper. DOI 10.1109/ICASSP40776.2020.9054253 added to [5]. | refs.json, References, refs.bib |
| 4 (moderate) | applied | [10] Table 9: RAVEn Base, 433 h unlabelled, 223 h labelled, 32.1% (c24); LiRA in the same table 38.8%. | M03 State of the art line; slots M03 sota; audit state_of_the_art_<slug> |
| 5 (moderate) | applied | [6] Table 1: Transcription Alignment 93.1 against SyncVSR 93.2, called "trivial" (c25, c26); Table 4: LRS2 43.2 to 30.7 with the audio loss (c27); Table 1: Training Strategy 92.1 against Training Strategy + LiRA 92.3 (c28). | M02 State of the art line; M02 verdict sentence; M03 body (0.2-point later gain); What the field needs next (M02) narrowed to what is not yet done |
| 6 (moderate) | applied in part | The AV-PPC 84.8% protocol is not stated in the target; LiRA-Frozen is the best layer of Fig. 3 (t72). The 80.30% AV-PPC frozen figure was not checked against a source in the wiki, so the frozen-against-AV-PPC comparison was removed rather than replaced. | M03 body |
| 7 (minor) | applied | Crossref: ICPR 2020 proceedings published 2021-01-10, inside the [concurrent] window. | M03 usual approach (AV-PPC removed from priors), M03 body label, Appendix, audit |
| 8 (minor) | applied | arXiv 2104.05418 lists lip reading among its downstream tasks (contrastive); cvf-kim21-mabm (audio memory) is in the M02 candidates, no wiki text, classified by title. | Appendix concurrent counts (M02 4, M03 3); M02 body; audits |
| 9 (minor) | applied | Target Sec. 1 "particularly beneficial for smaller labelled datasets" (t70); Sec. 4.2 "hard to optimise without a good initialisation" (t71). | M03 body; Where the claims outrun the evidence, item 3 |
| 10 (minor) | applied | [2] Sec. 4 Language Model states the partitions (c22). The point kept: the LM uses external labelled transcripts. | M12 body; LM partition question removed |
| 11 (minor) | applied | Target Table 1 labels LiRA-FineTuned "Self-supervised"; Fig. 4b plots LiRA-Supervised at 36%. | Verdict ("every other self-supervised method"); Where the claims outrun the evidence, item 2 |

Verdicts unchanged: M02, M03 and M12 stay standard. The new evidence (SyncVSR's 93.2 against 93.1; 92.1 to 92.3; 37.9% omitted from Table 2) supports standard.
Not applied: the evaluator's optional points (Out of time, ACCV 2016 workshops, not in the wiki; DC-TCN 88.4% above 88.1%) were left out for length.
