# Triage of the evaluation (2026-11-25)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | Lipper's user studies are closed-set listener phrase identification (t87, t126, t88, t135), the same family as Vid2speech's closed-set word classification (p29). Earlier works with a stronger quoted protocol: Lip2AudSpec transcription + 1-5 naturalness (p30, p31), improved Vid2speech STOI/ESTOI (p32). Le Cornu and Milner report listener word accuracy (p13) but the response format is unquoted and the wiki holds no source text. Two < three, so the SKILL behind rule fails; M12 downgraded to standard. Missing measures named: STOI/ESTOI, ASR WER on the output, listener transcription. | Verdict; M12 section; slots M12; Appendix M12; audit deciding_priors_note; verdict.json short |
| 2 | applied | t4 (streaming description), t107 (no hardware or end points), Table 11 constant 0.169 s (t82-t119). | Verdict last sentence ("not established"); Real-time bullet, per-window reading marked (inference) as one of two readings |
| 3 | applied (rested on other grounds) | Label kept: [2] first public 2018-07 vs target 2019-01 is within 6 months, so [concurrent] under the SKILL chronology rule (build_refs). M05 standard now rests first on the absence of repeats (t99, prior p9) and test-set selection (t131, t101); the concurrent system is cited only as having the same design, which is what blocks "ahead" regardless of chronology. | Verdict sentence 2; slots M05 note |
| 4 | applied | t90, t125, t135: audio-visual 81.25%, ten classes, chance 10%. | M12 Usual approach; slots M12 choice |
| 5 | applied | t113: held-out five-view row 1.91 / 1.83 (Table 10); Table 8 sentence removed; "does not transfer" softened to "not clearly best". | M05 evidence paragraph |
| 6 | applied | p6, p7, p24: Hush-Hush uses digits and phrases, 85:10:5 split; speaker separation of the split is not described. | M05 State of the art |
| 7 | applied | t1, t30, t31: authors frame regression against text lipreading and compare with Ephrat and Peleg in Table 4. | M06 Usual approach |
| 8 | applied | New quotes: p33 (Vid2speech 8th-order LPC, read in arxiv-1701.00495 Sec. 3), t134 (PESQ caveat, full sentence). Claim sentence on PESQ rewritten so the claim table no longer cuts it. | claims.md rows 2, 12, 16 |
| 9 | applied | p27 Table IV, p14 Table VII. | refs.json note for kefalas2023large |
| 10 | applied | t82, t107. | slots M13 choice: "0.169 s delay reported, hardware and timing end points unstated" |

Counts: 10 applied, 0 rejected, 0 unverified.
