# Evaluation: Vocoder-Based Speech Synthesis from Silent Videos

Date: 2026-11-18. Independent evaluator, single pass over the review and its claim table only (no sources reopened). The claim table was filled by the writer, not by a separate checker, so a row whose quote does not contain the number is treated as unverified.

## Claim checks

| # | Claim (first words) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Verdict: "changes two components: a CTC character head ... WORLD vocoder features" | Row 1, row 12 | correct | Quotes support multi-task text prediction and prediction of all vocoder features. |
| 2 | Verdict: "The text loss repeats a 2018 ultrasound design [2]" | Row 2, row 7 | wrong (overstated) | [2] trains frame-level HMM-state targets from ultrasound; the target trains a sequence-level CTC character loss from video. Same multi-task idea, not the same design. "Without citing it" has no supporting row (no check of the target's reference list). |
| 3 | Verdict: "moves ESTOI by 0.007 to 0.013 in one run per configuration" | Rows 9, 10; M02 section | correct | Seen +0.007/+0.008, unseen +0.013/+0.008; single run and PESQ-selected checkpoint quoted (row 10). |
| 4 | Verdict: "ESTOI 0.455 against 0.329 ... the ranking survives a later re-scoring [3]" | Rows 3, 15, 16 | insufficient evidence | 0.455 quoted; 0.329 quoted in row 18. [3] keeps both ESTOI values, so only PESQ was re-scored; and [3]'s unseen PESQ for this system is 1.26 (row 14) against 1.23 in the paper, i.e. it rises, so [3] is not a uniform re-scorer. "Survives a re-scoring" is too strong. |
| 5 | Verdict: "on unseen speakers the two tie" | Row 18; M06 section | wrong | The review's own numbers give ESTOI 0.202 to 0.227 for every variant against 0.198 for the GAN (up to 15% higher). PESQ ties; ESTOI does not. "As the authors say (Sec. 3.2)" has no quote. |
| 6 | Verdict: "15.1% and 51.6% WER come from the CTC head of a PESQ-selected model" | Rows 4, 10, 19 | correct | Table 3 row and Table 1 selection rule quoted; Sec. 2.4 best-path decoding cited. |
| 7 | Verdict: "9.29% ASR WER ... against 4.07% ... 38.15% against 16.05% [3]" | Rows 5, 13, 14 | correct for 9.29 / 38.15; insufficient for 4.07 / 16.05 / 17.84 | Comparator rows of [3] not quoted. Arithmetic (56%, 58%, 13%) correct. |
| 8 | M02 usual approach: "34 unique studies ... 10 synthesize speech" | Rows 6, 26 | not checked (ledger) | Outside scope. |
| 9 | M02 [2]: "about 7% relative error reduction in both tasks" | Row 7 | correct | Quote matches. |
| 10 | M02 "28-symbol CTC head (Table 1)" | Row 7 | insufficient evidence | No quote with 28 symbols. |
| 11 | M02 SOTA: "removing it raises ASR WER on LRS2 from 60.54% to 84.27% [4]" | Row 8 | insufficient evidence / possible mismatch | Quoted ablation row is "− Feature-level C.S." (feature-level content supervision), not labelled "CTC". 60.54% is not quoted. If other text supervision remains in that ablation, the 28% is the effect of one supervision term, not of "the text loss". |
| 12 | M02: "+0.01 and +0.03 PESQ, +0.007 and +0.008 ESTOI ... 1.6% and 1.8% ... 6.1% and 4.0%" | Row 9 | correct (arithmetic) | Values consistent with the bases given. |
| 13 | M02: "All four signs agree" | Row 9 | insufficient evidence | Four signs counted on ESTOI (and seen PESQ); unseen PESQ change is never given, and the unseen PESQ range 1.19 to 1.25 leaves room for a drop in one pair. |
| 14 | M06 usual approach: "165 ... 49 neural, 41 parametric, 16 Griffin-Lim, 3" | Rows 11, 30, 32 | not checked (ledger) | Outside scope. |
| 15 | M06 SOTA: "a 2023 comparison" | Reference 3 | wrong (inconsistent) | Cited as the 2024 journal version, read as arXiv v1; table numbers taken from the preprint. |
| 16 | M06: "38% higher" ESTOI vs GAN | Row 15 | correct | 0.455/0.329 = 1.38. |
| 17 | M06: "PESQ to 1.61 ... and 1.47 for the GAN ... drop by 14% to 15%" | Row 16 | correct for 1.61; insufficient for 1.47 | 1.90→1.61 = 15.3%, 1.71→1.47 = 14.0%. GAN row not quoted. |
| 18 | M06: "9.29% against 19.94% for the GAN" | Row 17 | insufficient evidence | 19.94% not in any quote. |
| 19 | Outrun: WER values 15.1, 14.4, 51.6, 69.3 from the CTC head, "unlike the 26.6% ASR WER of [5]" | Row 19 | partly supported | 26.6% not quoted. |
| 20 | Outrun: "authors concede this favours reconstruction over recognition on unseen speakers" | Row 20 | insufficient evidence | Quote is only the selection rule; the concession sentence (Sec. 3.2) is not quoted. |
| 21 | Outrun: "Improvement over existing approaches holds for seen speakers only" | Rows 18, 21 | wrong | Same as #5: unseen ESTOI is higher for every variant. |
| 22 | Outrun: "Real time" without latency | Row 22 | correct | |
| 23 | Outrun: "Filtering raised the GAN's PESQ to 1.80" | Row 23 | correct | This is the authors' own statement (Sec. 3.1); fine as long as it is not presented as the review's finding. |
| 24 | Outrun: "No WER chance level ... six-word grammar" | Row 24 | correct, weak | A grammar-based chance level is derivable (roughly 80% WER for slot-wise random guessing); the review could state it rather than say "no floor". |
| 25 | Table M11: "15/7/10 unseen-speaker split" | none | insufficient evidence | No row; GRID has 33 usable speakers, 15+7+10 = 32. Verify against Sec. 2.1. |

Strongest confound: different starting points and scorers across systems (WORLD vs raw waveform, paper-internal vs [3] PESQ, CTC-head WER vs ASR WER). The review handles the WER confound well and partly handles the PESQ one; it does not handle that [3] copies ESTOI rather than re-scoring it. No fairness issue on chronology: [3] and [4] are labelled [later] and used only as state of the art. No "first / only" claims; all verdicts are `standard`, `not applicable` or `not reported`, so no `ahead` rule checks apply.

## Required fixes (ordered by impact)

1. **Sentence:** "The WORLD route beats the 2019 GAN on seen GRID speakers (ESTOI 0.455 against 0.329), and the ranking survives a later re-scoring [3]; on unseen speakers the two tie." (Verdict), and "On unseen speakers the paper's own numbers are a tie, PESQ 1.19 to 1.25 against 1.24 and ESTOI 0.202 to 0.227 against 0.198 (Table 3), as the authors say (Sec. 3.2)." (M06), and "\"Improvement over existing video-to-speech approaches\" (Abstract) holds for seen speakers only (Table 3, Sec. 3.2)." (Where the claims outrun the evidence).
   **What is wrong:** Every variant's unseen ESTOI (0.202 to 0.227) exceeds the GAN's 0.198, up to 15% higher; only PESQ ties. "As the authors say" has no supporting quote. The three sentences overstate the tie and contradict the review's own numbers.
   **Fix:** "On unseen speakers PESQ ties (1.19 to 1.25 against 1.24) and ESTOI is higher (0.227 against 0.198), one run each (Table 3)." Quote the Sec. 3.2 sentence if keeping "as the authors say", otherwise drop it. Change the outrun bullet to: "holds clearly for seen speakers; on unseen speakers only ESTOI improves (Table 3)."

2. **Sentence:** "In a 2023 lip-to-speech system with a CTC loss before synthesis, removing it raises ASR WER on LRS2 from 60.54% to 84.27% [4] [later]: a 28% relative reduction from the text loss" (M02 State of the art; also the M02 table row).
   **What is wrong:** The quoted ablation row is "− Feature-level C.S.", not a row labelled CTC; the full-model 60.54% is not quoted. If the ablated model keeps other text supervision, the 28% is the effect of one supervision term, not of "the text loss".
   **Fix:** Quote both rows and name the ablation as the paper does: "removing feature-level content supervision (a CTC loss on the visual features) raises ASR WER on LRS2 from 60.54% to 84.27% (Table 1 of [4])". Say whether other text supervision remains in that ablation.

3. **Sentence:** "The text loss repeats a 2018 ultrasound design [2]" (Verdict) and "the paper does the same from video with a 28-symbol CTC head (Table 1) without citing it" (M02).
   **What is wrong:** [2] uses frame-level HMM-state classification from ultrasound; the target uses a sequence-level CTC character loss from video. "Repeats" and "the same" overstate the match. "Without citing it" and "28-symbol" have no supporting quote.
   **Fix:** "The text loss follows the multi-task idea of a 2018 ultrasound system [2] (frame-level HMM states there, a CTC character loss here)". Keep "without citing it" only if the target's reference list was checked, and add the Table 1 quote for the 28 symbols.

4. **Sentence:** "the ranking survives a later re-scoring [3]" (Verdict) and "The later table re-scores PESQ to 1.61 for this system and 1.47 for the GAN while keeping both ESTOI values (Table IV of [3]); both PESQ values drop by 14% to 15%, so the order holds under either scorer (inference)." (M06).
   **What is wrong:** [3] copies ESTOI rather than re-scoring it, and its unseen PESQ for this system is 1.26 against the paper's 1.23 (a rise), so [3] is not a consistent re-scoring. The GAN's 1.47 and 19.94% are not quoted.
   **Fix:** "A later table lists PESQ 1.61 for this system and 1.47 for the GAN (Table IV of [3]); its PESQ values differ from the originals in both directions (1.26 against 1.23 on unseen speakers), so it confirms the PESQ order but not a uniform re-scoring." Add the GAN row quote for 1.47 and 19.94%.

5. **Sentence:** "All four signs agree, but each is one run, checkpoint chosen by validation PESQ (Table 1), with no retraining spread." (M02).
   **What is wrong:** The unseen PESQ change for each pair is never given; the stated unseen PESQ range (1.19 to 1.25) leaves open a drop in one pair, so "all four signs" is not supported for PESQ.
   **Fix:** Give the unseen PESQ change for the mouth and face pairs, or say "All four ESTOI signs agree".

6. **Sentence:** "On the four seen GRID speakers a 2023 comparison lists this system ..." (M06 State of the art).
   **What is wrong:** Reference 3 is cited as the 2024 journal version but was read as arXiv v1; the year and the table numbering may differ between versions.
   **Fix:** "a 2023 preprint (journal 2024) lists ..." and note in the reference that table numbers are from arXiv v1.

Optional: state the GRID grammar chance level instead of "has no floor"; verify the 15/7/10 unseen split (GRID has 33 usable speakers).

## Scores

- Procedure: 6/10. Claim table rows often quote only the target's row while the claim rests on a comparator number (19.94%, 4.07%, 1.47, 60.54%, 26.6%) that no row quotes.
- Final text: 7/10. Clear position and a well-placed weakest claim (CTC-head WER is not speech WER); the unseen-speaker tie and the "repeats [2]" wording overstate the evidence.
