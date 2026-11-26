# Triage: Audio-Visual Speech Recognition with a Hybrid CTC/Attention Architecture

Evaluation by a language model separate from the writer (2026-11-26). Each finding checked against the source passage named.

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| F1 | applied | Read the 4 neural pre-2018-09 studies: arxiv-1611.06986 and arxiv-1611.02879 train CTC; WLAS (arxiv-1611.05358) is attention-only; arxiv-1803.04840 names CTC only to say it is not used (frame-wise). HMM 32 is a mention count. | M06 usual approach; table M06 (matched 28, non-neural); Appendix M06 (mentions vs designs); audit counts_/usual_approach_ |
| F2 | applied | NTCD-TIMIT (isca-abdelaziz17b_interspeech) "A simple bi-phone language model has been used for decoding"; regex missed it. Neural LM 0 of 32 stands. | Verdict; M07 usual approach; table M07 matched null; Appendix M07; audit note |
| F3 | applied | Sec. 5.4 says alpha and lambda are optimised on validation; range not given. | Verdict ("reports neither"); slots M06 note |
| F4 | applied | Body attributes later gains to encoder and data (inference). | verdict.json position |
| F5 | applied | Auto-AVSR Table 3: audio-only "Ours 3 448 1.5"; Sec. 3.3 "language models are not included for ASR and AV-ASR models since no further improvements are observed". | M06 and M07 state of the art; table M07 SOTA |
| F6 | applied | Table 2 caption "pre-trained on a non-publicly available dataset"; Sec. 6 "without using any external databases"; Sec. 5.1 "first pretrained on LRW". | Verdict; first bullet of claims section |
| F7 | applied (record only) | LCANet v1 13 Mar 2018; month rule gives [concurrent]. Noted that the authors cite it. | M06 body; verification_status |
| F8 | no change | Agrees with the existing verdict. | none |
| F9 | applied | Abstract "as the signal-to-noise ratio decreases", Sec. 7 "especially at high levels of noise", Sec. 6 "-5dB". | Last claims bullet, rephrased as a one-line slip |
| F10 | applied | LCANet Sec. 4.C "we tried different λ values (from 0.1 to 0.9) and only report the best result here". | Verdict |
| F11 | applied | isca-potamianos01_eurospeech match is "three repetitions of the noisy audio-only sequence" (listener test); talle99 gives 95% confidence intervals. Count 1 of 32; 21 of 22 without. "one-run" no longer read from a missing mention. | Verdict; M12 usual approach; table M12 (21 of 22); Appendix; audit |
| F12 | applied | Auto-AVSR Sec. 4.4 "a consequence of the overlapping noise type in the training and testing phases". | M12 state of the art |
| F13 | applied | Quotes added (t73-t82, c19-c25) and mapped. | claims.md rows 3, 17, 22, 23, 25, 26 |
| F14 | partly applied | LCANet venue and pages from the target's ref. [21] ("IEEE FG, 2018, pp. 548-555"): applied. CM-seq2seq arXiv DOI removed; the IEEE DOI is unverified, so not added. Afouras TPAMI volume and pages unverified: not added (open item). | refs.json; verification_status |
| F15 | applied | Appendix 0 of 32 supports the audio-visual qualifier; "in the wild" dropped. | M06 body |
| F16 | applied | Sec. 6 "(using early fusion)" and "Late fusion performs worse than early fusion"; gamma 0.85 (Sec. 5.4). | Fusion bullet re-aimed at the ranking; locator Sec. 6 |
| F17 | applied | Sec. 4.2 names train, validation and test partitions. | M12 body ("test is implied, inference"); unnamed-split wording removed from the gain bullet; M11 row |
| F18 | applied | isca-su18b-crossdomain and isca-su18b_interspeech have the same title and authors. | Appendix ("4 entries (3 studies)") |
| F19 | applied | Recall-check narration moved out of the M06 body; "unseen noise" replaced by "differ from the training babble". | M06 and M12 bodies |
| F20 | applied | "First" removed. | verdict.json short |

Gates after triage: check_review.py 0 FAIL, 1 WARN (read count accumulated in reused published tables, append-only); verify_quotes.py 93 found, 0 missing.
