# Evaluator: a language model separate from the writer

Date: 2026-11-26. Independent pass over `asr-is-all-you-need-cross-modal-distillation-for-lip-reading.md`, `compact.md`, `claims.md`, `*.slots.json`, `verdict.json`, the three topic audits, `tools/` (window counts, recall outputs) and the wiki source texts of the target and of the cited works (read-only). Brief: `references/evaluator-brief.md`; verdict rules: `skill-draft/SKILL.md` step 4.

## Claim check

| # | Claim (location in review) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | ASR teacher supplies transcripts and posteriors for unlabelled video (Verdict s1) | target Fig. 1 caption, §3.3 | correct | |
| 2 | Teacher trained on Librispeech (Outrun 1) | target §4.1, Table 1 | correct | The abstract itself says the teacher "has been trained on a large-scale audio-only corpus" (see fix 11). |
| 3 | LRS2 58.2 vs 58.5, LRS3 65.6 vs 68.8; 0.5% and 4.7% relative (M02) | target §5, Table 3 | correct | 0.3/58.5 = 0.51%; 3.2/68.8 = 4.65%. |
| 4 | VoxCeleb2 clean: LRS3 65.6 -> 61.7, 5.9% relative; LRS2 54.2 row also adds ASR-labelled LRS3 (M02) | target Table 3 rows "CTC + KD ASR ASR ASR 54.2" and "CTC + KD ASR _ ASR 61.7" | correct | 3.9/65.6 = 5.95%. |
| 5 | Filtered subset 334 h, ~140k of 1M utterances (Outrun 2) | target Table 1, §2 | correct | |
| 6 | "two ASR-agreement filters (90% valid English words; under 28% inter-recognizer WER)" (Outrun 2) | target §2 | wrong in detail | The first filter is a dictionary proxy on teacher output (share of words with 4 or more characters that are valid English words), not an agreement filter. Fix 12. |
| 7 | No teacher WER reported (Outrun 2) | target §3, §4.1, Table 3 | correct | |
| 8 | Margins over Conv-seq2seq 0.4 (51.3 vs 51.7) and 0.3 (59.8 vs 60.1) (Verdict, M12) | target Table 3, §5 | correct | Conv-seq2seq is [concurrent] (ICCV 2019; target marks it concurrent). |
| 9 | TM-seq2seq LRS3 59.9 without, 58.9 with external LM (M12) | [3] Table 2, row "TM-seq2seq V 49.8% 48.3% 59.9% 58.9%" | correct | Values verified. The sentence omits that TM-seq2seq was trained on non-public MV-LRS (target Table 3 dagger). Fix 13. |
| 10 | V2P 55.1 ± 0.9 on full LRS3 test, bootstrap error (Verdict, M12) | [2] Table 2 and §5 ("standard error ... estimated by bootstrap sampling") | correct | It is the test-resampling standard error of one system's WER, applied in the Verdict to an LRS2 difference between two systems. Fix 9. |
| 11 | Authors: Conv-seq2seq "very close to ours"; proprietary-data systems remain better (§6) | target §6 | correct | |
| 12 | Training-speed claim against CTC on ASR transcripts is shown only against CTC on GT (Outrun 3) | target §1 and Fig. 2 | correct | Fig. 2 is described by the authors as "indicative" greedy validation WER. |
| 13 | Authors name Wei Li et al. as "the closest work" (§1.1) | target §1.1 | correct quote | The review's gloss "uses the same mechanism" contradicts §1.1: there the teacher is trained with ground truth on the same dataset as the student, the student is audio-visual, and the method "does not apply naturally to unlabelled audio-visual data". Fix 1. |
| 14 | 77 of 77 earlier sentence-level studies use human or caption transcripts (M02 usual approach) | audit `counts_...`, `usual_approach_...`, `tools/m02_pop.json` | insufficient evidence | This is an absence count (no hit for three alternative regexes), not a count of the stated design. Fix 3. |
| 15 | Appendix: "Designs among the 77: ASR-generated labels 3 hits ...; unlabelled video 1 hit (enhancement)" | audit `prior_hits` vs. excluded list | wrong | isca-siciliano03_avsp, pmc-3810281-talkerxmod and arxiv-1804.04121 are in the excluded list, so they are not among the 77. Fix 10. |
| 16 | No wiki study before 2019-05 distils an audio/ASR teacher into a non-acoustic decoder (M02) | `tools/recall_distill.json`, KD audit | correct as worded | The nearest hard-target analogue is not named. Fix 5. |
| 17 | LIBS needs ground-truth sentences; 65.29% LRS2 WER; [concurrent] (arXiv 2019-11-26) | [6] Eq. 10 text, Table 5 | correct | |
| 18 | Throat-microphone student learns from a close-talk teacher; [concurrent] | [7] abstract; Interspeech 2019 (September) | correct; framing loose | A throat microphone is a body-conducted acoustic sensor, not a "non-acoustic decoder". Fix 14. |
| 19 | Prior cutoff before 2019-05; target first public 2019-11 | target arXiv v1 (Nov 2019); plan window | correct | |
| 20 | M12: 2 earlier LRS3 visual-only studies, 0 repeated runs, 1 bootstrap | `tools/m12_win.json`, M12 audit | correct | Deep Lip Reading (arxiv-1806.06053) and Hybrid CTC/Att. (arxiv-1810.00108) have no LRS3 results, so N = 2 holds. With only 2 priors the `behind` rule (3 or more) cannot apply, so `standard` is consistent with the rules. |
| 21 | USR 2.0 17.6% LRS3 VSR, 656 h labelled + 2,649 h unlabelled, own pseudo-labels, ICLR 2026 | [4] abstract, Table 7 | correct value | Not the lowest public-data figure in [4]'s own Table 7 (SynthVSR 16.9%). Fix 6. |
| 22 | Auto-AVSR 19.1% with external-ASR labels | [5] Table 2 (3,448 h) | correct | |
| 23 | LP Conformer 12.8% with 100k h non-public video | [8] abstract and §data (YT 100k h) | correct | Year given as 2023 in the text but ICASSP 2024 in the reference. Fix 15. |
| 24 | Gaps 44.1, 42.2, 47.0 points (inference) | arithmetic | correct | The 44.1-point M02 gap compares a no-human-label figure with a system trained on 656 h of human labels. Fix 7. |
| 25 | "single-run" WERs (Verdict, M12, table M03/M12) | target §4–§5, Table 3 | insufficient evidence | The paper gives one WER per row and states no run count; the review itself asks how many runs (Questions). Fix 8. |

## Required fixes, ordered by impact

**1. Major. Location: Verdict, sentence 3; M02 closing verdict ("the closest prior the authors name uses the same mechanism"); `slots.json` M02 note.**
Evidence: the `standard` verdict leans on Wei Li et al. (ICASSP 2019, pp. 6560–6564), which is cited by the authors (§1.1). That work is not in the wiki (no index or title match), was not read, has no `read_fulltext` entry, and is not in the reference list. Its first-public date is also unresolved. ICASSP 2019 met 12–17 May 2019, which falls inside this review's [concurrent] window (2019-05 to 2020-05). It would be prior only if its IEEE Xplore posting date (April 2019, unverified) is used. The target's own §1.1 says it differs on exactly the point M02 is about: the teacher is trained with ground truth on the student's dataset, the student is audio-visual, and the method "does not apply naturally to unlabelled audio-visual data". So "uses the same mechanism" is the reviewer's claim about an unread paper. Under SKILL step 4 it cannot decide a verdict. The other stated reasons do not settle the verdict either. A missing CTC-on-ASR-labels arm isolates only the KD term, not the label-source change. The `ahead` rule accepts repetition across datasets, and the label-source effect is reported on two datasets (LRS2, LRS3).
Fix: drop Li et al. as a reason, or read and cite it with a resolved date and label it prior or [concurrent] accordingly. Base `standard` on the rule clause "not supported well enough to call", for example: "the label-source effect is inconsistent across the two datasets (0.3 points on LRS2, 3.2 on LRS3), each from one reported WER, and the distillation term is not separated from CTC on ASR labels (no Table 3 row)." Update the `slots.json` note to match.

**2. Major. Location: Verdict, sentence 4 ("The 'no human labels' LRS2 result is a 0.3-point single-run difference, below V2P's 0.9-point bootstrap error").**
Evidence: the authors claim parity on LRS2 ("our method achieves similar performance on LRS2 (58.2%) and even better on LRS3 (65.6%)", §5) and conclude that human labels "are not necessary". A difference inside test noise supports a parity claim; it does not weaken it. As written, the sentence treats as a weakness the outcome the authors predicted. What the review can show is narrower: parity of ±1 point cannot be told apart from a loss of 1–2 points without spread, and the supervision moved to transcribed Librispeech audio and Librispeech LM text.
Fix: rewrite along the lines of "On LRS2 the no-label arm matches ground truth within V2P's test-set standard error (58.2% against 58.5%), which supports the authors' parity claim. The supervision moved to a teacher and a language model trained on transcribed Librispeech (§4.1), and which term carries the result is untested."

**3. Moderate. Location: M02 "Usual approach" ("Human or caption transcripts: 77 of 77"); 13-components table M02 "(pattern match 77)"; Appendix "Usual design: human or caption transcripts, 77 of 77".**
Evidence: in the audit (`counts_<slug>.regex`, `prior_hits`), the 77 are the whole dated-prior part of the 633-study sentence-level population after exclusions. No pattern for "human or caption transcripts" was run. The figure means "no full-text hit for the ASR-label, distillation or unlabelled-video regexes". The tier "pattern match" next to the positive design reads as a design count. Also, the inclusion rule names self-supervision as a label source, but no self-supervision regex was run.
Fix: write "none of the 77 earlier sentence-level studies has a full-text match for ASR-generated labels, teacher distillation or unlabelled video (pattern match, absence count, Appendix)". Drop "77 of 77" for the positive design, or label it "inferred from absence". Add a self-supervision term to the Appendix regex list, or remove self-supervision from the inclusion rule.

**4. Moderate. Location: Verdict sentence 2 and M02 usual approach ("none ... used ... unlabelled video").**
Evidence: Perfect Match (arxiv-1809.08001; ICASSP 2019, arXiv 2018-09, prior) appears in the 118 raw prior hits and was excluded as "audio-visual synchronisation". Its abstract says it uses "the learnt embeddings for visual speech recognition in self-supervision". It trains a lip-reading front end from untranscribed video, with audio as cross-modal supervision, and reports LRW word accuracy (Table 2). It is word-level, so leaving it out of a sentence-level population is defensible, but then the exclusion reason is wrong. SyncNet ("Out of time", Chung and Zisserman 2016) is the same idea; it is outside the wiki (unverified locator).
Fix: change the exclusion reason to "word-level (LRW), self-supervised audio-visual pretraining". Then either narrow the absence claim to "ASR-generated labels or distillation", or name Perfect Match as a word-level prior that already used audio as supervision for a lip-reading encoder on unlabelled video.

**5. Moderate. Location: M02 paragraph "Across signal types, no wiki study before 2019-05 ... distils an audio or ASR teacher into a non-acoustic decoder"; Appendix KD recall.**
Evidence: the any-signal recall was run in an acceptable form. A custom `recall2.py` scanned all 3,089 full-text studies before 2020-06 and every hit was classified. This is not the standard `--fulltext-pattern` / `recall_sample` path (`fulltext_pattern: null` in the audits), but it covers more. Its regexes, however, key on distillation and ASR-label vocabulary, so they miss audio-model-to-visual label transfer through forced alignment. Among the 77 kept priors, Sari et al. 2018 (isca-sari18-avicar, Interspeech 2018) uses "an audio ASR that is pre-trained using a much larger corpus (including portions of the Librispeech corpus ...)" whose "state-level forced alignments ... [are] used as output targets for the CNN used as visual feature extractor". Tatulli and Hueber 2017 (icassp2017-tatulli-multimodal-cnn-vsr) labels ultrasound and video frames from an audio ASR's forced alignment. Both use known transcripts and hard targets, so neither has the same design. But they are the nearest priors to the frame-wise term, which the authors credit for the speed-up ("explicit alignment information", §5). None of the expected outside-wiki examples is a speech-decoding prior with the same design. SoundNet and Albanie et al. 2018 use a visual teacher for an audio student; Owens et al. 2016 is not speech; Gupta et al. 2016 is RGB to depth. EMG and ultrasound work from that period regresses audio features or uses audio forced alignments, which is the same pattern as above.
Fix: name Sari et al. 2018 (and optionally Tatulli and Hueber 2017) in M02 as the closest earlier designs: an acoustic model gives frame targets to a visual decoder, on transcribed data with hard labels. Say that what the target adds is untranscribed video and soft posteriors. Add the forced-alignment class to the Appendix recall decisions.

**6. Moderate. Location: M02 and M12 "State of the art" (USR 2.0 17.6% "on public data"); table M02/M12.**
Evidence: [4]'s own Table 7, in the wiki source, lists SynthVSR at 16.9% LRS3 VSR (6,720 labelled hours, with language model) and ViT3D-CM at 17.0% (90,000 h non-public). SynthVSR (Liu et al., CVPR 2023) describes its training data as publicly available real data plus synthetic video (unverified beyond [4]'s table). USR 2.0's 17.6% is without a language model.
Fix: either state the condition under which USR 2.0 is best (no external LM, no synthetic training video, unified model), or cite SynthVSR 16.9% as the best public-data VSR WER and recompute the gaps (inference).

**7. Moderate. Location: M02 "State of the art", last sentence ("61.7% ... is 44.1 points higher (inference); model and data scale differ").**
Evidence: 61.7% uses no human labels, while USR 2.0 uses 656 h of human-labelled data (Table 7 of [4]). The gap mixes label regime with model and data scale.
Fix: add "and USR 2.0 uses 656 h of human labels". Alternatively, compare like with like: the paper's 59.8% (also ground truth) against 17.6%, or 61.7% against an external-ASR-label system with its labelled hours stated (Auto-AVSR, 818 h labelled plus 2,630 h automatically labelled, [5] Table 2).

**8. Minor. Location: Verdict ("single-run difference"); M12 heading and body ("single-run WERs"); table M03 "one run", M12 "one run".**
Evidence: the paper does not state how many runs underlie each row; the review's own Questions ask this. "Single run" goes beyond the evidence.
Fix: "one WER per row, with no run count or spread (Table 3)".

**9. Minor. Location: Verdict sentence 4; M12 margins sentence.**
Evidence: V2P's ±0.9 is the bootstrap standard error of one system's WER on the LRS3 full test set ([2] §5, Table 2). The Verdict applies it to an LRS2 difference between two arms that share a test set.
Fix: write "within V2P's test-set bootstrap standard error for a single system on LRS3 (±0.9; LRS2's test set is similar in size, 1,243 against 1,452 utterances) (inference)". Do not imply a significance test.

**10. Minor. Location: Appendix, first M02 entry ("Designs among the 77 ...").**
Evidence: of the three ASR-label hits, isca-siciliano03_avsp and pmc-3810281-talkerxmod are in the excluded list, and the unlabelled-video hit arxiv-1804.04121 is also excluded. Among the 77 there is 1 ASR-label hit (rs-19574628-saenko, forced alignment), 1 distillation hit (arxiv-1806.06053, mention) and 0 unlabelled-video hits.
Fix: give the hits "among the 118 raw" and among the 77 separately, as above.

**11. Minor (fairness). Location: "Where the claims outrun the evidence", bullets 1–2.**
Evidence: the abstract states that the teacher "has been trained on a large-scale audio-only corpus". The fine-tuned rows are labelled ASR/GT and GT in Table 3. §6 concedes "Given resource constraints we only utilized VoxCeleb2", which bears directly on "arbitrary amounts".
Fix: report these statements first. Then write that the text reports them honestly and the abstract wording overstates. Drop "the best rows fine-tune on ground truth" as evidence against claim (i), which concerns the no-ground-truth rows.

**12. Minor. Location: "Where the claims outrun the evidence", bullet 2.**
Evidence: the target's §2 describes a valid-word proxy on teacher output, followed by a second-recognizer agreement filter.
Fix: "two ASR-based filters: at least 90% of teacher-output words of 4 or more characters are valid English words, and under 28% WER between the teacher and a second recognizer (§2)".

**13. Minor. Location: M12, sentence on TM-seq2seq LM; M12 and Verdict on Conv-seq2seq.**
Evidence: TM-seq2seq's 59.9%/58.9% come from training on non-public MV-LRS (target Table 3 dagger; [3] Table 1). Conv-seq2seq (Zhang, Cheng, Wang, ICCV 2019, pp. 713–722) is used for the central M12 margin but has no reference entry, and its language model is not stated.
Fix: add "trained on non-public MV-LRS" to the TM-seq2seq sentence. Add a reference entry for Conv-seq2seq ([concurrent]) and say that its decoder and LM are not given in the target's Table 3.

**14. Minor. Location: M02 "Both same-family works are [concurrent] ... a throat-microphone student".**
Evidence: [7] distils a close-talk acoustic model into a throat-microphone (body-conducted audio) acoustic model. The student signal is acoustic.
Fix: call it an adjacent design (acoustic teacher into a body-conducted-audio student), not a same-family non-acoustic decoder.

**15. Minor. Location: M12 "State of the art" and table ("LP Conformer (2023)") vs reference 8 ("ICASSP 2024").**
Fix: use one convention, for example "LP Conformer (arXiv 2023; ICASSP 2024)".

**16. Minor (process notes in body). Location: M02 usual approach "(pattern match, snippets read, Appendix)"; M12 usual approach "(corpus paper excluded; pattern match, Appendix)".**
Evidence: SKILL writing rules ban notes on what was read in the body.
Fix: keep "(pattern match, Appendix)" and move "snippets read" and "corpus paper excluded" to the Appendix, where they already appear.

**17. Minor. Location: Appendix ledger counts "1,049 unique studies pattern match over all dates", "258 ... over all dates", "22 ... 131 with ledger or full-text mentions (all dates)", and "slot-filled 31 (M02)" (date scope not stated).**
Evidence: the review's comparisons are made at the target's time, and these all-years totals carry no claim. They are labelled, but "slot-filled 31" has no date scope.
Fix: state "all dates, not used in the comparison" once per topic, and give the date scope of "slot-filled 31", or replace these with the target-time counts that are already given.

**18. Minor. Location: M12 usual approach ("no comparator decoders").**
Fix: "does not state the decoders or language models of the comparator rows (Table 3)".

**19. Minor (unverified). Location: 13-components table, M03 "ASR-agreement filter ... standard".**
Evidence: V2P builds its data on Liao et al. (2013) ([2] §3). The same Google YouTube pipeline is described in [8] as keeping "islands where the user-uploaded captions match the result of a pre-trained audio-only speech recognition system". That is the nearest prior to the target's agreement filter. Whether V2P itself applies the island filter is not stated beyond the citation.
Fix (optional): give the M03 row its basis, for example "ASR-agreement filtering of web captions, V2P lineage [2]", or leave M03 uncounted.

## Scores

- Procedure: 6/10. Target-time windows, exclusions and the any-signal recall were done and recorded. The verdict reason relies on an unread, outside-wiki, date-unresolved work. The positive usual-approach count is an absence count. Self-supervision and forced-alignment label transfer were not searched.
- Final text: 6/10. Numbers check out. The Verdict misreads the authors' parity claim, the state-of-the-art condition misses a lower figure in [4]'s own table, and several framings (single run, filters, throat microphone) go beyond the sources.

Counts by severity: major 2, moderate 5, minor 12.
