# Brain2Speech-Net: Intelligible, Real-Time Brain-to-Speech Synthesis Without Text Decoding

Shreeram Suresh Chandra, Zexin Cai, Yu Tsao, Simon King, Berrak Sisman  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2609.04455)

**Section:** [Brain signals (EEG, MEG, intracortical)](../README.md#brain-signals-eeg-meg-intracortical) · **Review basis:** full_text+summary

Text-free synthesis of attempted speech from intracortical recordings in one participant with ALS; 47.2% WER on unseen utterances versus 6.8% on a training-set sample, with faster-than-real-time throughput (RTF ~0.5).

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Four implanted intracortical microelectrode arrays |
| Task | Speech synthesis from intracortical signals |
| Vocabulary | Large-vocabulary utterances; size not specified |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 47.2% WER on unseen utterances (cascades 20.6-22.9%); RTF 0.532 |

**Limitations.** Single implanted participant, offline only; closed-set score is from training data; future-dependent inference prevents streaming claims; MOS study showed reference text; synthetic single-speaker voice.

## Full review

### In short

A useful text-free inference path for attempted-speech synthesis, with faster-than-real-time throughput but 47.2% unseen-utterance WER and no demonstrated causal streaming.

### Review

Brain2Speech-Net offers a useful representation-level compromise between cascaded neural-to-text-to-speech and direct acoustic-unit generation. A phoneme-informed neural encoder and differentiable HMM alignment predict latents for a pretrained speech synthesizer, avoiding an explicit decoded text string at inference while still using phoneme and text-derived supervision during training. The important generalization result is the open-set speech WER of 47.2%, not the 6.8% closed-set number: Section V-A draws the closed evaluation from the training set. On the official unseen-utterance split, the method is much better than the tested direct-unit baseline (105.4% WER, which can exceed 100% because of insertions), but less accurate than the 5-gram cascade (22.9%) and LLM-reranked cascade (20.6%). Its open-set RTF of 0.532 is a throughput advantage over those cascades, not evidence of causal streaming or a measured delay to the first audible output. Forward-backward HMM inference uses future observations, and the study does not demonstrate a closed-loop communication trial. The 3.34/5 listening score is also qualified by showing listeners the reference text. Finally, all neural data come from one implanted participant, and synthetic reference speech cannot establish preservation of that person's voice or prosody. The work is a promising attempted-speech synthesis method with an explicit speed-accuracy tradeoff, not a general imagined-speech decoder or a validated everyday communication device.

### Why it matters

Shows how phoneme-informed neural features can support direct speech synthesis with limited intracortical training data, while exposing the accuracy cost of removing text-language-model decoding.

### Prior state of the art

Cascaded neural-to-text-to-speech systems exploit language models for intelligibility, while direct acoustic-unit synthesis is difficult with limited intracortical data; the paper compares both routes.

### What changed

Uses phoneme posterior representations as an uncertainty-preserving bridge to a TTS latent space; text and synthetic targets supervise training, but text decoding is omitted during synthesis inference.

### Position in the field

Invasive attempted-speech BCI synthesis, adjacent to non-invasive articulatory SSI and distinct from imagined speech.

### Practical value

A research baseline for investigating lower-latency synthesis without discrete text decoding; current open-set errors remain substantial.

### Advanced

Neural-to-speech representation alignment, removal of explicit inference-time text decoding, and a measured accuracy-throughput tradeoff.

### Unresolved

Causal streaming, first-audio latency, new-user transfer, spontaneous communication, natural voice identity and prosody, and independent replication.

### Narrowed or regressed

Open-set speech WER is higher than the cascaded baselines; the approach retains invasive recording and single-participant calibration.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | Intracortical neural recordings; not scalp EEG |
| Sensor | Four implanted microelectrode arrays; threshold-crossing and spike-band-power features, with 256 motor-cortex feature channels selected for decoding. |
| Body site | brain |
| Output | speech-audio |
| Vocabulary type | Closed training-utterance sample and open unseen-utterance evaluation |
| Vocabulary size | Large-vocabulary utterances; distinct target vocabulary size not specified. The comparison 5-gram language model has 125,000 words, not a verified system vocabulary count. |
| Metrics and results | Table II: Brain2Speech-Net closed/open speech WER 6.8%/47.2%, PER 10.9%/37.3%, MCD 4.632/5.522 dB, RTF 0.504/0.532. Open WER: 5-gram cascade 22.9%, LLM cascade 20.6%, direct-unit baseline 105.4%. Fig. 3: text-assisted MOS 3.34 ± 0.11 (95% CI), versus 3.85 ± 0.11 and 3.90 ± 0.11 for cascades and 1.57 ± 0.08 for direct units. Results are author-reported, not independently reproduced. |
| Evaluation protocol | Closed training-set sample versus official unseen-utterance test split, objective ASR-derived WER/PER and DTW-aligned MCD, RTF, and a text-assisted listening study. |

### Limits

- **Technical:** Future-dependent HMM posterior inference and sequence-level segment prediction complicate a streaming interpretation. Synthetic acoustic targets and pretrained single-speaker synthesis do not recover natural user acoustics.
- **Evaluation:** Closed-set evaluation samples 880 utterances from the training set and is not an independent test. Open-set evaluation uses the official 880-utterance test split from the same person. References are TTS-generated. The 20-listener MOS study displays reference text, so it is not unaided transcription intelligibility.
- **Deployment:** Offline evaluation of one implanted participant; RTF alone does not establish closed-loop conversational latency. Hardware for timing, first-audio delay, and everyday reliability are not specified.
- **Scope of this review:** Prompted attempted speech from one participant with ALS, synthetic single-speaker audio targets; not spontaneous inner speech, natural-voice restoration, or non-invasive sensing.

### Evidence

- One participant with ALS supplies prompted attempted-speech intracortical recordings. Table I lists 8,800 training and 880 test sentences; audio references are synthesized from transcripts with VITS. (Sections III and V-A; Table I; PDF pp. 2-5)
- The model uses CTC-supervised phoneme representations and a differentiable HMM to predict TTS contextual phoneme latents; it removes explicit text decoding at inference, not text-derived supervision during training. (Section IV and Figure 2; PDF pp. 3-4)
- The closed-set evaluation uniformly samples 880 utterances from the training set. Reviewer assessment: its 6.8% WER is not an independent held-out generalization result. (Section V-A; Table II; PDF pp. 4-5)
- Open-set speech WER is 47.2% for Brain2Speech-Net, 22.9% for the 5-gram cascade, 20.6% for the LLM-reranked cascade, and 105.4% for the direct-unit baseline. (Table II, Open WER column; PDF p. 5)
- Closed/open RTF is 0.504/0.532 for Brain2Speech-Net. The 5-gram cascade has 1.664/1.846. Reviewer assessment: RTF measures generation throughput and does not establish streaming first-output latency. (Table II; Section VI-B; PDF pp. 5-6)
- HMM forward-backward inference includes future observations until sequence termination; no prospective streaming communication evaluation is reported. This limits interpretation of the real-time claim. (Section IV-C; Sections V-VII; PDF pp. 4-6)
- Twenty English-speaking listeners evaluated 20 open-set samples per system with reference text displayed. Brain2Speech-Net MOS is 3.34 ± 0.11, with error bars labeled 95% confidence intervals. (Figure 3; Section VI-C; PDF pp. 5-6)
- The authors acknowledge that synthetic-reference metrics do not measure fidelity to natural recorded speech, the user's voice identity, or paralinguistic content, and that unseen-utterance performance deteriorates. (Section VII; PDF p. 6)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
