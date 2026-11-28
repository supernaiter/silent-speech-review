# Evaluator: a language model separate from the writer

Date: 2026-11-28. Target: Prajwal et al., "Learning Individual Speaking Styles for Accurate Lip to Speech Synthesis" (Lip2Wav), CVPR 2020; first public arXiv 2005.08209v1, 2020-05-17. Review evaluated: `learning-individual-speaking-styles-for-accurate-lip-to-speech-synthesis.md` (identical to `draft-before-evaluation/review.md`).

Sources checked: wiki source texts of the target (cvf-prajwal20-lip2wav, sc_text.txt), LipSound (isca-qu19-lipsound), Vougioukas et al. (isca-vougioukas19_ganv2s, plus the arXiv 1906.06301v1 PDF the target cites, fetched to /tmp/claude-0/dl/v2s), Lip2AudSpec (arxiv-1710.09798), Ephrat et al. 2017 (arxiv-1708.01204), Vid2Speech (arxiv-1701.00495), Le Cornu and Milner 2015 and 2017 (isca-cornu15-v2speech, doi-10.1109-taslp.2017.2716178), Kumar et al. 2018 (arxiv-1807.00619), Lipper (arxiv-1907.01367), Hush-Hush Speak (isca-uttam19-hushhush), RobustL2S (arxiv-2307.01233), Niu and Mak (arxiv-2303.00502), LipSound2 (arxiv-2112.04748), FastLTS (arxiv-2207.03800), Varshney et al. (arxiv-2206.02050); the three topic audits; extra.json.

## Claim table

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Lip2Wav has about 20 h and 5,000+ words per speaker; GRID 0.8 h per speaker (M03) | Target Table 1, Sec. 3 | correct | "GRID [7] 34 28 0.8 56"; "Lip2Wav (Ours) 5 120 ≈20 ≈5K". |
| 2 | 0 of 10 priors train on unconstrained speech or on more than about 1 h per speaker (Verdict, M03, Appendix) | Texts of all 10 priors | correct (count); procedure gap | Le Cornu 2015: GRID speaker 4, 800 training sentences; Le Cornu 2017: 800 training sentences per GRID speaker; Vid2Speech, Lip2AudSpec, Vougioukas, LipSound: GRID; Ephrat 2017: GRID and TCD-TIMIT ("less than 25 minutes of video used for training", Sec. 6.1); Kumar 2018, Lipper, Hush-Hush: OuluVS2. The count holds, but 6 of the 10 were not read for this verdict (extra.json open item). See fix 4. |
| 3 | GRID 7, OuluVS2 3, TCD-TIMIT 1 (Appendix) | Same texts | correct | LipSound is GRID-only; Vid2Speech has no TIMIT data. |
| 4 | Lip2Wav's "first to study this problem in a large vocabulary setting" (Sec. 2.1) holds | Target Sec. 2.1; Ephrat 2017 Sec. 6.1 | correct | TCD-TIMIT had unseen test words, but it is not a vocabulary in the thousands. |
| 5 | LipSound: attention mel decoder, Tacotron2-inspired, whole 3-s GRID clips, teacher forcing, Griffin-Lim (Verdict, M06) | LipSound Sec. 1, 2, 3.1, 5 | correct | "location-sensitive attention"; "All videos are 3 seconds long ... (total 75 frames)"; "teacher-forcing training strategy"; "Griffin Lim algorithm [35] with 50 iterations". |
| 6 | The target cites LipSound only as lip-to-text work (Sec. 2.2) | Target Sec. 2.2, ref. [28] | correct | "[6, 28, 37, 38] are limited to narrow vocabularies" in 2.2 only. |
| 7 | Previous works' "0.3 -0.5 seconds of context" fits frame-window models, "not LipSound or Lip2AudSpec, which feeds 3-s clips to a CNN + LSTM" (M06) | Lip2AudSpec Sec. 3.1, 4.2 | **wrong for Lip2AudSpec** | Lip2AudSpec: "divided into K non-overlapping slices each of length Lv"; "We fixed the length of each video slice Lv to 5 (which is equivalent to 200 ms)". Its input is 0.2 s, shorter than the target's claim. The claim-table quote (c16) gives only the speakers, not the input length. Fix 1. |
| 8 | Appendix: "whole 3-s clip input 2" | Same | wrong | It is 1 (LipSound) under the review's definition. Vougioukas et al. feed 7-frame windows into a GRU that runs over the whole clip (Sec. 2.1), so if a recurrent context across the clip counts, the second one is Vougioukas, not Lip2AudSpec. |
| 9 | 9 frames [6], 7 frames + GRU [3] (M06 usual approach) | Ephrat Sec. 5; Vougioukas Sec. 2.4 | correct | "Using K = 9 frames as input worked best"; "window of N = 7 frames". |
| 10 | Table 9 STOI 0.221 vs 0.446; Table 8 0.264 at 0.5 s vs 0.446 at 3 s; one speaker, one run | Target Tables 8, 9, 4 | correct | 0.446/0.311/1.290 equals the Hardware Security row of Table 4, so the ablations are on that speaker (inference). |
| 11 | Homophenes the dominant error (Sec. 6.3.1), neural vocoders poor (Sec. 5.3) credited to authors | Target | correct | Both are credited to the authors. |
| 12 | Table 2 WERs 26.64% and 32.51% equal Vougioukas's 26.6% and 32.5%, from an ASR trained on GRID (4% on ground truth); target names the Google API | Target Table 2, Sec. 6 footnote 4; Vougioukas Table 2, Sec. 3.2 (Interspeech and arXiv v1) | correct numbers; **wording too strong** | The values match to the one decimal [3] reports. Target Sec. 6: "Using an out-of-the-box ASR system⁴" with footnote "Google Speech-to-Text API", and "we use the open-source implementations ... or re-implement". STOI and PESQ of the same rows differ (0.564/1.684 vs 0.518/1.71; 0.513/1.673 vs 0.446/1.82). "Copied and re-run values are mixed" goes beyond the evidence. The writer's open item says copying "is the reviewer's reading". Fix 3. |
| 13 | Vid2Speech reported only MTurk human transcription | Vid2Speech Sec. 4.3 | correct | 23 MTurk workers, GRID vocabulary forced choice. |
| 14 | "Almost 4×" holds for ESTOI vs Ephrat (mean ratio 3.76); vs GAN, STOI ratios 1.78–2.17 | Target Table 4 (recomputed) | correct | ESTOI/Ephrat: 3.26, 2.96, 4.26, 4.86, 3.44, mean 3.76. STOI/GAN: 2.17, 2.14, 1.96, 1.78, 2.16. Also ESTOI/GAN 2.15–2.83 and STOI/Ephrat 2.27–2.58 are not mentioned. The abstract says "four times", without "almost". Fix 10. |
| 15 | Multi-speaker claim (Sec. 6.4) ignores Vougioukas's unseen-speaker test (WER 40.5%, Table 4) and Lip2AudSpec's joint four-speaker training | Vougioukas Table 4; Lip2AudSpec abstract | correct but incomplete | Lipper, which the target cites as [22], reports speaker-independent results ("we explore the results of Lipper for speaker-independent settings"). Hush-Hush Speak is speaker-independent. LipSound trains one model on all 33 GRID speakers. Fix 5. |
| 16 | Table 7: 34.2% ASR WER vs 38.8% classifier error | Target Table 7 | correct | |
| 17 | MTT+TTS 3.86 vs 3.04 intelligibility; naturalness 3.63 vs 3.15; 15 raters, no interval | Target Table 6, Sec. 6.3.2 | correct | |
| 18 | 800× in Sec. 1, 80× in contributions | Target Sec. 1 | numbers correct; **framing misleading** | Sec. 1 compares with "current multi-speaker datasets [2]", the contributions with "its counterparts", so the bases differ. The real gap is that Table 1 gives 25× (GRID) and 40× (TIMIT), not 80×. Fix 7. |
| 19 | RobustL2S STOI 0.583 vs 0.416 on Chemistry, official split, one model per speaker, AV-HuBERT fine-tuned on Whisper transcripts (M03 SOTA) | RobustL2S Table IV, Sec. IV-A | correct | Same table: Hong et al. [28] 0.566 STOI, **0.429 ESTOI > RobustL2S 0.397**. |
| 20 | "The later gain comes from external pre-training, not from more video per speaker" (M03) | RobustL2S Table IV, Sec. II | **unsupported / contradicted** | Hong et al. (VV-Memory, described in RobustL2S Sec. II as a key-value audio-visual memory) reach 0.566 on the same split, which is most of the 0.416→0.583 gain. RobustL2S does not ablate pre-training versus per-speaker data. Fix 2. |
| 21 | RobustL2S Table I: non-autoregressive seq2seq on SSL features raises STOI 0.50→0.583 (M06 SOTA) | RobustL2S Table I, Sec. III | correct | fs2s "adopts a non-autoregressive-based encoder-decoder". This is an ablation inside RobustL2S, Chemistry only. |
| 22 | Niu and Mak: asynchrony, Whisper-reference WER 24.69%, MOS with 95% CI; "one Chemistry Lectures output gives STOI 0.215 vanilla and 0.760 aligned" (M12 SOTA) | Niu and Mak Table 2, Table 4 caption | numbers correct; **example not like-for-like** | 0.215→0.760 is SLTS, whose own synchronization module shifts its output. For a model without that module, the same table gives VCA-GAN 0.543→0.659. These are test-set means of a model, not "one output". Fix 8. |
| 23 | M12 usual approach: 6 of 10 listener test, 0 of 10 run spread | M12 audit; prior texts | correct (as tallied) | |
| 24 | "Gains over baselines confound decoder, encoder, context and data" (Verdict) | Target Sec. 6, Tables 2–4 | **partly wrong** | Sec. 6 says the baselines were run with open-source code or re-implementations on the same splits, so data does not explain the Table 2–4 gaps over baselines. Fix 6. |
| 25 | Chronology labels: LipSound prior, Michelsanti [concurrent], RobustL2S, Niu and Mak, LipSound2 [later] | Dates | correct | LipSound (Interspeech, Sept 2019) is cited by the target. |

## Required fixes, by severity

1. **Major. M06 paragraph and Appendix M06 ("whole 3-s clip input 2").**
   - Evidence: Lip2AudSpec Sec. 4.2 says "We fixed the length of each video slice Lv to 5 (which is equivalent to 200 ms)", and Sec. 3.1 says the video is "divided into K non-overlapping slices". Lip2AudSpec does not feed 3-s clips. Its 0.2 s context supports the target's "0.3 -0.5 seconds" claim.
   - Fix: rest the rebuttal of Sec. 7.1 on LipSound alone. Optionally add that Vougioukas et al. run a GRU over the 7-frame encodings of the whole clip (Sec. 2.1), which is causal context beyond 0.5 s. Correct the Appendix count and the M06 audit entry, and replace note c16's "clips are 3 s" with the slice length.

2. **Major. M03 last sentence, "The later gain comes from external pre-training, not from more video per speaker."**
   - Evidence: RobustL2S Table IV, the table the review itself quotes, lists Hong et al. [28] at 0.566 STOI on Chemistry, against 0.583 for RobustL2S and 0.416 for Lip2Wav. RobustL2S Sec. II describes Hong et al. as a key-value memory model. On ESTOI, Hong et al. lead (0.429 vs 0.397). No cited work separates pre-training from per-speaker hours.
   - Fix: replace the sentence with something like "Later per-speaker models on the same split reach 0.566 (Hong et al., memory) and 0.583 (RobustL2S, external pre-training); neither varies per-speaker hours." Add the ESTOI values to the SOTA line.

3. **Medium. M12 paragraph ("Copied and re-run values are mixed, unlabelled") and Verdict ("equal").**
   - Evidence: 26.64/32.51 match [3]'s 26.6/32.5 to [3]'s one-decimal precision. The target states it ran the baselines itself (Sec. 6: "we use the open-source implementations provided by the authors if available or re-implement a version ourselves") and transcribed them with the Google API (footnote 4). The match is strong evidence, but the paper does not say the rows were copied. The writer's open item concedes that copying is a reading.
   - Fix: say "match to the precision of [3]" and "(inference) the WER cells appear taken from [3] while STOI and PESQ were re-run". Quote the Sec. 6 sentence, which makes the mismatch sharper.

4. **Medium. M03 "Ahead under the rule ... the deciding priors ... were read".**
   - Evidence: four of the ten priors were read for M03, and Vid2Speech only for M06. Le Cornu and Milner 2015 and 2017, Kumar et al. 2018, Lipper and Hush-Hush Speak were classified from ledger text (extra.json open items). Their texts confirm the count (GRID with 800 training sentences per speaker, or OuluVS2), so the verdict survives. The population is also narrower than the rule's "precedents from any signal" without a stated reason: lip video plus tongue ultrasound corpora, for example the Hueber et al. single-speaker silent speech interface corpora (hours per speaker unverified), are excluded.
   - Fix: read the remaining six or list them with locators ("Le Cornu and Milner 2015, Sec. 3: speaker 4, 800 training sentences", and so on). Add one sentence justifying the video-only boundary for this novelty claim.

5. **Medium. "Where the claims outrun the evidence", multi-speaker bullet.**
   - Evidence: Lipper, which the target cites as [22], reports speaker-independent synthesis. Hush-Hush Speak ("both speaker-independent and multi-view", Sec. 1) also does, as does LipSound (one model on all 33 GRID speakers, Sec. 2). The M12 audit already lists Lipper and Hush-Hush under unseen-speaker tests.
   - Fix: add Lipper first. It is the strongest counterexample, because the authors cite it.

6. **Medium. Verdict, "Gains over baselines confound decoder, encoder, context and data".**
   - Evidence: the baselines in Tables 2–4 were trained on the same splits (Sec. 6). Lip2Wav also leads on GRID at 0.8 h per speaker (Table 2: 0.731 vs 0.659 STOI), so the data do not explain the gains over baselines.
   - Fix: drop "data", or limit it to comparisons with the priors' own published numbers.

7. **Medium. Bullet "The data ratio is 800 times in §1, 80 times in the contributions."**
   - Evidence: Sec. 1 compares against "current multi-speaker datasets [2]" and the contributions against "its counterparts". Table 1 gives 20/0.8 = 25× (GRID) and 20/0.5 = 40× (TIMIT).
   - Fix: "80× is not supported by Table 1 (25× GRID, 40× TIMIT); 800× compares against multi-speaker datasets (inference)."

8. **Medium. M12 SOTA line and table cell "a-STOI 0.760 vs 0.215 vanilla".**
   - Evidence: in Niu and Mak Table 2, the 0.215 row is SLTS, whose synchronization module deliberately shifts its output. VCA-GAN on the same test set goes from 0.543 to 0.659 a-STOI. Both rows are test-set means, not one output.
   - Fix: cite VCA-GAN 0.543→0.659 as the alignment effect on a standard model, or label SLTS's 0.215 as an artifact of its own shift module. Replace "one Chemistry Lectures output".

9. **Minor. Appendix M03, "the published table also lists LipSound2 [9] [later]".**
   - Evidence: this is process narration, and the citation carries no claim. LipSound2 is relevant on its own merits: it keeps the location-aware attention encoder-decoder, pre-trains on about 2,400 h, and its Table (GRID) gives ESTOI 0.592 vs Lip2Wav 0.535.
   - Fix: use it in M06 (the attention-decoder line continued, with pre-training) or M03, or drop it.

10. **Minor. "4×" bullet.**
    - Fix: add ESTOI vs GAN-based 2.15–2.83 and STOI vs Ephrat 2.27–2.58 (inference), and note that the abstract says "four times" without "almost".

11. **Minor. Verdict, "its five speakers became the single-speaker benchmark".**
    - Evidence: later work often uses subsets: FastLTS 3 speakers, Let There Be Sound 2, Niu and Mak and Varshney et al. Chemistry only.
    - Fix: "its speakers, above all Chemistry Lectures, became the single-speaker benchmark."

12. **Minor. Question "are the 90/5/5 splits by duration or by video?"**
    - Evidence: Sec. 5.1 answers part of this: "we create these splits using different videos".
    - Fix: ask whether the percentages are by duration or by video count.

13. **Minor. M06, LipSound as the deciding prior.**
    - Evidence: LipSound never evaluates its synthesized audio as speech (no STOI, PESQ or listener test). The mels feed a lip-reading back-end.
    - Fix: add one clause so the reader sees that Lip2Wav was the first to report the speech quality of this decoder design. The verdict stays standard.

## Position checks

- **M03 "ahead".** The design count is verified and the design is repeated over 5 independently trained speakers. The verdict is defensible as a protocol (corpus) judgment, and the review itself says the hours are untested. The contribution is a dataset, so the review should keep the verdict on the corpus design and not imply a data-scale effect. Fixes 2 and 6 matter here. Fix 4 is procedural and does not change the verdict.
- **M06 "standard".** LipSound is a correct and sufficient deciding prior. The rebuttal of the 0.3–0.5 s claim must drop Lip2AudSpec (fix 1).
- **M12 "standard".** Standard is justified. The Table 2 finding is correct and important, but it needs the precision and inference hedge (fix 3).
- **SOTA lines.** Each is on its slot's own step with its conditions stated (split, speaker dependence, pre-training, transcript source). The M03 line omits the competing Hong et al. row and the ESTOI ranking. The M12 example is not like-for-like (fix 8).
- **Missing priors outside the ledger (unverified, low impact).** Aihara et al. 2015 (exemplar NMF lip-to-speech) and Takashima et al. 2019 (exemplar CNN lip-to-speech) used small single-speaker Japanese corpora. Neither would change the M03 count.
- **Authors' caveats.** Homophenes, neural vocoders, "metrics are not perfect", single-speaker focus (Sec. 6.4) and the 3-s memory limit (Table 8) are credited or not presented as the review's own findings.
- **Text rules.** English only. No language-model names (Whisper and AV-HuBERT are cited research systems). No disclaimers, apart from the process phrase in fix 9.

## Scores

- Procedure: 6/10. The counts are correct, all central numbers verify, and the chronology is right. However, six M03 priors were unread, the population boundary is not justified, and an error in a comparator's input length passed into the Appendix count.
- Final text: 6.5/10. The positions are clear and the Table 2 finding is valuable. There is one factual error about a comparator and one inference contradicted by the table the review quotes, and the copy assertion is unhedged.

## Final counts by severity

- Major: 2
- Medium: 6
- Minor: 5
- Total: 13
