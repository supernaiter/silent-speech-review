# SilentWear: an Ultra-Low Power Wearable System for EMG-based Silent Speech Recognition

Spacone, G., Frey, S., Pollo, G., Burrello, A., Jahier Pagliari, D., Kartsch, V., Cossettini, A., Benini, L. · arXiv preprint · 2026 · [arXiv:2603.02847](https://arxiv.org/abs/2603.02847)

## Verdict

The paper [[1]](#ref-1) changes deployment (M13), running a 15,489-parameter CNN on the neckband, and training (M03), fine-tuning on new-session batches. The sensor (M05) is the authors' 2025 neckband [[2]](#ref-2) [concurrent], with its hardware reused (§III-A). M13 is the strongest part: 20.5 mW including inference is below every read wearable that streams raw data [[2]](#ref-2), [[3]](#ref-3), [[4]](#ref-4), but the quantized on-device model has no accuracy figure (§IV-E), so the deployed path is unvalidated. M03 is standard: supervised recovery after electrode repositioning dates from 2005 [[5]](#ref-5), and no label-free baseline is run. The headline 77.5% silent accuracy tests days already in training; an unseen day gives 59.3% (Table II).

## Against the field, component by component

### M13 Deployment: on-body inference and power

**Usual approach:** 24 of 30 speech-wearable studies on the topic (pattern match, Appendix) decode off the body with no energy, latency or power figure [[6]](#ref-6), [[4]](#ref-4).

**State of the art:** No read prior decodes on the body. Lowest raw streaming: the same neckband at 22.2 mW [[2]](#ref-2) (2025), then 46 mW [[3]](#ref-3) and 76.5 mW [[4]](#ref-4). The target: 20.5 mW, one inference per 100 ms at 63.9 µJ and 2.47 ms (§IV-E).

Against the same hardware the saving is 1.7 mW (inference); inference takes 0.639 mW (§IV-E). Larger gaps mix front ends, radios and sensors. The authors' priority claim for on-device processing at the neck (§IV-F) holds against the read priors (Appendix). Accuracy comes from GPU runs, as the authors state (§III-E). Verdict: standard, as no on-device effect is shown across subjects.

### M03 Training: recalibration after repositioning

**Usual approach:** Among 41 sEMG studies with session or re-attachment wording (pattern match, Appendix), the most common design is session-independent training or label-free adaptation (11); 5 fine-tune on labeled new-session data, as the target does.

**State of the art:** An around-ear interface reached 92.24% across days without test-day calibration on a 25-class sentence task over three seeds [[7]](#ref-7) [concurrent] (2026). The target needs one labeled round to lift silent accuracy from 58% to 72% at a 1.4 s window (§IV-D).

In 2005, repositioning cut seven-channel EMG accuracy on ten digits from 97.3% to 76.2%, 21.1 points or 21.7% relative (inference), and normalization plus adaptation restored 87.1% [[5]](#ref-5). The target's silent drop from 77.5% to 59.3% is 18.2 points, 23.5% relative (inference), from different starting points (four subjects, 9 classes; three speakers, 10 digits). Verdict: standard.

### M05 Sensors: dry textile neckband

**Usual approach:** Of 21 dry or worn-object sEMG speech studies (pattern match, Appendix), 16 mention adhesive or tattoo-like patches and 7 a collar, choker, necklace or neckband; a study can match several (16 is an upper bound).

**State of the art:** 98.7% on five phrases from a textile scarf sensing radio-frequency phase, not sEMG [[8]](#ref-8) [concurrent] (2026). Read sEMG figures: 96% on 10 words, silver-paste electrodes [[6]](#ref-6); 92.7% on 11 voiced words, wet reference [[3]](#ref-3); both random splits; 5-, 10- and 11-class figures are not comparable.

Removing the wet reference dates from the 2025 version [[2]](#ref-2). Verdict: standard.

### M12 Evaluation: splits across sessions and speakers

**Usual approach:** Among 143 wearable-sensor word-classification studies (pattern match, Appendix), the most common split is speaker-disjoint (65), then random or k-fold (58) and session-disjoint (44); categories overlap. The target has per-subject batch and session splits, none speaker-disjoint.

**State of the art:** A neck-worn strain interface reached 85.8% on 26 words under subject-independent cross-validation [[9]](#ref-9) [concurrent] (2026).

Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Cued vocalized and silent commands | Recorded articulation (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Cue-derived class labels | Text or paired-audio targets (slot-filled 31) | – | standard |
| M03 Training and adaptation | Fine-tune on labeled new-session data | Label-free adaptation (pattern match 11) | 92.24% cross-day without calibration [[7]](#ref-7) (2026) | standard |
| M04 Use-time action | Vocalized or silent, 8 commands | Silent or overt (slot-filled 5,595) | – | standard |
| M05 Sensors | Dry textile neckband, 14 channels | Adhesive or tattoo-like patches (pattern match 16) | 98.7% on 5 phrases, RF-phase scarf, not sEMG [[8]](#ref-8) (2026) | standard |
| M06 Processing and decoding | 15k-parameter CNN; Random Forest baseline | Classifier over fixed windows (slot-filled 7,345) | – | standard |
| M07 Lexicon and LM | None (closed 9-class decision) | Lexicon or LM (slot-filled 119) | – | standard |
| M08 Output | Command or rest label | Class label (slot-filled 3,268) | – | standard |
| M09 Confirmation | Offline | Confirmation step (slot-filled 82) | – | not applicable |
| M10 Correction | Offline | Correction step (slot-filled 82) | – | not applicable |
| M11 Reference construction | Cue-trigger labels | Cue or transcript references (slot-filled 234) | – | standard |
| M12 Evaluation | Per-subject batch and session splits | Speaker-disjoint test (pattern match 65) | 85.8% on 26 words, subject-independent [[9]](#ref-9) (2026) | standard |
| M13 Device and cost | On-device CNN, 20.5 mW | Off-body, no power figure (pattern match 24) | No on-body prior; 22.2 mW raw streaming [[2]](#ref-2) (2025) | standard |

## Where the claims outrun the evidence

- The abstract leads with within-session results (84.8%, 77.5%), not unseen-day ones (71.1%, 59.3%; §III-D, Table II).
- "superior performance compared to our prior solution" (§V) compares cross-validated 84.8% and 77.5% (four subjects, 9 classes) with 87% and 68% (one subject, 8 classes, shuffled 5-fold) [[2]](#ref-2): vocalized is lower. Leave-one-session-out favours the target (71.1% vs 64%, 59.3% vs 54%).
- "more than 10% accuracy recovery with less than 10 minutes" (Abstract) is loose: one round of 20 repetitions per command takes about 10 minutes and lifts accuracy by 10 points vocalized (70% to 80%) and 14 silent (58% to 72%) (§IV-D).
- Transfer rates of 92.7 and 69.2 bit/min (§IV-C) are calculated; the authors leave closed-loop validation to future work (§V).
- No chance level is reported (§III-D); the code fixes one seed, 42.

## What the field needs next

- M13: per-subject accuracy of the quantized model on the device with causal filtering.
- M03: labeled fine-tuning against label-free normalization or feature-space adaptation at matched data, from 2 to 20 repetitions per command.
- M12: leave-one-subject-out and calibration-free unseen-day tests.

## Questions for the authors

- How much do results vary across seeds?
- Was the from-scratch fine-tuning baseline matched in data and update count?
- How often are commands detected during non-speech activity?

## Appendix: literature search

- M13, wearable-speech-sensor-on-device-inference. Inclusion rule: non-acoustic silent-speech or speech-recognition wearables (EMG, strain, accelerometer, ultrasound, EEG) whose decoder runs on an embedded processor on or near the body rather than on a PC, phone or cloud; the design compared is whether inference latency, energy per inference and total system power are measured; neural implants with external processing, acoustic keyword spotting and PC-tethered demos are excluded when read; versions count once. Ledger: 6,075 unique studies slot-filled for M13; 30 unique studies pattern match. Designs (full-text pattern match): energy per inference 4 (the target and three EEG handwriting studies), inference latency 3, system power 3; none of the three 24. Read in full: [[2]](#ref-2), [[3]](#ref-3), [[6]](#ref-6), [[4]](#ref-4). Known-item recall 1.0 (2 of 2 seeds).
- M03, emg-cross-session-recalibration. Inclusion rule: surface-EMG speech or silent-speech decoders tested on a session or day not used for training (electrodes re-attached), classified as no recalibration, supervised fine-tuning or retraining on new-session data, or unsupervised or feature-level adaptation; same-session random splits only, cross-speaker transfer without a session test, non-EMG sensors and reviews are excluded when read; versions count once. Ledger: 1,526 unique studies slot-filled for M03; 41 unique studies pattern match. Designs (full-text pattern match): unsupervised or feature-space adaptation 11, supervised new-session fine-tuning 5, no-recalibration wording 3. Read in full: [[5]](#ref-5), [[2]](#ref-2), [[7]](#ref-7). Known-item recall 1.0 (3 of 3 seeds).
- M05, wearable-integrated-dry-emg-speech-sensing (published table, reused). Inclusion rule: surface-EMG speech or silent-speech decoding with dry, textile or printed electrodes mounted on a worn object or garment; tattoo-like dry patches count as dry but not integrated; wet adhesive arrays and non-EMG wearables are excluded; versions count once. Ledger: 7,329 unique studies slot-filled for M05; 21 unique studies pattern match. Usual design: adhesive or tattoo-like patch wording, 16 of 21 (pattern match, upper bound); collar, choker, necklace or neckband 7; a study can match several. Read in full: [[3]](#ref-3), [[2]](#ref-2), [[6]](#ref-6), [[8]](#ref-8). Known-item recall 0.5.
- M12, wearable-sensor-word-test-split (published table, reused). Inclusion rule: word or command classification with a wearable non-acoustic face or neck sensor, classified by how test samples are separated from training samples (speaker-disjoint, session- or day-disjoint, random or per-class split); a paper counts under every split it reports. Ledger: 6,960 unique studies slot-filled for M12; 143 unique studies pattern match. Designs (pattern match, overlapping): speaker-disjoint 65, random or k-fold 58, session-disjoint 44. Read in full: [[5]](#ref-5), [[2]](#ref-2), [[9]](#ref-9).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Spacone, G., Frey, S., Pollo, G., Burrello, A., Jahier Pagliari, D., Kartsch, V., et al. “SilentWear: an Ultra-Low Power Wearable System for EMG-based Silent Speech Recognition.” *arXiv preprint (IEEE Sensors Journal format)*, 2026. doi:[10.48550/arXiv.2603.02847](https://doi.org/10.48550/arXiv.2603.02847). arXiv:[2603.02847](https://arxiv.org/abs/2603.02847). Target. Read as arXiv v2. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/silentwear-an-ultra-low-power-wearable-system-for-emg-based-silent-speech-recognition) [wiki: arxiv-2603.02847](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2603.02847/article.md)
2. <a id="ref-2"></a>Meier, F., Spacone, G., Frey, S., Benini, L., Cossettini, A. “A Parallel Ultra-Low Power Silent Speech Interface based on a Wearable, Fully-dry EMG Neckband.” *2025 IEEE SENSORS*, 2025. doi:[10.1109/SENSORS59705.2025.11330464](https://doi.org/10.1109/SENSORS59705.2025.11330464). arXiv:[2509.21964](https://arxiv.org/abs/2509.21964). The target's own conference version, which the target extends; deciding prior for M05, M03, M12, M13. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-parallel-ultra-low-power-silent-speech-interface-based-on-a-wearable-fully-dry-emg-neckband) [wiki: arxiv-2509.21964](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2509.21964/article.md)
3. <a id="ref-3"></a>Wu, P., Kaveh, R., Nautiyal, R., Zhang, C., Guo, A., Kachinthaya, A., et al. “Towards EMG-to-Speech with a Necklace Form Factor.” *Proc. Interspeech 2024*, 2024. doi:[10.21437/Interspeech.2024-1568](https://doi.org/10.21437/Interspeech.2024-1568). arXiv:[2407.21345](https://arxiv.org/abs/2407.21345). Prior; deciding prior for M05 and M13. [wiki: isca-wu24k_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-wu24k_interspeech/article.md) [wiki: arxiv-2407.21345](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2407.21345/article.md) [wiki: doi-10.48550-arxiv.2407.21345](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.48550-arxiv.2407.21345/article.md)
4. <a id="ref-4"></a>Tang, C., Gao, S., Li, C., Yi, W., Jin, Y., Zhai, X., et al. “Wearable intelligent throat enables natural speech in stroke patients with dysarthria.” *Nature Communications*, 2026. doi:[10.1038/s41467-025-68228-9](https://doi.org/10.1038/s41467-025-68228-9). arXiv:[2411.18266](https://arxiv.org/abs/2411.18266). arXiv 2024; deciding prior for M13. The .bib lists the first twelve authors. [wiki: arxiv-2411.18266](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2411.18266/article.md) [wiki: pmc-12816716-intelligent-throat](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12816716-intelligent-throat/article.md)
5. <a id="ref-5"></a>Maier-Hein, L., Metze, F., Schultz, T., Waibel, A. “Session Independent Non-Audible Speech Recognition Using Surface Electromyography.” *Proc. IEEE ASRU 2005*, 2005. doi:[10.1109/ASRU.2005.1566521](https://doi.org/10.1109/ASRU.2005.1566521). Prior; deciding prior for M03 and M12. [wiki: doi-10.1109-asru.2005.1566521](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-asru.2005.1566521/article.md)
6. <a id="ref-6"></a>Tang, C., Mallah, J., Kazieczko, D., Yi, W., Kandukuri, T. R., Occhipinti, E., et al. “Wireless Silent Speech Interface Using Multi-Channel Textile EMG Sensors Integrated into Headphones.” *IEEE Transactions on Instrumentation and Measurement*, 2025. doi:[10.1109/TIM.2025.3583386](https://doi.org/10.1109/TIM.2025.3583386). arXiv:[2504.13921](https://arxiv.org/abs/2504.13921). Prior; deciding prior for M05 and M13. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/wireless-silent-speech-interface-using-multi-channel-textile-emg-sensors-integrated-into-headpho) [wiki: arxiv-2504.13921](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2504.13921/article.md) [wiki: doi-10.1109-tim.2025.3583386](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tim.2025.3583386/article.md)
7. <a id="ref-7"></a>Xu, X., Dong, M., Yan, Y., Wang, C., Jiao, Y., Chen, J. “AESSI: An Around-Ear Silent Speech Interface for Cross-Day Online Reuse without Test-Day Calibration.” *arXiv preprint*, 2026. doi:[10.48550/arXiv.2609.21436](https://doi.org/10.48550/arXiv.2609.21436). arXiv:[2609.21436](https://arxiv.org/abs/2609.21436). State of the art for M03. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/aessi-an-around-ear-silent-speech-interface-for-cross-day-online-reuse-without-test-day-calibrat) [wiki: arxiv-2609.21436](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2609.21436/article.md)
8. <a id="ref-8"></a>Lin, Y., Yu, S., Liu, L., Wang, H., Wang, Y., Jiang, M., et al. “An in-sensor communication electronic textile for imperceptible and ultrarobust silent speech communication.” *Nature Communications*, 2026. doi:[10.1038/s41467-026-74035-7](https://doi.org/10.1038/s41467-026-74035-7). State of the art for M05 (radio-frequency phase sensing, not sEMG). The .bib lists the first twelve authors. [concurrent] [wiki: pmc-13396449-insensortextile](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13396449-insensortextile/article.md) [wiki: pmc-13396449-etextile](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13396449-etextile/article.md)
9. <a id="ref-9"></a>Hong, S., Yoo, J., Park, S. “Soft Multiaxial Strain Mapping Interface with AI-Driven Decoding for Silent Speech in Noise.” *Cyborg and Bionic Systems*, 2026. doi:[10.34133/cbsystems.0536](https://doi.org/10.34133/cbsystems.0536). State of the art for M12. [concurrent] [wiki: pmc-13006734-cvos-ssi](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13006734-cvos-ssi/article.md) [wiki: doi-10.34133-cbsystems.0536](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.34133-cbsystems.0536/article.md)
