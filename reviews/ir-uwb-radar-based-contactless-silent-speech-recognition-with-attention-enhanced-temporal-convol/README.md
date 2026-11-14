# IR-UWB Radar-Based Contactless Silent Speech Recognition with Attention-Enhanced Temporal Convolutional Networks

Sunghwa Lee, Jaewon Yu  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2509.26409)

**Section:** [Radar, RF & Wi-Fi](../../README.md#radar-rf--wi-fi) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *IR-UWB Radar-Based Contactless Silent Speech Recognition with Attention-Enhanced Temporal Convolutional Networks* (Sunghwa Lee and Jaewon Yu, arXiv 2025) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Contactless IR-UWB radar in front of the lips with an attention-enhanced TCN classifies 50 English words for one user at 91.1% mean accuracy, versus 74.0% for a hand-crafted baseline.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Novelda IR-UWB radar near lips (5-10 cm) |
| Task | Isolated word recognition |
| Vocabulary | 50 English words |
| Speaker | Speaker-dependent |
| Session | Cross-session |
| Online / offline | Not stated |
| Key result | 91.1% mean accuracy, 50 words, leave-one-session-out (baseline 74.0%) |

**Limitations.** Single participant, requires alignment before each utterance, no ablations or statistics, and no unseen users, words or free posture tested.


## More reviews in Radar, RF & Wi-Fi

- [Articulatory movements influence electromagnetic wave transmission through the vocal tract](../articulatory-movements-influence-electromagnetic-wave-transmission-through-the-vocal-tract/) (2026). Physical modeling and measurement of contact RF transmission through the vocal tract for three sustained vowels in two participants; simulations qualitatively agree with measurements below about 3 GHz.
- [Lip-Siri: Contactless Open-Sentence Silent Speech with Wi-Fi Backscatter](../lip-siri-contactless-open-sentence-silent-speech-with-wi-fi-backscatter/) (2026). Lip-Siri senses lip motion contactlessly with Wi-Fi frequency-shifted backscatter and decodes lexicon-constrained sentences, reporting 85.61% word accuracy and 36.87% sentence WER on a random 80/20 split plus three held-out users.
- [IR-UWB Radar-Based Contactless Silent Speech Recognition of Vowels, Consonants, Words, and Phrases](../ir-uwb-radar-based-contactless-silent-speech-recognition-of-vowels-consonants-words-and-phrases/) (2023). Proposes FERASEC feature extraction for contactless IR-UWB radar silent speech recognition of vowels, consonants, words and phrases. With the upper radar and DNN-HMM it reports 86.47% vowel and 81.59% consonant accuracy.
- [Movement Detection of Tongue and Related Body Parts Using IR-UWB Radar](../movement-detection-of-tongue-and-related-body-parts-using-ir-uwb-radar/) (2022). Uses IR-UWB radar aimed at the chin to detect hidden tongue movement states, achieving at least 90% accuracy for each of four participants on a binary task.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
