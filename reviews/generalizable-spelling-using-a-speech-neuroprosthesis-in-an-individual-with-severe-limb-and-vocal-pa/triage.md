# Triage of the evaluation (round 1)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | M04 audit pids: Willett 2021 counted under four designs; reviews and mention-only papers in the 252. Population cleaned to 22 prior studies that build, test or record a speller (reviews and mention-only removed); M07/M09/M12 counts relabelled as mentions; `matched` null for M04, M07, M09, M12; "spellers at the time used" removed | Verdict; all four Usual approach lines; slots.json; audits `prior_period_counts`; Appendix |
| 2 | applied | Meltzner 2018 Methods: NATO words are vocabulary items in word-sequence recognition. M04 reason now: no code-word letter code among the 22 prior studies; standard only because one participant | Verdict; M04; slots note |
| 3 | applied | Coordinator cutoff 2021-12-22 (received); prior before 2021-06-22, concurrent to 2022-06-22; undated rows dated from manifests; 2 studies of 2021 with unresolved month not counted; SilentSpeller dated 2022-04-29 (concurrent) | Appendix; audits `prior_period_counts.cutoff`; refs (build_refs target date 2021-12-22) |
| 4 | applied | Willett Table 1: 5.4% raw without LM, 0.89% with offline LM; Jude Results: T18 peak 110, T17 peak 47; target best block 30.79; target Discussion makes the 90 cpm comparison itself | Verdict; M04 State of the art (3.6 times, peak against peak, inference) |
| 5 | applied | Combination check over neural studies dated 2021 or earlier (hand-command and speech-decoding patterns): 5 matches, all mentions or separate participants; none combines both | M09; M09 audit `combination_check`; Appendix |
| 6 | applied | Target Results and Data exclusions: conversation 14.8%/16.7% over 28 trials; 15.7%/17.6% with OOV blocks; 13 self-reported copy-typing errors, 8.52%/13.75%; credited to the authors | Verdict; Where the claims outrun |
| 7 | applied | Fig. 2a, b plot the chance condition; claim and question deleted, chance item removed from needs-next | Where the claims outrun; Questions; What the field needs next |
| 8 | applied | SilentSpeller is in the wiki (doi-10.1145-3491102.3502015); read Abstract and Sec. 2: silently mouthed letters, 37 wpm at 87% in seven participants; labelled [concurrent] | M04; refs; notes d3, d4; M04 audit |
| 9 | applied | Target Fig. 4a passage: code words classified more accurately than letters (z = 3.78), isolated offline trials | M04; needs-next item narrowed to live sentence spelling in several participants |
| 10 | applied | M09 comparators now end-of-sentence command, click and dwell (mentions); Pandarinath T6 hand-squeeze click and dwell tasks | M09 Usual approach; slots |
| 11 | applied | M12 exclusion restatement removed; 98.43% tied to the 569/570 comparator | M09 State of the art; M12 |
| 12 | applied | M12 state of the art now the metric set of implanted text entry (Willett: CER, WER, cpm; Jude: cpm, wpm, WER) | M12; M12 audit; slots |
| 13 | applied | Pandarinath Methods quote: T6 squeezing her left hand in click tasks, holding still in dwell tasks | notes d9; M09 audit; M09 text |
| 14 | applied | Locators changed to § Discussion for limitations, multimodal control and deployment | M04, M09, Where the claims outrun; notes locs |
| 15 | applied | verdict.json position regenerated from the final Verdict | verdict.json |
| 16 | applied | Recall-sample note: arXiv 2208.12266 is v2 (journal version 2023), no evidence of an earlier target release | all four audits `recall_sample_check` |

Applied 16, rejected 0, unverified 0. Chaudhary 2022 dropped from the read list (now [concurrent], no longer cited) to keep 8 papers read besides the target; Duchnowski 1994 added as the deciding prior for spoken letter names.
