# LipVoicer: Generating Speech from Silent Videos Guided by Lip Reading

Yemini, Y., Shamsian, A., Bracha, L., Gannot, S., Fetaya, E. · ICLR 2024 · 2024 · [arXiv:2306.03258](https://arxiv.org/abs/2306.03258)

## Verdict

LipVoicer [[1]](#ref-1) changes three components: lip-reader text steers synthesis at use time (M07), a CTC recognizer trained on noised mel-spectrograms carries all text supervision (M02), and a video-conditioned diffusion model generates the mel-spectrogram (M06). The M07 change was ahead at publication: no earlier study among 165 video-to-speech papers uses lip-reader text at inference (pattern match, Appendix), the closest design [[2]](#ref-2) is [concurrent], and [later] AUTO-AVSR re-scores still rank it lowest in LRS3 WER [[3]](#ref-3). The words come from the lip reader, not the synthesizer: on LRS3 output WER is 21.4% against the lip reader's 19.1%, 5.4% with ground-truth text, and 86.2% without guidance, worse than the Lip2Speech baseline at 57.4% (Tables 4, 6, 7). No baseline received that text, so "state-of-the-art results" (Sec. 1) pit a 2023 lip reader against text-free synthesizers. M02, M06 and M12 are standard; words are scored only by an ASR from the same work as the lip reader.

## Against the field, component by component

### M07 Use-time information: lip-reader text guidance

**Usual approach:** Of 165 video-to-speech studies (pattern match, Appendix), 15 name predicted or lip-read text and 7 classifier or ASR guidance; earlier hits use text as a training loss or scoring transcript, or run lip-to-text plus TTS as a baseline [[4]](#ref-4). LipVoicer adds the transcript to video-only synthesis through ASR gradients (Eq. 3).

**State of the art:** LipAdapter (2026, [later]) reports 21.2% LRS3 WER against LipVoicer's 21.4%, scored with Whisper-Large [[5]](#ref-5). Under AUTO-AVSR LipVoicer stays lowest: 20.62% against 27.73% [[3]](#ref-3), 22.24% against 23.73% for Watch Your Speech [[6]](#ref-6).

Output WER tracks the lip reader: 19.1% to 21.4% with Ma et al. (2023), 32.3% to 38.1% with Ma et al. (2022), 0% to 5.4% with ground truth (Table 7); the synthesizer adds 2.3 to 5.8 points (inference). Lip2Speech ([concurrent]) uses text only in training losses [[7]](#ref-7); Hegde et al. condition a visual TTS on noisy lip-to-text output but report no WER of the generated speech [[2]](#ref-2). Verdict: ahead at publication (LRS2, LRS3, GRID); [later] text-aware systems follow it.

### M02 Training-only supervision: noise-conditioned CTC recognizer

**Usual approach:** Paired-audio targets (31 of 64 slot-filled studies with an M03 supervision record); 13 of 165 name a CTC loss and 10 an ASR or text loss on the generator (pattern match), as in Lip2Speech [[7]](#ref-7). LipVoicer keeps MelGen text-free and fine-tunes a time-step-aware ASR by CTC on noised mel-spectrograms (App. A.4).

**State of the art:** Watch Your Speech (2026, [later]) trains on ground-truth text without classifier guidance: 23.73% LRS3 WER against LipVoicer's 22.24% [[6]](#ref-6).

Two of 165 name a noise-conditioned recognizer (pattern match, Appendix), LipVoicer among them; the scheme follows Guided-TTS [[8]](#ref-8) (Sec. 4). The ASR is called swappable "without requiring any re-training" (Sec. 4), yet a guiding ASR at 6.1% instead of 3.6% WER raises output WER from 21.4% to 76.3% (Table 11). Verdict: standard.

### M06 Decoder: video-conditioned diffusion

**Usual approach:** Of 165 studies (pattern match, published counts), 54 name adversarial training, 22 a diffusion decoder. MelGen is a 400-step DDPM with classifier-free guidance on face and mouth video (App. A.3).

**State of the art:** V2SFlow (2024, [later]), 28.5% LRS3 WER without text [[9]](#ref-9); DiffV2S is the [concurrent] diffusion design [[10]](#ref-10).

MelGen alone (w2 = 0) scores 86.2% WER at STOI-Net 0.93 and DNSMOS 3.16, against 0.92 and 3.11 with guidance (Table 6): voice, not words. Verdict: standard.

### M12 Evaluation: ASR WER and opinion scores

**Usual approach:** Of 165 studies (pattern match, published counts), 83 name a listener test, 51 unseen speakers and 38 ASR WER on the output. LipVoicer has both, with 16 annotators per sample (Sec. 5.1, Appendix G).

**State of the art:** SLD-L2S (2026, [later]) re-scores LipVoicer at 20.62% LRS3 WER with AUTO-AVSR [[3]](#ref-3).

The evaluation ASR and the lip reader are both Ma et al. (2023) (Sec. 5), so their errors may correlate (inference). Listener intelligibility is a rating (3.44 against 4.38 for ground truth, LRS3, Table 2), not transcription. Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | LRS2, LRS3, GRID overt speech | Recorded speech video (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | CTC on noised mel for guiding ASR | Paired-audio targets (slot-filled 31) | [[6]](#ref-6) (2026): LRS3 WER 23.73% | standard |
| M03 Training and adaptation | One run; weights by listening | Training records (slot-filled 1,526) | – | standard |
| M04 Use-time action | Overt speech, audio removed | Silent or overt (slot-filled 5,595) | – | standard |
| M05 Sensors | Face frame, 88x88 mouth crop | Camera video (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | 400-step DDPM, CFG on video | Adversarial training (pattern match 54) | [[9]](#ref-9) (2024): LRS3 WER 28.5% | standard |
| M07 Lexicon and LM | Lip-reader text via ASR guidance | Video only, no text (pattern match 150) | [[5]](#ref-5) (2026): LRS3 WER 21.2% | ahead |
| M08 Output | 16 kHz waveform, DiffWave | Waveform or text (slot-filled 3,268) | – | standard |
| M09 Confirmation | Offline | Offline (slot-filled 82) | – | not applicable |
| M10 Correction | Offline | Offline (slot-filled 82) | – | not applicable |
| M11 Reference construction | Corpus transcripts and splits | Corpus references (slot-filled 234) | – | standard |
| M12 Evaluation | ASR WER, 16 raters per sample | Listener test (pattern match 83) | [[3]](#ref-3) (2026): LipVoicer re-scored 20.62% | standard |
| M13 Device and cost | Offline; misuse named | Hardware and cost (slot-filled 6,075) | – | standard |

## Where the claims outrun the evidence

- "State-of-the-art results" (Sec. 1): no baseline gets the lip reader's text, and the lip-to-text plus TTS control of [[4]](#ref-4) is not run.
- "More natural and synchronized" (Abstract): MelGen without guidance is sometimes more natural, and wrong text causes synchronization lapses (Appendix E.5).
- ReVISE: 33.2% against 33.9%, under an ASR measured at 6.4% instead of its reported 5.6% (Sec. 5) is not evidence either way.
- Guidance weights come from grid search and listening tests on unstated data (Appendix C); the released ASR config evaluates on the LRS3 test split.

## What the field needs next

- M07: the same lip-reader text into a duration-controlled TTS, scored by listener transcription.
- M07/M12: WER against the lip-reader text and the ground truth, by an ASR unrelated to the lip reader.
- M02: guiding ASRs of graded accuracy, with and without noise fine-tuning, over seeds.

## Questions for the authors

- Which data and listeners selected w1, w2 and t_ASR (App. C)?
- What do the ± values denote, and how many seeds stand behind each table?
- Do LRS2 or LRS3 test speakers appear in any training set?

## Appendix: literature search

- M07, lip-reader-text-guidance-for-video-to-speech (new). Inclusion rule: the 165-study video-to-speech population (population of the published M06 one-to-many decoder table), classified from the full text (reference list removed) by use of text predicted from the video at inference, classifier or ASR guidance of a sampler, and a named lip-reader-to-TTS cascade; every named design counts (upper bound, related-work mentions included); text used only as a training loss or scoring transcript is not use-time text. Ledger: 119 unique studies slot-filled for M07; 165 unique studies pattern match. Lip-reader-to-TTS cascade named 20, predicted or lip-read text 15, classifier or ASR guidance 7 (pattern match); every text-use hit before 2023-06 is a training loss, a WER transcript or a cascade baseline. Read in full: [[4]](#ref-4), [[7]](#ref-7), [[2]](#ref-2), [[5]](#ref-5), [[3]](#ref-3), [[6]](#ref-6). Known-item recall 1.0 (4 seeds).
- M02, text-supervision-in-video-to-speech-training (new). Inclusion rule: the same 165 studies, classified by training-only text supervision: a CTC or ASR/text loss on the generator or its features, and a recognizer trained on noised or time-step-conditioned spectrograms to guide sampling; text at inference is M07; full-text pattern counts, upper bound. Ledger: 64 unique studies with an M03 supervision record, paired audio 31 (slot-filled); CTC loss 13, ASR or text loss 10, noise-conditioned recognizer 2 (pattern match). Read in full: [[7]](#ref-7), [[6]](#ref-6). Known-item recall 1.0 (3 seeds).
- M06, video-to-speech-one-to-many-decoder (published table, reused). Inclusion rule: studies that synthesize a speech waveform from talking-face or lip video, audio muted at test, classified from the full text by how the acoustic decoder handles the one-to-many mapping; enhancement with noisy audio at test, talking-head generation and video-to-text-to-TTS pipelines excluded; every named design counts (upper bound); versions once. Ledger: 7,345 unique studies slot-filled for M06; 165 unique studies pattern match. Adversarial training 54, speech-unit conditioning 44, diffusion decoder 22, flow decoder 19, pitch or energy predictor 9 (pattern match, published counts). Read in full: [[9]](#ref-9), [[10]](#ref-10). Known-item recall 1.0.
- M12, video-to-speech-output-evaluation (published table, reused). Inclusion rule: the same video-to-speech population, counting the evaluation protocols its full text names (upper bound; versions once). Ledger: 6,960 unique studies slot-filled for M12; 165 unique studies pattern match. Listener test 83, unseen speakers 51, ASR WER on output 38 (pattern match, published counts). Read in full: [[3]](#ref-3), [[9]](#ref-9). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [lipvoicer-generating-speech-from-silent-videos-guided-by-lip-reading.bib](lipvoicer-generating-speech-from-silent-videos-guided-by-lip-reading.bib).

1. <a id="ref-1"></a>Yemini, Y., Shamsian, A., Bracha, L., Gannot, S., Fetaya, E. “LipVoicer: Generating Speech from Silent Videos Guided by Lip Reading.” *The Twelfth International Conference on Learning Representations (ICLR 2024)*, 2024. arXiv:[2306.03258](https://arxiv.org/abs/2306.03258). Target. Read as arXiv v2 (28 Mar 2024), the ICLR 2024 version. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lipvoicer-generating-speech-from-silent-videos-guided-by-lip-reading) [wiki: arxiv-2306.03258](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2306.03258/article.md)
2. <a id="ref-2"></a>Hegde, S., Mukhopadhyay, R., Jawahar, C. V., Namboodiri, V. “Towards Accurate Lip-to-Speech Synthesis in-the-Wild.” *Proceedings of the 31st ACM International Conference on Multimedia (MM '23)*, 2023. doi:[10.1145/3581783.3611787](https://doi.org/10.1145/3581783.3611787). arXiv:[2403.01087](https://arxiv.org/abs/2403.01087). [concurrent]; conditions synthesis on noisy lip-to-text output and the lip video. [concurrent] [wiki: arxiv-2403.01087](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2403.01087/article.md)
3. <a id="ref-3"></a>Liang, Y., Li, A., Yang, K., Yu, G., Liu, F., Dai, L., et al. “SLD-L2S: Hierarchical Subspace Latent Diffusion for High-Fidelity Lip to Speech Synthesis.” *arXiv preprint (AAAI 2026 copyright line)*, 2026. doi:[10.48550/arXiv.2602.11477](https://doi.org/10.48550/arXiv.2602.11477). arXiv:[2602.11477](https://arxiv.org/abs/2602.11477). [later]; re-scores the target with AUTO-AVSR. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/sld-l2s-hierarchical-subspace-latent-diffusion-for-high-fidelity-lip-to-speech-synthesis) [wiki: arxiv-2602.11477](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.11477/article.md) [wiki: arxiv-2602.11477-sldl2s](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.11477-sldl2s/article.md)
4. <a id="ref-4"></a>Hegde, S. B., Prajwal, K. R., Mukhopadhyay, R., Namboodiri, V. P., Jawahar, C. V. “Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild.” *Proceedings of the 30th ACM International Conference on Multimedia (MM '22)*, 2022. arXiv:[2209.00642](https://arxiv.org/abs/2209.00642). Prior; deciding prior for M07 (lip-to-text plus TTS named as an alternative, not used to guide synthesis). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lip-to-speech-synthesis-for-arbitrary-speakers-in-the-wild) [wiki: arxiv-2209.00642](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2209.00642/article.md)
5. <a id="ref-5"></a>Ghosh, S., Jawahar, C. V., Namboodiri, V. “LipAdapter: Text-to-Video Alignment is All You Need for Lip-to-Speech.” *Proc. Interspeech 2026*, 2026, 3548. doi:[10.21437/Interspeech.2026-518](https://doi.org/10.21437/Interspeech.2026-518). [later]; predicted text aligned to video into a pretrained TTS; state of the art for M07. [later] [wiki: isca-ghosh26b-lipadapt](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-ghosh26b-lipadapt/article.md) [wiki: isca-ghosh26b_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-ghosh26b_interspeech/article.md)
6. <a id="ref-6"></a>Lee, G., Oh, Y., Han, Y. “Watch Your Speech: Text-aware Video-to-Speech Synthesis with Textual Conditioning.” *arXiv preprint*, 2026. arXiv:[2610.01012](https://arxiv.org/abs/2610.01012). [later]; text conditioning from training onward, no classifier guidance. [later] [wiki: arxiv-2610.01012-wys](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2610.01012-wys/article.md) [wiki: arxiv-2610.01012](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2610.01012/article.md)
7. <a id="ref-7"></a>Kim, M., Hong, J., Ro, Y. M. “Lip-to-Speech Synthesis in the Wild with Multi-task Learning.” *2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2023. arXiv:[2302.08841](https://arxiv.org/abs/2302.08841). [concurrent]; baseline of the target; text used as a training loss only. [concurrent] [wiki: arxiv-2302.08841](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2302.08841/article.md)
8. <a id="ref-8"></a>Kim, H., Kim, S., Yoon, S. “Guided-TTS: A Diffusion Model for Text-to-Speech via Classifier Guidance.” *Proceedings of the 39th International Conference on Machine Learning (ICML)*, 2022. arXiv:[2111.11755](https://arxiv.org/abs/2111.11755). Prior; cited by the target as the source of its guidance scheme; not in the wiki (text-to-speech).
9. <a id="ref-9"></a>Choi, J., Kim, J., Li, J., Chung, J. S., Liu, S. “V2SFlow: Video-to-Speech Generation with Speech Decomposition and Rectified Flow.” *arXiv preprint*, 2024. arXiv:[2411.19486](https://arxiv.org/abs/2411.19486). [later]; best text-free LRS3 WER in the reused tables. [later] [wiki: arxiv-2411.19486](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2411.19486/article.md)
10. <a id="ref-10"></a>Choi, J., Hong, J., Ro, Y. M. “DiffV2S: Diffusion-based Video-to-Speech Synthesis with Vision-guided Speaker Embedding.” *2023 IEEE/CVF International Conference on Computer Vision (ICCV)*, 2023, 6692-6701. doi:[10.1109/ICCV51070.2023.00618](https://doi.org/10.1109/ICCV51070.2023.00618). arXiv:[2308.07787](https://arxiv.org/abs/2308.07787). [concurrent] diffusion video-to-speech. [concurrent] [wiki: arxiv-2308.07787-diffv2s](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2308.07787-diffv2s/article.md) [wiki: cvf23-choi_diffv2s](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cvf23-choi_diffv2s/article.md)
