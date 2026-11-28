# Learning Individual Speaking Styles for Accurate Lip to Speech Synthesis

K R Prajwal, Rudrabha Mukhopadhyay, Vinay P. Namboodiri, C V Jawahar. CVPR 2020. [doi:10.1109/CVPR42600.2020.01381](https://doi.org/10.1109/CVPR42600.2020.01381) · [arXiv:2005.08209](https://arxiv.org/abs/2005.08209)

## Verdict

Lip2Wav [[1]](#ref-1) changes the training corpus (M03) and the decoder (M06). The corpus is ahead: 0 of the 10 prior video-to-speech synthesizers trained on unconstrained speech or on more than about 1 h per speaker (Appendix), and its five speakers became the single-speaker benchmark. The decoder is standard: it departs from 9 of 10 priors, but LipSound [[2]](#ref-2) had already mapped whole 3-s lip clips to mel spectrograms with an attention decoder, teacher forcing and Griffin-Lim, and the paper cites it only as lip-to-text work (§2.2). The evaluation (M12) is standard, and two GRID WERs in Table 2 equal values measured with another recognizer [[3]](#ref-3). Gains over baselines confound decoder, encoder, context and data; each ablation is one speaker, one run.

## Against the field, component by component

### M03 Training data: per-speaker hours of natural speech

**Usual approach:** 7 of the 10 prior synthesizers (pattern match, screened, Appendix) train speaker-dependent GRID models, about 0.8 h per speaker (the target's Table 1); 3 use OuluVS2. Lip2Wav has about 20 h and more than 5,000 words per speaker.

**State of the art:** RobustL2S (2023) [[4]](#ref-4) [later] keeps the official split and one model per speaker but adds a pre-trained AV-HuBERT fine-tuned on Whisper transcripts: STOI 0.583 against 0.416 on Chemistry Lectures (Table IV).

Ahead under the rule: 0 of 10 priors share the design (Appendix); the deciding priors LipSound, Vougioukas et al. [[3]](#ref-3), Lip2AudSpec [[5]](#ref-5) and Ephrat et al. [[6]](#ref-6) were read and stay on GRID or TCD-TIMIT; 5 speakers are trained independently. Their claim to be "the first to study this problem in a large vocabulary setting" (§2.1) holds. The hours are untested: no model is trained on part of a speaker's data. The later gain comes from external pre-training, not from more video per speaker.

### M06 Decoder: autoregressive attention over 3-s windows

**Usual approach:** 9 of the 10 prior synthesizers (pattern match, screened, Appendix) regress features non-autoregressively from frame windows or a recurrent encoder, e.g. 9 frames [[6]](#ref-6) or 7 frames plus a GRU [[3]](#ref-3).

**State of the art:** RobustL2S (2023) [[4]](#ref-4) [later] isolates the sequence-mapping step: a non-autoregressive mapping between self-supervised features raises Chemistry Lectures STOI from 0.50 to 0.583 (Table I).

The authors say Ephrat et al. and the GAN-based work "do not make use of the well-studied sequence-to-sequence paradigm" (§2.1), true of those two. LipSound did: Tacotron2-inspired, whole 3-s GRID videos, teacher forcing, Griffin-Lim. The claim that previous works "use only about 0.3 -0.5 seconds of context" (§7.1) fits frame-window models, not LipSound or Lip2AudSpec, which feeds 3-s clips to a CNN + LSTM [[5]](#ref-5). Lip2Wav adds teacher-forcing decay (Table 9: STOI 0.221 always forced, 0.446 decayed); 3D-CNN encoders were already used [[3]](#ref-3). The context ablation (Table 8: 0.264 at 0.5 s, 0.446 at 3 s) is one speaker, one run. The authors report homophenes as the dominant error (§6.3.1) and neural vocoders failing on their mels (§5.3). Standard.

### M12 Evaluation: baseline rows and single runs

**Usual approach:** 6 of the 10 prior synthesizers run a human listener test and 0 of 10 report a run or seed spread (pattern match, hits inspected, Appendix).

**State of the art:** Niu and Mak (2023) [[7]](#ref-7) [later] show Lip2Wav audio and video are out of sync and score with alignment, Whisper-transcript WER (24.69%) and MOS with 95% intervals; one Chemistry Lectures output gives STOI 0.215 vanilla and 0.760 aligned (Table 2).

Table 2's GAN-based and Lip2AudSpec WERs (26.64%, 32.51%) equal those of Vougioukas et al. (26.6%, 32.5%), measured with an ASR trained on GRID (4% on ground truth; §3.2 of [[3]](#ref-3)), while the paper names the Google API for its WERs (§6). The STOI values of the same rows differ from that source (0.564 against 0.518; 0.513 against 0.446), and Vid2Speech reported only human transcription by MTurk workers [[8]](#ref-8). Copied and re-run values are mixed, unlabelled. Standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Voiced face video | Voiced speech | – | standard |
| M02 Training-only supervision | Paired mel target, no text | Paired audio target | – | standard |
| M03 Training and adaptation | One model per speaker, about 20 h of natural video, 5 speakers | GRID, about 0.8 h/speaker (7 of 10 prior) (pattern match 7) | [[4]](#ref-4) STOI 0.583 vs 0.416, one speaker | ahead |
| M04 Use-time action | Silent face video | Voiced video, audio removed | – | standard |
| M05 Sensors | Face crop 48x48 | Face or mouth crop | – | standard |
| M06 Processing and decoding | 3D-CNN + attention mel decoder, 3-s windows | Non-autoregressive regression (9 of 10 prior) (pattern match 9) | [[4]](#ref-4) seq2seq step 0.50 to 0.583 STOI | standard |
| M07 Lexicon and LM | None | None | – | standard |
| M08 Output | Mel, Griffin-Lim | Spectral features + vocoder | – | standard |
| M09 Confirmation | None (offline) | Mostly absent | – | not applicable |
| M10 Correction | None (offline) | Mostly absent | – | not applicable |
| M11 Reference construction | Video-disjoint splits | Held-out utterances | – | standard |
| M12 Evaluation | Objective metrics, ASR WER, MOS; one run | Listener test, no spread (6 of 10 prior) (pattern match 6) | [[7]](#ref-7) a-STOI 0.760 vs 0.215 vanilla | standard |
| M13 Device and cost | Offline GPU | Offline GPU | – | standard |

## Where the claims outrun the evidence

- "Almost 4× more intelligible" (Table 4 caption) holds for ESTOI against Ephrat et al. (mean ratio 3.76 over five speakers); against the GAN baseline the STOI ratios are 1.78 to 2.17 (inference).
- The claim that no previous lip-to-speech work tackles the multi-speaker case (§6.4) ignores the unseen-speaker test of Vougioukas et al. (WER 40.5%, Table 4 of [[3]](#ref-3)) and Lip2AudSpec's joint four-speaker training [[5]](#ref-5).
- Table 7 sets ASR WER on generated LRW words (34.2%) against a classifier's error (38.8%).
- Manual transcripts plus TTS beat Lip2Wav on intelligibility (3.86 against 3.04, Table 6); the authors' case is naturalness (3.63 against 3.15), from 15 raters with no interval.
- The data ratio is 800 times in §1, 80 times in the contributions.

## What the field needs next

- M03: one speaker trained on 1, 5 and 20 h, with and without external pre-training, one test split.
- M06: LipSound-style and Lip2Wav decoders on one encoder, data and vocoder, three seeds per speaker.
- M12: time-aligned metrics [[7]](#ref-7) and all baseline rows re-scored with one recognizer.

## Questions for the authors

- Which rows of Tables 2 and 3 were retrained, and which ASR produced each WER?
- Which GRID speakers form the mean, given S1 to S4 in Ephrat et al. and S1, S2, S4, S29 in Vougioukas et al.?
- Which validation metric selected the checkpoint, and are the 90/5/5 splits by duration or by video?
- How many annotators labelled the 50 files of Table 5?

## Appendix: literature search

Population for all three topics: video-only talking-face or lip video to speech waveform synthesizers, screened from the 165-study ledger pattern of the published M06 video-to-speech table by title and full text; reviews, datasets, enhancement and separation with audio at test, tongue-ultrasound, talking-head and off-task papers removed; versions once. Prior means first public before 2019-11, [concurrent] 2019-11 to 2020-11. Prior synthesizers: 10 (Le Cornu and Milner 2015 and 2017, Vid2Speech, Ephrat et al. 2017, Lip2AudSpec, Kumar et al. 2018, Lipper, Vougioukas et al. 2019, Hush-Hush Speak, LipSound); [concurrent]: 1 (Michelsanti et al. 2020, non-autoregressive). Full-text step (lip-to-speech or video-to-speech wording, reference lists removed, index year 2020 or earlier): 21 folders, 0 new synthesizers. Same-group earlier lip-to-speech systems: 0. The target cites LipSound only among lip-to-text works and does not cite Le Cornu and Milner 2015, Kumar et al. 2018 or Hush-Hush Speak.

- M03, training-data-scale-video-to-speech. Inclusion rule: the 165-study video-to-speech population classified by the training corpora and scale it names (published rule kept), screened as above. Ledger counts: 1,526 unique studies slot-filled for M03; 165 unique studies pattern match (all years). Prior designs: GRID 7, OuluVS2 3, TCD-TIMIT 1, unconstrained corpus 0, more than about 1 h per speaker 0. Later studies reusing the Lip2Wav speakers: 5. Read in full: [[2]](#ref-2), [[3]](#ref-3), [[5]](#ref-5), [[6]](#ref-6) (prior), [[4]](#ref-4) (state of the art); the published table also lists LipSound2 [[9]](#ref-9) [later]. Known-item recall 1.0.
- M06, video-to-speech-synthesis. Inclusion rule: studies that synthesize a speech waveform from talking-face or lip video and report the acoustic representation and waveform generation (published rule kept), screened as above and classified by decoder. Ledger counts: 7,345 unique studies slot-filled for M06; 165 unique studies pattern match (all years). Prior designs: non-autoregressive regression 9, autoregressive attention decoder 1 [[2]](#ref-2); whole 3-s clip input 2. Read in full: [[2]](#ref-2), [[3]](#ref-3), [[6]](#ref-6), [[5]](#ref-5), [[8]](#ref-8) (prior), [[4]](#ref-4) (state of the art). Known-item recall 1.0.
- M12, video-to-speech-output-evaluation. Inclusion rule: the same population compared by evaluation protocol (published rule kept), screened as above. Ledger counts: 6,960 unique studies slot-filled for M12; 165 unique studies pattern match (all years). Prior designs: listener test 6, PESQ 8, STOI or ESTOI 3, ASR WER on output 2, unseen-speaker test 3, run or seed spread 0, listener-score spread 1. Read in full: [[3]](#ref-3), [[8]](#ref-8) (prior), [[7]](#ref-7) (state of the art). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [learning-individual-speaking-styles-for-accurate-lip-to-speech-synthesis.bib](learning-individual-speaking-styles-for-accurate-lip-to-speech-synthesis.bib).

1. <a id="ref-1"></a>Prajwal, K. R., Mukhopadhyay, R., Namboodiri, V. P., Jawahar, C. V. “Learning Individual Speaking Styles for Accurate Lip to Speech Synthesis.” *2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2020, 13793-13802. doi:[10.1109/CVPR42600.2020.01381](https://doi.org/10.1109/CVPR42600.2020.01381). arXiv:[2005.08209](https://arxiv.org/abs/2005.08209). [wiki: cvf-prajwal20-lip2wav](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-prajwal20-lip2wav/article.md) [wiki: arxiv-2005.08209](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2005.08209/article.md)
2. <a id="ref-2"></a>Qu, L., Weber, C., Wermter, S. “LipSound: Neural Mel-spectrogram Reconstruction for Lip Reading.” *Interspeech*, 2019. doi:[10.21437/Interspeech.2019-1393](https://doi.org/10.21437/Interspeech.2019-1393). [wiki: isca-qu19-lipsound](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-qu19-lipsound/article.md) [wiki: isca-qu19_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-qu19_interspeech/article.md)
3. <a id="ref-3"></a>Vougioukas, K., Ma, P., Petridis, S., Pantic, M. “Video-Driven Speech Reconstruction using Generative Adversarial Networks.” *Proc. Interspeech 2019*, 2019, 4125–4129. doi:[10.21437/Interspeech.2019-1445](https://doi.org/10.21437/Interspeech.2019-1445). arXiv:[1906.06301](https://arxiv.org/abs/1906.06301). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/video-driven-speech-reconstruction-using-generative-adversarial-networks) [wiki: isca-vougioukas19_ganv2s](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-vougioukas19_ganv2s/article.md)
4. <a id="ref-4"></a>Sahipjohn, N., Shah, N., Tambrahalli, V., Gandhi, V. “RobustL2S: Speaker-Specific Lip-to-Speech Synthesis exploiting Self-Supervised Representations.” *arXiv preprint*, 2023. arXiv:[2307.01233](https://arxiv.org/abs/2307.01233). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/robustl2s-speaker-specific-lip-to-speech-synthesis-exploiting-self-supervised-representations) [wiki: arxiv-2307.01233](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2307.01233/article.md)
5. <a id="ref-5"></a>Akbari, H., Arora, H., Cao, L., Mesgarani, N. “Lip2AudSpec: Speech reconstruction from silent lip movements video.” *2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2018, 2516-2520. doi:[10.1109/ICASSP.2018.8461856](https://doi.org/10.1109/ICASSP.2018.8461856). arXiv:[1710.09798](https://arxiv.org/abs/1710.09798). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lip2audspec-speech-reconstruction-from-silent-lip-movements-video) [wiki: arxiv-1710.09798](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1710.09798/article.md)
6. <a id="ref-6"></a>Ephrat, A., Halperin, T., Peleg, S. “Improved Speech Reconstruction from Silent Video.” *2017 IEEE International Conference on Computer Vision Workshops (ICCVW)*, 2017, 455-462. doi:[10.1109/ICCVW.2017.61](https://doi.org/10.1109/ICCVW.2017.61). arXiv:[1708.01204](https://arxiv.org/abs/1708.01204). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/improved-speech-reconstruction-from-silent-video) [wiki: arxiv-1708.01204](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1708.01204/article.md)
7. <a id="ref-7"></a>Niu, Z., Mak, B. “On the Audio-visual Synchronization for Lip-to-Speech Synthesis.” *Proc. IEEE/CVF International Conference on Computer Vision (ICCV)*, 2023. arXiv:[2303.00502](https://arxiv.org/abs/2303.00502). [later] [wiki: arxiv-2303.00502](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2303.00502/article.md) [wiki: cvf-niu23-slts](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-niu23-slts/article.md) [wiki: cvf-niu23-slts-avsync](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf-niu23-slts-avsync/article.md)
8. <a id="ref-8"></a>Ephrat, A., Peleg, S. “Vid2speech: Speech Reconstruction from Silent Video.” *2017 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2017, 5095-5099. doi:[10.1109/ICASSP.2017.7953127](https://doi.org/10.1109/ICASSP.2017.7953127). arXiv:[1701.00495](https://arxiv.org/abs/1701.00495). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/vid2speech-speech-reconstruction-from-silent-video) [wiki: arxiv-1701.00495](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1701.00495/article.md)
9. <a id="ref-9"></a>Qu, L., Weber, C., Wermter, S. “LipSound2: Self-Supervised Pre-Training for Lip-to-Speech Reconstruction and Lip Reading.” *IEEE Transactions on Neural Networks and Learning Systems*, 2022. doi:[10.1109/TNNLS.2022.3191677](https://doi.org/10.1109/TNNLS.2022.3191677). arXiv:[2112.04748](https://arxiv.org/abs/2112.04748). [later] [wiki: arxiv-2112.04748](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2112.04748/article.md) [wiki: doi-10.1109-tnnls.2022.3191677](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tnnls.2022.3191677/article.md)
