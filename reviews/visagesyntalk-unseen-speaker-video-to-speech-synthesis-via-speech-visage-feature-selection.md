# VisageSynTalk: Unseen Speaker Video-to-Speech Synthesis via Speech-Visage Feature Selection

Joanna Hong, Minsu Kim, Yong Man Ro  
arXiv / imported corpus page 2022 · [arXiv](https://arxiv.org/abs/2206.07458)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

VisageSynTalk disentangles speech content and visage (identity) features for video-to-speech synthesis, yielding robust results for unseen speakers on benchmarks.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Talking-face video |
| Task | Speech synthesis from face video |
| Vocabulary | Not stated |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Not reported |

**Limitations.** Offline benchmarks only with a small MOS study (20 GRID samples, 16 raters); needs clean aligned video, no robustness to pose or occlusion.

## Full review

### In short

The paper is really about disentangling identity, and that is why the unseen-speaker results hold up.

### Review

The paper presents a novel disentanglement-based approach for video-to-speech synthesis that separates speech content and speaker identity from silent talking-face video using multi-head speech-visage feature selection masks, and synthesizes speech conditioned on these disentangled features. Evaluated on three datasets (GRID, TCD-TIMIT, LRW), the method achieves state-of-the-art objective metrics (STOI, ESTOI, PESQ) on unseen speakers with multi-speaker independent splits, as well as highest subjective MOS scores for naturalness, intelligibility, and voice matching. Ablations confirm the importance of the disentanglement and the multi-head mask design. Speaker verification analysis via EER demonstrates effective separation of identity and content features. Limitations include reliance on aligned, controlled videos, lack of real-time or in-the-wild evaluation, and relatively modest speech quality compared to natural voices. Nonetheless, the work meaningfully advances unseen-speaker video-to-speech robustness via representation learning rather than larger datasets or enrollment procedures.

### Why it matters

The paper matters because the content-style split is operational, not decorative: it beats prior video-to-speech systems on unseen-speaker GRID and TCD-TIMIT and scales to LRW with a principled feature selection and visage-style conditioned synthesizer architecture.

### Prior state of the art

Lip-to-speech systems improved waveform quality, but most treated face video as a single entangled signal and were weak on unseen speakers.

### What changed

Makes identity disentanglement explicit through speech-visage feature selection and a visage-style conditioned synthesizer.

### Position in the field

Strong video-to-speech synthesis paper focused on unseen-speaker generalization rather than core SSI hardware.

### Practical value

Useful when face-video synthesis must generalize beyond training identities without a speaker-specific enrollment pipeline.

### Advanced

system design; evaluation; speaker generalization

### Unresolved

in-the-wild robustness; real-time inference; noisy capture conditions

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | video |
| Body site | face |
| Output | speech-audio |
| Metrics and results | STOI, ESTOI, PESQ; MOS naturalness, intelligibility, and voice matching; Equal Error Rate (EER) for speaker verification of disentangled features. |
| Evaluation protocol | Multi-speaker independent and dependent benchmark evaluation plus MOS for naturalness, intelligibility, and voice matching; disentanglement validated via speaker verification EER. |

### Limits

- **Technical:** Even best scores fall short of natural speech; requires clean, aligned talking-face videos; no demonstrated robustness to occlusion or pose variation.
- **Evaluation:** Offline benchmark evaluations only; MOS study limited to 20 GRID samples rated by 16 participants; no in-the-wild tests.
- **Deployment:** No evaluation under camera noise, varying head poses, or real-time inference; limited to aligned, controlled talking-face video.
- **Scope of this review:** Talking-face speech synthesis for unseen speakers with benchmark datasets; no broader SSI application beyond video-to-speech synthesis is addressed.

### Evidence

- Disentangles speech content and visage style from silent talking-face video to synthesize speech for unseen speakers. (Abstract)
- The model explicitly separates speech-content features from identity-style features before synthesis using multi-head speech-visage feature selection masks. (3.1 Speech-visage feature selection)
- On unseen-speaker GRID, the proposed model reaches STOI 0.567, ESTOI 0.308, and PESQ 1.373, improving on End-to-end GAN and VV-Memory. On unseen-speaker TCD-TIMIT it reaches 0.478, 0.217, and 1.410. MOS naturalness 2.96, intelligibility 3.35, voice matching 3.34 on GRID dataset with 20 samples rated by 16 participants. (4.3 Experimental results)
- Evaluated on GRID corpus, TCD-TIMIT volunteer, and LRW datasets with multi-speaker independent and dependent settings; unseen speaker splits are employed; LRW contains 17,580 clustered speaker identities. (4 Experiments)
- Best achievable speech quality remains far from natural speech; method depends on high quality talking-face video aligned and cropped; no in-the-wild or real-time study; MOS ratings based on only 20 GRID samples rated by 16 participants. (4.3 Experimental results)
- No evaluation or discussion of deployment under realistic capture conditions such as camera noise, head pose drift, or occlusion; no latency or live interactive system reported. (4.3 Experimental results)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
