# iPhoneme: Brain-to-Text Communication for ALS Using ConformerXL Decoding

Yoonmin Cha, Dawit Chun, Sung Park  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2604.16441)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text+summary

ConformerXL-based intracortical brain-to-text decoding for ALS with a proposed gaze-confirmation interface; WFST decoding reaches 7.86% phoneme error rate retrospectively in one participant.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Four implanted 64-electrode intracortical microelectrode arrays |
| Task | Brain-to-text decoding |
| Vocabulary | 42 phoneme classes; word vocabulary not reported |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 7.86% PER with WFST (180 ms); 26.61% word error |

**Limitations.** No clearly independent final test (validation informs tuning); single participant, retrospective; noncausal model; latency incompletely measured; gaze interface not user-validated.

## Full review

### In short

A promising decoder and gaze-confirmation concept, with reported 7.86% phoneme error but no clearly independent final test, complete latency measurement or user validation of the interface.

### Review

iPhoneme combines a plausible intracortical sequence-decoding architecture with an interesting interaction proposal: gaze points to a target while an intentionally produced phoneme confirms a selection or gesture. The reported decoding progression reduces phoneme error from 10.62% with greedy output to 7.86% with WFST search, while word error remains 26.61%. Those results require a qualified interpretation. The paper explicitly uses validation-set confusion patterns to inform language-model corrections and explores 150 decoder configurations, yet does not establish a separate untouched final evaluation; official test labels are unavailable. The architecture itself also lacks matched ablations. The proposed interface has no reported gaze-task study, false-activation rate, selection accuracy or measured communication throughput, so corpus-frequency-based trigger scores do not establish safe or faster operation. The 180 ms CPU figure is similarly incomplete: the BiGRU requires the full input sequence, the discussion proposes future 500-1000 ms windows, and phoneme-to-word conversion depends on Claude Sonnet 4.5, which the authors plan to replace to enable fully offline operation. Model size, sequence lengths and preprocessing contain internal inconsistencies that further complicate reproduction. The useful contribution is a decoder-and-interface hypothesis with author-reported accuracy gains, rather than a demonstrated complete real-time communication system or a validated solution to unintended gaze selections.

### Why it matters

Connects neural phoneme decoding with a concrete interaction design question, while providing a staged decoder comparison that can be reproduced under cleaner evaluation boundaries.

### Prior state of the art

Neural speech decoders already combine sequence models and language-model constraints. Conformer, CTC, n-grams and WFSTs originate in existing sequence-recognition methods; gaze dwell-time is the interaction comparator proposed here.

### What changed

Adapts a Conformer to intracortical feature sequences and adds validation-confusion-informed phoneme correction and beam search; proposes phoneme onset/offset as a gaze gesture confirmation signal.

### Position in the field

Invasive attempted-speech brain-to-text decoding with a proposed multimodal selection interface; distinct from non-invasive articulatory SSI.

### Practical value

A candidate Conformer/LM baseline and a testable gaze-confirmation design; current evidence is insufficient to recommend its claimed complete system for clinical use.

### Advanced

Reported within-participant phoneme error reduction across decoder stages and a proposed combination of gaze pointing with phoneme confirmation.

### Unresolved

Independent final evaluation after validation-informed tuning, actual end-to-end latency, gaze interaction benefits, architecture contribution, and user/session transfer.

### Narrowed or regressed

Reported decoder latency rises from 45 ms for greedy decoding to 180 ms for WFST; dependence on full-sequence context and an external language model limits the claimed complete offline interface.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | text-entry |
| Input | Intracortical neural threshold crossings and spike-band power; gaze is a proposed additional interaction input. |
| Sensor | T15 uses four implanted 64-electrode microelectrode arrays, supplying 512 features from 256 intracortical sites. The paper calls this ECoG/iEEG, which should not be confused with a surface ECoG array or scalp EEG. Primary acquisition context: https://github.com/Neuroprosthetics-Lab/nejm-brain-to-text . |
| Body site | brain |
| Output | text |
| Vocabulary type | Sentence-level phoneme-to-text decoding; word-disjoint evaluation unclear |
| Vocabulary size | 42 output classes including CTC blank; this is a phoneme inventory, not a 42-word vocabulary. Exact evaluated word vocabulary is not reported. |
| Metrics and results | Table IV: greedy PER 10.62% / 45 ms; 6-gram rescoring PER 9.98% / 65 ms; WFST PER 7.86% / 180 ms. Reported word error is 26.61%. WFST gives a 2.76 percentage-point PER reduction from greedy. Reported error components are 5.2% substitutions, 1.8% deletions and 0.86% insertions. These are author-reported, not independently reproduced; latency hardware/boundaries and untouched evaluation are unclear. |
| Evaluation protocol | Retrospective single-participant phoneme/word decoding, decoder-stage comparisons and validation confusion matrices; proposed trigger ranking uses corpus frequency and validation precision/recall. |

### Limits

- **Technical:** BiGRU and unmasked sequence context are noncausal. Table II reports both 192.9M total parameters and approximately 25M for ConformerXL. Described trial lengths vary from typical 150 frames to 700-1400 frames. The preprocessing claim that 50/60 Hz lies outside a 0.3-300 Hz passband is internally incorrect; raw filtering and already-binned spike features need reconciliation.
- **Evaluation:** Validation confusion patterns explicitly inform language-model correction; 150 Optuna decoder configurations are explored without a separately reported untouched final evaluation. Hidden test labels are unavailable. Prior-work comparisons lack matched reruns, while architecture, UI and late-session effects lack controlled ablations.
- **Deployment:** Single implanted participant, retrospective decoding, full-sequence BiGRU and Claude Sonnet 4.5 phoneme-to-word conversion. CPU model and timing boundaries are unspecified; no integrated online gaze study or autonomous clinical communication trial is reported.
- **Scope of this review:** One participant and a retrospectively analyzed subset. The paper calls the task overt speech; the underlying T15 resource includes attempted vocalized and some attempted silent speech, without a separately reported mode-specific result here. No new clinical user trial.

### Evidence

- The study analyzes one T15 participant across 45 sessions, reporting 7,050 training and 1,021 validation trials. Test ground truth is unavailable, and the reported split percentages and total need reconciliation. (Section III; PDF pp. 2-3)
- ConformerXL combines a dilated-convolution/BiGRU prenet, 8x temporal subsampling and 12 modified Conformer blocks, followed by phoneme language modeling and WFST search. (Sections V-VII; Table II; PDF pp. 4-9)
- A confusion matrix derived from systematic errors on the validation set informs language-model correction weights. Decoder configurations are explored over 150 Optuna trials. Reviewer assessment: independent final evaluation after these choices is not established. (Sections VI-VII; Table V; PDF pp. 7-8 and 11)
- Table IV reports greedy/LM/WFST PER of 10.62%/9.98%/7.86% and respective latencies of 45/65/180 ms; the WFST reduction from greedy is 2.76 percentage points. (Table IV; Section IX; PDF p. 11)
- Reported WER is 26.61%; phoneme-error components are 5.2% substitutions, 1.8% deletions and 0.86% insertions. These do not establish exact-sentence accuracy or human communication performance. (Section IX; PDF p. 11)
- The authors acknowledge that the backward GRU needs the full sequence and propose future 500-1000 ms overlapping windows for deployment. Reviewer assessment: the 180 ms figure is not demonstrated causal acquisition-to-output latency. (Section X; PDF p. 12)
- Phonemes are converted to words using Claude Sonnet 4.5; replacing this dependency to enable fully offline operation is future work. The timing boundary for that stage is not specified. (Section V and Figure 5; Sections XI; PDF pp. 4-5 and 12-13)
- Gaze-plus-phoneme swipes and text dragging are proposed; trigger ranking combines validation precision/recall with corpus frequency. No integrated user study of selection errors, false activations or throughput is reported. (Section VIII; Figures 14-17; PDF pp. 9-11)
- Table II gives 192.9M total parameters but also approximately 25M for ConformerXL. Sequence-length descriptions also differ between typical 150-frame trials and 700-1400-frame architecture examples. (Table II; Sections III and V; PDF pp. 3-5)
- Section IV claims a 0.3-300 Hz bandpass removes 50/60 Hz interference because it is outside the passband. Reviewer assessment: those frequencies are inside the stated interval, and preprocessing details need correction. (Section IV; PDF p. 3)
- The discussion reports roughly 80.8% validation accuracy for 2025 sessions and acknowledges single-participant generalization limits; vocabulary shift and neural change are not isolated in controlled tests. (Section X; PDF p. 12)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
