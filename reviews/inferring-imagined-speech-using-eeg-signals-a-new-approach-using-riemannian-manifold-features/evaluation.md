# Evaluator: a language model separate from the writer

Date: 2026-11-26. Inputs read: the review (`<slug>.md`), `compact.md`, `claims.md`, `<slug>.slots.json`, `verdict.json`, both topic audits, the target full text (wiki `doi-10.1088-1741-2552-aa8235/source/text.txt`), Tates et al. (`read-essex-43678-riemann/text.txt`), Singh & Gumaste (`read-arxiv-1911.04255/text.txt`), and the wiki sources of the 5 target-time priors, plus wiki searches for other pre-2017 scalp-EEG covert-speech decoders and later same-dataset results. Nothing in the wiki or the review files was changed.

## Claim table

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Tangent+RVM beats Log+LDA, DaSalla, Min on vowels at p = 6×10⁻⁵, 2×10⁻⁵, 5×10⁻⁵, t(7) (M06) | Target Table 4(a) | correct | Values and df match. |
| 2 | Not significant vs Log+LDA on short words (p = 0.055) and short-versus-long method 1 (p = 0.091); "two of 12" (Verdict, M06) | Table 4(b), 4(c) | correct | 12 = 3 + 3 + 3 (method 1) + 3 (method 2) Tangent+RVM cells. No multiple-comparison correction in the paper; the review does not say so (finding M3). |
| 3 | RVM vs ELM 49.0/45.2 (p = 0.01), 50.1/46.6 (p = 0.02), 73.3/76.3 (p = 0.16) (M06) | §6.1 | correct numbers; wording "trails" wrong | p = 0.16 is not significant; the authors call it "quite equivalent"; RVM method 2 (80.1%, Table 2) exceeds ELM 76.3% (finding M4). |
| 4 | Pipeline is the Riemannian BCI approach the authors cite (§6.2) | §6.2 | correct quote, wrong use | §6.2 cites motor-imagery BCI work (Barachant, Congedo, Yger), a setting the M06 inclusion rule excludes (finding H1). |
| 5 | Analysed interval contains the word-specific visual cue (§4.1) | §4.1, §5.2 | correct | The authors say this themselves and give a reason (to exclude auditory evoked activity); the review does not credit them (finding M6). |
| 6 | Tates [2] "reports lower accuracy when segments of one trial share a fold"; "the authors state that the original cross-validation inflated accuracy" (Verdict, M12) | Tates §II-D, §III-A, §IV, §V | quote correct; conclusion not checked against the target | Target §5.2 splits by trials (270/30), and §6.1 labels each test trial by a vote over its three epochs, "the same procedure ... as in our proposed approach". Tates's stratified CV uses 1.4 s segments at a 0.1 s stride, not the target's protocol (finding H3). |
| 7 | Pooled median 0.89 → 0.74, 0.55 after imagery (M12) | Tates §III-A | correct numbers, missing condition | These are pairwise two-class contrasts pooled over participants. Tates reads the 0.55 sanity check as support for task-related decoding on this dataset (finding L1). |
| 8 | Tates attributes the best contrast to muscle tension and the cue (Verdict) | Tates §IV | correct | Participant 14: muscle; Participant 10: visual cue. |
| 9 | One channel and one band reach 0.609 for one participant; linked to length difference (Claims list) | Tates §III-B | number correct, attribution loose | Tates explains Participant 10 by the visual cue (posterior alpha), not by word length (finding L2). |
| 10 | Singh & Gumaste 58.6% vowels, 60.35% short words; ts+rvm column copied; subject sets differ (M06 SOTA) | Singh abstract, Table 7, §3.1 | numbers correct; caveat incomplete | Singh uses stratified 10-fold over 900 epoch samples per subject (3 per trial, shuffled), the leakage design Tates criticises. Singh's own same-subset baselines are 49.2% and 49.3%, not 49.0% and 50.1% (finding H4). |
| 11 | Singh 2019 is the state of the art for M06 | Wiki `doi-10.1109-access.2021.3116196` | wrong (insufficient search) | Panachakel & Ganesan 2021 (IEEE Access 9, [later], same ASU dataset) report vowel κ 0.78 ± 0.06 (about 85% accuracy, inference) and a minimum of 79.7% for vowels, testing on whole held-out trials with augmentation in training only (finding H4). |
| 12 | 5 prior decoders; 3 CSP, 3 SVM, 2 LDA; usual design "SVM, LDA or ELM, 5 of 5" (M06, Appendix) | Wiki full texts of the 5 priors | partly wrong | Yoshimura et al. 2016 (`pmc-4853397-covertvowel`) decodes with sparse logistic regression on cortical currents; `arxiv-1705.07771` uses CSP plus CRNN. The "5 of 5" count only holds for the negative "no Riemannian features" (finding M1). |
| 13 | None of the 5 priors used Riemannian features (Verdict, Appendix) | Wiki search, outside knowledge | correct but population incomplete | Torres-García et al. 2012 (BIOSIGNALS, wiki `doi-10.5220-0003769603700373`) is a pre-2017 scalp-EEG unspoken-speech decoder missing from the 5 (DWT plus NB/RF/SVM). I know of no imagined-speech EEG decoder before mid-2017 that used covariance tangent-space features (unverified beyond the wiki) (finding M2). |
| 14 | M12: 4 of 5 state chance, 1 of 5 permutation (Appendix) | Full-text counts of the 5 | correct | Deng 2010, Yoshimura 2016, s41133 2016 and Min 2016 mention chance; arxiv-1705.07771 does not. Yoshimura has the permutation tests. |
| 15 | M12 table cell "Within-subject CV, chance stated, untested ... (pattern match 4)" | Audit M12 | insufficient evidence | The 4 counts only chance-term mentions. "Untested" is not counted, and one of the 4 (Yoshimura) ran permutation tests (finding M8). |
| 16 | M12 standard; not behind | SKILL verdict rules | correct | Only 1 earlier paper (fewer than 3) meets the permutation-test condition. |
| 17 | Blocked recording 99.3 ± 1.4%, "erroneously optimistic" (M12) | §6.1 | correct | Correctly credited to the authors. |
| 18 | "the field's top ledger value, 96.4% for four classes" [5] (M12) | Audit `sota_candidates` | wrong | The audit lists 7 higher values (100, 99.67, 99, 98.81, 98.1, 97, 97) (finding M9). |
| 19 | Comparators are best grid means scored with 20 random 90%/10% splits (Claims list) | §6.1 | partly correct | "20 cross validations" is stated for DaSalla and Min, not for Log+LDA. "Best mean" is stated for all three (finding L3). |
| 20 | CSP count 6–14 and kernels per subject, no stated selection set (Claims list; M03) | §5.2 | correct, incomplete | The text shows the choices were driven by observed accuracy ("we found ... did not provide any improvement", "the highest accuracy in this case is obtained by ..."). M03 is `not_reported` with a filled cell (finding M7). |
| 21 | Complexity: 66.2% (2-class) vs 50.1% (3-class); margins 16.2 and 16.8 (inference); κ 0.32 and 0.25 | Table 2 | arithmetic correct; argument weak | κ already corrects for class count, so equal raw margins over chance do not refute the claim (finding M5). |
| 22 | Abstract 70% and 95% are single-subject maxima; best group mean 80.1% | Abstract, Table 3, Table 2 | essentially correct | They are single-fold maxima within one subject (Table 3 min÷max). Table 3 even shows 96.9% for S9, method 2 (finding L4). |
| 23 | Vowels and short words on different subject sets (Claims list) | Table 2 | correct | They overlap in S5, S8 and S12 only. |
| 24 | Repetition 8, 6, 6 and 6 of 15; one run; no seed (M12) | Table 2, §5.2 | correct | |
| 25 | Chronology: Tates, Singh, Jahangiri [later]; arxiv-1705.07771 prior | Target header, audit | correct under the audit's date; date choice open | The target was accepted on 26 July 2017. If the accepted manuscript went online then, first public is 2017-07 and arxiv-1705.07771 (May 2017) is [concurrent] (finding L5). |

## Findings, ordered by impact

### H1. High. M06 verdict justified with a different setting
- Location: Verdict sentence 2; M06 paragraph ("The method is not new to BCI, as the authors state"); `slots.json` M06 note ("cited BCI pipeline").
- Evidence: The M06 inclusion rule limits the population to scalp-EEG imagined/covert/inner speech and says "motor-imagery-only BCI studies are outside the population". Yet the main reason given for `standard` is that the pipeline is "the Riemannian BCI approach the authors cite (§6.2)", which is motor-imagery work (Barachant, Congedo, Yger). Within the stated setting the design is absent in 0 of 5 priors (Appendix). The effect is repeated over subjects (8 for vowels, 6 for the other tasks, Table 4), and the one deciding prior named (Min [3]) was read. The `ahead` conditions are therefore close to being met on their face. `standard` can only rest on the second half of the rule: "the difference is not supported well enough to call".
- Fix: Keep `standard`, but give a reason that belongs to the setting. The gain is measured against baselines at or below chance, run under a different protocol, with uncorrected multiple tests and selection on the evaluation folds (H2, M3, M7). Say plainly that the design is new to imagined-speech EEG (0 of the priors, Appendix). Present the motor-imagery origin as context only ("transferred from motor-imagery BCI, §6.2"), not as the reason for the verdict. Change the `slots.json` note to match.

### H2. High. Baseline-strength confound and the authors' own caveat are missing
- Location: Verdict ("The strongest confound is non-speech information"); M06 evidence paragraph.
- Evidence: §6.1 and Table 3 show that the comparators score near or below chance on vowels (Log+LDA subject means 29.3–40.3%, DaSalla 31.0–41.7%, chance 33%). The authors write "the accuracy is even below the chance level" and attribute DaSalla's failure to a different instruction set ("imagine vocalizing and mouthing", §6.1). The p = 6×10⁻⁵ vowel gain is therefore a gain over at-chance re-implementations, not over working decoders. This is the strongest confound for the M06 claim (baseline strength), and the review neither states it nor credits the authors' own explanation.
- Fix: Add one sentence to the M06 section and to the Verdict, for example: "The comparators reach chance or less on vowels (Table 3a; the authors attribute DaSalla's result to a different instruction set, §6.1), so the Table 4 gains measure distance from failed baselines, not from a working decoder."

### H3. High. Tates's leakage attribution adopted without checking the target's own text
- Location: Verdict sentence 4; M12 State of the art ("the authors state that the original cross-validation inflated accuracy"; "which leaves that statement open"); Questions ("Were the three epochs of a trial kept in one fold ...").
- Evidence: Target §5.2 partitions by trials ("90% (270 trials) ... 10% (30 trials) for testing"). §6.1 says the baseline uses "the same procedure to extract the time epoch ... as in our proposed approach" and that "the label of the tested trial is assigned by voting". So the test unit is the trial, and its epochs are voted together. Tates's "Stratified CV" splits 1.4 s segments at a 0.1 s stride (Tates §II-D), which is Tates's own reconstruction, not the target's protocol. Tates's grouped-CV short-versus-long median (about 0.75, Fig. 2) matches the target's 73.3% (method 1, Table 2), so the target's numbers do not show the 0.89-level inflation. Tates also says the Nguyen post-imagery check "appropriately collapsed to chance levels ... confirming that its high accuracies are driven by task-related SI" and that Group CV "still remained above chance" (§IV).
- Fix: State that the target reports trial-level test splits with epoch voting (§5.2, §6.1). Attribute the inflation claim to Tates as their reading of a protocol they reconstructed. Note that the target's short-versus-long accuracy equals Tates's grouped-CV value. Keep the confound that is supported: the cue and muscle explanations for the best contrast (Tates §IV). Replace the first Question with one the text does not answer: "Were overlapping epochs of one training trial used as separate training samples, and were CSP filters fit inside each training fold?"

### H4. High. M06 state of the art is neither the best later result nor protocol-checked
- Location: M06 State of the art; 13-components table M06 `sota`; `slots.json` M06 `sota`; audit `state_of_the_art`.
- Evidence: (a) Panachakel & Ganesan, "Decoding Imagined Speech From EEG Using Transfer Learning", IEEE Access 9, 2021 (wiki `doi-10.1109-access.2021.3116196`, [later]), use the same ASU dataset. Their abstract reports a minimum of 79.7% for vowels and up to 95.5% for short-versus-long words across subjects. Their mean κ is 0.78 ± 0.06 for vowels and 0.75 ± 0.05 for short words, about 85% and 83% three-class accuracy (inference). They test on whole held-out trials, with sliding-window augmentation in training only. Both values exceed Singh's 58.6% and 60.35%. (b) Singh & Gumaste build a [900, 60, 256] array per subject (3 epochs per trial) and use "stratified 10-fold validation" with shuffling (§4.1.1), which is exactly the segment-level leakage Tates shows inflates accuracy on this dataset (0.89 vs 0.74). The review gives only the copied column and the different subject sets as caveats. (c) Singh's own same-subset baselines are 49.2% (vowels) and 49.3% (short words), not 49.0% and 50.1%.
- Fix: Name Panachakel & Ganesan 2021 as the highest later same-dataset value (vowels κ 0.78, about 85%, inference), with its protocol. Either drop Singh or keep it as the closest same-family tangent-space decoder, adding "epochs split independently (stratified 10-fold over 900 epochs per subject), the design Tates [2] shows inflates accuracy". If Singh is kept, compute the gap against Singh's own subset baselines (49.2 → 58.6, 49.3 → 60.35; inference). Update `slots.json` and the audit `state_of_the_art`.

### M1. Medium. "matched = 5, n = 5" counts a negation, not a design
- Location: M06 Usual approach; table row M06 "Non-Riemannian features (CSP or statistics) + SVM/LDA/ELM, of 5 prior (pattern match 5)"; `slots.json` M06 `field`/`matched`; Appendix "Usual design: ... with SVM, LDA or ELM, 5 of 5 prior".
- Evidence: Of the 5 priors, Yoshimura et al. 2016 uses fMRI-informed cortical-current estimates with sparse logistic regression (wiki `pmc-4853397-covertvowel`). `arxiv-1705.07771` uses CSP-filtered DaSalla data with a CRNN. Only Deng 2010 (LDA), the s41133 2016 paper (SVM) and Min 2016 (SVM/ELM) fit "SVM, LDA or ELM", so 3 of 5. "3 name CSP" are mentions. Only arxiv-1705.07771 applies CSP itself, and Min names it only in related work. The table usually gives the most common positive design and its count; here 5 counts "not Riemannian", which is the absence claim restated.
- Fix: Write the usual approach as a positive design with its real count, for example "hand-crafted statistical, spectral or source features with a shallow classifier (LDA, SVM, ELM or sparse logistic regression), 4 of 5; one CSP + CRNN (pattern match)". Report "Riemannian or tangent-space features 0 of 5" separately as the absence count. Set `matched` to 4 (or 3) with that definition.

### M2. Medium. Target-time population misses a wiki prior; deciding prior DaSalla not named
- Location: Appendix M06 and M12 ("5 prior unique studies"); Verdict "None of the 5 prior".
- Evidence: Torres-García, Reyes-García & Villaseñor-Pineda, "Toward a silent speech interface based on unspoken speech", BIOSIGNALS 2012, pp. 370–373 (wiki `doi-10.5220-0003769603700373`; its manifest has no year, which probably hid it from the date filter). It covers scalp EEG, 21 subjects, imagined pronunciation of 5 words, DWT features and NB/RF/SVM/Bagging-RF, with chance stated at 20%. Suppes et al. 1997 PNAS (wiki `pmc-25146-brainwave`) has an "internal speech condition" with EEG and MEG. It is borderline under the rule and should be either included or excluded with a stated reason. DaSalla et al. 2009, the CSP comparator in Table 4, is not in the wiki and is cited in the review text without a reference entry. Other pre-2017 decoders I know of (Brigham & Kumar 2010, Wang et al. 2013, Zhao & Rudzicz 2015, González-Castañeda et al. 2017) are not wiki papers. None of them uses Riemannian or tangent-space features as far as I know (unverified). The absence claim therefore stands, but n changes. Known-item recall 0.25 (M06) and 0.0 (M12) measure the ledger pattern, not the hand-triaged target-time search, and the Appendix does not say which.
- Fix: Add Torres-García 2012, giving 6 prior (7 if Suppes 1997 is included under the rule). Recompute the M06 design counts and the M12 chance count (Torres-García states chance, so M12 becomes 5 of 6). In the Appendix, say that recall refers to the ledger-pattern population. Add DaSalla 2009 as a reference when it is named as a Table 4 comparator.

### M3. Medium. Uncorrected multiple comparisons in Table 4 not reported
- Location: M06 evidence paragraph; Verdict "two of 12".
- Evidence: Table 4 runs 21 paired t-tests at the 5% level with no correction (caption: "at the 5% significance level"). With Bonferroni over the 12 Tangent+RVM tests (α ≈ 0.0042), only 5 survive (inference): the three vowel tests, short words vs DaSalla (p = 0.001), and short-versus-long method 2 vs Min (p = 0.002).
- Fix: Add "uncorrected; 5 of 12 survive a Bonferroni correction (inference)". This gives the M06 verdict a reason inside the setting (H1).

### M4. Medium. "RVM trails ELM on short-versus-long" overstates a non-significant difference
- Location: Verdict sentence 2; M06 paragraph.
- Evidence: §6.1 reports 73.3 vs 76.3, t(5) = 1.39, p = 0.16, and calls it "quite equivalent". Method 2 with RVM reaches 80.1% (Table 2). The review treats p = 0.055 and p = 0.091 as "no gain" elsewhere, so it cannot read p = 0.16 as a loss.
- Fix: "RVM does not beat ELM on short-versus-long with method 1 (73.3% vs 76.3%, p = 0.16, §6.1)".

### M5. Medium. Complexity bullet does not say why the claim fails, and its arithmetic does not show it
- Location: "Where the claims outrun the evidence", Complexity bullet.
- Evidence: κ = (P − C)/(1 − C) is the authors' correction for class count (§5.2). Equal raw margins (16.2 vs 16.8 points) do not refute a κ comparison. The real gaps are elsewhere. Long and short words share only S3 and S6 (Table 2). The rhythm period differs (T = 1.4 s vs 1.0 s, §4.1), so analysed windows differ (4.5 s vs 4 s, §5.2). Trial counts differ (200 vs 300), and so do class counts (2 vs 3). The two κ values (0.32 ± 0.10 vs 0.25 ± 0.05) are not tested.
- Fix: Replace the margin arithmetic with: "the κ difference is untested and confounded by subject set (2 of 6 shared), window length and class count (Table 2, §4.1, §5.2)".

### M6. Medium. Visual cue presented as the reviewer's finding without the authors' reason
- Location: Verdict sentence 4; slots M04 note.
- Evidence: §4.1 says: "the analyzed signals correspond to a segment of the experiment where only a visual cue is present ... The aim is to avoid any possible evoked brain activity related to the sound." The authors state the design and its reason. The confound is the reviewer's (and Tates's) interpretation.
- Fix: "The authors analyse the interval in which the visual cue is shown, to exclude auditory responses (§4.1). That leaves a class-specific visual stimulus in the window, which Tates [2] link to posterior alpha differences."

### M7. Medium. M03 `not_reported` with a filled cell; the paper does indicate how tuning was done
- Location: table row M03; `slots.json` M03.
- Evidence: The skill checklist says "no `not_reported` with a filled cell", yet the cell reads "Per-subject CSP count and kernels; selection data not stated". §5.2 shows the choices were driven by observed results: CSP count "chosen empirically"; kernels with "small adjustments for each subject and each case"; "we found that incorporating frequency information did not provide any improvement"; "the highest accuracy in this case is obtained by using the multi-class CSP algorithm with 12–14 CSP components". §6.1 reports comparators as "the best mean values among the mentioned parameter set". In plain terms, settings were picked from accuracy on the evaluation folds, with no held-out selection set. One prior in the population (Yoshimura 2016) used nested hyper-parameter selection with a held-out group. That is 1 of 5, too few for `behind`.
- Fix: Set the M03 cell to "Per-subject CSP count, kernels and feature set chosen from observed CV accuracy (§5.2); no held-out selection set". Make the verdict `standard`, with Yoshimura 2016 named as the one prior with nested selection. Alternatively keep `not_reported` and empty the cell to "not stated". Keep the Question, reworded: "Were CSP count and kernel settings chosen on folds separate from those used for the reported accuracy?"

### M8. Medium. M12 usual-approach cell claims more than its count
- Location: table row M12; M12 Usual approach line ("The paper matches this").
- Evidence: The count of 4 is "chance-level term" mentions (audit `at_target_time_<slug>`). "Within-subject CV" and "untested" are not tallied, and one of the 4 (Yoshimura 2016) ran non-parametric permutation tests.
- Fix: "chance level stated, 4 of 5 (pattern match); permutation null 1 of 5". Drop "untested" from the count cell or tally it.

### M9. Medium. "the field's top ledger value, 96.4%" is wrong
- Location: M12, paragraph after State of the art.
- Evidence: The audit `sota_candidates` lists seven higher values (100%, 99.67%, 99%, 98.81%, 98.1%, 97%, 97%); 96.4% is eighth.
- Fix: "a high ledger value, 96.4% for four classes, comes from one-class runs [5]", or drop "top".

### L1. Low. Tates numbers need their condition and their positive reading
- Location: M12 State of the art.
- Evidence: 0.89, 0.74 and 0.55 are pooled medians over pairwise two-class contrasts (Tates §II-A, Fig. 1). Tates find vowels, short words and long words "clustered near chance" under grouped CV (Fig. 2). They read the 0.55 post-imagery result as confirming task-related decoding (§IV).
- Fix: Add "pairwise, pooled". Report that only short-versus-long stays clearly above chance under grouped CV (Tates Fig. 2). That point bears on the paper's three-class claims more directly than the 0.89 → 0.74 drop does.

### L2. Low. 0.609 single-feature result attached to the wrong confound
- Location: Claims bullet "In versus cooperate differs in length".
- Evidence: Tates attribute Participant 10's separation to the visual cue (posterior alpha) and Participant 14's to muscle tension tied to word length (§IV).
- Fix: "... one channel and one band reach 0.609 for Participant 10, whose discriminative components are posterior and alpha-band, consistent with the visual cue [2]".

### L3. Low. "20 random 90%/10% splits" generalised to all comparators
- Location: Claims bullet "Selection".
- Evidence: §6.1 states 20 cross-validations for DaSalla ("perform 20 cross validations") and Min ("using totally 20 cross validations"). For Log+LDA it states only "best mean values".
- Fix: "two of the three comparators are scored with 20 random 90%/10% splits".

### L4. Low. Abstract maxima are fold maxima
- Location: Claims bullet on 70% and 95%.
- Evidence: Table 3 min÷max ranges are per subject across folds (S6 short words up to 70%; method 2 up to 95.0% for S10/S14 and 96.9% for S9).
- Fix: "single-fold maxima within one subject (Table 3)".

### L5. Low. First-public date and concurrent boundary
- Location: header line; Appendix "first public before 2017-06"; audit `target_first_public` 2017-12.
- Evidence: The target was "Accepted for publication 26 July 2017". If the accepted manuscript was posted then (unverified for this article), first public is 2017-07. That would make arxiv-1705.07771 (May 2017) [concurrent] and shrink both populations by one. The authors' own Riemannian Neurocomputing paper ([28] in the target, doi 10.1016/j.neucom.2017.10.013) is [concurrent] and correctly not counted.
- Fix: Record the date basis in `component_review` and keep the population consistent with it.

### L6. Low. Restatement in the body
- Location: Verdict sentence 1 (method walkthrough); M06 paragraph listing the Table 4 p-values and the §6.1 RVM/ELM means.
- Evidence: Most of the M06 evidence paragraph repeats Table 4 and §6.1 values a reader gets from the paper.
- Fix: Keep only the numbers that carry the comparison (the two non-significant cells, the Bonferroni count, the at-chance baselines). Shorten sentence 1 to the changed component.

### L7. Low. Unsupported position on the dataset
- Location: Verdict last sentence ("The released dataset is the durable contribution").
- Evidence: No citation or location backs it.
- Fix: Cite the abstract (dataset published) and its later reuse ([2], [4], Panachakel & Ganesan 2021).

### L8. Low. Robustness claim: credit the authors' meaning
- Location: Claims bullet "Accuracy and robustness".
- Evidence: The authors equate robustness with RVM's lower spread than ELM ("more stable", §6.1) and with Bayesian outlier tolerance (§6.2, §7).
- Fix: "Robustness rests on lower fold-to-fold spread than ELM (§6.1); no perturbation, session or noise test is reported."

### L9. Low (optional addition). EMG filtering claim
- Location: none (missing).
- Evidence: §4.2 says the 8–70 Hz band-pass removes "possible artifacts related to EMG activity", yet that band keeps the EMG range. §5.1 notes 60–70 Hz activity over Broca's-area channels that persists at rest. Tates attribute Participant 14's separation to muscle tension.
- Fix: One clause in the M04/confound bullet: "the 8–70 Hz band the authors say removes EMG (§4.2) retains it".

## Scores

- Procedure: 6/10. The audits are reused and tallied, priors and the state of the art were read, and chronology labels are right. But the target-time population misses a wiki prior, the usual-approach count is a negation, and the M06 state of the art was not checked against later same-dataset results or the protocol of the chosen work.
- Final text: 5/10. Numbers mostly match their quotes. The M06 verdict reason comes from the wrong setting, the main baseline-strength confound and the authors' own caveat are missing, and the leakage attribution conflicts with the target's §5.2 and §6.1.

Counts by severity: High 4, Medium 9, Low 9.
