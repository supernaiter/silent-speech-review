# Decoding spoken phonemes from sensorimotor cortex with High-Density ECoG grids

Ramsey, Salari, Aarnoutse, Vansteensel, Bleichner, Freudenburg. NeuroImage 180(Pt A):301–311, 2018 (online 2017). [doi:10.1016/j.neuroimage.2017.10.011](https://doi.org/10.1016/j.neuroimage.2017.10.011)

## Verdict

The paper [[1]](#ref-1) changes the decoder (M06), and it is standard: correlation with class-mean spatiotemporal templates is the classifier the same group published for hand gestures on HD-ECoG [[2]](#ref-2). Its sensors (M05) are standard: micro- or HD arrays appear in 4 of 17 earlier intracranial speech decoders (pattern match, Appendix), and the credit to HD grids rests on no density test (Sec. 3.2). Evaluation (M12) is standard for 2017. The strongest confound is timing: trials are aligned to audio-marked voice onset (Sec. 2.2), and the group's gesture paper names systematic onset differences between classes as a source of inflated accuracy [[2]](#ref-2). The 12-point temporal gain is significant for five classes only (p=0.046). The pre-onset result does not separate decoding from sensory feedback, since plosive closure precedes voice onset (inference).

## Against the field, component by component

### M06 Processing and decoding: spatiotemporal template correlation

**Usual approach:** 15 of 17 intracranial speech decoders first public before 2017-04 train a discriminative, generative or regression decoder (pattern match, Appendix), for example LDA over time bins [[3]](#ref-3); Kellis et al. alone use a nearest centroid [[4]](#ref-4). The target picks the best-correlated class-mean HFB trace, with no fitted weights (Sec. 2.4).

**State of the art:** Zhao et al. (2026) [later], median 78.3% overt and 80.4% imagined syllables (six or eight classes) from 256-channel HD-ECoG in nine participants [[5]](#ref-5), against the target's 71.9% on four phonemes (empirical chance 29.4%).

Branco et al. built one channels-by-time template per gesture, labelled each left-out trial by highest Pearson correlation, on 3-mm HD grids in five patients (76.25% over S1, four gestures), and claimed temporal features add information beyond spatial ones [[2]](#ref-2). The target repeats both for phonemes and cites that paper only for alignment (Sec. 4). A linear SVM matches it (77.2% and 72.9%; p>0.3, Sec. 3.1). Verdict: standard.

### M05 Sensors: electrode scale

**Usual approach:** clinical grids at 4–10 mm or 1 cm in 11 of 17 prior studies, intracortical or depth microelectrodes in 4 (pattern match, Appendix), for example 1-cm grids [[3]](#ref-3); the target uses 3–4 mm grids, 32–72 analysed electrodes (Sec. 2.1).

**State of the art:** Duraivel et al. (2023) [later] decode nine-way phonemes up to 57% (chance 11.11%) from micro-ECoG in four patients; subsampled to standard spacing, median accuracy falls to 20-35% [[6]](#ref-6).

Kellis et al. used 1-mm micro-ECoG for words [[4]](#ref-4). "The high classification scores are likely to be enabled by the use of high density grids, and by the use of discrete phonemes" (Abstract) is untested: no density manipulation is reported (Sec. 3.2). Verdict: standard.

### M12 Evaluation: trial-level leave-one-out

**Usual approach:** within-subject k-fold cross-validation in 12 of 17 prior studies, leave-one-out in 2, held-out session or subject in none (pattern match, Appendix); Mugler et al. shuffled labels 100 times for chance [[3]](#ref-3). The target uses leave-one-trial-out and 500 label shuffles (120 for the SVM), as 5 of 17 priors shuffle labels.

**State of the art:** leave-one-subject-out testing, PCC 0.765 on unseen participants, Chen et al. (2024) [later] [[7]](#ref-7). Verdict: standard for 2017.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Same cued runs as test | No separate action | – | standard |
| M02 Training-only supervision | None; acoustically verified cue labels | None | – | standard |
| M03 Training and adaptation | Per-participant templates | Per-subject training | – | standard |
| M04 Use-time action | Overt isolated phonemes or rest | Overt speech | – | standard |
| M05 Sensors | HD-ECoG, 3–4 mm, 32–72 electrodes | Clinical grid, base 17 prior studies (pattern match 11) | [[6]](#ref-6) (2023): 57%, nine-way, micro-ECoG | standard |
| M06 Processing and decoding | Spatiotemporal template correlation | Trained decoder, base 17 prior studies (pattern match 15) | [[5]](#ref-5) (2026): 78.3% overt syllables, HD-ECoG | standard |
| M07 Lexicon and LM | Closed set, no LM | No LM, closed set | – | standard |
| M08 Output | Class label, offline | Class label | – | standard |
| M09 Confirmation | None (offline) | Offline study | – | not applicable |
| M10 Correction | None (offline) | Offline study | – | not applicable |
| M11 Reference construction | Cued label; VOT marked from audio | Prompt or hand labels | – | standard |
| M12 Evaluation | Leave-one-trial-out, permutation chance | k-fold CV, base 17 prior studies (pattern match 12) | [[7]](#ref-7) (2024): unseen subjects, PCC 0.765 | standard |
| M13 Device and cost | Clinical monitoring, offline | Offline clinical recording | – | standard |

## Where the claims outrun the evidence

- Timing (M06, M11). VOT was marked in Praat from audio (Sec. 2.2); for /p/ and /k/ it marks a burst after closure, for /u/ and /a:/ voicing onset (inference), so class-specific latencies enter the templates. Branco et al. say such systematic onset differences "may inflate classification" and align on the neural response instead [[2]](#ref-2). The gain from 63.5% to 75.5% (five classes, p=0.046) is 12.0 points, 19% relative (inference); 60.3% to 71.9% for four classes is not significant (p=0.064, Sec. 3.3).
- Feedback. The pre-onset window gives 64.0% (five classes, Sec. 4) and 58.3% (four phonemes, chance 28.8%, Table 2); the authors infer that "decoding does not depend entirely on sensory feedback", but plosive closure precedes voice onset in an overt task (inference).
- Acoustics. The 65–125 Hz band overlaps voice pitch (inference); microphonic contamination is not discussed (Sec. 1). Wilson et al. [later] found such artifacts in ECoG and intracortical recordings; removing them cut accuracy only from 29.3% to 25.8% [[8]](#ref-8). The post-onset window scores below the centred one (65.3% vs 72.4%, four classes, Table 2), against a sound-locked source (inference).
- Field comparison. Results "appear to exceed those of all studies we are aware of that specifically addressed decoding of generated phonemes from the sensorimotor region" (Sec. 4), which the authors qualify (Sec. 4). The five-class headline includes rest, which the SVM separates from speech at 92.8% (Table 2).

## What the field needs next

- M06/M11: align on the HFB response as in [[2]](#ref-2); re-test the temporal gain.
- M05: subsample the same HD grids to 1-cm spacing, as [[6]](#ref-6) did for micro-ECoG.
- M12: hold out runs, fit normalization on training trials, lead with four phonemes.
- M04: a mimed, soundless condition.

## Questions for the authors

- Were templates and run-wise z-scores computed without the held-out trial?
- How many runs per participant, and were trials of one run split across training and test?
- What is the mean cue-to-VOT latency per phoneme, and does STMF accuracy survive alignment on the HFB response?
- Which seeds drew the shuffles and random subsets?

## Appendix: literature search

- **Setting (all topics).** Ledger pattern of the published M12 partition topic (intracranial signal and speech unit in the ledger text), 618 unique studies; first public before 2017-04, screened by title and methods snippet: population 17 unique studies (versions merged; reviews, listening, mapping without decoder and non-speech BCIs excluded). 2017-04 to 2018-04 is [concurrent].
- **M06 / intracranial-speech-classifier-family.** Inclusion rule: setting above; design of interest: trial assigned to the best-correlated or nearest class-mean spatiotemporal template versus a trained discriminative, generative or regression decoder. Counts: slot-filled 7,345; pattern match 618 unique studies; population 17; trained decoder 15, nearest centroid 1, online power-threshold control 1; outside speech, the same group's gesture template classifier [[2]](#ref-2). Read in full: [[2]](#ref-2), [[4]](#ref-4), [[3]](#ref-3), [[5]](#ref-5). Known-item recall 1.0 (7 target-cited decoders).
- **M05 / intracranial-speech-electrode-scale** (published table, reused). Inclusion rule: published rule, decoder requirement kept. Counts: slot-filled 7,329; pattern match 618 unique studies; population 17; clinical grids 11, intracortical or depth 4, micro- or HD-ECoG in at least one participant 4 (only micro- or HD 2). Read in full: [[4]](#ref-4), [[3]](#ref-3), [[2]](#ref-2), [[6]](#ref-6). Known-item recall 1.0.
- **M12 / intracranial-speech-test-partition** (published table, reused). Inclusion rule: published rule. Counts: slot-filled 6,960; pattern match 618 unique studies; population 17; k-fold 12, leave-one-out 2, random holdout 1, jackknife 1, online closed loop 1, held-out session 0, held-out subject 0; label permutation for chance 5. Read in full: [[3]](#ref-3), [[7]](#ref-7). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [decoding-spoken-phonemes-from-sensorimotor-cortex-with-high-density-ecog-grids.bib](decoding-spoken-phonemes-from-sensorimotor-cortex-with-high-density-ecog-grids.bib).

1. <a id="ref-1"></a>Ramsey, N., Salari, E., Aarnoutse, E., Vansteensel, M., Bleichner, M., Freudenburg, Z. “Decoding spoken phonemes from sensorimotor cortex with High-Density ECoG grids.” *NeuroImage*, 2018, 180(Pt A), 301-311. doi:[10.1016/j.neuroimage.2017.10.011](https://doi.org/10.1016/j.neuroimage.2017.10.011). Target. Read as the PMC author manuscript (PMC6433278); online 2017-10-07. [wiki: doi-10.1016-j.neuroimage.2017.10.011](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1016-j.neuroimage.2017.10.011/article.md) [wiki: pmc-6433278-hdecog](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-6433278-hdecog/article.md)
2. <a id="ref-2"></a>Branco, M., Freudenburg, Z., Aarnoutse, E., Bleichner, M., Vansteensel, M., Ramsey, N. “Decoding hand gestures from primary somatosensory cortex using high-density ECoG.” *NeuroImage*, 2017. doi:[10.1016/j.neuroimage.2016.12.004](https://doi.org/10.1016/j.neuroimage.2016.12.004). Prior; deciding prior for M06 (same group; spatiotemporal template correlation, leave-one-out, 3-mm HD grids, hand gestures). [wiki: pmc-5322832-s1ecog](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-5322832-s1ecog/article.md)
3. <a id="ref-3"></a>Mugler, E. M., Patton, J. L., Flint, R. D., Wright, Z. A., Schuele, S. U., Rosenow, J., et al. “Direct classification of all American English phonemes using signals from functional speech motor cortex.” *Journal of Neural Engineering*, 2014, 11(3), 035015. doi:[10.1088/1741-2560/11/3/035015](https://doi.org/10.1088/1741-2560/11/3/035015). Prior; LDA over time bins, 1-cm grids, 10-fold cross-validation. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/direct-classification-of-all-american-english-phonemes-using-signals-from-functional-speech-motor-co) [wiki: doi-10.1088-1741-2560-11-3-035015](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2560-11-3-035015/article.md) [wiki: pmc-4097188-mugler](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-4097188-mugler/article.md)
4. <a id="ref-4"></a>Kellis, S., Miller, K., Thomson, K., Brown, R., House, P., Greger, B. “Decoding spoken words using local field potentials recorded from the cortical surface.” *Journal of Neural Engineering*, 2010, 7(5), 056007. doi:[10.1088/1741-2560/7/5/056007](https://doi.org/10.1088/1741-2560/7/5/056007). Prior; nearest-centroid word classifier on 1-mm micro-ECoG. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/decoding-spoken-words-using-local-field-potentials-recorded-from-the-cortical-surface) [wiki: doi-10.1088-1741-2560-7-5-056007](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2560-7-5-056007/article.md) [wiki: pmc-2970568-lfpwords](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2970568-lfpwords/article.md)
5. <a id="ref-5"></a>Zhao, Z., Wang, Z., Liu, Y., Qian, Y., Yin, Y., Gao, X., et al. “A neural architecture for imagined and overt speech motor dynamics.” *Nature Neuroscience*, 2026. doi:[10.1038/s41593-026-02456-0](https://doi.org/10.1038/s41593-026-02456-0). Later; state of the art for M06 (overt and imagined syllables, 256-channel HD-ECoG). [later] [wiki: natneuro-02456-motordyn](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/natneuro-02456-motordyn/article.md)
6. <a id="ref-6"></a>Duraivel, S., Rahimpour, S., Chiang, C., Trumpis, M., Wang, C., Barth, K., et al. “High-resolution neural recordings improve the accuracy of speech decoding.” *Nature Communications*, 2023, 14, 6938. doi:[10.1038/s41467-023-42555-1](https://doi.org/10.1038/s41467-023-42555-1). Later; state of the art for M05 (micro-ECoG phonemes; subsampling to standard spacing). [later] [wiki: doi-10.1038-s41467-023-42555-1](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41467-023-42555-1/article.md) [wiki: pmc-10628285-uecog](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10628285-uecog/article.md)
7. <a id="ref-7"></a>Chen, J., Chen, X., Wang, R., Le, C., Khalilian-Gourtani, A., Jensen, E., et al. “Subject-Agnostic Transformer-Based Neural Speech Decoding from Surface and Depth Electrode Signals.” *bioRxiv*, 2024. doi:[10.1101/2024.03.11.584533](https://doi.org/10.1101/2024.03.11.584533). Later; state of the art for M12 (leave-one-subject-out). [later] [wiki: doi-10.1101-2024.03.11.584533](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2024.03.11.584533/article.md)
8. <a id="ref-8"></a>Wilson, G. H., Stavisky, S. D., Willett, F. R., Avansino, D. T., Kelemen, J. N., Hochberg, L. R., et al. “Decoding spoken English from intracortical electrode arrays in dorsal precentral gyrus.” *Journal of Neural Engineering*, 2020, 17(6), 066007. doi:[10.1088/1741-2552/abbfef](https://doi.org/10.1088/1741-2552/abbfef). Later; microphonic contamination measured in intracortical and ECoG recordings during overt speech. [later] [wiki: doi-10.1088-1741-2552-abbfef](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552-abbfef/article.md)
