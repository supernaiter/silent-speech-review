# Triage of the independent evaluation (2026-11-27)

Each finding was checked against the TASLP article text (author-hosted PDF, sha256 e1c396cc...), Fig. 5 read from the rendered PDF page 7, and the wiki texts of the named papers.

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | §I contrasts with EMG ASR plus TTS; the M08 population holds only audio-producing studies, and recognition-then-synthesis appears once (Hueber 2010, ultrasound) | Verdict sentence 2 rewritten; "barely used" removed |
| 2 | applied | GETS Sec. 3 (GPT-4-refined EMG-to-text guidance), Sec. 4.1 (single subject), Table 1 (Gaddy and Klein 25.74), Table 4 (32.78 without guidance) | M06 and M04 state of the art; M08 line now says the best EMG system adds recognition-derived guidance; table cells |
| 3 | applied | Zahner 2014 and Diener 2015 are separate papers (§III-D refs 68, 71). Recount: M06 29 prior (HMM/GMM 21, TD 14); M08 14 indexed (direct 13); M12 denominator 14. Janke 2012, IJCNN 2015 and EMBC 2016 are not indexed and are listed as cited-not-indexed | Verdict, M06 usual approach (new: BLSTM and comparison), Appendix, audits; M08 moved from changed to incidental (route inherited) |
| 4 | applied | §I cites Lam 2006 and Tsuji 2008 (direct EMG) and Toda (EMA GMM); none is in the wiki index | M08 usual approach and Appendix, labelled as cited by the article |
| 5 | applied | 5 of 14, none EMG (Diener 2015 uses AB preference). Rule check: at least 3 earlier studies meet the condition, best read (Hueber and Bailly 2016, EMA); yardstick best comparable work; behind kept | M12 usual approach, table cell, audit note |
| 6 | applied | Abstract claims identity and mood retention; no test measures it; DNN uses TD15 without LDA (§V-A) | Verdict and claims list re-ranked |
| 7 | applied | §V-A points to [92] (EMBC 2016) | Table M13; Appendix cited-not-indexed list (bullet dropped for length; the EMA closed-loop citation removed) |
| 8 | applied | §V-C: GMM second best in WER; worst MCD in Fig. 5 | M06 body |
| 9 | applied | §I gives Toth's five channels and 380 utterances; Fig. 5 single-electrode DNN 5.29 (Spk2-Single), 5.61 (Spk1-Single) | M06 body |
| 10 | applied | Toth §4 EMG-to-Whisper; article §I 20.2% | M04 usual approach |
| 11 | applied | Six priors: Toth EMG synthesis, Hueber and Bailly EMA, others recognition or ECoG | M04 text, Appendix, refs note "Prior (EMA)" |
| 12 | applied | §IV states faulty channels were excluded per session | Question replaced |
| 13 | applied | Fig. 5 legend says only "LSTM" | M06 body and question 2 |
| 14 | applied | §V-E "compare ... to each other and to the given reference and resynthesized reference" vs "5 variations" | Questions; question 1 covers §V-D p value |
| 15 | applied | §V-C training-data sentence | M12 body |
| 16 | applied | TD/E4 in 14 of 29; HMM/GMM mostly recognizers | Verdict wording, M06 usual approach, Appendix setting (M06 uses the EMG subset) |
| 17 | applied | Ref [1] note states the wiki folder holds the 2016 dissertation; duplicate [later] tags removed | refs.json notes |

Applied 17, rejected 0, unverified 0. Verdicts unchanged (M06 standard, M08 standard, M04 behind, M12 behind); M08 reclassified from changed to incidental.
