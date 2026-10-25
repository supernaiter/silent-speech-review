# Denoising convolutional autoencoder based B-mode ultrasound tongue image feature extraction

Bo Li, Kele Xu, Dawei Feng, Haibo Mi, Huaimin Wang, Jian Zhu  
arXiv / imported corpus page 2019 · [arXiv](https://arxiv.org/abs/1903.00888)

**Section:** [Ultrasound & tongue imaging](../README.md#ultrasound--tongue-imaging) · **Review basis:** full_text+structured_benchmark+summary

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

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
