# Evaluation: Video-Driven Speech Reconstruction using Generative Adversarial Networks

Date: 2026-11-18. Independent evaluator, single pass. Inputs: the evaluator brief and the compact review with its claim table. I opened no sources. The writer filled the claim table, not a separate checker, so a quote only supports a claim when the quote itself contains the number. Arithmetic was recomputed. Statements about the literature come from my own knowledge and are marked as inference where I could not confirm them.

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Without the perceptual loss, WER is 83.3% (STOI 0.378) | Claim rows 2, 14 (Table 3 quote) | correct | The quote has 83.3% and 0.378. |
| 2 | 68% lower WER with the perceptual loss | Arithmetic | correct | (83.3-26.6)/83.3 = 68.1%. |
| 3 | Chance level of 81% for random GRID slot choices | Arithmetic from the GRID grammar | insufficient evidence | (3+3+3+0.96+0.9+3)/6 ≈ 0.81 is right only if the ASR outputs GRID words alone. The table does not show that the scorer is constrained to the grammar. |
| 4 | Against Lip2AudSpec: 18% lower WER, 16% higher STOI, 6% lower PESQ | Row 8 (quote: "WER 32.5% 26.6%") | partly | WER: (32.5-26.6)/32.5 = 18.2%, correct. The STOI and PESQ values are not in the quote. |
| 5 | Seen-speaker WER of 26.6%; unseen-speaker WER of 40.5% that varies from 40% to 60% by speaker | Rows 8, 23 | correct (26.6, 40-60%); 40.5 not quoted | The 40-60% range is quoted. The 40.5% figure is not. |
| 6 | Filtering the hum lifts PESQ to 1.80 and WER to 36%; STOI is printed as 4.7 | Row 25 | partly | The quote has STOI 4.7 and WER 36%. PESQ 1.80 is not quoted. |
| 7 | ASR scores 4% WER on real audio | Row 18 | correct | Quoted. |
| 8 | The speech encoder comes from the authors' face-animation model | Row 12 | correct | Quoted (Sec. 2.3). |
| 9 | The adversarial loss alone produces noise | Row 15 | correct | Quoted. |
| 10 | Predecessors use LSP [5], vocoder features [6] and an auditory spectrogram or autoencoder [7] | Rows 6, 11 | correct | Quoted. |
| 11 | WORLD-vocoder system [2]: ESTOI 0.455 vs 0.329 (seen) and 0.227 vs 0.198 (unseen) | Row 9 | partly | The quote has only this paper's row (0.329, 0.198). The values 0.455 and 0.227 are not quoted. The 38% and 15% figures follow arithmetically from them. |
| 12 | In [3], this system scores 19.94% WER and the successor [4] scores 4.07%; 80% lower | Row 7 | partly | 4.07 is quoted. 19.94 is not. (19.94-4.07)/19.94 = 79.6%, correct. |
| 13 | A mel-spectrogram system in [3] scores 5.62% | None | insufficient evidence | No claim-table row. |
| 14 | Unseen speakers in [3]: successor 16.05%, this paper re-scored at 32.76%; 51% lower | Rows 19, 22 | partly | Both values are quoted, and 51.0% is correct. But the 32.76 row in [3] is labelled "End-to-end WGAN (2018) [30]", while the target is from 2019. That row needs to be confirmed as the target. |
| 15 | "Today's best" on GRID unseen speakers is 16.05% | Row 19 | insufficient evidence | This is the successor's row in a 2023 table. The review does not show that it is the best row of [3]'s Table VII, or that nothing later beats it (inference: later GRID lip-to-speech work exists). |
| 16 | Speech units cut LRS3 WER from 72.5% to 50.7%, 30% relative | Row 13 | partly | 50.7 is quoted; 72.5 is not. (72.5-50.7)/72.5 = 30.1%, correct. |
| 17 | Earlier listener tests: 85% listener word accuracy [6], 23 MTurk transcribers [5], a survey [7] | Row 20 | partly | 85% is quoted. "23 MTurk" is not. |
| 18 | Earlier work declares speaker independence out of scope [5], [9] | Row 21 | correct | Quoted for [5]. |
| 19 | [10] and [11] are concurrent | Reference list | correct | AAAI 2019 (Jan-Feb 2019) and Interspeech 2019 are both within 6 months of the target's June 2019 arXiv. |
| 20 | The waveform route was "vindicated later" | Verdict vs M06 | wrong (overstated) | The successor [4] changes much more than the output type. The review's own mel-spectrogram comparator scores 5.62%, close to 4.07%. |
| 21 | "The unseen-speaker claim holds against prior work" | Verdict vs "Where the claims outrun the evidence" | contradiction | The verdict accepts the claim; the bullet section says the same claim outruns the evidence. |
| 22 | M05, M11 and M13 facts (50 kHz, 128x96, 7 frames, 90/5/5, 15/8/10, 4 days, 60 ms) | Component table | insufficient evidence | No claim-table rows. |
| 23 | Counts for usual approaches (49/41/16 of 165; 10/4/3 of 40; 83/51/38 of 165) | Appendix rows | not checkable | The Appendix is referenced but is not part of the review text. |
| 24 | M12 verdict "behind" | M12 section | correct | Backed by the paper's own cited priors that used listener tests, and by Sec. 3.2. |
| 25 | Reference 4 bibliography | Reference list | insufficient | The DOI is missing (inference: 10.1109/TCYB.2022.3162495). |

## Required fixes (ordered by impact)

1. **Sentence:** "The unseen-speaker claim holds against prior work, but 40.5% WER is halfway to chance (inference) and today's best is 16.05% [3]."
   **What is wrong:** 16.05% is the successor's row in [3]'s 2023 table. The review does not show that it is the best row of that table: [3]'s own pretrained model may score lower. It also does not show that no later work (2023-2026) beats it. The M12 "State of the art" line has the same problem.
   **Fix:** Report the best row of [3]'s Table VII, with its system name. Otherwise write "the best result in the 2023 comparison [3] is 16.05% (successor [4])". Check for later GRID unseen-speaker results and name any that are lower.

2. **Sentence:** "The waveform route was vindicated later, not here: a WORLD-vocoder system beat it on ESTOI within a year [2], and on one scorer its 19.94% seen-speaker WER fell to 4.07% with the journal successor [3], [4]."
   **What is wrong:** The successor changes the encoder, the discriminators and the losses, not only the output type. In the same table, a mel-spectrogram system scores 5.62%, close to 4.07%. The evidence does not credit raw-waveform output with the gain, so "vindicated" is too strong. This is the strongest confound for the M06 position, and the review leaves it unhandled.
   **Fix:** "A later raw-waveform successor reached 4.07% against 19.94% for this system on one scorer [3], [4], but with a different network and losses; a mel-spectrogram system scored 5.62% in the same table, so the gain is not attributable to waveform output."

3. **Sentence:** "The unseen-speaker claim holds against prior work, …" (Verdict), set against the bullet "'First to produce intelligible speech' on unseen speakers (Abstract): 40.5% WER, … with no chance level and no baseline numbers."
   **What is wrong:** The verdict accepts the claim, and the bullet section says it outruns the evidence. The review needs one position.
   **Fix:** State one position, for example: "The claim to be first on unseen GRID speakers is not contradicted by prior work, which declared speaker independence out of scope [5], [9]; whether 40.5% WER counts as intelligible is unsupported without a chance level or listener test."

4. **Sentence:** "The perceptual loss carries the words: without it WER is 83.3%, near the 81% of random GRID slot choices (inference)."
   **What is wrong:** 81% is the chance level only if the ASR can output nothing but GRID-grammar words. The review does not state that condition or give a location for it. The same 81% also drives "halfway to chance" for the 40.5% figure.
   **Fix:** Add the condition and its location, for example "(inference: assumes the ASR of Sec. 3.2 outputs GRID-grammar words only)". If that cannot be confirmed, drop the comparison with chance.

5. **Sentence:** "The scorer matters: 26.6% and 40.5% here, 19.94% and 32.76% later [3]."
   **What is wrong:** The quoted row in [3] is "End-to-end WGAN (2018) [30]", but the target is from 2019. That row may refer to another version or another paper.
   **Fix:** Confirm from [3]'s reference list that [30] is the target, and say so in the claim table. If it is not the target, remove 19.94% and 32.76% from the Verdict, M06, M12 and the component table.

6. **Sentence:** "M02: the perceptual-loss ablation over seeds, encoder trained without test speakers."
   **What is wrong:** This hints at a real confound but never states it. The perceptual encoder is pretrained from the authors' face-animation model (Sec. 2.3). If that model saw GRID speakers that are held out here, both the perceptual-loss gain and the unseen-speaker result could be inflated. The review never raises this under "Where the claims outrun the evidence".
   **Fix:** Add a bullet: "The perceptual-loss encoder is pretrained on the authors' face-animation model (Sec. 2.3); the paper does not state whether its training data excluded the unseen test speakers." Use the paper's own wording if it states the training data.

7. **Sentences:** "…reached ESTOI 0.455 against 0.329 … and 0.227 against 0.198 [2]"; "…lists this system at 19.94% WER…"; "a mel-spectrogram system there scores 5.62%"; "filtering it lifts PESQ to 1.80"; "16% higher STOI but 6% lower PESQ"; "from 72.5% to 50.7%"; "23 MTurk transcribers"; and the component-table facts (50 kHz, 128x96, 7 frames, 90/5/5, 15/8/10, 4 days, 60 ms).
   **What is wrong:** None of these numbers appears in a claim-table quote. The quoted rows hold only the other value in each comparison, or nothing at all.
   **Fix:** Add a quote and location for each number, or remove the number.

8. **Sentence:** "(pattern match, Appendix)" (used throughout), together with claim-table rows 26-42 ("Questions for the authors", "Appendix: literature search").
   **What is wrong:** The review text has no Appendix and no "Questions for the authors" section. Every count is therefore unverifiable from the review.
   **Fix:** Include the Appendix and the questions section in the review, or point to where they are published.

9. **Sentence:** Reference 4: "Mira, R., … IEEE Transactions on Cybernetics, 2023, 53(6), 3454-3466. arXiv:2104.13332."
   **What is wrong:** The DOI is missing, and the venue was taken second-hand from a citing paper.
   **Fix:** Add doi:10.1109/TCYB.2022.3162495 (inference; verify it), and confirm the venue against the publisher record.

## What works

The arithmetic for every relative change is correct. Labels for later and concurrent work are applied correctly, and no later work is treated as prior work. The M12 "behind" verdict rests on the paper's own cited priors, and the hum and STOI-typo points are drawn from the authors' own text.

## Scores

- Procedure: 6/10
- Final text: 6/10
