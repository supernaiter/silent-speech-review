# WESPER: Zero-shot and Realtime Whisper to Normal Voice Conversion for Whisper-based Speech Interactions

Jun Rekimoto  
Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (CHI '23), April 23--28, 2023 · [DOI](https://doi.org/10.1145/3544548.3580706) · [arXiv](https://arxiv.org/abs/2303.01639)

**Section:** [Acoustic, whisper & wearable motion sensors](../README.md#acoustic-whisper--wearable-motion-sensors) · **Review basis:** full_text

A structured review of *WESPER: Zero-shot and Realtime Whisper to Normal Voice Conversion for Whisper-based Speech Interactions* (Jun Rekimoto, Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (CHI '23), April 23--28, 2023) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

WESPER converts whispered speech to normal voice zero-shot and in real time without per-user paired data; conversion cuts Google ASR WER on wTIMIT whispers from 44.70 to 26.68.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Ordinary microphone (whispered speech) |
| Task | Whisper-to-normal voice conversion |
| Vocabulary | Not stated |
| Speaker | Speaker-independent |
| Session | Not stated |
| Online / offline | Online |
| Key result | WER 44.70 to 26.68 (CER 28.38 to 12.70) on wTIMIT whispers, Google ASR |

**Limitations.** Relies on whispered rather than truly silent speech and is evaluated on whisper datasets, not silent-speech benchmarks or broad public use.

## Full review

### In short

Strong whisper-conversion paper, but it remains whisper-based rather than truly silent SSI.

### Review

WESPER is strong on its own terms. The paper backs the important claims: common speech units reduce the whisper-normal mismatch, the non-autoregressive stack runs in real time, and recognition improves substantially after conversion. The boundary condition is scope, not evidence quality. This is adjacent to SSI because whispered speech still produces audible input, so it should not be sold as a full silent-speech result.

### Why it matters

The practical contribution is a low-friction whispered-speech conversion stack that can run in real time without per-user paired corpora.

### Prior state of the art

Whisper-to-normal conversion typically required paired whisper-normal corpora or speaker-dependent training, making discreet speech interfaces hard to deploy.

### What changed

WESPER removes the paired-data requirement by learning common speech units from unpaired whisper and normal speech.

### Position in the field

A strong adjacent paper on discreet speech interaction, but it sits next to SSI rather than inside fully silent speech.

### Practical value

Useful for privacy-preserving whispered interaction and accessibility, especially when a standard microphone is preferred over special sensors.

### Advanced

discreet_speech; real_time_conversion; speaker_independent_conversion

### Unresolved

Full-silence interaction and broader real-world robustness remain unresolved.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | whisper-to-normal speech conversion |
| Input | whispered speech from an ordinary microphone |
| Sensor | ordinary microphone |
| Output | speech-audio |
| Metrics and results | On wTIMIT whispers, Google ASR reports WER 44.70 and CER 28.38, while WESPER-converted whispers improve to WER 26.68 and CER 12.70; the HuBERT-base setup pretrained on Librispeech+wTIMIT reaches WER 13.75 and CER 5.47. |
| Evaluation protocol | MOS, MUSHRA, and speech-recognition evaluation on whispered and converted speech |

### Limits

- **Technical:** The method still depends on whispered speech rather than truly silent articulation.
- **Evaluation:** The core evidence is on whispered conversion datasets and listening studies, not on silent-speech benchmarks.
- **Deployment:** Although real time is shown, the paper does not establish a full silent interface or broad public-use robustness.
- **Scope of this review:** Whisper-to-normal conversion only; this is not fully silent speech.

### Evidence

- The abstract says WESPER is a zero-shot real-time whisper-to-normal conversion mechanism built from a speech-to-unit encoder and a unit-to-speech decoder. (ABSTRACT)
- The introduction states that the encoder and decoder operate in a non-autoregressive manner so the entire system works in real time and does not need per-user training. (1    INTRODUCTION)
- Table 2 shows Google ASR on whispered wTIMIT at WER 44.70/CER 28.38, while WESPER-converted whispers improve to WER 26.68/CER 12.70; the HuBERT-base setup pretrained on Librispeech+wTIMIT reaches WER 13.75/CER 5.47. (Table 2)
- The introduction explicitly motivates the work with whispered speech, not fully silent articulation, because ordinary microphones can capture whispers whereas silent speech systems often need special sensors. (1    INTRODUCTION)

## More reviews in Acoustic, whisper & wearable motion sensors

- [EchoSpeech: Continuous Silent Speech Recognition on Minimally-obtrusive Eyewear Powered by Acoustic Sensing](echospeech-continuous-silent-speech-recognition-on-minimally-obtrusive-eyewear-powered-by-acoustic.md) (2023). Glasses-mounted inaudible FMCW sonar recognizes silent speech from facial skin echoes: 4.5% WER on 31 commands and 6.1% on connected digits in 12 users, with walking/noise tests and a 73.3 mW demo.
- [Ultrasensitive Textile Strain Sensors Redefine Wearable Silent Speech Interfaces with High Machine Learning Efficiency](ultrasensitive-textile-strain-sensors-redefine-wearable-silent-speech-interfaces-with-high-machine-learning-efficiency.md) (2023). Combines an ultrasensitive graphene textile strain sensor in a throat choker with a lightweight 1D residual CNN to classify silent words. Reports 95.25% accuracy on 20 words and 90% few-shot transfer with 30 samples per class.
- [Unvoiced: Designing an LLM-assisted Unvoiced User Interface using Earables](unvoiced-designing-an-llm-assisted-unvoiced-user-interface-using-earables.md) (2024). Twin-IMU earable captures jaw motion during unvoiced speech; spectrograms are transcribed by Whisper and gaps filled by GPT-4, giving 93-99% task completion and 0.07-0.14 WER across 19 users.
- [EarCommand: "Hearing" Your Silent Speech Commands In Ear](earcommand-hearing-your-silent-speech-commands-in-ear.md) (2022). Earphone SSI senses ear-canal deformation with inaudible in-ear echoes to recognize silently mouthed commands; abstract reports 10.02% WER on 32 word commands and 12.33% on 25 sentence commands.
- [Poster: Recognizing Hidden-in-the-Ear Private Key for Reliable Silent Speech Interface Using Multi-Task Learning](poster-recognizing-hidden-in-the-ear-private-key-for-reliable-silent-speech-interface-using-mult.md) (2025). HEar-ID jointly recognizes whispered ear-canal letter spelling and user identity from in-ear audio and ultrasonic reflections; Top-1 word accuracy is 67.3% across 11 users (90.25% for eight selected users).
- [Silent Speech Sentence Recognition with Six-Axis Accelerometers using Conformer and CTC Algorithm](silent-speech-sentence-recognition-with-six-axis-accelerometers-using-conformer-and-ctc-algorith.md) (2025). Uses six wearable 6-axis IMUs (accelerometer plus gyroscope) on the face and neck with a Conformer-CTC model to recognize silently articulated words and word sequences. Reports 97.17% word-level accuracy in a 4-participant study.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
