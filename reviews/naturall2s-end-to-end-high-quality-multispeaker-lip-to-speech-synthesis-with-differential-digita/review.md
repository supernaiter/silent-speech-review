# NaturalL2S: End-to-End High-quality Multispeaker Lip-to-Speech Synthesis with Differential Digital Signal Processing

Liang, Y., Liu, F., Li, A., Li, X., Zheng, C. · arXiv preprint · 2025 · [arXiv:2502.12002](https://arxiv.org/abs/2502.12002)

## Verdict

NaturalL2S [[1]](#ref-1) changes the waveform generator (M06), a DDSP harmonic-and-noise prior feeding a conditional HiFi-GAN trained jointly behind a frozen AV-HuBERT, and drops use-time speaker input (M07). Both are standard: joint end-to-end waveform generation for many speakers predates it [[2]](#ref-2), [[3]](#ref-3), so the "first attempt" claim (§I) fails, and reference-free use follows DiffV2S [[4]](#ref-4). The quality lead over the four compared systems (Tables I–III) recurs in a [later] same-group test [[5]](#ref-5). Content does not: LRS3 WER is 30.4%, behind Lip2Speech Unit (27.7%, Table II) and the cited but uncompared LipVoicer (21.4%) [[6]](#ref-6). The joint-training ablation also removes DDSP and changes the vocoder corpus, and removing DDSP alone lowers DNS-MOS only from 2.95 to 2.89 (Table IV), so the source of the gain is not isolated.

## Against the field, component by component

### M06 Waveform generation: DDSP prior and joint vocoder

**Usual approach:** Of 165 video-to-speech studies (pattern match, Appendix), 49 name a neural vocoder on predicted acoustic features and 15 a pre-trained or separately trained vocoder. NaturalL2S instead trains a DDSP-conditioned HiFi-GAN with the generators.

**State of the art:** LipVoicer (ICLR 2024): LRS3 WER 21.4%, STOI-Net 0.92, DNSMOS 3.11 (Table 4) [[6]](#ref-6). NaturalL2S is 0.02 STOI-Net and 0.12 DNS-MOS higher and 9.0 WER points (42% relative) worse (inference); a [later] one-ASR table keeps the order, 30.37% against 20.62% [[5]](#ref-5).

Mira et al. already generate waveforms end-to-end on LRW, with hundreds of speakers [[2]](#ref-2), and Facetron trains a face-to-waveform GAN end-to-end on 33 GRID speakers [[3]](#ref-3). The DDSP prior is new to video-to-speech; the only other DDSP study among the 165 is [concurrent] (Appendix). The single-run LRS2 ablations (§V-C) do not separate the two: wo-e2e also drops DDSP and uses a vanilla HiFi-GAN trained on LRS3; DNS-MOS falls from 2.95 to 2.39 at equal WER (36.3% against 36.5%); wo-DDSP keeps joint training and scores 2.89 DNS-MOS and 37.0% WER (Table IV). Verdict: standard.

### M07 Use-time speaker information: none

**Usual approach:** Of the 165 studies (pattern match, Appendix), 21 name a speaker embedding from reference audio and 16 one derived from the face or video; NaturalL2S uses neither (§I).

**State of the art:** V2SFlow (2024, [concurrent]): on unseen LRS3 speakers SECS 0.664 from a video-derived and 0.851 from a reference-audio embedding, both at 28.5% WER (Table I) [[7]](#ref-7).

DiffV2S derives the speaker embedding from video alone [[4]](#ref-4). Without any speaker input NaturalL2S reaches voice similarity 0.63 on both sets, against 0.58 and 0.63 for DiffV2S and 0.72 and 0.76 for the reference-embedding Lip2Speech Unit (Tables I–II); the [later] re-score gives 0.628 against 0.627 (LRS3) and 0.562 against 0.569 (LRS2) for DiffV2S [[5]](#ref-5). Verdict: standard.

### M12 Evaluation: comparison set and listener test

**Usual approach:** Of 165 studies (pattern match, published counts), 83 name a listener test, 38 ASR WER, 51 unseen speakers and 40 confidence intervals or significance tests. NaturalL2S gives Auto-AVSR WER, predicted quality and a 15-listener test, without statistical tests (Tables I–IV).

**State of the art:** LipVoicer (ICLR 2024), 21.4% LRS3 WER [[6]](#ref-6); 20.62% against 30.37% for NaturalL2S in a [later] AUTO-AVSR table [[5]](#ref-5).

LipVoicer is set aside for relying on text (§I), yet its text comes from a lip reader on the same silent video [[6]](#ref-6). DiffV2S and the LRS2 Lip2Speech Unit are scored on author-supplied samples (§V); MOS pools LRS2 and LRS3 (Table III). STOI-Net rates NaturalL2S above ground truth (0.92 against 0.91, 0.94 against 0.93), a ceiling that cannot rank systems (inference). The [later] LRS3 listener test puts NaturalL2S (naturalness 3.54) above DiffV2S (2.95) and LipVoicer (2.51), below V2SFlow (3.88) [[5]](#ref-5). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | LRS2, LRS3 overt speech | Recorded speech video (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | HuBERT units, F0, mel targets | Paired-audio targets (slot-filled 31) | – | standard |
| M03 Training and adaptation | One run; GT F0 in training | Training records (slot-filled 1,526) | – | standard |
| M04 Use-time action | Overt speech, audio muted | Silent or overt (slot-filled 5,595) | – | standard |
| M05 Sensors | Mouth crop, frozen AV-HuBERT | Camera video (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | DDSP prior, joint HiFi-GAN | Vocoder on features (pattern match 49) | [[6]](#ref-6) (2024): WER 21.4% | standard |
| M07 Lexicon and LM | No speaker input | Audio-reference embedding (pattern match 21) | [[7]](#ref-7) (2024): SECS 0.664 | standard |
| M08 Output | 16 kHz waveform | Waveform or text (slot-filled 3,268) | – | standard |
| M09 Confirmation | Offline | Offline (slot-filled 82) | – | not applicable |
| M10 Correction | Offline | Offline (slot-filled 82) | – | not applicable |
| M11 Reference construction | LRS2, LRS3 references | Corpus references (slot-filled 234) | – | standard |
| M12 Evaluation | 15 listeners, ASR WER | Listener test (pattern match 83) | [[5]](#ref-5) (2026): re-score | standard |
| M13 Device and cost | One A100; no runtime | Hardware and cost (slot-filled 6,075) | – | standard |

## Where the claims outrun the evidence

- "The first attempt to jointly train the vocoder for the multi-speaker lip-to-speech task" (§I): see M06 [[2]](#ref-2), [[3]](#ref-3).
- §V-A calls voice similarity best on LRS3 and equal to DiffV2S on LRS2; Tables I–II show the reverse (0.63 against 0.58 on LRS2, 0.63 each on LRS3).
- "State-of-the-art performance in terms of speech quality" (§VI) excludes LipVoicer; the authors concede higher WER than Lip2Speech Unit (§V-B).
- DDSP gets ground-truth F0 in training, predicted F0 at inference (§IV-D), an unmeasured gap.

## What the field needs next

- M06: a factorial LRS3 ablation (joint or staged vocoder, with or without DDSP, same vocoder corpus) over several seeds.
- M07: SECS and WER for one generator with no speaker input, a video-derived and a reference-audio embedding, on unseen speakers.
- M12: one ASR and full test sets, with LipVoicer and V2SFlow.

## Questions for the authors

- Do test speakers appear in training or AV-HuBERT pre-training?
- How many clips enter Tables I–II, including supplied samples?
- Which Auto-AVSR decoding and normalization were used?
- How many runs underlie Table IV?

## Appendix: literature search

- M06, video-to-speech-synthesis (published table, reused). Inclusion rule: studies that synthesize a speech waveform from talking-face or lip video and report the acoustic representation and how it becomes a waveform; enhancement with noisy audio at test, talking-head generation, text-only lip reading and video-to-text-to-speech pipelines excluded; versions count once. Ledger: 7,345 unique studies slot-filled for M06; 165 unique studies pattern match. Usual design: neural vocoder on predicted acoustic features 49; parametric vocoder 41, Griffin-Lim 16 (pattern match, published counts). Read in full: [[6]](#ref-6), [[2]](#ref-2), [[3]](#ref-3). Known-item recall 1.0.
- M06, joint-end-to-end-lip-to-speech-training (new). Inclusion rule: the same 165 studies, classified by whether the waveform generator is trained with the visual-to-acoustic path or is a pre-trained or separately trained vocoder, and by use of a DDSP or harmonic-plus-noise model; a study counts under every design its full text names (upper bound); end-to-end training that stops at mel or units before a separate vocoder is not joint waveform training. Ledger: 165 unique studies pattern match. Pre-trained or separately trained vocoder 15; joint end-to-end waveform generation 11 (designs in [[2]](#ref-2), [[3]](#ref-3) and the target, the rest related-work mentions); DDSP or harmonic-plus-noise 6 (the target, one [concurrent] DDSP study by the same group, four harmonic-plus-noise vocoders of 2008–2015) (pattern match). Read in full: [[2]](#ref-2), [[3]](#ref-3), [[6]](#ref-6). Known-item recall 1.0 (4 seeds).
- M07, reference-speaker-conditioning-at-inference (new). Inclusion rule: the same 165 studies, classified by the speaker information supplied at use time (reference-audio embedding, face- or video-derived embedding, none); training-only or scoring-only embeddings excluded; every named design counts (upper bound). Ledger: 119 unique studies slot-filled for M07; 165 unique studies pattern match. Reference-audio embedding 21, video- or face-derived 16, no speaker embedding stated 2 (the target and [[4]](#ref-4)) (pattern match). Read in full: [[4]](#ref-4), [[3]](#ref-3), [[7]](#ref-7). Known-item recall 1.0.
- M12, video-to-speech-output-evaluation (published table, reused). Inclusion rule: the same video-to-speech population, counting the evaluation protocols its full text names. Ledger: 6,960 unique studies slot-filled for M12; 165 unique studies pattern match. Protocols: listener test 83, unseen speakers 51, ASR WER on output 38; confidence interval or significance 40, reference-free MOS predictor 21 (pattern match, published counts). Read in full: [[7]](#ref-7), [[5]](#ref-5), [[6]](#ref-6). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Liang, Y., Liu, F., Li, A., Li, X., Zheng, C. “NaturalL2S: End-to-End High-quality Multispeaker Lip-to-Speech Synthesis with Differential Digital Signal Processing.” *arXiv preprint*, 2025. doi:[10.48550/arXiv.2502.12002](https://doi.org/10.48550/arXiv.2502.12002). arXiv:[2502.12002](https://arxiv.org/abs/2502.12002). Target. Read as arXiv v1. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/naturall2s-end-to-end-high-quality-multispeaker-lip-to-speech-synthesis-with-differential-digita) [wiki: arxiv-2502.12002](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2502.12002/article.md)
2. <a id="ref-2"></a>Mira, R., Vougioukas, K., Ma, P., Petridis, S., Schuller, B. W., Pantic, M. “End-to-End Video-To-Speech Synthesis using Generative Adversarial Networks.” *IEEE Transactions on Cybernetics*, 2023, 53(6), 3454-3466. arXiv:[2104.13332](https://arxiv.org/abs/2104.13332). Prior; deciding prior for M06 (end-to-end waveform generation on LRW). Read as arXiv version in the wiki. [wiki: arxiv-2104.13332](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2104.13332/article.md)
3. <a id="ref-3"></a>Um, S., Kim, J., Lee, J., Kang, H. “Facetron: A Multi-speaker Face-to-Speech Model based on Cross-Modal Latent Representations.” *arXiv preprint*, 2021. arXiv:[2107.12003](https://arxiv.org/abs/2107.12003). Prior; deciding prior for M06 and M07 (end-to-end face-to-waveform GAN, face-derived speaker features). Read as arXiv v3. [wiki: arxiv-2107.12003](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2107.12003/article.md)
4. <a id="ref-4"></a>Choi, J., Hong, J., Ro, Y. M. “DiffV2S: Diffusion-based Video-to-Speech Synthesis with Vision-guided Speaker Embedding.” *2023 IEEE/CVF International Conference on Computer Vision (ICCV)*, 2023, 6692-6701. doi:[10.1109/ICCV51070.2023.00618](https://doi.org/10.1109/ICCV51070.2023.00618). arXiv:[2308.07787](https://arxiv.org/abs/2308.07787). Prior; baseline of the target; deciding prior for M07 (vision-guided speaker embedding). [wiki: arxiv-2308.07787-diffv2s](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2308.07787-diffv2s/article.md) [wiki: cvf23-choi_diffv2s](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf23-choi_diffv2s/article.md)
5. <a id="ref-5"></a>Liang, Y., Li, A., Yang, K., Yu, G., Liu, F., Dai, L., et al. “SLD-L2S: Hierarchical Subspace Latent Diffusion for High-Fidelity Lip to Speech Synthesis.” *arXiv preprint (AAAI 2026 copyright line)*, 2026. doi:[10.48550/arXiv.2602.11477](https://doi.org/10.48550/arXiv.2602.11477). arXiv:[2602.11477](https://arxiv.org/abs/2602.11477). Same-group follow-up that re-scores the target with AUTO-AVSR (Tables 1-2). Read as arXiv v1. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/sld-l2s-hierarchical-subspace-latent-diffusion-for-high-fidelity-lip-to-speech-synthesis) [wiki: arxiv-2602.11477](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.11477/article.md) [wiki: arxiv-2602.11477-sldl2s](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.11477-sldl2s/article.md)
6. <a id="ref-6"></a>Yemini, Y., Shamsian, A., Bracha, L., Gannot, S., Fetaya, E. “LipVoicer: Generating Speech from Silent Videos Guided by Lip Reading.” *International Conference on Learning Representations (ICLR)*, 2024. arXiv:[2306.03258](https://arxiv.org/abs/2306.03258). Prior; cited by the target but not compared; state of the art for M06 and M12. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lipvoicer-generating-speech-from-silent-videos-guided-by-lip-reading) [wiki: arxiv-2306.03258](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2306.03258/article.md)
7. <a id="ref-7"></a>Choi, J., Kim, J., Li, J., Chung, J. S., Liu, S. “V2SFlow: Video-to-Speech Generation with Speech Decomposition and Rectified Flow.” *arXiv preprint*, 2024. arXiv:[2411.19486](https://arxiv.org/abs/2411.19486). State of the art for M07 (speaker embedding source at equal WER). Read as arXiv v2. [concurrent] [wiki: arxiv-2411.19486](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2411.19486/article.md)
