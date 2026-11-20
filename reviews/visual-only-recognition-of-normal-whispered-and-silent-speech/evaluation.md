# Evaluation: Visual-Only Recognition of Normal, Whispered and Silent Speech

Date: 2026-11-20. Independent evaluator, one pass over the claim table and the review's positions (Verdict, component sections, "Where the claims outrun the evidence"). Sources were not re-opened; "insufficient evidence" means the claim-table quote does not carry the number or statement as written.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Paper changes two components: public three-mode lip-video corpus (M11) and train-one/test-all grid (M04) | Claim table 1; target Sec. 1 quote | correct | "audiovisual database which is publicly available" supports M11; grid supported by Tables 1-2 rows quoted elsewhere. |
| 2 | 53 speakers recorded | Claim table 6; Sec. 2 | correct | "In total, 53 participants (41 males and 12 females)". |
| 3 | Normal-trained model drops 3.3 / 8.3 points (digits) on whispered / silent | Claim table 4, 15; Sec. 5, Table 1 | correct | 68.0 - 64.7 = 3.3; 68.0 - 59.7 = 8.3, consistent with the quoted row. |
| 4 | Silent training beats normal training on silent test by 2.5 (digits) and 3.2 (phrases); remainder 5.8 and 5.3 is test-mode difficulty | Claim table 15; Tables 1-2 | correct (arithmetic) | 62.2 - 59.7 = 2.5; 68.0 - 62.2 = 5.8. Phrases: 64.4 - 61.2 = 3.2; implied normal/normal 69.7, 69.7 - 64.4 = 5.3, consistent with the 8.5 headline. Only the Table 1 normal row is quoted; the 62.2, 64.4, 61.2 cells are not in any quote. |
| 5 | 12.2% relative drop for both tasks | Claim table 13; arithmetic | correct | 8.3/68.0 = 12.2%; 8.5/69.7 = 12.2%. |
| 6 | Whispered-trained 65.1% beats silent-trained 64.4% on silent phrases, so "matched modes perform best" fails | Claim table 18; Sec. 5, Table 2 | correct in numbers, wording too strong | "the best performance in all 3 cases" is quoted. The 0.7-point inversion lies inside the run SDs (0.9-2.3) the review itself cites; the data do not show the matched claim, rather than refute it. Same applies to "whispered training is best on silent phrases" in the Verdict. |
| 7 | Abstract calls the loss "substantial" | Claim table 17; Abstract quote | wrong | The quoted abstract says "a significant performance drop", not "substantial". The misquote also hides the stronger point: "significant" is used without any significance test. |
| 8 | Silent lowest even under matched training (Sec. 1) | Claim table 19; Sec. 1 | correct | Quote: "performance on silent speech is always low even in the matched condition". Attributed to the authors, not claimed as the review's own finding. |
| 9 | Alignment names 6 stable points but lists 7 | Claim table 21; Sec. 4.1 | correct | Mouth centre (1) + two corners per eye (4) + two nose points (2) = 7. |
| 10 | Utterance boundaries "still being corrected at publication" (footnote 3) | Claim table 20, 25; Footnote 3 | insufficient evidence | The quote describes the segmentation problem (space bar pressed mid-utterance, long waits) but not that correction was ongoing at publication. The 91.8% OuluVS2 figure has no quote. |
| 11 | EMG-UKA: 8 speakers, 63 sessions, free trial subset | Claim table 5; [2] Abstract | correct (sessions/speakers) | "63 recorded sessions from 8 speakers" quoted; the trial subset is not quoted. |
| 12 | EMG-UKA silent WER 48.29 vs 26.90 audible, 28.19 whispered; uncited by target | Claim table 19; Table 4 of [2] | insufficient evidence | No quote carries these three values; "uncited here" needs a check against the target's reference list. |
| 13 | Ultrasound system fell from 75.3% to 45.7% words correct, 39% relative | Claim table 13; Table 2 of [4] | partly supported | 75.3% quoted; 45.7% not quoted. Arithmetic (29.6/75.3 = 39.3%) is right. |
| 14 | 4 speakers in [4] | Claim table 9; [4] Sec. 3 | correct | "Three female and one male French native speakers". |
| 15 | Tao & Busso: 40 speakers, leave-one-out, neutral-trained digits 52.93% to 50.87% on whisper | Claim table 14; [5] Table 1 | insufficient evidence | Quote "NEU WHI 50.87 71.85 68.14" carries 50.87 only; 52.93, the 40-speaker count and the leave-one-speaker-out protocol are not quoted, and the row label does not make clear which cell is visual-only. |
| 16 | [3] is a later study that used the corpus as "the only public visual set with normal and silent speech" | Claim table 2 | insufficient evidence | The cited quote is from the EMG-UKA abstract, not from [3]. Needs a [3] passage. |
| 17 | [3] reused the target's phrase split; "same 11 test speakers" | Claim table 10, 12; [3] Sec. 4.1 | insufficient evidence, possibly wrong | The quote gives [3]'s own split (20/8/11 speakers, 39 of 53). It does not show that these 11 test speakers, or the split, match the target's. |
| 18 | [3]: 22.55% silent WER normal-only, 12.91% with silent data, 9.97% best | Claim table 12, 16; [3] Table 1 | insufficient evidence | Only "LNCE 5.87 12.49 11.58 22.55" is quoted. That row's label (a loss name) and column meaning are not explained, so it is not shown that 22.55 is the normal-only silent WER; 12.91 and 9.97 are not quoted. 22.55 - 12.91 = 9.64 is correct arithmetic. |
| 19 | [3] adds data volume as well as mode, so mode and amount stay confounded | Claim table 16, 22 | correct as a judgement | Reasonable reading, provided [3]'s training sets differ in size; not quoted. |
| 20 | TaL: lip video with silent prompts for 81 speakers, whispered for one, 2020 | Claim table 7; [6] Abstract | insufficient evidence; internal contradiction | Section text says 81 speakers, the component table says 82; text and table say 2020, the reference list says SLT 2021 (arXiv Nov 2020). The quote only states the licence; speaker counts and per-mode coverage are not quoted. |
| 21 | M11 usual approach: surface EMG, 14 of 24 three-mode studies | Claim table 5, 27, 28; Appendix | consistent | Ledger-derived; outside detail check. Plausible as the usual three-mode design. |
| 22 | M11 verdict ahead: no prior released three-mode lip-video corpus | Claim table 8; Appendix | partly supported | Repeats and checks the authors' own "first" claim. Ledger recall for this slot is 0.67 (TaL missed), and the deciding visual priors are not all named (see fixes). |
| 23 | M04 usual approach: overt-trained decoder applied to silent speech, 23 confirmed (7 prior) | Claim table 11, 32, 33 | quote mismatch | The row's quote is the target's Sec. 1 "first audiovisual database" sentence, unrelated to the M04 tally. Count itself is ledger-derived. |
| 24 | M04 verdict standard, effect repeated from [4] and [5] | Claim table 3, 13, 14 | correct as a position | Prior silent-vs-vocalised drop [4] and whisper drop in lipreading [5] both predate the target. |
| 25 | Chronology labels | Reference list | correct | [3] (2023) and [6] (2020/2021) are marked [later] and are not treated as prior work or missed citations. |

## Strongest confound

The headline drops compare different test sets (normal vs silent test material), so test-mode difficulty and train-mode mismatch are mixed. The review handles this well by separating train-mode effect on a fixed test set (2.5 / 3.2 points) from test-mode difficulty (5.8 / 5.3). It does not connect the remaining test-mode gap to footnote 3: if segmentation errors (space-bar timing) are more frequent in silent recordings, part of the "silent is hardest" gap may be data-quality, not articulation. The comparison with [4] correctly declines to rank across different starting points. Positions are cited throughout; the over-strong ones are listed below.

## Required fixes (ordered by impact)

1. Correct the abstract quotation: the target says "significant performance drop", not "substantial". Use the exact word and note that no significance test backs it, which strengthens the 2.5-3.2-point point.
2. Support or remove "on the same 11 test speakers" and "reused its phrase split" for [3]: the quoted passage gives [3]'s own 20/8/11 split of 39 speakers and does not show identity with the target's test speakers.
3. Add quotes for the [3] figures (12.91, 9.97) and state which row and column of [3] Table 1 gives the 22.55 normal-only silent WER; the quoted "LNCE" row does not by itself establish it.
4. Fix the TaL contradiction: 81 speakers in the M11 text, 82 in the component table; and 2020 in text and table versus SLT 2021 in the reference list. Add a quote for speaker counts and the one-speaker whisper coverage.
5. Replace the claim-2 quote with a passage from [3] that supports "the only public visual set with normal and silent speech"; the current quote is from EMG-UKA.
6. Soften "fails" for "matched modes perform best" and "whispered training is best on silent phrases": the 65.1 vs 64.4 inversion is inside the run SDs, so the matched-best claim is not shown rather than refuted.
7. Add quotes for comparator numbers carried in the text without one: 45.7% in [4]; 52.93% and the 40-speaker leave-one-out protocol in [5]; 48.29 / 26.90 / 28.19 in [2] Table 4; the 62.2, 64.4, 61.2, 65.1 cells of target Tables 1-2.
8. For the M11 "ahead" verdict, name the visual priors that were weighed and set aside (for example the audiovisual whisper corpus behind [5], two modes with video; single-speaker ultrasound-plus-lip silent/vocalised recordings from the Ouisper line; Freitas et al. multimodal silent-speech corpora, LREC 2014) and state that ledger recall for this slot was 0.67.
9. Rephrase "still being corrected at publication" to what footnote 3 shows (known segmentation errors in the release), or add the supporting text; add a quote for the 91.8% OuluVS2 figure; consider noting segmentation quality as a possible part of the test-mode gap.
10. Replace the claim-table row 11 quote (M04 usual approach) with the Appendix M04 tally reference; the current target Sec. 1 quote does not relate to it. Also confirm "uncited here" for [2] against the target's reference list.

## Scores

- Procedure: 6/10. Arithmetic and target-paper quotes are sound; many comparator numbers and two [3] statements rest on quotes that do not carry them, and one abstract quotation is wrong.
- Final text: 7/10. Clear position, well-separated effects, honest handling of cross-modality comparisons; needs the misquote, the TaL contradiction and the unsupported [3] split claim fixed.
