# Evaluation: Mechanistic Interpretability of Brain-to-Speech Models Across Speech Modes

Date: 2026-11-22. Fallback evaluator (claim table only, one pass, no source access). Input: compact review with claim table. Sources were not re-read; "insufficient evidence" means the quoted passage does not carry the claim as written.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target explains an "inherited sEEG Conv1D-BiGRU decoder" | Claim 1; t1, t21, t22 | insufficient evidence | t21/t22 support a 64-channel Conv1D and a GRU. Neither "bidirectional" nor "inherited" is in any quote. |
| 2 | Design is rare (2 of 38) yet verdict "standard" because of one participant and no split | Claim 2; Verdict; M06 | wrong (reasoning) | Sample size and split are limitations of the evaluation, not of the design. A rare design with standard verdict needs a justification under the verdict rules, not a list of weaknesses. |
| 3 | KEEP-Conv 0.666 vs unpatched imagined 0.725 | Claims 3, 19; t36, t64 | correct | Numbers match. Column order (Full, KEEP-Conv, RAND-Conv, KEEP-RNN, RAND-RNN) is assumed, not quoted. |
| 4 | +0.102 (+18%), -0.059 (-8%), KEEP-RNN 36% below | Claim 19 | correct | 0.102/0.564 = 18.1%; 0.059/0.725 = 8.1%; 0.263/0.725 = 36.3%. |
| 5 | "The central claim ... does not hold" | Verdict vs claim 19 | wrong (strength) | The same finding is tagged "(inference)" in the outrun section but stated as fact in the Verdict. The authors' sufficiency claim may be relative to random blocks (0.666 vs 0.564), which the review confirms. The two places need to agree. |
| 6 | Full patching replaces the recipient activation | Claim 4; t60 | correct | t60 supports it directly. |
| 7 | Full patching "measures the donor" | Claims 4, 21; t35, t65, t34 | insufficient evidence | Identical 0.954 / MCD 1.63 for vocalized-to-imagined and vocalized-to-mimed (t35, t65) is the real evidence, but the Verdict does not cite it. The donor's own baseline is 0.752 (t34), so 0.954 is not the donor as evaluated. The review says this in the outrun section but not in the Verdict. |
| 8 | "Imagined-to-vocalized gives 0.177" | Claim 21; t67, t68 | correct | Table 1 and Table 3 agree. |
| 9 | "In reverse, KEEP-Conv and RAND-Conv tie at 0.575" | Claim 20; t68 | correct number, wrong framing | t68 is labeled "(Nec.)" (necessity) and t36 "(Suff.)" (sufficiency). These are different tests, not the same test reversed. A tie under ablation means something different from a tie under preservation. |
| 10 | Usual approach M06: 32 attribution, 6 probing, 2 interventions, of 38 | Claims 5, 6, 32 | wrong (internal) | 32 + 6 + 2 = 40, which is more than 38. Either the categories overlap (say so) or one count is wrong. |
| 11 | [2] as an example of hidden-layer probing, [concurrent] | Claim 5; ref list | correct | arXiv 2509 is within 6 months of 2602. It is used as an example, not as missed prior work. |
| 12 | [3] patches per-target-mode decoders, six-fold CV, permutation null | Claim 7; c1, c2, c4 | correct | Quotes support all three. Labeled [later] and used only as state of the art, which is fair. |
| 13 | "The target states neither a split nor a null"; Verdict: "no stated test split" | Claim 8; t51 (claim 29) | wrong | t51 (Fig. 5 caption): "Shaded regions indicate ± SEM across folds." The target reports folds. The review's own question section asks about "split, folds and seeds". Rephrase: folds are mentioned but neither the split nor whether selection used held-out folds is described. |
| 14 | Subspaces selected and scored on the same data | Claim 9; t52 | correct | t52: neurons ranked by mean effect "across the dataset". |
| 15 | One participant and one architecture "as the authors concede (Sec. 7)" | Claims 10, 26; t15 | insufficient evidence | The truncated t15 covers checking whether the bottlenecks generalize. Nothing quoted concedes one participant. |
| 16 | Komeiji et al. [5]: 46.3% vs 46.6% TER, 16 participants | Claim 12; k1 | insufficient evidence | k1 is truncated before any number. Neither 46.3%, the overt-trained condition nor the participant count is in the quote. Check the participant count against the abstract. |
| 17 | Martin et al. [4] as an overt-to-covert example | Claim 12 | insufficient evidence | No quote for [4]. The bibliographic data (Front. Neuroeng. 2014, 7:14) looks plausible. |
| 18 | Target's own quotation "vocalized activations improve imagined decoding" (Sec. 6.1) | Claim 15; t5 | wrong (quotation) | t5 reads "High-performing vocalized representations can be causally transferred to imagined inputs". The quotation marks imply verbatim text that the quote does not show. |
| 19 | [6]: same VocalMind recordings and decoder family, trains per condition, beats circular-shift null | Claim 14; d1–d3 | partly correct | d1–d3 support cross-condition transfer and the circular-shift null. "VocalMind" and "same decoder family" are not in any quote. d1 refers to linear decoders. |
| 20 | [6] is an example of label or trial permutation (M12 usual approach) | Claim 16; d3 | wrong | d3: "temporally circularly shifted target spectrograms". That is a circular-shift null, not a label or trial permutation. The review's own M04 paragraph says so. |
| 21 | [7]: shuffled-label null "tested on held-out subjects" | Claim 17; e1 | insufficient evidence | e1 supports the shuffled-label null only. Held-out subjects are not quoted. A shuffled-label null is also the usual approach (label permutation), so the state-of-the-art line does not show a difference from it. |
| 22 | No permutation or significance test in the target | Claim 18; t54 | insufficient evidence | This absence claim cannot be confirmed from t54. It is consistent with the quotes, and the SEM across folds (t51) is not a test. |
| 23 | Table 5: 96 to 120 conv winners vs 64 channels | Claim 23; t21, t25, t40–t45 | correct numbers, interpretation unsupported | Values 101, 118, 120, 108, 108, 96 match. The column header is not quoted, and t25 says channels are partitioned into groups and swept over windows, so the column may count group-by-window units. "Cannot exceed 64" depends on that header. |
| 24 | Shared continuous causal manifold has no tabulated values | Claim 24; t3, t57 | insufficient evidence | t57 points to Appendix C, which may hold a figure. "No tabulated values" is accurate only if no table exists. A figure-only result is a weaker objection. |
| 25 | "Decoder organization, not input quality" (Sec. 7) | Claim 25; t12 | insufficient evidence | t12 is truncated before the quoted words, so verbatim wording is not shown. |
| — | Component table: M09 and M10 both "slot-filled 82" | Table | insufficient evidence | Identical counts for two different slots may be a copy error. Check against the ledger. |

## Central claim and confound

The strongest confound is the reference point. KEEP-Conv beats random blocks of matched size (0.666 vs 0.564) but falls short of the unpatched imagined decoder (0.725). The review handles this correctly as an absolute-versus-relative issue. A second confound is the checkpoint: identical full-patch results for two recipients, above the donor's own baseline, suggest a different decoder from the baseline one. The review raises this in the outrun section but states the conclusion in the Verdict more strongly than the evidence allows. The overt-trained-on-covert comparison (M04) is a fair request.

## Absence and novelty

"Only the target and its [later] version intervene on internal activations (2 of 38)" names no deciding prior works. Activation patching and unit ablation have been applied to acoustic speech recognizers. Because the denominator includes audio-visual recognizers [2], such work may fall inside the scope. I do not know a specific earlier brain-to-speech study with the same design; this is inference, without a locator.

## Fairness

Chronology labels are consistent: [2] and [6] are concurrent, [7] (May 2026) is concurrent, and [3] (Sept 2026) is later. No later work is treated as missed prior work. The selection-on-same-data point and the necessity/sufficiency results come from the authors' own tables and are attributed to them.

## Required fixes (by impact)

1. Remove "no stated test split" and "states neither a split" (Verdict, M06). The target reports folds (Fig. 5 caption, t51). Say instead that the split and whether selection was held out are not described.
2. M12 usual approach: remove [6] as an example of label or trial permutation. It uses a circular-shift null (d3).
3. Make the Verdict match the evidence on the central claim. Either tag "does not hold" as inference as in the outrun section, or restate it as "the kept subspace beats random blocks but not the unpatched decoder".
4. Replace the "in reverse" sentence. Table 1 rows are necessity (Nec.) and sufficiency (Suff.) tests, not one test in two directions.
5. Fix the Sec. 6.1 quotation to the verbatim text (t5) or drop the quotation marks. Do the same for the Sec. 7 quotation unless the full text is quoted.
6. Reconcile the M06 tally: 32 + 6 + 2 = 40, which exceeds 38. State the overlap or correct the counts.
7. Justify the M06 "standard" verdict by the design, not by one participant and the missing split, or change the verdict.
8. In the Verdict, cite the identical 0.954 / 1.63 rows (Table 3) as the evidence that full patching reflects the donor, and note that 0.954 exceeds the donor baseline 0.752.
9. Quote the Table 5 column header before claiming winners "cannot exceed 64". t25 suggests group-by-window units.
10. Add quotes for [5] (46.3%, 46.6%, participant count) and [4], or remove the numbers.
11. Remove the unsupported details: "BiGRU" and "inherited" (claim 1), "VocalMind" and "same decoder family" for [6], "held-out subjects" for [7], and "one participant" as a Sec. 7 concession.
12. M12 state of the art: [7]'s shuffled-label null is the usual approach. Name a null design that actually goes beyond label permutation, or say that none is ahead.
13. Check the M09/M10 identical count (82) against the ledger.

## Scores

- Procedure: 6/10
- Final text: 5/10
