# Classification of intended phoneme production from chronic intracortical microelectrode recordings in speech-motor cortex

Brumberg, Wright, Andreasen, Guenther, Kennedy. Frontiers in Neuroscience 5:65, 2011. [doi:10.3389/fnins.2011.00065](https://doi.org/10.3389/fnins.2011.00065)

## Verdict

The paper [[1]](#ref-1) changes one component, the decoder (M06): it replaces the same participant's continuous three-vowel formant control [[2]](#ref-2) with discrete classification of 38 attempted phonemes, a class set that none of the 3 prior intracranial ledger studies uses (pattern match, Appendix); the largest read prior intracranial set was ten overt words [[3]](#ref-3). It is standard, not ahead: full phone sets were already the units of phone recognition from tongue ultrasound and lip video [[4]](#ref-4) and from EMG of silent speech [[5]](#ref-5) (Appendix), and nothing repeats the result beyond one participant with five pooled sessions. The evaluation (M12) is standard for 2011, but its samples are 300-ms bins assigned to folds at random, with no statement that a trial's 20 bins share a fold: the strongest confound for the 16–21% accuracies. "Intended" rests on an instruction and a post-trial denial check, with no attempt onset. The authors' conclusion that the rates are "truly not great enough to be useful as a communication device" holds; their reading of them as "a conservative, lower-bound" does not, because a trial-mixed split biases upward (inference).

## Against the field, component by component

### M06 Processing and decoding: size of the speech-unit class set

**Usual approach:** before 2010-11 the 3 intracranial ledger studies decode no discrete speech-unit set (pattern match, Appendix); the read discrete decoder classified ten overt words from micro-ECoG, 48% with the best five electrodes [[3]](#ref-3), and the same participant steered a formant synthesizer to three vowels, hit rate 45% to 70% [[2]](#ref-2); [concurrent] ECoG screened four phonemes [[6]](#ref-6). The paper classifies 38 phonemes from 31 clusters on two channels.

**State of the art:** Willett et al. (2023) [later] decode 39 attempted phonemes at 62% from 1 s of area 6v activity per trial, one participant [[7]](#ref-7); the target's best, 21.0% (SVM, Table 3), is about a third of that from 300-ms bins (inference).

Across signals the class set is not new: Hueber et al. recognized 40 phonetic classes from ultrasound and lip video at 60% without a language model, one speaker reading aloud [[4]](#ref-4); Walliczek et al. trained 45 phoneme units for EMG recognition of silent speech [[5]](#ref-5). Of 45 wiki studies from 2010 or earlier matching the full-phone-set pattern, none is an intracranial classifier (Appendix). Verdict: standard: new for intracranial signals, but one participant with pooled sessions is not repetition, and three classifiers on one split repeat the method, not the effect. Twenty of 38 phonemes exceed chance for all three classifiers (Fig. 4).

### M12 Evaluation: random 10-fold split over bins

**Usual approach:** among 12 prior intracranial studies, random trial splits are named by 3, k-fold cross-validation by 2, held-out sessions by 1 and online closed-loop decoding by 4 (pattern match, mentions, Appendix); the same participant's 2009 decoder ran online with feedback within 50 ms [[2]](#ref-2). The paper uses 10-fold cross-validation over random bins, 180 to 216 per phoneme, from 431 trials in five of 59 sessions.

**State of the art:** Willett et al. (2023) [later] test in real time on held-out sentences, 23.8% WER on a 125,000-word vocabulary [[7]](#ref-7).

Verdict: standard for 2011; fewer than three prior studies hold out sessions, but the split is weaker than the group's own online test with this participant [[2]](#ref-2).

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Cued attempt after a listen cue | Cued attempt (same participant, 2009) | – | standard |
| M02 Training-only supervision | None; cued stimulus as label | No training-only signal | – | standard |
| M03 Training and adaptation | Supervised fit on five pooled sessions | Per-subject training | – | standard |
| M04 Use-time action | Attempted isolated phonemes, locked-in | Attempted speech, same participant | – | standard |
| M05 Sensors | Neurotrophic Electrode, 2 channels, 31 clusters | Same implant as 2009 study | – | standard |
| M06 Processing and decoding | 38-phoneme classification, LDA, SVM, FDA, 300-ms bins | No discrete unit set, base 3 prior intracranial studies (pattern match 3) | [[7]](#ref-7) (2023): 39 attempted phonemes, 62% from 1 s per trial | standard |
| M07 Lexicon and LM | None; closed isolated-phoneme set | No LM, closed set | – | standard |
| M08 Output | Phoneme class label | Class label | – | standard |
| M09 Confirmation | None (offline) | Offline study | – | not applicable |
| M10 Correction | None (offline) | Offline study | – | not applicable |
| M11 Reference construction | Cued stimulus plus post-trial denial check | Cue or overt-production labels | – | standard |
| M12 Evaluation | 10-fold CV over random 300-ms bins, 5 pooled sessions | Random trial split, base 12 prior studies (pattern match 3) | [[7]](#ref-7) (2023): online, held-out sentences, 23.8% WER | standard |
| M13 Device and cost | Chronic wireless implant, offline, no code | Offline analysis of implant data | – | standard |

## Where the claims outrun the evidence

- Leakage. Bins are randomly partitioned (§ Classification analysis); sibling bins of one trial on both sides of the split let a classifier recognise the trial, not the phoneme (inference). No rest or shuffled-label control is reported (§ Experimental protocol), and binomial tests treat correlated bins as independent (§ Statistical analysis).
- "Conservative, lower-bound" (§ Discussion). The authors concede classification of segments outside the attempt, where "we do not expect the classifiers to correctly predict the appropriate phoneme" (§ Classification Summary); under a trial-mixed split such bins can still score (inference).
- "Intended". The attempt is checked only by instruction and post-trial denial; rejected-trial counts are not reported (§ Experimental protocol; § Discussion).
- Unit stability (M05). Sorting parameters from one off-line analysis were reused for all sessions, single and multi-units pooled (§ Recording system), and the five sessions are not identified (§ Experimental protocol).
- "Help prove the feasibility" (§ Discussion) outruns a study that "did not evaluate the tested methods for usefulness in a functional BMI" (§ Discussion); two authors own the electrode maker (§ Conflict of Interest Statement).

## What the field needs next

- M12: the 431 trials with each trial's bins in one fold and sessions held out, beside shuffled-label and rest baselines.
- M06: one decision per trial from an attempt-aligned window, per session, comparable with [[7]](#ref-7).
- M11: an independent attempt marker to place the window.

## Questions for the authors

- Were a trial's 20 bins kept in one fold, and what is the accuracy when they are, or with a session held out?
- Which five sessions were analysed, and what is the accuracy in each?
- How many trials were rejected for denied attempts, spasms or railing?
- How were the SVM and MARS settings chosen?

## Appendix: literature search

- M06, intracranial-phoneme-inventory-classification (published table, appended). Inclusion rule: intracranial signal named with phonemes, vowels, consonants or syllables in the ledger text; design = size of the speech-unit class set; target time: first public before 2010-11 is prior, 2010-11 to 2011-11 [concurrent]; versions merged, target folders excluded. Ledger counts: slot-filled 7,345 unique studies; pattern match 101 unique studies (all years). Prior population 3 unique studies, all without a discrete unit classifier (3 of 3; full inventory 0; small subset 0). Full-text pattern over the whole wiki (38–46 phonemes or phones, "all phonemes", "phoneme inventory"): 491 folders, 375 unique studies; 45 unique first public in 2010 or earlier, all snippets read; intracranial full-inventory classifiers among them 0; full-phone-set recognizers from other signals: tongue ultrasound and lip video [[4]](#ref-4), surface EMG [[5]](#ref-5), two audio-visual ASR systems. Recall sample 30 snippets, 0 with the same design. Known-item recall 1.0. Read in full: [[3]](#ref-3), [[2]](#ref-2), [[4]](#ref-4), [[5]](#ref-5), [[7]](#ref-7) (state of the art); [[6]](#ref-6) [concurrent] from the published table.
- M12, intracranial-speech-test-partition (published table, appended). Inclusion rule: intracranial speech decoding; design = separation of test from training data; published design regexes plus online closed-loop decoding, applied to studies first public before 2010-11. Ledger counts: slot-filled 6,960 unique studies; pattern match 618 unique studies (all years). Prior population 12 unique studies: random trial split 3, k-fold 2, held-out session or day 1, held-out subject 0, online closed loop 4 (pattern match, mentions). Known-item recall 1.0. Read in full: [[2]](#ref-2), [[7]](#ref-7) (state of the art).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Brumberg, J. S., Wright, E. J., Andreasen, D. S., Guenther, F. H., Kennedy, P. R. “Classification of intended phoneme production from chronic intracortical microelectrode recordings in speech-motor cortex.” *Frontiers in Neuroscience*, 2011, 5, 65. doi:[10.3389/fnins.2011.00065](https://doi.org/10.3389/fnins.2011.00065). Target. Version of record, published 12 May 2011. [wiki: doi-10.3389-fnins.2011.00065](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnins.2011.00065/article.md) [wiki: pmc-3096823-phoneme-intracortical](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3096823-phoneme-intracortical/article.md) [wiki: pmc-3096823-phonintent](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3096823-phonintent/article.md)
2. <a id="ref-2"></a>Guenther, F. H., Brumberg, J. S., Wright, E. J., Nieto-Castanon, A., Tourville, J. A., Panko, M., et al. “A Wireless Brain-Machine Interface for Real-Time Speech Synthesis.” *PLoS ONE*, 2009, 4(12), e8218. doi:[10.1371/journal.pone.0008218](https://doi.org/10.1371/journal.pone.0008218). Prior; same participant and implant. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-wireless-brain-machine-interface-for-real-time-speech-synthesis) [wiki: pmc-2784218-wireless](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wireless/article.md) [wiki: pmc-2784218-wirelesssynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wirelesssynth/article.md) [wiki: doi-10.1371-journal.pone.0008218](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1371-journal.pone.0008218/article.md)
3. <a id="ref-3"></a>Kellis, S., Miller, K., Thomson, K., Brown, R., House, P., Greger, B. “Decoding spoken words using local field potentials recorded from the cortical surface.” *Journal of Neural Engineering*, 2010, 7(5), 056007. doi:[10.1088/1741-2560/7/5/056007](https://doi.org/10.1088/1741-2560/7/5/056007). Prior; cited by the target. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/decoding-spoken-words-using-local-field-potentials-recorded-from-the-cortical-surface) [wiki: doi-10.1088-1741-2560-7-5-056007](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2560-7-5-056007/article.md) [wiki: pmc-2970568-lfpwords](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2970568-lfpwords/article.md)
4. <a id="ref-4"></a>Hueber, T., Chollet, G., Denby, B., Dreyfus, G., Stone, M. “Phone Recognition from Ultrasound and Optical Video Sequences for a Silent Speech Interface.” *Interspeech 2008*, 2008, 2032-2035. doi:[10.21437/Interspeech.2008-528](https://doi.org/10.21437/Interspeech.2008-528). Prior; deciding prior for the class-set design across signals. [wiki: isca-hueber08b-usphone](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-hueber08b-usphone/article.md) [wiki: isca-hueber08b_phonerec](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-hueber08b_phonerec/article.md)
5. <a id="ref-5"></a>Walliczek, M., Kraft, F., Jou, S., Schultz, T., Waibel, A. “Sub-Word Unit based Non-Audible Speech Recognition using Surface Electromyography.” *Interspeech 2006*, 2006. doi:[10.21437/Interspeech.2006-425](https://doi.org/10.21437/Interspeech.2006-425). Prior; deciding prior for the class-set design across signals. [wiki: isca-walliczek06_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-walliczek06_interspeech/article.md)
6. <a id="ref-6"></a>Leuthardt, E. C., Gaona, C., Sharma, M., Szrama, N., Roland, J., Freudenberg, Z., et al. “Using the electrocorticographic speech network to control a brain-computer interface in humans.” *Journal of Neural Engineering*, 2011, 8(3), 036004. doi:[10.1088/1741-2560/8/3/036004](https://doi.org/10.1088/1741-2560/8/3/036004). Concurrent. [concurrent] [wiki: doi-10.1088-1741-2560-8-3-036004](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2560-8-3-036004/article.md)
7. <a id="ref-7"></a>Willett, F. R., Kunz, E. M., Fan, C., Avansino, D. T., Wilson, G. H., Choi, E. Y., et al. “A high-performance speech neuroprosthesis.” *Nature*, 2023, 620(7976), 1031-1036. doi:[10.1038/s41586-023-06377-x](https://doi.org/10.1038/s41586-023-06377-x). Later; state of the art. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-high-performance-speech-neuroprosthesis) [wiki: doi-10.1038-s41586-023-06377-x](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-023-06377-x/article.md)
