# Evaluation

Date: 2026-11-14. Evaluator: fallback pass over the claim table, the Verdict and the component positions (no tools, no source re-reading). ChatGPT evaluation: chatgpt_pending.

## Findings

1. M06 State of the art set the 2024 50-word accuracy (99.6%, real-time sentences) beside the paper's offline isolated-word accuracy (47.1%); the conditions differ (offline isolated words without a language model against real-time sentence decoding).
2. Verdict: "the drop from 60.5% to 25.6% WER measures a closed-world prior" goes beyond t31 if read as "the language model adds nothing"; the supporting entries (t21, t47) show only that the model was trained on sentences limited to the 50 words.
3. Stability claim: the review says the no-recalibration claim rests on offline isolated-word analysis; t32 points to Fig. S10 in the supplement, so the basis needs confirmation.
4. Claim 7 and claim 11 ratios (44-fold, 58% relative, five times, about 20 times) are reviewer calculations; all are marked "(inference)" and follow from t16/s1, t9, p4 and s4.
5. M07 calls the 2023 ECoG result "the same error" (25.5% against 25.6%); this holds as a comparison of medians but the participants and sensors differ.
6. Claim 18 (recalibration requested three times) matches s3.
7. Claims 9, 10, 14 match s2, s4, p3, p4, s5.
