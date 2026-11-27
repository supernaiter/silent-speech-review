# Evaluator: a language model separate from the writer

Date: 2026-11-27. Scope: `compact.md`, `decoding-spoken-phonemes-from-sensorimotor-cortex-with-high-density-ecog-grids.md`, `slots.json`, `verdict.json`, the three topic audits, and the source texts in the wiki for the target (`doi-10.1016-j.neuroimage.2017.10.011/source/text.txt`, PMC6433278), Branco 2017 (`pmc-5322832-s1ecog`), Zhao 2026 (`natneuro-02456-motordyn`), Duraivel 2023, Wilson 2020, Chen 2024, Kellis 2010, Mugler 2014, Heger 2015 and the Matthews 2012 thesis. No file was modified.

## Claim table

| # | Claim (location in review) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target first public 2017-10-07; prior cutoff 2017-04; [concurrent] 2017-04 to 2018-04 (header, Appendix) | Target text l.4 "Neuroimage. 2017 Oct 7;180(Pt A):301–311" | correct | The ±6-month window is applied correctly. The wiki manifest for the target gives the wrong authors and "published 2018-02-15"; the review correctly uses the paper's own byline (Ramsey, Salari, Aarnoutse, Vansteensel, Bleichner, Freudenburg). |
| 2 | Branco 2017 is prior (first public 2016-12) | DOI 10.1016/j.neuroimage.2016.12.004; the target's reference list cites it as "Branco et al., 2016" | correct | It is well over 6 months before the target, and it is the authors' own paper, so treating it as a deciding prior is fair. The inclusion rule counts the authors' own gesture decoders. |
| 3 | Same template method as Branco: one channels-by-time template per class, highest Pearson correlation, leave-one-out, 3-mm HD grids, five patients, 76.25% over S1 (M06) | Branco, Feature Classification; Subjects; Results | correct | Branco also writes that the method "previously yielded robust results when used to discriminate spatial patterns ... Here we extended this method to spatiotemporal patterns". The spatial version goes back to Bleichner et al. 2016 (*Brain Struct Funct* 221:203–216), which the review does not name. |
| 4 | "The target ... cites that paper only for alignment (Sec. 4)" (M06) | Target Sec. 1, 2.1, 2.3, 4 | wrong | Branco et al. 2016 is cited in Sec. 1 (S1 decoding), in Sec. 2.1 and the Fig. 1 legend (electrode localization), in Sec. 2.3 (common average reference) and in Sec. 4 (alignment). What is true is that it is never credited as the source of the STMF classifier. |
| 5 | "The 12-point temporal gain is significant for five classes only (p=0.046)" (Verdict; Timing bullet) | Target Sec. 3.3; Table 2 | wrong as stated | p=0.046 (5-class) and p=0.064 (4-class) hold for the 1-s window. But Sec. 3.3 goes on: in the optimal 0.5-s window the STMF–SMF difference is "significant for the 4- and the 5-class classification at p<=0.05" (72.4 vs 55.7; 74.5 vs 59.7). |
| 6 | 75.5 → 63.5 (12.0 points, 19% relative); 71.9 vs 60.3, p=0.064 (Timing bullet) | Table 2; Sec. 3.3 | correct | 12.0/63.5 = 18.9% (inference is labelled). |
| 7 | Trials aligned to audio-marked VOT in Praat (Sec. 2.2) | Sec. 2.2, 2.3 | correct | Sec. 2.3 adds that rest trials are cut at "rest trial temporal mid points". The review does not use this (see fix 4). |
| 8 | Branco names systematic onset differences that "may inflate classification" and aligns on the neural response | Branco, Methods, Trial alignment | correct | The quote matches. |
| 9 | Pre-onset window: 64.0% (5-class), 58.3% (4-class, chance 28.8%) | Table 2; Sec. 4 | correct | |
| 10 | "decoding does not depend entirely on sensory feedback" (authors' quote) | Sec. 4 | correct | The authors concede the limitation themselves (Sec. 4: "it is not possible to predict ... where there is no somatosensory feedback"; actual movements carry "a certain degree of confound due to somatosensory feedback activity"). The review does not credit this. |
| 11 | SVM matches STMF: 77.2% and 72.9%, p>0.3 (M06) | Sec. 3.1; Table 2 | correct | |
| 12 | 3–4 mm grids, 32–72 analysed electrodes (M05) | Sec. 2.1; Table 1 | correct | |
| 13 | Abstract quote on HD grids; no density manipulation (M05) | Abstract; Sec. 3.2, 4 | correct | Sec. 4 rests the density claim only on informative electrodes clustering "within spaces of a square cm". No subsampling is reported. |
| 14 | 500 shuffles (120 for SVM), leave-one-trial-out (M12) | Sec. 2.4 | correct | |
| 15 | M12 tally: k-fold 12, LOO 2, holdout 1, jackknife 1, online 1, permutation 5 | M12 audit `prior_tally_<slug>` | correct | 12+2+1+1+1 = 17. Permutation is counted separately (Pei, Martin 2014, Mugler, Bouchard, Martin 2016), so the counts are internally consistent. |
| 16 | M05 tally: clinical 11, intracortical/depth 4, micro/HD ≥1 participant 4 (only 2) | M05 audit | correct as tallied | Leuthardt 2011 and Herff 2015 sit in two bins, which the wording allows. The bins are defined inconsistently, though (fix 9). |
| 17 | M06 tally: trained 15, nearest centroid 1 (Kellis), power-threshold 1 (Leuthardt) | M06 audit; Kellis, Methods | correct | |
| 18 | Population 17 complete; known-item recall 1.0 (7 target-cited decoders) | Target reference list vs audit seeds | insufficient | Four prior speech decoders that the target cites are not in the ledger at all: Blakely 2008, Bouchard & Chang 2014 (EMBC), Mugler 2015 (EMBC) and Jiang 2016 (EMBC). Recall 1.0 counts only the seeds present in the wiki. |
| 19 | Zhao 2026: median 78.3% overt, 80.4% imagined, six or eight classes, 256-ch HD-ECoG, nine participants (M06 SOTA) | Zhao, Abstract; Results; Methods | correct | Missing conditions: Mandarin syllables, awake tumour surgery, β1 features, median chance 0.167. |
| 20 | Duraivel 2023: up to 57% nine-way (chance 11.11%), four patients; subsampled to standard spacing 20–35% (M05 SOTA) | Duraivel, Results | correct, but a maximum | 57% is the single best subject and position (S1-P1). The mean P1 over four patients is 49.9%. The quote for "20–35%" is too thin to show the condition. |
| 21 | Chen 2024: PCC 0.765 on unseen participants, leave-one-subject-out (M12 SOTA) | Chen, Results | correct | The metric is spectrogram-reconstruction PCC over 43 unseen participants, not classification accuracy. The M12 audit labels it `timing: prior`, which contradicts the review's correct [later]. |
| 22 | Wilson 2020: artifacts "in ECoG and intracortical recordings"; removing them cut accuracy 29.3% → 25.8% | Wilson, Results | partly wrong | Wilson measured intracortical arrays only. The ECoG part is Wilson citing Roussel et al. The 29.3 → 25.8 figure is for intracortical HLFP at 125–5000 Hz after LRR. Wilson also quantifies the timing confound ("phoneme onset differences modestly increased decoding accuracy", mitigated by a neural onset marker), which the review leaves unused. |
| 23 | Post-onset 65.3% vs centred 72.4% (4-class) | Table 2 | correct | |
| 24 | SVM separates rest from speech at 92.8% (Table 2) | Table 2 | correct, but the wrong classifier | The headline is STMF, and STMF 2-class is 87.6%. The authors raise the rest-dominance caveat themselves (Sec. 3.1; Sec. 4: "classification can be biased by a single class, in our case most likely the rest condition"). |
| 25 | Field-comparison quote and authors' qualification (Sec. 4) | Sec. 4 | correct | It is credited. The bullet adds little beyond restating it. |

## Required fixes, ordered by impact

1. **High: Verdict sentence 5 and the Timing bullet ("significant for five classes only").**
   - Evidence: Sec. 3.3 reports the STMF–SMF difference "significant for the 4- and the 5-class classification at p<=0.05" in the 0.5-s centred window. Sec. 3.1 says STMF is "well over 10% better performance in all comparisons". The "five classes only" statement holds only for the 1-s window.
   - Fix: "In the 1-s window the temporal gain is significant for five classes (p=0.046) but not four (p=0.064); in the 0.5-s window the authors report p≤0.05 for both (Sec. 3.3), with five participants and one (R1) showing no gain (Sec. 4)."
   - The timing-confound argument still stands, because it applies to both windows.

2. **High: M06 paragraph ("cites that paper only for alignment (Sec. 4)").**
   - Evidence: Branco et al. 2016 is cited in Sec. 1, Sec. 2.1 (and the Fig. 1 legend) and Sec. 2.3, as well as Sec. 4.
   - Fix: replace with the accurate charge. The target cites [2] for localization, re-referencing and alignment, but not as the source of the STMF classifier. Sec. 4 instead lists the matched filter ("Fourth, we employed a classification technique ...") and the temporal concatenation ("Third, ... more fine-grained temporal evolution ... than previous studies") among the factors that set it apart from previous studies.
   - Optionally add that [2] itself presents the method as an extension of the group's earlier spatial template classifier (Bleichner et al. 2016, *Brain Struct Funct* 221:203–216; cited by the target).

3. **Medium: rationale for the M06 and M05 verdicts against the rule (Verdict; M06; M05; 13-components table).**
   - Evidence: SKILL.md defines `standard` as "matches the usual approach ... or the difference is not supported well enough to call". The target does not match the usual approach on either slot: template correlation in 1 of 17 versus a trained decoder in 15 of 17, and HD in every participant versus clinical grids in 11 of 17. The prose gets to `standard` through a prior that has the same design, which is an argument against `ahead`, not for "matches the usual approach". In the table, "Trained decoder (15)" and "Clinical grid (11)" sit next to "standard" with no explanation.
   - Using Branco 2017 is fair: it is prior, by the same authors, and the inclusion rule counts it.
   - Fix for M06: "Departs from the usual approach (15 of 17 trained) but is not ahead: [2] and [4] already classify by class-mean template or centroid, and a linear SVM equals it (p>0.3), so the difference is not supported: standard."
   - Fix for M05: "Not ahead: Kellis 2010, Bouchard 2014 and Herff 2015 (one participant) recorded with micro- or HD arrays (Appendix); no density test supports a gain: standard."

4. **Medium: a confound the review misses, the rest-epoch anchoring ("Field comparison" bullet).**
   - Evidence: Sec. 2.3 says HFB was "divided into trials based on the VOT markers or rest trial temporal mid points". Phoneme epochs are locked to an acoustic event about 0.8 s after the cue (Sec. 2.2). Rest epochs are locked to a time point with no event.
   - Consequence: part of the rest-versus-phoneme separation, and so part of the 5-class and 2-class scores, may reflect the different anchoring rather than speech content (inference).
   - Fix: state this, and use the STMF 2-class value (87.6%) rather than the SVM's 92.8%, since the headline being questioned is STMF.

5. **Medium: authors' own caveats presented as review findings (Timing, Feedback and Field-comparison bullets; "What the field needs next").**
   - Rest dominance and the 4-class analysis are the authors' own (Sec. 3.1; Sec. 4 "classification can be biased by a single class ..."). So "lead with four phonemes" asks for something they already report.
   - Problems with VOT alignment and the HFB-alignment remedy citing [2] are the authors' own (Sec. 4: "less accurate VOT determinations ... One way to solve this would be to align trials based on the timing of the HFB response").
   - The somatosensory-feedback limitation is the authors' own (Sec. 4 limitations).
   - Fix: credit each to the authors in one clause. Keep as the review's contribution only what it adds: the inflation direction of the onset bias (via [2]), the closure-before-VOT mechanism, and the anchoring point in fix 4.

6. **Medium: the Acoustics bullet.**
   - Wilson et al. [8] measured contamination in intracortical arrays only. Its ECoG statement cites Roussel et al. The 29.3% → 25.8% figure is for intracortical HLFP at 125–5000 Hz after linear-regression referencing, a different band from the target's 65–125 Hz.
     - Fix: give that condition. Cite Roussel et al. 2020 (*J Neural Eng*, "Observation and assessment of acoustic contamination of electrophysiological brain signals during speech production and sound perception", [later]; locator unverified) for ECoG.
   - The pitch-overlap inference holds mainly for the three male speakers (R2, L1, L2; Table 1). Four of the five recordings were hardware band-limited at 134.4 Hz (Sec. 2.1).
     - Fix: add both conditions.
   - "Not discussed (Sec. 1)" points an absence at one section.
     - Fix: point it at the whole paper.
   - The bullet takes no position, and its own evidence (a small LRR effect, the post-onset window scoring lower) argues that contamination does not carry the result.
     - Fix: state that plainly ("untested, but unlikely to carry the result"), or drop the bullet.

7. **Medium: population completeness and known-item recall (Appendix; M05 usual approach).**
   - Evidence: the target cites four prior intracranial speech decoders that are absent from the ledger.
     - Blakely et al. 2008, EMBC, "Localization and classification of phonemes using high spatial resolution ECoG grids". The target's Sec. 4 says these used "similar grids as the ones we used".
     - Bouchard & Chang 2014, EMBC, HD-ECoG vowel decoding. This is a different paper from P11, the 2014 J Neurosci paper.
     - Mugler et al. 2015, EMBC.
     - Jiang et al. 2016, EMBC, three vowels at 73%, a timing-based decoder.
   - "Known-item recall 1.0 (7 target-cited decoders)" therefore counts only the seeds present in the wiki. Against the target's own reference list it is 7 of 11 (inference).
   - Fix: add one Appendix line naming the four as "target-cited, not in ledger". In M05, name Blakely 2008 as an earlier HD-grid phoneme classifier the authors themselves cite. The HD/micro count rises to at least 6 (inference), and the verdict is unchanged.

8. **Low: version duplicates in the population (Appendix).**
   - Heger et al. 2015 (Interspeech; Sec. 2.1: "Seven epileptic patients ... Albany Medical Center") appears to share participants and recordings with Herff et al. 2015 (P15). That is the same basis on which Guenther 2009 and Brumberg 2009 were merged.
   - The Matthews 2012 thesis (P07) analyses data from the Neural Signals and Guenther collaboration (thesis introduction and acknowledgements), probably the same participant as P01 and P03.
   - Kanas 2014 (speech activity detection) has a target that is arguably not speech content.
   - Fix: merge them, or justify each in one line. The counts shift by 1–2 (for example, k-fold 12 → 11).

9. **Low: inconsistent M05 bins (Appendix; M05).**
   - The inclusion rule defines HD-ECoG as "about 4 mm", yet the clinical bin is "4–10 mm or 1 cm". The target's own L2 and L3 grids are 4 mm.
   - Fix: make the bins disjoint (for example, ≤4 mm = HD).

10. **Low: the timing confound can be sharpened (Timing bullet).**
    - Each test trial is epoched on its own audio VOT (Sec. 2.3). That oracle onset is not available in a silent or attempted-speech BCI, which is a separate problem from class-specific latency.
    - Wilson 2020 [8] puts a size on the onset confound: it "modestly increased decoding accuracy" and was mitigated by a neural onset marker.
    - Fix: add both in one sentence.

11. **Low: M05 state of the art.**
    - 57% is a single-subject, single-position maximum.
    - Fix: give the mean P1 of 49.9% over four patients, or the direct density contrast in the same Results section (four-way vowels: µECoG 71% vs ECoG 36.7%). Quote the full condition behind "20–35%".

12. **Low: M06 state of the art.**
    - Fix: add Zhao's conditions (Mandarin syllables, awake tumour surgery, β1 features, median chance 0.167) so that the medians over 6–8 classes are not read directly against a mean over 4 classes.

13. **Low: M12 state of the art and audits.**
    - Fix the state-of-the-art line: say that Chen's 0.765 is spectrogram PCC for speech synthesis over 43 unseen participants. (A peer-reviewed version of Chen 2024 may exist; unverified.)
    - Fix the audits: the M12 audit's `tally_<slug>` marks Chen `timing: prior`. The M05 audit's `tally_<slug>` carries stale values from the Kellis review (usual approach n=2, population 3, read_prior from 2008–2009). Correct both.

14. **Low: Questions for the authors.**
    - "Were templates ... computed without the held-out trial?" is already answered for the templates. Sec. 2.4 says "all trials except for one were used to screen the electrodes", and the Fig. 4 legend says "over trials and leave-one-out training sets".
    - Fix: narrow the question to the run-wise z-score (Sec. 2.3), which is computed over the whole run including the test trial.

15. **Low: restatement in the body.**
    - The Branco sentence (five patients, 76.25% over S1, four gestures) summarises the prior beyond what the verdict needs.
    - The Field-comparison bullet mostly restates the authors' claim and their own qualification.
    - Fix: trim both to the point that carries the position.

16. **Low: bibliography.**
    - Fix: give the Branco reference [2] its volume and pages (*NeuroImage* 147:130–142, per the target's reference list).

Also checked:
- No [later] or [concurrent] work is treated as prior.
- Every number in the claim table matches its quote, apart from findings 1, 2, 6 and 11.

## Scores

- Procedure: 7/10. Dating, the tallies and the quote checks are sound. The population misses four target-cited decoders and has probable duplicates.
- Final text: 6/10. There are two factual errors about the target, the uncredited author caveats need fixing, and the rest-anchoring confound is missed.

Counts: High 2, Medium 5, Low 9.
