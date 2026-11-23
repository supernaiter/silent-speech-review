# Subject-Independent Imagined Speech Detection via Cross-Subject Generalization and Calibration

Byung-Kwan Ko, Soowon Kim, Seo-Hyun Lee  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2511.13739)

**Section:** [Brain signals (EEG, MEG, intracortical)](../../README.md#brain-signals-eeg-meg-intracortical) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *Subject-Independent Imagined Speech Detection via Cross-Subject Generalization and Calibration* (Byung-Kwan Ko et al., arXiv 2025) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Detects imagined-speech versus rest states from 500 ms EEG windows in six subjects; accuracy rises from 67.0% (no subject data) to 78.1% with 10% subject calibration.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Scalp EEG (device and channels not stated) |
| Task | Imagined speech state detection (binary) |
| Vocabulary | 2 classes (speech state vs rest); no words |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Not stated |
| Key result | 78.1% accuracy with 10% self-calibration vs 67.0% strict LOSO, binary |

**Limitations.** Detects speech state, not words; six subjects, unclear splits and statistics, and no real-time, continuous or patient evaluation.


## More reviews in Brain signals (EEG, MEG, intracortical)

- [A Convolutional Framework for Mapping Imagined Auditory MEG into Listened Brain Responses](../a-convolutional-framework-for-mapping-imagined-auditory-meg-into-listened-brain-responses/) (2025). Mapping imagined onto listened MEG (M06) is ahead in design, but the subject-calibrated CNN gain is unproven: no ablation, a channel-shuffling null, and r 0.0113 against 0.0063.
- [An instantaneous voice-synthesis neuroprosthesis](../an-instantaneous-voice-synthesis-neuroprosthesis/) (2025). Closed-loop sentence voice from intracortical arrays holds for one participant; the design is standard, forced-choice and proxy-target metrics overstate intelligibility.
- [Brain-to-Text Decoding: A Non-invasive Approach via Typing](../brain-to-text-decoding-a-non-invasive-approach-via-typing/) (2025). Executed typing as the decoded action (M04) was ahead for MEG/EEG in 2025; keystroke-locked decoding (M06) and an n-gram LM (M07) are standard, and decoding needs known keystroke times.
- [Distinct Theta Synchrony across Speech Modes: Perceived, Spoken, Whispered, and Imagined](../distinct-theta-synchrony-across-speech-modes-perceived-spoken-whispered-and-imagined/) (2025). Exploratory comparison of EEG theta-band functional connectivity across perceived, spoken, whispered and imagined speech in ten healthy subjects; no recognition performance is measured.
- [EEG-to-Voice Decoding of Spoken and Imagined speech Using Non-Invasive EEG](../eeg-to-voice-decoding-of-spoken-and-imagined-speech-using-non-invasive-eeg/) (2025). Drops DTW from an EEG-to-Mel generator (M06, standard) but tests only the ten trained classes (M12, behind); one frozen ASR both trains and scores it, and EEG output beats recorded-speech WER.
- [Lightweight Diffusion-based Framework for Online Imagined Speech Decoding in Aphasia](../lightweight-diffusion-based-framework-for-online-imagined-speech-decoding-in-aphasia/) (2025). Diffusion EEG decoder (M06) standard: Diff-E lineage, no ablation, not smaller. Online use (M13) standard: one patient, 20 trials. M12: Table I overall row disagrees with class rows.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
