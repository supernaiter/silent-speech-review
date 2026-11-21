# Triage: Improving the Gap in Visual Speech Recognition Between Normal and Silent Speech Based on Metric Learning

Evaluation: `improving-the-gap-in-visual-speech-recognition-between-normal-and-silent-speech-based-on-metric-learning.eval.md` (2026-11-21, 12 required fixes). Each fix was checked against the target text, the named papers' source text and the notes and audits. Result: 10 applied (7 correct, 3 partly correct), 1 wrong, 1 unverifiable.

| # | Fix | Verdict | Evidence | Where applied |
|---|---|---|---|---|
| 1 | Remove "20/8/11 speaker counts" for [5] | wrong | Petridis et al. 2018, Sec. 4.2: "for the second set of experiments, i.e., phrases, we use 20, 8, 11 participants"; the 30/10/13 quote was the digits split. The claim stands; only the notes quote was wrong. | notes.json c3 quote and location corrected; text unchanged |
| 2 | Replace "one run per row" with "no run count or spread reported" | correct | Target Sec. 4.4 and Table 1 give no run count; Fig. 3 averages five subset runs (already stated). | Verdict, M03, claims section, slots M03/M12, verdict.json, fix_row.py |
| 3 | Resolve "route is new" against verdict standard; explain [3] | partly correct | Not a contradiction under the verdict rules (ahead needs repetition), but the text did not say so; [3] is concurrent and uses a domain classifier, not a paired divergence. Naming the 4 later studies is not needed: they are later and the Appendix gives the count. | M03 section, slots M03 note |
| 4 | Drop [3] as support for "common in EMG and ultrasound" | correct | [3] is first public 2023-04, within 6 months of the target, so [concurrent]. | Verdict now rests on the Appendix count (31 of 138) and [2]; verdict.json |
| 5 | Silent VER range covers only two-mode rows | correct | Normal-only row has silent VER 12.49% (Table 1); 6.66-7.77% holds over the 12 two-mode rows. | M03 section |
| 6 | Add quotes for unquoted numbers | partly correct | [4] 10 seeds and p = 0.002 and [3] 43.114% are in the sources and now quoted; "one model per row" for [3] is not stated and was removed; Fig. 3 normal data at 1,000 is stated in its caption ("remained constant at 1,000"); all 13 Table 1 rows were already in notes. | notes.json c12, c13, c14, t63; M03 section |
| 7 | Make "75% of it" exact | correct | 8.27/10.97 = 75% of the original gap; 8.27/9.20 = 90% of the gap the full loss closes. | Claims section |
| 8 | "Standard deviation" for [4]; seed spread is an analogy | correct | [4] Sec. 5.1: "standard deviation for the WER metric across different seeds is approximately 1%"; different task (EMG-to-speech). M12 rests on the missing run count in the target. | Verdict, verdict.json, fix_row.py |
| 9 | Comparator WERs do not rank against 10-phrase WER | correct | [3] is ASR WER on reconstructed speech, [2] and [4] open-vocabulary EMG-to-speech; target is a 10-phrase set. | M03 section |
| 10 | Say which split selected the weights is not stated | partly correct | Sec. 4.2 "adopted the parameters that achieved the best performance"; the 400-utterance validation split exists (Sec. 4.1). The original wording was accurate but is now more precise. | Verdict, claims section, fix_row.py |
| 11 | "Nearly doubles" for 11.58% to 22.55% | correct | Ratio 1.95. | M04 section, slots M04 note |
| 12 | Venue of [3] is ICASSP 2023 | unverifiable | The wiki source is arXiv v1 with no venue statement; meta_source must be paper_text. Kept as arXiv preprint (still [concurrent]). | verification_status open item |

Not applied as fixes: 1 (wrong), 12 (unverifiable). The evaluator's per-claim note 9 (normal WER also worsens with +LSKL) was not added, for length.
