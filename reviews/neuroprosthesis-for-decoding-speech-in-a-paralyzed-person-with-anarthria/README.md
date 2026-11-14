# Neuroprosthesis for Decoding Speech in a Paralyzed Person with Anarthria

David A. Moses, Sean L. Metzger, Jessie R. Liu, Gopala K. Anumanchipalli, Joseph G. Makin, Pengfei F. Sun, Josh Chartier, Maximilian E. Dougherty, Patricia M. Liu, Gary M. Abrams, Adelyn Tu-Chan, Karunesh Ganguly, Edward F. Chang  
New England Journal of Medicine 385(3) 2021 · [DOI](https://doi.org/10.1056/NEJMoa2027540)

**Section:** [Brain signals (EEG, MEG, intracortical)](../../README.md#brain-signals-eeg-meg-intracortical) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *Neuroprosthesis for Decoding Speech in a Paralyzed Person with Anarthria* (David A. Moses et al., New England Journal of Medicine 385(3) 2021) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

ECoG speech neuroprosthesis in a man with anarthria decodes attempted sentences from a 50-word vocabulary in real time: median 25.6% WER with a language model at 15.2 words per minute.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 128-electrode high-density ECoG over sensorimotor cortex |
| Task | Attempted word and sentence decoding to text |
| Vocabulary | 50 words |
| Speaker | Speaker-dependent |
| Session | Cross-session |
| Online / offline | Both |
| Key result | Median WER 25.6% with LM (60.5% without), 15.2 wpm; isolated words 47.1% (chance 2%) |

**Limitations.** Single participant, 50-word vocabulary, strong reliance on the language model, spurious detections, no independent use.

## Full review

### In short

First demonstration of real-time sentence decoding from attempted speech in a person with long-standing anarthria: 50-word vocabulary, median 25.6% WER with a language model, 15.2 words per minute.

### Review

The BRAVO1 study implanted a 128-electrode high-density ECoG array over left sensorimotor cortex of a man with anarthria for more than 15 years after brainstem stroke. A speech-detection model, a 50-word classifier and a 50-word language model combined via Viterbi decoding produced sentences in real time. Median WER over 15 blocks was 25.6% with the language model versus 60.5% without, against 92.1% chance, at a median 15.2 words per minute; 80 of 150 trials were error-free. Offline isolated-word classification reached 47.1% mean accuracy (chance 2%) over 9,800 trials. Stability analyses suggest models can use data spanning 81 weeks without daily recalibration, but they were designed post hoc. For SSI, the significance is proof that cortical activity during attempted articulation remains decodable years after loss of speech; the limitations are the tiny vocabulary, the heavy reliance on the language model, single-participant design and frequent spurious detections (968) in isolated-word analysis.

### Why it matters

Clinical proof of concept that attempted-speech cortical signals persist and are decodable into sentences long after anarthria onset, setting the baseline later ECoG and intracortical systems improved upon.

### Prior state of the art

Speech decoding from ECoG had been shown in epilepsy patients who could speak; decoding in people who had lost speech was unproven.

### What changed

First real-time sentence decoding in anarthria using speech detection, word classification and a language model, with long-term stability analysis over 81 weeks.

### Position in the field

Foundational clinical ECoG speech neuroprosthesis; predecessor of Metzger et al. 2023.

### Practical value

Establishes feasibility and a stability argument for chronic ECoG; vocabulary and speed are too limited for general communication.

### Advanced

Clinical population (anarthria), real-time sentence decoding, long-term signal stability.

### Unresolved

Vocabulary size, speed, multiple participants, independent use, false detection rate.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | Real-time decoding of attempted words and sentences from a fixed 50-word vocabulary. |
| Input | High-density ECoG high-gamma activity during attempted speech. |
| Sensor | 128-electrode (16 x 8, 4 mm spacing) high-density ECoG array, subdural over left sensorimotor cortex. |
| Body site | Brain (left precentral, postcentral, posterior middle frontal and posterior inferior frontal gyri). |
| Output | Text (words and sentences). |
| Vocabulary type | Closed vocabulary; 50 target sentences built from the same words. |
| Vocabulary size | 50 words. |
| Metrics and results | Real-time sentence decoding: median WER 25.6% with LM (95% CI 17.1-37.1), 60.5% without LM, chance 92.1%; median 15.2 words per minute (12.5 correct wpm); 80/150 trials error-free. Offline isolated-word accuracy 47.1% (chance 2%); 98% of attempts detected, 968 spurious detections. |
| Evaluation protocol | Real-time sentence decoding plus offline isolated-word classification and post hoc stability analyses. |

### Limits

- **Technical:** Word-level classification over a fixed 50-word set; sentence accuracy depends strongly on the LM (60.5% WER without vs 25.6% with). High-gamma (70-150 Hz) features only.
- **Evaluation:** Single participant; sentence results from 15 blocks / 150 trials; isolated-word results offline without LM; stability analyses post hoc with no multiple-comparison adjustment.
- **Deployment:** Percutaneous connector prevented independent daily use; testing at the participant's home with researchers.
- **Scope of this review:** Read the author-manuscript full text (eScholarship PDF) via automated extraction; Supplementary Appendix (model layer details, Fig. S5, S10) not read. No independent reproduction.

### Evidence

- Participant: 36-year-old man with anarthria and spastic quadriparesis after pontine stroke at age 20; 50 sessions over 81 weeks. (Methods, Participant; Discussion)
- A 128-electrode 16 x 8 high-density ECoG array (4 mm spacing) was implanted subdurally over left sensorimotor cortex. (Methods, Implant Device)
- Median real-time sentence WER was 25.6% with the language model and 60.5% without; chance was 92.1%; median rate 15.2 words per minute. (Results, Sentence Decoding; Fig. 2)
- Offline isolated-word classification averaged 47.1% across 50 words (chance 2%) from about 22 hours of data (9,800 trials). (Results, Word Detection and Classification; Abstract)
- Pipeline combines a speech-detection model, a 50-word classifier using 1 s before to 3 s after onset, and a language model via Viterbi decoding. (Methods, Modeling)
- 98% of word attempts were detected, but 968 detections were spurious. (Results; Fig. S5 referenced)
- Models performed consistently without daily or weekly recalibration and benefited from data spanning more than a year; these stability analyses were post hoc. (Results, Long-Term Stability; Fig. 4)
- Single participant, 50-word vocabulary, and no independent use because of the percutaneous connector. (Discussion; Methods)

## More reviews in Brain signals (EEG, MEG, intracortical)

- [EMA2S: An End-to-End Multimodal Articulatory-to-Speech System](../ema2s-an-end-to-end-multimodal-articulatory-to-speech-system/) (2021). End-to-end EMA-to-speech synthesis with multimodal joint loss and a neural vocoder, consistently improving objective and subjective quality over prior EMA-to-speech baselines.
- [Silent Speech and Emotion Recognition from Vocal Tract Shape Dynamics in Real-Time MRI](../silent-speech-and-emotion-recognition-from-vocal-tract-shape-dynamics-in-real-time-mri/) (2021). Sentence-level speech recognition from real-time MRI of the vocal tract, plus emotion and gender articulation analysis; reaches 40.6% PER on USC-TIMIT with a language model, beating earlier rtMRI baselines.
- [Towards Neural Decoding of Imagined Speech based on Spoken Speech](../towards-neural-decoding-of-imagined-speech-based-on-spoken-speech/) (2022). Transfers CSP+SVM models trained on spoken-speech EEG to imagined speech decoding; accuracy is slightly lower but not significantly different from direct training in a 5-class, 7-subject offline task.
- [A comparison of oscillatory characteristics in covert speech and speech perception](../a-comparison-of-oscillatory-characteristics-in-covert-speech-and-speech-perception/) (2020). EEG analysis comparing oscillatory activity in covert speech and speech perception in eight participants; finds stronger low-gamma for covert speech, stronger delta/theta for perception, and theta-gamma coupling.
- [Continuous Silent Speech Recognition using EEG](../continuous-silent-speech-recognition-using-eeg/) (2020). Decodes continuous sentences from 31-channel scalp EEG recorded during silent reading using CTC and a 4-gram language model; WER is very high (about 75-84%), showing feasibility only.
- [A high-performance neuroprosthesis for speech decoding and avatar control](../a-high-performance-neuroprosthesis-for-speech-decoding-and-avatar-control/) (2023). Text, voice and avatar from ECoG in one participant hold as a demonstration; sensor and decoder are standard, and an LM trained on the test pool inflates the text result.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
