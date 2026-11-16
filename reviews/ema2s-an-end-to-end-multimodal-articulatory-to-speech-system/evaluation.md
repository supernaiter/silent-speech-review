# Evaluation: EMA2S review

Date: 2026-11-16. Independent evaluator, single pass over the review and its claim table (the table was filled by the writer, so a quote that is missing or cut off counts as unsupported). No sources were re-opened. Calculations were checked by hand.

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Latent target adds 2.2% MCD (7.334 to 7.176) and 3.2% CCR (0.841 to 0.868) over the mel-loss system | Claim rows 2, 7, 19; arithmetic | correct | 0.158/7.334 = 2.15%; 0.027/0.841 = 3.21%. |
| 2 | S I loses to the baseline on all four metrics | Row 11 (baseline 7.815/1.279/0.696/0.818; S I 8.264/1.259/0.679/0.796) | correct | All four are worse. 5.7% MCD is right (0.449/7.815). |
| 3 | "the gain comes from the mel-spectrogram loss" / "Only the mel-spectrogram loss lifts it past the baseline" | Row 7 (S III 8.445/1.303/0.697/0.831) vs baseline (row 11) | wrong | S III (deep feature loss, no mel loss) beats the baseline on PESQ (1.303 vs 1.279), STOI (0.697 vs 0.696) and CCR (0.831 vs 0.818). It loses only on MCD. |
| 4 | "The latent target adds little: S III has a higher MCD than S I" | Row 7 | wrong as framed | MCD is the only metric where S III is worse than S I. On PESQ (+0.044), STOI (+0.018) and CCR (+0.035, +4.4%) S III is better. The review picks the one metric that fits. |
| 5 | S I to S II: MCD 11.3% lower, CCR 5.7% higher | Rows 12, 2 | correct | 0.930/8.264 = 11.25%; 0.045/0.796 = 5.65%. |
| 6 | Final MCD gain over the baseline is 8.2% | Rows 11, 19 | correct | 0.639/7.815 = 8.18%. |
| 7 | Baseline and EMA2S differ in targets, normalization and vocoder (§IV-B) | Row 13 | correct (partial quote) | The quote shows the baseline target is mel-cepstrum plus aperiodicity. Normalization is not quoted. |
| 8 | Lip2AudSpec predicted an autoencoder bottleneck decoded by the pre-trained decoder [2] | Row 6 | correct | Both quotes support it. |
| 9 | EMA2S claims the cross-modal comparison "without citing this precedent" | Row 6; no quote from the target's reference list | insufficient evidence | Nothing shows the target's reference list was checked for [2] or for other latent-target work. |
| 10 | [4]: EMG 18.091% WER with deep feature loss vs 18.866% without; MRI 41.326% vs 39.005% | Rows 5, 8 | insufficient evidence | The quoted rows show "18.342 18.091 5.2336" and "26.427 41.326". They do not say which column is WER, and neither 18.866 nor 39.005 is quoted. |
| 11 | In [4] "the sign of the effect depends on the modality mix" | Rows 5, 8 | insufficient evidence / likely wrong | Both quoted rows are "Tri-modal Encoder-Decoder with Deep Feature Loss". The two tables differ in task or dataset, and the quotes do not show that they differ in modality mix. |
| 12 | Parallel WaveGAN pre-trained on Japanese JNAS, no adaptation reported | Row 9 | correct (JNAS part) | "no adaptation reported" is an absence claim with no location. |
| 13 | [3]: BLSTM-WORLD 30.1% WER vs analysis-synthesis 14.3%; 10 listeners, 65 MNGU0 sentences | Rows 3, 14, 23 | 30.1% correct; rest insufficient evidence | The quote stops at "the WER of the target value was". 14.3%, 10 listeners and 65 sentences are not quoted. |
| 14 | [5]: 18.5% listener WER on MNGU0, HiFi-GAN-based, 70 listeners | Rows 10, 15 | 18.5% correct; 70 listeners insufficient evidence | The listener count is not in any quote. |
| 15 | [5]: listeners agreed on 28 of 60 pairs "for two models that transcription separated" | Row 17 | partly supported | 28 of 60 is quoted. "that transcription separated" is not supported by any quote. |
| 16 | A/B test: 10 listeners, 15 pairs each | Row 16 | correct | Both numbers are quoted. |
| 17 | ASR character rate from an "unnamed" engine | Row 16 (t79) | insufficient evidence | This absence claim has no quote. |
| 18 | Preference is 83% vs 17% in the prose, 0.80 vs 0.20 in the Fig. 4 bars | Row 18 | 83% correct; Fig. 4 values insufficient evidence | The same prose sentence is quoted twice. No reading of Fig. 4 is given. |
| 19 | The 2-3% increments are "of a size one retraining could move" | Row 19 | unsupported position | Labelled as inference, but no source on seed variance is cited. |
| 20 | Four-sensor result shown only as unlabelled bars | Row 20 | insufficient evidence | The quote is the text claim. That the bars are unlabelled is not shown. |
| 21 | Same three speakers in training and test, 304/50 each | Row 21 | correct | Quoted. |
| 22 | M05 "Nine EMA coils; four-coil subset" | Table only | insufficient evidence | No claim-table row for nine coils. |
| 23 | M12 verdict "behind" alongside "Yardstick: typical of the field" | M12 section | contradiction | The section calls the yardstick typical and the verdict behind. The usual approach it reports (crowd-worker tests, 15 of 79) does not show that a 10-listener A/B test is behind the field. Only the comparison with the baseline paper [3] supports "behind". |
| 24 | M02 state of the art = a 2024 reuse of the EMA2S loss [4] | M02 section | wrong kind of evidence | A later reuse with mixed results is not the best current work for training-only speech-latent supervision. Stronger current lines use self-supervised speech-unit targets: Hsu et al., ReVISE, CVPR 2023; Choi et al., "Intelligible Lip-to-Speech Synthesis with Speech Units", Interspeech 2023. |
| 25 | Bibliography: target as arXiv preprint; [5] as arXiv preprint | References | likely incomplete | As I recall, EMA2S appeared at IEEE ISCAS 2021 and [5] at Interspeech 2022 (medium confidence). Cite the published versions and keep the arXiv ids. |

Chronology: [4] and [5] are correctly labelled [later] and are not treated as prior work or as missed citations. [2] (2017) and [3] (2018) are valid priors. The strongest confound, a reimplemented baseline that differs in targets, normalization and vocoder, is handled in M06. The review does not apply the same caveat to its own S III/S I reading in M02.

## Required fixes (ordered by impact)

1. **Sentences:** Verdict, "With spectrogram loss only, the end-to-end system loses to the WORLD baseline on all four metrics (Table I); the gain comes from the mel-spectrogram loss." M06, "Only the mel-spectrogram loss lifts it past the baseline (S I to S II: MCD 11.3% lower, CCR 5.7% higher) (inference)." M02, "The latent target adds little: S III (deep feature loss, no mel loss) has a higher MCD than S I (8.445 vs 8.264 dB), ..."
   **What is wrong:** Table I as quoted contradicts these sentences. S III, which has no mel loss, beats S I on PESQ, STOI and CCR (1.303/0.697/0.831 vs 1.259/0.679/0.796). It also beats the baseline on the same three metrics (1.279/0.696/0.818). MCD is the only metric that supports the review's reading.
   **Fix:** Report all four metrics for S III. Rewrite the Verdict as: "With spectrogram loss only, the end-to-end system loses to the WORLD baseline on all four metrics; adding either the mel loss or the deep feature loss lifts PESQ, STOI and CCR past the baseline, and only the mel loss also lowers MCD below it (Table I)." Replace "adds little" with a statement that matches the mixed sign across metrics. Make the matching change to "Multimodal training is not shown to help beyond the loss-function effect".

2. **Sentence:** M02 State of the art, "voiced EMG-to-speech reaches 18.091% WER with it against 18.866% without (Table 4), while tri-modal MRI-to-speech gets worse, 41.326% against 39.005% (Table 3)", and "In the [later] reuse the sign of the effect depends on the modality mix [4]."
   **What is wrong:** 18.866 and 39.005 are not in any quote, and the quoted rows do not say which column is WER. Both quoted rows are "Tri-modal" systems, so the quotes do not support "modality mix" as the variable.
   **Fix:** Quote the without-loss rows and the column headers. Name the variable that actually differs between Tables 3 and 4 (task or dataset). If that cannot be shown, drop the "modality mix" sentence.

3. **Sentence:** M02, "the authors present the cross-modal comparison as their contribution (§III-B) without citing this precedent."
   **What is wrong:** No quote or location shows that the target's reference list lacks [2] or other latent-target work. This is an absence claim with no evidence.
   **Fix:** Add a claim-table row that names the checked reference list (e.g. "References [1]-[N], no Lip2AudSpec"), or delete "without citing this precedent".

4. **Sentences:** M12, "Yardstick: typical of the field. Verdict: behind."
   **What is wrong:** The section contradicts itself. Its own usual approach (crowd-worker tests) does not establish that a 10-listener A/B test is behind the field. The verdict rests only on the comparison with the baseline paper [3].
   **Fix:** State the basis directly: "Verdict: behind its own baseline paper [3], which used open transcription with an analysis-synthesis ceiling; EMA2S reports neither." Remove "typical of the field" or explain how it fits with "behind".

5. **Sentence:** M12, "listeners agreed on only 28 of 60 pairs for two models that transcription separated [5]", and "18.5% WER from 70 listeners, 2022 [5]."
   **What is wrong:** "that transcription separated" and "70 listeners" are not in any quote.
   **Fix:** Quote the [5] passage that gives the transcription WERs of the two models and the listener count, or remove both phrases.

6. **Sentence:** M12 usual approach, "the baseline paper had 10 listeners transcribe 65 MNGU0 sentences, with an analysis-synthesis ceiling (30.1% vs 14.3% WER) [3]."
   **What is wrong:** The quote stops before 14.3%. The 10 listeners and 65 sentences are not quoted.
   **Fix:** Add the full quote, with its location in [3], for 14.3%, the listener count and the sentence count, or drop the numbers that cannot be quoted.

7. **Sentence:** "The preference result is 83% vs 17% in the prose and 0.80 vs 0.20 in the Fig. 4 average bars (§IV-C.3)."
   **What is wrong:** The claim table quotes only the 83% prose sentence, twice. The 0.80/0.20 reading of Fig. 4 is not supported, and the sentence's point depends on that mismatch.
   **Fix:** Add the Fig. 4 reading (bar label or value) as its own row, or delete the mismatch clause.

8. **Sentence:** "the 2-3% increments over S II are of a size one retraining could move (inference)."
   **What is wrong:** No evidence on seed-to-seed variance in MCD or CCR is cited, so the position goes beyond its support.
   **Fix:** Reword to "no variance is reported, so increments of 2-3% cannot be separated from run-to-run variation", or cite a source for seed variance.

9. **Sentence:** M02, "**State of the art:** A [later] 2024 study reuses the EMA2S deep feature loss [4]: ..." (and the M02 row of the component table, "18.09% WER, EMG [4]").
   **What is wrong:** A later reuse with mixed results is not the state of the art for training-only speech-latent supervision. Current work in this slot uses self-supervised speech-unit targets.
   **Fix:** Name the current best line (for example ReVISE, Hsu et al., CVPR 2023, or Choi et al., Interspeech 2023, speech-unit targets for lip-to-speech) with its metric and value. Move [4] to the body as evidence about the EMA2S loss itself.

10. **Sentences:** M12, "an ASR character rate from an unnamed engine (§IV-A)", and M06, "with no adaptation reported (§IV-A)".
    **What is wrong:** Both are absence claims with no quote.
    **Fix:** Quote the §IV-A passage that describes the ASR and the vocoder, so the reader can see that no engine name and no adaptation are given.

11. **Sentence:** Reference 1, "*arXiv preprint*, 2021. arXiv:2102.03786", and Reference 5, "*arXiv preprint*, 2022. arXiv:2209.06337."
    **What is wrong:** Both appear to have peer-reviewed versions (ISCAS 2021 and Interspeech 2022; medium confidence).
    **Fix:** Check the venues and cite the published versions with their arXiv ids. Also add a claim-table row for "Nine EMA coils" (M05).

## Scores

- Procedure: 6/10. The arithmetic is correct throughout, chronology labels are right, and the baseline confound is handled. However, several numbers and absence claims have no quote, and the table evidence was read selectively for S III.
- Final text: 6/10. The positions are clear, but the central "mel loss alone" conclusion contradicts the paper's own Table I on three of four metrics, and the M12 verdict is internally inconsistent.
