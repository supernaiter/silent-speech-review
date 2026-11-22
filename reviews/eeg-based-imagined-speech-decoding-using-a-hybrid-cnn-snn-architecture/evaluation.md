# Independent evaluation: EEG-Based Imagined Speech Decoding Using a Hybrid CNN-SNN Architecture (arXiv:2607.03844)

Date: 2026-11-22. Fallback evaluator (claim table only): the review's Verdict, component sections, table and claim table were checked against the claim-table quotes and locations. No source was reopened. Where a judgement relies on general knowledge of the field, it is marked as such.

## Claim checks

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Target changes the decoder: temporal CNN, then two LIF layers, surrogate gradients (Verdict) | Row 1, Sec. III, III-C.2 | correct | The quotes support CNN followed by an LIF classifier. "Two" layers and "surrogate gradients" have no quote in the table. |
| 2 | First-use claim (Abstract; Sec. V) contradicted by a 2024 SNN+CNN inner-speech study [2] (Verdict; Claims list) | Rows 2, 15 | correct | Both quotes are present. The Verdict says the claim "fails against the Appendix count", but what refutes it is [2], not the count. |
| 3 | 80.13% on validation subset is below 82.6% competition winner on test trials; "benchmark claim is wrong" (Verdict) | Rows 3, 10, 11 | insufficient evidence | The numbers match. The quote for 82.6% does not say "test trials". No row quotes the authors saying they "surpass the literature", although M12 puts that phrase in quotation marks. The two accuracies come from different trial sets, so "wrong" is stronger than the evidence (see fix 1). |
| 4 | Ranking of the second-place 75.5% (M12) | Row 10 | correct | Quote matches. |
| 5 | 2.47 points, 3.0% relative below winner (M12) | Row 11 | correct | 82.6 - 80.13 = 2.47 and 2.47/82.6 = 2.99%. |
| 6 | "on easier data" (M12) | none | insufficient evidence | Nothing in the claim table shows that the validation subset is easier than the test trials. |
| 7 | 9.94 points, 14.2% relative over the 70.19% comparator (M12) | Row 12 | correct | 9.94/70.19 = 14.16%. The review correctly notes that Table II gives no comparator protocols. |
| 8 | Validation-as-test precedent, 59.47 ± 6.86 vs EEGNet 58.27 ± 9.62 [5] (M12) | Row 8 | correct | The numbers match. "Model selection inside the training subset" goes beyond the truncated quote ("We applied 5-fold"). |
| 9 | 750 validation trials used as test (M12; Claims) | Rows 9, 17 | correct | Quote matches. |
| 10 | "the 750 validation trials are the only held-out data" (Claims: Selection) | Rows 17, 18 | insufficient evidence | The target labels the test set "Test set (15%)". That label suggests a train/validation/test proportion split, which would mean the authors had a separate validation partition. The review needs to confirm Sec. III-A before claiming that no other held-out data existed. |
| 11 | [2]: 27.66%, four words, 128 channels, 10 participants, chance 25% (M06 SoA) | Row 5 | partly correct | 27.66%, 128 channels and four directions are quoted. "10 participants" has no quote. Chance is marked as inference, which is correct. |
| 12 | Spiking networks have decoded non-speech scalp EEG "since 2021" [4] (M06 SoA) | Row 5 | wrong (general knowledge) | [4] supports SNN decoding of EEG in 2021, but not that it started in 2021. SNN-based EEG modelling and classification goes back at least to the NeuCube architecture (Kasabov, Neural Networks 52, 2014). |
| 13 | 3 prior spiking speech decoders, "all lip reading or audio-visual" (M06 usual approach; Appendix) | Rows 4, 15, 26 | wrong (internal contradiction) | The ledger note says "3 prior speech spiking decoders, 1 EEG inner speech, 2 Siamese". The Claims list also counts [2] as "1 prior spiking EEG speech study". So the 3 cannot all be lip reading or audio-visual. |
| 14 | M06 state of the art is 27.66% [2] (M06 SoA; table row M06) | Rows 5, 30 | wrong (scope) | 27.66% is the nearest spiking prior, not the best result for the task. The Appendix lists 96.4% (four classes, 2018) as the state of the art for imagined-speech EEG word classification, so the component line and the table contradict the Appendix. |
| 15 | Only one run, no seeds; no dense-head control; spike-encoding rule unstated (M06) | Rows 16, 24 | correct (absence) | These are absence claims with section locations. They are acceptable. |
| 16 | Sec. IV credits spike-based dynamics for the gain (Claims: Attribution) | Row 16 | correct | Quote matches. |
| 17 | No chance level, per-subject scores, run variance or F1 averaging rule; chance 20% (Claims: Reporting) | Row 19 | correct | Chance is marked as inference, which is correct. |
| 18 | 98 ± 3 ms per trial on a T4 GPU; low power is only a Table I property (M13; Claims: Efficiency) | Rows 21, 22 | correct | Quotes match. |
| 19 | 112 of 167 offline; authors state offline (M13) | Row 13 | correct | Ledger tally plus the authors' own quote. The review attributes the offline admission to the authors, which is fair. |
| 20 | Online syllable imagery: 20 participants, 55.7% adaptive vs 52.3% static, chance 50% (2024) [6] (M13 SoA) | Row 14 | partly correct | Only 55.7 ± 1.39% is quoted. 52.3%, 20 participants and chance 50% have no quote. |
| 21 | M13 state of the art | Row 14 | insufficient evidence | The component is device and cost. Online accuracy for binary syllables does not set the state of the art for energy or neuromorphic deployment, which is the claim being judged. |
| 22 | Target: 64-channel EEG, 256 Hz, 15 participants, 5 classes (table M05; M06) | Row 6 | partly correct | 15 participants and five words are quoted. 64 channels and 256 Hz have no quote (they agree with the published Track 3 description, from general knowledge). |
| 23 | M03 "Subject-dependent", verdict "not reported" (table) | table | wrong (internal contradiction) | The cell states a training regime, but the verdict says it is not reported. The 750 validation trials pooled across subjects also suggest one pooled model, not per-subject models. |
| 24 | Target dataset naming: the authors write "2020 BCI Competition III dataset" (Row 3 quote) | Row 3 | missed target inconsistency | The authors confuse the 2020 Track 3 data with BCI Competition III. The review silently corrects this instead of noting it. |
| 25 | Chronology: [2] (2024), [3] (2022), [5] (2020), [6] (2024) as prior work for a 2026 target | reference list | correct | No later or concurrent work is treated as prior work. |

Central confound: the main benchmark comparison sets accuracy on the validation subset against competition accuracy on the separate test trials. M06 says a cross-dataset gap "measures the data as much as the design", but M12 treats a cross-split gap as decisive. The review flags the comparator protocols in Table II but not its own winner comparison.

Absence and novelty: the "1 of 29" sentence names its deciding prior [2]. From general knowledge, I know of no earlier hybrid CNN-SNN on imagined-speech EEG, but I cannot rule out earlier NeuCube-style SNN studies on imagined or inner speech EEG (unverified). Every slot verdict is `standard` or not applicable, so the rules for `ahead` do not apply. Calling M06 "standard" when 1 of 167 studies uses spiking may misdescribe how common the design is. Check this against the verdict rules.

## Required fixes (by impact)

1. Recast the benchmark position: 80.13% (validation subset) and 82.6% (test trials) are not measured on the same trials, so the claim is "not shown", not "wrong". Drop "on easier data" or give evidence for it. Add a claim-table row quoting the authors' superiority claim, and confirm that the 82.6% quote refers to test trials.
2. Resolve the contradiction about the 3 prior spiking speech decoders ("all lip reading or audio-visual") against the ledger note (1 EEG inner speech, 2 Siamese) and against [2] being counted as an EEG speech study.
3. Replace the M06 state of the art (27.66%, the nearest spiking prior) with the best result for the task, or label it as the nearest prior. Make the table row and the Appendix (96.4%, 2018) agree.
4. Correct "spiking networks had decoded non-speech scalp EEG since 2021 [4]". SNN EEG decoding predates this, for example NeuCube (2014). Either cite earlier work or drop "since".
5. Check Sec. III-A for a separate validation partition (the "Test set (15%)" label) before stating that the 750 trials were the only held-out data.
6. Fix the M03 row: either state the regime with a quote and give a verdict, or set the cell to "not reported".
7. Add quotes for the unquoted specifics: 10 participants [2]; 52.3%, 20 participants and chance 50% [6]; 64 channels and 256 Hz; two LIF layers; surrogate gradients; model selection inside the training subset [5].
8. Reword "fails against the Appendix count": [2] refutes the claim, and the count only records it.
9. Align the M13 state of the art with the component (energy or neuromorphic measurement on EEG decoding), or say that no measured comparator exists.
10. Note the authors' mislabelling of the 2020 Track 3 data as "BCI Competition III" as a reporting inconsistency.

## Scores

- Procedure: 7/10
- Final text: 6/10
