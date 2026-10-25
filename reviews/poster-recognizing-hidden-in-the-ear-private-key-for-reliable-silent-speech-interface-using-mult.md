# Poster: Recognizing Hidden-in-the-Ear Private Key for Reliable Silent Speech Interface Using Multi-Task Learning

Xuefu Dong, Liqiang Xu, Lixing He, Zengyi Han, Ken Christofferson, Yifei Chen, Akihito Taya, Yuuki Nishiyama, Kaoru Sezaki  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2512.16518)

**Section:** [Acoustic, whisper & wearable motion sensors](../README.md#acoustic-whisper--wearable-motion-sensors) · **Review basis:** full_text+summary

HEar-ID jointly recognizes whispered ear-canal letter spelling and user identity from in-ear audio and ultrasonic reflections; Top-1 word accuracy is 67.3% across 11 users (90.25% for eight selected users).

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Modified ANC earbud in-ear microphone (whisper + ultrasound) |
| Task | Spelling-based text entry and user authentication |
| Vocabulary | 50 English words spelled with 26 letters |
| Speaker | Speaker-dependent |
| Session | Cross-session |
| Online / offline | Not stated |
| Key result | 67.3% Top-1 word accuracy across 11 users; authentication TPR 81.76%, FPR 3.2% |

**Limitations.** Depends on whisper, three users fail badly, hardware is modified, and no replay/injection attacks or unseen-impostor tests are evaluated.

## Full review

### In short

HEar-ID jointly models ear-based spelling and identity, but all-user Top-1 is 67.3%, not the selected eight-user 90.25%; whisper dependence, participant failures, modified hardware, and untested attack resistance limit deployment claims.

### Review

HEar-ID's useful contribution is to couple ear-based spelling recognition with identity verification: whisper and ultrasonic features share a contrastively trained representation, then feed authentication and CTC spelling heads. This is a meaningful systems question, but the pilot results should not be reduced to the favorable 90.25% figure. Across all 11 participants, the reported Top-1 word accuracy is 67.3%; 90.25% applies only to eight users without degraded ultrasonic sensing, and the stated ReHEarSSE baseline is 91.4%. S5, S9, and S10 have below-10% recognition. Reported average authentication is 81.76% TPR and 3.2% FPR, with S9 and S10 near zero TPR; Figure 3(b) also disagrees with the prose about S5 TPR. The experiment holds out re-wearing sessions, but all participant identities appear in authentication training, so these are not unseen-attacker results. The private-key language refers to learned cross-modal similarity, not demonstrated cryptographic security, and replay or injection resistance is not tested. Finally, silent here includes whispering with subtle voice, and the commodity earbuds were modified and wired to a phone. The paper therefore supports a promising joint-model proof of concept, not a ready-to-use secure, fully silent interface.

### Why it matters

A preliminary demonstration that paired whisper and ultrasonic ear-canal signals can support a shared spelling/authentication pipeline, exposing that content-recognition success and identity-verification success can fail differently across users.

### Prior state of the art

The paper builds on ear-canal ultrasonic spelling recognition, particularly ReHEarSSE, and on earable biometric authentication. Its motivating gap is that decoding what was articulated does not by itself establish who articulated it.

### What changed

Pairs whisper mel-spectrogram features with autoregressive features of ultrasonic ear-canal motion, aligns them contrastively, and shares learned representations between a user-verification head and a letter-sequence spelling head.

### Position in the field

An exploratory earable SSI poster linking content decoding and biometric verification, with stronger value as a joint-model design and failure analysis than as evidence of deployable authentication security.

### Practical value

A research direction for verifying the identity behind low-audibility ear-based text entry. Practical value remains conditional on reliable sensing across users, explicit threat-model testing, reduced calibration burden, and a usable implementation.

### Advanced

Makes identity verification an explicit companion task to ear-based spelling recognition, using cross-modal alignment and a shared encoder rather than treating SSI solely as content decoding.

### Unresolved

Truly voiceless use, unseen words, unseen impostor identities, replay or signal-injection resistance, long-term and continuous verification, robustness to earbud replacement and placement, calibrated security operating points, and real-time end-to-end use.

### Narrowed or regressed

The added whisper stream does not establish aggregate recognition superiority: reported Top-1 is 67.3% across all 11 participants and 90.25% only for eight participants without degraded ultrasonic sensing, compared with a reported 91.4% ReHEarSSE baseline. Three users have below-10% recognition and two have near-zero genuine-user acceptance.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | text-entry; user authentication |
| Input | Low-frequency whisper audio plus 17.5–23 kHz ultrasonic reflections of ear-canal dynamic motion. The authors explicitly equate silent speech with whispering because participants produced subtle voice. |
| Sensor | Edifier W380NB active noise-canceling earbuds with the in-ear microphone detached from its circuitry and directly wired through a 3.5 mm jack to a Google Pixel 3a. Transmitted OFDM cycles contain 2046 samples at 48 kHz; ultrasonic band 17.5–23 kHz. |
| Body site | ear canal |
| Output | Spelled word text derived from 26 letter classes plus a CTC blank; separate binary user accept/reject decision. |
| Vocabulary type | Closed evaluation lexicon selected from frequent Oxford English Dictionary words; users spell letter names with subtle voice rather than freely dictating sentences. |
| Vocabulary size | 50 tested words; spelling output alphabet is 26 letters plus a CTC blank. |
| Metrics and results | Section 4.1.2 reports mean Top-1 word accuracy 67.3% across all 11 users; 90.25% only for eight without degraded ultrasonic sensing, alongside a 91.4% ReHEarSSE baseline. S5/S9/S10 recognition is below 10%. Reported mean authentication TPR is 81.76% and FPR 3.2%; S9/S10 have near-zero TPR. S5 TPR is inconsistent: 99.9% in prose versus 98.00% in Figure 3(b), with 3.4% FPR in both. EER is listed as a metric but no result is reported; the aggregate values above are reported, not independently reconciled. |
| Evaluation protocol | For each of 11 participants in turn, train a genuine-user-specific system and use the other ten as impostors. Hold out one randomly selected re-wearing session per participant. Evaluate Top-1/2/3 word accuracy against an implemented ReHEarSSE baseline and report per-user and average TPR/FPR for authentication, with 50 genuine and 500 impostor attempts per user model. Threshold selection uses Youden's J; the threshold-calibration data split is not clearly specified. |

### Limits

- **Technical:** Earbud placement and articulation are proposed causes of severe participant failures, not experimentally isolated explanations. Dependence on whisper features leaves strictly voiceless operation unvalidated. No component ablation establishes which loss or stream causes any gain. Authentication is a learned similarity decision, not a cryptographic key construction; inconsistent margin values and incomplete calibration details hinder reproduction.
- **Evaluation:** Small, predominantly male cohort; repeated closed 50-word lexicon; one held-out re-wearing session, not held-out identities. Authentication and contrastive components use all participants' identities in training and testing, while the SSI head uses only the genuine user's data. No replay/injection attack experiments, unseen-impostor protocol, confidence intervals, statistical significance tests, or isolated loss/component ablations are reported. EER is named but no numerical value is supplied. Figure 3(b) and prose disagree on S5 TPR, and the authentication margin has inconsistent specifications.
- **Deployment:** The experimental Edifier W380NB earbuds were modified: the in-ear microphone was removed from the earbud circuitry and wired directly to a Google Pixel 3a via a 3.5 mm jack for raw audio. The poster reports no end-to-end latency, power use, standalone earbud inference, walking test, or deployed communication study; per-user training uses other participants' data.
- **Scope of this review:** Eleven users, a repeated 50-word English lexicon, whispered letter spelling, and held-out re-wearing sessions. No unseen-word test, unrestricted dictation, fully voiceless validation, unseen-impostor test, replay/injection challenge, or clinical communication evaluation.

### Evidence

- HEar-ID proposes joint spelling and user verification from whisper audio and ultrasonic ear-canal reflections, with contrastive alignment and two task heads. The private-key wording describes the learned mapping rather than a specified cryptographic key-generation protocol. (Abstract and Section 1, PDF pp. 1–2; Section 3.2 and Figure 2, PDF pp. 2–3)
- The authors explicitly treat silent speech as whispering because participants still make subtle voice; the data-collection description also states that all participants spelled words with subtle voice. Fully voiceless operation is therefore not validated by this experiment. (Section 1, PDF p. 2; Section 4, PDF p. 4)
- The system uses 2046-sample OFDM cycles at 48 kHz, a 17.5–23 kHz ultrasonic band, 426 ms windows with 85 ms stride, 200-lag autoregressive ultrasonic features, and low-pass-filtered, downsampled whisper mel-spectrograms. (Section 3.1, PDF p. 2)
- The shared representation feeds an authentication branch with angular-triplet loss and a CTC spelling branch over 26 letters plus blank. Contrastive, authentication and CTC loss weights are 0.1, 0.5 and 0.3. The paper does not provide isolated component or loss ablations. (Sections 3.2–3.4 and Figure 2, PDF pp. 2–4; Section 4, PDF p. 4)
- The study has 11 users (ten reused ReHEarSSE participants and one recruit), nine male and two female, mean age 22. Each spelled four rounds of the same 50-word lexicon selected from 1000 frequent Oxford English Dictionary words. (Section 4, Preliminary Results, PDF p. 4)
- For each genuine-user model, one re-wearing session per participant is randomly selected for testing and the other sessions train the model. Authentication and CLWUM use all participant identities; the SSI head uses genuine-user data only. Each model receives 50 genuine and 500 other-participant impostor attempts at test time; this is session holdout, not unseen-impostor evaluation. (Section 4.1.1, Experiment Design, PDF p. 4)
- Reported Top-1 word accuracy is 67.3% across all 11 users and 90.25% only for eight users without degraded ultrasonic sensing; the stated ReHEarSSE baseline is 91.4%. S5, S9 and S10 are below 10%. The eight-user figure must not replace the all-user result or be described as outperforming the baseline. (Section 4.1.2, Silent-speech recognition, and Figure 3(a), PDF p. 4)
- Section 4.1.2 reports mean authentication TPR 81.76% and FPR 3.2%, with near-zero TPR for S9 and S10. The prose gives S5 TPR as 99.9%, but visually inspected Figure 3(b) labels S5 TPR 98.00%; both give S5 FPR 3.4%. These inconsistent S5 values are not reconciled by the paper. EER is named but no numerical EER is reported. (Section 4.1.2, Authentication, and Figure 3(b), PDF p. 4)
- Although described as commodity earbuds, the experimental Edifier W380NB setup removes the in-ear microphone from the earbud circuitry and wires it directly to a Google Pixel 3a through a 3.5 mm jack for unprocessed audio. The paper does not demonstrate unmodified standalone wireless-earbud inference. (Section 4, Preliminary Results, PDF p. 4)
- Section 3.3.1 describes the authentication margin m as 11.45 and later as 30 degrees. It states threshold calibration by Youden's J but does not clearly specify a separate calibration-data split; these details need clarification for faithful reproduction. (Section 3.3.1, User Authentication, PDF p. 3; Section 3.4, PDF p. 4)
- Replay and injection attacks motivate the introduction, but the experiment evaluates other cohort participants' attempts rather than replay or injection attacks. The poster reports neither an explicit evaluated attack protocol for those threats nor numerical real-time, power, walking, unseen-word or long-term continuous-verification results; expanding lexicons and refining continuous verification are future work. (Section 1, PDF p. 1; Sections 4–5 and Figure 3, PDF p. 4)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
