# Seeing Through Noise: Visually Driven Speaker Separation and Enhancement

Aviv Gabbay, Ariel Ephrat, Tavi Halperin, Shmuel Peleg  
arXiv 2017 · [arXiv](https://arxiv.org/abs/1708.06767)

**Section:** [Lip & face video](../../README.md#lip--face-video) · **Review basis:** full_text

A structured review of *Seeing Through Noise: Visually Driven Speaker Separation and Enhancement* (Aviv Gabbay et al., arXiv 2017) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Uses visual speech predictions from face video to build masks that separate or enhance a target speaker from audio mixtures, beating audio-only separation on GRID and TCD-TIMIT. Not an SSI paper.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera plus microphone (face video and audio) |
| Task | Audiovisual speech separation and enhancement |
| Vocabulary | Not applicable |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | GRID separation SDR 5.62, PESQ 2.6 vs audio-only 1.74, 1.85 |

**Limitations.** Not SSI; speaker-dependent models, unknown speakers need fine-tuning, and evaluation uses synthetic two-speaker mixtures.

## Full review

### In short

Strong audiovisual speech separation and enhancement leveraging face video for speaker-dependent masking; not a silent speech interface paper.

### Review

This paper presents a visually driven speech separation and enhancement system that uses speaker-dependent video-to-speech network predictions as spectrogram priors to build masking filters over mixed audio input. Experiments on synthetic two-speaker mixtures from GRID and TCD-TIMIT show the approach significantly outperforms audio-only baselines and raw video-to-speech outputs, with ratio masking achieving GRID SDR 5.62 and PESQ 2.6 (vs. audio-only 1.74/1.85), and TCD-TIMIT SDR 8.68 and PESQ 2.71 (vs. audio-only 2.91/2.16). Enhancement experiments similarly surpass raw predictions. An unknown-speaker transfer experiment on GRID demonstrates reduced but viable performance after limited fine-tuning (SDR 3.06, PESQ 2.42). The approach leverages visual information to overcome challenges in audio-only same-gender speaker separation but still requires known faces and training per speaker, limiting direct application in silent speech interfaces. Although effective for audiovisual separation and enhancement in controlled datasets, the method has medium-high deployment readiness gaps due to reliance on speaker-dependent models, lack of comprehensive real-world noisy testing, and limited zero-shot generalization.

### Why it matters

Demonstrates that visual speech predictions can effectively guide mask construction for separating or enhancing a known target speaker from noisy audio mixtures, notably improving on audio-only separation especially for same-gender mixtures.

### Prior state of the art

Audio-only speech separation methods struggled especially on same-gender mixtures, and prior video-to-speech methods generated speech directly without using them as separation priors.

### What changed

Reframes vid2speech predictions as an intermediate prior for constructing masks for speech separation and enhancement, rather than as final speech output.

### Position in the field

Strong 2017 audiovisual speech separation paper that effectively uses visual priors for masking, adjacent to but distinct from silent speech interface research.

### Practical value

Useful in scenarios requiring isolation of a visible speaker's voice from mixtures or background noise using audiovisual data.

### Advanced

system_design; evaluation

### Unresolved

real-world multi-speaker video; zero-shot unknown speakers; end-to-end training

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-enhancement |
| Input | audio plus face video |
| Sensor | camera + microphone |
| Body site | face |
| Output | speech-audio |
| Metrics and results | Table 1 reports GRID ratio-mask separation SDR 5.62 and PESQ 2.6 vs. audio-only 1.74 and 1.85; TCD-TIMIT ratio-mask SDR 8.68 and PESQ 2.71 vs. audio-only 2.91 and 2.16. Table 3 shows unknown-speaker GRID fine-tuned separation SDR 3.06 and PESQ 2.42. |
| Evaluation protocol | Speech separation and enhancement evaluated with SDR, SIR, SAR, PESQ metrics, plus unknown-speaker transfer test. |

### Limits

- **Technical:** Limited to speaker-dependent models; unknown-speaker separation requires fine-tuning with audiovisual samples; evaluated mostly on synthetic mixtures; real-world noisy environment performance not fully benchmarked.
- **Evaluation:** Evaluations use synthetic benchmark mixtures (GRID and TCD-TIMIT) with known speakers; unknown speaker separation evaluated with 5-min fine-tuning; no large-scale real-world noisy environment benchmarks.
- **Deployment:** Requires visible speaker face video and speaker-dependent model training; unknown speaker separation requires fine-tuning with audiovisual data.
- **Scope of this review:** Audiovisual speaker separation and enhancement tested on synthetic GRID and TCD-TIMIT two-speaker mixtures and limited unknown speaker transfer on GRID.

### Evidence

- Uses face video to separate or enhance a target speaker from noisy mixtures by applying video-to-speech neural network predictions as filters on the mixed audio. Compares results to audio-only baselines and raw vid2speech predictions. (ABSTRACT)
- The system predicts mel-scale speech spectrograms from the speaker's face video using a vid2speech neural network and uses these spectrograms as control signals to construct time-frequency masks (binary or ratio) to separate or enhance the target speaker from the audio mixture. (2. VISUALLY)
- Table 1 reports GRID ratio-mask separation SDR 5.62 and PESQ 2.6 vs. audio-only 1.74 and 1.85; TCD-TIMIT ratio-mask SDR 8.68 and PESQ 2.71 vs. audio-only 2.91 and 2.16. Table 3 shows unknown-speaker GRID fine-tuned separation SDR 3.06 and PESQ 2.42. (4.3. Results)
- Evaluations use synthetic benchmark mixtures (GRID and TCD-TIMIT) with known speakers; unknown speaker separation evaluated with 5-min fine-tuning; no large-scale real-world noisy environment benchmarks. (4. EXPERIMENTS)
- Requires visible speaker face video and speaker-dependent model training; unknown speaker separation requires fine-tuning with audiovisual data. (4.3. Results)
- This is an audiovisual separation system, not a silent speech interface. Unknown speaker separation still requires fine-tuning and visible face video, limiting immediate deployment. (5. CONCLUDING REMARKS)

## More reviews in Lip & face video

- [Improved Speech Reconstruction from Silent Video](../improved-speech-reconstruction-from-silent-video/) (2017). Reconstructs speech from silent full-face video plus optical flow with a CNN and temporal post-processing network, outperforming prior methods on GRID and TCD-TIMIT in objective metrics and human word accuracy.
- [Lip Reading Sentences in the Wild](../lip-reading-sentences-in-the-wild/) (2017). Introduces Watch, Listen, Attend and Spell and the BBC LRS dataset; lips-only decoding reaches 50.2% WER on open-vocabulary broadcast sentences, beating a professional lipreader (73.8%).
- [Lip2AudSpec: Speech reconstruction from silent lip movements video](../lip2audspec-speech-reconstruction-from-silent-lip-movements-video/) (2017). Lip2AudSpec reconstructs speech from silent lip video using an auditory-spectrogram autoencoder bottleneck as target, improving objective intelligibility metrics and human word accuracy (55.8% vs 50.9%) over a baseline on four GRID speakers.
- [Vid2speech: Speech Reconstruction from Silent Video](../vid2speech-speech-reconstruction-from-silent-video/) (2017). Vid2speech reconstructs intelligible speech from silent face video on GRID with speaker-specific models and LPC-style resynthesis, reaching about 80% human intelligibility and partial out-of-vocabulary recovery.
- [Deep Audio-Visual Speech Recognition](../deep-audio-visual-speech-recognition/) (2018). Landmark AVSR paper that releases LRS2-BBC and compares CTC and sequence-to-sequence Transformers on one shared encoder. Video-only TM-seq2seq reaches 48.3% WER with an LM (49.8% without; the 70.4% WAS baseline has no stated decoding conditions, and the same group's Transformer three months earlier already reached 50.0%). CTC and seq2seq differ little once an LM or audio is added.
- [Harnessing AI for Speech Reconstruction using Multi-view Silent Video Feed](../harnessing-ai-for-speech-reconstruction-using-multi-view-silent-video-feed/) (2018). Reconstructs speech audio from multi-view silent video on OuluVS2 with CNN-LSTM models, showing multi-view input improves PESQ over single view and that camera placement matters.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
