# Comparison of sEMG Encoding Accuracy Across Speech Modes Using Articulatory and Phoneme Features

Chenqian Le, Ruisi Li, Beatrice Fumagalli, Yasamin Esmaeili, Xupeng Chen, Amirhossein Khalilian-Gourtani, Tianyu He, Adeen Flinker, Yao Wang  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2604.18920)

**Section:** [Surface EMG](../README.md#surface-emg) · **Review basis:** full_text+summary

Forward encoding of sEMG envelopes from articulatory (SPARC) versus phoneme features across speech modes; articulatory features predict muscle activity better on most channels in 24 participants.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 8-channel lower-face/neck surface EMG |
| Task | Forward encoding of sEMG from speech features |
| Vocabulary | 50 sentence prompts per participant |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Gaddy replication voiced r 0.455 (SPARC) vs 0.443 (phoneme); main results plotted, not tabulated |

**Limitations.** Within-subject only; articulatory features inferred from paired voiced audio; DTW may inflate correlations; no actual decoding or synthesis gains tested.

## Full review

### In short

Articulatory features better predict aligned muscle envelopes across speech modes; this supports representation choice, while actual EMG-to-speech decoding gains remain untested.

### Review

This study offers useful evidence about which intermediate representations align with facial and neck muscle activity. In 24 speech-typical participants, a regularized linear model predicts sEMG envelopes from either audio-derived SPARC articulatory features or phoneme labels. SPARC performs better on most channels across aloud, mimed and subvocal production. This is forward encoding: the inputs are speech-derived features and the output is a muscle envelope. It is not evidence that EMG has been decoded into words or synthesized speech, a distinction the authors make explicitly. Silent trials are time-warped to paired aloud EMG, and both feature sets are extracted from the aloud audio. Applying the same warping path to both predictors makes their relative comparison more credible, but absolute correlations remain conditional on this reference-assisted alignment. They do not establish independent silent operation or equivalent natural timing across modes. The separate one-person Gaddy comparison shows modest correlation gains, from 0.443 to 0.455 for voiced speech and from 0.346 to 0.364 for mimed speech; these values must not be assigned to the main 24-person cohort. Shared predictive variance dominates, with additional unique SPARC contribution, so the findings do not imply that phonemic information is absent from EMG. Squared correlation and normalized absolute regression weights also require caution: neither establishes calibrated predictive variance explained or causal muscle specificity. The work supports testing articulatory targets in future decoders, while cross-user transfer, actual recognition improvements, and an unaligned real-time silent interface remain open.

### Why it matters

A comparatively broad within-subject physiological analysis that motivates articulatory intermediate targets without pretending to have demonstrated an end-to-end silent speech decoder.

### Prior state of the art

The paper contrasts phoneme labels with continuous articulatory targets for sEMG modeling. SPARC estimates vocal-tract kinematics from audio, while mTRF methods characterize time-lagged relationships between stimulus features and measured responses.

### What changed

Tests continuous, audio-inferred articulatory coordinates against phoneme one-hot features as forward predictors of muscle envelopes, including low-amplitude subvocal production and shared/unique predictive components.

### Position in the field

Non-invasive articulatory SSI representation research, using forward muscle-signal encoding rather than a complete speech decoder.

### Practical value

Helps choose candidate intermediate training targets and formulate electrode-placement hypotheses for subsequent sEMG decoding experiments.

### Advanced

Evidence for intermediate representation choice, comparison of muscle-signal predictability across speech modes, and descriptive electrode-to-articulator relationships.

### Unresolved

Whether the encoding advantage improves inverse speech decoding, unaligned silent inference, unseen-user and cross-mode transfer, and prospective electrode selection.

### Narrowed or regressed

No matched decoding or deployment regression established; paired voiced-reference alignment is an analysis requirement rather than a demonstrated deployable advantage.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | Forward encoding of sEMG from speech representations |
| Input | Surface electromyography with paired aloud audio used to derive predictors and timing references |
| Sensor | Eight surface EMG channels on lower face and neck; band-pass 10-450 Hz and 60 Hz harmonic notches, Hilbert envelopes at 2 kHz downsampled to 50 Hz. Aloud audio is processed at 16 kHz. |
| Body site | face; jaw; lip; throat |
| Output | Predicted sEMG envelopes and representation/electrode analyses; no decoded text or speech audio. |
| Vocabulary type | Prompted sentence encoding; no evaluated recognition vocabulary |
| Vocabulary size | 50 distinct sentence prompts per participant; phoneme representation has 39 ARPAbet phonemes plus silence, not a 40-word vocabulary. |
| Metrics and results | Primary 24-participant results report Pearson r by channel/mode in Figure 2, averaged across folds using Fisher z and summarized with SEM across subjects; precise per-channel means are not tabulated. SPARC outperforms phoneme features on most channels, and subvocal prediction is above the permutation threshold. Separate single-participant Gaddy results: voiced r 0.443 ± 0.017 (phoneme) versus 0.455 ± 0.021 (SPARC); mimed 0.346 ± 0.029 versus 0.364 ± 0.032, with gains on 7/8 electrodes in each mode. No WER, decoding accuracy or synthesis-quality result is reported. |
| Evaluation protocol | Within-subject sentence-level cross-validation of forward feature-to-EMG envelope regression, nested regularization selection, Pearson correlation, permutation nulls, paired FDR-controlled comparisons, variance partitioning and normalized weight maps. |

### Limits

- **Technical:** SPARC kinematics are inferred from voiced audio rather than measured during silent production. Aloud uses 14 features including pitch/loudness, silent modes use 12. DTW may inflate absolute correlations. Squared Pearson correlation is not automatically calibrated predictive R-squared; correlated predictors and normalized absolute weights limit causal anatomical interpretation.
- **Evaluation:** All models are evaluated within subjects using sentence-level folds, not held-out users or cross-mode transfer. Silent evaluation depends on paired voiced reference and response-derived DTW alignment. Fold count and exact repeat grouping are not detailed. Primary numeric results are plotted rather than tabulated. The Gaddy replication has one participant and incompletely specified uncertainty aggregation.
- **Deployment:** Offline forward encoding uses features derived from paired aloud audio and silently produced EMG warped to the paired aloud envelope. No autonomous silent decoder, latency measurement, wearable implementation, walking test, or patient communication study is provided.
- **Scope of this review:** Speech-typical participants and prompted sentences. Subvocal means attempted speech with an occluded vocal tract and no phonation; it should not be treated as unconstrained imagined speech. No clinical communication or end-to-end silent recognition study.

### Evidence

- Twenty-four speech-typical participants each produced 50 TIMIT sentences three times per mode. Aloud, mimed and subvocal modes are defined separately; subvocal involves an occluded vocal tract with no phonation. Eight facial/neck EMG channels were recorded. (Section II-A; Figure 1; PDF p. 2)
- The analysis compares forward prediction of EMG envelopes from SPARC and phoneme features; it explicitly does not demonstrate end-to-end decoding gains. (Introduction and Conclusion; PDF pp. 1 and 4)
- Features for every mode are extracted from paired aloud audio: 14 SPARC features for aloud, 12 kinematic features for silent modes, and 40 phoneme/silence one-hot indices at 50 Hz. (Section II-B; PDF p. 2)
- Silent envelopes are warped to paired aloud EMG with FastDTW. Both predictors use the same trial-specific path. Authors acknowledge possible inflation of absolute correlations; reviewer assessment: results remain conditional on paired-reference alignment. (Section II-A and Section III-B; PDF pp. 2 and 4)
- Evaluation is within subjects using sentence-level outer folds and training-only inner regularization selection; lags span -300 to +300 ms. Pearson correlations are averaged with Fisher z, and comparisons use FDR-controlled Wilcoxon tests. (Section II-C; PDF pp. 2-3)
- Figure 2 reports higher SPARC prediction correlation than phoneme features on most channels across modes; subvocal performance remains above the permutation threshold, and upper-lip channel 6 is strongest. Exact primary per-channel means are not tabulated. (Section III-A and Figure 2; PDF p. 3)
- On the separate single-participant Gaddy dataset, voiced correlation increases from 0.443 ± 0.017 to 0.455 ± 0.021, and mimed correlation from 0.346 ± 0.029 to 0.364 ± 0.032. SPARC improves on 7 of 8 electrodes in each mode. (Section III-A; PDF p. 3)
- Variance partitioning uses squared correlations from articulatory, phoneme and combined models. Shared contribution dominates, and unique articulatory contribution exceeds unique phoneme contribution; this does not imply absence of shared phonemic information. (Figure 3; Equations 3-5 and accompanying text; PDF pp. 3-4)
- Weight maps sum absolute coefficients over lags, average across participants and normalize within each channel. Anatomical relationships are descriptive; a formal quantitative consistency test is deferred. (Section III-B and Figure 4; PDF p. 4)
- Downstream decoding evaluation is future work. All reported comparisons are within-subject, and above-chance forward envelope prediction does not establish word recognition or new-user communication performance. (Section II-C and Conclusion; PDF pp. 3-4)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
