# Evaluator: a language model separate from the writer

Date: 2026-11-24. Target: LipVoicer (Yemini et al., ICLR 2024, arXiv:2306.03258).
Input: the brief (`wiki-context/skill-draft/references/evaluator-brief.md`) and `compact.md` (review plus claim table). No other writer files were read. No paper source text was opened (access attempts to the target text were refused), so every check below is made against the claim table's quotes and locations, plus outside knowledge marked "unverified" where I cannot locate it. SKILL.md was not available to me; for the `ahead` rule I apply the brief's paraphrase (ledger count in the Appendix, deciding priors named, effect repeated) together with the caller's reading (design count, deciding prior read, effect shown against the field's alternatives).

## Claim check table

| # | Claim (short) | Where checked | Result | Note |
|---|---|---|---|---|
| C1 | Three changed components M07/M02/M06 | Claim row 1 (Sec. 1, Sec. 4, App. A.4) | correct | Quotes support inference-time text use, text-free MelGen, ASR trained on GT text. |
| C2 | "No earlier study among 165 uses lip-reader text at inference" | Rows 2, 5, 30; Usual approach M07; Appendix M07 | wrong as worded | The review's own evidence says earlier work ran lip-to-text plus TTS [4] (row 5 quotes the cascade row of [4] Table 3) and the Appendix counts 20 cascade hits. A cascade uses lip-reader text at inference. See Finding 1. |
| C3 | Closest design [2] is [concurrent] | Row 2 timing note (2023-08/2023-10 vs 2023-06); ref [2] | correct | Within 6 months; label applied correctly. |
| C4 | [later] AUTO-AVSR re-scores rank LipVoicer lowest in LRS3 WER [3] | Rows 2, 8, 23 | insufficient quote | Quotes give LipVoicer 20.62 and Intelligible 27.73 only. SLD-L2S's own row is not quoted, so "lowest" in [3] is not shown. |
| C5 | 21.4 vs 19.1 vs 5.4 (GT) vs 86.2 (no guidance) vs Lip2Speech 57.4 | Rows 3, 9-11, 20 (Tables 4, 6, 7) | correct | Numbers match the quoted rows; "worse than" direction correct. The dataset (LRS3) for Table 4/6 rows is not in the quote, but the location is given. |
| C6 | Synthesizer adds 2.3 to 5.8 points (inference) | Row 11 | correct | 21.4-19.1=2.3; 38.1-32.3=5.8; 5.4-0=5.4. Labelled inference as required. |
| C7 | "No baseline received that text" | Row 4 (Sec. 5 Baselines) | correct (thin) | Supported by the baseline list; consistent with the authors' setup. |
| C8 | LipAdapter 21.2% vs LipVoicer 21.4%, Whisper-Large [5] | Row 7 | insufficient evidence for the comparison | LipVoicer's 21.4% in [5] is identical to LipVoicer's self-reported number under Ma et al. (2023) ASR (Table 7). It is likely copied rather than re-scored with Whisper-Large; the 0.2-point gap may mix two evaluators. See Finding 4. |
| C9 | WYS 23.73 vs LipVoicer 22.24 under AUTO-AVSR [6] | Rows 8, 14 | insufficient quote | Column header and ASR for [6]'s table are not quoted; WER column assumed to be the last. |
| C10 | Lip2Speech uses text only in training losses [7] | Row 12 | correct | CTC loss quote supports it. |
| C11 | Hegde et al. [2] report no WER of the generated speech | Row 12 ("Tables 1-4") | insufficient quote | Absence claim rests on a table range with no header quote. Unverified from my side; must be confirmed against [2]'s table headers. |
| C12 | M02 usual approach counts 31/64, 13, 10 | Rows 13, 34 | correct (ledger) | Exact tallies; not audited per brief. |
| C13 | Guiding ASR 6.1% -> output 76.3% (Table 11) vs "without requiring any re-training" | Row 16 | correct numbers, weak framing | Numbers match. The authors' sentence is about swapping in *improved* models; a worse ASR degrading output does not contradict it. See Finding 7. |
| C14 | MelGen 400-step DDPM with CFG on video | Row 18 | correct | T = 400 quoted. CFG detail relies on Appendix C.1 without a quote; minor. |
| C15 | V2SFlow 28.5% LRS3 WER without text [9] | Row 19 | correct | V2SFlow-V row quoted. |
| C16 | 16 annotators per sample | Row 22 | correct | Quoted. |
| C17 | Intelligibility 3.44 vs GT 4.38 | Row 25 | insufficient quote (header) | Column order not quoted; plausible that the first column is Intelligibility given the quoted instruction order. |
| C18 | Evaluation ASR = lip reader source (Ma et al. 2023) | Row 24 | correct | Both quotes present. |
| C19 | "Words are scored only by an ASR from the same work as the lip reader" (Verdict) | Rows 24, 27; Verdict | wrong as worded | The review itself reports a ReVISE-protocol ASR score (33.2%) and a Whisper-Large score in [5]; plus listener ratings. See Finding 6. |
| C20 | ReVISE: ASR at 6.4% instead of reported 5.6% | Row 27 | insufficient quote | 6.4% is quoted; 5.6% is not. The authors state this caveat themselves. |
| C21 | "More natural and synchronized" outruns evidence (App. E.5) | No claim-table row | no quote | Needs a quote from App. E.5. |
| C22 | Weights from grid search on unstated data; released ASR config evaluates on LRS3 test | No claim-table row | no quote | An implied test-set-tuning charge with no quote or code location. See Finding 5. |
| C23 | M07 table row "Video only, no text (pattern match 150)" | Appendix M07 | inconsistent | 150 appears nowhere in the Appendix; not derivable from 20/15/7 without stated overlap. |
| C24 | Bibliography [4], [7], [8] | Outside knowledge | correct | MM'22 arXiv:2209.00642; ICASSP 2023 arXiv:2302.08841; ICML 2022 arXiv:2111.11755. |
| C25 | Bibliography [3], [5], [6], [9], [10] | Outside knowledge | unverified | 2026 items beyond what I can locate; [9] may now carry an ICASSP 2025 venue; DiffV2S page range unverified. |

## Findings

1. **(Severe) The M07 novelty sentence is contradicted by the review's own evidence.** The Verdict says "no earlier study among 165 video-to-speech papers uses lip-reader text at inference". The M07 Usual approach line and the Appendix both say earlier work "run[s] lip-to-text plus TTS as a baseline [4]" and count 20 cascade hits. A lip-to-text plus TTS cascade uses lip-reader text at inference. The defensible statement is narrower: no earlier study *conditions a video-to-speech synthesizer on both the video and lip-reader text at inference* (here, through ASR classifier guidance). The deciding prior [4] is named and read in full, which is right, but the sentence must be narrowed so that [4] is the boundary rather than a counterexample.

2. **(Severe) The M07 `ahead` verdict does not show the effect against the field's alternative.** The design count (Appendix: 165 pattern match, 20/15/7) and the deciding prior ([4], read in full) are present. The effect is not. The only effect given is against text-free synthesizers (21.4% vs Lip2Speech 57.4%), and the review itself says this pits a lip reader against text-free systems and that the words come from the lip reader. The field's alternative for using lip-read text is the cascade of [4], and the review notes it was not run. The later LipAdapter [5], which feeds predicted text into a pretrained TTS (a cascade-like design), reaches 21.2% against 21.4%. So the evidence in the review suggests that guidance gives no measured advantage over the alternative that existed before. The M07 section also does not repeat the effect against the baseline; it repeats only the lip-reader tracking numbers. Required: either (a) downgrade to a verdict that records novelty of design without a demonstrated advantage (whatever SKILL.md calls that), or (b) keep `ahead` with an explicit limitation: "first to inject lip-reader text into a video-conditioned synthesizer; advantage over a lip-to-text plus TTS cascade with the same lip reader not shown". As written, the position is stronger than the evidence.

3. **(Severe) "Ahead at publication (LRS2, LRS3, GRID)" claims more datasets than the evidence covers.** Every M07 number in the review is LRS3. No LRS2 or GRID result is cited, and the lip reader named for inference (Ma et al. 2023) is stated for LRS2 and LRS3 only (row 4). Drop LRS2 and GRID from the verdict, or cite their tables.

4. **The LipAdapter state-of-the-art line likely compares across evaluators.** LipVoicer's 21.4% in [5] equals LipVoicer's self-reported Table 7 number under Ma et al. (2023) ASR, while the review says the comparison is "scored with Whisper-Large". If [5] copied the number, the 21.2 vs 21.4 gap mixes two ASRs. In addition, the two independent AUTO-AVSR re-scores of LipVoicer in the review differ by 1.6 points (20.62 in [3], 22.24 in [6]), so a 0.2-point margin is inside the re-scoring spread (inference). Check [5]'s table footnote; if copied, state it and say LipAdapter and LipVoicer are not separable on this evidence.

5. **The test-set-tuning implication has no quote.** "Guidance weights come from grid search and listening tests on unstated data (Appendix C); the released ASR config evaluates on the LRS3 test split" implies that hyperparameters may have been tuned on test data. There is no claim-table row, no quote from Appendix C and no file/line for the released config. Either supply the quote and the config path, or reduce it to the question already asked ("Which data and listeners selected w1, w2 and t_ASR?").

6. **"Words are scored only by an ASR from the same work as the lip reader" is overstated.** The review itself reports a ReVISE-protocol ASR score (33.2%) in the paper, and [5] and [3]/[6] re-score LipVoicer with Whisper-Large and AUTO-AVSR. The correlated-error concern is valid for the paper's main tables (row 24), but "only" is wrong. Note also that AUTO-AVSR used by [3] is Ma et al. (2023) again, so [3] does not remove the confound; Whisper-Large in [5] would, if it was actually re-scored (Finding 4).

7. **The Table 11 point argues against a claim the authors did not make.** The authors say swapping in *improved* models needs no retraining. Showing that a *worse* guiding ASR (6.1% vs 3.6%) raises output WER to 76.3% shows strong sensitivity to the guiding ASR. That is a useful point, but "yet" frames it as a contradiction. Rephrase it as sensitivity. Also quote the Table 11 row label: is the 6.1% ASR the same architecture without noise fine-tuning, or a different model? The interpretation depends on it.

8. **"Rank it lowest" in [3] is not shown.** The quotes from [3] give LipVoicer (20.62) and Intelligible (27.73) only. SLD-L2S's own row is missing. Quote the full WER column of [3] Table 1 before claiming "lowest".

9. **Ledger number 150 in the 13-component table is not in the Appendix.** "Video only, no text (pattern match 150)" for M07 is not among the Appendix tallies (165; 20/15/7). If it is 165 minus 15, say so and label it inference; otherwise add the tally to the Appendix.

10. **Hegde et al. [2] "report no WER" is an absence claim on a table range.** Quote the metric headers of [2] Tables 1-4. I believe [2] stresses accuracy of the content, so a WER-type metric there is plausible (unverified). If one exists, the "closest design" comparison should carry its number.

11. **Fairness: the M07 novelty echoes the authors' own claim without attribution.** The authors write "LipVoicer is the first method to use text inferred by lip-reading to enhance lip-to-speech synthesis" (row 1, Sec. 1). The review should say that the authors claim this and that the ledger check confirms it (in the narrowed form of Finding 1), not present it as its own finding. Likewise, the ReVISE ASR mismatch (Finding C20) is the authors' own stated caveat ("uncertain of the source of the degraded performance") and should be attributed to them.

12. **Two state-of-the-art lines name works that are not better than the target.** M02 names Watch Your Speech (23.73%), which is worse than LipVoicer (22.24%) on the review's own numbers. M12 "state of the art" is a re-score of LipVoicer, not a better evaluation protocol. If no later work beats the target on that component, say so plainly (for example "no later text-supervision design beats it on LRS3 WER; closest [6] 23.73%").

13. **Unquoted claims in "Where the claims outrun the evidence".** "MelGen without guidance is sometimes more natural, and wrong text causes synchronization lapses (Appendix E.5)" and the 5.6% ReVISE ASR figure have no quotes in the claim table. Add them.

14. **Label mismatch for M07.** The section heading says "Use-time information: lip-reader text guidance", and the 13-component table says "M07 Lexicon and LM". Use one slot name.

15. **Minor formatting.** References [2], [3], [5], [6], [7], [9], [10] repeat their timing label twice ("[concurrent] ... [concurrent]"). M12 "LipVoicer has both" follows a list of three protocols; say which two (listener test and ASR WER), and whether unseen-speaker testing applies.

## Required fixes, ordered by impact

1. Narrow the M07 novelty sentence so that the cascade of [4] is the boundary, and attribute the "first" claim to the authors (Findings 1, 11).
2. Revise the M07 `ahead` verdict: show the effect against the lip-to-text plus TTS alternative, or downgrade or qualify it, since the review's own evidence (lip-reader tracking, LipAdapter 21.2%) suggests no shown advantage (Finding 2).
3. Remove LRS2/GRID from the M07 verdict, or cite their results (Finding 3).
4. Verify whether [5] re-scored LipVoicer with Whisper-Large; otherwise state the evaluator mismatch and the re-scoring spread (Finding 4).
5. Quote Appendix C and the released config, or drop the test-split implication (Finding 5).
6. Replace "only" in the Verdict's evaluation sentence (Finding 6).
7. Quote the full [3] WER column for "lowest", and the [6] column header and ASR (Finding 8, C9).
8. Reframe Table 11 as sensitivity, with the row label quoted (Finding 7).
9. Fix the unexplained 150, the unquoted E.5 and 5.6% claims, the [2] absence claim, the SOTA lines that are not better than the target, the slot-name mismatch and the duplicate labels (Findings 9, 10, 12-15).

## Scores

- Procedure: 6/10. Ledger counts, deciding prior and read-in-full lists are in place, and the inference arithmetic is labelled. But several positions have no claim-table quote (E.5, Appendix C/config, 5.6%, "lowest" in [3]).
- Final text: 5/10. The core analysis (output WER tracks the lip reader; baselines lacked the text) is sharp and well supported. The headline `ahead` verdict contradicts the review's own Usual-approach evidence and does not show an effect against the field's alternative.

What works: the Table 7 decomposition (the synthesizer adds 2.3-5.8 points) and the w2 = 0 result (86.2%) isolate where the words come from. Those are the review's strongest contributions.
