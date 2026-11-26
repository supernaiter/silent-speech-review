# Decoding Vowels and Consonants in Spoken and Imagined Words Using Electrocorticographic Signals in Humans

Pei, Barbour, Leuthardt, Schalk. Journal of Neural Engineering 8(4):046028, 2011. [doi:10.1088/1741-2560/8/4/046028](https://doi.org/10.1088/1741-2560/8/4/046028)

## Verdict

The paper [[1]](#ref-1) changes two components. Its use-time action (M04), covert repetition of the same 36 words that are also decoded overtly, recorded on clinical ECoG, was ahead of the 2011 field, where imagined speech was decoded from EEG and intracranial work used attempted or overt speech (Appendix). Its decoder (M06), one classifier per electrode with the best location reported, is standard for its time but departs from the joint multi-electrode input of earlier and later work. The overt result holds; the covert result rests on prompt-defined labels with no silence check and on the best of 47–64 electrodes, and selection inside the folds is not stated (M03), so the gains over 25% chance are upper bounds. Today the same paired design on high-density ECoG reaches 80.4% median imagined-syllable accuracy [[2]](#ref-2), so this paper is a feasibility result, not a benchmark.

## Against the field, component by component

### M04 Use-time action: covert words paired with overt words

**Usual approach:** before 2011, EEG appears in 10 of the 39 prior ledger studies on imagined-speech decoding (pattern match, Appendix); the read EEG prior classified imagined /ba/ and /ku/ rhythms in seven subjects with no overt condition [[3]](#ref-3). Intracranial priors decoded attempted speech in one locked-in volunteer [[4]](#ref-4) or overt words [[5]](#ref-5).

**State of the art:** Zhao et al. (2026) [later] record imagined and articulated syllables in nine participants on 256-channel high-density ECoG: 80.4% median imagined accuracy against 16.7% chance, 78.3% articulated [[2]](#ref-2). Kunz et al. (2025) [later] decode inner sentences from intracortical arrays in real time at 26%–54% WER with a 125,000-word vocabulary [[6]](#ref-6). The target's 37.5% covert vowel accuracy is 12.5 points over its 25% chance; Zhao et al. stand 63.7 points over theirs (inference); units, class counts and arrays differ.

None of the 39 prior studies has an ECoG decoder of imagined speech; the three that mention ECoG are overt mapping studies or a review (Appendix). Leuthardt et al. [concurrent] used imagined phonemes as cursor-control features, covertly in patients 3 and 4 [[7]](#ref-7). Covert accuracy is significant in 5/6 patients for vowels and 4/6 for consonants (Sec. 3.1). Verdict: ahead at the time. Kunz et al. find attempted speech better than inner speech in two of three participants [[6]](#ref-6), while this paper (Sec. 3.1) and Zhao et al. find covert close to overt.

### M06 Processing and decoding: one electrode at a time

**Usual approach:** the 2011 base is thin: 3 prior intracranial speech-unit studies, 2 decoding from several electrodes jointly (pattern match, Appendix); Kellis et al. decoded from single micro-electrodes and from concatenated features of all of them [[5]](#ref-5). The paper ranks features by MRMR per channel, feeds the top 35 (consonants) or 40 (vowels) to Naive Bayes, and reports the best location (Sec. 2.5).

**State of the art:** joint input now dominates, 78 of 96 studies in the topic across years (pattern match), and the best imagined-speech result (2026) feeds all encoding electrodes as channels [[2]](#ref-2). Verdict: standard. Per-electrode decoding suits mapping but caps accuracy, as the authors concede (Sec. 4).

### M12 Evaluation: within-patient folds

**Usual approach:** k-fold cross-validation, in 3 of 15 prior intracranial speech studies and 132 of 618 across years (pattern match, Appendix); the paper uses ten-fold cross-validation within each patient (Sec. 2.5).

**State of the art:** leave-one-subject-out testing, PCC 0.765 on unseen participants in Chen et al. (2024) [later] [[8]](#ref-8). Verdict: standard for 2011, with no held-out session or patient.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Same prompted runs as test | No separate training-time action | – | standard |
| M02 Training-only supervision | None; labels from displayed word | No training-only signal | – | standard |
| M03 Training and adaptation | Per-patient MRMR + feature count; nesting not stated | Per-subject training | – | not reported |
| M04 Use-time action | Covert word repetition, paired overt runs, same 36 words | EEG, no overt pairing (pattern match 10) | [[2]](#ref-2) (2026): 80.4% median imagined syllables, HD-ECoG | ahead |
| M05 Sensors | Clinical grids, 48 or 64 contacts | Clinical ECoG grids | – | standard |
| M06 Processing and decoding | Per-electrode MRMR + Naive Bayes, best location | Joint multi-electrode decoding (pattern match 2) | [[2]](#ref-2) (2026): multi-electrode input, 80.4% | standard |
| M07 Lexicon and LM | None | No LM, closed set | – | standard |
| M08 Output | Vowel or consonant-pair class | Class label | – | standard |
| M09 Confirmation | None (offline) | Offline study | – | not applicable |
| M10 Correction | None (offline) | Offline study | – | not applicable |
| M11 Reference construction | Covert labels = prompted word, no silence check | Prompt-defined labels | – | standard |
| M12 Evaluation | Ten-fold CV within patient, best location vs 25% chance | k-fold cross-validation (pattern match 3) | [[8]](#ref-8) (2024): leave-one-subject-out, PCC 0.765 | standard |
| M13 Device and cost | Bedside clinical ECoG, offline, no code | Offline clinical recording | – | standard |

## Where the claims outrun the evidence

- Selection. Each accuracy is the best of 47–64 electrodes (Sec. 2.3, 3.1), and whether MRMR ranking and the 35/40 feature counts were fixed inside training folds is not stated (Sec. 2.5); testing that maximum against 25% chance overstates a pre-specified electrode (inference).
- Covert labels are the prompt. The paper describes no check that patients imagined the word and stayed silent (Sec. 2.2–2.3); Zhao et al. checked with video and audio, adding EMG in S6–S9 [[2]](#ref-2).
- Inconsistencies. Overt-consonant significance is p<0.0022 in Sec. 3.1 and p<0.022 in Table 3; Fig. 5 labels z=2 as p=0.0023, while a one-sided z of 2 gives about 0.023 (inference).
- The overt-covert comparison (Sec. 3.1) sets eight overt patients against six covert ones.
- "Effective communication with only little training" (Sec. 4) has no online test; the imagined-vowel demonstration is one offline fold from subject D (Supplementary Material).

## What the field needs next

- M03: electrode and feature selection nested in each training fold.
- M04/M11: covert trials checked by EMG or audio, and an overt-trained decoder tested on covert trials.
- M06: joint decoding over responsive electrodes against the single best electrode on the same folds.
- M12: a held-out session test across the monitoring days.

## Questions for the authors

- Were MRMR ranking, feature counts and the best location chosen within each training fold?
- How were the folds formed (by trial or run, stratified), and with what seed?
- Were classifier features normalized on training folds only?
- Did the bootstrap test account for choosing the best of 47–64 electrodes?

## Appendix: literature search

- **M04 / covert-speech-decoding-with-paired-overt-condition.** Inclusion rule: ledger text names decoding, classification or recognition together with imagined, covert, inner or unspoken speech, any signal; design of interest: covert-trial decoding with an overt condition on the same items in the same participants from intracranial electrodes; attempted speech is a different action; versions count once. Ledger counts: slot-filled 5,595; pattern match 777 unique studies, plus 88 full-text-only folders. First public before 2011: 39 studies (88 undated excluded); EEG 10, intracranial terms 6, ECoG 3 (none decodes imagined speech), paired overt/covert wording 1 (fMRI, no decoder), all pattern match. All years: paired wording 277, intracranial 433. A recall sample of 30 full-text snippets was read. Read in full: [[4]](#ref-4), [[3]](#ref-3), [[5]](#ref-5), [[7]](#ref-7) [concurrent], [[2]](#ref-2), [[6]](#ref-6). Known-item recall 0.5.
- **M06 / intracranial-speech-unit-classification.** Inclusion rule: ledger text names ECoG, sEEG or intracortical recording with phonemes, vowels, consonants or syllables; design of interest: single-electrode versus joint multi-electrode decoding; word-level decoders only as read priors. Ledger counts: slot-filled 7,345; pattern match 101 unique studies. Before 2011: 3 studies, multi-electrode 2. All years: 96 dated studies, multi-electrode 78, single-electrode 19 (pattern match). Read in full: [[5]](#ref-5), [[4]](#ref-4), [[2]](#ref-2). Known-item recall 0.33.
- **M12 / intracranial-speech-test-partition** (published table, reused). Inclusion rule: intracranial speech decoding studies; design of interest: how test data are separated from training data. Ledger counts: slot-filled 6,960; pattern match 618 unique studies; k-fold 132, held-out subject 28. Before 2011: 15 studies, k-fold 3, held-out session or subject 0 (pattern match). Read in full: [[8]](#ref-8). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [decoding-vowels-and-consonants-in-spoken-and-imagined-words-using-electrocorticographic-signals-in-h.bib](decoding-vowels-and-consonants-in-spoken-and-imagined-words-using-electrocorticographic-signals-in-h.bib).

1. <a id="ref-1"></a>Pei, X., Barbour, D., Leuthardt, E. C., Schalk, G. “Decoding Vowels and Consonants in Spoken and Imagined Words Using Electrocorticographic Signals in Humans.” *Journal of Neural Engineering*, 2011, 8(4), 046028. doi:[10.1088/1741-2560/8/4/046028](https://doi.org/10.1088/1741-2560/8/4/046028). Target. Read as the PMC author manuscript (PMC3772685). [wiki: doi-10.1088-1741-2560-8-4-046028](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2560-8-4-046028/article.md) [wiki: pmc-3772685-vowelcons](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3772685-vowelcons/article.md)
2. <a id="ref-2"></a>Zhao, Z., Wang, Z., Liu, Y., Qian, Y., Yin, Y., Gao, X., et al. “A neural architecture for imagined and overt speech motor dynamics.” *Nature Neuroscience*, 2026. doi:[10.1038/s41593-026-02456-0](https://doi.org/10.1038/s41593-026-02456-0). Later; state of the art for M04 and M06. Accepted 18 August 2026; online date not printed in the read version. [later] [wiki: natneuro-02456-motordyn](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/natneuro-02456-motordyn/article.md)
3. <a id="ref-3"></a>Deng, S., Srinivasan, R., Lappas, T., D'Zmura, M. “EEG classification of imagined syllable rhythm using Hilbert spectrum methods.” *Journal of Neural Engineering*, 2010, 7(4), 046006. doi:[10.1088/1741-2560/7/4/046006](https://doi.org/10.1088/1741-2560/7/4/046006). Prior; deciding prior for M04 (scalp EEG, imagined syllables, no overt condition). [wiki: doi-10.1088-1741-2560-7-4-046006](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2560-7-4-046006/article.md)
4. <a id="ref-4"></a>Guenther, F. H., Brumberg, J. S., Wright, E. J., Nieto-Castanon, A., Tourville, J. A., Panko, M., et al. “A Wireless Brain-Machine Interface for Real-Time Speech Synthesis.” *PLoS ONE*, 2009, 4(12), e8218. doi:[10.1371/journal.pone.0008218](https://doi.org/10.1371/journal.pone.0008218). Prior; deciding prior for M04 and M06 (intracortical, attempted speech, one locked-in participant). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-wireless-brain-machine-interface-for-real-time-speech-synthesis) [wiki: pmc-2784218-wirelesssynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wirelesssynth/article.md)
5. <a id="ref-5"></a>Kellis, S., Miller, K., Thomson, K., Brown, R., House, P., Greger, B. “Decoding spoken words using local field potentials recorded from the cortical surface.” *Journal of Neural Engineering*, 2010, 7(5), 056007. doi:[10.1088/1741-2560/7/5/056007](https://doi.org/10.1088/1741-2560/7/5/056007). Prior; deciding prior for M04 and M06 (micro-ECoG, overt words, single and concatenated electrodes). [wiki: doi-10.1088-1741-2560-7-5-056007](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2560-7-5-056007/article.md)
6. <a id="ref-6"></a>Kunz, E. M., Abramovich Krasa, B., Kamdar, F., Avansino, D., Hahn, N., Yoon, S., et al. “Inner speech in motor cortex and implications for speech neuroprostheses.” *Cell*, 2025. doi:[10.1016/j.cell.2025.06.015](https://doi.org/10.1016/j.cell.2025.06.015). Later; intracortical inner-speech decoding. [later] [wiki: cell-40816265-innersp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/cell-40816265-innersp/article.md)
7. <a id="ref-7"></a>Leuthardt, E. C., Gaona, C., Sharma, M., Szrama, N., Roland, J., Freudenberg, Z., et al. “Using the electrocorticographic speech network to control a brain-computer interface in humans.” *Journal of Neural Engineering*, 2011, 8(3), 036004. doi:[10.1088/1741-2560/8/3/036004](https://doi.org/10.1088/1741-2560/8/3/036004). Concurrent (same group); imagined phonemes as ECoG cursor-control features. [concurrent] [wiki: doi-10.1088-1741-2560-8-3-036004](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2560-8-3-036004/article.md)
8. <a id="ref-8"></a>Chen, J., Chen, X., Wang, R., Le, C., Khalilian-Gourtani, A., Jensen, E., et al. “Subject-Agnostic Transformer-Based Neural Speech Decoding from Surface and Depth Electrode Signals.” *bioRxiv*, 2024. doi:[10.1101/2024.03.11.584533](https://doi.org/10.1101/2024.03.11.584533). Later; state of the art in the published M12 topic table (leave-one-subject-out test). [later] [wiki: doi-10.1101-2024.03.11.584533](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2024.03.11.584533/article.md)
