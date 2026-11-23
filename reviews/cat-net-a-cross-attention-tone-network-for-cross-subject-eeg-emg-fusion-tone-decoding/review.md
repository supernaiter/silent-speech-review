# CAT-Net: A Cross-Attention Tone Network for Cross-Subject EEG-EMG Fusion Tone Decoding

Zhuang, Huang, Yu, Zou, Ju. arXiv preprint, 2025 (first page carries an AAAI 2026 copyright line). [arXiv:2511.10935](https://arxiv.org/abs/2511.10935)

## Verdict

The paper [[1]](#ref-1) changes EEG-EMG fusion (M06), EEG channel selection (M05) and subject-adversarial training (M03) for Mandarin tone decoding; all three are standard. Cross-attention is absent from the 30 ledger EEG-EMG studies (Appendix), but rests on a five-fold ablation with no seed count in which every ablated network falls below a concatenation DeepConvNet (Tables 3, 6). No EEG-only or EMG-only model is reported, and the authors' SHAP analysis finds EMG dominant except for silent Tone 2 (Appendix D), so what EEG adds is not shown. The subject discriminator's gain is 0.5% relative (inference). The leave-one-subject-out mean of 85.10% holds only if channel ranking and early stopping excluded the held-out subject, which the paper does not state.

## Against the field, component by component

### M06 Processing: EEG-EMG fusion form

**Usual approach:** Of 30 unique studies whose ledger records both scalp EEG and surface EMG (pattern match), fused decoders concatenate features (4) or fuse late (4); 8 record EMG only as an EEG artifact, counted separately (Appendix).

**State of the art:** Trained on data from five electrode configurations, an EEG+EMG decoder reaches 95.3% on 64 silent words (healthy participants, within-participant session split, 2025) [[2]](#ref-2) [concurrent]; a different task.

Li et al. report sEMG alone at 10.52% CER, EEG alone 38.85% and feature concatenation 13.14% (Table 3 of [[3]](#ref-3)). Its one-direction fusion rows drop an attention direction, not a signal (Sec. Cross-Attention Mechanism). Removing cross-attention gives 77.63% precision (Table 6, five-fold), while DeepConvNet on concatenated inputs reaches 86.56% (Table 3): a 1.52-point gain, 1.8% relative (inference), with no seed count. None of the 30 ledger studies, including [[3]](#ref-3) (prior) and [[2]](#ref-2) [concurrent], names cross-modal attention (Appendix). Verdict: standard; the effect is not separated from EMG or repeated.

### M05 Sensors: EEG channel subset

**Usual approach:** Of 34 unique EEG studies reducing channels (pattern match), 6 rank them by post-hoc attribution and 5 by anatomy; only the target uses trained attention weights (Appendix). Six electrodes over Broca's, Wernicke's and primary motor areas gave 80.1% on four imagined tones with audio-visual cues [[4]](#ref-4).

**State of the art:** Across three imagined-speech datasets, 50% of 64 channels can be removed without significant loss; best positions differ by dataset (2025) [[5]](#ref-5) [concurrent].

Cutting the full EEG set (88.45%) to 20 channels costs 0.37 points (inference) and 5 channels give 86.92% (Table 1): the 1.53-point spread (inference) is small, as the authors' SHAP finds EMG dominant (Appendix D). The 20 channels, 69% fewer than the 64-channel montage (inference), serve all later experiments, including leave-one-subject-out; the ranking data are not stated (Sec. Channel Selection). Verdict: standard.

### M03 Training: adversarial subject removal

**Usual approach:** Gradient reversal against a speaker or subject classifier, 6 of 18 unique studies (pattern match, Appendix), as in [[6]](#ref-6).

**State of the art:** Removing an intracortical decoder's session adversary raises validation phoneme error from 26.30% to 31.95% over 4 seeds (2026) [[7]](#ref-7) [concurrent].

Here the discriminator moves leave-one-subject-out accuracy from 84.69% to 85.10%, 0.5% relative (inference), with no seed count (Table 5); the authors call the difference "a slight drop". Verdict: standard.

### M12 Evaluation: held-out subjects

**Usual approach:** Leave-one-subject-out, 46 of 153 unique EEG studies (pattern match, Appendix), as here.

**State of the art:** Nearest comparable: an EEG pilot from an EEG-fMRI dataset reaches 82.4% on 8 inner-speech words, leave-one-subject-out over 4 participants (2025) [[8]](#ref-8) [concurrent]; chance is 12.5% there, 25% here (inference).

Per-subject accuracy spans 53.33% to 95.00% (Table 4). Sec. Cross-Subject Calibration uses no test-subject data, despite its name. Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Prompted characters, audible and silent | Cued production (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Tone and subject labels | Prompt class labels (slot-filled 31) | – | standard |
| M03 Training and adaptation | Gradient-reversal subject discriminator | Gradient reversal (pattern match 6) | 26.30% vs 31.95% PER, 4 seeds [[7]](#ref-7) | standard |
| M04 Use-time action | Audible and silent articulation | Overt or silent speech (slot-filled 5,595) | – | standard |
| M05 Sensors | 20 of 64 EEG channels by attention, 5 EMG | Post-hoc attribution (pattern match 6) | 50% of 64 channels removed, 3 datasets [[5]](#ref-5) | standard |
| M06 Processing and decoding | Bidirectional EEG-EMG cross-attention | Concatenation or late fusion (pattern match 4) | 95.3%, 64 silent words [[2]](#ref-2) | standard |
| M07 Lexicon and LM | None | Use-time lexicon or LM (slot-filled 119) | – | not applicable |
| M08 Output | Four tone classes | Class label (slot-filled 3,268) | – | standard |
| M09 Confirmation | None | Confirmation step (slot-filled 82) | – | not applicable |
| M10 Correction | None | Correction step (slot-filled 82) | – | not applicable |
| M11 Reference construction | Prompted-character tone labels | Stimulus labels (slot-filled 234) | – | standard |
| M12 Evaluation | 5-fold CV and LOSO, 10 subjects | Leave-one-subject-out (pattern match 46) | 82.4%, 8 words, 4 subjects, pilot [[8]](#ref-8) | standard |
| M13 Device and cost | Offline | Lab acquisition (slot-filled 6,075) | – | not reported |

## Where the claims outrun the evidence

- "Cross-attention is indispensable" (Sec. Cross-Attention Mechanism): all ablations lose 9.66 to 11.62 points (inference) and fall below a concatenation baseline (Table 3; Table 6), so they test a weakened network, not the fusion form.
- "Minimal-channel decoding" (Abstract) is shown only with all five EMG channels present (Table 1; Table A1).
- Appendix C claims the best accuracy on all ten subjects; CAT-Net trails GAT on S10 (89.17% against 90.00%, Table C2) and DeepConvNet on S9 (94.79% against 95.63%, Table 4), as the main text concedes for S9.
- 88.08% is accuracy in the text and average precision in Table 3; Appendix C's "significant margin" has no test or interval.
- Tone 3 at 20 channels reads 87.29 in Table 1 but 87.27 in Table 3.

## What the field needs next

- M06: identical encoders fused by concatenation, and EEG-only and EMG-only models, with seeds.
- M05: channel ranking nested inside each held-out-subject fold.
- M12: character-disjoint splits with confidence intervals.

## Questions for the authors

- Is the five-fold split by trial, repetition, character or subject?
- Which data ranked the channels, and which drove early stopping in each held-out-subject run?
- What replaces cross-attention in "w/o ct", and how many seeds stand behind each table?

## Appendix: literature search

- **M06 / eeg-emg-fusion-architecture.** Inclusion rule: Speech, tone or articulation decoders that record scalp EEG together with surface EMG and combine the two inside one model; the design value is the fusion form named in the full text (cross-modal or bidirectional attention, feature concatenation, late or decision-level fusion), and studies that record EMG only as an EEG artifact are counted separately. Boundary: non-speech EEG-EMG fusion (limb movement), reviews and datasets without decoding are excluded from the usual-approach reading but stay in the pattern-match population; versions of one study count once. Ledger counts: slot-filled 7,345 unique studies; pattern match 30 unique studies (41 folders). Design counts (full-text pattern match over the 30): EMG as EEG artifact 8, feature concatenation 4, late or decision-level fusion 4, cross-modal attention 0. Usual fused design: feature concatenation 4 and late or decision-level fusion 4, a tie (pattern match); EMG as EEG artifact 8, counted separately. Read in full: [[3]](#ref-3) (prior), [[2]](#ref-2) (state of the art). Known-item recall 1.0 (2 seeds).
- **M05 / attention-weight-eeg-channel-subset.** Inclusion rule: Neural signal speech or tone decoding studies that shrink the recording set for the main experiment by ranking channels with trained-model attention weights (or similar attribution) and keeping a top subset, and that report a full-versus-reduced accuracy comparison. Boundary: hardware-only channel counts, exhaustive or greedy selection without attention, EMG-only electrode subsets and papers with no full-versus-reduced comparison are excluded; selecting channels with data spanning test folds or subjects is included but flagged; versions of one study count once. Ledger counts: slot-filled 7,329 unique studies; pattern match 34 unique studies (42 folders). Design counts (full-text pattern match over the 34): post-hoc attribution 6, anatomical prior 5, trained attention weights 1 (the target), search-based selection 1. Usual design: post-hoc attribution, 6 (pattern match). Read in full: [[4]](#ref-4) (prior), [[5]](#ref-5) (state of the art). Known-item recall 0.5 (2 seed ids).
- **M03 / adversarial-speaker-removal-from-signal-encoder** (published topic table, reused). Inclusion rule: Studies that decode speech or text from a non-acoustic speech signal (lip or face video, articulatory imaging, EMG, EEG/ECoG/intracortical) and train the signal encoder against a speaker, subject or session classifier (gradient reversal, entropy-maximising or confusion loss, mutual-information penalty, or a VAE split of identity and content) to remove identity from the content representation. Boundary: GAN discriminators on the generated audio, plain multi-speaker training, and speaker classifiers used only for evaluation are excluded; versions count once; the pattern match is an upper bound. Ledger counts: slot-filled 1,526 unique studies; pattern match 18 unique studies. Usual design: gradient-reversal speaker or subject classifier on the signal encoder, 6 (pattern match), the target one of them. Read in full: [[6]](#ref-6) (prior), [[7]](#ref-7) ([concurrent]). Known-item recall 1.0.
- **M12 / eeg-held-out-subject-test** (published topic table, reused). Inclusion rule: EEG decoding studies that report accuracy on subjects whose data were not used to train the decoder (leave-one-subject-out, a fixed set of held-out subjects, or subject-independent cross-validation). Boundary: within-subject cross-validation only, fine-tuning on the test subject's labeled trials before scoring (counted, but recorded as calibrated transfer), and reviews are excluded; versions of one study count once. Ledger counts: slot-filled 6,960 unique studies; pattern match 153 unique studies. Usual design: leave-one-subject-out over all subjects, 46 (pattern match); fixed held-out subjects 41. Read in full: [[8]](#ref-8) (state of the art).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Zhuang, Y., Huang, C., Yu, Z., Zou, Y., Ju, J. “CAT-Net: A Cross-Attention Tone Network for Cross-Subject EEG-EMG Fusion Tone Decoding.” *arXiv preprint (first page carries an AAAI 2026 copyright line)*, 2025. arXiv:[2511.10935](https://arxiv.org/abs/2511.10935). arXiv v1 read [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/cat-net-a-cross-attention-tone-network-for-cross-subject-eeg-emg-fusion-tone-decoding) [wiki: arxiv-2511.10935](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2511.10935/article.md) [wiki: arxiv-2511.10935-catnet](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2511.10935-catnet/article.md)
2. <a id="ref-2"></a>Inoue, M., Sato, M., Tomeoka, K., Nah, N., Hatakeyama, E., Arulkumaran, K., et al. “A Silent Speech Decoding System from EEG and EMG with Heterogenous Electrode Configurations.” *Proc. Interspeech 2025*, 2025, 5603–5607. doi:[10.21437/Interspeech.2025-1183](https://doi.org/10.21437/Interspeech.2025-1183). arXiv:[2506.13835](https://arxiv.org/abs/2506.13835). arXiv v1 read; venue confirmed in Crossref [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-silent-speech-decoding-system-from-eeg-and-emg-with-heterogenous-electrode-configurations) [wiki: arxiv-2506.13835](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2506.13835/article.md) [wiki: isca-inoue25b-eegemg](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-inoue25b-eegemg/article.md) [wiki: isca-inoue25b_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-inoue25b_interspeech/article.md)
3. <a id="ref-3"></a>Li, H., Wang, M., Gao, H., Zhao, S., Li, G., Wang, Y. “Hybrid Silent Speech Interface Through Fusion of Electroencephalography and Electromyography.” *Proc. Interspeech 2023*, 2023, 1184–1188. doi:[10.21437/Interspeech.2023-805](https://doi.org/10.21437/Interspeech.2023-805). [wiki: isca-li23l-eegemgssi](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-li23l-eegemgssi/article.md) [wiki: isca-li23l_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-li23l_interspeech/article.md)
4. <a id="ref-4"></a>Li, H., Chen, F. “Classify Imaginary Mandarin Tones with Cortical EEG Signals.” *Proc. Interspeech 2020*, 2020, 4896–4900. doi:[10.21437/Interspeech.2020-1248](https://doi.org/10.21437/Interspeech.2020-1248). [wiki: isca-li20ma-eegtones](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-li20ma-eegtones/article.md) [wiki: isca-li20ma_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-li20ma_interspeech/article.md)
5. <a id="ref-5"></a>Rekrut, M., Ihl, J., Jungbluth, T., Krüger, A. “How low can you go: evaluating electrode reduction methods for EEG-based speech imagery BCIs.” *Frontiers in Neuroergonomics*, 2025, 6. doi:[10.3389/fnrgo.2025.1578586](https://doi.org/10.3389/fnrgo.2025.1578586). Accepted 29 May 2025, published 2 Jul 2025. [concurrent] [wiki: pmc-12263900-elecred](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12263900-elecred/article.md) [wiki: pmc-12263900-electrode](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12263900-electrode/article.md) [wiki: doi-10.3389-fnrgo.2025.1578586](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnrgo.2025.1578586/article.md)
6. <a id="ref-6"></a>Wand, M., Schmidhuber, J. “Improving Speaker-Independent Lipreading with Domain-Adversarial Training.” *Proc. Interspeech 2017*, 2017. doi:[10.21437/Interspeech.2017-421](https://doi.org/10.21437/Interspeech.2017-421). arXiv:[1708.01565](https://arxiv.org/abs/1708.01565). [wiki: arxiv-1708.01565](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1708.01565/article.md) [wiki: isca-wand17_dalip](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-wand17_dalip/article.md) [wiki: isca-wand17-domainadv](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-wand17-domainadv/article.md) [wiki: isca-wand17_lipread](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-wand17_lipread/article.md)
7. <a id="ref-7"></a>Zhang, Z., Li, S., Sabatini, B. L., Aoi, M., Mishne, G. “ALIGN: Adversarial Learning for Generalizable Speech Neuroprosthesis.” *arXiv preprint*, 2026. arXiv:[2603.18299](https://arxiv.org/abs/2603.18299). arXiv v1 read [concurrent] [wiki: arxiv-2603.18299-align](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2603.18299-align/article.md) [wiki: arxiv-2603.18299](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2603.18299/article.md) [wiki: arxiv-2603-18299-align](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2603-18299-align/article.md)
8. <a id="ref-8"></a>Attar, E. T. “Deep learning for inner speech recognition: a pilot comparative study of EEGNet and a spectro-temporal Transformer on bimodal EEG-fMRI data.” *Frontiers in Human Neuroscience*, 2025. doi:[10.3389/fnhum.2025.1668935](https://doi.org/10.3389/fnhum.2025.1668935). Received 21 Jul 2025, accepted 3 Sep 2025. [concurrent] [wiki: doi-10.3389-fnhum.2025.1668935](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnhum.2025.1668935/article.md)
