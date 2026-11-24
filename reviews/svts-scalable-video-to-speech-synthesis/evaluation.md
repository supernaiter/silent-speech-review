# Evaluator: a language model separate from the writer

Date: 2026-11-24. Target: SVTS: Scalable Video-to-Speech Synthesis (Mira et al., arXiv:2205.02058, 2022).
Input read in full: `wiki-context/skill-draft/references/evaluator-brief.md` and `compact.md` (review plus claim table). I did not open the writer's other work files (claims.md, notes, drafts, audit, prep). I used grep on the extracted source texts in `reader1/` (target, [2], [5], [6], [7], [8], [9], [10]) only to check quoted passages. LipSound2 [3] has no source text there, so I could not check it.

## Claim table

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Frozen LibriTTS Parallel WaveGAN; 1,556 h LRS3+VoxCeleb2 (Verdict) | target §2.1, Table 2 | correct | |
| 2 | VCVTS uses the same vocoder [2] (Verdict) | [2] Sec. 3 | correct | VCVTS uses GL **or** a LibriTTS-trained PWG, so "same vocoder" holds for one of its two settings |
| 3 | LipSound2 pre-trained on about 2400 h of VoxCeleb2 [3] (Verdict, M03) | claim-table quote only | insufficient quote | The quote says "∼2400h multi-lingual" and does not name VoxCeleb2. No source text was available to check |
| 4 | Later table: SVTS-S 2.37% GRID, SVTS-M 12.90% LRW [4] | claim-table quote | correct (quote) | Re-scored by the same lab, so it is not an independent replication. "Gains hold" should say that |
| 5 | V2SFlow: SVTS 78.0% WER vs V2SFlow-A 28.5% on SVTS's unseen split [5] | [5] Sec. III-A, Table I | correct | V2SFlow "adopt[s] the un-seen train-test split from SVTS". It scores WER against **ground-truth text labels**, while SVTS's protocol uses the transcript of the real audio. Not stated in the review |
| 6 | LipVoicer 21.4% on unseen LRS3 with lip-reader text [10] | [10] Table 4, §5 | correct | LipVoicer used "the LRS3 test files provided by the authors of SVTS" |
| 7 | GRID-seen 2.36 vs 4.60; LRW 13.40 vs 37.07 (Table 2) | target Table 2 (via claim table) | correct (quote) | |
| 8 | Griffin-Lim 2.41 vs PWG 2.36 (Table 3) | target Table 3 | correct | GL was computed on CPU (asterisk), which does not change the WER |
| 9 | 27.3 to 87.6 M parameters (Table 1) | claim-table quote | correct (quote) | |
| 10 | STOI 0.507→0.530, ESTOI 0.271→0.313, PESQ 1.25→1.26; +4.5/+15.5/+0.8% (inference) | Table 2 quote; arithmetic | correct | 0.023/0.507 = 4.5%; 0.042/0.271 = 15.5%; 0.01/1.25 = 0.8% |
| 11 | "the significant boost on all metrics" (§4.1) | target §4.1 | correct | |
| 12 | Random same-speaker clip for GRID/LRS3; the same video's audio for LRW (§3.1) | claim-table quotes | insufficient quote | The quotes "audio clip from the same speaker" / "using the audio clip" are thin. The LRW same-clip point is load-bearing for M07 and needs a fuller quote |
| 13 | SECS 0.851 vs 0.557; V2SFlow-V 28.5% [5] | [5] Table I | correct | |
| 14 | SVTS reports only objective metrics, WER only on GRID/LRW, plus the authors' own listening | target §3.4, §4.1, Table 2 caption | correct | The authors themselves warn that "no objective speech metric correlates perfectly with human perception" (§3.4) and ask readers to listen. The review does not credit this self-stated caveat |
| 15 | V2SFlow MOS: SVTS naturalness 1.03, intelligibility 1.49 [5] | [5] Table II | correct | 30 domain experts, 40 clips |
| 16 | 32 listeners, 85% word accuracy on GRID [6] | [6] Abstract, Sec. IV-B | correct | |
| 17 | 20 workers per sample [7] | [7] Sec. 5.2 | correct | |
| 18 | 20 listeners [8] | [8] | correct | |
| 19 | Unseen GRID 17.85 vs 16.12; the authors concede it (§4.1) | target §4.1 | correct | Correctly presented as the authors' own admission |
| 20 | "This strong performance is a consequence of our SVTS architecture" (§4.1) | target §4.1 | correct, with a location issue | The sentence is in the **LRW** paragraph, not about LRS3 or VoxCeleb2. The point that size and data are confounded still holds, since the model gets bigger for larger datasets |
| 21 | No seeds or repeated runs; 2.36 vs 2.90 read as "clearly superior" (§4.2, Table 4) | target §3.3, Table 4 | correct | |
| 22 | M12 verdict "behind", best comparable [6] | see Finding 1 | rule formally met; comparator choice weak | |

## Numbered findings

1. **M12 "behind": the rule is formally met, but the comparators chosen are not the most comparable.** The rule asks for three or more earlier comparable papers, the best one read and named, and a judgment on protocol rather than results. The review cites three earlier papers ([8] 2015, [6] 2017, [7] 2017). All three are in the M12 "Read in full" list. The best one ([6]) is named, and the verdict sentence states a protocol ("32-listener word-accuracy test"), not a score. So the letter of the rule is satisfied. Two weaknesses remain:
   - (a) All three comparators are GRID, speaker-dependent studies from 2015–2017. They are comparable only to SVTS's GRID setting, not to the LRW and LRS3 settings that carry the paper's main claim. Earlier multi-speaker or large-vocabulary works with human tests are cited by the target itself and would be closer comparators: Lip2Wav (Prajwal et al., CVPR 2020, target ref [32]) and Ephrat et al. ([10]/[11] in the target). These are outside knowledge and unverified here.
   - (b) The comparator sentence repeats a result ("85% word accuracy") next to the protocol. That blurs the "protocol, not results" basis. Drop the number or mark it as descriptive.
   - Required: either keep [6] as the best comparable for GRID and say explicitly that the verdict rests on the GRID protocol, or read and name a multi-speaker prior such as Lip2Wav as the best comparable.

2. **The review missed a second later, independent listener test of SVTS that was in a paper it read in full.** LipVoicer [10] ran an LRS3 MOS test on generated files the SVTS authors supplied themselves. It had 16 annotators per sample and filtered out unreliable Turkers. SVTS scored intelligibility 2.17 and naturalness 2.15 (Table 2), and LRS3 WER 82.4% (Table 4). The review cites LipVoicer only for its own 21.4%. This evidence strengthens the LRS3 verdict and the M12 section because it uses the authors' own outputs, not a reproduction. Its MOS (2.17) also differs a lot from V2SFlow's (1.49). That difference shows that MOS values from different tests are not comparable, and the review currently quotes one MOS as if it were definitive.

3. **WER protocol mismatch in the main comparator (strongest confound, not handled).** V2SFlow's 78.0% is computed against ground-truth text labels with its own ASR [5]. SVTS's protocol uses the transcript of the real audio as the reference (§3.4). LipVoicer's 82.4% is a third setting. The roughly 50-point gap is large enough to survive this difference. Still, the Verdict should note that 78.0% is not on SVTS's own WER definition. It should also note which SVTS checkpoint (LRS3-only or +VoxCeleb2) the later papers evaluated, because neither the review nor the quoted passages say.

4. **The LipSound2 VoxCeleb2 claim rests on an insufficient quote** (Verdict, M03). The quote says only "∼2400h multi-lingual". Either quote a passage that names VoxCeleb2 or drop "of VoxCeleb2".

5. **The M07 LRW same-clip claim needs a fuller quote.** "Using the audio clip" does not show that the embedding comes from the test utterance's own audio. This is the basis of the leakage point ("the generator thus receives the test utterance's own audio"), so the quote and location must carry it.

6. **Location error for the "consequence of our SVTS architecture" quote.** In §4.1 the sentence closes the LRW paragraph, but the review uses it against the LRS3/VoxCeleb2 scaling. Reattach it to LRW (where model size also grows), or use the §1 "deeper and wider for larger datasets" text alone.

7. **Internal inconsistency in the target that the review missed.** In Table 4, "w/o Spec. Conv." has PESQ, STOI and ESTOI identical to the full model (1.97 / 0.705 / 0.523) to three decimals. Only WER differs. This may be a copy error in the table. It weakens the "clearly superior" reading further and belongs in "Where the claims outrun the evidence" or in a question for the authors.

8. **The authors' self-stated caveat is not credited (fairness).** The authors themselves state that objective metrics do not match human perception (§3.4) and that no ASR worked on LRS3 (Table 2 caption). The review presents "no LRS3 WER, no listener test" as its own criticism. Add "as the authors note" for the LRS3 WER absence.

9. **The "gains hold in a later table" wording overstates independence** (Verdict). [4] comes from the same lab (Pantic) and re-scores SVTS. Say "re-scored by the same group" rather than implying replication.

10. **The M06 state of the art compares whole systems, not synthesis paths.** V2SFlow (rectified flow over decomposed speech attributes) and LipVoicer (diffusion with lip-reader text and ASR guidance) differ from SVTS in far more than the mel-predictor and vocoder path. That is acceptable as a "best work today" line, but the section verdict ("the vocoder is not the source of the gain") is supported only by Table 3, and the review should not suggest that the state-of-the-art gap concerns M06. LipVoicer also uses ASR guidance at generation. If its WER recognizer overlaps with the guidance recognizer, 21.4% is optimistic (unverified; check §5).

11. **Component labels in the 13-component table do not match the section headings.** M07 is labelled "Lexicon and LM" but holds the speaker embedding. M06 is labelled "Processing and decoding" and M03 "Training and adaptation", while the sections call them "Synthesis path" and "Training scale". This is acceptable if the labels are the fixed schema names, but the M07 row reads as a mismatch to a reader. Consider a parenthetical.

12. **State of the art may be out of date (unverified).** The LRS3 state of the art is given as 2024 (V2SFlow) and 2023 (LipVoicer). Work from 2025 on LRS3 lip-to-speech may report lower WER, for example text- or unit-conditioned diffusion and DiT systems. I cannot name a value with a locator, so this is a check to run, not a required fix.

## Required fixes, ordered by impact

1. Add LipVoicer's independent SVTS evaluation (82.4% LRS3 WER, MOS intelligibility 2.17 on author-supplied samples, 16 annotators per sample) to the Verdict, the M12 section and "Where the claims outrun the evidence" (Finding 2).
2. M12: state that the three priors are GRID speaker-dependent studies and limit the "behind" basis to that protocol, or name a multi-speaker prior as the best comparable. Remove the 85% result from the basis sentence (Finding 1).
3. Note the WER-reference mismatch (ground-truth text vs real-audio transcript) and the unknown SVTS checkpoint behind 78.0% (Finding 3).
4. Fix the insufficient quotes for LipSound2/VoxCeleb2 and for the LRW same-clip embedding (Findings 4, 5).
5. Relocate the "consequence of our SVTS architecture" quote to its LRW context (Finding 6).
6. Add the Table 4 identical-row inconsistency, credit the authors' own caveats, and reword "gains hold" (Findings 7–9).

## Scores

- Procedure: 7/10. Numbers check out against the sources, and the M12 rule is followed to the letter. However, a later independent evaluation of the target in a paper the writer read in full was missed, and two quotes are too thin.
- Final text: 7/10. The position is clear and well cited, but the main LRS3 case leans on one later test without its protocol caveat.
