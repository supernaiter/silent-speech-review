# Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping

Maryam Maghsoudi, Shihab Shamma  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2605.08075)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text+summary

Zero-shot imagined speech decoding by mapping imagined MEG to listened responses and decoding with a listened-trained contrastive model; above-chance word decoding with Recall@1 up to about 9.1%.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 157-channel whole-head MEG |
| Task | Imagined word decoding |
| Vocabulary | 76 content words from poems |
| Speaker | Speaker-independent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | Recall@1 up to ~9.1% (combined embeddings), 76 words, leave-one-subject-out |

**Limitations.** Small 76-word vocabulary from rhythmic stimuli by trained musicians; low SNR; non-portable MEG; not tested on natural continuous imagined speech.

## Full review

### In short

The study convincingly shows zero-shot imagined speech decoding by mapping MEG imagery to listened responses and decoding with a listened-trained contrastive model, marking a promising data-efficient advance despite limited vocabulary and hardware constraints.

### Review

This paper presents an innovative approach to imagined speech decoding by learning to map imagined MEG signals to listened MEG responses and leveraging a contrastive decoder trained only on listened data. The approach addresses longstanding challenges of scarce, noisy imagined speech datasets and timing variability by using rhythmic stimuli and trained musicians. The method generalizes well across unseen subjects and mapping architectures, although absolute decoding performance is substantially below listened speech ceilings due to noise and limited vocabulary size. The findings underscore the largely linear nature of the mapping and highlight data quantity as a key bottleneck, with the added insight that complex models like transformers currently underperform due to data scarcity. While hardware and dataset limitations temper deployment prospects, this zero-shot decoding pipeline provides a clear, scalable direction for practical imagined speech BCIs by exploiting richer listened speech neural representations.

### Why it matters

This is a proof-of-concept demonstration that zero-shot imagined speech decoding is achievable non-invasively by leveraging mappings from imagined to listened MEG and decoders trained only on listened data, highlighting a scalable path forward grounded in leveraging better characterized listened speech signals.

### Prior state of the art

Previous work mainly decoded imagined speech from noisy, limited datasets typically using within-subject training and small vocabularies, struggling with timing variability and low signal-to-noise ratio in imagined MEG or EEG; meanwhile, decoding listened speech had achieved higher accuracy with larger datasets and advanced decoders.

### What changed

Introduces a novel three-stage pipeline that maps imagined MEG to listened MEG, enabling exploitation of reliable listened speech decoding models for zero-shot decoding of imagined speech without imagined training labels, validated on held-out subjects.

### Position in the field

innovative; advances zero-shot imagined speech decoding leveraging listened speech decoders and cross-condition mappings

### Practical value

Currently limited by hardware and dataset size; presents a methodological advance and proof-of-concept rather than a ready BCI system; practical value expected to grow with dataset and model scaling.

### Advanced

The paper advances cross-subject imagined speech decoding by learning cross-condition mappings and demonstrates viability of zero-shot decoding using listened speech data and representations.

### Unresolved

Generalization to larger vocabularies and real-world continuous imagined speech remains unresolved; the effect of mobility or naturalistic conditions was not addressed.

### Narrowed or regressed

The work is limited in vocabulary size (76 words), decoding performance remains substantially below listened speech decoding ceiling, and fine-grained segment discrimination remains challenging.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-recognition |
| Input | magnetic |
| Sensor | 157-channel whole-head MEG system (axial gradiometers) |
| Body site | brain |
| Output | text |
| Vocabulary type | content-words extracted from poems |
| Vocabulary size | 76 |
| Metrics and results | Mean Pearson correlation between predicted and actual listened MEG signals; rank-based decoding metrics including Recall@k for word decoding (e.g., Recall@1 up to ~9.1% for combined embeddings); above-chance p-values reported for mapping and decoding. |
| Evaluation protocol | Quantitative experimental evaluation using cross-subject leave-one-subject-out generalization; analyses incorporate null baseline comparison; evaluation metrics include Pearson correlation and rank-based word decoding. |

### Limits

- **Technical:** Limited vocabulary of 76 words; signal-to-noise ratio in imagined MEG remains low; transformer models underperform due to dataset size; MEG instrumentation limits portability and deployment.
- **Evaluation:** Evaluations are based on 17 subjects with rhythmic stimuli and limited vocabulary size; results may not generalize to more complex real-world imagined speech; transformer models under current dataset size underperform, suggesting data limits.
- **Deployment:** The system requires MEG hardware which is non-portable and expensive, dataset size and training requirements preclude real-time use today, and vocabulary size and noise limit practical deployment; further dataset scaling and hardware development needed.
- **Scope of this review:** Limited to rhythmic stimuli from trained musicians and small vocabulary decoded from MEG; real-world applicability and continuous natural imagined speech decoding remain open challenges.

### Evidence

- The authors claim to contribute (1) a paired imagined-listened MEG dataset with rhythmic continuous stimuli from trained musicians for better alignment, (2) evaluation of six mapping models to transform imagined MEG into listened MEG with generalization to unseen subjects, (3) evidence that predicted listened signals preserve stimulus-specific information, (4) a contrastive decoder trained on listened data with multiple word embedding strategies, and (5) a proof-of-concept full pipeline for zero-shot imagined speech decoding without imagined labels. (Abstract, Introduction)
- The approach is novel in using learned mappings to convert imagined brain responses into listened counterparts to utilize richer, more reliable listened data decoders, which prior works did not apply for zero-shot imagined speech decoding. (Abstract, Introduction)
- The study uses a novel MEG dataset recorded from 17 trained musicians exposed to four rhythmic stimuli (two melodies and two poems) with paired imagined and listened conditions, enabling precise temporal alignment; vocabulary size is 76 unique content words from the poems. (Methods)
- All six mapping architectures achieve prediction correlations significantly above null on training data and generalize significantly above null to unseen subjects, demonstrating the learned mappings are not subject-specific and transfer to new individuals. (Results)
- Metrics include mean per-channel Pearson correlation between predicted and target listened MEG signals, and rank-based decoding performance such as Recall@1 reaching approximately 9.1% for the combined BERT + Wav2Vec2 embeddings on listened speech decoding. (Methods and Results)
- Decoding performance is substantially below the listened speech decoding ceiling, limited vocabulary size (76 words), and fine-grained segment discrimination remains challenging; mapping correlation values are small, introducing noise before decoding. (Results and Discussion)
- The system requires MEG hardware which is non-portable and expensive, dataset size and training requirements preclude real-time use today, and vocabulary size and noise limit practical deployment. (Discussion)
- The paper presents a proof-of-concept full pipeline for zero-shot imagined speech decoding from imagined MEG using a learned mapping to listened MEG and a contrastive decoder trained only on listened data, with no imagined speech labels used during training. (Abstract, Methods, Results, Conclusion)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
