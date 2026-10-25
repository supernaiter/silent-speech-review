# CS-ETS: Chaos-Inspired Samba-Based EMG-To-Speech Synthesis with Nonlinear Chaotic Losses

Sajid Fardin Dipto, Tarikul Islam Tamiti, David Vergano, Luke Baja-Ricketts, Anomadarshi Barua  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2607.18629)

**Section:** [Surface EMG](../README.md#surface-emg) · **Review basis:** full_text+summary

Smaller chaos-inspired Samba-based EMG-to-speech model with nonlinear losses; WER improves modestly from 42.20% to 41.26% while parameters drop from 54.10M to 32.03M.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Existing 8-channel facial EMG corpus |
| Task | Speech synthesis from EMG |
| Vocabulary | Open-vocabulary EMG corpus; size not specified |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 41.26% WER vs 42.20% baseline; 32.03M parameters |

**Limitations.** Single speaker and dataset; large acoustic-metric gains confounded by target-audio alignment applied only to the proposed output; insufficient split details and no confidence intervals.

## Full review

### In short

A smaller EMG-to-speech model with a modest reported WER gain; large acoustic-metric gains are confounded by reference-based alignment applied asymmetrically.

### Review

CS-ETS is a potentially useful compact EMG-to-speech model, but its strongest numerical claims require careful separation. The reported model size falls from 54.10M to 32.03M parameters, while WER improves only from 42.20% to 41.26%, a 0.94-percentage-point change without reported uncertainty. Within the smaller architecture, adding both temporal losses reduces WER from 50.37% to 41.26%, which is a more informative ablation than the broad chaos-theory framing. The headline acoustic improvements are less secure: Table 1 applies post-vocoder alignment to the proposed method but not to the baselines. Table 3 shows that alignment alone moves STOI from 0.15 to 0.61 and LSD from 1.92 to 1.10 while WER stays 50.37%. This is reference-dependent evaluation processing, not an independent recognition gain or a deployable correction of speech timing. The SI-SDR change from -41.96 to -33.41 dB is an 8.55 dB difference; interpreting the ratio of negative dB values as a 1.25-fold noise-reduction benefit is inappropriate. Human MOS is reported as 4.21 versus 3.98 from ten listeners, distinct from the automated NISQA values, but sampling and uncertainty are not detailed. Results come from one English speaker and one corpus, and the paper does not restate exact train/test counts. The contribution should therefore be treated as a promising compression and regularization study awaiting a matched-alignment evaluation, rather than proof that chaotic physics delivers large general speech-quality improvements.

### Why it matters

The compact model and paired-loss ablation warrant reproduction; the alignment ablation also demonstrates how evaluation processing can dominate apparent acoustic improvements.

### Prior state of the art

Gaddy-style EMG-to-speech systems use aligned vocalized targets, mel reconstruction and phoneme supervision. The paper compares retrained 2020/2021 models and reports another published streaming baseline.

### What changed

Adds two nonlinear temporal regularizers to a compact hybrid state-space/attention encoder and introduces reference-dependent waveform alignment for evaluation.

### Position in the field

Directly relevant EMG-based articulatory SSI synthesis and model-efficiency research, with substantial evaluation qualifications.

### Practical value

A compact architecture worth reproducing on a fully specified benchmark with identical evaluation processing across methods.

### Advanced

Model compression and a loss-ablation study on EMG-to-speech; explicit attention to waveform alignment during objective evaluation.

### Unresolved

Matched alignment for all models, exact held-out protocol, significance across seeds/listeners, cross-speaker transfer, end-to-end real-time operation and field noise.

### Narrowed or regressed

Without the added losses, the smaller architecture has worse WER than the comparison baseline. The full model only modestly improves WER and does not improve every quality metric.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | emg |
| Sensor | Eight-channel facial EMG from an existing corpus; workstation training on two RTX 4090 GPUs. No new wearable sensing system. |
| Body site | face; throat |
| Output | speech-audio |
| Vocabulary type | open-vocabulary EMG corpus |
| Vocabulary size | Not specified in this paper. |
| Metrics and results | Tables 1-3: model parameters 54.10M to 32.03M; WER 42.20% to 41.26%; FLOPs 2.40G to 2.08G; batch inference 5.97 to 5.55 ms for 200 time steps; RTF 0.0057 for both. Alignment-only ablation: STOI 0.15 to 0.61 and LSD 1.92 to 1.10 with WER unchanged at 50.37%. Human MOS: 4.21 versus 3.98 with ten listeners; no confidence intervals. All results author-reported, not independently reproduced. |
| Evaluation protocol | Author-retrained baselines, loss/channel/layer ablations, WER, aligned waveform metrics and computational counts; ten-person listening panel. |

### Limits

- **Technical:** Target-dependent evaluation alignment, unspecified timing boundaries and train/test details, weak absolute acoustic metrics, and an unverified chaos-mechanism explanation.
- **Evaluation:** One speaker and one dataset, insufficient split details, no reported confidence intervals or repeated seeds. Main acoustic metrics compare aligned proposed output with unaligned baselines. Ten-listener MOS lacks sample-count and uncertainty details. Table 3 single-loss labels conflict with explanatory prose.
- **Deployment:** Training and timing use a workstation setting; no prospective wearable interaction, noisy-environment, walking or clinical-user study. Target-audio-dependent post-vocoder alignment is unavailable during ordinary deployment.
- **Scope of this review:** Single-speaker offline EMG-to-speech experiments; waveform alignment uses target audio and cannot be assumed available at inference.

### Evidence

- The experiments use an eight-channel EMG input and describe a 19-hour open-vocabulary corpus from one English speaker across silent and vocalized speech. Exact train/test counts are not restated. (Sections 2 and 3.1; PDF pp. 2-3)
- Table 1 reports 32.03M parameters and 41.26% WER for CS-ETS versus 54.10M and 42.20% for the retrained 2021 baseline. Reviewer calculation: the WER difference is 0.94 percentage points. (Table 1; PDF p. 3)
- Table 1 marks post-vocoder alignment as present only for CS-ETS and absent for the baselines. Reviewer assessment: acoustic-metric comparisons combine model changes with unequal evaluation processing. (Section 2.4 and Table 1; PDF p. 3)
- In Table 3, adding alignment without either new loss changes LSD from 1.92 to 1.10 and STOI from 0.15 to 0.61, while WER remains 50.37%; adding both losses yields 41.26% WER. (Table 3 rows P1, P2 and P5; PDF p. 4)
- Post-vocoder alignment computes DTW between generated and target audio and reconstructs the aligned signal. Reviewer assessment: reference-dependent alignment is evaluation processing, not an available correction for ordinary unseen-input deployment. (Section 2.4; PDF p. 3)
- Table 2 reports 2.08G versus 2.40G FLOPs, 5.55 versus 5.97 ms batch inference, and identical RTF 0.0057. Section 3.3 defines the timing input as 200 time steps; full pipeline timing boundaries are not established. (Section 3.3; Table 2; PDF pp. 3-4)
- A panel of ten people gives human MOS 4.21 for CS-ETS versus 3.98 for the baseline. This is distinct from Table 1 automated NISQA-MOS 3.31 versus 3.30; listening sample counts and confidence intervals are not reported. (Section 5; Tables 1 and 3; PDF pp. 3-4)
- Table 3 assigns 49.45% WER to the configuration without MSDFA and 48.65% to the configuration without LER, while its explanatory prose associates the individual losses in the reverse way. (Section 4.3(a), Table 3 and following paragraph; PDF p. 4)
- SI-SDR is reported as -41.96 versus -33.41 dB. Reviewer calculation: the difference is 8.55 dB; dividing those negative dB numbers does not establish a 1.25-fold physical noise-reduction factor. (Introduction; Section 4.1; Table 1; PDF pp. 1 and 3)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
