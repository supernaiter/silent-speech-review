# Evaluation: A Cascade Sequence-to-Sequence Model for Chinese Mandarin Lip Reading (CSSMCM)

Evaluator: a language model separate from the writer

Date: 2026-11-28. Target: Zhao, Xu, Song, MMAsia '19, doi:10.1145/3338533.3366579, arXiv:1908.04917 (read as v2 text in the wiki, `papers/arxiv-1908.04917/source/text.txt`). Draft evaluated: `a-cascade-sequence-to-sequence-model-for-chinese-mandarin-lip-reading.md` with `claims.md`, `population.json`, `slots.json` and the three audit files. Sources re-read: the target; LipCH-Net (`doi-10.1609-aaai.v33i01.33019211`, sc_text); LipFormer (`arxiv-2302.02141`); Ma et al. 2022 (`arxiv-2202.13084`); VALLR-Pin (`arxiv-2512.20032`); LIBS (`arxiv-1911.11502`); Zhou et al. 2019 (`arxiv-1811.05250`); and, outside the draft, LRW-1000 (`arxiv-1810.06990`), Shillingford et al. 2018 (`arxiv-1807.05162`), Hirose et al. 2006 (`isca-hirose06b_interspeech`), Cascade-Free Mandarin VSR (`arxiv-2603.21808`).

## Claim table

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Tone stage has no precedent among the 2 prior Mandarin lip-reading decoders (Verdict, M06) | LipCH-Net §Characteristics, §Dataset; Zhou et al. §3; population.json | correct (within the stated population) | Also true of LRW-1000 (see #19), which the population leaves out. |
| 2 | Support is "one 1.59-point CER margin over the authors' re-implementation of LipCH-Net, from one run on one random split" (Verdict) | Target Table 3, §4.2, §3 | wrong (attribution) | 34.07 − 32.48 = 1.59 is right. But the V2P row is 27.96% PER for LipCH-Net-seq, CSSMCM-w/o video and CSSMCM alike, so the "LipCH-Net" baseline shares CSSMCM's own syllable-level first stage. It differs from CSSMCM by adding tone *and* video attention in stages 2–3 (P2C vs VPT2C). It is an ablation that bundles two changes, not a comparison with LipCH-Net, which used pinyin letters, CTC, 1.2M auxiliary sentences and beam search (LipCH-Net §Pinyin-to-Hanzi, Table 4). "One run" is an inference from the lack of any reported repeat. Write "no repeated runs reported". |
| 3 | "The strongest confound is that split" (Verdict) | Target Table 3, §4.3; LipFormer Table IV | wrong (judgment) | The shared-host split raises every system's absolute CER. It does not explain the margin between systems. For the tone claim the strongest confound is the tone+video bundle (#2). The only tone-without-video variant gets *worse*: 42.23% vs 34.07% CER for the no-tone system (Table 3, §4.3). The review quotes 42.23 but never says that it cuts against the tone stage. |
| 4 | All 11 hosts appear in training and test; on unseen hosts CSSMCM rises to 50.08% CER (Verdict, M12) | LipFormer §IV-A Table II ("Overlap Train 11 71452 / Test 11 20418", following [11]); Table IV ("CSSMCM 50.08 32.48") | correct, condition missing | The unseen split is LipFormer's own: 9 training speakers with 81,094 sentences, and 2 test speakers with 20,978 sentences. The 50.08 therefore uses a different training set and test set from Table 3. |
| 5 | "LipFormer's re-run puts CSSMCM at 32.48% on overlapping and 50.08% on unseen hosts, 17.6 points or 54% higher (inference)" (M12) | LipFormer Table IV vs target Table 3 | wrong ("re-run") | 32.48 matches CSSMCM's own Table 3 exactly, as do WAS 38.93 and LIBS-era values. LipFormer copied the overlap value; only the unseen value can be its own run. The arithmetic is correct (17.60; 54.2%), but the gap mixes speaker novelty with a larger training set and a different test set (#4). |
| 6 | "CMLR's labels are unchecked ASR output (§3)" (Verdict, M11) | Target §3 Text Acquisition, Data Generation | correct, but authors' caveat not credited | The paper reports no manual check. The authors do say "there is some noise in these text annotation" and that the timestamps "may have a few uncertain errors" (§3). The claim-table quote for t61 stops before that sentence. Missed internal inconsistency: §1 says CMLR is built from broadcasts "together with subtitles of what is said", while §3 says "there is no subtitle or text annotation in the original 'News Broadcast' program". |
| 7 | CMLR uses iFLYTEK output and its timestamps (M11) | Target §3 | correct | |
| 8 | LIBS [concurrent], same group, 31.27% on CMLR without a tone stage (Verdict) | LIBS abstract, §Experiments, Table 5; arXiv 1911.11502 v1 (Nov 2019) | correct, condition missing | Within ±6 months, so the concurrent label is right; authors Zhao, Xu, Song overlap. LIBS distils from a speech recognizer whose training adds AISHELL audio, so audio enters at training time. Say so before setting it against the tone stage. |
| 9 | Usual approach M06: the 2 priors output characters [5] or cascade picture-to-pinyin and pinyin-to-Hanzi [2] (M06) | Zhou et al. §3; LipCH-Net §Introduction | correct quotes, scope insufficient | Intermediate units are not Mandarin-specific. Across lip-reading decoders before 2019-02, the wiki holds V2P (Shillingford et al. 2018, arXiv 1807.05162: video → phoneme distributions → FST decoder with LM) and character models (LipNet 2016; WAS, arXiv 1611.05358, which surveys phoneme- and viseme-classifying CNNs). LRW-1000 word classes are defined by syllables (target §1). Measure the cascade/intermediate-unit element over all lip-reading decoders and keep the tone element Mandarin-only, or justify the narrower boundary in the Appendix. |
| 10 | VALLR-Pin [later] 7.89% CER on CMLR, from the 9.10% model of Ma et al. (M06 SotA) | VALLR-Pin §III-A, §III-C, Table II | correct, conditions incomplete | The single value comes from an arXiv preprint. Refinement uses a LoRA-fine-tuned Qwen-family 4B LLM over an N-best list plus predicted toneless pinyin (§III-C). The 9.10 is quoted from Ma et al., not re-run. |
| 11 | Ma et al.: 9.1±0.05 over ten runs, Mandarin LM, no phonetic intermediate (M06) | Ma et al. Table 3, Suppl. S5 | correct | Ma et al. also report 8.1±0.05 (best 8.0) with English pre-training and no pinyin (Table 3). Most of VALLR-Pin's margin is reached without any phonetic unit. Worth one clause. |
| 12 | "VALLR-Pin's toneless-pinyin step gains 1.21 points from 9.10 (inference); CSSMCM's tone step gains 1.59 points from 34.07, 4.7% relative" (M06) | VALLR-Pin Table II, Table III; target Table 3 | wrong (not like-for-like) | VALLR-Pin's 1.21 covers the dual pinyin decoder *and* LLM N-best refinement. It is not a pinyin-only step: its own pinyin-decoder-only ablation is 38.60 → 37.23 on a different set (Table III). CSSMCM's 1.59 bundles tone with video (#2). The baselines also differ (9.10 vs 34.07: 13.3% vs 4.7% relative). Drop the juxtaposition or label it as two different interventions. |
| 13 | Tone error falls from 6.99% to 6.14% with video; "verifies the conjecture" rests on a 0.85-point difference (M06, Claims) | Target Table 3, §4.3 | correct; missed point | Arithmetic correct. Missed internal inconsistency: the conjecture concerns "motion of the head" (and, in §1, of the neck), but the input is 64×128 grayscale lip crops (§4.1), so head and neck motion is largely outside the frame. The quoted slip ("VP2T ... predicting the pinyin sequence") is correctly reported. |
| 14 | Authors report tone without video is worst overall, 42.23% CER, from error accumulation (§4.3) (M06) | Target §4.3 | correct, credited | The authors give two reasons: "lack of visual information" and "accumulation of errors". |
| 15 | "LipCH-Net names intonation marks only within pinyin" (M06) | LipCH-Net §Characteristics ("initial, vowel and intonation mark"), §Picture-to-Pinyin (CTC over "Pinyin letter labels") | insufficient evidence | LipCH-Net never says whether its CTC labels carry tone marks. Rephrase: "LipCH-Net describes intonation marks as part of pinyin and does not say whether its picture-to-pinyin labels carry them." |
| 16 | The visual tone correlates behind the design (§1) "come from analyses such as" Attina et al. [8] (M06) | Target §1, ref [6] | wrong citation target | The target's stated basis is Chen & Massaro 2008, "Seeing pitch: Visual information for lexical tones of Mandarin-Chinese", JASA 123(4), 2356–2366 (target ref [6]), a perception study. Attina et al. is not cited by the target. Name Chen & Massaro through the target's citation. Attina can stay as extra support. |
| 17 | "Across signals the closest earlier design is sEMG tone classification of Thai monosyllables from one subject [9]" (M06) | wiki `isca-hirose06b_interspeech`; target §5 and ref [5] | wrong (closer priors exist) | Hirose et al., Interspeech 2006 (in the wiki): a separate tone recognizer for continuous Standard Chinese speech, applied per syllable after segmentation (one female speaker, 86.9%). It also states that "in most current systems ... syllable tone types are not utilized". The target's own §5 cites Chen et al., Eurospeech 1997 [5] for "syllable initial/final with tone", "syllable with tone" and "preme/toneme" units in Mandarin ASR. Both are earlier, Mandarin, continuous-speech designs and closer than Thai sEMG monosyllables. The full-text scan matched Hirose 2006 but the Appendix does not report it. I found no visual or silent-speech tone recognizer before 2019-02 in the wiki. |
| 18 | Of 53 [later] decoders, 10 mention pinyin and 3 tone prediction (M06) | M06 audit `usual_approach.note` | correct, qualification dropped | The audit says the 3 include one that describes the target, and the concurrent tally also has pinyin 1 and cascade 3. The review omits both. |
| 19 | M11 usual approach: priors use checked manuscripts; "0 ASR-generated" (M11, Appendix) | LRW-1000 `arxiv-1810.06990` §III-C | wrong (prior missing) | LRW-1000 (arXiv Oct 2018) is a prior Mandarin benchmark with three baseline decoders, cited by the target (§1, ref [14]). It used an iFLYTEK ASR tool and compared its output "again with the manually checked transcripts" over "several rounds of interleaved manual and automatic check". The population excludes it as a dataset paper, but CSSMCM is itself half a dataset paper, and word-level LRW-1000 decoders (Multi-Grained, TCN) are included. With LRW-1000 the prior practice is ASR-assisted *and* manually checked, which makes the M11 contrast sharper. |
| 20 | LipCH-Net 20,495 sentences, broadcast manuscripts checked by two persons (M11) | LipCH-Net §Dataset | correct | Its timestamps are automatic (OksrtClient, ">95% accuracy"). |
| 21 | M11 SotA: CMLR references reused unchanged by Ma et al. and later studies, "with no label audit" (M11) | Ma et al. Table 3; LipFormer; VALLR-Pin | insufficient evidence | This line gives no result on the reference-construction step. The "no label audit" absence claim covers only the three papers read. Name a labelled-reference practice with its condition, or mark "–" as other slots do. |
| 22 | M12 usual approach: LipCH-Net splits 7:1:2 with every speaker in each partition; 0 of 2 priors report run-to-run variability (M12) | LipCH-Net §Dataset | correct quotes, scope insufficient | LRW-1000 splits so that "there are no or few overlapped speakers" across partitions (§IV), a speaker-separated Mandarin prior. Speaker split and run variability do not depend on language. LipNet's unseen-speaker GRID protocol (2016) and LRS3's disjoint-video split (arXiv 1809.00496) are prior lip-reading practice. |
| 23 | M12 SotA: LipFormer (2023) 43.18% CER on unseen speakers, 27.79% overlap (M12, table) | LipFormer Table IV; `arxiv-2603.21808` Table III | outdated | Cascade-Free Mandarin VSR (Yang et al., arXiv 2603.21808, 2026; in the population): 38.23% CER unseen (s2 and s6 held out) and 20.38% on the official 7:1:2 split, video only, single run. It also lists CTCH-LipNet 22.02 / 62.47 and CT-MIR-Net 21.45 / 51.38. Its Table IV ablation removing phoneme and viseme representations (35.25 / 49.78) is also the most direct later evidence on M06's own step. |
| 24 | Ma et al. list the re-implementation's 34.0 as LipCH-Net (Claims) | Ma et al. Table 3 ("LipCH-Net [7] - CMLR 61 34.0") | correct | Propagation continues: `arxiv-2603.21808` Table III lists "LipCH-Net 34.07". Because of the shared V2P row (#2), the mislabel is stronger than the review says. |
| 25 | Overall PER 36.22% exceeds V2P's 27.96%; Table 3 does not say whether sub-network rows take reference inputs (Claims) | Target Table 3 | correct; hedged where a plain statement is available | The pattern holds for the whole table (LipCH-Net-seq 39.52, w/o video 46.67), so it more likely reflects how overall PER is defined than a CSSMCM-specific fault. VPT2C 3.90% CER is below its own input's 27.96% PER, so the sub-network rows can only come from reference inputs (inference). Say so plainly. |

Dating check (task item 1): LipCH-Net was presented at AAAI-19 (27 Jan–1 Feb 2019), more than 6 months before 2019-08-14. Its OJS/Crossref online date, 2019-07-17, falls inside the window. The target cites it, re-implements it and builds on it ("Same as [15]", §1), so treating it as prior is fair. Give both dates in reference 2. LIBS (2019-11), Multi-Grained (2019-08), Hsieh et al. (2019-09) and TCN (2020-01) are correctly concurrent. No later or concurrent work is treated as a missed prior.

Counts: 25 claims checked.
- Correct: 6 (#1, 7, 11, 14, 20, 24).
- Correct, condition missing: 4 (#4, 6, 8, 10).
- Correct, but scope or qualification insufficient: 5 (#9, 13, 18, 22, 25).
- Wrong: 7 (#2, 3, 5, 12, 16, 17, 19).
- Outdated: 1 (#23).
- Insufficient evidence: 2 (#15, 21).

Fixes: 3 high, 6 medium, 6 low.

## Required fixes, by impact

### High
1. **Central claim attribution (#2, #3, #12, #14).** Rewrite the Verdict and M06 to say three things:
   - The 1.59-point margin compares CSSMCM with its own first stage plus a pinyin-only character network, so it bundles the tone stage with video attention in stages 2–3.
   - The only tone-without-video comparison goes the other way: 42.23% vs 34.07% (Table 3; the authors' own §4.3 explanation, credited).
   - This bundle, not the shared-host split, is the strongest confound for the tone claim.

   Drop the VALLR-Pin 1.21 vs CSSMCM 1.59 juxtaposition, or label it as two different interventions on different baselines.
2. **Population boundary (#9, #19, #22).**
   - Add LRW-1000 (arXiv 1810.06990, Oct 2018, target ref [14]) as a prior Mandarin decoder study. It changes M11 to ASR-assisted with manual checks and adds 1 ASR-generated label prior. It changes M12 to 1 speaker-separated prior.
   - For the intermediate-unit element of M06 and for all of M12, measure over all lip-reading decoders: V2P phonemes 2018, LipNet unseen speakers 2016, LRS3 disjoint split. Otherwise state in the Appendix why a Mandarin-only boundary is used.
   - Keep the tone element Mandarin-only. Recount the prior denominators.
3. **Tone precedents (#16, #17).**
   - Replace "the closest earlier design is sEMG Thai" with Hirose et al. 2006 (Interspeech, in the wiki; separate tone recognizer for continuous Mandarin) and with the target's own ref [5], Chen et al. 1997, on tonal units in Mandarin ASR. Keep Srisuwan 2012 as the cross-signal example.
   - Name Chen & Massaro 2008 (target ref [6]) as the source of the visual-tone motivation. The draft cites Attina instead.
   - "Standard" stays right, and is better supported: explicit tone modelling was established in Mandarin recognition. Only its use in a lip-reading cascade is new.

### Medium
4. **"Re-run" (#5).** 32.48 is copied from CSSMCM's paper. Also state that the 50.08 unseen figure uses LipFormer's 9/2 split, with 81,094 training and 20,978 test sentences against 71,452 and 20,418. The 17.6-point gap therefore is not a pure speaker effect.
5. **M12 state of the art (#23).** Replace LipFormer 43.18 with Cascade-Free Mandarin VSR (2026) 38.23% CER on unseen speakers (s2 and s6 held out; 20.38% on the official split). Consider citing its phoneme and viseme ablation (Table IV) on M06's own step.
6. **Authors' caveats and missed inconsistency (#6).**
   - Credit §3's "there is some noise in these text annotation" and the timestamp caveat to the authors.
   - Add the §1 vs §3 contradiction: "together with subtitles" vs "no subtitle or text annotation".
7. **Head-motion conjecture vs lip-only input (#13).** Add that §4.3 claims to verify a head-motion conjecture with 64×128 lip crops (§4.1).
8. **LIBS condition (#8).** Note the audio-distilled teacher and the extra AISHELL speech data.
9. **M11 state-of-the-art line (#21).** Give a result on the reference-construction step, or use "–". Scope "no label audit" to the papers read.

### Low
10. Rephrase "standard by our rules" (process narration) as "standard: no repetition across seeds, speakers or datasets, so it cannot be judged ahead". Replace "one run" with "no repeated runs reported".
11. Table 3: state plainly that the sub-network rows must use reference inputs (inference), and that overall PER above V2P PER holds across the whole table (#25).
12. Appendix:
    - Say that the 3 later tone-prediction matches include one describing the target, and report concurrent pinyin 1 and cascade 3 (#18).
    - The recall-sample description omits an sEMG Mandarin silent-speech decoder (pmc-9312762) and a whispered-Mandarin corpus paper.
    - Report Hirose 2006 among the full-text matches.
13. Later cascades missing from the ledger: CTCH (Ma, Wang, Lin, IEEE DSC 2020, 22.0% CER) and CT-MIR-Net (Ma & Wang, ICIP 2022, 21.45%). Both are known through Ma et al. Table 3 and arXiv 2603.21808 Table III and should be labelled that way. They show the cascade line continued after CSSMCM.
14. LipCH-Net intonation sentence: rephrase as in #15.
15. References:
    - Duplicate "[Later] … [later]" and "[Concurrent] … [concurrent]" tags in refs 3, 4, 6 and 7.
    - Ref 1 has no pages: Ma et al. cite "1–6" (unverified).
    - Ref 2: add the OJS date 2019-07-17 next to the conference date.

Outside knowledge I could not locate: a visual Mandarin, Cantonese or Thai tone recognizer before 2019-02, and the two-stage base-syllable-plus-tone Mandarin dictation systems of the 1990s. Both are unverified and not required fixes.

## What holds up
- Every numeric value in the claim table matches its source: Table 3, LipFormer Table II and IV, Ma Table 3, VALLR-Pin Table II, LIBS.
- The chronology labels are right, and no later work is presented as a missed prior.
- The critique of the abstract's state-of-the-art claim, and Ma et al.'s mislabelled 34.0, are well founded.

## Scores
- Procedure: 6/10. The population was well documented and dated. But it excluded a prior that the target itself cites (LRW-1000), it is Mandarin-only for language-independent slots, and it did not report closer tone precedents found in the scan.
- Final text: 5/10. The numbers are accurate, but the central causal reading of the tone margin is wrong, the strongest confound is misidentified, one citation target is wrong, and one state-of-the-art line is outdated.
