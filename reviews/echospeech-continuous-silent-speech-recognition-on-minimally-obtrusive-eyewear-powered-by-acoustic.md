# EchoSpeech: Continuous Silent Speech Recognition on Minimally-obtrusive Eyewear Powered by Acoustic Sensing

Ruidong Zhang, Ke Li, Yihong Hao, Yufan Wang, Zhengnan Lai, François Guimbretière, Cheng Zhang  
CHI '23 · [DOI](https://doi.org/10.1145/3544548.3580801)

**Section:** [Acoustic, whisper & wearable motion sensors](../README.md#acoustic-whisper--wearable-motion-sensors) · **Review basis:** full_text

A structured review of *EchoSpeech: Continuous Silent Speech Recognition on Minimally-obtrusive Eyewear Powered by Acoustic Sensing* (Ruidong Zhang et al., CHI '23) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Glasses-mounted inaudible FMCW sonar recognizes silent speech from facial skin echoes: 4.5% WER on 31 commands and 6.1% on connected digits in 12 users, with walking/noise tests and a 73.3 mW demo.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Glasses-mounted speakers and microphones (inaudible FMCW active acoustic sensing) |
| Task | Silent command and connected-digit recognition |
| Vocabulary | 31 commands; connected 3-6 digit numbers |
| Speaker | Speaker-dependent |
| Session | Cross-session |
| Online / offline | Both |
| Key result | WER 4.5% commands, 6.1% digits; 16.8% walking without mobile data |

**Limitations.** Closed vocabulary; needs user fine-tuning (~40% WER without); sensitive to glasses slippage; no activation detection.

## Full review

### In short

Glasses-mounted inaudible FMCW sonar recognizes 31 silent commands (4.5% WER) and connected digits (6.1% WER) across remounts, with walking tests and a 73.3 mW smartphone demo, but needs per-user fine-tuning.

### Review

EchoSpeech is one of the most cited wearable SSI papers of the period and a clean example of active acoustic sensing. Two speakers and two microphones on a glasses frame emit 18-21 kHz and 21.5-24.5 kHz FMCW sweeps; differential echo profiles from four speaker-microphone paths capture skin deformation during silent speech, and a ResNet-18 with CTC decodes discrete commands or connected 3-6-digit numbers. In 12 participants, with the device removed and re-donned between sessions, user-specific fine-tuning (about 30 min) gave 4.5% WER on 31 commands and 6.1% on connected digits; with 6-8 minutes WER rose to 9.5%/14.4%, and without fine-tuning to about 40%. Walking without mobile training data raised WER to 16.8%, reduced to 10.7-13.1% with added walking data; a second 12-person study in a noisier room reached 4.7% with mobile fine-tuning. Injected 64-76 dB(A) noise changed WER by only 2-3%. A low-power BLE variant runs at 73.3 mW with smartphone inference. Limits: small closed vocabulary, user-dependent calibration, sensitivity to glasses slippage, no activation detection, and an ear-canal SPL near recommended limits at full amplitude.

### Why it matters

Shows that minimally obtrusive eyewear with commodity speakers and microphones can support continuous silent command and digit recognition robust to remounting, noise and walking at smartphone-level power.

### Prior state of the art

Acoustic-sensing SSIs used phones held near the mouth or isolated-word recognition; wearable SSIs often relied on skin-contact EMG or cameras.

### What changed

Glasses-frame FMCW sonar with multi-path echo profiles and CTC-based continuous recognition, evaluated with remounting, walking and noise, plus a low-power real-time demo.

### Position in the field

Representative CHI wearable acoustic SSI; benchmark for later earable/headphone sonar SSIs (e.g., HPSpeech) in the acoustic section.

### Practical value

Practical form factor and power budget for command-level silent input; strong template for evaluation under remounting and walking.

### Advanced

Wearable unobtrusiveness; continuous (connected-digit) recognition; remount, walking and noise robustness; power consumption.

### Unresolved

Open-vocabulary sentences; calibration-free use; activation detection; long-term in-the-wild use; acoustic exposure safety.

### Narrowed or regressed

Accuracy degrades without user-specific fine-tuning (about 40% WER) and when glasses slip.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | Silent recognition of discrete commands and continuous connected digits from facial skin deformation. |
| Input | Active acoustic sensing (inaudible FMCW echoes) from glasses-mounted speakers and microphones. |
| Sensor | Two speakers (18-21 kHz, 21.5-24.5 kHz FMCW, 12 ms sweeps) and two microphones on the glasses frame, 50 kHz sampling, Teensy 4.1; low-power BLE variant with nRF52840. |
| Body site | Face (cheek/skin around mouth, sensed from glasses frame). |
| Output | Command and digit labels (text tokens). |
| Vocabulary type | Closed vocabulary: 31 discrete commands and connected 3-6-digit numbers. |
| Vocabulary size | 31 commands; 10 digits. |
| Metrics and results | Main study (12 participants, user fine-tuning ~30 min): command WER 4.5% (SD 3.5), connected digits 6.1% (SD 4.2). With 6-8 min: 9.5%/14.4%; no fine-tuning ~40%. Walking without mobile data 16.8%; with others' walking data 13.1%/13.2%; with follow-up data 10.7%. Follow-up study (12 new participants): 4.7% with 10 mobile sessions, 8.2% with 2. Noise 64-76 dB(A): +2-3% WER static. Power 73.3 mW. |
| Evaluation protocol | User-dependent training with remounting between sessions, walking sessions, injected noise; real-time smartphone demos (CAD, music control, text input). |

### Limits

- **Technical:** Performance degrades when glasses are pushed or slip, especially for smaller faces; single speaker-microphone path doubles WER (5.8% to 12.0%).
- **Evaluation:** Small closed vocabularies (31 commands, digits); 12+12 participants, mostly non-native speakers; lab settings only; end-to-end latency not reported.
- **Deployment:** Requires 6-30 min user-specific data for best accuracy; no activation detection; estimated ear-canal SPL 78.6 dB at 100% amplitude (62.2 dB at 20%).
- **Scope of this review:** Read the author-hosted CHI '23 PDF via automated extraction (about the last 6% of text, likely references, not read); figures not visually inspected. Full-text alternative to an abstract-based EchoSpeech record.

### Evidence

- Two speakers on the left frame edge emit 18-21 kHz and 21.5-24.5 kHz FMCW sweeps (12 ms) and two microphones on the right edge sample at 50 kHz; four speaker-microphone paths form differential echo profiles. (Sec. 4.1, 4.3, 5.1-5.2; Fig. 1, 4)
- ResNet-18 with spatial pooling and CTC loss decodes both discrete commands and continuous connected digits from echo profiles; LSTM/GRU layers did not help. (Sec. 5.3-5.4; Sec. 8.2)
- Across 12 participants with remounting between sessions, WER was 4.5% (SD 3.5) for 31 commands and 6.1% (SD 4.2) for connected digits using about 30 min of user data. (Sec. 6.2, 7.2; Fig. 5)
- With 6-8 minutes of fine-tuning data WER was 9.5% (commands) and 14.4% (digits); without fine-tuning about 40%. (Sec. 7.2.3; Fig. 6a)
- Walking without mobile training data gave 16.8% WER; adding other users' walking data lowered commands to 13.1% and adding follow-up data to 10.7%. (Sec. 7.2.4; Sec. 7.3.2)
- A follow-up study with 12 new participants in a noisier room reached 4.7% WER (10 mobile sessions) and 8.2% (2 sessions) on commands. (Sec. 6.3, 7.3-7.4)
- Street (64 dB(A)) and restaurant (76 dB(A)) noise raised static WER by about 2% and 3%. (Sec. 7.7)
- A low-power variant (one speaker, two microphones, BLE) consumes 73.3 mW with inference on a smartphone; demos used 1-6 min of training data. (Sec. 8.1, 8.3, 8.5; Abstract)
- Glasses slippage degrades accuracy, activation detection is not evaluated, native vs non-native comparison is underpowered, and estimated ear-canal SPL is 78.6 dB at full amplitude. (Sec. 8.4-8.7)

## More reviews in Acoustic, whisper & wearable motion sensors

- [Ultrasensitive Textile Strain Sensors Redefine Wearable Silent Speech Interfaces with High Machine Learning Efficiency](ultrasensitive-textile-strain-sensors-redefine-wearable-silent-speech-interfaces-with-high-machine-learning-efficiency.md) (2023). Combines an ultrasensitive graphene textile strain sensor in a throat choker with a lightweight 1D residual CNN to classify silent words. Reports 95.25% accuracy on 20 words and 90% few-shot transfer with 30 samples per class.
- [WESPER: Zero-shot and Realtime Whisper to Normal Voice Conversion for Whisper-based Speech Interactions](wesper-zero-shot-and-realtime-whisper-to-normal-voice-conversion-for-whisper-based-speech-interactions.md) (2023). WESPER converts whispered speech to normal voice zero-shot and in real time without per-user paired data; conversion cuts Google ASR WER on wTIMIT whispers from 44.70 to 26.68.
- [Unvoiced: Designing an LLM-assisted Unvoiced User Interface using Earables](unvoiced-designing-an-llm-assisted-unvoiced-user-interface-using-earables.md) (2024). Twin-IMU earable captures jaw motion during unvoiced speech; spectrograms are transcribed by Whisper and gaps filled by GPT-4, giving 93-99% task completion and 0.07-0.14 WER across 19 users.
- [EarCommand: "Hearing" Your Silent Speech Commands In Ear](earcommand-hearing-your-silent-speech-commands-in-ear.md) (2022). Earphone SSI senses ear-canal deformation with inaudible in-ear echoes to recognize silently mouthed commands; abstract reports 10.02% WER on 32 word commands and 12.33% on 25 sentence commands.
- [Poster: Recognizing Hidden-in-the-Ear Private Key for Reliable Silent Speech Interface Using Multi-Task Learning](poster-recognizing-hidden-in-the-ear-private-key-for-reliable-silent-speech-interface-using-mult.md) (2025). HEar-ID jointly recognizes whispered ear-canal letter spelling and user identity from in-ear audio and ultrasonic reflections; Top-1 word accuracy is 67.3% across 11 users (90.25% for eight selected users).
- [Silent Speech Sentence Recognition with Six-Axis Accelerometers using Conformer and CTC Algorithm](silent-speech-sentence-recognition-with-six-axis-accelerometers-using-conformer-and-ctc-algorith.md) (2025). Uses six wearable 6-axis IMUs (accelerometer plus gyroscope) on the face and neck with a Conformer-CTC model to recognize silently articulated words and word sequences. Reports 97.17% word-level accuracy in a 4-participant study.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
