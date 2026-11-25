# Development of sEMG sensors and algorithms for silent speech recognition

Meltzner, G. S., Heaton, J. T., Deng, Y., De Luca, G., Roy, S. H., Kline, J. C. · Journal of Neural Engineering · 2018 · [doi:10.1088/1741-2552/aac965](https://doi.org/10.1088/1741-2552/aac965)

## Verdict

The paper [[1]](#ref-1) changes an 11-site face and neck sEMG array with an exhaustive subset search (M05), a Kaldi triphone HMM with HLDA, MLLR and SGMM (M06) and a hand-built natural-language class grammar (M07). All three are standard: subset search over trained models, HMM decoding and grammar-constrained decoding were in the field before 2018 (Appendix), and the same pipeline, task sets and per-subject rows were published by this group in 2014 [[2]](#ref-2), uncited here. The headline does not hold as stated: the 8.9% WER of Table 2 is the 2014 SGMM table with one of six subjects removed, whose six-subject mean is 11.2% [[2]](#ref-2). The "2,200-word vocabulary" is the corpus total; the test sets held 88 to 167 words each [[2]](#ref-2) under a grammar built from the corpus's own sentence rules (Fig. 3), and no test partition is reported (M12), so "far surpassing previous attempts" rests on unmatched protocols.

## Against the field, component by component

### M05 Sensors: 11-site array and subset search

**Usual approach:** Of 42 surface-EMG speech studies reporting electrode subsets (pattern match, unique studies, Appendix), 10 choose it by search over trained models; this paper takes the most expensive form, all 2,047 subsets of 11 sensors, best at 10.4% WER with 8 (Fig. 6).

**State of the art:** Hwang et al. (2026, [later]) score all 70 four-channel subsets of the Gaddy array, best 47.2% WER on EMG-to-speech [[3]](#ref-3); the comparison is on a different task, since the later subset searches in the ledger are on synthesis (Appendix).

The redundancy finding is not new: Sridhar et al. picked 5 of 11 sensors a priori by mutual information for 80.6% accuracy against 79.6% with all 11 [[4]](#ref-4), and this group had cut 11 to 8 with under 0.5% loss and reached 15.2% WER with four, ranked by a monophone model [[2]](#ref-2). The search identifies the best subset on the evaluated data, and the data that chose it are not named (Fig. 6). Verdict: standard.

### M06 Decoder: Kaldi triphone HMM with HLDA, MLLR and SGMM

**Usual approach:** Of 54 wearable silent-sentence studies (pattern match, unique studies, Appendix), 30 name HMM decoding, 16 CTC and 9 attention sequence-to-sequence; the paper follows that majority, porting an acoustic-ASR recipe to sEMG.

**State of the art:** 97.17% phrase accuracy on 33 closed-set Chinese phrases, 256-channel HD-sEMG with CTC (2023, [later]) [[5]](#ref-5); 12.2% WER on open-vocabulary silent EMG (2024, [later]) [[6]](#ref-6).

The 2014 report already holds this pipeline and these subject rows [[2]](#ref-2). HLDA cuts Corpus 2 WER from 11.3% to 7.3% (Fig. 5), 35% relative (inference), but mixture count and dimension were chosen on the sequences they are reported on (Fig. 4). The 8.9% and the 12.2% are not comparable: five speaker-dependent subjects, a grammar and 88 to 167 test words against an open vocabulary [[6]](#ref-6). Verdict: standard.

### M07 Use-time constraint: natural-language class grammar

**Usual approach:** Of 64 sEMG studies scored with WER or CER (pattern match, sparse slot, Appendix), 21 name an n-gram language model, 14 a neural or large language model, 4 a grammar and 3 none. This paper sits at the restrictive end, its grammar built from the corpus's own sentence rules with each word replaced by a natural-language class.

**State of the art:** 12.2% WER on the open-vocabulary Gaddy benchmark with LLM rescoring (2024, [later]) [[6]](#ref-6).

The authors concede that the sentence-construction grammar is an upper bound, yet the class grammar costs one point more, 6.8% against 5.8% WER (Fig. 3), keeping nearly all of that constraint (inference). How it was built for Corpus 3 is not stated, so the final WER stays entangled with grammar coverage of the test phrases (Table 2). Verdict: standard.


## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Subject-dependent training, 2-3 h | Training action (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Prompted text only | Training supervision (slot-filled 31) | – | standard |
| M03 Training and adaptation | No calibration stated | Training and calibration (slot-filled 1,526) | – | not reported |
| M04 Use-time action | Silently mouthed speech | Use-time action (slot-filled 5,595) | – | standard |
| M05 Sensors | 11 sites; 2,047-subset search | Subset by search over trained models (pattern match 10) | [[3]](#ref-3) (2026): 4-channel best 47.2% WER | standard |
| M06 Processing and decoding | Kaldi triphone HMM + SGMM | HMM decoding (pattern match 30) | [[5]](#ref-5) (2023): 97.17% closed-set; [[6]](#ref-6) (2024): 12.2% WER | standard |
| M07 Lexicon and LM | NL-class grammar from corpus rules | n-gram language model (pattern match 21) | [[6]](#ref-6) (2024): 12.2% WER, LLM rescoring | standard |
| M08 Output | Word sequence text | Output (slot-filled 3,268) | – | standard |
| M09 Confirmation | Offline | Confirmation (slot-filled 82) | – | not applicable |
| M10 Correction | Offline | Correction (slot-filled 82) | – | not applicable |
| M11 Reference construction | Prompted transcripts, TIMIT sets | References (slot-filled 234) | – | not reported |
| M12 Evaluation | 8.9% WER, 5 subjects, split unstated | Sentence-disjoint or open-vocabulary test (pattern match 13) | [[6]](#ref-6) (2024): 12.2% WER open vocabulary | not reported |
| M13 Device and cost | 4-6 h lab sessions; mini sensors | Device constraints (slot-filled 6,075) | – | standard |

## Where the claims outrun the evidence

- The 8.9% WER (Table 2) equals the mean of subjects 1 to 5 of the 2014 SGMM table; with the sixth it is 11.2% [[2]](#ref-2), 26% higher in relative terms (inference).
- The "2,200-word vocabulary" is the corpus total; the test sets held 154, 167, 115 and 88 words [[2]](#ref-2), and no unseen-word count supports the "previously unseen words" claim (Table 2).
- The best 8-sensor subset is described as two sensors on one side of the face (Fig. 6), while this group's array had 4 face and 4 neck sites [[2]](#ref-2).
- No test partition is given for Corpus 2 or 3, and features, grammar, mixture count, HLDA dimension and sensor subset were all selected with no stated validation set (Fig. 2 to Fig. 6).

## What the field needs next

- M12: report every subject and a held-out protocol with unseen-word counts per set, reconciling the 2014 and 2018 numbers.
- M07: decode Corpus 3 with a language model trained on external text, against the class grammar on the same subjects.
- M05: choose the sensor subset on one session and report it on another, against the mutual-information shortcut [[4]](#ref-4).

## Questions for the authors

- Why does Table 2 list five subjects when Corpus 3 had six, and is the missing one the 22.4% WER subject of 2014?
- Which phrases trained and which tested the final system, and is it the 2014 leave-one-task-out scheme?
- How was the class grammar built for Corpus 3, and did it cover test phrases absent from training?
- On which data was the 8-sensor subset chosen, and how many test words per set were unseen?

## Appendix: literature search

- M05 emg-speech-electrode-subset (published table reused). Inclusion rule: surface-EMG speech studies that evaluate a reduced subset of their electrodes or rank electrodes, classified by how the subset is chosen; fixed-array, sensor-hardware-only and non-speech studies excluded. Ledger: 7,329 slot-filled; 42 pattern match (unique studies). Usual design: exhaustive or greedy search over trained models, 10 (pattern match). Read in full: [[4]](#ref-4), [[2]](#ref-2), [[3]](#ref-3).
- M06 wearable-silent-sentence-decoding (published table reused). Inclusion rule: sentence or phrase recognition from silently articulated speech measured by body-worn non-video sensors, classified by sentence decoder; lip video, imagined speech and overt-only studies excluded. Ledger: 7,345 slot-filled; 54 pattern match (unique studies). Usual design: HMM decoding, 30 (pattern match). Known-item recall 1.0. Read in full: [[5]](#ref-5), [[2]](#ref-2), [[6]](#ref-6).
- M07 emg-recognition-grammar-and-language-model (new topic). Inclusion rule: surface-EMG decoders scored with WER or CER, classified by the use-time linguistic constraint their full text names (rule grammar, n-gram, neural or large language model, none); a study counts under every design it names. Ledger: 119 slot-filled; 64 pattern match (unique studies). Usual design: n-gram language model, 21 (pattern match). Known-item recall 0.67. Read in full: [[6]](#ref-6), [[2]](#ref-2).
- M12 emg-text-unseen-sentence-test (published table reused). Inclusion rule: surface-EMG decoders scored with WER or CER, classified by whether the headline error is measured on sentences absent from all training data. Ledger: 6,960 slot-filled; 64 pattern match (unique studies). Usual design: sentence-disjoint or open-vocabulary test, 13 (pattern match). Known-item recall 1.0. Read in full: [[6]](#ref-6), [[2]](#ref-2).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Meltzner, G. S., Heaton, J. T., Deng, Y., De Luca, G., Roy, S. H., Kline, J. C. “Development of sEMG sensors and algorithms for silent speech recognition.” *Journal of Neural Engineering*, 2018, 15(4), 046031. doi:[10.1088/1741-2552/aac965](https://doi.org/10.1088/1741-2552/aac965). Target. Read as the PMC author manuscript. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/development-of-semg-sensors-and-algorithms-for-silent-speech-recognition) [wiki: doi-10.1088-1741-2552-aac965](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552-aac965/article.md)
2. <a id="ref-2"></a>Deng, Y., Heaton, J. T., Meltzner, G. S. “Towards a Practical Silent Speech Recognition System.” *Proc. Interspeech 2014*, 2014, 1164-1168. doi:[10.21437/Interspeech.2014-296](https://doi.org/10.21437/Interspeech.2014-296). Prior, same group; deciding prior for M05, M06, M12. [wiki: isca-deng14b_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-deng14b_interspeech/article.md) [wiki: isca-deng14b-practicalssi](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-deng14b-practicalssi/article.md)
3. <a id="ref-3"></a>Hwang, I., Lee, J., Lee, K. “EMG-to-Speech with Fewer Channels.” *arXiv preprint*, 2026. doi:[10.48550/arXiv.2602.06460](https://doi.org/10.48550/arXiv.2602.06460). arXiv:[2602.06460](https://arxiv.org/abs/2602.06460). Later; state of the art for M05 subset search. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/emg-to-speech-with-fewer-channels) [wiki: arxiv-2602.06460](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.06460/article.md)
4. <a id="ref-4"></a>Sridhar, V. K. R., Prasad, R., Natarajan, P. “Mutual Information analysis for feature and sensor subset selection in surface electromyography based speech recognition.” *Proc. Interspeech 2010*, 2010. doi:[10.21437/Interspeech.2010-377](https://doi.org/10.21437/Interspeech.2010-377). Prior; deciding prior for M05. [wiki: isca-sridhar10](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-sridhar10/article.md) [wiki: isca-sridhar10_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-sridhar10_interspeech/article.md)
5. <a id="ref-5"></a>Chen, X., Zhang, X., Chen, X., Chen, X. “Decoding Silent Speech Based on High-Density Surface Electromyogram Using Spatiotemporal Neural Network.” *IEEE Transactions on Neural Systems and Rehabilitation Engineering*, 2023, 31, 2069-2078. doi:[10.1109/TNSRE.2023.3266299](https://doi.org/10.1109/TNSRE.2023.3266299). Later; closed-phrase state of the art for M06. [later] [wiki: tnsre-3266299-hdsemg](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/tnsre-3266299-hdsemg/article.md)
6. <a id="ref-6"></a>Benster, T., Wilson, G., Elisha, R., Willett, F. R., Druckmann, S. “A Cross-Modal Approach to Silent Speech with LLM-Enhanced Recognition.” *arXiv preprint*, 2024. doi:[10.48550/arXiv.2403.05583](https://doi.org/10.48550/arXiv.2403.05583). arXiv:[2403.05583](https://arxiv.org/abs/2403.05583). Later; open-vocabulary state of the art for M06, M07, M12. [later] [wiki: arxiv-2403.05583](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2403.05583/article.md)
