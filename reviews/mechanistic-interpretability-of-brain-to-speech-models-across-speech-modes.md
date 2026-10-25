# Mechanistic Interpretability of Brain-to-Speech Models Across Speech Modes

Maryam Maghsoudi, Ayushi Mishra  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2602.01247)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text+summary

Applies activation interventions to a stereotactic EEG brain-to-speech decoder across vocalized, mimed and imagined speech; baseline PCC is 0.75/0.73/0.57, but internal inconsistencies leave strong causal conclusions unestablished.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Stereotactic intracranial EEG (VOCALMind) |
| Task | Interpretability of speech reconstruction from sEEG |
| Vocabulary | Paired sentences; lexical size not reported |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Baseline PCC 0.7519 vocalized, 0.7254 imagined, 0.5686 mimed (author-reported, unresolved) |

**Limitations.** One participant and one architecture; donor replacement bypasses recipient information, scores and winner counts are internally inconsistent, and no deployable imagined-only transfer is shown.

## Full review

### In short

Offers useful activation-intervention diagnostics, but donor replacement bypasses recipient information, baseline/patch scores are unresolved, and winner counts exceed the stated layer width; strong causal conclusions are not established.

### Review

The useful idea is to ask which internal activations affect a brain-to-speech decoder, rather than treating prediction accuracy as an explanation. Channel/time interventions and matched random scrubbing controls are appropriate starting points. The strongest claims nevertheless exceed what the reported setup establishes. In Equation 1, replacing an entire activation tensor in the serial network causes the remaining network to operate on the donor representation; keeping the imagined input nominally fixed does not preserve its information downstream. High donor-conditioned performance therefore cannot rule out inferior imagined-signal quality or demonstrate successful imagined-only decoding. The numerical reporting also needs repair: the full vocalized patch reaches PCC 0.954, while the listed vocalized baseline is 0.752, even though the method describes the same fixed model; separate checkpoint language elsewhere makes the actual comparison unclear. More directly, a convolutional layer described as 64 channels is assigned 96 to 120 distinct winning neurons in Table 5. That cannot be reconciled with the stated channel-level definition without an unreported aggregation or different architecture. Claims of universally smooth monotonic interpolation are also inconsistent with nonmonotonic spectral-distortion curves, and interpolation through a continuous decoder is not sufficient evidence of a shared biological causal manifold. The KEEP-versus-random results suggest localized relative influence in some directions, but do not recover full donor performance and are not independently selected on held-out data. This paper is best treated as an exploratory interpretability proposal whose raw results, intervention semantics and counting conventions must be clarified before its mechanistic conclusions are used.

### Why it matters

A candidate toolkit for auditing how a decoder responds to cross-mode activation changes, with useful matched-control and multi-scale intervention ideas.

### Prior state of the art

Intervening on a neural network can identify dependencies in that network, but substituting donor activations is distinct from extracting more information from recipient brain signals. Smooth responses to interpolated activations do not by themselves establish a shared biological manifold.

### What changed

Studies where donor-mode activations influence a convolutional/bidirectional recurrent speech decoder through full replacement, temporal/channel subsets and neuron-level ranking.

### Position in the field

Offline interpretability analysis of an intracranial neural speech decoder, not a validated assistive communication system.

### Practical value

Potentially useful for debugging trained decoders after raw results and interventions are made reproducible; unsuitable as current evidence of reliable imagined-speech transfer.

### Advanced

Provides directional activation interventions, channel/time localization, matched random controls and sentence-level neuron diagnostics beyond ordinary predictive scores.

### Unresolved

Single shared decoder versus separate mode checkpoints, consistency of baseline/full-patch evaluation, impossible winner counts under the reported layer width, independent subspace selection, signal-quality confounds and biological interpretation.

### Narrowed or regressed

No demonstrated improvement to an imagined-only deployable decoder. Restricted scrubbing retains only part of full donor-conditioned performance, and quantitative contradictions prevent accepting strong sufficiency or shared-manifold conclusions.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | Invasive stereotactic EEG for vocalized, mimed and imagined speech; interventions additionally use paired donor-mode hidden activations. |
| Sensor | Existing stereotactic intracranial EEG electrodes in VOCALMind; acquisition channel counts and preprocessing are not detailed in this paper. |
| Body site | brain |
| Output | speech-audio |
| Vocabulary type | paired sentence-level speech-mode tasks |
| Vocabulary size | Exact unique lexical size unreported; 200 sentence samples per condition in winner analysis. |
| Metrics and results | Table 2 baseline PCC concat: vocalized 0.7519, imagined 0.7254, mimed 0.5686; MCD 2.7928/2.8830/3.2948. Table 3 full vocalized-to-imagined/mimed patch PCC 0.954 and MCD 1.63; imagined-to-vocalized PCC 0.177. Table 1 imagined-from-vocalized KEEP-Conv/RAND-Conv PCC 0.666/0.564 and KEEP-RNN/RAND-RNN 0.462/0.398. Table 5 reports 96-120 distinct convolutional winners despite a 64-channel architecture. Author-reported values, internally unresolved and not independently reproduced. |
| Evaluation protocol | Offline intervention analysis of a neural speech decoder, using flattened mel-spectrogram PCC, spectral distortion, baseline pitch measures, donor activation replacement, interpolation and matched random scrubbing controls. |

### Limits

- **Technical:** Whole-layer replacement removes the recipient path at that site. Smooth interpolation is expected from continuous computation and does not identify an intrinsic manifold. Neuron selection uses mean effects across the analyzed dataset. Convolutional winner counts and mode-specific model references conflict with the architectural description; model neurons are not biological neurons.
- **Evaluation:** One participant and one architecture; training details, fold counts, target alignment and held-out subspace selection are absent. Figure 5 uses a k=1 reference whereas the method describes an unpatched baseline. Full-patch scores are inconsistent with donor baselines under a shared serial model. Table 5 convolutional winner counts exceed the described 64 channels.
- **Deployment:** Diagnostic interventions require paired donor-mode brain recordings or activations for the same content. No deployable imagined-only transfer method, new-user test, intelligibility assessment or real-time demonstration.
- **Scope of this review:** One participant, one described model, paired speech-mode sentences and activation diagnostics. No biological intervention, intelligibility, open communication or clinical outcome.

### Evidence

- The study combines full activation patching, convex interpolation, channel/time localization, matched random scrubbing and neuron ranking in a speech decoder. (Sections 5-6; PDF pp. 3-8)
- VOCALMind data come from one participant, and Table 5 reports 200 sentence samples per mode-pair condition; no cross-person experiment is described. (Section 4.1 and Table 5; PDF pp. 3 and 14)
- Equation 1 computes the patched output as the post-layer network applied to donor activation. Reviewer assessment: in the stated serial architecture, complete replacement bypasses the recipient representation rather than improving information extraction from it. (Section 5, Equation 1; PDF p. 3)
- Table 3 lists vocalized baseline PCC 0.752 but full vocalized donor patch PCC 0.954. Methods describe a fixed model, while Appendix E refers to activations from a vocalized model. Reviewer assessment: checkpoint and evaluation semantics need reconciliation. (Sections 5.4 and Appendix B.1/E; Table 3; PDF pp. 6, 11-13)
- The convolutional output is described as 64 channels, but Table 5 lists 96-120 unique convolutional winner neurons. Reviewer assessment: these counts exceed the stated channel universe unless an unreported aggregation or different architecture is used. (Sections 4.2/5.2 and Table 5; PDF pp. 3-4 and 14, rendered table inspected)
- Table 1 imagined-from-vocalized KEEP-Conv/RAND-Conv PCC is 0.666/0.564, while KEEP-RNN/RAND-RNN is 0.462/0.398; full patch is 0.954. Reviewer assessment: localized control benefits are not full performance recovery. (Table 1; PDF p. 7)
- Figure 7 includes nonmonotonic recurrent MCD curves despite broad prose claims of monotonic interpolation. Reviewer assessment: smooth interpolation through a continuous decoder does not by itself establish a shared biological causal manifold. (Section 6.1, Appendix C and Figure 7; PDF pp. 7, 12-13, figure rendered)
- Top-k neurons are ranked by mean single-neuron effects across the analyzed dataset; a separate held-out selection/evaluation procedure is not specified. (Sections 5.5-5.6; PDF p. 6)
- Figure 5 labels delta PCC relative to k=1, whereas methods describe changes relative to an unpatched baseline. Reviewer assessment: reference conditions must be specified consistently before interpreting improvements. (Sections 5.4-6 and Figure 5; PDF pp. 6-8)
- Table 2 baseline PCC is 0.7519 for vocalized, 0.7254 for imagined and 0.5686 for mimed. Reviewer assessment: these baselines do not place mimed speech between the other two modes in decoding performance. (Table 2 and Discussion; PDF pp. 8 and 11)
- Evaluation centers on spectrogram correlation/distortion and intervention diagnostics; no word-recognition or listening-comprehension outcome, new participant or live communication test is reported. (Section 6 and Appendices A-F; PDF pp. 6-14)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
