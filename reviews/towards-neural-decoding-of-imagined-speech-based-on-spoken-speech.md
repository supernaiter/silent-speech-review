# Towards Neural Decoding of Imagined Speech based on Spoken Speech

Seo-Hyun Lee, Young-Eun Lee, Soowon Kim, Byung-Kwan Ko, Seong-Whan Lee  
arXiv / imported corpus page 2022 · [arXiv](https://arxiv.org/abs/2212.02047)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text

Transfers CSP+SVM models trained on spoken-speech EEG to imagined speech decoding; accuracy is slightly lower but not significantly different from direct training in a 5-class, 7-subject offline task.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 64-channel active-electrode EEG cap (10-10 system) |
| Task | Closed-set imagined word classification |
| Vocabulary | 5 words |
| Speaker | Speaker-dependent |
| Session | Same session |
| Online / offline | Offline |
| Key result | 26.8% accuracy (transfer) vs 30.5% direct, 5 classes, 7 subjects, p=0.098 |

**Limitations.** Small offline within-subject study with only 5 classes and 7 subjects; no online, cross-subject, or larger-vocabulary evaluation.

## Full review

### In short

Transfer of CSP+SVM models trained on spoken speech EEG to imagined speech achieves comparable, though slightly lower, accuracy within a limited 5-class, 7-subject offline EEG setup, with visual imagery control supporting specificity.

### Review

This work provides an initial quantitative assessment that classifiers trained on spoken speech EEG can transfer to imagined speech decoding with only a modest reduction in accuracy (26.8% transferred vs. 30.5% direct imagined speech, p=0.0983) on a small 5-class EEG dataset from seven subjects. A visual imagery control shows a significant drop in performance when transferred from spoken speech (p=0.022), supporting speech-specific neural feature overlap between spoken and imagined speech. However, the study is limited by small sample size, simple CSP+SVM models, offline analysis, and restricted five-class vocabulary, with no online or cross-subject tests. While promising, these results represent a preliminary baseline for transfer-based imagined speech EEG decoding rather than a fully deployable silent speech interface.

### Why it matters

The paper establishes a baseline showing that spoken speech EEG models can be transferred to imagined speech decoding with no statistically significant performance drop in a small, offline 5-class EEG task, introducing a novel transfer learning perspective with a visual imagery contrast to demonstrate speech specificity.

### Prior state of the art

Imagined-speech EEG decoding methods typically require direct training on limited imagined-speech data and rarely explore transfer from spoken speech EEG.

### What changed

The paper reframes imagined speech decoding as a transfer learning task from spoken speech EEG pretraining, with visual imagery decoding serving as a negative control to test speech specificity.

### Position in the field

An adjacent imagined-speech EEG transfer learning study rather than a direct silent speech interface or articulatory speech decoding study.

### Practical value

Provides a useful baseline for imagined speech EEG transfer approaches but lacks immediate applicability as a communication system due to limited vocabulary and offline evaluation.

### Advanced

Problem framing from direct imagined speech EEG training to cross-paradigm transfer learning; evaluation novelty by contrasting spoken speech transfer with visual imagery control.

### Unresolved

Cross-subject generalization, scalability to larger vocabularies, real-time or online decoding performance.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-recognition |
| Input | eeg |
| Sensor | 64-channel EEG cap with active electrodes placed according to international 10-10 system, referenced at FCz. |
| Body site | brain |
| Output | labels |
| Vocabulary type | closed-class word set |
| Vocabulary size | 5 classes |
| Metrics and results | Classification accuracy averaged across 7 subjects: imagined speech direct training 30.5% ± 4.9% vs. spoken speech transfer 26.8% ± 2.0% (p=0.0983); visual imagery direct 31.8% ± 4.1% vs. spoken speech transfer 26.3% ± 2.4% (p=0.022). Statistical tests include Kruskal-Wallis and bootstrap post-hoc analysis. |
| Evaluation protocol | 10-fold cross-validation within subjects; statistical significance tested using Kruskal-Wallis and bootstrap post-hoc analysis. |

### Limits

- **Technical:** Limited to offline 5-class classification with CSP+SVM; no deep learning or larger vocabulary; small cohort; no online or cross-subject tests.
- **Evaluation:** Evaluation limited to offline, within-subject 10-fold cross-validation on 7 subjects and 5 classes; no cross-subject or larger-vocabulary validation.
- **Deployment:** No online or real-time decoding implementation, no assistive user studies, no latency or practical deployment analysis.
- **Scope of this review:** Scope limited to preliminary within-subject EEG decoding using CSP+SVM on a 5-class vocabulary, not a comprehensive or scalable imagined speech system.

### Evidence

- In this paper, we performed a preliminary analysis to find out whether if it would be possible to utilize spoken speech electroencephalography data to decode imagined speech, by simply applying the pre-trained model trained with spoken speech brain signals to decode imagined speech. (Abstract)
- The classification performance of imagined speech data solely used to train and validation was 30.5 ± 4.9 %, the transferred performance of spoken speech based classifier to imagined speech data was 26.8 ± 2.0 %. (III. RESULTS)
- For visual imagery, solely trained performance was 31.8 ± 4.1 % and transferred performance of 26.3 ± 2.4 % with statistically significant difference p = 0.022. (III. RESULTS)
- The dataset involved 7 subjects and 5-class words/phrases recorded with a 64-channel EEG system. (II. MATERIALS)
- The model used was classical CSP+SVM on 64-channel EEG with only five classes and seven subjects, without online or cross-subject evaluation. (III. RESULTS)
- No online BCI, assistive-user study, latency analysis, or practical silent communication demonstration was performed. (IV. CONCLUSION)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
