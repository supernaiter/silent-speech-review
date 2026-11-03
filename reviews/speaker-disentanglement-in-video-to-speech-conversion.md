# Speaker disentanglement in video-to-speech conversion

Dan Oneata, Adriana Stan, Horia Cucu  
arXiv 2021 · [arXiv](https://arxiv.org/abs/2105.09652)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

A structured review of *Speaker disentanglement in video-to-speech conversion* (Dan Oneata et al., arXiv 2021) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Disentangles speaker identity from visual content in multi-speaker video-to-speech synthesis on GRID, enabling voice control; on unseen speaker identity control the best model reaches about 38.9% WER with 11.9% EER.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera (silent lip video) plus speaker embedding |
| Task | Video-to-speech synthesis with speaker control |
| Vocabulary | GRID fixed sentence grammar, 52 words |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | About 38.9% WER, 11.9% EER (gradient reversal), unseen speaker identity control, GRID |

**Limitations.** Closed-vocabulary read GRID speech only; intelligibility-control trade-off worsens on unseen speakers and speaker identity or embedding is required at inference.

## Full review

### In short

The paper effectively makes speaker identity a controllable factor in multi-speaker video-to-speech synthesis by disentangling it from content, showing the trade-off between intelligibility and voice control on GRID corpus data.

### Review

This work significantly advances video-to-speech synthesis by introducing explicit speaker identity conditioning through dedicated speaker inputs and adversarial disentanglement losses that remove speaker information from the visual front-end. Leveraging a strong ResNet+Tacotron2 baseline, it enables synthesis in multiple voices, including unseen speakers. The extensive evaluation on the GRID dataset demonstrates that the methods maintain or improve intelligibility while providing voice control. However, there remains a notable trade-off between intelligibility and speaker control for unseen speakers, and the method’s applicability is constrained by the fixed vocabulary and controlled recording conditions of GRID. Nevertheless, the study offers a valuable foundation for controllable lip-to-speech models and outlines important challenges for future deployments in real-world, spontaneous, or open-vocabulary settings.

### Why it matters

Provides an explicit mechanism to separate speaker identity from visual speech content enabling flexible multi-speaker voice control in video-to-speech conversion, overcoming limitations of previous single-speaker or entangled models.

### Prior state of the art

Prior video-to-speech methods assumed a single speaker or implicitly entangled speaker identity with content in visual features without explicit speaker control.

### What changed

Reconceptualizes multi-speaker video-to-speech as a controllable speaker disentanglement task with explicit auxiliary speaker inputs and adversarial disentanglement losses.

### Position in the field

A key reference in multi-speaker controllable video-to-speech synthesis demonstrating explicit speaker disentanglement mechanisms.

### Practical value

Enables personalized and multi-speaker lip-to-speech synthesis with explicit voice control, promising for assistive technologies requiring speaker adaptation.

### Advanced

system_design; evaluation

### Unresolved

Trade-offs remain between intelligibility and speaker control on unseen speakers, with improved disentanglement often decreasing intelligibility.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | video-to-speech synthesis with speaker control |
| Input | video (silent lip region) plus explicit speaker identity or speaker embedding |
| Sensor | camera |
| Body site | face; lip |
| Output | speech-audio |
| Vocabulary type | GRID fixed sentence grammar |
| Vocabulary size | 52 words |
| Metrics and results | On unseen speaker identity control, best results include WER around 38.9% with EER about 11.9% using gradient reversal model; speaker-independent linear model achieves WER 42.7% and EER 7.3%. |
| Evaluation protocol | Objective metrics including WER, EER, STOI, PESQ, MCD; additional listening tests for intelligibility and speaker similarity; speaker embeddings for similarity evaluation. |

### Limits

- **Technical:** Fixed vocabulary; trade-off between intelligibility and speaker control, especially on unseen speakers; no demonstration of open-vocabulary or spontaneous speech generalization.
- **Evaluation:** Evaluated only on closed-vocabulary GRID corpus; intelligibility and speaker control evaluated primarily on synthetic unseen speaker setups without spontaneous or open-vocabulary speech tests.
- **Deployment:** Limited to GRID dataset’s fixed vocabulary and read speech; performance degrades on unseen speakers; requires speaker identity or embedding at inference, limiting zero-shot naturalness and real-world open-vocabulary scenarios.
- **Scope of this review:** Only closed-vocabulary GRID dataset with read speech; unseen speaker testing relies on synthetic pairing, no real-world open-vocabulary evaluation.

### Evidence

- We introduce a new video-to-speech architecture and extend it to multi-speaker scenario by augmenting the network with an additional speaker-related input feeding either a discrete identity or a speaker embedding, enabling control of the target voice and synthesis for unseen identities. (Abstract)
- The model uses adversarial losses that dispel the identity from the video embeddings to better disentangle linguistic content and speaker identity. (Abstract)
- They augment a visual processing front-end (3D conv, ResNet, LSTM) and Tacotron2 decoder with a speaker embedding component injected into the decoder and a speaker classifier applied on visual features to remove speaker information and disentangle content and identity. (III. METHOD DESCRIPTION)
- Experiments are conducted on the GRID corpus dataset with 34,000 samples from 34 speakers and a 52-word fixed vocabulary with fixed sentence grammar. (IV. EXPERIMENTAL RESULTS)
- On unseen speaker control, the best speaker identity normalized rev-grad model achieves WER 38.9% and EER 11.9%; a speaker independent linear rev-grad model obtains WER 42.7% and EER 7.3%. (IV. EXPERIMENTAL RESULTS)
- For speaker-dependent evaluation on 4 speakers, models achieve WER as low as 17.8% (speaker-dependent baseline) and STOI around 0.468, PESQ around 1.85, and MCD around 32 decibels. (IV. EXPERIMENTAL RESULTS)
- The methods are limited to the GRID closed vocabulary and read speech with evaluation on synthetic unseen speaker setups; no results on open vocabulary or spontaneous speech are provided. (V. CONCLUSIONS)
- There is an observed trade-off between content intelligibility and speaker control, especially for unseen speakers, with improvements in disentanglement sometimes degrading intelligibility. (V. CONCLUSIONS)

## More reviews in Lip & face video

- [Sub-word Level Lip Reading With Visual Attention](sub-word-level-lip-reading-with-visual-attention.md) (2021). Camera-only lip reading with WordPiece sub-word units and a visual transformer pooling front-end; reaches 28.9% WER on LRS2 and 40.6% on LRS3 with public-data training (22.6%/30.7% with extended training).
- [FastLTS: Non-Autoregressive End-to-End Unconstrained Lip-to-Speech Synthesis](fastlts-non-autoregressive-end-to-end-unconstrained-lip-to-speech-synthesis.md) (2022). FastLTS is a non-autoregressive end-to-end lip-to-speech system that makes unconstrained synthesis substantially faster without obvious quality loss, evaluated on Lip2Wav and GRID.
- [Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction](learning-audio-visual-speech-representation-by-masked-multimodal-cluster-prediction.md) (2022). Self-supervised audio-visual pretraining (masked multimodal cluster prediction) enabling lipreading at 32.5% WER on LRS3 with only 30 h of labels, and 26.9% with 433 h plus self-training.
- [Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild](lip-to-speech-synthesis-for-arbitrary-speakers-in-the-wild.md) (2022). VAE-GAN lip-to-speech synthesis for arbitrary speakers in the wild; holds up on unconstrained LRW/LRS2, and multi-speaker pretraining with 5 h adaptation nearly matches a 20 h single-speaker model.
- [Multi-modality Associative Bridging through Memory: Speech Sound Recollected from Face Video](multi-modality-associative-bridging-through-memory-speech-sound-recollected-from-face-video.md) (2022). Memory-based cross-modal bridging recalls audio representations from face video, applied to word-level lip reading (LRW/LRW-1000) and speaker-dependent GRID speech reconstruction.
- [SVTS: Scalable Video-to-Speech Synthesis](svts-scalable-video-to-speech-synthesis.md) (2022). SVTS shows a simple spectrogram predictor with a pretrained vocoder outperforms prior complex video-to-speech models and scales to large datasets such as LRS3+VoxCeleb2.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
