# Continuous Silent Speech Recognition using EEG

Gautam Krishna, Co Tran, Mason Carnahan, Ahmed H Tewfik  
arXiv / imported corpus page 2020 · [arXiv](https://arxiv.org/abs/2002.03851)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text

Decodes continuous sentences from 31-channel scalp EEG recorded during silent reading using CTC and a 4-gram language model; WER is very high (about 75-84%), showing feasibility only.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 31-channel wet scalp EEG cap (10-20 montage) |
| Task | Continuous silent speech recognition from EEG |
| Vocabulary | 30 unique English sentences |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | WER ~74.9-84.2% across 12-72 sentence test sets; cross-subject WER 92.55% |

**Limitations.** Very small dataset (four subjects, 30 sentences), very high WER, poor cross-subject generalization, no real-time validation, full wet EEG cap required.

## Full review

### In short

Real EEG sentence-level silent speech recognition is demonstrated but at very high WER, confirming feasibility only and underscoring the immature state of current EEG silent speech technology.

### Review

This paper represents an important proof-of-concept for continuous silent speech recognition from real EEG signals. Using a comprehensive recording from 31 scalp sensors, handcrafted EEG features, KPCA compression, and a GRU+TCN CTC-based ASR model, the authors demonstrate decoding of silently read English sentences. Despite the novelty of continuous sentence-level decoding, performance remains far from practical, with within-subject WER averaging 83.34% and cross-subject WER degrading further to 92.55%. The small dataset of 30 sentences from four subjects limits robustness and generalizability. Real-time capability is unreported. Nonetheless, the work expands the experimental scope of EEG silent speech research, setting a challenging baseline and highlighting substantial challenges ahead for real deployment.

### Why it matters

The work extends EEG silent speech research from small-vocabulary or passive listening setups to continuous sentence recognition with real EEG, providing a candid benchmark of high error rates and subject variability that clarifies feasibility and informs future model and dataset design.

### Prior state of the art

Prior EEG silent speech work mostly focused on isolated commands, small vocabularies, or passive listening rather than imagined sentence reading with continuous decoding.

### What changed

Expansion from discrete word or command recognition to continuous sentence-level EEG silent speech decoding with CTC-based deep model and KPCA feature compression.

### Position in the field

A significant EEG silent speech reference for continuous sentence decoding that underscores current technological and data limitations.

### Practical value

Provides an important baseline for continuous silent speech decoding from EEG and encourages research toward improved modeling and datasets; currently not practical for real-world use.

### Advanced

Evaluation: single-word or small-vocabulary EEG silent speech recognition to continuous sentence decoding; Modality: EEG signal processing with feature engineering and deep CTC ASR.

### Unresolved

Cross-subject transfer robustness and real-time system feasibility remain unresolved.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | Continuous silent speech recognition from EEG. |
| Input | 31-channel scalp EEG recorded while subjects silently read sentences mentally. |
| Sensor | 32-electrode (31 EEG + ground) wet EEG cap with sensors placed according to standard 10-20 montage. |
| Body site | brain |
| Output | Text (decoded English sentences) |
| Vocabulary type | English read sentences silently (imagined speech). |
| Vocabulary size | 30 unique sentences, 72 total sentences used in testing. |
| Metrics and results | Word error rate (WER) averages from ~74.86% to 84.22% across 12 to 72 sentence test sets; cross-subject WER at 92.55%. |
| Evaluation protocol | Test set WER computed across varying vocabulary sizes and cross-subject conditions with character-level CTC decoding and external 4-gram language model. |

### Limits

- **Technical:** Very small dataset; high WER; limited subject pool; lack of cross-subject robustness; no real-time validation; requires full 31-channel EEG cap; no wearable or practical signal capture setup.
- **Evaluation:** Only 30 unique English sentences from four subjects; random 80/20 train/test split; WER metrics without unseen-word or cross-environment testing; no walking tested; no cross-device evaluation.
- **Deployment:** Very high word error rate (WER), poor subject generalization (cross-subject WER 92.55%), requirement of full 31-channel EEG cap, lack of real-time results, and small dataset size.
- **Scope of this review:** Demonstration limited to 30 unique silently read sentences across four subjects, no environmental or cross-device variability.

### Evidence

- The paper demonstrates the feasibility of using EEG signals for continuous silent speech recognition while subjects silently read English sentences without vocalizing. (Abstract)
- The paper introduces a continuous sentence-level silent speech recognition approach from real EEG data using a character-level CTC automatic speech recognition model, distinct from prior small-vocabulary or passive-listening EEG silent speech studies. (1. Introduction)
- EEG was recorded from four male subjects using a 32-electrode (31 channels plus ground) wet EEG cap placed according to standard 10-20 system at 1000 Hz sampling frequency while subjects silently read 30 USC-TIMIT English sentences. (3. Design of Experiments for building the ing rate,moving window average,kurtosis and power spectral)
- The EEG features extracted per channel are root mean square, zero crossing rate, moving window average, kurtosis, and power spectral entropy, totalling 155 features over 31 channels, which are reduced to 20 dimensions using Kernel Principal Component Analysis (KPCA) with polynomial kernel of degree 3. (4. EEG feature extraction details)
- The automatic speech recognition (ASR) model is based on Connectionist Temporal Classification (CTC) with an encoder of two GRU layers (128 and 64 units) followed by a Temporal Convolutional Network (TCN) with 32 filters and a decoder with softmax output for character-level transcription. (Connectionist Temporal Classification (CTC))
- Test-time word error rates (WER) ranged approx. from 74.86% to 84.22% for vocabulary sizes from 12 to 72 sentences (30 unique), with a WER of 83.34% on the 72 sentence test set; cross-subject WER rises to 92.55%. (6. Results)
- Limitations include the small dataset (four subjects, 30 unique sentences), poor accuracy indicated by very high WER, and weak generalization across subjects evidenced by increased cross-subject WER. (6. Results)
- The approach is not presently suitable for deployment given high WER, requirement of full 31-channel EEG cap, and lack of real-time decoding results. (7. Conclusion)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
