# Silent Speech Interfaces in the Era of Large Language Models: A Comprehensive Taxonomy and Systematic Review

Kele Xu, Yifan Wang, Ming Feng, Qisheng Xu, Wuyang Chen, Yutao Dou, Cheng Yang, Huaimin Wang  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2603.11877)

**Section:** [Surveys](../README.md#surveys) · **Review basis:** full_text+summary

Taxonomy and review of silent speech interfaces in the LLM era across neural, EMG, magnetic, ultrasound, optical, acoustic and RF sensing, with benchmark and dataset tables.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Review: multiple SSI sensing modalities |
| Task | Survey |
| Vocabulary | Mixed; varies across cited tasks |
| Speaker | Not stated |
| Session | Not applicable |
| Online / offline | Not applicable |
| Key result | Not reported |

**Limitations.** No reproducible review selection procedure; citation errors and mixed metric scales make its tables unsuitable for rankings or deployment claims.

## Full review

### In short

A broad and useful SSI taxonomy, but missing review-selection detail and concrete citation errors make its benchmark tables unsuitable for unverified rankings or deployment claims.

### Review

This review is useful for orienting readers across neural, muscular, articulatory, imaging and active-sensing approaches to silent speech. Its separation of recognition, direct synthesis and language-model integration helps explain where linguistic priors enter a pipeline and why sensor information, user calibration and computational cost remain important. Its quantitative synthesis needs substantially more caution. Although the title calls it systematic, the paper does not provide a reproducible study-selection and quality-assessment procedure; a Web of Science publication-count figure is not a documented search-and-screening protocol for the review itself. Tables combine small-command accuracy, open-vocabulary error rates, acoustic distortion, auditory-perception decoding and even wrist typing, without the split and calibration details needed for fair comparisons. There are also concrete attribution errors: Table IV assigns a 125,000-word intracortical ALS result with 2.5% WER to reference 132, which the bibliography identifies as Silentspeller, an electropalatography text-entry paper. Table II places references 83 and 88 under ultrasound, although their listed titles concern electro-optical stomatography. These are not merely stylistic issues; they break the path from a claimed result to its evidence. The repeated 15% WER usability threshold and 50 ms latency requirement should therefore be treated as contextual claims, not general acceptance standards demonstrated by this survey. The paper can guide literature discovery and research questions, but its numerical tables should not be imported into a leaderboard or used to infer clinical readiness without checking the original studies.

### Why it matters

A cross-modal reading map that brings language-model priors and generative synthesis into the broader SSI landscape, with numerical claims requiring primary-source verification.

### Prior state of the art

Earlier SSI reviews organize biosignal sensors and recognition/synthesis pipelines. This review adds emphasis on modern generative models, representation alignment and wearable form factors.

### What changed

Connects sensing positions along the speech-production chain with representation learning, direct synthesis and LLM-based correction or embedding alignment.

### Position in the field

Broad SSI synthesis spanning restorative communication, consumer interaction, sensing and generative decoding.

### Practical value

Useful for identifying sensor families, terminology and candidate references; quantitative or clinical decisions should return to source-level evidence.

### Advanced

Breadth of conceptual organization across sensing, recognition, synthesis and language-model integration.

### Unresolved

Reproducible literature coverage, source-accurate quantitative extraction, matched cross-modal comparisons, and validation of broad usability and deployment conclusions.

### Narrowed or regressed

No controlled system regression; citation and table inconsistencies reduce the reliability of the proposed benchmark synthesis.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | survey |
| Input | Survey of neural, EMG, magnetic, ultrasound, optical, acoustic and RF sensing, including adjacent speech resources. |
| Sensor | No new hardware; surveys EEG/ECoG, sEMG, EMA/PMA, ultrasound, MRI, cameras/depth, earables, contact sensors and radar. |
| Body site | brain; face; jaw; lip; oral-cavity; throat; tongue |
| Output | Literature taxonomy, benchmark/dataset tables and research roadmap |
| Vocabulary type | Mixed closed-set, open-vocabulary, reconstruction and adjacent tasks |
| Vocabulary size | Varies across cited tasks from small command sets to large word inventories; no unified evaluated vocabulary. |
| Metrics and results | No new system performance measurement. Tables II-IV reproduce accuracy, WER, CER, PER, MCD, MOS and other values from heterogeneous studies. Some rates appear as proportions and others as percentages. The review repeatedly proposes 15% WER and 50 ms latency thresholds, but supplies no common user study establishing them as universal criteria. |
| Evaluation protocol | Narrative taxonomy and tabulation of published results; no matched benchmark, meta-analysis or new user evaluation. |

### Limits

- **Technical:** Reference mismatches, mixed metric scales, duplicate rows and underspecified cohort/split conditions limit the tables. Statements about inherent noise immunity, recovered intent and universal latency requirements exceed what a heterogeneous narrative review can establish.
- **Evaluation:** No explicit reproducible search query/date, screening counts, eligibility rules, extraction procedure or study-quality assessment is reported. Tables mix recognition, reconstruction, perception, typing and articulator-analysis tasks with incompatible metrics and sparse split details. Citation mismatches and duplicated entries require correction.
- **Deployment:** Wearable, clinical and noisy-environment examples are taken from different cited studies; no integrated system or deployment experiment is performed by this review.
- **Scope of this review:** Narrative synthesis of heterogeneous SSI and adjacent resources. Its tables include listening EEG and wrist typing, which do not directly establish silent speech-production decoding.

### Evidence

- The review organizes SSI sensing along neural, neuromuscular and articulatory stages, then relates recognition, synthesis and language-model methods to these modalities. (Sections II-III; Tables I-IV; PDF pp. 3-10)
- Figure 1 describes Web of Science keyword publication counts for 2011-2025. No explicit study-screening flow, inclusion/exclusion protocol or quality-assessment procedure accompanies the review. (Figure 1; Introduction and review structure; PDF pp. 1-3 and 10-14)
- Table IV attributes an intracortical ALS result with 125,000-word vocabulary and 2.5% WER to reference 132; the bibliography identifies reference 132 as Silentspeller, an electropalatography text-entry paper. (Table IV and Reference 132; PDF pp. 9 and 18)
- Table II classifies references 83 and 88 as UTI, while their bibliography titles explicitly concern electro-optical stomatography. This is a modality-to-reference mismatch. (Table II and References 83/88; PDF pp. 6 and 16-17)
- Tables II-IV combine command accuracy, word/character/phoneme errors, distortion, top-10 perception accuracy and other measures. Evaluation splits and calibration conditions are not systematically tabulated, preventing fair cross-system ranking. (Tables II-IV; PDF pp. 6, 8 and 9)
- Table V includes wrist EMG typing, passive audiobook EEG and auditory-evoked EEG alongside speech-production datasets. Reviewer assessment: these are adjacent resources, not interchangeable silent speech-decoding evidence. (Section IV-B and Table V; PDF pp. 11-12)
- The text repeatedly describes 15% WER as a usability threshold and 50 ms as an end-to-end latency requirement, without a common user evaluation establishing universal applicability across the surveyed tasks. (Sections III-D and IV-A; Section VI-B; PDF pp. 10-11 and 14)
- The language-model discussion distinguishes post-processing, candidate rescoring and direct biosignal-to-embedding alignment, and acknowledges latency costs and over-correction that can diverge from user intent. (Section III-D; PDF pp. 9-10)
- The roadmap identifies user/session variation, missing parallel targets, continual learning, multimodal alignment and privacy as unresolved directions; these are proposed research priorities rather than tested solutions. (Sections IV-C and VI; PDF pp. 11 and 13-14)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
