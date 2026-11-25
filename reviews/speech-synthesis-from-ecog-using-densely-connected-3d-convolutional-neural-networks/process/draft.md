# Speech Synthesis from ECoG using Densely Connected 3D Convolutional Neural Networks

Angrick, Herff, Mugler, Tate, Slutzky, Krusienski, Schultz. Journal of Neural Engineering, 2019. [doi:10.1088/1741-2552/ab0c59](https://doi.org/10.1088/1741-2552/ab0c59) (bioRxiv [10.1101/478644](https://doi.org/10.1101/478644), 2018)

## Verdict

The paper changes two components: the neural-to-spectrogram regressor (M06), a per-participant 3D DenseNet over the electrode grid and time, and the waveform generator (M08), a WaveNet vocoder trained on a separate single-speaker corpus [[1]](#ref-1). Both are standard. The 3D convolution over the grid anticipated today's best ECoG decoders [[2]](#ref-2), but no simpler regressor is tested, so the claim that dense connectivity suits small data (Abstract) is unsupported in the paper. [Later] head-to-head tests give mixed results: a recurrent encoder-decoder beat it on sEEG [[3]](#ref-3), and it was only marginally ahead of a sequence model on HD ECoG [[4]](#ref-4). The evaluation (M12) has a strong retrained shuffle null but no listener or identification test, so "high quality" and "often intelligible" (§1) and "most natural" (Abstract) are assertions, not results. The "first" claim (§4) is scoped to high-quality speech, which the paper does not measure, while the [concurrent] sentence-level system [[5]](#ref-5) backed the same milestone with a listener test.

## Against the field, component by component

### M06 Processing: neural-to-spectrogram regressor

**Usual approach:** Among 180 unique studies on intracranial speech synthesis (pattern match, upper bound, Appendix), the full texts most often name recurrent sequence models (79), then linear regression (67), transformers (65) and 3D convolution (47); DenseNet appears in 11. The target treats the 8 × 8 grid and nine temporal offsets as a 3D volume (§2.2) for an 83,000-parameter DenseNet (§2.4).

**State of the art:** A [later] 2024 framework reaches a mean spectrogram PCC of 0.806 over 48 ECoG participants with a non-causal 3D ResNet (causal 0.797), against 0.745 for an LSTM [[2]](#ref-2). The target's six participants range from r = 0.19 to 0.69 (§3; mean 0.41 (inference)); tasks and data differ, so this is context, not a controlled gap.

The design proved well chosen: the best [later] ECoG decoder also uses 3D convolution [[2]](#ref-2). But linear models appear only as motivation (Abstract), and no baseline regressor is trained on the same folds. [Later] tests split: on sEEG, a recurrent encoder-decoder had lower test MSE than the re-run DenseNet in all three participants (P1: 2.1 vs 7.4, Table 1), significant by t-tests [[3]](#ref-3). On HD ECoG, DenseNet's correlation lead over a sequence model was marginal, and the authors declined to prefer convolutional over recurrent models [[4]](#ref-4). Verdict: standard: a competitive architecture, not a demonstrated advantage.

### M08 Output: waveform generation

**Usual approach:** A pretrained neural vocoder is the most frequent waveform step in the same 180-study population (51, pattern match, Appendix), ahead of unit selection (30), parametric vocoders (15) and Griffin-Lim (11). The target's WaveNet, trained on about 24 h of single-speaker LJ-Speech (§2.5), matches today's default.

**State of the art:** The best waveform-level value in the reused table (2024) is a mean MCD of 4.55 dB on a public sEEG word dataset with a WaveGlow vocoder [[6]](#ref-6) ([later]). The best ECoG correlation (2024) uses Griffin-Lim inversion [[2]](#ref-2), so the neural vocoder does not set the state of the art.

The vocoder voice is not the participant's; the claim that it captures "the speaker characteristics of the participants" (§2.5) has no reported measure, and no Griffin-Lim or resynthesis baseline isolates what WaveNet adds. Verdict: standard.

### M12 Evaluation: reconstruction test

**Usual approach:** Of 173 unique neural-reconstruction studies (pattern match, Appendix), 122 report correlation, 45 a human listening test and 20 identification among candidates. The target reports per-bin correlation and STOI against a null that swaps two parts of each recording and retrains, 60 times per participant (§3). This null is stronger than a label shuffle because it keeps the temporal statistics of both signals (inference).

**State of the art:** A [later] 2023 HD ECoG study identifies 12 words from reconstructions at 92–100% (chance 8%) and adds listener judgments at 58–66% (chance 50%) [[4]](#ref-4). The [concurrent] 2019 sentence system reports a median listener-transcription WER of 31% with a 25-word pool [[5]](#ref-5).

Verdict: standard; the missing perceptual test matters most for a paper whose headline is audible speech.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Overt single-word reading | Recorded overt speech (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | 40-bin logMel of paired audio | Paired-audio targets (slot-filled 31) | – | standard |
| M03 Training and adaptation | Per participant, 8.5-12.7 min | Per-participant training (slot-filled 1,526) | – | standard |
| M04 Use-time action | Overt reading | Overt speech (slot-filled 5,595) | – | standard |
| M05 Sensors | 64-ch 8x8 ECoG, 4 mm | Clinical ECoG grid (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | 3D DenseNet over grid x time | Recurrent model (pattern match 79) | [[2]](#ref-2) (2024): PCC 0.806 | standard |
| M07 Lexicon and LM | None | None (slot-filled 119) | – | not applicable |
| M08 Output | WaveNet on LJ-Speech | Neural vocoder (pattern match 51) | [[6]](#ref-6) (2024): MCD 4.55 dB | standard |
| M09 Confirmation | Offline | Offline (slot-filled 82) | – | not applicable |
| M10 Correction | Offline | Offline (slot-filled 82) | – | not applicable |
| M11 Reference construction | Original lapel-mic audio | Recorded audio (slot-filled 234) | – | standard |
| M12 Evaluation | Per-bin r, STOI, retrained null | Correlation (pattern match 122) | [[4]](#ref-4) (2023): 92-100% word ID | standard |
| M13 Device and cost | Offline, not real time | Hardware and cost (slot-filled 6,075) | – | standard |

## Where the claims outrun the evidence

- "High quality", "often intelligible" (§1) and "most natural" (Abstract) rest on selected examples; no listener or identification test is reported (§3).
- The test behind p < 0.001 is not named (§3); STOI is only plotted (Fig. 5c).
- The 5-fold unit is not stated (§3): with 50-ms frames and ±200 ms context (§2.2), frame-level folds would put neighbouring frames of one word on both sides (inference).

## What the field needs next

- M06: linear, MLP, recurrent and 3D-convolutional regressors on the same folds with several seeds, testing the small-data claim where it was made.
- M08: participant-voice vocoder against a corpus vocoder, scored by listeners and speaker similarity.
- M12: word-held-out folds with an identification test and listener transcription, the protocol later used on HD ECoG [[4]](#ref-4).

## Questions for the authors

- Do folds hold out whole words, and do test words occur in training?
- Were normalization statistics and the 20% validation split confined to training folds, and was validation used for selection?
- How many seeds stand behind each participant's correlation?
- Which test produced p < 0.001, and what are the STOI values per participant?

## Appendix: literature search

- M06 intracranial-synthesis-decoder-architecture. Inclusion rule: studies that reconstruct speech acoustics from intracranial recordings during overt, mouthed, attempted or imagined speech, classified by the regressor their full text names; a study counts under every design it names, including related-work mentions; heard-speech and text-only decoders excluded; versions once. Ledger: 7,345 slot-filled, 180 pattern match (unique studies). Full-text pattern counts: recurrent 79, linear regression 67, transformer 65, 3D convolution 47, unit selection 34, DenseNet 11. Usual design: recurrent sequence model, 79 (pattern match). Read in full: [[2]](#ref-2), [[4]](#ref-4), [[3]](#ref-3). Known-item recall 1.0.
- M08 intracranial-synthesis-waveform-generation (reused published table). Inclusion rule: intracranial production-speech acoustic reconstruction, classified by how predicted features become a waveform. Ledger: 3,268 slot-filled, 180 pattern match (unique studies). Counts: neural vocoder 51, unit selection 30, parametric vocoder 15, Griffin-Lim 11. Usual design: pretrained neural vocoder, 51 (pattern match). Read in full: [[6]](#ref-6). Known-item recall 1.0.
- M12 neural-speech-reconstruction-identification-test (reused published table). Inclusion rule: neural-to-acoustic reconstruction studies, classified by evaluation (correlation, identification, MCD, listener test, STOI). Ledger: 6,960 slot-filled, 173 pattern match (unique studies). Counts: correlation 122, listener test 45, MCD 31, STOI 23, identification 20. Usual design: correlation, 122 (pattern match). Read in full: [[4]](#ref-4), [[5]](#ref-5). Known-item recall 0.67.

## References

Numbered by first citation. BibTeX in the same order and keys: [speech-synthesis-from-ecog-using-densely-connected-3d-convolutional-neural-networks.bib](speech-synthesis-from-ecog-using-densely-connected-3d-convolutional-neural-networks.bib).

1. <a id="ref-1"></a>Angrick, M., Herff, C., Mugler, E., Tate, M. C., Slutzky, M. W., Krusienski, D. J., et al. “Speech Synthesis from ECoG using Densely Connected 3D Convolutional Neural Networks.” *Journal of Neural Engineering*, 2019, 16(3), 036019. doi:[10.1088/1741-2552/ab0c59](https://doi.org/10.1088/1741-2552/ab0c59). Target. Read as the PMC author manuscript; first public as bioRxiv 10.1101/478644 v1 (2018-11-27). [wiki: doi-10.1088-1741-2552-ab0c59](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552-ab0c59/article.md) [wiki: pmc-6822609-3dcnn](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-6822609-3dcnn/article.md) [wiki: doi-10.1101-478644](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-478644/article.md)
2. <a id="ref-2"></a>Chen, X., Wang, R., Khalilian-Gourtani, A., Yu, L., Dugan, P., Friedman, D., et al. “A neural speech decoding framework leveraging deep learning and speech synthesis.” *Nature Machine Intelligence*, 2024. doi:[10.1038/s42256-024-00824-8](https://doi.org/10.1038/s42256-024-00824-8). Later; state of the art for M06 (48 ECoG participants, 3D ResNet vs Swin vs LSTM). [later] [wiki: doi-10.1038-s42256-024-00824-8](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s42256-024-00824-8/article.md) [wiki: doi-10.1101-2023.09.16.558028](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2023.09.16.558028/article.md) [wiki: pmc-12965882-nmidecode](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12965882-nmidecode/article.md) [wiki: pmc-12965882-nsdecode](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12965882-nsdecode/article.md)
3. <a id="ref-3"></a>Kohler, J., Ottenhoff, M. C., Goulis, S., Angrick, M., Colon, A. J., Wagner, L., et al. “Synthesizing Speech from Intracranial Depth Electrodes using an Encoder-Decoder Framework.” *Neurons, Behavior, Data analysis, and Theory*, 2022. doi:[10.51628/001c.57524](https://doi.org/10.51628/001c.57524). arXiv:[2111.01457](https://arxiv.org/abs/2111.01457). Later; head-to-head test against the target's DenseNet on sEEG. [later] [wiki: arxiv-2111.01457](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2111.01457/article.md)
4. <a id="ref-4"></a>Berezutskaya, J., Freudenburg, Z. V., Vansteensel, M. J., Aarnoutse, E. J., Ramsey, N. F., van Gerven, M. A. J. “Direct speech reconstruction from sensorimotor brain activity with optimized deep learning models.” *Journal of Neural Engineering*, 2023, 20. doi:[10.1088/1741-2552/ace8be](https://doi.org/10.1088/1741-2552/ace8be). Later; MLP vs DenseNet vs seq2seq on HD ECoG; state of the art for M12. [later] [wiki: doi-10.1088-1741-2552-ace8be](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552-ace8be/article.md) [wiki: pmc-10510111-berezutskaya](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10510111-berezutskaya/article.md) [wiki: pmc-10510111-recon](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10510111-recon/article.md)
5. <a id="ref-5"></a>Anumanchipalli, G. K., Chartier, J., Chang, E. F. “Speech synthesis from neural decoding of spoken sentences.” *Nature*, 2019, 568, 493-498. doi:[10.1038/s41586-019-1119-1](https://doi.org/10.1038/s41586-019-1119-1). Concurrent; ECoG sentence synthesis with listener transcription. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/speech-synthesis-from-neural-decoding-of-spoken-sentences) [wiki: doi-10.1038-s41586-019-1119-1](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-019-1119-1/article.md) [wiki: pmc-9714519-speechsynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-9714519-speechsynth/article.md)
6. <a id="ref-6"></a>Arthur, F. V., Csapó, T. G. “Speech synthesis from intracranial stereotactic Electroencephalography using a neural vocoder.” *Infocommunications Journal*, 2024, 16(1). doi:[10.36244/icj.2024.1.6](https://doi.org/10.36244/icj.2024.1.6). Later; M08 state of the art in the reused published table (MCD on a public sEEG word dataset). [later] [wiki: doi-10.36244-icj.2024.1.6](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.36244-icj.2024.1.6/article.md)
