# Evaluator: a language model separate from the writer

Date: 2026-11-24. Mode: fallback evaluator (claim table and review positions in compact.md only; no sources opened). Outside knowledge is marked "unverified" where I cannot locate year, venue or value.

## Claim checks

| No | Claim (short) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target changes M06 twice; 35 of 50 name spectral parameters | Claim 1, Appendix | correct | Quote and tally carry it. |
| 2 | Front end standard: spatiotemporal convolution most frequent | Claim 4, Appendix (27 vs 24 of 148) | correct | Upper-bound pattern-match counts; "most frequent" holds by 3. |
| 3 | Formant target is "a real departure ... but it stays standard" | Verdict, M06 target section | insufficient evidence / wording | See finding 3: self-contradictory phrasing. |
| 4 | No ledger study first public before the target predicts formants | Appendix tally, claim 11 | wrong as written (internal) | The 6 formant hits are accounted for as 1+1+3 = 5; one hit is unexplained. See finding 1. |
| 5 | Earlier studies scored synthesized speech on held-out sentences [2][3][4] | Claims 3, 15, 19 | correct | Quotes for [2] and [3] carry it; [4] "ten sentences from the test set" carries it. |
| 6 | 5 or 17 stacked frames, feed-forward [5] | Claim 4 | correct | 8-8 context + centre = 17. |
| 7 | 1×3×3, 3×1×1, 3×3×3 branches + shuffle | Claim 5 | correct | |
| 8 | Tongue2Speech 15.93% WER, TaL1, single speaker [6] | Claims 6, 10, 16 | correct to the quote; SOTA status unverified | |
| 9 | (2+1)D CNN [7] is concurrent | Claim 7, ref 7 | correct | ICAISC Oct 2020, within 6 months of June 2020 arXiv. |
| 10 | Ablation drops 1.88/1.44/0.84 = 99.96 → 98.08/98.52/99.12 | Claim 8 | correct | Arithmetic checks. |
| 11 | Ablated MAE rises 117%, 210%, 67% | Claim 8 | insufficient quote | Only the full-model MAE .0052 is quoted; ablated MAE values (.0113, .0161, .0087 implied) are not in the claim table. Note R2 and MAE rank spatial vs temporal ablation in opposite order; worth stating. |
| 12 | 13-dim MGC-LSP+gain [3]; 24-order MGC-LSP+F0+energy [8] | Claim 9 | correct | |
| 13 | "the four priors read all predict spectral parameters [2], [4]" | Claim 11 | citation incomplete | Four priors are [2][3][4][8]; only two cited. [2] quote is an MCD value, which implies but does not state the target. |
| 14 | Every Table 1 baseline also predicts formants | Claim 12 | insufficient quote | Quote only names the Conv-BiLSTM baseline. |
| 15 | Motivation: poor vowel transitions of 24-order MGC-LSP | Claim 12 | insufficient quote | Quote says "poor performance of the synthesized version"; "vowel transitions" is not in it. |
| 16 | Two formants describe vowels, not consonants or voicing; corpus vowel-only | Claim 13 | insufficient quote | The quote ("segmented ... acoustic landmarks were prepared") does not show vowel-only data; the phonetic statement has no citation. |
| 17 | Hueber 150 test sentences, MCD, transcription [2] | Claim 15 | correct | |
| 18 | Csapó 23 listeners MUSHRA [3] | Claims 19-20 | correct | |
| 19 | Gosztolya 310/41/87 split, 14 listeners [4] | Claim 15 | insufficient quote | Neither number appears in any quoted passage. |
| 20 | 13,082 one-second clips, random 80/10/10 | Claim 18 | correct | |
| 21 | Conv-BiLSTM source predicted MGC-LSP (Sec. 2) | Claim 22 | insufficient / possible mismatch | The quote ("...toencoders, intended to predict 24 order MGC-LSP") describes the autoencoder work, not necessarily the Conv-BiLSTM source (target's ref [11]). |
| 22 | Conv-BiLSTM 90.01 joint R2 | Claim 22 | correct | |
| 23 | MAE values carry no unit | Claim 23 | insufficient quote | The normalization quote concerns pixel intensities, not formant targets. Position is reasonable; quote does not carry it. |
| 24 | M12 behind: at least four earlier studies held out sentences | Claims 3, 19 | correct on count; judgment partly | [2][3][4] plus p-csapo19-split ([8]); see finding 5 on confound. |
| 25 | Target bibliographic entry: arXiv preprint 2020 | Ref 1 | possibly incomplete (unverified) | I believe this paper appeared at MICCAI 2020 (LNCS); check for a published version. |

## Findings

1. **Formant tally does not add up (central to the novelty claim).** The Appendix and the M06 target section say there are 6 formant hits, then account for only 5 (target, one 2018 cortical encoding study, three later works). The sixth hit is unexplained, and it is exactly the one that could falsify "no ledger ultrasound-to-speech study first public before it predicts formants". Either identify the sixth (and whether it is prior and predicts formants) or correct the count.
2. **Absence claim names no deciding prior for formants and is not checked against early ultrasound synthesis work.** The deciding priors listed ([2][3][4][8]) all predict spectral parameters, which shows the usual target but not the absence of formant prediction. Candidates to rule out (unverified from my side): Denby and Stone, ICASSP 2004, "Speech synthesis from real time ultrasound images of the tongue"; Jaumard-Hakoun et al., Interspeech 2016, articulatory singing synthesis from tongue and lip imaging. State whether either predicts formants.
3. **Self-contradictory verdict wording.** "The formant target is a real departure ... but it stays standard" reads as two verdicts. Say plainly: departure from the usual target, verdict standard because no same-data comparison with a spectral target and no repetition (as the M06 section already says).
4. **Claim-table quotes too thin for several load-bearing statements.** Vowel-only corpus (finding basis for M06 and M04), "every Table 1 baseline predicts formants", "vowel transitions" motivation, Gosztolya 310/41/87 and 14 listeners, ablated MAE values, MAE unit. Each needs the actual passage; these are "insufficient quote", not proven wrong.
5. **Main confound for the M12 "behind" verdict is only partly handled.** The target's task is vowel formant tracking, not sentence synthesis; comparing it to sentence-level MUSHRA/MCD studies mixes task and evaluation. The review's strongest, well-supported point is the random clip-level split with possible window overlap (leakage), which is task-independent; the verdict should lean on that and on the absence of any held-out-session test, and acknowledge the task difference. "Best documented" chosen by listener count (23) is an odd criterion; say "most complete".
6. **Conv-BiLSTM origin may be misattributed.** The quote used to say the Conv-BiLSTM source predicted MGC-LSP refers to autoencoders. Confirm that the target's ref [11] (Conv-BiLSTM) itself predicted MGC-LSP, or reword.
7. **Ablation MAE vs R2 inconsistency not surfaced.** By R2 the spatial branch matters most (−1.88), by MAE the temporal branch (+210% vs +117%). This internal tension in the target's Table 2, together with no seeds, weakens the authors' ranking of components; worth one sentence.
8. **Incomplete citation of priors.** "the four priors read all predict spectral parameters [2], [4]" should cite [2], [3], [4], [8].
9. **Phonetic claim without support.** "Two formants describe vowels, not consonants or voicing" is reasonable domain knowledge but is presented as fact without a citation; soften to F1/F2 characterize vowel quality and do not encode voicing or most consonant cues, or cite.
10. **Bibliographic: likely published version of the target.** I recall a MICCAI 2020 version (Saha, Liu, Gick, Fels; LNCS). Unverified; if confirmed, cite the published version alongside arXiv.
11. **State of the art lines (unverified).** Tongue2Speech (Interspeech 2026, 15.93% WER, TaL1) is quoted correctly; I cannot confirm it is the best. Using a whole-system ASR WER as the M06 front-end state of the art does not isolate the front end; note that limitation or pick a front-end ablation. Other TaL-based ultrasound-to-speech systems (e.g. pseudo-target / domain-adversarial work around 2023) could be checked as alternatives, unverified.
12. **Usual-approach counts mix eras.** The 148-study front-end tally includes later work; in mid-2020 the dominant ultrasound-to-speech design was a feed-forward or 2D CNN on stacked frames ([5] shows this). The review mentions [5], which partly handles it; one clause stating the 2020 baseline would avoid implying 3D convolution was already the norm.
13. **Fairness: OK.** [7] correctly labelled concurrent and [6] later; neither is treated as missed prior work. The "first time" critique correctly separates the ledger-supported novelty from the unsupported "successful".

## Required fixes, ordered by impact

1. Resolve the sixth formant hit (finding 1) and name or rule out early formant-predicting priors (finding 2).
2. Replace thin quotes with passages that carry the claims (finding 4), especially vowel-only data and the Conv-BiLSTM target (finding 6).
3. Rewrite the M06 formant verdict sentence without contradiction (finding 3).
4. Reframe the M12 verdict around leakage/split and acknowledge the task difference (finding 5).
5. Add [3], [8] to the "four priors" citation (finding 8); soften or cite the phonetic statement (finding 9).
6. Optional: MAE/R2 ranking note (finding 7), published version of target (finding 10), era note (finding 12).

## Scores

- Procedure: 7/10 (claim table broad and mostly traceable; several quotes do not carry their claims; tally arithmetic slip).
- Final text: 7/10 (clear positions, correct numbers where checkable; one novelty claim rests on an incomplete tally).
