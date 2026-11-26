# Word pair classification during imagined speech using direct brain recordings

Martin, Brunner, Iturrate, Millán, Schalk, Knight, Pasley. Scientific Reports 6, 25803 (2016). DOI: [10.1038/srep25803](https://doi.org/10.1038/srep25803).

## Verdict

The paper changes two components of intracranial imagined-speech decoding [[1]](#ref-1). Whole-word identity as the decoded unit (M08) is ahead: none of the 4 earlier intracranial imagined-speech decoders classifies words (Appendix), and imagined word pairs beat chance in 4 of 5 subjects. DTW inside the SVM kernel (M06) is new in this population (Appendix) but standard by rule, because its gain is reported only as an unpaired test with no stated unit or size. The test partition (M12) is the usual within-participant cross-validation. The strongest confound is the heard word: the imagery epoch follows the auditory stimulus, and no same-delay epoch without imagery separates imagery from its trace. The "first demonstration of single-trial neural decoding of words during imagined speech" holds only for intracranial recordings; Suppes et al. recognised single internal-speech trials from scalp EEG/MEG in 1997 [[2]](#ref-2).

## Against the field, component by component

### M08 Output: whole-word identity from imagined speech

**Usual approach:** 3 of 4 prior intracranial imagined-speech decoders output sub-word classes (confirmed, Appendix): imagined phoneme versus rest [[3]](#ref-3), vowel or consonant classes inside imagined words [[4]](#ref-4), covert vowels [[5]](#ref-5); the fourth reconstructs spectrotemporal features [[6]](#ref-6). The paper classifies six whole words in 15 binary pairs.

**State of the art:** Kunz et al. (2025) [later] decode inner-speech sentences online from a 50-word vocabulary at 24%, 14% and 33% word error rate in three intracortical participants [[7]](#ref-7), a multiclass sequence task the binary design does not approach.

Within intracranial recordings the authors' first-demonstration claim holds: none of 44 full-text hits up to 2016 classifies imagined words besides the target (Appendix). The design repeats across subjects: significant in 4 of 5 subjects and 8 of 15 pairs after FDR correction [[1]](#ref-1). Verdict: ahead, for the unit, not the effect size, which the authors call small and likely not clinically significant.

### M06 Processing: temporal alignment inside the decoder

**Usual approach:** 3 of 4 priors feed time-averaged or fixed-window power without alignment (confirmed, Appendix) [[3]](#ref-3), [[4]](#ref-4), [[5]](#ref-5); Martin et al. use DTW only to score covert reconstructions [[6]](#ref-6). The paper puts per-electrode DTW distances into SVM kernels weighted by discriminative power.

**State of the art:** Zhao et al. (2026) [later] reach a median 80.4% on 6- or 8-class imagined syllables (9 participants, tenfold cross-validation) [[8]](#ref-8); the target's binary 57.7% against 50% chance is not on a common scale (inference).

The authors credit DTW kernels to speech recognition. Among 72 full-text DTW hits up to 2016, 8 use neural recordings and none other aligns imagined trials inside a decoder (Appendix). The gain rests on "p < 0.05; two-sample t-test" for overt and imagined speech, size in a supplementary figure, unit unstated [[1]](#ref-1); with and without DTW on the same pairs is a paired comparison (inference). Imagined epochs are fixed 1.5 s from cue onset, and the authors concede that cue timing limits accuracy and DTW degrades with noise. Verdict: standard.

### M12 Evaluation: within-participant leave-one-out

**Usual approach:** at the target's time 2 of 4 priors hold out covert trials within participant (confirmed, Appendix) [[4]](#ref-4), [[5]](#ref-5); none holds out a session or subject. The paper uses leave-one-out with one trial per class per fold and 1,000 label shuffles.

**State of the art:** Kunz et al. (2025) [later] test online on sentences absent from training blocks [[7]](#ref-7).

Usable trials per class and block grouping of folds are not stated [[1]](#ref-1). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Listen, imagine hearing, repeat aloud | Cued word or vowel repetition | – | standard |
| M02 Training-only supervision | Instructed word labels | Item labels | – | standard |
| M03 Training and adaptation | Per-subject offline training, inner LOO grid search | Per-participant offline | – | standard |
| M04 Use-time action | Imagine hearing the just-heard word | Cued imagery with paired overt condition | – | standard |
| M05 Sensors | Clinical ECoG, 5 patients, high gamma 70-150 Hz | Clinical ECoG, high-gamma power | – | standard |
| M06 Processing and decoding | Per-electrode DTW kernels in an SVM | Time-averaged or fixed-window power, no alignment, of 4 priors (confirmed 3) | [[8]](#ref-8) (2026): median 80.4%, 6- or 8-class imagined syllables | standard |
| M07 Lexicon and LM | None | None | – | standard |
| M08 Output | Whole-word identity, 15 binary pairs | Sub-word classes, of 4 priors (confirmed 3) | [[7]](#ref-7) (2025): online inner-speech sentences, 50-word WER 14-33% | ahead |
| M09 Confirmation | None | None | – | not applicable |
| M10 Correction | None | None | – | not applicable |
| M11 Reference construction | Instructed word identity, epochs at cue onset | Instructed labels | – | standard |
| M12 Evaluation | Within-subject leave-one-out, 1,000 label shuffles | Within-participant held-out covert trials, of 4 priors (confirmed 2) | [[7]](#ref-7) (2025): online test, sentences absent from training blocks | standard |
| M13 Device and cost | Clinical implants, offline | Clinical implants | – | standard |

## Where the claims outrun the evidence

- Suppes et al. recognised single internal-speech trials of 7 words at 46%, 39% and 43% in three 105-trial blocks for one subject, with prototypes from the same data [[2]](#ref-2); "neural decoding of words" covers it, and the target cites neither it nor Leuthardt et al. [[3]](#ref-3).
- No listen-then-rest epoch or rest-label classification is reported [[1]](#ref-1). Temporal electrodes alone give 58.0% against 57.7% for all; the authors read this as STG driving imagery, but a trace of the just-heard word fits equally (inference).
- The abstract's 88% is one pair in one subject; the group mean is 57.7% [[1]](#ref-1).
- Stimuli vary in syllable count, yet accuracy is not related to length or duration, and the passing imagined pairs are not named [[1]](#ref-1).

## What the field needs next

- M04/M11: a same-delay no-imagery condition classified with the identical pipeline.
- M06: per-subject paired tests of DTW against fixed-window kernels on imagined trials with a measured imagery onset.
- M08/M12: multiclass word sets on held-out sessions [[7]](#ref-7).

## Questions for the authors

- What are per-subject accuracies with and without DTW?
- How many imagined trials per class remained, and how many electrodes per subject?
- Which imagined pairs passed, and do they differ in syllable count?
- Were folds grouped by recording block?

## Appendix: literature search

Population for all three topics: human intracranial (ECoG, sEEG, depth, intracortical) decoders of imagined, covert or inner speech; attempted speech decoded from unit firing, scalp EEG/MEG, listening-only reconstruction, overt-only studies, analyses without a decoder and reviews are outside; versions count once. Priors: first public before 2015-11. Pattern-match studies first public up to 2015: 8 unique; excluded listening-only (2), no decoder (1), overt-only (1), leaving 4 decoders, all read in full: [[3]](#ref-3), [[4]](#ref-4), [[6]](#ref-6), [[5]](#ref-5).

M06, topic intracranial-imagined-speech-decoder-time-alignment. Inclusion rule: the population above; design of interest is how the decoder handles trial timing variability (time-averaged or fixed-window features, lagged linear model, HMM, or alignment such as DTW inside the classifier); DTW used only for scoring counts as evaluation. Ledger counts: slot-filled 7,345 unique studies; pattern match 89 unique studies (all years). Usual design at the target's time: time-averaged or fixed-window power without alignment 3 of 4; lagged linear model 1 of 4; alignment inside the decoder 0 of 4 (confirmed). All-years full-text pattern counts over the 89 studies, mentions included: DTW or time warping 23, hidden Markov model 17, lagged or temporal receptive field 12. Full-text DTW check (DTW or time-warp terms with EEG, ECoG, MEG, cortical or EMG terms; whole wiki, first public up to 2016): 72 unique studies, 8 with neural recordings including the target; none other uses temporal alignment inside an imagined- or covert-speech decoder. Read in full: the 4 priors and [[8]](#ref-8). Known-item recall 1.0 (5 of 5 seeds).

M08, topic intracranial-imagined-speech-output-unit. Inclusion rule: the population above; design of interest is the decoded unit of imagined trials (task versus rest, phoneme, vowel or consonant class, whole word, continuous acoustic features, sentence text); sub-word units classified inside word stimuli count as sub-word output. Ledger counts: slot-filled 3,268 unique studies; pattern match 89 unique studies. Usual design at the target's time: sub-word class 3 of 4; continuous spectrotemporal features 1 of 4; whole-word identity 0 of 4 (confirmed). All-years full-text pattern counts, mentions included: continuous spectrotemporal output 51, vowel, phoneme or syllable classes 43, whole-word classification 20. Full-text check (intracranial terms, imagined, covert, inner or silent speech terms, and word classification terms; whole wiki, first public up to 2016): 44 unique studies, no intracranial imagined-word classifier besides the target. Read in full: the 4 priors, [[2]](#ref-2) (outside the population) and [[7]](#ref-7). Known-item recall 1.0 (5 of 5 seeds).

M12, topic intracranial-imagined-speech-test-partition (published table, appended). Inclusion rule: the population above; design of interest is how test data are separated from training data. Ledger counts: slot-filled 6,960 unique studies; pattern match 89 unique studies. Usual design at the target's time: within-participant held-out covert trials 2 of 4; overt-trained model tested on covert trials 1 of 4; online test after screening 1 of 4; held-out session or subject 0 of 4 (confirmed). Read in full: the 4 priors and [[7]](#ref-7). Known-item recall 1.0 (5 of 5 seeds).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Martin, S., Brunner, P., Iturrate, I., Millán, J. d. R., Schalk, G., Knight, R. T., et al. “Word pair classification during imagined speech using direct brain recordings.” *Scientific Reports*, 2016, 6, 25803. doi:[10.1038/srep25803](https://doi.org/10.1038/srep25803). Target. Read as the published Scientific Reports article (with the 2017 corrigendum notice). [wiki: doi-10.1038-srep25803](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-srep25803/article.md) [wiki: pmc-4863149-ecog-word-pairs](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-4863149-ecog-word-pairs/article.md) [wiki: pmc-pmc4863149](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-pmc4863149/article.md) [wiki: pmc-4863149-wordpair](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-4863149-wordpair/article.md)
2. <a id="ref-2"></a>Suppes, P., Lu, Z., Han, B. “Brain wave recognition of words.” *Proceedings of the National Academy of Sciences of the USA*, 1997, 94(26), 14965–14969. doi:[10.1073/pnas.94.26.14965](https://doi.org/10.1073/pnas.94.26.14965). Prior, not cited by the target; scalp EEG/MEG word recognition during internal speech, including single trials. Read in full. [wiki: pmc-25146-brainwave](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-25146-brainwave/article.md)
3. <a id="ref-3"></a>Leuthardt, E. C., Gaona, C., Sharma, M., Szrama, N., Roland, J., Freudenberg, Z., et al. “Using the electrocorticographic speech network to control a brain-computer interface in humans.” *Journal of Neural Engineering*, 2011, 8(3), 036004. doi:[10.1088/1741-2560/8/3/036004](https://doi.org/10.1088/1741-2560/8/3/036004). Prior, not cited by the target; online control with imagined phonemes versus rest; deciding prior for M06, M08 and M12. Read in full. [wiki: doi-10.1088-1741-2560-8-3-036004](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2560-8-3-036004/article.md)
4. <a id="ref-4"></a>Pei, X., Barbour, D., Leuthardt, E. C., Schalk, G. “Decoding Vowels and Consonants in Spoken and Imagined Words Using Electrocorticographic Signals in Humans.” *Journal of Neural Engineering*, 2011, 8(4), 046028. doi:[10.1088/1741-2560/8/4/046028](https://doi.org/10.1088/1741-2560/8/4/046028). Prior; vowel and consonant classes inside imagined words; deciding prior for M06, M08 and M12. Read in full. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/decoding-vowels-and-consonants-in-spoken-and-imagined-words-using-electrocorticographic-signals-in-h) [wiki: doi-10.1088-1741-2560-8-4-046028](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2560-8-4-046028/article.md) [wiki: pmc-3772685-vowelcons](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3772685-vowelcons/article.md)
5. <a id="ref-5"></a>Ikeda, S., Shibata, T., Nakano, N., Okada, R., Tsuyuguchi, N., Ikeda, K., et al. “Neural decoding of single vowels during covert articulation using electrocorticography.” *Frontiers in Human Neuroscience*, 2014, 8, 125. doi:[10.3389/fnhum.2014.00125](https://doi.org/10.3389/fnhum.2014.00125). Prior, cited by the target; linear SVM on covert vowels; deciding prior for M06, M08 and M12. Read in full. [wiki: doi-10.3389-fnhum.2014.00125](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnhum.2014.00125/article.md) [wiki: pmc-3945950-covertvowel](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3945950-covertvowel/article.md) [wiki: pmc-3945950-covertvowl](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3945950-covertvowl/article.md)
6. <a id="ref-6"></a>Martin, S., Brunner, P., Holdgraf, C., Heinze, H., Crone, N. E., Rieger, J., et al. “Decoding spectrotemporal features of overt and covert speech from the human cortex.” *Frontiers in Neuroengineering*, 2014, 7, 14. doi:[10.3389/fneng.2014.00014](https://doi.org/10.3389/fneng.2014.00014). Prior; lagged linear reconstruction of covert speech, DTW used only for scoring; deciding prior for M06, M08 and M12. Read in full. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/decoding-spectrotemporal-features-of-overt-and-covert-speech-from-the-human-cortex) [wiki: doi-10.3389-fneng.2014.00014](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fneng.2014.00014/article.md) [wiki: pmc-4034498-overtcovert](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-4034498-overtcovert/article.md) [wiki: pmc-4034498-spectemp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-4034498-spectemp/article.md)
7. <a id="ref-7"></a>Kunz, E. M., Krasa, B. A., Kamdar, F., Avansino, D., Hahn, N., Yoon, S., et al. “Inner speech in motor cortex and implications for speech neuroprostheses.” *Cell*, 2025, 188(17), 4658–4673.e17. doi:[10.1016/j.cell.2025.06.015](https://doi.org/10.1016/j.cell.2025.06.015). Later; state of the art for M08 and M12. Read for the reported values. [later] [wiki: doi-10.1016-j.cell.2025.06.015](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1016-j.cell.2025.06.015/article.md) [wiki: cell-40816265-innersp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cell-40816265-innersp/article.md) [wiki: pmc-12360486-inner-motor](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12360486-inner-motor/article.md) [wiki: pmc-12360486-innercell](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12360486-innercell/article.md) [wiki: pmc-12360486-innermtrcx](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12360486-innermtrcx/article.md)
8. <a id="ref-8"></a>Zhao, Z., Wang, Z., Liu, Y., Qian, Y., Yin, Y., Gao, X., et al. “A neural architecture for imagined and overt speech motor dynamics.” *Nature Neuroscience*, 2026. doi:[10.1038/s41593-026-02456-0](https://doi.org/10.1038/s41593-026-02456-0). Later; state of the art for M06. Read for the reported value. [later] [wiki: natneuro-02456-motordyn](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/natneuro-02456-motordyn/article.md)
