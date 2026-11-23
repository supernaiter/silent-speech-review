# Evaluation: RESOUND review

Date: 2026-11-23
Evaluator: a language model separate from the writer

Inputs: the evaluator brief and `compact.md` (the review, references and claim table) only. I did not open any source. Outside knowledge that I could not locate in the given text is marked "unverified".

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | RESOUND changes the decoder (excitation and formant, additive fusion) and the use-time inputs (L2T text, 0.5 s prompt) | Claim row 1 (Sec. 2.3, 2.2.1, 1, 3.3) | correct | The quotes support all four parts. |
| 2 | "First study to incorporate source-filter theory" holds only as a label; Vid2Speech LPC with white-noise excitation | Claim rows 2, 12 | correct, but the deciding prior is incomplete | Vid2Speech models only the filter. A closer prior predicts both source and filter parameters from silent video: Michelsanti et al., "Vocoder-Based Speech Synthesis from Silent Videos", Interspeech 2020 (arXiv:2004.02541). It predicts WORLD vocoder parameters: spectral envelope, F0 and aperiodicity. Le Cornu & Milner (Interspeech 2015; IEEE/ACM TASLP 2017) used vocoder-parameter synthesis from visual features (year and locator unverified). |
| 3 | Without L2T & SRA, WER goes from 20.06 to 27.49, level with Intelligible L2S at 27.69 | Claim row 3 (Tables 1 and 3) | correct | Numbers and rows match. |
| 4 | "RESOUND matches the field's best: 20.06 vs 21.04 / 21.4%, and 28.55 vs 17.04 on LRS2" | Claim row 4 | numbers correct; wording wrong | On LRS2, RESOUND trails by 11.51 points. "Matches the field's best" cannot cover the LRS2 pair in the same sentence. |
| 5 | MAEF0 49.52 vs 81.63 and SECS 0.777 vs 0.591 pit a prompted system against "systems given none" | Claim row 5 | numbers correct; "systems" insufficient evidence | The quotes show no audio only for LipVoicer (a single face image) and DiffV2S. Nothing quoted shows how Intelligible L2S [8] gets speaker identity at inference, so the plural is not supported. |
| 6 | The SOTA claim rests on no repeated runs and on baseline rows of unstated provenance | Claim rows 6, 25, 29 | correct (absence claims) | The quote can only show training details. That is acceptable for an absence claim. |
| 7 | The ablation removes the Prosody Encoder and Excitation Generator together; UTMOS 3.002 to 2.176 (28%), MAEF0 49.52 to 69.219 (40%) | Claim row 13 | correct | My arithmetic: 27.5% and 39.8%. The authors report 28% and 40% themselves (w13), and the review does not present these as its own finding. |
| 8 | Removing L2T & SRA raises WER by 37% relative; UTMOS 3.002 to 2.840 | Claim row 18 | correct | 27.49 / 20.06 = 1.370. The authors state this figure themselves. |
| 9 | Similarity MOS 3.57 vs 2.40 (LipVoicer) and 2.96 (DiffV2S), Table 2 | Claim row 20 | insufficient quote | Three ± columns are quoted with no column headers. Nothing shows that the third column is similarity. |
| 10 | SECS 0.777 vs 0.750 and MAEF0 49.52 vs 55.42 against Intelligible L2S | Claim row 21 | correct | |
| 11 | 30-participant MOS "with 95% confidence intervals" | Claim row 23 | insufficient quote | The quote gives 30 participants and 20 samples but does not mention 95% CIs. The ± values alone do not establish the interval type. |
| 12 | "States no unseen-speaker split" | Claim row 23 (Sec. 3.1) | insufficient evidence; likely misleading | About 1,300 test utterances matches the standard LRS3 test set. Video-to-speech work usually treats that set as speaker-disjoint (unseen speakers), and V2SFlow's "unseen LRS3 speakers" is very likely the same set. The review's question about test speakers in AV-HuBERT pre-training is the right point. The M12 sentence suggests a different condition from V2SFlow's when it is probably the same. |
| 13 | LipVoicer's 21.04 differs from its own 21.4% | Claim row 25 | correct | |
| 14 | LRS2: 11.51 points, 68% relative (inference) | Claim row 26 | correct | 28.55 − 17.04 = 11.51 and 11.51 / 17.04 = 67.5%. |
| 15 | "Over 200 times slower"; Intelligible L2S faster at RTF 0.041 | Claim row 28 | correct | 14.117 / 0.063 = 224. |
| 16 | M06 state of the art: LipVoicer LRS3 WER 21.4% [4]; 20.62% in the [later] SLD-L2S table [5] | Claim rows 9, 24 | quotes correct; metric choice questionable | M06 is the decoder slot, and WER mostly reflects the lip-reader text, as the review itself argues. A naturalness metric (UTMOS or MOS) would fit the slot better. More recent video-to-speech systems from 2025 (for example AlignDiT, arXiv 2504.20629) may report lower LRS3 WER or higher naturalness (unverified). |
| 17 | M07 state of the art: V2SFlow SECS 0.851 (audio) / 0.664 (video), WER 28.5% | Claim row 16 | quote correct; comparability not stated | The review sets this SECS beside RESOUND's Resemblyzer SECS. Nothing quoted shows that V2SFlow used the same speaker encoder, so the cross-paper SECS values may not be comparable. |
| 18 | [concurrent] labels on NaturalL2S (Feb 2025) and V2SFlow (Nov 2024); [later] on SLD-L2S (2026) | References | correct | Neither concurrent work is used as a deciding prior. |
| 19 | LipVoicer uses text from the same lip-reader family (Ma et al. 2023 / Auto-AVSR) | Claim row 17 | correct | |
| 20 | Usual-approach counts (54/9; 21/23/16; 83/38/51) | Appendix | not checked (ledger tallies) | They agree with the Appendix. |

## Central claim and strongest confound

The review handles the audio-prompt confound well: a ground-truth 0.5 s segment against prompt-free baselines. It also correctly traces the WER gain to the lip reader.

It misses one confound. Auto-AVSR [22] is both the lip reader that supplies RESOUND's text at inference (Sec. 2.2.1) and the toolkit that scores WER on the output (Sec. 3.2). If the scorer comes from the same model family and training data as the text source, WER can favour RESOUND. Re-scored baselines would only partly remove that advantage.

Cross-paper WER comparisons (21.4% and 20.62% against 20.06) also mix different scorers. "Level with" is the right hedge, but the reason (different ASR) should be stated.

All slot verdicts are `standard` or `not applicable`, so the `ahead` rules do not apply.

## Required fixes (ordered by impact)

1. **Novelty, M06 and Verdict.** Name Michelsanti et al., Interspeech 2020 (WORLD F0, aperiodicity and envelope predicted from silent video) as a deciding prior for source-filter video-to-speech. It covers both excitation and filter, unlike Vid2Speech. Le Cornu & Milner 2015/2017 are possible further priors (unverified).
2. **Confound, M07 and M12.** State that Auto-AVSR is both the inference lip reader and the WER scorer, and that cross-paper WERs use different scorers.
3. **Verdict wording.** Split the sentence. RESOUND is level with the best on LRS3 but trails LipVoicer on LRS2 (28.55 against 17.04). Do not say "matches the field's best" over both.
4. **Verdict, "systems given none".** Limit this to LipVoicer and DiffV2S, or add evidence on how Intelligible L2S conditions on the speaker.
5. **M12, "no unseen-speaker split".** Note that the roughly 1,300-utterance LRS3 test set is the standard speaker-disjoint set, likely the same one as V2SFlow's. Keep the AV-HuBERT pre-training question.
6. **M07 state of the art.** Note that V2SFlow's SECS may use a different speaker encoder from RESOUND's Resemblyzer.
7. **Claim row 20.** Add the Table 2 column header that shows 3.57 / 2.40 / 2.96 are similarity MOS.
8. **Claim row 23.** Add the source for "95% confidence intervals", or drop the interval type.
9. **M06 state of the art.** Consider a naturalness-based state of the art for the decoder slot, and check 2025 systems such as AlignDiT (unverified).
10. **Component table, M07 row.** The row is labelled "Lexicon and LM" but the section is "Use-time inputs", and the audio prompt is not a lexicon or LM input. Align the label or explain the mapping.

## Scores

- Procedure: 8/10. Claim-table coverage is complete, the arithmetic is right, the chronology labels are right, and ablation caveats are credited to the authors. Points lost for the incomplete deciding prior and two thin quotes.
- Final text: 7/10. The position is clear and evidence-backed. One contradictory Verdict sentence, the missed scorer confound and the shaky unseen-speaker point reduce it.

Brief note on strengths: the review separates the lip-reader contribution from the decoder contribution, flags the audio-prompt advantage, and correctly notes that the source-filter ablation is confounded by removing two modules at once.
