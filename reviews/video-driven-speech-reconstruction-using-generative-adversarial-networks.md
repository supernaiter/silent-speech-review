# Video-Driven Speech Reconstruction using Generative Adversarial Networks

Konstantinos Vougioukas, Pingchuan Ma, Stavros Petridis, Maja Pantic  
arXiv / imported corpus page 2019 · [arXiv](https://arxiv.org/abs/1906.06301)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

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

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
