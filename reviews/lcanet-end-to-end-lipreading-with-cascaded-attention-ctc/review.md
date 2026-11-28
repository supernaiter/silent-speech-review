# LCANet: End-to-End Lipreading with Cascaded Attention-CTC

Xu, K., Li, D., Cassimatis, N., Wang, X. · IEEE FG · 2018 · [arXiv:1803.04988](https://arxiv.org/abs/1803.04988)

## Verdict

LCANet [[1]](#ref-1) changes one component, the decoder (M06): an attention layer placed before a single CTC loss, plus highway layers in the encoder. The design is new in lip reading (Appendix: no cascade or hybrid among the 57 sentence-level decoder studies before 2018-03, and none in a whole-wiki check to 2018-09), but it is standard, not ahead: one corpus, one run, no seeds (Sec. 4.C), and an ablation that cannot separate attention from CTC (Table II). The headline comparison over LipNet holds on GRID with overlapping speakers, 2.9% against 4.8% WER (Table III), and more clearly against LipNet without its language model, 5.6% [[2]](#ref-2); the comparison with LRSW does not, because Table III puts that system's 3.0% WER in the CER column [[3]](#ref-3). The multi-task baseline, ranked last at 4.9%, is the design the later best result under the same protocol uses [[4]](#ref-4). M12 is standard: the comparators' overlapped split, no unseen-speaker result.

## Against the field, component by component

### M06 Decoding: attention cascaded into a single CTC loss

**Usual approach:** Of the 57 sentence-level lip-reading decoder studies first public before 2018-03, 56 mention HMMs; the 5 neural ones train one loss, CTC in 4 (one [concurrent]) and attention in 1 [[3]](#ref-3) (pattern match, read, Appendix). None names a hybrid or cascade (Appendix). The authors' stated precedent, from audio ASR [[5]](#ref-5), trains a shared encoder on CTC and attention losses jointly; cascading avoids tuning the loss weight (Sec. 2.A).

**State of the art:** on the same GRID protocol, 1.83% WER without an external language model, from a hybrid CTC/attention model with the joint loss LCANet ranked last (2024, [later]) [[4]](#ref-4), 37% below LCANet's 2.9% (inference); on open vocabulary, 17.6% LRS3 visual-only WER with hybrid CTC/attention (2026, [later]) [[6]](#ref-6).

The ablation does not show what the cascade adds. A-CTC, called "the attention-only model" (Sec. 4.D), still trains on CTC alone (Table II), so no attention-only decoder is tested; WAS is that reference [[3]](#ref-3). Attention given highway layers lowers WER from 4.3% to 2.9% (H-CTC to LCANet, Table III), 33% relative (inference), from one run each. The joint-loss comparator, AH-CTC-CE at 4.9%, is worse than the CTC-only H-CTC at 4.3%, whereas the ASR joint model it follows outperformed both CTC and attention, best at λ = 0.2 [[7]](#ref-7); the λ chosen and the data that chose it are not stated (Sec. 4.C). The [concurrent] [[8]](#ref-8) trains CTC and attention back ends separately. Verdict: standard; new, but one corpus and one run, and the later field kept the joint loss.

### M12 Evaluation: GRID with overlapping speakers, one run

**Usual approach:** Of 14 GRID decoder studies before 2018-03, 8 name an overlapped-speaker and 7 an unseen-speaker split, 6 name a variability or significance measure, and none names seeds or repeated runs (pattern match, mentions, Appendix). LCANet follows the random 255-sentence-per-speaker split of its two comparators (Sec. 4.A), the overlapped split of [[2]](#ref-2) and the protocol of [[3]](#ref-3).

**State of the art:** 1.83% overlapped and 10.21% unseen-speaker WER from one model (2024, [later]) [[4]](#ref-4).

The like-for-like comparator is LipNet's overlapped row, 4.8% with a character 5-gram model and 5.6% without it [[2]](#ref-2); LCANet describes no language model (Fig. 2), so the gain over the LM-free row is 48% relative (inference). The paper does not state whether test speakers appear in training (Sec. 4.A), and gives no unseen-speaker result, the setting where LipNet's WER is 11.4% against 4.8% [[2]](#ref-2). No seeds, runs or intervals are given (Sec. 4.C), and the 255 sentences are a fresh random draw, so a 0.1-point gap to WAS is within redraw noise (inference). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training action | Overt GRID sentences | Overt speech | – | standard |
| M02 Supervision | Character transcripts; augmentation | Transcript labels | – | standard |
| M03 Training/adaptation | Scratch on GRID; one run | Supervised training | – | standard |
| M04 Use-time action | Overt speech video | Overt speech video | – | standard |
| M05 Sensors | RGB camera, 100x50 mouth crop | Mouth crop | – | standard |
| M06 Decoding | 3D-CNN, highway, Bi-GRU; attention cascaded into CTC | CTC: 4 of 5 neural decoders, 57 studies before 2018-03 (pattern match 4) | [[4]](#ref-4) 1.83% GRID overlapped | standard |
| M07 Lexicon/LM | Not stated | Grammar, lexicon or LM | – | not reported |
| M08 Output | Character transcript | Text | – | standard |
| M09 Confirmation | None | Mostly absent | – | not applicable |
| M10 Correction | None | Mostly absent | – | not applicable |
| M11 Reference | GRID prompts; own random draw | Benchmark splits | – | standard |
| M12 Evaluation | CER/WER/BLEU; overlapped speakers; one run | Overlapped split named: 8 of 14 GRID decoders before 2018-03 (pattern match 8) | [[4]](#ref-4) 1.83% overlapped, 10.21% unseen | standard |
| M13 Device/cost | Offline GPU; no latency | Offline benchmark | – | not applicable |

## Where the claims outrun the evidence

- Table III lists LRSW as "3.0" under CER with WER blank, but the source reports 3.0% as GRID word error rate, after one epoch of fine-tuning from LRS [[3]](#ref-3). "Our method still achieves better CER and WER" (Sec. 4.D) therefore rests on 2.9% against 3.0% WER, one run each; no GRID CER exists for that system.
- The abstract gives 3.0% WER, Table III 2.9%; the stated 37.5% WER gain over LipNet (Sec. 4.D) matches 3.0 (inference). The 12.3% gain over "the state-of-the-art methods" names no metric or comparator (Abstract). The highway gain is stated as 1.1 points (Sec. 4.D), Table III gives 4.1 against 2.9, 1.2 points (inference).
- The authors' explanation for the weak multi-task variant, that "only the shared encoder is jointly updated" (Sec. 4.D), is untested; the best λ of 0.1 to 0.9 has no named selection split (Sec. 4.C).
- Faster convergence is claimed for the cascade (Abstract, Sec. 4.E), but joint CTC-attention training was already reported to converge early [[7]](#ref-7), and the curves compare against LipNet, not against LCANet's own variants (Fig. 6).
- Cross-viseme confusion is called "not statistically significant" without a test (Sec. 4.F).
- The authors concede that the CTC loss itself is not modified (Sec. 5).

## What the field needs next

- M06: cascade, joint loss and CTC-only on one encoder, λ swept on validation data including 0 and 1, three or more seeds, on GRID and an open-vocabulary corpus.
- M12: unseen-speaker GRID results, a released overlapped test list and seed spread, so that gaps such as 2.9% against 3.0% can be read.

## Questions for the authors

- Which split selected λ and the early-stopping checkpoint?
- Were the decoded outputs produced with any language model, lexicon or GRID grammar constraint?
- What is the source of the LRSW CER of 3.0, and of the 12.3%?
- What is the WER spread over seeds, and what is the unseen-speaker WER?

## Appendix: literature search

- Setting, the same for both topics: sentence-level lip reading, visual or audio-visual (the 633-study population of the published M06 table), and its GRID subset (the 93-study population of the published M12 table), dated at the target's arXiv v1, 2018-03; [concurrent] 2017-09 to 2018-09. Counts are full-text pattern matches, mentions included, unless marked read.
- M06, sentence-lipreading-sequence-objective (published table, appended). Inclusion rule: the published rule (sentence-level or open-vocabulary speech from lip or face video, classified by the sequence objective the full text names). Ledger counts: 7,345 unique studies slot-filled for M06; 633 unique studies pattern match. Before 2018-03: 89 unique studies, minus 29 perception or neuroscience studies, 1 review, 1 enhancement study and 1 version duplicate, gives 57 decoder studies. Mentions among the 57: HMM 56, CTC 6, attention or sequence-to-sequence 2, hybrid or joint CTC/attention 0, highway network 0. Designs after reading the snippets: CTC 4 (arxiv-1611.01599, arxiv-1611.02879, arxiv-1611.06986, arxiv-1802.05521 [concurrent]), attention 1 ([[3]](#ref-3)); one CTC hit is a reference-list mention in a DNN-HMM system. Recall check over 2,615 wiki studies with text first public before 2018-09: 6 hits, the target, the [concurrent] [[8]](#ref-8) (separate CTC and attention back ends), and 4 mentions or citations; 0 other cascade designs. Read: [[2]](#ref-2), [[3]](#ref-3) (prior); [[7]](#ref-7), [[5]](#ref-5) (prior, audio ASR, outside the wiki); [[8]](#ref-8) ([concurrent]); [[4]](#ref-4), [[6]](#ref-6) (state of the art). Known-item recall 1.0 (published table).
- M12, grid-sentence-lipreading-protocol (published table, appended). Inclusion rule: the published rule (GRID lip-reading or VSR decoders classified by the evaluation partition the full text names, with a variability or significance regex), plus a seeds or repeated-runs regex. Ledger counts: 6,960 unique studies slot-filled for M12; 93 unique studies pattern match. Before 2018-03: 24 unique keys, minus 2 LRW-only, 2 enhancement and 1 statistics study and 5 version duplicates, gives 14 decoder studies, all prior. Mentions among the 14: overlapped-speaker split 8, unseen-speaker split 7, variability or significance 6, seeds or repeated runs 0. Later studies stating the same 255-per-speaker protocol: 4, including [[4]](#ref-4). Read: [[2]](#ref-2), [[3]](#ref-3) (prior); [[4]](#ref-4) (state of the art). Known-item recall 1.0 (published table).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Xu, K., Li, D., Cassimatis, N., Wang, X. “LCANet: End-to-End Lipreading with Cascaded Attention-CTC.” *IEEE International Conference on Automatic Face and Gesture Recognition (FG)*, 2018, 548-555. arXiv:[1803.04988](https://arxiv.org/abs/1803.04988). First public as arXiv:1803.04988v1 (13 Mar 2018). [wiki: arxiv-1803.04988](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1803.04988/article.md)
2. <a id="ref-2"></a>Assael, Y. M., Shillingford, B., Whiteson, S., de Freitas, N. “LipNet: End-to-End Sentence-level Lipreading.” *arXiv preprint*, 2016. arXiv:[1611.01599](https://arxiv.org/abs/1611.01599). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lipnet-end-to-end-sentence-level-lipreading) [wiki: arxiv-1611.01599](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1611.01599/article.md)
3. <a id="ref-3"></a>Chung, J. S., Senior, A., Vinyals, O., Zisserman, A. “Lip Reading Sentences in the Wild.” *IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2017. doi:[10.1109/CVPR.2017.367](https://doi.org/10.1109/CVPR.2017.367). arXiv:[1611.05358](https://arxiv.org/abs/1611.05358). The LRSW comparator of the target's Table III. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lip-reading-sentences-in-the-wild) [wiki: arxiv-1611.05358](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1611.05358/article.md) [wiki: cvf-chung17-lipreadwild](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-chung17-lipreadwild/article.md)
4. <a id="ref-4"></a>Wu, L., Zhang, X., Zhang, Y., Zheng, C., Liu, T., Xie, L., et al. “Landmark-Guided Cross-Speaker Lip Reading with Mutual Information Regularization.” *arXiv preprint*, 2024. arXiv:[2403.16071](https://arxiv.org/abs/2403.16071). GRID overlapped-speaker WER under the target's 255-per-speaker protocol, hybrid CTC/attention, no external LM. [later] [wiki: arxiv-2403.16071](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2403.16071/article.md)
5. <a id="ref-5"></a>Hori, T., Watanabe, S., Hershey, J. R. “Joint CTC/attention decoding for end-to-end speech recognition.” *Annual Meeting of the Association for Computational Linguistics (ACL)*, 2017. doi:[10.18653/v1/P17-1048](https://doi.org/10.18653/v1/P17-1048). Audio ASR; the target's reference [43] and the source of its multi-task comparator.
6. <a id="ref-6"></a>Haliassos, A., Mira, R., Petridis, S. “Pay Attention to CTC: Fast and Robust Pseudo-Labelling for Unified Speech Recognition.” *International Conference on Learning Representations (ICLR)*, 2026. arXiv:[2602.19316](https://arxiv.org/abs/2602.19316). [later] [wiki: arxiv-2602.19316](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.19316/article.md)
7. <a id="ref-7"></a>Kim, S., Hori, T., Watanabe, S. “Joint CTC-Attention Based End-to-End Speech Recognition Using Multi-Task Learning.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2017. arXiv:[1609.06773](https://arxiv.org/abs/1609.06773). Audio ASR; joint CTC-attention multi-task training, not cited by the target.
8. <a id="ref-8"></a>Afouras, T., Chung, J. S., Zisserman, A. “Deep Lip Reading: a comparison of models and an online application.” *Proc. Interspeech 2018*, 2018. arXiv:[1806.06053](https://arxiv.org/abs/1806.06053). [concurrent] [wiki: arxiv-1806.06053](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1806.06053/article.md) [wiki: isca-afouras18b-deeplip](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-afouras18b-deeplip/article.md) [wiki: isca-afouras18b_deeplipread](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-afouras18b_deeplipread/article.md) [wiki: isca-afouras18b_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-afouras18b_interspeech/article.md)
