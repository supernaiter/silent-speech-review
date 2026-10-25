# Silent versus modal multi-speaker speech recognition from ultrasound and video

Manuel Sam Ribeiro, Aciel Eshky, Korin Richmond, Steve Renals  
arXiv / imported corpus page 2021 · [arXiv](https://arxiv.org/abs/2103.00333)

**Section:** [Ultrasound & tongue imaging](../README.md#ultrasound--tongue-imaging) · **Review basis:** full_text

Speech recognition from ultrasound tongue imaging and lip video on TaL80 and TaL1; adaptation lowers multi-speaker silent WER from 77.79 to 69.84 versus 39.34 for modal speech, showing a large silent-mode gap.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Ultrasound probe and lip camera |
| Task | Speech recognition (modal, silent, whispered) |
| Vocabulary | Open vocabulary |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Silent WER 69.84 (TaL80, fMLLR+adaptation) vs modal 39.34; TaL1 speaker-dependent silent WER 37.94 |

**Limitations.** Silent-speech WER remains far from usable; relies on careful probe placement, corpus-style recording and adaptation, with no live interface evaluation.

## Full review

### In short

Large-corpus baseline with real silent-mode gap.

### Review

The paper is valuable because it does not hide the hard part. Even on the larger TaL80 setup, silent WER remains much worse than modal WER, and adaptation only partly closes the gap. That is a credible result, not a failure: it shows exactly where multi-speaker ultrasound SSI breaks. The secondary analysis matters too, because it confirms that silent speech is slower and occupies a smaller articulatory space, which helps explain why modal-trained recognizers transfer poorly.

### Why it matters

The strongest contribution is not headline WER but the diagnosis that silent speech is slower, occupies a smaller articulatory space, and benefits from adaptation but remains far harder than modal speech.

### Prior state of the art

Ultrasound-plus-video SSI work was often small-scale, single-speaker, and weak on speaking-mode mismatch.

### What changed

Moves to an 82-speaker corpus and treats silent-versus-modal mismatch as a domain adaptation problem with articulatory analysis alongside recognition.

### Position in the field

Core multi-speaker ultrasound SSI recognition paper.

### Practical value

Useful as a realistic benchmark for silent-versus-modal mismatch and for judging what classical adaptation buys on larger ultrasound corpora.

### Advanced

benchmark scale; evaluation; adaptation analysis

### Unresolved

real-time interaction; robustness to probe shift; in-the-wild generalization

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech recognition from ultrasound and lip video |
| Input | ultrasound tongue imaging and lip video |
| Sensor | ultrasound probe and camera |
| Body site | lip; tongue |
| Output | text |
| Vocabulary type | open-vocabulary ASR |
| Metrics and results | On TaL80 multi-speaker, silent WER drops from 77.79 raw to 69.84 with fMLLR plus unsupervised adaptation, while modal WER is 39.34 raw; on TaL1 speaker-dependent, silent WER falls from 52.64 raw to 37.94 |
| Evaluation protocol | TaL80 multi-speaker and TaL1 speaker-dependent WER across modal, silent, and whispered speech with articulatory-space analysis |

### Limits

- **Technical:** Performance is still far from usable for many silent conditions, and the pipeline relies on careful ultrasound capture plus external adaptation tricks.
- **Evaluation:** No live interface evaluation or end-user task is reported.
- **Deployment:** Portable deployment remains unclear because the system still depends on probe placement and corpus-style recording conditions.
- **Scope of this review:** Recognition from ultrasound and video under controlled corpus recording.

### Evidence

- The TaL corpus contains six sessions from one professional speaker in TaL1 and single-session recordings from 81 additional native English speakers in TaL80. (2. The TaL corpus)
- On TaL80 multi-speaker evaluation, silent WER improves from 77.79 raw to 69.84 with fMLLR plus unsupervised adaptation, while modal raw WER is 39.34. (Table 1: Word error rate on modal, silent, and whispered speech)
- The analysis finds significant speaking-mode differences in syllable rate and convex-hull articulatory space, but those differences do not directly correlate with WER differences. (4. Analysis)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
