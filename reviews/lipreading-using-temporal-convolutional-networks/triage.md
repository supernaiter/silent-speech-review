# Triage of the evaluation (14 required fixes)

| # | Verdict | Evidence | Where applied |
|---|---|---|---|
| 1 | applied | slots.json used whole-wiki slot-filled counts (n = 7,388) for inherited slots; no Appendix entry covers them. | Component table: inherited and not-applicable slots carry no count (matched = null); M03, M06 and M12 keep design counts with their LRW population (n = 156 / 155) named in the cell; "Offline (82)", "Not recorded (119)", "Not counted (234)" removed. |
| 2 | applied | Target §5.3 ("achieves the same robustness as the BGRU model", d3) and §6 (d4) already credit the augmentation. | "Outrun" robustness bullet removed and replaced by the fixed-length-TCN confound; the Verdict now says the authors report it (§5.3). |
| 3 | applied | Table 2: variable-length TCN 85.30 vs variable-length BGRU 82.40 (t42, t48); no fixed-length TCN row; [2] Sec. 3 uses word boundaries, the target's variable-length augmentation (d8) and a four-layer 1024-unit BGRU (d9). | Verdict, M06 evidence (matched +2.9, inference; [later] 90.0 vs 89.7 with conditions), M12, new "outrun" bullet on the 0.7-point unmatched lead. |
| 4 | applied | Abstract "train the model in one single stage" (d1) vs §4.2 "we adopt this pre-training strategy" (d2); "from scratch" in [2] means no external data, so the old criticism was misaimed. | Verdict and M03 describe the recipe as a 50-word warm-up then cosine training; M03 criticism re-aimed at the Abstract; table M03 choice. |
| 5 | applied | The target (§5.1, t65) and [2] (Tables 1-2) state no run count. | "single run(s)"/"one run" replaced by "no run count / run count not reported" in Verdict, M06, M03, M12, table notes, What next, verdict.json. |
| 6 | applied | Afouras et al. 2018 (arXiv 1806.06053) is in the wiki and was read: 10- and 15-layer depth-wise separable temporal convolution stacks with shortcuts, sentence level (LRS2), no dilation described in Sec. 2.3 (d14). | M06: depth stated as prior [@afouras2018deeplip]; novelty limited to multi-scale branching under the searched pattern; Appendix states depth and dilation were not searched. |
| 7 | applied | Weng and Kitani Table 2 (a) 1D TC 70.85 vs (b) Bi-LSTM 78.77 test, and Sec. 7.2 conclusion (d6, d7). | M06 prior count 7 studies (6 by pattern + [5]), cited with its numbers; Appendix and audit note record the lower bound. |
| 8 | applied | [2] Table 2 Student 2 92.8 (Scratch), Ensemble 93.4, with the target's variable-length augmentation (d8, d10, d11). | M03 State of the art now 92.8% (93.4% ensemble) and says the recipe keeps the target's cropping; M03 audit state_of_the_art and table cell updated. |
| 9 | applied | SyncVSR "leverages quantized audio" and vq-wav2vec tokens (d12, d13). | "LRW-only" removed; Verdict says it trains on LRW video with quantized audio-token targets. |
| 10 | applied | M12 audit: the 90 is the ResNet-18 front-end pattern count; 95.0 is with word boundaries (c19, c20). | M12 usual-approach line and table cell relabelled; table SOTA reads "95.0% LRW (WB)"; M12 text gives 93.2 without and 95.0 with WB. |
| 11 | applied | [6] Table 3: N4 78.4% uses N2's fixed front end (d5); N7 adds end-to-end training. | M06 uses the matched N2 74.6% vs N4 78.4%. |
| 12 | applied | M06 and M03 audit notes list the target among the 2 [concurrent] hits. | M06 "(the target and [8])"; Appendix "including the target" for both topics; the prior frame-dropping hit is named ([7]). |
| 13 | rejected | Wiki manifests for arXiv 2001.08702 and 2209.01383 hold arXiv versions only, and no venue version is in the wiki index. | References stay arXiv preprints. |
| 14 | applied | Published table recall 0.75; this run's audit 1.0 (4 of 4 seeds). | Appendix M12 states both. |

Counts: 14 findings; 13 applied, 1 rejected, 0 unverified. Afouras et al. 2018 added as a read prior (6 papers read besides the target).
