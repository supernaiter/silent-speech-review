# Do EEG Foundation Models Transfer to Speech? A Benchmark on Overt and Imagined Speech Decoding

Owais Mujtaba Khanday, Mohamed Baha Ben Ticha, Sanae Belfrouh, Marc Ouellet, Jose A. Gonzalez-Lopez  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2607.27268)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text+summary

Benchmark of EEG foundation models versus conventional models for overt and imagined speech decoding on two datasets; general EEG pretraining shows no consistent advantage and word decoding stays near chance.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Existing 64-channel scalp EEG |
| Task | Speech-related EEG classification |
| Vocabulary | 60 Spanish words/categories (UGR); 5 words/phrases (BCIC) |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Speech-mode accuracy 61.3% (EEGNet) vs 33.3% chance; 60-word accuracy 1.7-2.9% vs 1.7% chance |

**Limitations.** Test-subject-informed early stopping weakens unseen-user claims; small cohorts and fixed vocabularies; no pretraining ablation, multiple seeds or online evaluation.

## Full review

### In short

General EEG pretraining shows no consistent speech-decoding advantage here; word decoding remains weak, and test-subject-informed early stopping limits the unseen-user claim.

### Review

This is a useful caution for EEG-based silent communication: scaling a model pretrained on general EEG does not automatically improve speech-content decoding. In UGR-MINDVOICE, EEGNet reaches 61.3% accuracy on overt/covert/rest classification, compared with 57.3% for LaBraM and 56.6% for EEGMamba. Those are speech-mode results, not word-recognition accuracy. On the 60-word task, all models reach only 1.7–2.9% accuracy against 1.7% chance. In BCIC2020-T3, within-subject balanced accuracy is 25.7–30.2% for five imagined words/phrases, but cross-subject results are 18.9–20.2%, with no model significantly above 20% chance. The value is therefore a controlled comparison and a warning against importing foundation-model expectations into SSI, rather than a usable communication system. A major qualification is that Section 2.4 uses the held-out test subject to choose when training stops and which checkpoint is evaluated. This is test-informed model selection even without gradient updates, so UGR-MINDVOICE results are not a clean estimate of performance on a wholly untouched user. The paper also relies on official BCIC validation data, leaves multiple training seeds to future work, and contains a 30-versus-60-class inconsistency between its dataset table and word results. The experiments support a lack of consistent advantage for these two models under the reported conditions; they do not prove that all EEG pretraining fails or that speech-specific pretraining would solve the problem.

### Why it matters

A speech-focused negative-result benchmark that separates mode detection from lexical decoding and makes the limited cross-subject utility of the tested models visible.

### Prior state of the art

The paper situates its comparison against general EEG pretraining successes on non-speech tasks and small-vocabulary imagined-speech studies. Such results do not by themselves establish transfer to speech production.

### What changed

Evaluates whether generic pretrained EEG representations help speech-related classification, with compact baselines and separate speech-mode, semantic-category, word-identity, within-subject, and cross-subject results. This is an adjacent imagined-speech BCI benchmark, not articulatory SSI recognition.

### Position in the field

An adjacent imagined-speech EEG/BCI benchmark with negative transfer findings; useful for SSI evaluation methodology but not a demonstrated articulatory or deployable silent-speech interface.

### Practical value

Helps researchers justify compact baselines and distinguish task difficulty and participant splits before spending resources on larger pretrained EEG models.

### Advanced

Separates speech-mode discrimination from lexical decoding, compares pretrained and compact models, and exposes the gap between within-subject and cross-subject imagined-speech classification.

### Unresolved

Independent model selection, repeat-seed robustness, speech-specific pretraining, natural continuous language, online use, and clinical generalization remain unresolved.

### Narrowed or regressed

No new interface capability is demonstrated; larger pretrained models add parameters without a consistent performance gain under the tested protocol.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-recognition |
| Input | eeg |
| Sensor | Existing 64-channel scalp EEG recordings. UGR-MINDVOICE uses a 10–20 layout, 1000 Hz acquisition and FCz reference, retaining 62 scalp channels after preprocessing; both datasets are resampled to 200 Hz. No new hardware. |
| Body site | brain |
| Output | labels |
| Vocabulary type | closed-set word/phrase and category labels; no open vocabulary |
| Vocabulary size | UGR results: 60 word classes, six semantic categories, and three speech modes; BCIC: five words/phrases. Table 1 inconsistently lists 30 for the UGR word-class count. |
| Metrics and results | UGR-MINDVOICE Table 2: speech-mode accuracy EEGNet 61.3% (95% CI 56.5–66.1), LaBraM 57.3% (53.0–61.7), EEGMamba 56.6% (51.8–61.3), versus 33.3% chance; EEGNet semantic-category accuracy 19.9% versus 16.7% chance; 60-word accuracy across models 1.7–2.9% versus 1.7% chance. BCIC2020-T3 Table 3, mean ± SD across 15 participants: within-subject balanced accuracy EEGNet 26.7 ± 3.3%, EEGConformer 30.2 ± 4.4%, LaBraM 27.7 ± 2.7%, EEGMamba 25.7 ± 2.5%; cross-subject range 18.9–20.2%, all p > 0.18 against 20% chance. These are reported results, not independently reproduced measurements. |
| Evaluation protocol | Offline UGR-MINDVOICE leave-one-subject-out evaluation over 14 participants, with test-subject-informed early stopping; semantic and word tasks pool overt and covert examples. BCIC2020-T3 reports within-subject and leave-one-subject-out results over 15 participants. Accuracy or balanced accuracy, weighted F1, Cohen kappa, and Wilcoxon tests are reported. |

### Limits

- **Technical:** Low lexical signal, small cohorts and fixed vocabulary; EEGConformer collapses to chance on all UGR tasks under this training configuration. No random-initialization ablation of the same foundation architectures establishes the causal benefit or harm of pretraining.
- **Evaluation:** Section 2.4 explicitly uses the held-out test subject for early stopping and restores the best checkpoint; although gradients do not use that subject, model selection is test-informed. BCIC results use the official validation split, not a hidden test set. Multiple training seeds are left to future work. Table 1 lists 3/6/30 classes whereas Table 2 and the word-analysis text use 60 word classes.
- **Deployment:** Only offline classification is reported. No online communication interface, assistive-user trial, walking test, latency, power consumption, or mobile execution measurement is provided.
- **Scope of this review:** Two EEG datasets, two foundation-model families, and finite-label offline tasks. Spanish lexical tasks combine overt and covert trials; they do not establish a silent-only continuous decoder. No free-form thought reading, audio reconstruction, or open-vocabulary communication is tested.

### Evidence

- UGR-MINDVOICE starts with 15 participants and 22 sessions; excluding subject 15 for ICA errors leaves 14 evaluated participants. BCIC2020-T3 contains 15 healthy participants and five imagined words/phrases. (Sections 2.1 and 2.3; Table 1; PDF p. 2)
- Table 2 reports speech-mode accuracy of 61.3% for EEGNet, 57.3% for LaBraM, and 56.6% for EEGMamba against 33.3% chance. This task distinguishes overt, covert, and rest states rather than individual words. (Section 3.1; Table 2; PDF pp. 3–4)
- The UGR-MINDVOICE 60-word task yields 1.7–2.9% accuracy across the six models against 1.7% chance. EEGNet reaches 2.8%, LaBraM 1.9%, and EEGMamba 2.9%. (Table 2, Word (60-cl) columns; PDF p. 4)
- BCIC2020-T3 within-subject balanced accuracy is 26.7 ± 3.3% for EEGNet, 30.2 ± 4.4% for EEGConformer, 27.7 ± 2.7% for LaBraM, and 25.7 ± 2.5% for EEGMamba; these are means and standard deviations over 15 participants for five classes. (Table 3, Within-subject columns and caption; PDF p. 4)
- BCIC2020-T3 cross-subject balanced accuracy ranges from 18.9% to 20.2%; no model significantly exceeds 20% chance, with all reported one-sided Wilcoxon p-values greater than 0.18. (Table 3 and Section 3.1 continuation; PDF p. 4)
- Section 2.4 says the held-out UGR test subject determines early stopping and that the best checkpoint is restored. Reviewer assessment: excluding this subject from gradient updates does not make the evaluation independent, because the test subject informs model selection. (Section 2.4, first two paragraphs; PDF p. 2)
- The authors report BCIC2020-T3 results on the official validation split because official test labels are unavailable. Absence of this dataset from pretraining, as asserted by the authors, does not resolve the separate issue of validation/test separation during model selection. (Section 2.1 final paragraph; Section 2.4; PDF pp. 2–3)
- Table 1 lists UGR classes as 3/6/30, but Table 2 and Figure 1 label word identity as 60 classes. This review reports Table 2 values and preserves the inconsistency for clarification. (Table 1, PDF p. 2; Figure 1, PDF p. 3; Table 2, PDF p. 4)
- UGR semantic-category and word models train on pooled overt/covert labels. Their separate overt-only and covert-only evaluation shows no statistically significant difference, all p > 0.11; this is not a silent-only training protocol. (Section 2.4, PDF p. 2; Section 3.2, PDF p. 4)
- Multiple-seed experiments and speech-specific pretraining are explicitly future work. Reviewer assessment: speech-specific pretraining is a proposed direction, not an experimentally demonstrated remedy. (Section 4, final sentences; PDF p. 4)
- The paper compares pretrained LaBraM and EEGMamba with established baselines across speech-mode and lexical tasks on two datasets. Reviewer assessment: its contribution is comparative evidence about transfer, not a new decoder or usable speech interface. (Abstract; Sections 2.2 and 3; Tables 2–3; PDF pp. 1–4)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
