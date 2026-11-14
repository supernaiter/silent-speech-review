# Silent Speech and Emotion Recognition from Vocal Tract Shape Dynamics in Real-Time MRI

Laxmi Pandey, Ahmed Sabbir Arif  
arXiv 2021 · [arXiv](https://arxiv.org/abs/2106.08706)

**Section:** [Brain signals (EEG, MEG, intracortical)](../../README.md#brain-signals-eeg-meg-intracortical) · **Format:** itemized summary (earlier format; see the [component reviews](../../README.md#component-reviews))

A structured review of *Silent Speech and Emotion Recognition from Vocal Tract Shape Dynamics in Real-Time MRI* (Laxmi Pandey and Ahmed Sabbir Arif, arXiv 2021) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Sentence-level speech recognition from real-time MRI of the vocal tract, plus emotion and gender articulation analysis; reaches 40.6% PER on USC-TIMIT with a language model, beating earlier rtMRI baselines.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Real-time MRI scanner (full vocal tract) |
| Task | Sentence-level speech recognition from rtMRI |
| Vocabulary | Sentence transcription (size not stated) |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 40.6% PER on USC-TIMIT unseen data with language model |

**Limitations.** rtMRI is a large, immobile lab instrument with no deployable path; evidence limited to offline decoding on USC-TIMIT.

## Full review

### In short

Strong rtMRI recognition result, weak deployment story.

### Review

The paper earns its core claim. On USC-TIMIT it reaches 40.6% PER with the LM, which is materially better than the older rtMRI studies the authors cite. The second contribution is not filler: the emotion analysis shows systematic lower-boundary distortions and gender differences across vocal-tract subregions. But nothing here changes the fact that rtMRI is expensive, immobile, and unsuitable for day-to-day SSI deployment.

### Why it matters

The sentence-level rtMRI recognizer is real and clearly stronger than the cited earlier rtMRI baselines, but the modality remains a laboratory instrument rather than a deployable SSI path.

### Prior state of the art

rtMRI speech work mostly stayed at smaller recognition units or articulatory analysis rather than sentence-level transcription.

### What changed

Pushes rtMRI to sentence-level text output and links recognition with a second analysis of emotion-dependent geometry.

### Position in the field

Important articulatory recognition paper at the edge of SSI scope.

### Practical value

Useful for understanding what full vocal-tract imaging can encode and for benchmarking articulatory recognition under rich but impractical sensing.

### Advanced

recognition; analysis

### Unresolved

scaling; portability; broader vocabularies and speakers

### Evaluation details

| Item | Details |
| --- | --- |
| Task | sentence-level speech recognition from rtMRI |
| Input | real-time MRI video |
| Sensor | real-time MRI scanner |
| Body site | lip; oral-cavity; palate; throat; tongue |
| Output | text |
| Vocabulary type | sentence transcription |
| Metrics and results | 40.6% PER on USC-TIMIT with language model; prior cited rtMRI baselines were 58% error on VCV recognition and 57% error on phoneme classification |
| Evaluation protocol | USC-TIMIT recognition on unseen data plus emotion and gender articulation analysis on USC-EMO-MRI |

### Limits

- **Technical:** The sensing hardware is large and immobile, and the data scope is narrow relative to practical SSI needs.
- **Evaluation:** The recognition evidence is limited to USC-TIMIT and offline decoding.
- **Deployment:** No deployable hardware path, latency study, or accessibility trial exists.
- **Scope of this review:** Laboratory rtMRI recognition and articulatory analysis.

### Evidence

- The framework translates variable-length rtMRI vocal-tract shape sequences into text using an end-to-end deep neural network. (Abstract)
- The phrases-with-LM model reports 40.6 PER, 39.4 CER, and 42.1 WER on USC-TIMIT unseen data. (Table 2: Performance of the three examined speech recognition models exploiting vocal tract dynamics on unseen data.)
- The discussion frames the approach as potentially useful but explicitly notes that the enabling technology for day-to-day use does not yet exist. (7   DISCUSSION)

## More reviews in Brain signals (EEG, MEG, intracortical)

- [EMA2S: An End-to-End Multimodal Articulatory-to-Speech System](../ema2s-an-end-to-end-multimodal-articulatory-to-speech-system/) (2021). End-to-end EMA-to-speech synthesis with multimodal joint loss and a neural vocoder, consistently improving objective and subjective quality over prior EMA-to-speech baselines.
- [Neuroprosthesis for Decoding Speech in a Paralyzed Person with Anarthria](../neuroprosthesis-for-decoding-speech-in-a-paralyzed-person-with-anarthria/) (2021). ECoG speech neuroprosthesis in a man with anarthria decodes attempted sentences from a 50-word vocabulary in real time: median 25.6% WER with a language model at 15.2 words per minute.
- [Towards Neural Decoding of Imagined Speech based on Spoken Speech](../towards-neural-decoding-of-imagined-speech-based-on-spoken-speech/) (2022). Transfers CSP+SVM models trained on spoken-speech EEG to imagined speech decoding; accuracy is slightly lower but not significantly different from direct training in a 5-class, 7-subject offline task.
- [A comparison of oscillatory characteristics in covert speech and speech perception](../a-comparison-of-oscillatory-characteristics-in-covert-speech-and-speech-perception/) (2020). EEG analysis comparing oscillatory activity in covert speech and speech perception in eight participants; finds stronger low-gamma for covert speech, stronger delta/theta for perception, and theta-gamma coupling.
- [Continuous Silent Speech Recognition using EEG](../continuous-silent-speech-recognition-using-eeg/) (2020). Decodes continuous sentences from 31-channel scalp EEG recorded during silent reading using CTC and a 4-gram language model; WER is very high (about 75-84%), showing feasibility only.
- [A high-performance neuroprosthesis for speech decoding and avatar control](../a-high-performance-neuroprosthesis-for-speech-decoding-and-avatar-control/) (2023). 253-channel ECoG neuroprosthesis decodes silently attempted speech into text, synthesized voice and avatar movements; real-time median WER 25.5% at 78 wpm on a 1,024-word sentence set in one person with anarthria.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
