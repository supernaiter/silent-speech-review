# Evaluation: Speaking Without Sound (multi-speaker silent speech voicing from facial inputs)

Date: 2026-11-16. Independent evaluator, single pass over the review and its claim table. The claim table was filled by the writer, not by a separate checker, so a quote that is cut short or missing is counted as insufficient evidence, not as support. Sources were not re-opened.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Two changed components: face-image voice (M08) and pitch-flattened ContentVec target (M02) | Row 1 (Abstract; Sec. I) | correct | Both quotes support it. |
| 2 | Silent WER 40.12 to 38.91, voiced CER 9.96 to 13.28 (Table I) | Rows 3, 13 | correct | The column order is assumed (voiced WER, silent WER, voiced CER, silent CER). Voiced WER also gets worse (16.98 to 17.48), and the review does not mention this. |
| 3 | 3.0% relative silent WER gain, 33% relative voiced CER loss | Row 13, arithmetic | correct | 1.21/40.12 = 3.0%; 3.32/9.96 = 33.3%. |
| 4 | "Voiced CER loss of 3.32 points exceeds every silent gain" | Rows 3, 21 | correct | The silent gains are 1.21 (WER) and 1.86 (CER). |
| 5 | "From one training run" / "the paper reports one run per variant" | Rows 14, 24 (t80, cut off at "all experim...") | insufficient evidence | The quote may say that experiments were repeated over trials. No quote shows a single training run. |
| 6 | Similarity 0.5657 against random same-gender 0.5521, 2.5% relative | Rows 9, 19 | insufficient evidence | 0.5521 is not in any quote. The arithmetic is correct (0.0136/0.5521 = 2.46%). It is not stated which column (Base/Flatten, voiced/silent) 0.5657 is. |
| 7 | "Non-significant subjective difference" | Row 19 | insufficient evidence | No quote or location for a significance test. |
| 8 | Global F0 errors 24.80/30.83 against random 29.18/37.50 Hz, 15% and 18% lower | Row 20 | insufficient evidence | 29.18 and 37.50 are not in the quote. The arithmetic is correct (15.0%, 17.8%). |
| 9 | "The face predicts pitch within gender, not identity" | Row 20 | wrong (logic) | The random baseline is same-gender, so a 15–18% lower F0 error is evidence of facial cues beyond gender for pitch. The sentence reverses this. |
| 10 | "40 times" n_test; paired t-tests count repeats of one EMG input | Row 22 | partly supported | The "40 times" quote supports the resampling of faces. Nothing quotes the paired t-tests. |
| 11 | Silent pitch metrics scored against the voiced recording, nearest interpolation (§IV-B3) | No row | insufficient evidence | No claim row. On this benchmark, scoring against the parallel voiced recording is usual practice. The bullet does not say why it is an overclaim. |
| 12 | Face-image voices without reference audio in lip-to-speech, 2023 [2], [3] | Rows 2, 8 | correct, incomplete | Face-image voice control is older than 2023: Face2Speech (Goto et al., Interspeech 2020) for TTS, and Face-TTS / "Imaginary Voice" (Lee et al., ICASSP 2023). |
| 13 | [2] EER 36.72% face against 26.57% reference audio | Rows 8, 23 | correct | Both values are in the Table 1 quotes. |
| 14 | DiffV2S 3.91 MOS voice-face matching, unseen LRS3 speakers [3] | Row 7 | insufficient evidence | 3.91 is in the quote, but the quote does not show which column is voice matching. A MOS from a different listener panel cannot be compared with the target's embedding similarity. |
| 15 | "Neither video precedent is cited" | No row | insufficient evidence | It needs a locator (the target's reference list). |
| 16 | [5] DiffMV-ETS takes a speaker embedding from target audio [concurrent] | Row 6 | correct | The quote supports it. The label is plausible (Interspeech 2025, within about 4 months of ICASSP 2025). |
| 17 | [7] 25.14% WER mel, 26.55% units, 10 seeds | Row 12 | correct | The values and SDs are in the quote. |
| 18 | Seed variation about 1% WER [7] | Rows 14, 24 | correct | Quote: "approximately 1%". |
| 19 | Diff-ETS: 30.0% WER, 15.6% CER encoder, 32.1% own model, Whisper medium.en [4] | Rows 4, 16 | correct for values; condition insufficient | The numbers and the ASR model are quoted. The quotes do not show "silent split". |
| 20 | 38.91 is 30% worse than 30.0 | Row 16 | correct | 8.91/30.0 = 29.7%. |
| 21 | [8] 11.89% WER, rescores SU-ETS at 26.29% | Row 17 | correct for values; condition insufficient | The abstract quote is cut off ("on the"). It does not show the split or the ASR model. |
| 22 | "Three earlier models below 38.91%" | Row 18 | correct | Diff-ETS encoder 30.0, Diff-ETS 32.1, SU-ETS 26.29. The last value is a 2026 rescore of a 2023 model. |
| 23 | [6] 42.2% against 68.0% | Rows 10, 15 | correct | Note that these are DeepSpeech-scored, so they cannot be compared with Whisper numbers. |
| 24 | M02 table cell "Spectral targets (pattern match 54)" | Row 11, Appendix rows 31, 33 | wrong (label) | 54 is the number of studies that mention self-supervised representations. Mel targets are 36 of them. |
| 25 | M12 verdict `behind` | Section M12 | partly supported | The missing external baseline is shown. The 30% gap is mixed up with the voice change (face-chosen voices against the recorded speaker's voice). |

## Required fixes (by impact)

1. **Sentence (Verdict):** "Audio-free multi-speaker voicing holds as a pipeline; voices matching faces beyond gender and effective pitch disentanglement do not." and **(Where the claims outrun the evidence):** "...so the face predicts pitch within gender, not identity."
   **What is wrong:** The review's own F0 evidence compares against a random *same-gender* speaker and finds 15–18% lower error. That is evidence for facial cues beyond gender for pitch. The review states the opposite, so the position is stronger than its evidence and contradicts it.
   **Fix:** Separate pitch from timbre. For example: "Beyond gender, the face improves global F0 (15–18% lower error than a random same-gender voice, Table III) but barely changes timbre (0.0136 similarity margin, Table II); identity-level matching is untested." Change the Verdict sentence to match.

2. **Sentence (M02 State of the art):** "A [later] 2026 study on the same split, 10 seeds, reaches 25.14% WER with mel targets..." and table cell "25.14% WER, mel [7]".
   **What is wrong:** The M12 section reports 11.89% WER [8] on the same split. Giving 25.14% as the state of the art in one section and 11.89% in another is an internal contradiction. The quote for [8] is also cut off, so it does not establish the split or the ASR model.
   **Fix:** Relabel the M02 line as the best controlled comparison of target types ("best like-for-like comparison of mel against unit targets"), or give 11.89% [8] as the state of the art and keep [7] as the target-type evidence. Add the [8] quote that shows the silent split and the Whisper model.

3. **Sentence (Verdict):** "lip-to-speech set voices from face images without reference audio in 2023 [2], [3], so the new step is the transfer to EMG." and **(M08):** "The 'first' claim (§I) holds only for EMG input, and neither video precedent is cited."
   **What is wrong:** Face-image voice control is older than 2023 and is not limited to video: Face2Speech (Goto et al., Interspeech 2020) and Face-TTS / "Imaginary Voice" (Lee et al., ICASSP 2023) both set a TTS voice from a face image. The "neither cited" statement has no locator.
   **Fix:** Name Face2Speech (2020) as the earliest deciding prior, together with [2] and [3]. Write "face-image voice control dates to 2020 in TTS and 2023 in lip-to-speech". Give the location in the target's reference list that supports "neither is cited".

4. **Sentence (M08):** "its similarity of 0.5657 against 0.5521 for a random same-gender speaker (Table II)" and **(Where the claims outrun):** "...against random 29.18 Hz and 37.50 Hz are 15% and 18% lower".
   **What is wrong:** The baseline values 0.5521, 29.18 and 37.50 are not in any claim-table quote. It is also not stated which variant and condition 0.5657 refers to.
   **Fix:** Add the Table II and Table III quotes for the random-speaker rows. State "Flatten, silent" (or whichever applies) next to 0.5657.

5. **Sentence (Verdict):** "...from one training run on one EMG speaker." and **(M02):** "...and the paper reports one run per variant." and **(Where the claims outrun):** "...so paired t-tests count repeats of one EMG input." and "...and a non-significant subjective difference."
   **What is wrong:** None of these has a supporting quote. The quote given for the first (t80) is cut off at "all experim..." and may describe repeated trials.
   **Fix:** Quote the passages that state the number of training runs, the use of paired t-tests and the subjective-test result. If none exists, write "no repeated training runs are reported" and remove the statements about the t-tests and significance.

6. **Sentence (M12 State of the art):** "With the same Whisper medium.en, the 2024 Diff-ETS paper reports 30.0% WER ... the target's 38.91% is 30% worse in relative WER (inference)."
   **What is wrong:** Diff-ETS synthesizes the recorded speaker's own voice. The target synthesizes face-chosen voices of other speakers, which by itself can raise ASR error. The confound appears two paragraphs later but not where the number is given. The quotes also do not show that the 30.0% is on the silent split. Diff-ETS appeared about four months before the ICASSP 2025 deadline, so the authors may not have been able to compare against it.
   **Fix:** Add the condition in the same sentence ("in the recorded speaker's voice, against face-chosen voices here"). Add a quote that shows the silent split. Base the `behind` verdict on the missing external baseline, not on the 30% gap.

7. **Table cell (M02):** "Spectral targets (pattern match 54)"; **with the M02 verdict** "standard".
   **What is wrong:** 54 is the number of studies that mention self-supervised representations, not the number of spectral-target studies. Mel targets are 36 of 54, and only 4 remove or perturb pitch. With 4 of 54, the pitch-flattened target is uncommon. A `standard` verdict therefore needs those 4 named as deciding priors.
   **Fix:** Change the cell to "Mel targets (36 of 54, pattern match)". Name the 4 pitch-removal studies in the Appendix and cite the closest one in the M02 section, or change the verdict under the SKILL rules.

8. **Sentence (Where the claims outrun):** "Silent pitch metrics score against a different utterance, the voiced recording, aligned by nearest interpolation (§IV-B3)."
   **What is wrong:** There is no claim-table row. On this benchmark, scoring against the parallel voiced recording is usual practice, so the bullet does not show an overclaim. It also does not say which speaker's F0 is the reference when the output voice comes from another face.
   **Fix:** Add the §IV-B3 quote. State the specific problem (for example, the F0 reference is the original speaker and not the face-chosen target), or remove the bullet.

9. **Sentence (M08 State of the art):** "A 2023 video-to-speech model with a speaker embedding taken from video alone reached 3.91 MOS for voice-face matching on unseen LRS3 speakers [3]."
   **What is wrong:** The quote does not show which column is voice-face matching. A MOS from a different listener panel cannot be compared with the target's speaker-embedding similarity. Whether it is the best work today is not argued.
   **Fix:** Quote the column header. Add "not comparable with the target's embedding similarity". Where possible, give an objective face-to-voice metric (for example, EER 36.72% in [2]) as the state-of-the-art value.

## Scores

- Procedure: 6/10. Most numbers can be traced and the arithmetic is right, but several baseline values and test-design statements have no quote, and the claim table was filled by the writer.
- Final text: 6/10. The position is clear and the confounds are mostly named, but the beyond-gender conclusion contradicts its own F0 evidence, the state of the art is inconsistent between M02 and M12, and the face-voice prior art starts in 2020, not 2023.

The main strengths are the correct relative-change arithmetic, the clear separation of silent and voiced effects, and the use of seed variance from [7] to judge the size of a 1.21-point gain.
