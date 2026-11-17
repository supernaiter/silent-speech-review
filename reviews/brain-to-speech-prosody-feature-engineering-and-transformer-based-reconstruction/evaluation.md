# Evaluation: Brain-to-Speech: Prosody Feature Engineering and Transformer-Based Reconstruction

Date: 2026-11-17. Independent evaluator, single pass, over the review and its claim table only (no sources opened). The claim table was filled by the writer, not by a separate checker, so rows whose "quote" is the writer's own note (t100, t101) count as assertions, not evidence.

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Chapter changes M06 (wavelet, PAC, autoencoder, Transformer) and M08 (IHPR) | Row 1 quotes, target §1, §3.1–3.2 | correct | Quotes cover each element. |
| 2 | "No ablation isolates any part" | Row 2 / 9 | insufficient evidence | Quote is the writer's note (t100), not the target. Plausible absence claim; acceptable if stated as the reviewer's reading of §5 and Table 1. |
| 3 | "The same first two authors already published the pipeline as MiSTR [2]" | Row 8; reference list | partly supported | Shared first two authors is right per the references. The only MiSTR quote is "A Transformer-based decoder for prosody-aware spectrogram". Wavelet extraction is not quoted; the phase step rests on the MiSTR title ("Neural Phase Reconstruction"), which is not shown to be the same method as IHPR. "The pipeline" goes beyond what is shown. |
| 4 | "Table 1 matches MiSTR's value for value, uncited" / "repeats ... 28 values" | Rows 3, 21 | insufficient evidence | No row of MiSTR's Table 1 is quoted. The MiSTR quotes show only PC 0.91 (p3), HNR 12.7 with +1.6 dB over the best baseline (p1), Seq2Seq MCD 3.90 (p2) and 3.38 (p4). The other ~24 values and the 'uncited' status rest on the writer's note t101, not on a quote from MiSTR's table or from the chapter's reference list. |
| 5 | MCD "consistently lower" contradicts Table 1 (Seq2Seq 3.90 vs 3.92) | Row 22 | correct | Quotes support it. |
| 6 | MiSTR stated the Seq2Seq exception | Row 23 | correct | "slightly lower score of 3.90". |
| 7 | §4.4 shared-protocol claim fails: 5.39 and 5.04 equal [3]'s means from a per-speaker 80/20 split | Row 24 | partly supported | Quote "Mean 5.39 4.55 5.04 4.78" gives no column labels, so the mapping to regression and 3D-CNN is not shown; "per-speaker" is not in the truncated 80/20 quote. Labelled inference in the bullet, but stated as a plain failure in the Verdict. |
| 8 | §4.1 vs dataset: 100 words, notebook onboard microphone, 48 kHz | Row 25 | correct | Quotes support both sides. "Continuous speech" absent from the dataset is implied, not quoted. |
| 9 | "Significantly" without a test; "the dataset paper supplies a chance procedure [6]" | Row 26 | wrong (support) | The [6] quote is "All results are obtained in a non-shuffled 10-fold cross validation", which is not a chance procedure. |
| 10 | Harvest F0 may leak target information | Row 27 | correct as inference | Labelled inference; fair. |
| 11 | Chapter claims "high intelligibility" (Verdict) | none | no quote | No row quotes the chapter making an intelligibility claim; the abstract quote says "quantitative and perceptual metrics". |
| 12 | M06 usual approach: high gamma 62 of 180; wavelet 19, theta/beta 13, PAC 4 | Rows 5, 33 | plausible | Ledger tally; high gamma is the usual input. Not audited per brief. |
| 13 | M06 state of the art: 43.75% median listener WER [4], 31% WER 25-word pool [5], naturalness 18–29 [3] | Row 7 | numbers correct; framing weak | Values match quotes. These are output-intelligibility results on different recordings and tasks; they rank systems, not processing front ends. Acceptable as field ceiling but should be called that. |
| 14 | M08 state of the art: FC-DNN + WaveGlow mean MCD 4.55 dB [3] | Row 13 | insufficient evidence; internal tension | The quoted row has no column labels, so 4.55 is not tied to FC-DNN + WaveGlow in the shown quote. Also 4.55 is worse than the chapter's 3.92 and the 3.90 baseline; the review must say these MCDs are not on one protocol, otherwise the "state of the art" reads as below the target. |
| 15 | §3.2.2 "neural vocoder" vs §3.2.3 IHPR inconsistency | Row 14 | correct | Quotes support it. |
| 16 | HNR 11.1 to 12.7, +1.6 dB, 14%; "it is MiSTR's number" | Row 15 | correct | 1.6/11.1 = 14.4%. MiSTR quote p1 carries 12.7 and +1.6. |
| 17 | IHPR is "a Griffin-Lim-family method" | Row 12 | inference unmarked | Reasonable reading of §3.2.3, but a characterization; mark as inference. |
| 18 | M12 usual approach: crowd workers 15 of 79 | Row 16, 42 | wrong framing | 15 of 79 is a minority; the usual design is a listener test of any kind (79), not crowd workers. The summary table repeats "Crowd-worker listener tests (15)" as the usual approach. |
| 19 | Kohler et al. "two-choice test with 19 listeners" | Row 16 | partly supported | 19 listeners quoted; "two-choice" is not in the truncated quote. |
| 20 | MiSTR "printed 3.38" | Row 17 | insufficient | Quote does not name the metric; say MOSA-Net (or whatever MiSTR reports) explicitly. |
| 21 | Kohler: five runs per setting, above chance for two of three participants | Row 19 | mostly correct | "Five independent runs" quoted; "P2 and" truncated, three participants implied. |
| 22 | M12 "behind" the 24 prior listener-test studies | Rows 20, 43 | follows rules | Ledger count, deciding priors ([5], [7], [4]) and the effect (no listener measure) are given. |
| 23 | Chronology of MiSTR as prior work | Reference list; row 43 | needs care | MiSTR is Interspeech 2025 (arXiv 2508.03166, Aug 2025); the Appendix dates the target's first public version before 2025-10. MiSTR is within six months of the target. Because it is the same authors' own work they could cite it, but the chapter may be a contributed extended version written in parallel; the review should not imply misconduct beyond what the overlap shows. |
| 24 | Row 30 "Questions for the authors" | claim table only | contradiction | The claim table lists a section that is not in the review text. |

## Strongest confound

The comparisons in Table 1 mix numbers carried from different papers and protocols (tenfold CV vs per-speaker 80/20) with the chapter's own runs; absolute MCDs are therefore not comparable across rows or with [3]. The review handles this for §4.4 but then uses [3]'s 4.55 dB as a state of the art without the same caveat.

## Required fixes (ordered by impact)

1. **Sentence:** "Table 1 matches MiSTR's value for value, uncited (inference)." and "Table 1 repeats MiSTR's PC, MCD, STOI and HNR for all seven systems, 28 values (inference), without citing it [2]."
   **What is wrong:** The claim table shows only four MiSTR values (PC 0.91, HNR 12.7, +1.6 dB over the best baseline, Seq2Seq MCD 3.90). No row of MiSTR's Table 1 is quoted, so "value for value" and "28 values" are unsupported; "uncited" rests on the writer's own note, not on a quote of the chapter's reference list. The wording ("repeats", "uncited" stated twice) implies duplicate publication on stronger terms than the evidence.
   **Fix:** Either add quotes of MiSTR's Table 1 rows and a located statement that the chapter's reference list does not include MiSTR, or reduce to what is shown: "The proposed-model values MiSTR reports in its text (PC 0.91, HNR 12.7 dB, +1.6 dB over the best baseline) and its Seq2Seq MCD of 3.90 reappear in Table 1; the chapter does not cite MiSTR [2]." Keep the question to the authors (whether Table 1 is the MiSTR experiment) and drop "28 values" unless quoted.

2. **Sentence:** "the same first two authors already published the pipeline as MiSTR [2]." (also "MiSTR already combined wavelet extraction, a Transformer for prosody-aware spectrogram prediction and a harmonic phase vocoder [2].")
   **What is wrong:** Only the Transformer prosody-aware decoder is quoted from MiSTR; wavelet extraction and a harmonic phase method equivalent to IHPR are not shown. MiSTR (Aug 2025) is also within six months of the target's first public version, and the chapter may be a parallel extended version by the same group; "already published the pipeline" frames it as settled prior publication.
   **Fix:** Quote MiSTR's wavelet and phase-reconstruction passages, or narrow to "MiSTR [2], by the same first two authors and published about two months earlier, already used a Transformer decoder for prosody-aware spectrogram prediction with neural phase reconstruction." State neutrally that the chapter does not cite it, without implying intent.

3. **Sentence:** "\"Significantly\" (§5.1) has no test or chance level, though the dataset paper supplies a chance procedure [6]."
   **What is wrong:** The quoted support from [6] is about non-shuffled 10-fold cross-validation, not a chance procedure.
   **Fix:** Quote the [6] passage that defines the chance level (e.g. a shuffled or randomized baseline), or end the sentence at "has no test or chance level."

4. **Sentence:** "The claims of high intelligibility, of a lower MCD than every baseline and of one shared baseline protocol fail against the chapter's own table and its baselines' sources."
   **What is wrong:** No claim-table row quotes the chapter claiming "high intelligibility"; the shared-protocol failure is an inference in the bullet (column mapping of [3]'s Table I not quoted) but a flat statement here.
   **Fix:** Add the chapter's intelligibility sentence with its location or drop that item; mark the protocol point as inference ("appear to fail") or quote [3]'s Table I column headers so 5.39 and 5.04 are tied to regression and 3D-CNN.

5. **Sentence:** "**State of the art:** On the same dataset, FC-DNN with WaveGlow reached a mean MCD of 4.55 dB in 2024 [3]; that row does not appear in Table 1, while the 5.39 and 5.04 rows of the same paper do."
   **What is wrong:** The quote has no column labels, so 4.55 is not shown to be FC-DNN + WaveGlow; and 4.55 dB is higher than the chapter's 3.92 and the 3.90 baseline, so a reader sees a "state of the art" that the target beats, without the explanation that the protocols differ.
   **Fix:** Quote the column header for 4.55, and add: "MCDs from [3] (per-speaker 80/20) and Table 1 (tenfold CV) are not on one protocol, so 4.55 dB is the best figure on this dataset under [3]'s split, not a bar the chapter's 3.92 clears."

6. **Sentence:** "**Usual approach:** Of 79 studies scoring non-acoustic-to-speech output with listeners (pattern match, Appendix), 15 use crowd workers" (and the summary-table cell "Crowd-worker listener tests (15)").
   **What is wrong:** 15 of 79 is a minority, so crowd workers are not the usual approach; the usual approach is a listener test (79).
   **Fix:** "Usual approach: a listener test (79 studies, pattern match); 15 of these use crowd workers." Change the table cell to "Listener tests (79)".

7. **Sentence:** "the encoder-decoder baseline's paper ran a two-choice test with 19 listeners [7]" and "MiSTR printed 3.38 [2]."
   **What is wrong:** "Two-choice" is not in the quoted passage; the metric behind 3.38 is not named in the quote.
   **Fix:** Extend the [7] quote to show the forced choice (or write "an identification test with 19 listeners"); name the metric of 3.38 ("a MOSA-Net score of 3.38" if that is what MiSTR reports).

8. **Sentence:** "IHPR refines STFT phase iteratively under harmonic constraints (§3.2.3), a Griffin-Lim-family method"
   **What is wrong:** The family label is the reviewer's characterization, not the authors'.
   **Fix:** Add "(inference)" after "a Griffin-Lim-family method".

9. **Sentence (claim table row 30):** "Are the Table 1 numbers the MiSTR experiment, and which baseline values ..."
   **What is wrong:** The claim table lists a "Questions for the authors" section that the review does not contain.
   **Fix:** Add the section (it is the right place for the MiSTR question) or remove row 30.

## Scores

- Procedure: 6/10. Quotes are located and most numbers check, but the most serious claim (duplicated table) rests on the writer's own note rather than a source quote, and the claim table was not checked by a separate pass.
- Final text: 6/10. Clear positions and good internal-inconsistency findings (MCD exception, dataset description, vocoder path), but the MiSTR claim and two support mismatches need correcting before publication.
