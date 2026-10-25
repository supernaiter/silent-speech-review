# An Overview of Deep-Learning-Based Audio-Visual Speech Enhancement and Separation

['', '', '', '', '', '', '']  
arXiv / imported corpus page 2020 · [arXiv](https://arxiv.org/abs/2008.09586)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

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

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
