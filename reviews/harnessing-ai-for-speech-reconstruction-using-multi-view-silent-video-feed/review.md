# Harnessing AI for Speech Reconstruction using Multi-view Silent Video Feed

Yaman Kumar, Mayank Aggarwal, Pratham Nawal, Shin'ichi Satoh, Rajiv Ratn Shah, Roger Zimmermann. Proceedings of the 26th ACM International Conference on Multimedia (MM '18), pp. 1976–1983, 2018. [doi:10.1145/3240508.3241911](https://doi.org/10.1145/3240508.3241911) · [arXiv:1807.00619](https://arxiv.org/abs/1807.00619)

## Verdict

The paper [[1]](#ref-1) changes one component, the camera input (M05), feeding two OuluVS2 views to a video-to-speech regressor; no earlier video-to-speech ledger paper names multi-view input (Appendix). The design is new for speech output but standard on its evidence: two speakers, no repeats or split stated, best pairs only (Sec. 4.3, Sec. 6). Table 1 gives +11.4% and +12.2% PESQ for 0°+30° over 0° (inference), not the stated 26% and 27%. The 30° to 60° placement rule rests on two pairs; follow-up work by the same group finds 0°+45° best and 0°+60° below 0°+90° [[2]](#ref-2) [concurrent], and a 1.1% gain for 0°+30° on held-out data [[3]](#ref-3) [later] (inference). The evaluation (M12) is behind: PESQ only, where the systems it builds on all ran listener tests.

## Against the field, component by component

### M05 Sensors: number and placement of camera views

**Usual approach:** One camera: of 787 unique lip-reading and video-to-speech studies (pattern match, Appendix), 693 name no multi-view input; of 165 video-to-speech studies, 20 do, none before the target. The closest earlier design is multi-view lip reading to text, which the paper itself traces to a 2006 two-view study (Sec. 2); in the strongest, frontal plus profile gains 3% absolute accuracy [[4]](#ref-4). The paper moves this input to audio output.

**State of the art:** Lipper (2019) [concurrent] reports 2.130 PESQ for 0°+45° and 2.315 for 0°+45°+60° against 2.002 frontal, speaker-dependent on OuluVS2 (Tables 4–6) [[2]](#ref-2): a two-view gain of +6.4% (inference) from a stronger start (2.002 against 1.7674). Of the 20 multi-view video-to-speech studies (Appendix), only Lipper and Hush-Hush report multi-view PESQ on OuluVS2; Hush-Hush peaks at 1.964 [[3]](#ref-3).

The deciding prior ran 10 runs on a subject-independent split with significance tests and found the best pair 90° apart, frontal plus profile [[4]](#ref-4). The target's 30° to 60° rule (Sec. 4.3) compares only 0°+30° and 0°+60°, so it cannot locate an optimum. In Lipper 0°+60° (1.952) scores below 0°+90° (1.982) [[2]](#ref-2); in Hush-Hush Speak, on held-out data from an 85:10:5 split, 0°+30° moves PESQ from 1.920 to 1.941 and 0°+60° lowers it to 1.847 [[3]](#ref-3). Verdict: standard; first for speech output, but not shown with enough repetition to call ahead.

### M12 Evaluation: objective score only, two speakers

**Usual approach:** Of the 165 video-to-speech studies (pattern match, Appendix), 83 name a listener or opinion-score test. The systems the paper builds on all ran one: Vid2speech had 23 MTurk workers transcribe its output [[5]](#ref-5), Lip2AudSpec 20 workers per sample [[6]](#ref-6), and Le Cornu and Milner report 85% word accuracy from listeners [[7]](#ref-7). The paper reports PESQ alone, for Speakers 1 and 10 (Table 1).

**State of the art:** Current practice adds ASR WER on unseen speakers: on 33 unseen GRID speakers, the 2023 comparison table gives the lowest WER, 16.05%, to a 2022 WGAN it cites, and the best PESQ, 1.43, to its own model [[8]](#ref-8). On OuluVS2, Hush-Hush Speak (2019) [later] adds a stated split and a five-judge test [[3]](#ref-3).

PESQ measures quality, not intelligibility, yet the paper uses it for both (Sec. 4.2). Three prior systems ran listener tests and the target none: behind, against the best comparable work, the three systems above.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | None; voiced OuluVS2 speech | Voiced speech corpora (slot-filled 4,015) | – | standard |
| M02 Training-only supervision | Paired voiced audio | Paired audio (slot-filled 31) | – | standard |
| M03 Training and adaptation | Training data, split and seeds unstated | Per-corpus training (slot-filled 1,608) | – | not reported |
| M04 Use-time action | Voiced speech, video alone at test | Voiced articulation (slot-filled 6,538) | – | standard |
| M05 Sensors | Two of five OuluVS2 views (0°+30°, 0°+60°) | One camera view (145 of 165) (pattern match 165) | 0°+45°+60°: 2.315 PESQ [[2]](#ref-2) | standard |
| M06 Processing and decoding | CNN-LSTM to LPC/LSP features | Neural vocoder (49); parametric vocoder 41 (pattern match 165) | – | standard |
| M07 Lexicon and LM | No lexicon or language model | No language model (slot-filled 120) | – | not applicable |
| M08 Output | Waveform from LPC/LSP | Speech waveform (slot-filled 3,760) | – | standard |
| M09 Confirmation | None (offline) | None (slot-filled 82) | – | not applicable |
| M10 Correction | None (offline) | None (slot-filled 82) | – | not applicable |
| M11 Reference construction | OuluVS2 utterances with original audio | Original audio as reference (slot-filled 239) | – | standard |
| M12 Evaluation | PESQ only, Speakers 1 and 10 | Listener or opinion test (83) (pattern match 165) | 16.05% WER (2022 WGAN row), GRID unseen [[8]](#ref-8) | behind |
| M13 Device and cost | Offline, lab lighting | Offline (slot-filled 6,721) | – | not reported |

## Where the claims outrun the evidence

- **Stated gains.** Sec. 4.3 gives 26% (male) and 27% (female) for 0°+30° over 0°, and 80% for 0°+60° over 60°. Table 1 gives +11.4%, +12.2%, +24.6% and +27.1% (absolute +0.20, +0.22, +0.37, +0.42 PESQ) (inference). The text overstates every gain: all eight percentages in Sec. 4.3 exceed the matching Table 1 ratios (inference).
- **Selection.** Only "the best results among multiple views" are shown (Sec. 4.3); with no split or validation set stated (Sec. 6), the pairs may have been chosen on the test data.
- **Capacity confound.** The two-view model receives two image streams (inference; fusion undescribed, Sec. 3.2); no control feeds one view twice, so the gain is not shown to come from the second angle.
- **Headroom.** LPC resynthesis of the real audio scores 2.5291 and 2.6255 PESQ (Table 2); the gap from the best pair to it (0.56 and 0.63) exceeds the multi-view gain (inference).
- **"First" and "language independent".** Multi-view input predates the paper in lip reading, from 2006 (Sec. 2) to [[4]](#ref-4). Language and vocabulary independence (Sec. 1, Sec. 3) are untested; the authors leave the limited lexicon to future work (Sec. 6).
- **Authors' caveats.** The results are called preliminary (Sec. 4.3, Sec. 6), and model size is said to exceed on-camera deployment (Sec. 6).

## What the field needs next

- M05: all view pairs and triples on held-out speakers, with a same-view duplicate control, to separate angle from input size.
- M12: a listener transcription test and ASR WER on the output, with a stated speaker-disjoint split, so multi-view gains are measured in intelligibility.
- M05/M13: robustness when one camera drops out or drifts out of sync.

## Questions for the authors

- Which utterances and sessions of Speakers 1 and 10 were in training, and was any test utterance seen in training?
- How were the "best" view combinations chosen, and on which data?
- How were the 26%, 27% and 80% gains computed from Table 1?
- What LPC order, sample rate, fusion scheme and number of runs stand behind each value?

## Appendix: literature search

- M05 multi-view-camera-input (new topic table). Inclusion rule: video-based speech decoding (lip reading, visual speech recognition, video-to-speech) with an optical camera in the ledger, counted from the full text (reference list removed) by multi-view input, non-frontal pose handling and OuluVS2 use; a study counts under every design its text names (upper bound, related-work mentions included); talking-head generation and biometric-only studies excluded; versions counted once. Slot-filled 7,329 unique studies; pattern match 787 unique studies. Usual design: one camera view, 693 (pattern match; population minus multi-view hits). Design counts: non-frontal pose 128, multi-view input 94, OuluVS2 74. Added count: within the 165-study video-to-speech population of the M12 table, 20 unique studies name multi-view input; none is dated before the target, and only two of them report multi-view PESQ on OuluVS2 (Lipper, Hush-Hush). Read in full: [[4]](#ref-4), [[2]](#ref-2) [concurrent], [[3]](#ref-3) [later], target. Recall sample: 25 full-text-only snippets read, none with multi-view speech synthesis before the target. Known-item recall 1.0.
- M12 video-to-speech-output-evaluation (published topic table, appended). Inclusion rule: studies that synthesize a speech waveform from talking-face or lip video, compared by how the output is evaluated (listener or opinion tests, ASR WER on the output, unseen-speaker tests); a study counts under every protocol its full text names (upper bound); versions counted once. Slot-filled 6,960 unique studies; pattern match 165 unique studies. Usual design: listener or opinion-score test, 83 (pattern match). Design counts: listener test 83, unseen-speaker test 51, ASR WER on the output 38. State of the art from the table: [[8]](#ref-8) [later]. Read in full: [[5]](#ref-5), [[6]](#ref-6), [[7]](#ref-7), target. Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Kumar, Y., Aggarwal, M., Nawal, P., Satoh, S., Shah, R. R., Zimmermann, R. “Harnessing AI for Speech Reconstruction using Multi-view Silent Video Feed.” *Proceedings of the 26th ACM International Conference on Multimedia (MM '18)*, 2018, 1976-1983. doi:[10.1145/3240508.3241911](https://doi.org/10.1145/3240508.3241911). arXiv:[1807.00619](https://arxiv.org/abs/1807.00619). Target. Read as arXiv v2 (ACM MM '18 text); venue and pages confirmed against the Crossref record. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/harnessing-ai-for-speech-reconstruction-using-multi-view-silent-video-feed) [wiki: arxiv-1807.00619](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1807.00619/article.md)
2. <a id="ref-2"></a>Kumar, Y., Jain, R., Salik, K. M., Shah, R. R., Yin, Y., Zimmermann, R. “Lipper: Synthesizing Thy Speech using Multi-View Lipreading.” *Proceedings of the AAAI Conference on Artificial Intelligence*, 2019, 33, 2588-2595. doi:[10.1609/aaai.v33i01.33012588](https://doi.org/10.1609/aaai.v33i01.33012588). arXiv:[1907.01367](https://arxiv.org/abs/1907.01367). [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lipper-synthesizing-thy-speech-using-multi-view-lipreading) [wiki: arxiv-1907.01367](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1907.01367/article.md)
3. <a id="ref-3"></a>Uttam, S., Kumar, Y., Sahrawat, D., Aggarwal, M., Shah, R. R., Mahata, D., et al. “Hush-Hush Speak: Speech Reconstruction Using Silent Videos.” *Interspeech 2019*, 2019, 136-140. doi:[10.21437/Interspeech.2019-3269](https://doi.org/10.21437/Interspeech.2019-3269). [later] [wiki: isca-uttam19-hushhush](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-uttam19-hushhush/article.md) [wiki: isca-uttam19_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-uttam19_interspeech/article.md)
4. <a id="ref-4"></a>Petridis, S., Wang, Y., Li, Z., Pantic, M. “End-to-End Multi-View Lipreading.” *Proceedings of the British Machine Vision Conference (BMVC)*, 2017. doi:[10.5244/C.31.161](https://doi.org/10.5244/C.31.161). arXiv:[1709.00443](https://arxiv.org/abs/1709.00443). [wiki: arxiv-1709.00443](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1709.00443/article.md)
5. <a id="ref-5"></a>Ephrat, A., Peleg, S. “Vid2speech: Speech Reconstruction from Silent Video.” *2017 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2017, 5095-5099. doi:[10.1109/ICASSP.2017.7953127](https://doi.org/10.1109/ICASSP.2017.7953127). arXiv:[1701.00495](https://arxiv.org/abs/1701.00495). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/vid2speech-speech-reconstruction-from-silent-video) [wiki: arxiv-1701.00495](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1701.00495/article.md)
6. <a id="ref-6"></a>Akbari, H., Arora, H., Cao, L., Mesgarani, N. “Lip2AudSpec: Speech Reconstruction from Silent Lip Movements Video.” *2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2018, 2516-2520. doi:[10.1109/ICASSP.2018.8461856](https://doi.org/10.1109/ICASSP.2018.8461856). arXiv:[1710.09798](https://arxiv.org/abs/1710.09798). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lip2audspec-speech-reconstruction-from-silent-lip-movements-video) [wiki: arxiv-1710.09798](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1710.09798/article.md)
7. <a id="ref-7"></a>Le Cornu, T., Milner, B. “Generating Intelligible Audio Speech From Visual Speech.” *IEEE/ACM Transactions on Audio, Speech, and Language Processing*, 2017, 25(9), 1751-1761. doi:[10.1109/TASLP.2017.2716178](https://doi.org/10.1109/TASLP.2017.2716178). [wiki: doi-10.1109-taslp.2017.2716178](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-taslp.2017.2716178/article.md)
8. <a id="ref-8"></a>Kefalas, T., Panagakis, Y., Pantic, M. “Large-scale unsupervised audio pre-training for video-to-speech synthesis.” *IEEE/ACM Transactions on Audio, Speech, and Language Processing*, 2024, 32, 2255-2268. doi:[10.1109/TASLP.2024.3382500](https://doi.org/10.1109/TASLP.2024.3382500). arXiv:[2306.15464](https://arxiv.org/abs/2306.15464). Read as arXiv v1 (2023); Table VII. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/large-scale-unsupervised-audio-pre-training-for-video-to-speech-synthesis) [wiki: arxiv-2306.15464-v2apretrain](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2306.15464-v2apretrain/article.md)
