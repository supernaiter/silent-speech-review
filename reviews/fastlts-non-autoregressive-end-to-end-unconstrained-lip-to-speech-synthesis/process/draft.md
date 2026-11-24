# FastLTS: Non-Autoregressive End-to-End Unconstrained Lip-to-Speech Synthesis

Wang, Y., Zhao, Z. · ACM Multimedia (MM '22) · 2022 · [DOI:10.1145/3503161.3548194](https://doi.org/10.1145/3503161.3548194) · [arXiv:2207.03800](https://arxiv.org/abs/2207.03800)

## Verdict

FastLTS [[1]](#ref-1) changes one component, the decoding path (M06): a parallel acoustic decoder, a GAN generator fed with learned features instead of mel spectrograms, and a spatial-temporal transformer front end. All three are standard: direct waveform generation predates it [[2]](#ref-2), and so does a transformer visual front end for lip reading [[3]](#ref-3). The speedup is real but partly misattributed: 9.14× at the mel level is the non-autoregressive effect, while the 19.76× waveform figure mostly replaces Griffin-Lim with a GAN vocoder (§5.5), and no parallel mel-plus-vocoder system is timed. Evaluation (M12) is behind its own baseline: it drops the STOI/ESTOI that Lip2Wav reported on the same three speakers [[4]](#ref-4), and its Table 1 shows lower intelligibility than Lip2Wav on Chemistry Lectures.

## Against the field, component by component

### M06 Decoding path: parallel decoder, generator on learned features, transformer front end

**Usual approach:** Of 165 video-to-speech studies (pattern match, Appendix), 49 name a neural vocoder on predicted acoustic features and 24 an autoregressive or Tacotron decoder (9 prior). Of 1,342 articulator-video studies, 380 use a 3D-convolution front end (pattern match); FastLTS adds spatial and temporal transformers after a 3D-convolution tokenizer.

**State of the art:** On the same Lip2Wav speakers the [later] SLTS (2023) reaches STOI 0.757 and ESTOI 0.612 on Chemistry Lectures against 0.416 and 0.284 for Lip2Wav (Table 7) [[5]](#ref-5); FastLTS reports no STOI, so its gap is unknown. On GRID its PESQ of 1.939 trails the [concurrent] VCA-GAN at 2.008 [[6]](#ref-6) (Table 4) and the prior end-to-end GAN of Mira et al. at 2.10 on four seen speakers (Table III) [[2]](#ref-2), which Table 4 omits.

Mira et al. already map video to waveform with no intermediate representation or separate vocoder [[2]](#ref-2). On Lip2Wav FastLTS freezes the visual encoder and acoustic module while the generator trains (§4.4), so its generator is a vocoder trained on the model's own features (inference). That is what the Table 2 control lacks: a HiFi-GAN trained on ground-truth spectrograms fed Lip2Wav's over-smoothed predictions, scoring 1.35 quality MOS on Chess Analysis. That shows a train-test mismatch, not a need for end-to-end generation.

Speed is compared only with the autoregressive Lip2Wav, and GlowLTS's 5.337× is quoted from its paper at 30 s (§5.5). Of the 165 studies, 17 report inference speed, 1 prior (Appendix): useful measurement, narrow comparison set.

Of the 1,342 front-end studies, 102 name a transformer visual front end and 7 are prior, VTP among them [[3]](#ref-3), so "first ... for lip-to-speech synthesis and lipreading" (§1) fails for lip reading; among the 165 video-to-speech studies none prior names one (Appendix). No swap against a 3D-CNN front end is reported; the authors claim "comparable performance" (§5.4). Verdict: standard.

### M12 Evaluation: listener ratings without objective intelligibility

**Usual approach:** Of the 165 studies, 83 run a listener test, 56 report STOI or ESTOI (15 prior) and 38 an ASR WER (pattern match, Appendix). FastLTS uses MTurk MOS, plus PESQ on GRID, arguing that STOI penalizes GAN speech (§5.3).

**State of the art:** SLTS (2023, [later]) gives STOI, ESTOI and PESQ for FastLTS's three Lip2Wav speakers [[5]](#ref-5). The [later] RobustL2S rates FastLTS in a small test (ten raters, five samples, Sec. D): below Lip2Wav on intelligibility, above on quality and naturalness (Fig. 3) [[7]](#ref-7).

Lip2Wav reported STOI, ESTOI and PESQ for Chemistry Lectures, Chess Analysis and Hardware Security (Table 4) [[4]](#ref-4); FastLTS uses the same speakers and reports none, so SLTS lists Lip2Wav but not FastLTS (Table 7) [[5]](#ref-5). Its own MOS agrees with RobustL2S: Chemistry Lectures intelligibility is 3.73±0.11 against 3.88±0.10 for Lip2Wav (Table 1). Verdict: behind, against the best comparable work, its own baseline.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Lecture video, GRID read speech | Recorded speech video (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Mel, then waveform GAN losses | Paired-audio targets (slot-filled 31) | – | standard |
| M03 Training and adaptation | Two stages; upstream frozen on Lip2Wav | Training records (slot-filled 1,526) | – | standard |
| M04 Use-time action | Overt speech, audio muted | Silent or overt (slot-filled 5,595) | – | standard |
| M05 Sensors | S3FD face crop, 96x96 | Camera video (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | Parallel decoder, GAN generator, transformer front end | Vocoder on features (pattern match 49) | [[5]](#ref-5) (2023): chem STOI 0.757 | standard |
| M07 Lexicon and LM | None | None (slot-filled 119) | – | standard |
| M08 Output | 16 kHz waveform | Waveform or text (slot-filled 3,268) | – | standard |
| M09 Confirmation | Offline | Offline (slot-filled 82) | – | not applicable |
| M10 Correction | Offline | Offline (slot-filled 82) | – | not applicable |
| M11 Reference construction | Recorded audio; Lip2Wav splits | Corpus references (slot-filled 234) | – | standard |
| M12 Evaluation | MTurk MOS; GRID PESQ | Listener test (pattern match 83) | [[5]](#ref-5) (2023): chem STOI 0.757 | behind |
| M13 Device and cost | Params, batch-1 timing | Hardware and cost (slot-filled 6,075) | – | standard |

## Where the claims outrun the evidence

- Speed (§5.5): timing protocol is not stated, and the "high memory occupancy" of flow models (Abstract) rests on parameter counts, 85.92M against 50.09M (Table 5), not measured memory.
- GRID (§5.1, Table 4): three unnamed speakers, while Lip2Wav and Mira et al. average four [[4]](#ref-4), [[2]](#ref-2); the provenance of the baseline values is not stated, so the ranking is not a same-protocol comparison.
- Ablations (Table 6): CMOS has no dataset, rater count or uncertainty, and the "w/o waveform generator" waveform method is not stated, so its −0.274 quality CMOS may measure vocoder choice.
- Training regime: GRID trains the whole model on sampled windows, Lip2Wav freezes upstream (§4.4), so the corpora test two systems, with no seeds or repeated runs reported.

## What the field needs next

- M06: on the Lip2Wav speakers, a parallel mel decoder with a HiFi-GAN fine-tuned on its own predicted mels against FastLTS, timed on one GPU with real-time factor and peak memory (M13).
- M12: STOI, ESTOI, PESQ and ASR WER on the Lip2Wav test splits.
- M06 front end: a 3D-CNN against transformer swap with the decoder fixed, over several seeds.

## Questions for the authors

- Which GRID speakers and split were used, and were the Table 4 baseline values recomputed?
- How is the waveform produced in the "w/o waveform generator" ablation, and on which data and raters was Table 6 obtained?
- How many utterances per speaker were rated?
- Do the 50.09M parameters include the auxiliary mel layer and discriminators?
- How was inference time measured (warm-up, repetitions, synchronization)?

## Appendix: literature search

- M06, video-to-speech-synthesis (published table, reused). Inclusion rule: studies that synthesize a speech waveform from talking-face or lip video (audio muted at test) and report the acoustic representation and how it becomes a waveform; enhancement with noisy audio at test, talking-head generation, text-only lip reading and video-to-text-to-speech excluded; versions count once. Ledger: 7,345 unique studies slot-filled for M06; 165 unique studies pattern match. Usual design: neural vocoder on predicted acoustic features 49; parametric vocoder 41, Griffin-Lim 16 (pattern match, published counts). Added full-text counts over the 165 (reference lists removed, related-work mentions included, upper bound; prior = first public before 2022-01): autoregressive or Tacotron decoder named 24 (9 prior); non-autoregressive named 8 (0 prior); inference speed reported 17 (1 prior); parameter count reported 21 (7 prior); transformer visual front end 10 (0 prior). Read in full: [[4]](#ref-4), [[2]](#ref-2), [[5]](#ref-5). Known-item recall 1.0.
- M06, articulator-video-spatiotemporal-front-end (published table, reused). Inclusion rule: studies that decode text, speech or acoustic features from articulator video with a learned image front end, classified by how temporal context enters the front end; versions count once. Ledger: 1,342 unique studies pattern match. Usual design: 3D convolution 380 (pattern match). Added: transformer visual front end 102 (7 prior, pattern match). Read in full: [[3]](#ref-3). Known-item recall 1.0.
- M12, video-to-speech-output-evaluation (published table, reused). Inclusion rule: the same 165 video-to-speech studies, counting the evaluation protocols each full text names. Ledger: 6,960 unique studies slot-filled for M12; 165 unique studies pattern match. Protocols: listener test 83, unseen speakers 51, ASR WER on output 38 (published counts); added: STOI or ESTOI 56 (15 prior), PESQ 52 (23 prior) (pattern match). Read in full: [[4]](#ref-4), [[5]](#ref-5), [[7]](#ref-7). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [fastlts-non-autoregressive-end-to-end-unconstrained-lip-to-speech-synthesis.bib](fastlts-non-autoregressive-end-to-end-unconstrained-lip-to-speech-synthesis.bib).

1. <a id="ref-1"></a>Wang, Y., Zhao, Z. “FastLTS: Non-Autoregressive End-to-End Unconstrained Lip-to-Speech Synthesis.” *Proceedings of the 30th ACM International Conference on Multimedia (MM '22)*, 2022. doi:[10.1145/3503161.3548194](https://doi.org/10.1145/3503161.3548194). arXiv:[2207.03800](https://arxiv.org/abs/2207.03800). Target. Read as arXiv v2 (13 Jul 2022). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/fastlts-non-autoregressive-end-to-end-unconstrained-lip-to-speech-synthesis) [wiki: arxiv-2207.03800](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2207.03800/article.md)
2. <a id="ref-2"></a>Mira, R., Vougioukas, K., Ma, P., Petridis, S., Schuller, B. W., Pantic, M. “End-to-End Video-To-Speech Synthesis using Generative Adversarial Networks.” *IEEE Transactions on Cybernetics*, 2023, 53(6), 3454-3466. arXiv:[2104.13332](https://arxiv.org/abs/2104.13332). Prior; deciding prior for M06 (end-to-end waveform generation; GRID PESQ). [wiki: arxiv-2104.13332](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2104.13332/article.md)
3. <a id="ref-3"></a>Prajwal, K. R., Afouras, T., Zisserman, A. “Sub-word Level Lip Reading With Visual Attention.” *Proc. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2022. arXiv:[2110.07603](https://arxiv.org/abs/2110.07603). Prior; deciding prior for the M06 front-end novelty claim. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/sub-word-level-lip-reading-with-visual-attention) [wiki: arxiv-2110.07603](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2110.07603/article.md) [wiki: cvf-prajwal22-subword-vtp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-prajwal22-subword-vtp/article.md) [wiki: cvpr22-prajwal](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvpr22-prajwal/article.md)
4. <a id="ref-4"></a>Prajwal, K. R., Mukhopadhyay, R., Namboodiri, V. P., Jawahar, C. V. “Learning Individual Speaking Styles for Accurate Lip to Speech Synthesis.” *2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2020, 13793-13802. doi:[10.1109/CVPR42600.2020.01381](https://doi.org/10.1109/CVPR42600.2020.01381). arXiv:[2005.08209](https://arxiv.org/abs/2005.08209). Prior; the target's baseline (Lip2Wav); deciding prior for M12. [wiki: arxiv-2005.08209](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2005.08209/article.md) [wiki: cvf-prajwal20-lip2wav](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-prajwal20-lip2wav/article.md)
5. <a id="ref-5"></a>Niu, Z., Mak, B. “On the Audio-visual Synchronization for Lip-to-Speech Synthesis.” *arXiv preprint*, 2023. arXiv:[2303.00502](https://arxiv.org/abs/2303.00502). Later; state of the art on the Lip2Wav speakers (M06, M12). [later] [wiki: arxiv-2303.00502](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2303.00502/article.md) [wiki: cvf-niu23-slts](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-niu23-slts/article.md) [wiki: cvf-niu23-slts-avsync](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-niu23-slts-avsync/article.md)
6. <a id="ref-6"></a>Kim, M., Hong, J., Ro, Y. M. “Lip to Speech Synthesis with Visual Context Attentional GAN.” *arXiv preprint*, 2022. arXiv:[2204.01726](https://arxiv.org/abs/2204.01726). Concurrent; best GRID PESQ in the target's Table 4. [concurrent] [wiki: arxiv-2204.01726](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2204.01726/article.md)
7. <a id="ref-7"></a>Sahipjohn, N., Shah, N., Tambrahalli, V., Gandhi, V. “RobustL2S: Speaker-Specific Lip-to-Speech Synthesis exploiting Self-Supervised Representations.” *arXiv preprint*, 2023. arXiv:[2307.01233](https://arxiv.org/abs/2307.01233). Later; the only later work that rates the target in a listening test (Fig. 3). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/robustl2s-speaker-specific-lip-to-speech-synthesis-exploiting-self-supervised-representations) [wiki: arxiv-2307.01233](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2307.01233/article.md)
