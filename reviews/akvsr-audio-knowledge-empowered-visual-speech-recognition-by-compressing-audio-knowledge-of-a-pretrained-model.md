# Audio Knowledge Empowered Visual Speech Recognition

Jeong Hun Yeo, Minsu Kim, Jeongsoo Choi, Dae Hoe Kim, Yong Man Ro  
arXiv / imported corpus page 2023 · [arXiv](https://arxiv.org/abs/2308.07593)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

AKVSR improves visual speech recognition by transferring compressed linguistic knowledge from a pretrained audio model through a compact memory and cross-attention, without audio at inference. LRS3 WER drops from 46.1% to 41.6% (BASE).

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera (lip video) |
| Task | Visual speech recognition (lip reading) |
| Vocabulary | Open vocabulary sentences (LRS2/LRS3) |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | LRS3 WER 41.6% vs 46.1% baseline (BASE); LARGE reaches 23.6% with augmented data |

**Limitations.** Requires offline audio memory construction before training; benchmark-only evaluation without live, real-time or latency testing.

## Full review

### In short

The paper advances visual speech recognition by selectively transferring refined linguistic audio knowledge via a learned compact memory and cross-attention injection, improving benchmark WERs over prior audio-assisted methods without requiring audio inputs during inference.

### Review

This paper presents a strong technical contribution to visual speech recognition by leveraging large-scale pretrained audio models while addressing the key challenge that audio features contain speaker and noise characteristics detrimental to VSR. By vector quantization and clustering, the method isolates linguistic content into discrete memory slots. The ABM uses cross-attention to retrieve matched memory entries per visual frame, allowing purely video-based inference without audio inputs. The effectiveness is demonstrated across LRS2 and LRS3 datasets with up to 433 hours of labeled data and VoxCeleb2 pseudo-label augmentations. The proposed system improves WER from a baseline 46.1% to 41.6% with the BASE model and achieves state-of-the-art levels with LARGE models, outperforming previous methods including AV-HuBERT and RAVEn. Ablations illustrate key design choices, such as the dimensionality of the audio memory, the optimal number of clusters (200), the benefit of removing non-linguistic factors over naive distillation methods, and ABM cross-attention layers (2 layers best). However, the system currently requires offline memory construction before training, and lacks assessments in real-time, streaming, or real-world multi-speaker/noise environments, limiting deployment readiness. The paper strengthens the baseline of audio-empowered VSR by emphasizing selective linguistic knowledge transfer, but remains focused on sentence-level benchmark scenarios.

### Why it matters

Demonstrates that eliminating non-linguistic factors in audio knowledge transfer and using a trainable discrete memory combined with cross-attention bridging significantly improves VSR performance, offering a more principled and effective audio-to-video knowledge transfer than prior naive distillation or feature concatenation methods.

### Prior state of the art

Existing VSR methods have started to incorporate audio knowledge through distillation or multimodal memory to complement insufficient visual signals, but often retain speaker and noise factors or require audio inputs during inference.

### What changed

Transforms pretrained audio features into compact discrete memory removing non-linguistic components, then injects this linguistic memory into VSR via ABM cross-attention that operates without audio inputs at training or inference, improving selective audio knowledge transfer over previous audio-assisted VSR methods.

### Position in the field

Strong recent visual speech recognition paper that shows an effective refined audio knowledge transfer that outperforms naive distillation and auxiliary tasks on standard sentence-level benchmarks.

### Practical value

Enhances visual speech-to-text performance by importing linguistic audio features in a compact, selective form without needing audio during inference, useful for lip-reading systems seeking audio-pretraining benefits.

### Advanced

system_design; evaluation

### Unresolved

real-time deployment; preprocessing cost of memory construction; broader interface relevance beyond sentence-level VSR

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-recognition |
| Input | video (silent lip movement) |
| Sensor | camera |
| Body site | lip |
| Output | text |
| Vocabulary type | sentence-level open vocabulary |
| Metrics and results | WERs on LRS3: baseline 46.1%, AKVSR-HuBERT 41.6% (BASE) and for LARGE 29.1% (30h), 27.6% (433h), 23.6% (augmented); similar WER improvements on LRS2; comparison against prior SOTA with larger datasets; ablations detailed in Tables III–IX. |
| Evaluation protocol | Quantitative WER comparison on LRS2 and LRS3 visual speech recognition benchmarks, including multiple ablation experiments over choice of pretrained audio model (CPC, wav2vec2.0, HuBERT), memory cluster size, embedding dimension, ABM cross-attention layers, and training dataset sources. |

### Limits

- **Technical:** Offline compact audio memory construction required before training VSR; increases preprocessing cost and complexity; no real-time or streaming validation; no latency reported.
- **Evaluation:** Evaluations are benchmark WER measures on LRS2 and LRS3 datasets using only video inputs at inference; no live or real-time demonstrations; performance gains demonstrated via multiple ablation studies but no external data or environment tests.
- **Deployment:** Requires offline compact audio memory construction stage prior to VSR training; no evidence for real-time or embedded deployment; limited to sentence-level benchmarks without live camera or latency studies.
- **Scope of this review:** Sentence-level visual speech recognition on public datasets LRS2 and LRS3; no live or streaming experiments; no multi-environment or multi-speaker live deployment tested.

### Evidence

- We propose an Audio Knowledge empowered Visual Speech Recognition framework (AKVSR) which (1) utilizes rich audio knowledge encoded by a large-scale pretrained audio model, (2) saves the linguistic information by discarding non-linguistic information through quantization in compact audio memory, and (3) includes Audio Bridging Module which finds best-matched audio features from compact audio memory for training without audio inputs once the memory is composed. (Abstract)
- The proposed method stores refined linguistic audio knowledge in a compact discrete memory obtained by vector quantization from a pretrained audio model (HuBERT) and injects matched memory information into visual features via cross-attention in the Audio Bridging Module (ABM), obviating the need for audio inputs during training or inference. (C)
- Table I shows the baseline visual speech recognition WER on LRS3 is 46.1%, while AKVSR with HuBERT-based compact audio memory reduces it to 41.6% (BASE Transformer), with further improvements in LARGE models (29.1%, 27.6%, 23.6%) surpassing AV-HuBERT and previous state of the art without language models during inference. (27.6%)
- Table II on LRS2 confirms the proposed method improves WER over AV-HuBERT across Transformer BASE and LARGE models in low-resource (28h) and high-resource (223h) settings, e.g. from 32.2% to 28.7% WER in LARGE with 28h labeled data and from 25.5% to 24.1% in 223h data. (high)
- Experiments are performed on the sentence-level LRS2 and LRS3 datasets, including low-resource and high-resource labeled data splits, as well as pseudo-annotated VoxCeleb2 additions to extend training data. (resource)
- The method is evaluated strictly on benchmark datasets with WER as metric; there is no real-time or live camera study, and no latency analysis presented. (VII. Discussion)
- The proposed method requires an offline stage to build the compact audio memory before training the VSR model, which adds preprocessing time and complexity, making real-time deployment currently unavailable. (VII. Discussion)
- The evaluation is limited to sentence-level visual speech recognition benchmarks LRS2 and LRS3; there is no demonstration of generalization to real-world conditions, streaming, multi-speaker, or noisy environments. (VII. Discussion)
- The key novelty is explicitly removing speaker and noise characteristics from the pretrained audio model's features via vector quantization and storing linguistic content in discrete clusters, then retrieving matched audio memory contents via cross-attention ABM injecting purely video-conditioned audio knowledge during VSR training and inference. (C)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
