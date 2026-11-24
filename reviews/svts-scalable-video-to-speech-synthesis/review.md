# SVTS: Scalable Video-to-Speech Synthesis

Mira, R., Haliassos, A., Petridis, S., Schuller, B. W., Pantic, M. · arXiv preprint · 2022 · [arXiv:2205.02058](https://arxiv.org/abs/2205.02058)

## Verdict

SVTS [[1]](#ref-1) changes the synthesis path (M06), a conformer mel predictor before a frozen LibriTTS Parallel WaveGAN, and the training scale (M03), up to 1,556 hours of LRS3 plus VoxCeleb2. Both are standard: a neural vocoder on predicted features is the most common design (49 of 165 studies, pattern match, Appendix), the [concurrent] VCVTS uses the same vocoder [[2]](#ref-2), and the [concurrent] LipSound2 had pre-trained on about 2400 hours of VoxCeleb2 [[3]](#ref-3). The GRID-seen and LRW gains hold when the same group re-scores them in a [later] table (2.37% and 12.90% WER) [[4]](#ref-4). The LRS3 claim does not: the paper gives no LRS3 WER, as the authors note, and a [later] test of the authors' own LRS3 files finds 82.4% WER and intelligibility MOS 2.17 [[5]](#ref-5), with 78.0% in a second [later] test [[6]](#ref-6). Crediting the gains to scalability is unsupported: model size, data and an audio speaker embedding change together.

## Against the field, component by component

### M06 Synthesis path: mel predictor and pretrained vocoder

**Usual approach:** a neural vocoder on predicted acoustic features is the most frequent design (49 of 165 studies, pattern match, Appendix). SVTS follows it, replacing the authors' adversarial waveform GAN [[7]](#ref-7) with a conformer trained on L1 and spectral-convergence losses (§2.1).

**State of the art:** on the SVTS LRS3 test files, LipVoicer (2023) reaches 21.4% WER against 82.4% for SVTS in one table [[5]](#ref-5), and V2SFlow-A (2024) 28.5% against 78.0% [[6]](#ref-6); both replace the whole generator, so this is not a vocoder gap.

On small corpora the predictor holds: GRID-seen WER 2.36% against 4.60% for the end-to-end GAN, LRW 13.40% against 37.07% for VCA-GAN (Table 2). Griffin-Lim gives 2.41% against 2.36% WER (Table 3): the vocoder is not the source of the gain. Verdict: standard.

### M03 Training scale: model size and added VoxCeleb2

**Usual approach:** one benchmark corpus; GRID is named in 59 of 165 studies, LRS3 in 35, VoxCeleb2 in 16, 1,000 hours or more in 9 (pattern match, upper bound, Appendix). SVTS adds VoxCeleb2 and grows the model from 27.3 to 87.6 million parameters (Table 1).

**State of the art:** V2SFlow (2024), trained on LRS3-TED alone, reaches 28.5% WER on the SVTS split [[6]](#ref-6), without added video.

The [concurrent] LipSound2 had pre-trained on VoxCeleb2 [[3]](#ref-3). The added data moves STOI from 0.507 to 0.530 (+4.5%), ESTOI from 0.271 to 0.313 (+15.5%) and PESQ from 1.25 to 1.26 (+0.8%) (Table 2) (inference), called "the significant boost on all metrics" (§4.1) from one run. Verdict: standard.

### M07 Use-time speaker embedding from audio

**Usual approach:** an embedding from reference audio is the most frequent use-time speaker input (21 of 165 studies, pattern match, Appendix). SVTS uses a random same-speaker clip for GRID and LRS3, and for LRW the audio of the same video, following earlier LRW practice (§3.1).

**State of the art:** V2SFlow (2024) reaches SECS 0.851 against 0.557 for SVTS, and the same 28.5% WER with an embedding predicted from video [[6]](#ref-6).

On LRW the generator hears the test utterance's own audio, and no run drops the embedding. Verdict: standard.

### M12 Evaluation: no listener test, no LRS3 WER

**Usual approach:** a listener or opinion-score test is the most frequent protocol (83 of 165 studies; ASR WER on output 38; unseen speakers 51; pattern match, Appendix). SVTS reports objective metrics, WER only for GRID and LRW, and its authors' listening (§4.1); the authors themselves warn that objective metrics do not track perception (§3.4).

**State of the art:** LipVoicer (2023) rated the authors' own LRS3 files with 16 annotators per sample: intelligibility 2.17 for SVTS against 3.44 [[5]](#ref-5); V2SFlow (2024) gives 1.49 [[6]](#ref-6).

Earlier listener tests are on GRID (32 listeners [[8]](#ref-8), 20 workers per sample [[9]](#ref-9), 20 listeners [[10]](#ref-10)) or single-speaker data (15 raters in Lip2Wav [[11]](#ref-11)); the multi-speaker LRW baseline reports none [[7]](#ref-7). Verdict: standard for its multi-speaker settings; the listener-test gap is against [later] LRS3 practice.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | GRID, LRW, LRS3 overt speech | Recorded speech video (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Real-audio log-mel targets, no text | Paired-audio targets (slot-filled 31) | – | standard |
| M03 Training and adaptation | LRS3 + VoxCeleb2, 1,556 h | One benchmark corpus (GRID) (pattern match 59) | V2SFlow, LRS3 only, 28.5% WER [[6]](#ref-6) | standard |
| M04 Use-time action | Overt speech, audio muted | Silent or overt (slot-filled 5,595) | – | standard |
| M05 Sensors | 96x96 mouth crop, 20 fps | Camera video (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | Conformer mel, frozen Parallel WaveGAN | Neural vocoder on features (pattern match 49) | LipVoicer 21.4% vs SVTS 82.4% LRS3 WER [[5]](#ref-5) | standard |
| M07 Lexicon and LM | Audio embedding; LRW uses own clip | Reference-audio embedding (pattern match 21) | Video-derived embedding [[6]](#ref-6) | standard |
| M08 Output | Waveform via vocoder | Speech output (slot-filled 3,760) | – | standard |
| M09 Confirmation | None (offline) | Presentation step (slot-filled 82) | – | not applicable |
| M10 Correction | None (offline) | Correction step (slot-filled 82) | – | not applicable |
| M11 Reference construction | Real-audio ASR transcript as reference | Real-audio ASR error reported (pattern match 20) | Real-audio WER per row [[6]](#ref-6) | standard |
| M12 Evaluation | Objective metrics; no listener test | Listener test (pattern match 83) | LipVoicer MOS and WER on SVTS files [[5]](#ref-5) | standard |
| M13 Device and cost | Vocoder speed on one RTX 2080 Ti | Device constraints (slot-filled 6,721) | – | standard |

## Where the claims outrun the evidence

- The claim of the first intelligible LRS3 results (Abstract) rests on author listening; [later] tests find 82.4% [[5]](#ref-5) and 78.0% WER [[6]](#ref-6). V2SFlow scores against ground-truth text, not the §3.4 real-audio transcript; neither names the SVTS checkpoint.
- "This strong performance is a consequence of our SVTS architecture" (§4.1, LRW): the LRW model is larger than the GRID one (Table 1) and hears the clip's own audio (§3.1).
- "State-of-the-art results for GRID" (Abstract) holds for seen speakers only: unseen GRID WER is 17.85% against 16.12% for the end-to-end GAN, as the authors concede (§4.1).
- No seeds or repeated runs are reported (§3.3), yet 2.36% against 2.90% WER is read as "clearly superior" (§4.2), and that ablation row repeats the full model's PESQ, STOI and ESTOI exactly (Table 4).

## What the field needs next

- M12: LRS3 WER with the recognizer's real-audio error, and a listener test.
- M03: a data-scaling curve at fixed model size with at least three seeds.
- M07: LRW with a video-derived embedding.

## Questions for the authors

- For GRID and LRS3, can the reference clip be the evaluated utterance?
- How many runs stand behind each row of Tables 2–4?

## Appendix: literature search

- M06, video-to-speech-synthesis (published table, reused). Inclusion rule: studies that synthesize a speech waveform from talking-face or lip video and report the acoustic representation and how it becomes a waveform; enhancement with noisy audio at test, talking-head generation, text-only lip reading and video-to-text-to-speech pipelines excluded; versions count once. Ledger: 7,345 unique studies slot-filled for M06; 165 unique studies pattern match. Usual design: neural vocoder on predicted acoustic features 49; parametric vocoder 41, Griffin-Lim 16 (pattern match). Read in full: [[6]](#ref-6), [[2]](#ref-2), [[4]](#ref-4). Known-item recall 1.0 on the published seed set; 8 of 15 wiki papers cited by the target are in the population (0.53).
- M06, joint-end-to-end-lip-to-speech-training (published table, reused). Inclusion rule: the same 165 studies, classified by whether the waveform generator is trained with the visual path or is a pretrained or separately trained vocoder (upper bound). Ledger: 165 unique studies pattern match. Pretrained or separately trained vocoder 15 (pattern match). Read in full: [[7]](#ref-7), [[2]](#ref-2), [[3]](#ref-3), [[5]](#ref-5). Known-item recall 1.0.
- M03, training-data-scale-video-to-speech (new). Inclusion rule: the 165-study video-to-speech population, classified from the full text (reference list removed) by the training corpora and scale it names; every named corpus counts, including related-work and evaluation-only mentions (upper bound); audio-only corpora not counted. Ledger: 1,526 unique studies slot-filled for M03; 165 unique studies pattern match. GRID 59, LRS3 35, LRW 18, VoxCeleb2 16, model-size scaling 16, 1,000 hours or more 9 (pattern match). Read in full: [[3]](#ref-3), [[6]](#ref-6). Known-item recall 1.0 (3 seeds).
- M07, reference-speaker-conditioning-at-inference (published table, reused). Inclusion rule: the same 165 studies, classified by the speaker information supplied at use time; training-only or scoring-only embeddings excluded (upper bound). Ledger: 119 unique studies slot-filled for M07; 165 unique studies pattern match. Reference-audio embedding 21 (pattern match). Read in full: [[6]](#ref-6). Known-item recall 1.0.
- M11, asr-retranscribed-evaluation-reference (published table, reused). Inclusion rule: the same population, classified by how the WER text reference is built and whether the recognizer's error on the real test audio is reported (upper bound). Ledger: 234 unique studies slot-filled for M11; 165 unique studies pattern match. Real-audio recognizer error reported 20 (pattern match). Read in full: [[6]](#ref-6). Known-item recall 1.0.
- M12, video-to-speech-output-evaluation (published table, reused). Inclusion rule: the same population, counting the evaluation protocols its full text names (upper bound). Ledger: 6,960 unique studies slot-filled for M12; 165 unique studies pattern match. Listener test 83, unseen speakers 51, ASR WER on output 38 (pattern match). Read in full: [[8]](#ref-8), [[9]](#ref-9), [[10]](#ref-10), [[11]](#ref-11), [[2]](#ref-2), [[5]](#ref-5), [[6]](#ref-6). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Mira, R., Haliassos, A., Petridis, S., Schuller, B. W., Pantic, M. “SVTS: Scalable Video-to-Speech Synthesis.” *arXiv preprint*, 2022. doi:[10.48550/arXiv.2205.02058](https://doi.org/10.48550/arXiv.2205.02058). arXiv:[2205.02058](https://arxiv.org/abs/2205.02058). Target. Read as arXiv v2 (15 Aug 2022). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/svts-scalable-video-to-speech-synthesis) [wiki: arxiv-2205.02058](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2205.02058/article.md)
2. <a id="ref-2"></a>Wang, D., Yang, S., Su, D., Liu, X., Yu, D., Meng, H. “VCVTS: Multi-Speaker Video-to-Speech Synthesis via Cross-Modal Knowledge Transfer from Voice Conversion.” *arXiv preprint*, 2022. arXiv:[2202.09081](https://arxiv.org/abs/2202.09081). Concurrent; same LibriTTS Parallel WaveGAN vocoder; MOS test. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/vcvts-multi-speaker-video-to-speech-synthesis-via-cross-modal-knowledge-transfer-from-voice-conversion) [wiki: arxiv-2202.09081-vcvts](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2202.09081-vcvts/article.md)
3. <a id="ref-3"></a>Qu, L., Weber, C., Wermter, S. “LipSound2: Self-Supervised Pre-Training for Lip-to-Speech Reconstruction and Lip Reading.” *IEEE Transactions on Neural Networks and Learning Systems*, 2022. doi:[10.1109/TNNLS.2022.3191677](https://doi.org/10.1109/TNNLS.2022.3191677). arXiv:[2112.04748](https://arxiv.org/abs/2112.04748). Concurrent; VoxCeleb2 pre-training of a video-to-mel model. [concurrent] [wiki: arxiv-2112.04748](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2112.04748/article.md) [wiki: doi-10.1109-tnnls.2022.3191677](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tnnls.2022.3191677/article.md)
4. <a id="ref-4"></a>Kefalas, T., Panagakis, Y., Pantic, M. “Large-scale unsupervised audio pre-training for video-to-speech synthesis.” *arXiv preprint*, 2023. arXiv:[2306.15464](https://arxiv.org/abs/2306.15464). Later; re-scores SVTS on GRID and LRW. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/large-scale-unsupervised-audio-pre-training-for-video-to-speech-synthesis) [wiki: arxiv-2306.15464-v2apretrain](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2306.15464-v2apretrain/article.md)
5. <a id="ref-5"></a>Yemini, Y., Shamsian, A., Bracha, L., Gannot, S., Fetaya, E. “LipVoicer: Generating Speech from Silent Videos Guided by Lip Reading.” *International Conference on Learning Representations (ICLR)*, 2024. arXiv:[2306.03258](https://arxiv.org/abs/2306.03258). Later; lowest LRS3 WER among read works. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lipvoicer-generating-speech-from-silent-videos-guided-by-lip-reading) [wiki: arxiv-2306.03258](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2306.03258/article.md)
6. <a id="ref-6"></a>Choi, J., Kim, J., Li, J., Chung, J. S., Liu, S. “V2SFlow: Video-to-Speech Generation with Speech Decomposition and Rectified Flow.” *arXiv preprint*, 2024. arXiv:[2411.19486](https://arxiv.org/abs/2411.19486). Later; state of the art on the SVTS LRS3 unseen-speaker split; re-evaluates SVTS. [later] [wiki: arxiv-2411.19486](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2411.19486/article.md)
7. <a id="ref-7"></a>Mira, R., Vougioukas, K., Ma, P., Petridis, S., Schuller, B. W., Pantic, M. “End-to-End Video-To-Speech Synthesis using Generative Adversarial Networks.” *IEEE Transactions on Cybernetics*, 2023, 53(6), 3454-3466. arXiv:[2104.13332](https://arxiv.org/abs/2104.13332). Prior; the authors' own GAN baseline ([24] in the target). [wiki: arxiv-2104.13332](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2104.13332/article.md)
8. <a id="ref-8"></a>Le Cornu, T., Milner, B. “Generating Intelligible Audio Speech From Visual Speech.” *IEEE/ACM Transactions on Audio, Speech, and Language Processing*, 2017, 25(9), 1751-1761. doi:[10.1109/TASLP.2017.2716178](https://doi.org/10.1109/TASLP.2017.2716178). Prior; 32-listener word-accuracy test. [wiki: doi-10.1109-taslp.2017.2716178](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-taslp.2017.2716178/article.md)
9. <a id="ref-9"></a>Akbari, H., Arora, H., Cao, L., Mesgarani, N. “Lip2AudSpec: Speech reconstruction from silent lip movements video.” *arXiv preprint*, 2017. arXiv:[1710.09798](https://arxiv.org/abs/1710.09798). Prior; crowd listener test. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lip2audspec-speech-reconstruction-from-silent-lip-movements-video) [wiki: arxiv-1710.09798](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1710.09798/article.md)
10. <a id="ref-10"></a>Le Cornu, T., Milner, B. “Reconstructing intelligible audio speech from visual speech features.” *Proc. Interspeech 2015*, 2015. doi:[10.21437/Interspeech.2015-319](https://doi.org/10.21437/Interspeech.2015-319). Prior; 20-listener test. [wiki: isca-cornu15_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-cornu15_interspeech/article.md)
11. <a id="ref-11"></a>Prajwal, K. R., Mukhopadhyay, R., Namboodiri, V. P., Jawahar, C. V. “Learning Individual Speaking Styles for Accurate Lip to Speech Synthesis.” *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2020. arXiv:[2005.08209](https://arxiv.org/abs/2005.08209). Prior; listener test on single-speaker open-vocabulary data. [wiki: arxiv-2005.08209](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2005.08209/article.md) [wiki: cvf-prajwal20-lip2wav](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-prajwal20-lip2wav/article.md)
