# Evaluator: a language model separate from the writer

Target: Pasley et al., "Reconstructing Speech from Human Auditory Cortex", PLoS Biology 10(1): e1001251, published 2012-01-31. Evaluated on 2026-11-26.

Inputs read: `compact.md` (review plus claim table), `reconstructing-speech-from-human-auditory-cortex.md`, `.slots.json`, `.verdict.json`, both audits in `reconstructing-speech-from-human-auditory-cortex.audit/`, `read-target/text.txt`, `read-priors/chang2010.txt`, `read-priors/guenther2009.txt`, `read-sota/akbari2019.txt`, and the wiki records for Berezutskaya 2023 (`pmc-10510111-berezutskaya`) and Défossez et al. (`arxiv-2208.12266-natmi`). No review or wiki file was modified.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Mean r = 0.28 pools tasks and word/sentence sets | Target, Results ("averaged over all participants and stimulus sets (including different word sets and continuous sentences...)"); Methods, tasks N = 5 each | correct | Figure 3 groups participants by grid density and stimulus set, though not by task. See L2. |
| 2 | Word identification uses one participant, 47 words and pseudowords from one speaker | Target, Results, and the Figure 8 caption ("a single speaker in a high density 4 mm grid experiment") | correct | |
| 3 | Median rank 0.89 averaged, 0.76 single trial, chance 0.5 | Target, Results | correct | 0.76 × 46 ≈ 35 is marked as inference, which is right. |
| 4 | Smoothing of 500 ms × 2 octaves is the best setting, with no stated selection data | Figure 8 caption ("Best performance was achieved after smoothing...") | correct, needs one qualifier | Methods describe an 80/10/10 train/validation/test split for model fitting. The gap applies to the smoothing width only. See L3. |
| 5 | Grid density is confounded with amplifier and sampling rate (inference) | Methods: 4 mm N = 4 [46]; 3,052 Hz N = 4 [46] | correct and marked as inference, but incomplete | Ref [46] is Chang et al. 2010, which recorded four awake-craniotomy patients with a 64-channel 4-mm array. See M1. |
| 6 | No listener test | Target, Discussion ("not clearly intelligible to a human listener"); Figure S7 ("Single trial reconstructions are generally not intelligible") | correct | The review credits the authors' concession. |
| 7 | F(1,14) = 33.36; interaction F(5,70) = 3.33; Figure S3 gain at ≥16 Hz for all scales; linear r ≈ 0.10 at fast rates | Target, Results; Figure S3 caption | correct | |
| 8 | 3 resamples for the modulation model against 10 for the spectrogram model; training 2.5–17.5 min | Methods, Cross-Validation; Model Fitting | correct | |
| 9 | No noise-ceiling correction because more than 5 repeats were generally unavailable | Methods, Reconstruction Accuracy | correct | |
| 10 | Phase retrieval "the authors say is imperfect" | Figure S7 caption | insufficient quote | The source says the step "introduces additional acoustic artifacts that can distort". See L4. |
| 11 | Authors credit spectrogram reconstruction to non-human work (refs 14, 15) | Target, Discussion ("mammalian primary auditory cortex [14] or the avian midbrain [15]"); Introduction [12–15] | correct | |
| 12 | Chang 2010: single-trial pSTG classification in four listening patients | chang2010.txt, Results and Methods | correct | |
| 13 | Guenther 2009: Kalman-filter prediction of two formants during attempted speech | guenther2009.txt, Methods | correct | |
| 14 | Akbari 2019: 75% listener digit accuracy, 67% above linear-to-auditory-spectrogram, five patients, held-out digits and speakers | akbari2019.txt, Results; Methods | correct but needs a qualifier | The Abstract says 65%. The gain is relative, and DNN versus linear pooled is 68.5% vs 47.5%. See M5. |
| 15 | Berezutskaya 2023: 92–100% word identification, 12 words, chance 8%, five subjects | wiki pmc-10510111-berezutskaya ledger | correct | This is produced speech, not heard speech. See M4. |
| 16 | "No study in the 64-study heard-speech reconstruction population predates it" | M06 audit, prior_time_tally and inclusion_rule | wrong label | The 64 matches are not all heard-speech reconstruction studies. See H3. |
| 17 | M06 usual approach "Spectrogram target ... 24 of 64, all years" | M06 audit, pattern_counts; slots.json M06 | wrong basis | This is an all-years count presented as the usual approach. See H1. |
| 18 | M12 "Correlation is the default across years (122 of 173)"; "no evaluation to follow" in 2012 | M12 audit; target refs [12–16], [48–50] | wrong basis | See H2. |
| 19 | "Modulation target recurs in 6 keys, 4 distinct studies, the others [later]" | M06 audit, usual_approach note | correct | One of the four is the target itself. See M3. |
| 20 | "Comparison repeats across 15 participants (F(1,14) = 33.36)" | Target, Results | overstated | F(1,14) is a group main effect, and no per-participant consistency is reported. See M2. |

## Required fixes, ordered by impact

### High

**H1. The M06 usual approach uses an all-years count.**
- Location: M06 "Usual approach" ("Across all years the spectrogram target is the usual design (24 of 64, pattern match)"), the M06 row of the components table ("Spectrogram target, base 64, all years; ... (pattern match 24)"), and `slots.json` M06 (`n: 64`, `matched: 24`, `matched_tier: "pattern match (unique studies, all years)"`).
- Evidence: The audit `prior_time_tally` (cutoff 2012-01) gives a prior base of 2 and 0 for every design. The 24 sampled pids are all 2024–2026 works (arxiv-2604.05751, arxiv-2609.36736, doi-10.64898-2026...). Adoption after 2012 cannot be the usual approach at the target's time. 24 of 64 is also 37.5% of a mixed population, which is not a majority.
- Fix: Set the usual-approach cell to "None before 2012-01 (ledger: 2 earlier hits, 0 reconstructions; pattern match)". In `slots.json`, set `n: 2, matched: 0` (or `matched: null`) with the tier "pattern match, first public before 2012-01". Move "24 of 64" to a sentence on later adoption, for example "later adopted: spectrogram target in 24 of 64 ledger matches, all years".

**H2. The M12 standard verdict rests on an all-years count, and "no evaluation to follow" is wrong.**
- Location: M12 "Usual approach" ("so no evaluation to follow"; "Correlation is the default across years (122 of 173)"), the M12 table row ("Correlation, base 173, all years"), and `slots.json` M12 (`n: 173, matched: 122`).
- Evidence:
  - At 2012-01 the ledger prior base is 2 hits with 0 reconstruction evaluations (M12 audit, prior_time_tally). The 122/173 figure therefore describes the field after the target.
  - The target itself places its evaluation in an existing practice. It names stimulus reconstruction [12–15] (Bialek 1991; Stanley 1999; Mesgarani 2009; Ramirez 2011), all scored by reconstruction-to-stimulus similarity. It also cites human fMRI identification/decoding work [48–50] (Mitchell 2008; Kay 2008; Naselaris 2009), and its fitting follows [16,36,49] (Model Fitting).
  - "Standard" is defensible only against these priors, not against a count from later years.
- Fix:
  - Rewrite the usual approach as "No speech-reconstruction evaluation in the ledger before 2012-01; the authors take correlation scoring from non-human stimulus reconstruction [12–15] and candidate identification from human fMRI decoding (Kay et al. 2008, their ref 49)".
  - State the verdict basis as those cited priors.
  - Set `slots.json` M12 to `n: 2, matched: 0` (or `null`).
  - Keep 122/173 only as later adoption.

**H3. The pattern-match populations are mislabelled as reconstruction studies.**
- Location: Verdict ("the 64-study heard-speech reconstruction population"), M06 usual approach ("among 64 heard-speech reconstruction studies are behavioural"), and M12 usual approach ("the 173-study reconstruction population").
- Evidence:
  - The M06 inclusion rule itself says "production-only synthesis studies and encoding-only studies admitted by the pattern are counted but are not heard-speech reconstruction".
  - The candidate list includes non-neural work: isca-berthommier01-srs (audio-visual recognition of spectrally reduced speech), isca-gaudrain09 (speaker-identity perception), doi-10.1016-j.rlfa.2018.07.004 (laryngectomy silent speech), doi-10.1109-taslp.2017.2716178 (visual-to-audio), and fMRI tracking.
  - The M06 sentence contradicts itself: the two "heard-speech reconstruction studies" are "behavioural".
  - The M12 rule admits envelope-tracking attention decoding, which it says "is not a reconstruction study".
- Fix: Call these "64 (173) ledger pattern matches, not all reconstruction studies" everywhere. For M06 write "the 2 pattern matches first public before 2012-01 are behavioural perception studies; neural reconstructions 0".

**H4. The absence claim behind M06 "ahead" is under-tested and partly attributed to the wrong source.**
- Location: Verdict ("For 2012 this is ahead: no study ... predates it"), M06 usual approach ("in 2012 there was none for this task"), and Appendix (recall check).
- Evidence:
  - The full-text recall pattern targets only modulation-energy reconstruction (`fulltext_pattern`: "reconstruct ... modulation (energy|representation|spectrum|model)"). No full-text check was run for pre-2012 human heard-speech spectrogram or envelope reconstruction.
  - The three known-item seeds are the target and later works, so they cannot test recall of earlier work.
  - The two read "deciding priors" are adjacent designs, not reconstructions:
    - Chang 2010 is classification.
    - Guenther 2009 decodes formants during attempted production. This is itself an acoustic-representation decoder from human cortex driving synthesis, so "none for this task" holds only if the task is restricted to heard speech.
  - Outside the ledger, a plausible earlier human heard-speech reconstruction exists: MEG envelope reconstruction with a linear decoder by Ding and Simon, J Neurophysiol 107: 78–89 (January 2012 issue). Its online-first date is likely in 2011 (unverified; check whether it was public before 2012-01-31). If confirmed, "none for this task" fails for the envelope target, though not for spectrogram or modulation targets from intracranial recordings.
  - The authors do not claim priority anywhere in the text. Their stated contribution is applying stimulus reconstruction [12–15] to human non-primary STG and finding that a modulation-energy representation reconstructs fast rates better (Discussion, "In this study, we examined human STG..."). The "no study predates it" sentence is the reviewer's ledger finding, but it is written as if it were a field fact.
- Fix:
  - Narrow the claim to "earliest spectrogram and modulation-energy reconstruction of heard speech from human intracranial recordings among the ledger matches; the authors claim the human-STG and modulation-representation result, not priority".
  - Add a full-text recall pattern for pre-2012 heard-speech spectrogram and envelope reconstruction (ECoG/MEG/EEG), and report its hits.
  - Check Ding and Simon 2012 (online date), and name it, either as a prior for the envelope target or as excluded with a reason.
  - Say explicitly that Guenther 2009 is an acoustic-target decoding prior for production.

### Medium

**M1. The target and deciding prior [2] share a cohort, and the density confound is wider than stated.**
- Location: Verdict (prior [2]), M06 usual approach, "Electrode density" bullet, and the third author question.
- Evidence: The target's 4-mm group (N = 4) and its 3,052 Hz group (N = 4) both cite [46], which is Chang et al. 2010. Chang 2010 recorded exactly four patients during awake craniotomy, intraoperatively, with a customised 64-channel array at 4-mm spacing (chang2010.txt, Methods, "Subjects and intraoperative testing").
- Consequences:
  - Prior [2] is not independent of the target. The 4-mm participants very likely are Chang 2010's patients (inference).
  - Density also travels with the intraoperative awake-craniotomy setting and its shorter recordings, not only with the amplifier and sampling rate.
  - The question "Are the 4-mm grid participants the four recorded at 3,052 Hz?" is mostly answered by the shared citation.
- Fix:
  - Add to the density bullet: "both groups cite Chang et al. 2010 [2], four intraoperative patients with a 64-channel 4-mm array, so density also travels with intraoperative recording (inference)".
  - Note in M06 that [2] and the target likely share participants.
  - Reword the question as a confirmation request.

**M2. The "ahead" verdict lumps two targets and overstates repetition.**
- Location: Verdict ("the linear-versus-modulation comparison repeats across 15 participants (F(1,14) = 33.36)"), the M06 closing paragraph, and the verdict.json `short`.
- Evidence:
  - F(1,14) = 33.36 is a group main effect in one study. The paper reports no per-participant win count, and the 15 participants come from three labs, tasks and stimulus sets that are pooled.
  - The modulation target's later recurrence is within one lineage: Martin et al. 2014 and Martin's 2017 thesis share the Knight/Crone group, and Yang et al. 2015 uses modulation space only for evaluation (audit note).
  - The linear spectrogram target was later adopted (24 matches). The modulation target was not (4 studies including the target).
- Fix:
  - Split the verdict: the human spectrogram reconstruction is ahead and was later adopted; the modulation target is a novel representation result shown within one study and reused by the same lineage.
  - Replace "repeats across 15 participants" with "group main effect over 15 participants (F(1,14) = 33.36); per-participant consistency not reported".

**M3. Counts are labelled "unique studies" but are key counts that include the target.**
- Location: Appendix (M06 "temporal modulation 6 keys (4 distinct studies)"; M12 "identification among candidates 20"), and `slots.json` tiers ("unique studies").
- Evidence:
  - The temporal_modulation pid sample contains pmc-3269422-pasley (the target) and two versions of Martin 2014 (doi-10.3389-fneng.2014.00014 and pmc-4034498-spectemp).
  - The identification sample contains arxiv-2602-22597-vmi and arxiv-2602.22597-vmi, two versions of one study.
  - The other design counts (24, 13, 12, 122, 45, 31, 23, 20) may therefore be overcounts. The rule states "versions count once".
- Fix: Deduplicate versions and exclude the target from field counts, or relabel the counts as "ledger keys" with the deduplicated number beside each.

**M4. The M12 state of the art misses a larger heard-speech identification test that is already in the wiki.**
- Location: M12 "State of the art" and the M12 table row.
- Evidence:
  - Berezutskaya 2023 uses produced speech with a 12-word leave-one-out set.
  - The wiki holds Défossez et al. (arxiv-2208.12266-natmi; Nature Machine Intelligence, 2023). It identifies heard 3-s speech segments zero-shot among more than 1,000 candidates. Its ledger reports top-10 segment accuracy of 70.7% on the Gwilliams MEG set and 67.5% on Schoffelen. Splits keep identical sentences apart.
  - This is the closest later counterpart of the target's identification-among-candidates design for heard speech. It is contrastive, not acoustic reconstruction.
- Fix: Name it as the heard-speech identification state of the art (2023, top-10 70.7% over more than 1,000 segments, MEG), or state why it is excluded (no acoustic reconstruction). Keep Berezutskaya for produced-speech reconstruction.

**M5. The Akbari comparison needs the relative wording and the source inconsistency.**
- Location: Verdict ("beat it by 67% in listener digit accuracy"), M06 state of the art, and verdict.json `position` ("67% better by listeners").
- Evidence:
  - Akbari's Results say "75% accuracy, which is 67% higher than the baseline". The Abstract says "improving the intelligibility by 65%".
  - The gain is relative. 75 / 1.67 implies a baseline near 45% (inference), and the pooled DNN versus linear figures are 68.5% vs 47.5%.
  - "Made its linear spectrogram design the baseline" is inference. Akbari cites Pasley (ref list) but describes the baseline only as "Linear regression with auditory spectrogram", fit on their own story data with high-gamma and low-frequency features.
- Fix: Write "75% listener digit accuracy, 67% relative to a linear auditory-spectrogram baseline of the target's type (Results; the Abstract gives 65%; baseline about 45%, inference)".

### Low

**L1. Whole-ledger totals in the Appendix.**
- Location: Appendix ("slot-filled 7,345"; "slot-filled 6,960").
- Evidence: These are whole-ledger totals, not design counts with a denominator.
- Fix: Delete them, or replace them with the population denominator actually used (64 / 173 pattern matches, all years; 2 before 2012-01).

**L2. Pooling bullet.**
- Location: "Pooling" bullet.
- Evidence: Figure 3 groups participants by grid density and stimulus set (isolated words or sentences), so per-set values are visible per participant. Only a per-task mean is missing.
- Fix: Write "no per-task mean; Figure 3 groups by density and stimulus set only".

**L3. Smoothing selection.**
- Location: Verdict and the word-readout bullet.
- Evidence: Methods state an 80/10/10 train/validation/test split, and early stopping is monitored on validation data (Model Fitting; Cross-Validation). What is unstated is the selection data for the smoothing width.
- Fix: Write "smoothing width chosen as best-performing (Figure 8), with no stated selection set; the validation split is described only for model fitting".

**L4. Phase-retrieval wording.**
- Location: M06 weak points ("which the authors say is imperfect").
- Evidence: The authors' wording is "introduces additional acoustic artifacts that can distort" (Figure S7).
- Fix: Use the authors' wording or a close paraphrase without quotation-like attribution.

**L5. Method restatement in the body.**
- Location:
  - Verdict, first sentence ("it reconstructs heard speech from human superior temporal gyrus as a linear auditory spectrogram and as nonlinear temporal-modulation energy").
  - M06 ("the paper adds a 60-channel rate-scale modulation target").
  - M06 closing paragraph ("both targets share partitions").
- Evidence: These describe the paper's method rather than take a position against the field. The format bars summary.
- Fix: Cut to the position, for example "The paper [1] is the earliest human spectrogram and modulation-energy reconstruction in the ledger (M06)". Keep "identical partitions" only as evidence for the representation claim.

**L6. A question for the authors has a stated answer.**
- Location: Question 2 ("Which scheme, random trial subsampling or leave-one-word-out, produced each headline number?").
- Evidence: The question is valid: Results say leave-one-out, and Methods describe repeated random subsampling. But Methods also state that 20/10/3 resamples were used for encoding, spectrogram and modulation models.
- Fix: Keep the question, but cite both locations (Results, reconstruction procedure; Methods, Cross-Validation) so the inconsistency is the authors' own.

## Scores

- Procedure: 5/10. Target-paper claims are accurately quoted. The time-of-target rule is broken for both audited slots. Populations are mislabelled. The novelty recall check covers only one of the two representations.
- Final text: 6/10. The target critique (single participant, rank versus accuracy, pooling, inferred density confound, no listener test) is accurate. The M06 "ahead" and M12 "standard" bases need rewriting as above.

What holds: every number about the target (0.28, 47, 0.89/0.76, F values, N per grid and sampling rate, resamples, noise ceiling) matches the paper, and inferences are marked.

Counts by severity: High 4, Medium 5, Low 6.
