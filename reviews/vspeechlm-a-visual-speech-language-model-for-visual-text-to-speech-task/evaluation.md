# Evaluator: a language model separate from the writer

Date: 2026-11-24. Target: VSpeechLM (Wang et al., MMAsia '25, arXiv:2511.22229 v1).
Inputs: evaluator-brief.md, compact.md (review and claim table). Source text grepped for checking: papers/arxiv-2511.22229/source/sc_text.txt (target) and papers/arxiv-2603.14267/source/sc_text.txt (DiFlowDubber, Tables 1–2 only). No other writer files were read. Outside knowledge that I could not locate in a source is marked "unverified".

## Claim table

| No | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Per-frame phoneme aligner feeds a codec LM; baselines are duration-based or flow (Verdict) | Target §3.3.2 Eq. 4, §4.1 "Baselines" | correct | §4.1: three FastSpeech2-like baselines, EmoDubber flow matching. |
| 2 | "the authors themselves cite an earlier speech-LLM dubbing system (§2.1)" (Verdict) | Target lines 105–108 | wrong location | DubWise [24] is cited in §1 Introduction, not §2.1. §2.1 names only FastSpeech2 and flow-matching VisualTTS. The authors also say DubWise controls only global duration, which weakens it as evidence that the design is "standard". |
| 3 | Chem WER 12.5 vs EmoDubber 12.8 (Verdict, M06) | Target Table 1 | correct | 2.3% relative, arithmetic correct. |
| 4 | DiFlowDubber 9.65 vs 11.72 for "the same baseline" (Verdict, M06 SOTA) | DiFlowDubber Table 1 | correct numbers, wrong setting pairing | 9.65 and 11.72 are Setting 1.0 (ground-truth reference). VSpeechLM's copied baseline values match DiFlowDubber's **Setting 2.0** (non-GT reference) exactly: EmoDubber 12.8/12.81, StyleDubber 14.2/14.18, HPMDubbing 29.8/29.82 (Chem); EmoDubber 19.8/19.75, StyleDubber 19.6/19.58, HPMDubbing 44.2/44.15 (GRID). The matched comparison is Chem 11.12 vs 12.81 (13.2%, inference) and GRID 16.21 vs 19.75. |
| 5 | GRID 16.79 vs 18.53 (M06 SOTA) | DiFlowDubber Table 2 | correct numbers, same setting issue | Setting 1.0 again; Setting 2.0 is 16.21 vs 19.75. |
| 6 | 17.7% relative for DiFlowDubber (M06 SOTA, inference) | arithmetic | correct | (11.72−9.65)/11.72 = 17.7%. |
| 7 | "Absolute values use different ASR systems" (M06 SOTA) | Target Table 1 caption; DiFlowDubber §4.1 | insufficient evidence | The baseline values match to rounding across both papers, which suggests both copied the same EmoDubber-paper numbers. The review does not show that the ASR differs for those rows. |
| 8 | MCD-DTW-SL claims 17.6% / 60.9% do not follow; 18.9% and 39.3% (Where claims outrun) | Target §4.2, Table 1 | correct | 6.51→5.28 = 18.9%; 6.42→3.90 = 39.3%. 60.9% does not match any baseline either (DSU 10.6→3.90 = 63.2%, inference). |
| 9 | GRID tie with EmoDubber, 3.92 vs 3.90 | Target Table 1 | correct | |
| 10 | Argmax per frame, CE on MFA labels, no monotonic constraint (M06) | Target §3.3.2, §3.5.1 | correct | Missed point: the decoder trains on the ground-truth expanded sequence G and infers on the predicted P_exp (§3.5.3), a train/test mismatch that bears on the argmax-error question. |
| 11 | Hegde et al. attention plus upsampling (M06) | Claim-table quote | correct (quote) | |
| 12 | Chem 12.48 vs 15.02 without video (Table 2); 151% without pretraining (Table 3) | Target Tables 2–3 | correct | |
| 13 | AV-HuBERT, 25 fps; EnCodec 8 codebooks, 16 kHz (13-component table) | Target §3.2 | correct | |
| 14 | MCD-DTW-SL is the only sync metric (M12) | Target §4.1 | correct | |
| 15 | DiFlowDubber Chem LSE-C 8.31, LSE-D 6.73, GT vs non-GT reference (M12 SOTA) | DiFlowDubber Table 1 | correct | |
| 16 | Reference utterance not stated (M12) | Target §3.2 | correct | The review can go further (see fix 1): the copied baselines are Setting 2.0 values. |
| 17 | 6 of 7 report LSE; "only two of the six are prior"; verdict standard (M12) | DiFlowDubber Table 1 | wrong conclusion | V2C-Net, HPMDubbing, StyleDubber, Speaker2Dubber, ProDubber and EmoDubber, all prior (2022–2025) text-and-video dubbing systems, have LSE-C/LSE-D on Chem and GRID. Four of them are VSpeechLM's own baselines. LSE is the established protocol before the target, so "standard" does not follow. |
| 18 | Usual approach M06: diffusion 5, flow 4, mel 4 over 7 studies | Target §2.1; DiFlowDubber Table 1 | doubtful | The population leaves out the V2C dubbing line that the paper compares against. Target §2.1 itself says that earlier VisualTTS models are "primarily based on FastSpeech2 … or flow-matching". Diffusion as the most common decoder is implausible for this task, and the Appendix's "upper bound, related-work mentions included" caveat is dropped in the body. |
| 19 | "2 mention a codec-token language model, this paper and FunCineForge" | outside knowledge | likely wrong (unverified locator) | VoiceCraft-Dub (Sung-Bin et al., arXiv:2504.02386, 2025) is a neural-codec-LM dubbing system conditioned on text, lip video and reference speech. It is about 7 months before the target, so it counts as prior. |
| 20 | Baseline WER/MCD copied; UTMOS, Spk Sim regenerated (Where claims outrun) | Target Table 1 caption | correct | The caption also says "we follow the same computing methods as the baselines". "Rests on other papers' ASR setups" is fair, but it should mention that claim. |
| 21 | UTMOS 3.73 (Tables 1–2) vs 3.87 (Table 3) | Target Tables 1–3 | correct | 3.87 is also EmoDubber's Chem UTMOS in Table 1, so a transcription slip is plausible (inference). |
| 22 | GRID split: 33 × 100 ≠ 900 (Where claims outrun) | Target §4.1 | correct | Also 32,670 + 900 = 33,570 is more than 33 × 1,000 = 33,000 clips. |
| 23 | GRID GT 22.5% vs VSpeechLM 18.3%: "the ASR bounds that column" | Target Table 1, footnote 2 | correct, but the authors state it | Footnote 2 explains the GRID ASR errors on ground-truth audio ("lay"→"they"). The review presents this as its own finding without credit. |
| 24 | Human study: EmoDubber on Chem, StyleDubber on GRID; "reports no tie rates, blinding or uncertainty" | Target §4.3, Fig. 3 caption | partly wrong | §4.3 says that raters could declare a tie, and Fig. 3 shows "win-tie-loss ratios"; the text also discusses "many ties" on GRID. "No tie rates" is wrong. No blinding and no uncertainty is correct. 50 clips per dataset and 10 experts are not stated in the review. |
| 25 | LRS2 16.1 vs 91.4–198% WER; baselines' training not stated (Table 4) | Target Table 4, §4.5.3 | correct | Missed: Spk Sim scale is inconsistent in Table 4 (GT 1.00, systems 10.3–53.9). |

## Required fixes, ordered by impact

1. **Setting mismatch in the central WER comparison (Verdict, M06 SOTA, table row M06).** VSpeechLM's copied baseline numbers are DiFlowDubber's Setting 2.0 (non-ground-truth reference) values; the review pairs them with Setting 1.0 values (9.65 / 11.72; 16.79 / 18.53). Use Setting 2.0: Chem 11.12 vs 12.81, GRID 16.21 vs 19.75. Also state the confound this exposes: the baselines were scored with a non-GT reference. If VSpeechLM used the target recording as its reference (unknown, §3.2), the comparison favours VSpeechLM. This is the strongest confound for the central claim, and the review raises it only as an open question.
2. **M12 verdict "standard" does not hold.** DiFlowDubber Table 1/2 show LSE-C/LSE-D for six prior dubbing systems (V2C-Net '22, HPMDubbing '23, StyleDubber '24, Speaker2Dubber '24, ProDubber '25, EmoDubber '25), four of them VSpeechLM's own baselines. The reason given, "only two of the six are prior", comes from a population that omits them. Revisit the verdict (likely `behind`, per SKILL.md rules) or justify it against these works.
3. **The M06/M12 population leaves out the V2C dubbing literature.** The usual-approach counts (diffusion 5, flow 4, mel 4, codec LM 2) contradict the target's own §2.1 ("primarily based on FastSpeech2 … or flow-matching"). Restate the usual approach as FastSpeech2-style duration/mel and flow-matching decoders with lip-derived duration, or explain why the dubbing line is outside the population. Keep the "upper bound, related-work mentions included" caveat in the body.
4. **Codec-LM absence claim.** "2 mention a codec-token language model, this paper and FunCineForge" misses VoiceCraft-Dub (arXiv:2504.02386, 2025, prior; locator unverified). Name it as the deciding prior for the codec-LM half of "both halves are standard"; it is stronger evidence than DubWise.
5. **Human study "no tie rates" is wrong.** §4.3 and Fig. 3 report win-tie-loss ratios. Keep "no blinding or uncertainty" and add the sample size (50 clips, 10 raters).
6. **Credit the authors on GRID ASR.** Footnote 2 already attributes the 22.5% GT WER to ASR errors. Say "as the authors note", or drop the point.
7. **DubWise location.** Change "(§2.1)" to "(§1)". Note that the authors describe DubWise as global-duration control only.
8. **SOTA line should also name ProDubber.** ProDubber (CVPR 2025, prior or near-concurrent) has Chem WER 9.45 in DiFlowDubber's Setting 1.0, below DiFlowDubber's 9.65, but weak LSE. VSpeechLM does not compare against ProDubber or Speaker2Dubber. That missing-baseline point belongs in "Where the claims outrun the evidence".
9. **EmoDubber has no reference entry.** It is the main comparator throughout; add it, along with the venue discrepancy (VSpeechLM Table 1: "CVPR2024"; DiFlowDubber: CVPR'25).
10. **"Absolute values use different ASR systems"**: unsupported for the copied rows (see claim 7). Soften it or source it.
11. Minor additions: the train-on-G / infer-on-P_exp mismatch (§3.5.3) belongs in the argmax-error discussion; Table 4 Spk Sim scale inconsistency; the GRID clip total exceeding the dataset size.

## Fairness and chronology

DiFlowDubber (arXiv 2603, about 4 months after the target) is correctly labelled [concurrent] and used only as the state of the art, not as missed prior work. LipAdapter and Watch Your Speech are correctly labelled [later]. The "weaker than every other text-and-video study" sentence in the Verdict leans partly on concurrent and later work. Once the prior dubbing systems in fix 2 are counted, it can rest on prior work alone.

## Scores

- Procedure: 6/10. Numbers and quotes are mostly accurate and the arithmetic checks out. But the comparator population leaves out the paper's own baseline line, and the DiFlowDubber table was read without matching the setting.
- Final text: 5/10. The central WER comparison is paired across settings, the M12 verdict does not follow once the prior LSE reporters are counted, and one factual error (tie rates) and one uncredited author caveat remain.

Strengths (brief): the MCD-DTW-SL recomputation, the UTMOS inconsistency, the GRID split arithmetic and the decoder-pretraining dependence are correct and well located.
