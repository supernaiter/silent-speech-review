# Whisper-Flamingo: Integrating Visual Features into Whisper for Audio-Visual Speech Recognition and Translation

Andrew Rouditchenko, Yuan Gong, Samuel Thomas, Leonid Karlinsky, Hilde Kuehne, Rogerio Feris, James Glass. Interspeech 2024. [doi:10.21437/Interspeech.2024-322](https://doi.org/10.21437/Interspeech.2024-322) [arXiv:2406.10082](https://arxiv.org/abs/2406.10082)

## Verdict

The paper [[1]](#ref-1) changes three components, all standard. M06, gated cross-attention from frozen AV-HuBERT lip features into a pretrained audio-only decoder, is a new combination of prior parts [[2]](#ref-2), [[3]](#ref-3) (Appendix), and its deciding comparison with early fusion is one Whisper-Medium run (Table 2). M03, freezing the recognizer and training only new layers, is AVFormer's regime [[3]](#ref-3). M08, one model for English transcription and six En-X directions, improves on per-pair models [[4]](#ref-4) in scope, not in noisy BLEU (20.5 against 20.8, Table 4). The main overreach is the clean LRS3 gain, 2.3% to 1.5% WER: it rests on a beam-15 audio baseline that the authors' revision scores at 1.1% with beam 1, against 1.0% for Whisper-Flamingo (arXiv v3, Table 3). The noisy lead over AV-HuBERT rests on recreated noise and single runs.

## Against the field, component by component

### M06 Processing: gated cross-attention into a pretrained decoder

**Usual approach:** Of 159 prior AVSR studies, 97 name feature concatenation in a recognizer trained on audio-visual data, 14 cross-modal attention, none gated cross-attention (pattern match, Appendix). Whisper-Flamingo keeps the recognizer and adds zero-initialised tanh-gated attention to lip features in each decoder block (Sec. 2).

**State of the art:** DoubleHelix (2026) [later] reports 3.8% WER at 0 dB babble on LRS3 (0.68% clean) with frozen Whisper and AV-HuBERT encoders and 1,759 h [[5]](#ref-5); Whisper-Flamingo's 5.6% (433 h, Table 3) is 1.8 points behind (inference), with more training hours.

TM-seq2seq already attended separately to audio and video in every decoder layer [[2]](#ref-2) (Sec. 3.4); AVFormer fed full-frame visual tokens to a frozen recognizer [[3]](#ref-3); prompting Whisper fed image labels as text [[6]](#ref-6). New is the combination with lip features; 12 [later] AVSR studies name gated cross-attention (Appendix). The evidence is single Whisper-Medium runs at 0 dB: early fusion 10.0%, gated cross-attention 7.0% (Table 2); the encoder variant is only "significantly worse" (Sec. 2). Verdict: standard; ahead would need repetition across seeds, sizes or datasets.

### M03 Training: freeze the fine-tuned recognizer, train the new layers

**Usual approach:** Of 359 prior VSR/AVSR studies, 166 name end-to-end or full fine-tuning, 15 a frozen pretrained encoder, 9 adapters or prompt tuning (pattern match, Appendix). Whisper-Flamingo fine-tunes Whisper on noisy audio, freezes it and adds 630M trained parameters, 2.5B in total (Sec. 3.1).

**State of the art:** DoubleHelix (2026) [later] keeps both encoders frozen and reaches 0.68% clean LRS3 WER with 1,759 h [[5]](#ref-5); the authors' revision reports 0.76% with 1,759 h and beam 1 (arXiv v3), 0.08 points behind (inference).

AVFormer already froze the speech model and visual extractor and trained only adapters and a projection [[3]](#ref-3) (Sec. 3). Freezing "helps retain its strong audio skills" (Sec. 3.2), but no unfrozen control is shown. Verdict: standard.

### M08 Output: one model for transcription and En-X translation

**Usual approach:** 552 of 570 prior VSR/AVSR studies output only a transcript (pattern match, Appendix). The 2 prior translation systems are MuAViC's bilingual AV-HuBERT, one model per pair [[4]](#ref-4), and MixSpeech, from lip video [[7]](#ref-7). Whisper-Flamingo emits English and six En-X outputs from one parameter set (Table 4).

**State of the art:** MTC-AVSR (2026) [later] also uses one model, for four languages; at 0 dB babble it reports BLEU 25.2, 23.5, 20.3, 20.5 (Es, Fr, It, Pt) against 25.4, 22.4, 19.3, 19.9 for Whisper-Flamingo Large as it tabulates them, and bilingual AV-HuBERT keeps the best French score, 23.8 [[8]](#ref-8).

[Concurrent] VSP-LLM, XLAVS-R and SynesLM also translate (Appendix). Video lifts noisy average BLEU from 18.6 to 20.5, still below the per-pair 20.8, as the authors concede (Sec. 3.4). The clean lead, 22.9 against 21.9, is Whisper's: audio-only Whisper-Large scores 22.7 (Table 4). Verdict: standard.

### M12 Evaluation: noise files, beam size, single runs (incidental)

**Usual approach:** 125 of 159 prior AVSR studies show no run-variability pattern (pattern match, Appendix); this paper also reports single runs, and its code fixes seed 3407.

**State of the art:** USR 2.0 (2026) [later] reports mean and standard deviation over three random seeds on LRS3 [[9]](#ref-9). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Voiced TED speech | Voiced speech | – | standard |
| M02 Training-only supervision | Transcripts, translations | Text labels | – | standard |
| M03 Training and adaptation | Whisper fine-tuned, then frozen; new layers trained | End-to-end or full fine-tuning; of 359 prior (pattern match 166) | [[5]](#ref-5) 0.68%, frozen encoders [later] | standard |
| M04 Use-time action | Voiced speech, added noise | Voiced speech | – | standard |
| M05 Sensors | Mouth crops; log-Mel audio | Camera plus microphone | – | standard |
| M06 Processing and decoding | Gated cross-attention in Whisper decoder | Concatenation; of 159 prior (pattern match 97) | [[5]](#ref-5) 3.8% at 0 dB babble [later] | standard |
| M07 Lexicon and LM | No external LM; beam 15 | Neural LM or none | – | standard |
| M08 Output | One model: transcript and six En-X | Transcript only; of 570 prior (pattern match 552) | [[8]](#ref-8) one model, Es BLEU 25.2 [later] | standard |
| M09 Confirmation | None | Mostly absent | – | not applicable |
| M10 Correction | None | Mostly absent | – | not applicable |
| M11 Reference construction | LRS3, MuAViC test splits | Public split | – | standard |
| M12 Evaluation | Single runs; recreated noise | Single run; of 159 prior (pattern match 125) | [[9]](#ref-9) three seeds [later] | standard |
| M13 Device and cost | 2.5B parameters, GPUs; no latency | Cost often reported | – | standard |

## Where the claims outrun the evidence

- Clean LRS3, 2.3% to 1.5% (Table 3): at beam 1 the revision gives 1.1% against 1.0% (arXiv v3).
- The 52.1% relative noisy gain (Sec. 3.3) is a beam-15 figure; at beam 1, 12.4% to 7.2% is 42% (inference; arXiv v3, Table 3).
- "Slightly better" than AV-HuBERT (5.6% against 5.8%, Sec. 3.3) uses recreated noise, as the authors note; u-HuBERT (4.6%) was not tried as encoder, and the revision finds AV-HuBERT and CMA ahead at SNR ≤ 0 (arXiv v3, App. 8.2).
- "Significantly" (Sec. 1) has no test or seeds.
- The MuAViC noise file differs from the baseline's (Sec. 3.4), so 20.5 against 20.8 is not like-for-like.

## What the field needs next

- M06: early fusion, encoder insertion and gated decoder attention at equal trainable parameters, across sizes and seeds.
- M12: public LRS3 and MuAViC noise files at fixed SNRs; beam 1 and beam N for every baseline.
- M03: an unfrozen variant at equal steps.

## Questions for the authors

- Why decode the audio-only baseline with beam 15 when beam 1 gives 1.1%?
- How many MuAViC test utterances per language enter Table 4?
- How much do results vary across seeds?

## Appendix: literature search

- Setting: sentence-level AVSR on LRS3 and audio-visual En-X translation on MuAViC. Dated against 2024-06: prior before 2023-12, [concurrent] 2023-12 to 2024-12, [later] after 2024-12. Counts are full-text pattern matches with related-work mentions (upper bounds), versions once by key, target excluded.
- M06, avsr-stream-fusion-and-weighting (published table, appended). Inclusion rule: the published rule (AVSR studies classified by fusion design). Ledger counts: 7,345 unique studies slot-filled for M06; 349 unique studies pattern match (348 without the target). Prior 159: concatenation 97, cross-modal attention 14, gated cross-attention 0, Whisper, USM or BEST-RQ named 5. [Concurrent] 29: gated cross-attention 0. [Later] 100: gated cross-attention 12. Read: [[2]](#ref-2), [[3]](#ref-3), [[6]](#ref-6) (prior); [[5]](#ref-5) (state of the art). Known-item recall 1.0.
- M03, frozen-encoder-parameter-efficient-training-vsr (published table, appended). Inclusion rule: the published rule (VSR/AVSR studies classified by training regime). Ledger counts: 1,526 unique studies slot-filled for M03; 740 unique studies pattern match (739 without the target). Prior 359: end-to-end or full fine-tuning 166, frozen encoder 15, adapters or prompt tuning 9, LoRA 1. Read: [[3]](#ref-3) (prior); [[5]](#ref-5) (state of the art). Known-item recall 1.0.
- M08, audio-visual-speech-translation-output (new). Inclusion rule: VSR/AVSR studies whose full text names speech-to-text translation or BLEU, classified by hand into translation systems from lip or audio-visual input versus BLEU as a transcription metric or a mention; speech-to-speech and sign-language translation are out. Ledger counts: 3,268 unique studies slot-filled for M08; 1,049 unique studies pattern match. Prior 570: translation pattern 18, translation systems 2. [Concurrent] 53: translation pattern 7, including VSP-LLM, XLAVS-R and SynesLM. Read: [[4]](#ref-4), [[7]](#ref-7) (prior); [[8]](#ref-8) (state of the art). Known-item recall 1.0.
- M12, avsr-noise-and-run-variability-protocol (published table, appended). Inclusion rule: the published rule and regexes over the AVSR population. Ledger counts: 6,960 unique studies slot-filled for M12; 349 unique studies pattern match. Prior 159: run-variability pattern 34, babble 54, LRS3 38. Read: [[9]](#ref-9) (state of the art). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Rouditchenko, A., Gong, Y., Thomas, S., Karlinsky, L., Kuehne, H., Feris, R., et al. “Whisper-Flamingo: Integrating Visual Features into Whisper for Audio-Visual Speech Recognition and Translation.” *Interspeech 2024*, 2024, 2420-2424. doi:[10.21437/Interspeech.2024-322](https://doi.org/10.21437/Interspeech.2024-322). arXiv:[2406.10082](https://arxiv.org/abs/2406.10082). Reviewed version: Interspeech 2024 proceedings. arXiv v3 (2024-11-19) adds beam-1 and 1,759 h rows and an appendix on noise types; cited as 'arXiv v3'. [wiki: in24-whisperflamingo](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/in24-whisperflamingo/article.md) [wiki: isca-rouditchenko24-whisperflamingo](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-rouditchenko24-whisperflamingo/article.md) [wiki: isca-rouditchenko24_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-rouditchenko24_interspeech/article.md) [wiki: arxiv-2406.10082](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2406.10082/article.md)
2. <a id="ref-2"></a>Afouras, T., Chung, J. S., Senior, A., Vinyals, O., Zisserman, A. “Deep Audio-Visual Speech Recognition.” *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 2018. doi:[10.1109/TPAMI.2018.2889052](https://doi.org/10.1109/TPAMI.2018.2889052). arXiv:[1809.02108](https://arxiv.org/abs/1809.02108). Prior; deciding prior for M06 (separate audio and video attention in every decoder layer). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/deep-audio-visual-speech-recognition) [wiki: arxiv-1809.02108](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1809.02108/article.md) [wiki: doi-10.1109-tpami.2018.2889052](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tpami.2018.2889052/article.md)
3. <a id="ref-3"></a>Seo, P. H., Nagrani, A., Schmid, C. “AVFormer: Injecting Vision into Frozen Speech Models for Zero-Shot AV-ASR.” *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2023. <https://openaccess.thecvf.com/content/CVPR2023/papers/Seo_AVFormer_Injecting_Vision_Into_Frozen_Speech_Models_for_Zero-Shot_AV-ASR_CVPR_2023_paper.pdf> Prior; deciding prior for M03 and M06 (frozen ASR, adapters, full-frame visual tokens). [wiki: cvf-seo23-avformer](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-seo23-avformer/article.md)
4. <a id="ref-4"></a>Anwar, M., Shi, B., Goswami, V., Hsu, W., Pino, J., Wang, C. “MuAViC: A Multilingual Audio-Visual Corpus for Robust Speech Recognition and Robust Speech-to-Text Translation.” *Interspeech 2023*, 2023. doi:[10.21437/Interspeech.2023-2279](https://doi.org/10.21437/Interspeech.2023-2279). arXiv:[2303.00628](https://arxiv.org/abs/2303.00628). Prior; deciding prior for M08 (bilingual AV-HuBERT per language pair). [wiki: arxiv-2303.00628](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2303.00628/article.md) [wiki: isca-anwar23-muavic](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-anwar23-muavic/article.md) [wiki: isca-anwar23_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-anwar23_interspeech/article.md)
5. <a id="ref-5"></a>Cheng, Z. “DoubleHelix: Structured Cross-Modal Fusion for Audio-Visual Speech Recognition with LLMs.” *arXiv preprint*, 2026. arXiv:[2607.29112](https://arxiv.org/abs/2607.29112). State of the art for M06 and M03 (LRS3 AVSR). Preprint, v1. [later] [wiki: arxiv-2607.29112](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2607.29112/article.md) [wiki: arxiv-2607-29112-doublehelix](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2607-29112-doublehelix/article.md) [wiki: arxiv-2607.29112-doublehelix](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2607.29112-doublehelix/article.md)
6. <a id="ref-6"></a>Peng, P., Yan, B., Watanabe, S., Harwath, D. “Prompting the Hidden Talent of Web-Scale Speech Models for Zero-Shot Task Generalization.” *Interspeech 2023*, 2023. arXiv:[2305.11095](https://arxiv.org/abs/2305.11095). Prior; deciding prior for M06 (visual prompts into Whisper). [wiki: arxiv-2305.11095](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2305.11095/article.md)
7. <a id="ref-7"></a>Cheng, X., Jin, T., Huang, R., Li, L., Lin, W., Wang, Z., et al. “MixSpeech: Cross-Modality Self-Learning with Audio-Visual Stream Mixup for Visual Speech Translation and Recognition.” *IEEE/CVF International Conference on Computer Vision (ICCV)*, 2023. doi:[10.1109/ICCV51070.2023.01495](https://doi.org/10.1109/ICCV51070.2023.01495). arXiv:[2303.05309](https://arxiv.org/abs/2303.05309). Prior; deciding prior for M08 (translation from lip video). [wiki: arxiv-2303.05309](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2303.05309/article.md) [wiki: cvf23-cheng_mixspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf23-cheng_mixspeech/article.md)
8. <a id="ref-8"></a>A, L., Duan, Z., Li, J., Bao, F. “MTC-AVSR: Compressed-Token-based Audio-Visual Speech Recognition and Translation with Contrastive Language Alignment.” *Interspeech 2026*, 2026. doi:[10.21437/Interspeech.2026-266](https://doi.org/10.21437/Interspeech.2026-266). State of the art for M08 (MuAViC En-X, one model). [later] [wiki: isca-a26-mtcavsr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-a26-mtcavsr/article.md) [wiki: doi-10.21437-interspeech.2026-266](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.21437-interspeech.2026-266/article.md)
9. <a id="ref-9"></a>Haliassos, A., Mira, R., Petridis, S. “Pay Attention to CTC: Fast and Robust Pseudo-Labelling for Unified Speech Recognition.” *International Conference on Learning Representations (ICLR)*, 2026. arXiv:[2602.19316](https://arxiv.org/abs/2602.19316). State of the art for the M12 run-variability protocol. [later] [wiki: arxiv-2602.19316](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.19316/article.md)
