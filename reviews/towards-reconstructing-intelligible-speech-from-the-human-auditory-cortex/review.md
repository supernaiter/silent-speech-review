# Towards reconstructing intelligible speech from the human auditory cortex

Akbari, Khalighinejad, Herrero, Mehta, Mesgarani. Scientific Reports 9: 874, 2019. [doi:10.1038/s41598-018-37359-z](https://doi.org/10.1038/s41598-018-37359-z)

## Verdict

The paper [[1]](#ref-1) changes one component, the decoding target (M06): a network decodes a 256-node autoencoder code of WORLD vocoder parameters. For heard speech this is ahead: all 4 earlier heard-speech intracranial reconstruction studies in the ledger decode a spectrogram (Appendix), and the model ordering repeats in each of five patients (Fig. 4). The authors' wider claim that synthesizer parameters had never been estimated from neural data does not hold: formant-synthesizer parameters were decoded in 2009 [[2]](#ref-2) and ten LPC coefficients from ECoG in 2015 [[3]](#ref-3), both during production. The strongest confound is the autoencoder: raw vocoder parameters score below the spectrogram (ESTOI 0.30 against 0.40, Supplementary Table 2), so the gain belongs to a compression trained on 80 hours of external speech. The listener test (M12) is standard: ten closed-set digits, tokens from a patient or aggregation the paper does not name.

## Against the field, component by component

### M06 Processing and decoding: decoding target

**Usual approach:** before the target's first public date (bioRxiv, 2018-06), the 4 heard-speech intracranial reconstruction studies among the topic's ledger matches all decode a spectrogram, 3 by linear regression and 1 by a deep network (pattern match, Appendix), e.g. Pasley et al. [[4]](#ref-4) and Yang et al. [[5]](#ref-5), the same laboratory's network-versus-linear test in two patients. The paper departs in the target only; the deep regressor comes from Yang et al., whom the authors cite.

**State of the art:** the best listener score from neural signals among the topic's ledger metric candidates (Appendix) is 80% of words synthesized online for one participant with ALS from 6 keywords during production [[6]](#ref-6) (2024) [later], against 75% of 10 heard digits here; chance is 16.7% against 10% (inference). The closest later heard-speech design, a speech-GAN latent decoded from 9 intracranial subjects watching a film [[7]](#ref-7) [later], reports correlations only, and direct mel decoding correlates better.

A whole-wiki full-text check to 2018 finds 18 studies decoding or discussing synthesizer-like parameters (formants, LPC, mel-cepstra) from neural signals, all in production or imagery, and none decoding an autoencoder code (Appendix). The heard-speech vocoder target is new in its setting; the synthesizer idea is a decade older in production, a lineage the paper does not cite. The coded vocoder gains +17.5% relative ESTOI over the network spectrogram (0.47 against 0.40) and +52% over the linear baseline (0.31) (inference), with the ordering repeated across five patients; the listener gain has no per-patient repetition. Verdict: ahead for heard speech.

### M12 Evaluation: listener intelligibility test

**Usual approach:** correlation. All 14 reconstruction evaluations in the topic table first public 2017 or earlier score correlation, and none has listeners rate decoded audio (pattern match and whole-wiki check, Appendix). The paper adds 11 listeners, 40 TI-46 digit tokens per model, MOS and speaker gender beside ESTOI.

**State of the art:** listeners recognize 80% of 6 keywords synthesized online [[6]](#ref-6) (2024) [later]; open transcription arrived concurrently, a median 31% WER with a 25-word pool [[8]](#ref-8) [concurrent].

Listener scoring is the paper's most useful change to evaluation practice, yet networks are per patient, the patient behind the 40 tokens is not given, and each digit was repeated six times to raise the signal-to-noise ratio (Methods). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Passive listening to 30 min of stories | Passive listening in clinical sessions | – | standard |
| M02 Training-only supervision | Heard stimulus as target; autoencoder trained on 80 h of external speech | Paired stimulus target | – | standard |
| M03 Training and adaptation | Per-patient fit; duration sweep 10–30 min | Per-subject training | – | standard |
| M04 Use-time action | Listening to stories, sentences and digits | Listening to presented speech | – | standard |
| M05 Sensors | ECoG grids and depth electrodes; low-frequency plus high-gamma | Clinical ECoG, high gamma | – | standard |
| M06 Processing and decoding | Network to autoencoder code of WORLD parameters | Spectrogram target (pattern match 4) | [[6]](#ref-6) (2024): 80% listener recognition, 6 words | ahead |
| M07 Lexicon and LM | None; closed set of 10 digits | No language model | – | standard |
| M08 Output | WORLD-synthesized audio | Spectrogram inverted to audio | – | standard |
| M09 Confirmation | None (offline) | Offline study | – | not applicable |
| M10 Correction | None (offline) | Offline study | – | not applicable |
| M11 Reference construction | Presented stimulus; responses averaged over repeats | Presented stimulus | – | standard |
| M12 Evaluation | ESTOI; 11 listeners, 10 digits, MOS | Correlation (pattern match 14) | [[6]](#ref-6) (2024): 80% listener recognition, 6 words | standard |
| M13 Device and cost | Offline clinical recording | Offline clinical recording | – | standard |

## Where the claims outrun the evidence

- Priority (Introduction): "this has not been attempted previously" is contradicted by synthesizer-parameter decoding during production [[2]](#ref-2), [[3]](#ref-3) (Appendix); a heard-speech qualifier would make it true.
- Target or compression (Supplementary Table 2): raw vocoder 0.30, network spectrogram 0.40, coded vocoder 0.47. No coded spectrogram was tested, so the target is credited for what the 80-hour speech prior supplies (inference).
- Bottleneck (Supplementary Table 3): 32, 128 and 256 nodes tie at 0.47, yet 256 is said to maximize accuracy.
- Headline: 65% in the Abstract, 67% in Results (Fig. 3), over the same baseline.
- Averaging (M11): objective sentences repeated six times (Results, Supp. Fig. 1) or eight (Methods); the interface framing rests on averaged responses.
- Listeners: 11 (Fig. 3 caption) against "all the ten listeners" in Results.
- Electrodes (M05): up to 128 electrodes pooled across five patients (Fig. 5), a coverage no patient had; the authors call the combined setting an upper bound.

## What the field needs next

- M06: coded spectrogram against coded vocoder, one corpus, same patients.
- M12: open-set listener transcription of single-trial heard-speech reconstructions, per patient.
- M06: latent against mel targets scored by listeners, settling the [later] correlation result [[7]](#ref-7).

## Questions for the authors

- Which patient, or which aggregation of the five per-patient models, produced the 40 tokens per model?
- Were listener tokens decoded from single trials or from the average of six digit repetitions?
- Were the objective sentences presented six or eight times?
- Which validation data, folds and seeds selected the bottleneck size and feature extractor?
- How were "uncertain" responses scored, and what chance levels apply to digit and gender identification?

## Appendix: literature search

- **M06 / heard-speech-reconstruction-target-representation** (published table, reused and appended). Inclusion rule: studies whose ledger text names intracranial or auditory-cortex recordings, a listening or perception condition, an acoustic representation and reconstruction, decoding or synthesis; design of interest: the representation the decoder reconstructs; versions count once. Ledger counts: slot-filled 7,345 unique studies; pattern match 64 unique studies (72 folders), plus 5 full-text-only folders. First public 2017 or earlier (target 2018-06): 11 matches, 4 heard-speech intracranial reconstruction studies, 7 off-population; among the 4: spectrogram target 4, deep regression 1, vocoder or synthesizer target 0, compressed latent 0 (pattern match). Whole-wiki full-text checks to 2018: synthesizer-parameter decoding near a neural-recording term 18 studies, all production, imagery, reviews or non-neural; autoencoder or bottleneck target 0; listener rating of decoded audio 6 hits, none rating neural reconstructions. Listener scores among sota candidates: 92% and 85% (non-neural), 80% [[6]](#ref-6), 75% (target). Read in full: [[5]](#ref-5), [[2]](#ref-2), [[3]](#ref-3), [[7]](#ref-7), [[6]](#ref-6); read for the published table: [[4]](#ref-4), [[9]](#ref-9). Known-item recall 1.0 (3 seeds).
- **M12 / neural-speech-reconstruction-identification-test** (published table, reused and appended). Inclusion rule: studies that reconstruct a continuous acoustic speech representation from neural recordings and evaluate it; design categories overlap; versions count once. Ledger counts: pattern match 173 unique studies (221 folders). First public 2017 or earlier: 19 matches, 14 reconstruction evaluations, 5 off-population; correlation 14, listening-test pattern 8 (participants' listening tasks), listener rating of decoded audio 0. Read: [[6]](#ref-6), [[8]](#ref-8). Known-item recall 0.67.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Akbari, H., Khalighinejad, B., Herrero, J. L., Mehta, A. D., Mesgarani, N. “Towards reconstructing intelligible speech from the human auditory cortex.” *Scientific Reports*, 2019, 9, 874. doi:[10.1038/s41598-018-37359-z](https://doi.org/10.1038/s41598-018-37359-z). Target. Read as the Scientific Reports article with its supplement; first public as bioRxiv 10.1101/350124 (2018-06). [wiki: doi-10.1038-s41598-018-37359-z](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41598-018-37359-z/article.md) [wiki: pmc-6351601-audrecon](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-6351601-audrecon/article.md) [wiki: pmc-6351601-intelligible](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-6351601-intelligible/article.md)
2. <a id="ref-2"></a>Guenther, F. H., Brumberg, J. S., Wright, E. J., Nieto-Castanon, A., Tourville, J. A., Panko, M., et al. “A Wireless Brain-Machine Interface for Real-Time Speech Synthesis.” *PLoS ONE*, 2009, 4(12), e8218. doi:[10.1371/journal.pone.0008218](https://doi.org/10.1371/journal.pone.0008218). Prior; deciding prior for M06 (formant-synthesizer parameters decoded during attempted production). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-wireless-brain-machine-interface-for-real-time-speech-synthesis) [wiki: pmc-2784218-wireless](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wireless/article.md)
3. <a id="ref-3"></a>Chakrabarti, S. “Characterization and Decoding of Speech Representations From the Electrocorticogram.” *Old Dominion University*, 2015. doi:[10.25777/he41-jj63](https://doi.org/10.25777/he41-jj63). Prior; deciding prior for M06 (LPC coefficients decoded from ECoG during overt speaking). Thesis dated Summer 2015. [wiki: doi-10.25777-he41-jj63](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.25777-he41-jj63/article.md)
4. <a id="ref-4"></a>Pasley, B. N., David, S. V., Mesgarani, N., Flinker, A., Shamma, S. A., Crone, N. E., et al. “Reconstructing Speech from Human Auditory Cortex.” *PLoS Biology*, 2012, 10(1), e1001251. doi:[10.1371/journal.pbio.1001251](https://doi.org/10.1371/journal.pbio.1001251). Prior; heard-speech linear spectrogram reconstruction. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/reconstructing-speech-from-human-auditory-cortex) [wiki: doi-10.1371-journal.pbio.1001251](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1371-journal.pbio.1001251/article.md) [wiki: pmc-3269422-pasley](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3269422-pasley/article.md) [wiki: pmc-3269422-speechrecon](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3269422-speechrecon/article.md)
5. <a id="ref-5"></a>Yang, M., Sheth, S. A., Schevon, C. A., McKhann, G. M., Mesgarani, N. “Speech Reconstruction from Human Auditory Cortex with Deep Neural Networks.” *Proc. Interspeech 2015*, 2015. doi:[10.21437/Interspeech.2015-478](https://doi.org/10.21437/Interspeech.2015-478). Prior; deciding prior for M06 (heard speech, DNN versus linear regression, spectrogram target). [wiki: isca-yang15c_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-yang15c_interspeech/article.md)
6. <a id="ref-6"></a>Angrick, M., Luo, S., Rabbani, Q., Candrea, D. N., Shah, S., Milsap, G. W., et al. “Online speech synthesis using a chronically implanted brain-computer interface in an individual with ALS.” *Scientific Reports*, 2024, 14, 9617. doi:[10.1038/s41598-024-60277-2](https://doi.org/10.1038/s41598-024-60277-2). Later; state of the art for M06 and M12 (closed-set listener recognition of synthesized words). [later] [wiki: doi-10.1038-s41598-024-60277-2](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41598-024-60277-2/article.md) [wiki: pmc-11053081-als-ecog-synth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11053081-als-ecog-synth/article.md) [wiki: pmc-11053081-onlinesyn](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11053081-onlinesyn/article.md)
7. <a id="ref-7"></a>Berezutskaya, J., Ambrogioni, L., Ramsey, N. F., van Gerven, M. A. J. “Towards naturalistic speech decoding from intracranial brain data.” *2022 44th Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC)*, 2022, 3100-3104. doi:[10.1109/EMBC48229.2022.9871301](https://doi.org/10.1109/EMBC48229.2022.9871301). Later; heard-speech decoding of a compressed GAN latent. [later] [wiki: doi-10.1109-embc48229.2022.9871301](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-embc48229.2022.9871301/article.md)
8. <a id="ref-8"></a>Anumanchipalli, G. K., Chartier, J., Chang, E. F. “Speech synthesis from neural decoding of spoken sentences.” *Nature*, 2019, 568(7753), 493-498. doi:[10.1038/s41586-019-1119-1](https://doi.org/10.1038/s41586-019-1119-1). Concurrent (bioRxiv 10.1101/481267, 2018-11); listener transcription of synthesized sentences. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/speech-synthesis-from-neural-decoding-of-spoken-sentences) [wiki: doi-10.1038-s41586-019-1119-1](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-019-1119-1/article.md) [wiki: pmc-9714519-speechsynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-9714519-speechsynth/article.md)
9. <a id="ref-9"></a>Chang, E. F., Rieger, J. W., Johnson, K., Berger, M. S., Barbaro, N. M., Knight, R. T. “Categorical Speech Representation in Human Superior Temporal Gyrus.” *Nature Neuroscience*, 2010, 13(11), 1428-1432. doi:[10.1038/nn.2641](https://doi.org/10.1038/nn.2641). Prior; read for the published M06 topic table (pSTG ECoG, passive listening, classification). [wiki: pmc-2967728-categoricalstg](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2967728-categoricalstg/article.md)
