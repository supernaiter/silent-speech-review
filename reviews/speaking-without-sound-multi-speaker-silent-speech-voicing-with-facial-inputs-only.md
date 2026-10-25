# Speaking Without Sound: Multi-speaker Silent Speech Voicing with Facial Inputs Only

Jaejun Lee, Yoori Oh, Kyogu Lee  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2602.01879)

**Section:** [Surface EMG](../README.md#surface-emg) · **Review basis:** full_text+summary

Multi-speaker silent speech voicing from one user's EMG with target voices conditioned on facial images, without inference audio; pitch flattening modestly improves silent WER.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Existing facial/neck surface EMG plus target face image |
| Task | Speech synthesis from EMG |
| Vocabulary | Not stated |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Silent WER 38.91% with pitch flattening vs 40.12% without |

**Limitations.** Only one EMG participant; multi-user decoding and faithful personal-voice recovery not shown; main baseline is the same framework without flattening.

## Full review

### In short

Combines one users silent EMG with face-conditioned target voices without inference audio. Pitch flattening modestly helps silent word accuracy, but multi-user decoding and faithful personal-voice recovery are not demonstrated.

### Review

The contribution is an inference pipeline that does not need audible input: EMG supplies linguistic content and a face image supplies a target voice prior. Its multi-speaker label refers to synthesized target identities, however, while the EMG encoder is trained and tested on only one participant. The pitch-flattening intervention is plausible because audio-derived content targets can contain prosody that does not transfer cleanly from silent articulation. It lowers silent WER from 40.12% to 38.91% and CER from 26.14% to 24.28%, while worsening both voiced error measures; this is a mode-dependent trade-off rather than uniformly better content extraction. Objective target-voice similarity improves only slightly, and the silent score of 0.5657 remains close to the same-gender random reference of 0.5521. The reported paired tests support a difference but do not establish faithful recovery of a unique personal voice, especially when subjective consistency does not significantly improve. Local pitch also needs careful interpretation: it is evaluated using the EMG source speakers face, centered pitch contours and a voiced rendition aligned to the silent output by nearest interpolation. It therefore does not demonstrate exact prosody recovery for all sampled target identities or for an unobserved silent utterance. The study is a useful composition and target-preparation experiment, but evidence for new-user EMG operation, meaningful perceptual identity gains and practical communication remains limited.

### Why it matters

Shows how to remove audible reference requirements at inference and tests a simple pitch-target intervention that benefits silent more than voiced EMG.

### Prior state of the art

Prior EMG synthesizers can separate content and target voice but commonly require target audio. Face-based voice conversion supplies statistical voice cues; it cannot uniquely determine a persons original voice from facial appearance.

### What changed

Replaces source audio with an EMG-predicted ContentVec representation and target audio with face-conditioned identity/global pitch; pitch-flattens training speech to reduce target prosody mismatch.

### Position in the field

Contact-EMG content decoding with image-conditioned voice synthesis; one source EMG participant and many synthesized target identities.

### Practical value

A reference-audio-free option for selecting a plausible synthetic voice; current error rates and limited user validation prevent assuming communication readiness.

### Advanced

Enables face-conditioned target voices without target reference audio at inference; flattening improves reported silent WER/CER and pitch deviations over the same framework without flattening.

### Unresolved

New EMG users, actual voice recovery versus plausible face-conditioned output, independence of repeated target assignments, exact evaluation sample counts, optimizer/checkpoint reproducibility and complete latency.

### Narrowed or regressed

Flattening worsens voiced WER from 16.98% to 17.48% and voiced CER from 9.96% to 13.28%. Subjective consistency gains are not significant, and silent WER remains 38.91%.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | Silent or voiced surface EMG for content plus a target facial image for speaker identity and global pitch. Audio is needed for training targets and evaluation references. |
| Sensor | Existing Gaddy surface-EMG recordings from facial/neck electrodes plus 112 x 112 center-cropped target face images from LRS3. No new sensing hardware. |
| Body site | face;throat |
| Output | speech-audio |
| Vocabulary type | corpus utterance synthesis with variable target voices |
| Vocabulary size | Exact test lexicon not reported. |
| Metrics and results | Table I silent WER/CER 38.91%/24.28% with flattening versus 40.12%/26.14% without; voiced 17.48%/13.28% versus 16.98%/9.96%. Table II silent objective similarity 0.5657 versus 0.5626, same-gender random 0.5521; subjective consistency 3.29 versus 3.24 without significant difference. Table III silent local pitch deviation 17.93 versus 18.74, global pitch errors 24.80/30.83 Hz versus 28.91/36.45 Hz for male/female target groups. Author-reported, not independently reproduced. |
| Evaluation protocol | Offline voiced/silent EMG synthesis into sampled target-face voices, Whisper medium.en WER/CER, same-gender-controlled speaker similarity, face/voice consistency ratings and pitch deviations. |

### Limits

- **Technical:** Broad claims that silent EMG contains no pitch information are not directly tested. Praat PSOLA flattening does not prove complete representation disentanglement. DTW aligns silent inputs to a separate voiced target, and local-pitch evaluation uses nearest interpolation. Generated identity is statistically conditioned, not uniquely recoverable from a face.
- **Evaluation:** One EMG participant. Repeating target-face assignments ten times does not provide ten independently trained models or forty times as many independent source utterances. Main baseline is the same framework without flattening, not matched contemporary systems. Listener sample sizes and confidence intervals are omitted; paired t-test unit and dependence handling are unclear.
- **Deployment:** Requires contact EMG plus a facial image; inference is audio-free but training uses speech data. No portable implementation, streaming timing, longitudinal calibration or intended-user communication trial.
- **Scope of this review:** One-participant EMG benchmark, LRS3 target images and offline ratings; no multi-user EMG or clinical validation.

### Evidence

- Inference combines EMG-derived content with face-derived identity and global pitch; speech-based modules supply training targets, and pitch flattening precedes ContentVec extraction. (Section III and Figure 1; PDF pp. 1-3)
- The EMG dataset contains about twenty hours from a single speaker, while 50 male and 50 female LRS3 speakers provide target faces. Reviewer assessment: target-voice diversity is not multi-user EMG validation. (Sections IV-A and V; PDF pp. 3-4)
- Table I silent WER/CER improve from 40.12%/26.14% to 38.91%/24.28%, but voiced WER/CER worsen from 16.98%/9.96% to 17.48%/13.28%. (Table I; PDF p. 3)
- Table II silent objective similarity is 0.5657 with flattening versus 0.5626 without; the same-gender random-speaker reference is 0.5521. (Table II and Section IV-C2; PDF p. 4)
- Silent subjective face/voice consistency is 3.29 versus 3.24; the paper reports no significant subjective difference in either voiced or silent tests. (Table II and Section IV-C2; PDF p. 4)
- Table III silent local pitch deviation is 17.93 versus 18.74, while global errors are 24.80/30.83 Hz versus 28.91/36.45 Hz for male/female targets. (Table III; PDF p. 4)
- Local-pitch evaluation uses the source speakers face and the matching voiced rendition; nearest interpolation aligns silent-output and reference lengths. Reviewer assessment: this is not direct measurement of an unobserved silent acoustic target or all target voices. (Section IV-B3 and continuation; PDF pp. 3-4)
- Two targets from each gender group are sampled per source utterance across ten repetitions, yielding forty times as many synthesized assignments. Reviewer assessment: these are repeated source utterances, not forty times as much independent EMG evidence. (Section IV-A3; PDF p. 3)
- Pitch flattening is performed with Praat autocorrelation and PSOLA. Reviewer assessment: downstream ablation improvements do not by themselves demonstrate complete pitch disentanglement in the learned content embedding. (Section III-A4 and results; PDF pp. 2-4)
- The discussion explicitly recognizes one-speaker EMG data and treats multi-speaker EMG evaluation and stronger vocoding as future work. (Section V; PDF p. 4)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
