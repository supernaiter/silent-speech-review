# Adaptation of Tongue Ultrasound-Based Silent Speech Interfaces Using Spatial Transformer Networks

László Tóth, Amin Honarmandi Shandiz, Gábor Gosztolya, Tamás Gábor Csapó  
the Proceedings of Interspeech 2023 · [DOI](https://doi.org/10.21437/Interspeech.2023-1607) · [arXiv](https://arxiv.org/abs/2305.19130)

**Section:** [Ultrasound & tongue imaging](../../README.md#ultrasound--tongue-imaging) · **Review basis:** full_text+structured_benchmark+summary

A structured review of *Adaptation of Tongue Ultrasound-Based Silent Speech Interfaces Using Spatial Transformer Networks* (László Tóth et al., the Proceedings of Interspeech 2023) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Uses spatial transformer networks to adapt ultrasound-to-speech SSI across sessions and speakers; STN plus output-layer update recovers most of the full-adaptation gain.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Micro ultrasound tongue probe with fixing headset |
| Task | Speech synthesis from tongue ultrasound |
| Vocabulary | Read Hungarian sentences |
| Speaker | Both |
| Session | Cross-session |
| Online / offline | Offline |
| Key result | STN+out: 88% avg cross-speaker and 92% cross-session error reduction vs full adaptation (MSE) |

**Limitations.** Only four speakers and MSE-based evaluation without intelligibility tests; still requires probe-mounted ultrasound and supervised adaptation data.

## Full review

### In short

Strong full-text-backed evidence that most of the gain comes from fast input alignment, not from inventing a new SSI stack.

### Review

The paper earns its value by narrowing the adaptation problem. The data section is small but explicit: four Hungarian speakers with 209 read sentences each, plus four extra sessions for one speaker after dismounting and remounting the probe. The experiments then separate STN-only, STN+output-layer, and full retraining. That matters because the headline 88-92% recovery is not 'speaker independence'; it is evidence that affine correction plus a tiny amount of retuning removes most of the adaptation gap in this controlled UTI-to-speech setup.

### Why it matters

This is a concrete SSI adaptation paper, not a general SSI breakthrough: it shows that a small alignment front-end can recover most cross-session and cross-speaker performance in ultrasound-to-speech regression.

### Prior state of the art

UTI silent-speech models were known to break under probe remounting and speaker mismatch, so adaptation usually meant retraining or collecting more multi-speaker data.

### What changed

It isolates a large part of the adaptation problem as affine image misalignment and shows that updating the STN plus, optionally, the output layer recovers most of full adaptation.

### Position in the field

Strong ultrasound SSI adaptation result focused on remounting robustness and faster retuning.

### Practical value

Useful when a probe-mounted ultrasound SSI must be recalibrated after remounting or moved to a new speaker without paying full retraining cost.

### Advanced

speaker adaptation; session adaptation; alignment correction

### Unresolved

speaker-independent deployment; open-vocabulary decoding; day-to-day robustness beyond one repeated speaker

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech reconstruction |
| Input | ultrasound-based silent speech interface |
| Sensor | Articulate Instruments Ltd. Micro ultrasound system with probe-fixing headset |
| Body site | tongue |
| Output | speech-audio |
| Metrics and results | 2D Table 2: STN-only closes 75-76% of the adaptation gap, while STN+out reaches 88% average cross-speaker and 92% cross-session error reduction relative to full adaptation; 3D Table 3 keeps similar relative gains with 87% average improvement for STN+out |
| Evaluation protocol | Cross-speaker and cross-session adaptation on Hungarian UTI-to-speech conversion with MSE comparisons |

### Limits

- **Technical:** The method only corrects what an affine image transform and a small output-layer update can fix; it does not solve broader speaker-independent SSI or language coverage.
- **Evaluation:** Evidence is limited to four speakers, read Hungarian sentences, one speaker with repeated remounted sessions, and MSE-based regression quality rather than intelligibility or user studies.
- **Deployment:** A probe-mounted ultrasound rig and supervised adaptation data are still required, so this is faster retuning rather than plug-and-play deployment.
- **Scope of this review:** Ultrasound-to-spectrogram SSI adaptation under controlled recording conditions.

### Evidence

- The paper extends UTI-based SSI networks with a spatial transformer network so quick speaker and session adaptation can be done without retraining the whole model. (Abstract)
- Evaluation uses four Hungarian speakers with 209 read sentences each, plus four additional remounted sessions from speaker 048 recorded on different days. (4.1. Data Acquisition and Preprocessing)
- In the 2D adaptation study, STN+out recovers 88% of the cross-speaker gap and 92% of the cross-session gap relative to full adaptation, while STN-only recovers about 75-76%. (Table 2)
- The paper says future work should test a 3D localization network and smaller amounts of adaptation material, indicating the current evidence remains a controlled adaptation study rather than a broad deployment result. (6. Conclusions)

## More reviews in Ultrasound & tongue imaging

- [Speech Reconstruction from Silent Tongue and Lip Articulation By Pseudo Target Generation and Domain Adversarial Training](../speech-reconstruction-from-silent-tongue-and-lip-articulation-by-pseudo-target-generation-and-domain-adversarial-training/) (2023). Reconstructs speech from silent tongue ultrasound and lip video using pseudo acoustic targets and domain adversarial training, improving silent-mode WER by about 15% and MOS by 0.34 over TaLNet on TaL.
- [Improved Processing of Ultrasound Tongue Videos by Combining ConvLSTM and 3D Convolutional Networks](../improved-processing-of-ultrasound-tongue-videos-by-combining-convlstm-and-3d-convolutional-networks/) (2022). Combines 3D CNNs and ConvLSTM to regress mel-spectrograms from ultrasound tongue video, modestly outperforming prior architectures in accuracy and efficiency on single-speaker Hungarian data.
- [Conformer-based Ultrasound-to-Speech Conversion](../conformer-based-ultrasound-to-speech-conversion/) (2025). Compares Conformer-based models to a CNN for ultrasound tongue-to-speech conversion on four speakers; Conformer plus bi-LSTM gives a modest naturalness gain without improving objective spectral metrics.
- [3D Convolutional Neural Networks for Ultrasound-Based Silent Speech Interfaces](../3d-convolutional-neural-networks-for-ultrasound-based-silent-speech-interfaces/) (2021). Shows a compact (2+1)D 3D CNN outperforms 2D CNN and CNN+LSTM models for regressing 13 vocoder parameters from ultrasound tongue video, with lower complexity and training time.
- [Convolutional Neural Network-Based Age Estimation Using B-Mode Ultrasound Tongue Image](../convolutional-neural-network-based-age-estimation-using-b-mode-ultrasound-tongue-image/) (2021). Exploratory CNN regression of child age from tongue ultrasound images, reaching validation MSE 2.03 on UXTD versus 3.64 for a mean-age baseline.
- [Improving Neural Silent Speech Interface Models by Adversarial Training](../improving-neural-silent-speech-interface-models-by-adversarial-training/) (2021). Adds adversarial (GAN) loss to MSE training of a 3D CNN for ultrasound-to-mel-spectrogram mapping, giving modest objective quality improvements on Hungarian and English single-speaker corpora.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
