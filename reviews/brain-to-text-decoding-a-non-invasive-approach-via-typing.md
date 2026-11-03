# Brain-to-Text Decoding: A Non-invasive Approach via Typing

Jarod Lévy, Mingfang (Lucy) Zhang, Svetlana Pinet, Jérémy Rapin, Hubert Banville, Stéphane d'Ascoli, Jean-Rémi King  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2502.17480)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text

A structured review of *Brain-to-Text Decoding: A Non-invasive Approach via Typing* (Jarod Lévy et al., arXiv 2025) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Brain2Qwerty decodes sentences typed from memory using non-invasive MEG/EEG; average CER 32% with MEG (best participant 19%) versus 67% with EEG, in 35 healthy typists.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Non-invasive MEG and EEG during typing |
| Task | Brain-to-text decoding of typed sentences |
| Vocabulary | Spanish sentences of 5-8 words; 128 per session |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | CER 32% MEG average (19% best), 67% EEG |

**Limitations.** Typing not speech; offline with keystroke alignment; healthy participants; MEG not wearable.

## Full review

### In short

Brain2Qwerty decodes typed sentences from non-invasive MEG at 32% CER on average (19% best participant), far better than EEG (67%), but it decodes typing motor activity offline, not speech.

### Review

Brain2Qwerty is a non-invasive brain-to-text system that sidesteps speech entirely: 35 healthy skilled typists memorized short Spanish sentences and typed them on a QWERTY keyboard while MEG or EEG was recorded. A convolutional module (adapted from Défossez et al. 2023) encodes 0.5 s windows aligned to keystrokes, a sentence-level transformer contextualizes them, and a 9-gram character language model corrects the output. Average CER was 32% with MEG (best 19%, worst 45%) versus 67% with EEG, and Brain2Qwerty improved CER 2.25-fold over EEGNet with MEG. Error structure follows keyboard distance (R = 0.73), and correctly typed characters are decoded better than mistyped ones, indicating heavy reliance on motor signals. Sentence splits are clustered by TF-IDF similarity to avoid near-duplicate leakage. For an SSI review this is an adjacent non-invasive text-entry baseline: it highlights the MEG-EEG gap and the importance of a language model, but it needs keystroke-aligned segments, full-trial context (no real-time), actual hand movements, and a non-wearable MEG system.

### Why it matters

Best-documented non-invasive brain-to-text sentence decoding to date in this set, quantifying what MEG and EEG can deliver for typing-based communication.

### Prior state of the art

Non-invasive BCIs for text relied on slow evoked-potential spellers or small-vocabulary decoding; sentence-level non-invasive decoding was rare.

### What changed

Sentence-level character decoding from MEG/EEG during natural typing with a conv-transformer-LM pipeline and clustering-based train/test splits.

### Position in the field

Non-invasive text-entry neighbour of speech BCIs in the brain section; not a speech or silent-speech interface.

### Practical value

Benchmark numbers for MEG vs EEG text decoding and an architecture reusable for production tasks; clinical use for locked-in users remains untested.

### Advanced

Non-invasive sentence-level text decoding accuracy; dataset scale for typing-aligned M/EEG.

### Unresolved

Real-time decoding; users who cannot move their hands; wearable sensing; speech production.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | Decode typed sentences (characters) from MEG/EEG recorded during typing from memory. |
| Input | Non-invasive MEG and EEG aligned to keystrokes. |
| Sensor | Whole-head MEG and scalp EEG (system details not extracted), custom MR-compatible QWERTY keyboard. |
| Body site | Brain (scalp-recorded MEG/EEG). |
| Output | Text (characters/sentences). |
| Vocabulary type | Spanish declarative sentences of 5-8 words; TF-IDF clustered 80/10/10 splits. |
| Vocabulary size | 128 unique sentences per session; EEG about 4K sentences (146K characters), MEG 5.1K sentences (193K characters). |
| Metrics and results | CER: MEG 32% +/- 0.6 average (best 19%, worst 45%); EEG 67% +/- 1.5 (best 61%, worst 71%); MEG > EEG p < 1e-8. Improvement over EEGNet 1.14x (EEG) and 2.25x (MEG). Keyboard-distance vs confusion R = 0.73. Typing errors 3.6-3.9% of keystrokes. |
| Evaluation protocol | Offline, held-out sentence clusters, with linear ridge and EEGNet baselines. |

### Limits

- **Technical:** Requires keystroke-aligned M/EEG segments and full-trial context; supervised training only.
- **Evaluation:** Healthy skilled typists; Spanish sentences of 5-8 words; baseline CERs reported only as fold improvements in text; hand-typing error rate given mainly in figures.
- **Deployment:** MEG system used is not wearable; not real-time; relies on actual hand movements.
- **Scope of this review:** Read arXiv v1 HTML via automated extraction; figure-only values (hand error rate, per-participant curves) not inspected. Venue beyond arXiv not verified.

### Evidence

- 35 healthy right-handed skilled typists; 20 recorded with EEG and 20 with MEG (five did both); Spanish sentences of 5-8 words typed from memory without visual feedback. (Methods, Participants and Task)
- Brain2Qwerty: convolutional module on 0.5 s M/EEG windows, sentence-level transformer, and a pretrained 9-gram character KenLM. (Methods, Model)
- Average CER was 32% +/- 0.6 with MEG (best 19%, worst 45%) and 67% +/- 1.5 with EEG (best 61%, worst 71%). (Results; CER table)
- Relative to EEGNet, Brain2Qwerty improved CER 1.14-fold with EEG and 2.25-fold with MEG. (Results, Baselines)
- Sentences were split 80/10/10 using TF-IDF clustering so similar sentences stay in the same split. (Methods, Data splits)
- Decoder confusions track physical keyboard distance (R = 0.73, p = 0.02), indicating reliance on motor processes. (Results, Motor vs higher-level)
- Not real-time (needs full trial), requires keystroke-aligned segments, tested only on healthy participants, and the MEG is not wearable. (Discussion, Limitations)

## More reviews in Brain signals (EEG, MEG, intracortical)

- [A Convolutional Framework for Mapping Imagined Auditory MEG into Listened Brain Responses](a-convolutional-framework-for-mapping-imagined-auditory-meg-into-listened-brain-responses.md) (2025). Maps imagined auditory MEG (melodies and poems) to listened-response MEG; 8-condition classification reaches 50.7% (chance 12.5%), and calibrated cross-subject CNN beats shuffled controls, but correlations are small.
- [A cross-species neural foundation model for end-to-end speech decoding](a-cross-species-neural-foundation-model-for-end-to-end-speech-decoding.md) (2025). Introduces a cross-species self-supervised transformer encoder for Utah-array spiking data combined with audio-LLM end-to-end decoding, reporting state-of-the-art Brain-to-Text benchmark accuracy and imagined speech decoding.
- [An instantaneous voice-synthesis neuroprosthesis](an-instantaneous-voice-synthesis-neuroprosthesis.md) (2025). Intracortical BCI synthesizes a man with ALS's voice instantaneously with closed-loop audio feedback and prosody control; closed-set listener matching 94.34%, mimed and vocalized attempts decoded similarly.
- [Distinct Theta Synchrony across Speech Modes: Perceived, Spoken, Whispered, and Imagined](distinct-theta-synchrony-across-speech-modes-perceived-spoken-whispered-and-imagined.md) (2025). Exploratory comparison of EEG theta-band functional connectivity across perceived, spoken, whispered and imagined speech in ten healthy subjects; no recognition performance is measured.
- [EEG-to-Voice Decoding of Spoken and Imagined speech Using Non-Invasive EEG](eeg-to-voice-decoding-of-spoken-and-imagined-speech-using-non-invasive-eeg.md) (2025). Reconstructs cued overt and imagined speech audio and text from 130-channel wet EEG with subject-specific models; imagined-speech WER is 47.48% (2 s) and 43.46% (4 s) before language correction.
- [Lightweight Diffusion-based Framework for Online Imagined Speech Decoding in Aphasia](lightweight-diffusion-based-framework-for-online-imagined-speech-decoding-in-aphasia.md) (2025). Real-time diffusion-based EEG decoder for one person with aphasia classifying three imagined Korean words plus rest, reporting 65% top-1 and 70% top-2 accuracy over 20 online trials.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
