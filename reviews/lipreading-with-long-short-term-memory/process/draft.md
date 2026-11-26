# Lipreading with Long Short-Term Memory

Wand, M., Koutník, J., Schmidhuber, J. · ICASSP 2016 · 2016 · [DOI:10.1109/ICASSP.2016.7472852](https://doi.org/10.1109/ICASSP.2016.7472852) · [arXiv:1601.08188](https://arxiv.org/abs/1601.08188)

## Verdict

The paper changes decoding (M06): a feed-forward layer and two LSTM layers trained jointly on mouth crops replace hand-crafted features and a separate classifier [[1]](#ref-1). The design is ahead of its field: of 159 lip-reading studies first public before 2015-07, 113 name an HMM and 2 a recurrent network, and no read prior trains a recurrent model together with its visual front end (Appendix); the gain repeats on two disjoint speaker groups. Learning from raw lip pixels is not new, since an uncited 1994 time-delay network was trained on gray-level lip pixels [[2]](#ref-2); what is new is recurrent memory over the word. Pre-cut word clips (M04) and per-speaker splits (M12) are standard for the time and stated by the authors. The only baselines are linear SVMs on a six-frame vector, with no HMM although 113 of 159 prior studies name one (Appendix), so the gain is over a non-sequential classifier, not the usual pipeline. The 11.6% gain is relative, 8.3 points absolute (inference), and the t-test has no stated sample unit.

## Against the field, component by component

### M06 Decoding: recurrent network trained jointly on mouth pixels

**Usual approach:** Of 159 lip-reading studies first public before 2015-07 (pattern match, unique studies, Appendix), 113 name an HMM, 98 hand-crafted features, 16 an SVM, 4 learned deep features and 2 a recurrent network. The paper uses one network on 40 × 40 mouth crops (Sec. 3, Sec. 5.1).

**State of the art:** SyncVSR (2024) reaches 93.2% top-1 accuracy on the 500-word, speaker-independent LRW test, mean of three runs [[3]](#ref-3); the paper's speaker-dependent GRID word task has no current counterpart. Recurrent networks are named in 415 of 660 [later] studies (Appendix).

Neither recurrent prior has the design: Movellan and Mineiro run one diffusion network per word over pre-extracted lip-contour PCA features [[4]](#ref-4), and Wojdeł uses Jordan and Elman networks only for frame tasks over pre-extracted lip features, with HMMs for words [[5]](#ref-5). The deep-feature priors train features apart from the classifier: autoencoders feeding a linear SVM [[6]](#ref-6), and per-speaker CNNs feeding GMM-HMMs [[7]](#ref-7), as the authors themselves note (Sec. 2). A whole-wiki full-text check (34 matching studies, Appendix) adds none. The closest prior is the MS-TDNN of Duchnowski et al., trained by back-propagation on 384 gray-level pixel values per lip frame, with time handled by delays and DTW [[2]](#ref-2); it is missing from the reference list, so "Manual feature extraction is no longer required" (Sec. 1) restates a 1994 capability. The effect repeats: 79.4% against 71.1% for HOG + SVM on speakers 1–9 and 79.6% against 71.3% on speakers 10–19 (Table 1). Verdict: ahead.

### M04 Use-time input: word clips cut from corpus alignments

**Usual approach:** Of the 159 prior studies (pattern match, Appendix), 65 name continuous or sentence-level decoding and 41 isolated or pre-segmented word input. The paper classifies clips cut with GRID's frame-level alignments (Sec. 3), so word boundaries are given, not found.

**State of the art:** On LRW, SyncVSR (2024) scores 95.0% with word-boundary input and 93.2% without [[3]](#ref-3), 1.8 points (inference); GRID is now decoded as whole sentences, at 0.99% WER [[8]](#ref-8).

Pre-cut clips were common, e.g. hand-cut CUAVE digits [[9]](#ref-9). Letters are the weakest class (69.8% against 93.4% for other words on speaker 7, Sec. 5.2) and, as the authors note, can span 3–4 frames, so automatic segmentation errors would fall on the hardest class (inference). Verdict: standard.

### M12 Evaluation: per-speaker splits with speaker variability

**Usual approach:** Of the 159 prior studies (pattern match, Appendix), 52 name speaker-independent and 37 speaker-dependent evaluation, and 76 a standard deviation, confidence interval or significance test. The paper trains and tests within each speaker, holding speakers 10–19 out only from parameter selection, as the authors state (Sec. 3).

**State of the art:** LinProVSR (2026) reaches 0.99% visual-only WER on GRID sentences, split type not named [[8]](#ref-8).

Both protocols were in use: within-speaker [[7]](#ref-7), [[9]](#ref-9) and held-out speakers [[4]](#ref-4), [[6]](#ref-6). Speaker SDs (Table 1) are a strength; five random test videos per word (Sec. 3), no seeds and no session allocation are not. Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | GRID read sentences | Read speech | – | standard |
| M02 Training-only supervision | GRID labels, alignments | Corpus labels | – | standard |
| M03 Training and adaptation | Per-speaker training | Per-speaker training | – | standard |
| M04 Use-time action | Word clips cut from corpus alignments | Continuous decoding named (pattern match 65) | [[3]](#ref-3) (2024): LRW 95.0% with boundaries | standard |
| M05 Sensors | 40 x 40 gray mouth crop | Camera video | – | standard |
| M06 Processing and decoding | FF + 2 LSTM layers, joint training | HMM classifier (pattern match 113) | [[3]](#ref-3) (2024): LRW top-1 93.2% | ahead |
| M07 Lexicon and LM | None, 51-way softmax | No LM | – | standard |
| M08 Output | 51 word classes | Word classes | – | standard |
| M09 Confirmation | Offline | Offline | – | not applicable |
| M10 Correction | Offline | Offline | – | not applicable |
| M11 Reference construction | GRID labels | Corpus references | – | standard |
| M12 Evaluation | Per-speaker split, SDs, t-test | Speaker-independent named (pattern match 52) | [[8]](#ref-8) (2026): GRID WER 0.99% | standard |
| M13 Device and cost | Offline lab study | Offline | – | not applicable |

## Where the claims outrun the evidence

- **Baselines.** Both are linear SVMs on a six-frame vector (Sec. 5.1); no HMM or time-delay baseline is run, although HMMs dominate the prior population (Appendix) and a pixel-input MS-TDNN existed [[2]](#ref-2). The authors' view that an HMM would not help (Sec. 5.1) is untested.
- **Gain.** "Improves the accuracy by 11.6%" (Sec. 5.2) is relative; Table 1 gives 8.3 points (inference).
- **Significance.** The one-tailed t-test "with p = 0.05" (Sec. 5.2) has no sample unit, pairing or statistic.
- **Preprocessing.** Standardization over "the complete dataset" (Sec. 3) includes test clips as written (inference); Duchnowski et al. fitted PCA and LDA on training data only [[2]](#ref-2).
- **CNN layers.** That they did not help (Sec. 6) rests on unreported experiments.

## What the field needs next

- M06: an HMM and a time-delay network on the same 40 × 40 crops and splits to isolate recurrence.
- M12: held-out-speaker GRID evaluation with repeated seeds, which the authors list as future work (Sec. 6).
- M04: decoding whole 75-frame sentences without corpus alignments.

## Questions for the authors

- Did all three systems share the same random splits, and how many seeds or repeats were run?
- Is the t-test over speakers or clips, is it paired, and is 0.05 the observed p-value or the threshold?
- Were standardization statistics computed on training clips only?

## Appendix: literature search

Population for all three topics: ledgers that name optical-camera input and lip reading, visual speech recognition or audio-visual speech recognition (1,359 folders, 975 unique studies, pattern match). Studies whose full text names no automatic recognizer or classifier are excluded (54 prior, 59 [later]); versions count once. Dating against the target's first public month 2016-01: prior before 2015-07 (159 studies), [later] after 2016-07 (660 studies), 23 date unresolved. Design counts are full-text pattern matches with reference lists removed; related-work mentions count, so they are upper bounds.

**M06, lipreading-temporal-model-and-feature-learning.** Inclusion rule: automatic lip-reading, VSR or AVSR studies with optical-camera input, classified by the visual model their full text names (recurrent network, time-delay network, learned deep features, hand-crafted features, HMM, SVM). Slot-filled M06: 7,345 unique studies. Prior (159): HMM 113, hand-crafted features 98, SVM 16, time-delay network 10, learned deep features 4, recurrent network 2. [Later] (660): recurrent 415, learned deep features 442, hand-crafted 189, HMM 224. Usual design at the time: HMM classifier, 113 of 159 (pattern match). Whole-wiki full-text check: every folder dated 2015 or earlier with source text (723 of 1,844 folders), recurrent or time-delay network terms together with visual-speech terms, 34 matching studies; none trains a recurrent network jointly with its visual front end. Read in full: [[2]](#ref-2), [[4]](#ref-4), [[5]](#ref-5), [[6]](#ref-6), [[7]](#ref-7); state of the art [[3]](#ref-3). Known-item recall 1.0 (9 of 9).

**M04, lipreading-word-segmentation-at-test.** Inclusion rule: the same population, classified by whether the full text names isolated or pre-segmented word input or continuous, connected or sentence-level decoding; corpus-derived boundaries at test count as pre-segmented. Slot-filled M04: 5,595 unique studies. Prior (159): continuous decoding 65, isolated word input 41. [Later] (660): continuous 332, isolated 113. Usual design at the time: continuous or connected decoding, 65 of 159 (pattern match). Read in full: [[9]](#ref-9); state of the art [[3]](#ref-3). Known-item recall 1.0 (8 of 8).

**M12, lipreading-speaker-dependence-protocol.** Inclusion rule: the same population, classified by the evaluation partition the full text names (speaker-dependent or seen speakers, speaker-independent or held-out speakers) and by whether it reports a standard deviation, confidence interval or significance test. Slot-filled M12: 6,960 unique studies. Prior (159): speaker-independent 52, speaker-dependent 37, variability or significance 76. [Later] (660): speaker-independent 213, speaker-dependent 142, variability or significance 267. Usual design at the time: speaker-independent evaluation named, 52 of 159 (pattern match). State of the art [[8]](#ref-8). Known-item recall 1.0 (8 of 8).

## References

Numbered by first citation. BibTeX in the same order and keys: [lipreading-with-long-short-term-memory.bib](lipreading-with-long-short-term-memory.bib).

1. <a id="ref-1"></a>Wand, M., Koutník, J., Schmidhuber, J. “Lipreading with Long Short-Term Memory.” *2016 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2016, 6115-6119. doi:[10.1109/ICASSP.2016.7472852](https://doi.org/10.1109/ICASSP.2016.7472852). arXiv:[1601.08188](https://arxiv.org/abs/1601.08188). Target. Read as arXiv v1 (29 Jan 2016). [wiki: doi-10.1109-icassp.2016.7472852](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-icassp.2016.7472852/article.md) [wiki: arxiv-1601.08188](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1601.08188/article.md)
2. <a id="ref-2"></a>Duchnowski, P., Meier, U., Waibel, A. “See Me, Hear Me: Integrating Automatic Speech Recognition and Lip-reading.” *Proc. 3rd International Conference on Spoken Language Processing (ICSLP 94)*, 1994. <https://www.isca-archive.org/icslp_1994/duchnowski94_icslp.html> Prior; deciding prior for M06 (MS-TDNN on gray-level lip pixels). [wiki: isca-duchnowski94_icslp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-duchnowski94_icslp/article.md)
3. <a id="ref-3"></a>Ahn, Y. J., Park, J., Park, S., Choi, J., Kim, K. “SyncVSR: Data-Efficient Visual Speech Recognition with End-to-End Crossmodal Audio Token Synchronization.” *Interspeech 2024*, 2024. arXiv:[2406.12233](https://arxiv.org/abs/2406.12233). State of the art for M06 and M04 (LRW word accuracy). [later] [wiki: arxiv-2406.12233](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2406.12233/article.md)
4. <a id="ref-4"></a>Movellan, J. R., Mineiro, P. “A Diffusion Network Approach to Visual Speech Recognition.” *Proc. Auditory-Visual Speech Processing (AVSP 1999)*, 1999. <https://www.isca-archive.org/avsp_1999/movellan99_avsp.html> Prior; deciding prior for M06 (stochastic recurrent network on lip-contour features). Same paper also held as wiki folder avsp99-movellan99_avsp. [wiki: isca-movellan99_avsp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-movellan99_avsp/article.md)
5. <a id="ref-5"></a>Wojdeł, J. C. “Automatic Lipreading in the Dutch Language.” *PhD thesis, Technische Universiteit Delft*, 2003. <https://openalex.org/W1607796654> Prior; deciding prior for M06 (Jordan and Elman networks for frame tasks, HMM word recognizer). [wiki: oa-W1607796654](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/oa-W1607796654/article.md)
6. <a id="ref-6"></a>Ngiam, J., Khosla, A., Kim, M., Nam, J., Lee, H., Ng, A. Y. “Multimodal Deep Learning.” *Proceedings of the 28th International Conference on Machine Learning (ICML 2011)*, 2011. doi:[10.5555/3104482.3104569](https://doi.org/10.5555/3104482.3104569). Prior; deep-feature prior for M06. [wiki: w2076462394-ngiamavsr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/w2076462394-ngiamavsr/article.md)
7. <a id="ref-7"></a>Noda, K., Yamaguchi, Y., Nakadai, K., Okuno, H. G., Ogata, T. “Lipreading using Convolutional Neural Network.” *Interspeech 2014*, 2014. doi:[10.21437/Interspeech.2014-293](https://doi.org/10.21437/Interspeech.2014-293). Prior; cited by the target; deep-feature prior for M06. Same paper also held as wiki folder isca-noda14_interspeech. [wiki: isca-noda14-cnnlip](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-noda14-cnnlip/article.md)
8. <a id="ref-8"></a>Xue, F., Zhu, B., Jia, W., Li, S., Li, Y., Zhang, J., et al. “LinProVSR: Linguistics-Knowledge Guided Progressive Disambiguation Network for Visual Speech Recognition.” *Proceedings of the AAAI Conference on Artificial Intelligence (AAAI-26)*, 2026. doi:[10.1609/aaai.v40i14.38133](https://doi.org/10.1609/aaai.v40i14.38133). State of the art for M12 (GRID WER). [later] [wiki: aaai-38133-linprovsr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/aaai-38133-linprovsr/article.md)
9. <a id="ref-9"></a>Kumaravel, S. S. “Visual Speech Recognition using Histogram of Oriented Displacements.” *MS thesis, Clemson University*, 2015. <https://tigerprints.clemson.edu/all_theses/2112/> Prior; isolated-word, speaker-dependent example for M04 and M12. [wiki: oa-W650851844](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/oa-W650851844/article.md)
