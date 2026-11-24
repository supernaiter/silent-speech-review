# Evaluator: a language model separate from the writer

Date: 2026-11-24. Target: FastLTS (Wang & Zhao, ACM MM 2022, arXiv:2207.03800).
Inputs: `wiki-context/skill-draft/references/evaluator-brief.md`, the review `compact.md` (with its claim table). For table headers, row labels and conditions, I grepped only the target's source text (`papers/arxiv-2207.03800/source/sc_text.txt`), as brief step 1 and the "read the column header" rule allow. I did not open the writer's other work files or the comparator sources. Statements about comparators that come from my own knowledge are marked "unverified".

Note on the rule: the evaluator brief spells out verdict rules only for `ahead` (step 7). I took the rule for `behind` from the task statement ("at least three earlier comparable papers, the best one read and named"). I did not read SKILL.md itself.

## Numbered findings (ordered by impact)

1. **The M12 "behind" verdict does not meet the rule (at least three earlier comparable papers, the best one read and named).** The M12 section names one earlier comparable paper: Lip2Wav [4]. Its other two comparators are later: SLTS [5] (2023) and RobustL2S [7] (2023). They cannot count as earlier work, and a later paper may not carry a verdict against the target (brief step 5). Mira et al. [2] is prior and reports objective metrics on GRID, but it is not used under M12. The Appendix gives the tally "STOI or ESTOI 56 (15 prior)" but names none of those 15 prior papers. So the review never shows that Lip2Wav is "the best comparable work", as the Verdict line says. Required fix: name at least three prior video-to-speech papers that report STOI/ESTOI (or that use the same Lip2Wav or GRID protocol), say which is best and that it was read, or else drop the verdict to `standard`.

2. **The M12 performance evidence is cherry-picked, and it contradicts the target's own tables.** The review says "its Table 1 shows lower intelligibility than Lip2Wav on Chemistry Lectures", and "Its own MOS agrees with RobustL2S". In the source, Table 1 (Intelli. column) gives:
   - Chess Analysis: FastLTS 3.82±0.10 vs Lip2Wav 3.51±0.09.
   - Chemistry Lectures: 3.73±0.11 vs 3.88±0.10.
   - Hardware Security: 3.89±0.13 vs 3.57±0.11.

   Table 3 (GRID) gives 3.68±0.09 vs 3.47±0.13. FastLTS is therefore higher on intelligibility in 3 of the 4 conditions. Its only deficit, on Chemistry Lectures, lies within overlapping 95% confidence intervals (3.62–3.84 vs 3.78–3.98). The review reports only the unfavourable condition, both in the Verdict and in M12. Required fix: report all four conditions, or drop the performance argument from the M12 verdict.

3. **The M12 verdict mixes protocol with result and goes against the review's own usual-approach counts.** M12 is the evaluation slot. By the review's own Appendix, a listener test is the most common protocol (83 of 165), ahead of STOI/ESTOI (56). FastLTS also reports an objective metric, PESQ on GRID. The authors give an explicit reason for omitting STOI/ESTOI (§5.3, lines 571–586: GAN outputs with different intonation are penalized). The review mentions this reason but does not answer it. At most, the evidence supports "narrower than its baseline's protocol on Lip2Wav (no STOI/ESTOI/PESQ there)". It does not support "behind the field". The phrase "against the best comparable work" is stronger than the evidence (see 1).

4. **Chronology: VCA-GAN [6] is labelled [concurrent] and listed as an arXiv 2022 preprint.** To my knowledge, VCA-GAN (Kim, Hong, Ro) appeared at NeurIPS 2021 (Advances in Neural Information Processing Systems 34). That is more than 6 months before the target (arXiv July 2022), so it would be prior work, not concurrent. The arXiv id 2204.01726 is a later posting. This is unverified (I did not open the source), but I am fairly confident. Required fix: check the venue and year, correct the reference, and change the label to prior.

5. **The speed "misattribution" is presented as the reviewer's own finding, but the authors already separate the two effects.** §5.5 (lines 921–923) says the mel-level comparison is made "to eliminate the effects of using different waveform synthesis methods". It also says (lines 946–948) that "the Griffin-Lim algorithm causes great inference latency in Lip2Wav". The contributions list states both numbers, 9.14× for mel and 19.76× for waveform (lines 152–153). "Misattributed" fits only the abstract, which headlines 19.76× alone (line 32). Required fix: word it as "the abstract headlines the 19.76× waveform figure, which mostly reflects replacing Griffin-Lim, as §5.5 itself notes". Keep the valid point that no parallel mel-plus-neural-vocoder system is timed.

6. **"Timing protocol is not stated" is too strong.** §5.5 (lines 914–917) states the hardware (Xeon E5-2678 CPU, RTX-2080Ti GPU), batch size 1, and the speaker used (Chemistry Lectures). What is missing is warm-up, repetitions and synchronization, which the review's own question for the authors names correctly. Required fix: "warm-up, repetitions and GPU synchronization are not stated".

7. **The PESQ comparison with Mira et al. [2] (2.10 on four seen speakers, Table III) is an insufficient quote.** The quoted row "Ours 2.10 0.595 26.78 7.03 %" has no column header in the claim table, so it is not shown that 2.10 is PESQ (inference that it is the first column). The phrase "which Table 4 omits" also needs care. The target's Table 4 lists "GAN-based [37] 1.684", which may be the 2019 Interspeech conference version by the same group (Vougioukas et al.; the target's reference list includes an Interspeech 2019 DOI at line 1181; unverified that this is [37]). If so, the group's work is represented, though not the journal version. Required fix: quote the column header, and say "omits the journal version".

8. **The state-of-the-art lines (M06, M12) rest on SLTS (arXiv 2023) only, and the speaker assignment is an insufficient quote.** The claim-table quotes c9/c11/c13 give SLTS rows without speaker labels. That 0.757/0.612 belongs to Chemistry Lectures is not shown in the quote, so this is an insufficient quote, not wrong. The reference also lists SLTS as an arXiv preprint. To my knowledge it was published at a 2023 venue (possibly ICCV 2023; unverified). RobustL2S [7] also reports objective metrics on the Lip2Wav speakers, and may be a later or stronger entry for the state of the art (unverified). The review should say whether it checked this. Required fix: add the speaker label to the quote, update the venues, and state why SLTS rather than RobustL2S is taken as the state of the art.

9. **The Table 2 interpretation is fair, but it partly overlaps with a caveat the authors state.** The source (lines 618–620) confirms that HiFi-GAN was trained "on the audios and spectrograms from the Lip2Wav dataset" (ground truth). It also confirms the Chess Analysis quality MOS of 1.35±0.05. The train-test-mismatch reading is a reasonable inference, but it should carry "(inference)". The authors cite Lip2Wav [24] as having observed the same failure (line 624). The review does not mention this, so its counterargument reads as new when part of the context is in the paper.

10. **Minor: "GRID trains the whole model on sampled windows" is supported, but loosely.** The source (lines 475–488) says the sampling-window technique is used for training the wave generator. For small datasets, it says "this will reduce computation cost and memory occupancy while keeping a good performance". The paper does not name GRID explicitly at that point. The reading (small dataset means GRID, so the whole model is trained) is an inference and should be marked as such.

11. **Checked and correct (no fix):**
    - The quote for the transformer front-end novelty claim ("first practical transformer-based visual frontend for lip-to-speech synthesis and lipreading", line 143).
    - The counter-example VTP [3]: arXiv October 2021, prior by more than 6 months.
    - GRID uses three unnamed speakers (lines 504–505).
    - The basis for the memory claim is parameter counts (§5.6: "causing high memory usage", from Table 5's 85.92M vs 50.09M).
    - GlowLTS's 5.337× is quoted at 30 s (line 954).
    - The Lip2Wav stage-2 freeze (lines 483–486).
    - PESQ values: 1.939 for FastLTS and 2.008 for VCA-GAN (Table 4).
    - Table 6 states no dataset or rater count.

## Claim table (selected, at most 25)

| Claim | Where checked | Result | Note |
|---|---|---|---|
| M12 behind, best comparable named | review M12, Appendix | wrong (rule) | Only one earlier comparator (Lip2Wav); see finding 1 |
| Table 1: lower intelligibility on Chemistry Lectures | source Table 1 | correct but selective | Higher on 2 of 3 Lip2Wav speakers and on GRID; CIs overlap |
| Own MOS agrees with RobustL2S | source Tables 1, 3 | wrong as general statement | Holds for one of four conditions |
| FastLTS drops STOI/ESTOI | source §5.3 | correct | Reason stated by authors |
| 9.14× mel, 19.76× waveform | source §5.5, l.32, 152 | correct | "Misattributed" overstated; see finding 5 |
| Timing protocol not stated | source §5.5 l.914–917 | wrong (partly) | Hardware and batch size are stated |
| Memory claim rests on params | source §5.6, Table 5 | correct | |
| GlowLTS 5.337× at 30 s | source l.954 | correct | |
| PESQ 1.939 vs VCA-GAN 2.008 | source Table 4 | correct | |
| VCA-GAN [concurrent] | own knowledge | likely wrong (unverified) | NeurIPS 2021 |
| Mira PESQ 2.10, four seen speakers | claim table c32/c33 | insufficient quote | No column header |
| Table 4 omits Mira | source Table 4 | insufficient evidence | "GAN-based [37]" may be the 2019 version |
| SLTS chem STOI 0.757 / ESTOI 0.612 | claim table c9 | insufficient quote | No speaker label in quote |
| Lip2Wav 0.416/0.284 (Chemistry) | claim table c2/c8 | correct (consistent across two sources) | |
| Table 2 HiFi-GAN on GT spectrograms, 1.35 | source l.537–540, 618–620 | correct | Mark the mismatch as inference |
| Lip2Wav freezes upstream (§4.4) | source l.483–486 | correct | |
| GRID trains whole model on windows | source l.475–482 | correct (inference) | GRID not named at that point |
| GRID three unnamed speakers | source l.504 | correct | |
| "first ... lipreading" fails via VTP [3] | source l.143; VTP arXiv 2110.07603 | correct | |
| Table 6 lacks dataset/raters | source §6 | correct | |
| RobustL2S ten raters, five samples | claim table c25 | correct per quote | |
| Appendix counts | Appendix | not checked | Exact tallies per brief |

## Required fixes, by impact
1. M12: meet the "behind" rule (three named earlier comparators, best one read), or downgrade to `standard` (findings 1, 3).
2. Report all four intelligibility MOS comparisons, and remove "its own MOS agrees with RobustL2S" (finding 2).
3. Fix the VCA-GAN chronology, venue and label (finding 4).
4. Reword "misattributed" and "timing protocol is not stated" (findings 5, 6).
5. Add the missing column and speaker labels for the Mira and SLTS quotes; update the venues (findings 7, 8).

## Scores
- Procedure: 6/10. Quotes and locations are mostly accurate, and the target was checked carefully. The verdict rule was not applied to M12, and the chronology check missed VCA-GAN.
- Final text: 5/10. The M06 analysis is sound. The Verdict's main negative claim (M12) rests on selective evidence and one earlier comparator.
