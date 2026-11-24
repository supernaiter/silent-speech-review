# Denoising convolutional autoencoder based B-mode ultrasound tongue image feature extraction

Bo Li, Kele Xu, Dawei Feng, Haibo Mi, Huaimin Wang, Jian Zhu  
arXiv 2019 · [arXiv](https://arxiv.org/abs/1903.00888)

**Section:** [Ultrasound & tongue imaging](../../README.md#ultrasound--tongue-imaging) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *Denoising convolutional autoencoder based B-mode ultrasound tongue image feature extraction* (Bo Li et al., arXiv 2019) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Uses a denoising convolutional autoencoder to extract ultrasound tongue image features, improving silent speech recognition over prior feature extraction methods on the 2010 Silent Speech Challenge data.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Ultrasound tongue imaging (4-8 MHz microconvex probe) |
| Task | Silent speech recognition (feature extraction) |
| Vocabulary | Not stated |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | WER 6.17% with DCAE features, single-speaker Silent Speech Challenge data |

**Limitations.** Single-speaker dataset only, no cross-corpus validation, and robustness to different ultrasound systems and head movement is not validated.

## Full review

### In short

DCAE provides cleaner, more robust ultrasound tongue features leading to improved silent speech recognition, outperforming prior feature extraction strategies.

### Review

This paper presents a feature representation study applying denoising convolutional autoencoders (DCAE) to ultrasound tongue image sequences in the context of silent speech interfaces. The authors evaluate DCAE against previous methods such as discrete cosine transform and conventional autoencoders using both reconstruction metrics (Mean Square Error and Complex Wavelet Structural Similarity) and speech recognition performance on the 2010 Silent Speech Challenge dataset. Results indicate DCAE provides improved robustness to noise and preserves spatial tongue structure better than both traditional and deep autoencoder approaches, leading to the lowest word error rates among evaluated methods. While the contribution is modest and focused on feature extraction rather than full SSI system architecture, it establishes a useful baseline for ultrasound SSI feature compression with evidence-backed performance gains. Limitations include evaluation on a single dataset with no cross-speaker generalization and reliance on ultrasound hardware, thus deployment readiness remains medium with scope for broader validation.

### Why it matters

A well-supported demonstration that denoising convolutional autoencoders improve feature representation quality for ultrasound tongue images in silent speech tasks, offering a stronger baseline for ultrasound SSI research.

### Prior state of the art

Ultrasound tongue feature extraction primarily used direct-image representations or hand-crafted basis decomposition methods such as PCA (EigenTongue) and DCT.

### What changed

Introduces an unsupervised denoising convolutional autoencoder as a feature extractor compressing noisy ultrasound frames into latent representations for downstream recognition, replacing direct or handcrafted features.

### Position in the field

Feature-extraction focused contribution advancing ultrasound-based silent speech interfaces.

### Practical value

Provides a method yielding cleaner latent ultrasound features that can improve downstream speech recognition in ultrasound SSI pipelines.

### Advanced

system_design; evaluation

### Unresolved

Generalization to broader cross-subject scenarios beyond the 2010 Silent Speech Challenge dataset

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | ultrasound |
| Sensor | Ultrasound imaging system with 4–8 MHz, 128-element microconvex probe |
| Body site | tongue |
| Output | text |
| Vocabulary type | Not specified |
| Vocabulary size | Not specified |
| Metrics and results | Mean Square Error (MSE), Complex Wavelet Structural Similarity Index (CW-SSIM), Word Error Rate (WER) of 6.17% (best with DCAE) |
| Evaluation protocol | experimental study |

### Limits

- **Technical:** Single-speaker data; speckle noise and motion artifacts inherent in ultrasound; unknown cross-subject generalization.
- **Evaluation:** Evaluated only on a single speaker-specific dataset (2010 silent speech challenge); no multi-speaker or cross-corpus validation provided.
- **Deployment:** Need for specialized ultrasound imaging hardware; robustness to varying ultrasound systems and head movements not fully validated for real-world deployment.
- **Scope of this review:** Limited to ultrasound tongue image feature extraction; no multimodal fusion or speech synthesis explored.

### Evidence

- The denoising convolutional autoencoder (DCAE)-based method outperforms other feature extraction methods on reconstruction and silent speech recognition tasks. (Abstract)
- DCAE achieves Word Error Rate (WER) of 6.17%, better than state-of-the-art 6.45% using DCT features on the 2010 Silent Speech Challenge corpus. (3.3. Silent speech challenge)
- Ultrasound tongue images are high-dimensional, suffer from low signal-to-noise ratio and speckle noise, and can be affected by head movement causing rotation or displacement. (1. INTRODUCTION)
- The dataset used is the 2010 Silent Speech Challenge dataset with mid-sagittal ultrasound tongue image sequences recorded at 60 fps using a 4-8 MHz, 128-element microconvex probe. (3.1. Dataset)
- Evaluation is limited to a single-speaker dataset with no cross-speaker validation, raising questions about generalization. (4. CONCLUSION)
- Application of denoising convolutional autoencoder for feature extraction on ultrasound tongue images to reduce noise and preserve spatial structure better than prior AE and DCT methods. (2.4. Denoising Convolutional Auto-encoder)
- The approach requires ultrasound imaging equipment and stabilization hardware, limiting deployment to systems where such hardware is available. (3.1. Dataset)
- CAEs and DCAEs outperform traditional deep autoencoders and DCT in reconstruction metrics (MSE and CW-SSIM), indicating better preservation of spatial structure in ultrasound images. (3.2. Reconstruction error comparison)

## More reviews in Ultrasound & tongue imaging

- [Autoencoder-Based Articulatory-to-Acoustic Mapping for Ultrasound Silent Speech Interfaces](../autoencoder-based-articulatory-to-acoustic-mapping-for-ultrasound-silent-speech-interfaces/) (2019). Standard on the encoder: autoencoder features predate it and it is never compared with PCA or DCT; behind on F0, which is copied from the recording, so the listening test is not of a silent system.
- [SottoVoce: An Ultrasound Imaging-Based Silent Speech Interaction Using Deep Neural Networks](../sottovoce/) (2019). SottoVoce reconstructs speech audio from under-jaw ultrasound images with two DNNs to control unmodified smart speakers; command success rose from 42.5% to 65.0% with the second network, versus 90.0% for real audio.
- [Ultrasound-based Silent Speech Interface Built on a Continuous Vocoder](../ultrasound-based-silent-speech-interface-built-on-a-continuous-vocoder/) (2019). Continuous F0 targets from articulation were prior work; MVF carrying voicing instead of a flag is new but unproven: the F0 RMSE gain uses different reference contours and naturalness is not better.
- [3D Convolutional Neural Networks for Ultrasound-Based Silent Speech Interfaces](../3d-convolutional-neural-networks-for-ultrasound-based-silent-speech-interfaces/) (2020). (2+1)D front end (M06) is standard: established in lip reading, ported to ultrasound; a 6.3% MSE edge over CNN+LSTM, one speaker, one run; MSE-only evaluation (M12 behind).
- [Ultra2Speech - A Deep Learning Framework for Formant Frequency Estimation and Tracking from Ultrasound Tongue Images](../ultra2speech-a-deep-learning-framework-for-formant-frequency-estimation-and-tracking-from-ultrasound-tongue-images/) (2020). Formant target and hybrid front end (M06) are standard; evaluation (M12) is behind: random one-second clip split of one speaker, where earlier ultrasound work held out whole utterances.
- [Updating the Silent Speech Challenge benchmark with deep learning](../updating-the-silent-speech-challenge-benchmark-with-deep-learning/) (2018). Kaldi DNN-HMM cuts SSC WER from 17.4% to 6.45% (M06, M12: standard), but with the same bigram its own GMM gives 12.71%, so the DNN halves WER; one speaker, single runs.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
