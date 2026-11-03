# EarCommand: "Hearing" Your Silent Speech Commands In Ear

Yincheng Jin, Yang Gao, Xuhai Xu, Seokmin Choi, Jiyang Li, Feng Liu, Zhengxiong Li, Zhanpeng Jin  
Proc. ACM IMWUT 6(2), Article 57 2022 · [DOI](https://doi.org/10.1145/3534613)

**Section:** [Acoustic, whisper & wearable motion sensors](../README.md#acoustic-whisper--wearable-motion-sensors) · **Review basis:** abstract+secondary_sources

A structured review of *EarCommand: "Hearing" Your Silent Speech Commands In Ear* (Yincheng Jin et al., Proc. ACM IMWUT 6(2), Article 57 2022) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Earphone SSI senses ear-canal deformation with inaudible in-ear echoes to recognize silently mouthed commands; abstract reports 10.02% WER on 32 word commands and 12.33% on 25 sentence commands.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Earbud with inward-facing speaker and microphone (near-ultrasound echoes in ear canal) |
| Task | Silent command recognition |
| Vocabulary | 32 word-level and 25 sentence-level commands |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Not stated |
| Key result | WER 10.02% (word commands), 12.33% (sentence commands) |

**Limitations.** Reviewed from abstract and press only; closed command sets; participant count and calibration details unverified.

## Full review

### In short

Earphone-based SSI that infers silent commands from ear-canal deformation sensed with inaudible in-ear echoes; abstract reports 10.02% WER on 32 word-level and 12.33% on 25 sentence-level commands.

### Review

EarCommand is an early, widely cited earable SSI: an inward-facing speaker emits near-ultrasound signals into the ear canal and an inward-facing microphone captures echoes, from which ear-canal deformation caused by articulator movement during silent mouthing is mapped to commands. Its appeal for SSI is form factor: no camera, no skin electrodes, hands-free, and hardware close to commodity earbuds. The abstract reports a WER of 10.02% for 32 word-level commands and 12.33% for 25 sentence-level commands, and claims robustness across configurations and environmental conditions; press coverage mentions use with masks and in noise but gives no figures. Because the full text (ACM DL) could not be accessed, this review cannot verify the number of participants, user-dependence of training, session/remount handling, signal frequencies, model architecture or how the robustness tests were quantified. As stated, the vocabulary is a closed command set, so the result speaks to command recognition rather than open-vocabulary silent speech. Treat the numbers as author-reported headline results pending full-text review.

### Why it matters

Shows that ear-canal deformation sensed acoustically from an earbud carries enough articulatory information for closed-set silent command recognition, opening the earable SSI direction.

### Prior state of the art

Wearable SSIs mostly used skin-contact EMG, cameras or sensors near the mouth; earable sensing of speech-related ear-canal deformation was not established for silent command recognition.

### What changed

Introduces in-ear acoustic sensing of ear-canal deformation as the input modality for silent word- and sentence-level commands.

### Position in the field

Representative earable acoustic SSI in the acoustic section; precursor to later earable silent speech work.

### Practical value

Attractive form factor for private, hands-free command input on earbuds; practical accuracy and calibration burden unverified here.

### Advanced

Form factor (earphone, no camera or electrodes); new sensing locus (ear canal).

### Unresolved

Open vocabulary; cross-user generalization; calibration burden; real-time on-device operation; long-term fit variation (not verifiable from abstract).

### Evaluation details

| Item | Details |
| --- | --- |
| Task | Recognition of silently mouthed word-level and sentence-level commands from in-ear acoustic sensing. |
| Input | Active acoustic (near-ultrasound) echoes in the ear canal reflecting ear-canal deformation. |
| Sensor | Earbud-style device with inward-facing speaker emitting inaudible near-ultrasound signals and inward-facing microphone (per press coverage); exact specifications not verified. |
| Body site | Ear canal (skin of the external auditory canal). |
| Output | Command labels. |
| Vocabulary type | Closed command sets (word-level and sentence-level). |
| Vocabulary size | 32 word-level commands; 25 sentence-level commands. |
| Metrics and results | WER 10.02% (32 word-level commands) and 12.33% (25 sentence-level commands), per abstract. |
| Evaluation protocol | Human-subject evaluation described in abstract; protocol details not verified. |

### Limits

- **Technical:** Closed command sets only; technical details (frequencies, model, training regime) not verified because full text was not accessed.
- **Evaluation:** Only abstract-level WERs available; number of participants, splits and robustness conditions unverified. Press coverage reports rounded values (10.2%/12.3%) that differ slightly from the abstract (10.02%/12.33%).
- **Deployment:** Prototype earbud with a linked computer per press coverage; on-device performance, latency and power not verified.
- **Scope of this review:** Abstract (via ECNU research portal) and secondary press coverage (New Atlas) only; ACM full text not accessible from this environment. All non-abstract details are unverified. Chosen as the wearable/earable SSI because it is a widely cited 2022 IMWUT earable silent speech paper and was not yet in the dataset (EchoSpeech and Unvoiced had already been added).

### Evidence

- EarCommand is an earphone-based, hands-free silent speech system that exploits the relationship between ear canal deformation and articulator movement to recognize silent commands. (Abstract)
- The abstract reports 10.02% WER for 32 word-level commands and 12.33% WER for 25 sentence-level commands. (Abstract)
- The authors claim the system remains reliable and robust across various configurations and environmental conditions; no numbers were available to this review. (Abstract)
- Press coverage describes an inward-facing speaker emitting inaudible near-ultrasound signals and an inward-facing microphone capturing ear-canal echoes, processed on a linked computer. (New Atlas article on EarCommand)
- Only closed command vocabularies are reported; participant count, user-dependence and protocol details could not be verified without the full text. (Abstract; review scope)

## More reviews in Acoustic, whisper & wearable motion sensors

- [EchoSpeech: Continuous Silent Speech Recognition on Minimally-obtrusive Eyewear Powered by Acoustic Sensing](echospeech-continuous-silent-speech-recognition-on-minimally-obtrusive-eyewear-powered-by-acoustic.md) (2023). Glasses-mounted inaudible FMCW sonar recognizes silent speech from facial skin echoes: 4.5% WER on 31 commands and 6.1% on connected digits in 12 users, with walking/noise tests and a 73.3 mW demo.
- [Ultrasensitive Textile Strain Sensors Redefine Wearable Silent Speech Interfaces with High Machine Learning Efficiency](ultrasensitive-textile-strain-sensors-redefine-wearable-silent-speech-interfaces-with-high-machine-learning-efficiency.md) (2023). Combines an ultrasensitive graphene textile strain sensor in a throat choker with a lightweight 1D residual CNN to classify silent words. Reports 95.25% accuracy on 20 words and 90% few-shot transfer with 30 samples per class.
- [WESPER: Zero-shot and Realtime Whisper to Normal Voice Conversion for Whisper-based Speech Interactions](wesper-zero-shot-and-realtime-whisper-to-normal-voice-conversion-for-whisper-based-speech-interactions.md) (2023). WESPER converts whispered speech to normal voice zero-shot and in real time without per-user paired data; conversion cuts Google ASR WER on wTIMIT whispers from 44.70 to 26.68.
- [Unvoiced: Designing an LLM-assisted Unvoiced User Interface using Earables](unvoiced-designing-an-llm-assisted-unvoiced-user-interface-using-earables.md) (2024). Twin-IMU earable captures jaw motion during unvoiced speech; spectrograms are transcribed by Whisper and gaps filled by GPT-4, giving 93-99% task completion and 0.07-0.14 WER across 19 users.
- [End-to-end Silent Speech Recognition with Acoustic Sensing](end-to-end-silent-speech-recognition-with-acoustic-sensing.md) (2020). Silent speech recognition from lip movements using smartphone speaker and microphone active acoustic sensing; reaches 8.4% average WER domain-independent and 8.1% on unseen sentences within a 54-sentence corpus.
- [Poster: Recognizing Hidden-in-the-Ear Private Key for Reliable Silent Speech Interface Using Multi-Task Learning](poster-recognizing-hidden-in-the-ear-private-key-for-reliable-silent-speech-interface-using-mult.md) (2025). HEar-ID jointly recognizes whispered ear-canal letter spelling and user identity from in-ear audio and ultrasonic reflections; Top-1 word accuracy is 67.3% across 11 users (90.25% for eight selected users).

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
