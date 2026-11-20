# Neural Speaker Embeddings for Ultrasound-based Silent Speech Interfaces

Shandiz, A. H., Tóth, L., Gosztolya, G., Markó, A., Csapó, T. G. · Interspeech 2021 · 2021 · [doi:10.21437/Interspeech.2021-1466](https://doi.org/10.21437/Interspeech.2021-1466) · [arXiv:2106.04552](https://arxiv.org/abs/2106.04552)

## Verdict

The paper [[1]](#ref-1) trains an x-vector extractor on ultrasound (M06) and feeds it to a multi-speaker ultrasound-to-spectrum estimator (M03). M03 is standard: speaker vectors estimated from the articulatory signal and given to a shared decoder date from 2019 [[2]](#ref-2). The conditioning gain is 0.014 development and 0.016 test MSE, 2.3% and 2.4% relative (inference), with no repeated runs, on speakers seen in SSI training, as the authors state (Sec. 5.3). M06 is behind on test protocol, against the best comparable work: the 0.70% held-out-speaker error (Table 2) pools segments from one recording session per speaker (inference), so speaker and probe placement are not separated, as [[3]](#ref-3) did by holding out sessions. Nothing shows that the embedding helps a new speaker.

## Against the field, component by component

### M03 Training: speaker-embedding conditioning

**Usual approach:** a speaker embedding computed from reference audio and fed to a shared decoder, 20 of 42 studies (pattern match; Appendix). On the same corpus, TaL conditioned its 75-speaker ultrasound-to-speech decoder on x-vectors extracted from the audio with Kaldi [[4]](#ref-4). The paper departs from this audio-derived design by computing the x-vector from the ultrasound (Sec. 1), a departure [[2]](#ref-2) already made for lip video.

**State of the art:** in 2025, V2SFlow (video-to-speech, not ultrasound) predicts the speaker embedding from silent video and is scored on unseen LRS3 speakers; in one ablation table, dropping it lowers speaker similarity from 0.664 to 0.587 SECS while WER moves from 28.5% to 28.7% [[5]](#ref-5) [later].

Signal-derived vectors appear in 8 of the 42 studies (pattern match; Appendix). The deciding prior [[2]](#ref-2) estimates i-vectors from lip-video features, feeds them to hidden layers, and reports 15% and 10% relative WER gains on unseen GRID speakers. The target's gain is smaller and rests on one run with the same 31 speakers in training and test (Sec. 5.3): MSE 0.603 to 0.589 (development) and 0.669 to 0.653 (test). The x-vector model starts from the transfer-learned multi-speaker weights (Sec. 5.3), so extra training is not separated from speaker information (inference). MSE is a weak yardstick: in [[5]](#ref-5) [later] speaker conditioning moves speaker similarity, not content, and the target reports neither similarity nor unseen-speaker synthesis. Verdict: standard.

### M06 Processing: speaker recognition from ultrasound

**Usual approach:** speaker verification from the non-acoustic stream scored by equal error rate, 34 of 58 studies, 15 of them with a cross-session test (pattern match; Appendix). The paper instead scores closed-set identification on 50 speakers and 1-NN cosine leave-one-out on 31 held-out speakers (Sec. 5.1, 5.2).

**State of the art:** in 2020, 95.22% text-independent identification from 3D lip motion on 68 speakers [[6]](#ref-6); NAM verification across sessions reached 0.04% (male) and 1.1% (female) EER in 2006 [[7]](#ref-7), an EER, not comparable with identification error. The target's 0.70% error is below Wang's 4.78% error (inference), but the starting points differ: 31 against 68 speakers, and neighbours from the same recording.

Three earlier works separate speaker from session: [[7]](#ref-7) (NAM), [[8]](#ref-8) (mouth motion, six sessions) and [[3]](#ref-3), which tests EMG speaker identification on a held-out session: 83% and 84% accuracy against 55% chance. TaL80 has 81 speakers, 16,639 utterances and about 205 per session, so about one session per speaker (inference). TaL did not normalise probe position between sessions [[4]](#ref-4), and the authors note that remounting misaligns the image (Sec. 1): a nearest neighbour within one recording can match probe placement as easily as the speaker. Verdict: behind on test protocol, against the best comparable work [[3]](#ref-3).

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Vocalized TaL80 prompts | Overt speech (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Parallel audio mel targets | Paired audio (slot-filled 31) | – | standard |
| M03 Training and adaptation | Ultrasound x-vector input | Audio-derived embedding (pattern match 20) | SECS 0.587 to 0.664, video-to-speech, 2025 [[5]](#ref-5) [later] | standard |
| M04 Use-time action | Vocalized reading | Overt speech (slot-filled 5,595) | – | standard |
| M05 Sensors | Midsagittal ultrasound, 82 fps | Ultrasound imaging (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | 3D-CNN x-vector, 1-NN cosine | EER verification (pattern match 34) | Session-held-out test: 83-84% vs 55% chance [[3]](#ref-3); 95.22% identification, 68 speakers [[6]](#ref-6) | behind |
| M07 Lexicon and LM | None | None (slot-filled 119) | – | not applicable |
| M08 Output | 80-dim mel, WaveGlow | Spectral features (slot-filled 3,268) | – | standard |
| M09 Confirmation | None | None (slot-filled 82) | – | not applicable |
| M10 Correction | None | None (slot-filled 82) | – | not applicable |
| M11 Reference construction | Parallel speech | Recorded speech (slot-filled 234) | – | standard |
| M12 Evaluation | MSE on seen speakers; 1-NN error | Error vs reference (slot-filled 6,960) | – | not reported |
| M13 Device and cost | Offline laboratory | Offline (slot-filled 6,075) | – | not applicable |

## Where the claims outrun the evidence

- "Generalize nicely to unseen speakers" (Abstract) rests on leave-one-out over pooled development and test segments (Sec. 5.2), and the embedding layer was chosen on that same pool (Sec. 5.2, Table 2): 0.70% is not an untouched test result.
- "Below 3%" (Abstract) is a development-set figure, 1.96% to 3.16% (Table 1); the 1,145 test blocks of the 50-speaker set (Sec. 4) are never scored. Neither recognition table gives a chance level or repeated runs.
- The authors call the gain consistent for both development and test, but marginal (Sec. 5.3); one run per configuration cannot show consistency.
- The single-speaker MSE of about 0.26 is attributed to Fig. 3, a histogram; the values are in Table 3 (Sec. 5.3).
- Test MSE rises 2.5-fold from the single-speaker TaL1 system to the 31-speaker system (Table 3) (inference), on different test speakers; no multi-speaker system gets an MCD or listening score.

## What the field needs next

- M06: ultrasound speaker identification with enrolment and test in different sessions, with chance level and seeds, following [[3]](#ref-3).
- M03: x-vector conditioning tested on speakers held out from SSI training, against a shuffled-embedding control and acoustic x-vectors [[4]](#ref-4), scored by speaker similarity as well as MSE [[5]](#ref-5) [later].
- M12: repeated runs and an intelligibility score for single- and multi-speaker systems.

## Questions for the authors

- Is a segment's nearest neighbour often from the same file?
- What is the speaker-recognition error on the 1,145 test blocks?
- Was the multi-speaker baseline trained as long as the x-vector model that starts from its weights?

## Appendix: literature search

- M03 speaker-embedding-conditioning (new topic table). Inclusion rule: studies that decode speech or text from a non-acoustic speech signal (articulatory imaging, EMA/PMA, EMG, lip or face video, neural recordings) with one model shared across speakers and conditioned on a per-speaker or per-utterance embedding (x-vector, i-vector, d-vector/GE2E, speaker-encoder output, learned subject embedding); acoustic-only systems, audio-visual enhancement or separation with noisy audio at test, embeddings used only as an output metric, and reviews excluded; versions counted once. Slot-filled 1,526 unique studies; pattern match 42 unique studies. Full-text pattern counts: reference-audio embedding 20, unseen-speaker test 16, i-vector 12, x-vector 9, signal-derived embedding 8, learned subject embedding 2. Usual design: reference-audio speaker embedding, 20 (pattern match). State of the art: [[5]](#ref-5) [later]. Read in full: [[4]](#ref-4), [[2]](#ref-2), [[5]](#ref-5) [later], target. Known-item recall 1.0 (3 of 3 seeds).
- M06 speaker-recognition-from-articulation (new topic table). Inclusion rule: studies that identify or verify the speaker from a non-acoustic speech signal (lip or face motion during speech, ultrasound, EMA, EMG, non-audible murmur or throat microphones, EEG during speech tasks); static face recognition, acoustic-only speaker recognition and identification used only as an auxiliary loss excluded; audio-visual fusion counts when the non-acoustic stream is scored alone; versions counted once. Slot-filled 7,345 unique studies; pattern match 58 unique studies. Full-text pattern counts: EER verification 34, closed-set identification 21, cross-session test 15, unseen-speaker test 6 (target included). Usual design: EER verification, 34 (pattern match). State of the art: [[6]](#ref-6). Read in full: [[7]](#ref-7), [[8]](#ref-8), [[3]](#ref-3), [[6]](#ref-6), target. Known-item recall 0.75 (3 of 4 seeds; [[3]](#ref-3) is outside the ledger pattern and was read as a deciding prior).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Shandiz, A. H., Tóth, L., Gosztolya, G., Markó, A., Csapó, T. G. “Neural Speaker Embeddings for Ultrasound-based Silent Speech Interfaces.” *Proc. Interspeech 2021*, 2021, 1932–1936. doi:[10.21437/Interspeech.2021-1466](https://doi.org/10.21437/Interspeech.2021-1466). arXiv:[2106.04552](https://arxiv.org/abs/2106.04552). Target. Read as arXiv v2; venue and pages confirmed with Crossref. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/neural-speaker-embeddings-for-ultrasound-based-silent-speech-interfaces) [wiki: arxiv-2106.04552](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2106.04552/article.md) [wiki: doi-10.21437-interspeech.2021-1466](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.21437-interspeech.2021-1466/article.md) [wiki: isca-shandiz21-usspeaker](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-shandiz21-usspeaker/article.md) [wiki: isca-shandiz21_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-shandiz21_interspeech/article.md)
2. <a id="ref-2"></a>Kandala, P. A., Thanda, A., Margam, D. K., Aralikatti, R. C., Sharma, T., Roy, S., et al. “Speaker Adaptation for Lip-Reading Using Visual Identity Vectors.” *Proc. Interspeech 2019*, 2019, 2758–2762. doi:[10.21437/Interspeech.2019-3237](https://doi.org/10.21437/Interspeech.2019-3237). [wiki: isca-kandala19_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-kandala19_interspeech/article.md) [wiki: isca-kandala19-vivectors](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-kandala19-vivectors/article.md)
3. <a id="ref-3"></a>Diener, L., Amiriparian, S., Botelho, C., Scheck, K., Küster, D., Trancoso, I., et al. “Towards Silent Paralinguistics: Deriving Speaking Mode and Speaker ID from Electromyographic Signals.” *Proc. Interspeech 2020*, 2020, 3117–3121. doi:[10.21437/Interspeech.2020-2848](https://doi.org/10.21437/Interspeech.2020-2848). [wiki: isca-diener20_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-diener20_interspeech/article.md) [wiki: isca-diener20-emgmode](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-diener20-emgmode/article.md)
4. <a id="ref-4"></a>Ribeiro, M. S., Sanger, J., Zhang, J., Eshky, A., Wrench, A., Richmond, K., et al. “TaL: A Synchronised Multi-Speaker Corpus of Ultrasound Tongue Imaging, Audio, and Lip Videos.” *Proc. IEEE Spoken Language Technology Workshop (SLT)*, 2021, 1109–1116. doi:[10.1109/SLT48900.2021.9383619](https://doi.org/10.1109/SLT48900.2021.9383619). arXiv:[2011.09804](https://arxiv.org/abs/2011.09804). [wiki: arxiv-2011.09804](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2011.09804/article.md) [wiki: doi-10.1109-slt48900.2021.9383619](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-slt48900.2021.9383619/article.md)
5. <a id="ref-5"></a>Choi, J., Kim, J., Li, J., Chung, J. S., Liu, S. “V2SFlow: Video-to-Speech Generation with Speech Decomposition and Rectified Flow.” *Proc. IEEE ICASSP 2025*, 2025. doi:[10.1109/ICASSP49660.2025.10889780](https://doi.org/10.1109/ICASSP49660.2025.10889780). arXiv:[2411.19486](https://arxiv.org/abs/2411.19486). [later] [wiki: arxiv-2411.19486](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2411.19486/article.md)
6. <a id="ref-6"></a>Wang, J., Wu, T., Wang, S., Yu, M., Fang, Q., Zhang, J., et al. “Three-Dimensional Lip Motion Network for Text-Independent Speaker Recognition.” *Proc. 25th International Conference on Pattern Recognition (ICPR 2020, held 2021)*, 2021, 3380–3387. doi:[10.1109/ICPR48806.2021.9413218](https://doi.org/10.1109/ICPR48806.2021.9413218). arXiv:[2010.06363](https://arxiv.org/abs/2010.06363). [wiki: arxiv-2010.06363](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2010.06363/article.md)
7. <a id="ref-7"></a>Kojima, M., Kawanami, H., Saruwatari, H., Shikano, K., Matsui, T. “Study on nonaudible murmur speaker verification using multiple session data.” *Fourth Joint Meeting of the Acoustical Society of America and the Acoustical Society of Japan*, 2006. <https://naist.repo.nii.ac.jp/record/4474/files/ASAASJ_2006_(7).pdf> [wiki: asa2006-kojima-nam-speaker-verification](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/asa2006-kojima-nam-speaker-verification/article.md)
8. <a id="ref-8"></a>Davis, C., Kim, J., Aubanel, V., Zelic, G., Mahajan, Y. “The stability of mouth movements for multiple talkers over multiple sessions.” *Proc. FAAVSP 2015*, 2015. <https://www.isca-archive.org/avsp_2015/davis15_avsp.html> [wiki: isca-davis15_avsp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-davis15_avsp/article.md)
