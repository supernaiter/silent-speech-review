# Recurrent Neural Network Transducer for Audio-Visual Speech Recognition

Takaki Makino, Hank Liao, Yannis Assael, Brendan Shillingford, Basilio Garcia, Otavio Braga, Olivier Siohan. ASRU 2019. [doi:10.1109/ASRU46091.2019.9004036](https://doi.org/10.1109/ASRU46091.2019.9004036) [arXiv:1911.04890](https://arxiv.org/abs/1911.04890)

## Verdict

The paper [[1]](#ref-1) changes three components, all standard. M06: it is the first neural transducer for visual or audio-visual speech in the ledger (0 of 123 earlier sentence-level studies, Appendix), and the RNN-T decoder reached 0.9% LRS3 AVSR WER in 2023 [[2]](#ref-2) [later]; but the paper never trains CTC or attention on its own data, as [[3]](#ref-3) did. M02 scales the V2P caption-mining pipeline [[4]](#ref-4) to 31k hours. M03 adds overlapping-speech mixing in training, new among 107 earlier AVSR studies (Appendix), on one run and one test set. The LRS3 claim (Abstract) sets 31k hours against 1.4k and 4k hours (Table 7), so it measures data and decoder together, as the authors say (Sec. 4.5).

## Against the field, component by component

### M06 Processing: transducer decoder and frame-rate alignment

**Usual approach:** Of 123 sentence-level lip-reading and AVSR studies dated before the target, 79 name HMMs, 20 CTC and 16 attention sequence-to-sequence (pattern match, Appendix): CTC with FST decoding [[4]](#ref-4), CTC against seq2seq [[3]](#ref-3), hybrid CTC/attention [[5]](#ref-5), attention [[6]](#ref-6), which lists RNN-T as an option but does not use it. For alignment, 11 of 107 earlier AVSR studies upsample or interpolate video to the audio rate (pattern match), e.g. to 50 fps [[5]](#ref-5); [[3]](#ref-3) fixes video at 25 fps. None keeps the variable rate (Appendix).

**State of the art:** In 2023 an LSTM RNN-T decoder gives 0.9% LRS3 AVSR WER on 100k hours [[2]](#ref-2) [later]; the best value, 0.76% (2024), uses Whisper's attention decoder [[7]](#ref-7) [later], 0.14 points lower (inference) on other data.

The paper defers comparison with attention models (Sec. 6), so the 33.6% LRS3 visual WER is not attributable to the decoder. Variable-rate audio gives 19.8% A/V WER against 20.1% to 20.4% at fixed rates, ±0.5 (Table 4), not significant per the authors (Sec. 4.3): no gain, no cost. Standard.

### M02 Training-only supervision: caption-mined corpus scale

**Usual approach:** Of 361 VSR and AVSR studies dated before the target, 356 name no training corpus of 1,000 hours or more (pattern match, Appendix); the exception, [[4]](#ref-4), has 3,886 hours from the same Liao et al. (2013) pipeline. The target yields 31k hours from 150k hours of audio (Sec. 2), mainly by accepting a greater range of face pan and tilt angles.

**State of the art:** In 2023, 100k hours of transcribed YouTube video give 12.8% LRS3 VSR WER [[2]](#ref-2) [later], against 33.6% here (Table 7).

Sec. 2 calls the corpus 5 times the V2P and 10 times the TM-seq2seq data; Table 7's 4k and 1.4k hours give about 7.8 and 22 times (inference). Data and models are not released (Sec. 5). Standard.

### M03 Training: modality dropout and overlapping-speech augmentation

**Usual approach:** Of 107 AVSR studies dated before the target, 100 name neither noise in training nor modality dropout, and none mixes interfering speech into training audio (pattern match, Appendix); [[3]](#ref-3) adds babble at 0 dB with probability 0.25. The authors credit modality dropout to their reference 32 (Sec. 4.2), outside the wiki.

**State of the art:** In 2023 [[2]](#ref-2) [later] reports 0.9% AVSR WER within a missing-video robustness study (Sec. 5.3).

Overlap mixing cuts A/V WER on competing speech from 37.4% to 25.6% (Tables 5, 6), 32% relative (inference), and at 0 dB babble from 57.4% to 42.3%. Audio dropout lowers visual-only WER from 98.8% to 50.3% but raises audio-only from 24.0% to 46.0% (Table 3); the authors conclude concatenation fusion is not robust (Sec. 4.2). Standard.

### M12 Evaluation: noise protocol and intervals

**Usual approach:** Of 107 AVSR studies before the target, 50 test additive noise at stated SNRs without a variability estimate (pattern match, Appendix); the 9 with one date from 2017 or earlier. The paper adds 95% test-set intervals (Sec. 4), but no seeds or repeated runs.

**State of the art:** LRS3 AVSR WER is 0.76% (2024) [[7]](#ref-7) [later]. Noisy tests here use only the non-public YTD EV18, and Table 7 has no intervals. Standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Voiced speech in public YouTube videos | Voiced speech recorded for training | – | standard |
| M02 Training-only supervision | 31k h YouTube video, ASR-checked captions | No corpus of 1,000 h or more; of 361 studies before 2019-11 (pattern match 356) | [[2]](#ref-2) 100k h, 12.8% LRS3 VSR WER | standard |
| M03 Training and adaptation | Audio dropout; overlapping-speech mixing | No training noise or modality dropout; of 107 AVSR studies before 2019-11 (pattern match 100) | [[2]](#ref-2) 0.9% AVSR WER | standard |
| M04 Use-time action | Voiced speech; noise added at test | Voiced speech at use time | – | standard |
| M05 Sensors | Mouth crops, 23 to 30 fps; 16 kHz audio | Camera mouth region plus microphone | – | standard |
| M06 Processing and decoding | RNN-T; audio shift tied to video frame rate | HMM decoding; of 123 studies before 2019-11 (pattern match 79) | [[2]](#ref-2) RNN-T, 0.9% LRS3 AVSR WER | standard |
| M07 Lexicon and LM | Not stated | LM in decoding varies | – | not reported |
| M08 Output | Characters (75 symbols) | Text output | – | standard |
| M09 Confirmation | None (offline) | Mostly absent | – | not applicable |
| M10 Correction | None (offline) | Mostly absent | – | not applicable |
| M11 Reference construction | Non-public YTD EV18; LRS3-TED test | Public benchmark split | – | standard |
| M12 Evaluation | Babble, competing speech, 95% CIs; one run | Noise at stated SNRs, no variability estimate; of 107 AVSR studies before 2019-11 (pattern match 50) | [[7]](#ref-7) 0.76% LRS3 AVSR WER | standard |
| M13 Device and cost | 128 TPU cores; data and models restricted | Offline GPU or TPU training | – | standard |

## Where the claims outrun the evidence

- "Significantly improves the state-of-the-art on LRS3-TED" (Abstract): 33.6% against 55.1% visual-only is 39% lower (inference), 4.5% against 7.2% A/V 38% lower (inference), with 31k against 4k and 1.4k training hours (Table 7). The authors credit "far more data and a RNN-T model" (Sec. 4.5); neither is isolated.
- The clean A/V gain is small: 20.5% against 21.5% (Table 2, ±0.5) and 4.5% against 4.8% on LRS3 (Table 7). At 0 dB babble A/V (57.4%) is worse than visual-only (48.5%), as the authors report (Sec. 4.4).
- No seeds or repeated runs (Sec. 4); the relation of the selection shard to the 70-hour development set is not stated.

## What the field needs next

- M06: RNN-T, CTC and attention on the same 31k hours and front end, three or more seeds.
- M03: fusion that keeps A/V WER at or below the better single modality at 0 dB, on recorded noisy video.
- M12: noisy tests on a public set with matched training data and intervals.

## Questions for the authors

- Was an external language model used for Table 7?
- How many speakers are in YTD EV18, and do any appear in training?
- How do the factors of 5 and 10 in Sec. 2 relate to Table 7's hours?
- What text normalization precedes WER scoring?

## Appendix: literature search

- M06, sentence-lipreading-sequence-objective (published table, appended). Inclusion rule: studies that decode sentence-level or open-vocabulary speech from lip or face video (lip reading, VSR, AVSR or LRS2/LRS3 with sentence-level recognition), classified by the sequence objective their full text names; a study counts under every objective it names (upper bound); versions once. Ledger counts: 7,345 unique studies slot-filled for M06; 633 unique studies pattern match. Before 2019-11 (123 dated): HMM 79, CTC 20, attention or seq2seq 16, "transducer" 16, none a neural transducer (snippets read: finite-state transducers, ultrasound probes, mentions); 21 studies dated only to 2019 name no RNN-T. All dates: CTC 288, attention or seq2seq 281, HMM 196, transducer 119. Recall check over 2,671 wiki studies dated before 2019-11: 2 RNN-T hits, [[6]](#ref-6) (mention) and an EEG study first public 2019-08 ([concurrent]). Read: [[3]](#ref-3), [[4]](#ref-4), [[6]](#ref-6), [[5]](#ref-5) (prior); [[2]](#ref-2) (state of the art); [[8]](#ref-8) ([later]). Known-item recall 1.0.
- M06, avsr-audio-stream-input-representation (published table, appended). Inclusion rule: studies whose ledger names AVSR, classified by the audio input and audio-video rate alignment their full text names. Ledger counts: 349 unique studies pattern match. Before 2019-11 (107 dated): filterbank or MFCC 67, video upsampled or interpolated 11, variable frame rate 0; all dates: variable frame rate 2 (the target and [[8]](#ref-8)). Known-item recall 0.8.
- M02, asr-transcribed-unlabelled-video-training (published table, appended). Inclusion rule: studies whose ledger names lip reading, VSR or AVSR, classified by training-label source and, here, by a named corpus of 1,000 hours or more. Ledger counts: 31 unique studies slot-filled for M02; 1,049 unique studies pattern match. Before 2019-11 (361 dated): 5 hits for 1,000 hours or more, one a video training corpus ([[4]](#ref-4)); 356 without. All dates: 147. Known-item recall 1.0.
- M03, avsr-self-supervised-and-noise-augmented-training (published table, appended). Inclusion rule: the 349-study AVSR population classified by training regime; here modality dropout, noise added in training and interfering speech added in training. Ledger counts: 1,526 unique studies slot-filled for M03; 349 unique studies pattern match. Before 2019-11 (107 dated): noise in training 7, modality dropout 0, interfering speech in training 0; all dates 82, 31 and 2. Recall check over 2,671 wiki studies before 2019-11: 0 modality-dropout hits. Read: [[3]](#ref-3). Known-item recall 0.5.
- M12, avsr-noise-and-run-variability-protocol (published table, appended). Inclusion rule: the 349-study AVSR population classified by evaluation protocol with the table's published patterns. Ledger counts: 6,960 unique studies slot-filled for M12; 349 unique studies pattern match. Before 2019-11 (107 dated): additive noise at stated SNRs 56, of which 50 without a variability estimate; variability estimate 9; babble 38; interfering speech 10. Read: [[7]](#ref-7) (state of the art). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Makino, T., Liao, H., Assael, Y., Shillingford, B., Garcia, B., Braga, O., et al. “Recurrent Neural Network Transducer for Audio-Visual Speech Recognition.” *IEEE Automatic Speech Recognition and Understanding Workshop (ASRU)*, 2019. doi:[10.1109/ASRU46091.2019.9004036](https://doi.org/10.1109/ASRU46091.2019.9004036). arXiv:[1911.04890](https://arxiv.org/abs/1911.04890). First public as arXiv:1911.04890 (2019-11). [wiki: arxiv-1911.04890](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1911.04890/article.md) [wiki: doi-10.1109-asru46091.2019.9004036](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-asru46091.2019.9004036/article.md)
2. <a id="ref-2"></a>Chang, O., Liao, H., Serdyuk, D., Shah, A., Siohan, O. “Conformers are All You Need for Visual Speech Recognition.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2024, 10136-10140. arXiv:[2302.10915](https://arxiv.org/abs/2302.10915). State of the art for the RNN-T AVSR lineage (M06). [later] [later] [wiki: arxiv-2302.10915](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2302.10915/article.md)
3. <a id="ref-3"></a>Afouras, T., Chung, J. S., Senior, A., Vinyals, O., Zisserman, A. “Deep Audio-Visual Speech Recognition.” *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 2018. doi:[10.1109/TPAMI.2018.2889052](https://doi.org/10.1109/TPAMI.2018.2889052). arXiv:[1809.02108](https://arxiv.org/abs/1809.02108). Prior; deciding prior for M06 (CTC and sequence-to-sequence on one front end; video at 25 fps) and M03 (babble in training). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/deep-audio-visual-speech-recognition) [wiki: arxiv-1809.02108](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1809.02108/article.md) [wiki: doi-10.1109-tpami.2018.2889052](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tpami.2018.2889052/article.md)
4. <a id="ref-4"></a>Shillingford, B., Assael, Y., Hoffman, M. W., Paine, T., Hughes, C., Prabhu, U., et al. “Large-Scale Visual Speech Recognition.” *arXiv preprint*, 2018. arXiv:[1807.05162](https://arxiv.org/abs/1807.05162). Prior; deciding prior for M02 (3,886 h YouTube corpus from the same caption-mining pipeline; CTC with FST decoding). [wiki: arxiv-1807.05162](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1807.05162/article.md) [wiki: isca-shillingford19-largescale](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-shillingford19-largescale/article.md)
5. <a id="ref-5"></a>Petridis, S., Stafylakis, T., Ma, P., Tzimiropoulos, G., Pantic, M. “Audio-Visual Speech Recognition with a Hybrid CTC/Attention Architecture.” *IEEE Spoken Language Technology Workshop (SLT)*, 2018. doi:[10.1109/SLT.2018.8639643](https://doi.org/10.1109/SLT.2018.8639643). arXiv:[1810.00108](https://arxiv.org/abs/1810.00108). Prior; deciding prior for M06 (hybrid CTC/attention AVSR; visual features upsampled to 50 fps). [wiki: arxiv-1810.00108](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1810.00108/article.md) [wiki: doi-10.1109-slt.2018.8639643](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-slt.2018.8639643/article.md)
6. <a id="ref-6"></a>Zhou, P., Yang, W., Chen, W., Wang, Y., Jia, J. “Modality Attention for End-to-End Audio-Visual Speech Recognition.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2019. arXiv:[1811.05250](https://arxiv.org/abs/1811.05250). Prior; deciding prior for M06 (names RNN-T as one of three end-to-end approaches, uses attention). [wiki: arxiv-1811.05250](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1811.05250/article.md)
7. <a id="ref-7"></a>Rouditchenko, A., Gong, Y., Thomas, S., Karlinsky, L., Kuehne, H., Feris, R., et al. “Whisper-Flamingo: Integrating Visual Features into Whisper for Audio-Visual Speech Recognition and Translation.” *Interspeech 2024*, 2024. arXiv:[2406.10082](https://arxiv.org/abs/2406.10082). LRS3 AVSR state of the art (M12). [later] [later] [wiki: arxiv-2406.10082](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2406.10082/article.md) [wiki: isca-rouditchenko24-whisperflamingo](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-rouditchenko24-whisperflamingo/article.md) [wiki: in24-whisperflamingo](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/in24-whisperflamingo/article.md) [wiki: isca-rouditchenko24_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-rouditchenko24_interspeech/article.md)
8. <a id="ref-8"></a>Sterpu, G., Harte, N. “AV Taris: Online Audio-Visual Speech Recognition.” *arXiv preprint*, 2020. arXiv:[2012.07467](https://arxiv.org/abs/2012.07467). Discusses the target's variable-rate audio features and RNN-T training difficulty (M06). [later] [later] [wiki: arxiv-2012.07467](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2012.07467/article.md)
