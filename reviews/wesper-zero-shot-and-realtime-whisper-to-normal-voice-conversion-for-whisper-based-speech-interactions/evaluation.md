# Evaluation: WESPER review

Date: 2026-11-16. Independent evaluator, single pass, review and claim table only (no source access). The claim table was filled by the writer, not by a separate checker, so a row counts as support only when its quote contains the number or statement itself.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | WESPER needs no per-user training and no paired data | Row 1, Sec. 1 quote | correct | Quote states both. |
| 2 | Google WER 44.70% to 26.68% after conversion | Rows 3, 18 | correct (44.70 in row 18, 26.68 in row 3) | 40% relative is right: (44.70 − 26.68) / 44.70 = 40.3%. |
| 3 | Table 2 gives 13.75% for a whisper-pretrained recognizer without conversion | Rows 18, 20 | insufficient evidence | Row 18 quote is "wTIMIT(W) 44.70 28.38 0.34" with no column headers and no 13.75. The review itself says §5.2 gives 33.06% for that model. The Verdict uses 13.75% as settled. |
| 4 | "About twice as well" without conversion | Row 18 | depends on #3 | 26.68 / 13.75 = 1.94 holds only if 13.75 is the right value. With 33.06% the recognizer does worse than conversion plus Google. Google and HuBERT are also different recognizers. |
| 5 | Each target voice needs 26 hours of decoder training | No row | no quote | Unclear whether 26 h is training data or training time. |
| 6 | "Realtime" is an utterance-level ratio (1/20 GPU, 1/10 CPU) with no latency | No row | no quote | Plausible, but nothing supports it. |
| 7 | Disorder study: five and four speakers, one sentence each, quality ratings | Row 23 | partly | The quote shows the authors claim intelligibility. Speaker counts and the MUSHRA values 20.76 → 20.05 and the WESPER[S4] label have no quote. |
| 8 | Prosody 3.43 vs 3.31, not significant (Fig. 8) | Row 22 | partly | Quote says "almost equal". The numbers and the significance mark have no quote. |
| 9 | Language independence called a possibility, one German sentence | Row 24 | correct | |
| 10 | Encoder pretrained on Librispeech 960 h, LPC whisper copy, wTIMIT 58 h | Rows 5, 21 | correct (Librispeech, 58 h) | LPC copy has no quote. |
| 11 | 100 discrete units, 256-dim every 20 ms | Row 12 | partly | 100 units is quoted. 256-dim and 20 ms are not. |
| 12 | 39 of 60 studies use DTW pairs [3] | Row 4 | wrong citation | [3] supports "existing methods use DTW", not a ledger count of 39/60. |
| 13 | 50 of 60 studies use spectral mapping [5] | Row 11 | wrong citation | Row 11 has no quote. [5] cannot support a ledger count. |
| 14 | AGAN-W2SC baselines (GMM, BLSTM, CycleGAN) train on DTW-aligned pairs | Row 7 | correct | |
| 15 | Niranjan et al. [4] use non-parallel data only for encoder pretraining | Row 8 | insufficient evidence | The quote is cut off at "can be used for". "Only for encoder pretraining" is not shown. |
| 16 | Wagner et al. [5] align pairs by DTW | Row 9 | correct | |
| 17 | No earlier study in the Appendix population trains without pairs | Rows 10, 28 | contradiction | Row 28 lists "unpaired 15" in the same population. Row 10's quote is about raters, not about this claim. |
| 18 | WESPER works on three corpora, with 50 raters per study | Row 10 | partly | 50 participants is quoted. Three corpora is not. |
| 19 | FlowW2N trains on synthetic whisper only, with no real pairs | Rows 2, 6 | correct | |
| 20 | FlowW2N uses "the same toWhisper simulator" as WESPER | No row | no quote | This carries the "built on" lineage claim. |
| 21 | FlowW2N 14.0% vs 26.0% real-pair baseline, 1,404 utterances; fine-tuning on real pairs gives 102% and 79.9% | Row 16 | partly | 1,404 utterances is quoted. 14.0, 26.0, 102 and 79.9 are not. |
| 22 | FlowW2N: SSL-unit converters raise WER above input whisper; HuBERT-Soft 37.5%, raw whisper 8.3% | Rows 13, 14 | partly | The qualitative statement is quoted. Row 14's quote is only "Real Whisper", with no numbers and no recognizer. |
| 23 | "Best converter today loses to raw whisper, 14.0% against 8.3%" | Row 14 | insufficient evidence | The review says FlowW2N uses two recognizers. It is not shown that 14.0 and 8.3 come from the same one. "Best today" rests on a single preprint. |
| 24 | Wagner et al. labelled [concurrent], FlowW2N [later] | Ref list | correct | Wagner arXiv Dec 2022 vs target Mar 2023, about 3 months apart. FlowW2N is 2026. |
| 25 | Wagner et al. venue: ICASSP 2023 | Ref 5 | insufficient evidence | From memory (medium-low confidence) this paper appeared at IEEE SLT 2022. Check before publishing. |

## Central claim and confounds

The strongest attack in the review is the ASR comparison, which leans on 13.75%. It has three confounds:
- The target is inconsistent: its text says 33.06% and Table 2 says 13.75%.
- The comparison crosses recognizers: Google with conversion against HuBERT without.
- Possible leakage: wTIMIT whisper is in pretraining and in the test set.

The review notes the inconsistency and the leakage in the bullets but still states 13.75% as fact in the Verdict. The M02 `ahead` verdict conflicts with the review's own admission that no paired baseline exists and with the Appendix count of 15 unpaired studies. The M06 `standard` verdict is used to mean "untested", but the review's own count says the design is not the usual one.

## Required fixes (ordered by impact)

1. **Sentence:** "while the paper's own Table 2 gives 13.75% for a recognizer trained with whisper and no conversion." (Verdict). Also: "but a recognizer trained with whisper does about twice as well without conversion".
   **What is wrong:** The review reports elsewhere that §5.2 gives this model 33.06%, so the paper contradicts itself. The Verdict builds its strongest position on one of the two values. The claim-table quote (row 18) does not contain 13.75 and gives no column headers. The comparison also crosses recognizers (Google vs HuBERT), and the model was self-supervised-pretrained on wTIMIT whisper, not "trained with whisper" for ASR.
   **Fix:** Quote the full Table 2 row with its headers. In the Verdict, state that text (33.06%) and table (13.75%) disagree and that with the text value conversion wins. Say "pretrained on wTIMIT whisper" and name the recognizer change as a confound. If the 0.34 in row 18 belongs to the wTIMIT-pretrained model on wTIMIT(W), report it as a sign of train/test overlap.

2. **Sentence:** "No earlier study in the Appendix population trains a converter without pairs, and WESPER's converter works on three corpora with 50 raters per study. Verdict: ahead." (M02)
   **What is wrong:** The Appendix (row 28) counts 15 unpaired studies in the same population, which contradicts the sentence. The sentence names no unpaired prior. Cycle-consistent, non-parallel-capable whisper converters existed before 2023 (for example, CycleGAN/DiscoGAN-style whisper-to-normal work around 2019; inference, verify against the ledger). The `ahead` rule also needs the effect repeated, but the review itself says "no paired baseline is trained on the same data". "Three corpora" has no quote.
   **Fix:** Check the 15 unpaired studies by date and name any that precede WESPER. If any exist, or the effect stays unisolated, change the verdict to `different` or `standard` and keep the sentence "shows pairs are unnecessary, not that dropping them is free". Quote or drop "three corpora".

3. **Sentence:** "Verdict: standard, because the representation is never isolated" (M06). Also in the Verdict: "conversion through self-supervised units (M06), which is standard because it is never compared with a spectral or paired baseline."
   **What is wrong:** `standard` means the usual design. The review's own count says 50 of 60 studies use spectral mapping, and that before WESPER only Wagner et al. used SSL features, and only for evaluation. The label misstates the design to express a lack of evidence.
   **Fix:** Use the verdict that means "departs from the usual design, effect not isolated" (for example `different`, or the SKILL.md equivalent). Keep the missing-ablation reason.

4. **Sentence:** "Even the best converter today loses to raw whisper for a modern recognizer, 14.0% against 8.3%." (M06)
   **What is wrong:** Row 14's quote is only "Real Whisper", with no numbers. The review says FlowW2N uses two recognizers, and it is not shown that 14.0 and 8.3 come from the same one and the same test set. "Best converter today" rests on one 2026 preprint.
   **Fix:** Quote the Table 1 cells and name the recognizer for both values. Replace "the best converter today" with "the strongest converter in the ledger (FlowW2N, 2026)".

5. **Sentence:** "since each target voice needs 26 hours of decoder training" (Verdict). Also "26 h decoder training per target voice" (component table, M03).
   **What is wrong:** No quote supports it, and it is unclear whether 26 h is the amount of target-speaker speech or the training time.
   **Fix:** Add the §3 quote and say "26 h of target-voice speech" or "26 h of training", as the paper states.

6. **Sentence:** "also avoids real pairs, training on synthetic whisper from the same toWhisper simulator, and reaches 14.0% WER ... against 26.0% for a baseline trained on real pairs; fine-tuning on real pairs fails (102% WER, 79.9% after DTW)." (M02 state of the art). Also "its HuBERT-Soft comparator scores 37.5%" (M06).
   **What is wrong:** "Same toWhisper simulator", 14.0, 26.0, 102, 79.9 and 37.5 have no quote. The simulator claim carries "Later work built on" in the Verdict.
   **Fix:** Add a claim-table quote with location for each number and for the simulator, or drop what cannot be quoted. Soften "built on" to "also uses" if the simulator lineage is not stated by FlowW2N.

7. **Sentence:** "39 train on time-aligned parallel pairs, usually DTW-aligned (pattern match, Appendix) [3]" (M02). Also "50 of the 60 studies map frame-level spectral features (pattern match, Appendix) [5]" (M06).
   **What is wrong:** A ledger count is cited to a single paper. [3] supports only "existing methods use DTW", and [5] has no quote at all (row 11).
   **Fix:** Cite the Appendix only for the counts. Move [3] to a separate sentence on DTW as the typical alignment.

8. **Sentence:** "Niranjan et al. [4] use non-parallel data only for encoder pretraining." (M02)
   **What is wrong:** Row 8's quote is cut off ("where both parallel and non parallel data can be used for"). It does not show "only" or "encoder pretraining".
   **Fix:** Quote the full sentence from [4] §2, or rephrase to what it says.

9. **Sentence:** "for speaker S2′, MUSHRA falls from 20.76 to 20.05 (Table 3), which also labels the converted S5 row WESPER[S4]." Also: "rests on 3.43 versus 3.31 for whisper, marked not significant (Fig. 8)", "The disorder results rest on five and four speakers, one sentence each", and "decodes a 256-dimensional vector every 20 ms".
   **What is wrong:** None of these numbers or labels appears in a claim-table quote. Rows 22 and 23 quote only qualitative sentences, and row 12 quotes only the 100 units.
   **Fix:** Add a quote and location for each value (Table 3 cells, Fig. 8 values and significance mark, §5.3 speaker counts, §3.1 dimensions), or remove the value.

10. **Sentence:** "| M09 Confirmation | Utterance playback | ... | not reported |" (component table). Also Appendix rows "Slot-filled 31 unique studies" vs "Slot-filled 6,960 unique studies", and "Read in full: [2], [3], [4], [5], target" vs "Read in full: [2], [3], [4], target".
   **What is wrong:** M09 describes a feature in the paper but is marked "not reported". The Appendix gives different slot-filled totals and different read-in-full lists without explaining which component each belongs to.
   **Fix:** Either mark M09 as `standard` or state what is unreported. Label each Appendix block with its component (M02, M06, M12) so the differing totals and lists are visibly per component, and add [5] to the M06 list if it was read.

11. **Sentence:** "*Proc. IEEE ICASSP 2023*, 2023. arXiv:2212.01775." (Reference 5)
    **What is wrong:** From memory (medium-low confidence) this paper was published at IEEE SLT 2022, not ICASSP 2023.
    **Fix:** Verify the venue against the arXiv comments or DOI and correct it.

## Scores

- Procedure: 6/10. Concurrent and later works are labelled correctly, and the target's self-contradiction was found. But many numbers have no quote, two ledger counts carry wrong citations, and two verdict labels do not follow the rules.
- Final text: 6/10. The position is clear and the critique is sharp. The headline ASR attack rests on a disputed table value and a cross-recognizer comparison, and M02/M06 verdicts contradict the review's own evidence.
