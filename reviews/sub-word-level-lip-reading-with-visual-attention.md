# Sub-word Level Lip Reading With Visual Attention

K R Prajwal, Triantafyllos Afouras, Andrew Zisserman  
arXiv / imported corpus page 2021 · [arXiv](https://arxiv.org/abs/2110.07603)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

Camera-only lip reading with WordPiece sub-word units and a visual transformer pooling front-end; reaches 28.9% WER on LRS2 and 40.6% on LRS3 with public-data training (22.6%/30.7% with extended training).

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera (silent face/lip video) |
| Task | Lip reading (visual speech recognition) |
| Vocabulary | Open vocabulary, 30522 WordPiece tokens |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 22.6% WER on LRS2, 30.7% on LRS3 (extended training); 28.9%/40.6% public data only |

**Limitations.** Camera-only lip reading rather than articulatory SSI; offline benchmark results only, with no live silent dictation, latency, privacy or in-the-wild evaluation.

## Full review

### In short

Major lip-reading gain, adjacent to SSI.

### Review

The paper is materially stronger than prior public-data lip reading systems. The final model reaches 28.9 WER on LRS2 using only public data, and 22.6 with additional data, while the ablation table shows the gains are not accidental: WordPiece decoding and visual transformer pooling each buy substantial error reduction. The scope caveat is straightforward. This is a camera-based VSR system, not a tongue, EMG, or ultrasound SSI device.

### Why it matters

This is a strong visual speech recognition paper with real benchmark gains, but it is camera-only lip reading rather than an articulatory SSI modality.

### Prior state of the art

Lip-reading systems often used character-level decoding and average pooling over face features, leaving performance and data efficiency on the table.

### What changed

Introduces visual transformer pooling and WordPiece decoding, then reuses the encoder for visual speech detection.

### Position in the field

Top-tier lip-reading paper adjacent to SSI.

### Practical value

Useful when the problem is silent-video speech recognition and data-efficient visual speech detection, especially without audio.

### Advanced

model quality; data efficiency; transfer to VSD

### Unresolved

in-the-wild silent dictation; occlusion robustness; privacy-sensitive deployment

### Evaluation details

| Item | Details |
| --- | --- |
| Task | lip reading |
| Input | silent video |
| Sensor | camera |
| Body site | face; lip |
| Output | text |
| Vocabulary type | WordPiece sub-word units |
| Vocabulary size | 30522 tokens |
| Metrics and results | Public-data training reaches 28.9 WER on LRS2 and 40.6 on LRS3; extended training reaches 22.6 and 30.7; WordPiece reduces LRS2 WER from 41.0 to 37.2 and VTP further to 30.9 |
| Evaluation protocol | LRS2 and LRS3 WER benchmarks with ablations, plus AVA ActiveSpeaker visual speech detection transfer |

### Limits

- **Technical:** The system still depends on face video quality and benchmark-style training corpora.
- **Evaluation:** All results are offline benchmarks; no live silent dictation study is reported.
- **Deployment:** No discussion of on-device latency, privacy, or in-the-wild robustness beyond benchmarks.
- **Scope of this review:** Camera-only visual speech recognition and detection.

### Evidence

- The paper proposes attention-based pooling, sub-word units, and a visual speech detection model to improve lip reading from silent videos. (Abstract)
- The best public-data model reports 28.9 WER on LRS2 and 40.6 on LRS3, while the larger-data version reaches 22.6 and 30.7. (Table 1. Comparison of different lip reading models on the test sets of the LRS2 and LRS3 datasets in terms of Word Error Rate % (WER,)
- The ablation table shows WordPiece tokenization improves LRS2 WER from 41.0 to 37.2 and adding VTP further reduces it to 30.9, so both proposed changes do real work. (Table 2. Ablation on the design improvements proposed in this)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
