# Evaluator: a language model separate from the writer

Target: Herff et al., "Brain-to-text: decoding spoken phrases from phone representations in the brain", Frontiers in Neuroscience 2015, doi:10.3389/fnins.2015.00217.
Date: 2026-11-25. Input: compact.md (review + claim table), plus the source quotes recorded in notes.json (target t*, Jou 2006 p*, Schultz and Wand 2010 s*, comparators c*). No web check of the comparators was made; outside-knowledge points are marked "unverified".

## Claim check table

| No | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Gaussian phone models, dictionary, bigram, Viterbi (Verdict; M06) | t9, t12, t14, t15, t16 | correct | Quotes support every part. |
| 2 | "Abstract's priority claim concerns ECoG, not decoding" (Verdict) vs "The Abstract's priority claim for decoding continuous speech into words: the decoder already ran on continuous EMG" (Outrun bullet 1) | t1 | wrong (internal contradiction) | t1 says "for the first time ... from intracranial electrocorticographic (ECoG) recordings". The Verdict reads it correctly; the Outrun bullet attacks a claim the authors did not make. |
| 3 | Per-phrase dictionary holds the spoken words (§2.11) | t16 | correct | |
| 4 | Bigrams from the read texts, no stated exclusion of the test phrase (§2.10) | t15 | correct | Absence of exclusion is fairly stated as "no stated". |
| 5 | EMG prior kept test sentences out of its LM [2] | p4 | correct for [2] | Notes record that Schultz and Wand [3] do not state LM exclusion; the review rightly attributes it to [2] only. |
| 6 | 25% WER is closed-set; not comparable with [4] 25% on 1,024 words | t20, t16, c3, c4 | correct | Confound also includes task: [4] is attempted silent speech in an anarthric participant; not stated, minor. |
| 7 | "it matches the 10-word result (§3.2) (inference)" | t20, t21 | insufficient evidence | "75% of all words are recognized correctly" is word correctness; WER also counts insertions, so 75% correct does not by itself give 25% WER. The "(inference)" label is present; the wording "matches" should say "is consistent with, if accuracy counts insertions". |
| 8 | 47 of 102 record an HMM decoder; 28 HMM/GMM, 26 CTC (M06 usual) | Appendix | correct (consistent with Appendix) | |
| 9 | Card 2024: 2.5% WER final 5 sessions, 125,000 words [5] | c1, c2 | correct | |
| 10 | Metzger 2023: 25% median WER, 1,024 words [4] | c3, c4 | correct | |
| 11 | Jou: phoneme models + trigram; Schultz and Wand: 3-state HMMs + BN trigram | p1, p2, s1, s3 | correct | |
| 12 | Phone labels forced-aligned from parallel audio (§2.5) | t6, t18 | correct | |
| 13 | Authors concede context-dependent models need more data (§2.11, §4.1) | t35, t36 | correct | |
| 14 | 152 of 1,162 rescore with an LLM (M07 usual) | Appendix | insufficient evidence / inconsistent | Appendix inclusion rule for this table is "vocabulary of at least 1,000 words", yet the body describes the 1,162 as "studies naming a vocabulary, language model or lexicon"; the two populations differ. 152/1,162 (13%) is also not a usual design. |
| 15 | M07 SOTA on ECoG: 25.6% median WER with 50 words (Moses 2021) [6] | c6, c7 | number correct; SOTA wrong | [4] (2023, ECoG, already cited) reaches about the same WER on a 1,024-word set, and (unverified) reports a much lower median WER on its 50-phrase set; Moses 2021 is superseded by a work the review itself cites. |
| 16 | M07 SOTA "a 125,000-word vocabulary" [5] (also table row M07) | c2 | incomplete | No metric or value; the brief requires year, metric and value. |
| 17 | 108 and 101 words in [2], [3] | p3, s4 | correct | |
| 18 | 10 words: 75% correct (§3.2) | t21 | correct | |
| 19 | Randomized models share dictionaries and LM, so the test isolates the neural part | t16, t19, t25 | correct (reasoning) | |
| 20 | 21 of 145 sentence-disjoint; 45 and 17 of 132 nulls (M12 usual) | Appendix | correct (consistent) | 21/145 is a minority; the line names a usual approach the field does not usually take. |
| 21 | Willett 2023: held-out sentences, 23.8% WER, 125,000 words [7] | c5, c8 | correct | |
| 22 | "WER beats it at all dictionary sizes (p < 0.001)" | t25 | insufficient quote | t25 gives the test and p-value but not "all dictionary sizes"; the Fig. 5 caption may hold it. |
| 23 | Subject 4 both sessions and subject 5 session 2 rejected (§2.4) | t5 | correct | |
| 24 | §3.1 "approximately 150 ms" vs Fig. 4 caption "100 ms" is a contradiction | t30, t46 | insufficient evidence (likely not a contradiction) | The caption describes models at the 100 ms panel being different in auditory cortex; §3.1 says discriminability keeps rising until ~150 ms. Both can hold. |
| 25 | Real-time suitability asserted; evaluations offline (§4.4) | t33, t34 | correct, but the authors state it themselves | t33: "Despite the fact that the evaluations ... have been performed offline". Listing it under "claims outrun the evidence" presents the authors' own caveat as a finding. |

## Numbered findings (ordered by impact)

1. **Internal contradiction on the priority claim (Verdict vs Outrun bullet 1).** The Verdict correctly says the Abstract's "first time" claim concerns ECoG (t1). The first Outrun bullet then says the claim is about "decoding continuous speech into words" and refutes it with EMG work [2], [3]. The authors claim ECoG only. Delete or rewrite the bullet (for example: "the decoding chain is the group's EMG recognizer [2], [3]; the Abstract's 'first time' holds only for the signal").
2. **M07 state of the art is outdated and internally inconsistent.** It names Moses 2021 [6] (25.6% median WER, 50 words) as the ECoG state of the art, while the M06 section cites Metzger 2023 [4] with 25% median WER on 1,024 words, which is clearly better. Replace [6] with [4] (and, if verified, its small-set result). The [5] half gives only "125,000-word vocabulary" with no metric; add "WER 2.5% (final 5 sessions)" or equivalent from c1, also in the M07 table row.
3. **M07 count population mismatch.** The body says the 1,162 studies are those "naming a vocabulary, language model or lexicon"; the Appendix inclusion rule for the same table is "a vocabulary of at least 1,000 words". One of the two descriptions is wrong. Also, 152 of 1,162 (13%) LLM rescoring is not the usual approach; for a 2015 lexicon component the anachronistic LLM-rescoring framing misleads. State the plurality design, or say plainly that no design dominates.
4. **M07 verdict "standard" vs "the weak point".** The Verdict calls the lexicon the weak point and contrasts it with the EMG prior's LM exclusion [2], but the slot verdict is `standard` with no explanation of why a design weaker than its own deciding prior is standard. Either justify `standard` (test-covering vocabularies were common in 2015, LM exclusion unknown rather than absent) in one sentence, or use the verdict the rules give for a component behind its prior. Note that LM leakage is "not stated", not shown; keep the hedge in the Verdict consistent with Question 2.
5. **Authors' own caveat presented as a finding (Outrun bullet 6).** The paper itself says the evaluations "have been performed offline" (t33). The bullet should say the authors acknowledge this and that the real-time claim is untested, or be dropped.
6. **Fig. 4 "contradiction" is not shown.** "Increases until approximately 150 ms" (t30) and "different models ... 100 ms after production" (t46) are compatible (a snapshot vs a peak). Remove the bullet unless the caption gives 100 ms as the peak.
7. **"WER beats it at all dictionary sizes" lacks a quote.** t25 has no dictionary-size condition. Add the Fig. 5 or §3.2 passage that states significance per dictionary size, or drop "at all dictionary sizes".
8. **"it matches the 10-word result" overstates.** "75% of all words are recognized correctly" is word correctness; WER also counts insertions. Write "is consistent with the 10-word result if insertions are negligible (inference)".
9. **Usual-approach lines for M12 name minority designs.** 21 of 145 (sentence-disjoint) and 45 of 132 (permutation) are minorities; the text should say "the most frequently named" or give the share, not imply a norm.
10. **Central confound only half-handled.** The review handles the closed-set vocabulary versus [4]. It does not mention the task difference (overt read speech by epilepsy patients vs attempted speech in paralysis [4], [5], [7]) or that [5] and [7] are intracortical. One clause in the Verdict would cover it.
11. **"Same group" wording (Verdict).** Jou et al. 2006 were at CMU/Karlsruhe and Schultz and Wand 2010 at Karlsruhe; the shared author is Schultz. "Of the senior author's group" is more precise. Unverified: whether the target cites either EMG work; if it does, the M06 point is context the authors gave, and the review should say so.
12. **State of the art beyond the cited works (unverified, for the writer to check).** For M06/M12, later intracortical text decoders and the public Brain-to-Text benchmarks built on [7]/[5] data (2024-2025) may report lower WER than 23.8% under held-out sentences; for ECoG, later Chang-lab work (for example bilingual decoding, 2024) exists. Not a required fix unless located.

## Chronology and fairness

[4], [5], [6], [7] are all labelled [later] and used only as state of the art, not as prior work or missed citations: correct. [2] (2006) and [3] (2010) predate the target: correct as priors.

## Absence and novelty claims

The review makes no "none of the N" or "first/only" claim of its own. The Appendix known-item recall of 0.33 for M06 and 0.0 for the null-model table is reported transparently.

## Verdicts

All slot verdicts are `standard` or `not applicable`; no `ahead` verdict needs checking. See finding 4 for M07.

## Scores

- Procedure: 7/10 (every target claim is quoted and located; comparators are quoted; Appendix counts are given; two population descriptions conflict and one SOTA lacks a metric).
- Final text: 6/10 (clear position and a well-argued lexicon critique, but one direct internal contradiction, an outdated ECoG state of the art, and two Outrun bullets that are either the authors' own caveat or not a real inconsistency).
