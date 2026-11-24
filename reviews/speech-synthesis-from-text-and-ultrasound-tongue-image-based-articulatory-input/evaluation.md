# Evaluator: a language model separate from the writer

Date: 2026-11-24. Input: `compact.md` (review plus claim table). Target text consulted only through the prepared target passages (`prep/select/target.txt`, `prep/notes.merged.json`) to check table headers, column order and quotes the claim table truncates. No web sources opened; outside-knowledge items are marked "unverified".

Column order confirmed from the target notes: Tables 1 to 5 give development/test per system, in the order ult2wav, txt2wav, txt+ult2wav. All arithmetic below uses the test column unless stated.

## Claim check table

| No | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | 128 PCA coefficients next to linguistic features (Verdict) | claim 1, t7, t2 | correct | "Merlin" not in the quote, but target notes (Sec. 2.3) confirm Merlin recipe. |
| 2 | Test MCD falls for all 8 speakers by 0.015 to 0.229 dB, about 2% on average (Verdict) | Table 1 rows t35 to t42 | correct | Gains 0.071, 0.061, 0.210, 0.229, 0.080, 0.211, 0.015, 0.127; mean relative 2.2% (inference). |
| 3 | "one run per speaker" (Verdict) | t34 | insufficient evidence | t34 gives epochs and learning rate, not run count; the review itself asks "How many runs and which seeds" in Questions. Stated as fact in the Verdict, asked as an open question later. |
| 4 | "roughly 10 test sentences" (Verdict) | t5 (truncated), target notes Sec. 2.1 | correct (inference) | 5% of ~200 = ~10; target notes confirm 85/10/5 and that exact counts are not given. The t5 quote stops before the split; extend it. |
| 5 | Test BAP error rises for 6 of 8 speakers (Verdict, Where-claims) | Table 2 rows t43 to t50 | correct | Rises for 01fi, 02fe, 03mn, 04me, 06fe, 07me; falls for 05ms, 09fe. Rises are 0.001 to 0.014, i.e. smaller than or similar to the MCD gains the review calls a fall. |
| 6 | Test voicing error rises for all 8 speakers (Verdict, Where-claims) | Table 5 rows t67 to t74 | correct | All 8 rise (e.g. 03mn 6.828 to 7.674). |
| 7 | "so the excitation claim fails" (Verdict); "the gain is shown for the spectrum only" (M06) | Table 4 (F0-CORR) in target notes; t24 full sentence | wrong | Authors claim usefulness for "spectral and BAP prediction, and in some of the F0 measures". Test F0-CORR rises for 6 of 8 speakers with the combined input, strongly for 04me (0.423 to 0.745) and 05ms (0.560 to 0.734) (Table 4; inference). The review never mentions Table 4 and truncates t24 before "some of the F0 measures". |
| 8 | Holds for BAP "only on the development set" (Where-claims) | Table 2 dev columns | partly wrong | Dev BAP also rises for 06fe (0.373 to 0.386) and 07me (0.437 to 0.454); dev holds for 6 of 8, not all. |
| 9 | Authors say ultrasound "did not help" voicing; test error "in fact rises" (Where-claims) | t23, target notes Sec. 3 | insufficient quote / framing | t23 quotes "very poorly from ultrasound-only input", not "did not help". Authors do concede no voicing benefit, so a rise is consistent with their statement rather than a contradiction; "in fact" overstates the gap. |
| 10 | Naturalness claimed without listening test (Verdict, M12) | t92 | correct | Authors hedge: "may increase the naturalness". The Verdict's "Naturalness is claimed" drops the hedge; M12 quotes it correctly. |
| 11 | Authors concede the system is ruled out for TTS or silent-speech use (Verdict) | t29, target notes Sec. 5 | wrong attribution | Sec. 5 says only "both text and articulatory input are required" and lists speaker-independent training as future work. "Rules out TTS or silent-speech use" is the reviewer's inference, presented as the authors' concession. |
| 12 | Text-only test MCD 5.447 to 6.566 dB; ultrasound-only 7.050 to 8.396 dB (M06) | Table 1 | correct | Ranges match the test columns. |
| 13 | 6 x 1,024 MLP, WORLD features at 5 ms (M06) | t10, t9 | correct | |
| 14 | Single resampled frame enters (M06) | t8 + repository lines | correct (insufficient quote) | t8 shows resampling to 200 Hz, not that only one frame is used; the single-frame part rests on the uncited script lines. |
| 15 | Cao et al. used EMA as training targets or via a separate articulatory-to-acoustic network (M06) | t95 | insufficient quote | t95 says only "proposed a solution to integrate EMA-based articulatory data to DNN-TTS". The claim that feeding measured test-utterance articulation is "this paper's choice" (novel) rests on an unquoted reading of Cao et al. and Ling et al.; whether Ling et al. (HMM-TTS) used natural articulatory features at synthesis is unverified. |
| 16 | 2017 DNN took 5 images [2]; 3D CNN ~21% lower test MSE [5] (M06) | claim 10 | correct, condition missing | 21% is relative to a 2D CNN baseline in [5]; the review does not name the baseline. |
| 17 | Midsagittal Micro at 81.5 fps (M05) | t4 (truncated), target notes | correct | 81.5 fps is in the target notes, not in t4 as quoted. |
| 18 | Group's earlier data at 81.67 fps [6] (M05) | c17 | insufficient quote | c17 is about subjects and sentence counts; no frame rate quoted. |
| 19 | 2020 misalignment measure tied to no recognition or synthesis outcome [7] (M05) | c24 (truncated), c21 | insufficient quote | c24 is cut at "indicate corr..."; nothing quoted shows the absence of an outcome link. |
| 20 | 04me, flagged misaligned, has largest gain, so the gain "does not follow" misalignment (M05) | Table 1, t27 | wrong as an inference | 04me does have the largest gain (0.229). But the four flagged speakers (01fi, 04me, 05ms, 07me) average 0.099 dB gain, the four others (02fe, 03mn, 06fe, 09fe) 0.152 dB (inference); 07me, also flagged, has the smallest gain. One speaker is cherry-picked, and the authors' Fig. 2 claim concerns MCD level, not gain. |
| 21 | Usual approach M06: 37 DNN, 31 CNN of 51 (M06) | Appendix | correct (ledger) | Population is ultrasound-only-to-speech, not text+articulation TTS; see fix 6. |
| 22 | State of the art: Tongue2Speech 15.93% WER TaL1 (M06), 31.64% WER TaL80 (M12) [4] [later] | ledger note | unverified | Labelled [later] correctly and not treated as prior work. It solves a different task (no text input), so it is not the state of the art for text+ultrasound TTS. |
| 23 | Usual approach M12: 21 MCD, 14 MUSHRA (M12) | Appendix | correct; table cell wrong | Component table writes "MCD with MUSHRA (pattern match 21)", which reads as 21 studies with both; 21 is MCD alone. |
| 24 | Listening tests with 23 (2017), 24 (2018), 23 (2019), 22 (2020) listeners (M12) | claim 21 | insufficient quote | Only ledger notes are given; c20 (2019) quotes a MUSHRA result but not the listener count; no quote for 22 (2020) or 24 (2018). |
| 25 | Durations not modelled, so all systems use reference timing (Where-claims) | t14; target notes "compared without temporal warping" | correct (inference) | See fix 3: this undercuts the review's own timing-leak argument. |

## Required fixes, ordered by impact

1. **Excitation verdict omits F0-CORR (Table 4).** The Verdict ("the excitation claim fails") and M06 ("the gain is shown for the spectrum only") ignore the one excitation metric where the combined input clearly helps: test F0-CORR rises for 6 of 8 speakers, by 0.32 for 04me and 0.17 for 05ms (Table 4; inference). The authors' sentence t24 ends "and in some of the F0 measures"; the claim table truncates it. Restate: BAP gains do not hold on test, voicing is worse, F0-CORR mostly improves.
2. **Concession attributed to the authors that they do not make.** Sec. 5 says only that both text and articulatory input are required. "Which the authors concede rules out TTS or silent-speech use" must become the reviewer's own inference, marked as such.
3. **Leakage argument inconsistent with the duration point.** The review argues the ultrasound "carries its articulation and timing" of the reference utterance, then states that all systems use reference timing because durations are not modelled. If text-only also gets reference timing (and features are compared without temporal warping), timing is not an advantage of the combined input; the remaining leak is within-frame articulation only. Reconcile the two bullets and narrow the confound to what is actually left.
4. **Misalignment inference cherry-picks one speaker.** "The combined-system gain does not follow it" rests on 04me; the flagged group averages a smaller gain (0.099 vs 0.152 dB; inference), and 07me (flagged) has the smallest. Either drop the sentence or report the group means and note that n = 4 per group decides nothing.
5. **Inconsistent standard on small differences.** MCD drops of 0.015 to 0.080 dB count as a fall, while BAP rises of 0.001 to 0.007 (03mn, 04me, 06fe) count as the claim failing. With one model per speaker and ~10 test sentences, neither direction is resolved; say so once and apply it both ways.
6. **Usual approach and state of the art for M06 use the wrong population.** The 51-study ledger and Tongue2Speech are ultrasound-only-to-speech (no text). The target is articulatory-informed TTS; its usual design is linguistic-feature DNN/HMM TTS with EMA (Ling et al., Cao et al., which the paper itself cites). Add that comparison, or state explicitly that the field tally is a proxy. Tongue2Speech is not the state of the art for a text+ultrasound system (no common task).
7. **"One run per speaker" stated as fact** in the Verdict while Questions asks how many runs were used. Mark it "(not reported)" or drop it.
8. **Dev-set BAP claim overstated.** "Holds for BAP only on the development set": dev BAP also rises for 06fe and 07me. Say "on the development set for 6 of 8 speakers".
9. **Novelty of feeding measured test-utterance articulation** (M06, Cao et al. paragraph) rests on a quote (t95) that does not say how Cao et al. used EMA. Supply the quote or soften. Unverified: whether Ling et al. 2009 or Cao et al. 2017 also ran conditions with natural articulatory input at synthesis.
10. **Component table M12 cell** "MCD with MUSHRA (pattern match 21)" misstates the tally; write "MCD 21; MUSHRA 14".
11. **Insufficient quotes:** 81.67 fps for [6] (c17 is about subjects); listener counts 23/24/22 (only ledger notes); "tied to no outcome" for [7] (c24 truncated); "did not help" (t23 does not contain it); "single frame" (t8 covers resampling only). Extend the quotes; they are probably right.
12. **"did not help" framing:** a rise in voicing error is consistent with the authors' own statement, not a contradiction of it. Drop "in fact" or say the authors understate the effect.
13. **Verdict hedge dropped:** "Naturalness is claimed" should keep the authors' "may increase".
14. **M05 "Usual approach"** describes this paper's recording setup (inherited dataset), not the field's usual design; the "State of the art" line names the group's own measure rather than the best current work. Minor, as M05 is marked incidental.
15. **[5] comparison baseline:** add that the ~21% MSE reduction is relative to the 2D CNN in [5].
16. **Questions list** asks what test supports "significantly lower", but the review never quotes that phrase; add the source location (the authors' MCD prose in Sec. 3).

## Central claim and confounds

The review's central position, that a small spectral gain does not establish an articulatory benefit, is sound. It handles the leakage confound (fix 3 aside) and the missing listening test. It does not name two others: the text-only baseline is very weak (Merlin trained on about 170 sentences per speaker, MCD 5.4 to 6.6 dB), so any added same-utterance signal could help; and the combined system has 128 more input dimensions with no capacity-matched control (the noise control in "Where the claims outrun the evidence" partly covers this). Fairness: Tongue2Speech is correctly marked [later] and not treated as a missed citation. The verdict `behind` for M12 names deciding priors ([2], [3], [6], [8]) and the effect (no listener test), but the listener counts need quotes (fix 11).

## Scores

- Procedure: 7/10 (claim table complete and arithmetic correct throughout; several quotes truncated just before the decisive words; one excitation table ignored).
- Final text: 6/10 (clear position and correct numbers, but the excitation verdict is wrong as stated, one concession is misattributed, and the misalignment inference does not hold).

Positive, briefly: every Table 1, 2 and 5 number checked matches, the per-speaker ranges and the 2% average are right, and [later] is used correctly.
