# A high-performance speech neuroprosthesis

Francis R. Willett, Erin M. Kunz, Chaofei Fan, Donald T. Avansino, Guy H. Wilson, Eun Young Choi, Foram Kamdar, Matthew F. Glasser, Leigh R. Hochberg, Shaul Druckmann, Krishna V. Shenoy, Jaimie M. Henderson  
Nature 620(7976):1031-1036 2023 · [DOI](https://doi.org/10.1038/s41586-023-06377-x)

**Section:** [Brain signals (EEG, MEG, intracortical)](../../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text

A structured review of *A high-performance speech neuroprosthesis* (Francis R. Willett et al., Nature 620(7976):1031-1036 2023) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Intracortical speech BCI in a person with ALS decodes attempted speech to text in real time: 23.8% WER on a 125,000-word vocabulary at 62 words per minute; silently mouthed attempts reach 24.7%.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Four intracortical microelectrode arrays (areas 6v and 44) |
| Task | Attempted-speech (vocalized and mouthed) sentence decoding to text |
| Vocabulary | 50 words and 125,000-word English vocabulary |
| Speaker | Speaker-dependent |
| Session | Cross-day |
| Online / offline | Online |
| Key result | Real-time WER 23.8% (vocalized) / 24.7% (silent) at 125k words; 9.1% / 11.2% at 50 words; 62 wpm |

**Limitations.** Single participant, daily recalibration, researcher-operated; 24% WER judged insufficient for everyday use by the authors.

## Full review

### In short

Landmark intracortical speech-to-text BCI: 23.8% real-time WER on a 125,000-word vocabulary at 62 words per minute in one person with ALS, with silently mouthed attempts decoded about as well as vocalized ones.

### Review

This is the paper that moved attempted-speech BCIs from small closed vocabularies to large-vocabulary sentence decoding at conversational-adjacent speed. Four microelectrode arrays (two in area 6v, two in area 44) record from participant T12, who has bulbar-onset ALS. A five-layer GRU RNN emits phoneme probabilities every 80 ms and a 125,000-word trigram language model produces text. Over five vocalized and three silent (mouthed) evaluation days, real-time WER was 9.1%/11.2% for a 50-word vocabulary and 23.8%/24.7% for the 125,000-word vocabulary, at 62 words per minute. For SSI the most relevant finding is that silently mouthed attempts are decoded almost as well as vocalized attempts, i.e., the decoder does not rely on audible output. Neuroscientifically, area 44 carried little decodable information (below 12% classification), whereas area 6v supported 92% orofacial-movement and 62% phoneme classification from 1 s windows. Offline, a better language model reduced WER from 23.8% to 17.4% and testing closer in time to training to 11.8%, which shows how much of the gap is language-model and non-stationarity rather than neural signal. Limitations are those of the era: one participant, daily recalibration with 260-480 sentences, researcher-operated system, and a 24% WER the authors themselves call not yet sufficient for everyday use.

### Why it matters

Establishes that intracortical recordings from a few square millimetres of ventral precentral cortex suffice for large-vocabulary, real-time attempted-speech decoding, and that silent mouthing yields nearly the same accuracy as vocalized attempts.

### Prior state of the art

Prior speech BCIs (e.g., ECoG-based word classification in anarthria) decoded tens of words at around 15 words per minute; large-vocabulary sentence decoding had been shown mostly offline or in able speakers.

### What changed

Real-time phoneme-level RNN plus large n-gram language model decoding from intracortical arrays, extending vocabulary to 125,000 words and speed to 62 words per minute, with day-specific input layers to handle non-stationarity.

### Position in the field

Reference point for invasive speech neuroprostheses; the brain-section anchor against which later intracortical (Card 2024) and ECoG (Metzger 2023) systems are compared.

### Practical value

Demonstrates a viable architecture (phoneme RNN + LM) and quantifies how much LM quality and recalibration matter. Not yet a take-home device.

### Advanced

Vocabulary size (50 to 125,000 words) for real-time decoding; communication speed (62 wpm); silent (mouthed) versus vocalized attempted speech comparison; cortical localization (6v vs 44).

### Unresolved

Multiple participants; independent home use; recalibration-free stability; people with more profound orofacial weakness; WER low enough for everyday use.

### Narrowed or regressed

Requires daily training data (260-480 sentences, about 41 min) and day-specific decoder layers; invasive percutaneous arrays.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | Real-time decoding of attempted (vocalized or silently mouthed) sentences into text. |
| Input | Intracortical spiking activity (threshold crossings / spike-band features) from microelectrode arrays. |
| Sensor | Four intracortical microelectrode arrays: two 3.2 x 3.2 mm arrays in area 6v (ventral premotor) and two in area 44 (Broca's area). |
| Body site | Brain (left ventral precentral cortex area 6v and area 44). |
| Output | Text (phoneme probabilities decoded to words with an n-gram language model). |
| Vocabulary type | Closed 50-word set and large open-domain English vocabulary. |
| Vocabulary size | 50 words; 125,000 words. |
| Metrics and results | Real-time WER: 50-word 9.1% vocalized / 11.2% silent; 125,000-word 23.8% vocalized / 24.7% silent; 62 words per minute. Offline: improved LM 17.4%, plus temporally closer test sentences 11.8%; adding dorsal to ventral 6v array lowered offline WER from 32% to 21%; no same-day training 30% WER. Naive Bayes 1 s area 6v classification: 92% (33 orofacial movements), 62% (39 phonemes), 94% (50 words); area 44 below 12%. |
| Evaluation protocol | Real-time closed-loop evaluation on held-out sentences over 8 days, plus offline analyses of language model, array subsets and training data. |

### Limits

- **Technical:** Neural non-stationarity handled by day-specific input layers and rolling feature adaptation; without same-day training data WER was 30%. Area 44 arrays contributed little; performance relied on two small 6v arrays.
- **Evaluation:** Single participant; real-time evaluation over 8 days (5 vocalized, 3 silent) with 80 (125k) and 50 (50-word) trials per day. Offline improvements (17.4%, 11.8%) are retrospective analyses, not real-time results.
- **Deployment:** Percutaneous intracortical arrays, researcher-run sessions and daily recalibration; the authors state it is not yet a complete, clinically viable system.
- **Scope of this review:** Main article text read via an automated full-text extraction of the Nature open-access page (figures not visually inspected; Methods/Extended Data and Supplementary not exhaustively checked; data/code availability not verified). No independent reproduction.

### Evidence

- Participant T12 has bulbar-onset ALS, retains limited orofacial movement and vocalization but cannot produce intelligible speech; four microelectrode arrays were placed, two in area 6v and two in area 44. (Introduction; Fig. 1a)
- Real-time WER was 9.1% (vocalized) and 11.2% (silent) for a 50-word vocabulary, and 23.8% and 24.7% for a 125,000-word vocabulary. (Decoding attempted speech; Fig. 2b; Table 1)
- Decoded attempted speech ran at 62 words per minute on average. (Decoding attempted speech; Fig. 2c)
- A five-layer GRU RNN outputs phoneme probabilities every 80 ms with day-specific input layers and rolling feature adaptation, followed by a 125,000-word trigram language model in Kaldi. (Fig. 2a; Decoding attempted speech)
- From 1 s of area 6v activity, naive Bayes classification reached 92% for 33 orofacial movements, 62% for 39 phonemes and 94% for 50 words; area 44 was below 12%. (Fig. 1d; Results)
- Offline, an improved language model reduced WER from 23.8% to 17.4%, and testing on sentences closer in time to training reduced it to 11.8%. (Decoding attempted speech; Table 1)
- Evaluation spanned 8 days (5 vocalized, 3 silent); test sentences were not duplicated in training; final training set had 10,850 sentences, with 260-480 training sentences (41 +/- 3.7 min) collected per day. (Decoding attempted speech; Fig. 2b caption; Fig. 4c)
- Without training data from the evaluation day, WER rose to 30%, showing dependence on daily recalibration. (Fig. 4c; Decoding attempted speech)
- The authors state that a 24% WER is probably not yet low enough for everyday use, that results need confirmation in more participants, and that generalization to more profound orofacial weakness is open. (Discussion)

## More reviews in Brain signals (EEG, MEG, intracortical)

- [A high-performance neuroprosthesis for speech decoding and avatar control](../a-high-performance-neuroprosthesis-for-speech-decoding-and-avatar-control/) (2023). 253-channel ECoG neuroprosthesis decodes silently attempted speech into text, synthesized voice and avatar movements; real-time median WER 25.5% at 78 wpm on a 1,024-word sentence set in one person with anarthria.
- [Decoding speech perception from non-invasive brain recordings](../decoding-speech-perception-from-non-invasive-brain-recordings/) (2023). Contrastive deep model identifies heard 3 s speech segments from MEG/EEG across 175 participants; MEG top-1 up to 41% (best participants above 80%) among 1,000+ candidates, EEG much lower.
- [An Accurate and Rapidly Calibrating Speech Neuroprosthesis](../an-accurate-and-rapidly-calibrating-speech-neuroprosthesis/) (2024). Intracortical speech BCI in a man with ALS reaches 9.8% WER on a 125,000-word vocabulary on day 2 and about 2.5% later, and was used for 248 hours of self-paced conversation over 8.4 months.
- [Towards Neural Decoding of Imagined Speech based on Spoken Speech](../towards-neural-decoding-of-imagined-speech-based-on-spoken-speech/) (2022). Transfers CSP+SVM models trained on spoken-speech EEG to imagined speech decoding; accuracy is slightly lower but not significantly different from direct training in a 5-class, 7-subject offline task.
- [A Convolutional Framework for Mapping Imagined Auditory MEG into Listened Brain Responses](../a-convolutional-framework-for-mapping-imagined-auditory-meg-into-listened-brain-responses/) (2025). Maps imagined auditory MEG (melodies and poems) to listened-response MEG; 8-condition classification reaches 50.7% (chance 12.5%), and calibrated cross-subject CNN beats shuffled controls, but correlations are small.
- [A cross-species neural foundation model for end-to-end speech decoding](../a-cross-species-neural-foundation-model-for-end-to-end-speech-decoding/) (2025). Introduces a cross-species self-supervised transformer encoder for Utah-array spiking data combined with audio-LLM end-to-end decoding, reporting state-of-the-art Brain-to-Text benchmark accuracy and imagined speech decoding.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
