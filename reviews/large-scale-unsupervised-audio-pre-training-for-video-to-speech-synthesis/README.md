# Large-scale unsupervised audio pre-training for video-to-speech synthesis

Triantafyllos Kefalas, Yannis Panagakis, Maja Pantic  
arXiv 2023 · [arXiv](https://arxiv.org/abs/2306.15464)

**Section:** [Lip & face video](../../README.md#lip--face-video) · **Review basis:** full_text

A structured review of *Large-scale unsupervised audio pre-training for video-to-speech synthesis* (Triantafyllos Kefalas et al., arXiv 2023) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Pretrains the decoder of a video-to-speech model on large audio-only corpora, improving reconstruction quality on GRID, TCD-TIMIT and LRW, though WER gains are not consistent.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera (mouth-region video) |
| Task | Speech synthesis from lip video |
| Vocabulary | Not stated |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | PESQ 1.26-2.07, STOI 0.49-0.72, WER 2.66%-42.38% across GRID, TCD-TIMIT, LRW splits |

**Limitations.** WER improvements not consistent; objective benchmark metrics only, with no human listening tests, latency or real-world robustness evaluation.

## Full review

### In short

Good decoder-transfer pretraining improves video-to-speech quality on several benchmarks, but WER gains are not consistent. A useful methodological contribution with strong benchmark support, adjacent to SSI rather than a deployable system.

### Review

This paper methodologically advances video-to-speech synthesis by proposing an audio-to-audio pretraining stage on large audio-only speech corpora, which initializes the decoder in video-to-speech models. The authors design two encoder-decoder models generating either raw waveforms or mel spectrograms and pretrain corresponding audio-to-audio models on 3572 hours of diverse English speech data. Fine-tuning on several benchmarks under seen and unseen speaker conditions shows the pretraining improves perceptual quality and intelligibility metrics in many cases, though not uniformly across all. The approach reframes the data scarcity issue in video-to-speech by leveraging abundant audio-only corpora, a significant departure from canonical paired audio-visual training. Architectural improvements like batch normalization adaptation for cross-modal fine-tuning bolster the transfer. However, the work is a benchmark-method contribution evaluated only with objective offline metrics, lacking latency, robustness, or user studies, and with some inconsistent WER gains. It is valuable for data-efficient video-to-speech reconstruction research adjacent to SSI, rather than a ready interface.

### Why it matters

A valuable decoder-initialization and pretraining study allowing large audio-only corpora to improve video-to-speech reconstruction quality, advancing data efficiency in cross-modal speech synthesis.

### Prior state of the art

Video-to-speech systems largely rely on paired audio-visual data, limiting the use of large audio-only corpora.

### What changed

Moves decoder learning into an audio-only pretraining stage and transfers it back into video-to-speech.

### Position in the field

Strong adjacent reconstruction paper.

### Practical value

Useful when paired audio-visual data are scarce but large audio-only speech corpora exist; improves decoder initialization and speech reconstruction quality.

### Advanced

decoder_pretraining; audio_only_transfer; reconstruction_quality

### Unresolved

consistent_wer_gains; live_capture; deployment_latency

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | video |
| Sensor | Video input plus large-scale audio-only corpora used in pretraining; video from mouth region extraction; pretrained face/speaker embeddings for identity |
| Body site | lip |
| Output | speech-audio |
| Metrics and results | Objective reconstruction metrics: PESQ (1.26-2.07), STOI (0.49-0.72), ESTOI (0.20-0.53), and WER (2.66% to 42.38%) measured on GRID, TCD-TIMIT, LRW datasets for seen and unseen speaker splits; comparison to prior works such as WGAN and SVTS included; multiple cross-modal fine-tuning strategies evaluated. |
| Evaluation protocol | Seen and unseen speaker evaluation on GRID, TCD-TIMIT, and LRW datasets, with quantitative metrics (PESQ, STOI, ESTOI, WER) |

### Limits

- **Technical:** Pretraining does not reliably improve WER uniformly; benchmark audio quality remains modest; model complexity and latency implications not analyzed.
- **Evaluation:** Benchmark evaluation on standard datasets with objective metrics only; no human perceptual tests or deployment contexts evaluated.
- **Deployment:** No latency or real-world capture robustness study is given. No evidence of real-time deployment or joint visual robustness under diverse conditions.
- **Scope of this review:** Focus on video-to-speech waveform and mel spectrogram reconstruction only; no text-entry or command recognition addressed.

### Evidence

- In this paper we propose to train encoder-decoder models on more than 3,500 hours of audio data at 24kHz, and then use the pre-trained decoders to initialize the audio decoders for the video-to-speech synthesis task. (Abstract)
- We pre-train the audio-to-audio models on a combination of speech corpora in an unsupervised manner and use these pre-trained models to initialize and fine-tune the corresponding video-to-audio models. (III. VIDEO)
- We propose a modification to the batch normalization module which enables cross-modal parameter fine-tuning by keeping track of separate running statistics for the audio and video modalities. We apply this to the batch normalization layers of the decoder. (III. VIDEO)
- We conduct experiments on popular audio-visual datasets on seen (GRID, TCD-TIMIT) and unseen (GRID, LRW) speakers. (I. INTRODUCTION)
- On GRID unseen, V2A-MelSpec-S-SP + fine-tuning reaches PESQ 1.43, STOI 0.598, ESTOI 0.335, and WER 17.90; on LRW, V2A-MelSpec-M-SP trained from scratch reaches 1.48, 0.649, 0.484, and 14.96, showing pretraining helps quality but not always WER. (VI. RESULTS)
- No latency or real-world capture robustness study is given, so deployment readiness is limited. (VII. CONCLUSION)
- Pretraining does not uniformly improve WER and benchmark audio quality is still modest. (VI. RESULTS)
- All evidence is benchmark-based with no live interface or user-facing deployment. (VII. CONCLUSION)

## More reviews in Lip & face video

- [Audio Knowledge Empowered Visual Speech Recognition](../akvsr-audio-knowledge-empowered-visual-speech-recognition-by-compressing-audio-knowledge-of-a-pretrained-model/) (2023). AKVSR improves visual speech recognition by transferring compressed linguistic knowledge from a pretrained audio model through a compact memory and cross-attention, without audio at inference. LRS3 WER drops from 46.1% to 41.6% (BASE).
- [Audio-visual video-to-speech synthesis with synthesized input audio](../audio-visual-video-to-speech-synthesis-with-synthesized-input-audio/) (2023). Adds synthesized audio from a first-stage video-to-audio model as an auxiliary input to a second-stage audiovisual video-to-speech model. Improves reconstruction quality and intelligibility on benchmarks, though gains vary by model and dataset.
- [Auto-AVSR: Audio-Visual Speech Recognition with Automatic Labels](../auto-avsr-audio-visual-speech-recognition-with-automatic-labels/) (2023). Training lipreading and AV-ASR on 3,448 h including ASR-pseudo-labelled AVSpeech and VoxCeleb2 cuts LRS3 visual-only WER to 19.1% and audio-visual WER to 0.9%.
- [High-Quality Automatic Voice Over with Accurate Alignment: Supervision through Self-Supervised Discrete Speech Units](../high-quality-automatic-voice-over-with-accurate-alignment-supervision-through-self-supervised-discrete-speech-units/) (2023). An automatic voice-over system that supervises alignment by predicting self-supervised discrete speech units from text and lip video, improving lip-sync and speech quality on a single-speaker dataset. Not an SSI paper.
- [Improving the Gap in Visual Speech Recognition Between Normal and Silent Speech Based on Metric Learning](../improving-the-gap-in-visual-speech-recognition-between-normal-and-silent-speech-based-on-metric-learning/) (2023). Viseme-level metric learning that aligns normal and silent speech representations to improve silent visual speech recognition, reaching baseline parity with much less silent data on AV Digits.
- [Intelligible Lip-to-Speech Synthesis with Speech Units](../intelligible-lip-to-speech-synthesis-with-speech-units/) (2023). Lip-to-speech synthesis using self-supervised speech units as a pseudo-text target plus a multi-input vocoder; substantially cuts WER without text labels and reports state-of-the-art results on LRS2/LRS3.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
