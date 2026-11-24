# Evaluator: a language model separate from the writer

Target: Lee, S., Shin, Y. "Movement Detection of Tongue and Related Body Parts Using IR-UWB Radar." arXiv:2209.01762, 2022.
Date: 2026-11-24. Inputs: evaluator brief and `compact.md` only (review, references, claim table). No source text, web, or other work files were opened; checks rest on the claim-table quotes, internal consistency, recomputation, and outside knowledge (marked "unverified" where I cannot locate it).

## Claim check table

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Chin placement, RMS envelope into GMM–HMMs (Verdict) | Claims 1, 11 (t1, t15, t17, t30) | correct | t17: one Gaussian per state, so "GMM" means a single-mixture HMM (see finding 12). |
| 2 | Chin placement "rare (Appendix)" | Appendix M05 pattern counts | wrong as worded | Appendix gives chin 6 vs mouth/lips/face 5; see finding 1. |
| 3 | [2]: chin worse, 70.59 vs 86.47 on vowels | Claims 2, 7 (ct23, ct24, ct27) | insufficient quote | Row labels Upper/Lower match; no column header (vowels) or method row (FERASEC + DNN–HMM) is quoted. |
| 4 | Envelope beats CLEAN for all four participants | Claims 3, 13, 14 (t26, t35, t37–t44) | correct | 100/90/90/90 vs 85/65/80/70 and 82.5/72.5/82.5/57.5. |
| 5 | Mean error 25% to 7.5%, 70% relative (inference) | Recomputed | correct | (100-75)=25, (100-92.5)=7.5, 1-7.5/25=0.70. |
| 6 | Sign test p=0.0625; 36/40 CI about 77–96% | Recomputed | correct | 0.5^4=0.0625; Wilson 76.9–96.0%. |
| 7 | Pooled 148/160, CI about 87–96%, chance 50% | Recomputed (t52, t54) | correct | 40+36+36+36=148; Wilson 87.3–95.7%; 20/20 per class gives 50%. Pooling ignores participant clustering (finding 10). |
| 8 | LOOCV within participant, 40 trials, 4 participants, one an author | Claim 4 (t23, t60, t4, t5) | correct | |
| 9 | "The 100% participant is an author" | Claim 20 (t5, t41) | insufficient quote | Quotes show an author participated and one participant scored 100; nothing links the two. Same for "best 2016 speaker" (cp4 names Speaker 5 as an author, not as best). |
| 10 | Authors concede throat muscles move with the tongue (§IV); §V capability quote | No claim-table row | insufficient quote | Verdict and first "outrun" bullet rest on unquoted text. |
| 11 | 2016 predecessor at 10–16 cm aimed at lips and jaw; target 5–10 cm at chin | Claims 5, 6 (ps1, ps2, t3) | correct | |
| 12 | [2] lip radar 5–10 cm, chin radar 10–15 cm; lip wins with every method and task | Claim 7 (ct13, ct61, ct27) | correct | "consistently improved" supports "every". |
| 13 | Usual approach M05: "external non-contact 12, face 11, slot-filled, of 33" | Claim 5, Appendix | insufficient / mixed tallies | Slot-filled numerators placed over a pattern-match denominator; see finding 1. |
| 14 | Only this paper and its successor aim a contactless radar at the chin | Claim 8 (audit) | insufficient evidence | No deciding priors named for the other 4 chin studies; see finding 1. |
| 15 | [2]: chin loses lip information, lip radar suffers tooth occlusion | Claim 9 (ct59, ct39) | correct | |
| 16 | Lineage: two CLEAN features into MD-DTW [3] | Claim 10 (t22, cp14) | correct | |
| 17 | [4]: 91.1% vs 74.0%, one participant, 50 words, leave-one-session-out, same group's testbed | Claim 12 (cs1, cs2, cs9) | partly insufficient | 91.1/74.0 and single participant quoted; "50 words", "leave-one-session-out" and "same group" are not. |
| 18 | Short-template CLEAN keeps only the nearest echo (lips and jaw), which a chin beam misses (inference) | Claim 15 (ps4) | questionable inference | ps4 is about the first reflected pulse in [3], not explicitly the short-template variant; and the chin is part of the jaw (finding 4). |
| 19 | FERASEC lifts chin-radar vowels 40.88 to 66.91 with MD-DTW fixed | Claim 16 (ct20, ct22, ct14) | insufficient quote | Method row labels and column header not quoted; identity of the 40.88 baseline not stated. |
| 20 | M12 usual: speaker-dependent 22 of 32 vs 17 independent; [3] per-speaker CV | Claim 17 (cp3, t23), Appendix | correct | |
| 21 | [5] Lip-Siri: three new users, 81.5–85.5% word accuracy | Claim 18 (cs6) | correct | |
| 22 | 2016 variance motion detector exists and is not a baseline | Claim 21 (ps3, t61) | correct | |
| 23 | GUI-click trials, 1–3 s "regardless of the state" | Claim 22 (t8, t9) | correct | Authors' own statement partly addresses the duration cue (finding 11). |
| 24 | [later] labels for [2] 2023, [4] 2025, [5] 2026 | References vs target 2022 | correct | No later work is treated as prior work or as a missed citation. |
| 25 | Bibliography [2]–[5] | Reference list | [3] plausible; [2], [4], [5] unverified | [3] Sensors 16(11):1812 matches my recollection; ICCE-Asia DOI and Lip-Siri author list unverified. |

## Findings (required fixes, ordered by impact)

1. **M05 "rare" and "usual approach" conflict with the Appendix.** The Appendix pattern counts give "toward or under the chin 6" against "toward the mouth, lips or face 5", so chin placement is not rarer than mouth placement in the ledger. The point the review needs is narrower: a *contactless* radar under the chin appears in 2 of 33 studies. Also, "external non-contact 12, face as body site 11, slot-filled, of 33" places slot-filled numerators over the pattern-match total (the slot-filled total is 7,329), and 12 of 33 is a minority, which is weak support for calling it the usual approach. Fix: state the usual approach and rarity with counts from one tally, and say "contactless chin-facing radar: 2 of 33 (pattern match)". For the "only this paper and its successor" sentence, name what the other four chin studies are (for example, contact antennas) so the absence claim has its deciding priors.
2. **"The 100% participant is an author" is not supported by the quotes.** t5 says one male participant was an author, and t41 shows one participant at 100%, but nothing quoted links them. The same goes for "like the best 2016 speaker": cp4 identifies Speaker 5 as an author, not as the best speaker. Add the locator that links them (a participant label in Table I or §IV), or drop the sentence. This sentence feeds the M12 position.
3. **The Verdict and the first "outrun" bullet rest on unquoted text.** There is no claim-table row for the §IV throat-muscle concession or for the §V sentence "IR-UWB radar has the capability to detect the movement of invisible tongue". These carry the central position ("detection of closed-mouth movement, not of the tongue"). Add both quotes with locations.
4. **The inference about the chin beam missing the jaw is physically doubtful.** The chin is part of the mandible, so for a radar under the chin the nearest echo *is* jaw motion. The better explanation is that in a closed-mouth rest-versus-palate-touch task the jaw barely moves, so a nearest-echo feature has little to track. ps4 also describes the first reflected pulse in [3], not explicitly the short-template CLEAN variant. Reword, and keep the "(inference)" label.
5. **The [2] comparison in the Verdict leaves out its main confound.** In [2] the chin radar was at 10–15 cm and the lip radar at 5–10 cm, while this paper used the chin at 5–10 cm. The tasks in [2] (vowels, consonants, words, phrases) also depend heavily on the lips. "Found it worse" in the Verdict should carry this caveat. The M05 section half-handles it with "complementary channel".
6. **The Table 2 values from [2] lack column and row labels in the quotes.** "On vowels with FERASEC + DNN–HMM" (70.59 / 86.47) and "MD-DTW fixed … 40.88 to 66.91" each rely on a column header and a method row that are not quoted. Nothing says what the 40.88 row is (CLEAN + MD-DTW?), yet "lifts from" implies it is the CLEAN baseline. Quote the header and the row names.
7. **The M06 state of the art [4] is partly unquoted and a weak benchmark.** "50 words", "leave-one-session-out" and "the same group's testbed" (cs9 points to "[26]" without naming the group) are not in the quotes. A single-participant result on 50 words is also thin as the field's best for radar SSR input representations. Possible stronger or broader candidates, all unverified: Ferreira et al., "Exploring Silent Speech Interfaces Based on Frequency-Modulated Continuous-Wave Radar", Sensors 2022 (FMCW); Birkholz et al., non-invasive silent phoneme recognition with microwave signals, IEEE/ACM TASLP 2018; Digehsara et al., radar SSR headset, Interspeech 2022. Check these against the ledger, or state that [4] is the best *IR-UWB* result rather than the best radar result.
8. **"Both are standard [1]" cites the target for a field judgment.** [1] supports what the paper did, not that it is standard. The M05 `standard` verdict also sits uneasily with the review's own statement that chin placement is not the usual approach. I could not check this against the SKILL.md verdict rules, but the review should give one line on why an unusual, untested placement is still `standard`.
9. **The M06 body drops "upper bound".** The Appendix gives "engineered features 21 (pattern match, upper bound)", but the body says "21 of 32 radar studies, pattern match" without the qualifier. Add it.
10. **The statistical framing is loose (inference lines).** Overlap of the 36/40 interval with P3's 82.5% says nothing about a paired difference, and the sign test already makes the point. The pooled 148/160 interval treats trials as independent across four participants with very different scores (one at 100%). Say "approximate, ignores participant clustering", or report per-participant intervals only.
11. **The duration-cue point understates the authors' own statement.** §II-A says trials lasted 1–3 s "regardless of the state", which the authors offer as a control. Both class HMMs are also scored on the same sequence, so duration acts only through state occupancy. Keep it as a question, but soften "not excluded" to "not shown per state".
12. **Single-Gaussian emissions.** t17 says each state uses "a single mixture Gaussian". Note this in M06 ("Gaussian-emission HMMs") so the reader does not assume mixture models.
13. **The M12 state-of-the-art comparator differs in task.** [5] reports open-vocabulary word and sentence recognition by Wi-Fi backscatter, against binary state detection here. It is inside the declared population, but add a clause noting that the task differs, so the 81.5–85.5% is not read against this paper's 92.5%.

## Strongest confound and position check

The strongest confound for the central claim (tongue movement detection) is that the target signal is not separated from throat, jaw or head motion. The review handles it well: it relies on the authors' own §IV concession (credited to them, not claimed as its own finding) and asks for an ultrasound reference. The feature-versus-classifier confound in Table I is also named. The positions are generally backed by locations. The exceptions are findings 2, 3 and 6, where the quotes are too thin, and finding 1, where a position contradicts the review's own Appendix counts.

## Scores

- Procedure: 7/10. Arithmetic, chronology and most quotes check out; several load-bearing quotes are missing; the tallies are mixed in M05.
- Final text: 7/10. The position is clear and well hedged, but the M05 rarity claim, the author-participant link and the chin/jaw inference need correction.
