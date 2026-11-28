# Evaluator: a language model separate from the writer

Date: 2026-11-28. Target: Xu, Li, Cassimatis, Wang, "LCANet: End-to-End Lipreading with Cascaded Attention-CTC", IEEE FG 2018, arXiv:1803.04988 (v1, 13 Mar 2018; the only arXiv version, checked on the abs page).
Review evaluated: `lcanet-end-to-end-lipreading-with-cascaded-attention-ctc.md` (identical to `draft-before-evaluation/review.md`), with `claims.md`, slots/verdict/plan JSON, the two `.audit` files, `tools/*.json` and `ext/` (Kim 2017, Hori 2017).
Sources re-read: wiki `papers/arxiv-1803.04988/source/paper.pdf` and `text.txt` (Table III checked on the rendered PDF page 7, not only on the text extraction), `arxiv-1611.01599` (LipNet v2), `arxiv-1611.05358` (WAS), `arxiv-2403.16071` (Wu et al.), `arxiv-2602.19316` (Haliassos et al.), `aaai-38133-linprovsr`, `arxiv-1806.06053`, `ext/kim2017`, `ext/hori2017`; arXiv API for arXiv:1803.05563 and an attention+CTC title/abstract search.

## Claim table

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Dating: first public 2018-03 (arXiv v1, 13 Mar 2018); [concurrent] 2017-09 to 2018-09 (plan, Appendix) | arXiv abs page; text.txt p.1 stamp | correct | Only v1 exists; FG 2018 is later. |
| 2 | LCANet = 3D-CNN + highway + Bi-GRU encoder, attention before a single CTC loss (Verdict) | Sec. 3.A, 3.B.2, Table I, Table II caption | correct | |
| 3 | "Table III puts that system's [LRSW] 3.0% WER in the CER column" (Verdict; Where-claims bullet 1; verdict.json; Questions bullet 3) | Rendered PDF p.7, Table III; `pdftotext -layout` | **wrong** | On the page, LRSW's 3.0 sits under **WER %**, CER blank. The writer's reading comes from the pypdf text, which loses columns. |
| 4 | LRSW 3.0% is GRID WER after one epoch of fine-tuning from LRS; no GRID CER exists for it (Where-claims bullet 1) | WAS Table 8 ("Word error rates on external lip reading datasets": LRW 23.8%, GRID 3.0%), Sec. 5.4 | correct | So "better CER and WER" (Sec. 4.D) has no CER comparator. This part of the bullet stands. |
| 5 | Abstract 3.0% WER vs Table III 2.9%; 37.5% gain over LipNet matches 3.0 (Where-claims bullet 2) | Abstract; Sec. 4.D; Table III | correct | (4.8−3.0)/4.8 = 37.5%; with 2.9 it would be 39.6%. |
| 6 | Highway gain stated 1.1 points; Table III gives 4.1 vs 2.9 = 1.2 (Where-claims bullet 2) | Sec. 4.D; Table III | correct, incomplete | 4.1 − 3.0 = 1.1: the highway figure also comes from 3.0, so every number in the prose uses 3.0 and only Table III uses 2.9. The review does not link the two (see fix M2). |
| 7 | 12.3% gain names no metric or comparator (Abstract) | Abstract; Table III | correct | No pair in Table III gives 12.3% under CER, WER or BLEU (evaluator arithmetic). |
| 8 | A-CTC, called "the attention-only model", still trains on CTC alone (M06) | Sec. 4.D; Table II caption ("AH-CTC, H-CTC, and A-CTC use only the CTC loss function") | correct; quote too thin | claims.md cites the Table III row, not the Table II caption that proves it. |
| 9 | H-CTC 4.3% → LCANet 2.9%, 33% relative (M06) | Table III | correct | 32.6%. |
| 10 | AH-CTC-CE 4.9% worse than H-CTC 4.3%; λ tried from 0.1 to 0.9, best reported, selection data not stated (M06; Where-claims bullet 3) | Table III; Sec. 4.C eq. 11 | correct | |
| 11 | Kim 2017: joint model outperformed both CTC and attention, best at λ = 0.2 (M06) | ext/kim2017 Sec. 3.3, Table 1 | correct | CER, CHiME-4 and WSJ, λ ∈ {0.2, 0.5, 0.8}, no lexicon or LM. The target's comparator follows Hori [43], not Kim (see L4). |
| 12 | Hori 2017: shared encoder trained jointly on CTC and attention; cascade avoids tuning the weight (M06) | ext/hori2017 Fig. 1 caption; target Sec. 2.A | correct | Authors' own rationale, credited with location. |
| 13 | Usual approach: 57 decoder studies before 2018-03; HMM 56 (mentions); "the 5 neural ones" train one loss, CTC 4, attention 1 (M06) | audit `counts_lcanet`, `tools/seqobj_2018-03.json` | counts correct; **label wrong** | 89 − 32 = 57 checks. But the 57 include other neural decoders: Wand 2016 LSTM, Wand 2017 domain-adversarial, Petridis & Pantic 2017 multi-view, Tatulli 2017 CNN, Thangthai 2017 DNN-HMM, Miao 2016, Ninomiya 2015, the PCANet+LSTM tandem (1710.07161). The 5 are the end-to-end sequence decoders, not "the neural ones". |
| 14 | Table cell "CTC: 4 of 5 neural decoders, 57 studies (pattern match 4)"; slots.json matched 4, n 57 (M06 row) | slots.json; audit `usual_approach_lcanet` (n 56, HMM) | insufficient | The denominator is ambiguous: 4/5 in the text, 4/57 in the JSON, and the audit's usual approach is n=56 (HMM). |
| 15 | No cascade or hybrid among the 57; recall check finds none to 2018-09 (Verdict; Appendix) | audit `recall_check_lcanet`; `tools/recall_cascade.py` | correct for lip reading, with caveats | The code cuts at < 2018-09, so September 2018 is outside it, but the text says "to 2018-09". In that month the wiki holds Afouras et al. Deep AVSR (arXiv:1809.02108, 6 Sep 2018, separate CTC and seq2seq) and Petridis et al., hybrid CTC/attention AVSR (arXiv:1810.00108, 28 Sep 2018). In audio ASR, Das et al. (arXiv:1803.05563, 15 Mar 2018, ICASSP 2018) put attention inside CTC [concurrent]. An arXiv search found no earlier ASR cascade (evaluator search; unverified beyond arXiv). |
| 16 | GRID state of the art: 1.83% WER, same 255-per-speaker protocol, no external LM, hybrid CTC/attention (M06; M12; table cells) | Wu et al. Sec. 3.2 ("without using external language model"), Table 4, Sec. 3.4 | number correct; **not the best GRID result** | The wiki holds LinProVSR (AAAI 2026) at 0.99% GRID WER, with CFLip (2025) at 1.01% and LipFormer (2023) at 1.45%. The 24,750/8,250 split (250 test per speaker) is not the 255 draw, and its split type is not named. The M12 audit's own `state_of_the_art` is that 0.99%. The table cells drop the "same protocol" condition. |
| 17 | LRS3 visual-only state of the art 17.6% (2026) (M06) | Haliassos et al. Sec. 6, Table 7 | number correct; **not the best, conditions missing** | 17.6% uses LRS2+LRS3 labelled data (656 h) plus 2,649 h unlabelled, with no external LM. The same source's Table 7 lists LP Conformer at 12.8% (100,000 h labelled, no LM), SynthVSR at 16.9% and ViT3D-CM at 17.0%. It is also a different corpus and protocol from the slot's GRID step. |
| 18 | 37% below 2.9% (M06) | arithmetic | correct | (2.9−1.83)/2.9 = 36.9%. |
| 19 | LipNet overlapped: 4.8% with a character 5-gram LM, 5.6% without (Baseline-NoLM); unseen 11.4% (M12) | LipNet Table 2, Sec. on baselines, App. A.1 | correct | Baseline-NoLM is "Identical to LipNet, but with the language model used in beam search disabled." The 48% relative is correct. |
| 20 | "The paper does not state whether test speakers appear in training (Sec. 4.A)" (M12) | Sec. 4.A | **wrong / contradictory** | "255 sentences of each speaker are used for testing" after a random train/val/test division means every speaker is in both splits. The review's own Verdict calls the setting "overlapping speakers". |
| 21 | M12 usual: 14 GRID decoders, overlapped 8, unseen 7, variability 6, seeds 0 (mentions); 4 later studies with the 255 protocol | M12 audit `counts_lcanet` | correct | 24 − 5 − 5 = 14 checks. |
| 22 | Afouras 2018 [concurrent] trains CTC and attention back ends separately (M06) | arxiv-1806.06053 Sec. 1, Sec. 2 (recurrent and convolutional CTC; Transformer seq2seq) | correct; quote too thin | The quote "We select two models that use CTC" does not show the attention back end. |
| 23 | Faster convergence: Kim reports early convergence; Fig. 6 compares only against LipNet (Where-claims bullet 4) | Kim Sec. 3.3; target Sec. 4.E, Fig. 6 | correct | Fig. 6 caption says "#iteration", the text says epochs (target inconsistency, not raised). |
| 24 | "Not statistically significant" without a test (Sec. 4.F); authors concede the CTC loss is unmodified (Sec. 5) | target Sec. 4.F, Sec. 5 | correct | The Sec. 5 caveat is credited to the authors. |
| 25 | M07 "not reported" | target Sec. 3–4, Fig. 2 | correct | No LM, lexicon or grammar is described for decoding, while the LipNet comparator uses an LM. The verdict is justified. |

## Required fixes, ordered by severity

**C1. Critical. The LRSW "CER column" claim is false.**
- Location: Verdict ("because Table III puts that system's 3.0% WER in the CER column"); verdict.json `short` and `position`; Where-claims bullet 1 ("Table III lists LRSW as "3.0" under CER with WER blank"); Questions bullet 3 ("What is the source of the LRSW CER of 3.0"); claims rows 3, 18 and 28.
- Evidence: in the rendered PDF of arXiv:1803.04988v1 (p.7, Table III), the LRSW row has CER blank, WER 3.0 and BLEU blank. Only the pypdf text loses the column. WAS Table 8 gives 3.0% GRID WER.
- Fix: delete the mislabel claim everywhere. Restate the valid point. LRSW reports only a GRID WER, 3.0%, after pre-training on LRS and one epoch of GRID fine-tuning; the authors state the pre-training themselves (Sec. 4.D). So the claim of "better CER" has no comparator, and the WER comparison is 2.9 against 3.0 from one run each. The authors' own prose works from 3.0, which is a tie (see M2). Rewrite the Verdict sentence on this basis. Drop the CER half of Questions bullet 3 and keep the 12.3% half.

**H1. High. The GRID state-of-the-art line is not the best GRID result in the wiki, and the table cells drop its condition.**
- Location: M06 and M12 "State of the art" lines; table cells M06 and M12 ("[4] 1.83% GRID overlapped"); Verdict ("the later best result under the same protocol").
- Evidence: `aaai-38133-linprovsr` Table 3 gives 0.99% GRID WER (LinProVSR, 2026), and in the same table CFLip (2025) gives 1.01% and LipFormer (2023) 1.45%. They use a 24,750/8,250 split (250 test utterances per speaker, 33 speakers; split type not named). The published M12 audit's `state_of_the_art` is this 0.99%.
- Fix: report 0.99% (LinProVSR, 2026, [later]) as the lowest GRID WER, with its split. Keep 1.83% as the best result on the exact 255-per-speaker, no-LM protocol. In the table cells, write "1.83% (255-per-speaker protocol)" or give both.

**H2. High. The LRS3 state-of-the-art line has no conditions and is not the best even in its own source.**
- Location: M06 "State of the art" ("17.6% LRS3 visual-only WER with hybrid CTC/attention (2026, [later])").
- Evidence: Haliassos et al. 2026 get 17.6% with LRS2+LRS3 labelled data (656 h) plus 2,649 h unlabelled, no external LM, one model for all modalities. Their Table 7 lists LP Conformer at 12.8% (100,000 h labelled, no LM), SynthVSR at 16.9% and ViT3D-CM at 17.0%.
- Fix: state the conditions (labelled and unlabelled hours, no LM) and call it the best under public labelled data plus about 2,650 h unlabelled. Otherwise cite 12.8% (LP Conformer, 100k h) as the overall best. Since the slot's own step is GRID, the LRS3 line can also be dropped.

**M1. Medium. The M12 sentence on test-speaker overlap contradicts the source and the review itself.**
- Location: M12, "The paper does not state whether test speakers appear in training (Sec. 4.A)".
- Evidence: Sec. 4.A says the dataset is divided at random "where 255 sentences of each speaker are used for testing". Every speaker is therefore in training and test, and the Verdict and table both call the setting overlapped.
- Fix: write "Sec. 4.A implies overlapped speakers (255 test sentences from every speaker) and gives no unseen-speaker result".

**M2. Medium. The 3.0/2.9 discrepancy is stated but not connected.**
- Location: Where-claims bullet 2.
- Evidence: the abstract gives 3.0% WER. The 37.5% gain over LipNet is (4.8−3.0)/4.8, and the stated 1.1-point highway gain is 4.1 − 3.0. Every derived number in the prose uses 3.0; only Table III has 2.9.
- Fix: say that the prose's numbers all follow from 3.0 (inference), so the table's 2.9 is the outlier. At 3.0 the WER against LRSW is a tie, and this belongs in the Verdict's LRSW sentence (C1).

**M3. Medium. "The 5 neural ones" mislabels the population, and the table denominator is ambiguous.**
- Location: M06 "Usual approach"; table cell M06; slots.json M06 (`matched` 4, `n` 57).
- Evidence: `tools/seqobj_2018-03.json` lists other neural decoders among the 57: Wand 2016 LSTM, Wand 2017 domain-adversarial, Petridis & Pantic 2017, Tatulli 2017, Thangthai 2017 DNN-HMM, Miao 2016, Ninomiya 2015, arXiv:1710.07161. The audit's usual approach has n=56 (HMM mentions).
- Fix: write "the 5 end-to-end sequence decoders" and give the denominator explicitly as 4 of 5 (designs, read) within 57. Alternatively set `matched` to null, or keep it at 4 with a denominator that matches.

**M4. Medium. The review misses the strongest confound in the central LipNet comparison.**
- Location: Verdict; M06 paragraph; M12 paragraph.
- Evidence: Table III's LipNet row gives 1.9/4.8, LipNet's published figures with its 5-gram LM. Its BLEU of 96.0 does not appear in the LipNet paper, and Fig. 6 plots LipNet curves trained by the authors. So the row's provenance is unclear (inference). No plain 3D-CNN + Bi-GRU + CTC model is trained in-house. Against LipNet's 4.8, attention alone gains 0.7 (A-CTC 4.1), highway alone 0.5 (H-CTC 4.3) and both together 1.9 (2.9). The effects add up to more than their sum, from one run each.
- Fix: add one sentence. The paper has no in-house CTC-only baseline, the LipNet row mixes published LM-decoded figures with a BLEU and training curves from the authors' own runs, and the gains are superadditive. Mark it as inference and add a question for the authors.

**L1. Low. "The ablation does not show what the cascade adds" is overstated.**
- Location: M06 paragraph, first sentence.
- Evidence: H-CTC against AH-CTC (Table III) does measure attention placed before CTC. What is missing is a decoder trained without CTC.
- Fix: "The ablation does not test attention without CTC."

**L2. Low. The recall-window wording and the borderline September 2018 lip-reading work.**
- Location: Verdict ("none in a whole-wiki check to 2018-09"); Appendix.
- Evidence: `recall_cascade.py` uses `cut=(2018,9)` with `<`. The wiki holds arXiv:1810.00108 (Petridis et al., hybrid CTC/attention AVSR with visual-only results, 28 Sep 2018) and arXiv:1809.02108.
- Fix: write "before 2018-09". Name Petridis et al. 2018 as the first joint-loss lip-reading design, [concurrent] by month (just past six months by day). This also supports "the later field kept the joint loss".

**L3. Low. The concurrent ASR precedent goes unnamed.**
- Location: M06 "Usual approach" (only Hori's joint model is named from ASR).
- Evidence: Das, Li, Zhao, Gong, "Advancing Connectionist Temporal Classification With Attention Modeling", arXiv:1803.05563, 15 Mar 2018 (ICASSP 2018), puts attention inside CTC.
- Fix: add it as [concurrent], so that "new in lip reading" stays exact and readers know the idea appeared in ASR at the same time.

**L4. Low. The comparator's lineage is attributed to Kim.**
- Location: M06 ("the ASR joint model it follows outperformed both... [7]").
- Evidence: Sec. 4.C says the comparator follows [43], Hori 2017 (MTL training plus joint decoding); Kim 2017 is the training method Hori builds on.
- Fix: write "the joint training [5] builds on [7]".

**L5. Low. Claim-table quotes are too thin.**
- Location: claims rows 8 and 11.
- Fix: for row 8 quote the Table II caption ("AH-CTC, H-CTC, and A-CTC use only the CTC loss function"). For row 11 add a quote showing the Transformer seq2seq back end.

**L6. Low. A bibliographic detail is unverified.**
- Location: ref [4].
- Evidence: Wu et al. 2024 is listed as an arXiv preprint; it is believed to appear in LREC-COLING 2024 (not confirmed in the wiki text).
- Fix: check the venue and update it if confirmed.

**L7. Low. Some target-internal inconsistencies are not raised.**
- Location: Where-claims (optional additions).
- Evidence: Sec. 4.C names LRW [62] as a comparator, but Table III has no LRW row. The same sentence swaps the datasets of LRW and LRSW. The Fig. 6 caption says "#iteration" while the text says epochs.
- Fix: add these if space allows. They are not required for the verdicts.

## Positions and verdicts

- M06 `standard`: under the skill rules this is justified (new design, but one corpus, one run, no seeds; `ahead` needs repetition). The deciding priors are named and read (LipNet, WAS, Sanabria, the Urdu CTC study, Hori, Kim), and the authors' own reference list was checked ([2] Petridis 2017, [4] Wand 2016 and [6] Noda are word-level or HMM-tandem and do not affect the decoder-novelty claim). No search for the authors' own earlier lip-reading work is recorded (no such work is known to the evaluator).
- M12 `standard`: justified once M1 is fixed.
- M07 `not_reported`: justified.
- Strongest confound: no in-house CTC-only baseline, a LipNet row that mixes the LM condition and provenance, one run, and a fresh random test draw (M4). The review covers the LM and the random draw, not the baseline provenance.
- Fairness: no later work is treated as prior work. Kim and Hori are prior (2016-09 and 2017-07), and Afouras is labelled [concurrent]. The authors' own caveats (Sec. 5, the λ search, LRSW pre-training) are mostly credited. LRSW pre-training should be credited to Sec. 4.D, not only to WAS.
- Language: English only, no model names. Process notes are limited to the Appendix ("published table, appended"), which is acceptable there.

## Scores

- Procedure: 6/10. Dating, population filtering, the recall check and the external priors were done well. The central LRSW claim rests on a column-collapsed text extraction that was never checked against the PDF, and the state-of-the-art lines were not checked against the published M12 table's own state of the art or against the cited source's Table 7.
- Final text: 5/10. The verdict's main negative finding (C1) is false. Both state-of-the-art lines overstate their standing. The M12 overlap sentence contradicts the Verdict.

## Final counts by severity

Critical 1 · High 2 · Medium 4 · Low 7 (total 14 required fixes).
