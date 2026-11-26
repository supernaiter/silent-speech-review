# Evaluator: a language model separate from the writer

Date: 2026-11-26. Target: Angrick et al., "Real-time synthesis of imagined speech processes from minimally invasive recordings of neural activity", Communications Biology 4, 1055 (2021), doi:10.1038/s42003-021-02578-0.

Inputs read: compact.md (review + claim table), the review .md, slots.json, verdict.json, the three topic audits (M04, M06, M12: `tally_at_target_time_*`, `state_of_the_art_*`, `known_item_recall`, `read_fulltext`, candidate lists), notes.json entries t1-t71, the target source text (wiki `papers/doi-10.1038-s42003-021-02578-0/source/text.txt`), reader texts for Martin 2014, Brumberg 2018, Bocquelet 2016, Angrick 2019, Herff 2019, and the wiki source texts for Anumanchipalli 2019, Komeiji 2024, Angrick 2024, Wairagkar 2025 and Brain2voice 2.0 (doi-10.64898-2026.06.30.735633). The authors' public repository (cognitive-systems-lab/closed-loop-seeg-speech-synthesis, `master` as fetched on 2026-11-26) was used to check the code claims, because the code is not stored in the wiki or in the work folder.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | One participant, three ~5-min runs, no repetition | target Methods: Participant, Task | correct | Female, 20 y; 100 words per run. "her" is correct. |
| 2 | Imagined 0.32 ± 0.26 vs null 0.17 ± 0.22; whispered 0.64 ± 0.15; n1 = 75 | target Results: imagined, whispered | correct | Whispered value is labelled "median" in the paper, imagined "mean"; the review drops the label (see F7). |
| 3 | Null = 1,000 2-s segments from a separate grasping/eye-fixation session | Results: whispered; Fig. 4c legend | correct | Critique (null does not separate words) is sound. |
| 4 | Imagined output "scored only by DTW correlation" | Results: imagined; Fig. 4d | wrong in part | The paper also reports a VAD trial vs intertrial gating analysis (Fig. 4d). It does not test word content, but "only" is inaccurate (F8). |
| 5 | High-gamma 150-200 ms before current frame; inferior and middle frontal | Results: Anatomical and temporal contributions | correct as quoted | The inference built on it is not (F3). |
| 6 | More intertrial detections in imagined than whispered "agrees" with prompt-reading drive | Results: imagined; Fig. 4d | wrong (logic) | Prompt-driven output would be locked to the 2-s prompt window, not to the 1-s blank interval. The authors give their own explanation (F3, F4). |
| 7 | 7.331 ms per 10 ms frame | Table 1 | correct | Table total 7.331; text says 7.3 ms. These are processing times, not end-to-end latency; the review asks about latency, which is right. |
| 8 | Authors' "two major issues ... unaddressed" omits closed loops [6], [5] | Introduction; reference list (t71) | partly unfair | Issue (1) reads "all studies synthesizing speech from the neural activity are based on open-loop experiments". Bocquelet 2016 is EMA, not neural, so it is not a counterexample. Brumberg 2018 is (F5). |
| 9 | Guenther 2009 "did not attempt ... beyond basic vowel sounds" is accurate | Introduction (t5); Guenther 2009 | correct | |
| 10 | M06: 6 of 44 prior, 5 closed loops (intracortical 1, EMA 3, EEG 1) | M06 audit tally_at_target_time | matches audit; meaning unclear | 3 of the 5 are non-neural. Bocquelet 2015 (pilot) and Bocquelet 2016 may be one system (F6, F9). |
| 11 | Guenther 2009 / Brumberg 2018 / Bocquelet 2016 designs and dates | reader1 texts; refs | correct | Brumberg 2018: limb motor imagery (left hand, right hand, feet) mapped to vowel formants, not speech imagery. The review's "EEG motor imagery" is accurate. |
| 12 | M06 SOTA: Wairagkar 2025, median WER 43.75% | wiki pmc-12369848 text | correct | A stronger 2026 work meets the review's own M06 rule (F10). |
| 13 | M04: 8 of 21 confirmed (EMG 4, US/video 2, ECoG 2), Martin 2014 offline covert transfer | M04 audit; Martin 2014 text | correct | "Usual design, 8 of 21" needs wording (F11). Martin trained on overt and tested on covert, offline: correct. |
| 14 | M04 SOTA Komeiji 2024: 46.3% TER, 16 patients, offline | wiki text | correct | Sentence-level text decoding, not synthesis; acceptable for M04 as a transfer design. |
| 15 | M12: 7 prior produced/mimed/imagined reconstructions, 3 with identification or listener test | M12 audit (pids listed) | correct as tallied; dates all before 2021-03 | Population classification checked (F1, F2). |
| 16 | Martin 2014: "pairwise identification of covert reconstructions" | Martin 2014 Sec. 3, Fig. 10-11 | wrong | It is percentile-rank identification among 24-140 candidate 5-s segments (N = 123 in the best subject). Group rank 0.55 vs 0.5; significant in 1 of 7 subjects (F2). |
| 17 | Herff 2019: four-option listener test 66.1% vs 25% | Herff 2019 Results | correct | Overt speech. |
| 18 | Anumanchipalli 2019: median 31% WER, 25-word pool | wiki text | correct | Listener tests on audible output only. The mimed condition was scored by spectral distortion and correlation against audible trials, not by listeners. |
| 19 | M12 SOTA: Angrick 2024 80%; Berezutskaya 2023 92-100% | wiki texts | correct values; incomplete condition | 80% is over a 6-keyword vocabulary; Berezutskaya uses 12 words (chance 8%). Wairagkar 2025 [7] has a stronger identification result (F12). |
| 20 | STOI dropped (400 ms); "not intelligible" | Results: audible open-loop | correct | |
| 21 | Identification "over the 250-word list" is direct with matched references | Methods: Task; Results: imagined | wrong | Only words spoken in the audible run have references; 75 imagined words overlap (F13). |
| 22 | Fig. 4 script computes medians | figure_4.py:48-52 (master) | correct, but anchor not stored | The paper itself already shows the inconsistency (F7). |
| 23 | Fig. 3 test: n2 = 100 stated, script pools 1,000 | figure_3.py:118-143 (master) | correct | 100 reruns x 10 folds, `np.vstack`, Mann-Whitney per bin against `rc_corrs`. |
| 24 | VAD settings differ from config/evaluation.ini | evaluation.ini:21-26; exp3.py:47-51; vad.py:24 | correct, incomplete | Config holds threshold 0.5 and mean scale 1. The class default threshold is 4, as in the paper. `getint` on mean scale means 0.5 could not have been passed through this config (F14). |
| 25 | Whispered reference is the audible articulation; whisper below mic sensitivity | Results: whispered | correct, but authors' own statement | Presented as a finding (F4). |

## Findings (ordered by impact)

**F1. High. M12 verdict sentence and Verdict paragraph: the named "best comparable work" is inconsistent and mostly not comparable for the imagined condition.**
- Location: M12 closing sentence ("behind, against the best comparable work, Anumanchipalli et al. [10]"); Verdict sentence 3 ("behind the group's own earlier four-option listener test [3]").
- Evidence: Two different works are named as the yardstick. Both Herff 2019 and Anumanchipalli 2019 ran listener tests on intelligible overt reconstructions. Anumanchipalli's mimed condition, the closest to the target's silent conditions, was scored only by spectral distortion and correlation against audible trials. The target states its output "is not intelligible" (Results), so a listener test is not the fair yardstick. The one prior that identified covert reconstructions without acoustic ground truth is Martin 2014 [2]. It warped reconstructions to overt references with DTW and ranked them among candidates, which is the target's own reference setup. That makes Martin 2014 the best comparable work for the imagined claim. The rule (at least 3 earlier papers, best one read and named) is still met by the 3 pids (Martin 2014-05, Anumanchipalli 2019-04, Herff 2019-11, all before 2021-03). The naming, however, must be one work, and it should be Martin 2014.
- Fix: Name Martin et al. [2] as the best comparable work in both the Verdict and M12. Write: "behind, against the best comparable work, Martin et al. [2], who ranked covert reconstructions against DTW-aligned overt references (group rank 0.55, chance 0.5)". Keep Herff [3] and Anumanchipalli [10] as the overt listener-test examples.

**F2. High. M12 Usual approach: Martin 2014 design misdescribed, and the strength of the prior identification result is not given.**
- Location: M12 Usual approach, "pairwise identification of covert reconstructions [2]".
- Evidence: Martin 2014, Evaluation section and Figs. 10-11, quantified identification as "the percentile rank of the correct segment" among 24-140 5-s candidate segments (N = 123 in the best subject). Group median rank was 0.55 against chance 0.5 (p < 0.05). Covert identification beat chance in only 1 of 7 subjects (Discussion). This is not pairwise. Its weakness also matters for fairness: an identification test on imagined output was feasible in 2014, but expected to be weak.
- Fix: Write "rank identification of covert reconstructions among 24-140 candidate segments, group rank 0.55 against 0.5 chance, significant in 1 of 7 subjects [2]". Add one clause that a weak but above-chance rank test is still informative where DTW correlation against a non-speech null is not.

**F3. High. "Where the claims outrun the evidence", bullet 2: the inference that intertrial detections "agree" with prompt-reading drive is backwards, and the Fig. 5 lag does not support it.**
- Location: bullet 2 ("A visual prompt precedes every trial ... more detected speech in imagined than whispered intertrial intervals (Fig. 4) agrees").
- Evidence: Each word is shown for 2 s, followed by a 1-s blank intertrial interval (Methods: Task). Output driven by reading the prompt would be locked to the prompt window. Extra detections during the blank interval point to output that is not prompt-locked (noise or unpaced imagery), so they weaken the prompt-reading account rather than support it. The 150-200 ms lag in Fig. 5 is relative to the current output frame, not to prompt onset. The weights also come from the audible training run, so they cannot show what drives the imagined output. The real gap still stands: there was no prompt-only or reading-only run, and the whispered run had the same prompts.
- Fix: Drop "agrees" and the Fig. 5 link. State the confound directly: "every imagined trial followed a visual word prompt, and no prompt-without-imagery run was recorded, so gated output during trials does not by itself show imagery (inference)". Keep the matching question to the authors.

**F4. Medium. Fairness: the authors' own caveats are presented as the review's findings.**
- Location: "Where the claims outrun the evidence", bullets 2 and 4. M04 paragraph "Transfer is small".
- Evidence: For the intertrial detections the authors write "This is likely due, in part, to the inherent difficulty of knowing how the participant internally performed imagined speaking" (Results: imagined). The whispered-reference limitation ("below the sensitivity of the microphone. Therefore no reference is available") is the authors' statement (Results: whispered). The authors also state that the output "is not yet intelligible" and that only prompted single words were tested (Discussion). Bullet 4 adds no critique; it only restates the paper.
- Fix: Delete bullet 4, or turn it into a critique (for example, that DTW to a different-run audible token inflates correlation for both conditions and the null). Credit the authors' explanation in bullet 2 ("the authors attribute this to uncertainty about how the participant performed imagery").

**F5. Medium. M06 "missed citations" sentence: the quoted sentence is truncated, and one of the two works is outside the authors' stated scope.**
- Location: M06 paragraph, "The claim that 'two major issues remain unaddressed ...' omits the uncited closed loops [6], [5]".
- Evidence: The quote stops at the colon. Issue (1) reads "all studies synthesizing speech from the neural activity are based on open-loop experiments". Bocquelet 2016 synthesizes from EMA, not neural activity, so it is not a counterexample. Brumberg 2018 (EEG, closed loop, vowel formants) is one, but it decodes limb motor imagery, not speech imagery, so it does not contradict "the only research addressing both issues is" Guenther 2009. The authors' next paragraph already names Guenther as a real-time exception, so issue (1) is internally inconsistent in the target itself. That is a fairer and stronger point. Both works were published before the target (2016, 2018), so citing them as missed is chronologically fair.
- Fix: Write: "Issue (1), that 'all studies synthesizing speech from the neural activity are based on open-loop experiments' (Introduction), is contradicted by the authors' own Guenther example and omits Brumberg et al. [5], a closed-loop EEG formant synthesizer; Bocquelet et al. [6] synthesized from articulography and is outside that sentence."

**F6. Medium. M06 standard: the any-signal boundary is not applied consistently with M12, and the Verdict's "5 prior closed loops" hides that only 2 are neural.**
- Location: Verdict sentence 1; M06 Usual approach; table row M06; Appendix M06.
- Evidence: The M06 rule admits EMA, PMA, EMG, ultrasound and video, while M12 restricts its population to neural recordings of produced, mimed or imagined speech. Under M06's at-target-time tally, 3 of the 5 closed loops are EMA and the sixth study is PMA. Only Guenther 2009 (intracortical) and Brumberg 2018 (EEG) are neural, and both output two vowel formants. Published speech-BCI reviews generally describe the target as the first closed-loop synthesis from imagined speech (unverified here; no locator checked). The "standard" call is defensible, because the ahead rule needs repetition and this is one participant. But it must say so, and it must not lean on the EMA loops as if they were the same setting.
- Fix: Verdict: "5 prior closed loops, 2 of them neural (intracortical vowels [4], EEG motor-imagery vowels [5])". M06 verdict sentence: "standard: no earlier neural closed loop synthesized words (Appendix), but the effect has no repetition across participants or sessions, which the ahead rule requires". Add to the M06 Appendix entry that the boundary is any non-acoustic signal, and give the neural subcount.

**F7. Medium. Code-vs-paper claims: the anchors are file:line only, with no commit SHA and no stored snapshot; and the mean/median inconsistency is visible in the paper itself.**
- Location: "Where the claims outrun the evidence", bullet 5; Questions for the authors, item 2; claim table rows 21 and 23.
- Evidence: notes t66-t68 cite `eval_steps/figure_4.py:48-59`, `eval_steps/figure_3.py:118-143`, `config/evaluation.ini:21-26`, `eval_steps/exp3.py:47-53` and `local/vad.py:24-30`. None of these files is stored in the wiki paper folder or in the work folder, and no commit is recorded. I fetched `master` on 2026-11-26, and all three claims hold at those lines. figure_4.py logs `np.median` with `np.std` for both conditions. figure_3.py stacks 100 reruns x 10 folds into the chance array used by `mannwhitneyu`. evaluation.ini sets `vad_energy_threshold = 0.5` and `vad_energy_mean_scale = 1`. Independently of the code, the paper calls the whispered 0.64 ± 0.15 a "median" and the imagined 0.32 ± 0.26 a "mean" in parallel sentences, and the Fig. 4c legend says the black lines are medians.
- Fix: Lead with the paper-internal inconsistency ("the whispered value is reported as a median, the imagined as a mean, and Fig. 4c plots medians"), then cite the code with a pinned commit SHA and the retrieval date. Save the five files, or their hashes, with the notes. If no commit can be pinned, mark the code points "(repository master, retrieved <date>)".

**F8. Medium. Verdict: "imagined output is scored only by DTW correlation" omits the VAD gating analysis.**
- Location: Verdict sentence 3.
- Evidence: Fig. 4d and Results: imagined report the proportion of VAD-detected speech in trials vs intertrial intervals. This is a second test, of timing rather than content.
- Fix: Write "imagined output is scored by DTW correlation against a non-speech null and by VAD gating; neither tests word content".

**F9. Medium. M06 count "6 of 44": the meaning of the design count is unclear, and a version double count is possible.**
- Location: M06 Usual approach; table row M06 ("Online or causal synthesis, of 44 (pattern match 6)"); Appendix.
- Evidence: The 44 are pattern-match hits with year ≤ 2020, not synthesis studies, so "6 of 44" says online synthesis was a minority design. It does not describe a "usual approach" that the target matches. The audit's 3 EMA loops include `isca-bocquelet15-dnnsynth` (a real-time pilot) and `doi-10.1371-journal.pcbi.1005119` (Bocquelet 2016). These share authors and system, and the rule says "count versions once". The basis "year ≤ 2020" also differs slightly from the stated cutoff "before 2021-03".
- Fix: Reword to "Of 44 prior pattern-match studies at the target's time, 6 synthesized online or under simulated causal inference (Appendix)". Check whether Bocquelet 2015 is a version of the 2016 study and, if so, give 5 and 4. Align the cutoff wording with the basis.

**F10. Medium. M06 State of the art: the review's own rule admits a stronger work than the one cited.**
- Location: M06 State of the art; table row M06.
- Evidence: The M06 rule includes "offline studies only when they simulate causal frame-level inference". The M06 audit's overall state of the art is Brain2voice 2.0 (doi-10.64898-2026.06.30.735633, 2026, bioRxiv). It reports a 5.24% median listener WER on the same intracortical benchmark as Wairagkar 2025, with causal 10-ms outputs ("an 8x improvement ... over previous SOTA results (43.75%)").
- Fix: Cite it as the state of the art with "(2026) [later], preprint, simulated causal", or state why it is excluded (offline, not closed loop) and restrict the line to "closed loop with playback".

**F11. Low. M04 Usual approach wording: "the confirmed usual design, 8 of 21".**
- Location: M04 Usual approach; table row M04.
- Evidence: 8 confirmed of 21 pattern-match candidates is a design count, not a majority. The audit's 8 pids and the signal split (EMG 4, US/video 2, ECoG 2) are correct, and so is Martin 2014 as offline overt-to-covert transfer. "The method is Martin et al.'s run in closed loop" overstates: Martin used linear spectrotemporal and modulation regression; the target uses quantized LDA classification.
- Fix: Write "8 of 21 prior candidates confirmed this design (Appendix)" and "the design is Martin et al.'s [2], run in closed loop".

**F12. Low. M12 State of the art: conditions missing, and a stronger identification result already in the reference list is not used.**
- Location: M12 State of the art; table row M12.
- Evidence: Angrick 2024's 80% is over a 6-keyword vocabulary (Abstract). Wairagkar 2025 [7] reports listener matching of synthesized sentences to 1 of 6 transcripts at mean 94.34% and median 100% (Results, Fig. 2l left). Whether that was scored on the closed-loop output is unverified.
- Fix: Add "6 words" to the 80% figure, and add or consider Wairagkar [7] "94.34% six-option sentence identification (2025) [later]".

**F13. Medium. M12 paragraph and "What the field needs next": identification "over the 250-word list" is not possible with the recorded references.**
- Location: M12 paragraph ("which the 250-word list and matched overt references make direct"); What the field needs next, M12 item.
- Evidence: References exist only for words spoken in the audible run (100 prompts). 75 imagined words overlapped with it (Results: imagined), and the DTW analysis uses exactly those.
- Fix: Write "closed-set (rank) identification of each imagined trial among the ~75 words with audible references, against a mismatched-word null, as in Martin et al. [2]".

**F14. Low. VAD claim incomplete.**
- Location: "Where the claims outrun the evidence", bullet 5.
- Evidence: `local/vad.py:24` defaults to threshold 4 and mean scale 1, so the paper's threshold 4 matches the class default. The config overrides it with 0.5 and 1, and `exp3.py:49` reads the mean scale with `getint`, so 0.5 could not be passed through this config.
- Fix: Write "the paper's VAD threshold 4 and mean scaling 0.5 match neither config/evaluation.ini (0.5, 1) nor a value the script can read for the mean scale (integer); which values produced Fig. 4d is unclear". Pin the commit (F7).

**F15. Low. Reference list annotations.**
- Location: References [2], [11], [12].
- Evidence: [2] Martin 2014 carries "Target. Read as the published article.", but it is not the target of this review. [11] and [12] carry internal notes ("state of the art for M04", "state of the art of the published M12 table").
- Fix: Remove "Target." from [2] and the internal notes from [11] and [12].

**F16. Low. Process wording in the body.**
- Location: M12 closing sentence ("read in full").
- Evidence: Reading status belongs in the Appendix.
- Fix: Delete "read in full" from the body.

**F17. Low. M12 Usual approach: "4 report correlation only" is imprecise.**
- Location: M12 Usual approach; table row M12.
- Evidence: Angrick 2019 (doi-10.1088-1741-2552-ab0c59) reports correlation and STOI (reader2/angrick2019.txt, Fig. caption "STOI scores"). The category the tally actually tests is "no identification or listener test".
- Fix: Write "4 report no identification or listener test".

**F18. Low. M04 paragraph mixes summary statistics.**
- Location: M04 "Transfer is small: ... 0.15 above the null".
- Evidence: 0.32 is labelled a mean and 0.64 a median, and the code computes medians (F7). The "(inference)" label on the difference is right, but the difference rests on an unclear statistic.
- Fix: Write "0.32 (labelled a mean; likely a median, see below) ... 0.64 (median)", or drop the 0.15 subtraction.

## M12 population check (requested)

- Population of 7 (audit pids): Martin 2014 (ECoG, overt and covert), Chakrabarti 2015 (ODU dissertation, ECoG produced speech features), Angrick 2019 JNE (with its bioRxiv merged), Herff 2019, Anumanchipalli 2019 (pmc version merged), Angrick 2020 Interspeech, Clayton 2020 Interspeech (EEG imagined, heard, spoken).
- All are dated before 2021-03.
- Exclusions are right: Akbari 2019 (heard speech), Makin 2020 (text), Moses 2019 (classification or text).
- Classification is right: 3 have identification or listener tests (Martin, Herff, Anumanchipalli). Angrick 2019 has correlation and STOI only.
- Possible outside-ledger omissions, unverified and not required fixes: Herff et al. 2016 EMBC pilot of direct synthesis from ECoG; Krishna et al. 2020 ICASSP EEG speech synthesis.
- Known-item recall 0.67 (the missed seed is Anumanchipalli 2019, added by hand), as the Appendix states.

## Scores

- Procedure: 6/10. Tallies are traceable and the dates are right. The deciding prior for the imagined condition is misnamed, the code anchors are not pinned, and the boundaries differ between slots without being stated.
- Final text: 6/10. The central position (no word-content test for imagined output, one participant) is sound and well supported. Two supporting inferences are wrong or unfair (intertrial "agrees", Bocquelet as a missed neural citation), and the yardstick naming is inconsistent.

Counts by severity: High 3, Medium 9, Low 6.
