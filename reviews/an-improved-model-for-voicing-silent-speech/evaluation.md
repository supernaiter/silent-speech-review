# Evaluation: An Improved Model for Voicing Silent Speech (Gaddy and Klein, ACL-IJCNLP 2021)

Date: 2026-11-18. Independent evaluator, single pass, no source access: the review text and its claim table only, plus the evaluator's own background knowledge. The claim table was filled by the writer, not by a separate checker, so a quote that is cut off or missing counts as insufficient evidence, not as support.

## Claim check

| # | Claim | Where checked | Result | Note |
|---|---|---|---|---|
| 1 | Baseline 68.0% to 42.2% WER, an absolute gain of 25.8 points | Claim rows 4, 21 (Table 1; §1 quote "absolute improvement in error rate of 25.8%") | correct | 68.0 - 42.2 = 25.8. |
| 2 | Ablations: phoneme loss removed 51.7, hand-designed features 45.2, LSTM 46.0 | Rows 5, 10, 15, 21 | correct | The quotes give each value. |
| 3 | The ablations account for 16.3 of the 25.8 points | Rows 4, 21 | correct | 9.5 + 3.0 + 3.8 = 16.3. The ablations are run one at a time against the full model, so adding them up assumes the effects add (not stated). |
| 4 | Relative effects of "7%", "9%" and "18%" | Rows 10, 15 | wrong | The bases are mixed. 3.0/45.2 = 6.6%, 3.8/46.0 = 8.3% and 9.5/51.7 = 18.4% use the ablated model as the base. Against 42.2 they are 7.1%, 9.0% and 22.5%. The "9%" uses one base and the "18%" the other. |
| 5 | Human WERs of 36.1% and 28.5%, mean 32.3%, 40 samples, two listeners | Rows 17, 20, 23 | correct | (36.1 + 28.5)/2 = 32.3. The difference is 7.6. |
| 6 | Alignment changes and batching regularizer are not ablated (§2.3) | Row 21 | correct | The quotes are given in the "outrun" bullet. Table 1 has no matching row. |
| 7 | Code overwrites the checkpoint each epoch and evaluates the last one (transduction_model.py) | No claim-table row | insufficient evidence | No quote, file version or line numbers. Tuning hyperparameters on validation WER and evaluating the last checkpoint do not contradict each other. |
| 8 | Test items are drawn by sentence across all sessions (read_emg.py) | Row 24 | insufficient evidence | The quote supports only the session embedding. Nothing quoted shows how the split was built. The split comes from [2] and is reused here. |
| 9 | Prior EMG decoders used DNNs and LSTMs on TD features [5]; 2020 used a 3-layer, 1024-dimension BLSTM [2] | Row 6 | insufficient evidence (LSTM part) | The quotes from [5] cover DNN and MCD only, with nothing on LSTMs. The [2] architecture matches the evaluator's recollection. |
| 10 | Counts for M06: 83 studies, 18 TD, 18 LSTM/GRU, 26 Transformer/Conformer | Row 7 (ledger) | not checked (ledger) | Internal problem: by these counts Transformer/Conformer is the most common design, yet the usual approach given is TD features with DNN or LSTM. |
| 11 | GETS (2026): 11.89% Whisper, 21.32% DeepSpeech | Rows 8, 18 | correct | Both values are in the quotes. |
| 12 | GETS encoder is initialized "from this model" | Row 2 | insufficient evidence | The quote says "pre-trained weights from [4]". Nothing quoted shows that GETS's [4] is the 2021 paper and not the 2020 one. |
| 13 | The same model scores 25.74% under Whisper [3] | Rows 5, 19 | insufficient evidence | The row is labelled "Gaddy and Klein [4]", with the same question of which paper it is. It is also a rerun by other authors. [6] reports 26.75 ± 0.99 for "Gaddy's [3]". |
| 14 | The GETS gap comes from use-time text guidance, not from a new encoder | Row 9 | wrong (overreach) | The quotes show that guidance exists (MONA-LISA at 8.93%, GPT-4 refinement). They do not show that the encoder contributes nothing. That would need an ablation the review does not cite. |
| 15 | Ten-seed SD of 0.99 [6] | Rows 11, 14 | correct as quoted | 26.75 ± 0.99 (Whisper). It is unclear whether the ± is SD or another spread measure. The quote does not say. |
| 16 | The 3.0-point convolution effect is "about three SDs" | Row 22 | wrong (mismatched scales) | The SD is Whisper WER around 26.8%. The effect is DeepSpeech WER around 42-45%. The two cannot be divided without stating that assumption. |
| 17 | Alignment-loss SOTA: 25.14 ± 0.90 against 26.75 ± 0.99, 10 seeds, 98 utterances [6] | Row 14 | correct | The quote shows both values. "98 test utterances" is not in the quoted text but has a cited location (Sec. 4.1). |
| 18 | Tóth et al. [4]: phone-state multi-task, about half an hour from one speaker, about 7% relative gain, no listening test | Row 13 | partly insufficient | The phone-state targets and the half hour are quoted. The "about 7% relative" figure and "no listening test" have no quote. |
| 19 | The target credits the ultrasound prior (§1) | Row 3 | correct | "This auxiliary loss follows prior work on related tasks of generating speech from ultrasound." |
| 20 | M12 usual approach: Whisper in 9 of 16 studies | Row 16 | not checked (ledger) | Fairness issue: Whisper was released in September 2022, after the target. |
| 21 | Recognizer shift of 16.5 points | Row 19 | correct arithmetic, confounded | 42.2 - 25.74 = 16.46. The recognizer is confounded with a different training run and possibly a different checkpoint (see 13). |

Strongest confound: the comparison between DeepSpeech and Whisper (Verdict and M12). The review treats 42.2% (the authors' run, DeepSpeech) and 25.74% (another group's rerun, Whisper) as "the same model", so the whole 16.5 points goes to the recognizer. Run-to-run and checkpoint differences, and possibly which Gaddy-Klein model was run, are not separated out. The review partly handles the attribution confound in Table 1 (unablated changes) but not this one.

State of the art: GETS and the alignment loss [6] are plausible as the best later work on the Gaddy corpus. The evaluator cannot confirm whether other 2023-2026 EMG-to-speech work on this corpus scores lower (for example self-supervised-unit or diffusion vocoder approaches). The writer should confirm that no lower Whisper WER on the same split has been reported.

Novelty and absence: the review makes no "first / only" claims. The verdicts are all `standard` or `not applicable`, so the rules for `ahead` do not apply. The stated reasons for `standard`, however, are inconsistent with the usual approaches stated (fix 5).

## Required fixes (ordered by impact)

1. **Sentence:** "Model selection: tuning used validation WER (Appendix D), but the code overwrites the checkpoint each epoch and evaluates the last (transduction_model.py)."
   **Problem:** The claim table has no row, quote, line range or code version for it. Tuning hyperparameters on validation WER and reporting the last-epoch checkpoint do not contradict each other, so the "but" suggests a discrepancy that is not shown.
   **Fix:** Add a claim-table row with the exact code lines and commit. Reword to the plain fact: "The reported model is the last-epoch checkpoint (transduction_model.py:Lx-Ly); validation WER guided hyperparameter choice only (Appendix D)." If it cannot be quoted, drop the bullet.

2. **Sentence:** "Hand-designed features cost 3.0 points (45.2%, 7% relative) and the LSTM 3.8 (46.0%, 9%), one run each (inference)." together with "The phoneme loss is worth 9.5 points, an 18% relative reduction from 51.7% (inference)".
   **Problem:** The relative changes use different bases. 3.8/46.0 = 8.3%, not 9%. The 9% is against 42.2, while the 18% is against 51.7.
   **Fix:** Use one base throughout. Against the ablated model: 7%, 8%, 18%. Against 42.2: 7%, 9%, 23%. State the base once. If the ablated-model base is kept, the comparison with the ultrasound prior's "about 7%" stays like-for-like.

3. **Sentence:** "The same model scores 25.74% under Whisper [3], a recognizer shift larger than any ablation effect (inference)." (also in M12: "The same model is 42.2% under DeepSpeech and 25.74% under Whisper [3]: the recognizer moves the score 16.5 points")
   **Problem:** The quote labels the row "Gaddy and Klein [4]" and does not show that it is the 2021 model. It is also another group's rerun ([6] gives 26.75 ± 0.99 for the same baseline), so the recognizer is confounded with a different run.
   **Fix:** Confirm from GETS's reference list that its [4] is the 2021 paper and add that to the claim table. Reword to: "A later rerun of this model scores 25.74% under Whisper [3] (26.75 ± 0.99 over 10 seeds in [6]), against 42.2% under DeepSpeech here; recognizer and run differences together move the score about 16 points."

4. **Sentence:** "Against the later 0.99-point seed SD [6], the 3.0-point convolution effect is about three SDs (inference)."
   **Problem:** The SD is measured under Whisper at about 27% WER. The effect is under DeepSpeech at about 42-45% WER, so the ratio assumes the variance carries over across recognizer and error scale.
   **Fix:** "The only seed spread available, 0.99 points under Whisper at about 27% WER [6], is a different metric scale from the DeepSpeech ablations; it suggests but does not establish that the 3.0-point effect exceeds run noise." Make the same change in "Ten-seed reruns of this model vary by 0.99 points SD [6], so the effects are plausible but unrepeated."

5. **Sentence:** "M06 is standard because every comparison is a single run, yet it is the design that lasted" and the table row "Hand-crafted TD features with DNN or LSTM (pattern match 83)".
   **Problem:** (a) The stated usual approach contradicts the review's own counts: 26 Transformer/Conformer studies against 18 TD and 18 LSTM/GRU. (b) "Standard because single run" mixes up how common the design is with how strong the evidence is. By the review's own account the paper departs from the usual approach of its time. It falls short of `ahead` only because the effect was never repeated.
   **Fix:** State the usual approach as it was before 2021 and note that the 26 Transformer studies are mostly later, for example: "Before 2021, TD features with DNN or LSTM; most of the 26 Transformer/Conformer studies follow this paper." Then write: "Verdict: standard (not ahead: single run, no matched capacity)." Make the matching change for M02, where the usual approach is "acoustic targets alone" but the verdict is "standard" because a prior design exists. Say so in exactly those terms.

6. **Sentence:** "Of 16 unique studies on Gaddy silent-EMG voicing (pattern match, Appendix), 9 score with Whisper, 7 with DeepSpeech and 3 with listeners." and the table row "Whisper ASR WER (9)".
   **Problem:** Whisper was released in September 2022, after the target. Presenting it as the usual approach to evaluation implies that the authors departed from a practice they could not have followed. The three categories also add to 19 against 16 studies, and the overlap is not explained.
   **Fix:** "At the time, DeepSpeech WER (as here); later work moved to Whisper (9 of 16 studies, some reporting both)." In the table, give DeepSpeech as the usual approach for the paper's time and Whisper as later practice.

7. **Sentence:** "The gap comes from use-time text guidance (a recognizer at 8.93% WER refined by GPT-4, Sec. 3), not from a new encoder (inference)."
   **Problem:** The quotes show that GETS uses text guidance. They do not show that the encoder contributes nothing. "Not from a new encoder" is stronger than the evidence.
   **Fix:** "GETS keeps a convolution-plus-Transformer encoder initialized from this model and adds use-time text guidance (a recognizer at 8.93% WER refined by GPT-4, Sec. 3); the gain is most plausibly from the guidance, though GETS does not report an ablation that isolates it."

8. **Sentence:** "The prior design [4] trained an ultrasound-to-vocoder network jointly on forced-aligned phone states, half an hour from one speaker reading aloud, for about 7% relative gain with no listening test."
   **Problem:** The claim table quotes the phone-state targets and the half hour of data, but nothing supports "about 7% relative gain" or "no listening test". This 7% is then compared directly with the target's 18%.
   **Fix:** Add the quote and location in [4] (table and metric, for example the correlation or MCD values before and after) and the computation to the claim table. Otherwise remove the 7% figure and the comparison in M02.

9. **Sentence:** "Split: despite session embeddings (§2.1), test items are drawn by sentence across all sessions (read_emg.py); no held-out-session result exists."
   **Problem:** Row 24 quotes only the session embedding and nothing on how the split was built. The split was also defined in [2] and reused, so it is not a choice this paper made.
   **Fix:** Quote the split code (file, lines, commit) or the split description in [2], and reword: "The test split, inherited from [2], samples sentences across all sessions (read_emg.py:177-205); no held-out-session result is reported, so the session embeddings are not tested on unseen sessions."

10. **Sentence:** "Earlier surface-EMG decoders fed hand-crafted time-domain (TD) features to feed-forward or recurrent networks: DNNs and LSTMs in Janke's EMG-to-speech work [5]"
    **Problem:** The quotes from [5] in the claim table cover DNN and MCD results only. Nothing supports LSTMs.
    **Fix:** Add a quote and location showing LSTM use in [5], or reduce it to "DNNs in Janke's EMG-to-speech work [5]".

11. **Sentences:** "Hand-designed features cost 3.0 points ... (inference)", "The listeners score 36.1% and 28.5%, 7.6 points apart (inference)", "the three ablation effects sum to 16.3 of the 25.8 points (inference)".
    **Problem:** These are exact arithmetic on quoted numbers, not inference. Labelling them "(inference)" hedges statements the evidence supports outright. The label should be kept for real interpretive steps, such as the additivity of ablation effects.
    **Fix:** Drop "(inference)" from the plain differences and sums. Where it fits, add "assuming the effects are additive" to the attribution sentence.

12. **Sentences:** "(pattern match, Appendix)" in the M06, M02 and M12 sections, and claim rows 26-37 ("Questions for the authors", "Appendix: literature search").
    **Problem:** The review text cites an Appendix and a Questions section that do not appear in the text evaluated, so the ledger counts and the questions cannot be traced from the published review.
    **Fix:** Include the Appendix (ledger counts, papers read in full, known-item recall) and the Questions section in the review. Otherwise remove the "Appendix" pointers and the corresponding claim rows.

## Scores

- Procedure: 6/10. Arithmetic on the target is accurate and later work is labelled. Two load-bearing claims (model selection, split construction) have no supporting quote. The comparator identity in the two 2026 papers is never confirmed, and the confound between recognizer and rerun is not separated.
- Final text: 6/10. The position is clear and mostly tied to locations. Mixed relative-change bases, a cross-scale SD comparison, a usual approach for M06 that contradicts its own counts, and a later recognizer presented as usual practice all need correcting.

Brief note on strengths: the attribution gap (16.3 of 25.8 points explained, two changes not ablated) is well grounded and is the review's most useful finding.
