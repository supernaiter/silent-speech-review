# Decoding speech perception from non-invasive brain recordings

Alexandre Défossez, Charlotte Caucheteux, Jérémy Rapin, Ori Kabeli, Jean-Rémi King  
Nature Machine Intelligence 5:1097-1107 2023 · [DOI](https://doi.org/10.1038/s42256-023-00714-5) · [arXiv](https://arxiv.org/abs/2208.12266)

**Section:** [Brain signals (EEG, MEG, intracortical)](../../README.md#brain-signals-eeg-meg-intracortical) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *Decoding speech perception from non-invasive brain recordings* (Alexandre Défossez et al., Nature Machine Intelligence 5:1097-1107 2023) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Contrastive deep model identifies heard 3 s speech segments from MEG/EEG across 175 participants; MEG top-1 up to 41% (best participants above 80%) among 1,000+ candidates, EEG much lower.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Non-invasive MEG (208/273 sensors) and EEG (60/128 channels) |
| Task | Speech perception decoding (segment retrieval) |
| Vocabulary | Natural stories and sentences; 190-1,842 candidate segments |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | MEG top-1 up to 41.3% average; top-10 up to 70.7%; EEG top-10 17.7-25.7% |

**Limitations.** Perception not production; retrieval from fixed candidates; MEG not wearable; EEG performance low.

## Full review

### In short

Contrastive MEG/EEG decoder identifies which 3 s speech segment a listener heard among 1,000+ candidates (up to 41% top-1 with MEG), but it decodes perception, not silent production.

### Review

This paper is often cited in non-invasive 'brain-to-speech' discussions, so the scope matters for an SSI review: participants passively listened to stories or sentences, and the model performs zero-shot segment identification, not generation. A shared convolutional brain module (spatial attention, participant-specific layer, dilated residual convolutions) is trained with a CLIP-style contrastive loss against wav2vec 2.0 representations, pooling four public datasets with 175 participants (two MEG, two EEG). With 3 s of MEG it reaches up to 41.3% top-1 on average and above 80% for the best participants, and top-10 up to 70.7%; EEG is much weaker (17.7% and 25.7% top-10). The contrastive objective and pretrained speech targets clearly beat mel-spectrogram regression, and MEG remains better than EEG after equalizing channels, participants and duration. Interpretability analyses suggest the decoder leans on lexical and semantic rather than acoustic-phonetic information. For SSI, the relevance is methodological (contrastive alignment to self-supervised speech features, cross-subject pooling); there is no production or silent-speech task, no generative output, and MEG is not wearable.

### Why it matters

Strong methodological template for aligning non-invasive brain signals with pretrained speech representations across many subjects; establishes MEG-vs-EEG performance gaps on perception.

### Prior state of the art

Non-invasive speech decoding mostly classified a handful of words or phonemes per subject with hand-crafted features.

### What changed

Contrastive alignment with wav2vec 2.0 targets and a shared multi-subject architecture, evaluated as zero-shot retrieval among 1,000+ segments across four datasets.

### Position in the field

Key non-invasive perception-decoding reference in the brain section; not evidence for silent speech production decoding.

### Practical value

Reusable architecture (later adapted in Brain2Qwerty) and evidence on how much data and subjects matter for non-invasive decoding.

### Advanced

Scale of non-invasive datasets pooled across subjects; retrieval among large candidate sets; contrastive speech-representation targets.

### Unresolved

Speech production / imagined speech; generative (open-ended) output; real-time use; wearable sensing.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | Zero-shot identification of the heard 3 s speech segment from MEG/EEG during passive listening. |
| Input | Non-invasive MEG and EEG. |
| Sensor | MEG (273 and 208 sensors) and EEG (128 and 60 channels) from four public datasets. |
| Body site | Brain (scalp-recorded MEG/EEG). |
| Output | Retrieved speech segment (label among candidates). |
| Vocabulary type | Natural stories and sentences in English and Dutch; segment retrieval among test-set candidates. |
| Vocabulary size | Candidate sets of 190 to 1,842 segments per dataset; 175 participants; about 163 hours total (19.2 + 6.7 + 80.9 + 56.2 h). |
| Metrics and results | MEG top-1 up to 41.3% average, >80% best participant; MEG top-10 up to 70.7% (Gwilliams) and 67.5 +/- 0.4 (Schoffelen); EEG top-10 25.7 +/- 2.9 (Brennan and Hale) and 17.7 +/- 0.6 (Broderick); random-model top-10 0.5-5.3%. Equalized MEG top-10 30.3%/31.7%, still above EEG. |
| Evaluation protocol | Offline, within-dataset held-out segments with a shared multi-subject model; ablations and interpretability regressions. |

### Limits

- **Technical:** Retrieval over a predetermined candidate set; decoding relies largely on semantic/lexical content; EEG performance is low.
- **Evaluation:** Perception only in healthy volunteers. Table 2 values are mean +/- s.d. across three random seeds; text describes them as participant averages. Introduction (1,500 segments) and abstract (1,000 segments) differ; test sets range from 190 to 1,842 segments.
- **Deployment:** MEG is not portable and uncommon clinically; real-time decoding not addressed.
- **Scope of this review:** Read the published Nature Machine Intelligence PDF via automated extraction; Extended Data figure values (ablations) not inspected. arXiv v2 checked for metadata.

### Evidence

- Four public datasets: Broderick 2019 EEG (19 participants, 19.2 h), Brennan and Hale 2019 EEG (33, 6.7 h), Schoffelen 2019 MEG (96, 80.9 h), Gwilliams 2022 MEG (27, 56.2 h); participants passively listened to speech. (Table 1; Methods, Datasets)
- From 3 s of MEG, top-1 segment identification reaches up to 41.3% on average and above 80% for the best participants. (Abstract; Results; Fig. 2a)
- Top-10 accuracy: MEG 70.7% (Gwilliams) and 67.5 +/- 0.4 (Schoffelen); EEG 25.7 +/- 2.9 (Brennan and Hale) and 17.7 +/- 0.6 (Broderick). (Table 2; Results)
- Brain module with spatial attention, participant-specific layer and dilated residual convolutions, trained with CLIP-style contrastive loss to wav2vec2-large-xlsr-53 representations. (Methods, Model)
- After equalizing channels, participants and duration, MEG top-10 dropped to 30.3% and 31.7% but still outperformed EEG (P < 1e-6). (Results, Is MEG really much better than EEG?)
- In Gwilliams, nearly 36% of test words were never presented during training, yet decoding still reached about 40%. (Discussion, Comparison with previous works)
- The study covers perception in healthy volunteers; the contrastive objective retrieves from a predetermined set; production decoding and a generative module are left to future work. (Discussion)

## More reviews in Brain signals (EEG, MEG, intracortical)

- [A high-performance neuroprosthesis for speech decoding and avatar control](../a-high-performance-neuroprosthesis-for-speech-decoding-and-avatar-control/) (2023). Text, voice and avatar from ECoG in one participant hold as a demonstration; sensor and decoder are standard, and an LM trained on the test pool inflates the text result.
- [A high-performance speech neuroprosthesis](../a-high-performance-speech-neuroprosthesis/) (2023). Large-vocabulary attempted-speech decoding in one participant holds; sensor, decoder and LM are now field standard, but the spiking attribution and cross-study ratios outrun the evidence.
- [An Accurate and Rapidly Calibrating Speech Neuroprosthesis](../an-accurate-and-rapidly-calibrating-speech-neuroprosthesis/) (2024). Intracortical speech BCI in a man with ALS reaches 9.8% WER on a 125,000-word vocabulary on day 2 and about 2.5% later, and was used for 248 hours of self-paced conversation over 8.4 months.
- [Towards Neural Decoding of Imagined Speech based on Spoken Speech](../towards-neural-decoding-of-imagined-speech-based-on-spoken-speech/) (2022). Transfers CSP+SVM models trained on spoken-speech EEG to imagined speech decoding; accuracy is slightly lower but not significantly different from direct training in a 5-class, 7-subject offline task.
- [A Convolutional Framework for Mapping Imagined Auditory MEG into Listened Brain Responses](../a-convolutional-framework-for-mapping-imagined-auditory-meg-into-listened-brain-responses/) (2025). Maps imagined auditory MEG (melodies and poems) to listened-response MEG; 8-condition classification reaches 50.7% (chance 12.5%), and calibrated cross-subject CNN beats shuffled controls, but correlations are small.
- [A cross-species neural foundation model for end-to-end speech decoding](../a-cross-species-neural-foundation-model-for-end-to-end-speech-decoding/) (2025). Introduces a cross-species self-supervised transformer encoder for Utah-array spiking data combined with audio-LLM end-to-end decoding, reporting state-of-the-art Brain-to-Text benchmark accuracy and imagined speech decoding.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
