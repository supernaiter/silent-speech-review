# Evaluator: a language model separate from the writer

Date: 2026-11-24. Review evaluated: `compact.md` for VCVTS (Wang et al., arXiv:2202.09081, 2022).
Inputs: the evaluator brief, the compact review with its claim table, and greps of source text the writer stored (`prep/select/target.txt` target notes, `prep/read-cvf-prajwal20-lip2wav/text.txt`, `prep/read-arxiv-2105.09652-spkdisent/text.txt`). Mira et al. [8], Kefalas et al. [4], Choi et al. [3], TaLNet [2], V2SFlow [9] and Faces to Voices [5] were checked against claim-table quotes only, not against their full text.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | VCVTS changes M02 (VQCPC indices), M03 (VC trained on speech, reused), M06 (F0 predictor) | target notes lines 3, 8, 10, 16; claim row 1 | correct | |
| 2 | GL-vs-GL GRID MOS lead over Lip2Wav lies inside 95% intervals | target notes lines 32–37 (MOS "with 95% CI") | correct | Seen 3.46±0.12 vs 3.41±0.11; unseen 3.25±0.11 vs 3.13±0.12. The intervals overlap. MOS-SS behaves the same way. |
| 3 | No WER reported; intelligibility rests on STOI/ESTOI | target notes line 21 (five objective metrics, no WER) | correct | |
| 4 | Lip2Wav scores output with ASR | Lip2Wav text: Google ASR, GRID Table 2 WER 14.08%, LRW Table 7 WER 34.2% | correct, wrong setting cited | The 14.08% comes from Lip2Wav's speaker-specific GRID setting. The multi-speaker comparator is LRW Table 7 (34.2%). See finding 3. |
| 5 | XTS scores output with ASR and identity with an embedding-based error rate | XTS text: WER from a GRID ASR (2.8% on natural speech), EER for identity | correct, insufficient quote | The claim-table quote "12 yes dispel linear 35.5 12.7" is an ablation row. The main table rows (B 21.8, B-spk 17.8, SI 19.9 WER) carry the claim better. |
| 6 | "VCVTS says it follows both (§3.1)" | claim row 21; target notes line 20 | likely wrong | The only "following" text in the record is "both of which use GL following their papers", which concerns the vocoder, not evaluation. See finding 2. |
| 7 | Mira et al. WER 23.13% on unseen GRID, 42.51% on LRW | claim rows 21, 25 | insufficient quote | The quoted rows show the values, but the split quote ("all speakers ... 50-20-30 % split") does not show that this is the speaker-disjoint 33-speaker split. |
| 8 | M12 state of the art: Mira's model 16.05% WER in Kefalas Table VII | claim row 20 | insufficient evidence | This is a baseline row of [4], not [4]'s own best row. See finding 4. |
| 9 | Choi et al. 72.5 → 50.7 LRS3 WER, 30% relative | claim row 8 | correct | (72.5−50.7)/72.5 = 30.1%. "15 months later" (2022-02 → 2023-05) is right. |
| 10 | TaLNet 55.9 → 36.5 WER, 35% relative | claim row 11 | correct | 19.4/55.9 = 34.7%. |
| 11 | V2SFlow 28.5% WER, SECS 0.851 (A) / 0.664 (V) | claim rows 7, 17 | correct | |
| 12 | Faces to Voices 30.45% LRS3 WER | claim row 14 | insufficient quote | The column header is not in the quote. |
| 13 | F0-RMSE 43.16 (GL) vs 52.14 (PWG) vs Lip2Wav 49.33 | target notes lines 32–34 | correct | |
| 14 | "F0 gain credited to the predictor (§3.1)" | claim row 15; target notes line 26 | insufficient quote | The authors claim the best F0-RMSE. No quoted passage attributes it to the pitch predictor. |
| 15 | GRID MOS-SS 4.38 → 2.66 seen → unseen, "authors concede" | target notes lines 25, 33, 37 | correct | |
| 16 | "All three became common from 2023" | Appendix counts | wrong (overstated) | See finding 5. |
| 17 | F0 predictor: VCVTS earliest of the 9 ledger studies | Appendix M06 | insufficient evidence; earlier work known | See finding 6. |
| 18 | M12 "behind" verdict | M12 section, Appendix M12, Lip2Wav and XTS text | meets the rule, with gaps | See finding 1. |

## Findings

1. **M12 "behind" verdict: the rule is met, but the write-up is uneven.**
   - The rule needs three earlier comparable works in the same setting. The review names Lip2Wav (CVPR 2020) [6], XTS (arXiv 2021-05) [7] and Mira et al. (arXiv 2021-04) [8]. All predate VCVTS (2022-02), and all are video-to-speech on GRID and/or LRW with ASR WER on the output. I confirmed this for [6] and [7] from their text.
   - The best one, Mira et al. [8], is named and listed as read in full (Appendix M12).
   - The verdict rests on protocol (WER missing), not on scores. Two more earlier GRID WER works also support it: Vougioukas et al. 2019 (Interspeech, V2S GAN; WER 27.1 recomputed in the XTS table) and Lip2AudSpec (WER 32.5 in Lip2Wav Table 2).
   - Weaknesses:
     - (a) The yardstick paragraph quotes Mira's WER values (23.13%, 42.51%). These are results and add nothing to a protocol judgment, so a reader may take the verdict as results-based. Drop them or mark them as context.
     - (b) The usual-approach line says listener tests (83 of 165) are the most common protocol and ASR WER the least (38). VCVTS has a 20-listener MOS. The review never reconciles "behind" with VCVTS matching the most common protocol. Add one clause: within the earlier GRID/LRW multi-speaker subset, WER was the norm (all three named works).
     - (c) The M12 state-of-the-art line is a result (a WER), not a protocol. For an evaluation slot it should name the best protocol, for example speaker-disjoint split, ASR WER with stated real-audio WER, and an embedding speaker score.
   - Net: the verdict stands. Fix (a)–(c).

2. **"VCVTS says it follows both (§3.1)" is probably a misattribution.**
   - The only "following" passage in the record is about Griffin-Lim: "both of which use GL following their papers".
   - Read this way, the sentence implies VCVTS claimed to adopt the baselines' evaluation protocol, which then makes the missing WER look like a self-contradiction.
   - Fix: quote the exact §3.1 passage, or change the sentence to "VCVTS reuses both as baselines and follows them on the vocoder (§3)".

3. **Lip2Wav's WER is cited from the wrong setting.**
   - The 14.08% GRID WER (Lip2Wav Table 2) is speaker-specific: one model per speaker, on an "unseen test split" of utterances.
   - The multi-speaker comparator that matches VCVTS is Lip2Wav's LRW result, 34.2% WER with Google ASR (Table 7).
   - The protocol point holds either way, but the claim table should cite Table 7 for the "same setting" condition.

4. **The M12 state-of-the-art value is a baseline row, not the best row.**
   - 16.05% is Mira et al.'s model as re-run in Kefalas et al. Table VII. [4]'s own model in that table is presumably the best row (unverified).
   - Either give [4]'s own row with its value, or restate the line as a protocol (see finding 1c).
   - Also, the VCVTS unseen split (s1, s2, s4, s29 held out; 29 training speakers) is not the 33-speaker split of [4] and [8]. The review leaves this implicit. One phrase would prevent a reader from comparing numbers across splits.

5. **"All three became common from 2023" in the Verdict is stronger than the Appendix counts.**
   - Pitch or energy predictors: 9 of 165 video-to-speech studies.
   - Audio-only decoder pre-training: 4 of 30.
   - Only unit targets, with discrete-unit wording in 27 of 54 (and SSL-unit conditioning in 44 of 165), support "common".
   - Fix: "unit targets became common from 2023; audio-pretrained decoders and pitch predictors recur ([3], [4], [5])".

6. **The "earliest F0 predictor" claim needs a qualifier.**
   - The Verdict says the F0 predictor reaches video-to-speech "here earlier than in any other ledger study", and M06 says "VCVTS the earliest of the 9".
   - Michelsanti et al., "Vocoder-Based Speech Synthesis from Silent Videos" (Interspeech 2020, arXiv:2004.02541), estimates F0, together with spectral envelope and aperiodicity for a WORLD vocoder, directly from silent video. That is earlier explicit F0 prediction in video-to-speech (confidence medium on whether the ledger counts it as a "pitch predictor").
   - The Appendix M06 entry also does not say whether VCVTS was added to the 165 or matched by the pattern. M02 and M03 state "VCVTS added"; M06 does not.
   - Fix: name the deciding priors checked, and either restrict the claim to "a separate pitch-predictor module feeding the decoder" or cite Michelsanti 2020 as the earlier F0-from-video design.

7. **M06 confound sentence: the authors' attribution is not quoted.**
   - The point that F0-RMSE is better with GL (43.16) and worse with PWG (52.14) than Lip2Wav (49.33) is correct and useful.
   - "F0 gain credited to the predictor (§3.1)" has no quote showing the authors credit the predictor. They claim best F0-RMSE (target notes line 26).
   - Fix: quote the attribution, or write "the F0-RMSE lead is vocoder-dependent".

8. **The component table labels disagree with the section headings.**
   - The M07 row is "Lexicon and LM", but the section and content are use-time speaker information.
   - The M02 row's usual approach, "Paired-audio targets (slot-filled 11)", does not match the M02 text (27 of 54 discrete units, pattern match).
   - The Appendix gives that 11 as "11 of 22 (slot-filled, M03)" inside the M02 entry, while the ledger line says 31 slot-filled for M02.
   - Fix: align the labels and give one source for each count.

9. **The M03 usual-approach sentence is ambiguous.**
   - "9 use only an off-the-shelf vocoder and 4 pre-train a decoder on audio, all 2023 or later" reads as if all 13 are 2023 or later.
   - The Appendix ties "all 2023 or later" to the 4 only, and also lists "TTS decoder transfer 2", which includes TaLNet (2021).
   - Fix: attach the date to the 4, and mention the 2 TTS-transfer studies, since TaLNet decides the verdict.

10. **One question for the authors is partly answered in the paper.**
    - "How many test utterances and runs underlie Table 1?" The MOS part is stated: 60 utterances, 15 per GRID test speaker, 20 listeners (target notes line 22).
    - Fix: narrow the question to the objective-metric test counts and the number of runs.

11. **XTS quote (claim row 21).** The quoted row "12 yes dispel linear 35.5 12.7" is an ablation row with unclear columns. Replace it with the main-table row and the ASR sentence ("around 2.8% WER on the natural speech samples"). This is an insufficient quote, not a wrong claim.

12. **Minor: the "open vocabulary" bullet is fair but one-sided.** The authors do report that VCVTS (GL and PWG) beats Lip2Wav on LRW (target notes line 27). The bullet could note that the LRW lead also lacks WER, which ties it to M12 instead of standing alone.

## Required fixes, ordered by impact

1. Remove or correct "VCVTS says it follows both (§3.1)" (finding 2).
2. Tone down "all three became common from 2023" (finding 5).
3. Qualify the "earliest F0 predictor" claim and address Michelsanti et al. 2020 (finding 6).
4. M12: remove the result values from the yardstick, reconcile with the listener-test majority, and make the state-of-the-art line a protocol or [4]'s own best row, with the split difference noted (findings 1, 4).
5. Cite Lip2Wav LRW Table 7 for the multi-speaker WER comparator (finding 3).
6. Quote or drop the "credited to the predictor" attribution (finding 7).
7. Fix the table labels and count sources for M02 and M07, and the date scope in the M03 sentence (findings 8, 9).
8. Narrow the test-count question, and replace the XTS quote (findings 10, 11).

## Scores

- Procedure: 7/10. The comparators were read, the arithmetic is right, the CI-overlap check is correct, and the M12 rule is satisfied. Weak points are some quote–claim mismatches and the novelty claims without named deciding priors.
- Final text: 7/10. The position is clear and mostly backed. One likely misattribution and two overstatements in the Verdict need fixing.

The strongest parts: the GL-vs-GL confidence-interval reading, the vocoder confound on F0-RMSE, and the decision to rate M02, M03 and M06 standard for lack of ablation, with TaLNet named as the deciding prior.
