# Digital Voicing of Silent Speech

['', '']  
arXiv / imported corpus page 2020 · [arXiv](https://arxiv.org/abs/2010.02960)

**Section:** [Surface EMG](../README.md#surface-emg) · **Review basis:** full_text

Synthesizes speech from silent facial EMG by transferring audio targets from vocalized recordings; human WER reaches 3.6% on closed vocabulary, while open-vocabulary WER drops from 95.1% to 74.8%.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Facial and throat surface EMG electrodes |
| Task | Speech synthesis from silent EMG |
| Vocabulary | Closed dates/times set; open vocabulary of 9828 words |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 3.6% human WER closed vocabulary; 74.8% human WER open vocabulary |

**Limitations.** Speaker-dependent with substantial data collection; open-vocabulary WER remains high and all results come from the authors' own data setup.

## Full review

### In short

Core EMG SSI paper with real gains from target transfer.

### Review

The full text backs a strong SSI claim: the target-transfer pipeline is the key step that makes silent EMG viable for speech reconstruction instead of merely hoping a model trained on vocalized EMG will transfer. The closed-vocabulary result is genuinely strong, and the open-vocabulary numbers remain difficult but materially better than baseline. The main remaining weakness is generalization: the setup is speaker-dependent, performance in open vocabulary is still rough, and the system depends on relatively heavy data collection and alignment machinery.

### Why it matters

Strong EMG SSI paper showing that silent EMG can produce intelligible speech if training explicitly handles the mismatch between silent and vocalized articulations.

### Prior state of the art

Prior EMG-to-speech work largely trained on vocalized EMG and transferred poorly to silent EMG because aligned speech targets were missing.

### What changed

Introduces target transfer, CCA alignment, and predicted-audio refinement so silent EMG can train a speech generator directly.

### Position in the field

Core EMG silent-speech reconstruction paper with clear methodological relevance to SSI.

### Practical value

Important evidence that alignment strategy, not just model size, is the bottleneck in silent-EMG-to-speech generation.

### Advanced

system_design; problem_reframing; evaluation

### Unresolved

Cross-speaker transfer; lighter sensors; better open-vocabulary intelligibility

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | surface emg |
| Sensor | facial EMG electrodes |
| Body site | face; jaw; throat |
| Output | speech-audio |
| Vocabulary type | closed vocabulary dates/times plus open vocabulary book text |
| Vocabulary size | 9828 words in open-vocabulary condition |
| Metrics and results | Closed-vocabulary human WER reaches 3.6% with a 94% relative error reduction from the strongest baseline; open-vocabulary human WER drops from 95.1% to 74.8%; automatic open-vocabulary WER drops from 91.2% to 68.0% |
| Evaluation protocol | human transcription WER, automatic ASR WER, and ablations on data size and electrode subsets |

### Limits

- **Technical:** Speaker-dependent setup with substantial data collection and still-high WER in open-vocabulary conditions.
- **Evaluation:** Open-vocabulary outputs remain far from production quality, and all results come from the authors' data collection setup.
- **Deployment:** Requires facial EMG instrumentation and a speaker-specific training pipeline.
- **Scope of this review:** Silent EMG to speech reconstruction only.

### Evidence

- The paper studies digital voicing of silent speech from facial EMG and proposes target transfer from vocalized recordings so silent EMG can train a speech generator. (Abstract)
- Section 3.2 explains that audio target transfer aligns silent and vocalized EMG so silent EMG can receive speech targets, which is the core step that differentiates the method from direct transfer baselines. (3.2   Audio Target Transfer)
- The closed-vocabulary human evaluation reports 3.6% WER for the full model, described as a 94% relative error reduction from the strongest baseline. (4.1    Closed Vocabulary Condition)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
