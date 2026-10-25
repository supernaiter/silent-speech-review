# High-Quality Automatic Voice Over with Accurate Alignment: Supervision through Self-Supervised Discrete Speech Units

Junchen Lu, Berrak Sisman, Mingyang Zhang, Haizhou Li  
arXiv / imported corpus page 2023 · [arXiv](https://arxiv.org/abs/2306.17005)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

An automatic voice-over system that supervises alignment by predicting self-supervised discrete speech units from text and lip video, improving lip-sync and speech quality on a single-speaker dataset. Not an SSI paper.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera (lip video) plus text script |
| Task | Automatic voice-over (dubbing) |
| Vocabulary | Not stated |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | WER 24.7%, LSE-C 6.81, LSE-D 7.56, MOS 3.98 on single-speaker Chem dataset |

**Limitations.** Validated only on one single-speaker dataset; requires text scripts and pretrained unit tokenizer and vocoder; no multi-speaker or in-the-wild testing.

## Full review

### In short

This video-conditioned AVO system innovatively supervises alignment by predicting discrete speech units rather than reconstructing acoustic features, leading to better lip-sync and speech quality on a single-speaker dataset; however, it is not an SSI interface paper.

### Review

This paper presents DSU-AVO, an automatic voice over system that innovatively supervises the multimodal alignment learning through discrete speech unit prediction derived from self-supervised HuBERT models and clustering. By replacing acoustic feature reconstruction with classification of discrete units at the context level, the approach provides more direct learning signals that yield improved lip-sync accuracy and speech naturalness. The system integrates a pretrained unit vocoder for synthesis conditioned on predicted units, effectively alleviating the mismatch typical in prior acoustic decoding. Experimental evaluation on the single-speaker Chem dataset demonstrates significant gains over baselines in synchronization metrics (LSE-C 6.81 vs. 6.11 for Neural Dubber), duration deviation (FD 3.23 vs. 9.39), intelligibility (WER 24.7% vs. 75.8%), and subjective quality (MOS 3.98 vs. 2.43). Despite these strong contributions, the work is limited to single-speaker settings without multi-speaker or in-the-wild testing and depends on pretrained components, limiting immediate deployment scope. Furthermore, it does not constitute a silent speech interface per se but advances alignment supervision in video-conditioned speech synthesis.

### Why it matters

The key advance is reframing alignment supervision from acoustic regression to discrete speech unit prediction using self-supervised speech representations, delivering more direct and effective training for lip-synchronized speech generation in automatic voice over.

### Prior state of the art

Prior AVO systems used acoustic feature (mel-spectrogram) reconstruction as a learning objective, which provides indirect supervision for alignment and suffers from mismatch between context and acoustic features.

### What changed

Replaces acoustic feature regression with discrete speech unit prediction derived via HuBERT and k-means clustering for direct alignment supervision, and uses Unit HiFi-GAN vocoder for synthesis conditioned on predicted units, reducing mismatch and improving synchronization and naturalness.

### Position in the field

Advances automatic voice over and video-conditioned TTS; adjacent but not focused on silent speech interfaces.

### Practical value

Improves synchronization accuracy and speech naturalness for scripted dubbing applications, useful in media production and related domains.

### Advanced

system_design; evaluation

### Unresolved

Multi-speaker generalization; expressive prosody; strict SSI relevance

### Evaluation details

| Item | Details |
| --- | --- |
| Task | automatic voice over |
| Input | text + video (lip image frames) |
| Sensor | camera |
| Body site | lip |
| Output | speech-audio |
| Metrics and results | Lip Sync Error Confidence (LSE-C) 6.81, Lip Sync Error Distance (LSE-D) 7.56, Frame Disturbance (FD) 3.23, Word Error Rate (WER) 24.7%, Mean Opinion Score (MOS) 3.98 ± 0.08, Best-Worst Scaling (BWS) best 84.0% / worst 1.3% |
| Evaluation protocol | Objective metrics (LSE-C, LSE-D, FD, WER) and subjective listening tests (MOS, BWS) |

### Limits

- **Technical:** Single-speaker Chem dataset only; reliant on pretrained unit tokenizer and vocoder; no tests on multi-speaker, unseen words, or moving conditions; contextual mismatch remains an open issue outside studied domain.
- **Evaluation:** Evaluation limited to single-speaker Chem dataset; WER from ASR pretrained on Librispeech only and not adapted; no unseen words or walking tests reported.
- **Deployment:** Requires input of video frames and text scripts; depends on pretrained unit tokenizer and vocoder; only validated on single-speaker Chem dataset; no multi-speaker or in-the-wild testing yet.
- **Scope of this review:** Specific to automatic voice over with text and video inputs; not a generic silent speech interface solution.

### Evidence

- We propose a novel AVO method leveraging the learning objective of self-supervised discrete speech unit prediction, which not only provides more direct supervision for the alignment learning, but also alleviates the mismatch between the text-video context and acoustic features. (Abstract)
- We propose to guide the context modeling and alignment learning of AVO more directly by imposing discrete speech unit prediction as supervision at the context representation level, replacing mel-spectrogram reconstruction supervision, thus enabling more accurate lip-speech synchronization. (We propose to guide the context modeling)
- We utilize Chem dataset, a single-speaker audio-visual English speech dataset, with official transcripts from YouTube, using 6088 training samples, 200 validation, and 200 test samples for evaluation of our AVO systems. (4.1.1. Dataset)
- DSU-AVO achieves Lip Sync Error - Confidence (LSE-C) of 6.81, Lip Sync Error - Distance (LSE-D) of 7.56, Frame Disturbance (FD) of 3.23, Word Error Rate (WER) of 24.7%, Mean Opinion Score (MOS) of 3.98 ± 0.08, and Best-Worst Scaling (BWS) for lip-speech synchronization best 84.0% and worst 1.3%. (4.2. Experimental results)
- The method is trained and tested only on the single-speaker Chem dataset; it relies on paired video, text, and audio data and pretrained unit tokenizer and vocoder; generalization to multi-speaker, unseen words, and walking conditions is not reported. (4.1.1. Dataset)
- DSU-AVO requires text and video frame inputs, pretrained SSL-based discrete unit tokenizer and vocoder models, and has only demonstrated results on single-speaker data, limiting immediate deployment in multi-speaker or diverse dubbing scenarios. (3.3. DSU)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
