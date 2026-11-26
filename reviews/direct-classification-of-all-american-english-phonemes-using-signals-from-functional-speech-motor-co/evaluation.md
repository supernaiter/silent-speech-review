# Evaluation: Direct classification of all American English phonemes (Mugler et al., 2014)

Evaluator: a language model separate from the writer

Date: 2026-11-26. Inputs read: the review draft (`<slug>.md`), `compact.md`, `<slug>.slots.json`, `verdict.json`, `claims.md`, `notes.json`, the M06 and M12 audits, and the reader texts for the target (PMC4097188), Brumberg 2011 and Wilson 2020 (`reader-q1/`). Nothing in the wiki or the review files was changed.

## Claims checked

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Abstract's 36% is NU2 consonant accuracy, 36.1% (Verdict; outrun bullet 1) | Target Sec. 3.1: "Subject NU2 had the highest overall performance, in which 36.1% of consonant phonemes were correctly classified." | correct | |
| 2 | Vowels and consonants classified separately | Target Sec. 3.1: "Vowels and consonants were analyzed separately" | correct | |
| 3 | 20.4% mean "pools two classifiers" (outrun bullet 1) | Target Sec. 3.1, Fig. 3 caption | insufficient evidence | The text does not say how 20.4% was formed; see F5 |
| 4 | Onsets hand-labelled from the microphone for every analysed phoneme, test included | Target Sec. 2.4: "manually label the onset of each phoneme within each word" | correct | |
| 5 | "Windows span 300 ms around hand-labelled onsets" (outrun bullet 2) | Target Sec. 2.4: "features from 300 ms prior to 300 ms after phoneme onset"; Wilson: "equivalent 600 millisecond window" | wrong | F6 |
| 6 | Feature count tuned to maximum; electrode exclusion by significance; no nesting stated | Target Sec. 2.5 | correct | Headline link missing; F10 |
| 7 | NU2/NU3 repeated the first 160 words; folds not grouped by word | Target Sec. 2.3, 2.5 | correct | A stronger leak is missed; F7 |
| 8 | Brumberg 2011: 38 phonemes, 16–21%, chance 2.6% | notes b1b, b2a; M06 audit read_fulltext | correct | Authors cite it themselves; F4 |
| 9 | Pei 2011: 40.7±2.7% overt vowels, chance 25%; "nine consonant-pair groups" | notes p17 | partly wrong | Consonant classifier is 4-class matched groups from nine pairs; F14 |
| 10 | Leuthardt 2011: four phonemes in screening | notes l19 | correct | |
| 11 | 8 of 11 earlier intracranial studies name small subsets; 1 full inventory | M06 audit prior_tally | wrong as labelled | Population includes non-intracranial items; Brumberg counted in both designs; F1 |
| 12 | Wilson 2020: 33.9%, 39 phonemes, chance 6%, hand-labelled onsets within words | Wilson Abstract; Methods ("manually labeled using the Praat software package") | correct | Matched comparison omitted; F2 |
| 13 | Wilson restates onset sensitivity | notes w4 (Wilson Discussion) | correct | Wilson also qualifies it; F8 |
| 14 | Willett 2023: 39 isolated phonemes, 62%, naive Bayes, 1 s | M06 audit read_fulltext | correct | |
| 15 | M12: 9 of 34 k-fold "up to 2013" | M12 audit prior_tally for this slug | correct as tallied, wrong cutoff | F9 |
| 16 | Slots without audit have matched = null | slots.json | correct | M01–M05, M07–M11, M13 all null; M06 8/11 and M12 9/34 are design counts with denominators |
| 17 | No `ahead` / `behind` verdicts | slots.json | correct | But one design dimension was never tested for `ahead`; F3 |

## Findings (ordered by impact)

**F1. High. Verdict sentence 2; M06 Usual approach; table row M06; Appendix M06.**
Evidence: review "8 of 11 earlier intracranial speech-unit studies name small subsets of two to six units, but full-inventory classification already existed in Brumberg et al." The M06 audit `prior_tally.population_pids` includes `isca-manca13_interspeech` ("Perception and production of Italian vowels: an ERP study", a scalp-EEG study) and `pmc-3127251-tempo` (a computational model of oscillations, not intracranial data). The small-subset list of 8 includes `doi-10.3389-fnins.2011.00065` (Brumberg 2011, the one full-inventory study) and `doi-10.1038-nature11897`, and the audit's own note says: "The small_unit_subset hits for Brumberg 2011 and Bouchard 2013 come from text describing other work or articulator schematics". So at least 4 of the 8 are not intracranial small-subset classifiers, and Brumberg is counted both as a subset study and as the exception.
Fix: do not call the 11 "intracranial speech-unit studies". Write it as a pattern-match upper bound and say what it contains, for example: "8 of 11 pattern-matched studies before 2013-11 name subsets of two to six units (upper bound; two of the 8 are text mentions, including Brumberg 2011 itself, and the 11 include one scalp-EEG and one modelling paper, Appendix); every read decoder classified four classes except Brumberg's 38." Add the same caveat to the Appendix entry.

**F2. High. M06 second paragraph ("The accuracy comparison favours no one ...").**
Evidence: Wilson et al. [5], which the review read, ran a matched protocol on the target's word set and windows: "Decoding vowels and consonants separately as in [Mugler], the T5 dataset accuracy was 36.8% across 24 consonant classes (vs. 36.1% in Mugler et al.'s best participant) and 27.7% across 16 vowels classes (vs. 23.9%)" (Wilson, Results, decoding within stand-alone short words, Suppl. Fig. 2). The review sets three chance ratios side by side and then dismisses them, while the read source holds a direct comparison under the same protocol.
Fix: replace the ratio paragraph with the matched comparison: on the target's words, a 600-ms window and the best subject's trial count, intracortical arrays gave 36.8% versus 36.1% on 24 consonants and 27.7% versus 23.9% on vowels [5]. Then state the position this supports (on a matched protocol, ECoG grids at 1 cm spacing nearly matched intracortical arrays six years later). Use Wilson's "16 vowels classes" in the question about class counts, labelled as Wilson's matched set.

**F3. Medium. Verdict sentence 3; M06 verdict paragraph.**
Evidence: the target's Discussion has two "first" claims: "This study is the first to decode the entire set of phonemes from American English using ECoG. It is also the first to successfully analyze and classify individual phonemes within word production." The second is not scoped to ECoG. The review says "The authors' own 'first' is scoped to ECoG" and tests only class-set size. The deciding priors it read do not have phoneme-onset-aligned classification inside words: Brumberg used isolated phonemes, and Pei classified at word level (the target itself: "comparing the ECoG activation relative to word onset"). The M06 heading names "onset-aligned", but no design count exists for it.
Fix: either tally the within-word, phoneme-onset-aligned design over the 11 priors (Appendix) and apply the `ahead` rule (deciding priors Brumberg and Pei already read; repetition: 4 subjects, reproduced later by Wilson [5]), or state in one sentence why that dimension stays `standard`. In either case, quote both "first" claims and give a verdict on each.

**F4. Medium. Verdict sentence 2 (fairness).**
Evidence: the target's introduction already cites the 38-phoneme prior: "Speech BCIs using intracortically-recorded spikes to decode phonemes have achieved up to 21% classification success of all phonemes [Brumberg]" (Sec. 1). The review presents "full-inventory classification already existed in Brumberg et al." as its own finding against the paper.
Fix: add "which the authors cite (Sec. 1)" and give the verdict as agreeing with the authors' own ECoG scoping, not as a correction of it.

**F5. Medium. Outrun bullet 1 ("the 20.4% mean pools two classifiers"); Questions for the authors 1.**
Evidence: the target states only "Averaged across all subjects, 20.4±9.8% of all phonemes were classified correctly ... (7.4%...)" and gives vowel chance separately as 12.9%. The Fig. 3 caption ("Dark bars indicate performance across all phonemes") and "highest overall performance, in which 36.1% of consonant phonemes" leave open whether "all phonemes" is consonants only. notes q1b records the count as "unstated".
Fix: "the paper does not say whether the 20.4% all-phoneme mean is consonant-only or pooled from the separate vowel and consonant classifiers (Sec. 3.1)". Reword question 1 to match.

**F6. Medium. Outrun bullet 2 ("Windows span 300 ms around hand-labelled onsets").**
Evidence: target Sec. 2.4: "used the features from 300 ms prior to 300 ms after phoneme onset. These 12 time bins ..."; Wilson: "an equivalent 600 millisecond window centered on voice onset".
Fix: "Features span ±300 ms (600 ms, 12 bins) around hand-labelled onsets".

**F7. Medium. Outrun bullet 4 (Leakage); What the field needs next, M12.**
Evidence: folds are drawn over phoneme instances ("10-fold cross-validation with randomly-selected test sets, which were fully independent of each other and of the training sets", Sec. 2.5). With a mean phoneme length of 176 ms and ±300 ms windows, neighbouring phonemes of the same word trial share most of their ECoG samples, and nothing says they were kept in the same fold. The authors themselves note "the period surrounding phoneme onset could contain some information about neighboring phonemes" (Sec. 2.4). The review flags only word repetition, which is the weaker leak.
Fix: add that phonemes from the same trial, with overlapping 600-ms windows, can fall in both training and test folds, which contradicts the authors' "fully independent" claim. Change the next-step to "folds grouped by trial and by word".

**F8. Medium. Verdict sentence 5 ("onset precision governs phoneme decoding"); M06 last sentence ("which Wilson et al. restate").**
Evidence: the target shows only that adding Gaussian jitter to oracle onsets lowers accuracy. Wilson [5] also reports that audio-derived onsets bias plosive timing and inflate accuracy ("audio-derived phoneme onset biases inflate overt speech decoding accuracies, but only modestly so", 12.9% relative), and that microphonic contamination inflates accuracy (29.3% to 25.8% after artifact subtraction). Both apply to the target: audio-derived hand labels, overt speech, 65–250 Hz features. The review uses Wilson only as a restatement.
Fix: write "depends on" instead of "governs", and add one sentence: the target's audio-labelled onsets and overt high-gamma features carry the two confounds Wilson later measured as modest inflations [5]. Use this as the strongest confound in the Verdict.

**F9. Medium. M12 Usual approach; Appendix M12.**
Evidence: the M12 count uses `"cutoff_year": 2013` ("index year ... up to 2013"), while M06 and the brief use "first public before 2013-11 (more than six months before the target, 2014-05)". "Up to 2013" admits work from November and December 2013, which is concurrent. The random-split list also contains both `pmc-3269422-pasley` and `doi-10.1371-journal.pbio.1001251`, which look like two versions of Pasley et al. 2012 (versions must count once). One of them is also in the k-fold list.
Fix: recount M12 on studies first public before 2013-11 with versions merged, and state the denominator and cutoff exactly as for M06. If a recount is not possible, write "up to 2013 (includes [concurrent] months)" and say how the Pasley versions were handled.

**F10. Medium. Outrun bullet 3 (Selection optimism).**
Evidence: Sec. 2.5: "To determine peak performance for each subject, we excluded electrodes that did not contain significant features (p-values > 0.1) ... Features were selected from these electrodes for each subject to determine their best possible decoding performance"; also "adding bins to the feature set until performance no longer improved". The review lists the steps but does not say that the reported per-subject results (36.1%, 20.4%) are the "peak" configurations chosen this way.
Fix: state that the headline figures come from the per-subject peak configuration (electrodes, feature count and time bins tuned on cross-validated accuracy), so they are optimistic, and add the time-bin selection loop to the list. If the text leaves unclear which figures are peak, ask that in Questions for the authors.

**F11. Medium. M06 second paragraph (disclaimer in body).**
Evidence: "class counts, isolated versus in-word production and chance definitions differ, so these ratios are not evidence of a gap." Three reviewer ratios are computed and then disowned. This is a methodological disclaimer with no position behind it.
Fix: delete the ratio sentence (replaced by F2).

**F12. Low. M12 Usual approach ("132 of 618 across years").**
Evidence: a count across all years that includes the target's later field. The usual approach must be judged at the target's time. 9 of 34 is the count that applies.
Fix: drop "and 132 of 618 across years" from the Usual approach line and keep it in the Appendix only.

**F13. Low. M06 Usual approach last sentence; M12 Usual approach second clause (method restatement).**
Evidence: "with LDA on 140 ANOVA-ranked features (Sec. 2.4–2.5)" and "the paper averages five repetitions of ten-fold cross-validation within each subject and builds chance from 100 label shuffles (Sec. 2.5)" restate the method without saying how it departs from the field. LDA and k-fold were usual.
Fix: keep only the departure: in M06, phoneme-onset events inside words; in M12, "same as the field: random within-subject folds, no held-out session, subject or word".

**F14. Low. M06 Usual approach ("four vowels or nine consonant-pair groups at word level").**
Evidence: notes p17: "25% for four-vowel matched groups classification and for nine-consonant-pair matched groups classification". The consonant classifier was 4-class, with groups drawn from nine pairs.
Fix: "four vowels, or four-class groups drawn from nine consonant pairs, at word level, chance 25%".

**F15. Low. Verdict sentence 3 ("holds against the read ECoG priors").**
Evidence: among the 11 priors, the ECoG studies also include Bouchard 2013 (`doi-10.1038-nature11897`, "CV syllable reading (19 consonants × /a/,/u/,/i/), ECoG"), Pei 2012 and Leuthardt 2010 (nine vowels), and none was read. Blakely 2008 (ECoG, phonemes), cited by the authors, is not in the wiki (audit known_item_recall_note). The sentence does not give an ECoG-specific count.
Fix: give the count from the Appendix ("0 of the k ECoG studies among the 11 classify the full inventory"), and either read Bouchard 2013 as the deciding ECoG prior with the largest unit set or name it as unread.

**F16. Low. Outrun bullet 5 (Word identification).**
Evidence: "the authors call it insufficient for communication (Sec. 4)". This repeats the authors' own caveat as an overreach. The overreach is the abstract's framing ("aiding classification of whole words", "3.0 bits/s (33.6 words/min)").
Fix: tie the bullet to the abstract sentence, or drop it. Bullet 2 already covers the ITR.

**F17. Low. M12 State of the art; table row M12.**
Evidence: Chen et al. 2024 report spectrogram PCC 0.765 for speech reconstruction on unseen participants, not phoneme classification. The audit's `state_of_the_art.timing` reads "prior" (the review's [later] label is right).
Fix: add the condition: "(spectrogram reconstruction, leave-one-subject-out)". A journal version of the bioRxiv preprint may exist (unverified); check it before publishing.

**F18. Low (unverified). M06 Appendix population.**
Evidence: from outside knowledge, Tankus, Fried and Shoham, Nature Communications 2012 (3:1015), decoded five vowels from intracranial single units. It does not appear among the 11. It would add one small-subset prior and does not change the verdict.
Fix: check the ledger. If present, add it to the prior population. If not, leave it unless known-item recall is recomputed.

Verdict rules: no `ahead` or `behind` is claimed. M06 `standard` is admissible under the rule ("difference not supported well enough to call") because Brumberg 2011, read in full, has a 38-class design in the same intracranial population. F3 is about the dimension that was never tested. Counts in slots.json follow the rule: design counts with stated denominators for M06 (8/11, before 2013-11) and M12 (9/34), and matched = null for every slot without its own audit.

Scores: procedure 6/10; final text 6/10.

Findings by severity: High 2, Medium 9, Low 7 (total 18).
