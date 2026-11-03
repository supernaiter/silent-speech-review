# Advances and Challenges in Deep Lip Reading

Marzieh Oghbaie, Arian Sabaghi, Kooshan Hashemifard, Mohammad Akbari  
arXiv 2021 · [arXiv](https://arxiv.org/abs/2110.07879)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

A structured review of *Advances and Challenges in Deep Lip Reading* (Marzieh Oghbaie et al., arXiv 2021) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Survey of deep lip reading covering datasets, pipeline modules, challenges and evaluation metrics; contributes no new model or experiments.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Video (lip/face) |
| Task | Survey |
| Vocabulary | Not applicable |
| Speaker | Not stated |
| Session | Not applicable |
| Online / offline | Not applicable |
| Key result | Not reported |

**Limitations.** Literature synthesis only, with no original experiments or deployment evaluation.

## Full review

### In short

Good survey, not a model result.

### Review

The paper is strongest as field organization. The introduction explicitly says the survey focuses on dataset obstacles, evaluation metrics, and impediments across the VSR pipeline. Section 3.1.2 reviews why in-the-wild datasets matter because controlled corpora do not transfer cleanly to real-world conditions. Section 3.4 then summarizes the metric families, including word accuracy, sentence accuracy, error-rate metrics, and BLEU. That makes it useful background for SSI-adjacent visual speech work, but it cannot be cited as evidence that any specific lip-reading or lip-to-speech system works.

### Why it matters

The full text supports using this paper as orientation, not as system evidence: it is a structured review of where lip reading was succeeding and where data and evaluation were still bottlenecks.

### Prior state of the art

The lip-reading literature was growing quickly, but its datasets, task variants, and evaluation practices were still fragmented.

### What changed

This paper organizes the field into datasets, pipeline modules, data challenges, and evaluation metrics rather than proposing another model.

### Position in the field

Background survey for visual speech recognition and SSI-adjacent lip-reading context.

### Practical value

Useful for mapping datasets, metrics, and open problems before choosing a technical direction.

### Advanced

field synthesis; evaluation framing

### Unresolved

survey coverage is bounded by the literature up to 2021

### Evaluation details

| Item | Details |
| --- | --- |
| Task | survey |
| Input | video |
| Body site | face; lip |
| Metrics and results | surveyed metrics include word accuracy, sentence accuracy rate, error-rate family metrics, and BLEU |
| Evaluation protocol | literature survey over datasets, pipeline modules, challenges, and evaluation criteria in deep lip reading |

### Limits

- **Technical:** Survey article; it does not contribute a new model or experimental benchmark of its own.
- **Evaluation:** All claims are literature synthesis rather than original experiments.
- **Deployment:** No deployment path is evaluated because this is a review paper.
- **Scope of this review:** Deep lip-reading survey only.

### Evidence

- The abstract frames the paper as a comprehensive survey of deep-learning-based visual speech recognition focused on data challenges, task complications, and corresponding solutions. (A BSTRACT)
- The introduction says the survey specifically reviews major datasets, metrics, sub-modules of the VSR pipeline, and open problems rather than proposing a new model. (1       Introduction)
- Section 3.1.2 explains why in-the-wild datasets are necessary, noting that controlled datasets do not transfer cleanly to real-world conditions. (3.1.2   Lip Reading Datasets in the Wild)
- Section 3.4 reviews the field's evaluation metrics, including word accuracy, sentence accuracy, error-rate metrics, and BLEU. (3.4    Evaluation Criteria)

## More reviews in Lip & face video

- [Speaker disentanglement in video-to-speech conversion](speaker-disentanglement-in-video-to-speech-conversion.md) (2021). Disentangles speaker identity from visual content in multi-speaker video-to-speech synthesis on GRID, enabling voice control; on unseen speaker identity control the best model reaches about 38.9% WER with 11.9% EER.
- [Sub-word Level Lip Reading With Visual Attention](sub-word-level-lip-reading-with-visual-attention.md) (2021). Camera-only lip reading with WordPiece sub-word units and a visual transformer pooling front-end; reaches 28.9% WER on LRS2 and 40.6% on LRS3 with public-data training (22.6%/30.7% with extended training).
- [FastLTS: Non-Autoregressive End-to-End Unconstrained Lip-to-Speech Synthesis](fastlts-non-autoregressive-end-to-end-unconstrained-lip-to-speech-synthesis.md) (2022). FastLTS is a non-autoregressive end-to-end lip-to-speech system that makes unconstrained synthesis substantially faster without obvious quality loss, evaluated on Lip2Wav and GRID.
- [Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild](lip-to-speech-synthesis-for-arbitrary-speakers-in-the-wild.md) (2022). VAE-GAN lip-to-speech synthesis for arbitrary speakers in the wild; holds up on unconstrained LRW/LRS2, and multi-speaker pretraining with 5 h adaptation nearly matches a 20 h single-speaker model.
- [Multi-modality Associative Bridging through Memory: Speech Sound Recollected from Face Video](multi-modality-associative-bridging-through-memory-speech-sound-recollected-from-face-video.md) (2022). Memory-based cross-modal bridging recalls audio representations from face video, applied to word-level lip reading (LRW/LRW-1000) and speaker-dependent GRID speech reconstruction.
- [SVTS: Scalable Video-to-Speech Synthesis](svts-scalable-video-to-speech-synthesis.md) (2022). SVTS shows a simple spectrogram predictor with a pretrained vocoder outperforms prior complex video-to-speech models and scales to large datasets such as LRS3+VoxCeleb2.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
