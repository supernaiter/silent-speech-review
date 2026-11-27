# Evaluator: a language model separate from the writer

Target: Ma, Mira, Petridis, Schuller, Pantic, "LiRA: Learning Visual Speech Representations from Audio through Self-supervision", Interspeech 2021 (doi:10.21437/Interspeech.2021-1360; arXiv 2106.09171v1, 2021-06-16). Date of evaluation: 2026-11-27.

Sources checked: the wiki source text of the target (`papers/isca-ma21c-lira/source/text.txt`), the wiki texts of [2] (arXiv 2102.06657), [3] (isca-qu19-lipsound), [5] (arXiv 1911.12747), [6] (arXiv 2406.12233), [10] (arXiv 2212.06246, Table 9) and arXiv 2104.05418; the review's audit files; Crossref and Semantic Scholar metadata for DOIs and the AV-PPC publication date.

Dating: first public 2021-06-16, so the ±6-month window is 2020-12-16 to 2021-12-16. The review's month boundaries (prior before 2020-12, [concurrent] 2020-12 to 2021-12) fit this window. [2] (2021-02), [7] (2021-12-09) are correctly [concurrent]; [6] and [10] correctly [later]; [3], [4], [5], [8], [9] are correctly prior. One mislabel: AV-PPC (see fix 7).

## Claim table

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | PASE+ features regressed with L1 from a frozen encoder (Verdict) | Target Sec. 2.1, Fig. 1 | correct | |
| 2 | 24.5% vs 3.6% at 1% LRW labels (Verdict, M03) | Target Sec. 4.1 | correct | 20.9-point gap correct. |
| 3 | +0.7 on LRW (88.1 vs 87.4, Table 1), +0.3 on LRS2 (38.8 vs 39.1, Table 2) | Target Tables 1-2 | correct | |
| 4 | Prose states 0.8 points (Sec. 4.1) against 0.7 in Table 1 | Target Sec. 4.1 | correct | Real internal inconsistency in the target. |
| 5 | 5.6% relative error reduction; 0.8% relative on LRS2 (inference) | Arithmetic | correct | 0.7/12.6 = 5.6%; 0.3/39.1 = 0.77%. |
| 6 | "The same encoder from scratch already beats every self-supervised row in Table 1" (Verdict) | Target Table 1 | wrong as worded | LiRA-FineTuned (88.1) is itself labelled "Self-supervised" in Table 1 and beats 87.4. The M03 text says "other" correctly; the Verdict does not. |
| 7 | 87.4 is 2.6 points above AV-PPC 84.8; LiRA-Frozen 83.1 (M03) | Target Table 1 | correct (numbers) / insufficient evidence (inference) | AV-PPC's own abstract gives 80.30% "without further finetuning", so 84.8 is most likely a fine-tuned figure; comparing it with the frozen 83.1 mixes protocols. |
| 8 | Most of the 9.5-point gain over TM-seq2seq was reported by [2] (48.3 to 39.1) | Target Sec. 4.2, Table 2; [2] Sec. Results on LRS2, Table 3 | correct | But see fix 1: [2] also reports 37.9% with LRW initialisation, below LiRA's 38.8%. |
| 9 | Authors call the LRS2 gain "a small improvement" (Sec. 4.2) | Target Sec. 4.2 | correct | Properly credited. |
| 10 | PASE+ preferred on an MFCC remark without numbers (Sec. 2.1) | Target Sec. 2.1 | correct | |
| 11 | LipSound not cited; regresses mel spectrograms from lip video, 2019 | Target reference list; [3] abstract | correct | Target cites no Qu et al. work. |
| 12 | LipSound's GRID results are speaker-dependent | [3] Sec. 2 | correct | |
| 13 | LIBS distils a recognizer with ground-truth sentences in the loop | [4] quotes c06, c07 | correct | |
| 14 | KD-seq2seq 51.3% [5]: Jasper-style network, word-level-pretrained front end, 6-gram LM | [5] Sec. 3-5, Table 3 | correct | Missed: the 51.3% row is "CTC + KD, ASR, GT, ASR", i.e. full ground-truth fine-tuning after distillation pre-training, and it is a CTC model; the target's Table 2 labels it "Unsupervised" and "seq2seq" (fix 2). |
| 15 | Authors credit Afouras et al. and name the labelled-ASR dependency they avoid (Sec. 1) | Target Sec. 1 | correct | |
| 16 | LipSound2 pre-trains video-to-mel on about 2,400 h; [concurrent] | [7] abstract; arXiv date 2021-12-09 | correct | Inside the window by one week. |
| 17 | SyncVSR 93.2% LRW, no word boundary, three seeds, 157 h; 5.1 points above 88.1 | [6] Table 1, Sec. 3 | correct (numbers) | Not step-isolated (fix 5). [6] Table 1 also lists LiRA at 590 video hours against SyncVSR's 157. |
| 18 | SyncVSR ± 0.1 over three seeds (M12 SOTA) | [6] Table 1 caption, Sec. 3 | correct | Appropriate for the repetition step. |
| 19 | RAVEn 23.2% LRS2 WER, 1,759 h unlabelled, 223 h labelled, no LM; 15.6 points below 38.8 | [10] Table 9 | correct (numbers) / not like-for-like | [10] Table 9 has RAVEn Base with the same 433 h unlabelled as LiRA: 32.1% (fix 4). |
| 20 | 18-fold data claim, 76 h vs 1,362 h (Sec. 4.2) | Target Sec. 4.2; [2] Table 3 (730 + 632 h) | correct | The comparison with LiRA-Supervised at 36% is plotted in Fig. 4b, though not given as a number (fix 11). |
| 21 | Authors report scratch training degrades beyond 18% of LRS2 labels | Target Sec. 4.2 | correct | The "optimisation failure" reading is the authors' own ("hard to optimise without a good initialisation"), see fix 9. |
| 22 | "No external labelled datasets" against an LM on LRS2, LRS3 and LibriSpeech text without stated partitions | Target Sec. 3.5, Sec. 4.2; [2] Language Model paragraph | correct for the target / partly answered | [2] states the LM uses LRS2/LRS3 pre-training and training sets plus LibriSpeech training transcriptions (fix 10). |
| 23 | M02 usual approach 2 of 3 prior; regression of a self-supervised encoder's features 0 | Audit M02 counts; [3], [4], [5] | correct (as screened) | Labelled pattern match, screened; denominator at the target's time. Concurrent population misses cvf-kim21-mabm (fix 8). |
| 24 | M03 usual approach 2 of 3 contrastive or synchronisation; AV-PPC also contrastive | Audit M03 counts; AV-PPC abstract | correct (design) / chronology wrong for AV-PPC | AV-PPC was first published 2021-01-10 (ICPR 2020 proceedings), so it is [concurrent], not prior (fix 7). arXiv 2104.05418 was wrongly excluded as "no lip reading" (fix 8). |
| 25 | M12 30 of 30 prior LRW systems report no run spread | Audit M12; spot check of six listed texts (2001.08702, 2007.06504, 2009.14233, 2003.03206, 1805.12371, 2006.08599) | correct (spot check) | No spread wording found in the spot-checked texts. |

## Required fixes, ordered by severity

1. **Major. Location:** Verdict ("most of the 9.5-point LRS2 gain ... [2]") and M03 body. **Evidence:** [2], Results on LRS2 and Table 3: "In case, we use the pre-trained LRW model for initialisation the WER drops further to 37.9 %"; also row "Ours (V) LRW (157) + LRS2 (224) 37.9". [10] Table 9 repeats 37.9 for Ma et al. (2021b). The target's Table 2 leaves out this row, and only the qualifier "when no external labelled datasets are used" (Sec. 4.2) lets 38.8% count as state of the art. **Fix:** Say that the authors' concurrent paper already reaches 37.9% using word-level LRW labels for the front end, a lower WER than LiRA's 38.8%. Say that the LRS2 state-of-the-art claim rests on leaving that row out under the "no external labelled datasets" qualifier. Give this as a citation of [2] with its location. This makes the review's central position stronger.

2. **Moderate. Location:** M02 body (KD-seq2seq sentence). **Evidence:** [5] Table 3 and Sec. 5: 51.3% is the row "CTC + KD, ASR, GT, ASR", described as "training on each dataset with full supervision after unsupervised pre-training". The model is CTC-based, not seq2seq. The target's Table 2 labels it "KD-seq2seq [3] Unsupervised". **Fix:** Add that the target mislabels this comparator: it is fine-tuned on ground-truth transcripts and it is not a seq2seq model. Present this as an inconsistency in the target, located in Table 2.

3. **Moderate (bibliographic). Location:** Reference 2 and the .bib entry. **Evidence:** Crossref gives 10.1109/ICASSP39728.2021.9414567 for "End-To-End Audio-Visual Speech Recognition with Conformers". The DOI in the review, 10.1109/ICASSP39728.2021.9413459, resolves to "Adaptive Subsampling of Multidomain Signals with Product Graphs". **Fix:** Replace the DOI in the .md and the .bib. Also consider adding DOI 10.1109/ICASSP40776.2020.9054253 to [5].

4. **Moderate. Location:** M03 State of the art line and table row. **Evidence:** [10] Table 9: "RAVEn (Base) Transformer 433 223 32.1". LiRA's own row in the same table is "Ma et al. (2021a) Conformer 433 223 38.8". The Large 23.2% figure changes both model size and unlabelled hours (1,759 h against 433 h). **Fix:** Lead with RAVEn Base: same 433 h unlabelled LRS3, 223 h labelled, 32.1%, 6.7 points below LiRA. Keep Large 23.2% as the best figure, and state LiRA's 433 h and its LM use next to it so the conditions that decide the result are explicit.

5. **Moderate. Location:** M02 State of the art line and "What the field needs next" (M02). **Evidence:** [6] Table 1 already compares audio-token targets with ASR pseudo-label "Transcription Alignment" on one Transformer: 93.2 against 93.1, which the authors of [6] call "trivial". [6] Table 4 isolates the audio-reconstruction step on LRS2: 45.9 to 38.1 WER without CTC and 43.2 to 30.7 with CTC. [6] Table 1 also gives "Training Strategy + LiRA, DC-TCN, 595 h, LRW(WB) 92.3" against "Training Strategy 92.1". That is later evidence that LiRA pre-training adds 0.2 points under a stronger recipe. **Fix:** Cite one of these step-level contrasts in the SOTA line, not only the 93.2% system figure. Change the M02 "needs next" item so that it credits [6] for the recognizer-versus-audio-token comparison already done, and keeps only the parts not yet done (PASE+ and mel against tokens on one encoder at 1% to 100% labels). The 92.1 to 92.3 figure supports the review's "standard" verdict, and the review should use it.

6. **Moderate. Location:** M03 body ("LiRA-Frozen, the row that tests the representation, gives 83.1%" against AV-PPC 84.8). **Evidence:** The AV-PPC abstract (ICPR 2020, doi:10.1109/ICPR48806.2021.9413295) reports 80.30% on LRW "without further finetuning". The 84.8% in the target's Table 1 is therefore most likely a fine-tuned figure (insufficient quote: the target gives no protocol). Target Sec. 4.1: 83.1% is the best of eight layers in Fig. 3, and the selection split is not stated. **Fix:** Do not set frozen 83.1 against a probably fine-tuned 84.8. Either compare frozen with frozen (83.1 against 80.3, different backbones) or keep only the backbone argument (87.4 from scratch above 84.8). Add that the frozen figure is a best-layer selection with no stated selection split.

7. **Minor (chronology). Location:** M03 Usual approach ("AV-PPC ... is also contrastive") and the M03 Appendix line. **Evidence:** Semantic Scholar and Crossref give publication date 2021-01-10 (ICPR 2020 proceedings), and no earlier preprint was found. **Fix:** Label AV-PPC [concurrent] and keep it outside the prior denominator, as the Appendix count already does. The text should not suggest that it is a prior.

8. **Minor (population). Location:** Appendix, [concurrent] counts for M02 and M03. **Evidence:** arXiv 2104.05418 (Ma, Zeng, McDuff, Song, "Contrastive Learning of Global-Local Video Representations", 2021-04) evaluates on LRW and LRS2 (Sec. 4.1, Table 1), but the M03 audit excludes it as "general video representations, no lip reading". cvf-kim21-mabm (Kim et al., ICCV 2021, audio memory recalled from video; LRW 88.5 in [6] Table 1) is in the M02 candidate list but appears in neither the concurrent nor the excluded list. **Fix:** Add both to the [concurrent] tallies: M03 then has 2 concurrent (contrastive 1, mel regression 1), and M02 has 4 concurrent (distillation 2, memory 1, mel regression 1). Prior counts are unchanged.

9. **Minor (fairness). Location:** M03 body ("Label efficiency is the real result") and "Where the claims outrun the evidence", bullet 3. **Evidence:** Target Sec. 1, contribution 2 ("particularly beneficial for smaller labelled datasets"), and Sec. 4.1 ("particularly beneficial when the labelled training set is very small"). Sec. 4.2: "LiRA-Supervised is hard to optimise without a good initialisation". **Fix:** Credit both points to the authors with these locations. The review's own contribution is the contrast with the full-label gain and the optimisation confound in Fig. 4b.

10. **Minor. Location:** M12 body (LM "without stated partitions") and Questions for the authors (LM). **Evidence:** [2], Language Model paragraph: the LM is trained on "the training transcriptions of LibriSpeech (960 h), pre-training and training sets of LRS2 and LRS3". **Fix:** Note that the followed recipe states the partitions. Keep the real point: the LM is trained on transcripts of external labelled corpora (LRS3, LibriSpeech), which weakens "no external labelled datasets".

11. **Minor (wording). Location:** Verdict ("beats every self-supervised row in Table 1") and "Where the claims outrun the evidence", bullet 2. **Evidence:** Target Table 1 labels LiRA-FineTuned "Self-supervised". Fig. 4b plots LiRA-Supervised and LiRA-Supervised (CL) at 36% of LRS2. **Fix:** Write "every other self-supervised method". Write that the 18-fold claim is not given against LiRA-Supervised as a number, rather than saying the comparison is absent.

Not required (unverified outside knowledge): Chung and Zisserman, "Out of time: automated lip sync in the wild" (ACCV 2016 workshops), is, to the evaluator's knowledge, a synchronisation-pretrained network that was also applied to lip reading. It is not in the wiki. If confirmed, it adds a third prior to the M03 contrastive or synchronisation design. The target's own Table 1 also shows the authors' supervised DC-TCN [17] at 88.4%, above LiRA-FineTuned's 88.1%, which the review could mention.

The other checks raised in the evaluation request are satisfied. Owens and Efros (2018), Shukla et al. (2020) and the video-to-speech systems are rightly outside the decoder population. AV-HuBERT is [later] and is not used as a prior. The 2, 0 and 30 counts are labelled as pattern-match, screened design counts with denominators at the target's time. The published text has no disclaimers, process narration or model names, and it is English only.

## Scores

- Procedure: 7/10. Dating is correct, priors were read in full and screened populations are labelled. Deductions: one prior and one concurrent work were misclassified, two concurrent studies are missing, and neither SOTA line uses the step-level or like-for-like figure that its own source provides.
- Final text: 7/10. The numbers against the target are accurate and the main position is sound and well located. Deductions: the review missed the 37.9% result in the authors' concurrent paper and the mislabelled 51.3% comparator, one reference has a wrong DOI, and two of the review's findings are the authors' own statements.

## Final counts by severity

- Critical: 0
- Major: 1
- Moderate: 5
- Minor: 5
