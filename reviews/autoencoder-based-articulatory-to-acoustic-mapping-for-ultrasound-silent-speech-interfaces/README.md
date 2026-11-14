# Autoencoder-Based Articulatory-to-Acoustic Mapping for Ultrasound Silent Speech Interfaces

Gábor Gosztolya, MTA-SZTE Research Group on Artificial Intelligence, University of Szeged, Hungary, Gábor Infusz, ginfusz@inf.u-szeged.hu, Ádám Pintér, Institute of Informatics, University of Szeged, Szeged, Hungary, László Tóth, Institute of Informatics, University of Szeged, Szeged, Hungary, Alexandra Markó, Department of Phonetics, Eötvös Loránd University, MTA-ELTE Lendület Lingual Articulation Research Group, Budapest, Hungary, Gábor Csapó, Department of Telecommunications and Media Informatics, Budapest University of Technology and Economics, MTA-ELTE Lendület Lingual Articulation Research Group, Budapest, Hungary  
arXiv 2019 · [arXiv](https://arxiv.org/abs/1904.05259)

**Section:** [Ultrasound & tongue imaging](../../README.md#ultrasound--tongue-imaging) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *Autoencoder-Based Articulatory-to-Acoustic Mapping for Ultrasound Silent Speech Interfaces* (Gábor Gosztolya et al., arXiv 2019) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Compresses ultrasound tongue images with an autoencoder bottleneck before predicting spectral parameters, giving more accurate prediction and more natural speech with smaller models on a single speaker.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Ultrasound tongue imaging (2-4 MHz convex probe, 82 fps) |
| Task | Speech synthesis from ultrasound |
| Vocabulary | Not stated |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Improved NMSE, Pearson correlation and MUSHRA naturalness (exact values not stated) |

**Limitations.** Single-speaker corpus only, no cross-speaker or cross-session testing, and no real-time or mobile deployment.

## Full review

### In short

The paper advances ultrasound silent speech interfaces by compressing ultrasound images using an autoencoder bottleneck prior to spectral parameter prediction, resulting in improved accuracy and more natural synthesized speech with smaller models.

### Review

This study presents a system integration and efficiency improvement for ultrasound-based silent speech interfaces by compressing high-dimensional ultrasound tongue images via an autoencoder neural network. Instead of using the full raw pixel intensities as input to spectral parameter estimation neural networks, the authors extract bottleneck layer activations from the autoencoder as compressed features. This compression reduces redundancy and noise inherent in ultrasound images. The two-step process (autoencoder encoding and spectral DNN prediction) yields significantly better normalized mean squared error and correlation in predicting Mel-Generalized Cepstral Line Spectral Pair (MGC-LSP) parameters compared to pixel-wise inputs. Notably, this compression allows using multiple consecutive frames as input without an explosion in model size, further improving performance. Subjective listening tests demonstrate that synthesized speech from the compressed features scores higher naturalness than baseline methods. However, the study is limited to a single speaker dataset and acoustic conditions, with no investigation into session variability or real-time deployment. Overall, the work offers a practical system design advance in ultrasound SSI, emphasizing efficiency and improved acoustic prediction accuracy via latent representation learning.

### Why it matters

The key contribution lies in using an autoencoder to reduce ultrasound image redundancy and noise, enabling more compact and accurate articulatory-to-acoustic mapping, rather than novel acoustic modeling or SSI modality innovation.

### Prior state of the art

Ultrasound SSI typically used the whole ultrasound image pixel intensity frame as input features directly to deep neural network spectral parameter predictors.

### What changed

Replaces direct pixel intensity input with compressed latent features extracted by an autoencoder from ultrasound frames before spectral parameter prediction. Uses activations from bottleneck layer as input features, enabling use of multiple consecutive frames without increasing model size excessively.

### Position in the field

Efficiency-oriented ultrasound articulatory-to-acoustic mapping paper with latent representation learning.

### Practical value

Offers a method to reduce model size and improve parameter prediction in ultrasound SSI, potentially aiding more compact and efficient ultrasound speech interfaces.

### Advanced

system_design; evaluation

### Unresolved

cross-speaker and cross-session generalization, real-time deployment

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | ultrasound video |
| Sensor | Ultrasound imaging system with a 2-4 MHz convex array transducer producing mid-sagittal tongue images at 82 fps. |
| Body site | tongue |
| Output | speech-audio |
| Metrics and results | Normalized Mean Squared Error (NMSE) for MGC-LSP prediction averaged over 25 parameters; average Pearson correlation coefficient between true and predicted spectral parameters; MUSHRA listening scores for naturalness on synthesized speech. |
| Evaluation protocol | experimental study with quantitative regression metrics (NMSE, Pearson correlation) and subjective listening (MUSHRA) test for naturalness |

### Limits

- **Technical:** Autoencoder architecture details limited; only single-speaker data; limited exploration of bottleneck size impact; no speaker adaptation explored; no real-time or mobile deployment shown.
- **Evaluation:** Evaluation limited to a single-speaker ultrasound corpus; no cross-speaker or session testing; listening test conducted with native speakers on synthesized speech but no large-scale subjective evaluation.
- **Deployment:** Requires ultrasound imaging hardware in controlled setup; no demonstration of real-time or mobile deployment; unknown robustness across speakers or sessions.
- **Scope of this review:** Focused on ultrasound tongue imaging SSI for single-speaker spectral parameter regression; excludes multi-speaker, recognition, or broader SSI types.

### Evidence

- In this study we train an autoencoder neural network on the ultrasound images; the estimation of the spectral speech parameters is done by a second DNN, using the activations of the bottleneck layer of the autoencoder as features. (I. INTRODUCTION)
- Normalized mean squared error scores were lower, correlation values were higher, and listening test results showed more natural sounding synthesized utterances when using autoencoder bottleneck features versus full-image baseline. (IV. RESULTS USING OBJECTIVE MEASUREMENTS)
- The method was evaluated only on ultrasound recordings from one Hungarian female speaker reading 438 sentences; no cross-speaker or cross-session generalization was tested. (III. EXPERIMENTAL SETUP)
- No real-time or live deployment was demonstrated; system requires fixed ultrasound transducer setup and substantial computational resources not demonstrated as mobile or wearable. (VI. CONCLUSIONS)

## More reviews in Ultrasound & tongue imaging

- [Denoising convolutional autoencoder based B-mode ultrasound tongue image feature extraction](../denoising-convolutional-autoencoder-based-b-mode-ultrasound-tongue-image-feature-extraction/) (2019). Uses a denoising convolutional autoencoder to extract ultrasound tongue image features, improving silent speech recognition over prior feature extraction methods on the 2010 Silent Speech Challenge data.
- [SottoVoce: An Ultrasound Imaging-Based Silent Speech Interaction Using Deep Neural Networks](../sottovoce/) (2019). SottoVoce reconstructs speech audio from under-jaw ultrasound images with two DNNs to control unmodified smart speakers; command success rose from 42.5% to 65.0% with the second network, versus 90.0% for real audio.
- [Ultrasound-based Silent Speech Interface Built on a Continuous Vocoder](../ultrasound-based-silent-speech-interface-built-on-a-continuous-vocoder/) (2019). Adds CNN-based continuous F0 prediction to an ultrasound tongue-imaging SSI vocoder, lowering pitch RMSE versus a discontinuous F0 baseline, with a non-significant naturalness trend in MUSHRA tests on four Hungarian speakers.
- [Ultra2Speech -- A Deep Learning Framework for Formant Frequency Estimation and Tracking from Ultrasound Tongue Images](../ultra2speech-a-deep-learning-framework-for-formant-frequency-estimation-and-tracking-from-ultrasound-tongue-images/) (2020). Estimates and tracks formant frequencies from ultrasound tongue image sequences for speech synthesis; best U2F configuration reaches mean R2 99.96 on joint f1-f2 prediction versus 90.01 for a Conv-BiLSTM baseline.
- [3D Convolutional Neural Networks for Ultrasound-Based Silent Speech Interfaces](../3d-convolutional-neural-networks-for-ultrasound-based-silent-speech-interfaces/) (2021). Shows a compact (2+1)D 3D CNN outperforms 2D CNN and CNN+LSTM models for regressing 13 vocoder parameters from ultrasound tongue video, with lower complexity and training time.
- [Convolutional Neural Network-Based Age Estimation Using B-Mode Ultrasound Tongue Image](../convolutional-neural-network-based-age-estimation-using-b-mode-ultrasound-tongue-image/) (2021). Exploratory CNN regression of child age from tongue ultrasound images, reaching validation MSE 2.03 on UXTD versus 3.64 for a mean-age baseline.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
