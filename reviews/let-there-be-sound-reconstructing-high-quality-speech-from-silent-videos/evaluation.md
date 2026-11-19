# Evaluation: Let There Be Sound (Kim, Kim, Chung, AAAI 2024)

Date: 2026-11-19. Independent evaluator, single pass over the review and its claim table (claim table filled by the writer, not by a separate checker; quotes were weighed as the writer's own extraction). No sources were re-opened; items marked "from knowledge" rely on the evaluator's memory of the literature.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target changes targets (200 HuBERT units, pitch, energy) and decoder (variance predictors, flow post-net) | Row 1 quotes (Sec. Linguistic Predictor, footnote 2, Pitch/Energy Predictor) | correct | 200 clusters, 12th layer HuBERT-LARGE quoted. |
| 2 | "Large margin" holds on Lip2Wav (34.71 vs 48.73) but on GRID only 17.07 vs 17.62 | Row 2, Table 1 quotes | numbers correct, framing wrong | Same quoted row shows GRID naturalness MOS 4.46 vs 3.46 and intelligibility 4.63 vs 4.10 for VCA-GAN. The abstract's margin is plausibly about MOS; the review judges it on WER alone. |
| 3 | Scorer at 12.20% WER on real GRID speech | Row 2, Ground Truth row | correct | |
| 4 | Test sets draw on training speakers | Row 3, Sec. Datasets | correct | Both GRID and the two Lip2Wav speakers split 80/10/10. |
| 5 | VCA-GAN reports a GRID unseen-speaker split (15/8/10) | Row 17 | correct | |
| 6 | Later re-runs: 79.7% (V2SFlow) and 84.08% (Faces-to-Voices) LRS3 WER, successors 28.5% and 30.45% | Rows 4, 6, 11 | numbers correct, caveat missing | The target never trained or claimed LRS3; these are third-party trainings. The same system scores 79.7 vs 84.08 under two papers, i.e. a scorer/setup spread of ~4 points that the review does not mention. |
| 7 | Ablations do not single out the unit target (42.51 vs 42.33 vs 40.58) | Row 8, Table 5 | correct | No repeated runs: absence claim, location only. |
| 8 | VCVTS: 200-unit codebook, F0 with a two-layer convolution [2] | Row 7 | wrong (partly) | "200 160-dim units" and "a pitch predictor" are VCVTS quotes; "two 1D convolution layers" is a quote from the target's Model Configuration about its own predictors, not VCVTS. |
| 9 | VCVTS goes uncited; closest earlier design | Row 1 (References) | insufficient evidence | Absence not quoted; and ReVISE (Hsu et al., CVPR 2023, arXiv 2212.11377, Dec 2022) predicts HuBERT units from video for video-to-speech, earlier than the target and closer in target representation (from knowledge). Not named. |
| 10 | Choi et al. [6] predicted 200 HuBERT units beside mel | Row 6 | insufficient evidence | Only the V2SFlow table row (29.8%) is quoted; nothing from [6] supports "200 HuBERT units". |
| 11 | [6] labelled [concurrent] | Ref list | correct | arXiv May 2023, target Aug 2023; within six months, not treated as prior work. |
| 12 | GlowLTS (2022) flow-based lip-to-speech generator, cited in the paper | Row 10 | correct | |
| 13 | Faces-to-Voices UTMOS 4.031 vs 2.417, WER 30.45 vs 84.08, "official code" | Rows 11, 16 | correct | |
| 14 | Paper trains with no discriminator (Sec. Post-Net) | No row | no quote | Plausible, but unquoted. |
| 15 | Pitch skewness 0.654 / 0.652 / 0.696 | Row 12 | correct, selective | Same row: std 101.63 (with) vs 102.39 (without) vs 101.84 (real) moves toward real speech; skewness alone was picked. |
| 16 | Energy error "goes from 3.959 to 3.886" | Row 12 | insufficient evidence | Quote is an unlabelled list "4.155 4.275 5.314 3.886 3.959"; which column is "Ours" and the direction of change are not shown. |
| 17 | WER effect "not explained by better prosody" | Row 13 | stronger than evidence | Distribution moments do not measure frame-level pitch accuracy; no w/o-pitch WER is quoted. |
| 18 | Intelligibility MOS gap 0.16 (abstract, Table 1) vs 0.13 (Sec. Qualitative Results) | Row 21; Table 1 4.79 - 4.63 = 0.16 | correct | Genuine internal inconsistency in the target. |
| 19 | "Approaches vocoded speech" holds for GRID | Row 20 | partly wrong | Holds for MOS; GRID WER is 17.07 vs 12.44 vocoded, about 37% relative higher. |
| 20 | Authors retrain all baselines | Row 22 | insufficient evidence | Quotes show only that official implementations of VCA-GAN and MT were followed and MT is N/A on Lip2Wav. No consequence stated. |
| 21 | Vougioukas et al. and VCVTS test unseen GRID speakers | Row 18 | partly insufficient | Vougioukas quote fine; VCVTS quote says in-domain / out-of-domain speakers without naming GRID. |
| 22 | M12 state of the art: Faces-to-Voices 30.45% on unseen LRS3 | Rows 16, 4 | inconsistent | M02 cites V2SFlow at 28.5% on LRS3 (lower). The best value should be stated consistently, with the scorer caveat; LipVoicer (ICLR 2024, arXiv 2306.03258) also reports LRS3 WER in the low 20s with text guidance (from knowledge, verify value; different input assumptions). |
| 23 | M12 verdict "behind" | Appendix row 39 (unseen-speaker test 52 of 165) | judgment borderline | Unseen-speaker testing is a minority practice by the review's own count; "behind" rests on one comparator offering both settings. Acceptable if worded as such. |
| 24 | M02 usual approach: paired audio, 11 of 22 | Row 28 | insufficient evidence | Appendix row says the field is M03, the section is M02; and for studies defined by "self-supervised speech targets", paired audio is near-tautological. |
| 25 | Reference [2] and [5] venues | Ref list | wrong (medium confidence) | VCVTS appeared at ICASSP 2022; Faces-to-Voices at CVPR 2025 (from knowledge). Both listed as arXiv preprints. |

## Required fixes (ordered by impact)

1. Sentence: "The "large margin" holds on two-speaker Lip2Wav, WER 34.71% against 48.73% for VCA-GAN, but on GRID it is 17.07% against 17.62%, under a scorer at 12.20% on real speech (Table 1)." and the bullet ""Large margin" (Abstract): GRID WER 17.07% against 17.62% (Table 1) is 3% relative (inference), without an interval; the scorer gives 12.20% on real speech."
   Wrong: the same Table 1 row gives GRID naturalness MOS 4.46 against 3.46 and intelligibility 4.63 against 4.10 for VCA-GAN, which are large margins; the review tests the abstract's claim on WER only.
   Fix: state that the margin holds on GRID MOS (4.46 vs 3.46) and on Lip2Wav WER, and is only 0.55 points (3% relative) on GRID WER.

2. Sentence: "VCVTS (2022) predicts units from a 200-unit codebook and infers F0 with a two-layer convolution [2]; the paper repeats that decomposition with HuBERT units."
   Wrong: "two 1D convolution layers" is quoted from the target's own Model Configuration, not from VCVTS.
   Fix: "VCVTS (2022) predicts units from a 200-unit VQ codebook and infers F0 with a pitch predictor [2]; the paper repeats that decomposition with HuBERT units and two-layer convolutional predictors."

3. Sentence: "...and the closest earlier design, VCVTS with 200 self-supervised acoustic units and a pitch predictor [2], goes uncited."
   Wrong: ReVISE (Hsu et al., CVPR 2023, arXiv 2212.11377) already predicted HuBERT units from video for speech resynthesis before the target; it is not named, so "closest earlier design" is not established, and the "uncited" claim has no quote or location.
   Fix: name ReVISE as prior HuBERT-unit video-to-speech work, check and state whether the target cites it and VCVTS (give the reference-list location), and call VCVTS "the closest earlier design with a pitch predictor".

4. Sentence: "Two [later] re-runs from the authors' group put the system at 79.7% and 84.08% LRS3 WER on unseen speakers, against 28.5% and 30.45% for their successors [4], [5]."
   Wrong: omits that the target never trained or claimed LRS3, that these are trainings by other papers, and that the same system differs by about 4 points between the two re-runs (scorer and setup differ).
   Fix: add "a dataset the paper did not use; the two re-runs differ by 4.4 points for the same system, so cross-paper values are indicative only."

5. Sentence (M12): "**State of the art:** In 2025 Faces-to-Voices [later] reaches 30.45% LRS3 WER on unseen speakers, real speech at 2.29% [5]."
   Wrong: inconsistent with M02, which cites V2SFlow at 28.5% on the same benchmark; the stated value is not the best the review itself reports.
   Fix: give V2SFlow 28.5% [4] (or both, noting different scorers), and check text-guided systems such as LipVoicer (2023/2024) that report lower LRS3 WER under different assumptions.

6. Sentences: "The predictors barely move their targets: pitch skewness is 0.654 with the pitch predictor and 0.652 without, against 0.696 for real speech (Table 2); energy error goes from 3.959 to 3.886 (Table 3). Their WER effect (Table 5) is thus not explained by better prosody (inference)."
   Wrong: skewness is selected while the same row's std (101.63 vs 102.39, real 101.84) moves toward real speech; the energy quote does not show which value is the model's, so the direction is unverified; distribution moments cannot rule out frame-level prosody gains.
   Fix: report std alongside skewness, label which energy MAE belongs to which system, and replace the last sentence with "Table 2 and 3 show small distribution-level changes; whether prosody accounts for the WER effect is not tested."

7. Sentence: "In 2023 the [concurrent] Choi et al. predicted 200 HuBERT units beside mel [6]..."
   Wrong: no quote from [6] supports "200 HuBERT units"; the claim-table row quotes only V2SFlow's table.
   Fix: add the quote and location from [6] for the unit type and cluster count, or drop "200".

8. Sentence: ""Approaches vocoded speech" holds for GRID; on Lip2Wav WER is 34.71% against 6.05% vocoded (Table 1)..."
   Wrong: on GRID WER is 17.07% against 12.44% vocoded (about 37% relative higher); the claim holds for MOS only.
   Fix: "holds for GRID MOS (gaps 0.28 and 0.16) but not GRID WER (17.07% vs 12.44%); on Lip2Wav ..."

9. Sentence: "The authors retrain all baselines; MT is absent on Lip2Wav (Table 1)."
   Wrong: the quotes show only that official implementations of VCA-GAN and MT were followed; "retrain all" is unsupported, and the bullet states no consequence, so it is not a claim outrunning evidence.
   Fix: quote where retraining of each baseline is stated, and say what follows (for example, baseline numbers differ from the original papers and tuning is unverified), or remove the bullet.

10. Sentence: "Unlike the GAN-based VCA-GAN, the paper trains with no discriminator (Sec. Post-Net), using a variance adaptor and flow post-net from text-to-speech."
    Wrong: no claim-table row or quote supports "no discriminator".
    Fix: add the quote from Sec. Post-Net or the training-loss section.

11. Sentence: "Vougioukas et al. [7] and VCVTS [2] test unseen GRID speakers too."
    Wrong: the VCVTS quote mentions in-domain and out-of-domain speakers but not GRID.
    Fix: quote the VCVTS passage naming the GRID unseen-speaker set, or write "VCVTS tests out-of-domain speakers".

12. Sentence (M02): "...the usual supervision is paired audio (11 of 22 with that field filled, slot-filled)."
    Wrong: the Appendix row attributes the count to an M03 field while the section is M02, and for studies selected by self-supervised speech targets, paired audio is near-definitional, so the line says little about usual design.
    Fix: correct the field reference and state the usual target type (for example mel only vs units vs units plus prosody) instead.

13. References [2] and [5].
    Wrong: VCVTS was published at ICASSP 2022 and Faces-to-Voices at CVPR 2025 (medium confidence); both are listed as arXiv preprints.
    Fix: verify and update the venues.

## Scores

Procedure: 6/10. Final text: 6/10.

Short note: the MOS internal inconsistency (0.16 vs 0.13), the GRID all-speaker split and the near-equal ablation drops are well found and correctly quoted.
