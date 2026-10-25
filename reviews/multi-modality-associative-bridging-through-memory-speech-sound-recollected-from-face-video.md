# Multi-modality Associative Bridging through Memory: Speech Sound Recollected from Face Video

Minsu Kim, Joanna Hong, Se Jin Park, Yong Man Ro  
arXiv / imported corpus page 2022 · [arXiv](https://arxiv.org/abs/2204.01265)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

Memory-based cross-modal bridging recalls audio representations from face video, applied to word-level lip reading (LRW/LRW-1000) and speaker-dependent GRID speech reconstruction.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Silent face video |
| Task | Lip reading and speech synthesis from video |
| Vocabulary | LRW/LRW-1000 words; GRID phrase set |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Not reported |

**Limitations.** Speech reconstruction shown only on speaker-dependent GRID; best subjective scores need an added WaveNet vocoder; no live or uncontrolled conditions.

## Full review

### In short

The key idea is not generic fusion; it is storing cross-modal correspondences so video-only decoding can recover some audio-side structure later.

### Review

Table 1 is the cleanest recognition evidence: the proposed method reaches 85.4 on LRW and 50.82 on LRW-1000, which is especially meaningful because the LRW-1000 gap over the next best method is large. The reconstruction side is smaller but still real: Table 2 reports 0.738 STOI, 0.579 ESTOI, and 1.984 PESQ on speaker-dependent GRID, edging Lip2Wav and Yadav et al. The human study in Table 3 reinforces that the gains are audible, with 2.93 naturalness and 3.56 intelligibility before WaveNet, and 4.37/4.27 with the WaveNet vocoder. The catch is scope: the reconstruction result is speaker-dependent GRID, not broad in-the-wild SSI.

### Why it matters

The full text supports that the memory bridge is doing real work on benchmarks: gains are modest on LRW but large on LRW-1000 and enough to edge prior methods on GRID reconstruction.

### Prior state of the art

Audio-visual fusion and common-representation methods usually needed both modalities at inference or failed when one modality was missing.

### What changed

This paper claims that memory can preserve cross-modal associations so a visual-only downstream model can still borrow audio structure.

### Position in the field

Interesting cross-modal architectural paper adjacent to lip reading and lip-to-speech reconstruction.

### Practical value

Useful when paired audio-video data exists at training time and the goal is to improve visual-only inference with recalled audio structure.

### Advanced

cross-modal system design; benchmark quality

### Unresolved

speaker-independent reconstruction; in-the-wild deployment; online use

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | silent face video with recalled audio memory during training |
| Body site | face; lip |
| Output | speech-audio |
| Vocabulary type | word-level lip reading plus fixed-phrase speech reconstruction |
| Vocabulary size | LRW/LRW-1000 word vocabularies and GRID phrase set |
| Metrics and results | word accuracy; STOI; ESTOI; PESQ; human naturalness and intelligibility ratings |
| Evaluation protocol | word-level lip-reading benchmarks on LRW/LRW-1000 plus speaker-dependent GRID speech reconstruction with objective and human evaluation |

### Limits

- **Technical:** The speech-reconstruction claim remains on speaker-dependent GRID, and the best subjective scores require an added WaveNet vocoder.
- **Evaluation:** No live deployment, no uncontrolled capture conditions, and no speaker-independent reconstruction result are shown.
- **Deployment:** The method needs paired audio-video supervision and benchmark-like preprocessing.
- **Scope of this review:** Benchmark lip reading and speech reconstruction from face video.

### Evidence

- The abstract says the paper introduces an audio-visual multimodal bridging framework that can exploit both modalities even when only unimodal input is available at inference. (Abstract)
- Table 1 reports the proposed method at 85.4 word accuracy on LRW and 50.82 on LRW-1000, ahead of the listed prior methods on both datasets. (Table 1. Lip reading word accuracy comparison with visual modal inputs on LRW and LRW-1000 dataset.)
- Section 4.2.1 says the speech-reconstruction experiments use speaker-dependent GRID with subjects 1, 2, 4, and 29 following prior work. (4.2.1 Dataset)
- Table 2 reports speaker-dependent GRID reconstruction scores of 0.738 STOI, 0.579 ESTOI, and 1.984 PESQ for the proposed method. (Table 2. Performance of speech reconstruction comparison with visual modal inputs in a speaker-dependent setting on GRID.)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
