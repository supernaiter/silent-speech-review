# Evaluation (fallback, claim table only)

Date: 2026-11-14. Evaluator: fallback path. ChatGPT unavailable (owner logged out): chatgpt_pending. The free-model evaluator (two runs, the second with a compact input) returned no output before its timeout; this pass was made by the writer over `claims.md` and the Verdict and component positions only, with no new source reading except one passage check (Moses et al. 2021, 60.5% WER quote).

| No | Claim (first words) | Entry | Result | Note |
|---|---|---|---|---|
| 1 | The paper changed the sensor | t1, t32, t62 | match | 253 electrodes; CTC GRU; avatar output. |
| 2 | M05 and M06 are standard, and the text result is behind the [concurrent] | s3, t45 | match / wording | 23.8% at 125,000 vs 25.5% at 1,024; ratio 122 (inference) correct. "behind" is a verdict term that the rules reserve for earlier work; a [concurrent] system cannot make a slot "behind". |
| 3 | M08 is the real departure | t55, t70 | match | 54.4% perceptual WER, 1,024-word set; real-time avatar from decoded audio. |
| 5 | State of the art: 2.5% online WER | s1, s3 | match | |
| 6 | 25.5% at 1,024 words matches the error | t45, t25 | match | log10(122) = 2.09. |
| 7 | density benefit rests on an offline low-density simulation | t120 | match | |
| 10 | tenfold lower error | s1, t45 | match | 25.5 / 2.5 = 10.2. |
| 12 | 5-gram LM trained on the full 18,284-sentence pool | t38, t22, t119 | match | Test sentences drawn from the 1024-word-General set, itself drawn from the 18,284 pool. |
| 13 | 25.6% on 50 words, 60.5% without the LM | p1, p2 | insufficient quote | p2 quote lacked 60.5; source passage confirms "60.5% ... without language modeling". |
| 14 | 18.5% to 29.4%, 59% relative | t46, t39 | match | 10.9 / 18.5 = 0.589. |
| 15 | listener WER 31% (25-word pool) and 53% (50-word pool) | a4, a5 | match | |
| 17 | 43.75% median listener WER; 10.7 points worse | w2, t55 | match / condition | Wairagkar et al. used attempted vocalized speech; the review names only "different sentences". |
| 19 | six-way closed set; 74.3% at 50% chance | w3, t63, t100 | match | Chance 50% follows from the two-alternative design. |
| 20 | 5.21 dB inside 5.14–6.58 dB | t53, a3, t12 | match | Reference-voice difference stated. |
| 21 | personalised voice MCDs higher | t59, t60 | match | |
| 22 | avatar animation from decoded audio | t70 | match | |
| 23 | 78.3 WPM vs 14.2 WPM | t48, t7, t106 | match | |
| 24 | 9,655 vs 13,463; 256 vs 253 | t26, t25, t79 | match | |

Positions beyond evidence:
- Verdict sentence 2 uses "behind" for a comparison with a [concurrent] work; the slot verdicts are standard. Wording should not suggest a verdict the rules do not give.
- M08 state of the art: the 10.7-point gap compares silent attempts with vocalized attempts; the condition should be named.
- M07: "the WER understates error on sentences outside the pool" is marked (inference) and rests on t38/t119/t39; acceptable as inference.

Required fixes (by impact):
1. Replace "behind" in the Verdict with a non-verdict word.
2. Name the vocalized condition of the [later] synthesis comparator.
3. Extend the p2 quote so that 60.5% is in the quoted text.

Scores: procedure 7/10 (ChatGPT check pending), final text 8/10.
