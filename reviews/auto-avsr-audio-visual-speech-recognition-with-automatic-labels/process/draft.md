# Auto-AVSR: Audio-Visual Speech Recognition with Automatic Labels

Ma, P., Haliassos, A., Fernandez-Lopez, A., Chen, H., Petridis, S., Pantic, M. · ICASSP 2023 · 2023 · [DOI:10.1109/ICASSP49357.2023.10096889](https://doi.org/10.1109/ICASSP49357.2023.10096889) · [arXiv:2303.14307](https://arxiv.org/abs/2303.14307)

## Verdict

Auto-AVSR [[1]](#ref-1) changes one component, the training labels (M02), adding 2,630 h of AVSpeech and VoxCeleb2 transcribed by a public ASR model. The design is standard: Afouras et al. trained lip readers with CTC on ASR-generated transcripts of unlabelled video [[2]](#ref-2), and the same group had already added AVSpeech with automatically generated transcriptions [[3]](#ref-3); what the paper adds is scale (641 h to 2,630 h) and a comparison of four labellers. The scale result holds: LRS3 visual-only WER falls from 33.0% to 19.1% as automatic-label hours grow (Table 2), though the [later] USR 2.0 reaches 17.6% on the same two corpora with self-generated labels [[4]](#ref-4). Evaluation (M12) drops the ten-run means of the group's prior work [[3]](#ref-3), so the labeller ranking (Table 1) and the unanchored 30% headline carry less weight than claimed.

## Against the field, component by component

### M02 Training-only supervision: ASR transcripts of unlabelled video

**Usual approach:** Of 428 visual or audio-visual speech recognition studies with a recorded supervision kind (slot-filled, Appendix), 45 record text transcripts as the supervision; in the full texts of 1,049 such studies (pattern match, Appendix), 164 name self-supervised pretraining, 148 pseudo or automatic labels and 106 teacher distillation, only 18 of them dated up to 2022-09. Auto-AVSR adds automatically transcribed video instead of pretraining on it.

**State of the art:** USR 2.0 (2026) [[4]](#ref-4) reaches 17.6% LRS3 VSR, 0.9% ASR and 0.8% AVSR WER with 656 labelled and 2,649 unlabelled hours, generating its own pseudo-labels by self-training (Abstract; Table 7). That is 1.5 points (8% relative) below Auto-AVSR's 19.1% at nearly the same unlabelled volume (inference), with a larger (Huge) model, so the label source alone does not explain the gap.

Afouras et al. trained with "CTC loss on the ASR-generated transcripts" of VoxCeleb2 plus distillation, reaching 59.8% on LRS3 [[2]](#ref-2). Ma et al. added 641 h of AVSpeech with automatic English transcriptions and reached 31.5% best (32.1 ± 0.3 over ten runs) on LRS3 at 1,459 h [[3]](#ref-3). Auto-AVSR quadruples the automatic-label hours and cuts that WER by 12.4 points, 39% relative (inference). Using labels "rather than using the pre-trained ASR model for distillation" (§1) separates it from Afouras et al., not from its own cited CM-aux, which already did this. The contrast with captions filtered by a production ASR (§1) holds [[5]](#ref-5). The [concurrent] SynthVSR reuses the same 2,630 h [[6]](#ref-6). Verdict: standard.

### M12 Evaluation: LRS3 WER without repetition

**Usual approach:** Of 258 LRS3 visual-only studies (pattern match, Appendix), 141 record a supervision kind and 18 of them text labels (slot-filled). Auto-AVSR reports every row from a single run with no seeds (§3.3).

**State of the art:** LP Conformer (2023, [concurrent]) reports 12.8% VSR and 0.9% AVSR with 100k h of mined YouTube video [[5]](#ref-5); with public data, USR 2.0 (2026, [later]) reports 17.6% and 0.8% [[4]](#ref-4). Auto-AVSR's 0.9% AVSR equals the best concurrent figure and trails today's public-data best by 0.1 point (inference); its 19.1% VSR trails both.

The group's prior paper gave ten-run means with ± 0.3 on LRS3 [[3]](#ref-3). The VSR spread across the four labellers, 19.0% to 19.8% (Table 1), is under three such deviations (inference), and Whisper labels give the lowest VSR WER although Conformer-Transducer is chosen (§4.1). Verdict: standard, with repetition lost against the lineage.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Overt broadcast/YouTube speech video | Recorded speech video (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | 2,630 h ASR-transcribed AVSpeech/VoxCeleb2 | Human transcripts only (slot-filled 45) | [[4]](#ref-4) (2026): LRS3 VSR 17.6%, self-training | standard |
| M03 Training and adaptation | LRW init; single runs, no seeds | Training records (slot-filled 1,526) | – | standard |
| M04 Use-time action | Overt speech; A, V or AV at test | Silent or overt (slot-filled 5,595) | – | standard |
| M05 Sensors | Mouth ROI video and raw audio | Camera video (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | ResNet-18+Conformer, MLP fusion, CTC/attention | Encoder-decoder (slot-filled 7,345) | – | standard |
| M07 Lexicon and LM | LM for VSR only | LM or lexicon (slot-filled 119) | – | standard |
| M08 Output | English text, 5,000 subwords | Text (slot-filled 3,268) | – | standard |
| M09 Confirmation | Offline | Offline (slot-filled 82) | – | not applicable |
| M10 Correction | Offline | Offline (slot-filled 82) | – | not applicable |
| M11 Reference construction | Original LRS2/LRS3 splits | Corpus transcripts (slot-filled 234) | – | standard |
| M12 Evaluation | LRS2/LRS3 WER, single runs, noise test | LRS3 VSR WER, text labels (slot-filled 18) | [[5]](#ref-5) (2023): VSR 12.8%, AV 0.9%; [[4]](#ref-4) (2026): AV 0.8% | standard |
| M13 Device and cost | Public data, code and models | Device and cost (slot-filled 6,075) | – | standard |

## Where the claims outrun the evidence

- The 30% relative improvement (Abstract) names no baseline. Against AV-HuBERT's 1.4% in Table 4 the reduction from 0.9% is 36% (inference); against ViT3D-CM's 1.6% it is 44% (inference).
- "Outperforms methods … with 26 times more training data" (Abstract) matches ViT3D-CM at 90,000 h against 3,448 h on AVSR only; on visual-only ViT3D-CM is better (17.0% against 19.1%), which the authors concede (§4.3).
- Table 4 lists CM-aux on LRS3 only at 37.9% without extra data, while Table 3 gives its 1,459 h automatic-transcription row on LRS2 (25.5%); the 31.5% LRS3 row [[3]](#ref-3) is missing.
- The LRS3 audio-only 1.0% row is stated as 1,921 h in §4.3 and 1,902 h in Table 4.
- Babble noise appears in training and test; the authors attribute the low babble WER mainly to this overlap (§4.4). Pink and white noise, not named for training, give 16.2% and 24.2% AVSR WER at −7.5 dB (Table 5).
- The paper gives no speaker or video-identity check between the added YouTube corpora and the LRS3 test set (§3.1).

## What the field needs next

- M02: external-ASR labels against self-training labels [[4]](#ref-4) and a human-transcribed subset, at equal hours and model size, reporting label WER beside downstream WER.
- M12: repeated runs with mean and spread, as in [[3]](#ref-3), before ranking labellers.
- M11: a speaker- and video-ID disjointness audit between VoxCeleb2, AVSpeech and the LRS2/LRS3 test sets.
- M04: a silent-articulation test set; all training and test video here is overt speech.

## Questions for the authors

- Which baseline gives the 30% relative improvement in the Abstract?
- How many runs and which seeds underlie each row, and what is the run-to-run spread?
- Which data selected the final checkpoints? The released code defaults both validation and test lists to the LRS3 test file.
- Do any AVSpeech or VoxCeleb2 speakers or videos appear in the LRS3 test set?

## Appendix: literature search

- M02, asr-transcribed-unlabelled-video-training. Inclusion rule: studies whose ledger text names lip reading, VSR, AVSR or audio-visual speech recognition, classified from the full text by the label source for unlabelled video; a study counts under every design its text names (upper bound); versions once. Ledger counts: slot-filled M02 31; population 1,049 unique studies (pattern match). Usual design: M03 supervision kind text labels 45 of 428 (slot-filled); full-text designs: self-supervised pretraining 164, pseudo or automatic labels 148 (18 dated up to 2022-09), teacher distillation 106, human or caption transcripts 9 (pattern match). Read in full: [[2]](#ref-2), [[3]](#ref-3) (prior); [[4]](#ref-4), [[6]](#ref-6) (state of the art). Known-item recall 1.0 (8 seeds).
- M12, lrs3-visual-only-wer (reused published table). Inclusion rule: studies reporting visual-only WER on the LRS3 test set, any training regime; audio-only, audio-visual and quoted rows excluded; versions once. Ledger counts: 258 unique studies (pattern match). Usual design: text labels 18 of 141 (slot-filled). Read in full for this review: [[5]](#ref-5) (state of the art), [[3]](#ref-3) (prior). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [auto-avsr-audio-visual-speech-recognition-with-automatic-labels.bib](auto-avsr-audio-visual-speech-recognition-with-automatic-labels.bib).

1. <a id="ref-1"></a>Ma, P., Haliassos, A., Fernandez-Lopez, A., Chen, H., Petridis, S., Pantic, M. “Auto-AVSR: Audio-Visual Speech Recognition with Automatic Labels.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2023. doi:[10.1109/ICASSP49357.2023.10096889](https://doi.org/10.1109/ICASSP49357.2023.10096889). arXiv:[2303.14307](https://arxiv.org/abs/2303.14307). Target. Read as arXiv v3. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/auto-avsr-audio-visual-speech-recognition-with-automatic-labels) [wiki: arxiv-2303.14307](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2303.14307/article.md)
2. <a id="ref-2"></a>Afouras, T., Chung, J. S., Zisserman, A. “ASR is all you need: cross-modal distillation for lip reading.” *IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2020. arXiv:[1911.12747](https://arxiv.org/abs/1911.12747). Prior; deciding prior for M02 (CTC on ASR-generated transcripts of unlabelled video). Read as arXiv v2. [wiki: arxiv-1911.12747](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1911.12747/article.md)
3. <a id="ref-3"></a>Ma, P., Petridis, S., Pantic, M. “Visual Speech Recognition for Multiple Languages in the Wild.” *Nature Machine Intelligence*, 2022, 930-939. doi:[10.1038/s42256-022-00550-z](https://doi.org/10.1038/s42256-022-00550-z). arXiv:[2202.13084](https://arxiv.org/abs/2202.13084). Prior; same group; deciding prior for M02 (AVSpeech with automatically generated transcriptions) and M12 (ten-run means). Read as arXiv v2. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/visual-speech-recognition-for-multiple-languages-in-the-wild) [wiki: arxiv-2202.13084](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2202.13084/article.md) [wiki: doi-10.1038-s42256-022-00550-z](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s42256-022-00550-z/article.md)
4. <a id="ref-4"></a>Haliassos, A., Mira, R., Petridis, S. “Pay Attention to CTC: Fast and Robust Pseudo-Labelling for Unified Speech Recognition.” *International Conference on Learning Representations (ICLR)*, 2026. arXiv:[2602.19316](https://arxiv.org/abs/2602.19316). [later]; state of the art for M02 and M12 with public data. Read as arXiv v1. [later] [wiki: arxiv-2602.19316](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.19316/article.md)
5. <a id="ref-5"></a>Chang, O., Liao, H., Serdyuk, D., Shah, A., Siohan, O. “Conformers are All You Need for Visual Speech Recognition.” *arXiv preprint*, 2023. arXiv:[2302.10915](https://arxiv.org/abs/2302.10915). [concurrent]; best LRS3 VSR WER on non-public data (M12). Read as arXiv v2. [concurrent] [wiki: arxiv-2302.10915](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2302.10915/article.md)
6. <a id="ref-6"></a>Liu, X., Lakomkin, E., Vougioukas, K., Ma, P., Chen, H., Xie, R., et al. “SynthVSR: Scaling Up Visual Speech Recognition With Synthetic Supervision.” *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2023. arXiv:[2303.17200](https://arxiv.org/abs/2303.17200). [concurrent]; reuses the target's 2,630 h pseudo-labelled data (M02, M12). [concurrent] [wiki: arxiv-2303.17200](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2303.17200/article.md) [wiki: cvf23-liu_synthvsr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf23-liu_synthvsr/article.md)
