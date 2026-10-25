# NasoVoce: A Nose-Mounted Low-Audibility Speech Interface for Always-Available Speech Interaction

Jun Rekimoto, Yu Nishimura, Bojian Yang  
CHI '26 / arXiv · [DOI](https://doi.org/10.1145/3772318.3791397) · [arXiv](https://arxiv.org/abs/2603.10324)

**Section:** [Acoustic, whisper & wearable motion sensors](../README.md#acoustic-whisper--wearable-motion-sensors) · **Review basis:** full_text+existing_expert_seed

NasoVoce, nose-pad microphone and vibration sensor on smart glasses, with multimodal fusion for low-audibility and whispered speech interaction under noise, evaluated by ASR error rates and audio quality.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Nose-pad MEMS microphone and vibration sensor in smart glasses |
| Task | Low-audibility speech enhancement and recognition |
| Vocabulary | Open vocabulary (via Whisper ASR) |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Not stated |
| Key result | Not reported |

**Limitations.** ASR evaluation uses synthetic noise; in-the-wild testing only qualitative; fusion not fully streaming; whispered vibration signals remain weak.

## Full review

### In short

A strong deployment-focused speech interface leveraging a novel nose-pad dual-sensor configuration and multimodal fusion to enable robust low-audibility speech interaction with AI under noise, backed by extensive evaluation.

### Review

NasoVoce represents a serious, well-constructed system integrating a discreet smart-glasses nose-pad form factor housing a MEMS microphone and vibration sensor. By fusing these complementary modalities via a novel dual-input D-DCCRN enhancement model trained with Whisper-based knowledge distillation, it robustly captures low-volume and whispered speech. The extensive dataset of 104 hours from 45 participants, rigorous evaluation covering ASR metrics, objective speech quality evaluation, a large-scale subjective study, and real-world qualitative trials establish its practical feasibility. While the core method is validated, deployment aspects such as continuous streaming, adaptive sensor fusion depending on context, smartphone integration, and accommodation for physiological variability like nasal patency require further study and development.

### Why it matters

Demonstrates a feasible, socially acceptable, and noise-robust wearable speech interface design embracing discreet whispered speech input complemented by a novel hardware sensor fusion architecture and rigorous multi-modal enhancement and ASR evaluation, moving beyond small-vocabulary silent speech towards open-vocabulary AI conversation.

### Prior state of the art

Wearable silent speech and whispered speech interfaces typically struggled to balance wearability, vocabulary size, noise robustness, and social acceptability, often limited to small command sets or requiring obtrusive sensors.

### What changed

NasoVoce innovates by mounting a MEMS microphone and vibration sensor at the smart glasses nose pad, capturing complementary air- and skin-conducted signals for robust low-volume and whispered speech capture, combined with a dual-input enhancement model.

### Position in the field

A strong modern SSI-adjacent wearable speech paper that refocuses from fully silent recognition to discreet, robust AI voice interaction with open vocabulary.

### Practical value

High for wearable AI voice agents by addressing sensor placement, noise robustness, perceptual quality, and practical evaluation in diverse contexts.

### Advanced

wearability; discreet_speech; noise_robust_capture; ai_voice_agent_alignment; multimodal_fusion

### Unresolved

continuous_streaming; adaptive_sensor_gating; longitudinal_wearability; physiological_variability

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-enhancement; speech-recognition for whispered and low-audibility speech to support always-available AI voice interaction |
| Input | acoustic; vibration; multimodal |
| Sensor | MEMS microphone (Syntiant SPH0141LM4H-1) and MEMS vibration sensor (Syntiant V2S200D) integrated in smart glasses nose pads providing synchronized PDM output. |
| Body site | face; nose; oral-cavity |
| Output | speech-audio |
| Vocabulary type | Open-vocabulary speech |
| Vocabulary size | Open vocabulary via downstream Whisper ASR |
| Metrics and results | Recognition accuracy expressed in word error rate (WER) and character error rate (CER) under varying noise conditions; PESQ and STOI perceptual audio quality; MUSHRA subjective audio quality scores. |
| Evaluation protocol | Quantitative ASR accuracy (WER, CER) on held-out data, objective perceptual quality metrics (PESQ, STOI), MUSHRA subjective ratings with 50 evaluators, and qualitative in-the-wild recordings in four real-world environments. |

### Limits

- **Technical:** Fusion model not fully streaming; whispered vibration signals remain weak limiting enhancement quality; performance under extreme noise favors vibration sensor input only at very low SNR.
- **Evaluation:** Evaluations used synthetic noise corruption for ASR and objective metrics; in-the-wild testing was qualitative with limited environments; no unseen words generalization tested.
- **Deployment:** Fully streaming continuous operation, smartphone integration, adaptive sensor gating based on SNR, and calibration for physiological factors such as nasal patency remain future work.
- **Scope of this review:** Targets low-audibility whispered speech, not fully silent speech without any acoustic leakage; assumes hand-covering mouth for privacy.

### Evidence

- NasoVoce is a smart-glasses nose-pad interface integrating a MEMS microphone and vibration sensor to capture low-audibility whispered speech robustly under environmental noise. (Abstract)
- The main sensing innovation is the nose-pad location combining airborne and skin-conducted sensing with a MEMS microphone and MEMS vibration sensor, mounted on smart glasses for discreet always-available speech interaction. (3 NasoVoce)
- ASR recognition accuracy measured in word error rate (WER) and character error rate (CER) using Whisper Large-v2 with 1,000 held-out items under synthetic noise ranging from -10 dB to 10 dB; objective perceptual speech quality evaluated with PESQ and STOI metrics; subjective MUSHRA ratings with 50 participants under different noise conditions. (5 Evaluation)
- Limitations include not yet achieving fully streaming speech processing integration, fusion performance degradation under extreme noise favoring vibration-only input, and the need for calibration to physiological variability such as nasal patency. (6 Discussions)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
