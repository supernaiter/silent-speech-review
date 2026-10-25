# Physiological Noise Augmentation Improves Non-Invasive Brain-to-Speech

Benjamin Ballyk, Teyun Kwon, Miran Özdogan, Oiwi Parker Jones  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2607.05165)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text+summary

Physiological noise augmentation (PNA) using ICA-derived artifact components for non-invasive MEG imagined-speech decoding; improves 10-class imagined digit accuracy, e.g. EEGNet 73.0% to 76.3% with 10-trial averaging.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | MEG with EOG and ECG reference sensors |
| Task | Imagined digit classification |
| Vocabulary | 10 digits |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | EEGNet accuracy 73.0% to 76.3% with PNA and 10-trial averaging, 10 classes |

**Limitations.** Single-subject MEG dataset only; requires recorded EOG/ECG reference channels; no unseen subjects, real-time or wearable tests.

## Full review

### In short

Introducing PNA, the paper advances non-invasive brain-to-speech decoding by creating artifact-informed augmentations via ICA, significantly improving imagined speech classification accuracy on MEG data when combined with trial averaging.

### Review

This paper presents Physiological Noise Augmentation (PNA), an innovative augmentation framework leveraging ICA to remix independent artifact components (ocular, cardiac) into cleaned MEG data for imagined speech decoding. PNA theoretically equivalates to anisotropic Jacobian regularization, penalizing model sensitivity to physiological noise directions, and empirically improves decoding accuracy by 4.7% absolute on the MegNIST dataset when combined with 10-trial averaging. The work advances non-invasive brain-to-speech decoding by explicitly modeling physiological noise for robustness rather than solely relying on input-level heuristics or artifact removal. Limitations include reliance on artifact reference channels and single-subject data. This method establishes a principled augmentation approach that addresses the signal-to-noise bottleneck partially and sets a template for artifact-aware learning in neural signal decoding.

### Why it matters

The key value is the principled use of artifact components for physiologically grounded data augmentation that enhances robustness and reduces trial repetition requirements, providing both theoretical grounding and clear empirical benefits in MEG imagined speech decoding.

### Prior state of the art

Non-invasive brain-to-speech decoding relied on multi-trial averaging to improve SNR and heuristic input-level augmentations; physiological artifacts were viewed as nuisances to be removed via ICA before decoding; prior work did not exploit artifact component remixing for augmentation.

### What changed

Proposes a new artifact-aware augmentation framework that integrates ICA-based artifact component remixing, previously unused in brain-to-speech decoding, to explicitly impose invariance to physiological noise.

### Position in the field

advances artifact-aware robust decoding in non-invasive brain-to-speech research, moving beyond heuristic augmentation toward physiologically grounded regularization frameworks

### Practical value

Provides a method that could improve decoding accuracy and reduce patient repetition burden, but limited by artifact reference data requirement and dataset scope.

### Advanced

Moved robustness to task-irrelevant physiological artifacts by artifact-aware augmentation; reduced trial repetition requirements for decoding accuracy via complementary use of multi-trial averaging.

### Unresolved

Unclear whether artifact invariance generalizes to unseen subjects, broader vocabularies, or other neural modalities beyond MEG.

### Narrowed or regressed

No regression in decoding accuracy or interpretability reported.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-recognition |
| Input | magnetic |
| Sensor | magnetoencephalography (MEG) with electrooculography (EOG) and electrocardiography (ECG) reference sensors |
| Body site | brain |
| Output | labels |
| Vocabulary type | digits |
| Vocabulary size | 10 |
| Metrics and results | Decoding accuracy on the 10-class imagined digit classification task; e.g., EEGNet accuracy improves from 73.0% to 76.3% with PNA and 10-trial averaging. |
| Evaluation protocol | Quantitative evaluation with cross-validation on the MegNIST dataset using accuracy metrics; multi-trial averaging simulated; no reported real-time tests. |

### Limits

- **Technical:** Requires artifact reference signals during recording; evaluated only on single-subject MEG dataset; no generalization or real-time tests.
- **Evaluation:** Evaluation limited to a single-subject imagined digit classification task on a MEG dataset; no multi-subject or multi-vocabulary evaluation; no tests under real-world deployment conditions or unseen subjects/words.
- **Deployment:** Current method requires recorded artifact reference channels (EOG, ECG) for ICA component identification, limiting applicability to such datasets; studies only single-subject MEG data; not demonstrated in real-time or on mobile/wearable hardware.
- **Scope of this review:** Evaluation limited to single-subject MEG imagined digit classification with known artifact references; excludes multi-subject, other modalities, real-time, or clinical deployment contexts.

### Evidence

- We introduce PNA, an augmentation framework that isolates artifact-related independent components (ocular and cardiac activity) and reinjects scaled artifact projections into cleaned data to generate realistic label-preserving samples, improving decoding accuracy and theoretical regularization insight on the MegNIST MEG dataset. (Abstract, Sections 1,3,4,5)
- PNA differs from prior augmentation methods by utilizing ICA-based decomposition to remix physiological artifacts with empirical distributions of artifact-to-clean ratio for augmentation, approximating anisotropic Jacobian regularization. (Sections 3.1, 3.2)
- PNA with 10-trial averaging improves EEGNet decoding accuracy by 4.7 percentage points absolute over real data alone, achieving 76.3% accuracy on the MegNIST imagined-digit classification task. (Section 4.1, Tables 1 and 2)
- PNA relies on artifact reference signals (EOG, ECG) recorded during acquisition to identify artifact components, limiting applicability; only tested on a single-subject MEG dataset with a limited vocabulary of digits; no evaluation on unseen words or multi-subject generalization. (Section 5)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
