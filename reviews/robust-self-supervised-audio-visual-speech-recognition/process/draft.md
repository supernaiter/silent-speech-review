# Robust Self-Supervised Audio-Visual Speech Recognition

Bowen Shi, Wei-Ning Hsu, Abdelrahman Mohamed. Interspeech 2022. [doi:10.21437/Interspeech.2022-99](https://doi.org/10.21437/Interspeech.2022-99) [arXiv:2201.01763](https://arxiv.org/abs/2201.01763)

## Verdict

The paper [[1]](#ref-1) changes training (M03): self-supervised audio-visual pre-training with noise mixed into pre-training and fine-tuning. The design was new for AVSR: none of the 143 AVSR ledger studies dated before it pre-trains self-supervised or adds noise in pre-training (pattern match, Appendix). M03 is still standard, not ahead: every result is one run on one test set (Sec. 3.1), and the new part, noise in pre-training, buys 1.5 and 1.1 WER points (Table 3). M12 is behind the best comparable work: earlier AVSR studies reported 95% confidence intervals or repeated runs [[2]](#ref-2), [[3]](#ref-3), [[4]](#ref-4); this paper reports neither. The headline 49.6% babble reduction over [[5]](#ref-5) sets 30 h of labels plus unlabelled pre-training and a LARGE model against a 433 h supervised system: it measures the whole recipe.

## Against the field, component by component

### M03 Training: self-supervised pre-training with added noise

**Usual approach:** Of 349 AVSR ledger studies, 143 predate the target; 141 of the 143 have no self-supervised pre-training (pattern match, Appendix), and the other two only cite it. Robustness came from noise in supervised training (14 of 143, pattern match, upper bound): babble at 0 dB with probability 0.25 [[6]](#ref-6), babble at -10 to 10 dB from 30 LRS3 clips [[5]](#ref-5), NOISEX babble at -5 to 20 dB [[7]](#ref-7). None of the 143 adds noise during pre-training (Appendix). The paper moves the 0 dB, 0.25 recipe of [[6]](#ref-6) (Sec. 3.1) into AV-HuBERT pre-training [[8]](#ref-8) [concurrent].

**State of the art:** In 2026, at the same budget (Large model, LRS3 and VoxCeleb2 unlabelled, 30 h of labels), pseudo-labelling reaches 2.2% clean AVSR WER against 3.3% for AV-HuBERT, a third lower (inference) [[9]](#ref-9) [later]. In NOISEX babble at 10 to -5 dB (Base, 30 h, no noise augmentation for any model) it averages 14.1% against 24.4%, 42% lower (inference).

Pre-training carries most of the gain: noisy WER falls from 42.9% from scratch to 9.3% with clean pre-training at 30 h (Table 3). The scratch baseline is weak: 3.5% clean AV WER at 433 h (Table 3) against 2.3% for the supervised Conformer of [[7]](#ref-7) at 595 h (Table 2). Noise in pre-training moves average noisy WER from 9.3% to 7.8% at 30 h and from 6.9% to 5.8% at 433 h (16.1% and 15.9% relative, Table 3), one run per cell. Two label budgets repeat the direction, not the measurement: standard. Later gains came without noise augmentation [[9]](#ref-9) (inference).

### M12 Evaluation: noise categories and run variability

**Usual approach:** 183 of 349 AVSR studies test with additive noise at stated SNRs and no run-to-run variability (pattern match, Appendix); babble appears in 128, interfering speech in 91 (14 before the target). The paper follows this with four noise types at five SNRs (Sec. 3.1).

**State of the art:** Whisper-Flamingo (2024) lists AV-HuBERT at 1.4% clean and 5.8% in 0 dB LRS3 babble (433 h labels, 1,759 h unlabelled; this paper's Table 2 values) and two other models with the same budget and noise file at 4.6% and 4.4% [[10]](#ref-10) [later]; its own best clean AVSR WER is 0.76%.

Before the target, [[2]](#ref-2) gave 95% confidence intervals for babble and overlapping-speech tests (Table 5), [[3]](#ref-3) repeated each experiment 5 times with 95% intervals, and [[4]](#ref-4) trained five random initialisations on LRS2. This paper gives neither (Sec. 3.1; the released configs fix seed 1337), so the 1.1-point gain from noisy pre-training at 433 h cannot be separated from run-to-run variation (inference). Behind, against the best comparable work.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Voiced LRS3 and English VoxCeleb2 video | Voiced speech recorded for training | – | standard |
| M02 Training-only supervision | Subword transcripts, 30 h or 433 h of LRS3 | Text labels | – | standard |
| M03 Training and adaptation | AV-HuBERT pre-training; noise in pre-training and fine-tuning | No self-supervised pre-training before 2022-01 (pattern match 141) | [[9]](#ref-9) 2.2% clean AVSR WER at 30 h (Large) | standard |
| M04 Use-time action | Voiced speech video with added noise at test | Voiced speech at use time | – | standard |
| M05 Sensors | Lip video and one microphone; MUSAN and LRS3 noise | Camera mouth region plus microphone | – | standard |
| M06 Processing and decoding | AV-HuBERT LARGE encoder, 9-layer Transformer decoder | CNN front end plus sequence model | – | standard |
| M07 Lexicon and LM | No external LM (released config; paper silent) | LM in decoding varies | – | standard |
| M08 Output | Text (subwords) | Text output | – | standard |
| M09 Confirmation | None (offline) | Mostly absent | – | not applicable |
| M10 Correction | None (offline) | Mostly absent | – | not applicable |
| M11 Reference construction | LRS3 test set; MUSAN and LRS3 noise pools | Public benchmark split | – | standard |
| M12 Evaluation | Four noise types, five SNRs, no variability | Noise test at stated SNRs, no run variability (pattern match 183) | [[10]](#ref-10) 0.76% clean | behind |
| M13 Device and cost | 64 V100 GPUs; no runtime | Offline GPU training | – | standard |

## Where the claims outrun the evidence

- The 49.6% babble reduction (14.1% against 28.0%, Table 2) sets 30 h of labels plus pre-training on 433 h of LRS3 and 1,326 h of VoxCeleb2 against a 433 h supervised system [[5]](#ref-5). Xu et al. trained on LRS3 babble, the test source, this paper on MUSAN babble (Sec. 3.2): noise favours the comparator, data and model size the target.
- The 39.0% clean gain over [[7]](#ref-7) (1.4% against 2.3%, Table 2) is credited with "fewer labeled hours" (433 h against 595 h, Sec. 3.2), leaving out the unlabelled VoxCeleb2 hours.
- In the released code, validation and test babble are one file (cf. the noise pools of Table 1) and the checkpoint is chosen on validation accuracy; if validation is noisy, selection saw the test noise.
- The code splits speech-noise clips 60/20/20 by list order, not speaker, so test and training interferers may share speakers; the 48.1% to 7.7% speech-noise result (Sec. 3.3.1) may be optimistic (inference).
- The authors concede the MUSAN and LRS3 babble mismatch (Sec. 3.2), the missing LRS2 audio of [[6]](#ref-6) (footnote 2), and leave real noisy use to future work (Sec. 4).

## What the field needs next

- M03: clean against noisy pre-training over at least three seeds and on a second test set with recorded noise.
- M03: noise-augmented pre-training combined with pseudo-labelling at 30 h [[9]](#ref-9), to test whether the gains add.
- M12: speaker-disjoint interfering-speech tests (overlapping speech was tested before [[2]](#ref-2)), separate validation and test noise, and confidence intervals.

## Questions for the authors

- How many runs underlie each cell of Tables 2-4?
- Was the checkpoint selected on clean or noisy validation data, with which babble file?
- Are test interferers disjoint from training interferers and LRS3 test speakers?
- Was an external language model used? The released config sets its weight to 0.

## Appendix: literature search

- M03, avsr-self-supervised-and-noise-augmented-training. Inclusion rule: studies whose ledger names audio-visual speech recognition (the 349-study AVSR population), classified by the training regime their full text names (self-supervised pre-training, noise added during training, noise added during pre-training); the state at the target's time uses the studies dated before 2022-01; related-work mentions included (upper bound); visual-only lip reading out; versions once. Ledger counts: 1,526 unique studies slot-filled for M03; 349 unique studies pattern match. Before 2022-01: 143 studies; no self-supervised pre-training 141 (the two matches are citations, read); noise added during training 14; noise in pre-training 0 (pattern match). All dates: self-supervised pre-training 160, noise added during training 61, noise in pre-training 8 (pattern match). Read in full: [[6]](#ref-6), [[5]](#ref-5), [[7]](#ref-7) (prior), [[9]](#ref-9) (state of the art). Known-item recall 0.5.
- M12, avsr-noise-and-run-variability-protocol (published table, appended). Inclusion rule: the same 349-study AVSR population, classified by the evaluation protocol its full text names (additive noise at stated SNRs, babble, run-to-run variability; interfering speech added here); a study counts under every protocol it names. Ledger counts: 6,960 unique studies slot-filled for M12; 349 unique studies pattern match. Usual design: additive noise at stated SNRs without run-to-run variability, 183 (pattern match); babble 128; run variability 33; interfering speech 91, 14 before 2022-01. Sentence-level AVSR studies before 2022-01 with run or test-set variability, read: [[2]](#ref-2), [[3]](#ref-3), [[4]](#ref-4) (prior); state of the art [[10]](#ref-10). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [robust-self-supervised-audio-visual-speech-recognition.bib](robust-self-supervised-audio-visual-speech-recognition.bib).

1. <a id="ref-1"></a>Shi, B., Hsu, W., Mohamed, A. “Robust Self-Supervised Audio-Visual Speech Recognition.” *Interspeech 2022*, 2022. doi:[10.21437/Interspeech.2022-99](https://doi.org/10.21437/Interspeech.2022-99). arXiv:[2201.01763](https://arxiv.org/abs/2201.01763). First public as arXiv:2201.01763 (2022-01). [wiki: isca-shi22-robustav](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-shi22-robustav/article.md) [wiki: isca-shi22_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-shi22_interspeech/article.md) [wiki: arxiv-2201.01763](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2201.01763/article.md)
2. <a id="ref-2"></a>Makino, T., Liao, H., Assael, Y., Shillingford, B., Garcia, B., Braga, O., et al. “Recurrent Neural Network Transducer for Audio-Visual Speech Recognition.” *IEEE Automatic Speech Recognition and Understanding Workshop (ASRU)*, 2019. doi:[10.1109/ASRU46091.2019.9004036](https://doi.org/10.1109/ASRU46091.2019.9004036). arXiv:[1911.04890](https://arxiv.org/abs/1911.04890). Prior; deciding prior for M12 (95% CIs, babble and overlapping-speech tests). [wiki: arxiv-1911.04890](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1911.04890/article.md) [wiki: doi-10.1109-asru46091.2019.9004036](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-asru46091.2019.9004036/article.md)
3. <a id="ref-3"></a>Sterpu, G., Saam, C., Harte, N. “How to Teach DNNs to Pay Attention to the Visual Modality in Speech Recognition.” *IEEE/ACM Transactions on Audio, Speech, and Language Processing*, 2020. doi:[10.1109/TASLP.2020.2980436](https://doi.org/10.1109/TASLP.2020.2980436). arXiv:[2004.08250](https://arxiv.org/abs/2004.08250). Prior; five repetitions with 95% CIs (M12). [wiki: arxiv-2004.08250](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2004.08250/article.md)
4. <a id="ref-4"></a>Sterpu, G., Harte, N. “AV Taris: Online Audio-Visual Speech Recognition.” *arXiv preprint*, 2020. arXiv:[2012.07467](https://arxiv.org/abs/2012.07467). Prior; five random initialisations on LRS2 (M12). [wiki: arxiv-2012.07467](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2012.07467/article.md)
5. <a id="ref-5"></a>Xu, B., Lu, C., Guo, Y., Wang, J. “Discriminative Multi-Modality Speech Recognition.” *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2020. doi:[10.1109/CVPR42600.2020.01444](https://doi.org/10.1109/CVPR42600.2020.01444). Prior; babble comparator in the target's Table 2. [wiki: cvf-xu20-msr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-xu20-msr/article.md) [wiki: cvf-xu20-aemsr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-xu20-aemsr/article.md)
6. <a id="ref-6"></a>Afouras, T., Chung, J. S., Senior, A., Vinyals, O., Zisserman, A. “Deep Audio-Visual Speech Recognition.” *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 2018. doi:[10.1109/TPAMI.2018.2889052](https://doi.org/10.1109/TPAMI.2018.2889052). arXiv:[1809.02108](https://arxiv.org/abs/1809.02108). Prior; deciding prior for M03 (babble at 0 dB, probability 0.25, during supervised training). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/deep-audio-visual-speech-recognition) [wiki: arxiv-1809.02108](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1809.02108/article.md) [wiki: doi-10.1109-tpami.2018.2889052](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tpami.2018.2889052/article.md)
7. <a id="ref-7"></a>Ma, P., Petridis, S., Pantic, M. “End-to-End Audio-Visual Speech Recognition with Conformers.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2021, 7613-7617. arXiv:[2102.06657](https://arxiv.org/abs/2102.06657). Prior; supervised AVSR with NOISEX babble augmentation; clean LRS3 comparator. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/end-to-end-audio-visual-speech-recognition-with-conformers) [wiki: arxiv-2102.06657](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2102.06657/article.md)
8. <a id="ref-8"></a>Shi, B., Hsu, W., Lakhotia, K., Mohamed, A. “Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction.” *International Conference on Learning Representations (ICLR)*, 2022. arXiv:[2201.02184](https://arxiv.org/abs/2201.02184). The pre-training method the target builds on. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/learning-audio-visual-speech-representation-by-masked-multimodal-cluster-prediction) [wiki: arxiv-2201.02184](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2201.02184/article.md)
9. <a id="ref-9"></a>Haliassos, A., Mira, R., Petridis, S. “Pay Attention to CTC: Fast and Robust Pseudo-Labelling for Unified Speech Recognition.” *International Conference on Learning Representations (ICLR)*, 2026. arXiv:[2602.19316](https://arxiv.org/abs/2602.19316). State of the art for M03 at the 30 h budget. [later] [wiki: arxiv-2602.19316](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.19316/article.md)
10. <a id="ref-10"></a>Rouditchenko, A., Gong, Y., Thomas, S., Karlinsky, L., Kuehne, H., Feris, R., et al. “Whisper-Flamingo: Integrating Visual Features into Whisper for Audio-Visual Speech Recognition and Translation.” *Interspeech 2024*, 2024. arXiv:[2406.10082](https://arxiv.org/abs/2406.10082). LRS3 AVSR state of the art and 0 dB babble comparison table (M12). [later] [wiki: arxiv-2406.10082](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2406.10082/article.md) [wiki: isca-rouditchenko24-whisperflamingo](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-rouditchenko24-whisperflamingo/article.md) [wiki: in24-whisperflamingo](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/in24-whisperflamingo/article.md) [wiki: isca-rouditchenko24_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-rouditchenko24_interspeech/article.md)
