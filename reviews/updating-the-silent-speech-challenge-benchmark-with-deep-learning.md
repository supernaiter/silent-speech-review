# Updating the silent speech challenge benchmark with deep learning

Yan Ji, Licheng Liu, Hongcui Wang, Zhilei Liu, Zhibin Niu, Bruce Denby  
arXiv 2017 · [arXiv](https://arxiv.org/abs/1709.06818)

**Section:** [Ultrasound & tongue imaging](../README.md#ultrasound--tongue-imaging) · **Review basis:** full_text

A structured review of *Updating the silent speech challenge benchmark with deep learning* (Yan Ji et al., arXiv 2017) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Updates the Silent Speech Challenge ultrasound-plus-lip benchmark with Kaldi DNN-HMM recognition, cutting WER from 17.4% to 6.45% on the same single-speaker archive.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Under-chin ultrasound transducer plus lip camera |
| Task | Continuous silent speech recognition |
| Vocabulary | WSJ0 5000-word lexicon |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 6.45% WER (DNN-HMM, task-specific LM) vs 17.4% original benchmark |

**Limitations.** Small single-speaker controlled archive; no speaker independence, real-world robustness or live deployment evidence.

## Full review

### In short

Benchmark update with a real, reproducible WER gain.

### Review

The strongest part of the paper is methodological discipline. It does not introduce a new sensing modality; it keeps the Silent Speech Challenge framing intact long enough to ask what deep learning changes. Table 2 is the headline: the original 17.4% WER benchmark remains 17.4% under a Kaldi GMM-HMM reproduction, then drops to 6.45% with a DNN-HMM. Table 3 also shows that language-model choice matters, with DNN WER moving from 11.44% under the WSJ LM to 6.45% under the task-specific CSR LM. That makes this a benchmark-updating paper with genuine value, but still within a single-speaker controlled archive rather than a broadly deployable SSI.

### Why it matters

This is a benchmark-anchored SSI paper with a real methodological payoff: on the same archive and decoding framing, DNN-HMM recognition almost triples performance over the original benchmark value.

### Prior state of the art

The Silent Speech Challenge was a fixed ultrasound-plus-lip benchmark whose published reference point was 17.4% WER with an HTK GMM-HMM system.

### What changed

The paper reruns the benchmark with matched decoding in Kaldi, then shows a DNN-HMM can cut WER to 6.45% and that language-model choice matters materially.

### Position in the field

Canonical benchmark update for ultrasound-plus-lip silent speech recognition.

### Practical value

High for benchmarking and for understanding what part of the gain comes from model class versus feature or language-model choice.

### Advanced

benchmark reproducibility; evaluation; modeling baseline

### Unresolved

speaker independence; larger corpora; live deployment

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech recognition |
| Input | ultrasound tongue imaging and lip video |
| Sensor | Ultrasound transducer placed under the chin plus a small lip video camera |
| Body site | tongue / lips |
| Output | text |
| Vocabulary type | continuous-speech benchmark vocabulary |
| Vocabulary size | WSJ0 5000-word lexicon with task-specific and WSJ language-model settings |
| Metrics and results | Table 2 reports 17.4% WER for the original HTK benchmark, 17.4% for a Kaldi GMM-HMM reproduction, and 6.45% for the Kaldi DNN-HMM with 30-element DCT features. Table 3 shows DNN WER of 11.44% with the WSJ LM and 6.45% with the task-specific CSR LM. |
| Evaluation protocol | Direct comparison to the original Silent Speech Challenge benchmark plus language-model and feature sweeps on the same single-speaker archive. |

### Limits

- **Technical:** Everything remains single-speaker, controlled, and benchmark-bounded; there is no evidence of speaker independence or real-world robustness.
- **Evaluation:** The archive is small and single-speaker, so large gains on this benchmark do not automatically transfer to broader SSI deployment.
- **Deployment:** No live deployment, calibration burden analysis, or user-facing interface is reported.
- **Scope of this review:** Speaker-dependent ultrasound-plus-lip benchmark study.

### Evidence

- The abstract says the 2010 Silent Speech Challenge benchmark is updated with deep-learning results and that a best word error rate of 6.4% is obtained compared with the published 17.4% value. (Abstract)
- The Silent Speech Challenge benchmark is a single-speaker archive built from ultrasound and lip video recorded from one native English speaker with an independent test corpus. (1.2. The Silent Speech Challenge benchmark)
- Table 2 reports 17.4% WER for the original HTK benchmark, 17.4% for the Kaldi GMM-HMM reproduction, and 6.45% for the Kaldi DNN-HMM using 30-element DCT features. (Table 2. Comparison with original HTK result of [52], using 30-element DCT features)
- Table 3 shows that with 30-element DCT features the DNN system gets 11.44% WER under the WSJ language model and 6.45% under the task-specific CSR language model. (Table 3. Comparing results for the 2 different LM, for 30-element feature vectors of both types)

## More reviews in Ultrasound & tongue imaging

- [Contour-based 3d tongue motion visualization using ultrasound image sequences](contour-based-3d-tongue-motion-visualization-using-ultrasound-image-sequences.md) (2016). Builds a contour-based pipeline that maps midsagittal ultrasound tongue contours to 3D tongue motion using a database of 1000 3D shapes; evaluation is qualitative, with about 1.2 s per frame association.
- [Autoencoder-Based Articulatory-to-Acoustic Mapping for Ultrasound Silent Speech Interfaces](autoencoder-based-articulatory-to-acoustic-mapping-for-ultrasound-silent-speech-interfaces.md) (2019). Compresses ultrasound tongue images with an autoencoder bottleneck before predicting spectral parameters, giving more accurate prediction and more natural speech with smaller models on a single speaker.
- [Denoising convolutional autoencoder based B-mode ultrasound tongue image feature extraction](denoising-convolutional-autoencoder-based-b-mode-ultrasound-tongue-image-feature-extraction.md) (2019). Uses a denoising convolutional autoencoder to extract ultrasound tongue image features, improving silent speech recognition over prior feature extraction methods on the 2010 Silent Speech Challenge data.
- [SottoVoce: An Ultrasound Imaging-Based Silent Speech Interaction Using Deep Neural Networks](sottovoce.md) (2019). SottoVoce reconstructs speech audio from under-jaw ultrasound images with two DNNs to control unmodified smart speakers; command success rose from 42.5% to 65.0% with the second network, versus 90.0% for real audio.
- [Ultrasound-based Silent Speech Interface Built on a Continuous Vocoder](ultrasound-based-silent-speech-interface-built-on-a-continuous-vocoder.md) (2019). Adds CNN-based continuous F0 prediction to an ultrasound tongue-imaging SSI vocoder, lowering pitch RMSE versus a discontinuous F0 baseline, with a non-significant naturalness trend in MUSHRA tests on four Hungarian speakers.
- [Ultra2Speech -- A Deep Learning Framework for Formant Frequency Estimation and Tracking from Ultrasound Tongue Images](ultra2speech-a-deep-learning-framework-for-formant-frequency-estimation-and-tracking-from-ultrasound-tongue-images.md) (2020). Estimates and tracks formant frequencies from ultrasound tongue image sequences for speech synthesis; best U2F configuration reaches mean R2 99.96 on joint f1-f2 prediction versus 90.01 for a Conv-BiLSTM baseline.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
