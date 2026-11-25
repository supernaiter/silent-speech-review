# End-to-End Audio-Visual Speech Recognition with Conformers

Pingchuan Ma, Stavros Petridis, Maja Pantic. arXiv preprint, 2021. [arXiv:2102.06657](https://arxiv.org/abs/2102.06657)

## Verdict

The paper [[1]](#ref-1) changes the recognition back-end (M06: Conformer encoders trained jointly with ResNet-18 front-ends on raw pixels and waveforms) and the use-time language model (M07: a Transformer LM replacing a recurrent one). Both are standard by the verdict rules. Raw-input end-to-end audio-visual training predates it [[2]](#ref-2), and the Conformer, absent from every dated ledger study before it (Appendix), is credited from one LRS2 visual-only ablation step that also swaps the decoder (Table 2). Still, the recipe became a template: [later] Auto-AVSR keeps it and reaches 19.1% LRS3 visual-only WER from 3,448 h [[3]](#ref-3), against 43.3% here, so later gains came from data, not architecture. The main overreach: a "large margin" LRS3 visual-only claim (§5) while Table 4 lists RNN-T at 33.6% [[4]](#ref-4). No result carries seeds or intervals.

## Against the field, component by component

### M06 Processing: Conformer encoder and raw-input end-to-end training

**Usual approach:** among 633 sentence-level lip-reading and AVSR studies (pattern match, unique studies), a recurrent encoder is named most often (233), then the Conformer (200), a Transformer encoder (125) and temporal convolution (123); AVSR audio streams are usually filterbank or MFCC inputs (182 of 349, pattern match).

**State of the art:** the best LRS3 visual-only WER is 12.8%, from the [later] LP Conformer on 100k h of non-public video (2023; 0.9% audio-visual) [[5]](#ref-5); the best audio-visual LRS3 WER is 0.76%, from [later] Whisper-Flamingo (2024) [[6]](#ref-6). The target's 43.3% visual-only and 2.3% audio-visual (LRS3 v0.4) trail these by 30.5 and 1.5 points (inference).

None of the 200 Conformer matches is dated before February 2021, and the three deciding priors read use BLSTMs [[7]](#ref-7), a Transformer encoder on frozen visual features [[8]](#ref-8) and LSTMs [[4]](#ref-4) (Appendix). The "+ Conformer encoder" step (46.2% to 42.4%, 8.2% relative (inference)) replaces encoder and decoder at once (§5), runs once, on LRS2 visual-only only (Table 2). The larger step is end-to-end training (63.5% to 50.9%, Table 2), which [[2]](#ref-2) had shown for raw pixels and waveforms on LRW words. Raw waveform ties log-Mel filterbanks on clean LRS2 (4.3% each, Table 3) and leads by at most 7.5 points at -5 dB babble (Fig. 2), one run per curve. Verdict: standard.

### M07 Use-time language model: Transformer LM

**Usual approach:** a neural LM or LLM rescoring is the most common use-time design in the same population (143 of 633, pattern match; Appendix); the deciding priors decode with a character RNN-LM [[7]](#ref-7) or a 4-layer LSTM LM [[8]](#ref-8). The paper swaps in a Transformer LM trained on 16.2 million words (§4).

**State of the art:** later systems drop the external LM: [later] USR 2.0 reaches 17.6% LRS3 visual-only WER without one (2026) [[9]](#ref-9).

The LM is credited with 4.5 points (42.4% to 37.9%, 10.6% relative (inference)) on LRS2 visual-only only, and Tables 3 and 4 do not mark which rows use it. TM-seq2seq's 48.3% on LRS2 is its with-LM figure [[8]](#ref-8), so the "6× fewer training data" comparison (§5) pits LM-decoded rows without saying so. Verdict: standard.

### M12 Evaluation: comparison rows and noise protocol (incidental)

**Usual approach:** an additive-noise test at stated SNRs appears in 183 of 349 AVSR studies, babble noise in 128, run-to-run variability in 33 (pattern match; Appendix). The paper follows the majority.

**State of the art:** 0.76% LRS3 audio-visual WER (2024) [[6]](#ref-6); the closest prior, RNN-T, reports every WER with a 95% confidence interval [[4]](#ref-4).

The RNN-T rows sit in the LRS3 v0.4 table (Table 4), yet RNN-T was scored on an LRS3-TED test set of 1,436 utterances [[4]](#ref-4), while the target's test has 1,321 (§2). The 2.5- and 2.2-point audio-only and audio-visual gains over RNN-T (4.8% and 4.5%) cross test-set versions. Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | LRS2, LRS3 overt speech; noise and crop augmentation | Recorded speech video (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Character transcripts | Text labels (slot-filled 31) | – | standard |
| M03 Training and adaptation | One run per row; optional LRW init; alpha not given | Training records (slot-filled 1,526) | – | standard |
| M04 Use-time action | Overt speech, clean or babble noise | Overt speech (slot-filled 5,595) | – | standard |
| M05 Sensors | 88x88 grayscale mouth crop; raw 16 kHz waveform | Camera video and microphone (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | ResNet-18 front-ends, Conformer encoders, MLP fusion, end-to-end | Recurrent encoder (pattern match 233) | [[5]](#ref-5) (2023): LRS3 VSR WER 12.8% | standard |
| M07 Lexicon and LM | Transformer LM, shallow fusion | Neural LM or LLM rescoring (pattern match 143) | [[9]](#ref-9) (2026): LRS3 VSR WER 17.6%, no external LM | standard |
| M08 Output | Characters | Text output (slot-filled 3,268) | – | standard |
| M09 Confirmation | Offline | Offline (slot-filled 82) | – | not applicable |
| M10 Correction | Offline | Offline (slot-filled 82) | – | not applicable |
| M11 Reference construction | LRS2; LRS3 v0.4 and v0.0 | Corpus references (slot-filled 234) | – | standard |
| M12 Evaluation | Single-run WER; LRS2 babble sweep in a figure | Noise test at stated SNRs (pattern match 183) | [[6]](#ref-6) (2024): LRS3 AVSR WER 0.76% | standard |
| M13 Device and cost | Front-end parameter counts; no runtime | Hardware and cost (slot-filled 6,075) | – | standard |

## Where the claims outrun the evidence

- The "large margin" claim (§5) is contradicted by Table 4: RNN-T's 33.6% is below 43.3%, a 29% relative WER deficit (inference). The defensible claim is efficiency: 595 h against 31,000 h (§5).
- The encoder and decoder swap is one step (§5), so the title credits the Conformer for gains whose largest measured step is end-to-end training (Table 2).
- The claim that deep speech representations are more robust to noise than log-Mel features (§5) rests on one figure, one noise type also used in training (NOISEX babble, §4), and no repeated runs.
- The v0.0 rows (30.4%, 1.3%, 1.2%, Table 4) are called "new state-of-the-art" though the authors concede speaker overlap drives them (§5).
- LM use per row and the clean or noisy status of results are not stated (Table 3, Table 4).

## What the field needs next

- M06: separate encoder and decoder swaps on LRS2 and LRS3 at fixed data, with at least three seeds per row.
- M06: raw waveform against log-Mel under unseen noise types, with per-SNR tables.
- M07: each LRS3 row with and without the external LM.
- M12: all comparison rows re-scored on one LRS3 test version with confidence intervals, as RNN-T did [[4]](#ref-4).

## Questions for the authors

- Which rows of Tables 3 and 4 use the Transformer LM, with what beam settings?
- What CTC weight alpha was used in training, and how was the checkpoint selected?
- On which LRS3 test version was the RNN-T comparison run?

## Appendix: literature search

- M06 / sentence-lipreading-encoder-architecture. Inclusion rule: sentence-level or open-vocabulary lip reading or AVSR studies (ledger names lip reading, VSR, AVSR or LRS2/LRS3 with sentence-level recognition), classified by the temporal encoder named in the full text; a study counts under every encoder it names; versions once. Ledger: 7,345 slot-filled; 633 pattern match (unique studies). Pattern counts: recurrent 233, Conformer 200, Transformer encoder 125, temporal convolution 123. Conformer matches dated before 2021-02: 0. Read in full: [[7]](#ref-7), [[8]](#ref-8), [[4]](#ref-4) (prior); [[5]](#ref-5), [[3]](#ref-3) (state of the art). Known-item recall 0.83.
- M06 / avsr-audio-stream-input-representation. Inclusion rule: studies whose ledger names AVSR, classified by audio input (raw waveform to a learned front-end, or filterbank/MFCC/spectrogram); a study counts under each it names; versions once. Ledger: 7,345 slot-filled; 349 pattern match (unique studies). Pattern counts: filterbank or MFCC 182, raw waveform 45. Read in full: [[2]](#ref-2), [[7]](#ref-7), [[4]](#ref-4) (prior); [[6]](#ref-6) (state of the art). Known-item recall 0.8.
- M07 / use-time-language-model-visual-speech (published table, reused). Inclusion rule: the same 633-study population, classified by use-time language information (n-gram LM, neural LM or LLM rescoring, explicit no external LM). Ledger: 119 slot-filled; 633 pattern match (unique studies). Usual: neural LM or LLM rescoring, 143 (pattern match). Read in full for this review: [[7]](#ref-7), [[8]](#ref-8) (prior); [[9]](#ref-9) (state of the art). Known-item recall 1.0.
- M12 / avsr-noise-and-run-variability-protocol. Inclusion rule: the 349-study AVSR population, classified by additive-noise test at stated SNRs, babble noise, and run variability (seeds, repeated runs, confidence intervals); a study counts under each it names. Ledger: 6,960 slot-filled; 349 pattern match (unique studies). Pattern counts: noise at stated SNR 183, babble 128, run variability 33. Read in full: [[4]](#ref-4), [[8]](#ref-8) (prior); [[6]](#ref-6) (state of the art).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Ma, P., Petridis, S., Pantic, M. “End-to-End Audio-Visual Speech Recognition with Conformers.” *arXiv preprint*, 2021. doi:[10.48550/arXiv.2102.06657](https://doi.org/10.48550/arXiv.2102.06657). arXiv:[2102.06657](https://arxiv.org/abs/2102.06657). Target. Read as arXiv v1. [wiki: arxiv-2102.06657](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2102.06657/article.md)
2. <a id="ref-2"></a>Petridis, S., Stafylakis, T., Ma, P., Cai, F., Tzimiropoulos, G., Pantic, M. “End-to-End Audiovisual Speech Recognition.” *Proc. IEEE ICASSP 2018*, 2018. doi:[10.1109/ICASSP.2018.8461326](https://doi.org/10.1109/ICASSP.2018.8461326). arXiv:[1802.06424](https://arxiv.org/abs/1802.06424). Prior; deciding prior for M06 (raw pixels and waveforms, LRW words). [wiki: arxiv-1802.06424](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1802.06424/article.md)
3. <a id="ref-3"></a>Ma, P., Haliassos, A., Fernandez-Lopez, A., Chen, H., Petridis, S., Pantic, M. “Auto-AVSR: Audio-Visual Speech Recognition with Automatic Labels.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2023. doi:[10.1109/ICASSP49357.2023.10096889](https://doi.org/10.1109/ICASSP49357.2023.10096889). arXiv:[2303.14307](https://arxiv.org/abs/2303.14307). [later]; same group, same Conformer recipe at 3,448 h. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/auto-avsr-audio-visual-speech-recognition-with-automatic-labels) [wiki: arxiv-2303.14307](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2303.14307/article.md)
4. <a id="ref-4"></a>Makino, T., Liao, H., Assael, Y., Shillingford, B., Garcia, B., Braga, O., et al. “Recurrent Neural Network Transducer for Audio-Visual Speech Recognition.” *IEEE Automatic Speech Recognition and Understanding Workshop (ASRU)*, 2019. doi:[10.1109/ASRU46091.2019.9004036](https://doi.org/10.1109/ASRU46091.2019.9004036). arXiv:[1911.04890](https://arxiv.org/abs/1911.04890). Prior; LSTM RNN-T on 31k h YouTube, LRS3 comparison row. [wiki: arxiv-1911.04890](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1911.04890/article.md) [wiki: doi-10.1109-asru46091.2019.9004036](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-asru46091.2019.9004036/article.md)
5. <a id="ref-5"></a>Chang, O., Liao, H., Serdyuk, D., Shah, A., Siohan, O. “Conformers are All You Need for Visual Speech Recognition.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2024, 10136-10140. arXiv:[2302.10915](https://arxiv.org/abs/2302.10915). [later]; best LRS3 visual-only WER (non-public data). [later] [wiki: arxiv-2302.10915](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2302.10915/article.md)
6. <a id="ref-6"></a>Rouditchenko, A., Gong, Y., Thomas, S., Karlinsky, L., Kuehne, H., Feris, R., et al. “Whisper-Flamingo: Integrating Visual Features into Whisper for Audio-Visual Speech Recognition and Translation.” *Interspeech 2024*, 2024. arXiv:[2406.10082](https://arxiv.org/abs/2406.10082). [later]; LRS3 AVSR state of the art. [later] [wiki: arxiv-2406.10082](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2406.10082/article.md) [wiki: isca-rouditchenko24-whisperflamingo](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-rouditchenko24-whisperflamingo/article.md) [wiki: in24-whisperflamingo](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/in24-whisperflamingo/article.md) [wiki: isca-rouditchenko24_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-rouditchenko24_interspeech/article.md)
7. <a id="ref-7"></a>Petridis, S., Stafylakis, T., Ma, P., Tzimiropoulos, G., Pantic, M. “Audio-Visual Speech Recognition with a Hybrid CTC/Attention Architecture.” *Proc. IEEE Spoken Language Technology Workshop (SLT)*, 2018. doi:[10.1109/SLT.2018.8639643](https://doi.org/10.1109/SLT.2018.8639643). arXiv:[1810.00108](https://arxiv.org/abs/1810.00108). Prior; the target's baseline lineage (BLSTM encoder, RNN-LM). [wiki: arxiv-1810.00108](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1810.00108/article.md) [wiki: doi-10.1109-slt.2018.8639643](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-slt.2018.8639643/article.md)
8. <a id="ref-8"></a>Afouras, T., Chung, J. S., Senior, A., Vinyals, O., Zisserman, A. “Deep Audio-Visual Speech Recognition.” *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 2018. doi:[10.1109/TPAMI.2018.2889052](https://doi.org/10.1109/TPAMI.2018.2889052). arXiv:[1809.02108](https://arxiv.org/abs/1809.02108). Prior; Transformer encoder on frozen visual features, LSTM language model. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/deep-audio-visual-speech-recognition) [wiki: arxiv-1809.02108](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1809.02108/article.md) [wiki: doi-10.1109-tpami.2018.2889052](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tpami.2018.2889052/article.md)
9. <a id="ref-9"></a>Haliassos, A., Mira, R., Petridis, S. “Pay Attention to CTC: Fast and Robust Pseudo-Labelling for Unified Speech Recognition.” *International Conference on Learning Representations (ICLR)*, 2026. arXiv:[2602.19316](https://arxiv.org/abs/2602.19316). [later]; LRS3 VSR without an external language model. [later] [wiki: arxiv-2602.19316](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.19316/article.md)
