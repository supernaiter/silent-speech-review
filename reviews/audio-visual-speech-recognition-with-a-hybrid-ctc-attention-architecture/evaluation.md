# Evaluation: Audio-Visual Speech Recognition with a Hybrid CTC/Attention Architecture

Evaluator: a language model separate from the writer

Date: 2026-11-26. Inputs: `compact.md`, the draft `audio-visual-speech-recognition-with-a-hybrid-ctc-attention-architecture.md`, `*.slots.json`, `verdict.json`, `*.plan.json`, the three audits and `tools/*.json`, and the source texts in the wiki (`papers/arxiv-1810.00108`, `arxiv-1803.04988`, `arxiv-1809.02108`, `arxiv-2303.14307`, `arxiv-2202.13084`, `arxiv-1611.05358`, `arxiv-1611.06986`, and selected population studies). The wiki and the review files were not modified.

## 1. Claims checked

| # | Claim (location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target first public as arXiv:1810.00108v1, 28 Sep 2018 (Refs [1]) | target `text.txt` p. 1 margin: "arXiv:1810.00108v1 [cs.CV] 28 Sep 2018" | correct | |
| 2 | LCANet [2] is [concurrent] (Verdict, M06, Refs) | LCANet `text.txt` l. 95: "arXiv:1803.04988v1 [cs.CV] 13 Mar 2018"; plan `cutoff_rule` 2018-03 to 2019-03; SKILL.md l. 88 (±6 months, dates kept as YYYY-MM) | correct under the month rule; borderline | By day, 13 Mar to 28 Sep is 6.5 months, so it would be prior. The authors cite it (Sec. 1, ref. [21], as IEEE FG 2018). Either label leaves the M06 verdict unchanged (see F10). |
| 3 | Afouras et al. [5] is [concurrent] | arXiv:1809.02108 v1 is dated 6 Sep 2018 (the wiki text is v2, 22 Dec 2018) | correct | |
| 4 | "the paper runs neither CTC-only nor attention-only on LRS2" (Verdict; slots M06 note) | target Sec. 5.4: α and λ "are optimised on the validation set. The optimal values ... are 0.2 and 0.1" | wrong as worded | The paper reports no α = 0 or α = 1 result. The validation search may have included them. "Reports" is supported; "runs" is not (F3). |
| 5 | LCANet AH-CTC-CE 4.9% against 2.9% WER for the single-loss cascade (Verdict) | LCANet Table III rows 3 and 6; Sec. 4.C | correct | Missing context: AH-CTC-CE is LCANet's reimplementation of the acoustic hybrid [43] (Watanabe et al.). λ was swept from 0.1 to 0.9 and only the best was reported, so the hybrid was the tuned side (F10). |
| 6 | Front end pretrained on LRW (Sec. 5.1); LM reads 9.4 million LibriSpeech words (Sec. 5.3) | target Secs. 5, 5.1, 5.3 | correct; claim-table quote insufficient | Claim-table rows 3 and 20 quote t18 ("trained for 20 epochs") and t16 ("more than 2 million words"). Neither quote supports LRW pretraining or the 9.4 million words (F13). |
| 7 | "trained only on LRS2" overreach (Verdict, Where the claims outrun) | target Sec. 6; Table 2 caption; Sec. 1 | correct; fairness incomplete | The Sec. 6 sentence covers the audio-only model too, which has no LRW component. The cleaner overreach is the visual-only claim "without using any external databases" (Sec. 6, also Sec. 1), which rests on the LRW-pretrained ResNet. The authors' own distinction (the Table 2 caption flags non-public pretraining) is not reported (F6). |
| 8 | Sec. 1 places 32.9 points "at high SNR levels"; Sec. 6 places it at −5 dB (Where the claims outrun) | target Sec. 1, Sec. 6, Abstract, Sec. 7 | correct but missing context | The Abstract ("as the signal-to-noise ratio decreases") and Sec. 7 ("especially at high levels of noise") agree with Sec. 6. This is a single wording slip in Sec. 1, not an overreach. The claim table has no Sec. 6 quote (F9). |
| 9 | 8.3% to 7.0%, 16% relative (inference); one run; unnamed split | target Table 2, Secs. 4.2, 5.2, 5.4, 6 | correct; split wording slightly strong | Sec. 4.2 names the standard train, validation and test partitions, and Sec. 5.4 tunes on validation, so test is implied (inference). The point that the split is "not stated" stands, but more weakly (F17). |
| 10 | Noise sweep uses early fusion only (Fig. 3); late fusion 8.5% | target Sec. 6 "(using early fusion)"; Table 2 | correct; wrong locator | The early-fusion statement is in Sec. 6 text, not in Fig. 3. The bullet names a gap, not a claim that outruns evidence (F16). |
| 11 | Training noise babble only; eight test types exclude babble | target Sec. 5.2, Sec. 6 | correct | Cafe noise (Loizou) contains background babble, so "unseen" holds for the label more than for the acoustics (F19). The claim-table quote t21 does not mention babble (F13). |
| 12 | Auto-AVSR [6]: 1.5% LRS2 AVSR, 14.6% visual-only at 3,448 h; 79% and 77% lower (inference) | Auto-AVSR Table 3; arithmetic | correct | Missing context: in the same table the audio-only model also gives 1.5%, and Auto-AVSR decodes its ASR and AV-ASR models without an LM, "since no further improvements are observed" (Sec. 3.3) (F5). |
| 13 | CM-seq2seq [7] 3.9% at 380 h (Table 3 of [6]); 44% below 7.0% | Auto-AVSR Table 3, A+V block: "CM-seq2seq [22] 380 3.9" | correct | The same block lists the target as "CTC/Attention [2] 380 7.0" and marks it with extra data, which supports the LRW point. |
| 14 | Auto-AVSR Transformer LM on 166 million characters (M07 SoTA) | Auto-AVSR Sec. 3.3 | correct; incomplete | That LM is used for the visual-only models only (F5). |
| 15 | Ma et al. 2022 [8]: 29.5 ± 0.4% over ten runs; lists this paper at 63.5% (M12 SoTA) | NMI Table 1 | correct | The paper is visual-only with no noise sweep, so it covers only the variability half of M12 (F12). |
| 16 | [5] trains CTC and seq2seq separately and reports results without an external LM | Afouras Sec. 1 l. 39; Table 2 (+extLM columns) | correct | The target's "A + V [29]* 8.2" is the TM-CTC model with extLM (Afouras l. 506, 651). |
| 17 | Population: 38 before 2018-09, minus 5 perception entries (4 studies) and 1 duplicate, gives 32 | `tools/clean_before.json`, `m06_obj.json` | correct | Perception exclusions and the huang09b merge check out. Minor: of the 4 "studies dated only to 2018", isca-su18b-crossdomain and isca-su18b_interspeech look like versions of one paper, so this is 4 entries and probably 3 studies (F18). |
| 18 | M06: "All 32 ... name HMMs" as usual approach; table "HMM named ... (pattern match 32)" | `clean_before.json` pids; WLAS `text.txt` (8 HMM mentions, no HMM design) | mention count shown as design count | The 32 include the 4 neural studies (WLAS, Sanabria, 1611.02879, 1803.04840), which mention HMMs only as background. "CTC 4" also includes WLAS, which is attention-only (F1). |
| 19 | M07: "28 of 32 name neither an n-gram nor a neural LM" (Verdict, M07, table) | `m07_lm.json` regex; NTCD-TIMIT (isca-abdelaziz17b): "A simple bi-phone language model has been used for decoding"; isca-abdelaziz17-turboav (5 × "language model"); JSALT 2000 report oa-W3099202502 (9 × "LM") | wrong as a design count | At least three of the 28 name a language model; the regex misses "bi-phone", "language model" and "LM". "Neural LM 0" is plausible (F2). |
| 20 | M12: 22 at stated SNRs, 20 without variability; "the 2 with one date from 1999 and 2001" | `m12_noise.json`; isca-potamianos01_eurospeech l. 512 ("three repetitions of the noisy audio-only sequence", a human-listener procedure); talle99 (25 runs, 95% CI) | partly wrong | The Potamianos 2001 match is a perception protocol, not run variability, so the count is 1 of 32 and 21 of 22 (inference). The Verdict's "one-run noise sweep, as in 20 of 32" turns the absence of a mention into a design ("one-run") (F11). |
| 21 | Novelty "holds only with the authors' qualifiers, audio-visual and in the wild" | target Abstract ("first time ... used for audio-visual recognition of speech"); Sec. 1 adds "in-the-wild"; Appendix 0 of 32 | judgment stronger than needed | The review's own ledger (0 of 32 across all sentence-level AVSR) supports the Abstract's broader AVSR-only claim, so the "in the wild" qualifier is not needed (F15). |
| 22 | verdict.json `position`: "the objective later reached 1.5% LRS2 AVSR WER" | body M06 inference: "later gains came from encoder and data" | contradiction | The position credits the objective with a gain that the body attributes to the encoder and the data (F4). |
| 23 | Bibliography [2], [5], [7] | target ref. [21]; IEEE records (outside knowledge) | partly wrong | [2] appeared at IEEE FG 2018, pp. 548–555 (stated in the target's own ref. [21]), not only as an arXiv preprint. [7]'s DOI 10.48550/arXiv.2102.06657 is the arXiv DOI, while its pages are ICASSP's; the IEEE DOI is, as best I recall, 10.1109/ICASSP39728.2021.9414567 (unverified). [5] TPAMI final issue 2022, 44(12):8717–8727 (unverified) (F14). |

## 2. Findings (ordered by impact)

**F1. Medium. M06 usual approach and 13-components table: a mention count is presented as a design count.**
Location: M06 "Usual approach", first sentence; table row M06 "HMM named; neural: one CTC or attention loss; of 32 before 2018-09 (pattern match 32)"; Appendix "HMM 32, CTC 4, attention or seq2seq 1".
Evidence: `clean_before.json` lists all 4 neural studies (arxiv-1611.02879, 1611.05358, 1611.06986, 1803.04840) under `m06_hmm`. WLAS (1611.05358) is an attention model that mentions HMMs only in related work. WLAS is also in `m06_ctc`, so "CTC 4" is not 4 CTC designs. In the table, "(pattern match 32)" under "Usual approach (count)" will be read as 32 of 32 HMM systems.
Fix: Write "HMM-based recognition in the 28 non-neural studies; the 4 neural ones train a single loss, CTC ([3] and two others) or attention (WLAS [4]); all 32 mention HMMs (pattern match, mentions included)". In the table, use "HMM-based (28 of 32, non-neural)" and keep "pattern match 32" only for the mention tally. In the Appendix, write "CTC 4 (mentions; 3 CTC designs)" or drop the design reading.

**F2. Medium. M07 usual approach, Verdict and table: "28 of 32 name neither an n-gram nor a neural LM" is a regex artifact.**
Location: Verdict, last sentence; M07 "Usual approach"; table row M07 "(pattern match 28)"; Appendix M07 "neither 28".
Evidence: The n-gram regex (`n-gram|[2-5]-gram|trigram|bigram language`) misses the population's own wording. NTCD-TIMIT (isca-abdelaziz17b_interspeech) says "A simple bi-phone language model has been used for decoding". Turbo decoders (isca-abdelaziz17-turboav) mention "language model" 5 times, and the JSALT 2000 report (oa-W3099202502) mentions "LM" 9 times. All three are in the "neither" 28.
Fix: Keep the robust part, "none of the 32 names a neural LM (pattern match, Appendix)", and give the LM in use as n-gram or phone-level LMs and task grammars (12 match grammar or lexicon). Drop "28 of 32 name none" from the Verdict and the table, or relabel it "28 do not match the n-gram pattern" without a design reading. In the Verdict, state why M07 is standard (no LM-free result), not the count.

**F3. Medium. Verdict: "runs neither CTC-only nor attention-only on LRS2" is stronger than the evidence.**
Location: Verdict, first sentence; slots M06 note ("no CTC-only or attention-only run on LRS2"); M06 body.
Evidence: Sec. 5.4 says α and λ "are optimised on the validation set". The searched range is not given, so α = 0 or 1 may have been run and not reported. The review's own question ("What WER do α = 0 and α = 1 give, and what ranges were searched?") assumes "not reported".
Fix: Replace "runs neither" with "reports neither", in the Verdict and in `slots.json` M06 `note`.

**F4. Medium. verdict.json `position` credits the objective with later gains that the body attributes to the encoder and the data.**
Location: verdict.json `position`: "the objective later reached 1.5% LRS2 AVSR WER".
Evidence: The M06 body says "later gains came from encoder and data (inference)". Auto-AVSR Table 3 also gives 1.5% for audio-only at 3,448 h.
Fix: Write "the same objective is used in the current best LRS2 system (1.5% WER at 3,448 h), where encoder and data, not the objective, account for the gap (inference)", or drop the clause.

**F5. Medium. M06 and M07 state of the art leave out context in the read source that bears directly on the review's argument.**
Location: M06 "State of the art"; M07 "State of the art".
Evidence: Auto-AVSR Table 3 gives audio-only 1.5% and audio-visual 1.5% at 3,448 h. Sec. 3.3 says "language models are not included for ASR and AV-ASR models since no further improvements are observed", so the 166M-character LM applies only to the visual-only models.
Fix: In M06, add "audio-only is also 1.5% there, so the clean AV gain vanishes at that scale". In M07, add "its AV and audio models use no LM, as it found no gain". This is the direct state-of-the-art evidence that the LM question matters for the visual-only result, not for the 7.0% AV result.

**F6. Medium. Fairness of the "trained only on LRS2" critique: the authors' own distinction is not reported, and the strongest instance is missed.**
Location: Verdict, third sentence; "Where the claims outrun the evidence", bullet 1.
Evidence: The Table 2 caption and Sec. 6 frame the contrast as pretraining on a "non-publicly available dataset" ([29]). LRW is public. The Sec. 6 "trained only on LRS2" sentence covers the audio-only model too, which uses no LRW (only the LibriSpeech LM text). The visual-only claim "state-of-the-art performance when training only on LRS2, i.e., without using any external databases" (Sec. 6; also Sec. 1 "without using external datasets") directly contradicts the LRW-pretrained ResNet (Sec. 5.1).
Fix: Open the bullet with what the authors say ("the authors separate non-public pretraining from their public data, Table 2 caption"). Then state the overreach: the visual-only "without any external databases" claim (Secs. 1 and 6) contradicts the LRW pretraining (Sec. 5.1), and both the audio-only and AV claims include LibriSpeech LM text (Sec. 5.3).

**F7. Low. LCANet chronology is correct under the skill's month rule but is a boundary case; the record should say so.**
Location: Verdict ("The concurrent GRID study [2]"); M06; Refs [2]; plan `deciding_priors`.
Evidence: LCANet v1 is dated 13 Mar 2018 and the target v1 28 Sep 2018, which is 6.5 months by day and exactly 6 by month. SKILL.md fixes dates as YYYY-MM, so [concurrent] follows the rule. The authors cite and discuss it (Sec. 1, ref. [21]).
Effect if counted as prior: none on the verdict. The 0-of-32 absence is for AVSR and LCANet is visual-only, and the M06 verdict is standard for protocol reasons. Novelty is already credited only with qualifiers. If prior, the review could fairly add that the authors cite [2] (Sec. 1) without its finding that the multi-task variant was worse.
Fix: No change required. Optionally note "[2] (2018-03, cited by the authors as [21])" so a reader does not take the label as an excuse for the authors.

**F8. Low. The M06 verdict reasons are valid.**
Location: M06 last sentence ("one dataset, one run, no ablation crediting the objective").
Evidence: These are protocol reasons, not results. They are consistent with SKILL.md: `standard` is used when "the difference is not supported well enough to call".
Fix: None beyond F3.

**F9. Low. The 32.9-point "contradiction" bullet misrepresents a one-line slip as an overreach.**
Location: "Where the claims outrun the evidence", bullet 3.
Evidence: The Abstract ("as the signal-to-noise ratio decreases") and Sec. 7 ("especially at high levels of noise") match Sec. 6 (−5 dB, construction drilling). Only Sec. 1 says "high SNR levels". The claim-table row 23 quotes only Sec. 1.
Fix: Rephrase as "Sec. 1 says 'high SNR levels' where Sec. 6, the Abstract and Sec. 7 mean high noise", or drop the bullet. Add the Sec. 6 quote "32.9% (construction drilling noise) at -5dB".

**F10. Low. The LCANet comparison lacks the context that strengthens it.**
Location: Verdict, second sentence; M06 body.
Evidence: LCANet Sec. 4.C introduces AH-CTC-CE as "a multi-task learning architecture [43]", i.e. the acoustic hybrid. It says "we tried different λ values (from 0.1 to 0.9) and only report the best result". The hybrid was therefore tuned and still lost (4.9 against 2.9 WER, single run, GRID).
Fix: Add "(λ tuned over 0.1–0.9, Sec. 4.C)" after the numbers.

**F11. Low. M12 counts: the variability tally includes a human-listener protocol, and "one-run" is read from a missing mention.**
Location: M12 "Usual approach" ("the 2 with one date from 1999 and 2001"); Verdict ("a one-run noise sweep, as in 20 of 32"); table row M12.
Evidence: The isca-potamianos01_eurospeech match is "three repetitions of the noisy audio-only sequence" (a human perception test). Only talle99 (5-fold cross-validation × 5 initialisations, 95% CI) reports run variability. Not matching a variability regex does not show a single run.
Fix: Write "1 of 32 (1999) gives a run-variability estimate (inference after reading the two matches)". In the Verdict, write "a noise sweep with no variability estimate, as in 20 of 22 noise studies (pattern match)", not "one-run".

**F12. Low. M12 state of the art covers only variability; a read source has the noise-protocol counterpart.**
Location: M12 "State of the art".
Evidence: Auto-AVSR Sec. 4.4 trains with NOISEX babble and tests babble (seen), pink and white (unseen). It notes that the low babble WER is "likely mainly a consequence of the overlapping noise type in the training and testing phases". This is the same seen/unseen issue the review credits to the target.
Fix: Add one sentence: "[6] (2023) keeps babble training and tests seen and unseen types, noting that seen-type results are optimistic (Sec. 4.4)". This makes the target's unseen-only test a point in its favour that later work confirms.

**F13. Low (procedure). Several claim-table quotes do not carry the claim.**
Location: claims.md rows 3, 17, 20, 23, 24.
Evidence:
- Row 3: no quote contains "9.4 million".
- Rows 3 and 20: LRW pretraining is quoted with t18 "trained for 20 epochs".
- Row 17: "babble only" is quoted with t21, which is about a uniform selection of levels.
- Row 23: no Sec. 6 quote.
- Row 24: "early fusion only" is quoted with a noise-type list.
Fix: Use these quotes:
- "The ResNet is first pretrained on LRW for isolated word recognition" (Sec. 5.1).
- "transcriptions of the LibriSpeech corpus which contains 9.4 million words" (Sec. 5.3).
- "babble noise at different SNR levels (0 dB, 5 dB and 10 dB) from the NOISEX database" (Sec. 5.2).
- "32.9% (construction drilling noise) at -5dB" (Sec. 6).
- "we run experiments under varying noise levels (using early fusion)" (Sec. 6).

**F14. Low. Bibliographic details.**
Location: References [2], [5], [7] and the `.bib`.
Evidence and fixes:
- [2]: published at IEEE FG 2018, pp. 548–555 (the target's ref. [21]). Give the venue and keep the arXiv id.
- [7]: the DOI given is the arXiv DOI, while its pages (7613–7617) are ICASSP's. Use the IEEE DOI (10.1109/ICASSP39728.2021.9414567, unverified) or drop the pages.
- [5]: TPAMI early access 2018, final vol. 44(12), 2022, pp. 8717–8727 (unverified). Add the volume and pages, or state "early access 2018".

**F15. Low. The novelty sentence understates the review's own evidence.**
Location: M06 body ("holds only with the authors' qualifiers, audio-visual and in the wild").
Evidence: The Appendix finds 0 of 32 across all sentence-level AVSR, which already supports the Abstract's broader "first ... for audio-visual recognition of speech". The qualifier that matters is "audio-visual" (LCANet is visual-only); "in the wild" is not needed.
Fix: Write "The novelty claim holds for audio-visual recognition (0 of 32, Appendix); in visual-only lip reading, [2] had trained the same objective as a baseline."

**F16. Low. The late-fusion bullet names a gap, not an overreach, and has the wrong locator.**
Location: "Where the claims outrun the evidence", bullet 4.
Evidence: "(using early fusion)" is in Sec. 6 text. The authors claim nothing about late fusion under noise. The claim that does go beyond the evidence is the Sec. 6 ranking "Late fusion performs worse than early fusion", which is tested only in clean audio with one fixed γ = 0.85 (Sec. 5.4).
Fix: Re-aim the bullet at the early-over-late ranking (clean audio only, single γ, one run). Cite Sec. 6 for "using early fusion".

**F17. Low. "Unnamed split" needs a hedge.**
Location: "Where the claims outrun the evidence", bullet 2; M12 body; M11 row.
Evidence: Sec. 4.2 names the standard train, validation and test partitions. Sec. 5.4 tunes all weights on validation. The test partition is implied but never written next to Table 2.
Fix: Write "the partition behind Table 2 and Fig. 3 is not written (test is implied by tuning on validation, Sec. 5.4, inference)".

**F18. Low. Appendix population detail.**
Location: Appendix, "4 studies dated only to 2018 are left out".
Evidence: isca-su18b-crossdomain and isca-su18b_interspeech appear to be versions of one Interspeech 2018 paper. aaai-29926-vishallu ("Visual Hallucination Elevates Speech Recognition") looks misdated in the ledger; it is likely a later AAAI paper (unverified). Neither point changes the 32.
Fix: Write "4 entries (3 studies) dated only to 2018 are left out".

**F19. Low. Body wording: process narration and an "unseen noise" nuance.**
Location: M06 body ("The recall check over 2,236 earlier wiki studies (Appendix) finds one design ..."); M12 body ("the sweep measures robustness to unseen noise").
Evidence: SKILL.md l. 110 bars notes about the review's own process in the body; the recall-check count belongs in the Appendix. Cafe noise contains background speech, so it is not fully unseen relative to babble.
Fix: Write "In visual-only lip reading, LCANet [2] trained CTC and attention losses jointly as a baseline (AH-CTC-CE, Table II, Sec. 4.C) ..." and keep "2,236" in the Appendix. In M12, write "eight noise types other than the training babble".

**F20. Low. verdict.short uses "First".**
Location: verdict.json `short`: "First hybrid CTC/attention AVSR in the ledger (0 of 32 earlier)".
Evidence: SKILL.md l. 111 restricts "first"; the phrase repeats the authors' claim as the review's own finding.
Fix: Write "No earlier sentence-level AVSR study in the ledger (0 of 32) trains hybrid CTC/attention; no CTC- or attention-only result, LRW and LibriSpeech under the LRS2-only claim, one run: all standard."

Not findings. These checked out:
- The population is held at the target's time (before 2018-09).
- The human-perception entries are removed (5 entries, 4 studies), and the huang09b duplicate is merged.
- Afouras [5] is correctly [concurrent], and no [concurrent] or [later] work is treated as prior or as a missed citation.
- The authors' crediting of the acoustic hybrid [20] and of LCANet [21] is reported as theirs (Sec. 1).
- All numbers for the target (8.3, 63.5, 7.0, 8.5, 6.9 points, α = 0.2, λ = 0.1), Auto-AVSR (1.5, 14.6, 3.9 at 380 h) and Ma et al. 2022 (29.5 ± 0.4; target listed at 63.5) match their sources, and the inference arithmetic (79%, 77%, 44%, 16%) is correct.
- Later LRS2 results that might beat 14.6% visual-only or 1.5% AVSR (2024–2026) are unverified here. No better LRS2 figure was located.

## 3. Scores

- Procedure: 7/10. Population, chronology, the read sources and the numbers are sound. The M06 and M07 counts are read as designs, and four claim-table quotes do not carry their claims.
- Final text: 6.5/10. The position is clear and mostly backed. The main verdict uses "runs" where only "reports" is supported, the M07 count is a regex artifact, the position contradicts the body on what produced later gains, and two read sources hold context the text leaves out.

Counts by severity: High 0, Medium 6, Low 14.
