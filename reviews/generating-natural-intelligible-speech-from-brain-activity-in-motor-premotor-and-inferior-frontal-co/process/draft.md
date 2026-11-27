# Generating Natural, Intelligible Speech From Brain Activity in Motor, Premotor, and Inferior Frontal Cortices

Herff, Diener, Angrick, Mugler, Tate, Goldrick, Krusienski, Slutzky, Schultz. Frontiers in Neuroscience 13: 1267, 2019. [doi:10.3389/fnins.2019.01267](https://doi.org/10.3389/fnins.2019.01267)

## Verdict

The paper [[1]](#ref-1) changes the decoder (M06), selecting stored frames by cosine similarity of high-gamma features, and the waveform step (M08), overlap-adding the participant's own audio. Both are standard. Unit selection is new to intracranial synthesis (0 of 5 earlier studies, Appendix) but 6 earlier ultrasound and EMG studies used it, and the authors cite the EMG precedent [[2]](#ref-2). The strongest confound is the comparison the paper does not run: on the same six participants a DenseNet-plus-WaveNet decoder correlates higher [[3]](#ref-3), and in EMG unit selection ranked last of four mappings and ran slower than a DNN [[4]](#ref-4), against the paper's claims of superiority and speed. The listener test (M12) is standard, but four options on the 30 best-correlated words support "intelligible" only for those words, and "natural" is not measured.

## Against the field, component by component

### M06 Processing and decoding: unit selection by neural similarity

**Usual approach:** all 5 intracranial production reconstructions first public before 2019-05 regress continuous acoustic or synthesizer parameters, 3 with linear or Kalman models and 3 with deep networks (pattern match, Appendix) [[5]](#ref-5), [[6]](#ref-6). The target instead picks the nearest of over 50,000 stored frames, with no concatenation cost.

**State of the art:** a [later] 2024 framework reaches a mean spectrogram PCC of 0.806 (causal 0.797) across 48 ECoG participants [[7]](#ref-7), against the target's 0.246 on different data.

The design is borrowed, as the paper says: EMG-to-speech matched input segments to an EMG/audio inventory in 2014 [[2]](#ref-2), later with a cosine target cost [[4]](#ref-4). The in-paper baseline is a random-unit null (highest r = 0.04, Fig. 6A), so "superior results than more complex approaches" has no reported comparison. The authors concede "slightly lower" correlations than DNN studies; on the same recordings the gap is a mean of 0.41 against 0.246 (40% lower) and a best participant of 0.69 against 0.574 (17% lower) [[3]](#ref-3) (inference). Word-disjoint folds and waveform-level scoring may explain part of it (inference). Verdict: standard.

### M08 Output: concatenated own-voice units

**Usual approach:** of the 3 earlier intracranial studies that output a waveform, 2 use a parametric synthesizer or vocoder [[5]](#ref-5), [[6]](#ref-6) and 1 a WaveNet trained on another speaker [[3]](#ref-3) (pattern match, Appendix). The target overlap-adds 150 ms windows of the participant's own audio.

**State of the art:** a [later] 2026 intracortical system reaches 5.24% listener transcription WER for one participant, offline [[8]](#ref-8); the target reports no transcription score.

The naturalness argument, that units already carry the speaker's F0, is the EMG argument [[2]](#ref-2). In the EMG head-to-head, listeners never preferred unit selection, DNN mapping ranked first, and unit selection stayed above a real-time factor of 1 while the DNN was fastest [[4]](#ref-4). The target's under 1 ms per 10 ms window holds "for our limited dataset size", and the search grows with the inventory (inference). Verdict: standard.

### M12 Evaluation: listener test

**Usual approach:** all 13 earlier listener-test studies of speech synthesized from non-acoustic signals use transcription or identification (Appendix); the neural production precedent identifies 325 spliced words among 10, 25 and 50 choices and transcribes sentences at a median 31% WER with a 25-word pool [[6]](#ref-6).

**State of the art:** listeners match sentences among 6 at 94.34% and transcribe at a median 43.75% WER [[9]](#ref-9) (2025, [later], intracortical, one participant).

The paper states the design plainly: 55 listeners, four-word forced choice with random distractors from the same mostly CVC list, chance 25%, mean 66.1% (Fig. 5B), 55% of the way from chance to ceiling (inference). Its stimuli are the 30 best-correlated words, and four options is fewer than any choice size in the precedent. STOI 0.15 is mapped to "36%" by a noisy-speech predictor the authors themselves call "notoriously unreliable" for synthesis. Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Overt single-word reading | Recorded overt speech | – | standard |
| M02 Training-only supervision | Paired audio as unit inventory, no labels | Paired-audio targets | – | standard |
| M03 Training and adaptation | Per participant, 8.3-11.7 min, word-disjoint 5-fold | Per-participant training | – | standard |
| M04 Use-time action | Overt reading; causal variant for best participant only | Overt speech | – | standard |
| M05 Sensors | 64-ch 8x8 ECoG, 4 mm; log high gamma, 450 ms context | ECoG grid over speech cortex, high gamma | – | standard |
| M06 Processing and decoding | Nearest-frame unit selection by cosine similarity, no concatenation cost | Regression to continuous parameters (pattern match 5) | [[7]](#ref-7) (2024): PCC 0.806, 48 participants | standard |
| M07 Lexicon and LM | None | None | – | not applicable |
| M08 Output | Overlap-added 150 ms own-voice audio units | Parametric synthesizer or vocoder (pattern match 2) | [[8]](#ref-8) (2026): 5.24% listener WER, offline | standard |
| M09 Confirmation | Offline | Offline | – | not applicable |
| M10 Correction | Offline | Offline | – | not applicable |
| M11 Reference construction | Original microphone audio | Recorded audio | – | standard |
| M12 Evaluation | Four-choice listener test on 30 best words; r; STOI | Listener transcription or identification (confirmed 13) | [[9]](#ref-9) (2025): 94.34% six-sentence match | standard |
| M13 Device and cost | Offline intraoperative; under 1 ms per window | Offline clinical recording | – | standard |

## Where the claims outrun the evidence

- "Natural" and "prosody and accentuation" (Abstract) rest on own-voice units; no naturalness or speaker-similarity rating exists, and listeners rated EMG unit selection lowest [[4]](#ref-4).
- "Superior results than more complex approaches" is contradicted on the same data [[3]](#ref-3).
- "Real-time ready": the causal result (0.528 against 0.57) is reported only for the best participant (Fig. 6B).
- "Intelligible" rests on 30 pre-selected words pooled over unnamed participants (Fig. 5B).
- Recording length of the same participants: 8.3 to 11.7 min (Experiment Design; Table 1) against 8.5 to 12.7 min [[3]](#ref-3).

## What the field needs next

- M06: unit selection, linear regression and a DNN on identical word-disjoint folds, scored on the same waveform.
- M08: own-voice concatenation against a vocoder, rated blind for naturalness and speaker similarity.
- M12: open transcription of every test word, per participant.
- M13: search time against inventory size, in closed loop.

## Questions for the authors

- Which participants supplied the 30 listening words, and what is accuracy per participant?
- Were those words chosen from test-fold correlations only?
- What are the causal correlations for all six participants?
- Which seeds fixed the folds and the 1,000 random-unit baselines?

## Appendix: literature search

- M06 intracranial-synthesis-decoder-architecture (published table, reused and appended). Inclusion rule: intracranial production-speech acoustic reconstruction, classified by the neural-to-acoustic model; prior-time tally of studies first public before 2019-05 reconstructing continuous acoustic or synthesizer parameters from intracranial recordings during produced speech, versions once, reviews, perception and classification studies excluded; Martin 2014 and Chakrabarti 2015 added from the M12 reconstruction table. Ledger: 7,345 slot-filled, 180 pattern match (unique studies). At target time: 5 studies; regression to continuous parameters 5 of 5 (linear or Kalman 3, deep network 3); unit selection 0 of 5; [concurrent] none. Whole-wiki full-text check (unit selection, concatenative or corpus-based synthesis): 153 unique studies (191 folders); 34 folders with the match near a signal term read as snippets; neural-signal unit selection before the target 0 (one 2019 workshop report mentions the authors' talk); biosignal unit selection 6 prior studies (ultrasound and lip video 3, EMG 3). Read in full: [[3]](#ref-3), [[6]](#ref-6), [[2]](#ref-2), [[4]](#ref-4); state of the art [[7]](#ref-7). Known-item recall 1.0.
- M08 intracranial-synthesis-waveform-generation (published table, reused and appended). Inclusion rule: intracranial production-speech acoustic reconstruction, classified by how features become a waveform; prior-time tally of the studies above that output a waveform. Ledger: 3,268 slot-filled, 180 pattern match (unique studies). At target time: 3 studies; parametric synthesizer or vocoder 2 of 3, neural vocoder 1 of 3, own-voice concatenation 0 of 3; same full-text check as M06. Read in full: [[5]](#ref-5) (published table), [[6]](#ref-6), [[3]](#ref-3); state of the art [[8]](#ref-8). Known-item recall 1.0.
- M12 listener-intelligibility-test (published table, reused and appended). Inclusion rule: speech synthesized from non-acoustic signals evaluated by listeners who transcribe or identify words or sentences; naturalness-only, ASR-only, acoustic-input conversion and mentions excluded; versions once. Ledger: 6,960 slot-filled, 37 pattern match (unique studies). At target time: 13 prior studies (confirmed include decisions), 2 of them neural; [concurrent] 2. Read in full: [[6]](#ref-6); state of the art [[9]](#ref-9). Known-item recall 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [generating-natural-intelligible-speech-from-brain-activity-in-motor-premotor-and-inferior-frontal-co.bib](generating-natural-intelligible-speech-from-brain-activity-in-motor-premotor-and-inferior-frontal-co.bib).

1. <a id="ref-1"></a>Herff, C., Diener, L., Angrick, M., Mugler, E., Tate, M. C., Goldrick, M. A., et al. “Generating Natural, Intelligible Speech From Brain Activity in Motor, Premotor, and Inferior Frontal Cortices.” *Frontiers in Neuroscience*, 2019, 13, 1267. doi:[10.3389/fnins.2019.01267](https://doi.org/10.3389/fnins.2019.01267). Target. Read as the published article (PMC6882773), published 22 November 2019. [wiki: doi-10.3389-fnins.2019.01267](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnins.2019.01267/article.md) [wiki: pmc-6882773-b2speech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-6882773-b2speech/article.md) [wiki: pmc-6882773-braintospeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-6882773-braintospeech/article.md)
2. <a id="ref-2"></a>Zahner, M., Janke, M., Wand, M., Schultz, T. “Conversion from Facial Myoelectric Signals to Speech: A Unit Selection Approach.” *Proc. Interspeech 2014*, 2014. doi:[10.21437/Interspeech.2014-164](https://doi.org/10.21437/Interspeech.2014-164). [wiki: isca-zahner14_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-zahner14_interspeech/article.md)
3. <a id="ref-3"></a>Angrick, M., Herff, C., Mugler, E., Tate, M. C., Slutzky, M. W., Krusienski, D. J., et al. “Speech Synthesis from ECoG using Densely Connected 3D Convolutional Neural Networks.” *Journal of Neural Engineering*, 2019, 16(3), 036019. doi:[10.1088/1741-2552/ab0c59](https://doi.org/10.1088/1741-2552/ab0c59). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/speech-synthesis-from-ecog-using-densely-connected-3d-convolutional-neural-networks) [wiki: doi-10.1088-1741-2552-ab0c59](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552-ab0c59/article.md) [wiki: pmc-6822609-3dcnn](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-6822609-3dcnn/article.md) [wiki: doi-10.1101-478644](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-478644/article.md)
4. <a id="ref-4"></a>Janke, M., Diener, L. “EMG-to-Speech: Direct Generation of Speech From Facial Electromyographic Signals.” *IEEE/ACM Transactions on Audio, Speech, and Language Processing*, 2017, 25(12), 2375-2385. doi:[10.1109/TASLP.2017.2738568](https://doi.org/10.1109/TASLP.2017.2738568). [wiki: doi-10.1109-taslp-2017-2738568](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-taslp-2017-2738568/article.md)
5. <a id="ref-5"></a>Guenther, F. H., Brumberg, J. S., Wright, E. J., Nieto-Castanon, A., Tourville, J. A., Panko, M., et al. “A Wireless Brain-Machine Interface for Real-Time Speech Synthesis.” *PLoS ONE*, 2009, 4(12), e8218. doi:[10.1371/journal.pone.0008218](https://doi.org/10.1371/journal.pone.0008218). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-wireless-brain-machine-interface-for-real-time-speech-synthesis) [wiki: pmc-2784218-wireless](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wireless/article.md) [wiki: pmc-2784218-wirelesssynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wirelesssynth/article.md) [wiki: doi-10.1371-journal.pone.0008218](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1371-journal.pone.0008218/article.md)
6. <a id="ref-6"></a>Anumanchipalli, G. K., Chartier, J., Chang, E. F. “Speech synthesis from neural decoding of spoken sentences.” *Nature*, 2019, 568(7753), 493–498. doi:[10.1038/s41586-019-1119-1](https://doi.org/10.1038/s41586-019-1119-1). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/speech-synthesis-from-neural-decoding-of-spoken-sentences) [wiki: doi-10.1038-s41586-019-1119-1](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-019-1119-1/article.md) [wiki: pmc-9714519-speechsynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-9714519-speechsynth/article.md)
7. <a id="ref-7"></a>Chen, X., Wang, R., Khalilian-Gourtani, A., Yu, L., Dugan, P., Friedman, D., et al. “A neural speech decoding framework leveraging deep learning and speech synthesis.” *Nature Machine Intelligence*, 2024. doi:[10.1038/s42256-024-00824-8](https://doi.org/10.1038/s42256-024-00824-8). [later] [wiki: doi-10.1038-s42256-024-00824-8](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s42256-024-00824-8/article.md) [wiki: doi-10.1101-2023.09.16.558028](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2023.09.16.558028/article.md) [wiki: pmc-12965882-nmidecode](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12965882-nmidecode/article.md) [wiki: pmc-12965882-nsdecode](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12965882-nsdecode/article.md)
8. <a id="ref-8"></a>Wairagkar, M., Srinivasan, A., Card, N. S., Singer-Clark, T., Hou, X., Iacobacci, C., et al. “Brain2voice 2.0: High-performance voice synthesis brain-computer interface.” *bioRxiv*, 2026. doi:[10.64898/2026.06.30.735633](https://doi.org/10.64898/2026.06.30.735633). [later] [wiki: doi-10.64898-2026.06.30.735633](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.64898-2026.06.30.735633/article.md)
9. <a id="ref-9"></a>Wairagkar, M., Card, N. S., Singer-Clark, T., Hou, X., Iacobacci, C., Miller, L. M., et al. “An instantaneous voice-synthesis neuroprosthesis.” *Nature*, 2025. doi:[10.1038/s41586-025-09127-3](https://doi.org/10.1038/s41586-025-09127-3). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/an-instantaneous-voice-synthesis-neuroprosthesis) [wiki: doi-10.1038-s41586-025-09127-3](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-025-09127-3/article.md) [wiki: doi-10.1101-2024.08.14.607690](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2024.08.14.607690/article.md) [wiki: pmc-12369848-voicesynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12369848-voicesynth/article.md) [wiki: pmc-12369848-voice-synth-np](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12369848-voice-synth-np/article.md) [wiki: pmc-11370360-instvoice](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11370360-instvoice/article.md)
