# SVTS: Scalable Video-to-Speech Synthesis

Rodrigo Mira, Alexandros Haliassos, Stavros Petridis, Björn W. Schuller, Maja Pantic  
arXiv / imported corpus page 2022 · [arXiv](https://arxiv.org/abs/2205.02058)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

SVTS shows a simple spectrogram predictor with a pretrained vocoder outperforms prior complex video-to-speech models and scales to large datasets such as LRS3+VoxCeleb2.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera (lip video) |
| Task | Speech synthesis from lip video |
| Vocabulary | GRID 51, LRW 500, LRS3 >50,000 words |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Not reported |

**Limitations.** Depends on large curated aligned datasets; weaker on unseen speakers and unconstrained conditions; no LRS3 WER or user study.

## Full review

### In short

A key scaling contribution that demonstrates simple spectrogram prediction plus pretrained vocoder pipelines outperform prior complex models on diverse datasets, marking foundational progress in large-scale video-to-speech synthesis.

### Review

This work provides a pragmatically designed and thoroughly evaluated video-to-speech system prioritizing scalability. It employs a clean architectural split—video-to-spectrogram predictor using ResNet18 plus conformers, paired with a pretrained Parallel WaveGAN vocoder—favoring ease of training on large unlabeled audiovisual corpora. The method beats prior art on popular benchmarks like GRID and LRW and achieves intelligible speech on challenging datasets like LRS3, with further improvements shown when scaling training data by incorporating VoxCeleb2. While it does not solve deployment challenges in-the-wild, it marks an important shift in the field toward prioritizing data scale and simplicity rather than complex loss engineering or small-data-specific approaches, providing a strong baseline for large-scale visual silent speech research.

### Why it matters

Establishes a practical, scalable video-to-speech baseline capable of leveraging large, unconstrained datasets (notably LRS3+VoxCeleb2) with competitive intelligibility, shifting the field from intricate small-dataset loss engineering to data-driven scaling.

### Prior state of the art

Previous video-to-speech methods typically relied on small, constrained datasets, complex loss functions, and architectures that scaled poorly to large, diverse datasets.

### What changed

Shifts towards simpler, scalable architectures using a two-stage spectrogram prediction plus pretrained vocoder pipeline; demonstrates results on large, less constrained datasets such as LRW and especially LRS3.

### Position in the field

Foundational large-scale video-to-speech paper, demonstrating scalability and strong baseline for lip-based silent speech reconstruction relevant to SSI modalities.

### Practical value

Provides a reliable, scalable video-to-speech system useful as a baseline for future research and a blueprint emphasizing data scale over complex losses; useful especially for those seeking to develop large-scale silent speech interfaces.

### Advanced

system_design; deployment; evaluation

### Unresolved

In-the-wild robustness; higher fidelity on unconstrained data

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | video |
| Sensor | camera |
| Body site | lip |
| Output | speech-audio |
| Vocabulary type | word- and sentence-level audiovisual speech |
| Vocabulary size | GRID (51 words), LRW (500 words), LRS3 (>50,000 words), LRS3+VoxCeleb2 (~1,500+ hours data) |
| Metrics and results | PESQ, STOI, ESTOI, and WER evaluated on generated speech with pretrained ASR models; GRID and LRW WER reported, but no WER for LRS3 due to ASR unreliability; vocoder speed measured in clips/second; loss function ablations measured by same metrics. |
| Evaluation protocol | Quantitative benchmark evaluations and ablation studies including vocoder and loss comparisons. |

### Limits

- **Technical:** Dependent on large curated audiovisual datasets; lower fidelity and intelligibility on unseen speakers and unconstrained conditions; no demonstration of robustness to in-the-wild variation; ASR evaluation limitations on complex datasets.
- **Evaluation:** No user studies or open-vocabulary ASR-based WER for LRS3 due to ASR unreliability on generated audio; evaluation focused on seen and unseen speakers splits on standard datasets.
- **Deployment:** Requires reasonably cropped, aligned lip video and substantial, curated audiovisual training data; no unconstrained deployment validation yet.
- **Scope of this review:** Limited to lip-video to speech reconstruction, does not address cross-modal or other silent speech modalities.

### Evidence

- We introduce a scalable video-to-speech framework consisting of two components: a video-to-spectrogram predictor and a pre-trained neural vocoder, which converts the mel-frequency spectrograms into waveform audio, achieving state-of-the-art results on GRID and LRW, and intelligible results on LRS3. (Abstract)
- Our model uses a simpler, scalable predictor/vocoder split, with a ResNet18+conformer video-to-spectrogram predictor trained on scaled training data, combined with a pretrained Parallel WaveGAN vocoder; this enables efficient and scalable training unlike more complex architectures or bespoke loss engineering of prior work. (2. Methodology)
- We evaluate on the small GRID dataset (27 hours), medium-scale LRW (around 150 hours), the challenging large-scale LRS3 corpus (312 hours), and a combined LRS3+VoxCeleb2 corpus exceeding 1,500 hours, with seen and unseen speaker splits where applicable. (3. Experimental setup)
- Quantitative evaluation metrics include PESQ, STOI, ESTOI for speech quality and intelligibility assessment, as well as WER measured using pretrained ASR models on generated audio for GRID and LRW; WER on LRS3 was not reported due to ASR unreliability on generated samples. (3.4. Evaluation metrics)
- Parallel WaveGAN neural vocoder outperforms Griffin-Lim and other neural vocoders on all evaluation metrics and runs significantly faster (around 54.7 clips/sec on GRID with Nvidia RTX 2080 Ti) enabling efficient waveform synthesis during inference. (4.2. Ablations)
- SVTS achieves on GRID seen speakers PESQ 1.97, STOI 0.705, ESTOI 0.523, and WER 2.36%; on GRID unseen speakers PESQ 1.40, STOI 0.588, ESTOI 0.318, and WER 17.85%; on LRW unseen speakers PESQ 1.49, STOI 0.649, ESTOI 0.483, and WER 13.4%. LRS3 tasks yield intelligible results without reported WER. (4.1. Experiments)
- The approach depends on large, curated audiovisual datasets and trained models do not yet achieve high fidelity or robustness on unconstrained unseen data, with ASR evaluation unreliable on LRS3 generated speech and no user studies reported. (4. Results)
- Deployment requires cropped and aligned lip video input and substantial training data; real-time usage is plausible given vocoder speed but not explicitly validated; end-user deployment requires further robustness and validation. (2. Methodology)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
