# AVSRBench: A Multi-Condition AVSR Benchmark

Rishabh Jain, Naomi Harte  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2609.10366)

**Section:** [Lip & face video](../../README.md#lip--face-video) · **Review basis:** full_text+summary

A structured review of *AVSRBench: A Multi-Condition AVSR Benchmark* (Rishabh Jain and Naomi Harte, arXiv 2026) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Benchmark comparing visual-only, audio-only and audio-visual speech recognition across six datasets; sub-1% AV WER on LRS3, visual-only collapses out of domain, and AV fusion helps clearly mainly under Lombard speech.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | RGB camera and microphone (audio-visual) |
| Task | Audio-visual speech recognition benchmark |
| Vocabulary | Dataset-dependent; continuous open vocabulary (GRID fixed grammar) |
| Speaker | Not stated |
| Session | Not applicable |
| Online / offline | Offline |
| Key result | 0.79% AV WER on LRS3 (Llama-AVSR); visual-only WER 110.07% on RoomReader-AV (Auto-AVSR) |

**Limitations.** Uses fixed public checkpoints without retraining; camera-based AVSR rather than wearable SSI; no real-time or on-device measurement; limited speaker-split and statistical detail.


## More reviews in Lip & face video

- [A First Exploration of Neuromorphic OT-CFM for Multi-Speaker VSR](../lipsflow-a-first-exploration-of-neuromorphic-ot-cfm-for-multi-speaker-vsr/) (2026). Neuromorphic OT-CFM (LipsFlow) for multi-speaker visual speech recognition from event streams; 22.3% WER and 19.8% VER on DVS-Lip with 240 ms latency.
- [LipSody: Lip-to-Speech Synthesis with Enhanced Prosody Consistency](../lipsody-lip-to-speech-synthesis-with-enhanced-prosody-consistency/) (2026). LipSody, lip-to-speech synthesis with enhanced prosody consistency from facial video; improves reference prosody metrics and gets 54.22% listener preference, but not WER.
- [SLD-L2S: Hierarchical Subspace Latent Diffusion for High-Fidelity Lip to Speech Synthesis](../sld-l2s-hierarchical-subspace-latent-diffusion-for-high-fidelity-lip-to-speech-synthesis/) (2026). SLD-L2S, a hierarchical subspace latent diffusion model for lip-to-speech synthesis that improves naturalness, while word accuracy and speaker similarity trail stronger baselines.
- [Landmark Guided Visual Feature Extractor for Visual Speech Recognition with Limited Resource](../landmark-guided-visual-feature-extractor-for-visual-speech-recognition-with-limited-resource/) (2025). Combines 20 lip landmarks with image features for visual word recognition; with one-third training data on LRW-ID, accuracy improves from 85.75% to 86.65%, at larger model size.
- [LipDiffuser: Lip-to-Speech Generation with Conditional Diffusion Models](../lipdiffuser-lip-to-speech-generation-with-conditional-diffusion-models/) (2025). LipDiffuser generates speech from mouth video plus the target speaker's enrollment audio using a conditional diffusion model. On LRS3-CHiME3 at -10 dB it improves quality and speaker similarity, but WER is 38% versus 36% for the best baseline.
- [LTA-L2S: Lexical Tone-Aware Lip-to-Speech Synthesis for Mandarin with Cross-Lingual Transfer Learning](../lta-l2s-lexical-tone-aware-lip-to-speech-synthesis-for-mandarin-with-cross-lingual-transfer-lear/) (2025). LTA-L2S synthesizes Mandarin speech from lip video using English pretraining and tone-aware generation, reducing character and tone errors versus baselines, but CER remains 61.2%.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
