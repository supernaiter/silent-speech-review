# Triage: Continuous Silent Speech Recognition using EEG

Date: 2026-11-20. Each required fix in the evaluation was checked against notes.json, the target's source text, the named papers' source passages and the topic tables. Result: 12 of 13 applied (8 correct, 4 partly correct), 1 wrong. Gate after the changes: check_review 0 FAIL, 0 WARN; body 6,941 characters.

| # | Class | What was done |
|---|---|---|
| 1 | partly correct | Card et al. 2024 (NEJM) reports 2.5% WER over the final five Copy Task sessions with a 125,000-word vocabulary (Results), which is later and better. Its main text does not say whether the evaluation sentences were absent from training, so it was added beside Willett et al. 2023 (23.8%, sentences never duplicated in training) and did not replace it. Updated the M12 State of the art, the table row, the Appendix, refs and notes (c10). The topic-table state_of_the_art is unchanged. |
| 2 | correct | The source (Sec. 6) puts the exception at the 10-sentence set, which has higher WER than the larger sets, not at 10 against 5. Rewrote the M07 sentence (84.08% against 79.63% to 83.34%) and the non-monotonic bullet, and corrected notes t22 and t23. |
| 3 | correct | In Makin et al., about 3% is the mean WER of one example participant (Results, Fig. 2a), from intracranial ECoG during overt speech. The Verdict and M12 now give these conditions and make the point about the lenient protocol. Added notes c8 and c9. |
| 4 | correct | The paper names the held-out subject ("the last subject or fourth subject"). Removed "without its identity". Extended the t28 quote so that it contains 92.55. |
| 5 | correct | Limited the closing Verdict sentence to the target: "The paper does not show EEG decoding of unseen silently read sentences." The ZuCo line of work was not added; this is noted in verification_status. |
| 6 | partly correct | The source sentence in Sec. 1 does cover listening ("and while they were listening"); the stored quote had been cut short. The source does credit refs [1-3] jointly. Extended the t55 quote, and the Verdict and M06 now attribute CTC on EEG to the authors' earlier papers jointly, "among them" ICASSP 2019. Same change in the row and the open items. |
| 7 | correct | 1,477 (M04) and 1,460 (M06) are the full-text pattern populations, that is, the 1,458 ledger pattern matches plus studies found only in full text (audit fulltext_only_folders 20 and 3). The Appendix now says so. |
| 8 | partly correct | "Typed", "10 hours" and "nine subjects" are in Zhang et al.'s abstract, and the c3 quote was extended. "Real-time" was dropped because the authors themselves say the model is not causal. The comparison of 10 h with 90 recordings was dropped. The state of the art stays, since it comes from the published topic table, and the text now says that decoder relies on typing, a motor action, not on reading. |
| 9 | correct | Named both scalp-EEG pattern matches in the M04 text and the Appendix: the Rezazadeh Sereshkeh 2018 thesis (hdl 1807/97898) and the Cooney, Folli and Coyle 2018 review (iScience). Their snippets were confirmed: neither decodes sentences. |
| 10 | correct | Added or extended quotes for 86.73% (t24), 0.39 (c5), the character-based model (t12), the GRU and TCN layers (t10), and the authors' STG motivation (t60). The lobe bullet now refers to "the frontal and temporal involvement cited as motivation" and no longer to a "neuroanatomical reading". |
| 11 | partly correct | Target ref. [21] is Toshniwal et al. 2018, a comparison of LM-integration methods, not a corpus, so "corpus not given" stands. M07 now says that the reference cited for the LM names no corpus. Added notes t61. |
| 12 | wrong | 63 for phonemes comes from the published M08 topic table neural-text-output-unit (phonemes 63 of 145, pattern match). It equals the M06 CTC/asynchronous count by coincidence. No change. |
| 13 | correct | Added "(inference)" to the sentence that begins "Trained on the 30 prompts". |

Steps 6-8 were rerun: render, build_refs, fill_row plus fix_row, check_review, claim table and compact. verdict.json and the row were updated to match the text.
