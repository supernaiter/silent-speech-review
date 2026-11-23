# Evaluation: SoniSpeech review

Date: 2026-11-23. Fallback evaluator (claim table only). Input: the compact review, its Verdict, its component sections and its claim table. No sources were reopened. Points marked "from memory" come from the evaluator's own knowledge and need checking against the source before anyone applies them.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper moves eyewear acoustic sensing from command sets to open-vocabulary sentences | Row 1, t1/t2 | correct | The quotes say "first large-scale, open-vocabulary" and "first open-vocabulary baseline ... 26.3% WER". |
| 2 | Closest earlier acoustic system used 54 sentences [2] | Row 2, c1 | correct (number); judgment questionable | The 54 sentences are in the quote. But 54 sentences is a closed set, so it is not evidence that open-vocabulary acoustic sensing is standard. The closest prior is also missing: EchoSpeech (Zhang et al., CHI 2023), FMCW echo profiles on eyewear with a command and digit set, by the same group (from memory). |
| 3 | Corpus matches earlier one-speaker silent corpora in size [3], [4] | Rows 2, 13, 14, c12/c8 | wrong (as framed) | The c12 quote says "utterances by a single speaker" and does not say silent. SSR7000 is an ultrasound-plus-audio corpus and is probably voiced (from memory). In hours, SoniSpeech's valid time is 26.7 h over 18,000 utterances, so roughly 13 h is silent (inference). That is far more than the 3.6 h of silent EMG in [4]. |
| 4 | Voiced-to-silent transfer was shown for silent EMG in 2020 [4] | Row 3/18, c11 | insufficient evidence | The c11 quote is cut off: "show that such a transfer causes a". No number or condition survives. |
| 5 | Without vocalized-only data, EMG silent WER rose to 71.6% [4] | Rows 3/17, c10 | correct (number); context missing | No baseline is given. The full model is about 68% WER (from memory), so the effect is about 3.6 points. [4] scores ASR run on synthesized audio, not direct recognition. "Shown in 2020" overstates the match with a 33.7% to 26.3% gain. |
| 6 | M12 behind: one speaker, held-out sessions, one run | Rows 4, 19, 21, 22, t63/t54 | correct (facts); verdict partly supported | The single speaker is quoted. Seeds are missing (absence; Table 3 gives single values). The pattern counts show 6 of 22 studies use random splits, which is weaker than holding out sessions. Only 7 of 22 hold out users, a plurality and not a majority. |
| 7 | 26.3% is a floor for this corpus, not evidence beyond this speaker | Row 5, t47/t63 | correct | |
| 8 | Abstract's 34 h is session time; valid utterances total 26.7 h | Row 24, t83/t5 | partly correct | The quote says "34 hours across 18,000 utterances" and does not mention sessions. Calling it "session time" is an inference. |
| 9 | Voiced-data gain called "significant" (§5.1) without a test | Row 25, t86 | no quote | The quoted sentence says "confirms" and does not contain "significant". |
| 10 | Baselines use 140 of 160 training sessions after a mic channel failure | Row 26, t38/t57/t8 | correct | 180 sessions per mode, with 1,000 of 9,000 sentences held out for test, leaves 160 for training. The noise hit the last 20 silent and 11 voiced sessions. |
| 11 | No WER on 242 unseen test word types | Row 27, t12 | correct | Absence claim. The count is quoted. |
| 12 | Robustness is cited from command-set work (§6), not measured | Row 28, t55 | insufficient evidence | t55 shows only the single quiet environment. No quote shows the citation of command-set work. |
| 13 | M05 usual approach: 28 studies, 16 Doppler, 12 FMCW/echo | Rows 6, 33, 34 | contradiction | The body says "28 unique studies (pattern match)". The Appendix row says "22 pattern match ... topic population 28". |
| 14 | [2] reached 8.4% WER on held-out users (2020) | Row 9, c1 | no quote | 8.4% is not in the quote. |
| 15 | [6] cross-user FMCW 14.22–19.05% WER over 41 words, after 10-word fine-tuning | Rows 9, 20, c3 | mismatch | The only quote gives "WER-w ... 4.56% to 8.96%". The 14.22–19.05% range, the 41 words and the 10-word fine-tuning appear in no quote. This number carries the M05 and M12 state-of-the-art lines and the summary table. |
| 16 | [5] tested on 5 speakers disjoint from 15 training speakers | Row 21, c4 | partly correct | "5 speakers" is quoted, but "15 training speakers" is not. [5] is voiced multimodal ASR (audio plus ultrasonic Doppler), not silent speech, so it is a weak yardstick for an SSI split. |
| 17 | [2] used leave-one-domain-out over users | Row 21, c2 | correct (loosely) | The quote says "different users and positions". |
| 18 | [7] lowered Gaddy benchmark WER from 28.8% to 12.2% | Row 11, c5 | correct | |
| 19 | [7] reached 22.2% with a 4-gram LM alone | Rows 11, 29, c6/c7 | insufficient evidence | The table row "MONA 9.1% 7.7% 8.9% 22.2%" has no column header, so neither the condition (silent EMG, 4-gram, no LLM) nor the column is shown. |
| 20 | 4-point gap to 22.2% mixes sensor and decoder | Row 12 | judgment incomplete | The gap also mixes speaker, corpus, vocabulary and test split. The two WERs come from different benchmarks. |
| 21 | SSR7000 has 7,484 utterances; 9,000 is about 1.2 times that | Rows 13, 14 | correct (arithmetic); count not quoted | 9,000 / 7,484 = 1.20. The number 7,484 is not in the c12 quote. |
| 22 | EMG corpus has 9,828 word types vs 5,356 here | Rows 13, 14, c9/t10 | correct | |
| 23 | Adding voiced data cuts silent WER from 33.7% to 26.3% (22% relative) | Row 17, t45/t47 | correct | 7.4 / 33.7 = 22.0%. |
| 24 | [8] lowers silent EMG WER from 26.75% to 25.14%, 10 seeds, p = 0.002; labelled [concurrent] | Row 16, c14/c15 | partly correct | 26.75%, the 6.0% relative reduction and the 10 seeds are quoted. 25.14% is consistent with them. p = 0.002 is not quoted. The [concurrent] label fits (Interspeech 2026 against an August 2026 preprint), and [8] is not treated as prior work. |
| 25 | M03 usual approach: paired audio "most frequent", 31 of 138 | Rows 15, 41 | insufficient evidence | No other category counts are given. The same "slot-filled 31" also appears for M02 in the summary table, which suggests a copied count. |

## Required fixes, by impact

1. **[6] numbers.** No quote gives 14.22–19.05% WER, 41 words or 10-word fine-tuning. The only quote gives WER-w of 4.56–8.96%. Find the source quote or replace the number in the M05 and M12 state-of-the-art lines and in the summary table.
2. **SSR7000 called "silent".** The quote does not say the utterances are silent, and the corpus is probably voiced ultrasound plus audio (from memory). Recheck. If voiced, rewrite the M11 comparison, the Verdict's "matches earlier one-speaker silent corpora" and the "large-scale holds for acoustic sensing only" bullet.
3. **Size comparison in hours.** SoniSpeech has about 13 h of valid silent speech (inference from 26.7 h over two modes). [4] has 3.6 h. Measured this way the corpus is larger than the one-speaker silent EMG corpus. State the hours, then decide whether M11 is still `standard`.
4. **M05 verdict contradicts itself.** The section calls 26.3% "the open-vocabulary reference for acoustic sensing in 2026" but rates the slot `standard`, citing a 54-sentence closed set. Either apply the `ahead` rules (Appendix count, deciding priors, effect repeated) or explain why open vocabulary on one speaker is not a step. Name EchoSpeech (CHI 2023, eyewear FMCW, same group) as the deciding prior from which the FMCW echo profiles come.
5. **[4] as precedent for M03/M04.** Give the full-model baseline beside 71.6% (about 68%, from memory, so a gain of about 3.6 points). Note that [4] scores ASR on synthesized audio. Replace the cut-off c11 quote with one that states the transfer result and its number. Soften "shown for silent EMG in 2020" to "the direction was shown".
6. **"Significant" (§5.1).** Quote the sentence that uses the word, or drop the bullet. t86 does not say it.
7. **[2] 8.4% WER on held-out users.** Add a quote that contains the number and the held-out condition.
8. **[7] 22.2%.** Quote the column header or the text giving the condition (silent EMG, 4-gram LM, no LLM rescoring). Add speaker, corpus and vocabulary to the list of things the 4-point gap mixes.
9. **Ledger count inconsistencies.** Reconcile M05 "28 unique studies (pattern match)" with the Appendix's "22 pattern match; population 28". Check the duplicated "slot-filled 31" for M02 and M03. Support "most frequent" with the other category counts or drop it.
10. **M12 `behind`.** Six of 22 studies use random splits, which are weaker than holding out sessions. Of the deciding priors, [5] is voiced multimodal ASR and [6] is a small vocabulary. Base the verdict on what is missing (a single speaker, no seeds and no validation split), not on the split type alone.
11. **[8] p = 0.002 and 25.14%.** Add the quote, or drop p.
12. **Robustness bullet.** Add the §6 quote that cites command-set work for walking, noise and other users.
13. **"34 hours is session time".** The quote says "34 hours across 18,000 utterances". Reword to "the abstract's 34 h against 26.7 h of valid utterance recordings" unless a quote ties 34 h to sessions.

## Scores

- Procedure: 6/10. Most numbers are traced. The quotes behind the [6], [2], [7] and [8] figures are cut off or missing, and two count totals disagree.
- Final text: 6/10. The position is clear and fair on chronology. The corpus-size framing and the M05 verdict rest on comparisons that the quoted evidence does not carry.
