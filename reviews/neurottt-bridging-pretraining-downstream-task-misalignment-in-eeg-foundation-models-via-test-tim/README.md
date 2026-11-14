# NeuroTTT: Bridging Pretraining-Downstream Task Misalignment in EEG Foundation Models via Test-Time Training

Suli Wang, Yangshen Deng, Zhenghua Bao, Xinyu Zhan, Yiqun Duan  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2509.26301)

**Section:** [Brain signals (EEG, MEG, intracortical)](../../README.md#brain-signals-eeg-meg-intracortical) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *NeuroTTT: Bridging Pretraining-Downstream Task Misalignment in EEG Foundation Models via Test-Time Training* (Suli Wang et al., arXiv 2025) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

NeuroTTT adds task-specific self-supervision and test-time training to EEG foundation models, raising within-subject 5-class imagined speech balanced accuracy for CBraMod to 58.98%.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 64-channel scalp EEG (existing dataset) |
| Task | Closed-set imagined speech classification |
| Vocabulary | 5 phrases (hello, help me, stop, thank you, yes) |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Balanced accuracy 58.98% (CBraMod, TTT with Tent), within-subject, 5 classes |

**Limitations.** Within-subject only for imagined speech, needs labeled user data, and participant counts, splits and statistical tests are unclear.


## More reviews in Brain signals (EEG, MEG, intracortical)

- [A Convolutional Framework for Mapping Imagined Auditory MEG into Listened Brain Responses](../a-convolutional-framework-for-mapping-imagined-auditory-meg-into-listened-brain-responses/) (2025). Maps imagined auditory MEG (melodies and poems) to listened-response MEG; 8-condition classification reaches 50.7% (chance 12.5%), and calibrated cross-subject CNN beats shuffled controls, but correlations are small.
- [A cross-species neural foundation model for end-to-end speech decoding](../a-cross-species-neural-foundation-model-for-end-to-end-speech-decoding/) (2025). Introduces a cross-species self-supervised transformer encoder for Utah-array spiking data combined with audio-LLM end-to-end decoding, reporting state-of-the-art Brain-to-Text benchmark accuracy and imagined speech decoding.
- [An instantaneous voice-synthesis neuroprosthesis](../an-instantaneous-voice-synthesis-neuroprosthesis/) (2025). Intracortical BCI synthesizes a man with ALS's voice instantaneously with closed-loop audio feedback and prosody control; closed-set listener matching 94.34%, mimed and vocalized attempts decoded similarly.
- [Brain-to-Text Decoding: A Non-invasive Approach via Typing](../brain-to-text-decoding-a-non-invasive-approach-via-typing/) (2025). Brain2Qwerty decodes sentences typed from memory using non-invasive MEG/EEG; average CER 32% with MEG (best participant 19%) versus 67% with EEG, in 35 healthy typists.
- [Distinct Theta Synchrony across Speech Modes: Perceived, Spoken, Whispered, and Imagined](../distinct-theta-synchrony-across-speech-modes-perceived-spoken-whispered-and-imagined/) (2025). Exploratory comparison of EEG theta-band functional connectivity across perceived, spoken, whispered and imagined speech in ten healthy subjects; no recognition performance is measured.
- [EEG-to-Voice Decoding of Spoken and Imagined speech Using Non-Invasive EEG](../eeg-to-voice-decoding-of-spoken-and-imagined-speech-using-non-invasive-eeg/) (2025). Reconstructs cued overt and imagined speech audio and text from 130-channel wet EEG with subject-specific models; imagined-speech WER is 47.48% (2 s) and 43.46% (4 s) before language correction.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
