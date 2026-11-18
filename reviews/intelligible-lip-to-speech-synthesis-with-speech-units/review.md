# Intelligible Lip-to-Speech Synthesis with Speech Units

Jeongsoo Choi, Minsu Kim, Yong Man Ro. Interspeech 2023 (arXiv preprint May 2023). [DOI](https://doi.org/10.21437/Interspeech.2023-194) · [arXiv:2305.19603](https://arxiv.org/abs/2305.19603)

## Verdict

The paper [[1]](#ref-1) adds 200 HuBERT units as a target beside the mel-spectrogram (M02) and feeds them to the vocoder (M06); both are standard. The units carry the gain, LRS3 ASR WER 72.5% to 50.7% in one run; vocoder and mel augmentation move WER by 0.3 and 0.2 points (Table 3) (inference). The headline 29.8% rests on a pretrained AV-HuBERT encoder, a step of 20.4 points (41% relative) against 21.8 points (30%) for the units, with no unit ablation on that encoder (inference). The [concurrent] ReVISE also predicts HuBERT units from an AV-HuBERT-initialised encoder [[2]](#ref-2); the [later] V2SFlow, same first author, is 1.3 points lower under the same ASR model, and its listeners rate the target 2.46 of 5 for naturalness against 4.40 in the paper's own test of the non-AV-HuBERT variant (Sec. 4.3) [[3]](#ref-3). It also needs a speaker embedding from unstated speech (Sec. 2.2), and nothing is repeated over seeds.

## Against the field, component by component

### M02 Training-only supervision: speech units beside the mel target

**Usual approach:** Of 54 unique studies that synthesize speech from a non-acoustic signal and name self-supervised speech representations (pattern match, Appendix), 53 name units and 36 also name mel targets (co-mention, not confirmed joint targets). The paper's baseline, SVTS [[4]](#ref-4) modified to its framework, regresses mel alone (Table 3).

**State of the art:** In 2023 the paper's 29.8% was the lowest LRS3 WER without text labels among the systems compared here; the [concurrent] ReVISE gives 33.9% from units alone, its scorer at 5.6% on real audio against 2.5% here [[2]](#ref-2), and DiffV2S 39.2% in V2SFlow's table. In 2024 V2SFlow [later], predicting content and pitch tokens and a speaker embedding, reaches 28.5% with the same ASR model, 4% relative lower [[3]](#ref-3) (inference).

The unit gain is one run with a ResNet-18 encoder. AV-HuBERT is itself pretrained to predict audio-visual clusters, so on it the units may add far less (inference). In silent EMG, means over 10 seeds give 26.55% WER with a soft-unit target against 25.14% with mel, seed spread about 1% [[5]](#ref-5) [later]; if LRS3 spread is similar, the gain is far beyond it (inference). Verdict: standard; ReVISE [concurrent] shares the unit target but not the mel target, and the gain is one run on one dataset.

### M06 Processing: unit-conditioned vocoder

**Usual approach:** Of 165 unique video-to-speech studies (pattern match, Appendix), 49 name a neural vocoder, 41 a parametric vocoder and 16 Griffin-Lim. The paper adds units and the speaker embedding to a neural vocoder trained on blurred, noised mel (Sec. 3.2.3); ReVISE decodes units alone with a unit HiFi-GAN [[2]](#ref-2).

**State of the art:** In 2024 V2SFlow [later] replaces mel regression with a rectified-flow decoder: UTMOS 3.624 against 2.657 for the target, 36% higher, at a WER 1.3 points lower [[3]](#ref-3) (inference). The [concurrent] LipVoicer reaches 21.4% LRS3 WER with lip-reader text at inference, under a scorer at 1.0% on real audio, and 86.2% without it [[6]](#ref-6).

The vocoder takes WER from 50.7% to 50.4% and STOI from 0.542 to 0.552; augmentation then gives 50.2% but STOI 0.543 (Table 3), each under 1% relative WER in single runs (inference), with drops on the other metrics the authors concede (Sec. 4.2). Verdict: standard; naturalness has since moved to generative decoders.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | None; voiced TED and BBC speech | Recorded speech corpora (slot-filled 4,015) | – | standard |
| M02 Training-only supervision | 200 HuBERT units predicted beside mel | Units named, mel co-named (36) (pattern match 54) | V2SFlow: LRS3 WER 28.5% vs 29.8% [[3]](#ref-3) | standard |
| M03 Training and adaptation | Per-dataset training | Per-corpus training (slot-filled 1,608) | – | standard |
| M04 Use-time action | Voiced speech, video used alone | Voiced articulation (slot-filled 6,538) | – | standard |
| M05 Sensors | 88x88 grayscale lip crop | Mouth or face crop from video (slot-filled 8,898) | – | standard |
| M06 Processing and decoding | Vocoder fed mel, units, speaker embedding | Neural vocoder (49) (pattern match 165) | UTMOS 3.624 vs 2.657 (V2SFlow) [[3]](#ref-3) | standard |
| M07 Lexicon and LM | No LM; speaker embedding from unstated speech | No language model (slot-filled 120) | – | not reported |
| M08 Output | Waveform in the speaker's voice | Synthesized audio (slot-filled 3,760) | – | standard |
| M09 Confirmation | None | None (slot-filled 82) | – | not applicable |
| M10 Correction | None | None (slot-filled 82) | – | not applicable |
| M11 Reference construction | LRS3 unseen-speaker split; LRS2 test | Within-corpus splits (slot-filled 239) | – | standard |
| M12 Evaluation | STOI, ESTOI, PESQ, ASR WER; 20-clip MOS | Objective scores plus listeners (slot-filled 8,381) | – | standard |
| M13 Device and cost | Offline | Laboratory recording (slot-filled 6,721) | – | not reported |

## Where the claims outrun the evidence

- "Exceeds text-supervised Multi-Task" (Sec. 4.1): 50.2% against 65.8% on LRS3 and 44.8% against 57.8% on LRS2 (Table 1, Table 2), 24% and 22% relative (inference), each a single run. Retrained and rescored by LipVoicer, the [concurrent] comparator [[7]](#ref-7) gives 57.4% on LRS3 [[6]](#ref-6): its figure moves 8.4 points with who trains and scores it (inference).
- The modified baseline scores 72.5% against 78.0% for published SVTS (Table 1, Table 3), 5.5 points before any unit (inference).
- MOS 4.40 for naturalness against 4.98 for real speech (Table 4) rests on 15 raters, 20 clips, an undefined ± and prior-system samples from their authors (Sec. 4.3). V2SFlow's listeners gave the target 2.46 against 4.42 for real speech [[3]](#ref-3), 56% against 88% of ground truth (inference); V2SFlow does not name the variant it rated, so it does not confirm the paper's score.
- V2SFlow groups the target with audio-embedding systems; its video-derived embedding keeps WER at 28.5% but speaker similarity falls from 0.851 to 0.664 [[3]](#ref-3). If the target behaves like V2SFlow, its WER would survive a video-derived embedding and its speaker similarity would not (inference).

## What the field needs next

- M02: units against mel-only targets with the AV-HuBERT encoder, over several seeds, on LRS2 and LRS3.
- M12: one public scorer and fixed released clips for every system, with MOS intervals.
- M07: audio- and video-derived speaker embeddings side by side, naming the speech segment used.

## Questions for the authors

- Which speech segment gives the speaker embedding at test, and is it ever the test utterance?
- Was the AV-HuBERT LARGE checkpoint pretrained only, or also fine-tuned for lip reading with text?
- How many training runs underlie Tables 1-3, and which data selected the checkpoints?
- In Table 4, is ± a standard deviation or an interval, and did all raters hear all clips?
- Are LRS3 test speakers in AV-HuBERT pretraining, and do LRS2 test speakers appear in training?

## Appendix: literature search

- M02 ssl-speech-unit-target (published topic table, appended). Inclusion rule: studies that synthesize speech from a non-acoustic speech signal and train the encoder to predict self-supervised speech representations (HuBERT units, soft units, ContentVec, wav2vec features) from paired or aligned audio, instead of or besides spectral targets; recognition-only studies, self-generated targets and acoustic-input conversion excluded; versions counted once. Slot-filled 31 unique studies; pattern match 54 unique studies. Usual design: supervision_kind=paired_audio, 11 of the 22 topic studies with that M03 field filled (slot-filled). Design counts (pattern match, full text): self-supervised units 53, mel targets 36, pitch removed or perturbed 4. Read in full: [[5]](#ref-5) [later], [[3]](#ref-3) [later], [[2]](#ref-2) [concurrent], target. Known-item recall 1.0.
- M06 video-to-speech-synthesis (published topic table, appended). Inclusion rule: studies that synthesize a speech waveform from video of the talking face or lips and state the acoustic representation and how it becomes a waveform; audio-visual enhancement or separation with noisy audio at test, talking-head generation, text-only lip reading and video-to-text-to-TTS pipelines excluded; versions counted once. Slot-filled 7,345 unique studies; pattern match 165 unique studies (187 folders). Usual design: neural vocoder, 49 (pattern match, full text). Design counts: neural vocoder 49, parametric vocoder 41, Griffin-Lim 16, auditory spectrogram 3. Read in full: [[3]](#ref-3) [later], [[6]](#ref-6) [concurrent], target; earlier GRID entries of the table carried over. Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Choi, J., Kim, M., Ro, Y. M. “Intelligible Lip-to-Speech Synthesis with Speech Units.” *Interspeech 2023*, 2023, 4349-4353. doi:[10.21437/Interspeech.2023-194](https://doi.org/10.21437/Interspeech.2023-194). arXiv:[2305.19603](https://arxiv.org/abs/2305.19603). Target. Read as arXiv v1 (31 May 2023) and the Interspeech proceedings version. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/intelligible-lip-to-speech-synthesis-with-speech-units) [wiki: arxiv-2305.19603](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2305.19603/article.md) [wiki: isca-choi23-liptospeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-choi23-liptospeech/article.md) [wiki: isca-choi23_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-choi23_interspeech/article.md)
2. <a id="ref-2"></a>Hsu, W., Remez, T., Shi, B., Donley, J., Adi, Y. “ReVISE: Self-Supervised Speech Resynthesis with Visual Input for Universal and Generalized Speech Enhancement.” *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2023. arXiv:[2212.11377](https://arxiv.org/abs/2212.11377). [concurrent] [wiki: arxiv-2212.11377](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2212.11377/article.md)
3. <a id="ref-3"></a>Choi, J., Kim, J., Li, J., Chung, J. S., Liu, S. “V2SFlow: Video-to-Speech Generation with Speech Decomposition and Rectified Flow.” *arXiv preprint*, 2024. arXiv:[2411.19486](https://arxiv.org/abs/2411.19486). Read as arXiv v2 (30 May 2025). [later] [wiki: arxiv-2411.19486](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2411.19486/article.md)
4. <a id="ref-4"></a>Mira, R., Haliassos, A., Petridis, S., Schuller, B. W., Pantic, M. “SVTS: Scalable Video-to-Speech Synthesis.” *Interspeech 2022*, 2022. arXiv:[2205.02058](https://arxiv.org/abs/2205.02058). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/svts-scalable-video-to-speech-synthesis) [wiki: arxiv-2205.02058](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2205.02058/article.md)
5. <a id="ref-5"></a>Lee, J., Hwang, I., Lee, J., Kim, E., Han, D., Lee, K. “Enhancing EMG-to-Speech via Silent-Voiced Representation Alignment.” *Proc. Interspeech 2026*, 2026. doi:[10.21437/Interspeech.2026-2931](https://doi.org/10.21437/Interspeech.2026-2931). [later] [wiki: isca-lee26v_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-lee26v_interspeech/article.md)
6. <a id="ref-6"></a>Yemini, Y., Shamsian, A., Bracha, L., Gannot, S., Fetaya, E. “LipVoicer: Generating Speech from Silent Videos Guided by Lip Reading.” *International Conference on Learning Representations (ICLR)*, 2024. arXiv:[2306.03258](https://arxiv.org/abs/2306.03258). [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lipvoicer-generating-speech-from-silent-videos-guided-by-lip-reading) [wiki: arxiv-2306.03258](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2306.03258/article.md)
7. <a id="ref-7"></a>Kim, M., Hong, J., Ro, Y. M. “Lip-to-Speech Synthesis in the Wild with Multi-task Learning.” *2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2023. arXiv:[2302.08841](https://arxiv.org/abs/2302.08841). [concurrent] [wiki: arxiv-2302.08841](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2302.08841/article.md)
