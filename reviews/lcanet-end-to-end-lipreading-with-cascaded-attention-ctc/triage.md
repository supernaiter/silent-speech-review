# Triage: LCANet (evaluation of 2026-11-28)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| C1 | applied | pdftotext -layout of the wiki PDF page 7 places LRSW 3.0 under WER %, CER and BLEU blank; the earlier reading came from column-collapsed pypdf text. Chung et al. Table 8 gives 3.0% GRID WER. | Verdict LRSW sentence rewritten (no comparator for CER, 2.9 vs 3.0 tie); verdict.json short and position; first outrun bullet rewritten with the authors' own LRS pretraining note (Sec. 4.D); question on LRSW CER removed; notes t22/t45 corrected |
| H1 | applied | aaai-38133-linprovsr Table 3: LinProVSR 0.99, CFLip 1.01 (LipFormer 1.45); Table 2: GRID 24,750 / 8,250, split type not named | M12 state-of-the-art line; M12 table cell; M06 line states the 255-per-speaker, no-LM protocol; notes l1-l3; ref added |
| H2 | applied | Slot step is GRID; LRS3 17.6% is a different corpus and data regime | LRS3 line and its reference removed |
| M1 | applied | Sec. 4.A: 255 test sentences from every speaker after a random split | M12 paragraph rewritten (speakers overlap) |
| M2 | applied | (4.8-3.0)/4.8 = 37.5%; 4.1-3.0 = 1.1 | Second outrun bullet; Verdict tie wording |
| M3 | applied | tools/seqobj_2018-03.json lists other neural systems among the 57 | "5 end-to-end sequence decoders"; slots.json M06 usual/field, n = 5, matched = 4; audit usual_approach_<slug> n 4 of population 5 |
| M4 | applied | LipNet text has no BLEU; Fig. 6 plots LipNet curves (Sec. 4.E); no plain CTC model in Table II | Verdict ("no in-house CTC-only or attention-only baseline"); new outrun bullet; author question. Superadditivity against the external LipNet row not stated, because that row is not an in-house baseline |
| L1 | applied | H-CTC vs AH-CTC measures attention before CTC | "The ablation does not test attention without CTC." |
| L2 | applied | recall_cascade.py cut is < 2018-09 | Verdict and Appendix say "before 2018-09"; Appendix names arxiv-1810.00108 ([concurrent] by month, joint loss) and arxiv-1809.02108; M06 paragraph cites the joint-loss lip-reading study |
| L3 | applied | arXiv:1803.05563v1 abstract read (attention within the CTC framework, 15 Mar 2018) | M06 usual-approach line, [concurrent]; ref added |
| L4 | applied | Sec. 4.C: comparator follows [43] (Hori 2017) | M06 paragraph: follows Hori, whose joint training builds on Kim |
| L5 | applied | Table II caption; Afouras abstract "the transformer is a sequence-to-sequence model" | claims rows for A-CTC and Afouras; notes t55, a2 |
| L6 | unverified | Venue not stated in the wiki text of arxiv-2403.16071 | Kept as arXiv preprint; verification_status |
| L7 | applied (partly) | Fig. 6 caption "#iteration" vs epochs in Sec. 4.E | Added to the convergence bullet; LRW-row absence and the dataset swap not added (space) |
