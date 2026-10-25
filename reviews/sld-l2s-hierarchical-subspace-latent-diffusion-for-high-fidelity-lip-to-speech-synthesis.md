# SLD-L2S: Hierarchical Subspace Latent Diffusion for High-Fidelity Lip to Speech Synthesis

Yifan Liang, Andong Li, Kang Yang, Guochen Yu, Fangkun Liu, Lingling Dai, Xiaodong Li, Chengshi Zheng  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2602.11477)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text+summary

SLD-L2S, a hierarchical subspace latent diffusion model for lip-to-speech synthesis that improves naturalness, while word accuracy and speaker similarity trail stronger baselines.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Existing RGB video (mouth crops) |
| Task | Lip-to-speech synthesis |
| Vocabulary | Continuous speech; size not reported |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | LRS3 WER 30.22%, UTMOS 4.21; listener naturalness 4.17 vs 3.88 (V2SFlow) |

**Limitations.** Needs reference audio for speaker identity; WER worse than baselines; small listener study; no measured runtime or latency.

## Full review

### In short

Improves lip-to-speech naturalness with a structured codec-latent flow model, but word accuracy and speaker similarity trail stronger baselines; reference audio and unmeasured runtime limit broader claims.

### Review

SLD-L2S makes a plausible case for generating continuous neural-codec latents with a structured convolutional flow model. The matched DiT comparison and the LRS2 transfer test are useful, and the strongest outcome is improved perceived naturalness: LRS3 listeners rate the proposed method at 4.17 versus 3.88 for V2SFlow. That gain should not be mistaken for better recovery of the words. WER is 30.22% on LRS3 and 39.54% on LRS2, worse than V2SFlow and substantially worse than LipVoicer; subjective intelligibility and speaker similarity also remain below V2SFlow. Learned quality predictors even rate the generated speech above the original recordings, illustrating why these scores cannot establish faithful reconstruction by themselves. The input boundary also matters: although linguistic content comes from video, a reference audio utterance supplies the speaker embedding, so the evaluated system does not recover voice identity from lip movements alone. The ablations reveal a multi-objective trade-off rather than uniformly beneficial components: removing the SLM loss improves UTMOS, SCOREQ and WER while reducing D-BERT and speaker similarity. Finally, ten flow evaluations are an algorithmic step count, not measured end-to-end latency, and ordinary speech-video benchmarks do not establish transfer to actual silent articulation or speech impairment. This is a worthwhile synthesis-quality result with a concrete architecture contribution, but content fidelity and operational evidence remain the main limitations.

### Why it matters

Demonstrates a quality-oriented continuous-codec generation route and exposes the trade-offs among naturalness, lexical accuracy and identity preservation.

### Prior state of the art

Lip-to-speech systems already use AV-HuBERT, diffusion/flow models and neural codecs or speech units. Lip movements underdetermine phonetic detail, prosody and speaker voice; generative priors can improve naturalness without guaranteeing intended words.

### What changed

Generates continuous X-Codec-hubert latents from visual features and a reference speaker embedding using subspace convolutional flow modeling, instead of directly predicting mel features or discrete residual tokens.

### Position in the field

Non-invasive video-to-speech synthesis with audio-conditioned speaker identity; adjacent to silent-speech interfaces but evaluated on normal speech videos.

### Practical value

A promising high-naturalness synthesis baseline; applications requiring exact communication should prioritize reducing word errors and validating input/reference conditions.

### Advanced

Higher predicted audio-quality scores on two benchmarks and higher rated naturalness on LRS3; ten flow evaluations rather than thirty for V2SFlow; parameter-matched backbone and loss ablations.

### Unresolved

Actual inference time/energy, reference-speaker utterance selection, silent-articulation/patient transfer, statistical reliability of listener differences, and disentangled contributions of subspace structure versus codec/pretraining.

### Narrowed or regressed

WER is worse than V2SFlow and LipVoicer on both datasets, and speaker similarity is below V2SFlow. Some loss removals improve quality predictors and WER while reducing embedding similarity.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | Mouth-region video for content plus a reference audio-derived speaker embedding for voice identity. |
| Sensor | Existing RGB video processed into 88 x 88 grayscale mouth crops using facial landmarks; no acquisition hardware or new recording system reported. |
| Body site | lip;face |
| Output | speech-audio |
| Vocabulary type | continuous speech-video corpus synthesis |
| Vocabulary size | No fixed command vocabulary; exact evaluated lexical size is not reported. |
| Metrics and results | Table 1: LRS3 UTMOS 4.2096, SCOREQ 4.6075, D-BERT 0.8284, WER 30.22%, SECS 0.804; LRS2 WER 39.54%. V2SFlow WER is 27.55%/34.17%, and LipVoicer 20.62%/24.92%. Table 2 listener naturalness/intelligibility/similarity: proposed 4.17/3.65/3.77, V2SFlow 3.88/3.69/3.90. Proposed uses 10 function evaluations versus V2SFlow 30. No measured inference time or independent reproduction. |
| Evaluation protocol | Offline LRS3 synthesis and LRS2 transfer; learned quality metrics, recognizer-derived WER, speech/speaker embedding similarities, five-point listener ratings and architecture/loss ablations. |

### Limits

- **Technical:** Visual ambiguity persists despite perceptual priors. Full generator has 57.7M parameters in the DiCB comparison, excluding unspecified complete-system cost. Speaker identity requires GE2E reference audio. Data-prediction loss weights by 1/(1-t)^2; numerical endpoint handling is not specified. Semantic, quality and word metrics respond differently to loss choices.
- **Evaluation:** Small subjective evaluation: 15 listeners and 30 synthesized samples, with randomization/blinding and uncertainty definitions not fully described. Baselines have heterogeneous reference-speaker and frontend dependencies. No repeated-seed uncertainty or latency benchmark. Table 3 duplicates a loss-removal label, leaving the final ablation ambiguous.
- **Deployment:** Large pretrained visual encoder and iterative generator, with speaker identity obtained from reference audio. No measured latency, mobile power, streaming interaction or patient evaluation.
- **Scope of this review:** Offline English speech-video benchmarks and a small listening study. No actual silent articulation, patient communication, walking or longitudinal user evaluation.

### Evidence

- The model combines AV-HuBERT visual features, parallel subspace decomposition, a convolutional flow backbone and continuous neural-codec latent generation with semantic and SLM auxiliary losses. (Proposed Method; Figure 1; PDF pp. 3-5)
- Task training uses LRS3 official splits; LRS2 is a transfer test. Speaker identity is supplied by a 256-dimensional GE2E embedding from a reference utterance. Reviewer assessment: the evaluated identity input is not purely visual. (Experimental Setup and Implementation Details; PDF pp. 5-6)
- Table 1 reports WER 30.22%/39.54% on LRS3/LRS2, versus V2SFlow 27.55%/34.17% and LipVoicer 20.62%/24.92%. Quality gains therefore coexist with worse lexical error rates. (Table 1; PDF p. 5)
- Fifteen listeners assess 30 synthesized samples. Table 2 gives proposed naturalness 4.17, intelligibility 3.65 and similarity 3.77, versus V2SFlow 3.88, 3.69 and 3.90 respectively. (Table 2 and Evaluation Metrics; PDF p. 6)
- Table 1 quality predictors score the proposed synthesis above ground-truth recordings on both datasets, while human naturalness remains below ground truth. Reviewer assessment: reference-free quality scores are not measures of exact reconstruction fidelity. (Tables 1-2; PDF pp. 5-6)
- The DiCB versus DiT ablation approximately matches parameters at 57.7M versus 57.8M. Replacing DiCB reduces SECS from 0.804 to 0.618, with smaller changes in WER and quality metrics. (Table 3; PDF p. 6)
- Removing SLM loss increases UTMOS from 4.2096 to 4.2885 and SCOREQ from 4.6075 to 4.6958, and lowers WER from 30.22% to 29.99%, while reducing D-BERT and SECS. Reviewer assessment: the loss has metric-specific trade-offs, not uniformly better intelligibility. (Table 3; Auxiliary Losses discussion; PDF pp. 6-7)
- Table 3 labels two different rows w/o Lsem, while the prose also discusses removing both losses. Reviewer assessment: the final ablation label must be clarified rather than silently reinterpreted. (Table 3; Ablation Study; PDF pp. 6-7)
- Ten function evaluations are compared with thirty for V2SFlow, but no complete inference-time or energy measurement is reported. Reviewer assessment: fewer steps do not establish a faster end-to-end deployed system. (Table 1; Comparison with State-of-the-Art Methods; PDF pp. 5-7)
- The experiments use ordinary LRS3/LRS2 speech videos; no new silent-articulation or speech-impaired participant study is presented. (Experimental Setup; Results; PDF pp. 5-7)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
