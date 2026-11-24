# Triage of the independent evaluation (2026-11-24)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | SKILL.md `behind` rule needs at least 3 earlier ledger papers meeting the condition, best one read and named. Only Lip2Wav (prior, read) reports STOI/ESTOI on the same Lip2Wav speakers; the 15 prior STOI/ESTOI pattern hits are other corpora and were not read; SLTS and RobustL2S are [later]. Rule not met. | M12 verdict changed to standard, "narrower than its baseline's protocol" (Verdict, M12 section, slots.json, extra.json) |
| 2 | applied | Target Table 1 and Table 3 (notes t23, t24, t26, t27, t29, t30, t34, t35): FastLTS intelligibility MOS is higher than Lip2Wav on Chess Analysis, Hardware Security and GRID, lower on Chemistry Lectures. | M12 section now gives all four conditions; Verdict no longer cites Chemistry only; "agrees with RobustL2S" removed |
| 3 | applied | The listener test is the usual protocol (83 of 165, Appendix); the authors give a reason for omitting STOI (§5.3, t62). | M12 verdict standard; the reason stays in the Usual-approach line |
| 4 | applied | VCA-GAN p. 1: "35th Conference on Neural Information Processing Systems (NeurIPS 2021)" (c39); the target cites it as NeurIPS 34 (2021). First public 2021-12, more than 6 months before 2022-07: prior. | refs.json (NeurIPS 2021, first_public 2021-12), M06 State of the art ("the prior VCA-GAN") |
| 5 | applied | §5.5 separates mel and waveform speed itself (t86, t87). | Verdict reworded: the abstract headlines 19.76×, which mostly reflects replacing Griffin-Lim, "as §5.5 itself notes" |
| 6 | applied | §5.5 states hardware and batch size (t3, t73). | "warm-up, repetitions and GPU synchronization are not stated" |
| 7 | applied | Mira et al. Table III header "Method PESQ STOI MCD WER" (c30); target Table 4 lists "GAN-based [37] 1.684" (t39), the 2019 Interspeech GAN of the same group (target reference list). | Claim table adds c30; text: "2.10 PESQ"; "Table 4 lists only that group's 2019 GAN, at 1.684" replaces "which Table 4 omits" |
| 8 | applied | SLTS Table 7 header and chem block (c9, c14); RobustL2S chem STOI 0.583 (c19) is below SLTS 0.757, so SLTS stays the state of the art; SLTS venue ICCV 2023 from the CVF open-access version in the wiki (cvf-niu23-slts). | M06 State of the art adds the RobustL2S comparison; refs.json SLTS venue; claim table location "Table 7, chem block" |
| 9 | applied | Target §5.4: "This matches the observation of [24]" (t84). | M06 text: "a failure Lip2Wav also reported (§5.4)"; mismatch reading marked "(inference)" |
| 10 | applied | §4.4 says "for small dataset" without naming GRID (t20). | Training-regime bullet marked "(inference)" |
| 11 | no change | Evaluator confirmed these items. | – |

Counts: 10 applied, 0 rejected, 0 unverified (item 11 needed no change).
