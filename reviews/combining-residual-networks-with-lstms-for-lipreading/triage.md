# Triage: combining-residual-networks-with-lstms-for-lipreading

Evaluation: combining-residual-networks-with-lstms-for-lipreading.eval.md (12 required fixes). Applied 11, rejected 1, unverified 0.

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | WAS was pretrained on BBC sentences (target Sec. 5.1, c7, c22); extra pretraining favours the comparator. The weakness is a single cross-system comparison with no run count. | Verdict sentence 4; claims-outrun bullet 1 |
| 2 | applied | SyncVSR trains the encoder to predict quantized audio tokens, four per frame (arxiv-2406.12233 Sec. 2; c30, c31). | Verdict sentence 5; M06 and M12 state of the art; slots M06/M12 sota cells; verdict.short |
| 3 | applied | The target has 3 of the 156 keys (audit dated counts). Counting basis set to keys everywhere (156 keys = 154 studies; 155 = 153), marked as upper bounds. The recurrent count (115) is not dated against 2017-03, so it was dropped from the text and table. | Verdict; M06; M03; Appendix header and entries; slots matched_tier |
| 4 | applied | The M06 front-end audit has 0 of 4 [concurrent] keys naming a ResNet and 103 of 149 [later]. The text states that the default descends from this paper and that "standard" rests only on the repetition rule. | Verdict sentences 2–3; M06 usual approach and verdict line; slots M06 field/note |
| 5 | applied | WAS uses a VGG-M ConvNet whose features feed an encoder LSTM (arxiv-1611.05358 Sec. 2.1; c28, c29). | M06 usual approach |
| 6 | applied | LipNet is [concurrent] (2016-11). The sentence now reads "Earlier and [concurrent] work had the parts" and credits the authors' own citation (§4.2, c27). | M06 body |
| 7 | applied | The paper gives no run count (t68). "One run" was replaced with "no run count or dispersion reported". | Verdict; M06; M12; slots M12 choice |
| 8 | applied | Narrowed the per-step pattern to require a loss term: 11 keys (target 3, prior 0, [concurrent] 0, [later] 8), down from 33. Word-boundary count marked as an upper bound with negated mentions included. | M03 usual approach; Appendix M03; M03 audit dated counts |
| 9 | applied | ISCA §5.1 has 74.2%, while arXiv v4 §5.1 has 76.2% (c18), matching WAS Table 8 (23.8% WER, c6). It is now stated as a misprint, and the author question was dropped. | Claims-outrun bullet 1; Questions |
| 10 | rejected | The wiki manifest for arxiv-2209.01383 records only arXiv v3, with no ICASSP venue or DOI, so [5] stays a preprint per the triage rule. Recorded in verification_status. | extra.json open_items |
| 11 | applied | The authors name singular/plural and tense pairs (target Sec. 3, c32) and discuss the errors (Sec. 5.3, t42). Table 5 has four inflection pairs among the ten rows (SPEND/SPENT, WANTS/WANTED, BENEFIT/BENEFITS twice); the evaluator's count of five was not adopted. | M12 body |
| 12 | applied | 79.6% is in Table 3 (t30). N4 and N5 add the two directions (t30, c23). The Table 3 top-10 anomaly (N5 96.3% < N4 97.4%; t29, t30) became an author question. | M03 body ("Tables 3 and 4"); M06 body; Questions |

The M12 usual approach changed from a front end to an evaluation protocol: 145 of 155 keys name no repeated-run statistic, and the 10 that do are all [later]. These counts were appended to the M12 audit as `usual_approach_<slug>` and `dated_pattern_counts_<slug>`; the published values were kept.
