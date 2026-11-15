Evaluator: a language model separate from the writer

Date: 2026-11-15. Scope: the brief (`evaluator-brief.md`) and the compact review with its claim table only. No sources were opened and no search was run. "Known work" notes below come from the evaluator's own knowledge and are marked as such.

## Claim checks

| No | Claim (short) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper changes one component, M02: joint losses predicting pretrained audio and visual representations | Row 1, t3 | correct | The quote supports the description. "Changes one component" sits awkwardly with the review's M03 finding that recipe tuning and time masking carry as much gain (see fix 14). |
| 2 | Gain falls from 3.7 (LRS2, 380 h) to 1.5 (LRS3, 1,459 h) | Row 2/9, t86, t89, t92, t95, t99 | partly correct | 33.2−29.5=3.7 and 33.6−32.1=1.5 are right. No quote gives "380 h". The two figures come from different test sets (LRS2 vs LRS3) as well as different data sizes, so the drop cannot be credited to data scale alone. Table 5 also has an LRS3 column at 595 h, which would give a same-test-set comparison, but the review does not use it. |
| 3 | 12.5% and 4.7% relative | Row 9 | correct | 3.7/29.5=12.5%; 1.5/32.1=4.7%. |
| 4 | Authors concede the shrinking effect (S9.8) | Row 9, t99 | correct | The review credits the authors, which is fair. |
| 5 | 31.5% LRS3; 14.5 points behind 17.0% [5] [concurrent] | Rows 3, 7, 17; t21, t28 | correct | 31.5−17.0=14.5. The [concurrent] label fits (arXiv Jan 2022 against target Feb 2022). Small oddity: t28 cites the system as "[17]" and t30 as "[6]"; the reference numbering inside the target should be checked. |
| 6 | 13.9 points behind 17.6% [6] | Row 17, s1 | correct | 31.5−17.6=13.9. |
| 7 | [6] used ~2,500 h unlabelled video with pseudo-labels, "public labelled data" | Row 6, s1 | insufficient evidence | The quote omits the hour count ("hours of unlabelled data") and says nothing about public labelled data or pseudo-labels in place of a frozen teacher. |
| 8 | [6] reaches 23.7% with 30 h labels, "below the paper's 31.5% with 1,459 h" | Row 12 | insufficient evidence | The only quote is the target's t21. The 23.7 value comes from an audit note with no "30 h" condition. The comparison also leaves out the unlabelled data [6] uses, so 30 h against 1,459 h is not like for like. |
| 9 | Layer 6 placement | Row 5, t63 | correct | |
| 10 | LiRA 38.8% LRS2; ASR-is-all-you-need 51.3% / 59.8% | Row 8, p2, p3 | correct | Numbers match the quotes. |
| 11 | Initializes from supervised LRW and LRS models; hyperparameters tuned on LRS2 val | Row 11, t111, t65 | partly correct | The quotes support LRW initialization and LRS2-validation tuning. They do not support "LRS models". |
| 12 | Tuning + better LM move LRS3 44.9→39.1; aux losses + time masking add 3.3 to 35.8 | Row 13, t112, t91, t86 | insufficient evidence | This mixes Table S9 (baseline 44.9) with Table 5 (39.1). The t91 quote has no row label, so it is unclear which ablation gives 39.1. Nothing quoted says a better LM was involved. 39.1−35.8=3.3 is arithmetically right. |
| 13 | LRS2: no time masking 32.6, no audio aux 31.4, no visual aux 30.6 | Row 14, t87, t88, t90 | correct | Note that removing both aux losses (33.2) costs more than removing time masking (32.6), which weakens the Verdict's "as much as" framing. |
| 14 | At matched 595 h best run 35.1% beats CM-seq2seq 43.3% by 8.2 | Row 18, t19, t22, t23 | correct | |
| 15 | "...and it beats a 31,000-hour RNN-T at 33.6% by 2.1 points" | Row 18, t25, t26 | wrong as written | The sentence's subject is the 595 h best run (35.1%), which is worse than 33.6%. The 2.1-point gain belongs to the 1,459 h result (31.5%). |
| 16 | Abstract's "up to 21 times more data" leaves out the 90,000 h system | Row 19, t113, t30 | correct | 31,000/1,459 ≈ 21. The review should add that the authors disclose the 90,000 h system in the main text (t30), so this is an abstract-level framing issue and not something hidden. |
| 17 | Best-of-ten vs single numbers; mean–best gap up to 0.8 | Row 20, t80, t48 | correct | "Selection split not stated" is an absence claim that cannot be verified from the quotes. |
| 18 | It/Pt/Fr only comparator is retrained CM-seq2seq at 57.9–67.0% mean WER | Row 21, t110, t43, t46 | wrong / insufficient | t110 gives CM-seq2seq on Italian at 71.5±0.4 mean, which is outside the stated 57.9–67.0 range. The 57.9 and 67.0 figures may be other rows, possibly the paper's own model. No quote supports "retrained by the authors on the same data". |
| 19 | Mandarin and Spanish have published baselines, so the SOTA claim holds there | Verdict | no quote | No claim-table row supports this. |
| 20 | 60% ASR-disagreement filter; size and label noise change together | Row 22, t68 | correct (inference) | t5 is irrelevant to the claim. |
| 21 | Code crops 88 px with fixed normalization and sets a length penalty, neither in the paper | Row 23, t83, t84 | partly wrong | t83 shows that the paper does describe normalization by overall mean and variance. Neither code line is quoted, and t84 is about the LM, not a length penalty. Only the 88 px crop and the length penalty are possibly undisclosed. |
| 22 | Authors point to subject-independent VSR as future work | Row 24, t109 | mismatch | t109 says prior subject-independent work "has shown that this can be addressed". That cites prior work and does not state future work. t76 gives split sizes for an unnamed dataset, so "speaker overlap not reported" cannot be verified. |
| 23 | M02 usual approach: 104 studies, 20 cross-modal distillation, 5 audio-feature regression | Rows 4, 26, 27 | partly supported | Rows 26 and 27 give 104 and 20. The "5" is not visible in any Appendix row (row 27 is truncated). |
| 24 | M03 usual approach: self-supervised 31 of 75, paired audio 17 | Rows 10, 30 | correct per tally | |
| 25 | M12 usual approach: transcribed video 18 of 141 | Rows 15, 34 | correct per tally, wrong category | M12 is Evaluation, but its usual approach is given as a supervision kind. 18 of 141 (13%) is also weak support for "most common". |

### State of the art (evaluator's own knowledge, not checked against sources, confidence medium)
- LRS3 visual-only WERs below 17.0% exist before 2026: LP-Conformer, Chang et al., "Conformers are all you need for visual speech recognition", ICASSP 2024, 12.8% (large non-public YouTube data); SynthVSR, Liu et al., CVPR 2023, 16.9% (public plus synthetic data). The M12 "17.0% overall" state-of-the-art line is therefore outdated.
- Auto-AVSR, Ma et al., ICASSP 2023, 19.1% with about 3,448 h of public, automatically labelled data. It does not beat [6] at 17.6%, but it is the direct same-group successor and a natural reference for the "data scale" argument.

### Fairness
- [5] is labelled [concurrent] and [6] is labelled [later], and neither is treated as missed prior work. That is correct.
- The shrinking effect of the auxiliary losses is credited to the authors (S9.8). That is correct.
- The abstract point (claim 16) should acknowledge the authors' own disclosure in the text (t30).

## Required fixes (ordered by impact)

1. **M12 comparator sentence (claim 15):** split the sentence so that the 2.1-point gain over RNN-T [8] is attached to the 1,459 h result (31.5%), not to the 595 h best run (35.1%).
2. **Data-scale argument (Verdict, M02):** compare the effect of the auxiliary losses on the same test set (LRS3 at 595 h, Table 5, against LRS3 at 1,459 h, Table S26) instead of LRS2 against LRS3. Either quote a source for "380 h" or drop it. Soften "fades at the data scale the field has since adopted" until that comparison is made.
3. **It/Pt/Fr baseline (claim 18):** the stated range 57.9–67.0% conflicts with the quoted Italian CM-seq2seq mean of 71.5%. Correct which rows these numbers belong to, and add a quote showing the baseline was retrained by the authors.
4. **Mandarin/Spanish (Verdict):** add claim-table rows with the published baselines and their values, or remove "holds for Mandarin and Spanish".
5. **Recipe vs losses (Verdict, M03):** the "as much of the headline gain" claim combines Table S9 and Table 5 without a labelled row for 39.1 and without evidence for "better language model". Quote the row labels, or restate it as an LRS2 within-Table-5 comparison. Note that removing both auxiliary losses (33.2) costs more than removing time masking (32.6).
6. **State of the art for M02, M03 and M12:** for [6], add quotes for 23.7% at 30 h, for "public labelled" and for the hour count of unlabelled data. State the unlabelled data volume when comparing it to the paper's 1,459 h. Update the overall LRS3 state of the art (e.g., Chang et al. 2024, 12.8%; SynthVSR 2023, 16.9%) or limit the claim explicitly to "lowest in the paper's Table 2".
7. **Code claim (claim 21):** remove "fixed normalization ... not in the paper", because t83 describes it. Quote the code lines for the 88 px crop and the length penalty.
8. **Subject-independence bullet (claim 22):** t109 refers to prior work, not to future work. Rephrase it, and name the dataset for which speaker overlap is unreported.
9. **Component table, M08 and M11:** the verdict "not reported" contradicts the entries ("Characters", "Benchmark splits"). Use `standard` or explain.
10. **M12 usual approach:** it describes a supervision design, not an evaluation design. Restate it for evaluation (e.g., single-run test WER on the LRS3 test split), or move it to M02/M03.
11. **Initialization (claim 11):** add a quote for initialization from LRS models, or limit the claim to LRW.
12. **M02 usual approach count "5 regress audio features":** add it to the Appendix row or drop it.
13. **Abstract framing (claim 16):** add that the authors disclose the 90,000 h system in Sec. 1.5 (t30).
14. **Verdict opening:** "changes one component, M02" is in tension with the review's own M03 analysis. Say that the gains also depend on recipe and augmentation changes.

## Scores
- Procedure: 6/10. The claim table is mostly traceable and the arithmetic is right. Several conditions (hours, "public", "30 h", "retrained") have no quote, and the code claims are not quoted.
- Final text: 5/10. It has one wrong comparison sentence, one contradicted baseline range, one data-scale argument that compares across test sets, and an outdated LRS3 state of the art.
