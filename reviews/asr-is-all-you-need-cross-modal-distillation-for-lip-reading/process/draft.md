# ASR is all you need: cross-modal distillation for lip reading

Afouras, T., Chung, J. S., Zisserman, A. · ICASSP 2020 · 2020 · [arXiv:1911.12747](https://arxiv.org/abs/1911.12747)

## Verdict

The paper [[1]](#ref-1) changes the training labels (M02): an audio-only ASR teacher supplies transcripts and posteriors for unlabelled video. This departed from lip-reading practice, where none of the 77 earlier studies used ASR-generated labels, distillation or unlabelled video (pattern match, Appendix). The verdict is standard: the authors name cross-modal ASR distillation for audio-visual recognition as the closest work (§1.1), and no Table 3 row trains CTC on ASR transcripts without distillation, so the distillation term is untested in WER. The "no human labels" LRS2 result is a 0.3-point single-run difference, below V2P's 0.9-point bootstrap error on LRS3 [[2]](#ref-2) (inference); the 3.9-point LRS3 gain from an ASR-filtered VoxCeleb2 subset is the better-supported finding (inference). The public-data state-of-the-art claim (M12) rests on 0.3- and 0.4-point margins over the [concurrent] Conv-seq2seq (inference).

## Against the field, component by component

### M02 Training-only supervision: ASR-teacher labels on unlabelled video

**Usual approach:** Human or caption transcripts: 77 of 77 sentence-level studies first public before 2019-05; none trains on ASR-generated labels, teacher distillation or unlabelled video (pattern match, snippets read, Appendix). Typical are V2P, with clips "paired with transcripts" [[2]](#ref-2), and TM-seq2seq [[3]](#ref-3).

**State of the art:** USR 2.0 (2026) [[4]](#ref-4) [later] reaches 17.6% LRS3 visual-only WER from 656 h labelled and 2,649 h unlabelled public video with self-generated pseudo-labels; Auto-AVSR (2023) [[5]](#ref-5) [later] reaches 19.1% with external-ASR labels. The paper's best no-human-label figure, 61.7% (LRS3, Table 3), is 44.1 points higher (inference); model and data scale differ.

Across signal types, no wiki study before 2019-05 (2,648 with full text) distils an audio or ASR teacher into a non-acoustic decoder (Appendix). Both same-family works are [concurrent]: LIBS aligns recognizer output with "the ground truth sentence", so it needs transcripts (65.29% LRS2 WER) [[6]](#ref-6), and a throat-microphone student learns from a close-talk teacher [[7]](#ref-7). The authors call ASR distillation for audio-visual recognition "the closest work to ours" (§1.1).

Without human transcripts the student reaches 58.2% (LRS2) and 65.6% (LRS3) against 58.5% and 68.8% for CTC on ground truth (Table 3), 0.3 points (0.5% relative) and 3.2 points (4.7% relative) better (inference). The arms differ in labels and loss; CTC on ASR transcripts (§1) has no WER. Clean VoxCeleb2 lowers LRS3 WER from 65.6% to 61.7%, 5.9% relative (inference); the LRS2 drop to 54.2% also adds ASR-labelled LRS3 (Table 3). Verdict: standard; the closest prior the authors name uses the same mechanism, and the distillation term lacks WER evidence.

### M12 Evaluation: public-data claim from single runs

**Usual approach:** Of 2 earlier LRS3 visual-only studies (corpus paper excluded; pattern match, Appendix), neither reports seeds or repeated runs; V2P gives bootstrap test errors [[2]](#ref-2). The paper reports single-run WERs and no comparator decoders (Table 3).

**State of the art:** USR 2.0 (2026) [[4]](#ref-4) [later] reaches 17.6% on public data and LP Conformer (2023) [[8]](#ref-8) [later] 12.8% with 100k h of non-public video, 42.2 and 47.0 points below the paper's 59.8% (inference).

The authors claim: "we obtain state-of-the-art results on the challenging LRS2 and LRS3 datasets for training only on publicly available data" (Abstract); they concede that proprietary-data systems remain better and that Conv-seq2seq obtains results "very close to ours" (§6). The margins over Conv-seq2seq, 0.4 points on LRS2 (51.3% against 51.7%) and 0.3 on LRS3 (59.8% against 60.1%), are each below V2P's 0.9-point bootstrap error on the full LRS3 test set (55.1% ± 0.9) [[2]](#ref-2) (inference). The paper's 59.8% with a 6-gram LM sits between TM-seq2seq without (59.9%) and with (58.9%) its external LM [[3]](#ref-3). Verdict: standard; single runs matched both earlier studies.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Overt speech video with paired audio | Recorded speech video | – | standard |
| M02 Training-only supervision | ASR-teacher transcripts + frame-wise KD, unlabelled VoxCeleb2 | Human or caption transcripts (pattern match 77) | [[4]](#ref-4) (2026): LRS3 VSR 17.6%, own pseudo-labels | standard |
| M03 Training and adaptation | ASR-agreement filter; optional GT fine-tuning; one run | Pretraining then fine-tuning | – | standard |
| M04 Use-time action | Overt speech; video only at test | Overt speech video | – | standard |
| M05 Sensors | Face video via public lip-reading front end | Camera video | – | standard |
| M06 Processing and decoding | Jasper-lip convolutional CTC student | CTC or seq2seq on visual features | – | standard |
| M07 Lexicon and LM | 8192-width beam, 6-gram Librispeech LM | External LM at decoding | – | standard |
| M08 Output | English graphemes | Characters or words | – | standard |
| M09 Confirmation | Offline study | Offline | – | not applicable |
| M10 Correction | Offline study | Offline | – | not applicable |
| M11 Reference construction | LRS2/LRS3 test transcripts; no overlap statement | Corpus transcripts | – | standard |
| M12 Evaluation | LRS2/LRS3 WER, one run, no spread | One run, no seeds or repeated runs (pattern match 2) | [[4]](#ref-4) (2026): 17.6% public; [[8]](#ref-8) (2023): 12.8% non-public | standard |
| M13 Device and cost | Public data; four 11 GB GPUs | Device and cost | – | standard |

## Where the claims outrun the evidence

- "Without requiring human annotated ground truth data" (Abstract): the teacher is trained on transcribed Librispeech (§4.1, Table 1), and the best rows fine-tune on ground truth (Table 3): labels move from video to audio.
- "we show how arbitrary amounts of unlabelled video data can be leveraged to improve performance" (Abstract): one 334 h subset kept by two ASR-agreement filters (90% valid English words; under 28% inter-recognizer WER; §2), with no unfiltered or random-subset control and no teacher WER (§4.1). The filter keeps what the teacher transcribes well.
- Faster training than CTC on ASR transcriptions (§1) is shown only against CTC on ground truth (Fig. 2).

## What the field needs next

- M02: ground-truth against ASR labels crossed with CTC against CTC plus distillation, at fixed data and model, with teacher WER per corpus.
- M02: unfiltered, filtered and random VoxCeleb2 subsets, equal hours.
- M12: repeated runs or bootstrap errors as in [[2]](#ref-2), with comparators decoded under one language model.
- M11: a speaker overlap audit between VoxCeleb2 and the LRS2/LRS3 test sets.

## Questions for the authors

- What WER does CTC on ASR transcripts alone reach on LRS2 and LRS3?
- What is the teacher's WER on LRS2, LRS3 and the clean VoxCeleb2 subset?
- How many runs and seeds underlie each Table 3 row, and how were checkpoints selected?
- Do VoxCeleb2 speakers appear in the LRS2 or LRS3 test sets?

## Appendix: literature search

- M02, asr-transcribed-unlabelled-video-training (published table, appended). Inclusion rule: lip-reading, VSR and AVSR studies classified from the full text (reference list removed) by the label source for unlabelled video (ASR or automatic transcripts, self-supervision, teacher distillation); for this review restricted to the 633-study sentence-level population by first-public date, prior before 2019-05 and [concurrent] 2019-05 to 2020-05; perception, neuroscience, synthesis, enhancement, corpus and review papers excluded on reading; versions once. Ledger counts: slot-filled 31 (M02); 1,049 unique studies pattern match over all dates. Before 2019-05: 118 raw, 77 kept; [concurrent]: 17 kept including the target; date unresolved (2019 only): 14. Designs among the 77 (pattern match, snippets read): ASR-generated labels 3 hits, 0 real (forced alignment, perception, synthesis); distillation 1 hit, 0 real (mention); unlabelled video 1 hit, 0 real (enhancement). Usual design: human or caption transcripts, 77 of 77. Recall check over 3,089 wiki studies with full text before 2020-06, any signal, ASR or automatic transcripts: 20 hits, 0 prior with the design (formant targets for a silent speech interface; ASR transcription for a human speechreading tool). Read: [[2]](#ref-2), [[3]](#ref-3) (prior); [[6]](#ref-6) ([concurrent]); [[4]](#ref-4), [[5]](#ref-5) (state of the art). Known-item recall 1.0.
- M02, knowledge-distillation-in-speech-decoding (published table, appended). Inclusion rule: speech decoding from any non-acoustic or audio-visual signal with a teacher-student objective; for this review, whole-wiki full-text recall for a distillation term with a non-acoustic signal term, snippets classified. Ledger counts: 22 unique studies ledger match, 131 with ledger or full-text mentions (pattern match, all dates). Before 2020-06: 3,089 scanned (2,648 before 2019-05), 26 hits; same design before 2019-05: 0; [concurrent]: 2 ([[6]](#ref-6), [[7]](#ref-7)); the rest are two-stream video distillation, mentions, reference lists and perception studies. Known-item recall 1.0.
- M12, lrs3-visual-only-wer (published table, appended). Inclusion rule: visual-only WER on the LRS3 test set, any training regime; versions once. Ledger counts: 258 unique studies pattern match over all dates. Before 2019-05: 3 raw, 2 after excluding the corpus paper; repeated training runs 0 of 2; bootstrap test errors 1 of 2 ([[2]](#ref-2)); [concurrent]: 3 besides the target. Read: [[2]](#ref-2), [[3]](#ref-3) (prior); [[4]](#ref-4), [[8]](#ref-8) (state of the art). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [asr-is-all-you-need-cross-modal-distillation-for-lip-reading.bib](asr-is-all-you-need-cross-modal-distillation-for-lip-reading.bib).

1. <a id="ref-1"></a>Afouras, T., Chung, J. S., Zisserman, A. “ASR is all you need: cross-modal distillation for lip reading.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2020. arXiv:[1911.12747](https://arxiv.org/abs/1911.12747). Target. Read as arXiv v2. [wiki: arxiv-1911.12747](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1911.12747/article.md)
2. <a id="ref-2"></a>Shillingford, B., Assael, Y., Hoffman, M. W., Paine, T., Hughes, C., Prabhu, U., et al. “Large-Scale Visual Speech Recognition.” *arXiv preprint*, 2018. arXiv:[1807.05162](https://arxiv.org/abs/1807.05162). Prior; caption-mined training data (M02) and bootstrap test errors on LRS3 (M12). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/large-scale-visual-speech-recognition) [wiki: arxiv-1807.05162](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1807.05162/article.md) [wiki: isca-shillingford19-largescale](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-shillingford19-largescale/article.md) [wiki: isca-shillingford19_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-shillingford19_interspeech/article.md)
3. <a id="ref-3"></a>Afouras, T., Chung, J. S., Senior, A., Vinyals, O., Zisserman, A. “Deep Audio-Visual Speech Recognition.” *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 2018. doi:[10.1109/TPAMI.2018.2889052](https://doi.org/10.1109/TPAMI.2018.2889052). arXiv:[1809.02108](https://arxiv.org/abs/1809.02108). Prior; TM-seq2seq with and without external LM (M12). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/deep-audio-visual-speech-recognition) [wiki: arxiv-1809.02108](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1809.02108/article.md) [wiki: doi-10.1109-tpami.2018.2889052](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tpami.2018.2889052/article.md)
4. <a id="ref-4"></a>Haliassos, A., Mira, R., Petridis, S. “Pay Attention to CTC: Fast and Robust Pseudo-Labelling for Unified Speech Recognition.” *International Conference on Learning Representations (ICLR)*, 2026. arXiv:[2602.19316](https://arxiv.org/abs/2602.19316). State of the art for M02 and M12 on public data. [later] [wiki: arxiv-2602.19316](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.19316/article.md)
5. <a id="ref-5"></a>Ma, P., Haliassos, A., Fernandez-Lopez, A., Chen, H., Petridis, S., Pantic, M. “Auto-AVSR: Audio-Visual Speech Recognition with Automatic Labels.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2023. doi:[10.1109/ICASSP49357.2023.10096889](https://doi.org/10.1109/ICASSP49357.2023.10096889). arXiv:[2303.14307](https://arxiv.org/abs/2303.14307). External-ASR labels on unlabelled video (M02). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/auto-avsr-audio-visual-speech-recognition-with-automatic-labels) [wiki: arxiv-2303.14307](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2303.14307/article.md)
6. <a id="ref-6"></a>Zhao, Y., Xu, R., Wang, X., Hou, P., Tang, H., Song, M. “Hearing Lips: Improving Lip Reading by Distilling Speech Recognizers.” *Proceedings of the AAAI Conference on Artificial Intelligence*, 2020, 34(04). doi:[10.1609/aaai.v34i04.6174](https://doi.org/10.1609/aaai.v34i04.6174). arXiv:[1911.11502](https://arxiv.org/abs/1911.11502). ASR-teacher distillation into a lip reader on transcribed data (M02). [concurrent] [wiki: arxiv-1911.11502](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1911.11502/article.md) [wiki: doi-10.1609-aaai.v34i04.6174](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1609-aaai.v34i04.6174/article.md)
7. <a id="ref-7"></a>Suzuki, T., Ogata, J., Tsunakawa, T., Nishida, M., Nishimura, M. “Knowledge Distillation for Throat Microphone Speech Recognition.” *Interspeech 2019*, 2019. doi:[10.21437/Interspeech.2019-3115](https://doi.org/10.21437/Interspeech.2019-3115). Close-talk teacher distilled into a throat-microphone student (M02). [concurrent] [wiki: isca-suzuki19_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-suzuki19_interspeech/article.md)
8. <a id="ref-8"></a>Chang, O., Liao, H., Serdyuk, D., Shah, A., Siohan, O. “Conformers are All You Need for Visual Speech Recognition.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2024, 10136-10140. arXiv:[2302.10915](https://arxiv.org/abs/2302.10915). Best LRS3 VSR WER on non-public data (M12). [later] [wiki: arxiv-2302.10915](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2302.10915/article.md)
