# AESSI: An Around-Ear Silent Speech Interface for Cross-Day Online Reuse without Test-Day Calibration

Xiran Xu, Mochu Dong, Yujie Yan, Chenxi Wang, Yu Jiao, Jing Chen  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2609.21436)

**Section:** [Surface EMG](../../README.md#surface-emg) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *AESSI: An Around-Ear Silent Speech Interface for Cross-Day Online Reuse without Test-Day Calibration* (Xiran Xu et al., arXiv 2026) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Around-ear cEEGrid system recognizing 25 fixed Mandarin sentences from silent articulation without test-day calibration; 92.24% mean accuracy on held-out later-day sessions and 98.00% in 250 live trials 21+ days later.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Bilateral around-ear cEEGrid electrodes (mixed EMG/EEG), 18 channels |
| Task | Closed-set sentence recognition |
| Vocabulary | 25 fixed Mandarin sentences |
| Speaker | Both |
| Session | Cross-day |
| Online / offline | Both |
| Key result | 92.24% accuracy, cross-day held-out sessions, no test-day calibration, chance 4%; 98.00% live (245/250) |

**Limitations.** Closed 25-sentence set only; mixed signal sources not separated; open-vocabulary conversation, walking, noise, long wear and patient use untested; live test used a single seed.


## More reviews in Surface EMG

- [A 1000-hour EEG-EMG-audio dataset of Japanese speech production](../a-1000-hour-eeg-emg-audio-dataset-of-japanese-speech-production/) (2026). A 1020-hour EEG-EMG-audio dataset of Japanese overt speech from three participants, with signal-quality and physiological validation but no decoding benchmarks.
- [Affect Decoding in Phonated and Silent Speech Production from Surface EMG](../affect-decoding-in-phonated-and-silent-speech-production-from-surface-emg/) (2026). Affect decoded from silent-articulation EMG, a design absent from 99 ledger studies (M08, ahead); it works within subject, nears chance across speakers, and is not separated from facial expression.
- [Comparison of sEMG Encoding Accuracy Across Speech Modes Using Articulatory and Phoneme Features](../comparison-of-semg-encoding-accuracy-across-speech-modes-using-articulatory-and-phoneme-features/) (2026). Applies an ECoG articulatory-versus-phoneme encoding comparison (Chartier 2018) to sEMG in three speech modes; the gain is small, mode contrasts are confounded, and no decoder is tested.
- [Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading](../cross-modal-masking-for-robust-silent-speech-synthesis-using-semg-and-lipreading/) (2026). Speech synthesis from fused sEMG and lip video is new to the ledger (M05, ahead); span masking (M03) adds a non-significant clean gain; seen speakers only (M12, behind).
- [CS-ETS: Chaos-Inspired Samba-Based EMG-To-Speech Synthesis with Nonlinear Chaotic Losses](../cs-ets-chaos-inspired-samba-based-emg-to-speech-synthesis-with-nonlinear-chaotic-losses/) (2026). Smaller chaos-inspired Samba-based EMG-to-speech model with nonlinear losses; WER improves modestly from 42.20% to 41.26% while parameters drop from 54.10M to 32.03M.
- [EMG-to-Speech with Fewer Channels](../emg-to-speech-with-fewer-channels/) (2026). Halving EMG electrodes costs synthesis the same ~35% relative WER known from recognition; initialization helps, channel dropout does not, and a weak unrepeated baseline undercuts the ranking.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
