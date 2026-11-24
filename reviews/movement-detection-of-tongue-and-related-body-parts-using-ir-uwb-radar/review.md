# Movement Detection of Tongue and Related Body Parts Using IR-UWB Radar

Sunghwa Lee, Younghoon Shin. arXiv preprint, 2022. [arXiv](https://arxiv.org/abs/2209.01762)

## Verdict

The paper [[1]](#ref-1) changes radar placement (M05, chin, not mouth) and the front end (M06, an RMS envelope into Gaussian HMMs); both are standard, because neither departure is backed by a controlled comparison. A contactless chin-facing radar appears in 2 of 33 radar studies (Appendix), is never compared here with a mouth-facing one, and lost to the lips in the authors' [later] two-radar study, 70.59% against 86.47% on vowels, with the chin radar farther away there (10–15 cm) [[2]](#ref-2). The envelope beats the 2016 CLEAN features [[3]](#ref-3) for all four participants (Table I), but feature and classifier change together. The task separates rest from palate touch, and the authors concede that throat muscles move with the tongue (§IV): what is shown is closed-mouth movement, not tongue movement. Evaluation (M12) is within-participant leave-one-out on 40 trials for each of 4 participants, one an author (§II-A), the default.

## Against the field, component by component

### M05 Sensors: radar aimed at the chin

**Usual approach:** In the 33 radar or RF studies (pattern match), the recorded sensor values are mostly external non-contact (12) with the face as body site (11) (slot-filled); the 2016 predecessor aimed at lips and jaw from 10–16 cm [[3]](#ref-3), this paper at the chin from 5–10 cm (§II-A).

**State of the art:** [later] (2023) the same group recorded a lip-facing radar at 5–10 cm and a chin-facing one at 10–15 cm together; over 20 participants the lip radar won with every method and task, 86.47% against 70.59% on vowels with FERASEC + DNN–HMM [[2]](#ref-2).

Of 6 studies whose text places a sensor toward or under the chin (pattern match, Appendix), only this paper and its successor aim a contactless radar there; the other 4 describe contact antennas or ultrasound probes below the chin. Its value is untested: the paper argues that skin and teeth weaken tongue echoes for a mouth-facing radar (§I) but records no mouth-facing condition. The successor finds the chin loses lip information and the lips suffer tooth occlusion [[2]](#ref-2): complementary, not better. Verdict: standard.

### M06 Processing: envelope features into GMM–HMMs

**Usual approach:** Engineered features into a classical classifier (21 of 32 radar studies, pattern match, upper bound); the lineage is two CLEAN features, distance and reflection strength, into MD-DTW [[3]](#ref-3). The paper replaces them with one RMS envelope (400-sample window) into two five-state HMMs with one Gaussian per state (§II-B).

**State of the art:** the best learned IR-UWB front end, a [later] (2025) temporal convolutional network on the testbed of [[2]](#ref-2), reaches 91.1% on 50 words against 74.0% for hand-crafted features + DNN–HMM, one participant, leave-one-session-out [[4]](#ref-4).

Table I gives 100, 90, 90 and 90% against 85, 65, 80 and 70% for short-template CLEAN + MD-DTW: mean error falls from 25% to 7.5%, 70% relative (inference). Four of four improving gives a one-sided sign-test p of 0.0625 (inference). Table I never crosses features with classifiers; short-template CLEAN keeps only the nearest echo [[3]](#ref-3), which under the chin is skin that barely moves with the mouth closed (inference). With MD-DTW fixed, the [later] envelope-based FERASEC lifts chin-radar vowels from 40.88% (short-template CLEAN) to 66.91% [[2]](#ref-2). Verdict: standard.

### M12 Evaluation: within-participant leave-one-out

**Usual approach:** Speaker-dependent testing (22 of 32 radar studies, pattern match, against 17 speaker-independent, upper bounds), as in the per-speaker cross-validation of [[3]](#ref-3); here each of 40 frame sets is tested against models trained on the other 39 (§III).

**State of the art:** [later] (2026) contactless Wi-Fi backscatter tests three users absent from training at 81.5% to 85.5% word accuracy, on open-vocabulary sentences, not a binary task [[5]](#ref-5).

Pooled, 148 of 160 trials are correct, about 87–96% against 50% chance, ignoring clustering (inference). The 100% participant, P1, is an author (§IV). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | 20 instructed repetitions per state | Prompted repetition; slot total (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Instructed state labels, no audio | Prompt labels; slot total (slot-filled 31) | – | standard |
| M03 Training and adaptation | Per-participant models | Speaker-dependent training; slot total (slot-filled 1,526) | – | standard |
| M04 Use-time action | Closed mouth, rest or palate touch | Silent articulation; slot total (slot-filled 5,595) | – | standard |
| M05 Sensors | One IR-UWB radar aimed at the chin | Contactless radar at face or mouth (slot-filled 12) | Lip-facing beats chin-facing, 86.47% vs 70.59% vowels [[2]](#ref-2) [later] | standard |
| M06 Processing and decoding | RMS envelope + class-wise GMM-HMMs | Engineered features (pattern match 21) | 91.1% on 50 words, one participant [[4]](#ref-4) [later] | standard |
| M07 Lexicon and LM | None | No lexicon or LM; slot total (slot-filled 119) | – | not applicable |
| M08 Output | Two state labels | Closed-set labels; slot total (slot-filled 3,268) | – | standard |
| M09 Confirmation | None | Mostly absent; slot total (slot-filled 82) | – | not applicable |
| M10 Correction | None | Mostly absent; slot total (slot-filled 82) | – | not applicable |
| M11 Reference construction | Instructed state | Prompted labels; slot total (slot-filled 234) | – | standard |
| M12 Evaluation | Within-participant leave-one-out | Speaker-dependent (pattern match 22) | New users 81.5-85.5% words [[5]](#ref-5) [later] | standard |
| M13 Device and cost | Bench setup | Device constraints; slot total (slot-filled 6,075) | – | not applicable |

## Where the claims outrun the evidence

- "IR-UWB radar has the capability to detect the movement of invisible tongue" (§V) rests on a moving-versus-still contrast. The authors say throat muscles moved with the tongue (§IV), and no ultrasound, articulograph or palatograph reference shows what the envelope tracks; head motion would also raise it (inference).
- The 2016 pipeline already detected motion from the variance of frame-to-frame amplitude change [[3]](#ref-3), yet no such motion detector is a baseline for this rest-versus-movement task (Table I).
- Trials were opened and closed by a GUI click and last 1–3 s "regardless of the state" (§II-A). Per-state durations are not shown, so a duration cue in the HMM likelihoods remains possible (inference).

## What the field needs next

- M05: chin- and mouth-facing radars with matched antenna and distance, on tongue contrasts (/t/ against /k/).
- M11: a simultaneous ultrasound tongue reference.
- M06: crossed baselines (envelope with DTW, CLEAN with HMM) and a variance motion detector.
- M12: held-out, non-author participants with chance and intervals.

## Questions for the authors

- What were the per-state durations?
- What accuracy does a model trained on three participants reach on the fourth?

## Appendix: literature search

**M05, rf-articulator-sensing-placement.** Inclusion rule: speech or silent-speech recognition studies that sense the articulators with radar or other RF signals (IR-UWB, FMCW/SFCW, mmWave, RFID, backscatter, Wi-Fi channel sensing); compared design is the RF front end and where it points; Wi-Fi used only as a data link is excluded; datasets and surveys count; related-work mentions are inside the upper bound. Ledger counts: slot-filled 7,329 unique studies; pattern match 33 unique studies. Usual design: radar modality 21 (slot-filled); external non-contact 12 (slot-filled); face as body site 11 (slot-filled). Full-text placement patterns over the 33 studies: toward or under the chin 6, of which contactless radar 2 (snippets read; the other 4 are contact antennas or ultrasound probes); contact antenna on the face 6; toward the mouth, lips or face 5 (pattern match). Known-item recall 0.75. Read in full: [[2]](#ref-2), [[3]](#ref-3).

**M06, radar-ssr-input-representation.** Inclusion rule: the same radar population; compared design is the classifier input, engineered features versus raw frames or spectrograms into a learned network; throat-vibration speech recovery and datasets without a recognizer are excluded; versions count once. Ledger counts: slot-filled 7,345 unique studies; pattern match 32 unique studies. Usual design: engineered features 21 (pattern match, upper bound). Known-item recall 1.0. Read in full: [[4]](#ref-4), [[2]](#ref-2), [[3]](#ref-3).

**M12, radar-ssr-speaker-split.** Inclusion rule: the same radar population; compared design is whether test speakers are held out or models are trained and tested within one speaker; a paper counts under every split it reports. Ledger counts: slot-filled 6,960 unique studies; pattern match 32 unique studies. Usual design: speaker-dependent 22 (pattern match); speaker-independent 17 (pattern match, upper bound). Known-item recall 1.0. Read in full: [[5]](#ref-5), [[3]](#ref-3).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Lee, S., Shin, Y. “Movement Detection of Tongue and Related Body Parts Using IR-UWB Radar.” *arXiv preprint*, 2022. arXiv:[2209.01762](https://arxiv.org/abs/2209.01762). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/movement-detection-of-tongue-and-related-body-parts-using-ir-uwb-radar) [wiki: arxiv-2209.01762](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2209.01762/article.md)
2. <a id="ref-2"></a>Lee, S., Shin, Y., Kim, M., Seo, J. “IR-UWB Radar-Based Contactless Silent Speech Recognition of Vowels, Consonants, Words, and Phrases.” *IEEE Access*, 2023. doi:[10.1109/ACCESS.2023.3344177](https://doi.org/10.1109/ACCESS.2023.3344177). arXiv:[2312.09572](https://arxiv.org/abs/2312.09572). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/ir-uwb-radar-based-contactless-silent-speech-recognition-of-vowels-consonants-words-and-phrases) [wiki: arxiv-2312.09572](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2312.09572/article.md) [wiki: doi-10.1109-access.2023.3344177](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-access.2023.3344177/article.md)
3. <a id="ref-3"></a>Shin, Y. H., Seo, J. “Towards Contactless Silent Speech Recognition Based on Detection of Active and Visible Articulators Using IR-UWB Radar.” *Sensors*, 2016, 16(11), 1812. doi:[10.3390/s16111812](https://doi.org/10.3390/s16111812). [wiki: doi-10.3390-s16111812](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3390-s16111812/article.md) [wiki: pmc-5134471-iruwb](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-5134471-iruwb/article.md)
4. <a id="ref-4"></a>Lee, S., Yu, J. “IR-UWB Radar-Based Contactless Silent Speech Recognition with Attention-Enhanced Temporal Convolutional Networks.” *IEEE International Conference on Consumer Electronics-Asia (ICCE-Asia)*, 2025. doi:[10.1109/ICCE-Asia67487.2025.11263683](https://doi.org/10.1109/ICCE-Asia67487.2025.11263683). arXiv:[2509.26409](https://arxiv.org/abs/2509.26409). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/ir-uwb-radar-based-contactless-silent-speech-recognition-with-attention-enhanced-temporal-convol) [wiki: arxiv-2509.26409](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2509.26409/article.md)
5. <a id="ref-5"></a>Tian, Y., Du, H., Gu, C., Zhang, J., Wang, S., Zhou, H., et al. “Lip-Siri: Contactless Open-Sentence Silent Speech with Wi-Fi Backscatter.” *arXiv preprint*, 2026. arXiv:[2601.18177](https://arxiv.org/abs/2601.18177). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lip-siri-contactless-open-sentence-silent-speech-with-wi-fi-backscatter) [wiki: arxiv-2601-18177-lipsiri](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2601-18177-lipsiri/article.md)
