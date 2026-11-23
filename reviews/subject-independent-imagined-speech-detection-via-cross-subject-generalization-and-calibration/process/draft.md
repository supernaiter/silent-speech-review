# Subject-Independent Imagined Speech Detection via Cross-Subject Generalization and Calibration

Ko, B.-K., Kim, S., Lee, S.-H. · arXiv preprint · 2025 · [arXiv:2511.13739](https://arxiv.org/abs/2511.13739)

## Verdict

The paper [[1]](#ref-1) changes only the training regime (M03) of an inherited EEG speech-versus-idle detector: a subject-cyclic schedule and fine-tuning on 5–15% of the held-out subject's samples. Both are standard. The cyclic schedule has no counterpart among 141 EEG imagined-speech studies (pattern match, Appendix), but rests on one comparison of two settings, with no pooled baseline and no seeds. Target-subject calibration after source-subject training was described by 2021 [[2]](#ref-2). Without calibration the detector barely separates the classes (MCC 0.044 and 0.123, Table I), so "subject-independent" holds only with the target's labelled data. Every label is a surrogate timed from overt speech [[3]](#ref-3), so detection of imagery itself is not shown.

## Against the field, component by component

### M03 Training: subject-cyclic schedule and calibration

**Usual approach:** Of 141 EEG imagined-, inner- or covert-speech studies with cross-subject, calibration or transfer terms (pattern match, Appendix), 61 test held-out subjects, 56 train per subject only, 38 use domain adaptation and 25 fine-tune on the target subject. The paper trains each subject for N epochs per shuffled cycle, R cycles, then fine-tunes two epochs on target samples (§II.B).

**State of the art:** Belfrouh et al. (2026, [later]): five classes, 15 subjects, zero-shot LOSO near the 20% chance level, 53.71% after 60 calibration trials per class (about 25 min), 5 seeds [[4]](#ref-4).

Of 4 full-text hits for a subject-cyclic schedule among the 141, three are false positives (Appendix). Yet N=5, R=6 and N=3, R=10 both give 30 epochs per subject (inference), and the switch lowers accuracy from 0.694 to 0.670 while MCC rises from 0.044 to 0.123 (Table I), with overlapping spreads. Calibration follows the inter-subject transfer recipe [[2]](#ref-2); a [concurrent] same-institution system fine-tunes on ten trials per class [[5]](#ref-5). At 10% (N=3, R=10), MCC 0.382 against 0.561 subject-dependent closes 59% of the gap from strict LOSO, AUC 0.801 against 0.860 closes 76% (inference). Verdict: standard.

### M11 Ground truth: overt-timed surrogate labels

**Usual approach:** Of 49 EEG imagined-speech studies mentioning overt speech or label alignment (pattern match, Appendix), 10 tie labels to overt speech; a [concurrent] comparator labels imagined trials by cue and block [[6]](#ref-6).

**State of the art:** the cited labeling method (Soroush et al., 2022) sets imagined-speech onset and offset from the same participant's average overt onset and duration (sEEG, 7 participants) [[3]](#ref-3).

Windows are aligned by this overt-speech-based method (§II.A), so the "speech" interval is a post-cue window, not an observed event. The detector can learn cue-locked responses rather than imagery (inference). Verdict: standard, and the main confound.

### M12 Evaluation: strict and calibrated LOSO, six subjects

**Usual approach:** Of 153 EEG studies with held-out-subject terms (pattern match, published table), 46 run leave-one-subject-out over all subjects, as here; EEG speech/non-speech detection with leave-one-subject-out testing dates from 2020, about 76% detection accuracy [[7]](#ref-7).

**State of the art:** Attar (2025, [concurrent]): 82.4% accuracy, macro-F1 0.70, eight inner-speech words, LOSO over four participants [[8]](#ref-8).

Strict LOSO at 0.694 accuracy with MCC 0.044 (Table I) implies a dominant idle class (inference); no class balance or chance level is given (§II.A). Verdict: standard.

### M13 Operation: calibration cost

**Usual approach:** Of 445 EEG imagined-speech studies (pattern match, Appendix), 110 name online or closed-loop operation, 15 a latency value and 4 a calibration time.

**State of the art:** Bhadra et al. (2025): closed-loop binary syllable-imagery EEG BCI, 100 ms mean delay to feedback, daily recalibration [[9]](#ref-9).

Calibration is a share of samples (§II.B); its duration, latency and false activations are not reported. Verdict: not reported.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Imagined speech and idle trials, 6 subjects | Recorded task trials (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Binary idle/speech window labels | Class labels (slot-filled 31) | – | standard |
| M03 Training and adaptation | Subject-cyclic schedule; 2-epoch fine-tune on 5–15% target samples | Held-out-subject testing; target fine-tuning (pattern match 61) | [[4]](#ref-4) (2026): 53.71% five-class, 60 trials/class | standard |
| M04 Use-time action | Imagined speech | Imagined or overt speech (slot-filled 5,595) | – | standard |
| M05 Sensors | Scalp EEG, CAR, 0.5–125 Hz | Scalp EEG (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | MRF-EEGNet (CNN + LSTM) | CNN classifier (slot-filled 7,345) | – | standard |
| M07 Lexicon and LM | None | None (slot-filled 119) | – | not applicable |
| M08 Output | Speech/idle state per 500-ms window | Class label (slot-filled 3,268) | [[7]](#ref-7) (2020): ~76% detection | standard |
| M09 Confirmation | Offline | Offline (slot-filled 82) | – | not applicable |
| M10 Correction | Offline | Offline (slot-filled 82) | – | not applicable |
| M11 Reference construction | Surrogate labels timed from overt speech | Overt-speech-tied labels (pattern match 10) | [[3]](#ref-3) (2022): overt-timed surrogate labels | standard |
| M12 Evaluation | Strict and calibrated LOSO, 6 subjects | LOSO over all subjects (pattern match 46) | [[8]](#ref-8) (2025): 82.4%, 8 words, LOSO | standard |
| M13 Device and cost | Calibration time and latency not reported | Online or closed-loop (pattern match 110) | [[9]](#ref-9) (2025): online, 100 ms | not reported |

## Where the claims outrun the evidence

- "Consistent" cyclic gains (Abstract): accuracy falls 0.694 to 0.670 (§III, Table I); no seeds.
- "All performance metrics improved progressively" with calibration (§III): at N=5, R=6 accuracy is 0.778 at 10% and 0.777 at 15%.
- MCC 0.358 ± 0.791 (§III, Table I, 10%, N=5, R=6) is an outlier spread.
- The Fig. 2 caption assigns N=5, R=6 to both curves.
- 500-ms windows with 50-ms shift share 90% of samples (inference); no trial-level calibration/test split is stated (§II.A–B).
- "Scalable, user-adaptive" systems (Abstract) are untested; the authors call the evidence preliminary (§I).

## What the field needs next

- M03: cyclic versus shuffled pooled training at equal epochs over seeds, and calibration versus training from scratch on the same target data.
- M11: labels from a measured onset with a cue-only control.
- M12: trial-disjoint calibration and test sets, chance level, per-subject MCC.
- M13: calibration in minutes and false activations per minute in continuous EEG.

## Questions for the authors

- What do the ± values aggregate, over how many seeds?
- Are calibration and test windows separated by trial?
- What is the idle-to-speech window ratio?
- How many minutes do 5%, 10% and 15% correspond to?

## Appendix: literature search

- M03, imagined-speech-eeg-cross-subject-calibration (new). Inclusion rule: EEG imagined, inner or covert speech decoders or detectors whose ledger records cross-subject training, held-out-subject testing, transfer learning, fine-tuning or calibration, classified by full-text pattern; reviews and datasets counted; every named design counts (upper bound). Ledger: 1,526 unique studies slot-filled for M03; 141 unique studies pattern match. Held-out-subject testing 61, per-subject-only training 56, domain adaptation or subject-invariant learning 38, target-subject fine-tuning or calibration 25, subject-cyclic schedule 4 (the target; the other three are false positives) (pattern match). Read in full: [[2]](#ref-2), [[5]](#ref-5), [[4]](#ref-4). Known-item recall 1.0 (5 seeds).
- M03, cross-subject-pooled-training (published table, reused). Inclusion rule: speech or language decoders from neural or other biosignals that train one model on data pooled across participants; per-participant models excluded. Ledger: 1,526 unique studies slot-filled; 370 unique studies pattern match. Usual design: per-subject model, 90 of 379 (pattern match, published counts). Known-item recall 1.0.
- M11, overt-speech-reference-for-imagined-eeg (new). Inclusion rule: EEG imagined-speech studies that build or align imagined-speech labels from overt speech or another explicit reference; overt-speech recognition excluded. Ledger: 234 unique studies slot-filled for M11; 49 unique studies pattern match. Labels or alignment tied to overt speech 10, speech-activity detection 7, cue-locked epochs 6 (pattern match). Read in full: [[3]](#ref-3), [[6]](#ref-6).
- M12, eeg-held-out-subject-test (published table, reused). Inclusion rule: EEG decoding studies reporting accuracy on subjects not used for training; calibrated transfer counted and recorded as such. Ledger: 6,960 unique studies slot-filled for M12; 153 unique studies pattern match. Leave-one-subject-out over all subjects 46, fixed held-out subjects 41 (pattern match, published counts). Read in full: [[8]](#ref-8), [[7]](#ref-7).
- M13, imagined-speech-eeg-online-operation (new). Inclusion rule: EEG imagined, inner or covert speech studies, classified by full-text pattern into online or closed-loop operation, reported latency, reported calibration time and idle-state detection; related-work hits count (upper bound). Ledger: 6,075 unique studies slot-filled for M13; 445 unique studies pattern match. Online or closed-loop 110, idle-state detection 69, latency value 15, calibration time 4 (pattern match). Read in full: [[9]](#ref-9).

## References

Numbered by first citation. BibTeX in the same order and keys: [subject-independent-imagined-speech-detection-via-cross-subject-generalization-and-calibration.bib](subject-independent-imagined-speech-detection-via-cross-subject-generalization-and-calibration.bib).

1. <a id="ref-1"></a>Ko, B., Kim, S., Lee, S. “Subject-Independent Imagined Speech Detection via Cross-Subject Generalization and Calibration.” *arXiv preprint*, 2025. doi:[10.48550/arXiv.2511.13739](https://doi.org/10.48550/arXiv.2511.13739). arXiv:[2511.13739](https://arxiv.org/abs/2511.13739). Target. Read as arXiv v1. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/subject-independent-imagined-speech-detection-via-cross-subject-generalization-and-calibration) [wiki: arxiv-2511.13739](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2511.13739/article.md)
2. <a id="ref-2"></a>Panachakel, J. T., Ganesan, R. A. “Decoding Imagined Speech From EEG Using Transfer Learning.” *IEEE Access*, 2021, 9, 135370-135385. doi:[10.1109/ACCESS.2021.3116196](https://doi.org/10.1109/ACCESS.2021.3116196). Prior; deciding prior for M03 (inter-subject transfer to a new target subject, Sec. I). [wiki: doi-10.1109-access.2021.3116196](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-access.2021.3116196/article.md)
3. <a id="ref-3"></a>Soroush, P. Z., Herff, C., Ries, S. K., Shih, J. J., Schultz, T., Krusienski, D. J. “The Nested Hierarchy of Overt, Mouthed, and Imagined Speech Activity Evident in Intracranial Recordings.” *bioRxiv*, 2022. doi:[10.1101/2022.08.04.502829](https://doi.org/10.1101/2022.08.04.502829). Prior; the labeling method [31] of the target (published in NeuroImage 269, 119913, 2023). Read as bioRxiv v1. [wiki: doi-10.1101-2022.08.04.502829](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2022.08.04.502829/article.md)
4. <a id="ref-4"></a>Belfrouh, S., Errattahi, R., Salmam, F. Z. “Rapid Calibration for Cross-Subject Imagined Speech Decoding Toward Restoring Communication.” *Odyssey 2026: The Speaker and Language Recognition Workshop*, 2026. doi:[10.21437/Odyssey.2026-21](https://doi.org/10.21437/Odyssey.2026-21). Later; state of the art for M03 calibration. [later] [wiki: isca-belfrouh26_odyssey](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-belfrouh26_odyssey/article.md) [wiki: isca-belfrouh26-xcalib](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-belfrouh26-xcalib/article.md)
5. <a id="ref-5"></a>Park, J., Kwak, H., Shin, G., Jeon, Y., Park, S., Hwang, J., et al. “Toward Practical BCI: A Real-time Wireless Imagined Speech EEG Decoding System.” *arXiv preprint*, 2025. doi:[10.48550/arXiv.2511.07936](https://doi.org/10.48550/arXiv.2511.07936). arXiv:[2511.07936](https://arxiv.org/abs/2511.07936). Concurrent; same institution; per-user fine-tuning on ten trials per class. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/toward-practical-bci-a-real-time-wireless-imagined-speech-eeg-decoding-system) [wiki: arxiv-2511-07936-wirelessimg](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2511-07936-wirelessimg/article.md)
6. <a id="ref-6"></a>Alonso-Vázquez, D., Mendoza-Montoya, O., Caraza, R., Martinez, H. R., Antelis, J. M. “From pronounced to imagined: improving speech decoding with multi-condition EEG data.” *Frontiers in Neuroinformatics*, 2025. doi:[10.3389/fninf.2025.1583428](https://doi.org/10.3389/fninf.2025.1583428). Concurrent; labels from cue and block condition (Sec. 2.2). [concurrent] [wiki: pmc-12245923-pron2img-eeg](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12245923-pron2img-eeg/article.md)
7. <a id="ref-7"></a>Sharon, R. A., Murthy, H. A. “The "Sound of Silence" in EEG -- Cognitive Voice Activity Detection.” *Proc. Interspeech 2020*, 2020. doi:[10.21437/Interspeech.2020-2383](https://doi.org/10.21437/Interspeech.2020-2383). arXiv:[2010.05497](https://arxiv.org/abs/2010.05497). Prior; EEG speech/non-speech state detection with leave-one-subject-out testing. [wiki: isca-sharon20_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-sharon20_interspeech/article.md) [wiki: arxiv-2010.05497](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2010.05497/article.md)
8. <a id="ref-8"></a>Attar, E. T. “Deep learning for inner speech recognition: a pilot comparative study of EEGNet and a spectro-temporal Transformer on bimodal EEG-fMRI data.” *Frontiers in Human Neuroscience*, 2025. doi:[10.3389/fnhum.2025.1668935](https://doi.org/10.3389/fnhum.2025.1668935). Concurrent; state of the art for M12 (published table). [concurrent] [wiki: doi-10.3389-fnhum.2025.1668935](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnhum.2025.1668935/article.md) [wiki: fhn-41209398-eegnet](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/fhn-41209398-eegnet/article.md) [wiki: pmc-12589180-egx](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12589180-egx/article.md)
9. <a id="ref-9"></a>Bhadra, K., Giraud, A., Marchesotti, S. “Learning to operate an imagined speech Brain-Computer Interface involves the spatial and frequency tuning of neural activity.” *Communications Biology*, 2025, 8. doi:[10.1038/s42003-025-07464-7](https://doi.org/10.1038/s42003-025-07464-7). Prior (bioRxiv 2023); state of the art for M13 (online closed-loop operation). [wiki: doi-10.1038-s42003-025-07464-7](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s42003-025-07464-7/article.md) [wiki: biorxiv-2023.09.11.557181](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/biorxiv-2023.09.11.557181/article.md) [wiki: pmc-11842755-bcilearn](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11842755-bcilearn/article.md)
