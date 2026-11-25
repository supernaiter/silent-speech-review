# Evaluator: a language model separate from the writer

Date: 2026-11-25. Input: `compact.md` (review, references, claim table) only; sources were not re-opened. Points that rest on outside knowledge I could not locate are marked "unverified".

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | The target changes the back-end (ResNet-18 + Conformer, end-to-end) and the LM (Transformer replacing RNN) | CT 1 (Abstract), CT 12 ([7] RNN-LM) | correct | |
| 2 | Raw-pixel and raw-waveform end-to-end AV training predates the target [2] | CT 2, c01 | correct | [2] is ICASSP 2018, LRW. |
| 3 | The Conformer step is a single LRS2 visual-only ablation that also swaps the decoder, 46.2 to 42.4 (8.2% rel.) | CT 9, t47/t48/c19 | correct | 3.8/46.2 = 8.2%. |
| 4 | End-to-end training 63.5 to 50.9 is the larger step | CT 10, t41 | correct, quote thin | t41 gives the 12.6 delta. The cited c20 is the Conformer row and does not hold 63.5 or 50.9. |
| 5 | LM step 42.4 to 37.9, 4.5 points (10.6% rel.) | CT 15, t44/t49 | correct | 4.5/42.4 = 10.6%. |
| 6 | Raw waveform ties filterbank at 4.3%, at most 7.5 points ahead at -5 dB babble | CT 11, t63/t64/c21 | correct | "One run per curve" is an absence claim and no quote shows it. |
| 7 | The "large margin" LRS3 visual-only claim is contradicted by RNN-T 33.6% | CT 4/21, c18/c17 | insufficient quote | c18 is cut off mid-sentence. In §5 the authors probably mean other methods trained on public data, and they state the 52x data gap to [19] themselves (t98). See Fix 1. |
| 8 | 43.3 vs 33.6 is a 29% relative deficit | CT 21 | correct (inference) | 9.7/33.6 = 28.9%. |
| 9 | Audio-only and AV gains over RNN-T are 2.5 and 2.2 points (4.8 and 4.5 vs 2.3) | CT 20, t96/t86/t93 | correct | |
| 10 | RNN-T was scored on 1,436 utterances, the target on 1,321 | CT 19, c14/c31 | correct | This is a real comparability point and the review handles it well. |
| 11 | TM-seq2seq 48.3% on LRS2 is its with-LM figure | CT 16, c10 | correct | The column header is not quoted, but 49.8/48.3 matches the no-LM/+extLM pair in [8]. |
| 12 | The "6x fewer training data" comparison | CT 16, t71 | correct | The target's 39.1% (Table 3, LRS2 V) differs from the 37.9% at the end of the Table 2 ablation (LRS2 V, +LM). The review does not mention this gap. See Fix 4. |
| 13 | v0.0 rows 30.4/1.3/1.2 are called new SOTA although the authors concede speaker overlap | CT 25, c34/t99 | correct | The review credits the concession to the authors, so this is fair. |
| 14 | 595 h vs 31,000 h | CT 22, t98 | correct | 157 + 438 = 595. |
| 15 | Transformer LM on 16.2 M words | CT 13, c32 | correct | |
| 16 | LP Conformer: 12.8% VSR, 0.9% AVSR, 100k h, "2023" | CT 6, c27 | number correct, year inconsistent | The text and the table say 2023, but reference [5] says ICASSP 2024. |
| 17 | Whisper-Flamingo 0.76% LRS3 AVSR (2024) | CT 6, c28 | correct | Possibly beaten later: MMS-LLaMA (Yeo et al., 2025, arXiv:2503.11315) reports about 0.72% (unverified). Both numbers rest on very large audio pre-training, and the review does not say so (cf. the "non-public" caveat it gives [5]). |
| 18 | 30.5- and 1.5-point gaps to SOTA | CT 7 | correct (inference) | |
| 19 | Auto-AVSR 19.1% from 3,448 h; "later gains came from data, not architecture" | CT 3, c23/c25 | number correct, inference too strong | See Fix 2. c25 describes the audio front-end only. |
| 20 | USR 2.0 17.6% LRS3 VSR without an external LM (ICLR 2026) | CT 14, c26/c30 | correct as quoted | "Later systems drop the external LM" ignores the LLM-decoder line (VSP-LLM 2024, Llama-AVSR 2024/25), which moves the LM into the decoder. Venue and year unverified. |
| 21 | Neural LM or LLM rescoring is "the most common" use-time design (143 of 633) | CT 12/40, Appendix M07 | insufficient evidence | The Appendix gives no counts for n-gram LM or for no external LM, so "most common" cannot be checked. |
| 22 | RNN-T "reports every WER with a 95% CI" | CT 18, c15 | insufficient quote | c15 defines CI but does not show it is given for every WER. |
| 23 | Babble noise used in training and test (NOISEX) | CT 24, c33 | insufficient quote | c33 is cut off before the verb. "No repeated runs" is supported only by "trained for 50 epochs" (t29), which does not show it. |
| 24 | "alpha not given" (M03) and question 2 | no CT row | insufficient evidence | This is an absence claim with no location. Check Sec. 4 (Experimental settings) and the decoding equations before keeping it (unverified: I believe the paper states the CTC weight). |
| 25 | Reference [1] listed as an arXiv preprint | References | wrong | The target appeared at ICASSP 2021 (pp. 7613-7617, doi:10.1109/ICASSP39728.2021.9414567). The header, Verdict and reference list should cite the venue version; "read as arXiv v1" can stay. |

## Numbered findings (required fixes, by impact)

1. **The "main overreach" may rest on a misread scope (Verdict, Where the claims outrun, CT 4/21).** The quote c18 is truncated. In §5 the authors set the RNN-T row apart as trained on 52x more data (t98), so "outperforms other methods by a large margin" most likely refers to publicly trained methods. Quote the full sentence and the sentence before it. If the scope is public-data methods, change the point from "contradicted" to "unqualified wording". Then it is no longer the review's main overreach, and the Verdict's headline criticism has to change.
2. **"Later gains came from data, not architecture" (Verdict) is stronger than its evidence.** It compares one same-group model at 3,448 h with the target at 595 h, so data, augmentation and training recipe all change at once. Ma et al. 2022 ("Visual speech recognition for multiple languages in the wild", Nature Machine Intelligence) improved LRS3 VSR at comparable public-data scale through the recipe alone: about 31-32% vs 43.3% (unverified value). Either soften the sentence to "largely from data (inference)" or drop it.
3. **The Conformer novelty claim and the "standard" verdict for M06 pull against each other.** The review says no dated ledger study used a Conformer before the target, which reads as a first-use claim, yet it rates M06 standard. Say which verdict rule decides this: for example, that the Conformer was already standard in audio ASR, which needs Gulati et al., Interspeech 2020, cited as the deciding prior; or that the effect is confounded with the decoder swap. Without this, a reader cannot tell why the first use of the field's now second-most-common encoder is "standard".
4. **The review misses a gap between two of the target's own numbers.** The Table 2 ablation ends at 37.9% (LRS2 visual-only, + Transformer LM), but the visual-only row of Table 3 on LRS2 is 39.1% (t71). Check whether the two use different data or settings. Either way it bears on question 1 (which rows use the LM) and on the "6x fewer data" comparison.
5. **Bibliography.** [1] should be cited as ICASSP 2021 (see row 25). [5]: the text and the component table say 2023 while the reference says ICASSP 2024; pick one and use the publication year consistently.
6. **The "most common" LM design (M07 Usual approach) lacks comparator counts.** Add the Appendix counts for n-gram LM and for no external LM, or say "a common design".
7. **The M07 state-of-the-art line is one-sided.** Add the LLM-decoder line (VSP-LLM, Llama-AVSR) next to "drop the external LM". Note also that the best VSR result the review cites (12.8%, [5]) is the lower WER and does not come from [9].
8. **The M12 / AVSR state-of-the-art lines need a pre-training caveat.** Whisper-Flamingo's 0.76% depends on Whisper's large-scale audio pre-training. MMS-LLaMA (2025) may be lower at about 0.72% (unverified).
9. **Some absence claims rest on non-supporting quotes.** "One run per curve", "no repeated runs" (t29 says only "50 epochs"), "alpha not given" (no row) and "every WER with a CI" (c15) each need a location or softer wording.
10. **Claim-table hygiene.** CT 10 cites c20 (the Conformer row) for the 63.5 to 50.9 step. Add the two Table 2 rows that hold those values.

## Fairness, chronology, confounds

- No [later] work is treated as prior work or as a missed citation. All of [3], [5], [6] and [9] postdate the target by more than 6 months and are labelled [later].
- Strongest confounds: the decoder swap folded into the Conformer step, RNN-T's 52x more data, and different LRS3 test versions. The review handles all three, which is its main strength. The remaining confound is unstated LM use per row (Finding 4).
- Speaker overlap in v0.0 is credited to the authors, not presented as the review's own finding.

## Scores

- Procedure: 7/10. Most claims are traceable and the arithmetic is right, but several quotes are truncated or do not show the claim, and the headline overreach rests on a cut-off quote.
- Final text: 7/10. The positions are clear, but the main-overreach framing, the "data not architecture" inference and the [1] venue need fixing.
