# VCVTS: Multi-speaker Video-to-Speech synthesis via cross-modal knowledge transfer from voice conversion

Disong Wang, Shan Yang, Dan Su, Xunying Liu, Dong Yu, Helen Meng  
arXiv 2022 · [arXiv](https://arxiv.org/abs/2202.09081)

**Section:** [Lip & face video](../../README.md#lip--face-video) · **Review basis:** full_text

A structured review of *VCVTS: Multi-speaker Video-to-Speech synthesis via cross-modal knowledge transfer from voice conversion* (Disong Wang et al., arXiv 2022) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

VCVTS performs multi-speaker video-to-speech synthesis by transferring knowledge from voice conversion, with speaker control from reference speech, on GRID and LRW.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Silent lip video plus reference speech |
| Task | Speech synthesis from lip video |
| Vocabulary | GRID 52 words; LRW 500+ words |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Not reported |

**Limitations.** Large seen/unseen speaker gap and vocoder-dependent quality; offline benchmarks only, requires reference speech, not validated interactively.

## Full review

### In short

The real move is importing structure from voice conversion, not just adding another speaker embedding.

### Review

Table 1 is the anchor. On GRID seen speakers, VCVTS with GL reaches 1.816 PESQ, 0.691 STOI, 0.512 ESTOI, and 4.38 MOS speaker similarity, improving over XTS and Lip2Wav. On unseen GRID speakers, the same model reaches 1.417/0.582/0.330 with 3.25 MOS naturalness and 2.66 MOS speaker similarity, again ahead of the baselines listed there. LRW is harder, but the model still reaches 1.352 PESQ, 0.628 STOI, and 0.458 ESTOI with 3.68 MOS speaker similarity. The paper is strongest where the architecture is most explicit: Section 2.3 shows that the VTS system is literally composed from VC speaker and pitch modules plus a Lip2Ind front-end.

### Why it matters

The full text supports that the VC transfer route improves both seen and unseen speaker VTS, especially on GRID, and gives a more controlled multi-speaker pipeline than prior lip-to-speech baselines.

### Prior state of the art

Multi-speaker VTS was usually a black-box lip-to-speech mapping with weak intermediate structure and brittle speaker control.

### What changed

VCVTS borrows interpretable discrete content units, a speaker encoder, and pitch control from voice conversion instead of learning VTS from scratch.

### Position in the field

Strong multi-speaker video-to-speech systems paper with a clear cross-modal transfer story.

### Practical value

Useful when VTS must preserve speaker identity and intelligibility across multiple speakers instead of retraining separate systems.

### Advanced

system design; speaker control; evaluation

### Unresolved

reference-free control; more robust unseen-speaker generalization; live deployment

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | silent lip video plus reference speech for speaker control |
| Body site | lip |
| Output | speech-audio |
| Vocabulary type | constrained and open-vocabulary video-to-speech |
| Vocabulary size | GRID: 52 words; LRW: 500+ words |
| Metrics and results | PESQ; STOI; ESTOI; MCD; F0-RMSE; MOS speech naturalness; MOS speaker similarity |
| Evaluation protocol | objective and subjective VTS comparison on GRID and LRW for seen and unseen speakers |

### Limits

- **Technical:** The seen/unseen gap remains large, and waveform quality still depends on the vocoder choice.
- **Evaluation:** All evidence is offline benchmark evidence on GRID and LRW with reference speech available for speaker control.
- **Deployment:** The system is complex, reference-speech-dependent, and not validated in an interactive SSI setting.
- **Scope of this review:** Multi-speaker VTS from lip video only.

### Evidence

- The abstract presents VCVTS as a multi-speaker video-to-speech system built on cross-modal knowledge transfer from voice conversion. (ABSTRACT)
- Section 2.3 says the proposed system concatenates a Lip2Ind network with the speaker encoder, pitch predictor, and decoder of a voice-conversion system to form multi-speaker VTS. (2.3. Multi-speaker VTS system)
- Section 3 says experiments use GRID with seen and unseen speaker partitions and LRW with default splits for unconstrained evaluation. (3. EXPERIMENTS)
- Table 1 reports VCVTS on unseen GRID speakers at 1.417 PESQ, 0.582 STOI, 0.330 ESTOI, 3.25 MOS speech naturalness, and 2.66 MOS speaker similarity with Griffin-Lim. (Table 1. Objective and subjective evaluation results of different VTS systems on testing speakers, where ‘Seen’ and ‘Unseen’ denote that)

## More reviews in Lip & face video

- [FastLTS: Non-Autoregressive End-to-End Unconstrained Lip-to-Speech Synthesis](../fastlts-non-autoregressive-end-to-end-unconstrained-lip-to-speech-synthesis/) (2022). FastLTS is a non-autoregressive end-to-end lip-to-speech system that makes unconstrained synthesis substantially faster without obvious quality loss, evaluated on Lip2Wav and GRID.
- [Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction](../learning-audio-visual-speech-representation-by-masked-multimodal-cluster-prediction/) (2022). Self-supervised audio-visual pretraining (masked multimodal cluster prediction) enabling lipreading at 32.5% WER on LRS3 with only 30 h of labels, and 26.9% with 433 h plus self-training.
- [Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild](../lip-to-speech-synthesis-for-arbitrary-speakers-in-the-wild/) (2022). VAE-GAN lip-to-speech synthesis for arbitrary speakers in the wild; holds up on unconstrained LRW/LRS2, and multi-speaker pretraining with 5 h adaptation nearly matches a 20 h single-speaker model.
- [Multi-modality Associative Bridging through Memory: Speech Sound Recollected from Face Video](../multi-modality-associative-bridging-through-memory-speech-sound-recollected-from-face-video/) (2022). Memory-based cross-modal bridging recalls audio representations from face video, applied to word-level lip reading (LRW/LRW-1000) and speaker-dependent GRID speech reconstruction.
- [SVTS: Scalable Video-to-Speech Synthesis](../svts-scalable-video-to-speech-synthesis/) (2022). SVTS shows a simple spectrogram predictor with a pretrained vocoder outperforms prior complex video-to-speech models and scales to large datasets such as LRS3+VoxCeleb2.
- [VisageSynTalk: Unseen Speaker Video-to-Speech Synthesis via Speech-Visage Feature Selection](../visagesyntalk-unseen-speaker-video-to-speech-synthesis-via-speech-visage-feature-selection/) (2022). VisageSynTalk disentangles speech content and visage (identity) features for video-to-speech synthesis, yielding robust results for unseen speakers on benchmarks.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
