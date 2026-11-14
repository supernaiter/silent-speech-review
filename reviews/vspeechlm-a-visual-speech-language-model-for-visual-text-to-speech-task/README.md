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

- [Landmark Guided Visual Feature Extractor for Visual Speech Recognition with Limited Resource](../landmark-guided-visual-feature-extractor-for-visual-speech-recognition-with-limited-resource/) (2025). Combines 20 lip landmarks with image features for visual word recognition; with one-third training data on LRW-ID, accuracy improves from 85.75% to 86.65%, at larger model size.
- [LipDiffuser: Lip-to-Speech Generation with Conditional Diffusion Models](../lipdiffuser-lip-to-speech-generation-with-conditional-diffusion-models/) (2025). LipDiffuser generates speech from mouth video plus the target speaker's enrollment audio using a conditional diffusion model. On LRS3-CHiME3 at -10 dB it improves quality and speaker similarity, but WER is 38% versus 36% for the best baseline.
- [LTA-L2S: Lexical Tone-Aware Lip-to-Speech Synthesis for Mandarin with Cross-Lingual Transfer Learning](../lta-l2s-lexical-tone-aware-lip-to-speech-synthesis-for-mandarin-with-cross-lingual-transfer-lear/) (2025). LTA-L2S synthesizes Mandarin speech from lip video using English pretraining and tone-aware generation, reducing character and tone errors versus baselines, but CER remains 61.2%.
- [NaturalL2S: End-to-End High-quality Multispeaker Lip-to-Speech Synthesis with Differential Digital Signal Processing](../naturall2s-end-to-end-high-quality-multispeaker-lip-to-speech-synthesis-with-differential-digita/) (2025). NaturalL2S synthesizes speech from mouth video without a reference audio of the speaker, using differentiable DSP. It improves quality and naturalness, but WER is worse than the comparison (30.4% vs 27.7% on LRS3).
- [RESOUND: Speech Reconstruction from Silent Videos via Acoustic-Semantic Decomposed Modeling](../resound-speech-reconstruction-from-silent-videos-via-acoustic-semantic-decomposed-modeling/) (2025). RESOUND synthesizes speech from silent video plus a 0.5 s reference audio by separating content and prosody paths; naturalness improves, but LRS2 WER (28.55%) is worse than LipVoicer (17.04%).
- [A First Exploration of Neuromorphic OT-CFM for Multi-Speaker VSR](../lipsflow-a-first-exploration-of-neuromorphic-ot-cfm-for-multi-speaker-vsr/) (2026). Neuromorphic OT-CFM (LipsFlow) for multi-speaker visual speech recognition from event streams; 22.3% WER and 19.8% VER on DVS-Lip with 240 ms latency.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
