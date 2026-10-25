# Relating the Neural Representations of Vocalized, Mimed, and Imagined Speech

Maryam Maghsoudi, Rupesh Chillale, Shihab A. Shamma  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2602.22597)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text+summary

Cross-mode analysis of speech reconstruction from sEEG in vocalized, mimed and imagined speech in one participant, showing envelope correlation needs sentence-discrimination checks.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Existing intracranial sEEG, 110 contacts |
| Task | Speech reconstruction across speech modes |
| Vocabulary | 100 prompted sentences |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Rank area above chance 0.59 (nonlinear, vocalized within-mode); cross-mode at most 0.14 |

**Limitations.** Single participant; split, alignment and model-selection details incomplete; linear and nonlinear models use different targets and nulls; no online or intelligibility evaluation.

## Full review

### In short

A useful one-participant cross-mode analysis showing why envelope correlation needs sentence-discrimination checks; incomplete split/alignment reporting and mixed model results limit the stronger conclusions.

### Review

The useful idea in this short study is to ask whether a reconstructed speech envelope identifies the intended sentence, rather than accepting a high correlation as sufficient evidence of useful decoding. Applying condition-specific decoders across vocalized, mimed and imagined speech exposes both common structure and important failures: the linear mimed-to-imagined mapping has rank area -0.01 despite the general above-null correlation claim. The proposed planning-plus-articulation-plus-feedback explanation is a plausible hypothesis, but its components are assumed rather than independently measured, and the authors appropriately leave direct subspace tests and a listening condition for future work. Reproducibility also limits interpretation. Only one participant is analyzed, split sizes and grouping of repeated sentences are not given, silent neural activity is compared with vocalized acoustic targets, and exact time-lag and alignment choices are unclear. Linear and nonlinear models use different spectrogram representations and null perturbations, so their differences cannot be attributed solely to linearity. The broad claim of better sentence preservation by the linear model requires qualification: Figure 3 reports nonlinear versus linear vocalized-to-vocalized rank areas of 0.59 versus 0.32, while several other pairs favor the linear model. A steeper correlation-versus-rank relationship is not an overall superiority test. This is an interesting representation-analysis pilot and a useful warning against relying on envelope correlation alone, rather than a demonstrated general imagined-speech decoder.

### Why it matters

Shows that cross-mode acoustic similarity and sentence-specific information can diverge, making evaluation choice central to representation claims.

### Prior state of the art

Prior work decodes each speaking mode or compares activation patterns. Ridge decoding and convolutional/recurrent spectrogram models are established approaches; high acoustic correlation alone does not establish linguistic identity preservation.

### What changed

Uses condition-specific linear mappings as probes of cross-mode transfer and supplements correlation with top-k envelope-matching analysis, alongside a nonlinear baseline.

### Position in the field

Single-participant invasive speech-mode transfer study, focused on neural/acoustic representation relationships rather than operational text entry.

### Practical value

A compact linear baseline and an evaluation lesson for cross-mode neural decoding; insufficient evidence for a deployable speech restoration system.

### Advanced

Separates envelope reconstruction similarity from sentence-level discriminability and evaluates all nine train/test mode combinations.

### Unresolved

Sentence-disjoint split integrity, repeated-trial grouping, target alignment in silent modes, rank-area scaling, statistical independence, cross-user transfer and direct tests of the proposed neural decomposition.

### Narrowed or regressed

Some transfers preserve envelope correlation without positive sentence-discrimination area; linear mimed-to-imagined rank area is -0.01. Nonlinear versus linear superiority varies by train/test pair.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | Intracranial stereotactic EEG during vocalized, mimed and imagined speech. |
| Sensor | 110 retained sEEG contacts in the analyzed release. Primary VocalMind describes nine right-hemisphere depth shafts and 140 initial contacts, recorded at 1 kHz, with 30 abnormal contacts removed; these details describe the source dataset, not new acquisition. Source: https://www.nature.com/articles/s41597-025-04741-2 . |
| Body site | brain |
| Output | spectrograms and sentence-ranking analysis |
| Vocabulary type | fixed prompted sentence set; acoustic reconstruction rather than unrestricted text output |
| Vocabulary size | 100 prompted sentences, repeated twice per mode; lexical vocabulary size not reported. |
| Metrics and results | Figure 3 rank area above chance, rows training V/M/I and columns testing V/M/I: linear [0.32,0.05,0.07; 0.11,0.13,-0.01; 0.11,0.08,0.07]; nonlinear [0.59,0.07,0.01; 0.14,0.06,0.04; 0.10,0.04,0.07]. This is top-k rank-curve area, not ROC AUC, classification accuracy or WER. Exact normalization is unclear. Reconstruction correlations are reported above their nulls (all p much less than 0.001); no numerical correlation table or listener result is supplied. |
| Evaluation protocol | Offline within- and cross-mode reconstruction correlations, shuffled/shifted null comparisons, sentence-envelope top-k matching and area above the chance rank curve. |

### Limits

- **Technical:** The linear target is an NSL auditory representation whereas the nonlinear target is mel-spectrograms. Linear nulls shuffle trial pairings and nonlinear nulls circularly shift targets. The planning/articulation/feedback decomposition is assumed, and no direct subspace or sensory-feedback experiment is performed.
- **Evaluation:** Train/test proportions, lag support, regularization grid and model selection boundaries are insufficiently reported. Sentence repetitions may require grouping across modes; this is not explicitly documented. Linear and nonlinear models use different target representations and different null constructions. Pairwise condition summaries are not independent participants.
- **Deployment:** Retrospective, externally cued single-participant analysis with acoustic targets from vocalized speech; no online communication, listener intelligibility, word-error or latency evaluation.
- **Scope of this review:** The analyzed dataset is one Mandarin-speaking participant with repeated prompted sentences. Primary VocalMind acquisition was an epilepsy-monitoring participant with intact language, not a clinical speech-restoration trial.

### Evidence

- The study uses one VocalMind participant, 100 Mandarin sentences repeated twice in each of three modes and signals from 110 electrodes, with vocalized audio as stimulus targets. (Section 2.1; PDF p. 2)
- Condition-specific time-lagged ridge mappings are evaluated across all three modes, and sentence-envelope top-k ranking supplements reconstruction correlation. (Sections 2.2 and 2.4; PDF p. 2)
- Training/test division and a regularization grid search are mentioned without exact split sizes, lag values, repetition grouping or complete alignment procedure. Reviewer assessment: independence and reproducibility cannot be established from this description. (Sections 2.1-2.4; PDF p. 2)
- Figure 3 reports linear rank areas [0.32,0.05,0.07; 0.11,0.13,-0.01; 0.11,0.08,0.07] for V/M/I training and V/M/I testing. Mimed-to-imagined area is -0.01 despite the general above-null correlation result. (Sections 3.1/3.3; Figure 3; PDF pp. 2-4)
- Figure 3 reports nonlinear vocalized-to-vocalized area 0.59 versus linear 0.32; mimed-to-mimed is 0.06 versus linear 0.13. Reviewer assessment: model ordering depends on condition and does not support universal linear superiority. (Figure 3; Sections 3.3-3.4; PDF pp. 3-4)
- The linear decoder uses NSL time-frequency targets and trial-shuffled nulls, whereas the nonlinear decoder uses mel-spectrogram targets and circularly shifted nulls. Reviewer assessment: the comparison changes more than model linearity. (Sections 2.1-2.3 and 3.4; PDF pp. 2 and 4)
- Equation 3 defines a sum of top-k performance minus k/N, while Figure 3 reports rank-area values without sufficient normalization and candidate-count detail. Reviewer assessment: this quantity must not be interpreted as ROC AUC or recognition accuracy. (Section 2.4 Equation 3; Figure 3; PDF pp. 2 and 4)
- The planning, articulation and sensory decomposition in Equation 4 is assumed. Direct subspace alignment tests and a listening condition are explicitly proposed as future work. (Sections 3.2 and 4; PDF pp. 3-4)
- Figure 4 compares relationships across nine condition pairs and reports a Steiger-test p value for differing correlation/rank relationships. Reviewer assessment: this is not a controlled overall decoder-superiority or cross-participant test. (Figure 4; Section 3.4; PDF p. 4)
- The paper reports offline reconstructions and rank/correlation analyses, with no WER, listener intelligibility, online latency or prospective communication test. (Sections 2-5; PDF pp. 2-4)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
