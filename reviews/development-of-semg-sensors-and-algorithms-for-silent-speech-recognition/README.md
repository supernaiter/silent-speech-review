# Development of sEMG sensors and algorithms for silent speech recognition

Geoffrey S. Meltzner, James T. Heaton, Yunbin Deng, Gianluca De Luca, Serge H. Roy, Joshua C. Kline  
Journal of Neural Engineering 15(4), 046031 2018 · [DOI](https://doi.org/10.1088/1741-2552/aac965)

**Section:** [Surface EMG](../../README.md#surface-emg) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *Development of sEMG sensors and algorithms for silent speech recognition* (Geoffrey S. Meltzner et al., Journal of Neural Engineering 15(4), 046031 2018) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Face- and neck-worn sEMG sensors with staged recognition algorithms decode silently mouthed phrases; abstract reports 8.9% WER on 1,200+ phrases from a 2,200-word vocabulary.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Face- and neck-worn surface EMG sensors |
| Task | Silent speech recognition to text |
| Vocabulary | 2,200-word vocabulary, 1,200+ phrases |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Not stated |
| Key result | 8.9% WER (91.1% recognition rate), 2,200-word vocabulary |

**Limitations.** Reviewed from the abstract only; participants, speaker dependence, grammar constraints and session design were not verified.

## Full review

### In short

Important large-vocabulary sEMG silent speech result (8.9% WER, 2,200 words); reviewed from the abstract only.

### Review

This paper reports one of the strongest pre-deep-learning sEMG silent speech recognition results: face- and neck-worn sensors with algorithms developed in stages, from isolated words to grammar-constrained word sequences to phoneme-based models that recognize previously untrained words. The abstract reports an 8.9% WER (91.1% recognition rate) on more than 1,200 phrases from a 2,200-word vocabulary and frames applications for laryngectomy, covert communication and private phone use. The full text could not be retrieved for this review, so sensor count and placement, number of participants, speaker dependence, grammar constraints and session design are unverified; the vocabulary size alone does not establish open-vocabulary performance if a task grammar constrains decoding.

### Why it matters

Evidence that wearable sEMG with phoneme-based modeling can scale silently mouthed recognition to a vocabulary in the low thousands, an important bar for later EMG SSI work.

### Prior state of the art

sEMG silent speech recognition was mostly limited to small isolated-word vocabularies with taped laboratory electrodes.

### What changed

Purpose-built face and neck sEMG sensors plus staged recognition (isolated words, grammar-based sequences, phoneme models for untrained words) reach low WER on a 2,200-word vocabulary.

### Position in the field

Key sEMG SSI reference for vocabulary scaling and clinical (laryngectomy) motivation.

### Practical value

Benchmark-level reference for large-vocabulary EMG SSI; details needed to judge comparability were not verifiable here.

### Advanced

vocabulary_scale; sensor_design; phoneme_based_generalization

### Unresolved

Speaker independence; grammar-free open vocabulary; cross-session robustness (all unverified)

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-recognition |
| Input | surface emg |
| Sensor | face- and neck-worn sEMG sensors |
| Body site | face; throat |
| Output | text |
| Vocabulary type | large vocabulary phrases (grammar details unverified) |
| Vocabulary size | 2,200 words |
| Metrics and results | 8.9% WER (91.1% recognition rate) on more than 1,200 phrases from a 2,200-word vocabulary (abstract) |
| Evaluation protocol | staged evaluation from isolated words to grammar-based sequences and phoneme-based recognition of untrained words (details unverified) |

### Limits

- **Technical:** Not verifiable from the abstract beyond reliance on custom face and neck sEMG sensors.
- **Evaluation:** Only the 8.9% WER on 1,200+ phrases from a 2,200-word vocabulary is verifiable; grammar constraints, participants and splits were not checked.
- **Deployment:** Requires face- and neck-worn sEMG sensors; real-time or field use not verifiable from the abstract.
- **Scope of this review:** Silent (mouthed) speech recognition to text from sEMG.

### Evidence

- The abstract describes face- and neck-worn sEMG sensors and algorithms for recognizing silently mouthed words and phrases, developed from isolated words to grammar-based word sequences to phoneme-based models for untrained words. (Abstract (Europe PMC / ADS))
- The abstract reports an 8.9% word error rate (91.1% recognition rate) on more than 1,200 phrases from a 2,200-word vocabulary. (Abstract (Europe PMC / ADS))
- The abstract names applications for laryngectomy patients, covert military communication and private phone use in public. (Abstract (Europe PMC / ADS))
- The full text (PMC6168082) could not be retrieved for this review; sensor count, participants, speaker dependence and grammar constraints are unverified. (Reviewer note)

## More reviews in Surface EMG

- [AlterEgo: A Personalized Wearable Silent Speech Interface](../alterego-a-personalized-wearable-silent-speech-interface/) (2018). Wearable headset that recognizes silently articulated words from face and jaw neuromuscular signals and answers through bone-conduction audio; abstract reports 92% median word accuracy in user studies.
- [Digital Voicing of Silent Speech](../digital-voicing-of-silent-speech/) (2020). Synthesizes speech from silent facial EMG by transferring audio targets from vocalized recordings; human WER reaches 3.6% on closed vocabulary, while open-vocabulary WER drops from 95.1% to 74.8%.
- [An Improved Model for Voicing Silent Speech](../an-improved-model-for-voicing-silent-speech/) (2021). Improves open-vocabulary silent-speech voicing from facial EMG using learned convolutional features, a Transformer and auxiliary phoneme loss, cutting WER from 68.0% to 42.2% (automatic) and 32.3% (human) for one speaker.
- [Sequence-to-Sequence Voice Reconstruction for Silent Speech in a Tonal Language](../sequence-to-sequence-voice-reconstruction-for-silent-speech-in-a-tonal-language/) (2022). SSRNet reconstructs Mandarin speech from five-channel facial sEMG using duration-aware Seq2Seq and tonal multitask learning, cutting ASR CER from 46.62% to 21.99% over the baseline.
- [Knowledge Distilled Ensemble Model for sEMG-based Silent Speech Interface](../knowledge-distilled-ensemble-model-for-semg-based-silent-speech-interface/) (2023). Distills a ResNet ensemble into a lightweight model for spelling via the NATO phonetic alphabet from 3-channel facial sEMG on portable hardware. KDE-SSI reaches 85.9% accuracy on 26 classes with 0.12 ms inference per sample.
- [A Parallel Ultra-Low Power Silent Speech Interface based on a Wearable, Fully-dry EMG Neckband](../a-parallel-ultra-low-power-silent-speech-interface-based-on-a-wearable-fully-dry-emg-neckband/) (2025). A fully dry wearable EMG neckband with ultra-low-power BioGAP-Ultra classifies 8 silently articulated words for one healthy user at 68% accuracy, dropping to 54% on an unseen re-wearing session; acquisition plus BLE uses 22.2 mW.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
