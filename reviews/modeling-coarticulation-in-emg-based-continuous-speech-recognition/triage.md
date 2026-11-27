# Triage of the independent evaluation

Evaluator: a language model separate from the writer (one round, 20 findings). Each finding was checked against the target text and the cited source passage.

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | Target §3.1 (Kirchhoff 1999), §3.3 (Bahl et al. 1991), §3.4 ("using only one BDPF stream ... similar to ... Yu and Schultz, 2003"), §4 ("has also been described in (Yu and Schultz, 2003)"); Yu and Schultz 2003 is not in the wiki or ledger, so it is described through the target's citation and left unread. The rule says an unread any-signal prior with the same design blocks ahead; the target's own description shows it is the one-stream form, so the multi-stream form cannot be called ahead on read priors. | M06 downgraded to standard (slots, Verdict, M06 section, verdict.short); acoustic-ASR boundary stated in the M06 section and the Appendix; audit dated_counts.acoustic_asr_lineage |
| 2 | applied | Suppes 1997 and Manabe 2003 have no HMM; Meltzner 2008 matches only through a cited title; feature streams confirmed in Jou 2007 only | M06 Usual approach: "name no feature stream", "feature streams match 4, confirmed only in [Jou 2007]"; "HMM" dropped; audit note |
| 3 | applied | Only means and paired t-tests (§3.4, t47); pooled condition uses the same 28 sessions (§4) | M06 section: repetition sentence; Verdict sentence on repetition removed |
| 4 | applied | §3.4: one BDPF stream has a comparable Gaussian count and is 10.6% relative better; §4: speaker-dependent CD phones cannot be trained; Table 4: 56.55% vs 45.24% | Verdict and M06 confound sentence; "weight 0.01" confound dropped |
| 5 | applied | Wand and Schultz 2009b Sec. 4.5: triphone "Speaker-Independent Training" uses all data including the test speaker; only CI cross-speaker and MLLR runs hold the speaker out | Verdict (M03 sentence), M06 Usual approach, M03 Usual approach |
| 6 | applied | Benster et al. 2024 Abstract and Table 3: 3.7% vocal, 12.2% silent; LLM-rescored ensemble | M06 State of the art, slots M06 sota, audit state_of_the_art. The optional 8.0% test-selected ensemble was not added (budget of the body). |
| 7 | applied in part | The audit SOTA is a synthesis result with only p < 0.01. No held-out-speaker EMG recognition result with a value was read (the closest table candidate, Wu et al. 2022, reports phrase accuracy without a clear held-out-speaker value in the read passages). | State of the art line now labels it a synthesis yardstick with its condition (one session, 4 speakers, p < 0.01); audit timing for this review recorded as later in state_of_the_art_<slug> (published value kept, append-only); open item in verification_status |
| 8 | applied | M03 table has one confirmed held-out-speaker study before 2009-06; all-years usual design 40 of 76 is later practice | M03 Usual approach (count and tier), slots M03 field, Appendix wording, audit usual_approach_at_target_time_<slug> |
| 9 | applied | Wand et al. 2009 §3.1, §4.1: speakers 6 and 11 "in a reasonable range"; speaker 15 is an extra session (500 sentences, half silent); 108-word vocabulary; target §5 "within useful range for silent speech applications" | Verdict last sentence; Silent speech bullet |
| 10 | applied | Understatement of a prior, not overreach | Moved to Questions |
| 11 | applied | Authors call 31.25% and 31.49% "essentially the same" (§3.4) | Bullet dropped; Fig. 7 values now used for the one-stream vs nine-stream point in M06 |
| 12 | applied | §3.4 presents the lattice WER as an information estimate; Table 3 lists it as a row | Lattice bullet reworded |
| 13 | applied | Table 3 / §3.4: 14.8% against the CD-PF row; §3.3: 24.1% against baseline; 21.4% against CI PF (inference) | New "Bundling gain" bullet |
| 14 | applied | Target §4 "for the first time"; Walliczek 2006 Secs. 4.3-4.4 CD and clustered phone units on EMG | New "Priority" bullet |
| 15 | applied | Process sentence in the body | Moved to the Appendix |
| 16 | applied | Restatement of method and results | M03 and M12 restatements removed; Table 3 ladder reduced to 35.78 vs 41.99 and 42.16 vs 31.49 |
| 17 | applied | Test-set tuning biases, not bounds; the authors state it (§3.3) | Verdict: "optimistic: as the authors state (§3.3)" |
| 18 | applied | Jou 2007 Sec. 4.3: the test set is split into two halves for two-fold cross-validation | M06 Usual approach and M12 Usual approach |
| 19 | applied | audit_tally roles allow only target / sota / prior | isca-wand09_interspeech moved from read_fulltext to read_concurrent in the M06 audit; Appendix lists it as [concurrent] |
| 20 | applied | Hueber 2007 and 2008 are HMM phone recognizers from ultrasound and lip video inside the rule (2008: "monophone only") | Dated population 14; counts in M06 section, slots and Appendix; Hueber 2008 cited |

Counts: 19 applied, 1 applied in part, 0 rejected, 0 unverified.
