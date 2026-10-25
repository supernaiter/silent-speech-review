# Transfer Learning from ImageNet for MEG-Based Decoding of Imagined Speech

Soufiane Jhilal, Stéphanie Martin, Anne-Lise Giraud  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2601.15909)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text+summary

Adapts ImageNet-pretrained vision models to MEG time-frequency images for closed-set imagined-speech classification, reaching 60.6% (pooled CV) and 51.7% (leave-one-subject-out) on three-vowel decoding (chance 33%).

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 248-magnetometer MEG (non-invasive) |
| Task | Closed-set imagined speech condition and vowel classification |
| Vocabulary | 3 vowel classes; 18 syllable items |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Three-vowel balanced accuracy 60.6% pooled CV, 51.7% LOSO, chance 33% |

**Limitations.** Decodes task/vowel labels, not words or sentences; binary contrasts may reflect attention or residual sensorimotor activity; no online, clinical or communication evaluation.

## Full review

### In short

ImageNet-pretrained vision models improve closed-set MEG classification, including held-out-subject tests, but the study decodes task/vowel labels—not sentences—and leaves practical communication undemonstrated.

### Review

This paper's useful contribution is a representation-learning experiment: it turns MEG time-frequency scalograms into three learned spatial maps and adapts ImageNet-pretrained ResNet-18 and ViT-Tiny models to classify imagined-speech conditions and vowel labels. On the full window, ResNet-18 reports balanced accuracy of 90.4% SAP / 77.5% LOSO for imagined speech versus silence, 81.0% / 72.2% for imagined speech versus silent reading, and 60.6% / 51.7% for three-vowel classification. SAP is trial-grouped pooled evaluation, not evidence of held-out-person performance; LOSO is the actual participant-held-out protocol. The ablation supports a contribution from pretraining and learned sensor mixing, but these results remain class-label decoding on a closed French paradigm. They do not show word or sentence transcription, speech reconstruction, or a usable SSI. The authors themselves caution that task engagement, attention, or residual sensorimotor activity may help distinguish imagined speech from silence and that vowel accuracy is below practical speech-BCI needs. Larger phonemic sets, adaptive timing, interpretability, and further domain adaptation are left for future work.

### Why it matters

Shows that image-like MEG time-frequency representations paired with ImageNet pretraining and learned sensor mixing can support above-chance imagined-speech condition and three-vowel classification, including a separate leave-one-subject-out evaluation.

### Prior state of the art

Non-invasive imagined-speech studies commonly classify neural recordings into limited tasks or labels. This paper tests whether MEG time-frequency structure can be recast as image-like inputs so that vision-model pretraining can be transferred to closed-set imagined-speech classification.

### What changed

Transforms each epoch's 248-channel MEG scalograms into three learned spatial mixtures, resizes the resulting time-frequency representation to 224×224×3, and fine-tunes pretrained ImageNet vision models for imagined-speech condition and vowel labels.

### Position in the field

A non-invasive MEG representation-learning study for closed-set imagined-speech condition and vowel classification, not an end-to-end speech restoration or text-entry system.

### Practical value

Methodological evidence that ImageNet-pretrained vision backbones can be adapted to learned image-like MEG time-frequency inputs under participant-held-out evaluation. It does not yet provide text/audio output or demonstrate a communication interface.

### Advanced

Applies ImageNet-pretrained vision representations to MEG time-frequency maps for imagined-speech task and vowel classification, and reports both trial-grouped pooled evaluation and leave-one-subject-out evaluation on 21 participants.

### Unresolved

Larger phonemic inventories and naturalistic or continuous imagined speech; linguistic decoding beyond three vowel labels; clinical or communication-user validation; real-time use; interpretation of task engagement, attention, and residual sensorimotor contributions; replication outside this French MEG cohort.

### Narrowed or regressed

The demonstrated outputs are offline class labels for two task contrasts and three cued vowels, not transcribed sentences, reconstructed speech, or a working communication interface. Fine-grained vowel results are modest, especially under held-out-subject evaluation.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-recognition |
| Input | Magnetoencephalography (MEG), recorded with 248 magnetometers at 1 kHz; non-invasive. |
| Sensor | MEG recorded at 1 kHz with 248 magnetometers; device make/model is not specified in the reviewed text. |
| Body site | brain |
| Output | labels |
| Vocabulary type | Cued French sentence imagery and closed-set three-vowel labels; no open vocabulary or continuous text output. |
| Vocabulary size | Closed set of 18 syllable items combining one of five consonants or none with one of three vowels; the distinct sentence-set size is not separately specified beyond three blocks of 34 sentence trials. |
| Metrics and results | Full-window ResNet-18 balanced accuracy (mean ± 95% CI): ISP vs silence 90.4 ± 2.5% SAP and 77.5 ± 1.3% LOSO; ISP vs silent reading 81.0 ± 2.0% SAP and 72.2 ± 1.5% LOSO; three-vowel decoding 60.6 ± 1.5% SAP and 51.7 ± 0.8% LOSO (three-class chance 33%). SAP is trial-grouped pooled 10-fold CV; LOSO is participant-held-out. Table 4's no-pretraining convolutional/random-initialization/partial-fine-tuning variant reports 81.6/70.8% for ISP-vs-silence, 72.1/64.9% for ISP-vs-silent-reading, and 53.3/46.0% for vowels (SAP/LOSO). |
| Evaluation protocol | Offline balanced-accuracy classification with 95% bootstrap confidence intervals. The paper compares LDA, EEGNet, a shallow CNN, a Riemannian tangent-space classifier, ResNet-18, and ViT-Tiny across pre-cue, post-cue, and full (-300 to 500 ms) windows. It reports stratified 10-fold SAP grouped by trial and a distinct 21-fold leave-one-subject-out (LOSO) protocol; pairwise model tests use Wilcoxon signed-rank tests and comparisons against chance use permutation tests, with Holm-Bonferroni correction stated. |

### Limits

- **Technical:** The task labels are ISP-versus-silence, ISP-versus-silent-reading, and /a/, /e/, /i/ vowel classes. The binary contrast can reflect task engagement, attention, or residual sensorimotor activity, as the authors acknowledge. Closed-set epoch classification does not establish word/sentence decoding or speech reconstruction; SAP and LOSO have different generalization meanings.
- **Evaluation:** The cohort is 21 neurotypical native French speakers after excluding five of 26 participants, and stimuli use a closed, cued syllable/sentence paradigm. Subject-Agnostic Pooled (SAP) uses trial-grouped 10-fold cross-validation and must not be read as subject-independent; Leave-One-Subject-Out (LOSO) is the separate held-out-participant protocol. The main content task is three-vowel classification, not word or sentence decoding. The authors note that task engagement, attention, or residual sensorimotor activity could contribute to ISP-versus-silence discrimination and that vowel scores are below practical speech-BCI requirements. Online, clinical, naturalistic, and continuous-speech evaluation is absent.
- **Deployment:** The paper evaluates offline classification of recorded MEG epochs. It reports no real-time or online interface, continuous speech decoding, user communication study, portable implementation, latency, or deployment measurement. The recording uses a 248-magnetometer MEG system.
- **Scope of this review:** Twenty-one neurotypical native French participants after exclusions; cued, closed-set sentence/syllable tasks; two condition contrasts and three-vowel classification. No continuous sentence transcription, open-vocabulary decoding, speech synthesis, clinical cohort, online use, or user communication outcome.

### Evidence

- The abstract presents an image-based MEG approach that maps imagined-speech signals to time-frequency representations for ImageNet-pretrained vision models, and reports three task families: imagery versus silence, imagery versus silent reading, and vowel decoding. (Abstract; PDF p. 1)
- Twenty-six neurotypical native French speakers took part and five were excluded, leaving 21. The paradigm used three blocks of 34 sentences (6–11 syllables), a closed set of 18 syllable items, silent reading followed by imagery at 400 ms per syllable, and 248-channel MEG recorded at 1 kHz. (Section 2.1, Dataset and tasks; PDF p. 1)
- Preprocessing includes 50/100/150 Hz notch filters, a 0.5–150 Hz band-pass, downsampling to 500 Hz, ICA and AutoReject artifact handling, and pre-cue (-300 to 0 ms), post-cue (0 to 500 ms), and full (-300 to 500 ms) epochs; silence examples come from inter-trial rest, not inter-syllable gaps. (Section 2.2, Preprocessing and epoch extraction; PDF p. 2)
- The representation applies Morlet CWT independently to each channel at 96 log-spaced frequencies from 1 to 150 Hz, then uses a learnable 1×1 sensor-space projection to mix 248 channel scalograms into three maps and resizes the result to 224×224×3 for the vision models. (Sections 2.3–2.4 and Fig. 2; PDF p. 2)
- The evaluation distinguishes Subject-Agnostic Pooled stratified 10-fold cross-validation grouped by trial from a separate Leave-One-Subject-Out protocol with 21 folds; balanced accuracy is used, with 50% binary and 33% three-class chance levels. (Evaluation protocol in Section 2.5; PDF p. 3)
- For full-window ISP-versus-silence decoding, ResNet-18 reports 90.4 ± 2.5% SAP and 77.5 ± 1.3% LOSO balanced accuracy; SAP is pooled trial-grouped evaluation and LOSO is the participant-held-out result. (Section 3.1, Table 1 and Fig. 3; PDF p. 3)
- For full-window ISP-versus-silent-reading decoding, ResNet-18 reports 81.0 ± 2.0% SAP and 72.2 ± 1.5% LOSO balanced accuracy; the text identifies this contrast as more difficult than ISP versus silence. (Section 3.2, Table 2 and Fig. 4; PDF p. 3)
- For full-window three-class /a/, /e/, /i/ decoding, ResNet-18 reports 60.6 ± 1.5% SAP and 51.7 ± 0.8% LOSO balanced accuracy; the separate post-cue LOSO table entry is 51.4 ± 0.9% and should not be substituted for the full-window value. (Section 3.3 and Table 3, PDF p. 3; Fig. 5, PDF p. 4)
- In the full-window ablation, the convolutional-projection model with random initialization and partial fine-tuning reports SAP/LOSO balanced accuracy of 81.6/70.8% for ISP versus silence, 72.1/64.9% for ISP versus silent reading, and 53.3/46.0% for vowel decoding, below the pretrained baseline entries. (Section 3.4, Table 4; PDF p. 4)
- The discussion says ISP-versus-silence decoding may be influenced by broader task engagement, attention, or residual sensorimotor activity, and that current vowel accuracy remains below what would be required for practical speech BCIs; future work includes larger phonemic sets and adaptive timing. (Section 4, Discussion; PDF p. 4)
- The conclusion describes an image-driven MEG decoding strategy and imagery-locked discriminative information, while framing it as a foundation for future non-invasive speech decoding studies rather than reporting a communication interface or sentence transcription result. (Section 5, Conclusion; PDF p. 4)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
