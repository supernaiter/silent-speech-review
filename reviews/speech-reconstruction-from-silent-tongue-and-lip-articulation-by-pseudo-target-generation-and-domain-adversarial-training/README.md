# Speech Reconstruction from Silent Tongue and Lip Articulation By Pseudo Target Generation and Domain Adversarial Training

Ruichen Zheng, Yang Ai, Zhenhua Ling  
arXiv 2023 · [arXiv](https://arxiv.org/abs/2304.05574)

**Section:** [Ultrasound & tongue imaging](../../README.md#ultrasound--tongue-imaging) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *Speech Reconstruction from Silent Tongue and Lip Articulation By Pseudo Target Generation and Domain Adversarial Training* (Ruichen Zheng et al., arXiv 2023) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Reconstructs speech from silent tongue ultrasound and lip video using pseudo acoustic targets and domain adversarial training, improving silent-mode WER by about 15% and MOS by 0.34 over TaLNet on TaL.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Ultrasound tongue imaging plus optical lip camera |
| Task | Speech synthesis from silent articulation |
| Vocabulary | Not stated |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Silent mode: 43.1% WER, STOI 0.517, MOS 3.33 on TaL corpus |

**Limitations.** Evaluated only on TaL with some speakers excluded; silent mode lags vocalized; requires specialized ultrasound and video hardware with no real-time study.

## Full review

### In short

Strong SSI paper improving silent speech reconstruction by generating pseudo acoustic targets and using domain adversarial training to address domain mismatch; validated with TaL dataset showing substantial WER and MOS gains over TaLNet.

### Review

This work convincingly addresses two key challenges in silent speech reconstruction: lack of paired acoustic targets and vocalized-silent domain mismatch. By generating pseudo acoustic targets via DTW alignment from paired vocalized articulation data and employing domain adversarial training to produce domain-invariant articulatory feature representations, the authors overcome limitations of prior ultrasound-and-lip based SSI systems trained only on vocalized data. Iterative retraining further refines the model. The experimental results on the TaL dataset validate that these approaches yield substantial improvements in WER, MCD, STOI, and MOS compared to the TaLNet baseline, both in silent and vocalized speaking modes. However, a clear performance gap remains between silent and vocalized modes, and hardware constraints limit deployment readiness. Overall, the paper provides a strong system integration and training methodology contribution advancing articulatory-to-acoustic conversion for silent speech interfaces using multimodal tongue ultrasound and lip video data.

### Why it matters

The paper's key addition is a novel training approach leveraging pseudo target generation and domain adversarial learning to overcome silent mode data scarcity and domain mismatch in multimodal tongue ultrasound plus lip video speech reconstruction, not just the neural decoder design.

### Prior state of the art

Ultrasound-and-lip reconstruction models trained on vocalized speech perform poorly on silent articulation due to missing acoustic targets and domain mismatch.

### What changed

Introduces DTW-generated pseudo acoustic targets for silent articulation and domain adversarial training to learn domain-invariant features, combined with iterative retraining to improve silent-mode speech reconstruction.

### Position in the field

A strong core SSI result advancing articulatory-to-acoustic conversion with ultrasound and lip video, addressing silent speech training challenges.

### Practical value

Provides a working approach for silent-mode articulatory speech reconstruction that could benefit clinical or silent communication settings where ultrasound and lip video capture are feasible.

### Advanced

silent_mode_training; domain_adaptation; multimodal_articulatory_reconstruction

### Unresolved

The remaining performance gap between silent and vocalized modes and hardware specialization remain unresolved.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | ultrasound tongue imaging; optical lip video |
| Sensor | Ultrasound tongue imaging system; optical lip video camera |
| Body site | tongue; lip; oral-cavity |
| Output | speech-audio |
| Metrics and results | Silent mode: MCD 3.935 dB, STOI 0.517, WER 43.114%, MOS 3.330; Vocalized mode: WER 17.309%, improvements of ~15% WER and 0.34 MOS in silent mode compared to TaLNet baseline. Metrics from Table 1 of the paper. |
| Evaluation protocol | Objective metrics (MCD, STOI, WER) via ASR plus subjective MOS testing on silent and vocalized test sets; ablation on iterative training and domain adversarial training. |

### Limits

- **Technical:** No ground truth acoustic data for silent mode complicates training; DTW-based pseudo labels may still have alignment noise; silent mode performance lags vocalized; some speakers with poor articulation.
- **Evaluation:** Evaluation restricted to the TaL corpus; results validated on silent and vocalized modes with some speakers excluded due to unreliable articulations.
- **Deployment:** Specialized ultrasound and lip video hardware requirements; no deployment or real-time study provided.
- **Scope of this review:** Articulatory-to-acoustic speech reconstruction from silent tongue and lip articulation only; multimodal ultrasound and optical lip video input in controlled corpus setting.

### Evidence

- The paper proposes pseudo target generation using DTW alignment between vocalized and silent articulations, domain adversarial training to learn robust domain-invariant articulatory representations, and iterative training strategy to improve speech reconstruction from silent tongue and lip articulation. (3. PROPOSED METHOD)
- The paper combines dynamic time warping-based pseudo target generation, domain adversarial training, and iterative retraining tailored for silent articulatory-to-acoustic conversion from multimodal tongue ultrasound and lip video input, addressing domain mismatch and lack of paired acoustic targets for silent speech reconstruction. (3. PROPOSED METHOD)
- In silent mode the paper reports MCD 3.935 dB, STOI 0.517, WER 43.114%, and MOS 3.330, improving on TaLNet by about 15 WER points and 0.34 MOS; in vocalized mode WER reduces from 26.890% to 17.309%. (4.3 Experimental Results)
- The evaluation is performed on the TaL corpus containing synchronized audio, ultrasound tongue images, and lip videos in vocalized and silent speaking modes from 81 native English speakers, with 1212 paired utterances, in a speaker-independent setting. (4. EXPERIMENTS)
- Silent-mode speech reconstruction performance remains worse than vocalized mode, and some speakers with unreliable silent articulations are excluded; specialized ultrasound and optical lip video hardware constrain deployment. (4.3 Experimental Results)

## More reviews in Ultrasound & tongue imaging

- [Adaptation of Tongue Ultrasound-Based Silent Speech Interfaces Using Spatial Transformer Networks](../adaptation-of-tongue-ultrasound-based-silent-speech-interfaces-using-spatial-transformer-networks/) (2023). Uses spatial transformer networks to adapt ultrasound-to-speech SSI across sessions and speakers; STN plus output-layer update recovers most of the full-adaptation gain.
- [Improved Processing of Ultrasound Tongue Videos by Combining ConvLSTM and 3D Convolutional Networks](../improved-processing-of-ultrasound-tongue-videos-by-combining-convlstm-and-3d-convolutional-networks/) (2022). Combines 3D CNNs and ConvLSTM to regress mel-spectrograms from ultrasound tongue video, modestly outperforming prior architectures in accuracy and efficiency on single-speaker Hungarian data.
- [Conformer-based Ultrasound-to-Speech Conversion](../conformer-based-ultrasound-to-speech-conversion/) (2025). Compares Conformer-based models to a CNN for ultrasound tongue-to-speech conversion on four speakers; Conformer plus bi-LSTM gives a modest naturalness gain without improving objective spectral metrics.
- [3D Convolutional Neural Networks for Ultrasound-Based Silent Speech Interfaces](../3d-convolutional-neural-networks-for-ultrasound-based-silent-speech-interfaces/) (2021). Shows a compact (2+1)D 3D CNN outperforms 2D CNN and CNN+LSTM models for regressing 13 vocoder parameters from ultrasound tongue video, with lower complexity and training time.
- [Convolutional Neural Network-Based Age Estimation Using B-Mode Ultrasound Tongue Image](../convolutional-neural-network-based-age-estimation-using-b-mode-ultrasound-tongue-image/) (2021). Exploratory CNN regression of child age from tongue ultrasound images, reaching validation MSE 2.03 on UXTD versus 3.64 for a mean-age baseline.
- [Improving Neural Silent Speech Interface Models by Adversarial Training](../improving-neural-silent-speech-interface-models-by-adversarial-training/) (2021). Adds adversarial (GAN) loss to MSE training of a 3D CNN for ultrasound-to-mel-spectrogram mapping, giving modest objective quality improvements on Hungarian and English single-speaker corpora.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
