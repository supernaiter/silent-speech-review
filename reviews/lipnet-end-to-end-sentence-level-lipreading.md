# LipNet: End-to-End Sentence-level Lipreading

Yannis M. Assael, Brendan Shillingford, Shimon Whiteson, Nando de Freitas  
arXiv 2016 · [arXiv](https://arxiv.org/abs/1611.01599)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

A structured review of *LipNet: End-to-End Sentence-level Lipreading* (Yannis M. Assael et al., arXiv 2016) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

End-to-end lipreader (spatiotemporal CNN, Bi-GRU, CTC) decoding GRID sentences from video; 4.8% WER on overlapped speakers and 11.4% on unseen speakers.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera (frontal face/lip video) |
| Task | Sentence-level lipreading |
| Vocabulary | GRID closed grammar (64,000 possible sentences) |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 4.8% WER overlapped speakers, 11.4% WER unseen speakers on GRID |

**Limitations.** Only GRID's tiny fixed grammar with vocalized speech; no open vocabulary, in-the-wild, silent-articulation or real-time evaluation.

## Full review

### In short

Historic first end-to-end sentence-level lipreader, but only on the tiny, rigid GRID grammar.

### Review

LipNet showed that spatiotemporal convolutions, bidirectional GRUs and CTC could be trained end to end to map lip video to character sequences, removing hand-crafted features and frame alignments. On GRID it reports 4.8% WER on the overlapped-speaker split and 11.4% on held-out speakers, with clear gains over its own LSTM and 2D-CNN baselines and over three hearing-impaired lipreaders (47.7% average WER). The weakness is the benchmark: GRID is a fixed six-slot grammar with a few dozen words, so the result says little about open-vocabulary lipreading, and the headline comparison to a prior word-level 86.4% accuracy is not like-for-like. For SSI, it is mainly the architectural template that later camera-based silent speech systems built on.

### Why it matters

Established the end-to-end sequence lipreading template (STCNN + RNN + CTC) that later visual SSI work inherited.

### Prior state of the art

Lipreading was mostly word classification or relied on hand-engineered visual features and separate sequence models.

### What changed

Trains a single network end to end from video frames to character sequences with CTC, at sentence level.

### Position in the field

Seminal deep lipreading paper; background for camera-based SSI rather than an SSI system itself.

### Practical value

Architectural reference and GRID baseline; limited direct value for real silent-speech use.

### Advanced

end_to_end_modeling; sentence_level_decoding

### Unresolved

Open vocabulary; in-the-wild video; truly silent articulation

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-recognition |
| Input | video |
| Sensor | camera (GRID frontal face video) |
| Body site | face; lip |
| Output | text |
| Vocabulary type | closed grammar (GRID command + color + preposition + letter + digit + adverb) |
| Vocabulary size | GRID grammar with 64,000 possible sentences |
| Metrics and results | GRID WER 4.8% / CER 1.9% overlapped speakers (95.2% sentence-level accuracy); WER 11.4% / CER 6.4% unseen speakers; hearing-impaired lipreaders 47.7% WER |
| Evaluation protocol | GRID overlapped-speaker and unseen-speaker splits; baselines and human lipreader comparison |

### Limits

- **Technical:** Video-only model trained on GRID's restricted grammar; unseen-speaker WER (11.4%) is more than twice the overlapped-speaker WER (4.8%).
- **Evaluation:** Single constrained dataset; human baseline is 3 people on 300 videos; the 86.4% prior comparison is word-level and speaker-dependent.
- **Deployment:** Offline evaluation on recorded frontal video; no real-time or silent-speaker testing.
- **Scope of this review:** Lipreading of vocalized speech video on GRID; not silent speech specifically.

### Evidence

- The paper presents LipNet as an end-to-end sentence-level lipreading model combining spatiotemporal convolutions, a recurrent network and CTC loss. (Abstract; Section 3)
- Table 2 reports LipNet WER 4.8% (CER 1.9%) on overlapped speakers and 11.4% (CER 6.4%) on unseen speakers, versus Baseline-NoLM 5.6%/13.6%. (Section 4.3, Table 2)
- The unseen-speaker split holds out speakers 1, 2, 20 and 22 (3,971 test videos); the overlapped split holds out 255 random sentences per speaker. (Section 4, dataset description)
- Three hearing-impaired lipreaders average 47.7% WER on unseen-speaker GRID videos (300 videos). (Section 4.3)
- Evaluation is limited to GRID, whose grammar allows only 64,000 sentences; audio-visual integration and larger datasets are left to future work. (Sections 4 and 5)

## More reviews in Lip & face video

- [Improved Speech Reconstruction from Silent Video](improved-speech-reconstruction-from-silent-video.md) (2017). Reconstructs speech from silent full-face video plus optical flow with a CNN and temporal post-processing network, outperforming prior methods on GRID and TCD-TIMIT in objective metrics and human word accuracy.
- [Lip Reading Sentences in the Wild](lip-reading-sentences-in-the-wild.md) (2017). Introduces Watch, Listen, Attend and Spell and the BBC LRS dataset; lips-only decoding reaches 50.2% WER on open-vocabulary broadcast sentences, beating a professional lipreader (73.8%).
- [Lip2AudSpec: Speech reconstruction from silent lip movements video](lip2audspec-speech-reconstruction-from-silent-lip-movements-video.md) (2017). Lip2AudSpec reconstructs speech from silent lip video using an auditory-spectrogram autoencoder bottleneck as target, improving objective intelligibility metrics and human word accuracy (55.8% vs 50.9%) over a baseline on four GRID speakers.
- [Seeing Through Noise: Visually Driven Speaker Separation and Enhancement](seeing-through-noise-visually-driven-speaker-separation-and-enhancement.md) (2017). Uses visual speech predictions from face video to build masks that separate or enhance a target speaker from audio mixtures, beating audio-only separation on GRID and TCD-TIMIT. Not an SSI paper.
- [Vid2speech: Speech Reconstruction from Silent Video](vid2speech-speech-reconstruction-from-silent-video.md) (2017). Vid2speech reconstructs intelligible speech from silent face video on GRID with speaker-specific models and LPC-style resynthesis, reaching about 80% human intelligibility and partial out-of-vocabulary recovery.
- [Deep Audio-Visual Speech Recognition](deep-audio-visual-speech-recognition.md) (2018). Landmark AVSR paper that releases LRS2-BBC and compares CTC and sequence-to-sequence Transformers on one shared encoder. Video-only TM-seq2seq reaches 48.3% WER with an LM (49.8% without; the 70.4% WAS baseline has no stated decoding conditions, and the same group's Transformer three months earlier already reached 50.0%). CTC and seq2seq differ little once an LM or audio is added.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
