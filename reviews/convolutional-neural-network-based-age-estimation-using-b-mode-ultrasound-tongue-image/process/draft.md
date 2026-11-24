# Convolutional Neural Network-Based Age Estimation Using B-Mode Ultrasound Tongue Image

Xu, K., Csapó, T. G., Feng, M. · arXiv preprint · 2021 · [arXiv:2101.11245](https://arxiv.org/abs/2101.11245)

## Verdict

The paper changes one component, the output (M08): a speaker's age regressed by a CNN from single B-mode tongue frames [[1]](#ref-1). The output is new (none of the 99 paralinguistic studies in the Appendix matches an age-estimation pattern), but the verdict is standard because the evidence does not show that age is decoded. Frames of the same children fall on both sides of a random 80/20 split (§4.1), so a network that recognises the child returns that child's age, and a single ultrasound frame identifies speakers with 3.16% error in [concurrent] work [[2]](#ref-2). Evaluation (M12) is behind the best comparable work, which tests held-out children on the same UXTD corpus and finds them well below seen children [[3]](#ref-3). The abstract's "MAE" values are validation MSE in the body, taken on the data used to pick the augmentation (§4.3–4.4), and the proposed speech-therapy use is not tested. The claim that tongue images carry age information beyond speaker identity (§4.4) is unsupported.

## Against the field, component by component

### M08 Output: speaker age from tongue images

**Usual approach:** Among 99 studies that infer a paralinguistic property from a non-acoustic production signal (pattern match, published table, Appendix), the labels are emotion (50) or speaker identity (7); none matches an age-estimation pattern (0, Appendix).

**State of the art:** Diener et al. (2020, [concurrent]) identify speakers from EMG at 73% UAR (chance 12.5%) on held-out sessions [[4]](#ref-4). The target holds out neither children nor sessions, so it has no comparable figure.

Diener et al. hold out sessions so that results rest on speaker characteristics rather than session-specific aspects [[4]](#ref-4); the target has no such control. Its support is validation MSE 2.03 against 3.64 for a mean-age predictor on UXTD (§4.4), 44% lower (inference), and 4.87 against 5.35 on UPX (§4.5), 9% lower (inference). Speaker recognition alone could produce both gaps (M12). The authors call the work a proof of concept with a narrow age range (§5). Verdict: standard; no speaker-controlled, repeated effect shows the new output works.

### M12 Evaluation: children shared between training and validation

**Usual approach:** Of 148 ultrasound studies (pattern match, upper bound, Appendix), 48 mention a held-out-speaker test and 43 a speaker-dependent setup; none matches a random frame split pooled across speakers (0). The target splits frames at random 80/20, states no grouping by child, session or utterance, and has no test set (§4.1).

**State of the art:** Al Ani et al. (2024, [later]) report 82.32% precision for held-out speakers against 92.12% multi-speaker on nine UXTD children [[5]](#ref-5); the target does not measure this gap.

On the 58 UXTD children, Ribeiro et al. compare seen speakers with leave-one-speaker-out testing: their raw-image CNN falls from 74.70% to 59.42% (Table 1) [[3]](#ref-3), 20% relative (inference). Fabre et al. (2015) [[6]](#ref-6) and Eshky et al. (2019) [[7]](#ref-7) also test on unseen speakers. For age the leak is worse than for phonetic classes (inference): each child carries one label, so any speaker cue is an age cue, and ultrasound tongue videos are very speaker-specific [[2]](#ref-2). The 2.03 is a minimum validation MSE (§4.4) after the rotation setting was chosen among nine Table 3 rows on the same data (§4.3), with no seeds. Verdict: behind the best comparable work (same corpus, held-out speakers).

### M06 Decoder: single-frame CNN

**Usual approach:** Of the 148 ultrasound studies (pattern match, published table), 27 integrate frames by 3D convolution and 24 by a CNN with a recurrent layer. The target scores one frame from every 150 (§4.1) with a 2D CNN.

**State of the art:** Tongue2Speech (2026, [later]) reaches 15.93% WER with a 3D CNN and Transformer [[8]](#ref-8), a speech task; no age estimator exists to compare.

A frame-level model suits a static trait, but the paper neither pools a child's frames nor describes any normalisation (§3.1, §4.1–4.2). Ribeiro et al. add the speaker-mean frame as a second channel, lifting held-out-speaker CNN accuracy to 67.00% [[3]](#ref-3). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | UltraSuite child recordings | Recorded speech (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Age label only; audio unused | Paired-audio targets (slot-filled 31) | – | standard |
| M03 Training and adaptation | Pooled children, RMSprop, no seeds | Training records (slot-filled 1,526) | – | standard |
| M04 Use-time action | Overt child speech | Silent or overt (slot-filled 5,595) | – | standard |
| M05 Sensors | B-mode frame 63×412 | Ultrasound tongue imaging (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | 2D CNN on one frame | 3D convolution over frames (pattern match 27) | [[8]](#ref-8) (2026): WER 15.93% (speech task) | standard |
| M07 Lexicon and LM | None | None (slot-filled 119) | – | not applicable |
| M08 Output | Scalar age | Emotion label (pattern match 50) | [[4]](#ref-4) (2020): speaker ID 73% UAR | standard |
| M09 Confirmation | Offline | Offline (slot-filled 82) | – | not applicable |
| M10 Correction | Offline | Offline (slot-filled 82) | – | not applicable |
| M11 Reference construction | Child age from cohort data | Corpus references (slot-filled 234) | – | standard |
| M12 Evaluation | Random 80/20 frame split | Held-out speakers (pattern match 48) | [[5]](#ref-5) (2024): held-out-speaker precision 82.32% | behind |
| M13 Device and cost | Training GPU only | Hardware and cost (slot-filled 6,075) | – | standard |

## Where the claims outrun the evidence

- The abstract reports MAE 2.03 and 4.87; §4.4–4.5 and Table 3 call them validation MSE; Eq. (1), named MSE, prints an unsquared residual; no age unit is given.
- "Ultrasound tongue images contain some age information" (§4.4): speaker identification explains the same result (M12).
- The abstract proposes a speech-therapy assessment tool; §4 reports only age error, no session-level measurement.
- A clinical linguist cannot estimate age from an ultrasound image (§1): no human-reader experiment backs this.
- §4.1 assigns both 24,449 and 54,582 frames to UXTD.

## What the field needs next

- M12: leave-one-child-out testing on UXTD and UPX, one estimate per child, error in years against the cohort-mean predictor, several seeds.
- M12: age error on held-out children set beside speaker-recognition accuracy on the same frames.
- M06: a speaker-mean channel and pooling over a child's frames against the single-frame model.
- M08: within-child tracking across UPX sessions, which the therapy claim requires.

## Questions for the authors

- Did any child contribute frames to both training and validation?
- Are 2.03 and 4.87 MSE or MAE, and in years?
- Is 2.03 the best epoch on validation data, and how many runs were made?
- Was any intensity normalisation applied?
- Was the mean-age predictor fitted on training or validation ages?

## Appendix: literature search

- M08, paralinguistic-output-from-production-signals (published table, reused). Inclusion rule: studies that infer a paralinguistic property of the speaker or utterance (affect, speaker identity, speaking mode, prosody) from a non-acoustic speech-production signal (EMG, EMA, ultrasound, real-time MRI, electropalatography, strain sensors, ECoG or intracortical recordings); acoustic-only and face-video emotion recognition excluded; versions count once. Ledger: 3,268 unique studies slot-filled for M08; 99 unique studies pattern match. Usual design: audio output 12 (slot-filled, 71 studies with an M08 value). Full-text patterns over the candidates (this review): emotion 50, speaker identity 7, age estimation 0 (pattern match). The target's ledger text names no paralinguistic keyword; it enters by the inclusion rule (a speaker trait from ultrasound). Read in full: [[4]](#ref-4). Known-item recall 1.0.
- M12, ultrasound-tongue-speaker-split (new). Inclusion rule: studies whose ledger lists ultrasound imaging, classified by full-text pattern into held-out-speaker tests (speaker-independent, unseen or held-out speakers, leave-one-speaker-out, cross-speaker) and within-speaker setups (speaker-dependent, single-speaker); related-work mentions count (upper bound); a study counts under every split it names; versions count once. Ledger: 6,960 unique studies slot-filled for M12; 148 unique studies pattern match. Held-out speakers 48, speaker-dependent 43, random frame-level split 0 (pattern match). Read in full: [[3]](#ref-3), [[6]](#ref-6), [[7]](#ref-7), [[5]](#ref-5), [[2]](#ref-2). Known-item recall 1.0 (2 seeds).
- M06, ultrasound-image-sequence-temporal-layer (published table, reused). Inclusion rule: studies listing ultrasound imaging, classified by how the network integrates frames over time (3D convolution, CNN then recurrent layer, ConvLSTM, Transformer); related-work mentions count (upper bound). Ledger: 7,345 unique studies slot-filled for M06; 148 unique studies pattern match. 3D convolution 27, CNN then recurrent 24, ConvLSTM 9, Transformer or Conformer 8 (pattern match, published counts). Read in full (published table): [[8]](#ref-8). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [convolutional-neural-network-based-age-estimation-using-b-mode-ultrasound-tongue-image.bib](convolutional-neural-network-based-age-estimation-using-b-mode-ultrasound-tongue-image.bib).

1. <a id="ref-1"></a>Xu, K., Csapó, T. G., Feng, M. “Convolutional Neural Network-Based Age Estimation Using B-Mode Ultrasound Tongue Image.” *arXiv preprint*, 2021. doi:[10.48550/arXiv.2101.11245](https://doi.org/10.48550/arXiv.2101.11245). arXiv:[2101.11245](https://arxiv.org/abs/2101.11245). Target. Read as arXiv v1. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/convolutional-neural-network-based-age-estimation-using-b-mode-ultrasound-tongue-image) [wiki: arxiv-2101.11245](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2101.11245/article.md)
2. <a id="ref-2"></a>Shandiz, A. H., Tóth, L., Gosztolya, G., Markó, A., Csapó, T. G. “Neural Speaker Embeddings for Ultrasound-based Silent Speech Interfaces.” *Proc. Interspeech 2021*, 2021, 1932–1936. doi:[10.21437/Interspeech.2021-1466](https://doi.org/10.21437/Interspeech.2021-1466). arXiv:[2106.04552](https://arxiv.org/abs/2106.04552). Single-frame speaker recognition from ultrasound (Table 1). Read as arXiv v2. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/neural-speaker-embeddings-for-ultrasound-based-silent-speech-interfaces) [wiki: arxiv-2106.04552](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2106.04552/article.md) [wiki: doi-10.21437-interspeech.2021-1466](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.21437-interspeech.2021-1466/article.md) [wiki: isca-shandiz21-usspeaker](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-shandiz21-usspeaker/article.md) [wiki: isca-shandiz21_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-shandiz21_interspeech/article.md)
3. <a id="ref-3"></a>Ribeiro, M. S., Eshky, A., Richmond, K., Renals, S. “Speaker-independent classification of phonetic segments from raw ultrasound in child speech.” *arXiv preprint*, 2019. arXiv:[1907.01413](https://arxiv.org/abs/1907.01413). Prior; deciding prior for M12 (same UXTD corpus, leave-one-speaker-out). Cited by the target. [wiki: arxiv-1907.01413](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1907.01413/article.md)
4. <a id="ref-4"></a>Diener, L., Amiriparian, S., Botelho, C., Scheck, K., Küster, D., Trancoso, I., et al. “Towards Silent Paralinguistics: Deriving Speaking Mode and Speaker ID from Electromyographic Signals.” *Proc. Interspeech 2020*, 2020, 3117-3121. doi:[10.21437/Interspeech.2020-2848](https://doi.org/10.21437/Interspeech.2020-2848). Closest speaker-trait decoder from a production signal, held-out sessions. [concurrent] [wiki: isca-diener20-emgmode](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-diener20-emgmode/article.md) [wiki: isca-diener20_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-diener20_interspeech/article.md)
5. <a id="ref-5"></a>Al Ani, S., Cleland, J., Zoha, A. “Automated Classification of Phonetic Segments in Child Speech Using Raw Ultrasound Imaging.” *arXiv preprint*, 2024. arXiv:[2402.17482](https://arxiv.org/abs/2402.17482). Held-out-speaker evaluation on UXTD. [later] [wiki: arxiv-2402.17482](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2402.17482/article.md)
6. <a id="ref-6"></a>Fabre, D., Hueber, T., Bocquelet, F., Badin, P. “Tongue Tracking in Ultrasound Images using EigenTongue Decomposition and Artificial Neural Networks.” *Proc. Interspeech 2015*, 2015, 2410-2414. doi:[10.21437/Interspeech.2015-521](https://doi.org/10.21437/Interspeech.2015-521). Prior; held-out-speaker test on ultrasound. [wiki: doi-10.21437-interspeech.2015-521](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.21437-interspeech.2015-521/article.md)
7. <a id="ref-7"></a>Eshky, A., Ribeiro, M. S., Richmond, K., Renals, S. “Synchronising audio and ultrasound by learning cross-modal embeddings.” *Proc. Interspeech 2019*, 2019. doi:[10.21437/Interspeech.2019-1804](https://doi.org/10.21437/Interspeech.2019-1804). Prior; test on unseen speakers and sessions of child ultrasound. [wiki: isca-eshky19-sync](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-eshky19-sync/article.md)
8. <a id="ref-8"></a>Sonkar, Y., Kilaru, Y., Yelimeli, S., Shah, N., Gandhi, V. “Tongue2Speech: Real-Time Speech Synthesis from Tongue Ultrasound Videos via Spatiotemporal Transformers.” *Proc. Interspeech 2026*, 2026, 6856–6860. doi:[10.21437/Interspeech.2026-3023](https://doi.org/10.21437/Interspeech.2026-3023). State of the art in the reused M06 table. [later] [wiki: isca-sonkar26_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-sonkar26_interspeech/article.md)
