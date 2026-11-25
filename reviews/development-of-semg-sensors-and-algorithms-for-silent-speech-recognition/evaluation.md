# Evaluator: a language model separate from the writer

Date: 2026-11-25. Target: Meltzner et al., J. Neural Eng. 2018, 15(4) 046031, doi:10.1088/1741-2552/aac965.
Inputs read: evaluator-brief.md, compact.md (review plus claim table). Source passages consulted: the source-quote entries in `notes.json` in the same work folder (target t1–t80, comparators c1–c13). No web sources were opened. Outside knowledge that I could not locate is marked "unverified".

## Claim check table

| No | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | 11 sensors, 7 neck/chin and 4 face; final system MFCC + NL grammar + MLLR + HLDA + SGMM (Verdict) | t13, t14, t41 | correct | |
| 2 | 8.9% WER equals the mean of subjects 1–5 of the 2014 SGMM table; six-subject mean 11.2% (Verdict; Outrun 1) | t42–t47, c1–c3 | correct | Recomputed: target rows 1.4, 13.9, 12.9, 10.7, 5.6 average 8.9; adding subject 6 (22.4) gives 66.9/6 = 11.15. The per-task means also match: for example, special operations (5 × 7.5 + 12.7)/6 = 8.37 against 8.4 in 2014, and digits (5 × 13.8 + 26.2)/6 = 15.87 against 15.9. The 26% relative figure is right (11.2/8.9 = 1.26). |
| 3 | [2] is uncited in the target (Verdict) | t78 | correct | |
| 4 | Test sets held 154/167/115/88 words (Verdict; Outrun 2) | c5 | correct | The same quote gives 70/36/36/41 unseen words (see finding 4). |
| 5 | Grammar "built from the corpus's own sentence rules" applies to the Corpus 3 headline (Verdict) | t80 | wrong as stated | t80 describes how the grammar was built for Corpus 2. The review's own M07 section says the Corpus 3 construction is not stated (finding 2). |
| 6 | 2,047 subsets; best 8-sensor subset 10.4% WER (M05) | t39, t40 | correct | 2^11 − 1 = 2,047. |
| 7 | Hwang et al. 2026: all 70 four-channel subsets, best 47.2% WER (M05 SOTA) | claim row 6 | insufficient quote | The row carries an audit value and no source quote for 47.2% or 70. C(8,4) = 70 is consistent with an 8-channel array. |
| 8 | Sridhar et al.: 5 of 11 sensors, 80.6% against 79.6% with all 11 (M05) | c10 | insufficient quote | The quote shows only 80.6%. The figures "5 of 11" and "79.6%" come from the note's paraphrase and are not in the quoted text. |
| 9 | This group cut 11 sensors to 8 with under 0.5% loss; best four-sensor subset 15.2% WER, ranked by a monophone model (M05) | c7, c8 | correct, misattributed | [2] reports the cut from 11 to 8 by citing an earlier subset study (its ref. [26], Colby et al.). That study, not [2], is the deciding prior (finding 9). |
| 10 | "the data that chose it are not named" (M05) | t39, t66 | correct | |
| 11 | "The search identifies the best subset on the evaluated data" (M05); "mixture count and dimension were chosen on the sequences they are reported on" (M06) | t66 | stronger than the evidence | The source says only that no independent selection data are stated. It does not say the same data were used (finding 6). |
| 12 | HLDA cuts WER from 11.3% to 7.3%, 35% relative (M06) | t37 | correct | 4.0/11.3 = 35.4%. The test is the Corpus 2 phoneme task, not Corpus 3. |
| 13 | M06 usual approach: 30 HMM, 16 CTC and 9 attention of 54 | Appendix tally | not checkable | 30 + 16 + 9 = 55 > 54, which is fine if a study counts under several designs, but the M06 inclusion rule does not say so (the M07 rule does). |
| 14 | [5]: 97.17% phrase accuracy, 33 Chinese phrases, 256-channel HD-sEMG with CTC (M06 SOTA) | c12 | correct | This is classification accuracy, not WER. The table's "97.17% closed-set" should name the metric. |
| 15 | [6]: 12.2% WER on Gaddy silent EMG with LLM rescoring (M06, M07, M12 SOTA) | c11 | correct | The benchmark is a single speaker. The review says "open vocabulary" but not "single speaker". |
| 16 | 6.8% against 5.8% WER, and the authors call the sentence-construction grammar an upper bound (M07) | t31–t33 | correct | Both figures come from Corpus 2 word HMMs (MFCC, 2 mixtures). The inference "keeping nearly all of that constraint" is labelled (inference) but has no unigram or NATO WER to anchor it. |
| 17 | 8-sensor subset "two sensors on one side of the face" against the 2014 layout of 4 face + 4 neck (Outrun 3) | t79, c13 | insufficient reasoning | t79 is the authors' conclusion about an adequate future configuration (2 sensors × 4 detection points), not necessarily a description of the best Fig. 6 subset. The review does not state the contradiction it implies (finding 5). |
| 18 | No test partition for Corpus 2 or 3; no validation set stated (Outrun 4) | t63, t64, t66 | correct for the target | [2] does state a protocol for the same data (c4), and the review leaves that out (finding 3). |
| 19 | Six subjects in Corpus 3, five in Table 2 (Questions) | t23, t42 | correct | |
| 20 | Usual approach M12: "sentence-disjoint or open-vocabulary test", 13 of 64 | Appendix tally | wrong label | 13 of 64 is a minority, so it is not the usual approach (finding 7). |
| 21 | Usual approach M05: search over trained models, 10 of 42 | Appendix tally | weak label | 10 of 42 is a minority. The review does not say what the other 32 do (finding 7). |
| 22 | Chronology: [3], [5] and [6] are labelled [later]; [2] and [4] are prior | refs | correct | No later work is treated as prior work. |
| 23 | Bibliographic entries [1]–[6] | outside knowledge | unverified | Titles, venues and arXiv ids look plausible. The page range 1164–1168 for [2] and the volume and pages for [5] were not checked. |

## Findings (required fixes, ordered by impact)

1. **The authors' own exclusion caveat is missed, and the Verdict is too strong.** The target reports that three of 19 participants were excluded as non-compliant because of noisy or weak sEMG (t11, Methods, Protocol). The corpus counts 9 + 4 + 6 add up to exactly 19, so the drop from six Corpus 3 subjects to five in Table 2 may be one of those exclusions. The review's arithmetic is right (row 2), but "The headline does not hold as stated" presents an undisclosed or unexplained exclusion as a refutation. Fix: say that 8.9% is the five-subject mean of the 2014 rows, that the six-subject mean is 11.2% [2], and that the target's exclusion statement (t11) does not identify the dropped subject. The question to the authors can stay.

2. **The review contradicts itself on the Corpus 3 grammar.** The Verdict says the test sets were decoded "under a grammar built from the corpus's own sentence rules (Fig. 3)". The M07 section says "How it was built for Corpus 3 is not stated", and t80 and Fig. 3 concern Corpus 2 only. The M07 opening line and the components-table row ("NL-class grammar from corpus rules") carry the same overreach. Fix: limit the construction claim to Corpus 2 and mark Corpus 3 as unstated everywhere.

3. **The review leaves out the 2014 protocol it holds, which makes M12 look worse than the evidence.** c4 states that in [2] each task set was tested with models trained on the other three task sets plus TIMIT, with half of the common phrases and text messages reserved for validation. Because Table 2 reproduces those rows, the headline is most likely a task-disjoint test with a validation set: close to the "sentence-disjoint" design the review counts as the usual approach for M12. "No test partition is reported" is true of the target, but the Verdict's "rests on unmatched protocols" and the M12 `not reported` verdict should say that [2] documents a held-out-task protocol for the same numbers. The second question ("is it the 2014 leave-one-task-out scheme?") shows the reviewer knew this.

4. **The review asks about unseen words although its own source answers.** Outrun 2 says "no unseen-word count supports the 'previously unseen words' claim", and the last question asks "how many test words per set were unseen?". c5, the passage cited for the vocabularies, gives 70, 36, 36 and 41 unseen words per set [2]. Fix: say the target reports no unseen-word count, and that [2] reports 70/36/36/41 for the same task sets.

5. **A sensor-configuration inconsistency in the target is missed, and the one stated is unclear.** (a) Fig. 6 gives the best 8-sensor subset at 10.4% WER, while Table 2 gives the final 8-sensor system at 8.9%. The review never reconciles the two or asks which data and decoder layers each used. (b) [2] recorded the Table 2 data with 8 sensors (4 face, 4 neck; c6, c13). An exhaustive 11-sensor search (2,047 subsets) therefore cannot have run on those recordings, so the subset search and the headline come from different data. Outrun 3 hints at this, but t79 reads as a future-hardware recommendation, not as a description of the subset. Fix: state the contradiction explicitly as (a) and (b), and drop the "one side of the face" reading unless Fig. 6 supports it.

6. **Data reuse is stated as a fact where the source says only "not stated".** "The search identifies the best subset on the evaluated data" (M05) and "mixture count and dimension were chosen on the sequences they are reported on" (M06) go beyond t66, which records only that no independent selection data are described. Fix: "no separate selection data are stated (Fig. 4, Fig. 6)".

7. **Two "usual approach" labels are minorities of their own counts.** In M12, 13 of 64 is not the usual design. Most of the ledger presumably does not use a sentence-disjoint test, and the usual approach is whatever the other 51 do. In M05, 10 of 42 picking the subset by search over trained models is also a minority, and the other 32 are not described. Since the M05 `standard` verdict leans on this line, give the majority design and its count, or reword as "one established design (10 of 42)".

8. **Two comparator numbers have no supporting quote.** Hwang et al. 2026 (47.2% WER, 70 subsets; claim row 6) has only an audit value. Sridhar et al. "5 of 11" and "79.6%" (claim row 7) appear only in the note's paraphrase, not in the quote. Add the source quotes and locations, or drop the numbers.

9. **The deciding prior for the cut from 11 to 8 sensors is cited second-hand.** The under-0.5% loss result comes from the earlier subset study that [2] cites (Colby et al., its ref. [26]), not from [2]. Name that study directly as the deciding prior for M05. Its year and venue are unverified here, so locate them before citing.

10. **The SOTA metrics and conditions are mixed.** The "[5] (2023): 97.17% closed-set" table cell should say "phrase classification accuracy" (it is not WER, and the CER was 3.11%). [6] (12.2% WER) is a single-speaker benchmark and gets most of its gain from LLM rescoring. It is used as the state of the art for M06, M07 and M12 alike, so for M06 (the decoder) say that the gain comes from rescoring, an M07 effect. "Single speaker" should appear wherever 8.9% is set against 12.2%.

11. **The M07 inference has no anchor.** "Keeping nearly all of that constraint" depends on how much an unconstrained grammar would cost, and the review does not report the unigram or NATO grammar WERs. Without them, a one-point gap could also mean that grammar restrictiveness matters little on this task. Either give the Fig. 3 unigram value or drop the clause.

12. **The M07 verdict `standard` sits with a minority design.** The paper's rule grammar is one of only 4 of 64 studies in the ledger. `standard` can still be right, since grammar-constrained decoding predates 2018, but the line should say so ("established but rare; the field moved to n-gram and neural LMs") and not imply the paper follows the usual approach.

13. **Minor points.** In the M06 tally, 30 + 16 + 9 = 55 against 54 studies needs the "counts under every design" rule, as M07 states it. In the first Verdict sentence, "changes an 11-site ... array" reads as a slip for "combines" or "uses".

## State of the art, possible better or later work (unverified, for the writer to check)

- M06 and M12, open-vocabulary silent EMG-to-text: later work after Benster et al. 2024 on the Gaddy benchmark may report WER below 12.2%. I cannot name a value with confidence. Check the 2025–2026 entries in the ledger.
- M05: Gaddy and Klein (2020 and 2021) report electrode-ablation results on the 8-channel array for EMG-to-speech. These would be earlier than Hwang 2026 on the same task (unverified locator).

## Scores

- Procedure: 7/10. The central arithmetic was recomputed and is right. The claim table covers most numbers. Two comparator rows lack quotes, and the review did not use its own protocol and unseen-word data from [2].
- Final text: 6/10. The central finding (the 2014 rows reused, one subject dropped, no citation) is well supported and important. Its overstatement, the Corpus 3 grammar contradiction, the missed exclusion caveat and the minority "usual approach" labels need fixing.

The review's strongest contribution is that it recomputed the Table 2 means against the 2014 Table 6 and caught the uncited prior. That check holds up.
