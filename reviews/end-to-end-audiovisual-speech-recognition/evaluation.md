# Evaluator: a language model separate from the writer

Target review: `compact.md` for Petridis et al., "End-to-End Audiovisual Speech Recognition", ICASSP 2018, arXiv:1802.06424.
Date: 2026-11-25. Inputs: the evaluator brief, `compact.md` (review, references, claim table), and the source passages stored in `notes.json` for entries the claim table cites (t35, t7, t68, t74, c8-c12). No web check; outside knowledge that I could not locate is marked "unverified".

## Claim check (25 claims)

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | 18-layer ResNet on raw waveform, two BGRU layers (Verdict) | Claim row 1, §3.2 quote | correct | "1D" follows from the temporal kernel quote. |
| 2 | Streams joined by concatenation and a two-layer fusion BGRU (Verdict, M06) | notes t19 (§3.3) | correct | Claim row 1 quotes only the labelling sentence; t19 holds the concatenation. Insufficient quote in the table, correct in source. |
| 3 | Raw front end ties MFCC BGRU, 97.7% each (Verdict) | Claim row 3, Table 1 | correct | |
| 4 | Babble -5 to 20 dB in training and test (Verdict, M12) | t7, t25, t68 | correct | |
| 5 | "Significantly outperforms" has no test (Verdict) | t52, t40 | correct | Notes confirm no significance test. |
| 6 | MFCC baseline is a 2-layer BGRU trained longer (M06) | t74 | correct | |
| 7 | Authors concede "significantly higher" training effort (M06) | t35 quote, §5 | correct | Quote is in notes, not in claim row 10: insufficient quote in the table only. |
| 8 | 0.9 / 3.5 / 7.5 points over MFCC at 5 / 0 / -5 dB (M06) | t39 | correct | |
| 9 | 14.1-point AV gain at -5 dB; 0.3-point clean gain, 13% fewer errors (M12) | t38, t33 | correct | 2.3 -> 2.0 errors = 13% (inference) checks out. |
| 10 | Visual 82.0% vs 83.0% for landmark-ROI ResNet [13] (Claims section) | t28, t29, t42 | correct | |
| 11 | "State-of-the-art ... compared with itself" (Claims section) | t4, t73 | correct | |
| 12 | "First end-to-end": OuluVS system already raw images + spectrograms (Claims section) | t1, t71, t60 | correct but not the reviewer's finding | See finding 5. |
| 13 | Ryumin 2023: 98.76% LRW AV, log-Mel (M06 SOTA) | c1, c2, Table 9 | correct | |
| 14 | 38% fewer errors, 1.24 vs 2.0 (M06) | arithmetic | correct | (2.0-1.24)/2.0 = 0.38. |
| 15 | Ryumin audio-only 96.07%, visual 87.16% (M06) | c3, Table 9 | correct | |
| 16 | Ryumin 98.76% is the best LRW AV result today (M06 SOTA, Verdict) | outside knowledge | unverified | Ledger-best only; I cannot confirm no higher LRW AV accuracy exists. Wording "best LRW audio-visual result" should say "best in the ledger" as the reference entry does. |
| 17 | Whisper-Flamingo 0.76% LRS3 WER (M06 SOTA) | claim row 8: audit tally only | insufficient quote | No source quote in table; condition (clean, AVSR vs ASR, training data scale) unstated. Later LLM-based AVSR systems (2024-2025) report similar sub-1% LRS3 WER (unverified). |
| 18 | Ma 2021: log-Mel = raw, 4.3% WER audio-only LRS2 (M06) | c11 | correct | Condition clean, audio-only, Conformer; the quote itself does not name LRS2, the note does. |
| 19 | Ma 2021: raw leads by at most 7.5 points at -5 dB babble (M06) | c12 | correct | Coincides numerically with the target's 7.5; fine. |
| 20 | Stafylakis: late 1.90% vs intermediate 2.79% MCR, audio-only 6.90% (M06) | c8, Table 8 | correct number, selective comparison | See finding 3. |
| 21 | Stafylakis: train on 4 of 6 DEMAND categories, fixed noisy test files (M12) | c5, c6 | correct | |
| 22 | Makino 2019 gives 95% confidence intervals (M12) | claim row 17: audit tally only | insufficient quote | Plausible (unverified). |
| 23 | 44 LRW AV studies: 29 spectral, 18 raw; 349 AVSR: 182 vs 45 (M06 usual) | Appendix | correct as tallies | Not re-counted, per brief. |
| 24 | 183 / 128 / 33 of 349 (M12 usual) | Appendix | correct as tallies | |
| 25 | Ma et al. 2021 DOI 10.48550/arXiv.2102.06657 (References) | bibliography | wrong | That is the arXiv DataCite DOI; the ICASSP 2021 paper has an IEEE DOI (10.1109/ICASSP39728.2021.9414567, unverified from memory). |

## Findings (numbered, ordered by impact)

1. **M06 verdict rationale contradicts itself.** The Verdict says the processing "is standard: raw waveform is the minority audio input (18 against 29)". Being the minority design is an argument that the paper departs from the usual approach, not that it follows it. The M06 section ends with the real reason ("`ahead` needs repetition across seeds, subjects or datasets, which the paper lacks"). Fix: state the slot as a departure from the usual design (or whatever non-`ahead` label SKILL.md allows) and give the missing repetition as the reason it is not `ahead`; do not cite the minority count as evidence of "standard".

2. **Field counts are dominated by later work, and the verdict leans on them.** The LRW audio-visual tallies (44 studies, 18 raw waveform, 4 concatenation-plus-BGRU "this paper and three [later] ones") include studies published after 2018, with related-work mentions counted (upper bound). At publication the raw-waveform AVSR design on LRW was, by the review's own count, unprecedented among the 4 fusion matches. The review should say once that the 18/29 split is mostly post-2018 and therefore describes the field the paper helped create, not the field it entered (fairness, brief item 5).

3. **Fusion comparator is selective and condition-mismatched.** Stafylakis et al. Table 8 lists three intermediate-fusion variants (2.79, 2.20, 3.17% MCR); the review quotes only 2.79 against late 1.90. The best intermediate (2.20) should be the one compared. The test condition is also different from the target (DEMAND noise -10 to 20 dB, word boundaries used, per note c8), and the review does not state it, so "Fusion has no baseline" is supported but the implied size of the late-fusion advantage is not transferable. Fix: give 2.20 as the best intermediate and add "DEMAND, -10 to 20 dB, word boundaries".

4. **Question 4 is answered by the paper.** "Was the MFCC baseline trained with the same babble augmentation?" Note t74 quotes §5: the MFCC network "is trained in the same way as the BGRU networks in section 4.3", and §4.3 contains the babble augmentation (t7). Either drop the question or narrow it ("§5 says 'the same way as §4.3'; does that include the noise augmentation?").

5. **"First end-to-end" rebuttal presents the authors' own scoping as the review's finding.** The authors themselves cite [15, 16] as end-to-end AVSR from raw images and spectrograms (t60, t71) and restrict their claim to raw waveforms on large in-the-wild data (t1). The review's conclusion, "new are the waveform input and the dataset scale", is exactly the authors' claim. The bullet does not show the claim outrunning the evidence; drop it or reword as agreement.

6. **SOTA wording overstated for LRW.** The Verdict and M06 call 98.76% "the best LRW audio-visual result"; the reference list correctly says "best ... in the ledger". The text should carry the same qualifier, since ledger coverage is not proof of the field maximum (unverified whether a higher LRW AV result exists).

7. **Cross-paper inference stated more firmly than its evidence.** "The raw front end is not what separates the 2023 system" rests on comparing a 96.07% log-Mel audio ResNet in another paper, with a different training recipe, against 97.7% here. It is marked "(cross-paper, inference)", which is right, but the opening sentence states it as fact. Soften the first clause to match ("suggests"), or lead with the same-group controlled result [4], which is the stronger evidence the review already has.

8. **Claim table lacks source quotes for two comparator rows.** Row 8 (Whisper-Flamingo 0.76% LRS3 WER) and row 17 (Makino 95% CIs) say only "see audit tally". Both carry a SOTA line. Add the quote and location (and for row 8 the condition: clean LRS3 test, AVSR, training data).

9. **Strongest confound only partly named.** The MFCC-vs-raw noise margin changes at least three things at once: representation, depth (no convolutional front end) and training length (MFCC trained longer with early stopping). The review names the first two in the Verdict and the third only in M06. The Verdict sentence "so representation and depth change together" should add training schedule, which cuts the other way (the deeper model was trained for less time), so the confound is stated in full.

10. **Run-variability inference is reasonable but unanchored.** "The 14.1-point gain at -5 dB is too large to be run-to-run variation (inference)" gives no reference for the typical LRW seed spread. A one-clause anchor (any ledger study reporting LRW seed variance) would turn the inference into a supported statement; otherwise keep it as is.

11. **Bibliographic: wrong DOI for [4].** `10.48550/arXiv.2102.06657` is the arXiv DOI; the ICASSP 2021 version (pp. 7613-7617, cited) has an IEEE DOI. [5] (CVIU 2018) lacks its journal DOI and volume/pages (unverified from memory: vol. 176-177, pp. 22-32). The reference list also repeats "[later]" twice on entries 2-6 (cosmetic).

12. **Minor: "one run" is absence-based.** The claim table quotes the training sentence (t47) to support "one run"; that sentence does not state the number of runs. Acceptable as an absence claim, but say "no repeated runs reported" rather than "one run".

## Required fixes, ordered by impact

1. Rewrite the M06 verdict rationale (finding 1) and add the post-2018 caveat on the field tallies (finding 2).
2. Compare late fusion with the best intermediate variant (2.20%) and state the DEMAND / -10 to 20 dB / word-boundary condition (finding 3).
3. Drop or narrow question 4 (finding 4); drop or reword the "first end-to-end" bullet (finding 5).
4. Qualify "best LRW audio-visual result" as ledger-best (finding 6); soften the first clause of the cross-paper inference (finding 7).
5. Add source quotes for claim rows 8 and 17 (finding 8); add training length to the Verdict confound (finding 9).
6. Fix the [4] DOI and complete [5] bibliographic data (finding 11); "no repeated runs reported" (finding 12).

## Scores

- Procedure: 7/10. Target numbers, arithmetic and chronology labels all check out; two SOTA rows lack quotes, and one comparator is cherry-picked.
- Final text: 6/10. Clear positions and good controlled comparator [4], but the headline M06 verdict sentence argues against its own label, and two "claims outrun evidence" items (question 4, "first end-to-end") are weaker than presented.
