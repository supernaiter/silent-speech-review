# An Overview of Deep-Learning-Based Audio-Visual Speech Enhancement and Separation

Daniel Michelsanti, Zheng-Hua Tan, Shi-Xiong Zhang, Yong Xu, Meng Yu, Dong Yu, Jesper Jensen  
arXiv 2020 · [arXiv](https://arxiv.org/abs/2008.09586)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

A structured review of *An Overview of Deep-Learning-Based Audio-Visual Speech Enhancement and Separation* (Daniel Michelsanti et al., arXiv 2020) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Survey of deep-learning audio-visual speech enhancement and separation, mapping design choices and noting the lack of standardized audio-visual evaluation.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Microphone and camera (review) |
| Task | Survey |
| Vocabulary | Not applicable |
| Speaker | Not stated |
| Session | Not applicable |
| Online / offline | Not applicable |
| Key result | Not reported |

**Limitations.** Not a primary SSI contribution; no new benchmark or unified re-evaluation, and lack of standardized evaluation limits performance comparisons.

## Full review

### In short

Strong AV speech survey, not an SSI system paper.

### Review

The full text is strong as a survey: it synthesizes how AV speech enhancement and separation systems are built, where visual input helps most, what fusion choices dominate, and why evaluation remains hard to compare across papers. Its practical value is field-mapping rather than new algorithmic evidence. For SSI work, it is adjacent because it touches silent-video speech reconstruction and multimodal speech processing, but it does not introduce a new silent-speech interface or benchmark.

### Why it matters

Good map of AV speech enhancement/separation design choices and evaluation gaps, but not a primary SSI contribution.

### Prior state of the art

AV speech enhancement and separation knowledge was dispersed across modality choices, fusion strategies, datasets, and evaluation practices.

### What changed

Organizes the area into acoustic features, visual features, deep learning methods, fusion techniques, training targets, datasets, and evaluation gaps.

### Position in the field

Survey paper adjacent to SSI via audio-visual speech processing rather than silent-speech interaction itself.

### Practical value

Useful orientation document for choosing AV speech enhancement/separation components and understanding current evaluation weaknesses.

### Advanced

evaluation; problem_reframing

### Unresolved

Standardized AV evaluation; low-resource deployment; robust fusion under real-world conditions

### Evaluation details

| Item | Details |
| --- | --- |
| Task | survey |
| Input | audio + video |
| Sensor | microphone + camera |
| Body site | face; lip |
| Output | speech-audio |
| Metrics and results | Survey identifies PESQ, STOI/ESTOI, SDR/SI-SDR, and WER as common metrics, while noting the lack of standardized audio-visual evaluation procedures |
| Evaluation protocol | literature review |

### Limits

- **Technical:** No new benchmark, no unified re-evaluation, and no direct empirical comparison across systems.
- **Evaluation:** The paper explicitly states that lack of standardized AV evaluation makes broad performance ranking hard to interpret.
- **Deployment:** Not a deployable system; conclusions remain dependent on the underlying papers it surveys.
- **Scope of this review:** Survey of AV speech enhancement and separation, plus adjacent silent-video and non-speech AV source separation work.

### Evidence

- The paper presents an overview of deep-learning-based audio-visual speech enhancement and separation systems, including features, fusion methods, training targets, datasets, and evaluation methods. (XII. C ONCLUSION)
- The conclusion states that visual information benefits both enhancement and separation, and that AV systems can outperform audio-only systems especially at low SNR or when source permutation is an issue. (XII. C ONCLUSION)
- The paper explicitly says that fair comparison is hard because of application-specific constraints and the lack of standardized audio-visual evaluation procedures. (XII. C ONCLUSION)

## More reviews in Lip & face video

- [Speech Prediction in Silent Videos using Variational Autoencoders](speech-prediction-in-silent-videos-using-variational-autoencoders.md) (2020). Variational autoencoder model for speech synthesis from silent lip video that models one-to-many ambiguity; on GRID reports STOI 0.724, ESTOI 0.540 and PESQ 1.932, leading Lip2Wav on ESTOI and PESQ.
- [Vocoder-Based Speech Synthesis from Silent Videos](vocoder-based-speech-synthesis-from-silent-videos.md) (2020). Predicts full vocoder features from silent face video with joint visual speech recognition training on GRID; speaker-dependent model reaches PESQ 1.90 and WER 15.1%, but speaker-independent performance drops sharply.
- [Advances and Challenges in Deep Lip Reading](advances-and-challenges-in-deep-lip-reading.md) (2021). Survey of deep lip reading covering datasets, pipeline modules, challenges and evaluation metrics; contributes no new model or experiments.
- [Speaker disentanglement in video-to-speech conversion](speaker-disentanglement-in-video-to-speech-conversion.md) (2021). Disentangles speaker identity from visual content in multi-speaker video-to-speech synthesis on GRID, enabling voice control; on unseen speaker identity control the best model reaches about 38.9% WER with 11.9% EER.
- [Sub-word Level Lip Reading With Visual Attention](sub-word-level-lip-reading-with-visual-attention.md) (2021). Camera-only lip reading with WordPiece sub-word units and a visual transformer pooling front-end; reaches 28.9% WER on LRS2 and 40.6% on LRS3 with public-data training (22.6%/30.7% with extended training).
- [Lipper: Synthesizing Thy Speech using Multi-View Lipreading](lipper-synthesizing-thy-speech-using-multi-view-lipreading.md) (2019). Lipper reconstructs speech from multi-view lip video on OuluVS2 as a regression problem; the best three-view setting reaches PESQ 2.315 with 0.169 s end-to-end delay, though audio remains robotic.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
