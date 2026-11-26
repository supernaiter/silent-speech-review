# Reconstructing Speech from Human Auditory Cortex

Pasley, David, Mesgarani, Flinker, Shamma, Crone, Knight, Chang. PLoS Biology 10(1): e1001251, 2012. [doi:10.1371/journal.pbio.1001251](https://doi.org/10.1371/journal.pbio.1001251)

## Verdict

The paper [[1]](#ref-1) changes the decoding target (M06): it reconstructs heard speech from human superior temporal gyrus as a linear auditory spectrogram and as nonlinear temporal-modulation energy. For 2012 this is ahead: no study in the 64-study heard-speech reconstruction population predates it (Appendix), the read human priors classified syllable responses [[2]](#ref-2) or decoded formants during attempted speech [[3]](#ref-3), and the linear-versus-modulation comparison repeats across 15 participants (F(1,14) = 33.36). The evaluation (M12), Pearson r plus a candidate-identification rank, is standard. The single-trial word readout overreaches: one participant, 47 candidates from one speaker, a median rank of 0.76 rather than an accuracy, and smoothing tuned with no stated selection data. The paper reports no listener test; [later] work made its linear spectrogram design the baseline and beat it by 67% in listener digit accuracy with vocoder-parameter targets [[4]](#ref-4).

## Against the field, component by component

### M06 Processing and decoding: what is reconstructed

**Usual approach:** in 2012 there was none for this task: the 2 hits first public before 2012 among 64 heard-speech reconstruction studies are behavioural (pattern match, Appendix). Chang et al. classified single-trial pSTG responses in four listening patients [[2]](#ref-2); Guenther et al. predicted two formants with a Kalman filter from attempted speech [[3]](#ref-3). The authors credit linear spectrogram reconstruction to non-human work (refs 14, 15, Results). Across all years the spectrogram target is the usual design (24 of 64, pattern match); the paper adds a 60-channel rate-scale modulation target.

**State of the art:** Akbari et al. (2019) [later] crossed linear regression and deep networks with auditory-spectrogram and vocoder targets in five ECoG patients; the network-vocoder pair reached 75% listener digit accuracy, 67% above linear regression to the auditory spectrogram, on digits and speakers absent from training [[4]](#ref-4). The target's linear design is that baseline.

The protocol supports a representation claim: both targets share partitions, the nonlinear model wins across 15 participants, gaining at fast rates (interaction F(5,70) = 3.33), and it exceeds spectrogram reconstruction at 16 Hz and above for all scales (Figure S3), where the linear model stays near r = 0.10. Weak points: no overall r for the modulation model, 3 resamples against 10, and audio only via phase retrieval, which the authors say is imperfect. The modulation target recurs in 6 ledger keys, 4 distinct studies, the others [later], including Martin et al. [[5]](#ref-5); spectrogram (24) and vocoder targets (13 of 64) carried the field. Verdict: ahead for its time.

### M12 Evaluation: correlation plus identification rank

**Usual approach:** the 173-study reconstruction population has 2 hits before 2012, a review and a phoneme classifier, so no evaluation to follow (pattern match, Appendix). Correlation is the default across years (122 of 173), identification among candidates rare (20); the paper uses both.

**State of the art:** Berezutskaya et al. (2023) [later] classify 12 produced words from reconstructed spectrograms at 92–100% against 8% chance in five subjects [[6]](#ref-6); for heard speech, Akbari et al. hold out items and speakers and test with listeners [[4]](#ref-4). Test words come from the same single-speaker set (leave-one-out, Results), and correlations lack a noise-ceiling correction because more than 5 repeats were generally unavailable, as the authors report. Verdict: standard; identification is run in one participant, so it is not repeated.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Clinical listening sessions | No separate training-time action | – | standard |
| M02 Training-only supervision | Heard stimulus as regression target | Paired stimulus target | – | standard |
| M03 Training and adaptation | Per-participant fit, 2.5–17.5 min | Per-subject training | – | standard |
| M04 Use-time action | Listening; three tasks pooled | Listening to presented speech | – | standard |
| M05 Sensors | Subdural ECoG, 4 or 10 mm grids, high gamma | Clinical ECoG grids | – | standard |
| M06 Processing and decoding | Linear spectrogram and modulation-energy targets | Spectrogram target, base 64, all years; none before 2012 (pattern match 24) | [[4]](#ref-4) (2019): 75% listener digit accuracy | ahead |
| M07 Lexicon and LM | No LM; 47-item closed set for testing | No LM, closed set | – | standard |
| M08 Output | Spectrogram or modulation features | Acoustic features | – | standard |
| M09 Confirmation | None (offline) | Offline study | – | not applicable |
| M10 Correction | None (offline) | Offline study | – | not applicable |
| M11 Reference construction | Presented stimulus as reference | Presented stimulus | – | standard |
| M12 Evaluation | Pearson r; rank among 47 words, one participant | Correlation, base 173, all years; none before 2012 (pattern match 122) | [[6]](#ref-6) (2023): 92–100% word ID, 12 words | standard |
| M13 Device and cost | Offline clinical recording | Offline clinical recording | – | standard |

## Where the claims outrun the evidence

- Word readout (Abstract): one 4-mm-grid participant, 47 words and pseudowords from one speaker, median rank 0.89 averaged and 0.76 single-trial against 0.5 chance (Figure 8). Rank 0.76 puts the correct word above about 35 of 46 alternatives (inference); it is not an identification rate. The 500 ms by 2 octave smoothing is the best-performing setting with no stated selection set (Figure 8).
- Intelligibility: the Abstract ties accuracy to the range critical for intelligibility through cited psychoacoustics; the authors concede single-trial reconstructions are generally not intelligible, and listener testing came later [[4]](#ref-4).
- Electrode density (M05): r = 0.43 for 4-mm grids (N = 4) against 0.19 with five or fewer responsive electrodes (N = 6) (Figure 4C). The 4-mm and 3,052 Hz groups are both N = 4 with the same citation, so density likely travels with amplifier and sampling rate (inference).
- Pooling: mean r = 0.28 pools three tasks (5 participants each) and word and sentence sets, with no per-task mean (Figure 3).

## What the field needs next

- M06: spectrogram, modulation and vocoder targets compared by listener intelligibility in the same participants.
- M12: speaker-disjoint tests with a noise ceiling, and word identification in several participants with smoothing fixed on validation data.
- M05: grid density varied with amplifier and sampling rate fixed.

## Questions for the authors

- Were standardization statistics estimated on training partitions only?
- Which scheme, random trial subsampling or leave-one-word-out, produced each headline number?
- Are the 4-mm grid participants the four recorded at 3,052 Hz?
- How was the smoothing width chosen, which seeds drove the resamples, and how many sessions were recorded?

## Appendix: literature search

- **M06 / heard-speech-reconstruction-target-representation.** Inclusion rule: ledger text names intracranial or auditory-cortex recordings, a listening or perception condition, an acoustic representation and reconstruction, decoding or synthesis; design of interest: the reconstructed representation (spectrogram, temporal-modulation energy, envelope, vocoder parameters); production-only and encoding-only studies admitted by the pattern are counted but are not heard-speech reconstruction; design patterns overlap; versions count once. Ledger counts: slot-filled 7,345; pattern match 64 unique studies, plus 5 full-text-only folders. First public before 2012-01: 2 hits, both behavioural; neural reconstruction 0, spectrogram target 0, modulation target 0. All years: spectrogram target 24, vocoder parameters 13, envelope 12, temporal modulation 6 keys (4 distinct studies) (pattern match). Recall check: full-text pattern for modulation-energy reconstruction over the wiki, 8 folders, all target versions or [later] work; 5 recall-sample snippets read. Read in full: [[2]](#ref-2), [[3]](#ref-3), [[4]](#ref-4). Known-item recall 1.0 (3 seeds).
- **M12 / neural-speech-reconstruction-identification-test** (published table, reused). Inclusion rule: studies that reconstruct a continuous acoustic speech representation from neural recordings and evaluate it; design categories correlation, identification among candidates, mel-cepstral distortion, listening test, STOI, overlapping. Ledger counts: slot-filled 6,960; pattern match 173 unique studies; correlation 122, listening test 45, mel-cepstral distortion 31, STOI 23, identification among candidates 20. First public before 2012-01: 2 hits (a review and a phoneme classifier), reconstruction evaluations 0. Read for the table: [[6]](#ref-6). Known-item recall 0.67.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Pasley, B. N., David, S. V., Mesgarani, N., Flinker, A., Shamma, S. A., Crone, N. E., et al. “Reconstructing Speech from Human Auditory Cortex.” *PLoS Biology*, 2012, 10(1), e1001251. doi:[10.1371/journal.pbio.1001251](https://doi.org/10.1371/journal.pbio.1001251). Target. Read as the published article. [wiki: doi-10.1371-journal.pbio.1001251](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1371-journal.pbio.1001251/article.md) [wiki: pmc-3269422-pasley](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3269422-pasley/article.md) [wiki: pmc-3269422-speechrecon](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3269422-speechrecon/article.md)
2. <a id="ref-2"></a>Chang, E. F., Rieger, J. W., Johnson, K., Berger, M. S., Barbaro, N. M., Knight, R. T. “Categorical Speech Representation in Human Superior Temporal Gyrus.” *Nature Neuroscience*, 2010, 13(11), 1428-1432. doi:[10.1038/nn.2641](https://doi.org/10.1038/nn.2641). Prior; deciding prior for M06 (pSTG ECoG, passive listening, classification, no reconstruction). [wiki: pmc-2967728-categoricalstg](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2967728-categoricalstg/article.md)
3. <a id="ref-3"></a>Guenther, F. H., Brumberg, J. S., Wright, E. J., Nieto-Castanon, A., Tourville, J. A., Panko, M., et al. “A Wireless Brain-Machine Interface for Real-Time Speech Synthesis.” *PLoS ONE*, 2009, 4(12), e8218. doi:[10.1371/journal.pone.0008218](https://doi.org/10.1371/journal.pone.0008218). Prior; deciding prior for M06 (attempted production, Kalman-filter formant decoding). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-wireless-brain-machine-interface-for-real-time-speech-synthesis) [wiki: pmc-2784218-wireless](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wireless/article.md)
4. <a id="ref-4"></a>Akbari, H., Khalighinejad, B., Herrero, J. L., Mehta, A. D., Mesgarani, N. “Towards reconstructing intelligible speech from the human auditory cortex.” *Scientific Reports*, 2019, 9, 874. doi:[10.1038/s41598-018-37359-z](https://doi.org/10.1038/s41598-018-37359-z). Later; state of the art for M06 (heard-speech reconstruction judged by listeners). [later] [wiki: doi-10.1038-s41598-018-37359-z](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41598-018-37359-z/article.md) [wiki: pmc-6351601-audrecon](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-6351601-audrecon/article.md) [wiki: pmc-6351601-intelligible](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-6351601-intelligible/article.md)
5. <a id="ref-5"></a>Martin, S., Brunner, P., Holdgraf, C., Heinze, H., Crone, N. E., Rieger, J., et al. “Decoding spectrotemporal features of overt and covert speech from the human cortex.” *Frontiers in Neuroengineering*, 2014, 7, 14. doi:[10.3389/fneng.2014.00014](https://doi.org/10.3389/fneng.2014.00014). Later; reuses the modulation-based reconstruction model. [later] [wiki: doi-10.3389-fneng.2014.00014](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fneng.2014.00014/article.md) [wiki: pmc-4034498-overtcovert](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-4034498-overtcovert/article.md) [wiki: pmc-4034498-spectemp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-4034498-spectemp/article.md)
6. <a id="ref-6"></a>Berezutskaya, J., Freudenburg, Z. V., Vansteensel, M. J., Aarnoutse, E. J., Ramsey, N. F., van Gerven, M. A. J. “Direct speech reconstruction from sensorimotor brain activity with optimized deep learning models.” *Journal of Neural Engineering*, 2023, 20, 056010. doi:[10.1088/1741-2552/ace8be](https://doi.org/10.1088/1741-2552/ace8be). Later; state of the art of the published M12 table. [later] [wiki: doi-10.1088-1741-2552-ace8be](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552-ace8be/article.md) [wiki: pmc-10510111-berezutskaya](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10510111-berezutskaya/article.md) [wiki: pmc-10510111-recon](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10510111-recon/article.md)
