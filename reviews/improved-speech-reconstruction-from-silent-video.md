# Improved Speech Reconstruction from Silent Video

Ariel Ephrat, Tavi Halperin, Shmuel Peleg  
arXiv / imported corpus page 2017 · [arXiv](https://arxiv.org/abs/1708.01204)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

Reconstructs speech from silent full-face video plus optical flow with a CNN and temporal post-processing network, outperforming prior methods on GRID and TCD-TIMIT in objective metrics and human word accuracy.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera (full-face video plus optical flow) |
| Task | Speech synthesis from silent video |
| Vocabulary | 51-word GRID grammar plus unseen words in TCD-TIMIT |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | GRID S3 STOI 0.68, PESQ 1.974; human word accuracy 55.8% vs 50.9% (Vid2Speech) |

**Limitations.** Per-speaker training, unconstrained vocabulary only partly intelligible, limited audio quality, and no real-time, unseen-speaker or in-the-wild evaluation.

## Full review

### In short

Strong, benchmark-setting speaker-dependent video-to-speech system that advances speech reconstruction from silent face video but remains limited to per-speaker training and constrained conditions.

### Review

This paper demonstrates a solid early approach to direct speech reconstruction from silent full-face video using a two-stream ResNet encoder (pixels and optical flow) feeding a decoder and a Tacotron-inspired postnet to produce smooth, natural speech spectrogram reconstructions. Tested on GRID and TCD-TIMIT lipspeaker datasets, it achieves significant improvements in objective intelligibility (STOI up to 0.68 on GRID speaker S3) and subjective word accuracy (55.8% vs 50.9% over Vid2Speech). The method shows promising but limited success on the unconstrained vocabulary of TCD-TIMIT, where intelligibility is notably lower. Its main limitation remains explicit speaker-dependence, requiring separate training per speaker and lacking validation on unseen or in-the-wild speakers. Overall, it sets a benchmark for speaker-dependent video-to-speech systems using end-to-end CNN architectures but leaves open questions about generalization and deployment.

### Why it matters

The paper’s key value lies in successfully demonstrating that a dual-input CNN model combining full-face video pixels and optical flow with a temporal post-processing network can reconstruct intelligible and more natural speech audio from silent video, surpassing prior methods in objective and human evaluation, and extending progress towards unconstrained vocabulary speech reconstruction, though speaker-independence and real-world usage remain unresolved.

### Prior state of the art

Video-to-speech speechreading methods mostly treated as visual-to-text classification with limited vocabularies; voxel-to-audio regression methods existed but yielded robotic or unintelligible speech due to limited network architectures and loss functions.

### What changed

Introduces a dual-stream ResNet encoder with pixels plus optical flow, a post-processing CBHG network for temporal refinement, and regression to mel and linear spectrogram audio features enabling smoother and more natural speech reconstruction, as well as evaluation beyond constrained vocabularies.

### Position in the field

Early strong baseline for visually-driven speech reconstruction; notable for integrating optical flow and postnet to improve audio naturalness and intelligibility.

### Practical value

Provides a reference architecture and baseline benchmarks for speaker-dependent video-to-speech synthesis and audio reconstruction from silent face video for controlled settings and lab conditions.

### Advanced

system_design; evaluation

### Unresolved

speaker-independent reconstruction; real-time processing; in-the-wild capture; unconstrained vocabulary full intelligibility

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | silent full-face video frames plus dense optical flow derived from consecutive frames |
| Sensor | camera |
| Body site | face |
| Output | speech-audio |
| Vocabulary type | mixed benchmark vocabulary |
| Vocabulary size | 51-word GRID grammar plus many unseen words in TCD-TIMIT testing |
| Metrics and results | GRID S3 STOI of 0.68, ESTOI 0.398, PESQ 1.974, ViSQOL 3.349; TCD-TIMIT Lipspeaker 3 STOI 0.63, ESTOI 0.447, PESQ 1.612; Mechanical Turk word accuracy improved from 50.9% to 55.8% over previous Vid2Speech method. |
| Evaluation protocol | Objective speech quality and intelligibility metrics plus human intelligibility study and ablation experiments. |

### Limits

- **Technical:** Speaker-dependent modeling requiring per-speaker training; unconstrained vocabularies only partially intelligible; audio quality still limited; no demonstration of real-time or unseen speaker generalization.
- **Evaluation:** Evaluation is offline using GRID and TCD-TIMIT datasets, with no unseen speaker evaluation beyond lipspeaker subsets and no real-time or in-the-wild validation; objective metrics (STOI, ESTOI, PESQ, ViSQOL) and Mechanical Turk intelligibility tests on limited vocabulary datasets.
- **Deployment:** Speaker-dependent model requiring per-speaker training on cropped, registered full-face video; no demonstrated use on unknown speakers or unconstrained real-world conditions; no real-time deployment shown.
- **Scope of this review:** Speaker-dependent speech reconstruction from full-face silent video; two benchmark datasets GRID and TCD-TIMIT Lipspeakers; no unseen speaker or real-world environment tested.

### Evidence

- We present an end-to-end model based on a convolutional neural network (CNN) for generating an intelligible and natural-sounding acoustic speech signal from silent video frames of a speaking person, trained and evaluated on GRID and TCD-TIMIT datasets with significant quality improvements over prior methods. (Abstract)
- The proposed model includes a dual-tower Residual neural network (ResNet) encoder processing grayscale face images and optical flow separately, whose embeddings are concatenated and fed to a decoder and a post-processing CBHG network inspired by Tacotron to produce mel and linear spectrograms representing speech. (4. Model architecture)
- Experiments are performed on GRID dataset speakers S1-S4 using 80/20 train/test splits and on TCD-TIMIT lipspeakers 1-3, showing quantitative improvements on objective intelligibility metrics (STOI, ESTOI) and speech quality metrics (PESQ, ViSQOL). (6. Experiments)
- On GRID test speaker S3 the model achieves STOI 0.68, ESTOI 0.398, PESQ 1.974, ViSQOL 3.349 when reconstructing speech; on TCD-TIMIT lipspeaker 3 it achieves STOI 0.63, ESTOI 0.447, PESQ 1.612, with many test words outside training. (6. Experiments)
- The method is explicitly speaker-dependent requiring per-speaker training; the TCD-TIMIT dataset unconstrained vocabulary setting results in less intelligible reconstructed speech; no unseen speaker or real-time deployment evaluation was conducted. (4. Model architecture)
- The model requires individual per-speaker training on registered full-face video frames, limiting real-world deployment; speaker independence and in-the-wild robustness are not addressed. (4. Model architecture)
- The approach models speechreading as a direct regression from silent video frames to speech spectrogram features instead of a classification approach, allowing reconstruction of speech from unconstrained word dictionaries. (Introduction)
- The method improves prior video-to-speech work by fusing raw pixels and optical flow features within a dual-stream CNN encoder, replacing VGG with ResNet, and employing a Tacotron-based post-processing network to enhance speech naturalness and smoothness. (4. Model architecture)
- Evaluation includes objective intelligibility and speech quality metrics, human intelligibility experiments (Mechanical Turk), and ablations of optical flow and postnet components, demonstrating pixels carry most information but flow and postnet improve results. (6. Experiments)
- The system reconstructs multi-frame speech audio by jointly predicting mel-scale spectrograms over multiple consecutive video frames, improving smoothness over prior single-frame prediction methods. (4. Model architecture)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
