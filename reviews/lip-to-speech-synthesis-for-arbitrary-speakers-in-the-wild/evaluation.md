# Evaluation: Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild

Date: 2026-11-20. Fallback evaluator (claim table only): the claim table, Verdict and component sections were checked against the quotes and locations given. No sources were reopened. Points from background knowledge are marked as inference.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper changes M02 (frozen ASR-encoder target), M06 (VAE latent + critic), M08 (reference-audio embedding) | Row 1; Sec. 3.2.2, 3.2.4 | correct | The quotes support a frozen 1024-d encoder and a 256-d speaker embedding from a random 1 s segment. |
| 2 | "15-sample listener test" (Verdict; M12 table row) | Row 2 | insufficient evidence | The only quote is "20 participants". Nothing in the claim table supports 15 samples. |
| 3 | LRS2 PESQ/STOI below the seq2seq baseline | Row 3; Table 3 | correct | 0.60/0.34 vs 0.97/0.43. The GAN-based baseline (0.80/0.40, row 18) is also above the target. |
| 4 | "the gain is distribution match, not content" | Table 3 rows | position stronger than evidence | Sync also improves (LSE-C 2.507 vs 1.991; LSE-D 8.155 vs 8.532). PESQ/STOI are signal-match metrics, not content metrics, so "not content" is not shown. Content is unmeasured. |
| 5 | Later study rates intelligibility 1.07 of 5 [3] | Row 4; [3] Table 2 | insufficient evidence (condition) | The quoted row has no column header. The Verdict leaves out the condition: 10 long sentences of 10 s or more (row 23), a harder test than the target's own. |
| 6 | SED uses embeddings of the kind the voice loss optimizes | Row 18; Sec. 3.2.7 | insufficient evidence | The quote shows that the identity network penalizes the output. No quote shows that SED is computed with that network. |
| 7 | Test-time voice reference unspecified | Rows 1, 16 | insufficient evidence | The quote covers training-time extraction only. The absence at test time needs a locator or an "(unstated)" note. |
| 8 | "First to handle ambiguity explicitly" omits Yadav et al. [4] | Rows 5, 14 | correct (as far as checkable) | Yadav et al., ICASSP 2021 (VAE, shared author Namboodiri), is real and predates the target by more than a year, so the omission is fair to raise. |
| 9 | "KL-matches lips to a frozen ASR encoder's embeddings (Sec. 3.2.3)" | Row 7 | insufficient evidence | The quotes cover the frozen encoder and R = 10 segments. They contain nothing on a KL objective. |
| 10 | Speech units 72.5% to 50.7% WER on LRS3 [5] | Row 8; [5] Table 3 | insufficient evidence (dataset) | The numbers match. The quote does not name LRS3. |
| 11 | V2SFlow 28.5% WER, real speech 2.5% [6] | Row 8; [6] Table I | correct | |
| 12 | Without the content encoder: FDSD 1.273 to 2.856, intelligibility 3.22 to 2.51 | Row 9; Tables 3-4 | correct numbers, wording issue | The ablation is labelled "w/o Content Encoder". "Scratch-trained speech encoder" is not in the quote. |
| 13 | M06 counts (54 / 22 / 19 of 165) | Row 33 | correct, incomplete | The Appendix ranks speech-unit conditioning (44) second. The section leaves it out. |
| 14 | Faces-to-Voices 30.45% LRS3 WER [8] | Row 11; [8] Table 2 | insufficient evidence (dataset) | The quoted row holds two blocks (30.45 and 39.37). The dataset of each is not shown. |
| 15 | PESQ/STOI 38% and 21% below baseline | Row 12 | correct | (0.97-0.60)/0.97 = 38.1%; (0.43-0.34)/0.43 = 20.9%. "L1" baseline is not in the quote. |
| 16 | Lip-to-text+TTS FDSD 0.984, LSE-D 19.012 | Row 13 | correct numbers, wrong inference | A lip-reader-plus-TTS system probably gets the words more right but loses sync. Its low FDSD shows that FDSD ignores sync. It does not show that FDSD ignores words. |
| 17 | M08: "48 name a speaker label, 23 reference audio" | Rows 15, 38; component table | wrong | The Appendix says 48 is "speaker label or reference-audio embedding" combined, and the component table says "Label or audio (48)". The section text contradicts both. |
| 18 | DiffV2S voice-match MOS 3.91 [9] | Row 17 | insufficient evidence | The quoted row has three MOS values and no headers, and the dataset (LRS3) is not quoted. |
| 19 | LRS2 SED 5.95 vs 6.13-6.47 | Row 18 | correct | |
| 20 | Rated voice match 2.69 | Row 19 | correct (column inferred) | |
| 21 | GRID WERs 26.6% [7], 14.08% [2], 51.6% speaker-independent [10] | Row 21 | correct numbers | The "seen speakers" condition for 26.6% is not in the quote. |
| 22 | Successor rated 3.49 [3] | Row 23 | insufficient evidence | Only the VAE-GAN row (1.07) is quoted. 3.49 and "LRS3" have no quote. |
| 23 | p ≈ 0.035, unspecified t-test | Row 23 | correct | |
| 24 | "Substantial improvement" (Abstract) | Row 24 | wrong quotation | The abstract quote reads "outperform all baselines by a large margin". The review's quoted phrase is not in the source quote. |
| 25 | No seeds/variances/test counts; t-test across 4 criteria and 7 systems | Row 25 | insufficient evidence | No quote supports absence or "7 systems". The quotes given are unrelated sentences. |
| 26 | Non-frontal FDSD 3.473 vs 1.351, 2.6x | Row 26 | correct | 3.473/1.351 = 2.57. |

**Internal consistency.** The state-of-the-art figures disagree across sections. The component table gives M02 as 50.7% [5] although the M02 text cites V2SFlow at 28.5% [6]. M06 gives Faces-to-Voices (2025) 30.45% as the state of the art, while M02 and M12 cite V2SFlow (2024) at a lower 28.5%. If the ASR model or test set differs, the text has to say so. Otherwise the best figure must be used consistently.

**Central claim and confound.** The strongest confound is that the 1.07 intelligibility rating [3] comes from a different and harder protocol (≥10 s LRS3 sentences, a different listener pool). The Verdict reports it without that condition, so it reads as a direct contradiction of the target's 3.22. The review does handle the PESQ/STOI one-to-many objection (the "outrun" section).

**Fairness.** All works after the target ([3], [5], [6], [8], [9]) are labelled [later] and used only as state of the art, never as missed citations. Yadav et al. [4] is prior (2021) and fairly raised.

**State of the art (inference, medium confidence).** LipVoicer (Yemini et al., ICLR 2024, arXiv:2306.03258) guides a diffusion lip-to-speech model with a lip-reader's text and reports LRS3 WER in the low 20s, which may be below V2SFlow's 28.5% under its own ASR. This should be checked and either cited or distinguished by evaluation condition.

**Verdicts.** M12 `behind` rests on a missing metric. The authors' own lineage [2] reported WER on GRID, so the rule "behind the best comparable work" is defensible. The verdict text should state that this is a protocol gap, not a measured deficit.

## Required fixes (ordered by impact)

1. M08: "48 name a speaker label" contradicts the Appendix and the table ("speaker label or reference-audio embedding, 48"). Correct the breakdown.
2. Verdict and M12 table: "15-sample listener test" has no supporting quote. Add the locator and quote for the sample count, or remove it.
3. Verdict: state the condition behind 1.07 of 5 [3] (10 long sentences ≥10 s, a different listener test). Add the quote and column header for 1.07 and for the successor's 3.49.
4. Reconcile the state-of-the-art figures across M02, M06, M12 and the component table (50.7% vs 28.5% vs 30.45%). Name the dataset and ASR for [8] 30.45% and [5] 50.7%.
5. M06: replace "FDSD rewards plausible speech, not the words". The lip-to-text+TTS row shows that FDSD ignores sync (LSE-D 19.012), not that it ignores words.
6. Verdict: "the gain is distribution match, not content" goes beyond Table 3. Sync (LSE-C/LSE-D) also improves, and content is unmeasured rather than shown to be absent.
7. "Outrun" section: the quoted "Substantial improvement" does not match the abstract quote ("outperform all baselines by a large margin"). Quote the actual wording.
8. M02: "KL-matches" has no supporting quote. "Scratch-trained speech encoder" does not match the ablation label "w/o Content Encoder". Quote or reword both.
9. M08 and Verdict: add a quote showing that SED uses the same identity network as the voice loss, and a locator for the unspecified test-time reference.
10. M06: "L1 sequence-to-sequence baseline" has no quote for "L1". Add one or drop "L1".
11. "Outrun" section: "No seeds, variances or test counts" and "7 systems" need locators or explicit "(unstated)" notes.
12. References: DiffV2S [9] appeared at ICCV 2023 and V2SFlow [6] at ICASSP 2025 (inference, medium confidence). Update the venues from "arXiv preprint".
13. State of the art: check LipVoicer (ICLR 2024, text-guided diffusion, LRS3 WER) against the cited figures, and cite it or distinguish it by condition (inference).

## Scores

- Procedure: 7/10
- Final text: 6/10
