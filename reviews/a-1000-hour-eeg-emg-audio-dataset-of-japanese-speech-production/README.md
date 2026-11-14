# A 1000-hour EEG-EMG-audio dataset of Japanese speech production

Motoshige Sato, Ilya Horiguchi, Masakazu Inoue, Kenichi Tomeoka, Eri Hatakeyama, Yuya Kita, Atsushi Yamamoto, Ippei Fujisawa, Shuntaro Sasai  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2606.01264)

**Section:** [Surface EMG](../../README.md#surface-emg) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *A 1000-hour EEG-EMG-audio dataset of Japanese speech production* (Motoshige Sato et al., arXiv 2026) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

A 1020-hour EEG-EMG-audio dataset of Japanese overt speech from three participants, with signal-quality and physiological validation but no decoding benchmarks.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 128/62/63-channel scalp EEG, 3-channel facial EMG, microphone |
| Task | Dataset |
| Vocabulary | Open vocabulary |
| Speaker | Not stated |
| Session | Not applicable |
| Online / offline | Not applicable |
| Key result | Not reported |

**Limitations.** Only three Japanese male participants; evaluation limited to signal-quality checks without downstream decoding experiments.

## Full review

### In short

A 1020-hour multimodal EEG-EMG-audio dataset for Japanese overt speech vastly expands data resources, enabling diverse speech decoding and EEG research, though generalization is limited by three participants and no decoding benchmarks are presented.

### Review

This paper releases the JapanEEG dataset, a large-scale multimodal collection of 1020 hours of scalp EEG, facial EMG, and audio recorded during open-vocabulary overt Japanese speech from three participants using three different EEG systems. The dataset substantially exceeds prior public speech EEG datasets in scale and diversity of recording hardware. Rigorous technical validation demonstrates expected physiological EEG spectral profiles and event-related potentials across devices and participants, confirming high data quality. The work's principal contribution is the dataset itself, positioned to enable diverse speech decoding studies and to support broader EEG research on artifact modeling, representation learning, and cross-session/device adaptation. Limitations include a small participant pool limiting generalization and the lack of downstream decoding benchmarks. Overall, this dataset fills a notable gap in publicly available speech EEG resources, particularly for overt speech in Japanese, and offers valuable opportunities for the SSI community to develop and evaluate decoding approaches with large longitudinal multimodal EEG data.

### Why it matters

A large multimodal dataset of high-quality EEG, EMG, and audio for overt Japanese speech with strong technical validation, advancing data availability for non-invasive speech decoding research.

### Prior state of the art

Prior public EEG datasets for speech decoding were smaller in scale (hours from single- or few-channel systems), often limited to imagined speech or single devices, and predominantly in languages other than Japanese.

### What changed

Significantly larger scale and multimodal dataset with cross-device, longitudinal recordings in Japanese overt speech, supporting broader research areas beyond speech decoding alone.

### Position in the field

significant dataset contribution expanding scale and modality diversity for speech EEG decoding in Japanese overt speech

### Practical value

High practical value for research in EEG-based speech decoding, artifact modeling, and cross-device studies; direct application to deployed systems not presented.

### Advanced

scale of available EEG speech datasets dramatically increased with simultaneous multimodal recording and multiple EEG systems across many sessions.

### Unresolved

Generalization to larger subject populations is unresolved due to only three participants.

### Narrowed or regressed

No regression in the axes of modality or evaluation scope was identified from the text.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | dataset |
| Input | multimodal |
| Sensor | g.Pangolin (128 ch), g.SCARABEO (62 ch), eego™sports (63 ch); scalp EEG caps with up to 128 channels plus facial EMG electrodes (3 channels) configured around lips and eyes; lavalier microphone for audio recording. |
| Body site | brain |
| Output | audio |
| Vocabulary type | open vocabulary |
| Vocabulary size | open vocabulary |
| Evaluation protocol | quantitative |

### Limits

- **Technical:** Small sample size (n=3) limits generalization; lack of downstream decoding evaluations; longitudinal recordings from few participants only; no testing of wearable or mobile suitability reported.
- **Evaluation:** Evaluation is limited to basic signal quality and physiological validation analyses, not downstream decoding performance or benchmarking.
- **Deployment:** The dataset itself is not a deployed system; no deployment readiness or specific application deployment is described.
- **Scope of this review:** Data collected only from three Japanese male participants limits participant diversity; evaluation limited to signal quality checks without decoding experiments.

### Evidence

- We present a multimodal dataset of 1020 hours of simultaneously recorded scalp electroencephalography (EEG), facial electromyography (EMG), and speech audio from three healthy native Japanese speakers during open-vocabulary overt speech. (Abstract)
- Three scalp EEG systems were employed across the dataset: g.Pangolin (128 channels), g.SCARABEO (62 channels), and eego™sports (63 channels). Facial EMG was recorded simultaneously with three bipolar channels placed on the upper lip, lower lip, and eye regions. (Methods section)
- The dataset is publicly available via OpenNeuro in Brain Imaging Data Structure (BIDS) format under a CC0 waiver with approximately 955 GB in size. (Data Records)
- Technical validation comprised power spectral density and event-related potential analyses across participants, devices, and tasks, showing the expected 1/f spectral profile, task-related alpha-band attenuation, and time-locked evoked responses consistent with speech-related cortical activity. (Technical Validation section)
- The dataset involves only three participants, limiting generalizability across larger populations. (Methods section)

## More reviews in Surface EMG

- [AESSI: An Around-Ear Silent Speech Interface for Cross-Day Online Reuse without Test-Day Calibration](../aessi-an-around-ear-silent-speech-interface-for-cross-day-online-reuse-without-test-day-calibrat/) (2026). Around-ear cEEGrid system recognizing 25 fixed Mandarin sentences from silent articulation without test-day calibration; 92.24% mean accuracy on held-out later-day sessions and 98.00% in 250 live trials 21+ days later.
- [Affect Decoding in Phonated and Silent Speech Production from Surface EMG](../affect-decoding-in-phonated-and-silent-speech-production-from-surface-emg/) (2026). Binary affect (polite vs frustrated) classification from facial/neck sEMG in phonated and silent speech; silent-only within-subject AUC 0.829, but transfer to unseen speakers is weak.
- [Comparison of sEMG Encoding Accuracy Across Speech Modes Using Articulatory and Phoneme Features](../comparison-of-semg-encoding-accuracy-across-speech-modes-using-articulatory-and-phoneme-features/) (2026). Forward encoding of sEMG envelopes from articulatory (SPARC) versus phoneme features across speech modes; articulatory features predict muscle activity better on most channels in 24 participants.
- [Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading](../cross-modal-masking-for-robust-silent-speech-synthesis-using-semg-and-lipreading/) (2026). Silent speech synthesis fusing sEMG and lipreading with cross-modal masked training, improving performance and robustness to modality degradation over monomodal baselines.
- [CS-ETS: Chaos-Inspired Samba-Based EMG-To-Speech Synthesis with Nonlinear Chaotic Losses](../cs-ets-chaos-inspired-samba-based-emg-to-speech-synthesis-with-nonlinear-chaotic-losses/) (2026). Smaller chaos-inspired Samba-based EMG-to-speech model with nonlinear losses; WER improves modestly from 42.20% to 41.26% while parameters drop from 54.10M to 32.03M.
- [EMG-to-Speech with Fewer Channels](../emg-to-speech-with-fewer-channels/) (2026). Halving EMG electrodes costs synthesis the same ~35% relative WER known from recognition; initialization helps, channel dropout does not, and a weak unrepeated baseline undercuts the ranking.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
