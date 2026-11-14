# A high-performance neuroprosthesis for speech decoding and avatar control

Sean L. Metzger, Kaylo T. Littlejohn, Alexander B. Silva, David A. Moses, Margaret P. Seaton, Ran Wang, Maximilian E. Dougherty, Jessie R. Liu, Peter Wu, Michael A. Berger, Inga Zhuravleva, Adelyn Tu-Chan, Karunesh Ganguly, Gopala K. Anumanchipalli, Edward F. Chang  
Nature 620(7976):1037-1046 2023 · [DOI](https://doi.org/10.1038/s41586-023-06443-4)

**Section:** [Brain signals (EEG, MEG, intracortical)](../../README.md#brain-signals-eeg-meg-intracortical) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *A high-performance neuroprosthesis for speech decoding and avatar control* (Sean L. Metzger et al., Nature 620(7976):1037-1046 2023) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

253-channel ECoG neuroprosthesis decodes silently attempted speech into text, synthesized voice and avatar movements; real-time median WER 25.5% at 78 wpm on a 1,024-word sentence set in one person with anarthria.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 253-channel high-density ECoG array over sensorimotor and temporal cortex |
| Task | Silent attempted speech to text, speech synthesis and avatar |
| Vocabulary | 1,024-word general set; 529- and 50-phrase AAC sets |
| Speaker | Speaker-dependent |
| Session | Cross-day |
| Online / offline | Both |
| Key result | Real-time median WER 25.5%, PER 18.5%, 78.3 wpm; 50-phrase set WER 4.92% (offline) |

**Limitations.** Single participant; AAC results offline; synthesized speech on general sentences has 54.4% perceptual WER; lab-based use.

## Full review

### In short

ECoG neuroprosthesis decoding silently attempted speech into text (median 25.5% WER, 78 wpm, 1,024-word set), synthesized speech and avatar facial movements in one person with anarthria after brainstem stroke.

### Review

This is the most SSI-like of the 2023 neuroprostheses: the participant attempts to speak silently, without vocalizing, and a 253-channel ECoG array over sensorimotor and temporal cortex drives three outputs. Text decoding uses a phone-level CTC model (1D convolution + 4 bidirectional GRU layers) with a 5-gram LM; on the 1024-word-General set it reached median 25.5% WER and median 18.5% PER in real time at 78.3 words per minute, and 4.92% WER on a 50-phrase AAC set offline. Speech synthesis predicts discrete HuBERT units and achieves MCD 3.45-5.21 dB, but perceptual WER of synthesized 1024-word-General speech remains high (median 54.4%). Avatar animation and emotional expression decoding are the paper's novelty for embodied communication rather than accuracy. Training needed under two weeks of data (9,506 trials), and a frozen code-word classifier stayed at 96.8% mean accuracy across 19 later sessions. Caveats: one participant; 529- and 50-phrase AAC results are offline simulations; personalized voice was applied offline; the avatar is evaluated by forced-choice perception and correlation with healthy speakers, not by communicative use.

### Why it matters

Shows that a non-penetrating ECoG array can support multimodal (text, voice, face) decoding from silent attempted speech at high speed, extending the SSI output space beyond text.

### Prior state of the art

Moses et al. (2021) decoded 50 words at 15 words per minute with ECoG in anarthria; speech synthesis from ECoG had been shown offline in able speakers (Anumanchipalli 2019).

### What changed

Higher-density 253-channel ECoG, phone-level CTC decoding with a 1,024-word real-time vocabulary, unit-based speech synthesis and facial-avatar decoding in one system.

### Position in the field

ECoG counterpart to Willett et al. (2023); key evidence that silent attempted speech in severe paralysis can drive text and voice outputs.

### Practical value

Useful blueprint for multi-output communication BCIs and for discrete-unit speech synthesis without ground-truth audio from the user.

### Advanced

Speed (78 wpm), vocabulary for real-time ECoG decoding, synthesized speech and avatar outputs, stability of a frozen classifier across sessions.

### Unresolved

Synthesized-speech intelligibility for general vocabulary; multiple participants; independent daily use; closed-loop feedback.

### Narrowed or regressed

Synthesized speech is far less intelligible than text output on general sentences (median perceptual WER 54.4% vs text WER 25.5%).

### Evaluation details

| Item | Details |
| --- | --- |
| Task | Decode silently attempted sentences into text, synthesized speech and avatar facial movements. |
| Input | High-density electrocorticography (ECoG) during silent attempted speech. |
| Sensor | 253-channel high-density ECoG array (3 mm spacing), subdural over left middle superior/middle temporal gyri, precentral and postcentral gyri. |
| Body site | Brain (left sensorimotor and temporal cortex surface). |
| Output | Text, synthesized speech audio, avatar facial animation, discrete expression/movement labels. |
| Vocabulary type | 1024-word-General sentence set (real time); 529- and 50-phrase AAC sets (offline). |
| Vocabulary size | 1,024 words (general set); 39,378-word vocabulary offline; 529 and 50 phrases. |
| Metrics and results | Text, 1024-word-General real-time: median WER 25.5% (99% CI 19.3-34.5), PER 18.5%, CER 19.9%, 78.3 wpm. Offline 39,378-word vocabulary WER 27.6%. 529-phrase-AAC WER 17.1% (89.9 wpm); 50-phrase-AAC WER 4.92% (101 wpm). Synthesis MCD 3.45/4.49/5.21 dB and perceptual median WER 8.20%/28.2%/54.4% for 50/529/1024 sets. Avatar forced-choice accuracy 85.7%/87.7%/74.3%; articulatory movement classification 87.8%; nine-way emotion 74.0%. Frozen NATO code-word classifier 96.8% over 19 later sessions. |
| Evaluation protocol | Real-time text, synthesis and acoustic-avatar decoding; offline simulations for AAC sets, direct avatar, vocabulary scaling and electrode exclusion. |

### Limits

- **Technical:** Phone-level CTC with 5-gram LM; synthesis via HuBERT units and vocoder. Coverage limited to one array; authors call for denser and broader coverage.
- **Evaluation:** Single participant. AAC phrase-set results are offline; general-vocabulary offline result uses a 39,378-word vocabulary. Avatar evaluated perceptually and by correlation with healthy speakers. Text says 13 days of data collection in Results versus 14 in Discussion.
- **Deployment:** Percutaneous connection, laboratory sessions, no closed-loop feedback during decoding; personalized voice applied offline.
- **Scope of this review:** Read the author-manuscript full text (eScholarship PDF) via automated extraction; about the last 11% of the text (likely late Methods/references) was not read; Extended Data and Supplementary Table values not checked. No independent reproduction.

### Evidence

- Participant is 47, with quadriplegia and anarthria from a pontine infarct in 2005; she attempted to silently speak sentences without vocalizing, which the authors distinguish from imagined speech. (Methods, Participant; Results, Overview)
- A 253-channel high-density ECoG array with 3-mm spacing was placed subdurally over left temporal, precentral and postcentral cortex. (Methods, Neural implant)
- Real-time 1024-word-General decoding reached median WER 25.5% (99% CI 19.3-34.5), median PER 18.5% and CER 19.9% at 78.3 words per minute. (Results, Text decoding; Fig. 2)
- Offline, the 529-phrase-AAC set reached 17.1% WER at 89.9 wpm and the 50-phrase-AAC set 4.92% WER at 101 wpm. (Results, Text decoding; Fig. 2)
- Text decoder: 1D convolution plus 4 bidirectional GRU layers predicting 39 phones plus silence with CTC, decoded with a 5-gram KenLM; speech synthesis predicts 100 HuBERT discrete units with CTC and vocodes them. (Methods)
- Synthesized speech MCD was 3.45, 4.49 and 5.21 dB and perceptual median WER 8.20%, 28.2% and 54.4% for the 50-phrase, 529-phrase and 1024-word sets. (Results, Speech synthesis; Fig. 3)
- Avatar forced-choice perceptual accuracy was 85.7%, 87.7% and 74.3%; six-way articulatory movement classification median 87.8%; nine-way emotional expression 74.0%. (Results, Facial-avatar decoding; Fig. 4)
- Training used 9,506 sentence trials (about 1.6 h per day) over 13 days; a NATO code-word classifier frozen at day 40 averaged 96.8% across 19 later sessions. (Results, Text decoding)
- Single participant; the authors call for validation in other individuals, note closed-loop feedback was not provided and that denser, broader coverage is needed. (Discussion)

## More reviews in Brain signals (EEG, MEG, intracortical)

- [A high-performance speech neuroprosthesis](../a-high-performance-speech-neuroprosthesis/) (2023). Intracortical speech BCI in a person with ALS decodes attempted speech to text in real time: 23.8% WER on a 125,000-word vocabulary at 62 words per minute; silently mouthed attempts reach 24.7%.
- [Decoding speech perception from non-invasive brain recordings](../decoding-speech-perception-from-non-invasive-brain-recordings/) (2023). Contrastive deep model identifies heard 3 s speech segments from MEG/EEG across 175 participants; MEG top-1 up to 41% (best participants above 80%) among 1,000+ candidates, EEG much lower.
- [An Accurate and Rapidly Calibrating Speech Neuroprosthesis](../an-accurate-and-rapidly-calibrating-speech-neuroprosthesis/) (2024). Intracortical speech BCI in a man with ALS reaches 9.8% WER on a 125,000-word vocabulary on day 2 and about 2.5% later, and was used for 248 hours of self-paced conversation over 8.4 months.
- [Towards Neural Decoding of Imagined Speech based on Spoken Speech](../towards-neural-decoding-of-imagined-speech-based-on-spoken-speech/) (2022). Transfers CSP+SVM models trained on spoken-speech EEG to imagined speech decoding; accuracy is slightly lower but not significantly different from direct training in a 5-class, 7-subject offline task.
- [A Convolutional Framework for Mapping Imagined Auditory MEG into Listened Brain Responses](../a-convolutional-framework-for-mapping-imagined-auditory-meg-into-listened-brain-responses/) (2025). Maps imagined auditory MEG (melodies and poems) to listened-response MEG; 8-condition classification reaches 50.7% (chance 12.5%), and calibrated cross-subject CNN beats shuffled controls, but correlations are small.
- [A cross-species neural foundation model for end-to-end speech decoding](../a-cross-species-neural-foundation-model-for-end-to-end-speech-decoding/) (2025). Introduces a cross-species self-supervised transformer encoder for Utah-array spiking data combined with audio-LLM end-to-end decoding, reporting state-of-the-art Brain-to-Text benchmark accuracy and imagined speech decoding.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
