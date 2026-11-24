# Knowledge Distilled Ensemble Model for sEMG-based Silent Speech Interface

Wenqiang Lai, Qihan Yang, Ye Mao, Endong Sun, Jiangnan Ye. arXiv preprint, 2023. [arXiv:2308.06533](https://arxiv.org/abs/2308.06533)

## Verdict

KDE-SSI [[1]](#ref-1) changes three components: a soft-voting ResNet1D ensemble supplies soft targets for a student (M02), the deployed decoder is that single student (M06), and its time and size are reported (M13). All three are standard: same-modality distillation of word classifiers was published for lip reading three years earlier [[2]](#ref-2). The headline "7.0× smaller, 20.8× faster" compares the student with six models on a GPU (Fig. 5), so most of it follows from N = 6. The comparison that matters, the student against one ResNet1D (85.9% vs 81.2%, Table II), comes from one unseeded split whose grouping unit is not stated (§IV.E), with no student trained without a teacher. So 85.9% is not comparable with the later subject-independent 85.8% on the same words [[3]](#ref-3), and the deployment claim (§V.B) has no device measurement.

## Against the field, component by component

### M02 Training-only supervision: ensemble teacher

**Usual approach:** of 131 studies mentioning distillation, the teacher is most often audio, ASR or cross-modal (46); compression to a smaller student appears in 20 and an ensemble teacher in 2, one being the target (pattern match, unique studies, Appendix).

**State of the art:** Ma et al. [[2]](#ref-2) (prior, 2020) lifted a lip-reading classifier from 85.3% (teacher) to 87.9% with a same-architecture student on LRW, 500 words (Table 1), and list each efficient student with and without distillation, e.g. 84.4% and 85.3% at 9.3 M parameters (Table 3).

KDE-SSI lacks that control (Tables II–III), so its 4.7-point gain over ResNet1D (inference) may come from architecture, soft targets or split noise. Verdict: standard.

### M06 Decoder: ensemble, then one student

**Usual approach:** among 360 closed-vocabulary word-classification studies (pattern match, unique studies, Appendix), CNNs (35) and HMMs (25) are the most frequent named decoder families (slot-filled); e.g. 82.9% on 32 sEMG words with word HMMs [[4]](#ref-4).

**State of the art:** on the same 26 NATO words, CVOS [[3]](#ref-3) ([later], 2026) reports 85.8% from a neck strain sensor.

The N sweep is not monotonic: N = 4 gives the best teacher (88.0%) and the worst student (83.2% at T = 5, Table III). Without seeds, one-point row differences are not evidence. Verdict: standard.

### M13 Operating constraints: time and size

**Usual approach:** 24 of 30 wearable studies whose ledgers mention embedded processing decode off the body with no latency, energy or power figure (pattern match, Appendix). KDE-SSI reports time and size, but on a Tesla P100 (§IV.E).

**State of the art:** SilentWear [[5]](#ref-5) ([later], 2026) runs a 15k-parameter CNN on a microcontroller at 2.47 ms and 63.9 µJ per inference, 20.5 mW in total; CVOS [[3]](#ref-3) ([later]) shrinks its 26-word model from 12.4 MB to 3.6 MB at a cost of 85.8% to 82%.

The ensemble's 147.9 MB over six estimators is about 24.7 MB each (inference), close to the student's 21.1 MB, so the student is roughly one backbone. sEMG recognition already ran on Android in 2013 [[6]](#ref-6). Verdict: standard.

### M05 Sensors: three facial channels

**Usual approach:** 8 and 4 channels are the most frequent counts among 17 facial-EMG layout studies (2 each, slot-filled, Appendix); KDE-SSI uses three channels on LAO, DAO and ZM (§II.A) without a placement comparison.

**State of the art:** Zhu et al. [[7]](#ref-7) (prior, 2021) needed ten electrodes selected from 120 for 86% on ten English digits; four textile electrodes gave 96% on ten words under a random split [[8]](#ref-8) ([later], 2025).

The authors concede three muscles miss some words (§V.B); seven classes stay below F1 0.80 (Table IV). Verdict: standard.

### M12 Evaluation: test split

**Usual approach:** of 143 wearable-sensor word studies, 65 name a speaker-disjoint split, 58 a random or k-fold one (pattern match, mentions included, Appendix); sample splits are common, e.g. 80/20 per category [[9]](#ref-9).

**State of the art:** CVOS [[3]](#ref-3) ([later], 2026): 85.8% on the 26 NATO words, subject-independent stratified 5-fold.

KDE-SSI pools 3,900 samples from five male speakers 4:1:1 (§IV.E) without the grouping unit; with ten consecutive repetitions per trial (§II.C), a sample split puts near-duplicates on both sides (inference). Verdict: not reported.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Prompted silent mouthing of 26 NATO words | Recorded or prompted production (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Soft targets from a 6-ResNet1D ensemble, KL + CE | Audio or ASR teacher (pattern match 46) | [[2]](#ref-2) (2020): LRW 87.9% (teacher 85.3%) | standard |
| M03 Training and adaptation | Offline pooled training, no calibration | Training records (slot-filled 1,526) | – | standard |
| M04 Use-time action | Paced mouthing, 2 s per word | Silent or overt (slot-filled 5,595) | – | standard |
| M05 Sensors | 3 BITalino sEMG channels (LAO, DAO, ZM) | 8 or 4 channels (slot-filled 2) | [[8]](#ref-8) (2025): 96%, 10 words, 4 electrodes | standard |
| M06 Processing and decoding | Soft-voting ResNet1D ensemble, then one student | CNN or HMM classifier (slot-filled 35) | [[3]](#ref-3) (2026): 85.8%, 26 NATO words | standard |
| M07 Lexicon and LM | None | No lexicon for isolated words (slot-filled 119) | – | standard |
| M08 Output | One of 26 class labels | Class label or text (slot-filled 3,268) | – | standard |
| M09 Confirmation | None | Mostly absent (slot-filled 82) | – | not applicable |
| M10 Correction | None (fuzzy matching proposed) | Mostly absent (slot-filled 82) | – | not applicable |
| M11 Reference construction | Prompt identity as label, new dataset | Prompt labels (slot-filled 234) | – | standard |
| M12 Evaluation | 4:1:1 split of pooled samples, unit unstated | Speaker-disjoint split (pattern match 65) | [[3]](#ref-3) (2026): 85.8%, subject-independent | not reported |
| M13 Device and cost | GPU time 0.12 ms, 21.1 MB | Off-body, no latency or power (pattern match 24) | [[5]](#ref-5) (2026): 2.47 ms, 20.5 mW on MCU | standard |

## Where the claims outrun the evidence

- "Negligible accuracy reduction (0.1%)" (§V.A) is one pair on one split; N = 4 loses 4.8 points (Table III).
- Spelling any English word (Abstract) is untested: output is one of 26 classes; fuzzy matching is future work (§VI).

## What the field needs next

- M12: leave-one-speaker-out and leave-one-session-out results on the 26 NATO words, with female speakers.
- M02: the student without a teacher, over several seeds, as in [[2]](#ref-2).
- M13: latency and energy on a phone or microcontroller, as in [[5]](#ref-5).
- M08/M10: an end-to-end spelling test.

## Questions for the authors

- Which unit does the 4:1:1 split separate, with which seed? Per-speaker accuracies?
- What is the student architecture and parameter count, and its accuracy trained on labels alone?
- Which device, batch size and precision gave 2.50 ms and 0.12 ms?
- Are precision, recall and F1 macro- or micro-averaged?

## Appendix: literature search

- M02, knowledge-distillation-in-speech-decoding (new; replaces an EMG-only topic that matched only the target). Inclusion rule: speech, word or language decoding from any non-acoustic or audio-visual signal that trains a student on teacher outputs or representations, found by ledger text or full text; classified by teacher source and compression use; full-text counts include related-work mentions; acoustic-only ASR distillation out of scope. Ledger: 31 unique studies slot-filled for M02; 22 unique studies pattern match in ledger text, 131 unique studies with full text in scope. Designs: audio or ASR teacher 46, EMG or neural signal named 27, compression student 20, ensemble teacher 2 (pattern match). Read in full: [[2]](#ref-2). Known-item recall 1.0 (4 seeds).
- M06, closed-vocabulary-word-classification (published table, reused). Inclusion rule: words or utterances decoded from non-acoustic signals by classifying segments into a closed set of at most a few hundred items. Ledger: 7,345 unique studies slot-filled for M06; 360 unique studies pattern match. Decoder families: other 82, CNN 35, HMM 25 (slot-filled). Read in full: [[4]](#ref-4). Known-item recall 0.5.
- M13, wearable-speech-sensor-on-device-inference (published table, reused). Inclusion rule: non-acoustic speech wearables whose decoder runs on an embedded processor on or near the body; design compared: whether latency, energy per inference and system power are measured. Ledger: 6,075 unique studies slot-filled for M13; 30 unique studies pattern match. Usual design: off-body decoding with no such figure, 24 (pattern match). Read in full: [[5]](#ref-5), [[6]](#ref-6). Known-item recall 1.0.
- M05, facial-emg-channel-layout (new). Inclusion rule: facial surface-EMG silent-speech recognition studies that specify or compare electrode, channel or muscle placement against word-recognition performance. Ledger: 7,329 unique studies slot-filled for M05; 17 unique studies pattern match. Channel counts 8 and 4, 2 studies each (slot-filled). Read in full: [[7]](#ref-7), [[8]](#ref-8). Known-item recall 0.0.
- M12, wearable-sensor-word-test-split (published table, reused). Inclusion rule: word or command classification from wearable face or neck sensors, classified by how test samples are separated. Ledger: 6,960 unique studies slot-filled for M12; 143 unique studies pattern match. Speaker-disjoint 65, random or k-fold 58, session-disjoint 44 (pattern match). Read in full: [[3]](#ref-3), [[9]](#ref-9). Known-item recall 0.75.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Lai, W., Yang, Q., Mao, Y., Sun, E., Ye, J. “Knowledge Distilled Ensemble Model for sEMG-based Silent Speech Interface.” *arXiv preprint (submitted to the IEEE Region 8 Student Paper Contest 2023)*, 2023. doi:[10.48550/arXiv.2308.06533](https://doi.org/10.48550/arXiv.2308.06533). arXiv:[2308.06533](https://arxiv.org/abs/2308.06533). Target. Read as arXiv v1. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/knowledge-distilled-ensemble-model-for-semg-based-silent-speech-interface) [wiki: arxiv-2308.06533](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2308.06533/article.md)
2. <a id="ref-2"></a>Ma, P., Martinez, B., Petridis, S., Pantic, M. “Towards Practical Lipreading with Distilled and Efficient Models.” *2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2021, 7608-7612. doi:[10.1109/ICASSP39728.2021.9415063](https://doi.org/10.1109/ICASSP39728.2021.9415063). arXiv:[2007.06504](https://arxiv.org/abs/2007.06504). Prior; deciding prior for M02 and M13 (same-modality distillation into word classifiers, efficient students). [wiki: arxiv-2007.06504](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2007.06504/article.md)
3. <a id="ref-3"></a>Hong, S., Yoo, J., Park, S. “Soft Multiaxial Strain Mapping Interface with AI-Driven Decoding for Silent Speech in Noise.” *Cyborg and Bionic Systems*, 2026. doi:[10.34133/cbsystems.0536](https://doi.org/10.34133/cbsystems.0536). Later; state of the art for M12 (published table). [later] [wiki: pmc-13006734-cvos-ssi](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13006734-cvos-ssi/article.md) [wiki: pmc-13006734-strainssi](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13006734-strainssi/article.md) [wiki: doi-10.34133-cbsystems.0536](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.34133-cbsystems.0536/article.md)
4. <a id="ref-4"></a>Walliczek, M., Kraft, F., Jou, S., Schultz, T., Waibel, A. “Sub-Word Unit based Non-Audible Speech Recognition using Surface Electromyography.” *Interspeech 2006*, 2006. doi:[10.21437/Interspeech.2006-425](https://doi.org/10.21437/Interspeech.2006-425). Prior; cited by the target; M06 comparator (closed-vocabulary sEMG word recognition). [wiki: isca-walliczek06_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-walliczek06_interspeech/article.md)
5. <a id="ref-5"></a>Spacone, G., Frey, S., Pollo, G., Burrello, A., Jahier Pagliari, D., Kartsch, V., et al. “SilentWear: an Ultra-Low Power Wearable System for EMG-based Silent Speech Recognition.” *arXiv preprint*, 2026. doi:[10.48550/arXiv.2603.02847](https://doi.org/10.48550/arXiv.2603.02847). arXiv:[2603.02847](https://arxiv.org/abs/2603.02847). Later; state of the art for M13 (published table). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/silentwear-an-ultra-low-power-wearable-system-for-emg-based-silent-speech-recognition) [wiki: arxiv-2603.02847](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2603.02847/article.md)
6. <a id="ref-6"></a>Meltzner, G. S., Heaton, J. T., Deng, Y. “The MUTE Silent Speech Recognition System.” *Interspeech 2013*, 2013. <https://www.isca-archive.org/interspeech_2013/meltzner13_interspeech.html> Prior; M13 comparator (sEMG recognizer on a portable Android device). [wiki: isca-meltzner13-mute](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-meltzner13-mute/article.md)
7. <a id="ref-7"></a>Zhu, M., Zhang, H., Wang, X., Wang, X., Yang, Z., Wang, C., et al. “Towards optimizing electrode configurations for silent speech recognition based on high-density surface electromyography.” *Journal of Neural Engineering*, 2021, 18(1), 016005. doi:[10.1088/1741-2552/abca14](https://doi.org/10.1088/1741-2552/abca14). Prior; deciding prior for M05. [wiki: doi-10.1088-1741-2552-abca14](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552-abca14/article.md)
8. <a id="ref-8"></a>Tang, C., Mallah, J., Kazieczko, D., Yi, W., Kandukuri, T. R., Occhipinti, E., et al. “Wireless Silent Speech Interface Using Multi-Channel Textile EMG Sensors Integrated into Headphones.” *IEEE Transactions on Instrumentation and Measurement*, 2025. doi:[10.1109/TIM.2025.3583386](https://doi.org/10.1109/TIM.2025.3583386). arXiv:[2504.13921](https://arxiv.org/abs/2504.13921). Later; M05 comparator (four-electrode wearable, 10 words). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/wireless-silent-speech-interface-using-multi-channel-textile-emg-sensors-integrated-into-headpho) [wiki: arxiv-2504.13921](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2504.13921/article.md) [wiki: doi-10.1109-tim.2025.3583386](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tim.2025.3583386/article.md)
9. <a id="ref-9"></a>Lu, Y., Tian, H., Cheng, J., Zhu, F., Liu, B., Wei, S., et al. “Decoding lip language using triboelectric sensors with deep learning.” *Nature Communications*, 2022, 13, 1401. doi:[10.1038/s41467-022-29083-0](https://doi.org/10.1038/s41467-022-29083-0). Prior; M12 comparator (per-category sample split). [wiki: doi-10.1038-s41467-022-29083-0](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41467-022-29083-0/article.md)
