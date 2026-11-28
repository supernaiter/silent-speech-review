# Spatio-Temporal Fusion based Convolutional Sequence Learning for Lip Reading

Zhang, X., Cheng, F., Wang, S. · ICCV 2019 · 2019 · [doi:10.1109/ICCV.2019.00080](https://doi.org/10.1109/ICCV.2019.00080)

## Verdict

The paper [[1]](#ref-1) changes M06 twice: STFM replaces global average pooling before the sequence model, and a convolutional encoder-decoder with width-restricted self-attention replaces the Transformer. Both are standard. Keeping the spatial layout was not new: 7 of 13 prior lip readers that state their reduction use a fully connected layer over the map, two replacing average pooling for the same reason [[2]](#ref-2) [[3]](#ref-3) (Appendix), and STFM is tested only against average pooling. The encoder-decoder gains are measured against Transformer baselines the authors call inconsistent with the originals (§4.2); the final 51.7% and 60.1% WER on LRS2 and LRS3 trail TM-seq2seq's LM-free 49.8% and 59.9% [[4]](#ref-4). The state-of-the-art claim (§5) holds on GRID but fails on LRW against an earlier 15.67% error [[3]](#ref-3), and the paper does not state the LM condition of its own rows (§3.5, M07).

## Against the field, component by component

### M06 Processing: spatial reduction before the sequence model

**Usual approach:** Of 121 prior lip-reading decoders, 13 state how the per-frame map is reduced (pattern match, snippets read, Appendix): a fully connected layer over the map in 7, pooling to a vector in 5, as in the line the paper reproduces [[4]](#ref-4), and pyramid attention in 1 [[5]](#ref-5). STFM pools to 5×5 and fuses with temporal convolutions (§3.2), a layout-keeping design.

**State of the art:** SyncVSR (2024) [[6]](#ref-6) [later] reaches 93.2% LRW top-1 without word boundaries, LRW data only, three runs; the paper's 16.3% LRW error (Table 3) is 83.7%, 9.5 points lower (inference).

Against the paper's claim that average pooling discards "local spatial information" (Abstract), Stafylakis and Tzimiropoulos had replaced it "with a fully connected layer, which is more adequate for face images that are centred" [[2]](#ref-2), uncited. In Table 2 STFM beats GAP for Conv-seq2seq on LRW (18.7 to 16.3), LRS2 (55.6 to 51.7) and LRS3 (65.5 to 60.1), 13%, 7% and 8% relative (inference); one run each, no fully connected control. Verdict: standard.

### M06 Processing: convolutional sequence model and local self-attention

**Usual approach:** Recurrent models are named by 43 of 121 prior decoders (mention count, Appendix); temporal-convolution back ends are used by 8, three at sentence level, among them the CTC models FC-15 [[7]](#ref-7) and V2P-FullyConv [[8]](#ref-8). A convolutional encoder-decoder or width-restricted self-attention appears in 0 of 121 prior and 0 of 25 [concurrent] decoders (Appendix).

**State of the art:** LP Conformer (2024) [[9]](#ref-9) [later] reaches 12.8% LRS3 WER with 100k hours of non-public video; USR (2024) [[10]](#ref-10) [later] 16.0% on LRS2 without an LM, 35.7 points below the paper (inference).

Afouras et al. had found a fully convolutional lip reader "trains faster than BL and TM", 3.4 against 13 days, at 55.0% against 50.0% LRS2 WER with an LM [[7]](#ref-7), uncited. Table 1 reverses the accuracy order (55.6% against a reproduced TM-seq2seq at 60.5%), but the authors state the reproduction lacks MV-LRS and uses a lighter front end (§4.2). Attention widths above 100 match global attention and train 20% faster (Fig. 4). Verdict: standard; new form, no gain against a full-strength baseline.

### M07 Use-time language information: LM condition

**Usual approach:** All 5 prior decoders reporting LRS2 or LRS3 state the LM condition per row, 3 report both [[7]](#ref-7) [[4]](#ref-4) [[8]](#ref-8) (Appendix). The paper gives beam width 5 only (§3.5).

**State of the art:** USR (2024) [[10]](#ref-10) [later] states its 16.0% LRS2 WER is LM-free.

Table 3's TM-CTC (54.7%, 66.3%) and TM-seq2seq (48.3%, 58.9%) are the "+ extLM" columns of their source; LM-free they read 65.0%, 74.7%, 49.8% and 59.9% [[4]](#ref-4). Against those the paper trails TM-seq2seq by 1.9 and 0.2 points (inference). Verdict: not reported.

### M12 Evaluation: benchmark comparison

**Usual approach:** One error rate per system; 4 of 5 prior LRS2 or LRS3 decoders give no run spread (Appendix), as here.

**State of the art:** LinProVSR (2026) [[11]](#ref-11) [later] reaches 0.99% GRID WER, split type not named.

GRID 1.3% on the overlapped-speaker split (§4.1) also beats the omitted LCANet, 2.9% [[12]](#ref-12). On LRW, Stafylakis et al. reported 15.67% without word boundaries [[3]](#ref-3), 0.6 points below the paper (inference); V2P's 55.1 ± 0.9% on LRS3 (5-gram LM, 3,886 hours) [[8]](#ref-8) is omitted. Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Voiced speech video | Voiced speech video | – | standard |
| M02 Training-only supervision | Character labels only | Text labels | – | standard |
| M03 Training and adaptation | ImageNet init; LRW + LRS pre-train; length curriculum | Pretraining, length curriculum | – | standard |
| M04 Use-time action | Video only at test | Video only at test | – | standard |
| M05 Sensors | 112x112 lip crops | Mouth crops | – | standard |
| M06 Processing and decoding | STFM instead of GAP; conv encoder-decoder, local self-attention | Of 13 prior stating it: FC over map 7, pooled 5 (pattern match 7) | [[6]](#ref-6) (2024): LRW 93.2%; [[9]](#ref-9): LRS3 12.8% | standard |
| M07 Lexicon and LM | LM use not stated | LM stated per row | [[10]](#ref-10) (2024): LRS2 16.0%, no LM | not reported |
| M08 Output | 40 characters | Characters | – | standard |
| M09 Confirmation | Offline | Offline | – | not applicable |
| M10 Correction | Offline | Offline | – | not applicable |
| M11 Reference construction | Benchmark splits | Benchmark splits | – | standard |
| M12 Evaluation | One WER per row | Of 5 prior on LRS2/LRS3, no spread 4 (pattern match 4) | [[11]](#ref-11) (2026): GRID 0.99% | standard |
| M13 Device and cost | Training days only | Training time | – | standard |

## Where the claims outrun the evidence

- "State-of-the-art results on GRID and LRW" (§5) fails on LRW against [[3]](#ref-3) (its Table 6, V16).
- The authors concede the LRS2/LRS3 results are "not comparable" with Afouras et al. for lack of MV-LRS(w) (§4.3); the abstract still claims comparable performance.
- The 12-day saving (Abstract) equals Table 4's 19 days for TM-CTC minus 7 (inference), across different data, front ends and training schemes (Table 4).
- §4.2 credits TF-block-b with 2.4% over TM-seq2seq on LRW; Table 1 gives 22.1 against 18.7, 3.4 points (inference).
- TM-seq2seq with GAP reads 59.5% and 69.8% in Table 2 but 60.5% and 70.8% in Table 1, while the TM-CTC rows agree (inference).

## What the field needs next

- M06: STFM against a fully connected and a flatten projection of the same map [[3]](#ref-3), same back end, several seeds.
- M06: Conv-seq2seq against TM-seq2seq with identical data, front end and training budget; the attention-width sweep on each dataset.
- M07, M12: every row with and without an external LM.

## Questions for the authors

- Is an external LM used at test on any dataset?
- Which dataset does Fig. 4 use, and how many runs stand behind each point?
- Which data select checkpoints?
- Why do the TM-seq2seq rows of Tables 1 and 2 differ?

## Appendix: literature search

- Shared population for all topics: lip-reading and VSR decoders from the index (camera input; title or ledger names lip reading, VSR, LRW, LRS2/3 or speechreading; the ledger names a model), with survey, review, dataset, perception, enhancement, separation, synthesis, talking-face, forgery, synchronisation, keyword-spotting and challenge titles removed, then on reading 49 perception, neuroimaging and education studies and 19 non-decoder or off-task rows removed and 12 duplicate versions merged; target removed: 515 studies, dated against 2019-10 as prior (before 2019-04) 121, [concurrent] (2019-04 to 2020-04) 25, date unresolved 2, [later] 367. Design counts are full-text pattern matches with every prior and [concurrent] hit snippet read. Same-group prior decoders: none; the target's own-group citation is a speaker-authentication study.
- M06 lipreading-front-end-spatial-reduction (new). Inclusion rule: decoders of the shared population with a learned convolutional front end, classified by how the per-frame map is reduced before the temporal model: pooling to a per-frame vector, a fully connected layer over the map (flatten then project included), or spatial or spatiotemporal attention or pyramid modules; hand-crafted features and fully connected networks on raw pixels excluded; mentions are not designs. Ledger counts: slot-filled 7,345 (M06); ledger pattern match 418 unique studies. Prior: reduction stated by 13 of 121; fully connected over the map 7, pooled to a vector 5, spatiotemporal pyramid attention 1; fully connected layer replacing average pooling with a stated reason 2. [Concurrent]: pooled to a vector 5, spatial attention 2. Read: [[2]](#ref-2), [[3]](#ref-3), [[5]](#ref-5), [[4]](#ref-4) (prior); [[6]](#ref-6) (state of the art).
- M06 sentence-lipreading-encoder-architecture (published table, appended). Inclusion rule: sentence-level lip-reading decoders classified by temporal encoder; for this review the shared population, classified for temporal-convolution sequence models (front-end spatiotemporal convolution excluded), convolutional encoder-decoders, Transformer self-attention and width-restricted self-attention. Ledger counts (all dates): slot-filled 7,345; pattern match 633 unique studies. Prior: recurrent 43 of 121 (mention count); temporal-convolution back end used 8 (sentence level 3, pretraining stage only 3); self-attention used 2; convolutional encoder-decoder 0; width-restricted self-attention 0. [Concurrent]: width-restricted self-attention 0 of 25. [Later]: local-attention pattern 14. Read: [[7]](#ref-7), [[8]](#ref-8), [[4]](#ref-4) (prior); [[9]](#ref-9), [[10]](#ref-10) (state of the art). Known-item recall of the published table 0.83.
- M12 lrs2-visual-only-sentence-evaluation (published table, appended); also the basis of M07. Inclusion rule: visual-only CER or WER on the LRS2 test set; for this review prior decoders of the shared population reporting LRS2 or LRS3, read for the LM condition per row and run spread, plus the best prior LRW and GRID results. Ledger counts (all dates): slot-filled 6,960 (M12); pattern match 127 unique studies. Prior: LRS2 or LRS3 reported by 5 of 121; LM condition stated 5, both conditions 3, run spread 1; LRW mentioned by 18. Read: [[4]](#ref-4), [[8]](#ref-8), [[3]](#ref-3), [[12]](#ref-12) (prior); [[10]](#ref-10), [[11]](#ref-11) (state of the art).

## References

Numbered by first citation. BibTeX in the same order and keys: [spatio-temporal-fusion-based-convolutional-sequence-learning-for-lip-reading.bib](spatio-temporal-fusion-based-convolutional-sequence-learning-for-lip-reading.bib).

1. <a id="ref-1"></a>Zhang, X., Cheng, F., Wang, S. “Spatio-Temporal Fusion based Convolutional Sequence Learning for Lip Reading.” *IEEE/CVF International Conference on Computer Vision (ICCV)*, 2019, 713-722. doi:[10.1109/ICCV.2019.00080](https://doi.org/10.1109/ICCV.2019.00080). Target. ICCV 2019 proceedings (CVF open access); no arXiv preprint. [wiki: cvf-zhang19-stfcsl](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-zhang19-stfcsl/article.md)
2. <a id="ref-2"></a>Stafylakis, T., Tzimiropoulos, G. “Deep word embeddings for visual speech recognition.” *arXiv preprint*, 2017. arXiv:[1710.11201](https://arxiv.org/abs/1710.11201). Fully connected layer in place of the ResNet's final average pooling for centred faces (M06). [wiki: arxiv-1710.11201](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1710.11201/article.md)
3. <a id="ref-3"></a>Stafylakis, T., Khan, M. H., Tzimiropoulos, G. “Pushing the boundaries of audiovisual word recognition using Residual Networks and LSTMs.” *Computer Vision and Image Understanding*, 2018. arXiv:[1811.01194](https://arxiv.org/abs/1811.01194). Fully connected layer in place of ResNet average pooling; LRW 15.67% error without word boundaries (M06, M12). [wiki: arxiv-1811.01194](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1811.01194/article.md)
4. <a id="ref-4"></a>Afouras, T., Chung, J. S., Senior, A., Vinyals, O., Zisserman, A. “Deep Audio-Visual Speech Recognition.” *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 2018. doi:[10.1109/TPAMI.2018.2889052](https://doi.org/10.1109/TPAMI.2018.2889052). arXiv:[1809.02108](https://arxiv.org/abs/1809.02108). TM-CTC and TM-seq2seq; WER with and without external LM on LRS2 and LRS3 (M06, M12). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/deep-audio-visual-speech-recognition) [wiki: arxiv-1809.02108](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1809.02108/article.md) [wiki: doi-10.1109-tpami.2018.2889052](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tpami.2018.2889052/article.md)
5. <a id="ref-5"></a>Xiao, J. “3D Feature Pyramid Attention Module for Robust Visual Speech Recognition.” *arXiv preprint*, 2018. arXiv:[1810.06178](https://arxiv.org/abs/1810.06178). Spatiotemporal pyramid attention mask in the lip-reading front end (M06). [wiki: arxiv-1810.06178](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1810.06178/article.md)
6. <a id="ref-6"></a>Ahn, Y. J., Park, J., Park, S., Choi, J., Kim, K. “SyncVSR: Data-Efficient Visual Speech Recognition with End-to-End Crossmodal Audio Token Synchronization.” *Interspeech 2024*, 2024. arXiv:[2406.12233](https://arxiv.org/abs/2406.12233). LRW 93.2% top-1, LRW only, no word boundaries (state of the art). [later] [wiki: arxiv-2406.12233](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2406.12233/article.md)
7. <a id="ref-7"></a>Afouras, T., Chung, J. S., Zisserman, A. “Deep Lip Reading: a comparison of models and an online application.” *Proc. Interspeech 2018*, 2018. arXiv:[1806.06053](https://arxiv.org/abs/1806.06053). Fully convolutional CTC lip reader with training-time comparison on LRS2 (M06). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/deep-lip-reading-a-comparison-of-models-and-an-online-application) [wiki: arxiv-1806.06053](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1806.06053/article.md) [wiki: isca-afouras18b-deeplip](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-afouras18b-deeplip/article.md) [wiki: isca-afouras18b_deeplipread](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-afouras18b_deeplipread/article.md) [wiki: isca-afouras18b_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-afouras18b_interspeech/article.md)
8. <a id="ref-8"></a>Shillingford, B., Assael, Y., Hoffman, M. W., Paine, T., Hughes, C., Prabhu, U., et al. “Large-Scale Visual Speech Recognition.” *arXiv preprint*, 2018. arXiv:[1807.05162](https://arxiv.org/abs/1807.05162). V2P and V2P-FullyConv; LRS3 55.1% with a 5-gram LM (M06, M12). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/large-scale-visual-speech-recognition) [wiki: arxiv-1807.05162](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1807.05162/article.md) [wiki: isca-shillingford19-largescale](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-shillingford19-largescale/article.md) [wiki: isca-shillingford19_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-shillingford19_interspeech/article.md)
9. <a id="ref-9"></a>Chang, O., Liao, H., Serdyuk, D., Shah, A., Siohan, O. “Conformers are All You Need for Visual Speech Recognition.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2024, 10136-10140. arXiv:[2302.10915](https://arxiv.org/abs/2302.10915). LRS3 12.8% WER with 100k h (state of the art). [later] [wiki: arxiv-2302.10915](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2302.10915/article.md)
10. <a id="ref-10"></a>Haliassos, A., Mira, R., Chen, H., Landgraf, Z., Petridis, S., Pantic, M. “Unified Speech Recognition: A Single Model for Auditory, Visual, and Audiovisual Inputs.” *Advances in Neural Information Processing Systems (NeurIPS)*, 2024. arXiv:[2411.02256](https://arxiv.org/abs/2411.02256). LRS2 16.0% WER without LM (state of the art). [later] [wiki: arxiv-2411.02256](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2411.02256/article.md)
11. <a id="ref-11"></a>Xue, F., Zhu, B., Jia, W., Li, S., Li, Y., Zhang, J., et al. “LinProVSR: Linguistics-Knowledge Guided Progressive Disambiguation Network for Visual Speech Recognition.” *AAAI*, 2026. doi:[10.1609/aaai.v40i14.38133](https://doi.org/10.1609/aaai.v40i14.38133). GRID 0.99% WER (state of the art). [later] [wiki: aaai-38133-linprovsr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/aaai-38133-linprovsr/article.md)
12. <a id="ref-12"></a>Xu, K., Li, D., Cassimatis, N., Wang, X. “LCANet: End-to-End Lipreading with Cascaded Attention-CTC.” *IEEE International Conference on Automatic Face and Gesture Recognition (FG)*, 2018, 548-555. arXiv:[1803.04988](https://arxiv.org/abs/1803.04988). GRID 2.9% WER (M12). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lcanet-end-to-end-lipreading-with-cascaded-attention-ctc) [wiki: arxiv-1803.04988](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1803.04988/article.md)
