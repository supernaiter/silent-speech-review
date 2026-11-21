# Independent evaluation: Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping

Date: 2026-11-21. Evaluator: fallback evaluator (claim table only). Input: the compact review, its claim table and reference list. Sources were not re-opened; outside knowledge is marked as such and needs checking.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | The paper changes M06, M03, M11, all standard (Verdict) | Claim 1, t9, t40 (Sec. 2.2, 2.5) | correct | Six mappings and frozen mapping at inference are quoted. |
| 2 | Imagined-to-listened mapping before a listened-trained decoder is "a new route (Appendix)" | Claim 2; M06 section; ref [4] | wrong (internal) | The M06 section names an earlier mapping study [4] (the authors' own) and gives the verdict `standard`. "New route" in the Verdict conflicts with both. It is new only as a mapping-then-decoding pipeline; say that. |
| 3 | No control passes unmapped imagined MEG or null-mapping output through the decoder (Sec. 3.4) | Claim 2, n3 | insufficient evidence | n3 shows the comparisons that were made (ceiling, chance). It does not show that no other control exists anywhere in the paper. Add a statement of what Sec. 3.4 and Appendix D contain. |
| 4 | Closed stimulus set: same two poems, 76 words as candidates (Sec. 2.4) | Claim 3, n7, t3 | correct | The poem-identity effect on ranks is marked as inference. That is appropriate. |
| 5 | Word-level "significant" result names no test (Fig. 4A) | Claim 3, n2 | insufficient evidence | The quote shows the word "significant". The absence of a test cannot be checked from it. |
| 6 | Usual approach M06: cross-condition generalization 8 of 112, perception-to-imagery 6 | Claim 4, claim 25 | insufficient evidence | The "6" is cut off in the Appendix row. 8 of 112 (7%) is not a "usual" design (see fix 6). |
| 7 | [3] overt-trained model 46.3% TER vs 46.6% covert-trained, eight sentences, 16 participants (2024) | Claim 5, k1, k3, p5 | partly correct | 46.3% and 16 participants are quoted. The k1 quote stops at "comparable to that using", so 46.6% and "eight sentences" have no quote. |
| 8 | [4] is the one earlier mapping example; it decodes nothing and calibrates on the held-out subject | Claim 6, b5, b42, b48 | correct | The calibration layer is trained on held-out subject data (b42), and the output is a listened-response reconstruction (b48). |
| 9 | Four-way accuracy 34% (predicted listened) vs 30% (imagined), a 13% relative gain | Claim 7, t25, t27 | correct | 4/30 = 13.3%. Against 25% chance this is +9 vs +5 points. That framing is stronger and could be added. |
| 10 | Encoder differences vanish in the full pipeline (Discussion) | Claim 7, n4 | correct | |
| 11 | [5] cross-subject MEG motor imagery; neither stage sees the held-out subject (Sec. 2.5) | Claim 9, h1, t41 | correct | |
| 12 | [6] 61.3% Top-10 over 1024 segments, 3-subject perceived-speech MEG, with fine-tuning (2026, concurrent) | Claim 10, s1, s2, s4 | insufficient evidence | s1 lists "61.3%, 43.0%, and 39.9%, respectively". The quote does not show that 61.3% belongs to the Armeni 3-subject, 1024-segment set. The [concurrent] label is correct (arXiv 2608, three months after the target). It is used only as state of the art, not as a missed citation. |
| 13 | Held-out mapping beats null, RNN t = 9.59 (Table 2), on the training subjects' four stimuli | Claim 11, t18, t3 | correct | The template inference is marked. |
| 14 | [2] MEG melodies, N = 71 (2023), vs 17 recruited, 13 in Fig. A7 | Claim 13, p1, t2, t43 | partly correct | 71 and 17 are quoted. "13 of them shown in Fig. A7" has no quote. |
| 15 | The paper permutes trial pairings for the mapping null (Sec. 2.3) | Claim 14, t13 | wrong (quote) | t13 says only that training is LOSO. It does not support a pairing-permutation null. Cite the passage that defines the null. |
| 16 | [3] shuffle model run through the full decoder, effect size 1.34 | Claim 15, k2 | partly correct | The shuffle model is quoted. The effect size 1.34 has no quote. |
| 17 | Word stage compared only with analytic chance and the listened ceiling (Sec. 3.4) | Claim 16, n3, t32 | correct | |
| 18 | M12 `not reported`: word-level test, decoder split unit and seeds absent (Appendix C) | M12 section | insufficient evidence | The claim table has no row for these absences. |
| 19 | Figs. A5–A6 use the top-20 most decodable words, chosen from the plotted results | Claim 17, n1 | partly correct | Top-20 selection is quoted. "Chosen from the plotted results" (circular selection) is inference and is not marked. |
| 20 | Consistent top-20 words could come from decoder bias; no input-shuffled control | Claim 18, t44, t45 | correct (inference) | The authors' own Fig. 4C overlap with the listened decoder's top-20 fits the bias reading. The review could say so. |
| 21 | Raw imagined p-value is 0.10 in Sec. 3.2 and 0.12 in the Fig. 2 caption | Claim 19, t25 | insufficient evidence | The only quote gives p = 0.10 and is located at "Sec. 3.2; Fig. 2 caption". No quote shows 0.12. As written, the table points the other way. |
| 22 | Table 3: BERT above BERT+Wav2Vec2 at Recall@5/@10, yet the latter is "best overall" | Claim 20, t33, t36, t37 | correct | 0.365 > 0.351 and 0.550 > 0.541; the combined model wins only at the first column (0.091 > 0.086). Column headers are not quoted. |
| 23 | Abstract claims direct BCI applicability; offline bidirectional RNN (Appendix A.1) | – | insufficient evidence | There is no claim-table row for this bullet. |
| 24 | Strongest confound handled | Verdict, M06 | correct | The review names the closed stimulus set (poem identity versus word identity) and the missing unmapped control. Both are the main confounds. |
| 25 | Chronology and fairness | References | correct | [4] is the authors' own and prior. [6] is correctly labelled concurrent and is not held against the authors. |

## Usual approach and state of the art

- **M06.** The stated usual approach covers 8 of 112 studies. The typical design is within-condition training on imagined data. Cross-condition transfer is the most common *transfer* design. The state-of-the-art line is restricted to overt-to-covert ECoG. For decoding imagined (inner) speech, later and stronger work exists: Kunz et al., *Cell*, 2025, "Inner speech in motor cortex and implications for speech neuroprostheses". It uses intracortical arrays, decodes inner-speech sentences from a large vocabulary and tests transfer from attempted to inner speech. Outside knowledge: check the metric and value before citing it.
- **M03.** The state of the art [6] uses target fine-tuning, so it is not zero-shot. A zero-shot cross-subject perceived-speech result would be a closer comparator if one exists. The review states the mismatch ("with target data"), which is acceptable.
- **M11 and M12.** These are plausible.

## Absence and novelty

- The "new route" claim names only [4] in the body. The Appendix lists [7] (Martin et al. 2014, which aligns covert speech to overt-trained decoders) as a deciding prior, but [7] is never cited in the text. Another candidate prior for overt-to-imagined transfer with domain adaptation, from outside knowledge: Lee, Y.-E., Lee, S.-H., Kim, S.-H., Lee, S.-W., "Towards Voice Reconstruction from EEG during Imagined Speech", AAAI 2023, arXiv:2301.07173. It is not a mapping into perception space, but it should be named as a deciding prior.

## Verdicts

- No slot is marked `ahead`, so the `ahead` rules are not triggered.
- M06 is `standard` while the Verdict calls the route "new". The two must agree.
- M13 is `not applicable` although the paper fills the slot (laboratory MEG, offline). `standard` fits better.

## Required fixes (by impact)

1. Claim 21: quote the Fig. 2 caption showing p = 0.12, or drop the p-value inconsistency bullet. The only quote gives 0.10 for both locations.
2. Make the Verdict and M06 agree. The route is new only as mapping plus decoding. [4] already maps imagined to listened MEG, and the verdict is `standard`.
3. Claim 12: show that 61.3% Top-10 is the value for the Armeni 3-subject, 1024-segment set. The quote reads "respectively" over three values.
4. Claim 15: replace t13 with the passage that defines the paper's pairing-permutation null.
5. Add quotes for the [3] values 46.6% (covert-trained), "eight sentences" and effect size 1.34, or remove them.
6. M06 usual approach: 8 of 112 is not usual. Call it the most common transfer design, or state the usual within-condition design with its count.
7. Add claim-table rows for "13 of them shown in Fig. A7", the abstract BCI claim and the bidirectional RNN (Appendix A.1), and the M12 absences (test, split unit, seeds).
8. Add support for "names no test" (Fig. 4A) and "no control passes unmapped imagined MEG" (Sec. 3.4). Say which sections were searched.
9. M06 state of the art: consider later intracortical inner-speech decoding (Kunz et al., *Cell*, 2025) as the best imagined-speech result, with its metric and value checked.
10. Novelty: cite [7] in the body as a deciding prior, and consider Lee et al., AAAI 2023 (arXiv:2301.07173).
11. Mark "chosen from the plotted results" (Appendix D.1) as inference, or cite where the selection is defined.
12. References [7] and [8] are not cited in the review text, and claim-table rows 22–23 refer to a "Questions for the authors" section that the compact review does not contain. Align them.
13. Set M13 to `standard` (laboratory MEG, offline), since the paper fills the slot.

## Scores

- Procedure: 6/10. The claim table covers most numbers, but several numbers lack quotes (fixes 1, 3, 5, 7), one quote does not support its claim (fix 4), and only the writer ran the claim check.
- Final text: 7/10. The position is clear, the confounds are identified and inferences are marked. The Verdict and M06 contradict each other, and one internal-inconsistency charge against the authors (p = 0.12) is unsupported.
