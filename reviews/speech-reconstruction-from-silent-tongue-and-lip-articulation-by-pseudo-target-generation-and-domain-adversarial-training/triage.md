# Triage of the independent evaluation (13 findings)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | Table 2: w/o DAT 25.032% vs TaLNet 26.890% vs full 17.309% vocalized WER (t35, t25, t26); 1.9 of 9.6 points. | "Where the claims outrun the evidence", bullet 2 rewritten. |
| 2 | applied | Table 1 (t23-t26): silent-vocalized gap 33.1 to 25.8 points absolute, ratio 2.2 to 2.5. | Verdict, last sentence names both absolute and relative gap. |
| 3 | applied | Earlier regex hits in the M03 population were a review, paralinguistics papers and reference-list mentions, not checked as silent-vs-vocalized priors; the read priors [5], [6] use speakers and sessions, [7] uses fMLLR. | "No earlier match among 12" dropped from Verdict and extra.json open items; Verdict and M03 now state the label is new against the read priors and untested alone (why the verdict stays standard). |
| 4 | applied | t62/Sec. 4.4: Eq. (3) reduces to LRecon,s; the model may still start from vocalized-pretrained TaLNet (t18). | Verdict: "drops the vocalized loss with the discriminator". |
| 5 | applied | Different baselines (68.0 EMG vs 46.016 ultrasound) do not support "coarser"; g8 quote added for 68.0; 46.016 is Table 2 w/o ITS (t32). | M02 evidence paragraph: schedule difference stated without the comparative judgment; Table 2 cited. |
| 6 | applied | M11 slot-filled count 234 is a slot count, not a topic tally. | M11 usual line "no topic tally"; table field "Transcript (no topic tally)". |
| 7 | unverified | No ACM MM 2024 follow-up by Zheng, Ai, Ling (diffusion, text-guided pseudo targets) in the wiki checkout or index-730b0b4 (title and author search). | Not used; listed in verification_status. |
| 8 | unverified | The target's text and wiki manifest give no ICASSP venue; no proceedings version in the wiki. | Reference [1] kept as arXiv; listed in verification_status. |
| 9 | applied | j1 supports DTW transfer only; realignment is g1 ([3]). Target reference list contains neither [2] nor [3]. | Verdict attributes realignment to [3] alone; refs note "Uncited by the target" added to [2]. |
| 10 | applied (p) / unverified (31.64) | Lee et al. 2026 Sec. 5.1 "(p=0.002)" added as l4. Tongue2Speech has no source text in the wiki; 31.64% comes from the published M12 table (confirmed_in_text). | Notes l4; claim table; Tongue2Speech value kept, open item in verification_status. |
| 11 | applied | Published include reasons of the 16 confirmed: all EMG-based except the target. | Appendix M02 line gives the signal breakdown. |
| 12 | applied | Appendix: MCD 21, MUSHRA 14. | Table M12 field "MCD". |
| 13 | applied | Appendix tally 16 confirmed, 15 with the design; g5 is non-parallel vocalized data. | M02 "15 of 16 confirmed (52 pattern match)"; M03 "its non-parallel vocalized data"; claim table regenerated. |

Counts: 10 applied, 1 partly applied and partly unverified (#10), 2 unverified (#7, #8), 0 rejected.
