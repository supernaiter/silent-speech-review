# Ultra2Speech -- A Deep Learning Framework for Formant Frequency Estimation and Tracking from Ultrasound Tongue Images

Pramit Saha, Yadong Liu, Bryan Gick, Sidney Fels  
arXiv / imported corpus page 2020 · [arXiv](https://arxiv.org/abs/2006.16367)

**Section:** [Ultrasound & tongue imaging](../README.md#ultrasound--tongue-imaging) · **Review basis:** full_text

Estimates and tracks formant frequencies from ultrasound tongue image sequences for speech synthesis; best U2F configuration reaches mean R2 99.96 on joint f1-f2 prediction versus 90.01 for a Conv-BiLSTM baseline.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Ultrasound probe (tongue images) |
| Task | Formant estimation from ultrasound |
| Vocabulary | Not applicable |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Mean R2 99.96 on joint f1-f2 prediction vs 90.01 baseline |

**Limitations.** Focuses on formant tracking and vowel trajectories rather than full speech reconstruction; single collected dataset, no cross-speaker or real-time device evaluation.

## Full review

### In short

Strong ultrasound SSI paper with unusually clear quantitative gains.

### Review

The full text shows this is more than a formant-regression curiosity. U2F cleanly beats the Conv-BiLSTM and plain 3D CNN baselines, and the joint f1-f2 result at 99.96 mean R2 is far above the recurrent baseline. The interesting systems insight is that hybrid spatial-temporal blocks plus channel shuffling are not cosmetic: the ablations show each piece contributes, and the conclusion frames the model as a path toward less manual tongue-contour extraction in SSI pipelines.

### Why it matters

A strong SSI paper because it turns ultrasound tongue video into a high-quality articulatory-to-acoustic mapping problem with convincing quantitative gains.

### Prior state of the art

Ultrasound SSI work often depended on handcrafted tongue features or weaker sequence models.

### What changed

U2F uses hybrid 2D spatial and 1D temporal convolutions with shuffling to learn end-to-end formant tracking from raw ultrasound clips.

### Position in the field

Core ultrasound-based SSI work for speech restoration.

### Practical value

Useful as a full-text-backed reference for ultrasound-to-acoustic mapping and articulatory feature learning.

### Advanced

ultrasound_ssi; articulatory_to_acoustic_mapping; tongue_tracking

### Unresolved

broader speech coverage and real-time patient deployment remain unresolved.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | ultrasound tongue image sequences |
| Sensor | ultrasound probe |
| Body site | tongue; oral-cavity |
| Output | speech-audio |
| Metrics and results | The best U2F configuration reaches mean R2 99.96 on joint f1-f2 prediction, versus 90.01 for the Conv-BiLSTM baseline on the same joint task. |
| Evaluation protocol | train-dev-test split on ultrasound videos with MAE and mean R2 plus baseline and ablation comparisons |

### Limits

- **Technical:** The reported system focuses on formant tracking and synthesized vowel trajectories rather than full open-vocabulary speech reconstruction.
- **Evaluation:** Evaluation is on the collected ultrasound dataset and does not establish cross-speaker clinical deployment.
- **Deployment:** The work motivates SSI use but does not present a real-time deployed device.
- **Scope of this review:** Ultrasound tongue-image to formant / synthesized speech pipeline.

### Evidence

- The abstract says U2F maps ultrasound tongue images to formant trajectories and then synthesizes continuous vowel trajectories with a Klatt synthesizer. (Abstract)
- Table 1 reports the best U2F configuration at mean R2 99.96 on joint f1-f2 prediction, outperforming the recurrent and standard 3D CNN baselines. (Table 1. Performance comparison with baseline methods)
- The discussion lists the hybrid spatial-temporal feature extraction and channel shuffling as the central architectural contribution. (5    Discussion and Conclusion)
- The paper evaluates end-to-end mapping to formant frequencies and vowel trajectories, not a full open-vocabulary speech restoration benchmark. (5    Discussion and Conclusion)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
