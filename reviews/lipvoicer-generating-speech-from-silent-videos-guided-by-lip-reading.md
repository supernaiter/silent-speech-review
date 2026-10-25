# LipVoicer: Generating Speech from Silent Videos Guided by Lip Reading

Yochai Yemini, Aviv Shamsian, Lior Bracha, Sharon Gannot, Ethan Fetaya  
arXiv / imported corpus page 2023 · [arXiv](https://arxiv.org/abs/2306.03258)

**Section:** [Lip & face video](../README.md#lip--face-video) · **Review basis:** full_text

LipVoicer generates speech from silent video with a diffusion model guided at inference by text from a lip reader via an ASR classifier. On LRS3 it achieves WER 21.4%, versus 86.2% without ASR guidance.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera (lip video) |
| Task | Speech synthesis from lip video |
| Vocabulary | Open vocabulary (LRS2/LRS3) |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | WER 21.4% on LRS3 test (86.2% without ASR guidance) |

**Limitations.** Heavy stack of lip reader, ASR and diffusion with hundreds of inference steps, unsuitable for real-time use; quality depends on lip-reader accuracy.

## Full review

### In short

Strong full-text paper demonstrating that inference-time text guidance via ASR classifier is key to significantly improved intelligibility in lip-to-speech synthesis on challenging in-the-wild video datasets, outperforming prior baselines.

### Review

LipVoicer advances lip-to-speech synthesis by decoupling the task into lip-reading and guided diffusion generation, using classifier guidance derived from ASR on inferred text at inference time. This disentangles text content estimation from speech characteristic generation, markedly improving intelligibility and naturalness on challenging, in-the-wild datasets LRS2 and LRS3 compared to recent baselines. Extensive evaluation shows LipVoicer nearly matches ground truth metrics on human and machine assessments, and ablative studies demonstrate that ASR-guided text guidance at inference is critical, dropping WER from ~21% to over 86% without it. The system is modular and allows substitution of lip-reader and ASR for improvements. However, it relies on heavy models and offline generation, limiting deployment on mobile or real-time scenarios, and poses risks of speech manipulation if malicious text is injected. Overall, LipVoicer sets a new standard for intelligible and natural lip-to-speech synthesis on complex data, useful as a reference architecture for future work focused on intelligibility rather than real-time constraints.

### Why it matters

Shows the crucial role of leveraging text inferred by lip-reading at inference as classifier guidance to overcome intrinsic ambiguity in lip motion, resulting in state-of-the-art intelligibility and naturalness in lip-to-speech synthesis for in-the-wild data.

### Prior state of the art

Prior lip-to-speech systems map silent lip video directly to audio or audio features, often producing ambiguous or unintelligible speech on in-the-wild datasets with diverse speakers and open vocabulary.

### What changed

LipVoicer incorporates inferred text from a lip-reading network at inference time as guidance for diffusion-based speech generation, reducing ambiguity and improving intelligibility and synchronization.

### Position in the field

A top-tier recent lip-to-speech synthesis achieving near ground-truth intelligibility and naturalness on unconstrained in-the-wild datasets, setting a new state-of-the-art for video-to-speech intelligibility over prior direct regression or unit-based methods.

### Practical value

Highly practical as a reference architecture for generating intelligible speech from silent videos with unconstrained vocabulary in challenging real-world conditions; less suitable for mobile or real-time applications currently.

### Advanced

text_guidance; intelligibility; in_the_wild_video_to_speech

### Unresolved

real-time deployment; misuse mitigation; dependence on lip-reader quality

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | silent lip video |
| Sensor | camera |
| Body site | lip |
| Output | speech-audio |
| Vocabulary type | open |
| Vocabulary size | open vocabulary including hundreds of speakers' utterances as in LRS2/LRS3 datasets |
| Metrics and results | Human mos scores for intelligibility, naturalness, quality, synchronization with mean and confidence intervals; objective automatic speech recognition word error rate (WER), non-intrusive speech quality and intelligibility DNSMOS and STOI-Net; SyncNet audio-visual synchronization metrics (LSE-C, LSE-D). Exact WER on LRS3 test goes from 21.4% with LipVoicer to 86.2% without ASR guidance; LipVoicer outperforms baselines Lip2Speech, VCA-GAN, SVTS in both human and objective metrics. |
| Evaluation protocol | Human mean opinion scores (MOS) on intelligibility, naturalness, quality, synchronization; objective metrics including WER, DNSMOS, STOI-Net, SyncNet metrics on LRS2 and LRS3 test sets. |

### Limits

- **Technical:** Depends on quality and performance of large pretrained lip-reader and ASR models plus heavy diffusion model; generation is offline with hundreds of inference steps limiting real-time use; quality degrades with less accurate lip-readers; risk of adversarial misuse via text injection.
- **Evaluation:** Evaluations are strong on benchmark datasets LRS2 and LRS3 but not aimed at real-time, mobile, or on-device use; reliance on quality lip-reader and ASR.
- **Deployment:** Heavy model stack including lip-reader, ASR, and diffusion; no focus on low-latency or on-device deployment; recognized risk of misuse from malicious text injection.
- **Scope of this review:** Lip-to-speech from silent lip video only; does not handle audio/video noisy inputs or multimodal fusion beyond lip video and inferred text guidance.

### Evidence

- The paper proposes LipVoicer, which first predicts text from lip video and then uses that text to guide diffusion-based speech generation. (Abstract)
- LipVoicer combines lip-reading, diffusion generation, classifier-free guidance, and ASR classifier guidance in one inference loop, a novel system design in lip-to-speech. (4)
- LipVoicer is evaluated on LRS2 and LRS3, in-the-wild audiovisual datasets with hundreds of speakers and open vocabulary; evaluation includes human MOS and objective WER, DNSMOS, STOI-Net, and synchronization with SyncNet metrics. (5)
- On LRS3 ablation, removing ASR guidance increases WER from 21.4% to 86.2%, showing that text guidance is essential for intelligibility; LipVoicer outperforms baselines Lip2Speech, VCA-GAN, SVTS in human and objective evaluations. (5)
- The stack depends on a lip-reader, an ASR model, and a relatively heavy diffusion model; inference is not real-time and deployment on mobile or low-latency platforms is not claimed or targeted; misuse risk from injected text at inference is acknowledged. (6)
- LipVoicer requires a heavy model stack for inference and does not claim real-time or on-device deployment readiness; social misuse risks from incorrect or malicious text guidance are noted but not addressed here. (6)
- LipVoicer achieved human mean opinion scores near ground truth on LRS2 and LRS3 on intelligibility (3.44-3.53 vs 4.33-4.38), naturalness, quality, and synchronization, outperforming recent baselines. (5)
- LipVoicer uses pretrained lip-reader Ma et al. (2023) with WER 14.6% on LRS2 and 19.1% on LRS3 to generate text at inference time; uses a modified ASR Burchi & Timofte (2023) fine-tuned on noised data for classifier guidance. (5)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
