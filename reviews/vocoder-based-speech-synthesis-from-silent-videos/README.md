# Vocoder-Based Speech Synthesis from Silent Videos

Daniel Michelsanti, Olga Slizovskaia, Gloria Haro, Emilia Gomez, Zheng-Hua Tan, Jesper Jensen  
arXiv 2020 · [arXiv](https://arxiv.org/abs/2004.02541)

**Section:** [Lip & face video](../../README.md#lip--face-video) · **Review basis:** full_text

A structured review of *Vocoder-Based Speech Synthesis from Silent Videos* (Daniel Michelsanti et al., arXiv 2020) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Predicts full vocoder features from silent face video with joint visual speech recognition training on GRID; speaker-dependent model reaches PESQ 1.90 and WER 15.1%, but speaker-independent performance drops sharply.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera (silent frontal face/mouth video) |
| Task | Speech synthesis from silent video |
| Vocabulary | GRID closed vocabulary, fixed 6-word sentences |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Speaker-dependent PESQ 1.90, ESTOI 0.455, WER 15.1%; speaker-independent WER 51.6% |

**Limitations.** GRID-only closed-vocabulary evaluation with frontal video; speaker-independent results degrade sharply and no noisy or in-the-wild testing.

## Full review

### In short

A notable step forward in lip-to-speech synthesis by predicting full vocoder features and jointly training for recognition, achieving strong speaker-dependent results but lacking unseen speaker generalization.

### Review

This paper proposes a strong and interpretable baseline for video-to-speech synthesis by predicting a full set of WORLD vocoder parameters from silent videos using deep learning. The system employs a video encoder and GRU recursive module to regress spectral envelope, fundamental frequency, aperiodic parameters, and voiced/unvoiced decisions. Joint multi-task learning with an auxiliary visual speech recognition decoder provides measurable improvements. Evaluation on the GRID corpus shows that mouth-only input performs better than full-face input for reconstruction, and speaker-dependent results significantly surpass previous GAN-based methods with PESQ up to 1.90 and ESTOI 0.455, accompanied by low WER. However, generalization to unseen speakers remains a significant challenge, with PESQ dropping to 1.23 and WER rising above 50%. The closed vocabulary and controlled conditions of GRID limit deployment readiness. Overall, the paper advances video-to-speech by combining full vocoder parameter prediction with auxiliary recognition in a multi-task framework, outperforming prior approaches in speaker-dependent settings while highlighting the need for improved generalization.

### Why it matters

Demonstrates that full vocoder parameter prediction from video plus auxiliary speech recognition creates a practical baseline with better quality and intelligibility than prior partial feature or direct waveform methods.

### Prior state of the art

Prior video-to-speech systems predicted partial acoustic features or directly generated waveforms causing artifacts, with vocoder fundamental frequency and aperiodic parameters often synthesized or omitted.

### What changed

Estimates all vocoder features (SP, F0, AP) directly from raw video frames with optional VSR auxiliary task improving reconstruction; uses deep video encoder and GRU-based recursive module with dedicated decoders for each vocoder parameter.

### Position in the field

Provides a well-designed full vocoder parameter lip-to-speech baseline illustrating limits of speaker-independent generalization on GRID with multi-task VSR training.

### Practical value

Useful as an interpretable baseline for controlled speaker-dependent video-to-speech applications, highlighting benefits of predicting full vocoder parameters.

### Advanced

system_design; evaluation

### Unresolved

Speaker-independent generalization remains weak with large performance drops compared to speaker-dependent conditions.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction from silent video |
| Input | video (silent frontal face or mouth region) |
| Sensor | camera |
| Body site | lip |
| Output | speech-audio |
| Vocabulary type | closed-vocabulary English sentences |
| Vocabulary size | GRID dataset vocabulary with fixed sentence structure of 6 words |
| Metrics and results | Speaker-dependent vid2voc with VSR achieves PESQ 1.90, ESTOI 0.455, WER 15.1%; speaker-independent version drops to PESQ 1.23, ESTOI 0.227, WER 51.6%. |
| Evaluation protocol | Objective speech quality (PESQ), intelligibility (ESTOI), and word error rate (WER) from auxiliary VSR system measured under speaker-dependent and speaker-independent settings. |

### Limits

- **Technical:** Restricted to closed vocabulary GRID, speaker-dependent models perform well but speaker-independent results degrade sharply, limiting real-world application.
- **Evaluation:** Evaluation performed only on GRID corpus with fixed sentence grammar under controlled speaker-dependent and independent splits; no tested generalization to open vocabulary, noisy, or varied environments.
- **Deployment:** Limited to closed-vocabulary GRID sentences, requires frontal silent video input; speaker-independent performance is significantly worse, limiting generalization to unseen speakers and real-world environments.
- **Scope of this review:** Silent frontal video on GRID corpus with speaker-dependent and independent protocols; closed English vocabulary fixed sentence grammar; not tested for noisy or in-the-wild conditions.

### Evidence

- We present a way to synthesise speech from the silent video of a talker using deep learning that learns a mapping from raw video frames to acoustic features and reconstructs speech with a vocoder synthesis algorithm, trained also to predict text in a multi-task fashion for simultaneous speech reconstruction and recognition in real time. (Abstract)
- Our method differs from prior work by predicting all vocoder features (spectral envelope, fundamental frequency, and aperiodic parameters) directly from raw video frames rather than only spectral envelope or estimating waveforms directly, enabling focus on speech intelligibility and quality and outperforming prior GAN-based approaches. (1. Introduction)
- Experiments are conducted on the GRID corpus consisting of audio and video from 34 speakers uttering 1000 six-word closed vocabulary sentences, with evaluations in speaker-dependent and speaker-independent settings using distinct training, validation, and test partitions per setting. (2.1. Audio)
- The system is evaluated using PESQ for speech quality, ESTOI for intelligibility, and WER from the auxiliary VSR decoder's CTC-based transcription in speaker-dependent and speaker-independent conditions, with higher PESQ/ESTOI and lower WER indicating better results. (2.5. Evaluation Metrics)
- In speaker-dependent experiments, the mouth-input system with VSR achieves PESQ 1.90, ESTOI 0.455, and WER 15.1%, outperforming prior GAN-based and bottleneck feature methods; speaker-independent results degrade to PESQ 1.23, ESTOI 0.227, and WER 51.6%. (3. Results)
- Performance drops substantially in the speaker-independent scenario, showing weaker generalization to unseen speakers with a large spread in scores due to differing facial characteristics and speech traits. (3.2. Speaker Independent Case)
- The approach requires silent frontal face or mouth region video input, relies on the controlled closed-vocabulary GRID dataset, and shows limited ability to generalize to unseen speakers, constraining its applicability in real-world settings. (Abstract)
- The system uses a deep network mapping silent video frames concatenated in temporal context through 3-D convolutions, followed by a GRU-based recursive module and separate decoders for spectral envelope, aperiodic parameters, voiced/unvoiced state, fundamental frequency, and auxiliary VSR output decoded with CTC loss to jointly learn speech reconstruction and recognition. (2.3. Architecture)
- The system reconstructs speech waveforms from predicted WORLD vocoder parameters using the STRAIGHT vocoder synthesis algorithm and obtains text transcriptions from the auxiliary VSR decoder by best path CTC decoding. (2.4. Waveform Reconstruction)
- Previous methods predicted incomplete spectral features or direct waveforms causing artifacts; this work instead estimates spectral envelope, F0, and aperiodic parameters, enabling better speech intelligibility and quality. (1. Introduction)

## More reviews in Lip & face video

- [Speech Prediction in Silent Videos using Variational Autoencoders](../speech-prediction-in-silent-videos-using-variational-autoencoders/) (2020). Variational autoencoder model for speech synthesis from silent lip video that models one-to-many ambiguity; on GRID reports STOI 0.724, ESTOI 0.540 and PESQ 1.932, leading Lip2Wav on ESTOI and PESQ.
- [Speaker disentanglement in video-to-speech conversion](../speaker-disentanglement-in-video-to-speech-conversion/) (2021). Disentangles speaker identity from visual content in multi-speaker video-to-speech synthesis on GRID, enabling voice control; on unseen speaker identity control the best model reaches about 38.9% WER with 11.9% EER.
- [Sub-word Level Lip Reading With Visual Attention](../sub-word-level-lip-reading-with-visual-attention/) (2021). Camera-only lip reading with WordPiece sub-word units and a visual transformer pooling front-end; reaches 28.9% WER on LRS2 and 40.6% on LRS3 with public-data training (22.6%/30.7% with extended training).
- [Lipper: Synthesizing Thy Speech using Multi-View Lipreading](../lipper-synthesizing-thy-speech-using-multi-view-lipreading/) (2019). Lipper reconstructs speech from multi-view lip video on OuluVS2 as a regression problem; the best three-view setting reaches PESQ 2.315 with 0.169 s end-to-end delay, though audio remains robotic.
- [Video-Driven Speech Reconstruction using Generative Adversarial Networks](../video-driven-speech-reconstruction-using-generative-adversarial-networks/) (2019). Uses a GAN to generate speech audio directly from silent frontal face video on GRID; speaker-dependent WER is 26.6%, while unseen speakers degrade to 40.5% WER.
- [FastLTS: Non-Autoregressive End-to-End Unconstrained Lip-to-Speech Synthesis](../fastlts-non-autoregressive-end-to-end-unconstrained-lip-to-speech-synthesis/) (2022). FastLTS is a non-autoregressive end-to-end lip-to-speech system that makes unconstrained synthesis substantially faster without obvious quality loss, evaluated on Lip2Wav and GRID.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
