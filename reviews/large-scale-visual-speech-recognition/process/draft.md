# Large-Scale Visual Speech Recognition

Brendan Shillingford, Yannis Assael, Matthew W. Hoffman, Thomas Paine, Cían Hughes, Utsav Prabhu, Hank Liao, Hasim Sak, Kanishka Rao, Lorrayne Bennett, Marie Mulville, Ben Coppin, Ben Laurie, Andrew Senior, Nando de Freitas. arXiv preprint, 2018. [arXiv:1807.05162](https://arxiv.org/abs/1807.05162)

## Verdict

The paper [[1]](#ref-1) changes M02, M06 and M07, all standard; its lasting contribution is data scale, not the decoder. None of the 59 earlier sentence-level lip-reading studies in the ledger trains on a video corpus of 1,000 hours or more (Appendix), against 3,886 hours here, but no training-size ablation measures what the scale buys. The claim to be first with deep phoneme recognition plus production-grade word decoding (Sec. 1) fails against [[2]](#ref-2) and [[3]](#ref-3) (Appendix). The LM-free ablation is a strength, but the LM's training text is not named (Sec. 4). The zero-shot LRS3 claim (Table 2) mixes training data, decoder, LM and a YouTube source never screened for TED talks.

## Against the field, component by component

### M02 Training supervision: mined corpus scale

**Usual approach:** None of the 59 studies before 2018-01 names a single video training corpus of 1,000 hours or more (pattern match, Appendix); the largest the target lists is LRS at about 246 hours [[4]](#ref-4) (Sec. 2). LSVSR mines 3,886 hours from public YouTube video, keeping about 2% of clips (Sec. 3).

**State of the art:** [[5]](#ref-5) [later] (2024) trains on 100k hours of transcribed YouTube video for 12.8% LRS3 visual-only WER; V2P's zero-shot 55.1% (Table 2) is 4.3 times that (inference).

LSVSR is 15.8 times LRS but 8.2 times the [concurrent] LRS3 [[6]](#ref-6) at about 475 hours (inference), so "an order of magnitude greater than any previous dataset" (Sec. 2) holds only against prior corpora. The field followed this direction [[5]](#ref-5). Standard, not ahead: no model is trained on a subset, so data and architecture are not separated in the gains over the retrained LipNet and WAS-style baselines (Table 1).

### M06 Processing: CTC phonemes with WFST word decoding

**Usual approach:** 57 of the 59 earlier studies mention HMM decoding (pattern match, Appendix); neural sentence-level lip readers emitted characters, by CTC [[7]](#ref-7) or attention [[4]](#ref-4). V2P emits 41 phonemes plus blank (Table 5) into lexicon and word n-gram WFSTs (Sec. 4).

**State of the art:** Sub-word outputs without a lexicon lead today: 12.8% LRS3 WER [[5]](#ref-5) [later] (2024), 17.6% on public data [[8]](#ref-8) [later] (2026).

Both halves preceded the target: [[2]](#ref-2) (prior) decodes visual-only DNN-HMM phoneme models through a Kaldi WFST with a pronunciation dictionary and word bigram (its Sec. 5); [[3]](#ref-3) (prior) decodes CTC phoneme or viseme posteriors through Eesen WFSTs, scoring video-only output in visemes (its Table 2). The authors credit Eesen and deep-network/HMM hybrids (Sec. 2), not these two. A recall check over 2,209 wiki studies finds no earlier visual-only CTC phoneme model decoded to words by WFST (Appendix). The measured phoneme gain is 3.2 WER points in the LipNet pair, 89.8% against 93.0% (Table 1), on one test set and one run. Standard.

### M07 Lexicon and LM: word 5-gram

**Usual approach:** 33 of the 59 earlier studies name a grammar, lexicon or dictionary and 7 an n-gram LM (pattern match, Appendix). V2P uses a Katz 5-gram with a vocabulary of about one million words (Sec. 4).

**State of the art:** [[8]](#ref-8) [later] (2026) reaches 17.6% LRS3 WER with no external LM.

Removing the LM costs 40.9% to 53.6% WER (Table 1), 31% relative (inference); only 1 of the 59 earlier studies states a no-LM condition (Appendix). The vocabulary-extension claim (Sec. 1) is untested: V2P-NoLM changes vocabulary and drops the LM at once, and no out-of-vocabulary rate is given. Standard.

### M12 Evaluation: human readers and uncertainty

**Usual approach:** 54 of the 59 earlier studies report no human-lipreader result (pattern match, Appendix); WAS [[4]](#ref-4) had a professional at 87.6% WER including declined clips (its Table 5).

**State of the art:** No later sentence-level study in the ledger table repeats a professional comparison (Appendix); the best LRS3 visual-only WER is 12.8% [[5]](#ref-5) [later] (2024).

The readers' 92.9% and 86.4% WER come from 274- and 153-video subsets, the model's 40.9% from the full test (Table 1); reader count is not stated. The ± values are bootstrap estimates over one training run (Sec. 5.1). Standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Voiced YouTube speech | Voiced speech recorded for training | – | standard |
| M02 Training-only supervision | 3,886 h mined YouTube, forced-aligned phonemes | No video corpus of 1,000 h or more; of 59 before 2018-01 (pattern match 59) | [[5]](#ref-5) 100k h, 12.8% LRS3 WER | standard |
| M03 Training and adaptation | From scratch; duration curriculum | Supervised training on transcribed data | – | standard |
| M04 Use-time action | Voiced speech at test | Voiced speech at use time | – | standard |
| M05 Sensors | Mouth-region video, faces within 30 degrees | Camera mouth region | – | standard |
| M06 Processing and decoding | CTC over 41 phonemes, lexicon and 5-gram WFSTs | HMM decoding; of 59 before 2018-01 (pattern match 57) | [[5]](#ref-5) 12.8% LRS3 WER | standard |
| M07 Lexicon and LM | Katz 5-gram, about 1M words; LM-free ablation | Grammar or lexicon; of 59 before 2018-01 (pattern match 33) | [[8]](#ref-8) 17.6%, no external LM | standard |
| M08 Output | Words via phonemes | Text output | – | standard |
| M09 Confirmation | None (offline) | Mostly absent | – | not applicable |
| M10 Correction | None (offline) | Mostly absent | – | not applicable |
| M11 Reference construction | Held-out LSVSR test; split not stated | Stated benchmark partition | – | not reported |
| M12 Evaluation | Professional readers; bootstrap; zero-shot LRS3 | No human-reader result; of 59 before 2018-01 (pattern match 54) | [[5]](#ref-5) 12.8% LRS3 WER | standard |
| M13 Device and cost | Offline benchmark | Offline GPU training | – | not applicable |

## Where the claims outrun the evidence

- Zero-shot "state-of-the-art performance" (Sec. 5.1): 55.1% against 57.9% for the [concurrent] TM-seq2seq [[9]](#ref-9) (Table 2) has no uncertainty for the comparator and mixes data, decoder and LM; the prose says V2P wins "in both experiments", but Table 2 has no TM-seq2seq filtered-test score.
- LRS3 comes from TED and TEDx talks [[6]](#ref-6) and LSVSR from public YouTube (Sec. 3); no exclusion of those talks is stated.
- The Table 1 caption calls the intervals standard deviations; Sec. 5.1 calls them standard errors.
- The LM text is unnamed (Sec. 4), so overlap with test transcripts is open.

## What the field needs next

- M02: train on nested LSVSR subsets, with seeds, tested on a public set.
- M07: decode with and without the 5-gram at a fixed vocabulary, then extend the vocabulary and report out-of-vocabulary rates.
- M12: retest LRS3 after removing TED and TEDx videos from training.

## Questions for the authors

- Is the test split by video, channel or speaker, and does it share speakers with training?
- Were TED or TEDx videos in LSVSR training?
- Which text trained the 5-gram LM?
- What is V2P's WER on the two human subsets, and how many readers took part?

## Appendix: literature search

- Setting, the same for every topic: sentence-level lip reading, VSR or AVSR, the 633-study ledger population of the M06 table. Window for the target (first public 2018-07): prior before 2018-01, [concurrent] 2018-01 to 2019-01. 88 studies are dated before 2018-01; removing 28 human-perception or neuroscience entries and 1 version duplicate leaves 59. Concurrent: 17 besides the target; 6 dated only to 2018 or undated are date unresolved. Counts are full-text pattern matches with mentions, reference lists removed (upper bounds).
- M02, asr-transcribed-unlabelled-video-training (published table, appended). Inclusion rule: the published rule (training-label source for unlabelled lip video), restricted to the setting and classified by a named video corpus of 1,000 hours or more. Ledger counts: 31 unique studies slot-filled; 1,049 unique studies pattern match. Of the 59: 1,000 hours or more 2 (read: formula, citation), so 59 without; YouTube 2; forced alignment 18. Recall check over 2,209 wiki studies before 2018-01: 8 hits, none a labelled video corpus of that size. Read: [[4]](#ref-4) (prior); [[5]](#ref-5) (state of the art). Known-item recall 1.0.
- M06, sentence-lipreading-sequence-objective (published table, appended). Inclusion rule: the published rule (sequence objective named in the full text), plus WFST, DNN-HMM and phoneme-unit patterns. Ledger counts: 7,345 unique studies slot-filled; 633 unique studies pattern match. Of the 59: HMM 57, phoneme units 52, DNN-HMM or tandem 14, WFST 7, CTC 5 (3 designs: [[7]](#ref-7), [[3]](#ref-3), one audio-visual character model), attention 1. Concurrent: CTC 10, attention 8. Recall check (CTC with WFST or Eesen, lips or video) over 2,209 wiki studies before 2018-01: 5 hits, 2 audio-visual designs, 3 mentions; 0 visual-only. Read: [[2]](#ref-2), [[3]](#ref-3) (prior); [[8]](#ref-8) (state of the art). Known-item recall 1.0.
- M07, use-time-language-model-visual-speech (published table, appended). Inclusion rule: the published rule and patterns (use-time language information named in the full text). Ledger counts: 119 unique studies slot-filled; 633 unique studies pattern match. Of the 59: grammar, lexicon or dictionary 33; n-gram 7; neural LM 0; no-LM statement 1. Concurrent: neural LM 3. Read: [[9]](#ref-9) ([concurrent]); [[8]](#ref-8) (state of the art). Known-item recall 1.0.
- M12, human-lipreader-baseline (published table, appended). Inclusion rule: the published rule (machine and human lipreaders on the same items), plus run-variability and bootstrap patterns. Ledger counts: 6,960 unique studies slot-filled; 64 unique studies pattern match. Of the 59: human-lipreader result 5 (54 without); confirmed same-item comparisons 3 ([[7]](#ref-7), [[4]](#ref-4), one other); variability estimate 10; bootstrap 6. Read: [[4]](#ref-4) (prior). Known-item recall 0.8.

## References

Numbered by first citation. BibTeX in the same order and keys: [large-scale-visual-speech-recognition.bib](large-scale-visual-speech-recognition.bib).

1. <a id="ref-1"></a>Shillingford, B., Assael, Y., Hoffman, M. W., Paine, T., Hughes, C., Prabhu, U., et al. “Large-Scale Visual Speech Recognition.” *arXiv preprint*, 2018. arXiv:[1807.05162](https://arxiv.org/abs/1807.05162). First public as arXiv:1807.05162 (2018-07); read as v3 (dated 1 Oct 2018); later version at Interspeech 2019. [wiki: arxiv-1807.05162](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1807.05162/article.md) [wiki: isca-shillingford19-largescale](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-shillingford19-largescale/article.md) [wiki: isca-shillingford19_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-shillingford19_interspeech/article.md)
2. <a id="ref-2"></a>Thangthai, K., Harvey, R. “Improving Computer Lipreading via DNN Sequence Discriminative Training Techniques.” *Interspeech*, 2017. doi:[10.21437/Interspeech.2017-1550](https://doi.org/10.21437/Interspeech.2017-1550). Prior; deciding prior for M06 (visual-only DNN-HMM phoneme models decoded through a Kaldi WFST with a pronunciation dictionary and word bigram). [wiki: isca-thangthai17_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-thangthai17_interspeech/article.md) [wiki: isca-thangthai17-dnnsdt](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-thangthai17-dnnsdt/article.md) [wiki: isca-thangthai17_lipdnn](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-thangthai17_lipdnn/article.md) [wiki: isca-thangthai17_lipread](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-thangthai17_lipread/article.md)
3. <a id="ref-3"></a>Sanabria, R., Metze, F., De La Torre, F. “Robust End-to-End Deep Audiovisual Speech Recognition.” *arXiv preprint*, 2016. arXiv:[1611.06986](https://arxiv.org/abs/1611.06986). Prior; deciding prior for M06 (CTC phoneme/viseme posteriors decoded through Eesen WFSTs, audio-visual). [wiki: arxiv-1611.06986](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1611.06986/article.md)
4. <a id="ref-4"></a>Chung, J. S., Senior, A., Vinyals, O., Zisserman, A. “Lip Reading Sentences in the Wild.” *IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2017. doi:[10.1109/CVPR.2017.367](https://doi.org/10.1109/CVPR.2017.367). arXiv:[1611.05358](https://arxiv.org/abs/1611.05358). Prior; LRS corpus, character attention decoder, professional lipreader on LRS test clips. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lip-reading-sentences-in-the-wild) [wiki: arxiv-1611.05358](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1611.05358/article.md) [wiki: cvf-chung17-lipreadwild](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-chung17-lipreadwild/article.md)
5. <a id="ref-5"></a>Chang, O., Liao, H., Serdyuk, D., Shah, A., Siohan, O. “Conformers are All You Need for Visual Speech Recognition.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2024, 10136-10140. arXiv:[2302.10915](https://arxiv.org/abs/2302.10915). 100k h transcribed YouTube video; best LRS3 visual-only WER (M02, M06). [later] [wiki: arxiv-2302.10915](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2302.10915/article.md)
6. <a id="ref-6"></a>Afouras, T., Chung, J. S., Zisserman, A. “LRS3-TED: a large-scale dataset for visual speech recognition.” *arXiv preprint*, 2018. arXiv:[1809.00496](https://arxiv.org/abs/1809.00496). LRS3-TED corpus from TED and TEDx talks. [concurrent] [wiki: arxiv-1809.00496](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1809.00496/article.md)
7. <a id="ref-7"></a>Assael, Y. M., Shillingford, B., Whiteson, S., de Freitas, N. “LipNet: End-to-End Sentence-level Lipreading.” *arXiv preprint*, 2016. arXiv:[1611.01599](https://arxiv.org/abs/1611.01599). Prior; character CTC, visual-only, GRID. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lipnet-end-to-end-sentence-level-lipreading) [wiki: arxiv-1611.01599](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1611.01599/article.md)
8. <a id="ref-8"></a>Haliassos, A., Mira, R., Petridis, S. “Pay Attention to CTC: Fast and Robust Pseudo-Labelling for Unified Speech Recognition.” *International Conference on Learning Representations (ICLR)*, 2026. arXiv:[2602.19316](https://arxiv.org/abs/2602.19316). Best public-data LRS3 visual-only WER, no external LM (M07). [later] [wiki: arxiv-2602.19316](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.19316/article.md)
9. <a id="ref-9"></a>Afouras, T., Chung, J. S., Senior, A., Vinyals, O., Zisserman, A. “Deep Audio-Visual Speech Recognition.” *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 2018. doi:[10.1109/TPAMI.2018.2889052](https://doi.org/10.1109/TPAMI.2018.2889052). arXiv:[1809.02108](https://arxiv.org/abs/1809.02108). TM-seq2seq, the comparison system in the target's Table 2. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/deep-audio-visual-speech-recognition) [wiki: arxiv-1809.02108](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1809.02108/article.md) [wiki: doi-10.1109-tpami.2018.2889052](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tpami.2018.2889052/article.md)
