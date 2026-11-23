# A Parallel Ultra-Low Power Silent Speech Interface based on a Wearable, Fully-dry EMG Neckband

Fiona Meier, Giusy Spacone, Sebastian Frey, Luca Benini, Andrea Cossettini  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2509.21964)

**Section:** [Surface EMG](../../README.md#surface-emg) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

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

- [A Silent Speech Decoding System from EEG and EMG with Heterogenous Electrode Configurations](../a-silent-speech-decoding-system-from-eeg-and-emg-with-heterogenous-electrode-configurations/) (2025). Pooled EEG/EMG pretraining lifts 64-word accuracy, but each test subject's training sessions, the patient's included, are in pretraining; the coordinate kernel is neither new nor best.
- [Articulatory Feature Prediction from Surface EMG during Speech Production](../articulatory-feature-prediction-from-surface-emg-during-speech-production/) (2025). Articulatory route works on vocalized EMG but trails the mel baseline on WER; it exists for ECoG since 2019, and the electrode subset is never tested against equal-size alternatives.
- [CAT-Net: A Cross-Attention Tone Network for Cross-Subject EEG-EMG Fusion Tone Decoding](../cat-net-a-cross-attention-tone-network-for-cross-subject-eeg-emg-fusion-tone-decoding/) (2025). CAT-Net fuses EEG and surface EMG with cross-attention to classify Mandarin lexical tones in silent articulation, reporting 85.10% leave-one-subject-out accuracy over 4 tones.
- [Confidence-Based Self-Training for EMG-to-Speech: Leveraging Synthetic EMG for Robust Modeling](../confidence-based-self-training-for-emg-to-speech-leveraging-synthetic-emg-for-robust-modeling/) (2025). Synthetic EMG with confidence filtering (M03, standard) gives a small real-EMG gain, 23.30% to 21.87% WER on one speaker; large gains appear only on synthetic test EMG.
- [emg2speech: Synthesizing speech from electromyography using self-supervised speech models](../emg2speech-synthesizing-speech-from-electromyography-using-self-supervised-speech-models/) (2025). Ports a 2023 ECoG recipe (text-to-speech HuBERT units, CTC) to EMG; phoneme guidance (M02) and covariance input (M06) are standard. Table 6 mixes listener and decoder scoring, so it ranks no route.
- [From Silent Signals to Natural Language: A Dual-Stage Transformer-LLM Approach](../from-silent-signals-to-natural-language-a-dual-stage-transformer-llm-approach/) (2025). GPT-2 correction of one ASR transcript is neither first nor near the field: LLM correction of silent-EMG hypotheses already reached 12.2% WER on this benchmark; here 30% on ~100 utterances, one run.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
