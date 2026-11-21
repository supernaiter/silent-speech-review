# Evaluation: Improving Neural Silent Speech Interface Models by Adversarial Training

Date: 2026-11-21. Fallback evaluator (claim table only): the claim table and the review's positions were checked against each other and against general knowledge of the literature. No sources were reopened.

## Claim check

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target adds an adversarial loss from a discriminator to MSE, weighted 0.75/0.25 | Claim row 1 (Abstract; §4.2) | correct | The quotes support the MSE + adversarial extension and the 0.75-0.25 ratio. "Patch-GAN" has no quote in the table. |
| 2 | "The claim to be first holds only for ultrasound" | Claim row 2 (target §6) | wrong framing | The authors' own sentence already limits the claim to "ultrasound-based silent speech interfaces". The review presents a limit the authors state themselves as its own correction. |
| 3 | Test STOI up 0.24% relative (Hun), 1.8% (Eng) | Claim row 3, Table 3 | correct | 0.7050 to 0.7067 = +0.24%. 0.612 to 0.623 = +1.80%. |
| 4 | "One run per condition" | Claim rows 3, 18 | insufficient evidence | No quote says one run. What the evidence supports is that no seeds or variance are reported. |
| 5 | GAN model has lower test MSE than the MSE-only model: 0.326 to 0.29 (Hun), 0.317 to 0.293 (Eng) | Claim row 19, Table 2 | correct (values) | The values match the quoted rows if columns 3 and 7 are the test MSE columns. The quote does not include the column headers. |
| 6 | Lower MSE "points at the baseline rather than the discriminator" (Verdict) | Claim rows 3, 19, 20 | stronger than evidence | This is inference, but the Verdict states it plainly. An adversarial term can act as a regularizer and lower held-out MSE. The 5-frame output change can also make the two MSE values not comparable. The "Where the claims outrun" section is more careful ("open candidate") than the Verdict. |
| 7 | Output changed from 1 to 5 mel frames for GAN experiments; the text does not say the baseline did the same | Claim row 10 (§4.2) | correct | The quote reads "here we specified 5 consecutive spectral vectors". The scope of "here" is ambiguous, and the review handles that correctly. |
| 8 | PESQ +2.3 to 2.7%, ESTOI +2.5 to 5.2%, MCD 1.5 to 4.5% relative | Claim row 9, Table 3 | correct | Recomputed: PESQ 2.26% / 2.66%; ESTOI 2.48% / 5.19%; MCD 1.49% / 4.47%. |
| 9 | SI-SDR -39.4 to -36.0 dB, SDR -18.3 to -16.9 dB | Claim row 17, Table 3 | correct | The ranges cover all four rows. |
| 10 | "MCD and six other objective scores"; table cell "MSE, R2, STOI, PESQ, SDR, MCD" | Claim rows 12, 17; Table 3 | inconsistent | Table 3 has seven columns: STOI, ESTOI, PESQ, SI-SDR, SDR, an unnamed column (2.797/2.777/2.827/2.735) and MCD. Table 2 adds MSE and R2. The component-table cell omits ESTOI, SI-SDR and the seventh column. |
| 11 | English test = 24 utterances | Claim row 21/25 (§4.1) | correct | The quote gives 1015/50/24. |
| 12 | 0.75/0.25 chosen with no stated selection set | Claim row 21 | insufficient evidence | This is an absence claim. The quote is consistent with it but cannot prove it. |
| 13 | Usual M02: regression loss only, 129 of 400 (pattern match); 50 adversarial | Claim rows 4, 26-29 | plausible | This is a ledger tally and is out of scope for verification. Regression-only losses are plausibly typical for this period. |
| 14 | M02 state of the art: EMA-to-speech with HiFi-GAN losses, 18.5% WER, 70 listeners, 2022 [3] [later] | Claim row 6 | correct (numbers); weak as state of the art | The quotes support 18.5% and 70 listeners. It uses a different input (EMA) and a different setup, so it cannot rank the target's loss design. The reference is listed as an arXiv preprint. To my knowledge it appeared in Proc. Interspeech 2022 (medium confidence). |
| 15 | Closest prior [2]: Wasserstein critic plus L1, perceptual and smoothness losses; without the adversarial term the output was noise | Claim row 7 | partly supported | The quotes support L1 and "adversarial loss is necessary for the production of speech". The Wasserstein critic, the perceptual and smoothness losses, and "output was noise" have no quote. |
| 16 | No ultrasound study before the target used an adversarial loss on the mapping (0, pattern match with snippet check) | Claim rows 8, 28 | plausible | I know of no earlier ultrasound-to-speech work with an adversarial mapping loss (low confidence). |
| 17 | M12 usual: MCD 21 of 51, MUSHRA 14 | Claim rows 11, 33-36 | plausible | This is a ledger tally. Note that it makes listening tests a minority practice (14 of 51). |
| 18 | M12 state of the art: 15.93% WER on TaL1 ultrasound, 2026 [4] [later]; 2.99 dB MCD and 27.9% WER on TaL1 tongue [5] [concurrent] | Claim row 13 | correct (per quotes) | The quotes support both numbers. Labels: [5] (arXiv Nov 2020) is within 6 months of the target (Apr 2021), so [concurrent] is right, and the authors cite it themselves. [4] is correctly marked [later]. |
| 19 | Authors cite 2.99 dB against their best 3.229 dB | Claim row 14 | correct | Comparability of MCD definitions is not discussed (minor). |
| 20 | Authors skip MUSHRA as slow | Claim row 15 (§5) | correct | Quote: "slow and troublesome". |
| 21 | Same group ran MUSHRA eight months earlier: 22 listeners, 16 sentences, 13 min [6] | Claim row 16 | mostly correct | 22 listeners and 13 min are quoted. "16 sentences" has no quote. The eight months match arXiv Aug 2020 to Apr 2021. |
| 22 | "Four earlier ultrasound-to-speech studies from the same group ran listening tests" (Verdict) | Claim row 35 | stated too firmly | The Appendix says pattern match. The Verdict drops that qualifier and widens "MUSHRA" to "listening tests". |
| 23 | "Justify the utility of GANs" rests on metrics the authors say may not reflect perception | Claim row 22 (§5) | correct | This is the authors' own caveat, and the review attributes it to them. |
| 24 | M03 next step: "held-out TaL1 sessions, not random utterance splits" | none | unsupported | Nothing in the review or the claim table shows the splits were random. The review's own question (row 25) suggests the English test set may be the TaL1 xaud set. |
| 25 | Claim rows 24-25 ("Questions for the authors") and the Appendix | compact review | inconsistent | The compact review contains neither section, so these rows point to text that is not in it. |

Central confound: baseline strength and setup. The GAN generator predicts 5 frames and may not share the baseline's configuration. The review names this confound but draws a firmer conclusion in the Verdict than it supports. A second confound is that all changes are small and absolute values are close, with no variance reported. The review handles this one reasonably.

Chronology: no later work is treated as prior work or as a missed citation.

## Required fixes (ordered by impact)

1. Verdict: mark "points at the baseline rather than the discriminator" as inference. Add the alternatives: the adversarial term may act as a regularizer that lowers held-out MSE, and the 5-frame output may make the two MSE values not comparable. Match the hedging in "Where the claims outrun the evidence".
2. Replace "one run per condition" (Verdict, M02, "Where the claims outrun") with "no repeated runs or variance reported", unless a location in the paper states a single run.
3. Rephrase "the claim to be first holds only for ultrasound". The authors already restrict their claim to ultrasound (§6). Keep the point that the design (critic plus regression loss) predates the target in video-to-speech [2].
4. Remove or support the M03 next step on "random utterance splits". The review gives no evidence of the split type, and the English test set may be the TaL1 xaud set.
5. Align the metric list. The component table cell, the M12 text ("six other") and Table 3's seven columns (STOI, ESTOI, PESQ, SI-SDR, SDR, unnamed seventh column, MCD) plus MSE and R2 should agree. Name the seventh column.
6. Verdict on M12: add "(pattern match, Appendix)" to "four earlier ... studies" and keep "MUSHRA" rather than "listening tests". State that "behind" rests on the group's own earlier practice [6], because listening tests are a minority practice in the ledger (14 of 51). Check this against the verdict rules.
7. M02 state of the art: say that [3] uses a different input (EMA) and cannot rank the target's loss design, or choose a closer comparator. Update reference [3] to its published version (Interspeech 2022) if confirmed.
8. Claim table: add quotes for Patch-GAN, 82 fps, the 25-frame input and the 80-band mel. For [2], add the Wasserstein critic, the perceptual and smoothness losses and "output was noise". For [6], add "16 sentences".
9. Claim table rows 5 and 19: include the Table 2 column headers so the test MSE values can be attributed.
10. Reconcile claim rows 24-25 and 26-38 with the published text: either include "Questions for the authors" and the Appendix, or drop the rows.
11. Clarify the populations behind the counts. M05's "Ultrasound imaging (slot-filled 7,329)" sits beside M12's "51 unique ultrasound-to-speech studies", and a reader cannot tell what each count covers.

## Scores

- Procedure: 7/10
- Final text: 6/10

The arithmetic is accurate throughout, the chronology labels are right, and the 5-frame confound is well spotted.
