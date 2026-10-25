# Movement Detection of Tongue and Related Body Parts Using IR-UWB Radar

Sunghwa Lee, Younghoon Shin  
arXiv / imported corpus page 2022 · [DOI](https://doi.org/10.1109/ICTC55196.2022.9952644) · [arXiv](https://arxiv.org/abs/2209.01762)

**Section:** [Radar, RF & Wi-Fi](../README.md#radar-rf--wi-fi) · **Review basis:** full_text

Uses IR-UWB radar aimed at the chin to detect hidden tongue movement states, achieving at least 90% accuracy for each of four participants on a binary task.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | IR-UWB radar with sinuous antennas and dielectric lens |
| Task | Binary tongue-movement classification |
| Vocabulary | 2 classes |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | >=90% accuracy per participant, 2 tongue states, 4 participants |

**Limitations.** Only two states, four participants, manual trial boundaries, stationary lab setup; no continuous speech, unseen-user, or vocabulary-level tests.

## Full review

### In short

Good sensing primitive, very small task.

### Review

The claim should stay narrow. The experimental section describes only two states: tongue resting on the floor of the mouth and a tongue-tip movement touching the palate before returning. Table I shows the proposed feature extraction plus GMM-HMM reaching 100/90/90/90 accuracy across the four participants, beating both CLEAN-based baselines. That is enough to take radar seriously as a contactless oral-motion sensor. It is not enough to claim word recognition, phoneme decoding, or robust silent-speech interaction because the entire study is four people, two states, short 1-3 second recordings, and manually delimited trials.

### Why it matters

The full text supports a narrow but real result: radar can detect simple invisible tongue movement states with at least 90% accuracy for each of four participants.

### Prior state of the art

Most SSI sensing work relied on contact sensors, audio, ultrasound, or visible articulators rather than contactless radar pointed under the chin.

### What changed

The paper strips the problem down to a binary tongue-motion detection task and shows radar can separate the two states without contact.

### Position in the field

Early contactless radar sensing paper for SSI-adjacent tongue-motion detection, not full speech decoding.

### Practical value

Useful as a proof that a non-contact radar sensor can sense hidden oral motion before anyone tries larger-vocabulary SSI on the same hardware.

### Advanced

sensor modality; contactless oral-motion sensing

### Unresolved

continuous articulation; larger vocabularies; user generalization

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-recognition |
| Input | IR-UWB radar pointed at the chin |
| Sensor | IR-UWB radar module with LNA evaluation board, sinuous antennas, and dielectric lens |
| Body site | tongue; chin |
| Output | labels |
| Vocabulary type | binary tongue-state classification |
| Vocabulary size | 2 classes |
| Metrics and results | classification accuracy by participant |
| Evaluation protocol | leave-one-out cross-validation against CLEAN+MD-DTW baselines on two tongue-motion states |

### Limits

- **Technical:** Only two states, four participants, manual trial boundaries, and a stationary lab setup are tested.
- **Evaluation:** No continuous speech, no unseen-user split, and no vocabulary-level recognition are reported.
- **Deployment:** The hardware is promising but far from a complete radar SSI system.
- **Scope of this review:** Binary tongue-motion detection only.

### Evidence

- The abstract states that the study classifies motionless and moving states of an invisible tongue using an IR-UWB radar pointed toward the participant's chin. (Abstract)
- Section A says the experiment uses four participants, two tongue-motion states, and twenty repetitions of each state per participant. (A. Experimental Environment)
- Section B explains that the proposed method turns radar frame sets into envelope features and classifies them with a five-state left-to-right GMM-HMM. (B. Feature Extraction and Classifier Selection)
- Table I reports participant-wise classification accuracy of 100, 90, 90, and 90 percent for the proposed feature extraction plus GMM-HMM pipeline. (TABLE I)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
