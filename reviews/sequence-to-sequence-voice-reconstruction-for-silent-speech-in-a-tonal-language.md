# Sequence-to-Sequence Voice Reconstruction for Silent Speech in a Tonal Language

Huiyan Li, Haohong Lin, You Wang, Hengyang Wang, Ming Zhang, Han Gao, Qing Ai, Zhiyuan Luo, Guang Li  
arXiv / imported corpus page 2022 · [arXiv](https://arxiv.org/abs/2108.00190)

**Section:** [Surface EMG](../README.md#surface-emg) · **Review basis:** full_text

SSRNet reconstructs Mandarin speech from five-channel facial sEMG using duration-aware Seq2Seq and tonal multitask learning, cutting ASR CER from 46.62% to 21.99% over the baseline.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Five facial Ag/AgCl sEMG electrodes, 2000 Hz |
| Task | Speech synthesis from silent EMG |
| Vocabulary | Mandarin read sentences (2260 words / 1373 characters) |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 21.99% objective ASR CER, 6.41% human-listener CER, six speakers |

**Limitations.** Speaker-dependent with six speakers and controlled read sentences; no cross-speaker, unseen-word, real-time, or mobile evaluation.

## Full review

### In short

SSRNet innovatively applies duration-aware Seq2Seq modeling and tonal multitask learning to reconstruct intelligible Mandarin speech from facial sEMG signals, markedly improving performance over prior methods but remains speaker-dependent with limited deployment evaluation.

### Review

This work presents SSRNet, a novel duration-regulated Seq2Seq model for reconstructing audible speech from silent sEMG signals in Mandarin Chinese, a tonal language where tone preservation is essential. By extracting duration alignment via DTW and employing a learned duration predictor and length regulator, SSRNet aligns variable-length silent sEMG features with audio frame counts, enabling more accurate mel-spectrogram generation. The model also incorporates a multitask loss combining vocal sEMG reconstruction and toneme classification to enhance tonal feature fidelity. Trained and evaluated on a Mandarin silent speech corpus from six speakers, SSRNet demonstrates significantly reduced character error rates both objectively via automatic speech recognition and subjectively through human listeners, surpassing a baseline method by a wide margin. However, the approach remains speaker-dependent, with no cross-speaker or environment generalization tested, no assessment of latency or real-time capability, and limited to controlled read speech context. Overall, SSRNet advances tonal silent speech decoding by explicitly modeling timing and tonal information, providing a valuable architecture for future development though deployment challenges persist.

### Why it matters

Demonstrates effective duration-regulated Seq2Seq mapping with toneme supervision enabling practical Mandarin tonal silent speech reconstruction from sEMG, bridging the gap between neuromuscular signal decoding and natural sounding tonal speech synthesis in tonal languages.

### Prior state of the art

Prior sEMG silent speech reconstruction approaches mostly treated decoding as frame-level tasks in non-tonal languages, without explicit duration alignment or handling tonal features critical in Mandarin Chinese silent speech synthesis.

### What changed

Introduces explicit duration extraction between silent sEMG and audio via DTW and integrates a duration predictor and length regulator to time-align input features, plus toneme classification loss for tonal information preservation, enabling effective tonal speech reconstruction in Mandarin.

### Position in the field

State-of-the-art demonstration of tonal silent speech reconstruction using facial sEMG with duration-regulated Seq2Seq and tonal multitask learning, significantly improving over previous baselines but limited to controlled conditions and speakers.

### Practical value

Provides foundational design and evaluation framework for tonal silent speech reconstruction valuable for privacy-preserving speech augmentation in noisy environments; key step towards practical Mandarin SSI with room to enhance real-time capability and robustness.

### Advanced

system_design;evaluation

### Unresolved

Cross-speaker transfer, real-time latency, walking/mobile robustness

### Evaluation details

| Item | Details |
| --- | --- |
| Task | sEMG-based silent speech-to-voice reconstruction |
| Input | Five-channel facial surface electromyography (sEMG) recorded at 2000 Hz with Ag/AgCl electrodes placed near mouth and neck muscles |
| Sensor | Five facial surface Ag/AgCl electrodes positioned near nose, mouth corners, and chin with a sampling frequency of 2000 Hz; differential electrode for channel 1 and single electrodes for others |
| Body site | face |
| Output | speech-audio |
| Vocabulary type | Mandarin read sentences |
| Vocabulary size | 2260 words / 1373 characters from AISHELL-3 corpus read sentences |
| Metrics and results | Average objective ASR CER 21.99%±4.99% on six speakers; subjective CER 6.41% average (best 1.19%); accompanied by Mel-Cepstral Distortion (MCD) and Short-Term Objective Intelligibility (STOI) metrics; baseline CER was 46.62% objective and 39.76% subjective. |
| Evaluation protocol | Quantitative: ASR character error rate (CER), Mel-Cepstral Distortion (MCD), Short-Term Objective Intelligibility (STOI). Qualitative: Human listener transcription CER and naturalness ratings per speaker. |

### Limits

- **Technical:** Speaker-dependent training, limited to controlled read sentences, no cross-speaker generalization, no evaluation of real-time latency or robustness to noise or motion, few electrodes with limited articulatory coverage, limited vocabulary
- **Evaluation:** Evaluation limited to six native Mandarin speakers, fixed controlled read sentences; phoneme and tone classification limited to in-vocabulary tokens; no unseen word generalization or cross-domain tests; no mobile or real-time latency tests; subjective tests with 10 listeners.
- **Deployment:** Speaker-dependent models trained on six specific Mandarin speakers; requires five facial sEMG electrodes with fixed placement; no reported real-time inference or latency analysis; lacks cross-speaker or cross-environment robustness evaluation; no assessment in walking or mobile conditions.
- **Scope of this review:** Limited to silent speech reconstruction from facial sEMG in Mandarin Chinese with fixed electrode setup; no evaluation in other languages, body sites, or conversational scenarios.

### Evidence

- We propose SSRNet, the first Seq2Seq-based method for silent speech reconstruction in Mandarin Chinese, extracting duration alignment between silent sEMG and vocal audio, with joint toneme classification and vocal sEMG reconstruction losses, and use a state-of-the-art vocoder to generate audio waveform. (Abstract)
- Five channels of facial sEMG are recorded using wet Ag/AgCl electrodes positioned around the face and neck, sampled at 2000 Hz. Electrodes are placed 1cm from nose, mouth corners, and chin, with one channel differential. (II. DATA ACQUISITION)
- Dataset includes six native Mandarin speakers reading phonetically balanced AISHELL-3 sentences, totaling about 5.79 hours of silent speech, split 8:1:1 for training, validation, testing per speaker. (II. DATA ACQUISITION)
- SSRNet introduces a duration extractor using DTW to obtain alignment between silent sEMG and audio, duration predictor to predict length alignment, and length regulator to resample features, enabling Seq2Seq mel-spectrogram prediction with tonal-aware multitask learning. (III. THE PROPOSED METHODS)
- On six speakers, SSRNet achieves average ASR character error rate (CER) of 21.99% (SD 4.99%), outperforming baseline with CER 46.62% objectively. Subjective human transcription CER is 6.41% average (best 1.19%) across six speakers, with naturalness ratings improved. (IV. EXPERIMENTS)
- The system uses speaker-dependent training, limited to six Mandarin speakers with no cross-speaker or cross-environment generalization tested, no latency or real-time inference evaluation, and no mobile or walking scenario testing. (IV. EXPERIMENTS)
- The approach requires wearing five specific facial sEMG electrodes; no real-time operation, cross-speaker transfer, or mobile scenario tested, limiting deployment readiness currently to controlled lab environments. (II. DATA ACQUISITION)
- Output audio waveforms are generated by a pre-trained Parallel WaveGAN vocoder conditioned on predicted mel-spectrograms. (III. THE PROPOSED METHODS)
- Training loss includes mean absolute error between predicted and target mel-spectrograms, mean squared error for predicted duration against ground truth from DTW alignment, cross-entropy toneme classification loss, and a vocal sEMG reconstruction loss, jointly optimized. (III. THE PROPOSED METHODS)
- Evaluation metrics include objective ASR CER via Mandarin ASR system, Mel-Cepstral Distortion (MCD), Short-Term Objective Intelligibility (STOI), as well as subjective human listener transcriptions and naturalness ratings over reconstructed voices from six speakers. (IV. EXPERIMENTS)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
