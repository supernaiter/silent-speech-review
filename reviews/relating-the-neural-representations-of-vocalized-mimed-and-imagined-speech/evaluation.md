# Evaluation: Relating the Neural Representations of Vocalized, Mimed, and Imagined Speech

Date: 2026-11-22. Fallback evaluator (claim table only). Input: the compact review, its reference list and claim table. No source was opened. Notes marked "inference" rely on general knowledge of the literature, not on a source check.

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | One participant, 100 sentences, two repetitions (Verdict) | Row 2: t2, t3 (Sec. 2.1) | correct | Both quotes match. |
| 2 | Authors defer the direct test of the hierarchy (Verdict) | Row 2: t46 (Sec. 4) | correct | "Future research could use subspace analyses ... to directly test this hypothesis." |
| 3 | Silent trials scored against vocalized-audio targets (Verdict) | Row 3: t5 (Sec. 2.1) | correct | t5 says the vocalized audio is the stimulus representation. "No stated alignment" is an absence claim with no quote, which is acceptable. |
| 4 | Earlier work used DTW [2], [3] (Verdict, M04, M11 row) | Row 3, 7: a2, c3 | insufficient evidence | a2 supports DTW for [3]. c3 ("with the corresponding original speech from the overt condition") does not mention time warping, so the table has no support for DTW in [2]. |
| 5 | Linear model "better preserves sentence structure" is a slope, not a level (Verdict) | Row 3: t43, t53 | correct | t43 states a steeper slope (Steiger p = 1.24e-4). |
| 6 | Six pairs: nonlinear higher in three, lower in two, tied in one (Verdict) | Row 3: t29-t31, t39-t41 | correct | V-V 0.59/0.32, M-V 0.14/0.11, M-I 0.04/-0.01 are higher. M-M 0.06/0.13 and I-M 0.04/0.08 are lower. I-I 0.07/0.07 is tied. Arithmetic is right and labeled inference. |
| 7 | [2] ran rank scoring against a 10,000-shuffle null in seven patients (Verdict, null section) | Row 1, 15: c6, c2 | insufficient evidence | Seven patients matches c2. The c6 fragment "the segment label in the candidate set 10,000" could mean candidate-set size or iterations. It does not establish 10,000 shuffles. |
| 8 | Discriminability claim (Sec. 5) fails for linear mimed-to-imagined, AUC -0.01 | Row 16: t51, t30 | correct | Both quotes match. |
| 9 | Imagined-trained nonlinear: Vocalized like Imagined (p = 0.74), Mimed lower (p = 0.02, d = 0.29) | Row 17: t38 | correct | The numbers match. "Against the hierarchy" is the reviewer's reading, and it is reasonable. |
| 10 | Linear vs nonlinear confounds target (NSL vs mel-spectrogram) and null | Row 18: t5, t20, t9, t52 | insufficient evidence | NSL for the linear model (t5) and the two nulls (t9, t52) are supported. No quote shows that the nonlinear model's target is a mel-spectrogram. t20 describes only the architecture. |
| 11 | Best AUC 0.59 nonlinear vs 0.32 linear | Row 18: t39, t29 | correct | |
| 12 | No seeds or reruns stated (Sec. 2.3) | Row 19: t11 | insufficient evidence | This is an absence claim. t11 does not bear on it, so the row should be marked as absence rather than cite t11. |
| 13 | M04 usual approach: 23 of 33 (confirmed) | Row 4 | insufficient evidence | Ledger tally, outside this check. |
| 14 | [2] is ECoG reconstruction of covert reading in seven patients; [3] synthesized 58 mimed sentences | Row 5: c1, c2, a1 | insufficient evidence | Seven patients is supported. No quote shows "reading" in [2] or the count 58 in [3]. |
| 15 | Overt-trained Transformer: 46.3% TER on covert vs 46.6% covert-trained, 16 participants [4] | Row 6: k1, k2 | insufficient evidence | 46.6% (covert-trained) and 16 participants are supported. The 46.3% overt-trained figure, the central number, has no quote. "Sentences" is not supported either. |
| 16 | [2] covert loss r 0.46 vs 0.66, and a rest control | Row 8: c7, c4 | correct | c4 is truncated ("the subject remained"), but the reading is plausible. |
| 17 | "The paper gives neither" (covert loss, rest control) | Row 8 | insufficient evidence | The Verdict says only six of nine cross-pairs have both AUCs "stated" in text. Fig. 3 probably shows the full matrix (Gv on Xm, Xi), which is a covert loss relative to within-condition decoding. |
| 18 | Covert identification rank 0.55 vs chance 0.5 [2] | Row 10: c5 | correct | The quote does not say "covert". The location (Sec. 3, Fig. 11) makes it plausible. |
| 19 | [5]: 92-100% word identification vs 8% chance, five subjects; correlation and identification dissociate | Row 11: b2, b4, b1 | correct | |
| 20 | Fig. 4 "restates that dissociation at sentence level" | Row 12: t43, t53 | insufficient evidence | t43 shows AUC rising with correlation for both models, with different slopes. That is a model difference in the correlation-to-identification mapping, not a dissociation. The wording overstates the parallel. |
| 21 | Linear null permutes trials; nonlinear null circularly shifts targets | Row 13: t9, t52 | correct | |
| 22 | [6] trains nulls identically on mismatched trial pairs, LOSO; labeled [concurrent] | Row 14: e1, e2 | correct | It is about three months after the target and correctly labeled concurrent, not prior. Calling a same-group concurrent preprint "state of the art" for nulls is weakly justified. |
| 23 | M05: sEEG, 110 electrodes | No row | no quote | The number appears in the component table with no claim-table entry. |
| 24 | M03 verdict "not reported" while the cell describes per-condition ridge and CNN-RNN | Component table | wrong (internal inconsistency) | Either the training details are reported or the verdict needs a reason (e.g. no hyperparameters or splits). M11 has the same pattern. |
| 25 | "Training on mimed or imagined speech and testing elsewhere is the paper's only extension" | M04 | insufficient evidence | A novelty-type claim with no deciding prior named. Inference: cross-condition generalization between overt and imagined intracranial speech decoding in both directions was reported before (e.g. Proix et al., Nature Communications, 2022). Check before keeping the sentence. |

## State of the art and usual approach

- M04 state of the art: [4] is a reasonable ECoG overt-to-covert comparator. Inference: a stronger and later transfer result exists in microelectrode recordings: Kunz et al., Cell, 2025, "Inner speech in motor cortex and implications for speech neuroprostheses". That work decodes inner speech with attempted-speech-related decoders in several participants, including sentence decoding with a large vocabulary. Either name it as state of the art or narrow the line to "ECoG".
- M12 identification state of the art: [5] is a 12-word overt task from 2023. Inference: later reconstruction work reports listener intelligibility at sentence level, e.g. Wairagkar et al., Nature, 2025 (instantaneous voice synthesis) and Chen et al., Nature Machine Intelligence, 2024 (ECoG speech synthesis across many participants). Consider one of these, or restrict the claim to "word identification".
- The usual-approach lines for M04 and M12 are plausible designs for the task.

## Central claim and confounds

- Timing alignment is named as the strongest confound and handled. The review says the paper states no alignment, and that [3] realigned with DTW. The [2] half needs a quote.
- The target and null mismatch between decoders is handled (outrun section).
- Not handled: whether the train and test splits are sentence-disjoint. With 100 sentences × 2 repetitions, repetition leakage would inflate rank AUC. This appears only under "needs next" (M05), with no location. Claim-table row 22 asks about N, but the review text has no "Questions for the authors" section.
- Not handled: the vocalized condition carries auditory feedback of the participant's own voice and articulation artifacts. Gv on Xv being highest may reflect auditory responses rather than a shared representation, which also bears on the hierarchy.
- Hedging: "may track timing as much as representation (inference)" is correctly hedged. The six-pair count can be stated plainly, because it is arithmetic over quoted values.

## Fairness

- [6] is correctly marked [concurrent] and not treated as prior work. No later work is presented as a missed citation.
- The slope finding (Fig. 4, Steiger test) is the authors' own result. The review reframes it rather than claiming it, which is acceptable.

## Verdicts

- No slot is `ahead`, so the ahead rules do not apply.
- "standard, without repetition" (M04) is not a defined verdict phrase. Use "standard" and say what is missing in the text.
- M09 and M10 both show "slot-filled 82", and M07's usual approach reads "None (slot-filled 119)". Check these tallies for copy errors.

## Required fixes (ordered by impact)

1. Add a quote from [2] showing time warping or alignment of covert reconstructions, or drop [2] from "earlier work used dynamic time warping" (Verdict, M04, M11 row).
2. Add a quote for the 46.3% overt-trained TER in [4], the central comparator number, and for "sentences".
3. Confirm that "10,000" in [2] is a shuffle or null count, not a candidate-set size, or reword the Verdict and the null section.
4. Recheck "the paper gives neither" against Fig. 3. If the full 3×3 AUC matrix is shown, the paper does give a covert loss relative to within-condition decoding.
5. Add the sentence-disjoint split / repetition leakage confound and the auditory-feedback confound to "Where the claims outrun the evidence", each with a paper location or "not stated".
6. Support or remove the novelty sentence "the paper's only extension", and name the deciding prior (check Proix et al., 2022, for bidirectional cross-condition decoding).
7. Update or narrow the state-of-the-art lines: M04 (Kunz et al., Cell, 2025, inner speech; or restrict to ECoG) and M12 identification (sentence-level intelligibility work from 2024-2025, or restrict to word identification).
8. Add quotes for the mel-spectrogram target of the nonlinear model, the 58 mimed sentences in [3], "covert reading" in [2] and the 110 electrodes (M05).
9. Fix the component-table inconsistencies: M03 and M11 "not reported" despite described content, identical "82" counts for M09/M10, and "None" as a usual approach for M07.
10. Soften "Fig. 4 restates that dissociation", because a model difference in slope is not a dissociation of correlation and identification.
11. Replace "standard, without repetition" with a defined verdict. Remove or add the "Questions for the authors" content that claim-table row 22 refers to, and mark row 19 as an absence claim rather than citing t11.

## Scores

- Procedure: 6/10
- Final text: 6/10
