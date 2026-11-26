# Evaluator: a language model separate from the writer

Date: 2026-11-26. Independent evaluation of the review of Proix et al., "Imagined speech can be decoded from low- and cross-frequency intracranial EEG features" (Nat. Commun. 13, 48, 2022; bioRxiv 10.1101/2021.01.26.428315, posted 2021-01-26 per the preprint footer "this version posted January 26, 2021").

Inputs read: compact.md, the review .md, claims.md, slots.json, verdict.json, both topic audits; source texts: target (published `source/text.txt` and bioRxiv `source/text.txt`), Pei 2011 (pmc-3772685-vowelcons), Ikeda 2014 (pmc-3945950-covertvowel), Leuthardt 2011, Martin 2014 (doi-10.3389-fneng.2014.00014), Livezey 2019, Zhao 2026 (natneuro-02456-motordyn), Brumberg 2011 (doi-10.3389-fnins.2011.00065), Guenther 2009 (pmc-2784218-wireless). The released code (Zenodo 10.5281/zenodo.5702872) is not in the wiki or the work folder, so the code claims could only be checked against the notes.

## Claim check

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | "'Comparable to BHA' rests on imagined BHA passing in 1 pair" (Verdict); "'Comparable' (Abstract)" (Where the claims outrun, bullet 1) | Target abstract, Results, Introduction; preprint | Wrong | "Comparable" is not in the abstract of either version. It appears only for spatial power patterns (Results, "comparable, but not identical"). The authors' wording is Results: imagined BHA "did not yield better scores than with other bands (10 significant participant-representation pairs …) which were equally good using e.g., theta or beta power", and Introduction: "imagined speech could equally well be decoded from low- and cross-frequency features". The point stands, but the quote and location are wrong. |
| 2 | Imagined BHA: 1 pair at 0.61; power: 10 pairs at median 0.60 (IQR 0.59–0.63); CFC: 12 pairs at 0.60 (IQR 0.59–0.61); overt BHA: 15 pairs at 0.64 | Target Results, "Decoding" paragraphs | Correct | The numbers match. |
| 3 | "1 of 24 pairs (8 participants × 3 representations)" (inference) | Fig. 7 caption "N = 8, studies 1 and 2"; Results (three representation spaces) | Correct for BHA; insufficient quote | The claim-table "quote" q1 is the reviewer's own note, not source text. 24 is right for a single band. It is not shown to be the right denominator for the pooled "10" (three bands) or "12" (six CFC combinations) counts (see #4). |
| 4 | "about 6 of 24 pairs would pass on any of six tests by chance (inference); 12 did" | Results; Methods, Decoding | Insufficient evidence | This holds only if "12 participant-representation pairs" counts distinct pairs. If it counts significant cells (pair × CFC combination, 144 tests), the expected false positives are about 7.2 (inference). The paper's use of "8 significant pairs" for three non-BHA overt bands pooled suggests the cell reading. |
| 5 | No correction across representations, bands or combinations; per-subject inverse-binomial thresholds | Methods, Decoding | Correct | "Thresholds … obtained independently for each subject from an inverse binomial distribution". There is no family-wise correction for the decoding tests. |
| 6 | "The 0.60 medians are of passing pairs only" | Results | Correct | "10 significant participant-representation pairs, median performance 0.60". |
| 7 | Pei et al. fed 8–12 and 18–26 Hz amplitudes to the covert-word decoder | Pei 2011, Sec. 2.5 | Correct | "These four sets of features" (three bands plus LMP) went to a Naive Bayes classifier. |
| 8 | Ikeda: beta 55.6% vs high-gamma maximum 46.7% (chance 33.3%) | Ikeda 2014, Results; Table 5 | Correct, condition missing | 55.6% is one Broca's-area electrode in the beta block of Table 5. Both values are per-electrode maxima at uncorrected p < 0.05. |
| 9 | "Earlier low-frequency covert decoders are omitted [4], [2]"; Ikeda "uncited here" | Target reference list | Wrong for [4]; correct for [2] | The target cites Pei 2011 ("Decoding vowels and consonants in spoken and imagined words…") and does not cite Ikeda 2014 or Leuthardt 2011. |
| 10 | "The Discussion nonetheless says earlier covert decoders used 'only BHA features'" | Target Discussion | Overread | The sentence is "Previous studies attempting to decode covert speech using only BHA features obtained performances similar to …". It refers to the studies that used BHA only. It does not say that all earlier decoders did. The real gap is that the paper never credits Pei's or Ikeda's low-frequency inputs. |
| 11 | Overt: lower bands redundant with high gamma [8] | Livezey 2019, "Classification relevant information in lower frequency bands" | Correct | "No bands see a significant improvement … over … Hγ". |
| 12 | M06 usual approach: all 5 priors used gamma/high-gamma power, 2 also theta-to-beta, none coupling | Audit prior_tally; Leuthardt 2011 (75–100, 92.5–97.5, 410–420 Hz features); Pei; Ikeda; Martin 2014/2016 | Correct within the stated population; population boundary unstated | Guenther 2009 (cited by the target) and Brumberg 2011 are intracranial decoders of *attempted* speech in paralysed participants. Both decode from unit firing, not gamma power. They are in the wiki but outside the candidate set. Brumberg states the participant was "asked to attempt to speak, rather than simply imagine speaking". |
| 13 | Prior cutoff: "Before the preprint (2021-01)" (M06) vs "first public before 2020" (Appendix) | Audit cutoff_year 2020; preprint date | Inconsistent | Under the ±6-month rule, priors are those first public before 2020-07-26. The 2020-01 to 2020-07 window is not stated as checked. The 2020 candidates in the audit are MEG (Dash 2020, excluded as scalp) or overt only, so the counts probably do not change (inference). |
| 14 | All-years pattern counts (89 studies) not used as the usual approach | Body, table, Appendix | Correct | They appear only in the Appendix, labelled "all-years … mentions included". The table uses confirmed 5 / 4. |
| 15 | CFC input absent before the target (0 of 5; 34 full-text hits) | Audit fulltext_recall_check; recall_pac.txt | Plausible; scope narrower than the wording | The pattern required imagined/covert/inner-speech terms, so overt production decoders were out of scope by construction. Livezey 2019 (cited by the target) analysed β–Hγ amplitude–amplitude coupling beside a classifier and is not named as a deciding prior. I know of no pre-2020-07 intracranial or scalp imagined-speech decoder with PAC input, but I could not verify that further. |
| 16 | M12: 4 of 5 priors hold out trials or blocks within participant | Martin 2014, "Covert speech decoding" | Wrong for [5] | For covert speech, Martin 2014 "trained using data from the overt speaking condition" and applied the model to covert data. That is an overt-to-covert transfer, not a split of covert trials. The audit quote comes from the *overt* section ("90% … training set and 10% … testing set"). |
| 17 | Paper uses 10-fold CV with nested 5-fold feature selection | Methods, Decoding | Correct | |
| 18 | Code z-scores CFC features over all trials before folds | Notes t52 only (code not stored) | Insufficient evidence | No code excerpt or code version is stored. The claim-table quote is a paper sentence about band averaging. z-scoring along the trial axis is label-free, so its effect on accuracy is unknown (inference). The review states it as a fact without that qualification. |
| 19 | "surrogates number 200 in code against 1,000 in the text" | Methods: CFC ("randomly shuffling 200 times"); Fisher distance and pairwise correlation ("repeated 1000 times") | Imprecise, reads as wrong | The text itself uses 200 surrogates for the MI z-scores. The reported discrepancy (notes t54) concerns only the *feature-distance permutation* count. This is a descriptive analysis and not a test-partition issue, yet it sits under M12. |
| 20 | Classes hard-coded per participant | Notes t55 (getData_covert.m:15-31), not viewable | Insufficient evidence | Hard-coding a clustering result is not a flaw in itself. The review does not say why it matters. The related question for the authors (per-participant assignments) is fair. |
| 21 | Mouthing: three controls credited; authors' CFC caveat | Methods, Signal processing; Discussion | Correct | Both caveats are quoted accurately and credited. |
| 22 | SOTA M06: Zhao 2026, median 80.4%, chance 16.7%, 6 or 8 classes, 9 participants, tenfold CV, β1 input | Zhao 2026, Abstract; Results (Fig. 5i); Methods | Correct, conditions missing | Median 0.804 (IQR 0.590–0.808) is over all 9 participants. Chance 16.7% is the "median chance" (S6–S9 had 1/8). There are about 360 trials per modality (45–60 repetitions per syllable), against 7–24 per word in the target. Input comes from "SI encoding electrodes" chosen by an encoding analysis (whether that selection is fold-local is unverified). β1 (12–24 Hz) is a low-frequency feature, so this SOTA supports the paper's thesis. The review does not say so. |
| 23 | "4.8 against 1.2 times chance" (inference) | Arithmetic | Correct arithmetic, unequal comparison | 0.804/0.167 = 4.8 and 0.60/0.5 = 1.2. But the target's 0.60 is the median of passing pairs only (selected). Zhao's median covers all participants. |
| 24 | SOTA M12: Kunz 2025, closed-loop, sentences absent from training blocks, 14–33% WER (50 words), 3 participants | Kunz 2025, Results Fig. 3; STAR Methods (claim rows u1–u4) | Correct numbers, missing caveat | The best value (14%, T15) comes from a model with online retraining "up to and including during the evaluation block" (u3, already in the claim table). The review omits this, although it is a test-partition caveat. |
| 25 | M11 next step: realigned overt trials >80% for 3 of 4 participants, 6-class | Discussion; Supplementary Fig. 21 | Correct | The authors propose this themselves ("Future work will be necessary"). The review credits [1]. |

## Required fixes, ordered by impact

1. **Major. Verdict (sentence 5) and "Where the claims outrun the evidence" (bullet 1): misattributed quote.**
   - Evidence: "Comparable" / "Comparable to BHA" does not occur in either abstract (published or bioRxiv). The authors' claims are in the Results ("did not yield better scores than with other bands … equally good using e.g., theta or beta power") and the Introduction ("could equally well be decoded from low- and cross-frequency features").
   - Fix: quote the Results sentence with its location, e.g. "'Equally good' (Results, Decoding imagined speech) is measured against imagined BHA passing in 1 of 24 pairs …".

2. **Major. M06, "Against the field", and "Where the claims outrun", bullet 4: Pei 2011 is cited by the target, and the Discussion sentence is overread.**
   - Evidence: the target's reference list contains "Decoding vowels and consonants in spoken and imagined words using electrocorticographic signals in humans". The Discussion says "Previous studies attempting to decode covert speech using only BHA features obtained performances similar to …".
   - Fix: write "The paper cites Pei et al. [4] but not its 8–12 and 18–26 Hz inputs, and does not cite Ikeda et al. [2] (or Leuthardt et al. [3]); its Introduction frames BHA as the prior covert feature." Drop "nonetheless says earlier covert decoders used 'only BHA features'". Change bullet 4 to "Ikeda et al. is uncited and Pei et al.'s low-frequency inputs are not acknowledged".

3. **Major. "Where the claims outrun the evidence", bullet 2, and the M06 verdict sentence: the multiple-testing arithmetic depends on an unresolved denominator and can contradict the verdict.**
   - Evidence: if "12 pairs" are distinct pairs, the review's own figures (6.4 expected of 24 at p = 1 − 0.95^6) give P(X ≥ 12) ≈ 0.01 (inference), which undercuts "lacks an effect separated from multiple testing". If "12" counts significant cells out of 144 (pair × six combinations), about 7.2 are expected and P(X ≥ 12) ≈ 0.06 (inference). Power's 10 of 72 cells is then P ≈ 0.003 (inference), so CFC has the lower per-test pass rate. The paper's "8 significant pairs" for three pooled overt bands points to the cell reading.
   - Fix: settle the reading from Fig. 7 (count the orange circles per panel) and state it. Under the cell reading, write "12 of 144 participant-representation-combination tests passed, against about 7 expected at 5% (inference); power passed 10 of 72". Under the pair reading, state that 12 exceeds the rough family-wise expectation and base the verdict on fix 4 instead.

4. **Major. M06 verdict reasoning (Verdict; M06 last paragraph; slots.json M06 note).**
   - Evidence: the `ahead` rule needs (a) 0 of N ledger designs (met: 0 of 5 plus the full-text check), (b) deciding priors read (met), and (c) an effect shown with repetition. CFC passed in participants of two datasets (12 "pairs", Fig. 7), so (c) is arguably met unless the review gives protocol reasons. The review's reasons mix protocol points (no correction, no test against power) with a results point (equal selected medians, 0.60 vs 0.60). Its strongest protocol point is in M12 instead: the pre-fold z-scoring applies to the CFC classifier scripts only (notes t52).
   - Fix: state why (c) is not met in protocol terms: per-subject uncorrected thresholds; the count unresolved or not above the family-wise expectation (fix 3); label-free but test-inclusive z-scoring applied only to CFC features (marked inference as to effect); no single CFC combination shown repeatedly. Remove the equal-medians argument as a reason, or label it descriptive, since the medians are of selected pairs.

5. **Major. M12 "Usual approach", Appendix M12 counts, and slots.json M12 (`matched` 4): Martin 2014 is miscounted.**
   - Evidence: Martin 2014, Covert speech decoding: "the decoding model was trained using data from the overt speaking condition. Second, the same model … was applied to data from the covert condition". The audit quote supporting a trial split comes from the overt-speech section.
   - Fix: write "3 of 5 hold out covert trials within participant [4], [2], [6]; Martin et al. trained on overt and tested on covert trials of the same session [5]; Leuthardt et al. tested online after a screening run [3]". Update the Appendix line and `matched` to 3. The usual approach (within-participant, same session) and the `standard` verdict are unchanged.

6. **Major. Population boundary for M06/M12 (Usual approach "all 5"; Appendix inclusion rule).**
   - Evidence: Guenther et al. 2009 (PLoS ONE; wiki pmc-2784218-wireless; cited by the target) decoded attempted vowel production online from intracortical units in a locked-in participant. Brumberg et al. 2011 (Front. Neurosci.; wiki doi-10.3389-fnins.2011.00065) classified "intended phoneme production" offline from units. The inclusion rule ("imagined, covert or inner speech") neither includes nor excludes attempted speech without output. Neither study is in the candidate set, because the ledger pattern does not match "attempted/intended". Including them makes gamma/high-gamma input 5 of 7 and online tests 2 of 7.
   - Fix: add to the Appendix inclusion rule: "attempted speech by paralysed participants (e.g. Guenther 2009, Brumberg 2011; unit-firing inputs) excluded". Alternatively, include them and change "all 5" to "5 of 7 field-potential decoders; 2 decoded unit firing".

7. **Major. M12 "State of the art" and table row M12: Kunz 2025 caveat omitted.**
   - Evidence: claim-table entry u3: T15's model "employed online retraining … even the sentences decoded in real-time were involved in continually retraining the model throughout the session up to and including during the evaluation block". T15 gives the 14% end of "14% to 33%".
   - Fix: add "(T15's decoder was retrained online during the evaluation block; T12 and T16: 24% and 33%)" or quote only T12/T16 as the uncontaminated values.

8. **Major. M12 last paragraph and "Questions for the authors" (surrogates): the code claims are imprecise and unanchored.**
   - Evidence: the target Methods use 200 surrogates for MI z-scores ("randomly shuffling 200 times") and 1,000 permutations for Fisher distances and correlations. The 200-vs-1,000 discrepancy (notes t54) concerns only the feature-distance permutation, a descriptive analysis unrelated to the test partition. No code excerpt or code version is stored. The claim-table quotes for row 14 are paper sentences, not code.
   - Fix: write "the released feature-distance scripts permute labels 200 times where the Methods state 1,000 (clustering_fisher_grouping.py:54-55, 207-214; Zenodo 10.5281/zenodo.5702872)" and move it out of M12 (or to the Questions only). For the z-scoring, add "label-free, but test trials enter the scaling; effect on accuracy not measured (inference)". Either say why hard-coded classes matter (the paper does not list the assignments) or drop it from the body. Store the quoted code lines in notes.

9. **Minor. M06 "Usual approach" vs Appendix: cutoff wording.**
   - Evidence: the preprint was posted 2021-01-26, so priors are those first public before 2020-07-26 (±6-month rule). The Appendix uses "before 2020", while the body says "Before the preprint (2021-01)".
   - Fix: state "first public before 2020-07 (six months before the 2021-01-26 preprint); no intracranial imagined-speech decoder in 2020-01 to 2020-07 among the candidates (Appendix)". Apply the same wording in both places.

10. **Minor. M06 "Usual approach", last sentence: "tests low-frequency power across three datasets".**
    - Evidence: decoding (Fig. 7) excluded study 3 ("study 3 was excluded, as it contained only three syllables"). Only the spectral and CFC mapping used all three datasets.
    - Fix: "decodes from low-frequency power and CFC in two datasets (8 participants)".

11. **Minor. Verdict and M06: the Ikeda comparison lacks its condition.**
    - Evidence: 55.6% is a single Broca's-area electrode (Table 5, beta block). 46.7% is the per-electrode high-gamma maximum. Both are uncorrected p < 0.05 per electrode.
    - Fix: add "best single electrodes, uncorrected". Apply the same multiple-testing standard used for the target, or soften "beta beating high gamma" to "a beta-band electrode exceeding the best high-gamma electrode".

12. **Minor. M06 novelty sentence: deciding prior and scope.**
    - Evidence: the full-text check pattern required imagined/covert terms. Livezey 2019 (cited by the target) analysed β–Hγ coupling beside an overt classifier and found the lower bands added nothing.
    - Fix: write "None of the 5 priors, and none of 34 full-text coupling hits on imagined or covert speech up to 2021 (Appendix), uses coupling as decoder input; Livezey et al. analysed β–high-gamma amplitude coupling in overt speech but did not feed it to the classifier [8]".

13. **Minor. M06 body: process wording.**
    - Evidence: "a full-text check of all wiki papers up to 2021 (34 hits)" exposes internal process in the body.
    - Fix: phrase it as an Appendix-backed absence claim, as in fix 12.

14. **Minor. M06 "State of the art": the comparison conditions and the credit to the paper are missing.**
    - Evidence: Zhao's median covers all 9 participants, while the target's covers passing pairs only. Zhao has about 360 trials per modality (45–60 repetitions per syllable) against 7–24 per word in the target. Chance 16.7% is the median (1/8 for S6–S9). The input is β1 (12–24 Hz), a low-frequency band.
    - Fix: add the trial counts and "median chance", drop or qualify the 4.8 vs 1.2 ratio, and add one clause: "a later low-frequency (β1) decoder, consistent with the paper's direction".

15. **Minor. Verdict: credit the authors' own concessions.**
    - Evidence: the Discussion says "binary classification far from a real imagined speech BCI setting" and that the quantitative comparison with BHA studies "is difficult considering differences in study designs".
    - Fix: acknowledge these where the Verdict says "not parity with a working decoder", so the review does not present a conceded point as its own finding.

16. **Minor. Verdict sentence 2: "Low-frequency power is standard".**
    - Evidence: 2 of 5 is precedent, not the usual approach. The usual approach is gamma/high-gamma (5 of 5).
    - Fix: "Low-frequency power has precedent (2 of 5 earlier decoders, Appendix)".

17. **Minor. Claim table rows 15–16: q1 is not a source quote.**
    - Evidence: q1 reads "At the reported pair-count level, 8 participants × 3 representation spaces = 24 …", which is a derivation.
    - Fix: cite the Fig. 7 caption ("N = 8, studies 1 and 2") and the Results naming the three representation spaces, and keep "(inference)".

## Scores

- Procedure: 6/10. The prior set was read in full and is mostly right. The audits are traceable and the pattern counts are kept out of the usual approach. But one prior's test partition was miscoded, the attempted-speech boundary is unstated, and the code claims rest on notes without excerpts.
- Final text: 5/10. The position is clear and most numbers match. But one quote is misattributed, the claim that Pei is uncited is wrong, the multiple-testing argument can contradict the verdict, and the SOTA caveat for M12 is missing.

What is right, briefly: the target's decoding numbers, the Pei/Ikeda low-frequency inputs, the Livezey redundancy result, the uncorrected per-subject thresholds and the credit for the mouthing controls all check out. The all-years counts are correctly kept to the Appendix.

Counts by severity: critical 0, major 8, minor 9.
