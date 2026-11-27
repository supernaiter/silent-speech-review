# Jointly Learning Visual and Auditory Speech Representations from Raw Data

Alexandros Haliassos, Pingchuan Ma, Rodrigo Mira, Stavros Petridis, Maja Pantic. ICLR 2023. [arXiv:2212.06246](https://arxiv.org/abs/2212.06246)

## Verdict

The paper [[1]](#ref-1) changes the pre-training objective (M03), asymmetric cross-modal prediction of momentum-teacher latents, and training-only audio supervision (M02); both stay standard. At Large with 1,759 h unlabelled and 30 h labelled, without self-training or LM, its 32.5% VSR WER equals AV-HuBERT's 32.5% [[2]](#ref-2) (Table 1), so "surpasses all self-supervised methods on VSR" rests on Base (4.8 and 5.9 points), 27.8% against 28.6% with 433 h labelled, and self-training, all single runs. The largest VSR gain after pre-training, 32.5% to 24.8% (7.7 points), comes from the fine-tuned audio encoder's pseudo-labels (Sec. 3.2), the usual audio-teacher route. The 90,000-hour comparison is made against 25.9% while the same Table 1 lists 19.3%. USR 2.0 now reaches 23.7% at the same budget [[3]](#ref-3) [later].

## Against the field, component by component

### M03 Training: self-supervised pre-training objective

**Usual approach:** Of the 33 pre-training studies dated 2022 or earlier (pattern match, unique studies, Appendix), the 24 with full text mention contrastive objectives in 18, cluster targets in 14 and audio-feature regression in 14; the LRS3 reference was AV-HuBERT's iterated cluster prediction [[2]](#ref-2), and the authors' LiRA regressed frozen PASE+ features [[4]](#ref-4). This paper drops offline targets.

**State of the art:** USR 2.0 (2026) reaches 23.7% VSR WER at the same Large, 30 h budget [[3]](#ref-3) [later], 27% relative below the 32.5% here and 1.1 points below the self-trained 24.8% (inference).

The design is new against its priors: of 13 full-text hits for momentum or EMA teachers near visual speech (Appendix), none predates the target, and the one hit among the 24 studies to 2022 is AV2vec [[5]](#ref-5) [concurrent]. The asymmetry matters inside the paper (symmetric variant 49.0% against 32.9%, Table 3), but every ablation is Base, validation set, one run (Sec. 4.4). At Large there is no VSR gain over AV-HuBERT (32.5% for both, Table 1 and [[3]](#ref-3)), and AV-data2vec reaches 30.8% there [[6]](#ref-6) [concurrent]. Base margins come with a decoder (hybrid CTC/attention, Sec. 3.2) not stated to match the comparators'. Standard.

### M02 Training-only supervision: audio teacher for the video model

**Usual approach:** Of 14 lip-reading or video-to-speech studies to 2022 that transfer audio knowledge to video (pattern match, unique studies, Appendix), 10 distil from a frozen audio recogniser [[7]](#ref-7). Here a jointly trained audio teacher supplies latents, then the fine-tuned audio encoder pseudo-labels unlabelled video (Sec. 3.2).

**State of the art:** USR 2.0 (2026) uses EMA-teacher pseudo-labels and reaches 23.7% at the matched budget [[3]](#ref-3) [later], against 24.8% with this paper's ASR pseudo-labels.

Pseudo-labelling, the usual distillation route, carries the final gain: 32.5% to 24.8%, 24% relative (inference), against no gap to AV-HuBERT from pre-training. Self-trained, 24.8% and 24.4% sit below AV-HuBERT's 28.6% and 26.9% (Tables 1 and 2), but round count and LM use in pseudo-labelling are not stated, so the rows are not like-for-like. As the authors state, no extra data is needed (Sec. 4.3). Standard.

### M12 Evaluation: LRS3 WER from single runs

**Usual approach:** 37 of 49 LRS3 system papers dated 2022 or earlier show no run-spread pattern (pattern match, unique studies, Appendix); so does this paper.

**State of the art:** 17.6% VSR WER, USR 2.0 Huge (2026), LRS2+LRS3 labelled [[3]](#ref-3) [later]; at the target's time Table 1 lists 19.3% from 90,000 labelled hours including non-public data.

The headline 23.8% uses an LM; the 25.9% it is set against does not, and is called semi-supervised in the abstract but supervised in Table 1. LRS2 (17.9%, Table 9) has no AV-HuBERT row. Standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Voiced LRS3 / VoxCeleb2 talking-face video | Voiced speech recorded for training | – | standard |
| M02 Training-only supervision | Joint audio-teacher latents; ASR pseudo-labels in self-training | Distillation from a frozen audio recogniser (10 of 14, to 2022) (pattern match 10) | [[3]](#ref-3) EMA-teacher pseudo-labels, 23.7% (Large, 30 h) | standard |
| M03 Training and adaptation | Asymmetric cross-modal prediction of momentum-teacher latents | Contrastive objectives (18 of 24, to 2022); AV-HuBERT on LRS3 (pattern match 18) | [[3]](#ref-3) 23.7% at Large, 30 h, LRS3+VoxCeleb2 | standard |
| M04 Use-time action | Voiced speech video at test | Voiced speech at use time | – | standard |
| M05 Sensors | Grayscale mouth ROI, 25 fps; raw 16 kHz audio | Camera mouth ROI plus microphone | – | standard |
| M06 Processing and decoding | ResNet-18 + Transformer; hybrid CTC/attention | CNN front end + sequence model | – | standard |
| M07 Lexicon and LM | Transformer LM, shallow fusion, beam 40 | LM in decoding (sparse slot) | – | standard |
| M08 Output | Text | Text output | – | standard |
| M09 Confirmation | None (offline) | Mostly absent | – | not applicable |
| M10 Correction | None (offline) | Mostly absent | – | not applicable |
| M11 Reference construction | LRS3 and LRS2 public test sets | Public benchmark split | – | standard |
| M12 Evaluation | LRS3 test WER, single runs, no seeds | No run spread (37 of 49 LRS3 systems, to 2022) (pattern match 37) | [[3]](#ref-3) 17.6% (Huge, LRS2+LRS3 labelled) | standard |
| M13 Device and cost | 32 / 128 A100 GPUs for pre-training | Offline GPU training | – | standard |

## Where the claims outrun the evidence

- "Surpasses all self-supervised methods on VSR on LRS3" (Abstract) fails at Large with 30 h: 32.5% for both (Table 1); Sec. 4.2 states it for Base only.
- The asymmetric loss is chosen on Base in single validation runs (Sec. 4.4, Table 3), then used unablated at Large.
- "Transcribed data ... can be largely substituted" (Sec. 4.2): the best 30 h result also uses ASR pseudo-labels and an LM trained on text including LRS2 and LRS3 (App. A.4).
- Removal of LRS3 test videos from unlabelled pre-training is not stated (Appendix A.1).

## What the field needs next

- M03: rerun AV-HuBERT, RAVEn and AV-data2vec under one fine-tuning recipe at Base and Large, three or more seeds, on LRS3 and LRS2.
- M02: fix the encoder and compare pseudo-label sources (audio encoder, EMA teacher, none) with rounds and LM use stated.
- M11: exclude LRS3 test videos from pre-training and add the noisy-audio test the authors defer (App. C.3).

## Questions for the authors

- Were the AV-HuBERT rows copied from Shi et al. (2022), and did their decoder, beam and LM match yours?
- How many self-training rounds were run; did the pseudo-labeller use the LM or filtering?
- Were LRS3 test videos removed from the unlabelled pre-training data?
- How many runs underlie Tables 1 to 3, and what is the spread?
- Which LM weight gave 23.8% (the public script sets 0.3), and which text normalisation precedes scoring?

## Appendix: literature search

- M03, self-supervised-pretraining. Inclusion rule: self-supervised or teacher-generated pre-training on unlabelled non-audio-only input before supervised fine-tuning for speech or text decoding; audio-only self-supervised ASR and checkpoint reuse excluded. Ledger counts: 1,526 unique studies slot-filled for M03; 123 unique studies pattern match (all years). At the target's time (ledger year 2022 or earlier): 33 unique studies, 24 with full text; contrastive 18, cluster 14, masked 14, audio-feature regression 14, momentum teacher 1 (pattern match, mentions included). Full-text pattern for momentum or EMA teachers near visual speech: 13 further hits, none earlier than the target. Read in full: [[2]](#ref-2) (prior), [[4]](#ref-4) (prior), [[3]](#ref-3) (state of the art). Known-item recall 1.0.
- M02, audio-knowledge-transfer-to-video. Inclusion rule: lip-reading and video-to-speech studies with video-only input at test that use paired audio or a speech model in training (distillation, audio-feature regression, audio memory); audio-visual models needing audio at test excluded. Ledger counts: 31 unique studies slot-filled for M02; 54 unique studies pattern match (all years). At the target's time: 19 unique studies, 14 with full text; knowledge distillation 10, audio memory 4, audio-latent prediction 1 (pattern match). [[4]](#ref-4) falls outside the pattern and is added as a named prior. Read in full: [[7]](#ref-7) (prior), [[4]](#ref-4) (prior), [[3]](#ref-3) (state of the art). Known-item recall 1.0.
- M12, lrs3-visual-only-wer. Inclusion rule: visual-only WER on the LRS3 test set, any training regime; audio-only and audio-visual rows excluded; for the run-spread count, two surveys, the corpus paper and the target are removed. Ledger counts: 6,960 unique studies slot-filled for M12; 258 unique studies pattern match (all years). At the target's time: 59 unique studies, 53 with full text, 49 systems; 12 match a run-spread pattern (upper bound). Read in full: [[3]](#ref-3) (state of the art). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [jointly-learning-visual-and-auditory-speech-representations-from-raw-data.bib](jointly-learning-visual-and-auditory-speech-representations-from-raw-data.bib).

1. <a id="ref-1"></a>Haliassos, A., Ma, P., Mira, R., Petridis, S., Pantic, M. “Jointly Learning Visual and Auditory Speech Representations from Raw Data.” *International Conference on Learning Representations (ICLR)*, 2023. arXiv:[2212.06246](https://arxiv.org/abs/2212.06246). [wiki: arxiv-2212.06246](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2212.06246/article.md)
2. <a id="ref-2"></a>Shi, B., Hsu, W., Lakhotia, K., Mohamed, A. “Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction.” *International Conference on Learning Representations (ICLR)*, 2022. arXiv:[2201.02184](https://arxiv.org/abs/2201.02184). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/learning-audio-visual-speech-representation-by-masked-multimodal-cluster-prediction) [wiki: arxiv-2201.02184](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2201.02184/article.md)
3. <a id="ref-3"></a>Haliassos, A., Mira, R., Petridis, S. “Pay Attention to CTC: Fast and Robust Pseudo-Labelling for Unified Speech Recognition.” *International Conference on Learning Representations (ICLR)*, 2026. arXiv:[2602.19316](https://arxiv.org/abs/2602.19316). [later] [wiki: arxiv-2602.19316](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.19316/article.md)
4. <a id="ref-4"></a>Ma, P., Mira, R., Petridis, S., Schuller, B. W., Pantic, M. “LiRA: Learning Visual Speech Representations from Audio through Self-supervision.” *Interspeech*, 2021. doi:[10.21437/Interspeech.2021-1360](https://doi.org/10.21437/Interspeech.2021-1360). [wiki: isca-ma21c-lira](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-ma21c-lira/article.md)
5. <a id="ref-5"></a>Zhang, J., Wan, G., Ling, Z., Pan, J., Gao, J., Liu, C. “Self-Supervised Audio-Visual Speech Representations Learning by Multimodal Self-Distillation.” *arXiv*, 2022. arXiv:[2212.02782](https://arxiv.org/abs/2212.02782). [concurrent] [wiki: arxiv-2212.02782](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2212.02782/article.md)
6. <a id="ref-6"></a>Lian, J., Baevski, A., Hsu, W., Auli, M. “AV-data2vec: Self-supervised Learning of Audio-Visual Speech Representations with Contextualized Target Representations.” *arXiv*, 2023. arXiv:[2302.06419](https://arxiv.org/abs/2302.06419). [concurrent] [wiki: arxiv-2302.06419](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2302.06419/article.md)
7. <a id="ref-7"></a>Afouras, T., Chung, J. S., Zisserman, A. “ASR is all you need: cross-modal distillation for lip reading.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2020. arXiv:[1911.12747](https://arxiv.org/abs/1911.12747). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/asr-is-all-you-need-cross-modal-distillation-for-lip-reading) [wiki: arxiv-1911.12747](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1911.12747/article.md)
