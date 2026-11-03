# Sub-word Level Lip Reading With Visual Attention

K R Prajwal, Triantafyllos Afouras, Andrew Zisserman  
arXiv 2021 · [arXiv](https://arxiv.org/abs/2110.07603)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

A structured review of *Sub-word Level Lip Reading With Visual Attention* (K R Prajwal et al., arXiv 2021) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Camera-only lip reading with WordPiece sub-word units and a visual transformer pooling front-end; reaches 28.9% WER on LRS2 and 40.6% on LRS3 with public-data training (22.6%/30.7% with extended training).

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera (silent face/lip video) |
| Task | Lip reading (visual speech recognition) |
| Vocabulary | Open vocabulary, 30522 WordPiece tokens |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 22.6% WER on LRS2, 30.7% on LRS3 (extended training); 28.9%/40.6% public data only |

**Limitations.** Camera-only lip reading rather than articulatory SSI; offline benchmark results only, with no live silent dictation, latency, privacy or in-the-wild evaluation.

## Full review

### In short

Major lip-reading gain, adjacent to SSI.

### Review

The paper is materially stronger than prior public-data lip reading systems. The final model reaches 28.9 WER on LRS2 using only public data, and 22.6 with additional data, while the ablation table shows the gains are not accidental: WordPiece decoding and visual transformer pooling each buy substantial error reduction. The scope caveat is straightforward. This is a camera-based VSR system, not a tongue, EMG, or ultrasound SSI device.

### Why it matters

This is a strong visual speech recognition paper with real benchmark gains, but it is camera-only lip reading rather than an articulatory SSI modality.

### Prior state of the art

Lip-reading systems often used character-level decoding and average pooling over face features, leaving performance and data efficiency on the table.

### What changed

Introduces visual transformer pooling and WordPiece decoding, then reuses the encoder for visual speech detection.

### Position in the field

Top-tier lip-reading paper adjacent to SSI.

### Practical value

Useful when the problem is silent-video speech recognition and data-efficient visual speech detection, especially without audio.

### Advanced

model quality; data efficiency; transfer to VSD

### Unresolved

in-the-wild silent dictation; occlusion robustness; privacy-sensitive deployment

### Evaluation details

| Item | Details |
| --- | --- |
| Task | lip reading |
| Input | silent video |
| Sensor | camera |
| Body site | face; lip |
| Output | text |
| Vocabulary type | WordPiece sub-word units |
| Vocabulary size | 30522 tokens |
| Metrics and results | Public-data training reaches 28.9 WER on LRS2 and 40.6 on LRS3; extended training reaches 22.6 and 30.7; WordPiece reduces LRS2 WER from 41.0 to 37.2 and VTP further to 30.9 |
| Evaluation protocol | LRS2 and LRS3 WER benchmarks with ablations, plus AVA ActiveSpeaker visual speech detection transfer |

### Limits

- **Technical:** The system still depends on face video quality and benchmark-style training corpora.
- **Evaluation:** All results are offline benchmarks; no live silent dictation study is reported.
- **Deployment:** No discussion of on-device latency, privacy, or in-the-wild robustness beyond benchmarks.
- **Scope of this review:** Camera-only visual speech recognition and detection.

### Evidence

- The paper proposes attention-based pooling, sub-word units, and a visual speech detection model to improve lip reading from silent videos. (Abstract)
- The best public-data model reports 28.9 WER on LRS2 and 40.6 on LRS3, while the larger-data version reaches 22.6 and 30.7. (Table 1. Comparison of different lip reading models on the test sets of the LRS2 and LRS3 datasets in terms of Word Error Rate % (WER,)
- The ablation table shows WordPiece tokenization improves LRS2 WER from 41.0 to 37.2 and adding VTP further reduces it to 30.9, so both proposed changes do real work. (Table 2. Ablation on the design improvements proposed in this)

## More reviews in Lip & face video

- [Speaker disentanglement in video-to-speech conversion](speaker-disentanglement-in-video-to-speech-conversion.md) (2021). Disentangles speaker identity from visual content in multi-speaker video-to-speech synthesis on GRID, enabling voice control; on unseen speaker identity control the best model reaches about 38.9% WER with 11.9% EER.
- [FastLTS: Non-Autoregressive End-to-End Unconstrained Lip-to-Speech Synthesis](fastlts-non-autoregressive-end-to-end-unconstrained-lip-to-speech-synthesis.md) (2022). FastLTS is a non-autoregressive end-to-end lip-to-speech system that makes unconstrained synthesis substantially faster without obvious quality loss, evaluated on Lip2Wav and GRID.
- [Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction](learning-audio-visual-speech-representation-by-masked-multimodal-cluster-prediction.md) (2022). Self-supervised audio-visual pretraining (masked multimodal cluster prediction) enabling lipreading at 32.5% WER on LRS3 with only 30 h of labels, and 26.9% with 433 h plus self-training.
- [Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild](lip-to-speech-synthesis-for-arbitrary-speakers-in-the-wild.md) (2022). VAE-GAN lip-to-speech synthesis for arbitrary speakers in the wild; holds up on unconstrained LRW/LRS2, and multi-speaker pretraining with 5 h adaptation nearly matches a 20 h single-speaker model.
- [Multi-modality Associative Bridging through Memory: Speech Sound Recollected from Face Video](multi-modality-associative-bridging-through-memory-speech-sound-recollected-from-face-video.md) (2022). Memory-based cross-modal bridging recalls audio representations from face video, applied to word-level lip reading (LRW/LRW-1000) and speaker-dependent GRID speech reconstruction.
- [SVTS: Scalable Video-to-Speech Synthesis](svts-scalable-video-to-speech-synthesis.md) (2022). SVTS shows a simple spectrogram predictor with a pretrained vocoder outperforms prior complex video-to-speech models and scales to large datasets such as LRS3+VoxCeleb2.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
