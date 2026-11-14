# LTA-L2S: Lexical Tone-Aware Lip-to-Speech Synthesis for Mandarin with Cross-Lingual Transfer Learning

Kang Yang, Yifan Liang, Fangkun Liu, Zhenping Xie, Chengshi Zheng  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2509.25670)

**Section:** [Lip & face video](../../README.md#lip--face-video) · **Review basis:** full_text+summary

A structured review of *LTA-L2S: Lexical Tone-Aware Lip-to-Speech Synthesis for Mandarin with Cross-Lingual Transfer Learning* (Kang Yang et al., arXiv 2025) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

LTA-L2S synthesizes Mandarin speech from lip video using English pretraining and tone-aware generation, reducing character and tone errors versus baselines, but CER remains 61.2%.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Existing video (CN-CVS), 96x96 mouth crops |
| Task | Lip-to-speech synthesis |
| Vocabulary | Mandarin continuous speech; size not stated |
| Speaker | Speaker-independent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | CER 61.2%, TER 40.9% on CN-CVS unseen-speaker split |

**Limitations.** High character error rate, ASR-based evaluation, unclear speaker-embedding source, and no truly silent or real-time evaluation.


## More reviews in Lip & face video

- [Landmark Guided Visual Feature Extractor for Visual Speech Recognition with Limited Resource](../landmark-guided-visual-feature-extractor-for-visual-speech-recognition-with-limited-resource/) (2025). Combines 20 lip landmarks with image features for visual word recognition; with one-third training data on LRW-ID, accuracy improves from 85.75% to 86.65%, at larger model size.
- [LipDiffuser: Lip-to-Speech Generation with Conditional Diffusion Models](../lipdiffuser-lip-to-speech-generation-with-conditional-diffusion-models/) (2025). LipDiffuser generates speech from mouth video plus the target speaker's enrollment audio using a conditional diffusion model. On LRS3-CHiME3 at -10 dB it improves quality and speaker similarity, but WER is 38% versus 36% for the best baseline.
- [NaturalL2S: End-to-End High-quality Multispeaker Lip-to-Speech Synthesis with Differential Digital Signal Processing](../naturall2s-end-to-end-high-quality-multispeaker-lip-to-speech-synthesis-with-differential-digita/) (2025). NaturalL2S synthesizes speech from mouth video without a reference audio of the speaker, using differentiable DSP. It improves quality and naturalness, but WER is worse than the comparison (30.4% vs 27.7% on LRS3).
- [RESOUND: Speech Reconstruction from Silent Videos via Acoustic-Semantic Decomposed Modeling](../resound-speech-reconstruction-from-silent-videos-via-acoustic-semantic-decomposed-modeling/) (2025). RESOUND synthesizes speech from silent video plus a 0.5 s reference audio by separating content and prosody paths; naturalness improves, but LRS2 WER (28.55%) is worse than LipVoicer (17.04%).
- [VSpeechLM: A Visual Speech Language Model for Visual Text-to-Speech Task](../vspeechlm-a-visual-speech-language-model-for-visual-text-to-speech-task/) (2025). VSpeechLM generates lip-synchronized speech from text, a reference voice and lip video by converting lip timing into phoneme sequences; WER is 12.5% on Chem and 18.3% on GRID.
- [A First Exploration of Neuromorphic OT-CFM for Multi-Speaker VSR](../lipsflow-a-first-exploration-of-neuromorphic-ot-cfm-for-multi-speaker-vsr/) (2026). Neuromorphic OT-CFM (LipsFlow) for multi-speaker visual speech recognition from event streams; 22.3% WER and 19.8% VER on DVS-Lip with 240 ms latency.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
