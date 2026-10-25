# Ultrasound-based Silent Speech Interface Built on a Continuous Vocoder

Moham Salah Alradhi, Géza Németh, Gábor Gosztolya, Tamás Gábor Csapó, László Tóth, Alexandra Markó  
arXiv / imported corpus page 2019 · [arXiv](https://arxiv.org/abs/1906.09885)

**Section:** [Ultrasound & tongue imaging](../README.md#ultrasound--tongue-imaging) · **Review basis:** full_text+structured_benchmark+summary

Adds CNN-based continuous F0 prediction to an ultrasound tongue-imaging SSI vocoder, lowering pitch RMSE versus a discontinuous F0 baseline, with a non-significant naturalness trend in MUSHRA tests on four Hungarian speakers.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Midsagittal ultrasound tongue imaging (~82 fps) |
| Task | Speech synthesis from ultrasound |
| Vocabulary | Not stated |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | F0 RMSE ~30.6 Hz vs ~65.3 Hz baseline; V/UV accuracy ~78.8% |

**Limitations.** Small four-speaker Hungarian dataset, speaker-dependent training, no speaker-independent evaluation, and naturalness gains are not significant.

## Full review

### In short

The key advancement is continuous F0 tracking via CNNs yielding lower pitch error and slight naturalness improvement over discontinuous F0 pipelines in ultrasound SSI.

### Review

This paper presents an incremental but meaningful refinement in ultrasound-based SSIs by employing a continuous F0 vocoder predicting ContF0 and MVF directly from ultrasound tongue images via CNNs. The continuous F0 modeling reduces F0 RMSE substantially compared to discontinuous F0 baseline. Subjectively, synthesized speech gains slight, though statistically non-significant, naturalness improvement. The study uses a four-speaker Hungarian dataset with limited utterance duration, thus generalization, real-time deployment beyond controlled settings, and cross-speaker robustness need further exploration. Nevertheless, the method provides a computationally feasible vocoder design that simplifies excitation modeling in SSI and contributes to the field by transitioning from discontinuous to continuous pitch modeling.

### Why it matters

Demonstrates that continuous pitch estimation from ultrasound articulatory data is feasible and beneficial for SSI vocoders, improving pitch modeling and slightly enhancing speech naturalness, without introducing new sensor modalities.

### Prior state of the art

Prior UTI-based SSI vocoder systems typically predicted discontinuous F0 with a binary voiced/unvoiced classification followed by voiced F0 regression.

### What changed

Replaces the discontinuous voiced/unvoiced F0 prediction pipeline with continuous F0 interpolation and a continuous vocoder framework predicting ContF0 and MVF parameters.

### Position in the field

A vocoder-focused SSI articulation-to-speech synthesis study focusing on continuous pitch modeling from ultrasound tongue images.

### Practical value

Potentially improves synthesized speech naturalness in ultrasound-based SSI by refining pitch modeling, but practical deployment is limited by dataset size and hardware requirements.

### Advanced

system_design; evaluation

### Unresolved

Cross-speaker generalization and robustness beyond the four-speaker UTI dataset used remain unaddressed.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | ultrasound tongue imaging |
| Sensor | Ultrasound tongue imaging system capturing midsagittal tongue ultrasound cine at ~82 fps. |
| Body site | tongue |
| Output | speech-audio |
| Metrics and results | V/UV classification accuracy (about 78.8% average), F0 Root Mean Square Error (RMSE) in Hz (continuous F0 ~30.6 Hz, baseline discontinuous ~65.3 Hz), Maximum Voiced Frequency RMSE (654–1177 Hz range depending on speaker), subjective MUSHRA naturalness scores with no significant difference but trend favoring continuous vocoder. |
| Evaluation protocol | Objective (V/UV accuracy, RMSE) plus subjective listening tests (MUSHRA) by native Hungarian speakers. |

### Limits

- **Technical:** Limited speaker generalization; linked to fixed ultrasound frame rate for prediction; MVF estimation accuracy varies by speaker; CNN uses single frames rather than consecutive or recurrent context which might improve accuracy.
- **Evaluation:** Evaluated using a small dataset of four speakers; objective metrics include V/UV classification accuracy and F0 RMSE, while subjective MUSHRA tests show minor non-significant gains in naturalness.
- **Deployment:** Requires ultrasound tongue imaging hardware and a CNN-based vocoder pipeline; real-time capabilities are mentioned but deployment is limited by hardware and speaker-dependent training.
- **Scope of this review:** Limited to ultrasound tongue imaging based SSI for speech reconstruction; small four-speaker Hungarian dataset; no speaker-independent evaluation.

### Evidence

- We use a continuous F0 tracker which does not apply a strict voiced/unvoiced decision. Continuous vocoder parameters (ContF0, Maximum Voiced Frequency and Mel-Generalized Cepstrum) are predicted using a convolutional neural network with UTI as input, improving naturalness compared to baseline vocoder using standard discontinuous F0. (Abstract)
- The proposed system uses continuous pitch tracking via interpolation of F0 in unvoiced regions, avoiding the discontinuities caused by strict voiced/unvoiced binary splits common in prior SSI vocoders. (2. Continuous F0 modeling within vocoders)
- Objective evaluation shows average V/UV decision accuracy around 78.8%, baseline F0 prediction RMSE about 65 Hz, and continuous F0 prediction RMSE about 30.6 Hz across four speakers, indicating the continuous F0 model yields significantly lower pitch error. (4.2. Objective evaluation)
- Data recorded from four Hungarian speakers (2 female, 2 male), about 15-minute recordings each composed of 209 sentences, split into training/validation/test sets; evaluation on 9 test sentences per speaker; speaker-dependent CNN models trained separately. (3.1. Data acquisition)
- Subjective MUSHRA listening tests conducted with 23 native Hungarian listeners comparing baseline and continuous vocoder synthetic speech; results indicate slightly better but not statistically significant naturalness in continuous vocoder output. (4.3. Subjective listening test)
- The system uses speaker-dependent models trained on ultrasound data recorded at fixed frame rate (~82 fps); the CNN input are single ultrasound images without recurrent context, which limits generalization and temporal modeling; cross-speaker and broader corpus robustness are not demonstrated. (3.4. DNN training with the baseline vocoder)
- The vocoder design uses low-dimensional excitation parameters (ContF0 and MVF) predicted by CNNs from ultrasound images, enabling computationally feasible speech synthesis potentially suitable for real-time operation, though adaptation to wearable or mobile platforms and speaker-independent models are not addressed. (5. Conclusions)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
