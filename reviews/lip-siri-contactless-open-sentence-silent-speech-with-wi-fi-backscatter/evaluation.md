# Evaluation: Lip-Siri: Contactless Open-Sentence Silent Speech with Wi-Fi Backscatter

Date: 2026-11-22. Fallback evaluator (claim table only). Input: the compact review with its claim table. Sources were not re-opened; points marked "evaluator knowledge" are from memory and need checking against the source.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target changes sensor (backscatter tag) and output (subword sentences) | Row 1; Sec. V-C.2 quote | correct | The quote supports subword-token output. The tag is cited by location only, with no quote. |
| 2 | Wi-Fi lip reading predates the target [2] | Row 2; Hameed Abstract | correct | The quote names Wi-Fi and radar lip reading. Earlier Wi-Fi lip reading exists (WiHear, Wang, Zhou and Ni, MobiCom 2014; evaluator knowledge), so [2] is a valid example but not the earliest. |
| 3 | 340 scripted sentences, each read at least twice, 80/20 random split | Rows 3, 11, 18 | insufficient evidence | 340 sentences and the random 80/20 split are quoted. "Each read at least twice" has no quote. Recurrence of test sentences in training is correctly marked as inference. |
| 4 | 36.87% WER vs visual baseline 32.3% in the same room | Rows 4, 14 | correct | 32.3% and "same test environment" are quoted. 36.87% is cited (t19) but not quoted in these rows. |
| 5 | M05 usual approach: 21 of 33 RF studies use radar | Rows 5, 19, 20 | wrong (mixed bases) | 33 is a pattern-match count of unique studies and 21 is a slot-filled count (Appendix: 7,329 slot-filled). Writing "Of 33 ..., 21" mixes two denominators. |
| 6 | M05 SOTA: 95% Wi-Fi lip reading, five vowels plus closed lips (2022) [2] | Row 6 | partly correct | 95% is quoted. "Five vowels plus closed lips" is not quoted. |
| 7 | M05 SOTA choice | Rows 6, 10 | wrong (weak choice) | The review itself cites contactless mmWave radar sequence systems at 9.5% and 4.55% WER on fixed sentence sets (Table I). Those are closer to the target's task than six-class vowel classification. |
| 8 | M08 usual approach: class label most common, 5 of 19 | Rows 7, 23, 24 | wrong (contradicted by Appendix) | The Appendix gives full-text pattern counts with sequence decoding at 12, against class label at 5 (slot-filled). "Most common" holds only within the slot-filled subset, and the review does not say so. |
| 9 | Deciding priors classify vowels [2] or fixed sentences [4] | Row 7 | correct | The RVTALL quote supports sentence classification. |
| 10 | SoniSpeech 26.3% open-vocabulary silent WER, 1,000 test sentences, one speaker [5] [later] | Rows 8, 9 | partly correct | 26.3% and 1,000 sentences from a separate split are quoted. "One speaker" has no quote. The [later] label is consistent (arXiv 2608 vs 2601). |
| 11 | 10.57-point gap; 12 users | Row 9 | correct | 36.87 − 26.3 = 10.57. 15 − 3 = 12, marked as inference. |
| 12 | Table I radar systems at 9.5% and 4.55% WER, closed-set | Row 10 | partly correct | mSilent 9.5% is quoted. 4.55% is not quoted. |
| 13 | M12 usual approach: 22 speaker-dependent, 17 speaker-independent of 32 | Rows 11, 27, 28 | insufficient evidence (ledger) | The counts come from the ledger. They overlap (39 > 32), which is acceptable, but the review should say they overlap. |
| 14 | M12 SOTA: the target's own new-user result, 81.5–85.5% / 36.3–39.6% | Row 12 | correct number, wrong framing | The numbers match the Sec. VI-F quote. Naming the target as the state of the art for its own component is circular. |
| 15 | New users within about 4 points of 85.61% | Row 13 | correct | 85.61 − 81.5 = 4.11. |
| 16 | 4.57 points, 14% relative above baseline; authors say "comparably" | Row 14 | correct | 36.87 − 32.3 = 4.57, and 4.57/32.3 = 14.1%. That the baseline is [8] (Ma et al. 2022) is not shown by the quote. |
| 17 | Voice-assistant test: 50 dB noise, Siri 98% to 31%, Lip-Siri 90.5% with 100-word lexicon | Row 15 | insufficient evidence | Only the 98% quiet result is quoted. 50 dB, 31%, 90.5% and the 100-word lexicon have no quote. The "(inference)" tag sits after the reported numbers, so it reads as if those numbers were inferred. |
| 18 | 717.5 ms latency starts at a manual end click | Row 16 | partly correct | The manual start and end buttons are quoted. 717.5 ms is not quoted. |
| 19 | Two-month drift: accuracy −4.3%, WER +5.6%, unit unclear | Row 17 | correct | The quote matches, and it does not state the unit. |
| 20 | Claim table row 18, "Questions for the authors" | Row 18 | wrong (internal) | The review has no such section. |
| 21 | "Only the sensing chain is new" (M05 novelty) | M05 section | insufficient evidence | No deciding prior is named for backscatter speech sensing. An earlier backscatter design exists: RFID Tattoo, wireless RFID tags on the face for speech recognition (Wang et al., Proc. ACM IMWUT 3(4), 2019; evaluator knowledge). It is contact-based but has the same backscatter sensing chain. |
| 22 | Verdict: "36.87% WER is worse ..., so the paper shows ... not open-sentence silent speech" | Verdict | wrong (logic) | The open-sentence conclusion follows from the random split, not from the WER gap to the baseline. "So" links two separate findings. |
| 23 | Slot verdicts | Table | correct | No `ahead` or other non-standard positive verdict, so the `ahead` rules do not apply. M13 is "not reported" although the SDR and 20 dBm are reported. It is defensible because power is not measured, but the reason should be given. |

Central confound: test sentences recur between training and test under the random split. The review identifies this and handles it well. A second confound is not handled: the review does not say whether the visual baseline [8] was trained or fine-tuned on the same 340-sentence corpus. If it was not, the 4.57-point comparison favours the system that saw the test sentences, and the "worse than baseline" point understates the gap. Fairness: SoniSpeech is correctly labelled [later] and used only as a reference point, not as a missed citation. No author-reported caveat is presented as the review's own finding; jumping (§VIII-B) and lexicon coverage (§V-C.1) are both attributed.

## Required fixes (ordered by impact)

1. M08 usual approach: reconcile "class label, most common, 5 of 19" with the Appendix count of 12 for sequence decoding. Either state that the 5 of 19 is within the slot-filled subset, or name sequence decoding as the usual design and revise the M08 framing.
2. M05 state of the art: replace the six-class vowel result, or justify it, given that the review itself cites contactless radar systems at 9.5% and 4.55% WER on sentence sets (Table I). Those are the closer contactless comparators.
3. M05 usual approach: stop mixing denominators ("Of 33 [pattern match] ..., 21 [slot-filled]"). Give the count and its base consistently in the text and in the table.
4. Add source quotes, or remove the claims, for: "each read at least twice", "five vowels plus closed lips", SoniSpeech "one speaker", 4.55% WER, 50 dB, 31%, 90.5%, the 100-word lexicon, 717.5 ms, and the identity of the visual baseline as [8].
5. M05 novelty ("only the sensing chain is new"): name the deciding priors for backscatter speech sensing, for example RFID Tattoo (IMWUT 2019), and optionally WiHear (MobiCom 2014) for Wi-Fi lip reading. Then restate what is new: a passive, off-body tag rather than backscatter as such.
6. M12 state of the art: do not name the target as its own state of the art. Give an external evaluation protocol (for example, a speaker- and sentence-disjoint test) or write "–".
7. Verdict: remove the "so" that links the WER gap to the open-sentence conclusion, and state the two findings separately.
8. Voice-assistant bullet: move "(inference)" so that it covers only the point that audio noise cannot affect a radio sensor, not the reported 31% and 90.5%.
9. Visual-baseline comparison: say whether [8] was trained or fine-tuned on the target corpus. If the paper does not say, state that this is unknown.
10. Claim table row 18: remove it, or add the "Questions for the authors" section it refers to.

## Scores

- Procedure: 6/10
- Final text: 6/10

The review's main position (no sentence-disjoint test, so "open sentence" is untested) is well supported by quoted locations.
