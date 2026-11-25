# Machine translation of cortical activity to text with an encoder–decoder framework

Makin, Moses, Chang. Nature Neuroscience 23(4), 575–582 (2020). [doi:10.1038/s41593-020-0608-8](https://doi.org/10.1038/s41593-020-0608-8)

## Verdict

Makin et al. [[1]](#ref-1) changed the decoder (M06, an autoregressive encoder–decoder), the output unit (M08, words), the training-only targets (M02, MFCC regression) and the training data (M03, transfer); all four are standard. An attention encoder–decoder had already decoded EEG to text [[2]](#ref-2), and Brain2Char [[3]](#ref-3) [concurrent] used the same MFCC loss. The internal protocol is strong: 30 models per condition, matched held-out blocks, corrected tests and a length-only noise control. The headline 3% WER comes from held-out repeats of the same 50 sentences, so the claimed gain over the cited 60% baseline [[4]](#ref-4), tested leave-one-phrase-out, compares unlike protocols. Unseen sentences and participants were never tested; today's reference is 23.8% WER on never-repeated sentences with 125,000 words [[5]](#ref-5).

## Against the field, component by component

### M06 Decoding: autoregressive encoder–decoder

**Usual approach:** Of 145 neural text-decoding studies (pattern match, unique studies), 63 name CTC, 46 an encoder–decoder and 43 HMM or Viterbi decoding (upper bounds, Appendix). Makin et al. decode greedily with no language model (Methods, Testing).

**State of the art:** 2.5% online WER over the final five sessions, decoding a phoneme every 80 ms, with a 125,000-word vocabulary from day two (2024) [[6]](#ref-6) [later].

Krishna et al. [[2]](#ref-2) (2019-08) trained an attention RNN encoder–decoder on EEG for 9 or 30 repeated sentences: 70% WER from two electrodes (Sec. 7). The design is prior; Makin et al. add ECoG and a far stronger result, cutting WER from about 33% for a phoneme-HMM sentence classifier to about 3% (Fig. 2a), 91% relative (inference). Since 2023, encoder–decoders appear in 30 of 82 studies and CTC in 45 (Appendix); the best systems decode phonemes with a language model [[6]](#ref-6) [[7]](#ref-7). Verdict: standard.

### M08 Output: whole words

**Usual approach:** Of the 145 studies, 63 name phonemes, 49 characters and 25 words or sentence classes (pattern match, upper bounds, Appendix). Makin et al. use a 1,806-class word softmax (Methods).

**State of the art:** phonemes combined into words by a language model, 2.5% WER (2024) [[6]](#ref-6) [later].

A word softmax emits only words seen in training (Methods), and the authors report whole training sentences substituted (Discussion). Verdict: standard for a 250-word closed task.

### M02 Training-only targets: MFCC regression

**Usual approach:** 16 studies match auxiliary acoustic or articulatory losses (pattern match, unique studies); paired audio in 5 of 11 slot-filled records (Appendix).

**State of the art:** grapheme-to-phoneme labels with no audio target: 25.5% WER from ECoG on 249 sentences never used as training targets, 1,024 words (2023) [[7]](#ref-7) [later].

Brain2Char [[3]](#ref-3) [concurrent] adds the same MFCC loss to a CTC decoder. Without MFCCs, errors rise several-fold (Results). Verdict: standard; the target needs overt speech, which the authors concede a prosthesis user may lack (Discussion).

### M03 Training data: transfer

**Usual approach:** a model per participant, 90 of 379 studies (pattern match, unique studies).

**State of the art:** a sequence-to-sequence sEEG phoneme decoder from a 25-patient cohort, transferred to a held-out subject: PER from 57% within-subject to 49%, 45% with four source subjects (2025) [[8]](#ref-8) [later].

For participant a, task transfer cut WER by 31% and cross-participant pretraining by about 17% (Fig. 3a); combining them did not beat task transfer alone, and cross-participant transfer did not help either picture-description participant (Results). Verdict: standard.

### M12 Evaluation: repeats, not unseen sentences

**Usual approach:** Of the 145 studies, 21 describe a sentence-disjoint test and 10 repeated training sentences (pattern match, upper bounds). Makin et al. hold out repeat blocks, about 10% of data (Methods).

**State of the art:** 23.8% online WER on sentences never duplicated in training, 125,000 words (2023) [[5]](#ref-5) [later]; 25.5% from ECoG [[7]](#ref-7) [later].

Herff et al. [[4]](#ref-4) had already decoded each held-out phrase with models trained on the rest of the session. Against such tests, 3% on repeats of a 250-word set is not comparable. Verdict: standard for 2020; the repeat-only test is the paper's main limit.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Overt reading | Cued or overt speech (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | MFCC regression | Paired audio (5 of 11) (pattern match 16) | No audio target [[7]](#ref-7) | standard |
| M03 Training and adaptation | Cross-participant, cross-task transfer | Per-subject model (90 of 379) (pattern match 379) | Group transfer, 45% PER [[8]](#ref-8) | standard |
| M04 Use-time action | Overt reading | Cued or overt speech (slot-filled 5,595) | – | standard |
| M05 Sensors | Clinical ECoG | ECoG (233 of 246) (slot-filled 7,329) | 253-electrode ECoG [[7]](#ref-7) | standard |
| M06 Processing and decoding | Encoder–decoder, no LM | CTC 63 of 145 (pattern match 145) | 2.5% WER [[6]](#ref-6) | standard |
| M07 Lexicon and LM | None | n-gram or neural LM (slot-filled 119) | – | standard |
| M08 Output | Words, 1,806 classes | Phonemes 63 of 145 (pattern match 145) | Phonemes, 2.5% WER [[6]](#ref-6) | standard |
| M09 Confirmation | None | None (slot-filled 82) | – | not applicable |
| M10 Correction | None | None (slot-filled 82) | – | not applicable |
| M11 Reference construction | Corrected prompt text | Prompt text (slot-filled 234) | – | standard |
| M12 Evaluation | Held-out repeat blocks | Disjoint 21 of 145 (pattern match 145) | 23.8% unseen [[5]](#ref-5) | standard |
| M13 Device and cost | Offline clinical | Offline laboratory (slot-filled 6,075) | – | standard |

## Where the claims outrun the evidence

- "Previous state-of-the-art" 60% WER (Results) mixes protocols: Herff et al. report WER as low as 25% leave-one-phrase-out [[4]](#ref-4).
- The 3% figure and the fourfold (64 channels) and eightfold (no convolution) ablations are quantified for one example participant (Fig. 2a); the other three are only "quite similar" (Supplementary Fig. 1). Participant a, with about four minutes of MOCHA-1 data, starts at about 53% (Fig. 3a).
- Generalization to new sentences is inferred from transfer gains (Fig. 3, Discussion); every test stays on MOCHA-1.
- The tuning block stayed in the final tests, and no seeds are given; the public code sets none (Methods).

## What the field needs next

- M12 and M06: encoder–decoder against phoneme CTC with a language model on the same ECoG data, sentence-disjoint.
- M02: MFCC against text-derived phone targets in the same participants.
- M03: a held-out-participant test.

## Questions for the authors

- Were training and held-out blocks recorded on different days?
- Is the 30-s z-scoring window causal, and does it cross block boundaries?
- What is each ablation's WER for all four participants?
- Does the MOCHA-1 decoder emit words outside the MOCHA-1 vocabulary?

## Appendix: literature search

- M06 neural-encoder-decoder-text-decoding. Inclusion rule: same population as the M08 output-unit topic; the design compared is the sequence decoder (autoregressive encoder–decoder, CTC, or HMM/Viterbi); a paper counts under every decoder its full text names. Ledger counts: 7,345 slot-filled; 145 pattern match (unique studies). Usual design: CTC 63, encoder–decoder 46, HMM or Viterbi 43 (pattern match, upper bounds); 2023 onward (82 studies): encoder–decoder 30, CTC 45, HMM or Viterbi 22. Read in full: [[2]](#ref-2), [[4]](#ref-4) (deciding priors), [[6]](#ref-6) (state of the art), [[8]](#ref-8). Known-item recall 0.6 (5 seeds).
- M08 neural-text-output-unit (reused topic table). Inclusion rule as published: neural decoders that output text and report WER, CER or PER; the design compared is the unit emitted before any lexicon or language model. Ledger counts: 3,268 slot-filled; 145 pattern match (unique studies). Usual design: phonemes 63, characters 49, words or sentence classes 25 (pattern match, upper bounds). Read in full: [[6]](#ref-6) (state of the art), [[7]](#ref-7), [[5]](#ref-5). Known-item recall 0.8 (as published).
- M02 auxiliary-speech-feature-regression (reused topic table). Inclusion rule as published: non-acoustic text or speech-unit decoders whose training adds a loss regressing acoustic or articulatory features of the paired speech, discarded at use time. Ledger counts: 31 slot-filled (sparse slot); 16 pattern match (unique studies). Usual design from M03 supervision kind: paired audio, 5 of 11 (slot-filled). Read in full: [[3]](#ref-3) (deciding prior), [[7]](#ref-7) (state of the art). Known-item recall 0.0 (as published).
- M03 cross-subject-pooled-training (reused topic table). Inclusion rule as published: speech or language decoders from neural or other biosignals trained on data pooled across participants; transfer by fine-tuning from another participant counts. Ledger counts: 1,526 slot-filled; 370 pattern match in the ledger, 379 with full-text hits (unique studies). Usual design: per-subject model, 90 of 379 (pattern match). Read in full: [[8]](#ref-8) (state of the art for this review). Known-item recall 1.0 (as published).
- M12 neural-text-unseen-sentence-test (reused topic table). Inclusion rule as published: same population as M08; the design compared is whether WER is measured on sentences absent from training or on repeats. Ledger counts: 6,960 slot-filled; 145 pattern match (unique studies). Usual design: sentence-disjoint test 21, repeated training sentences 10 (pattern match, upper bounds). Read in full: [[5]](#ref-5) (state of the art), [[7]](#ref-7), [[4]](#ref-4), [[2]](#ref-2). Known-item recall 0.8 (as published).

## References

Numbered by first citation. BibTeX in the same order and keys: [machine-translation-of-cortical-activity-to-text-with-an-encoder-decoder-framework.bib](machine-translation-of-cortical-activity-to-text-with-an-encoder-decoder-framework.bib).

1. <a id="ref-1"></a>Makin, J. G., Moses, D. A., Chang, E. F. “Machine translation of cortical activity to text with an encoder-decoder framework.” *Nature Neuroscience*, 2020, 23, 575–582. doi:[10.1038/s41593-020-0608-8](https://doi.org/10.1038/s41593-020-0608-8). [wiki: doi-10.1038-s41593-020-0608-8](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41593-020-0608-8/article.md) [wiki: pmc-10560395-makin](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10560395-makin/article.md)
2. <a id="ref-2"></a>Krishna, G., Han, Y., Tran, C., Carnahan, M., Tewfik, A. H. “State-of-the-art speech recognition using EEG and towards decoding of speech spectrum from EEG.” *arXiv*, 2019. arXiv:[1908.05743](https://arxiv.org/abs/1908.05743). [wiki: arxiv-1908.05743-eegasr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1908.05743-eegasr/article.md)
3. <a id="ref-3"></a>Sun, P., Anumanchipalli, G. K., Chang, E. F. “Brain2Char: a deep architecture for decoding text from brain recordings.” *Journal of Neural Engineering*, 2020, 17(6), 066015. doi:[10.1088/1741-2552/abc742](https://doi.org/10.1088/1741-2552/abc742). arXiv:[1909.01401](https://arxiv.org/abs/1909.01401). [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/brain2char-a-deep-architecture-for-decoding-text-from-brain-recordings) [wiki: doi-10.1088-1741-2552-abc742](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552-abc742/article.md) [wiki: pmc-9591243-brain2char](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-9591243-brain2char/article.md)
4. <a id="ref-4"></a>Herff, C., Heger, D., de Pesters, A., Telaar, D., Brunner, P., Schalk, G., et al. “Brain-to-text: decoding spoken phrases from phone representations in the brain.” *Frontiers in Neuroscience*, 2015, 9, 217. doi:[10.3389/fnins.2015.00217](https://doi.org/10.3389/fnins.2015.00217). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/brain-to-text-decoding-spoken-phrases-from-phone-representations-in-the-brain) [wiki: doi-10.3389-fnins.2015.00217](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnins.2015.00217/article.md)
5. <a id="ref-5"></a>Willett, F. R., Kunz, E. M., Fan, C., Avansino, D. T., Wilson, G. H., Choi, E. Y., et al. “A high-performance speech neuroprosthesis.” *Nature*, 2023, 620, 1031–1036. doi:[10.1038/s41586-023-06377-x](https://doi.org/10.1038/s41586-023-06377-x). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-high-performance-speech-neuroprosthesis) [wiki: doi-10.1038-s41586-023-06377-x](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-023-06377-x/article.md) [wiki: pmc-10468393-neuroprosthesis](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10468393-neuroprosthesis/article.md)
6. <a id="ref-6"></a>Card, N. S., Wairagkar, M., Iacobacci, C., Hou, X., Singer-Clark, T., Willett, F. R., et al. “An accurate and rapidly calibrating speech neuroprosthesis.” *New England Journal of Medicine*, 2024, 391(7), 609–618. doi:[10.1056/NEJMoa2314132](https://doi.org/10.1056/NEJMoa2314132). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/an-accurate-and-rapidly-calibrating-speech-neuroprosthesis) [wiki: doi-10.1056-nejmoa2314132](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1056-nejmoa2314132/article.md) [wiki: doi-10.1056-NEJMoa2314132](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1056-NEJMoa2314132/article.md) [wiki: pmc-11328962-rapidcal](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11328962-rapidcal/article.md)
7. <a id="ref-7"></a>Metzger, S. L., Littlejohn, K. T., Silva, A. B., Moses, D. A., Seaton, M. P., Wang, R., et al. “A high-performance neuroprosthesis for speech decoding and avatar control.” *Nature*, 2023, 620, 1037–1046. doi:[10.1038/s41586-023-06443-4](https://doi.org/10.1038/s41586-023-06443-4). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-high-performance-neuroprosthesis-for-speech-decoding-and-avatar-control) [wiki: doi-10.1038-s41586-023-06443-4](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-023-06443-4/article.md) [wiki: pmc-10826467-avatarnp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10826467-avatarnp/article.md)
8. <a id="ref-8"></a>Singh, A., Thomas, T., Li, J., Hickok, G., Pitkow, X., Tandon, N. “Transfer learning via distributed brain recordings enables reliable speech decoding.” *Nature Communications*, 2025, 16, 8749. doi:[10.1038/s41467-025-63825-0](https://doi.org/10.1038/s41467-025-63825-0). [later] [wiki: doi-10.1038-s41467-025-63825-0](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41467-025-63825-0/article.md)
