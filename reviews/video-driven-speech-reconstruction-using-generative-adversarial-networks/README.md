# Video-Driven Speech Reconstruction using Generative Adversarial Networks

Konstantinos Vougioukas, Pingchuan Ma, Stavros Petridis, Maja Pantic  
arXiv 2019 · [arXiv](https://arxiv.org/abs/1906.06301)

**Section:** [Lip & face video](../../README.md#lip--face-video) · **Review basis:** full_text

A structured review of *Video-Driven Speech Reconstruction using Generative Adversarial Networks* (Konstantinos Vougioukas et al., arXiv 2019) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Uses a GAN to generate speech audio directly from silent frontal face video on GRID; speaker-dependent WER is 26.6%, while unseen speakers degrade to 40.5% WER.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera (silent frontal face video) |
| Task | Speech synthesis from silent video |
| Vocabulary | GRID corpus |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Speaker-dependent WER 26.6%, STOI 0.518; unseen speakers WER 40.5%, PESQ 1.24 |

**Limitations.** GRID-only evaluation, frontal faces only, audible artifacts and poor voice consistency for unseen speakers; in-the-wild use is future work.

## Full review

### In short

Foundational direct video-to-audio result with clear generalization limits.

### Review

The full text justifies why this paper matters: it pushes past intermediate-feature pipelines and gets to direct raw-audio generation with intelligible outputs on GRID. Table 2 shows a meaningful intelligibility win over Lip2AudSpec even though PESQ is slightly worse, and the ablation study makes clear the perceptual and adversarial losses are doing real work. The same text also keeps the review honest: unseen speakers degrade sharply, voice identity can morph, and the method only handles frontal faces.

### Why it matters

A foundational lip-to-speech paper because it demonstrates intelligible direct audio generation from silent video, but the unseen-speaker degradation is substantial and the method is frontal-view only.

### Prior state of the art

Earlier video-to-speech pipelines often relied on intermediate speech features or text and were mostly speaker-dependent.

### What changed

This model learns direct silent-video to raw-audio synthesis with GAN and perceptual losses and evaluates both seen and unseen speakers.

### Position in the field

Core early video-driven speech reconstruction work.

### Practical value

Useful as a historically important baseline for direct video-to-audio synthesis.

### Advanced

direct_audio_generation; lip_to_speech; synchrony

### Unresolved

unseen-speaker fidelity, broader visual conditions, and natural voice quality remain unresolved.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | silent frontal face video |
| Sensor | camera |
| Body site | face; lip |
| Output | speech-audio |
| Metrics and results | In the speaker-dependent setup the model reports WER 26.6%, STOI 0.518, MCD 22.29, and AV confidence 4.4 with one-frame offset; unseen speakers drop to WER 40.5% and PESQ 1.24. |
| Evaluation protocol | GRID speaker-dependent and speaker-independent evaluation using PESQ, WER, AV synchrony, STOI, and MCD plus ablations |

### Limits

- **Technical:** Artifacts remain, unseen-speaker voice consistency is poor, and the model is restricted to frontal faces.
- **Evaluation:** All reported experiments are on GRID, which constrains linguistic and visual diversity.
- **Deployment:** In-the-wild pose variation and real-world deployment are future work.
- **Scope of this review:** Frontal silent-video speech reconstruction only.

### Evidence

- The abstract says the model directly synthesizes audio from silent video and evaluates both speaker-dependent and speaker-independent scenarios on GRID. (Abstract)
- Table 2 reports speaker-dependent WER 26.6%, STOI 0.518, MCD 22.29, and AV confidence 4.4 with one-frame offset for the proposed model. (Table 2)
- The ablation study says the adversarial loss is necessary for speech production and the perceptual loss is critical for preserving content. (Table 3)
- The conclusion says unseen speakers still produce degraded voices and that the method operates solely on frontal faces, leaving in-the-wild video as future work. (5           Conclusions)

## More reviews in Lip & face video

- [Lipper: Synthesizing Thy Speech using Multi-View Lipreading](../lipper-synthesizing-thy-speech-using-multi-view-lipreading/) (2019). Lipper reconstructs speech from multi-view lip video on OuluVS2 as a regression problem; the best three-view setting reaches PESQ 2.315 with 0.169 s end-to-end delay, though audio remains robotic.
- [Speech Prediction in Silent Videos using Variational Autoencoders](../speech-prediction-in-silent-videos-using-variational-autoencoders/) (2020). Variational autoencoder model for speech synthesis from silent lip video that models one-to-many ambiguity; on GRID reports STOI 0.724, ESTOI 0.540 and PESQ 1.932, leading Lip2Wav on ESTOI and PESQ.
- [Vocoder-Based Speech Synthesis from Silent Videos](../vocoder-based-speech-synthesis-from-silent-videos/) (2020). Predicts full vocoder features from silent face video with joint visual speech recognition training on GRID; speaker-dependent model reaches PESQ 1.90 and WER 15.1%, but speaker-independent performance drops sharply.
- [Deep Audio-Visual Speech Recognition](../deep-audio-visual-speech-recognition/) (2018). Landmark AVSR paper that releases LRS2-BBC and compares CTC and sequence-to-sequence Transformers on one shared encoder. Video-only TM-seq2seq reaches 48.3% WER with an LM (49.8% without; the 70.4% WAS baseline has no stated decoding conditions, and the same group's Transformer three months earlier already reached 50.0%). CTC and seq2seq differ little once an LM or audio is added.
- [Harnessing AI for Speech Reconstruction using Multi-view Silent Video Feed](../harnessing-ai-for-speech-reconstruction-using-multi-view-silent-video-feed/) (2018). Reconstructs speech audio from multi-view silent video on OuluVS2 with CNN-LSTM models, showing multi-view input improves PESQ over single view and that camera placement matters.
- [Visual-Only Recognition of Normal, Whispered and Silent Speech](../visual-only-recognition-of-normal-whispered-and-silent-speech/) (2018). Compares visual-only recognition of normal, whispered and silent speech, showing silent speech is a distinct regime: matched-condition silent accuracy is 62.2% (digits) and training on normal speech lowers it further.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
