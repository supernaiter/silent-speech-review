# Evaluation: Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading

Date: 2026-11-22. Independent evaluation pass, claim table and review positions only; sources not re-opened. "Insufficient evidence" means the claim-table quote does not show the number or condition, not that the claim is false.

## Claim checks

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Verdict: fusion cuts silent WER from 54.5% (best lip-only) to 40.5% (Table III) | Row 2, t33f, t33g | correct | Lip-only without masking 54.5; full model 40.5. Lip-only with masking is worse (about 57.2), so 54.5 is the best lip-only model. |
| 2 | Verdict: "six laryngeal speakers"; §V-E "three laryngectomized speakers" | Rows 2, 19 | insufficient evidence | No quote gives either speaker count. |
| 3 | Verdict: masking's clean gain of 3.5 points, which "the authors call not significant (§V-B)" | Row 3, t33g, t33i, t41 | insufficient evidence | 44.0 - 40.5 = 3.5 is right. No quote shows the authors calling the multimodal gain not significant. t41 is about unimodal settings, and t40 calls the lip-only 2.7-point *degradation* not significant. This may be a conflation. |
| 4 | Verdict: masking "never tested against whole-stream dropout" | Rows 11, 22, t77 | insufficient evidence | Both the masked and unmasked models keep a video dropout of up to 75%, "similar to prior audiovisual" work (t77). If that dropout removes the whole video stream, then whole-stream dropout is present in both arms. The review asks this as a question (row 22) but states the conclusion as settled. |
| 5 | Verdict: capacity confound, 46.9% WER with sEMG zeroed; 7.6 of the 10.5-point lead needs no sEMG | Row 4, t34a, t33f | correct (arithmetic); column mapping insufficient evidence | 54.5 - 44.0 = 10.5 and 54.5 - 46.9 = 7.6. The quote does not show the column headers that put 46.9 under "sEMG removed" and 92.5 under "lips removed". The mapping is plausible against the unimodal results. Labelled inference, which is appropriate. |
| 6 | Verdict / M12: test speakers all seen in training; splits are text-disjoint and speaker-overlapping (§IV-A) | Rows 15, t59 | insufficient evidence | t59 gives only a 20/70 sentence split. No quote states the speaker overlap, and that overlap carries the "behind" verdict. |
| 7 | Verdict: laryngectomized gain not significant (§V-E) | Row 19, t36b, t36c, t51 | correct | 68.2 against 75.1, and t51 is the authors' own statement. |
| 8 | M05 usual approach: two earlier fused decoders, digits [2] and 100 sentences [3] | Row 5, c7, c3 | correct for digits and classification; "100 sentences" insufficient | c3 confirms sentence-level classification, but no quote shows the sentence count. |
| 9 | M05 SOTA: AVE Speech 95.51% on unseen subjects, three-stream, at -10 dB, below visual-only 98.55% | Row 6, c4, c5 | partly correct | 95.51 (fusion, test) and 98.55 are quoted. Neither the -10 dB condition nor the fact that 98.55 is the *visual-only* model appears in the quotes (c5 says only "which achieves"). |
| 10 | M05 SOTA: GETS 11.89% WER, silent EMG-to-speech, English Gaddy corpus [concurrent] | Row 6, c13 | insufficient evidence | The quote is cut off at "on the". It does not show the silent condition or the corpus. The [concurrent] label fits the dates (Interspeech 2026 against a June 2026 target). An 11.89% WER for EMG-to-*speech* on silent Gaddy data would be far below earlier synthesis results, so confirm it is not an EMG-to-text figure. |
| 11 | M05 SOTA framing: AVE Speech as state of the art for fusion | Row 6 | judgment questionable | Its fusion model scores below its own visual-only model, and the metric is closed-set sentence accuracy, not synthesis WER. That makes it a weak state-of-the-art reference. The review does give the gap, which keeps the line honest. |
| 12 | M05: earlier gains "14.5% relative over video and 2.4% over EMG" [2] | Row 8, c8 | number correct; "relative" insufficient | c8 says "improves the results ... by 14.5%" and does not say whether that is relative or absolute. |
| 13 | M05: target gain 14.0 points (25.7% relative) | Row 8 | correct | 54.5 - 40.5 = 14.0, and 14.0 / 54.5 = 25.7%. |
| 14 | M05: AVE fusion fell below vision once audio degraded; "the unmasked target model repeats this" (92.5% with lips removed against 83.2% sEMG-only) | Row 9, t34a, t33c | numbers correct; judgment wrong | These are two different effects. AVE Speech shows fusion below its best single stream with all inputs present. The target shows a fused model degrading when one input is missing. With both inputs present, the target's fusion (44.0) beats both single streams. |
| 15 | M05 verdict ahead: ledger count, deciding priors, effect repeated | Rows 7, 23, 24 | meets rule | 20 pattern-match studies, 2 confirmed, deciding priors [2] and [3] named, and the 14.0-point effect repeated. I know of no earlier speech synthesis from fused sEMG and lip video, although ultrasound-plus-lip synthesis exists and does not count. The capacity confound (#5) weakens the effect but the verdict is scoped to "six laryngeal speakers". |
| 16 | M03 usual approach: modality dropout in "38 of 44 matching studies" | Rows 10, 27, 28 | contradiction | Appendix row 27 gives "21 unique studies pattern match" for M03, while the body says 44 matching studies. Reconcile. |
| 17 | M03: spans of up to 0.4 per one-second chunk (§III-C) | Row 11, t21 | insufficient evidence | t21 says only "When Mm = 0, no masking is applied." The 0.4 ratio and the one-second chunk are not quoted. |
| 18 | M03 verdict "standard" | Section M03 | judgment inconsistent | The usual approach is given as whole-stream dropout and the target is said to differ ("span masking instead of modality dropout"). No prior that uses per-stream time-span masking is cited, so "standard" has no deciding prior. Either cite span or time masking priors, or justify the verdict another way. |
| 19 | M03 SOTA line: AV-HuBERT [5] | Row 12, c9, t76 | incomplete | It gives no year-metric-value for [5]. The line reports the target's own numbers instead. More recent robust audio-visual pre-training exists (for example RAVEn, ICLR 2023; BRAVEn, ICASSP 2024), but neither is a direct modality-dropout comparator. |
| 20 | M03: masking moves lips-removed WER from 92.5% to 73.7% and sEMG-removed WER from 46.9% to 48.2% | Row 12, t34a, t34c | correct | Matches the quotes, under the column mapping noted in #5. |
| 21 | M03: frame-rate augmentation costs 13.3 points (57.3 against 44.0) | Row 13, t34b, t34a | correct | This is plain arithmetic on Table IV, so the "(inference)" hedge is unnecessary. |
| 22 | M03: masking worsens sEMG-only by "about 10 points" and lip-only by 2.7 | Row 14, t40, t44 | 2.7 correct; 10 insufficient | t40 gives 2.7 and calls it not significant, but the review leaves that out. No quote shows about 10 for sEMG. The concession in t44 is correctly attributed to the authors. |
| 23 | M12 verdict "behind" | Rows 15, 17, 18 | judgment contradicts own counts | By the review's own tallies, 52/165 studies hold speakers out and 78/165 run listener tests, so both are minority practices. Seen-speaker, ASR-scored evaluation is the majority. Speaker-dependent evaluation is also the norm in sEMG-to-speech work on single-speaker corpora. "Behind" needs a rule-based basis or should be "standard". |
| 24 | M12 SOTA: V2SFlow 28.5% WER, LRS3, unseen speakers | Row 16, c11, c12 | number correct; SOTA status unverified | 28.5 is quoted, and c12 confirms the unseen split. Check whether later lip-to-speech work reports lower LRS3 WER, for example LipVoicer (ICLR 2024), which I recall reports a lower WER. That recollection is not verified. |
| 25 | Outrun list: 101.7M against 55.6M parameters (§IV-B) | Row 20, t55 | insufficient evidence | The quote shows 46.1M and 55.6M only. 101.7M equals their sum, so either quote the multimodal count or mark it as computed. The "Table IV names no test cohort", unitless bitrate and unstated Whisper normalization claims have no quote or checked location (absence claims). |

## Required fixes, ordered by impact

1. Verdict: support "a clean gain of 3.5 points the authors call not significant (§V-B)" with a quote about the multimodal gain, or remove it. The only significance quote (t40) is about the lip-only degradation.
2. M12: the "behind" verdict contradicts the review's own counts, since speaker hold-out (52/165) and listener tests (78/165) are minority practices. It also ignores the speaker-dependent norm in sEMG-to-speech. Restate the verdict on a basis the verdict rules allow, or change it to "standard".
3. M03: reconcile "38 of 44 matching studies" with the Appendix's "21 unique studies pattern match".
4. M03: the "standard" verdict has no deciding prior for per-stream span masking, and the section calls the method "instead of" the usual approach. Cite span or time masking priors, or revise the verdict.
5. Verdict and M03: check whether the 75% video dropout in both arms removes the whole video stream (§IV-D). If it does, "never tested against whole-stream dropout" is wrong. If it does not, say so with a quote.
6. Add a quote from §IV-A for speaker overlap between train and test, and for the six laryngeal and three laryngectomized speaker counts. These carry the M12 verdict and the "six laryngeal speakers" scope of M05.
7. M05: the claim that the target "repeats" AVE Speech's below-vision fusion conflates two effects (a full-input fusion deficit against a missing-input degradation). Reword or drop it.
8. M05 SOTA: add quotes for the -10 dB condition and for 98.55% being visual-only. State that it is closed-set accuracy, not synthesis.
9. M05 SOTA: replace the truncated GETS quote with one that shows the silent condition, the Gaddy corpus and that the figure is for synthesized speech, not text. Verify the venue and DOI.
10. M03: quote the 0.4 span ratio and the one-second chunk. t21 does not show them.
11. M03: quote the sEMG-only degradation (about 10 points), and say that the 2.7-point lip-only degradation is not significant (t40).
12. Outrun list: quote the 101.7M multimodal parameter count or mark it as the sum of the two branches. Give the checked locations for the Table IV cohort, the bitrate units and the Whisper normalization absence claims.
13. M05: confirm that [2]'s 14.5% and 2.4% are relative improvements before labelling them "relative".
14. M03 SOTA line: give a year-metric-value for the cited state of the art, or reframe the line as the closest cited prior.
15. M12 SOTA: check later lip-to-speech LRS3 results (for example LipVoicer, ICLR 2024) against V2SFlow's 28.5% WER before calling it the state of the art.
16. Drop the "(inference)" hedge on the 13.3-point arithmetic, which is a direct calculation from Table IV.
17. "What the field needs next", M05 item: [3] (c2, no subject overlap) does not support "reported per speaker". Drop the citation or quote a per-speaker report.

## Scores

- Procedure: 6/10. The claim table covers every number, but several quotes are truncated or do not contain the stated value or condition. One count contradicts the Appendix.
- Final text: 6/10. The target-paper numbers and arithmetic are accurate and the capacity confound is well chosen. The M03 and M12 verdicts are not carried by the review's own evidence, and one central sentence (the 3.5-point significance claim) has no support.

The central confound, capacity (7.6 of the 10.5-point lead remains with sEMG zeroed), is identified and correctly hedged. The review attributes the authors' own caveats (t44, t51) to them rather than presenting them as its own findings. No later work is treated as prior work.
