# Modeling Coarticulation in EMG-based Continuous Speech Recognition

Schultz, Wand. Speech Communication 52(4), 2010. [doi:10.1016/j.specom.2009.12.002](https://doi.org/10.1016/j.specom.2009.12.002)

## Verdict

The paper [[1]](#ref-1) changes the EMG acoustic model (M06): nine phonetic-feature streams whose models are bundled by decision trees, beside a phone stream. The design is ahead: none of the 12 prior non-acoustic-signal recognizers bundles features (Appendix), the group's feature streams [[2]](#ref-2) and clustered triphones [[3]](#ref-3) were separate, and the gain holds over 28 sessions of 14 speakers and under pooled training. Its size is an upper bound, because stream weights and tree size were tuned on the test set (§3.3). The "speaker-independent" result (M03) tests the speakers it trained on (§4), weaker than the group's earlier held-out-speaker design on the same corpus [[3]](#ref-3). Usefulness for silent speech rests on audible scores only; the group's [concurrent] silent test with the same features gave above 80% WER for most speakers [[4]](#ref-4).

## Against the field, component by component

### M06 Processing: phonetic-feature streams and their bundling

**Usual approach:** At the target's time, 8 of 12 prior non-acoustic-signal recognizers (pattern match, unique studies; Appendix) use phone or word HMM units with no feature stream, 4 name feature streams and none bundles them. In EMG the group had tried the ingredients separately: articulatory-feature streams (a subset of 29 classifiers, chosen on development data) beside a context-independent phone HMM, 33.9% to 29.9% WER on one speaker [[2]](#ref-2), and tree-clustered triphones in a speaker-independent recognizer, 68.92% to 60.97% WER [[3]](#ref-3); clustered sub-word units go back to [[5]](#ref-5), while [[6]](#ref-6) used context-independent phones. The target clusters the feature models themselves.

**State of the art:** In 2024 [later], 12.2% WER on open-vocabulary silent EMG, one speaker, LLM-enhanced decoding [[7]](#ref-7), against the target's 31.49% on audible EMG with 101 test words. Mode, vocabulary and decoder differ, so the gap measures the field's progress, not bundling.

A full-text search for feature bundling over the whole wiki returns only the target, papers and surveys citing it, and the [concurrent] speaking-mode study that uses it and names the target as its source [[4]](#ref-4) (Appendix). The ablation favours bundling over context alone: context without bundling 41.99% WER, bundling without context 35.78%, both 31.49% (Table 3); under pooled training a context-dependent phone stream moves 45.24% only to 44.95%, not significant (Table 4). Two confounds remain: the model grows from 290 to 2,489 Gaussians (Table 2) with no context-dependent phone control in the speaker-dependent tables, and the phone stream keeps weight 0.01 (§3.3). Verdict: ahead, by the zero count among 12 prior studies (Appendix), four read priors without the design [[6]](#ref-6), [[5]](#ref-5), [[2]](#ref-2), [[3]](#ref-3), and repetition over 14 speakers and two training regimes.

### M03 Training: pooled multi-speaker models

**Usual approach:** Per-speaker models. The only confirmed prior surface-EMG study with a held-out speaker in the published table is the group's own on the same corpus, with MLLR adaptation [[3]](#ref-3) (Appendix). The target pools the 14 pilot speakers and tests each of them (§4).

**State of the art:** In 2024 [later], one-session adaptation of a cross-speaker sEMG model to a left-out speaker beats training from scratch [[8]](#ref-8). The target has no held-out speaker.

The "about 28%" reduction claimed for the speaker-independent system (§5) is pooled (62.15% to 44.95% WER, Table 4). Verdict: standard; one confirmed prior does not meet the three-paper rule for behind.

### M12 Evaluation: selection on the test set

**Usual approach:** Three of four read priors choose settings from test results with no development set [[6]](#ref-6), [[5]](#ref-5), [[3]](#ref-3); [[2]](#ref-2) selects streams on a development subset. The target tunes weights and the 70-leaf size on the test set (§3.3) and does not name the data for the 220-leaf choice (§4).

**State of the art:** The 2024 open-vocabulary silent-EMG test [[7]](#ref-7) [later]; the target decodes 10 sentences per speaker with the 101 test words (§2.2). Verdict: standard, below the lineage's best protocol [[2]](#ref-2).

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Read sentences, both modes; EMG-PIT | Read sentences | – | standard |
| M02 Training-only supervision | Audio forced-alignment labels | Paired-audio labels | – | standard |
| M03 Training and adaptation | Per-speaker; pooled, same speakers tested | Per-speaker models | Left-out-speaker adaptation [[8]](#ref-8) | standard |
| M04 Use-time action | Audible scored; silent unscored | Overt speech | – | standard |
| M05 Sensors | 5 channels, TD15 + LDA | TD features | – | standard |
| M06 Processing and decoding | Bundled phonetic-feature streams | Phone units without feature streams, of 12 prior studies (pattern match 8) | 12.2% WER, silent, open vocabulary [[7]](#ref-7) | ahead |
| M07 Lexicon and LM | Trigram, 101 test words | Trigram, test words | – | standard |
| M08 Output | Words; lattices | Words | – | standard |
| M09 Confirmation | Offline | None | – | not applicable |
| M10 Correction | Offline | None | – | not applicable |
| M11 Reference construction | Read prompts | Prompt text | – | standard |
| M12 Evaluation | Test-set tuning | Test-informed selection | Open-vocabulary test [[7]](#ref-7) | standard |
| M13 Device and cost | Lab acquisition | Lab setup | – | standard |

## Where the claims outrun the evidence

- **Silent speech.** Claimed in §1, scored nowhere (§2.2); the [concurrent] silent test reached 30.10% WER for the one speaker with earlier silent sessions [[4]](#ref-4).
- **Effect size.** Test-set tuning (§3.3, the authors' caveat) makes the reported gains optimistic.
- **Stream count.** Five streams give 31.25% and nine 31.49% (Fig. 7).
- **Significance.** α = 0.7% (§3.2) against α ≤ 0.07% (Table 3).
- **Lattice.** 18.76% WER at density 100 (§3.4) is an oracle bound (inference).
- **Prior work.** §3.2 credits [[2]](#ref-2) with up to 10% relative; that paper reports 11.8%.

## What the field needs next

- M06: bundled features against a context-dependent phone system of matched Gaussian count, tuned on held-out sessions.
- M04 and M12: a silent-mode test on the EMG-PIT silent recordings.
- M03: leave-one-speaker-out tests over the 64 main-collection speakers.
- M06: bundled features as an auxiliary target of a neural EMG encoder on the benchmark of [[7]](#ref-7).

## Questions for the authors

- On which data was the 220-leaf size chosen?
- What do the bundled systems score with weights fixed on another session?
- How large must a context-dependent phone system be to match 31.49% WER?
- How is the TD15 mean normalized, and is LDA fitted on training data only?
- What is the best system's silent-mode WER?

## Appendix: literature search

- **M06 articulatory-recognizer-unit-and-context-modeling** (new topic). Inclusion rule: recognizers of phones, words or sentences from non-acoustic speech-production signals, classified by unit design (context-independent units; context-dependent or tree-clustered units; phonetic-feature streams beside phone models; data-driven bundling of features); acoustic-input and lip-video-only recognizers, feature prediction without a recognizer, perception studies and reviews excluded; versions once. Ledger: 7,345 slot-filled; 118 pattern match (unique studies); 13 full-text-only folders on bundling. Dated population, 12 prior unique studies (published M06 table): no feature stream 8, feature streams 4, context-dependent units 7, bundled features 0 (pattern match). All years: context-dependent 36, feature streams 26, bundled features 21, all but one (a neuroscience paper) from the target's line or papers and surveys citing it. Read in full: [[6]](#ref-6), [[5]](#ref-5), [[2]](#ref-2), [[3]](#ref-3) (prior), [[4]](#ref-4) ([concurrent]), [[7]](#ref-7) (state of the art). Known-item recall 0.75 (4 seeds).
- **M03 emg-cross-speaker-training-and-calibration** (published table, reused). Inclusion rule: surface-EMG decoders trained on several speakers and tested on a speaker held out of training, with or without adaptation; pooled training with speaker-mixed tests excluded; versions once. Ledger: 1,526 slot-filled; 64 pattern match (unique studies); 4 confirmed, 1 before the target [[3]](#ref-3). The target is listed and excluded. Usual design: held-out-speaker test of a pooled model 40 (pattern match, all years). State of the art: [[8]](#ref-8). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Schultz, T., Wand, M. “Modeling Coarticulation in EMG-based Continuous Speech Recognition.” *Speech Communication*, 2010, 52(4), 341. doi:[10.1016/j.specom.2009.12.002](https://doi.org/10.1016/j.specom.2009.12.002). Target. Read as the accepted manuscript (HAL hal-00616230v1). [wiki: doi-10.1016-j.specom.2009.12.002](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1016-j.specom.2009.12.002/article.md)
2. <a id="ref-2"></a>Jou, S. S., Schultz, T., Waibel, A. “Continuous Electromyographic Speech Recognition with a Multi-Stream Decoding Architecture.” *Proc. IEEE ICASSP 2007*, 2007, 401-404. doi:[10.1109/ICASSP.2007.366934](https://doi.org/10.1109/ICASSP.2007.366934). Prior; same group; deciding prior for M06 and M12. [wiki: doi-10.1109-icassp.2007.366934](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-icassp.2007.366934/article.md)
3. <a id="ref-3"></a>Wand, M., Schultz, T. “Towards Speaker-Adaptive Speech Recognition Based on Surface Electromyography.” *Proc. BIOSIGNALS 2009, Porto*, 2009, 155-162. doi:[10.5220/0001549601550162](https://doi.org/10.5220/0001549601550162). Prior; same group; deciding prior for M06 and M03. Venue and year as cited by the target (Wand and Schultz 2009b). [wiki: doi-10.5220-0001549601550162](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.5220-0001549601550162/article.md)
4. <a id="ref-4"></a>Wand, M., Jou, S. S., Toth, A. R., Schultz, T. “Impact of Different Speaking Modes on EMG-based Speech Recognition.” *Proc. Interspeech 2009*, 2009. doi:[10.21437/Interspeech.2009-228](https://doi.org/10.21437/Interspeech.2009-228). Concurrent; same group and corpus; uses the target's bundled phonetic features and cites the target. [concurrent] [wiki: isca-wand09_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-wand09_interspeech/article.md)
5. <a id="ref-5"></a>Walliczek, M., Kraft, F., Jou, S., Schultz, T., Waibel, A. “Sub-Word Unit based Non-Audible Speech Recognition using Surface Electromyography.” *Proc. Interspeech 2006*, 2006. doi:[10.21437/Interspeech.2006-425](https://doi.org/10.21437/Interspeech.2006-425). Prior; same group; deciding prior for M06. [wiki: isca-walliczek06_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-walliczek06_interspeech/article.md)
6. <a id="ref-6"></a>Jou, S., Schultz, T., Walliczek, M., Kraft, F., Waibel, A. “Towards Continuous Speech Recognition Using Surface Electromyography.” *Proc. Interspeech 2006 - ICSLP*, 2006. doi:[10.21437/Interspeech.2006-212](https://doi.org/10.21437/Interspeech.2006-212). Prior; same group; deciding prior for M06. [wiki: isca-jou06_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-jou06_interspeech/article.md)
7. <a id="ref-7"></a>Benster, T., Wilson, G., Elisha, R., Willett, F. R., Druckmann, S. “A Cross-Modal Approach to Silent Speech with LLM-Enhanced Recognition.” *arXiv preprint*, 2024. doi:[10.48550/arXiv.2403.05583](https://doi.org/10.48550/arXiv.2403.05583). arXiv:[2403.05583](https://arxiv.org/abs/2403.05583). Later; state of the art for M06. [later] [wiki: arxiv-2403.05583](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2403.05583/article.md)
8. <a id="ref-8"></a>Scheck, K. “Personalizing Myoelectric Silent Speech Interfaces via Cross-Speaker Training and Voice Timbre Control.” *University of Bremen (dissertation)*, 2026. doi:[10.26092/elib/5498](https://doi.org/10.26092/elib/5498). Later; dissertation reprinting Scheck et al. 2024 (EMBC); state of the art for M03 in the published table. [later] [wiki: doi-10.26092-elib.5498](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.26092-elib.5498/article.md)
