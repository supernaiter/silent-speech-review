# Auto-AVSR: Audio-Visual Speech Recognition with Automatic Labels

Pingchuan Ma, Alexandros Haliassos, Adriana Fernandez-Lopez, Honglie Chen, Stavros Petridis, Maja Pantic  
ICASSP 2023 · [DOI](https://doi.org/10.1109/ICASSP49357.2023.10096889) · [arXiv](https://arxiv.org/abs/2303.14307)

**Section:** [Lip & face video](../../README.md#lip--face-video) · **Review basis:** full_text

A structured review of *Auto-AVSR: Audio-Visual Speech Recognition with Automatic Labels* (Pingchuan Ma et al., ICASSP 2023) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Training lipreading and AV-ASR on 3,448 h including ASR-pseudo-labelled AVSpeech and VoxCeleb2 cuts LRS3 visual-only WER to 19.1% and audio-visual WER to 0.9%.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Video camera (lip region) and microphone |
| Task | Visual, audio and audio-visual speech recognition |
| Vocabulary | Open-vocabulary English (LRS2/LRS3) |
| Speaker | Speaker-independent |
| Session | Not applicable |
| Online / offline | Offline |
| Key result | LRS3 WER: VSR 19.1%, ASR 1.0%, AV-ASR 0.9%; LRS2 VSR 14.6% |

**Limitations.** Vocalized broadcast/YouTube speech only; no silent or wearable-view test; pseudo-labels noisy; benchmark-only evaluation.

## Full review

### In short

Pseudo-labelling unlabelled AVSpeech and VoxCeleb2 with a public ASR model scales VSR training to 3,448 h and cuts LRS3 visual-only WER to 19.1%, with AV-ASR at 0.9%.

### Review

Auto-AVSR is a data-scaling paper: rather than new architecture, it shows that transcripts from an off-the-shelf ASR model (NVIDIA Conformer-Transducer) are good enough to train lipreading at scale. Adding automatically labelled English subsets of AVSpeech (1,323 h) and VoxCeleb2 (1,307 h) to LRS2/LRS3 brings training to 3,448 h; LRS3 VSR WER falls monotonically from 33.0% (818 h) to 19.1%, and LRS2 VSR reaches 14.6%. AV-ASR reaches 0.9% on LRS3 and ASR 1.0%, where gains saturate. The model is a ResNet-18 + Conformer encoder per modality with MLP fusion and a joint CTC/attention Transformer decoder; a Transformer LM helps VSR only. Noise experiments show the visual stream matters most at low SNR (e.g., white noise at -7.5 dB: 88.9% audio-only vs 24.2% AV). For SSI, the relevance is the visual-only VSR result and the recipe of pseudo-labelling to overcome labelled-data scarcity. Note that 19.1% is not the best prior VSR (ViT3D-CM reports 17.0% with about 90,000 h); the claim is data efficiency. All data are vocalized, frontal 'in-the-wild' broadcast/YouTube speech, so silent-speech lip motion and wearable camera viewpoints are not tested.

### Why it matters

Practical, reproducible recipe showing that automatic labels from public ASR models make large-scale lipreading training feasible with public data only.

### Prior state of the art

Best VSR systems depended on large non-public labelled corpora (tens of thousands of hours) or self-supervised pretraining.

### What changed

Uses pseudo-labelled public data to reach competitive VSR and state-of-the-art AV-ASR with 26x less data than the strongest non-public system.

### Position in the field

Widely used open baseline for visual and audio-visual speech recognition in the video section.

### Practical value

Released-style training recipe and models are a standard starting point for lip-based SSI front-ends and pretraining.

### Advanced

Training data scale via automatic labels; public-data VSR and AV-ASR benchmark performance; noise robustness of AV fusion.

### Unresolved

Silent (non-vocalized) speech; non-frontal or wearable camera views; non-English languages; speaker-specific adaptation.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | Visual-only, audio-only and audio-visual sentence-level speech recognition. |
| Input | Lip-region video and audio. |
| Sensor | Ordinary video camera and microphone recordings (LRS2, LRS3, VoxCeleb2, AVSpeech). |
| Body site | Lips / face (video). |
| Output | Text. |
| Vocabulary type | Open-vocabulary English, SentencePiece 5,000 units. |
| Vocabulary size | Open vocabulary; 3,448 h of training data. |
| Metrics and results | LRS3 VSR WER 19.1% (3,448 h) vs 33.0% (818 h); LRS3 ASR 1.0%; LRS3 AV-ASR 0.9% (prior AV-HuBERT 1.4%). LRS2 VSR 14.6%, ASR 1.5%, AV-ASR 1.5%. Pink noise -7.5 dB: A 56.8% vs AV 16.2%; white noise -7.5 dB: A 88.9% vs AV 24.2%. |
| Evaluation protocol | Offline benchmark evaluation on LRS2/LRS3 test sets with data-scaling and noise ablations. |

### Limits

- **Technical:** Pseudo-labels are noisy; pseudo-label quality does not track LibriSpeech WER, so ASR labeller choice is empirical; ASR performance saturates.
- **Evaluation:** Evaluated on LRS2/LRS3 benchmarks only; babble noise shared between training and testing may be optimistic; no silent-speech test set.
- **Deployment:** Large models trained on thousands of hours; no latency or on-device evaluation.
- **Scope of this review:** Read arXiv v3 PDF via automated extraction; Table 1 column labels were garbled in extraction so its per-column mapping was not used. Code/model availability not verified.

### Evidence

- Unlabelled AVSpeech and VoxCeleb2 are transcribed with public pre-trained ASR models (Conformer-Transducer selected) and combined with LRS2/LRS3 for training. (Sec. 2.1-2.2; Abstract)
- English-filtered AVSpeech contributes 1,323 h and VoxCeleb2 1,307 h; full training set totals 3,448 h. (Sec. 2.1; Table 2 caption)
- LRS3 VSR WER decreases from 33.0% (818 h) to 19.1% (3,448 h); ASR from 1.5% to 1.0%. (Sec. 4.2; Table 2)
- LRS3 AV-ASR reaches 0.9% WER versus 1.4% for AV-HuBERT; best prior VSR (ViT3D-CM) is 17.0% with about 90,000 h. (Table 4)
- LRS2 VSR WER is 14.6% with 3,448 h, compared with 22.6% for VTP. (Table 3)
- At -7.5 dB white noise, audio-only WER is 88.9% versus 24.2% audio-visual. (Table 5)
- Architecture: ResNet-18 front-ends with 12-layer Conformer encoders, MLP fusion and 6-layer Transformer decoder trained with joint CTC/attention; Transformer LM used only for VSR. (Sec. 2.3, 3.3)
- Pseudo-label quality is not correlated with LibriSpeech WER, ASR gains saturate, and babble noise is shared between train and test. (Sec. 4.1, 4.2, Table 5 discussion)

## More reviews in Lip & face video

- [Audio Knowledge Empowered Visual Speech Recognition](../akvsr-audio-knowledge-empowered-visual-speech-recognition-by-compressing-audio-knowledge-of-a-pretrained-model/) (2023). AKVSR improves visual speech recognition by transferring compressed linguistic knowledge from a pretrained audio model through a compact memory and cross-attention, without audio at inference. LRS3 WER drops from 46.1% to 41.6% (BASE).
- [Audio-visual video-to-speech synthesis with synthesized input audio](../audio-visual-video-to-speech-synthesis-with-synthesized-input-audio/) (2023). Adds synthesized audio from a first-stage video-to-audio model as an auxiliary input to a second-stage audiovisual video-to-speech model. Improves reconstruction quality and intelligibility on benchmarks, though gains vary by model and dataset.
- [High-Quality Automatic Voice Over with Accurate Alignment: Supervision through Self-Supervised Discrete Speech Units](../high-quality-automatic-voice-over-with-accurate-alignment-supervision-through-self-supervised-discrete-speech-units/) (2023). An automatic voice-over system that supervises alignment by predicting self-supervised discrete speech units from text and lip video, improving lip-sync and speech quality on a single-speaker dataset. Not an SSI paper.
- [Improving the Gap in Visual Speech Recognition Between Normal and Silent Speech Based on Metric Learning](../improving-the-gap-in-visual-speech-recognition-between-normal-and-silent-speech-based-on-metric-learning/) (2023). Viseme-level metric learning that aligns normal and silent speech representations to improve silent visual speech recognition, reaching baseline parity with much less silent data on AV Digits.
- [Intelligible Lip-to-Speech Synthesis with Speech Units](../intelligible-lip-to-speech-synthesis-with-speech-units/) (2023). Lip-to-speech synthesis using self-supervised speech units as a pseudo-text target plus a multi-input vocoder; substantially cuts WER without text labels and reports state-of-the-art results on LRS2/LRS3.
- [Large-scale unsupervised audio pre-training for video-to-speech synthesis](../large-scale-unsupervised-audio-pre-training-for-video-to-speech-synthesis/) (2023). Pretrains the decoder of a video-to-speech model on large audio-only corpora, improving reconstruction quality on GRID, TCD-TIMIT and LRW, though WER gains are not consistent.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
