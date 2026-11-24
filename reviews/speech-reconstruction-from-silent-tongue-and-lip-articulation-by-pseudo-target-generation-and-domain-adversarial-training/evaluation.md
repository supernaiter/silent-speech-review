# Evaluator: a language model separate from the writer

Date: 2026-11-24. Inputs: `references/evaluator-brief.md` and `compact.md` (review, references, claim table). The target's own text was checked only through grep of the extracted target notes (`prep/select/target.txt`); no other writer files were opened. No web sources were opened; outside knowledge is marked "unverified".

## Claim check table

| No | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Silent WER 59.960 to 43.114, vocalized 26.890 to 17.309 (Verdict; "outrun" bullet 3) | Claim rows 5, 25 (t23-t26); target notes | correct | 16.85 pts / 28.1% rel.; 9.58 pts / 35.6% rel. Arithmetic right. |
| 2 | "not a narrowed silent-vocalized gap" (Verdict) | Same numbers | wrong as stated (metric unnamed) | Absolute gap shrinks 33.07 to 25.81 points; only the ratio widens (2.23 to 2.49). See finding 2. |
| 3 | "w/o DAT ... still improves vocalized WER to 25.032%, so continued training explains the vocalized gain as well" ("outrun" bullet 2) | Claim row 24; target notes Table 2 | wrong in degree | w/o DAT recovers 1.86 of the 9.58-point gain (about 19%); continued training cannot explain the gain "as well". |
| 4 | Ablation "also removes all vocalized training data" (Verdict, M03) | Claim rows 3, 14 (t62) | insufficient evidence | t62 shows the vocalized loss is dropped. The model still starts from TaLNet pretrained on 11,487 vocalized utterances (target notes line 18) if initialised from it; "all vocalized training data" overstates. |
| 5 | Mode discriminator has "no earlier match among 12 domain-adversarial studies" (Verdict) | Claim row 3; Appendix M03 | insufficient evidence | The 12 is a pattern-match upper bound; the Appendix names no deciding prior checked for silent-vs-vocalized adversarial training, and does not say how many of the 12 predate the target. |
| 6 | DTW transfer with realignment established in [2], [3] (Verdict) | Claim row 2 (j1, g1, g2) | partly supported | g1 supports realignment for [3]; j1 supports only DTW transfer for [2]. "uncited here" is attached only to [3] in the reference list. |
| 7 | Gaddy and Klein Table 5: 76.5 vs 68.0, 8.5 points; here 46.016 to 43.114 (M02) | Claim row 9 (g3, t12, t37); target notes Table 2 | numbers correct; judgment unsupported | 68.0 is not in any quote (insufficient quote). 46.016 is the Table 2 "w/o iterative" row; cite Table 2, not only Fig. 2a. "Coarser form" is not shown by comparing point gains from different baselines (68 vs 46). |
| 8 | 15 confirmed of 52 pattern-match (M02) vs Appendix "16 confirmed" | Appendix M02 | correct but unclear | 15 of 16 confirmed use the design; the text says "15 confirmed of 52", hiding the 16. |
| 9 | "only ultrasound study in the confirmed set" (M02) | Appendix | insufficient evidence | No Appendix line lists signals of the confirmed set. |
| 10 | GETS [4] 11.89% silent EMG WER (M02 SOTA) | Claim row 8 (l3) | correct (quote) | Later work, correctly labelled; not ranked. |
| 11 | [3] gives vocalized samples own session embeddings (M03) | Claim row 11 (g4) | correct | |
| 12 | [5] speakers, [6] EMG sessions, [7] fMLLR on TaL (M03) | Claim row 12 (w1, w2, r1) | correct | |
| 13 | [8] 26.75 to 25.14%, 10 seeds, p = 0.002 (M03 SOTA) | Claim row 13 (l1, l2) | correct except p | 6.0% rel. checks out; p = 0.002 has no quote (insufficient quote). |
| 14 | w/o DAT 51.199 vs 43.114 (M03) | Claim row 14 (t33, t24) | correct | |
| 15 | [3] 71.6% without non-parallel vocalized data, 3.6 points worse (M03) | Claim row 14 (g5) | correct | Gaddy's extra data is non-parallel vocalized-only; the target's vocalized data are TaL paired takes. Analogy is loose. |
| 16 | No field count for M11 (M11) vs table "Transcript as reference (slot-filled 234)" | M11 section, components table | wrong (internal contradiction) | See finding 6. |
| 17 | [3] 9.5% lower bound (M11) | Claim row 15 (g6) | correct | |
| 18 | Silent MCD/STOI use PWG waveforms of test pseudo targets; reference 10.246% vs 4.110% (M11) | Claim rows 17, 18 (t21, t22, t53, t66) | correct | Authors state this caveat themselves (Sec. 4.3); the review presents the bias as inference, which is fair. |
| 19 | MCD 21 / MUSHRA 14 / ASR 3 of 51 (M12) | Appendix M12 | correct; table cell misleading | Table row says "MCD with MUSHRA (pattern match 21)"; MUSHRA is 14. |
| 20 | Tongue2Speech [9] 31.64% WER on TaL80 (M12 SOTA) | Claim row 20 | insufficient quote | Only "audit" given, no quote from [9]. |
| 21 | 18 of 81 speakers dropped by first-round DTW cost (Verdict, M12) | Claim rows 4, 21 (t13, t14) | correct | Authors report this themselves (Sec. 4.2); review does not claim it as its own finding. |
| 22 | Test speakers are training speakers (M12) | Claim row 22 (t16, t19) | correct | The paper's "speaker-independent" means no speaker fine-tuning; the review could say so once. |
| 23 | Invariance asserted, not measured; authors say "may" (outrun bullet 1) | Claim row 23 (t40) | correct | Row 23 cites t68 in "Notes entry" but quotes t2; minor table mismatch. |

## Findings (ordered by impact)

1. **Wrong inference on the vocalized gain ("outrun" bullet 2).** w/o DAT reaches 25.032% vocalized WER against 26.890% (TaLNet) and 17.309% (full). Continued silent-only training accounts for 1.9 of 9.6 points; the remaining 7.7 points come with the vocalized loss plus discriminator. Rewrite: "continued training explains about a fifth of the vocalized gain (1.9 of 9.6 points, inference); the rest comes with the vocalized loss and discriminator together, which Table 2 does not separate."
2. **Absolute vs relative gap left unnamed (Verdict, last sentence).** The absolute silent-vocalized WER gap narrows from 33.1 to 25.8 points; the ratio widens from 2.2x to 2.5x (inference). "Not a narrowed gap" is true only in relative terms. State the metric, or say "the absolute gap narrows by 7.3 points but the relative gap widens". This is the review's central position, so it must be exact.
3. **Novelty claim without deciding priors (Verdict, sentence 3).** "No earlier match among 12 domain-adversarial studies" rests on a pattern-match upper bound; the Appendix names no checked prior that trains a silent-vs-vocalized adversary, nor how many of the 12 predate April 2023. Either name the deciding priors read (e.g. [5], [6], [7] and which of the 12 were opened) or weaken to "none of the read priors [5]-[7] uses the speaking mode as domain label". Also reconcile with the M03 verdict `standard`: if the domain label is new, say why the verdict is still `standard` (effect not isolated by the ablation).
4. **Overstated ablation confound (Verdict; M03).** "Removes all vocalized training data" is too strong if the w/o DAT model, like the full model, starts from TaLNet pretrained on vocalized TaL data (target notes: 11,487 vocalized utterances; TaLNet is the pretrained encoder for first-iteration targets). Say "removes the vocalized loss together with the discriminator" (as the M03 section already does).
5. **Unsupported "coarser form" judgment (M02).** Comparing an 8.5-point gain from a 68.0% baseline on EMG with a 2.9-point gain from 46.0% on ultrasound does not show the target's realignment is coarser; the design difference (every five epochs vs three rounds) is enough. Also cite Table 2 ("w/o iterative" 46.016) next to Fig. 2a, and add the 68.0% figure to the claim-table quote.
6. **Internal contradiction on M11 counts.** The M11 section says "No field count exists for M11", but the component table gives "Transcript as reference (slot-filled 234)". Remove one or explain that 234 is a slot-fill count without a topic tally.
7. **Missing same-task follow-up as state of the art (M02, M11) – unverified.** The same authors later published a TaL silent-articulation reconstruction paper with text-guided pseudo targets and diffusion models (Zheng, Ai, Ling, "Speech Reconstruction from Silent Lip and Tongue Articulation by Diffusion Models and Text-Guided Pseudo Target Generation", ACM Multimedia 2024, arXiv 2024; values and locator unverified). It is a closer state of the art for both pseudo-target generation and pseudo-reference construction on the same corpus than EMG papers [4], [8]. Check it and, if confirmed, use it for M02/M11 state of the art.
8. **Bibliographic status of the target – unverified.** The target appears to have been published at ICASSP 2023 (Zheng, Ai, Ling). Reference [1] lists it only as an arXiv preprint. Check and add the proceedings version if confirmed.
9. **[2] cited for realignment without support.** Quote j1 supports DTW target transfer only. Attach the realignment to [3] alone, or quote [2] on iterative alignment. Also make "uncited here" explicit for [2] in the reference list if true; currently only [3] carries "Uncited by the target".
10. **Insufficient quotes for comparators.** p = 0.002 for [8] (claim row 13) and 31.64% WER for [9] (claim row 20) have no source quote. Add quotes; do not change the text until checked.
11. **"Only ultrasound study in the confirmed set" (M02) lacks an Appendix locator.** Add the signal breakdown of the 16 confirmed studies to the Appendix line, or drop the claim.
12. **Component table cell for M12 misleading.** "MCD with MUSHRA (pattern match 21)" reads as 21 studies using both; the Appendix says MCD 21, MUSHRA 14. Write "MCD (pattern match 21)".
13. **Minor clarity.** "15 confirmed of 52" (M02) should read "15 of 16 confirmed (52 pattern match)" to match the Appendix. The analogy to [3]'s 71.6% (non-parallel vocalized-only data) differs from TaL paired vocalized takes; say so in a clause. Claim row 23 lists t68 but quotes t2.

## Confound and fairness summary

- Strongest confound for the central claim: absolute vs relative change (finding 2), followed by the joint removal of vocalized loss and discriminator in the only ablation (handled in M03, overstated in the Verdict). Single-run results are noted against [8]'s 10 seeds. The pseudo-target reference bias for MCD/STOI is handled correctly.
- Chronology: [4], [8], [9] (2026) are labelled [later] and used only as state of the art, not as missed citations. Correct.
- Self-reported caveats (18 speakers excluded, pseudo-reference WER 10.246%, "may" on invariance) are cited to the paper's sections, not claimed as the reviewer's discovery. Correct.

## Scores

- Procedure: 7/10 (claim table thorough, quotes mostly match; two comparator quotes missing, novelty claim lacks deciding priors, possible same-task follow-up not checked).
- Final text: 6/10 (one wrong inference, central gap statement imprecise, one internal contradiction).
