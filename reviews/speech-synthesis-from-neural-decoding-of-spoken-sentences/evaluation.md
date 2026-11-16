# Independent evaluation: "Speech synthesis from neural decoding of spoken sentences" (Anumanchipalli, Chartier, Chang, Nature 2019)

Date: 2026-11-16. Single pass by a separate evaluator over the compact review only. No claim table or sources were available in this pass. Rows marked "insufficient evidence" could not be checked against a quote and need the writer's claim-table quote before publication.

## Claim table

| # | Claim (review location) | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Abstract says "Intermediate articulatory dynamics enhanced performance even with limited data" (Where the claims outrun, item 1) | Evaluator knowledge of the abstract | correct | The quote matches the published abstract. |
| 2 | Median WER 31% (25-word pool) and 53% (50-word pool) (Where the claims outrun, item 3) | Evaluator knowledge of the paper | correct | Matches the reported listener-transcription medians. |
| 3 | 0.54 dB gain of the articulatory pipeline over the direct decoder (Verdict) | Review only | insufficient evidence | No quote or location is given in the review. Add the figure or panel and the MCD values of both decoders. |
| 4 | Stage-1 target carries 18 place-manner dimensions trained on phoneme labels; the intermediate is the bottleneck of an encoder-decoder fed phoneme labels and MFCCs (Verdict; M06) | Review only | insufficient evidence | Plausible from the Methods, but the review gives no location for "18" or for the inputs of the inversion model. This carries the central confound, so it needs an exact Methods location. |
| 5 | Direct decoder learning rate 0.005 vs 0.001; a 6-layer direct decoder was tried and dropped (M06) | Review only | insufficient evidence | No location is given. Needs a Methods locator. |
| 6 | Mimed n is 38 in the text and 58 in the Fig. 4e caption (Where the claims outrun, item 4) | Review only | insufficient evidence | Internal inconsistencies have to be quoted exactly. The table says "58 mimed trials", so the review uses one of the two numbers without saying why. |
| 7 | "No mimed MCD in the text" (M04) | Evaluator knowledge | insufficient evidence | Fig. 4 reports spectral distortion for mimed vs audible trials. If a mimed value exists in a figure, "cannot be placed on that scale" is too strong. |
| 8 | P3/P4 test sizes 98/82 vs 93/81; 5-fold CV vs single split; direct-decoder gap attributed to Fig. 3a but shown in Fig. 2e (Where the claims outrun, item 5) | Review only | insufficient evidence | Each one needs both locations quoted. Fig. 3a does plot both decoders against training-data amount, so the "misattribution" may be wrong. |
| 9 | Cross-speaker conservation r>0.8 is partly built in by the shared inversion (Where the claims outrun, item 2) | Review | correct (as inference) | Correctly labelled as inference. |
| 10 | Le Godais et al. 2023 found direct decoding "slightly better" (Verdict) vs "at least as good" (M06) | Internal consistency | wrong | The review states the same finding two ways. That study also used linear methods, so it is not a test of the deep pipeline. |
| 11 | Chen et al. 2024: interpretable synthesizer parameters as the intermediate, large cohort (M06 SOTA) | Evaluator knowledge | correct | Nature Machine Intelligence 2024, 48 participants, ECoG. The intermediate is acoustic (pitch, formants, loudness), not articulatory. The review should say so. |
| 12 | Wairagkar et al. 2025: instantaneous voice synthesis from intracortical arrays in ALS (M08, M05, M12, M13 SOTA) | Evaluator knowledge | correct | Correct as a 2025 result. It omits ECoG work from the same lineage (see fix 6). |
| 13 | Martin et al. 2014 decoded spectrograms, overt-to-covert transfer in ECoG (M04, M08) | Evaluator knowledge | correct | |
| 14 | Guenther et al. 2009: formant synthesis (M08) | Evaluator knowledge | correct | Real-time vowel formant synthesis from an intracortical electrode, not sentences. |
| 15 | Gaddy & Klein 2020: silent EMG training with transferred audible targets beats audible-only training (M04 SOTA) | Evaluator knowledge | correct | Gaddy & Klein 2021 (ACL, "An improved model for voicing silent speech") is the stronger later result in the same design. |
| 16 | Komeiji et al. 2024: overt-trained models match covert-trained ones for covert decoding in ECoG (M04 SOTA) | Evaluator knowledge | correct (approximately) | Small cohort. "Match" should be "comparable in N participants". |
| 17 | Janke 2016: EMG silent penalty MCD 5.54 to 6.81 dB (M04) | Review only | insufficient evidence | Needs a page or table locator. |
| 18 | Herff et al. 2019 unit selection, "came between" (M08) | Evaluator knowledge | correct | Labelled [later]. That is correct relative to the bioRxiv preprint. |
| 19 | Angrick et al. 2019 vocoded ECoG log-mel spectrograms with WaveNet, [concurrent] (M08) | Evaluator knowledge | correct | |
| 20 | Chartier et al. 2018 (Neuron) labelled [concurrent] but used as the lab's own prior encoding result (M06) | Chronology | correct | It was online in May 2018, before the November 2018 preprint, and it is the authors' own work, so using it as background is fair. |
| 21 | Ledger counts "confirmed 4: 0 prior, 1 [concurrent], 2 [later]" (M06), and likewise 15/23/29 | Arithmetic | wrong (unclear) | The parts sum to 3, 14, 22 and 28. Each count apparently includes the target paper. Say so, or the counts read as errors. |
| 22 | "Sentence waveforms judged by listeners are the departure" while M08 is rated `standard` (M08) | Verdict rules | wrong | A component the review itself calls a departure, with 2 prior works neither of which did sentence-level waveforms, cannot be `standard` without justification. |
| 23 | M06 is "a rare route" with 0 prior works but is rated `standard` (M06) | Verdict rules | wrong | `standard` conflicts with "usual approach: decode directly". The review needs the verdict label that the rules give to a design that is new but not shown to be better. "Not ahead" is not the same as "standard". |
| 24 | "Its lasting contribution is sentence synthesis from ECoG" (Verdict) | Chronology and fairness | wrong (overclaim) | Angrick et al. 2019 [11] and Herff et al. 2019 [13] synthesized ECoG speech at the same time. The contribution is shared, so it needs qualifying. |
| 25 | "Closed pools without a chance baseline leave this paper's WER uninterpretable" (M12) | Position vs evidence | wrong (too strong) | The WER can be interpreted relative to pool size. It is just not comparable to open-vocabulary WER. Sentence-identification tasks in the same figure have trivially known chance levels. |

## Required fixes (ordered by impact)

1. **Sentence:** "The mechanistic claim does not hold as tested: the intermediate is the bottleneck of an encoder-decoder fed phoneme labels and the participant's own MFCCs, so the 0.54 dB gain over the direct decoder mixes articulation with extra supervision, and a later linear comparison found direct decoding slightly better [5]."
   **What is wrong:** The confound is real, but "does not hold" claims a refutation the evidence does not give. The supervision confound shows the attribution is not isolated, not that it is false. The 0.54 dB value, the encoder-decoder inputs and the "18 place-manner" target have no stated locations. [5] is a linear-method study on different data, so it is not a test of this pipeline.
   **Fix:** "The attribution to articulation is not isolated: the intermediate is trained with phoneme-derived place-manner targets (Methods, <locator>), so the 0.54 dB MCD gain over the direct decoder (Fig. <panel>) confounds articulatory structure with extra supervision; a later linear-method comparison on different recordings found no advantage for the articulatory route [5]." Add the Methods and figure locators.

2. **Sentence:** "### M06 Articulatory intermediate (changed; standard)" (with "a rare route (confirmed 4: 0 prior ...)").
   **What is wrong:** The review states that the usual approach is direct decoding and that this route has no prior instance. A `standard` verdict contradicts that. "Not ahead" means the benefit is not shown. It does not mean the design is usual.
   **Fix:** Apply the verdict label the rules give to a changed component that departs from the usual approach without a shown advantage (not `standard`), and change the table row M06 to match. Otherwise explain in one sentence why `standard` applies.

3. **Sentence:** "Sentence waveforms judged by listeners are the departure (confirmed 15: 2 prior, 1 [concurrent], 11 [later])." with heading "M08 Sentence waveform (changed; standard)".
   **What is wrong:** Same inconsistency. The text calls it a departure, but the verdict and the table say `standard`.
   **Fix:** Either give the non-standard verdict, naming the deciding priors [2], [3] and the concurrent [11], or remove "are the departure" and state why concurrent work makes it standard.

4. **Sentence:** "Its lasting contribution is sentence synthesis from ECoG."
   **What is wrong:** Concurrent ECoG synthesis (Angrick et al. 2019 [11]; Herff et al. 2019 [13]) means this is not the paper's alone. It also conflicts with M08 being rated `standard`.
   **Fix:** "Its lasting contribution is listener-tested sentence synthesis from ECoG, alongside concurrent work [11]."

5. **Sentence:** "Closed pools without a chance baseline leave this paper's WER uninterpretable." (M12), and in the Verdict: "Intelligibility is overstated by closed word pools with no chance level."
   **What is wrong:** This position is stronger than the evidence. A closed-pool WER is interpretable relative to pool size. It is not comparable to open-vocabulary WER, and the paper does not report the chance WER.
   **Fix:** "Closed pools (25 and 50 words) without a reported chance WER make these figures incomparable with open-vocabulary WER." In the Verdict, write "Intelligibility is measured only with closed word pools, without a reported chance WER."

6. **Sentence:** "**State of the art:** Wairagkar et al. 2025 [12] synthesize voice instantaneously from intracortical arrays in a participant with ALS; unit selection [13] and differentiable synthesis [6] came between. This offline result is far behind." (M08)
   **What is wrong:** This omits the later ECoG work most directly comparable to the target. Metzger et al., Nature 2023 ("A high-performance neuroprosthesis for speech decoding and avatar control", doi:10.1038/s41586-023-06443-4) did speech synthesis from ECoG in a participant with paralysis. Littlejohn et al., Nature Neuroscience 2025 ("A streaming brain-to-voice neuroprosthesis to restore naturalistic communication", doi:10.1038/s41593-025-01905-6) did streaming ECoG voice synthesis. No metric or value is given for [12], and "far behind" has no number.
   **Fix:** Add Metzger 2023 and Littlejohn 2025 with their reported metric and value, and give the metric for [12], for example its listener intelligibility. Replace "far behind" with the comparison of metrics, or state it as offline vs real-time without a quantitative claim.

7. **Sentence:** "Le Godais et al. 2023 [5] found direct decoding at least as good." (M06) vs "a later linear comparison found direct decoding slightly better [5]" (Verdict).
   **What is wrong:** The same result is stated two ways. A linear-method comparison is also not "state of the art" for this component.
   **Fix:** Use one wording with the reported metric and value, for example "found no advantage for an articulatory intermediate with linear decoders [5] (metric, value)". Move [5] out of the "State of the art" line into the body text.

8. **Sentence:** "EMG quantifies the penalty (MCD 5.54 to 6.81 dB) [16]; with no mimed MCD in the text, this paper cannot be placed on that scale."
   **What is wrong:** Fig. 4 of the target reports spectral distortion for mimed trials, possibly only in a figure. "Cannot be placed" is then wrong, or at least unchecked. The [16] values also have no locator.
   **Fix:** If Fig. 4 gives a mimed MCD value or a distribution, compare it, noting the different sessions and sentences. If it does not, write "the mimed MCD is shown only graphically (Fig. 4<panel>) without a value". Add the page or table for 5.54 and 6.81 dB in [16].

9. **Sentence:** "Mimed n is 38 in the text, 58 in the Fig. 4e caption; ..." and "P3/P4 test sizes are 98/82 in Methods, 93/81 in captions; ... the direct-decoder gap is attributed to Fig. 3a but shown in Fig. 2e."
   **What is wrong:** Each alleged inconsistency in the target needs both exact locations. Fig. 3a does plot both decoders against training duration, so the "attributed to Fig. 3a but shown in Fig. 2e" point may be wrong. The table uses "58 mimed trials" without saying which number is correct.
   **Fix:** Give the paragraph or section for each number, keep only inconsistencies confirmed against the claim-table quotes, and drop or reword the Fig. 3a/2e item if Fig. 3a shows the comparison.

10. **Sentence:** "a rare route (confirmed 4: 0 prior, 1 [concurrent], 2 [later])", and likewise M08 (15), M04 (23), M12 (29).
    **What is wrong:** The parts sum to one less than the total each time (3, 14, 22, 28). Readers will take these as arithmetic errors.
    **Fix:** Add "including this paper" to each count, or list the target as a part.

11. **Sentence:** "**State of the art:** Chen et al. 2024 [6] use interpretable synthesizer parameters from a speech auto-encoder as the intermediate, across a large cohort;"
    **What is wrong:** The intermediate in [6] is acoustic (pitch, formants, loudness), not articulatory. The cohort size and the metric and value are missing.
    **Fix:** "Chen et al. 2024 [6] use acoustic synthesizer parameters (not articulation) as the intermediate across 48 participants (metric, value)."

12. **Sentence:** Reference 16: "Dissertation defended 2016-04-22; the wiki folder is named after the related journal article (Janke and Diener, IEEE/ACM TASLP 2017, doi:10.1109/TASLP.2017.2738568)."
    **What is wrong:** This is a process note about the wiki. It is not bibliographic content.
    **Fix:** Delete "the wiki folder is named after the related journal article". If the journal article is cited, keep it as a separate reference.

13. **Sentence:** Reference 24: "Gonzalez, J. A., Cheah, L. A., Gomez, A. M., others" and references 23 and 25 without volume or pages.
    **What is wrong:** The bibliographic entries are incomplete or malformed.
    **Fix:** Reference 24: "Gonzalez, J. A., Cheah, L. A., Gomez, A. M., Green, P. D., Gilbert, J. M., Ell, S. R., et al." Reference 23: add *Computer Speech & Language* 36, 274–293. Reference 25: add *PLoS ONE* 11(3), e0151327.

## Scores

- Procedure: 6/10. The components are compared against the field with chronology labels, and the central confound is identified. Several load-bearing numbers have no locators, and the verdict labels contradict the text in two components.
- Final text: 6/10. The position is clear and concise. The headline position overstates the refutation, the state of the art for ECoG synthesis is incomplete, and the M12 judgment is too strong.

The strongest point is identifying the extra supervision (phoneme-derived targets) as the confound behind the articulatory-pipeline gain. The review handles it better than one more participant or one more seed would.
