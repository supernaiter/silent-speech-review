# Transfer Learning from ImageNet for MEG-Based Decoding of Imagined Speech

Jhilal S, Martin S, Giraud AL. IEEE International Symposium on Biomedical Imaging (ISBI), 2026. [arXiv:2601.15909](https://arxiv.org/abs/2601.15909)

## Verdict

The paper [[1]](#ref-1) changes training (M03), fine-tuning ImageNet-pretrained ResNet-18 and ViT-Tiny on MEG scalograms, and the representation (M06), a learned three-map sensor projection. M03 is standard: ImageNet-pretrained CNNs on MEG Morlet scalograms of imagined phrases came earlier, in work the paper cites only for its decoding result [[2]](#ref-2), as did a frozen ImageNet ResNet50 on imagined-speech EEG [[3]](#ref-3). The new evidence is an ablation over 21 participants with leave-one-subject-out testing: removing pretraining costs 5.7 to 8.9 points of balanced accuracy across the three tasks and both splits of Table 4 (inference). M06 is standard: the projection is tested against PCA-3, not against the earlier sensor mosaic [[2]](#ref-2). The strongest confound is in M12: the binary tasks contrast imagery with rest and with silent reading that always precedes it (Fig. 1), and no EMG separates imagery from movement, unlike [[4]](#ref-4); only the vowel task, 51.7% for held-out participants against 33% chance (Table 3), bears on speech content.

## Against the field, component by component

### M03 Training: ImageNet-pretrained vision backbone

**Usual approach:** Of 8 unique ledger studies on ImageNet backbones for neural speech decoding (pattern match, Appendix), 5 use an ImageNet CNN on time-frequency images and 2 an ImageNet ViT. The paper follows the majority and adds a ViT, training only the last block, head and projection (Sec. 2.5).

**State of the art:** For five imagined MEG phrases (2020, prior), ImageNet CNNs on sensor-mosaic scalograms reached 93.24% in the imagination stage, within subject on a 70/15/15 split [[2]](#ref-2). The paper's three-vowel task reaches 60.6% pooled and 51.7% held-out (Table 3); tasks and splits differ, so the gap says nothing about the method.

Removing ImageNet weights lowers imagery versus silence from 90.4% to 81.6% pooled and held-out vowels from 51.7% to 46.0% (Table 4), relative drops of 9.7% and 11.0% (inference). The earlier MEG work compared pretrained CNNs only with a shallow network on statistical features [[2]](#ref-2). Verdict: standard; the design is prior, the ablation is the contribution.

### M06 Representation: scalograms with a learned sensor projection

**Usual approach:** Among 43 unique ledger studies of imagined-speech MEG decoding (pattern match, Appendix), raw time-series CNNs appear in 8, scalogram inputs in 7 and scalogram images with a pretrained CNN in 3. The paper mixes 248-channel scalograms into three maps with a 1×1 convolution (Sec. 2.4).

**State of the art:** Dash et al. (2020, prior) tiled scalograms of 196 sensors into one 14×14 image, which beat per-sensor scalograms in all three task stages [[2]](#ref-2).

The only control, PCA-3, costs 3.9 points pooled for imagery versus silence and 3.5 for vowels, pooled and held-out alike (inference), and full fine-tuning costs 3.0 points pooled with overlapping 95% intervals (Table 4; inference). Verdict: standard; the gain over a fixed layout is untested.

### M12 Evaluation: null model and task confounds

**Usual approach:** Label or trial permutation is the most frequent empirical null (45 of 132 unique studies, pattern match, Appendix), as in the paper's 10,000-iteration tests (Sec. 2.5).

**State of the art:** Concurrent MEG work (2026) shuffles only the pairing under test, so the null passes through the full decoder [[5]](#ref-5).

A chance-level null does not remove confounds. Silence comes from inter-trial rest (Sec. 2.2), and the authors concede engagement or sensorimotor activity may drive it (Sec. 4). Imagery always follows reading of the same sentence (Fig. 1). Earlier MEG imagery work recorded lip and jaw EMG and showed micromovements did not discriminate syllables [[4]](#ref-4), and within-subject MEG decoding was above chance before any stimulus [[2]](#ref-2). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Imagined and silently read French sentences | Speech production tasks (slot-filled 4,015) | – | standard |
| M02 Training-only supervision | Condition and vowel labels only | Paired audio or text labels (slot-filled 31) | – | standard |
| M03 Training and adaptation | ImageNet ResNet-18 / ViT-Tiny, last block tuned | ImageNet CNN on time-frequency images (pattern match 5) | 93.24%, 5 imagined phrases [[2]](#ref-2) | standard |
| M04 Use-time action | Offline imagined-speech epochs | Overt or silent production (slot-filled 6,538) | – | standard |
| M05 Sensors | 248-magnetometer MEG, 1 kHz | MEG or EEG (slot-filled 8,898) | – | standard |
| M06 Processing and decoding | Scalograms, learned 3-map projection | Raw time-series CNN (pattern match 8) | 14x14 sensor mosaic [[2]](#ref-2) | standard |
| M07 Lexicon and LM | None | None (slot-filled 120) | – | not applicable |
| M08 Output | Condition or vowel labels | Class labels (slot-filled 3,760) | – | standard |
| M09 Confirmation | Offline | None (slot-filled 82) | – | not applicable |
| M10 Correction | Offline | None (slot-filled 82) | – | not applicable |
| M11 Reference construction | Cue timing, 400 ms per syllable | Corpus or cue labels (slot-filled 239) | – | standard |
| M12 Evaluation | Permutation null; SAP, LOSO | Label or trial permutation (pattern match 45) | Pairing-only shuffle [[5]](#ref-5) | standard |
| M13 Device and cost | Laboratory MEG, offline | Laboratory (slot-filled 6,721) | – | standard |

## Where the claims outrun the evidence

- The introduction presents image-like TF input for pretrained vision models as the proposal; [[2]](#ref-2) did this on MEG and is cited only for imagined sentences.
- "Shared neural representations across participants" (Abstract; Table 3): above-chance LOSO on imagery versus rest or reading can reflect task state; only vowels, 18.4 points above chance (inference), speak to content.
- Pooled ablation gaps of 3.0 to 3.9 points (inference) rest on unreported seeds and no stated selection data (Sec. 2.5).
- "Imagery-locked" (Sec. 5): syllables last 400 ms but epochs span 800 ms (inference), so windows overlap neighbouring syllables.

## What the field needs next

- M06: the 14×14 mosaic [[2]](#ref-2) against the learned projection with one backbone.
- M12: counterbalanced imagery and reading, with articulatory EMG as in [[4]](#ref-4).
- M03: repeated seeds, and vowels on epochs that do not overlap adjacent syllables.

## Questions for the authors

- Which data selected checkpoints and hyperparameters within each fold?
- Which baseline interval was used for z-scoring?
- What is the bootstrap resampling unit?
- Can a participant contribute to both training and test folds in SAP?

## Appendix: literature search

- M03 imagenet-pretrained-vision-backbone-neural-speech (new). Inclusion rule: speech or language decoders from EEG, MEG or intracranial recordings that initialize a vision backbone pretrained on natural images (ImageNet CNN or ViT) and fine-tune it, or train a head on it, using time-frequency or other image-like neural inputs; decoding of viewed images is excluded; non-speech imagery and reviews remain as pattern matches (upper bound); versions counted once. Ledger counts: slot-filled 1,526 unique studies (M03); pattern match 8 unique studies (10 folders). Design counts (pattern match, full text): ImageNet CNN on time-frequency images 5 (one study indexed under two DOIs), ImageNet ViT 2. Read in full: [[2]](#ref-2) (prior; state of the art), [[3]](#ref-3) (prior). Known-item recall 1.0 (2 seeds).
- M06 imagined-speech-meg-classification (new). Inclusion rule: studies that decode imagined, covert or inner speech, or contrast it with other conditions, from MEG and report a classification score; perceived-only, overt-only and EEG-only studies are excluded; reviews remain as pattern matches (upper bound); versions counted once. Ledger counts: slot-filled 7,345 unique studies (M06); pattern match 43 unique studies (60 folders). Design counts (pattern match, full text): raw time-series CNN 8, scalogram or time-frequency input 7, time-frequency image with pretrained CNN 3. Read in full: [[2]](#ref-2) (state of the art), [[4]](#ref-4), [[3]](#ref-3) (prior). Known-item recall 1.0 (1 seed).
- M12 null-model-construction-neural-decoding (published table, reused). Inclusion rule: neural decoding or neural-response prediction studies that test significance against an empirical null built by shuffling or permuting the data rather than only against theoretical chance. Ledger counts: slot-filled 6,960 unique studies (M12); pattern match 132 unique studies (157 folders). Usual design: label or trial permutation 45 (pattern match). Read in full: [[4]](#ref-4), [[2]](#ref-2) (prior).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Jhilal, S., Martin, S., Giraud, A. “Transfer Learning from ImageNet for MEG-Based Decoding of Imagined Speech.” *IEEE International Symposium on Biomedical Imaging (ISBI)*, 2026. doi:[10.48550/arXiv.2601.15909](https://doi.org/10.48550/arXiv.2601.15909). arXiv:[2601.15909](https://arxiv.org/abs/2601.15909). Target. arXiv:2601.15909 v1 read. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/transfer-learning-from-imagenet-for-meg-based-decoding-of-imagined-speech) [wiki: arxiv-2601.15909](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2601.15909/article.md) [wiki: arxiv-2601.15909-imgmeg](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2601.15909-imgmeg/article.md)
2. <a id="ref-2"></a>Dash, D., Ferrari, P., Wang, J. “Decoding Imagined and Spoken Phrases From Non-invasive Neural (MEG) Signals.” *Frontiers in Neuroscience*, 2020, 14, 290. doi:[10.3389/fnins.2020.00290](https://doi.org/10.3389/fnins.2020.00290). [wiki: doi-10.3389-fnins.2020.00290](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnins.2020.00290/article.md) [wiki: doi-10.3389-fnhum.2020.00290](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnhum.2020.00290/article.md)
3. <a id="ref-3"></a>Panachakel, J. T., Ganesan, R. A. “Decoding Imagined Speech From EEG Using Transfer Learning.” *IEEE Access*, 2021, 9, 135371-135385. doi:[10.1109/ACCESS.2021.3116196](https://doi.org/10.1109/ACCESS.2021.3116196). [wiki: doi-10.1109-access.2021.3116196](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-access.2021.3116196/article.md)
4. <a id="ref-4"></a>Orpella, J., Mantegna, F., Assaneo, M. F., Poeppel, D. “Speech imagery decoding as a window to speech planning and production.” *bioRxiv*, 2022. doi:[10.1101/2022.05.30.494046](https://doi.org/10.1101/2022.05.30.494046). [wiki: doi-10.1101-2022.05.30.494046](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2022.05.30.494046/article.md)
5. <a id="ref-5"></a>Maghsoudi, M., Shamma, S. “Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping.” *arXiv preprint*, 2026. arXiv:[2605.08075](https://arxiv.org/abs/2605.08075). [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/zero-shot-imagined-speech-decoding-via-imagined-to-listened-meg-mapping) [wiki: arxiv-2605.08075](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2605.08075/article.md) [wiki: arxiv-2605-08075-zeromeg](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2605-08075-zeromeg/article.md) [wiki: arxiv-2605.08075-i2lmeg](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2605.08075-i2lmeg/article.md)
