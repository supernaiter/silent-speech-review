# Unvoiced: Designing an LLM-assisted Unvoiced User Interface using Earables

Tanmay Srivastava, Prerna Khanna, Shijia Pan, Phuc Nguyen, Shubham Jain  
Proceedings of the 22nd ACM Conference on Embedded Networked Sensor Systems (SenSys '24), pp. 784-798 · [DOI](https://doi.org/10.1145/3666025.3699374)

**Section:** [Acoustic, whisper & wearable motion sensors](../README.md#acoustic-whisper--wearable-motion-sensors) · **Review basis:** full_text

A structured review of *Unvoiced: Designing an LLM-assisted Unvoiced User Interface using Earables* (Tanmay Srivastava et al., Proceedings of the 22nd ACM Conference on Embedded Networked Sensor Systems (SenSys '24), pp. 784-798) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Twin-IMU earable captures jaw motion during unvoiced speech; spectrograms are transcribed by Whisper and gaps filled by GPT-4, giving 93-99% task completion and 0.07-0.14 WER across 19 users.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Twin-IMU earable (jaw motion accelerometer and gyroscope) |
| Task | Unvoiced command and phrase recognition via spectrogram generation |
| Vocabulary | Task phrases, 20 commands, digits, 30 general phrases, 50 unseen words |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Not stated |
| Key result | 93.1-98.6% task completion; WER 0.07 (seen phrases), 0.14 (unseen words); 19 participants |

**Limitations.** Per-user models trained with audible samples; LLM correction leans on language priors; latency and power unreported; prototype only.

## Full review

### In short

Earable jaw-motion SSI that leans on Whisper and GPT-4 to fill gaps; promising task completion, user-dependent.

### Review

Unvoiced uses a twin-IMU earable (one IMU at the temporal bone, one at the temporomandibular joint as a noise reference) to capture jaw motion during unvoiced speech, generates word-level spectrograms with a BiLSTM-attention model and a six-term custom loss, transcribes them with Whisper, and lets GPT-4 plus a vowel-class SVM fill missing words. With 19 participants it reports task completion of 93.1-98.6% across four command tasks, WER of 0.07 on in-training phrases and 0.14 on 50 unseen words, and above 90% top-1 on isolated commands. Robustness to walking and 60 dB noise is tested. The models are personalized (training uses 20 audible samples per item per user), latency and power are not reported, and the LLM step means accuracy partly reflects language priors over a small task space rather than signal decoding alone.

### Why it matters

Shows how an LLM can be used as an explicit error-correction layer over a weak, low-bandwidth jaw-motion signal to make earable silent commands usable.

### Prior state of the art

Earable jaw-motion SSI (e.g., MuteIt) recognized small command sets with signal processing or classifiers and had no mechanism to recover missing or ambiguous words.

### What changed

Maps IMU jaw motion to spectrograms recognized by Whisper and adds GPT-4 gap filling with phonetic (vowel-class) filtering, plus a twin-IMU noise reference.

### Position in the field

Representative earable IMU SSI paper and an early example of LLM-assisted silent speech decoding.

### Practical value

Practical template for earable silent commands; field use limited by personalization and unreported latency/power.

### Advanced

llm_assisted_decoding; earable_form_factor; motion_noise_cancellation

### Unresolved

User-independent models; latency and power; commercial earable compatibility; broader vocabularies

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction; speech-recognition; command-recognition |
| Input | IMU jaw motion (accelerometer and gyroscope) |
| Sensor | twin-IMU earable prototype (temporal bone and temporomandibular joint) |
| Body site | jaw |
| Output | text; commands |
| Vocabulary type | task phrases, isolated commands, digits and general phrases |
| Vocabulary size | 4 tasks x 5 phrases; 30 general phrases; 20 commands plus digits 0-9; 50 unseen words |
| Metrics and results | Task completion 98.6%, 97.7%, 94.8%, 93.1% on four tasks; WER 0.07 in-training phrases, 0.11 out-of-training phrases, 0.14 unseen words; isolated-command top-1 above 90%; TCR 93% at 60 dB acoustic noise |
| Evaluation protocol | 19-participant user study with per-user models, baselines (MuteIt, LIMU-BERT, BiDiLSTM), motion and acoustic noise, longitudinal and leave-one-user-out fine-tuning tests |

### Limits

- **Technical:** Per-user models trained with audible samples; LLM correction can hallucinate plausible but wrong words; reliance on Whisper and GPT-4 adds compute and possibly cloud dependence.
- **Evaluation:** 19 participants with small task phrase sets; some inconsistencies between reported numbers in text and figures (e.g., 25-day vs 4-week longitudinal study); latency and power not reported.
- **Deployment:** Research prototype not tested on commercial earables; motion noise types limited; users with speech impairments not studied.
- **Scope of this review:** Unvoiced command and short-phrase recognition from jaw motion via earables.

### Evidence

- The paper presents an earable unvoiced user interface that converts jaw motion to word spectrograms, transcribes them with Whisper, and uses GPT-4 with phonetic filtering to fill missing words. (Abstract; Sections 4-6)
- The prototype uses two IMUs, one at the temporal bone and one at the temporomandibular joint as a reference for adaptive noise cancellation; audio is used only in training. (Hardware and preprocessing sections)
- Task completion rates are 98.6%, 97.7%, 94.8% and 93.1% for media control, home control, messaging and quick notes. (Section 8, evaluation)
- Table 2 reports WER 0.07 for in-training phrases, 0.11 for out-of-training phrases and 0.14 for 50 unseen words. (Table 2)
- 19 participants (11 female, 8 male) with five native languages; 8 took part in noisy sessions; per-user training uses 20 audible samples per phrase, command or digit. (Study design section)
- The authors list personalized models, an early prototype not tested on commercial earables, limited noise types and a small, non-diverse population as limitations. (Section 10)

## More reviews in Acoustic, whisper & wearable motion sensors

- [Poster: Recognizing Hidden-in-the-Ear Private Key for Reliable Silent Speech Interface Using Multi-Task Learning](poster-recognizing-hidden-in-the-ear-private-key-for-reliable-silent-speech-interface-using-mult.md) (2025). HEar-ID jointly recognizes whispered ear-canal letter spelling and user identity from in-ear audio and ultrasonic reflections; Top-1 word accuracy is 67.3% across 11 users (90.25% for eight selected users).
- [Silent Speech Sentence Recognition with Six-Axis Accelerometers using Conformer and CTC Algorithm](silent-speech-sentence-recognition-with-six-axis-accelerometers-using-conformer-and-ctc-algorith.md) (2025). Uses six wearable 6-axis IMUs (accelerometer plus gyroscope) on the face and neck with a Conformer-CTC model to recognize silently articulated words and word sequences. Reports 97.17% word-level accuracy in a 4-participant study.
- [EchoSpeech: Continuous Silent Speech Recognition on Minimally-obtrusive Eyewear Powered by Acoustic Sensing](echospeech-continuous-silent-speech-recognition-on-minimally-obtrusive-eyewear-powered-by-acoustic.md) (2023). Glasses-mounted inaudible FMCW sonar recognizes silent speech from facial skin echoes: 4.5% WER on 31 commands and 6.1% on connected digits in 12 users, with walking/noise tests and a 73.3 mW demo.
- [Ultrasensitive Textile Strain Sensors Redefine Wearable Silent Speech Interfaces with High Machine Learning Efficiency](ultrasensitive-textile-strain-sensors-redefine-wearable-silent-speech-interfaces-with-high-machine-learning-efficiency.md) (2023). Combines an ultrasensitive graphene textile strain sensor in a throat choker with a lightweight 1D residual CNN to classify silent words. Reports 95.25% accuracy on 20 words and 90% few-shot transfer with 30 samples per class.
- [WESPER: Zero-shot and Realtime Whisper to Normal Voice Conversion for Whisper-based Speech Interactions](wesper-zero-shot-and-realtime-whisper-to-normal-voice-conversion-for-whisper-based-speech-interactions.md) (2023). WESPER converts whispered speech to normal voice zero-shot and in real time without per-user paired data; conversion cuts Google ASR WER on wTIMIT whispers from 44.70 to 26.68.
- [NasoVoce: A Nose-Mounted Low-Audibility Speech Interface for Always-Available Speech Interaction](nasovoce.md) (2026). NasoVoce, nose-pad microphone and vibration sensor on smart glasses, with multimodal fusion for low-audibility and whispered speech interaction under noise, evaluated by ASR error rates and audio quality.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
