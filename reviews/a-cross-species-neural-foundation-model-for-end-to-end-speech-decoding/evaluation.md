# Evaluation: A cross-species neural foundation model for end-to-end speech decoding

Date: 2026-11-20. Fallback evaluator (claim table only): the claim table, the Verdict and the component sections of the compact review. No sources were opened; "insufficient evidence" means the claim-table quote does not carry the claim as written.

## Claim check

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Cascaded single-model holdout WER 6.35% / 4.06% | Claim 2; Table 1, Table 2 | correct | Numbers match the quotes. |
| 2 | 6.35% / 4.06% is "below every other single-model entry" in Tables 1 and 2 | Claim 2 | insufficient evidence | Only the RNN baselines are quoted; other single-model rows (e.g. Li et al. single model, Feng et al.) are not. |
| 3 | "so M03 and M07 are standard" follows from the cascaded result | Verdict | wrong (logic) | A best-in-table cascaded WER does not imply a standard verdict; the verdicts rest on the usual-approach comparison, not on this result. |
| 4 | E2E single model 15.67% / 11.06% trails RNN baselines 9.76% / 6.67% | Claims 3, 15 | correct | Numbers are the target's Tables 1 and 2; [2] and [3] are attributions of the baselines, not the sources of the numbers. |
| 5 | Abstract's 24.69% to 10.22% pairs a 10-model LLM-merged ensemble with a single prior entry | Claims 4, 25 | partly correct | 10 seeds and 10.22% "+ Ensemble" quoted; the LLM merger and Feng et al. being a single model are not quoted. |
| 6 | 366.8 h human and monkey pretraining | Claim 6; Appendix O | correct | Abstract rounds to 367 h. |
| 7 | 39–45% lower WER for imagined speech vs training from scratch | Claim 8; Sec. 5.1 | correct | Quote matches. |
| 8 | Monkey data: validation PER 15.95% to 14.39% (T12), 7.61% to 7.12% (T15), one run each | Claim 9; Table 4 | partly correct | Numbers match; "validation PER" and "one run each" are not in the quote. |
| 9 | Range of cross-species gains 0.49–1.56 points | Claim 24; Table 4 | correct | 7.61-7.12 = 0.49; 15.95-14.39 = 1.56; other columns 1.55, 0.89 fall inside. |
| 10 | Table 9 tie, 12.67% vs 12.53%, human data equalized, T12 imagined | Claim 10 | partly correct | Numbers match; the condition (equalized human data, T12 imagined) is not in the quote. |
| 11 | Sec. 6 credits human data over cross-species | Claims 4, 9 | correct | Author-stated; attributed. |
| 12 | M03 state of the art: [4] pools three datasets, 8.7% E2E on the '25 competition split | Claim 7 | partly correct | Pooling and 8.7% quoted; the split is not named in the quote. A decoding WER is offered as the state of the art for a training component without the pooled-vs-single gain in [4]. |
| 13 | M06 usual approach: 97 studies (pattern match), 61 separate decode (slot-filled) | Claims 11, 37, 38 | wrong (inconsistent) | Appendix gives 61 of 96 slot-filled, 97 pattern match and 7,345 slot-filled; the denominators do not agree. |
| 14 | E2E path into an audio-LLM with neural-text contrastive alignment | Claim 12 | partly correct | Audio-LLM quoted; contrastive alignment not quoted. |
| 15 | Cascaded state of the art 2.5% online WER on 125,000 words (2024) [3] | Claims 13, 19 | partly correct | 2.5% (final 5 sessions, Copy Task) quoted; 125,000-word vocabulary not in quote. |
| 16 | [4] lists BIT at 11.1% | Claim 13 | correct | Consistent with the target's 11.06%. |
| 17 | Feng et al. [5] "trailed its own cascade (26.3% against 23.8%)" | Claim 14 | wrong | Per the quote, 23.8% is the hybrid result of previous research (Willett et al. [2]) that [5] calls "on par", not a cascade of [5]. |
| 18 | 24.69% to 15.67% is 37% relative | Claim 14 | correct | 9.02 / 24.69 = 36.5%; marked inference. |
| 19 | Ensemble 10.22% trails Li et al. ensemble 5.77% [6] | Claim 15 | correct | Ensemble vs ensemble; ensemble sizes not compared. |
| 20 | "The authors concede the gap (Sec. 4.2)" | Claim 16 | insufficient evidence | The quote concedes that prior E2E methods trail the cascade; it does not concede that BIT's own E2E trails. |
| 21 | Cascade = 5-gram plus a 6.7B rescoring LLM (Appendix D) | Claim 18 | partly correct | 5-gram quoted; the rescoring LLM and its size are not. |
| 22 | Headline ensembles: fine-tuned merger LLM over 10 models, a second merger LLM over 29; 1.76% is the 29-model figure | Claim 20 | partly correct | 10 and 29 seeds and 1.76% quoted; merger identities, fine-tuning and the 29-to-1.76% mapping are not. |
| 23 | M12 state of the art: 23.8% online, never-repeated sentences, 125,000 words (2023) [2] | Claim 22 | partly correct | 23.8% at 125,000 words quoted; "online" and "never-repeated" not. Also older and weaker than the 2.5% (2024) [3] used as state of the art elsewhere, without explanation. |
| 24 | Unlabeled holdout recordings can enter pretraining (Appendix A.4) | M12 section | insufficient evidence | No claim-table row or quote. |
| 25 | "Excluding the fine-tuning data" raises WER 6.35% to 7.24% and 4.06% to 4.36%, 14% / 7% relative | Claim 23; Table 8a | partly correct | Numbers and arithmetic correct (14.0%, 7.4%); the paragraph is about holdout recordings in pretraining, but the sentence says "fine-tuning data". What is excluded is unclear. |
| 26 | No ablation reports seeds or intervals | Claim 26 | insufficient evidence | The quote (30 models for hyperparameter tuning) is not evidence of absence and suggests seeds were used for tuning. |
| 27 | Imagined speech is a 50-word task, no chance baseline or test count | Claim 27 | correct | 50 words quoted; test-set split described without count. |
| 28 | E2E 0.95 s per sentence vs about 50 ms in [4] (outrun bullet; M13 row) | Claim 28 | wrong (unmatched units) | The quote for [4] gives "approximately 50ms inference time" with no per-sentence unit or hardware; the comparison is not like for like. |
| 29 | Component-table counts for M01, M02, M04, M05, M08–M11, M13 | Component table | insufficient evidence | No claim-table or Appendix tally rows. M05 "Utah arrays, 128/256 electrodes" also unquoted. |

## Central claim and position

- Strongest confound: task type (end-to-end vs cascade). The review compares the E2E model with cascades and labels M06 "behind the best comparable work", while the only prior E2E comparator ([5]) is beaten by 37% relative. The section text states both facts, but the verdict line merges them.
- Ensemble vs single model in the abstract: handled well (Verdict, outrun bullet).
- Leakage of holdout recordings into pretraining: handled, but the key sentence is ambiguous and its premise (Appendix A.4) has no quote.
- Fairness: [4] (concurrent, about four months after the target's first release) is labelled correctly and not treated as prior work, but it is used to fault the target on latency (outrun bullet) and as the end-to-end bar. The 0.95 s and bidirectional caveat is the authors' own (Sec. 6) and is attributed.
- No "first / only" or "none of the N" claims; no `ahead` verdicts. The one non-standard verdict (M06 `behind`) names comparators and repeats the effect.
- Unsupported position: "Hidden-label holdouts are stronger" (M12) has no citation.

## Required fixes (by impact)

1. M06: remove "trailed its own cascade (26.3% against 23.8%)". Per the quote, 23.8% is Willett et al.'s hybrid result, which [5] calls "on par".
2. M12: say exactly what Table 8a excludes (holdout recordings from pretraining, or fine-tuning data), and add a claim-table quote for Appendix A.4.
3. Drop or qualify the 0.95 s vs about 50 ms comparison (outrun bullet and M13 row). The units and hardware do not match, and the comparator is concurrent.
4. M06 verdict line: say "ahead of the prior end-to-end decoder [5], behind cascades on the same holdouts" instead of "behind the best comparable work".
5. M06 ledger counts: make the denominators agree (61 of 96 slot-filled vs 97 pattern match vs 7,345 slot-filled) in the section, the table and the Appendix.
6. Component table: add Appendix tally rows for the M01, M02, M04, M05, M08–M11 and M13 counts, or remove the counts. Quote the M05 sensor description.
7. Add quotes for unquoted specifics: the merger LLMs, fine-tuning and the 29-model-to-1.76% mapping (Appendix H); the rescoring LLM and its size (Appendix D); the contrastive alignment; Feng et al. as a single model; "every other single-model entry".
8. Add the stated conditions to the quotes, or drop them: the '25 competition split for 8.7% [4]; 125,000 words for 2.5% [3]; "online" and "never-repeated" for 23.8% [2]; "validation PER" and "one run each" (Table 4); "T12 imagined" and "human data equalized" (Table 9).
9. "The authors concede the gap (Sec. 4.2)": rephrase. The quote concedes that prior E2E methods trail the cascade, not that BIT does.
10. "No ablation reports seeds or intervals": cite the tables themselves. The tuning quote does not show absence.
11. M12 state of the art: explain why 23.8% (2023) [2] is used rather than 2.5% (2024) [3], or align with the other sections.
12. M03 state of the art: report the pooled-vs-single-dataset gain in [4], not only its end-to-end WER.
13. Verdict: drop the "so M03 and M07 are standard" inference from the cascaded result. Base those verdicts on the usual-approach comparison.
14. M12: cite evidence for "Hidden-label holdouts are stronger", or remove it.

## Scores

- Procedure: 6/10
- Final text: 6/10

The core numbers for the target and its main comparators match the quotes. The ensemble-vs-single and leakage critiques are well aimed.
