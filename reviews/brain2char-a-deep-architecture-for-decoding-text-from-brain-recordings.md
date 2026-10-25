# Brain2Char: A Deep Architecture for Decoding Text from Brain Recordings

Pengfei Sun, Gopala K. Anumanchipalli, Edward F. Chang  
arXiv / imported corpus page 2019 · [arXiv](https://arxiv.org/abs/1909.01401)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text+structured_benchmark+summary

Brain2Char decodes text at character level from invasive ECoG with neural sequence models, reaching 7.0-10.6% WER for three participants on 1200-1900 word vocabularies; silent speech WER is about 40% and 67%.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Implanted ECoG grids (16x16, 16x8) on speech cortex |
| Task | Sentence-level text decoding from brain signals |
| Vocabulary | 1200-1900 words (English sentences) |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | WER 7.0-10.6% for three participants, 1200-1900 word vocabularies; silent speech WER ~40% and 67% |

**Limitations.** Invasive implant, per-subject and per-session calibration, only four participants, silent speech tested on two subjects with about 20 sentences, no cross-subject transfer.

## Full review

### In short

Brain2Char establishes a new state-of-the-art for continuous character decoding from invasive ECoG with competitive WER on large vocabularies and silent speech, demonstrating feasibility for communication BCIs.

### Review

Brain2Char represents a significant step forward from earlier work limited to phoneme classification or small vocabularies by demonstrating continuous decoding of character sequences from ECoG recordings during overt and silent speech. The proposed architecture integrates multi-scale convolutional encoders and sequential recurrent and dilated CNN decoders with auxiliary physiological regularization and session calibration, yielding 7-11% WER on vocabularies up to 1900 words in 3 participants. Silent speech is decoded at higher WER (~40-67%) in two subjects. Remaining challenges include invasiveness, the need for per-subject calibration, limited vocabulary, and generalization beyond the training participants. Nevertheless, this system sets a new benchmark for neural speech recognition from direct brain signals and is promising for communication BCIs especially in clinical populations unable to speak.

### Why it matters

Provides the first demonstration of sentence-level brain-to-character decoding with modern neural sequence models and independent evaluation on multiple subjects, going beyond toy imagined-word classification models toward realistic speech recognition from brain signals.

### Prior state of the art

Prior brain-to-text decoding from ECoG data had not achieved continuous sentence-level character decoding with competitive WER on vocabulary sizes above approximately 50 words, often limited to phoneme or word classification.

### What changed

Introduces a modular architecture combining 3D multi-scale inception convolutional encoder, bidirectional LSTM layers, dilated CNN decoder layers with CTC loss and language model beam search, plus latent feature regularization using speech acoustics, articulatory kinematics, and session embeddings.

### Position in the field

Strong benchmark in sentence-level ECoG-based brain text decoding with larger vocabularies and physiological regularization.

### Practical value

Potentially useful for clinical communication BCIs once invasiveness and calibration challenges are addressed.

### Advanced

evaluation; system_design

### Unresolved

cross-subject transfer; larger vocabulary decoding

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-recognition |
| Input | electrocorticography (ECoG) invasive brain recordings |
| Sensor | 16x16 and 16x8 electrode ECoG grids implanted on ventral sensorimotor cortex, inferior frontal gyrus, superior temporal gyrus |
| Body site | brain |
| Output | text |
| Vocabulary type | sentence-level English |
| Vocabulary size | 1200 - 1900 words |
| Metrics and results | Word Error Rate (WER): 10.6%, 8.5%, and 7.0% for three participants on vocabularies from 1200 to 1900 words; Silent speech decoding WER: ~40% and 67% for two subjects on 20 sentences. |
| Evaluation protocol | Experimental study with neural signals and synchronous audio-text; train/test splits with increasing data sizes; partial neural data tests; silent speech trials. |

### Limits

- **Technical:** Limited dataset size; invasive sensor modality; session to session neural variability; vocabulary limited to 1200-1900 words; no cross-subject transfer; silent speech decoding at higher error rates.
- **Evaluation:** Evaluation restricted to 4 participants with invasive ECoG, limited sentence sets, and no cross-subject testing or long-term deployment; silent speech tested only on two participants with about 20 sentences each; no walking or mobile scenarios assessed.
- **Deployment:** Invasive ECoG recording modality requiring clinical implantation; calibration needed per subject and per session; vocabulary sizes remain limited for realistic free text use; no real-world deployment tested.
- **Scope of this review:** Sentence-level decoding from invasive ECoG collected during speech tasks in 4 participants; no non-invasive or cross-subject generalization assessed.

### Evidence

- Brain2Char achieves low word error rates (10.6%, 8.5%, and 7.0%) decoding character sequences directly from ECoG brain recordings with vocabularies of 1200 to 1900 words. (Abstract)
- Brain2Char combines 3D inception layers for multi-band spatiotemporal ECoG feature extraction, bi-directional LSTM layers, dilated CNN layers with CTC loss, and language model beam search to decode text from brain signals. (1.1 Brain2Char Architecture)
- Evaluation performed on ECoG recordings from 4 participants reading prompted sentences with vocabularies between 400 and 1900 words, recorded over several sessions; also tested silent mimed speech in 2 participants with acceptable error rates. (2 Experimental Results)
- Reported word error rates of Brain2Char reach as low as 7.0% for one participant and 10-11% for others on vocabulary tasks of 1200-1900 words; silent speech decoding WER is around 40-67%. (2 Experimental Results)
- Brain2Char is limited by reliance on invasive ECoG sensor hardware, session-specific calibration, and limited dataset per participant; generalization to other subjects or larger vocabularies remains unproven. (1 Neural Speech Recognition from ECoG)
- Although Brain2Char demonstrates hands-free, incremental, and real-time capable decoding, deployment for practical communication BCIs is limited by invasiveness and need for extensive calibration. (3 Conclusion)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
