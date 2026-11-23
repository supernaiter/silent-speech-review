# Evaluation: Poster: Recognizing Hidden-in-the-Ear Private Key for Reliable Silent Speech Interface Using Multi-Task Learning (HEar-ID)

Date: 2026-11-23
Evaluator: a language model separate from the writer

Inputs: evaluator brief and compact.md (review, references, claim table) only. No sources, web or wiki were opened, so every check below goes only as far as the claim-table quote. Outside knowledge is marked "unverified".

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | HEar-ID changes sensing, model, enrollment and output (Verdict) | Row 1 (Abstract; §3.2; §3.4) | correct | The quotes support whisper plus ultrasound, a shared embedding, 50 words with impostor rejection, and accept/deny. |
| 2 | All-user Top-1 67.3%; 8-user 90.25% below the 91.4% baseline (Verdict) | Row 3 (§4.1.2) | correct (numbers); position too strong | The numbers match. "No gain" and "below" rest on a 1.15-point gap on 8 users with no variance, against a baseline whose data are unclear. The evidence supports "no demonstrated gain", not "below". |
| 3 | 8-user subset is "selected" / "post-hoc" (Verdict, Outrun bullet 1) | Rows 3, 28 | insufficient quote | No quote says how the 8 of 11 users were chosen. The Conclusion wording only shows that a subset was reported. |
| 4 | Impostors are the other participants, whose data also train the model (Verdict, M03, M12) | Rows 4, 19 (§4.1.1) | correct | t59 and t33 support it directly. |
| 5 | Replay, which motivates the paper, is never tried (Verdict) | Row 4 (§1) | correct as far as the quote goes | The motivation quote supports it. The absence of a replay test is plausible but has no quote. |
| 6 | 91.4% baseline split is unstated (Outrun bullet 1) | Rows 28, 32 (t35, §4.1.1) | insufficient evidence | t35 ("We implement the pipeline of [5] serving as a baseline") suggests the authors re-ran the baseline, probably on their own data. Keep the point as the question to the authors, not as a fact. |
| 7 | OFDM, 17.5–23 kHz and 0–11 kHz bands (M05) | Row 6 (§3.1, §1) | correct | |
| 8 | "One ANC-earbud microphone" (M05) | Row 6 | insufficient quote | No quote mentions a single microphone. |
| 9 | No whisper-only or ultrasound-only result (M05) | Row 11 vs rows 3, 28 | wrong (internal contradiction) | The review itself cites an ultrasonic-only baseline (91.4%) that the authors implemented (t35). An ultrasound-only result therefore exists, at least for the baseline pipeline. What is missing is an ablation of HEar-ID's own model. The inference that "audio may carry most of the content" is also weakened by the strong ultrasound-only baseline. |
| 10 | HPSpeech 90.3%, 8 silent commands, user-dependent, held-out sessions (M05 SOTA) | Row 7 | partly insufficient | 90.3%, FMCW and the 18/2 session split are quoted. "8 commands" is not quoted. |
| 11 | M05 state of the art choice | Section M05; References | wrong / incomplete | The authors' own earbud-ultrasound spelling system, ReHEarSSE, supplies the 91.4% comparator but is missing from the reference list and is not named as state of the art. HPSpeech (8 commands) against HEar-ID (50 words) does not compare like with like. Other candidates the reviewer may check: EchoSpeech (2023, glasses), EarCommand (2022, ear canal) (unverified). |
| 12 | M2SILENT within-user WER 4.56–8.96%, cross-user 14.22–19.05%, 41 words, fine-tuned on 10 words (M05, M12) | Rows 9, 26 | insufficient quote | The quote names "WER-w" and "WER-c" but does not define them. Reading them as within-user and cross-user is plausible given s9 but not shown. |
| 13 | SoniSpeech 26.3% WER, open vocabulary, one speaker [later] | Row 9 | correct | It is correctly labelled [later] and not treated as prior work. |
| 14 | Zhu et al. cut "audio digit" WER by 24–29% relative | Row 10 | partly insufficient | 24–29% is quoted. "Digit" is not. |
| 15 | Cai et al. fuse vocal and echo keyword spotters on a headset | Row 10 | correct | |
| 16 | Okamoto: EER 0.2%; disjoint impostors; held-out session; 5.5% (male) under impersonation | Rows 13, 18 | partly insufficient | 0.2%, the disjoint impostors and the held-out session are quoted. The quote does not show that "case A" is impersonation. |
| 17 | Okamoto (2007, GMM) as M06 state of the art | M06 section | questionable | A 2007 GMM verifier on murmur is not the current state of the art for a learned shared-encoder model. Recent whispered or neural speaker verification work would be the fairer reference (unverified; the reviewer should locate one). |
| 18 | HEar-ID names EER but reports none | Row 14 | correct | It names EER, and the claim of absence is consistent with the reported TPR/FPR. |
| 19 | Youden's J threshold on unnamed data; one run without seeds | Row 15 | partly insufficient | Youden's J is quoted. "One run without seeds" has no supporting quote; t18 only describes the split. The 30 vs 11.45 margin inconsistency is correctly raised. |
| 20 | Enrolls "from a few spellings" (M03) | Row 17 | insufficient quote | The quote covers only manufacturer-supplied impostor data. |
| 21 | Chetty and Wagner: digits 70–90%, verification EER 0.9–1.2%, liveness 0.6–0.8%, held-out impostors (M08) | Row 21 | partly insufficient | All numbers are quoted. The quotes do not show which range is verification and which is liveness (both are labelled "fused audio and lip motion"). Held-out impostors are supported. |
| 22 | Ezz et al.: face authentication plus lip-read silent digits 96.2%; Li et al.: whisper mask, words >92%, 4 users >90% | Row 22 | partly insufficient | The quote does not say what 96.2% at N=10 measures or that the input is digits. Li et al. is a "low-decibel" mask, so "whisper" overstates it. |
| 23 | HEar-ID has no cascade baseline (§4.1.2) | Row 23 | insufficient / location mismatch | The text cites §4.1.2, the table §4.1.1. The quote (t35) describes a recognition baseline and does not support the absence of a cascaded recognizer-plus-verifier. |
| 24 | HEar-ID holds out one session per user | Row 25 | correct | |
| 25 | User-held-out tests predate HEar-ID [11], [2], [3]; read verifiers keep impostors out of training [4], [5] | Row 27 | correct | All five quotes support it. |
| 26 | S3 FPR 19.20%, S9/S10 TPR 0.00%; Fig. 3b means 80.00%/3.27%; S5 98.00% in figure vs 99.9% in text | Rows 29, 30 | insufficient quote | Only the figure caption is quoted, not the per-user values. 81.76%, 3.2% and 99.9% are quoted from the text. The arithmetic is correctly marked (inference). |
| 27 | 24.1 points, 26% relative below 91.4% | Row 28 | correct arithmetic | (91.4−67.3)/91.4 = 26.4%. It is marked inference. The comparison carries the same unknown-baseline-data confound as #6. |
| 28 | "First earable ... silent or whispered speech" refuted except for "earable" | Row 31 | correct as far as the quote goes | [4] and [9] precede it. Earlier earable authentication from speech-related vibration may exist, e.g. MandiPass (2021, earable IMU, vocal vibration) (unverified). Check it before stating that "only 'earable' remains". |
| 29 | M05 usual approach: 16 of 28 Doppler vs 22 ledger matches | M05; Appendix | inconsistency to explain | Two denominators (28 published, 22 ledger) appear in one slot without explanation. State why the published table has 28. |
| 30 | M12 verdict "behind" | M12; Appendix | follows the rules | It names prior user-held-out work ([11], [2], [3]) and prior disjoint-impostor verifiers ([4], [5]) and gives the ledger count (7 of 22). The state-of-the-art cell, however, names the [concurrent] M2SILENT. The prior works should carry the verdict instead. |

## Strongest confound

The central recognition claim compares HEar-ID (fused input, 8 of 11 users, session held out) with an ultrasonic-only baseline whose users, words and split are unknown. The review flags this ("whose split is unstated", plus a question to the authors), yet the Verdict still states "no gain" and "below" as fact. The 91.4% figure also undercuts the review's own M05 argument that audio carries the content.

## Required fixes, ordered by impact

1. Add ReHEarSSE (the authors' earbud-ultrasound spelling system and the source of the 91.4% comparator) to the references. Consider it the M05 state of the art in place of, or next to, HPSpeech, whose 8-command task is not comparable.
2. Remove the contradiction in M05. An ultrasound-only result (the implemented baseline, t35) exists. Say instead that HEar-ID's own model has no single-modality ablation, and soften or drop the inference that audio carries most of the content.
3. Soften the Verdict: "no demonstrated gain over a baseline with unknown data", not "below". Drop "selected" and "post-hoc" unless a quote shows how the 8 users were chosen.
4. Fix "no cascade baseline (§4.1.2)". The location does not match, and the quote (t35) does not support the claim. Quote the passage showing there is no cascaded recognizer-plus-verifier, or rephrase.
5. Quote the Fig. 3b per-user values (S3, S9, S10, S5) that bullets 2–3 of "Where the claims outrun the evidence" rely on.
6. Quote the M2SILENT definition of WER-w and WER-c. Carry the M12 "behind" verdict on the prior works, not the [concurrent] one.
7. Chetty and Wagner: quote which EER is verification and which is liveness.
8. Replace or supplement Okamoto (2007, GMM) as the M06 state of the art with a current neural or whispered speaker-verification result.
9. Explain the 28 vs 22 denominators in the M05 usual approach.
10. Novelty: check earlier earable speech-vibration authentication (e.g. MandiPass, 2021, unverified) before saying "only 'earable' remains".
11. Add quotes or drop the details for: "one ANC-earbud microphone", HPSpeech "8 commands", Zhu "digit", Ezz "digits", "few spellings", "one run without seeds".
12. Li et al.: "low-decibel", not "whisper".
13. Okamoto 5.5%: quote that case A is impersonation.
14. Questions to the authors: keep the baseline-split question, and drop the parallel factual claim that the split is unstated, or quote its absence.

## Scores

- Procedure: 6/10. The claim table is complete, the inference labels are correct and the chronology labels are right. The key comparator is missing from the references, and several details have no supporting quote.
- Final text: 6/10. The position is clear and the evaluation criticisms (shared impostors, no replay test, no EER) are well grounded. There is one internal contradiction, the Verdict wording goes beyond the evidence, and the M05/M06 state-of-the-art choices are weak.

Strengths in brief: the impostor-overlap and missing-EER points are well supported, the 30 vs 11.45 margin inconsistency is a good catch, and the [concurrent]/[later] labels are applied correctly.
