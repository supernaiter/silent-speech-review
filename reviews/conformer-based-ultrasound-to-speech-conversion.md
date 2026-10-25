# Conformer-based Ultrasound-to-Speech Conversion

Ibrahim Ibrahimov, Zainkó Csaba, Gábor Gosztolya  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2506.03831)

**Section:** [Ultrasound & tongue imaging](../README.md#ultrasound--tongue-imaging) · **Review basis:** full_text+summary

Compares Conformer-based models to a CNN for ultrasound tongue-to-speech conversion on four speakers; Conformer plus bi-LSTM gives a modest naturalness gain without improving objective spectral metrics.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Ultrasound tongue imaging (Micro system, 81.5 fps) |
| Task | Speech synthesis from ultrasound |
| Vocabulary | Read sentences; size not stated |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | MUSHRA naturalness 32 vs 28 (CNN), p=0.037, held-out sentences |

**Limitations.** Four speakers with ten test sentences each, low absolute naturalness, no intelligibility test, and no real-time or truly silent operation.

## Full review

### In short

A four-speaker ultrasound-to-speech comparison finds a modest naturalness gain from Conformer plus bi-LSTM, without objective-fidelity gains; reduced training time is not proof of real-time or truly silent operation.

### Review

This is a useful but narrowly scoped ultrasound-to-speech architecture comparison. Four TaL80 speakers receive separate models that map tongue ultrasound frames to 80-dimensional mel features, then synthesize audio with a pretrained HiFi-GAN vocoder. The strongest positive result is perceptual: 27 listeners rated 20 selected utterances, and Figure 3 reports rounded mean naturalness of 32/100 for Conformer with bi-LSTM versus 28 for both the CNN and Conformer Base, with natural speech at 96. The bi-LSTM versus CNN comparison is reported significant at p=0.037. This is not an intelligibility score or evidence of near-natural speech. Neither proposed model significantly improves the objective measures: Base worsens MSE for one speaker and MCD for three; bi-LSTM worsens MCD for one. Training takes about 30% and 80% of baseline time for Base and bi-LSTM respectively, but inference speed is not measured. The conclusion's claim that both models use fewer parameters is contradicted by the reported 2.66M, 5.35M and 4.09M counts for Base, bi-LSTM and CNN. The source treats ultrasound beam lines within a frame as sequence steps, so its architecture should not be described as proven long-range temporal speech modeling. The value for SSI is an alternative acoustic-feature predictor and a warning against selecting models by spectral error alone. Truly silent articulation, unseen-user transfer, intelligibility and practical online communication remain unvalidated; the suggested explanation involving silent intervals is a hypothesis rather than an established cause.

### Why it matters

A source-grounded comparison showing that a model preferred by listeners can have no better, and sometimes worse, spectral metrics. Its practical research value is in acoustic-feature model selection, not demonstrated deployable silent communication.

### Prior state of the art

The paper builds on established ultrasound-to-acoustic mapping using fully connected, convolutional and recurrent networks. Its direct comparator is the open 2D-CNN ultrasound-to-mel implementation of Csapo et al.; SottoVoce is related prior work, not an experimentally matched comparator here.

### What changed

Replaces the acoustic-feature predictor with a frame-level Conformer or Conformer plus two bi-LSTM layers while retaining an ultrasound-to-80-dimensional-mel-to-vocoder pipeline. It exposes a mismatch between perceptual naturalness and objective spectral measures.

### Position in the field

An incremental acoustic-feature modeling study within ultrasound-based SSI, complementary to end-to-end interaction work such as SottoVoce rather than a replacement demonstrated under the same task conditions.

### Practical value

Offers two candidate predictors with different training-cost, model-size and perceptual tradeoffs. The reported low absolute naturalness and unmeasured intelligibility limit claims about usable speech communication.

### Advanced

Perceived naturalness for Conformer with bi-LSTM; reported training-time reduction for both variants; parameter reduction for Conformer Base only.

### Unresolved

Speech intelligibility, truly silent articulation, unseen speakers and words, repeated-session robustness, inference latency, energy consumption, and clinical communication.

### Narrowed or regressed

Conformer Base has significantly worse MSE for speaker 03mn and worse MCD for 01fi, 03mn and 04me. The bi-LSTM variant has worse MCD for 04me and more parameters than the CNN baseline.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | ultrasound tongue imaging; paired audio supplies acoustic supervision and evaluation references, not a reported inference input |
| Sensor | Articulate Instruments Micro ultrasound system, 81.5 fps; scanline frames resized by bicubic interpolation from 64x842 to 64x128 and normalized to [-1,1]. Training server includes an NVIDIA TITAN Xp with 12 GB VRAM and 32 GB host RAM. |
| Body site | tongue |
| Output | speech-audio synthesized from predicted 80-dimensional mel spectrograms |
| Vocabulary type | Continuous speech-audio reconstruction from read-sentence recordings, not a word-classification benchmark; open-vocabulary generalization is not established. |
| Vocabulary size | Unknown; no lexicon size is reported. Ten test sentences per speaker are not ten word classes. |
| Metrics and results | Figure 3 rounded average naturalness: natural 96, lower anchor 4, CNN 28, Base 28, bi-LSTM 32 (0-100 scale). Reported p-values: bi-LSTM vs CNN 0.037, Base vs CNN 0.698, bi-LSTM vs Base 0.015. Table 1 MSE for speakers 01fi/02fe/03mn/04me: CNN 0.464/0.623/0.395/0.484; Base 0.511/0.618/0.462/0.524; bi-LSTM 0.482/0.581/0.378/0.449. Base's 03mn worsening has p=0.026; no bi-LSTM MSE difference is significant. Table 2 MCD in dB: CNN 3.221/3.009/3.641/3.172; Base 3.517/3.121/4.133/3.465; bi-LSTM 3.253/3.037/3.704/3.258. Base worsens significantly for 01fi/03mn/04me (each p=0.001); bi-LSTM worsens for 04me (p=0.002). Parameters CNN/Base/bi-LSTM: 4.09M/2.66M/5.35M; proposed-model training times approximately 30%/80% of CNN per speaker, not inference times. |
| Evaluation protocol | Speaker-dependent held-out-sentence regression and speech synthesis: sentence-level MSE and MCD, plus a MUSHRA-style 0-100 naturalness listening test with natural references and a noise-added lower anchor. |

### Limits

- **Technical:** Frame-level modeling treats the 64 ultrasound beam lines as sequence positions; this is not evidence of long-range inter-frame temporal learning. Spectral errors and listening judgments diverge. The Figure 4 silent-interval explanation is based on one selected utterance and remains hypothetical. Bi-LSTM is larger than the CNN despite the conclusion's contrary generalization.
- **Evaluation:** Four speakers with ten test utterances each; listening uses five randomly selected utterances per speaker and 27 non-native English listeners. No repeated-training uncertainty, intelligibility transcription, formal equivalence test or held-out-speaker experiment is reported. Subjective-test statistical handling and multiplicity correction are insufficiently specified for independent validation from the paper alone.
- **Deployment:** Offline speaker-specific corpus experiments using ultrasound equipment and a TITAN Xp server. No end-to-end online interaction, mobile inference, energy measurement, walking test or patient evaluation is reported.
- **Scope of this review:** Four known speakers, paired corpus recordings and held-out read sentences. No separately documented truly silent test condition, patient cohort, unseen-user evaluation, unknown-word analysis, spontaneous dialogue or environmental robustness experiment.

### Evidence

- The authors propose Base and bi-LSTM Conformer predictors for ultrasound-to-mel mapping and claim perceptual and training-time advantages over a 2D-CNN baseline, rather than a new sensor. (p.1 Abstract and Introduction; p.2 Figure 1; pp.2-3 Sections 3.2-3.5)
- The dataset comprises four selected TaL80 speakers, two female and two male, with 204/141/193/190 recordings. Ten shared read sentences per speaker are test data; the remaining recordings are split 9:1 for train/development. Models are speaker-specific. (p.2 Section 2 Dataset and Section 3.2 Baseline; p.3 Section 4.1)
- Micro ultrasound scanlines at 81.5 fps are synchronized with audio, resized from 64x842 to 64x128 and normalized to [-1,1]. The synthesis path predicts 80 mel dimensions and uses pretrained HiFi-GAN VCTK_V1. (p.2 Section 2 and Figure 1; p.3 Section 3.5)
- The Base network uses linear layers around a Conformer block, with the bi-LSTM variant adding two recurrent layers. Section 3.3 explicitly treats beam lines as sequence steps while retaining frame-level learning, so long-range temporal speech learning is not established by this description. (p.2 Figure 2 and Section 3.3; p.3 Sections 3.3-3.4)
- Training is limited to 20 epochs, batch size 128 and development-MSE early stopping with patience 3. Base uses encoder dimension 256, 32 heads, kernel 31 and feedforward expansion 3, with AdamW and cosine-decay restarts. (p.2 Section 3.1; p.3 Section 3.3)
- Sections 3.2-3.4 report CNN/Base/bi-LSTM parameter counts of 4.09M/2.66M/5.35M and Base/bi-LSTM training times of approximately 30%/80% of baseline per speaker. These are training-time comparisons, not inference measurements. (p.2 Section 3.2; p.3 Sections 3.3-3.4)
- Table 1 lists MSE for 01fi/02fe/03mn/04me: CNN 0.464/0.623/0.395/0.484; Base 0.511/0.618/0.462/0.524; bi-LSTM 0.482/0.581/0.378/0.449. Base is significantly worse for 03mn (p=0.026); none of the proposed-model MSE improvements is significant. (p.3 Table 1 and Section 4.2)
- Table 2 MCD in dB for 01fi/02fe/03mn/04me is CNN 3.221/3.009/3.641/3.172; Base 3.517/3.121/4.133/3.465; bi-LSTM 3.253/3.037/3.704/3.258. Lower is better. Base significantly worsens three speakers (each p=0.001); bi-LSTM significantly worsens 04me (p=0.002). (p.3 Table 2 and Section 4.3)
- The naturalness test uses five randomly selected utterances per speaker, 20 total, rated by 27 non-native English listeners (14 female, 13 male, ages 20-55). Order is randomized and the scale is 0-100; the lower anchor is original speech with white noise at a stated 0.0005 level. (p.4 Section 4.4)
- Visually checked Figure 3 labels rounded average naturalness as natural 96, anchor 4, CNN 28, Base 28 and bi-LSTM 32. The 03mn panel instead gives CNN 33, Base 31 and bi-LSTM 32, so the bi-LSTM advantage is not universal across speakers. Error bars are described as 95% confidence intervals. (p.4 Figure 3 and caption)
- The reported pooled listening comparisons give p=0.037 for bi-LSTM versus CNN, p=0.698 for Base versus CNN and p=0.015 for bi-LSTM versus Base. These are naturalness comparisons, not word-recognition or intelligibility results. (p.4 Section 4.4)
- Section 5 says both proposed models have fewer parameters, contradicting the 5.35M bi-LSTM versus 4.09M CNN counts in Sections 3.2 and 3.4. Only Base's 2.66M count supports a reduction; do not propagate the conclusion's generalization. (p.4 Section 5, second paragraph; p.2 Section 3.2; p.3 Sections 3.3-3.4)
- Figure 4 compares one 01fi test utterance (014_xaud). The authors suggest inaccurate silent intervals may explain disagreement between objective and subjective results, but explicitly leave this for future analysis. The figure is not a controlled causal test. (p.4 Figure 4, caption and Section 5)
- The paper evaluates synchronized ultrasound/audio corpus recordings and held-out read sentences, without a separately described truly silent articulation test, unseen-speaker experiment, lexical-overlap analysis or intelligibility transcription. Held-out sentences alone do not establish those capabilities. (p.2 Section 2; p.3 Sections 4.1-4.3; p.4 Section 4.4)
- Section 5 suggests potential for real-time use based on computational advantages, but the reported measurements concern training duration. No inference latency, mobile energy, walking test or online communication outcome is presented. (p.2 Section 3.1; p.3 Sections 3.3-3.4; p.4 Section 5)
- A nonsignificant p-value for Base versus CNN is not a formal equivalence test. The small four-speaker/20-listening-utterance evaluation and lack of reported repeated-training uncertainty constrain generalization; subjective comparison units and multiple-comparison correction require clarification. (p.3 Section 4.2; p.4 Section 4.4)
- The authors point to https://doi.org/10.5281/zenodo.15544868 for full code and synthesized samples. This review records the source's availability statement, not an independent audit of artifact completeness or successful reproduction. (p.4 Section 5, final paragraph)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
