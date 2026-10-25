# Improved Processing of Ultrasound Tongue Videos by Combining ConvLSTM and 3D Convolutional Networks

Amin Honarmandi Shandiz, László Tóth  
arXiv / imported corpus page 2022 · [arXiv](https://arxiv.org/abs/2206.12947)

**Section:** [Ultrasound & tongue imaging](../README.md#ultrasound--tongue-imaging) · **Review basis:** full_text

Combines 3D CNNs and ConvLSTM to regress mel-spectrograms from ultrasound tongue video, modestly outperforming prior architectures in accuracy and efficiency on single-speaker Hungarian data.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Micro ultrasound tongue probe with headset, plus microphone |
| Task | Speech synthesis from tongue ultrasound |
| Vocabulary | Not stated |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | MSE ~0.276, mean R2 ~0.73 on mel-spectrogram regression |

**Limitations.** Single-speaker dataset with no perceptual intelligibility testing, cross-speaker evaluation, or real-time tests.

## Full review

### In short

An empirically supported, incremental advancement showing that hybrid 3D-CNN plus ConvLSTM models modestly outperform prior ultrasound tongue video SSI architectures in mel-spectrogram regression accuracy and model efficiency on single-speaker data.

### Review

This work contributes a systematic experimental study on neural network architectures for direct articulatory-to-acoustic regression in ultrasound tongue image-based silent speech interfaces. By leveraging a hybrid model that combines early 3D convolutional layers and a top ConvLSTM layer, the authors demonstrate improved mel-spectrogram reconstruction accuracy, model compactness, and faster training compared to earlier 3D-CNN and 3D-CNN+BiLSTM baselines. The dataset consists of a publicly available Hungarian single-speaker corpus, with synchronized ultrasound video at 82 fps and audio at 11 kHz. While the scope is limited to objective spectrogram error metrics without perceptual or cross-speaker validation, the work clarifies the advantages of fusing spatial and temporal information through ConvLSTM in this SSI application. Deployment challenges remain due to hardware and training data constraints, and generalizability is not addressed. Nonetheless, the paper provides valuable architectural insights and empirical validation for ultrasound SSI modeling choices, serving as a practical reference for future ultrasound-based silent speech reconstruction research.

### Why it matters

This study delivers concrete evidence that integrating ConvLSTM layers atop 3D-CNN feature extractors enhances articulatory-to-speech spectral regression accuracy and reduces network complexity, offering a technically sound and resource-efficient SSI architecture alternative to classical CNN plus sequential LSTM models in ultrasound tongue video speech reconstruction.

### Prior state of the art

Baseline ultrasound tongue SSI models typically combined 2D-CNN with LSTM layers or employed 3D-CNNs, with limited prior use of ConvLSTM architectures, which integrate convolution and temporal gating in one layer and thus preserve spatiotemporal structure more directly but were not widely applied in this domain before.

### What changed

Replacing the uppermost dense or BiLSTM temporal integration layers of a 3D-CNN architecture with a ConvLSTM layer reduces the model depth and size and improves mel-spectrogram regression accuracy, producing a more compact and accurate network for SSI ultrasound speech reconstruction.

### Position in the field

Focused on comparing temporal feature integration architectures within ultrasound tongue video SSI direct speech reconstruction pipelines

### Practical value

Provides architecture design insights for researchers seeking tradeoffs between accuracy, network size, and training speed in ultrasound tongue SSI systems

### Advanced

system_design; evaluation

### Unresolved

cross-speaker generalization; intelligibility evaluation; real-world deployment robustness

### Evaluation details

| Item | Details |
| --- | --- |
| Task | Speech reconstruction from ultrasound tongue video sequences |
| Input | Ultrasound tongue video sequences (82 fps) synchronized with audio (11,025 Hz) |
| Sensor | Ultrasound tongue imaging probe (Micro system by Articulate Instruments) with stabilizing headset; Audio-Technica ATR 3350 microphone |
| Body site | tongue |
| Output | Speech audio spectra reconstructed via mel-spectrogram regression followed by WaveGlow vocoder synthesis |
| Metrics and results | Mean squared error (MSE) on mel-spectrogram regression around 0.276; mean R2 regression score approximately 0.73; improvements are incremental but consistent compared to baselines |
| Evaluation protocol | Objective regression using mean squared error (MSE) and R2 scores on train, development, and test splits for mel-spectrogram frame prediction from ultrasound tongue video input sequences. |

### Limits

- **Technical:** Limited dataset from one speaker; absence of perceptual acoustic evaluations; ConvLSTM layers have more parameters requiring filter size adjustments; computations performed offline without real-time deployment tests
- **Evaluation:** Evaluation is limited to a single-speaker Hungarian dataset; the metrics are mean squared error and R2 score on mel-spectrogram regression, without perceptual intelligibility testing or cross-speaker/word generalization analysis.
- **Deployment:** The approach requires access to specialized ultrasound tongue imaging hardware and synchronized audio for training. It was trained on single-speaker data only, limiting generalizability. Real-time deployment performance and robustness to varied environmental factors remain untested.
- **Scope of this review:** Single-speaker articulatory-to-acoustic regression using synchronized ultrasound tongue videos and audio mel-spectrograms; no perceptual, cross-speaker, or robustness evaluations included

### Evidence

- The authors claim that a hybrid model combining 3D-CNN and ConvLSTM layers performs better for direct ultrasound tongue video to speech mel-spectrogram mapping accuracy, while being faster and smaller than previous 3D-CNN baselines. (Abstract)
- Replacing the uppermost 3D-CNN and BiLSTM layers with a ConvLSTM layer reduces model depth and size and improves mel-spectrogram regression accuracy, creating an efficient hybrid architecture for ultrasound tongue video SSI reconstruction. (4 Experimental Setup)
- The best hybrid 3D-CNN + ConvLSTM model achieved mean squared error around 0.276 and mean R2 score about 0.73 on the test set for mel-spectrogram regression, outperforming 3D-CNN alone and 3D-CNN + BiLSTM baselines. (5 Results)
- Evaluations were performed only on a single female Hungarian speaker dataset of 438 sentences split into 310 training, 41 development, and 87 test samples; no cross-speaker, cross-language, or perceptual intelligibility testing was conducted. (3 Data acquisition)
- The approach is limited by requiring specialized ultrasound hardware, single-speaker training data, lack of perceptual or multi-speaker evaluation, and untested real-time deployment in varied conditions. (3 Data acquisition)
- Although not experimentally proven, reducing the network depth via ConvLSTM increases training and inference speed, suggesting potential for faster, more compact models suitable for real-time usage after further validation. (5 Results)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
