# Evaluation: An instantaneous voice-synthesis neuroprosthesis (review)

Date: 2026-11-17. Independent evaluator, single pass over the review and its claim table only (no sources re-read). The claim table was filled by the writer, so a row marked "correct" means only that the writer's own quote carries the claim; it was not checked against the source.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper changed M02, M06, M08 (Verdict) | Claim table row 1 | correct | Quotes cover neural syllable boundaries, decoder changes and intonation accuracies. |
| 2 | 94.34% six-choice matching, chance near 17% | Row 2, 22 | insufficient evidence | 94.34% is quoted. No quote says there were six options, so the 1/6 chance level rests on an unquoted premise. |
| 3 | Open transcription 43.75% median WER, tagged "(inference)" | Row 2, t17 | wrong label | 43.75% is reported directly by the authors (Fig. 2l), so it is not an inference. Only the chance level is. |
| 4 | "The intelligibility claim does not [hold]" | Verdict, rows 2/22 | position stronger than evidence | The authors report open-transcription WER themselves. The review presents a caveat the authors already disclose as a failed claim. |
| 5 | Later model 5.24% WER "on the same data" | Row 3 | insufficient evidence | The quote gives 5.24% only. Nothing shows the same sentences, trials or listener protocol. |
| 6 | 88% below 43.75% | Row 7 | correct (arithmetic) | (43.75 − 5.24)/43.75 = 88.0%. But it compares closed-loop with offline simulated inference. That confound is noted in M06 but not in the Verdict. |
| 7 | Synthesis every 10 ms; "inference under 10 ms" | Row 5, 8 | partly wrong | The quote says the whole pipeline took under 10 ms ("from signal acquisition to synthesis"), not only inference. |
| 8 | Playback delay "shown only in Extended Data Fig. 1c"; 25 ms cited by the follow-up | Rows 8, 9 | insufficient evidence | The "only" is an absence claim with no support. The end-to-end latency of about 25 ms is reportedly stated by the target paper itself (inference, medium confidence), so attributing it to the follow-up may be wrong. |
| 9 | 2009 closed loop 30–70 ms / within 50 ms | Rows 6, 9 | correct | Both quotes are present. They are consistent if 50 ms is an upper bound on typical delay. |
| 10 | Angrick 2021 unintelligible imagined words; Angrick 2024 six-word vocabulary, seconds after overt speech | Row 6 | correct | Matches the quotes. The [concurrent] label for the 2024 work is reasonable. |
| 11 | M06 usual approach: 24 offline/acausal, 9 causal (pattern match) | Rows 4, 28 | contradiction | The Appendix row gives 24 as **slot-filled** ("decoding step role generate"), not pattern match. |
| 12 | M02 "Synthesis usually trains on the user's paired audio" | Rows 10, 32 | contradiction | The Appendix tally gives "other 8, paired audio 7". Paired audio is not the majority. |
| 13 | M02 boundaries "with manual review (Methods)" | Row 13 | insufficient evidence | The quote (t5) does not mention manual review. |
| 14 | "Only 3 of the 56 align targets with timing inferred from neural data" | Rows 12, 34 | insufficient evidence | The two later works are not named. The review's own Appendix gives known-item recall 0.0 for this slot, so the absence claim is weakly grounded. |
| 15 | Metzger 2023: 54.4% WER on 1,024 words | Row 15 | insufficient evidence | The quote is truncated ("54.4% (99%"). The 1,024-word condition is not in it. The number itself is consistent with the published paper. |
| 16 | Anumanchipalli 2019: 31% WER, 25-word pool | Row 15 | correct | |
| 17 | 10.65-point gain over ECoG | Row 17 | correct (arithmetic) | 54.4 − 43.75 = 10.65. The cross-participant caveat is stated. |
| 18 | "Binary decoders trigger predefined pitch profiles: intonation is classified, not synthesized" | No row | no quote | No claim-table row supports it. It also sits uneasily with the Verdict's "voice with decoded ... pitch" and with the three-level pitch (melody) task. |
| 19 | M08 usual approach "without user control of pitch" | Row 14 | no quote | The ledger tally row does not carry the pitch qualifier. |
| 20 | Contamination: 3.03% of 627 trials; stethoscope 100% WER vs 43.60% | Row 20 | partly unsupported | 3.03% and 43.60% are quoted. "627" and "100% WER" are not. The quote says only that intelligible speech "could not be synthesized". |
| 21 | Open transcription with 7 listeners "here and in the follow-up" | Row 19 | insufficient evidence | The 7-listener quote is from [2] only. Nothing quoted for the target. |
| 22 | Residual speech 96.43% vs 43.75% "on 20 residual-speech trials" | Row 23 | insufficient evidence | The WERs are quoted. "20 trials" is not. |
| 23 | Mimed r = 0.82 vs 0.83; r against TTS target | Row 21 | correct | The quotes support the values and the proxy-target point. |
| 24 | Pitch 73.02% vs 50% chance | Row 24 | correct | 189 pairs and binary higher/lower judgement. Chance of 50% is a sound inference. |
| 25 | M05 SOTA: 256 electrodes, 2.5% text WER [8] | Table | correct (from knowledge) | Card et al. 2024 report 97.5% word accuracy. No claim-table row exists for it. |
| — | M12 usual approach "15 of 79 (pattern match)" vs table "(pattern match 37)" and Appendix "37 pattern match (unique studies)" | Rows 39, 40 | contradiction | The denominator 79 exceeds the 37 unique pattern-match studies. 15/79 (19%) is also hard to call "usual". |
| — | M03 verdict "not reported" while the row describes cumulative multi-session training that matches the usual approach | Table | contradiction | The verdict should be `standard`, or the reason should be given. |

**Usual approach / state of the art.** The state-of-the-art lines rely on the same group's later work [2] (5.24% WER). It is correctly labelled [later] and not treated as prior work. Its bioRxiv identifier uses a non-10.1101 prefix. I could not verify it, and it should be checked. I know of no closed-loop, sentence-level, open-vocabulary intracortical voice synthesis that beats this paper's closed-loop result. The 88% comparison is offline against closed-loop and must stay qualified wherever it appears.

**Central confound.** The strongest confound is closed-loop real-time output (this paper) against offline simulated-real-time output ([2]), possibly also with different sentences and listener pools. The M06 section handles it, but the Verdict ("on the same data") does not.

**Fairness.** No later work is treated as prior. However, the Verdict presents the gap between forced choice and open transcription as the review's own finding, although the authors report both numbers in Fig. 2l.

**References.** [9], [10] and [11] are never cited in the body. Claim-table rows 25 and 26 point to a "Questions for the authors" section that is not in the review. Bibliographic data for [1] and [3]–[8] match my knowledge.

## Required fixes (ordered by impact)

1. **Sentence:** "The same group's later causal model reaches 5.24% WER on the same data [2], so this paper is the closed-loop proof, not the quality benchmark."
   **Wrong:** "on the same data" has no supporting quote, and the comparison hides the offline-versus-closed-loop confound.
   **Fix:** "The same group's later causal model reaches 5.24% listener WER with the same participant, evaluated offline with simulated real-time inference [2]; this paper is the closed-loop proof, not the quality benchmark."

2. **Sentence:** "The intelligibility claim does not: six-choice matching at 94.34% has a chance level near 17%, while open transcription gives 43.75% median WER (inference)."
   **Wrong:** The authors report the 43.75% WER themselves (Fig. 2l), so the "(inference)" tag is misplaced. "Six-choice" has no quote. "Does not [hold]" overstates a gap the authors disclose.
   **Fix:** Add a quote that establishes six options. Then write: "Intelligibility is weaker than the headline: the 94.34% six-choice matching (chance about 17%, inference) sits beside a 43.75% median open-transcription WER that the authors also report (Fig. 2l)."

3. **Sentence:** "\"Instantaneous\" refers to inference under 10 ms; the playback driver added the largest delay, shown only in Extended Data Fig. 1c. The follow-up cites 25 ms [2], versus 30–70 ms in 2009 [3]."
   **Wrong:** The quote covers the whole pipeline from signal acquisition to synthesis, not inference alone. "Shown only" is unsupported. The about-25 ms end-to-end latency appears to be stated by the target paper itself, not only by [2].
   **Fix:** "\"Instantaneous\" refers to neural processing from acquisition to synthesis under 10 ms; the audio playback driver added the largest delay (Extended Data Fig. 1c)." Cite the end-to-end figure from [1] if it is there; otherwise keep it as cited in [2].

4. **Sentence:** "Binary decoders trigger predefined pitch profiles (Methods): intonation is classified, not synthesized."
   **Wrong:** There is no claim-table quote. The sentence also conflicts with the Verdict's "voice with decoded intonation, emphasis and pitch" and ignores the three-level pitch task.
   **Fix:** Add the Methods quote and restrict the sentence to question intonation and emphasis. State separately how pitch level was produced. Otherwise delete the sentence.

5. **Sentence:** "The contamination control is a strength: 3.03% of 627 trials were acoustically correlated, and stethoscope decoding gave 100% WER against 43.60% for neural synthesis on matched trials (Methods)."
   **Wrong:** "627" and "100% WER" are not in the quotes. The quote says only that intelligible speech "could not be synthesized".
   **Fix:** Add quotes for 627 and the stethoscope WER. Otherwise write: "3.03% of trials were acoustically correlated, and decoding stethoscope and muscle signals yielded no intelligible speech, against 43.60% WER for neural synthesis (Methods)."

6. **Sentence:** "Only 3 of the 56 align targets with timing inferred from neural data: this paper and two [later] works (Appendix)."
   **Wrong:** The two works that decide the claim are not named. The Appendix reports known-item recall 0.0 for this slot. The rarity also does not square with a bare `standard` verdict.
   **Fix:** Name the two later works with year. Write "3 of the 56 ledger studies found (pattern match; known-item recall 0.0 for this slot)". Then add one clause on why the verdict stays `standard`, for example "no alternative alignment is tested, so the benefit is not shown".

7. **Sentence:** "After session 1 the boundaries came from the previous session's decoder, with manual review (Methods)."
   **Wrong:** The quote (t5) does not mention manual review.
   **Fix:** Add the quote for manual review, or delete "with manual review".

8. **Sentence:** "**Usual approach:** Of 87 studies that pair synthesis with real-time, online or causal operation (pattern match, unique studies), 24 describe offline or acausal decoding and 9 causal frame-level models (pattern match, upper bounds)."
   **Wrong:** The Appendix gives 24 as a slot-filled count ("decoding step role generate"), not pattern match.
   **Fix:** Use one basis. Either "24 (slot-filled)" with its own denominator, or a pattern-match count taken from the Appendix.

9. **Sentence:** "**Usual approach:** Synthesis usually trains on the user's paired audio; without it, 15 of 56 studies (pattern match, unique studies) use TTS targets and 2 a reference speaker; ..."
   **Wrong:** The Appendix tally ("other 8, paired audio 7", slot-filled) does not show paired audio as the usual choice.
   **Fix:** "Paired audio is the largest named category (7 of 31 slot-filled; 8 other); without it, 15 of 56 studies (pattern match) use TTS targets ..."

10. **Sentence:** "**Usual approach:** Crowd-worker transcription (15 of 79 studies, pattern match)." (and the table cell "Crowd-worker listeners (15 of 79) (pattern match 37)")
    **Wrong:** The denominator of 79 exceeds the 37 unique pattern-match studies the Appendix reports. 15 of 79 (19%) is not a "usual" approach.
    **Fix:** Reconcile the denominator with the Appendix. Then write "The most common named listener test is crowd-worker transcription (15 of N)".

11. **Sentence (table):** "| M03 Training and adaptation | Cumulative multi-session training | Supervised training on accumulated sessions (slot-filled 1,526) | – | not reported |"
    **Wrong:** The component is described in the paper and matches the usual approach, so "not reported" contradicts the row.
    **Fix:** Change the verdict to `standard`.

12. **Sentence:** "Residual speech (Fig. 2l): 96.43% to 43.75% WER is a fair within-participant comparison, but on 20 residual-speech trials."
    **Wrong:** "20 trials" is not in the quote.
    **Fix:** Add the quote with the trial count, or drop ", but on 20 residual-speech trials".

13. **Sentence:** "**State of the art:** Open transcription, 7 listeners per trial, here and in the follow-up (2026) [2]."
    **Wrong:** The 7-listener quote comes from [2] only. Nothing quoted shows 7 listeners in the target.
    **Fix:** Add a target quote, or write "Open transcription, 7 listeners per trial, in the follow-up (2026) [2]."

14. **Sentence:** "Earlier sentence synthesis scored 31% listener WER from a 25-word pool in speakers who could talk (2019) [7] and 54.4% on 1,024 words in anarthria (2023) [6]."
    **Wrong:** The quote for [6] is truncated ("54.4% (99%") and does not show the 1,024-word condition.
    **Fix:** Replace the claim-table quote with the full sentence that states the 1,024-word set.

15. **Sentence:** "**Usual approach:** Audio output in 11 of 22 neural-synthesis studies (slot-filled), without user control of pitch."
    **Wrong:** "Without user control of pitch" is not in the ledger tally row and is not sourced.
    **Fix:** Delete the qualifier, or support it with a count.

16. **Reference list and claim table:** [9], [10] and [11] are listed but never cited in the review body. Rows 25 and 26 refer to a "Questions for the authors" section that does not exist.
    **Fix:** Cite [9]–[11] where they are used, or remove them and renumber. Drop rows 25 and 26 or restore the section. Verify the DOI prefix of [2].

## Scores

- Procedure: 6/10. The quotes are attached to most numbers. However, several numbers (627, 100%, 20 trials, 7 listeners in the target, manual review, the pitch-profile mechanism) carry no quote, and the ledger counts disagree with the Appendix.
- Final text: 6/10. The position is clear and the closed-loop versus quality-benchmark framing is sound. But the Verdict overstates the intelligibility failure, and the comparison with the later model is under-qualified.

What works: the proxy-target critique of Pearson r, the stated chance levels and the cross-participant caveat on the ECoG gain are well made.
