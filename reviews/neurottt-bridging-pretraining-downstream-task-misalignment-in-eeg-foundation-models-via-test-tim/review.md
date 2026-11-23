# NeuroTTT: Bridging Pretrain–Downstream Task Misalignment in EEG Foundation Models via Test-Time Training

Wang S, Deng Y, Bao Z, Zhan X, Duan Y. arXiv, 2025. [arXiv:2509.26301](https://arxiv.org/abs/2509.26301)

## Verdict

NeuroTTT [[1]](#ref-1) changes two components of EEG foundation-model fine-tuning: self-supervised losses added during training (M02) and unlabeled test-time updates (M03). Both are standard. The M02 design is rare in the ledger (Appendix), but its effect appears only in a CBraMod figure without numbers in the text (Fig. 3). The proposed self-supervised test-time step never beats off-the-shelf Tent on balanced accuracy (Tables 1–3). The state-of-the-art claim rests on internal baselines: on imagined speech the best balanced accuracy, 0.5898, is 23.6 points below the 82.6% competition winner on the same corpus [[2]](#ref-2) (inference). Test-time cost is not reported (M13).

## Against the field, component by component

### M02 Training-only supervision: self-supervised losses during fine-tuning

**Usual approach:** Of 40 unique ledger studies that fine-tune a neural foundation model (pattern match, Appendix), 37 show no added self-supervised loss, and the band, jigsaw and flip pretext tasks match only the target. The paper trains stopped-band prediction plus one task transform jointly with the task loss (Sec. 3.1).

**State of the art:** The two other studies with an added loss are [later] (2026; Appendix); the reference point is the paper's own MLP-head row, 0.4733 balanced accuracy on BCIC2020-III (Table 1).

Every "TTT" row is Stage I plus a test-time method (Sec. 4.1); Stage I alone appears only in Fig. 3. Imagined-speech runs with the added losses train 150 epochs against 100 for supervised runs (Sec. 4.1), so length and objective are confounded. Verdict: standard.

### M03 Adaptation: self-supervised test-time training and Tent

**Usual approach:** Among 38 unique studies of unlabeled use-time adaptation (pattern match, Appendix), pseudo-label self-training is named in 11, entropy minimization in 6 and self-supervised test-time training in 6, both counts including the target and a [concurrent] sEEG decoder using entropy minimization [[3]](#ref-3).

**State of the art:** On the same corpus a [later] benchmark (2026) fine-tunes LaBraM-Base to 27.7% balanced accuracy, 30.2% at best, on the official validation split [[4]](#ref-4), level with the paper's LaBraM rows (0.2720, 0.2742; Table 1).

With the same Stage-I model, Tent exceeds the self-supervised step on CBraMod (0.5898 vs 0.5887 speech, 0.7280 vs 0.7196 stress, 0.5674 vs 0.5435 motor imagery) and on LaBraM (0.2742 vs 0.2720, 0.7269 vs 0.7161, 0.45110 vs 0.43835; Tables 1–3), as the authors note (Sec. 4.2). On speech the authors call the TTT effect modest (Sec. 4.3), so most of the 11.7-point lead over the MLP row is Stage I (inference). SHOT starts from a classifier trained on a fixed backbone (Appendix B.4). Verdict: standard.

### M12 Evaluation: BCIC2020-III and external comparison

**Usual approach:** Of 16 unique ledger studies on this corpus (pattern match, Appendix), 10 use a subject-independent term and 4 cross-validation. The paper tests within subject on the competition split, cross-subject runs being at chance (Appendix B.1).

**State of the art:** The 2020 competition winner (2022) reached 82.6% on the released test data, 10 trials per class [[2]](#ref-2); with balanced classes, accuracy equals balanced accuracy, so the paper's best is 23.6 points (29% relative) lower (inference).

The paper keeps the competition splits "for consistency with prior work" (Appendix B.1) but tabulates no prior result. Cross-subject gains rest on test subjects 8–9 (motor imagery) and 33–36 (stress), with no seed count, no definition of ± and no significance test (Secs. 4.1–4.2). Verdict: standard.

### M13 Operating cost: per-sample updates of a full backbone

**Usual approach:** Of 64 unique ledger studies tying use-time adaptation or inference to cost (pattern match, Appendix), 22 report memory or FLOPs and 19 a latency in ms. The paper calls Stage I free at deployment (Sec. 1) but gives no figure for one Adam step per test sample through the whole model (Table 7).

**State of the art:** A [concurrent] decoder (2025) adapts to a new session by updating under 1% of its parameters and infers at about 2.44 ms per chunk on a CPU [[5]](#ref-5). Verdict: not reported.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Benchmark task recordings | Recorded task protocol (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Band-stop and task SSL losses in fine-tuning | Task-label loss only (pattern match 37) | – | standard |
| M03 Training and adaptation | SSL test-time step per sample, or Tent | Pseudo-label self-training (pattern match 11) | [[4]](#ref-4) (2026): 30.2% BAcc, same corpus | standard |
| M04 Use-time action | Offline benchmark trials | Overt or silent production (slot-filled 5,595) | – | standard |
| M05 Sensors | Existing scalp EEG | Scalp EEG (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | CBraMod, LaBraM-Base, linear/MLP head | Model per task (slot-filled 7,345) | – | standard |
| M07 Lexicon and LM | None | None (slot-filled 119) | – | not applicable |
| M08 Output | Class labels | Class labels (slot-filled 3,268) | – | standard |
| M09 Confirmation | Offline | None (slot-filled 82) | – | not applicable |
| M10 Correction | Offline | None (slot-filled 82) | – | not applicable |
| M11 Reference construction | Corpus labels and splits | Corpus labels (slot-filled 234) | – | standard |
| M12 Evaluation | Within-subject speech; 2-4 test subjects | Subject-independent terms (pattern match 10) | [[2]](#ref-2) (2022): 82.6% | standard |
| M13 Device and cost | Not reported | Memory or FLOPs reported (pattern match 22) | [[5]](#ref-5) (2025): <1% parameters adapted | not reported |

## Where the claims outrun the evidence

- "State-of-the-art performance" (Abstract; Sec. 5) is internal; 82.6% on the same data predates it [[2]](#ref-2).
- "Markedly higher" (Abstract) fails for LaBraM on speech: 0.2742 against 20% chance (Table 1; chance from [[4]](#ref-4)).
- The public motor-imagery loader builds validation from the test subjects while checkpoints are selected on validation kappa, and the test-time script uses SGD and five steps where Table 7 states Adam and one step (code).

## What the field needs next

- M03: Tent, self-supervised TTT and pseudo-labels on one fixed Stage-I model, with seeds and per-subject paired tests.
- M02: Stage I against supervised fine-tuning at matched epochs, both backbones, with numbers.
- M12: BCIC2020-III results beside the competition's; leave-one-subject-out for stress and motor imagery.
- M13: per-sample adaptation latency and memory on wearable-class hardware.

## Questions for the authors

- How many seeds underlie Tables 1–3, and what does ± denote?
- Which BCIC2020-III trials are validation and test, and whose test labels were used?
- Was the Table 3 checkpoint selected on subjects 6–7 or on the test subjects?
- What are the Fig. 3 values without test-time adaptation, and for LaBraM?

## Appendix: literature search

- M02, auxiliary-ssl-loss-in-neural-fine-tuning (new). Inclusion rule: neural-signal decoders that start from a checkpoint pretrained on large neural corpora and add a training-only self-supervised loss to supervised fine-tuning; pretraining-only objectives and use-time updates excluded; versions once; full-text hits are an upper bound. Ledger: 31 unique studies slot-filled for M02; 40 unique studies pattern match (neural foundation-model population). Self-supervised loss added to fine-tuning 3 unique studies (the target and two [later] 2026 studies); domain-specific pretext task (stopped band, temporal jigsaw, A–P flip) 1 (the target); remainder 37 (pattern match).
- M03, unlabeled-test-time-adaptation (new). Inclusion rule: decoders of speech-related or neural signals that update weights or normalization state from unlabeled test data (self-supervised test-time training, entropy minimization, pseudo-label self-training, source-free adaptation); training-only losses, labeled recalibration and update-free test-time augmentation excluded; versions once. Ledger: 1,526 unique studies slot-filled for M03; 26 unique studies pattern match in the ledger, 38 with full-text hits. Pseudo-label self-training 11, entropy minimization 6, self-supervised test-time training 6, unsupervised re-centering 1 (pattern match). Read in full: [[3]](#ref-3), [[4]](#ref-4).
- M12, bci2020-imagined-speech-benchmark (published table, reused). Inclusion rule: studies reporting classification on the 2020 International BCI Competition Track 3 imagined-speech data, classified by the test data scored; citation-only papers are pattern matches; versions once. Ledger: 6,960 unique studies slot-filled for M12; 16 unique studies pattern match. Subject-independent or cross-subject term 10, k-fold cross-validation 4 (pattern match, published counts). Read in full: [[2]](#ref-2) and two earlier same-corpus studies (published table). Known-item recall 0.33.
- M13, use-time-adaptation-cost (new). Inclusion rule: speech-related or neural-signal decoders whose text ties test-time adaptation or inference to latency, runtime, memory, compute, power or wearability; training-only cost excluded; unmeasured privacy or edge claims are pattern matches only. Ledger: 6,075 unique studies slot-filled for M13; 64 unique studies pattern match. Memory or FLOPs reported 22, latency in ms reported 19, embedded or edge device named 12 (pattern match). Read in full: [[5]](#ref-5) and one EEG edge-latency study.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Wang, S., Deng, Y., Bao, Z., Zhan, X., Duan, Y. “NeuroTTT: Bridging Pretrain–Downstream Task Misalignment in EEG Foundation Models via Test-Time Training.” *arXiv preprint*, 2025. doi:[10.48550/arXiv.2509.26301](https://doi.org/10.48550/arXiv.2509.26301). arXiv:[2509.26301](https://arxiv.org/abs/2509.26301). Target. Read as arXiv v2. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/neurottt-bridging-pretraining-downstream-task-misalignment-in-eeg-foundation-models-via-test-tim) [wiki: arxiv-2509.26301](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2509.26301/article.md) [wiki: arxiv-2509-26301-neurottt](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2509-26301-neurottt/article.md)
2. <a id="ref-2"></a>Jeong, J., Cho, J., Lee, Y., Lee, S., Shin, G., Kweon, Y., et al. “2020 International Brain-Computer Interface Competition: A Review.” *Frontiers in Human Neuroscience*, 2022, 16, 898300. doi:[10.3389/fnhum.2022.898300](https://doi.org/10.3389/fnhum.2022.898300). Prior; state of the art for M12 (Track 3 imagined speech). [wiki: pmc-9354666-bcicomp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-9354666-bcicomp/article.md) [wiki: doi-10.3389-fnhum.2022.898300](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnhum.2022.898300/article.md) [wiki: pmc-9354666-bci2020](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-9354666-bci2020/article.md)
3. <a id="ref-3"></a>Wang, S., Li, Y., Cai, S., Li, H. “A Robust Multi-Scale Framework with Test-Time Adaptation for sEEG-Based Speech Decoding.” *arXiv preprint*, 2025. arXiv:[2509.24700](https://arxiv.org/abs/2509.24700). Tent on sEEG word decoding. [concurrent] [wiki: arxiv-2509.24700](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2509.24700/article.md)
4. <a id="ref-4"></a>Khanday, O. M., Ben Ticha, M. B., Belfrouh, S., Ouellet, M., Gonzalez-Lopez, J. A. “Do EEG Foundation Models Transfer to Speech? A Benchmark on Overt and Imagined Speech Decoding.” *arXiv preprint*, 2026. doi:[10.48550/arXiv.2607.27268](https://doi.org/10.48550/arXiv.2607.27268). arXiv:[2607.27268](https://arxiv.org/abs/2607.27268). neural-checkpoint benchmark on the same BCIC2020-T3 data. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/do-eeg-foundation-models-transfer-to-speech-a-benchmark-on-overt-and-imagined-speech-decoding) [wiki: arxiv-2607.27268](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2607.27268/article.md) [wiki: arxiv-2607-27268-eegfm](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2607-27268-eegfm/article.md) [wiki: arxiv-2607-27268-eegfmspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2607-27268-eegfmspeech/article.md)
5. <a id="ref-5"></a>Ryoo, A. H., Krishna, N. H., Mao, X., Azabou, M., Dyer, E. L., Perich, M. G., et al. “Generalizable, real-time neural decoding with hybrid state-space models.” *Advances in Neural Information Processing Systems (NeurIPS 2025)*, 2025. arXiv:[2506.05320](https://arxiv.org/abs/2506.05320). adaptation share and inference latency for M13. [concurrent] [wiki: arxiv-2506.05320](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2506.05320/article.md)
