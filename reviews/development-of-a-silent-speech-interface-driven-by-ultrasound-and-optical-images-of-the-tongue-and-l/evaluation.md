# Evaluation of the component review draft

Evaluator: a language model separate from the writer

Date: 2026-11-27. Target: Hueber et al., Speech Communication 52(4), 2010, doi:10.1016/j.specom.2009.11.004. Files read: the review (`<slug>.md`), `compact.md`, `claims.md`, `<slug>.slots.json`, `verdict.json`, the three audits (M06, M08, M12), and the wiki source texts of the target (accepted manuscript, HAL), [2] (`isca-hueber09_cdms`), [3] Kaburagi 1998, [4] Engwall 2005, [7] Li 2019, [10] Sonkar 2026, [11] Hueber 2011, [13] Hueber and Bailly 2016, and the merged versions `icassp2007-hueber-eigentongue-ssi`, `icphs2007-hueber-ouisper`, `isca-hueber08_segvocoder`. The wiki and the review files were not modified.

## Claim check

| # | Claim (location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | First public 2009-11; [2] Interspeech 2009 [concurrent] | Target p.1 (accepted 19 Nov 2009, received 5 Dec 2008); [2] header (6–10 Sep 2009) | correct | [2] is 2 months before the target, so [concurrent] is right. Note that the manuscript was received 2008-12, before [2] existed. |
| 2 | Earlier conference versions merged with the target (Appendix M06, M08) | M06/M08 audit `merged_target_versions`; ICASSP 2007 text | wrong for one item | ICASSP 2007 "Eigentongue" is not an earlier version of this route. It maps ultrasound and lip features to LSF with a neural network ("Extracted visual features are input to a neural network which learns the relation between the vocal tract configuration and line spectrum frequencies", Abstract). That is direct mapping, and merging it hides it. See F1. |
| 3 | "Recognition then synthesis ... first shown at Interspeech 2008 [9]" (M08) | ICPhS 2007 Ouisper Abstract | wrong | ICPhS 2007 already describes the route: "The search is driven by the recognition of phone units using Hidden Markov Models trained on video sequences." The audit merges this paper, but the text names 2008. |
| 4 | M06: 10 of 11 prior unique studies use HMMs (pattern match) | M06 audit dated_counts; wiki titles | insufficient evidence (one miss) | `isca-manabe03_eurospeech` (EMG, recognizes 5 Japanese vowels with a three-layer neural network, Eurospeech 2003) fits the inclusion rule and is missing. The count becomes 10 of 12. The verdict does not change. |
| 5 | M08: 2 prior studies, both direct mapping; recognition then synthesis 0 | M08 audit; Kaburagi Sec. 3 | partly wrong | Correct for the two studies counted. However, the group's own ICASSP 2007 direct mapping is merged away (F1), and Kaburagi gates its database search with a phoneme decision (F5). |
| 6 | "context-dependent models 'could not have been efficiently trained' on under one hour (§4.1)" | Target Sec. 4.1 | correct | Quote and location match. |
| 7 | [2]: 61 minutes, single speaker; CD fusion 57.7 to 62.6; CD-MSHMM 65.6; 8-point gain | [2] Sec. 2.1, Table 1, Sec. 5 | correct (numbers); condition missing | The numbers match. [2] uses 1020 sentences in 34 lists, 40 phones, and two lists held out for validation. The target uses 780 sentences (about 45 min) in 26 lists and 41 phones. The baselines differ: 57.7% in [2] against 59.0% in the target. See F3. |
| 8 | "The journal cites it only as ongoing fusion work (§4.2)" | Target Sec. 6 | wrong | Sec. 6 says: "the use of context dependent multistream HMMs as in Gravier et al. (2002) is being tested, and preliminary results look interesting (Hueber et al. (2009))." See F2. |
| 9 | Kaburagi: phoneme-restricted search preferred for 84% of stimuli by ten listeners | Kaburagi Abstract, Sec. 3.1–3.2, Sec. 4.2 | correct; condition missing | This was a pairwise quality preference: ten subjects, ten sentences, excitation taken from the original speech, frame-level phoneme classification. It was not an intelligibility test. |
| 10 | Engwall: maps EMA frames directly to LSP | Engwall Sec. 2, 4 | imprecise | The input is EMA tongue coils plus optical facial motion capture (Qualisys), mapped through talking-head articulatory parameters. |
| 11 | M06 SOTA: 6.17% WER, SSC, 5k-word bigram [7] | Li 2019 Abstract, Table 2, Sec. 3.3 | insufficient quote | 6.17% (DCAE, length 60) is correct. Li gives no "5k bigram"; it only says it follows the setting of Ji et al. 2018 [ref 1 there]. |
| 12 | M08 SOTA: 15.93% single-speaker / 31.64% multi-speaker WER on TaL [10] | Sonkar Abstract, Sec. 6, Table 1 | correct | ASR is Whisper Medium, and Day 1 is excluded. Say "Whisper ASR WER". |
| 13 | M12 SOTA: median 43.75% listener WER [12]; group's 60% word accuracy [13] | audit read_fulltext; CSL 2016 Sec. 5 | correct quotes; inconsistent as SOTA | 60% word accuracy (about 40% WER) is better than the named SOTA. It is for modal speech, French, the better speaker only, and silent speech was lower. See F6. |
| 14 | "apart from the target, the 30 confirmed studies ... date from 2014 on" (M12) | M12 audit dated_counts (confirmed_unique 29 + target = 30) | wrong count | Apart from the target there are 29. Nine of them have no index year. |
| 15 | 7 listeners, 20 sentences, oracle phones, 97% ceiling (§5.3, Fig. 10) | Target Sec. 5.3 | correct | |
| 16 | About 60% is not enough for intelligible synthesis (§6) | Target Sec. 6 | correct | The same caveat appears in Sec. 5.3 (66%) and in the 2008 paper. |
| 17 | 66% in §5.3 vs 67.6% in Table 1 | Target Sec. 5.3, Table 1 | correct | This is a real internal inconsistency in the paper. |
| 18 | Speaker B transducer shift after 240 sentences; B 10.7 points lower | Target Sec. 2, Table 1 (59.0 − 48.3) | correct numbers; misleading framing | The first 240 sentences were dropped from both speakers, so the shifted images are not in the data. The remaining B data are "less stable". The authors report all of this themselves. See F4. |
| 19 | Hybrid "without limiting the available vocabulary" vs test words covered | Target Sec. 4.1, 4.2 | correct (inference) | The word lists and the diphone/triphone lists come from the CMU-Arctic sentences, which include the test lists. |
| 20 | Validation experiments and PCA subset not stated to exclude test lists | Target Sec. 3, 4.1 | correct | [2] states that its validation lists were excluded. The target does not. |
| 21 | "all data are uttered speech from two speakers (§2)" | Target Introduction p.5 | wrong location | The uttered-speech statement is in the Introduction, before Sec. 2. |

## Findings (ordered by impact)

**F1 — High — Appendix M08 and M06 (merged_target_versions), Verdict sentence 3, M08 Usual approach.**
Evidence: the audits merge `icassp2007-hueber-eigentongue-ssi` as a target version. Its abstract says ultrasound and lip features "are input to a neural network which learns the relation between the vocal tract configuration and line spectrum frequencies (LSF) contained in a one-hour speech corpus". This is the group's own direct mapping from ultrasound and video, evaluated only by normalized MSE. It is a different design from the target's recognition-then-unit-selection route, so it is not an earlier version of it. Merging it removes the one direct-mapping prior on the same modality and from the same lab. It also hides the group's own path: direct mapping in 2007, recognition then synthesis in 2007–2009, then GMM/HMM mapping in 2011 [11].
Fix: un-merge ICASSP 2007 and count it as a prior direct-mapping study (M08: 3 prior, direct mapping 3). Cite it in the M08 Usual approach. Change "both prior speech-output studies" to "all three prior studies, including the group's own 2007 neural mapping on the same corpus". Recast "no direct-mapping baseline is run" as "the group's own 2007 direct mapping is not compared on the same data or measure". In M06, drop the ICASSP 2007 and ISSP 2008 entries from merged versions because neither has a recognizer, or label them "same system, no recognizer".

**F2 — High — M06 section, last two sentences ("is contradicted by ..."; "The journal cites it only as ongoing fusion work (§4.2)").**
Evidence: Sec. 6 of the target says that context-dependent multi-stream HMMs are "being tested, and preliminary results look interesting (Hueber et al. (2009))". The manuscript was received on 5 Dec 2008, before [2], and revised in Oct 2009. [2] also trained on about 59 of 61 minutes, while the target trained on about 43 of 45 minutes. So the assumption in Sec. 4.1 is not "contradicted on under one hour". It dates from before [2], and the authors themselves flag it as superseded.
Fix: replace both sentences with: "The stated reason for staying context-independent (§4.1) dates from the December 2008 submission; the group's [concurrent] study on a larger 61-minute set obtained 62.6% with context-dependent fusion and 65.6% with context-dependent multi-stream HMMs against a 57.7% baseline [2], and the journal points to these results itself (§6)."

**F3 — Medium — Verdict sentence 2 ("weaker than the authors' own [concurrent] ... decoder [2]"); ref [2] note "same group and databases".**
Evidence: [2] reports one unnamed speaker, the first 1020 sentences (34 lists), 40 phones, and validation lists excluded. The target uses 780 sentences per speaker after dropping 240 (26 lists), 41 phones, and validation inside the jackknife. The baselines differ: 57.7% in [2] against 59.0% for the target's speaker A. The task is the same (CMU-Arctic continuous phone decoding, free phone loop and a 2.5k-word dictionary). The data subset and protocol are not.
Fix: say "weaker than the context-dependent multi-stream decoder of the [concurrent] study [2], an 8-point gain over its own baseline on a larger 1020-sentence set of the same corpus". Change the ref note to "same group and corpus, different subset and protocol".

**F4 — Medium — Verdict sentence 4, "Where the claims outrun the evidence" bullets 1 and 4 (fairness).**
Evidence: the authors state that the oracle test "is in no way meant to be an evaluation of the final performance of our system" (Sec. 5.3). They write "reasonably intelligible ... when the phonetic prediction is correct" themselves. They report B's displacement, drop the first 240 sentences from both speakers, and attribute B's deficit to it (Sec. 2, 4.2). Bullet 4 says "B's transducer shifted after 240 sentences" as if the shifted data were used, but they were dropped. Only residual instability remains ("palatal traces of speaker B between Time 2 and Time 4 still appeared less stable").
Fix: in the Verdict, write "system output from recognized phones is not measured, as the authors state (§5.3)". In bullet 1, keep only the overreach that is the review's own: the conclusion "a reasonable approach for making an SSI" rests on oracle phones and five web examples, with no aggregate score and an unnamed speaker. Rewrite bullet 4 as: "The authors report that B's images were displaced, drop the first 240 sentences from both speakers, and note residual instability (§2); with B 10.7 points lower (Table 1), the second speaker is not a replication (inference)." Alternatively, move it to an "authors' own caveats" clause.

**F5 — Medium — M08 section ("0 of 2 prior" vs "The closest prior already couples a phoneme decision to a database search"); Appendix M08 classification.**
Evidence: Kaburagi Sec. 3 does the following. "Before the sample selection, the phoneme category of the input articulator position is first determined and the search area of the database is restricted to portions of the same category." The classification is frame-level, done in phoneme-specific subspaces. The 84% result is a pairwise quality preference with excitation taken from the original speech (Sec. 4.2). Counting this study as pure "direct mapping" while the text calls it the closest precursor of recognition-gated selection is inconsistent.
Fix: classify Kaburagi as "phoneme-gated lookup (frame-level), direct spectral output". Say that the target's departure is sequence-level phone recognition plus diphone unit selection, not the use of a phoneme decision. Add the conditions to the 84% sentence: quality preference, original excitation, ten sentences.

**F6 — Medium — M12 State of the art line and table row.**
Evidence: the named SOTA is a 43.75% median WER [12]. The same line gives 60% word accuracy [13], which is about 40% WER (inference) and so better. [13] Sec. 5 reports that result for modal speech, French, the better speaker only (Sec. 4.1.3), and it says silent-speech decoding was 15% worse. [12] is intracortical, attempted vocalization by one participant. Neither condition is stated, and neither is comparable to an oracle-phone test.
Fix: state the conditions for both: "[12] intracortical, attempted vocalized speech, open transcription; [13] modal French speech, best speaker". Either pick one as SOTA with its condition or write "no comparable test; best reported listener scores are ...". Do not call a result SOTA when the same line gives a better one.

**F7 — Medium — M08 Usual approach ("first shown at Interspeech 2008 [9]"); dating of the route.**
Evidence: ICPhS 2007 (Ouisper), which the M08 audit merges, already uses HMM phone recognition to drive the corpus search. The 2008 paper adds the segmental vocoder evaluation.
Fix: write "first shown at ICPhS 2007 and Interspeech 2008 [9]" and add the ICPhS 2007 reference. On the dating question, keep 2009-11 as the counting date for the usual approach. This is the consolidated journal, and the counts are the field at the time it was written. For precedence statements, use the first version (2007-08). Recomputing with a 2006-10 cutoff leaves HMMs in the majority for M06 (about 6 of 8 in the ledger, inference), and M08 keeps 0 prior recognition-then-synthesis studies. Neither verdict changes. State this in one Appendix clause.

**F8 — Medium — M12 Usual approach ("apart from the target, the 30 confirmed studies"); slots.json M12 note "0 of 30 confirmed before 2014"; absence claim without deciding priors.**
Evidence: the audit gives `confirmed_unique` 29 without the target and 30 with it. Nine studies have no index year and are assumed to be later. The absence claim ("not yet practice") names no prior. The two prior output studies that were read used a pairwise preference test (Kaburagi Sec. 4.2) and "informal subjective judgment" (Engwall Sec. 5). The group's own 2011 work [11] ran a transcription test (3 listeners, 15 sentences) with no score, which fits the 2014 boundary of the rule.
Fix: write "apart from the target, the 29 confirmed studies (9 without an index year) date from 2014 on (Appendix); the two prior output studies used a quality preference test [3] and informal judgment [4]". Correct the slots note to "0 of 29 other confirmed studies before 2014".

**F9 — Low — Appendix M06 population completeness.**
Evidence: `isca-manabe03_eurospeech` ("Speech Recognition Using EMG; Mime Speech Recognition", Eurospeech 2003) recognizes vowels from EMG with a three-layer back-propagation network. It is in the wiki, within the rule, and not in the 11. The target also cites Jorgensen et al. 2003 (EMG/EPG, IJCNN) and Fagan et al. 2008 (PMA, Med. Eng. Phys. 30(4)) as SSI recognizers. Neither is in the wiki, and neither uses an HMM according to their own descriptions (unverified here). NAM studies (Nakajima, Heracleous) are correctly excluded as acoustic input. The Schultz/Jou line is complete.
Fix: add Manabe 2003 (HMM 10 of 12, neural network 4). In one clause, add that two recognizers the target cites (Jorgensen 2003, Fagan 2008) are outside the ledger.

**F10 — Low — M08 population completeness (outside the wiki).**
Evidence: two direct-mapping studies known from outside knowledge are not in the wiki: Denby and Stone, "Speech synthesis from real time ultrasound images of the tongue", ICASSP 2004 (ultrasound to LSF, neural network), and Toda, Black and Tokuda, "Statistical mapping between articulatory movements and acoustic spectrum using a Gaussian mixture model", Speech Communication 50(3), 2008 (EMA, GMM). Venue and page details are unverified here. Both would make direct mapping more clearly the usual approach. The "one speaker each" generalization would not hold for Toda 2008 (MOCHA, more than one speaker; unverified).
Fix: no change to counts (ledger only). Optionally add one clause to the Appendix: "known direct-mapping studies outside the ledger (Denby and Stone 2004; Toda et al. 2008) are not counted".

**F11 — Low — M06 State of the art ("with a 5k-word bigram language model").**
Evidence: Li 2019 Sec. 3.3: "We followed the same setting for the whole recognition system as in [1]" (Ji et al. 2018). The text gives no LM size. The SSC 2010 data are 60 fps helmet recordings, a different and later acquisition by the same lineage.
Fix: write "Kaldi DNN-HMM in the setting of Ji et al. 2018". Either drop "5k bigram" or cite Ji 2018 for it. Add "single speaker, 60 fps ultrasound" as the condition.

**F12 — Low — M08 Usual approach (Engwall characterization).**
Evidence: Engwall Sec. 2 combines EMA tongue coils with Qualisys facial motion capture, mapped to talking-head articulatory parameters, then to LSP.
Fix: write "EMA and facial motion capture to LSP through talking-head parameters [4]".

**F13 — Low — M06 Usual approach example "3-state phone HMMs [6] [concurrent]".**
Evidence: the usual approach is defined over prior studies. [6] is [concurrent] and cannot illustrate the prior norm.
Fix: replace it with a prior example from the 10, for example Maier-Hein et al. 2005 (ASRU) or Walliczek et al. 2006. Keep [6] only as a [concurrent] aside.

**F14 — Low — M12 verdict reason ("Verdict standard: unusual for its time, but ...").**
Evidence: under the rules, `standard` applies here because the difference "is not supported well enough to call": one oracle-phone test, an unnamed speaker, 20 sentences. "Unusual for its time" reads as if the rule had been set aside.
Fix: write "Verdict standard: no confirmed prior used listener transcription (Appendix), but a single oracle-phone test of 20 sentences from an unnamed speaker measures unit selection and HNM, not the interface (§5.3)."

**F15 — Low — Verdict sentence 4 location; restated results.**
Evidence: "all experiments are performed here using uttered speech" is in the Introduction (p. 5), not §2. The M06 State of the art line restates the full Table 1 ranges for both speakers, which is a results restatement.
Fix: cite "(Introduction; §2)". In the M06 SOTA line keep one figure (best phone accuracy 67.6%, speaker A, word-based dictionary that includes the test words) and drop the ranges.

## Checks that passed

- [concurrent] labels for [2], [6] and [8] and [later] labels for [7] and [10]–[13] are correct under the ±6-month rule.
- The Appendix labels all-years figures (M06 neural network 81 / HMM 60; M08 direct 60 / recognition 22; M12 crowd workers 15) as all-years and pattern match, and the verdicts do not use them.
- The M08 `standard` verdict is consistent with the rules. `ahead` would need an effect shown with repetition and a comparison, and the paper has neither.
- The 60%, 66% vs 67.6%, 10.7-point, 97% ceiling and seven-listener numbers all match the target.

## Scores

- Procedure: 6/10. The populations were hand-enumerated and labelled. However, the version merge hid a same-lab direct-mapping prior, and one in-wiki M06 prior was missed.
- Final text: 6/10. The positions are clear and mostly sourced. One factual error about the target's own citations, an inconsistent M12 SOTA, and some of the authors' own caveats presented as the review's findings need fixing.

Counts: High 2, Medium 6, Low 7.
