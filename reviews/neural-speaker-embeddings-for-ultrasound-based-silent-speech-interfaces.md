# Neural Speaker Embeddings for Ultrasound-based Silent Speech Interfaces

Amin Honarmandi Shandiz, László Tóth, Gábor Gosztolya, Alexandra Markó, Tamás Gábor Csapó  
arXiv / imported corpus page 2021 · [arXiv](https://arxiv.org/abs/2106.04552)

**Section:** [Ultrasound & tongue imaging](../README.md#ultrasound--tongue-imaging) · **Review basis:** full_text

Trains x-vector speaker embeddings from ultrasound tongue video, achieving under 1% speaker recognition error on unseen speakers, but adding them to multi-speaker ultrasound-to-speech synthesis gives only marginal gains.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Micro ultrasound system, mid-sagittal tongue images at 82 fps |
| Task | Speaker recognition and ultrasound-to-speech synthesis |
| Vocabulary | Not applicable |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Under 1% speaker recognition error on unseen speakers; single-speaker synthesis MCD 3.12 |

**Limitations.** Multi-speaker synthesis gains are marginal and evaluated speaker-dependently on the same 31 speakers; no robustness to session or probe shifts and no live deployment.

## Full review

### In short

The ultrasound-based x-vector speaker embedding is highly effective for speaker recognition, achieving under 1% error on unseen speakers, but its integration yields only a marginal improvement in multi-speaker ultrasound-to-speech synthesis accuracy.

### Review

This work presents a well-executed adaptation of the x-vector speaker embedding architecture to ultrasound tongue imaging for silent speech interfaces. The authors trained a 3D-CNN based x-vector network on 50 speakers from the TaL80 corpus and validated its speaker recognition ability on 31 held-out speakers, achieving extremely low error rates down to around 0.7% with a simple 1-NN classifier (Tables 1 and 2). The embedding vectors show appropriate clustering by speaker (Fig. 3), demonstrating strong speaker discriminability. However, when integrated as auxiliary input into a multi-speaker ultrasound-to-speech spectral estimator, the actual quantitative improvement in synthesis quality is marginal. The multi-speaker model's mean squared error in spectral estimation only improves slightly (from 0.669 to 0.653) with the addition of the x-vector embeddings (Table 3), a result consistent with prior reports. The system operates offline on the TaL80 dataset, and does not yet address critical practical issues such as cross-session robustness, probe placement variation, or fully speaker-independent synthesis, limiting immediate deployment readiness. Nonetheless, the paper provides a strong contribution in the area of speaker characterization from ultrasound video and highlights key challenges in extending this to multi-speaker SSI synthesis.

### Why it matters

The study firmly establishes that x-vector style embeddings can be trained successfully from ultrasound tongue video and generalize to unseen speakers, but reveals that naïve incorporation into SSI synthesis yields limited gains, indicating the need for more sophisticated integration methods and SSI modeling for speaker-independent multi-speaker operation.

### Prior state of the art

Ultrasound-based silent speech interfaces (SSI) have traditionally been speaker-dependent due to speaker-specific anatomical differences, and speaker conditioning usually relied on simpler speaker descriptors.

### What changed

Trains a dedicated ultrasound-based x-vector network for speaker embedding and injects it as an auxiliary input to a multi-speaker ultrasound-to-speech spectral estimation network.

### Position in the field

Speaker-representation study adjacent to multi-speaker ultrasound SSI research.

### Practical value

Strong speaker embedding for ultrasound data; marginal evidence for improved multi-speaker SSI synthesis so far.

### Advanced

speaker representation; multi-speaker modeling

### Unresolved

optimal integration of speaker embeddings into SSI synthesis; true speaker-independent multi-speaker synthesis; robustness to session variability and probe misalignment

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | ultrasound |
| Sensor | Articulate Instruments’ Micro ultrasound system capturing 64x842 pixel mid-sagittal tongue images at 82 fps, resized to 64x128 for processing. |
| Body site | tongue |
| Output | speech-audio |
| Metrics and results | Speaker recognition error rates (%); Mean squared error (MSE) in spectral estimation; Mel-cepstral distortion (MCD) derived from MSE was 3.12 for single speaker synthesis. |
| Evaluation protocol | Speaker recognition on held-out speakers and ultrasound-to-spectrum speech synthesis error evaluation in single and multi-speaker settings. |

### Limits

- **Technical:** Marginal multi-speaker synthesis gain likely due to suboptimal method of injecting speaker embeddings after convolutional layers; no robustness to session or probe changes tested.
- **Evaluation:** Multi-speaker synthesis experiments are speaker-dependent with train, dev, and test sets drawn from the same 31-speaker subset; no fully speaker-independent SSI evaluation presented.
- **Deployment:** No evidence of live deployment or robustness to session and probe shifts; no cross-session or probe-position variability handling demonstrated.
- **Scope of this review:** Ultrasound speaker representation with limited downstream multi-speaker speech synthesis evaluation on a controlled corpus.

### Evidence

- We adjusted the x-vector framework popular in speech processing to operate with ultrasound tongue videos, producing speaker embedding vectors which we tested in multi-speaker ultrasound-to-speech conversion. (Abstract)
- Speaker recognition error rates on development set for the 50-speaker training subset decreased to 1.96% with 164-frame (2 sec) segments (Table 1). (5. Results)
- Speaker recognition error rates for the held-out 31 speakers using 1-nearest neighbor leave-one-out testing are as low as 0.70% when embeddings are extracted from FC#2 without nonlinearity (Table 2). (5. Results)
- The mean squared error (MSE) for the ultrasound-to-spectrum spectral estimation task in the single-speaker setup is about 0.265 on the test set; in a multi-speaker setup without x-vector conditioning it rises to 0.669; adding x-vector conditioning marginally improves MSE to 0.653 (Table 3). (5. Results)
- The multi-speaker synthesis experiment is speaker-dependent as the training, development, and test sets come from the same 31 speakers, so full speaker-independence is not demonstrated; probe-shift and cross-session variation handling are not studied. (5. Results)
- The method used to integrate the x-vector speaker embeddings into the SSI spectral estimation network is suboptimal, as simple concatenation is not possible and embeddings were injected only after convolutional layers, limiting gain and requiring further study. (5. Results)
- No probe-shift, session-variation, or live SSI deployment study is provided, and results remain offline and lab-bound, limiting deployment readiness. (6. Conclusions)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
