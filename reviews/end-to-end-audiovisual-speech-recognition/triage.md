# Triage of the evaluation (12 findings)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | SKILL.md verdict rule: `ahead` needs repetition across seeds, subjects or datasets; the paper has one dataset and no repeated runs (notes t47) and ties MFCC in clean audio (t26, t27). Minority status is a departure, not a reason for `standard`. | Verdict sentences 2–3; M06 closing verdict sentence (reason first); slots M06 note; verdict.short |
| 2 | applied | Recount of the 44-study audit by year: 2 studies dated before 2018-02 (arxiv-1611.05358, doi-10.1109-access.2017.2761539), both spectral only; 0 raw waveform; the other 17 raw-waveform matches are later (incl. arxiv-2102.06657). Related-work mentions cannot be separated by the pattern count, so flagged as upper bound. | Verdict; M06 Usual approach; Appendix; audit key dated_counts_<slug> |
| 3 | applied | arxiv-1811.01194 Table 8: AV2 intermediate 2.20% MCR is the best intermediate; caption: DEMAND noise, -10 dB to 20 dB; word boundaries used (notes c8, c15). | M06 fusion sentence |
| 4 | applied | §5: the MFCC network "is trained in the same way as the BGRU networks in section 4.3" (t74); §4.3 holds the babble augmentation (t7). | Question 4 dropped |
| 5 | applied | §1: the authors themselves cite [15, 16] and scope their claim to raw waveforms on a large in-the-wild database (t1, t60, t71). | "First end-to-end" bullet dropped |
| 6 | applied | c4: Ryumin et al. claim the highest LRW AVSR result known to them; the ledger is the basis. | Verdict and M06 State of the art: "in the ledger"; slots M06 sota |
| 7 | applied | Cross-paper comparison (c3 vs t26, t28) differs in recipe. | Same-group controlled result [later] Ma 2021 placed first; cross-paper numbers now "suggest" with "(inference)" |
| 8 | applied | arxiv-2406.10082 Sec. 4: "achieve 1.1% / 0.76% AVSR WER using LRS3 433h / LRS3+VoxCeleb2 1,759h"; arxiv-1911.04890 Sec. 4: "CI denotes the half width of the 95% confidence intervals". | notes c13, c14; claim rows 10 and 19; 1,759 h condition added to M06 State of the art |
| 9 | applied | §5: MFCC baseline "trained for longer using early stopping" (t74). | Verdict confound sentence now names representation, depth and training length |
| 10 | rejected | No LRW seed-variance figure in notes; the sentence is already marked "(inference)". | Kept; listed in verification_status |
| 11 | applied (partly) | Wiki manifest of arxiv-2102.06657 gives DOI 10.1109/ICASSP39728.2021.9413459 (not the evaluator's number); no DOI or pages for arxiv-1811.01194 in the wiki, so [5] stays with its arXiv id. Duplicate "[later]" in reference notes removed. | refs.json [3] DOI; reference notes |
| 12 | applied | No run count is stated (t47 unstated). | "no repeated runs reported" in Verdict and M12; slots M12 choice; en.limitations |

Counts: 11 applied (one partly), 1 rejected, 0 unverified.
