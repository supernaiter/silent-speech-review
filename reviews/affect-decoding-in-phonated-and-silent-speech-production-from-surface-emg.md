# Affect Decoding in Phonated and Silent Speech Production from Surface EMG

Simon Pistrosch, Kleanthis Avramidis, Zhao Ren, Tiantian Feng, Jihwan Lee, Monica Gonzalez-Machorro, Anton Batliner, Tanja Schultz, Shrikanth Narayanan, Björn W. Schuller  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2603.11715)

**Section:** [Surface EMG](../README.md#surface-emg) · **Review basis:** full_text+summary

Binary affect (polite vs frustrated) classification from facial/neck sEMG in phonated and silent speech; silent-only within-subject AUC 0.829, but transfer to unseen speakers is weak.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 8-channel bipolar facial/neck surface EMG (gel) |
| Task | Affect classification |
| Vocabulary | Binary affect labels (polite/frustrated) |
| Speaker | Both |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Silent-only within-subject AUC 0.829; held-out-speaker EMG AUC 0.567-0.574 |

**Limitations.** Small imbalanced cohort; facial expression and speech motor activity not separated; fixed task order; no independent-day, mobile or patient testing.

## Full review

### In short

Useful evidence that prompted silent articulation carries affect cues, with silent-only AUC 0.829 within a person; weak unseen-speaker transfer and inseparable facial-expression effects limit deployment claims.

### Review

This paper makes a useful contribution to silent paralinguistics by asking what emotional information remains in facial and neck EMG when speech is articulated without phonation. Its strongest evidence is a paired-mode dataset and a reasonably careful set of sentence-grouped, held-out-speaker and repeated-content comparisons. The headline AUC of 0.845 is a within-person result for prompted binary affect classification, not word recognition or unseen-user performance. For silent-only within-person decoding, structural EMG features reach AUC 0.829; phonated-to-silent transfer reaches 0.763 with BioCodec. In contrast, the pooled prompted EMG results fall to AUC 0.567-0.574 for held-out speakers, making personalization a central limitation. The repeated-content analysis is particularly valuable: EMG retains moderate discrimination when the same sentences express both labels, whereas lexical cues appear to help the speech foundation model substantially on affect-specific sentences. This does not isolate speech articulation itself, however. The strongest within-person channel is the eyebrow-region electrode, and the authors explicitly acknowledge that concurrent facial expressions cannot be disentangled from articulatory modulation. Fixed condition order and immediate phonated-then-silent repetition introduce further alternatives. The spontaneous experiment is phonated only, and its training description conflicts between methods and results, so it should not be presented as demonstrated transfer to natural silent conversation. Overall, this is a worthwhile dataset-and-evaluation study with informative negative generalization results, but it does not yet establish a deployable affect-aware communication interface.

### Why it matters

Shows where silent affect decoding works and fails, with paired articulation modes and lexical-control analyses that expose the gap between personalization and generalization.

### Prior state of the art

Facial EMG emotion recognition and EMG speech decoding already exist, but often address passive emotion elicitation or lexical reconstruction separately. This study examines their intersection during speech production.

### What changed

Combines paired-mode speech production with affect classification and explicit sentence/speaker controls, rather than reconstructing words or audio.

### Position in the field

Silent paralinguistics: affect-label inference from articulatory and facial signals, complementary to lexical silent speech recognition.

### Practical value

Offers baseline designs and evidence for personalized affect sensing; the held-out-speaker and repeated-content results are more useful for system planning than the headline score alone.

### Advanced

Adds affect labels and channel-level analyses to silent articulation; tests sentence-grouped evaluation, held-out speakers, repeated lexical content and cross-mode transfer.

### Unresolved

Natural silent conversation, independent recording days, patient populations, separation of articulation from facial expression, real-time operation and the exact spontaneous-training protocol.

### Narrowed or regressed

EMG discriminability drops sharply for unseen speakers; prompted repeated-content trials are harder than affect-specific sentences. Speech foundation-model features outperform EMG in spontaneous phonated conversation.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | affect-classification |
| Input | Eight-channel facial and neck surface EMG; separately evaluated audio baselines for phonated speech. |
| Sensor | actiCHamp Plus amplifier with eight bipolar Ag/AgCl surface electrodes at infrahyoid, suprahyoid, mylohyoid, mentalis, upper orbicularis oris, depressor supercilii and bilateral zygomaticus major sites; 10 kHz acquisition downsampled to 1 kHz. Gel and skin preparation; separate Rode NT1-A/Focusrite audio acquisition. |
| Body site | face;throat |
| Output | labels |
| Vocabulary type | Affect classes rather than lexical output |
| Vocabulary size | Not a word-vocabulary task: binary polite/frustrated labels, with neutral trials excluded from the primary reported classification. |
| Metrics and results | Table 5 prompted pooled EMG: TD-0 within-subject AUC 0.845 +/- 0.058 and BAC 0.762 +/- 0.063; EMG held-out-speaker AUC 0.567-0.574. Table 8 silent-only within-subject structural AUC 0.829 +/- 0.056; phonated-to-silent BioCodec AUC 0.763 +/- 0.094. Table 9 spontaneous phonated held-out-speaker BioCodec AUC 0.630 +/- 0.009, BAC 0.595 +/- 0.014, versus Vox-Profile AUC 0.743 +/- 0.004. Table 9 dispersion is described at trial level and should not be equated with subject-wise SD in Tables 5/8. Results are author-reported, not independently reproduced. |
| Evaluation protocol | Offline binary polite-versus-frustrated classification with neutral trials excluded; 5-fold sentence-grouped within-subject evaluation and nested leave-one-subject-out evaluation. Additional repeated-content, cross-mode, single-electrode and spontaneous-phonated analyses. |

### Limits

- **Technical:** Whole-utterance summary features and baseline normalization require trial context. Facial expression and speech motor activity are not causally separated. The structural-feature median-frequency equation integrates half the spectral area rather than specifying the frequency splitting that area; implementation is unclear.
- **Evaluation:** Small and demographically imbalanced cohort; affect and mode order are fixed, and silent trials immediately follow phonated counterparts. Sentence grouping reduces direct lexical leakage, but task/order effects remain. Section 5.3 and Section 6.3 disagree on whether training includes spontaneous trials. No independent-day or patient test.
- **Deployment:** Laboratory recordings with eight gel electrodes, roughly one hour of preparation, participant-held recording button and offline whole-trial features. No mobile, continuous or clinical evaluation.
- **Scope of this review:** English prompted/induced polite and frustrated expression in 12 adults without current neurological or psychiatric diagnoses. Neutral data are collected but excluded from the reported binary comparisons. No clinical cohort or spontaneous silent condition.

### Evidence

- ST-CASE contains 2,780 utterances from 12 participants: 1,588 phonated and 1,192 silent. Task 2 is phonated only; all silent recordings come from prompted Tasks 1 and 3. (Sections 3.1-3.4; Tables 2/4; PDF pp. 2-5)
- The study evaluates affect labels rather than lexical reconstruction, comparing handcrafted/TD EMG features and pretrained BioCodec embeddings with separate acoustic baselines. (Sections 2.1 and 4; PDF pp. 2 and 4-5)
- Within-subject evaluation groups all repetitions of a sentence in the same fold. Inter-subject evaluation uses an outer leave-one-subject-out loop and sentence-grouped inner folds. Neutral trials are excluded from the binary affect results. (Sections 5.1 and 6.1; PDF p. 5)
- Table 5 reports within-subject TD-0 AUC 0.845 +/- 0.058 and BAC 0.762 +/- 0.063, while the three EMG representations yield only 0.567-0.574 AUC in held-out-speaker evaluation. (Table 5; PDF p. 6)
- Table 8 reports silent-only within-subject structural AUC 0.829 +/- 0.056 and phonated-to-silent BioCodec AUC 0.763 +/- 0.094. Silent-only held-out-speaker AUC ranges from 0.563 to 0.608. (Table 8; PDF p. 7)
- On repeated lexical content, within-subject EMG AUC is 0.720-0.751, whereas Vox-Profile falls from 0.889 on affect-specific sentences to 0.469 on repeated-content sentences. Reviewer assessment: this is useful lexical-confound control, not proof of articulation-specific affect coding. (Table 6; Section 6.1; PDF p. 6)
- The eyebrow-region E6 channel has high within-subject discriminability; the paper acknowledges that the design cannot disentangle articulatory modulation from accompanying facial expressions. (Table 3; Figures 4/5; Section 7; PDF pp. 5, 7-9)
- Prompted affect conditions occur in a fixed temporal order, and every phonated trial immediately precedes its silent counterpart. Task 3 repeats Task 1 roughly 30 minutes later. Reviewer assessment: order, repetition and within-visit adaptation are not independent-day generalization tests. (Section 3.2; Figure 3 and Section 6.2; PDF pp. 3 and 6-7)
- Section 5.3 says training uses controlled and spontaneous tasks, whereas Section 6.3 describes training on controlled Tasks 1/3 and testing the held-out speaker on spontaneous Task 2. Reviewer assessment: the exact training-domain boundary must be clarified before claiming controlled-to-spontaneous transfer. (Sections 5.3 and 6.3; PDF pp. 5 and 8)
- Table 9 reports spontaneous phonated BioCodec AUC 0.630 and BAC 0.595, compared with Vox-Profile AUC 0.743 and BAC 0.670. These are phonated affect results, not spontaneous silent-speech decoding. (Table 9; Section 6.3; PDF p. 8)
- The protocol requires skin preparation, conductive gel and participant-held button segmentation. The dataset is not publicly released, and no online latency, mobile use or clinical communication evaluation is reported. (Sections 3.1-3.3 and 4.1; PDF pp. 2-4)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
