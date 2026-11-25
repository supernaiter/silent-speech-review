# High-performance brain-to-text communication via handwriting

Francis R. Willett, Donald T. Avansino, Leigh R. Hochberg, Jaimie M. Henderson, Krishna V. Shenoy. Nature, 2021. DOI: [10.1038/s41586-021-03506-2](https://doi.org/10.1038/s41586-021-03506-2)

## Verdict

The paper changes the use-time action (M04, attempted handwriting), training label timing (M02, HMM labels from neural data) and the decoder (M06, a causal character RNN) [[1]](#ref-1). The action is the real contribution: none of the 36 studies dated 2020 or earlier in the 154-study neural text-entry population names attempted handwriting (pattern match, Appendix), and 90 raw characters per minute in copy typing more than double the 39.2 correct characters per minute the same participant reached by point-and-click [[2]](#ref-2). All three are standard under the verdict rules: the evidence is one participant, and M02 and M06 follow designs the field had or soon replaced [[3]](#ref-3), [[4]](#ref-4). The strongest overreach is ">99% accuracy offline": the language model ran only on stored outputs, and online word error rate was 25.1% (Table 1). Attempted speech at 62 words per minute [[4]](#ref-4) and attempted finger typing at 110 characters per minute [[5]](#ref-5) have since overtaken it [later].

## Against the field, component by component

### M04 Use-time action: attempted handwriting

**Usual approach:** Attempted speech is the most frequent recorded action among neural text-entry studies (37 of 123 slot-filled); cursor or keyboard selection appears in 37 of 154 (pattern match). The paper replaces its lineage's point-and-click keyboard with handwriting.

**State of the art:** In 2017 the same participant, T5, typed 39.2 correct characters per minute by point-and-click [[2]](#ref-2); 90 characters per minute is about 2.3 times that (inference). In 2026 attempted finger typing reached 110 characters per minute at 1.6% word error rate with a 5-gram model in T18 [[5]](#ref-5) [later].

The design is new (Appendix), but tested in one participant (§ Discussion); [later] handwriting decoding gave T18 a 2% character error rate [[6]](#ref-6). Verdict: standard (no repetition across participants).

### M02 Training-only supervision: label timing without observable output

**Usual approach:** Alignment-free CTC is the most frequent timing design (64 of 154 studies, against 40 naming an HMM or forced alignment; pattern match). The target, with no audio or pen trace, labels time steps with HMM character templates fitted to neural data and adds synthetic sentences.

**State of the art:** In 2023 the same group's speech BCI trained with CTC and reached 23.8% online word error rate with a 125,000-word vocabulary [[4]](#ref-4) [later].

CTC had already removed frame labels from neural text decoding, on ECoG with synchronous speech [[3]](#ref-3), and the successor system uses it. Verdict: standard.

### M06 Decoder: streaming character RNN

**Usual approach:** A recurrent or CTC decoder plus a language model (decode step in 61 of 96 studies, slot-filled). The target emits character and new-character probabilities with a one-second output delay (Fig. 2) and no language model online.

**State of the art:** In 2024 online attempted-speech decoding reached 2.5% word error rate with a 125,000-word vocabulary [[7]](#ref-7) [later], against the target's raw online 25.1% (Table 1). Starting points differ: words after real-time language models against raw characters. Verdict: standard.

### M07 Use-time lexicon: language model only after the fact

**Usual approach:** An n-gram model in the decoding loop (134 of 1,162 studies, pattern match). The [concurrent] anarthria study ran it in real time (median word error rate 60.5% to 25.6%, 50 words) [[8]](#ref-8).

**State of the art:** [[7]](#ref-7) (2024) [later], as for M06. The target's 50,000-word bigram corrects stored outputs only (Table 1). Verdict: standard.

### M12 Evaluation: held-out copy-typing sentences

**Usual approach:** A sentence-disjoint test (21 studies against 10 testing on repeated training sentences, pattern match); the target follows it.

**State of the art:** [[4]](#ref-4) (2023) [later], the same split at 125,000 words. Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | T5 prompted sentences | Prompted sentences (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | HMM labels from neural data | Alignment-free CTC (pattern match 64) | [[4]](#ref-4) (2023): WER 23.8%, CTC | standard |
| M03 Training and adaptation | Daily recalibration, 50 sentences | Daily supervised recalibration (slot-filled 1,526) | – | standard |
| M04 Use-time action | Attempted handwriting, 31 characters | Attempted speech (slot-filled 37) | [[5]](#ref-5) (2026): 110 characters per minute | standard |
| M05 Sensors | Two microelectrode arrays, hand knob | Implanted arrays (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | Causal character RNN | RNN or CTC decoder + LM (slot-filled 61) | [[7]](#ref-7) (2024): online WER 2.5% | standard |
| M07 Lexicon and LM | Offline 50,000-word bigram only | n-gram LM in the loop (pattern match 134) | [[7]](#ref-7) (2024): online WER 2.5% | standard |
| M08 Output | Characters, 31-symbol set | Phonemes (pattern match 63) | – | standard |
| M09 Confirmation | Characters shown as detected | No confirmation step (slot-filled 82) | – | standard |
| M10 Correction | No backspace | No correction step (slot-filled 82) | – | standard |
| M11 Reference construction | Prompted text; free typing unstated | Prompted text (slot-filled 234) | – | standard |
| M12 Evaluation | Held-out sentences, one participant | Sentence-disjoint test (pattern match 21) | [[4]](#ref-4) (2023): WER 23.8% | standard |
| M13 Device and cost | One participant, percutaneous implant | Single-participant implant (slot-filled 6,075) | – | standard |

## Where the claims outrun the evidence

- The ">99%" headline (Abstract) is a retrospective bigram model with an unstated corpus that swaps out-of-vocabulary words (Extended Data Table 1).
- The free-typing benchmark of 24.4 correct characters per minute (§ Decoding handwritten sentences) is T6's rate [[2]](#ref-2); T5 was the best of that study's three participants (§ Discussion), so the 73.8 characters per minute comparison confounds participant with interface.
- The Abstract pairs the 90 characters per minute plateau (5.4% error, Fig. 2) with 94.1% accuracy, the complement of the five-day 5.9% error (Table 1) (inference).
- No backspace was implemented (§ Decoding handwritten sentences), whereas the compared keyboard had one [[2]](#ref-2); raw characters per minute without editing are not correct characters per minute with editing.
- Reduced calibration and unsupervised retraining are offline simulations, as the authors say (§ Daily decoder retraining); the online test came [later] in the same participant, 6.35% character error rate over 403 days [[9]](#ref-9).

## What the field needs next

- M04: handwriting, speech and typing compared within participants.
- M07 and M10: language model and delete command in the real-time loop.
- M03: online unsupervised recalibration in several participants.

## Questions for the authors

- How was the intended text established for free-typing answers?
- Which corpus trained the 50,000-word bigram model?

## Appendix: literature search

- M04, neural-text-entry-action (new). Inclusion rule: neural BCI studies (intracortical, ECoG, sEEG, EEG, MEG) whose ledger names the recording modality with a text output, text error rate or text-entry rate; the design compared is the use-time action that drives text; a study counts under every action its full text names (upper bound); versions once. Ledger: 5,595 unique studies slot-filled for M04; 154 unique studies pattern match. Usual design: attempted speech 37 of 123 slot-filled. Full-text counts: imagined or inner speech 68, attempted speech 56, overt speech 46, speech perception 39, cursor or keyboard 37, evoked-potential speller 29, attempted handwriting 28; among the 36 studies dated 2020 or earlier, attempted handwriting 0 (pattern match). Read in full: [[2]](#ref-2), [[5]](#ref-5), [[4]](#ref-4), [[6]](#ref-6). Known-item recall 1.0.
- M02, unaligned-neural-sentence-label-timing (new). Inclusion rule: the same 154 studies, classified by how per-time-step targets are obtained for sentences with no observable timing (CTC, HMM or forced alignment, audio- or onset-aligned labels, time warping, synthetic augmentation); every named design counts (upper bound). Ledger: 31 unique studies slot-filled for M02; 154 unique studies pattern match. CTC 64, HMM or forced alignment 40, time warping 29, synthetic augmentation 29, audio- or onset-aligned 25; dated 2020 or earlier: CTC 4, HMM 9 of 36 (pattern match). Read in full: [[3]](#ref-3), [[4]](#ref-4). Known-item recall 1.0.
- M06, phoneme-rnn-ctc-lm-decoding (published table, reused). Inclusion rule: recurrent or CTC-trained decoders emitting phoneme or character probabilities turned into words with a language model. Ledger: 7,345 unique studies slot-filled for M06; 97 unique studies pattern match; decode step 61 of 96 slot-filled. Read in full: [[7]](#ref-7), [[4]](#ref-4), [[3]](#ref-3). Known-item recall 0.5.
- M07, large-vocabulary-lm-for-neural-speech (published table, reused). Inclusion rule: neural decoders constraining output with a vocabulary of at least 1,000 words via an n-gram or neural language model. Ledger: 119 unique studies slot-filled for M07; 1,162 unique studies pattern match; n-gram model 134, neural rescoring 14 (pattern match). Read in full: [[7]](#ref-7), [[8]](#ref-8). Known-item recall 1.0.
- M12, neural-text-unseen-sentence-test (published table, reused). Inclusion rule: whether reported error rates are measured on sentences absent from training or on repeats. Ledger: 6,960 unique studies slot-filled for M12; 145 unique studies pattern match; sentence-disjoint 21, repeated training sentences 10. Read in full: [[4]](#ref-4), [[9]](#ref-9). Known-item recall 0.8.

## References

Numbered by first citation. BibTeX in the same order and keys: [high-performance-brain-to-text-communication-via-handwriting.bib](high-performance-brain-to-text-communication-via-handwriting.bib).

1. <a id="ref-1"></a>Willett, F. R., Avansino, D. T., Hochberg, L. R., Henderson, J. M., Shenoy, K. V. “High-performance brain-to-text communication via handwriting.” *Nature*, 2021, 593(7858), 249-254. doi:[10.1038/s41586-021-03506-2](https://doi.org/10.1038/s41586-021-03506-2). Target. Read as the PMC author manuscript (NIHMS1693320). [wiki: doi-10.1038-s41586-021-03506-2](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-021-03506-2/article.md) [wiki: pmc-8163299-b2thand](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-8163299-b2thand/article.md)
2. <a id="ref-2"></a>Pandarinath, C., Nuyujukian, P., Blabe, C. H., Sorice, B. L., Saab, J., Willett, F. R., et al. “High performance communication by people with paralysis using an intracortical brain-computer interface.” *eLife*, 2017, e18554. doi:[10.7554/eLife.18554](https://doi.org/10.7554/eLife.18554). Prior; deciding prior for M04 (point-and-click typing, same participant T5). [wiki: pmc-5319839-ibcityping](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-5319839-ibcityping/article.md) [wiki: pmc-5319839-hiprofiBCI](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-5319839-hiprofiBCI/article.md)
3. <a id="ref-3"></a>Sun, P., Anumanchipalli, G. K., Chang, E. F. “Brain2Char: a deep architecture for decoding text from brain recordings.” *Journal of Neural Engineering*, 2020. doi:[10.1088/1741-2552/abc742](https://doi.org/10.1088/1741-2552/abc742). arXiv:[1909.01401](https://arxiv.org/abs/1909.01401). Prior (arXiv 1909.01401, 2019); deciding prior for M02 and M06 (CTC character decoding from ECoG with synchronous speech). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/brain2char-a-deep-architecture-for-decoding-text-from-brain-recordings) [wiki: doi-10.1088-1741-2552-abc742](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552-abc742/article.md)
4. <a id="ref-4"></a>Willett, F. R., Kunz, E. M., Fan, C., Avansino, D. T., Wilson, G. H., Choi, E. Y., et al. “A high-performance speech neuroprosthesis.” *Nature*, 2023. doi:[10.1038/s41586-023-06377-x](https://doi.org/10.1038/s41586-023-06377-x). Later; state of the art for M02 and M12. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-high-performance-speech-neuroprosthesis) [wiki: doi-10.1038-s41586-023-06377-x](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-023-06377-x/article.md)
5. <a id="ref-5"></a>Jude, J. J., Levi-Aharoni, H., Acosta, A. J., Allcroft, S. B., Nicolas, C., Lacayo, B. E., et al. “Restoring rapid natural bimanual typing with a neuroprosthesis after paralysis.” *Nature Neuroscience*, 2026. doi:[10.1038/s41593-026-02218-y](https://doi.org/10.1038/s41593-026-02218-y). Later; state of the art for M04 (character rate). [later] [wiki: pmc-13633126-bitype](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13633126-bitype/article.md) [wiki: doi-10.1038-s41593-026-02218-y](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41593-026-02218-y/article.md) [wiki: pmc-13633126-bityping](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13633126-bityping/article.md) [wiki: pmc-13633126-bimanualtype](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13633126-bimanualtype/article.md) [wiki: pmc-13633126-bimantype](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13633126-bimantype/article.md) [wiki: pmc-13633126-ibcityping](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13633126-ibcityping/article.md)
6. <a id="ref-6"></a>Levin, A. D., Avansino, D. T., Kamdar, F. B., Card, N. S., Wairagkar, M., Jacques, B. G., et al. “Cross-brain transfer of high-performance intracortical speech and handwriting BCIs.” *bioRxiv preprint*, 2026. doi:[10.64898/2026.01.12.699110](https://doi.org/10.64898/2026.01.12.699110). Later; handwriting BCI in further participants (M04, M12). [later] [wiki: pmc-12871243-xbrain](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12871243-xbrain/article.md)
7. <a id="ref-7"></a>Card, N. S., Wairagkar, M., Iacobacci, C., Hou, X., Singer-Clark, T., Willett, F. R., et al. “An accurate and rapidly calibrating speech neuroprosthesis.” *New England Journal of Medicine*, 2024, 391(7), 609-618. doi:[10.1056/NEJMoa2314132](https://doi.org/10.1056/NEJMoa2314132). Later; state of the art for M06 and M07. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/an-accurate-and-rapidly-calibrating-speech-neuroprosthesis) [wiki: pmc-11328962-rapidcal](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11328962-rapidcal/article.md) [wiki: doi-10.1056-NEJMoa2314132](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1056-NEJMoa2314132/article.md) [wiki: doi-10.1056-nejmoa2314132](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1056-nejmoa2314132/article.md)
8. <a id="ref-8"></a>Moses, D. A., Metzger, S. L., Liu, J. R., Anumanchipalli, G. K., Makin, J. G., Sun, P. F., et al. “Neuroprosthesis for decoding speech in a paralyzed person with anarthria.” *New England Journal of Medicine*, 2021, 385, 217-227. doi:[10.1056/NEJMoa2027540](https://doi.org/10.1056/NEJMoa2027540). Concurrent; online language model in a speech neuroprosthesis (M07). [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/neuroprosthesis-for-decoding-speech-in-a-paralyzed-person-with-anarthria) [wiki: doi-10.1056-nejmoa2027540](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1056-nejmoa2027540/article.md)
9. <a id="ref-9"></a>Fan, C., Hahn, N., Kamdar, F., Avansino, D., Wilson, G. H., Hochberg, L., et al. “Plug-and-Play Stability for Intracortical Brain-Computer Interfaces: A One-Year Demonstration of Seamless Brain-to-Text Communication.” *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, 2023. arXiv:[2311.03611](https://arxiv.org/abs/2311.03611). Later; online test of unsupervised recalibration of the handwriting decoder (M03). [later] [wiki: pmc-pmc11086983](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-pmc11086983/article.md) [wiki: pmc-11086983-plugplay](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11086983-plugplay/article.md) [wiki: arxiv-2311.03611](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2311.03611/article.md)
