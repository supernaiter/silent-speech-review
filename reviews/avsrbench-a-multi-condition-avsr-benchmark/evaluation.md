# Independent evaluation: AVSRBench (arXiv:2609.10366)

Date: 2026-11-22. Fallback evaluator (claim table only). Input: the compact review with its claim table. No sources were opened; every check below is quote against claim. Ledger tallies (rows 4, 10, 26-37) are outside this check.

## Claim checks

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Three released checkpoints, zero-shot, three input modes, six corpora (Verdict) | Row 1, t1 | insufficient evidence | Quote says "six conditions", not six corpora; "released" and "zero-shot" are not in the quote. LombardGrid frontal/profile may be one corpus. |
| 2 | WildVSR: Auto-AVSR 19.1 to 38.6 WER (Verdict, M12) | Rows 2, 6, c1, c2 | correct | Both numbers in c1 and the 3448h row of c2. |
| 3 | Concurrent tests on conversational video [3] and a matched unseen set over five runs [4] (Verdict) | Row 2, c7, c6 | correct | Five runs stated in c6. |
| 4 | Auto-AVSR VO WER above 100% even on Easy clips; "collapse lies in the video channel, not in short turns" (Verdict) | Row 3, t61 | correct number / judgment too strong | 105.35 (Easy VO) supports >100%. But Hard VO is 126.95, 21.6 points worse, so short turns do add error. "not in short turns" should be "not only in short turns". Column headers are not in the quote. |
| 5 | LLM-decoder blame for Llama-AVSR rests on one run (Verdict) | Claim table | insufficient evidence | No quote or location shows the authors attributing the failure to the LLM decoder. |
| 6 | [4]: Auto-AVSR 0.95% AV on LRS3 to 14.0 ± 0.3% on matched unseen set (M12 SOTA) | Row 5, c4, c6 | partly correct | Numbers present; that they are audio-visual WER is not in the quote. [4] shares an author (Harte) with the target, so it is not an independent group; a harder test set is a benchmark result, not "state of the art" in the usual sense. |
| 7 | LombardGrid: 64.88 frontal, 92.50 profile VO (M12) | Row 7, t37 | correct | |
| 8 | [5]: 25.00 / 39.45 for a model trained on Lombard GRID, unseen speakers | Row 7, c12 | insufficient evidence | c12 has three columns (25.00 / 27.84 / 27.66); which one is the Lombard-trained, unseen-speaker, visual-only model is not in the quote. |
| 9 | Profile penalty 1.43 vs 1.58 times, "so the zero-shot gap is domain, not pose" | Row 8 | arithmetic correct / judgment too strong | 92.50/64.88 = 1.43, 39.45/25.00 = 1.58. In absolute terms the profile penalty is 27.62 vs 14.45 points, so pose costs the zero-shot model nearly twice as much. A ratio alone cannot assign the gap to domain rather than pose. |
| 10 | RR-AV 113.20 to 110.07 when doubling data (Table XI) | Row 9, t64, t58 | insufficient evidence | 110.07 matches Table IX (t58); 113.20 is not in any quote (t64 is only the legend). |
| 11 | WildVSR 49.3 to 38.6, 21.7% relative | Row 9, c2 | correct | (49.3-38.6)/49.3 = 21.7%. |
| 12 | No seeds, repeated runs or intervals (Sec. III) | Claim table | insufficient evidence | Absence claim; plausible, no quote possible. |
| 13 | RR-AV uses corrected transcripts on individual streams and keeps every turn, split at 2 s (M11) | Row 11, t11, t16 | partly correct | Individual stream and 2 s split supported. "Corrected transcripts" and "keeps every turn" are not in any quote. |
| 14 | LRS-VoxMM: Auto-AVSR 11.03% AV and 55.15% VO (M11 SOTA) | Row 12, c7 | wrong / no quote | 55.15 appears in no quote. c7 reads "0.93 8.91 / 11.03"; the column meaning is not quoted. |
| 15 | AV beats AO by 2.12 points, 16.1% relative, on LRS-VoxMM | Row 13, c7 | contradiction | 11.03 - 8.91 = 2.12, which would make 8.91 the AV value, against row 14 (11.03 = AV). 16.1% relative only works if AO = 13.15, a value in no quote. In c8 the review reads the value after the slash (70.71) as Llama-AVSR visual-only, but reads the same slot for Auto-AVSR (11.03) as audio-visual. The column mapping is inconsistent. |
| 16 | RR-AV: AV 0.99 worse than AO (26.39 vs 25.40) | Row 13, t58 | correct | |
| 17 | Easy clips 15.9 words, 105.35% VO, about twice LRS-VoxMM | Row 14, t61, t65 | partly correct | 15.9 and 105.35 quoted; "twice" depends on the unquoted 55.15. |
| 18 | [6]: transmission alone pushes Auto-AVSR VO to 90.26% on Zoom-transmitted LRS3 | Row 15, c14 | insufficient evidence | Quote gives no model, modality, corpus or clean baseline. In the quote, Zoom (90.26) is lower than the comparison condition (92.08), so "pushes ... to" needs the untransmitted baseline. |
| 19 | [6] "absent from the authors' explanations" | Row 15, refs | fairness issue | [6] (arXiv 2603) appeared about six months before the target (2609). Under the brief's rule the authors may not have read it, so its absence is not a fault. |
| 20 | Hard boundary below 2 s in text, at most 2.0 s in code | Row 16, t16 | insufficient evidence | Text supported; no code line is quoted. Affects only clips of exactly 2.0 s. |
| 21 | Llama-AVSR 311.48% VO on RR-AV, 70.71% on LRS-VoxMM; Table X omits it | Row 17, t60, c8, t63 | partly correct | 311.48 and the omission are quoted. 70.71 as visual-only depends on the unresolved column mapping (row 15). |
| 22 | GRID AV 8.90 worse, LombardGrid AV 2.29 better | Row 18, t31, t34 | correct | 21.47 vs 12.57; 11.73 vs 14.02. |
| 23 | Lombard gain 16.3% relative for one model; AV-HuBERT +0.40, Llama-AVSR -2.79 | Row 19 | correct | 2.29/14.02 = 16.3%. The authors' phrase "helps mainly under Lombard speech" has no location. |
| 24 | Prose 45.57% vs Table VIII 43.15% | Row 20, t100 | insufficient evidence | 45.57 quoted; 43.15 not quoted. |
| 25 | GPU memory 17.91 vs 2.29 GB; latency not measured | Row 21, t73, t87 | correct | The authors also cite "slow autoregressive generation" (t87), a qualitative latency argument with no measurement. |

## Section-level checks

- **Usual approach.** LRS3 as a test set in 33 of 75 cross-corpus studies, and corrected transcripts in 16 of 59 conversational studies, are plausible as typical designs. Counts not audited.
- **State of the art.** Both SOTA lines cite concurrent benchmark results, not the best method. That is acceptable for an evaluation or reference component, but the M11 line rests on numbers whose columns are unresolved (rows 14-15).
- **Central claim and confound.** The review names the main confound: each condition changes style, vocabulary, transmission, pose and preprocessing at once. It also notes possible LRS3 speaker overlap. It does not handle absolute vs relative change in the pose argument (row 9). Two positions go beyond their evidence: "not in short turns" and "domain, not pose".
- **Fairness.** [6] is criticized as an omission although it falls within six months of the target (row 19). [3] and [4] are correctly labelled concurrent. [4] shares an author with the target, which the review does not say.
- **Absence and novelty.** "testing released checkpoints outside LRS3 dates from WildVSR [2]" holds for publicly released checkpoints. Cross-corpus zero-shot VSR testing is older: Shillingford et al., "Large-Scale Visual Speech Recognition", 2018, arXiv:1807.05162, evaluated its YouTube-trained model on LRS3 without training on it.
- **Verdicts.** No slot is `ahead`. M13 is marked "not reported" although the row itself says inference GPU memory is reported; "partly reported" or a matching cell would be consistent.

## Required fixes (ordered by impact)

1. Resolve the LRS-VoxMM column mapping (c7, c8). Quote the Table 2 header of [3], then fix 11.03 AV, 55.15 VO, the 2.12-point / 16.1% AV gain and the Llama-AVSR 70.71 VO so they use one consistent reading. As written, rows 12-13 contradict each other.
2. Support or drop the [6] sentence. Quote the model, modality, corpus and untransmitted baseline behind 90.26%. Remove "absent from the authors' explanations", because [6] is within six months of the target.
3. Remove or soften "so the zero-shot gap is domain, not pose". The absolute profile penalty (27.62 vs 14.45 points) points the other way. Quote which [5] column is the Lombard-trained, unseen-speaker, visual-only model, and whether it saw profile video in training.
4. Change "not in short turns" to "not only in short turns". Hard VO (126.95) is 21.6 points above Easy (105.35).
5. Give a location for the authors attributing the Llama-AVSR failure to the LLM decoder, or reword the sentence.
6. Add quotes for the unquoted values: 113.20 and 31.14 (Table XI), 43.15 (Table VIII), the code line that sets the 2.0 s boundary, and "corrected transcripts" / "keeps every turn" (Sec. II-A).
7. Replace "six corpora" with the authors' "six conditions", or quote the corpus list. Quote "released" and "zero-shot".
8. State that the [4] numbers (0.95, 14.0 ± 0.3) are audio-visual, with a quote. Note that [4] shares an author with the target.
9. Narrow "dates from WildVSR [2]" to publicly released checkpoints. Earlier zero-shot cross-corpus testing on LRS3 exists (Shillingford et al. 2018, arXiv:1807.05162).
10. Reconcile M13: GPU memory is reported, so "not reported" conflicts with the row's own cell.

## Scores

- Procedure: 7/10. The claim table covers nearly every number and the arithmetic checks out. But several numbers carry no quote, and the LRS-VoxMM columns were never pinned down.
- Final text: 6/10. The position is clear and well targeted. One internal contradiction (LRS-VoxMM AV/AO), two overreaching causal sentences and one fairness slip on [6] need fixing before publication.
