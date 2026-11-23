# Triage: emg2speech review

Date: 2026-11-23. Input: `emg2speech-synthesizing-speech-from-electromyography-using-self-supervised-speech-models.eval.md` (independent evaluation of the compact review and claim table, 12 required fixes). Each finding was checked against the source passage it concerns (target text, or the named paper's source text in the wiki). Round 1 of at most 2.

Result: 7 correct, 4 partly correct, 1 wrong, 0 unverifiable. Applied: 11 of 12 (all correct and partly correct ones).

| # | Finding | Verdict | Evidence | Where applied |
|---|---|---|---|---|
| 1 | Table 6: 61.02% is pooled listener WER, 51.17% decoder WER; carry the "all 460 sentences" training caveat into the Verdict; quote "460 evaluated sentences" | correct: applied | App. D.3: "for all evaluated sentences (460 sentences in total across DATA GENERAL and DATA ALS)" and "the mean WER of 61.02%" (rater transcripts); App. D.4: "decode phonemes on all 460 sentences", then WFST decoding "yields a WER of 51.17%". | Verdict sentence 3 (scoring differs, training caveat, the table ranks neither route); `verdict.short`; notes.json t104; row fields `position_in_field`, `axes_regressed` via fix_row.py |
| 2 | No quote shows the ALS corpus was silent; drop "silent" | wrong: rejected | Sec. 3.2: "A participant diagnosed with amyotrophic lateral sclerosis (ALS) silently articulates English sentences (with overt articulatory movements but no audible output)" (notes.json t96, already present but not mapped in the claim table). | No text change; t96 added to claim-table rows 4 and 20 |
| 3 | M02 usual approach: "10 are synthesis studies" contradicts the Appendix; the table names the minority design | partly correct: applied | The published topic table's note says the 34 pattern matches are "recognition and synthesis; 10 of them are synthesis", so the section line was right and the Appendix wording ("in 10 of 34") was the ambiguous one. The table cell did name the minority design. | M02 usual-approach line now opens with acoustic targets only and says the 34 include recognition; Appendix usual-design line reworded; slots M02 `field` "Acoustic targets only; phoneme loss in 10" (count and tier unchanged) |
| 4 | M02 state of the art: 25.14% with an added loss conflicts with GETS at 11.89% on the same benchmark | partly correct: applied | No real conflict: GETS Sec. 3.2, "this guidance mechanism is utilized exclusively during the inference stage, requiring no additional linguistic labels during training". It adds no training loss. The text did not say why, so a clause was added. | M02 state-of-the-art line ("GETS (11.89%) guides only at inference"); notes.json c22 |
| 5 | [9]: quotes do not name the target type for 26.55% and 25.14% | correct: applied | Lee et al. 2026 Table 1 rows "Ours (Mel)" 25.14 and "Ours (SU)" 26.55; Sec. 5.1: "our model (Mel) achieves ... (from 26.75% to 25.14%)", "our model (SU) ... reducing the WER from 27.78% to 26.55%". | M06 paragraph names both row labels; notes.json c11, c12 quotes replaced |
| 6 | "Pretrained vocoder" is a Tacotron; no quote for "learned with CTC" | partly correct: applied | The paper itself calls it a vocoder: Sec. 2 "a pretrained Tacotron (Wang et al., 2017) vocoder"; Sec. 5.3 "Training is performed with the connectionist temporal classification (CTC) loss". The wording was the paper's; the quotes were short. | Verdict sentence 1 (Tacotron "vocoder", §2; CTC, §5.3); notes.json t101 extended, new t103; slots M08 choice; row `canon_before`, `output_type` |
| 7 | M12: sentence-disjoint (13 of 64) is a minority; held-out speaker (21) is most named | partly correct: applied | The published topic compares sentence-disjoint against closed or repeated sentences (13 against 9); held-out speaker (21) is a separate axis, so the usual approach of the topic stands. The line did not say so. | M12 usual-approach line ("13 ... against 9 a closed set; held-out speakers (21) are another axis"); slots M12 `field` "Sentence-disjoint (13) over closed (9)" (count and tier unchanged) |
| 8 | [3]: no column header for 73.53, no quote that the 1,970 test sentences are unseen | correct: applied | Gowda and Miller 2025: "The mean WER is 73.53%"; Sec. 5: "Sentences in the test set are not present in the training and validation sets". | M12 sentence ("73.53% mean WER on 1,970 test sentences absent from training"); notes.json c17 quote replaced, new c23 |
| 9 | No quote that Table 5 audio came only from the guided model | correct: applied | Sec. 5.3.1: raters "listened to all 400 synthesized audio samples in the test set (generated from dis(H)HUBERT units obtained via phoneme-guided decoding with vec(E) as input)". | First bullet of "Where the claims outrun the evidence" cites §5.3.1; notes.json t106 |
| 10 | "More fluid, natural interaction" is not in the quote | correct: applied | App. D.4: "it can enable a more fluid, natural interaction". | notes.json t105; claim-table row 3 |
| 11 | [8]: no quote for "one ALS participant" and "benchmark" | correct: applied | Wairagkar et al. 2026 Abstract: "on our prior intracortical brain-to-voice benchmark dataset"; Methods: "of participant T15 with ALS". | notes.json c24, c25; claim-table row 6 |
| 12 | p < 10^-6 not tied to the healthy corpus | correct: applied | Table 3 caption: "on DATA GENERAL. Values are averaged over 5 random seeds. The improvement is statistically significant (p<10^-6)." | M02 paragraph cites the Table 3 caption; notes.json t23 quote extended |

Claim-check rows not listed among the fixes (rows 2, 8, 9, 11 to 14, 16, 18, 20, 21, 23 to 25 marked correct) need no change.

## Reruns

- Steps 6 to 8 rerun after the edits: render, references (9 references, unchanged), `fill_row.py` then `fix_row.py` (22 legacy fields set to English text that matches the revised review), gate, claim table.
- `check_review.py`: 0 FAIL, 1 WARN (14 papers read in full besides the target; unchanged from the first round, read only in the passages holding the cited values). Body 6,970 characters.
- `verify_quotes.py`: 105 found, 0 missing, 24 unchecked.
- `audit_tally.py`: all four audits pass. Tallies, usual approaches and states of the art equal the published topic tables; candidates only appended.
- `claims.md` regenerated and every mapping refilled (44 rows, no open mappings); `compact.md` regenerated.

## Still open (to `verification_status`)

- Appendix C of the target is partly garbled in the source text extraction (unchanged).
- Whether the 460 test sentences entered EMG2TEXT training stays a question for the authors.
