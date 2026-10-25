# VisualTTS: TTS with Accurate Lip-Speech Synchronization for Automatic Voice Over

Junchen Lu, Berrak Sisman, Rui Liu, Mingyang Zhang, Haizhou Li  
arXiv / imported corpus page 2022 · [arXiv](https://arxiv.org/abs/2110.03342)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

VisualTTS conditions TTS on silent lip video to improve lip-speech synchronization for automatic voice-over, evaluated on the scripted GRID corpus.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Mono video camera (lip region) plus text script |
| Task | Automatic voice-over (lip-synced TTS) |
| Vocabulary | GRID fixed-grammar sentences, 33 speakers |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | LSE-C 5.87, LSE-D 8.45, MOS 4.17 on GRID test set |

**Limitations.** Restricted to scripted GRID data with paired text; no unseen speakers, spontaneous speech, or real-time tests; does not decode silent speech.

## Full review

### In short

VisualTTS effectively improves lip-speech synchronization in scripted voice over by conditioning TTS on lip video, but does not tackle silent speech decoding or unscripted scenarios.

### Review

VisualTTS presents an audio-visual multi-speaker neural TTS system conditioned on both text and lip video inputs to synthesize speech synchronizing accurately with lip motions. Key innovations include textual-visual attention that aligns textual embeddings with visual lip embeddings extracted by a pretrained lip-reading model, and a visual fusion strategy that incorporates temporal visual features into the acoustic decoder. Experiments on the constrained GRID dataset show significant improvements in lip-speech synchronization metrics (LSE-C, LSE-D, frame disturbance) compared to Tacotron baselines, including one with textual-visual attention but without fusion. Subjective listening tests show no improvement in speech naturalness, indicating VisualTTS primarily enhances audiovisual synchrony. Limitations include reliance on scripted video-text input pairs, fixed vocabulary and speaker identities, and no demonstration of real-time synthesis or generalization. The work constitutes a meaningful contribution for dubbing and automated voice over applications but does not address silent speech recognition or free speaking SSI tasks, positioning it adjacent to but not core within silent speech interfaces.

### Why it matters

Demonstrates that integrating lip-video visual embeddings via novel textual-visual attention and visual fusion within TTS measurably improves audiovisual synchronization, advancing automatic voice over technology.

### Prior state of the art

Traditional TTS systems synthesize speech from text input without considering lip video or lip-speech temporal synchronization, often generating natural but temporally unsynchronized speech.

### What changed

Unlike canonical single-modal TTS, VisualTTS integrates lip motion visual embeddings at alignment and acoustic decoding stages to optimize speech output timing to synchronize with video lip motion.

### Position in the field

A specialized audiovisual synchronization-enhanced TTS related but not core to silent speech interfaces; does not decode speech from silent video without text input.

### Practical value

Valuable for automatic voice over and dubbing applications with available scripted silent videos; improves perceived audiovisual synchrony without compromising naturalness.

### Advanced

system_design; evaluation

### Unresolved

The system requires both text script and lip video as input; it does not address decoding from video-only silent speech or speaker adaptation to unseen speakers.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | automatic voice over with lip-speech synchronization |
| Input | Text script plus silent lip video from a mono camera capturing lip region. |
| Sensor | Mono video camera capturing lip region from video frames. |
| Body site | lip |
| Output | speech-audio |
| Vocabulary type | Executing fixed grammar scripted sentences from predefined GRID dataset. |
| Vocabulary size | 33,000 utterances from GRID corpus spanning 33 speakers with fixed sentence grammar. |
| Metrics and results | LSE-C (higher better): 5.87; LSE-D (lower better): 8.45; Frame Disturbance (lower better): 5.92; MOS: 4.17±0.06 on GRID test set averaged across 33 speakers, comparing favorably in lip-speech synchronization to baselines. |
| Evaluation protocol | Objective lip-speech synchronization metrics (LSE-C, LSE-D, Frame Disturbance) and subjective listening tests including MOS and preference tests on synthetic speech paired with test videos. |

### Limits

- **Technical:** Requires paired text scripts aligned with video; training and evaluation restricted to fixed grammar GRID corpus; visual encoder weights fixed during TTS training; no speaker-independent or vocabulary adaptation shown.
- **Evaluation:** Evaluation restricted to the scripted GRID dataset; no tests on spontaneous speech, large-vocabulary, unseen speakers, or real-time synthesis; subjective voice quality comparable to baselines with no improvement.
- **Deployment:** Requires pre-recorded silent lip video and matching text script; limited to scripted GRID dataset utterances; unknown real-time capability; fixed speaker set and vocabulary; no adaptation to unseen speakers or spontaneous speech.
- **Scope of this review:** Limited to GRID dataset scripted utterances with paired silent video and text; no demonstration on spontaneous or unconstrained speech or unseen speakers.

### Evidence

- The paper formulates the automatic voice over (AVO) task and proposes VisualTTS, a visual-conditioned TTS model with textual-visual attention and visual fusion strategies for accurate lip-speech synchronization. (ABSTRACT)
- VisualTTS adopts two novel mechanisms: 1) textual-visual attention (TVA) aligning textual and visual embeddings for alignment, and 2) visual fusion strategy during acoustic decoding to incorporate visual embeddings into mel-spectrogram generation, improving lip-speech synchronization. (3. VISUALTTS)
- Experiments conducted on the GRID dataset with 33 speakers, 900 training and 100 test utterances each, use 24kHz audio and 25Hz video with lip region cropping. (4. EXPERIMENTS)
- Lip-speech synchronization is evaluated with LSE-C (higher better), LSE-D (lower better), and Frame Disturbance (FD, lower better). VisualTTS achieves LSE-C 5.87, LSE-D 8.45, FD 5.92, outperforming baselines Tacotron and Tacotron with TVA. (4. EXPERIMENTS)
- Subjective listening tests with 12 listeners show VisualTTS has comparable mean opinion score (MOS) 4.17±0.06 to baselines, indicating similar speech naturalness. (4. EXPERIMENTS)
- Limitations include requirement of paired text script and silent video, evaluation only on scripted GRID dataset with fixed grammar and vocabulary, no demonstration on real-time synthesis, or generalization to unseen speakers or spontaneous speech. (5. CONCLUSION)
- VisualTTS requires a pre-recorded silent video and matching text script for synthesis, limiting deployment to scripted applications like automatic dubbing; real-time capability and mobile suitability are not reported. (3. VISUALTTS)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
