# Soft Active Electromyography Interface for Machine Learning-Enabled Silent Speech Recognition

Yuta Kurotaki, Shusuke Yamakoshi, Reitaro Yoshida, Yutaka Isoda, Tamami Takano, Yuji Isano, Yusuke Miyake, Kentaro Kuribayashi, Hiroki Ota  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2608.27048)

**Section:** [Surface EMG](../README.md#surface-emg) · **Review basis:** full_text+summary

Hand-worn soft fingertip dry-electrode EMG interface for silent recognition of 30 words with drone control; 97.2% mean participant-dependent accuracy across three participants.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Hand-worn fingertip dry electrodes, 4-channel facial surface EMG |
| Task | Closed-vocabulary word/command recognition |
| Vocabulary | 30 words (4-command drone subset) |
| Speaker | Speaker-dependent |
| Session | Not stated |
| Online / offline | Both |
| Key result | 97.2% mean participant-dependent accuracy, 30 words, 3 participants; combined model 92.1% |

**Limitations.** Only three participants and a fixed 30-word vocabulary; no unseen users or words, repeat-session, latency, power or quantified real-world testing; recognition runs on a PC.

## Full review

### In short

A strong touch-to-activate wearable EMG prototype with high closed-vocabulary accuracy, but the three-participant, speaker-dependent evaluation does not establish broad generalization or deployment readiness.

### Review

This paper is most valuable as an interaction and wearable-hardware contribution: sensing occurs only when the user touches the perioral region, avoiding permanent facial attachment while retaining dry-electrode EMG acquisition. The reported 97.2 ± 1.3% mean accuracy is strong for the tested 30-word task, and the liquid-metal interconnect and pressure tests support the device-engineering case. However, the recognition evidence comes from only three participants, the pooled model is not an unseen-user test, and real-time drone control is demonstrated without latency or command-success statistics. The work therefore establishes a credible laboratory prototype for intentional command input, not yet a general silent-speech recognizer or a validated privacy and security guarantee.

### Why it matters

The paper shows that a removable hand-worn EMG interface can acquire useful perioral signals on demand and drive a real device, shifting the SSI design question from continuous attachment toward explicit user initiation.

### Prior state of the art

Prior non-invasive SSI systems used face- or throat-mounted EMG patches and other continuously attached sensors, while intentionally placed ultrasound systems required gel or handheld operation. MFCC-based EMG classifiers and silent-command drone control had also been reported.

### What changed

The clearest contribution is relocating perioral EMG sensing to a hand-worn, touch-to-activate device that is physically off the face between inputs, while integrating stretchable liquid-metal wiring, active amplification, classification, and command control.

### Position in the field

A meaningful system-design advance for non-invasive EMG SSI that prioritizes intentional activation and reduced facial attachment, with recognition evidence still limited to a small closed-vocabulary laboratory study.

### Practical value

Potentially useful for deliberate, private command input in noisy settings where a user can touch the mouth area; current reliance on a PC, manual placement, and participant-specific data limits immediate use.

### Advanced

User-controlled sensing onset, removability from the face, mechanically compliant wiring, and a complete command-recognition demonstration move forward.

### Unresolved

Unseen-user generalization, unseen words, continuous sentences, placement and re-donning robustness, longer-term wear, quantified command latency, and field use remain unresolved.

### Narrowed or regressed

The interface is not hands-free and requires deliberate fingertip contact at four perioral locations; evaluation remains a small, closed-vocabulary, participant-dependent study.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | closed-vocabulary silent-speech word and command recognition |
| Input | Four-channel surface EMG from the buccinator, orbicularis oris, depressor labii inferioris, and mentalis using fingertip dry electrodes |
| Sensor | Ecoflex-encapsulated hand-worn interface with transparent FPC solder-coated fingertip dry electrodes, liquid-metal interconnects, an active EMG amplification circuit, a wrist reference electrode, and Arduino digitization at 1 kHz |
| Body site | face; lip; skin |
| Output | 30 word-class labels; four labels mapped to drone commands |
| Vocabulary type | closed word-level command vocabulary; examples are English, but the full language scope is not explicitly stated |
| Vocabulary size | 30 words; four-command subset for drone control |
| Metrics and results | Mean participant-dependent test accuracy 97.2 ± 1.3% (S01 97.5%, S02 98.3%, S03 95.8%); combined model test accuracy 92.1% and macro F1 0.921, with five-fold CV score 0.836; Conformer accuracy 91.1%; contact-pressure SNR 31.0–35.5 dB; liquid-metal interconnect ΔR/R0 stayed within ±0.5% across 10–50% strain tests. |
| Evaluation protocol | Participant-dependent stratified train/test evaluation with five-fold cross-validation and hyperparameter tuning; a combined three-participant model; DNN-versus-Conformer comparison; electrical durability and contact-pressure SNR measurements; and a qualitative real-time drone-control proof of concept. |

### Limits

- **Technical:** Manual contact pressure and placement can vary; only four channels fit the hand design; recognition depends on a PC; no latency, power, false-activation, repeat-session, or long-term durability evaluation of the complete worn system is reported.
- **Evaluation:** Only three participants and a fixed 30-word vocabulary were evaluated. The combined model pools those same participants rather than holding out an unseen person. No unseen-word, sentence-level, walking, longitudinal, or quantified noisy-versus-quiet comparison is reported.
- **Deployment:** Recognition ran on a PC connected to an Arduino, with commands sent to a Tello drone over Wi-Fi. End-to-end latency, battery operation, mobile execution, command success counts, environmental conditions, and sustained use were not quantified.
- **Scope of this review:** Thirty-word silent articulation by three participants (examples are English; the full language scope is not explicitly stated), with four-command drone control. No clinical users, unseen participants, unseen words, continuous speech, multilingual testing, or extended real-world use are reported.

### Evidence

- The authors present a hand-worn soft active EMG interface that acquires perioral signals only during intentional fingertip contact, classifies 30 silently articulated words, and controls a drone with four recognized commands. (Abstract; Introduction; Results, Design for Intent-Driven SSR; Application to Human-Computer Interaction)
- The main novelty is the touch-to-activate system configuration: fingertip dry electrodes, active amplification, Ecoflex encapsulation, and liquid-metal interconnects are integrated into a hand-worn device that is separated from the perioral skin outside intended use. (Results, Design for Intent-Driven SSR and Device Design and Characterization; Discussion)
- Participant-dependent DNN models achieved a mean test accuracy of 97.2 ± 1.3% across three participants (97.5%, 98.3%, and 95.8%); the pooled three-participant model achieved 92.1% test accuracy and macro F1 of 0.921. (Results, Implementation of Machine Learning-Integrated Silent Speech Interface; Discussion; Supplementary Figures 9 and 16)
- The dataset contains 30 word classes from three participants: S01 recorded 60 trials per word, while S02 and S03 recorded 30 trials per word; Gaussian jitter augmented only the S02/S03 training data, and evaluation used stratified splitting and five-fold cross-validation. (Methods, Software for silent speech classification; Results, Implementation of Machine Learning-Integrated Silent Speech Interface)
- The study does not evaluate held-out unseen participants, unseen words, continuous sentences, walking, repeat-session placement variability, or long-term real-world use; the authors identify placement variability, vocabulary expansion, and sentence-level recognition as future work. (Discussion, final paragraph; Methods)
- A PC executed the pretrained classifier in real time, received four-channel EMG through an Arduino, and sent Start, Move, Turn, and Stop commands over Wi-Fi to a Tello drone; latency and per-command success statistics were not reported. (Results, Application to Human-Computer Interaction; Methods, Drone operation application)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
