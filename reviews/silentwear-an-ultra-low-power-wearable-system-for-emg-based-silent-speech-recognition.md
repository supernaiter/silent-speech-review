# SilentWear: an Ultra-Low Power Wearable System for EMG-based Silent Speech Recognition

Giusy Spacone, Sebastian Frey, Giovanni Pollo, Alessio Burrello, Daniele Jahier Pagliari, Victor Kartsch, Andrea Cossettini, Luca Benini  
arXiv 2026 · [arXiv](https://arxiv.org/abs/2603.02847)

**Section:** [Surface EMG](../README.md#surface-emg) · **Review basis:** full_text+summary

SilentWear, an ultra-low-power dry textile neckband with embedded CNN for EMG command recognition; silent balanced accuracy is 77.5% on pooled-day batches but drops to 59.3% on a new day.

## Evaluation conditions

| | |
| --- | --- |
| Sensor | Dry textile neckband, 14-channel differential surface EMG |
| Task | Closed-set command recognition |
| Vocabulary | 8 commands plus rest |
| Speaker | Speaker-dependent |
| Session | Cross-day |
| Online / offline | Offline |
| Key result | 59.3% silent balanced accuracy on held-out days (77.5% pooled-day), 9 classes; 2.47 ms inference |

**Limitations.** Only four subjects and subject-specific models; large drop on new days; no closed-loop user study, walking or false-trigger evaluation.

## Full review

### In short

A useful dry-neckband and embedded-CNN study: silent balanced accuracy falls from 77.5% across pooled-day batches to 59.3% on a new day; 2.47 ms is compute time, while closed-loop usability remains untested.

### Review

SilentWear is strongest as an integrated sensing-and-embedded-computing study. It combines a fully dry 14-channel textile neckband, a 15,489-parameter CNN and explicit multiday tests, while reporting both inference energy and the larger acquisition/communication power budget. The key recognition result is the day-transfer gap: silent balanced accuracy is 77.5% when training and testing use different batches from the same set of days, but only 59.3% when an entire day is held out. That difference is more informative for daily use than the headline accuracy alone. Incremental fine-tuning improves next-batch results with roughly one additional acquisition batch, although this is supervised recalibration and is not demonstrated as on-device learning. The embedded measurements are valuable but must retain their boundaries: 2.47 ms is inference time on an 800 ms window, predictions are scheduled every 100 ms, and the 27.1-hour battery duration is an estimate from the reported power and battery capacity. Neither the analytical information-transfer rate nor near-perfect classification of cued rest segments measures actual communication throughput or accidental activations during daily activity. The paper explicitly says that online closed-loop system validation remains future work. Offline zero-phase filtering also needs reconciliation with a causal deployed implementation, and quantized recognition accuracy is not separately reported. This is a useful reproducible direction for personalized command interfaces, with stronger hardware evidence than evidence for everyday communication readiness.

### Why it matters

Makes the cost of day-to-day sensor repositioning visible while providing a compact embedded baseline and a concrete supervised recalibration strategy.

### Prior state of the art

Dry neck EMG sensing and the BioGAP-Ultra hardware were presented in prior work. Wearable SSI reports often use small vocabularies and offline classifiers without testing electrode repositioning or reporting integrated energy.

### What changed

Extends the prior neckband study with four-person multiday recordings, a small CNN, next-batch fine-tuning and GAP9 deployment benchmarks.

### Position in the field

Personalized non-invasive EMG command recognition with on-device inference and dry neck sensing; distinct from open-vocabulary speech transcription or synthesis.

### Practical value

Strong candidate baseline for research on low-power personalized command interfaces; hardware and day-transfer evidence identify practical development priorities.

### Advanced

Combines fully dry neck sensing with measured embedded compute/energy and explicit unseen-day/repositioning evaluation; provides sequential recalibration comparisons and public data/code links.

### Unresolved

Closed-loop communication accuracy, accidental activations in daily activity, cross-user generalization, quantized-versus-floating accuracy, causal preprocessing parity, long-duration comfort and measured battery endurance.

### Narrowed or regressed

Silent balanced accuracy drops from 77.5% in pooled-day batch evaluation to 59.3% on a held-out day. An 800 ms window improves calculated throughput and compute cost at some accuracy loss.

### Evaluation details

| Item | Details |
| --- | --- |
| Task | command-recognition |
| Input | 14-channel differential surface EMG from a fully dry textile neckband. |
| Sensor | 27 dry SoftPulse electrodes in a textile neckband form 14 differential channels: 10 overlapping central channels and four lateral channels; four shorted electrodes provide ground. BioGAP-Ultra uses two ADS1298 AFEs, GAP9/NE16 and nRF5340 BLE, in 26 x 65 x 13 mm electronics with a 150 mAh Li-Po battery. |
| Body site | throat |
| Output | commands;labels |
| Vocabulary type | closed-set isolated commands |
| Vocabulary size | Eight fixed commands plus one rest class, nine output classes total. |
| Metrics and results | Table II, 1.4 s windows: SpeechNet balanced accuracy 84.8 +/- 4.6% vocalized and 77.5 +/- 6.6% silent for pooled-day held-out batches; 71.1 +/- 8.3% and 59.3 +/- 2.2% for held-out days. Random Forest silent results are 62.9% and 48.7%, respectively. Table III, 800 ms windows: 2.47 ms / 63.9 microjoules at 240 MHz, or 1.60 ms / 97.1 microjoules at 370 MHz. System power 20.5 mW with 100 ms stride; estimated battery life 27.1 h. Author-reported measurements, not independently reproduced. |
| Evaluation protocol | Subject-specific balanced accuracy using pooled-day held-out batches, leave-one-session-out testing and sequential next-batch fine-tuning; window-length ablation and analytical ITR; embedded latency/energy benchmarking. |

### Limits

- **Technical:** Offline preprocessing uses a zero-phase 20 Hz high-pass filter plus 50 Hz notch; causal deployment equivalence is not established. Trigger timing imperfectly aligns articulation. Quantization changes recognition accuracy by an unreported amount. Whole-window ITR omits actual cue/rest/correction overhead.
- **Evaluation:** Four subjects and eight commands plus rest. Global evaluation mixes every recording day into train and test through different batches; only leave-one-session-out isolates a new day. All models remain subject- and mode-specific. Rest is downsampled to class balance, unlike typical idle-heavy use. Online closed-loop validation is explicitly future work.
- **Deployment:** Personalized fixed-command models, cued seated data and sensor-fit sensitivity. No closed-loop user study, walking/activity false-trigger study, patient cohort or measured all-day endurance. Recalibration is trained offline rather than demonstrated on-device.
- **Scope of this review:** Four seated participants, eight prompted English commands plus rest, three days and separate models for vocalized/silent conditions. No unseen words, sentences, patient communication or naturalistic continuous use.

### Evidence

- Four subjects each provide three multiday sessions with neckband repositioning, containing eight prompted commands in vocalized and silent modes. Classification includes a ninth rest class, which is downsampled for balance. (Sections III-B/C; PDF pp. 3-4)
- SpeechNet uses temporal then spatial CNN blocks with 15,489 parameters; the dry neckband hardware extends prior conference work. GAP9 deployment uses 8-bit post-training quantization. (Sections III-A/E/G; Table I; PDF pp. 3-5)
- Silent balanced accuracy is 77.5 +/- 6.6% for pooled-day held-out batches and 59.3 +/- 2.2% for held-out sessions, an 18.2 percentage-point gap. Corresponding Random Forest values are 62.9% and 48.7%. (Table II; PDF p. 6)
- The Global protocol trains and tests on separate batches from all three days. The Inter-Session protocol holds one day out. Models are explicitly subject-specific and condition-specific. (Section III-D; PDF p. 4)
- The text reports that one 1.4-second-window adaptation round improves silent accuracy from about 58% to 72%, with roughly 20 repetitions per word and about 10 minutes of acquisition. The protocol evaluates the following unseen batch. (Sections III-D and IV-D; Figures 7/8; PDF pp. 4 and 7-8)
- For an 800 ms input, GAP9 achieves 2.47 ms and 63.9 microjoules per inference at 240 MHz/0.65 V, or 1.60 ms and 97.1 microjoules at 370 MHz/0.8 V. (Table III; Section IV-E; PDF pp. 7-8)
- A 100 ms sliding-window stride gives reported total power 20.5 mW: 15.3 mW acquisition, 4.55 mW data handling/result streaming and 0.639 mW compute. Battery life of 27.1 h with 150 mAh is explicitly estimated. (Section IV-E; PDF p. 8)
- Online validation under real-time closed-loop user interaction and adaptive recalibration is explicitly left for future work. Reviewer assessment: embedded latency does not establish operational communication accuracy or usability. (Section V; PDF p. 10)
- ITR uses class accuracy and input-window duration; reported silent peak is 69.2 bit/min at 800 ms. Reviewer assessment: this analytical rate omits the cued protocol, rest intervals and error correction and is not measured user throughput. (Sections III-B/F and IV-C; PDF pp. 3-6)
- Offline preprocessing uses a zero-phase Butterworth high-pass filter; acquisition labels follow visual triggers with acknowledged reaction-time mismatch. Reviewer assessment: causal online filter/segmentation parity and post-quantization accuracy need explicit verification. (Sections III-C/G and V; PDF pp. 4-5 and 9-10)
- Figures 7/8 use five tested batches with the first batch preceding adaptation, leaving four sequential updates in the specified protocol; the text nevertheless describes five fine-tuning rounds and Figure 8 repeats a vocalized caption. Reviewer assessment: update counts and condition labeling need correction. (Sections III-D and IV-D; Figures 7/8; PDF pp. 4 and 7-8)

---

Part of the [Silent Speech Interface Review](https://github.com/supernaiter/silent-speech-review). Found an error? [Open an issue](https://github.com/supernaiter/silent-speech-review/issues/new?template=correction.yml).
