# Discriminative Multi-modality Speech Recognition

Xu, B., Lu, C., Guo, Y., Wang, J. · CVPR 2020 · [doi:10.1109/CVPR42600.2020.01444](https://doi.org/10.1109/CVPR42600.2020.01444) · [arXiv:2005.05592](https://arxiv.org/abs/2005.05592)

## Verdict

AE-MSR [[1]](#ref-1) changes processing (M06): a lip-guided soft-mask enhancer before an audio-visual EleAtt-GRU recogniser, and a pseudo-3D (P3D) front-end; both are standard. Using the video to enhance and then to recognise was done with HMMs in 2002 and 2013 [[2]](#ref-2), [[3]](#ref-3), and the enhancer is the soft-mask network of [[4]](#ref-4). The second pass gives large LRS3 gains (0 dB: 41.1% to 25.5% WER, Table 3), but each system runs once, the audio-visual baseline is trained on clean magnitudes (§4.3), and several baseline cells are published values [[5]](#ref-5) from more data and other babble. The LRW claim survives the omitted prior results only narrowly (84.8% against 84.07% [[6]](#ref-6)), and [concurrent] work reports 85.3% [[7]](#ref-7). That EleAtt-GRU beats the Transformer is not tested, because front-end, data and decoder change together.

## Against the field, component by component

### M06 Processing: lip-guided enhancement before audio-visual recognition

**Usual approach:** Of 84 AVSR decoders public before 2019-11 (pattern match, Appendix), 53 mention MFCC or filterbank input and 17 any audio enhancement; one feeds a visually enhanced signal to an audio-visual recogniser [[3]](#ref-3). Deep LRS2/LRS3 systems fed noisy spectrograms to the fused recogniser [[5]](#ref-5); AE-MSR inserts a separately trained, frozen mask estimator (§3.1, §4.3).

**State of the art:** On LRS3 with 0 dB babble from 30 LRS3 speakers, CMA reaches 4.4% and AV-HuBERT 5.8% audio-visual WER with 1,759 h unlabelled and 433 h labelled data and no enhancer, as tabulated in 2024 by [later] Whisper-Flamingo [[8]](#ref-8), whose noise file differs; AE-MSR's 25.5% (Table 3) is about 21 points higher (inference).

Read precedents: AVCDCN with audio-only and audio-visual decoding on connected digits [[2]](#ref-2), twin-HMM enhancement before a speaker-dependent GRID recogniser [[3]](#ref-3), and an audio-visual enhancer feeding an LSTM phone recogniser [[9]](#ref-9); [concurrent] pipelined separation before AVSR on LRS2 [[10]](#ref-10). AE-MSR adds sentence scale. At 0 dB the second pass takes VA 32.5% to VAV 25.5% (22% relative; Table 3, inference). Deligne et al. state the deciding caveat: after matched retraining, audio-visual ASR without enhancement and with AVCDCN "become very similar" [[2]](#ref-2). AE-MSR's audio-visual baseline rises from 6.8% clean to 32.2% at 10 dB (Table 3), so the gain is not measured against a noise-trained audio-visual model. Verdict: standard.

### M06 Processing: P3D front-end and EleAtt-GRU decoder

**Usual approach:** Of 17 LRW decoders public before 2019-11 (pattern match, Appendix), 13 mention a 3D convolution followed by a ResNet; pseudo-3D appears in 2, neither as the front-end used. AE-MSR uses a 50-layer P3D (§3.1).

**State of the art:** [Later] SyncVSR (2024) reaches 93.2% LRW top-1 without word boundaries (95.0% with), LRW data only, mean of three runs [[11]](#ref-11); AE-MSR's 84.8% (Table 1) is 8.4 points lower (inference).

Table 1 cites 83.0% from 2017 as the state of the art (§5.1), yet 84.07% [[6]](#ref-6) and a boundary-free 15.67% misclassification rate [[12]](#ref-12) came earlier. AE-MSR does not state word-boundary use; 84.8% clears the best boundary-free prior by about half a point in one run (inference). No ablation swaps P3D (§5.1). The EleAtt-GRU claim (§3.2) sets EG-seq2seq (P3D, LRS3 only) against TM-seq2seq values pre-trained on MV-LRS, LRS2 and LRS3 [[5]](#ref-5); the visual-only gap (59.9% to 57.8%, Table 2) mixes front-end, data and decoder. Verdict: standard.

### M12 Evaluation: noisy-test protocol and baselines

**Usual approach:** Of the 84 prior AVSR decoders (pattern match, Appendix), 49 mention stated-SNR tests and 32 babble; 5 mention run variability or significance, 3 on reading, all on small-vocabulary corpora. AE-MSR gives one WER per system at six conditions (§5).

**State of the art:** [Later] USR 2.0 (2026) reports mean and standard deviation over three seeds on LRS3 [[13]](#ref-13).

Seven baseline cells in Tables 2–3 (TM-seq2seq 9.0%, 59.9%, 8.0%, 60.5%, 44.3%; Google 10.4%, 70.3%) equal the no-LM values of [[5]](#ref-5), whose noisy models used 0 dB babble from 20 LRS2 utterances; AE-MSR mixes 30 LRS3 utterances (§4.3), so the 0 dB comparison mixes test noise and training data (inference). The authors note that at -10 dB audio can hurt (§5.1). Verdict: standard (Appendix).

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Voiced TED/BBC video | Voiced speech video | – | standard |
| M02 Training-only supervision | L1 to clean magnitude; character seq2seq | Paired clean audio | – | standard |
| M03 Training and adaptation | Frozen LRW front-end; babble p = 0.25; curriculum | Supervised, babble-augmented | – | standard |
| M04 Use-time action | Noisy voiced speech, lip video | Overt speech | – | standard |
| M05 Sensors | 16 kHz audio; 112x112 mouth, 25 fps | Mic plus camera | – | standard |
| M06 Processing and decoding | Lip-guided mask enhancer before AV EleAtt-GRU; P3D front-end | No enhancer; MFCC or filterbank, mentions of 84 prior AVSR (pattern match 53) | [[8]](#ref-8) (2024): 4.4% AV WER, LRS3 0 dB babble | standard |
| M07 Lexicon and LM | No external LM (Table 2) | No LM | – | standard |
| M08 Output | 41 characters; 500 LRW words | Characters | – | standard |
| M09 Confirmation | None | Offline | – | not applicable |
| M10 Correction | None | Offline | – | not applicable |
| M11 Reference construction | LRS3, LRW splits; test partition not stated | Benchmark splits | – | not reported |
| M12 Evaluation | One run, six conditions; copied baseline cells | Stated-SNR test, mentions of 84 prior AVSR (pattern match 49) | [[13]](#ref-13) (2026): three seeds | standard |
| M13 Device and cost | 1 GPU, 15 days; no inference cost | Training cost only | – | standard |

## Where the claims outrun the evidence

- "More advantageous in terms of robustness and accuracy" than single visual awareness (§1): the double use predates it [[2]](#ref-2), [[3]](#ref-3), and no noise-trained audio-visual baseline is run (M06).
- "Ablation study ... demonstrates the effectiveness of each of the above sub-modules" (§1): only the enhancer block and VA/VAV vary (Tables 3–4); P3D and EleAtt-GRU are not ablated.
- "Consistently achieves the state-of-the-art performance by a significant margin" (Abstract): Table 2 and Table 3 give no test or variability.
- Clean rows are empty for enhanced systems (Table 3), so the enhancer's clean-audio cost is unknown.

## What the field needs next

- M06: add the enhancer to an audio-visual model trained on the same noise, clean rows included.
- M06: swap P3D for a 3D-convolution ResNet in one LRW pipeline, three or more seeds.
- M12: re-run all baselines under one released noise file and report seed variability.

## Questions for the authors

- Which LRS3 partition gives Tables 2–4?
- Was the single-awareness audio-visual model trained on noisy audio?
- Which TM-seq2seq cells were re-run, and with which test noise?
- Does the LRW model use word boundaries?
- Is Table 3 decoded with beam search or a language model?

## Appendix: literature search

- Shared population for all topics. Inclusion rule: lip-reading, VSR and AVSR decoders named in title or ledger; surveys, datasets, perception, neuroimaging, education, enhancement- or separation-only, synthesis, talking-head, forgery, synchronisation and keyword-spotting studies removed by title and on reading; versions merged; target excluded. Dated by first public month against 2020-05: prior before 2019-11, [concurrent] 2019-11 to 2020-11. 606 unique studies: prior 194, [concurrent] 27, date unresolved 4, [later] 381. All design counts below are full-text mention counts (pattern match, reference lists removed, upper bounds) with their denominators.
- M06, avsr-audio-feature-denoising (published table, reused). Inclusion rule: AVSR decoders of the shared population, classified by MFCC or filterbank input, any audio enhancement, learned audio-only denoisers and audio-visual enhancement or separation, then on reading for a visually guided enhancer feeding an audio-visual recogniser. Ledger: 7,345 unique studies slot-filled for M06, 349 pattern match (published); this review 254 AVSR decoders (prior 84, [concurrent] 9, [later] 161). Prior counts of 84: MFCC or filterbank 53, any audio enhancement 17, learned audio-only denoiser 4, audio-visual enhancement or separation 3 (1 design on reading, [[3]](#ref-3)). Outside the population, enhancement-titled with a recogniser: [[2]](#ref-2), [[9]](#ref-9), [[4]](#ref-4). [Concurrent] 9: separation front-end then recogniser 2 ([[10]](#ref-10) and its multi-channel sequel). Read in full: [[2]](#ref-2), [[3]](#ref-3), [[9]](#ref-9), [[4]](#ref-4), [[5]](#ref-5), [[8]](#ref-8). Known-item recall 0.8 (published); 1.0 for this review (4 seeds).
- M06, word-lipreading-visual-frontend (published table, reused). Inclusion rule: LRW and LRW-1000 word-level decoders of the shared population, classified by 3D convolution, ResNet, both, I3D or two-stream, pseudo-3D or factorised 3D convolution, and TCN back-end; pseudo-3D hits read. Ledger: 156 unique studies pattern match (published); this review 99 LRW decoders (prior 17, [concurrent] 12, date unresolved 1, [later] 69). Prior counts of 17: 3D convolution and ResNet 13, I3D or two-stream 6, pseudo-3D 2 (0 as the front-end used). [Concurrent] 12: 3D convolution and ResNet 10, TCN back-end 5, pseudo-3D 1 (citation). Read in full: [[6]](#ref-6), [[12]](#ref-12), [[7]](#ref-7), [[11]](#ref-11). Known-item recall 1.0 (published and this review, 6 seeds).
- M12, avsr-noise-and-run-variability-protocol (published table, reused). Inclusion rule: the same 254 AVSR decoders, classified by stated-SNR tests, babble noise, SNRs at or below -5 dB, a language-model statement and run variability or significance; variability hits read. Ledger: 6,960 unique studies slot-filled for M12, 349 pattern match (published). Prior counts of 84: stated SNR 49, babble 32, SNR at or below -5 dB 17, language model 15, run variability or significance 5 (3 on reading). [Concurrent] 9: run variability 4 (3 on reading). Read in full: [[5]](#ref-5), [[3]](#ref-3), [[13]](#ref-13). Known-item recall 1.0 (published).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Xu, B., Lu, C., Guo, Y., Wang, J. “Discriminative Multi-modality Speech Recognition.” *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2020, 14433-14442. doi:[10.1109/CVPR42600.2020.01444](https://doi.org/10.1109/CVPR42600.2020.01444). arXiv:[2005.05592](https://arxiv.org/abs/2005.05592). Target. Read as the CVF Open Access version (same text as arXiv v1). [wiki: cvf-xu20-aemsr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-xu20-aemsr/article.md) [wiki: cvf-xu20-msr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-xu20-msr/article.md)
2. <a id="ref-2"></a>Deligne, S., Potamianos, G., Neti, C. “Audio-Visual Speech Enhancement with AVCDCN (Audio-Visual Codebook Dependent Cepstral Normalization).” *Proc. 7th International Conference on Spoken Language Processing (ICSLP 2002)*, 2002. doi:[10.21437/ICSLP.2002-421](https://doi.org/10.21437/ICSLP.2002-421). Prior; deciding prior for M06 (audio-visual enhancement with audio-only and audio-visual recognisers). Not cited by the target. [wiki: isca-deligne02_icslp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-deligne02_icslp/article.md)
3. <a id="ref-3"></a>Abdelaziz, A. H., Zeiler, S., Kolossa, D. “Using Twin-HMM-Based Audio-Visual Speech Enhancement as a Front-End for Robust Audio-Visual Speech Recognition.” *Interspeech 2013*, 2013, 867-871. doi:[10.21437/Interspeech.2013-257](https://doi.org/10.21437/Interspeech.2013-257). Prior; deciding prior for M06 (audio-visual enhancement front-end for an audio-visual recogniser). Not cited by the target. [wiki: isca-abdelaziz13-twinhmm](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-abdelaziz13-twinhmm/article.md) [wiki: isca-abdelaziz13_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-abdelaziz13_interspeech/article.md)
4. <a id="ref-4"></a>Afouras, T., Chung, J. S., Zisserman, A. “The Conversation: Deep Audio-Visual Speech Enhancement.” *Interspeech 2018*, 2018. doi:[10.21437/Interspeech.2018-1400](https://doi.org/10.21437/Interspeech.2018-1400). arXiv:[1804.04121](https://arxiv.org/abs/1804.04121). Prior; source of the 1D-ResNet soft-mask enhancer (M06), cited by the target as [3]. [wiki: arxiv-1804.04121](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1804.04121/article.md) [wiki: isca-afouras18-conversation](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-afouras18-conversation/article.md)
5. <a id="ref-5"></a>Afouras, T., Chung, J. S., Senior, A., Vinyals, O., Zisserman, A. “Deep Audio-Visual Speech Recognition.” *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 2018. doi:[10.1109/TPAMI.2018.2889052](https://doi.org/10.1109/TPAMI.2018.2889052). arXiv:[1809.02108](https://arxiv.org/abs/1809.02108). Prior; TM-seq2seq baseline whose Table 2 values reappear in the target's Tables 2-3 (M06, M12). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/deep-audio-visual-speech-recognition) [wiki: arxiv-1809.02108](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1809.02108/article.md) [wiki: doi-10.1109-tpami.2018.2889052](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tpami.2018.2889052/article.md)
6. <a id="ref-6"></a>Weng, X., Kitani, K. “Learning Spatio-Temporal Features with Two-Stream Deep 3D CNNs for Lipreading.” *British Machine Vision Conference (BMVC)*, 2019. arXiv:[1905.02540](https://arxiv.org/abs/1905.02540). Prior; higher LRW result than the target's cited state of the art (M06). [wiki: arxiv-1905.02540](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1905.02540/article.md)
7. <a id="ref-7"></a>Martinez, B., Ma, P., Petridis, S., Pantic, M. “Lipreading using Temporal Convolutional Networks.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2020. arXiv:[2001.08702](https://arxiv.org/abs/2001.08702). [concurrent]; LRW result above the target (M06). [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lipreading-using-temporal-convolutional-networks) [wiki: arxiv-2001.08702](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2001.08702/article.md)
8. <a id="ref-8"></a>Rouditchenko, A., Gong, Y., Thomas, S., Karlinsky, L., Kuehne, H., Feris, R., et al. “Whisper-Flamingo: Integrating Visual Features into Whisper for Audio-Visual Speech Recognition and Translation.” *Interspeech 2024*, 2024. arXiv:[2406.10082](https://arxiv.org/abs/2406.10082). [later]; tabulates noisy LRS3 AVSR results (Table 3); state of the art for M06. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/whisper-flamingo-integrating-visual-features-into-whisper-for-audio-visual-speech-recognition-and-tr) [wiki: arxiv-2406.10082](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2406.10082/article.md) [wiki: isca-rouditchenko24-whisperflamingo](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-rouditchenko24-whisperflamingo/article.md) [wiki: in24-whisperflamingo](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/in24-whisperflamingo/article.md) [wiki: isca-rouditchenko24_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-rouditchenko24_interspeech/article.md)
9. <a id="ref-9"></a>Pasa, L., Morrone, G., Badino, L. “An Analysis of Speech Enhancement and Recognition Losses in Limited Resources Multi-Talker Single Channel Audio-Visual ASR.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2020. doi:[10.1109/ICASSP40776.2020.9053532](https://doi.org/10.1109/ICASSP40776.2020.9053532). arXiv:[1904.08248](https://arxiv.org/abs/1904.08248). Prior; deep audio-visual enhancement feeding a phone recogniser (M06). [wiki: arxiv-1904.08248](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1904.08248/article.md)
10. <a id="ref-10"></a>Yu, J., Zhang, S., Wu, J., Ghorbani, S., Wu, B., Kang, S., et al. “Audio-Visual Recognition of Overlapped Speech for the LRS2 Dataset.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2020. doi:[10.1109/ICASSP40776.2020.9054083](https://doi.org/10.1109/ICASSP40776.2020.9054083). arXiv:[2001.01656](https://arxiv.org/abs/2001.01656). [concurrent]; integrated AVSR against a pipelined separation-plus-recognition system (M06). [concurrent] [wiki: arxiv-2001.01656](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2001.01656/article.md)
11. <a id="ref-11"></a>Ahn, Y. J., Park, J., Park, S., Choi, J., Kim, K. “SyncVSR: Data-Efficient Visual Speech Recognition with End-to-End Crossmodal Audio Token Synchronization.” *Interspeech 2024*, 2024. arXiv:[2406.12233](https://arxiv.org/abs/2406.12233). [later]; state of the art for the LRW front-end (M06). [later] [wiki: arxiv-2406.12233](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2406.12233/article.md)
12. <a id="ref-12"></a>Stafylakis, T., Khan, M. H., Tzimiropoulos, G. “Pushing the boundaries of audiovisual word recognition using Residual Networks and LSTMs.” *Computer Vision and Image Understanding*, 2018. arXiv:[1811.01194](https://arxiv.org/abs/1811.01194). Prior; LRW results with and without word boundaries (M06). [wiki: arxiv-1811.01194](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1811.01194/article.md)
13. <a id="ref-13"></a>Haliassos, A., Mira, R., Petridis, S. “Pay Attention to CTC: Fast and Robust Pseudo-Labelling for Unified Speech Recognition.” *International Conference on Learning Representations (ICLR)*, 2026. arXiv:[2602.19316](https://arxiv.org/abs/2602.19316). [later]; seed-level variability on LRS3 (M12 protocol yardstick). [later] [wiki: arxiv-2602.19316](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.19316/article.md)
