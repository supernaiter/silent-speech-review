# Knowledge Distilled Ensemble Model for sEMG-based Silent Speech Interface

Wenqiang Lai, Qihan Yang, Ye Mao, Endong Sun, Jiangnan Ye  
arXiv 2023 · [arXiv](https://arxiv.org/abs/2308.06533)

**Section:** [Surface EMG](../../README.md#surface-emg) · **Review basis:** full_text

A structured review of *Knowledge Distilled Ensemble Model for sEMG-based Silent Speech Interface* (Wenqiang Lai et al., arXiv 2023) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Distills a ResNet ensemble into a lightweight model for spelling via the NATO phonetic alphabet from 3-channel facial sEMG on portable hardware. KDE-SSI reaches 85.9% accuracy on 26 classes with 0.12 ms inference per sample.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 3-channel facial sEMG (BITalino, adhesive Ag/AgCl electrodes) |
| Task | Spelling via NATO alphabet classification |
| Vocabulary | 26 NATO phonetic alphabet words |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 85.9% accuracy, 26-class NATO alphabet, fixed 4:1:1 split; model 21.1 MB, 0.12 ms per sample |

**Limitations.** Only 5 young male subjects, speaker-dependent; adhesive electrodes with precise placement; no unseen-word or cross-session testing.

## Full review

### In short

This paper delivers a practical spelling-focused sEMG silent speech system by compressing a ResNet ensemble into a lightweight model achieving 85.9% accuracy on the NATO alphabet with portable hardware, but remains limited to 5 young male subjects and speaker-dependent scenarios.

### Review

This paper presents a practical silent speech interface based on facial sEMG signals captured from three facial muscles, targeting spelling via the NATO phonetic alphabet. It leverages a ResNet1D backbone ensemble model combined via soft voting (VE-ResNet) achieving up to 88% accuracy on a small dataset of 5 young male subjects. To improve deployment practicality, the ensemble is compressed using knowledge distillation into a lightweight KDE-SSI model, maintaining 85.9% accuracy with much smaller model size and faster inference. The authors demonstrate careful preprocessing, data collection, and system design tying COTS hardware, alphabet-level interaction, and model compression. However, the dataset remains limited in size and demographics, evaluation does not include cross-subject generalization or unseen-word tests, and the system remains speaker-dependent with obtrusive adhesive electrodes. The work is a meaningful step toward portable spelling-oriented silent speech interfaces showing a balanced tradeoff between performance and deployability, but substantial evaluation and refinement are needed for broader real-world deployment.

### Why it matters

The principal contribution is demonstrating that knowledge distillation can compress a strong ensemble silent speech model into a lightweight, low-latency model suitable for practical portable spelling interfaces using the NATO phonetic alphabet over a real 3-channel facial sEMG dataset, addressing the deployment challenges of size and speed while maintaining competitive accuracy.

### Prior state of the art

Prior sEMG SSI research often used small vocabularies or large, complex models with non-portable custom hardware, limiting practical deployment.

### What changed

Uses NATO phonetic alphabet spelling to enable arbitrary word construction and compresses a 6-model ResNet ensemble into a smaller single KDE-SSI model with negligible accuracy loss, improving portability and latency.

### Position in the field

core sEMG SSI paper

### Practical value

High for portable spelling-based silent speech interface applications where model size and low inference latency are critical.

### Advanced

portable_text_entry; model_compression; alphabet_scaling

### Unresolved

speaker_independence; broader_demographics; continuous_language

### Evaluation details

| Item | Details |
| --- | --- |
| Task | text-entry |
| Input | emg |
| Sensor | BITalino MuscleBIT bundle with prefixed electrode distances and adhesive Ag/AgCl electrodes on 3 facial muscles (levator anguli oris, depressor anguli oris, zygomaticus major). |
| Body site | face |
| Output | text |
| Vocabulary type | NATO phonetic alphabet |
| Vocabulary size | 26 classes |
| Metrics and results | KDE-SSI achieved 85.9% accuracy with precision 87.4%, recall 85.7%, and F1-score 0.855 on the 26-class NATO alphabet classification. Ensemble VE-ResNet reached up to 86.0% accuracy. Model sizes were 21.1 MB (KDE-SSI) vs 147.9 MB (VE-ResNet), with inference latency 0.12 ms vs 2.50 ms per sample respectively. |
| Evaluation protocol | 4:1:1 train/validation/test split on whole dataset; experiments compare single ResNet1D, ensemble VE-ResNet, and distilled KDE-SSI models at various ensemble sizes and KD temperatures. |

### Limits

- **Technical:** Model requires adhesive electrodes with precise placement on 3 facial muscles; training data limited to 5 male subjects; method currently speaker-dependent; no generalization to broader users or conditions validated.
- **Evaluation:** Evaluation limited to speaker-dependent scenario with 5 young male subjects; no testing on unseen words or cross-session generalization; accuracy evaluated on fixed 4:1:1 train/val/test split.
- **Deployment:** Requires adhesive skin electrodes and controlled quiet seated posture; only tested on 5 young male subjects; speaker-independent use not demonstrated.
- **Scope of this review:** Focuses on spelling interface via NATO alphabet; not continuous speech decoding or broader language recognition.

### Evidence

- The main contribution of our work is threefold: 1) construct a 26 words NATO phonetic alphabet dataset (3900 data samples in total) from the facial sEMG signals of 5 male subjects; 2) achieve 81.2% test accuracy for the single model on the created dataset; 3) implement a Knowledge Distilled Ensemble Model for Silent Speech Interface (KDE-SSI), a lightweight convolutional network that extracts knowledge from a pre-trained voting ensemble ResNet model (VE-ResNet) while maintaining performance, achieving 85.9% accuracy. (Abstract)
- The dataset consists of 3900 samples, collected from 5 male subjects aged 22 to 24; each subject repeated the 26 NATO phonetic alphabet words 30 times, resulting in 150 samples per class, recorded via BITalino MuscleBIT bundle on 3 facial muscles: levator anguli oris, depressor anguli oris, and zygomaticus major. (II.DATASET)
- KDE-SSI achieves 85.9% accuracy with 87.4% precision, 85.7% recall and 0.855 F1-score on the 26-class NATO phonetic alphabet classification; VE-ResNet teacher ensemble reaches 86.0% accuracy; inference time and model size of KDE-SSI are 0.12 ms and 21.1 MB versus 2.50 ms and 147.9 MB for VE-ResNet. (V.RESULT)
- The evaluation is limited to 5 young male subjects; only speaker-dependent training and testing are conducted; no cross-subject or cross-session robustness analysis; the system requires adhesive electrodes placed on three facial muscles; does not address speaker independence or broader demographics. (II.DATASET)
- The proposed method reduces model size by a factor of 7 and speeds inference by about 20x compared to the teacher ensemble, enabling portable, practical deployment with COTS hardware and low latency, while preserving accuracy. (IV.METHOD)

## More reviews in Surface EMG

- [Sequence-to-Sequence Voice Reconstruction for Silent Speech in a Tonal Language](../sequence-to-sequence-voice-reconstruction-for-silent-speech-in-a-tonal-language/) (2022). SSRNet reconstructs Mandarin speech from five-channel facial sEMG using duration-aware Seq2Seq and tonal multitask learning, cutting ASR CER from 46.62% to 21.99% over the baseline.
- [A Parallel Ultra-Low Power Silent Speech Interface based on a Wearable, Fully-dry EMG Neckband](../a-parallel-ultra-low-power-silent-speech-interface-based-on-a-wearable-fully-dry-emg-neckband/) (2025). A fully dry wearable EMG neckband with ultra-low-power BioGAP-Ultra classifies 8 silently articulated words for one healthy user at 68% accuracy, dropping to 54% on an unseen re-wearing session; acquisition plus BLE uses 22.2 mW.
- [A Silent Speech Decoding System from EEG and EMG with Heterogenous Electrode Configurations](../a-silent-speech-decoding-system-from-eeg-and-emg-with-heterogenous-electrode-configurations/) (2025). Jointly trains on EEG and EMG data with heterogeneous electrode configurations for silent Japanese 64-word classification, reaching 95.3% for eight healthy subjects and 54.5% for one patient (chance 1.6%).
- [Articulatory Feature Prediction from Surface EMG during Speech Production](../articulatory-feature-prediction-from-surface-emg-during-speech-production/) (2025). Predicts 12-dim articulatory features, pitch and loudness from vocalized-speech sEMG and resynthesizes audio with an articulatory synthesizer. Feature correlation is about 0.9 against audio-derived proxy targets, but WER is 15.5% versus 12.6% for the Gaddy baseline (one male speaker).
- [CAT-Net: A Cross-Attention Tone Network for Cross-Subject EEG-EMG Fusion Tone Decoding](../cat-net-a-cross-attention-tone-network-for-cross-subject-eeg-emg-fusion-tone-decoding/) (2025). CAT-Net fuses EEG and surface EMG with cross-attention to classify Mandarin lexical tones in silent articulation, reporting 85.10% leave-one-subject-out accuracy over 4 tones.
- [Confidence-Based Self-Training for EMG-to-Speech: Leveraging Synthetic EMG for Robust Modeling](../confidence-based-self-training-for-emg-to-speech-leveraging-synthetic-emg-for-robust-modeling/) (2025). Uses confidence-filtered synthetic EMG generated from speech, mixed with real data, for EMG-to-speech; on real vocalized EMG from one speaker, WER falls from 23.30% to 21.87%.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
