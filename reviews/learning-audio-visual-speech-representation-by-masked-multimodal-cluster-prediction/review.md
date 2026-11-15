# Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction

Bowen Shi, Wei-Ning Hsu, Kushal Lakhotia, Abdelrahman Mohamed. ICLR 2022. [arXiv:2201.02184](https://arxiv.org/abs/2201.02184)

## Verdict

The paper [[1]](#ref-1) changes two components: the pre-training objective (M03), masked prediction of audio-visual cluster labels refined over five iterations, and audio as training-only supervision (M02), with video alone at test. The M03 gain is large on the paper's own terms: its scratch baseline falls from 92.3% to 32.5% WER at 30 h of labels, and it is far below the 59.8% of cross-modal distillation [[2]](#ref-2), although that margin also mixes 334 h against 1,759 h of unlabelled video. Both components remain standard by our rules, because the effect is shown on one test set with no repeated runs in Table 1. Later work now beats the design at the same budget: 23.7% against 32.5% with the same model size, unlabelled data and 30 h of labels [[3]](#ref-3) [later]. The headline claim of beating the best prior system with 1/1000 of the labels overreaches: 32.5% against 33.6% [[4]](#ref-4) is a 1.1-point gap between different training regimes with no variance reported.

## Against the field, component by component

### M03 Training: self-supervised pre-training objective

**Usual approach:** Of the 141 LRS3 papers with a recorded training slot, 6 use self-supervised pre-training; text labels (18) and paired audio (17) dominate (slot-filled, Appendix). The earlier unlabelled-video routes were distillation from an audio recogniser [[2]](#ref-2) and regression of audio features [[5]](#ref-5) [concurrent]. This paper makes the targets audio-visual and refines them from its own encoder.

**State of the art:** In 2026, at the same model size, unlabelled data (LRS3 plus English VoxCeleb2) and 30 h of labels, a unified pseudo-labelling model reaches 23.7% against 32.5% here, 27% relative lower (inference) [[3]](#ref-3) [later]; at 433 h it is 21.5% against 28.6%.

Distillation used ASR-transcribed VoxCeleb2 (334 h) and reached 59.8% [[2]](#ref-2); the paper's 1,759 h is larger because of different filtering parameters and ASR model (Sec. 4.2), so that margin mixes objective and data size. Audio-feature regression moved LRS2 WER from 39.1% to 38.8% over its supervised baseline [[5]](#ref-5); pre-training here moves LRS3 WER from 62.3% to 28.6% at 433 h, a different dataset, so only each gain over its own baseline compares. The verdict is still standard: one test set, no repeated runs (Table 1), and the cluster-quality evidence (NMI 44.2% against 39.7% for audio-only clusters, Table E.1) is a proxy, not a recognition result.

### M02 Training-only supervision: audio as target, video at test

**Usual approach:** Audio used only in training is common; paired audio is the recorded supervision kind in 258 folders (slot-filled, M03 field; M02 is sparse), usually as features [[5]](#ref-5) or ASR transcripts [[2]](#ref-2). Here audio is masked input and part of the cluster targets.

**State of the art:** Later work (2026) keeps audio in training through a teacher that sees unmasked audio-visual input and pseudo-labels unlabelled data; its visual-only WER is lower than this paper's in every matched size and data group of its Table 2 [[3]](#ref-3) [later].

The audio-only result (1.3% against 2.3% ASR WER) sets a model without a language model against one with it (Table 4). Standard.

### M12 Evaluation: LRS3 visual-only WER

**Usual approach:** Unseen-speaker LRS3 test WER is the field benchmark for sentence lip reading [[6]](#ref-6); 258 unique studies mention LRS3 (pattern match, Appendix). The paper follows it.

**State of the art:** 17.6% in 2026 [[3]](#ref-3) [later]; 33.6% in 2019 from 31,000 h of transcribed video [[4]](#ref-4).

The 1.1-point margin over the prior best is 3.3% relative (inference), with no repeated runs. Standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Voiced TED/YouTube speech | Voiced speech recorded for training (slot-filled 4,015) | – | standard |
| M02 Training-only supervision | Audio as training-only target and input; Video-only test | Paired audio as training-only supervision (slot-filled 258) | [[3]](#ref-3) unified pseudo-labels | standard |
| M03 Training and adaptation | Masked prediction of refined audio-visual clusters | Transcribed-video training; self-supervised in 6 of 141 LRS3 papers (slot-filled 6) | [[3]](#ref-3) 23.7% at 30 h | standard |
| M04 Use-time action | Voiced speech video at test | Voiced speech at use time (slot-filled 6,538) | – | standard |
| M05 Sensors | Mouth ROI 96x96, 25 Hz; filterbank audio | Camera mouth ROI plus microphone (slot-filled 8,898) | – | standard |
| M06 Processing and decoding | ResNet-18 + Transformer; CTC or S2S | CNN front end + sequence model (slot-filled 8,925) | – | standard |
| M07 Lexicon and LM | 4-gram LM (CTC); none (S2S) | LM in decoding (sparse slot) (slot-filled 120) | – | standard |
| M08 Output | Text | Text output (slot-filled 3,760) | – | standard |
| M09 Confirmation | None (offline) | Mostly absent (slot-filled 82) | – | not applicable |
| M10 Correction | None (offline) | Mostly absent (slot-filled 82) | – | not applicable |
| M11 Reference construction | LRS3 open-speaker test | Public benchmark split (slot-filled 239) | – | standard |
| M12 Evaluation | LRS3 test WER, no repeated runs | LRS3 visual-only WER (pattern match 258) | [[3]](#ref-3) 17.6% | standard |
| M13 Device and cost | 32-64 V100 GPUs | Offline GPU training (slot-filled 6,721) | – | standard |

## Where the claims outrun the evidence

- "1/1000 of the labeled data" counts only transcribed hours; the 30 h model also uses 1,759 h of unlabelled audio-visual data (Sec. 4.2, Table 1).
- Sec. C.2 contrasts 18.0% for seen speakers with 30.5% for unseen speakers, but no Table 1 row gives 30.5% (32.5% at 30 h, 28.6% at 433 h), and the seen-speaker groups come from trainval, which is also in the 433 h LRS3 pre-training pool (Sec. 4.2).
- The LiRA comparison uses the authors' re-implementation of its objective (Table 1 note), not the published system [[5]](#ref-5).
- The S2S decoder is called LM-free but is trained on LRS3 transcripts, so it carries in-domain text knowledge (Appendix B.4).
- Self-training alone exceeds 50% WER (Appendix C.3), yet its rounds, filtering and pseudo-label quality are not given.

## What the field needs next

- M03: matched-budget comparisons (30 h and 433 h labels, fixed unlabelled data) over at least three seeds and a second test set such as LRS2.
- M04: test whether audio-visual pre-training transfers to silent articulation, where lip motion differs from voiced speech.
- M11: report overlap between pre-training videos and LRS3 test talks, and a seen-speaker split excluded from pre-training.

## Questions for the authors

- Which labelled budget produced the 30.5% unseen-speaker WER in Sec. C.2?
- Were the Sec. C.2 seen-speaker groups excluded from fine-tuning and pre-training?
- How many runs underlie each Table 1 entry, and what is the spread? Only Sec. C.2 gives one (18.0 ± 0.5%).
- Which text normalisation and scoring tool produced the WERs, and do they match those of the comparators?

## Appendix: literature search

- M03, self-supervised-pretraining. Inclusion rule: self-supervised or teacher-generated pre-training on unlabelled non-audio-only input before supervised fine-tuning for speech or text decoding; audio-only self-supervised ASR and checkpoint reuse excluded. Ledger counts: 1,526 unique studies slot-filled for M03; 123 unique studies pattern match. Usual design in the population: supervision_kind=self_supervised, 31 studies (slot-filled, of 75 with M03 recorded). Read in full: [[2]](#ref-2) (prior), [[5]](#ref-5) ([concurrent]), [[3]](#ref-3) (state of the art). Known-item recall 1.0.
- M12, lrs3-visual-only-wer. Inclusion rule: visual-only WER on the LRS3 test set, any training regime; audio-only and audio-visual rows excluded. Ledger counts: 6,960 unique studies slot-filled for M12; 258 unique studies pattern match. Training design among the 141 with M03 recorded: text_prompt 18, paired_audio 17, self_supervised 6 (slot-filled). Read in full: [[3]](#ref-3) (state of the art). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Shi, B., Hsu, W., Lakhotia, K., Mohamed, A. “Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction.” *International Conference on Learning Representations (ICLR)*, 2022. arXiv:[2201.02184](https://arxiv.org/abs/2201.02184). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/learning-audio-visual-speech-representation-by-masked-multimodal-cluster-prediction) [wiki: arxiv-2201.02184](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2201.02184/article.md)
2. <a id="ref-2"></a>Afouras, T., Chung, J. S., Zisserman, A. “ASR is all you need: cross-modal distillation for lip reading.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2020. arXiv:[1911.12747](https://arxiv.org/abs/1911.12747). [wiki: arxiv-1911.12747](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1911.12747/article.md)
3. <a id="ref-3"></a>Haliassos, A., Mira, R., Petridis, S. “Pay Attention to CTC: Fast and Robust Pseudo-Labelling for Unified Speech Recognition.” *International Conference on Learning Representations (ICLR)*, 2026. arXiv:[2602.19316](https://arxiv.org/abs/2602.19316). [later] [wiki: arxiv-2602.19316](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.19316/article.md)
4. <a id="ref-4"></a>Makino, T., Liao, H., Assael, Y., Shillingford, B., Garcia, B., Braga, O., et al. “Recurrent Neural Network Transducer for Audio-Visual Speech Recognition.” *IEEE Automatic Speech Recognition and Understanding Workshop (ASRU)*, 2019. doi:[10.1109/ASRU46091.2019.9004036](https://doi.org/10.1109/ASRU46091.2019.9004036). arXiv:[1911.04890](https://arxiv.org/abs/1911.04890). [wiki: doi-10.1109-asru46091.2019.9004036](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-asru46091.2019.9004036/article.md)
5. <a id="ref-5"></a>Ma, P., Mira, R., Petridis, S., Schuller, B. W., Pantic, M. “LiRA: Learning Visual Speech Representations from Audio through Self-supervision.” *Interspeech*, 2021. doi:[10.21437/Interspeech.2021-1360](https://doi.org/10.21437/Interspeech.2021-1360). [concurrent] [wiki: isca-ma21c-lira](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-ma21c-lira/article.md)
6. <a id="ref-6"></a>Afouras, T., Chung, J. S., Zisserman, A. “LRS3-TED: a large-scale dataset for visual speech recognition.” *arXiv*, 2018. arXiv:[1809.00496](https://arxiv.org/abs/1809.00496). [wiki: arxiv-1809.00496](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1809.00496/article.md)
