# An Accurate and Rapidly Calibrating Speech Neuroprosthesis

Nicholas S. Card, Maitreyee Wairagkar, Carrina Iacobacci, Xianda Hou, Tyler Singer-Clark, Francis R. Willett, Erin M. Kunz, Chaofei Fan, Maryam Vahdati Nia, Darrel R. Deo, Aparna Srinivasan, Eun Young Choi, Matthew F. Glasser, Leigh R. Hochberg, Jaimie M. Henderson, Kiarash Shahlaie, Sergey D. Stavisky, David M. Brandman  
New England Journal of Medicine 391(7):609-618 2024 · [DOI](https://doi.org/10.1056/NEJMoa2314132)

**Section:** [Brain signals (EEG, MEG, intracortical)](../../README.md#brain-signals-eeg-meg-intracortical) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *An Accurate and Rapidly Calibrating Speech Neuroprosthesis* (Nicholas S. Card et al., New England Journal of Medicine 391(7):609-618 2024) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Intracortical speech BCI in a man with ALS reaches 9.8% WER on a 125,000-word vocabulary on day 2 and about 2.5% later, and was used for 248 hours of self-paced conversation over 8.4 months.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Four 64-electrode intracortical microelectrode arrays in precentral gyrus |
| Task | Attempted speech to text with personalized TTS output |
| Vocabulary | 50 words and 125,000-word English vocabulary |
| Speaker | Speaker-dependent |
| Session | Cross-day |
| Online / offline | Online |
| Key result | Copy-task WER 2.5% at 31.6 wpm (125k words); conversation WER 3.7% |

**Limitations.** Single participant; rate well below natural speech; researcher needed to set up; long-term ALS progression effects unknown.

## Full review

### In short

Intracortical speech BCI used for self-paced conversation over 8.4 months: 9.8% WER on a 125,000-word vocabulary on day 2 and about 2.5% WER in later sessions, with 3.7% WER in conversation mode.

### Review

Card et al. push the Willett-style intracortical approach to near-everyday accuracy. Four 64-electrode arrays (256 sites) in left precentral gyrus of a man with ALS and severe dysarthria decode phonemes every 80 ms, which are combined into words and sentences with openly available language models and spoken via a TTS voice resembling his pre-ALS voice. After 30 minutes of data the 50-word decoder reached 0.44% WER; on day 2, with 1.4 additional hours, 125,000-word WER was 9.8%; by session 15 and through the final five sessions, copy-task WER was 2.5% at 31.6 words per minute. Most importantly, the participant used the system in self-initiated conversation for 248 cumulative hours over 8.4 months (22,679 sentences), with 3.7% WER on 925 labelled conversation sentences and only three short self-requested recalibrations. Caveats: one participant; speaking rate (31.6 wpm) is far below natural conversation; the headline '97.5% accuracy' corresponds to the copy task, while conversational labels and self-reports (52.9% correct, 32.3% mostly correct) are less clean; a researcher still had to connect and launch the system.

### Why it matters

Strongest evidence to date (in this set) that an invasive speech neuroprosthesis can be accurate enough and stable enough for sustained, self-initiated daily communication.

### Prior state of the art

Willett et al. (2023) and Metzger et al. (2023) reached about 24-26% WER on large vocabularies in research sessions with daily recalibration.

### What changed

Roughly tenfold lower WER on a 125,000-word vocabulary, rapid calibration (usable on day 1-2), and long-term personal conversational use with speech detection from neural activity.

### Position in the field

Current reference point for intracortical speech-to-text BCIs aimed at practical home use.

### Practical value

Shows that, with 256 electrodes in precentral gyrus, near-usable accuracy is achievable quickly and maintained over months; informs clinical translation.

### Advanced

Accuracy on large vocabulary; calibration speed; months-long personal use; neural speech start/stop detection.

### Unresolved

Multiple participants; speech rate close to natural conversation; performance as ALS progresses; fully independent setup.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | Real-time decoding of attempted speech to text, read aloud with a personalized TTS voice, in copy and conversation modes. |
| Input | Intracortical neural activity from microelectrode arrays during attempted speech. |
| Sensor | Four 64-electrode (8 x 8) intracortical microelectrode arrays (256 sites) in left precentral gyrus: two ventral premotor, one primary motor (BA4), one area 55b. |
| Body site | Brain (left precentral gyrus). |
| Output | Text and synthesized speech (TTS in a voice resembling the participant's pre-ALS voice). |
| Vocabulary type | Closed 50-word set and large open English vocabulary. |
| Vocabulary size | 50 words; 125,000 words. |
| Metrics and results | 50-word WER 0.44% on session 1 (after 30 min of data); 125,000-word copy-task WER 9.8% on session 2; 2.5% by session 15; final five sessions 2.5% (95% CI 2.0-3.1) at 31.6 wpm. Conversation-mode WER 3.7% on 925 labelled sentences. 248.3 cumulative hours over 8.4 months, 22,679 sentences, 84 sessions. |
| Evaluation protocol | Real-time copy task and self-paced conversation mode over 84 sessions; offline evaluation of speech detection. |

### Limits

- **Technical:** Decoder details (RNN and language-model specifics) are largely in supplementary material not reviewed here; the main text describes 80 ms phoneme decoding with open-source language models.
- **Evaluation:** Single participant. Conversation-mode WER computed on 925 sentences with known labels; self-reported accuracy is subjective. The abstract's 97.5% figure is tied to copy-task WER in the main text.
- **Deployment:** Percutaneous intracortical arrays; a researcher needed to connect and launch the system; effects of ALS progression not studied.
- **Scope of this review:** Read the author-manuscript full text (eScholarship PDF) via automated extraction; Supplementary Appendix (architecture, LM details) not read. No independent reproduction.

### Evidence

- Participant: 45-year-old man with ALS and severe dysarthria (ALSFRS-R 23); unintelligible to non-caregivers. (Methods, Study participant)
- Four 64-electrode arrays (256 sites) were implanted in left precentral gyrus: two ventral premotor, one BA4, one area 55b. (Methods, Surgical implantation; Discussion)
- On session 1 the 50-word vocabulary reached 0.44% WER; on session 2, the 125,000-word copy task reached 9.8% WER. (Results; Abstract)
- Copy-task WER was 2.5% by session 15 and 2.5% (95% CI 2.0-3.1) in the final five sessions at 31.6 words per minute. (Results)
- Conversation-mode WER was 3.7% (95% CI 3.3-4.3) on 925 sentences with known labels. (Results, Conversation)
- The system was used for 248.3 cumulative hours over 8.4 months across 84 sessions, communicating 22,679 sentences, including self-initiated use in 72 sessions. (Results; Abstract)
- Phonemes are decoded every 80 ms from neural activity without microphone input and turned into words and sentences with openly available language models; output is spoken by a TTS voice designed to sound like his pre-ALS voice. (Methods / Results)
- The authors note a single participant, uncertain durability as ALS progresses, no data on other disorders, and that a researcher was needed to connect and launch the system. (Discussion)

## More reviews in Brain signals (EEG, MEG, intracortical)

- [A Convolutional Framework for Mapping Imagined Auditory MEG into Listened Brain Responses](../a-convolutional-framework-for-mapping-imagined-auditory-meg-into-listened-brain-responses/) (2025). Maps imagined auditory MEG (melodies and poems) to listened-response MEG; 8-condition classification reaches 50.7% (chance 12.5%), and calibrated cross-subject CNN beats shuffled controls, but correlations are small.
- [A cross-species neural foundation model for end-to-end speech decoding](../a-cross-species-neural-foundation-model-for-end-to-end-speech-decoding/) (2025). Introduces a cross-species self-supervised transformer encoder for Utah-array spiking data combined with audio-LLM end-to-end decoding, reporting state-of-the-art Brain-to-Text benchmark accuracy and imagined speech decoding.
- [An instantaneous voice-synthesis neuroprosthesis](../an-instantaneous-voice-synthesis-neuroprosthesis/) (2025). Intracortical BCI synthesizes a man with ALS's voice instantaneously with closed-loop audio feedback and prosody control; closed-set listener matching 94.34%, mimed and vocalized attempts decoded similarly.
- [Brain-to-Text Decoding: A Non-invasive Approach via Typing](../brain-to-text-decoding-a-non-invasive-approach-via-typing/) (2025). Brain2Qwerty decodes sentences typed from memory using non-invasive MEG/EEG; average CER 32% with MEG (best participant 19%) versus 67% with EEG, in 35 healthy typists.
- [Distinct Theta Synchrony across Speech Modes: Perceived, Spoken, Whispered, and Imagined](../distinct-theta-synchrony-across-speech-modes-perceived-spoken-whispered-and-imagined/) (2025). Exploratory comparison of EEG theta-band functional connectivity across perceived, spoken, whispered and imagined speech in ten healthy subjects; no recognition performance is measured.
- [EEG-to-Voice Decoding of Spoken and Imagined speech Using Non-Invasive EEG](../eeg-to-voice-decoding-of-spoken-and-imagined-speech-using-non-invasive-eeg/) (2025). Reconstructs cued overt and imagined speech audio and text from 130-channel wet EEG with subject-specific models; imagined-speech WER is 47.48% (2 s) and 43.46% (4 s) before language correction.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
