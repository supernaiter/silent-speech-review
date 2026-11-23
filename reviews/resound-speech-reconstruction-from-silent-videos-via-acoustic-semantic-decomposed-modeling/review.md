# RESOUND: Speech Reconstruction from Silent Videos via Acoustic-Semantic Decomposed Modeling

Pham, L.-K., Tran, T. V. T., Pham, M.-T., Nguyen, V. · Interspeech 2025 · 2025 · [doi:10.21437/Interspeech.2025-1160](https://doi.org/10.21437/Interspeech.2025-1160) · [arXiv:2505.22024](https://arxiv.org/abs/2505.22024)

## Verdict

RESOUND [[1]](#ref-1) changes the decoder (M06), splitting it into excitation and formant paths, and the use-time inputs (M07), adding lip-reader text and a 0.5 s audio prompt. Both are standard: source-filter synthesis from silent video dates to Vid2Speech [[2]](#ref-2) and pitch and energy predictors to Let There Be Sound [[3]](#ref-3), so the claim to be "the first study to incorporate source-filter theory into L2S synthesis" (§1; Appendix, M06) holds only as a label. The intelligibility gain comes from the lip reader: without L2T and SRA, LRS3 WER rises from 20.06 to 27.49, level with Intelligible L2S at 27.69 (Tables 1, 3). With it, RESOUND matches the field's best: 20.06 against 21.04 for LipVoicer in its table and 21.4% in LipVoicer's paper [[4]](#ref-4), and 28.55 against 17.04 on LRS2. The prosody and similarity leads (MAEF0 49.52 against 81.63, SECS 0.777 against 0.591 for LipVoicer) pit a system prompted with audio (§3.3) against systems given none. The SOTA claim (§5) rests on no reported repeated runs and baseline rows of unstated provenance.

## Against the field, component by component

### M06 Decoder: excitation and formant generators

**Usual approach:** Of 165 video-to-speech studies (pattern match, Appendix), 54 name adversarial training on the regressed acoustic output and 9 a pitch, energy or variance predictor. RESOUND adds FastSpeech 2 pitch and energy predictors and sums excitation and formant generators into a coarse mel (§2.3).

**State of the art:** LipVoicer (ICLR 2024): LRS3 WER 21.4% with lip-reader text at inference [[4]](#ref-4); a [later] AUTO-AVSR re-score gives 20.62%, still the lowest WER in that 2026 table [[5]](#ref-5). RESOUND's 20.06 is level with both.

Five of the 165 studies match "source-filter" (pattern match, Appendix). Vid2Speech predicts LPC filter features from video and leaves excitation "out of the scope", using white noise [[2]](#ref-2); VCVTS added a pitch predictor [[6]](#ref-6), Let There Be Sound pitch and energy predictors [[3]](#ref-3), and the [concurrent] NaturalL2S drives a harmonic source with predicted F0 [[7]](#ref-7). New is only the summed split in mel space, and the ablation does not isolate it: "w/o Acoustic branch" removes the Prosody Encoder and the Excitation Generator together (§4.2), taking UTMOS from 3.002 to 2.176 (28% relative), below Intelligible L2S at 2.680 [[8]](#ref-8), and MAEF0 from 49.52 to 69.219 (40%). Verdict: standard.

### M07 Use-time inputs: lip-reader text and audio prompt

**Usual approach:** Of the 165 studies (pattern match, Appendix), 21 name a reference-audio speaker embedding, 23 an audio prompt or reference segment and 16 lip-reader text. RESOUND uses a 0.5 s prompt for timbre, pitch and energy (§1, §3.3) and Auto-AVSR text as phonemes (§2.2.1).

**State of the art:** V2SFlow (2024, [concurrent]): SECS 0.851 with an audio-derived and 0.664 with a video-derived embedding on unseen LRS3 speakers, both at 28.5% WER [[9]](#ref-9).

LipVoicer conditions on text from the same lip-reader family at inference [[4]](#ref-4). That text carries RESOUND's WER: removing L2T and SRA raises it by 37% relative while UTMOS moves only from 3.002 to 2.840 (Table 3). The prompt is the confound: a random 0.5 s ground-truth segment (§3.3); if cut from the test utterance, it hands over its pitch, energy and timbre. The MAEF0 lead and the similarity MOS lead (3.57 against 2.40 for LipVoicer and 2.96 for DiffV2S, Table 2) compare a prompted system with systems given no audio; DiffV2S takes speaker identity from video alone [[10]](#ref-10). Against Intelligible L2S the gaps shrink to SECS 0.777 against 0.750 and MAEF0 49.52 against 55.42. Verdict: standard.

### M12 Evaluation: comparison table and listener test

**Usual approach:** Of 165 studies (pattern match, published counts), 83 name a listener test, 38 ASR WER on the output and 51 an unseen-speaker test. RESOUND reports Auto-AVSR WER and a 30-participant MOS with 95% confidence intervals (Table 2), but states no unseen-speaker split or repeated runs (§3.1, §3.3).

**State of the art:** LipVoicer (ICLR 2024), as for M06: 21.4% LRS3 WER [[4]](#ref-4); 20.62% in a [later] table [[5]](#ref-5).

Baseline rows are of unstated provenance: LipVoicer's 21.04 differs from its own 21.4% [[4]](#ref-4). On LRS2 RESOUND trails LipVoicer by 11.51 points (68% relative) (inference), attributed to noise without a test (§4.1), yet the conclusion claims SOTA (§5). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | LRS2, LRS3 overt speech | Recorded speech video (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | HuBERT units, Praat F0, energy | Paired-audio targets (slot-filled 31) | – | standard |
| M03 Training and adaptation | AV-HuBERT frozen (LRS3), tuned (LRS2) | Training records (slot-filled 1,526) | – | standard |
| M04 Use-time action | Overt speech, audio muted | Silent or overt (slot-filled 5,595) | – | standard |
| M05 Sensors | Mouth crop 96x96 | Camera video (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | Excitation and formant generators | Adversarial training (pattern match 54) | [[4]](#ref-4) (2024): LRS3 WER 21.4% | standard |
| M07 Lexicon and LM | Lip-reader text, 0.5 s audio prompt | Audio-reference embedding (pattern match 21) | [[9]](#ref-9) (2024): SECS 0.851 | standard |
| M08 Output | Waveform via multi-input vocoder | Waveform or text (slot-filled 3,268) | – | standard |
| M09 Confirmation | Offline | Offline (slot-filled 82) | – | not applicable |
| M10 Correction | Offline | Offline (slot-filled 82) | – | not applicable |
| M11 Reference construction | LRS2, LRS3 references | Corpus references (slot-filled 234) | – | standard |
| M12 Evaluation | 30-listener MOS, ASR WER | Listener test (pattern match 83) | [[4]](#ref-4) (2024): LRS3 WER 21.4% | standard |
| M13 Device and cost | RTF 0.063; no hardware | Hardware and cost (slot-filled 6,075) | – | standard |

## Where the claims outrun the evidence

- "This separated structure leads to the improvement of speech accuracy and naturalness" (§1): accuracy follows the lip reader (Table 3), and naturalness is tested only by removing two modules at once (§4.2).
- "Over 200 times slower" and "potential for real-time applications" (§4.1): RTF 0.063 against 14.117 with no hardware or timed pipeline stated, and Intelligible L2S is faster at 0.041 (Table 1).
- No seeds or run counts in the paper (§3.3).

## What the field needs next

- M07: MAEF0 and SECS with prompts from another utterance of the speaker, and with none.
- M06: removing only the excitation/formant split, predictors kept, over several seeds.
- M12: baselines rerun under one ASR, prompt protocol and timed pipeline on unseen LRS3 speakers.

## Questions for the authors

- At test time, is the 0.5 s prompt cut from the utterance being reconstructed?
- Were Table 1 baselines rerun, and with which prompts?
- Does the RTF of 0.063 include Auto-AVSR and G2P, and on which hardware?
- Do LRS3 test speakers appear in training or AV-HuBERT pre-training?

## Appendix: literature search

- M06, video-to-speech-one-to-many-decoder (published table, reused). Inclusion rule: the video-to-speech population (speech synthesized from talking-face or lip video, audio muted at test), classified from full text with the reference list removed by how the decoder handles the one-to-many mapping; a study counts under every design it names (upper bound); enhancement with noisy audio, talking-head generation and video-to-text-to-speech pipelines excluded; versions count once. Ledger: 7,345 unique studies slot-filled for M06; 165 unique studies pattern match. Designs: adversarial training 54, SSL-unit conditioning 44, diffusion decoder 22, flow decoder 19, pitch or energy predictor 9 (pattern match, published counts); "source-filter" 5, excitation and formant in one sentence 1 (pattern match, this review). Read in full: [[2]](#ref-2), [[6]](#ref-6), [[3]](#ref-3), [[4]](#ref-4), [[5]](#ref-5). Known-item recall 1.0.
- M07, reference-speaker-conditioning-at-inference (published table, reused). Inclusion rule: the same 165 studies, classified by the speaker information supplied at use time (reference-audio embedding, face- or video-derived embedding, none); training-only or scoring-only embeddings excluded; every named design counts (upper bound); for this review also audio prompts and lip-reader text at use time. Ledger: 119 unique studies slot-filled for M07; 165 unique studies pattern match. Reference-audio embedding 21, video- or face-derived 16, none claimed 2 (pattern match, published counts); audio prompt or reference segment 23, lip-reader text 16 (pattern match, this review, related-work mentions included). Read in full: [[10]](#ref-10), [[9]](#ref-9), [[4]](#ref-4). Known-item recall 1.0.
- M12, video-to-speech-output-evaluation (published table, reused). Inclusion rule: the same video-to-speech population, counting the evaluation protocols its full text names (listener tests, ASR WER on the output, unseen-speaker tests). Ledger: 6,960 unique studies slot-filled for M12; 165 unique studies pattern match. Listener test 83, unseen speakers 51, ASR WER on output 38 (pattern match, published counts). Read in full: [[4]](#ref-4), [[5]](#ref-5). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Pham, L., Tran, T. V. T., Pham, M., Nguyen, V. “RESOUND: Speech Reconstruction from Silent Videos via Acoustic-Semantic Decomposed Modeling.” *Interspeech 2025*, 2025. doi:[10.21437/Interspeech.2025-1160](https://doi.org/10.21437/Interspeech.2025-1160). arXiv:[2505.22024](https://arxiv.org/abs/2505.22024). Target. Read as arXiv v1. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/resound-speech-reconstruction-from-silent-videos-via-acoustic-semantic-decomposed-modeling) [wiki: arxiv-2505.22024](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2505.22024/article.md) [wiki: isca-pham25-resound](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-pham25-resound/article.md)
2. <a id="ref-2"></a>Ephrat, A., Peleg, S. “Vid2speech: Speech Reconstruction from Silent Video.” *2017 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2017, 5095-5099. doi:[10.1109/ICASSP.2017.7953127](https://doi.org/10.1109/ICASSP.2017.7953127). arXiv:[1701.00495](https://arxiv.org/abs/1701.00495). Prior; deciding prior for M06 (LPC source-filter synthesis from silent video, white-noise excitation). Read in Secs. 3.1-3.2. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/vid2speech-speech-reconstruction-from-silent-video) [wiki: arxiv-1701.00495](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1701.00495/article.md)
3. <a id="ref-3"></a>Kim, J., Kim, J., Chung, J. S. “Let There Be Sound: Reconstructing High Quality Speech from Silent Videos.” *Proceedings of the AAAI Conference on Artificial Intelligence (AAAI-24)*, 2024. arXiv:[2308.15256](https://arxiv.org/abs/2308.15256). Prior; cited by the target; deciding prior for M06 (pitch and energy predictors beside an SSL-unit linguistic predictor). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/let-there-be-sound-reconstructing-high-quality-speech-from-silent-videos) [wiki: arxiv-2308.15256](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2308.15256/article.md)
4. <a id="ref-4"></a>Yemini, Y., Shamsian, A., Bracha, L., Gannot, S., Fetaya, E. “LipVoicer: Generating Speech from Silent Videos Guided by Lip Reading.” *International Conference on Learning Representations (ICLR)*, 2024. arXiv:[2306.03258](https://arxiv.org/abs/2306.03258). Prior; state of the art for M06 and M12; deciding prior for M07 (lip-reader text at inference). Read in Table 4 and Sec. 5.1. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lipvoicer-generating-speech-from-silent-videos-guided-by-lip-reading) [wiki: arxiv-2306.03258](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2306.03258/article.md)
5. <a id="ref-5"></a>Liang, Y., Li, A., Yang, K., Yu, G., Liu, F., Dai, L., et al. “SLD-L2S: Hierarchical Subspace Latent Diffusion for High-Fidelity Lip to Speech Synthesis.” *arXiv preprint (AAAI 2026 copyright line)*, 2026. doi:[10.48550/arXiv.2602.11477](https://doi.org/10.48550/arXiv.2602.11477). arXiv:[2602.11477](https://arxiv.org/abs/2602.11477). Re-scores LipVoicer with AUTO-AVSR (Table 1). Read in Table 1 and Experimental Setup. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/sld-l2s-hierarchical-subspace-latent-diffusion-for-high-fidelity-lip-to-speech-synthesis) [wiki: arxiv-2602.11477](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.11477/article.md) [wiki: arxiv-2602.11477-sldl2s](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.11477-sldl2s/article.md)
6. <a id="ref-6"></a>Wang, D., Yang, S., Su, D., Liu, X., Yu, D., Meng, H. “VCVTS: Multi-Speaker Video-to-Speech Synthesis via Cross-Modal Knowledge Transfer from Voice Conversion.” *ICASSP 2022 - IEEE International Conference on Acoustics, Speech and Signal Processing*, 2022, 7252-7256. doi:[10.1109/ICASSP43922.2022.9747427](https://doi.org/10.1109/ICASSP43922.2022.9747427). arXiv:[2202.09081](https://arxiv.org/abs/2202.09081). Prior; deciding prior for M06 (pitch predictor in video-to-speech). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/vcvts-multi-speaker-video-to-speech-synthesis-via-cross-modal-knowledge-transfer-from-voice-conversion) [wiki: arxiv-2202.09081-vcvts](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2202.09081-vcvts/article.md)
7. <a id="ref-7"></a>Liang, Y., Liu, F., Li, A., Li, X., Zheng, C. “NaturalL2S: End-to-End High-quality Multispeaker Lip-to-Speech Synthesis with Differential Digital Signal Processing.” *arXiv preprint*, 2025. doi:[10.48550/arXiv.2502.12002](https://doi.org/10.48550/arXiv.2502.12002). arXiv:[2502.12002](https://arxiv.org/abs/2502.12002). F0-driven harmonic-plus-noise DDSP source in lip-to-speech. Read in Sec. III. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/naturall2s-end-to-end-high-quality-multispeaker-lip-to-speech-synthesis-with-differential-digita) [wiki: arxiv-2502.12002](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2502.12002/article.md)
8. <a id="ref-8"></a>Choi, J., Kim, M., Ro, Y. M. “Intelligible Lip-to-Speech Synthesis with Speech Units.” *Interspeech 2023*, 2023, 4349-4353. doi:[10.21437/Interspeech.2023-194](https://doi.org/10.21437/Interspeech.2023-194). arXiv:[2305.19603](https://arxiv.org/abs/2305.19603). Prior; baseline and lineage of the target (speech-unit targets, multi-input vocoder). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/intelligible-lip-to-speech-synthesis-with-speech-units) [wiki: arxiv-2305.19603](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2305.19603/article.md) [wiki: isca-choi23-liptospeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-choi23-liptospeech/article.md) [wiki: isca-choi23_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-choi23_interspeech/article.md)
9. <a id="ref-9"></a>Choi, J., Kim, J., Li, J., Chung, J. S., Liu, S. “V2SFlow: Video-to-Speech Generation with Speech Decomposition and Rectified Flow.” *arXiv preprint*, 2024. arXiv:[2411.19486](https://arxiv.org/abs/2411.19486). State of the art for M07 (speaker embedding from audio or video). Read in Table I and Sec. III-A. [concurrent] [wiki: arxiv-2411.19486](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2411.19486/article.md)
10. <a id="ref-10"></a>Choi, J., Hong, J., Ro, Y. M. “DiffV2S: Diffusion-based Video-to-Speech Synthesis with Vision-guided Speaker Embedding.” *2023 IEEE/CVF International Conference on Computer Vision (ICCV)*, 2023, 6692-6701. doi:[10.1109/ICCV51070.2023.00618](https://doi.org/10.1109/ICCV51070.2023.00618). arXiv:[2308.07787](https://arxiv.org/abs/2308.07787). Prior; baseline of the target; video-derived speaker embedding, no reference audio at inference. [wiki: arxiv-2308.07787-diffv2s](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2308.07787-diffv2s/article.md) [wiki: cvf23-choi_diffv2s](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf23-choi_diffv2s/article.md)
