# LiRA: Learning Visual Speech Representations from Audio through Self-supervision

Pingchuan Ma, Rodrigo Mira, Stavros Petridis, Björn W. Schuller, Maja Pantic. Interspeech 2021. [doi:10.21437/Interspeech.2021-1360](https://doi.org/10.21437/Interspeech.2021-1360) · [arXiv:2106.09171](https://arxiv.org/abs/2106.09171)

## Verdict

LiRA [[1]](#ref-1) changes the training-only supervision (M02), regressing frozen PASE+ features instead of distilling a recognizer, and the pre-training objective (M03), regression instead of contrastive learning; both stay standard. Pre-training helps strongly at 1% of LRW labels (24.5% against 3.6%, Sec. 4.1), but with all labels adds 0.7 points on LRW (88.1% against 87.4%, Table 1) and 0.3 on LRS2 (38.8% against 39.1%, Table 2), one run each. The same encoder from scratch already beats every self-supervised row in Table 1, and most of the 9.5-point LRS2 gain over TM-seq2seq was reported by the authors' [concurrent] Conformer paper [[2]](#ref-2). PASE+ is preferred on an MFCC remark without numbers (Sec. 2.1), and LipSound [[3]](#ref-3), which regressed mel spectrograms from lip video in 2019, is not cited.

## Against the field, component by component

### M02 Training-only supervision: audio-derived target

**Usual approach:** 2 of the 3 prior studies that feed audio into a video-only lip reader (pattern match, screened, Appendix) distil a supervised recognizer: LIBS [[4]](#ref-4), with ground-truth sentences in the loop, and Afouras et al. [[5]](#ref-5), on unlabelled VoxCeleb2. LipSound [[3]](#ref-3) regresses mel spectrograms without transcripts. LiRA's teacher is a self-supervised acoustic encoder, so no labelled audio enters pre-training.

**State of the art:** SyncVSR (2024) [[6]](#ref-6) [later] predicts audio tokens from video and reaches 93.2% on LRW (no word boundary, LRW data only, three seeds), 5.1 points above LiRA's single-run 88.1% (inference).

The authors credit Afouras et al. and name what they avoid, an ASR "trained on large amounts of labelled data" (Sec. 1). The effect of that departure is not measured: no row compares PASE+ with recognizer or spectrogram targets on one encoder (Sec. 2.1, Tables 1 to 2). KD-seq2seq's 51.3% [[5]](#ref-5) uses a Jasper-style network, a word-level-pretrained front end and a 6-gram LM, so it is no yardstick for LiRA's Conformer, hybrid CTC/attention and Transformer LM (Sec. 3.5). LipSound's GRID results are speaker-dependent, but the design predates LiRA. Of 3 [concurrent] studies, 2 distil and LipSound2 [[7]](#ref-7) pre-trains video-to-mel on about 2,400 h. Standard: the target is new among the 3 priors (Appendix), but nothing separates it from the backbone.

### M03 Training: pre-training objective and transfer

**Usual approach:** Of 3 prior visual-speech pre-training studies (pattern match, screened, Appendix), 2 learn contrastive or synchronisation embeddings [[8]](#ref-8) [[9]](#ref-9) and 1 distils an ASR teacher [[5]](#ref-5); AV-PPC, in the target's Table 1, is also contrastive.

**State of the art:** RAVEn (2023) [[10]](#ref-10) [later] reaches 23.2% LRS2 WER (1,759 h unlabelled, 223 h labelled, no LM), 15.6 points below LiRA's 38.8% with an LM (inference).

LiRA-Supervised, with no pre-training, reaches 87.4%, 2.6 points above AV-PPC's 84.8%, the best other self-supervised row (inference); LiRA-Frozen, the row that tests the representation, gives 83.1%. "Significantly outperforms other self-supervised methods" thus holds for the system, not the objective. On LRS2 the authors call the gain over curriculum learning "a small improvement" (Sec. 4.2), 0.8% relative (inference), and the 9.5 points over TM-seq2seq repeat the 9.2 (48.3% to 39.1%) of the followed recipe [[2]](#ref-2) (inference). Label efficiency is the real result: a 20.9-point gap at 1% of LRW labels (inference). Standard: confounded by the backbone, one run per point.

### M12 Evaluation: single-run benchmark claims

**Usual approach:** None of the 30 prior LRW systems with full text reports a run spread (pattern match, 8 hits inspected, Appendix); LiRA follows this.

**State of the art:** SyncVSR (2024) [[6]](#ref-6) [later] reports 93.2% ± 0.1 over three seeds.

The 0.7-point LRW gain, a 5.6% relative error reduction (inference), has no seed or interval (Sec. 3.4 to 3.5), and the prose states 0.8 points (Sec. 4.1). The authors qualify the LRS2 claim to "no external labelled datasets" (Sec. 4.2), but the LM uses LRS2, LRS3 and LibriSpeech text without stated partitions (Sec. 3.5). Standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Voiced LRS3 (pre-training), LRW and LRS2 talking-face video | Voiced speech recorded for training | – | standard |
| M02 Training-only supervision | Frozen PASE+ acoustic features as L1 regression target | Distillation from a supervised speech recognizer (2 of 3 prior) (pattern match 2) | [[6]](#ref-6) audio-token prediction, LRW 93.2% (no word boundary, three seeds) | standard |
| M03 Training and adaptation | Audio-feature regression pre-training on LRS3, then frozen or fine-tuned encoder | Cross-modal contrastive or synchronisation pre-training (2 of 3 prior) (pattern match 2) | [[10]](#ref-10) LRS2 VSR WER 23.2% (Large, 1,759 h unlabelled, no LM) | standard |
| M04 Use-time action | Voiced speech video at test | Voiced speech at use time | – | standard |
| M05 Sensors | dlib-landmark mouth ROI, 96x96, 88x88 crop, 25 fps | Camera mouth ROI | – | standard |
| M06 Processing and decoding | 3D conv + ResNet-18 + Conformer; MS-TCN (LRW) or hybrid CTC/attention (LRS2) | CNN front end + sequence model | – | standard |
| M07 Lexicon and LM | Transformer LM (LRS2, LRS3, LibriSpeech text), beam 20 | LM in sentence decoding | – | standard |
| M08 Output | Word class (LRW) or text (LRS2) | Word class or text | – | standard |
| M09 Confirmation | None (offline) | Mostly absent | – | not applicable |
| M10 Correction | None (offline) | Mostly absent | – | not applicable |
| M11 Reference construction | Public LRW and LRS2 test sets | Public benchmark split | – | standard |
| M12 Evaluation | LRW accuracy and LRS2 WER, one run per point, no seeds | No run spread (30 of 30 prior LRW systems) (pattern match 30) | [[6]](#ref-6) LRW 93.2% ± 0.1 (three seeds) | standard |
| M13 Device and cost | Offline GPU training | Offline GPU training | – | standard |

## Where the claims outrun the evidence

- "Significantly" (Abstract) rests on no test or spread, and the scratch backbone beats the other self-supervised methods (Table 1).
- The 18-fold data claim (76 h against 1,362 h, Sec. 4.2) compares against TM-seq2seq with another architecture and LM, not LiRA-Supervised at 76 h.
- The authors report that scratch training degrades beyond 18% of LRS2 labels (Sec. 4.2), so the Fig. 4b gap partly measures optimisation failure.

## What the field needs next

- M02: one encoder and decoder with four targets (PASE+, mel, recognizer posteriors, audio tokens [[6]](#ref-6)) at 1%, 10% and 100% of LRW labels.
- M03: contrastive priors rerun on the same encoder.
- M12: three or more seeds per point, with the LM fixed or removed.

## Questions for the authors

- Which LRS3 partitions were used for pre-training (Sec. 3.1)?
- What do LiRA-Supervised and LiRA-FineTuned give at 76 h, and what do MFCC targets give?
- Which LM and CTC weights, and which checkpoint-selection split, were used?

## Appendix: literature search

- M02, audio-knowledge-transfer-to-video. Inclusion rule: lip-reading and video-to-speech studies with video-only input at test that use paired audio or a speech model in training to enrich the visual model (published rule kept); video-to-speech systems whose audio is the output, self-distillation without audio and AVSR without transfer removed. Ledger counts: 31 unique studies slot-filled for M02; 54 unique studies pattern match (all years). Prior means first public before 2020-12, [concurrent] 2020-12 to 2021-12. Screened prior studies: 2 in the ledger pattern (distillation from a supervised recognizer 2) plus 1 from the full-text step (mel regression, [[3]](#ref-3)); regression of a self-supervised audio encoder's features 0; 3 [concurrent] (distillation 2, mel regression 1). Full-text pattern (audio-feature, mel, PASE, wav2vec or HuBERT regression in lip-reading or video-to-speech text): 75 full-text-only folders; recall sample of 30, of which 1 earlier study has the same family of design [[3]](#ref-3). Read in full: [[4]](#ref-4) (prior), [[5]](#ref-5) (prior), [[3]](#ref-3) (prior), [[6]](#ref-6) (state of the art). Known-item recall 1.0 on the published seed set; 0.83 on this review's seeds (SyncVSR missed by the pattern).
- M03, self-supervised-pretraining. Inclusion rule: self-supervised or teacher-generated pre-training on unlabelled non-audio-only input before supervised fine-tuning for speech or text decoding (published rule kept), screened to visual-speech decoders evaluated on lip reading. Ledger counts: 1,526 unique studies slot-filled for M03; 123 unique studies pattern match (all years). Screened prior studies: 3 (contrastive or synchronisation 2, teacher distillation 1, audio-feature regression 0); AV-PPC named through the target's Table 1; 1 [concurrent] [[7]](#ref-7). Read in full: [[8]](#ref-8) (prior), [[5]](#ref-5) (prior), [[10]](#ref-10) (state of the art). Known-item recall 1.0.
- M12, lrw-word-accuracy. Inclusion rule: visual-only top-1 accuracy on the English LRW test set (published rule kept); for the run-spread count, LRW word-level systems first public before 2020-12 with full text, datasets, keyword spotting, enhancement, separation, face generation, lip-to-speech and surveys removed. Ledger counts: 6,960 unique studies slot-filled for M12; 155 unique studies pattern match (all years). Prior systems after screening: 30; spread-pattern hits 8, all augmentation ranges, normalisation or timing averages, none a run spread. Read in full: [[6]](#ref-6) (state of the art). Known-item recall 0.75.

## References

Numbered by first citation. BibTeX in the same order and keys: [lira-learning-visual-speech-representations-from-audio-through-self-supervision.bib](lira-learning-visual-speech-representations-from-audio-through-self-supervision.bib).

1. <a id="ref-1"></a>Ma, P., Mira, R., Petridis, S., Schuller, B. W., Pantic, M. “LiRA: Learning Visual Speech Representations from Audio through Self-supervision.” *Interspeech*, 2021. doi:[10.21437/Interspeech.2021-1360](https://doi.org/10.21437/Interspeech.2021-1360). arXiv:[2106.09171](https://arxiv.org/abs/2106.09171). [wiki: isca-ma21c-lira](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-ma21c-lira/article.md) [wiki: arxiv-2106.09171](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2106.09171/article.md) [wiki: isca-ma21c_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-ma21c_interspeech/article.md)
2. <a id="ref-2"></a>Ma, P., Petridis, S., Pantic, M. “End-to-End Audio-Visual Speech Recognition with Conformers.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2021. doi:[10.1109/ICASSP39728.2021.9413459](https://doi.org/10.1109/ICASSP39728.2021.9413459). arXiv:[2102.06657](https://arxiv.org/abs/2102.06657). [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/end-to-end-audio-visual-speech-recognition-with-conformers) [wiki: arxiv-2102.06657](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2102.06657/article.md)
3. <a id="ref-3"></a>Qu, L., Weber, C., Wermter, S. “LipSound: Neural Mel-spectrogram Reconstruction for Lip Reading.” *Interspeech*, 2019. doi:[10.21437/Interspeech.2019-1393](https://doi.org/10.21437/Interspeech.2019-1393). [wiki: isca-qu19-lipsound](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-qu19-lipsound/article.md) [wiki: isca-qu19_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-qu19_interspeech/article.md)
4. <a id="ref-4"></a>Zhao, Y., Xu, R., Wang, X., Hou, P., Tang, H., Song, M. “Hearing Lips: Improving Lip Reading by Distilling Speech Recognizers.” *AAAI Conference on Artificial Intelligence*, 2020. doi:[10.1609/aaai.v34i04.6174](https://doi.org/10.1609/aaai.v34i04.6174). arXiv:[1911.11502](https://arxiv.org/abs/1911.11502). [wiki: arxiv-1911.11502](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1911.11502/article.md) [wiki: doi-10.1609-aaai.v34i04.6174](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1609-aaai.v34i04.6174/article.md)
5. <a id="ref-5"></a>Afouras, T., Chung, J. S., Zisserman, A. “ASR is all you need: cross-modal distillation for lip reading.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2020. arXiv:[1911.12747](https://arxiv.org/abs/1911.12747). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/asr-is-all-you-need-cross-modal-distillation-for-lip-reading) [wiki: arxiv-1911.12747](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1911.12747/article.md)
6. <a id="ref-6"></a>Ahn, Y. J., Park, J., Park, S., Choi, J., Kim, K. “SyncVSR: Data-Efficient Visual Speech Recognition with End-to-End Crossmodal Audio Token Synchronization.” *Interspeech*, 2024. arXiv:[2406.12233](https://arxiv.org/abs/2406.12233). [later] [wiki: arxiv-2406.12233](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2406.12233/article.md) [wiki: isca-ahn24-syncvsr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-ahn24-syncvsr/article.md) [wiki: isca-ahn24_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-ahn24_interspeech/article.md) [wiki: in24-syncvsr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/in24-syncvsr/article.md)
7. <a id="ref-7"></a>Qu, L., Weber, C., Wermter, S. “LipSound2: Self-Supervised Pre-Training for Lip-to-Speech Reconstruction and Lip Reading.” *IEEE Transactions on Neural Networks and Learning Systems*, 2022. doi:[10.1109/TNNLS.2022.3191677](https://doi.org/10.1109/TNNLS.2022.3191677). arXiv:[2112.04748](https://arxiv.org/abs/2112.04748). [concurrent] [wiki: arxiv-2112.04748](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2112.04748/article.md) [wiki: doi-10.1109-tnnls.2022.3191677](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tnnls.2022.3191677/article.md)
8. <a id="ref-8"></a>Chung, S., Chung, J. S., Kang, H. “Perfect Match: Improved Cross-modal Embeddings for Audio-visual Synchronisation.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2019. arXiv:[1809.08001](https://arxiv.org/abs/1809.08001). [wiki: arxiv-1809.08001](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1809.08001/article.md)
9. <a id="ref-9"></a>Chung, S., Kang, H., Chung, J. S. “Seeing voices and hearing voices: learning discriminative embeddings using cross-modal self-supervision.” *Interspeech*, 2020. arXiv:[2004.14326](https://arxiv.org/abs/2004.14326). [wiki: arxiv-2004.14326](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2004.14326/article.md)
10. <a id="ref-10"></a>Haliassos, A., Ma, P., Mira, R., Petridis, S., Pantic, M. “Jointly Learning Visual and Auditory Speech Representations from Raw Data.” *International Conference on Learning Representations (ICLR)*, 2023. arXiv:[2212.06246](https://arxiv.org/abs/2212.06246). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/jointly-learning-visual-and-auditory-speech-representations-from-raw-data) [wiki: arxiv-2212.06246](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2212.06246/article.md)
