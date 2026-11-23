# CAT-Net: A Cross-Attention Tone Network for Cross-Subject EEG-EMG Fusion Tone Decoding

Zhuang, Huang, Yu, Zou, Ju. arXiv preprint, 2025 (first page carries an AAAI 2026 copyright line). [arXiv:2511.10935](https://arxiv.org/abs/2511.10935)

## Verdict

The paper [[1]](#ref-1) changes EEG-EMG fusion (M06), EEG channel selection (M05) and subject-adversarial training (M03) for four-class Mandarin tone decoding; all three are standard. Cross-attention fusion is new among EEG-EMG decoders (Appendix), but its support is one five-fold ablation in which every ablated network falls below a DeepConvNet fed concatenated EEG and EMG (Table 3; Table 6). No result separates EEG from EMG (Tables 1-6), so the paper does not show that EEG carries tone information. The subject discriminator lifts the mean from 84.69% to 85.10% (Table 5). The leave-one-subject-out mean of 85.10% stands.

## Against the field, component by component

### M06 Processing: EEG-EMG fusion form

**Usual approach:** Of 30 unique studies whose ledger records both scalp EEG and surface EMG (pattern match), 8 treat EMG as an EEG artifact, 4 concatenate features and 4 fuse late; none names cross-modal attention (Appendix).

**State of the art:** Pooled EEG+EMG pretraining reaches 95.3% on 64 silent words, within-participant session split (2025) [[2]](#ref-2) [concurrent]; a different task.

Li et al. compared fusion forms with single modalities: sEMG alone 10.52% CER, EEG alone 38.85%, feature concatenation 13.14% [[3]](#ref-3). The paper has no single-modality model (Tables 1-6, C1-C3). Removing cross-attention gives 77.63% precision, removing the BiLSTM 78.42% (Table 6), while DeepConvNet on concatenated inputs reaches 86.56% average (Table 3). Against that baseline the gain is 1.52 points, 1.8% relative (inference), from one run. Verdict: standard; no repetition.

### M05 Sensors: EEG channel subset

**Usual approach:** Of 34 unique EEG studies recording a channel subset or reduction (pattern match), 6 rank channels by post-hoc attribution and 5 by anatomy; only the target uses trained attention weights (Appendix). An anatomical 6-electrode subset reached 80.1% on four imagined tones [[4]](#ref-4).

**State of the art:** Across three imagined-speech datasets, 50% of 64 channels can be removed without significant loss, and the best positions differ between datasets (2025) [[5]](#ref-5) [concurrent].

Cutting the full EEG set (88.45%) to 20 channels costs 0.37 points (inference); 5 channels still give 86.92%, with EMG always present (Table 1). A 1.53-point spread from 5 channels to the full set (inference) fits EMG carrying the decision. One pooled subset removing 69% of channels (inference) serves all held-out subjects; the ranking data are not stated (Sec. Channel Selection). Verdict: standard.

### M03 Training: adversarial subject removal

**Usual approach:** Gradient reversal against a speaker or subject classifier, 6 of 18 unique studies (pattern match, Appendix), as in [[6]](#ref-6).

**State of the art:** An intracortical decoder ablates its session adversary over 4 seeds: validation phoneme error rises from 26.30% to 31.95% (2026) [[7]](#ref-7) [concurrent].

Here the discriminator moves leave-one-subject-out accuracy from 84.69% to 85.10%, 0.5% relative (inference), in single runs (Table 5); the authors call the gain slight. Verdict: standard.

### M12 Evaluation: held-out subjects

**Usual approach:** Leave-one-subject-out, 46 of 153 unique EEG studies (pattern match, Appendix), as here.

**State of the art:** 82.4% on 8 inner-speech words, leave-one-subject-out over 4 participants (2025) [[8]](#ref-8) [concurrent]; chance is 12.5% there against 25% here (inference).

Per-subject accuracy spans 53.33% to 95.00% (Table 4). The five-fold split unit is not stated (Sec. Baseline Comparisons). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Prompted characters, audible and silent | Cued production (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Tone and subject labels | Prompt class labels (slot-filled 31) | – | standard |
| M03 Training and adaptation | Gradient-reversal subject discriminator | Gradient reversal (pattern match 6) | 26.30% vs 31.95% PER, 4 seeds [[7]](#ref-7) | standard |
| M04 Use-time action | Audible and silent articulation | Overt or silent speech (slot-filled 5,595) | – | standard |
| M05 Sensors | 20 of 64 EEG channels by attention weight, 5 EMG | Post-hoc attribution (pattern match 6) | 50% of 64 channels removed, 3 datasets [[5]](#ref-5) | standard |
| M06 Processing and decoding | Bidirectional EEG-EMG cross-attention | EMG as EEG artifact (pattern match 8) | 95.3%, 64 silent words [[2]](#ref-2) | standard |
| M07 Lexicon and LM | None | Use-time lexicon or LM (slot-filled 119) | – | not applicable |
| M08 Output | Four tone classes | Class label (slot-filled 3,268) | – | standard |
| M09 Confirmation | None | Confirmation step (slot-filled 82) | – | not applicable |
| M10 Correction | None | Correction step (slot-filled 82) | – | not applicable |
| M11 Reference construction | Prompted-character tone labels | Stimulus labels (slot-filled 234) | – | standard |
| M12 Evaluation | Five-fold CV and LOSO, 10 subjects | Leave-one-subject-out (pattern match 46) | 82.4%, 8 words, 4 subjects [[8]](#ref-8) | standard |
| M13 Device and cost | Offline; no latency or device figures | Lab acquisition (slot-filled 6,075) | – | not reported |

## Where the claims outrun the evidence

- "Cross-attention is indispensable" (Sec. Cross-Attention Mechanism): all ablations lose 9.66 to 11.62 points (inference) and fall below a concatenation baseline (Table 3; Table 6), so they test a weakened network, not the fusion form.
- "Minimal-channel decoding" (Abstract) is shown only with all five EMG channels present (Table 1).
- Appendix C claims the best accuracy on all ten subjects; Table C2 has CAT-Net below GAT on S10, Table 4 below DeepConvNet on S9.
- 88.08% is accuracy in the text and average precision in Table 3; "significant margin" has no test or interval (Appendix C).

## What the field needs next

- M06: identical encoders fused by concatenation, and EEG-only and EMG-only models, with seeds.
- M05: channel ranking nested inside each held-out-subject fold.
- M12: character-disjoint splits (each character is shown four times, Sec. Data Collection) with confidence intervals.

## Questions for the authors

- Is the five-fold split by trial, repetition, character or subject?
- Which data ranked the channels, and which drove early stopping in each held-out-subject run?
- What replaces cross-attention in "w/o ct", and how many seeds stand behind each table?
- Is the Eq. 4 centroid loss, absent from Algorithm 1, used?

## Appendix: literature search

- **M06 / eeg-emg-fusion-architecture.** Inclusion rule: Speech, tone or articulation decoders that record scalp EEG together with surface EMG and combine the two inside one model; the design value is the fusion form named in the full text (cross-modal or bidirectional attention, feature concatenation, late or decision-level fusion), and studies that record EMG only as an EEG artifact are counted separately. Boundary: non-speech EEG-EMG fusion (limb movement), reviews and datasets without decoding are excluded from the usual-approach reading but stay in the pattern-match population; versions of one study count once. Ledger counts: slot-filled 7,345 unique studies; pattern match 30 unique studies (41 folders). Design counts (full-text pattern match over the 30): EMG as EEG artifact 8, feature concatenation 4, late or decision-level fusion 4, cross-modal attention 0. Usual design: EMG as EEG artifact, 8 (pattern match). Read in full: [[3]](#ref-3) (prior), [[2]](#ref-2) (state of the art). Known-item recall 1.0 (2 seeds).
- **M05 / attention-weight-eeg-channel-subset.** Inclusion rule: Neural signal speech or tone decoding studies that shrink the recording set for the main experiment by ranking channels with trained-model attention weights (or similar attribution) and keeping a top subset, and that report a full-versus-reduced accuracy comparison. Boundary: hardware-only channel counts, exhaustive or greedy selection without attention, EMG-only electrode subsets and papers with no full-versus-reduced comparison are excluded; selecting channels with data spanning test folds or subjects is included but flagged; versions of one study count once. Ledger counts: slot-filled 7,329 unique studies; pattern match 34 unique studies (42 folders). Design counts (full-text pattern match over the 34): post-hoc attribution 6, anatomical prior 5, trained attention weights 1 (the target), search-based selection 1. Usual design: post-hoc attribution, 6 (pattern match). Read in full: [[4]](#ref-4) (prior), [[5]](#ref-5) (state of the art). Known-item recall 0.5 (2 seed ids).
- **M03 / adversarial-speaker-removal-from-signal-encoder** (published topic table, reused). Inclusion rule: Studies that decode speech or text from a non-acoustic speech signal (lip or face video, articulatory imaging, EMG, EEG/ECoG/intracortical) and train the signal encoder against a speaker, subject or session classifier (gradient reversal, entropy-maximising or confusion loss, mutual-information penalty, or a VAE split of identity and content) to remove identity from the content representation. Boundary: GAN discriminators on the generated audio, plain multi-speaker training, and speaker classifiers used only for evaluation are excluded; versions count once; the pattern match is an upper bound. Ledger counts: slot-filled 1,526 unique studies; pattern match 18 unique studies. Usual design: gradient-reversal speaker or subject classifier on the signal encoder, 6 (pattern match), the target one of them. Read in full: [[6]](#ref-6) (prior), [[7]](#ref-7) ([concurrent]). Known-item recall 1.0.
- **M12 / eeg-held-out-subject-test** (published topic table, reused). Inclusion rule: EEG decoding studies that report accuracy on subjects whose data were not used to train the decoder (leave-one-subject-out, a fixed set of held-out subjects, or subject-independent cross-validation). Boundary: within-subject cross-validation only, fine-tuning on the test subject's labeled trials before scoring (counted, but recorded as calibrated transfer), and reviews are excluded; versions of one study count once. Ledger counts: slot-filled 6,960 unique studies; pattern match 153 unique studies. Usual design: leave-one-subject-out over all subjects, 46 (pattern match); fixed held-out subjects 41. Read in full: [[8]](#ref-8) (state of the art).

## References

Numbered by first citation. BibTeX in the same order and keys: [cat-net-a-cross-attention-tone-network-for-cross-subject-eeg-emg-fusion-tone-decoding.bib](cat-net-a-cross-attention-tone-network-for-cross-subject-eeg-emg-fusion-tone-decoding.bib).

1. <a id="ref-1"></a>Zhuang, Y., Huang, C., Yu, Z., Zou, Y., Ju, J. “CAT-Net: A Cross-Attention Tone Network for Cross-Subject EEG-EMG Fusion Tone Decoding.” *arXiv preprint (first page carries an AAAI 2026 copyright line)*, 2025. arXiv:[2511.10935](https://arxiv.org/abs/2511.10935). arXiv v1 read [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/cat-net-a-cross-attention-tone-network-for-cross-subject-eeg-emg-fusion-tone-decoding) [wiki: arxiv-2511.10935](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2511.10935/article.md) [wiki: arxiv-2511.10935-catnet](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2511.10935-catnet/article.md)
2. <a id="ref-2"></a>Inoue, M., Sato, M., Tomeoka, K., Nah, N., Hatakeyama, E., Arulkumaran, K., et al. “A Silent Speech Decoding System from EEG and EMG with Heterogenous Electrode Configurations.” *Proc. Interspeech 2025*, 2025, 5603–5607. doi:[10.21437/Interspeech.2025-1183](https://doi.org/10.21437/Interspeech.2025-1183). arXiv:[2506.13835](https://arxiv.org/abs/2506.13835). arXiv v1 read; venue confirmed in Crossref [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-silent-speech-decoding-system-from-eeg-and-emg-with-heterogenous-electrode-configurations) [wiki: arxiv-2506.13835](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2506.13835/article.md) [wiki: isca-inoue25b-eegemg](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-inoue25b-eegemg/article.md) [wiki: isca-inoue25b_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-inoue25b_interspeech/article.md)
3. <a id="ref-3"></a>Li, H., Wang, M., Gao, H., Zhao, S., Li, G., Wang, Y. “Hybrid Silent Speech Interface Through Fusion of Electroencephalography and Electromyography.” *Proc. Interspeech 2023*, 2023, 1184–1188. doi:[10.21437/Interspeech.2023-805](https://doi.org/10.21437/Interspeech.2023-805). [wiki: isca-li23l-eegemgssi](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-li23l-eegemgssi/article.md) [wiki: isca-li23l_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-li23l_interspeech/article.md)
4. <a id="ref-4"></a>Li, H., Chen, F. “Classify Imaginary Mandarin Tones with Cortical EEG Signals.” *Proc. Interspeech 2020*, 2020, 4896–4900. doi:[10.21437/Interspeech.2020-1248](https://doi.org/10.21437/Interspeech.2020-1248). [wiki: isca-li20ma-eegtones](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-li20ma-eegtones/article.md) [wiki: isca-li20ma_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-li20ma_interspeech/article.md)
5. <a id="ref-5"></a>Rekrut, M., Ihl, J., Jungbluth, T., Krüger, A. “How low can you go: evaluating electrode reduction methods for EEG-based speech imagery BCIs.” *Frontiers in Neuroergonomics*, 2025, 6. doi:[10.3389/fnrgo.2025.1578586](https://doi.org/10.3389/fnrgo.2025.1578586). Accepted 29 May 2025, published 2 Jul 2025. [concurrent] [wiki: pmc-12263900-elecred](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12263900-elecred/article.md) [wiki: pmc-12263900-electrode](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12263900-electrode/article.md) [wiki: doi-10.3389-fnrgo.2025.1578586](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnrgo.2025.1578586/article.md)
6. <a id="ref-6"></a>Wand, M., Schmidhuber, J. “Improving Speaker-Independent Lipreading with Domain-Adversarial Training.” *Proc. Interspeech 2017*, 2017. doi:[10.21437/Interspeech.2017-421](https://doi.org/10.21437/Interspeech.2017-421). arXiv:[1708.01565](https://arxiv.org/abs/1708.01565). [wiki: arxiv-1708.01565](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1708.01565/article.md) [wiki: isca-wand17_dalip](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-wand17_dalip/article.md) [wiki: isca-wand17-domainadv](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-wand17-domainadv/article.md) [wiki: isca-wand17_lipread](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-wand17_lipread/article.md)
7. <a id="ref-7"></a>Zhang, Z., Li, S., Sabatini, B. L., Aoi, M., Mishne, G. “ALIGN: Adversarial Learning for Generalizable Speech Neuroprosthesis.” *arXiv preprint*, 2026. arXiv:[2603.18299](https://arxiv.org/abs/2603.18299). arXiv v1 read [concurrent] [wiki: arxiv-2603.18299-align](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2603.18299-align/article.md) [wiki: arxiv-2603.18299](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2603.18299/article.md) [wiki: arxiv-2603-18299-align](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2603-18299-align/article.md)
8. <a id="ref-8"></a>Attar, E. T. “Deep learning for inner speech recognition: a pilot comparative study of EEGNet and a spectro-temporal Transformer on bimodal EEG-fMRI data.” *Frontiers in Human Neuroscience*, 2025. doi:[10.3389/fnhum.2025.1668935](https://doi.org/10.3389/fnhum.2025.1668935). Received 21 Jul 2025, accepted 3 Sep 2025. [concurrent] [wiki: doi-10.3389-fnhum.2025.1668935](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnhum.2025.1668935/article.md)
