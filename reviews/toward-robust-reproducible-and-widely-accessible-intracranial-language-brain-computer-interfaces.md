# Toward Robust, Reproducible, and Widely Accessible Intracranial Language Brain-Computer Interfaces: A Comprehensive Review of Neural Mechanisms, Hardware, Algorithms, Evaluation, Clinical Pathways and Future Directions

Dongyi He, Wai Ting Siok, Nizhuan Wang  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2603.12279)

**Section:** [Surveys](../README.md#surveys) · **Review basis:** full_text+summary

Review of intracranial language BCIs covering neural mechanisms, hardware, algorithms, evaluation and clinical pathways, proposing a composite weighted benchmark.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Review: intracortical arrays, ECoG, SEEG |
| Task | Survey |
| Vocabulary | Not applicable |
| Speaker | Not stated |
| Session | Not applicable |
| Online / offline | Not applicable |
| Key result | Not reported |

**Limitations.** Composite benchmark is unvalidated with author-chosen weights; narrative rather than systematic; some source attributions and mechanism claims need correction.

## Full review

### In short

A useful systems-level agenda for speech neuroprostheses, but its composite benchmark is unvalidated and several source attributions and mechanism claims need correction before reuse.

### Review

The strongest contribution of this review is its insistence that speech neuroprostheses be judged as complete communication systems: electrode coverage, calibration burden, user control, latency, voice identity and longitudinal reliability belong alongside decoding accuracy. Its critical synthesis tables and explicit discussion of mixed chronic-stability evidence are useful starting points for planning studies. The proposed numerical benchmark should be treated more cautiously. Direction normalization and weighted averaging make a formula reproducible, but do not establish that heterogeneous tasks or languages measure equivalent user benefit. The default text-rate component saturates at 30 words per minute, for example, so faster systems become indistinguishable on that component; no prospective utility validation or sensitivity analysis is reported. Source attribution also needs correction. Section 4.2 credits a 78-word-per-minute result to Chartier with reference 8, although reference 8 is the Silva review and the paper itself attributes that result to Metzger in Table 1. The discussion further extends SPARC, an audio-to-articulation and speech-synthesis framework, into claims about neural intent and ownership without a corresponding BCI control experiment. Similarly, contextual sequence decoding and saliency are not themselves proof of a causal cortical mechanism. These limitations do not erase the value of the proposed design questions, but they make the review better suited as a structured agenda and checklist than as an authoritative benchmark, primary-result database or validated clinical selection guide.

### Why it matters

Organizes the questions a credible longitudinal communication study should answer, especially calibration, user agency and measurement boundaries.

### Prior state of the art

Speech neuroprosthesis reviews already discuss neural features, decoding and clinical translation. Individual studies report incompatible WER/PER, acoustic correlations, listening scores and latency boundaries, limiting direct comparisons.

### What changed

Connects mechanism, recording choice, experiment design, decoder, evaluation and deployment; proposes utility scores and scenario-specific minimum-system profiles as organizing tools.

### Position in the field

Broad intracranial language-BCI synthesis connecting neural mechanisms to experimental and deployment design, adjacent to non-invasive articulatory SSI.

### Practical value

A useful checklist for research design and reporting after source verification; unsuitable for automatic import of benchmark values or clinical readiness scores.

### Advanced

Makes calibration, user agency, longitudinal stability, heterogeneous hardware and task-specific evaluation explicit parts of the design problem.

### Unresolved

Validation of score weights/ranges, cross-language perceptual calibration, prospective user utility, source-attribution accuracy and evidence for the proposed modality-specific deployment profiles.

### Narrowed or regressed

No measured regression in a new system. Compression into a single normalized score can hide meaningful metric differences and trade-offs.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | survey |
| Input | Primarily intracortical MEA, cortical-surface ECoG and depth SEEG; non-invasive and acoustic studies are included as supporting context. |
| Sensor | Reviews penetrating microelectrode arrays, macro/high-density ECoG and SEEG depth electrodes, with qualitative coverage, resolution, stability and deployment trade-offs. No original acquisition system. |
| Body site | brain |
| Output | literature synthesis and proposed evaluation framework |
| Vocabulary type | Heterogeneous reviewed tasks, not one recognition vocabulary |
| Vocabulary size | Not applicable to this review; cited vocabularies range from fixed commands to large lexical sets. |
| Metrics and results | No original decoder score or measured benchmark result. Table 5 proposes discrete-task weights: WER 0.35, PER 0.20, onset latency 0.15, communication rate 0.10 and perceptual score 0.20. Its rate range is 0-30 wpm and latency range 0-3 s. Other templates cover synthesis, prosody and conversation. All reported accuracy, correlation, speed and stability examples belong to cited studies and are not directly comparable pooled results. |
| Evaluation protocol | Narrative literature synthesis, qualitative decision matrices and proposed direction-normalized weighted benchmark templates; no new experiment or pooled effect estimate. |

### Limits

- **Technical:** Composite scores depend on author-selected clipping ranges and weights; correlated metrics and perceptual proxies may double-count evidence. CTC path factorization does not explicitly model output-label dependencies, and saliency or recurrent-model gains do not independently validate cortical causality.
- **Evaluation:** Narrative rather than reproducibly screened systematic coverage. The composite benchmark is not applied to a shared multilingual cohort, validated against user outcomes or subjected to reported weight/range sensitivity analysis. Underlying studies vary in participant population, speaking mode, output task and measurement boundary.
- **Deployment:** The review itself supplies no prospective deployment validation. Its hardware tables mix acute clinical recording experience with investigational chronic communication systems; supplier examples are expressly illustrative rather than verified procurement or approval guidance.
- **Scope of this review:** Narrative literature review, not a new clinical trial, exhaustive evidence synthesis or validated consensus standard. Primary intracranial studies coexist with acoustic modeling and non-invasive perception examples.

### Evidence

- The review organizes five coupled questions across neural representations, recording, datasets, decoding and deployment, and proposes a unified evaluation framework rather than reporting a new decoder experiment. (Introduction; PDF pp. 2-3)
- Table 2 separates consensus, unresolved disputes, sources of discrepancy and proposed resolving experiments across four neural-mechanism themes. (Table 2; PDF p. 11)
- The deployment utility in Equations 1-2 combines normalized accuracy/responsiveness with infection, power, packaging, care and home-use burdens. No empirical validation of this composite against user outcomes is reported. (Section 3.3; PDF p. 16)
- Equations 3-5 and Table 5 specify clipped normalized metrics, task weights and language/task aggregation. The proposed text-rate component saturates at 30 wpm; reviewer assessment: higher rates receive the same component score, and sensitivity and user-utility validation are needed. (Section 5.3; Table 5; PDF pp. 23-24)
- Section 4.2 attributes 78 wpm to Chartier et al. with reference 8, but reference 8 is the Silva et al. review. Table 1 instead attributes median 78 wpm to Metzger et al. reference 50. Reviewer assessment: the attribution is internally inconsistent. (Table 1; Section 4.2; References 8/50; PDF pp. 4, 19, 32 and 34)
- The paper describes SPARC as an acoustic-to-articulatory framework, yet later interprets its features as controlled by neural intent in a shared-control argument. Reviewer assessment: audio representation disentanglement does not establish BCI user-intent control or ownership. (Sections 4.2 and 6.4; Reference 53; PDF pp. 18-19, 28 and 34)
- The discussion describes CTC as implicitly modeling label dependencies and as an acoustic-linguistic dual path. Reviewer assessment: a contextual encoder and CTC path summation are not an explicit output-label language model or simultaneous acoustic reconstruction. (Sections 2.4 and 4.4; Reference 108; PDF pp. 10, 20 and 37)
- The reliability-first home-use profile recommends ECoG or SEEG, while the hardware matrix explicitly states that chronic unattended SEEG home-use evidence is limited. Reviewer assessment: the profile remains a design heuristic rather than demonstrated modality superiority. (Table 4; Section 6.3; PDF pp. 15 and 27)
- Longitudinal sections contrast selected multimonth speech-control successes with continuing retraining, connectors and setup burden; broad unattended no-recalibration use is not established. (Sections 3.3, 5.5 and 6.2; PDF pp. 15-16, 25 and 27)
- Table 1 combines text decoding, acoustic reconstruction, speech perception, voice conversion and clinical control, with different metrics and populations. Reviewer assessment: these examples should not be pooled into a single performance comparison. (Table 1; PDF p. 4)
- The full review presents narrative coverage and 143 bibliography entries without a reproducible search/screening or evidence-quality audit protocol. Reviewer assessment: comprehensive scope is not proof of exhaustive systematic coverage. (Sections 1-8 and References; PDF pp. 2-39)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
