# Advances and Challenges in Deep Lip Reading

Marzieh Oghbaie, Arian Sabaghi, Kooshan Hashemifard, Mohammad Akbari  
arXiv 2021 · [arXiv](https://arxiv.org/abs/2110.07879)

**Section:** [Surveys](../README.md#surveys) · **Review basis:** full_text

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

## More reviews in Surveys

- [An Overview of Deep-Learning-Based Audio-Visual Speech Enhancement and Separation](an-overview-of-deep-learning-based-audio-visual-speech-enhancement-and-separation.md) (2020). Survey of deep-learning audio-visual speech enhancement and separation, mapping design choices and noting the lack of standardized audio-visual evaluation.
- [Silent Speech Interfaces for Speech Restoration: A Review](silent-speech-interfaces-for-speech-restoration-a-review.md) (2020). Review of SSI modalities for speech restoration, focusing on deployment bottlenecks such as latency, scarce patient data and modality trade-offs; cites ideal latency of about 50 ms, acceptable up to 100 ms.
- [An Introduction to Silent Paralinguistics](an-introduction-to-silent-paralinguistics.md) (2025). Survey introducing silent paralinguistics: conveying emotion and speaking style, not only content, in silent speech, reviewing biosignal sensing modalities and open research problems without new experiments.
- [Biosignal-Based Spoken Communication: A Survey](biosignal-based-spoken-communication-a-survey.md) (2017). Survey that frames silent speech within biosignal-based spoken communication, spanning articulatory, muscular and neural signals for communication devices, rehabilitation and speech science.
- [Silent Speech Interfaces in the Era of Large Language Models: A Comprehensive Taxonomy and Systematic Review](silent-speech-interfaces-in-the-era-of-large-language-models-a-comprehensive-taxonomy-and-system.md) (2026). Taxonomy and review of silent speech interfaces in the LLM era across neural, EMG, magnetic, ultrasound, optical, acoustic and RF sensing, with benchmark and dataset tables.
- [Toward Robust, Reproducible, and Widely Accessible Intracranial Language Brain-Computer Interfaces: A Comprehensive Review of Neural Mechanisms, Hardware, Algorithms, Evaluation, Clinical Pathways and Future Directions](toward-robust-reproducible-and-widely-accessible-intracranial-language-brain-computer-interfaces.md) (2026). Review of intracranial language BCIs covering neural mechanisms, hardware, algorithms, evaluation and clinical pathways, proposing a composite weighted benchmark.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
