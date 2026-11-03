# An instantaneous voice-synthesis neuroprosthesis

Maitreyee Wairagkar, Nicholas S. Card, Tyler Singer-Clark, Xianda Hou, Carrina Iacobacci, Lee M. Miller, Leigh R. Hochberg, David M. Brandman, Sergey D. Stavisky  
Nature 644(8075):145-152 2025 · [DOI](https://doi.org/10.1038/s41586-025-09127-3)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text+secondary_sources

A structured review of *An instantaneous voice-synthesis neuroprosthesis* (Maitreyee Wairagkar et al., Nature 644(8075):145-152 2025) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Intracortical BCI synthesizes a man with ALS's voice instantaneously with closed-loop audio feedback and prosody control; closed-set listener matching 94.34%, mimed and vocalized attempts decoded similarly.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Four intracortical microelectrode arrays (256 electrodes) in ventral precentral gyrus |
| Task | Real-time brain-to-voice synthesis with intonation and pitch control |
| Vocabulary | Unconstrained synthesis; 956 cued sentences evaluated |
| Speaker | Speaker-dependent |
| Session | Cross-session |
| Online / offline | Online |
| Key result | Closed-set intelligibility 94.34%; question intonation 90.5%; emphasis 95.7%; ~60% open word intelligibility (press release) |

**Limitations.** Single participant; open intelligibility inconsistent; reviewed from preprint plus press release, not final Nature text.

## Full review

### In short

Intracortical brain-to-voice BCI synthesizes the participant's voice causally with closed-loop audio feedback and lets him modulate intonation, emphasis and pitch; intelligibility is improved but not yet consistent.

### Review

Using the same 256-electrode intracortical implant as Card et al. (participant T15, ALS with severe dysarthria), this work replaces text decoding with direct, causal voice synthesis. A Transformer-based decoder predicts Bark cepstral coefficients, pitch and voicing every 10 ms and drives a vocoder, so the participant hears his BCI voice as he attempts to speak. Training targets were created without ground-truth speech by time-aligning TTS of the cued text to neural activity at estimated syllable boundaries; a voice-cloning TTS provided own-voice targets. In the preprint, closed-set listener matching (one of six same-length transcripts) averaged 94.34% over 956 sentences, and silently mimed attempts produced synthesis as correlated with targets (r = 0.89) as vocalized attempts, which is directly relevant to silent speech. Paralinguistic control was demonstrated: question intonation 90.5% and word emphasis 95.7% in closed loop, plus distinct pitch levels for short melodies. The published version (per the press release) reports listeners understood almost 60% of synthesized words versus 4% of his unaided speech, with about 25 ms latency; this open-transcription figure was not verified in the full text. Single participant, closed-set main intelligibility test, and acknowledged inconsistency of intelligibility are the main limits.

### Why it matters

First demonstration that intracortical signals can drive instantaneous, expressive voice synthesis with closed-loop feedback, including from silently mimed attempts, without any ground-truth speech from the user.

### Prior state of the art

Speech BCIs decoded text (with optional TTS) at sentence level; direct neural speech synthesis was offline or had large delays.

### What changed

Causal 10 ms-resolution synthesis with audio feedback, TTS-aligned pseudo-targets for an anarthric/dysarthric user, and decoding of paralinguistic features (intonation, emphasis, pitch).

### Position in the field

Leading intracortical brain-to-voice result; complements text-based neuroprostheses (Willett 2023, Card 2024).

### Practical value

Shows a path to natural conversational turn-taking and prosody that text-to-TTS pipelines cannot provide; pseudo-target method is reusable for SSIs lacking audio ground truth.

### Advanced

Latency (instantaneous, closed-loop synthesis); prosody and pitch control; synthesis from mimed speech; training without ground-truth audio.

### Unresolved

Consistent open-vocabulary intelligibility; multiple participants; long-term learning effects; home use.

### Narrowed or regressed

Open intelligibility (almost 60% of words, per press release) is far below text-decoding accuracy reported for the same participant in Card et al. 2024.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | Causal, real-time synthesis of the participant's voice from attempted (vocalized or mimed) speech, with paralinguistic control. |
| Input | Intracortical threshold crossings and spike-band power from microelectrode arrays. |
| Sensor | Four intracortical microelectrode arrays (256 electrodes) in ventral precentral gyrus: ventral premotor (6v), primary motor (M1) and area 55b. |
| Body site | Brain (left ventral precentral gyrus). |
| Output | Synthesized speech audio (Bark cepstral coefficients, pitch, voicing to vocoder), optionally in a cloned own voice. |
| Vocabulary type | Cued sentences plus self-guided speech, pseudo-words, spelling and interjections; unconstrained synthesis rather than vocabulary-bound decoding. |
| Vocabulary size | Not applicable (open, unit-free synthesis); 956 evaluation sentences in closed-set listener test. |
| Metrics and results | Preprint: closed-set 6-alternative listener matching 94.34% mean (median 100%) on 956 sentences; correlation with target speech r = 0.89 +/- 0.04 (attempted) and 0.89 +/- 0.03 (mimed); question intonation 90.5%; word emphasis 95.7%; loud vs quiet 90%; neural processing within 10 ms. Press release (published version): almost 60% of words understood with the BCI vs 4% without; ~25 ms synthesis latency. |
| Evaluation protocol | Real-time closed-loop synthesis across research sessions, evaluated by crowdsourced listener tests and closed-loop paralinguistic tasks. |

### Limits

- **Technical:** Targets are TTS-derived and aligned at putative syllable boundaries estimated from neural data; decoder modified for session nonstationarities. Quality depends on participant energy and enunciation.
- **Evaluation:** Single participant. Main preprint intelligibility metric is a 6-alternative closed-set matching task; open transcription numbers (about 60% vs 4%) and 25 ms latency seen only in a secondary source.
- **Deployment:** Percutaneous intracortical arrays; research sessions; long-term practice effects unknown.
- **Scope of this review:** Full text read for the bioRxiv preprint (10.1101/2024.08.14.607690) via automated extraction, not the final Nature version (publisher page unreachable); published-version figures (almost 60% word intelligibility vs 4%, ~25 ms latency) come from the UC Davis/EurekAlert press release and the Nature abstract. Session counts not verified.

### Evidence

- Participant T15 is a 45-year-old man with ALS and severe dysarthria, unable to produce intelligible speech, with four arrays (256 electrodes) in 6v, M1 and 55b. (Results, Continuous speech synthesis)
- A Transformer-based decoder predicts Bark-frequency cepstral coefficients, pitch and voicing every 10 ms from binned threshold crossings and spike-band power, then a vocoder plays audio with neural processing within 10 ms. (Results; Fig. 1c)
- With no ground-truth audio, targets were TTS of the cued text time-aligned to neural activity using putative syllable boundaries; own-voice targets came from voice-cloning TTS. (Results; Fig. 1d; Fig. 2g)
- Fifteen listeners matched each of 956 sentences to one of 6 same-length transcripts with mean 94.34% (median 100%) accuracy. (Results; Fig. 2b)
- Mimed (silent) attempts yielded synthesis correlation r = 0.89 +/- 0.03, not statistically different from vocalized attempts (0.89 +/- 0.04). (Results; Fig. 2c-d)
- Closed-loop question intonation reached 90.5% and word emphasis 95.7%; pitch decoding produced distinct low/medium/high levels for melodies. (Results; Fig. 3e, 3g, 3i)
- Listeners understood almost 60% of synthesized words with the BCI versus 4% without it; synthesis latency about one-fortieth of a second. (UC Davis press release via EurekAlert (published version))
- Single participant; synthesized words still not consistently intelligible; quality depended on participant energy and enunciation; long-term use effects unknown. (Limitations)

## More reviews in Brain signals (EEG, MEG, intracortical)

- [A Convolutional Framework for Mapping Imagined Auditory MEG into Listened Brain Responses](a-convolutional-framework-for-mapping-imagined-auditory-meg-into-listened-brain-responses.md) (2025). Maps imagined auditory MEG (melodies and poems) to listened-response MEG; 8-condition classification reaches 50.7% (chance 12.5%), and calibrated cross-subject CNN beats shuffled controls, but correlations are small.
- [A cross-species neural foundation model for end-to-end speech decoding](a-cross-species-neural-foundation-model-for-end-to-end-speech-decoding.md) (2025). Introduces a cross-species self-supervised transformer encoder for Utah-array spiking data combined with audio-LLM end-to-end decoding, reporting state-of-the-art Brain-to-Text benchmark accuracy and imagined speech decoding.
- [Brain-to-Text Decoding: A Non-invasive Approach via Typing](brain-to-text-decoding-a-non-invasive-approach-via-typing.md) (2025). Brain2Qwerty decodes sentences typed from memory using non-invasive MEG/EEG; average CER 32% with MEG (best participant 19%) versus 67% with EEG, in 35 healthy typists.
- [Distinct Theta Synchrony across Speech Modes: Perceived, Spoken, Whispered, and Imagined](distinct-theta-synchrony-across-speech-modes-perceived-spoken-whispered-and-imagined.md) (2025). Exploratory comparison of EEG theta-band functional connectivity across perceived, spoken, whispered and imagined speech in ten healthy subjects; no recognition performance is measured.
- [EEG-to-Voice Decoding of Spoken and Imagined speech Using Non-Invasive EEG](eeg-to-voice-decoding-of-spoken-and-imagined-speech-using-non-invasive-eeg.md) (2025). Reconstructs cued overt and imagined speech audio and text from 130-channel wet EEG with subject-specific models; imagined-speech WER is 47.48% (2 s) and 43.46% (4 s) before language correction.
- [Lightweight Diffusion-based Framework for Online Imagined Speech Decoding in Aphasia](lightweight-diffusion-based-framework-for-online-imagined-speech-decoding-in-aphasia.md) (2025). Real-time diffusion-based EEG decoder for one person with aphasia classifying three imagined Korean words plus rest, reporting 65% top-1 and 70% top-2 accuracy over 20 online trials.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
