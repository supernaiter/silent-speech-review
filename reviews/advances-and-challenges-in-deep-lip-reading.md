# Advances and Challenges in Deep Lip Reading

Marzieh Oghbaie, Arian Sabaghi, Kooshan Hashemifard, Mohammad Akbari  
arXiv / imported corpus page 2021 · [arXiv](https://arxiv.org/abs/2110.07879)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

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

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
