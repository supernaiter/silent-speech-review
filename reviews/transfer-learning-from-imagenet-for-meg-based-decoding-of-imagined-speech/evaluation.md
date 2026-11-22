# Independent evaluation: Transfer Learning from ImageNet for MEG-Based Decoding of Imagined Speech

Date: 2026-11-22. Fallback evaluator (claim table only): the claim table, the Verdict and the component sections were checked; no source was re-opened. Ledger counts (rows 27 to 37) are outside this check.

## Claim check

| No | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target fine-tunes ImageNet ResNet-18 and ViT-Tiny, last block, head and 1×1 projection trained | Rows 1, 7 (t17, t15) | correct | t17 supports the partial fine-tuning; model names not in a quote but consistent with Table 3 row label. |
| 2 | [2] used ImageNet-pretrained CNNs on MEG Morlet scalograms of imagined phrases | Row 2 (d1, d2) | correct | Both quotes support it. |
| 3 | Target cites [2] "only for its decoding result" / "only for imagined sentences" | Rows 2, 21 | insufficient evidence | No quote of the target's own citation context for [2]. |
| 4 | [3] used a frozen ImageNet ResNet50 on imagined-speech EEG | Row 2 (p1) | insufficient evidence | p1 supports "frozen ResNet"; "ResNet50" and "ImageNet" are not in the quote. |
| 5 | 21 participants, LOSO testing | Row 3 (t5) | correct | |
| 6 | Removing pretraining costs 5.7 to 8.9 points | Rows 3, 10 (t35, t36, t37) | wrong / insufficient | The numbers the review gives (90.4 to 81.6) yield 8.8, not 8.9. The pretrained baselines (90.4, and any held-out imagery-vs-silence baseline) have no quote; only the RandomInit rows are quoted. 51.7 to 46.0 = 5.7 is correct. |
| 7 | Relative drops 9.7% and 11.0% | Row 10 | correct (arithmetic) | 8.8/90.4 = 9.7%; 5.7/51.7 = 11.0%. Depends on the unquoted 90.4. |
| 8 | Vowels 60.6% pooled, 51.7% held-out; chance 33% | Rows 5, 9, 22 (t28, t21) | correct | Values are the full-window columns of the ResNet-18 row; 51.7 − 33.3 = 18.4 is correct. |
| 9 | Imagery always follows silent reading of the same sentence (Fig. 1) | Rows 5, 19 (t61) | correct | |
| 10 | No EMG in the target | Row 5 (t62) | correct (absence, stated as unstated) | |
| 11 | Silence from inter-trial rest; authors concede engagement / sensorimotor effects | Row 18 (t11, t39) | correct | |
| 12 | [2] state of the art: 93.24% within subject, random split, five imagined phrases | Row 8 (d4, d5) | wrong / insufficient | 93.24% is not in any quote; d4 gives 93.56 ± 1.92% for ST-CNN in the production stage, without saying imagined or spoken. "Random" and "within subject" are not in d5. |
| 13 | [2] mosaic of 196 sensors into one 14×14 image | Row 14 (d3) | correct | |
| 14 | The mosaic "beat per-sensor scalograms in every stage" | Row 14 (d4) | insufficient evidence | d4 reports only ST-CNN accuracies; no comparison with per-sensor scalograms is quoted. |
| 15 | [2] compared pretrained CNNs only with a shallow network on statistical features | Row 11 (d8) | insufficient evidence | d8 shows a shallow ANN baseline; "only" and "statistical features" are not supported. |
| 16 | 248-channel scalograms mixed into three maps by a 1×1 convolution | Row 13 (t15) | insufficient evidence | t15 is about resizing to 224×224×3; the channel count and the 1×1 convolution need t17 and a channel-count quote. |
| 17 | PCA-3 costs 3.9 (imagery vs silence) and 3.5 (vowels); full fine-tuning costs 3.0 | Row 15 (t54, t56, t57) | correct (arithmetic), condition unclear | 90.4 − 86.5 = 3.9 and 90.4 − 87.4 = 3.0 are pooled; 3.5 holds for both pooled (60.6 − 57.1) and held-out (51.7 − 48.2). The text does not state the split. |
| 18 | "Overlapping 95% intervals" | Row 15 | insufficient evidence | Table 4 reports ± values whose meaning is not quoted; nothing shows they are 95% intervals. |
| 19 | 10,000-iteration permutation tests | Row 16 (t22) | correct | |
| 20 | [5] shuffles only the pairing under test; concurrent | Row 17 (z1) | correct | arXiv 2605 is about four months after 2601, so [concurrent] is right, and it is used as state of the art, not as a missed citation. |
| 21 | [4] recorded lip and jaw EMG; micromovements did not discriminate syllables | Row 20 (o2) | insufficient evidence | o2 supports the second half; "lip and jaw EMG" is not quoted. |
| 22 | [2] above chance "before any stimulus" | Row 20 (d6) | insufficient evidence | d6 says "in this stage" without naming the stage. |
| 23 | Abstract claims shared neural representations | Row 22 (t3) | correct | |
| 24 | Seeds unreported, no stated selection data | Row 23 (t43) | plausible absence | t43 and t44 are the same sentence; the absence is a reading of Sec. 2.5. |
| 25 | Syllables 400 ms, epochs 800 ms, so windows overlap | Row 24 (t10, t4) | partly insufficient | t10 gives −300 to 500 ms (800 ms); the 400 ms per syllable is not quoted. t4 is from the Abstract while the bullet cites Sec. 5. |

## Central claim, confounds and fairness

- Strongest confound handled: imagery vs rest and imagery vs reading can reflect task state and order (Fig. 1), with no EMG; the review limits content claims to the vowel task. This is right.
- Confound not handled: the pooled split. The review notes that 800-ms epochs overlap neighbouring 400-ms syllables but does not ask whether overlapping epochs from the same trial or sentence can fall in both training and test in the pooled split, which would inflate the pooled numbers that carry the ablation (90.4, 86.5, 87.4). This needs the target's split description before any statement.
- Absolute vs relative change: both are given for the pretraining ablation; fine once the baseline is quoted.
- State of the art (M03): [2] is a 2020 result on a different task and split; the review says so. No later ImageNet-pretrained MEG imagined-speech work is named; the evaluator cannot confirm none exists.
- Fairness: no later work is treated as prior; [5] is labelled concurrent and not counted as a missed citation. The review attributes the engagement caveat to the authors (Sec. 4), so it does not present it as its own finding.
- Verdicts: all component verdicts are `standard` or `not applicable`, so the `ahead` rules do not apply. M13 is `not applicable` although a usual approach and count are filled in; the M06 table cell repeats the count ("(8) (pattern match 8)").
- Bibliography: entries [2] (Front. Neurosci. 14:290, 2020) and [3] (IEEE Access 9, 135371-135385, 2021) look consistent with what the evaluator knows; the ISBI 2026 venue for [1] and the arXiv id for [5] could not be checked.

## Required fixes (ordered by impact)

1. Pretraining ablation range: the stated numbers give 8.8, not 8.9 points; correct the range or name the condition that gives 8.9, and add a Table 4 quote for the pretrained baselines (90.4 and any held-out baseline used).
2. [2] state of the art: 93.24% is not in the quote (d4 gives 93.56% for ST-CNN, production stage); quote the exact value with its condition (imagined or spoken, stage, network) and support "within subject" and "random split", or correct the figure.
3. "Overlapping 95% intervals": quote what the ± values in Table 4 are, or drop the claim.
4. State the split (pooled or held-out) for each ablation gap (3.9, 3.5, 3.0) in M06 and in "Where the claims outrun the evidence".
5. "Beat per-sensor scalograms in every stage" [2]: add the comparison quote or remove.
6. [4] "lip and jaw EMG": add a quote naming the recording, or say only that micromovements were checked.
7. [2] "above chance before any stimulus": add a quote naming the pre-stimulus stage.
8. "The paper cites [2] only for its decoding result / imagined sentences": add the target's citation context.
9. [2] "compared pretrained CNNs only with a shallow network on statistical features": support "only" and "statistical features" or soften to what d8 says.
10. M06 description: replace t15 with t17 plus a quote giving 248 channels for the 1×1 convolution claim.
11. Add a quote for "400 ms per syllable" and cite the Abstract (t4) or quote Sec. 5 for "imagery-locked".
12. [3] "ResNet50" and "ImageNet": add a quote naming the backbone and its pretraining.
13. Claim table hygiene: rows 6 and 12 carry unrelated target quotes (participant and sentence counts) for ledger tallies; mark them as tally. Row 23 repeats t43/t44.
14. Consider one sentence on possible train/test leakage from overlapping epochs in the pooled split, as a question to the authors, once the split is checked.
15. Table: make M13 consistent (`standard` if a usual approach is given) and remove the duplicated count in the M06 cell.

## Scores

- Procedure: 6/10. Positions are mostly anchored, but several load-bearing numbers (90.4, 93.24, 95% intervals) lack a supporting quote and two claim-table rows carry unrelated quotes.
- Final text: 7/10. Clear position, correct handling of the main task confound and of chronology; the numeric errors and unquoted details above need fixing before publication.
