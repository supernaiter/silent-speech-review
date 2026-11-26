# Audio-Visual Speech Recognition with a Hybrid CTC/Attention Architecture

Stavros Petridis, Themos Stafylakis, Pingchuan Ma, Georgios Tzimiropoulos, Maja Pantic. SLT 2018. [doi:10.1109/SLT.2018.8639643](https://doi.org/10.1109/SLT.2018.8639643) [arXiv:1810.00108](https://arxiv.org/abs/1810.00108)

## Verdict

The paper [[1]](#ref-1) changes one component, M06, and it is standard: none of the 32 earlier sentence-level AVSR studies in the ledger trains a hybrid CTC/attention objective (Appendix), but the paper runs neither CTC-only nor attention-only on LRS2 (Sec. 5.4, Table 2), so the objective's share of its 7.0% WER is unmeasured. The concurrent GRID study [[2]](#ref-2) found a jointly trained CTC plus attention variant worse than a single-loss cascade (4.9% against 2.9% WER, Table III); this paper does not settle the question. The strongest overreach is the "trained only on LRS2" framing: the visual front end is pretrained on LRW (Sec. 5.1) and the language model reads 9.4 million LibriSpeech words (Sec. 5.3), with no LM-free result. M07 and M12 are standard: a neural LM where 28 of 32 earlier studies name none, and a one-run noise sweep, as in 20 of 32 (Appendix).

## Against the field, component by component

### M06 Processing: hybrid CTC/attention objective and joint decoding

**Usual approach:** All 32 sentence-level AVSR studies in the ledger dated before 2018-09 name HMMs (pattern match, mentions included, Appendix); the neural ones train one loss, CTC in [[3]](#ref-3) or attention in WLAS [[4]](#ref-4). None of the 32 trains a hybrid CTC/attention objective (Appendix). The authors credit the objective to acoustic ASR and the GRID cascade [[2]](#ref-2) (Sec. 1); the concurrent [[5]](#ref-5) trains CTC and seq2seq separately (Sec. 1).

**State of the art:** The same objective with a Conformer encoder and 3,448 hours gives 1.5% LRS2 AVSR WER and 14.6% visual-only (2023) [[6]](#ref-6) [later], against 7.0% and 63.5% here (Table 2), 79% and 77% lower (inference).

At the same 380 hours, CM-seq2seq [[7]](#ref-7) [later], same objective, gives 3.9% (Table 3 of [[6]](#ref-6)), 44% below 7.0%: later gains came from encoder and data (inference). The recall check over 2,236 earlier wiki studies (Appendix) finds one design training CTC and attention losses jointly: LCANet's AH-CTC-CE variant with joint decoding (Table II, Sec. 4.C) [[2]](#ref-2) [concurrent], visual-only on lab-recorded GRID. The novelty claim holds only with the authors' qualifiers, audio-visual and in the wild (Sec. 1). Standard: one dataset, one run, no ablation crediting the objective.

### M07 Lexicon and LM: external-text RNN language model

**Usual approach:** 28 of the 32 earlier sentence-level AVSR studies name neither an n-gram nor a neural language model, and none names a neural one (pattern match, Appendix). Here a character RNN-LM on LibriSpeech and LRS2 text is shallow-fused (Secs. 5.3, 5.4); the concurrent [[5]](#ref-5) also uses an external LM and reports results without it (Table 2).

**State of the art:** [[6]](#ref-6) [later] (2023) decodes visual-only models with a Transformer LM trained on 166 million characters (Sec. 3.3), at 14.6% LRS2 WER.

With no LM-free LRS2 number (Table 2), the LM and its out-of-domain text cannot be separated from the 6.9-point visual-only gain over WAS [[4]](#ref-4) (Sec. 6). Standard.

### M12 Evaluation: noise sweep and run variability

**Usual approach:** 22 of the 32 earlier sentence-level AVSR studies test additive noise at stated SNRs, and 20 of them give no variability estimate (pattern match, Appendix); the 2 with one date from 1999 and 2001. The paper follows this, with one run and no seeds (Sec. 5.2), but its strength is that training noise is babble only (Sec. 5.2) and the eight test noise types exclude babble (Sec. 6): the sweep measures robustness to unseen noise.

**State of the art:** [[8]](#ref-8) [later] (2022) reports LRS2 WER as mean and standard deviation over ten runs: 29.5 ± 0.4% visual-only on LRW and LRS2, 380 hours (Table 1), where it lists this paper at 63.5%.

The split behind Table 2 and Fig. 3, and how noise segments are selected and mixed, are not stated (Sec. 6). Standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Voiced broadcast speech (LRS2; LRW for pre-training) | Voiced speech recorded for training | – | standard |
| M02 Training-only supervision | Text labels; LRW words and LRS2 word boundaries for front-end pre-training | Text labels | – | standard |
| M03 Training and adaptation | LRW-pretrained ResNet; babble noise in training | Supervised training on transcribed data | – | standard |
| M04 Use-time action | Voiced speech; noise added at test | Voiced speech at use time | – | standard |
| M05 Sensors | Mouth ROI video and 83 audio features; early or late fusion | Camera mouth region plus microphone | – | standard |
| M06 Processing and decoding | Hybrid CTC/attention, BLSTM encoder, joint beam search | HMM named; neural: one CTC or attention loss; of 32 before 2018-09 (pattern match 32) | [[6]](#ref-6) 1.5% LRS2 AVSR WER, same objective | standard |
| M07 Lexicon and LM | Character RNN-LM, LibriSpeech and LRS2 text, shallow fusion | No n-gram or neural LM named; of 32 before 2018-09 (pattern match 28) | [[6]](#ref-6) Transformer LM, 166M characters | standard |
| M08 Output | Characters | Text output | – | standard |
| M09 Confirmation | None (offline) | Mostly absent | – | not applicable |
| M10 Correction | None (offline) | Mostly absent | – | not applicable |
| M11 Reference construction | LRS2 public partitions; result split not named | Public benchmark split | – | standard |
| M12 Evaluation | Eight unseen noise types, -5 to 20 dB; one run | Noise at stated SNRs, no variability estimate; of 32 before 2018-09 (pattern match 20) | [[8]](#ref-8) mean and std over ten runs | standard |
| M13 Device and cost | Offline benchmark; hardware and latency not stated | Offline GPU training | – | not applicable |

## Where the claims outrun the evidence

- Sec. 6 says the models, "trained only on LRS2", outperform the externally pretrained [[5]](#ref-5); but the visual ResNet is pretrained on LRW (Sec. 5.1), the LM reads LibriSpeech (Sec. 5.3), and [[8]](#ref-8) lists this system under LRW plus LRS2 (Table 1). The 7.0% against 8.2% (Table 2) mixes objective, front end, LM text and fusion.
- The clean audio-visual gain, 8.3% to 7.0% WER (Table 2), 16% relative (inference), comes from one run on an unnamed split (Sec. 6), with no seeds (Sec. 5.2).
- Sec. 1 places the 32.9-point maximum gain "at high SNR levels"; Sec. 6 places it at −5 dB, construction-drilling noise.
- The noise sweep uses early fusion only (Fig. 3), so the 8.5% late-fusion WER (Table 2) says nothing about noise; the authors leave noise-adaptive weighting to future work (Sec. 7).

## What the field needs next

- M06: an α sweep including 0 and 1, front end, LM and data fixed, three or more seeds, on two corpora.
- M07: results without the LM and with an LRS2-text-only LM.
- M12: a released noisy test list (noise files, segments, SNRs), late fusion included.

## Questions for the authors

- Which LRS2 partition produced Table 2 and Fig. 3?
- What WER do α = 0 and α = 1 give, and what ranges were searched?
- What is the WER without the language model?
- Did all systems see identical noise mixtures?

## Appendix: literature search

- Setting, the same for every topic: sentence-level AVSR, studies whose ledger matches both the sentence-level lip-reading pattern and the AVSR pattern (265 unique keys). State at the target's time: 38 dated before 2018-09, minus 5 human-perception entries (4 studies) and 1 version duplicate, gives 32; 4 studies dated only to 2018 are left out. Counts are full-text pattern matches, mentions included.
- M06, sentence-lipreading-sequence-objective (published table, appended). Inclusion rule: the published rule (sentence-level or open-vocabulary speech from lip or face video, classified by the sequence objective the full text names), restricted here to the AVSR subset. Ledger counts: 7,345 unique studies slot-filled for M06; 633 unique studies pattern match. Of the 32: HMM 32, CTC 4, attention or seq2seq 1, hybrid or joint CTC/attention 0. Recall check over 2,236 wiki studies first public before 2018-09: 5 hits, one design ([[2]](#ref-2), [concurrent], visual-only GRID) and 4 mentions or citations. Read: [[3]](#ref-3), [[4]](#ref-4) (prior); [[2]](#ref-2), [[5]](#ref-5) ([concurrent]); [[6]](#ref-6) (state of the art). Known-item recall 1.0.
- M07, use-time-language-model-visual-speech (published table, appended). Inclusion rule: the published rule (use-time language information named in the full text), restricted to the AVSR subset. Ledger counts: 119 unique studies slot-filled for M07; 633 unique studies pattern match. Of the 32: n-gram LM 4, neural LM 0, neither 28; grammar or lexicon 12. Read: [[5]](#ref-5) ([concurrent]); [[6]](#ref-6) (state of the art). Known-item recall 1.0.
- M12, avsr-noise-and-run-variability-protocol (published table, appended). Inclusion rule: the published rule and regexes (additive noise at stated SNRs, babble, run variability), restricted to the sentence-level subset. Ledger counts: 6,960 unique studies slot-filled for M12; 349 unique studies pattern match. Of the 32: additive noise at stated SNRs 22, without a variability estimate 20; babble 14; variability estimate 2. Read: [[8]](#ref-8) (state of the art). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Petridis, S., Stafylakis, T., Ma, P., Tzimiropoulos, G., Pantic, M. “Audio-Visual Speech Recognition with a Hybrid CTC/Attention Architecture.” *IEEE Spoken Language Technology Workshop (SLT)*, 2018. doi:[10.1109/SLT.2018.8639643](https://doi.org/10.1109/SLT.2018.8639643). arXiv:[1810.00108](https://arxiv.org/abs/1810.00108). First public as arXiv:1810.00108v1 (dated 28 Sep 2018). [wiki: arxiv-1810.00108](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1810.00108/article.md) [wiki: doi-10.1109-slt.2018.8639643](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-slt.2018.8639643/article.md)
2. <a id="ref-2"></a>Xu, K., Li, D., Cassimatis, N., Wang, X. “LCANet: End-to-End Lipreading with Cascaded Attention-CTC.” *arXiv preprint*, 2018. arXiv:[1803.04988](https://arxiv.org/abs/1803.04988). Visual-only GRID; multi-task CTC + attention variant with joint decoding (M06), cited by the target. [concurrent] [wiki: arxiv-1803.04988](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1803.04988/article.md)
3. <a id="ref-3"></a>Sanabria, R., Metze, F., De La Torre, F. “Robust End-to-End Deep Audiovisual Speech Recognition.” *arXiv preprint*, 2016. arXiv:[1611.06986](https://arxiv.org/abs/1611.06986). Prior; deciding prior for M06 (CTC-only end-to-end AVSR). [wiki: arxiv-1611.06986](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1611.06986/article.md)
4. <a id="ref-4"></a>Chung, J. S., Senior, A., Vinyals, O., Zisserman, A. “Lip Reading Sentences in the Wild.” *IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2017. doi:[10.1109/CVPR.2017.367](https://doi.org/10.1109/CVPR.2017.367). arXiv:[1611.05358](https://arxiv.org/abs/1611.05358). Prior; deciding prior for M06 (attention-only audio-visual character decoder). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lip-reading-sentences-in-the-wild) [wiki: arxiv-1611.05358](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1611.05358/article.md) [wiki: cvf-chung17-lipreadwild](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-chung17-lipreadwild/article.md)
5. <a id="ref-5"></a>Afouras, T., Chung, J. S., Senior, A., Vinyals, O., Zisserman, A. “Deep Audio-Visual Speech Recognition.” *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 2018. doi:[10.1109/TPAMI.2018.2889052](https://doi.org/10.1109/TPAMI.2018.2889052). arXiv:[1809.02108](https://arxiv.org/abs/1809.02108). Separate CTC and seq2seq models on one front end, with and without an external LM (M06, M07); a comparison system in the target's Table 2. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/deep-audio-visual-speech-recognition) [wiki: arxiv-1809.02108](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1809.02108/article.md) [wiki: doi-10.1109-tpami.2018.2889052](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tpami.2018.2889052/article.md)
6. <a id="ref-6"></a>Ma, P., Haliassos, A., Fernandez-Lopez, A., Chen, H., Petridis, S., Pantic, M. “Auto-AVSR: Audio-Visual Speech Recognition with Automatic Labels.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2023. doi:[10.1109/ICASSP49357.2023.10096889](https://doi.org/10.1109/ICASSP49357.2023.10096889). arXiv:[2303.14307](https://arxiv.org/abs/2303.14307). LRS2 state of the art for the joint CTC/attention lineage (M06, M07). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/auto-avsr-audio-visual-speech-recognition-with-automatic-labels) [wiki: arxiv-2303.14307](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2303.14307/article.md)
7. <a id="ref-7"></a>Ma, P., Petridis, S., Pantic, M. “End-to-End Audio-Visual Speech Recognition with Conformers.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2021, 7613-7617. doi:[10.48550/arXiv.2102.06657](https://doi.org/10.48550/arXiv.2102.06657). arXiv:[2102.06657](https://arxiv.org/abs/2102.06657). CM-seq2seq: joint CTC/attention with a Conformer encoder at the target's 380 h (M06). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/end-to-end-audio-visual-speech-recognition-with-conformers) [wiki: arxiv-2102.06657](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2102.06657/article.md)
8. <a id="ref-8"></a>Ma, P., Petridis, S., Pantic, M. “Visual Speech Recognition for Multiple Languages in the Wild.” *Nature Machine Intelligence*, 2022, 930-939. doi:[10.1038/s42256-022-00550-z](https://doi.org/10.1038/s42256-022-00550-z). arXiv:[2202.13084](https://arxiv.org/abs/2202.13084). LRS2 results as mean and standard deviation over ten runs (M12). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/visual-speech-recognition-for-multiple-languages-in-the-wild) [wiki: arxiv-2202.13084](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2202.13084/article.md) [wiki: doi-10.1038-s42256-022-00550-z](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s42256-022-00550-z/article.md)
