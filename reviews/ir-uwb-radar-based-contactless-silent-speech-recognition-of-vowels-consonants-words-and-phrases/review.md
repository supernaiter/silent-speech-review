# IR-UWB Radar-Based Contactless Silent Speech Recognition of Vowels, Consonants, Words, and Phrases

Sunghwa Lee, Younghoon Shin, Myungjong Kim, Jiwon Seo. IEEE Access, 2023. [DOI](https://doi.org/10.1109/ACCESS.2023.3344177) · [arXiv](https://arxiv.org/abs/2312.09572)

## Verdict

The paper changes one component, the radar feature front end (M06), and it is standard: engineered features into a sequence classifier is the usual radar design, and the gain over the authors' 2016 features is large and repeated over 20 participants [[1]](#ref-1), [[2]](#ref-2). Its conclusion that raw frames do not work is unsupported, since raw frames were tested only as DNN–HMM input (Table 3); the first author's [later] convolutional network on minimally processed frames from the same testbed beats hand-crafted features + DNN–HMM, 91.1% to 74.0%, on one participant and 50 words [[3]](#ref-3). The "first phoneme-level contactless radar SSR" claim holds only as consonant-syllable classification: silent vowel classification with contactless IR-UWB radar was reported in 2016 [[2]](#ref-2). Evaluation (M12) is within-speaker leave-one-out without seeds or spread, the field's default and unlike [later] RF work tested on unseen users [[4]](#ref-4). The lip-versus-chin result confounds position with antenna and distance; phone or watch use (M13) is asserted, not measured.

## Against the field, component by component

### M06 Processing: radar input representation

**Usual approach:** Hand-engineered features are the default in radar speech recognition (21 of 32 unique studies, pattern match, an upper bound); the 2016 IR-UWB baseline fed two CLEAN features to MD-DTW template matching [[2]](#ref-2). FERASEC stays in that design, replacing them with six envelope and derivative features.

**State of the art:** [later] (2025) a temporal convolutional network on minimally processed frames from the target's testbed reaches 91.1% on 50 words against 74.0% for hand-crafted features + DNN–HMM, with fold spread falling from 10.3 to 3.3 points, on one participant [[3]](#ref-3).

The feature effect is well supported: with MD-DTW and the upper radar, FERASEC lifts vowels from 51.59% to 80.56% and consonants from 42.68% to 74.50% (Table 2), 29.0 and 31.8 points, or 56% and 75% relative from a low base (inference). The old features were run only with MD-DTW, so no row isolates the feature gain under the DNN–HMM. The DNN–HMM adds 5.91 points on vowels and 7.09 on consonants and loses on phrases, 96.88% against 98.02% (Table 2) (inference). The argument against learning rests on Table 3, a DNN–HMM on raw or clutter-reduced frames at 44.38% and 48.13% for vowels; a frame-wise network on 256-dimensional frames is a weak test of learned representations, and the [later] result contradicts the conclusion on the same testbed, if only for one participant [[3]](#ref-3). Verdict: standard.

### M12 Evaluation: speaker split and uncertainty

**Usual approach:** Speaker-dependent testing is the usual radar design (22 of 32 unique studies, pattern match, against an overlapping 17 speaker-independent, upper bound), as in the per-speaker jackknife of the 2016 baseline [[2]](#ref-2); the paper follows it with per-participant leave-one-out over 20 repetitions (§IV-C).

**State of the art:** [later] (2026) contactless Wi-Fi backscatter work tests three users absent from training at 81.5% to 85.5% word accuracy and 36.3% to 39.6% sentence WER [[4]](#ref-4).

Table 2 gives means with no spread, seeds or chance level. Words and phrases use only the 4 native English speakers (Table 2 caption), so the 88.95% word and 96.88% phrase figures rest on 4 people. Every test item comes from a speaker whose other repetitions trained the model, so the numbers measure within-speaker repeatability. Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | 20 prompted silent repetitions | Prompted repetition; slot total (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Prompt labels, no audio | Prompt labels; slot total (slot-filled 31) | – | standard |
| M03 Training and adaptation | Per-participant models | Speaker-dependent training; slot total (slot-filled 1,526) | – | standard |
| M04 Use-time action | Silent, fixed head | Silent articulation; slot total (slot-filled 5,595) | – | standard |
| M05 Sensors | Two IR-UWB radars, lips and chin | Radar or RF sensing, topic population (pattern match 32) | – | standard |
| M06 Processing and decoding | FERASEC + MD-DTW or DNN-HMM | Engineered features (pattern match 21) | 91.1% on 50 words, one participant [[3]](#ref-3) [later] | standard |
| M07 Lexicon and LM | None | No lexicon or LM; slot total (slot-filled 119) | – | not applicable |
| M08 Output | Vowel and consonant syllables, words, phrases | Closed-set labels; slot total (slot-filled 3,268) | Open-vocabulary sentences [[4]](#ref-4) [later] | standard |
| M09 Confirmation | None | Mostly absent; slot total (slot-filled 82) | – | not applicable |
| M10 Correction | None | Mostly absent; slot total (slot-filled 82) | – | not applicable |
| M11 Reference construction | Prompted item | Prompted labels; slot total (slot-filled 234) | – | standard |
| M12 Evaluation | Within-speaker leave-one-out | Speaker-dependent (pattern match 22) | New users 81.5-85.5% words [[4]](#ref-4) [later] | standard |
| M13 Device and cost | Device use not measured | Device constraints; slot total (slot-filled 6,075) | – | not reported |

## Where the claims outrun the evidence

- "First phoneme-level" (Abstract) needs a qualifier: Shin and Seo classified five silently read vowels from contactless IR-UWB with one speaker (F-measure 0.943) [[2]](#ref-2), and a radar at 0.45 m classified five spoken (voiced) vowels for three participants [[5]](#ref-5), uncited. Neither classifies consonants, so what is new is contactless classification of 11 consonant syllables.
- Those items are CVC and VCV syllables classified as whole tokens (§III-A), not phonemes in running speech. Contact radar recognised 25 phonemes in 2018, as the paper notes [[6]](#ref-6), and [later] contact radar classifies 26 phonemes at 85.40% in a pooled three-speaker model [[7]](#ref-7).
- §V-D credits both the 2016 vowel and word results to five speakers; the vowel test used one [[2]](#ref-2).
- Lip beats chin (§V-B), but the positions also differ in antenna, beam width (55° × 50° versus 40° × 35°) and distance (5–10 versus 10–15 cm) (§III-B, §III-C).
- The single-radar position aid is tested on one participant, 88.13% against 89.38% with both radars on vowels (§V-E2), with no stated threshold.

## What the field needs next

- M12: speaker-held-out tests for contactless radar, with seeds, per-speaker spread and chance level.
- M06: a learned temporal front end against FERASEC on the 20-participant phoneme data.
- M05: a placement study that swaps antennas between lip and chin at matched distance.
- M08: open-vocabulary decoding from IR-UWB, as [later] backscatter work attempts [[4]](#ref-4).

## Questions for the authors

- What is accuracy with the test speaker excluded from training, and how many seeds underlie each Table 2 cell?
- Were the 20 repetitions recorded in one sitting or across separate placements?
- Which split produced Table 3?
- What correlation threshold gates acquisition?

## Appendix: literature search

**M06, radar-ssr-input-representation.** Inclusion rule: speech or silent-speech recognition from radar or RF sensing of the articulators (IR-UWB, FMCW, SFCW, CW Doppler, mmWave, Wi-Fi or RFID backscatter); compared design is the classifier input, engineered features versus raw frames or spectrograms into a learned network; throat-vibration speech recovery and datasets without a recognizer excluded; versions count once. Ledger counts: slot-filled 7,345 unique studies; pattern match 32 unique studies. Usual design: engineered features 21 (pattern match, upper bound); HMM 11; DTW template matching 9; learned network on raw frames or spectrograms 4. Known-item recall 1.0 (5 seeds). Read in full: [[3]](#ref-3), [[7]](#ref-7), [[2]](#ref-2), [[5]](#ref-5).

**M12, radar-ssr-speaker-split.** Inclusion rule: the same radar population; compared design is whether test speakers are held out (speaker-independent, new-user) or models are trained and tested within one speaker; a paper counts under every split it reports; related-work mentions are inside the upper bound. Ledger counts: slot-filled 6,960 unique studies; pattern match 32 unique studies. Usual design: speaker-dependent 22 (pattern match); speaker-independent 17 (pattern match, upper bound). Known-item recall 1.0. Read in full: [[4]](#ref-4), [[2]](#ref-2).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Lee, S., Shin, Y., Kim, M., Seo, J. “IR-UWB Radar-Based Contactless Silent Speech Recognition of Vowels, Consonants, Words, and Phrases.” *IEEE Access*, 2023. doi:[10.1109/ACCESS.2023.3344177](https://doi.org/10.1109/ACCESS.2023.3344177). arXiv:[2312.09572](https://arxiv.org/abs/2312.09572). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/ir-uwb-radar-based-contactless-silent-speech-recognition-of-vowels-consonants-words-and-phrases) [wiki: arxiv-2312.09572](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2312.09572/article.md) [wiki: doi-10.1109-access.2023.3344177](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-access.2023.3344177/article.md)
2. <a id="ref-2"></a>Shin, Y. H., Seo, J. “Towards Contactless Silent Speech Recognition Based on Detection of Active and Visible Articulators Using IR-UWB Radar.” *Sensors*, 2016, 16(11), 1812. doi:[10.3390/s16111812](https://doi.org/10.3390/s16111812). [wiki: doi-10.3390-s16111812](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3390-s16111812/article.md) [wiki: pmc-5134471-iruwb](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-5134471-iruwb/article.md)
3. <a id="ref-3"></a>Lee, S., Yu, J. “IR-UWB Radar-Based Contactless Silent Speech Recognition with Attention-Enhanced Temporal Convolutional Networks.” *IEEE International Conference on Consumer Electronics-Asia (ICCE-Asia)*, 2025. doi:[10.1109/ICCE-Asia67487.2025.11263683](https://doi.org/10.1109/ICCE-Asia67487.2025.11263683). arXiv:[2509.26409](https://arxiv.org/abs/2509.26409). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/ir-uwb-radar-based-contactless-silent-speech-recognition-with-attention-enhanced-temporal-convol) [wiki: arxiv-2509.26409](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2509.26409/article.md)
4. <a id="ref-4"></a>Tian, Y., Du, H., Gu, C., Zhang, J., Wang, S., Zhou, H., et al. “Lip-Siri: Contactless Open-Sentence Silent Speech with Wi-Fi Backscatter.” *arXiv preprint*, 2026. arXiv:[2601.18177](https://arxiv.org/abs/2601.18177). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lip-siri-contactless-open-sentence-silent-speech-with-wi-fi-backscatter) [wiki: arxiv-2601-18177-lipsiri](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2601-18177-lipsiri/article.md)
5. <a id="ref-5"></a>Hameed, H., Usman, M., Tahir, A., Hussain, A., Abbas, H., Cui, T. J., et al. “Pushing the limits of remote RF sensing by reading lips under the face mask.” *Nature Communications*, 2022, 13, 5168. doi:[10.1038/s41467-022-32231-1](https://doi.org/10.1038/s41467-022-32231-1). [wiki: pmc-9452506-rflip](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-9452506-rflip/article.md) [wiki: doi-10.1038-s41467-022-32231-1](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41467-022-32231-1/article.md) [wiki: pmc-9452506-rflipread](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-9452506-rflipread/article.md)
6. <a id="ref-6"></a>Birkholz, P., Stone, S., Wolf, K., Plettemeier, D. “Non-invasive silent phoneme recognition using microwave signals.” *IEEE/ACM Transactions on Audio, Speech, and Language Processing*, 2018, 26(12), 2404–2411. doi:[10.1109/TASLP.2018.2865609](https://doi.org/10.1109/TASLP.2018.2865609).
7. <a id="ref-7"></a>Menezes, J., Mouras, A., Fietkau, A., Kazzy, D., Birkholz, P. “Multimodal Silent Recognition of Phonemes Using Radar and Optopalatographic Silent Speech Interfaces.” *Proc. Interspeech 2025*, 2025, 5058–5062. doi:[10.21437/Interspeech.2025-759](https://doi.org/10.21437/Interspeech.2025-759). [later] [wiki: isca-menezes25-radaropg](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-menezes25-radaropg/article.md) [wiki: isca-menezes25_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-menezes25_interspeech/article.md)
