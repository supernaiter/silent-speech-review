# Lipper: Synthesizing Thy Speech using Multi-View Lipreading

Yaman Kumar, Rohit Jain, Khwaja Mohd. Salik, Rajiv Ratn Shah, Yifang Yin, Roger Zimmermann. Proceedings of the AAAI Conference on Artificial Intelligence 33 (AAAI-19), pp. 2588–2595, 2019. [doi:10.1609/aaai.v33i01.33012588](https://doi.org/10.1609/aaai.v33i01.33012588) · [arXiv:1907.01367](https://arxiv.org/abs/1907.01367)

## Verdict

The paper [[1]](#ref-1) changes the camera input (M05), up to five OuluVS2 views chosen by a pose classifier, and the regressor (M06), a spatio-temporal CNN with BiGRU predicting LPC/LSP features. Both are standard: multi-view speech reconstruction on OuluVS2 appears in the authors' 2018 system [[2]](#ref-2) [concurrent], and the LPC/LSP target is the Vid2speech route [[3]](#ref-3). The evaluation (M12) is behind: PESQ plus a four-alternative phrase choice, where four earlier systems measured intelligibility directly. The best view combination is chosen on the speaker-dependent test results it is reported on, and on two held-out speakers the three-view gain over frontal falls from +15.6% to +2.1% and +5.7% PESQ (Tables 4, 6, 10; inference). The conclusion's real-time and speaker-independence claims are unsupported.

## Against the field, component by component

### M05 Sensors: number and placement of camera views

**Usual approach:** One camera: 693 of 787 unique lip-reading and video-to-speech studies name no multi-view input (pattern match, Appendix); of 165 video-to-speech studies, 20 name multi-view input. The paper itself credits multi-view reconstruction to the authors' 2018 work (Related Work) [[2]](#ref-2), and multi-view lip reading to text found frontal plus profile best [[4]](#ref-4).

**State of the art:** This paper (2019) holds the highest multi-view PESQ on OuluVS2 in the topic table, 2.315 for 0°+45°+60° against 2.002 frontal, speaker-dependent (Tables 4, 6). Hush-Hush Speak [[5]](#ref-5) [later], with a stated 85:10:5 split, reaches 1.964 with the same views against 1.920 frontal: +2.3% (inference).

The chosen triple does not transfer: on held-out speakers 38 and 39, 0°+45° (2.03, 1.85) matches or beats 0°+45°+60° (1.94, 1.86) (Table 10), and all five views give 2.086, below the triple (Table 8). The deciding prior ran 10 repetitions with significance tests [[4]](#ref-4); this paper reports no repeats (Tables 4–10). Verdict: standard.

### M06 Processing: regression to LPC/LSP features

**Usual approach:** Of 165 video-to-speech studies (pattern match, Appendix), 49 name a neural vocoder and 41 a parametric vocoder. The paper keeps the parametric route, LPC order 24 with LSP encoding, and presents regression as its departure from lip reading (Abstract), though speech regression from video predates it [[3]](#ref-3) [[6]](#ref-6).

**State of the art:** On GRID with four seen speakers, a later comparison table gives the lowest ASR WER, 4.07% at PESQ 1.76, to an end-to-end WGAN (2022) generating raw waveform [[7]](#ref-7) [later]. The paper reports no WER, so the gap is unknown. Verdict: standard for 2019.

### M12 Evaluation: quality metric and closed-set listening

**Usual approach:** 83 of 165 video-to-speech studies name a listener or opinion test, 51 an unseen-speaker test, 38 ASR WER on the output (pattern match, Appendix). The paper's listener test is phrase-level: one correct and three random options, chance 25%, giving 80.25% (Table 12). PESQ rates quality, and the authors found it misjudged noisy samples (Sec. User-Study) [[1]](#ref-1).

**State of the art:** On 33 unseen GRID speakers, the same table gives 16.05% WER to an end-to-end WGAN (2022) [[7]](#ref-7) [later]; the paper's unseen-speaker test has two speakers (Table 10).

Four earlier systems measured intelligibility directly: listeners classify each word among the GRID options [[3]](#ref-3); listeners transcribe and rate naturalness 1–5 [[8]](#ref-8); STOI and ESTOI [[9]](#ref-9); listener word accuracy 85% [[6]](#ref-6). None of these measures appears in the paper (Tables 4–12; Appendix). Verdict: behind, against the best comparable work, Lip2AudSpec [[8]](#ref-8).

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | None; voiced OuluVS2 speech | Voiced speech corpora (slot-filled 4,015) | – | standard |
| M02 Training-only supervision | Paired voiced audio (LPC/LSP targets) | Paired audio (slot-filled 31) | – | standard |
| M03 Training and adaptation | Per-speaker training (2 train, 1 test phrase); 2 held-out speakers | Per-corpus training (slot-filled 1,608) | – | standard |
| M04 Use-time action | Voiced speech, video alone at test | Voiced articulation (slot-filled 6,538) | – | standard |
| M05 Sensors | Up to five OuluVS2 views, pose classifier picks the combination | One camera view (693 of 787) (pattern match 787) | 0°+45°+60°: 2.315 PESQ, speaker-dependent (this paper); 1.964 held-out [[5]](#ref-5) | standard |
| M06 Processing and decoding | STCNN+BiGRU to LPC (order 24)/LSP features | Neural vocoder (49); parametric vocoder 41 (pattern match 165) | 4.07% WER, GRID seen speakers (2022 WGAN row) [[7]](#ref-7) | standard |
| M07 Lexicon and LM | No lexicon or language model | No language model (slot-filled 120) | – | not applicable |
| M08 Output | Waveform from LPC/LSP; ancillary 10-class text | Speech waveform (slot-filled 3,760) | – | standard |
| M09 Confirmation | None (offline) | None (slot-filled 82) | – | not applicable |
| M10 Correction | None (offline) | None (slot-filled 82) | – | not applicable |
| M11 Reference construction | Recorded OuluVS2 audio as PESQ reference | Original audio as reference (slot-filled 239) | – | standard |
| M12 Evaluation | PESQ; 4-alternative phrase choice; 2 unseen speakers | Listener or opinion test (83) (pattern match 165) | 16.05% WER, GRID unseen speakers (2022 WGAN row) [[7]](#ref-7) | behind |
| M13 Device and cost | Controlled setting; delay hardware and timing boundaries not stated | Offline (slot-filled 6,721) | – | not reported |

## Where the claims outrun the evidence

- **Selection on the test set.** No validation set is named; the decision logic picks view combinations from the speaker-dependent results, reused for OOV and held-out tests [[1]](#ref-1). The 2.315 is optimistic (inference).
- **Speaker independence.** Claimed in the conclusion, conceded as weak in future work [[1]](#ref-1); two speakers, one per gender, cannot separate speaker from gender (Table 10).
- **Real time.** Table 11 gives 0.169 s for all ten phrases, against 0.94–1.95 s for a phrase classifier [[4]](#ref-4) whose delay grows with phrase length. A delay constant over length is per-window, not end-to-end (inference); hardware is not stated.
- **Text accuracy.** 97.0% against 95.6% uses a random split across speakers; the speaker split gives 78.5% (Table 2), as the authors concede.
- **Language independence.** Shown only by speaker-dependent demo videos in Hindi, English and Chinese [[1]](#ref-1).

## What the field needs next

- M05: view combinations chosen on a validation split, tested on held-out speakers, with a duplicated-view control.
- M12: ASR WER, STOI/ESTOI and open listener transcription on a speaker-disjoint OuluVS2 split.
- M06: the multi-view front end with a neural vocoder.

## Questions for the authors

- Which phrases form the speaker-dependent split?
- Was the Ephrat and Peleg baseline in Table 4 retrained on your split?
- What hardware and end points define the 0.169 s delay?
- How many judgments make up the user study, and how was variance computed?

## Appendix: literature search

- **M05, multi-view camera input.** Inclusion rule: video-based speech decoding (lip reading, VSR, video-to-speech) with an optical camera in the ledger; full-text counts of multi-view input, non-frontal pose and OuluVS2 use (upper bound, related-work mentions included); talking-head and biometric studies excluded; versions counted once. Slot-filled 7,329 unique studies; pattern match 787 unique studies. Usual design: one camera view, 693 (pattern match); multi-view input 94, non-frontal pose 128, OuluVS2 74. Within the 165-study video-to-speech population: multi-view input 20; multi-view PESQ on OuluVS2 2. Read in full: [[1]](#ref-1), [[2]](#ref-2), [[4]](#ref-4), [[5]](#ref-5). Known-item recall 7 of 7.
- **M06, video-to-speech synthesis.** Inclusion rule: studies that synthesize a speech waveform from talking-face or lip video and report the acoustic representation and waveform generation; audio-visual enhancement with noisy audio at test, talking-head generation and video-to-text-to-TTS excluded; versions counted once. Slot-filled 7,345; pattern match 165 unique studies. Usual design: neural vocoder, 49 (pattern match); parametric vocoder 41, Griffin-Lim 16, auditory spectrogram 3. Read in full: [[3]](#ref-3), [[7]](#ref-7). Known-item recall 1.0 (3 of 3 table seeds); 4 of 7 for the target's seeds, the three missed being text lip-reading papers.
- **M12, video-to-speech output evaluation.** Inclusion rule: the M06 population, classified by evaluation protocol: listener or opinion tests, ASR WER on the output, unseen-speaker tests (upper bound, related-work mentions included). Slot-filled 6,960; pattern match 165 unique studies. Usual design: listener or opinion test, 83 (pattern match); unseen-speaker test 51, ASR WER on output 38. Read in full: [[3]](#ref-3), [[8]](#ref-8), [[9]](#ref-9), [[6]](#ref-6), [[7]](#ref-7). Known-item recall 1.0 (3 of 3 table seeds); 4 of 7 for the target's seeds, the three missed being text lip-reading papers.

## References

Numbered by first citation. BibTeX in the same order and keys: [lipper-synthesizing-thy-speech-using-multi-view-lipreading.bib](lipper-synthesizing-thy-speech-using-multi-view-lipreading.bib).

1. <a id="ref-1"></a>Kumar, Y., Jain, R., Salik, K. M., Shah, R. R., Yin, Y., Zimmermann, R. “Lipper: Synthesizing Thy Speech using Multi-View Lipreading.” *Proceedings of the AAAI Conference on Artificial Intelligence*, 2019, 33, 2588-2595. doi:[10.1609/aaai.v33i01.33012588](https://doi.org/10.1609/aaai.v33i01.33012588). arXiv:[1907.01367](https://arxiv.org/abs/1907.01367). Target. Read as arXiv:1907.01367 v1 (AAAI-19 text, copyright line on the first page); volume and pages from the AAAI proceedings record. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lipper-synthesizing-thy-speech-using-multi-view-lipreading) [wiki: arxiv-1907.01367](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1907.01367/article.md)
2. <a id="ref-2"></a>Kumar, Y., Aggarwal, M., Nawal, P., Satoh, S., Shah, R. R., Zimmermann, R. “Harnessing AI for Speech Reconstruction using Multi-view Silent Video Feed.” *Proceedings of the 26th ACM International Conference on Multimedia (MM '18)*, 2018, 1976-1983. doi:[10.1145/3240508.3241911](https://doi.org/10.1145/3240508.3241911). arXiv:[1807.00619](https://arxiv.org/abs/1807.00619). [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/harnessing-ai-for-speech-reconstruction-using-multi-view-silent-video-feed) [wiki: arxiv-1807.00619](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1807.00619/article.md)
3. <a id="ref-3"></a>Ephrat, A., Peleg, S. “Vid2speech: Speech Reconstruction from Silent Video.” *2017 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2017, 5095-5099. doi:[10.1109/ICASSP.2017.7953127](https://doi.org/10.1109/ICASSP.2017.7953127). arXiv:[1701.00495](https://arxiv.org/abs/1701.00495). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/vid2speech-speech-reconstruction-from-silent-video) [wiki: arxiv-1701.00495](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1701.00495/article.md)
4. <a id="ref-4"></a>Petridis, S., Wang, Y., Li, Z., Pantic, M. “End-to-End Multi-View Lipreading.” *Proceedings of the British Machine Vision Conference (BMVC)*, 2017. doi:[10.5244/C.31.161](https://doi.org/10.5244/C.31.161). arXiv:[1709.00443](https://arxiv.org/abs/1709.00443). [wiki: arxiv-1709.00443](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1709.00443/article.md)
5. <a id="ref-5"></a>Uttam, S., Kumar, Y., Sahrawat, D., Aggarwal, M., Shah, R. R., Mahata, D., et al. “Hush-Hush Speak: Speech Reconstruction Using Silent Videos.” *Interspeech 2019*, 2019, 136-140. doi:[10.21437/Interspeech.2019-3269](https://doi.org/10.21437/Interspeech.2019-3269). [later] [wiki: isca-uttam19-hushhush](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-uttam19-hushhush/article.md) [wiki: isca-uttam19_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-uttam19_interspeech/article.md)
6. <a id="ref-6"></a>Le Cornu, T., Milner, B. “Generating Intelligible Audio Speech From Visual Speech.” *IEEE/ACM Transactions on Audio, Speech, and Language Processing*, 2017, 25(9), 1751-1761. doi:[10.1109/TASLP.2017.2716178](https://doi.org/10.1109/TASLP.2017.2716178). [wiki: doi-10.1109-taslp.2017.2716178](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-taslp.2017.2716178/article.md)
7. <a id="ref-7"></a>Kefalas, T., Panagakis, Y., Pantic, M. “Large-scale unsupervised audio pre-training for video-to-speech synthesis.” *IEEE/ACM Transactions on Audio, Speech, and Language Processing*, 2024, 32, 2255-2268. doi:[10.1109/TASLP.2024.3382500](https://doi.org/10.1109/TASLP.2024.3382500). arXiv:[2306.15464](https://arxiv.org/abs/2306.15464). Read as arXiv v1 (2023); Table VII. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/large-scale-unsupervised-audio-pre-training-for-video-to-speech-synthesis) [wiki: arxiv-2306.15464-v2apretrain](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2306.15464-v2apretrain/article.md)
8. <a id="ref-8"></a>Akbari, H., Arora, H., Cao, L., Mesgarani, N. “Lip2AudSpec: Speech Reconstruction from Silent Lip Movements Video.” *2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2018, 2516-2520. doi:[10.1109/ICASSP.2018.8461856](https://doi.org/10.1109/ICASSP.2018.8461856). arXiv:[1710.09798](https://arxiv.org/abs/1710.09798). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lip2audspec-speech-reconstruction-from-silent-lip-movements-video) [wiki: arxiv-1710.09798](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1710.09798/article.md)
9. <a id="ref-9"></a>Ephrat, A., Halperin, T., Peleg, S. “Improved Speech Reconstruction from Silent Video.” *2017 IEEE International Conference on Computer Vision Workshops (ICCVW)*, 2017, 455-462. doi:[10.1109/ICCVW.2017.61](https://doi.org/10.1109/ICCVW.2017.61). arXiv:[1708.01204](https://arxiv.org/abs/1708.01204). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/improved-speech-reconstruction-from-silent-video) [wiki: arxiv-1708.01204](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1708.01204/article.md)
