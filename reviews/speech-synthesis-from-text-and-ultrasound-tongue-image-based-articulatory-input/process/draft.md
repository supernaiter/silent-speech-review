# Speech Synthesis from Text and Ultrasound Tongue Image-based Articulatory Input

Csapó, T. G., Tóth, L., Gosztolya, G., Markó, A. · arXiv preprint · 2021 · [arXiv:2107.02003](https://arxiv.org/abs/2107.02003)

## Verdict

The paper changes one component: the acoustic model of a Merlin DNN-TTS receives 128 PCA coefficients of the ultrasound tongue image next to the linguistic features (M06) [[1]](#ref-1). The network is the field's usual frame-wise fully connected regression, so M06 is standard; the pairing is new only in its sensor, as the paper's own Sec. 1.3 scopes it after EMA-based articulatory TTS. Test MCD falls for all 8 speakers, but by 0.015 to 0.229 dB, about 2% on average, from one run per speaker on roughly 10 test sentences (Table 1, Sec. 2.1; inference). On the test set BAP error rises for 6 of 8 speakers and voicing error for all 8 (Tables 2, 5; inference), so the excitation claim fails. Naturalness is claimed (Abstract, Sec. 5) without the listening test the same group ran in at least 4 earlier ultrasound-to-speech studies (M12, behind). The ultrasound input is a recording of the very utterance being scored, and the system needs text and articulation together, which the authors concede rules out TTS or silent-speech use (Sec. 5).

## Against the field, component by component

### M06 Acoustic model: text plus ultrasound input

**Usual approach:** Of 51 ultrasound-to-speech studies (pattern match, Appendix), 37 name a fully connected DNN and 31 a CNN regressing vocoder or mel features frame by frame [[2]](#ref-2), [[3]](#ref-3). The paper keeps that design, six hidden layers of 1,024 units predicting WORLD features at 5 ms steps (Sec. 2.3), and only adds one PCA-compressed ultrasound frame per step to the text input.

**State of the art:** Tongue2Speech [later] (2026) reaches 15.93% ASR WER on single-speaker TaL1 with a spatio-temporal CNN and Transformer [[4]](#ref-4). The paper reports no intelligibility, so no common metric exists; by design it trails on temporal context and vocoder.

Multi-frame input was already established: the group's 2017 DNN took 5 images [[2]](#ref-2), and a 3D CNN reported about 21% lower test MSE in a relative sense [[5]](#ref-5). Here a single resampled frame enters (Sec. 2.2). By the paper's account, Cao et al. used EMA as training targets or through a separate articulatory-to-acoustic network (Sec. 1.3); feeding measured articulation of the test utterance at synthesis is this paper's choice. Text carries almost all of the result: test MCD is 5.447 to 6.566 dB from text alone against 7.050 to 8.396 dB from ultrasound alone (Table 1). Verdict: standard; the gain is shown for the spectrum only.

### M05 Sensor: probe position (incidental)

**Usual approach:** Inherited: midsagittal Micro ultrasound at 81.5 fps from UltraSuite-TaL80 (Sec. 2.1), as in the group's earlier data at 81.67 fps [[6]](#ref-6).

**State of the art:** The misalignment measure, MSE between per-utterance mean images, comes from 2020 work that tied it to no recognition or synthesis outcome [[7]](#ref-7); this paper adds a qualitative link to synthesis error.

Speakers whose test images differ from training show higher MCD (Fig. 2), a visual association the authors concede is unquantified (Sec. 4.2). The combined-system gain does not follow it: 04me, flagged as misaligned, has the largest test-MCD gain, 0.229 dB (Table 1; inference). Verdict: standard.

### M12 Evaluation: objective errors only (incidental)

**Usual approach:** Of the 51 studies, 21 report MCD and 14 a MUSHRA test (pattern match, Appendix). The paper reports MCD, BAP and three F0 errors (Sec. 3), no listener test, yet concludes that combined input "may increase the naturalness" (Abstract, Sec. 5).

**State of the art:** Tongue2Speech [later] (2026) scores its output with ASR, 31.64% WER on TaL80 [[4]](#ref-4); this paper has no intelligibility measure to compare.

Against the best comparable work, the authors' own, it is behind: listening tests with 23 listeners in 2017 [[2]](#ref-2), 24 in 2018 [[8]](#ref-8), 23 in 2019 [[6]](#ref-6) and 22 in 2020 [[3]](#ref-3). Published samples (Sec. 3) were not rated.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Read sentences, TaL80 | Recorded read or overt speech (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | WORLD features of paired audio | Paired-audio targets (slot-filled 31) | – | standard |
| M03 Training and adaptation | Per-speaker DNN, one run | Training records (slot-filled 1,526) | – | standard |
| M04 Use-time action | Audible reading, text supplied | Silent or overt (slot-filled 5,595) | – | standard |
| M05 Sensors | Micro probe, 81.5 fps, PCA 128 | Midsagittal ultrasound (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | Text + 1 UTI frame, 6x1024 MLP | Frame-wise DNN or CNN (pattern match 37) | [[4]](#ref-4) (2026): WER 15.93% TaL1 | standard |
| M07 Lexicon and LM | Merlin text front end | No use-time aid (slot-filled 119) | – | not applicable |
| M08 Output | WORLD waveform | Waveform (slot-filled 3,268) | – | standard |
| M09 Confirmation | Offline | Offline (slot-filled 82) | – | not applicable |
| M10 Correction | Offline | Offline (slot-filled 82) | – | not applicable |
| M11 Reference construction | Synchronous TaL80 audio | Parallel recordings (slot-filled 234) | – | standard |
| M12 Evaluation | MCD, BAP, F0 errors only | MCD with MUSHRA (pattern match 21) | [[4]](#ref-4) (2026): WER 31.64% TaL80 | behind |
| M13 Device and cost | Needs text and ultrasound | Operating constraints (slot-filled 6,075) | – | not applicable |

## Where the claims outrun the evidence

- "Useful for the spectral and BAP prediction" (Sec. 3) holds for BAP only on the development set; on test, BAP error is higher than text-only for 6 of 8 speakers, for example 0.450 to 0.464 for 07me (Table 2; inference).
- The authors say ultrasound "did not help" voicing (Sec. 3); test voicing error in fact rises for all 8 speakers, for example 6.828 to 7.674 for 03mn (Table 5; inference).
- The ultrasound is recorded in sync with the reference utterance (Sec. 2.1) and carries its articulation and timing. With no control using another repetition, a mismatched utterance or 128 dimensions of noise, the MCD gain is not attributable to articulatory knowledge (Table 1).
- Durations are not modelled (Sec. 2.3), so all systems use reference timing (inference).

## What the field needs next

- M06: a mismatched-token control (ultrasound of another repetition, or ultrasound predicted from text) to separate articulatory knowledge from leakage.
- M06: a multi-frame ultrasound encoder in the fusion, plus a duration model.
- M12: MUSHRA or MOS and ASR WER on TaL80 output, with significance across speakers, on the scale of [[4]](#ref-4).
- M05: re-mount the probe between sessions and regress synthesis error on the measures of [[7]](#ref-7).

## Questions for the authors

- Which durations drive the systems at test time: forced-aligned natural durations?
- How many utterances are in each test set?
- How many runs and which seeds stand behind each cell, and what test supports "significantly lower"?
- What are the units of BAP, F0-RMSE and voicing error in Tables 2 to 5?

## Appendix: literature search

- M06, ultrasound-to-speech-network-architecture (published table, reused). Inclusion rule: studies that map ultrasound tongue images (with or without lip video) to acoustic features or a waveform with a trained network and name the mapping architecture; ultrasound-to-text recognition, contour tracking, ultrasound prediction from other signals and reviews excluded; versions count once. Ledger: 7,345 unique studies slot-filled for M06; 51 unique studies pattern match. Usual design: frame-wise neural regression, fully connected DNN 37, CNN 31, recurrent 25, 3D CNN 19 (pattern match, published counts). Read in full: [[5]](#ref-5), [[2]](#ref-2), [[6]](#ref-6), [[4]](#ref-4). Known-item recall 1.0 (published seeds); 0.83 for this review's cited seeds.
- M12, ultrasound-to-speech-output-evaluation (published table, reused). Inclusion rule: the same ultrasound-to-speech population, classified by the output measures used (MCD or other spectral distance, MUSHRA or MOS, listener transcription, ASR on the output); recognition-only studies, contour tracking and reviews excluded; versions count once. Ledger: 6,960 unique studies slot-filled for M12; 51 unique studies pattern match. Measures: MCD 21, MUSHRA 14, listener intelligibility 5, MOS 4, ASR on the output 3 (pattern match, published counts); earlier listening-test studies from the target's group 4 (pattern match). Read in full: [[3]](#ref-3), [[2]](#ref-2), [[8]](#ref-8), [[4]](#ref-4). Known-item recall 0.57 (published seeds); 0.83 for this review's cited seeds.
- M05, transducer misalignment (no tally; incidental). Read in full: [[7]](#ref-7).

## References

Numbered by first citation. BibTeX in the same order and keys: [speech-synthesis-from-text-and-ultrasound-tongue-image-based-articulatory-input.bib](speech-synthesis-from-text-and-ultrasound-tongue-image-based-articulatory-input.bib).

1. <a id="ref-1"></a>Csapó, T. G., Tóth, L., Gosztolya, G., Markó, A. “Speech Synthesis from Text and Ultrasound Tongue Image-based Articulatory Input.” *arXiv preprint*, 2021. doi:[10.48550/arXiv.2107.02003](https://doi.org/10.48550/arXiv.2107.02003). arXiv:[2107.02003](https://arxiv.org/abs/2107.02003). Target. Read as arXiv v1. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/speech-synthesis-from-text-and-ultrasound-tongue-image-based-articulatory-input) [wiki: arxiv-2107.02003](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2107.02003/article.md)
2. <a id="ref-2"></a>Csapó, T. G., Grósz, T., Gosztolya, G., Tóth, L., Markó, A. “DNN-Based Ultrasound-to-Speech Conversion for a Silent Speech Interface.” *Proc. Interspeech 2017*, 2017, 3672–3676. doi:[10.21437/Interspeech.2017-939](https://doi.org/10.21437/Interspeech.2017-939). Prior; read (published M06 and M12 tables). [wiki: isca-csapo17-us2speech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-csapo17-us2speech/article.md) [wiki: isca-csapo17_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-csapo17_interspeech/article.md) [wiki: isca-csapo17_ussynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-csapo17_ussynth/article.md) [wiki: isca-csapo17_ustospeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-csapo17_ustospeech/article.md)
3. <a id="ref-3"></a>Csapó, T. G., Zainkó, C., Tóth, L., Gosztolya, G., Markó, A. “Ultrasound-based Articulatory-to-Acoustic Mapping with WaveGlow Speech Synthesis.” *Proc. Interspeech 2020*, 2020, 2727–2731. doi:[10.21437/Interspeech.2020-1031](https://doi.org/10.21437/Interspeech.2020-1031). arXiv:[2008.03152](https://arxiv.org/abs/2008.03152). Prior; deciding prior for M12 (behind). [wiki: isca-csapo20b-uswaveglow](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-csapo20b-uswaveglow/article.md) [wiki: isca-csapo20b_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-csapo20b_interspeech/article.md) [wiki: arxiv-2008.03152](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2008.03152/article.md)
4. <a id="ref-4"></a>Sonkar, Y., Kilaru, Y., Yelimeli, S., Shah, N., Gandhi, V. “Tongue2Speech: Real-Time Speech Synthesis from Tongue Ultrasound Videos via Spatiotemporal Transformers.” *Proc. Interspeech 2026*, 2026, 6856–6860. doi:[10.21437/Interspeech.2026-3023](https://doi.org/10.21437/Interspeech.2026-3023). Later; state of the art for M06 and M12 (published tables). [later] [wiki: isca-sonkar26_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-sonkar26_interspeech/article.md)
5. <a id="ref-5"></a>Tóth, L., Shandiz, A. H. “3D Convolutional Neural Networks for Ultrasound-Based Silent Speech Interfaces.” *Artificial Intelligence and Soft Computing (ICAISC 2020), Lecture Notes in Computer Science 12415*, 2020, 159–169. doi:[10.1007/978-3-030-61401-0_16](https://doi.org/10.1007/978-3-030-61401-0_16). arXiv:[2104.11532](https://arxiv.org/abs/2104.11532). Prior; multi-frame input (M06). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/3d-convolutional-neural-networks-for-ultrasound-based-silent-speech-interfaces) [wiki: arxiv-2104.11532](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2104.11532/article.md)
6. <a id="ref-6"></a>Csapó, T. G., Al-Radhi, M. S., Németh, G., Gosztolya, G., Grósz, T., Tóth, L., et al. “Ultrasound-based Silent Speech Interface Built on a Continuous Vocoder.” *Proc. Interspeech 2019*, 2019. doi:[10.21437/Interspeech.2019-2046](https://doi.org/10.21437/Interspeech.2019-2046). Prior; read (M05 recording rate, M12 listening test). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/ultrasound-based-silent-speech-interface-built-on-a-continuous-vocoder) [wiki: isca-csapo19-usvocoder](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-csapo19-usvocoder/article.md) [wiki: doi-10.21437-interspeech.2019-2046](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.21437-interspeech.2019-2046/article.md) [wiki: isca-csapo19_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-csapo19_interspeech/article.md)
7. <a id="ref-7"></a>Csapó, T. G., Xu, K. “Quantification of Transducer Misalignment in Ultrasound Tongue Imaging.” *arXiv preprint*, 2020. doi:[10.48550/arXiv.2008.02470](https://doi.org/10.48550/arXiv.2008.02470). arXiv:[2008.02470](https://arxiv.org/abs/2008.02470). Prior; misalignment measure (M05). [wiki: arxiv-2008.02470](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2008.02470/article.md)
8. <a id="ref-8"></a>Grósz, T., Gosztolya, G., Tóth, L., Csapó, T. G., Markó, A. “F0 Estimation for DNN-Based Ultrasound Silent Speech Interfaces.” *Proc. IEEE ICASSP 2018*, 2018, 291–295. doi:[10.1109/ICASSP.2018.8461732](https://doi.org/10.1109/ICASSP.2018.8461732). Prior; listening test (M12). [wiki: doi-10-1109-icassp-2018-8461732](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10-1109-icassp-2018-8461732/article.md)
