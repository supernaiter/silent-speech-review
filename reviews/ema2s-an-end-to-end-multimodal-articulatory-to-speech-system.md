# EMA2S: An End-to-End Multimodal Articulatory-to-Speech System

Yu-Wen Chen, Kuo-Hsuan Hung, Shang-Yi Chuang, Jonathan Sherman, Wen-Chin Huang, Xugang Lu, Yu Tsao  
arXiv / imported corpus page 2021 · [arXiv](https://arxiv.org/abs/2102.03786)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text

End-to-end EMA-to-speech synthesis with multimodal joint loss and a neural vocoder, consistently improving objective and subjective quality over prior EMA-to-speech baselines.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | EMA with nine sensors (lips, jaw, tongue) |
| Task | Speech synthesis from EMA |
| Vocabulary | Not applicable |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Not reported |

**Limitations.** Small dataset (three speakers, 354 utterances each), small listening test, no cross-speaker testing, and intrusive lab-grade EMA hardware.

## Full review

### In short

EMA2S achieves consistent quality improvements over prior EMA-to-speech baselines by combining multimodal joint loss training with a neural vocoder, though gains remain confined to lab EMA conditions.

### Review

EMA2S integrates a spectral encoder, EMA encoder, and a shared decoder, training jointly to minimize losses on spectrogram, mel-spectrogram, and a deep feature loss measuring embedding similarity between articulatory and acoustic modalities. The use of a neural vocoder (Parallel WaveGAN) marks a departure from traditional parametric vocoders and yields demonstrable benefit. Evaluated on the NTT EMA corpus with three speakers, EMA2S outperforms a strong BLSTM-based baseline on MCD (7.815 to 7.176), PESQ (1.279 to 1.350), STOI (0.696 to 0.716), and CCR (0.818 to 0.868). In an A/B listening test with 10 participants, EMA2S was preferred 83% of the time. A reduced four-EMA-sensor variant also improves over baseline, indicating potential for reduced sensor setups. Despite these gains, the hardware remains intrusive laboratory EMA, limiting deployment practicalities, and the dataset size and speaker count constrain generalizability. The study contributes a rigorous multimodal joint-loss EMA-to-waveform synthesis pipeline with verified gains over prior methods but does not close the gap to wearable silent speech interfaces.

### Why it matters

Provides a more natural and intelligible articulatory-to-speech synthesis baseline by effectively leveraging a neural vocoder and multimodal joint loss, improving reconstruction quality beyond prior parametric vocoder pipelines.

### Prior state of the art

EMA-to-speech systems typically relied on parametric vocoders with a single acoustic loss, limiting naturalness and intelligibility.

### What changed

Replaces traditional parametric vocoders with an end-to-end neural vocoder architecture (Parallel WaveGAN) and incorporates a combined loss over spectrogram, mel-spectrogram, and deep features for improved articulatory-to-speech mapping.

### Position in the field

EMA-based articulatory-to-speech synthesis with the integration of modern neural vocoding and multimodal loss training, showing incremental but well-documented gains.

### Practical value

Serves as a significant improved lab baseline for EMA articulatory-to-speech synthesis; useful for research on data-efficient, multimodal articulatory representations but limited for immediate practical use due to hardware requirements.

### Advanced

System design; reconstruction quality improved via neural vocoder and joint multimodal loss training.

### Unresolved

Hardware practicality; cross-speaker robustness; naturalness ceiling remain unresolved.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | magnetic (EMA) |
| Sensor | Electromagnetic midsagittal articulography (EMA) with nine sensors including lips, jaw, and multiple tongue positions. |
| Body site | jaw; lip; tongue |
| Output | speech-audio |
| Metrics and results | Mel-cepstral distortion, PESQ, short-time objective intelligibility, character correct rate by ASR, and subjective A/B listening preference percentages. |
| Evaluation protocol | Objective evaluation metrics (mel-cepstral distortion, PESQ, STOI, character correct rate with pre-trained ASR) combined with subjective A/B listening preference test and ablation with fewer sensors. |

### Limits

- **Technical:** Small dataset size (three speakers, 354 utterances each), dependence on intrusive EMA sensors, and lack of large-scale or diverse speaker evaluation.
- **Evaluation:** Evaluations are confined to a small dataset with only three speakers; the subjective A/B listening test involved only 10 participants with 15 questions total, and no cross-speaker generalization testing was reported.
- **Deployment:** The system requires laboratory-grade EMA hardware, which is intrusive and limits portability. Even the reduced four-sensor configuration still depends on EMA instrumentation and controlled environment recording conditions.
- **Scope of this review:** Focused on laboratory EMA articulatory-to-speech synthesis with neural vocoder reconstruction; not addressing wearable or silent speech device deployment.

### Evidence

- We present EMA2S, an end-to-end multimodal articulatory-to-speech system that directly converts articulatory movements to speech signals using a neural-network-based vocoder combined with multimodal joint-training of spectrogram, mel-spectrogram, and deep features. (Abstract)
- EMA2S uses a combined multimodal loss consisting of spectrogram loss, mel-spectrogram loss, and deep feature loss, leveraging the idea of multimodal learning by calculating dissimilarity between articulatory and spectral embeddings during training. (III. PROPOSED METHOD)
- The system replaces traditional parametric vocoders with a Parallel WaveGAN-based neural vocoder, allowing an end-to-end trainable articulatory-to-speech waveform synthesis pipeline. (III. PROPOSED METHOD)
- Objective evaluation metrics used include mel-cepstral distortion (MCD), perceptual evaluation of speech quality (PESQ), short-time objective intelligibility (STOI), and character correct rate (CCR) from a pre-trained automatic speech recognition (ASR) system. (IV. EXPERIMENTS)
- Experiments performed on the NTT EMA corpus with three speakers, each contributing 354 utterances, split into 304 training and 50 testing utterances per speaker, with sensors placed on upper lip, lower lip, upper jaw, lower jaw, tongue tip, tongue blade, tongue dorsum, tongue rear, and velum. (IV. EXPERIMENTS)
- The EMA2S system achieves superior objective scores compared to the baseline: MCD 7.176 vs 7.815, PESQ 1.350 vs 1.279, STOI 0.716 vs 0.696, and CCR 0.868 vs 0.818, as shown in Table I of the paper. (IV. EXPERIMENTS)
- The subjective A/B listening test with 10 participants and 15 questions in total shows that EMA2S speech output was preferred 83% over the baseline's 17%. (IV. EXPERIMENTS)
- The dataset is limited to three speakers and 354 utterances each, recorded in laboratory conditions with EMA sensors, which are intrusive and impractical for general deployment. (IV. EXPERIMENTS)
- Even with only four less invasive EMA sensors, the system still outperforms the baseline, but still depends on EMA hardware and controlled conditions, limiting portability and real-world deployment. (IV. EXPERIMENTS)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
