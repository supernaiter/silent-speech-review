# Voice Activity Detection for Ultrasound-based Silent Speech Interfaces using Convolutional Neural Networks

Amin Honarmandi Shandiz, Laszlo Toth  
arXiv / imported corpus page 2021 · [DOI](https://doi.org/10.1007/978-3-030-83527-9_43) · [arXiv](https://arxiv.org/abs/2105.13718)

**Section:** [Ultrasound & tongue imaging](../README.md#ultrasound--tongue-imaging) · **Review basis:** full_text

CNN speech-versus-silence detection from ultrasound tongue images on one speaker (TaL1), reaching 85.2% test accuracy; removing silence slightly improves downstream SSI reconstruction (MCD 3.05 vs 3.12).

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Ultrasound tongue imaging |
| Task | Speech/silence detection for ultrasound SSI |
| Vocabulary | 2 classes (speech/silence) |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 85.2% test accuracy, F1 0.9, ROC AUC 0.859, single speaker |

**Limitations.** Single-speaker data with speech-derived labels; no cross-speaker validation, live test, or robustness to probe shift and new users.

## Full review

### In short

Preprocessing paper, narrow but legitimate.

### Review

The paper does not solve ultrasound SSI, but it does close a real preprocessing gap. The classifier reaches 85.2% test accuracy with 0.859 ROC AUC on the ultrasound speech/silence task, and the downstream experiment shows that keeping long silence can worsen MCD. The scope remains narrow because everything is single-speaker TaL1 and the gains are incremental rather than transformative.

### Why it matters

The result is modest but real: ultrasound-based speech-versus-silence detection works reasonably well on one speaker, and silence trimming slightly helps downstream SSI reconstruction.

### Prior state of the art

Ultrasound SSI systems usually assumed speech frames or used speech-side VAD labels without testing ultrasound-only VAD itself.

### What changed

Adds an explicit ultrasound VAD stage and checks how silence removal affects articulatory-to-acoustic synthesis metrics.

### Position in the field

Core ultrasound SSI preprocessing paper.

### Practical value

Useful if an ultrasound SSI pipeline needs a simple front-end to drop silence before synthesis.

### Advanced

preprocessing; evaluation

### Unresolved

cross-speaker robustness; real-time deployment; broader corpora

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech/silence detection for ultrasound-based SSI |
| Input | ultrasound tongue images |
| Sensor | ultrasound imaging system |
| Body site | tongue |
| Output | speech/silence labels |
| Vocabulary size | 2 classes |
| Metrics and results | Ultrasound VAD reaches 85.2% test accuracy, F1 0.9, and ROC AUC 0.859; with Conv3D+BiLSTM SSI, removing silence yields test MCD 3.05 versus 3.12 when keeping 180 ms silence |
| Evaluation protocol | single-speaker TaL1 classification accuracy/AUC plus SSI reconstruction with and without silence removal |

### Limits

- **Technical:** Single-speaker data and speech-derived labels limit the result.
- **Evaluation:** No cross-speaker validation or live interactive test is provided.
- **Deployment:** Practical robustness to probe shift, silence styles, and new users is unknown.
- **Scope of this review:** Speech-silence preprocessing for one ultrasound SSI setup.

### Evidence

- The paper first shows silence handling affects SSI quality, then trains a CNN to separate speech and silent ultrasound tongue images. (Abstract)
- The ultrasound speech-silence classifier reaches 0.852 test accuracy, 0.9 F1, and 0.859 ROC AUC. (Table 5.)
- With ultrasound-based VAD and the Conv3D+BiLSTM SSI model, removing silence gives test MCD 3.05 versus 3.12 when keeping 180 ms silence. (Table 7. Training the SSI system with removing or retaining silence from the data)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
