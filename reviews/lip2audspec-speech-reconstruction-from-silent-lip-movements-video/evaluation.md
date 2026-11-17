# Evaluation: Lip2AudSpec review

Date: 2026-11-17. Independent evaluator, single pass, no tools beyond the review and its claim table (the claim table was filled by the writer, not by a separate checker; its quotes were taken as given but not as proof of what they are attached to). Sources were not re-opened; statements about outside work are from the evaluator's own knowledge and are marked with a confidence level.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | 32-unit noisy bottleneck target; 8 kHz, 128-bin auditory spectrogram with toolbox inversion | Claim rows 1, 13 | correct | Quotes support size 32, 8 kHz, 128 bins, toolbox parameters. |
| 2 | "four of the five bottleneck settings tried lose to direct spectrogram regression" | Rows 8-9 (Tables 7-8) | insufficient evidence | Quotes give bare number rows with no column headers. 1.19, 1.26, 1.09, 1.29 are all below 1.69, but nothing shows which column is the "best direct-spectrogram run" or that 1.29 in Table 8 is a bottleneck setting (1.29 also appears in Table 7). |
| 3 | PESQ 1.76 vs 1.69, Corr2D 0.89 both, 4% gain | Row 8 | correct arithmetic, labels unverified | 1.76/1.69 = +4.1%. Same column-label problem as #2. |
| 4 | No noise: PESQ 1.09, Corr2D 0.46; 16/64 units: 1.19, 1.26 | Row 9 | correct numbers, labels unverified | Numbers are in the quoted row. |
| 5 | S29 chosen for wide frequency range; 32 "found to be most optimal" | Rows 1, 7 | correct | "Tuned on the evaluated speaker" is a fair inference. |
| 6 | Gender 85.1 vs 43.2; naturalness 1.63 vs 1.35 | Row 16 | correct | Averages are in the quoted rows. |
| 7 | Female-speaker baseline gender 21% and 17% "below guessing", "points to a faulty baseline excitation" | Rows 16, 18 | wrong (judgment) | The third choice was "hard to say". Low "correct" rates can come from listeners choosing "hard to say" on poor audio, which is not a wrong guess. Below-chance inference and the causal reading go beyond the evidence. |
| 8 | Word accuracy 55.8 vs 50.9, +9.6% relative, "significantly better" with no test | Row 20 | partly wrong | Arithmetic correct (55.8/50.9 = 1.096). But the quoted "significantly better" refers to "three out of four speakers", not to the average the sentence pairs it with. |
| 9 | S4: accuracy 57.7 vs 54.9; PESQ 1.79 vs 1.61; letters 6.0% vs 9.1%, chance 4.0% | Row 21 | insufficient evidence / likely misplaced | 57.7/54.9 and 1.79 are quoted; 1.61 and 6.0% are not. Table 6 columns (25%, 4%, 10% chance) look like word categories, not speakers, so "On S4 ... letters" likely attaches an all-speaker category result to S4. |
| 10 | Closed set: vocabulary, unlimited replay, 19% chance | Row 22 | correct | |
| 11 | STMI average 0.80 vs per-speaker mean 0.83 | Row 23 | correct | (0.82+0.84+0.84+0.82)/4 = 0.83. Good catch. |
| 12 | Split given as 10/10 (Sec. 4.2) and 90/5/5 (Sec. 4.3.2) | Rows 24, 14 | wrong / unsupported | Row 24 quotes the 10/10 sentence twice and a 150-epoch sentence; no target quote gives 90/5/5. The only 90/5/5 quote in the table (row 14) is from [2] Sec. 3.1. The claimed internal inconsistency appears to borrow [2]'s split. |
| 13 | Released script writes test-set predictions every epoch | Row 24 (code lines) | insufficient evidence | No quote; and the sentence never says what follows from it (test-set model selection?). |
| 14 | Lip2AudSpec re-trained by [2]: STOI 0.446, WER 32.5%, PESQ 1.82 vs 1.71 | Rows 14, 19 | correct | Consistent column reading across the three rows. |
| 15 | Unseen speakers: "no intelligible speech" [2] | Rows 2, 25 | insufficient evidence | Quote "training the Lip2AudSpec model on the same data did not produce intelligible results" does not itself say "unseen speakers"; the context sentence is missing. Plausibly correct (evaluator recalls a speaker-independent section in [2]). |
| 16 | 4.07% WER and STOI 0.731 as "2023 leaders" / "a 2023 table" [3] | Rows 6, 14 | wrong (attribution and date) | 4.07 is the row "End-to-end WGAN (2022)" and 0.731 is the row "Lip2Wav", a 2020 system. These are two different systems, neither from 2023, quoted from [3]'s comparison table. [3]'s own system's row is not quoted. |
| 17 | 87% lower WER, 64% higher STOI | Row 15 | correct arithmetic | 87.5% and 63.9%. Mixes two different systems (see #16). |
| 18 | WER scorers have 4% and 0.1% WER on real audio | Row 15 | correct, handled in M06 | Not carried into the Verdict (see fixes). |
| 19 | 2023 leaders "regress spectrograms or waveforms directly" | Row 6 | questionable | [3]'s contribution is large-scale audio-only pre-training of the decoder side, which is close to the latent-target idea the review calls dead in video. |
| 20 | "The latent idea survives outside video as a deep-feature loss, 18.091% Whisper WER" [5] | Row 5 | wrong (state of the art) / insufficient (number) | Speech-latent targets thrive inside video-to-speech: discrete self-supervised speech units as targets, e.g. ReVISE (Hsu et al., CVPR 2023) and Choi et al., "Intelligible Lip-to-Speech Synthesis with Speech Units" (Interspeech 2023) (high confidence these exist; metrics not checked here). A deep-feature loss is a perceptual loss, not a latent target. The quoted row has 18.342 and 18.091 with no header showing which is Whisper WER. |
| 21 | Before 2018 lip-to-speech was parametric | Row 12 | overstated | Ephrat, Halperin & Peleg, "Improved Speech Reconstruction from Silent Video" (ICCV Workshops 2017; arXiv Aug 2017) predicted spectrogram features rather than LSP/LPC (medium confidence on its exact output and inversion). It is within 6 months of the target, so it is not a missed citation, but it contradicts the general sentence. |
| 22 | "the inversion gives smooth audio, not intelligible audio" | M06 | wrong (judgment, internal contradiction) | The review states that no experiment isolates the representation, then credits [2]'s PESQ/STOI pattern to the inversion. PESQ is also not a "smoothness" measure. |
| 23 | Ledger counts (40, 10/4/3; 165, 49/41/16/3) | Appendix rows | not checked | Outside scope per brief. |
| 24 | Chronology tags [2], [3], [5] later; [4], [6] prior | References | correct | No later work treated as prior work. |
| 25 | Bibliography of [3] | References | likely outdated | Evaluator recalls the paper appeared in IEEE/ACM TASLP (2024); low-medium confidence. |

Central confound: the bottleneck result is one speaker, one run, with the bottleneck size selected on that speaker; the representation result is against a re-implemented baseline. Both are handled well. The cross-paper WER comparison uses different ASR scorers; handled in M06 but not in the Verdict.

Verdicts: all slots `standard`, `not applicable` or `not reported`; no `ahead` verdict to check against the rules.

## Required fixes (ordered by impact)

1. **Sentence:** "The split is given as 10/10 samples (Sec. 4.2) and as 90/5/5 (Sec. 4.3.2); the released training script writes test-set predictions after every epoch."
   **Wrong:** No quote from the target gives a 90/5/5 split; the only 90/5/5 quote in the claim table is from [2] Sec. 3.1. The internal inconsistency looks borrowed from the later paper. The code half states a fact but no consequence.
   **Fix:** Quote the target's Sec. 4.3.2 wording for 90/5/5, or delete the inconsistency. If kept, state what the code does (e.g. "test-set predictions are written after every epoch, so the reported epoch may have been picked on test data") with the file and line numbers, or drop it. Remove the dependent question in "Questions for the authors" if the inconsistency goes.

2. **Sentence:** "The latent idea survives outside video as a deep-feature loss, at 18.091% Whisper WER for articulatory-to-speech in 2024 [5] [later]. The 2023 leaders on the same four GRID speakers regress spectrograms or waveforms directly and reach 4.07% ASR WER [3] [later]."
   **Wrong:** Speech-latent targets are current practice inside video-to-speech: self-supervised speech units as targets (ReVISE, Hsu et al., CVPR 2023; Choi et al., Interspeech 2023). [3] itself is built on audio-only pre-training of the decoder side, so "regress directly" misdescribes it. A deep-feature loss is not a latent target. The quoted row for [5] has two numbers (18.342, 18.091) with no header.
   **Fix:** Name speech-unit targets in video-to-speech as the state of the art for M02, with year, metric and value from their papers. Describe [3]'s design correctly. Either drop [5] or quote the column header that shows 18.091 is Whisper WER.

3. **Sentence:** "a 2023 table on that split lists 4.07% WER and STOI up to 0.731 [3]" (and "The 2023 leaders on the same four GRID speakers", and the M02/M06 table cells "4.07% ASR WER, GRID-4, direct targets [3]" / "STOI 0.731 / WER 4.07%, GRID-4 [3]").
   **Wrong:** 4.07% is the row "End-to-end WGAN (2022)" and 0.731 is the row "Lip2Wav" (2020), two different systems reported inside [3]'s comparison table. Neither is a 2023 system, and the table cell presents them as one result.
   **Fix:** Name each system and year (e.g. "End-to-end WGAN (2022) reaches 4.07% WER and Lip2Wav (2020) STOI 0.731, both as listed in [3], Table IV"), cite the original papers or mark them as reported by [3], and give [3]'s own row if it is better.

4. **Sentence:** "on those speakers later work cut ASR WER from 32.5% to 4.07% [2], [3]"
   **Wrong:** The two figures come from different ASR scorers (4% vs 0.1% WER on real audio, as the review itself says in M06), and from different systems. The Verdict states the drop with no caveat.
   **Fix:** Add the caveat, or use STOI in the Verdict: "later work raised STOI from 0.446 to 0.731 on those speakers [2], [3]; the WER figures (32.5% vs 4.07%) use different ASR scorers."

5. **Sentence:** "Vougioukas et al. found Lip2AudSpec ahead on PESQ (1.82 against 1.71) and behind on STOI and WER [2]: the inversion gives smooth audio, not intelligible audio."
   **Wrong:** The review says no experiment changes only the representation, then attributes [2]'s result to the inversion. PESQ does not measure smoothness.
   **Fix:** "...behind on STOI and WER [2]; which part of the system causes this is not tested."

6. **Sentence:** "The baseline's gender rates for the female speakers, 21% and 17%, are below guessing among three choices (inference), which points to a faulty baseline excitation, not a representation effect."
   **Wrong:** One of the three choices was "hard to say". Listeners choosing it on poor audio lower the correct rate without guessing wrong, so 1/3 is not the chance floor and the causal reading is unsupported.
   **Fix:** "The baseline's correct-gender rates for the two female speakers are 21% and 17% (Table 5); the paper does not report how often listeners chose 'hard to say' or the wrong gender, so a faulty baseline excitation cannot be ruled out."

7. **Sentence:** "On S4 the baseline wins on accuracy (57.7 against 54.9) and PESQ (1.79 against 1.61, Table 4); letters fall to 6.0% against 9.1% and 4.0% chance (Table 6)."
   **Wrong:** Table 6 columns (chance 25%, 4%, 10%) look like GRID word categories, not speakers, so the letter result is likely not an S4 result. The values 1.61 and 6.0% have no quote in the claim table.
   **Fix:** Split into two sentences: the S4 result (with a quote for 1.61) and "For letters, accuracy is 6.0% against 9.1% for Vid2Speech, with 4.0% chance (Table 6, all speakers)", adding the quote for 6.0%.

8. **Sentence:** "Word accuracy is 55.8% against 50.9% (Table 5), a 9.6% relative gain (inference), called "significantly better" with no test (Sec. 4.3.4)."
   **Wrong:** The authors' "significantly better" is claimed per speaker, "for three out of four speakers", not for the average.
   **Fix:** "Word accuracy is 55.8% against 50.9% (Table 5), a 9.6% relative gain (inference); the paper calls it "significantly better ... for three out of four speakers" with no test (Sec. 4.3.4), and on S4 the baseline is ahead."

9. **Sentence:** "The bottleneck gain rests on one speaker and one run, and four of the five bottleneck settings tried lose to direct spectrogram regression." (also M02: "The bottleneck gives PESQ 1.76 against 1.69 for the best direct-spectrogram run")
   **Wrong:** The claim-table quotes for Tables 7 and 8 are number rows without column headers, so which column is direct regression and which are bottleneck settings cannot be checked; 1.29 appears in both tables.
   **Fix:** Add the column headers of Tables 7 and 8 to claim rows 8 and 9 and confirm the count "four of five"; if the 1.29 column of Table 8 is not a bottleneck variant, change the count.

10. **Sentence:** "Before 2018 lip-to-speech was parametric: LSP of LPC [4] or an artificially set excitation [6]."
    **Wrong:** Too general: Ephrat, Halperin & Peleg (ICCV Workshops 2017, arXiv Aug 2017) already predicted spectrogram-domain features (medium confidence). It is concurrent with the target, so not a missed citation, but the sentence claims the whole field.
    **Fix:** "The two prior systems the paper compares against were parametric: LSP of LPC [4] or an artificially set excitation [6]."

11. **Sentence:** "Speaker characteristics are shown only for speakers seen in training (Sec. 4.2); on unseen speakers the method failed [2]." (and Verdict: "on unseen speakers the method produced no intelligible speech [2]")
    **Wrong:** The quote ("training the Lip2AudSpec model on the same data did not produce intelligible results") does not say which data; the unseen-speaker setting is asserted but not shown.
    **Fix:** Extend the quote in claim rows 2 and 25 with the preceding sentence that names the speaker-independent split, and cite its section in [2].

Not required but advised: update reference [3] to its journal version if it has one (evaluator recalls IEEE/ACM TASLP, 2024; low-medium confidence); M09 and M10 show identical counts (82), which is worth a quick check against the ledger.

## Scores

- Procedure: 6/10. Claim table covers every number, but several quotes lack headers or context, and one quote from a later paper was used to support a claim about the target.
- Final text: 6/10. The position is clear and the STMI and S29 points are strong; the M02 state of the art is wrong, the SOTA figures are misdated and merged, and three judgments go beyond their evidence.

Strengths (brief): the single-speaker, single-run ablation critique, the STMI averaging error, and the scorer caveat in M06 are well-founded and properly located.
