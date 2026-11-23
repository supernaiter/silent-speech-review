# LTA-L2S: Lexical Tone-Aware Lip-to-Speech Synthesis for Mandarin with Cross-Lingual Transfer Learning

Yang, K., Liang, Y., Liu, F., Xie, Z., Zheng, C. · arXiv preprint · 2025 · [arXiv:2509.25670](https://arxiv.org/abs/2509.25670)

## Verdict

LTA-L2S [[1]](#ref-1) changes the encoder initialization (M03), unit target (M02) and F0 decoder (M06) of Mandarin lip-to-speech; all three are standard. Its lowest CER (61.2%) and TER (40.9%) on CN-CVS unseen speakers hold against five baselines (Table 1), but random initialization alone returns CER to 74.6%, near Intelligible (74.9%), while tone-specific variants move CER 0.3 to 3.2 points in single runs (Tables 3-4, inference). Removing the pitch predictor leaves TER at 40.9% (Table 3), so its own tone metric does not support the tone-aware label. The closest design, V2SFlow [[2]](#ref-2), is not compared, and FA-GAN [[3]](#ref-3), the other CN-CVS study, is not cited. Test labels are FunASR transcripts with no real-audio error reported (M11, behind).

## Against the field, component by component

### M03 Training: English-pretrained encoder

**Usual approach:** Of 468 non-English visual-speech studies (pattern match, Appendix), 43 name AV-HuBERT, 21 English or cross-lingual transfer, 19 training from scratch; the paper fine-tunes AV-HuBERT Base pretrained on 1,759 hours of English (Sec. 2.1).

**State of the art:** In Mandarin CMLR recognition, English-only pretraining gives 16.2% CER, Mandarin-only 22.6%, six-language 15.8% [[4]](#ref-4) (2023).

Random initialization raises CER from 61.2% to 74.6% (Table 4), 18% relative, against 28% in recognition, whose baseline is Mandarin-pretrained (inference). Multilingual pretraining beat English-only there (Sec. 5.2) [[4]](#ref-4), untested here. Verdict: standard.

### M02 Supervision: unit target

**Usual approach:** Of 54 non-acoustic-to-speech studies with self-supervised targets (pattern match, Appendix), 23 use HuBERT units, 12 an F0 target, like V2SFlow [[2]](#ref-2); the paper clusters layer 9 of an ASR-fine-tuned wav2vec 2.0 into 2,000 units (Sec. 2.2).

**State of the art:** V2SFlow (2024): 28.5% WER, LRS3 unseen speakers [[2]](#ref-2).

The ASR-fine-tuned target is in 1 of the 54 studies, the paper (Appendix); HuBERT units give 64.4% CER against 61.2%, with no repeats reported (Table 4). Verdict: standard.

### M06 Decoding: flow-matching F0 and postnet

**Usual approach:** Adversarial training leads (54 of 165 video-to-speech studies, pattern match, Appendix); flow decoders appear in 19, pitch predictors in 9, since VCVTS (2022) [[5]](#ref-5). The paper adds rectified-flow F0 and a flow-matching mel postnet (Secs. 2.3-2.5).

**State of the art:** V2SFlow (2024; content, pitch and speaker from video, rectified-flow decoder): 28.5% WER, LRS3 [[2]](#ref-2). On CN-CVS, FA-GAN (2024) reports 43.19% WER on single-speaker data [[3]](#ref-3).

The paper keeps V2SFlow's decomposition with continuous pitch, but not V2SFlow in Tables 1-2. Removing pitch changes neither V2SFlow's WER (28.5%) [[2]](#ref-2) nor LTA-L2S's TER (40.9%, Table 3). The postnet lifts DNSMOS (2.942 to 3.200), yet the variant without it has the best CER (61.0%) and TER (40.7%, Table 3). Verdict: standard.

### M11-M12 Evaluation: re-transcribed labels

**Usual approach:** Of 165 video-to-speech studies (pattern match, Appendix), 83 run a listener test, 38 score output by ASR and 20 report the ASR error on real audio; 2, SVTS [[6]](#ref-6) and this paper, use ASR transcripts of real audio as reference. The paper re-labels the CN-CVS test set with FunASR (Sec. 3.1).

**State of the art:** V2SFlow (2024) prints the real-audio ASR error, 2.5% WER on LRS3, beside every system [[2]](#ref-2).

The ground-truth row has no CER or TER (Table 1), so FunASR's error against corpus labels is unknown; Intelligible [[7]](#ref-7), GAN-based video-to-speech [[8]](#ref-8) and SVTS report the real-audio error: M11 is behind the best comparable work. Values are protocol-bound: FA-GAN lists VCA-GAN at 49.70% WER (single speaker, CN-CVS-trained ASR) [[3]](#ref-3), this paper at 96.5% CER (unseen speakers, FunASR; Table 1). M12 is standard but unrepeated (Sec. 3.4).

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | CN-CVS speech video | Recorded speech video (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | ASR-fine-tuned w2v2 units, F0 | HuBERT units (pattern match 23) | [[2]](#ref-2) (2024): 28.5% WER | standard |
| M03 Training and adaptation | English AV-HuBERT init | AV-HuBERT encoder (pattern match 43) | [[4]](#ref-4) (2023): 16.2% CER | standard |
| M04 Use-time action | Overt, audio muted | Silent or overt (slot-filled 5,595) | – | standard |
| M05 Sensors | 96x96 lip crop | Camera video (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | Flow F0, flow postnet | Adversarial training (pattern match 54) | [[2]](#ref-2) (2024): 28.5% WER | standard |
| M07 Lexicon and LM | Speaker embedding | Lexicon or LM (slot-filled 119) | – | standard |
| M08 Output | HiFi-GAN | Waveform or text (slot-filled 3,268) | – | standard |
| M09 Confirmation | Offline | Offline (slot-filled 82) | – | not applicable |
| M10 Correction | Offline | Offline (slot-filled 82) | – | not applicable |
| M11 Reference construction | FunASR test labels | Real-audio error (pattern match 20) | [[2]](#ref-2) (2024): 2.5% WER | behind |
| M12 Evaluation | 15 listeners, CER/TER | Listener test (pattern match 83) | [[3]](#ref-3) (2024): 43.19% WER | standard |
| M13 Device and cost | Two GPUs | Hardware and cost (slot-filled 6,075) | – | standard |

## Where the claims outrun the evidence

- Tone-aware: TER is computed from FunASR text via g2pM (Sec. 3.4), so it scores the recognized syllable's tone, not the generated F0; it does not move when pitch is removed (Table 3).
- Attribution: the gain over Intelligible (74.9%) matches the random-initialization gap (74.6%, Tables 1 and 4); no seeds back smaller effects (Sec. 3.2).
- "Significantly" (Abstract): no statistical test; MOS ± undefined (Table 2).
- Sec. 4.3 reports PER where Table 4 reports TER.
- The audio behind the test speaker embedding is unstated (Sec. 2.3), so voice identity from lips alone is not shown.

## What the field needs next

- M03: English-only, multilingual and Mandarin-pretrained encoders on one CN-CVS split [[4]](#ref-4).
- M06: continuous, quantized and no pitch over several seeds, tone scored from the synthesized F0.
- M11: real-audio CER and TER against CN-CVS and FunASR labels.
- M12: VCA-GAN and FA-GAN [[3]](#ref-3) rescored under one CN-CVS protocol.

## Questions for the authors

- Which FunASR model made the labels, and how many labels changed?
- How many runs stand behind Tables 3-4, and what is ± in Table 2?
- How many speakers and hours are in the test split, and how was the checkpoint selected?

## Appendix: literature search

- M03, cross-lingual-encoder-transfer-to-video-speech. Inclusion rule: lip-reading, visual speech recognition and video-to-speech studies whose ledger names a non-English or multilingual target, classified from full text (reference list removed) by whether the visual encoder is transferred from English or other external pretraining, is AV-HuBERT-family, or is trained from scratch; a study counts under every design it names (upper bound); audio-only encoders excluded; versions counted once. Ledger: 1,526 unique studies slot-filled for M03; 468 unique studies pattern match. Designs (pattern match): AV-HuBERT-family encoder 43, English or cross-lingual transfer 21, trained from scratch 19. Read in full: [[4]](#ref-4). Known-item recall 1.0.
- M02, ssl-speech-unit-target (published table, reused). Inclusion rule: speech synthesized from a non-acoustic signal with the encoder trained to predict self-supervised speech representations from paired audio; recognition-only studies, self-generated targets and acoustic-input conversion excluded; versions counted once. Ledger: 31 unique studies slot-filled for M02; 54 unique studies pattern match; usual design paired audio 11 of 22 (slot-filled, published). Added (full-text pattern match over the 54): HuBERT unit target 23, F0 or pitch target 12, ASR-fine-tuned SSL target 1 (the target). Read in full: [[7]](#ref-7), [[2]](#ref-2). Known-item recall 1.0 (published seeds); 0.75 for this review's seeds.
- M06, video-to-speech-one-to-many-decoder (published table, reused). Inclusion rule: video-to-speech studies (speech synthesized from talking-face or lip video, audio muted at test), classified from full text by decoder design; enhancement with noisy audio at test, talking-head generation and video-to-text-to-speech pipelines excluded; versions counted once. Ledger: 7,345 unique studies slot-filled for M06; 165 unique studies pattern match. Designs (published counts): adversarial training 54, speech-unit conditioning 44, diffusion decoder 22, flow decoder 19, pitch or energy predictor 9. Read in full: [[2]](#ref-2), [[5]](#ref-5), [[9]](#ref-9), [[7]](#ref-7). Known-item recall 1.0 (published seeds); 0.64 for this review's seeds.
- M11, asr-retranscribed-evaluation-reference. Inclusion rule: the same video-to-speech population, classified from full text by how the text reference for ASR scoring is built (ASR transcripts of real audio as reference) and whether the ASR error on real test audio is reported; a study counts under every design it names (upper bound); versions counted once. Ledger: 234 unique studies slot-filled for M11; 165 unique studies pattern match. Designs (pattern match): real-audio ASR error reported 20, ASR transcripts of real audio as reference 2 ([[6]](#ref-6) and the target). Read in full: [[6]](#ref-6), [[7]](#ref-7), [[8]](#ref-8), [[2]](#ref-2), [[3]](#ref-3). Known-item recall 1.0.
- M12, video-to-speech-output-evaluation (published table, reused). Inclusion rule: the same video-to-speech population, counting the evaluation protocols its full text names. Ledger: 6,960 unique studies slot-filled for M12; 165 unique studies pattern match. Protocols (published counts): listener test 83, unseen speakers 51, ASR WER on output 38. CN-CVS video-to-speech studies in the population: [[3]](#ref-3) and the target. Read in full: [[3]](#ref-3), [[10]](#ref-10), [[6]](#ref-6). Known-item recall 1.0 (published seeds); 0.64 for this review's seeds.

## References

Numbered by first citation. BibTeX in the same order and keys: [lta-l2s-lexical-tone-aware-lip-to-speech-synthesis-for-mandarin-with-cross-lingual-transfer-lear.bib](lta-l2s-lexical-tone-aware-lip-to-speech-synthesis-for-mandarin-with-cross-lingual-transfer-lear.bib).

1. <a id="ref-1"></a>Yang, K., Liang, Y., Liu, F., Xie, Z., Zheng, C. “LTA-L2S: Lexical Tone-Aware Lip-to-Speech Synthesis for Mandarin with Cross-Lingual Transfer Learning.” *arXiv preprint*, 2025. doi:[10.48550/arXiv.2509.25670](https://doi.org/10.48550/arXiv.2509.25670). arXiv:[2509.25670](https://arxiv.org/abs/2509.25670). Target. Read as arXiv v1. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lta-l2s-lexical-tone-aware-lip-to-speech-synthesis-for-mandarin-with-cross-lingual-transfer-lear) [wiki: arxiv-2509.25670](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2509.25670/article.md) [wiki: arxiv-2509.25670-ltal2s](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2509.25670-ltal2s/article.md)
2. <a id="ref-2"></a>Choi, J., Kim, J., Li, J., Chung, J. S., Liu, S. “V2SFlow: Video-to-Speech Generation with Speech Decomposition and Rectified Flow.” *arXiv preprint*, 2024. arXiv:[2411.19486](https://arxiv.org/abs/2411.19486). Prior; closest design for M06, state of the art for M02, M06 and M11. Read as arXiv v2. [wiki: arxiv-2411.19486](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2411.19486/article.md)
3. <a id="ref-3"></a>Yang, Q., Bai, Y., Liu, F., Zhang, W. “Integrated visual transformer and flash attention for lip-to-speech generation GAN.” *Scientific Reports*, 2024, 14, 4525. doi:[10.1038/s41598-024-55248-6](https://doi.org/10.1038/s41598-024-55248-6). Prior; the other CN-CVS video-to-speech study in the wiki; not cited by the target. [wiki: doi-10.1038-s41598-024-55248-6](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41598-024-55248-6/article.md) [wiki: pmc-10894270-fagan-lts](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10894270-fagan-lts/article.md)
4. <a id="ref-4"></a>Zinonos, A., Haliassos, A., Ma, P., Petridis, S., Pantic, M. “Learning Cross-Lingual Visual Speech Representations.” *arXiv preprint*, 2023. arXiv:[2303.09455](https://arxiv.org/abs/2303.09455). Prior; deciding prior and reference point for M03. Read as arXiv v1. [wiki: arxiv-2303.09455](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2303.09455/article.md)
5. <a id="ref-5"></a>Wang, D., Yang, S., Su, D., Liu, X., Yu, D., Meng, H. “VCVTS: Multi-Speaker Video-to-Speech Synthesis via Cross-Modal Knowledge Transfer from Voice Conversion.” *arXiv preprint*, 2022. doi:[10.48550/arXiv.2202.09081](https://doi.org/10.48550/arXiv.2202.09081). arXiv:[2202.09081](https://arxiv.org/abs/2202.09081). Prior; pitch predicted from video (M06). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/vcvts-multi-speaker-video-to-speech-synthesis-via-cross-modal-knowledge-transfer-from-voice-conversion) [wiki: arxiv-2202.09081-vcvts](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2202.09081-vcvts/article.md)
6. <a id="ref-6"></a>Mira, R., Haliassos, A., Petridis, S., Schuller, B. W., Pantic, M. “SVTS: Scalable Video-to-Speech Synthesis.” *arXiv preprint*, 2022. arXiv:[2205.02058](https://arxiv.org/abs/2205.02058). Prior; baseline of the target; ASR references from real audio (M11). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/svts-scalable-video-to-speech-synthesis) [wiki: arxiv-2205.02058](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2205.02058/article.md)
7. <a id="ref-7"></a>Choi, J., Kim, M., Ro, Y. M. “Intelligible Lip-to-Speech Synthesis with Speech Units.” *arXiv preprint (Interspeech 2023)*, 2023. arXiv:[2305.19603](https://arxiv.org/abs/2305.19603). Prior; baseline of the target; M02, M06 and M11. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/intelligible-lip-to-speech-synthesis-with-speech-units) [wiki: arxiv-2305.19603](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2305.19603/article.md) [wiki: isca-choi23-liptospeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-choi23-liptospeech/article.md) [wiki: isca-choi23_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-choi23_interspeech/article.md)
8. <a id="ref-8"></a>Vougioukas, K., Ma, P., Petridis, S., Pantic, M. “Video-Driven Speech Reconstruction using Generative Adversarial Networks.” *Proc. Interspeech 2019*, 2019. doi:[10.21437/Interspeech.2019-1445](https://doi.org/10.21437/Interspeech.2019-1445). Prior; reports real-audio ASR error (M11). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/video-driven-speech-reconstruction-using-generative-adversarial-networks) [wiki: isca-vougioukas19_ganv2s](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-vougioukas19_ganv2s/article.md)
9. <a id="ref-9"></a>Kim, M., Hong, J., Ro, Y. M. “Lip to Speech Synthesis with Visual Context Attentional GAN.” *arXiv preprint*, 2022. arXiv:[2204.01726](https://arxiv.org/abs/2204.01726). Prior; baseline of the target; adversarial decoder (M06). [wiki: arxiv-2204.01726](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2204.01726/article.md)
10. <a id="ref-10"></a>Kim, M., Hong, J., Ro, Y. M. “Lip-to-Speech Synthesis in the Wild with Multi-Task Learning.” *arXiv preprint (ICASSP 2023)*, 2023. arXiv:[2302.08841](https://arxiv.org/abs/2302.08841). Prior; baseline of the target (M12). [wiki: arxiv-2302.08841](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2302.08841/article.md)
