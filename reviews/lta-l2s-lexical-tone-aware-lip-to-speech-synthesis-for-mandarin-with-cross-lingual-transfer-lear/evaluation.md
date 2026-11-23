# Independent evaluation: LTA-L2S review

Date: 2026-11-23. Fallback evaluator (claim table only): one pass over the compact review and its claim table, with no sources reopened. Outside knowledge is marked "unverified" where its year, venue or value could not be located.

## Claim checks

| No | Claim (short) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Three changed components (M03, M02, M06), all standard | Claim row 1 (t2, t3, t13) | correct | Quotes show English pretraining, ASR-fine-tuned units and the F0 flow sampler. |
| 2 | CER 61.2 / TER 40.9 lowest against five baselines (Table 1) | Rows 2, 4 (t34, t38, t88) | insufficient evidence | The values match t34. The baseline list in t88 is cut after "Intelligible [8] and", so the fifth baseline and the count of five cannot be checked from the quote. |
| 3 | Random init 74.6 vs Intelligible 74.9 | Row 2 (t54, t38) | correct | |
| 4 | Tone variants move CER 0.3 to 3.2 points "in single runs" | Row 2 (t51, t55) | partly wrong | 61.5 - 61.2 = 0.3 and 64.4 - 61.2 = 3.2 are right. "Single runs" goes further than the evidence: the paper reports no repeats (row 11, t58), but that does not show only one run was made. |
| 5 | w/o pitch leaves TER at 40.9, "so its own tone metric does not support the tone-aware label" | Rows 3, 11 (t51, t48, t55), row 1 (t3) | position too strong | The numbers are correct. The paper also ties the tone-aware claim to the ASR-fine-tuned units (Abstract, t3), and the HuBERT-unit variant has higher TER (42.8 vs 40.9, Table 4). TER fails to support the pitch predictor, not the whole label. The DNSMOS drop without pitch (3.200 to 2.731) also shows the predictor does something. |
| 6 | V2SFlow not compared; FA-GAN not cited | Row 4 (t88, t89) | insufficient quote / partly correct | The claim that FA-GAN is missing from [1]-[35] is supported. The V2SFlow claim depends on the cut baseline list (see No 2). |
| 7 | "FA-GAN, the other CN-CVS study" | Row 4; Appendix M12 | scope issue | The Appendix scopes this to the wiki population. The Verdict states it generally. The CN-CVS dataset paper (Chen et al., ICASSP 2023) appears to include video-to-speech baselines on the corpus (unverified, medium confidence). |
| 8 | M03 usual approach: 43 / 21 / 19 of 468; AV-HuBERT Base, 1,759 h English | Row 5 (t8); Appendix | correct counts; insufficient quote for "Base" | t8 gives 1,759 h of English but does not name the Base size. 43 of 468 (about 9%) is the most common named design, not a majority design, so "usual approach" should say so. |
| 9 | CMLR CER: English-only 16.2, Mandarin-only 22.6, six-language 15.8 [4] | Row 6 (c44, c27, c26) | correct | The last column matches all three rows. Reading "Monolingual" as Mandarin-only fits CMLR. Lower CMLR CERs from later recognition work may exist (unverified); the line is cross-task (recognition) by design. |
| 10 | "Random init raises CER from 61.2 to 74.6, 18% relative, against 28% in recognition" | Row 7 (t53, t54, c44, c27) | wrong (calculation framing) | 13.4 / 74.6 = 18.0% and 6.4 / 22.6 = 28.3% are reductions measured from the worse system. A rise from 61.2 is 21.9% relative (inference). Change the wording to "pretraining lowers CER by 18% relative to random init" or give 21.9%. The baselines differ (random init vs Mandarin-pretrained), and the review says so. |
| 11 | Multilingual beat English-only (Sec. 5.2 of [4]) | Row 8 (c46) | correct | |
| 12 | M02 counts 23 / 12 of 54; layer 9, 2,000 clusters | Row 9 (t9, t10, v4, v3) | correct | The V2SFlow HuBERT tokens and pitch target are supported. |
| 13 | V2SFlow 28.5% WER, LRS3 unseen speakers | Row 10 (v5, v7) | correct | Later or stronger LRS3 video-to-speech results may exist (for example text-guided diffusion systems such as LipVoicer); unverified, so not a required fix. |
| 14 | ASR-fine-tuned target 1 of 54; HuBERT 64.4 vs 61.2 | Row 11 (t55, t53) | correct | |
| 15 | Pitch predictors "since VCVTS (2022) [5]" | Row 12 (t13 only) | insufficient quote | The only quote is from the target. Nothing from [5] supports pitch prediction or the "since" dating. |
| 16 | Rectified-flow F0 and flow-matching postnet | Row 13 (t79, t4, t80) | correct | |
| 17 | V2SFlow decomposes content, pitch and speaker and uses an RFM decoder | Row 14 (v1, v2, v5) | correct | |
| 18 | FA-GAN 43.19% WER, single speaker | Row 15 (f1, f2, f3) | correct | The column header of 49.70 / 43.19 is not quoted, but the values are consistent with WER. |
| 19 | Target "keeps V2SFlow's decomposition"; V2SFlow absent from Tables 1-2 | Row 16 (v1, t12, t88) | mostly correct | "Keeps" implies descent from V2SFlow, which the target does not cite. "Shares" is the accurate word. Absence from the tables depends on No 2. |
| 20 | Removing pitch leaves V2SFlow WER at 28.5 | Row 17 (v6) | insufficient quote | The row label is "w/o cp". No quoted legend says that "cp" means pitch removal. |
| 21 | Postnet: DNSMOS 2.942 to 3.200; w/o postnet best CER 61.0, TER 40.7 | Row 18 (t49, t48) | correct | |
| 22 | M11 counts; SVTS uses real-audio ASR transcripts as reference | Row 19 (c10) | correct | |
| 23 | V2SFlow ground-truth WER 2.5; Intelligible 4.2 / 2.5, Vougioukas 4%, SVTS 0.1% | Rows 21, 22 (v8, c37, g1, c11) | correct | The empty ground-truth row in Table 1 (t40) supports "behind". |
| 24 | VCA-GAN 49.70% WER in [3] vs 96.5% CER in Table 1 | Row 23 (f2, t35) | correct | It is clearly framed as protocol-bound. |
| 25 | TER computed from FunASR text via g2pM | Row 25 (t21) | correct | This is the review's strongest point. |
| 26 | "Significantly" untested; MOS ± undefined | Row 27 (t5, t64) | insufficient quote for ± | t64 does not show the ± column. |
| 27 | Sec. 4.3 says PER where Table 4 says TER | Row 28 (t71) | correct | |
| 28 | Speaker-embedding audio unstated | Row 29 (t14) | correct | |
| 29 | Component table: M07 "Speaker embedding" under Lexicon and LM | Component table | wrong | A speaker embedding is not a lexicon or language model. The cell should read "none". |

Central claim and confound: the strongest confound is the starting point. The gain over Intelligible equals the random-init gap, and the review handles this well (Verdict; "Attribution"). A second confound is not raised: whether the baselines were retrained on the same CN-CVS split with FunASR labels. Every system is at CER of 61% or more, so these are absolute differences between largely unintelligible outputs. The review implies this but could state it.

Fairness: V2SFlow (arXiv 2024-11) and FA-GAN (2024) are more than 6 months older than the target (2025-09), so treating them as prior work is fair. No later work is treated as missed.

Verdicts: M11 "behind" is backed by named comparators that report real-audio error ([2], [6], [7], [8]) and by an Appendix count. The review frames it against the best comparable work, not the majority (20 of 165), which is correct. There is no "ahead" verdict.

## Required fixes (ordered by impact)

1. Verdict, "so its own tone metric does not support the tone-aware label": narrow this to the pitch predictor. The unit target, which the abstract also ties to tone, lowers TER (40.9 vs 42.8 for HuBERT units, Table 4).
2. M03, "raises CER from 61.2% to 74.6% ..., 18% relative": the 18% and 28% are reductions measured from the worse system. Reword as "pretraining lowers CER by 18% relative (from 74.6%)", or give the rise from 61.2% as 21.9% (inference).
3. Verdict, "FA-GAN [3], the other CN-CVS study": scope this to the wiki population, as the Appendix does, or check the CN-CVS dataset paper's own video-to-speech baselines.
4. Verdict, "in single runs": replace with "with no repeats reported" to match the evidence (Sec. 3.2).
5. M06, "Removing pitch changes neither V2SFlow's WER": quote the legend of Table III in [2] that defines "cp", or drop the V2SFlow half of the sentence.
6. Verdict and M06, "V2SFlow ... is not compared" / "not V2SFlow in Tables 1-2" and "five baselines": quote the full baseline list from Sec. 3.3 (t88 is cut off).
7. Component table, M07: replace "Speaker embedding" with "none". It is not a lexicon or language model.
8. M06 usual approach, "pitch predictors in 9, since VCVTS (2022) [5]": add a quote from [5] that supports pitch prediction from video, or drop "since".
9. M03 usual approach: say that AV-HuBERT is the most common named design (43 of 468), not the typical one, and support "Base" with a quote or remove it. Change "keeps V2SFlow's decomposition" to "shares" in M06.

## Scores

- Procedure: 7/10. The claim table is dense and nearly every number has a located quote. A few quotes are cut off or come from the wrong source (Nos 2, 15, 20).
- Final text: 7/10. The TER-from-transcripts and initialization-confound points are sharp. One position is too strong, and one relative-change figure is framed wrongly.

Strengths, briefly: the review separates protocol-bound numbers well, identifies the initialization confound behind the headline gain, and catches that TER is scored from recognized text rather than from the generated F0.
