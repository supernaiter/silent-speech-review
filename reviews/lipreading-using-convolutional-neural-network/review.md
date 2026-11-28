# Lipreading using Convolutional Neural Network

Noda, K., Yamaguchi, Y., Nakadai, K., Okuno, H. G., Ogata, T. · Interspeech 2014 · 2014 · [DOI:10.21437/Interspeech.2014-293](https://doi.org/10.21437/Interspeech.2014-293)

## Verdict

The paper [[1]](#ref-1) changes the visual front end (M06): a CNN on mouth images emits 40 phoneme posteriors for a GMM-HMM; no CNN appears among the 88 prior lip-reading decoders (pattern match, Appendix), but a network on lip pixels [[2]](#ref-2), network phoneme posteriors decoded by HMMs [[3]](#ref-3) and features learned from mouth regions [[4]](#ref-4) all came first. M06 is standard, not ahead: the gain over PCA is one comparison on one test set, without seeds or a named test speaker (Sec. 6.3). Evaluation (M12) is behind: the CNN is trained on shuffled frames of all 300 words (Sec. 5), so the 84 "open-vocabulary" test words are unseen only by the HMM, while read priors hold out whole utterances or speakers [[5]](#ref-5). The strongest confound is supervision: only the CNN features see phoneme labels. "Significantly outperform" (Abstract) has no test statistic.

## Against the field, component by component

### M06 Visual front end: CNN phoneme posteriors into a GMM-HMM

**Usual approach:** Of the 88 prior lip-reading decoders (mention counts, pattern match, Appendix), 79 name an HMM and 67 hand-crafted appearance or shape features (DCT, PCA, AAM); 18 name a neural network with phonetic or viseme units, 1 learned deep features [[4]](#ref-4) and 0 a CNN. The paper swaps the hand-crafted stage for a supervised CNN and keeps the HMM.

**State of the art:** SyncVSR (2024) reaches 93.2% top-1 on the LRW word benchmark (visual only, no word boundaries, mean of three runs), trained on 157 h of LRW video with vq-wav2vec audio-token targets pretrained on outside audio [[6]](#ref-6) [later]. The paper's best is about 37% on 84 unseen words of seen speakers (Sec. 6.3); vocabulary, speakers and task differ, so no gap can be read off (inference).

Duchnowski et al. fed 384-dimensional lip-pixel vectors to an MS-TDNN with phoneme and viseme layers [[2]](#ref-2); Heckmann et al. decoded ANN phoneme posteriors, from lip parameters taken by blue-ink chroma keying, with phoneme HMMs [[3]](#ref-3); Ngiam et al. learned autoencoder features from PCA-whitened mouth regions [[4]](#ref-4). What is new is convolution over mouth pixels: a whole-wiki check finds no earlier CNN on lip images (Appendix), so the authors' "remain unaddressed" (Sec. 2) holds for CNNs, not for neural networks on lip images. The authors' [concurrent] journal paper reuses the pipeline [[7]](#ref-7); 393 of 625 [later] decoders name a CNN (mention counts, Appendix). The three Gaussian counts of Fig. 5 are settings on one test set, not repetitions. Verdict: standard.

### M12 Evaluation: shuffled frames and test words seen by the CNN

**Usual approach:** Of the same 88 prior decoders (mention counts, pattern match, Appendix), 36 name speaker-independent tests, 23 speaker-dependent tests, 20 a standard deviation, interval or significance test, and 0 a random frame-level split. The paper splits shuffled frames 5/6 to 1/6 (Sec. 5) and tests seen speakers (Sec. 6.3).

**State of the art:** On AVLetters2 with one speaker held out per fold, Petridis et al. (2019) report 36.8% (SD 2.9, ten runs) visual-only, against 8.3% listed for Cox et al.'s AAM+HMM [[8]](#ref-8) [later].

Against best comparable work, five read priors hold whole utterances or speakers out of training, meeting the rule of three: letter sequences split 170/15/15 with a cross-validation set [[2]](#ref-2), sentence halves [[3]](#ref-3), speaker-independent isolated words [[9]](#ref-9), one speaker held out per fold [[5]](#ref-5), odd versus even speakers [[4]](#ref-4). The CNN is trained on frames of all 300 words (Sec. 5), so the 84 test words are new only to the HMM, and 100 Hz phoneme test frames have same-utterance neighbours in training (inference). Visual-only accuracy "degrades dramatically" for held-out speakers [[5]](#ref-5), and the authors concede their data cannot support a speaker-independent model (Sec. 7). With test words excluded from CNN training, the same group's best visual word rate was about 22.5% on 40 test words [[7]](#ref-7); the test sets differ, so this fits a leak without measuring it (inference). Verdict: behind.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Read isolated Japanese ATR words | Read speech | – | standard |
| M02 Training-only supervision | Phoneme labels by audio forced alignment (HTK) | Aligned phonetic labels | – | standard |
| M03 Training and adaptation | Six speaker-specific CNNs; no adaptation | Per-speaker or pooled training | – | standard |
| M04 Use-time action | Pre-segmented isolated words, offline | Isolated or continuous input | – | standard |
| M05 Sensors | One frontal 100 Hz monochrome camera; manual mouth crop | Camera, automatic or manual ROI | – | standard |
| M06 Processing and decoding | CNN phoneme posteriors into a GMM-HMM | HMM over hand-crafted features (pattern match 79) | [[6]](#ref-6) (2024): LRW top-1 93.2%, no word boundaries | standard |
| M07 Lexicon and LM | No language model or lexicon reported | Word HMMs, no LM | – | standard |
| M08 Output | Isolated word; 40 phoneme posteriors as features | Word classes | – | standard |
| M09 Confirmation | Offline | Offline | – | not applicable |
| M10 Correction | Offline | Offline | – | not applicable |
| M11 Reference construction | Corpus word labels | Corpus references | – | standard |
| M12 Evaluation | Shuffled-frame split; test words in CNN training; seen speakers | Held-out utterances; speaker-independent named (pattern match 36) | [[8]](#ref-8) (2019): AVLetters2, speaker held out, 36.8%, ten runs | behind |
| M13 Device and cost | Offline laboratory study, one GPU | Offline | – | not applicable |

## Where the claims outrun the evidence

- **"Significantly outperform"** (Abstract) rests on Fig. 5 with no test, interval or repeat (Sec. 6.3).
- **Supervision confound.** Only the CNN features are trained with phoneme labels (Sec. 6.3); a labelled network on PCA inputs, as in [[3]](#ref-3), is the missing control.
- **Untested claims.** Shift- and rotation-resistance (Sec. 1) is not tested; "hand-labeled data are not required" (Sec. 1) sits beside manual 128 × 128 mouth crops (Sec. 4).
- **"Reliable information source"** (Sec. 6.3) rests on about 37% words on seen speakers, test words inside the CNN training pool (Sec. 5).
- The authors themselves trace weak consonants to labels and sample counts (Sec. 6.1) and the weaker all-speaker CNN to limited image variation (Sec. 5, footnote 1).

## What the field needs next

- M12: tests on held-out utterances and speakers, a CNN trained without test-word frames, repeated runs.
- M06: a network on PCA or pixel inputs with the same phoneme labels, to isolate convolution.
- M02: audio-aligned against visually refined phoneme boundaries, since the authors trace consonant errors to labels (Sec. 6.1).

## Questions for the authors

- Were frames of the 84 test words in the CNN training set?
- Which speakers give the Fig. 5 word result, pooled or averaged?
- What did the single all-speaker CNN score (Sec. 5, footnote 1)?
- What does a majority-class baseline score on the phoneme test frames?

## Appendix: literature search

Population (one for both topics): lip-reading, VSR or AVSR decoders whose ledger names optical-camera input; versions merged by ledger key and by real title (empty index titles filled from wiki manifests); 42 non-decoders removed by a checked list (perception, speaker identification, synthesis, tracking, segmentation, corpora, enhancement, surveys) and 190 by a recognizer-term filter, hand-checked for prior and [concurrent] studies; the same group's journal paper [[7]](#ref-7) added; the target (two wiki folders) excluded. Dating against 2014-09: prior before 2014-03, [concurrent] 2014-03 to 2015-03, [later] after; months from arXiv ids, ICASSP (May) and ISCA venues (September). Result: 88 prior, 11 [concurrent], 625 [later], 2 date unresolved. Design counts are full-text pattern matches with reference lists removed; related-work mentions count (upper bounds).

**M06, lipreading-temporal-model-and-feature-learning** (published table, appended). Inclusion rule: decoders of the population classified by the visual model their full text names: CNN on mouth images, learned deep features, neural network with phonetic or viseme units (TDNN, ANN/HMM), phoneme a posteriori features, hand-crafted features, HMM. Ledger: slot-filled M06 7,345 unique studies; pattern match 975 unique studies. Prior (88): HMM 79, hand-crafted 67, neural network with phonetic or viseme units 18, learned deep features 1, phoneme a posteriori features 1 [[3]](#ref-3), CNN 0 (one false hit, the CNN news network, removed). [Concurrent] (11): CNN 1 [[7]](#ref-7). [Later] (625): CNN 393, learned deep features 442. Usual design at the time: HMM over hand-crafted features, 79 of 88 (pattern match). Whole-wiki check (743 folders dated 2014 or earlier with lip-reading terms): CNN, only the target. Read: [[2]](#ref-2), [[3]](#ref-3), [[4]](#ref-4), [[7]](#ref-7); state of the art [[6]](#ref-6). Known-item recall 1.0 (published table).

**M12, lipreading-speaker-dependence-protocol** (published table, appended). Inclusion rule: the same population classified by the evaluation partition its full text names: speaker-independent, speaker-dependent, random frame-level split, cross-validation or jackknife, and variability or significance reporting. Ledger: slot-filled M12 6,960 unique studies; pattern match 975 unique studies. Prior (88): speaker-independent 36, speaker-dependent 23, cross-validation or jackknife 23, variability or significance 20, random frame split 0. [Concurrent] (11): random frame split 1. [Later] (625): speaker-independent 202, speaker-dependent 151, variability or significance 200, random frame split 23. Usual design at the time: whole utterances held out, speaker-independent named in 36 of 88 (pattern match). Read: [[2]](#ref-2), [[3]](#ref-3), [[9]](#ref-9), [[5]](#ref-5), [[4]](#ref-4), [[7]](#ref-7); state of the art [[8]](#ref-8). Known-item recall 1.0 (published table).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Noda, K., Yamaguchi, Y., Nakadai, K., Okuno, H. G., Ogata, T. “Lipreading using Convolutional Neural Network.” *Interspeech 2014*, 2014, 1149-1153. doi:[10.21437/Interspeech.2014-293](https://doi.org/10.21437/Interspeech.2014-293). Target. Also held as wiki folder isca-noda14_interspeech. [wiki: isca-noda14-cnnlip](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-noda14-cnnlip/article.md) [wiki: isca-noda14_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-noda14_interspeech/article.md)
2. <a id="ref-2"></a>Duchnowski, P., Meier, U., Waibel, A. “See Me, Hear Me: Integrating Automatic Speech Recognition and Lip-reading.” *Proc. 3rd International Conference on Spoken Language Processing (ICSLP 94)*, 1994. doi:[10.21437/ICSLP.1994-139](https://doi.org/10.21437/ICSLP.1994-139). Prior; deciding prior for M06 (MS-TDNN on lip pixels) and M12 (whole-sequence split with a cross-validation set). [wiki: isca-duchnowski94_icslp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-duchnowski94_icslp/article.md)
3. <a id="ref-3"></a>Heckmann, M., Berthommier, F., Kroschel, K. “A Hybrid ANN/HMM Audio-Visual Speech Recognition System.” *Proc. Auditory-Visual Speech Processing (AVSP 2001)*, 2001. <https://www.isca-archive.org/avsp_2001/heckmann01_avsp.html> Prior; deciding prior for M06 (ANN phoneme posteriors from lip parameters into HMMs) and M12 (utterance-level split). [wiki: isca-heckmann01-annhmm](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-heckmann01-annhmm/article.md)
4. <a id="ref-4"></a>Ngiam, J., Khosla, A., Kim, M., Nam, J., Lee, H., Ng, A. Y. “Multimodal Deep Learning.” *Proceedings of the 28th International Conference on Machine Learning (ICML 2011)*, 2011. <https://ai.stanford.edu/~ang/papers/icml11-MultimodalDeepLearning.pdf> Prior; cited by the target; deciding prior for M06 (learned features from mouth regions) and M12 (speaker-independent CUAVE split). [wiki: w2076462394-ngiamavsr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/w2076462394-ngiamavsr/article.md)
5. <a id="ref-5"></a>Cox, S., Harvey, R., Lan, Y., Newman, J., Theobald, B. “The challenge of multispeaker lip-reading.” *Proc. International Conference on Auditory-Visual Speech Processing (AVSP 2008)*, 2008. <https://www.isca-archive.org/avsp_2008/cox08_avsp.html> Prior; deciding prior for M12 (speaker held out per fold; speaker-independent degradation). [wiki: isca-cox08_avsp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-cox08_avsp/article.md)
6. <a id="ref-6"></a>Ahn, Y. J., Park, J., Park, S., Choi, J., Kim, K. “SyncVSR: Data-Efficient Visual Speech Recognition with End-to-End Crossmodal Audio Token Synchronization.” *Interspeech 2024*, 2024. doi:[10.21437/Interspeech.2024-432](https://doi.org/10.21437/Interspeech.2024-432). arXiv:[2406.12233](https://arxiv.org/abs/2406.12233). State of the art for the M06 visual front end (LRW word accuracy). [later] [wiki: arxiv-2406.12233](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2406.12233/article.md)
7. <a id="ref-7"></a>Noda, K., Yamaguchi, Y., Nakadai, K., Okuno, H. G., Ogata, T. “Audio-visual speech recognition using deep learning.” *Applied Intelligence*, 2015, 42, 722-737. doi:[10.1007/s10489-014-0629-7](https://doi.org/10.1007/s10489-014-0629-7). Same authors; same CNN pipeline with test words excluded from CNN training. Published online 20 December 2014. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/audio-visual-speech-recognition-using-deep-learning) [wiki: doi-10.1007-s10489-014-0629-7](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1007-s10489-014-0629-7/article.md)
8. <a id="ref-8"></a>Petridis, S., Wang, Y., Ma, P., Li, Z., Pantic, M. “End-to-End Visual Speech Recognition for Small-Scale Datasets.” *Pattern Recognition Letters*, 2020. doi:[10.1016/j.patrec.2020.01.022](https://doi.org/10.1016/j.patrec.2020.01.022). arXiv:[1904.01954](https://arxiv.org/abs/1904.01954). Protocol state of the art for M12 (speaker-independent splits, ten runs). [later] [wiki: arxiv-1904.01954](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1904.01954/article.md)
9. <a id="ref-9"></a>Miyajima, C., Tokuda, K., Kitamura, T. “Audio-visual speech recognition using MCE-based HMMs and model-dependent stream weights.” *Proc. 6th International Conference on Spoken Language Processing (ICSLP 2000)*, 2000. doi:[10.21437/ICSLP.2000-446](https://doi.org/10.21437/ICSLP.2000-446). Prior; deciding prior for M12 (speaker-independent isolated words). [wiki: isca-miyajima00_icslp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-miyajima00_icslp/article.md)
