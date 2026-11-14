# Non-invasive electromyographic speech neuroprosthesis: a geometric perspective

Harshavardhana T. Gowda, Lee M. Miller  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2502.05762)

**Section:** [Surface EMG](../../README.md#surface-emg) · **Review basis:** full_text+summary

A structured review of *Non-invasive electromyographic speech neuroprosthesis: a geometric perspective* (Harshavardhana T. Gowda and Lee M. Miller, arXiv 2025) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Decodes silently articulated sEMG into phoneme sequences and English text without alignment to recorded audio, using a geometric representation of multi-site muscle activity. One healthy participant: PER 48.47% and WER 73.53% on large vocabulary; WER 14% on a 67-word date task.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 31-electrode wet surface EMG on face, jaw, lips and neck |
| Task | Silent speech to text (phonemes and words) |
| Vocabulary | Large vocabulary (over 6500 words); also 67-word closed set and NATO code words |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | PER 48.47%, WER 73.53%, held-out sentences, one participant; WER 14% on 67-word closed set |

**Limitations.** Main result from one healthy participant with 31 gel electrodes, a stationary amplifier and manual segmentation; word decoding depends on a language model; streaming and day-to-day stability are untested.


## More reviews in Surface EMG

- [A Parallel Ultra-Low Power Silent Speech Interface based on a Wearable, Fully-dry EMG Neckband](../a-parallel-ultra-low-power-silent-speech-interface-based-on-a-wearable-fully-dry-emg-neckband/) (2025). A fully dry wearable EMG neckband with ultra-low-power BioGAP-Ultra classifies 8 silently articulated words for one healthy user at 68% accuracy, dropping to 54% on an unseen re-wearing session; acquisition plus BLE uses 22.2 mW.
- [A Silent Speech Decoding System from EEG and EMG with Heterogenous Electrode Configurations](../a-silent-speech-decoding-system-from-eeg-and-emg-with-heterogenous-electrode-configurations/) (2025). Jointly trains on EEG and EMG data with heterogeneous electrode configurations for silent Japanese 64-word classification, reaching 95.3% for eight healthy subjects and 54.5% for one patient (chance 1.6%).
- [Articulatory Feature Prediction from Surface EMG during Speech Production](../articulatory-feature-prediction-from-surface-emg-during-speech-production/) (2025). Predicts 12-dim articulatory features, pitch and loudness from vocalized-speech sEMG and resynthesizes audio with an articulatory synthesizer. Feature correlation is about 0.9 against audio-derived proxy targets, but WER is 15.5% versus 12.6% for the Gaddy baseline (one male speaker).
- [CAT-Net: A Cross-Attention Tone Network for Cross-Subject EEG-EMG Fusion Tone Decoding](../cat-net-a-cross-attention-tone-network-for-cross-subject-eeg-emg-fusion-tone-decoding/) (2025). CAT-Net fuses EEG and surface EMG with cross-attention to classify Mandarin lexical tones in silent articulation, reporting 85.10% leave-one-subject-out accuracy over 4 tones.
- [Confidence-Based Self-Training for EMG-to-Speech: Leveraging Synthetic EMG for Robust Modeling](../confidence-based-self-training-for-emg-to-speech-leveraging-synthetic-emg-for-robust-modeling/) (2025). Uses confidence-filtered synthetic EMG generated from speech, mixed with real data, for EMG-to-speech; on real vocalized EMG from one speaker, WER falls from 23.30% to 21.87%.
- [emg2speech: Synthesizing speech from electromyography using self-supervised speech models](../emg2speech-synthesizing-speech-from-electromyography-using-self-supervised-speech-models/) (2025). emg2speech synthesizes speech from face and neck surface EMG via HuBERT units without the user's own recordings; silent speech from one ALS participant gives 50.82% human-transcribed WER.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
