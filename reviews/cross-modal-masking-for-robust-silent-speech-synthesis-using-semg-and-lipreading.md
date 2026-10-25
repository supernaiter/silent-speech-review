# Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading

Eder del Blanco, David Gimeno-Gómez, Eva Navas, Carlos-D. Martínez-Hinarejos, Inma Hernáez  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2606.09667)

**Section:** [Surface EMG](../README.md#surface-emg) · **Review basis:** full_text+summary

Silent speech synthesis fusing sEMG and lipreading with cross-modal masked training, improving performance and robustness to modality degradation over monomodal baselines.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 8 bipolar face/neck sEMG sensors plus RGB lip video |
| Task | Speech synthesis from sEMG and video |
| Vocabulary | Spanish sentences; about 30 phoneme classes |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Not reported |

**Limitations.** Limited-vocabulary Spanish data; adaptation to laryngectomized users limited; no real-time, wearable or spontaneous-speech evaluation.

## Full review

### In short

The paper advances silent speech synthesis by leveraging masked training to robustly fuse electromyography and lipreading, showing improved performance and resilience, but adaptation to laryngectomized users remains challenging.

### Review

This paper makes a significant contribution to silent speech interface research by proposing a masked multimodal speech synthesis system that robustly integrates surface electromyography and lipreading signals. The approach addresses prior gaps by improving performance in multi-speaker silent speech synthesis and introducing temporal adaptive masking during training to enhance robustness against sensor noise and modality degradation. The authors provide extensive experimental validation on a Spanish dataset including laryngectomized and laryngeal speakers, showing substantial reductions in word error rates and complementary modality contributions at the phonemic level. However, the study reveals challenges in adapting to post-laryngectomy speakers due to variability and speech production differences, highlighting an important future direction. Overall, this work advances the SSI field by demonstrating the benefits and necessity of robust multimodal fusion strategies and sets a foundation for practical silent speech restoration systems, though further progress is needed for clinical deployment and generalization.

### Why it matters

Confirms that masked multimodal integration of sEMG and lipreading improves silent speech synthesis robustness and accuracy, while emphasizing that clinical adaptation requires addressing speaker variability and articulation differences.

### Prior state of the art

Prior work explored unimodal silent speech interfaces using either sEMG or lipreading; multimodal combinations of sEMG and lipreading were limited to classification tasks and mostly in audible speech conditions; masking strategies used mainly in audio-visual speech recognition for enhancing robustness but not extensively for silent speech synthesis.

### What changed

First use of masked multimodal training combining sEMG and lipreading for continuous silent speech synthesis with detailed evaluation showing improved WER and phoneme accuracy and robustness under modality degradation and sensor failure simulations.

### Position in the field

Intermediate-advanced position; builds meaningfully on prior SSI methods by combining modalities under masked training and demonstrates robustness enhancements, but clinical deployment challenges remain.

### Practical value

Improves silent speech synthesis robustness; offers insights for practical SSI designs; yet needs further clinical validation and deployment advances.

### Advanced

Robustness to modality degradation improved; multimodal integration effectiveness advanced; phone-level articulatory class-level understanding enhanced.

### Unresolved

Generalization to unseen speakers beyond the dataset, full speaker-independent operation, efficacy for other languages remain unexplored.

### Narrowed or regressed

Adaptation to laryngectomized speakers shows performance challenges; unimodal masking degrades performance especially for sEMG.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction (silent speech synthesis) |
| Input | multimodal (sEMG and video lipreading) |
| Sensor | Surface electromyography 8 bipolar sensors placed on face and neck; video from RGB camera of speaker's lips |
| Body site | face; lip |
| Output | speech-audio (mel spectrograms) and phonetic labels |
| Vocabulary type | Phoneme-level labels, sentence-level utterances with limited vocabulary size not quantified extensively |
| Vocabulary size | Limited to about 30 phoneme classes plus silence token; test sentences phonemically balanced |
| Metrics and results | Phone Accuracy and Word Error Rate (WER) from Whisper v3, Structural Similarity Index (SSIM) for spectrogram quality; exact metrics provided with confidence intervals. |
| Evaluation protocol | Quantitative evaluation with monomodal baselines and multimodal models under controlled experimental conditions including masking ablations and bitrate/video degradation simulations. |

### Limits

- **Technical:** Single speaker generalization and adaptation to alaryngeal speakers limited; real-time inference not demonstrated; masking only validated in specific degradation regimes.
- **Evaluation:** Evaluation focuses on multi-speaker but limited vocabulary Spanish dataset; unseen words testing is limited; limited adaptation success for laryngectomized users; generalization to other languages or spontaneous speech not assessed.
- **Deployment:** Current study does not evaluate real-time deployment, mobile suitability, or wearable system practicalities; robustness to speaker variability especially post-laryngectomy remains a challenge.
- **Scope of this review:** Limited to Spanish language sentence data; limited number of laryngectomized subjects; no spontaneous speech or large vocabulary continuous speech tested.

### Evidence

- Main contributions: 1) Demonstrate sEMG and lipreading are complementary, fusion improves WER and phone accuracy; 2) critical role of temporal adaptive masking for robustness and generalization; 3) phone-level multimodal contributions with benefits for vowels and affricates. (Abstract, Introduction)
- Proposes masked multimodal speech synthesis framework integrating sEMG and lipreading with modality masking during training to improve robustness and performance under modality degradation and sensor failure conditions in continuous speech synthesis. (Introduction, Methods)
- Evaluation on multi-speaker Spanish ReSSInt dataset including audible and silent speech, with 8-channel sEMG and lip video, controlled studio conditions, with data splits ensuring text independence. Includes laryngeal and laryngectomized subjects for silent speech synthesis evaluation. (Section IV)
- Performance reported via Word Error Rate (WER), Phone Accuracy, Structural Similarity Index Measure (SSIM) for spectral reconstruction; WER improvements up to 14 absolute points over strongest unimodal baseline. (Section V)
- Adaptation to laryngectomized speakers remains an open challenge due to articulatory variability and lack of paired audible speech; multimodal fusion less beneficial for such speakers. (Section V)
- Robust multimodal fusion with masking promotes resilience to sensor noise, missing or degraded modality data, advancing towards real-world deployments, but real-time and mobile suitability not demonstrated yet. (Abstract, Conclusion)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
