# Lipper: Synthesizing Thy Speech using Multi-View Lipreading

Yaman Kumar, Rohit Jain, Khwaja Mohd. Salik, Rajiv Ratn Shah, Yifang Yin, Roger Zimmermann  
arXiv 2019 · [arXiv](https://arxiv.org/abs/1907.01367)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

A structured review of *Lipper: Synthesizing Thy Speech using Multi-View Lipreading* (Yaman Kumar et al., arXiv 2019) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Lipper reconstructs speech from multi-view lip video on OuluVS2 as a regression problem; the best three-view setting reaches PESQ 2.315 with 0.169 s end-to-end delay, though audio remains robotic.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Multi-view cameras (lip video) |
| Task | Speech synthesis from multi-view lip video |
| Vocabulary | OuluVS2 phrases, including OOV phrase tests |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Both |
| Key result | PESQ 2.315 (0 deg+45 deg+60 deg views), 0.169 s delay; user study 80.25% audio-only accuracy |

**Limitations.** Robotic audio, lips alone cannot recover prosody, controlled OuluVS2 conditions only, and weak speaker-independent results.

## Full review

### In short

Strong multi-view lip-to-speech baseline with honest quality limits.

### Review

The full text gives Lipper more credit than a quick skim would. The best three-view configuration at 0°, 45°, and 60° materially beats the single-view setups, and Table 11 shows why the authors can plausibly call it near real-time: 0.169 s versus roughly 0.94 to 1.95 s for the speechreading comparison. But the conclusion is equally important, because it openly admits robotic audio, controlled-camera assumptions, and weak speaker-independent behavior. This is a strong baseline, not a solved deployment story.

### Why it matters

A serious early multi-view video-to-speech system whose importance is the regression framing and practical latency analysis, though audio quality remains robotic and speaker independence is weak.

### Prior state of the art

Most lipreading systems classified phrases or words rather than synthesizing speech directly, and usually from a single view.

### What changed

Lipper combines multiple camera views, regression-based speech reconstruction, OOV testing, and explicit delay analysis.

### Position in the field

Core multi-view video speech-reconstruction work in SSI-adjacent silent video research.

### Practical value

Useful as a baseline for multi-view lip-to-speech systems, especially when latency and OOV behavior matter.

### Advanced

multi_view_fusion; regression_framing; latency

### Unresolved

speaker independence, naturalness, and in-the-wild robustness remain unresolved.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | multi-view lip video |
| Sensor | camera |
| Body site | face; lip |
| Output | speech-audio |
| Metrics and results | Best three-view setting 0°+45°+60° reaches PESQ 2.315, end-to-end delay stays at 0.169 s across phrases, and user-study accuracy is 80.25% audio-only / 81.25% audio-visual. |
| Evaluation protocol | speaker-dependent and speaker-independent OuluVS2 PESQ benchmarks, OOV phrase tests, delay comparison, and user study |

### Limits

- **Technical:** The generated audio is still robotic and lip-only sensing cannot recover prosody or full vocal tract information.
- **Evaluation:** The work is confined to controlled OuluVS2 conditions and speaker-independent results remain weak.
- **Deployment:** Real-world pose variation and broader speaker coverage are not solved.
- **Scope of this review:** Multi-view lip-video speech reconstruction only.

### Evidence

- The abstract says Lipper reconstructs speech from silent multi-view videos by treating lipreading as a regression task rather than classification. (Abstract)
- Table 6 reports the best three-view combination at 0°+45°+60° with PESQ 2.315, higher than any single-view result in Table 4. (Table 6)
- Table 11 shows Lipper at 0.169 seconds delay across phrases, substantially below the 0.94 to 1.95 second delays of the speechreading comparison. (Table 11)
- The conclusion says the audio remains robotic, the system assumes controlled camera conditions, and speaker-independent performance is not good enough for deployment. (Conclusion)

## More reviews in Lip & face video

- [Video-Driven Speech Reconstruction using Generative Adversarial Networks](video-driven-speech-reconstruction-using-generative-adversarial-networks.md) (2019). Uses a GAN to generate speech audio directly from silent frontal face video on GRID; speaker-dependent WER is 26.6%, while unseen speakers degrade to 40.5% WER.
- [Speech Prediction in Silent Videos using Variational Autoencoders](speech-prediction-in-silent-videos-using-variational-autoencoders.md) (2020). Variational autoencoder model for speech synthesis from silent lip video that models one-to-many ambiguity; on GRID reports STOI 0.724, ESTOI 0.540 and PESQ 1.932, leading Lip2Wav on ESTOI and PESQ.
- [Vocoder-Based Speech Synthesis from Silent Videos](vocoder-based-speech-synthesis-from-silent-videos.md) (2020). Predicts full vocoder features from silent face video with joint visual speech recognition training on GRID; speaker-dependent model reaches PESQ 1.90 and WER 15.1%, but speaker-independent performance drops sharply.
- [Deep Audio-Visual Speech Recognition](deep-audio-visual-speech-recognition.md) (2018). Landmark AVSR paper that releases LRS2-BBC and compares CTC and sequence-to-sequence Transformers on one shared encoder. Video-only TM-seq2seq reaches 48.3% WER with an LM (49.8% without; the 70.4% WAS baseline has no stated decoding conditions, and the same group's Transformer three months earlier already reached 50.0%). CTC and seq2seq differ little once an LM or audio is added.
- [Harnessing AI for Speech Reconstruction using Multi-view Silent Video Feed](harnessing-ai-for-speech-reconstruction-using-multi-view-silent-video-feed.md) (2018). Reconstructs speech audio from multi-view silent video on OuluVS2 with CNN-LSTM models, showing multi-view input improves PESQ over single view and that camera placement matters.
- [Visual-Only Recognition of Normal, Whispered and Silent Speech](visual-only-recognition-of-normal-whispered-and-silent-speech.md) (2018). Compares visual-only recognition of normal, whispered and silent speech, showing silent speech is a distinct regime: matched-condition silent accuracy is 62.2% (digits) and training on normal speech lowers it further.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
