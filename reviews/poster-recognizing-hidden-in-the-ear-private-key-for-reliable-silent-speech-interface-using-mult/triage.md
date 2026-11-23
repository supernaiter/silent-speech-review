# Triage of the independent evaluation (14 required fixes)

Evaluator: a language model separate from the writer. Each fix was checked against notes.json and, where needed, the specific source lines in the wiki (target Secs. 1, 3.2, 4, 4.1.1-4.1.2, Fig. 1, Fig. 3; Chetty 2008 Sec. 4; Okamoto 2007 Sec. 3; HPSpeech Sec. 3; Zhu 2007 Sec. 1; Ezz 2020 Sec. 4; arXiv 2604.20229 abstract). ReHEarSSE and MandiPass are not in the wiki index.

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | ReHEarSSE [5] is the target's ultrasonic-only baseline, run per participant in Fig. 3a (t66, t22); DOI 10.1145/3613904.3642095 located. Not in the wiki, so its value is the one the target reports. | References (new entry); M05 State of the art; Verdict; table M05 cell. HPSpeech kept as a secondary comparator. |
| 2 | applied | Correct: an ultrasound-only result exists for the baseline pipeline (t22, t66); HEar-ID's own model has no single-stream ablation (t60). | M05 last paragraph rewritten; the "audio may carry most of the content" inference dropped. |
| 3 | applied (partly) | "Below" is a 1.15-point gap with no variance, so the Verdict now says "no gain" with both numbers. The subset is defined by "users without degraded performance in ultrasonic sensing" (t61, Sec. 4.1.2), so exclusion by performance after testing is quoted; "selected"/"post-hoc" replaced by that description. | Verdict; first bullet of "Where the claims outrun the evidence". |
| 4 | applied | The text cited §4.1.2 while t35 is §4.1.1, and t35 does not show the absence of a cascade. Rephrased to what t35 shows: the only baseline is a recognition pipeline. | M08 paragraph. |
| 5 | applied | Fig. 3b per-user labels are in the extracted figure text (t64 TPR, t65 FPR, axis order S1-S4, S6-S8, S11, S5, S9, S10): S3 FPR 19.20, S9/S10 TPR 0.00, S5 TPR 98.00. | Claim table rows 28-29 now cite t64/t65. |
| 6 | applied (partly) | WER-w/WER-c definition quoted (s15) and added to the claim table. The M12 "behind" verdict already rests on the prior works [13], [2], [3] and the read verifiers, not on the [concurrent] M2SILENT; the state-of-the-art line may include concurrent work (skill rule), so it stays. | Claim table row 25; M12 text unchanged. |
| 7 | applied | Chetty Sec. 4: the first EER block is GMM speaker verification (Fig. 1 DET curves), the second is the liveness test with fraudulent videos (ch6, ch7). The review's assignment was already correct. | Claim table row for M08 state of the art. |
| 8 | applied | Whispered-speech speaker verification of Gołębiowska and Syga (arXiv 2604.20229, 2026, labelled [concurrent] by date): EER 1.88% whisper vs whisper (gs1). Okamoto kept as the prior comparator with the same silent-signal condition. | M06 State of the art; References; M06 Appendix read list; M06 audit read_fulltext. |
| 9 | applied | The published M05 table counts 28 studies: 22 ledger matches plus full-text-only matches. | M05 Usual approach. |
| 10 | unverified | MandiPass is not in the wiki index and was not read. The sentence now says only that the claim rests on the earable qualifier, with no absence claim. | Last bullet of "Where the claims outrun the evidence"; verification_status. |
| 11 | applied | Quotes added: earbud microphone (t62), HPSpeech 8 commands (hp7), Zhu continuous digit task (s16), Ezz ten Arabic digits (sp3), few-shot registration (t63, Fig. 1; "few spellings" changed to "a few recorded commands"), no seeds or repeated runs (t29). "One ANC-earbud microphone" changed to "the earbud microphone". | M05, M03, M08 text; claim table. |
| 12 | applied | CS-TENG is a low-decibel mask; "whisper" replaced. | M08 paragraph. |
| 13 | applied | Okamoto Sec. 3 defines case A as impersonation (ok7). | Claim table row for M06 state of the art. |
| 14 | applied | Fig. 3a shows the baseline run per participant (t66), so "split is unstated" was dropped as a fact; the question now asks whether 91.4% is computed on the same 8 users and sessions. | First bullet of "Where the claims outrun the evidence"; Questions for the authors. |

Also from the check table: finding 17 (Okamoto called a GMM verifier) is rejected on that point, because Okamoto uses per-speaker SVMs; the replacement in fix 8 was applied for currency. Finding 27 (the 24.1-point arithmetic) is no longer needed: the sentence was removed with fix 3. The target DOI (10.1145/3714394.3754429) was added to the header and references.

Counts: 13 applied (fixes 3 and 6 in part; the M12 state-of-the-art part of fix 6 rejected), 0 rejected outright, 1 unverified (fix 10, MandiPass). ReHEarSSE's 91.4% is taken from the target's own report (fix 1).
