# Multi-Subject Pretraining Enables Short-Calibration Personalization for Closed-Corpus Surface EMG Speech Decoding

Chenqian Le, Beatrice Fumagalli, Yasamin Esmaeili, Xupeng Chen, Tianyu He, Nikasadat Emami, Adeen Flinker, Yao Wang  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2609.21288)

**Section:** [Surface EMG](../../README.md#surface-emg) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *Multi-Subject Pretraining Enables Short-Calibration Personalization for Closed-Corpus Surface EMG Speech Decoding* (Chenqian Le et al., arXiv 2026) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Multi-subject pretraining plus target fine-tuning for 8-channel face/neck sEMG decoding of a closed 50-sentence corpus (27 subjects, LOSO); 21.7% CER / 31.9% WER, with 3-minute calibration not significantly worse.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 8-channel lower-face/neck surface EMG |
| Task | Closed-corpus sEMG-to-text decoding |
| Vocabulary | 50 closed TIMIT-based sentences |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 21.7% CER / 31.9% WER, pretrain + fine-tune, closed 50 sentences; 78.6% CER on unseen sentences |

**Limitations.** Evaluation sentences can appear in other subjects' pretraining; performance collapses on unseen sentences; offline only, healthy adults, no latency or electrode re-donning tests.


## More reviews in Surface EMG

- [A 1000-hour EEG-EMG-audio dataset of Japanese speech production](../a-1000-hour-eeg-emg-audio-dataset-of-japanese-speech-production/) (2026). A 1020-hour EEG-EMG-audio dataset of Japanese overt speech from three participants, with signal-quality and physiological validation but no decoding benchmarks.
- [AESSI: An Around-Ear Silent Speech Interface for Cross-Day Online Reuse without Test-Day Calibration](../aessi-an-around-ear-silent-speech-interface-for-cross-day-online-reuse-without-test-day-calibrat/) (2026). Around-ear cEEGrid system recognizing 25 fixed Mandarin sentences from silent articulation without test-day calibration; 92.24% mean accuracy on held-out later-day sessions and 98.00% in 250 live trials 21+ days later.
- [Affect Decoding in Phonated and Silent Speech Production from Surface EMG](../affect-decoding-in-phonated-and-silent-speech-production-from-surface-emg/) (2026). Affect decoded from silent-articulation EMG, a design absent from 99 ledger studies (M08, ahead); it works within subject, nears chance across speakers, and is not separated from facial expression.
- [Comparison of sEMG Encoding Accuracy Across Speech Modes Using Articulatory and Phoneme Features](../comparison-of-semg-encoding-accuracy-across-speech-modes-using-articulatory-and-phoneme-features/) (2026). Applies an ECoG articulatory-versus-phoneme encoding comparison (Chartier 2018) to sEMG in three speech modes; the gain is small, mode contrasts are confounded, and no decoder is tested.
- [Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading](../cross-modal-masking-for-robust-silent-speech-synthesis-using-semg-and-lipreading/) (2026). Speech synthesis from fused sEMG and lip video is new to the ledger (M05, ahead); span masking (M03) adds a non-significant clean gain; seen speakers only (M12, behind).
- [CS-ETS: Chaos-Inspired Samba-Based EMG-To-Speech Synthesis with Nonlinear Chaotic Losses](../cs-ets-chaos-inspired-samba-based-emg-to-speech-synthesis-with-nonlinear-chaotic-losses/) (2026). Smaller chaos-inspired Samba-based EMG-to-speech model with nonlinear losses; WER improves modestly from 42.20% to 41.26% while parameters drop from 54.10M to 32.03M.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
