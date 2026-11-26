# Direct classification of all American English phonemes using signals from functional speech motor cortex

Mugler, Patton, Flint, Wright, Schuele, Rosenow, Shih, Krusienski, Slutzky. Journal of Neural Engineering 11(3):035015, 2014. [doi:10.1088/1741-2560/11/3/035015](https://doi.org/10.1088/1741-2560/11/3/035015)

## Verdict

The paper [[1]](#ref-1) changes one component: its decoder (M06) classifies phonemes across the General American inventory as events inside spoken words, aligned to hand-labelled phoneme onsets, on ECoG. Against the field of its time this is standard, not ahead: 8 of 11 earlier intracranial speech-unit studies name small subsets of two to six units, but full-inventory classification already existed in Brumberg et al., 38 attempted phonemes at 16–21% against 2.6% chance from an intracortical implant [[2]](#ref-2) (Appendix). The authors' own "first" is scoped to ECoG and holds against the read ECoG priors, which classified four vowels or four phonemes [[3]](#ref-3), [[4]](#ref-4) (Appendix). The headline overreaches: the abstract's "up to 36% accuracy when classifying all phonemes" is subject NU2's consonant accuracy (36.1%, Sec. 3.1), vowels and consonants were classified separately, and every analysed phoneme, test trials included, sits on an onset placed by hand from the microphone (Sec. 2.4). What the paper does establish is that onset precision governs phoneme decoding (Sec. 3.1); Wilson et al. [later] used the same within-word, hand-labelled protocol on 39 phonemes [[5]](#ref-5).

## Against the field, component by component

### M06 Processing and decoding: full phoneme inventory, onset-aligned

**Usual approach:** before 2013-11, 8 of 11 intracranial speech-unit studies name small subsets of two to six phonemes, vowels or syllables (pattern match, Appendix); the read ECoG decoders classified four vowels or nine consonant-pair groups at word level, 40.7±2.7% overt vowel accuracy against 25% chance [[3]](#ref-3), or four phonemes as cursor-control screening [[4]](#ref-4). The paper departs by classifying each phoneme as an event at its own onset, with LDA on 140 ANOVA-ranked features (Sec. 2.4–2.5); onsets were marked by hand from the microphone (Sec. 2.4).

**State of the art:** Willett et al. (2023) [later] classify 39 attempted isolated phonemes at 62% with naive Bayes on 1 s of intracortical population activity, one participant [[6]](#ref-6). Inside spoken words, with hand-labelled onsets as here, Wilson et al. (2020) [later] reach 33.9% on 39 phonemes (chance 6%) [[5]](#ref-5).

One prior of 11 has the full inventory, Brumberg et al. (Appendix), so the verdict is standard. The accuracy comparison favours no one: the target's 20.4±9.8% mean against 7.4% shuffled chance is about 2.8 times chance, Brumberg's 16–21% is about 6–8 times 2.6% chance, and Wilson's 33.9% about 5.7 times 6% (inference); class counts, isolated versus in-word production and chance definitions differ, so these ratios are not evidence of a gap. The paper does not state the vowel or total class count (only 24 consonants, Sec. 3.1). Its lasting result is onset sensitivity: Gaussian onset noise with a 100-ms standard deviation, below the 176-ms mean phoneme length, sharply lowers accuracy (Sec. 3.1), which Wilson et al. restate [[5]](#ref-5).

### M12 Evaluation: repeated within-subject folds

**Usual approach:** k-fold cross-validation, named by 9 of 34 intracranial speech studies up to 2013 and 132 of 618 across years (pattern match, Appendix); the paper averages five repetitions of ten-fold cross-validation within each subject and builds chance from 100 label shuffles (Sec. 2.5).

**State of the art:** leave-one-subject-out testing, PCC 0.765 on unseen participants, Chen et al. (2024) [later] [[7]](#ref-7). Verdict: standard for 2014, with no held-out session, subject or word.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Same prompted word runs as test | No separate training-time action | – | standard |
| M02 Training-only supervision | None; labels from words via CMU dictionary | No training-only signal | – | standard |
| M03 Training and adaptation | ANOVA ranking, 140 features, peak tuning | Per-subject training | – | standard |
| M04 Use-time action | Overt reading of 320 monosyllabic words | Overt word production | – | standard |
| M05 Sensors | Clinical ECoG grids, high-gamma, mu, beta, LMP | Clinical ECoG grids | – | standard |
| M06 Processing and decoding | Full inventory, onset-aligned LDA | 2-6-unit subset, base 11 prior studies (pattern match 8) | [[6]](#ref-6) (2023): 39 phonemes, 62% | standard |
| M07 Lexicon and LM | None; optional stimulus-list constraint | No LM, closed set | – | standard |
| M08 Output | Phoneme class label | Class label | – | standard |
| M09 Confirmation | None (offline) | Offline study | – | not applicable |
| M10 Correction | None (offline) | Offline study | – | not applicable |
| M11 Reference construction | Hand-labelled onsets from microphone | Hand or prompt labels | – | standard |
| M12 Evaluation | 5 x 10-fold CV within subject, shuffled chance | k-fold CV, base 34 studies to 2013 (pattern match 9) | [[7]](#ref-7) (2024): leave-one-subject-out, PCC 0.765 | standard |
| M13 Device and cost | Bedside clinical ECoG, offline, no code | Offline clinical recording | – | standard |

## Where the claims outrun the evidence

- "All phonemes". The abstract's 36% is a consonant result (Sec. 3.1), and with vowels and consonants classified separately (Sec. 3.1) the 20.4% mean pools two classifiers; NU2's 72.3% uses only the four most frequent phonemes (Sec. 3.1).
- Oracle segmentation. Windows span 300 ms around hand-labelled onsets for every analysed phoneme (Sec. 2.4). The authors concede they are "not strictly decoding words" and that real-time use needs an onset detector (Sec. 4); the 3.0 bits/s, 33.6 words/min rate is for a hypothetical BCI (Sec. 3.3), not comparable with the 2.1 bits/s cited for the best communication BCI (Sec. 1).
- Selection optimism (M03). Features are ranked on training data, but the feature count was raised "until decoding performance reached a maximum" and peak-performance electrodes were excluded by significance, with no stated nesting (Sec. 2.5).
- Leakage. NU2 and NU3 repeated the first 160 words (Sec. 2.3), and the paper does not say folds were grouped by word (Sec. 2.5).
- Word identification, 14.8% rising to 18.8% when restricted to the 320 stimulus words, is for NU2 only (Sec. 3.3); the authors call it insufficient for communication (Sec. 4).

## What the field needs next

- M06: one classifier over the whole inventory with stated class counts, against Brumberg et al.'s 38-class design.
- M11/M06: onsets from a neural detector or forced aligner at test, reporting the drop from hand labels.
- M12: folds grouped by word and a held-out session.
- M03: feature count and electrode exclusion nested in training folds.

## Questions for the authors

- How many vowel classes, and how many classes in total, entered the all-phoneme result, and how was 20.4% pooled from the vowel and consonant classifiers?
- Were the feature count and electrode exclusions chosen within each training fold?
- Were label shuffles stratified, and was feature selection repeated per shuffle?
- What seeds produced the five fold repetitions?

## Appendix: literature search

- **M06 / intracranial-phoneme-inventory-classification.** Inclusion rule: ledger text names ECoG, sEEG, intracortical or Utah-array recording with phonemes, vowels, consonants or syllables (the population of the published topic intracranial-speech-unit-classification); design of interest: full phoneme inventory (38–44 classes) versus a subset of two to six units; listening, mapping and review papers stay in the count; versions count once. Ledger counts: slot-filled 7,345; pattern match 101 unique studies. First public before 2013-11: 11 unique studies; small subset 8, full inventory 1 (Brumberg 2011). [concurrent] and excluded: Ikeda et al. 2014 (three covert vowels), Toyoda et al. 2014 (44-phoneme mapping, no classifier). All years: small subset 54, full inventory 30 (pattern match, upper bounds). Read in full: [[2]](#ref-2), [[3]](#ref-3), [[4]](#ref-4), [[6]](#ref-6), [[5]](#ref-5). Known-item recall 1.0.
- **M12 / intracranial-speech-test-partition** (published table, reused). Inclusion rule: intracranial speech decoding studies; design of interest: how test data are separated from training data. Ledger counts: slot-filled 6,960; pattern match 618 unique studies; k-fold 132, held-out subject 28. Up to 2013: 34 unique studies (18 undated excluded), k-fold 9, random split 9, held-out session wording 5, held-out subject 0 (pattern match). Read in full: [[7]](#ref-7). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [direct-classification-of-all-american-english-phonemes-using-signals-from-functional-speech-motor-co.bib](direct-classification-of-all-american-english-phonemes-using-signals-from-functional-speech-motor-co.bib).

1. <a id="ref-1"></a>Mugler, E. M., Patton, J. L., Flint, R. D., Wright, Z. A., Schuele, S. U., Rosenow, J., et al. “Direct classification of all American English phonemes using signals from functional speech motor cortex.” *Journal of Neural Engineering*, 2014, 11(3), 035015. doi:[10.1088/1741-2560/11/3/035015](https://doi.org/10.1088/1741-2560/11/3/035015). Target. Read as the PMC author manuscript (PMC4097188), published in final form 19 May 2014. [wiki: doi-10.1088-1741-2560-11-3-035015](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2560-11-3-035015/article.md) [wiki: pmc-4097188-mugler](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-4097188-mugler/article.md)
2. <a id="ref-2"></a>Brumberg, J. S., Wright, E. J., Andreasen, D. S., Guenther, F. H., Kennedy, P. R. “Classification of Intended Phoneme Production from Chronic Intracortical Microelectrode Recordings in Speech-Motor Cortex.” *Frontiers in Neuroscience*, 2011, 5, 65. doi:[10.3389/fnins.2011.00065](https://doi.org/10.3389/fnins.2011.00065). Prior; deciding prior for M06 (38 attempted isolated phonemes, intracortical, one locked-in participant). [wiki: doi-10.3389-fnins.2011.00065](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnins.2011.00065/article.md) [wiki: pmc-3096823-phonintent](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3096823-phonintent/article.md) [wiki: pmc-3096823-phoneme-intracortical](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3096823-phoneme-intracortical/article.md)
3. <a id="ref-3"></a>Pei, X., Barbour, D., Leuthardt, E. C., Schalk, G. “Decoding Vowels and Consonants in Spoken and Imagined Words Using Electrocorticographic Signals in Humans.” *Journal of Neural Engineering*, 2011, 8(4), 046028. doi:[10.1088/1741-2560/8/4/046028](https://doi.org/10.1088/1741-2560/8/4/046028). Prior; deciding prior for M06 (four vowels or consonant-pair groups decoded at word level on ECoG). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/decoding-vowels-and-consonants-in-spoken-and-imagined-words-using-electrocorticographic-signals-in-h) [wiki: doi-10.1088-1741-2560-8-4-046028](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2560-8-4-046028/article.md) [wiki: pmc-3772685-vowelcons](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3772685-vowelcons/article.md)
4. <a id="ref-4"></a>Leuthardt, E. C., Gaona, C., Sharma, M., Szrama, N., Roland, J., Freudenberg, Z., et al. “Using the electrocorticographic speech network to control a brain-computer interface in humans.” *Journal of Neural Engineering*, 2011, 8(3), 036004. doi:[10.1088/1741-2560/8/3/036004](https://doi.org/10.1088/1741-2560/8/3/036004). Prior; deciding prior for M06 (four phonemes in ECoG screening for cursor control). [wiki: doi-10.1088-1741-2560-8-3-036004](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2560-8-3-036004/article.md)
5. <a id="ref-5"></a>Wilson, G. H., Stavisky, S. D., Willett, F. R., Avansino, D. T., Kelemen, J. N., Hochberg, L. R., et al. “Decoding spoken English from intracortical electrode arrays in dorsal precentral gyrus.” *Journal of Neural Engineering*, 2020, 17(6), 066007. doi:[10.1088/1741-2552/abbfef](https://doi.org/10.1088/1741-2552/abbfef). Later; same within-word, hand-labelled onset protocol on 39 phonemes. [later] [wiki: doi-10.1088-1741-2552-abbfef](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552-abbfef/article.md)
6. <a id="ref-6"></a>Willett, F. R., Kunz, E. M., Fan, C., Avansino, D. T., Wilson, G. H., Choi, E. Y., et al. “A high-performance speech neuroprosthesis.” *Nature*, 2023, 620, 1031-1036. doi:[10.1038/s41586-023-06377-x](https://doi.org/10.1038/s41586-023-06377-x). Later; state of the art for M06 (39 attempted isolated phonemes, 62%). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-high-performance-speech-neuroprosthesis) [wiki: doi-10.1038-s41586-023-06377-x](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-023-06377-x/article.md)
7. <a id="ref-7"></a>Chen, J., Chen, X., Wang, R., Le, C., Khalilian-Gourtani, A., Jensen, E., et al. “Subject-Agnostic Transformer-Based Neural Speech Decoding from Surface and Depth Electrode Signals.” *bioRxiv*, 2024. doi:[10.1101/2024.03.11.584533](https://doi.org/10.1101/2024.03.11.584533). Later; state of the art in the published M12 topic table (leave-one-subject-out test). [later] [wiki: doi-10.1101-2024.03.11.584533](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2024.03.11.584533/article.md)
