# Evaluator: a language model separate from the writer

Evaluation of the component review of "Jointly Learning Visual and Auditory Speech Representations from Raw Data" (RAVEn, arXiv:2212.06246, first public 2022-12). Date: 2026-11-27.
Inputs: compact.md, the review .md, slots.json, verdict.json, the three topic audits, claims.md. Sources re-read: target text.txt and page 6 of paper.pdf (Table 1 LM column), AV-HuBERT [2], USR 2.0 [3], AV2vec [5], AV-data2vec [6], LP-Conformer (arXiv:2302.10915), and the ledger M02 hits arXiv:2007.06504, 2008.02516, 2108.13630, 2108.03543 and 2203.07996. Counts were recomputed with the writer's own yearcount.py.

## Claim table

| # | Claim (location) | Where checked | Status | Note |
|---|---|---|---|---|
| 1 | Large, 1,759 h / 30 h, no self-training, no LM: RAVEn 32.5 = AV-HuBERT 32.5 (Verdict, M03) | Target Table 1 (PDF p.6, LM column ✗ for both); [2] Abstract and Table (S2S, no LM); [3] Table 2; [6] Table 1 | correct | Same budget and no LM on both sides. The conditions still differ: [2] fine-tunes with S2S cross-entropy and no CTC ([2] App. B; [6] Table 1 "CE"), while RAVEn uses hybrid CTC/attention with λ = 0.1 (App. A.4). |
| 2 | Base margins 4.8 and 5.9 points; 27.8 vs 28.6 at 433 h (Verdict) | Target Sec. 4.2; Table 2 | correct | [3] Table 2 lists RAVEn Large/433 h as 28.2, not 27.8. A later paper by the same first author therefore narrows the margin to 0.4 points. |
| 3 | Self-training 32.5 → 24.8, 7.7 points, 24% relative (inference) (Verdict, M02) | Target Table 1; Sec. 4.2 | correct (arithmetic) | "Largest gain after pre-training" is a tie: Base → Large is also 7.7 points (40.2 → 32.5, Sec. 4.2). |
| 4 | Pseudo-labelling by the fine-tuned audio encoder is "the usual audio-teacher route" (Verdict, M02) | Target Sec. 3.2; [2] Sec. 4 and App. B.4 | correct, but the deciding prior is missing | AV-HuBERT already pseudo-labelled the same unlabelled data with a fine-tuned audio HuBERT and states "no additional data is used". That is the exact prior for both the route and the "no extra data" point. The review names neither. |
| 5 | "Pseudo-labelling ... carries the final gain ... against no gap to AV-HuBERT from pre-training" (M02) | Target Tables 1–2; [2] | misleading | With the same route and data, AV-HuBERT gains 3.9 points (32.5 → 28.6) and RAVEn gains 7.7 (32.5 → 24.8). After self-training RAVEn is 3.8 points better, so the route alone does not explain the gain. The confound is the quality of the pseudo-labeller (RAVEn's audio encoder reaches 2.7% ASR at 30 h; AV-HuBERT uses an A/MFCC→AV HuBERT labeller) and the decoder. The review does not handle this. |
| 6 | "Round count and LM use in pseudo-labelling are not stated" (M02, Questions) | Target Sec. 3.2 | partly wrong | Sec. 3.2 describes one pass (fine-tune the audio encoder, pseudo-label, fine-tune on both). What is actually missing is how the pseudo-labels were decoded: beam, LM, filtering. |
| 7 | Symmetric variant 49.0 vs 32.9 (M03) | Target Table 3 | correct numbers, selective | Cross-modal only (40.8) is also symmetric and is the closer baseline. Against it the asymmetric gain is 7.9 points, not 16.1. |
| 8 | Ablations are Base, validation set, "one run" (M03, Where...) | Target Sec. 4.4 | correct for Base and validation; "one run" is not in the text | The paper reports no run count. Write "no repeat runs or spread reported". |
| 9 | "Surpasses all self-supervised methods" fails at Large/30 h; Sec. 4.2 states it for Base only (Where...) | Abstract; Sec. 4.2; Sec. 4.3 | correct | Credit the authors' own hedge, "by a large margin in most settings" (Sec. 1). Sec. 4.3 makes the claim for all configurations of Table 2, which holds there. |
| 10 | 23.8% with LM vs Serdyuk 2021 25.9% without LM (M12) | PDF p.6 Table 1: Serdyuk 2021 LM ✗; RAVEn 23.8 LM ✓; RAVEn 24.8 LM ✗ | correct but misleading | 24.8% without LM also beats 25.9%, so the LM does not weaken the 90,000-hour claim. The real issue is Serdyuk 2022 at 19.3% (no LM), which the authors bold in their own Table 1. The table is honest; the abstract and Sec. 4.2 overstate. |
| 11 | Serdyuk 2021 called "semi-supervised" in the abstract, listed under "supervised" in Table 1 (M12) | Abstract; Table 1 | correct | |
| 12 | Serdyuk 2022 19.3% with 90,000 h including non-public data (Verdict, M12) | Table 1 | correct | |
| 13 | LRS2 17.9% has no AV-HuBERT row (M12) | Table 9 | correct, but unfair framing | Table 9 does not contain the row. Whether [2] reported LRS2 VSR at all is unverified; if it did not, the authors had nothing to copy. Reframe as: the LRS2 "significantly outperform all" claim has no self-supervised comparator at equal scale. |
| 14 | LRS3 test removal from pre-training not stated (Where..., Next, Questions) | Target App. A.1 | weak | A.1 states that LRS3 test speakers are separate from training, and 433 h is pretrain plus trainval. AV-HuBERT uses the same splits. The only open risk is speaker overlap between VoxCeleb2 and the LRS3 test set, and the bullet does not name it. |
| 15 | LM trained on text including LRS2/3 (Where...) | App. A.4 | correct | |
| 16 | USR 2.0 23.7%, Large, 30 h, LRS3+Vox2 [later] (Verdict, M02, M03) | [3] Table 2 | correct | The ✓ is "shared params", not an LM; [3] mentions no LM. The comparison with 24.8 (no LM) is matched. |
| 17 | USR 2.0 as M03 state of the art | [3] Table 2 | wrong component | USR 2.0 is semi-supervised, and its gain comes from pseudo-labelling (M02). Without self-training at Large/30 h, the best objective is BRAVEn 30.8 (2024, [later]) and AV-data2vec 30.8 ([concurrent]), both in [3] Table 2. |
| 18 | AV-data2vec 30.8% [6] [concurrent] (M03) | [6] Table 1 (Large, 1,759 h, 30 h, CE) | correct | arXiv 2302.06419 (2023-02) is concurrent. |
| 19 | M12 state of the art 17.6% (USR 2.0 Huge) | [3] Abstract; LP-Conformer arXiv:2302.10915 | wrong or incomplete | LP-Conformer (Chang et al., arXiv 2302.10915, 2023-02, ICASSP 2024) reports 12.8% LRS3 VSR WER trained on 100k h of YouTube data (its Table, "LP CONFORMER ... 100K 12.8"). The same line cites the non-public 19.3% for the target's time, so non-public data cannot be excluded today. |
| 20 | "New against its priors"; 13 full-text momentum/EMA hits, none earlier (M03, Appendix) | Target Sec. 2; audit recall_sample | wrong scope | See the novelty section below. |
| 21 | M03: 33 studies to 2022, 24 with full text, contrastive in 18 (M03, table, Appendix) | yearcount.py rerun | not rule-compliant | See the counts section below. |
| 22 | M02: "10 of 14 distil from a frozen audio recogniser" [7] | Full text of the hits | overstated | arXiv:2007.06504 self-distils lip-reading models; it is not audio distillation, yet it is listed in usual_approach.pids. FastLR (2008.02516) says "we do not introduce any distillation method". SimulLR (2108.13630) mentions distillation only in related work. These are mention counts, not designs. |
| 23 | M12: 37 of 49 LRS3 system papers to 2022 show no run spread | yearcount.py rerun | population and window wrong | The 49 include speech separation and extraction (2101.03149, 2207.04213, 2210.06177, 2210.17456, 2212.10744), keyword spotting (2009.01225, 2110.15957), AV synchronisation (2112.04432) and a PLoS CB perception study. None of these reports visual-only LRS3 WER. About 17 of the 53 with full text are dated 2022-06 to 2022-12 ([concurrent]). |
| 24 | M02 Appendix "Known-item recall 1.0" | M02 audit known_item_recall_<slug> | wrong | The audit gives recall 0.5 and lists isca-ma21c-lira as missed. |
| 25 | Chronology labels [2] prior, [4] prior, [7] prior, [5] concurrent (2022-12-06), [6] concurrent (2023-02), [3] later | arXiv ids | correct | |

### Dating and window
The rule (SKILL.md §4; review-format.md) is: prior means first public more than 6 months before the target, i.e. before 2022-06. Works from 2022-06 to 2023-06 are [concurrent]. The audit uses "ledger year ≤ 2022" and calls that window "at the target's time". It mixes prior with concurrent work, and one paper (ReVISE, arXiv 2212.11377, 2022-12-21) was posted after the target.
Recount with the writer's yearcount.py and arXiv months (inference):
- M03: 15 prior with full text, 8 concurrent.
- M02: 13 prior with full text, 2 concurrent (2207.05692, 2212.02782).
- M12: 34 prior with full text, 17 concurrent, 2 with month unresolved.
Using the ±6-month window does not change any verdict. It does change the counts the Usual approach lines rest on.

### Novelty against any-signal priors
The design is not new against prior work in any signal:
- The objective, a masked student regressing latents from a momentum or EMA teacher, is data2vec (Baevski et al., arXiv 2202.03555, 2022-02, speech, vision and text). Without masking it is BYOL (Grill et al., 2020) and BYOL-A for audio (Niizumi et al., arXiv 2103.06695, 2021-03).
- The target cites data2vec, BYOL and DINO itself in Sec. 2 and states how it differs: multimodal, no target normalisation or averaging, Transformer predictors.
- Pan et al. 2022 (arXiv 2203.07996, prior, in the M03 ledger) put a MoCo v2 momentum encoder into an AV speech recognition pipeline. The full-text regex missed it because it does not match "MoCo".
- The 13 "full-text hits" are folders, not unique studies. They include the target and duplicates (2512.14083 twice, 2607.08236 three times), which leaves about 9 unique studies besides the target (inference).

What remains new is the cross-modal, asymmetric use of momentum teachers for audio-visual speech, and only that can be claimed. data2vec was not read (no read_fulltext entry with role prior), which the novelty rule requires.

Unverified: BraVe (Recasens et al., 2021, cross-modal BYOL-style video/audio, cited by the target) may also use an EMA target network.

### Counts
- The M03 population of 33 includes 2005–2014 Interspeech papers on lip contour tracking, sensorimotor mapping, articulatory primitives and tongue MRI, plus deepfake detection (2203.01265), speech separation (2101.03149), a cortical graph NN (2206.02671), Relaxed Attention (2209.09735), AV enhancement (2210.17456), AV synchronisation and VAD. These are outside the inclusion rule, so "33 pre-training studies" is not accurate.
- "Contrastive in 18" counts mentions. AV-HuBERT itself mentions contrastive learning only in related work. The 13-components table drops the word "mention" ("Contrastive objectives (18 of 24)").
- Deduplication is applied for the ledger tallies but not for the full-text hits (13 folders).

## Required fixes, ordered by impact

1. **Major, M02 and Verdict: matched self-training confound.** Name AV-HuBERT's self-training as the deciding prior: an audio HuBERT labeller, the same data and no extra data ([2] Sec. 4 and App. B.4). State that the same route gives 3.9 points for AV-HuBERT and 7.7 for RAVEn, leaving RAVEn 3.8 points ahead after self-training (Table 1). Put the remaining difference down to pseudo-labeller ASR quality and the decoder. Replace "round count and LM unstated" with "pseudo-label decoding (beam, LM, filtering) not stated". Drop "As the authors state, no extra data is needed", or add that AV-HuBERT makes the same point.
2. **Major, M03 novelty sentence.** Replace "The design is new against its priors" with a scoped claim. The momentum-teacher masked latent regression is data2vec's (2022-02) and BYOL's; the asymmetric cross-modal audio-visual use is what is new. Name data2vec and Pan et al. 2022 (MoCo v2) as deciding priors, read data2vec, and credit the authors' own distinction (Sec. 2). Report the full-text hits as about 9 unique studies besides the target, not 13 folders.
3. **Major, windows (M03, M02, M12 and Appendix).** Recount "at the target's time" with prior meaning first public before 2022-06. Alternatively, label the counts "prior and [concurrent], to 2022" and give the concurrent share: M03 8 of 23 with full text, M02 2 of 15, M12 about 17 of 53 (inference).
4. **Major, off-population.** Apply the inclusion rules before reporting denominators: M03 (pre-deep-learning and non-decoding papers) and M12 (separation, extraction, KWS, synchronisation and perception papers have no visual-only LRS3 WER). Otherwise say "papers matching the pattern", not "pre-training studies" or "LRS3 system papers".
5. **Major, M02 usual approach.** Change "10 distil from a frozen audio recogniser" to "mention distillation in 10 of 14 (pattern match, upper bound)". Remove arXiv:2007.06504 from usual_approach.pids: it self-distils lip-reading models. Name the audio-distillation designs that are confirmed: [7] and LIBS (1911.11502).
6. **Major, M12 state of the art.** Add LP-Conformer (Chang et al., arXiv 2302.10915, ICASSP 2024): 12.8% LRS3 VSR with 100k h of non-public YouTube data. Keep 17.6% (USR 2.0 Huge) as the best result on public data, and label both.
7. **Major, M03 state of the art.** For a pre-training objective, give the best result without pseudo-labels at Large/30 h: 30.8% for BRAVEn (2024, [later]) and AV-data2vec ([concurrent]) ([3] Table 2; [6] Table 1). Move USR 2.0's 23.7% to M02 only, or mark it as semi-supervised.
8. **Major, M12 LM sentence.** Rewrite it. 24.8% without LM already beats Serdyuk 2021's 25.9% (no LM), so the LM is not the problem. The problem is that the abstract picks 25.9% while Serdyuk 2022's 19.3% (no LM, 90,000 h) sits bolded in the authors' own Table 1. Say the table reports it honestly and the abstract and Sec. 4.2 overstate.
9. **Major, M02 Appendix.** Change known-item recall to 0.5 (LiRA missed), matching the audit.
10. **Minor, M03 asymmetry.** Report cross-modal only (40.8%) as the symmetric baseline: a gain of 7.9 points, not 16.1 against 49.0.
11. **Minor, decoder.** Replace "not stated to match the comparators'" with a plain statement. [2] fine-tunes with S2S cross-entropy and no CTC, and uses no LM for S2S ([2] App. B). RAVEn uses CTC/attention. This applies to the Large tie too.
12. **Minor, wording.** "Largest VSR gain after pre-training" should be "as large as the Base-to-Large gain (40.2 → 32.5, Sec. 4.2)". "One run" should be "no repeat runs or spread reported".
13. **Minor, fairness.** Credit "by a large margin in most settings" (Sec. 1) before criticising the abstract.
14. **Minor, test overlap.** Drop the LRS3-test bullet, the M11 next step and the question, or narrow them to VoxCeleb2–LRS3 test speaker overlap. A.1 states that the LRS3 test speakers are separate.
15. **Minor, LRS2 sentence.** Reframe it as having no self-supervised comparator at equal scale, unless [2] reported LRS2 VSR and the authors left it out.
16. **Minor, body restatement.** Remove the method restatements: "Here a jointly trained audio teacher supplies latents, then the fine-tuned audio encoder pseudo-labels unlabelled video (Sec. 3.2)", "This paper drops offline targets." and "As the authors state, no extra data is needed (Sec. 4.3)." Remove the process note "(sparse slot)" from the M07 table cell.
17. **Minor, questions.** Remove "Were the AV-HuBERT rows copied from Shi et al.?": the values match [2]'s published ones and [2] App. B gives the decoder. Keep the decoder-matching question as a statement.
18. **Minor, M03 table cell.** Write "Contrastive objectives mentioned (18 of 24)", so that the table does not present a mention count as a design count.
19. **Minor, 433 h margin.** [3] Table 2 lists RAVEn Large/433 h as 28.2, not 27.8. Note this beside the 27.8 vs 28.6 margin in the Verdict.
20. **Minor, bibliography.** [5] and [6] were also published at ICASSP 2023. The venues can be updated; the arXiv ids are correct.
21. **Minor, M03 Appendix.** "13 further hits, none earlier than the target": the 13 include the target itself, so "further" is wrong.

## Scores
- Procedure: 6/10. All target numbers and comparators check out against the sources. The problems are the windows, which use ledger years instead of ±6 months; the populations, which are not filtered by the inclusion rules; mention counts presented as designs; recall misreported; and a novelty claim made without reading the any-signal prior (data2vec).
- Final text: 6/10. The position is clear and well located, but the central M02 argument leaves out the matched AV-HuBERT self-training comparison, and two state-of-the-art lines name the wrong or an incomplete best work.

Severity counts: critical 0, major 9, minor 12.
