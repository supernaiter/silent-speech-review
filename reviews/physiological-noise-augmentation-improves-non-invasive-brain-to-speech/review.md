# Physiological Noise Augmentation Improves Non-Invasive Brain-to-Speech

Benjamin Ballyk, Teyun Kwon, Miran Özdogan, Oiwi Parker Jones · arXiv preprint, 2026 · [arXiv:2607.05165](https://arxiv.org/abs/2607.05165)

## Verdict

The paper [[1]](#ref-1) changes one component, training-set augmentation (M03), and it is standard: re-injecting recorded artifact signals from other trials into neural training data was done two years earlier for EEG speech decoding [[2]](#ref-2), which the paper does not cite; ICA-based artifact projection is the refinement. The gain needs ten averaged imaginings per decision (M04), behind the single-trial decoding typical of the field; at single trial neither model gains beyond seed error (Table 1), as the authors concede (Sec. 4.1). The main claim holds only narrowly: at 10 trials EEGNet rises from 73.0% to 76.3% (Table 1), not the 4.7 points and 77.6% of the abstract and contributions, and generic white noise reaches 0.747 against 0.763 (Table 2). The claimed mechanism, invariance to tracked artifacts, is not directly tested.

## Against the field, component by component

### M03 Training: artifact-component augmentation

**Usual approach:** among 45 pattern-matched studies that augment neural training data (Appendix), the commonest designs are masking or channel dropout (12), additive noise (10) and time shift or crop (10); 4 match artifact or reference-signal injection, and two of them, this paper and Sato et al. [[2]](#ref-2), re-inject recorded artifacts. PNA departs from the generic input-level default by drawing perturbations from the recording's own EOG/ECG-correlated ICA components.

**State of the art:** Sato et al. (2024, prior) mix recorded EOG or EMG from other trials into EEG and then test the invariance directly: top-10 accuracy from EOG input alone falls from 28.8% to 5.02% (chance 2%), at a cost of 76.0% to 72.3% on EEG input [[2]](#ref-2). PNA reports no such test, so the gap is in evidence, not design.

The paper's Related Work says neural augmentations lack draws from the empirical noise distribution (Sec. 2); the 2024 work already does this with label-preserving donor trials. Against generic augmentation the PNA edge is small and model-dependent: with 10-trial MLP decoding, frequency shift (0.596), temporal shift (0.584) and white noise (0.578) all beat Raw+PNA (0.574), and so does Clean Only with averaging (0.581). Verdict: standard.

### M04 Use-time action: ten repeated imaginings per decision

**Usual approach:** among 68 pattern-matched imagined-speech EEG/MEG studies, 9 state single-trial decoding; of the 3 multi-trial-averaging matches, two are versions of [[3]](#ref-3), which decodes single trials, so this paper is the only one that averages test trials (Appendix).

**State of the art:** single-trial MEG reaches 93.24% on five imagined phrases in eight subjects with SST-CNN in the imagination stage [[3]](#ref-3) (2020, prior; stated chance level 30%), a different task, so no like-for-like gap. The yardstick here is typical practice: PNA's benefit exists only when the user imagines each digit ten times (Appendix A.2), and at single trial EEGNet scores 0.332 with PNA against 0.337 raw (Table 1). The authors say so (Sec. 4.1), but the conclusion that PNA reduces the repetition burden (Sec. 5) has no accuracy-versus-repetitions comparison behind it. Verdict: behind.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | MegNIST screen-cued imagined digits | Cued task (slot-filled 4,015) | – | standard |
| M02 Training-only supervision | Digit labels only | Class labels (slot-filled 31) | – | standard |
| M03 Training and adaptation | ICA artifact components remixed from donor trials | Masking or channel dropout (12) (pattern match 45) | EOG-only top-10 28.8% to 5.02% after mixing [[2]](#ref-2) | standard |
| M04 Use-time action | 10 imaginings averaged per decision | Single-trial decoding (9) (pattern match 68) | 93.24% single-trial, 5 imagined phrases [[3]](#ref-3) | behind |
| M05 Sensors | Whole-head MEG with EOG and ECG references | Per-study sensor (slot-filled 8,898) | – | standard |
| M06 Processing and decoding | MLP and EEGNet classifiers | Raw time-series CNN (slot-filled 8,925) | – | standard |
| M07 Lexicon and LM | None (ten-digit closed set) | Not recorded (slot-filled 120) | – | not applicable |
| M08 Output | Digit class probabilities | Class label (slot-filled 3,760) | – | standard |
| M09 Confirmation | None | Mostly absent (slot-filled 82) | – | not applicable |
| M10 Correction | None | Mostly absent (slot-filled 82) | – | not applicable |
| M11 Reference construction | One subject, 12,000 balanced trials, 10:1:1 | Per-study corpus (slot-filled 239) | – | standard |
| M12 Evaluation | Accuracy, 5 seeds, unnamed split | Held-out accuracy (slot-filled 8,381) | – | not reported |
| M13 Device and cost | Laboratory MEG, offline, references required | Laboratory (slot-filled 6,721) | – | standard |

## Where the claims outrun the evidence

- The abstract, contributions (Sec. 1) and Discussion (Sec. 5) give +4.7 points for EEGNet, the contributions also 77.6%; Table 1 and Table 2 give 0.730 to 0.763, i.e. +3.3 points (4.5% relative, 12% fewer errors) (inference), and Sec. 4.2 names 76.3% as the best result. None of Tables 1-5 contains 77.6%; 4.7 points over the same 73.0% baseline gives 77.7%, so the two headline numbers agree with each other but with no tabulated run (inference).
- Baseline augmentations are tuned on single-trial validation (Table 5) but compared at 10 trials, and are applied after averaging while PNA is applied before it (Table 2 caption): neither ordering nor tuning is matched.
- EEGNet Raw+PNA leads white noise by 0.016 with standard errors of 0.011 and 0.012 (Table 2), and no test is named (inference).
- Invariance is the stated goal (Sec. 3, Eq. 1), but no experiment decodes from EOG/ECG components alone or measures decoder sensitivity along artifact directions; evidence is accuracy and embeddings (Fig. 4, Appendix C), unlike the direct test in [[2]](#ref-2).
- One subject and ten digits (Sec. 4); the authors concede this (Sec. 5).

## What the field needs next

- M03: compare PNA with reference-channel mixing [[2]](#ref-2) at matched strength, and report decoding from artifact components alone with and without PNA.
- M04: report EEGNet accuracy against the number of averaged test trials with and without PNA, and the repetitions needed to reach a fixed accuracy.
- M12: tune every augmentation at the evaluated number of trials, apply all at the same point relative to averaging, and test differences across seeds and held-out sessions.

## Questions for the authors

- Are Tables 1-2 scored on the held-out test split, and how many averaged test samples are scored?
- How are test-time averages formed: disjoint groups or resampled subsets of the test pool?
- Which run gives 4.7 points and 77.6%, for example a higher augmented-to-raw ratio (Fig. 5)?
- What are the EOG/ECG correlation thresholds and the Table 2 seed count?
- How are sessions assigned to train, validation and test?

## Appendix: literature search

- M03, neural-signal-training-augmentation (new topic table). Inclusion rule: speech or language decoders from EEG, MEG, ECoG, sEEG or intracortical recordings that perturb or remix real training recordings (noise, shifts or crops, masking or channel dropout, scaling, mixup, artifact or reference-signal injection); model-generated signals, target-only augmentation and artifact removal without re-injection excluded. Ledger: 1526 slot-filled; 45 unique studies by pattern match. Designs (full-text pattern match): masking or channel dropout 12, additive noise 10, time shift or crop 10, mixup 6, amplitude scaling 4, artifact or reference-signal injection 4. Read in full: [[2]](#ref-2) (deciding prior and state of the art). Known-item recall 1.0.
- M04, imagined-speech-test-trial-averaging (new topic table). Inclusion rule: imagined, covert or inner speech decoding from EEG or MEG that states whether each test decision uses one trial or an average of repeated trials; averaging over subjects, folds or seeds excluded. Ledger: 5595 slot-filled; 68 unique studies by pattern match. Designs (full-text pattern match): single-trial decoding 9, multi-trial averaging 3 (this paper and two versions of [[3]](#ref-3), which decodes single trials). Read in full: [[3]](#ref-3) (deciding prior and state of the art). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Ballyk, B., Kwon, T., Özdogan, M., Parker Jones, O. “Physiological Noise Augmentation Improves Non-Invasive Brain-to-Speech.” *arXiv preprint*, 2026. arXiv:[2607.05165](https://arxiv.org/abs/2607.05165). Target. Read as arXiv 2607.05165v1. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/physiological-noise-augmentation-improves-non-invasive-brain-to-speech) [wiki: arxiv-2607.05165](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2607.05165/article.md)
2. <a id="ref-2"></a>Sato, M., Tomeoka, K., Horiguchi, I., Arulkumaran, K., Kanai, R., Sasai, S. “Scaling Law in Neural Data: Non-Invasive Speech Decoding with 175 Hours of EEG Data.” *arXiv preprint*, 2024. arXiv:[2407.07595](https://arxiv.org/abs/2407.07595). [wiki: arxiv-2407.07595](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2407.07595/article.md)
3. <a id="ref-3"></a>Dash, D., Ferrari, P., Wang, J. “Decoding Imagined and Spoken Phrases From Non-invasive Neural (MEG) Signals.” *Frontiers in Neuroscience*, 2020, 14, 290. doi:[10.3389/fnins.2020.00290](https://doi.org/10.3389/fnins.2020.00290). [wiki: doi-10.3389-fnins.2020.00290](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnins.2020.00290/article.md) [wiki: doi-10.3389-fnhum.2020.00290](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnhum.2020.00290/article.md) [wiki: pmc-7154084-megphrases](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-7154084-megphrases/article.md)
