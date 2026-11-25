# Lipreading Using Temporal Convolutional Networks

Brais Martinez, Pingchuan Ma, Stavros Petridis, Maja Pantic. arXiv preprint, 2020. [arXiv:2001.08702](https://arxiv.org/abs/2001.08702)

## Verdict

The paper [[1]](#ref-1) changes the temporal back end (M06), a multi-scale dilated TCN in place of a BGRU, and the training recipe (M03), single-stage cosine training with variable-length temporal cropping. Both are standard. The multi-scale TCN has no prior pattern hit among 26 prior LRW studies (Appendix), but its gain over a BGRU is one run on one dataset: 85.30% against 84.60% for the fixed-length BGRU (Table 2), and a [later] matched-recipe test from the same group gives 90.0% against 89.7% [[2]](#ref-2). Frame-drop robustness comes from the cropping, not the TCN: trained the same way, both heads lose about the same share of accuracy with five frames removed (Table 2). The 1.2-point LRW and 3.2-point LRW-1000 gains are single runs against literature numbers from other recipes. Today it sits 7.9 points below the best LRW-only system [[3]](#ref-3) (inference); its lasting value is adoption as a default back end, not a shown advantage.

## Against the field, component by component

### M06 Processing: temporal back end

**Usual approach:** a recurrent back end (LSTM or GRU) after a 3D-conv + ResNet front end; 115 of 156 unique word-level LRW / LRW-1000 studies name one (pattern match, Appendix), and 24 of the 26 prior studies do. The paper replaces the BGRU of its baseline [[4]](#ref-4) with a non-causal, dilated, multi-scale TCN.

**State of the art:** at the time, 84.1% on LRW from a Kinetics-pretrained two-stream I3D with a Bi-LSTM [[5]](#ref-5), 1.2 points below the paper. Today, SyncVSR [[3]](#ref-3) [later] (2024) reaches 93.2% on LRW without word boundaries (mean of three runs) and 58.2% on CAS-VSR-W1K, against 85.3% and 41.4% here.

Temporal convolution on LRW is not new: 6 prior studies name it (pattern match, Appendix), and the read priors found it weaker than a Bi-LSTM: a shallow two-layer stage (74.6%, N2) used to initialise the Bi-LSTM system (83.0%, N7) [[6]](#ref-6), and 22.51% error for TConv against 17.01% for two BiLSTM layers [[7]](#ref-7). New are depth, dilation and multi-scale branches: 0 prior hits, 2 [concurrent] (with [[8]](#ref-8)) and 38 [later] (Appendix). The evidence that it beats a recurrent head is thin: against the stronger fixed-length BGRU the gap is 0.7 points, a 4.5% relative error reduction (inference), from single runs. Under one matched recipe the group later measured MS-TCN 90.0%, BGRU 89.7%, DC-TCN 92.1% [[2]](#ref-2) [later]. Verdict: standard.

### M03 Training: single-stage schedule and variable-length cropping

**Usual approach:** word-boundary indicators are the temporal handling named most often (40 of 156, pattern match), and time masking the common augmentation today (27, all [concurrent] or [later]); prior systems trained in stages [[6]](#ref-6). The paper trains once with a cosine schedule and crops each clip at random points around the word (§4.3, §5.1).

**State of the art:** the [later] matched recipe of [[2]](#ref-2) (2022) reaches 92.1% from scratch on LRW with crop, flip, mixup, time masking and word-boundary indicators (Table 1), against 85.3% here without boundaries or mixup.

No prior study names variable-length cropping (0 prior, 2 [concurrent], 7 [later], pattern match, Appendix); the closest prior removes frames outside known word boundaries [[7]](#ref-7). With five frames removed, the fixed-length BGRU falls from 84.60% to 32.94% and the variable-length one from 82.40% to 68.74% (Table 2), at a full-clip cost the authors concede (§5.3). One dataset, one self-designed perturbation and one run do not meet the repetition rule for ahead (Table 2). The "from scratch" framing (§4.2) also clashes with the adopted 50-hardest-word pretraining. Verdict: standard.

### M12 Evaluation: LRW top-1 accuracy

**Usual approach:** top-1 accuracy on the LRW test set with a ResNet-18 front end and a temporal model, 90 of 155 LRW studies (pattern match). The paper follows it and adds LRW-1000.

**State of the art:** SyncVSR [[3]](#ref-3) [later] (2024), 95.0% with word boundaries and 93.2% without, reported as a mean of three runs.

With no seeds, run count or dispersion (§5.1), the 1.2-point margin over [[5]](#ref-5) and the 0.7-point margin over its own BGRU cannot be separated from run-to-run variance (inference). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | LRW, LRW-1000 broadcast speech | Recorded speech video (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Word-class labels only | Paired-audio targets (slot-filled 31) | – | standard |
| M03 Training and adaptation | One-stage cosine; variable-length crop | Word-boundary indicators (pattern match 40) | [[2]](#ref-2) (2022): 92.1% LRW | standard |
| M04 Use-time action | Overt speech, audio unused | Silent or overt (slot-filled 5,595) | – | standard |
| M05 Sensors | Grayscale 88x88 mouth crop | Camera video (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | Multi-scale dilated TCN | Recurrent back end (pattern match 115) | [[3]](#ref-3) (2024): 93.2% LRW | standard |
| M07 Lexicon and LM | None (closed softmax) | Not recorded (slot-filled 119) | – | standard |
| M08 Output | One word class | Text or class (slot-filled 3,268) | – | standard |
| M09 Confirmation | Offline | Offline (slot-filled 82) | – | not applicable |
| M10 Correction | Offline | Offline (slot-filled 82) | – | not applicable |
| M11 Reference construction | LRW, LRW-1000 labels | Not counted (slot-filled 234) | – | standard |
| M12 Evaluation | LRW, LRW-1000 top-1, one run | LRW test top-1 (pattern match 90) | [[3]](#ref-3) (2024): 95.0% LRW | standard |
| M13 Device and cost | 3 to 1 GPU-weeks; no size | Compute stated (slot-filled 6,075) | – | standard |

## Where the claims outrun the evidence

- The LRW-1000 result (41.4% vs 38.23% for ResNet + LSTM in [[9]](#ref-9)) has no own BGRU baseline, so back end and recipe are confounded (Table 1).
- §5.3 credits the TCN with BGRU-level robustness, yet with five frames removed the TCN keeps 83.8% of its full-clip accuracy and the variable-length BGRU 83.4% (inference). The robustness belongs to the augmentation (Table 2).
- The babble-noise result (6.53% vs 26.21% error at -5 dB, §5.4) names no corpus, split, sample count or noise source (Fig. 2).
- The 3-to-1 GPU-week saving (§1) names no hardware, and no parameters or FLOPs are given, though §5.2 faults [[5]](#ref-5) for heavier compute.

## What the field needs next

- M06: compare temporal heads under one recipe with at least three seeds on LRW and LRW-1000, as [[2]](#ref-2) began with single runs.
- M03: test variable-length cropping against time masking and word-boundary indicators on naturally segmented speech.
- M12: report run-to-run spread, as [[3]](#ref-3) does.

## Questions for the authors

- Which test partitions produced Table 1, and which split selected the checkpoint?
- How were the 50 hardest words taken from [[6]](#ref-6) chosen, and were test-set errors used?
- What does a BGRU trained with your recipe score on LRW-1000?
- What corpus, split and babble source does Fig. 2 use, and how many runs stand behind each Table 2 value?

## Appendix: literature search

- **M06, topic word-lipreading-temporal-backend.** Inclusion rule: studies whose ledger names English LRW or Mandarin LRW-1000 / CAS-VSR-W1K (word-level lip reading), classified by the temporal back end their full text names (recurrent, temporal convolution, Transformer, Conformer); related-work mentions counted (upper bound); versions once. Ledger counts: slot-filled 7,345 unique studies; pattern match 156 unique studies. Usual design: recurrent back end, 115 (pattern match); Transformer 79, temporal convolution 76, Conformer 34. Dated (prior before 2019-07; [concurrent] to 2020-07): population prior 26, [concurrent] 14, [later] 106, date unresolved 14; recurrent prior 24; temporal convolution prior 6 studies; multi-scale TCN prior 0, [concurrent] 2, [later] 38. Read in full: [[6]](#ref-6), [[7]](#ref-7), [[5]](#ref-5), [[2]](#ref-2), [[3]](#ref-3). Known-item recall 1.0 (8 seeds).
- **M03, topic word-lipreading-temporal-augmentation.** Inclusion rule: the same 156-study population, classified by named training-time data handling (variable-length cropping, time masking, frame dropping or jitter, mixup, word-boundary indicators, crop and flip, multi-stage training). Ledger counts: slot-filled 1,526 unique studies; pattern match 156 unique studies. Usual design: word-boundary indicators, 40 (pattern match); time masking 27, mixup 25, frame dropping or jitter 13, variable-length cropping 9. Variable-length cropping prior 0, [concurrent] 2, [later] 7; time masking prior 0; multi-stage training prior 4. Read in full: [[6]](#ref-6), [[7]](#ref-7), [[2]](#ref-2). Known-item recall 1.0 (4 seeds).
- **M12, topic lrw-word-accuracy** (reused published table, appended). Inclusion rule: visual-only word-level lip reading on English LRW with top-1 test accuracy; LRW-1000 excluded; versions once. Ledger counts: slot-filled 6,960 unique studies; pattern match 155 unique studies. Usual design: ResNet-18 front end with a temporal model, 90 (pattern match). Read in full: [[3]](#ref-3). Known-item recall 0.75 (published table).

## References

Numbered by first citation. BibTeX in the same order and keys: [lipreading-using-temporal-convolutional-networks.bib](lipreading-using-temporal-convolutional-networks.bib).

1. <a id="ref-1"></a>Martinez, B., Ma, P., Petridis, S., Pantic, M. “Lipreading using Temporal Convolutional Networks.” *arXiv preprint*, 2020. doi:[10.48550/arXiv.2001.08702](https://doi.org/10.48550/arXiv.2001.08702). arXiv:[2001.08702](https://arxiv.org/abs/2001.08702). Target. Read as arXiv v1. [wiki: arxiv-2001.08702](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2001.08702/article.md)
2. <a id="ref-2"></a>Ma, P., Wang, Y., Petridis, S., Shen, J., Pantic, M. “Training Strategies for Improved Lip-reading.” *arXiv preprint*, 2022. doi:[10.48550/arXiv.2209.01383](https://doi.org/10.48550/arXiv.2209.01383). arXiv:[2209.01383](https://arxiv.org/abs/2209.01383). [later]; same-recipe comparison of temporal heads. [later] [wiki: arxiv-2209.01383](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2209.01383/article.md)
3. <a id="ref-3"></a>Ahn, Y. J., Park, J., Park, S., Choi, J., Kim, K. “SyncVSR: Data-Efficient Visual Speech Recognition with End-to-End Crossmodal Audio Token Synchronization.” *Proc. Interspeech 2024*, 2024. doi:[10.21437/Interspeech.2024-432](https://doi.org/10.21437/Interspeech.2024-432). arXiv:[2406.12233](https://arxiv.org/abs/2406.12233). [later]; state of the art on LRW and CAS-VSR-W1K. [later] [wiki: arxiv-2406.12233](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2406.12233/article.md) [wiki: in24-syncvsr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/in24-syncvsr/article.md)
4. <a id="ref-4"></a>Petridis, S., Stafylakis, T., Ma, P., Cai, F., Tzimiropoulos, G., Pantic, M. “End-to-End Audiovisual Speech Recognition.” *Proc. IEEE ICASSP 2018*, 2018. arXiv:[1802.06424](https://arxiv.org/abs/1802.06424). Prior; the target's baseline [15]. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/end-to-end-audiovisual-speech-recognition) [wiki: arxiv-1802.06424](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1802.06424/article.md)
5. <a id="ref-5"></a>Weng, X., Kitani, K. “Learning Spatio-Temporal Features with Two-Stream Deep 3D CNNs for Lipreading.” *British Machine Vision Conference (BMVC)*, 2019. arXiv:[1905.02540](https://arxiv.org/abs/1905.02540). Prior; best prior LRW result in the target's Table 1 (reference [16]). [wiki: arxiv-1905.02540](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1905.02540/article.md)
6. <a id="ref-6"></a>Stafylakis, T., Tzimiropoulos, G. “Combining Residual Networks with LSTMs for Lipreading.” *Proc. Interspeech 2017*, 2017. doi:[10.21437/Interspeech.2017-85](https://doi.org/10.21437/Interspeech.2017-85). arXiv:[1703.04105](https://arxiv.org/abs/1703.04105). Prior; deciding prior for M06 (temporal-convolution vs BiLSTM back end on LRW); reference [10] of the target. [wiki: arxiv-1703.04105](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1703.04105/article.md) [wiki: isca-stafylakis17_lipread](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-stafylakis17_lipread/article.md)
7. <a id="ref-7"></a>Stafylakis, T., Khan, M. H., Tzimiropoulos, G. “Pushing the boundaries of audiovisual word recognition using Residual Networks and LSTMs.” *Computer Vision and Image Understanding*, 2018. arXiv:[1811.01194](https://arxiv.org/abs/1811.01194). Prior; deciding prior for M06 and M03. [wiki: arxiv-1811.01194](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1811.01194/article.md)
8. <a id="ref-8"></a>Ma, P., Martinez, B., Petridis, S., Pantic, M. “Towards Practical Lipreading with Distilled and Efficient Models.” *Proc. IEEE ICASSP 2021*, 2021. arXiv:[2007.06504](https://arxiv.org/abs/2007.06504). [concurrent]; same group. [concurrent] [wiki: arxiv-2007.06504](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2007.06504/article.md)
9. <a id="ref-9"></a>Yang, S., Zhang, Y., Feng, D., Yang, M., Wang, C., Xiao, J., et al. “LRW-1000: A Naturally-Distributed Large-Scale Benchmark for Lip Reading in the Wild.” *IEEE International Conference on Automatic Face and Gesture Recognition (FG)*, 2019. arXiv:[1810.06990](https://arxiv.org/abs/1810.06990). Prior; source of the LRW-1000 baseline in the target's Table 1 (reference [18]). [wiki: arxiv-1810.06990](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1810.06990/article.md)
