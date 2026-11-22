# Independent evaluation: iPhoneme (arXiv:2604.16441)

Date: 2026-11-22. Fallback evaluator (claim table only). Input: the review's Verdict, component sections, component table, "Where the claims outrun the evidence", references and claim table. No source was re-opened; judgments rest on the quotes and locations in the claim table and on general knowledge of the field, marked where they go beyond the table.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | iPhoneme WER 26.61% | Row 1, t34 (target Abstract) | correct | "73.39% word accuracy (26.61% WER)". |
| 2 | Card et al. 2.5% online WER, same participant, 125,000-word vocabulary | Rows 1, 7, 13, f1 | correct | Quote gives 2.5% (95% CI 2.0–3.1) for the Copy Task in the final 5 sessions. The condition (final sessions only, online, continually updated decoder) is not attached in the Verdict; see the confound below. |
| 3 | Willett et al. 23.8% online WER | Rows 1, 10, 17, f5, f6 | correct | 125,000-word, vocal; sentences never in training (f6). |
| 4 | Metzger et al. 25% online WER | Rows 1, 10, f8 | correct, condition missing | 25% median WER is for a 1,024-word vocabulary with ECoG; the review sets it beside 125,000-word results without that condition. |
| 5 | "Card et al. (89%)" matches no figure in Card et al. | Rows 2, 3, 20, t40, t37, f2, f3 | insufficient evidence | f2/f3 show 90.2% and 97.5%; they do not show that 89% appears nowhere (supplement, per-session figures). The absence is asserted from two abstract quotes. |
| 6 | The 3-point gain sets phoneme accuracy against Card's figure | Rows 2, 3, 9, t40, t31 | correct by inference | 92.14 (Table IV, phoneme) − 89 = 3. The claim row for the Verdict does not cite t31; the link is left to the reader. |
| 7 | Validation errors shape the LM; 150 decoder configurations searched | Row 4, t75, t23 | correct | Both quotes support it. |
| 8 | M07 change is "standard" | Rows 5, 12, component table | wrong (internal) | The section itself says iPhoneme uses a lexicon-free phoneme 6-gram and an LLM phoneme-to-word encoder, while the usual design is LLM rescoring over a word n-gram. That is a departure, not the usual design; the verdict contradicts its own text. |
| 9 | M06 usual approach: 61 of 96 with a design value run a separate decode step | Row 6, Appendix | insufficient evidence | Mixes bases: "97 pattern-match unique studies" then "61 of the 96 ... (slot-filled)". Which ledger tier the 96 comes from is unclear. |
| 10 | 26.61% is about 10.6 times Card's 2.5% | Row 7 | correct arithmetic | 26.61 / 2.5 = 10.64. It is a calculation, not an inference; the label is wrong, and the two numbers come from different conditions. |
| 11 | B2T 2025 holdout: RNN baseline 6.67%, BIT 4.06% | Row 8, f10, f11 | correct per quote | [5] is about 5 months before the target; [concurrent] is right. Whether 4.06% is the best holdout result for these data (competition leaderboard, later work) is not shown. |
| 12 | 7.86% PER not comparable with Willett's 19.7% online PER | Row 9, t31, f5 | correct, quote ambiguous | f5 does not label the 19.7 column as PER; plausible from Willett et al. Table 1, but the quote should show the column. |
| 13 | Table II ~25M vs §V 192.9M parameters | Row 11, t77, t12 | correct | Clear internal inconsistency in the target. |
| 14 | M07 usual approach: LLM rescoring is most common (152 of 1,162) | Rows 12, 36, 37 | insufficient evidence | 152 of 1,162 is 13%; no count is given for word n-gram decoding, which is the more plausible typical design. "Most common" is not shown. |
| 15 | LM choice moved Willett from 23.8% to 17.4% offline | Row 14, f7 | correct | Supported by f7. |
| 16 | M07 state of the art = 2.5% WER [2] | Row 13 | judgment beyond evidence | A system WER does not isolate the LM. The LM-specific evidence is the 23.8 → 17.4 effect and Card's LM configuration. |
| 17 | M12 usual approach: 21 sentence-disjoint, 10 repeated sentences of 145 | Rows 16, 40, 41 | insufficient evidence | The line states no usual design; 21 + 10 of 145 means most name neither. The 6,960 slot-filled figure and the 145 base are not reconciled. |
| 18 | Split: 7,050 + 1,021 = 8,071, plus 13.2% unlabeled test | Row 18, t6, t7, t3, t8 | correct | The target is inconsistent: 7,050 / 8,071 = 87.3%, not the stated 73.7%. The review hints at this but could state it plainly. "Scores come from trials used for tuning" is a fair, labeled inference. |
| 19 | Validation accuracy ~80.8% on 2025 sessions | Row 19, t58 | correct | Supported. |
| 20 | "Highest reported performance on T15" contradicted | Row 20, t36, f1 | correct, weaker comparator chosen | The like-for-like contradiction is the 6.67% baseline on the same recordings [5]; the online 2.5% carries a condition gap. |
| 21 | Target calls T15 "intact speech motor cortex" and ECoG; Card: ALS, severe dysarthria, four microelectrode arrays | Row 21, t4, t74, f4 | partly wrong | ECoG vs four Utah arrays is a real error. "Intact speech motor cortex" is not contradicted by ALS with dysarthria. The target's own abstract says "intracranial EEG" and "256-channel" (t3), an additional internal inconsistency the review misses. |
| 22 | 180 ms CPU claim ignores the bidirectional GRU's 100–200 ms | Row 22, t56, t57 | insufficient evidence | t57 does not show that the 100–200 ms is attributed to the bidirectional GRU. Table IV attaches 180 ms to the WFST beam stage (t31), so its scope is unclear. |
| 23 | 3–10× faster than dwell, no user study | Row 23, t49 | correct | The quote supports the claim; the absence of a study is plausible. |
| 24 | Reference details [2]–[4] | References | correct | NEJM 2024;391(7):609–618; Nature 620:1031–1036; Nature 620:1037–1046; DOIs are consistent with these. |
| 25 | M09 "untested" (Verdict) vs "not reported" (table); M13 "not reported" while 180 ms is claimed | Verdict, component table | wrong (internal) | Labels differ for the same component. M13 is claimed without support rather than unreported. |

## Central claim and strongest confound

The central position is that iPhoneme is behind and its "highest on T15" claim fails. The strongest confound is the starting point and the evaluation condition. Card's 2.5% is online, from the final five sessions, with a decoder updated through use. iPhoneme reports an offline score on an unnamed, tuned split that includes 2025 sessions where accuracy drops to ~80.8%. The review notes that the split is unnamed but still leads with the 2.5% and the 10.6× ratio. The position holds on like-for-like evidence: the 6.67% RNN baseline on the B2T 2025 holdout of the same recordings is far below 26.61%. The review should lead with that evidence and mark the online figures as a different condition. Fairness: [5] is correctly labeled [concurrent] and is not counted as a missed citation. The review does not present the authors' own caveat about 2025 sessions as its own finding; it cites §X. No "first / only" or "none of N" claims appear.

## Required fixes (by impact)

1. M07 verdict: "standard" contradicts the section's own description. A lexicon-free phoneme 6-gram with an LLM phoneme-to-word step differs from word n-gram plus LLM rescoring. Change the verdict, or justify it.
2. Lead the "behind" case with the same-data comparator: the 6.67% B2T 2025 baseline [5] on the same recordings. State that Card's 2.5% is online, from the final sessions, under a different condition, and attach the 1,024-word vocabulary and ECoG condition to Metzger's 25%.
3. Participant description: drop "intact speech motor cortex" as an error, since ALS with dysarthria does not contradict it. Keep ECoG vs microelectrode arrays, and add the target's internal "intracranial EEG" wording (t3).
4. "89% matches no figure in Card et al.": either cite a full-text check (including the supplement) or soften the wording to the figures checked. In the Verdict claim row, cite the target's 92.14% phoneme accuracy (t31).
5. M07 usual approach: 152 of 1,162 (13%) does not show that LLM rescoring is "most common". Give the competing count (word n-gram), or reword.
6. M12 and M06 usual-approach lines: name the usual design for M12 (most of the 145 name neither split type), and reconcile the 6,960 slot-filled with the 145 pattern-match base. In M06, state which tier the 61 of 96 comes from.
7. Split: state plainly that the target's percentages and counts disagree (7,050 / 8,071 = 87.3%, stated 73.7%; 8,071 is called the total, yet a 13.2% test share is added).
8. Latency point: quote the passage that ties the 100–200 ms to the bidirectional GRU, and note that Table IV ties 180 ms to the WFST stage. Otherwise, weaken the claim.
9. Align the labels: M09 is "untested" in the Verdict and "not reported" in the table. M13 is claimed without evidence, not "not reported".
10. M07 state of the art: replace the system-level 2.5% with LM-specific evidence, such as the 23.8 → 17.4% LM effect [3] or Card's LM configuration.
11. Relabel "about 10.6 times that error (inference)" as a calculation across different conditions.
12. State of the art on the B2T 2025 holdout: check whether any result beats BIT's 4.06% (competition leaderboard or later papers) before calling it the best on these data.

## Scores

- Procedure: 7/10. The claim table is complete, the quotes are located and the chronology is labeled, but several ledger bases are muddled and some absence claims rest on abstract quotes.
- Final text: 6/10. The main conclusion holds, but the M07 verdict contradicts its own section, the lead comparator mixes conditions, and one "error" in the target is not an error.

The review correctly catches the 25M vs 192.9M parameter inconsistency, the ECoG mislabel, the tuning on validation errors and the unsupported 89% comparator.
