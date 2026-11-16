# Evaluation: Brain-to-Text Decoding: A Non-invasive Approach via Typing

Date: 2026-11-16. Independent evaluator, one pass, no tools beyond the review and its claim table; no sources were re-opened. The claim table was filled by the writer, not by a separate checker, so a quote that is truncated or absent counts as insufficient evidence, not as support.

## Claim check

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target decodes executed typing; no earlier MEG/EEG ledger paper decodes typed text; ahead in Feb 2025 | Claim table rows 1, 7, 27 (audit only) | insufficient evidence | No quote; Appendix-only. Plausible. The closest non-invasive executed-movement prior known to the evaluator is EEG decoding of executed handwriting into characters (Crell and Müller-Putz, Computers in Biology and Medicine, 2024); it is not typing, so the "ahead" verdict can stand, but it should be named as a deciding prior next to [5]. |
| 2 | [later] async encoder gives CER 0.59 instead of 0.39 "on this dataset" / "on the target's own data" [2] | Rows 2, 13 | insufficient evidence | The quote gives 0.59→0.25 and 0.39→0.23 as a benefit of *scale*. It does not say that 0.59/0.39 were obtained on the target's recordings, nor at which data scale. Condition is attached without support. |
| 3 | 32% MEG and 67% EEG CER | Row 2 (t1) | correct | "CER of 32±0.6% with MEG and 67±1.5% with EEG". |
| 4 | Hand information peaks 40 ms after the keypress (Sec. 2.1) | Row 3 (t15) | insufficient evidence | Quote gives peak accuracy 74±1.3%, no latency. The 40 ms figure and the "after the keypress, when touch feedback is present" inference rest on nothing quoted. |
| 5 | Authors concede no route for people who cannot move | Row 3 (t47), row 10 (t45) | correct | "conducted exclusively with healthy participants". |
| 6 | [later] control: aligned windows without MEG 6.8% vs 34.9% with MEG [3] | Rows 4, 14 | wrong | Quote: "reduces balanced character accuracy from 37.0% to 6.5%". Neither number matches; the quoted manipulation ("preserve the aligned-window structure") may also differ from "without MEG". 3.45% chance and 22.0% vs 22.3% listening figures have no quote. |
| 7 | Brain2Qwerty v2: real-time MEG, 39% WER, nine subjects × 10 h [2] | Rows 6, 17 | partly correct | Nine subjects × 10 h quoted. 0.39 WER inferable from row 17 context but not in the visible quote; "real-time" has no quote. |
| 8 | Invasive typing 110 characters/min at 1.6% WER online [4] | Row 6 (n13) | insufficient evidence | 110 cpm quoted; the WER is cut off ("with a wo..."). 1.6% not visible. |
| 9 | Willett 2021: 90 characters/min, 94.1% raw online accuracy [5] | Row 8 | correct | Matches quote and the published abstract. |
| 10 | 20 MEG and 20 EEG participants; cohorts share five people | Rows 9, 19 | correct | 20 + 20 − 35 recruited = 5 overlap; arithmetic holds. |
| 11 | Typists screened at ≥80% accuracy (Sec. 4.1) | Row 10 | correct | Quote matches. |
| 12 | 500-ms keypress windows (Sec. 4.1) | Row 11 | correct | "0.5s time windows around each key press". |
| 13 | Async CTC encoder CER 0.25 "without a language model" vs 0.23 locked [2] | Row 12 | partly correct | Numbers match; "CTC" and "without a language model" are not in the quote. |
| 14 | EEGNet lacks subject layer; 1.14-fold EEG gain | Row 15 | correct | Both quoted. |
| 15 | 9-gram char KenLM, beam 30, weight 5 | Row 16 | correct | Quoted. |
| 16 | LLM lowers WER 0.43→0.39 but raises CER 0.26→0.31 [2] | Row 17 | insufficient evidence / possible contradiction | 0.43 n-gram WER and 0.31 CER quoted; the n-gram CER 0.26 is not visible (the visible comparator is Encoder alone 0.28). Also Encoder-alone CER 0.28 here sits beside "CER 0.23/0.25 without a language model" in M06: either different conditions (scale, held-out subjects) or a contradiction; the review does not say which. |
| 17 | LM corrects typists' own typos; typos 3.9% of keystrokes | Row 18 | correct | Quoted. |
| 18 | CER scored against the intended sentence (Sec. 4.1) | Row 18 | insufficient evidence | Location given, no quote for this point; it carries the "mixes decoding with language correction" position. |
| 19 | "Two-fold" MEG-over-EEG gain compares mostly different people | Row 19 | correct | 67/32 ≈ 2.1; overlap of five supported. |
| 20 | Single fixed split seed; undefined ± | Row 20, 24 | correct | Quoted. Note the ± is defined as SEM across subjects for the character-level 74% (row 3 quote); the review should say only the sentence-CER ± is undefined, which it does by scoping to "headline CER". Acceptable. |
| 21 | 14% chance is for single characters (Sec. 2.1) | Row 21 | insufficient evidence | Quote is from Sec. 4.2.4 and contains no 14%. Location and number both unsupported. |
| 22 | Inconsistencies: "heard" vs RSVP; 3.9% vs 3.6% | Row 22 | correct | Both typo rates and "hearing" quoted; RSVP side unquoted but is the paper's main task description. |
| 23 | Ledger denominators: 1,477 (M04), 1,460 (M06), 1,458 (M07 and table) | Rows 5, 25, 26, 30, 31, 35; table | wrong (internal) | M04 text says 1,477 with text; the table says pattern match 1,458; Appendix row 25 gives 1,458 + 20 = 1,478. M06 text says 1,460, table 1,458. Denominators disagree. |
| 24 | M12 verdict "not reported" | Component table | wrong | The paper reports CER against intended text; "not reported" is not a verdict category that fits. It should be `standard` (or the review must say what is not reported). |
| 25 | M09 and M10 both "slot-filled 82" | Component table | insufficient evidence | Identical counts for two different slots look like a copy; no Appendix row confirms either. |

Central claim and confound: the review's central position is that the 32% CER depends on known keystroke times and on a language model correcting typos. The strongest confound is that the 0.39 vs 0.59 contrast comes from a later pipeline, a different encoder and possibly a different data scale, with no language model, while the target's 32% includes the n-gram LM; the review compares across setups in the Verdict ("so the 32% MEG CER rests on known keystroke times") without stating this. Partly handled by "(inference)" in M06, not in the Verdict.

Fairness: [2], [3], [4] are correctly labelled [later] and used as state of the art, not as missed citations. However, the dependence on keystroke timing is a limitation the authors state themselves (Discussion, "Training indeed requires knowing both the timing and identity of each character"; also quoted by [2] Sec. 1), and the Verdict presents it as the review's finding without attribution.

## Required fixes (ordered by impact)

1. **Sentence:** "A [later] control clears window timing as a label leak: aligned windows without MEG give 6.8% balanced character accuracy against 34.9% with MEG [3]." (Verdict) and "The timing does not leak labels: synthetic aligned inputs reach 6.8% balanced character accuracy against 34.9% with MEG and 3.45% chance, unlike word-aligned listening data, where brain-free inputs score 22.0% against 22.3% [3]." (M06)
   **Wrong:** The only quote gives 37.0% → 6.5%, for inputs "that preserve the aligned-window structure". 6.8%, 34.9%, 3.45%, 22.0% and 22.3% have no supporting quote.
   **Fix:** Use the quoted values (6.5% vs 37.0%) with the quoted condition, or add the quote and location for each number kept; drop any number that cannot be quoted.

2. **Sentence:** "on this dataset the group's [later] asynchronous encoder gives CER 0.59 instead of 0.39 [2]" (Verdict) and "On the target's own data the asynchronous encoder gives CER 0.59 against 0.39 locked [2], so keystroke times remove about a third of the error at this data scale (inference)." (M06)
   **Wrong:** The quote reports 0.59 and 0.39 only as the starting points of a data-scale curve; it does not establish that they were measured on the target's recordings. Comparing them to the target's 32% (with LM) mixes encoder, data and LM.
   **Fix:** State the condition the source gives (the smaller-data point of the scaling comparison, no LM), and either quote where [2] says this is the target's dataset or remove "on this dataset" / "on the target's own data". In the Verdict, change "so the 32% MEG CER rests on known keystroke times" to "the target's decoder depends on known keystroke times, which the authors acknowledge (Discussion); in [later] work, removing them raised CER from 0.39 to 0.59 at small data scale [2]".

3. **Sentence:** "The signal is executed finger movement of healthy typists, with hand information peaking 40 ms after the keypress (Sec. 2.1)" (Verdict) and "a hand signal that peaks after the keypress, when touch feedback is already present (inference)" (M04)
   **Wrong:** The quoted Sec. 2.1 passage gives a peak accuracy (74%), not a latency. The 40 ms value is unsupported, and the M04 inference depends on it.
   **Fix:** Add the quote and figure that give the 40 ms peak for hand/motor information, or delete the latency and the touch-feedback inference.

4. **Sentence:** "Among 1,477 MEG or EEG language-decoding studies with full text (pattern match, unique studies, Appendix)" (M04) and "(310 of 1,460 MEG or EEG studies, pattern match, Appendix)" (M06)
   **Wrong:** The component table gives "pattern match 1,458" for M04, M06 and M07; the Appendix gives 1,458 + 20 = 1,478 for M04. Three different denominators for the same pool.
   **Fix:** Use one denominator per slot, identical in text, table and Appendix, and state whether full-text-only additions are included.

5. **Sentence:** Component table row "M12 Evaluation | CER vs intended text | CER/WER (slot-filled 8,381) | – | not reported"
   **Wrong:** The paper reports CER (and the review discusses it at length); "not reported" contradicts the row's own content and is not a usable verdict.
   **Fix:** Change the verdict to `standard`, or, if the intent is that sentence-level chance/WER is missing, write that as the reason and keep the verdict category valid.

6. **Sentence:** "In 2026 a [later] LLM pipeline lowers WER from 0.43 with an n-gram model to 0.39 but raises CER from 0.26 to 0.31 [2]." (M07)
   **Wrong:** The quote shows CER 0.31 vs Encoder alone 0.28; the n-gram CER 0.26 is not visible. Also, Encoder-alone CER 0.28 here conflicts on its face with "CER 0.25 without a language model, against 0.23 keystroke-locked" in M06 from the same source.
   **Fix:** Quote the 0.26 n-gram CER with its location, and state the condition of each figure (e.g., held-out-subject evaluation in Fig. 3 vs full-data scaling in Fig. 1) so the 0.23/0.25 and 0.28 values are not read as the same setting.

7. **Sentence:** "In 2026 the [later] Brain2Qwerty v2 decodes typed sentences from real-time MEG at 39% WER ... [2]; invasive typing reaches 110 characters per minute at 1.6% WER online [4]." (M04)
   **Wrong:** "real-time" has no quote; the 1.6% WER is cut off in the quote ("with a wo...").
   **Fix:** Add the full quotes (real-time decoding in [2]; the WER value in [4]) or drop "real-time" and the 1.6%.

8. **Sentence:** "Chance: the 14% chance is for single characters (Sec. 2.1); nothing anchors the 32% and 67% sentence CER." (Where the claims outrun the evidence) and "CER is scored against the intended sentence (Sec. 4.1)" (M07)
   **Wrong:** The quote supplied for chance is from Sec. 4.2.4 and contains no 14%; the scoring-against-intended-text claim has no quote, yet it carries the position that the headline CER "mixes decoding with language correction".
   **Fix:** Give the passage and correct section for the 14% chance level and for scoring against the intended sentence; correct the section number if it is 4.2.4.

9. **Sentence:** "Its decoder (M06) is standard: keystroke-locked windows are the usual segmentation ... so the 32% MEG CER rests on known keystroke times." (Verdict)
   **Wrong:** The authors state this limitation themselves (Discussion: "Training indeed requires knowing both the timing and identity of each character"); the review presents it as its own finding.
   **Fix:** Attribute it: "as the authors note (Discussion)", and keep the review's contribution to the quantification from [2].

10. **Sentence:** Component table rows "M09 Confirmation ... Mostly absent (slot-filled 82)" and "M10 Correction ... Mostly absent (slot-filled 82)"
    **Wrong:** Identical counts for two different slots with no Appendix row; looks like a copied value.
    **Fix:** Check each slot's tally in the ledger and report its own count, or mark the count as shared and say why.

Advisory (not required): in M04, name EEG decoding of executed handwriting into characters (Crell and Müller-Putz, Computers in Biology and Medicine, 2024) among the deciding non-invasive priors, so the "none decodes executed keystrokes" sentence is shown to exclude the nearest executed-movement design.

## Scores

- Procedure: 5/10. Claim table present and mostly located, but several load-bearing numbers have truncated or missing quotes, and one comparator ([3]) contradicts its own quote.
- Final text: 6/10. Clear positions and well-chosen confounds (cohort overlap, LM correction, keystroke timing), undermined by unsupported numbers and inconsistent denominators.
