# Triage: Deep Lip Reading (arxiv-1806.06053), round 1

Source: deep-lip-reading-a-comparison-of-models-and-an-online-application.eval.md (25 claims: 17 correct, 6 wrong, 2 insufficient evidence; 16 fixes).

| # | applied/rejected/unverified | Evidence | Where applied |
|---|---|---|---|
| 1 (rows 11) BL vs FC-10 rebuttal | applied | Target Sec. 3.3: "We suspect that this is in part due to the CTC loss having a local nature" (t97). The rebuttal misread the authors. | M06 body: the rebuttal is replaced by the authors' hedge, and the review notes that no attention-decoded BL tests it. |
| 2 (rows 13, 19) M13 count and basis | applied, with a corrected count | The audit population has 4 prior decoders. On reading, the ICPhS 2011 Cai paper also reports a real-time figure (Sec. 4.4, "only about 0.90t seconds", c25), so the count at the target's time is 2 of 4, not the evaluator's 1 of 4. Both are Cai et al. 2011 on one system. Ma's delay is algorithmic (c24). The target's final online output equals the offline one (t94). | M13 usual approach; slots.json M13 (n=4, matched=2, field and note); M13 audit (usual_approach time-scoped, counts.measured prior 2 / later 4 / total 6, note); Appendix M13 line; Verdict; "Not reported" now rests on missing partial-hypothesis accuracy, delay in ms and beam-search cost. |
| 3 (rows 3, 9) architecture confound, CER | applied | TPAMI Table 2: TM-CTC 54.7% and TM-seq2seq 48.3%, both with the external LM (c19, c4). Target Table 1 CER: 33.9/34.0 (T2), 35.3/38.6 (greedy) (t24, t32, t23, t31). | M06 body; Verdict; slots M06 note; next-steps M06 bullet ("on one encoder"). |
| 4 (row 24) baseline data confound | applied | Target Sec. 3.1: "We also make use of the MV-LRS dataset used in [6]" (t100), against Auto-AVSR Table 3 (c12). | "Where the claims outrun the evidence", bullet 2, recast as unresolved; Verdict; slots M12 note. |
| 5 (row 8) "for the first time" | applied | Target Sec. 1 (t1): the phrase is about adapting MT and ASR architectures. | M06 body: the phrase is attributed correctly, and the CTC-versus-attention 0-prior is stated as the ledger's finding. |
| 6 (row 3) 5-point threshold | applied | No source gives run-to-run spread (t80). | Verdict: the threshold is dropped. |
| 7 (row 2) MV-WAS, Stafylakis back end | applied | Target Sec. 1.1, ref. 15 (t96); Sec. 3.2, 2-layer temporal convolution (t98). | M06 usual approach. |
| 8 (row 4) "over 20" in the Verdict | applied | Abstract and Sec. 3.3 say "percent"; 19.2/70.4 = 27% relative with T1. | Verdict; M12 body ("as relative change with both"). |
| 9 (rows 10, 22) TM's T1 has no external LM | applied | arXiv App. A.3: α=0.0, W=5 (t62); Table 1 caption. | M07 body. |
| 10 (row 17) Table 5 | applied | arXiv Table 5 caption: one utterance from the start and from frame 55 (t99). | M13 body. |
| 11 (row 16) 25 fps | applied | TPAMI Sec. 3.1, "sampled at 25 fps (40 ms per frame)" (c20). | M13 body, cited to [7]; extra.json open item updated. |
| 12 (rows 14, 18, 20) conditions | applied | Cai: Julius, CPU/audio time (c23). Ma: LRS3 only, 438 h (c16), computed delay (c24). Sterpu: 12 viseme clusters (c21), own online claim (c22). TCD-TIMIT is not named in the text, to fit the length. | M13 usual approach, state of the art and body. |
| 13 arXiv-only locators | applied | The ISCA text has no appendix. | M07 ("arXiv Table 3", "arXiv App. A.3/A.4"); M13 ("arXiv Table 5"); notes loc suffixes. The question citing App. A.4 was removed for length. |
| 14 (row 1) population label | applied | tools/excl.json and all.log: the prior list includes phrase and viseme classifiers and ultrasound-plus-lip systems. | Appendix setting line; "sentence-level" is dropped in the Verdict and M06; extra.json open item. |
| 15 reference [10] (Sterpu) venue and "?." | unverified / rejected | The wiki text and registration give no ICIP venue or DOI, so the arXiv locator stays (extra.json open item). The "?." comes from the shared build_refs formatting of a title that ends in "?"; changing the title would misquote it, and common code is out of scope. | not applied |
| 16 Appendix recall wording, hybrid exclusions | applied | M06 ctc-vs-attention audit: known-item recall missed only isca-afouras18b-deeplip; LCANet is excluded as a cascaded single model. | Appendix M06 ctc-vs-attention line. |
| row 5 (TPAMI also credits 70.4% to WAS) | not applied | Optional and correct (c5), but omitted to keep the body within 7,000 characters. | none |

Cuts made to stay within 7,000 body characters:
- The LRS3 sentence, and with it the LRS3 reference, so there are now 9 references.
- The FC-15 3.4/3.5-day bullet.
- The WLAS on-line extension sentence.
- "preliminary" (Sec. 5).
- The duplicate Auto-AVSR MV-WAS clause in M12.
- Two questions.

Verdicts: no change. M13 stays not_reported, now on the basis of missing partial-hypothesis accuracy, delay in ms and beam-search timing.

Gates after triage:
- check_review: 0 FAIL, 1 WARN (read budget, 24 papers, all from reused tables). Body is 6,994 characters.
- verify_quotes: 103 found, 0 missing.
- audit_tally: all 5 audits exit 0.
- claims.md (60 claims) and compact.md have been regenerated. snapshot_draft.py was not rerun.
