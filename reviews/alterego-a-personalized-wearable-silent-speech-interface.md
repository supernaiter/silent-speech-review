# AlterEgo: A Personalized Wearable Silent Speech Interface

Arnav Kapur, Shreyas Kapur, Pattie Maes  
Proceedings of the 23rd International Conference on Intelligent User Interfaces (IUI '18), pp. 43-53 · [DOI](https://doi.org/10.1145/3172944.3172977)

**Section:** [Surface EMG](../README.md#surface-emg) · **Review basis:** abstract+secondary_sources

A structured review of *AlterEgo: A Personalized Wearable Silent Speech Interface* (Arnav Kapur et al., Proceedings of the 23rd International Conference on Intelligent User Interfaces (IUI '18), pp. 43-53) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Wearable headset that recognizes silently articulated words from face and jaw neuromuscular signals and answers through bone-conduction audio; abstract reports 92% median word accuracy in user studies.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Head-worn surface EMG electrodes on face and jaw, with bone-conduction headphones |
| Task | Closed-vocabulary silent word/command recognition |
| Vocabulary | Small task vocabularies (about 20 words per application, per MIT News) |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Not stated |
| Key result | 92% median word accuracy in user studies (abstract) |

**Limitations.** Small closed vocabularies and per-user customization; full protocol (splits, sessions, architecture) not verified because only the abstract and press coverage were available.

## Full review

### In short

Landmark wearable EMG SSI framed as a closed-loop assistant; headline accuracy rests on tiny task vocabularies.

### Review

AlterEgo is one of the most visible SSI papers because it packages surface neuromuscular sensing, a personalized recognizer and bone-conduction audio feedback into a single head-worn loop for talking to a computer without audible speech or visible movement. The abstract reports a 92% median word accuracy in user studies, and the MIT press release describes a 10-subject arithmetic study with about 15 minutes of per-user customization and task vocabularies of about 20 words. That makes the result a closed-vocabulary, per-user command/word recognition claim rather than evidence for open-vocabulary silent dictation. The full PDF could not be accessed for this review, so electrode-level details, model architecture, split design and cross-session behavior are taken from secondary sources or left unverified.

### Why it matters

Its lasting value is the interaction framing: a discreet, bidirectional silent-speech loop (silent input, bone-conduction output) built around personalization, not a new recognition benchmark.

### Prior state of the art

EMG silent speech recognition was mostly laboratory work with taped electrode arrays and offline evaluation, rarely framed as an always-available personal interface with private audio feedback.

### What changed

Integrates face/jaw neuromuscular sensing, a per-user recognizer and bone-conduction output into a wearable closed loop for querying computing services, and evaluates it with users on task-specific vocabularies.

### Position in the field

Highly cited HCI landmark for wearable EMG silent speech; frequently used as the reference point for 'intelligence augmentation' framing of SSI.

### Practical value

Useful as a design reference for discreet bidirectional SSI interaction; weak as a quantitative baseline because vocabularies are small and full protocol details are hard to compare.

### Advanced

interaction_design; wearable_form_factor; personalization

### Unresolved

Open vocabulary; cross-session and re-wear robustness; speaker independence; truly 'internal' versus articulated speech

### Evaluation details

| Item | Details |
| --- | --- |
| Task | command-recognition; speech-recognition |
| Input | surface neuromuscular (EMG) signals from face and jaw |
| Sensor | head-worn electrode headset with bone-conduction headphones |
| Body site | face; jaw |
| Output | text; commands |
| Vocabulary type | closed task-specific vocabulary |
| Vocabulary size | about 20 words per application (MIT News; not verified in full text) |
| Metrics and results | 92% median word accuracy in user studies (abstract); about 92% average transcription accuracy in a 10-subject arithmetic study (MIT News) |
| Evaluation protocol | user studies with per-user customization on task-specific vocabularies (details unverified) |

### Limits

- **Technical:** Recognition is personalized and reported on small task vocabularies (about 20 words per application according to MIT News); the abstract describes signals during 'internal' speech, but how much articulation is required is not verifiable from the sources seen.
- **Evaluation:** Only the 92% median word accuracy is verifiable from the abstract; split design, session separation and per-task breakdown could not be checked in the full text.
- **Deployment:** Requires a custom head-worn electrode headset in contact with the face and jaw and per-user customization.
- **Scope of this review:** Closed-vocabulary silent word/command recognition for human-computer interaction; not speech synthesis or open dictation.

### Evidence

- The abstract describes a wearable interface that captures neuromuscular signals from internal speech articulators, feeds reconstructed words to a computing system, and returns output via bone-conduction audio, enabling discreet bidirectional communication. (Abstract (MIT Media Lab publication page))
- The abstract reports a 92% median word accuracy in user studies. (Abstract (MIT Media Lab publication page))
- MIT News describes a 10-subject usability study in which each subject spent about 15 minutes customizing the arithmetic application and about 90 minutes using it, with about 92% average transcription accuracy and task vocabularies of about 20 words. (MIT News, 4 April 2018 (secondary source))
- MIT News states that an electrode-placement study started with 16 facial sites and the prototype uses seven contact points on either side of the mouth and along the jaws, with personalization by retraining the last two network layers. (MIT News, 4 April 2018 (secondary source))
- The full paper PDF could not be retrieved for this review, so architecture, split and cross-session details remain unverified. (Reviewer note)

## More reviews in Surface EMG

- [Development of sEMG sensors and algorithms for silent speech recognition](development-of-semg-sensors-and-algorithms-for-silent-speech-recognition.md) (2018). Face- and neck-worn sEMG sensors with staged recognition algorithms decode silently mouthed phrases; abstract reports 8.9% WER on 1,200+ phrases from a 2,200-word vocabulary.
- [Digital Voicing of Silent Speech](digital-voicing-of-silent-speech.md) (2020). Synthesizes speech from silent facial EMG by transferring audio targets from vocalized recordings; human WER reaches 3.6% on closed vocabulary, while open-vocabulary WER drops from 95.1% to 74.8%.
- [An Improved Model for Voicing Silent Speech](an-improved-model-for-voicing-silent-speech.md) (2021). Improves open-vocabulary silent-speech voicing from facial EMG using learned convolutional features, a Transformer and auxiliary phoneme loss, cutting WER from 68.0% to 42.2% (automatic) and 32.3% (human) for one speaker.
- [Sequence-to-Sequence Voice Reconstruction for Silent Speech in a Tonal Language](sequence-to-sequence-voice-reconstruction-for-silent-speech-in-a-tonal-language.md) (2022). SSRNet reconstructs Mandarin speech from five-channel facial sEMG using duration-aware Seq2Seq and tonal multitask learning, cutting ASR CER from 46.62% to 21.99% over the baseline.
- [Knowledge Distilled Ensemble Model for sEMG-based Silent Speech Interface](knowledge-distilled-ensemble-model-for-semg-based-silent-speech-interface.md) (2023). Distills a ResNet ensemble into a lightweight model for spelling via the NATO phonetic alphabet from 3-channel facial sEMG on portable hardware. KDE-SSI reaches 85.9% accuracy on 26 classes with 0.12 ms inference per sample.
- [A Parallel Ultra-Low Power Silent Speech Interface based on a Wearable, Fully-dry EMG Neckband](a-parallel-ultra-low-power-silent-speech-interface-based-on-a-wearable-fully-dry-emg-neckband.md) (2025). A fully dry wearable EMG neckband with ultra-low-power BioGAP-Ultra classifies 8 silently articulated words for one healthy user at 68% accuracy, dropping to 54% on an unseen re-wearing session; acquisition plus BLE uses 22.2 mW.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
