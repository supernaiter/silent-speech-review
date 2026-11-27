# Audio-visual speech recognition using deep learning

Noda, K., Yamaguchi, Y., Nakadai, K., Okuno, H. G., Ogata, T. · Applied Intelligence 42 · 2015 · [DOI:10.1007/s10489-014-0629-7](https://doi.org/10.1007/s10489-014-0629-7)

## Verdict

The paper changes decoding (M06): a denoising autoencoder cleans 11-frame MFCC windows, a per-speaker CNN turns mouth crops into phoneme posteriors, and a multi-stream HMM fuses both with hand-set weights [[1]](#ref-1). The audio denoiser is new to AVSR (0 of 65 prior AVSR studies name a learned denoiser, pattern match, Appendix), but it is shown on one corpus of six male speakers with no per-speaker breakdown or repeated runs, so M06 is standard. The CNN is the authors' own uncited Interspeech 2014 design, three months older [[2]](#ref-2), and multi-stream HMM fusion was the usual design (29 of 65, Appendix). Evaluation (M12) is behind: stream weights and autoencoder depth are chosen on the test words, whereas read priors tuned weights on held-out data and tested unseen speakers [[3]](#ref-3), [[4]](#ref-4). The "additional 10 %" gain at 0 dB (Sec. 6.5) is a best-of-11 upper bound from one run.

## Against the field, component by component

### M06 Audio front end: denoising autoencoder on MFCC windows

**Usual approach:** Of 65 AVSR studies first public before 2014-06 (pattern match, Appendix), 33 name MFCC or filterbank features, 9 any audio enhancement and 0 a learned denoiser. The paper inserts a five-hidden-layer autoencoder between MFCCs and the HMM (Sec. 5.1).

**State of the art:** Robust AVSR now uses no denoiser: LP Conformer (100k h) reaches 1.9% WER on LRS3 sentences with babble at 0 dB, as tabulated in Whisper-Flamingo (2024) [[5]](#ref-5) [later]; that English, speaker-independent sentence test allows no single gap.

The design transfers audio-only denoising the paper cites (its reference 13). The only earlier audio-visual denoising autoencoder in a whole-wiki check (Appendix) [[6]](#ref-6) trains on examples with a single modality as input (Sec. 3.2), not on noisy audio. Training uses 10 dB steps, testing 5 dB steps (Sec. 5.1, Sec. 6.1). Verdict: standard.

### M06 Visual front end: CNN phoneme posteriors

**Usual approach:** Of 127 prior lip-reading studies with a recognizer (pattern match, Appendix), 102 name an HMM, 87 hand-crafted features, 4 learned deep features and 0 a CNN on mouth images.

**State of the art:** SyncVSR (2024) reaches 93.2% top-1 on the 500-word, speaker-independent LRW test [[7]](#ref-7) [later]; the paper's best visual-only word rate is about 22.5% on 40 unseen words of seen speakers (Sec. 6.4).

The departure belongs to [[2]](#ref-2), three months earlier and the only hit of a whole-wiki CNN-lipreading check (Appendix): same authors, six male ATR speakers, one CNN per speaker, 6 × 6 and PCA baselines. It reports 58% phoneme and about 37% word recognition (84 test words); this paper reports 45.87% phonemes at 32 × 32 (Table 4) and about 22.5% words, unexplained. Verdict: standard.

### M06 Fusion: multi-stream HMM with swept weights

**Usual approach:** Of 65 prior AVSR studies (pattern match, Appendix), 29 name multi-stream or coupled HMMs, 23 feature concatenation and 9 automatic or trained stream weights.

**State of the art:** With babble at 0 dB on LRS3, VIT 3D falls from 6.1% WER audio-only to 2.9% audio-visual, as tabulated in Whisper-Flamingo (2024) [[5]](#ref-5), a 52% relative reduction (inference).

The sweep is the group's: Yoshida and Nakadai swept from 0 to 1 at 0.1 intervals, then fitted linear regressions of the optimal weight on SNR [[8]](#ref-8) (Sec. 3.2, Fig. 1). The paper drops the regression, so its "adaptively switching" (Sec. 8) has no test-time rule, as the authors concede (Sec. 7.2). Verdict: standard.

### M12 Evaluation: test-set selection, seen speakers, Gaussian noise

**Usual approach:** Of 65 prior AVSR studies (pattern match, Appendix), 46 test noise at stated SNRs, 23 babble or recorded noise, 24 white or Gaussian noise, 11 report run variability and 9 name a held-out set. The paper uses Gaussian noise, the training speakers ("closed-speaker", Sec. 6.1) and one run.

**State of the art:** USR 2.0 (2026) reports AVSR WER as mean and SD over three random seeds [[9]](#ref-9) [later].

Against best comparable work, three read priors do what the paper does not. Papandreou et al. search the audio weight between 0.0 and 1.0 in steps of 0.1, the paper's grid (Sec. 5.3), on a reserved speaker group, with NOISEX babble and held-out speakers [[3]](#ref-3); Potamianos and Neti set the exponent on a held-out set and test babble [[4]](#ref-4); Miyajima et al. train weights by GPD and test held-out speakers by jackknife [[10]](#ref-10). Verdict: behind.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Read isolated Japanese ATR words | Read speech | – | standard |
| M02 Training-only supervision | Phoneme labels by audio forced alignment | Corpus or aligned labels | – | standard |
| M03 Training and adaptation | Per-speaker CNNs; no adaptation | Per-speaker or pooled training | – | standard |
| M04 Use-time action | Pre-segmented isolated words, offline | Isolated or continuous input | – | standard |
| M05 Sensors | One frontal monochrome camera, one microphone | Camera and microphone | – | standard |
| M06 Processing and decoding | Denoising autoencoder, per-speaker CNN, multi-stream HMM | MFCC or filterbank without learned denoiser (pattern match 33) | [[5]](#ref-5) (2024): LRS3 AVSR WER 1.9%, babble 0 dB | standard |
| M07 Lexicon and LM | No LM or grammar reported | No LM | – | standard |
| M08 Output | Isolated word, 400-word vocabulary | Word classes | – | standard |
| M09 Confirmation | Offline | Offline | – | not applicable |
| M10 Correction | Offline | Offline | – | not applicable |
| M11 Reference construction | Corpus word labels | Corpus references | – | standard |
| M12 Evaluation | Gaussian noise, seen speakers, test-set tuning | Additive noise at stated SNRs, no run variability (pattern match 46) | [[9]](#ref-9) (2026): three seeds, mean and SD | behind |
| M13 Device and cost | Offline laboratory study | Offline | – | not applicable |

## Where the claims outrun the evidence

- **Priority.** "Applications to lipreading remains unaddressed" (Sec. 2.2) is contradicted by [[2]](#ref-2), absent from the 52-item reference list and the only earlier CNN lipreading hit (Appendix).
- **Test-set selection.** The fusion result is the best over "all stream weight pairs" (Sec. 5.3); five hidden layers won on the same curves (Sec. 6.1).
- **Baselines.** Internal only (Sec. 6.4); no DNN-HMM, which the authors call advantageous (Sec. 7.3).
- **Inconsistencies.** 24000 recordings for 400 words × 6 speakers (Sec. 4); "216 training words" (Sec. 5.2) against 360 elsewhere.

## What the field needs next

- M06: the denoiser against noise-augmented HMM training and a DNN-HMM, with babble and recorded noise.
- M06: weights predicted from estimated SNR at test time, as in [[8]](#ref-8).
- M12: a development split for weights and depth, held-out speakers, repeated runs.

## Questions for the authors

- Are the 10% and 65% gains absolute or relative, and at which SNR?
- Is the denoiser applied to noisy test features in Sec. 6.5?
- Why are visual rates below the 2014 paper's?

## Appendix: literature search

Dating against the target's first public month 2014-12: prior before 2014-06, [concurrent] 2014-06 to 2015-06, [later] after 2015-06; months from arXiv ids, ICASSP (May) and ISCA venues (September). Versions count once by ledger key; the target is excluded. Design counts are full-text pattern matches with reference lists removed; related-work mentions count, so they are upper bounds.

**M06, avsr-audio-feature-denoising.** Inclusion rule: studies whose ledger names AVSR, classified by whether their full text names a learned audio denoiser (denoising autoencoder or neural enhancement), any audio enhancement, and MFCC or filterbank features. Ledger: slot-filled M06 7,345 unique studies; pattern match 349 unique studies. Prior (65): MFCC or filterbank 33, any enhancement 9, learned denoiser 0, denoising autoencoder 0. [Concurrent] (5): learned denoiser 0. [Later] (274): denoising autoencoder 4, learned denoiser 12. Usual design at the time: MFCC or filterbank features without a learned denoiser, 33 of 65 (pattern match). Whole-wiki check (1,349 folders dated 2014 or earlier): denoising autoencoder with audio-visual terms, 1 hit [[6]](#ref-6), read. State of the art [[5]](#ref-5). Known-item recall 0.8 (4 of 5).

**M06, lipreading-temporal-model-and-feature-learning** (published table, appended). Inclusion rule: automatic lip-reading, VSR or AVSR studies with optical-camera input, classified by the visual model their full text names; studies with no automatic recognizer excluded. Ledger: pattern match 975 unique studies. Prior (127, 64 excluded): HMM 102, hand-crafted features 87, learned deep features 4, CNN 0. [Concurrent] (11): CNN 1 [[2]](#ref-2). [Later] (632): CNN 397. Usual design at the time: HMM classifier, 102 of 127 (pattern match). Whole-wiki check (1,349 folders): CNN with lip-reading terms, 1 hit [[2]](#ref-2), read. State of the art [[7]](#ref-7). Known-item recall 1.0 (9 of 9).

**M06, avsr-stream-fusion-and-weighting.** Inclusion rule: the same 349 AVSR studies, classified by the fusion design their full text names: multi-stream or coupled HMM with stream weights, automatic or trained weights, feature concatenation, deep multimodal fusion. Prior (65): multi-stream HMM 29, concatenation 23, automatic weights 9, deep fusion 0. [Concurrent] (5): deep fusion 1. [Later] (274): concatenation 92, multi-stream HMM 29, deep fusion 26. Usual design at the time: multi-stream HMM, 29 of 65 (pattern match). Read: [[8]](#ref-8), [[10]](#ref-10), [[4]](#ref-4), [[3]](#ref-3); state of the art [[5]](#ref-5). Known-item recall 1.0 (7 of 7).

**M12, avsr-noise-and-run-variability-protocol** (published table, appended). Inclusion rule: the same 349 AVSR studies, classified by evaluation protocol: additive noise at stated SNRs, babble or recorded noise, white or Gaussian noise, run variability, named held-out set. Prior (65): stated SNR 46, babble or recorded 23, Gaussian 24, variability 11, held-out set 9. Usual design at the time: additive noise at stated SNRs without run variability, 46 of 65 (pattern match). Read: [[3]](#ref-3), [[4]](#ref-4), [[10]](#ref-10); state of the art [[9]](#ref-9). Known-item recall 1.0 (4 of 4).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Noda, K., Yamaguchi, Y., Nakadai, K., Okuno, H. G., Ogata, T. “Audio-visual speech recognition using deep learning.” *Applied Intelligence*, 2015, 42, 722-737. doi:[10.1007/s10489-014-0629-7](https://doi.org/10.1007/s10489-014-0629-7). Target. Published online 20 December 2014. [wiki: doi-10.1007-s10489-014-0629-7](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1007-s10489-014-0629-7/article.md)
2. <a id="ref-2"></a>Noda, K., Yamaguchi, Y., Nakadai, K., Okuno, H. G., Ogata, T. “Lipreading using Convolutional Neural Network.” *Interspeech 2014*, 2014. doi:[10.21437/Interspeech.2014-293](https://doi.org/10.21437/Interspeech.2014-293). Same authors; published three months before the target; not in the target's reference list. Same paper also held as wiki folder isca-noda14_interspeech. [concurrent] [wiki: isca-noda14-cnnlip](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-noda14-cnnlip/article.md) [wiki: isca-noda14_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-noda14_interspeech/article.md)
3. <a id="ref-3"></a>Papandreou, G., Katsamanis, A., Pitsikalis, V., Maragos, P. “Adaptive Multimodal Fusion by Uncertainty Compensation With Application to Audiovisual Speech Recognition.” *IEEE Transactions on Audio, Speech, and Language Processing*, 2009, 17(3). doi:[10.1109/TASL.2008.2011515](https://doi.org/10.1109/TASL.2008.2011515). Prior; deciding prior for M12 (weights grid-searched on a reserved speaker group, NOISEX babble, held-out speakers). [wiki: doi-10.1109-tasl.2008.2011515](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tasl.2008.2011515/article.md)
4. <a id="ref-4"></a>Potamianos, G., Neti, C. “Audio-Visual Speech Recognition in Challenging Environments.” *Proc. 8th European Conference on Speech Communication and Technology (Eurospeech 2003)*, 2003. doi:[10.21437/Eurospeech.2003-1026](https://doi.org/10.21437/Eurospeech.2003-1026). Prior; deciding prior for M12 (stream exponent on a held-out set, babble noise). [wiki: isca-potamianos03_eurospeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-potamianos03_eurospeech/article.md)
5. <a id="ref-5"></a>Rouditchenko, A., Gong, Y., Thomas, S., Karlinsky, L., Kuehne, H., Feris, R., et al. “Whisper-Flamingo: Integrating Visual Features into Whisper for Audio-Visual Speech Recognition and Translation.” *Interspeech 2024*, 2024. arXiv:[2406.10082](https://arxiv.org/abs/2406.10082). Tabulates noisy LRS3 results (Table 3); state of the art for the M06 audio front end and fusion. [later] [wiki: arxiv-2406.10082](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2406.10082/article.md) [wiki: isca-rouditchenko24-whisperflamingo](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-rouditchenko24-whisperflamingo/article.md) [wiki: in24-whisperflamingo](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/in24-whisperflamingo/article.md) [wiki: isca-rouditchenko24_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-rouditchenko24_interspeech/article.md)
6. <a id="ref-6"></a>Ngiam, J., Khosla, A., Kim, M., Nam, J., Lee, H., Ng, A. Y. “Multimodal Deep Learning.” *Proceedings of the 28th International Conference on Machine Learning (ICML 2011)*, 2011. doi:[10.5555/3104482.3104569](https://doi.org/10.5555/3104482.3104569). Prior; cited by the target; deciding prior for the M06 audio denoiser and deep fusion. [wiki: w2076462394-ngiamavsr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/w2076462394-ngiamavsr/article.md)
7. <a id="ref-7"></a>Ahn, Y. J., Park, J., Park, S., Choi, J., Kim, K. “SyncVSR: Data-Efficient Visual Speech Recognition with End-to-End Crossmodal Audio Token Synchronization.” *Interspeech 2024*, 2024. arXiv:[2406.12233](https://arxiv.org/abs/2406.12233). State of the art for the M06 visual front end (LRW word accuracy). [later] [wiki: arxiv-2406.12233](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2406.12233/article.md)
8. <a id="ref-8"></a>Yoshida, T., Nakadai, K. “Two-Layered Audio-Visual Integration in Voice Activity Detection and Automatic Speech Recognition for Robots.” *Interspeech 2010*, 2010. doi:[10.21437/Interspeech.2010-716](https://doi.org/10.21437/Interspeech.2010-716). Prior; same group (Nakadai); deciding prior for M06 fusion (stream-weight regression on SNR). [wiki: isca-yoshida10-twolayer](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-yoshida10-twolayer/article.md)
9. <a id="ref-9"></a>Haliassos, A., Mira, R., Petridis, S. “Pay Attention to CTC: Fast and Robust Pseudo-Labelling for Unified Speech Recognition.” *International Conference on Learning Representations (ICLR)*, 2026. arXiv:[2602.19316](https://arxiv.org/abs/2602.19316). Protocol state of the art for M12 (three seeds). [later] [wiki: arxiv-2602.19316](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.19316/article.md)
10. <a id="ref-10"></a>Miyajima, C., Tokuda, K., Kitamura, T. “Audio-visual speech recognition using MCE-based HMMs and model-dependent stream weights.” *Proc. 6th International Conference on Spoken Language Processing (ICSLP 2000)*, 2000. doi:[10.21437/ICSLP.2000-446](https://doi.org/10.21437/ICSLP.2000-446). Prior; deciding prior for M06 and M12 (trained stream weights, speaker-independent jackknife). [wiki: isca-miyajima00_icslp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-miyajima00_icslp/article.md)
