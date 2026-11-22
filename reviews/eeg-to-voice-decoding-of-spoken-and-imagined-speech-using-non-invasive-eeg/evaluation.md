# Independent evaluation: EEG-to-Voice Decoding of Spoken and Imagined speech Using Non-Invasive EEG

Date: 2026-11-22. Independent evaluator, working from the compact review and its claim table only. No sources were reopened. Points marked "evaluator knowledge" come from the evaluator's own reading of the literature, not from the claim table.

## Claim check

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target removes DTW (M06, Verdict) | Claim row 1, t1 (Abstract) | correct | t1 states "without dynamic time warping (DTW) or explicit temporal alignment". |
| 2 | Target also removes the discriminator; keeps HiFi-GAN vocoder and spoken-to-imagined transfer | Claim rows 1, 5 | insufficient evidence | No quote supports removal of the adversarial loss, the HiFi-GAN vocoder or the transfer step. p3 is a NeuroTalk quote, not the target's. |
| 3 | 2 s: EEG output WER 0.4586 vs recorded-speech WER 0.6375 (Table 4) | Claim rows 3, 12, t39, t40 | correct | 0.6375 - 0.4586 = 0.1789, about 0.18. 0.1789 / 0.6375 = 28.1% relative. Arithmetic is right. On CER the same rows show EEG 0.2618 vs recorded 0.2566, so EEG does not beat the recording on CER. The review does not say this. |
| 4 | The strongest confound is reproduction of trained class templates | Verdict, M12, t17, t57 | insufficient evidence | A stronger confound is not addressed. The frozen pretrained HuBERT supplies the CTC training loss (row 5) and also scores WER (t57, t17). A generator trained against the evaluator can produce Mel frames that this ASR decodes better than natural speech, which explains EEG beating the recording without any template argument. If the same checkpoint is used for both, the review should name this first. |
| 5 | "All ten classes are in training and test" (Verdict); "every class in every split, by design" (M12) | Claim row 9, t11 | insufficient evidence | t11 supports a random 2:1:1 subject-specific split only. Neither the class count of ten nor "every class in every split, by design" is quoted. A random split makes it likely but is not a design statement. |
| 6 | Imagined CER 0.2710 (2 s) and 0.2474 (4 s) | Claim row 7, t24, t29 | correct | The values match the second column of each quote. The column labels are not in the quote. |
| 7 | 130-channel EEG | Claim row 7, t13 | insufficient evidence | No quote is given. The count is unusual and needs one. |
| 8 | At 4 s imagined WER 0.4346 is below spoken WER 0.4893 (Table 2) | Claim row 13, t30 | correct | |
| 9 | Pooled WER 0.4870 to 0.4658 at 4 s (Table 5) | Claim row 17 | insufficient evidence | t43 and t44 are not quoted. Possible internal inconsistency: the Table 2 per-mode WERs at 4 s (0.4893 spoken, 0.4346 imagined) average about 0.462, but the pooled "before" value is 0.4870. This needs unequal weighting or a different run to explain. |
| 10 | Correction gives 2.9% and 4.4% relative | Claim row 17 | correct | 0.0135 / 0.4586 = 2.94%. 0.0212 / 0.4870 = 4.35%. |
| 11 | Five Llama-3.2-1B candidates, scored by CER and perplexity | Claim row 15, t23 | insufficient evidence | t23 supports CER plus perplexity scoring. "Five" and "Llama-3.2-1B" are not quoted. |
| 12 | Imagined PCC drops from 0.7484 (2 s) to 0.5834 (4 s) | Claim row 18, t28, t33 | correct | The quotes match. The differences in participants, stimuli and loss weights (t21, t54, t18, t19) are not quoted. |
| 13 | Methods enrol 11 participants for 2 s; Table 1 reports 10 | Claim row 19, t59 | insufficient evidence | t59 supports 11. Nothing in the claim table shows that Table 1 reports 10. |
| 14 | "Comparable linguistic accuracy" has no statistical test | Where the claims outrun the evidence | insufficient evidence | This is an absence claim with no claim-table row. It is plausible from the section cited. |
| 15 | NeuroTalk used DTW | Claim row 1, p2 | correct | |
| 16 | NeuroTalk imagined CER 68.26% (Table 1) | Claim row 6, p6 | correct | |
| 17 | NeuroTalk held-out word CER 83.06%; 12 trained words; 64 channels; six participants | Claim row 6, p5, p8 | insufficient evidence | p5 supports only that an unseen word was tested. 83.06%, the trained-word count, 64 channels and six participants are not quoted. |
| 18 | NeuroTalk authors concede the model may be classifying into training classes | Claim row 11, p7 | correct | |
| 19 | Willett et al. reached 23.8% WER online on sentences not in training (2023) | Claim row 10; evaluator knowledge | correct | This is the 125,000-word vocabulary result. |
| 20 | M12 state of the art is the 23.8% WER result | Evaluator knowledge | wrong (outdated) | Later intracortical work is better: Card et al., "An accurate and rapidly calibrating speech neuroprosthesis", NEJM 2024, reports about 2.5% WER (97.5% accuracy) online with a 125,000-word vocabulary. |
| 21 | Benster et al. reached 12.2% WER on silent EMG with an LLM over an ensemble (2024) | Claim row 16; evaluator knowledge | correct | This is a prior work: March 2024, before the target in December 2025. |
| 22 | M06 usual approach: 569 EEG/MEG studies, 98 / 71 / 64 | Body vs Appendix row 23 | wrong (contradiction) | The body says 569 unique pattern-match studies. Appendix row 23 says 538. One of the two is wrong. |
| 23 | Reference 3: Nature 621, 1031-1036 | Evaluator knowledge | wrong | The volume is 620 (issue of 24 Aug 2023), pages 1031-1036. |
| 24 | Reference 2: author initials "Lee, Y., Lee, S., Kim, S., Lee, S." | Evaluator knowledge | insufficient evidence | The authors are Young-Eun Lee, Seo-Hyun Lee, Sang-Ho Kim and Seong-Whan Lee. The initials as written are ambiguous. Use Lee, Y.-E., Lee, S.-H., Kim, S.-H., Lee, S.-W. |
| 25 | Chronology and fairness | References 2-4 vs target (arXiv 2512, Dec 2025) | correct | All comparators are well before the target. No later work is treated as a prior work or as a missed citation. The NeuroTalk concession is credited to its authors. |

Usual approach lines: M06 (classification / regression / contrastive among EEG/MEG studies), M12 (random or repeated-sentence splits common, sentence-disjoint rare) and M07 (n-gram more common than LLM) are plausible as typical designs. The ledger counts are outside this check.

Absence and novelty claims: the review makes no "first" or "only" claim. "No run with DTW" and "no chance level or shuffled-EEG baseline" are absence claims about the target and are consistent with the cited sections.

Verdicts: M12 `behind` names a deciding prior (NeuroTalk's held-out word), gives a ledger count and states the effect (the GT-vs-EEG WER inversion). It follows the rules. M09 and M10 are `not applicable` and M13 is `not reported`. These are reasonable labels.

## Required fixes, ordered by impact

1. Name the evaluator-in-the-loss confound in the Verdict and in M12. The same frozen HuBERT ASR gives the CTC training loss and scores WER, so the generator is optimised for its own judge. Rank this confound above, or beside, the class-template inference. First confirm from the target that the same checkpoint is used for both.
2. Resolve the contradiction between 569 and 538 pattern-match unique studies for M06. The body and Appendix row 23 disagree.
3. Correct reference 3 to *Nature* 620, 1031-1036.
4. Update the M12 state of the art. Add the later, better intracortical result (Card et al., NEJM 2024, about 2.5% WER online, 125,000-word vocabulary), or state why 23.8% is kept as the comparator.
5. Add quotes for the load-bearing unquoted claims:
   - ten classes, and every class in every split
   - removal of the discriminator, and the HiFi-GAN vocoder
   - 130 channels
   - five Llama-3.2-1B candidates
   - Table 1 reporting 10 participants
   - the 4-s pooled WERs (t43, t44)
   - the differences in participants, stimuli and loss weights between 2 s and 4 s
   - NeuroTalk's 83.06% held-out CER, word count, 64 channels and six participants
6. State that the GT inversion holds for WER only. At 2 s the EEG CER (0.2618) is slightly worse than the recorded-speech CER (0.2566). This also qualifies the template-reproduction reading.
7. Soften "the claim of voice reconstruction from imagined speech is not supported" to match the evidence. It is shown only for trials of trained classes under a random split, with no unseen content.
8. Check the 4-s pooled "before" WER (0.4870) against the Table 2 per-mode WERs (0.4893, 0.4346, mean about 0.462). Explain the weighting, or flag it as an internal inconsistency of the target.
9. Change "is not a duration effect" to "cannot be attributed to duration". The confounds prevent attribution; they do not prove the absence of an effect.
10. Harmonise CER units in the M06 state-of-the-art paragraph. NeuroTalk is given as 68.26% and the target as 0.2710. Use one unit, for example 27.10%.
11. Claim-table rows 20-22 cite a section, "Questions for the authors", that the compact review does not contain. Add the section or drop the rows.
12. Write the NeuroTalk author initials in full (Lee, Y.-E., Lee, S.-H., Kim, S.-H., Lee, S.-W.).

## Scores

- Procedure: 6/10. Many rows quote only part of what they claim, and two numbers contradict the Appendix.
- Final text: 7/10. The position is clear and well targeted, but the main confound is incomplete and one state-of-the-art line is outdated.
