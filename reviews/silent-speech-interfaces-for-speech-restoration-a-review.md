# Silent Speech Interfaces for Speech Restoration: A Review

Jose A. Gonzalez-Lopez, Alejandro Gomez-Alanis, Juan M. Martin-Donas, Jose L. Perez-Cordoba, Angel M. Gomez  
arXiv / imported corpus page 2020 · [DOI](https://doi.org/10.1109/ACCESS.2020.3026579) · [arXiv](https://arxiv.org/abs/2009.02110)

**Section:** [Surveys](../README.md#surveys) · **Review basis:** full_text

Review of SSI modalities for speech restoration, focusing on deployment bottlenecks such as latency, scarce patient data and modality trade-offs; cites ideal latency of about 50 ms, acceptable up to 100 ms.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Multimodal biosignal and articulator sensors (review) |
| Task | Survey |
| Vocabulary | Not applicable |
| Speaker | Not stated |
| Session | Not applicable |
| Online / offline | Not applicable |
| Key result | Not reported |

**Limitations.** A review that synthesizes uneven prior results without a unified benchmark and does not itself resolve deployment obstacles.

## Full review

### In short

Core SSI survey with concrete deployment constraints.

### Review

The full text is strongest where it stops being a catalog and starts naming bottlenecks. The latency discussion is unusually concrete, arguing that 50 ms is ideal and 100 ms may still be acceptable, which sharply favors direct synthesis over slower ASR-TTS cascades. The later challenge section also makes clear that SSI progress is held back less by model fashion than by tiny patient datasets, weak public data availability, and difficult real-world sensor placement.

### Why it matters

A strong field survey that is most useful for identifying what blocks SSI deployment: latency, scarce patient data, and modality-specific tradeoffs.

### Prior state of the art

SSI literature was fragmented across modalities and clinical populations.

### What changed

This review consolidates the sensing landscape and makes latency, patient data scarcity, and deployment practicality explicit cross-cutting bottlenecks.

### Position in the field

Core SSI background review for speech-restoration framing.

### Practical value

Useful as a top-level map of SSI modalities and system bottlenecks.

### Advanced

field_mapping; latency_requirements; modality_tradeoffs

### Unresolved

patient-scale data, robust public datasets, and clinically viable deployment remain unresolved.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | survey |
| Input | non-acoustic biosignals and articulator sensing |
| Sensor | multimodal biosignal sensors |
| Body site | brain; face; lip; oral-cavity; throat; tongue |
| Metrics and results | The review cites an ideal SSI latency of about 50 ms, acceptable latency up to 100 ms, and disruptive delayed-feedback effects by 200 ms. |
| Evaluation protocol | comparative review of sensing modalities, restoration scenarios, latency requirements, and dataset constraints |

### Limits

- **Technical:** It is a review and therefore inherits the uneven quality and comparability of the literature it summarizes.
- **Evaluation:** The paper synthesizes prior results rather than running a unified benchmark.
- **Deployment:** It identifies many deployment obstacles but does not itself resolve them.
- **Scope of this review:** Speech-restoration SSI review, not a new system.

### Evidence

- The abstract frames the paper as a review of SSI research for speech restoration using non-acoustic biosignals and articulator sensing. (Abstract)
- The latency discussion states that 50 ms is ideal for SSI, values up to 100 ms may still be acceptable, and larger delays disrupt communication. (IV. SENSING TECHNIQUES)
- The challenges section says SSI studies mostly rely on small datasets recorded by different groups and that public datasets remain a major bottleneck. (V. C URRENT CHALLENGES AND FUTURE RESEARCH)
- The review explicitly covers brain activity sensors, muscle activity sensors, and articulator tracking as alternative SSI sensing routes. (IV. S ENSING TECHNIQUES)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
