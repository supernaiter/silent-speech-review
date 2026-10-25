# An Improved Model for Voicing Silent Speech

David Gaddy, Dan Klein  
arXiv / imported corpus page 2021 · [arXiv](https://arxiv.org/abs/2106.01933)

**Section:** [Surface EMG](../README.md#surface-emg) · **Review basis:** full_text

Improves open-vocabulary silent-speech voicing from facial EMG using learned convolutional features, a Transformer and auxiliary phoneme loss, cutting WER from 68.0% to 42.2% (automatic) and 32.3% (human) for one speaker.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Facial surface EMG electrodes |
| Task | Speech synthesis from silent EMG |
| Vocabulary | Open vocabulary |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 42.2% automatic WER, 32.3% human WER (from 68.0%), single speaker, open vocabulary |

**Limitations.** Single-speaker lab data only; no cross-session or cross-speaker evaluation, wearable or mobility tests; human evaluation used only 40 samples and two raters.

## Full review

### In short

This paper substantially improves open-vocabulary silent speech voicing using learned convolutional EMG features, Transformer modeling, and phoneme supervision, reducing WER from 68.0% to 42.2% automatic and 32.3% human in a single-speaker lab setting.

### Review

This paper presents a noteworthy advancement in open-vocabulary silent speech voicing using facial EMG from a single speaker. By shifting from hand-designed EMG features to learned convolutional features, introducing a Transformer architecture for improved temporal context, and adding an auxiliary phoneme prediction loss, the authors achieve a substantial 25.8% absolute reduction in WER—from 68.0% to 42.2% automatic and further to 32.3% in human transcription. Ablation experiments convincingly show that each component contributes to performance gains. The phoneme confusion and articulatory feature analyses provide valuable insights into model errors, showing persistent challenges with voicing and nasality distinctions, consistent with prior findings. Despite these gains, the work's scope is currently limited to a single speaker and session-dependent setting without evaluation of speaker independence, multi-session robustness, or practical deployment considerations such as wearable stability or mobile use. Thus, while this represents a strong speaker-dependent EMG silent-speech reconstruction baseline and advances evaluation practices, substantial work remains to achieve robust, generalizable, and deployable silent speech prosthetics.

### Why it matters

Provides a strong step forward in speaker-dependent facial EMG silent speech reconstruction, demonstrating the value of learned features, Transformer architectures, and auxiliary phoneme prediction loss to substantially lower WER and improve intelligibility over prior work.

### Prior state of the art

Prior work used hand-crafted facial EMG features with recurrent LSTM-based models achieving 68.0% WER in open-vocabulary silent speech voicing.

### What changed

Replaces hand-designed features with learned convolutional features, swaps LSTM with Transformer layers, and adds auxiliary phoneme prediction loss during training.

### Position in the field

Strong speaker-dependent facial EMG silent speech reconstruction paper demonstrating large intelligibility improvements in open-vocabulary synthesis.

### Practical value

Serves as a strong open-vocabulary facial EMG voicing baseline and demonstrates the efficacy of learned EMG feature extraction and auxiliary phoneme supervision; useful for single-speaker experimental research but not yet practical deployment.

### Advanced

Model quality and open-vocabulary intelligibility improved significantly; also adds detailed phoneme-level error analysis.

### Unresolved

Speaker independence and session robustness remain unaddressed; wearable practicality and long-term use not evaluated.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | emg |
| Body site | face |
| Output | speech-audio |
| Metrics and results | Primary metric is word error rate (WER) evaluated both automatically and by human transcription; ablations report WER values of 45.2%, 46.0%, and 51.7% when specific components are removed. |
| Evaluation protocol | Automatic and human transcription evaluations using word error rate (WER) on open-vocabulary silent speech synthesis from facial EMG. |

### Limits

- **Technical:** Model trained on single speaker without addressing speaker independence or robustness across sessions; no wearable or real-world mobility evaluation; phoneme distinctions like voicing remain challenging.
- **Evaluation:** Human evaluation on only 40 silent speech samples with two raters; no session-independent or cross-speaker evaluation; automatic WER metric validated but still limited.
- **Deployment:** Single-speaker lab data only; no tests on wearable electrodes, mobility, or long-term recalibration; no cross-session or cross-speaker evaluation.
- **Scope of this review:** Single speaker, facial EMG signals, open-vocabulary silent speech voicing only.

### Evidence

- Improves silent-speech voicing by replacing hand-designed EMG features with learned convolutional features, using a Transformer, and adding a phoneme auxiliary loss. (Abstract)
- Our model improves WER absolute by 25.8% from prior 68.0% to 42.2% as measured by automatic transcription, with human transcription averaging 32.3% WER on held-out samples. (3 Results)
- The gain comes from replacing hand-crafted EMG features by convolutional feature extraction, employing a Transformer encoder on top, and adding an auxiliary phoneme prediction loss to improve learning. (2 Model)
- All data is from a single English speaker with 19 hours of facial EMG recordings in silent and vocalized speech; evaluation includes open-vocabulary automatic WER and human transcription on 40 samples by two raters; no cross-speaker or multi-session tests reported. (3 Results)
- The system is limited to a single speaker, no session or speaker independence evaluation, and lacks tests for wearable robustness, mobility, or long-term recalibration. (5 Conclusion)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
