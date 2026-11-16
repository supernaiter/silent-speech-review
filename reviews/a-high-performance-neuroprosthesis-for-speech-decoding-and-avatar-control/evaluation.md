# Independent evaluation: A high-performance neuroprosthesis for speech decoding and avatar control (Metzger et al., Nature 2023)

Date: 2026-11-16. Single pass by an evaluator separate from the writer, over the compact review and its claim table; no sources were re-opened. Statements below that rely on the evaluator's own knowledge of the literature are marked "(evaluator knowledge)".

## Claim check

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | 253-electrode HD-ECoG; CTC RNN decoders; text, voice and avatar outputs | Claim table 1 | correct | Quotes support all three. |
| 2 | Text result trails [1], which reached a similar error on a vocabulary about 120 times larger | Claim table 2 | correct, but overstated | 125,000 / 1,024 = 122. 25.5% vs 23.8% with a 99% CI of [19.3, 34.5] does not show the paper "trails"; the paper is also faster (78.3 vs about 62 WPM in [1], evaluator knowledge). |
| 3 | Listeners got 54.4% of words wrong on the 1,024-word set | Claim table 3 | correct | Selective: 8.2% and 28.2% on the two smaller sets go unmentioned. |
| 4 | Real-time avatar animated from decoded audio | Claim tables 3, 22 | correct | The authors state this themselves; the review presents it as its own finding. |
| 5 | 5-gram LM trained on the 18,284-sentence pool that holds the 249 test sentences | Claim table 12 | correct (inference) | Quotes support that the LM pool is the pre-pruning pool from which test sentences were drawn. |
| 6 | Phone error 18.5% to 29.4%, 59% relative | Claim table 14 | correct | 29.4 / 18.5 = 1.59. |
| 7 | Usual approach M05: "Of 253 studies ... 233 record ECoG" | Text vs table vs Appendix | wrong | Table and Appendix say 233 of 246; text implies 233 of 253. |
| 8 | Usual approach M07: LLM rescoring in 14 studies | Text vs Appendix row 38 | wrong | Appendix gives 152 (pattern match). |
| 9 | SOTA 2.5% WER at 125,000 words, 2024 [2] | Claim table 5 | correct | Matches the quote; [2] correctly labeled later. |
| 10 | [1] 23.8% at 125,000 words | Claim table 5 | correct | |
| 11 | "The paper's 25.5% ... matches the error at two orders of magnitude less vocabulary" | Claim table 6 | insufficient | Referent unclear: the preceding sentence lists both 2.5% and 23.8%. |
| 12 | M06 SOTA about tenfold lower error | Claim table 10 | correct arithmetic | 25.5 / 2.5 = 10.2, across vocabulary, modality, participant and LM (LLM rescoring in [2]). |
| 13 | M07 "State of the art": [4] 25.6% on 50 words, 60.5% without LM | Claim table 13 | correct numbers, wrong slot | [4] is 2021 prior work, not state of the art. |
| 14 | Anumanchipalli: listener WER 31% (25-word pool), 53% (50-word pool) | Claim table 15 | correct | |
| 15 | Wairagkar 2025: 43.75% median listener WER; 10.7 points better | Claim table 17 | correct | 54.4 - 43.75 = 10.65. |
| 16 | M08 state of the art | Evaluator knowledge | incomplete | Missing the later same-participant, same-array ECoG streaming brain-to-voice work (Littlejohn et al., Nature Neuroscience, 2025). |
| 17 | 12 workers per trial "without listener criteria" | Claim table 18 | insufficient | The quote gives 12 evaluators. Nothing quoted shows the absence of criteria. |
| 18 | Avatar test two-way, 74.3% at 50% chance | Claim table 19 | correct | |
| 19 | M12 "no seeds, chance values or variance" | Claim tables 3, 19 vs text | wrong | The review itself cites a 50% chance level, and the paper reports 99% CIs throughout. |
| 20 | Released code normalises over training and test trials | No claim-table row | insufficient | No location or quote. |
| 21 | MCD 5.21 dB inside 5.14-6.58 dB [5] | Claim table 20 | correct | |
| 22 | Personalised voice "MCDs are higher in all sets" | Claim table 21 | contradicted by the quote | The quote says "similar MCD performance". No values are given. |
| 23 | Fourfold speed claim set against 14.2 WPM and 50-word systems [4] | Claim table 23 | wrong | The fourfold claim cites the paper's refs 1, 3, 9 (prior BCIs, which include the open-vocabulary handwriting BCI, evaluator knowledge). The 14.2 WPM figure is a separate comparison with the participant's own device. |
| 24 | 9,655 vs 13,463 sentences; 256 electrodes analysed on a 253-electrode array | Claim table 24 | partly correct | The sentence counts do differ in the quotes. "256" is probably the amplifier channel count (evaluator knowledge), so calling it an inconsistency is weak. |
| 25 | Chronology labels | Reference list | wrong | The target [3] is labeled [concurrent]; [1] is not labeled in the list, though the text calls it concurrent. |

Table rows for M01 ("13 days") and M03 ("95/5 development split") have no claim-table entry, so the evidence for them is insufficient.

## Required fixes (ordered by impact)

1. **Sentence:** "M08 is the real departure but the weakest evidence ..." (Verdict), together with "Verdict: standard; one participant and one model cannot carry ahead." (M08).
   **What is wrong:** The Verdict calls M08 the real departure, but the slot verdict is `standard`, so the review contradicts itself.
   **Fix:** Either make the M08 slot verdict a non-standard verdict that the rules allow without a count-backed `ahead` (for example "different, unproven") or call M08 "the main addition" in the Verdict. The two must agree.

2. **Sentence:** "Verdict: not reported: no seeds, chance values or variance; the released code normalises over training and test trials." (M12)
   **What is wrong:** The review itself reports a 50% chance level two lines earlier, and the paper gives 99% CIs for every main metric. The claim about code normalisation has no location or quote.
   **Fix:** Write "no seeds or repeated training runs; CIs are across trials/pseudo-blocks only". Either add a file or function locator for the normalisation claim or delete it.

3. **Sentence:** "The personalised voice is not what Fig. 3 measures; its MCDs are higher in all sets (Extended Data Fig. 5)."
   **What is wrong:** The quote in the claim table says the authors observed "similar MCD performance". No values support "higher in all sets".
   **Fix:** Give the Extended Data Fig. 5 values per set, or write "the paper reports only 'similar' MCDs for the personalised voice and no intelligibility test of it".

4. **Sentence:** "The fourfold speed claim sets 78.3 WPM on 1,024 words against 14.2 WPM head tracking and 50-word systems [4] (Discussion)."
   **What is wrong:** The fourfold claim cites the paper's refs 1, 3 and 9 (earlier BCIs). These include an open-vocabulary handwriting BCI, not only 50-word systems. The 14.2 WPM device rate is a separate comparison.
   **Fix:** Name the cited baselines and their rates and vocabularies. Say that the concurrent intracortical system [1] (about 62 WPM, evaluator knowledge) is not four times slower.

5. **Sentence:** "**Usual approach:** n-gram LMs (134 studies) or LLM rescoring (14; both pattern match) ..." (M07)
   **What is wrong:** The Appendix gives "neural LLM rescoring, 152 (pattern match)". The same quantity has two values.
   **Fix:** Use one count and source in the text, the summary table and the Appendix.

6. **Sentence:** "Of 253 studies decoding speech from ECoG (pattern match, unique studies), 233 record ECoG (slot-filled) ..." (M05)
   **What is wrong:** The denominator conflicts with the table and the Appendix (233 of 246). The sentence also reads as if 20 ECoG-decoding studies do not record ECoG.
   **Fix:** Write "233 of the 246 slot-filled studies record ECoG; 253 match the pattern" and keep the table identical.

7. **Sentence:** "3. Metzger, S. L., ... [concurrent]" and "1. Willett, F. R., ..." (References)
   **What is wrong:** The target paper is labeled concurrent with itself. [1], which the text calls concurrent, carries no label.
   **Fix:** Remove the label from [3] and add [concurrent] to [1].

8. **Sentence:** "**State of the art:** Continuous intracortical synthesis (2025) at 43.75% median listener WER [6] ..." (M08)
   **What is wrong:** It omits the later streaming brain-to-voice decoder from the same group, the same participant and the same ECoG array (Littlejohn et al., Nature Neuroscience, 2025). That work is the closest like-for-like successor for M08, and it also bears on M05.
   **Fix:** Add it as [later] with its reported metric, set and value, and state whether it changes the M08 comparison.

9. **Sentence:** "M05 and M06 are standard, and the text result trails the [concurrent] intracortical system, which reached a similar error on a vocabulary about 120 times larger [1] (inference)." (Verdict)
   **What is wrong:** 25.5% (99% CI 19.3-34.5) against 23.8% does not show "trails" on error. The paper decodes faster. The 120-fold figure is arithmetic and does not need "(inference)".
   **Fix:** Write "reaches a similar WER (25.5% vs 23.8%) on a 1,024-word vocabulary against 125,000 words [1], at a higher rate", and put the hedge only on the cross-vocabulary interpretation.

10. **Sentence:** "The paper's 25.5% at 1,024 words [3] matches the error at two orders of magnitude less vocabulary (inference)." (M05)
    **What is wrong:** The referent is unclear: the preceding sentence lists both 2.5% [2] and 23.8% [1].
    **Fix:** Write "matches the 23.8% of [1] at a vocabulary two orders of magnitude smaller".

11. **Sentence:** "Verdict: standard in design; the WER understates error on sentences outside the pool (inference)." (M07)
    **What is wrong:** The section's own finding is that the LM was trained on a pool that contains the test sentences. That is not standard design, and the Verdict calls it the strongest confound.
    **Fix:** Give a verdict that reflects the leakage (for example "standard LM type; test-set overlap"), consistent with the Verdict paragraph.

12. **Sentence:** "... earlier ECoG work had 25.6% on 50 words, 60.5% without the LM [4]." (M07, State of the art)
    **What is wrong:** [4] (2021) is prior work, not state of the art.
    **Fix:** Move it to the Usual approach line or label it "prior".

13. **Sentence:** "Crowd transcription (15 of 37 studies, pattern match); the paper uses 12 workers per trial without listener criteria." (M12)
    **What is wrong:** No quote or location shows that listener criteria are absent.
    **Fix:** Cite the Methods passage that shows it or delete "without listener criteria".

14. **Sentence:** "... 256 electrodes are analysed on a 253-electrode array." and "Real-time 'avatar control' is animation from decoded audio; neural-to-gesture decoding was offline (Fig. 4)." (Where the claims outrun the evidence)
    **What is wrong:** The figure of 256 is most likely the recording channel count, not a contradiction. The avatar point is something the authors state themselves ("We used the acoustic approach for real-time audio-visual synthesis"), but the review presents it as its own finding.
    **Fix:** Drop the 256/253 point or note it as a possible channel count, and keep only the 9,655 vs 13,463 discrepancy as unexplained. Attribute the avatar point to the authors ("as the authors state") and keep the critique to the gap between the title's "avatar control" and this design.

## Scores

- Procedure: 6/10. Most numbers trace to quotes, and the chronology for [2] and [6] is handled. However, several table and Appendix counts disagree with the text, a few positions have no quote, and a same-participant successor is missing.
- Final text: 6/10. The positions are clear and the LM-leakage confound is well identified. There are internal contradictions (M08 departure vs standard, M12 chance/variance, M07 counts) and two overstatements (personalised voice, fourfold speed).

The review correctly isolates the language model trained on the test-sentence pool as the main confound, and correctly separates the real-time avatar path from neural-to-gesture decoding.
