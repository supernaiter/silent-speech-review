# Independent evaluation: Comparison of sEMG Encoding Accuracy Across Speech Modes Using Articulatory and Phoneme Features

Date: 2026-11-22. Fallback evaluator (claim table only). Input: the compact review (Verdict, component sections, component table, claims list, references) and its claim table. No sources were opened. Notes drawn from general knowledge of the literature are marked (inference).

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | [1] is an encoding study and trains no decoder; "better SSI intermediates" is untested | Claim row 1 (Abstract; §I; §II) | correct | The quote says "representation/encoding analysis (not end-to-end decoding)". |
| 2 | Gaddy gains: +0.012 voiced (2.7%), +0.018 mimed (5.2%) | Claim row 3 (§III-A) | correct | 0.455−0.443=0.012, 0.012/0.443=2.71%; 0.364−0.346=0.018, 0.018/0.346=5.20%. Marked as inference, correctly. |
| 3 | "24-participant results are plotted only" | Claim table | insufficient evidence | No row gives the cohort size or says that no values are tabulated. |
| 4 | Silent mode uses 12 features against 14 aloud | Claim row 4 (§II-B) | insufficient evidence | The quote gives 14 for aloud and mentions two laryngeal features. The value 12 for silent is implied, not quoted. |
| 5 | DTW inflation "as the authors concede (§III-B)" | Claim row 4 | correct for DTW only | The quote concedes DTW inflation. The sentence also covers the 12-vs-14 confound, which has no concession quoted. |
| 6 | Folds, seeds and sessions unstated (M12) | Claim table | insufficient evidence | No row. Absence claims about the target need a location, for example "§II-C gives k-fold CV without fold assignment". |
| 7 | Chartier et al. made "the same comparison on ECoG with the same outcome" | Claim row 2 | correct | The quote says articulatory beat both the acoustic and the phoneme models. |
| 8 | Chartier: articulatory, phoneme and **formant** models; 5 participants; p<1e-20 | Claim row 6 | mismatch / insufficient | The quote says "acoustic", not "formant". Neither 5 participants nor p<1e-20 is quoted. |
| 9 | Chartier inferred kinematics from produced audio | Claim row 7 | correct | The quote is truncated but carries the point. |
| 10 | Lee et al. [3]: correlation about 0.9, 8-electrode Gaddy layout, one speaker, vocalized | Claim row 8 | partly correct | The quote says "approximately 0.9 **for most** articulatory features" and vocalized only. The review drops "for most". The 8-electrode layout and single speaker are not quoted. |
| 11 | "A 12-dimensional smooth trajectory and a 40-dimensional one-hot" | Claim row 9; row 4 | wrong as written | SPARC has 14 dimensions for aloud speech (row 4), so 12 applies only to the silent modes. 40-dim one-hot is correct. |
| 12 | Shared component takes "the largest share on every channel" | Claim row 10 (§III-A, Fig. 3) | partly correct | The quote says it "dominates across electrodes". "On every channel" is stronger than that. |
| 13 | M06 usual approach: 137 studies; 124 acoustic, 41 phonetic, 23 articulatory | Claim row 5 (tally) | correct (counts) | These are pattern-match counts, and the Appendix calls 124 an upper bound. The text says "124 use acoustic predictors", which reads as confirmed. The pool is mostly perception-side neural encoding, so it is a loose stand-in for sEMG encoding (inference). |
| 14 | "The target is the only surface-EMG study among them" | Claim row 5 | insufficient evidence | This is an absence claim. No deciding priors are named and there is no quote. |
| 15 | M06 state of the art is Chartier et al. 2018 | Component section | insufficient evidence | Plausible as the classic production-side articulatory-vs-phoneme encoding result. It is eight years old, though, and the review does not say why no later encoding comparison (ECoG, sEEG or intracortical) supersedes it (inference). |
| 16 | M02 usual approach: 15 confirmed; earliest DTW-based is Janke [4] | Claim row 11 | partly correct | The quote supports DTW alignment of audible data to silent EMG. "Earliest" rests on a 2016 dissertation that collects earlier papers. DTW alignment of audible to silent EMG appeared in Janke and colleagues' work around 2010 (inference; check Janke, Wand, Schultz 2010). The line also gives the earliest study, not the usual design. |
| 17 | Fast-DTW radius 30 on z-scored EMG envelopes | Claim row 12 (§II-A) | partly correct | Radius 30 is quoted. "z-scored EMG envelopes" is not. |
| 18 | GETS [5]: 11.89% WER, silent Gaddy EMG, DTW-transferred targets, [concurrent] | Claim row 13 | partly correct | 11.89% WER on the silent EMG test set is quoted. "Gaddy" and "DTW-transferred targets" are not. [concurrent] is right (Interspeech 2026, within 6 months of an April 2026 preprint). As state of the art it is plausible next to earlier open-vocabulary Gaddy results of about 12% WER (inference). |
| 19 | The null shuffles phoneme spans inside each warped utterance (§II-C) | Claim table | insufficient evidence | No row for §II-C. The argument rests on it. |
| 20 | "Nearly all electrodes" rests on unvalued bars; the authors call the Gaddy gain modest | Claim row 14 | correct | Both phrases are quoted. |
| 21 | 7 of 8 Gaddy electrodes; ± undefined | Claim row 15 | partly correct | 7 of 8 is quoted. "± undefined" has no location. |
| 22 | Formal anatomy test deferred; Lee et al. linked electrodes to articulators earlier | Claim row 16 | correct | Both are quoted. [3] (2025) is more than 6 months before the target, so it is fair as prior work. |
| 23 | "Session- and speaker-held-out encoding tests, as in [2]" | Claim row 17 | wrong in part | The quote supports session-held-out testing only. Chartier et al. fitted per-participant models. Speaker-held-out testing is not "as in [2]". |
| 24 | M12 verdict "not reported" | Component table | inconsistent | The same row lists "Within-subject CV, span-shuffle null", so evaluation is reported. If the verdict means "test-split details missing", say so in the terms SKILL.md uses. |
| 25 | Chronology and fairness | References; labels | correct | No later work is treated as prior. [5] is labelled concurrent and used only as state of the art. The review attributes the DTW-inflation and "modest" caveats to the authors and does not present them as its own findings. |

**Central claim and confound.** The strongest confound for "articulatory beats phoneme" is a weak baseline that differs in form: a sparse 40-dim step train against a continuous, audio-derived, speaker-timed trajectory. The review handles this, marks it as inference and proposes a smoothed phoneme control. It also reports both absolute and relative change. Two confounds remain unaddressed. First, regularisation and dimensionality differ under elastic net (12/14 against 40 predictors). Second, for mode contrasts, aloud and silent use different feature sets as well as the warp; the review raises this but quotes no concession for it. The positions are otherwise tied to locations. Item 11 is the main place where the stated evidence does not support the wording.

## Required fixes (by impact)

1. M06 confound paragraph: replace "A 12-dimensional smooth trajectory" with "a 12- or 14-dimensional smooth trajectory (silent / aloud)". The current wording contradicts the Verdict and claim row 4.
2. "What the field needs next", M12: drop "speaker-held-out … as in [2]" or split it. Chartier et al. [2] support session-held-out testing only.
3. M06 usual approach: support "the target is the only surface-EMG study among them" with the deciding priors and a ledger locator, or remove it.
4. M02 usual approach: state the typical design of the 15 confirmed studies rather than only the earliest. Before calling [4] the earliest, check whether DTW alignment of audible to silent EMG was published before the 2016 dissertation (Janke et al., c. 2010), and cite that publication if so.
5. Add claim-table rows, with quotes and locations, for these values: 24 participants and "plotted only"; Chartier's 5 participants and p<1e-20; Lee et al.'s 8-electrode layout and single speaker; "z-scored EMG envelopes"; GETS on Gaddy data with DTW-transferred targets; the §II-C span-shuffle null; "± undefined"; folds, seeds and sessions unstated; and the "subvocal above chance" claim attributed to the authors.
6. Chartier comparator: the quote says "acoustic", but the text says "formant". Use the source's term or quote the passage that names formants.
7. Lee et al. [3]: write "about 0.9 for most articulatory features", as quoted.
8. M06 usual approach: change "124 use acoustic predictors" to wording that shows these are pattern-match hits (upper bound), as the Appendix does.
9. Verdict: limit "as the authors concede (§III-B)" to the DTW inflation, or quote a concession for the 12-vs-14 feature confound.
10. Variance partitioning: change "largest share on every channel" to "dominates across electrodes" (§III-A).
11. M12 verdict: resolve "not reported" against the row's own entry (within-subject CV listed), following the SKILL.md verdict rules.
12. M06 state of the art: say why Chartier et al. 2018 is still the reference, or name a later production-side articulatory-vs-phoneme encoding comparison if one exists.
13. References: remove the process notes ("arXiv v2 read"; "the wiki entry is filed under …") from the published list, or move them out of the review text.

## Scores

- Procedure: 7/10. The claim table covers the main numbers and the calculations are correct. About a dozen numbers and absence claims in the text have no quoted support.
- Final text: 6/10. The position is clear and fair to the authors. One factual slip (12 vs 14 dimensions), one over-attribution to [2], and two unsupported priority or absence claims lower the score.
