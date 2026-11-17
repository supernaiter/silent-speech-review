# Independent evaluation: Neuroprosthesis for Decoding Speech in a Paralyzed Person with Anarthria (Moses et al., NEJM 2021)

Date: 2026-11-17. Independent evaluator, single pass over the compact review and its claim table. Sources were not re-opened; checks use the claim-table quotes plus the evaluator's own knowledge of the literature.

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Main result 25.6% median WER, 50 words, one participant | Claim table rows 1, 2 (Abstract; Results) | correct | Matches the paper. |
| 2 | 60.5% WER without LM, 25.6% with LM | Row 2 (Results, Sentence decoding) | correct | 34.9-point drop; the paper rounds to 35. |
| 3 | LM trained only on sentences built from the 50 words | Row 2, 15 (Methods, Modeling) | correct | Quote supports it. |
| 4 | Chance 92.1% WER, "sampled from that model" | Row 15 | insufficient evidence | The quote gives 92.1% but says nothing about how chance was generated. |
| 5 | "Without daily or weekly recalibration" rests on post hoc offline isolated-word analysis | Row 17 | correct | Quotes t32, t19 and t39 support it. Weeks 79–81 is not in a quote. |
| 6 | Head-movement typing baseline at 5 correct words/min | Row 20 | correct | |
| 7 | "Usable at WER below 30%" is uncited | Row 19 | insufficient evidence | The quote stops before any citation marker, so the table cannot show the sentence is uncited. |
| 8 | 22 h over 48 sessions, 128 electrodes, 81 weeks | Rows 3, 13 | correct | |
| 9 | [1] 99.6% on 50 words after 30 min of data, 2024 | Rows 3, 5 | correct | Matches Card et al. 2024. |
| 10 | [1] 2.5% WER at 125,000 words | Row 9 | correct | Card et al. report 97.5% accuracy, i.e. 2.5% WER. |
| 11 | [1] participant asked for recalibration three times | Row 18 | correct | |
| 12 | [4] 25.5% median WER at 1,024 words, 253-channel ECoG, 2023 | Rows 9, 14 | correct | |
| 13 | [3] 61% produced-utterance accuracy, chance 7%, three epilepsy patients | Row 6 | partly correct | 61% and three patients are quoted. Chance 7% is not in any quote. |
| 14 | [5] WER as low as 3% on about 250 words | Row 10 | correct but incomplete | The quote says "held-out repeat set", meaning repeats of training sentences. The review leaves out this condition. |
| 15 | 58% relative LM gain | Row 11 | correct | (60.5 − 25.6) / 60.5 = 57.7%. This is arithmetic, not inference. |
| 16 | About 44 times less data | Row 7 | correct | 22 h / 0.5 h = 44. |
| 17 | 1,024 words is about 20 times 50 words | Row 9 | correct | |
| 18 | M06 usual approach: model family "other" (82 of 355) | Row 4, Appendix | correct as a tally, not informative | "Other" does not describe a design. |
| 19 | M07 usual approach: large-vocabulary LLM rescoring (152 of 1,162) | Row 8, Appendix | wrong as framing | 152 of 1,162 is about 13%, which is not "usual". Most of that work is also later than 2021. |
| 20 | Each component "standard" vs Verdict "the advance is the population" | Verdict vs component table | contradiction | M04 (usual: speaking participants) and M13 (usual: acute recordings) differ from the paper but are marked standard. |
| 21 | M07 verdict "standard" | M07 section | contradiction | The section says the usual design is large-vocabulary rescoring and the paper uses a 50-word closed LM. |
| 22 | Ref [2] labelled [concurrent] | Reference list | wrong | [2] is the target paper itself. |
| 23 | "Decoder is far behind" today | Verdict | overreach | The comparison mixes sensor type (intracortical vs ECoG), participant and decoding unit (phonemes vs whole words). |
| 24 | Chronology of [1], [4] as [later] | References | correct | Both are later than the target and are not treated as prior work. |

Stronger or more recent work: within ECoG, [4] is a reasonable state of the art. For intracortical decoding, Willett et al. (Nature 2023) reported 9.1% WER on 50 words and 23.8% on 125,000 words. [1] supersedes it, so the stated state of the art stands.

## Required fixes (ordered by impact)

1. **Sentences:** "each component is standard for 2021 ECoG work, and the advance is the population, not the decoder." and the table rows "M04 Use-time action … Overt speech by speaking participants … standard" and "M13 Device and cost … Acute clinical recordings … standard", together with "The chronic implant is the departure; … Verdict: standard."
   **What is wrong:** These contradict each other. The review says the advance is the population and the chronic implant, and its own usual-approach column for M04 and M13 (and the M05 text) shows the paper departs from it. Yet every one of these slots is marked standard.
   **Fix:** Give M04 and M13 (and M05 if the chronic implant is kept as "the departure") a non-standard verdict that follows the verdict rules: ledger count in the Appendix, the deciding priors named, and the effect repeated. Otherwise remove the claim that these slots are where the paper departs.

2. **Sentence:** "Verdict: standard; generalisation beyond the 50 words is untested." (M07)
   **What is wrong:** The same section says the usual design is large-vocabulary rescoring and the paper uses an LM restricted to 50 words. The Verdict calls this the "strongest overreach". Marking it standard contradicts all three statements.
   **Fix:** Give M07 a verdict that reflects the departure (for example, behind or narrower than usual), with the Appendix count and the deciding prior. Alternatively, restate the usual approach for 2021 so that "standard" follows from it.

3. **Sentence:** "Of 1,162 studies naming a vocabulary or language model at use time (pattern match, unique studies), the usual design is large-vocabulary neural or LLM rescoring (152, pattern match)"
   **What is wrong:** 152 of 1,162 (about 13%) is a plurality at most, not "the usual design". LLM rescoring is also largely later than 2021, so it misstates what was usual when the paper was written. The Appendix has only 119 slot-filled studies for this slot.
   **Fix:** Report it as a share ("the largest named group, 152 of 1,162, pattern match"). Drop "LLM" or mark it as later practice. State that the slot is sparse (119 slot-filled).

4. **Sentence:** "The deciding prior, an ECoG encoder-decoder in speaking participants, reported WERs as low as 3% on a set of about 250 words [5]."
   **What is wrong:** The quote in the claim table says the 3% is on a "held-out repeat set", meaning repeats of sentences seen in training. That condition is more closed-world than the target's. Leaving it out makes the prior look stronger, and the next sentence's criticism of "test sentences drawn from the model's own word set" applies to [5] even more.
   **Fix:** Add the condition ("on held-out repeats of training sentences"). Reword the comparison so it does not imply that [5] avoided the closed-set problem.

5. **Sentence:** "Against today the decoder is far behind: 99.6% accuracy on 50 words after 30 minutes of data [1] ([later]), where this paper used 22 hours."
   **What is wrong:** The strongest confound is not handled here. [1] uses intracortical arrays, a participant with dysarthria rather than anarthria, and phoneme-level decoding. The gap cannot be attributed to "the decoder". The 22 hours is all recorded data, not the training set for the sentence decoder alone.
   **Fix:** Say "the system" instead of "the decoder". Name the sensor and participant differences in the sentence, as the M06 section partly does. Describe 22 h as total recorded data.

6. **Sentence:** "the most frequent ledger model family is "other" (82 of 355, slot-filled), then CNNs (35) and HMMs (25)"
   **What is wrong:** "Other" is a residual category and says nothing about the usual design. The sentence also mixes the 360 pattern-match base with the 355 slot-filled base.
   **Fix:** Lead with the most frequent named family (CNN, 35 of 355, slot-filled), note that most records are uncategorised, and use one base consistently.

7. **Reference:** "2. Moses, D. A., Metzger, S. L., … "Neuroprosthesis for decoding speech in a paralyzed person with anarthria." … [concurrent]"
   **What is wrong:** This is the target paper. It is not concurrent work.
   **Fix:** Remove the [concurrent] label. Better, do not cite the target as a numbered reference and refer to it as "the paper".

8. **Sentences:** "The prior design reached 61% produced-utterance accuracy (chance 7%) …" and "with chance itself sampled from that model (92.1% WER; § Methods, Modeling)".
   **What is wrong:** No claim-table quote supports "chance 7%" or the statement that chance was sampled from the language model.
   **Fix:** Add the source quotes and locations for both. If they cannot be found, drop "chance 7%" and "sampled from that model" (and "LM-sampled chance" in the M12 row).

9. **Sentence:** "Usability: "usable at word error rates below 30%" is uncited (§ Discussion)"
   **What is wrong:** The claim-table quote stops before the end of the sentence, so it does not show whether a citation marker follows. Calling the threshold uncited needs that check.
   **Fix:** Check the full sentence in the paper. If it carries a citation, replace "uncited" with a comment on the cited source. If it does not, quote the full sentence in the claim table.

10. **Sentence:** "The paper's gain from its language model (a 58% relative reduction, inference) is measured on a vocabulary five times smaller than that (inference)"
    **What is wrong:** Both values are plain arithmetic from quoted numbers ((60.5 − 25.6) / 60.5 = 57.7%; 250 / 50 = 5). Labelling them "inference" hedges where the evidence allows a plain statement.
    **Fix:** Remove both "(inference)" labels. Keep "inference" only for comparisons across studies, such as "44 times less data".

## Scores

- Procedure: 7/10. Most comparator numbers trace to quotes, and the chronology labels are correct. However, several claims have no quote (chance values, uncited), and the verdict rules are not applied to the slots the review itself names as departures.
- Final text: 6/10. The position is clear and well argued on the closed-world language model. It is weakened by contradictions between the verdict labels and the text, an anachronistic "usual approach" for M07, and a decoder-vs-system confound in the headline comparison.

The central critique (the LM gain measures a closed-world prior; the stability claim rests on a post hoc offline analysis) is well supported by the quoted passages.
