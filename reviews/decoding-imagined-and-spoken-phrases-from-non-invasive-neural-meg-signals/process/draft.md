# Decoding Imagined and Spoken Phrases From Non-invasive Neural (MEG) Signals

Dash D, Ferrari P, Wang J. Frontiers in Neuroscience, 2020. [doi:10.3389/fnins.2020.00290](https://doi.org/10.3389/fnins.2020.00290)

## Verdict

The paper [[1]](#ref-1) changes the decoder (M06), feeding Morlet scalograms, per sensor or as a 14 × 14 sensor mosaic, to CNNs, and training (M03), initialising them from ImageNet. Neither design appears among the 17 earlier imagined-speech decoders of any electrophysiological signal (Appendix), yet both are standard: the comparator is an in-house network with more inputs than training trials (Sec. 5.1), the mosaic's gain is not significant for imagination and coincides with augmentation given only to the mosaic, and no network is trained from scratch. The strongest problem is in evaluation (M12): before any phrase is shown, SST-CNN classifies the pre-stimulus window at 42.96% against the authors' 30% chance (Table 1). The same laboratory's [later] study of the same paradigm and RMS features reports 45.46% for imagined phrases under 5-fold cross-validation [[2]](#ref-2), against 80.83% here. The 93% is a within-session trial-split figure for a preparation interval after reading, not evidence of decodable imagined speech.

## Against the field, component by component

### M06 Decoder: scalogram images and a sensor mosaic

**Usual approach:** Of 17 prior imagined-speech decoders (pattern match, Appendix), 12 use hand-crafted features with a shallow classifier, 2 any CNN, none time-frequency images with a CNN; the closest prior CNN convolves raw synthetic EEG [[3]](#ref-3). The paper replaces this with scalogram CNNs (Sec. 3).

**State of the art:** No later imagined-speech MEG study reports a higher five-class score; the closest, same laboratory and paradigm (2020, [later]), reaches 54.34% with 9 sensors and 45.46% with 196 (SVM, 5-fold CV, 7 subjects, 20% chance) [[2]](#ref-2).

For imagination, ST-CNN reaches 91.71% and SST-CNN 93.24%, not different (p = 0.2135, Sec. 4.1); the mosaic's other wins coincide with 100- and 200-ms shift augmentation used for SST-CNN alone, which the authors concede (Sec. 5.1). The ANN has 1,176 inputs for about 250 training trials per subject (Sec. 5.1), so the margin over its 80.83% is not a margin over the field's shallow decoders. Verdict: standard.

### M03 Training: ImageNet-pretrained CNNs

**Usual approach:** None of the 17 prior or 8 [concurrent] decoders initialises from ImageNet (pattern match, Appendix); the paper fine-tunes AlexNet, ResNet101 and Inception-ResNet-v2 (Sec. 3.2).

**State of the art:** A [later] MEG study (2026) ran the missing control: removing ImageNet weights lowers imagery versus silence from 90.4% to 81.6% and held-out-participant three-vowel accuracy from 51.7% to 46.0% at 33% chance [[4]](#ref-4), relative drops of 9.7% and 11.0% (inference).

With no randomly initialised network, the paper shows that pretrained CNNs work, not that pretraining helps. Citing the group's EMBC 2019 CNN transfer-learning paper on MEG speech [[5]](#ref-5) [concurrent], its earlier version, the same paragraph states "To our knowledge, this is the first study using CNNs to explore neural speech decoding with MEG" (Sec. 1; Appendix). Verdict: standard.

### M12 Evaluation: trial splits and the pre-stimulus floor

**Usual approach:** 13 of 17 prior decoders test on held-out trials of the same recording (pattern match, Appendix), as do the paper's three random 70/15/15 splits (Sec. 3.1).

**State of the art:** On the same paradigm (2020, [later]), an SVM on the same 1,176 RMS features under 5-fold CV gives 45.46% for imagination and 76.62% for articulation [[2]](#ref-2).

The pre-stimulus control is to the authors' credit, and it fails: with pseudo-randomised order (Sec. 2.2), 42.96% is 12.96 points above their 30% and 22.96 above the 20% of their later study (inference); the authors raise carryover (Sec. 5.3). The same features drop 43.8% relative between the two protocols (inference), with classifier, folds and cohort changed together. EMG during internal speech [[6]](#ref-6) and across-day testing [[7]](#ref-7) occur in 1 of 17 priors each (Appendix), too few for behind. Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Cued reading, 1-s covert preparation, then overt articulation | Prompted imagery or overt speech | – | standard |
| M02 Training-only supervision | Five phrase class labels | Class-label supervision | – | standard |
| M03 Training and adaptation | ImageNet-pretrained AlexNet, ResNet101, Inception-ResNet-v2; no from-scratch control | No ImageNet initialisation, 17 of 17 prior (pattern match 0) | Pretraining ablation, 90.4 vs 81.6% [[4]](#ref-4) [later] | standard |
| M04 Use-time action | 1-s preparation interval between text and speech | Cued imagined speech | – | standard |
| M05 Sensors | 196 of 204 gradiometers, Elekta MEG, 1 kHz | MEG or EEG | – | standard |
| M06 Processing and decoding | Morlet scalograms per sensor or as 14 × 14 mosaic into CNNs; RMS-feature ANN baseline | Hand-crafted features + shallow classifier, 12 of 17 prior (pattern match 12) | 54.34%, 5 imagined phrases, 9 sensors, SVM [[2]](#ref-2) | standard |
| M07 Lexicon and LM | None (closed set) | No lexicon | – | not applicable |
| M08 Output | Phrase class | Class label | – | standard |
| M09 Confirmation | None (offline) | None | – | not applicable |
| M10 Correction | None (offline) | None | – | not applicable |
| M11 Reference construction | Cue-timed segments, 8 healthy adults | Cue labels | – | standard |
| M12 Evaluation | Three random 70/15/15 trial splits within subject; pre-stimulus above chance | Within-subject trial split, 13 of 17 prior (pattern match 13) | 45.46%, same features, 5-fold CV [[2]](#ref-2) | standard |
| M13 Device and cost | Laboratory MEG, offline | Laboratory | – | standard |

## Where the claims outrun the evidence

- "Imagined" (Title): the window is the 1 s between a 1-s text display and overt speech (Sec. 2.2), which the authors allow mixes preparation and imagination (Sec. 5.3); no EMG is recorded, and the claim that timing prevents muscle activation (Sec. 5.3) is not measured.
- The abstract's "up to 93%" does not subtract the 42.96% pre-stimulus floor (Table 1).
- Trial counts disagree: about 75 per phrase per subject (Sec. 2.3), about 50 (Sec. 3.2.4.2), about 60 (Sec. 4.2).
- Table 2 rows each sum to 1,382 with 40 to 51 errors, while the text reports about 12 per phrase (inference).
- Pairwise t-tests are uncorrected (Sec. 4.1); seeds and splits are unreported (Sec. 3.1).

## What the field needs next

- M12: block- or session-wise folds; test whether the pre-stimulus window predicts the previous phrase.
- M04: imagery without a following overt response, with articulatory EMG as in [[6]](#ref-6).
- M03 and M06: CNNs from random initialisation, as [[4]](#ref-4) did, and both scalogram inputs with identical augmentation.

## Questions for the authors

- What constrained the pseudo-randomised order?
- Were splits stratified, and how many test trials per subject and phrase remained?
- Was RMS chosen on training trials only?
- Is 1,382 in Table 2 the total test set or the per-phrase total?

## Appendix: literature search

Target-time population for all three topics: imagined, covert, inner or internal speech decoders from scalp EEG, MEG, ECoG, depth or intracortical recordings first public before 2019-01, found by a full-text pattern over the whole wiki and triaged by hand; fMRI, fNIRS, reviews, listening-only, overt-only and analyses without a decoder excluded; versions once. Target time 2019-07, the EMBC 2019 version [[5]](#ref-5); journal received 2019-08 and published 2020-04. 17 prior unique studies (one EEG and MEG, six intracranial, ten EEG; no MEG-only), 8 [concurrent] (2019-01 to 2020-01).

- M06 imagined-speech-neural-time-frequency-image-cnn (new). Inclusion rule: decoders of imagined, covert or inner speech from electrophysiological recordings; design compared is decoder input and classifier; related-work mentions do not count. Ledger counts: slot-filled 7,345 unique studies (M06); pattern match 309 unique studies, all years. Among the 17 prior (pattern match): shallow classifier 12, any CNN 2, time-frequency image with CNN 0, ImageNet-pretrained 0; among the 8 [concurrent]: any CNN 6, time-frequency image with CNN 0. Whole-wiki recall check (any electrophysiological speech decoder up to 2019, overt included): 2 hits, both off-design. Read: [[3]](#ref-3) (prior), [[2]](#ref-2) (state of the art). Known-item recall 1.0 (3 seeds).
- M03 imagenet-pretrained-vision-backbone-neural-speech (published table, reused). Inclusion rule: speech or language decoders from EEG, MEG or intracranial recordings that initialise a vision backbone pretrained on natural images. Ledger counts: slot-filled 1,526 unique studies (M03); pattern match 8 unique studies, all years, none before 2020 other than the target. At target time: 0 of 17 prior, 0 of 8 [concurrent]. Read: [[4]](#ref-4) (state of the art). Known-item recall 1.0 (2 seeds).
- M12 imagined-speech-neural-test-partition-and-artifact-controls (new). Inclusion rule: same population; design compared is test separation and EMG recorded during the covert condition; EMG named only for artifact removal or background does not count. Ledger counts: slot-filled 6,960 unique studies (M12); pattern match 309 unique studies, all years. Among the 17 prior (pattern match): within-subject k-fold, leave-one-out or random split 13; held-out-subject term 7; session or day term 3, across-day evaluation 1; EMG term 7, EMG during covert speech 1, EMG removal re-tested 1; permutation null 4. Read: [[6]](#ref-6), [[7]](#ref-7) (prior), [[2]](#ref-2) (state of the art). Known-item recall 1.0 (2 seeds).

## References

Numbered by first citation. BibTeX in the same order and keys: [decoding-imagined-and-spoken-phrases-from-non-invasive-neural-meg-signals.bib](decoding-imagined-and-spoken-phrases-from-non-invasive-neural-meg-signals.bib).

1. <a id="ref-1"></a>Dash, D., Ferrari, P., Wang, J. “Decoding Imagined and Spoken Phrases From Non-invasive Neural (MEG) Signals.” *Frontiers in Neuroscience*, 2020, 14, 290. doi:[10.3389/fnins.2020.00290](https://doi.org/10.3389/fnins.2020.00290). Target. Published version read. [wiki: doi-10.3389-fnins.2020.00290](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnins.2020.00290/article.md) [wiki: doi-10.3389-fnhum.2020.00290](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnhum.2020.00290/article.md) [wiki: pmc-7154084-megphrases](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-7154084-megphrases/article.md)
2. <a id="ref-2"></a>Dash, D., Wisler, A., Ferrari, P., Davenport, E. M., Maldjian, J., Wang, J. “MEG Sensor Selection for Neural Speech Decoding.” *IEEE Access*, 2020, 8, 182320-182337. doi:[10.1109/ACCESS.2020.3028831](https://doi.org/10.1109/ACCESS.2020.3028831). Same laboratory and paradigm; state of the art for M06 and M12. [later] [wiki: pmc-7668411-megsel](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-7668411-megsel/article.md) [wiki: doi-10.1109-access.2020.3028831](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-access.2020.3028831/article.md) [wiki: pmc-7668411-meg-sensor-selection](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-7668411-meg-sensor-selection/article.md)
3. <a id="ref-3"></a>Wang, K., Wang, X., Li, G. “Simulation Experiment of BCI Based on Imagined Speech EEG Decoding.” *arXiv preprint*, 2017. arXiv:[1705.07771](https://arxiv.org/abs/1705.07771). Prior; closest earlier CNN decoder in the population. [wiki: arxiv-1705.07771](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1705.07771/article.md)
4. <a id="ref-4"></a>Jhilal, S., Martin, S., Giraud, A. “Transfer Learning from ImageNet for MEG-Based Decoding of Imagined Speech.” *IEEE International Symposium on Biomedical Imaging (ISBI)*, 2026. arXiv:[2601.15909](https://arxiv.org/abs/2601.15909). State of the art for M03 (pretraining ablation). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/transfer-learning-from-imagenet-for-meg-based-decoding-of-imagined-speech) [wiki: arxiv-2601.15909](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2601.15909/article.md) [wiki: arxiv-2601.15909-imgmeg](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2601.15909-imgmeg/article.md)
5. <a id="ref-5"></a>Dash, D., Ferrari, P., Heitzman, D., Wang, J. “Decoding speech from single trial MEG signals using convolutional neural networks and transfer learning.” *41st Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)*, 2019, 5531-5535. doi:[10.1109/EMBC.2019.8857874](https://doi.org/10.1109/EMBC.2019.8857874). Earlier conference version by the same group. [concurrent]
6. <a id="ref-6"></a>Suppes, P., Lu, Z., Han, B. “Brain wave recognition of words.” *Proceedings of the National Academy of Sciences*, 1997, 94(26), 14965-14969. doi:[10.1073/pnas.94.26.14965](https://doi.org/10.1073/pnas.94.26.14965). Prior; EMG recorded during internal speech. [wiki: pmc-25146-brainwave](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-25146-brainwave/article.md)
7. <a id="ref-7"></a>Rezazadeh Sereshkeh, A. “Development of a Hybrid Brain-Computer Interface Based on Imagined Speech Using Electroencephalography and Near-Infrared Spectroscopy.” *University of Toronto (PhD thesis)*, 2018. <http://hdl.handle.net/1807/97898> Prior; across-day evaluation and EMG-removal re-test. [wiki: oa-W3088488915](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/oa-W3088488915/article.md)
