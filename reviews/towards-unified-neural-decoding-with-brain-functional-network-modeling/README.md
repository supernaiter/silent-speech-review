# Towards Unified Neural Decoding with Brain Functional Network Modeling

Di Wu, Linghao Bu, Yifei Jia, Lu Cao, Siyuan Li, Siyu Chen, Yueqian Zhou, Sheng Fan, Wenjie Ren, Dengchang Wu, Kang Wang, Yue Zhang, Yuehui Ma, Jie Yang, Mohamad Sawan  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2506.12055)

**Section:** [Brain signals (EEG, MEG, intracortical)](../../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text+summary

A structured review of *Towards Unified Neural Decoding with Brain Functional Network Modeling* (Di Wu et al., arXiv 2025) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Shared training across intracranial sEEG with differing electrode layouts improves 23-class initial-sound classification for vocalized and silent (mouthed) Mandarin speech, but accuracy drops on unseen subjects.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Implanted stereo-EEG depth electrodes |
| Task | Closed-set initial-sound classification |
| Vocabulary | 23 classes (21 consonants plus i, u) |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Both |
| Key result | Shared training gains of 5.10% / 4.97% (silent offline, participants 10/11) |

**Limitations.** Only five silent and two online participants, random sample splits, reduced unseen-subject accuracy, and bedside setup with implanted electrodes.


## More reviews in Brain signals (EEG, MEG, intracortical)

- [A Convolutional Framework for Mapping Imagined Auditory MEG into Listened Brain Responses](../a-convolutional-framework-for-mapping-imagined-auditory-meg-into-listened-brain-responses/) (2025). Maps imagined auditory MEG (melodies and poems) to listened-response MEG; 8-condition classification reaches 50.7% (chance 12.5%), and calibrated cross-subject CNN beats shuffled controls, but correlations are small.
- [A cross-species neural foundation model for end-to-end speech decoding](../a-cross-species-neural-foundation-model-for-end-to-end-speech-decoding/) (2025). Introduces a cross-species self-supervised transformer encoder for Utah-array spiking data combined with audio-LLM end-to-end decoding, reporting state-of-the-art Brain-to-Text benchmark accuracy and imagined speech decoding.
- [An instantaneous voice-synthesis neuroprosthesis](../an-instantaneous-voice-synthesis-neuroprosthesis/) (2025). Intracortical BCI synthesizes a man with ALS's voice instantaneously with closed-loop audio feedback and prosody control; closed-set listener matching 94.34%, mimed and vocalized attempts decoded similarly.
- [Brain-to-Text Decoding: A Non-invasive Approach via Typing](../brain-to-text-decoding-a-non-invasive-approach-via-typing/) (2025). Brain2Qwerty decodes sentences typed from memory using non-invasive MEG/EEG; average CER 32% with MEG (best participant 19%) versus 67% with EEG, in 35 healthy typists.
- [Distinct Theta Synchrony across Speech Modes: Perceived, Spoken, Whispered, and Imagined](../distinct-theta-synchrony-across-speech-modes-perceived-spoken-whispered-and-imagined/) (2025). Exploratory comparison of EEG theta-band functional connectivity across perceived, spoken, whispered and imagined speech in ten healthy subjects; no recognition performance is measured.
- [EEG-to-Voice Decoding of Spoken and Imagined speech Using Non-Invasive EEG](../eeg-to-voice-decoding-of-spoken-and-imagined-speech-using-non-invasive-eeg/) (2025). Reconstructs cued overt and imagined speech audio and text from 130-channel wet EEG with subject-specific models; imagined-speech WER is 47.48% (2 s) and 43.46% (4 s) before language correction.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
