# Lipreading using Convolutional Neural Network

Noda, K., Yamaguchi, Y., Nakadai, K., Okuno, H. G., Ogata, T. · Interspeech 2014 · 2014 · [DOI:10.21437/Interspeech.2014-293](https://doi.org/10.21437/Interspeech.2014-293)

## Verdict

The paper [[1]](#ref-1) changes the visual front end (M06): a CNN on mouth images emits 40 phoneme posteriors for a GMM-HMM. No CNN appears among the 110 prior lip-reading decoders (pattern match, Appendix), but a shared-weight network on lip pixels [[2]](#ref-2), network phoneme posteriors in HMMs [[3]](#ref-3) and learned mouth features [[4]](#ref-4) came first; only spatial convolution is new. M06 is standard: the word gain over PCA is one unrepeated comparison (Sec. 6.3). Evaluation (M12) is behind because the CNN was trained on image sequences from all 300 words (Sec. 4), so the 84 test words are unseen only by the HMM, whereas the best comparable prior fits every stage on training data [[2]](#ref-2); the authors' "closed-speaker" test (Sec. 6.3) was common then [[5]](#ref-5). The strongest confound follows: only the CNN was fitted, with labels, on test-word frames, so exposure and supervision both favour it over unsupervised PCA.

## Against the field, component by component

### M06 Visual front end: CNN phoneme posteriors into a GMM-HMM

**Usual approach:** Of the 110 prior lip-reading decoders (mention counts, pattern match, Appendix), 80 name both an HMM and hand-crafted appearance or shape features (DCT, PCA, AAM); 20 name a neural network with phonetic or viseme units, 1 learned deep features [[4]](#ref-4) and 0 a CNN. The paper keeps the HMM.

**State of the art:** SyncVSR (2024) reaches 93.2% top-1 on LRW (visual only, no word boundaries, mean of three runs), trained on 157 h of LRW video with vq-wav2vec audio tokens as targets [[6]](#ref-6) [later]. The paper's best is about 37% on 84 test words unseen by the HMM, seen speakers (Sec. 6.3); the tasks differ, so no gap can be read off (inference).

Duchnowski et al. fed 384-dimensional lip-pixel vectors to an MS-TDNN, a temporal shared-weight convolution [[2]](#ref-2); Heckmann et al. decoded ANN phoneme posteriors from chroma-keyed lip parameters [[3]](#ref-3); Ngiam et al. learned features from PCA-whitened mouth regions [[4]](#ref-4). Huang and Kingsbury (ICASSP 2013) used DBNs for audio-visual recognition, as the authors' journal version cites [[7]](#ref-7). What is new is spatial (2-D) convolution: a whole-wiki check finds no earlier CNN on lip images (Appendix), so "remain unaddressed" (Sec. 2) holds for 2-D CNNs only. The missing control existed: one labelled network on 32 PCs against raw pixels gave 52 against 55 and 45 against 44 word accuracy [[2]](#ref-2). 457 of 756 [later] decoders name a CNN (mention counts, Appendix). Fig. 2 repeats the CNN phoneme rate over six speakers; the word comparison has no repeat. Verdict: standard.

### M12 Evaluation: test-word frames inside CNN training

**Usual approach:** Of the same 110 prior decoders (mention counts, pattern match, Appendix), 46 name speaker-independent tests, 28 speaker-dependent tests, 28 a standard deviation, interval or significance test, and 0 a random frame-level split. The paper splits shuffled frames 5/6 to 1/6 (Sec. 5) over all 300 words (Sec. 4).

**State of the art:** On AVLetters2 with one speaker held out per fold, Petridis et al. (2020; arXiv 2019) report 36.8% (SD 2.9, ten runs) visual-only, against 8.3% listed for Cox et al.'s AAM+HMM [[8]](#ref-8) [later].

The best comparable prior is Duchnowski et al.: one speaker, as in the target's per-speaker CNNs, letter sequences split 170/15/15, PCA and LDA "computed using only the training set" [[2]](#ref-2). Ngiam et al. "ensured that no test data was used" for feature learning [[4]](#ref-4); [[3]](#ref-3), [[9]](#ref-9), [[5]](#ref-5) and the target's own reference [[10]](#ref-10) also hold test utterances or speakers out. Here about 5/6 of the test-word frames trained the CNN, and the 58% phoneme rate rests on 100 Hz frames with neighbours in training (inference). Seen speakers are not the defect: that mode "is widely adopted" [[5]](#ref-5), and the authors concede the data are "insufficient to acquire a speaker-independent model" (Sec. 7). The [concurrent] journal version trains the CNN on the 360 training words only, without naming the change, and reaches about 22.5% on 40 test words [[7]](#ref-7) at higher chance; the test sets differ, so this fits a leak without measuring it (inference). Verdict: behind.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Read isolated Japanese ATR words | Read speech | – | standard |
| M02 Training-only supervision | Phoneme labels by audio forced alignment (HTK) | Aligned phonetic labels | – | standard |
| M03 Training and adaptation | Six speaker-specific CNNs; no adaptation | Per-speaker or pooled training | – | standard |
| M04 Use-time action | Pre-segmented isolated words, offline | Isolated or continuous input | – | standard |
| M05 Sensors | One frontal 100 Hz monochrome camera; manual mouth crop | Camera, automatic or manual ROI | – | standard |
| M06 Processing and decoding | CNN phoneme posteriors into a GMM-HMM | HMM with hand-crafted features (pattern match 80) | [[6]](#ref-6) (2024): LRW top-1 93.2%, no word boundaries | standard |
| M07 Lexicon and LM | Closed 84-word lexicon implied; no LM | Word HMMs, no LM | – | standard |
| M08 Output | Isolated word; 40 phoneme posteriors as features | Word classes | – | standard |
| M09 Confirmation | Offline | Offline | – | not applicable |
| M10 Correction | Offline | Offline | – | not applicable |
| M11 Reference construction | Corpus word labels | Corpus references | – | standard |
| M12 Evaluation | Test-word frames in CNN training | Speaker-independent test named (mention count) (pattern match 46) | [[8]](#ref-8) (2019): AVLetters2, speaker held out, 36.8%, ten runs | behind |
| M13 Device and cost | Offline laboratory study, one GPU | Offline | – | not applicable |

## Where the claims outrun the evidence

- **Exposure plus supervision.** Only the CNN saw labels and test-word frames (Sec. 4, Sec. 5); PCA and 6 × 6 did not (Sec. 6.3).
- **"Significantly outperform"** (Abstract; Sec. 7) has no test, interval or repeat (Fig. 5).
- **Untested claims.** Shift- and rotation-resistance (Sec. 1) is untested; mouths are still cropped by hand (Sec. 4).
- **"Reliable information source"** (Sec. 6.3) rests on about 37% words, test words inside CNN training.
- The authors themselves trace weak consonants to labels (Sec. 6.1) and the weaker all-speaker CNN to limited image variation (Sec. 5, footnote 1).

## What the field needs next

- M12: a CNN retrained without test-word frames, utterance-level phoneme splits, repeated runs; then the speaker-independent model the authors propose (Sec. 7).
- M06: a labelled network on PCA inputs under that split, to isolate convolution.
- M02: the better phoneme labelling the authors call for (Sec. 6.1), against audio forced alignment.

## Questions for the authors

- How does word accuracy change with a CNN retrained without the 84 test words?
- Are the Fig. 5 word rates pooled over the six speakers or from one?
- What did the single all-speaker CNN score (Sec. 5, footnote 1)?
- What does a majority-class baseline score on the phoneme test frames?

## Appendix: literature search

Population (one for both topics): lip-reading, VSR or AVSR decoders whose ledger names optical-camera input and whose ledger text or title names the task; versions merged by ledger key and by real title (empty index titles filled from wiki manifests); 95 non-decoders removed by a checked list (perception, neuroimaging, speaker identification, synthesis, tracking, segmentation, voice activity detection, corpora, enhancement, separation, toolboxes, surveys) and 368 by a recognizer-term filter, hand-checked for prior and [concurrent] studies; the same group's journal paper [[7]](#ref-7) added; the target (two wiki folders) excluded. Dating against 2014-09: prior before 2014-03, [concurrent] 2014-03 to 2015-03, [later] after; months from arXiv ids, ICASSP (May) and ISCA venues (September). Result: 110 prior, 11 [concurrent], 756 [later], 3 date unresolved. Design counts are full-text pattern matches with ligatures normalised and reference lists removed; related-work mentions count (upper bounds). Same-group prior on the 216 ATR word corpus line: [[11]](#ref-11).

**M06, lipreading-temporal-model-and-feature-learning** (published table, appended). Inclusion rule: decoders of the population classified by the visual model their full text names: CNN on mouth images, learned deep features, neural network with phonetic or viseme units (TDNN, ANN/HMM), phoneme a posteriori features, hand-crafted features, HMM. Ledger: slot-filled M06 7,345 unique studies; pattern match 975 unique studies. Prior (110): HMM 101, hand-crafted 86, both 80, neural network with phonetic or viseme units 20, learned deep features 1, phoneme a posteriori features 1 [[3]](#ref-3), CNN 0 (one false hit, the CNN news network, removed). [Concurrent] (11): CNN 1 [[7]](#ref-7). [Later] (756): CNN 457, learned deep features 529. Usual design at the time: HMM with hand-crafted features, 80 of 110 (pattern match). Whole-wiki check (743 folders dated 2014 or earlier with lip-reading terms): CNN, only the target. Read: [[2]](#ref-2), [[3]](#ref-3), [[4]](#ref-4), [[7]](#ref-7); state of the art [[6]](#ref-6). Known-item recall 1.0 (published table).

**M12, lipreading-speaker-dependence-protocol** (published table, appended). Inclusion rule: the same population classified by the evaluation partition its full text names: speaker-independent, speaker-dependent, random frame-level split, cross-validation or jackknife, and variability or significance reporting. Ledger: slot-filled M12 6,960 unique studies; pattern match 975 unique studies. Prior (110): speaker-independent 46, speaker-dependent 28, cross-validation or jackknife 27, variability or significance 28, random frame split 0 (the pattern matches the target's and the journal version's split sentences; a broader shuffle or random-split pattern hits 2 prior studies, both utterance-level). [Concurrent] (11): random frame split 1 [[7]](#ref-7). [Later] (756): speaker-independent 249, speaker-dependent 190, variability or significance 270, random frame split 6. Usual design at the time: whole utterances held out; speaker-independent test named in 46 of 110 (pattern match). Read: [[2]](#ref-2), [[4]](#ref-4), [[3]](#ref-3), [[9]](#ref-9), [[5]](#ref-5), [[10]](#ref-10), [[7]](#ref-7); state of the art [[8]](#ref-8). Known-item recall 1.0 (published table).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Noda, K., Yamaguchi, Y., Nakadai, K., Okuno, H. G., Ogata, T. “Lipreading using Convolutional Neural Network.” *Interspeech 2014*, 2014, 1149-1153. doi:[10.21437/Interspeech.2014-293](https://doi.org/10.21437/Interspeech.2014-293). Target. Also held as wiki folder isca-noda14_interspeech. [wiki: isca-noda14-cnnlip](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-noda14-cnnlip/article.md) [wiki: isca-noda14_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-noda14_interspeech/article.md)
2. <a id="ref-2"></a>Duchnowski, P., Meier, U., Waibel, A. “See Me, Hear Me: Integrating Automatic Speech Recognition and Lip-reading.” *Proc. 3rd International Conference on Spoken Language Processing (ICSLP 94)*, 1994. doi:[10.21437/ICSLP.1994-139](https://doi.org/10.21437/ICSLP.1994-139). Prior; deciding prior for M06 (MS-TDNN on lip pixels) and M12 (whole-sequence split with a cross-validation set). [wiki: isca-duchnowski94_icslp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-duchnowski94_icslp/article.md)
3. <a id="ref-3"></a>Heckmann, M., Berthommier, F., Kroschel, K. “A Hybrid ANN/HMM Audio-Visual Speech Recognition System.” *Proc. Auditory-Visual Speech Processing (AVSP 2001)*, 2001. <https://www.isca-archive.org/avsp_2001/heckmann01_avsp.html> Prior; deciding prior for M06 (ANN phoneme posteriors from lip parameters into HMMs) and M12 (utterance-level split). [wiki: isca-heckmann01-annhmm](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-heckmann01-annhmm/article.md)
4. <a id="ref-4"></a>Ngiam, J., Khosla, A., Kim, M., Nam, J., Lee, H., Ng, A. Y. “Multimodal Deep Learning.” *Proceedings of the 28th International Conference on Machine Learning (ICML 2011)*, 2011. <https://ai.stanford.edu/~ang/papers/icml11-MultimodalDeepLearning.pdf> Prior; cited by the target; deciding prior for M06 (learned features from mouth regions) and M12 (speaker-independent CUAVE split). [wiki: w2076462394-ngiamavsr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/w2076462394-ngiamavsr/article.md)
5. <a id="ref-5"></a>Cox, S., Harvey, R., Lan, Y., Newman, J., Theobald, B. “The challenge of multispeaker lip-reading.” *Proc. International Conference on Auditory-Visual Speech Processing (AVSP 2008)*, 2008. <https://www.isca-archive.org/avsp_2008/cox08_avsp.html> Prior; deciding prior for M12 (speaker held out per fold; speaker-independent degradation). [wiki: isca-cox08_avsp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-cox08_avsp/article.md)
6. <a id="ref-6"></a>Ahn, Y. J., Park, J., Park, S., Choi, J., Kim, K. “SyncVSR: Data-Efficient Visual Speech Recognition with End-to-End Crossmodal Audio Token Synchronization.” *Interspeech 2024*, 2024. doi:[10.21437/Interspeech.2024-432](https://doi.org/10.21437/Interspeech.2024-432). arXiv:[2406.12233](https://arxiv.org/abs/2406.12233). State of the art for the M06 visual front end (LRW word accuracy). [later] [wiki: arxiv-2406.12233](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2406.12233/article.md)
7. <a id="ref-7"></a>Noda, K., Yamaguchi, Y., Nakadai, K., Okuno, H. G., Ogata, T. “Audio-visual speech recognition using deep learning.” *Applied Intelligence*, 2015, 42, 722-737. doi:[10.1007/s10489-014-0629-7](https://doi.org/10.1007/s10489-014-0629-7). Same authors; same CNN pipeline with test words excluded from CNN training. Published online 20 December 2014. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/audio-visual-speech-recognition-using-deep-learning) [wiki: doi-10.1007-s10489-014-0629-7](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1007-s10489-014-0629-7/article.md)
8. <a id="ref-8"></a>Petridis, S., Wang, Y., Ma, P., Li, Z., Pantic, M. “End-to-End Visual Speech Recognition for Small-Scale Datasets.” *Pattern Recognition Letters*, 2020. doi:[10.1016/j.patrec.2020.01.022](https://doi.org/10.1016/j.patrec.2020.01.022). arXiv:[1904.01954](https://arxiv.org/abs/1904.01954). Protocol state of the art for M12 (speaker-independent splits, ten runs); arXiv 2019, journal 2020. [later] [wiki: arxiv-1904.01954](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1904.01954/article.md)
9. <a id="ref-9"></a>Miyajima, C., Tokuda, K., Kitamura, T. “Audio-visual speech recognition using MCE-based HMMs and model-dependent stream weights.” *Proc. 6th International Conference on Spoken Language Processing (ICSLP 2000)*, 2000. doi:[10.21437/ICSLP.2000-446](https://doi.org/10.21437/ICSLP.2000-446). Prior; deciding prior for M12 (speaker-independent isolated words). [wiki: isca-miyajima00_icslp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-miyajima00_icslp/article.md)
10. <a id="ref-10"></a>Lan, Y., Theobald, B., Harvey, R., Ong, E., Bowden, R. “Improving Visual Features for Lip-reading.” *Proc. International Conference on Auditory-Visual Speech Processing (AVSP 2010)*, 2010. <https://www.isca-archive.org/avsp_2010/lan10_avsp.html> Prior; cited by the target (its reference 2); speaker held out per fold (M12). [wiki: isca-lan10_avsp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-lan10_avsp/article.md)
11. <a id="ref-11"></a>Yoshida, T., Nakadai, K. “Audio-Visual Speech Recognition System for a Robot.” *Proc. International Conference on Auditory-Visual Speech Processing (AVSP 2010)*, 2010. <https://www.isca-archive.org/avsp_2010/yoshida10_avsp.html> Prior; same group (Nakadai); Japanese word corpus with 216 ATR phonemically balanced words. [wiki: isca-yoshida10_avsp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-yoshida10_avsp/article.md)
