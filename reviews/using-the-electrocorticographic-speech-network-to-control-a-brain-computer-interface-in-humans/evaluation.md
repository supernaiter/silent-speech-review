# Evaluator: a language model separate from the writer

Date: 2026-11-27. Inputs read: compact.md, the review draft (`<slug>.md`), slots.json, verdict.json, claims.md, notes.json, the three audit files. Source texts read: the target (PMC3701859 author manuscript, `papers/doi-10.1088-1741-2560-8-3-036004/source/text.txt`), Guenther 2009 (`pmc-2784218-wirelesssynth`), Kellis 2010 (`doi-10.1088-1741-2560-7-5-056007`), Card 2024 (`doi-10.1056-nejmoa2314132`), Singer-Clark 2025 (`pmc-12208300-cursor`), Duraivel 2023 (`doi-10.1038-s41467-023-42555-1`), Brumberg 2010 review (`pmc-2829990-bcispeech`). I also scanned the manifests of all 9,072 wiki folders for work before 2011-11 on BCIs, ECoG, intracortical recording, EEG or imagined speech.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target first public 2011-04 (online 7 April 2011) | Target PMC header "J Neural Eng. 2011 Apr 7;8(3):036004" | correct | The manifest gives the issue date 2011-06-01, but 2011-04 is right. Claim row 32 quotes Abstract text, which does not show a date (L7). |
| 2 | Windows: prior before 2010-10, concurrent 2010-10 to 2011-10; Kellis prior, Brumberg 2011 and Pei 2011 concurrent, [6], [7], [11] later | Kellis text "2010 Sep 1"; Brumberg 2011 manifest 2011-05-16; Pei 2011 manifest 2011-08 | correct | |
| 3 | M04 prior population is 1 (Guenther 2009 plus its Interspeech report) | Wiki-wide scan of folders before 2011 | correct (complete within the wiki) | Before 2010-10 the wiki has no other closed-loop study driven by speech tasks or speech cortex. The remaining hits are reviews (Brumberg 2010 *Speech Commun.*, `pmc-2829990`/`doi-10.1016-j.specom.2010.01.001`, which the audit's excluded list omits; Denby 2010; erd.10.34), offline EEG/MEG work (Suppes 1997/1999; Deng 2010, imagined syllable rhythm) and perception studies. Leuthardt 2004, Schalk 2008, Wilson 2006, DaSalla 2009 and Kennedy's early work are not in the wiki. `pmc-3321121-revspeech` and `pmc-3342676-gammaev` are labelled 2010 in the wiki but are 2012 papers, so they are out of window. |
| 4 | M05 prior population is 2; M12 prior population is 1 | Audit prior_tally; wiki scan | correct | Both are labelled as pattern-match tallies. |
| 5 | Guenther 2009: locked-in participant, attempted speech, formant synthesizer, feedback within 50 ms, 25 sessions, hit rate 45% to 70% | Guenther abstract and Results | correct | "first block to last block across sessions" supports "per-block hit rate". |
| 6 | Guenther 2009 is not cited by the target | grep of the target for Guenther/Brumberg/Kennedy: 0 hits | correct | |
| 7 | Earlier ECoG cursor tasks included single-word articulation [3], [4] | Target Sec. 4 | partly correct | The target attributes this to four works together (Schalk 2008a; Leuthardt 2004; Leuthardt 2005; Hinterberger 2008), not to [3] and [4] alone (L3). |
| 8 | The "first demonstration" claims do not hold against the field | Abstract; Sec. 1; Sec. 4 | wrong as phrased | The authors' "first" claims are narrower than the review says (H2). |
| 9 | Imagined arm is vowel vs rest, so it detects a task | Sec. 2.4 "imagined phoneme vs. rest (patients 3 & 4)" | correct | |
| 10 | "Two of four immediately >90%" is contradicted by Table 2 | Sec. 4; Table 2; Fig. 8 caption | insufficient evidence | Table 2 lists final accuracies. "Immediately" refers to early performance, which is in Fig. 8 (H1). |
| 11 | 68-91% (Abstract, Sec. 3) vs ">69%" vs Table 2's 69% | Abstract; Sec. 3; Fig. 8 caption; Table 2 | correct, location wrong | ">69%" is in the Fig. 8 caption, not the Sec. 3 text. The gap is 1 point (L2). |
| 12 | 560 Hz for Patient 4 vs a 0-550 Hz range | Table 2; Sec. 2.3; Sec. 2.2 | correct, incomplete | Patient 4 was sampled at 9600 Hz, so 560 Hz could be recorded. Sec. 3 says "as high as 550 Hz". Patients 1-3 were bandpassed at 0.1-500 Hz but screened to 550 Hz (L1). |
| 13 | Condition confounded with patient; overt-imagined difference from Patient 3 only | Sec. 2.4; Sec. 3; Fig. 7 (160 overt / 99 imagined trials) | correct | The authors disclose that only one patient was screened both ways. The overreach is the generalization in the Discussion, which the review does not quote (L4). |
| 14 | No EMG, microphone or video check of imagined trials | Text grep for EMG/microphone/audio/mouth/artifact: no monitoring described | correct | Patients were in a clinical 24-hour video monitoring unit (Sec. 2.1), but the paper does not report using it as a check. Say "none reported" (L11). |
| 15 | Patient 1's control was over auditory cortex (BA 42) | Table 2; Sec. 3 "Auditory Cortex (BA 42 and BA 22)" | correct | The authors themselves name auditory processing as one level at which the sites may work (Discussion). That should be credited (L5). |
| 16 | Microgrid: 16 microwires, 75 µm, 1 mm, dorsal premotor, Patient 2, 410-420 Hz, 76%, 139 trials | Sec. 2.2; Sec. 2.3; Table 2; Sec. 2.4 | correct | |
| 17 | "First microscale ECoG device control" stands | Sec. 4; M05 audit (micro-ECoG device control 0 of 2); wiki scan | correct (verified within the wiki; one patient) | From outside knowledge (unverified): the cited Leuthardt 2009a and Wang 2009 micro-ECoG studies are offline. I know of no earlier closed-loop micro-ECoG control in humans. |
| 18 | Kellis: 85.0% on two-word pairs over face motor cortex | Kellis Results "85.0 ± 13.1% ... over 45 two-word combinations" | correct | Add: offline, mean over 45 pairs. |
| 19 | Chance 46.2% (2.7% SD), 32 blocks of 425 white-noise trials | Sec. 2.4 | correct | |
| 20 | Time-outs count as failures | Sec. 2.4 "successes divided by the total number of trials"; time-out 8-15 s | correct | |
| 21 | Patient 4: 69% of 69 trials is about 3.8 SD above 46.2% (inference) | Arithmetic | arithmetic correct, labelling ambiguous | sqrt(0.462×0.538/69) = 0.060, and (0.69-0.462)/0.060 = 3.8 binomial standard errors. Against the paper's 2.7% SD the result would be 8.4. Whether "final accuracy" covers all 69 trials is an assumption (M1). |
| 22 | Card 2024: 99.6%, 50 words, day one, intracortical, one ALS participant | Card abstract | correct | |
| 23 | Singer-Clark 2025: 2.90 bits per second through right-hand imagery | Singer-Clark abstract; Results (mean of optimized blocks, peak 3.16) | correct value; off-slot | The control action is not a speech task (M4). |
| 24 | Duraivel 2023: up to 57% nine-way (chance 11.11%), four intraoperative patients, offline | Duraivel Results | correct | Offline, so it does not match the review's own "for device control" framing (L9). |
| 25 | Notes t31 (98/139/61/69 trials), t36 (32 blocks of 425, 46.2%, SD 2.7%), t38 (time-out 8-15 s; time-outs count against accuracy) | Sec. 2.4 | correct | t7 still says "theoretical chance", which contradicts t36. Claim row 7 cites t7 (L7). |

## Findings, ordered by impact

**H1. High. Verdict, sentence 4, and "Where the claims outrun the evidence", bullet 2.** The claim "two of four patients immediately >90%" is dismissed using Table 2.
- *Evidence:* Sec. 4 reads "two of our four patients immediately had greater that 90% accuracy without any prior training". "Immediately" refers to early performance. Table 2 lists only "Final Accuracy". Early performance is shown in the Fig. 8 learning curves, and accuracy was "assessed after each block" (Sec. 2.4). Final values of 91/76/73/69% cannot refute an early-block claim; accuracy may have fallen later. Neither the notes nor the claim table record a Fig. 8 value.
- *Fix:* Read the early blocks in Fig. 8. If two patients exceeded 90% early on, drop the point from the Verdict and from the bullet. If they did not, cite the Fig. 8 value. If Fig. 8 cannot be read, write: "Table 2 gives only final accuracies (91, 76, 73, 69%); the 'immediately >90%' claim rests on Fig. 8 and is not tabulated." Remove it from the Verdict's list of claims that "do not hold".

**H2. High. Verdict, sentence 4, and M04, paragraph 3.** The authors' "first" claims are paraphrased more broadly than they are written, so the refutation partly misses.
- *Evidence:* the three claims in full:
  - Abstract: "We demonstrate here for the first time that ECoG signals associated with different overt and imagined phoneme articulation can enable invasively monitored human patients to control a one-dimensional computer cursor rapidly and accurately."
  - Sec. 1: "We demonstrate for the first time that the electrocorticographic signals associated with speech can be effectively used to select from one of two choices with minimal training."
  - Sec. 4: "first demonstration that neural correlates of different actual and imagined phoneme articulations can be used for rapid and effective control of a cursor on a screen."

  Guenther 2009 [2] is intracortical and drives a formant synthesizer, not ECoG and not a screen cursor. The paper's own Sec. 4 contradicts the Sec. 1 claims: "concrete evidence ... has been absent" and "first time ... ECoG signals associated with speech ... select from one of two choices", because earlier ECoG BCIs used "articulation of single words". Guenther contradicts only the broad "speech network" wording. The scoped claim (different overt phonemes driving an ECoG cursor) holds for Patients 1-2. The "different ... imagined phoneme articulations" part is not supported by the study's own design, since the imagined arm was phoneme vs rest.
- *Fix:* Quote the three sentences in the Appendix or claim table. In the Verdict, replace "the 'first demonstration' of speech-network control ... do[es] not hold against the field" with three points: (a) the Sec. 1 claims that such evidence was absent and that speech-ECoG two-choice selection was a first are contradicted by the paper's own Sec. 4, and the broad wording also by [2]; (b) "different overt phonemes driving an ECoG cursor" holds (Patients 1-2); (c) "different imagined phonemes" was never tested (Sec. 2.4).

**M1. Medium. M12, paragraph 3.** The call for "a null from patient data after selection is the proper test" is misframed, and "3.8 standard deviations" is ambiguous.
- *Evidence:* Features were selected on separate screening data (Sec. 2.3), and online trials are new data (Sec. 2.4), so selection circularity does not inflate online accuracy. The real gaps are different. White Gaussian noise lacks ECoG's temporal (1/f, drift) structure. A constant cursor bias would score about 50% against randomized targets, which is above the 46.2% floor. The 3.8 figure is a binomial standard error at n = 69 under p = 0.462 (about 6.0 points), not the paper's 2.7% SD; against that SD it would be 8.4. The paper does not say whether "final accuracy" is cumulative over all 69 trials or the last block only (Sec. 2.4: "assessed after each block").
- *Fix:* Replace "a null from patient data after selection is the proper test" with: "a noise floor without ECoG temporal structure; a conservative test against 50% still leaves Patient 4 at about 3.2 binomial standard errors (0.19/0.060) if final accuracy covers all 69 trials (inference)." Write "3.8 binomial standard errors for 69 trials (inference)". Keep the "(inference)" labels.

**M2. Medium. M04 "Usual approach", Appendix M04, slots M04 field.** A population of one study cannot define a "usual approach", and same-group priors that the target cites go unexamined.
- *Evidence:* There is 1 of 1 pattern-match study. The comparable ECoG design came from the target's own citations: band power from a motor or word task vs rest driving a 1-D cursor, in Leuthardt 2004, Schalk 2008a and Leuthardt 2005/2006 "Seattle experience" (TNSRE 14:194). The M06 row itself says "Linear band-power cursor". The target also cites Schalk 2007a (SfN abstract, "Toward brain-computer interfacing using phonemes decoded from ECoG") and Leuthardt 2009b (Neurosurg Focus 27:E4), both same-group, neither checked. From outside knowledge (unverified): Leuthardt 2004 used saying the word "move" in both actual and imagined form. If so, "imagined vowel versus rest as an ECoG control task" is not new either.
- *Fix:* Write "The wiki holds one earlier closed-loop speech study [2], too few to define a usual approach; the comparable ECoG design in the target's citations is a task-vs-rest band-power 1-D cursor [3], [4]." Check Leuthardt 2004 for imagined word tasks, and name Leuthardt 2005/2006, Schalk 2007a and Leuthardt 2009b as unchecked same-group priors. Soften "Its addition is narrower: ... imagined vowel versus rest" to match what you find.

**M3. Medium. M05 "Usual approach" and the table row (field: "1-mm micro-ECoG offline (1 of 2)").** One of two studies is not a usual approach, and the clinical standard is left out.
- *Evidence:* The prior population is one penetrating closed-loop study and one micro-ECoG offline study (audit). The usual sensor for ECoG BCIs at the time was the 10-mm clinical grid. The target uses it in all four patients (Sec. 2.2), and so do the cited ECoG cursor priors (Sec. 4).
- *Fix:* Field: "10-mm clinical grid (target and cited ECoG priors); in the wiki, 1 penetrating and 1 micro-ECoG offline (2 studies, no majority)". Keep the pattern-match label.

**M4. Medium. M04 "State of the art", second clause; "What the field needs next", M12 bullet.** Singer-Clark 2025 [7] is outside the slot's step, and its units do not match the target's.
- *Evidence:* M04 is "speech task as the closed-loop control signal". In [7], cursor control uses "Right hand mouse" imagery, and the authors write "the cursor BCI could be controlled with non-speech, non-orofacial imagery". The comparison "2.90 bits per second" vs "at most 1 bit per selection" sets bits per second against bits per selection.
- *Fix:* Remove [7] from the M04 state-of-the-art line. If it stays at all, put it in one sentence labelled as a different action at the same site. To compare the target, give Wolpaw bits per trial: 0.56 at 91% and 0.11 at 69% for two targets (inference). Say that bits per second cannot be computed because trial durations are not reported (only the 8-15 s time-out).

**M5. Medium. M12 "State of the art" and the table row ("[6] (2024): day-1 word accuracy").** The line has no value, and it does not address the slot's design of interest, which is how the chance floor is built.
- *Evidence:* The M12 inclusion rule is "the online accuracy figure and how its chance floor is built". Card 2024 reports WER 0.44% (95% CI 0.0-1.4%) on 50 words on day one; the review's line states neither the value nor any null construction.
- *Fix:* State the value and condition ("99.6% word accuracy, 50 words, day one, 1 ALS participant, intracortical; reported with a 95% CI"). Either name a later online study that reports an explicit empirical or shuffle null, or write "no later study in the ledger reports a constructed null (pattern match)" if that is what the audit shows.

**M6. Medium. "Where the claims outrun the evidence" (missing item).** The review misses an internal inconsistency over Patient 1's condition.
- *Evidence:* The Fig. 9 caption says, "For Patient 1, A & C, demonstrate the variable cortical topographies of activation that are different between imagined 'oo' and 'ee'". Sec. 2.3 and Fig. 5 place Patient 1 in overt-only screening, Sec. 2.4 in overt control, and the Fig. 2 caption says "the patient spoke the phonemes".
- *Fix:* Add a bullet: "Fig. 9 calls Patient 1's contrast 'imagined', while Sec. 2.3, Sec. 2.4 and Fig. 2 say overt." Add a question for the authors.

**L1. Low. Bullet 3 and Questions, item 2 (560 Hz).** The 560 Hz point leaves out acquisition details that change the question.
- *Evidence:* Sec. 2.2: "The data for Patient 4 was digitally lowpass filtered at 4800 Hz and downsampled to 9600Hz", so 560 Hz could be recorded. Sec. 3 says frequencies "occurred as high as 550 Hz". Patients 1-3 were bandpassed at 0.1-500 Hz yet screened from 0 to 550 Hz.
- *Fix:* "Table 2's 560 Hz exceeds the 0-550 Hz screening range (Sec. 2.3) and Sec. 3's 'as high as 550 Hz', though Patient 4's 9600 Hz sampling could carry it; Patients 1-3 were screened to 550 Hz above their 500 Hz bandpass."

**L2. Low. Bullet 1.** The headline discrepancy is overstated, and ">69%" has the wrong location.
- *Evidence:* ">69%" is the Fig. 8 caption ("All patients finished with greater than 69% accuracy"). The gap between 68% and 69% is 1 point.
- *Fix:* Cite the Fig. 8 caption. Write "68% (Abstract, Sec. 3) vs 69% (Table 2); the Fig. 8 caption's '>69%' excludes Patient 4's own 69%."

**L3. Low. Verdict, sentence 2, and the M04 usual-approach line.** The "single words" attribution is narrower than the target's.
- *Evidence:* The Sec. 4 sentence cites Schalk 2008a, Leuthardt 2004, Leuthardt 2005 and Hinterberger 2008 together.
- *Fix:* Write "the paper itself says earlier ECoG BCIs (four works, including [3], [4]) included single-word articulation".

**L4. Low. Bullet 4.** The overreach about the overt-imagined difference sits in the Discussion, and the authors disclose the single-patient basis.
- *Evidence:* Sec. 3 discloses it: "in the patient who was screened for both". The Discussion generalizes: "The substantial difference between actual and imagined speech is in marked contrast to results ... that ... motor movements and motor imagery have similar neural signatures", citing Pei et al. 2010.
- *Fix:* Quote the Discussion sentence as the overreach and credit the Sec. 3 disclosure.

**L5. Low. Throughout.** Caveats the authors state themselves are not credited.
- *Evidence:* The Discussion says phonemes "likely do not access higher order lexical processing", that "signal characteristics in open-loop situations may not generalize to closed-loop situations", and that sites may reflect "auditory, phonological, semantic, motor" levels. The last bears on the BA 42 bullet.
- *Fix:* Add a clause to the BA 42 bullet: "the authors themselves allow an auditory level (Discussion)".

**L6. Low. Missing item.** The paper states an electrode constraint that its own control sites break.
- *Evidence:* Sec. 2.3 says selection was "constrained to ... motor cortex, Wernicke's, and Broca's area", yet Patient 1's control site is BA 42 and Patient 4's include BA 22 and BA 43 (Table 2). The Fig. 2 caption says "perisylvian".
- *Fix:* This is optional. Either add it to the BA 42 bullet or drop it.

**L7. Low. Claim table and notes.** Two claim-table rows rest on the wrong evidence.
- *Evidence:* Row 32 (date) quotes Abstract text that shows no date. Row 7 cites t7, whose condition says "theoretical chance", while t36 (correct) gives an empirical noise floor.
- *Fix:* Quote the PMC header "J Neural Eng. 2011 Apr 7;8(3):036004" in row 32. Change t7's condition to "empirical, white-noise input (Sec. 2.4)", or cite t36 in row 7.

**L8. Low. Body (M04, M05, M12 usual-approach lines; "the wiki holds", "Outside the wiki").** These lines restate the method and use process wording.
- *Evidence:* "The paper maps one or two screened vowels to cursor direction." "The target adds a 16-microwire 1-mm grid ... (Sec. 2.2)." "The target reports final accuracy against 46.2% ... (Sec. 2.4)." These restate the method inside usual-approach lines.
- *Fix:* Fold each into a contrast sentence (for example, "unlike [2]'s continuous formant decoder, the target uses push-pull vowel features"). Move the "wiki holds / outside the wiki" process wording to the Appendix and keep the counts in the body.

**L9. Low. M05 "State of the art".** The line does not match the review's own "for device control" framing.
- *Evidence:* Duraivel is offline. Microscale device control today is intracortical: Card 2024 reports 97.3% word accuracy on 125,000 words within 16 hours (Card Discussion).
- *Fix:* Add "offline" to the table cell, and add one clause naming intracortical arrays as the microscale device-control reference [6]. Add "one patient, offline, mean over 45 pairs" to the Kellis figure.

**L10. Low. Table row M09.** The row is internally inconsistent.
- *Evidence:* The choice is "Target hit", yet the verdict is "not applicable".
- *Fix:* Set it to standard (cursor dwell or hit, as in the priors), or set the choice to "None (selection by hit)".

**L11. Low. Bullet 5.** The wording does not allow for the unit's clinical video.
- *Evidence:* Patients were in a "24-hour video monitoring unit" (Sec. 2.1).
- *Fix:* "No EMG, microphone or video check of imagined trials is reported (Sec. 2.2-2.4)."

## Scores

Procedure: 7/10. Dating, windows and wiki populations are correct and complete, the comparator numbers check out, and the notes corrections (t31, t36, t38) are right. But Fig. 8 was not used, and same-group priors cited by the target were not followed up.

Final text: 6/10. The Verdict rests two of its positions on misreadings: "immediately >90%" judged from final accuracies, and the scoped "first" claims paraphrased too broadly. Two state-of-the-art lines are off their slot's step.

What holds: the dating, Guenther as the uncited prior, the arithmetic, the microscale "first" check, the vowel-vs-rest point, and the reading of the chance floor.

Counts: High 2, Medium 6, Low 11.
