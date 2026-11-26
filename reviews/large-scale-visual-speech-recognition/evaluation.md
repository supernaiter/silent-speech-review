# Evaluation: Large-Scale Visual Speech Recognition (component review draft)

Evaluator: a language model separate from the writer

Date: 2026-11-26. Inputs: `compact.md` (same text as `large-scale-visual-speech-recognition.md`), `claims.md`, `large-scale-visual-speech-recognition.slots.json`, `verdict.json`, the four topic audits, `tools/` (count_win.py, all.json, excl.json, recall_*.json), and these wiki sources (read-only): target `arxiv-1807.05162/source/text.txt` (v3) and `isca-shillingford19-largescale`; `isca-thangthai17_interspeech` (+ `-dnnsdt`, `_lipdnn` manifests); `arxiv-1611.06986`; `arxiv-1611.02879`; `arxiv-2302.10915`; `arxiv-2602.19316`; `arxiv-1809.02108`; `arxiv-1911.04890`; `arxiv-2606-07435-lipgap`.

## 1. Claim check

| # | Claim (location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Population: 88 prior, minus 28 perception/neuroscience and 1 duplicate = 59; 17 concurrent; 6 unresolved (Appendix) | `tools/all.json` + `excl.json` recomputed | correct | 88 − 28 − 1 (`isca-huang09b_interspeech`) = 59; 18 concurrent incl. target; 11 unresolved − 4 perception − 1 duplicate = 6. |
| 2 | Window: first public 2018-07; prior < 2018-01; [concurrent] 2018-01 to 2019-01 | target manifest, arXiv id | correct | LRS3 [6] and [9] (both 2018-09) are correctly [concurrent]; [5], [8] correctly [later]. |
| 3 | "59 earlier sentence-level lip-reading studies ... trains on a video corpus" (Verdict) | the 59 ids | wrong (wording) | The 59 include ultrasound-plus-optical SSI phone recognition (`isca-hueber07_interspeech`, `isca-hueber08b_phonerec`, `conf-icphs2011-cai-...`), AV speech enhancement (`isca-abdelaziz13_interspeech`, `isca-kolossa12_avenh`), VAD (`isca-yoshida10-twolayer`), a mini review (`arxiv-1710.01292`), a book chapter (`doi-10.5772-36466`), a corpus paper (`isca-narwekar17_prav`) and phonetic analyses (`isca-ouni07_avsp`, `isca-xue05_avsp`). They are not all sentence-level lip-reading systems, and some train nothing. |
| 4 | M02 "matched 59", tier pattern match; "None of the 59 ... names a corpus of 1,000 h or more" | all.json `over_1000_hours` | correct as an absence, misleading as a count | The regex matched 2 priors (LipNet, Thangthai 2017), which were read and rejected. "59" is the complement of a pattern search plus two readings. "Pattern match 59" in the table reads as 59 hits. |
| 5 | M06 "57 of the 59 earlier studies mention HMM decoding" | all.json `hmm` regex `\bHMMs?\b|hidden markov` | wrong (mention presented as design) | The regex counts any HMM mention. LipNet [7] and WAS [4] are among the 57: only `arxiv-1710.01292` and `isca-ouni07_avsp` miss. So the sentence counts as HMM decoders the two works it then contrasts with them. The table cell "HMM decoding ... (pattern match 57)" presents the mention count as a design count. |
| 6 | M07 "33 ... name a grammar, lexicon or dictionary" | regex `grammar|lexicon|dictionary|pronunciation` | insufficient (mention) | This is a mention count. It also catches "pronunciation" and non-decoding uses such as "dictionary learning". The table shortens it to "Grammar or lexicon", which reads as a design. |
| 7 | M12 "54 of the 59 report no human-lipreader result"; Appendix "confirmed same-item comparisons 3 ([7], [4], one other)" | all.json `human_lipreader` hits | wrong (internal contradiction) | The 5 hits are LipNet, `arxiv-1704.08028`, `doi-10.5772-36466`, `isca-cisar07-comb` and `isca-thangthai17_interspeech`. WAS [4] is not among them, so it is counted in the "54 without", yet the same paragraph cites WAS's professional at 87.6%. At least 6 report a result, so at most 53 do not. Several of the 5 hits only cite human rates (Thangthai, a book chapter). |
| 8 | 3,886 h; LRS ~246 h; LRS3 ~475 h; 15.8× and 8.2× (inference) | target Fig. 2 table; arithmetic | correct | 3886/246 = 15.8; 3886/475 = 8.2. |
| 9 | "keeping about 2% of clips" (Sec. 3) | target l.239 | correct | |
| 10 | M02 SOTA: [5] 100k h, 12.8% LRS3 VSR; V2P 55.1% is 4.3× (inference) | [5] Sec. 4, Table 2 | numbers correct; condition missing | [5] trains on YT and then fine-tunes on TED-LRS3 ("training on YT, and fine-tuning on TED-LRS3"). V2P's 55.1% is zero-shot, so the 4.3× ratio compares a fine-tuned system with a zero-shot one. |
| 11 | M02 "Standard, not ahead: no model is trained on a subset, so data and architecture are not separated in the gains over the retrained LipNet and WAS-style baselines (Table 1)" | target Sec. 5 | wrong (reasoning) | Every Table 1 baseline is retrained on LSVSR "using our training setup" with the same 5-gram LM. Table 1 therefore holds data fixed: its gains come from architecture and decoding only. The data effect is never measured. The only cross-corpus comparison (Table 2) changes data, model, decoder and LM together. |
| 12 | Verdict "its lasting contribution is data scale, not the decoder" | target Table 1; [5]; `arxiv-1911.04890` | insufficient | The paper's only controlled evidence is architectural: LipNet-Large-Ph 72.7% vs V2P 40.9% at similar size, same data and same LM. "Lasting" can rest only on later work, which the Verdict does not cite. |
| 13 | Target claim wording (Sec. 1) | target l.126 | correct | "Our approach is the first to combine a deep learning-based phoneme recognition model with production-grade word-level decoding techniques." The review's paraphrase is fair. The Interspeech 2019 version keeps a narrowed form ("first to combine a deep learning phoneme-based visual speech recognition model with phoneme-to-word decoding techniques"). |
| 14 | [2] Thangthai & Harvey 2017: visual-only DNN-HMM phoneme models, Kaldi WFST (HCLG), TCD-TIMIT dictionary, word bigram (its Sec. 5) | [2] text l.355-400 | correct | Interspeech 2017, August 2017: prior. "All experiments use the phoneme unit." |
| 15 | [3] Sanabria et al. 2016: CTC phoneme/viseme posteriors through Eesen WFSTs; video-only scored in visemes (its Table 2) | [3] text, Sec. 3, 5.2, Table 2 | correct | arXiv v1 is dated 21 Nov 2016: prior. Word decoding is shown only for audio and audio-visual input. Video-only results are viseme accuracy (65.7%). |
| 16 | Verdict "fails against [2] and [3]" | as 14, 15 | partly wrong | [3] does not decode visual-only input to words, so it cannot by itself refute a lip-reading claim. `verdict.json` says "approached by" [3], but the Verdict text says "fails against" it. |
| 17 | "The authors credit Eesen and deep-network/HMM hybrids (Sec. 2)" | target l.167, 417, 452 | wrong location | Eesen (Miao et al., 2015) is cited in Sec. 4 (Decoding) and Sec. 5 (Baseline-LipNet-Ch), not Sec. 2. Sec. 2 places the hybrids (incl. Almajai et al. 2016) under work that "still focus[es] on single-word classification". |
| 18 | Recall check: 2,209 studies, 5 hits, 0 visual-only CTC+WFST (Appendix) | `recall_ctc_wfst.json` | correct | The hits are `arxiv-1611.02879` (AV character CTC, confirmed character-based), [3], an EMA silent-speech paper, and two papers that only mention CTC. |
| 19 | Phoneme gain 3.2 points, 89.8 vs 93.0 (Table 1) | target Table 1 | correct | Same 7M LipNet, same FST pipeline and LM, phoneme vs character lexicon. "One run" is not stated by the paper; it reports no repeats (see fix L4). |
| 20 | Katz 5-gram, ~50M n-grams, ~1M vocabulary (Sec. 4) | target l.422 | correct | |
| 21 | "LM-free ablation"; "Removing the LM costs 40.9% to 53.6%", 31% relative (inference) | target Sec. 5 (V2P-NoLM) | numbers correct, label wrong | V2P-NoLM replaces the 5-gram with a 100k-word dictionary "weighted by their smoothed frequency in the training data, essentially a uni-gram language model". It is not LM-free. The comparison with "1 of 59 states a no-LM condition" compares unlike things. 31.1% relative is correct. |
| 22 | M07 SOTA: [8] 17.6% with no external LM | [8] abstract, Table; [5] Sec. 4 | correct but not the best | [5] also uses no external LM ("no external LM was used") and reaches 12.8%. [8]'s 17.6% is the best result on public data only (~2,500 h unlabelled). |
| 23 | M06 SOTA: "Sub-word outputs without a lexicon lead" | [5] Sec. 4 | correct, imprecise | [5] tokenizes at character level with an RNN-T. "Character or sub-word" is accurate. |
| 24 | M12: readers 92.9% (274 videos, no context) and 86.4% (153, with context); model 40.9% on the full test; reader count not stated | target Sec. 5, Table 1 | correct | The pairing is right. Not mentioned: the subsets were selected by length (≥6 and ≥12 words), and readers saw whole-head clips with up to 10 replays. |
| 25 | "The Table 1 caption calls the intervals standard deviations; Sec. 5.1 calls them standard errors" (Where the claims outrun) | target Table 1 caption, Sec. 5.1 | wrong as a criticism | The bootstrap standard deviation of an error-rate estimate is its standard error. Both passages describe the same quantity ("standard error ... estimated by bootstrap sampling"). There is no inconsistency to report. |
| 26 | M12 SOTA: "No later sentence-level study in the ledger table repeats a professional comparison (Appendix)" | Appendix M12 entry; all.json later hits | insufficient evidence | The Appendix gives prior counts only. There are 13 later `human_lipreader` pattern hits, e.g. `arxiv-2606-07435-lipgap` (Jain & Harte 2026: three VSR models vs 410 human participants, word-level MaFI). 12.8% LRS3 WER is not a state of the art for evaluation practice. |
| 27 | Zero-shot LRS3: 55.1% vs TM-seq2seq 57.9% (target Table 2); no TM-seq2seq filtered score | target Table 2, Sec. 5.1; [9] Table 2 | correct for the target; comparator differs in [9] | The published [9] (arXiv v2/TPAMI, its Table 2) gives LRS3 video-only TM-seq2seq at 59.9% (no LM) and 58.9% (+ext LM). In [9], 57.9% is the noisy audio-only result. Makino et al. 2019 (Table 7) and [5] (Table 2) also list 58.9 or 59.9. |
| 28 | Quote "in both experiments" | target Sec. 5.1 | wrong quote | The text reads "In both cases, V2P outperforms TM-seq2seq". |
| 29 | Verdict "a YouTube source never screened for TED talks" | target Sec. 3, 5 | stronger than evidence | The paper states no exclusion, which is what the "Where the claims outrun" bullet correctly says. "Never screened" asserts a fact the paper does not report. |
| 30 | TED overlap raised as a bullet, a question and a next step | — | appropriate | Raising it as an open question with a test is right. It applies equally to [5] and Makino 2019 (same YouTube mining, evaluated on LRS3), which the review could note. |
| 31 | Ref [2] DOI 10.21437/Interspeech.2017-1550 | [2] PDF footer l.153; manifests of `isca-thangthai17-dnnsdt`, `isca-thangthai17_lipdnn` | likely wrong | The PDF footer prints `http://dx.doi.org/10.21437/Interspeech.2017-106`. Two of the three other wiki records give 2017-106. Only the `_interspeech` manifest has 2017-1550. |
| 32 | [5] ICASSP 2024 pp. 10136-10140 | — | unverified | The year is consistent. I could not locate the pages. |
| 33 | M11 `not_reported` with a filled cell ("Held-out LSVSR test; split not stated") | SKILL.md checklist ("no `not_reported` with a filled cell"); target Sec. 5 | rule conflict | The paper does give the test size (~37 min, ~63,000 frames, ~7,100 words). It also states that blurry videos were removed from validation and test but kept in training. The review omits both. |

## 2. Findings and required fixes (ordered by impact)

### High

**H1. M02 verdict reason misreads Table 1.** Location: M02 section, last sentence, and `slots.json` M02 note.
Evidence: Target Sec. 5: baselines are trained "using our training setup" with "the same language model". All Table 1 rows use LSVSR. Table 1 holds data fixed, so its gains are architecture and decoder gains.
Fix: "Standard, not ahead: the data effect is never measured. Every Table 1 row trains on LSVSR with the same LM, so Table 1 isolates architecture and decoding at fixed data. The only cross-corpus result (Table 2) changes data, model, decoder and LM at once, on one test set." This keeps `standard` under the skill rule: the absence holds (0 of 59), but the effect condition fails.

**H2. Verdict headline outruns its evidence.** Location: Verdict, first sentence ("lasting contribution is data scale, not the decoder").
Evidence: The paper's only controlled comparison is architectural: LipNet-Large-Ph 72.7% vs V2P 40.9% at similar parameter count, same data and LM (Table 1). The data contribution is unmeasured in the paper (H1).
Fix: Rest "lasting" on later work and name it: the same YouTube-mining line grew to 31k h (Makino et al. 2019, ASRU, arXiv:1911.04890, 33.6% LRS3 video-only without LRS3 training, its Table 7) and 100k h [5]. State that the paper's own measured gains are architectural.

**H3. M02 state of the art compares fine-tuned with zero-shot.** Location: M02 "State of the art" line and table cell.
Evidence: [5] Sec. 4: "training on YT, and fine-tuning on TED-LRS3". V2P 55.1% is zero-shot (target Sec. 5.1).
Fix: Write "12.8% after LRS3 fine-tuning". Either drop the 4.3× ratio or mark it as mixed-condition. Add Makino et al. 2019 (33.6%, 31k h, no LRS3 training) as the like-for-like zero-shot comparator. It is in the wiki (`arxiv-1911.04890`).

**H4. Mention counts presented as design counts (M06, M12, M07).** This is the same error corrected in earlier reviews.
- M06. Location: Usual approach, table row M06. Evidence: the HMM regex matches any mention, and LipNet [7] and WAS [4] are in the 57. Fix: "57 of 59 mention HMMs (pattern match, mentions, including [7] and [4], which only cite HMM work)". In the table, change the cell to "HMM-based (mentions; pattern match 57)". Or base the usual-approach count on design patterns (DNN-HMM or tandem 14, WFST 7) with the mention count as an upper bound.
- M12. Location: Usual approach, Appendix M12, table row. Evidence: WAS [4] is not among the 5 `human_lipreader` hits but is cited as a professional comparison and listed among the 3 confirmed. Fix: recount as "6 report a human-lipreader result (5 pattern hits + [4] read), at most 53 without". Note that the pattern hits include citations of human rates. Update `slots.json` matched (54 → 53 or fewer) and the Appendix.
- M07. Location: Usual approach, table. Evidence: the regex includes "pronunciation" and catches "dictionary learning". Fix: label it "mention a grammar, lexicon, dictionary or pronunciation (pattern match, mentions)". In the table, write "Grammar or lexicon mentioned".

### Medium

**M1. M02 usual approach is an absence set just below the target.** Location: M02 Usual approach; `slots.json` M02 (`matched` 59, tier pattern match).
Evidence: The 59 is the complement of 2 regex hits that were read and rejected. "Pattern match 59" renders as 59 hits. "No corpus ≥ 1,000 h" names no design.
Fix: Describe the typical design: "public labelled corpora of 7–246 h (TCD-TIMIT ~7 h [2], GRID 28 h, ViaVoice 35 h, LRS ~246 h [4]; target Fig. 2)". Keep the absence as "0 of 59 at ≥ 1,000 h (pattern search, 2 hits read and rejected)". If the renderer needs `matched`, use 0 with field "≥ 1,000 h corpus", or explain the complement in the cell.

**M2. Population described too narrowly.** Location: Verdict sentence 2; Appendix "Setting".
Evidence: see claim 3. The 59 include SSI ultrasound work, speech enhancement, VAD, reviews, a book chapter and corpus papers.
Fix: Write "59 earlier lip-reading, VSR or AVSR entries (including reviews, corpus papers and ultrasound-plus-video SSI work)". Alternatively, drop the non-system entries and recount.

**M3. "Fails against [2] and [3]" overstates [3]; the stronger prior is missing; the surviving narrower novelty is unstated.** Location: Verdict sentence 3; M06 paragraph 2.
Evidence: [3] decodes words only for audio and AV input; its video-only output is viseme accuracy (Table 2). `verdict.json` says "approached by". The target itself cites Almajai et al. 2016 (ICASSP 2016, "Improved speaker independent lip reading using speaker adaptive training and deep neural networks") among "deep networks with traditional speech techniques" (Sec. 2). To my knowledge, that paper is a visual-only DNN-HMM Kaldi system decoding words on RM with a word LM. This is outside knowledge and should be verified; the paper is not in the wiki. The review's own recall check finds no earlier visual-only CTC-phoneme plus WFST system.
Fix: "The claim fails as worded against [2] (and against Almajai et al. 2016, which the target cites); [3] had CTC phonemes with WFST word decoding for audio-visual input only. What remains new is a visual-only CTC phoneme model decoded by WFST (0 earlier among 2,209 wiki studies, Appendix)." Also note that the claim persists in the Interspeech 2019 version.

**M4. "LM-free ablation" is a unigram ablation.** Location: Verdict sentence 4; M07 paragraph; table M07 "LM-free ablation"; Next-steps M07.
Evidence: Target Sec. 5: V2P-NoLM uses a 100k-word dictionary weighted by smoothed training frequency, "essentially a uni-gram language model".
Fix: "Replacing the 5-gram with a 100k-word unigram raises WER from 40.9% to 53.6% (Table 1), 31% relative (inference)". Drop the comparison with the "no-LM condition" count, or recount for unigram or no-LM decoding.

**M5. M07 state of the art is not the best no-LM result.** Location: M07 State of the art; table M07.
Evidence: [5] Sec. 4 says "no external LM was used", and [5] reaches 12.8%.
Fix: "[5] 12.8% without an external LM (100k h in-house); best on public data [8] 17.6%, also without an external LM."

**M6. The SD vs SE bullet is not an inconsistency.** Location: "Where the claims outrun the evidence", bullet 3.
Evidence: A bootstrap standard deviation of the WER estimate is its standard error. Caption and Sec. 5.1 agree.
Fix: Delete the bullet. If needed, replace it with: "The ± values are test-resampling errors on a ~37-minute, ~7,100-word test set (Sec. 5); no repeated training runs are reported."

**M7. TM-seq2seq comparator value.** Location: "Where the claims outrun", bullet 1.
Evidence: [9] as cited (arXiv v2/TPAMI, Table 2) reports 59.9% (no LM) and 58.9% (+ext LM) for LRS3 video-only. 57.9% in [9] is the noisy audio-only row. The target quotes 57.9% from an earlier preprint.
Fix: "57.9% as quoted by the target (Table 2); the published [9] gives 58.9% with its external LM (its Table 2)."

**M8. M12 state of the art: absence not backed, and the metric does not fit the slot.** Location: M12 State of the art; table M12.
Evidence: The Appendix has no later tally for M12, and there are 13 later pattern hits. The latest human–machine comparison in the wiki is Jain & Harte 2026 (`arxiv-2606-07435-lipgap`: three VSR models vs 410 human participants on MaFI, word-level, non-professional).
Fix: Add the later count to the Appendix. Name Jain & Harte 2026 as the most recent human comparison, and say it is word-level and non-professional. Keep "no later professional sentence-level comparison" only if the tally supports it. Remove "12.8% LRS3 WER" from the M12 state of the art cell, or state that it answers the accuracy gap, not evaluation practice.

**M9. Verdict asserts "never screened for TED talks".** Location: Verdict last sentence.
Evidence: The paper does not report any screening. The bullet in "Where the claims outrun" correctly says "no exclusion ... is stated".
Fix: "... and a YouTube source with no stated exclusion of TED talks". Optionally add that the same question applies to [5] and Makino et al. 2019.

### Low

**L1. Ref [2] DOI.** Location: References [2] and `.bib` `thangthai2017dnn`. Evidence: the PDF footer reads `10.21437/Interspeech.2017-106`; `isca-thangthai17-dnnsdt` and `isca-thangthai17_lipdnn` manifests agree. Fix: change to 10.21437/Interspeech.2017-106 after one check of the ISCA archive page.

**L2. Wrong section for Eesen credit.** Location: M06 paragraph 2. Evidence: Eesen is cited at target Sec. 4 (Decoding) and Sec. 5. Fix: "(Secs. 2 and 4)". Optionally add that Sec. 2 files the hybrids under single-word work.

**L3. Misquote.** Location: "Where the claims outrun", bullet 1. Fix: "In both cases, V2P outperforms TM-seq2seq" (Sec. 5.1).

**L4. "One run" not stated by the paper.** Location: M06 last sentence; M12 last sentence; `slots.json` M03 note. Fix: "no repeated training runs are reported".

**L5. Method language in the body.** Location: M06 ("A recall check over 2,209 wiki studies finds ..."); M12 ("in the ledger table"). Fix: state the facts with the Appendix reference, e.g. "No earlier visual-only CTC phoneme model decoded to words by WFST appears among 2,209 wiki studies (Appendix)".

**L6. Internal tension in the M06 usual approach.** Location: "neural sentence-level lip readers emitted characters". Evidence: [2] is a neural (DNN-HMM) phoneme system and appears in the next paragraph. Fix: "end-to-end neural sentence-level lip readers emitted characters".

**L7. M11 verdict conflicts with the skill rule and misses stated test facts.** Location: table M11; `slots.json` M11. Evidence: claim 33. Fix: put only the missing element in the cell ("Split unit and speaker overlap not stated"). Mention the 37-minute test and the validation/test-only blur filter in M12, since both bear on the ± values and on comparability with training.

**L8. M12 human-subset conditions.** Location: M12 paragraph. Evidence: target Sec. 5: the subsets were selected by length (≥6 and ≥12 words), and readers saw whole-head clips with up to 10 replays. Fix: add one clause, because both conditions affect the 40.9% vs 86.4/92.9% comparison.

**L9. "Sub-word" for [5].** Location: M06 State of the art. Fix: "Character or sub-word outputs without a lexicon".

## 3. Scores

- Procedure: 6/10. Windows, population arithmetic, deciding priors and the recall checks were done and are reproducible. However, three usual-approach counts are mention counts presented as designs, one is contradicted by the review's own reading of WAS, and the 1,000-hour absence is framed as a matched count.
- Final text: 6/10. The target is quoted fairly and the arithmetic is correct. However, the M02 verdict reason misreads Table 1, the state of the art comparison mixes fine-tuned and zero-shot results, the "LM-free" label is wrong, and one overreach bullet (SD vs SE) is not an error.

Counts by severity: High 4, Medium 9, Low 9.
