# Evaluation: Continuous Silent Speech Recognition using EEG

Date: 2026-11-20. Fallback evaluator, claim table only (no sources re-opened; outside knowledge used only for state-of-the-art and novelty checks, marked as such).

## Claim checks

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target claims feasibility of continuous silent speech recognition from EEG | Claim 1, t30 (Abstract) | correct | Quote matches. |
| 2 | Continuous CTC decoding was already applied to EEG by the authors in [2], "during speaking and listening" | Claims 1, 12, t55 (Sec. 1) | insufficient evidence | t55 credits target refs [1, 2, 3] jointly with isolated and continuous recognition while "speaking out loud". It says nothing about listening and does not say which of the three used continuous CTC. Review ref [2] (ICASSP 2019) is, to my knowledge, mainly isolated recognition. The continuous CTC work is more likely in the authors' other 2019 papers. |
| 3 | 83.34% WER on 72 test recordings, 30 sentences | Claim 2, t20 (Table 1) | correct | |
| 4 | Random 80/20 split; all 30 sentences in test, each repeated in training | Claims 2, 20, t3, t13, t58 | correct (inference) | 4 x 90 = 360 recordings, so the test set has 72. Each subject has 90 recordings of 30 sentences, three repeats each. With the random split, test sentences repeat in training. The inference is sound and could be stated plainly. |
| 5 | 4-gram LM "of unreported corpus" | Claims 2, 16, t12/t49 | insufficient evidence | The quote cites the target's ref [21] for the LM. The review does not say what [21] is, so it has not shown that the corpus is unreported. |
| 6 | Trial-length cue (encoder length = feature rate x length) | Claim 13, t57 | correct as inference | Labelled as inference in M06. The Verdict states it without that label. |
| 7 | Silent reading of on-screen sentences "in their mind" | Claims 5, 8, t1, t56 | correct | |
| 8 | "First" claim: 2 scalp-EEG pattern matches up to 2020, neither decodes sentences | Claim 7, Appendix | insufficient evidence | The two deciding prior works are not named. Outside knowledge: I know of no earlier scalp-EEG work that decodes continuous silent sentences, so the conclusion is plausible. |
| 9 | Authors attribute 84.08% (10 sentences) vs 74.86% (5 sentences) to the LM | Claims 17, 23, t22, t23, t15, t16 | wrong as framed | t22 says WER rises with vocabulary size except at 10 sentences, so the anomaly is 10 against the larger sets (for example 30 at 83.34%), not 10 against 5. The rise from 5 to 10 is the expected direction. t23's LM explanation applies to the anomaly. |
| 10 | Feasibility rests on WER 74.86% to 84.08% | Claim 22, t15, t16 | insufficient evidence | Only three Table 1 rows are quoted. The claim table does not show that no other row lies outside this range. |
| 11 | All sensors 83.34% vs frontal 85.04% vs temporal 86.73% | Claim 24, t20, t25, t24, t53 | partly supported | 85.04 is quoted, but 86.73 appears in no quote because t24 is cut off. No quote shows the "neuroanatomical reading" the review criticises. |
| 12 | Cross-subject 92.55%, "one held-out subject without its identity" | Claim 25, t28, t52 | wrong / insufficient | The quotes name the test subject as "the last subject or fourth subject", so the identity is given. 92.55 is not in either quote. |
| 13 | M04 usual approach: perception 784 of 1,477 | Claim 4 vs claims 28, 34 | contradiction | The Appendix gives 1,458 unique pattern-match studies for M04 and M06, while the text gives populations of 1,477 (M04) and 1,460 (M06). Reconcile or explain. |
| 14 | M06 usual approach: event-locked 310 vs CTC/async 63 | Claims 9, 34 | correct (ledger) | Plausible as the typical design. |
| 15 | M08 usual approach: phonemes, pattern match 63 | Table row M08 | insufficient evidence | No claim-table row covers it. 63 is the same count as the M06 CTC/async count, a possible copy error. |
| 16 | M07 usual approach: neural LM 169 vs n-gram 56 | Claims 14, 38 | correct (ledger) | Plausible today. For 2020 EEG work, n-gram or no LM was more typical, but the slot asks for today. |
| 17 | M12 usual approach: sentence-disjoint 21 of 145; none of 29 up to 2019 | Claims 18, 42 | correct (ledger) | |
| 18 | M04 SOTA: "real-time MEG decoding of typed sentences, 39% WER, 10 h per subject" [4] | Claim 6, c3 | partly supported | 39% WER is quoted. "Real-time", "typed" and "10 h per subject" are not. Comparing 10 h with "90 recordings" mixes units. Typing is a motor task, not a reading or perception task, so it is a weak state of the art for a silent-reading slot. |
| 19 | M06 SOTA: async encoder CER 0.59 to 0.25 with scale [4] | Claim 11, c4 | correct | |
| 20 | M07 SOTA: WER 0.39 (LLM) vs 0.43 (n-gram) vs 0.55 (none) [4] | Claim 15, c5 | partly supported | 0.43 and 0.55 are quoted. 0.39 comes from the audit, not from a quote. |
| 21 | Character CTC over 20 KPCA components of 155 features | Claim 10, t7, t9, t12 | partly supported | 155 and 20 are quoted. "Character" and "GRU-TCN" (component table) have no quote. |
| 22 | M12 SOTA: Willett et al. 2023, 23.8% WER on unseen sentences [5] | Claim 19, c6, c7 | correct but outdated | Outside knowledge: Card et al. 2024 (NEJM 391:609-618, intracortical, 125,000-word vocabulary) reports about 2.5% WER on held-out sentences. That result is later and much better, so it should be the state of the art or be added. |
| 23 | Makin et al. [3]: WER as low as 3% on held-out repeats, 30-50 sentences | Claims 3, 21, c1, c2 | correct, condition missing | "As low as 3%" is the best participant's figure, and the review drops that condition. The strongest confound, intracranial ECoG against scalp EEG, is named only by the word "ECoG", which is not enough. [concurrent] is a fair label: the Nature Neuroscience paper appeared in 2020, close to the target. |
| 24 | "Silent-reading EEG decoding of unseen sentences remains unshown" | Verdict | judgment too broad | It is unclear whether this refers to the target or to the field. If it refers to the field, it needs to address ZuCo-based EEG-to-text work (Wang and Ji, AAAI 2022) and the critique that such models do not beat noise inputs (Jo et al., 2024). Outside knowledge. |
| 25 | Chronology and fairness of [3], [4], [5] | References, labels | correct | No later work is treated as prior work or as a missed citation. The non-monotonic WER (an authors' own observation) is attributed to the authors. |

## Required fixes (ordered by impact)

1. M12 state of the art: replace or supplement Willett et al. 2023 (23.8%) with Card et al. 2024, NEJM, about 2.5% WER on held-out sentences with a 125,000-word vocabulary [later]. Update the component table.
2. M07 and "Where the claims outrun the evidence": correct the reading of t22/t23. The authors' exception concerns the 10-sentence row against larger vocabularies, not 10 against 5. Restate which comparison the LM explanation covers.
3. Verdict: give the Makin et al. comparison its conditions (best participant; intracranial ECoG against scalp EEG) so it reads as a point about the lenient protocol, not about modality performance.
4. Cross-subject bullet: drop "without its identity" (the paper names the fourth subject). Add a quote containing 92.55%, or remove the number.
5. Verdict: limit "remains unshown" to the target, or address the ZuCo EEG-to-text line of work and its noise-baseline critique.
6. M06 and Verdict: re-source the claim that [2] already decoded EEG continuously with CTC during speaking and listening. t55 supports only "speaking out loud" and credits three papers jointly. Cite the right prior paper or soften the claim.
7. Reconcile the population counts: 1,477 (M04) and 1,460 (M06) in the text against 1,458 in the Appendix.
8. M04 state of the art: support "real-time", "typed" and "10 h per subject" with a quote. Drop the 10 h against 90 recordings comparison or put both in the same unit. Justify a typing task as the state of the art for a silent-reading action, or choose a reading or perception decoder.
9. "First" claim: name the two deciding scalp-EEG pattern matches in the Appendix.
10. Add the missing quotes for 86.73% (temporal), 0.39 (LLM WER), the character-level CTC output, GRU-TCN, and the authors' neuroanatomical interpretation.
11. LM corpus: check what the target's ref [21] is before writing "corpus not given" and "unreported corpus".
12. M08: verify the count of 63 for phoneme output, which matches the M06 CTC/async count.
13. Label "Trained on the 30 prompts, it would reduce decoding to choosing among memorised sentences" as inference in the text, as is done in M06 and M12.

## Scores

- Procedure: 6/10. The claim table is mostly traceable, but several numbers lack quotes, two population counts disagree, and the deciding priors for "first" are not named.
- Final text: 6/10. The position on the repeated-sentence protocol and the LM confound is well founded. The M12 state of the art is outdated, the LM anomaly is misread, and one factual error remains (subject identity).

The core critique holds: test sentences repeat training sentences, there is no chance or LM-only baseline, and trial length is confounded with sentence identity.
