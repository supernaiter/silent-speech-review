# Relating the Neural Representations of Vocalized, Mimed, and Imagined Speech

Maghsoudi, Chillale, Shamma. arXiv preprint, 2026. [arXiv:2602.22597](https://arxiv.org/abs/2602.22597)

## Verdict

The paper [[1]](#ref-1) changes two components, both standard: it applies each condition-trained sEEG decoder to the other speech modes (M04), the field's usual transfer test (23 of 33 studies, confirmed, Appendix), and adds sentence-rank scoring to correlation (M12), which an overt-to-covert reconstruction study already ran against a 10,000-shuffle null in seven patients [[2]](#ref-2). The hierarchy claim rests on one participant and two repetitions of 100 sentences (Sec. 2.1), and the authors defer its direct test (Sec. 4). The strongest confound is timing: silent trials are scored against vocalized-audio targets (Sec. 2.1) with no stated alignment, where earlier work used dynamic time warping [[2]](#ref-2), [[3]](#ref-3). "Linear better preserves sentence structure" is a slope (Fig. 4), not a level: of six pairs with both AUCs stated, the nonlinear model is higher in three, lower in two, tied in one (Secs. 3.3, 3.4; inference).

## Against the field, component by component

### M04 Use-time action: cross-mode transfer

**Usual approach:** 23 of 33 ledger studies on overt-to-silent transfer apply an overt-trained decoder to silent or covert input without retraining (confirmed; Appendix), e.g. ECoG reconstruction of covert reading in seven patients [[2]](#ref-2) and synthesis of 58 mimed sentences [[3]](#ref-3). The paper also trains on mimed and imagined speech and tests on the other modes.

**State of the art:** Among ECoG studies, an overt-trained Transformer decodes covert sentences at 46.3% token error rate against 46.6% covert-trained, in 16 participants (2024) [[4]](#ref-4); the paper has one participant and no error rate (Sec. 2.1).

Both priors realigned silent output to the overt trial before scoring [[2]](#ref-2), [[3]](#ref-3); the paper names missing timing cues as the obstacle (Sec. 1) yet states no alignment, so the transfer ordering may track timing as much as representation (inference). Martin et al. also give the covert loss (r 0.46 against 0.66) and a rest control [[2]](#ref-2); the paper plots cross-mode scores (Figs. 2, 3) but states no relative loss and has no rest control. Verdict: standard; the ordering rests on one participant.

### M12 Evaluation: identification beyond correlation

**Usual approach:** Of 173 ledger studies reconstructing acoustic speech from neural recordings (pattern match, unique studies; Appendix), 122 report correlation, 45 a listening test and 20 identification among candidates (full-text pattern match; overlapping). Covert identification rank was 0.55 against chance 0.5 [[2]](#ref-2).

**State of the art:** For word identification, a classifier on reconstructions reaches 92-100% accuracy against 8% chance in five subjects, and correlation and identification dissociate (2023) [[5]](#ref-5). The paper's Fig. 4 shows only that AUC rises more steeply with correlation for the linear model, with no classifier or listener test. Verdict: standard.

### M12 Evaluation: null models

**Usual approach:** 45 of 132 ledger studies with empirical nulls permute labels or trials (pattern match, unique studies; Appendix); the linear decoder does (Sec. 2.2), the nonlinear one circularly shifts targets (Sec. 3.4).

**State of the art:** A [concurrent] MEG study by the same group trains nulls identically on mismatched trial pairs, leave-one-subject-out (2026) [[6]](#ref-6).

The paper gives no shuffle count, against 10,000 in [[2]](#ref-2), and with different nulls "above null" is not comparable between decoders. Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Cued sentences in three modes | Cued speech (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Vocalized-audio targets | Paired audio (slot-filled 31) | – | standard |
| M03 Training and adaptation | Per-condition ridge and CNN-RNN | Training (slot-filled 1,526) | – | not reported |
| M04 Use-time action | Each mode-trained decoder on the others | Overt-trained decoder on covert input (confirmed 23) | Overt-trained Transformer, 16 participants [[4]](#ref-4) | standard |
| M05 Sensors | sEEG, 110 electrodes, one participant | Intracranial or scalp (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | Ridge decoder and CNN-RNN | Neural decoder (slot-filled 7,345) | – | standard |
| M07 Lexicon and LM | No LM | No LM (acoustic output) (slot-filled 119) | – | not applicable |
| M08 Output | Spectrogram and envelope | Spectrogram or vocoder output (slot-filled 3,268) | – | standard |
| M09 Confirmation | None | Confirmation (slot-filled 82) | – | not applicable |
| M10 Correction | None | Correction (slot-filled 82) | – | not applicable |
| M11 Reference construction | Vocalized audio for silent trials | Paired speech (slot-filled 234) | DTW to the overt trial [[2]](#ref-2) | not reported |
| M12 Evaluation | Correlation, rank AUC, two nulls | Correlation; trial permutation (pattern match 122) | Word identification [[5]](#ref-5); pairing-shuffle null [concurrent] [[6]](#ref-6) | standard |
| M13 Device and cost | Offline analysis | Device constraints (slot-filled 6,075) | – | not applicable |

## Where the claims outrun the evidence

- "Discriminability is preserved above chance" (Sec. 5) fails for linear mimed-to-imagined, AUC -0.01 (Sec. 3.3).
- The Imagined-trained nonlinear model scores Vocalized like Imagined (p = 0.74) and Mimed lower (p = 0.02, d = 0.29; Sec. 3.4), against the hierarchy.
- Linear against nonlinear confounds model class with target (NSL features against mel-spectrograms, Secs. 2.1, 2.3) and null; the best AUC is 0.59 nonlinear against 0.32 linear (Fig. 3).
- No seeds or reruns are stated (Sec. 2.3).
- No split is stated to keep both repetitions of a sentence in one partition (Sec. 2.2); repetition leakage would inflate rank AUC (inference).
- Vocalized trials add auditory feedback (Sec. 3.2), so the top vocalized scores of every decoder can reflect auditory responses rather than a shared representation (inference); the authors defer a listened-speech control (Sec. 4).

## What the field needs next

- M04 and M11: align silent reconstructions to the vocalized reference [[2]](#ref-2) and report relative loss against within-condition decoding.
- M12: one target and one null for both decoders, with a stated shuffle count, a rest control and a classifier or listener test [[5]](#ref-5).
- M05: a second participant with sentence-disjoint splits.

## Questions for the authors

- Were both repetitions of a sentence kept in one partition?
- How were mimed and imagined trials aligned with the vocalized targets?
- Is N in the rank analysis 100 or the test-sentence count, and how is AUC scaled?
- How many shuffles or shifts formed each null, and which test gave each p-value?
- Which data selected the ridge penalty and lags?

## Appendix: literature search

Ledger at wiki commit 730b0b4: 7,388 unique studies.

**M04, overt-to-silent-transfer** (published topic table, reused). Inclusion rule: studies that apply a decoder trained only on overt speech to silent, mimed or imagined speech without retraining; alignment-only use, whisper transfer and perception-to-imagery transfer are excluded. Ledger counts: M04 slot filled in 5,595 unique studies; 33 pattern match (unique studies); 23 confirmed. Usual design: overt-trained decoder applied to silent or covert input, 23 (confirmed). Read in full: [[2]](#ref-2) and [[3]](#ref-3) (prior), [[4]](#ref-4) (state of the art). Known-item recall: 1.0.

**M12, neural-speech-reconstruction-identification-test** (new topic). Inclusion rule: studies that reconstruct a continuous acoustic speech representation from EEG, MEG, ECoG, sEEG or intracortical recordings and evaluate it; classification-only and text-only decoders are excluded; versions of one study count once. Ledger counts: M12 slot filled in 6,960 unique studies; 173 pattern match (unique studies). Usual design (full-text pattern match over the 173; categories overlap): correlation 122, human listening test 45, mel-cepstral distortion 31, STOI 23, identification among candidates 20. Read in full: [[2]](#ref-2) and [[3]](#ref-3) (prior), [[5]](#ref-5) (state of the art). Known-item recall: 0.67.

**M12, null-model-construction-neural-decoding** (published topic table, reused). Inclusion rule: neural decoding studies that test against an empirical null built by shuffling or permuting labels, trials, time or channels; theoretical chance only is excluded. Ledger counts: M12 slot filled in 6,960 unique studies; 132 pattern match (unique studies). Usual design: label or trial permutation, 45 (pattern match). Read in full: [[2]](#ref-2) (prior), [[6]](#ref-6) (state of the art).

**Inherited slots (M01-M03, M05-M11, M13).** Table counts are slot-filled ledger values at the same commit.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Maghsoudi, M., Chillale, R., Shamma, S. A. “Relating the Neural Representations of Vocalized, Mimed, and Imagined Speech.” *arXiv preprint*, 2026. arXiv:[2602.22597](https://arxiv.org/abs/2602.22597). arXiv v1 [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/relating-the-neural-representations-of-vocalized-mimed-and-imagined-speech) [wiki: arxiv-2602-22597-vmi](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602-22597-vmi/article.md) [wiki: arxiv-2602.22597](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.22597/article.md) [wiki: arxiv-2602.22597-vmi](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.22597-vmi/article.md) [wiki: isca-maghsoudi26_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-maghsoudi26_interspeech/article.md)
2. <a id="ref-2"></a>Martin, S., Brunner, P., Holdgraf, C., Heinze, H., Crone, N. E., Rieger, J., et al. “Decoding spectrotemporal features of overt and covert speech from the human cortex.” *Frontiers in Neuroengineering*, 2014, 7, 14. doi:[10.3389/fneng.2014.00014](https://doi.org/10.3389/fneng.2014.00014). [wiki: doi-10.3389-fneng.2014.00014](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fneng.2014.00014/article.md) [wiki: pmc-4034498-overtcovert](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-4034498-overtcovert/article.md)
3. <a id="ref-3"></a>Anumanchipalli, G. K., Chartier, J., Chang, E. F. “Speech synthesis from neural decoding of spoken sentences.” *Nature*, 2019, 568, 493-498. doi:[10.1038/s41586-019-1119-1](https://doi.org/10.1038/s41586-019-1119-1). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/speech-synthesis-from-neural-decoding-of-spoken-sentences) [wiki: doi-10.1038-s41586-019-1119-1](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-019-1119-1/article.md)
4. <a id="ref-4"></a>Komeiji, S., Mitsuhashi, T., Iimura, Y., Suzuki, H., Sugano, H., Shinoda, K., et al. “Feasibility of decoding covert speech in ECoG with a Transformer trained on overt speech.” *Scientific Reports*, 2024, 14, 11491. doi:[10.1038/s41598-024-62230-9](https://doi.org/10.1038/s41598-024-62230-9). [wiki: pmc-11106343-ecogtransformer](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11106343-ecogtransformer/article.md) [wiki: doi-10.1038-s41598-024-62230-9](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41598-024-62230-9/article.md) [wiki: doi-10.1101-2024.02.05.578911](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2024.02.05.578911/article.md) [wiki: doi-10.21203-rs.3.rs-3927907-v1](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.21203-rs.3.rs-3927907-v1/article.md)
5. <a id="ref-5"></a>Berezutskaya, J., Freudenburg, Z. V., Vansteensel, M. J., Aarnoutse, E. J., Ramsey, N. F., van Gerven, M. A. J. “Direct speech reconstruction from sensorimotor brain activity with optimized deep learning models.” *Journal of Neural Engineering*, 2023, 20, 056010. doi:[10.1088/1741-2552/ace8be](https://doi.org/10.1088/1741-2552/ace8be). [wiki: doi-10.1088-1741-2552-ace8be](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552-ace8be/article.md) [wiki: pmc-10510111-berezutskaya](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10510111-berezutskaya/article.md) [wiki: pmc-10510111-recon](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10510111-recon/article.md)
6. <a id="ref-6"></a>Maghsoudi, M., Shamma, S. “Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping.” *arXiv preprint*, 2026. arXiv:[2605.08075](https://arxiv.org/abs/2605.08075). [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/zero-shot-imagined-speech-decoding-via-imagined-to-listened-meg-mapping) [wiki: arxiv-2605.08075](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2605.08075/article.md) [wiki: arxiv-2605-08075-zeromeg](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2605-08075-zeromeg/article.md)
