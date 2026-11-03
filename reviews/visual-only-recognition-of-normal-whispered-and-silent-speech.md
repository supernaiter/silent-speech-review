# Visual-Only Recognition of Normal, Whispered and Silent Speech

Stavro Petridis, Jie Shen, Doruk Cetin, Maja Pantic  
arXiv 2018 · [arXiv](https://arxiv.org/abs/1802.06399)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

A structured review of *Visual-Only Recognition of Normal, Whispered and Silent Speech* (Stavro Petridis et al., arXiv 2018) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Compares visual-only recognition of normal, whispered and silent speech, showing silent speech is a distinct regime: matched-condition silent accuracy is 62.2% (digits) and training on normal speech lowers it further.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Three cameras (frontal, 45-degree, profile views) |
| Task | Closed-set visual speech recognition |
| Vocabulary | 10 digits and 10 short phrases |
| Speaker | Speaker-independent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Silent speech 62.2% digits / 64.4% phrases (matched training); 59.7% / 61.2% when trained on normal speech |

**Limitations.** Closed vocabulary, laboratory recordings only, accuracy far from practical silent communication, and no live interface shown.

## Full review

### In short

Strong evidence that silent lipreading needs dedicated training.

### Review

The value of the paper is empirical clarity. It records a reasonably sized three-mode database and shows that silent speech underperforms both normal and whispered speech even in matched conditions, while mismatched training makes things worse. In the digits experiment, silent matched performance is 62.2% and normal-trained testing on silent drops to 59.7%. In the phrases experiment, silent matched performance is 64.4% and normal-trained testing on silent drops to 61.2%. That makes the main lesson hard to ignore: silent visual speech should be treated as its own training regime rather than borrowed from vocalized lipreading.

### Why it matters

This is a core SSI result because the full text shows silent visual speech is a distinct regime, not just a slightly harder version of normal lipreading.

### Prior state of the art

Visual speech systems often assumed that vocalized data would transfer acceptably to whispered or silent speech.

### What changed

The paper tests that assumption directly and shows silent speech is consistently worse and not well served by vocalized-only training.

### Position in the field

Important visual-only SSI benchmark and transfer-analysis paper.

### Practical value

High for anyone building camera-based silent speech systems or designing training data collection.

### Advanced

dataset coverage; evaluation; problem framing

### Unresolved

open vocabulary; real-world capture; broader participant diversity

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech recognition |
| Input | visual speech video across normal, whispered, and silent modes |
| Sensor | Three cameras capturing frontal, 45-degree, and profile views at 1280x780 and 30 fps |
| Body site | face / lips |
| Output | text |
| Vocabulary type | digits and short phrases |
| Vocabulary size | 10 digits and 10 fixed short phrases |
| Metrics and results | Digits matched-condition classification rates are 68.0% for normal, 70.5% for whispered, and 62.2% for silent speech. Phrases matched-condition rates are 69.7%, 70.8%, and 64.4%, while training on normal and testing on silent drops to 59.7% for digits and 61.2% for phrases. |
| Evaluation protocol | Repeated subject-independent train / validation / test experiments for digits and phrases, with matched and mismatched train-test speech modes. |

### Limits

- **Technical:** The task remains closed-vocabulary and laboratory-recorded, and the reported recognition rates are still far from practical open-ended silent communication.
- **Evaluation:** Only digits and fixed phrases are evaluated; there is no open-vocabulary or in-the-wild test.
- **Deployment:** No real deployment or live camera interface is shown.
- **Scope of this review:** Visual-only closed-vocabulary SSI recognition study.

### Evidence

- The database contains 53 participants for digits and 39 participants for phrases, recorded in normal, whispered, and silent speech with frontal, 45-degree, and profile cameras. (2. DATABASE DESCRIPTION)
- In the digits experiment, Table 1 reports matched-condition classification rates of 68.0% for normal, 70.5% for whispered, and 62.2% for silent speech, while normal-trained testing on silent drops to 59.7%. (Table 1. Mean classification rate (and standard deviation) for the digits experiment.)
- In the phrases experiment, Table 2 reports matched-condition classification rates of 69.7% for normal, 70.8% for whispered, and 64.4% for silent speech, while normal-trained testing on silent drops to 61.2%. (Table 2. Mean classification rate (and standard deviation) for the phrases experiment.)
- The conclusion states that using vocalized training data for a silent speech recognition system is not the best approach because performance on silent speech suffers the most. (6. CONCLUSION)

## More reviews in Lip & face video

- [Harnessing AI for Speech Reconstruction using Multi-view Silent Video Feed](harnessing-ai-for-speech-reconstruction-using-multi-view-silent-video-feed.md) (2018). Reconstructs speech audio from multi-view silent video on OuluVS2 with CNN-LSTM models, showing multi-view input improves PESQ over single view and that camera placement matters.
- [Lipper: Synthesizing Thy Speech using Multi-View Lipreading](lipper-synthesizing-thy-speech-using-multi-view-lipreading.md) (2019). Lipper reconstructs speech from multi-view lip video on OuluVS2 as a regression problem; the best three-view setting reaches PESQ 2.315 with 0.169 s end-to-end delay, though audio remains robotic.
- [Video-Driven Speech Reconstruction using Generative Adversarial Networks](video-driven-speech-reconstruction-using-generative-adversarial-networks.md) (2019). Uses a GAN to generate speech audio directly from silent frontal face video on GRID; speaker-dependent WER is 26.6%, while unseen speakers degrade to 40.5% WER.
- [Improved Speech Reconstruction from Silent Video](improved-speech-reconstruction-from-silent-video.md) (2017). Reconstructs speech from silent full-face video plus optical flow with a CNN and temporal post-processing network, outperforming prior methods on GRID and TCD-TIMIT in objective metrics and human word accuracy.
- [Lip2AudSpec: Speech reconstruction from silent lip movements video](lip2audspec-speech-reconstruction-from-silent-lip-movements-video.md) (2017). Lip2AudSpec reconstructs speech from silent lip video using an auditory-spectrogram autoencoder bottleneck as target, improving objective intelligibility metrics and human word accuracy (55.8% vs 50.9%) over a baseline on four GRID speakers.
- [Seeing Through Noise: Visually Driven Speaker Separation and Enhancement](seeing-through-noise-visually-driven-speaker-separation-and-enhancement.md) (2017). Uses visual speech predictions from face video to build masks that separate or enhance a target speaker from audio mixtures, beating audio-only separation on GRID and TCD-TIMIT. Not an SSI paper.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
