# Ultra2Speech -- A Deep Learning Framework for Formant Frequency Estimation and Tracking from Ultrasound Tongue Images

Pramit Saha, Yadong Liu, Bryan Gick, Sidney Fels  
arXiv 2020 · [arXiv](https://arxiv.org/abs/2006.16367)

**Section:** [Ultrasound & tongue imaging](../../README.md#ultrasound--tongue-imaging) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *Ultra2Speech -- A Deep Learning Framework for Formant Frequency Estimation and Tracking from Ultrasound Tongue Images* (Pramit Saha et al., arXiv 2020) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Estimates and tracks formant frequencies from ultrasound tongue image sequences for speech synthesis; best U2F configuration reaches mean R2 99.96 on joint f1-f2 prediction versus 90.01 for a Conv-BiLSTM baseline.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Ultrasound probe (tongue images) |
| Task | Formant estimation from ultrasound |
| Vocabulary | Not applicable |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Mean R2 99.96 on joint f1-f2 prediction vs 90.01 baseline |

**Limitations.** Focuses on formant tracking and vowel trajectories rather than full speech reconstruction; single collected dataset, no cross-speaker or real-time device evaluation.

## Full review

### In short

Strong ultrasound SSI paper with unusually clear quantitative gains.

### Review

The full text shows this is more than a formant-regression curiosity. U2F cleanly beats the Conv-BiLSTM and plain 3D CNN baselines, and the joint f1-f2 result at 99.96 mean R2 is far above the recurrent baseline. The interesting systems insight is that hybrid spatial-temporal blocks plus channel shuffling are not cosmetic: the ablations show each piece contributes, and the conclusion frames the model as a path toward less manual tongue-contour extraction in SSI pipelines.

### Why it matters

A strong SSI paper because it turns ultrasound tongue video into a high-quality articulatory-to-acoustic mapping problem with convincing quantitative gains.

### Prior state of the art

Ultrasound SSI work often depended on handcrafted tongue features or weaker sequence models.

### What changed

U2F uses hybrid 2D spatial and 1D temporal convolutions with shuffling to learn end-to-end formant tracking from raw ultrasound clips.

### Position in the field

Core ultrasound-based SSI work for speech restoration.

### Practical value

Useful as a full-text-backed reference for ultrasound-to-acoustic mapping and articulatory feature learning.

### Advanced

ultrasound_ssi; articulatory_to_acoustic_mapping; tongue_tracking

### Unresolved

broader speech coverage and real-time patient deployment remain unresolved.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | ultrasound tongue image sequences |
| Sensor | ultrasound probe |
| Body site | tongue; oral-cavity |
| Output | speech-audio |
| Metrics and results | The best U2F configuration reaches mean R2 99.96 on joint f1-f2 prediction, versus 90.01 for the Conv-BiLSTM baseline on the same joint task. |
| Evaluation protocol | train-dev-test split on ultrasound videos with MAE and mean R2 plus baseline and ablation comparisons |

### Limits

- **Technical:** The reported system focuses on formant tracking and synthesized vowel trajectories rather than full open-vocabulary speech reconstruction.
- **Evaluation:** Evaluation is on the collected ultrasound dataset and does not establish cross-speaker clinical deployment.
- **Deployment:** The work motivates SSI use but does not present a real-time deployed device.
- **Scope of this review:** Ultrasound tongue-image to formant / synthesized speech pipeline.

### Evidence

- The abstract says U2F maps ultrasound tongue images to formant trajectories and then synthesizes continuous vowel trajectories with a Klatt synthesizer. (Abstract)
- Table 1 reports the best U2F configuration at mean R2 99.96 on joint f1-f2 prediction, outperforming the recurrent and standard 3D CNN baselines. (Table 1. Performance comparison with baseline methods)
- The discussion lists the hybrid spatial-temporal feature extraction and channel shuffling as the central architectural contribution. (5    Discussion and Conclusion)
- The paper evaluates end-to-end mapping to formant frequencies and vowel trajectories, not a full open-vocabulary speech restoration benchmark. (5    Discussion and Conclusion)

## More reviews in Ultrasound & tongue imaging

- [3D Convolutional Neural Networks for Ultrasound-Based Silent Speech Interfaces](../3d-convolutional-neural-networks-for-ultrasound-based-silent-speech-interfaces/) (2021). Shows a compact (2+1)D 3D CNN outperforms 2D CNN and CNN+LSTM models for regressing 13 vocoder parameters from ultrasound tongue video, with lower complexity and training time.
- [Convolutional Neural Network-Based Age Estimation Using B-Mode Ultrasound Tongue Image](../convolutional-neural-network-based-age-estimation-using-b-mode-ultrasound-tongue-image/) (2021). Exploratory CNN regression of child age from tongue ultrasound images, reaching validation MSE 2.03 on UXTD versus 3.64 for a mean-age baseline.
- [Improving Neural Silent Speech Interface Models by Adversarial Training](../improving-neural-silent-speech-interface-models-by-adversarial-training/) (2021). Adds adversarial (GAN) loss to MSE training of a 3D CNN for ultrasound-to-mel-spectrogram mapping, giving modest objective quality improvements on Hungarian and English single-speaker corpora.
- [Neural Speaker Embeddings for Ultrasound-based Silent Speech Interfaces](../neural-speaker-embeddings-for-ultrasound-based-silent-speech-interfaces/) (2021). Trains x-vector speaker embeddings from ultrasound tongue video, achieving under 1% speaker recognition error on unseen speakers, but adding them to multi-speaker ultrasound-to-speech synthesis gives only marginal gains.
- [Silent versus modal multi-speaker speech recognition from ultrasound and video](../silent-versus-modal-multi-speaker-speech-recognition-from-ultrasound-and-video/) (2021). Speech recognition from ultrasound tongue imaging and lip video on TaL80 and TaL1; adaptation lowers multi-speaker silent WER from 77.79 to 69.84 versus 39.34 for modal speech, showing a large silent-mode gap.
- [Speech Synthesis from Text and Ultrasound Tongue Image-based Articulatory Input](../speech-synthesis-from-text-and-ultrasound-tongue-image-based-articulatory-input/) (2021). Limited-data TTS augmented with ultrasound tongue images; combined text plus ultrasound gives the lowest test MCD for all 8 speakers, while ultrasound-only input remains far worse.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
