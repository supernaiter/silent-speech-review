# Zero-shot personalized lip-to-speech synthesis with face image based voice control

Zheng-Yan Sheng, Yang Ai, Zhen-Hua Ling  
arXiv / imported corpus page 2023 · [arXiv](https://arxiv.org/abs/2305.14359)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

Zero-shot personalized lip-to-speech synthesis that controls voice identity with face-image-based speaker embeddings, needing no enrollment speech; validated on GRID with 13 unseen speakers.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera (lip video plus face image) |
| Task | Speech synthesis from lip video |
| Vocabulary | Constrained GRID grammar, 6-word sentences |
| Speaker | Speaker-independent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Not reported |

**Limitations.** Tested only on GRID's constrained vocabulary; speech quality below natural speech, with no open-vocabulary, in-the-wild, or real-time evaluation.

## Full review

### In short

Demonstrates effective zero-shot voice control in Lip2Speech by leveraging face image-based speaker embeddings, validated on GRID corpus but constrained by dataset vocabulary and speech naturalness.

### Review

This work advances lip-to-speech synthesis by achieving zero-shot personalized voice control using face images without reference speech, a step forward from prior methods requiring speech enrollment of unseen speakers. The method employs a VAE to disentangle speaker-independent linguistic content and a face identity encoder trained by cross-modal voice-face representation learning to produce speaker embeddings aligned with voice characteristics. Experimental results on the constrained GRID corpus demonstrate the effectiveness of face-based voice control by comparable speaker similarity (lower EER) and face-voice matching MOS compared to speech-reference-based baselines. However, the approach is currently limited to limited vocabulary, shows some speech quality tradeoffs, and lacks validation on open vocabulary or wild video data. This establishes a baseline for zero-shot personalized Lip2Speech with identity control from face images, inviting further work on scaling to diverse and unconstrained real-world scenarios.

### Why it matters

The primary scientific contribution is enabling zero-shot speaker identity control for Lip2Speech synthesis without needing any enrollment speech, by learning and applying face image-based speaker embeddings derived from cross-modal knowledge transfer from speech embeddings, which is a new paradigm in silent video speech synthesis.

### Prior state of the art

Multi-speaker Lip2Speech typically depends on speech-based speaker embeddings (SSE) from reference speech, requiring enrollment and thus not supporting zero-shot voice control from silent video alone.

### What changed

Replaces the need for reference speech embeddings by face-based speaker embeddings trained via cross-modal loss, enabling speaker identity control from only silent video input in a zero-shot setting. Also introduces a VAE to disentangle speaker identity from lip video content in latent representation.

### Position in the field

Advances zero-shot lip-to-speech personalization by cross-modal embedding of face images to voice characteristics, contributing to silent speech interfaces and visual speech reconstruction fields.

### Practical value

Useful for silent video speech reconstruction with speaker identity control without enrollment speech, but currently constrained to limited vocabulary and controlled lab conditions.

### Advanced

system_design; problem_reframing; evaluation

### Unresolved

Open-vocabulary scaling; robustness to pose and in-the-wild video

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | video (lip-centered frames) plus face image |
| Sensor | camera |
| Body site | lip |
| Output | speech-audio |
| Vocabulary type | sentence-level utterances constrained by GRID grammar |
| Vocabulary size | Constrained GRID grammar with 6-word utterances |
| Metrics and results | STOI, ESTOI, PESQ for intelligibility and quality; Equal Error Rate (EER) for speaker similarity; Mean Opinion Score for Speech Naturalness (MOS-SN); Mean Opinion Score for Face-Voice Matching (MOS-FVM) for identity consistency |
| Evaluation protocol | Objective intelligibility and quality metrics (STOI, ESTOI, PESQ), speaker similarity (EER), and subjective mean opinion scores (MOS-SN for naturalness, MOS-FVM for face-voice matching) on Mechanical Turk ratings. |

### Limits

- **Technical:** Limited by GRID constrained vocabulary; occasional gender mismatches in ablations; speech synthesis quality below natural speech and speaker-reference upper bound; limited robustness and generalization beyond controlled dataset.
- **Evaluation:** Tested only on GRID dataset; 13 unseen speakers evaluated. Objective metrics (STOI, ESTOI, PESQ, EER) and subjective MOS-SN and MOS-FVM evaluated. No explicit unseen word or unconstrained vocabulary testing. No evaluation on mobile or real-time settings.
- **Deployment:** Currently limited to constrained vocabulary of GRID corpus with 6-word sentences. Speech quality remains below ground truth and seen-speaker baselines. Requires large-scale and diverse audiovisual data for real-world application. Not tested for open vocabulary or in-the-wild videos.
- **Scope of this review:** Focuses on lip-to-speech synthesis with speaker identity control under constrained vocabulary (GRID corpus); not for large vocabulary or open-domain visual speech recognition or synthesis.

### Evidence

- In this paper, we propose a zero-shot personalized Lip2Speech synthesis method, in which face images control speaker identities. (ABSTRACT)
- We present a method of associated voice-face representation learning that transfers knowledge from a speech identity encoder to a face identity encoder, enabling face images to control voice characteristics in Lip2Speech synthesis without requiring reference speech. (2.2. Associated Voice)
- Experiments were conducted on the GRID dataset consisting of 33 speakers with constrained vocabulary utterances. Training used 20 speakers (10 female + 10 male), with 13 speakers held out for unseen testing. (3.1. Datasets)
- Evaluation uses objective metrics STOI, ESTOI, PESQ for intelligibility and naturalness assessment; EER for speaker similarity; and subjective MOS-SN for naturalness and MOS-FVM for face-voice matching to assess identity matching. (3.4. Evaluation Results)
- The method is limited to the GRID dataset constrained vocabulary setting; synthesis speech quality is below ground truth and seen-speaker upper bound, and is not tested on open vocabulary or in-the-wild video conditions. (4. CONCLUSION)
- Zero-shot personalized Lip2Speech can be achieved from face images without enrollment speech at inference, enabling new assistive applications where speech is unavailable as reference. (2. PROPOSED METHOD)
- The system uses a VAE structure to disentangle speaker identity and linguistic content in video, enabling control of voice characteristics through concatenation of face-based speaker embeddings and latent content codes for decoding speech. (2.1. VAE)
- Face identity encoder is trained by multi-losses (cosine similarity, gender contrastive, cross-entropy) to produce face embeddings aligned with speech identity embeddings for voice control at inference stage. (2.2. Associated Voice)
- Evaluation is conducted with seen and unseen speakers from GRID; subjective tests with MOS-SN and MOS-FVM on Amazon Mechanical Turk with 20 listeners over 20 randomly selected sentences. (3.4. Evaluation Results)
- Objective evaluation shows Proposed Speech using reference speech embeddings achieves lower EER, but Proposed using face embeddings achieves comparable intelligibility and quality, validating face-based voice control feasibility. (3.4. Evaluation Results)
- Proposed-VAE variant sometimes produces incorrect speaker gender voice, indicating challenges in disentangling speaker identity in the latent space effectively. (3.4. Evaluation Results)
- Face-voice matching MOS-FVM is introduced to assess how well synthesized speech matches face image identity, providing a novel subjective evaluation metric for cross-modal identity consistency. (3.4. Evaluation Results)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
