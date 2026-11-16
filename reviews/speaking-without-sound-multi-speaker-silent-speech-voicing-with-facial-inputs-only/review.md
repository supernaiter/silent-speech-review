# Speaking Without Sound: Multi-speaker Silent Speech Voicing with Facial Inputs Only

Lee J, Oh Y, Lee K. ICASSP 2025. [arXiv:2602.01879](https://arxiv.org/abs/2602.01879)

## Verdict

The paper [[1]](#ref-1) changes two components: the voice comes from a face image instead of reference audio (M08), and the EMG encoder's ContentVec target from pitch-flattened speech (M02). M08 is standard: face-image voice control dates to 2020 in text-to-speech (cited, §II-B) and 2023 in lip-to-speech [[2]](#ref-2), [[3]](#ref-3); only the transfer to EMG is new. M02 is standard: flattening lowers silent WER from 40.12% to 38.91% but raises voiced CER from 9.96% to 13.28% (Table I), with no repeated training runs on one EMG speaker. The evaluation (M12) is behind: only the paper's own two variants are compared, while earlier work on the same split and ASR reports a published model, at 30.0% WER in the recorded speaker's voice [[4]](#ref-4). The cost of face-chosen voices is never separated from vocoder and content-estimator error. Audio-free multi-speaker voicing holds, and the face predicts global pitch beyond gender (Table III); timbre beyond gender and effective pitch disentanglement remain unsupported.

## Against the field, component by component

### M08 Output: voice set from a face image

**Usual approach:** Of 93 unique studies that synthesize speech from non-acoustic signals with a controllable voice (pattern match, Appendix), 48 condition on a speaker label, 23 on reference audio and 23 on face-image cues. In EMG, the [concurrent] multi-voice system uses target audio [[5]](#ref-5).

**State of the art:** A 2023 video-to-speech model, speaker embedding from video alone, reached 3.91 MOS for voice matching on unseen LRS3 speakers and speaker similarity of 0.625 against 0.770 with the audio embedding [[3]](#ref-3); neither is on the target's scale.

The deciding prior [[2]](#ref-2) prices the choice: EER of 36.72% from the face against 26.57% from reference audio. The target gives no audio upper bound; its silent Flatten similarity of 0.5657 against 0.5521 for a random same-gender speaker (Table II) is 2.5% higher (inference). The "first" claim (§I) holds only for EMG: the paper's references include the 2020 text-to-speech work but neither lip-to-speech precedent. Verdict: standard.

### M02 Training-only supervision: pitch-flattened content target

**Usual approach:** On the Gaddy benchmark the encoder learns spectral targets from the DTW-aligned voiced recording [[6]](#ref-6). Of 54 unique synthesis studies mentioning self-supervised speech representations (pattern match, Appendix), 36 also use mel targets and 4 remove or perturb pitch.

**State of the art:** The best controlled comparison of target types, a [later] 2026 study with 10 seeds, gives 25.14% WER with mel and 26.55% with unit targets [[7]](#ref-7).

Silent WER improves 3.0% relative, voiced CER worsens 33% (inference), and voiced WER also rises (16.98% to 17.48%). Seed variation on the 98-utterance split is about 1% WER [[7]](#ref-7), the size of the 1.21-point gain (inference), and no repeated training runs are reported (§IV-A3). The authors concede little pitch variation in one-speaker EMG (§V). Verdict: standard; the gain is too small to call.

### M12 Evaluation: no external baseline

**Usual approach:** Of 16 unique studies on Gaddy silent-EMG voicing (pattern match, Appendix), 9 score with Whisper and 7 with DeepSpeech, and earlier ones report a published model on the same split: 42.2% against 68.0% WER [[6]](#ref-6).

**State of the art:** With the same Whisper medium.en and split, Diff-ETS (2024) reports 30.0% WER for the Gaddy and Klein encoder, in the recorded speaker's voice [[4]](#ref-4); the target's 38.91%, in face-chosen voices, is 30% worse relative (inference). A [later] 2026 model reaches 11.89% on the silent test set [[8]](#ref-8).

Yardstick: best comparable work. The verdict rests on the missing external baseline [[6]](#ref-6), [[4]](#ref-4), not on the gap, which mixes voice change, an in-the-wild vocoder (conceded, §V) and an unreported n_test. Verdict: behind.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Voiced and silent reading, one speaker | Reading tasks (slot-filled 4,015) | – | standard |
| M02 Training-only supervision | ContentVec of pitch-flattened speech | Mel targets (36) (pattern match 54) | 25.14% WER, mel [[7]](#ref-7) | standard |
| M03 Training and adaptation | Per-speaker EMG encoder | Per-speaker training (slot-filled 1,608) | – | standard |
| M04 Use-time action | Silent articulation, DTW targets | Silent with voiced targets (slot-filled 6,538) | – | standard |
| M05 Sensors | Surface EMG plus face image | Surface EMG (slot-filled 8,898) | – | standard |
| M06 Processing and decoding | EMG to ContentVec, decoder | Encoder plus vocoder (slot-filled 8,925) | – | standard |
| M07 Lexicon and LM | No language model | No language model (slot-filled 120) | – | standard |
| M08 Output | Voice and pitch from a face image | Speaker label (48) (pattern match 93) | 3.91 MOS from video [[3]](#ref-3) | standard |
| M09 Confirmation | None | None (slot-filled 82) | – | not applicable |
| M10 Correction | None | None (slot-filled 82) | – | not applicable |
| M11 Reference construction | Gaddy split | Within-corpus splits (slot-filled 239) | – | standard |
| M12 Evaluation | Base vs Flatten, Whisper | Whisper WER (9) (pattern match 16) | 11.89% WER [[8]](#ref-8) | behind |
| M13 Device and cost | Laboratory, offline | Laboratory (slot-filled 6,721) | – | not applicable |

## Where the claims outrun the evidence

- "Facial cues beyond gender" (§IV-C2) holds for pitch, not timbre: silent Flatten Global F0 errors (24.80, 30.83) are 15% and 18% below a random same-gender voice (29.18 Hz, 37.50 Hz), silent Base errors (28.91, 36.45) only 1% and 3% (inference, Table III); timbre rests on a 0.0136 similarity margin (inference), and the subjective test has no random-face control (§IV-B2).
- "Effectiveness of the proposed pitch-disentanglement" (Abstract, §IV-C1): the voiced CER loss of 3.32 points exceeds every silent gain, and no probe shows pitch removed from the content embedding.
- The test set is "40 times" n_test (§IV-A3): trials resample faces, not EMG utterances or models, and the paired t-tests (§IV-C) give no pairing unit; counting every output inflates the sample (inference).
- Local F0 deviation, the new pitch metric, uses only the EMG speaker's own face and scores silent output against the voiced repetition stretched by nearest interpolation (§IV-B3), so its silent gain (18.74 to 17.93, 4% relative, inference) rests on prosody the silent utterance never had.

## What the field needs next

- M08: an audio-reference upper bound and a same-voice control from one EMG content estimate [[2]](#ref-2).
- M02: several training seeds per variant before attributing 1-point changes [[7]](#ref-7).
- M12: the shared Whisper medium.en protocol against a published model [[4]](#ref-4).

## Questions for the authors

- What is n_test; is it the 98-utterance split?
- Were target speakers disjoint from LRS3 training speakers?
- How many training runs and seeds, and which checkpoint?
- What WER results in the recorded speaker's own voice?

## Appendix: literature search

- M08 biosignal-to-speech-voice-control. Inclusion rule: studies that synthesize speech audio from a non-acoustic speech signal (surface EMG, mouth or face video, ultrasound, articulography, neural recordings) and set the output voice through a speaker representation, whether from reference audio, a speaker label or a face image; single-voice systems, text-to-speech after text decoding and acoustic-input conversion excluded; versions counted once. Slot-filled 3,268 unique studies; pattern match 93 unique studies. Design counts (pattern match, full text): speaker label 48, reference audio 23, face image 23. Read in full: [[2]](#ref-2), [[3]](#ref-3), [[5]](#ref-5), target [[1]](#ref-1). Known-item recall 1.0.
- M02 ssl-speech-unit-target. Inclusion rule: studies that synthesize speech from a non-acoustic speech signal and train the encoder to predict self-supervised speech representations (HuBERT units, soft units, ContentVec, wav2vec) derived from paired or aligned audio; recognition-only studies, self-generated targets and acoustic-input conversion excluded; versions counted once. Slot-filled 31 unique studies; pattern match 54 unique studies. Usual design: supervision_kind=paired_audio, 11 (slot-filled, M03 field). Design counts (pattern match, full text): self-supervised units 53, mel targets 36, pitch removed or perturbed 4. Read in full: [[7]](#ref-7), target. Known-item recall 1.0.
- M12 silent-emg-voicing-benchmark. Inclusion rule: studies that synthesize audible speech from silently articulated surface EMG on the Gaddy open-vocabulary corpus and score it by ASR or listener transcription; recognition-only studies, other corpora and voiced-only results excluded; versions counted once. Slot-filled 6,960 unique studies; pattern match 16 unique studies. Design counts (pattern match, full text): Whisper 9, DeepSpeech 7, listener transcription 3. Read in full: [[6]](#ref-6), [[4]](#ref-4), [[8]](#ref-8), target. Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Lee, J., Oh, Y., Lee, K. “Speaking Without Sound: Multi-speaker Silent Speech Voicing with Facial Inputs Only.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2025. arXiv:[2602.01879](https://arxiv.org/abs/2602.01879). Target. arXiv v1 (2026-02-02) states the paper was presented at ICASSP 2025. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/speaking-without-sound-multi-speaker-silent-speech-voicing-with-facial-inputs-only) [wiki: arxiv-2602.01879](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.01879/article.md)
2. <a id="ref-2"></a>Sheng, Z., Ai, Y., Ling, Z. “Zero-Shot Personalized Lip-to-Speech Synthesis with Face Image Based Voice Control.” *arXiv preprint*, 2023. arXiv:[2305.14359](https://arxiv.org/abs/2305.14359). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/zero-shot-personalized-lip-to-speech-synthesis-with-face-image-based-voice-control) [wiki: arxiv-2305.14359](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2305.14359/article.md)
3. <a id="ref-3"></a>Choi, J., Hong, J., Ro, Y. M. “DiffV2S: Diffusion-based Video-to-Speech Synthesis with Vision-guided Speaker Embedding.” *arXiv preprint*, 2023. arXiv:[2308.07787](https://arxiv.org/abs/2308.07787). [wiki: arxiv-2308.07787-diffv2s](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2308.07787-diffv2s/article.md) [wiki: cvf23-choi_diffv2s](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf23-choi_diffv2s/article.md)
4. <a id="ref-4"></a>Ren, Z., Scheck, K., Hou, Q., van Gogh, S., Wand, M., Schultz, T. “Diff-ETS: Learning a Diffusion Probabilistic Model for Electromyography-to-Speech Conversion.” *arXiv preprint*, 2024. arXiv:[2405.08021](https://arxiv.org/abs/2405.08021). [wiki: arxiv-2405.08021](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2405.08021/article.md)
5. <a id="ref-5"></a>Scheck, K., Dombeck, T., Ren, Z., Wu, P., Wand, M., Schultz, T. “DiffMV-ETS: Diffusion-based Multi-Voice Electromyography-to-Speech Conversion using Speaker-Independent Speech Training Targets.” *Proc. Interspeech 2025*, 2025. doi:[10.21437/Interspeech.2025-1914](https://doi.org/10.21437/Interspeech.2025-1914). [concurrent] [wiki: isca-scheck25_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-scheck25_interspeech/article.md)
6. <a id="ref-6"></a>Gaddy, D., Klein, D. “An Improved Model for Voicing Silent Speech.” *Proc. ACL-IJCNLP 2021 (Short Papers)*, 2021. doi:[10.18653/v1/2021.acl-short.23](https://doi.org/10.18653/v1/2021.acl-short.23). arXiv:[2106.01933](https://arxiv.org/abs/2106.01933). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/an-improved-model-for-voicing-silent-speech) [wiki: arxiv-2106.01933](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2106.01933/article.md) [wiki: doi-10.18653-v1-2021.acl-short.23](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.18653-v1-2021.acl-short.23/article.md)
7. <a id="ref-7"></a>Lee, J., Hwang, I., Lee, J., Kim, E., Han, D., Lee, K. “Enhancing EMG-to-Speech via Silent-Voiced Representation Alignment.” *Proc. Interspeech 2026*, 2026. doi:[10.21437/Interspeech.2026-2931](https://doi.org/10.21437/Interspeech.2026-2931). [later] [wiki: isca-lee26v_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-lee26v_interspeech/article.md)
8. <a id="ref-8"></a>Lee, J., Lee, J., Lee, K. “GETS: Guiding EMG-to-Speech Synthesis via Silent Speech Recognition.” *Proc. Interspeech 2026*, 2026. doi:[10.21437/Interspeech.2026-1938](https://doi.org/10.21437/Interspeech.2026-1938). [later] [wiki: isca-lee26r_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-lee26r_interspeech/article.md)
