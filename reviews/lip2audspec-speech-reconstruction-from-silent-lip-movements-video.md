# Lip2AudSpec: Speech reconstruction from silent lip movements video

Hassan Akbari, Himani Arora, Liangliang Cao, Nima Mesgarani  
arXiv 2017 · [arXiv](https://arxiv.org/abs/1710.09798)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

A structured review of *Lip2AudSpec: Speech reconstruction from silent lip movements video* (Hassan Akbari et al., arXiv 2017) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Lip2AudSpec reconstructs speech from silent lip video using an auditory-spectrogram autoencoder bottleneck as target, improving objective intelligibility metrics and human word accuracy (55.8% vs 50.9%) over a baseline on four GRID speakers.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera (silent lip video) |
| Task | Speech synthesis from silent lip video |
| Vocabulary | 51 words (GRID closed vocabulary) |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Human word accuracy 55.8% vs 50.9% baseline; STMI 0.80 vs 0.52, four GRID speakers |

**Limitations.** Only four GRID speakers and closed vocabulary; lip-only input misses tongue and throat cues; no real-world recordings.

## Full review

### In short

The paper's auditory spectrogram autoencoder bottleneck target is a key innovation that produces more intelligible, natural reconstructed speech from lip videos than prior methods, as confirmed by objective and human evaluations.

### Review

This paper meaningfully advances lip-to-speech reconstruction by combining a robust auditory spectrogram audio representation compressed by a noise-robust deep autoencoder with a video-driven CNN-LSTM model predicting bottleneck features to reconstruct natural-sounding speech. Experiments on the GRID dataset with 4 speakers show significant gains over the prior Vid2Speech baseline: average spectral-temporal modulation index (STMI) improved from 0.52 to 0.80, PESQ from 1.76 to 1.88, and Corr2D from 0.61 to 0.88, evidencing more accurate acoustic reconstructions. Additionally, a Mechanical Turk human transcription evaluation found a 5% absolute word accuracy improvement (51% to 56%) and a striking correct speaker gender classification increase (43% to 85%), demonstrating better preservation of pitch and speaker traits. Nonetheless, the approach remains limited to a small closed vocabulary and speaker pool. The method depends solely on lip video, thus missing articulatory cues from tongue or throat that particularly affect vowel and high-frequency speech reconstruction. Despite these limitations, the paper sets a valuable benchmark focusing on the importance of speech representation and an audio-visual pipeline design for better intelligibility in lip-based speech reconstruction.

### Why it matters

Demonstrates that leveraging a deep compressed auditory spectrogram representation as a reconstruction target materially improves intelligibility and pitch preservation in lip-to-speech systems over prior spectrogram or LPC-based methods on a well-known benchmark.

### Prior state of the art

Prior lip-to-speech systems like Vid2Speech reconstructed speech but suffered weak pitch and quality due to target representations missing excitation parameters.

### What changed

Shifts from using classical LPC or spectrogram targets to auditory spectrogram compressed by a deep autoencoder for better speaker and pitch preservation; evaluates with human transcription and objective metrics.

### Position in the field

Strong lip-to-speech reconstruction baseline focused on improved acoustic targets rather than solely on visual feature encoders.

### Practical value

Useful as a reference lip-to-speech system that highlights the impact of appropriate speech representation on intelligibility and speaker characteristics preservation.

### Advanced

system_design; evaluation

### Unresolved

open-vocabulary reconstruction, speaker independence beyond GRID, richer articulation features beyond lips

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | silent lip video |
| Sensor | camera |
| Body site | lip |
| Output | speech-audio |
| Vocabulary type | closed vocabulary |
| Vocabulary size | 51 words |
| Metrics and results | Average over four speakers: STMI 0.80 vs 0.52 baseline, PESQ 1.88 vs 1.76 baseline, Corr2D 0.88 vs 0.61 baseline; human word accuracy 55.8% vs 50.9%, correct gender 85.1% vs 43.2%. |
| Evaluation protocol | Quantitative objective metrics (Corr2D, PESQ, STMI) plus human transcription and quality/naturalness/female/male recognition surveys on Mechanical Turk. |

### Limits

- **Technical:** Lip-only video input misses tongue and throat information affecting some vowels and high-frequency speech; only evaluated on limited closed vocabulary and speaker set.
- **Evaluation:** Evaluations are on the 4-speaker GRID corpus only; human intelligibility measured via Mechanical Turk limited to vocabulary and speakers in dataset.
- **Deployment:** Trained and evaluated strictly on 4 GRID speakers with controlled vocabulary; lacks real-world recordings and speaker variability; lip-only input misses tongue/throat cues affecting vowel/high-frequency fidelity.
- **Scope of this review:** Closed vocabulary lip-to-speech reconstruction on GRID corpus videos of 4 speakers only.

### Evidence

- Introduces a deep neural network that reconstructs intelligible speech from silent lip movement videos using auditory spectrogram targets and compares it to Vid2Speech. (Abstract)
- The model first compresses auditory spectrograms through an autoencoder and then predicts those bottleneck features from silent lip video using CNN, LSTM, and fully connected layers. (3.2 Network I)
- Average STMI improved from 0.52 to 0.80, PESQ improved from 1.76 to 1.88, Corr2D improved from 0.61 to 0.88 compared to Vid2Speech across four GRID corpus speakers. (4.3.3 Lip)
- Human evaluation showed average word accuracy improved from 50.9% to 55.8%, and correct gender recognition improved from 43.2% to 85.1% over Vid2Speech. (4.3.4 Human evaluations)
- Lip-only video input misses tongue and throat information, making it difficult to reconstruct high frequency details and different vowels accurately; limited to 4 speakers and closed vocabulary in GRID corpus. (1 Introduction)
- The network is trained and tested on a small closed-vocabulary dataset of 4 GRID corpus speakers; lacking real-world generalization and speaker variability for direct practical deployment. (4.1 Dataset)

## More reviews in Lip & face video

- [Improved Speech Reconstruction from Silent Video](improved-speech-reconstruction-from-silent-video.md) (2017). Reconstructs speech from silent full-face video plus optical flow with a CNN and temporal post-processing network, outperforming prior methods on GRID and TCD-TIMIT in objective metrics and human word accuracy.
- [Lip Reading Sentences in the Wild](lip-reading-sentences-in-the-wild.md) (2017). Introduces Watch, Listen, Attend and Spell and the BBC LRS dataset; lips-only decoding reaches 50.2% WER on open-vocabulary broadcast sentences, beating a professional lipreader (73.8%).
- [Seeing Through Noise: Visually Driven Speaker Separation and Enhancement](seeing-through-noise-visually-driven-speaker-separation-and-enhancement.md) (2017). Uses visual speech predictions from face video to build masks that separate or enhance a target speaker from audio mixtures, beating audio-only separation on GRID and TCD-TIMIT. Not an SSI paper.
- [Vid2speech: Speech Reconstruction from Silent Video](vid2speech-speech-reconstruction-from-silent-video.md) (2017). Vid2speech reconstructs intelligible speech from silent face video on GRID with speaker-specific models and LPC-style resynthesis, reaching about 80% human intelligibility and partial out-of-vocabulary recovery.
- [Harnessing AI for Speech Reconstruction using Multi-view Silent Video Feed](harnessing-ai-for-speech-reconstruction-using-multi-view-silent-video-feed.md) (2018). Reconstructs speech audio from multi-view silent video on OuluVS2 with CNN-LSTM models, showing multi-view input improves PESQ over single view and that camera placement matters.
- [Visual-Only Recognition of Normal, Whispered and Silent Speech](visual-only-recognition-of-normal-whispered-and-silent-speech.md) (2018). Compares visual-only recognition of normal, whispered and silent speech, showing silent speech is a distinct regime: matched-condition silent accuracy is 62.2% (digits) and training on normal speech lowers it further.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
