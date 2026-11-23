# Silent Speech Sentence Recognition with Six-Axis Accelerometers using Conformer and CTC Algorithm

Xie, Y., Han, Z., Xiao, Q., Liang, L., Tao, L.-Q., Ren, T.-L. · arXiv preprint · 2025 · [arXiv:2502.17829](https://arxiv.org/abs/2502.17829)

## Verdict

The paper [[1]](#ref-1) changes the decoder (M06, Conformer with CTC), the training data (M03, concatenated words plus noise) and the sensing (M05, six six-axis IMUs); all three are standard. CTC decoding of silently articulated phrases predates it, with 15 subjects [[2]](#ref-2), and the cited Luo et al. already trained CTC for silent sentences [[3]](#ref-3), so the claim that no prior SSI recognizes sentences dynamically (§1) fails. Liu et al. trained IMU decoders on concatenated sentences and tested on spoken ones [[4]](#ref-4); this paper does not say whether its length curve (Fig. 3a) scores recorded or concatenated sequences. The headline 97.17% is a word ratio on 4 participants with an unstated split.

## Against the field, component by component

### M06 Sentence decoder: Conformer with CTC

**Usual approach:** Of 54 silent sentence-recognition studies with body-worn or contact sensors (pattern match, Appendix), 30 name HMM decoding, 16 CTC and 9 attention sequence-to-sequence decoders. The paper takes the CTC route plus a cross-entropy loss (§2.3).

**State of the art:** Chen et al. (2023): CTC syllable decoding from four 64-channel HD-sEMG arrays, 33 Chinese phrases, 15 subjects, phrase accuracy 97.17 ± 1.53%, character error rate 3.11 ± 1.46% [[2]](#ref-2). The target matches the accuracy on 4 participants, with a word-ratio metric.

Luo et al. trained CTC against attention for 54 silent sentences (§4.4) and report 8.1% WER on unseen sentences [[3]](#ref-3). The target trains a single decoder (§3.2), states no CTC search or language model (§2.3.1) and tests no held-out word combination. Verdict: standard.

### M03 Training data: concatenated words plus noise

**Usual approach:** In the same 54 studies (pattern match, Appendix), 17 name time masking or warping and 4 match word-concatenation synthesis, one of which uses it [[4]](#ref-4). The target adds tenfold concatenation and Gaussian noise (§2.1.2).

**State of the art:** Liu et al. (2024): trained only on sentences concatenated from segmented words, 92.0% on 93 spoken fluent sentences (n = 7), 96.4% with individual segmentation parameters, 25.1% without segmentation [[4]](#ref-4).

The target describes no segmentation; dropping it cost Liu et al. 66.9 points, 73% relative (inference). A [later] study shows that concatenation misses coarticulation [[5]](#ref-5). Lengths up to 19 exceed every recorded item in Table 1, so the curve most likely scores concatenations (inference); Liu et al. are not cited. Verdict: standard.

### M05 Sensors: six six-axis IMUs, channel and axis ablation

**Usual approach:** Of 20 inertial silent-speech studies (pattern match, Appendix, mostly reviews), 14 name a sensor-count comparison and 9 a gyroscope. The accelerometer lineage uses acceleration only [[6]](#ref-6); Liu et al. add gyroscopes and a head reference IMU [[4]](#ref-4). The target records both at 50 Hz on the face (Fig. 1).

**State of the art:** Choi et al. (2026, [later]): all combinations of ten accelerometers, 100 silent words, 20 participants, subject-dependent; plateau at five sensors, 92.30 ± 4.64% [[6]](#ref-6).

The target's channel result (§3.4) agrees but rests on 4 participants. Its useful result is Fig. 4(c): single gyroscope axes 92.39–93.39% against accelerometer axes 87.62–92.42%, which argues against discarding the gyroscope; motion is handled only by a 2 Hz high-pass filter (§2.2) and never tested. Verdict: standard.

### M12 Evaluation: split and metric

**Usual approach:** Of 143 wearable-sensor word-classification studies (pattern match, published counts), 65 name a speaker-disjoint test, 58 a random split and 44 a session-disjoint test. The target gives a 70:15:15 split without unit or speaker overlap (§2.1.2) and blind scores only in Fig. 3(b).

**State of the art:** Hong et al. (2026, [later]): 85.8% for 26 words, subject-independent 5-fold cross-validation, plus re-attachment after two weeks [[7]](#ref-7).

Accuracy counts correct words (§3.1), not exact sentences. Sessions are not reported, though electrode repositioning alone cut EMG accuracy to 76.2% [[8]](#ref-8). No chance level is given. Verdict: not reported.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Prompted silent repetitions | Prompted recording (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Text labels, CTC + CE | Text or phoneme labels (slot-filled 31) | – | standard |
| M03 Training and adaptation | Word concatenation, noise | Time masking or warping (pattern match 17) | [[4]](#ref-4) (2024): 92.0% on spoken sentences | standard |
| M04 Use-time action | Silent articulation | Silent or overt (slot-filled 5,595) | – | standard |
| M05 Sensors | 6 IMUs, accel + gyro | Sensor-count comparison (pattern match 14) | [[6]](#ref-6) (2026): 92.30%, 5 sensors | standard |
| M06 Processing and decoding | Conformer + CTC | HMM decoding (pattern match 30) | [[2]](#ref-2) (2023): 97.17%, CER 3.11% | standard |
| M07 Lexicon and LM | Not stated | Lexicon or LM (slot-filled 119) | – | not reported |
| M08 Output | Word-sequence text | Text or labels (slot-filled 3,268) | – | standard |
| M09 Confirmation | Offline | Offline (slot-filled 82) | – | not applicable |
| M10 Correction | Offline | Offline (slot-filled 82) | – | not applicable |
| M11 Reference construction | Fixed prompt list | Prompt text (slot-filled 234) | – | standard |
| M12 Evaluation | 70:15:15, unit unstated | Speaker-disjoint test (pattern match 65) | [[7]](#ref-7) (2026): 85.8%, subject-independent | not reported |
| M13 Device and cost | Portability claimed | Device constraints (slot-filled 6,075) | – | not reported |

## Where the claims outrun the evidence

- The novelty claim of §1 fails against the M06 priors (Appendix).
- "Arbitrary silent sentences" (§4) rests on 16 words, two sentences and eight phrases (Table 1); the authors concede the small dataset (§4).
- 97.17% "at both word and sentence levels" (§5) against 97.24% and 97.16% (§3.1).
- "CTC decoding effectively mitigates the impact of sentence length" (§3.2) has no non-CTC control.
- Inputs are 36 × window (§2.2), the first block takes 30 channels (§2.3.1).
- Daily-use "portability" (§5) with one laryngectomized participant and no wear-time or latency measure.

## What the field needs next

- M03: train on concatenated words, test on articulated held-out sequences with WER [[3]](#ref-3).
- M05: gyroscope against accelerometer axes, with a head reference, under movement and re-attachment.
- M06: CTC, attention and whole-sentence classification on the same split.
- M12: speaker- and session-disjoint tests with exact blind scores and chance level.

## Questions for the authors

- Is the 70:15:15 split by sample, session or participant?
- Are the Fig. 3(a) sequences recorded or concatenated?
- How many few-shot samples are used, and are they disjoint from test data?
- Greedy or beam CTC decoding; any lexicon or language model?
- Why 30 input channels for 36 × window samples?
- What does the laryngectomized participant score?

## Appendix: literature search

- M06, wearable-silent-sentence-decoding (new). Inclusion rule: sentence or phrase recognition from silently articulated speech measured by body-worn or contact non-video sensors (EMG, inertial, strain, triboelectric, magnetic, EMA, ultrasound, active acoustic), classified by decoder: whole-sentence classification, HMM, CTC or attention sequence-to-sequence; lip video, imagined, overt-only and synthesis-only studies excluded; a study counts under every decoder its full text names (upper bound). Ledger: 7,345 unique studies slot-filled for M06; 54 unique studies pattern match. HMM 30, CTC 16, attention sequence-to-sequence 9, word-concatenation synthesis 4, whole-sentence classification 1 (pattern match). Read in full: [[2]](#ref-2), [[3]](#ref-3), [[4]](#ref-4). Known-item recall 1.0 (5 seeds).
- M03, word-concatenation-sentence-training-data (new). Inclusion rule: the same 54 studies, classified by how sentence training data are obtained or enlarged (concatenated word recordings, additive noise, time masking or warping; every named design counts). Ledger: 1,526 unique studies slot-filled for M03; 54 unique studies pattern match. Time masking or warping 17, word-concatenation synthesis 4 (one study using it, one [later] study rejecting it, one false hit), additive noise 3 (pattern match). Read in full: [[4]](#ref-4), [[5]](#ref-5). Known-item recall 1.0 (3 seeds).
- M05, wearable-inertial-silent-speech-sensing (new). Inclusion rule: silent-speech studies naming wearable accelerometers, gyroscopes or IMUs on the face, jaw or neck, classified by inertial quantity and by whether sensor count, subsets or axes are compared; vibration pickups for voiced speech, EMA without inertial sensors and gesture IMUs excluded. Ledger: 7,329 unique studies slot-filled for M05; 13 unique studies pattern match in the ledger plus 8 full-text-only records, 20 unique studies. Sensor-count or subset comparison 14, gyroscope 9, axis comparison 4 (the target and three records of [[4]](#ref-4), where it is a calibration test) (pattern match). Read in full: [[6]](#ref-6), [[4]](#ref-4). Known-item recall 1.0 (3 seeds).
- M12, wearable-sensor-word-test-split (published table, reused). Inclusion rule: word or command classification with a wearable non-acoustic face or neck sensor, classified by how test samples are separated from training samples. Ledger: 6,960 unique studies slot-filled for M12; 143 unique studies pattern match. Speaker-disjoint 65, random or k-fold 58, session- or day-disjoint 44 (pattern match, published counts). Read in full: [[7]](#ref-7), [[8]](#ref-8).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Xie, Y., Han, Z., Xiao, Q., Liang, L., Tao, L., Ren, T. “Silent Speech Sentence Recognition with Six-Axis Accelerometers using Conformer and CTC Algorithm.” *arXiv preprint*, 2025. doi:[10.48550/arXiv.2502.17829](https://doi.org/10.48550/arXiv.2502.17829). arXiv:[2502.17829](https://arxiv.org/abs/2502.17829). Target. Read as arXiv v3. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/silent-speech-sentence-recognition-with-six-axis-accelerometers-using-conformer-and-ctc-algorith) [wiki: arxiv-2502.17829](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2502.17829/article.md)
2. <a id="ref-2"></a>Chen, X., Zhang, X., Chen, X., Chen, X. “Decoding Silent Speech Based on High-Density Surface Electromyogram Using Spatiotemporal Neural Network.” *IEEE Transactions on Neural Systems and Rehabilitation Engineering*, 2023, 31. doi:[10.1109/TNSRE.2023.3266299](https://doi.org/10.1109/TNSRE.2023.3266299). Prior; state of the art and deciding prior for M06 (CTC decoding of silent phrases). [wiki: tnsre-3266299-hdsemg](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/tnsre-3266299-hdsemg/article.md) [wiki: doi-10.1109-tnsre.2023.3266299](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tnsre.2023.3266299/article.md)
3. <a id="ref-3"></a>Luo, J., Wang, J., Cheng, N., Jiang, G., Xiao, J. “End-to-end Silent Speech Recognition with Acoustic Sensing.” *arXiv preprint*, 2020. arXiv:[2011.11315](https://arxiv.org/abs/2011.11315). Prior; cited by the target; deciding prior for M06 (CTC compared for silent sentences). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/end-to-end-silent-speech-recognition-with-acoustic-sensing) [wiki: arxiv-2011.11315](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2011.11315/article.md)
4. <a id="ref-4"></a>Liu, S., Fawden, T., Zhu, R., Malliaras, G. G., Bance, M. “A data-efficient and easy-to-use lip language interface based on wearable motion capture and speech movement reconstruction.” *Science Advances*, 2024, 10(26), eado9576. doi:[10.1126/sciadv.ado9576](https://doi.org/10.1126/sciadv.ado9576). Prior; state of the art for M03, deciding prior for M05 and M06; not cited by the target. [wiki: pmc-11204283-liplang-wearable](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11204283-liplang-wearable/article.md) [wiki: doi-10.1126-sciadv.ado9576](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1126-sciadv.ado9576/article.md) [wiki: pmc-11204283-lip-mocap](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11204283-lip-mocap/article.md) [wiki: pmc-11204283-wearlip](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11204283-wearlip/article.md) [wiki: pmc-11204283-wearlipiface](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11204283-wearlipiface/article.md)
5. <a id="ref-5"></a>Satterlee, N., Zuo, X., Moon, K., Lee, S. Q., Peterson, M., Kang, J. S. “Sentence-Level Silent Speech Recognition Using a Wearable EMG/EEG Sensor System with AI-Driven Sensor Fusion and Language Model.” *Sensors*, 2025, 25(19), 6168. doi:[10.3390/s25196168](https://doi.org/10.3390/s25196168). Later work; shows that concatenated word signals do not reproduce sentence signals (M03). [later] [wiki: doi-10.3390-s25196168](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3390-s25196168/article.md) [wiki: pmc-12526642-emg-eeg-ssi](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12526642-emg-eeg-ssi/article.md) [wiki: pmc-12526642-emgeeg-snn](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12526642-emgeeg-snn/article.md)
6. <a id="ref-6"></a>Choi, H., Jung, S., Sohn, J., Im, C. “Efficient Sensor Configuration for Accelerometer-based Silent Speech Interfaces: Regionally Distributed Sensor Placement Strategy Considering Articulatory Dynamics.” *Research Square preprint*, 2026. doi:[10.21203/rs.3.rs-10442598/v1](https://doi.org/10.21203/rs.3.rs-10442598/v1). Later work; state of the art for M05. [later] [wiki: rs-10442598-accssi](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/rs-10442598-accssi/article.md)
7. <a id="ref-7"></a>Hong, S., Yoo, J., Park, S. “Soft Multiaxial Strain Mapping Interface with AI-Driven Decoding for Silent Speech in Noise.” *Cyborg and Bionic Systems*, 2026. doi:[10.34133/cbsystems.0536](https://doi.org/10.34133/cbsystems.0536). Later work; state of the art for M12 (published table). [later] [wiki: pmc-13006734-cvos-ssi](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13006734-cvos-ssi/article.md) [wiki: doi-10.34133-cbsystems.0536](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.34133-cbsystems.0536/article.md)
8. <a id="ref-8"></a>Maier-Hein, L., Metze, F., Schultz, T., Waibel, A. “Session Independent Non-Audible Speech Recognition Using Surface Electromyography.” *Proc. IEEE ASRU 2005*, 2005. doi:[10.1109/ASRU.2005.1566521](https://doi.org/10.1109/ASRU.2005.1566521). Prior; session effect for M12 (published table). [wiki: doi-10.1109-asru.2005.1566521](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-asru.2005.1566521/article.md)
