# Decoding spoken words using local field potentials recorded from the cortical surface

Kellis, Miller, Thomson, Brown, House, Greger. Journal of Neural Engineering 7(5):056007, 2010. [doi:10.1088/1741-2560/7/5/056007](https://doi.org/10.1088/1741-2560/7/5/056007)

## Verdict

The paper [[1]](#ref-1) changes two components, both standard under the verdict rules. Its sensors (M05) replace the only prior design in the ledger, a penetrating intracortical electrode (2 of 2 prior studies, Appendix), with 1-mm surface micro-ECoG; its decoder (M06) replaces continuous formant regression with closed-set word classification. Neither is new as a design, since the authors cite high spatial resolution ECoG phoneme classification (Blakely et al. 2008, ref. 31) and their own EMBC 2010 word report (ref. 47), and neither is repeated beyond one patient and one 15/15 split. The strongest confound is selection on the evaluation data: trials were kept only if judged stereotyped, more than half discarded for some words (Sec. 2.2), and the best five electrodes, chosen by overall accuracy with no separate selection set (Sec. 3.3), carry gains of up to 20.0 percentage points. That micro-scale recording matters is untested: the clinical grid in the same patient was not decoded (Sec. 2.1, 2.3).

## Against the field, component by component

### M05 Sensors: electrode scale

**Usual approach:** before 2010-03 the ledger holds two intracranial speech decoders, both the Neurotrophic Electrode system in one locked-in participant (intracortical microelectrode, 2 of 2, slot-filled; Appendix) [[2]](#ref-2).

**State of the art:** Duraivel et al. (2023) [later] decode spoken phonemes from thin-film micro-ECoG in four patients, up to 57% against 11.11% chance; subsampled to standard intracranial spacing, median accuracy falls to 20–35% [[3]](#ref-3). The target has one patient and no spacing comparison.

No prior speech decoder in the ledger records micro-ECoG or high-density ECoG (full-text check, Appendix), but the paper is not first: the authors cite Blakely et al. 2008 (ref. 31), and Brumberg et al. [later] name these two studies as the earlier micro-ECoG speech work [[4]](#ref-4). Verdict: standard. The scale argument rests on neighbour differences within one array (nearly 30% at 1 mm, Sec. 4.2), with no macro baseline or significance test (Sec. 2.6).

### M06 Decoding: closed-set words instead of continuous formants

**Usual approach:** both prior intracranial speech decoders map neural activity to continuous F1/F2 formants with a Kalman filter (formant regression 2 of 2, word classification 0, slot-filled; Appendix) [[2]](#ref-2); the authors draw this contrast themselves (Sec. 1).

**State of the art:** Card et al. (2024) [later] reach 99.6% with a 50-word vocabulary from intracortical arrays [[5]](#ref-5). The target reaches 48% on ten words with its best five FMC electrodes (Sec. 3.3), 38 points over the 10% chance of ten classes (inference), on one fifth the vocabulary.

The 500-ms decision delay (Sec. 4.1) is, as the authors concede, slow for conversation (Sec. 4.4.3); the prior decoder gave feedback within 50 ms [[2]](#ref-2). Adding the Wernicke's array to FMC changed accuracy by 0.40 ± 0.43 points (Sec. 3.2), while keeping the best five of 16 FMC electrodes raised it by 13.5 ± 5.2 points (Sec. 3.3): with 15 training trials per word, more input lowered accuracy, the signature of an under-regularised classifier (inference). Verdict: standard; the authors' concurrent report on spoken-word classification from surface LFPs (ref. 47) shares the design, shown in one patient.

### M12 Evaluation: one adjacent split in one patient

**Usual approach:** the prior intracranial speech decoder was tested online in closed loop, hit rate rising from 45% to 70% between first and last blocks [[2]](#ref-2) (online test 2 of 2 prior studies, held-out session or subject 0, slot-filled; Appendix). The paper uses one offline 15/15 split of 30 adjacent stereotyped trials per word (Sec. 2.2), with no repeated splits (Sec. 2.6).

**State of the art:** leave-one-subject-out testing; Chen et al. (2024) [later] reach PCC 0.765 on unseen participants [[6]](#ref-6).

Repetition: 1 patient, 1 split, no reruns; four recording days get no day-wise score (Sec. 2.2). Two prior studies are below the 3 needed for behind. Verdict: standard for 2010, and weaker than its only prior, which tested online.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Same runs as test | No separate action | – | standard |
| M02 Training-only supervision | None | None | – | standard |
| M03 Training and adaptation | Per-patient PCA, 15 trials/word | Per-subject training | – | standard |
| M04 Use-time action | Overt repetition, 10 words | Attempted speech (prior) | – | standard |
| M05 Sensors | Micro-ECoG, 2×16, 1 mm | Intracortical electrode (slot-filled 2) | [[3]](#ref-3) (2023): 57% phonemes | standard |
| M06 Processing and decoding | PCA + nearest centroid, word set | Kalman formant regression (slot-filled 2) | [[5]](#ref-5) (2024): 99.6%, 50 words | standard |
| M07 Lexicon and LM | Closed word set | No LM | – | standard |
| M08 Output | Word label, offline | Formants with feedback | – | standard |
| M09 Confirmation | None (offline) | Offline study | – | not applicable |
| M10 Correction | None (offline) | Offline study | – | not applicable |
| M11 Reference construction | Prompted word, curated trials | Prompt labels | – | standard |
| M12 Evaluation | One adjacent 15/15 split | Online closed-loop test (slot-filled 2) | [[6]](#ref-6) (2024): PCC 0.765, unseen subjects | standard |
| M13 Device and cost | Bedside, wired, offline | Implanted wireless (prior) | – | standard |

## Where the claims outrun the evidence

- Selection on test data. The best five electrodes are those "with best overall accuracy" (Sec. 3.3); gains run from 4.0 points (89.6%, two words) to 20.0 points (48%, ten words), so all 16 FMC electrodes gave about 28% on ten words (inference).
- Trial curation. Stereotypy was judged on inflection, pitch and duration with no thresholds, rater count or blinding (Sec. 2.2); for "yes", 81 of 166 trials passed (Table 1). The authors name pitch and inflection as a confound (Sec. 4.3)
- Local assemblies. The Abstract reads word-specific electrode patterns as independent local processing; the evidence is neighbour differences such as 84.4% versus 56.7% for "hot" 1 mm apart (Sec. 3.5), with 15 decode trials per word and no test against sampling variability (Sec. 2.6).
- Locked-in use. The patient spoke overtly, offline (Sec. 2.2, 4.4.3); the locked-in claim (Abstract) is prospective.

## What the field needs next

- M05: decode the co-implanted clinical grid and the micro-ECoG arrays on the same trials.
- M12: fix curation and electrode selection on training data only; add repeated splits and a day-held-out test.
- M04: repeat the words in an attempted or mimed condition.

## Questions for the authors

- Were the best five electrodes chosen on the decode trials?
- Which day supplied each 30-trial block, and what is accuracy when training and decode days differ?
- Were log-normalization statistics fitted on training trials only?
- Who judged stereotypy, and what is accuracy on all recorded trials?

## Appendix: literature search

Setting for all three topics: human studies decoding produced, attempted or imagined speech from intracranial recordings, one shared ledger pattern (intracranial signal plus speech unit); target first public 2010-09; prior = before 2010-03, [concurrent] = 2010-03 to 2011-03; off-population: reviews, listening-only studies, studies without a decoder; versions count once.

- **M05 / intracranial-speech-electrode-scale.** Inclusion rule: the setting above; design of interest: intracortical microelectrodes, clinical 1-cm grids, 4-mm high-density ECoG or micro-ECoG. Ledger counts: slot-filled 7,329; pattern match 618 unique studies. Prior: 7 pattern-match hits, 5 off-population (2 reviews, 1 perception study, 2 without a decoder), population 2 (one participant lineage); intracortical microelectrode 2, micro-ECoG 0, high-density ECoG 0, clinical grid 0. [Concurrent]: 6 hits, 0 in population. Full-text check of all wiki papers mentioning speech (reference lists removed): micro-ECoG wording 114 unique studies, before 2012 only the target and [[4]](#ref-4); high-density or 1–4 mm wording before 2012 only [concurrent] studies without a speech decoder. All years, pattern match with mentions: high-density ECoG 138, micro-ECoG 51, clinical 1-cm grid 47. Read in full: [[2]](#ref-2), [[4]](#ref-4), [[3]](#ref-3). Known-item recall 1.0.
- **M06 / intracranial-speech-decoding-target.** Inclusion rule: the setting above; design of interest: closed-set word classification, phoneme or syllable classification, or continuous acoustic/formant regression. Ledger counts: slot-filled 7,345; pattern match 618 unique studies. Prior population 2: formant regression 2, word classification 0, phoneme classification 0 (slot-filled). All years, pattern match with mentions: continuous acoustic/formant regression 318, closed-set word classification 163, phoneme or syllable classification 122. Read in full: [[2]](#ref-2), [[5]](#ref-5). Known-item recall 1.0.
- **M12 / intracranial-speech-test-partition** (published table, reused). Inclusion rule: intracranial speech decoding studies; design of interest: how test data are separated from training data. Ledger counts: slot-filled 6,960; pattern match 618 unique studies; k-fold 132 (all years). Prior population 2: online closed-loop test 2, held-out session or day 0, held-out subject 0. Read in full: [[2]](#ref-2), [[6]](#ref-6) [later]. Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [decoding-spoken-words-using-local-field-potentials-recorded-from-the-cortical-surface.bib](decoding-spoken-words-using-local-field-potentials-recorded-from-the-cortical-surface.bib).

1. <a id="ref-1"></a>Kellis, S., Miller, K., Thomson, K., Brown, R., House, P., Greger, B. “Decoding spoken words using local field potentials recorded from the cortical surface.” *Journal of Neural Engineering*, 2010, 7(5), 056007. doi:[10.1088/1741-2560/7/5/056007](https://doi.org/10.1088/1741-2560/7/5/056007). Target. Read as the PMC author manuscript (PMC2970568). [wiki: doi-10.1088-1741-2560-7-5-056007](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2560-7-5-056007/article.md) [wiki: pmc-2970568-lfpwords](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2970568-lfpwords/article.md)
2. <a id="ref-2"></a>Guenther, F. H., Brumberg, J. S., Wright, E. J., Nieto-Castanon, A., Tourville, J. A., Panko, M., et al. “A Wireless Brain-Machine Interface for Real-Time Speech Synthesis.” *PLoS ONE*, 2009, 4(12), e8218. doi:[10.1371/journal.pone.0008218](https://doi.org/10.1371/journal.pone.0008218). Prior; deciding prior for M05, M06 and M12 (intracortical, continuous formant decoding, online across sessions, one locked-in participant). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-wireless-brain-machine-interface-for-real-time-speech-synthesis) [wiki: pmc-2784218-wirelesssynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wirelesssynth/article.md)
3. <a id="ref-3"></a>Duraivel, S., Rahimpour, S., Chiang, C., Trumpis, M., Wang, C., Barth, K., et al. “High-resolution neural recordings improve the accuracy of speech decoding.” *Nature Communications*, 2023, 14, 6938. doi:[10.1038/s41467-023-42555-1](https://doi.org/10.1038/s41467-023-42555-1). Later; state of the art for M05 (micro-ECoG speech decoding, four patients). [later] [wiki: doi-10.1038-s41467-023-42555-1](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41467-023-42555-1/article.md) [wiki: pmc-10628285-uecog](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10628285-uecog/article.md)
4. <a id="ref-4"></a>Brumberg, J. S., Wright, E. J., Andreasen, D. S., Guenther, F. H., Kennedy, P. R. “Classification of Intended Phoneme Production from Chronic Intracortical Microelectrode Recordings in Speech-Motor Cortex.” *Frontiers in Neuroscience*, 2011, 5, 65. doi:[10.3389/fnins.2011.00065](https://doi.org/10.3389/fnins.2011.00065). Later; describes Blakely et al. 2008 and the target as the earlier micro-ECoG speech studies. [later] [wiki: pmc-3096823-phonintent](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-3096823-phonintent/article.md)
5. <a id="ref-5"></a>Card, N. S., Wairagkar, M., Iacobacci, C., Hou, X., Singer-Clark, T., Willett, F. R., et al. “An accurate and rapidly calibrating speech neuroprosthesis.” *New England Journal of Medicine*, 2024, 391(7), 609–618. doi:[10.1056/NEJMoa2314132](https://doi.org/10.1056/NEJMoa2314132). Later; state of the art for M06 (50-word accuracy, intracortical). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/an-accurate-and-rapidly-calibrating-speech-neuroprosthesis) [wiki: doi-10.1056-nejmoa2314132](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1056-nejmoa2314132/article.md) [wiki: doi-10.1056-NEJMoa2314132](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1056-NEJMoa2314132/article.md) [wiki: pmc-11328962-rapidcal](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11328962-rapidcal/article.md)
6. <a id="ref-6"></a>Chen, J., Chen, X., Wang, R., Le, C., Khalilian-Gourtani, A., Jensen, E., et al. “Subject-Agnostic Transformer-Based Neural Speech Decoding from Surface and Depth Electrode Signals.” *bioRxiv*, 2024. doi:[10.1101/2024.03.11.584533](https://doi.org/10.1101/2024.03.11.584533). Later; state of the art in the published M12 topic table (leave-one-subject-out test). [later] [wiki: doi-10.1101-2024.03.11.584533](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2024.03.11.584533/article.md)
