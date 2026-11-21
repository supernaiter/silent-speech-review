# Independent evaluation: Brain2Speech-Net review

Date: 2026-11-21. Fallback evaluator (claim table only). Sources were not re-opened. The evaluator checked each claim against the claim-table quote and location. Notes marked "evaluator knowledge" come from the evaluator's own background and were not checked against a source.

## Claim checks

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper changes M06 (phoneme-logit bottleneck, deep-HMM) and M08 (VITS decoder) | Row 1, t1–t3 | correct | The quotes support the one-pass design, phoneme logits and the left-to-right HMM. M02 (VITS pseudo-targets) is also new to the paper. It is listed in the table but not in the Verdict's "two components". |
| 2 | Alignment uses evidence from the end of the utterance; [2] causal within 10 ms | Rows 2, 6, t73, c24 | correct | t73 ("until termination at EOS") supports acausal alignment. c24 supports 10 ms. |
| 3 | Unseen-sentence WER 2.3x the 5-gram + LLM cascade (0.472 vs 0.206) | Row 3, t25, t27 | correct | 0.472 / 0.206 = 2.29. The column alignment (third WER column = held-out) is inferred from row shapes. "Inference" is not needed for a plain ratio. |
| 4 | Intelligibility rests on a 1–5 rating and ASR | Row 4, t39, t23 | correct | t39 supports the 1–5 rating. No quote names the ASR system (Whisper), which the review names elsewhere. |
| 5 | Usual approach M06: 24 of 84 slot-filled, frame-level generation; 87 pattern match | Rows 5, 29, 30 | insufficient evidence | The text gives "24 of 84 (slot-filled)". The component table gives "pattern match 87". Appendix row 29 gives 7,345 slot-filled. The denominators are not reconciled. |
| 6 | [2]: 43.75% median listener WER on participant T15 (2025) | Row 7, c20 | correct (number); insufficient evidence (participant, "open transcription") | c20 gives the number. The quote names neither T15 nor open transcription. Both match the evaluator's knowledge of [2]. |
| 7 | [5]: 5.24% "on the same benchmark with causal 10 ms outputs, simulated offline" | Row 7, c27, c28 | insufficient evidence | c27 supports only "naive listeners ... 5.24%". c28 is cited, but no quote is given for "same benchmark", "causal 10 ms" or "simulated offline". |
| 8 | Target's 0.472 is "Whisper WER" on "another participant [6]" | Row 8, t27, t10, t23 | insufficient evidence | t10 ("256 motor-cortex channels") names neither the participant nor the ASR model. |
| 9 | "Three prior works in the topic table meet this causal condition" | Row 9, c30, t75 | insufficient evidence | Only [3] is named. The other two are not identified. t75 supports "cites Wairagkar for prosody". |
| 10 | RTF 0.532 is throughput on whole utterances | Row 10, t27, t65, t74 | insufficient evidence | The code locator (scripts/synthesize.py) has no quote. t65 gives only the RTF value. |
| 11 | M08 usual approach: neural vocoder 51 of 180 | Rows 11, 33, 34 | correct (as tally) | Consistent with the Appendix. |
| 12 | [2] uses an LPCNet vocoder | Row 13, c33 | correct | |
| 13 | MCD 5.522 vs DSU 6.181 dB | Row 14, t27, t26 | correct | "Fixes one voice" and "no seeds" have no quote. They are absence and inference claims. |
| 14 | M02 usual approach: 56 pattern match; cued-text TTS [2]; reference speaker [7] | Rows 15, 37, 38, c26, c32 | correct (examples); wrong (count consistency) | Appendix row 37 gives 31 slot-filled and row 38 gives "of 32 (slot-filled)", which contradict each other. The most common slot-filled kinds are "other" and paired audio, not TTS targets, so "follows this" is not backed by a most-common count. |
| 15 | One VITS supplies targets, decoder, MCD reference; reference WER 0.025 | Row 17, t9, t11, t28, t71 | correct | t28 supports 0.025. That the targets and decoder use the same VITS model is a reasonable reading of t11 and t71. |
| 16 | M12 usual approach: 29 text-verified studies, crowd workers 15; [8] 31% with 25-word pool | Rows 18, 41, 42, c31 | correct ([8]); wrong (count consistency) | c31 matches. The text says 29 studies, while the component table and Appendix say 37 pattern match (plus 66 full-text-only). |
| 17 | MOS 3.34 read as "intelligible" | Row 21, t38 | correct | "About half the words are wrong" is arithmetic from 0.472, so it does not need the "inference" label. |
| 18 | "Faster than real time" rests on RTF without hardware or timing endpoints | Row 22, t4, t48, t73 | correct | The absence claim is reasonable. First-audio latency is correctly labelled as inference. |
| 19 | Held-out WER 7x seen-set (0.472 vs 0.068); cascade about fourfold (0.059 to 0.229) | Row 23, t27, t32, t24 | correct (first ratio); insufficient evidence (cascade) | 0.472 / 0.068 = 6.9. No quote supports 0.059. The comparator here is the 5-gram cascade (0.229), while the Verdict uses the 5-gram + LLM cascade (0.206). |
| 20 | Released Phase 1 config selects the checkpoint on the official test split | Row 24, t57, t46 | insufficient evidence | This is the review's most serious charge. The quotes say only that Table 1 reports the test split. The code lines (train_phase1.py:87-94, config 6-8) are cited but not quoted. |
| 21 | λCTC 0.1 (Sec. 5) vs 0.3 (released config); 5.71 h vs 5.2 h | Row 25, t19, t61, t11, t12 | wrong (quote); partly correct | The quote given for the config (t61) is the Sec. 5 sentence, which says 0.1. No quote shows 0.3. t11 supports 5.71 h. No quote is shown for 5.2 h (t12). |
| 22 | M05: "4 arrays, 256 features" | Component table, t10 | insufficient evidence | t10 says "256 motor-cortex channels". In [6] (evaluator knowledge) only the two area-6v arrays were used for decoding, so "4 arrays" may overstate the input. |
| 23 | [5] labelled [concurrent] | Ref 5, title year | correct in text; missing in table | [5] (June 2026) falls within 6 months of the target (Sept 2026). The component table rows M02 and M08 cite "5.24% [5]" without the label. |
| 24 | Reference [5] DOI 10.64898/... | Ref list | insufficient evidence | This is an unusual prefix for a bioRxiv preprint. It should be verified. |
| 25 | Title and version | Header, ref 1 | insufficient evidence | The header title ("Fast and Intelligible ... Without Text Decoding") differs from the record's slug ("Intelligible Real-Time ..."). Ref 1 says "arXiv v2". The review does not say which version the quotes come from. |

## Central claim, confounds and position strength

- **"Real-time" is judged by a different definition.** The authors use "real time" to mean RTF < 1 against the cascades. The review judges it by causal first-audio latency. The review partly handles this: it says RTF is throughput and labels latency as inference. However, the M06 verdict "behind" compares the target against a causal system [2] on a property the authors did not claim to measure. That position is acceptable only if the review states plainly that the authors define "real time" as throughput.
- **WER against the cascades.** The cascades decode text with an LM. The target avoids text decoding by design. The 2.3x gap is a correct number, but it reflects the absence of an LM as much as the design of the synthesis step. The review does not say this.
- **M12 "behind, against what is typical of the field".** The counts given (29 or 37 listener-transcription studies, against 6,960 slot-filled studies for evaluation) do not show that listener transcription is typical. They show it is used in a minority of studies. Either give the denominator for synthesis-only studies or soften the verdict.
- **Better or more recent work for M06.** Evaluator knowledge, not checked: Littlejohn et al., "A streaming brain-to-voice neuroprosthesis to restore naturalistic communication", Nature Neuroscience, 2025. It reports causal streaming synthesis from ECoG at roughly 80 ms decoding increments. It is prior work for the causal condition and is missing from the comparators.

## Required fixes (ordered by impact)

1. Row 24 (checkpoint selected on the test split): quote the exact code and config lines in the claim table, or drop the allegation.
2. Row 25 (λCTC): replace the t61 quote with the config line that shows 0.3, and add the Sec. 6 quote for 5.2 h.
3. M12 verdict: reconcile 29, 37 and 66 into one count with its denominator. Then either show that listener transcription is the typical test among synthesis studies, or downgrade "behind".
4. M06 state of the art: quote [5] for "same benchmark", "causal 10 ms" and "simulated offline", or cut those words.
5. M06 "three prior works": name all three with locators, and add Littlejohn et al. 2025 (streaming ECoG synthesis) as a causal comparator, or say why it is excluded.
6. Row 23 (held-out against seen set): quote the cascade's seen-set value (0.059), and use the same cascade (5-gram or 5-gram + LLM) as the Verdict.
7. M06 and Verdict on "real time": say plainly that the authors define "real time" as RTF < 1, and that the "behind" verdict concerns causality, not their stated metric.
8. Rows 4 and 8: add quotes that name the ASR model (Whisper) and the participant or dataset behind the target's WER.
9. M05 row: verify "4 arrays" against "256 motor-cortex channels" (t10), and correct it if only the area-6v arrays are used.
10. Row 10: quote the synthesize.py lines that show RTF is computed on whole utterances.
11. M02 Appendix: fix the 31 against 32 contradiction. Also state that the most common slot-filled kind is not TTS targets, or rephrase "follows this".
12. M06 counts: make the text ("24 of 84, slot-filled") and the component table ("pattern match 87") use the same count type.
13. Title and version: confirm which arXiv version the quotes come from, and make the header title match it.
14. Component table: add [concurrent] to the [5] entries in rows M02 and M08.
15. Remove the "inference" hedges from plain arithmetic (the 2.3x ratio in the Verdict, and "about half the words are wrong" in M12).
16. Reference [5]: verify the DOI prefix 10.64898.

## Scores

- Procedure: 6/10. Most numbers trace to quotes, but the two most serious charges (selecting the checkpoint on the test split, and the λCTC mismatch) lack the quotes that would carry them, and several counts contradict each other.
- Final text: 6/10. The position is clear and the comparators are mostly correct. The M06 and M12 "behind" verdicts are stronger than the stated evidence, and one causal comparator is missing.
