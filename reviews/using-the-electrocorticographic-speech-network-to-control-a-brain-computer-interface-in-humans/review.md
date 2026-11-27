# Using the electrocorticographic speech network to control a brain-computer interface in humans

Leuthardt, Gaona, Sharma, Szrama, Roland, Freudenberg, Solis, Breshears, Schalk. Journal of Neural Engineering 8(3):036004, 2011. [doi:10.1088/1741-2560/8/3/036004](https://doi.org/10.1088/1741-2560/8/3/036004)

## Verdict

The paper [[1]](#ref-1) changes the control action (M04), screened vowels driving a 1-D ECoG cursor, and the sensor (M05), one 1-mm microgrid; both are standard. Its Sec. 1 "first" claims are contradicted by its own Sec. 4, which lists earlier ECoG BCIs using word articulation, and the broad "speech network" wording also by an uncited closed-loop speech-cortex BCI [[2]](#ref-2). The narrow claim, different overt vowels driving an ECoG cursor, holds for Patients 1-2; "different imagined phoneme articulations" (Sec. 4) was not tested: the imagined arm was vowel versus rest (Sec. 2.4). All four patients beat a 46.2% noise floor, but condition is confounded with patient, Table 2 disagrees with Fig. 8, and imagined speech identity, rather than task engagement, is not shown to move the cursor.

## Against the field, component by component

### M04 Use-time action: speech task as the closed-loop control signal

**Usual approach:** one earlier closed-loop speech-cortex study (pattern match, Appendix), attempted vowels decoded into formants [[2]](#ref-2), is too few to define one. The comparable ECoG design in the target's citations is task-versus-rest band power driving a 1-D cursor, with tasks including single-word articulation (Sec. 4, four works, including [[3]](#ref-3), [[4]](#ref-4), [[5]](#ref-5)); auditory cortex also drove a cursor [[6]](#ref-6).

**State of the art:** [later] attempted-speech BCIs decode words online: 99.6% on a 50-word vocabulary on day one, intracortical, one participant with ALS (2024) [[7]](#ref-7). The target's Wolpaw bits per trial are 0.56 at 91% and 0.11 at 69% (inference); bits per second need trial durations, which are not reported (Sec. 2.4).

The claims, quoted against the Appendix priors: "for the first time that ECoG signals associated with different overt and imagined phoneme articulation can enable" cursor control (Abstract); "for the first time that the electrocorticographic signals associated with speech can be effectively used to select from one of two choices" (Sec. 1); "first demonstration that neural correlates of different actual and imagined phoneme articulations" (Sec. 4). [Concurrent] works classify speech units offline [[8]](#ref-8), [[9]](#ref-9). Repetition: 4 patients, one pairing each, 61-139 trials (Sec. 2.4). Verdict: standard.

### M05 Sensors: electrode scale for device control

**Usual approach:** clinical epilepsy grids at 10 mm, used by the target in all four patients (Sec. 2.2) and, by its own account, by ECoG work to date (Sec. 4). Prior intracranial speech decoders number 2, no majority (pattern match, Appendix): a penetrating electrode in closed loop [[2]](#ref-2) and 1-mm micro-ECoG offline, 85.0% mean over 45 word pairs [[10]](#ref-10).

**State of the art:** [later] micro-ECoG thin films reach up to 57% nine-way phoneme accuracy offline (chance 11.11%) in four intraoperative patients (2023) [[11]](#ref-11); microscale device control is now intracortical [[7]](#ref-7).

None of the 2 prior decoders used micro-ECoG for device control (Appendix), so the "first demonstration that microscale ECoG recordings can be utilized for device control in humans" (Sec. 4) stands within that population. It rests on one patient and 76% over 139 trials (Table 2, Sec. 2.4). Verdict: standard; ahead needs repetition, here n = 1.

### M12 Evaluation: online accuracy and its chance floor

**Usual approach:** the one prior online study reports per-block hit rate over 25 sessions [[2]](#ref-2) (pattern match, 1 unique study, Appendix); the target reports final accuracy against a white-noise floor.

**State of the art:** [later] 99.6% word accuracy on 50 words on day one, with bootstrap 95% confidence intervals from 10,000 resamples and no chance floor (2024) [[7]](#ref-7).

White noise lacks ECoG's temporal structure; a constant cursor bias would score about 50% (inference). Patient 4's 69% over 69 trials is 3.8 binomial standard errors above 46.2% and about 3.2 above 50% (inference), if final accuracy covers all 69 trials; the paper does not say whether it means the last block or the run (Sec. 2.4). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Open-loop vowel screening | Per-subject screening | – | standard |
| M02 Training-only supervision | None | None | – | not applicable |
| M03 Training and adaptation | Per-patient r2 features, 1-min normaliser | Per-subject calibration | – | standard |
| M04 Use-time action | Vowel pair (overt) or vowel vs rest (imagined) | Task-vs-rest band-power cursor (cited ECoG priors); 1 closed-loop speech study | [[7]](#ref-7) (2024): 99.6%, 50 words | standard |
| M05 Sensors | 10-mm grids; one 1-mm microgrid | 10-mm clinical grids (Sec. 4) | [[11]](#ref-11) (2023): 57% nine-way, offline | standard |
| M06 Processing and decoding | Weighted band power to velocity | Linear band-power cursor | – | standard |
| M07 Lexicon and LM | None | None | – | not applicable |
| M08 Output | 1-D cursor, 2 targets | Cursor | – | standard |
| M09 Confirmation | None (selection by target hit) | None | – | not applicable |
| M10 Correction | None | None | – | not applicable |
| M11 Reference construction | Cued side | Cue labels | – | standard |
| M12 Evaluation | Accuracy vs noise floor 46.2% | Online hit rate (1 study) | [[7]](#ref-7) (2024): 99.6%, bootstrap CI | standard |
| M13 Device and cost | Acute epilepsy monitoring | Clinical monitoring | – | standard |

## Where the claims outrun the evidence

- Table 2 does not match Fig. 8: Patient 1's last block reads 96% (Table 2: 91%), and Patients 3 and 4 end near 69% and 73%, reversed against Table 2 (read from figure).
- "Two of our four patients immediately had greater that 90% accuracy" (Sec. 4): Fig. 8 shows about 88% and 90% in the first blocks of Patients 1 and 2 (read from figure), borderline rather than wrong.
- 68% (Abstract, Sec. 3) against 69% (Table 2); the Fig. 8 caption's "greater than 69%" excludes Patient 4's own 69%.
- Table 2's 560 Hz exceeds the 0-550 Hz screening range (Sec. 2.3), though Patient 4's 9600 Hz sampling could carry it; Patients 1-3 were screened above their 500 Hz bandpass (Sec. 2.2).
- The Fig. 9 caption calls Patient 1's contrast "imagined", while Sec. 2.3 and Sec. 2.4 say overt.
- Sec. 3 discloses that one patient was screened both ways, yet Sec. 4 generalises a "substantial difference between actual and imagined speech".
- No EMG, microphone or video check of imagined trials is reported (Sec. 2.2 to 2.4).
- Patient 1's control site is auditory cortex (BA 42; Table 2), which can track hearing one's own vowel; the authors themselves allow an auditory level (Sec. 4).

## What the field needs next

- M04: imagined vowel versus imagined vowel in patients who also do the overt pairing, with EMG and audio monitoring.
- M12: a floor from rest data or a biased cursor, and bits per second [[7]](#ref-7).

## Questions for the authors

- Is Table 2's final accuracy the last block or the whole run, and why do Patients 1, 3 and 4 differ from Fig. 8?
- Why was no patient tested with two imagined vowels?

## Appendix: literature search

Target first public 2011-04 (online 7 April 2011). Prior = first public before 2010-10; [concurrent] = 2010-10 to 2011-10. One setting for all topics: human closed-loop or intracranial speech work in any signal; reviews, perception-only and non-decoding studies excluded; reports of one experiment counted once.

- **M04 / speech-task-closed-loop-bci-control** (new). Inclusion rule: studies that close a loop from recorded activity to a device with feedback in a speech context; design of interest: a speech task (overt, attempted or imagined) as the control action. Ledger counts: slot-filled 5,595; pattern match 171 unique studies (all years: speech-task control 31, limb motor control 28, evoked-potential selection 62, pattern match). Prior population 1 unique study (Guenther 2009 and its Interspeech report), too few for a usual design. Same-group priors outside the wiki, described through the target's citations: [[3]](#ref-3), [[4]](#ref-4), [[5]](#ref-5) (ECoG cursor tasks including single-word articulation, Sec. 4), [[12]](#ref-12) (multimodal BCI, Sec. 4), and a 2007 Society for Neuroscience abstract (Schalk et al. 2007a) on phonemes separable during actual speech (Sec. 1); other prior outside the wiki: [[6]](#ref-6). Read in full: [[2]](#ref-2) (prior), [[7]](#ref-7) (state of the art). Known-item recall 0.75 (one later speech-cortex cursor study missed by the ledger pattern).
- **M05 / intracranial-speech-electrode-scale** (published table, reused). Inclusion rule: electrode type and scale used to record speech-related activity in intracranial speech decoding. Ledger counts: slot-filled 7,329; pattern match 618 unique studies. Prior decoders before 2010-10: 2 (penetrating intracortical 1, closed loop; 1-mm micro-ECoG 1, offline; micro-ECoG device control 0). Read in full: [[2]](#ref-2), [[10]](#ref-10) (prior), [[11]](#ref-11) (state of the art). Known-item recall 1.0.
- **M12 / real-time-intracranial-speech-online-evaluation** (published table, reused). Inclusion rule: intracranial speech studies with real-time, online or closed-loop operation; design of interest: the online accuracy figure and how its chance floor is built. Ledger counts: slot-filled 6,960; pattern match 134 unique studies; online accuracy reported 18 (published tally); in this review's full-text pattern, empirical chance or permutation 65 (all years, pattern match, upper bound). Prior population 1 unique study, which reports online hit rate. Read in full: [[2]](#ref-2) (prior), [[7]](#ref-7) (state of the art). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Leuthardt, E. C., Gaona, C., Sharma, M., Szrama, N., Roland, J., Freudenberg, Z., et al. “Using the electrocorticographic speech network to control a brain-computer interface in humans.” *Journal of Neural Engineering*, 2011, 8(3), 036004. doi:[10.1088/1741-2560/8/3/036004](https://doi.org/10.1088/1741-2560/8/3/036004). Target. Read as the PMC author manuscript (PMC3701859); published online 7 April 2011. [wiki: doi-10.1088-1741-2560-8-3-036004](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2560-8-3-036004/article.md)
2. <a id="ref-2"></a>Guenther, F. H., Brumberg, J. S., Wright, E. J., Nieto-Castanon, A., Tourville, J. A., Panko, M., et al. “A Wireless Brain-Machine Interface for Real-Time Speech Synthesis.” *PLoS ONE*, 2009, 4(12), e8218. doi:[10.1371/journal.pone.0008218](https://doi.org/10.1371/journal.pone.0008218). Prior; deciding prior for M04 and M12; not cited by the target. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-wireless-brain-machine-interface-for-real-time-speech-synthesis) [wiki: pmc-2784218-wirelesssynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wirelesssynth/article.md) [wiki: pmc-2784218-wireless](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wireless/article.md) [wiki: doi-10.1371-journal.pone.0008218](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1371-journal.pone.0008218/article.md)
3. <a id="ref-3"></a>Leuthardt, E. C., Schalk, G., Wolpaw, J. R., Ojemann, J. G., Moran, D. W. “A brain-computer interface using electrocorticographic signals in humans.” *Journal of Neural Engineering*, 2004, 1, 63-71. doi:[10.1088/1741-2560/1/2/001](https://doi.org/10.1088/1741-2560/1/2/001). Prior, same group; described through the target's citation.
4. <a id="ref-4"></a>Schalk, G., Miller, K. J., Anderson, N. R., Wilson, J. A., Smyth, M. D., Ojemann, J. G., et al. “Two-dimensional movement control using electrocorticographic signals in humans.” *Journal of Neural Engineering*, 2008, 5, 75-84. doi:[10.1088/1741-2560/5/1/008](https://doi.org/10.1088/1741-2560/5/1/008). Prior, same group; described through the target's citation.
5. <a id="ref-5"></a>Leuthardt, E. C., Miller, K. J., Schalk, G., Rao, R. P. N., Ojemann, J. G. “Electrocorticography-based brain computer interface--the Seattle experience.” *IEEE Transactions on Neural Systems and Rehabilitation Engineering*, 2006, 14, 194-198. doi:[10.1109/TNSRE.2006.875536](https://doi.org/10.1109/TNSRE.2006.875536). Prior, same group; described through the target's citation (cited there as Leuthardt 2005).
6. <a id="ref-6"></a>Wilson, J. A., Felton, E. A., Garell, P. C., Schalk, G., Williams, J. C. “ECoG factors underlying multimodal control of a brain-computer interface.” *IEEE Transactions on Neural Systems and Rehabilitation Engineering*, 2006, 14, 246-250. doi:[10.1109/TNSRE.2006.875570](https://doi.org/10.1109/TNSRE.2006.875570). Prior; described through the target's citation.
7. <a id="ref-7"></a>Card, N. S., Wairagkar, M., Iacobacci, C., Hou, X., Singer-Clark, T., Willett, F. R., et al. “An accurate and rapidly calibrating speech neuroprosthesis.” *New England Journal of Medicine*, 2024, 391(7), 609-618. doi:[10.1056/NEJMoa2314132](https://doi.org/10.1056/NEJMoa2314132). Later; state of the art for M04 and M12. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/an-accurate-and-rapidly-calibrating-speech-neuroprosthesis) [wiki: doi-10.1056-nejmoa2314132](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1056-nejmoa2314132/article.md) [wiki: pmc-11328962-rapidcal](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11328962-rapidcal/article.md)
8. <a id="ref-8"></a>Brumberg, J. S., Wright, E. J., Andreasen, D. S., Guenther, F. H., Kennedy, P. R. “Classification of intended phoneme production from chronic intracortical microelectrode recordings in speech-motor cortex.” *Frontiers in Neuroscience*, 2011, 5, 65. doi:[10.3389/fnins.2011.00065](https://doi.org/10.3389/fnins.2011.00065). Concurrent. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/classification-of-intended-phoneme-production-from-chronic-intracortical-microelectrode-recordings-i) [wiki: doi-10.3389-fnins.2011.00065](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnins.2011.00065/article.md) [wiki: pmc-3096823-phoneme-intracortical](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3096823-phoneme-intracortical/article.md) [wiki: pmc-3096823-phonintent](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3096823-phonintent/article.md)
9. <a id="ref-9"></a>Pei, X., Barbour, D., Leuthardt, E. C., Schalk, G. “Decoding Vowels and Consonants in Spoken and Imagined Words Using Electrocorticographic Signals in Humans.” *Journal of Neural Engineering*, 2011, 8(4), 046028. doi:[10.1088/1741-2560/8/4/046028](https://doi.org/10.1088/1741-2560/8/4/046028). Concurrent, same group. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/decoding-vowels-and-consonants-in-spoken-and-imagined-words-using-electrocorticographic-signals-in-h) [wiki: doi-10.1088-1741-2560-8-4-046028](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2560-8-4-046028/article.md) [wiki: pmc-3772685-vowelcons](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3772685-vowelcons/article.md)
10. <a id="ref-10"></a>Kellis, S., Miller, K., Thomson, K., Brown, R., House, P., Greger, B. “Decoding spoken words using local field potentials recorded from the cortical surface.” *Journal of Neural Engineering*, 2010, 7(5), 056007. doi:[10.1088/1741-2560/7/5/056007](https://doi.org/10.1088/1741-2560/7/5/056007). Prior; deciding prior for M05; cited by the target. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/decoding-spoken-words-using-local-field-potentials-recorded-from-the-cortical-surface) [wiki: doi-10.1088-1741-2560-7-5-056007](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2560-7-5-056007/article.md) [wiki: pmc-2970568-lfpwords](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2970568-lfpwords/article.md)
11. <a id="ref-11"></a>Duraivel, S., Rahimpour, S., Chiang, C., Trumpis, M., Wang, C., Barth, K., et al. “High-resolution neural recordings improve the accuracy of speech decoding.” *Nature Communications*, 2023, 14, 6938. doi:[10.1038/s41467-023-42555-1](https://doi.org/10.1038/s41467-023-42555-1). Later; state of the art for M05. [later] [wiki: doi-10.1038-s41467-023-42555-1](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41467-023-42555-1/article.md) [wiki: pmc-10628285-uecog](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10628285-uecog/article.md)
12. <a id="ref-12"></a>Leuthardt, E. C., Schalk, G., Roland, J., Rouse, A., Moran, D. W. “Evolution of brain-computer interfaces: going beyond classic motor physiology.” *Neurosurgical Focus*, 2009, 27, E4. doi:[10.3171/2009.4.FOCUS0979](https://doi.org/10.3171/2009.4.FOCUS0979). Prior, same group; described through the target's citation.
