# Evaluation: Audio-visual video-to-speech synthesis with synthesized input audio

Date: 2026-11-22. Fallback evaluator (claim table only, no source access). Input: compact review, claim table and reference list. Sources were not re-opened. Where a note draws on outside knowledge rather than the claim table, it is marked as inference.

## Claim checks

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper adds a second synthesis pass on first-pass speech plus video, with modality dropout (Verdict) | Claim row 1, Sec. I quotes | correct | Quotes support both the pre-trained V2A first stage and modality dropout. |
| 2 | GRID unseen: pre-trained base 17.63% WER, its second pass 17.70% (Table VI) | Claim row 3 | insufficient evidence | 17.63 is quoted (t25). 17.70 has no quote. The State of the art line gives 17.69% for the best second-pass model (t39), so it is unclear which model gives 17.70 and whether 17.69 vs 17.70 are two different rows or a rounding slip. |
| 3 | Earlier systems keep lower WER on three of the four WER splits [4], [5] | Claim rows 3, 6 | partly correct | The quotes support GRID 4-speaker (SVTS-S 2.37 vs 3.67), GRID unseen (16.05 vs 17.69) and LRW (12.90 vs 14.24). The fourth split is not named, and no quote shows it. |
| 4 | Strongest confound is extra training with no equal-training control (§V-C, §V-C3) | Claim table | insufficient evidence | No row quotes §V-C or §V-C3. The point is reasonable, but it is an absence claim and the location is not shown. |
| 5 | §I claims no earlier method used audio inputs at inference, but autoregressive decoders do [2] | Claim row 15 | wrong as framed | The quotes match the passages. But feeding back previous output frames in an autoregressive decoder is not the same design as giving a separate audio encoder a whole synthesized utterance, and the review says so itself ("The departure is a whole-utterance, non-autoregressive second pass"). The rebuttal is stronger than the evidence. It also names a 2021/2022 work when earlier autoregressive lip-to-speech decoders exist (inference: Lip2Wav, Prajwal et al., CVPR 2020, Tacotron 2-style decoder). |
| 6 | Modality dropout comes from audio-visual recognition [3] | Claim row 2 | wrong (chronology) | AV-HuBERT (2022) is not the origin. Modality dropout predates it (inference: ModDrop, Neverova et al., IEEE TPAMI 2016, arXiv:1501.00102). Ngiam et al. (ICML 2011) already zeroed out one modality during training. Say "is common in audio-visual recognition [3]" instead. |
| 7 | Training-set audio comes from a base fitted to the same set; the train/test gap is not measured (§V-C) | Claim table | insufficient evidence | No quote. The mismatch inference is plausible and labelled as inference. |
| 8 | LRW raw waveform WER 29.79 → 24.96, 4.83 points, 16.2% relative | Claim row 8 | partly correct | 24.96 is quoted (t27). 29.79 has no quote. The arithmetic is right (29.79 − 24.96 = 4.83; 4.83/29.79 = 16.2%). The 24.96 row is the modality-dropout (GT audio) variant, so the drop mixes the second pass with the dropout variant. |
| 9 | 4-speaker GRID without audio pre-training: 4.68 → 4.84 (Table III) | Claim row 9 | insufficient evidence | 4.84 is quoted (t24). 4.68 has no quote. |
| 10 | GRID unseen 16.05% (2021) [4]; LRW 12.90% (2022) [5] | Claim rows 6, 14 | correct values, year inconsistent | Both values are quoted. The paper's table labels [4] as "(2022)", the reference list gives the journal year 2023, and the review says 2021 (arXiv). Use one convention. |
| 11 | [later] flow-based model reaches 28.5% WER on LRS3 [8] | Claim row 7 | insufficient evidence | The source is an audit tally, not a quote from V2SFlow. LRS3 is not one of the paper's datasets, so this number cannot be compared with anything in the review. |
| 12 | Neural vocoder is the usual decoder, 49 of 165 | Claim rows 4, 19 | correct (ledger) | Ledger tally, accepted as given. |
| 13 | Seven of 165 feed predicted spectrogram frames back (teacher forcing or scheduled sampling) | Claim row 5 | wording error | Teacher forcing feeds ground-truth frames, not predicted frames. Only scheduled sampling and free-running inference feed predictions. |
| 14 | Memory network recalls audio context from video alone [7] | Claim row 5 | correct | Quote supports it. |
| 15 | 38 of 44 modality-dropout studies are recognition/lip reading/pre-training | Claim rows 10, 24 | correct (ledger) | Ledger tally. |
| 16 | GT-audio dropout variant uses ground-truth audio in audio-only passes, synthesized audio at inference (§V-C) | Claim table | insufficient evidence | No quote. |
| 17 | No video-to-speech study isolates modality dropout; 4 of 165 mention it, all 2023 or later | Claim row 11 | insufficient evidence / contradiction | No deciding works are named. The target itself compares variants with and without dropout (Table VII), which is an isolation of dropout. The sentence contradicts the next one. |
| 18 | GRID unseen: plain dropout best (18.32%) | Claim row 12 | mismatch | The quote for this row is 17.63, the pre-trained base, not a dropout variant. 18.32 has no quote. 18.32 is also worse than 17.69 (AV2A-MelSpec-S) and 17.70, so "best" on GRID unseen is wrong unless it is restricted to one model family. |
| 19 | LRW mel: variant without dropout best (14.24%, Table VII) | Claim row 12 | partly correct | 14.24 is quoted for AV2A-MelSpec-M. The quote does not show that this variant has no dropout. |
| 20 | 83 of 165 run a listener or opinion test [9], [10] | Claim rows 13, 27 | correct (ledger) | Both cited works are plausible examples. |
| 21 | Paper reports only PESQ, STOI, ESTOI, ASR WER and concedes imperfect correlation with perception (§V-D) | Claim row 13 | partly correct | The four metrics are quoted. The concession about perception has no quote. |
| 22 | M12 State of the art: best WER in the field table is 16.05% | Claim row 14 | wrong component | This is a decoding result, not an evaluation practice. The M12 state of the art should name the strongest evaluation protocol (for example a listener intelligibility test with MOS, multiple seeds). |
| 23 | STOI 0.690 → 0.698 (Table III), single runs with no seeds | Claim row 16 | insufficient evidence | 0.698 is quoted (t23). 0.690 has no quote, and the only other Table III STOI quoted is 0.696 (t24). The batch-size quote does not show that only single runs were made. |
| 24 | Authors note WER fluctuates (§VI-A) and the decoder may suffer from fine-tuning twice (§VI) | Claim table | insufficient evidence | No quote. If the authors raise fine-tuning effects themselves, the extra-training confound is partly their own caveat. The Verdict should credit them rather than present it as the review's own finding. |
| 25 | TCD-TIMIT: VCA-GAN STOI 0.595 [6] beats every proposed model (Table V) | Claim row 17 | partly correct | 0.595 for VCA-GAN is quoted (t31). The proposed models' TCD-TIMIT STOI values are not quoted, so "beats every" is not shown. |

## Required fixes (ordered by impact)

1. Fix the GRID unseen numbers. The plain-dropout "best" at 18.32% contradicts the 17.69% and 17.70% given elsewhere, and its quote is the 17.63% base. Add quotes for 17.70 and 18.32 and say which model each row is.
2. Restate the §I rebuttal. An autoregressive frame feedback loop [2] is not the same as a separate audio input at inference. Say the novelty claim is narrower than §I states, not false, and cite the earliest autoregressive lip-to-speech decoder (inference: Lip2Wav, CVPR 2020).
3. Correct the origin of modality dropout. It predates AV-HuBERT (ModDrop, Neverova et al., TPAMI 2016, arXiv:1501.00102). Change "comes from" to "is common in".
4. Resolve the M03 absence claim. "No video-to-speech study isolates modality dropout" conflicts with the target's own Table VII ablation. Name the 4 ledger studies or drop the sentence.
5. Add quotes for the base values used in the effect sizes: 29.79 (LRW raw waveform), 4.68 (GRID 4-speaker) and 0.690 (STOI). Also say that the 24.96 row includes the dropout variant, so the 4.83-point gain is not the second pass alone.
6. Add quotes and locations for the extra-training confound (§V-C, §V-C3), the GT-audio training detail and the authors' own caveats (§VI, §VI-A). Credit the authors where they raised fine-tuning effects themselves.
7. Replace the M12 State of the art line with an evaluation-practice benchmark, not a WER number. The M12 table row needs the same change.
8. Either quote the proposed models' TCD-TIMIT STOI values or soften "beats every proposed model".
9. Name the fourth WER split in "three of the four", or say which split the proposed model wins.
10. Fix "teacher forcing" in the M06 usual approach. Teacher forcing feeds ground-truth frames.
11. Use one year convention for [4] (the 2021 arXiv year vs the 2022 table label vs the 2023 journal year).
12. The LRS3 V2SFlow figure is not on any of the paper's splits. Quote it from the source and label it as a different benchmark. Check whether stronger recent LRS3 results exist (inference: LipVoicer, Yemini et al., arXiv:2306.03258, ICLR 2024, reports a lower LRS3 WER, medium confidence). Also cite V2SFlow's published venue if there is one (low confidence: ICASSP 2025).

## Scores

- Procedure: 6/10
- Final text: 5/10

What works: the review takes a clear position, separates ledger tallies from quoted values, uses the correct [later] label for V2SFlow, and its proposed controls (an equal-training base, cross-fitted training audio, seeds and a listener test) are concrete and fit the confounds.
