# Triage: Deep Audio-Visual Speech Recognition (evaluation of 2026-11-16)

Each required fix was checked against the target text (arXiv v2) and, where needed, the cited works' text in the wiki, the wiki ledger index and Crossref. Counts: 7 applied (5 correct, 2 partly correct), 1 rejected, 0 unverified.

| # | Fix | Judgment | Evidence location | Action |
|---|---|---|---|---|
| 1 | "had already compared" treats concurrent [2] as prior | correct | [2] arXiv 1806.06053 (June 2018) vs target 1809.02108 (Sept 2018): within 6 months, so [concurrent]; Appendix M06 lists "No prior example" | Verdict and verdict.json "position": "the same group's concurrent paper compares CTC with a Transformer on LRS2 [2] and no prior work does (Appendix), the comparison mixes ...". Verdict stays standard (justified by the confounds). slots.json M06 note updated. |
| 2 | M06 state of the art lacks year/metric/value; [8] and [9] are not benchmark sources | correct | Auto-AVSR (arXiv 2303.14307) §2: "Transformer decoder for joint CTC/attention training"; §4.3: LRS2 WER "14.6 %, 1.5 % and 1.5 %" (visual, audio, AV), LRS3 visual 19.1%, AV 0.9%; Table 3: 3,448 h training data. Suggested values confirmed. | M06 State of the art now cites Auto-AVSR (2023) [8] with LRS2-BBC 14.6% video-only and 1.5% AV against 48.3% / 8.5% here, noting 3,448 h of training data. [8] VoxLRS-SA and [9] ViCocktail removed from this line. New reference added; references renumbered by first appearance. |
| 3 | M11 state of the art: lead with LRS3-TED, demote ViCocktail, table cell [9] -> [3] | partly correct | LRS3-TED (1809.00496) §2: split by video; "it is unlikely that there are many identities that appear in both training and test sets ... contrast to the LRW and the LRS2-BBC datasets". LRS3 is low-overlap by argument, not an enforced speaker-disjoint split, so it cannot be called "speaker-disjoint"; ViCocktail does enforce non-overlap ("ensure that the speakers do not overlap with the training set"), so it stays as a later example rather than being dropped. | M11 State of the art leads with the concurrent LRS3-TED and its stated low overlap, notes later work reports on it [8], keeps ViCocktail (labelled Vietnamese) and VoxLRS-SA as later examples. Table cell changed to "low-overlap split [3]". slots.json M11 "field" updated. |
| 4 | Concurrent LSVSR presented as current state of the art in reporting | correct | LSVSR (1807.05162): "Standard deviations are bootstrap estimates" (2018, concurrent). Auto-AVSR (2023) reports single WER values with no seeds, SD or CI. | M12 State of the art: "single runs remain the norm: the concurrent LSVSR (2018) is an early exception ...; Auto-AVSR reports single values [8]". Table cell updated. |
| 5 | Binomial SE stated as if exact; ignores clustering and pairing | correct | Arithmetic: sqrt(0.085 x 0.915 / 6663) = 0.0034; gap 8.5 - 8.2 = 0.3 (Table 2). | Sentence rewritten as a binomial approximation that ignores utterance clustering and pairing, marked "(inference)". slots.json M12 note updated. |
| 6 | Reference [14] (Sterpu et al.) never cited | wrong | The review cites it in the Appendix, M06 excluded examples ("Sterpu et al. [14] (seq2seq vs seq2seq with joint CTC, no CTC alone)"); the evaluator's compact version omitted the Appendix. The gate's "every reference cited" check passes. | Rejected. (After renumbering it is [15].) |
| 7 | Reference [1] bibliographic data incomplete | correct | Crossref for doi:10.1109/TPAMI.2018.2889052: volume 44, issue 12, pages 8717-8727, issued 2022-12. (The wiki manifest's "41(12) 2019" is wrong.) | Reference 1 now reads "vol. 44, no. 12, pp. 8717-8727, 2022 (early access 2018)"; title line "IEEE TPAMI 44(12), 2022 (early access 2018)"; refs.bib entry updated. |
| 8 | Curriculum wording reads as an accusation of borrowing | correct | Target §5.2 and WLAS (1611.05358) §3.1 both say "We introduce a new strategy where we start training only on single word examples"; WLAS authors Chung, Senior, Vinyals, Zisserman are all co-authors of the target. | Rewritten: "The curriculum (§5.2), called "a new strategy", repeats the authors' own WLAS curriculum (§3.1 of [5])." slots.json M03 note updated. |

## Items the evaluator marked "insufficient evidence" (claim table), now checked

| Claim | Result | Evidence |
|---|---|---|
| 50.0% for the group's own Transformer in [2] | confirmed | [2] results table, TM row: 50.0% |
| Noisy: CTC 23.6%, seq2seq 34.2%, Google S2T 86.3% | confirmed | Target Table 2, Noisy block (LRS2-BBC, + extLM for TM models) |
| Beam 100 vs 35, alpha 0.5 vs 0.1; beam 6 without LM | confirmed | Target §6 "Beam search"; Appendix C (W = 6, alpha = 0.0 without LM; W = 35, alpha = 0.1 with LM); Appendix D (W = 100, alpha = 0.5) |
| GPU GTX 1080 Ti (§5.4) vs Titan X (§6.4) | confirmed | Target §5.4 "single GeForce GTX 1080 Ti GPU with 11GB"; §6.4 "single GeForce Titan X GPU with 12GB" |
| LRS3 paper says LRS2-BBC people likely recur | confirmed | LRS3-TED §2 (quoted above) |
| M09 and M10 both slot-filled 82 | confirmed | Wiki ledger index fill rates: M09 82 / 7,388 unique, M10 82 / 7,388 unique |

No item remains unverified; verification_status in verdict.json is empty.

## Other edits made to pass the format gate

- M12 section: "Usual approach" and "State of the art" now on their own lines, as the gate requires; State of the art gives a year.
- "### Inherited" heading (no slot named, no Usual approach line) folded into a bold "Inherited:" paragraph.
- Body length trimmed to stay within 7,000 characters (6,941; original 6,513).
