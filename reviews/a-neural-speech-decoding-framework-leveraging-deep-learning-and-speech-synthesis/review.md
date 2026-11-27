# A neural speech decoding framework leveraging deep learning and speech synthesis

Xupeng Chen, Ran Wang, Amirhossein Khalilian-Gourtani, Leyao Yu, Patricia Dugan, Daniel Friedman, Werner Doyle, Orrin Devinsky, Yao Wang, Adeen Flinker. Nature Machine Intelligence 6, 467–480, 2024. [doi:10.1038/s42256-024-00824-8](https://doi.org/10.1038/s42256-024-00824-8) · preprint [doi:10.1101/2023.09.16.558028](https://doi.org/10.1101/2023.09.16.558028)

## Verdict

The paper [[1]](#ref-1) changes the intermediate representation (M06), 18 acoustic parameters rendered by a differentiable synthesizer, and the training-only supervision (M02), Praat-supervised speech-autoencoder targets. Both depart from the usual approach (Appendix) but are not new: the authors cite their earlier pipeline and name Praat supervision as the change (§ Methods; § Discussion), and the 2021 preprint already had the parameter decoder, synthesizer and causal variants on five participants [[2]](#ref-2). New here are scale and coverage: 48 participants, 43 on low-density clinical grids, right-hemisphere implants, and Swin and LSTM decoders. The held-out-word test is not new, since novel sentences were tested in 2019 [[3]](#ref-3). Natural speech is claimed without a listener test, which single-word ECoG synthesis had in 2019 [[4]](#ref-4). The causal PCC of 0.797 reconstructs 50 trained words within participants; held-out words are called comparable (Fig. 2b), with no numeric fold means or chance level.

## Against the field, component by component

### M06 Processing: differentiable acoustic-parameter synthesis

**Usual approach:** Of 10 intracranial speech-synthesis decoders first public before 2023-03-17 (pattern match, designs checked, Appendix), 4 regress spectrograms, 3 select units, 2 decode vocoder or formant parameters and 1 uses articulatory kinematics [[5]](#ref-5), [[4]](#ref-4). This paper's loss follows a differentiable synthesizer, contrasted with DDSP by the authors (§ Methods).

**State of the art:** No study isolates this step. On the same paradigm, [concurrent] SwinTW (2024) reaches PCC 0.817 over 43 grid-only participants (new decoder, causality not stated) [[6]](#ref-6); this paper reaches 0.806 non-causal and 0.797 causal (Fig. 2a).

Wiki full text shows no differentiable synthesizer in neural decoding before the 2021 preprint (Appendix), which already "decodes interpretable speech parameters from cortical signals, which drives a rule-based differentiable speech synthesizer" [[2]](#ref-2). Verdict: standard. That preprint compared causal and non-causal ResNet; new here are Swin and LSTM at 48 participants, with no significant causal loss for ResNet and Swin (P=0.093, P=0.196; not an equivalence test) and a loss for LSTM (P=0.009) (Fig. 2a).

### M02 Training-only supervision: speech-autoencoder targets

**Usual approach:** None of the 10 prior decoders names an autoencoder latent (pattern match, Appendix); they regress paired-audio features directly. Across signals, Lip2AudSpec used speech-autoencoder "bottleneck features" in 2017 [[7]](#ref-7).

**State of the art:** No study ablates the guidance loss; the group's [concurrent] 2024 decoder uses the same guidance [[6]](#ref-6).

The authors say their earlier autoencoder "completely relied on unsupervised training" and that Praat supervision is new (§ Methods). Verdict: standard. Loss weights were tuned on three participants, split unstated (§ Methods).

### M08 Output: waveform generation

**Usual approach:** Of the 10 prior decoders, 3 use a neural vocoder, 3 concatenate units, 2 use Griffin-Lim and 2 a formant or parametric vocoder (Appendix); this paper, like [[2]](#ref-2), uses Griffin-Lim.

**State of the art:** Single words: 55 listeners, four choices, 66.1% against 25% chance (2019) [[4]](#ref-4); sentences: median perceptual WER 8.20%, 50-phrase set, one participant, attempted silent speech ([concurrent]) [[8]](#ref-8).

Verdict: standard. PCC and STOI+ use spectrograms (§ Methods), so "naturalistic speech that highly resembles the speaker’s own voice" (§ Discussion) rests on audio examples.

### M12 Evaluation: test partition

**Usual approach:** Of the 10 prior decoders, 8 mention k-fold cross-validation, 4 random splits, 3 held-out sessions, none held-out subjects, 7 a chance control (pattern match, Appendix) [[5]](#ref-5). This paper adds five folds of 10 withheld words (Fig. 2b) to a random trial split; the PNAS version of [[2]](#ref-2) reports an unseen-word test ([concurrent]).

**State of the art:** PCC 0.765 on unseen participants, five-fold within sex (2024, [concurrent]) [[6]](#ref-6); this paper has no held-out-participant test.

Verdict: standard. Each word occurs eight times (§ Methods), so test trials repeat trained words (inference).

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Overt words, 5 tasks | Overt production | – | standard |
| M02 Training-only supervision | Speech-autoencoder targets, Praat labels | Paired-audio targets, of 10 (pattern match 10) | No ablation; [[6]](#ref-6) [concurrent] (2024) same guidance | standard |
| M03 Training and adaptation | Per-participant | Per-participant training | – | standard |
| M04 Use-time action | Overt speech, offline | Overt, offline | – | standard |
| M05 Sensors | Clinical ECoG, 43 LD and 5 HB grids | Clinical ECoG grids | – | standard |
| M06 Processing and decoding | 18 parameters, differentiable synthesizer | Spectrogram regression, of 10 (pattern match 4) | Not isolated; [[6]](#ref-6) [concurrent] (2024): PCC 0.817 | standard |
| M07 Lexicon and LM | None | None at use time | – | standard |
| M08 Output | Griffin-Lim waveform | Neural vocoder or units (3 each), of 10 | [[4]](#ref-4) (2019): 66.1%, 4-choice words | standard |
| M09 Confirmation | Offline | Offline | – | not applicable |
| M10 Correction | Offline | Offline | – | not applicable |
| M11 Reference construction | Own recorded audio | Recorded audio | – | standard |
| M12 Evaluation | Trial split; held-out words | k-fold (mentions), of 10 (pattern match 8) | [[6]](#ref-6) [concurrent] (2024): PCC 0.765, unseen participants | standard |
| M13 Device and cost | Offline; 43.99 ms GPU | Offline | – | standard |

## Where the claims outrun the evidence

- Split: Results give 80/20, Methods 350/50 of 400 trials, that is 87.5/12.5% (§ Results; § Methods).
- Baselines: "significantly more accurate" than direct or GAN decoding (§ Discussion) rests on one baseline, the group's earlier model, in three participants with no test reported (Supplementary Fig. 10).
- Test monitoring: code v1.0.1 tests every epoch, with no validation set (train_e2a.py:770-825); reported epoch and seeds unstated (§ Methods).
- Real time: under 50 ms holds for causal ResNet, 43.99 ± 1.09 ms, not causal Swin, 59.13 ± 0.74 ms (Supplementary Table 1).
- Density: "not significantly different" except participant 2, in five hybrid-grid participants (Fig. 3d).
- Right hemisphere: left-hemisphere damage untested, as the authors concede (§ Discussion).

## What the field needs next

- M06: bottleneck against mel regression on all 48 participants, fixed splits and seeds.
- M12: held-out-word and held-out-participant tests with fold values and a shuffled-data chance level.
- M08: listener tests, Griffin-Lim against neural vocoders.

## Questions for the authors

- Which split produced Fig. 2a, 80/20 or 350/50?
- Do test and training trials share sessions?
- What is the PCC without the guidance loss or the Praat labels?
- Which epoch is reported?

## Appendix: literature search

- Decoder population (M02, M06, M08, M12). Inclusion rule: human studies that synthesize speech acoustics from intracranial recordings during produced or imagined speech, first public before 2023-03-17, drawn from the 180 unique studies (pattern match) of the published intracranial-synthesis ledger pattern after removing talking-face, lip, ultrasound, articulography, EMG and EEG work, perception, primate, review, dataset and ethics papers; versions merged: 10 unique studies (Guenther 2009, Angrick 2019, Anumanchipalli 2019, Herff 2019, Wilson 2020, Angrick 2021, two sEEG studies of 2021-2022, Kohler 2022, one 2022 vocoder-parameter study). Four 2023 decoders are [concurrent]. The same-group 2021 preprint is outside the ledger pattern and counted separately.
- M06 intracranial-synthesis-intermediate-representation. Inclusion rule: the decoder population classified by intermediate representation, designs checked in method passages: spectrogram 4, unit selection 3, vocoder or formant parameters 2, articulatory 1, differentiable synthesizer 0. Whole-wiki full-text search for differentiable synthesis or DDSP: 15 unique studies, all snippets read; none in neural decoding before 2021-12. Unfiltered ledger pattern (mention counts): 63 rows indexed 2022 or earlier. Read in full: [[2]](#ref-2), [[9]](#ref-9), [[5]](#ref-5), [[3]](#ref-3), [[6]](#ref-6). Known-item recall 0.6.
- M02 speech-latent-target (published table, reused). Inclusion rule: non-acoustic-to-speech synthesis supervised with paired speech, by direct spectral regression or by matching a speech-autoencoder latent not used at test time. Published table: 40 unique studies (pattern match, all signals). In the decoder population: autoencoder latent 0 of 10. Read in full: [[7]](#ref-7), [[2]](#ref-2). Known-item recall 0.2.
- M08 intracranial-synthesis-waveform-generation (published table, reused). Inclusion rule: intracranial production-speech reconstruction classified by how acoustic features become a waveform. Published table: 180 unique studies (pattern match). In the decoder population, designs checked: neural vocoder 3, unit concatenation 3, Griffin-Lim 2, formant synthesizer 1, parametric vocoder 1. Read in full: [[5]](#ref-5), [[3]](#ref-3), [[4]](#ref-4). Known-item recall 0.6.
- M12 intracranial-speech-test-partition (published table, reused). Inclusion rule: intracranial speech decoding studies classified by how test data are separated from training data. Published table: 618 unique studies (pattern match). In the decoder population, mention counts: k-fold 8, random trial split 4, held-out session or day 3, held-out subject 0, chance or shuffled control 7; held-out content tested in 1 (novel sentences, [[3]](#ref-3)). Read in full: [[6]](#ref-6), [[2]](#ref-2), [[5]](#ref-5). Known-item recall 0.8.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Chen, X., Wang, R., Khalilian-Gourtani, A., Yu, L., Dugan, P., Friedman, D., et al. “A neural speech decoding framework leveraging deep learning and speech synthesis.” *Nature Machine Intelligence*, 2024, 6, 467-480. doi:[10.1038/s42256-024-00824-8](https://doi.org/10.1038/s42256-024-00824-8). Target. First public as bioRxiv 10.1101/2023.09.16.558028 v1 (2023-09-17). [wiki: doi-10.1038-s42256-024-00824-8](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s42256-024-00824-8/article.md) [wiki: doi-10.1101-2023.09.16.558028](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2023.09.16.558028/article.md) [wiki: pmc-12965882-nmidecode](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12965882-nmidecode/article.md) [wiki: pmc-12965882-nsdecode](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12965882-nsdecode/article.md)
2. <a id="ref-2"></a>Wang, R., Chen, X., Khalilian-Gourtani, A., Yu, L., Dugan, P., Friedman, D., et al. “Distributed feedforward and feedback cortical processing supports human speech production.” *Proceedings of the National Academy of Sciences*, 2023, 120(42), e2300255120. doi:[10.1073/pnas.2300255120](https://doi.org/10.1073/pnas.2300255120). Prior (same group). First public as bioRxiv 10.1101/2021.12.06.471521 (2021-12-07). [wiki: pmc-10589651-ffwd](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10589651-ffwd/article.md)
3. <a id="ref-3"></a>Anumanchipalli, G. K., Chartier, J., Chang, E. F. “Speech synthesis from neural decoding of spoken sentences.” *Nature*, 2019, 568(7753), 493-498. doi:[10.1038/s41586-019-1119-1](https://doi.org/10.1038/s41586-019-1119-1). Prior. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/speech-synthesis-from-neural-decoding-of-spoken-sentences) [wiki: doi-10.1038-s41586-019-1119-1](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-019-1119-1/article.md) [wiki: pmc-9714519-speechsynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-9714519-speechsynth/article.md)
4. <a id="ref-4"></a>Herff, C., Diener, L., Angrick, M., Mugler, E., Tate, M. C., Goldrick, M. A., et al. “Generating natural, intelligible speech from brain activity in motor, premotor, and inferior frontal cortices.” *Frontiers in Neuroscience*, 2019, 13, 1267. doi:[10.3389/fnins.2019.01267](https://doi.org/10.3389/fnins.2019.01267). Prior. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/generating-natural-intelligible-speech-from-brain-activity-in-motor-premotor-and-inferior-frontal-co) [wiki: doi-10.3389-fnins.2019.01267](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnins.2019.01267/article.md)
5. <a id="ref-5"></a>Angrick, M., Herff, C., Mugler, E., Tate, M. C., Slutzky, M. W., Krusienski, D. J., et al. “Speech synthesis from ECoG using densely connected 3D convolutional neural networks.” *Journal of Neural Engineering*, 2019, 16(3), 036019. doi:[10.1088/1741-2552/ab0c59](https://doi.org/10.1088/1741-2552/ab0c59). Prior. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/speech-synthesis-from-ecog-using-densely-connected-3d-convolutional-neural-networks) [wiki: doi-10.1088-1741-2552-ab0c59](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552-ab0c59/article.md) [wiki: pmc-6822609-3dcnn](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-6822609-3dcnn/article.md) [wiki: doi-10.1101-478644](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-478644/article.md)
6. <a id="ref-6"></a>Chen, J., Chen, X., Wang, R., Le, C., Khalilian-Gourtani, A., Jensen, E., et al. “Subject-agnostic transformer-based neural speech decoding from surface and depth electrode signals.” *bioRxiv*, 2024. doi:[10.1101/2024.03.11.584533](https://doi.org/10.1101/2024.03.11.584533). [concurrent] (same group). Later published in Journal of Neural Engineering (2025), doi:10.1088/1741-2552/adab21. [concurrent] [wiki: doi-10.1101-2024.03.11.584533](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2024.03.11.584533/article.md) [wiki: pmc-10980022-satrans-decode](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10980022-satrans-decode/article.md) [wiki: pmc-10980022-subjagn](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10980022-subjagn/article.md) [wiki: doi-10.1088-1741-2552-adab21](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552-adab21/article.md) [wiki: pmc-11773629-sdtrans](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11773629-sdtrans/article.md) [wiki: pmc-11773629-swintw](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11773629-swintw/article.md)
7. <a id="ref-7"></a>Akbari, H., Arora, H., Cao, L., Mesgarani, N. “Lip2AudSpec: Speech reconstruction from silent lip movements video.” *2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2018, 2516-2520. doi:[10.1109/ICASSP.2018.8461856](https://doi.org/10.1109/ICASSP.2018.8461856). arXiv:[1710.09798](https://arxiv.org/abs/1710.09798). Prior. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lip2audspec-speech-reconstruction-from-silent-lip-movements-video) [wiki: arxiv-1710.09798](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1710.09798/article.md)
8. <a id="ref-8"></a>Metzger, S. L., Littlejohn, K. T., Silva, A. B., Moses, D. A., Seaton, M. P., Wang, R., et al. “A high-performance neuroprosthesis for speech decoding and avatar control.” *Nature*, 2023, 620(7976), 1037-1046. doi:[10.1038/s41586-023-06443-4](https://doi.org/10.1038/s41586-023-06443-4). [concurrent]. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-high-performance-neuroprosthesis-for-speech-decoding-and-avatar-control) [wiki: doi-10.1038-s41586-023-06443-4](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-023-06443-4/article.md)
9. <a id="ref-9"></a>Guenther, F. H., Brumberg, J. S., Wright, E. J., Nieto-Castanon, A., Tourville, J. A., Panko, M., et al. “A wireless brain-machine interface for real-time speech synthesis.” *PLoS ONE*, 2009, 4(12), e8218. doi:[10.1371/journal.pone.0008218](https://doi.org/10.1371/journal.pone.0008218). Prior. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-wireless-brain-machine-interface-for-real-time-speech-synthesis) [wiki: doi-10.1371-journal.pone.0008218](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1371-journal.pone.0008218/article.md) [wiki: pmc-2784218-wirelesssynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wirelesssynth/article.md)
