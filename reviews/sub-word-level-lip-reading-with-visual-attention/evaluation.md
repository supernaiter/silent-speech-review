# Evaluation: Sub-word Level Lip Reading With Visual Attention (Prajwal, Afouras, Zisserman, CVPR 2022)

Date: 2026-11-17. Independent evaluator, one pass. Inputs were the review and its claim table. The claim table was filled by the writer, not by a separate checker, so a row counts as support only when its quote itself carries the number and the condition. No sources were re-opened. Notes on later work come from the evaluator's own knowledge and say so.

## Claim check

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Verdict: VTP pools a 24x24 map by attention; WordPiece output | Rows 1, 14 (t16, t17, t19) | correct | Six layers with 8 heads and 30,522 tokens are quoted. "24x24" is not quoted directly; it follows from 96 px input at H/4 (Table 3, row 10). Acceptable. |
| 2 | Verdict: 37.2 to 30.9% WER on LRS2; 80.2 to 88.2 test mAP | Row 2 (t36, t37, t51, t52) | correct | The Table 4 rows hold two numbers each. The review takes the second column as test; the quote does not label the columns, but this reading is plausible. |
| 3 | Verdict: "best [later] systems keep standard ResNet-18 trunks" | Row 3 (n10, n15) | insufficient evidence | True for [4] and [5]. Not true across the best later work: the lowest LRS3 VSR WER known to the evaluator (LP Conformer, 12.8%, 2024) uses a linear-projection front-end, not a ResNet-18. See fix 3. |
| 4 | Verdict and Where the claims outrun: "first use of sub-word units" is wrong, given FastLR [2] | Rows 4, 22 (n1, n2, t2) | correct | FastLR (ACM MM 2020, arXiv Aug 2020) brings BPE into lipreading on LRS2 with a 1k vocabulary. It appeared more than 12 months before the target, so it is fair prior work. |
| 5 | Verdict: the SOTA table spans 389 to 31,000 hours | Row 5 (t28, t29, t33) | correct | |
| 6 | M06 usual approach: 3D conv + ResNet + average pooling, 254 of 1,116 | Row 6 (n5) + ledger | correct | The [3] quote supports per-frame average pooling. Ledger counts are outside this check. |
| 7 | M06 SOTA: 17.6% on LRS3 from [4] with 656 labelled + 2,649 unlabelled hours | Row 7 (n13) | insufficient evidence | 17.6% is quoted. The hours are not quoted (they match LRS2+LRS3 and VoxCeleb2+AVSpeech, so they are plausible). Lower WERs exist: see fix 3. |
| 8 | M06 SOTA: 19.1% at 3,448 h in 2023 [5] | Row 7 (n8) | correct | 3,448 h is not in the quote but matches Auto-AVSR as the evaluator knows it. |
| 9 | 30.7% vs 17.6%: "13.1 points or 43% relative behind today" | Row 8 | correct (arithmetic) | 13.1/30.7 = 42.7%. "43% relative behind" is ambiguous: it is a 43% reduction from the paper's value, but 74% higher than 17.6. The SOTA reference point also changes under fix 3. |
| 10 | CBAM in ResNet blocks: 83.14% vs 83.10% on LRW [3] | Row 9 (n6) | insufficient evidence | The quote only says CBAM was plugged in. Neither number is quoted. |
| 11 | Table 3: 35.7, 33.8, 30.9% "at roughly matched parameter counts" | Row 10 (t42–t44) | insufficient evidence | The WERs are quoted. The column read as 2, 3, 6 looks like a layer count, which would argue against matched size. No parameter count is quoted. |
| 12 | Auto-AVSR 33.0% at 818 h vs paper 40.6% at 698 h: "7.6 points in favour of plain averaging with a stronger temporal encoder" | Row 11 (n9, t30) | wrong (judgment) | The numbers and the 7.6-point difference are right. Attributing the gap to averaging is not supported: the hours, encoder, CTC/attention loss, augmentation and LM all differ. Same-generation evidence points the other way: VTP at 698 h (40.6) beats ResNet + Conformer at 639 h (43.3) [7]. |
| 13 | 132 later averaging studies vs 38 attention | Row 12, ledger | not checked (ledger) | |
| 14 | M08 usual approach: characters in [7], 75 graphemes in [8] | Row 13 (n16, n17) | correct | |
| 15 | M08 SOTA: SentencePiece 5,000 [5] and 1,000 [4] | Row 15 (n11, n14) | correct | |
| 16 | FastLR 1k BPE, BPE helped "to 75.7% WER" [2] | Row 16 (n2, n3) | correct | This is an ablation value from a non-autoregressive model with a high WER. |
| 17 | 41.0 to 37.2%, 3.8 points, 9% relative | Row 17 | correct | 3.8/41.0 = 9.3%. |
| 18 | "BPE is called worse with no number (Sec. 4.2)" | Row 18 (t19 only) | insufficient evidence | No quote shows the paper saying BPE is worse. |
| 19 | "the field settled on 1,000 to 5,000 units" | Row 18 (n11, n14) | insufficient evidence | The only support is two systems from one group. |
| 20 | GPT-2 rescoring adds 1.1; all-n-gram 30.92 vs curriculum 30.91; TEDxext uses YouTube ASR captions | Row 19 (t38, t40, t8) | partly insufficient | The 1.1 and 30.92 are quoted. 30.91, "GPT-2" and "YouTube" are not. |
| 21 | 9- and 2.7-point gains over [7] mix design with data | Row 20 (t28–t30, t53) | correct | The paper's "9%" and "2.7%" are absolute points (37.9 to 28.9; 43.3 to 40.6). The review reads them correctly. |
| 22 | "Ten times less data" vs 31,000 h; includes non-public MV-LRS and ASR-labelled TEDxext | Row 21 (t54, t34, t33) | correct | 31,000/2,676 = 11.6x. |
| 23 | "All results are single runs (Sec. 4.4, Sec. 5)" | Row 23 (t59) | wrong (no support) | The quote is about public-data training. It says nothing about runs or seeds. |
| 24 | Public code: LM weight 0.35; extended checkpoint trained on LRS3v2; 22.3% instead of 22.6% | Row 24 (t67, t73) | wrong (contradicted) | The README quote (t67) gives α = 0.7 / 0.6, the same as the paper, not 0.35. The t73 quote repeats the Table 1 row and supports neither LRS3v2 nor 22.3%. The text also cites Sec. 4.2 / Table 1, not the repository. |
| 25 | M04 "Silent video of spoken sentences" | Table row M04 | wrong (wording) | LRS2/LRS3 test clips show voiced speech with the audio not used. "Silent video" suggests silent speech, against the project rule to record the input signal and the speech mode separately. |
| 26 | M12 verdict "not reported" | Table | insufficient evidence | The paper reports WER on LRS2/LRS3. The review's concern is unmatched training data, and that is not "not reported". |
| 27 | M06 verdict "ahead" (ledger count, deciding priors, effect repeated) | Appendix rows 27–30; Verdict | correct | The ledger tally is in the Appendix. Deciding priors [6] and [3] are named. The effect repeats on LRS2 VSR and on AVA speech detection. |
| 28 | Chronology and bibliography of [2]–[8] | References | correct | Venues, years and arXiv ids match the evaluator's knowledge. [4] and [5] are correctly marked [later]. |

## Required fixes (by impact)

1. **Sentence:** "The public code uses LM weight 0.35 against 0.7 and 0.6 (Sec. 4.2), and its extended checkpoint was trained on LRS3v2, not TEDxext, scoring 22.3% rather than 22.6% (Table 1)."
   **Wrong:** the review's own README quote gives α = 0.7 / 0.6, which contradicts 0.35. Nothing quoted supports LRS3v2 or 22.3%, and the sentence cites paper sections, not the repository.
   **Fix:** delete the bullet, or quote the exact repository lines (file and line) that show 0.35, LRS3v2 and 22.3%, and cite the repository as the location.

2. **Sentence:** "All results are single runs (Sec. 4.4, Sec. 5), so the 1.1-point LM and 0.9-point flip gains (Table 2) carry no error bars."
   **Wrong:** the quoted passage (public-data training) does not say anything about runs. "Flip" is not in the quote, which says "test-time augmentation".
   **Fix:** write "No seed variance or error bars are reported (Table 2), so the 1.1-point LM and 0.9-point test-time-augmentation gains are of unknown reliability." Alternatively, quote a passage that states single runs.

3. **Sentence:** "**State of the art:** 17.6% visual-only LRS3 WER in 2026 from a ResNet-18 model …" Related sentences: "is 13.1 points or 43% relative behind today" and, in the Verdict, "the best [later] systems keep standard ResNet-18 trunks".
   **Wrong:** 17.6% is not the lowest reported LRS3 VSR WER. From the evaluator's knowledge, not re-checked here: LP Conformer (Chang et al., "Conformers are All You Need for Visual Speech Recognition", ICASSP 2024) reports 12.8% with about 100k h of non-public YouTube data and a linear-projection front-end. SynthVSR (Liu et al., CVPR 2023) reports about 16.9% with public plus synthetic data.
   **Fix:** state the scope ("best with public audiovisual data and a ResNet-18 front-end: 17.6% [4]"), and add the 12.8% non-public result as the absolute best. Recompute or qualify the 13.1-point gap, and write the relative figure unambiguously ("43% lower than the paper's 30.7%"). Restrict the Verdict claim to "the best public-data systems keep ResNet-18 trunks".

4. **Sentence:** "… 33.0% on LRS3 with 818 hours [5] against the paper's 40.6% with 698 hours, 7.6 points in favour of plain averaging with a stronger temporal encoder (inference)."
   **Wrong:** the comparison changes the hours, encoder, loss, augmentation and LM together. It cannot be credited to averaging, and the review's own data ([7] at 639 h, 43.3%, against VTP's 40.6%) shows VTP ahead within the same generation.
   **Fix:** "… a 7.6-point gap that comes from a newer recipe (Conformer, CTC/attention, augmentation, 120 more hours); it shows VTP was not needed for later gains, not that averaging is better."

5. **Sentence:** "WER falls as VTP pools at higher resolution (35.7, 33.8, 30.9%) at roughly matched parameter counts (Table 3)."
   **Wrong:** no parameter count is quoted. The quoted column (2, 3, 6) looks like a layer count, which suggests the model sizes differ.
   **Fix:** quote the parameter counts from Table 3, or drop "at roughly matched parameter counts". If the values are layer counts, write "with 2, 3 and 6 VTP layers".

6. **Sentence:** "… or insert CBAM in ResNet blocks while keeping average pooling, which left LRW accuracy at 83.14% against 83.10% [3] (Appendix)."
   **Wrong:** neither number is in the quoted source passage.
   **Fix:** add the table quote and location from [3] with both accuracies, or drop the numbers.

7. **Sentence:** "Its vocabulary size is untested: BPE is called worse with no number (Sec. 4.2), and the field settled on 1,000 to 5,000 units."
   **Wrong:** no quote shows the paper calling BPE worse. "The field settled" rests on two systems from one group ([4], [5]).
   **Fix:** quote the Sec. 4.2 sentence about BPE. Replace the last clause with "the two later systems cited use 1,000 [4] and 5,000 [5] units".

8. **Sentence:** "Standard, because FastLR split LRS2 words into a 1k byte-pair vocabulary and found BPE helped, to 75.7% WER [2] (Appendix)."
   **Wrong:** one prior use in a high-WER non-autoregressive model makes the unit not new; it does not make it standard. The review's own usual-approach line says characters were the norm in 2021. The label and its reason do not agree.
   **Fix:** "Not new, so standard by the verdict rules: FastLR already used a 1k BPE vocabulary on LRS2 [2] …". If the rules separate "not new" from "standard", keep the label and state the rule that applies.

9. **Sentence (table, M04):** "Silent video of spoken sentences".
   **Wrong:** the test material is voiced speech with the audio discarded, not silent speech.
   **Fix:** "Video only (audio not used) of voiced speech".

10. **Sentence (table, M12):** "WER across unequal training data | … | not reported".
    **Wrong:** the paper reports WER, so "not reported" does not describe the problem the review raises, which is training hours that are not matched.
    **Fix:** use the verdict label for an uncontrolled or confounded comparison (for example `behind` or the rule-defined equivalent), with the reason "training hours not matched (Table 1)".

11. **Sentence:** "Inherited components are standard: GPT-2 rescoring (M07) adds 1.1 points; all-n-gram training (M03) equals a curriculum, 30.92 against 30.91% (Sec. 4.4); TEDxext uses YouTube ASR captions (M02) …"
    **Wrong:** "GPT-2", "30.91" and "YouTube" are not in the quotes. Only 1.1, 30.92 and "imperfect ASR transcriptions" are.
    **Fix:** extend the claim-table quotes to cover these three items, or remove the unquoted specifics.

## Central claim and confounds

The strongest confound is the difference in training data (389 to 31,000 h, partly non-public). The review handles it well for the paper's own SOTA claims, but it ignores the same confound in its own Auto-AVSR comparison (fix 4). The M06 "ahead" verdict rests on the matched in-paper ablation and a second task, which is sound. The FastLR rebuttal of "first use" is fair and well supported.

## Scores

- Procedure: 6/10. The claim table is complete in form. Several rows quote text that does not carry the claim (rows 23 and 24 contradict or miss it), and the SOTA search missed lower published WERs.
- Final text: 6/10. The positions are clear and mostly well grounded. One unsupported code claim, one unsupported single-run claim and one over-attributed comparison need correction before publication.
