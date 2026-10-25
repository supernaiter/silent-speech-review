# WESPER: Zero-shot and Realtime Whisper to Normal Voice Conversion for Whisper-based Speech Interactions

Jun Rekimoto  
Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (CHI '23), April 23--28, 2023 · [DOI](https://doi.org/10.1145/3544548.3580706) · [arXiv](https://arxiv.org/abs/2303.01639)

**Section:** [Acoustic, whisper & wearable motion sensors](../README.md#acoustic-whisper--wearable-motion-sensors) · **Review basis:** full_text

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

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
