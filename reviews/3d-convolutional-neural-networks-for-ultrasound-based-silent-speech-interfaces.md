# 3D Convolutional Neural Networks for Ultrasound-Based Silent Speech Interfaces

László Tóth, Amin Honarmandi Shandiz  
arXiv / imported corpus page 2021 · [DOI](https://doi.org/10.1007/978-3-030-61401-0_16) · [arXiv](https://arxiv.org/abs/2104.11532)

**Section:** [Ultrasound & tongue imaging](../README.md#ultrasound--tongue-imaging) · **Review basis:** full_text

Shows a compact (2+1)D 3D CNN outperforms 2D CNN and CNN+LSTM models for regressing 13 vocoder parameters from ultrasound tongue video, with lower complexity and training time.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Micro ultrasound system, 64-element convex transducer, 82 fps |
| Task | Vocoder parameter regression from ultrasound |
| Vocabulary | Not applicable |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Not reported |

**Limitations.** Single-speaker read-aloud data, MSE and R2 only, no pitch, no listening or intelligibility tests, and no silent articulation or real-time study.

## Full review

### In short

Temporal context helps, but the evidence is a single-speaker vocoder-parameter study.

### Review

The paper provides a solid but narrow contribution showing that, on a single-speaker ultrasound dataset, a (2+1)D 3D CNN architecture that processes spaced frames (stride s=6, about 300 ms context) outperforms both 2D CNN and a more complex CNN+LSTM model in regression of vocoder coefficients (13 LSP parameters without F0). The 3D CNN yields test MSE of 0.315 and mean R2 of 0.683 compared to 0.366/0.633 for 2D CNN and 0.336/0.661 for CNN+LSTM. The study is limited to speaker-dependent regression, no pitch modeling, no listening tests, and one female Hungarian speaker. The method shows promise as a simpler temporal front-end for ultrasound SSI but requires more robust evaluation and evaluation of perceptual quality before deployment.

### Why it matters

Demonstrates that a compact (2+1)D 3D CNN outperforms 2D CNN and CNN+LSTM models for ultrasound video to speech vocoder parameter regression on a standard dataset, improving regression metrics while reducing model complexity and training time.

### Prior state of the art

Ultrasound SSI systems often processed frames independently or used heavier recurrent stacks to add temporal context.

### What changed

Uses spaced temporal context inside a compact 3D CNN instead of a recurrent sequence model.

### Position in the field

Method paper for speaker-dependent ultrasound-to-acoustic mapping.

### Practical value

Useful as a simpler temporal front-end for ultrasound SSI models when the task is frame-aligned regression of vocoder acoustic features.

### Advanced

algorithm design; model efficiency

### Unresolved

cross-speaker robustness; perceptual quality; silent articulation

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | ultrasound |
| Sensor | Micro ultrasound system by Articulate Instruments Ltd. with 2-4 MHz 64-element convex transducer at 82 fps |
| Body site | tongue |
| Output | speech-audio |
| Metrics and results | Mean squared error (MSE) and mean R2 coefficient for 13 vocoder parameters predicting Mel-Generalized Cepstral Coefficients (LSP representation) without pitch (F0). |
| Evaluation protocol | Development/test objective comparison across FCN, 2D CNN, 3D CNN with various temporal strides, and re-trained CNN+LSTM under matched parameter count. |

### Limits

- **Technical:** Single-speaker data; models 13 vocoder coefficients without pitch; no silent articulation or real-time deployment tested; no subjective quality evaluation.
- **Evaluation:** Only MSE and R2 are reported; there are no listening tests or intelligibility evaluations.
- **Deployment:** No silent articulation scenario, no real-time study, and no robustness-to-probe-shift analysis.
- **Scope of this review:** Speaker-dependent direct speech synthesis from read-aloud ultrasound, not general SSI deployment.

### Evidence

- The paper claims that a compact (2+1)D 3D CNN is a better ultrasound-to-acoustic regressor than 2D CNN and CNN+LSTM baselines. (Abstract)
- Ultrasound tongue videos from one Hungarian female speaker reading 438 sentences were collected, split as 310 train, 41 dev, 87 test. (3 Data Acquisition)
- The model predicts 13 vocoder coefficients representing Mel-Generalized Cepstral Coefficients converted to Line Spectral Pairs (LSPs) standardized per coefficient; pitch (F0) is not estimated. (3 Data Acquisition)
- The 3D CNN processes sequences of 5 ultrasound frames spaced s frames apart; best stride s=6 corresponds to ~300 ms context. (4 Experimental Set-Up)
- 3D CNN with s=6 achieves MSE 0.315 and mean R2 0.683 on test set; 2D CNN MSE 0.366 R2 0.633; CNN+LSTM MSE 0.336 R2 0.661. (5 Results)
- The study is limited to one speaker, 13 vocoder coefficients without pitch, no listening tests, no silent articulation scenario or real-time testing. (6 Conclusions)
- 3D CNN model is smaller and trains faster than CNN+LSTM with five times more parameters; 3D CNN is a viable alternative for ultrasound SSI video regression but not ready for real-world deployment. (6 Conclusions)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
