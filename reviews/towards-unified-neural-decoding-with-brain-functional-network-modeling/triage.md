# Triage: Towards Unified Neural Decoding with Brain Functional Network Modeling

Evaluation: a language model separate from the writer (9 required fixes; claim-check rows folded into them).

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | Full sentence (p. 10): accuracy above chance "even before the practice session, despite the absence of any subject-specific calibration or training"; the claim concerns the models, and both models were trained on data from the test participants (single-subject on own data, p. 10; multi-subject on all subjects, Methods p. 28). The objection stands; it now quotes the authors' wording ("no subject-specific calibration or training") and says both models were trained on the test participants' data. | Verdict sentence 3; claims-outrun bullet 1; notes t67 full quote; verdict.json position |
| 2 | applied | Du-IN Table 2: Brant 11.16-12.42%, BrainBERT 6.72-7.50% on 61 classes, well above 1/61 chance. "Barely exceeding chance" is MIBRAIN's own statement about its 23-class task (p. 8). | Verdict last sentence; M03 paragraph; verdict.json short and position |
| 3 | applied | Audit: 370 unique studies match in the ledger, 379 once full-text-only matches are added; the design counts are over 379. | M03 usual approach; Appendix M03 entry |
| 4 | applied | The authors themselves disclose that i and u are included alongside 21 initials (Discussion, p. 18). | Bullet removed from "Where the claims outrun the evidence" |
| 5 | applied | Notes t26, t30, t42 and t71 hold the quotes. | Claim table rows 38-40 added; row 1 maps t26 |
| 6 | applied | New notes entries: c15 and c16 (Brant 12.42, BrainBERT 7.50, Table 2), c17 (61-word task), c18 (Singh single transfer subject), t73 (fewer than three participants), t74 (single enrollment order). Channel selection on p. 24 and the experimental split on p. 28 are given as locations; whether test samples were excluded stays a question to the authors. | notes.json; claim table rows 3, 5, 6, 10 |
| 7 | rejected | The Population Transformer (arXiv 2406.03044) is not in the wiki (index 730b0b4), so it cannot be read or used under the brief. | - |
| 8 | rejected | The wiki holds Chen et al. only as bioRxiv preprints (pmc-10980022-satrans-decode, pmc-10980022-subjagn = bioRxiv v2); there is no peer-reviewed version. The PMC wiki ids were added to the reference's pid list. | refs.json pid list |
| 9 | rejected | The M09 slot covers presentation and confirmation shown to the user. During free practice the display showed "Correct" or the top three predictions (notes t57), so this is presentation, not an evaluation metric. | - |

Counts: applied 6, rejected 3, unverified 0.
