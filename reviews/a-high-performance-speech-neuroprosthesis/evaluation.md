# Evaluation: A high-performance speech neuroprosthesis (Willett et al., Nature 2023)

Date: 2026-11-16. Independent evaluator, one pass over the compact review and its claim table. No sources were reopened; where outside knowledge is used it is marked with a confidence level.

## Claim check

| # | Claim (section, first words) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Verdict, "The paper [1] changed three components" (6v arrays, 5-layer GRU, 125,000-word trigram) | Claim table row 1 | correct | Quotes support all three. |
| 2 | Verdict, "All three are standard against today's ledger because the field adopted them" | Rows 2, 6, 29; verdict logic | wrong (procedure) | The paper is judged against later adoption, not against the field at publication. This contradicts "was new for attempted speech" and "the real advance of 2023". |
| 3 | Verdict, "23.8% online WER at 62 words per minute ... new for attempted speech" | Row 3 | correct | Quotes match. Deciding priors [4] (50 words) and [5] (about 250 words, overt speech) are named elsewhere. |
| 4 | Verdict, "Crediting spiking resolution for the gain is overreach, since a [concurrent] ECoG system reached a similar error at a higher rate [3]" | Rows 4, 10, 21 | insufficient evidence / contradiction | The quote only says the BCI "records spiking activity". It does not show the authors crediting resolution for the gain. M05 then says the vocabularies (125,000 vs 1,024) are too far apart to rank sensors, so [3] cannot carry the overreach claim. |
| 5 | Verdict, "The 2.7x and 3.4x margins are untested ratios" | Rows 5, 22 | correct | 25.6/9.1 ≈ 2.8 and 62 wpm vs about 18 wpm (90 characters/min) ≈ 3.4 are consistent with the quotes. |
| 6 | M05 usual approach, "67 of 75 ... 20 ... 2022 or earlier and 37 from 2024" | Rows 6, 28, 29 | insufficient evidence | Row 29 is truncated after "4 in ...", so the 2024 count cannot be checked here. "67 of 75 intracortical studies record microelectrodes" is close to circular. |
| 7 | M05, "Before this paper, sentence decoding from cortex was an ECoG result [4], [5]" | Row 7; [6] | wrong | The handwriting BCI [6] (2021) decoded sentences from intracortical arrays. The claim holds only for speech. [5] studied overt speech in epilepsy patients, not a BCI user. |
| 8 | M05 state of the art, "2.5% WER on 125,000 words in 2024 ... about a tenth ... 31.6 words per minute, half" | Row 8 | correct | 2.5/23.8 = 0.105 and 31.6/62 = 0.51. Confound: [2] reports its final 5 sessions after months of accumulated data and with a stronger language model. |
| 9 | M05, "dorsal 6v array cut offline WER from 32% to 21% ... factor of 0.57 per electrode doubling over ten seeds" | Row 9 | correct | Quotes match (adding the dorsal array to the ventral one; s.d. over ten RNNs). This is the authors' finding, and the review credits it to them. |
| 10 | M05, "[concurrent] 253-channel ECoG ... 25% median WER on 1,024 words at 78 words per minute" | Row 10 | correct | All three quotes match. |
| 11 | M06 usual approach, "of 97 ... 79 use CTC and 76 a recurrent network; GRU with day-specific input layers comes from [6]" | Rows 11, 33, 18 | correct | Consistent with the Appendix row and the day-specific input layer quote. |
| 12 | M06 state of the art, "the same family holds the 2024 best result [2]; the gap is data and sensors, not architecture" | Row 12 | wrong (judgment) | The quote gives only a WER. Nothing in it isolates data and sensors. The review's own M07 shows the language model alone moving WER from 23.8% to 17.4%. On the same T12 dataset, the Brain-to-Text Benchmark '24 (Willett et al., arXiv:2412.17227, Dec 2024) reports top offline entries near 5.8% WER from model ensembling and LLM rescoring (inference from memory, medium confidence). Same data and sensors, much lower WER. |
| 13 | M06, "19.7% ... 21.4% ... 23.8% and 9.1% ... the same neural evidence gives a 2.6-fold difference" | Row 13 | numbers correct, wording wrong | 23.8/9.1 = 2.6. The two conditions use different sentence sets and blocks and have different phoneme error rates, so the neural evidence is not "the same". |
| 14 | M06, "not overly reliant" vs "60.5% without, 25.6% with [4]" | Row 14 | insufficient evidence | The 60.5% figure is cut off from the quote ("without language modeling and 25.6%"). It agrees with [4] as I recall it (medium confidence). |
| 15 | M07 usual approach, "n-gram models (146) and neural rescoring (152) dominate" among 1,162 | Rows 15, 37, 38 | wrong (overstatement) | 298 of 1,162 is about a quarter, and only 119 are slot-filled. "Dominate" is not supported. |
| 16 | M07 state of the art, "2.5% WER with neural rescoring in 2024 [2]" | Row 16 | insufficient evidence | The quote gives the WER but says nothing of neural rescoring. [2] did use n-gram plus LLM rescoring (high confidence), but the claim table needs a quote and location. |
| 17 | M07, "an improved model alone cut offline WER from 23.8% to 17.4%, a 27% relative reduction ... 11.8%" | Row 17 | partly wrong | 17.4% is offline. 23.8% is the online figure. Both come from the same data with the same phoneme error rate (19.7), but the sentence calls 23.8% offline. 26.9% relative is correct. |
| 18 | M03 usual approach, daily recalibration as in [6] | Row 18 | correct | |
| 19 | M03 state of the art, "30 minutes of data on day one and accuracy held through session 84 [2]" | Row 19 | incomplete condition | The 99.6% after 30 minutes was on a 50-word vocabulary (high confidence). [2] also kept training on accumulated data afterwards, so this is not calibration-free operation. |
| 20 | M03, "260–480 sentences (Sec. 3; 260–440 in Sec. 4) ... 140 min ... 30% (Fig. 4c)" | Row 20 | correct | Quotes match. Flagging the paper's internal inconsistency is good. |
| 21 | M03/M12 verdicts, "M12 not reported"; table row M12 "Online WER, one participant ... not reported" | Table vs text | wrong | Evaluation is reported (online WER, CIs, Table 1). What is missing is seeds and selection data. That is a limitation, not an absent component. |
| 22 | Table M08 state of the art, "78 words/min [3]" | Row 10 | incomplete condition | Needs the condition (1,024 words, 25% median WER). |
| 23 | Where, "released code keeps the checkpoint with the lowest error on the partition named 'test'" | Row 23 | insufficient evidence | The quotes show testDir = 'test' and best-checkpoint saving on valOutputs. They do not show valOutputs being computed on testDir. |
| 24 | Where, "2.7x ... another participant and sensor [4]; 3.4x ... handwriting [6]" | Row 22 | correct | |
| 25 | References [1]–[6]; [2] [later], [3] [concurrent] | Reference list | correct | Bibliographic details and chronology labels look right (same Nature issue for [1] and [3]; NEJM Aug 2024 for [2]). |

**Strongest confound.** The central comparison sets 23.8% at 125,000 words against priors with different participants, sensors and vocabularies, and against [2], which has more accumulated data and a stronger language model. The review handles the vocabulary confound in M05 but then ignores it in the Verdict. It assigns the gap to [2] to "data and sensors" without evidence.

## Required fixes (ordered by impact)

1. **Sentence:** "All three are standard against today's ledger because the field adopted them, and a [later] system on the same design reached 2.5% WER on the same vocabulary [2]."
   **Problem:** The verdict uses later adoption, from work the authors could not have read, to call the paper's own components standard. That is a fairness and verdict-rule error. It also contradicts "was new for attempted speech" and "The online 125,000-word vocabulary was the real advance of 2023".
   **Fix:** Judge each component against the ledger studies dated before August 2023 (the Appendix gives 20 of 75 dated 2022 or earlier). For M07, and for M05 if supported, either apply the `ahead` rule (Appendix ledger count, deciding priors [4] and [5] named, effect repeated by [2]) or state why the component was already standard at publication. Mention [2] only as later confirmation.

2. **Sentence:** "Crediting spiking resolution for the gain is overreach, since a [concurrent] ECoG system reached a similar error at a higher rate [3]." (The same reasoning appears in "Spiking resolution as the cause (Abstract) has no within-study sensor control, and the [concurrent] ECoG result sits in the same error band [3].")
   **Problem:** This contradicts M05 ("With vocabularies two orders of magnitude apart, neither paper ranks the sensors"). [3]'s 25% is on 1,024 words, not 125,000. A median is also not directly comparable with the aggregate 23.8%.
   **Fix:** Rest the overreach claim on the missing within-study sensor or feature control. Write: "the concurrent ECoG result [3] (25% median WER on 1,024 words at 78 words per minute) is on a vocabulary about 120 times smaller and cannot settle the question either way."

3. **Sentence:** same Verdict sentence as fix 2, claim table rows 4 and 21.
   **Problem:** The supporting quote ("BCI that records spiking activity from intracortical microelectrode arrays") does not show the authors attributing the gain to spiking resolution. Without such a passage the review attacks a claim it has not shown the paper makes.
   **Fix:** Quote and locate the passage where the authors credit spiking or intracortical resolution for the improvement. If there is none, reword to "the paper implies, without testing, that intracortical recording explains the gain".

4. **Sentence:** "**State of the art:** the same family holds the 2024 best result [2]; the gap is data and sensors, not architecture."
   **Problem:** No cited evidence isolates data and sensors. The review's own M07 shows the language model alone cutting WER from 23.8% to 17.4%. [2] also used a stronger language model with LLM rescoring.
   **Fix:** Delete "the gap is data and sensors, not architecture" or replace it with: "[2] differs in participant, accumulated data and language model, so the source of the gap is not identified."

5. **Sentence:** same M06 State of the art line (and table row M06 "Same family [2]").
   **Problem:** It misses the most relevant later work for the decoding component. The Brain-to-Text Benchmark '24 on this paper's own T12 dataset (Willett et al., arXiv:2412.17227, 2024) reports top offline entries at about 5.8% WER through ensembling and LLM rescoring (medium confidence; verify the exact value). With data and sensors held fixed, it shows large gains from the decoding and language model stages.
   **Fix:** Cite it, with year, metric and value, as the state of the art for M06/M07 on the same data, marked [later].

6. **Sentence:** "the same neural evidence gives a 2.6-fold difference in word error from the vocabulary alone (inference)."
   **Problem:** The 125,000-word and 50-word conditions used different sentence sets and blocks, and their phoneme error rates differ (19.7% vs 21.4%). The neural evidence is not the same.
   **Fix:** "with similar phoneme error (19.7% vs 21.4%) on different sentence sets, word error differs 2.6-fold (23.8% vs 9.1%), which points to the vocabulary and language model (inference)."

7. **Sentence:** "Verdicts: M03 standard, M12 not reported." and table row "M12 Evaluation | Online WER, one participant | ... | not reported".
   **Problem:** Evaluation is reported (online WER with confidence intervals, Table 1). The missing items, seeds and stated selection data, are limitations of a reported component.
   **Fix:** Give M12 the verdict the rules assign to a reported component (for example standard) and list the missing seeds, the selection split and the single participant as limitations.

8. **Sentence:** "**State of the art:** in 2024, 30 minutes of data on day one and accuracy held through session 84 [2]."
   **Problem:** The condition is missing. The 99.6% after 30 minutes was on a 50-word vocabulary. [2] went on updating its decoder with accumulated data, so this is not a fixed calibration budget against this paper's daily recalibration.
   **Fix:** "in 2024, 99.6% accuracy on a 50-word vocabulary after 30 minutes of day-one data, with large-vocabulary accuracy maintained through session 84 as data accumulated [2]."

9. **Sentence:** "Before this paper, sentence decoding from cortex was an ECoG result [4], [5]."
   **Problem:** The handwriting BCI [6] (2021) decoded sentences from intracortical arrays. [5] decoded overt speech in epilepsy patients, not in a BCI user.
   **Fix:** "Before this paper, decoding sentences from speech-related cortical activity was an ECoG result: in a paralysed participant [4] and in overt speech of epilepsy patients [5]."

10. **Sentence:** "among 1,162 unique studies naming a vocabulary or language model (pattern match), n-gram models (146) and neural rescoring (152) dominate"
    **Problem:** 298 of 1,162 (about 26%) is not dominance, and only 119 studies are slot-filled.
    **Fix:** "n-gram models (146) and neural rescoring (152) are the most frequent named designs, though most matches name neither."

11. **Sentence:** "an improved model alone cut offline WER from 23.8% to 17.4%, a 27% relative reduction (inference)"
    **Problem:** 23.8% is the online WER. 17.4% is an offline replay of the same data.
    **Fix:** "an improved model alone cut WER on the same data from 23.8% (online) to 17.4% (offline replay), a 27% relative reduction (inference)."

12. **Sentence:** "**State of the art:** online 125,000-word decoding at 2.5% WER with neural rescoring in 2024 [2]."
    **Problem:** The claim-table quote supports the WER but not "with neural rescoring".
    **Fix:** Add a quote and location from [2] describing its language model (n-gram plus large-language-model rescoring), or drop "with neural rescoring".

13. **Sentence:** "The released code keeps the checkpoint with the lowest error on the partition named "test", the split behind its own offline WER (neuralSequenceDecoder.py)"
    **Problem:** The quoted lines show testDir = 'test' and best-checkpoint saving on valOutputs, but no line connects valOutputs to testDir. The leakage claim is an inference presented as fact.
    **Fix:** Quote the line that computes valOutputs from the 'test' partition, or reword to "appears to select ... (inference from lines 267 and 493)".

14. **Sentence:** table row "M08 Output | Text, 62 words/min | ... | 78 words/min [3]"
    **Problem:** The state-of-the-art rate is given without its condition, so it reads as a like-for-like improvement.
    **Fix:** "78 words/min at 25% median WER on 1,024 words [3]".

## Scores

- Procedure: 7/10. The claim table is complete and comparators are quoted. The verdict logic (later adoption as the standard), one unsupported state-of-the-art judgment and a missed same-dataset benchmark lower it.
- Final text: 6/10. Clear position, but the Verdict contradicts M05, and several conditions are missing from comparator numbers.

Strengths, briefly: arithmetic is right throughout, the paper's internal 260–480 vs 260–440 inconsistency is caught, the chronology labels are correct, and the code-level selection concern is a useful lead once it is properly sourced.
