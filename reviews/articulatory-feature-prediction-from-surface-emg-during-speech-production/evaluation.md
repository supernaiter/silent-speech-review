# Evaluation: Articulatory Feature Prediction from Surface EMG during Speech Production

Date: 2026-11-21. Mode: fallback evaluator (claim table only). Input was the compact review and its claim table. No source was reopened, so each verdict below is judged against the quoted passage and its location. Bibliographic details and later work were not checked on the web.

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper changes the intermediate target (M06) and proposes an electrode subset (M05) | Row 1, t1/t3 | correct | Both quotes support it. |
| 2 | WER 15.5% vs 12.6%, PER 36.0 vs 33.9 (Table 2) | Rows 2, 21, t27–t31 | correct | Matches the table rows. |
| 3 | SBS 84.4 vs 77.9 comes with a different synthesizer | Row 3, t72; row 21, t57 | insufficient evidence | t72 is about the Whisper ASR scorer and t57 about the single speaker. No quote shows HiFi-GAN for the baseline or the articulatory synthesizer with an external speaker embedding for the proposed route. The central confound depends on this. |
| 4 | "approximately 0.9" correlations are against audio-inverted features | Row 4, t17, t8, t56 | partly wrong | The inversion source is supported (t8, t56). The quoted wording is not the source's: t17 says "an average correlation of 0.9 for EMA and loudness". The 0.9 also covers EMA and loudness only. The third correlation column in Table 3 (0.538, 0.576), probably pitch, is far lower, and "correlations of about 0.9" hides that. |
| 5 | Subset never compared with equal-size alternatives; ranked 5th of 70 [2] | Rows 5, 15, c13, c14, t63 | insufficient evidence | The target selects electrodes 2, 3, 4, 6 (t63, t40). [2] ranks a subset "(1, 2, 3, 5)" from its ref. [12]. This could be zero-based indexing of the same subset, but the review never states the mapping or that [12] is the target. |
| 6 | Best four-channel subset reached 47.2% WER in [2] | Row 15, c14 | insufficient evidence | c14 is one row (1356 → 47.2) and does not show that this row is the minimum. The very different scale (47.2 against the target's 22.9 at four channels) needs the protocol difference stated. |
| 7 | 12-dimensional pseudo-EMA, pitch, loudness | Row 7, t7, t9 | correct | |
| 8 | GETS reaches 11.89% WER on silent EMG, same corpus [4] | Row 8, c10 | partly supported | The number and the silent condition are in the quote. "Same corpus" is not. |
| 9 | Best vocalized result at submission was Gaddy et al. 12.6% | Row 9, t28 | insufficient evidence | The quote only shows the baseline in the target's own Table 2, re-scored there. Calling it "the best vocalized result at submission" is a claim about the literature with no source. |
| 10 | 2.9 points, 23% relative | Row 9 | correct | 15.5 − 12.6 = 2.9; 2.9 / 12.6 = 23.0%. |
| 11 | Anumanchipalli et al.: articulatory intermediate beats direct decoder by 0.54 dB MCD [5] | Row 10, c6–c8 | correct | Kinematics inferred from audio (c7), matching the review's wording. |
| 12 | 4 confirmed articulatory-intermediate studies, none earlier on surface EMG; priority holds for EMG only | Row 11, t2, ledger | correct but misframed | The ledger count is outside this check. The authors' t2 claim is already limited to surface EMG, so "holds for EMG only" restates the authors' scope rather than narrowing it. The evaluator knows of no earlier surface-EMG work with an articulatory-feature intermediate. |
| 13 | Wu et al. [concurrent]: audio-estimated EMA on same corpus as a pre-training modality, speech units as intermediate [6] | Row 12, c1, c2 | partly supported | c2 supports audio-estimated EMA (13-dim) on the dataset. "Pre-training modality" and "speech units as the intermediate" have no quote. The [concurrent] label is right: Dec 2024 is within 6 months of the target. |
| 14 | Zhu et al.: sequential forward selection over 120 electrodes [7] | Row 13, c12 | insufficient evidence | c12 gives 10 optimal vs 40 non-optimized electrodes. It does not mention SFS or 120 electrodes. |
| 15 | Sridhar et al.: 5 of 11 sensors by MI, 80.6% vs 79.6% [8] | Row 14, c11 | correct | |
| 16 | Four electrodes raise WER 15.5 → 22.9; two electrodes 46.9 (Table 3) | Row 16, t40, t52 | correct | |
| 17 | 7.4 points, 48% relative, for halving | Row 17 | correct | 7.4 / 15.5 = 47.7%. The array goes from 8 to 4 electrodes. |
| 18 | Authors call the choice an informed alternative to random search (Sec. 4.4) | Row 18, t54 | correct | |
| 19 | Selecting partition unstated | Rows 18, 27, t63 | insufficient evidence | This is an absence claim. The review does not name the sections it searched. |
| 20 | Lips over tongue describes the pseudo-labels | Row 20, t20 | correct | The inference follows from claim 4. |
| 21 | "Comparable intelligibility" is the authors' claim | Row 21 | insufficient evidence | No quote shows the authors using this wording, so the heading rebuts a claim the table never shows the authors made. |
| 22 | Vocalized only, one speaker; Gaddy and Klein report 42.2% WER on silent [3] | Row 22, t4, t12, c5 | correct | c5 "This work 42.2" matches the silent result of [3]. |
| 23 | 95% intervals have no stated construction; no seeds or reruns | Row 23, t61, t59 | insufficient evidence | t61 states that the intervals are 95% CIs. The absence of a construction method and of reruns is plausible, but the review does not say which sections were checked. |
| 24 | Slot verdicts (all standard / not applicable / not reported) | Component table | correct | No `ahead` verdict, so the `ahead` rules do not apply. |
| 25 | Chronology: [2] and [4] marked [later], used as state of the art, not as prior work | References, rows 5, 8, 15 | correct | The review does not fault the authors for missing them. |

**Central confound.** The review names the synthesizer difference as the main confound, and that is the right one. Its evidence for the difference is missing from the claim table (claim 3). A second confound is only partly handled. The M06 state of the art (11.89%, silent) is set next to a vocalized result, and the review says "silent" without saying that the task differs. The vocalized baseline is the target's own re-scored run, not a literature figure (claim 9).

## Required fixes (by impact)

1. Add a claim-table quote with its location (for example Sec. 4.3 or 4.5) showing that the baseline uses HiFi-GAN and the proposed route uses the articulatory synthesizer with an external speaker embedding. The Verdict's central position rests on it.
2. M05: state that the subset (1, 2, 3, 5) in [2] is the target's 2, 3, 4, 6 under zero-based indexing, quoting [2], and confirm that [2]'s ref. [12] is the target. Support "best reached 47.2%" with a quote that shows it is the minimum. In the component table, give the best subset's value as the state of the art instead of the target's rank, and state the protocol difference from the target's 22.9%.
3. Remove the quotation marks around "approximately 0.9" or use the source wording ("average correlation of 0.9"). Say that it covers EMA and loudness only, and that the third correlation in Table 3 is about 0.54.
4. Replace "At submission, the best vocalized result was Gaddy et al. at 12.6%" with "the paper's re-scored Gaddy et al. baseline", or cite a literature source. In the M06 state-of-the-art line, say that 11.89% is silent EMG and not comparable with the vocalized 12.6/15.5. Add a quote from [4] for "same corpus".
5. Wu et al. [6]: add quotes for "pre-training modality" and "speech units as the intermediate", or remove both phrases.
6. Zhu et al. [7]: add a quote for sequential forward selection and 120 electrodes, or describe the study by what c12 supports.
7. "Comparable intelligibility": quote the authors' sentence that makes this claim, with its location, or reword the heading.
8. Reword "the authors' priority claim holds for EMG only". The authors already limit their claim to surface EMG (t2), so the review should confirm the claim rather than present it as a narrowing.
9. For the absence claims (selecting partition unstated, CI construction unstated, no reruns), name the sections checked (Sec. 3.1–3.2, 4.1–4.4, table captions).

## Scores

- Procedure: 7/10. Every number is tied to a location, the arithmetic is right and the chronology labels are right. Several comparator details and the central confound lack a supporting quote.
- Final text: 7/10. The position is clear and fair to the authors. Some sentences go beyond their quotes (fixes 1–4).
