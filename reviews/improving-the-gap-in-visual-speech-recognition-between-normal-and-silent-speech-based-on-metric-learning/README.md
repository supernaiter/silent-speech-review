# Improving the Gap in Visual Speech Recognition Between Normal and Silent Speech Based on Metric Learning

Sara Kashiwagi, Keitaro Tanaka, Qi Feng, Shigeo Morishima  
Interspeech 2023 · [DOI](https://doi.org/10.21437/Interspeech.2023-370) · [arXiv](https://arxiv.org/abs/2305.14203)

**Section:** [Lip & face video](../../README.md#lip--face-video) · **Review basis:** full_text

A structured review of *Improving the Gap in Visual Speech Recognition Between Normal and Silent Speech Based on Metric Learning* (Sara Kashiwagi et al., Interspeech 2023) for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.

Viseme-level metric learning that aligns normal and silent speech representations to improve silent visual speech recognition, reaching baseline parity with much less silent data on AV Digits.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Lip video cropped via Dlib face landmarks |
| Task | Closed-set phrase recognition (silent VSR) |
| Vocabulary | 10 fixed phrases |
| Speaker | Speaker-independent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 6.66% VER, 9.97% WER on silent speech, 10-phrase AV Digits |

**Limitations.** Limited to 10 fixed phrases on small datasets; no open-vocabulary, continuous speech, real-time, or in-the-wild evaluation.

## Full review

### In short

Strong viseme-level metric learning approach reduces silent speech VSR errors on a small 10-phrase dataset, notably achieving parity with baselines using much less silent data.

### Review

This paper addresses the longstanding silent speech gap in visual speech recognition by framing normal and silent speech as viseme distribution alignment problems, employing novel metric learning losses that minimize KL divergence between viseme probability distributions both inter- and intra-speech types. This methodological reframing allows leveraging scarce silent training data more efficiently, as validated on the AV Digits dataset with an augmentation from OuluVS2 normal speech. The key result is that with half the silent data, the method achieves equivalent or better silent speech visual recognition error rates than strong baselines. However, the vocabulary remains tiny (10 fixed phrases), and evaluation is restricted to carefully controlled datasets without real-time or in-the-wild deployment studies. Thus, the contribution is a technically strong, core silent VSR contribution demonstrating successful viseme-level metric learning for cross-speech mode alignment, but its scalability to open vocabulary or larger datasets and deployment robustness is untested.

### Why it matters

Provides one of the first effective metric learning methods to close the performance gap in silent speech visual recognition by aligning viseme distributions between normal and silent speech, validated with controlled public datasets but still limited in vocabulary scale and real-world robustness assessment.

### Prior state of the art

Silent visual speech recognition performs worse than normal speech VSR due to scarcity of silent data and differing lip dynamics between speaking modes.

### What changed

Instead of treating normal and silent speech independently, the paper proposes minimizing Kullback-Leibler divergence between predicted viseme distributions across speech types, imposing metric learning regularization that aligns viseme representations between normal and silent speech.

### Position in the field

Core SSI-adjacent visual speech recognition work improving silent speech recognition

### Practical value

Useful for low-data silent phrase recognition scenarios, enabling better silent VSR using limited silent data by leveraging abundant normal speech data through metric learning.

### Advanced

low_data_transfer; visual_silent_recognition; viseme_alignment

### Unresolved

open_vocabulary; in_the_wild_robustness; richer_language_modeling

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-recognition |
| Input | video (lip-focused grayscale video frames) |
| Sensor | face-aligned lip video captured and cropped using Dlib face landmarking |
| Body site | lip |
| Output | text |
| Vocabulary type | fixed phrase |
| Vocabulary size | 10 phrases |
| Metrics and results | Viseme Error Rate (VER) and Word Error Rate (WER); best silent speech result: 6.66% VER and 9.97% WER with combined losses including LNCE, LSCE, LWKL, LNKL, LSKL |
| Evaluation protocol | Viseme Error Rate (VER) and Word Error Rate (WER) on AV Digits silent and normal speech, plus OuluVS2 normal speech augmentation; cross-validation with 39 speakers. |

### Limits

- **Technical:** Model limited to 10 fixed phrases, using separate visual and language models, relying on text to phoneme to viseme mapping; no end-to-end open vocabulary training or testing; small dataset size limits broader applicability.
- **Evaluation:** Evaluation is limited to AV Digits and OuluVS2 datasets focused on short fixed phrases; no validation on open vocabulary, larger vocabulary, or continuous speech datasets.
- **Deployment:** Current work lacks real-time mobile evaluation and robustness testing in-the-wild; system trained and validated only on small 10-phrase vocabulary datasets and controlled setups.
- **Scope of this review:** Limited to closed vocabulary phrase recognition on small datasets; does not address continuous or open vocabulary speech recognition or real-world conditions.

### Evidence

- This paper presents a novel metric learning approach to address the performance gap between normal and silent speech in visual speech recognition (VSR) by leveraging the shared literal content between the two speech types. (Abstract)
- The main contribution is a novel metric learning approach based on viseme distribution alignment using Kullback-Leibler divergence to bring normal and silent speech viseme probability distributions close in latent space, enabling better silent speech VSR. (3.2. Metric learning for inter)
- Viseme Error Rate (VER) and Word Error Rate (WER) metrics were used for evaluation; best silent speech results were 6.66% VER and 9.97% WER achieved by the combined loss LNCE + LSCE + LWKL + LNKL + LSKL. (4.4. Experimental results)
- Evaluation was conducted on the AV Digits dataset with 39 speakers uttering 10 fixed phrases in both normal and silent speech modes, augmented with 1560 normal speech utterances from OuluVS2; the test set includes 550 utterances from 11 speakers. (4.1. Database)
- The study is limited to a small fixed vocabulary of 10 phrases and uses only controlled datasets (AV Digits and OuluVS2) without any evaluation on open vocabulary, continuous speech, or in-the-wild conditions, restricting generalization and deployment readiness. (5. Conclusion)
- The approach improves silent speech VSR accuracy with less silent data, achieving parity with baseline trained on twice the silent data, but lacks real-time or in-the-wild mobile deployment evaluations. (4.4. Experimental results)

## More reviews in Lip & face video

- [Audio Knowledge Empowered Visual Speech Recognition](../akvsr-audio-knowledge-empowered-visual-speech-recognition-by-compressing-audio-knowledge-of-a-pretrained-model/) (2023). AKVSR improves visual speech recognition by transferring compressed linguistic knowledge from a pretrained audio model through a compact memory and cross-attention, without audio at inference. LRS3 WER drops from 46.1% to 41.6% (BASE).
- [Audio-visual video-to-speech synthesis with synthesized input audio](../audio-visual-video-to-speech-synthesis-with-synthesized-input-audio/) (2023). Adds synthesized audio from a first-stage video-to-audio model as an auxiliary input to a second-stage audiovisual video-to-speech model. Improves reconstruction quality and intelligibility on benchmarks, though gains vary by model and dataset.
- [Auto-AVSR: Audio-Visual Speech Recognition with Automatic Labels](../auto-avsr-audio-visual-speech-recognition-with-automatic-labels/) (2023). Training lipreading and AV-ASR on 3,448 h including ASR-pseudo-labelled AVSpeech and VoxCeleb2 cuts LRS3 visual-only WER to 19.1% and audio-visual WER to 0.9%.
- [High-Quality Automatic Voice Over with Accurate Alignment: Supervision through Self-Supervised Discrete Speech Units](../high-quality-automatic-voice-over-with-accurate-alignment-supervision-through-self-supervised-discrete-speech-units/) (2023). An automatic voice-over system that supervises alignment by predicting self-supervised discrete speech units from text and lip video, improving lip-sync and speech quality on a single-speaker dataset. Not an SSI paper.
- [Intelligible Lip-to-Speech Synthesis with Speech Units](../intelligible-lip-to-speech-synthesis-with-speech-units/) (2023). Lip-to-speech synthesis using self-supervised speech units as a pseudo-text target plus a multi-input vocoder; substantially cuts WER without text labels and reports state-of-the-art results on LRS2/LRS3.
- [Large-scale unsupervised audio pre-training for video-to-speech synthesis](../large-scale-unsupervised-audio-pre-training-for-video-to-speech-synthesis/) (2023). Pretrains the decoder of a video-to-speech model on large audio-only corpora, improving reconstruction quality on GRID, TCD-TIMIT and LRW, though WER gains are not consistent.

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
