# VSpeechLM: A Visual Speech Language Model for Visual Text-to-Speech Task

Yuyue Wang, Xin Cheng, Yihan Wu, Xihua Wang, Jinchuan Tian, Ruihua Song  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2511.22229)

**Section:** [Lip & face video](../../README.md#lip--face-video) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *VSpeechLM: A Visual Speech Language Model for Visual Text-to-Speech Task* (Yuyue Wang et al., arXiv 2025) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

VSpeechLM generates lip-synchronized speech from text, a reference voice and lip video by converting lip timing into phoneme sequences; WER is 12.5% on Chem and 18.3% on GRID.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Existing video; AV-HuBERT lip features (25 fps) |
| Task | Visual text-to-speech (video dubbing) |
| Vocabulary | Not stated (text-conditioned English) |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | WER 12.5% (Chem), 18.3% (GRID) on generated speech |

**Limitations.** Requires input text and reference audio, so it does not read content from lips; table inconsistencies and no silent-speech use evaluated.


## More reviews in Lip & face video

- [Landmark Guided Visual Feature Extractor for Visual Speech Recognition with Limited Resource](../landmark-guided-visual-feature-extractor-for-visual-speech-recognition-with-limited-resource/) (2025). Lip-landmark graph plus pixel fusion is a standard design (2020 precedent); the 0.90-point low-data gain comes from one unseeded run, and LRW 91.69% stays below 95.0%.
- [LipDiffuser: Lip-to-Speech Generation with Conditional Diffusion Models](../lipdiffuser-lip-to-speech-generation-with-conditional-diffusion-models/) (2025). Diffusion decoder with per-frame MP-FiLM (M06) and audio-only pretraining (M02) are standard; quality and speaker-similarity leads rest on enhanced targets and a clean-reference enrollment.
- [LTA-L2S: Lexical Tone-Aware Lip-to-Speech Synthesis for Mandarin with Cross-Lingual Transfer Learning](../lta-l2s-lexical-tone-aware-lip-to-speech-synthesis-for-mandarin-with-cross-lingual-transfer-lear/) (2025). Mandarin lip-to-speech whose gain over Intelligible matches its English-initialization ablation; the tone components move CER little with no repeats reported, and pitch removal leaves TER at 40.9%.
- [NaturalL2S: End-to-End High-quality Multispeaker Lip-to-Speech Synthesis with Differential Digital Signal Processing](../naturall2s-end-to-end-high-quality-multispeaker-lip-to-speech-synthesis-with-differential-digita/) (2025). DDSP prior and jointly trained vocoder (M06) are standard: joint waveform training predates it; quality leads its baselines, but LRS3 WER 30.4% trails the uncompared LipVoicer (21.4%).
- [RESOUND: Speech Reconstruction from Silent Videos via Acoustic-Semantic Decomposed Modeling](../resound-speech-reconstruction-from-silent-videos-via-acoustic-semantic-decomposed-modeling/) (2025). Decoder split (M06) and lip-reader text plus audio prompt (M07) are standard; WER gain comes from the lip reader, LRS3 WER level with LipVoicer, prosody leads confounded by the prompt.
- [A First Exploration of Neuromorphic OT-CFM for Multi-Speaker VSR](../lipsflow-a-first-exploration-of-neuromorphic-ot-cfm-for-multi-speaker-vsr/) (2026). Event input and a two-step OT-CFM decoder are standard; the DVS-Lip evaluation is behind: WER on an isolated-word set with no split details or seeds, and baselines that do not match their sources.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
