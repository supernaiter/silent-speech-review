# Improving Neural Silent Speech Interface Models by Adversarial Training

Amin Honarmandi Shandiz, László Tóth, Gábor Gosztolya, Alexandra Markó, Tamás Gábor Csapó  
arXiv 2021 · [DOI](https://doi.org/10.1007/978-3-030-76346-6_39) · [arXiv](https://arxiv.org/abs/2104.11601)

**Section:** [Ultrasound & tongue imaging](../../README.md#ultrasound--tongue-imaging) · **Review basis:** full_text

A structured review of *Improving Neural Silent Speech Interface Models by Adversarial Training* (Amin Honarmandi Shandiz et al., arXiv 2021) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Adds adversarial (GAN) loss to MSE training of a 3D CNN for ultrasound-to-mel-spectrogram mapping, giving modest objective quality improvements on Hungarian and English single-speaker corpora.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Micro ultrasound probe under the chin (tongue) |
| Task | Speech synthesis from ultrasound |
| Vocabulary | Not applicable |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Not reported |

**Limitations.** Modest objective-only gains on single-speaker corpora with limited data; no listening tests, real-time operation or multi-speaker robustness.

## Full review

### In short

A clean, well-executed incremental advance using GAN loss to modestly improve articulatory-to-acoustic mapping from ultrasound, validated objectively on two single-speaker corpora.

### Review

This paper demonstrates an incremental but methodologically sound improvement to ultrasound tongue imaging-based neural silent speech interfaces by adding adversarial training with a Patch-GAN discriminator to a 3D CNN generator. Tested on two single-speaker corpora (Hungarian and English), the combined MSE and adversarial loss yields consistent albeit small gains across multiple objective metrics (STOI, PESQ, MCD, SI-SDR etc.). Although there is no subjective listening test, the rigorous objective evaluation supports the claim that adversarial loss serves as a useful perceptual quality proxy improving articulatory-to-acoustic mappings. The contribution is primarily an improved training objective rather than novel model architecture or multi-speaker evaluation. Deployment is limited by speaker dependency and lack of real-time or robustness analysis.

### Why it matters

Demonstrates that combining adversarial loss with MSE training of a 3D CNN generator improves objective speech quality metrics in ultrasound-to-speech mapping, providing a justified but modest quality improvement without architectural novelty.

### Prior state of the art

Ultrasound-to-speech systems typically train models using MSE loss, which does not align well with perceptual speech quality; 3D CNN architectures were previously effective generators without adversarial losses.

### What changed

Adds a Patch-GAN discriminator and adversarial loss combined with MSE to improve quality without changing the generator architecture, trained on synchronized ultrasound and speech spectral data.

### Position in the field

Training-objective refinement for speaker-dependent ultrasound-based silent speech interfaces.

### Practical value

Useful for existing 3D CNN ultrasound-to-speech systems seeking small improvements in objective quality metrics, but not immediately deployable for practical applications.

### Advanced

Training objective - introducing adversarial loss beyond conventional MSE regression; Evaluation metric consistency across multiple speech quality and intelligibility metrics.

### Unresolved

Larger perceptual gains beyond incremental improvements; multi-speaker and real-world robustness; subjective listening test validation.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | ultrasound |
| Sensor | Ultrasound probe (Micro system by Articulate Instruments Ltd.) positioned under the chin for tongue imaging in midsagittal plane. |
| Body site | tongue |
| Output | speech-audio |
| Metrics and results | Mean squared error (MSE), mean R2 score, Short-Time Objective Intelligibility (STOI), extended STOI (ESTOI), Perceptual Evaluation of Speech Quality (PESQ), Scale-Invariant Signal-to-Distortion Ratio (SI-SDR), Signal-to-Distortion Ratio (SDR), Perceptual Metric for Speech Quality Evaluation (PMSQE), Mel-Cepstral Distortion (MCD). |
| Evaluation protocol | Objective quality metrics comparing MSE vs GAN training on held-out test data for Hungarian and English corpora. |

### Limits

- **Technical:** Limited training data per speaker; only single-speaker corpora; modest objective metric improvements; no subjective perceptual validation.
- **Evaluation:** No subjective listening tests; limited to single-speaker datasets; only objective speech quality and intelligibility metrics reported.
- **Deployment:** Speaker-dependent setup; no evidence of real-time operation or multi-speaker robustness; offline evaluation only.
- **Scope of this review:** Focus on speaker-dependent ultrasound to mel-spectrogram articulatory-to-speech reconstruction; no multi-speaker or real-time analysis.

### Evidence

- The paper applies GAN-style adversarial training to ultrasound-based articulatory-to-acoustic mapping and compares it against pure MSE training for silent speech interface models. (Abstract)
- We extend the conventional MSE training loss with an adversarial loss component provided by a Patch-GAN discriminator network to improve perceptual speech quality in articulatory-to-acoustic mapping from ultrasound data. (3 Generative Adversarial Networks for Articulatory-to-Acoustic Mapping)
- Evaluation metrics include MSE, R2, STOI, ESTOI, PESQ, SI-SDR, SDR, PMSQE, and MCD, demonstrating consistent albeit slight improvements in all metrics for both Hungarian and English corpora when using GAN training versus MSE-only training. (5 Results)
- Experiments used two single-speaker corpora: a Hungarian female speaker with 438 sentences and the TAL1 English subset with 1015 train, 50 dev, and 24 test utterances, focusing on speaker-dependent ultrasound-to-speech reconstruction. (4 Experimental Set-Up)
- The system is limited by the lack of listening tests, multi-speaker evaluation, real-time operation evidence, speaker-independence, and practical deployment readiness. (5 Results)
- The training framework operates offline on lab-recorded single-speaker ultrasound data with no real-time demonstration or multi-speaker generalization. (6 Conclusions)

## More reviews in Ultrasound & tongue imaging

- [3D Convolutional Neural Networks for Ultrasound-Based Silent Speech Interfaces](../3d-convolutional-neural-networks-for-ultrasound-based-silent-speech-interfaces/) (2021). Shows a compact (2+1)D 3D CNN outperforms 2D CNN and CNN+LSTM models for regressing 13 vocoder parameters from ultrasound tongue video, with lower complexity and training time.
- [Convolutional Neural Network-Based Age Estimation Using B-Mode Ultrasound Tongue Image](../convolutional-neural-network-based-age-estimation-using-b-mode-ultrasound-tongue-image/) (2021). Exploratory CNN regression of child age from tongue ultrasound images, reaching validation MSE 2.03 on UXTD versus 3.64 for a mean-age baseline.
- [Neural Speaker Embeddings for Ultrasound-based Silent Speech Interfaces](../neural-speaker-embeddings-for-ultrasound-based-silent-speech-interfaces/) (2021). Trains x-vector speaker embeddings from ultrasound tongue video, achieving under 1% speaker recognition error on unseen speakers, but adding them to multi-speaker ultrasound-to-speech synthesis gives only marginal gains.
- [Silent versus modal multi-speaker speech recognition from ultrasound and video](../silent-versus-modal-multi-speaker-speech-recognition-from-ultrasound-and-video/) (2021). Speech recognition from ultrasound tongue imaging and lip video on TaL80 and TaL1; adaptation lowers multi-speaker silent WER from 77.79 to 69.84 versus 39.34 for modal speech, showing a large silent-mode gap.
- [Speech Synthesis from Text and Ultrasound Tongue Image-based Articulatory Input](../speech-synthesis-from-text-and-ultrasound-tongue-image-based-articulatory-input/) (2021). Limited-data TTS augmented with ultrasound tongue images; combined text plus ultrasound gives the lowest test MCD for all 8 speakers, while ultrasound-only input remains far worse.
- [Voice Activity Detection for Ultrasound-based Silent Speech Interfaces using Convolutional Neural Networks](../voice-activity-detection-for-ultrasound-based-silent-speech-interfaces-using-convolutional-neural-networks/) (2021). CNN speech-versus-silence detection from ultrasound tongue images on one speaker (TaL1), reaching 85.2% test accuracy; removing silence slightly improves downstream SSI reconstruction (MCD 3.05 vs 3.12).

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
