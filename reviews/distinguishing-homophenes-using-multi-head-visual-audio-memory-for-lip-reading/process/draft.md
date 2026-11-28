# Distinguishing Homophenes Using Multi-Head Visual-Audio Memory for Lip Reading

Minsu Kim, Jeong Hun Yeo, Yong Man Ro. AAAI 2022 (arXiv April 2022). [arXiv:2204.01725](https://arxiv.org/abs/2204.01725)

## Verdict

The paper [[1]](#ref-1) changes training-only supervision (M02), recalling stored audio features from video, and processing (M06), addressing that memory with eight key heads at four depths. Both are standard. The audio memory is the authors' own [concurrent] design [[2]](#ref-2), their single-memory baseline (Table 1). The homophene-specific part, multiple heads, adds 0.3 LRW points in one run, while four depths add 1.3. The LRW state-of-the-art claim rests on a 0.1-point single-run margin over DC-TCN, the 3-point LRW-1000 gain over the earlier memory also swaps Bi-GRU for MS-TCN, and the homophene evidence is twelve words without sample counts.

## Against the field, component by component

### M02 Training-only supervision: audio recalled from a memory

**Usual approach:** Before the paper, all 3 decoders that transfer audio into a video-only lip reader distil an audio or ASR teacher, as in [[3]](#ref-3), and none recalls audio from a memory (pattern match, Appendix); LiRA [[4]](#ref-4) regresses PASE+ audio features. The paper stores audio in a value memory recalled from video, as its authors' [concurrent] ICCV paper did [[2]](#ref-2).

**State of the art:** At the time LiRA (2021) reached 88.1% on LRW [[4]](#ref-4), 0.4 points below the paper's 88.5% (inference). Today SyncVSR (2024) [[5]](#ref-5) [later], supervising frames with quantized audio tokens, reaches 93.2% on LRW without word boundaries, LRW video only, mean of three runs: 4.7 points higher, 41% less error (inference). On LRS2 without a language model it gives 22.0% WER from 661 h of video, against the paper's 44.5% from 818 h [[5]](#ref-5).

The memory's LRW effect is real: 86.1% without memory to 88.5% (Table 1), a 17% relative error cut (inference). Verdict: standard; recall from an audio memory is inherited from [[2]](#ref-2), and the new value-memory contrastive loss (Sec. 3.2) has no ablation.

### M06 Processing: multi-head keys and multi-depth memory for homophenes

**Usual approach:** Of 44 prior lip-reading decoders whose ledger names homophenes, visemes or one-to-many mapping (pattern match, Appendix), 24 name viseme intermediate units and 22 a language model; none of the 44 names an audio memory or multi-head memory. A typical prior design classifies visemes and resolves the one-to-many mapping by language-model perplexity [[6]](#ref-6); the paper retrieves several audio candidates per frame.

**State of the art:** The same group's [later] multi-temporal lip-audio memory is listed at 91.7% on LRW and 54.3% on LRW-1000 with DC-TCN [[5]](#ref-5); SyncVSR (2024), which also targets homophenes, reaches 93.2% and 58.2% with no memory [[5]](#ref-5), 4.4 points above the paper on LRW-1000 (inference).

The paper's numbers place the gain away from the heads: in Table 1 heads add 0.3 points (86.9% to 87.2%, 2% less error) and four depths 1.3 (10%) (inference); in Table 2 one head at four depths (87.53%) beats eight heads at one depth (87.22%). The authors' own motivation: a single memory can address the same slots for homophenes (Sec. 3.1); their ICCV memory gave about and amount 0.906 address similarity [[2]](#ref-2). Verdict: standard; no prior in the Appendix count has the design, but its homophene-specific effect is not repeated over datasets or seeds.

### M12 Evaluation: LRW and LRW-1000 claims

**Usual approach:** single-run LRW top-1 test accuracy, the paper's protocol throughout (Tables 1-6).

**State of the art:** At the time the best single LRW model was DC-TCN at 88.4% (Table 3); a self-distilled ensemble had reached 88.5% (2020) [[7]](#ref-7), and word-boundary input gave 55.7% on LRW-1000 (2020) [[8]](#ref-8), above the paper's 53.82%. Today the best like-for-like LRW figure is 93.2% (2024) [[5]](#ref-5). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | No user training action; voiced broadcast clips | Recorded speech corpora | – | standard |
| M02 Training-only supervision | Paired audio stored in a value memory, recalled from video | Knowledge distillation from an audio or ASR teacher (pattern match 3) | LRW 93.2%, audio-token supervision [[5]](#ref-5) | standard |
| M03 Training and adaptation | End-to-end; LRW-pretrained front end for sentences | Per-corpus supervised training | – | standard |
| M04 Use-time action | Voiced speech, video alone at test | Voiced articulation | – | standard |
| M05 Sensors | Lip crop 112x112; mel-spectrogram in training only | Mouth crop from video | – | standard |
| M06 Processing and decoding | 8 key heads, 112 slots, memory at 4 depths of MS-TCN or Transformer | Viseme intermediate units (pattern match 24) | LRW 93.2%, LRW-1000 58.2%, no memory [[5]](#ref-5) | standard |
| M07 Lexicon and LM | No external language model | No language model in word classification | – | standard |
| M08 Output | Word class (500 or 1,000); characters on LRS2 | Word class or text | – | standard |
| M09 Confirmation | None | None | – | not applicable |
| M10 Correction | None | None | – | not applicable |
| M11 Reference construction | Benchmark splits; six homophene pairs from a viseme map | Benchmark splits | – | standard |
| M12 Evaluation | Top-1 accuracy, WER; single run, no seeds | Single-run LRW top-1 accuracy | LRW 93.2%, no word boundaries, three runs [[5]](#ref-5) | standard |
| M13 Device and cost | Offline; no latency or memory cost | Benchmark only | – | not reported |

## Where the claims outrun the evidence

- "Sets a new state-of-the-art" (Sec. 4.2) rests on 88.5% against 88.4% for DC-TCN (Table 3), 0.9% less error, one run, no seeds (inference); Table 3 lists that self-distillation work's single model (87.9%, not its 88.5% ensemble), but Table 4 its LRW-1000 ensemble (46.60%, single 45.3%) [[7]](#ref-7).
- The 3% LRW-1000 lead over [[2]](#ref-2) (Sec. 4.2) compares an MS-TCN model with a Bi-GRU one, whose memory added 5.89 points over its own baseline [[2]](#ref-2); the paper has no LRW-1000 baseline without memory, and omits [[8]](#ref-8) at 55.7% with word boundaries.
- The LRS2 gain of 5.3% WER (Table 5) is against a 2018 baseline; a prior conformer gives 42.4% with an RNN language model and 37.9% with a Transformer one [[9]](#ref-9), and the paper has no language-model row.
- Table 6 gives 12 words without denominators (Sec. 4.3); all values are even, consistent with 50 test clips per word, so +2% is one clip (inference), and two words gain 0 points (Table 6).
- Slots, heads and depths each take their ablation's best score (Table 2); no validation data are named (Sec. 4.1).

## What the field needs next

- M06: heads and depths ablated jointly on LRW and LRW-1000 over seeds, with accuracy on all viseme-identical word pairs and clip counts.
- M02: memory recall, audio-feature regression [[4]](#ref-4) and audio-token supervision [[5]](#ref-5) on one back end and data budget.
- M12: a no-memory MS-TCN baseline on LRW-1000 and an LRS2 language-model row.

## Questions for the authors

- Which data selected N, h and the depths, and what is the run-to-run spread of Tables 1-6?
- How many homophene pairs did the viseme map yield in LRW, and how were the six reported chosen?

## Appendix: literature search

- M02 audio-knowledge-transfer-to-video (published topic table, appended). Inclusion rule: lip-reading and video-to-speech studies that take only lip or face video at test and use paired audio or a speech model during training to enrich the visual model, by distillation, audio-feature regression or a memory of audio representations; for this review dated against 2022-02 and restricted to decoders that transfer audio (perception studies, audio-visual recognizers needing audio at test, video-to-speech systems with audio only as output, and distillation between video models excluded); versions counted once. Slot-filled 31 unique studies; pattern match 54 unique studies (67 folders). Prior (before 2021-08): 3 studies, knowledge distillation 3, memory recall 0, audio-feature regression 0 (pattern match). [Concurrent] (2021-08 to 2022-08): 6 studies, knowledge distillation 4, memory recall 1 ([[2]](#ref-2)), audio-feature regression 1. Usual design: knowledge distillation, 3 of 3 prior (pattern match). Read in full: [[2]](#ref-2) [concurrent], [[3]](#ref-3), [[4]](#ref-4), [[5]](#ref-5) [later], target. Known-item recall 0.75 (3 of 4 seeds).
- M06 homophene-disambiguation-in-lip-reading (new topic table). Inclusion rule: lip-reading decoders, video only at test, whose ledger names homophenes, visemes, visually similar words or one-to-many mapping, classified by the mechanism their full text names; perception studies, surveys, talking heads, audio-visual recognizers and video-to-speech excluded; full-text counts are mentions (pattern match, upper bounds); versions counted once. Slot-filled 7,345 unique studies; pattern match 128 unique studies (164 folders) before filtering. Prior (before 2021-08): 44 decoders; viseme intermediate units 24, language model 22, audio supervision 6, homophene named 8, audio memory 0, multi-head memory 0. [Concurrent]: 3 decoders, multi-head memory 1. Date unresolved: 11. Usual design: viseme intermediate units, 24 of 44 (pattern match). Read in full: [[6]](#ref-6), [[2]](#ref-2) [concurrent], [[5]](#ref-5) [later], target. Known-item recall 0.67 (2 of 3 seeds).
- M12 lrw-word-accuracy (published topic table, appended). Inclusion rule: visual-only word-level lip reading on LRW with top-1 test accuracy; word-boundary results labelled; versions counted once. Slot-filled 6,960 unique studies; pattern match 155 unique studies (191 folders). Usual design: ResNet-18 front end with a temporal model, top-1 accuracy on the LRW test set, 90 of 155 (pattern match, all years). Read in full: [[7]](#ref-7), [[8]](#ref-8), [[4]](#ref-4), [[9]](#ref-9), [[5]](#ref-5) [later], target. Known-item recall 1.0 (4 of 4 seeds).

## References

Numbered by first citation. BibTeX in the same order and keys: [distinguishing-homophenes-using-multi-head-visual-audio-memory-for-lip-reading.bib](distinguishing-homophenes-using-multi-head-visual-audio-memory-for-lip-reading.bib).

1. <a id="ref-1"></a>Kim, M., Yeo, J. H., Ro, Y. M. “Distinguishing Homophenes Using Multi-Head Visual-Audio Memory for Lip Reading.” *Proceedings of the AAAI Conference on Artificial Intelligence*, 2022. arXiv:[2204.01725](https://arxiv.org/abs/2204.01725). Target. Read as arXiv v1 (April 2022), the AAAI camera-ready. [wiki: arxiv-2204.01725](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2204.01725/article.md)
2. <a id="ref-2"></a>Kim, M., Hong, J., Park, S. J., Ro, Y. M. “Multi-modality Associative Bridging through Memory: Speech Sound Recollected from Face Video.” *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)*, 2021. arXiv:[2204.01265](https://arxiv.org/abs/2204.01265). [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/multi-modality-associative-bridging-through-memory-speech-sound-recollected-from-face-video) [wiki: arxiv-2204.01265](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2204.01265/article.md) [wiki: cvf-kim21-mabm](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-kim21-mabm/article.md)
3. <a id="ref-3"></a>Zhao, Y., Xu, R., Wang, X., Hou, P., Tang, H., Song, M. “Hearing Lips: Improving Lip Reading by Distilling Speech Recognizers.” *Proceedings of the AAAI Conference on Artificial Intelligence*, 2020, 34(04). doi:[10.1609/aaai.v34i04.6174](https://doi.org/10.1609/aaai.v34i04.6174). arXiv:[1911.11502](https://arxiv.org/abs/1911.11502). [wiki: arxiv-1911.11502](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1911.11502/article.md) [wiki: doi-10.1609-aaai.v34i04.6174](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1609-aaai.v34i04.6174/article.md)
4. <a id="ref-4"></a>Ma, P., Mira, R., Petridis, S., Schuller, B. W., Pantic, M. “LiRA: Learning Visual Speech Representations from Audio through Self-supervision.” *Interspeech*, 2021. doi:[10.21437/Interspeech.2021-1360](https://doi.org/10.21437/Interspeech.2021-1360). arXiv:[2106.09171](https://arxiv.org/abs/2106.09171). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lira-learning-visual-speech-representations-from-audio-through-self-supervision) [wiki: isca-ma21c-lira](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-ma21c-lira/article.md)
5. <a id="ref-5"></a>Ahn, Y. J., Park, J., Park, S., Choi, J., Kim, K. “SyncVSR: Data-Efficient Visual Speech Recognition with End-to-End Crossmodal Audio Token Synchronization.” *Interspeech 2024*, 2024. arXiv:[2406.12233](https://arxiv.org/abs/2406.12233). [later] [wiki: arxiv-2406.12233](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2406.12233/article.md)
6. <a id="ref-6"></a>Fenghour, S., Chen, D., Guo, K., Xiao, P. “Disentangling Homophemes in Lip Reading using Perplexity Analysis.” *arXiv preprint*, 2020. arXiv:[2012.07528](https://arxiv.org/abs/2012.07528). [wiki: arxiv-2012.07528](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2012.07528/article.md)
7. <a id="ref-7"></a>Ma, P., Martinez, B., Petridis, S., Pantic, M. “Towards Practical Lipreading with Distilled and Efficient Models.” *2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2021, 7608-7612. doi:[10.1109/ICASSP39728.2021.9415063](https://doi.org/10.1109/ICASSP39728.2021.9415063). arXiv:[2007.06504](https://arxiv.org/abs/2007.06504). [wiki: arxiv-2007.06504](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2007.06504/article.md)
8. <a id="ref-8"></a>Feng, D., Yang, S., Shan, S., Chen, X. “Learn an Effective Lip Reading Model without Pains.” *arXiv preprint*, 2020. arXiv:[2011.07557](https://arxiv.org/abs/2011.07557). [wiki: arxiv-2011.07557](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2011.07557/article.md)
9. <a id="ref-9"></a>Ma, P., Petridis, S., Pantic, M. “End-to-End Audio-Visual Speech Recognition with Conformers.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2021, 7613-7617. arXiv:[2102.06657](https://arxiv.org/abs/2102.06657). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/end-to-end-audio-visual-speech-recognition-with-conformers) [wiki: arxiv-2102.06657](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2102.06657/article.md)
