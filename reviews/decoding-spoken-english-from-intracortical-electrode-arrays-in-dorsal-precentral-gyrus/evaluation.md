# Evaluation: decoding-spoken-english-from-intracortical-electrode-arrays-in-dorsal-precentral-gyrus

Evaluator: a language model separate from the writer

Date: 2026-11-27. Target: Wilson et al., J Neural Eng 17(6):066007 (2020), doi:10.1088/1741-2552/abbfef. Sources checked: wiki `pmc-8293867-dorsal/source/text.txt` (PMC author manuscript of the journal version), the reader copies of Mugler 2014, Roussel 2020, Peterson 2024, Livezey 2019 and Stavisky 2019, the wiki texts of Willett 2023 (`doi-10.1038-s41586-023-06377-x`), Anumanchipalli 2019 (`pmc-9714519-speechsynth`) and Herff 2015 (`doi-10.3389-fnins.2015.00217`), the two topic audits, and the bioRxiv API record for 10.1101/2020.06.30.180935.

## Claim table

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | First public 2020-07 (bioRxiv v1 2020-07-01); synthesis added only in the journal version, online 2020-11-11 (ref 1 note) | bioRxiv API: one version, 2020-07-01, title "Decoding spoken English phonemes ...", abstract has no synthesis | correct | Prior cutoff 2020-01 and [concurrent] window 2020-01 to 2021-01 follow from it. The synthesis is dated 2020-07 internally (open item in `verification_status`). No claim depends on that: Herff 2019 is prior either way. |
| 2 | 10- and 11-class syllable and word decoding, T5 84.6% on 10 syllables [2] (Verdict, M06) | stavisky.txt, Results | correct | T5: syllables 10 classes 84.6%, words 11 classes 83.5%. |
| 3 | Brumberg: 38 attempted phonemes, 16–21%, chance 2.6% [3] | audit read_fulltext quote | correct | |
| 4 | Mugler: all phonemes in words, hand-labelled onsets, 4 ECoG subjects; best subject 36.1% consonants, 23.9% vowels [4] | mugler.txt Sec. 3.1; target Sec. 3.2 | correct | Mugler's mean over subjects was 20.4% on all phonemes; the review uses the best subject (NU2), as the target does. |
| 5 | Matched test: 36.8% on 24 consonants and 27.7% on 16 vowels; 2% and 16% relative (inference) | target text offset ~50.1k, inside Sec. 3.2 | correct number, wrong section | The passage is in Sec. 3.2, before the Sec. 3.3 heading. The review and claim table say Sec. 3.3. The arithmetic is right (1.9%, 15.9%). |
| 6 | Calling the matched test "like-for-like" (M06) | target Sec. 4.1: "should not be viewed as exact, matched performance tests but rather ballpark estimates" | wrong (wording) | This contradicts the authors' own caveat, which the review quotes elsewhere. Onset labelling (hand vs audio-derived), classifier and word set (232/256 shared) differ. |
| 7 | Livezey: deep networks, 57 CV syllables, 4 ECoG subjects [6] | claim-table quotes | correct | "The RNN gain ... follows [6]" is loose: Livezey used feedforward deep networks. The target cites Livezey, Angrick and Anumanchipalli together for machine-learning methods (Sec. 3.2). |
| 8 | Willett 2023 [later]: 62% on 39 attempted isolated phonemes from 6v arrays, one participant; 28.1 points above 33.9% (inference) | Willett text: "naive Bayes classifier applied to 1 s ... 39 phonemes with 62%"; "speak single phonemes" | correct | The conditions are mostly stated. It could add that Willett's decoder is naive Bayes on a 1-s window and the target's is an RNN on 500-ms windows. I know of no later intracortical isolated-phoneme result above 62% under comparable conditions. The audit correctly rejects a 92% sequence-decoding candidate as a different metric. |
| 9 | RNN 33.4% (Sec. 3.4) vs 33.9% (Abstract, Sec. 4) | target text | value correct, wrong section | 33.4% is at the end of Sec. 3.2 (offset ~51.0k, before the 3.3 heading). Sec. 2.6 adds a third value: 32.4% with the electrode exclusions vs 33.9% without. |
| 10 | Matched set: 256 of 320 (Sec. 2.2) vs 232 shared plus 80 replaced (Sec. 3.3); "neither sum is 320" | target Sec. 2.2: "already had 256 of the 320 words ... To fill out the remaining 64 words"; Sec. 3.2: "232 of our words ... the missing 80 words" | wrong | Sec. 2.2 sums to 320 (256 + 64). Only Sec. 3.2 fails (232 + 80 = 312). The inconsistency is real; the stated reason is wrong, and so is the section (3.2, not 3.3). |
| 11 | Chance 6% has no derivation; uniform chance ≈ 2.6% (inference) | target: Abstract only; the Results use permutation tests without stating the level | correct (insufficient derivation) | A 6% figure is higher than uniform chance, so it is conservative, not an overclaim. Mugler reports empirical chance levels (7.4%, 12.9%), which suggests a frequency-based estimate. Better placed as a question than under "claims outrun the evidence". |
| 12 | T11 11.22% vs T5 29.29% "does not repeat it" | target Sec. 3.2 | number correct, misleading referent | 11.22% is the 39-class HLFP result. No matched Mugler test was run in T11, so "it" (the matched test) misdescribes it. |
| 13 | Folds are "utterance-level" over three repetitions of 420 words; test phonemes share words with training (Verdict; "Where" bullet, Secs. 2.2, 2.7) | target Sec. 2.7: logistic regression "in a leave-one-out cross-validation setup"; LOO for Figs 3A, 3F, 5D; 20-fold for Figs 4, 5E, 5F; Sec. 2.8: RNN "10 folds ... such that each spoken phoneme utterance appeared in the test set once" | wrong (understated) | Folds are over phoneme instances, not word utterances. The other phonemes of the same spoken word, whose 500-ms windows overlap the test window, are in training as well as the other two repetitions. The authors themselves note overlapping phoneme windows within a training fold (Sec. 2.7, duration sweeps). In Sec. 3.2 they also say the 420-word dictionary lets longer windows "exploit neural correlates of adjacent phonemes". The Verdict presents this as the reviewer's inference without that credit. |
| 14 | "Competitive" (Sec. 1) becomes "ballpark estimates" (Sec. 4.1); the authors judge two dorsal arrays insufficient (Sec. 4) | target offsets 12.8k (Intro), 70.6k (3.7), 72.4k (Sec. 4), 86.5k (4.1) | correct | |
| 15 | Synthesis r = 0.523 vs Herff best 0.574, mean 0.246; most random trials unintelligible (Sec. 3.7) [9] | target Sec. 3.7 | correct | These are values as reported by the target. Herff 2019 itself was not read (see fix L8). |
| 16 | Roussel: 20 datasets, 5 centres, ECoG and intracortical; ECoG decoders with and without 90–200 Hz [5]; bioRxiv 2019-08 | roussel.txt Abstract, Table 1, Sec. 3.2 ("ECoG data from participants P2 and P5") | correct | P5 also had a Utah array, but the decoding comparison used P5's ECoG. "ECoG decoders" is right. |
| 17 | LRR 29.3% → 25.8%, 12% relative (inference); realignment 54.9% → 47.8%, 12.9% (Sec. 3.4); pre-voice 34.8% over 18 classes (Sec. 3.5) | target Secs. 3.4, 3.5 | correct numbers | Under "controls lower accuracy modestly", the pre-voice window is 34.8% against 54.9% for the centred window, a 37% relative drop (inference). Window position also changes, but the review lists it with no comparison point. The Discussion cites the pre-voice result as Fig. 5D, the Results as Fig. 5F, an inconsistency in the target. |
| 18 | LRR can remove shared neural signal, "as the target concedes (Sec. 3.5)" | target Sec. 3.5: "it also can subtract out genuine neural signal that is shared across electrodes" | correct claim, wrong quote | Claim table row 15 quotes a Sec. 4.1 sentence about residual contamination instead. |
| 19 | Peterson 2024 [later]: artifact removal in 54 patients; consonant decoder re-tested, similar or better than raw; ICA lowers accuracy [8] | peterson.txt | partly correct | The decoder re-test covers three subjects (A–C), not the 54-patient set; the sentence merges the two. No number is given (values are only in Fig. 7b). A plausible state-of-the-art choice for "artifact removal with decoding re-tested". Later intracortical speech BCIs (for example Willett 2023, and possibly later ones from the same group) may include Roussel-style contamination checks. Unverified. |
| 20 | Verdict: M12 "adds overt-speech confound controls that no prior decoder with full text in the Appendix population applies" | M12 audit design counts: pre-onset window 5, condition-invariant 1; Anumanchipalli 2019 (`pmc-9714519-speechsynth`, in the population with full text): "To rule out the possibility that the decoder is relying on the auditory feedback ... we tested our decoder on silently mimed speech" | wrong (overstated) | The review's own Appendix counts mentions of two of the three control types in prior decoders. Anumanchipalli 2019 ran an explicit overt-speech confound control: a mimed condition against auditory feedback and acoustic signal, which the target lists among the possible corrections ("auditory feedback restriction", Sec. 4.1). Only "contamination test or artifact removal: 0" supports an absence claim. |
| 21 | M06 usual approach: of 28 decoders (19 full text), 8 mention a full inventory, 8 a deep network (pattern match, mentions) | M06 audit prior_tally | correct tallies, incomplete as a usual approach | The most frequent mention in the same tally is a small unit subset, 12 of 19. The audit's own usual-approach design (published table) is "small subset". The line names the precedent (full inventory exists) rather than the usual design. The table cell "pattern match 8" has no denominator and no "mentions" label, so it reads as a design count. The M12 cell "pattern match 19" is likewise an absence-of-mention count with no "of 19". |
| 22 | 28-decoder population, filtered and version-merged | M06/M12 audit population_pids, version_groups | mostly correct | Herff 2015 appears as `pmc-4464168-brain2text`, but its sibling `doi-10.3389-fnins.2015.00217` is not in the version group (no count effect). Kellis et al. 2010 (`pmc-2970568-lfpwords`, spoken-word decoding from micro-ECoG, cited by the target) is in the wiki but not in the population. Moses 2016 (listening) and Makin 2020 ([concurrent], 2020-03) are correctly excluded. Salari 2019 (repeated vowels) is correctly excluded as a non-decoder. |
| 23 | Deciding priors for M06 (Brumberg, Mugler, Stavisky, Livezey) and M12 (Roussel, Stavisky) correctly characterised | reader files, audits | correct, one missing for M12 | Anumanchipalli 2019 (mimed control) should be a deciding prior for the M12 absence claim. Herff 2015 used 20 phones plus silence (a subset, not a full inventory) and leave-one-phrase-out validation, which bears on the word-held-out point. Pei 2011, Guenther 2009, Angrick 2019 and Moses 2019 do not change either verdict. |
| 24 | "Headline accuracies are single cross-validated estimates, no seeds (Sec. 2.8; Fig. 3)" | target Sec. 2.7; Fig. 3 caption ("standard deviation across 10 repetitions of 10-fold") | insufficient as worded | The 29.3% is leave-one-out, which is deterministic, so seeds do not apply. The real gap is no interval on the headline numbers and no repeated RNN runs. The sweeps do report s.d. |
| 25 | M12 "standard, not ahead": the step comes from Roussel, realignment covers first phonemes only (Sec. 4.1), T5 only | target Sec. 4.1: "restricted to classifying the first phoneme"; SKILL `standard` = "difference not supported well enough to call" | correct | The verdict follows the rules: single participant, no other repetition, deciding prior read. The authors' own novelty framing is not credited: "novel use of a decontamination procedure" (Sec. 4) and "two potential limitations which have received little prior attention" (Sec. 1). |

No model names and no non-English text appear in the review. The `.md` is identical to `draft-before-evaluation/review.md`.

## Required fixes, ordered by severity

### High

**H1. The fold unit behind the "strongest confound" is misdescribed, and the authors are not credited.**
- Location: Verdict, sentence 4; "Where the claims outrun the evidence", shared-words bullet; Questions, first bullet; claim table rows 4 and 18.
- Evidence: Sec. 2.7 says logistic regression ran "in a leave-one-out cross-validation setup" (Figs 3A, 3F, 5D); Sec. 2.8 says the RNN used "10 folds ... such that each spoken phoneme utterance appeared in the test set once". Sec. 2.7 also notes "overlapping phoneme windows in the same training fold". In Sec. 3.2 the authors say "given the limited dictionary size ... (420 words), increasing the decoding window may allow the classifier to exploit neural correlates of adjacent phonemes".
- Fix: State that folds are over phoneme instances, not utterances. Neighbouring phonemes of the same spoken word, whose 500-ms windows overlap the test window, sit in training alongside the word's other repetitions. Credit the authors' Sec. 3.2 caveat in the Verdict sentence, and keep "(inference)" only for the claim that no word-held-out test bounds the effect. Correct "Secs. 2.2, 2.7" so text and claim table agree (2.7 and 2.8). Optionally cite Herff 2015's leave-one-phrase-out validation as a prior with held-out utterances.

**H2. The Verdict's M12 absence claim is broader than the Appendix supports.**
- Location: Verdict, sentence 3 ("adds overt-speech confound controls that no prior decoder ... applies"); M12 slot note.
- Evidence: The M12 Appendix counts pre-onset window mentions in 5 prior decoders and condition-invariant alignment in 1. Anumanchipalli et al. 2019 (Nature 568:493, doi:10.1038/s41586-019-1119-1, wiki `pmc-9714519-speechsynth`, in the 28-decoder population with full text) decoded silently mimed sentences "to rule out the possibility that the decoder is relying on the auditory feedback of participants' vocalization". The target names "auditory feedback restriction" as one such correction (Sec. 4.1).
- Fix: Restrict the absence claim to "a contamination test or artifact removal (0 of 19, pattern match, Appendix)". Name Anumanchipalli 2019 as a deciding prior (mimed-speech control) in the M12 section and the Appendix; read it and add a `read_fulltext` entry. The M12 verdict stays `standard`.

### Medium

**M1. The inconsistency in the matched word count is misstated.**
- Location: "Where the claims outrun the evidence", Inconsistencies bullet; claim table row 22.
- Evidence: Sec. 2.2: "already had 256 of the 320 words ... To fill out the remaining 64 words" (256 + 64 = 320). Sec. 3.2: "232 of our words ... the missing 80 words" (232 + 80 = 312).
- Fix: Write "256 shared plus 64 filled (Sec. 2.2) against 232 shared plus 80 replaced, 312 in all (Sec. 3.2) (inference)". Drop "neither sum is 320" and correct the section to 3.2.

**M2. "Like-for-like" contradicts the authors' own caveat.**
- Location: M06 section, paragraph after the State of the art line.
- Evidence: Sec. 4.1 says the comparisons "should not be viewed as exact, matched performance tests but rather ballpark estimates". Mugler hand-labelled onsets (mugler.txt, Data Preprocessing), while the target uses audio-derived onsets. The comparison is against Mugler's best subject only (mean 20.4% on all phonemes).
- Fix: Write "The closest matched test is the authors'" and attach the Sec. 4.1 caveat to that paragraph. State that the comparator is Mugler's best subject and that the onset labelling differs.

**M3. The M06 usual approach and the table counts read as design counts, and the most common design is omitted.**
- Location: M06 "Usual approach" line; 13-components table, rows M06 ("pattern match 8") and M12 ("pattern match 19"); `slots.json` field text.
- Evidence: The M06 prior_tally gives small unit subset 12 of 19 mentions, full inventory 8, deep network 8. The audit's own usual-approach design is "small subset".
- Fix: State in the Usual approach line that small unit subsets (12 of 19 mentions) were the typical design at the time, and that the full inventory (8 mentions, 2 confirmed by reading) is the precedent the target follows. In the table write "8 of 19 (mentions)" and "19 of 19 without a contamination-test mention".

**M4. The authors' own claims and caveats are not credited at their locations, and one quote is wrong.**
- Location: M12 section ("The paper adds LRR re-referencing ..."); M12 State of the art line; claim table row 15.
- Evidence: The authors call LRR a "novel use of a decontamination procedure previously deployed for electrical stimulation artifact reduction" (Sec. 4). They frame both confounds as having "received little prior attention" (Sec. 1). The "removes genuine shared neural signal" concession is in Sec. 3.5 ("it also can subtract out genuine neural signal that is shared across electrodes"), but claim row 15 quotes a Sec. 4.1 sentence on residual contamination.
- Fix: Report the authors' novelty framing before the verdict, and say why the review still calls the component standard. Replace the claim-table quote with the Sec. 3.5 sentence.

### Low

**L1. Wrong section locations.**
- Location: Inconsistencies bullet ("33.4% in Sec. 3.4"); M06 matched test and claim table ("Sec. 3.3").
- Evidence: Both passages sit in Sec. 3.2, before the Sec. 3.3 heading.
- Fix: Change both to Sec. 3.2. Optionally add the third RNN value (32.4% with electrode exclusions, Sec. 2.6).

**L2. The chance item is misframed.**
- Location: "Where the claims outrun the evidence", Chance bullet.
- Evidence: 6% is above uniform chance (2.6%), so it is conservative. Mugler reports empirical chance levels (7.4%, 12.9%).
- Fix: Keep this as a question for the authors, or reword it as "underived, probably frequency-based" rather than an overreach.

**L3. The Peterson state-of-the-art line merges two cohorts and gives no number.**
- Location: M12 State of the art line.
- Evidence: The DenseNet re-test covers subjects A–C. The 54-patient set is the denoising application.
- Fix: Say "three subjects" for the decoder re-test. Read the values from Fig. 7b, or state "values only in Fig. 7b" in the open items; that note is already there, so it is not published text.

**L4. The pre-voice result has no comparison point.**
- Location: M12, controls paragraph.
- Evidence: 34.8% pre-voice vs 54.9% for the centred window (Sec. 3.5), a 37% relative drop (inference).
- Fix: Give both numbers and say the window position differs, so the drop is not an estimate of contamination alone.

**L5. The T11 sentence points at the wrong test.**
- Location: M06, "T11 does not repeat it (11.22% against 29.29%)".
- Fix: Reword as "T11 reaches 11.22% against T5's 29.29% on the 39-class task; no matched test was run in T11 (Sec. 3.2)".

**L6. The RNN lineage is attributed to [6] alone.**
- Location: M06, "The RNN gain is modest (Sec. 4) and follows [6]".
- Evidence: Livezey used feedforward deep networks. The target cites [6] with Angrick and Anumanchipalli (Sec. 3.2).
- Fix: Write "follows the deep-network work it cites [6]", or drop "follows [6]".

**L7. The variability bullet is imprecise.**
- Location: "Where the claims outrun the evidence", Variability bullet.
- Evidence: The headline 29.3% is leave-one-out, which is deterministic. The Fig. 3 sweeps do report s.d. over 10 repetitions of 10-fold cross-validation.
- Fix: Say there is no interval on the headline accuracies and no repeated RNN runs.

**L8. Population and version gaps.**
- Location: Appendix, M06 and M12 population.
- Evidence: Kellis et al. 2010 (`pmc-2970568-lfpwords`, prior spoken-word micro-ECoG decoder, cited by the target) is in the wiki but absent from the population. The Herff 2015 sibling `doi-10.3389-fnins.2015.00217` is not merged.
- Fix: Add Kellis 2010 to the population (the counts become 29 decoders) or justify its exclusion. Merge the Herff 2015 versions.

**L9. Process notes in published text.**
- Location: References, ref 9 note ("values as reported by the target"); Appendix M06 ("[3] and [7] (state of the art) from the published table").
- Fix: Remove both phrases. The reading status belongs in the JSON (`read_fulltext`, `verification_status`).

## Scores

- Procedure: 7/10. Dating is correct and checked, the population is filtered and version-merged, the deciding priors for M06 are read and correctly characterised, and the verdict rules are applied correctly. Points are lost because Anumanchipalli 2019 (mimed control, in the population) is missing as an M12 deciding prior, because of the fold-unit misreading of Secs. 2.7–2.8, and because of the Kellis 2010 population gap.
- Final text: 6/10. The position is clear and most numbers match the source. Points are lost because the central confound is misdescribed, the M12 absence claim in the Verdict is overstated, one stated inconsistency is factually wrong, "like-for-like" contradicts the authors, two sections are wrong, and two process notes remain in published text.

## Final counts by severity

- High: 2 (H1, H2)
- Medium: 4 (M1–M4)
- Low: 9 (L1–L9)
- Total required fixes: 15
