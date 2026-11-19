# Evaluation: Ultrasound-based Silent Speech Interface Built on a Continuous Vocoder

Date: 2026-11-19. Fallback evaluator (claim table only). Input: the Verdict, the component sections, "Where the claims outrun the evidence", the reference list and the claim table. No sources were opened. Bibliographic details and later state-of-the-art work are checked only from general knowledge and are marked as such.

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper [1] changes the acoustic target (M06) and the excitation (M08): ContF0 and MVF replace V/UV plus F0 | Row 1 (Abstract, Sec. 3.3, Sec. 3.5) | correct | The quotes support ContF0/MVF/MGC-LSP prediction and Kalman interpolation. "Changes the acoustic target (M06)" conflicts with the M06 section, which says the paper "stays in this default" (parametric vocoder). |
| 2 | Interpolated F0 targets from articulation were prior practice [2], [3], [4] | Rows 2, 10, 11 | correct | All three quotes show continuous or interpolated F0. That all three priors keep a V/UV flag is quoted only for [2] (and implied for [4] by its V/UV error). No quote shows it for [3]. |
| 3 | 31 Hz vs 65 Hz scores each system against a different reference contour | Rows 3, 9, 21 (Table 1, Sec. 4.2) | correct (by inference) | "For all segments" and the authors' "interpolated F0 is simpler to predict" carry the point. Row 27 shows that the review itself does not know how unvoiced frames enter the 65 Hz figure, so the review should say the comparison is uninterpretable, not describe exactly how it is computed. |
| 4 | Listeners hear no significant difference | Rows 19, 22 (Sec. 4.3) | correct | "None of the 'c'–'f' / 'd'–'g' / 'e'–'h' pairs differed significantly." |
| 5 | M12 is behind the field (no intelligibility test) | Rows 17, 39, 40; M12 table row | insufficient evidence | The usual approach given is listener transcription, "11 studies before this paper (confirmed)". The Appendix row says 11 of 29 confirmed, and its usual-design line is "crowd_workers, 15". So 11 is a minority and does not match the stated usual design. The verdict is also written as "behind (typical of the field)", which contradicts itself. |
| 6 | Same group replaced the continuous vocoder with WaveGlow in 2020: MCD 5.47 to 5.37 dB, significant listener preference [5] | Rows 4, 16 | insufficient evidence | The quote shows only "error is attained by the baseline vocoder (MCD: 5.47 dB)". 5.37 is not quoted, and neither is any significance. The fragment may read "the lowest error is attained by the baseline vocoder", which would reverse the direction. Nothing quoted shows that the [5] baseline is the continuous vocoder. |
| 7 | Usual approach for M08 includes "the group's own two-network design [6]" | Row 5 | wrong / unsupported | The p7 quote is a results row (86.1%, 0.562, 0.719), not a design description. The t15 quote is the target's own baseline and describes three networks (V/UV, log F0, MGC-LSP), not two. |
| 8 | Paper drops the V/UV decision; MVF carries voicing (Sec. 4.1) | Row 6 | correct | |
| 9 | M08 state of the art: EMA to continuous log F0 plus V/UV flag, 10.49 Hz F0 RMSE and 10.32% V/UV error, one speaker, 2018 [4] | Row 7 | insufficient evidence | The quote "proposed 4.801 0.1260 0.4128 10.32 10.49" has no column headers, so the assignment of 10.49 to F0 RMSE and 10.32 to V/UV error cannot be checked. "One speaker" is not quoted. A 2018 result is not shown to be the best today. |
| 10 | Later work: 26.7 Hz on frames voiced in both signals, rtMRI, 2023 [7] [later] | Row 8 | correct | Both the number and the condition are quoted. The [later] label is right. |
| 11 | "The field now mostly leaves F0 implicit" (53 studies, 35 later) | Rows 8, 31 | wrong (wording) | 53 of 138 is not "mostly". It is more than the 31 explicit-V/UV studies, but less than half of the set. |
| 12 | 30.56 Hz is over all frames against an interpolated contour | Rows 9 (Table 1, Sec. 4.2) | correct | |
| 13 | MVF as voicing carrier appears in no other of the 138 studies except the group's follow-up | Row 12 | insufficient evidence | The quotes come only from the target. No Appendix tally row covers MVF, and the follow-up is not cited. Deciding priors are missing: the continuous vocoder with MVF and no V/UV flag already existed in statistical TTS. From general knowledge: Csapó, Németh, Cernak, Garner, EUSIPCO 2016 (continuous vocoder modelling unvoiced sounds), and Al-Radhi, Csapó, Németh, Interspeech 2017. The review also contradicts itself: the Verdict says "only dropping the flag is new", while M08 treats MVF voicing as unique. |
| 14 | Authors report false voicing from MVF predictions | Row 13 (Sec. 4.1) | correct | |
| 15 | M06 usual approach: parametric vocoder, 34 of 51 (10 prior); no prior study uses a neural vocoder | Rows 14, 35 | correct (tally) | The count comes from the Appendix. The quotes t14/p9 do not bear on the count. This is consistent with general knowledge: the group's 2020 WaveGlow paper is the earliest neural-vocoder ultrasound-to-speech work I know of. |
| 16 | M06 state of the art: 2025 Conformer to mel-spectrogram/HiFi-GAN significantly preferred over 2D-CNN, p = 0.037 [8] [later] | Rows 15, 26 | insufficient evidence | The quote gives only "statistically significant, with a p value of 0.037". It shows neither the comparison, nor its direction, nor the HiFi-GAN pipeline. No metric value is given, so the state of the art has no score to compare against. |
| 17 | M12 state of the art: EMA-synthesized speech, 30.1% listener transcription WER, 2018 [4] | Row 18 | correct (number); insufficient (state of the art) | The quote supports 30.1% from a subjective test. This result is from 2018 and from a different modality, and the review does not show it is the best today. |
| 18 | Predicted excitation + original spectra: 43.45 vs 40.87, not significant | Row 19 | insufficient evidence | 43.45 and the non-significance are quoted. 40.87 is not quoted, and neither is the mapping of variants to conditions. |
| 19 | Predicting spectra drops it to 18.59, a 57% loss; both vocoders end about equal | Row 20 | correct | (43.45 − 18.59) / 43.45 = 57.2%. It is labelled as inference. 18.59 vs 19.91 is quoted. |
| 20 | "Spectral mapping, not F0, limits quality" | Rows 19, 20, 22 | wrong (overstated) | The review's own numbers go from 56.06 (analysis-synthesis) to 43.45 (predicted excitation, original spectra). That is a 12.6-point loss from excitation alone. Spectral prediction costs more (about 25 points), but excitation is not free. The data support "spectral mapping limits quality more than excitation". |
| 21 | "Significantly lower RMSE" names no test and gives no voiced-frame RMSE; the authors concede that interpolated F0 is simpler to predict | Row 21 | correct | |
| 22 | Analysis-synthesis alone is 56.06 vs 55.03 (Fig. 3); the test supports equality | Row 22 | correct | |
| 23 | V/UV accuracy of 78.84% has no chance level or class balance | Row 23 | correct | The 77–81% per-speaker range is quoted. The review should say which system this V/UV figure belongs to, since the proposed system has no flag. |
| 24 | "A single CNN could be used" and real time are untested: three CNNs trained, no latency | Row 24 | correct | |
| 25 | Nine test sentences per speaker and no repeated runs | Row 25 | partly correct | Nine sentences is quoted. "No repeated runs" is not shown: the quote is about early stopping. |

Also unchecked: the component table gives "180 sentences each" (M03), "81.67 fps" (M05) and the slot-filled counts (4,015; 31; 1,608; 6,538; 8,898; 120; 82; 239; 6,721). None of them has a claim-table row or an Appendix tally row.

Central claim and confound: the strongest confound is that the F0 RMSE uses a different reference contour for each system (an interpolated contour against one with unvoiced frames). The review handles it and ties it to the authors' own concession. The second confound is the baseline's architecture: a separate V/UV network against no flag. The review notes that no condition isolates MVF. The relative-change figure (57%) is labelled as inference.

Fairness: [5], [7] and [8] are correctly labelled [later]. None is treated as prior work or as a missed citation. [2], [3] and [4] all appeared more than six months before the target. The review attributes the authors' own findings (false voicing, no significant difference, "interpolated F0 is simpler to predict") to the authors.

Bibliography (general knowledge, not verified): the entries for [1], [4], [6] and [7] look plausible. [2] has no page range.

## Required fixes (by impact)

1. M12 verdict: resolve "behind (typical of the field)". Either make the verdict standard, or show that listener intelligibility testing was the usual design before 2019. The stated usual approach (listener transcription, 11 confirmed) conflicts with the Appendix usual design ("crowd_workers, 15") and is a minority of the 29 confirmed studies. Give the state of the art for today with metric and value, or say that no comparable figure exists.
2. Replace "Spectral mapping, not F0, limits quality" with "spectral mapping limits quality more than excitation". By the review's own figures, predicted excitation alone costs 12.6 MUSHRA points (56.06 to 43.45).
3. [5] claims (MCD 5.47 to 5.37 dB, significant listener preference, continuous vocoder as the baseline): quote both MCD values, the significance statement and the identity of the baseline. The current fragment may say that the baseline had the lowest error, which would reverse the claim.
4. Novelty in M08: name the deciding priors for the flag-free continuous vocoder with MVF (the TTS work of the same group, e.g. Csapó et al., EUSIPCO 2016; Al-Radhi et al., Interspeech 2017). Cite the "group's follow-up". Add an Appendix tally row for the MVF absence claim. Make "only dropping the flag is new" (Verdict) agree with the MVF-uniqueness sentence (M08).
5. [6] "two-network design": unsupported. The quoted design (t15) is the target's three-network baseline. Quote the [6] design or remove the phrase.
6. [4] figures (10.49 Hz F0 RMSE, 10.32% V/UV error, one speaker): add the column headers and the speaker count to the quote.
7. [8] state of the art for M06: quote the comparison, its direction and the model pipeline, and give a metric value. The p-value alone is not a state-of-the-art figure.
8. Add the quote for 40.87 and the mapping of MUSHRA variants to conditions (Sec. 4.3, Fig. 3).
9. Add claim-table or Appendix support for "180 sentences each" (M03), "81.67 fps" (M05) and every slot-filled count in the component table.
10. Change "the field now mostly leaves F0 implicit" to a statement the count supports, e.g. "more studies now leave F0 implicit (53) than predict a V/UV flag (31)".
11. Verdict: change "changes the acoustic target (M06)" so that it agrees with the M06 section ("stays in this default"). For example: it swaps one parametric vocoder for another.
12. Remove or support "no repeated runs" (row 25) and "all three priors keep the flag" for [3] (row 11). Say which system the 78.84% V/UV accuracy belongs to.

## Scores

- Procedure: 6/10. Every number has a claim-table row, but several quotes lack the second number, the column headers or the direction. Some component-table numbers have no row, and one absence claim has no tally.
- Final text: 6/10. The review handles the main confound well. The M12 verdict contradicts itself, and the bottleneck conclusion goes beyond the review's own figures.

The review identifies the main problem with the headline result: the F0 RMSE compares different reference contours. It ties this to the authors' own concession, and it labels later work correctly.
