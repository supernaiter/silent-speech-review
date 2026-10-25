# EMG-to-Speech with Fewer Channels

Injune Hwang, Jaejun Lee, Kyogu Lee  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2602.06460)

**Section:** [Surface EMG](../README.md#surface-emg) · **Review basis:** full_text+summary

Channel-reduction study for EMG-to-speech using exhaustive subset search and full-channel pretraining; best four-channel subsets reach about 47.2% WER versus roughly 35% with all eight channels.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Subsets of 8-channel face/neck surface EMG |
| Task | Speech synthesis from EMG |
| Vocabulary | Open vocabulary; size not reported |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 47.2% WER, best 4-channel subset (full-channel ~35%) |

**Limitations.** Single subject; subset selection not clearly independent of reporting; no repeated runs or physically built reduced-channel device.

## Full review

### In short

Exhaustive subset search shows useful channel complementarity, and full-channel pretraining helps smaller EMG inputs. Single-person evaluation, unclear selection independence and a dropout text/figure conflict limit layout recommendations.

### Review

The useful result is that sensor selection is a joint prediction problem: channel 6 is removed first by greedy elimination yet belongs to the best four-channel subset, while channel 3 appears in nine of the ten highest-ranked subsets. Evaluating all seventy combinations is a meaningful improvement over a partial search, and the paper shows why a ranking of individual channel importance should not be treated as an optimal device layout. The best from-scratch four-channel combination, 1/3/5/6, reaches 47.2% recognizer-derived WER; full-channel pretraining reduces the penalty of using four to six channels, but the plotted reduced-channel results remain above the roughly 35% eight-channel reference. Transfer learning and channel dropout must also be separated: plain pretraining already helps, and the paper does not show that added dropout always improves it. In fact, Section 5.4 says no dropout is best with four channels, whereas Figure 3 places the 0.125-dropout curve lowest there. That discrepancy needs source results before selecting a training policy. The phoneme analysis is valuable as a complementary diagnostic, but category errors and surface-electrode locations do not isolate causal contributions of particular muscles; silence is included in the overall phoneme error, and channel importance differs from the synthesis-WER ranking. Finally, all results come from one existing participant and virtually removed channels. The work offers a credible training and sensor-search baseline, while independent subset validation and a genuinely reduced wearable recording study remain necessary before claiming a practical sensor layout.

### Why it matters

Makes channel interactions and task-dependent sensor utility explicit, rather than equating individually important channels with the best low-channel system.

### Prior state of the art

Gaddy-style EMG-to-speech already maps facial/neck muscle signals to acoustic features with phoneme supervision and a vocoder. Reduced-channel subsets and dropout are established ideas; channel information depends on interactions and the downstream objective.

### What changed

Completes the full four-of-eight subset search and compares random initialization with full-channel pretraining at dropout probabilities 0, 0.125 and 0.25.

### Position in the field

Single-participant EMG-to-speech benchmark analysis aimed at fewer facial/neck sensors.

### Practical value

Useful for selecting candidate electrode combinations and pretraining baselines; current evidence cannot prescribe a universally best four-channel device.

### Advanced

Evaluates all seventy four-channel subsets, demonstrates that greedy channel importance does not determine the best combination, and improves four-to-six-channel WER through fine-tuning.

### Unresolved

Independent subset-selection/test separation, repeated-seed uncertainty, cross-person/session robustness, exact reduced-input checkpoint adaptation, and actual reduced-electrode hardware usability.

### Narrowed or regressed

Reducing sensors still increases synthesis WER relative to the full eight-channel reference. Dropout is not uniformly beneficial relative to ordinary pretraining, and the best four-channel setting is inconsistent between text and figure.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | Surface electromyography from selected channels of an eight-channel face/neck array; voiced acoustic targets and phoneme labels are training supervision. |
| Sensor | Eight existing surface-EMG channels distributed across cheeks, chin and throat, with retrospective subsets. Figure 1 lists positions including left cheek, left chin, below chin, throat and right facial sites; physical reduced-channel acquisition is not tested. |
| Body site | face;neck |
| Output | speech-audio |
| Vocabulary type | continuous open-vocabulary corpus speech |
| Vocabulary size | Not reported for the evaluated open-vocabulary subset. |
| Metrics and results | Table 1 four-channel WER: subset 1356 47.2%, 2357 47.3%, 1346 47.7%; at least ten combinations outperform greedy 1234. Table 2 inclusion-average WER: channel 3 51.4%, channel 2 52.3%, channel 1 52.6%, channel 5 52.8%. Table 3 total phoneme error 16.0% with eight channels and 17.1% after removing channel 8; silence 4.5% versus 5.8%. Figure 3 places the full-channel WER reference at approximately 35%; exact fine-tuned numeric values are not tabulated. Author-reported, not independently reproduced. |
| Evaluation protocol | Offline channel-ablation study with greedy backward elimination, exhaustive four-channel search, direct phoneme-head category errors, and HiFi-GAN synthesis transcribed by Whisper medium. |

### Limits

- **Technical:** Automatic WER combines encoder, vocoder and recognizer errors. Anatomical assignments are interpretations of broad surface recordings. Paper describes resizing the first convolution for reduced inputs but does not fully specify pretrained weight transfer. Exact checkpoint, optimization schedule and result split are not provided in the paper.
- **Evaluation:** One subject, no explicit sample counts or independent split for choosing among seventy subsets versus reporting their final WER. No repeated-run intervals, statistical tests or human listening study. Frame/category phoneme errors are not interchangeable with synthesized-speech WER. Figure 3 conflicts with Section 5.4 about the best dropout setting at four channels.
- **Deployment:** Retrospective channel removal from a fixed eight-channel recording setup; no physically redesigned four-channel device, latency, power, comfort or clinical communication trial.
- **Scope of this review:** Existing one-person open-vocabulary dataset and offline synthesized-speech evaluation; no new clinical, multi-person, mobile or real-world recording study.

### Evidence

- The study evaluates all seventy four-of-eight channel subsets and compares them with greedy backward elimination. (Sections 3.1.1-3.1.2 and 5.2; PDF pp. 2-4)
- Experiments reuse a single-subject dataset, retaining approximately sixteen hours of open-vocabulary data and excluding the closed-vocabulary portion. (Section 4.1; PDF p. 3)
- Table 1 reports WER 47.2% for subset 1356, 47.3% for 2357 and 47.7% for 1346; channel 3 appears in nine of the top ten subsets. (Table 1; PDF p. 3)
- Channel 6 is removed first in greedy elimination but appears in the best four-channel subset. Reviewer assessment: individual elimination rank does not determine optimal combinations. (Sections 5.1-5.2; Table 1; PDF pp. 3-4)
- Table 3 total phoneme error is 16.0% for the eight-channel baseline and 17.1% after the worst single-channel removal, channel 8. Silence is included and has 4.5% baseline error. (Table 3; PDF p. 4)
- The phoneme analysis assigns ablation effects to nearby muscles from approximate electrode locations. Reviewer assessment: these observations do not isolate individual-muscle causality or match the synthesis-WER channel ranking. (Section 5.3; PDF p. 4)
- Fine-tuning is compared with random initialization for selected four-to-seven-channel subsets, using independent training-time channel dropout probabilities 0, 0.125 and 0.25 during full-channel pretraining. (Section 3.2 and Section 5.4; PDF pp. 3-4)
- Section 5.4 states that no dropout is best at four channels, but Figure 3 plots the 0.125-dropout green curve lowest at four channels. Reviewer assessment: exact source results are needed before endorsing the stated best setting. (Section 5.4 and Figure 3; PDF p. 4, rendered and visually inspected)
- Dataset and experimental sections do not identify separate final evaluation data for selecting the best among seventy subsets, nor report repeated-seed uncertainty. Reviewer assessment: independence of selection and performance estimation remains unverified. (Sections 3-5; PDF pp. 2-4)
- The reported evaluation removes channels from existing recordings and measures synthesized-speech WER with Whisper medium; no reduced-array hardware or user communication trial is presented. (Sections 4.2-6; PDF pp. 3-4)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
