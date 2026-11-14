# Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction

Bowen Shi, Wei-Ning Hsu, Kushal Lakhotia, Abdelrahman Mohamed  
ICLR 2022 / arXiv · [arXiv](https://arxiv.org/abs/2201.02184)

**Section:** [Lip & face video](../../README.md#lip--face-video) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction* (Bowen Shi et al., ICLR 2022 / arXiv) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Self-supervised audio-visual pretraining (masked multimodal cluster prediction) enabling lipreading at 32.5% WER on LRS3 with only 30 h of labels, and 26.9% with 433 h plus self-training.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera and microphone (audio-visual video; video-only at lipreading inference) |
| Task | Lipreading (visual speech recognition) and ASR |
| Vocabulary | Open vocabulary (LRS3) |
| Speaker | Speaker-independent |
| Session | Not applicable |
| Online / offline | Offline |
| Key result | 32.5% WER (30 h labels), 26.9% WER (433 h + self-training) on LRS3 lipreading |

**Limitations.** Vocalized English TED-style video only; no silent-articulation, real-time or on-device evaluation; heavy pretraining compute.

## Full review

### In short

Self-supervised audio-visual pretraining that made strong lipreading possible with little labeled data.

### Review

AV-HuBERT pretrains a ResNet-plus-Transformer encoder on 1,759 hours of unlabeled audio-visual video by masking both streams and predicting iteratively refined cluster targets, with modality dropout so the model can run on lips alone. With only 30 hours of labeled LRS3 it reaches 32.5% lipreading WER, below a prior 33.6% system trained on 31,000 hours of transcribed video; with 433 labeled hours plus self-training it reaches 26.9%. It also gives 1.3% ASR WER on LRS3. For SSI, the main lesson is that visual front-ends benefit hugely from audio-visual self-supervision, and these representations became a common backbone for lip-to-text and lip-to-speech work. The limitation is that everything is measured on vocalized TED-style video, not silent articulation.

### Why it matters

Showed that self-supervised audio-visual pretraining cuts labeled-data needs for lipreading by orders of magnitude, providing a reusable visual speech backbone.

### Prior state of the art

State-of-the-art lipreading relied on very large transcribed video corpora, sometimes tens of thousands of hours of non-public data.

### What changed

Masked multimodal cluster prediction with iterative target refinement and modality dropout learns visual speech features from unlabeled audio-visual video.

### Position in the field

Core VSR representation-learning paper; widely used backbone for visual SSI and lip-to-speech research.

### Practical value

High as a pretrained visual encoder; direct silent-speech performance is not evaluated.

### Advanced

self_supervised_learning; label_efficiency; visual_representation

### Unresolved

Silent articulation; non-English and low-resource lipreading; short-utterance homophene ambiguity

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-recognition |
| Input | video (lip region) and audio for pretraining; video only for lipreading |
| Sensor | camera and microphone (TED/VoxCeleb2 video) |
| Body site | face; lip |
| Output | text |
| Vocabulary type | open vocabulary (LRS3) |
| Vocabulary size | open vocabulary; unigram subword units |
| Metrics and results | LRS3 lipreading WER 32.5% with 30 h labeled (vs 33.6% prior SOTA using 31,000 h); 28.6% with 433 h labeled; 26.9% with 433 h plus self-training; ASR WER 1.3% (vs 2.3% prior) |
| Evaluation protocol | LRS3 benchmark with 30 h and 433 h labeled fine-tuning, CTC and seq2seq criteria, ablations of masking and clustering |

### Limits

- **Technical:** Large models (103M/325M parameters) and heavy pretraining compute; short utterances remain hard because of homophenes.
- **Evaluation:** English LRS3 only; adding non-English pretraining helps only when English data are scarce; no noisy AVSR results in this paper.
- **Deployment:** Offline benchmark evaluation; no real-time or on-device testing.
- **Scope of this review:** Audio-visual representation learning evaluated on lipreading and ASR of vocalized speech.

### Evidence

- The abstract introduces AV-HuBERT, which masks multi-stream video input and predicts automatically discovered and iteratively refined multimodal hidden units. (Abstract; Section 3)
- With 30 h labeled LRS3 and 1,759 h unlabeled pretraining, the LARGE model reaches 32.5% lipreading WER, versus 33.6% for a prior system trained on 31,000 h of transcribed video. (Section 4, lipreading results table)
- With 433 h labeled data the LARGE model reaches 28.6% WER, and 26.9% with self-training. (Section 4, lipreading results table)
- Pretraining uses LRS3 (433 h) plus English VoxCeleb2 (1,326 h), 1,759 h total. (Section 4.1)
- Appendix analysis attributes higher error on short utterances to homophenes, and the ethics statement notes speaker-distribution bias and surveillance risk. (Appendix F; Ethics Statement)

## More reviews in Lip & face video

- [FastLTS: Non-Autoregressive End-to-End Unconstrained Lip-to-Speech Synthesis](../fastlts-non-autoregressive-end-to-end-unconstrained-lip-to-speech-synthesis/) (2022). FastLTS is a non-autoregressive end-to-end lip-to-speech system that makes unconstrained synthesis substantially faster without obvious quality loss, evaluated on Lip2Wav and GRID.
- [Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild](../lip-to-speech-synthesis-for-arbitrary-speakers-in-the-wild/) (2022). VAE-GAN lip-to-speech synthesis for arbitrary speakers in the wild; holds up on unconstrained LRW/LRS2, and multi-speaker pretraining with 5 h adaptation nearly matches a 20 h single-speaker model.
- [Multi-modality Associative Bridging through Memory: Speech Sound Recollected from Face Video](../multi-modality-associative-bridging-through-memory-speech-sound-recollected-from-face-video/) (2022). Memory-based cross-modal bridging recalls audio representations from face video, applied to word-level lip reading (LRW/LRW-1000) and speaker-dependent GRID speech reconstruction.
- [SVTS: Scalable Video-to-Speech Synthesis](../svts-scalable-video-to-speech-synthesis/) (2022). SVTS shows a simple spectrogram predictor with a pretrained vocoder outperforms prior complex video-to-speech models and scales to large datasets such as LRS3+VoxCeleb2.
- [VCVTS: Multi-speaker Video-to-Speech synthesis via cross-modal knowledge transfer from voice conversion](../vcvts-multi-speaker-video-to-speech-synthesis-via-cross-modal-knowledge-transfer-from-voice-conversion/) (2022). VCVTS performs multi-speaker video-to-speech synthesis by transferring knowledge from voice conversion, with speaker control from reference speech, on GRID and LRW.
- [VisageSynTalk: Unseen Speaker Video-to-Speech Synthesis via Speech-Visage Feature Selection](../visagesyntalk-unseen-speaker-video-to-speech-synthesis-via-speech-visage-feature-selection/) (2022). VisageSynTalk disentangles speech content and visage (identity) features for video-to-speech synthesis, yielding robust results for unseen speakers on benchmarks.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
