# Independent evaluation: From Silent Signals to Natural Language (arXiv:2509.04507)

Date: 2026-11-21. Fallback evaluator (claim table only). Input: the Verdict, component sections, component table, references and claim table of the compact review. No source was re-opened; claims are judged against the quotes and locations in the claim table, plus general knowledge of the field where stated.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper keeps the Gaddy EMG-to-speech pipeline and changes the recognizer and adds GPT-2 correction | Claim rows 1, 13 (t3, t6, t7, t8, t46) | correct | Quotes show Gaddy-style transduction, a new Transformer ASR and a GPT-2 stage. "Transformer transducer" in M01 is looser than t46 ("Transformer encoder"). |
| 2 | Paper claims to be the first LLM correction stage in SSI (Sec. 1) | Row 2, 17 (t17) | correct | t17 states this verbatim. |
| 3 | [3] passed beam lists and ensembles from silent EMG to an LLM and reached 12.2% test WER on the same benchmark | Rows 2, 9 (c1, c3) | correct, partly insufficient | c1 gives 12.2% on silent EMG; "test" and "10-model ensemble" are not in the quoted text. Consistent with the known result of [3]. |
| 4 | Recognizer gain 36% to 32.5% swaps the scoring ASR on the same audio | Row 3 (t10, t11) | correct | Table 1 values match. Row 3 also attaches c9 (a quote from [6]) to a claim about the target; that quote does not belong to this row. |
| 5 | Final 30% does not beat 28.8% from a direct EMG-to-text decoder | Row 4 (c2, t12) | correct, insufficient attribution | 28.8% appears in Table 3 of [3] as "GADDY (2022)". The original work behind 28.8% is not named or cited in the review; whether it used the same ~100-utterance test set is not shown. |
| 6 | One run, about 100 utterances, no split, seeds or uncertainty | Row 5 (t21) | partly wrong | t21 says "the complete test set (≈100 utterances)", so a test split exists; what is missing is which split. "No split" overstates. Seeds and uncertainty: absence claim, plausible. |
| 7 | Earlier designs give the LM several hypotheses: [4] GPT-2 beam rescoring, [5] 5-gram then LLM, [3] LLM over beams/ensembles | Row 7 (c8, c7, c3) | correct | Quotes support each design. |
| 8 | Paper rewrites one ASR output with GPT-2; its related work cites N-best correction | Row 8 (t47, t48) | insufficient evidence | t47 ("operating on the ASR output") does not say a single hypothesis. t48 is shown without context, so it is not clear it is related work rather than the paper's own design. |
| 9 | Paper's 30% trails 12.2% by 17.8 points | Row 9 | correct | 30 − 12.2 = 17.8. |
| 10 | LLM effect 32.5% to 30% (2.5 points, 7.7% relative) versus 20.6% to 18.0% in [3] (12.6% relative) | Row 10 (t11, t12, t14, c4) | arithmetic correct; 20.6% unsupported | 2.5/32.5 = 7.7%; 2.6/20.6 = 12.6%. c4 quotes only 18.0%; no quote carries 20.6%. "No larger than" is accurate (2.5 vs 2.6 points), but absolute gains are near equal; say so plainly. |
| 11 | [3] averaged 5 seeds and fixed its test model before testing | Row 11 (c6) | partly insufficient | c6 supports five random initializations. "Fixed its test model before testing" has no quote. Location column says "Sec. 2.5", which is the target's section, not [3]'s. |
| 12 | Paper's threshold, filters and checkpoint are unstated (Sec. 2.5) | Row 11 (t30, t32) | contradiction | The component table (M07) states "threshold 0.7", while the M07 text says the threshold is unstated. No quote supports 0.7. |
| 13 | M06 state of the art: GETS (2026) 11.89% with Whisper-medium, 21.32% with DeepSpeech | Row 14 (c9) | partly insufficient | c9 gives 11.89% but is cut before the dataset name; 21.32% has no quote. Correctly labelled [later]. |
| 14 | Scorer alone shifts WER by 9.4 points, more than the paper's 3.5-point recognizer gain | Row 15 | correct if #13 holds | 21.32 − 11.89 = 9.43; 36 − 32.5 = 3.5. |
| 15 | The 36% baseline matches the figure [3] gives for Gaddy's audio route | Row 16 (c5) | insufficient, possibly wrong | c5 reads "a 36% WER when directly", which is cut off and, as it stands, suggests direct decoding rather than the audio route. Hedged as inference, but the quote does not support "audio route". |
| 16 | No condition separates GPT-2 effect from scorer change | Row 18 (t10–t12) | correct | Table 1 has only the three rows. |
| 17 | "Substantial improvements in intelligibility" rests on WER only; no listener rating | Row 19 (t13, t36) | correct | 6/36 = 16.7%, consistent with the paper's "16% relative". |
| 18 | sEMG at 1000 Hz (Sec. 2.2) versus processing at 16 kHz (Sec. 3) | Row 20 (t16) | insufficient evidence | Only the 16 kHz statement is quoted; the 1000 Hz statement has no quote. |
| 19 | Fig. 2 shows a convolutional front end that Sec. 2.3 omits | Row 20 (t46) | insufficient evidence | t46 does not show the omission. Note that Gaddy's model has convolutional blocks, so Fig. 2 may simply be accurate and the text incomplete. |
| 20 | 0.78 s per utterance does not establish near-real-time use | Row 21 (t12, t15) | partly insufficient | 0.78 s is in Table 1; the paper's own "near-real-time" wording is not quoted, so the review rebuts a claim the reader cannot see. |
| 21 | M07 usual approach: n-gram LM (78), LLM rescoring or correction (50) of 382 | Rows 6, 26, 27 | outside check | Ledger tally; plausible as the usual design. |
| 22 | M06 usual approach: Whisper (9), DeepSpeech (7) of 16 | Rows 12, 31 | outside check | Plausible: DeepSpeech in the Gaddy line, Whisper in later work. |
| 23 | M07 verdict behind | M07 section, Appendix rows | correct | Best comparable work named, counts in Appendix, effect compared. |
| 24 | M03, M12, M13 verdict "not reported" | Component table | inconsistent | Each row states content the paper reports (Gaddy corpus; WER on ~100 utterances; 0.78 s on GPU). The verdict label needs a short reason (for example, which detail is missing) or a different label. |
| 25 | Fairness: [6] is later work | References, M06 | correct | Labelled [later], used only as state of the art, not as a missed citation. [3] (2024) predates the target by more than 6 months, so citing it as missed prior work is fair. |

## Central claim and confounds

The strongest confound for the "behind" position is system strength: 12.2% in [3] comes from a different, stronger EMG front end with cross-modal training and a 10-model ensemble, so the 17.8-point gap is not a measure of the LLM stage. The review handles this by comparing the added LLM effect (2.5 versus 2.6 points), which is the right move, but that comparison rests on a 20.6% starting value that has no quote and on validation data in [3] versus test data in the target. The second confound, scorer change versus system change, is handled well. The priority rebuttal names the deciding prior work [3].

## Required fixes (by impact)

1. Resolve the M07 contradiction: the table says "threshold 0.7" and the text says the threshold is unstated. Quote the value with its location, or remove it.
2. Supply the quote and location for the 20.6% starting WER in [3], or drop the relative-effect comparison; state plainly that absolute gains are about equal (2.5 versus 2.6 points).
3. Quote the full sentence behind c5 ("a 36% WER when directly ..."). If it refers to direct decoding, revise "Gaddy's audio route" in M06.
4. Name and cite the original source of the 28.8% direct EMG-to-text result, and state whether its test set matches the target's.
5. Add quotes for the GETS 21.32% DeepSpeech value and for the dataset behind 11.89%, since the 9.4-point scorer argument depends on both.
6. Replace "no split" in the Verdict with "the test split is not identified"; t21 shows a test set was used.
7. Add a quote showing that the GPT-2 stage receives a single hypothesis, and show that the N-best sentence in Sec. 1 is related work.
8. Add the missing quotes for the 1000 Hz sampling rate (Sec. 2.2) and the omission of the convolutional front end, or drop the inconsistency bullet.
9. Quote the paper's "near-real-time" wording before rebutting it.
10. Give a reason for "not reported" on M03, M12 and M13, or change those labels; each row lists content the paper does report.
11. Support "fixed its test model before testing" for [3] with a quote, or remove it.
12. Fix the claim table: remove the GETS quote (c9) from row 3, and correct the row 11 location (Sec. 2.5 is the target's section, the [3] evidence is Sec. 4.6 / Sec. 5).

## Scores

- Procedure: 7/10. The claim table covers every number and citation, but several rows carry truncated or missing quotes for load-bearing values.
- Final text: 6/10. Clear position and well-chosen comparators. One internal contradiction and several unquoted figures weaken the central comparison.

The scorer-versus-system argument and the priority rebuttal are the review's strongest parts.
