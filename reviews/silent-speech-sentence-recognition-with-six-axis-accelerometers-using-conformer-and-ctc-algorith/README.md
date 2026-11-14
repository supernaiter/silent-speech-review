# Silent Speech Sentence Recognition with Six-Axis Accelerometers using Conformer and CTC Algorithm

Yudong Xie, Zhifeng Han, Qinfan Xiao, Liwei Liang, Lu-Qi Tao, Tian-Ling Ren  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2502.17829)

**Section:** [Acoustic, whisper & wearable motion sensors](../../README.md#acoustic-whisper--wearable-motion-sensors) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *Silent Speech Sentence Recognition with Six-Axis Accelerometers using Conformer and CTC Algorithm* (Yudong Xie et al., arXiv 2025) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Uses six wearable 6-axis IMUs (accelerometer plus gyroscope) on the face and neck with a Conformer-CTC model to recognize silently articulated words and word sequences. Reports 97.17% word-level accuracy in a 4-participant study.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Six 6-axis MEMS IMUs on face and neck |
| Task | Silent word and sentence recognition |
| Vocabulary | 16 English words, 2 English sentences, 8 Mandarin phrases |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 97.17% word-level accuracy (correct words / total words), 4 participants; not sentence-level accuracy |

**Limitations.** Only 4 participants and a small closed vocabulary; accuracy drops for unseen users and some stay below 90% after few-shot calibration; real-time use, other days and re-wearing are untested.


## More reviews in Acoustic, whisper & wearable motion sensors

- [Poster: Recognizing Hidden-in-the-Ear Private Key for Reliable Silent Speech Interface Using Multi-Task Learning](../poster-recognizing-hidden-in-the-ear-private-key-for-reliable-silent-speech-interface-using-mult/) (2025). HEar-ID jointly recognizes whispered ear-canal letter spelling and user identity from in-ear audio and ultrasonic reflections; Top-1 word accuracy is 67.3% across 11 users (90.25% for eight selected users).
- [NasoVoce: A Nose-Mounted Low-Audibility Speech Interface for Always-Available Speech Interaction](../nasovoce/) (2026). NasoVoce, nose-pad microphone and vibration sensor on smart glasses, with multimodal fusion for low-audibility and whispered speech interaction under noise, evaluated by ASR error rates and audio quality.
- [SoniSpeech: A Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces](../sonispeech-a-large-scale-open-vocabulary-tri-modal-dataset-for-wearable-silent-speech-interfaces/) (2026). Single-speaker open-vocabulary dataset (ultrasound echoes, audio, video) from eyeglass-mounted sensors; an echo-only baseline trained on mixed voiced/silent data reaches 26.3% WER on silent speech.
- [Unvoiced: Designing an LLM-assisted Unvoiced User Interface using Earables](../unvoiced-designing-an-llm-assisted-unvoiced-user-interface-using-earables/) (2024). Twin-IMU earable captures jaw motion during unvoiced speech; spectrograms are transcribed by Whisper and gaps filled by GPT-4, giving 93-99% task completion and 0.07-0.14 WER across 19 users.
- [EchoSpeech: Continuous Silent Speech Recognition on Minimally-obtrusive Eyewear Powered by Acoustic Sensing](../echospeech-continuous-silent-speech-recognition-on-minimally-obtrusive-eyewear-powered-by-acoustic/) (2023). Glasses-mounted inaudible FMCW sonar recognizes silent speech from facial skin echoes: 4.5% WER on 31 commands and 6.1% on connected digits in 12 users, with walking/noise tests and a 73.3 mW demo.
- [Ultrasensitive Textile Strain Sensors Redefine Wearable Silent Speech Interfaces with High Machine Learning Efficiency](../ultrasensitive-textile-strain-sensors-redefine-wearable-silent-speech-interfaces-with-high-machine-learning-efficiency/) (2023). Combines an ultrasensitive graphene textile strain sensor in a throat choker with a lightweight 1D residual CNN to classify silent words. Reports 95.25% accuracy on 20 words and 90% few-shot transfer with 30 samples per class.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
