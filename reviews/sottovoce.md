# SottoVoce: An Ultrasound Imaging-Based Silent Speech Interaction Using Deep Neural Networks

Naoki Kimura, Michinari Kono, Jun Rekimoto  
CHI '19 · [DOI](https://doi.org/10.1145/3290605.3300376)

**Section:** [Ultrasound & tongue imaging](../README.md#ultrasound--tongue-imaging) · **Review basis:** full_text+existing_expert_seed

SottoVoce reconstructs speech audio from under-jaw ultrasound images with two DNNs to control unmodified smart speakers; command success rose from 42.5% to 65.0% with the second network, versus 90.0% for real audio.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | 3.5 MHz convex ultrasound probe under the jaw |
| Task | Speech synthesis from ultrasound for voice-assistant control |
| Vocabulary | ~500 training commands; 4 Alexa commands in end-to-end test |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Offline |
| Key result | 65.0% smart speaker command success (4 commands x5, two networks) vs 90.0% ground-truth audio |

**Limitations.** Only two participants, speaker-dependent, tiny end-to-end command set, bulky non-wearable probe, 2.61 s latency, and unassessed ultrasound safety.

## Full review

### In short

A solid proof of concept that reconstructs speech audio from ultrasound for controlling unmodified smart speakers, showcasing important system design insight despite prototype limitations in latency, hardware bulk, and speaker dependency.

### Review

Kimura et al. present a well-engineered proof of concept for silent speech interaction using ultrasonic imaging and deep neural networks. Their primary contribution is a two-stage neural pipeline converting ultrasonic images captured below the jaw into Mel-spectrogram features and refining those into audio signals, which can then control unmodified commercial smart speakers like Amazon Alexa. This architectural decision to reconstruct audio, rather than directly classify commands, is a significant reframing within SSI research. The study provides modest yet concrete quantitative results: a 65% command recognition success rate with the two-network pipeline, 33.56% word error rate on Google STT, and demonstration of system use with limited command sets. They explicitly discuss limitations such as speaker dependence, system latency (~2.61 s), bulky hardware, and user adaptation requirements for silent speech without vocal fold vibration. These aspects clarify that while the prototype is not ready for real-world deployment or continuous real-time interaction, it is a strong conceptual and technical foundation for future research on SSI architectures that reuse existing voice ecosystems via speech regeneration.

### Why it matters

This paper's key value lies in reframing silent speech interaction as a speech regeneration and ecosystem reuse problem, deploying a two-stage DNN approach to produce audio from ultrasonic tongue and jaw imaging. It demonstrates practical integration with existing voice agents, highlighting a promising architectural direction distinct from direct command recognition methods.

### Prior state of the art

Most prior silent speech interfaces recognized commands directly or relied on visible cameras or other sensors, lacking integration with unchanged smart speaker ecosystems.

### What changed

This work shifts SSI from direct command recognition to speech audio regeneration that can be fed to standard speech recognition engines and smart speakers without modification.

### Position in the field

An early and influential demonstration of ultrasound-based speech regeneration SSI with system-level insights stronger than its present prototype performance.

### Practical value

medium as a systems design contribution and research direction; low-to-medium as a direct deployable interface in reported form

### Advanced

ecosystem_integration; speech_regeneration; smart_speaker_control; user_adaptation_loop

### Unresolved

real_time_interaction; open_vocabulary; speaker_independence; wearable_ultrasound

### Evaluation details

| Item | Details |
| --- | --- |
| Task | speech-reconstruction |
| Input | ultrasound |
| Sensor | 3.5 MHz convex ultrasound probe attached under the jaw, with ultrasound images captured to display monitor and digitized video stored |
| Body site | jaw; oral-cavity |
| Output | speech-audio |
| Vocabulary type | Command-level |
| Vocabulary size | Approximately 500 training spoken commands per collaborator; end-to-end evaluation on four specific Alexa commands repeated five times each |
| Metrics and results | Network 1 alone achieved an average 42.5% smart speaker command recognition success; Network 1 plus Network 2 achieved 65.0%; ground-truth audio reached 90.0%. Google speech-to-text word error rates were 41.03% for Network 1 outputs and 33.56% for Network 2 outputs, versus 20.61% for ground truth audio. |
| Evaluation protocol | Quantitative smart speaker success rates, word error rates with Google speech-to-text, and qualitative user adaptation observations. |

### Limits

- **Technical:** Speaker-dependent training; latency unsuitable for real-time use (2.61 s per utterance); differences in silent versus voiced articulation require user adaptation; bulky hardware; potential unknown safety issues with continuous ultrasound emission; small vocabulary size.
- **Evaluation:** Only two participants were used for training and testing; the command vocabulary is small (four Alexa commands) in end-to-end testing, repeated five times each; and no speaker-independent or open vocabulary evaluations were performed.
- **Deployment:** The device requires a bulky 3.5 MHz convex probe attached under the jaw and digitized display capture; continuous ultrasonic emission safety is not evaluated; the system is not wearable or miniaturized; and its latency (~2.61 s per command) is too slow for real-time use.
- **Scope of this review:** Prototype supports only a fixed small command vocabulary in speaker-dependent training; no demonstration of open vocabulary or continuous real-time interaction.

### Evidence

- An ultrasound-only silent-voice system that regenerates audio and controls an unchanged smart speaker with deep neural networks. (Abstract)
- Network 1 plus Network 2 reached 65.0% smart-speaker command success versus 42.5% for Network 1 alone and 90.0% ground-truth audio; Google speech-to-text WER for Network 2 was 33.56%; total processing time was 2.61 s for a roughly 3.68 s command clip. (4   RESULTS)
- Approximately 500 speech commands were collected from each of two collaborators using an ultrasound probe under the jaw with paired audio, speaker-dependent training only, and end-to-end testing used four Alexa commands repeated five times each. (4   RESULTS)
- The system is speaker dependent, slow (2.61 seconds per command), limited to four end-to-end commands, uses bulky 3.5 MHz probe hardware under the jaw, and users must adapt their silent articulation for best results. (5   END-TO-END EVALUATION)
- Generated audio signals can control existing smart speakers like Amazon Echo and Echo Show without modification, demonstrated with four Alexa commands. (4   RESULTS)
- The paper's main novelty lies in system design to reconstruct speech audio from ultrasound images and use that to control unmodified smart speakers, rather than direct command recognition from ultrasound features. (3   SYSTEM ARCHITECTURE OF SOTTOVOCE)
- The system is not real-time; with 3.68 s of input, neural networks processing consumes 2.36 s and total processing time is 2.61 s, unsuitable for real-time interaction. (3   SYSTEM ARCHITECTURE OF SOTTOVOCE)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
