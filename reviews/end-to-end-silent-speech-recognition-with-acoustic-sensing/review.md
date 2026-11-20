# End-to-end Silent Speech Recognition with Acoustic Sensing

Luo, J., Wang, J., Cheng, N., Jiang, G., Xiao, J. · IEEE SLT 2021 · 2021 · [doi:10.1109/SLT48900.2021.9383622](https://doi.org/10.1109/SLT48900.2021.9383622) · [arXiv:2011.11315](https://arxiv.org/abs/2011.11315)

## Verdict

The paper [[1]](#ref-1) changes two components: carrier phase on 8 near-ultrasonic tones from a phone instead of Doppler shift (M05), and an attention decoder chosen over CTC (M06). M05 is new for speech, not for acoustic sensing [[2]](#ref-2), and standard on the evidence: one unrepeated ablation in which raw phase is worse than Doppler. M06 is standard: attention beat CTC on a shared front end in 2018 with the same internal-language-model explanation [[3]](#ref-3), and hybrid CTC/attention, already used for lip reading [[4]](#ref-4), is not tested. The strongest overreach is the "speaker-independent and environment-independent" 8.4% WER (Abstract): a domain is a user and an environment (Sec. 4.3), but tuning used a random split that includes the held-out users, and all tests use 54 sentences built from 29 words.

## Against the field, component by component

### M05 Sensors: phase of near-ultrasonic reflections

**Usual approach:** Doppler-shift features from a continuous-wave carrier, 16 of the 28 studies on active acoustic speech sensing (pattern match with full-text recall; Appendix), back to a 40 kHz ultrasonic emitter [[5]](#ref-5). The paper replaces Doppler with I/Q phase, delta and double-delta on 8 carriers (17–23 kHz) of a commodity phone.

**State of the art:** in 2026, a dataset baseline on acoustic-sensing eyewear reached 26.3% WER on open-vocabulary silent speech from FMCW echo profiles alone (5,356 word types, one speaker) [[6]](#ref-6) [later]; against 29 words, the two do not rank.

None of the 28 studies in the Appendix uses carrier phase apart from the target; later work moved to FMCW echo profiles (12, pattern match). The authors take the case against Doppler from device-free gesture tracking (Sec. 1) [[2]](#ref-2). The 2007 prior gave 70.5% WER on clean digits in its ultrasonic-only column (Table 1) [[5]](#ref-5), a different task. Within the target, phase delta plus double-delta (11.2%) beats Doppler (29.4%), 62% relative (inference), but raw phase (32.1%) is worse than Doppler, and only phase got deltas (Table 2). One split, no seeds. Verdict: standard.

### M06 Decoding: attention encoder-decoder versus CTC

**Usual approach:** hybrid CTC/attention is named in 79 of the 132 studies whose full text names both decoders (pattern match with full-text recall; Appendix), mentions, not use; lip reading used it in 2018 [[4]](#ref-4). The paper tests only the two pure forms.

**State of the art:** Auto-AVSR (2023) trains with joint CTC/attention and reaches 14.6% visual-only WER on LRS2 [[7]](#ref-7) [later]. The closest controlled comparison of the pure forms is from 2018: Transformer 50.0% against 55.0% WER for the best CTC model (Table 1) on a shared front end, 9% relative (inference), attributed to the attention model learning the corpus [[3]](#ref-3).

The target's gaps are 3.7 against 2.6%, 10.5 against 8.4% and 8.8 against 8.1% (bar labels, Fig. 4(c)), 30%, 20% and 8% relative (inference), one run each. Direction and explanation repeat [[3]](#ref-3); 3 studies make this comparison (confirmed; Appendix). Verdict: standard.

### M12 Evaluation: how test data are separated

**Usual approach:** a user-held-out test, 7 of the 22 ledger matches on acoustic sensing (pattern match; Appendix), as with 5 disjoint test speakers in 2007 [[5]](#ref-5). The paper reports a random split (2.6%), leave-one-domain-out (8.4%) and leave-one-sentence-out (8.1%).

**State of the art:** in 2025, near-ultrasonic FMCW on a 41-word set gave within-user (WER-w) 4.56–8.96% and cross-user (WER-c) 14.22–19.05% WER even after fine-tuning on 10 words per new user [[8]](#ref-8) [later].

The target's cross-domain 8.4% sits at that within-user level (inference); tasks differ, so this is context, not evidence. The test holds out users and environments, matching the usual approach; the defect is tuning on random-split validation data that covers all users (Sec. 4.3). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Silent mouthing of prompted sentences | Overt or attempted speech (slot-filled 4,015) | – | standard |
| M02 Training-only supervision | Word label sequences from the prompts | Paired audio or text labels (slot-filled 31) | – | standard |
| M03 Training and adaptation | From scratch; time-scaling augmentation | Supervised training per task (slot-filled 1,608) | – | standard |
| M04 Use-time action | Handheld phone, user-chosen distance | Silent articulation at use (slot-filled 6,538) | – | standard |
| M05 Sensors | I/Q phase with deltas on 8 carriers (17–23 kHz), phone speaker and microphone | Doppler-shift features (pattern match 16) | 26.3% WER open vocabulary, FMCW eyewear, 2026 [[6]](#ref-6) [later] | standard |
| M06 Processing and decoding | CNN plus attention encoder-decoder (LSTM) | Hybrid CTC/attention (pattern match 79) | Joint CTC/attention, 14.6% WER visual-only, LRS2, 2023 [[7]](#ref-7) [later] | standard |
| M07 Lexicon and LM | Beam search; beam width and any external language model not stated | Language model or lexicon (slot-filled 120) | – | not reported |
| M08 Output | Word sequence | Text (slot-filled 3,760) | – | standard |
| M09 Confirmation | None | Absent (slot-filled 82) | – | not applicable |
| M10 Correction | None | Absent (slot-filled 82) | – | not applicable |
| M11 Reference construction | Private: 54 sentences, 29 words, 10 volunteers | Study-specific corpus (slot-filled 239) | – | standard |
| M12 Evaluation | WER: random, leave-one-domain-out, leave-one-sentence-out | User held out (pattern match 7) | Cross-user WER 14.22–19.05%, 41 words, 2025 [[8]](#ref-8) [later] | standard |
| M13 Device and cost | Commodity phone, deployment claimed | Laboratory, offline (slot-filled 6,721) | – | not reported |

## Where the claims outrun the evidence

- "Generalizing very well across different domains" (Sec. 4.3) rests on unspecified folds and on tuning with data from the held-out users.
- The unseen-sentence test recombines 29 words seen in training; "very impressive" (Sec. 4.3) overstates it, and the worst sentence reaches 18.2% (Fig. 4(b)).
- "Each component in our pipeline boosts the recognition performance" (Sec. 4.2): raw phase does not beat Doppler.
- The internal-language-model explanation (Sec. 4.4) is asserted, not tested.
- Deployment on "existing smart devices" (Sec. 1) has no latency or power figures; lip-to-phone distance was left to each user (Sec. 4.1).

## What the field needs next

- M05: phase, Doppler and FMCW echo profiles on the same users with identical deltas and seeds.
- M12: user-disjoint folds with hyperparameters chosen without the held-out users, plus a word-disjoint test.
- M06: hybrid CTC/attention against attention-only, with and without an external language model.

## Questions for the authors

- How many leave-one-domain-out folds were run, and did tuning data include held-out users?
- Were deltas computed for the Doppler features?
- What beam width was used, and how was Standard Chinese tokenized for WER?

## Appendix: literature search

- M05 active-acoustic-speech-sensing (new topic table). Inclusion rule: studies that emit an acoustic signal (near-ultrasonic or ultrasonic, from a loudspeaker, earphone or transducer) and decode speech, silent speech or mouth state from its reflection or Doppler shift off the lips, face, jaw or vocal tract, captured by a microphone; B-mode tongue imaging, RF radar, Wi-Fi and laser sensing excluded when read; reviews and datasets without a decoding result are pattern matches only; versions counted once. Slot-filled 7,329 unique studies; pattern match 22 unique studies; 28 unique studies with full text after the full-text recall pattern. Full-text pattern counts: Doppler 16, FMCW, echo profile or chirp 12, commodity device 11, carrier phase 1 (the target). Usual design: Doppler-shift features, 16 (pattern match). State of the art: [[6]](#ref-6) [later]. Read in full: [[5]](#ref-5), [[6]](#ref-6) [later], target. Recall sample: 10 full-text-only snippets read, none with carrier phase.
- M06 ctc-vs-attention (published topic table, appended). Inclusion rule unchanged: the same front end trained with a CTC decoder and with an attention or sequence-to-sequence decoder, results side by side; hybrid-only studies excluded. Slot-filled 7,345 unique studies; pattern match 114 unique studies; confirmed 3 unique studies. Full-text pattern count over 132 studies: hybrid CTC/attention 79. Usual design: hybrid CTC/attention, 79 (pattern match). State of the art: [[7]](#ref-7) [later]; closest controlled comparison [[3]](#ref-3). Read in full: [[3]](#ref-3), [[4]](#ref-4), [[7]](#ref-7) [later], target. Known-item recall 0.5 (published table).
- M12 acoustic-sensing-test-split (new topic table). Inclusion rule: the M05 population; the design compared is how the test set is separated from training (user held out, session or day held out, random sample split); a paper counts under every protocol it names. Slot-filled 6,960 unique studies; pattern match 22 unique studies. Full-text pattern counts: user held out 7, random split 6, session held out 3. Usual design: user held out, 7 (pattern match). State of the art: [[8]](#ref-8) [later]. Read in full: [[5]](#ref-5), [[8]](#ref-8) [later], target.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Luo, J., Wang, J., Cheng, N., Jiang, G., Xiao, J. “End-to-End Silent Speech Recognition with Acoustic Sensing.” *2021 IEEE Spoken Language Technology Workshop (SLT)*, 2021, 606–612. doi:[10.1109/SLT48900.2021.9383622](https://doi.org/10.1109/SLT48900.2021.9383622). arXiv:[2011.11315](https://arxiv.org/abs/2011.11315). Target. Read as arXiv v1. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/end-to-end-silent-speech-recognition-with-acoustic-sensing) [wiki: arxiv-2011.11315](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2011.11315/article.md)
2. <a id="ref-2"></a>Wang, W., Liu, A. X., Sun, K. “Device-Free Gesture Tracking Using Acoustic Signals.” *Proc. 22nd Annual International Conference on Mobile Computing and Networking (MobiCom)*, 2016, 82–94. doi:[10.1145/2973750.2973764](https://doi.org/10.1145/2973750.2973764). Cited by the target as [18]; metadata from the target's reference list.
3. <a id="ref-3"></a>Afouras, T., Chung, J. S., Zisserman, A. “Deep Lip Reading: A Comparison of Models and an Online Application.” *Proc. Interspeech 2018*, 2018, 3514–3518. doi:[10.21437/Interspeech.2018-1943](https://doi.org/10.21437/Interspeech.2018-1943). arXiv:[1806.06053](https://arxiv.org/abs/1806.06053). [wiki: arxiv-1806.06053](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1806.06053/article.md) [wiki: isca-afouras18b-deeplip](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-afouras18b-deeplip/article.md) [wiki: isca-afouras18b_deeplipread](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-afouras18b_deeplipread/article.md) [wiki: isca-afouras18b_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-afouras18b_interspeech/article.md)
4. <a id="ref-4"></a>Petridis, S., Stafylakis, T., Ma, P., Tzimiropoulos, G., Pantic, M. “Audio-Visual Speech Recognition with a Hybrid CTC/Attention Architecture.” *2018 IEEE Spoken Language Technology Workshop (SLT)*, 2018, 513–520. doi:[10.1109/SLT.2018.8639643](https://doi.org/10.1109/SLT.2018.8639643). arXiv:[1810.00108](https://arxiv.org/abs/1810.00108). [wiki: arxiv-1810.00108](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1810.00108/article.md) [wiki: doi-10.1109-slt.2018.8639643](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-slt.2018.8639643/article.md)
5. <a id="ref-5"></a>Zhu, B., Hazen, T. J., Glass, J. R. “Multimodal Speech Recognition with Ultrasonic Sensors.” *Proc. Interspeech 2007*, 2007, 662–665. doi:[10.21437/Interspeech.2007-284](https://doi.org/10.21437/Interspeech.2007-284). [wiki: isca-zhu07_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-zhu07_interspeech/article.md)
6. <a id="ref-6"></a>Zhang, R., Liu, J., Guimbretière, F., Zhang, C. “SoniSpeech: A Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces.” *Proc. Interspeech 2026*, 2026. arXiv:[2608.00803](https://arxiv.org/abs/2608.00803). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/sonispeech-a-large-scale-open-vocabulary-tri-modal-dataset-for-wearable-silent-speech-interfaces) [wiki: isca-zhang26y-sonispeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-zhang26y-sonispeech/article.md) [wiki: arxiv-2608.00803](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2608.00803/article.md)
7. <a id="ref-7"></a>Ma, P., Haliassos, A., Fernandez-Lopez, A., Chen, H., Petridis, S., Pantic, M. “Auto-AVSR: Audio-Visual Speech Recognition with Automatic Labels.” *Proc. IEEE ICASSP 2023*, 2023. doi:[10.1109/ICASSP49357.2023.10096889](https://doi.org/10.1109/ICASSP49357.2023.10096889). arXiv:[2303.14307](https://arxiv.org/abs/2303.14307). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/auto-avsr-audio-visual-speech-recognition-with-automatic-labels) [wiki: arxiv-2303.14307](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2303.14307/article.md)
8. <a id="ref-8"></a>Zhou, J., Ding, D., Li, Y., Lu, Y., Wang, Y., Zhang, Y., et al. “M2SILENT: Enabling Multi-user Silent Speech Interactions via Multi-directional Speakers in Shared Spaces.” *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems*, 2025, 1–19. doi:[10.1145/3706598.3714174](https://doi.org/10.1145/3706598.3714174). [later] [wiki: doi-10.1145-3706598.3714174](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1145-3706598.3714174/article.md)
