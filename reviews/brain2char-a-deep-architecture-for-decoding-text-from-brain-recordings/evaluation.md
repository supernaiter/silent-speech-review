# Evaluation: Brain2Char review

Date: 2026-11-17. Independent evaluator, one pass, no tools beyond the review and its claim table. The claim table was filled by the writer, not by a separate checker, so a row whose quote does not contain the stated number or condition is scored "insufficient evidence", not "correct".

## Claim check

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Brain2Char changed output unit to characters (Verdict, M08) | Row 1/6 quote, Sec. 2.3 | correct | Quote says characters instead of word sequences. |
| 2 | MFCC auxiliary loss in concurrent work [2] (Verdict, M02) | Rows 2, 17 | correct | Makin et al. regress MFCCs during training and discard them at test; the bioRxiv preprint came about two months before the arXiv version of the target, so [concurrent] is right. |
| 3 | Headline 7.0-10.6% WER, 1,200-1,900 words (Verdict) | Row 3 quote | correct | Numbers match the abstract. |
| 4 | "the best results rely on repeated sentences (Sec. 4)" (Verdict) | Row 3 | insufficient evidence | No Sec. 4 quote. It also sits awkwardly next to "the test partition is unstated": if the partition is unstated, the review cannot say the headline relies on repeats, only that Fig. 4b shows WER falls sharply with repeats. |
| 5 | LM trained on the task corpus (Verdict, M06, M07) | Row 34 quote, Sec. 2.4 | correct | "KenLM is used to train the word language models of the speech corpus that is used for speaking tasks." |
| 6 | 80% mean WER on sentence-disjoint tests (Verdict, M08, M12) | Row 4/25 quote, Fig. 4a | correct (number); condition insufficient | Quote gives 25-120%, mean 80% across four participants, but does not itself say "sentence-disjoint"; acceptable given Sec. 3.3 context, should cite the sentence that defines the blue bar. |
| 7 | 25.5% for later ECoG phoneme decoding [3] | Row 12 quote | correct (number); comparison confounded | See central claim below. |
| 8 | 68% relative gap, 253 electrodes | Row 26 | correct arithmetic | (80 - 25.5) / 80 = 68%. Only the electrode count is given as a confound. |
| 9 | PER 65-74%, "phonetically close but misspelled" (M08) | Row 9 quote | wrong (interpretation) | PERs of 65-74% are high; the authors only say they are "much lower" than WER. "Phonetically close" is not supported. |
| 10 | "the failure a phoneme unit plus lexicon avoids" (M08) | none | insufficient evidence | No same-data comparison cited; this is inference stated as fact. |
| 11 | 39 phones with CTC from ECoG [3] | Row 7 quote | correct | |
| 12 | 2.5% online WER at 125,000 words [4] | Row 12 (c2) | correct | Card et al. 2024 report 97.5% word accuracy; intracortical, not ECoG, which the review should keep in view when contrasting with an ECoG paper. |
| 13 | 3% WER on held-out repeats [2] | Row 11 quote | correct (number); condition incomplete | Makin et al. used small closed sentence sets (vocabulary of a few hundred words at most) versus 1,200-1,900 words here; the review omits this when using 3% to rebut "new state of the art". |
| 14 | ~30% gains over DeepSpeech baseline (M06) | Row 13 quote | correct | |
| 15 | [2] trained 30 models per condition | Row 13 (m7) | insufficient evidence | No quote shown for this number. |
| 16 | 10-25% LM gain is confounded by task-corpus LM (M06) | Row 14 quote | partly wrong | The same quoted sentence says the gain over a LibriSpeech LM is only 3-15%; the review omits this, which bounds the confound and changes the argument. |
| 17 | Articulatory targets inverted from same audio (M02) | Row 16 quote | correct | |
| 18 | [3] uses g2p labels, no audio | Row 18 quote | correct | |
| 19 | "8% from MFCC ... up to 15 points with articulatory targets for P2" (M02) | Row 19 quote | insufficient evidence | 8% is quoted (unit relative vs absolute unclear); "15 points" is not quoted and mixes units with the 8%. |
| 20 | "significantly better" with no test (M02, Outrun) | Rows 19, 28 | partly correct | Row 28 supports "significant gains" in Sec. 3.1; no quote for "significantly better" in Sec. 3.2. |
| 21 | "authors concede paralyzed users lack" overt speech (Sec. 4) (M02) | Row 20 quote | wrong citation | Quote is the Sec. 2.1 participant description (no neurological conditions), not a Sec. 4 concession. |
| 22 | P4 84% -> 10% with repeats (M12) | Row 25 (t42) | insufficient evidence | Only the Fig. 4a sentence is quoted. |
| 23 | 23.8% WER, 125,000 words, unseen sentences [5] (M12) | Row 23 quote | correct | But inconsistent with M06/M08, which give [4] 2.5% as the state of the art on the same kind of test. |
| 24 | 4% calibration gain captioned as two participants, legend P1-P4 (Outrun) | Row 29 | insufficient evidence | Caption quoted; neither the 4% nor the legend content is quoted. |
| 25 | "Incremental decoding" uses 850 ms look-ahead (Outrun, M13) | Row 31 quote | wrong (overstated) | Quote says "context latency ... is 850 ms"; that is a latency, not shown to be pure look-ahead, and a bounded latency does not make decoding non-incremental. |

## Central claim and confounds

The central position is that 7.0-10.6% WER does not support "new state of the art" and that on unseen sentences the system (80%) is far behind later ECoG work (25.5% [3]). The strongest confounds for the 80% vs 25.5% comparison are not handled: [3] decodes with a 1,024-word constrained vocabulary and language model, uses far more training data collected over weeks, and records attempted silent speech in a paralyzed participant with a 253-electrode high-density array, whereas Brain2Char decodes overt speech in healthy epilepsy patients with clinical grids and an open 1,200-1,900-word task corpus. Only electrode count is named. The rebuttal using [2] (3%) has the same problem in the other direction (much smaller sentence sets). The LM-confound argument omits the authors' own LibriSpeech-LM comparison.

Fairness: [2] is correctly labelled [concurrent]; it is fair to note it, but the review should not present the authors' failure to beat it as an error in the arXiv version. No later work is treated as prior. No absence or "first/only" claim has a deciding prior named (see fix 11). No slot verdict is `ahead`, so the `ahead` rules do not apply.

## Required fixes (ordered by impact)

1. **Sentence:** "On sentence-disjoint tests the decoder averages 80% WER, against 25.5% for [later] ECoG phoneme decoding [3]." (Verdict) and "Against [3], 80% versus 25.5% is a 68% relative gap (inference), with a 253-electrode array there." (M12)
   **Wrong:** The comparison omits the main confounds: [3] uses a 1,024-word constrained vocabulary and LM, much more training data, and a high-density array; Brain2Char uses open 1,200-1,900-word corpora, clinical grids and overt speech.
   **Fix:** Name these confounds in the M12 sentence (vocabulary constraint, training amount, array density) and soften the Verdict to "far above the 25.5% that later ECoG work reached with a 1,024-word constrained vocabulary [3]".

2. **Sentence:** "The 10–25% language-model gain (Fig. 2b) is confounded: an LM trained on the task corpus already holds any repeated test sentence."
   **Wrong:** The quoted source sentence also reports that the gain over a LibriSpeech-trained LM is only 3–15%, which bounds how much the task-corpus LM can explain. The review leaves this out.
   **Fix:** Add "; against a LibriSpeech LM the gain is 3–15% (Sec. 3.1), so the task-corpus overlap explains at most that share."

3. **Sentence:** ""New state-of-the-art" (Sec. 5) rests on cross-study numbers without shared data; [2] reported 3% on repeats." and "At the time, 3% WER on held-out repeats (2020) [2] [concurrent]."
   **Wrong:** It leaves out that [2]'s 3% was on small closed sentence sets with a far smaller vocabulary, so it is a cross-study comparison of exactly the kind the sentence criticizes. Also, [2] is concurrent with the arXiv version.
   **Fix:** Add the vocabulary/sentence-set size of [2] and "[concurrent]" to the Outrun bullet, e.g. "[2] [concurrent] reported 3% on repeats of a much smaller sentence set".

4. **Sentence:** "**State of the art:** 23.8% online WER on sentences never duplicated in training, 125,000 words (2023) [5]; from ECoG, 25.5% on 249 unseen sentences (2023) [3]; both [later]." (M12, and table row M12 "23.8% unseen [5]")
   **Wrong:** M06 and M08 give 2.5% online WER at 125,000 words [4] (2024) as the current state of the art. M12 names an older, weaker result for the same kind of test, so the sections contradict each other.
   **Fix:** Lead with [4] (2.5%, 2024) in M12, keep [5] as the first 125,000-word result if wanted, and update the table row.

5. **Sentence:** "Its unseen-sentence outputs are phonetically close but misspelled (PER 65–74%, mean WER 80%; Sec. 3.3, Table 3), the failure a phoneme unit plus lexicon avoids."
   **Wrong:** PERs of 65–74% are not "phonetically close". The authors only say that PER is much lower than WER. The final clause is an untested claim stated as fact.
   **Fix:** "On unseen sentences PER (65–74%) is lower than WER (mean 80%) (Sec. 3.3, Table 3), so part of the error is spelling; a phoneme unit with a lexicon would target that error (inference)."

6. **Sentence:** "Gains are 8% from MFCC over two participants and up to 15 points with articulatory targets for P2 (Fig. 3b), called "significantly better" with no test."
   **Wrong:** "15 points" and "significantly better" have no quote in the claim table. The sentence also mixes a relative-or-unspecified 8% with absolute points.
   **Fix:** Quote the Fig. 3b / Sec. 3.2 passage for 15 and for "significantly better", and state whether each figure is relative or absolute. If no such quote exists, drop the 15-point figure.

7. **Sentence:** "Both need overt speech, which the authors concede paralyzed users lack (Sec. 4)."
   **Wrong:** The supporting quote is the Sec. 2.1 description of the participants (no neurological conditions), not a concession in Sec. 4.
   **Fix:** Quote the Sec. 4 passage. If there is none, rewrite as "Both need overt speech; all participants could speak normally (Sec. 2.1)."

8. **Sentence:** ""Incremental decoding" (Table 1) uses a model with 850 ms look-ahead (Sec. 2.4)." (and table row M13 "Offline, 850 ms look-ahead")
   **Wrong:** The source says "context latency ... is 850 ms". That is a latency, not shown to be pure look-ahead, and a bounded latency is compatible with incremental decoding.
   **Fix:** "'Incremental decoding' (Table 1) carries an 850 ms context latency (Sec. 2.4); no online test is reported." Change the M13 cell to "Offline, 850 ms context latency".

9. **Sentence:** "the test partition is unstated, the best results rely on repeated sentences (Sec. 4)" (Verdict)
   **Wrong:** There is no Sec. 4 quote. The sentence also asserts what the headline relies on while saying, in the same breath, that the partition is unstated.
   **Fix:** "the test partition is unstated, and WER falls steeply as test sentences repeat in training (Fig. 4b)", with the Fig. 4b quote added to the claim table.

10. **Sentences without quoted support:** "P4 falls from 84% to 10% as test sentences repeat (Fig. 4b)", "[2] trained 30 models per condition", "The 4% calibration gain is captioned as two participants; the legend lists P1–P4 (Fig. 3a)."
    **Wrong:** The claim table gives no quote containing 84%/10%, 30 models, 4%, or the legend content.
    **Fix:** Add the source quote or a figure-reading note for each. Drop any number that cannot be located.

11. **Sentence:** "None of the 29 studies dated up to 2019 matches the character patterns; from 2023 on, characters (35) trail phonemes (42) (Appendix)."
    **Wrong:** This absence claim names no deciding prior. Character-output BCIs (P300 spellers) and pre-2019 speech decoders with phone or word outputs (e.g. Herff et al. 2015, Brain-to-Text, phone units; Moses et al. 2019, sentence classification) should be named, so the reader can see what the pattern excludes.
    **Fix:** Name the deciding priors and restrict the scope explicitly: "no pre-2019 speech-decoding study emits characters; earlier work used phones [Herff 2015] or sentence classes [Moses 2019]; P300 spellers are outside the scope."

12. **Reference list:** "6. Willett, F. R., Avansino, D. T., ... "High-performance brain-to-text communication via handwriting."..."
    **Wrong:** [6] is never cited in the review body. It appears only in an Appendix row, which breaks "Numbered by first citation".
    **Fix:** Cite [6] in the body where it is relevant (for example as later character-output work in M08), or remove it from the numbered list.

Optional, lower priority: "the articulatory branch adds a regularizer, not information (inference)". The inversion model brings in priors learned from other speakers' articulatory data, so "little information beyond the audio" is more accurate.

## Scores

- Procedure: 6/10. The claim table covers most rows, but about a third of the numeric claims lack a containing quote, and the central comparison was not checked for confounds.
- Final text: 6/10. The position is clear and the internal-inconsistency findings are useful (phoneme vs character in Sec. 2.3, calibration caption). The headline comparison and the LM argument overreach.

The review has a clear position, follows the per-component format, and correctly finds the paper's own inconsistencies (Sec. 2.3 phoneme wording, the overt/silent claim, the missing significance tests).
