# Evaluation: Intelligible Lip-to-Speech Synthesis with Speech Units (review)

Date: 2026-11-18. Independent evaluator, single pass, review and claim table only (no sources re-read, no web).

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | 200 HuBERT units beside mel, fed to vocoder | Row 1 (t1, t3, t7) | correct | |
| 2 | LRS3 WER 72.5 to 50.7 with units; vocoder and augmentation move 0.3 and 0.2 | Row 2 (Table 3) | correct | 50.7→50.4→50.2 |
| 3 | AV-HuBERT step 41% relative, larger than units 30% | Row 3 (t54, t78, t82, t91) | wrong as worded | Relative values correct (20.4/50.2 = 40.6%, 21.8/72.5 = 30.1%), but in absolute points the AV-HuBERT step (20.4) is smaller than the unit step (21.8). "Larger" holds only relatively, from a lower base. |
| 4 | No unit ablation on the AV-HuBERT encoder | Row 3 | correct (absence, inference) | Row 3 has no location |
| 5 | ReVISE "already" predicts HuBERT units from AV-HuBERT | Row 4 (r3) | insufficient evidence / fairness | Quote r3 is a fragment; "already" implies priority for a work labelled [concurrent] |
| 6 | V2SFlow 1.3 points lower "under the same scorer" | Row 4, 9 (s1, s2) | insufficient evidence | s1 shows 29.8 in V2SFlow's table; nothing quoted shows V2SFlow re-scored with the target's ASR model rather than copying the number |
| 7 | V2SFlow listeners rate target 2.46 naturalness vs 4.40 in paper's own test | Row 4, 21 (s4, s11, t107, t29) | insufficient evidence / misleading | Column header of s4 not quoted; t29 states the paper's own MOS used the earlier visual encoder, not AV-HuBERT, so the two ratings may be of different variants |
| 8 | Speaker embedding from unstated speech (Sec. 2.2) | Row 5 (t21) | correct | |
| 9 | M02 usual approach: 53 of 54 name units, 36 name mel; "units beside mel is the common form" | Row 6, 27 (Appendix) | position beyond evidence | Co-mention in a pattern match does not show joint unit+mel targets; the 54 were selected by naming SSL representations, so 53 naming units is near-circular |
| 10 | Baseline = SVTS modified, mel only | Row 7 (t75, t78) | correct | |
| 11 | 2023 lowest LRS3 WER without text labels, 29.8%; ReVISE 33.9%, scorer 5.6% vs 2.5% | Row 8 (t54, r1, r2, t26) | numbers correct; "lowest" insufficient | Deciding 2023 priors not named (e.g. DiffV2S, ICCV 2023; RobustL2S, 2023); whether the public AV-HuBERT checkpoint used was text-fine-tuned is not settled by t33 |
| 12 | V2SFlow 28.5%, 4% relative lower | Row 9 (s2) | correct | 1.3/29.8 = 4.4% |
| 13 | Units cut WER 21.8 points, 30% relative | Row 10 | correct | |
| 14 | EMG: 10 seeds, units 26.55% vs mel 25.14%, spread about 1% | Row 11 (e1, e2, e5) | insufficient evidence | Quotes give the two values but not which is units and which is mel, nor "10 seeds"; the transfer to LRS3 lip-to-speech is unmarked inference |
| 15 | M06 usual approach: 49 neural, 41 parametric, 16 Griffin-Lim of 165 | Row 12, 32 (Appendix) | correct (ledger) | |
| 16 | Vocoder on blurred, noised mel; units + speaker embedding | Row 13 (t3, t12, t18) | correct | |
| 17 | V2SFlow UTMOS 3.624 vs 2.657, 36% higher | Row 14 (s1, s2) | correct | 3.624/2.657 = 1.364 |
| 18 | LipVoicer 21.4%, 86.2% without guidance | Row 15 (l1, l2) | correct | |
| 19 | LipVoicer scorer 1.0% on real audio | Row 15 | no quote | l5 gives lip-reader WER (14.6%, 19.1%), not the scorer on real audio |
| 20 | Vocoder 50.7→50.4, STOI 0.542→0.552; augmentation 50.2, STOI 0.543 | Row 16 | correct | |
| 21 | "a loss on other metrics the authors concede (Sec. 4.2)" | Row 16 (t114) | no quote | t114 is about evaluation sets, not a concession |
| 22 | Multi-Task: 50.2 vs 65.8 (LRS3), 44.8 vs 57.8 (LRS2), 24% and 22% | Row 17 | correct | 23.7%, 22.5% |
| 23 | [7] scores 57.4% under LipVoicer's scorer, 8.4 points from scorer | Row 18 (l4) | insufficient evidence | l4 says "LIP2SPEECH"; nothing quoted ties that label to [7]; the target's own comparison is under one scorer, so this does not show the claim outruns evidence |
| 24 | Modified baseline 72.5 vs published SVTS 78.0 | Row 19 | correct | |
| 25 | MOS 4.40 vs 4.98; 15 raters, 20 clips, samples from prior authors; V2SFlow 2.46 vs 4.42 (56% vs 88%) | Row 20, 21 | numbers correct; "did not replicate in the only later listener test" beyond evidence | "only" is an unsupported absence claim; variants differ (t29), so non-replication is not shown |
| 26 | V2SFlow-V keeps 28.5% WER, similarity 0.851→0.664; "voice claims do not survive" | Row 22 (s2, s7, s10) | numbers correct; conclusion unmarked inference | The A/V drop is V2SFlow's, not the target's |
| 27 | Component table verdicts M03, M07 "not reported" | Table vs t116, Row 26 | inconsistent | M03 content ("per-dataset training", t116) and M07 content ("No LM") are reported; M03 count 1,608 in table vs "11 of 22" in Appendix row 26 |

Strongest confound: encoder change (ResNet-18 to pretrained AV-HuBERT) versus unit target, and absolute versus relative change. The review handles the encoder confound but resolves the size comparison with relative change only, from a lower starting point.

Fairness: [concurrent] ReVISE and LipVoicer, and [later] V2SFlow and [5], are not treated as missed citations, except the word "already" for ReVISE (fix 4).

## Required fixes (ordered by impact)

1. Sentence: "The headline 29.8% rests on a pretrained AV-HuBERT encoder, a larger step (41% relative) than the units (30%), with no unit ablation on that encoder (inference)."
   Wrong: in absolute points the AV-HuBERT step (50.2 to 29.8, 20.4 points) is smaller than the unit step (72.5 to 50.7, 21.8 points); "larger" holds only in relative terms from a lower base.
   Fix: "The headline 29.8% rests on a pretrained AV-HuBERT encoder, a step of 20.4 points (41% relative) against 21.8 points (30%) for the units, with no unit ablation on that encoder (inference)."

2. Sentence: "...and its listeners rate the target 2.46 of 5 for naturalness against 4.40 in the paper's own test [3]."
   Wrong: the paper's MOS used the earlier visual encoder, not AV-HuBERT (Sec. 4.3, t29), so the two ratings may be of different variants; the claim table also does not show that 2.46 is the naturalness column.
   Fix: quote V2SFlow's Table II header for the column, and add "of a possibly different variant (the paper's own test used the non-AV-HuBERT encoder, Sec. 4.3)".

3. Sentence: "...the variants differ, but the claim did not replicate in the only later listener test."
   Wrong: "only later listener test" is an unsupported absence claim, and with differing variants non-replication is not shown.
   Fix: "the variants differ, so V2SFlow's test does not confirm the paper's naturalness score [3]."

4. Sentence: "The [concurrent] ReVISE already predicts HuBERT units from an AV-HuBERT encoder [2];"
   Wrong: "already" implies priority for a work the review itself labels concurrent; the authors could not be expected to build on it.
   Fix: "The [concurrent] ReVISE also predicts HuBERT units from an AV-HuBERT encoder [2];" and add a quote naming AV-HuBERT as ReVISE's encoder (r3 is a fragment).

5. Sentence: "...the [later] V2SFlow, same first author, is 1.3 points lower under the same scorer..."
   Wrong: no quote shows V2SFlow re-scored the target with the same ASR model; its 29.8 may be copied from the paper.
   Fix: quote V2SFlow's statement of its ASR scorer, or write "is 1.3 points lower in V2SFlow's table, which lists the target's 29.8% [3]".

6. Sentence: "Verdict: standard; ReVISE [concurrent] shares the design, and the gain is one run on one dataset."
   Wrong: the review states elsewhere that ReVISE predicts units alone and decodes them with a unit HiFi-GAN; it does not share the units-beside-mel design.
   Fix: "Verdict: standard; ReVISE [concurrent] shares the unit target but not the mel target, and the gain is one run on one dataset."

7. Sentence: "In silent-EMG voicing, 10 seeds show unit targets no better than mel, 26.55% against 25.14% WER, with seed spread about 1% [5] [later]; the LRS3 gain is far beyond such spread, so its direction holds for a weak encoder."
   Wrong: the quotes give two values without saying which is units and which is mel, and do not mention 10 seeds; seed spread from an EMG system does not establish run-to-run spread for LRS3 lip-to-speech, so "its direction holds" is unmarked inference.
   Fix: add the quote that labels the two rows and the seed count; rewrite the end as "if seed spread here is similar, the LRS3 gain is far beyond it (inference)."

8. Sentence: "The WER claims survive without audio; the voice claims do not."
   Wrong: the audio- versus video-embedding comparison is V2SFlow's own system, not the target; the target was never tested with a video-derived embedding.
   Fix: "If the target behaves like V2SFlow, its WER would survive a video-derived embedding and its speaker similarity would not (inference) [3]."

9. Sentence: "The [concurrent] LipVoicer reaches 21.4% LRS3 WER with lip-reader text at inference, under a scorer at 1.0% on real audio, and 86.2% without it [6]."
   Wrong: no quote supports 1.0% on real audio; l5 gives the lip reader's WER.
   Fix: add the LipVoicer passage stating the scorer's real-audio WER with its location, or delete "under a scorer at 1.0% on real audio".

10. Sentence: "...each under 1% relative WER in single runs (inference), a loss on other metrics the authors concede (Sec. 4.2)."
    Wrong: the quoted t114 is not a concession; no Sec. 4.2 quote supports it.
    Fix: add the Sec. 4.2 sentence in which the authors note the metric drop, or write "a STOI and PESQ loss (Table 3) that the authors do not discuss".

11. Sentence: "Of 54 unique studies ... 53 name units and 36 also name mel targets: units beside mel is the common form."
    Wrong: a pattern match of names does not show joint unit+mel targets in one model, and selecting on SSL representations makes 53 of 54 near-circular.
    Fix: "...53 name units and 36 also name mel targets (pattern match; co-mention, not confirmed joint targets)."

12. Sentence: "In 2023 the paper set the lowest LRS3 WER without text labels, 29.8%;"
    Wrong: the deciding 2023 comparisons besides ReVISE are not named (e.g. DiffV2S, Choi, Kim, Ro, ICCV 2023; RobustL2S, 2023, which also uses AV-HuBERT features), and t33 does not settle whether the AV-HuBERT checkpoint was fine-tuned with text.
    Fix: name the 2023 video-to-speech LRS3 results checked (with WER) and state which AV-HuBERT checkpoint was used (pretrained only or VSR-fine-tuned), or soften to "the lowest LRS3 WER among the compared systems without text labels".

13. Sentence: "The [concurrent] comparator [7] scores 57.4% on LRS3 under LipVoicer's scorer [6], 8.4 points from scorer choice (inference)."
    Wrong: l4 reads "LIP2SPEECH"; nothing quoted ties that entry to [7]. And the paper's comparison is under one scorer, so the bullet does not show how the "exceeds Multi-Task" claim outruns its evidence.
    Fix: quote LipVoicer's citation for the Lip2Speech row; then state the actual limit (e.g. single run, samples or scorer differ across papers) or move the bullet out of this section.

14. Component table rows M03 "Per-dataset training ... not reported" and M07 "No LM; speaker embedding from speech ... not reported".
    Wrong: both entries are reported in the paper (t116 "on each dataset"; no LM), so "not reported" contradicts the row; the M03 count (slot-filled 1,608) also differs from Appendix "11 of 22".
    Fix: give M03 and M07 a verdict from the allowed set that matches the content (e.g. standard), and use one M03 count consistent with the Appendix or state the scope of each.

## Scores

Procedure: 6/10. Final text: 6/10.

The arithmetic on the target's tables is accurate throughout, and the encoder confound is identified, which is the right central concern.
