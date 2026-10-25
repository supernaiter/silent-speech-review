# EEG-Based Imagined Speech Decoding Using a Hybrid CNN-SNN Architecture

Fatima Shalhoub, Mariam Al Mawla, Kabalan Chaccour, Iván López-Espejo, Hoda Fares  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2607.03844)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text+summary

Hybrid CNN-SNN classifier for five-class EEG imagined speech; reports 80.13% accuracy and 80.14% F1 in offline subject-dependent evaluation, about 98 ms GPU prediction time per trial.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Existing 64-channel scalp EEG |
| Task | Imagined speech command classification |
| Vocabulary | 5 words/phrases (Hello, Help me, Stop, Thank you, Yes) |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 80.13% accuracy, 5 classes, subject-dependent, validation subset |

**Limitations.** Evaluated on the validation subset, not the hidden test set; no per-subject results, uncertainty or matched CNN/SNN ablation; power and online use unmeasured.

## Full review

### In short

Promising five-class EEG classification at a reported 80.13% accuracy; independent replication, a matched spiking ablation, and actual power and online tests remain necessary.

### Review

The useful contribution is a concrete hybrid classifier for a narrow imagined-speech task: temporal CNN features are processed by leaky-integrate-and-fire neurons, and five prompted words or phrases are selected by their output firing rates. The paper reports 80.13% accuracy and 80.14% F1 for a subject-dependent evaluation involving 15 healthy participants. These are not free-form text or speech synthesis results. The evaluation uses the original 750-trial validation subset as its test set because official test labels are unavailable; a further independent model-selection split is not described. Table II compares published scores, with a 9.94 percentage-point difference from the highest listed comparator, but the study provides neither a matched non-spiking ablation nor repeated-run or per-participant uncertainty. Consequently, the result motivates replication without establishing that spike dynamics themselves explain the gain. The reported 98 ± 3 ms prediction time is measured on a Tesla T4 GPU with prerecorded trials. It excludes a demonstrated live acquisition-to-feedback path, and the zero-phase preprocessing and symmetric convolutions need a causal redesign or explicit buffering analysis. No power consumption or neuromorphic-hardware result substantiates energy-efficiency claims. Reproduction also needs clarification of the input duration: Figure 2 labels 795 time samples, while the text states 256 Hz sampling and calls each trial two seconds; these descriptions do not reconcile directly. This is an interesting five-command EEG architecture study, with substantial gaps between offline benchmark accuracy and a practical silent communication interface.

### Why it matters

Introduces a reproducible-in-principle architecture hypothesis for combining learned EEG features with spiking temporal integration, while leaving causal attribution and deployment validation open.

### Prior state of the art

The paper compares existing EEG imagined-speech classifiers based on spectral features, CNNs, SPD geometry, and attention or transfer learning using previously published accuracy values.

### What changed

A CNN extracts a 64-dimensional temporal feature sequence, which is spike-encoded and classified by LIF layers using average output firing rates rather than a conventional dense decision head.

### Position in the field

Non-invasive imagined-speech EEG classification for small command vocabularies, distinct from articulatory SSI and continuous brain-to-speech synthesis.

### Practical value

A candidate research baseline for testing spiking decision heads under matched EEG preprocessing and participant splits.

### Advanced

Reported within-participant five-class accuracy and exploration of a spiking decision layer after convolutional feature extraction.

### Unresolved

Independent test-set replication, cross-participant and cross-session transfer, causal online operation, energy consumption, and the contribution of the SNN versus the CNN.

### Narrowed or regressed

No controlled regression established; deployment comparisons lack measured power, memory, or matched CNN inference costs.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | command-recognition |
| Input | Scalp electroencephalography (EEG) |
| Sensor | Existing 64-channel scalp EEG, international 10-20 placement, reported sampling frequency 256 Hz; amplifier and wearable configuration are not specified here. |
| Body site | brain |
| Output | labels |
| Vocabulary type | closed-set prompted words and phrases |
| Vocabulary size | 5 classes: Hello, Help me, Stop, Thank you, Yes. |
| Metrics and results | Author-reported accuracy 80.13% and F1 80.14%. Table II lists comparator accuracies 48.10%, 70.19%, 58.51%, 66.93%, and 69.00%; the largest listed comparator is 9.94 percentage points below the proposed result. Tesla T4 prediction time is approximately 98 ± 3 ms per trial, with an asserted real-time factor near 0.05 based on two-second trials. Accuracy/F1 uncertainty and the definition of the timing ± quantity are not specified. Results are not independently reproduced. |
| Evaluation protocol | Offline, subject-dependent five-class classification; reported mean accuracy and F1, literature comparison, and GPU prediction timing. |

### Limits

- **Technical:** The temporal spike-encoding rule is described qualitatively. Zero-phase forward-backward filtering and symmetric convolution padding use future samples within a trial. Figure 2 input length conflicts with the stated trial duration and sampling rate. Sparse activity, operation counts, memory, and power are unmeasured.
- **Evaluation:** Subject-dependent evaluation on the original validation subset; no results on the official hidden-label test subset. No per-subject scores, repeated-run uncertainty, confusion matrix, or matched CNN-only/SNN-only ablation is reported. Hyperparameter-selection separation is not specified. Table II imports literature results rather than rerunning all methods.
- **Deployment:** Offline prerecorded EEG and Tesla T4 GPU inference only; no wearable device, power measurement, live feedback, asynchronous detection, or clinical evaluation.
- **Scope of this review:** Five prompted English words or phrases from 15 healthy participants; no continuous transcription, acoustic reconstruction, patient study, or unseen vocabulary.

### Evidence

- The study uses 15 healthy participants and five imagined-speech classes from 64-channel EEG. It trains on 4,500 trials and evaluates on the original 750-trial validation subset, leaving the official unlabeled test subset unused. (Section III-A; PDF p. 3)
- Three temporal convolution layers produce 64-dimensional features, followed by spike encoding, a 32-neuron LIF hidden layer and five LIF outputs decoded by average firing rate. (Sections III-C1 and III-C2; Figure 2; PDF pp. 3-5)
- The subject-dependent setup reports mean classification accuracy 80.13% and F1 80.14%. Per-subject scores and accuracy confidence intervals are not reported. (Section IV; PDF p. 5)
- Table II compares previously published accuracies, including 70.19% for the highest listed alternative. There is no matched CNN-only ablation; reviewer assessment: the comparison does not isolate the effect of spiking neurons. (Section IV and Table II; PDF p. 5)
- Prediction time is approximately 98 ± 3 ms per trial on a Google Colab Tesla T4 GPU. The authors explicitly state that the study uses prerecorded EEG offline and requires real-time validation. (Section IV; PDF pp. 5-6)
- Figure 2 labels input shape (B, 64, 795), while Section III-A states 256 Hz sampling and Section IV describes two-second trials. Reviewer assessment: input length and timing assumptions need reconciliation. (Figure 2; Sections III-A and IV; PDF pp. 3 and 5)
- Channel z-score statistics are computed on training data and applied to test data. Training uses 350 epochs with different CNN and SNN learning rates; a separate hyperparameter-selection subset is not described. (Sections III-B and IV; PDF pp. 3 and 5)
- Preprocessing uses zero-phase forward-backward filtering and the convolutional feature extractor uses symmetric padding. Reviewer assessment: offline prediction time alone does not demonstrate causal streaming latency. (Sections III-B, III-C1 and IV; PDF pp. 3-5)
- The paper discusses low-power and neuromorphic potential but reports no measured power consumption or neuromorphic-hardware deployment; inference is timed on a GPU. (Table I; Sections IV and V; PDF pp. 3 and 5-6)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
