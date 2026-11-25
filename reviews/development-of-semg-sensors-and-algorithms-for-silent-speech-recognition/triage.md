# Triage of the evaluation (2026-11-25)

Evaluator: a language model separate from the writer (13 findings). Each finding was checked against notes.json and, where needed, the specific passage of the wiki source text (target, Deng et al. 2014, Sridhar et al. 2010, Hwang et al. 2026).

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | Target Methods, Protocol: 19 enrolled, three excluded as non-compliant, corpus not named; corpus counts 9 + 4 + 6 = 19 (t11, t83). The five-of-six arithmetic stands (c1-c3). | Verdict reworded ("mean of five of the six 2014 subjects"; omitted subject not identified, stated exclusion as one possible reason; "does not hold" removed); claims item 1; question 1; verdict.json |
| 2 | applied | Target text describes grammar construction only for Corpus 2 (Methods, Modeling grammatical context); the final system only "incorporates NL Equivalence Grammar" (t41, t80). | Verdict no longer says how the Corpus 3 grammar was built; M07 limits the construction to Corpus 2 and marks Corpus 3 unstated; table row M07 changed |
| 3 | applied | Deng et al. 2014 Sec. 2.1: each task set tested with models trained on the other three plus TIMIT, half of common phrases and text messages reserved for validation (c4). | Verdict states the 2014 protocol; question on the partition restated as whether Table 2 uses it; M12 table note |
| 4 | applied | Deng et al. 2014 Table 1: unseen words 70, 36, 36, 41 (c5). | Claims item 2 restated; unseen-word question removed |
| 5 | applied (partly) | Target Discussion: "final 8-sensor system" (t81); 11 sensors stated without per-corpus breakdown (t13, t82); 2014 data recorded with 8 sensors (c6); Fig. 6 best subset 10.4% vs Table 2 8.9% (t40, t42). The "one side of the face" reading (t79) is the authors' configuration conclusion and was dropped. | Claims item 3 rewritten; question 4 |
| 6 | applied | t66 records only that no independent selection data are described. | M05 and M06 now say "no separate selection data are stated" |
| 7 | applied | Audit notes: M05 attribution 21 (upper bound), search 10, single-channel 5, random 3 of 42; M12 sentence-disjoint 13, closed 9, held-out-speaker 21 of 64. "Standard" for M05 rests on the design predating the paper (Sridhar 2010; 2014 report), per the SKILL rule. | M05 usual-approach line gives the distribution; Appendix M05 and M12 lines; table field labels for M05 and M12 |
| 8 | applied | Hwang et al. Sec. 3 "all possible 4-channel combinations out of the 8 available channels (a total of 70 combinations)" and Table 1 first row 47.2 (c14, c15); Sridhar et al. Abstract full sentence with 5, 11 and 79.6% (c10 quote extended). | notes.json; M05 numbers kept; claim table rows 7-8 |
| 9 | unverified | Colby et al. (ICASSP 2009), cited by Deng et al. 2014 as [26], is not in the wiki and was not read. | M05 now attributes the 11-to-8 cut to "an earlier study by this group" as stated in [2]; not cited directly |
| 10 | applied | c12 is phrase classification accuracy; c11 is a single-speaker benchmark with LLM rescoring (Benster et al. Abstract). | M06 state of the art and comparison sentence; table cells M06 and M12 |
| 11 | applied | Unigram and NATO WERs appear only in Fig. 3, not in the text. | Clause "keeping nearly all of that constraint (inference)" removed |
| 12 | applied | M07 audit: grammar 4 of 64. | M07 usual-approach line ("established but rare"); verdict line notes the untested effect |
| 13 | applied | Published M06 inclusion rule counts a study under every decoder it names. | M06 usual-approach line and Appendix; "changes" replaced by "combines" in the Verdict |

Unverified suggestions in the evaluation's "possible better or later work" section: no later Gaddy-benchmark value below 12.2% appears among the M07/M12 audit candidates read; Gaddy and Klein electrode ablations were not read and are not cited.

Counts: 13 findings; 11 applied, 1 applied in part, 1 unverified, 0 rejected.
