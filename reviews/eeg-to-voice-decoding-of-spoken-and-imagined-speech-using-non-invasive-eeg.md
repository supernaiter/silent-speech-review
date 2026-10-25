# EEG-to-Voice Decoding of Spoken and Imagined speech Using Non-Invasive EEG

Hanbeot Park, Yunjeong Cho, Hunhee Kim  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2512.22146)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text+summary

Reconstructs cued overt and imagined speech audio and text from 130-channel wet EEG with subject-specific models; imagined-speech WER is 47.48% (2 s) and 43.46% (4 s) before language correction.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | EGI 130-channel wet high-density scalp EEG |
| Task | Speech synthesis and text from EEG |
| Vocabulary | 10 closed classes per condition (words and sentences) |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Imagined WER 47.48% at 2 s, 43.46% at 4 s, closed classes, before correction |

**Limitations.** Random splits include every class in training and test, imagined trials use overt audio as targets, and no unseen content, real-time use or clinical test is shown.

## Full review

### In short

Subject-specific EEG reconstructs known cued utterances offline, but imagined-speech WER remains 47.48% at 2 s and 43.46% at 4 s before correction; unseen content, real-time use and fully alignment-free processing are not demonstrated.

### Review

This is an offline EEG-to-voice proof of concept for repeatedly cued, known utterances, not evidence that arbitrary imagined sentences can be read from the scalp. A separate Generator is trained for each participant and speech mode, with overt recordings supplying acoustic targets for imagined trials. The random 2:1:1 split deliberately places every class in every subset. Before language correction, reported imagined-speech WER is 0.4748 ± 0.0947 for 2-s trials and 0.4346 ± 0.0525 for 4-s trials; corresponding CER is 0.2710 ± 0.0459 and 0.2474 ± 0.0361. Thus word errors remain substantial. Acoustic correlation drops from 0.7484 ± 0.0522 to 0.5834 ± 0.0584, but different cohorts, stimuli and loss settings prevent a clean duration-only interpretation. The useful systems idea is to learn a local EEG-to-Mel mapping without DTW inside the Generator and assess both voice and downstream text. That should not be called entirely alignment-free: segmentation is explicitly synchronized, imagined targets reuse spoken recordings, and MCD evaluation uses DTW. Language correction modestly reduces pooled spoken/imagined WER from 0.4586 to 0.4451 at 2 s and from 0.4870 to 0.4658 at 4 s; these are not imagined-only gains or proof that meaning is always preserved. The unexplained 11-versus-ten 2-s participant count, incomplete model and split details, and lack of unseen-content, artifact-control, listener or real-time tests are important limits. The work is relevant to silent communication as a constrained reconstruction experiment, not yet a usable communication aid.

### Why it matters

An integrated, auditable example of local-context EEG-to-acoustic regression evaluated in overt and imagined conditions, showing why acoustic similarity, recognized text and language-model post-processing must be assessed separately.

### Prior state of the art

Prior EEG imagined-speech work includes restricted-vocabulary recognition and reconstruction using overt-speech acoustic targets. Removing DTW from a Generator does not eliminate supervised timing assumptions, paired spoken targets, or the need to test novel linguistic content.

### What changed

Uses a subject-specific EEG embedding, encoder, local-context adapter and Mel decoder without explicit attention alignment or generated-speech feedback, followed by frozen HiFi-GAN and HuBERT components. Spoken-pretrained weights initialize a separate imagined-speech Generator; optional Llama correction and personalized xTTS resynthesis follow decoding.

### Position in the field

Non-invasive neural SSI reconstruction study with learned acoustic targets and downstream pretrained speech modules, not a demonstrated general-purpose or clinical communication interface.

### Practical value

Provides a concrete pipeline and separate acoustic/text evaluations for studying constrained imagined-speech reconstruction. Clinical utility and natural conversational performance remain untested.

### Advanced

Evaluates trial-level EEG-to-audio-to-text reconstruction under both overt and imagined production, with separate acoustic and text metrics, two utterance-duration conditions, and an explicit before/after correction analysis.

### Unresolved

Unseen words or sentences, new users, held-out sessions or cue blocks, imagined-speech-specific neural information versus cue or artifact effects, exact spoken-target pairing and preprocessing split isolation, reproducible model configuration, listener intelligibility and real-time assistive use.

### Narrowed or regressed

The 4-s condition has worse acoustic similarity than the 2-s condition, while its participants, stimulus composition and loss emphasis also differ. Acquisition uses a wet 130-channel cap in a shielded room, with long subject-specific training and offline whole-trial inference rather than practical streaming communication.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | Offline reconstruction of cued overt and imagined speech as audio and text. |
| Input | Non-invasive scalp EEG during overt speech and instructed subvocal imagination without overt muscle movement. Spoken audio supplies training/evaluation targets, not an inference input to the EEG Generator. |
| Sensor | EGI wet-type 130-channel high-density EEG, geodesic scalp montage, Cz reference, 250 Hz sampling, KCl wetting and nominal pre-recording impedance below 50 kΩ; spoken audio recorded at 44.1 kHz and processed at 22.05 kHz. |
| Body site | brain |
| Output | Reconstructed speech audio and ASR text; optional corrected text and personalized TTS resynthesis. |
| Vocabulary type | Closed, repeatedly cued stimulus classes; English words and sentences are listed, with participants described as native Korean speakers. |
| Vocabulary size | Ten classes per evaluated condition: five words plus five sentences at 2 s; ten sentences at 4 s after excluding ten word-only classes from the 20 collected classes. Number of unique lexical word types is not reported. |
| Metrics and results | Before correction/TTS, Table 1 imagined 2-s results (mean ± s.d.) are CER 0.2710 ± 0.0459, WER 0.4748 ± 0.0947, PCC 0.7484 ± 0.0522, RMSE 1.7163 ± 0.2308 and MCD 7.5284 ± 0.3200 dB. Table 2 imagined 4-s results are CER 0.2474 ± 0.0361, WER 0.4346 ± 0.0525, PCC 0.5834 ± 0.0584, RMSE 2.2331 ± 0.2605 and MCD 9.5125 ± 0.6660 dB. Spoken WER is 0.4466 ± 0.1064 at 2 s and 0.4893 ± 0.0948 at 4 s. Pooled spoken/imagined correction results: 2-s CER 0.2618→0.2487 and WER 0.4586→0.4451; 4-s CER 0.2763→0.2723 and WER 0.4870→0.4658. Word-position associations have p<0.01 in all conditions but R²≤0.02. These are reported values, not independently reproduced or reconciled pooled statistics. |
| Evaluation protocol | Offline subject-dependent training with random class-balanced train/validation/test allocation of 2:1:1 and no unseen classes. Tables 1 and 2 use 100 samples per subject and report CER, WER, PCC, RMSE and MCD before optional correction/TTS. Table 3 uses sentence-clustered regression for word-position effects; Tables 4 and 5 pool both speech modes to compare ASR output before and after language correction with ASR on recorded voice. |

### Limits

- **Technical:** Imagined trials lack contemporaneous acoustic ground truth and are supervised with overt recordings of the same content. Generator architecture and frozen ASR checkpoint details are incomplete. The source describes session-wise and trial-wise normalization, fixed loss weights and later adjustment of L1 weight, and normalized versus directly estimated Mel scales; these descriptions require implementation clarification. ICA is described but does not itself establish that decoding is independent of residual muscle activity or auditory-cue effects. MCD uses DTW despite the Generator's no-DTW framing.
- **Evaluation:** Random subject-specific 2:1:1 splits include every class in training, validation and test. Grouping of the four same-cue repetitions, session isolation and preprocessing fit boundaries are not specified. The 2-s participant count conflicts between Methods and Results. Duration conditions differ in cohort, vocabulary and training loss emphasis, so their differences cannot be attributed to duration alone. No shuffled-EEG, class-template or component-ablation baseline, clinical cohort or blinded listener test is reported. Pooled correction tables do not provide imagined-only gains or a transparent reconciliation with the separate-mode tables.
- **Deployment:** Wet electrodes require KCl preparation and stable scalp contact; subjects sit with minimal movement in a shielded laboratory. Processing and inference are offline and consume the entire EEG sequence. Reported training takes about 48 h per subject for 2-s tasks or 84 h for 4-s tasks on one RTX 4090. No latency, power, walking, patient communication or everyday-use evaluation is reported.
- **Scope of this review:** Twenty-page arXiv v1 full text; no independent execution of author experiments or external verification of data/code availability. Results concern cued 2-s word/sentence and 4-s sentence tasks, not spontaneous thought or unrestricted communication.

### Evidence

- Methods enroll 23 healthy Korean-native adults (20 male, three female), with 11 in the 2-s condition and 12 in the 4-s condition. Results instead describe ten subjects for 2-s evaluation, without explaining the difference. Acquisition is seated in a shielded room with wet EGI 130-channel scalp EEG at 250 Hz and a Cz reference. (Method: Participants and EEG Recording, PDF p. 3; 2-s/4-s speech condition, p. 6; Result before Table 1, p. 14)
- Each auditory cue is followed by a fixation/task pair repeated four times; participants overtly produce or imagine the cued content without overt vocalization. The 2-s condition has 400 trials per task over ten word/sentence classes; 4-s acquisition has 800 trials per task over 20 classes, but ten word-only classes are excluded from training and inference, leaving ten sentence classes. Split grouping of the same-cue repetitions is unspecified. (Experimental paradigm and Figure 1, PDF pp. 5–6; Dataset, p. 7; Result between Tables 1 and 2, p. 14)
- The dataset is randomly split 2:1:1 into training, validation and test with subject-specific training and all classes in every split, explicitly avoiding unseen classes. Imagined-speech acoustic targets are recordings of the same sentences from overt speech, not contemporaneous imagined audio. This is not an unseen-content or unseen-user evaluation. (Dataset, PDF pp. 6–7)
- The Generator consists of EEG embedding, encoder, local-context adapter and Mel decoder, without explicit attention alignment or output feedback. Frozen HiFi-GAN and HuBERT convert generated Mel representations to audio and text. Separate subject/mode Generators use spoken-to-imagined initialization and L1 plus CTC training; the paper reports no isolated component ablation. (EEG-to-Voice pipeline and Figure 2, PDF pp. 7–8; Training Loss Term and Figure 3, pp. 8–10; Result, pp. 13–19)
- No DTW inside the Generator is not equivalent to an alignment-free workflow: task annotations and CPU timestamps are explicitly used to verify synchronized EEG/audio segments, while MCD evaluation aligns reference and reconstructed mel-cepstral sequences with DTW after voice-activity filtering. (Signal Segmentation, PDF p. 4; EEG-to-Voice pipeline, p. 7; Evaluation Metrics: MCD, p. 12)
- Table 1 reports imagined 2-s mean ± s.d.: CER 0.2710 ± 0.0459, WER 0.4748 ± 0.0947, RMSE 1.7163 ± 0.2308, MCD 7.5284 ± 0.3200 and PCC 0.7484 ± 0.0522. Spoken CER is 0.2519 ± 0.0539 and WER 0.4466 ± 0.1064. Evaluation uses 100 samples per subject, mixing words and sentences, before optional correction and TTS. (Table 1 and surrounding Results, PDF p. 14; Language Model setting and TTS evaluation exclusions, pp. 11–12)
- Table 2 reports imagined 4-s mean ± s.d.: CER 0.2474 ± 0.0361, WER 0.4346 ± 0.0525, RMSE 2.2331 ± 0.2605, MCD 9.5125 ± 0.6660 and PCC 0.5834 ± 0.0584. Spoken CER is 0.2929 ± 0.0668 and WER 0.4893 ± 0.0948. Twelve subjects are evaluated with 100 sentence samples per subject. Compared with 2-s tasks, cohorts, stimulus composition and loss emphasis differ, so the acoustic decrease is not a controlled duration-only effect. (Table 2 and surrounding Results, PDF pp. 14–16; experimental condition cohorts, p. 6)
- Table 4 pools spoken and imagined outputs: at 2 s, CER changes from 0.2618 ± 0.0480 to 0.2487 ± 0.0504 and WER from 0.4586 ± 0.0968 to 0.4451 ± 0.0972 after correction. Table 5 pooled 4-s CER changes from 0.2763 ± 0.0658 to 0.2723 ± 0.0665 and WER from 0.4870 ± 0.0699 to 0.4658 ± 0.0788. These are not imagined-only correction results; the source does not transparently reconcile the pooled values with Tables 1 and 2. (Figure 7 caption and Tables 4–5 with captions, PDF pp. 18–19; separate-mode Tables 1–2, p. 14)
- Sentence-clustered word-position regression reports positive coefficients with p<0.01 in all conditions, but the source states R²≤0.02 and non-monotonic binned patterns. The imagined coefficients are 0.136 (SE 0.018, p<0.001) at 2 s and 0.051 (SE 0.015, p<0.01) at 4 s. Position explains only a small fraction of the decoding-error variation. (Figure 6, Table 3 and Word position effects on character error rate, PDF pp. 16–17)
- Llama-3.2-1B-Instruct generates five correction candidates, filters allowed characters, word-count changes and article preservation, and scores similarity to the original ASR text plus perplexity. The original text is retained as a candidate; these constraints are a design intent, not an independent test that every correction preserves meaning. Personalized xTTS-v2 resynthesis is auxiliary and excluded from primary quantitative evaluation. (Language Model setting, PDF pp. 10–11; TTS Model Few-shot Fine-tuning, pp. 11–12)
- The paper explicitly states that all generation is offline, without real-time constraints, using the entire EEG sequence. Training takes approximately 48 h per subject at 2 s or 84 h at 4 s on one RTX 4090, for about 1500 epochs. No real-time, power, walking, clinical communication or listener-intelligibility result is reported. (EEG-to-Voice pipeline, PDF pp. 7–8; Generator Training, p. 10; Participants/EEG Recording, p. 3; complete Results, pp. 13–19)
- Implementation details need clarification: normalization is described both per session and per trial; loss weights are described as fixed but L1 weight is later reduced when training is unstable; normalized Mel outputs and direct target-scale estimation are both described. Exact layer configuration, ASR checkpoint, loss coefficients, split isolation for preprocessing, cue-block/session holdout and imagined/overt trial pairing are not sufficiently specified for reproduction. (Neural signal processing, PDF pp. 3–4; Dataset, pp. 6–7; Pretrained Components, p. 8; Coefficient Tuning and Generator Training, pp. 9–10; Results, p. 14)
- ICA artifact removal is reported, but no shuffled-EEG, class-template, cue-specific or residual-muscle control is evaluated in Results. With repeated known classes and random within-subject splitting, the study does not establish decoding of arbitrary imagined sentences or performance on a new session, user or clinical population. This is a limitation of validation scope, not a claim that leakage or artifact dependence was demonstrated. (Neural signal processing, PDF p. 4; Experimental paradigm and Dataset, pp. 5–7; complete Results, pp. 13–19)
- The authors claim direct open-loop EEG-to-Voice reconstruction without DTW or explicit temporal alignment, comparable linguistic accuracy for spoken and imagined conditions, and minimal correction without semantic distortion. Their reported quantitative experiments are offline subject-specific tests of known cued stimuli and correction metrics pooled across speech modes. (Abstract, PDF p. 1; Introduction, p. 2; Dataset and pipeline, pp. 7–8; Figure 7 and Tables 4–5, pp. 18–19)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
