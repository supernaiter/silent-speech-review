# Evaluator: a language model separate from the writer

Date: 2026-11-28. Target: Zhao et al., "Hearing Lips: Improving Lip Reading by Distilling Speech Recognizers" (LIBS), AAAI 2020, doi:10.1609/aaai.v34i04.6174; first public as arXiv:1911.11502 v1, 2019-11-26.
Review checked: `hearing-lips-improving-lip-reading-by-distilling-speech-recognizers.md`, with `claims.md`, `slots.json`, `verdict.json` and the two audit files.
Sources read: wiki source texts for arxiv-1911.11502 (v1) and doi-10.1609-aaai.v34i04.6174 (AAAI version; the passages checked match, pages 6917–6924), arxiv-1911.12747, cvf-ren21-master-kd, arxiv-1908.04917, arxiv-1611.05358, arxiv-1810.00108, arxiv-1809.02108, arxiv-2411.02256, arxiv-2202.13084, isca-sari18-avicar, icassp2017-tatulli, isca-kolossa12_avenh, plus the Crossref record for doi:10.1109/ICASSP.2019.8682868.

## Claim table

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Recognizer distilled at sequence, context and frame level, with transcripts kept (Verdict) | Target Abstract; Fig. 1; Eq. 8, Eq. 10 | correct | |
| 2 | No distilled teacher outputs in lip-reader training before 2019-05 (0 of 77) (Verdict, M02) | M02 audit `counts_hearing-lips…`; Crossref for Li et al. | correct within the stated boundary; context missing | Li, Wang, Lei, Siniscalchi, Lee (ICASSP 2019) were online 2019-04-17 (Crossref `created`), so they are **prior**, not "date unresolved". They distil an ASR teacher into an audio-visual student, which the review's own 77-population includes ("lip-reading, VSR and AVSR decoders"). "Ahead" holds only for a video-only student, and the Verdict needs to say that. See Fix 1. |
| 3 | 13 of 77 decoders use forced-alignment targets (Verdict, M02, Appendix) | Audit pid list; isca-kolossa12_avenh full text | wrong (overcount) | Kolossa et al. 2012, "Inventory-Based Audio-Visual Speech Enhancement", uses audio forced alignment to build a clean-speech inventory. It does not use it as targets for a visual or AV model, and it is an enhancement paper, a type the inclusion rule says was removed. Sarı 2018 and Tatulli 2017 are correct. The Verdict also calls all 13 "lip-reader training", but the Appendix says only 8 are for the visual stream. |
| 4 | Afouras et al. [2] is [concurrent] (Verdict, M02) | arXiv 1911.12747 v1, 2019-11-28 | correct | Two days after the target. |
| 5 | Afouras: 58.5% vs 57.9% LRS2 WER (M02) | [2] §5, Table 3 | correct; condition incomplete | ASR/GT means fine-tuning with "a small fraction" of ground truth. Decoding uses a 6-gram LM (§4). ASR labels alone give 58.2%. |
| 6 | Quotes "the closest work to ours" and "from the video signal alone" ([2] §1.1) | [2] lines 138–146 | correct | |
| 7 | Ren et al. Table 1: 57.5 / 54.2 / 53.4 LRS2 WER (M02 state of the art) | [3] Table 1 | correct; conditions not stated | These are single values. Teacher sizes, training data and LM are not given there. The table is the motivating ablation of a paper that proposes an alternative teacher. |
| 8 | 3.3 points (5.7%) vs 2.90 points (4.3%); baseline about 11 points weaker (M02) | arithmetic | correct | 57.5−54.2=3.3 and 3.3/57.5=5.74%. 68.19−65.29=2.90 and 2.90/68.19=4.25%. 68.19−57.5=10.7. |
| 9 | CER 38.93→31.27 (CMLR) and 48.28→45.53 (LRS2); 19.7% and 5.7% relative; teachers 31.27–34.94; 9.63 at 20% of the data (M02) | Target Tables 2–4 | correct | |
| 10 | Teacher 2 9.23% vs Teacher 1 9.83%, students 34.94% vs 31.27%; authors blame the dimension mismatch (Where the claims outrun) | Target Table 2; Implementation details; §Experimental results | correct | Teacher 2 differs from Teacher 1 only in encoder width (decoder already 512), so the dimension explanation and teacher width cannot be told apart. The point is fair and the authors are credited. |
| 11 | Frame-level adds 0.44 CER points on LRS2 (Where the claims outrun) | Target Table 3 (45.97→45.53) | correct | |
| 12 | Table 5: CMLR 31.27 vs CSSMCM 32.48; LRS2 CTC/Attention 42.1/63.5 and TM-seq2seq 49.8 vs 45.53/65.29 (M12) | Target Table 5 | correct | |
| 13 | Authors concede TM-seq2seq "achieves the lowest WER on the LRS2 dataset" (M12) | Target, comparison with the state of the art, p. 6 | correct; credited | The authors do not concede CTC/Attention's lower CER and WER, and the review correctly adds it. |
| 14 | CTC/Attention uses an external LM; TM-seq2seq 49.8% is its no-LM figure (M12) | [11] §1, §5.3, Table 2 (V 42.1/63.5, LM weight 0.1 for visual); [12] Table 2 (49.8% plain, 48.3% +extLM) | correct | This handles the LM confound well: the no-LM TM-seq2seq still beats LIBS. |
| 15 | USR 16.0% LRS2 VSR WER, no LM, 1,759 unlabelled hours (M12 state of the art) | [8] Table 6 | correct; "best" label in ref [8] wrong | The same table lists Auto-AVSR at 14.6% (3,448 labelled hours, with LM) and USR at 15.4% with LM. The reference annotation "Best LRS2 visual-only WER" holds only with conditions attached. |
| 16 | Ma et al. 2022: 9.1% CER on CMLR, mean of ten runs, "trained on CMLR alone" (M12) | [9] Table 3, §Methods (LM) | insufficient condition | The audiovisual training set is CMLR only, but decoding adds an external Mandarin LM trained on CMLR plus news2016zh text (Methods; Suppl. S5). The 22.2-point gap is therefore against an LM system, while LIBS's LM use is not reported. |
| 17 | 10.4% vs 39.5% CER is from Chung et al. on LRS, not LRS2, and the audio model also saw 342,644 audio-only utterances (Where the claims outrun) | [13] Tables 4–5, §3.3, §4.1, §5.1 | correct | §3.3: the audio-only mode draws the auxiliary set, so "the same amount of training data" (target §1) does not hold. |
| 18 | CMLR is split at random 7:1:2 over eleven hosts, so test speakers are seen in training (inference) | [10] §3 (eleven hosts; "randomly divided … 7:1:2") | correct as inference | slots.json M11 states this as a fact without the inference label. |
| 19 | Self-distillation [14] and Ren [3], both [later], show video teachers help | [3] §3 ("a video teacher can also promote"); [14] word-level born-again | correct | [14] is word-level (LRW), and the reference notes that. |
| 20 | Before 2019-05, none of 4 LRS2 visual-only decoders reports run counts (M12) | M12 audit (pids 1806.06053, 1809.02108, 1810.00108, 1811.05250) | correct (pattern match, hits read) | |
| 21 | CSSMCM [10] [concurrent] | arXiv 1908.04917 (2019-08) | correct | Same group, within 6 months. |
| 22 | Whole-wiki recall: 3,089 scanned, 26 hits, 0 same-design priors (Appendix) | M02 audit `recall_check_…` | correct | The regex needs distillation vocabulary, which is why forced alignment is tallied separately. That is consistent. |
| 23 | Abstract claims state of the art on CMLR and LRS2; it holds for CMLR only (Verdict) | Target Abstract; Table 5 | correct | |

Other checks, no error found:
- Ephrat et al. (Vid2speech and its follow-ups) regress audio features from video; they are video-to-speech work, not recognizer-teacher text decoders, and the Appendix lists audio-feature regression as 0.
- I found no pre-2019-05 "Wang et al." audio-teacher lip reader (unverified, not a required fix).
- The text contains no model names and no non-English text.

## Required fixes (by severity)

1. **Medium.**
   - **Location:** Verdict, sentence 2; M02 "State of the art" paragraph; ref [6] ("date unresolved").
   - **Evidence:** Crossref for doi:10.1109/ICASSP.2019.8682868 has `created` 2019-04-17 and issue date 2019-05, so Li et al. were public before 2019-05 and are a prior, not undated. Their design distils an ASR teacher's outputs into an audio-visual student, and the review's own population includes AVSR decoders. The absence claim therefore holds only for video-input students, which is the boundary in the audit's "same design" rule, but the Verdict does not say so.
   - **Fix:** In the Verdict, name Li et al. (2019-04) as the closest prior, described through [2] §1.1 and labelled as such, and state the boundary: an ASR teacher into a video-only student. Drop "date unresolved" from ref [6] and label it prior.
2. **Medium.**
   - **Location:** Verdict and the M02 verdict sentence.
   - **Evidence:** The authors claim novelty themselves: "This is to our best knowledge the first attempt along this line" (Introduction, p. 2, in both versions). notes.json records it, but the review presents "ahead" without crediting it.
   - **Fix:** Quote the authors' claim with its location, then state what the review adds: the ledger count, the concurrent Afouras et al., and Li et al. as the AV prior.
3. **Medium.**
   - **Location:** Verdict ("13 of 77 decoders" of "lip-reader training"), M02 Usual approach, Appendix.
   - **Evidence:** isca-kolossa12_avenh is an AV speech-enhancement paper. It uses forced alignment only to build an audio inventory, not as targets for a visual or AV model, and it falls under the stated exclusion of enhancement papers. The Appendix gives 8 of the 13 for the visual stream, yet the Verdict says "lip-reader training".
   - **Fix:** Recount: drop Kolossa from the 13, and from the 77 if it is not a decoder. Re-check the remaining pids. In the Verdict, write "visual or audio-visual model (N, of which 8 for the visual stream)".
4. **Medium.**
   - **Location:** Table row M02 ("Forced-alignment audio targets (of 77 prior decoders); distillation 0 (pattern match 13)") and slots.json M02 `field`/`matched`.
   - **Evidence:** The prose gives transcript-only supervision as the usual approach and forced alignment as a minority of 13 of 77. The table cell instead presents the minority design as the usual approach and attaches "pattern match 13" to "distillation 0", so a reader takes the 13 for a distillation count.
   - **Fix:** Write "Transcript only; forced-alignment targets 13 of 77 (pattern match); distillation 0 of 77". Make `matched` refer to the count named in `field`.
5. **Medium.**
   - **Location:** M12 State of the art ("trained on CMLR alone, Ma et al. (2022) report 9.1% CER"); ref [9].
   - **Evidence:** [9] decodes with an external LM. The Mandarin LM is trained on CMLR plus news2016zh text (Methods, eq. 2; Suppl. S5). LIBS's LM use is not reported, so the 22.2-point gap mixes LM conditions, which is the confound the review itself raises for Table 5.
   - **Fix:** Add "with an external LM (CMLR plus news2016zh text)", and say that the gap is not like-for-like on the LM.
6. **Low.**
   - **Location:** ref [8] annotation "Best LRS2 visual-only WER".
   - **Evidence:** USR Table 6 itself lists Auto-AVSR at 14.6% (3,448 labelled hours, with LM) and USR at 15.4% (with LM).
   - **Fix:** Write "best LRS2 VSR WER without an LM at 223 labelled hours", or cite 15.4% (with LM) and Auto-AVSR 14.6% (3,448 labelled hours).
7. **Low.**
   - **Location:** M02 State of the art (Ren et al.); Verdict ("a video teacher at least as useful").
   - **Evidence:** Ren Table 1 gives single values with no teacher sizes, teacher training data, LM setting or run count. It is the motivating ablation of a paper that argues against plain audio teachers. The video-teacher advantage is 0.8 WER points.
   - **Fix:** State these conditions in one clause, and write "about as useful (0.8 points, single values)".
8. **Low.**
   - **Location:** M02, [concurrent] Afouras sentence.
   - **Evidence:** In [2] Table 3, "ASR/GT" means fine-tuning on "a small fraction" of the ground truth. Decoding uses a 6-gram LibriSpeech LM, and ASR labels alone give 58.2%.
   - **Fix:** Write "distillation, then fine-tuning on a small fraction of ground truth (6-gram LM)", optionally adding 58.2% for ASR labels alone.
9. **Low.**
   - **Location:** slots.json M11 `note`.
   - **Evidence:** The note states "CMLR test speakers also appear in training" as a fact, while the review text correctly labels it as inference from [10].
   - **Fix:** Add "(inference)".
10. **Low (procedure).**
    - **Location:** Appendix M02; claims.md rows 35 and 39.
    - **Evidence:** The target's own reference list cites Gupta, Hoffman and Malik 2016 (cross-modal distillation, image to depth), Romero et al. 2014 and Kim and Rush 2016 as KD priors (Related Work). These are outside the speech setting, but the rule asks for target-cited priors to be named. Claims.md row 35 gives the M02 known-item recall from the M12 audit (5/5), while the M02 audit has 4/4.
    - **Fix:** Name the target-cited KD priors in one line as outside the setting. Point row 35 to the M02 audit.

## Central claim and confounds

- **Strongest confound.** The audio-specific benefit is not isolated: no same-size video teacher is tested, and the baselines differ in strength across datasets. The review handles this well, using Ren Table 1 and [14], the stronger baseline, and the relative change.
- **LRS2 state-of-the-art claim.** The LM confound is handled correctly: the no-LM TM-seq2seq still beats LIBS.
- **Remaining weak point.** The novelty boundary. The "ahead" verdict is defensible only as "into a video-only student", and the prior AV distillation of Li et al. has to be dated and stated (Fix 1).
- **Positions are backed.** Each position carries a citation, a table or a location.
- **No later work treated as prior.** Afouras, Suzuki and CSSMCM are correctly labelled [concurrent], and Ren, Ma, USR and [14] [later].
- **No disclaimers or process narration** in the published text, apart from "date unresolved" in ref [6] (Fix 1).
- **Verdicts.**
  - M02 `ahead` meets the rule: the count is in the Appendix, repetition over 2 datasets and 3 teachers is reported (single runs, stated), and the priors are named, though Li et al. is misdated.
  - M07 `not reported` is justified: the target gives no LM statement and compares against LM-decoded systems.
  - M12 `standard` is justified: 0 of 4 earlier decoders report run counts.

## Scores

- Procedure: 7/10. The audits and quotes are thorough, and the numbers check out. One misclassified forced-alignment pid breaks the stated exclusion, the decisive prior was left undated although Crossref resolves it, and the authors' own novelty claim is not credited.
- Final text: 7/10. It is accurate on every number checked and handles the LM confound and the motivating 10.4%/39.5% gap well. The novelty boundary, the table cell for M02 and the LM condition for Ma et al. need fixing.

## Final counts by severity

High 0 · Medium 5 · Low 5 (one of them procedural).
