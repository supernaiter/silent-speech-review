# Poster: Recognizing Hidden-in-the-Ear Private Key for Reliable Silent Speech Interface Using Multi-Task Learning

Dong, X., Xu, L., He, L., Han, Z., Christofferson, K., Chen, Y., Taya, A., Nishiyama, Y., Sezaki, K. · UbiComp Companion '25 · 2025 · [arXiv:2512.16518](https://arxiv.org/abs/2512.16518)

## Verdict

HEar-ID [[1]](#ref-1) changes the sensing (in-ear ultrasound plus whisper, M05), the model (shared encoder with contrastive, triplet and CTC heads, M06), enrollment (M03) and the output (word plus accept or deny, M08). Each is standard: audio-plus-ultrasound fusion [[2]](#ref-2), headphone echo sensing [[3]](#ref-3), verification from murmured speech [[4]](#ref-4) and content-plus-identity output [[5]](#ref-5) predate it; what is new is the combination on one earbud. The spelling result is no gain: all-user Top-1 is 67.3%, and the selected 8-user 90.25% is below the ultrasonic-only baseline it calls comparable, 91.4% (§4.1.2). Authentication is tested only against the other participants, whose data also train the model (§4.1.1), so M12 is behind; replay, the attack that motivates the paper (§1), is never tried.

## Against the field, component by component

### M05 Sensors: in-ear ultrasound plus whisper

**Usual approach:** Of 28 active-acoustic studies, 16 use Doppler features from a continuous-wave carrier; of the 22 ledger matches, 12 mount on glasses or a headset, 11 name a fused audio stream and 8 an earphone or ear canal (pattern match, Appendix). HEar-ID uses OFDM (1 of 22, the target) and one ANC-earbud microphone for 17.5–23 kHz reflections and 0–11 kHz whisper (§1).

**State of the art:** HPSpeech [[3]](#ref-3) (2023): 90.3% on 8 silent commands from headphone FMCW echoes, user-dependent, held-out sessions. HEar-ID: 67.3% on 50 words. The [concurrent] M2SILENT reaches within-user WER 4.56–8.96% on 41 words [[6]](#ref-6); the [later] SoniSpeech 26.3% WER on open vocabulary, one speaker [[7]](#ref-7).

Ultrasound cut audio digit WER by 24–29% relative [[2]](#ref-2); a headset fuses vocal and echo keyword spotters [[8]](#ref-8). No whisper-only or ultrasound-only result is given (§4.1.2); with "silent" meaning subtle voicing (§1), audio may carry most of the content (inference). Verdict: standard.

### M06 Processing: shared encoder, contrastive and triplet heads

**Usual approach:** Of 75 verification studies, 37 name HMM or Gaussian-mixture models, 13 cross-modal alignment, 8 metric learning and 6 a shared or multi-task encoder (pattern match, Appendix).

**State of the art:** Okamoto et al. [[4]](#ref-4) (2007): EER 0.2% from non-audible murmur, impostors disjoint from customers, held-out session; 5.5% (male) under impersonation. HEar-ID names EER but reports none (§4.1.2).

The threshold is fixed with Youden's J on unnamed data (§3.4), and one run without seeds (§4.1.1) cannot separate the shared encoder from a cascade. Verdict: standard.

### M03 Training: enrollment and impostor data

**Usual approach:** 27 of the 75 studies use impostor or background data, 9 name enrollment (pattern match, Appendix). HEar-ID enrolls from a few spellings and trains against other people's data, to be supplied by manufacturers (§3.4).

**State of the art:** Okamoto et al. [[4]](#ref-4) (2007) test 18 male and 9 female impostors who are not customers, on a held-out session.

Test impostors are training impostors (§4.1.1), so the manufacturer proposal is untested on strangers. Verdict: standard.

### M08 Output: word and identity together

**Usual approach:** 67 of the 75 studies return identity only; 8 name content and identity together (pattern match, upper bound, Appendix).

**State of the art:** Chetty and Wagner [[5]](#ref-5) (2008): digits at 70–90%, then speaker verification at EER 0.9–1.2% and liveness at 0.6–0.8% (Sec. 4), held-out impostors.

Face authentication plus lip-read silent digits reaches 96.2% [[9]](#ref-9); a whisper mask recognises words above 92% and 4 users above 90% [[10]](#ref-10). HEar-ID adds one network for both, with no cascade baseline (§4.1.2). Verdict: standard.

### M12 Evaluation: test split and impostors

**Usual approach:** Of 22 acoustic-sensing studies, 7 hold out users, 6 split at random, 3 hold out sessions (pattern match, Appendix). HEar-ID holds out one session per user, with user-dependent recognition (§4.1.1).

**State of the art:** M2SILENT [[6]](#ref-6) (2025, [concurrent]): cross-user WER 14.22–19.05% on 41 words after fine-tuning on 10 words per new user.

User-held-out tests predate HEar-ID [[11]](#ref-11), [[2]](#ref-2), [[3]](#ref-3), and both read verifiers keep impostors out of training [[4]](#ref-4), [[5]](#ref-5). Verdict: behind (best comparable work).

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | 50 words spelled, subtle voice | Recorded articulation (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | CTC letter targets | Text or paired-audio labels (slot-filled 31) | – | standard |
| M03 Training and adaptation | Few-shot enrollment, others as impostors | Impostor data (pattern match 27) | [[4]](#ref-4) (2007): disjoint impostors | standard |
| M04 Use-time action | Spell a word, subtle voice | Silent or overt (slot-filled 5,595) | – | standard |
| M05 Sensors | In-ear OFDM ultrasound + whisper | CW Doppler carrier (pattern match 16) | [[3]](#ref-3) (2023): 90.3%, 8 commands | standard |
| M06 Processing and decoding | Shared encoder, contrastive + triplet + CTC | HMM or GMM (pattern match 37) | [[4]](#ref-4) (2007): EER 0.2% | standard |
| M07 Lexicon and LM | Decoder constraint not stated | Lexicon or LM (slot-filled 119) | – | not reported |
| M08 Output | Word + accept/deny, one model | Identity only (pattern match 67) | [[5]](#ref-5) (2008): EER 0.9–1.2% | standard |
| M09 Confirmation | Automatic accept or deny | Offline (slot-filled 82) | – | not applicable |
| M10 Correction | None | Offline (slot-filled 82) | – | not applicable |
| M11 Reference construction | Fixed 50-word list | Corpus references (slot-filled 234) | – | standard |
| M12 Evaluation | Session held out, same users | User held out (pattern match 7) | [[6]](#ref-6) (2025): cross-user WER 14.22–19.05% | behind |
| M13 Device and cost | Modified earbud wired to phone | Hardware stated (slot-filled 6,075) | – | standard |

## Where the claims outrun the evidence

- "90.25% over 8 out of 11 participants" (Conclusion) is a post-hoc subset; 67.3% for all is 24.1 points (26% relative) below the 91.4% baseline (inference), whose split is unstated (§4.1.1).
- "Robust authentication under real-world conditions" (Conclusion): S3 has FPR 19.20%, S9 and S10 TPR 0.00% (Fig. 3b).
- Mean TPR 81.76% and FPR 3.2% (§4.1.2) differ from the Fig. 3b means, 80.00% and 3.27% (inference); S5 is 99.9% TPR in text, 98.00% in Fig. 3b.
- "First earable solution to authenticate via silent or whispered speech" (§2.2): murmur [[4]](#ref-4) and silent lip passwords [[9]](#ref-9) came first; only "earable" remains.

## What the field needs next

- M12: impostors disjoint from training, and whisper replayed through the earbud, reported as EER.
- M05: whisper-only, ultrasound-only and fused results on one split, and unvoiced articulation.
- M06: a cascaded recognizer and verifier against the shared encoder, over several seeds.

## Questions for the authors

- How many sessions and samples per participant?
- Was the 91.4% baseline run on the same users, words and sessions?
- Which margin was used, 11.45 or 30 degrees?

## Appendix: literature search

- M05, active-acoustic-speech-sensing (published table, reused). Inclusion rule: studies that emit a near-ultrasonic or ultrasonic signal and decode speech, silent speech or mouth state from its reflection or Doppler shift, captured by a microphone; tongue ultrasound imaging, RF radar, Wi-Fi and laser excluded; reviews and datasets count as pattern matches only. Ledger: 7,329 unique studies slot-filled for M05; 22 unique studies pattern match. Usual design: Doppler-shift features from a continuous-wave carrier 16 of 28 (pattern match, published counts); FMCW, echo profile or chirp 12. Read in full: [[2]](#ref-2), [[11]](#ref-11), [[7]](#ref-7), [[8]](#ref-8). Known-item recall 0.5.
- M05, active-acoustic-sensor-placement-and-audio-stream (new). Inclusion rule: the same population, classified by transducer placement and by fusion with a voiced or whispered audio stream; every named design counts (upper bound). Ledger: 7,329 unique studies slot-filled; 22 unique studies pattern match. Glasses or headset 12, smartphone or loudspeaker 12, audio stream fused 11, FMCW or chirp 11, in-ear, earphone or headphone 8, OFDM 1 (the target) (pattern match). Read in full: [[3]](#ref-3), [[8]](#ref-8), [[2]](#ref-2).
- M03, speech-signal-verification-enrollment (new). Inclusion rule: studies that verify or identify a user from speech-production signals (voice, whisper, murmur, lip or face motion, articulatory or active-acoustic sensing, imagined-speech EEG), found by authentication, verification, identification, biometric or impostor wording; classified by enrollment, impostor or background data, few-shot enrollment and threshold calibration; surveys and mentions count as matches. Ledger: 1,526 unique studies slot-filled for M03; 75 unique studies pattern match. Impostor or background data 27, enrollment 9, threshold calibration 3, few-shot enrollment 1 (pattern match). Read in full: [[4]](#ref-4), [[5]](#ref-5).
- M06, speech-signal-verification-model (new). Inclusion rule: the same 75 studies, classified by identity model. Ledger: 7,345 unique studies slot-filled for M06; 75 unique studies pattern match. HMM or Gaussian mixture 37, cross-modal alignment 13, GMM-UBM or i-/x-vector 11, metric-learning embedding 8, multi-task or shared encoder 6 (pattern match). Read in full: [[4]](#ref-4), [[5]](#ref-5).
- M08, content-and-identity-output (new). Inclusion rule: the same 75 studies, classified by whether content and an identity decision are returned for the same utterance; separately trained stages count as joint output. Ledger: 3,268 unique studies slot-filled for M08; 75 unique studies pattern match. Content and identity together 8, identity only 67, silent or unvoiced input 33, EER 26, attack or liveness test 22 (pattern match). Read in full: [[5]](#ref-5), [[9]](#ref-9), [[10]](#ref-10).
- M12, acoustic-sensing-test-split (published table, reused). Inclusion rule: the active-acoustic population, classified by how the test set is separated from training (user, session or random split); a paper counts under every protocol it names. Ledger: 6,960 unique studies slot-filled for M12; 22 unique studies pattern match. User held out 7, random split 6, session held out 3 (pattern match, published counts). Read in full: [[11]](#ref-11), [[2]](#ref-2), [[6]](#ref-6). Known-item recall 0.5.

## References

Numbered by first citation. BibTeX in the same order and keys: [poster-recognizing-hidden-in-the-ear-private-key-for-reliable-silent-speech-interface-using-mult.bib](poster-recognizing-hidden-in-the-ear-private-key-for-reliable-silent-speech-interface-using-mult.bib).

1. <a id="ref-1"></a>Dong, X., Xu, L., He, L., Han, Z., Christofferson, K., Chen, Y., et al. “Poster: Recognizing Hidden-in-the-Ear Private Key for Reliable Silent Speech Interface Using Multi-Task Learning.” *Companion of the 2025 ACM International Joint Conference on Pervasive and Ubiquitous Computing (UbiComp Companion '25)*, 2025. arXiv:[2512.16518](https://arxiv.org/abs/2512.16518). Target. Read as arXiv v1. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/poster-recognizing-hidden-in-the-ear-private-key-for-reliable-silent-speech-interface-using-mult) [wiki: arxiv-2512.16518](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2512.16518/article.md)
2. <a id="ref-2"></a>Zhu, B., Hazen, T. J., Glass, J. R. “Multimodal Speech Recognition with Ultrasonic Sensors.” *Proc. Interspeech 2007*, 2007. doi:[10.21437/Interspeech.2007-284](https://doi.org/10.21437/Interspeech.2007-284). Prior; audio plus ultrasonic Doppler fusion (M05), disjoint test speakers (M12). [wiki: isca-zhu07_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-zhu07_interspeech/article.md)
3. <a id="ref-3"></a>Zhang, R., Chen, H., Agarwal, D., Jin, R., Li, K., Guimbretière, F., et al. “HPSpeech: Silent Speech Interface for Commodity Headphones.” *Proceedings of the 2023 ACM International Symposium on Wearable Computers (ISWC '23)*, 2023. doi:[10.1145/3594738.3611365](https://doi.org/10.1145/3594738.3611365). Prior; state of the art for M05 (headphone echo sensing); leave-one-participant-out model (M12). [wiki: doi-10.1145-3594738.3611365](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1145-3594738.3611365/article.md)
4. <a id="ref-4"></a>Okamoto, H., Kojima, M., Matsui, T., Kawanami, H., Saruwatari, H., Shikano, K. “Study on Speaker Verification with Non-Audible Murmur Segments.” *Proc. Interspeech 2007*, 2007, 2017-2020. doi:[10.21437/Interspeech.2007-164](https://doi.org/10.21437/Interspeech.2007-164). Prior; state of the art for M03 and M06 (verification from murmured speech, disjoint impostors). [wiki: isca-okamoto07_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-okamoto07_interspeech/article.md)
5. <a id="ref-5"></a>Chetty, G., Wagner, M. “Audio-Visual Multilevel Fusion for Speech and Speaker Recognition.” *Proc. Interspeech 2008*, 2008. doi:[10.21437/Interspeech.2008-153](https://doi.org/10.21437/Interspeech.2008-153). Prior; state of the art for M08 (digit recognition plus speaker verification and liveness). [wiki: isca-chetty08_avfusion](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-chetty08_avfusion/article.md) [wiki: isca-chetty08-avfusion](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-chetty08-avfusion/article.md)
6. <a id="ref-6"></a>Zhou, J., Ding, D., Li, Y., Lu, Y., Wang, Y., Zhang, Y., et al. “M2SILENT: Enabling Multi-user Silent Speech Interactions via Multi-directional Speakers in Shared Spaces.” *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems (CHI '25)*, 2025. doi:[10.1145/3706598.3714174](https://doi.org/10.1145/3706598.3714174). State of the art for M12 (cross-user WER). [concurrent] [wiki: doi-10.1145-3706598.3714174](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1145-3706598.3714174/article.md)
7. <a id="ref-7"></a>Zhang, R., Liu, J., Guimbretière, F., Zhang, C. “SoniSpeech: A Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces.” *Proc. Interspeech 2026*, 2026. doi:[10.7298/xjjr-9m85](https://doi.org/10.7298/xjjr-9m85). Later; published state of the art for the active-acoustic topic. [later] [wiki: isca-zhang26y-sonispeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-zhang26y-sonispeech/article.md) [wiki: arxiv-2608.00803](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2608.00803/article.md)
8. <a id="ref-8"></a>Cai, Z., Ma, Y., Lu, F. “Robust Dual-Modal Speech Keyword Spotting for XR Headsets.” *IEEE Transactions on Visualization and Computer Graphics*, 2024. arXiv:[2401.14978](https://arxiv.org/abs/2401.14978). Prior; vocal and ultrasonic echo fusion on a headset (M05). [wiki: arxiv-2401.14978-xrkws](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2401.14978-xrkws/article.md)
9. <a id="ref-9"></a>Ezz, M., Mostafa, A. M., Nasr, A. A. “A Silent Password Recognition Framework Based on Lip Analysis.” *IEEE Access*, 2020, 8. doi:[10.1109/ACCESS.2020.2982359](https://doi.org/10.1109/ACCESS.2020.2982359). Prior; face authentication plus lip-read silent password (M08). [wiki: doi-10.1109-access.2020.2982359](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-access.2020.2982359/article.md)
10. <a id="ref-10"></a>Li, J., Shi, Y., Chen, J., Huang, Q., Ye, M., Guo, W. “Flexible Self-Powered Low-Decibel Voice Recognition Mask.” *Sensors*, 2024, 24(10), 3007. doi:[10.3390/s24103007](https://doi.org/10.3390/s24103007). Prior; low-decibel content recognition plus identification of four users (M08). [wiki: pmc-11124924-csteng-mask](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11124924-csteng-mask/article.md)
11. <a id="ref-11"></a>Luo, J., Wang, J., Cheng, N., Jiang, G., Xiao, J. “End-to-End Silent Speech Recognition with Acoustic Sensing.” *arXiv preprint*, 2020. arXiv:[2011.11315](https://arxiv.org/abs/2011.11315). Prior; user-held-out acoustic-sensing test (M12). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/end-to-end-silent-speech-recognition-with-acoustic-sensing) [wiki: arxiv-2011.11315](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2011.11315/article.md)
