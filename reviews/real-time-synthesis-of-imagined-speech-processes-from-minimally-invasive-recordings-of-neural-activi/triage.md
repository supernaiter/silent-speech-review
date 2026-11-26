# Triage of the evaluation (2026-11-26)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| F1 | applied | Martin 2014 ranked covert reconstructions against DTW-aligned overt references (Sec. 2, Fig. 11), the setup closest to the imagined condition; Herff 2019 and Anumanchipalli 2019 listener tests are on overt output | Verdict, M12 verdict sentence, verdict.json, slots M12 note, M12 audit `deciding_prior` |
| F2 | applied | Martin 2014 text: "percentile rank of the correct" segment, "24–140 segments ... (5 s duration)", covert "in one subject (out of seven)" above chance | M12 Usual approach; notes c16-c18 |
| F3 | applied | Prompt 2 s, blank 1 s (Methods: Task); intertrial detections do not support prompt-locked output, and the Fig. 5 lag is relative to the output frame | Claims-outrun bullet 2 rewritten: no prompt-without-imagery run; Fig. 5 link and "agrees" removed |
| F4 | applied | Authors' own statements: intertrial detections due to "inherent difficulty of knowing how the participant internally performed imagined speaking"; whisper below microphone sensitivity | Authors' explanation credited (bullet 2); whispered-reference bullet deleted; note t74 |
| F5 | applied | Issue (1) quoted in full (t72); authors name Guenther 2009 as addressing both issues (t73), so the paper contradicts itself; Bocquelet 2016 is articulography, outside the sentence; Brumberg 2018 is an EEG closed loop | M06 paragraph |
| F6 | applied | M06 rule admits any non-acoustic signal; only 2 closed loops are neural, both vowel formants | Verdict, M06 Usual approach and verdict sentence (no repetition), Appendix M06, M06 audit |
| F7 | applied | Repository HEAD pinned to f80da4527490d7c172a9d29d86480f9e47cb30b9 (git ls-remote, 2026-11-26); figure_4.py:48-49 np.median; figure_3.py:118-142 vstack and mannwhitneyu; evaluation.ini:23-24; files and sha256 saved in code-f80da45/; paper-internal median/mean inconsistency (t32, t75) put first | Claims-outrun bullets 4-5; notes t60-t68 locations; extra.json code_commit |
| F8 | applied | Fig. 4d VAD gating analysis exists (t35, t42) | Verdict ("and by VAD gating; neither tests word content") |
| F9 | applied | Bocquelet 2015 pilot and 2016 share group and system: counted once (5 meet rule, 4 closed loops); wording now "Of 44 ... 5 synthesized"; cutoff stated with "no candidate dated 2021-01 or 2021-02" | M06 Usual approach, slots M06 (matched 5), Appendix, audit |
| F10 | applied | Brain2voice 2.0 meets the M06 rule (simulated causal inference) and was read (published M06 table, role sota; c20, c21) | M06 State of the art and slots M06 sota, labelled [later, preprint], simulated; Wairagkar 2025 kept as best closed loop |
| F11 | applied | 8 of 21 is a design count; Martin used linear regression, target uses LDA classification | M04 Usual approach and verdict sentence ("with a different regressor") |
| F12 | applied in part | Angrick 2024 vocabulary of 6 keywords confirmed (c19); Berezutskaya 12 words in audit metric. Rejected: Wairagkar 94.34% six-option sentence identification not added, because whether it was scored on closed-loop output is unverified and it is a sentence task, not word identification | M12 State of the art, slots M12 sota |
| F13 | applied | Only words spoken in the audible run have references; 75 imagined words overlap (t37) | What the field needs next, M12 item; 250-word claim removed from M12 paragraph |
| F14 | applied | vad.py:24 default threshold 4; evaluation.ini 0.5 and 1; exp3.py:49 getint on mean scale | Claims-outrun bullet 5; note t66 |
| F15 | applied | Internal notes came from reused refs entries | refs.json `note` fields removed |
| F16 | applied | Process wording | "read in full" removed from body |
| F17 | applied | Angrick 2019 reports correlation and STOI | M12 Usual approach and slots field: "no identification or listener test" |
| F18 | applied | Mean/median labels differ | M04 paragraph: labels stated, 0.15 subtraction dropped |

Applied: 17 (F12 in part). Rejected: 0 in full, 1 part (F12, Wairagkar 94.34%). Verdicts unchanged: M04 standard, M06 standard, M12 behind (deciding prior changed to Martin 2014; the rule's 3 earlier studies still hold).
