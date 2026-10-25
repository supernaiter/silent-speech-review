# Silent Speech and Emotion Recognition from Vocal Tract Shape Dynamics in Real-Time MRI

Laxmi Pandey, Ahmed Sabbir Arif  
arXiv / imported corpus page 2021 · [arXiv](https://arxiv.org/abs/2106.08706)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text

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

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
