# Audio-visual video-to-speech synthesis with synthesized input audio

Triantafyllos Kefalas, Yannis Panagakis, Maja Pantic  
arXiv / imported corpus page 2023 · [arXiv](https://arxiv.org/abs/2307.16584)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

Adds synthesized audio from a first-stage video-to-audio model as an auxiliary input to a second-stage audiovisual video-to-speech model. Improves reconstruction quality and intelligibility on benchmarks, though gains vary by model and dataset.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera (lip video) plus synthesized audio |
| Task | Speech synthesis from lip video |
| Vocabulary | Sentence-level benchmark vocabularies (size not stated) |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | WER 2.65% on GRID (33 seen speakers); WER 24.96% on LRW unseen speakers |

**Limitations.** Depends on first-stage synthesized audio quality; WER gains inconsistent; no in-the-wild, noisy or real-time evaluation.

## Full review

### In short

The paper credibly shows that incorporating synthesized audio as an auxiliary input in a second-stage audiovisual synthesis model improves video-to-speech reconstruction quality and intelligibility in benchmarks, though gains depend on model variant and dataset.

### Review

This paper presents a significant advance in video-to-speech synthesis by proposing and evaluating a two-stage approach that treats synthesized audio as an essential intermediate modality to enhance speech reconstruction from silent video. The AV2A architectures append a learnable audio encoder to a pretrained V2A model and are trained with modality dropout to prevent reliance on a single modality. Across benchmark datasets (GRID with 4 and 33 speakers, both seen and unseen, TCD-TIMIT lipspeakers, and LRW), AV2A models, particularly raw waveform V2A-WaveGAN variants with audio pretraining and modality dropout using ground-truth audio during training, consistently improve perceptual and intelligibility metrics (PESQ up to 2.10, STOI up to 0.723, ESTOI up to 0.553), with reductions in WER compared to base V2A models. However, improvements are not universal: some mel-spectrogram models underperform older baselines on certain datasets, and WER gains are modest or fluctuating, especially on unseen speaker splits. The work’s main contribution lies in demonstrating the feasibility and benefits of incorporating synthesized audio in a staged AV2A approach, with novel training methods to balance modalities. This overcomes traditional practices discarding audio at inference, framing synthesized audio as a useful intermediate representation. Nonetheless, limitations remain due to lack of real-time testing, reliance on benchmark datasets under clean conditions, and dependence on the quality of first-stage synthesized audio. The approach is promising for silent-video speech reconstruction research but requires further development and deployment-oriented evaluation for practical use.

### Why it matters

Demonstrates a novel two-stage audiovisual speech synthesis pipeline that leverages synthesized audio as an intermediate representation, trained with modality dropout, achieving improved objective metrics and enabling robust audiovisual speech reconstruction from silent videos.

### Prior state of the art

Most video-to-speech synthesis systems used either video only or included audio during training but discarded audio input at inference, treating missing audio as unavailable rather than as an explicit intermediate representation.

### What changed

Introduces a two-stage pipeline leveraging synthesized audio from a first-stage V2A model as explicit input to a second-stage AV2A model, trained with modality dropout to robustly combine video and audio modalities for speech reconstruction.

### Position in the field

A strong contribution to video-to-speech synthesis literature centered on staged audiovisual reconstruction incorporating synthesized audio.

### Practical value

Provides a benchmarked, replicable approach to combining synthesized audio with silent video for improved speech synthesis; relevant for researchers of audiovisual speech synthesis and multimodal enhancement.

### Advanced

system_design; evaluation

### Unresolved

impact of different training variants across datasets; live deployment suitability; correlation with real-time constraints; dependence on synthesized audio quality

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | Silent video plus synthesized audio |
| Sensor | camera |
| Body site | lip |
| Output | speech-audio |
| Vocabulary type | Sentence-level benchmark vocabularies |
| Metrics and results | GRID (4 speakers, seen): PESQ 1.95, STOI 0.698, ESTOI 0.532, WER 3.67%; GRID (33 speakers, seen): PESQ 2.10, STOI 0.723, ESTOI 0.553, WER 2.65%; TCD-TIMIT (3 lipspeakers, seen): PESQ 1.44, STOI 0.566, ESTOI 0.411; LRW unseen: WER down to 24.96% in best raw waveform models; metrics reported include PESQ, STOI, ESTOI, WER. |
| Evaluation protocol | Multi-dataset quantitative benchmark comparison with multiple training variants and modalities in raw waveform and mel-spectrogram domains, including seen and unseen speaker splits. |

### Limits

- **Technical:** Effectiveness depends on the quality of synthesized audio from the first-stage V2A model; WER improvements are inconsistent across datasets and model variants; no demonstrated results for in-the-wild noisy conditions or real-time inference.
- **Evaluation:** Objective metrics (PESQ, STOI, ESTOI, WER) on benchmark datasets; lack of in-the-wild, noisy environment, or real-time latency evaluations; WER unavailable for TCD-TIMIT due to lack of suitable pre-trained ASR models.
- **Deployment:** Benchmark evaluations only; relies on pretrained base models; no real-time or latency evaluation; no in-the-wild or noisy environment testing; dependency on quality of synthesized audio inputs.
- **Scope of this review:** Applies to video-to-audio reconstruction tasks in benchmark datasets with limited speaker diversity and controlled conditions; does not address noisy or real-time conditions.

### Evidence

- In this work we investigate video-to-speech synthesis models that include audio and video inputs during both training and inference. We do so in both the raw waveform and mel spectrogram domains. (Abstract)
- We propose a video-to-speech synthesis approach that employs audio and video inputs during both training and inference by transforming the V2A model into a corresponding AV2A model, using the V2A model to synthesize the input audio, and training under modality dropout. (I. INTRODUCTION)
- We construct the audio-visual-to-audio Generator by appending an audio encoder to the video-to-audio Generator, which receives the synthesized audio as input and concatenates audio and video features with a speaker embedding before feeding to temporal and decoding modules. (III. RAW WAVEFORM MODELS)
- Experiments evaluate the models on GRID in seen speaker splits with 4 and 33 speakers, on unseen GRID with 33 speakers, on TCD-TIMIT lipspeakers, and on LRW in an unseen speaker setting. (V. EXPERIMENTAL METHODOLOGY)
- On GRID 4-speaker seen split, the best AV2A-WaveGAN model with audio pretraining and modality dropout using ground truth audio achieved PESQ 1.95, STOI 0.698, ESTOI 0.532, and WER 3.67 percent, outperforming base V2A-WaveGAN and other baselines. (VI. RESULTS)
- On GRID 33-speaker seen split, AV2A-WaveGAN with audio pretraining and modality dropout (GT audio) achieved PESQ 2.10, STOI 0.723, ESTOI 0.553, and WER 2.65, surpassing the base V2A-WaveGAN and several prior methods. (VI. RESULTS)
- For TCD-TIMIT with 3 lipspeakers (seen), AV2A-WaveGAN with audio pretraining and modality dropout (GT audio) reached PESQ 1.44, STOI 0.566, ESTOI 0.411. (VI. RESULTS)
- The paper relies on objective metrics and WER across benchmark corpora, and WER is unavailable for TCD-TIMIT as no accurate pre-trained ASR model could be found. (V. EXPERIMENTAL METHODOLOGY)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
