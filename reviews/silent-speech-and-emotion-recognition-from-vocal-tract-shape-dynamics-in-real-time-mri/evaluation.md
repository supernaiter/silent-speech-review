# Evaluator: a language model separate from the writer

Date: 2026-11-24. Inputs: `wiki-context/skill-draft/references/evaluator-brief.md` and `compact.md` (review, references, claim table). Target statements were spot-checked by grep against `prep/select/target.txt` (the extracted target claims), as step 1 of the brief allows. No comparator source was opened; outside knowledge I cannot locate is marked "unverified". SKILL.md was not read. The M12 rule is checked against the caller's statement of it: at least three earlier comparable papers in the same setting, the best one read and named, and a judgment on protocol, not results.

## Claim checks

| No | Claim (section) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target holds out 2 speakers (920 videos) and trains on 8 (3,680) (M12) | claim rows 15–17; target.txt l.6–7 | correct | 3,680/8 = 460 and 920/2 = 460; the arithmetic holds. |
| 2 | 40.6% PER with LM (Verdict) | claim row 4; target.txt l.23 | correct | |
| 3 | "First study" sentence claim in the Abstract (M08) | claim row 14; target.txt l.1 | correct | |
| 4 | LM is both a "5-gram" and a 4×1,024 LSTM (outrun) | claim row 30; target.txt l.38 | correct | Internal contradiction in the target, quoted. |
| 5 | Saha et al. used a different database, not "the same dataset" (outrun) | claim row 31; target.txt l.30 | correct | The target says "same dataset" in §2, and its own Table 2 labels Saha's row "Vocal Tract Morphology MRI", so the target contradicts itself. The review could say so: that is stronger than relying on [9] alone. |
| 6 | Fig. 3 labels letters as phonemes (outrun) | claim row 29 | insufficient quote | No quote or locator for Fig. 3 is given. |
| 7 | Audible speech; no emotion classifier (Verdict, outrun) | claim rows 5, 27 | correct | |
| 8 | Katsamanis: 30 classes, 460 utterances, 1 speaker, 49.4%, 10 random 95/5 splits [3] | claim row 14 | correct, thin | The "shape LDA 49.4%" quote does not show that this is the reported best or headline configuration. |
| 9 | [4] used 9-fold CV; [5] used leave-one-subject-out repeated ten times | claim row 19 | correct as quoted | See Finding 2: comparability is the issue, not the numbers. |
| 10 | Csapó held out 10 test sentences per speaker [6] | claim row 20 | insufficient quote | The quote gives 430 train and 20 validation sentences. The 10 test sentences are implied (460 − 450), not quoted. |
| 11 | Otani: 43/4/4 speakers; dWER 8.2–23.5%; read speech 4.5–11.1% [8] | claim rows 13, 18 | correct | |
| 12 | Tongue2Speech: 15.93% WER "on one TaL1 speaker" [7] | claim row 8 | insufficient quote | The quote supports 15.93% only. "One TaL1 speaker" and the fact that the WER is ASR on synthesized speech are not shown. |
| 13 | Table 2 compares against converted classifier accuracies; the caption concedes the tasks differ | claim row 21; target.txt l.29–33 | correct | |
| 14 | Lee et al. 2006: one speaker, five productions, "preliminary" [10] | claim row 25 | correct | |
| 15 | Table 3: 1.00 against 0.91 (M05) | claim row 26 | correct | The two quoted rows are Angry 1.00 and Angry 0.91, as stated. |

## Findings (ordered by impact)

1. **The M12 "behind" verdict only partly meets the rule. The three comparators are not in the target's setting.** The verdict names three earlier works that repeated their evaluation: [3] (2011), [4] (2014) and [5] (2019). All are earlier and all were read in full (Appendix). The judgment is on protocol (repetition), not on results, so that part of the rule is met. But only [3] is a sequence recognizer on continuous rtMRI speech. [4] is voice-activity detection: a detector, not a decoder, even though the review files it under "Earlier MRI decoders". [5] classifies sustained phonemes from static MR images (target.txt l.31). Strictly, the review has one comparable paper in the same setting, not three. Required fix: either name two more earlier rtMRI recognizers or decoders with repeated or cross-validated protocols (the Appendix tally of 11 should contain candidates), or narrow the sentence to say that [4] and [5] are different tasks that only show that repetition was feasible with MRI data.

2. **The "best comparable work [3]" is not clearly better on protocol overall, and the review does not weigh the trade-off.** [3] uses one speaker with random 95/5 splits of 460 unique utterances. That design is speaker-dependent but sentence-disjoint by construction. The target tests on two unseen speakers, which the Appendix counts in only 10 of 88 studies. That is stronger than [3] on the speaker axis, though its sentences very likely overlap with training (the review's own confound). "Behind on repetition" is defensible. The M12 text should still state that the target is ahead of [3] on speaker independence and behind on repetition and sentence-disjointness. As written, a reader infers that [3]'s protocol dominates.

3. **The M12 state-of-the-art work appears to use a single split as well.** Otani et al. [8] report one 43/4/4 speaker split, and the quotes show no repeats. If that is right, the best current rtMRI work does not repeat either, which weakens repetition as the axis that decides "behind". The review should state whether [8] repeats. If it does not, it should say that the verdict rests on the earlier work ([3]), not on the current state of the art. (Repeats in [8] are unverified from the quotes given.)

4. **The M12 "usual approach" cell names a minority practice.** The table row reads "Repeated splits (pattern match 11)", but the Appendix gives 11 of 88. The usual protocol is then a single, non-repeated split, which is what the target does. Required fix: describe the usual approach as a single split, and give repeated splits (11) as the stronger minority that the "behind" verdict is measured against. The same weakness, milder, appears in M08: a descriptive report in 16 of 75 is called the usual approach.

5. **M08 is called "standard" while also "unique among 88".** The Verdict says "Both are standard", then calls the text output unique and new ("the step to words is new"). If the ahead rule is unmet, say that the verdict is standard because the ahead criteria fail (one split, no repeats), not because the design is common. As written, the sentence reads as a contradiction.

6. **The M06 state of the art does not cover lip reading.** The M06 ledger pattern includes "lip or face camera" video (Appendix). The state of the art given is an ultrasound-to-speech synthesis system on one speaker [7]. For articulator-video decoding to text, large-vocabulary visual speech recognition on LRS3 (for example Auto-AVSR, 2023, about 19% WER, with later work lower) is a stronger and more direct state of the art (unverified values). Required fix: either restrict the M06 pattern to non-lip articulators or name the lip-reading state of the art.

7. **Insufficient quotes for three statements:** Fig. 3 "labels letters as phonemes" (no quote), Csapó's "10 test sentences" (only 430/20 quoted), and Tongue2Speech "on one TaL1 speaker" and "WER" (WER of ASR on synthesized speech, which is not stated). Add the quotes or soften the wording.

8. **"Kim et al. (2014)" has no reference entry.** M05 cites it as the source of the NEDM method with no number in the reference list. Add it or cite it as "[target ref 10]".

9. **The M12 table cell for this paper, "One speaker split", is ambiguous.** It reads as "one speaker". Use "One 8/2 speaker-disjoint split, no repeats".

10. **Fairness check passed.** [7] and [8] are labelled [later] and used only as state of the art, never as prior work or as missed citations. Katsamanis 2011 was available to the authors, so the omission is fair to raise, and the review correctly concedes that the step to words is new. The weaknesses the authors state themselves (the Table 2 caption on task mismatch) are credited to them, not presented as the review's own finding.

11. **Strongest confound handled.** The review names the closed 460-sentence list and the speaker-transfer reading, and marks it as inference. It also adds possible LM leakage. That is adequate. One point to add: the LM ablation (44.1% to 40.6% PER, target.txt l.20/23) gives a small gain, and with a shared sentence list that gain may itself come from leakage.

## Scores

- Procedure: 7/10. The comparators were read and quoted, the target claims check out, and the chronology is clean. The M12 comparator set is not in the target's setting.
- Final text: 7/10. The positions are clear and mostly cited. M12 overstates how comparable its comparators are and mislabels the usual approach.
