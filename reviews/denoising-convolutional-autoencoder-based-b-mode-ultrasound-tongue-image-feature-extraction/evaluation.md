# Evaluator: a language model separate from the writer

Date: 2026-11-25. Review evaluated: `compact.md` (Li et al., arXiv:1903.00888). Sources consulted: the claim table in `compact.md`, plus the writer's notes (`notes.json`: quotes t1–t61, c1–c28, j1–j4, k1–k3) and `prep/tallies.txt`. The original PDFs were not reopened. I recomputed all arithmetic myself (x/1023 for every Table 2 value, the relative changes, and points converted to words).

## Claim check

| No | Claim (short) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper changes M06 only: DCT/FC-AE replaced by speckle-trained CAE | t6, t9, t44, Table 2 rows | correct | |
| 2 | Speckle denoising predates it [2]; "first attempt" holds only for the convolutional variant | j1, j2, t14 | correct, with a caveat | Supported by j1/j2. Whether CNN feature extraction on tongue ultrasound is itself new is not examined. See finding 7. |
| 3 | 6.17% (length 60) vs 6.45% (DCT, length 30); "at equal length the margin is 0.41 points" | t23, t34, t35, t42 | partly wrong | 0.41 is the length-60 margin. At length 30 the margin is 6.45 − 6.24 = 0.21. The Verdict and "Where the claims outrun" give only the larger figure. See finding 2. |
| 4 | Denoising adds 0.05 points over CAE | t40, t42 | correct | 6.22 → 6.17. |
| 5 | Eight new WERs are not k/1023; 6.45 and 7.72 are | c23, c9, c13, recomputed | correct | 66/1023 = 6.45%, 79/1023 = 7.72%. None of 6.58, 7.37, 7.26, 7.54, 6.22, 6.34, 6.17, 6.24 is k/1023 to two decimals. |
| 6 | Usual M06: PCA/DCT ~30 per stream; 32/13/13 of 39 [4][5] | tallies M06, c17, c18 | insufficient quote for [5] | The row cites Cai [5], but its second quote and location come from Ji et al. (doi-10.1016… Sec. 3.3), not Cai 2011. The counts match the tallies. |
| 8 | 6.17% is the lowest SSC WER in the topic tables; reference 6.45% (2018) | tallies M06/M12 | correct | Lower values in the tables (3.42%, 3.6%) are on other corpora. |
| 9 | Kimura 2020: 20.5% WER with a 65k LM [6] | k1, k2; tallies | correct, check needed | The tallies line reads "WER 20.5% (30d-DCT+SpecAug); no-aug 18.7%". If 18.7% is a WER without augmentation, "reaches 20.5%" is not the paper's best value. Verify the metric of 18.7. |
| 10 | Deep AE 7.37 → CAE 6.22, 16% relative | t36, t40 | correct | 15.6%. |
| 11 | DCT → DCAE: 6.2% relative (length 60), 3.3% relative (length 30) | t34, t35, t42, t43 | correct | |
| 12 | Denoising: 0.05 and 0.10 points, about 0.5 and 1 word | t40–t43 | correct | |
| 13 | [2] applies speckle corruption in training only, on stacked RBMs; target gives no noise level | j2, j3, t44 | correct; insufficient quote for the second half | The quote cited for "no noise level" is the Adam sentence (t7). t44 ("randomly generated speckle noises were added") is the right quote. |
| 14 | Usual M12: 1023 words, closed 5k bigram, 3 of 8 studies | c6, c10, c12, tallies M12 | correct, with a caveat | See finding 6 on a possible double count. |
| 16 | SOTA M12: 6.17%, "0.28 points below the 6.45% reference" | t42, t35 | arithmetic correct, internally inconsistent | This repeats the cross-length comparison the review criticises elsewhere. See finding 2. |
| 17 | Later studies change the LM [6] or re-record the sentences [7] | k1, k2 | insufficient quote for [7] | No quote or location from SSR7000 is given. |
| 18 | Ji: 6 ins, 8 del, 52 sub over 1023 words = 6.45% | c25–c27, c23 | correct | 66/1023 = 6.45%. |
| 19 | New values are "averages over runs or another test set" | recomputed | correct as inference | It conflicts with "unrepeated runs" in the Verdict. See finding 3. |
| 20 | Reconstruction test frames are random, so they neighbour training frames of the same utterances (inference) | t4, t45, **t53, t56** | contradicted by the writer's own notes | See finding 1. |
| 21 | "Outperforms" crosses lengths; no seed, repeat or significance test | t23, t7, t44 | correct | |
| 22 | "first attempt" omits that the criterion appears "in a paper it cites" [2] | t14, j1 | insufficient quote | Nothing in the claim table shows that the target cites Jaumard-Hakoun 2016. See finding 5. |
| 23 | Robustness claims are untested; single speaker | t19, t52, c5 | correct | |
| 24 | DCT MSE rises 86.27 → 89.03 from (5,6) to (10,6); this is impossible for a plain orthonormal truncation | t24, t25, t17 | correct as inference | The authors flag the DCT exception themselves (t17, "except with DCT"). The review's wording, "leaves unexplained", is fair. |
| 25 | §3.3 "K = 60 and 30" concatenated, yet the length-30 row equals Ji's per-stream K = 30 | t9, c28 | correct as inference; insufficient quote | The quoted target sentence is the DNN-HMM sentence. The "K = 60 and 30" wording appears only in the writer's paraphrase (t9), not in a quote. |
| M07 row | State of the art cell: "20.5% WER, 65k LM [6]" | k1 | wrong framing | See finding 4. |
| Ref 1 | Target cited as "arXiv preprint, 2019" | outside knowledge | probably incomplete | See finding 6. |

## Numbered findings (ordered by impact)

1. **Claim 20 is contradicted by the writer's own notes.** The review infers that the 30,000 reconstruction test frames "neighbour training frames of the same utterances", because they were "randomly selected" (§3.2). The writer's notes on the public code say otherwise:
   - t53 (`input data with noise.py:25-31,59-61`): the split is by directory, "first 10 directories / remaining directories".
   - t56 (`:205-213,299-305`): "validation data reused for evaluation".

   With a directory split, the test frames are probably not neighbours of training frames from the same utterances. The real problem the code shows is a different one: the data used for model selection or validation are reused as the test set. Required fix: replace the neighbour inference with the code finding, cite t53 and t56, and say that the paper's text ("randomly selected") and the released code disagree.

2. **The equal-length margin is reported selectively, and the review repeats the comparison it criticises.**
   - The Verdict and "Where the claims outrun" say "at equal length the margin is 0.41 points". That is the length-60 figure (6.58 → 6.17).
   - At length 30, the length of the 6.45% reference, the margin is 0.21 points (6.45 → 6.24, about 2 words).
   - The M06 body gives both margins. The Verdict, the bullet and the M12 state-of-the-art line ("0.28 points below the 6.45% reference") do not.
   - The 0.28 figure is exactly the cross-length comparison the review faults the authors for.

   Required fix: say "0.41 points at length 60 and 0.21 at length 30 (about 4 and 2 words)" wherever the margin appears, and restate the M12 state of the art at matched length or label it as cross-length.

3. **The review contradicts itself on repeated runs.**
   - The Verdict says "from unrepeated runs". The M12 verdict says "the same single-run reporting as Ji et al.".
   - The M12 body argues that the non-integer error counts mean the values are "averages over runs or another test set". The Questions ask the same thing.

   The paper does not report the number of runs, so "unrepeated" is not established. Required fix: use "number of runs and seeds not reported" in the Verdict and the M12 verdict, and keep the averages question.

4. **The M07 state-of-the-art cell names a worse, non-comparable result.** "20.5% WER, 65k LM [6]" is 3× the target's error rate and uses a different LM. Calling it the state of the art for the lexicon/LM component is misleading. Required fix: give "6.45% / 6.17% under the closed 5k bigram; no later result under the same LM [6][7]", or leave the cell as "–" with the Kimura result in a note.

5. **The citation link in claim 22 is not evidenced.** "a paper it cites [2]" needs the target's reference-list entry for Jaumard-Hakoun 2016 (its number and location). No such quote is in the claim table. The notes add a relevant fact the review omits: Kele Xu is a co-author of both [2] and the target (j1 condition). That makes the omission more notable, and the review could state it plainly. Required fix: add the target's citation of [2] as a quote with its location, or drop "it cites". Optionally, mention the shared co-author.

6. **The bibliographic venue is probably incomplete, and the SSC count may include the target twice.**
   - To my knowledge, this paper appeared at IEEE ICASSP 2019 (Li et al., pp. 7130–7134). This is unverified. Reference 1 cites only the arXiv preprint.
   - The M12 tally note in `prep/tallies.txt` lists "the target, Li 2019" as two separate SSC studies. If "Li 2019" is the ICASSP version of the target, the "8 unique SSC studies" and "5 recognize the SSC test sentences" counts include one paper twice, despite the rule "versions counted once".

   Required fix: check the venue. If it is ICASSP 2019, cite that version and recount M12; "3 of 8" may become "3 of 7". Medium confidence.

7. **The novelty concession may be too generous to the convolutional part.** The review accepts "first" for the convolutional variant without naming a prior convolutional feature extractor on tongue ultrasound. Two works I know of are candidates:
   - Tatulli and Hueber, "Feature extraction using multimodal convolutional neural networks for visual speech recognition", ICASSP 2017. Supervised CNN features from tongue ultrasound and lip images.
   - Xu et al., "Convolutional neural network-based automatic classification of midsagittal tongue gestural targets using B-mode ultrasound images", JASA Express Letters 2017. A target co-author is on this paper.

   Neither is an autoencoder, so the specific claim "denoising CAE" may still stand. However, "first convolutional" should not be implied without a check. Both references are unverified (year and venue from memory).

8. **The state of the art for M06 is restricted to SSC.** For the feature-extraction component, later work on other ultrasound corpora uses learned CNN encoders or raw-image models. One example is the TaL corpus baselines (Ribeiro et al., 2021, arXiv:2011.09804, in the writer's tallies at 3.42% WER on TaL1). These are not comparable numbers. One sentence saying that the field moved from fixed feature extractors to learned or end-to-end image encoders on other corpora would place the 2019 result in context. This is an optional improvement, not a correctness error.

9. **Some quotes do not match the claim they support.** Each of the following is "insufficient quote", not "wrong":
   - claim 6: the [5] row is located in Ji et al., not in Cai 2011;
   - claim 13: the "no noise level" quote is t7; it should be t44;
   - claim 17: there is no SSR7000 quote;
   - claim 25: the "K = 60 and 30" phrase is not quoted.

10. **Kimura 2020 needs a check.** The tallies record "WER 20.5% (30d-DCT+SpecAug); no-aug 18.7%". If 18.7% is a WER, then "reaches 20.5%" understates the later study's best value. The conclusion that it does not test under the closed bigram stands either way. Verify the metric of 18.7.

11. **Minor points.**
    - The DCT-MSE bullet could say that the authors flag the DCT exception themselves (t17), so the review does not appear to present it as its own discovery.
    - The verdict labels (all `standard` or `not reported` / `not applicable`) follow the rules. No `ahead` verdict needs an Appendix justification.

## Positions and fairness

- **Central confound.** The confound is the different starting point: feature length 60 vs 30, and possibly a different run protocol (non-integer error counts vs Ji's integer counts). The review identifies both. It undercuts its own point in the M12 state-of-the-art line (finding 2).
- **Chronology.** [6] and [7] are correctly marked [later] and are not treated as prior work.
- **Absence and novelty claims.** "first attempt" is handled by naming the deciding prior [2]. See findings 5 and 7.

## Scores

- Procedure: 7/10. Tallies, arithmetic and the comparator quotes are sound. However, the code evidence in the writer's own notes was not carried into the review, and it contradicts one inference (finding 1).
- Final text: 7/10. The position is clear and well argued. It needs the margin restated, the self-contradiction on runs fixed, and the M07 state-of-the-art cell corrected.
