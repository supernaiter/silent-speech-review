# A First Exploration of Neuromorphic OT-CFM for Multi-Speaker VSR

Lin Chen, Jingping Fang, Hairui Liu, Chenyang Xu, Junhao Chen, Xiaorui Li, Weidong Cai, Xiaoming Chen  
ECCV 2026 · [DOI](https://doi.org/10.1007/978-3-032-37281-9_8) · [arXiv](https://arxiv.org/abs/2606.31225)

**Section:** [Lip & face video](../../README.md#lip--face-video) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *A First Exploration of Neuromorphic OT-CFM for Multi-Speaker VSR* (Lin Chen et al., ECCV 2026) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Neuromorphic OT-CFM (LipsFlow) for multi-speaker visual speech recognition from event streams; 22.3% WER and 19.8% VER on DVS-Lip with 240 ms latency.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Event streams from RGB video or DVS dataset (camera) |
| Task | Visual speech recognition (multi-speaker) |
| Vocabulary | Not stated |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 22.3% WER, 19.8% VER on DVS-Lip, 240 ms latency |

**Limitations.** Camera-based, not a wearable SSI; author-reported benchmark results only; vocabulary and speaker split details limited; on-device, walking and clinical use untested.


## More reviews in Lip & face video

- [AVSRBench: A Multi-Condition AVSR Benchmark](../avsrbench-a-multi-condition-avsr-benchmark/) (2026). Benchmark comparing visual-only, audio-only and audio-visual speech recognition across six datasets; sub-1% AV WER on LRS3, visual-only collapses out of domain, and AV fusion helps clearly mainly under Lombard speech.
- [LipSody: Lip-to-Speech Synthesis with Enhanced Prosody Consistency](../lipsody-lip-to-speech-synthesis-with-enhanced-prosody-consistency/) (2026). LipSody, lip-to-speech synthesis with enhanced prosody consistency from facial video; improves reference prosody metrics and gets 54.22% listener preference, but not WER.
- [SLD-L2S: Hierarchical Subspace Latent Diffusion for High-Fidelity Lip to Speech Synthesis](../sld-l2s-hierarchical-subspace-latent-diffusion-for-high-fidelity-lip-to-speech-synthesis/) (2026). SLD-L2S, a hierarchical subspace latent diffusion model for lip-to-speech synthesis that improves naturalness, while word accuracy and speaker similarity trail stronger baselines.
- [Landmark Guided Visual Feature Extractor for Visual Speech Recognition with Limited Resource](../landmark-guided-visual-feature-extractor-for-visual-speech-recognition-with-limited-resource/) (2025). Combines 20 lip landmarks with image features for visual word recognition; with one-third training data on LRW-ID, accuracy improves from 85.75% to 86.65%, at larger model size.
- [LipDiffuser: Lip-to-Speech Generation with Conditional Diffusion Models](../lipdiffuser-lip-to-speech-generation-with-conditional-diffusion-models/) (2025). LipDiffuser generates speech from mouth video plus the target speaker's enrollment audio using a conditional diffusion model. On LRS3-CHiME3 at -10 dB it improves quality and speaker similarity, but WER is 38% versus 36% for the best baseline.
- [LTA-L2S: Lexical Tone-Aware Lip-to-Speech Synthesis for Mandarin with Cross-Lingual Transfer Learning](../lta-l2s-lexical-tone-aware-lip-to-speech-synthesis-for-mandarin-with-cross-lingual-transfer-lear/) (2025). LTA-L2S synthesizes Mandarin speech from lip video using English pretraining and tone-aware generation, reducing character and tone errors versus baselines, but CER remains 61.2%.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
