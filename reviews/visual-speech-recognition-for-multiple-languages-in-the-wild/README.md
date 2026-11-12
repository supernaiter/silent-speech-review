# Visual speech recognition for multiple languages in the wild

Pingchuan Ma, Stavros Petridis, Maja Pantic  
Nature Machine Intelligence 4(11), 930-939 2022 · [DOI](https://doi.org/10.1038/s42256-022-00550-z) · [arXiv](https://arxiv.org/abs/2202.13084)

**Section:** [Lip & face video](../../README.md#lip--face-video) · **Review basis:** full_text

A structured review of *Visual speech recognition for multiple languages in the wild* (Pingchuan Ma et al., Nature Machine Intelligence 4(11), 930-939 2022) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Multilingual lipreader using auxiliary feature-prediction losses and time masking; public-data results of 25.5% WER on LRS2, 31.5% on LRS3 and 8.0% CER on Mandarin CMLR.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Camera (face/lip video) |
| Task | Visual speech recognition (lipreading) |
| Vocabulary | Open vocabulary; English, Mandarin, Spanish, Italian, Portuguese, French |
| Speaker | Speaker-independent |
| Session | Not applicable |
| Online / offline | Offline |
| Key result | 25.5% WER LRS2, 31.5% WER LRS3, 8.0% CER CMLR (best of ten runs) |

**Limitations.** Vocalized in-the-wild video only; silent speech untested; small non-English test sets and offline evaluation.

## Full review

### In short

Careful VSR engineering that reaches strong multilingual lipreading with public data only.

### Review

The paper argues that design choices, not just data scale, drive VSR performance. A Conformer hybrid CTC/attention lipreader is improved with prediction-based auxiliary tasks (regressing frozen ASR and VSR features), time masking, tuned batching and a stronger language model. Using public data only, it reports 25.5% best WER on LRS2 and 31.5% on LRS3, 8.0% CER on Mandarin CMLR and 43.9% WER on Spanish CMU-MOSEAS, plus gains in Italian, Portuguese and French TEDx subsets. Reporting mean and standard deviation over ten runs is a welcome rigor step. The paper explicitly lists silent and Lombard speech as largely unexplored, so its value for SSI is as a strong multilingual visual backbone rather than as silent-speech evidence.

### Why it matters

Shows that auxiliary feature-prediction losses and augmentation let public-data lipreaders compete with systems trained on far larger private corpora, across several languages.

### Prior state of the art

Best English VSR results came from models trained on thousands to tens of thousands of hours of non-public data, and non-English VSR was weak.

### What changed

Adds prediction-based auxiliary tasks, time masking and tuned training to a Conformer CTC/attention VSR model, and extends evaluation to Mandarin, Spanish, Italian, Portuguese and French.

### Position in the field

Major VSR reference for multilingual lipreading; background for camera-based SSI.

### Practical value

Strong reusable recipe and pretrained models for multilingual visual speech front-ends.

### Advanced

multilingual_vsr; training_recipe; evaluation_rigor

### Unresolved

Silent and Lombard speech; accent and demographic bias; lipreading robustness to pose, lighting and resolution

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-recognition |
| Input | video |
| Sensor | camera (in-the-wild video datasets) |
| Body site | face; lip |
| Output | text |
| Vocabulary type | open vocabulary, multilingual |
| Vocabulary size | open vocabulary |
| Metrics and results | Best WER 25.5% LRS2 and 31.5% LRS3 (1,459 h public data); CER 8.0% on CMLR Mandarin; WER 43.9% on CMU-MOSEAS Spanish; mean±std over ten runs reported (e.g., LRS3 32.1±0.3) |
| Evaluation protocol | public benchmarks in English, Mandarin, Spanish, Italian, Portuguese and French; ablations; ten runs per experiment |

### Limits

- **Technical:** Gains shrink as training data grow; Mandarin and Spanish gains smaller than English, attributed to language mismatch in auxiliary models.
- **Evaluation:** Benchmarks are vocalized in-the-wild videos; small non-English test sets make close comparisons uncertain; AVSpeech labels are machine-generated.
- **Deployment:** Offline evaluation only; authors flag dual-use surveillance risk and call for regulation before commercialization.
- **Scope of this review:** Visual speech recognition of vocalized speech; silent speech not evaluated.

### Evidence

- The paper presents a VSR model improved with prediction-based auxiliary tasks, time masking and hyperparameter optimization, arguing design choices matter as much as data size. (Abstract; Methods)
- Trained on 1,459 h of public data, the model reaches 25.5% best WER on LRS2 (25.8±0.4 mean) and 31.5% on LRS3 (32.1±0.3 mean). (Tables 1 and 2 (arXiv v2))
- On CMLR Mandarin the model reaches 8.0% best CER, versus 22.0% for the prior method listed; on CMU-MOSEAS Spanish it reaches 43.9% best WER. (Tables 3 and 4 (arXiv v2))
- Ablations show that removing both auxiliary tasks and time masking raises WER from 29.5 to 35.0 on LRS2 and from 35.8 to 39.1 on LRS3. (Table 5 (arXiv v2))
- The challenges section notes that silent speech and Lombard speech remain largely unexplored and that person-independence, pose and non-English accents are open problems. (Section 2.2 (arXiv v2))

## More reviews in Lip & face video

- [FastLTS: Non-Autoregressive End-to-End Unconstrained Lip-to-Speech Synthesis](../fastlts-non-autoregressive-end-to-end-unconstrained-lip-to-speech-synthesis/) (2022). FastLTS is a non-autoregressive end-to-end lip-to-speech system that makes unconstrained synthesis substantially faster without obvious quality loss, evaluated on Lip2Wav and GRID.
- [Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction](../learning-audio-visual-speech-representation-by-masked-multimodal-cluster-prediction/) (2022). Self-supervised audio-visual pretraining (masked multimodal cluster prediction) enabling lipreading at 32.5% WER on LRS3 with only 30 h of labels, and 26.9% with 433 h plus self-training.
- [Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild](../lip-to-speech-synthesis-for-arbitrary-speakers-in-the-wild/) (2022). VAE-GAN lip-to-speech synthesis for arbitrary speakers in the wild; holds up on unconstrained LRW/LRS2, and multi-speaker pretraining with 5 h adaptation nearly matches a 20 h single-speaker model.
- [Multi-modality Associative Bridging through Memory: Speech Sound Recollected from Face Video](../multi-modality-associative-bridging-through-memory-speech-sound-recollected-from-face-video/) (2022). Memory-based cross-modal bridging recalls audio representations from face video, applied to word-level lip reading (LRW/LRW-1000) and speaker-dependent GRID speech reconstruction.
- [SVTS: Scalable Video-to-Speech Synthesis](../svts-scalable-video-to-speech-synthesis/) (2022). SVTS shows a simple spectrogram predictor with a pretrained vocoder outperforms prior complex video-to-speech models and scales to large datasets such as LRS3+VoxCeleb2.
- [VCVTS: Multi-speaker Video-to-Speech synthesis via cross-modal knowledge transfer from voice conversion](../vcvts-multi-speaker-video-to-speech-synthesis-via-cross-modal-knowledge-transfer-from-voice-conversion/) (2022). VCVTS performs multi-speaker video-to-speech synthesis by transferring knowledge from voice conversion, with speaker control from reference speech, on GRID and LRW.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
