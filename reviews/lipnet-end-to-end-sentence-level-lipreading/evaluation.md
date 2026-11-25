# Evaluator: a language model separate from the writer

Date: 2026-11-25. Target: Assael et al., "LipNet: End-to-End Sentence-level Lipreading", arXiv:1611.01599 (2016-11).
Inputs read in full: `wiki-context/skill-draft/references/evaluator-brief.md` and `compact.md` (review, references, claim table). The verdict rules and chronology rules were checked against `wiki-context/skill-draft/SKILL.md` (step 3.4, step 4, writing rules). The M04 and M06 audit files were consulted only for `read_fulltext` roles, `recall_sample` and the before-target counts. No wiki `source/` text was opened, so a quote that looks too thin is marked "insufficient quote", not "wrong".

## Claim check

| # | Claim (short) | Where checked | Result | Note |
|---|---|---|---|---|
| C1 | LipNet changes M06: STCNN + Bi-GRU + character CTC | claim row 1 (t1, Abstract) | correct | |
| C2 | "of the 67 earlier sentence-level studies 41 name HMMs and none a CTC or attention decoder" | Appendix M06; audit `pattern_counts_before_target` | wrong on chronology | The cutoff is 2016-11, so the six-month [concurrent] window is counted as "earlier". The same audit also counts `end_to_end: 2` before the cutoff, and those two studies are never named or read. See F3. |
| C3 | 86.4% is a video-only, speaker-dependent result under the GRID grammar [3] | rows 3, 18; audit M06/M12 Gergen quotes | correct | "Speaker-dependent" (90/5/5 split) and "task grammar" are both quoted. "Word HMMs" has insufficient quote. |
| C4 | 2.8× compares across task level, split and decoder constraint | rows 3, 19 | correct | 4.8% WER against 13.6% gives 2.83× (inference). The review handles this confound. |
| C5 | Panel: three hearing-impaired students, ten minutes of annotated video, 300 clips (§4.2) | rows 17, 20 (q5, t34) | insufficient quote | The quotes give "three members of the Oxford Students' Disability Community" and "10 minutes … 300 random videos". "Hearing-impaired" is not in either quote. |
| C6 | 2D convolutions instead of STCNN: 11.6% vs 4.8% overlapped, 26.7% vs 11.4% unseen (Table 2) | row 8 (t25 is the LipNet row only) | insufficient quote | Only the LipNet row is quoted. The Baseline-2D values and the "about 1.2×" from the 5-gram have no quote. |
| C7 | LRW [7] "classifies 500 clips" | row 7 (c1, c4) | wrong | LRW is a 500-word classification task with many clips per word. Read "500 word classes" (correct with the quote's location). |
| C8 | WAS reaches 3.0% GRID WER under this protocol, without CTC [8] | rows 9, 14 (l2, l3) | correct | The 255-utterances-per-speaker split is quoted. |
| C9 | M06 state of the art: LRS3 VSR 17.6% WER [6]; GRID 0.99% [2] "against 4.8% here overlapped" | rows 6, 2; M12 audit | condition mismatch | The audit records LinProVSR's split type as "not named". The comparison with the overlapped 4.8% supplies a condition that the source does not give. "Still uses a 3D front end [2]" has no quote. On LRS3, lower visual-only WERs exist with large extra training data, e.g. Chang et al. 2024 (ICASSP, "Conformers are all you need for visual speech recognition", about 12.8%). This value is unverified, so it is not a required fix, but the line should state that its comparison condition excludes such data. |
| C10 | Wand et al. [5] cut single words from GRID alignments | row 7 (w1) | correct | |
| C11 | Wand [5] "reports both" a seed and an interval | rows 4, 16 (w3, w4) | wrong as worded | The quotes show a spread across speakers (79.6% ± 4.3%) and a one-tailed t-test. Neither is a seed. |
| C12 | Florescu 2010 [4]: vocalised training data cannot be used directly; "measured in lip video since 2010" | row 12 (f1) | partly supported | The quote is correct. However, the system is ultrasound plus lip video, so "in lip video" overstates the modality. See F6. |
| C13 | Petridis 2018 [9]: 69.7% → 61.2%; silent-trained 64.4% | row 11 (p1) | insufficient quote for 64.4% | The quoted row is "Normal 69.7 66.3 61.2". The 64.4% silent-trained value is not in the quote. |
| C14 | [10]: professionals 92.9% WER without context and 86.4% with context, model 40.9%, bootstrap intervals | row 15 (v2) | insufficient quote | Only 92.9 ± 0.9 is quoted. 86.4%, 40.9% and "bootstrap" have no quote. |
| C15 | Professional reader with ten years' experience [8] | row 17 (l6, l7) | insufficient quote | The quote is not reproduced in the claim table. |
| C16 | Table 1 caption: Gergen "consider[s] only … isolated words", but its composite HMM decodes the whole sentence [3] | row 18 | correct | The authors could read [3] (they cite it), so the criticism is fair. |
| C17 | 64,000 admissible sentences | row 20 | correct, unmarked arithmetic | 4×4×4×25×10×4 = 64,000. This is the reviewer's arithmetic and needs "(inference)". |
| C18 | 4 held-out speakers of 34 (§4.1) | row 21 (t7) | correct | |
| C19 | Chronology labels: [3], [7], [8] [concurrent]; [5] prior; [2], [6], [9], [10] [later] | References; dates | correct | [5] (arXiv 2016-01) is more than six months before the target. |

## Findings (required fixes, ordered by impact)

1. **M06 `ahead` fails the repetition condition, and the review admits it.** SKILL.md step 4 requires "the effect is shown with repetition (seeds, subjects or datasets)". The section itself ends "Verdict: ahead, on one corpus and one run". The Verdict says "no Table 2 number carries a seed or an interval", and the review gives no per-speaker results. The overlapped and unseen splits of one corpus are not independent datasets. By the rule, M06 is `standard` ("the difference is not supported well enough to call"). The design's novelty can still be stated as a plain, Appendix-backed absence fact. Changing the verdict alters the Verdict's first two sentences, the table row and `slots.json`.

2. **M06 `ahead`: the deciding priors named are not prior and are not in the same setting.** The audit's `role: prior` entries for M06 are Wand 2016 [5], Chung & Zisserman LRW [7] and Gergen 2016 [3].
   - [7] and [3] are labelled [concurrent] in the review itself. By SKILL.md, a [concurrent] work does not count as prior, so it cannot be a deciding prior.
   - [5] is the only true prior, and it is a word classifier. The M06 inclusion rule excludes isolated-word classification, so [5] is outside the population that the absence claim counts.
   - None of the 41 prior sentence-level HMM studies, the closest earlier designs in the same setting (sentence-level GRID or AV decoding), was read or named.
   
   The `ahead` (or absence) claim therefore lacks a read, named prior in the same setting. Name and read at least one pre-2016-05 sentence-level visual decoder (for example a GRID sentence-level HMM system from the ledger's 41).

3. **M06 absence claim: chronology window, and two unexamined "end-to-end" hits.** The "67 earlier" studies use a 2016-11 cutoff, which counts the [concurrent] window (2016-05 to 2016-11) as earlier. State it as "first public before 2016-11", or recount with a 2016-05 cutoff, which the review already uses for the wiki-wide CTC check.
   - The same before-target count has `end_to_end: 2`, and these two studies are not named, read or excluded in the text.
   - The M06 audit has `recall_sample: null`. SKILL.md step 3.4 requires a `--fulltext-pattern` run and a reading of the recall-sample snippets whenever `ahead` or an absence is claimed. That step was not done.
   
   Until these points are resolved, "none a CTC or attention decoder" rests on a regex count alone.

4. **M06 `ahead` is argued from later results and adoption, not from protocol.** "The field took both, and the best GRID result today still uses a 3D front end [2]" is not a rule criterion, and the 3D-front-end part has no quote. The section's own evidence also cuts against the decoder slot. It locates the gain in the 3D front end (Table 2) and then says "That CTC was the decisive half is not shown", citing a [concurrent] attention model at 3.0% [8]. The CTC objective is the part that defines the decoding slot. If the measured effect belongs to the front end, the slot assignment, and with it the `ahead` claim, does not follow from the stated evidence. Note that WAS [8] also uses a 2D (VGG-style) front end and is better than LipNet on GRID. This is unverified outside knowledge, but it argues against "the gain sits there". Either assign the front-end effect where it belongs and verdict M06 on the decoder alone, or drop the adoption argument.

5. **M04 `behind` compares against a population from a different setting.** SKILL.md requires at least three earlier ledger papers meeting a condition the target does not, with the best read and named.
   - The four earlier studies are one ultrasound-plus-lip-video study [4], two surface-EMG studies and one ECoG study. Only [4] is visual. The others are different signals and tasks, not "the same setting" as sentence-level video lipreading.
   - The "usual approach" line restates the topic's own inclusion rule. "23 of 33 overt-to-silent studies apply an overt-trained decoder to silent articulation" is close to true by construction. It is not the usual use-time action for lipreading, which the review's own M01 row puts at overt speech (slot-filled 4,015).
   - Among studies in the target's task, testing on silent articulation is not typical of the field. The condition the target "does not meet" is imposed from one motivating sentence in §5.
   
   This is a protocol condition, which is the right kind, but the setting does not match. The defensible reading is `standard` for M04, with the silent-dictation remark moved to "Where the claims outrun the evidence" as an untested application claim backed by [4] and [9].

6. **M04: no yardstick is stated, the tier is mixed, and the prior count is inconsistent.** SKILL.md says to "Say whether the yardstick is 'best comparable work' or 'typical of the field'". The text says only "against the four earlier studies built to measure this gap". There are three further problems:
   - The usual-approach line cites "23 … (confirmed)", but the 13-components row says "pattern match 33".
   - The audit's `usual_approach.n_prior` is 7, while the recomputed chronology and the text give four. The Appendix should say which one is the tally.
   - "A transfer cost measured in lip video since 2010 [4]" should read "in ultrasound and lip video".

7. **Verdict overstatement about [5].** "while the study reimplemented as its LSTM baseline reports both [5]" implies a seed and an interval. [5] reports a spread across speakers and a t-test, not a seed. Rewrite it, for example: "reports a spread across speakers and a significance test".

8. **LRW "classifies 500 clips" [7] is wrong.** It classifies 500 words. This weakens the comparison it supports.

9. **M06 state-of-the-art condition.** "0.99% WER on GRID against 4.8% here overlapped" pairs the target's overlapped split with a value whose split the audit records as "not named". Either state the LinProVSR split as the source gives it, or drop "overlapped". The LRS3 17.6% line should name the condition that makes it the best value, or acknowledge large-data systems.

10. **Unquoted numbers.** Several numbers carry a claim but are not inside their quotes:
    - Baseline-2D 11.6% and 26.7% (Table 2)
    - the 5-gram's "about 1.2×" (§4.3)
    - 1.69× (§1)
    - 64.4% [9]
    - 86.4% and 40.9% and "bootstrap" [10]
    - "hearing-impaired" (§4.2)
    - "ten years' experience" [8]
    
    Each needs the full quote added to notes, or the claim removed. This is the single most frequent error class in SKILL.md, with 274 fixes.

11. **"64,000 admissible sentences" is the reviewer's arithmetic.** Mark it "(inference)".

12. **Minor: the confounds of the human comparison could be stated more plainly.** The 4.1× against humans compares a model trained on 29 speakers' data with a panel given ten minutes of video. The review says this (§4.2, "grammar-prior baseline"), and the handling is adequate. No fix is required, unless the writer wants to give the relative and absolute gap (47.7% vs 11.4% WER; inference from 4.1×, unverified here) as SKILL.md asks.

Not findings: the [concurrent] and [later] labels are correct throughout, and no [concurrent] or [later] work is treated as a missed citation. The M12 `standard` verdict is consistent with the Appendix (variability reporting in 3 of 12 studies before the target). The central confound of the 2.8× claim (task level, split, grammar) is identified and handled.

## Scores

- Procedure: 5/10. The SKILL rules for both non-standard verdicts are not met: `ahead` lacks repetition, a read prior in the same setting and a recall-sample check, and `behind` lacks a same-setting population and a yardstick.
- Final text: 7/10. The confound analysis of the headline claims is sharp and well located. The weaknesses are the verdict labels, one factual slip (LRW) and several unquoted numbers.
