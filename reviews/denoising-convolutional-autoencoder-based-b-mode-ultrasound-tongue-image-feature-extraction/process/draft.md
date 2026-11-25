# Denoising Convolutional Autoencoder Based B-Mode Ultrasound Tongue Image Feature Extraction

Li B, Xu K, Feng D, Mi H, Wang H, Zhu J. arXiv preprint, 2019. [arXiv:1903.00888](https://arxiv.org/abs/1903.00888)

## Verdict

The paper [[1]](#ref-1) changes one component, the ultrasound feature extractor (M06), replacing DCT or a fully connected autoencoder with a convolutional autoencoder trained on speckle-corrupted inputs; it is standard. Speckle denoising of tongue ultrasound predates it [[2]](#ref-2), so the "first attempt" (§4) holds only for the convolutional variant. The headline 6.17% against the "state-of-the-art" 6.45% (Abstract) sets length 60 against DCT at length 30; at equal length the margin is 0.41 points, about 4 words of the 1023-word test [[3]](#ref-3) (inference), from unrepeated runs on one speaker. Denoising adds 0.05 points over the plain convolutional autoencoder (Table 2), so the evidence supports convolution, not denoising. The eight new WERs in Table 2 are not whole error counts over 1023 words, while the two that equal Ji et al.'s published values are (inference), and the paper does not say how they were obtained.

## Against the field, component by component

### M06 Processing: convolutional denoising autoencoder features

**Usual approach:** PCA (EigenTongues) or 2D-DCT coefficients, about 30 per stream; of 39 unique ultrasound feature studies (pattern match, Appendix), 32 use PCA, 13 DCT and 13 autoencoders [[4]](#ref-4) [[5]](#ref-5). The paper keeps the DCT and fully connected autoencoder baselines of Ji et al. [[3]](#ref-3).

**State of the art:** the target's 6.17% (2019) remains the lowest SSC WER in the topic tables (Appendix); at the time the reference was 6.45% with 30 DCT coefficients and a DNN-HMM (2018) [[3]](#ref-3). The [later] end-to-end SSC model reaches 20.5% (2020) with a 65,000-word language model [[6]](#ref-6).

Convolution is what moves WER: the fully connected Deep AE gives 7.37% and the CAE 6.22% at length 60 (Table 2), 16% relative (inference). Against DCT the gain is small: 6.58% to 6.17% at length 60 (6.2% relative) and 6.45% to 6.24% at length 30 (3.3% relative) (inference). Denoising contributes 0.05 points at length 60 and 0.10 at length 30 (Table 2), half a word and one word (inference). Jaumard-Hakoun et al. added speckle noise to tongue images during training only (Sec. 3.1), the same criterion on stacked-RBM layers [[2]](#ref-2); the target gives no noise distribution or level (§3.1). Verdict: standard: a margin of a few words over DCT, one speaker, no repetition, and prior denoising.

### M12 Evaluation: SSC word error rate

**Usual approach:** WER on the 100 WSJ0 test sentences (1023 words) of the single SSC speaker with the closed WSJ0 5k bigram; 3 of 8 unique SSC studies (pattern match, Appendix) use this condition [[5]](#ref-5) [[3]](#ref-3). The paper keeps it and adds image reconstruction (§3.2).

**State of the art:** 6.17% (2019), the paper's own value, 0.28 points below the 6.45% reference (inference). The two [later] studies recognizing the SSC sentences change the language model (2020) [[6]](#ref-6) or re-record the sentences (2022) [[7]](#ref-7) (Appendix), so no later study tests the closed-bigram number under its own condition.

Ji et al. report 6 insertions, 8 deletions and 52 substitutions over 1023 words for 6.45% (Table 2) [[3]](#ref-3). The target's length-30 DCT (6.45%) and Deep AE (7.72%) equal Ji et al.'s values, but its new values, such as 6.17%, 6.22% and 6.58%, are not whole error counts over 1023 words (inference): averages over runs or another test set, neither stated. Reconstruction test frames (30,000) are drawn at random from the single-speaker SSC archive (§3.2), so they neighbour training frames of the same utterances (inference). Verdict: standard, with the same single-run reporting as Ji et al.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Silent TIMIT reading, one speaker (SSC) | Reading tasks (slot-filled 4,015) | – | standard |
| M02 Training-only supervision | Unlabelled reconstruction; recognizer labels from Ji et al. | Text or phone labels (slot-filled 31) | – | standard |
| M03 Training and adaptation | 200 epochs; selection data, noise, seeds unstated | Per-speaker training (slot-filled 1,608) | – | not reported |
| M04 Use-time action | Silent articulation | Overt or silent (slot-filled 6,538) | – | standard |
| M05 Sensors | Ultrasound plus lip camera, 60 fps, ROI 50x60 | Ultrasound plus lips (slot-filled 8,898) | – | standard |
| M06 Processing and decoding | Denoising convolutional AE features | PCA or DCT, about 30 per stream (pattern match 32) | 6.17% WER [[1]](#ref-1) | standard |
| M07 Lexicon and LM | WSJ language model | Closed WSJ0 5k bigram; SSC studies, M12 tally of 8 (pattern match 3) | 20.5% WER, 65k LM [[6]](#ref-6) | standard |
| M08 Output | Word sequence | Text (slot-filled 3,760) | – | standard |
| M09 Confirmation | None | None (slot-filled 82) | – | not applicable |
| M10 Correction | None | None (slot-filled 82) | – | not applicable |
| M11 Reference construction | SSC split for WER; random frames for reconstruction | SSC split (slot-filled 239) | – | standard |
| M12 Evaluation | WER, 1023 words, single runs; MSE, CW-SSIM | SSC WER, closed bigram (pattern match 3) | 6.17% WER [[1]](#ref-1) | standard |
| M13 Device and cost | Offline helmet; no runtime | Laboratory prototype (slot-filled 6,721) | – | not reported |

## Where the claims outrun the evidence

- "Outperforms" the 6.45% "state-of-the-art" (Abstract) crosses feature lengths; at equal length the margin is 0.41 points, with no seed, repeat or significance test (§3).
- The "first attempt to use denoising CAE" (§4) omits that the speckle-denoising criterion appears in a paper it cites [[2]](#ref-2).
- Robustness to "head movements, variability due to different imaging systems and speckle noises" (§4) has no head-motion, instrument or noise-level test; all data come from the single SSC speaker [[3]](#ref-3).
- DCT reconstruction MSE rises from 86.27 to 89.03 as length grows from 30 to 60 (Table 1); adding orthonormal coefficients cannot raise squared error (inference), so the DCT baseline is not a plain truncation, which §3.2 leaves unexplained.
- §3.3 calls the inputs "concatenated tongue and lip feature vectors of dimension K = 60 and 30", yet the length-30 row reproduces Ji et al.'s per-stream K=30 values, a 120-component vector with deltas [[3]](#ref-3) (inference).

## What the field needs next

- M06 and M12: rerun the SSC comparison at equal length with several seeds and per-sentence error counts, with a paired test of DCAE against DCT.
- M06: isolate denoising by varying speckle variance and testing on corrupted or unseen-session images.
- M05 and M06: train on one ultrasound set-up and test on another, with other speakers.

## Questions for the authors

- Are the new Table 2 values averages over runs, or from a test set other than the 1023-word SSC test?
- Were the length-30 DCT and Deep AE results rerun or copied from Ji et al.?
- Does "length" count one stream or both?
- What speckle level, seeds and normalization were used, and which data selected the architectures (§3.1)?
- Which DCT coefficients form the (10, 6) features?

## Appendix: literature search

- M06 ultrasound-tongue-image-features. Inclusion rule: studies that compress ultrasound tongue images, with or without lip images, into feature vectors by DCT, PCA/EigenTongues, autoencoders or learned CNN encoders for recognition, synthesis or articulatory mapping; contour-only tracking, raw-image end-to-end models with no feature stage and reviews excluded; versions counted once. Ledger counts: slot-filled 7,345 unique studies (M06); pattern match 39 unique studies. Usual design (pattern match, full text; a study can match several): PCA/EigenTongue 32, DCT 13, autoencoder 13, raw-image CNN 2. Read in full: [[2]](#ref-2) (prior), [[3]](#ref-3) (prior), [[4]](#ref-4) (prior), [[5]](#ref-5) (prior). Known-item recall 0.75.
- M12 silent-speech-challenge-benchmark. Inclusion rule: studies reporting recognition or reconstruction results on the SSC archive (single speaker, silent TIMIT training, 100 WSJ0 5k test sentences) or on the same 100 sentences re-recorded; mere citations and other ultrasound corpora excluded; surveys kept in the pattern count only; versions counted once. Ledger counts: slot-filled 6,960 unique studies (M12); pattern match 8 unique studies, of which 5 recognize the SSC test sentences and 3 decode with the closed WSJ0 5k bigram. Read in full: [[5]](#ref-5) (prior), [[3]](#ref-3) (prior), [[6]](#ref-6), [[7]](#ref-7). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [denoising-convolutional-autoencoder-based-b-mode-ultrasound-tongue-image-feature-extraction.bib](denoising-convolutional-autoencoder-based-b-mode-ultrasound-tongue-image-feature-extraction.bib).

1. <a id="ref-1"></a>Li, B., Xu, K., Feng, D., Mi, H., Wang, H., Zhu, J. “Denoising Convolutional Autoencoder Based B-mode Ultrasound Tongue Image Feature Extraction.” *arXiv preprint*, 2019. arXiv:[1903.00888](https://arxiv.org/abs/1903.00888). Target. Title and authors from the first page of arXiv:1903.00888 v1 (2019-03). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/denoising-convolutional-autoencoder-based-b-mode-ultrasound-tongue-image-feature-extraction) [wiki: arxiv-1903.00888](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1903.00888/article.md)
2. <a id="ref-2"></a>Jaumard-Hakoun, A., Xu, K., Leboullenger, C., Roussel-Ragot, P., Denby, B. “An Articulatory-Based Singing Voice Synthesis Using Tongue and Lips Imaging.” *Proc. Interspeech 2016*, 2016. doi:[10.21437/Interspeech.2016-385](https://doi.org/10.21437/Interspeech.2016-385). Prior; deciding prior for M06 (speckle-noise denoising autoencoder on tongue ultrasound). Title, authors and DOI from the paper's first page; URL from the ISCA archive. [wiki: isca-jaumardhakoun16_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-jaumardhakoun16_interspeech/article.md)
3. <a id="ref-3"></a>Ji, Y., Liu, L., Wang, H., Liu, Z., Niu, Z., Denby, B. “Updating the Silent Speech Challenge benchmark with deep learning.” *Speech Communication*, 2018. doi:[10.1016/j.specom.2018.02.002](https://doi.org/10.1016/j.specom.2018.02.002). arXiv:[1709.06818](https://arxiv.org/abs/1709.06818). Prior; deciding prior for M06 (fully connected DAE and DCT baselines) and the SSC reference value. Title and authors from the first page of arXiv:1709.06818 v1 (2017-09); journal version in Speech Communication, 2018. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/updating-the-silent-speech-challenge-benchmark-with-deep-learning) [wiki: arxiv-1709.06818](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1709.06818/article.md) [wiki: doi-10.1016-j.specom.2018.02.002](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1016-j.specom.2018.02.002/article.md)
4. <a id="ref-4"></a>Hueber, T., Aversano, G., Chollet, G., Denby, B., Dreyfus, G., Oussar, Y., et al. “Eigentongue Feature Extraction for an Ultrasound-Based Silent Speech Interface.” *Proc. IEEE ICASSP 2007*, 2007, 1245–1248. <https://www.gipsa-lab.grenoble-inp.fr/~thomas.hueber/mes_documents/hueber_icassp2007.pdf> Prior; typical work of the usual M06 approach (PCA EigenTongues). Title and authors from the paper's first page; URL of the author-hosted manuscript. [wiki: icassp2007-hueber-eigentongue-ssi](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/icassp2007-hueber-eigentongue-ssi/article.md)
5. <a id="ref-5"></a>Cai, J., Denby, B., Roussel, P., Dreyfus, G., Crevier-Buchman, L. “Recognition and Real Time Performances of a Lightweight Ultrasound Based Silent Speech Interface Employing a Language Model.” *Proc. Interspeech 2011*, 2011, 1005–1008. doi:[10.21437/Interspeech.2011-410](https://doi.org/10.21437/Interspeech.2011-410). Title and authors from the paper's first page; DOI and URL from the ISCA archive record. [wiki: isca-cai11_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-cai11_interspeech/article.md) [wiki: isca-cai11-lightssi](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-cai11-lightssi/article.md)
6. <a id="ref-6"></a>Kimura, N., Su, Z., Saeki, T. “End-to-End Deep Learning Speech Recognition Model for Silent Speech Challenge.” *Proc. Interspeech 2020 (Show and Tell)*, 2020. <https://www.isca-archive.org/interspeech_2020/kimura20_interspeech.html> Title and authors from the paper's first page; URL from the ISCA archive. [later] [wiki: isca-kimura20_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-kimura20_interspeech/article.md) [wiki: isca-kimura20-sschallenge](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-kimura20-sschallenge/article.md)
7. <a id="ref-7"></a>Kimura, N., Su, Z., Saeki, T., Rekimoto, J. “SSR7000: A Synchronized Corpus of Ultrasound Tongue Imaging for End-to-End Silent Speech Recognition.” *Proceedings of the 13th Conference on Language Resources and Evaluation (LREC 2022)*, 2022, 6866–6873. <https://aclanthology.org/2022.lrec-1.741> Title, authors, venue and pages from the paper's first page. [later] [wiki: lrec22-ssr7000](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/lrec22-ssr7000/article.md) [wiki: doi-10.63317-2b659u3p6oeh](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.63317-2b659u3p6oeh/article.md)
