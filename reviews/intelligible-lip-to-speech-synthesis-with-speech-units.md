# Intelligible Lip-to-Speech Synthesis with Speech Units

['', '', '']  
arXiv / imported corpus page 2023 · [arXiv](https://arxiv.org/abs/2305.19603)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

Lip-to-speech synthesis using self-supervised speech units as a pseudo-text target plus a multi-input vocoder; substantially cuts WER without text labels and reports state-of-the-art results on LRS2/LRS3.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Lip video (optional AV-HuBERT visual front-end) |
| Task | Speech synthesis from lip video |
| Vocabulary | Open vocabulary (LRS2/LRS3) |
| Speaker | Speaker-independent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Not reported |

**Limitations.** Evaluated only on LRS2/LRS3 test sets with a 15-rater MOS study; no robustness to pose, occlusion, or lighting, and no latency or on-device analysis.

## Full review

### In short

Speech units as a pseudo-text target enable strong content supervision that substantially cuts WER without text labels, and the multi-input vocoder improves speech quality from blurry mel outputs, yielding a state-of-the-art lip-to-speech system on LRS benchmarks.

### Review

This paper presents a significant advancement in lip-to-speech synthesis by combining self-supervised quantized speech units as auxiliary prediction targets with a multi-input vocoder that conditions on both mel-spectrograms and speech units. This architecture allows improved speech content modeling without text labels, a key bottleneck in prior work. Experimental results on LRS3 and LRS2 benchmarks demonstrate clear metric improvements, notably a reduction in word error rate (WER) from 65.8% to 29.8% when using a strong AV-HuBERT visual encoder plus speech units. The vocoder design, augmented during training with blur and noise, further enables intelligible speech synthesis from blurry predicted mel features. Human evaluations confirm gains in naturalness, intelligibility, and clearness relative to prior state of the art. Despite these merits, the work remains benchmark-focused without investigation of real-time operation, mobile compatibility, or robustness to real-world video variations such as occlusion or pose changes. The approach significantly moves the field towards practical lip-to-speech reconstruction by eliminating reliance on text labels, but future work must address deployment and generalization challenges.

### Why it matters

A strong contribution to video-based speech reconstruction that eliminates the need for paired text transcriptions by leveraging self-supervised speech units, enabling intelligible speech synthesis with improved content fidelity. The multi-input vocoder innovation also materially enhances waveform quality from predicted features.

### Prior state of the art

Lip-to-speech models typically either use blurry acoustic targets alone for supervision or require paired text labels as stronger content guidance.

### What changed

Uses discrete speech units derived via speech model quantization as pseudo-text supervision to the multi-target L2S model, enabling improved content modeling without text labels; additionally, uses speech units to condition a multi-input vocoder for waveform generation, enhancing intelligibility and speech quality.

### Position in the field

Core video-to-speech / silent-speech reconstruction work utilizing self-supervised speech units for content modeling.

### Practical value

High practical value in constructing lip-to-speech models when paired text labels are unavailable, improving intelligibility significantly on standard benchmarks.

### Advanced

content_supervision; vocoder_design; reconstruction_intelligibility

### Unresolved

live_inference; occlusion_robustness; unconstrained_capture

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | video |
| Sensor | Lip video with visual front-end optionally replaced by AV-HuBERT models pretrained on LRS3 and VoxCeleb2 |
| Body site | lip |
| Output | speech-audio |
| Metrics and results | Metrics used include STOI, ESTOI, PESQ, and Word Error Rate (WER) on LRS2 and LRS3 datasets, plus Mean Opinion Score (MOS) for naturalness, intelligibility, and clearness based on human raters. |
| Evaluation protocol | Quantitative evaluation on standard benchmarks (LRS2, LRS3) using STOI, ESTOI, PESQ, WER metrics and a small-scale human Mean Opinion Score (MOS) study. |

### Limits

- **Technical:** Limited by dependence on benchmark video quality, vocoder stack complexity, and residual challenge in matching natural speech quality; no tested robustness to pose, occlusion, or spontaneous environment variability.
- **Evaluation:** Evaluation is limited to test sets from LRS2 and LRS3 datasets, with no cross-dataset or live deployment exploration; human evaluation is limited to 15 participants rating MOS on 20 samples.
- **Deployment:** No latency analysis, on-device implementation, or in-the-wild robustness to camera position/lighting/occlusion is demonstrated, limiting immediate real-world deployment.
- **Scope of this review:** Focuses strictly on lip-to-speech synthesis (speech reconstruction) without addressing text entry, command recognition, or speech enhancement. Evaluation confined to standard benchmarks LRS2 and LRS3.

### Evidence

- We propose a novel Lip-to-Speech synthesis (L2S) framework that uses quantized self-supervised speech representations, named speech units, as an additional prediction target alongside mel-spectrogram, allowing strong content supervision without text labels, and introduce a multi-input vocoder conditioned on mel-spectrogram and speech units to generate clear waveforms even from noisy mel-spectrograms. (Abstract)
- The main technical advance is treating quantized speech units as pseudo-text supervision during training and conditioning the multi-input vocoder on both mel-spectrogram and these speech units to improve speech content fidelity and waveform quality without relying on text labels. (2.2. Multi)
- On LRS3 dataset, the proposed method achieves STOI=0.578, ESTOI=0.393, PESQ=1.31, and WER=29.8%, substantially outperforming Multi-Task baseline WER of 65.8%. On LRS2, it reaches STOI=0.585, ESTOI=0.412, PESQ=1.34, and WER=35.7%, again improving over previous methods, as reported in Tables 1 and 2. (4.1 Quantitative Comparison)
- Evaluation is performed on LRS2 and LRS3 large-scale sentence-level lip-to-speech datasets with thousands of speakers in natural and wild environments; human MOS evaluation involved 15 participants rating naturalness, intelligibility, and clearness on 20 test samples from LRS3. (3.1 Datasets)
- The approach depends on quality of benchmark video datasets (LRS2 and LRS3) and the vocoder stack complexity; the synthesized speech audio quality remains far from natural speech and no evaluation on real-world deployment scenarios, occlusion robustness, or user mobility has been conducted. (4 Results)
- No latency analysis, on-device deployment, or robustness under uncontrolled camera settings has been demonstrated; thus, deployment readiness for real-world applications remains limited despite benchmark performance gains. (5 Conclusions)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
