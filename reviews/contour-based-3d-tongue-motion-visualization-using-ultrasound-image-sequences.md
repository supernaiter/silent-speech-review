# Contour-based 3d tongue motion visualization using ultrasound image sequences

Kele Xu, Yin Yang, Clemence Leboullenger, Pierre Roussel, Bruce Denby  
arXiv 2016 · [arXiv](https://arxiv.org/abs/1605.05967)

**Section:** [Ultrasound & tongue imaging](../README.md#ultrasound--tongue-imaging) · **Review basis:** full_text

A structured review of *Contour-based 3d tongue motion visualization using ultrasound image sequences* (Kele Xu et al., arXiv 2016) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Builds a contour-based pipeline that maps midsagittal ultrasound tongue contours to 3D tongue motion using a database of 1000 3D shapes; evaluation is qualitative, with about 1.2 s per frame association.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | B-mode ultrasound tongue imaging |
| Task | 3D tongue motion visualization |
| Vocabulary | Not applicable |
| Speaker | Not stated |
| Session | Not applicable |
| Online / offline | Offline |
| Key result | Not reported (about 1.2 s average to associate a frame with the 3D model) |

**Limitations.** Not a recognizer; uses only midsagittal information with a simplified driving scheme and has no quantitative accuracy benchmark.

## Full review

### In short

Useful tongue-modeling tool, not a recognizer.

### Review

The full text supports a more careful reading than the seed version. The method is technically specific: contour extraction from ultrasound drives a finite-element tongue model through modal reduction and modal warping, and the runtime system searches a 1000-shape database using contour similarity. Section 5 reports about 1.2 seconds per frame association on desktop hardware, which is better than a purely offline toy demo but still not a proven real-time SSI. The authors are also explicit that quantitative evaluation is missing and that midsagittal-only information cannot capture out-of-plane tongue motion. So this is valuable adjacent modeling work, but not a speech-decoding paper.

### Why it matters

This is an SSI-adjacent articulatory visualization paper, not a speech recognizer, but it offers a concrete modeling pipeline for turning ultrasound contours into 3D tongue motion.

### Prior state of the art

Ultrasound tongue work often focused on contour tracking or 2D visualization rather than a contour-driven 3D deformation model.

### What changed

The paper links ultrasound contour extraction to a 3D finite-element tongue model via modal reduction, modal warping, and contour-matching over a precomputed shape database.

### Position in the field

Adjacent tongue-modeling and visualization work that can support SSI interpretation and articulation analysis.

### Practical value

Moderate for articulatory analysis and future SSI tooling, limited as a direct communication interface.

### Advanced

articulatory modeling; visualization; problem framing

### Unresolved

quantitative validation; out-of-plane motion; end-to-end interactive performance

### Evaluation details

| Item | Details |
| --- | --- |
| Task | tongue motion visualization |
| Input | B-mode ultrasound tongue images |
| Sensor | B-mode ultrasound imaging with contour extraction from the midsagittal tongue surface |
| Body site | tongue |
| Output | 3D tongue visualization |
| Metrics and results | The database contains 1000 sample 3D tongue shapes, and Section 5 reports about 1.2 seconds on average to build the association between the current ultrasound frame and the 3D tongue model on the reported desktop hardware. The paper explicitly says no effective quantitative evaluation method is yet available. |
| Evaluation protocol | Qualitative visualization with runtime reporting and midsagittal overlay validation against ultrasound contours. |

### Limits

- **Technical:** The model uses only midsagittal information, relies on a simplified four-node driving scheme, and lacks a quantitative accuracy benchmark.
- **Evaluation:** Validation is qualitative and runtime-oriented; no MRI- or EMA-backed quantitative benchmark is reported.
- **Deployment:** This is not a communication interface and does not show user-facing SSI deployment.
- **Scope of this review:** SSI-adjacent visualization and modeling paper, not speech recognition.

### Evidence

- The abstract describes a contour-based 3D tongue deformation visualization framework that uses B-mode ultrasound sequences, a generic finite-element tongue model, modal reduction, and modal warping. (ABSTRACT)
- The method builds a 1000-shape 3D tongue database and selects the tongue shape whose projected contour best matches the contour extracted from the current ultrasound frame. (4. CONTOUR-BASED 3D TONGUE MOTION VISUALIZATION)
- Section 5 reports an average processing time of about 1.2 seconds to build the association between the current ultrasound frame and the 3D tongue model on the reported desktop platform. (5. RESULTS)
- The discussion says there is still no effective quantitative evaluation method, midsagittal-only motion is insufficient for full tongue accuracy, and future validation should use modalities such as MRI and EMA. (6. DISCUSSION AND FUTURE WORK)

## More reviews in Ultrasound & tongue imaging

- [Updating the silent speech challenge benchmark with deep learning](updating-the-silent-speech-challenge-benchmark-with-deep-learning.md) (2017). Updates the Silent Speech Challenge ultrasound-plus-lip benchmark with Kaldi DNN-HMM recognition, cutting WER from 17.4% to 6.45% on the same single-speaker archive.
- [Autoencoder-Based Articulatory-to-Acoustic Mapping for Ultrasound Silent Speech Interfaces](autoencoder-based-articulatory-to-acoustic-mapping-for-ultrasound-silent-speech-interfaces.md) (2019). Compresses ultrasound tongue images with an autoencoder bottleneck before predicting spectral parameters, giving more accurate prediction and more natural speech with smaller models on a single speaker.
- [Denoising convolutional autoencoder based B-mode ultrasound tongue image feature extraction](denoising-convolutional-autoencoder-based-b-mode-ultrasound-tongue-image-feature-extraction.md) (2019). Uses a denoising convolutional autoencoder to extract ultrasound tongue image features, improving silent speech recognition over prior feature extraction methods on the 2010 Silent Speech Challenge data.
- [SottoVoce: An Ultrasound Imaging-Based Silent Speech Interaction Using Deep Neural Networks](sottovoce.md) (2019). SottoVoce reconstructs speech audio from under-jaw ultrasound images with two DNNs to control unmodified smart speakers; command success rose from 42.5% to 65.0% with the second network, versus 90.0% for real audio.
- [Ultrasound-based Silent Speech Interface Built on a Continuous Vocoder](ultrasound-based-silent-speech-interface-built-on-a-continuous-vocoder.md) (2019). Adds CNN-based continuous F0 prediction to an ultrasound tongue-imaging SSI vocoder, lowering pitch RMSE versus a discontinuous F0 baseline, with a non-significant naturalness trend in MUSHRA tests on four Hungarian speakers.
- [Ultra2Speech -- A Deep Learning Framework for Formant Frequency Estimation and Tracking from Ultrasound Tongue Images](ultra2speech-a-deep-learning-framework-for-formant-frequency-estimation-and-tracking-from-ultrasound-tongue-images.md) (2020). Estimates and tracks formant frequencies from ultrasound tongue image sequences for speech synthesis; best U2F configuration reaches mean R2 99.96 on joint f1-f2 prediction versus 90.01 for a Conv-BiLSTM baseline.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
