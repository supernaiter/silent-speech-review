# Triage: Zero-Shot Personalized Lip-to-Speech Synthesis with Face Image Based Voice Control

Evaluator: fallback language model (eval.md, 2026-11-24, 14 numbered findings). Triage by the writer. Source passages opened only where a finding needed them (Kefalas et al. Table VII and reference [20]; target Sec. 3.4).

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | Kefalas et al. Table VII (GRID 33 speakers, unseen), source text: the 16.05% row is the comparison row "End-to-end WGAN (2022) [20]". Reference [20] is Mira et al., TCYB 2023, first public on arXiv 2021-04. Kefalas's own best WER on this split is 17.08% (V2A-WaveGAN-SP + basic fine-tuning). The 16.05% row is still the lowest WER in the table, so it remains the state of the art, now attributed to Mira et al. (arXiv 2021, prior). Notes k1, k2. | M06 and M12 State of the art lines; slots M06/M12 sota; audits (state_of_the_art_<slug>); extra.json |
| 2 | applied | Table 1 reports STOI/ESTOI; only ASR WER is missing. | Verdict, last sentence |
| 3 | applied | M07 section: Facetron tested gender recognition for unseen speakers (f23). | Claims section, first bullet: "same input and an unseen-speaker test" |
| 4 | applied | MOS-FVM rates the fit to the face, while EER measures the match to the speaker's own voice (t23, t25). | Claims section, third bullet |
| 5 | applied | Fig. 2 is about content embeddings (t36), not about the face embedding. | M07: "chiefly gender (inference, Fig. 2)" replaced with "recovers part of the voice, not the speaker's own (inference)" |
| 6 | rejected | Target Sec. 3.4: "Proposed achieved much better performance on MOS-FVM and EER (p <0.05) for unseen speakers". The CML comparison is also significance-tested, but only for MOS-FVM and EER, which are the two values the review cites. Notes t75 added with the full quote. | Notes only |
| 7 | applied | Appendix tally: gradient reversal 6, content-identity disentanglement 5 of 18. | M03 Usual approach; slots M03 field |
| 8 | applied | V2SFlow-V row of Table I (notes c30, verified quote). The cross-dataset gap remark is now marked (inference). | M07 State of the art |
| 9 | rejected | The 13-components table labels are the fixed spec slot names printed by render_review.py (as in earlier reviews). The section headings name the component in this paper. | None |
| 10 | applied | The Griffin-Lim ground truth bounds PESQ only. | M06 body |
| 11 | applied | Table 1 has no prior systems, and Table 2 omits the zero-shot model. | Claims section, second bullet: "is never compared with a prior system" |
| 12 | unverified | "Show Me Your Face, And I'll Tell You How You Speak" (arXiv 2206.14009) and Face2Speech are not in the wiki (index-730b0b4 title search). Neither was read, so neither is cited. | None (logged in verification_status) |
| 13 | applied | The claim-table row was split by the skeleton at "(Sec. V-B)". | claims.md row 7: full sentence, mapped to f20 and f8 |
| 14 | unverified | The wiki first pages of VCVTS and Oneata et al. print no venue, and their manifests say arXiv. The target manifest says "ICASSP 2023 / arXiv", but the paper's first page prints no venue. All three stay arXiv preprints. | None (logged in verification_status) |

Also applied: table row 23 (pretraining overlap) moved from "Where the claims outrun the evidence" to the Questions for the authors. In the Verdict, Facetron's teacher is now named "prosody embedding" (claim-check row 2).

Counts: 10 applied, 2 rejected, 2 unverified.
