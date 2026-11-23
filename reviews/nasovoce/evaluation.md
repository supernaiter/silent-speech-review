# Independent evaluation: NasoVoce component review

Date: 2026-11-23. Evaluator input: the compact review, its reference list and its claim table only. No source was reopened. Points that depend on the evaluator's own knowledge of the literature are marked "(inference)" and have to be checked against the source before they are applied.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper changes the sensor site: microphone plus vibration sensor in the nose pad (Verdict) | Claim row 1, quote t1 (Sec. 1) | correct | The quote states it directly. |
| 2 | The fusion model is "a dual-input enhancer trained against a frozen recognizer" (Verdict) | Claim row 1, quotes t9, t11 (Sec. 4.1) | insufficient evidence | t9 gives the D-DCCRN objective as clean-speech reconstruction. t11 describes soft and hard distillation losses, which apparently belong to recognizer training. No quote says "frozen" or says the enhancer is trained through the recognizer. The sentence may merge two separate components. |
| 3 | Fusion for recognition predates the paper, which refutes the §2 claim (Verdict) | Claim row 2, quotes g1, t5 | correct | Graciarena 2004 fuses a standard microphone and a throat microphone for recognition, so the §2 "no prior work" sentence is wrong as written. |
| 4 | Conducted sensors paired with an air microphone "date from 2004" [2], [3] (Verdict) | Claim row 2 | wrong (inference) | Earlier pairings exist: Graciarena, Franco, Sonmez, Bratt, "Combining standard and throat microphones for robust speech recognition", IEEE Signal Processing Letters 10(3), 2003. Zheng et al., "Air- and bone-conductive integrated microphones for robust speech detection and enhancement", IEEE ASRU 2003. The 2003 Graciarena paper is also the earlier deciding prior for the §2 refutation. |
| 5 | The §1 claim that throat or skull sensors miss whisper is contradicted by [3] (Verdict) | Claim row 3, quotes t80, p1 | partly correct | [3] covers the throat, and only soft whisper. It says nothing about skull contact. For skull or behind-the-ear contact, the non-audible murmur work (Nakajima et al., ICASSP 2003, NAM microphone behind the ear) is the closer counterexample (inference). |
| 6 | Every quantitative test adds noise to the microphone only, with a clean vibration channel (Verdict, M12) | Claim rows 4, 15, 18, quotes t78, t79 | correct | Eq. 1 and the Fig. 6 caption support it. The Fig. 9 caption ("microphone signal with added noise") extends it to MUSHRA. |
| 7 | "Reliably recognize whispered speech even under noisy conditions" rests on digital noise with no point values, dispersion or test | Claim row 19, quotes t35, t64 | correct | The quote and the figure reference support it. The absence of dispersion is a reading claim with no quote, which is acceptable. |
| 8 | 1,000 evaluation items against 4 × 200 = 800 | Claim row 20, quotes t26, t28, t29 | insufficient evidence | The quote "200 utterances from each of" is cut off before the speaker count. n = 4 comes from a separate quote. The gap may have a plain explanation (for example, five groups of 200, or normal and whispered sets), so the review should present it as unexplained rather than as an error. Row 24 already asks the question. |
| 9 | The axes run from 20 to −10 dB SNR in Figs. 7 and 8, while the prose calls 10 dB "very strong noise" | Claim row 21, quotes t77, t39 | correct for Fig. 8; insufficient for Fig. 7 | Only the Fig. 8 axis is quoted. |
| 10 | MUSHRA at 0 dB: 68.7 against 37.6, a gain of +31.1, measured against raw noisy audio | Claim row 22, quotes t46, t47, t41 | arithmetic correct; condition insufficient | The quotes are the bare numbers 37.6 and 68.7, with no condition label and no dB level. The comparator ("raw noisy audio") rests on an unstated entry. |
| 11 | "Always-available" is not shown, because streaming is future work (§4) | Claim row 23, quote t25 | correct | |
| 12 | The authors concede that whispered enhancement degrades under noise (§6) | Claim row 18, quote t54 | correct | The review credits the authors correctly. |
| 13 | M05 state of the art: whispered WER mostly below 10% at noise up to 80 dB(A), one speaker [5] (2025) | Claim row 8, quotes w1–w4 | correct | The number, the condition and n = 1 all match. Whether a single-subject demonstration counts as the state of the art is debatable, but the review states n = 1, which is enough. |
| 14 | Throat microphone, soft whisper: WER 99.3% → 32.9% after adaptation, four speakers, quiet room [3] | Claim row 9, quotes p1, p2 | correct for the WER and the quiet room; insufficient for "four speakers" | No quote gives the speaker count. |
| 15 | M06 state of the art: WER at 0 dB SNR 95.6% → 52.6%, 45% relative [2] | Claim row 12, quote g2 | 95.6 correct; 52.6 insufficient; calculation correct | Only 95.6% is quoted. (95.6 − 52.6) / 95.6 = 45.0%. |
| 16 | M06: a 2004 result as the state of the art | M06 section | wrong (state of the art) | A 2004 result is the earliest deciding prior, not the best current work. More recent work on deep air and bone/body-conducted fusion includes Yu et al., "Time-domain multi-modal bone/air conducted speech enhancement", IEEE SPL 2020, and Wang, Zhang, Wang, "Fusing bone-conduction and air-conduction sensors for complex-domain speech enhancement", IEEE/ACM TASLP 2022 (inference; take the metric and value from the source). |
| 17 | [4]: two-channel model 32.9% U/V error at −11.4 dB, against 38.1% (conducted only) and 52.7% (air only), one speaker | Claim row 13, quotes n3, n4 | numbers present; column mapping and metric insufficient | The quote "38.1 52.7 32.9" has no column headers, and "U/V error" is not quoted. The value 32.9 also appears in [3], so check that the two were not mixed up. One speaker is supported. |
| 18 | Field "usually tests conducted sensors with noise physically present" [2], [4], [5] (Verdict); M12 usual approach is 44 physical against 15 digital out of 123 | Claim rows 5, 14, quotes g4, n2, w3 | wrong for [4]; insufficient for [2]; "usually" overstated | n2 states that recorded noise was "superimposed" on the signals, which is digital mixing of noise recorded through both channels, not noise present during recording. [2] reports results by SNR (clean, 0 dB), which suggests digital mixing too (inference). 44 of 123 (36%) is a plurality among the studies that name a protocol, not "usually". |
| 19 | Throat microphone corrupted by noise in a vehicle at about 100 dB SPL [2] | Claim row 17, quote g4 | insufficient evidence | The quote does not mention a vehicle or 100 dB SPL. The phrase "we found" in Sec. 1 may refer to the authors' earlier study, not to [2]. |
| 20 | The paper concedes a 2018 nose-pad vibration sensor (V-Speech) | Claim row 7, quote t81 | correct; incomplete | V-Speech is not given a reference number or a locator (Maruri et al., Proc. ACM IMWUT 2018; inference). The claim that the departure is "the co-located microphone" depends on whether V-Speech also used a microphone, and the review does not show that. |
| 21 | No single-input enhancer control, so the fusion gain is not separated from the enhancement gain (M06) | Claim row 22, unstated entry | correct as an absence claim | §5.2 reports that Vib alone beats Enhanced under strong noise. This is the paper's own evidence for the point and should be cited. |
| 22 | M12 verdict "behind (typical of the field)" | Table, M12 section | contradiction | The label calls the paper behind the field and typical of the field at once. By the review's own count (15 digital against 44 physical), digital-only testing is not typical. |
| 23 | M11 verdict "not reported" while the row describes "clean recordings and corpus transcripts" | Table | contradiction | Either the construction is reported or it is not. |
| 24 | M09 and M10 "not described" with verdict "not applicable"; usual approach "offline (82)" for both | Table | insufficient evidence | The labels are inconsistent with M11. The count of 82 also appears as the M05 whisper count. Confirm that it is not a copied value. |

## Central claim and confounds

The central claim is that fusing the nose-pad microphone and vibration sensor gives robust whispered recognition under noise. The review identifies the strongest confound correctly: the vibration channel stays clean while noise is added only to the microphone. The review also identifies the second confound, the missing single-input enhancer control. Both are handled. The review weakens its own case in two ways. It cites [4] (and possibly [2]) as examples of physically present noise, although both appear to use digital mixing. It also omits the paper's own §5.2 result, where Vib alone beats Enhanced, which is the most direct evidence for the confound. The positions on M05 and M06 rest on named citations. The M12 "behind" position rests on a 44 against 15 ledger split, which is weaker than "usually".

## Fairness

No work dated within 6 months of the target, or later, is treated as prior work. [5] dates from January 2025. The review credits author caveats correctly: §6 on whisper degradation, §4 on streaming, and §2 on V-Speech. It does not present them as its own findings.

## Absence and novelty claims

- "None of the 123 names a nose-pad site": the review names V-Speech (2018) itself, so this sentence describes a gap in the ledger, not novelty. Give V-Speech a reference and a locator.
- "Date from 2004": an earlier origin exists (2003, see row 4).

## Required fixes, by impact

1. Remove [4] as an example of "noise physically present", and check [2] on the same point. Replace "usually" with the actual split (44 against 15 of 123) in the Verdict and in M12.
2. Resolve the contradictory M12 verdict "behind (typical of the field)".
3. Replace "date from 2004" with the 2003 priors: Graciarena et al., IEEE SPL 10(3), 2003, and Zheng et al., ASRU 2003. Use Graciarena 2003 as the deciding prior for the §2 refutation.
4. M06 state of the art: relabel the 2004 result as the deciding prior, and state a current deep-fusion result with its year, metric and value (for example Yu et al. 2020 or Wang et al. 2022, values taken from the source).
5. Support or revise "trained against a frozen recognizer". The quoted enhancer objective is clean-speech reconstruction, and nothing quoted says "frozen".
6. Add the missing quotes: [2] 52.6% and the "vehicle, about 100 dB SPL" claim, with the right attribution. [4] column headers and the "U/V error" metric (and confirm that 32.9 is not mixed up with [3]). The [3] speaker count. The MUSHRA condition labels and the raw-noisy reference. The Fig. 7 axis range.
7. Limit "contradicted by [3]" to throat sensors and soft whisper, or add a skull/behind-ear counterexample such as the NAM microphone (Nakajima et al., 2003).
8. Align the M09, M10 and M11 verdicts with the row text ("not reported" against a described reference construction). Verify the repeated count of 82.
9. Cite V-Speech with a reference number and a locator. Show whether it used a microphone before calling the co-located microphone the departure.
10. Cite the paper's own §5.2 result (Vib better than Enhanced under strong noise) for the missing single-input control. Present the 1,000 against 800 point as unexplained, not as an error.

## Scores

- Procedure: 6/10. Claims are tied to locations and quotes, and the confound analysis is sound. However, several numbers and conditions lack quotes, and one comparator is miscategorized.
- Final text: 6/10. The position is clear and fair to the authors. The M12 framing, the 2004 origin date and the M06 state of the art need correction.
