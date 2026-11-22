# Independent evaluation: IR-UWB Radar-Based Contactless Silent Speech Recognition of Vowels, Consonants, Words, and Phrases

Date: 2026-11-22. Fallback evaluator (claim table only). I worked from the compact review and its claim table and did not re-open the sources. Where I name outside work, it comes from my own background knowledge, and the confidence is stated.

## Claim checks

| # | Claim (section) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | FERASEC gain is large and repeated over 20 participants (Verdict, M06) | Claim rows 1, 7; t6, t19, t21 | correct | t6 gives 20 participants. t19 and t21 give 51.59→80.56 (vowels) and 42.68→74.50 (consonants). |
| 2 | Relative gains of 56% and 75% (M06) | Row 7 arithmetic | correct | 80.56/51.59 = 1.562 and 74.50/42.68 = 1.746. This is plain arithmetic, so the "(inference)" tag is not needed. |
| 3 | DNN–HMM adds 5.91 and 7.09 points and loses on phrases, 96.88 vs 98.02 (M06) | Row 8; t21, t23 | correct | 86.47−80.56 = 5.91 and 81.59−74.50 = 7.09. The "(inference)" tag is again not needed. |
| 4 | Table 3 raw and clutter-reduced frames reach 44.38% and 48.13% on vowels (M06) | Row 9; t28, t29 | correct | The numbers match. |
| 5 | Raw frames were tested "only through a DNN–HMM" (Verdict, M06) | Rows 2, 9, 24; t56 | insufficient evidence | t56 refers to "these end-to-end approaches" in the plural. No quote shows that the DNN–HMM was the only model. The "256-dimensional frames" detail (t12) is not quoted. |
| 6 | [3]: TCN 91.1% vs 74.0% for "hand-crafted features + DNN–HMM", 50 words, fold spread 10.3→3.3, same testbed, one participant (Verdict, M06 SOTA) | Row 6; s1, s2 | partly correct | 91.1 vs 74.0 and the single participant are quoted. s1 calls the baseline only "the conventional hand-crafted feature method", so "+ DNN–HMM" is not quoted. The 50 words, the spread figures and the same testbed are also not quoted. |
| 7 | [3] is "the same group's" work and "reverses the conclusion on the same hardware" (Verdict, M06) | Reference list; row 9 | wrong / overstated | [3] has two authors (Lee, Yu), and only the first author is shared with the target. [3] uses one participant and a 50-word task. It does not repeat the raw-frame DNN–HMM test on vowels and consonants with 20 participants. It weakens the authors' generalisation but does not reverse it. |
| 8 | The 2016 vowel test used one speaker, F-measure 0.943 [2] (Verdict, "outrun") | Rows 3, 14; p1, p2 | correct | p1: "A speaker was asked to silently read…". p2: 0.943. |
| 9 | §V-D wrongly credits the 2016 vowel result to five speakers ("outrun") | Row 16; t68, p1, p3 | insufficient evidence | t68 is a fragment: "…classification tasks, respectively, with five speakers". p3 says the 2016 cross-validation was run "for each speaker independently", so [2] had more than one speaker in some task. §V-D may refer to a different 2016 task. The full t68 sentence is needed before calling this an error of the target. |
| 10 | [4] classified five vowels with a radar at 0.45 m for three participants ("outrun") | Rows 3, 14, 15; p5 | insufficient evidence | p5 confirms vowels A, E, I, O, U plus "empty". The 0.45 m distance and the three participants are not quoted. No quote says whether the speech was silent or voiced (it was under a face mask). If it was voiced, [4] does not count against a claim about SSR. |
| 11 | No radar study classifies consonants contactlessly, so "first phoneme-level" holds for the 11 consonants ("outrun") | Rows 15, 17; t4 | contradiction | Row 17 says the items are CVC and VCV syllables classified as whole tokens, not phonemes. The review cannot say both that the claim "holds" for consonants and that the items are not phonemes. |
| 12 | [6]: contact radar, 26 phonemes, 85.40%, pooled three-speaker model ("outrun") | Row 17; p8 | partly correct | 85.40% for radar is quoted. The 26 phonemes, the pooled three-speaker model and the contact placement are not quoted. |
| 13 | Words and phrases use only the 4 native English speakers (M12) | Row 13; t7 | plausible, partly quoted | t7 is cut off before the restriction appears. The "Table 2 note" itself is not quoted. |
| 14 | Table 2 gives means with no spread, seeds or chance level (M12) | Row 12; t60, t45 | plausible | An absence claim. The quotes are consistent with it but cannot prove it. |
| 15 | Per-participant LOOCV over 20 repetitions (Verdict, M12) | Rows 4, 10; t17, t9 | correct | — |
| 16 | 2016 baseline used template matching or HMMs, "two CLEAN features", per-speaker "jackknife" (M06, M12 usual approach) | Rows 5, 10; p3 | insufficient evidence | p3 supports per-speaker cross-validation only. No quote supports the classifier type, the two CLEAN features or the word "jackknife". |
| 17 | Lip vs chin differ in antenna and beam (55°×50° vs 40°×35°) and distance (5–10 vs 10–15 cm) ("outrun") | Row 18; t63 | partly correct | The antenna types and beam widths are quoted. The distances are not. |
| 18 | Position aid tested on one participant, 89.38% vs 88.13% on vowels ("outrun") | Row 19; t43, t44 | insufficient evidence | t43 reads "when both uppe…". The quotes do not show which condition is the aided one. The single participant (t55) is not quoted. |
| 19 | [5] Lip-Siri: three unseen users, 81.5–85.5% words, 36.3–39.6% sentence WER (M12 SOTA) | Row 11; s6 | partly correct | The word range is quoted. The WER range is cut off in s6. |
| 20 | Usual approach M06: engineered features, 21 of 32 (pattern match) | Rows 5, 26 | plausible | This is a ledger count. Appendix row 26 calls 21 an "upper bound", but the M06 text presents it as the default without that qualifier. |
| 21 | Usual approach M12: speaker-dependent, 22 of 32 | Rows 10, 30 | plausible, narrow | Speaker-independent is 17 of 32 (upper bound). The two overlap (22 + 17 > 32), so "usual" rests on a small margin. |
| 22 | Components table counts (M01–M13) | Table vs rows 25, 29 | internal inconsistency | M05 "Contactless radar (slot-filled 8,898)" is larger than either stated unique-study total (7,345 for M06, 6,960 for M12). Contactless radar is also not plausibly the usual sensor across silent speech work. The count appears to be the total number of slot-filled studies, labelled as if it were the count for the named design. M01, M04, M08 and M13 show the same pattern. |
| 23 | Chronology labels for [3] (2025), [5] (2026), [6] (2025) as [later]; [4] (2022) as uncited prior work | Reference list | correct | The target is from December 2023. [4] (August 2022) predates it by more than 6 months, so calling it uncited is fair. |
| 24 | M12 is "behind" [later] RF work on unseen users (Verdict) | Row 4 | judgment too strong | [5] uses a different modality (Wi-Fi backscatter), a different task and different users. "Unlike" fits the evidence; "behind" does not. |

## Central claim and confound

- The strongest confound for the FERASEC gain is the baseline. It is the authors' own 2016 feature set, designed in [2] for a single-speaker setup, and it is compared only with MD-DTW. Table 2 as quoted does not show the old features run through the DNN–HMM. The review reports the gain as well supported but does not address how strong the baseline is. The 56% and 75% relative gains start from a low base (51.59% and 42.68%); the absolute gains are 29.0 and 31.8 points.
- In the raw-frames argument, the review sets a single-participant, 50-word result [3] against a 20-participant vowel and consonant result. This mixes task, data and participant count. The review names the single participant, but it still says the result "reverses" the target's conclusion.

## Absence and novelty

- "First phoneme-level contactless radar SSR": the review names [2] and [4] as deciding priors for vowels. It should also name the earlier contact precedent for radar phoneme recognition, Birkholz, Stone, Wolf and Plettemeier, "Non-invasive silent phoneme recognition using microwave signals", IEEE/ACM TASLP 26(12), 2018 (medium confidence on volume and pages). The review currently cites only a [later] 2025 work [6] for contact radar phonemes.
- Contactless RF work on mouth shapes predates the target outside radar, for example WiHear (Wang et al., MobiCom 2014, Wi-Fi). It does not decide a radar-specific claim but is worth one clause if the qualifier is widened to "RF" (low to medium confidence on how it maps to phonemes).

## Verdicts

All slot verdicts are `standard`, `not applicable` or `not reported`. There is no `ahead` verdict to audit. M13 "not reported" fits the text: device use is asserted, not measured.

## Required fixes (ordered by impact)

1. Resolve the contradiction between "the claim holds for the 11 consonants" and "the items are CVC/VCV syllables, not phonemes". State one position: either the consonant claim holds only as syllable-token classification, or it does not hold as phoneme recognition.
2. Tone down "reverses the conclusion on the same hardware" and "beats". [3] is one participant and 50 words and does not repeat the raw-frame test. Replace "the same group's" with "the first author's later". Quote the [3] baseline and do not write "+ DNN–HMM" unless [3] says it.
3. Verify "raw frames were tested only through a DNN–HMM" against Table 3 and §V-E1. t56 says "approaches" in the plural. If several models were tested, rewrite the M06 and Verdict sentences.
4. Re-check the §V-D "five speakers" correction against the full t68 sentence. p3 shows [2] had multiple speakers in some task, so §V-D may be about a different 2016 task. Keep the correction only if §V-D clearly refers to the vowel test.
5. Establish whether [4] used silent or voiced speech and quote the 0.45 m distance and the three participants. If the speech was voiced, [4] does not qualify an SSR-first claim and should be presented as voiced RF vowel classification.
6. Address the baseline confound: the old features are evaluated only with MD-DTW, and the relative gains start from a low base. Give the absolute gains next to the relative ones.
7. Fix the components-table counts. M05's 8,898 is larger than both unique-study totals, and it labels a total slot count as the count for "contactless radar". Either show the count for the named design or label the number as a total.
8. Add the missing quotes to the claim table: [3] fold spread 10.3→3.3, 50 words and same testbed; the 256-dimensional frames; the [5] WER range; the lip and chin distances; [6] 26 phonemes, pooled three speakers and contact placement; the 2016 classifier, "two CLEAN features" and "jackknife"; and t55 (one participant) plus the full t43 condition for the position aid.
9. Name Birkholz et al. 2018 (TASLP) as the earlier contact-radar phoneme precedent next to [6].
10. Replace "behind" with "unlike" for the M12 comparison with Wi-Fi backscatter [5], and say that the modality differs.
11. Mark the M06 usual-approach count as an upper bound, as the Appendix does. Note the narrow 22 vs 17 margin in M12.
12. Drop the "(inference)" tags from direct arithmetic on Table 2 values.

## Scores

- Procedure: 7/10. The claim table covers every number, but about a third of the supporting details are not in the quoted passages, and the table counts are inconsistent.
- Final text: 6/10. The position is clear and the comparisons are well chosen, but the phoneme-claim contradiction, the overstated "reverses" and the unverified §V-D correction need fixing.

The arithmetic, chronology labels and core Table 2 and Table 3 numbers are accurate, and the lip-versus-chin confound is a useful addition beyond what the authors report.
