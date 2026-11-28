# Deep Lip Reading: a comparison of models and an online application

Afouras, Chung, Zisserman. Proc. Interspeech 2018, pp. 3514–3518. [doi:10.21437/Interspeech.2018-1943](https://doi.org/10.21437/Interspeech.2018-1943) · [arXiv:1806.06053](https://arxiv.org/abs/1806.06053v1)

## Verdict

The paper [[1]](#ref-1) changes the sequence back end (M06, standard) and adds online decoding (M13, not reported). Its Transformer and convolutional CTC readers have no counterpart among the 49 earlier sentence-level decoders (pattern match, Appendix), but one run per model settles only the family gaps of 5 points or more, not the 0.7–2.1-point FC-10/FC-15 and T1/T2 orderings. The LRS2 claim holds without the non-public T2 LM, yet "over 20" points needs T2, the 70.4% baseline is credited to two papers with no conditions, and training data differ. "Low latency" rests on a 22- or 32-frame lag and unscored examples, while real-time factors were measured for articulator video in 2011 [[2]](#ref-2) and later streaming work reports delay and error [[3]](#ref-3).

## Against the field, component by component

### M06 Processing: three back ends on one front end

**Usual approach:** All 49 earlier sentence-level decoders mention HMMs (pattern match, Appendix); the neural ones use CTC over recurrent layers (LipNet [[4]](#ref-4), which BL follows, Sec. 2.2) or LSTM attention (WLAS [[5]](#ref-5)). The paper adds a Transformer and a depthwise temporal-convolution CTC model on the front end of [[6]](#ref-6); none of the 49 mentions a Transformer and neither temporal-convolution hit is a back end (Appendix).
**State of the art:** Auto-AVSR (2023) [[7]](#ref-7) reaches 14.6% LRS2 visual-only WER with joint CTC/attention, 3,448 hours and an LM; with 818 hours it scores 27.9%, and the best LRS2-only system it lists scores 32.9% (its Table 3). The gap to 50.0% here is 35.4 points; Auto-AVSR's own 818-to-3,448-hour step is worth 13.3 (inference).

The authors claim the precedent, "for the first time" (Sec. 1); the Appendix agrees: no confirmed earlier study compares CTC and attention on one front end. The group's [concurrent] TM-seq2seq paper [[8]](#ref-8) reuses this Transformer (48.3% with LM, its Table 2); LRS3 [[9]](#ref-9) followed. Greedy TM leads FC-15 by 6.8 points and by 5.0 after beam search and the T2 LM, with beam width 15 against 100 (inference). The authors blame BL's deficit on CTC (Sec. 3.3), but FC-10 uses CTC and beats BL by 5.1 points (inference). Standard: one run on one dataset (Sec. 3.1) gives no repetition.

### M13 Operation: online decoding and latency

**Usual approach:** 5 of 12 lip- or articulator-video decoders that claim online operation report a measured latency, delay or real-time factor (pattern match, Appendix); before the target, Cai et al. [[2]](#ref-2) give real-time factors of 0.65 and 0.58 for one speaker with a 20k trigram (its Table 5), and WLAS lists an on-line decoder as an extension (its Sec. 6) [[5]](#ref-5). Here FC lags by its right context, 22 or 32 frames, and reproduces the offline output (Sec. 4).
**State of the art:** Ma et al. (2023) [[3]](#ref-3) report LRS3 streaming visual-only WER of 50.6% against 38.6% offline, with 580 ms visual-encoder delay and 1,060 ms in total (its Table 1, Sec. 4).

At 25 frames per second, unstated in the paper, the lag is 0.88 s or 1.28 s (inference). No delay in ms or partial-hypothesis WER is given; 0.4 and 0.5 changes per frame come from two examples (Table 5). The [concurrent] Sterpu et al. [[10]](#ref-10) keep accuracy with online-capable monotonic attention (61.58% vs 61.52%, their Table 1), also without an online test. The authors call the study preliminary (Sec. 5). Not reported: "low latency" (Abstract) needs the delay and online error that [[3]](#ref-3) measures.

### M07 Language model: character LSTM, two corpora

**Usual approach:** Of the 49, 27 mention a grammar, lexicon or dictionary, 7 an n-gram LM and none a neural LM (pattern match, Appendix); LipNet uses a character 5-gram [[4]](#ref-4). The paper shallow-fuses a character LSTM trained on T1 (2M words) or the non-public T2 (26M; Table 3).
**State of the art:** Auto-AVSR (2023) [[7]](#ref-7) decodes its 14.6% with a Transformer LM on 166 million characters (its Sec. 3).

T2 gains 0.7–1.3 points (Sec. 3.3), single runs. Algorithm 1 takes a word dictionary (App. A.4) without saying what it constrains; a lexicon on CTC alone would bias M06. Standard.

### M12 Evaluation: the LRS2 claim

**Usual approach:** None of the 49 reports LRS2 (pattern match, Appendix); here and in [concurrent] work [[8]](#ref-8) each system has one error rate.
**State of the art:** Auto-AVSR (2023) [[7]](#ref-7) also gives one value per system (its Table 3).

Table 1 credits 70.4% to MV-WAS (the paper's ref. 15), Sec. 3.3 to WLAS, which reports 50.2% on the unreleased LRS, not LRS2 (its Table 5) [[5]](#ref-5); Auto-AVSR lists MV-WAS with LRS2 data only, 223 hours (its Table 3). Against it, 50.0% is 20.4 points (29% relative) and T1 decoding 19.2 points (27% relative), so "over 20" holds as points only with T2 (inference). Not reported: no seeds or test-speaker composition (Sec. 3.1).

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Voiced BBC speech | Voiced speech | – | standard |
| M02 Training-only supervision | Subtitles; word pretraining | Transcribed video | – | standard |
| M03 Training and adaptation | WLAS curriculum; MV-LRS | Length curriculum | – | standard |
| M04 Use-time action | Voiced speech | Voiced speech | – | standard |
| M05 Sensors | Mouth crop, 3D+ResNet front end | Camera mouth region | – | standard |
| M06 Processing and decoding | BLSTM-CTC, conv CTC, Transformer | HMM in 49 of 49 (mentions) | [[7]](#ref-7) 14.6% | standard |
| M07 Lexicon and LM | Char LSTM LM, T1 vs T2 | Lexicon 27 of 49 (mentions) | [[7]](#ref-7) Transformer LM | standard |
| M08 Output | Characters | Characters | – | standard |
| M09 Confirmation | None | Mostly absent | – | not applicable |
| M10 Correction | None | Mostly absent | – | not applicable |
| M11 Reference construction | LRS2 test | Benchmark partition | – | standard |
| M12 Evaluation | One run; 70.4% baseline | No LRS2 in 49 (mentions) | [[7]](#ref-7) one value | not reported |
| M13 Device and cost | Online FC, 22/32-frame lag | Measured delay, 12 online decoders (pattern match 5) | [[3]](#ref-3) 580 ms, 50.6% | not reported |

## Where the claims outrun the evidence

- Depthwise convolutions "double the network training speed" with no accuracy loss (Sec. 3.3): no ablation is shown.
- The baseline gap mixes data and model: 70.4% is listed as LRS2-only [[7]](#ref-7); every model here adds MV-LRS and LRW (Sec. 3.2).
- FC-15 trains in 3.4 days (Table 1) or 3.5 (Sec. 3.3); TM's 13 days include a curriculum extended to the longest validation sample (Sec. 3.3).

## What the field needs next

- M13: partial-hypothesis WER and delay in ms against lookahead, on a public test set.
- M06: CTC against seq2seq at matched beam, LM weight and lexicon, over seeds.
- M12: all models retrained without MV-LRS and T2.

## Questions for the authors

- Which system produced 70.4%, on what data, with what LM and beam?
- Does Algorithm 1's dictionary restrict CTC outputs, and TM's?
- Does T2 contain subtitles of LRS2 test programmes?
- What frame rate and end-to-end delay apply online?
- What data selected the CTC beam settings (App. A.4)?

## Appendix: literature search

- Setting for M06, M07 and M12: sentence-level lip reading, VSR or AVSR decoders, the 633-study ledger population of the M06 table. Window for the target (first public 2018-06): prior before 2017-12, [concurrent] 2017-12 to 2018-12. Removing human-perception and neuroscience studies, phonetic analyses, reviews and reports, corpus papers, enhancement, separation, synchronisation and keyword-spotting papers and version duplicates leaves 49 prior decoders, 14 [concurrent] and 2 date unresolved. Counts are full-text pattern matches (mentions, upper bounds), reference lists removed where detected.
- M06, ctc-vs-attention (published table, appended). Inclusion rule: the published rule, CTC-trained and attention or seq2seq decoders trained on one front end and compared side by side; hybrid-only systems excluded. Ledger counts: 7,345 unique studies slot-filled; 114 unique studies pattern match. Confirmed comparisons besides the target: 0 prior, 1 [concurrent] [[8]](#ref-8), 2 later (acoustic sensing, EEG). Recall estimate 1.0 (published, full-text-only sample of 30); known-item recall 0.5. Read: [[5]](#ref-5), [[4]](#ref-4) (prior); [[8]](#ref-8) ([concurrent]); [[7]](#ref-7) (state of the art).
- M06, sentence-lipreading-sequence-objective (published table, appended). Inclusion rule: the published rule (sequence objective named in the full text), filtered to decoders, plus Transformer, temporal-convolution and recurrent patterns. Ledger counts: 7,345 unique studies slot-filled; 633 unique studies pattern match. Of the 49 prior: HMM 49, recurrent 13, CTC 6, temporal convolution 2 (a spatiotemporal front end [[4]](#ref-4) and a reference title), attention 1 [[5]](#ref-5), Transformer 0. [Concurrent] 14: CTC 9, attention 8, temporal convolution 7, Transformer 2. Recall check over 1,900 wiki studies before 2017-12: 0 Transformer lip readers (1 hit, an instrument term); 0 temporal-convolution CTC back ends (3 hits, all describing LipNet). Read: [[5]](#ref-5), [[4]](#ref-4) (prior); [[10]](#ref-10) ([concurrent]). Known-item recall 1.0.
- M07, use-time-language-model-visual-speech (published table, appended). Inclusion rule: the published rule (use-time language information named in the full text). Ledger counts: 119 unique studies slot-filled; 633 unique studies pattern match. Of the 49 prior: grammar, lexicon or dictionary 27; n-gram LM 7; neural LM 0; no-LM statement 1. [Concurrent]: neural LM 3, n-gram 3. Read: [[4]](#ref-4) (prior); [[7]](#ref-7) (state of the art). Known-item recall 1.0.
- M12, lrs2-visual-only-sentence-evaluation (published table, appended). Inclusion rule: the published rule (visual-only CER or WER on the LRS2 test set). Ledger counts: 6,960 unique studies slot-filled; 127 unique studies pattern match. Of the 49 prior: LRS2 0; seed, deviation, interval or bootstrap mentions 16 (the published table found such hits to be augmentation or normalisation, not run spread). [Concurrent] LRS2: 3 ([[8]](#ref-8) and two audio-visual systems). Read: [[5]](#ref-5) (prior); [[8]](#ref-8) ([concurrent]); [[7]](#ref-7) (state of the art). Known-item recall 1.0.
- M13, streaming-lip-reading-decoding (new topic). Inclusion rule: decoders of lip, face or articulator video, alone or with audio, that claim online, streaming, simultaneous or real-time operation, classified by a measured latency, delay or real-time factor; perception, enhancement, separation, synthesis and phonetic studies excluded on reading the ledger text; versions once. Ledger counts: 6,075 unique studies slot-filled; 25 unique studies pattern match, of which 10 decoders besides the target; the whole-wiki recall check (26 hits before 2017-12) adds 2, giving 12 (4 prior, 8 later). Measured latency, delay or real-time factor: 5 of 12 (1 prior, read [[2]](#ref-2); 4 later). Read: [[2]](#ref-2), [[5]](#ref-5) (prior); [[10]](#ref-10) ([concurrent]); [[3]](#ref-3) (state of the art).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Afouras, T., Chung, J. S., Zisserman, A. “Deep Lip Reading: a comparison of models and an online application.” *Proc. Interspeech 2018*, 2018, 3514-3518. doi:[10.21437/Interspeech.2018-1943](https://doi.org/10.21437/Interspeech.2018-1943). arXiv:[1806.06053](https://arxiv.org/abs/1806.06053). Target of this review (arXiv v1, 15 Jun 2018; the DOI is the Interspeech version). [wiki: arxiv-1806.06053](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1806.06053/article.md) [wiki: isca-afouras18b-deeplip](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-afouras18b-deeplip/article.md) [wiki: isca-afouras18b_deeplipread](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-afouras18b_deeplipread/article.md) [wiki: isca-afouras18b_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-afouras18b_interspeech/article.md)
2. <a id="ref-2"></a>Cai, J., Denby, B., Roussel, P., Dreyfus, G., Crevier-Buchman, L. “Recognition and Real Time Performances of a Lightweight Ultrasound Based Silent Speech Interface Employing a Language Model.” *Proc. Interspeech 2011*, 2011. doi:[10.21437/Interspeech.2011-410](https://doi.org/10.21437/Interspeech.2011-410). Prior; real-time factors for continuous recognition from ultrasound and lip video, single speaker. [wiki: isca-cai11-lightssi](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-cai11-lightssi/article.md)
3. <a id="ref-3"></a>Ma, P., Moritz, N., Petridis, S., Fuegen, C., Pantic, M. “Streaming Audio-Visual Speech Recognition with Alignment Regularization.” *Proc. Interspeech 2023*, 2023. doi:[10.21437/Interspeech.2023-487](https://doi.org/10.21437/Interspeech.2023-487). arXiv:[2211.02133](https://arxiv.org/abs/2211.02133). Streaming visual-only WER and algorithmic delay on LRS3. [later] [wiki: arxiv-2211.02133](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2211.02133/article.md) [wiki: isca-ma23-streamingav](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-ma23-streamingav/article.md) [wiki: isca-ma23_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-ma23_interspeech/article.md)
4. <a id="ref-4"></a>Assael, Y. M., Shillingford, B., Whiteson, S., de Freitas, N. “LipNet: End-to-End Sentence-level Lipreading.” *arXiv preprint*, 2016. arXiv:[1611.01599](https://arxiv.org/abs/1611.01599). Prior; character CTC with a 5-gram LM, GRID. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lipnet-end-to-end-sentence-level-lipreading) [wiki: arxiv-1611.01599](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1611.01599/article.md)
5. <a id="ref-5"></a>Chung, J. S., Senior, A., Vinyals, O., Zisserman, A. “Lip Reading Sentences in the Wild.” *IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2017. doi:[10.1109/CVPR.2017.367](https://doi.org/10.1109/CVPR.2017.367). arXiv:[1611.05358](https://arxiv.org/abs/1611.05358). Prior; attention decoder on LRS; on-line decoder named as an extension. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lip-reading-sentences-in-the-wild) [wiki: arxiv-1611.05358](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1611.05358/article.md) [wiki: cvf-chung17-lipreadwild](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-chung17-lipreadwild/article.md)
6. <a id="ref-6"></a>Stafylakis, T., Tzimiropoulos, G. “Combining Residual Networks with LSTMs for Lipreading.” *Proc. Interspeech 2017*, 2017. doi:[10.21437/Interspeech.2017-85](https://doi.org/10.21437/Interspeech.2017-85). arXiv:[1703.04105](https://arxiv.org/abs/1703.04105). Prior; source of the shared visual front end (target Sec. 2.1). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/combining-residual-networks-with-lstms-for-lipreading) [wiki: isca-stafylakis17-resnetlstm](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-stafylakis17-resnetlstm/article.md) [wiki: isca-stafylakis17_lipread](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-stafylakis17_lipread/article.md) [wiki: arxiv-1703.04105](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1703.04105/article.md)
7. <a id="ref-7"></a>Ma, P., Haliassos, A., Fernandez-Lopez, A., Chen, H., Petridis, S., Pantic, M. “Auto-AVSR: Audio-Visual Speech Recognition with Automatic Labels.” *Proc. IEEE ICASSP 2023*, 2023. doi:[10.1109/ICASSP49357.2023.10096889](https://doi.org/10.1109/ICASSP49357.2023.10096889). arXiv:[2303.14307](https://arxiv.org/abs/2303.14307). Best LRS2 visual-only WER (14.6%); Table 3 lists earlier LRS2 systems with training hours. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/auto-avsr-audio-visual-speech-recognition-with-automatic-labels) [wiki: arxiv-2303.14307](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2303.14307/article.md)
8. <a id="ref-8"></a>Afouras, T., Chung, J. S., Senior, A., Vinyals, O., Zisserman, A. “Deep Audio-Visual Speech Recognition.” *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 2022, 44(12), 8717-8727. doi:[10.1109/TPAMI.2018.2889052](https://doi.org/10.1109/TPAMI.2018.2889052). arXiv:[1809.02108](https://arxiv.org/abs/1809.02108). Same group; TM-seq2seq and TM-CTC on LRS2-BBC (early access 2018). [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/deep-audio-visual-speech-recognition) [wiki: arxiv-1809.02108](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1809.02108/article.md) [wiki: doi-10.1109-tpami.2018.2889052](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tpami.2018.2889052/article.md)
9. <a id="ref-9"></a>Afouras, T., Chung, J. S., Zisserman, A. “LRS3-TED: a large-scale dataset for visual speech recognition.” *arXiv preprint*, 2018. arXiv:[1809.00496](https://arxiv.org/abs/1809.00496). Same group; LRS3-TED corpus. [concurrent] [wiki: arxiv-1809.00496](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1809.00496/article.md)
10. <a id="ref-10"></a>Sterpu, G., Saam, C., Harte, N. “Can DNNs Learn to Lipread Full Sentences?.” *arXiv preprint*, 2018. arXiv:[1805.11685](https://arxiv.org/abs/1805.11685). Monotonic (online-capable) attention for lipreading on TCD-TIMIT. [concurrent] [wiki: arxiv-1805.11685](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1805.11685/article.md)
