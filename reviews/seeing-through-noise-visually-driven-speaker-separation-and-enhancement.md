# Seeing Through Noise: Visually Driven Speaker Separation and Enhancement

Aviv Gabbay, Ariel Ephrat, Tavi Halperin, Shmuel Peleg  
arXiv / imported corpus page 2017 · [arXiv](https://arxiv.org/abs/1708.06767)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

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

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
