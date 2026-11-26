# Fully Implanted Brain-Computer Interface in a Locked-In Patient with ALS

Vansteensel, M. J., Pels, E. G. M., Bleichner, M. G., Branco, M. P., Denison, T., et al. · New England Journal of Medicine 375(21), 2060–2066 · 2016 · [doi:10.1056/NEJMoa1608085](https://doi.org/10.1056/NEJMoa1608085)

## Verdict

The paper [[1]](#ref-1) changes the device and how it is operated (M13): subdural ECoG feeding a subcutaneous transmitter, nothing through the skin, used at home without investigators from day 197. Both departures are standard under the verdict rules: the skin-closed link predates it [[2]](#ref-2), and independent home use rests on one participant, although none of the 19 independent-use pattern matches in the ledger population predates it (Appendix). The main claim, that one locked-in user can communicate with it without the team, holds, and the [later] follow-up of the same user extends it to 7 years [[3]](#ref-3), in time but not across people. The click's reliability is not shown: 89% spelling accuracy pools target-letter steps with more numerous non-target steps, with no chance level or false-click rate (Fig. 3; M12). The rate, two letters per minute with unspecified word prediction, is 55 times below [later] intracortical typing (inference) [[4]](#ref-4).

## Against the field, component by component

### M13 Device: skin-closed ECoG implant

**Usual approach:** Of 382 implanted-sensor speech or communication studies (pattern match, unique studies; Appendix), 103 name wireless telemetry, 50 a fully implanted system and 48 a percutaneous connector, upper bounds, almost all from 2017 or later. Before 2016 the skin-closed designs here are one lineage, the neurotrophic electrode with FM telemetry, which "eliminates the need for wires or connectors passing through the skin" [[2]](#ref-2). The paper swaps that electrode for subdural strips, two of four connected to the implant (Methods).

**State of the art:** The same implant in 2024, 7 years of independent at-home use by the same user [[3]](#ref-3). The [later] intracortical speech system used daily at home still runs through a percutaneous pedestal, its authors leaving fully implantable systems to future work [[5]](#ref-5); the [later] wireless home system also mates to a pedestal [[6]](#ref-6). On the skin, the paper is not behind the field today.

Against [[2]](#ref-2) it differs in sensor and task, not in the skin-closed principle, and both rest on one participant; two further patients died before implantation (Methods). Verdict: standard.

### M13 Operation: independent home use

**Usual approach:** Of the 382 studies, 181 name a hospital, bedside or laboratory setting, 31 home use and 19 independent use (pattern match, upper bounds; Appendix). The [concurrent] intracortical typing study collected data in participants' homes with researchers monitoring from the laboratory and named a fully implanted wireless system as future work [[7]](#ref-7).

**State of the art:** 7 years with the same implant (2024) [[3]](#ref-3); across devices, 19 months and more than 3,800 hours of independent use at 56 words per minute, one user, with daily set-up by trained care partners (2026) [[5]](#ref-5), both [later].

Independence was partial: set-up needed help with antenna, receiver, tablet and cables (Results), and logs show use on 32 days from day 197 to day 266, 46% of the 70 days (inference), at 86 minutes per day. Verdict: standard, because one participant gives no repetition.

### M12 Evaluation: accuracy without a floor

**Usual approach:** Of the 382 studies, 169 name a chance level or shuffled null and 54 a false-positive rate (pattern match, upper bounds; Appendix); the 9 chance-level matches before 2016 are offline classification, not online selection.

**State of the art:** In 2024, 99.6% online accuracy on a 50-word vocabulary on the first day of use, chance fixed by the vocabulary [[8]](#ref-8), [later].

Spelling accuracy (89%, 44 runs) counts a click on the target letter and a withheld click on every other highlighted letter, with more inactive than active steps (Fig. 3); a user who never clicks would score above half (inference). In a [later] night-time study of an implanted ECoG user with late-stage ALS, daytime decoders produced 245 unintended clicks per hour [[9]](#ref-9). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Attempted hand movement, practice tasks | Cued attempted movement | – | standard |
| M02 Training-only supervision | Task cues; labels not described | Cue-timed labels | – | standard |
| M03 Training and adaptation | Tuned to day 157, then fixed | Per-user tuning | – | standard |
| M04 Use-time action | Attempted hand movement as a click | Attempted movement | – | standard |
| M05 Sensors | Subdural ECoG, 2 of 4 strips connected | Intracranial arrays | – | standard |
| M06 Processing and decoding | ECoG features to a click | Feature-based click | – | standard |
| M07 Lexicon and LM | Word prediction, unspecified | Speller defaults | – | standard |
| M08 Output | Letters by sequential scanning | Text | – | standard |
| M09 Confirmation | Scan selection only | No confirmation | – | standard |
| M10 Correction | No correction step | No correction loop | – | standard |
| M11 Reference construction | Dictated words, active and inactive steps | Cued targets | – | standard |
| M12 Evaluation | Run accuracy, no chance level | Chance level named, of 382 (pattern match 169) | [[8]](#ref-8) (2024): 99.6%, 50 words | standard |
| M13 Device and cost | Skin-closed ECoG implant, home use | Wireless telemetry, of 382 (pattern match 103) | [[3]](#ref-3) (2024): 7 years at home | standard |

## Where the claims outrun the evidence

- "Two letters per minute" (Abstract) rounds up the word-prediction rate: 33 s per letter is 1.8 letters per minute, the initial 52 s is 1.2 (inference; Results [[1]](#ref-1)).
- Target-task accuracy (91%, 83 runs, days 15 to 262) pools runs before and after settings were fixed on day 157 (Results; Fig. 2 [[1]](#ref-1)).
- "Capable of meeting the requirements for independent communication" (Discussion) rests on one user, set-up help and use on 32 of 70 days (inference; Results [[1]](#ref-1)).

## What the field needs next

- M12: class-wise sensitivity and false clicks per minute for scanning spellers, with chance from the scan design.
- M13: the skin-closed system in several users, with logs that separate BCI use from eye-tracker availability.
- M07: spelling rate with and without word prediction, the predictor stated.

## Questions for the authors

- What were accuracies on active and inactive steps, and the false-click rate at rest?
- How many target-task runs came after day 157, and how accurate were they?
- Which word prediction was used, and what was the rate without it?

## Appendix: literature search

- M13, wireless-implanted-speech-bci (published table, reused). Inclusion rule: speech or communication studies with implanted neural sensors (intracortical, ECoG, sEEG, depth), classified by how the signal leaves the body: percutaneous connector or pedestal, wireless telemetry (including a transmitter on a pedestal), or a fully implanted system; reviews and related-work mentions inflate full-text counts (upper bounds); wearable EMG or EEG devices excluded. Ledger: 6,075 unique studies slot-filled for M13; 382 unique studies pattern match. Usual design: system implemented and evaluated 216 of 296 with M13 recorded (slot-filled). This review's run over the 382: wireless telemetry 103, fully implanted 50, percutaneous connector 48 (pattern match, upper bounds); first public before 2016: wireless telemetry 10 (the neurotrophic-electrode lineage and works citing it), fully implanted 1 and percutaneous 1 (both mentions, not designs). Published run: 52, 51, 35. Read in full: [[2]](#ref-2) (prior), [[3]](#ref-3) (state of the art), [[5]](#ref-5). Known-item recall 1.0 (published, 3 seeds); this run 0.4 (5 seeds; the target, its 2024 follow-up and [[6]](#ref-6) fall outside the pattern).
- M13, implanted-communication-bci-home-use (new). Inclusion rule: same population; the design compared is where and by whom the system is operated: hospital or laboratory (epilepsy monitoring, bedside, laboratory), the participant's home, and use without investigators (independent use); full-text pattern counts with the reference list removed (upper bounds); a study counts under every setting it names. Ledger: 382 unique studies pattern match. Counts: hospital or laboratory 181, home use 31, independent use 19 (pattern match); first public before 2016: 10, 1 and 0. Read in full: [[7]](#ref-7) (concurrent), [[3]](#ref-3) (state of the art), [[6]](#ref-6), [[5]](#ref-5). Known-item recall 0.4 (5 seeds).
- M12, implanted-communication-bci-chance-and-false-positives (new). Inclusion rule: same population; the design compared is the floor reported for accuracy: a chance level or shuffled or permutation null, and a false-positive (unintended selection) rate; offline classification studies count (upper bounds). Ledger: 6,960 unique studies slot-filled for M12; 382 unique studies pattern match. Counts: chance level 169, false-positive rate 54 (pattern match); chance level before 2016: 9, all offline classification. Read in full: [[8]](#ref-8) (state of the art), [[9]](#ref-9). Known-item recall 0.4 (5 seeds).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Vansteensel, M. J., Pels, E. G. M., Bleichner, M. G., Branco, M. P., Denison, T., Freudenburg, Z. V., et al. “Fully Implanted Brain-Computer Interface in a Locked-In Patient with ALS.” *New England Journal of Medicine*, 2016, 375(21), 2060–2066. doi:[10.1056/NEJMoa1608085](https://doi.org/10.1056/NEJMoa1608085). Target. Read as the PMC author manuscript. [wiki: pmc-5326682-als-implant-bci](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-5326682-als-implant-bci/article.md)
2. <a id="ref-2"></a>Guenther, F. H., Brumberg, J. S., Wright, E. J., Nieto-Castanon, A., Tourville, J. A., Panko, M., et al. “A Wireless Brain-Machine Interface for Real-Time Speech Synthesis.” *PLoS ONE*, 2009, 4(12), e8218. doi:[10.1371/journal.pone.0008218](https://doi.org/10.1371/journal.pone.0008218). Prior; deciding prior for M13 (skin-closed telemetry). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-wireless-brain-machine-interface-for-real-time-speech-synthesis) [wiki: pmc-2784218-wireless](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wireless/article.md) [wiki: pmc-2784218-wirelesssynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wirelesssynth/article.md) [wiki: doi-10.1371-journal.pone.0008218](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1371-journal.pone.0008218/article.md)
3. <a id="ref-3"></a>Vansteensel, M. J., others “Longevity of a Brain-Computer Interface for Amyotrophic Lateral Sclerosis.” *New England Journal of Medicine*, 2024, 391(7), 619–626. doi:[10.1056/NEJMoa2314598](https://doi.org/10.1056/NEJMoa2314598). Later; same participant and system. [later] [wiki: pmc-11395392-bcilong](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11395392-bcilong/article.md)
4. <a id="ref-4"></a>Jude, J. J., Levi-Aharoni, H., Acosta, A. J., Allcroft, S. B., Nicolas, C., Lacayo, B. E., et al. “Restoring rapid natural bimanual typing with a neuroprosthesis after paralysis.” *Nature Neuroscience*, 2026, 29. doi:[10.1038/s41593-026-02218-y](https://doi.org/10.1038/s41593-026-02218-y). Later. [later] [wiki: doi-10.1038-s41593-026-02218-y](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41593-026-02218-y/article.md) [wiki: pmc-13633126-bimantype](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13633126-bimantype/article.md) [wiki: pmc-13633126-bimanualtype](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13633126-bimanualtype/article.md) [wiki: pmc-13633126-bitype](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13633126-bitype/article.md) [wiki: pmc-13633126-bityping](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13633126-bityping/article.md) [wiki: pmc-13633126-ibcityping](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13633126-ibcityping/article.md)
5. <a id="ref-5"></a>Card, N. S., Singer-Clark, T., Peracha, H., Iacobacci, C., Hou, X., Wairagkar, M., et al. “Long-term independent use of an intracortical brain-computer interface for speech and cursor control.” *Nature Medicine*, 2026, 32(7), 2504–2510. doi:[10.1038/s41591-026-04414-6](https://doi.org/10.1038/s41591-026-04414-6). Later. [later] [wiki: pmc-13375540-ltbci](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13375540-ltbci/article.md) [wiki: pmc-13375540-ibciterm](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13375540-ibciterm/article.md) [wiki: pmc-13375540-ltc-speechbci](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13375540-ltc-speechbci/article.md)
6. <a id="ref-6"></a>Simeral, J. D., Hosman, T., Saab, J., Flesher, S. N., Vilela, M., Franco, B., et al. “Home Use of a Percutaneous Wireless Intracortical Brain-Computer Interface by Individuals With Tetraplegia.” *IEEE Transactions on Biomedical Engineering*, 2021, 68(7), 2313–2325. doi:[10.1109/TBME.2021.3069119](https://doi.org/10.1109/TBME.2021.3069119). Later. [later] [wiki: pmc-8218873-wirelesshomebci](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-8218873-wirelesshomebci/article.md)
7. <a id="ref-7"></a>Pandarinath, C., Nuyujukian, P., Blabe, C. H., Sorice, B. L., Saab, J., Willett, F. R., et al. “High performance communication by people with paralysis using an intracortical brain-computer interface.” *eLife*, 2017, 6, e18554. doi:[10.7554/eLife.18554](https://doi.org/10.7554/eLife.18554). Concurrent. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/high-performance-communication-by-people-with-paralysis-using-an-intracortical-brain-computer-interf) [wiki: pmc-5319839-ibcityping](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-5319839-ibcityping/article.md) [wiki: pmc-5319839-hiprofiBCI](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-5319839-hiprofiBCI/article.md)
8. <a id="ref-8"></a>Card, N. S., Wairagkar, M., Iacobacci, C., Hou, X., Singer-Clark, T., Willett, F. R., et al. “An accurate and rapidly calibrating speech neuroprosthesis.” *New England Journal of Medicine*, 2024, 391(7), 609–618. doi:[10.1056/NEJMoa2314132](https://doi.org/10.1056/NEJMoa2314132). Later. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/an-accurate-and-rapidly-calibrating-speech-neuroprosthesis) [wiki: doi-10.1056-nejmoa2314132](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1056-nejmoa2314132/article.md) [wiki: doi-10.1056-NEJMoa2314132](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1056-NEJMoa2314132/article.md) [wiki: pmc-11328962-rapidcal](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11328962-rapidcal/article.md)
9. <a id="ref-9"></a>Leinders, S., Aarnoutse, E. J., Branco, M. P., Freudenburg, Z. V., others “Implanted brain-computer interface functionality during nighttime in late-stage amyotrophic lateral sclerosis.” *Scientific Reports*, 2026. doi:[10.1038/s41598-026-44228-7](https://doi.org/10.1038/s41598-026-44228-7). Later. [later] [wiki: pmc-13133098-alsnight](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-13133098-alsnight/article.md)
