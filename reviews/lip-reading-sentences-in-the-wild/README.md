# Lip Reading Sentences in the Wild

Joon Son Chung, Andrew Senior, Oriol Vinyals, Andrew Zisserman  
2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pp. 3444-3453 · [DOI](https://doi.org/10.1109/CVPR.2017.367) · [arXiv](https://arxiv.org/abs/1611.05358)

**Section:** [Lip & face video](../../README.md#lip--face-video) · **Review basis:** full_text

A structured review of *Lip Reading Sentences in the Wild* (Joon Son Chung et al., 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pp. 3444-3453) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Introduces Watch, Listen, Attend and Spell and the BBC LRS dataset; lips-only decoding reaches 50.2% WER on open-vocabulary broadcast sentences, beating a professional lipreader (73.8%).

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera (broadcast face/lip video), optional audio |
| Task | Sentence-level lipreading and audio-visual recognition |
| Vocabulary | Open vocabulary, 17,428 words |
| Speaker | Speaker-independent |
| Session | Not applicable |
| Online / offline | Offline |
| Key result | 50.2% lips-only WER on LRS; 13.9% audio-visual WER (clean); 3.0% WER on GRID |

**Limitations.** Vocalized broadcast speech only, offline batch decoding, and lips-only WER still near 50%.

## Full review

### In short

Moved lipreading to open-vocabulary broadcast sentences and beat a professional lipreader.

### Review

The paper introduces the Watch, Listen, Attend and Spell model and the BBC-derived LRS dataset (118,116 sentences, 17,428-word vocabulary, time-based train/val/test splits). Lips-only decoding reaches 50.2% WER on the LRS test set after curriculum learning, scheduled sampling and beam search, against 73.8% WER for a professional lipreader on 200 test videos; adding lips to audio lowers WER from 17.7% to 13.9% in clean conditions and helps more in noise. It also reports 3.0% WER on GRID and 23.8% on LRW. For SSI the key shift is from closed grammars to open-vocabulary, in-the-wild visual speech, though the data are vocalized broadcast speech and decoding is offline.

### Why it matters

Made large-vocabulary, in-the-wild visual speech recognition a credible research target and supplied the dataset template later VSR work relied on.

### Prior state of the art

Lipreading was evaluated mainly on constrained corpora such as GRID or word-level LRW.

### What changed

Introduces an attention-based audio-visual sequence-to-sequence model and a large broadcast sentence dataset, enabling open-vocabulary lips-only decoding.

### Position in the field

Seminal in-the-wild VSR paper and dataset; background for camera-based SSI.

### Practical value

Benchmark and modeling reference; 50% lips-only WER is far from usable silent dictation.

### Advanced

dataset_scale; open_vocabulary; audio_visual_fusion

### Unresolved

Silent (non-vocalized) speech; online decoding; usable lips-only accuracy

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-recognition; dataset |
| Input | video (lip region) with optional audio |
| Sensor | broadcast camera footage (BBC); microphone audio for AV variants |
| Body site | face; lip |
| Output | text |
| Vocabulary type | open vocabulary (broadcast speech) |
| Vocabulary size | 17,428 words in LRS |
| Metrics and results | LRS lips-only WER 50.2% (CER 39.5%) vs professional lipreader 73.8%; audio-visual clean WER 13.9% vs audio-only 17.7%; GRID WER 3.0%; LRW WER 23.8% |
| Evaluation protocol | LRS test set with time-based split, noise conditions for audio, professional lipreader comparison, GRID and LRW benchmarks |

### Limits

- **Technical:** Batch decoding over full sequences; unconstrained attention alignment; lips-only WER remains about 50%.
- **Evaluation:** Dataset is BBC news and debate programmes; human comparison uses one professional lipreader on 200 videos.
- **Deployment:** Offline model trained on broadcast footage; no live or silent-speaker evaluation.
- **Scope of this review:** Visual and audio-visual recognition of vocalized broadcast speech.

### Evidence

- The paper proposes the Watch, Listen, Attend and Spell network with curriculum learning and scheduled sampling for lips-only and audio-visual sentence recognition. (Abstract; Section 3)
- LRS comprises 118,116 sentences with a 17,428-word vocabulary from BBC broadcasts, split by date into train (101,195), val (5,138) and test (11,783) utterances. (Section 4 (dataset), split table)
- Lips-only WAS+CL+SS+BS reaches 50.2% WER on the LRS test set, versus 73.8% for a professional lipreader; audio-visual WLAS reaches 13.9% WER in clean conditions. (Section 5, Table 5)
- WAS achieves 3.0% WER on GRID and 23.8% on LRW. (Table 8)
- The authors note unconstrained attention alignment and batch-mode decoding over the whole sequence, proposing monotonic constraints and online architectures as future work. (Conclusion / future work)

## More reviews in Lip & face video

- [Improved Speech Reconstruction from Silent Video](../improved-speech-reconstruction-from-silent-video/) (2017). Reconstructs speech from silent full-face video plus optical flow with a CNN and temporal post-processing network, outperforming prior methods on GRID and TCD-TIMIT in objective metrics and human word accuracy.
- [Lip2AudSpec: Speech reconstruction from silent lip movements video](../lip2audspec-speech-reconstruction-from-silent-lip-movements-video/) (2017). Lip2AudSpec reconstructs speech from silent lip video using an auditory-spectrogram autoencoder bottleneck as target, improving objective intelligibility metrics and human word accuracy (55.8% vs 50.9%) over a baseline on four GRID speakers.
- [Seeing Through Noise: Visually Driven Speaker Separation and Enhancement](../seeing-through-noise-visually-driven-speaker-separation-and-enhancement/) (2017). Uses visual speech predictions from face video to build masks that separate or enhance a target speaker from audio mixtures, beating audio-only separation on GRID and TCD-TIMIT. Not an SSI paper.
- [Vid2speech: Speech Reconstruction from Silent Video](../vid2speech-speech-reconstruction-from-silent-video/) (2017). Vid2speech reconstructs intelligible speech from silent face video on GRID with speaker-specific models and LPC-style resynthesis, reaching about 80% human intelligibility and partial out-of-vocabulary recovery.
- [Deep Audio-Visual Speech Recognition](../deep-audio-visual-speech-recognition/) (2018). Landmark AVSR paper that releases LRS2-BBC and compares CTC and sequence-to-sequence Transformers on one shared encoder. Video-only TM-seq2seq reaches 48.3% WER with an LM (49.8% without; the 70.4% WAS baseline has no stated decoding conditions, and the same group's Transformer three months earlier already reached 50.0%). CTC and seq2seq differ little once an LM or audio is added.
- [Harnessing AI for Speech Reconstruction using Multi-view Silent Video Feed](../harnessing-ai-for-speech-reconstruction-using-multi-view-silent-video-feed/) (2018). Reconstructs speech audio from multi-view silent video on OuluVS2 with CNN-LSTM models, showing multi-view input improves PESQ over single view and that camera placement matters.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
