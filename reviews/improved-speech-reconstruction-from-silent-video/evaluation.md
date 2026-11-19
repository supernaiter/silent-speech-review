# Evaluation: Improved Speech Reconstruction from Silent Video (Ephrat, Halperin, Peleg, ICCVW 2017)

Date: 2026-11-19
Mode: fallback evaluator (claim table only). No sources opened, no web search. Input: compact.md (review sections + claim table). Run by a claude-opus-5-5 subagent in place of sonnet. Items marked "(from memory)" use the evaluator's own background knowledge and were not checked against sources; treat them as leads, not findings.

## Claim check

| # | Claim (section) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Flow lowers STOI 0.670 to 0.665; post-net adds 0.015 (Verdict) | Claim 1, Table 5 quotes | correct (numbers) | 0.665 to 0.68 = +0.015. But see fix 3: M06 section itself shows the full-model row mixes two synthesis paths, so "the post-net adds 0.015" is not a clean post-net effect. |
| 2 | "one GRID speaker in one run" (Verdict, M05) | Claims 1, 13, 27 | insufficient evidence | S3 is inferred by matching Table 5 values to the Table 2 S3 row (sound inference). "One run" is inferred from a single random split; no quote says one run. Acceptable as inference; label it. |
| 3 | S4 STOI 0.584 to 0.700 vs Vid2speech (Verdict) | Claim 2, Table 3 | correct | Speaker label not in quote; row order consistent with Table 2 S4 Lin-synth (0.7 0.462 1.922 3.3). |
| 4 | S3: Le Cornu ESTOI 0.437 vs 0.398, PESQ 2.055 vs 1.974 (Verdict) | Claim 2, Table 3 | correct | |
| 5 | "a [later] ASR re-scoring gives 27.83% / 53.52% vs 14.08% / 31.26%" (Verdict, M12) | Claim 3, Lip2Wav Tables 2-3 | wrong (characterisation) | Numbers match. But Lip2Wav's row for this model has GRID STOI 0.659, ESTOI 0.376, PESQ 1.825, which matches no row of the target's Tables 2-3 (S1-S4: 0.68/0.70/0.667/0.475 etc.). So these are Lip2Wav's own re-run of the method under Lip2Wav's setup, not a re-scoring of the target's outputs. |
| 6 | Unconstrained-dictionary result rests on one of three TCD-TIMIT speakers (Verdict, Outrun) | Claims 4, 25, Table 4 | correct | 0.630 vs 0.318 / 0.357; authors themselves say Lipspeaker 3 "performs best, by a large margin". |
| 7 | 165 studies; 76 mouth, 15 face, 7 flow (M05) | Claim 5 (audit) | not checkable | Ledger tally; outside this check. |
| 8 | Full face gave 40% lower test error than mouth in Vid2speech [2] | Claim 6, Fig. 2 caption of [2] | correct | |
| 9 | "adds a tower over 8 flow fields (Sec. 5)" | Claim 6 / Claim 1 | insufficient evidence | Quote only says K = 9 frames. 8 flow fields is an inference (9 frames give 8 consecutive flows); no quote for the flow-field count. |
| 10 | Lip2Wav uses the face without flow, expects flow to hurt under head motion | Claim 7, Lip2Wav Sec. 2 | insufficient evidence | Quote is truncated ("could be a detrimental feature in unconstrained settings due"); "head motion" and the referent (flow) are not in the quote. Plausible. |
| 11 | Lip2Wav 14.08% vs 27.83% as M05 state of the art | Claim 7 | correct number, wrong use | System-level WER; Lip2Wav differs in encoder, decoder, vocoder and training setup, so it is not evidence about the sensor choice (face vs face+flow). |
| 12 | Best 2023 GRID row 4.07% on four seen speakers [5]; 16.05% unseen [5] (M05, M06, M12) | Claims 7, 12, 18 | no quote | Only "audit state_of_the_art"; no quote or table location from [5]. Values, condition (seen/unseen, which speakers, which ASR) unverified. |
| 13 | Pixels+flow 0.7% lower STOI, 1.4% lower PESQ (M05) | Claim 8 | correct | 0.665/0.670 = -0.75%; 1.921/1.949 = -1.44%. Labelled inference. |
| 14 | Authors say pixels carry most information (Sec. 6.2) | Claim 9 | correct | Fairness: the M05 position is the authors' own conclusion and is credited as such. Good. |
| 15 | 49 neural vocoder, 41 parametric, 16 Griffin-Lim; "15 name a post-net, all others dated 2019 or later" (M06) | Claim 10 (audit) | not checkable / unclear | Counts outside this check. The post-net sentence is ambiguous ("all others" than what?) and reads as an implicit priority claim without naming deciding priors (see fix 8). |
| 16 | Predecessors used LSP [2] and STRAIGHT [3] | Claim 11 | correct content, chronology issue | Quotes support. [3] is labelled [concurrent]; calling it a "predecessor" contradicts that label. |
| 17 | Lip2Wav halves GRID WER [4] | Claim 12 | correct | 14.08/27.83 = 0.51. Same caveat as row 5 (Lip2Wav's re-run). |
| 18 | Full-model Table 5 row = Lin-synth STOI/ViSQOL + Mel-synth PESQ (M06) | Claim 13, Tables 2, 3, 5 | correct | S3 Mel 0.666/0.398/1.974/3.164, Lin 0.68/0.354/1.904/3.349, Ours 0.68/0.398/1.974/3.349. ESTOI also from Mel-synth (not in Table 5). Strong point of the review. |
| 19 | Lin-synth beats Mel-synth on STOI for all four GRID speakers | Claim 14, Table 2 | correct | 0.475>0.442, 0.667>0.631, 0.68>0.666, 0.7>0.644. |
| 20 | Vid2speech 23 MTurk workers, 82.6% on S4 vs 19% chance [2] | Claim 16 | insufficient evidence | Quote "Audio-only 40.0% 82.6%" has two values; the review drops the 40.0% and does not state which condition 82.6% is. The 19% chance applies to a per-category (constrained-choice) task, so 82.6% is probably that condition; must be stated. "S4" not in quote. |
| 21 | Le Cornu and Milner 20 listeners [6], 85% word accuracy [3] | Claim 16 | correct | Listener count is from the 2015 paper [6], the 85% from [3]; attribution is explicit. |
| 22 | Paper reports STOI, ESTOI, PESQ, ViSQOL only | Claim 17 | correct | |
| 23 | "re-scoring shows what objective scores miss": PESQ 1.825 > 1.772 while WER ~2x (M12) | Claim 19, Lip2Wav Table 2 | wrong (judgment) | Same table: STOI 0.731 vs 0.659 and ESTOI 0.535 vs 0.376 both favour Lip2Wav, in line with WER. Only PESQ disagrees. The objective intelligibility scores this paper itself uses did not "miss" the gap. |
| 24 | 82 of 165 name no listener test (M12) | Claim 20 (audit) | insufficient evidence | 165-83 = 82 is arithmetic; "name no listener test" under pattern match is not "objective-only". Labelled inference; acceptable, but wording should not equate the two. |
| 25 | Trails Le Cornu on S3 by 8.9% ESTOI / 3.9% PESQ; leads on S4 by 6.5% / 14.0% (Outrun) | Claim 21, Table 3 | correct | 0.398/0.437 = -8.9%; 1.974/2.055 = -3.9%; 0.462/0.434 = +6.5%; 1.922/1.686 = +14.0%. |
| 26 | S3 "Ours" takes better mode per metric; authors call it "our best results" | Claims 22-23 | correct | Disclosed by authors; review says so. Fair. |
| 27 | "Conclusively demonstrates the superiority" rests on supplementary video | Claim 24 | correct | |
| 28 | Authors concede "not entirely intelligible" (Sec. 6.1) | Claim 25 | insufficient evidence (location) | Notes id t9 sits among early notes (likely the Abstract), while location says Sec. 6.1. Verify the location. |
| 29 | M03 "Per-speaker training" with verdict "not reported"; M11 "Random GRID and TCD-TIMIT splits" with verdict "not reported" (13-component table) | Table vs claim 27 | wrong (internal contradiction) | The paper reports per-speaker training and 80/20 and 90/10 random splits (claim 27). Verdict "not reported" contradicts the row's own content unless it means something narrower (seeds, speaker overlap); if so, say it. |
| 30 | M12 state of the art = 16.05% unseen-speaker WER [5] | Claim 18 | wrong category | For an evaluation component, the state of the art should be an evaluation protocol (e.g. listener transcription plus ASR WER plus MOS on the same clips), not a system score. |

Chronology / fairness: [4] (2020) and [5] (2023) are labelled [later] and used only as state of the art, not as missed citations. Correct. [3] is labelled [concurrent] but called a predecessor in M06 (row 16). The target itself compares against [3], so its use as comparator is fair.

Novelty / absence: no explicit "first / only" sentence. The M06 post-net sentence implies early use; deciding prior not named. (From memory) Tacotron (Wang et al., Interspeech 2017, arXiv:1703.10135, Mar 2017) already used a post-processing net from mel to linear spectrogram followed by Griffin-Lim, before this paper; it should be named as the source of the design.

Verdicts: no slot is `ahead`, so the `ahead` rules do not apply. M12 "standard, a step back from both comparators" is supported by claims 16-17.

State of the art (from memory, unverified): later GRID / LRS video-to-speech work exists after Kefalas et al. 2023 (e.g. diffusion- and speech-unit-based lip-to-speech systems of 2023-2024). Whether any reports a lower GRID WER under the same condition is not checked here; the review should confirm [5] is still the best row under its stated condition. (From memory, low confidence) arXiv:2306.15464 may have a later journal version (IEEE/ACM TASLP, 2024); check and cite the version of record. Vid2speech [2] lacks pages and DOI (ICASSP 2017).

Strongest confound: the Lip2Wav comparison (Verdict, M05, M06, M12) is a different starting point. Lip2Wav re-ran this method in its own setup (its STOI for this model matches none of the target's rows), and it compares whole systems. The review uses that comparison as component-level state of the art for sensors, decoder and evaluation without saying so. The Table 3 comparator-split confound is handled (Outrun bullet 1, Question 29).

## Required fixes (ordered by impact)

1. Verdict, M12: replace "ASR re-scoring" with "Lip2Wav's re-run of this method in its own setup (its GRID STOI for this model, 0.659, matches none of the paper's Tables 2-3)". Say that the 27.83% / 53.52% WER are under Lip2Wav's conditions.
2. M12 body: drop or rewrite "shows what objective scores miss". In the same Lip2Wav table, STOI (0.731 vs 0.659) and ESTOI (0.535 vs 0.376) agree with WER; only PESQ disagrees. Restate as "PESQ ranks the two systems the wrong way round; STOI and ESTOI do not".
3. Verdict: "the post-net adds 0.015" contradicts the M06 finding that the full-model row combines Lin-synth STOI/ViSQOL with Mel-synth PESQ/ESTOI. Qualify it ("+0.015 STOI for the full row, which mixes synthesis paths, M06").
4. M05 state of the art and table cell: the Lip2Wav vs this paper WER gap is a whole-system difference and does not bear on face vs face+flow. Either name a sensor-level comparison or state the gap as system-level context only.
5. M06, M12 state of the art: add quotes and table locations from [5] for 4.07% (four seen GRID speakers) and 16.05% (unseen speakers), with the ASR used. Confirm no later work beats them under the same condition.
6. M12 state of the art: for an evaluation component, state the best evaluation protocol (e.g. listener transcription plus ASR WER on the same clips, with chance level), not a system WER.
7. M12 usual approach: Vid2speech "82.6%" comes from a row with two values (40.0% and 82.6%). Name the condition of 82.6% (likely the constrained per-category choice, to which the 19% chance applies) and give the 40.0% condition, or quote the column headers. Support "S4" with a quote.
8. M06 usual approach: rewrite the ambiguous "15 name a post-net, all others dated 2019 or later" and name the deciding prior for the mel-to-linear post-net with Griffin-Lim (Tacotron, Wang et al., 2017, arXiv:1703.10135, from memory; verify).
9. 13-component table: M03 and M11 say "not reported" while the cells state per-speaker training and random 80/20 / 90/10 splits (claim 27). Change the verdict, or say what exactly is not reported (seeds, number of runs, speaker overlap).
10. M06: [3] is labelled [concurrent] but called a "predecessor". Call it the concurrent comparator, or cite the 2015 predecessor [6] for STRAIGHT if it supports it.
11. M05: "8 flow fields" is not quoted (the quote gives K = 9 frames). Quote Sec. 5 for the flow count or mark it as inference.
12. References and claim 25: add pages and DOI for Vid2speech [2]; check for a version of record of [5]; verify that "not entirely intelligible" is in Sec. 6.1 and not the Abstract (notes id t9).

## Scores

- Procedure: 7/10. The claim table covers every target number with quotes, the arithmetic checks out, and the synthesis-path mixing in Tables 2/3/5 is a strong original finding. Weak points: no quotes for [5], a mischaracterised Lip2Wav comparison, and system-level results used as component state of the art.
- Final text: 6/10. Clear position, fair handling of what the authors disclose, correct inference labels. The re-scoring characterisation, the "objective scores miss" judgment, and the Verdict vs M06 inconsistency on the post-net need fixing before publication.
