# VSpeechLM: A Visual Speech Language Model for Visual Text-to-Speech Task

Yuyue Wang, Xin Cheng, Yihan Wu, Xihua Wang, Jinchuan Tian, Ruihua Song. ACM Multimedia Asia (MMAsia '25), 2025. [DOI](https://doi.org/10.1145/3743093.3771012) · [arXiv:2511.22229](https://arxiv.org/abs/2511.22229)

## Verdict

VSpeechLM [[1]](#ref-1) changes one component, synthesis (M06): a per-frame phoneme aligner feeds a pretrained codec language model instead of a duration-based, diffusion or flow decoder. Both halves are standard: lip-set phoneme durations without a duration predictor appear in Hegde et al. [[2]](#ref-2) (§3.2.2), and the authors themselves cite an earlier speech-LLM dubbing system (§2.1). The content gain over the strongest baseline is small, 12.5% against 12.8% WER on Chem (Table 1), while the [concurrent] DiFlowDubber reports 9.65% against 11.72% for the same baseline [[3]](#ref-3). The synchronization claim is the weakest: it rests on a length-weighted spectral distance alone (§4.1), its headline reductions do not follow from Table 1, and on GRID the method ties EmoDubber on that metric. On lip sync the evaluation (M12) is weaker than every other text-and-video study in the Appendix population.

## Against the field, component by component

### M06 Synthesis: lip-timed phonemes into a codec language model

**Usual approach:** of the 7 studies that synthesize speech from lip video plus text (pattern match, unique studies, Appendix), 5 take phoneme timing from the lips or from attention to the video, with diffusion (5), flow-matching (4) or duration-based mel (4) decoders; 2 mention a codec-token language model, this paper and the [concurrent] FunCineForge [[4]](#ref-4). VSpeechLM keeps lip-derived timing and swaps in an autoregressive EnCodec language model initialised from ESPnet (§4.1).

**State of the art:** the [concurrent] DiFlowDubber (2026) [[3]](#ref-3) reports Chem WER 9.65% against 11.72% for EmoDubber in its Table 1 (ground-truth reference, Whisper-V3), and GRID 16.79% against 18.53% (Table 2): a 17.7% relative reduction on Chem, against 2.3% for VSpeechLM over EmoDubber (12.5% vs 12.8%) (inference). Absolute values use different ASR systems.

Each lip frame takes its most similar phoneme, trained by cross-entropy on forced-alignment labels, with no monotonic constraint (§3.3.2, §3.5). Hegde et al. [[2]](#ref-2) (prior) let visual queries attend over phonemes and upsampled the result, so video-text alignment set durations (§3.2.2). DiFlowDubber and the [later] LipAdapter [[5]](#ref-5) add monotonic alignment search; per-frame argmax can reorder or skip phonemes, and the paper does not measure how often. The visual timing helps (Chem WER 12.48% vs 15.02% without video, Table 2), but the decoder carries the system: without pretraining WER is 151% (Table 3). Verdict: standard.

### M12 Evaluation: synchronization without a lip-sync score

**Usual approach:** 6 of the 7 text-and-video studies report SyncNet scores (LSE-C/LSE-D), including both priors, LipVoicer [[6]](#ref-6) and Hegde et al. [[2]](#ref-2), and the [later] Watch Your Speech [[7]](#ref-7); all 7 report ASR WER and a listener test (pattern match, Appendix). VSpeechLM is the exception and measures "duration synchronization" with MCD-DTW-SL alone (§4.1).

**State of the art:** DiFlowDubber (2026) [[3]](#ref-3) reports Chem LSE-C 8.31 and LSE-D 6.73 (Table 1) and separates a ground-truth reference from another utterance of the same speaker. VSpeechLM has neither, and does not state which utterance is the test reference (§3.2).

MCD-DTW-SL rewards matching the recording's duration, not the visible lips. Verdict: standard, since only two of the six are prior; the protocol is still weaker on the paper's central claim.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Recorded voiced speech (Chem, GRID, LRS2) | Recorded speech video (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | MFA phoneme durations as aligner labels | Paired-audio targets (slot-filled 31) | – | standard |
| M03 Training and adaptation | ESPnet SpeechLM init, joint fine-tuning | Pretrain then adapt (slot-filled 1,526) | – | standard |
| M04 Use-time action | Script, lip video, reference voice | Visual TTS task (slot-filled 5,595) | – | standard |
| M05 Sensors | AV-HuBERT lip features, 25 fps | Camera video (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | Per-frame phoneme argmax into codec LM | Lip-derived timing, diffusion/flow/mel decoder (pattern match 5) | [[3]](#ref-3) (2026): Chem WER 9.65% vs EmoDubber 11.72% | standard |
| M07 Lexicon and LM | Reference speech prompt | Reference voice (slot-filled 119) | – | standard |
| M08 Output | EnCodec 8 codebooks, 16 kHz | Waveform (slot-filled 3,268) | – | standard |
| M09 Confirmation | Offline | Offline (slot-filled 82) | – | not applicable |
| M10 Correction | None | None (slot-filled 82) | – | not applicable |
| M11 Reference construction | Chem, GRID, LRS2 recordings | Recorded reference (slot-filled 234) | – | standard |
| M12 Evaluation | WER, Spk Sim, UTMOS, MCD-DTW-SL, A/B test | WER + listener test + SyncNet LSE (pattern match 6) | [[3]](#ref-3) (2026): Chem LSE-C 8.31, LSE-D 6.73 | standard |
| M13 Device and cost | Not reported | Research code (slot-filled 6,075) | – | not reported |

## Where the claims outrun the evidence

- §4.2 claims MCD-DTW-SL reductions of 17.6% on Chem and 60.9% on GRID. Table 1 gives 6.51 to 5.28 against EmoDubber, 18.9%, and 6.42 to 3.90 against StyleDubber, 39.3% (inference); EmoDubber, the stronger GRID baseline, scores 3.92 against 3.90.
- Baseline WER and MCD are copied from earlier papers, while UTMOS and Spk Sim are regenerated (Table 1 caption), so WER rests on other papers' ASR setups.
- Chem UTMOS of the full model is 3.73 in Tables 1–2 but 3.87 in Table 3, unexplained.
- The GRID split does not add up: 100 test clips per speaker for 33 speakers cannot give 900 test samples (§4.1).
- On GRID, ground truth scores 22.5% WER and VSpeechLM 18.3% (Table 1): the ASR bounds that column.
- The human study uses EmoDubber on Chem but StyleDubber on GRID (§4.3), and reports no tie rates, blinding or uncertainty.
- The LRS2 lead (16.1% vs 91.4–198% WER, Table 4) does not say how baselines were trained, and the decoder's pretraining corpus is not named (§4.1).

## What the field needs next

- M12: LSE-C/LSE-D with ground-truth and non-ground-truth references, and all baselines rescored with one ASR and one speaker model.
- M06: per-frame argmax against monotonic alignment search on the same decoder, with phoneme order errors.
- M06: the codec-language-model decoder against a flow-matching dubbing decoder at equal data, separating decoder from pretraining.
- M03: the pretraining corpus, and LRS2 baselines trained on the same data.

## Questions for the authors

- Is the test reference the target recording or another utterance of the speaker?
- How are 900 GRID test samples obtained from 100 clips for each of 33 speakers?
- Which models compute WER and Spk Sim?
- Why is Chem UTMOS 3.87 in Table 3 but 3.73 in Tables 1 and 2?
- On which data were the LRS2 baselines trained?
- How many runs or seeds stand behind each table, and is the validation split used for checkpoint selection?

## Appendix: literature search

- M06 text-and-video-to-speech-decoder. Inclusion rule: studies that synthesize a speech waveform from talking-face or lip video together with text, either given (visual TTS, video dubbing) or predicted by a lip reader and used in synthesis; plain video-to-speech, talking-head generation, recognition and TTS-only cascades excluded; versions counted once. Ledger: 7,345 slot-filled unique studies; pattern match 9 unique studies, 7 included after the boundary check (one plain video-to-speech study and one talking-head synthesis study excluded). Full-text design counts over the 7 (upper bound, related-work mentions included): diffusion 5, lip-derived phoneme timing 5, flow matching 4, duration-based mel synthesis 4, codec-token language model 2. Read in full: [[2]](#ref-2), [[3]](#ref-3), [[5]](#ref-5). Known-item recall 1.0 (5 seeds).
- M12 text-and-video-to-speech-evaluation. Inclusion rule: same population; protocols counted from the full text. Ledger: 6,960 slot-filled unique studies; pattern match 9 unique studies, 7 included (same exclusions). Counts over the 7: ASR WER 7, listener test 7, SyncNet LSE 6, speaker similarity 4, MCD-DTW-SL 2. Read in full: [[3]](#ref-3), [[2]](#ref-2), [[5]](#ref-5).

## References

Numbered by first citation. BibTeX in the same order and keys: [vspeechlm-a-visual-speech-language-model-for-visual-text-to-speech-task.bib](vspeechlm-a-visual-speech-language-model-for-visual-text-to-speech-task.bib).

1. <a id="ref-1"></a>Wang, Y., Cheng, X., Wu, Y., Wang, X., Tian, J., Song, R. “VSpeechLM: A Visual Speech Language Model for Visual Text-to-Speech Task.” *ACM Multimedia Asia (MMAsia '25)*, 2025. doi:[10.1145/3743093.3771012](https://doi.org/10.1145/3743093.3771012). arXiv:[2511.22229](https://arxiv.org/abs/2511.22229). Target. Read as arXiv v1 (27 Nov 2025). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/vspeechlm-a-visual-speech-language-model-for-visual-text-to-speech-task) [wiki: arxiv-2511.22229](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2511.22229/article.md)
2. <a id="ref-2"></a>Hegde, S., Mukhopadhyay, R., Jawahar, C. V., Namboodiri, V. “Towards Accurate Lip-to-Speech Synthesis in-the-Wild.” *Proceedings of the 31st ACM International Conference on Multimedia (MM '23)*, 2023. doi:[10.1145/3581783.3611787](https://doi.org/10.1145/3581783.3611787). arXiv:[2403.01087](https://arxiv.org/abs/2403.01087). Prior; deciding prior for the M06 aligner (video-text attention sets phoneme durations). [wiki: arxiv-2403.01087](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2403.01087/article.md)
3. <a id="ref-3"></a>Nguyen, N., Tran, T. V. T., Choi, J., Huynh-Nguyen, H., Hy, T., Nguyen, V. “DiFlowDubber: Discrete Flow Matching for Automated Video Dubbing via Cross-Modal Alignment and Synchronization.” *arXiv preprint*, 2026. arXiv:[2603.14267](https://arxiv.org/abs/2603.14267). [concurrent]; state of the art on Chem and GRID. Read as arXiv v4. [concurrent] [wiki: arxiv-2603.14267](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2603.14267/article.md)
4. <a id="ref-4"></a>Liu, J., Xiang, Y., Zhao, H., Li, X., Ling, Z. “FunCineForge: A Unified Dataset Toolkit and Model for Zero-Shot Movie Dubbing in Diverse Cinematic Scenes.” *arXiv preprint*, 2026. arXiv:[2601.14777](https://arxiv.org/abs/2601.14777). [concurrent]; in the text-and-video population (pattern match). [concurrent] [wiki: arxiv-2601.14777](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2601.14777/article.md)
5. <a id="ref-5"></a>Ghosh, S., Jawahar, C. V., Namboodiri, V. “LipAdapter: Text-to-Video Alignment is All You Need for Lip-to-Speech.” *Proc. Interspeech 2026*, 2026, 3548. doi:[10.21437/Interspeech.2026-518](https://doi.org/10.21437/Interspeech.2026-518). [later]; MAS durations from lips into a pretrained TTS. [later] [wiki: isca-ghosh26b_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-ghosh26b_interspeech/article.md) [wiki: isca-ghosh26b-lipadapt](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-ghosh26b-lipadapt/article.md)
6. <a id="ref-6"></a>Yemini, Y., Shamsian, A., Bracha, L., Gannot, S., Fetaya, E. “LipVoicer: Generating Speech from Silent Videos Guided by Lip Reading.” *International Conference on Learning Representations (ICLR)*, 2024. arXiv:[2306.03258](https://arxiv.org/abs/2306.03258). Prior; in the text-and-video population (pattern match). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lipvoicer-generating-speech-from-silent-videos-guided-by-lip-reading) [wiki: arxiv-2306.03258](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2306.03258/article.md)
7. <a id="ref-7"></a>Lee, G., Oh, Y., Han, Y. “Watch Your Speech: Text-aware Video-to-Speech Synthesis with Textual Conditioning.” *arXiv preprint*, 2026. arXiv:[2610.01012](https://arxiv.org/abs/2610.01012). [later]; in the text-and-video population (pattern match). [later] [wiki: arxiv-2610.01012-wys](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2610.01012-wys/article.md) [wiki: arxiv-2610.01012](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2610.01012/article.md)
