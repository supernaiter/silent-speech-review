# A Parallel Ultra-Low Power Silent Speech Interface based on a Wearable, Fully-dry EMG Neckband

Fiona Meier, Giusy Spacone, Sebastian Frey, Luca Benini, Andrea Cossettini  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2509.21964)

**Section:** [Surface EMG](../../README.md#surface-emg) · **Review basis:** full_text+summary

A structured review of *A Parallel Ultra-Low Power Silent Speech Interface based on a Wearable, Fully-dry EMG Neckband* (Fiona Meier et al., arXiv 2025) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

A fully dry wearable EMG neckband with ultra-low-power BioGAP-Ultra classifies 8 silently articulated words for one healthy user at 68% accuracy, dropping to 54% on an unseen re-wearing session; acquisition plus BLE uses 22.2 mW.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Dry-electrode textile neckband, 14-channel EMG |
| Task | Closed-set command word classification |
| Vocabulary | 8 commands |
| Speaker | Speaker-dependent |
| Session | Cross-session |
| Online / offline | Not stated |
| Key result | Silent 68% (pooled 5-fold), 54% leave-one-session-out, chance 12.5% |

**Limitations.** Single participant, cue-aligned 1.4 s segments, no on-device inference reported, and no walking, natural conversation or patient testing.


## More reviews in Surface EMG

- [A Silent Speech Decoding System from EEG and EMG with Heterogenous Electrode Configurations](../a-silent-speech-decoding-system-from-eeg-and-emg-with-heterogenous-electrode-configurations/) (2025). Jointly trains on EEG and EMG data with heterogeneous electrode configurations for silent Japanese 64-word classification, reaching 95.3% for eight healthy subjects and 54.5% for one patient (chance 1.6%).
- [Articulatory Feature Prediction from Surface EMG during Speech Production](../articulatory-feature-prediction-from-surface-emg-during-speech-production/) (2025). Predicts 12-dim articulatory features, pitch and loudness from vocalized-speech sEMG and resynthesizes audio with an articulatory synthesizer. Feature correlation is about 0.9 against audio-derived proxy targets, but WER is 15.5% versus 12.6% for the Gaddy baseline (one male speaker).
- [CAT-Net: A Cross-Attention Tone Network for Cross-Subject EEG-EMG Fusion Tone Decoding](../cat-net-a-cross-attention-tone-network-for-cross-subject-eeg-emg-fusion-tone-decoding/) (2025). CAT-Net fuses EEG and surface EMG with cross-attention to classify Mandarin lexical tones in silent articulation, reporting 85.10% leave-one-subject-out accuracy over 4 tones.
- [Confidence-Based Self-Training for EMG-to-Speech: Leveraging Synthetic EMG for Robust Modeling](../confidence-based-self-training-for-emg-to-speech-leveraging-synthetic-emg-for-robust-modeling/) (2025). Uses confidence-filtered synthetic EMG generated from speech, mixed with real data, for EMG-to-speech; on real vocalized EMG from one speaker, WER falls from 23.30% to 21.87%.
- [emg2speech: Synthesizing speech from electromyography using self-supervised speech models](../emg2speech-synthesizing-speech-from-electromyography-using-self-supervised-speech-models/) (2025). emg2speech synthesizes speech from face and neck surface EMG via HuBERT units without the user's own recordings; silent speech from one ALS participant gives 50.82% human-transcribed WER.
- [From Silent Signals to Natural Language: A Dual-Stage Transformer-LLM Approach](../from-silent-signals-to-natural-language-a-dual-stage-transformer-llm-approach/) (2025). Corrects transcripts of speech synthesized from silent EMG (Digital Voicing data) with a Transformer recognizer and GPT-2, reducing WER from 36% to 30% on about 100 utterances.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
