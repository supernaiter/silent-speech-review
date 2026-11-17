# Neuroprosthesis for Decoding Speech in a Paralyzed Person with Anarthria

Moses, Metzger, Liu, Anumanchipalli, Makin, Sun, Chartier, Dougherty, Liu, Abrams, Tu-Chan, Ganguly, Chang. New England Journal of Medicine 385, 217–227 (2021). [doi:10.1056/NEJMoa2027540](https://doi.org/10.1056/NEJMoa2027540)

## Verdict

The paper changed who is decoded (M04, anarthria; M13, a chronic implant) and moved a closed-vocabulary pipeline from speaking epilepsy patients into that setting (M06, M07); the decoder is standard for 2021 ECoG work, and the advance is the population, rated standard because one participant gives no repetition. The main claim, sentences decoded from a person who cannot speak, holds for 50 words and one participant at 25.6% median WER. The strongest overreach is the language model: trained only on sentences from the test set's 50 words, its drop from 60.5% to 25.6% WER measures a closed-world prior. The no-recalibration claim rests on a post hoc offline analysis of isolated words, not on real-time sentence use. Against today the system is far behind: an intracortical phoneme decoder in a participant with dysarthria reached 99.6% accuracy on 50 words after 30 minutes of recordings [[1]](#ref-1) ([later]), where this paper collected 22 hours of isolated-word data.

## Against the field, component by component

### M06 Decoding: speech detection plus closed-set word classification

**Usual approach:** Of 355 closed-set classification studies with a model-family record (slot-filled, unique studies), the most frequent named family is CNN (35), then HMM (25); 82 are uncategorised. The paper's detector, 50-word classifier and Viterbi search repeat the 2019 ECoG design [[2]](#ref-2).

**State of the art:** 99.6% on a 50-word vocabulary on day one, intracortical, 2024 [[1]](#ref-1) ([later]).

The prior design reached 61% produced-utterance accuracy (chance 7%) in three speaking epilepsy patients [[2]](#ref-2). The decoder is unchanged in kind and not compared with alternatives on the same data (§ Methods, Modeling). Verdict: standard. The 2024 system used about 44 times less recording time (inference) but differs in sensor, participant and unit, so the gap belongs to the system.

### M07 Language model: a prior restricted to the test vocabulary

**Usual approach:** In 2021 ECoG work the prior was closed-set [[2]](#ref-2), [[3]](#ref-3). The slot is sparse (119 slot-filled); of 1,162 studies naming a language model (pattern match, unique studies), the largest group, large-vocabulary neural rescoring, has 152 (pattern match), with [later] examples [[1]](#ref-1), [[4]](#ref-4). The paper's 50-word n-gram model matches 2021 practice.

**State of the art:** 2.5% WER at 125,000 words in 2024 [[1]](#ref-1) ([later]); within ECoG, 25.5% WER at 1,024 words in 2023 [[4]](#ref-4) ([later]), the same error on a vocabulary about 20 times larger (inference).

The deciding prior, an ECoG encoder-decoder in speaking participants, reported WERs as low as 3% with about 250 words, on repetitions of its training sentences [[3]](#ref-3). The paper's gain from its language model (a 58% relative reduction, inference) is measured on a vocabulary five times smaller (inference), with test sentences built from the model's own 50 words; both results are closed-world. Verdict: standard for 2021; it trails [[1]](#ref-1) today and is untested beyond its 50 words.

### M05 Sensors: chronic ECoG in anarthria

**Usual approach:** ECoG appears in 233 of 246 studies on ECoG speech decoding (slot-filled).

**State of the art:** 253-channel high-density ECoG in a participant with anarthria, 25.5% WER at 1,024 words, 2023 [[4]](#ref-4) ([later]).

Chronic use is rated under M13. The electrode analysis (Fig. 3A) is attribution, not ablation. Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Cued attempted word production, 50 words | Attempted or overt cued speech (slot-filled 4,015) | – | standard |
| M02 Training-only supervision | Cued word identity; no audio | Text-derived labels (slot-filled 31) | – | standard |
| M03 Training and adaptation | 22 h over 48 sessions, cumulative | Supervised training on accumulated sessions (slot-filled 1,608) | 99.6% on 50 words after 30 min of data, 2024 [[1]](#ref-1) | standard |
| M04 Use-time action | Attempted speech, participant with anarthria | Overt speech by speaking participants (slot-filled 6,538) | – | standard |
| M05 Sensors | 128-electrode chronic ECoG, sensorimotor cortex | ECoG (slot-filled 233) | 253-channel ECoG, 25.5% WER at 1,024 words, 2023 [[4]](#ref-4) | standard |
| M06 Processing and decoding | Speech detector + 50-word classifier + Viterbi with LM | CNN, most frequent named family (slot-filled 35) | 99.6% on 50 words, intracortical, 2024 [[1]](#ref-1) | standard |
| M07 Lexicon and LM | LM restricted to the 50 words | Closed-set priors in 2021; large-vocabulary rescoring later (pattern match 152) | 2.5% WER at 125,000 words, 2024 [[1]](#ref-1) | standard |
| M08 Output | Text | Text (slot-filled 3,760) | – | standard |
| M09 Confirmation | Decoded sentence shown on screen; no confirmation | Absent in most studies (slot-filled 82) | – | standard |
| M10 Correction | None | Absent in most studies (slot-filled 82) | – | standard |
| M11 Reference construction | Cued target sentence | Cued prompt text (slot-filled 239) | – | standard |
| M12 Evaluation | Median WER over 15 blocks, words per minute, LM-sampled chance | WER or accuracy on held-out trials (slot-filled 8,381) | – | standard |
| M13 Device and cost | One chronic implant, percutaneous connector, supervised use, 81 weeks | Acute clinical recordings (slot-filled 6,721) | – | standard |

## Where the claims outrun the evidence

- Language model: trained on sentences limited to the 50 words, with chance itself sampled from that model (92.1% WER; § Methods, Modeling). The 35-point gain holds only in this closed world.
- Stability: "without daily or weekly recalibration" rests on offline cross-validation of isolated words from weeks 79–81, designed post hoc (§ Statistical analyses; Fig. 4). The [later] intracortical participant asked for recalibration three times in personal use [[1]](#ref-1).
- Usability: "usable at word error rates below 30%" cites only a volume on acoustic speech recognition (§ Discussion) and is applied to a vocabulary where every word is known in advance.
- Speed: the only same-participant baseline is head-movement typing at 5 correct words per minute (§ Methods, Participant); no spelling BCI was compared.

## What the field needs next

- M07: a language model trained on text excluding the test sentences, and vocabularies of 1,000 words or more.
- M03: real-time sentence WER against weeks since last training, in more than one participant.
- M05: electrode-dropping ablations on the chronic array.
- M06: word classification against phoneme decoding on the same recordings.

## Questions for the authors

- Do test sentences appear verbatim in the language-model training set, and how were the 50 chosen?
- Were stability folds split by session or by trial, and how many training runs underlie each value?
- Which data selected hyperparameters, ensembles and detection thresholds, and how were features normalised?
- How was trial time defined for words per minute, and what was the WER of the conversational demonstration?

## Appendix: literature search

Ledger at wiki commit 730b0b4: 7,388 unique studies.

**M06, closed-vocabulary-word-classification.** Inclusion rule: studies that decode words or utterances from non-acoustic signals by classifying each detected segment into a closed set of at most a few hundred words or utterances, with or without a language-model or context prior; open-vocabulary phoneme or character decoders are excluded unless they also report a closed-set word test; acoustic-only ASR is excluded. Ledger counts: 7,345 slot-filled unique studies; 360 pattern match (unique studies). Model families among 355 studies with a record (slot-filled): "other" (uncategorised) 82, CNN 35, HMM 25; most frequent named family CNN. Read in full: [[1]](#ref-1) (state of the art), [[2]](#ref-2) (prior). Known-item recall: 0.5.

**M07, large-vocabulary-lm-for-neural-speech.** Inclusion rule: neural speech decoders that constrain output with a vocabulary of at least 1,000 words via an n-gram or neural language model at use time; 50-word or command sets count as small vocabulary; LLM rescoring counts. Ledger counts: 119 slot-filled unique studies (sparse slot); 1,162 pattern match (unique studies). Largest named group: large-vocabulary neural rescoring, 152 of 1,162 (pattern match). Read in full: [[1]](#ref-1), [[4]](#ref-4) (state of the art), [[3]](#ref-3) (prior). Known-item recall: 1.0.

**M05, ecog-speech-decoding.** Inclusion rule: papers that decode speech units, words, sentences or acoustics from ECoG in humans during produced, attempted, mimed or imagined speech; clinical and high-density grids, micro-ECoG, online or offline are included; intracortical, sEEG-only and listening-only studies are excluded. Ledger counts: 7,329 slot-filled unique studies; 253 pattern match (unique studies). Usual design: modalities = ECoG, 233 (slot-filled) of 246. Read in full: [[1]](#ref-1), [[4]](#ref-4) (state of the art). Known-item recall: 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Card, N. S., Wairagkar, M., Iacobacci, C., Hou, X., Singer-Clark, T., Willett, F. R., et al. “An accurate and rapidly calibrating speech neuroprosthesis.” *New England Journal of Medicine*, 2024, 391(7), 609–618. doi:[10.1056/NEJMoa2314132](https://doi.org/10.1056/NEJMoa2314132). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/an-accurate-and-rapidly-calibrating-speech-neuroprosthesis) [wiki: doi-10.1056-nejmoa2314132](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1056-nejmoa2314132/article.md) [wiki: doi-10.1056-NEJMoa2314132](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1056-NEJMoa2314132/article.md) [wiki: pmc-11328962-rapidcal](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11328962-rapidcal/article.md)
2. <a id="ref-2"></a>Moses, D. A., Leonard, M. K., Makin, J. G., Chang, E. F. “Real-time decoding of question-and-answer speech dialogue using human cortical activity.” *Nature Communications*, 2019, 10, 3096. doi:[10.1038/s41467-019-10994-4](https://doi.org/10.1038/s41467-019-10994-4). [wiki: pmc-6667454-qa](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-6667454-qa/article.md) [wiki: doi-10.1038-s41467-019-10994-4](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41467-019-10994-4/article.md) [wiki: pmc-6667454-qadecode](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-6667454-qadecode/article.md) [wiki: pmc-6667454-qadialogue](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-6667454-qadialogue/article.md)
3. <a id="ref-3"></a>Makin, J. G., Moses, D. A., Chang, E. F. “Machine translation of cortical activity to text with an encoder-decoder framework.” *Nature Neuroscience*, 2020, 23, 575–582. doi:[10.1038/s41593-020-0608-8](https://doi.org/10.1038/s41593-020-0608-8). [wiki: doi-10.1038-s41593-020-0608-8](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41593-020-0608-8/article.md) [wiki: pmc-10560395-makin](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10560395-makin/article.md)
4. <a id="ref-4"></a>Metzger, S. L., Littlejohn, K. T., Silva, A. B., Moses, D. A., Seaton, M. P., Wang, R., et al. “A high-performance neuroprosthesis for speech decoding and avatar control.” *Nature*, 2023, 620, 1037–1046. doi:[10.1038/s41586-023-06443-4](https://doi.org/10.1038/s41586-023-06443-4). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-high-performance-neuroprosthesis-for-speech-decoding-and-avatar-control) [wiki: doi-10.1038-s41586-023-06443-4](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-023-06443-4/article.md) [wiki: pmc-10826467-avatarnp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10826467-avatarnp/article.md)
