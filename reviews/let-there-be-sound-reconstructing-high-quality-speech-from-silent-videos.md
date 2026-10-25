# Let There Be Sound: Reconstructing High Quality Speech from Silent Videos

Ji-Hoon Kim, Jaehun Kim, Joon Son Chung  
arXiv / imported corpus page 2023 · [arXiv](https://arxiv.org/abs/2308.15256)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

Reconstructs speech from silent lip video using self-supervised linguistic conditioning, variance predictors and flow-based refinement. On GRID it reports WER 17.07% and MOS close to vocoded speech.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera (lip video) |
| Task | Speech synthesis from lip video |
| Vocabulary | GRID 51 words; Lip2Wav large vocabulary |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | WER 17.07%, CER 9.17% on GRID; MOS naturalness gap 0.28 vs vocoded speech |

**Limitations.** Evaluated mainly on constrained GRID and Lip2Wav subsets; multi-stage pipeline with no latency, streaming or real-world evaluation.

## Full review

### In short

Strong lip-to-speech system that reduces ambiguity via SSL linguistic conditioning, variance predictors, and flow-based refinement, achieving near-vocoded naturalness and improved intelligibility on standard datasets.

### Review

This work proposes a high-quality lip-to-speech reconstruction system using only lip video inputs. It innovatively addresses the intrinsic one-to-many mapping challenge caused by homophenes and speech variability. The authors leverage intermediate-layer HuBERT self-supervised representations as linguistic predictor targets, explicitly model pitch and energy variance to capture prosodic richness, and incorporate a flow-based post-net to refine mel-spectrogram outputs that otherwise tend to be over-smoothed. Comprehensive experiments on the constrained GRID dataset and the larger Lip2Wav Chemistry and Chess datasets demonstrate state-of-the-art results in both perceptual naturalness (MOS only 0.28 below vocoded speech on GRID) and intelligibility (WER/CER improvements compared to prior methods). Ablation studies confirm the critical contributions of each component, especially the self-supervised linguistic predictor and flow post-net. However, the method remains a multi-stage research system without real-time capabilities or end-to-end simplicity, limiting immediate deployment readiness. Evaluation is limited to public datasets without open-environment testing. Overall, the paper significantly advances lip-to-speech quality as a reconstruction problem focused on ambiguity reduction, but leaves challenges of generalization, inference efficiency, and deployment for future work.

### Why it matters

It contributes a novel pipeline that disentangles linguistic content and acoustic variation from silent lip video using self-supervised representations and variance modeling, refined by flow-based post-processing, achieving state-of-the-art high-quality lip-to-speech reconstruction.

### Prior state of the art

Lip-to-speech quality was limited by homophenes, over-smoothed outputs, and weak prosodic control.

### What changed

Employs SSL linguistic conditioning, explicit pitch and energy variance predictors, and a flow-based post-net refinement, moving beyond simple mel-spectrogram regression and inadequately modeled one-to-many ambiguities.

### Position in the field

Notable advance in lip-to-speech synthesis enhancing ambiguity resolution and speech quality with SSL and flow-based methods, representing leading-edge progress in video-to-speech.

### Practical value

Provides a strong lip-to-speech baseline with detailed component ablations and quantitative benchmarking useful for research and development of high-quality silent video speech synthesis systems.

### Advanced

ambiguity_reduction; speech_quality; prosody_modeling

### Unresolved

real-time inference; broader generalization; simpler end-to-end deployment

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | video |
| Sensor | camera |
| Body site | lip |
| Output | speech-audio |
| Vocabulary type | phonetic |
| Vocabulary size | GRID: 51; Lip2Wav: large vocabulary |
| Metrics and results | MOS naturalness gap 0.28 and intelligibility gap 0.16 vs vocoded speech on GRID; WER 17.07%, CER 9.17% on GRID; WER and CER improvements over prior SOTA on Lip2Wav; pitch distribution moments and energy MAE metrics validate variance predictors. |
| Evaluation protocol | MOS for naturalness and intelligibility, WER/CER via ASR transcription comparison, pitch-energy statistical analysis, and ablations. |

### Limits

- **Technical:** Multi-stage pipeline; no latency or streaming evaluation; complex architecture not end-to-end; needs neural vocoder at inference.
- **Evaluation:** Evaluated mainly on GRID and Lip2Wav subsets, which are relatively constrained and do not cover open-world, real-time, or cross-domain deployment scenarios.
- **Deployment:** No real-time or on-device deployment targets; system is a multi-stage research pipeline without simplified inference or low-latency optimization.
- **Scope of this review:** Lip-to-speech reconstruction from silent video only; no multi-modal or audio-assisted input considered.

### Evidence

- We propose a novel lip-to-speech system that alleviates the one-to-many mapping problem by incorporating self-supervised speech representations to disambiguate homophenes, modeling acoustic variance for speech variation, and employing a flow-based post-net to refine synthesized speech details. (Introduction)
- Our method combines self-supervised linguistic targets from intermediate HuBERT layers, explicit variance predictors for pitch and energy, and a flow-based post-net to enhance speech reconstruction quality, addressing one-to-many ambiguity more explicitly than previous work. (Method)
- On the GRID dataset, our model achieves a MOS gap from vocoded speech of only 0.28 in naturalness and 0.13 in intelligibility; WER and CER are 17.07% and 9.17% respectively, outperforming previous lip-to-speech methods. (Quantitative Results)
- We evaluate on the constrained GRID dataset and larger Lip2Wav Chemistry and Chess multi-speaker subsets; evaluation includes MOS naturalness/intelligibility, WER/CER via ASR, and pitch-energy statistics. (Experimental Settting)
- The system is a multi-stage research pipeline without real-time or on-device deployment claims; end-to-end simplification and inference latency remain for future work. (Conclusion)
- Evaluations are limited to GRID and Lip2Wav datasets which do not cover open-world or real-time deployment, with manual transcription used in Lip2Wav due to lack of text labels. (Evaluation Metrics)
- Each component independently contributes to quality: linguistic predictor clarifies homophenes improving intelligibility and errors; pitch and energy variance predictors improve prosodic modeling; flow post-net improves naturalness and detail. (Ablation Study)
- Using the 12th layer of HuBERT-large with 200 K-means clusters for quantized linguistic representation yields the best intelligibility (lowest phoneme error rate) and contributes strongly to pronunciation accuracy in the model. (Analysis on Self)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
