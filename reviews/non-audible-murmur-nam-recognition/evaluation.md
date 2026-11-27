# Evaluator: a language model separate from the writer

Review: non-audible-murmur-nam-recognition (Nakajima, Kashioka, Campbell, Shikano, "Non-Audible Murmur (NAM) Recognition", IEICE Trans. Inf. & Syst. E89-D(1), 2006, doi:10.1093/ietisy/e89-d.1.1; English version of IEICE Trans. D-II J87-D-II(9):1757-1764, Sept. 2004). Date of evaluation: 2026-11-27.

Sources checked: target English text (wiki doi-10.1093-ietisy-e89-d.1.1, source/sc_text.txt) and Japanese version (ieice2004-nakajima-nam-recognition, sc_text.txt: Table 1, received 2004-02-16, published 2004-09); ICASSP 2003 (doi-10.1109-icassp.2003.1200069); Eurospeech 2003 (isca-nakajima03_eurospeech); ASRU 2003 (asru2003-heracleous-iterative-mllr-nam); EUSIPCO 2004 (naist-4544); EURASIP 2007 (eurasip2007-heracleous-tissue-conductive); SPECOM 2005 (naist-4825, reference list); Tatara 2002; Jou 2004; Graciarena 2004; Manabe 2003; Whisphone 2025. DOIs of [3], [4], [8], [9], [10] resolved at doi.org and match the reference list.

Version check: the wiki text is the target article (English 2006 version). The Japanese 2004 version has the same Table 1 (A 93.3 / B 90.0 / C 89.2 / D 88.4). First public 2004-09 and the window 2004-03 to 2005-03 are correct.

## Claim table

| # | Claim (location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Rows A–C of Table 1 equal the 2003 table (Verdict; "Where the claims outrun") | Target Table 1; ICASSP 2003 Table 1; Japanese Table 1 | correct | They are identical at the printed precision: Acc 93.33/90.00/89.17 and Sub, Del, Ins, Err and S.Err all match. |
| 2 | Training set grew from 2,100 files to about 4,610 utterances (inference) | Target §3.5; ICASSP §4.5 | correct | 525×4 + 1,255×2 = 4,610. The review cannot tell whether the 2003 description or the 2004 description of the training set is incomplete. The question to the authors handles this correctly. |
| 3 | Whispered 20,000-word Japanese dictation with the same decoder existed in 2002 [4] | Tatara §5.2 | correct | 20,000-word vocabulary, julius-3.1, close-talking (air) microphone. |
| 4 | 74%, 4 speakers, speaker-independent [4] | Tatara §5.2–5.3, Table 3 | insufficient evidence | The 74% and the 4 test speakers are correct. Tatara reports a "recognition rate" and does not define it as word accuracy. The paper also does not state that the test speakers are disjoint from the 80 training speakers. |
| 5 | A close-talking microphone kept 91.7–91.9% in TV and music [5] | EUSIPCO Table 2 | correct, but selective | The same table shows audible speech through the NAM microphone at 93.8 (quiet), 93.2 (TV) and 92.9 (music), so the NAM microphone lost less accuracy. See fix 1. |
| 6 | Live noise at 60 dBA cut NAM accuracy to 53.3%; 83.7% clean; four noises [6] | EURASIP 2007 §3.2 | correct, conditions missing in the Verdict | Silicone microphone, a different (female) speaker, 100 adaptation utterances. With noise superimposed at 50 and 60 dBA, accuracy stayed close to clean. |
| 7 | 93.9% silicone vs 88.9% stethoscopic, one speaker, 20K [6] | EURASIP 2007 §3.1 | correct | 350 adaptation and 48 test utterances, male speaker. The same 93.9% was already reported in 2005 (naist-4824, naist-4825). |
| 8 | "The best later result on the task, 93.9%, has barely moved" (Verdict) | Audit sota_candidates (ledger only) | insufficient evidence | No search of later NAM dictation results is documented. The year is the 2007 repeat, not the 2005 first report. |
| 9 | Both prior body-conducted recognizers are the group's own (M05) | naist-4825 refs [7], [8]; Graciarena 2004 ref [4]; M05 audit prior_note | wrong / incomplete | Graciarena, Franco, Sonmez, Bratt, IEEE SPL 10(3):72–74, March 2003 (throat plus standard microphone, robust ASR) and Strand et al., ASRU 2003, pp. 315–320 (in-ear earplug ASR in extreme noise) both predate 2004-03. The audit itself notes Graciarena 2003. |
| 10 | Throat microphone "still the most common site over all years (41 of 82, slot-filled)" | M05 audit usual_approach note | wrong as stated | The audit says the ledger files the NAM site below the mastoid under "neck" for several NAM papers, so 41 is not a count of throat microphones. |
| 11 | Site chosen by listening and spectra; no rate for any other site (M05) | Target §3.3 | correct, but credit is missing | The authors say this themselves: other sites "failed to obtain a recognition rate sufficient to be evaluated using numerical values", and the bone-conduction earphones gave a poor S/N (§3.3). |
| 12 | 3 of 4 prior unvoiced recognizers run LVCSR; fourth is EMG 5 vowels [10] (M04) | Tatara; Manabe abstract; audits | correct for the counted set; set incomplete | Ito, Takeda, Itakura, "Acoustic analysis and recognition of whispered speech", IEEE ASRU 2001, pp. 429–432, is cited in wiki sources and is missing. Two of the three LVCSR studies are the target group's own. |
| 13 | Authors concede the NAM/whisper boundary is vague (§3.1) | Target §3.1 | correct | Credited to the authors. |
| 14 | 19.3-point gap says nothing about speaking mode (inference) | Arithmetic; Tatara | correct | The metrics may also differ (see #4). |
| 15 | Retraining with 2,100 files [2]; iterative MLLR with 350 utterances, 88.62% on 72 utterances [7] | ICASSP §4.5; ASRU abstract, §3.1–3.2 | correct | 88.62% uses PTM initial models. |
| 16 | Tatara's unadapted normal model gave 27% [4] | Tatara §5.3 | correct | |
| 17 | 90.83% vs 88.62%: 6× the data for 2.21 points, different initial models (M03) | ICASSP Table 1 Sum/Avg; ASRU §3.1–3.2 | correct arithmetic, misleading comparison | With the same kind of monophone initial models, iterative MLLR reached 71.09% (ASRU §3.1, 200 utterances). |
| 18 | "No unadapted baseline is given" plus question 4 | Target; ASRU §3.2; EUSIPCO §1 | correct for the target; the question is already answered | Unadapted normal-speech PTM models score −0.81% on the same 72 utterances [7], [5]. |
| 19 | Paper keeps retraining and names MLLR without running it (§3.5) | Target §3.5 | correct | |
| 20 | Both prior studies expose the sensor to noise physically; neither states a level or an air baseline (M12) | ASRU §3.1; ICASSP §6 | correct for the two counted; set incomplete | The missing priors in #9 are noise-robust ASR studies with a standard microphone. |
| 21 | 44 of 123 unique studies (M12), pattern match | M12 audit note | mention count presented as a design count | The audit calls these full-text "named in" counts and upper bounds, with papers naming both protocols counted in both. |
| 22 | TV news: 93.3→89.2, 62% more errors; close-talking 94.4→91.7, 48% more errors (inference) | Target Table 1; EUSIPCO Table 2 | arithmetic correct; conclusion wrong | 10.83/6.67 = 1.62 and 8.3/5.6 = 1.48. "The NAM degradation is no smaller" compares different speaking modes, models, sessions and uncalibrated noise, and ignores the like-for-like NAM-microphone row (#5). |
| 23 | Whisphone: WER mostly <10% up to 80 dB(A), one speaker, 2025 [11] | Whisphone §2.2–2.3 | correct, conditions missing | 15 fixed Japanese phrases × 3, off-the-shelf Google Voice Search and Whisper large-v3, no adaptation, ANC earbud, whisper (not murmur). |
| 24 | Test and training text both Mainichi; no disjointness stated; same speaker (Where the claims outrun) | Target §3.5–3.6; ICASSP §6 | correct, credit missing | ICASSP §6 calls it an "open test" with newly recorded data. If rows A–C used the ATR-only 2003 model, overlap with the JNAS text can only affect row D, which conflicts with the review's own inference. |
| 25 | Chronology labels: [5], [8], [9] concurrent; [6], [11] later; 2003 papers and Tatara 2002 prior | Manifests; Japanese received 2004-02-16 | correct | No work the authors could not have read is treated as prior or as a missed citation. |

## Required fixes (ordered by severity)

1. **Major. Location: M12 component section ("The NAM degradation is no smaller") and the Verdict sentence on noise robustness.**
   - Evidence: EUSIPCO 2004 Table 2 [5] has a like-for-like row the review leaves out. With the same speech, the same session and the same noise, the NAM microphone went from 93.8 to 93.2 (TV) and 92.9 (music). The close-talking microphone went from 94.4 to 91.7 and 91.9. The review sets NAM murmur on a retrained monophone model (target) against audible speech on an MLLR-adapted PTM model (EUSIPCO), in different recording sessions, with no noise level in either.
   - Fix: report both rows of [5]. Drop "no smaller". State instead that the target's noise test cannot support robustness without a level and a same-session air baseline. The concurrent same-group data show a smaller loss for the NAM microphone under those conditions, but with audible speech.
2. **Major. Location: M05 usual approach ("both prior body-conducted recognizers are the group's own", 2 of 2); M12 usual approach (2 of 2, "neither states a level or an air-microphone baseline"); Appendix M05 and M12 dated counts.**
   - Evidence: two recognizers that predate 2004-03 are missing. One is Graciarena, Franco, Sonmez, Bratt, "Combining standard and throat microphones for robust speech recognition", IEEE Signal Processing Letters 10(3):72–74, March 2003. The other is Strand, Holter, Egeberg, Stensby, "On the feasibility of ASR in extreme noise using the PARAT earplug communication terminal", Proc. ASRU 2003, pp. 315–320. Both are cited in naist-4825 refs [7] and [8], and Graciarena 2003 is also cited in Graciarena 2004 ref [4]. Zheng et al., ASRU 2003, pp. 249–253 (air- and bone-conductive microphones) is a possible third prior; whether it has a recognizer is unverified. The M05 audit records Graciarena 2003 but the text omits it.
   - Fix: add these works to the dated populations, labelled as described through the citing paper if they cannot be read. Restate the M05 usual approach: at 2004-03, conducted-sensor recognizers outside the group used a throat microphone or an in-ear earplug together with a standard microphone in noise. Recheck the M12 "neither states a level or air baseline" claim against them.
3. **Major. Location: Verdict sentence 1 ("all three are standard, being the design of the group's 2003 reports"); the M05, M04 and M03 verdict lines; verdict.json.**
   - Evidence: the 2003 ICASSP and Eurospeech reports are the same experiment, since rows A–C are identical. In M05 and M12 the "usual approach" population consists only of that earlier report plus ASRU 2003 from the same group. A design that only the authors had used is not field practice, so the stated reason for `standard` is circular. Under the rule, `standard` here is correct because one speaker gives no repetition, not because the design is common.
   - Fix: state the verdict reason as no repetition (one speaker, speaker-dependent). Credit the design to the authors' own 2003 reports and say plainly that before 2004-03 no independent group had used a NAM microphone or recognized murmur. Either date the experiment to its first public report (ICASSP 2003; ASJ March 2003, target ref [8]) or justify keeping 2004-09 in one sentence.
4. **Major. Location: M05 usual approach ("still the most common site over all years (41 of 82 unique studies, slot-filled)").**
   - Evidence: the M05 audit note says "the ledger files the NAM site below the mastoid under neck for several NAM papers". The 41 therefore mixes throat microphones with NAM microphones.
   - Fix: re-tally neck sites without the NAM papers, or drop the claim.
5. **Moderate. Location: M03 section ("6 times the data for 2.21 points"; "No unadapted baseline is given"); Questions for the authors, item 4.**
   - Evidence: ASRU 2003 §3.1 reports that iterative MLLR on monophone initial models, the same model type as the retraining, reached 71.09% (200 utterances, 5 iterations). The 88.62% comes from PTM models. ASRU §3.2 and EUSIPCO §1 report −0.81% for the unadapted normal-speech PTM models on the same 72 utterances.
   - Fix: add the monophone-to-monophone comparison (90.83 vs 71.09). Cite −0.81% as the group's unadapted baseline, and replace question 4 or narrow it to the target's monophone model.
6. **Moderate. Location: M04 and M03 usual approach and the Appendix (prior 4; prior 3); the target reference list.**
   - Evidence: Ito, Takeda, Itakura, "Acoustic analysis and recognition of whispered speech", IEEE ASRU 2001, pp. 429–432 is cited in wiki sources. The same work is also cited as Itoh et al., ICASSP 2002, vol. 1, pp. 389–392. It is a whispered-speech recognizer from Tatara's group, and its transfer method is unverified. The target's own reference [8] (Nakajima et al., Proc. ASJ, pp. 175–176, March 2003) is not named. From outside knowledge, unverified locators: Jorgensen, Lee, Agabon, sub-auditory EMG word recognition, IJCNN 2003; Sugie and Tsunoda, EMG vowel discrimination, IEEE Trans. BME 1985.
   - Fix: name these works, read Ito 2001 if obtainable, and recount "3 of 4" and "2 of 3".
7. **Moderate. Location: Verdict, last sentence ("the best later result on the task, 93.9%, has barely moved"); SOTA lines for M03, M04 and M05 ("2007").**
   - Evidence: the 93.9% first appears in 2005 (naist-4824, Grenoble sOc-EUSAI 2005; naist-4825, SPECOM 2005), and Heracleous et al., Interspeech 2004 gives 93.5%. The sota_candidates are ledger-only, and no later search of NAM dictation is shown. Possible later candidates were not checked: Babani et al., ICASSP 2011; Heracleous and Hagita, audiovisual NAM 2010; Yang et al., ISCSLP 2012.
   - Fix: date the result to 2005 with its conditions (silicone microphone, 350 MLLR utterances, 48 test utterances, male speaker). Either document the later search or limit the claim to "the best in the audited ledger".
8. **Moderate. Location: M12 usual approach ("44 of 123 unique studies"); Appendix M03 ("fine-tuning 86, retraining 81, MLLR 36, SAT 17, MAP 10"); Appendix M12 ("physically present 44, digital 15").**
   - Evidence: the audits describe these as full-text "named in" pattern counts and as upper bounds. The retraining regex includes "re-estimat", which matches any Baum–Welch HMM paper.
   - Fix: label them as mention counts (pattern match, mentions), or remove them from the usual-approach sentences.
9. **Minor. Location: M12 state of the art and the 13-components table.**
   - Evidence: Whisphone §2.3 used 15 fixed Japanese phrases × 3, Google Voice Search and Whisper large-v3 with no adaptation, an ANC earbud and a single male subject.
   - Fix: add these conditions, especially the fixed phrase set, the off-the-shelf recognizer and the whisper mode. Consider whether a NAM-microphone noise study (Yang et al., ISCSLP 2012, VTS compensation; values unverified) fits the step better.
10. **Minor. Location: Verdict ("[later] live noise at 60 dBA cut NAM accuracy to 53.3%").**
    - Evidence: EURASIP 2007 §3.2 used a silicone microphone, a different (female) speaker and 100 adaptation utterances, starting from 83.7% clean. With superimposed noise at 60 dBA, accuracy stayed close to clean, and the group attributes the drop to the Lombard reflex (naist-4825 abstract).
    - Fix: add the conditions and the 83.7% starting point to the Verdict.
11. **Minor. Location: M04 ("74% on 4 speakers, speaker-independent").**
    - Evidence: Tatara §5.3 gives a "recognition rate" without defining the metric, and does not state that the test speakers are disjoint from the training speakers.
    - Fix: write "recognition rate" and drop "speaker-independent", or mark it as inference.
12. **Minor. Location: M05 ("no recognition rate is reported for any other site or sensor"); "Where the claims outrun the evidence", test-independence bullet.**
    - Evidence: the authors state the failure at other sites and with bone-conduction earphones themselves (§3.3), and ICASSP §6 calls the test "an open test". The review's own inference that rows A–C used the ATR-only model limits the overlap concern to row D.
    - Fix: credit §3.3 and the "open test" statement. Say that text overlap with JNAS can matter only for row D, unless rows A–C used the JNAS-augmented model.
13. **Minor. Location: verdict.json "position" vs the md Verdict; "B–D are described only qualitatively (Table 1)".**
    - Evidence: verdict.json cites [@heracleous2003accurate] as one of "the group's 2003 reports", but the md cites [2] and [3]. The descriptions of the B–D environments are in §3.6, not in Table 1.
    - Fix: align the two texts and change the location to §3.6.

Checked with no fix needed: English only; no model names; no process disclaimers in the published text; bibliographic DOIs of [3], [4], [8], [9] and [10] resolve to the stated papers; chronology labels are correct; the authors' noise caveats (§3.6) and the NAM/whisper boundary (§3.1) are credited.

## Scores

- Procedure: 5/10. The version check, dating, chronology and most quotes are sound. However, the prior populations for M05 and M12 miss conducted-sensor recognizers cited in wiki sources, one of which the audit itself records. Mention counts and a misfiled slot count are presented as design counts, and a comparator table is quoted selectively.
- Final text: 5/10. The text is clear, takes a position and gives exact numbers. The central noise-robustness argument, however, rests on a cross-condition comparison contradicted by the cited table's own like-for-like row. The `standard` verdicts are justified by self-precedent, and the "barely moved" state-of-the-art claim lacks support.

## Final counts by severity

Critical 0, major 4, moderate 4, minor 5 (total 13).
