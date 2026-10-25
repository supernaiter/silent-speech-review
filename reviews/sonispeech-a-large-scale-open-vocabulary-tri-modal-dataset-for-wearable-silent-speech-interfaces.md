# SoniSpeech: A Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces

Ruidong Zhang, Jiacheng Liu, François Guimbretière, Cheng Zhang  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2608.00803)

**Section:** [Acoustic, whisper & wearable motion sensors](../README.md#acoustic-whisper--wearable-motion-sensors) · **Review basis:** full_text+summary

Single-speaker open-vocabulary dataset (ultrasound echoes, audio, video) from eyeglass-mounted sensors; an echo-only baseline trained on mixed voiced/silent data reaches 26.3% WER on silent speech.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Eyeglass-frame ultrasound speakers/microphones (FMCW echoes), audio, video |
| Task | Dataset; silent speech recognition |
| Vocabulary | Open vocabulary, 5,356 word types |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 26.3% silent WER with mixed voiced/silent training (78.4% voiced-only training) |

**Limitations.** Single author in one quiet setting; population and everyday-environment generalization untested; baseline uses echoes only, not trimodal fusion; no latency or power measurements.

## Full review

### In short

A useful single-speaker open-vocabulary eyewear dataset: mixed voiced/silent training reaches 26.3% silent WER, but population and everyday-environment generalization remain untested.

### Review

SoniSpeech is most valuable as shared training and evaluation data for acoustic-sensing eyewear, not as proof that an everyday silent-speech product is ready. It records ultrasound echoes, audio and frontal video in parallel voiced and strictly silent modes, using conversational sentence material. The headline 34.1 hours is session duration; usable utterances total 26.7 hours, and all recordings come from one fluent English-speaking author in one quiet environment. The central baseline result is 26.3% WER on silent test speech when training with both voiced and silent data, compared with 33.7% for silent-only training. A model trained only on voiced data reaches 78.4% WER on silent speech, demonstrating a large domain gap rather than successful zero-shot transfer. The dataset includes 242 test word types absent from its declared training texts, but no separate error rate on those words is reported. The benchmark uses the first 140 sessions per mode, and the paper discloses microphone problems in later training sessions. Walking and multi-user claims are borrowed from earlier EchoSpeech work, not tested at SoniSpeech's vocabulary scale. The corpus creates a useful platform for larger-vocabulary SSI and cross-modal methods; generalization, natural speech disfluencies, realistic environments and deployment costs remain unverified.

### Why it matters

Makes synchronized non-contact acoustic-sensing data available at a scale suitable for open-vocabulary research and quantifies the voiced/silent mismatch.

### Prior state of the art

The paper contrasts large contact-sensor SSI corpora with small-command acoustic-eyewear studies such as EchoSpeech; existing ultrasound-tongue corpora use different hardware and are not direct accuracy comparators.

### What changed

Provides paired voiced/silent acoustic echoes plus audio and frontal video at open-vocabulary scale in an eyewear form factor, with a reproducible single-speaker recognition benchmark.

### Position in the field

Non-invasive articulatory SSI dataset and acoustic-eyewear benchmark; directly relevant to open-vocabulary wearable speech input.

### Practical value

Provides a concrete training benchmark and paired modalities for domain adaptation and fusion, with clear known limitations.

### Advanced

Dataset scale and access for acoustic eyewear, conversational vocabulary coverage, parallel speech modes, and measurable voiced-to-silent transfer gaps.

### Unresolved

Multi-user transfer, noisy/mobile conditions, re-donning and placement variation, spontaneous articulation, and clinical use.

### Narrowed or regressed

No demonstrated regression versus another system under matched conditions; the dataset trades population diversity for within-speaker scale.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | dataset; speech-recognition |
| Input | Ultrasound acoustic echoes for baseline recognition; synchronized audible audio and frontal video also recorded. |
| Sensor | Two speakers and two ultrasound microphones on an eyeglass frame; FMCW bands 18-28 and 29-39 kHz at 5 ms period, 100 kHz audio sampling, four differential-echo channels at 200 Hz and 80 range bins; laptop camera at 1080p/30 fps. |
| Body site | face; lip |
| Output | text |
| Vocabulary type | open-vocabulary conversational English sentence prompts |
| Vocabulary size | 5,356 word types overall; 1,000 subword output units. |
| Metrics and results | Table 3 silent-test WER: voiced-only training 78.4%, silent-only 33.7%, mixed 26.3%. Voiced-test WER: 16.9%, 55.7%, 15.8%, respectively. Table 2: 5,356 total word types, 5,114 train and 1,684 test types, 242 test OOV types; 39/39 ARPABET phonemes. Session duration 34.1 h versus valid utterance duration 26.7 h. Author-reported results, not independently reproduced. |
| Evaluation protocol | Within-speaker evaluation on held-out sentence/session sets; three training-mode combinations and training-data scaling; greedy CTC WER without an external language model. |

### Limits

- **Technical:** Large voiced/silent mismatch, recorded microphone failures, and fixed-user/fixed-environment training; the echo-only baseline does not evaluate trimodal fusion.
- **Evaluation:** Single author, one quiet setting, re-recorded disfluencies and errors, no reported multi-seed uncertainty. Baselines use the first 140 sessions per mode, not every recorded training session. Tokenizer training is described as using the transcript corpus without explicitly stating train-only scope.
- **Deployment:** Custom frame, microcontroller/audio board and laptop capture; no measured recognition latency, power consumption, mobile inference or real-world communication study.
- **Scope of this review:** One author, read and corrected English sentence prompts, controlled quiet environment, baseline uses acoustic echoes only despite trimodal recording.

### Evidence

- All data come from one non-native but fluent English-speaking author in a controlled quiet environment, with parallel voiced and strictly silent modes. Errors and disfluencies were re-recorded. (Section 3.3; PDF p. 3)
- The dataset has 18,000 utterances and 34.1 hours of session-level recordings but 26.7 hours of valid utterance recordings; these durations should not be conflated. (Sections 3.3-3.4; Table 2; PDF p. 3)
- Silent-test WER is 78.4% after voiced-only training, 33.7% after silent-only training, and 26.3% after mixed voiced/silent training. (Table 3; Section 5.1; PDF p. 4)
- The released sentence corpus has 8,000 training and 1,000 test texts per mode, 5,356 unique word types overall and 242 test word types absent from the training texts. No OOV-specific WER is reported. (Sections 3.2-3.4; Table 2; PDF p. 3)
- Microphone channel 1 has high noise in the last 20 silent and last 11 voiced training sessions. The baseline configurations use the first 140 sessions of each mode. (Section 3.3; Section 4.2; Section 5.2; PDF pp. 3-4)
- The corpus synchronizes ultrasound echoes, audible audio and frontal video; its baseline uses four-channel differential echoes with ResNet-34 and CTC, greedy decoding and no external language model. (Sections 3.1, 3.5 and 4; PDF pp. 2-4)
- The discussion cites earlier EchoSpeech walking, noise and multi-user results, whereas SoniSpeech itself uses one speaker and one quiet environment. Reviewer assessment: those robustness claims cannot be transferred to this open-vocabulary benchmark. (Section 6; PDF p. 4)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
