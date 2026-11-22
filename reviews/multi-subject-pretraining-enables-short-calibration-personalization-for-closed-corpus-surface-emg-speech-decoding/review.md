# Multi-Subject Pretraining Enables Short-Calibration Personalization for Closed-Corpus Surface EMG Speech Decoding

Le, C., Fumagalli, B., Esmaeili, Y., Chen, X., He, T., Emami, N., Flinker, A., Wang, Y. · arXiv preprint · 2026 · [arXiv:2609.21288](https://arxiv.org/abs/2609.21288)

## Verdict

The paper [[1]](#ref-1) changes training (M03): pretraining on the other members of a 27-person cohort, then calibrating on the held-out one. The design is standard: sEMG decoders have been pretrained on other speakers and adapted to a new one since 2008 [[2]](#ref-2), [[3]](#ref-3), [[4]](#ref-4); cohort size and a 1-to-26 pool sweep combined with minute-level calibration budgets are what it adds. The strongest confound is the closed corpus: other participants' repetitions of the five test sentences stay in pretraining (§3.2), and once those sentences leave all training, CER rises from 21.7% to 78.6% and WER from 31.9% to 99.9% (Table 3). The 3-minute result thus measures how fast a model recognizes sentences already seen from other people. The evaluation (M12) is behind the best comparable work, which reports silent-EMG error on sentences absent from training [[5]](#ref-5), [[6]](#ref-6).

## Against the field, component by component

### M03 Training: multi-subject pretraining and calibration budget

**Usual approach:** Across all signal types, the most common design is a per-participant model (90 of 379 unique studies, pattern match with full-text-only hits, Appendix). Among 76 sEMG studies on cross-speaker training (64 pattern match plus full-text-only hits, Appendix), 40 test a pooled model on a held-out speaker, 13 adapt to the target speaker and 13 vary the amount of adaptation data; the target adds minute-level calibration budgets combined with a pool-size sweep from 1 to 26 participants.

**State of the art:** In 2024, cross-speaker sEMG-to-speech pretraining fine-tuned on one session of a leave-out speaker beat training from scratch (p < 0.01) with four speakers [[4]](#ref-4), [[7]](#ref-7); the target tests 27 participants.

An HMM recognizer trained on all speakers but the test speaker and adapted with MLLR beat the zero-shot system, with no gain beyond 120 words of target data [[2]](#ref-2). A model trained on 28 subjects was fine-tuned on 4 new ones with 1 to 8 sessions over 100 fixed phrases [[3]](#ref-3). A 2023 study by Zhang and colleagues, cited by the target, found that more training speakers raised cross-speaker phrase accuracy, as summarized in [[7]](#ref-7); the pool-size sweep extends that trend to 26 participants. The authors disclaim the paradigm (§1); the claim rests on scale.

The gain over zero-shot transfer is large: 49.3% to 21.7% CER, 27.6 points or 56% relative (inference). The gain over direct checkpoint fine-tuning (68.0% CER) does not isolate pretraining: that control used about 282 target trials, not 263, kept evaluation-sentence repetitions, and starts from a checkpoint with a different montage (§3.2, §5.6). The pool-size curve (74.4% to 21.7% CER, 1 to 26 participants) had not flattened; only 16 of 27 improved at every step (§4.4). Verdict: standard.

### M12 Evaluation: closed corpus versus unseen sentences

**Usual approach:** Of 64 sEMG studies scored with WER or CER (pattern match), 13 name a sentence-disjoint or open-vocabulary test and 9 a closed or repeated sentence set (Appendix); the target's headline sits on the closed side.

**State of the art:** On open-vocabulary silent EMG, WER reached 12.2% for one speaker in 2024 [[6]](#ref-6); the target's backbone lineage reported 42.2% in 2021 [[5]](#ref-5). The target's unseen-sentence WER is 99.9% (Table 3).

Starting points differ: hours of one speaker against 21.3 minutes per participant plus an 18.7-hour checkpoint (Abstract, §3.4). The closed-set number does not show open decoding: a nearest-template baseline on EMG envelopes already reaches 60.3% CER, so sentence identity is partly recoverable without a decoder (Table 4), and the authors concede the result does not establish compositional decoding (§4.6). Verdict: behind (best comparable work).

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Aloud and mimed sentences | Recorded articulation (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | Character transcripts (CTC) | Text or paired-audio targets (slot-filled 31) | – | standard |
| M03 Training and adaptation | Pretrain on 26, calibrate 1-13 min | Held-out-speaker test of pooled model (pattern match 40) | Leave-out-speaker adaptation beats scratch, 4 speakers [[4]](#ref-4) (2024) | standard |
| M04 Use-time action | Aloud and mimed | Silent or overt (slot-filled 5,595) | – | standard |
| M05 Sensors | 8-channel face and neck sEMG | Sensor montage (slot-filled 7,329) | – | standard |
| M06 Processing and decoding | Conv-transformer, CTC, checkpoint | Encoder plus CTC (slot-filled 7,345) | – | standard |
| M07 Lexicon and LM | External KenLM, beam 100 | Lexicon or LM (slot-filled 119) | – | standard |
| M08 Output | Character text | Text or waveform (slot-filled 3,268) | – | standard |
| M09 Confirmation | Offline | Offline (slot-filled 82) | – | not applicable |
| M10 Correction | Offline | Offline (slot-filled 82) | – | not applicable |
| M11 Reference construction | 50 TIMIT sentences, 45/5 split | Corpus references (slot-filled 234) | – | not reported |
| M12 Evaluation | Closed corpus; unseen test 99.9% WER | Sentence-disjoint test (pattern match 13) | 12.2% WER open vocabulary, one speaker [[6]](#ref-6) (2024) | behind |
| M13 Device and cost | Laboratory, healthy adults | Laboratory study (slot-filled 6,075) | – | standard |

## Where the claims outrun the evidence

- No calibration budget is tested on unseen sentences, where full calibration still gives 78.6% CER (Table 3, §3.5).
- Three minutes is not significantly different from full calibration (p = 0.27, CER), which the authors call no equivalence result (§4.2). Ten minutes beats full calibration (18.6% CER, p = 0.030); the authors tie this to equal epochs giving unequal update counts (§4.2, Table 2 note). Calibration-trial shuffling and pool sampling each use one fixed seed, with no value given and no repeated-seed runs (§3.5).
- The checkpoint-versus-random gap of 23.2 points includes 5 of 27 non-converged folds; on converged folds it is 9.7 points (§4.1).
- The subject-specific adapter gives no detectable gain (-0.8 points), tested only with 26 in pretraining (§4.3).

## What the field needs next

- M12: a sentence-disjoint split with many sentence types, with the calibration sweep on unseen sentences.
- M03: calibration budgets at matched update counts with repeated seeds, and the pool-size curve beyond 26 participants to locate saturation.
- M05: calibration and test across electrode re-donning, which was not tested (§5.6).

## Questions for the authors

- How were the five evaluation sentences chosen, and does their selection depend on any test result?
- What seed values were used, and how much do the calibration and pool-size curves move across seeds?
- How are text normalization, case and punctuation handled for CER and WER?
- How many sessions did each participant give, and were calibration and test trials from the same session?

## Appendix: literature search

- M03, emg-cross-speaker-training-and-calibration. Inclusion rule: surface-EMG speech decoders that train on several speakers and test on a speaker held out of that pool, with or without target calibration; per-speaker models averaged over speakers, speaker-mixed random splits and session-only adaptation are excluded; reviews count as pattern matches only; versions count once. Ledger: 1,526 unique studies slot-filled for M03; 64 unique studies pattern match (74 folders), 13 full-text-only folders; 76 unique studies with text. Designs (pattern match): held-out-speaker test 40, per-speaker models only 21, target-speaker adaptation 13, adaptation-data amount sweep 13, training-pool-size sweep 1 (the target; full-text pattern). Read in full: [[2]](#ref-2), [[3]](#ref-3), [[7]](#ref-7). Known-item recall 1.0 (3 of 3 seeds).
- M03, cross-subject-pooled-training (published table, reused). Inclusion rule: speech or language decoders from neural or other biosignals that train one model on data pooled across participants, with or without participant-specific layers; per-participant models averaged over participants are excluded; transfer by fine-tuning from other participants counts; versions count once. Ledger: 1,526 unique studies slot-filled for M03; 370 unique studies pattern match, 379 with full-text-only hits. Usual design: per-participant model, 90 of 379 (pattern match), the most common design. Known-item recall 1.0.
- M12, emg-text-unseen-sentence-test. Inclusion rule: surface-EMG decoders scored with WER or CER; the design compared is whether the headline error is measured on sentences absent from all training or on repeats of training sentences; each protocol a paper names is counted; reviews count as pattern matches only; versions count once. Ledger: 6,960 unique studies slot-filled for M12; 64 unique studies pattern match (79 folders). Designs (pattern match): held-out speaker 21, sentence-disjoint or open vocabulary 13, closed or repeated sentences 9. Read in full: [[6]](#ref-6), [[5]](#ref-5). Known-item recall 1.0 (3 of 3 seeds).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Le, C., Fumagalli, B., Esmaeili, Y., Chen, X., He, T., Emami, N., et al. “Multi-Subject Pretraining Enables Short-Calibration Personalization for Closed-Corpus Surface EMG Speech Decoding.” *arXiv preprint*, 2026. doi:[10.48550/arXiv.2609.21288](https://doi.org/10.48550/arXiv.2609.21288). arXiv:[2609.21288](https://arxiv.org/abs/2609.21288). Target. Read as arXiv v1. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/multi-subject-pretraining-enables-short-calibration-personalization-for-closed-corpus-surface-emg-speech-decoding) [wiki: arxiv-2609.21288](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2609.21288/article.md)
2. <a id="ref-2"></a>Wand, M., Schultz, T. “Towards Speaker-Adaptive Speech Recognition Based on Surface Electromyography.” *Proc. BIOSIGNALS 2008*, 2008. doi:[10.5220/0001549601550162](https://doi.org/10.5220/0001549601550162). Prior; deciding prior for M03. [wiki: doi-10.5220-0001549601550162](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.5220-0001549601550162/article.md)
3. <a id="ref-3"></a>Wu, J., Zhang, Y., Xie, L., Yan, Y., Zhang, X., Liu, S., et al. “A novel silent speech recognition approach based on parallel inception convolutional neural network and Mel frequency spectral coefficient.” *Frontiers in Neurorobotics*, 2022, 16, 971446. doi:[10.3389/fnbot.2022.971446](https://doi.org/10.3389/fnbot.2022.971446). Prior; deciding prior for M03. [wiki: doi-10.3389-fnbot.2022.971446](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnbot.2022.971446/article.md) [wiki: pmc-9478652-picnn-semg](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-9478652-picnn-semg/article.md)
4. <a id="ref-4"></a>Scheck, K., Ren, Z., Dombeck, T., Sonnert, J., van Gogh, S., Hou, Q., et al. “Cross-Speaker Training and Adaptation for Electromyography-to-Speech Conversion.” *Proc. 46th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)*, 2024. doi:[10.1109/EMBC53108.2024.10781707](https://doi.org/10.1109/EMBC53108.2024.10781707). Prior; state of the art for M03; read as the reprint in the 2026 dissertation (Sec. IV-B).
5. <a id="ref-5"></a>Gaddy, D., Klein, D. “An Improved Model for Voicing Silent Speech.” *Proc. ACL-IJCNLP 2021 (Short Papers)*, 2021, 175–181. doi:[10.18653/v1/2021.acl-short.23](https://doi.org/10.18653/v1/2021.acl-short.23). arXiv:[2106.01933](https://arxiv.org/abs/2106.01933). Prior; deciding prior for M12; backbone lineage. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/an-improved-model-for-voicing-silent-speech) [wiki: doi-10.18653-v1-2021.acl-short.23](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.18653-v1-2021.acl-short.23/article.md) [wiki: arxiv-2106.01933](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2106.01933/article.md)
6. <a id="ref-6"></a>Benster, T., Wilson, G., Elisha, R., Willett, F. R., Druckmann, S. “A Cross-Modal Approach to Silent Speech with LLM-Enhanced Recognition.” *arXiv preprint*, 2024. doi:[10.48550/arXiv.2403.05583](https://doi.org/10.48550/arXiv.2403.05583). arXiv:[2403.05583](https://arxiv.org/abs/2403.05583). Prior; state of the art for M12. [wiki: arxiv-2403.05583](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2403.05583/article.md)
7. <a id="ref-7"></a>Scheck, K. “Personalizing Myoelectric Silent Speech Interfaces via Cross-Speaker Training and Voice Timbre Control.” *University of Bremen (dissertation)*, 2026. doi:[10.26092/elib/5498](https://doi.org/10.26092/elib/5498). Prior; dissertation (defended 2026-01) reprinting Scheck et al. 2024 (EMBC), read there; summarizes Zhang et al. 2023 on training-speaker count. [wiki: doi-10.26092-elib.5498](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.26092-elib.5498/article.md)
