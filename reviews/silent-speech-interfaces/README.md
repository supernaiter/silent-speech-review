# Silent speech interfaces

Bruce Denby, Tanja Schultz, Kiyoshi Honda, Thomas Hueber, James M. Gilbert, Jonathan S. Brumberg  
Speech Communication 52(4), 270-287 2010 · [DOI](https://doi.org/10.1016/j.specom.2009.08.002)

**Section:** [Surveys](../../README.md#surveys) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *Silent speech interfaces* (Bruce Denby et al., Speech Communication 52(4), 270-287 2010) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Founding review that defines silent speech interfaces, surveys seven sensing technologies from EMA to intracortical implants, and scores them on six practical criteria; concludes no technology meets all of them.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Seven SSI technology families (review) |
| Task | Survey |
| Vocabulary | Not applicable |
| Speaker | Not stated |
| Session | Not applicable |
| Online / offline | Not applicable |
| Key result | Not reported |

**Limitations.** Pre-deep-learning review; cited results are small-vocabulary and heterogeneous, and the comparison scores are qualitative.

## Full review

### In short

The founding SSI review: defines the field and its seven sensing families, but its numbers are pre-deep-learning.

### Review

This special-issue overview is the paper that named and scoped silent speech interfaces as speech processing without an intelligible acoustic signal. It organizes the field into seven technology families (EMA/magnetic sensing, ultrasound and optical imaging of tongue and lips, NAM microphones, glottal EM/vibration sensors, surface EMG, EEG and intracortical implants) and motivates them through three application drivers: speech-handicapped users such as laryngectomees, private phone use in quiet places, and noisy environments. Its six-criterion comparison table (works in silence, in noise, for laryngectomy, non-invasive, ready for market, low cost) remains a useful lens, and the challenge list (sensor positioning, speaker independence, Lombard/silent-speech effects, prosody, limited dictionaries) is still largely open. The cited performance numbers are early small-vocabulary results and should not be used as current baselines.

### Why it matters

Defines the SSI problem space and the evaluation criteria still used to compare modalities; essential historical framing rather than technical evidence.

### Prior state of the art

Work on non-acoustic speech sensing was scattered across speech production research, speech pathology, telecom privacy and BCI, without a shared name or comparison frame.

### What changed

Unifies these lines under the SSI label, surveys seven demonstrator technologies, scores them on six practical criteria and lists common challenges and future directions.

### Position in the field

Foundational reference for the SSI field; the standard citation for its definition and modality taxonomy.

### Practical value

Useful for framing and for the modality comparison criteria; numeric results are historical only.

### Advanced

field_definition; modality_taxonomy; deployment_criteria

### Unresolved

Speaker independence; sensor positioning robustness; silent-vs-vocalized mismatch; prosody; large vocabularies

### Evaluation details

| Item | Details |
| --- | --- |
| Task | survey |
| Input | non-acoustic articulatory, muscular and neural signals (review) |
| Sensor | review of EMA/magnetic, imaging, NAM, glottal EM/vibration, sEMG, EEG and intracortical sensors |
| Body site | brain; face; lip; throat; tongue |
| Metrics and results | Cites early results such as over 90% recognition for EMA on 9 words and 13 phonemes, 93% sEMG accuracy on English digits, about 70% sEMG accuracy on 100 words, and about 60% correct phonetic targets for ultrasound/optical recognition from a one-hour two-speaker database |
| Evaluation protocol | narrative review with a six-criterion, 1-5 scored comparison of seven SSI technologies |

### Limits

- **Technical:** Review article; reported results come from early systems with small vocabularies and heterogeneous protocols.
- **Evaluation:** No unified benchmark; the comparison table uses author-assigned 1-5 scores rather than measured quantities.
- **Deployment:** Concludes that no technology met all six criteria at the time; does not itself resolve deployment barriers.
- **Scope of this review:** Survey of SSI technologies up to about 2009.

### Evidence

- The abstract defines SSIs as systems enabling speech communication without an intelligible acoustic signal and presents demonstrators built on seven technology types. (Abstract)
- Section III reviews EMA/magnetic sensing, ultrasound and optical imaging of tongue and lips, NAM microphones, glottal EM/vibration sensors, surface EMG, EEG and intracortical implants. (Section III.A-III.G)
- The sEMG section cites 93% accuracy on English digits, 92% on six control words, and around 70% on 100 words, with up to 90% speaker-dependent results. (Section III.E)
- Section IV.B scores each technology from 1 to 5 on working in silence, in noise, for laryngectomy, non-invasiveness, market readiness and cost. (Section IV.B, comparison table)
- Section IV.A lists common challenges: sensor positioning and robustness, speaker independence, Lombard and silent-speech effects, prosody and nasality, and limited dictionary size. (Section IV.A)

## More reviews in Surveys

- [Biosignal-Based Spoken Communication: A Survey](../biosignal-based-spoken-communication-a-survey/) (2017). Survey that frames silent speech within biosignal-based spoken communication, spanning articulatory, muscular and neural signals for communication devices, rehabilitation and speech science.
- [An Overview of Deep-Learning-Based Audio-Visual Speech Enhancement and Separation](../an-overview-of-deep-learning-based-audio-visual-speech-enhancement-and-separation/) (2020). Survey of deep-learning audio-visual speech enhancement and separation, mapping design choices and noting the lack of standardized audio-visual evaluation.
- [Silent Speech Interfaces for Speech Restoration: A Review](../silent-speech-interfaces-for-speech-restoration-a-review/) (2020). Review of SSI modalities for speech restoration, focusing on deployment bottlenecks such as latency, scarce patient data and modality trade-offs; cites ideal latency of about 50 ms, acceptable up to 100 ms.
- [Advances and Challenges in Deep Lip Reading](../advances-and-challenges-in-deep-lip-reading/) (2021). Survey of deep lip reading covering datasets, pipeline modules, challenges and evaluation metrics; contributes no new model or experiments.
- [An Introduction to Silent Paralinguistics](../an-introduction-to-silent-paralinguistics/) (2025). Survey introducing silent paralinguistics: conveying emotion and speaking style, not only content, in silent speech, reviewing biosignal sensing modalities and open research problems without new experiments.
- [Silent Speech Interfaces in the Era of Large Language Models: A Comprehensive Taxonomy and Systematic Review](../silent-speech-interfaces-in-the-era-of-large-language-models-a-comprehensive-taxonomy-and-system/) (2026). Taxonomy and review of silent speech interfaces in the LLM era across neural, EMG, magnetic, ultrasound, optical, acoustic and RF sensing, with benchmark and dataset tables.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
