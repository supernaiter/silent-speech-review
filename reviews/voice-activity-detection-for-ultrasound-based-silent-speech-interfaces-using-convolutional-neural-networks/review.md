# Voice Activity Detection for Ultrasound-based Silent Speech Interfaces using Convolutional Neural Networks

Amin Honarmandi Shandiz, László Tóth. arXiv preprint, 2021. [arXiv:2105.13718](https://arxiv.org/abs/2105.13718)

## Verdict

The paper [[1]](#ref-1) changes two components: a single-frame 2D CNN labelling ultrasound tongue frames as speech or silence (M06), trained on acoustic-VAD labels from the parallel audio (M02). Both are standard: a single-frame CNN VAD on lip images with audio-derived labels dates from 2015 [[2]](#ref-2), and an ultrasound tongue-activity speech detector from 2019 [[3]](#ref-3); the paper discusses only acoustic VAD (Sec. 3). The evaluation (M12) is behind the best comparable work: four checked earlier non-acoustic VAD studies (of 46 pattern matches, Appendix) tested held-out speakers, the best reaching 92.2% on unseen GRID speakers with lip video [[4]](#ref-4); this paper tests one speaker on a file split, holding out no TaL1 session. Accuracy 0.852 is about 11 points above always answering "speech", and 43% of silence frames are kept (inference, Table 6). The claim that ultrasound VAD "performed similarly" to speech VAD (Sec. 5.4) rests on MCD changes of 0.01 to 0.05 and MSE changes of mixed sign, with no repeated runs or test.

## Against the field, component by component

### M06 Processing: speech activity detection from a non-acoustic signal

**Usual approach:** Among 119 unique non-acoustic VAD studies (pattern match, upper bound, Appendix), the full text names classical SVM, GMM or HMM classifiers (74), temporal smoothing (42), CNNs (37) and recurrent networks (36). The paper uses a CNN on one frame with no temporal context or smoothing (Sec. 4.2).

**State of the art:** In 2019, a CNN and unidirectional LSTM reached 92.2% frame-level accuracy on held-out GRID speakers (column SiA; 96.5% under SdA) [[4]](#ref-4).

The design predates the paper: a single-frame CNN on mouth pixels gave 96.99% speaker-dependent VAD accuracy [[2]](#ref-2); a CNN detected mouth state from reflected ultrasonic chirps as a VAD [[5]](#ref-5); and ultrasound echo variance was thresholded as "estimated tongue activity" to find child speech [[3]](#ref-3). Only the tongue-image input is new. Verdict: standard.

### M02 Training-only supervision: labels from the synchronized audio

**Usual approach:** In the same population, audio-derived labels appear in 23 studies (forced alignment 17, acoustic VAD or energy 6) and manual annotation in 22 (pattern match, Appendix). The paper uses the coarser VAD form (WebRTC, Sec. 5.3).

**State of the art:** Labels from GRID alignment files (2019) [[4]](#ref-4), as in [[2]](#ref-2).

Verdict: standard, since audio-derived labels are the common route. With no hand-checked frames and the VAD mode unstated (Sec. 5.1), 0.852 measures agreement with WebRTC, not with speech.

### M12 Evaluation: protocol for the detector

**Usual approach:** Of the 119 studies, 46 mention a held-out-speaker or leave-one-subject-out test, 30 a single speaker and 13 a held-out session (pattern match, Appendix).

**State of the art:** Held-out speakers: 27 training, 3 validation, 2 test (2019) [[4]](#ref-4).

All results come from one TaL1 speaker on a file split (train 1015, validation 50, test 24; Sec. 4.1), although TaL1 has six sessions and its corpus paper [concurrent] benchmarks by leaving one out [[6]](#ref-6). The cost is known: the single-frame CNN fell from 96.99% to 74.07% on held-out speakers [[2]](#ref-2), a 24% relative drop (inference), and an unadapted ultrasound synthesis model on a new session scored MUSHRA naturalness 1.19 on a 0 to 100 scale [[7]](#ref-7). The comparators are lip-video studies on other corpora; the like-for-like gap is the session split TaL1 allowed. Verdict: behind the best comparable work [[4]](#ref-4).

### M12 Evaluation: synthesis output (incidental)

**Usual approach:** MCD, the default in ultrasound-to-speech work (21 of 51 studies, pattern match, Appendix), as here.

**State of the art:** A [later] 2026 system reports ASR WER of 31.64% on synthesized TaL80 speech [[8]](#ref-8).

Retained silence raises MCD (Table 3), yet every ultrasound-VAD MCD in Table 7 is 0.01 to 0.05 below Table 4 (3.05 against 3.08 for Conv3D+BiLSTM), with no seeds or test; whether both test sets were trimmed alike is open.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Read speech, TaL1 recordings | Recorded speech sessions (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | WebRTC VAD on parallel audio | Audio-derived labels (alignment 17, VAD 6) (pattern match 23) | [[4]](#ref-4) (2019): alignment labels | standard |
| M03 Training and adaptation | Single speaker; seeds not stated | Training records (slot-filled 1,526) | – | standard |
| M04 Use-time action | Overt read speech | Silent or overt (slot-filled 5,595) | – | standard |
| M05 Sensors | Ultrasound tongue images, 82 fps | Sensor recorded (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | Single-frame 2D CNN, no smoothing | Classical SVM/GMM/HMM (pattern match 74) | [[4]](#ref-4) (2019): 92.2% frame accuracy, unseen speakers | standard |
| M07 Lexicon and LM | None | None recorded (slot-filled 119) | – | not applicable |
| M08 Output | Speech/silence label; mel to WaveGlow | Output types (slot-filled 3,268) | – | standard |
| M09 Confirmation | Offline | Offline (slot-filled 82) | – | not applicable |
| M10 Correction | Offline | Offline (slot-filled 82) | – | not applicable |
| M11 Reference construction | WebRTC labels as reference | Reference construction (slot-filled 234) | – | not reported |
| M12 Evaluation | One speaker, file split | Held-out speakers (pattern match 46) | [[4]](#ref-4) (2019): 92.2% SiA frame accuracy, 27/3/2 speakers | behind |
| M13 Device and cost | Energy saving claimed, not measured | Device constraints (slot-filled 6,075) | – | not reported |

## Where the claims outrun the evidence

- No majority baseline: speech is 8514 of 11453 test frames (Table 6), so always answering "speech" scores 74.3% (inference); kappa 0.57 (Table 5) is the honest figure.
- Weak silence class: 1268 of 2939 test silence frames are labelled speech (Table 6): specificity 57% (inference).
- Mixed MSE: with 180 ms kept, ultrasound VAD lowers MSE (test) from 0.29 to 0.26 but raises MSE (dev) from 0.259 to 0.35 (Conv3D+BiLSTM, Tables 4 and 7), so "slightly better MSE" (Sec. 5.4) is one column.
- The output is described as the probability of silence (Sec. 4.2), but recall 0.95 equals 8096/8514, so speech is the positive class (inference, Tables 5 and 6).

## What the field needs next

- M12: held-out-session tests on TaL1 and held-out-speaker tests on TaL80, with a majority baseline and specificity, as in [[4]](#ref-4).
- M06: a temporal detector (LSTM or smoothing) against the single-frame CNN on the same split.
- M13: measured latency and energy on a wearable (motivation, Sec. 2).

## Questions for the authors

- Which WebRTC VAD version and aggressiveness mode produced the labels?
- Were the train, validation and test files separated by recording session?
- Which threshold produced Tables 5 and 6, and which class is "Positive"?
- In Table 7, was the test set trimmed by the ultrasound VAD or by the speech VAD before MCD was computed?

## Appendix: literature search

- M06, non-acoustic-speech-activity-detection. Inclusion rule: studies detecting speech against non-speech (including voicing, mouth state and endpoints) from lip video, ultrasound, ultrasonic Doppler, radar, EMG, EMA, EEG, MEG or ECoG; audio-visual systems count when a non-acoustic branch is evaluated. Ledger counts: slot-filled 7345; pattern match 119 unique studies (upper bound: papers using an acoustic VAD only for preprocessing also match). Usual design (full-text pattern match): classical SVM, GMM or HMM 74; temporal smoothing 42; CNN 37; recurrent network 36. Read in full: [[2]](#ref-2), [[5]](#ref-5), [[3]](#ref-3), [[4]](#ref-4). Known-item recall: 1.0 (7 seeds).
- M02, audio-derived-speech-activity-labels. Inclusion rule: same population; source of the training labels. Ledger counts: slot-filled 31 (sparse slot); pattern match 119 unique studies. Usual design (full-text pattern match): audio-derived 23 (forced alignment 17; acoustic VAD or energy 6); manual annotation 22. Read in full: [[2]](#ref-2), [[4]](#ref-4). Known-item recall: 1.0 (6 seeds).
- M12, non-acoustic-speech-activity-evaluation-protocol. Inclusion rule: same population; held-out speakers, held-out sessions or a single speaker. Ledger counts: slot-filled 6960; pattern match 119 unique studies. Usual design (full-text pattern match): held-out speakers 46; single speaker 30; held-out sessions 13. Prior non-acoustic VAD studies with a held-out-speaker test, snippets checked: 4 (2013 to 2019). Read in full: [[4]](#ref-4), [[2]](#ref-2), [[5]](#ref-5), [[6]](#ref-6), [[7]](#ref-7).
- M12, ultrasound-to-speech-output-evaluation (published topic table, appended). Inclusion rule: studies synthesizing speech or acoustic features from ultrasound tongue images and evaluating the output. Ledger counts: slot-filled 6960; pattern match 51 unique studies. Usual design: MCD 21, MUSHRA 14 (pattern match). State of the art read in full: [[8]](#ref-8). Known-item recall: 0.57.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Shandiz, A. H., Tóth, L. “Voice Activity Detection for Ultrasound-based Silent Speech Interfaces using Convolutional Neural Networks.” *arXiv preprint*, 2021. doi:[10.48550/arXiv.2105.13718](https://doi.org/10.48550/arXiv.2105.13718). arXiv:[2105.13718](https://arxiv.org/abs/2105.13718). Target. Read as arXiv v3. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/voice-activity-detection-for-ultrasound-based-silent-speech-interfaces-using-convolutional-neural-networks) [wiki: arxiv-2105.13718](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2105.13718/article.md)
2. <a id="ref-2"></a>Le Cornu, T., Milner, B. “Voicing classification of visual speech using convolutional neural networks.” *Proc. FAAVSP 2015*, 2015. <https://www.isca-archive.org/avsp_2015/cornu15_avsp.html> Prior; deciding prior for M06, M02 and M12. [wiki: isca-cornu15_avsp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-cornu15_avsp/article.md)
3. <a id="ref-3"></a>Ribeiro, M. S., Eshky, A., Richmond, K., Renals, S. “Ultrasound Tongue Imaging for Diarization and Alignment of Child Speech Therapy Sessions.” *Proc. Interspeech 2019*, 2019. doi:[10.21437/Interspeech.2019-2612](https://doi.org/10.21437/Interspeech.2019-2612). Prior; deciding prior for M06 (ultrasound tongue activity). [wiki: isca-ribeiro19_usdiarize](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-ribeiro19_usdiarize/article.md)
4. <a id="ref-4"></a>Sharma, T., Aralikatti, R., Margam, D. K., Thanda, A., Roy, S., Pujitha A. K., et al. “Real Time Online Visual End Point Detection Using Unidirectional LSTM.” *Proc. Interspeech 2019*, 2019. doi:[10.21437/Interspeech.2019-3253](https://doi.org/10.21437/Interspeech.2019-3253). Prior; state of the art for M06/M12 (speaker-independent visual VAD). [wiki: isca-sharma19b_vvad](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-sharma19b_vvad/article.md)
5. <a id="ref-5"></a>McLoughlin, I., Song, Y. “Low Frequency Ultrasonic Voice Activity Detection using Convolutional Neural Networks.” *Proc. Interspeech 2015*, 2015. doi:[10.21437/Interspeech.2015-327](https://doi.org/10.21437/Interspeech.2015-327). Prior; CNN VAD from a non-acoustic (ultrasonic) signal. [wiki: isca-mcloughlin15_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-mcloughlin15_interspeech/article.md)
6. <a id="ref-6"></a>Ribeiro, M. S., Sanger, J., Zhang, J., Eshky, A., Wrench, A., Richmond, K., et al. “TaL: A Synchronised Multi-Speaker Corpus of Ultrasound Tongue Imaging, Audio, and Lip Videos.” *Proc. IEEE Spoken Language Technology Workshop (SLT 2021)*, 2021. doi:[10.1109/SLT48900.2021.9383619](https://doi.org/10.1109/SLT48900.2021.9383619). arXiv:[2011.09804](https://arxiv.org/abs/2011.09804). Prior; corpus and session-held-out benchmark. [concurrent] [wiki: arxiv-2011.09804](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2011.09804/article.md) [wiki: doi-10.1109-slt48900.2021.9383619](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-slt48900.2021.9383619/article.md)
7. <a id="ref-7"></a>Gosztolya, G., Grósz, T., Tóth, L., Markó, A., Csapó, T. G. “Applying DNN Adaptation to Reduce the Session Dependency of Ultrasound Tongue Imaging-based Silent Speech Interfaces.” *Acta Polytechnica Hungarica*, 2020, 17(7), 109–124. doi:[10.12700/aph.17.7.2020.7.6](https://doi.org/10.12700/aph.17.7.2020.7.6). Prior; cross-session dependency of ultrasound SSI. [wiki: doi-10.12700-aph.17.7.2020.7.6](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.12700-aph.17.7.2020.7.6/article.md)
8. <a id="ref-8"></a>Sonkar, Y., Kilaru, Y., Yelimeli, S., Shah, N., Gandhi, V. “Tongue2Speech: Real-Time Speech Synthesis from Tongue Ultrasound Videos via Spatiotemporal Transformers.” *Proc. Interspeech 2026*, 2026, 6856–6860. doi:[10.21437/Interspeech.2026-3023](https://doi.org/10.21437/Interspeech.2026-3023). State of the art for ultrasound-to-speech output evaluation. [later] [wiki: isca-sonkar26_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-sonkar26_interspeech/article.md)
