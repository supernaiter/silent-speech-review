# Speech synthesis from neural decoding of spoken sentences

Gopala K. Anumanchipalli, Josh Chartier, Edward F. Chang  
Nature 568:493-498 2019 · [DOI](https://doi.org/10.1038/s41586-019-1119-1)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text

A structured review of *Speech synthesis from neural decoding of spoken sentences* (Gopala K. Anumanchipalli et al., Nature 568:493-498 2019) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Two-stage bLSTM decoder maps ECoG to inferred articulatory kinematics and then to speech, yielding offline synthesized sentences that listeners transcribe with 31% median WER (25-word pool) in epilepsy patients.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Clinical high-density ECoG arrays (vSMC, STG, IFG) |
| Task | Speech synthesis from neural signals |
| Vocabulary | Read sentences; 25/50-word listener pools |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | MCD 5.14-6.58 dB; listener median WER 31% (25-word pool), 53% (50-word pool) |

**Limitations.** Offline, able-speaking epilepsy patients; inferred kinematics; closed-pool listener tests; mimed speech worse than audible.

## Full review

### In short

Two-stage ECoG decoder (neural to inferred articulatory kinematics to acoustics) synthesizes intelligible sentences offline in five epilepsy patients; mimed (silent) speech is decodable above chance but worse.

### Review

This is the canonical articulatory-intermediate brain-to-speech paper. In five epilepsy patients with clinical high-density ECoG over vSMC, STG and IFG, stacked bLSTMs map neural activity to 33 articulatory kinematic features (inferred from audio, not measured) and then to 32 acoustic parameters. Median MCD ranged 5.14-6.58 dB across participants, and the two-stage approach beat direct ECoG-to-acoustics by 0.54 dB. Crowdsourced listeners transcribed 43% (25-word pool) and 21% (50-word pool) of trials perfectly, with median WER 31% and 53%; these are closed-pool transcription tests, not open intelligibility. Robust performance needed as little as 25 minutes of speech. For SSI, the important test is mimed speech: 58 held-out sentences silently mouthed by P1 were decoded significantly above chance, but worse than audible speech, which the authors attribute to missing phonation signals. Everything is offline, in able speakers, with articulatory targets derived from acoustic-to-articulatory inversion; the stage-2 decoder transfers across participants only partially.

### Why it matters

Demonstrates that an articulatory intermediate representation improves neural speech synthesis and that silently mimed speech carries decodable cortical information.

### Prior state of the art

Brain-to-speech work reconstructed spectrograms directly or classified small sets of units, with limited intelligibility.

### What changed

Explicit neural-to-kinematics-to-acoustics decomposition with bLSTMs, evaluated by large-scale listener transcription, plus a mimed-speech test.

### Position in the field

Foundational offline ECoG speech synthesis study; precursor of the UCSF clinical neuroprostheses.

### Practical value

Motivates articulatory intermediates for SSIs across modalities; listener-test protocol is reusable.

### Advanced

Intelligibility of neurally synthesized sentences; articulatory intermediate representation; mimed-speech decoding evidence.

### Unresolved

Real-time synthesis; paralyzed users; open-vocabulary intelligibility; silent speech quality.

### Narrowed or regressed

Mimed (silent) speech decoding is inferior to audible speech.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | Offline synthesis of spoken sentences from ECoG via inferred articulatory kinematics. |
| Input | High-density ECoG (high-gamma and related features). |
| Sensor | Clinical high-density subdural ECoG arrays covering ventral sensorimotor cortex, superior temporal gyrus and inferior frontal gyrus. |
| Body site | Brain (cortical surface). |
| Output | Synthesized speech audio (MFCC, F0, voicing parameters to vocoder). |
| Vocabulary type | MOCHA-TIMIT and other read sentences; closed word pools for listener transcription. |
| Vocabulary size | Listener transcription with 25- and 50-word pools; 325 words in single-word identification. |
| Metrics and results | Median MCD 5.14-6.58 dB across participants (P < 1e-18 vs chance); two-stage better than direct decoding by 0.54 dB; spectral feature correlations mostly r > 0.6. Listener transcription: 43% (25-word pool) and 21% (50-word pool) of trials perfect; median WER 31% and 53%. Mimed speech above chance (P < 1e-11) but inferior to audible speech. |
| Evaluation protocol | Offline held-out sentence synthesis, crowdsourced listener tests (1,755 listeners, 16 tasks), mimed-speech test and cross-participant transfer. |

### Limits

- **Technical:** Articulatory kinematics inferred from audio (no EMA in clinic); MCD sensitive to speaker identity; direct decoding might match two-stage with more data (untested).
- **Evaluation:** Five epilepsy patients who could speak; listener tests use closed word pools; mimed test only in P1 (58 sentences) with no numeric MCD in text.
- **Deployment:** Temporary clinical ECoG for epilepsy monitoring; offline analysis only.
- **Scope of this review:** Read the published Nature PDF (third-party mirror) via automated extraction; numeric values shown only in figures (reference/chance MCD, mimed MCD) not inspected. No independent reproduction.

### Evidence

- Five participants with intractable epilepsy had clinical high-density ECoG arrays covering vSMC, STG and IFG. (Methods; Extended Data Fig. 3)
- Stage 1: 3-layer bLSTM maps 300 ms neural windows to 33 articulatory kinematic features; stage 2: 3-layer bLSTM maps kinematics to 32 acoustic parameters. (Methods; Fig. 1)
- Median MCD of decoded speech was 5.14 to 6.58 dB across participants; direct ECoG-to-acoustics decoding was worse by 0.54 dB. (Results; Fig. 2)
- Listeners transcribed 43% (25-word pool) and 21% (50-word pool) of trials perfectly; median sentence WER was 31% and 53%. (Results, listener transcription; Fig. 2)
- Robust performance could be achieved with as little as 25 min of speech training data. (Results; Fig. 2e)
- For 58 held-out sentences silently mimed by P1, decoding was significantly above chance (P < 1e-11) but inferior to audible speech. (Results; Fig. 3)
- Articulatory kinematics were inferred from audio because EMA was not feasible clinically; listener tests used closed vocabularies; stage-2 transfer from P1 to P2 performed less well than a P2-trained decoder. (Discussion; Methods)

## More reviews in Brain signals (EEG, MEG, intracortical)

- [A Novel Task-Oriented Text Corpus in Silent Speech Recognition and its Natural Language Generation Construction Method](a-novel-task-oriented-text-corpus-in-silent-speech-recognition-and-its-natural-language-generation-construction-method.md) (2019). Proposes a task-oriented text corpus and a hybrid natural language generation method for building EEG silent speech recognition datasets; claims gains over template and neural NLG but gives no numeric benchmark.
- [Brain2Char: A Deep Architecture for Decoding Text from Brain Recordings](brain2char-a-deep-architecture-for-decoding-text-from-brain-recordings.md) (2019). Brain2Char decodes text at character level from invasive ECoG with neural sequence models, reaching 7.0-10.6% WER for three participants on 1200-1900 word vocabularies; silent speech WER is about 40% and 67%.
- [A comparison of oscillatory characteristics in covert speech and speech perception](a-comparison-of-oscillatory-characteristics-in-covert-speech-and-speech-perception.md) (2020). EEG analysis comparing oscillatory activity in covert speech and speech perception in eight participants; finds stronger low-gamma for covert speech, stronger delta/theta for perception, and theta-gamma coupling.
- [Continuous Silent Speech Recognition using EEG](continuous-silent-speech-recognition-using-eeg.md) (2020). Decodes continuous sentences from 31-channel scalp EEG recorded during silent reading using CTC and a 4-gram language model; WER is very high (about 75-84%), showing feasibility only.
- [EMA2S: An End-to-End Multimodal Articulatory-to-Speech System](ema2s-an-end-to-end-multimodal-articulatory-to-speech-system.md) (2021). End-to-end EMA-to-speech synthesis with multimodal joint loss and a neural vocoder, consistently improving objective and subjective quality over prior EMA-to-speech baselines.
- [Neuroprosthesis for Decoding Speech in a Paralyzed Person with Anarthria](neuroprosthesis-for-decoding-speech-in-a-paralyzed-person-with-anarthria.md) (2021). ECoG speech neuroprosthesis in a man with anarthria decodes attempted sentences from a 50-word vocabulary in real time: median 25.6% WER with a language model at 15.2 words per minute.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
