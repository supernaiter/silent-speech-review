# FastLTS: Non-Autoregressive End-to-End Unconstrained Lip-to-Speech Synthesis

Yongqi Wang, Zhou Zhao  
arXiv 2022 · [DOI](https://doi.org/10.1145/3503161.3548194) · [arXiv](https://arxiv.org/abs/2207.03800)

**Section:** [Lip & face video](../../README.md#lip--face-video) · **Review basis:** full_text

A structured review of *FastLTS: Non-Autoregressive End-to-End Unconstrained Lip-to-Speech Synthesis* (Yongqi Wang and Zhou Zhao, arXiv 2022) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

FastLTS is a non-autoregressive end-to-end lip-to-speech system that makes unconstrained synthesis substantially faster without obvious quality loss, evaluated on Lip2Wav and GRID.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Silent talking-face video |
| Task | Speech synthesis from lip video |
| Vocabulary | Lip2Wav 5000+ words; GRID 51 words |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Not reported |

**Limitations.** Benchmark corpora only with three speakers per dataset slice; no in-the-wild user study or live camera-to-audio latency test.

## Full review

### In short

This paper matters because it makes unconstrained lip-to-speech materially faster without obviously sacrificing quality.

### Review

The strongest evidence is joint, not isolated. Table 3 shows FastLTS improving GRID MOS over Lip2Wav from 3.27/3.47/3.54 to 3.59/3.68/3.73 for quality, intelligibility, and naturalness, while Section 5.5 reports 19.76x waveform speedup at a 3-second window. Table 5 also shows the speedup is not bought with GlowLTS-scale bloat: FastLTS uses 50.09M parameters versus 39.87M for Lip2Wav and 85.92M for GlowLTS. The remaining caution is quality headroom: Table 4 gives FastLTS a GRID PESQ of 1.939, which is strong but not the top reported number in that comparison.

### Why it matters

The full text supports a real systems gain: FastLTS keeps competitive perceptual quality while pushing waveform inference to 19.76x the autoregressive baseline at 3-second input length.

### Prior state of the art

Unconstrained lip-to-speech systems typically predicted mel-spectrograms first and then relied on slow autoregressive or heavy flow-based waveform generation.

### What changed

FastLTS removes the intermediate spectrogram bottleneck from the main inference path and uses a fully parallelized decoder plus GAN vocoder.

### Position in the field

Strong unconstrained lip-to-speech systems paper centered on latency reduction rather than a new sensing modality.

### Practical value

Useful when lip-to-speech quality matters but the older autoregressive waveform stack is too slow for interactive use.

### Advanced

system design; model efficiency; evaluation

### Unresolved

live deployment; robustness to unconstrained capture artifacts; broader speaker coverage

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | silent talking-face video |
| Body site | face; lip |
| Output | speech-audio |
| Vocabulary type | large-vocabulary unconstrained speech |
| Vocabulary size | Lip2Wav: 5000+ words; GRID: 51 words |
| Metrics and results | MOS quality/intelligibility/naturalness; PESQ; waveform acceleration ratio; parameter count |
| Evaluation protocol | subjective MOS on Lip2Wav and GRID, PESQ on GRID, plus mel and waveform inference-speed comparison |

### Limits

- **Technical:** Evidence is still limited to benchmark corpora with offline generation windows and three evaluated speakers per dataset slice.
- **Evaluation:** The main quality evidence is subjective MOS plus GRID PESQ; there is no in-the-wild user study or end-to-end conversational latency test.
- **Deployment:** The paper supports lower-latency generation, but not a live camera-to-audio interactive deployment.
- **Scope of this review:** Unconstrained lip-to-speech synthesis from face video only.

### Evidence

- The abstract presents FastLTS as an end-to-end non-autoregressive lip-to-speech model that directly generates waveform audio from unconstrained talking-face video with low latency. (ABSTRACT)
- Section 5.1 states that experiments use the Lip2Wav corpus with 5 speakers but evaluate on 3 speakers, and also test adaptation on 3 speakers from the constrained GRID dataset. (5.1 Datasets)
- On GRID, FastLTS reports MOS 3.59 for quality, 3.68 for intelligibility, and 3.73 for naturalness, versus 3.27, 3.47, and 3.54 for Lip2Wav. (Table 3: MOS on GRID Dataset)
- Section 5.5 reports that waveform synthesis reaches a 19.76x acceleration ratio at 3-second input length. (5.5         Inference Speedup)

## More reviews in Lip & face video

- [Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction](../learning-audio-visual-speech-representation-by-masked-multimodal-cluster-prediction/) (2022). Self-supervised audio-visual pretraining (masked multimodal cluster prediction) enabling lipreading at 32.5% WER on LRS3 with only 30 h of labels, and 26.9% with 433 h plus self-training.
- [Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild](../lip-to-speech-synthesis-for-arbitrary-speakers-in-the-wild/) (2022). VAE-GAN lip-to-speech synthesis for arbitrary speakers in the wild; holds up on unconstrained LRW/LRS2, and multi-speaker pretraining with 5 h adaptation nearly matches a 20 h single-speaker model.
- [Multi-modality Associative Bridging through Memory: Speech Sound Recollected from Face Video](../multi-modality-associative-bridging-through-memory-speech-sound-recollected-from-face-video/) (2022). Memory-based cross-modal bridging recalls audio representations from face video, applied to word-level lip reading (LRW/LRW-1000) and speaker-dependent GRID speech reconstruction.
- [SVTS: Scalable Video-to-Speech Synthesis](../svts-scalable-video-to-speech-synthesis/) (2022). SVTS shows a simple spectrogram predictor with a pretrained vocoder outperforms prior complex video-to-speech models and scales to large datasets such as LRS3+VoxCeleb2.
- [VCVTS: Multi-speaker Video-to-Speech synthesis via cross-modal knowledge transfer from voice conversion](../vcvts-multi-speaker-video-to-speech-synthesis-via-cross-modal-knowledge-transfer-from-voice-conversion/) (2022). VCVTS performs multi-speaker video-to-speech synthesis by transferring knowledge from voice conversion, with speaker control from reference speech, on GRID and LRW.
- [VisageSynTalk: Unseen Speaker Video-to-Speech Synthesis via Speech-Visage Feature Selection](../visagesyntalk-unseen-speaker-video-to-speech-synthesis-via-speech-visage-feature-selection/) (2022). VisageSynTalk disentangles speech content and visage (identity) features for video-to-speech synthesis, yielding robust results for unseen speakers on benchmarks.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
