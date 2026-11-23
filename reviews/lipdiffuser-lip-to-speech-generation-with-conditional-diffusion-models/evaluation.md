# Independent evaluation: LipDiffuser (arXiv:2505.11391)

Date: 2026-11-23. Fallback evaluator (claim table only). Input was the compact review with its claim table. No source was reopened. Items that rely on outside knowledge and could not be located are marked "unverified".

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | LipDiffuser changes the decoder (per-frame MP-FiLM diffusion) and the training targets (audio-only pretraining, enhanced LRS3) | CT 1; Sec. 3.3, 4.1 quotes | correct | Both quotes support it. |
| 2 | Table 1 is the only quantitative table and isolates neither change | CT 2, 11 | insufficient evidence | This is an absence claim. The quote given (t55) is about pretraining being "required". No quote or list of the Sec. 4-5 experiments shows that no other table or ablation exists. |
| 3 | Kefalas et al. [2] ablated audio-only decoder pretraining with mixed effect; not cited by the target | CT 2, 3, 14 | correct (direction); insufficient quote (conditions) | The rows show 25.75 to 18.57 and 2.66 to 3.58 (3.66 with fine-tuning). The quote does not show the column header (WER), the seen/unseen split, or that "+ basic fine-tuning" means initialization from the pretrained decoder. The check of the target's reference list ([1]-[41]) is stated. |
| 4 | Quality lead over the recordings: DNSMOS 3.64 vs 3.56 for the clean reference, after training on enhanced targets | CT 4; Table 1 | correct for DNSMOS; incomplete | The numbers match by column position. In the same rows, NISQA is 4.57 for LipDiffuser against 4.65 for Clean, so the target is below the reference there. The DNSMOS gap (0.08) is inside one SD (±0.30 / ±0.36). The review applies that yardstick to WER but not here. |
| 5 | SpkSim 0.63 vs 0.37 for IL2S (SSL); enrollment from the clean reference | CT 5, 19; Table 1 caption | correct | The caption quote supports it. The question to the authors about same-utterance enrollment is in place. |
| 6 | V2SFlow [3]: audio-derived embedding raises SECS (0.851 vs 0.664) at unchanged WER (28.5) | CT 5, 18; V2SFlow Table I | correct | The [concurrent] label fits: the arXiv version is from Nov 2024 and the target from May 2025, about 5.5 months apart. It is used as evidence, not as a missed citation. |
| 7 | WER 0.38 vs 0.36 (LipVoicer, IL2S (SSL)), within one SD | CT 6; Table 1 | correct (numbers); wording | ±0.33-0.35 is a per-utterance SD over 1,321 files, not an uncertainty on the mean. The plain statement is that no interval or test is reported. The authors themselves call the WER "comparable" (Sec. 5, t17), so the review restates the authors' own result rather than finding something new. |
| 8 | No cross-dataset result; Sec. 5 reports only the in-domain test | CT 6, 22; Secs. 1, 5, 6 | insufficient evidence | The only quote for absence is "We begin with in-domain results...". "Begin" suggests that more results follow, and v3 may hold a cross-dataset table or figure. The quote does not establish absence. This claim appears in the Verdict and in "Where the claims outrun the evidence". |
| 9 | M06 usual approach: 165 studies, adversarial 54, diffusion 22, upsampling 15 (earliest 1999), FiLM 1 | CT 7, 25-29; Appendix | correct (ledger tally) | The counts are exact ledger tallies. "FiLM 1 (this paper)" names no deciding prior. The verdict is `standard`, so the review makes no novelty claim. Speaker-conditioned V2S systems that use FiLM/AdaIN-style modulation are unverified. |
| 10 | DiffV2S conditions its denoiser on concatenated visual features and a speaker embedding | CT 8; DiffV2S Sec. 3.2.1 | correct | The quote matches. |
| 11 | M06 state of the art: Faces-to-Voices, 30.45% LRS3 WER, 10 steps, video speaker embedding, Whisper Medium | CT 9; F2V Table 2, Sec. 4.4 | correct (number); inconsistent choice | The review's own M12 line gives V2SFlow at 28.5% LRS3 WER, which is lower. The review does not explain why the 30.45% system is the state of the art (different ASR or different table). Later candidates, e.g. DiVISe (2025), are unverified. |
| 12 | 0.02 worse than LipVoicer, about 6% relative (inference) | CT 10 | correct | 0.02 / 0.36 = 5.6%. |
| 13 | 32 sampling steps, QuartzNet, 1,321 LRS3-CHiME3 files | CT 10 | correct | The steps and file count are quoted. The QuartzNet quote is not shown (insufficient quote, minor). |
| 14 | M02 usual approach: 9 audio-only pretraining, 6 enhanced audio, upper bounds | CT 12, 30-34 | correct (ledger tally) | — |
| 15 | 960 h enhanced LibriSpeech pretraining; LRS3 audio enhanced | CT 13 | correct | — |
| 16 | Pretraining called "required" with no number without it, and no raw-vs-enhanced comparison | CT 15 | correct | The quote matches. The absence part rests on the same unquoted single-table check as #2. |
| 17 | M12 usual approach counts (83, 38, 23, 22, 21, 40) | CT 16, 35-38 | correct (ledger tally) | — |
| 18 | 15 listeners; means and SDs only | CT 17 | correct | — |
| 19 | SpkSim = cosine between enrollment and output embeddings; V+E vs V systems | CT 19 | correct | — |
| 20 | Lead over IL2S (SSL) of 0.26, about 70% relative (inference) | CT 20 | correct | 0.26 / 0.37 = 70.3%. |
| 21 | F2V attributes above-ground-truth predictor scores to noisy recordings; LipDiffuser targets are denoised | CT 21 | correct | — |
| 22 | "Highest speech quality" compares enhanced-target training with baselines trained on LRS3 | CT 23 | correct | This is the main confound and the review handles it. |
| 23 | Listening test gives no sample count, interval or test | CT 24 | insufficient evidence | The quotes describe the test but do not show what the Fig. 1 caption contains. The absence has to be checked against the figure. |
| 24 | References: authors, venues, ids | Reference list | mostly correct; unverified | [2] may have a later journal version (IEEE/ACM TASLP, 2024), unverified. The F2V page range 15874-15884 is unverified. |
| 25 | Chronology and fairness | Whole text | correct | No later work is treated as prior work. The [concurrent] labels on [3] and [5] fit. Kefalas (2023) is legitimately prior. |

## Central claim and confound

The strongest confounds are training on enhanced targets (for the quality metrics) and an enrollment drawn from the clean reference (for SpkSim). The review names and handles both. Two positions go beyond the quoted evidence: "no cross-dataset result" (#8) and "Table 1 is the only table" (#2). No slot verdict is `ahead`, so the verdict rules for `ahead` do not apply.

## Required fixes (ordered by impact)

1. **Cross-dataset absence (Verdict; "Where the claims outrun the evidence").** The quote "We begin with in-domain results" implies that more results follow. Check all of Sec. 5 and every figure in v3. Then either quote the passage that shows no cross-dataset result exists, or remove the claim.
2. **Quality-lead sentence (Verdict).** Limit it to DNSMOS. Add that NISQA is below the clean reference (4.57 vs 4.65, Table 1). Also say that the 0.08 DNSMOS gap is within one SD, the same yardstick the review uses for WER.
3. **M06 state of the art.** Reconcile Faces-to-Voices (30.45% WER) with V2SFlow (28.5% LRS3 WER, cited under M12). Either state the ASR and evaluation differences that keep the two apart, or choose consistently.
4. **Kefalas numbers (M02 state of the art, claim table 2/14).** Add the column header (WER), the row and condition labels (Table V seen GRID speakers; Table VII unseen), and confirm that "+ basic fine-tuning" means initialization from the audio-pretrained decoder.
5. **WER comparison wording (Verdict).** Replace "within one standard deviation" with "no interval or test is reported (per-utterance SDs ±0.33-0.35)". Note that the authors themselves call the WER comparable (Sec. 5), so the review should not present this as its own finding.
6. **Single-table and no-ablation claims (Verdict, M06, M02).** Support them with the relevant evidence: a statement that Table 1 is the only table, with the list of Sec. 4-5 experiments. Do not cite the pretraining quote (t55) for this.
7. **Listening-test absence (claim table 24).** Quote or describe the Fig. 1 caption or axis to show that no sample count, interval or test is given.

## Scores

- Procedure: 7/10
- Final text: 7/10
