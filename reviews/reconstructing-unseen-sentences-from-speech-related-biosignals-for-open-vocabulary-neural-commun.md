# Reconstructing Unseen Sentences from Speech-related Biosignals for Open-vocabulary Neural Communication

Deok-Seon Kim, Seo-Hyun Lee, Kang Yin, Seong-Whan Lee  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2510.27247)

**Section:** [Surface EMG](../README.md#surface-emg) · **Review basis:** full_text+summary

Reconstructs held-out English sentences from EEG and face/neck EMG with personalized models; overt EEG+EMG phoneme accuracy is 48.58% (EEG alone 36.83%) versus an 11% baseline.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 128-channel actiCAP EEG plus 10 face/neck EMG channels |
| Task | Held-out sentence reconstruction (audio and phonemes) |
| Vocabulary | 474 cued English sentences; 39 phonemes plus silence |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Overt phoneme accuracy 48.58% EEG+EMG, 36.83% EEG, held-out sentences, baseline 11% |

**Limitations.** Strongest evidence is overt/whispered, imagined results are from a representative subject, CER only for examples, and silent targets use overt audio.

## Full review

### In short

Held-out sentence reconstruction is demonstrated in personalized EEG/EMG experiments, but the strongest aggregate evidence is overt/whispered phoneme decoding—not unrestricted imagined-speech communication.

### Review

The useful contribution is a subject-specific test of whether learned phoneme and acoustic mappings can reconstruct sentence texts absent from training. Fifteen healthy participants provide 474 English sentences per mode, split into 444 training and 30 test sentences, and inference is explicitly described as receiving neither target text nor recorded audio. Across participants, EEG+EMG increases phoneme accuracy from 36.83% to 48.58% for overt speech and from 30.54% to 40.97% for whispered speech. These are phoneme scores, not sentence recognition rates; whispered acoustic RMSE remains 0.58 and MCD is 4.73 versus 4.71 for EEG alone. The two low-CER examples are selected sentences from one subject, not a corpus-wide intelligibility result. For imagined speech, Table V reports 31.35% phoneme accuracy for both delta and high-gamma EEG from a representative subject, not a 15-person mean. The additional patient experiment uses attempted overt speech in one person, with EEG-only/combined phoneme accuracy of 42.85%/45.63%, and cannot establish silent clinical communication. Personalized models, overt-audio supervision, fixed speech-mode order, limited artifact controls and unavailable supplementary detail keep this an offline proof of concept. Held-out sentence texts are a meaningful step beyond closed sentence classes, but novel words, spontaneous inner speech, real-time use and general clinical benefit remain unverified.

### Why it matters

A concrete held-out-sentence and modality-comparison protocol that separates phoneme prediction from acoustic reconstruction; its value is experimental evidence about biosignal reconstruction, not ready-to-use silent conversation.

### Prior state of the art

The paper situates itself against non-invasive EEG studies dominated by predefined word/sentence categories, while acknowledging earlier unseen-word reconstruction and held-out-sentence EEG-to-text work.

### What changed

Extends the reconstruction question to disjoint sentence texts with phoneme/acoustic prediction and compares available biosignal modalities, rather than demonstrating unrestricted thought decoding or a new general-purpose language interface.

### Position in the field

Non-invasive, speaker-dependent biosignal-to-speech reconstruction with held-out sentence texts; a relevant SSI research step with much narrower validation than unrestricted neural conversation.

### Practical value

Offers a protocol for comparing acoustic and phoneme objectives and the added value of EMG where muscle activity is available. Benefit for routine assistive communication remains unknown.

### Advanced

Subject-specific held-out sentence reconstruction beyond repeated sentence classes; explicit EEG versus EEG+EMG comparison for overt and whispered speech; exploratory attempted-overt evaluation in one person with ataxic dysarthria.

### Unresolved

Unseen users and sessions; truly novel lexical words; spontaneous imagined communication; neural specificity versus muscle/cue contamination; whole-test intelligibility; online latency and usability; wider clinical benefit.

### Narrowed or regressed

Adding ten face/neck EMG channels increases sensing burden relative to EEG alone. Whispered EEG+EMG has MCD 4.73 versus 4.71 for EEG alone and the same rounded RMSE 0.58, so not every reconstruction metric improves.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | Reconstruct cued, held-out English sentences from overt/whispered/imagined biosignals, with primary aggregate comparison in overt and whispered conditions. |
| Input | High-density scalp EEG, alone or channel-concatenated with face/neck surface EMG; overt audio and sentence text supply training targets, not inference inputs. |
| Sensor | Brain Vision/Recorder at 1000 Hz; Standard 128-channel actiCAP with FCz reference; ten EMG channels on face/neck; synchronized 44100-Hz microphone. Network input is described as 127 EEG plus ten EMG channels; the channel-count reconciliation is not explicit in the main text. |
| Body site | Scalp for EEG; face and neck for EMG. |
| Output | Predicted acoustic features and 40-class phoneme sequences; HiFi-GAN synthesized audio followed by DeepSpeech text for evaluation. |
| Vocabulary type | Cued English sentences with nonoverlapping training/test sentence texts; open sentence-sequence output within a fixed phoneme inventory, not verified unrestricted lexical generalization. |
| Vocabulary size | 39 phoneme classes plus silence; 474 English sentence stimuli for healthy participants and 155 attempted-overt patient stimuli. Number of distinct lexical words is unknown. |
| Metrics and results | Healthy-participant mean phoneme accuracy: overt EEG 36.83%, EEG+EMG 48.58%; whispered EEG 30.54%, EEG+EMG 40.97%. In that order, RMSE 0.50/0.46 and 0.58/0.58; MCD 4.18/3.81 and 4.71/4.73; F1 0.34/0.47 and 0.16/0.24. Authors use an 11% most-frequent-silence baseline. Table II selected-example CER: overt 0.18 and 0.36, whispered 0.50 and 0.40, all EEG+EMG. Table V representative-subject imagined delta/high-gamma phoneme accuracy: both 31.35%, with RMSE 0.65/0.71 and MCD 5.33/5.72. Single-patient attempted-overt EEG/EEG+EMG phoneme accuracy: 42.85%/45.63%. |
| Evaluation protocol | Offline, personalized held-out sentence reconstruction with EEG-only and EEG+EMG comparisons; exploratory single-patient attempted-overt reconstruction and representative-subject frequency/source analyses. |

### Limits

- **Technical:** Whispered/imagined training targets use corresponding overt audio, not contemporaneous silent acoustic ground truth. Filtering and common-average referencing alone do not establish neural specificity or exclusion of muscle artifacts; fixed overt→whispered→imagined order may carry echoic traces, acknowledged by authors. The input/feature/checkpoint details and phoneme scoring require clarification. Source localization is descriptive, not causal evidence for a speech mechanism.
- **Evaluation:** Main aggregate metrics are 15 subject means over 30 test sentences. The text reports paired Wilcoxon p<0.0001 for specified modality improvements, but confidence intervals, exact p values, multiple-comparison handling and error-bar definition are not specified in the main text. CER is shown only for two examples from one subject, not an overall test rate. Fig. 7 and Table V concern a representative subject; supplementary material is referenced but absent from the reviewed 11-page PDF.
- **Deployment:** High-density cap plus optional face/neck electrodes, individual training and trial segmentation. Button-controlled cued acquisition; no autonomous start/stop, mobile use, walking, longitudinal deployment or measured end-to-end latency reported.
- **Scope of this review:** Reviewed all 11 pages of arXiv v1, including main-text figures/tables and references; key pipeline, aggregate and frequency tables visually checked. Referenced supplementary tables/figures are not contained in this PDF and were not verified. No independent experimental reproduction or verification of external code/data availability.

### Evidence

- Fifteen healthy adults perform 474 English sentences in fixed overt, whispered and imagined order; 444 training and 30 test sentences do not overlap. Only the final repeated attempt is retained. (p.2, II.A Data Acquisition; Fig.1)
- Acquisition uses a 128-channel actiCAP, ten face/neck EMG channels at 1000 Hz and synchronized 44100-Hz audio; the network description later specifies 127 EEG input channels. (p.2, II.A; p.4, III.C)
- The decoder is personalized per subject. Corresponding overt recordings supply whispered/imagined acoustic targets, while inference explicitly receives neither recorded audio nor target sentence text. (p.3, III.A Framework and Fig.2)
- Three ConvBlocks and a Bi-GRU predict acoustic features and phonemes; HiFi-GAN generates audio and DeepSpeech produces text. Silent-mode training combines phoneme-informed DTW with CTC rather than demonstrating a new sensor or deployment platform. (pp.3–4, III.A–C; Fig.2; equations 1–6)
- Across 15 participants, overt phoneme accuracy increases from EEG 36.83% to EEG+EMG 48.58%, and whispered accuracy from 30.54% to 40.97%. These are phoneme metrics, not sentence accuracy. (p.5, IV.A and Fig.3(a))
- Overt EEG/combined RMSE is 0.50/0.46, MCD 4.18/3.81 and F1 0.34/0.47. Whispered values are RMSE 0.58/0.58, MCD 4.71/4.73 and F1 0.16/0.24; combined sensing does not improve every whispered metric. (p.5, IV.A and Fig.3(b–d))
- Each subject contributes an average over 30 test sentences; authors report paired Wilcoxon p<0.0001 for all overt metrics and whispered phoneme accuracy/F1. The 11% baseline is the most frequent silence class, not a shuffled temporal null model. (p.5, IV.A and Fig.3 caption)
- CER 0.18/0.36 for overt and 0.50/0.40 for whispered speech are two EEG+EMG examples from one representative subject, not overall test-set character error rates or human-listener intelligibility. (p.5, Table II; p.7, IV.A continuation)
- One 66-year-old man with ataxic dysarthria provides 155 attempted-overt sentences split 145/10. EEG/combined phoneme accuracy is 42.85%/45.63%; this is not a patient imagined-speech test or evidence of broad clinical benefit. (p.7, IV.B Sentence Reconstruction in a Speech-impaired Patient)
- Table V is explicitly from a representative subject: imagined delta and high-gamma EEG both reach 31.35% phoneme accuracy. Delta/high-gamma RMSE is 0.65/0.71 and MCD 5.33/5.72; these are not 15-person aggregate imagined-speech scores. (pp.8–9, IV.E; p.9, Table V caption and rows)
- Fig.7 relates sentence length and phoneme accuracy in a representative subject (PCC −0.459 overt, −0.623 whispered). These correlations do not establish causation; W-score panel labels/caption and text require implementation reconciliation. (pp.7–8, IV.D; p.8, Fig.7 and Table IV)
- sLORETA maps at 1, 1.25 and 1.5 seconds describe estimated activity from a representative subject. They do not establish that reconstructed content is causally driven by the highlighted cortical areas. (p.5, III.F; pp.8–9, IV.E and Fig.8)
- Authors acknowledge that the fixed overt-to-whispered-to-imagined order may introduce echoic traces. Main preprocessing describes filters and common-average referencing, not a control proving independence from residual muscle activity. (pp.2–3, II.B; p.10, V.E continuation)
- Disjoint sentence texts support unseen-sentence evaluation, but the main text does not report lexical word overlap, cross-user/session tests, whole-test CER or online latency; broad unrestricted neural communication remains unverified. (pp.2–4, II.A and III.A–D; pp.9–10, V.A and V.E)
- Training uses AdamW, learning rate 1e-3, weight decay 1e-5, cosine scheduling, at most 200 epochs, early stopping, GRU dropout 0.1 and length-2048 batching. Validation allocation is not specified in the main training description. (p.4, III.C Training Details)
- The conclusion links reconstructed audio and a toy dataset from one subject. Supplementary figures/tables referenced throughout are absent from this 11-page PDF; completeness of external data/code and those supplements was not verified in this review. (p.10, VI Conclusion; pp.2,5,7–8 supplementary references)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
