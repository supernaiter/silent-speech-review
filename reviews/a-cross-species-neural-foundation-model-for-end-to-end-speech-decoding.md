# A cross-species neural foundation model for end-to-end speech decoding

Yizi Zhang, Linyang He, Chaofei Fan, Tingkai Liu, Han Yu, Trung Le, Jingyuan Li, Scott Linderman, Lea Duncker, Francis R Willett, Nima Mesgarani, Liam Paninski  
arXiv 2025 · [arXiv](https://arxiv.org/abs/2511.21740)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text+summary

Introduces a cross-species self-supervised transformer encoder for Utah-array spiking data combined with audio-LLM end-to-end decoding, reporting state-of-the-art Brain-to-Text benchmark accuracy and imagined speech decoding.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Intracortical Utah microelectrode arrays (spikes, SBP) |
| Task | Neural speech-to-text decoding |
| Vocabulary | Up to 125,000 words (attempted); 50 words (imagined) |
| Speaker | Not stated |
| Session | Not stated |
| Online / offline | Offline |
| Key result | WER values not given in review; ~0.95 s end-to-end latency per sentence |

**Limitations.** Only two human participants; bidirectional attention and large LLMs hinder real-time, on-device use, and imagined vocabulary is limited.

## Full review

### In short

Introduces a cross-species pretrained transformer encoder enabling state-of-the-art end-to-end neural speech decoding with audio-LLMs, improving accuracy and enabling imagined speech decoding, but latency and real-time deployment remain challenges.

### Review

This paper presents a significant step forward in speech brain-computer interfaces by integrating a transformer-based neural encoder pretrained via self-supervised learning on extensive human and monkey neural datasets with an audio-LLM decoder for end-to-end neural-to-text speech decoding. The approach achieves state-of-the-art word error rates on challenging Brain-to-Text ’24 and ’25 benchmarks, substantially improving upon prior RNN-based cascaded and end-to-end models. Importantly, the model successfully decodes both attempted and imagined speech, exhibiting cross-task representational alignment. However, practical deployment is currently limited by slower inference speeds for the end-to-end approach and bidirectional attention's unsuitability for real-time decoding. Further improvements in LLM decoder design, modality alignment, and handling neural signal variability and plasticity are required for long-term, real-world application. Overall, the approach offers a promising foundation for future scalable, integrated neuroprosthetic speech decoding systems.

### Why it matters

Establishes transformer-based cross-species self-supervised pretraining combined with audio-LLM end-to-end decoding as a new paradigm for speech BCIs achieving top decoding accuracy and cross-task generalization, though practical real-time use and robustness require further work.

### Prior state of the art

Prior speech BCIs relied on cascaded RNN encoders decoding phonemes combined with n-gram language models. Limited or no large scale pretraining, transformers not widely used, end-to-end speech decoding with LLMs was emerging but still relied on RNNs and lacked large-scale neural data integration.

### What changed

Introduces a pretrained transformer-based neural encoder trained cross-species and cross-task with self-supervised masked modeling, integrated end-to-end with large audio-LMs via contrastive alignment to decode neural activity directly to text, improving accuracy and enabling imagined speech decoding and cross-task generalization.

### Position in the field

Advances state-of-the-art in intracortical speech BCIs by enabling end-to-end transformer and LLM-based decoding with pretrained neural encoders and cross-modal alignment, moving beyond cascaded and RNN-based methods.

### Practical value

High potential for improving speech neuroprosthetics accuracy and enabling imagined speech decoding, but current latency and generalization limitations constrain immediate real-world deployment.

### Advanced

Input modality moved from RNN-based phoneme decoding to transformer-based encoder with cross-species self-supervised pretraining; output shifted from phoneme-level to direct neural-to-text end-to-end decoding; problem framing moved from cascaded systems to joint end-to-end differentiable optimization integrating neural and language model modalities.

### Unresolved

Remaining generalization to unseen subjects is unclear; full real-time suitability and robust long-term deployment with larger LLMs remain open; addressing neural plasticity and co-adaptation is future work.

### Narrowed or regressed

Decoding latency for end-to-end method is slower (approx. 0.95s per sentence) than cascaded (0.24s); bidirectional attention in encoder limits online real-time decoding currently.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-recognition |
| Input | electrophysiological neural spiking activity (Utah arrays) |
| Sensor | Utah microelectrode arrays with thresholded spikes and spike-band power (SBP) features |
| Body site | brain |
| Output | text |
| Vocabulary type | natural language English text |
| Vocabulary size | Up to 125,000 words in attempted speech dataset; 50 words for imagined speech dataset |
| Metrics and results | Word Error Rate (WER) on Brain-to-Text ’24 and ’25 benchmarks; Phoneme Error Rate (PER) in phoneme decoding; Representational Similarity Analysis scores; processing latency per sentence (approx. 0.95s end-to-end, 0.24s cascaded) |
| Evaluation protocol | Quantitative performance evaluation on held-out datasets (word error rate), ablation studies, representational similarity analysis, and decoding error analyses. |

### Limits

- **Technical:** End-to-end latency and computational requirements; bidirectional attention inhibits online decoding; large pretrained LLMs require substantial resources; need for large labeled and unlabeled datasets; limited real-time applicability currently.
- **Evaluation:** Evaluations focused on two human participants (T12, T15) and limited imagined speech vocabulary; unknown performance on larger, more diverse subject sets; small batch sizes for contrastive learning may limit modality alignment effectiveness; inference strategies like nucleus sampling could be further optimized.
- **Deployment:** End-to-end model latency (~0.95s per sentence) and requirement for bidirectional attention constrain real-time deployment; larger LLMs unsuitable for on-device use; dependency on large unlabeled and labeled datasets for pretraining and fine-tuning.
- **Scope of this review:** Limited to Utah array intracortical neural recordings, tested only on two human participants and associated monkey data; generalization to other populations or hardware untested.

### Evidence

- We introduce an end-to-end BraIn-to-Text (BIT) framework that translates neural activity into coherent sentences using a single differentiable neural network with a cross-task, cross-species pretrained neural encoder, supporting both attempted and imagined speech decoding. (Abstract, Introduction, Methods, Experiments, Discussion)
- BIT Cascaded achieves state-of-the-art WER of 6.35% on Brain-to-Text ’24 hold-out, outperforming previous best 7.98%, and BIT End-to-End reduces prior end-to-end WER from 24.69% to 10.22%. (Evaluation)
- The neural encoder is a transformer pretrained with self-supervised masked modeling on 367 hours of human and monkey Utah array neural data across speech and motor tasks. (Methods)
- Speech decoding was conducted on Brain-to-Text Benchmark ’24 and ’25 intracortical Utah array datasets with two human participants (T12 and T15) for attempted speech and a smaller imagined speech dataset involving the same individuals. (Methods, Evaluation)
- Phoneme decoding uses a 41-token vocabulary including phonemes plus blank and silence tokens, with phoneme error rates (PER) correlated with word error rates (WER) after decoding. (Appendix)
- End-to-end decoding requires about 0.95 seconds per sentence on average, slower than cascaded decoding at 0.24 seconds, limiting real-time applicability; bidirectional attention in the neural encoder is unsuitable for online decoding. (Discussion)
- LLMs of larger scale than 1.5B parameters used here cannot run on-device, limiting mobile real-time applications. (Discussion)
- This work combines cross-species, cross-task transformer-based self-supervised pretraining with an audio-LLM end-to-end decoder for neural speech decoding, a novel integration beyond prior cascaded, RNN-based, or purely task-specific models. (Full text)
- Evaluations were conducted on two particular human participants (T12 and T15) for attempted speech with large vocabularies and on imagined speech with a reduced 50-word vocabulary, limiting generalization scope. (Evaluation)
- Contrastive learning is employed to align neural and text embeddings in a shared latent space to improve cross-modal alignment and decoding performance. (Methods)
- This model was pretrained on thresholded spikes and spike-band power (SBP) features from Utah array intracortical recordings. (Methods)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
