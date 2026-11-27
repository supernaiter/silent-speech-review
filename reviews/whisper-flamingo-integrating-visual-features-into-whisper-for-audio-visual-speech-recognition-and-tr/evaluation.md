# Evaluator: a language model separate from the writer

Date: 2026-11-27. Target: Rouditchenko et al., "Whisper-Flamingo: Integrating Visual Features into Whisper for Audio-Visual Speech Recognition and Translation", Interspeech 2024 (doi:10.21437/Interspeech.2024-322; arXiv 2406.10082 v1 2024-06-14, v2 2024-11-07, v3 2024-11-19, dates confirmed on the arXiv abstract page).

Sources checked: Interspeech text (wiki `in24-whisperflamingo/source/sc_text.txt`), arXiv v3 text (wiki `arxiv-2406.10082/source/text.txt`), DoubleHelix (`arxiv-2607.29112`), MTC-AVSR (`isca-a26-mtcavsr`), USR 2.0 (`arxiv-2602.19316`), Simic and Bocklet (`arxiv-2312.13873`), the four topic audits, `notes.json`, `claims.md`, the public code repository (`whisper_ft_muavic.py`, `whisper_decode_video.py`, `README.md`), arXiv abstract pages and DOI resolution.

## Claim table

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Gated cross-attention, tanh gates initialised at 0, at the start of each decoder block (M06) | Interspeech Sec. 2, Eq. 1-2 | correct | "initialized to 0 ... beginning of each block, before the self-attention layer". |
| 2 | Deciding fusion comparison is one Whisper-Medium run: early fusion 10.0%, gated 7.0% at 0 dB (Verdict, M06) | Interspeech Table 2, Sec. 3.2 | correct, incomplete | Numbers right. Early and late fusion fine-tune all Whisper parameters ("In both cases, all of Whisper's parameters are fine-tuned"), while Whisper-Flamingo freezes Whisper, so the comparison mixes fusion design with freezing. The review does not say this. |
| 3 | Encoder insertion only "significantly worse" (M06) | Interspeech Sec. 2 | correct | No numbers given. |
| 4 | 630M added parameters, 2.5B total; Whisper frozen after noisy fine-tuning (M03) | Interspeech Sec. 3.1, Sec. 2 | correct | AV-HuBERT is frozen but its batch-norm statistics update (Sec. 3.1); minor. |
| 5 | "No unfrozen control is shown" (M03) | Interspeech Table 2, Sec. 3.2 | wrong as worded | Early and late fusion are unfrozen audio-visual variants. What is missing is an unfrozen gated cross-attention variant. |
| 6 | Clean LRS3 2.3% to 1.5%, beam 15 (Verdict, Where-claims) | Interspeech Table 3, Sec. 3.1, Sec. 3.3 | correct | v1/Interspeech claims "improves the clean WER from 2.3% to 1.5%". |
| 7 | Beam 1: audio-only 1.1%, Whisper-Flamingo 1.0% (arXiv v3 Table 3) | v3 Table 3 | correct | 433 h rows. The review does not say that v3 itself drops the 2.3-to-1.5 clean claim and reports clean parity in Sec. 3.3 (0.86% vs 0.85%, 1,759 h). See fix H1. |
| 8 | 52.1% relative noisy gain is a beam-15 figure; beam 1 12.4% to 7.2% is 42% (inference) | Interspeech Sec. 3.3; v3 Table 3 | arithmetic correct, framing wrong | (12.4 - 7.2) / 12.4 = 41.9%. Both models use the same beam size in both comparisons. v3 App. 8.2: beam 15 is better for SNR ≤ 0 and Whisper-Flamingo "significantly outperforms" audio-only Whisper at both beam sizes. v3 Sec. 3.3 already revises the figure to 49.5% (1,759 h). This is not an overreach. |
| 9 | "Slightly better" than AV-HuBERT (5.6% vs 5.8%) on recreated noise, as the authors note | Interspeech Sec. 3.3, Table 3 | correct | Credited. |
| 10 | u-HuBERT (4.6%) "was not tried as encoder" | Interspeech Sec. 3.3 | correct, not credited | The authors say they would like to try it "but the weights are not publicly available". The review presents this as a shortfall without that reason. |
| 11 | v3 App. 8.2: AV-HuBERT and CMA ahead at SNR ≤ 0 | v3 App. 8.2 | correct | Credited as "the revision finds". |
| 12 | "Significantly" (Sec. 1) has no test or seeds | Interspeech Sec. 1, 3 | correct | v3 App. 8.2 itself notes that differences "might be due to different random seeds"; could be credited. |
| 13 | Noisy BLEU 20.5 vs per-pair 20.8; video lifts 18.6 to 20.5; clean 22.9 vs 21.9, audio-only 22.7 (M08, Verdict) | Interspeech/v3 Table 4, Sec. 3.4 | correct | The authors state the noise-file difference themselves (Sec. 3.4; v3 Table 4 caption: "not directly comparable"). |
| 14 | MuAViC noise file differs, so 20.5 vs 20.8 is not like-for-like (Where-claims) | Interspeech Sec. 3.4 | correct, author caveat | This repeats the authors' own caveat and does not show an overreach. The Verdict meanwhile states "not in noisy BLEU (20.5 against 20.8)" without that qualifier. |
| 15 | DoubleHelix 3.8% at 0 dB babble, 0.68% clean, frozen Whisper and AV-HuBERT, 1,759 h (M06 SOTA) | DoubleHelix Sec. 4.3, Table 2, Sec. 4 | numbers correct, conditions missing | DoubleHelix's own Table 2 gives AVGER 3.7% at 0 dB, lower than DoubleHelix. Its decoder is a 3B LLM with LoRA on Whisper-medium. Its babble noise file is not specified, and its results are single runs. The review also says the target uses "more training hours", but v3 shows Whisper-Flamingo at 5.6% with 1,759 h as well, so hours do not explain the 1.8-point gap. |
| 16 | DoubleHelix reference: "Cheng, Z." | DoubleHelix p. 1; arXiv citation_author meta | wrong | Three authors: Ziwei Cheng, Zhenhua Tan, Zhuomin Zhu. The page header also reads "MM '26". |
| 17 | 0.76% for Whisper-Flamingo at 1,759 h, beam 1; 0.08 points behind DoubleHelix (M03 SOTA) | v3 Table 3, Sec. 3.3 | correct, condition missing | 0.76% is the model trained without noise. The noise-trained model scores 0.86%. Audio-only fine-tuned Whisper-Large also reaches 0.68% (v3), so clean LRS3 cannot rank training regimes. |
| 18 | MTC-AVSR noisy BLEU 25.2/23.5/20.3/20.5 vs Whisper-Flamingo Large 25.4/22.4/19.3/19.9; bilingual AV-HuBERT French 23.8 (M08 SOTA) | MTC-AVSR Table 2, Sec. 3.3 | correct, conditions missing | MTC-AVSR trains with MUSAN babble (Sec. 3.1) and says itself that the noisy files are not released, "preventing a direct like-for-like comparison". The 13-components table cell picks Es 25.2, which is below the target's 25.4. |
| 19 | USR 2.0 reports mean and SD over three seeds on LRS3 (M12 SOTA) | USR 2.0 App. Table 13 | correct, condition missing | Only in the appendix training-duration table: Base models, low-resource setting, 50 epochs. The main results are single numbers. |
| 20 | Code fixes seed 3407 (M12) | repo `whisper_ft_muavic.py` l.30, `whisper_decode_video.py` l.49 | correct | The claim-table quote (the A6000 GPU line) does not support it; the code does. |
| 21 | TM-seq2seq attends separately to audio and video in each decoder layer [2]; AVFormer froze ASR and visual extractor [3]; prompting fed CLIP labels [6] | notes p1-p4 | correct | The quotes are thin but they match. |
| 22 | The 2 prior translation systems are MuAViC per-pair [4] and MixSpeech from lip video [7] | notes p5, p6; target Sec. 3.4 | insufficient quote | Quote p5 is about noise and p6 about AVMuST-TED gains. "Per pair" is supported by the target's Sec. 3.4, not by the MuAViC quote. The facts are right as far as known. |
| 23 | Usual approach counts: 97/14/0 of 159 (M06), 166/15/9 of 359 (M03), 552 of 570 (M08), 125 of 159 (M12) | audits `dated_pattern_counts_*` | tallies correct | All match the audits; 12 [later] gated hits match. 552 and 125 are complements (570 - 18; 159 - 34), so they are lower bounds on "no such pattern", not upper bounds. The Appendix's blanket "(upper bounds)" is wrong for them. "Output only a transcript" overstates what 570 - 18 measures. |
| 24 | Chronology window: prior before 2023-12, [concurrent] 2023-12 to 2024-12 | audit cutoffs | approximately correct | Month-level rounding of ±6 months from 2024-06-14. VSP-LLM (2402), XLAVS-R (2403) and SynesLM (2408) are correctly [concurrent]. |
| 25 | "New is the combination with lip features" (M06); "M03 ... is AVFormer's regime" | target refs [5]-[7], Table 3; `arxiv-2312.13873` | incomplete | The target's own Table 3 compares with Adaptive AV [7] (Simic and Bocklet, arXiv 2312.13873, ICASSP 2024). That work freezes Whisper and trains an audio-visual fusion module on LRS3 lip features with babble noise. It is in the ledger and [concurrent] by the review's window, but not named. FAVA [6] (May et al., ASRU 2023, audio-only ASR fine-tuned with lips) is not named either. |

## Required fixes, ordered by severity

**H1 (high). Location: Verdict, "Where the claims outrun the evidence" (first two bullets), "Questions for the authors" (first question).**
Evidence: v3 Sec. 3.3 no longer contains "improves the clean WER from 2.3% to 1.5%". It reports clean results at beam 1 (0.85% audio-only vs 0.86% Whisper-Flamingo, 1,759 h, "results are close"). It replaces 52.1% with "49.5% relative noisy WER improvement". It reports beam 1 and beam 15 for every own model (Table 3), and App. 8.1 to 8.2 explain that beam 1 is better for SNR > 0 and beam 15 for SNR ≤ 0. The review presents the beam-1 parity as its own finding against the paper ("the main overreach") and asks the authors a question their revision already answers.
Fix: say that the Interspeech/v1 clean-gain claim outran its evidence and that the authors themselves withdrew it in arXiv v3 (Sec. 3.3, Table 3, App. 8.2). Replace the beam-15 question with one v3 leaves open, or drop it.

**H2 (high). Location: M06 "State of the art"; 13-components table, M06 row.**
Evidence: DoubleHelix Table 2 lists AVGER at 3.7% at 0 dB, below DoubleHelix's 3.8%. DoubleHelix decodes with a LoRA-tuned 3B LLM on frozen Whisper-medium and AV-HuBERT. It does not identify its babble noise file and reports single runs. v3 Table 3 shows Whisper-Flamingo at 5.6% with 1,759 h too, so "with more training hours" misattributes the gap.
Fix: state the deciding conditions (LLM decoder, different and unspecified babble file, single run, both systems at 1,759 h). Mark the 1.8-point gap as not like-for-like. Either name the lower 0 dB value DoubleHelix itself tabulates, or restrict the claim to clean and average WER.

**H3 (high). Location: M06 evidence paragraph ("New is the combination with lip features"); M03 ("AVFormer's regime"); Appendix "Read:" lines.**
Evidence: The target's ref. [7], Simic and Bocklet, "Self-supervised adaptive AV fusion module for pre-trained ASR models" (arXiv 2312.13873, Dec 2023; ICASSP 2024), freezes Whisper and trains a cross-attention fusion module on LRS3 lip features with babble noise. The target compares with it in Table 3 ("Adaptive AV"). It is in the ledger (all four audits list it) and is [concurrent] under the review's window. FAVA [6] (May et al., ASRU 2023) fine-tunes an audio-only ASR with lip input and is also cited and tabulated by the target.
Fix: name both as [concurrent] works that the target itself cites, described through the target's citation where not read. Qualify "new combination" to gated cross-attention inside the pretrained decoder. For M03, note that a frozen Whisper plus trained lip fusion was concurrent and appears in the target's own Table 3.

**M1 (medium). Location: M06 evidence and verdict sentence; M03 "no unfrozen control is shown".**
Evidence: Interspeech Sec. 3.2: early and late fusion fine-tune all of Whisper, while Whisper-Flamingo freezes it. The audio-visual gain over audio-only is repeated across three model sizes and two datasets (Table 4 noisy rows: 16.7 to 18.5, 17.6 to 19.6, 18.6 to 20.5 BLEU; LRS3 Tables 2 and 3).
Fix: (a) Name freezing as the confound in the early-fusion vs gated comparison. (b) Rewrite the M03 sentence as "no unfrozen gated cross-attention variant". (c) Give the verdict reason as "the advantage over alternative fusion designs rests on one Medium run" instead of "ahead would need repetition across seeds, sizes or datasets", since the gain over audio-only is repeated across sizes and datasets.

**M2 (medium). Location: "Where the claims outrun the evidence", second bullet.**
Evidence: v3 Table 3 and App. 8.2. Both comparisons use the same beam size for both models. The gain is 42% at beam 1 and 52.1% at beam 15 (433 h), and the authors revise it to 49.5% at 1,759 h. Beam 15 is the better decoder at 0 dB for both models.
Fix: drop the bullet, or recast it as "the noisy gain holds at both beam sizes (42% to 52%, inference; arXiv v3)". Do not list it as an overreach.

**M3 (medium). Location: M08 "Usual approach"; Appendix opening sentence; M12 "Usual approach".**
Evidence: M08 audit gives 18 translation or BLEU hits among 570; 552 is the complement. The M08 population (1,049 VSR/AVSR studies) is not restricted to transcript output. The M12 audit note itself says 125 "is a lower bound for single-run reporting".
Fix: write "552 of 570 prior VSR/AVSR studies name no speech translation or BLEU (pattern match, Appendix)". Change the Appendix to "positive counts are upper bounds; complements (552, 125) are lower bounds".

**M4 (medium). Location: "Where the claims outrun the evidence" (u-HuBERT, MuAViC noise-file bullets); "What the field needs next" (M12).**
Evidence: Interspeech Sec. 3.3 says u-HuBERT weights are not public. Sec. 3.4 and the Table 4 caption state the different noise file. The authors' public repository (README, "noise.tar.gz") releases their LRS3 and MuAViC babble test noise files.
Fix: credit each as the authors' own caveat, with the reason. Change the field-needs line to ask other groups to adopt the authors' released noise files, or to release their own.

**M5 (medium). Location: M08 "State of the art"; 13-components table, M08 row.**
Evidence: MTC-AVSR Sec. 3.1 mixes MUSAN babble; its Sec. 3.3 says the noisy files differ, "preventing a direct like-for-like comparison". In its Table 2, Spanish is the language where Whisper-Flamingo Large (25.4) beats MTC-AVSR (25.2).
Fix: state the noise difference and that MTC-AVSR covers four of six directions. Change the table cell to a value that carries the claim, for example "one model, 4 directions; best It/Pt noisy BLEU (20.3/20.5), different babble".

**M6 (medium). Location: reference [5] and `.bib` key `cheng2026doublehelix`.**
Evidence: the DoubleHelix PDF p. 1 and the arXiv metadata list three authors: Cheng, Ziwei; Tan, Zhenhua; Zhu, Zhuomin.
Fix: correct the authors. Consider noting the "MM '26" header only if acceptance can be confirmed; otherwise keep "arXiv preprint".

**L1 (low). Location: M12 "State of the art".**
Evidence: USR 2.0 App. Table 13 reports seeds only for Base, low-resource, 50-epoch runs. Its main tables are single numbers.
Fix: add these conditions. Prior studies the audit already read (arxiv-1911.04890, 95% CI on all values; arxiv-2004.08250, 5 repeats) are stronger protocol exemplars. Note them or justify choosing USR 2.0.

**L2 (low). Location: M03 "State of the art".**
Evidence: v3 Table 3: 0.76% is Whisper-Flamingo trained without noise, and the noise-trained model scores 0.86%. Audio-only fine-tuned Whisper-Large also scores 0.68%.
Fix: add "trained without noise". Note that clean LRS3 cannot separate training regimes, because the authors' own audio-only model already ties DoubleHelix.

**L3 (low). Location: Verdict, M08 sentence.**
Evidence: the review elsewhere says 20.5 vs 20.8 is not like-for-like.
Fix: "not ahead in noisy BLEU (20.5 against 20.8 on a non-identical noise file, Table 4)".

**L4 (low). Location: M06 "Usual approach"; M08 clean-BLEU sentence.**
Evidence: Interspeech Sec. 2 says early fusion by addition or concatenation is the common design for both SSL and supervised models. Sec. 3.4 attributes the clean lead over 21.9 to fine-tuned audio-only Whisper (22.7).
Fix: credit both statements to the authors.

**L5 (low). Location: Appendix, chronology sentence.**
Evidence: ±6 months from 2024-06-14 is 2023-12-14 to 2024-12-14. The bins use month granularity from arXiv ids.
Fix: add "month-level" to the window description. No reclassification is needed for the works named.

**L6 (low). Location: `claims.md` rows 18, 22, 23 (not published text).**
Evidence: the quotes do not carry "one model per pair", "from lip video" or "seed 3407".
Fix: attach the target's Sec. 3.4 quote for per-pair models and the code line for the seed.

No Japanese text, model names, process disclaimers or full-text excerpts appear in the published review. The phrases "(published table, appended)" and "Known-item recall 1.0" in the Appendix are internal jargon but follow the required Appendix form. Bibliographic details for [1], [2], [3], [4], [6], [7], [8] and [9] match what I could check (both DOIs resolve to the ISCA archive pages).

## Scores

- Procedure: 6/10. The version check is right: the Interspeech text equals v1, and v3 is used and labelled as the authors' revision. Tallies match the audits, numbers trace to sources, and the code was read. Against that: the target's own closest comparators ([6], [7]) were skipped despite being in the ledger. The state-of-the-art conditions were not read off the comparator papers, and the bibliographic author list is wrong.
- Final text: 6/10. The position is clear and most numbers are exact. The central "main overreach" is presented as the reviewer's discovery although the authors corrected it in v3, and one listed overreach (the noisy gain) is not one. Two state-of-the-art lines compare across noise files without saying so, and several author caveats are not credited.

## Final counts by severity

- High: 3 (H1, H2, H3)
- Medium: 6 (M1 to M6)
- Low: 6 (L1 to L6)
- Total required fixes: 15
