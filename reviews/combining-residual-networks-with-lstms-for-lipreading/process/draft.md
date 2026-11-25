# Combining Residual Networks with LSTMs for Lipreading

Themos Stafylakis, Georgios Tzimiropoulos. Proc. Interspeech 2017, 2017. [doi:10.21437/Interspeech.2017-85](https://doi.org/10.21437/Interspeech.2017-85) [arXiv:1703.04105](https://arxiv.org/abs/1703.04105)

## Verdict

The paper [[1]](#ref-1) changes the processing chain (M06), one 3D convolution layer, a per-frame ResNet-34 and a two-layer Bi-LSTM, and the training recipe (M03), three stages with the word loss at every time step. Both are standard: the LRW benchmark [[2]](#ref-2) is [concurrent] and the ledger holds 0 prior LRW studies (Appendix), so nothing can be behind, and every ablation is one run on one test set, so nothing qualifies as ahead. The design is now the field's default: 106 of 156 LRW / LRW-1000 ledger keys name 3D convolution and a ResNet together, and 115 a recurrent back end (pattern match, Appendix). The main overreach is the Abstract's 6.8-point state-of-the-art margin: the comparator [[3]](#ref-3) [concurrent] was pretrained on extra BBC sentence data, which §2 concedes and the Abstract omits, and §5.1 gives it as 74.2% where §2 and §6 give 76.2%. Today 83.0% sits 10.2 points below SyncVSR [[4]](#ref-4) [later] without word boundaries (inference).

## Against the field, component by component

### M06 Processing: 3D-conv + ResNet front end and Bi-LSTM back end

**Usual approach:** today a 3D convolution followed by a ResNet: 106 of 156 LRW / LRW-1000 ledger keys (pattern match, Appendix), 103 of them among the 149 [later] studies; 115 of 156 name a recurrent back end. At the time there was none: 0 prior studies and 4 [concurrent] ones, none naming a ResNet (Appendix); the benchmark's baselines are VGG-M networks without a recurrent back end [[2]](#ref-2).

**State of the art:** at the time, WAS [[3]](#ref-3) [concurrent], 23.8% word error on LRW (76.2% accuracy) after pretraining on BBC sentences, 6.8 points below the paper's 83.0%. Today SyncVSR [[4]](#ref-4) [later] (2024), 93.2% without word boundaries, mean of three seeds on LRW video only, 10.2 points above (inference); the 2022 recipe [[5]](#ref-5) [later] keeps the 3D convolution plus ResNet encoder.

The parts predate the combination: a prior GRID lipreader chained a feed-forward layer and two LSTM layers on raw mouth images [[6]](#ref-6), and LipNet [[7]](#ref-7) [concurrent] put spatiotemporal convolutions before a bidirectional GRU. The paper adds the ResNet and a 500-word broadcast test. Its 2D-to-3D step (69.6% to 74.6%, +5.0 points, Table 2) runs against the benchmark paper, where whole-network 3D ConvNets trail 2D ones by about 14 points [[2]](#ref-2) [concurrent]; here the 3D layer is one layer in front of a 2D trunk (inference). The ResNet beats a parameter-matched DNN by 4.9 points and the Bi-LSTM beats temporal convolution by 3.8 points (78.4% vs 74.6%, Table 3), but N4 and N5 keep N2's front end frozen (§5.2), so the back-end gain is conditional on it. Verdict: standard; each step is one run with no dispersion.

### M03 Training: three-stage recipe and per-time-step word loss

**Usual approach:** word-boundary indicators are the temporal handling named most often (40 of 156, pattern match), with time masking 27; a word loss applied at every time step is named in 33 keys (the target's 3, 1 [concurrent], 29 [later]; Appendix). The paper trains a temporal-convolution back end, then the Bi-LSTM for 5 epochs on a frozen front end, then end to end (§4.5), with ±5-pixel crops and flips as its only augmentation (§4.1).

**State of the art:** [[5]](#ref-5) [later] (2022) reaches 92.8% on LRW from a single model (93.4% as an ensemble) with word-boundary indicators, self-distillation, mixup and time masking.

The paper leaves out temporal augmentation, although the [concurrent] benchmark paper had already gained 3.5 points of top-1 validation error from random time shifts of up to 0.2 s [[2]](#ref-2). End-to-end fine-tuning adds 1.9 points (79.6% to 81.5%, Table 4); the per-time-step loss has no table row (§4.4). Verdict: standard.

### M12 Evaluation: LRW top-1 accuracy

**Usual approach:** top-1 accuracy on the 25,000-clip LRW test set; 90 of 155 LRW keys name a ResNet-18 front end with a temporal model (pattern match). The paper reports one run.

**State of the art:** SyncVSR [[4]](#ref-4) [later] (2024), 93.2% without and 95.0% with word boundaries, each a mean of three seeds.

LRW splits by broadcast date, not speaker [[2]](#ref-2), so the missing speaker statement (§3) is the benchmark's gap; the paper's own are no seed, run count or checkpoint rule (§4.5). The top confusions in Table 5 are inflection pairs (SPEND to SPENT 26%), errors a closed 500-class score cannot separate (inference). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | LRW broadcast speech video | Inherited LRW lineage | – | standard |
| M02 Training-only supervision | Word-class labels only | Inherited LRW lineage | – | standard |
| M03 Training and adaptation | Three stages; per-step word loss; crop and flip | Word-boundary indicators, LRW n=156 (pattern match 40) | [[5]](#ref-5) (2022): 92.8% LRW (WB) | standard |
| M04 Use-time action | Overt speech, audio unused | Inherited LRW lineage | – | standard |
| M05 Sensors | Grayscale 112x112 mouth crop | Inherited LRW lineage | – | standard |
| M06 Processing and decoding | 3D conv + ResNet-34 + two-layer Bi-LSTM | 3D conv + ResNet front end, LRW n=156 (pattern match 106) | [[4]](#ref-4) (2024): 93.2% LRW | standard |
| M07 Lexicon and LM | None (500-class softmax) | Inherited LRW lineage | – | standard |
| M08 Output | One word class per clip | Inherited LRW lineage | – | standard |
| M09 Confirmation | Offline | Not applicable (offline) | – | not applicable |
| M10 Correction | Offline | Not applicable (offline) | – | not applicable |
| M11 Reference construction | LRW labels, date-based splits | Inherited LRW lineage | – | standard |
| M12 Evaluation | LRW top-1, one run | ResNet-18 front end, LRW n=155 (pattern match 90) | [[4]](#ref-4) (2024): 93.2% LRW (no WB) | standard |
| M13 Device and cost | One 12 GB GPU | Not compared | – | standard |

## Where the claims outrun the evidence

- The comparator is 74.2% in §5.1 but 76.2% in §2 and §6 (arXiv v4 gives 76.2% in §5.1). WAS reached 23.8% word error after sentence pretraining and one epoch of LRW fine-tuning [[3]](#ref-3); §2 concedes the extra training resources, the Abstract does not.
- The per-time-step loss gain (about 3 points) has no table or run count (§4.4).
- Concatenation over addition (83.0% vs 81.5%, Table 4) is a 1.5-point single-run difference (inference).

## What the field needs next

- M06: repeat the 2D-versus-3D and recurrent-versus-temporal-convolution comparisons with several seeds, on a second word-level set, all trained end to end.
- M03: add temporal augmentation (time shifts, time masking) and report the per-time-step loss as a table row.
- M12: report run-to-run spread and a score that separates inflection errors from other confusions.

## Questions for the authors

- How many runs, with which seeds, stand behind Tables 2 to 4, and which validation metric selected the checkpoint?
- Why does §5.1 give 74.2% for WAS where §6 gives 76.2%?
- What does a Bi-LSTM trained end to end from scratch score?

## Appendix: literature search

Dating for all topics: target first public 2017-03 (arXiv v1); prior before 2016-09, [concurrent] 2016-09 to 2017-09, [later] after. The target has three ledger keys among the 156.

- **M06, topic word-lipreading-visual-frontend** (new). Inclusion rule: studies whose ledger names English LRW or Mandarin LRW-1000 / CAS-VSR-W1K (word-level lip reading), classified by the visual front end their full text names (3D convolution, ResNet, VGG, ViT or patch transformer); related-work mentions counted (upper bound); versions once by key. Ledger counts: slot-filled 7,345 unique studies; pattern match 156 unique studies. Usual design: 3D convolution and ResNet both named, 106 (pattern match): the target's 3 keys, prior 0, [concurrent] 0 of 4, [later] 103 of 149. 3D convolution 122, ResNet 124, VGG 64, ViT 13. Read in full: [[6]](#ref-6), [[2]](#ref-2), [[7]](#ref-7), [[3]](#ref-3), [[4]](#ref-4), [[5]](#ref-5). Known-item recall 1.0 (8 seeds).
- **M06, topic word-lipreading-temporal-backend** (reused published table, appended). Inclusion rule: the same population, classified by the temporal back end named (recurrent, temporal convolution, Transformer, Conformer). Ledger counts: slot-filled 7,345 unique studies; pattern match 156 unique studies. Usual design: recurrent back end, 115 (pattern match). Dated against 2017-03: prior 0, [concurrent] 4, [later] 149. Read in full: [[6]](#ref-6), [[7]](#ref-7), [[3]](#ref-3), [[2]](#ref-2). Known-item recall 1.0 (8 seeds).
- **M03, topic word-lipreading-temporal-augmentation** (reused published table, appended). Inclusion rule: the same population, classified by named training-time data handling (temporal cropping, time masking, frame dropping, mixup, word-boundary indicators, crop and flip, multi-stage training). Ledger counts: slot-filled 1,526 unique studies; pattern match 156 unique studies. Usual design: word-boundary indicators, 40 (pattern match); time masking 27. Word loss at every time step (added pattern): 33, of which the target's 3, prior 0, [concurrent] 1, [later] 29. Read in full: [[2]](#ref-2), [[5]](#ref-5). Known-item recall 1.0 (4 seeds).
- **M12, topic lrw-word-accuracy** (reused published table, appended). Inclusion rule: visual-only word-level lip reading on English LRW with top-1 test accuracy; LRW-1000 excluded; versions once. Ledger counts: slot-filled 6,960 unique studies; pattern match 155 unique studies. Usual design: ResNet-18 front end with a temporal model, 90 (pattern match). Read in full: [[4]](#ref-4), [[3]](#ref-3), [[2]](#ref-2). Known-item recall 0.75.

## References

Numbered by first citation. BibTeX in the same order and keys: [combining-residual-networks-with-lstms-for-lipreading.bib](combining-residual-networks-with-lstms-for-lipreading.bib).

1. <a id="ref-1"></a>Stafylakis, T., Tzimiropoulos, G. “Combining Residual Networks with LSTMs for Lipreading.” *Proc. Interspeech 2017*, 2017. doi:[10.21437/Interspeech.2017-85](https://doi.org/10.21437/Interspeech.2017-85). arXiv:[1703.04105](https://arxiv.org/abs/1703.04105). Target. Read as the ISCA Interspeech 2017 proceedings version; arXiv v4 consulted for Sec. 5.1. [wiki: isca-stafylakis17-resnetlstm](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-stafylakis17-resnetlstm/article.md) [wiki: arxiv-1703.04105](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1703.04105/article.md) [wiki: isca-stafylakis17_lipread](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-stafylakis17_lipread/article.md) [wiki: isca-stafylakis17_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-stafylakis17_interspeech/article.md)
2. <a id="ref-2"></a>Chung, J. S., Zisserman, A. “Lip Reading in the Wild.” *Asian Conference on Computer Vision (ACCV)*, 2016. doi:[10.1007/978-3-319-54184-6_6](https://doi.org/10.1007/978-3-319-54184-6_6). [concurrent]; the LRW benchmark and its VGG-M baselines; deciding paper for M06 and M03. [concurrent] [wiki: w2594690981-lrw](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/w2594690981-lrw/article.md)
3. <a id="ref-3"></a>Chung, J. S., Senior, A., Vinyals, O., Zisserman, A. “Lip Reading Sentences in the Wild.” *IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2017. doi:[10.1109/CVPR.2017.367](https://doi.org/10.1109/CVPR.2017.367). arXiv:[1611.05358](https://arxiv.org/abs/1611.05358). [concurrent]; the target's state-of-the-art comparator on LRW. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lip-reading-sentences-in-the-wild) [wiki: arxiv-1611.05358](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1611.05358/article.md) [wiki: cvf-chung17-lipreadwild](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-chung17-lipreadwild/article.md)
4. <a id="ref-4"></a>Ahn, Y. J., Park, J., Park, S., Choi, J., Kim, K. “SyncVSR: Data-Efficient Visual Speech Recognition with End-to-End Crossmodal Audio Token Synchronization.” *Proc. Interspeech 2024*, 2024. doi:[10.21437/Interspeech.2024-432](https://doi.org/10.21437/Interspeech.2024-432). arXiv:[2406.12233](https://arxiv.org/abs/2406.12233). [later]; state of the art on LRW. [later] [wiki: arxiv-2406.12233](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2406.12233/article.md) [wiki: in24-syncvsr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/in24-syncvsr/article.md)
5. <a id="ref-5"></a>Ma, P., Wang, Y., Petridis, S., Shen, J., Pantic, M. “Training Strategies for Improved Lip-reading.” *arXiv preprint*, 2022. doi:[10.48550/arXiv.2209.01383](https://doi.org/10.48550/arXiv.2209.01383). arXiv:[2209.01383](https://arxiv.org/abs/2209.01383). [later]; state of the art for the LRW training recipe. [later] [wiki: arxiv-2209.01383](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2209.01383/article.md)
6. <a id="ref-6"></a>Wand, M., Koutník, J., Schmidhuber, J. “Lipreading with Long Short-Term Memory.” *Proc. IEEE ICASSP 2016*, 2016. doi:[10.1109/ICASSP.2016.7472852](https://doi.org/10.1109/ICASSP.2016.7472852). arXiv:[1601.08188](https://arxiv.org/abs/1601.08188). Prior; LSTM back end on raw mouth images (GRID, speaker-dependent). [wiki: arxiv-1601.08188](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1601.08188/article.md) [wiki: doi-10.1109-icassp.2016.7472852](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-icassp.2016.7472852/article.md)
7. <a id="ref-7"></a>Assael, Y. M., Shillingford, B., Whiteson, S., de Freitas, N. “LipNet: End-to-End Sentence-level Lipreading.” *arXiv preprint*, 2016. doi:[10.48550/arXiv.1611.01599](https://doi.org/10.48550/arXiv.1611.01599). arXiv:[1611.01599](https://arxiv.org/abs/1611.01599). [concurrent]; spatiotemporal convolution with a bidirectional GRU (GRID). [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lipnet-end-to-end-sentence-level-lipreading) [wiki: arxiv-1611.01599](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1611.01599/article.md)
