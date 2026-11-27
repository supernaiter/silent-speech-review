# Using the electrocorticographic speech network to control a brain-computer interface in humans

Leuthardt, Gaona, Sharma, Szrama, Roland, Freudenberg, Solis, Breshears, Schalk. Journal of Neural Engineering 8(3):036004, 2011. [doi:10.1088/1741-2560/8/3/036004](https://doi.org/10.1088/1741-2560/8/3/036004)

## Verdict

The paper [[1]](#ref-1) changes the control action (M04), cued overt or imagined vowels screened per patient to drive a 1-D cursor, and the sensor (M05), adding one 1-mm microgrid. Both are standard. Closed-loop control from speech cortex preceded it: a locked-in participant steered a formant synthesizer by attempted speech over 25 sessions [[2]](#ref-2), uncited here, and the paper itself says earlier ECoG cursor tasks included single-word articulation [[3]](#ref-3), [[4]](#ref-4). Its addition is narrower: screened vowel features, and imagined vowel versus rest as an ECoG control task. The 1-bit online result holds above a noise-derived chance level; the "first demonstration" of speech-network control and "two of four patients immediately >90%" claims do not hold against the field and Table 2. With condition confounded with patient and imagined trials unmonitored, it does not show that imagined speech identity, rather than task engagement, drives the cursor.

## Against the field, component by component

### M04 Use-time action: speech task as the closed-loop control signal

**Usual approach:** before 2010-10 the wiki holds 1 closed-loop speech-cortex study (pattern match, 1 unique study, Appendix): attempted vowels decoded continuously into formants with feedback within 50 ms [[2]](#ref-2). Outside the wiki, same-group ECoG cursors used hand, tongue and single-word tasks [[3]](#ref-3), [[4]](#ref-4), and auditory cortex drove a cursor [[5]](#ref-5) (target Sec. 1, Sec. 4). The paper maps one or two screened vowels to cursor direction.

**State of the art:** [later] attempted-speech BCIs decode words online, 99.6% on a 50-word vocabulary on day one, intracortical, one participant with ALS (2024) [[6]](#ref-6); [later] speech motor cortex drives a cursor at 2.90 bits per second, but through attempted right-hand imagery (2025) [[7]](#ref-7). The target offers 2 choices at 68-91% (chance 46.2%), at most 1 bit per selection (inference).

The Sec. 1 claim that such evidence "has been absent" is contradicted by the paper's own Sec. 4 and by Guenther et al. [[2]](#ref-2). Two [concurrent] works classify speech units offline [[8]](#ref-8), [[9]](#ref-9). The protocol is overt vowel versus vowel in Patients 1-2 and imagined vowel versus rest in Patients 3-4 (Sec. 2.4): the imagined arm detects a task, it does not discriminate speech units. Repetition: 4 patients, one pairing each, 61-139 trials (Sec. 2.4). Verdict: standard; the setting had a closed-loop prior (Appendix).

### M05 Sensors: electrode scale for device control

**Usual approach:** before 2010-10 the wiki holds 2 intracranial speech-production decoders (pattern match, unique studies, Appendix): a penetrating electrode in closed loop [[2]](#ref-2) and 1-mm micro-ECoG offline, 85.0% on two-word pairs over face motor cortex [[10]](#ref-10). The target adds a 16-microwire 1-mm grid over dorsal premotor cortex in Patient 2 to clinical 10-mm grids (Sec. 2.2).

**State of the art:** [later] micro-ECoG thin films reach up to 57% nine-way phoneme accuracy offline (chance 11.11%) in four intraoperative patients (2023) [[11]](#ref-11).

None of the 2 prior decoders used micro-ECoG for device control (Appendix), so the authors' claim of the first microscale ECoG device control (Sec. 4) stands as stated. It rests on one patient, one band (410-420 Hz) and 76% over 139 trials (Table 2, Sec. 2.4); Kellis et al., whom it cites, had shown word discrimination at that scale [[10]](#ref-10). Verdict: standard; ahead needs repetition and here n = 1.

### M12 Evaluation: online accuracy and its chance floor

**Usual approach:** the one prior online study reports per-block hit rate and its trend over 25 sessions [[2]](#ref-2) (pattern match, 1 unique study, Appendix). The target reports final accuracy against 46.2% (2.7% SD) chance from 32 blocks of 425 trials of white Gaussian noise (Sec. 2.4).

**State of the art:** [later] online word accuracy from the first day of use (2024) [[6]](#ref-6).

The noise floor counts time-outs as failures (Sec. 2.4) but is not the patient's own signal; a null from patient data after selection is the proper test, which the margins would likely survive: Patient 4's 69% of 69 trials is about 3.8 standard deviations above 46.2% (inference). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Open-loop vowel screening | Per-subject screening | – | standard |
| M02 Training-only supervision | None | None | – | not applicable |
| M03 Training and adaptation | Per-patient r2 features, 1-min normaliser | Per-subject calibration | – | standard |
| M04 Use-time action | Overt vowel pair (P1-2); imagined vowel vs rest (P3-4) | Attempted speech, continuous decoder (1 of 1) (pattern match 1) | [[6]](#ref-6) (2024): 99.6%, 50 words | standard |
| M05 Sensors | 10-mm grids; one 1-mm microgrid | 1-mm micro-ECoG offline (1 of 2) (pattern match 1) | [[11]](#ref-11) (2023): 57% nine-way | standard |
| M06 Processing and decoding | Weighted band power to velocity | Linear band-power cursor | – | standard |
| M07 Lexicon and LM | None | None | – | not applicable |
| M08 Output | 1-D cursor, 2 targets | Cursor | – | standard |
| M09 Confirmation | Target hit | None | – | not applicable |
| M10 Correction | None | None | – | not applicable |
| M11 Reference construction | Cued side | Cue labels | – | standard |
| M12 Evaluation | Accuracy vs noise chance 46.2% | Online hit rate (1 of 1) (pattern match 1) | [[6]](#ref-6) (2024): day-1 word accuracy | standard |
| M13 Device and cost | Acute epilepsy monitoring | Clinical monitoring | – | standard |

## Where the claims outrun the evidence

- The headline number disagrees with itself: 68-91% (Abstract, Sec. 3), "greater than 69%" (Sec. 3), and 69% for Patient 4 (Table 2).
- "Two of our four patients immediately had greater that 90% accuracy" (Sec. 4), yet only Patient 1 finished at or above 90% (Table 2: 91%, 76%, 73%, 69%).
- Table 2 lists 560 Hz for Patient 4, outside the 0-550 Hz spectral range (Sec. 2.3).
- Overt control only in Patients 1-2, imagined only in Patients 3-4 (Sec. 2.4); the overt-imagined difference comes from Patient 3's screening data alone (Fig. 7).
- Imagined trials have no EMG, microphone or video check (Sec. 2.2 to Sec. 2.4), so subvocal movement is not excluded.
- Patient 1's overt control used auditory cortex (BA 42; Table 2), which can track hearing one's own vowel rather than motor intent.

## What the field needs next

- M04: imagined vowel versus imagined vowel in the patients who also do the overt pairing, with EMG and audio monitoring.
- M12: a null from the patient's own data after feature selection, and bits per second, so speech-task control can be compared with attempted-speech and cursor BCIs [[6]](#ref-6), [[7]](#ref-7).
- M05: micro-ECoG closed-loop control in several patients, against macro-grid control at the same site [[11]](#ref-11).

## Questions for the authors

- Were features retuned between control blocks?
- How was a 560 Hz feature estimated when the spectrum stops at 550 Hz?
- Why was no patient tested with two imagined vowels?

## Appendix: literature search

Target first public 2011-04 (online 7 April 2011). Prior = first public before 2010-10; [concurrent] = 2010-10 to 2011-10. One setting for all topics: human closed-loop or intracranial speech work in any signal; reviews, perception-only and non-decoding studies excluded; reports of one experiment counted once.

- **M04 / speech-task-closed-loop-bci-control** (new). Inclusion rule: studies that close a loop from recorded activity to a device with feedback in a speech context; design of interest: a speech task (overt, attempted or imagined) as the control action. Ledger counts: slot-filled 5,595; pattern match 171 unique studies (all years: speech-task control 31, limb motor control 28, evoked-potential selection 62, pattern match). Prior population 1 unique study (Guenther 2009 and its Interspeech report); usual design: attempted speech to a continuous decoder, 1 of 1 (pattern match). Priors outside the wiki, from the target's citations: [[3]](#ref-3), [[4]](#ref-4), [[5]](#ref-5). Read in full: [[2]](#ref-2) (prior), [[6]](#ref-6) and [[7]](#ref-7) (state of the art). Known-item recall 0.75 (missed [[7]](#ref-7)).
- **M05 / intracranial-speech-electrode-scale** (published table, reused). Inclusion rule: electrode type and scale used to record speech-related activity in intracranial speech decoding. Ledger counts: slot-filled 7,329; pattern match 618 unique studies. Prior decoders before 2010-10: 2 (penetrating intracortical 1, closed loop; 1-mm micro-ECoG 1, offline; micro-ECoG device control 0). Read in full: [[2]](#ref-2), [[10]](#ref-10) (prior), [[11]](#ref-11) (state of the art). Known-item recall 1.0.
- **M12 / real-time-intracranial-speech-online-evaluation** (published table, reused). Inclusion rule: intracranial speech studies with real-time, online or closed-loop operation; design of interest: the online accuracy figure and how its chance floor is built. Ledger counts: slot-filled 6,960; pattern match 134 unique studies; online accuracy reported 18 (all years, pattern match). Prior population 1 unique study, which reports online hit rate. Read in full: [[2]](#ref-2) (prior), [[6]](#ref-6) (state of the art). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Leuthardt, E. C., Gaona, C., Sharma, M., Szrama, N., Roland, J., Freudenberg, Z., et al. “Using the electrocorticographic speech network to control a brain-computer interface in humans.” *Journal of Neural Engineering*, 2011, 8(3), 036004. doi:[10.1088/1741-2560/8/3/036004](https://doi.org/10.1088/1741-2560/8/3/036004). Target. Read as the PMC author manuscript (PMC3701859); published online 7 April 2011. [wiki: doi-10.1088-1741-2560-8-3-036004](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2560-8-3-036004/article.md)
2. <a id="ref-2"></a>Guenther, F. H., Brumberg, J. S., Wright, E. J., Nieto-Castanon, A., Tourville, J. A., Panko, M., et al. “A Wireless Brain-Machine Interface for Real-Time Speech Synthesis.” *PLoS ONE*, 2009, 4(12), e8218. doi:[10.1371/journal.pone.0008218](https://doi.org/10.1371/journal.pone.0008218). Prior; deciding prior for M04 and M12; not cited by the target. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-wireless-brain-machine-interface-for-real-time-speech-synthesis) [wiki: pmc-2784218-wirelesssynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wirelesssynth/article.md) [wiki: pmc-2784218-wireless](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wireless/article.md) [wiki: doi-10.1371-journal.pone.0008218](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1371-journal.pone.0008218/article.md)
3. <a id="ref-3"></a>Leuthardt, E. C., Schalk, G., Wolpaw, J. R., Ojemann, J. G., Moran, D. W. “A brain-computer interface using electrocorticographic signals in humans.” *Journal of Neural Engineering*, 2004, 1, 63-71. doi:[10.1088/1741-2560/1/2/001](https://doi.org/10.1088/1741-2560/1/2/001). Prior, same group; described through the target's citation.
4. <a id="ref-4"></a>Schalk, G., Miller, K. J., Anderson, N. R., Wilson, J. A., Smyth, M. D., Ojemann, J. G., et al. “Two-dimensional movement control using electrocorticographic signals in humans.” *Journal of Neural Engineering*, 2008, 5, 75-84. doi:[10.1088/1741-2560/5/1/008](https://doi.org/10.1088/1741-2560/5/1/008). Prior, same group; described through the target's citation.
5. <a id="ref-5"></a>Wilson, J. A., Felton, E. A., Garell, P. C., Schalk, G., Williams, J. C. “ECoG factors underlying multimodal control of a brain-computer interface.” *IEEE Transactions on Neural Systems and Rehabilitation Engineering*, 2006, 14, 246-250. doi:[10.1109/TNSRE.2006.875570](https://doi.org/10.1109/TNSRE.2006.875570). Prior; described through the target's citation.
6. <a id="ref-6"></a>Card, N. S., Wairagkar, M., Iacobacci, C., Hou, X., Singer-Clark, T., Willett, F. R., et al. “An accurate and rapidly calibrating speech neuroprosthesis.” *New England Journal of Medicine*, 2024, 391(7), 609-618. doi:[10.1056/NEJMoa2314132](https://doi.org/10.1056/NEJMoa2314132). Later; state of the art for M04 and M12. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/an-accurate-and-rapidly-calibrating-speech-neuroprosthesis) [wiki: doi-10.1056-nejmoa2314132](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1056-nejmoa2314132/article.md) [wiki: pmc-11328962-rapidcal](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11328962-rapidcal/article.md)
7. <a id="ref-7"></a>Singer-Clark, T., Hou, X., Card, N. S., Wairagkar, M., Iacobacci, C., Peracha, H., et al. “Speech motor cortex enables BCI cursor control and click.” *Journal of Neural Engineering*, 2025, 22(3), 036015. doi:[10.1088/1741-2552/add0e5](https://doi.org/10.1088/1741-2552/add0e5). Later; cursor control from speech motor cortex (bioRxiv 2024-11). [later] [wiki: pmc-12208300-cursor](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12208300-cursor/article.md) [wiki: pmc-12208300-spchcursor](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12208300-spchcursor/article.md) [wiki: pmc-12208300-vpcg-cursor](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12208300-vpcg-cursor/article.md) [wiki: doi-10.1088-1741-2552.add0e5](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552.add0e5/article.md) [wiki: doi-10.1101-2024.11.12.623096](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2024.11.12.623096/article.md) [wiki: pmc-11601350-spmotor](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11601350-spmotor/article.md)
8. <a id="ref-8"></a>Brumberg, J. S., Wright, E. J., Andreasen, D. S., Guenther, F. H., Kennedy, P. R. “Classification of intended phoneme production from chronic intracortical microelectrode recordings in speech-motor cortex.” *Frontiers in Neuroscience*, 2011, 5, 65. doi:[10.3389/fnins.2011.00065](https://doi.org/10.3389/fnins.2011.00065). Concurrent. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/classification-of-intended-phoneme-production-from-chronic-intracortical-microelectrode-recordings-i) [wiki: doi-10.3389-fnins.2011.00065](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnins.2011.00065/article.md) [wiki: pmc-3096823-phoneme-intracortical](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3096823-phoneme-intracortical/article.md) [wiki: pmc-3096823-phonintent](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3096823-phonintent/article.md)
9. <a id="ref-9"></a>Pei, X., Barbour, D., Leuthardt, E. C., Schalk, G. “Decoding Vowels and Consonants in Spoken and Imagined Words Using Electrocorticographic Signals in Humans.” *Journal of Neural Engineering*, 2011, 8(4), 046028. doi:[10.1088/1741-2560/8/4/046028](https://doi.org/10.1088/1741-2560/8/4/046028). Concurrent, same group. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/decoding-vowels-and-consonants-in-spoken-and-imagined-words-using-electrocorticographic-signals-in-h) [wiki: doi-10.1088-1741-2560-8-4-046028](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2560-8-4-046028/article.md) [wiki: pmc-3772685-vowelcons](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3772685-vowelcons/article.md)
10. <a id="ref-10"></a>Kellis, S., Miller, K., Thomson, K., Brown, R., House, P., Greger, B. “Decoding spoken words using local field potentials recorded from the cortical surface.” *Journal of Neural Engineering*, 2010, 7(5), 056007. doi:[10.1088/1741-2560/7/5/056007](https://doi.org/10.1088/1741-2560/7/5/056007). Prior; deciding prior for M05; cited by the target. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/decoding-spoken-words-using-local-field-potentials-recorded-from-the-cortical-surface) [wiki: doi-10.1088-1741-2560-7-5-056007](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2560-7-5-056007/article.md) [wiki: pmc-2970568-lfpwords](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2970568-lfpwords/article.md)
11. <a id="ref-11"></a>Duraivel, S., Rahimpour, S., Chiang, C., Trumpis, M., Wang, C., Barth, K., et al. “High-resolution neural recordings improve the accuracy of speech decoding.” *Nature Communications*, 2023, 14, 6938. doi:[10.1038/s41467-023-42555-1](https://doi.org/10.1038/s41467-023-42555-1). Later; state of the art for M05. [later] [wiki: doi-10.1038-s41467-023-42555-1](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41467-023-42555-1/article.md) [wiki: pmc-10628285-uecog](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10628285-uecog/article.md)
