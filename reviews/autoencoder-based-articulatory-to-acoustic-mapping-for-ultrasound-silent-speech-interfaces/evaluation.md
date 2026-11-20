# Independent evaluation: Autoencoder-Based Articulatory-to-Acoustic Mapping for Ultrasound Silent Speech Interfaces

Date: 2026-11-20. Fallback evaluator (claim table only). Input: the compact review, its claim table and reference list. No sources were opened. Statements about other work come from the evaluator's own knowledge and are marked as such.

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | One-layer AE bottleneck, no further hidden layers, 1-17 frames into a spectral DNN | Claim rows 1, 6 (t10, t55, t8) | correct | t55 and t10 carry it. The 64-512 bottleneck range is not quoted, but Table I rows (N = 64, N = 256) are consistent with it. |
| 2 | AE features of tongue images predate the target [2], [3] | Row 2 (c1, c2) | correct | [2] (2016) and [3] (2018) are both prior and both use deep AEs on tongue images. |
| 3 | Only baseline is raw pixels; no PCA/DCT baseline | Row 2 (t54) | correct | t54 records it as unstated, which supports "no PCA/DCT baseline". |
| 4 | "Never names PCA or DCT" (M06 paragraph) | Row 2 (t54) | insufficient evidence | t54 supports only the missing baseline, not the absence of any mention in the text. The wording needs a quote or should be "never compares with". |
| 5 | Headline 25-29% NMSE reduction | Row 3 (t21) | correct | (0.534-0.394)/0.534 = 26.2%, (0.534-0.376)/0.534 = 29.6%. These agree with the authors' rounding. |
| 6 | Pixel baseline "gained nothing" from context | Row 3 (t11, t12) | partly wrong | Test NMSE goes from 0.534 to 0.530, a small gain (0.7%), not zero. "Almost nothing" is accurate. |
| 7 | Single-frame gain 13.5-19.7% relative | Row 3 (t11, t13, t18) | correct | (0.534-0.462)/0.534 = 13.5%; (0.534-0.429)/0.534 = 19.7%. |
| 8 | Dense AE trailed DCT in [3], [4] | Row 4 (c2, c5) | correct | c2 and c5 support it in qualitative terms. |
| 9 | Usual approach: "PCA or 2D-DCT ... 32 of 39"; "about 30 per stream" | Row 5, Appendix rows 21-22 | wrong label / insufficient evidence | The Appendix gives 32 for PCA/EigenTongue alone and 13 for DCT. The 32 is labelled as the PCA-or-DCT union. "About 30 per stream" has no quote. |
| 10 | SOTA: DCAE 6.17% WER vs 6.45% DCT on SSC, 2019 [4] [concurrent] | Row 7 (c4) | insufficient evidence / contradiction | c4 quotes 6.17%, but the DCT comparison is cut off ("compared to the"). The next paragraph gives [4] as "6.58% against 7.37%" with no labels. As written, [4]'s DCT figure appears as both 6.45% and 6.58%. |
| 11 | [3]: DCT 6.45%, dense DAE 7.72% (about 20% worse) | Row 8 | insufficient evidence | Neither number is quoted. The 20% arithmetic is right if the numbers are. |
| 12 | [3]: 10.07% vs 99.51% WER at five features | Row 10 (c3) | insufficient evidence | c3 supports the direction (the DAE stays useful at K = 5) but not the numbers. |
| 13 | Comparing the SSC benchmark with this paper | Rows 7-8 | judgment beyond evidence | The SSC scores come from recognition (WER, HMM-DNN). The target does synthesis (NMSE of MGC-LSP). Feature rankings from recognition may not transfer, and the review does not say so. |
| 14 | M08 usual approach: V/UV + F0 regression, 31 of 138 | Row 11, Appendix rows 27-28 | judgment beyond evidence | 31 of 138 is 22%, a minority. That does not establish a usual approach. The target (t7) cites [2], [6], [7], [22] for copying F0 as standard practice. The verdict "behind (typical of the field)" contradicts itself. |
| 15 | M08 SOTA: 10.49 Hz RMSE, 10.32% voicing error, EMA, 2018 [6] | Row 12 (c8) | insufficient evidence | c8 is a bare table row, and its column mapping is not shown. The input is EMA, not ultrasound, and the review gives this modality difference no weight. |
| 16 | [5]: r = 0.74, listeners could not tell the samples apart | Rows 12, 14 (c6, c7) | correct | Quotes match. [5] is the authors' own prior work (2018), so it is fair to use. |
| 17 | MUSHRA 16.58 / 40.98 / 75.16 | Rows 13, 17 (t22, t29) | correct | Values appear in t22. t29 carries the authors' admission that quality is lower than vocoded speech, and the review credits it to them. |
| 18 | 30-33% correlation gain is a 1 - r reduction; raw r +15.7% | Row 15 (t51, t12, t17) | correct | 1 - r: 0.320 to 0.224 (30%) and 0.213 (33%); 0.107/0.680 = 15.7%. |
| 19 | Best configuration picked from dev and test together | Row 16 (t17, t33) | insufficient evidence, possibly wrong | t33 says Fig. 4 shows development-set scores, which points to selection on development data. No quote shows test scores were used for selection. |
| 20 | "Definitely significant" rests on no test; sizes differ only without context | No claim-table row | no quote | This bullet has no claim-table row and no quoted passage for either part. |
| 21 | 8.7M vs 46.2M weights | Row 18 (t12, t16) | correct, incomplete | The numbers match Table I. It is not stated whether 8.7M includes the AE encoder (8,192 x N weights). |
| 22 | Missed caveat: no perceptual gain from neighbouring frames | Row 9 (t31) | review missed it | t31 (§V) says listeners heard no naturalness gain from context frames. The review quotes this only in the claim table. It directly limits the multi-frame NMSE headline and belongs in "Where the claims outrun the evidence". |
| 23 | [4] labelled [concurrent] | Ref list | correct | ICASSP 2019 / arXiv March 2019 against target arXiv April 2019. It is not treated as a missed citation. |
| 24 | Absence: "Only convolutional autoencoders beat DCT" | Rows 4, 8 (c5) | correct but narrow | This rests on two studies, both on the same single-speaker SSC benchmark. Name the scope in the sentence. |
| 25 | M06 verdict standard; M08 behind | Sections | M06 consistent; M08 see #14 | The M08 verdict depends on a minority count. |

## State of the art and usual approach (evaluator knowledge, not checked against sources)

- For ultrasound-to-speech synthesis specifically (as opposed to SSC recognition), the same group's prior work (Csapó et al., Interspeech 2017) fed resized raw pixels (64 x 128 = 8,192) to a DNN. The target's pixel baseline is therefore the group's own usual design, and PCA/DCT is more typical of recognition. The review should note this split.
- Later synthesis-side encoders would make a stronger state-of-the-art line for this task: for example, 3D-CNN ultrasound-to-speech mapping (Tóth and Shandiz, 2020) and CNN/LSTM encoders by the same group (2019-2021). This is from memory, with medium confidence; check year, metric and value before citing.

## Strongest confound

The confound is task transfer combined with baseline strength. The case that the bottleneck does not beat "the usual compression" rests on recognition WER on SSC, while the target measures synthesis NMSE on a different single-speaker corpus. The review handles baseline strength well (single-frame comparison, a pixel network that cannot use context). It does not handle task transfer.

## Required fixes (ordered by impact)

1. M08: 31 of 138 is not a usual approach. Either relabel it as a minority design and change the verdict, or justify "behind" another way (for example, that copying F0 makes the MUSHRA result unachievable at use time). Also deal with the target's citations [2], [6], [7], [22] for copied F0.
2. M06: say plainly that the SSC evidence [3], [4] comes from recognition (WER), not synthesis. Soften "nothing shows the bottleneck beats the usual compression" to a statement about that task. Consider a synthesis-side state of the art.
3. Settle the [4] DCT figure (6.45% vs 6.58%) and label what "6.58% against 7.37%" compares.
4. Add quotes with locations for 6.45, 7.72, 6.58, 7.37, 10.07 and 99.51 (rows 7, 8, 10) and a column mapping for c8.
5. Add the authors' own §V caveat (t31): context frames brought no perceptual gain. It qualifies the headline directly.
6. Add a claim-table row with quotes for the "definitely significant" bullet and the "significant only without context frames" statement, or remove it.
7. Support with a quote, or withdraw, the claim that the best configuration was chosen from development and test together. t33 points to development-set selection.
8. Change "gained nothing from context" to "almost nothing (0.534 to 0.530)".
9. Fix the M06 count label: 32 is PCA/EigenTongue alone (DCT 13). Give the union count or relabel it. Source "about 30 per stream" or drop it.
10. Replace "never names PCA or DCT" with "never compares with PCA or DCT" unless a text search of the target confirms it.
11. M08 state of the art: state that [6] is EMA-based and that its Hz RMSE is not comparable to ultrasound results.
12. Size bullet: say whether the 8.7M figure includes the autoencoder encoder weights.

## Scores

- Procedure: 6/10. The arithmetic is correct and was checked. Several numeric comparator claims have no quotes, and one bullet has no claim-table row.
- Final text: 6/10. The position on M06 is clear and mostly fair. The M08 verdict and the transfer from recognition to synthesis go beyond the evidence.
