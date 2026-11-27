# A neural speech decoding framework leveraging deep learning and speech synthesis

Xupeng Chen, Ran Wang, Amirhossein Khalilian-Gourtani, Leyao Yu, Patricia Dugan, Daniel Friedman, Werner Doyle, Orrin Devinsky, Yao Wang, Adeen Flinker. Nature Machine Intelligence 6, 467–480, 2024. [doi:10.1038/s42256-024-00824-8](https://doi.org/10.1038/s42256-024-00824-8) · preprint [doi:10.1101/2023.09.16.558028](https://doi.org/10.1101/2023.09.16.558028)

## Verdict

The paper [[1]](#ref-1) changes the intermediate representation (M06), 18 acoustic parameters rendered by a differentiable synthesizer, and the training-only supervision (M02), targets from a per-participant speech autoencoder. Both are standard for this paper: the group's 2021 preprint already had the pipeline, with causal and anticausal decoders, on five participants [[2]](#ref-2), although none of 63 prior intracranial-synthesis ledger studies names a differentiable synthesizer (Appendix). What it adds is scale: 48 participants, three decoders, both hemispheres and a held-out-word test (5 of 202 prior studies, Appendix). The claim of natural speech in the speaker's voice is untested: the waveform comes from Griffin-Lim (M08) and no listener rated it, as listeners already did for ECoG synthesis in 2019 [[3]](#ref-3). Its advantage over direct spectrogram or GAN decoding rests on three participants (Supplementary Fig. 10). The causal PCC of 0.797 is within-participant reconstruction of 50 trained words (M12).

## Against the field, component by component

### M06 Processing: differentiable acoustic-parameter synthesis

**Usual approach:** Of 63 prior intracranial-synthesis ledger studies (pattern match, unique studies, 2022 or earlier), 12 name direct spectrogram regression and 27 vocoder or formant parameters [[4]](#ref-4), [[3]](#ref-3); this paper computes its loss after a differentiable synthesizer.

**State of the art:** The group's [concurrent] SwinTW decoder (2024), same 50-word paradigm: subject-specific PCC 0.817 over 43 participants with the grid only, non-causal by its description (inference), and 0.838 over 39 with more electrodes [[5]](#ref-5); this paper reaches 0.806 non-causal and 0.797 causal (Fig. 2a).

Decoded formants drove a synthesizer in 2009 [[6]](#ref-6); differentiability is absent from the 63 prior studies and named in 5 from 2024 on, this paper included (Appendix), but the 2021 preprint already "decodes interpretable speech parameters from cortical signals, which drives a rule-based differentiable speech synthesizer" [[2]](#ref-2). Verdict: standard. New here: causal ResNet and Swin match their non-causal versions (P=0.093, P=0.196) (Fig. 2a).

### M02 Training-only supervision: speech-autoencoder targets

**Usual approach:** Of 11 prior studies in the speech-latent-target population (pattern match, unique studies, 2022 or earlier), 5 name an autoencoder latent and 3 direct spectral regression; Lip2AudSpec used speech-autoencoder "bottleneck features" in 2017 [[7]](#ref-7). Here the latent is interpretable, with Praat labels (§ Methods).

**State of the art:** The same guidance trains the group's [concurrent] 2024 decoder, PCC 0.838 [[5]](#ref-5).

The 2021 preprint's encoder already "generates reference speech parameters from actual speech signals used for the training of the ECoG decoder" [[2]](#ref-2). Verdict: standard. Its loss weights were tuned on three participants, selection split unstated (§ Methods: Model training).

### M08 Output: waveform generation

**Usual approach:** Among the 63 prior studies, 7 name a neural vocoder and 4 Griffin-Lim (pattern match); Angrick et al. used WaveNet [[4]](#ref-4). This paper, like the group's earlier pipeline [[2]](#ref-2), uses Griffin-Lim.

**State of the art:** Listener transcription of synthesized ECoG speech, median 31% WER with a 25-word pool (2019) [[3]](#ref-3); this paper has no listener score.

Verdict: standard. PCC and STOI+ use spectrograms (§ Methods: Evaluation metrics), so "naturalistic speech that highly resembles the speaker’s own voice" (§ Discussion) rests on audio examples only.

### M12 Evaluation: test partition

**Usual approach:** Of 202 prior intracranial ledger studies (pattern match, unique studies, 2022 or earlier), 76 name k-fold cross-validation, 39 random trial splits, 7 held-out subjects and 5 held-out words. This paper adds a five-fold test with 10 words withheld from all training (Fig. 2b) to a within-participant random split.

**State of the art:** PCC 0.765 on participants outside the training set, same paradigm (2024, [concurrent]) [[5]](#ref-5); this paper has no held-out-participant test.

Verdict: standard. Each word is produced eight times (§ Methods: Experiments design), so test trials repeat trained words (inference). The held-out-word result has no fold values (Fig. 2b), and there is no chance level, though the 2021 preprint reported one [[2]](#ref-2).

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Overt words, 5 tasks | Overt production | – | standard |
| M02 Training-only supervision | Speech-autoencoder targets, Praat labels | Autoencoder latent, of 11 (pattern match 5) | [[5]](#ref-5) [concurrent] (2024): PCC 0.838 | standard |
| M03 Training and adaptation | Per-participant; tuning split unstated | Per-participant training | – | not reported |
| M04 Use-time action | Overt speech, offline | Overt, offline | – | standard |
| M05 Sensors | Clinical ECoG, 43 LD and 5 HB grids | Clinical ECoG grids | – | standard |
| M06 Processing and decoding | 18 parameters, differentiable synthesizer | Spectrogram regression, of 63 (pattern match 12) | [[5]](#ref-5) [concurrent] (2024): PCC 0.817 (43, grid only) | standard |
| M07 Lexicon and LM | None | None at use time | – | standard |
| M08 Output | Griffin-Lim waveform | Neural vocoder 7, Griffin-Lim 4 (of 63) | [[3]](#ref-3) (2019): listener WER 31%, 25-word pool | standard |
| M09 Confirmation | Offline | Offline | – | not applicable |
| M10 Correction | Offline | Offline | – | not applicable |
| M11 Reference construction | Own recorded audio | Recorded audio | – | standard |
| M12 Evaluation | Trial split; held-out words | k-fold, of 202 (pattern match 76) | [[5]](#ref-5) [concurrent] (2024): PCC 0.765 on unseen participants | standard |
| M13 Device and cost | Offline; 43.99 ms GPU (causal ResNet) | Offline | – | standard |

## Where the claims outrun the evidence

- Split: Results give 80/20, Methods 350/50 of 400 trials, that is 87.5/12.5% (§ Results; § Methods).
- Selection: the released script tests every epoch with no validation set (train_e2a.py:770-825); no seeds (§ Methods).
- Real time: under 50 ms holds for causal ResNet, 43.99 ± 1.09 ms, not causal Swin, 59.13 ± 0.74 ms (Supplementary Table 1); real time was not the focus (§ Discussion).
- Density: "no consistent gain" rests on five people (Fig. 3d).
- Right hemisphere: people with left-hemisphere damage remain untested, as the authors concede (§ Discussion).

## What the field needs next

- M06: parameter bottleneck against mel regression on all 48 participants, same splits and seeds.
- M12: held-out-word and held-out-participant tests with fold values and a shuffled-data chance level.
- M08: listener tests, Griffin-Lim against a neural vocoder.

## Questions for the authors

- Which split produced Fig. 2a, 80/20 or 350/50?
- Do test trials share recording sessions with training trials?
- What is the PCC without the guidance loss or the Praat labels?
- What are the held-out-word fold values and the chance PCC?

## Appendix: literature search

- M06 intracranial-synthesis-intermediate-representation. Inclusion rule: the published intracranial-synthesis population (ledger text names an intracranial signal and speech synthesis or spectrogram reconstruction; 180 unique studies, pattern match), classified by the intermediate representation its full text names; mention counts, upper bounds. First public 2022 or earlier: 63 unique studies (13 dated 2023, 39 date unresolved). Designs in the prior period: vocoder or formant parameters 27, direct spectrogram regression 12, articulatory kinematic intermediate 7, GAN latent 3, differentiable synthesizer 0; all years: direct spectrogram regression 81, differentiable synthesizer 5 (index year 2024 or later, including the target and its successor). The same-group 2021 preprint is outside the ledger pattern. Read in full: [[2]](#ref-2), [[6]](#ref-6), [[4]](#ref-4), [[3]](#ref-3), [[5]](#ref-5). Known-item recall 0.6.
- M02 speech-latent-target (published table, reused). Inclusion rule: non-acoustic-to-speech synthesis supervised with paired speech, by direct spectral regression or by matching a speech autoencoder latent not used at test time. 40 unique studies (pattern match); first public 2022 or earlier: 11, of which 5 name an autoencoder latent and 3 direct spectral regression. Read in full: [[7]](#ref-7), [[2]](#ref-2). Known-item recall 0.2 (the target is in the population as its PMC version).
- M08 intracranial-synthesis-waveform-generation (published table, reused). Inclusion rule: intracranial production-speech reconstruction classified by how acoustic features become a waveform. 180 unique studies (pattern match); first public 2022 or earlier: 63, of which unit selection 17, neural vocoder 7, Griffin-Lim 4. Read in full: [[4]](#ref-4), [[3]](#ref-3). Known-item recall 0.6.
- M12 intracranial-speech-test-partition (published table, reused). Inclusion rule: intracranial speech decoding studies classified by how test data are separated from training data; held-out words added. 618 unique studies (pattern match); first public 2022 or earlier: 202, of which k-fold 76, random trial split 39, held-out session or day 35, held-out subject 7, held-out words 5. Read in full: [[5]](#ref-5), [[2]](#ref-2). Known-item recall 0.8.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Chen, X., Wang, R., Khalilian-Gourtani, A., Yu, L., Dugan, P., Friedman, D., et al. “A neural speech decoding framework leveraging deep learning and speech synthesis.” *Nature Machine Intelligence*, 2024, 6, 467-480. doi:[10.1038/s42256-024-00824-8](https://doi.org/10.1038/s42256-024-00824-8). Target. Read as the Version of Record (PMC OA BioC XML); first public as bioRxiv 10.1101/2023.09.16.558028 v1, 2023-09-17. [wiki: doi-10.1038-s42256-024-00824-8](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s42256-024-00824-8/article.md) [wiki: doi-10.1101-2023.09.16.558028](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2023.09.16.558028/article.md) [wiki: pmc-12965882-nmidecode](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12965882-nmidecode/article.md) [wiki: pmc-12965882-nsdecode](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12965882-nsdecode/article.md)
2. <a id="ref-2"></a>Wang, R., Chen, X., Khalilian-Gourtani, A., Yu, L., Dugan, P., Friedman, D., et al. “Distributed feedforward and feedback cortical processing supports human speech production.” *Proceedings of the National Academy of Sciences*, 2023, 120(42), e2300255120. doi:[10.1073/pnas.2300255120](https://doi.org/10.1073/pnas.2300255120). Prior (same group); deciding prior for M02 and M06. First public as bioRxiv 10.1101/2021.12.06.471521 (2021-12-07), which already describes the speech-parameter decoder, differentiable synthesizer, pretrained speech encoder and causal/anticausal models; read as the PNAS version. [wiki: pmc-10589651-ffwd](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10589651-ffwd/article.md)
3. <a id="ref-3"></a>Anumanchipalli, G. K., Chartier, J., Chang, E. F. “Speech synthesis from neural decoding of spoken sentences.” *Nature*, 2019, 568(7753), 493-498. doi:[10.1038/s41586-019-1119-1](https://doi.org/10.1038/s41586-019-1119-1). Prior; articulatory-intermediate design (M06) and listener test (M08). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/speech-synthesis-from-neural-decoding-of-spoken-sentences) [wiki: doi-10.1038-s41586-019-1119-1](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-019-1119-1/article.md) [wiki: pmc-9714519-speechsynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-9714519-speechsynth/article.md)
4. <a id="ref-4"></a>Angrick, M., Herff, C., Mugler, E., Tate, M. C., Slutzky, M. W., Krusienski, D. J., et al. “Speech synthesis from ECoG using densely connected 3D convolutional neural networks.” *Journal of Neural Engineering*, 2019, 16(3), 036019. doi:[10.1088/1741-2552/ab0c59](https://doi.org/10.1088/1741-2552/ab0c59). Prior; usual-approach example for M06 and M08 (log-mel regression, WaveNet vocoder). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/speech-synthesis-from-ecog-using-densely-connected-3d-convolutional-neural-networks) [wiki: doi-10.1088-1741-2552-ab0c59](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552-ab0c59/article.md) [wiki: pmc-6822609-3dcnn](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-6822609-3dcnn/article.md) [wiki: doi-10.1101-478644](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-478644/article.md)
5. <a id="ref-5"></a>Chen, J., Chen, X., Wang, R., Le, C., Khalilian-Gourtani, A., Jensen, E., et al. “Subject-agnostic transformer-based neural speech decoding from surface and depth electrode signals.” *bioRxiv*, 2024. doi:[10.1101/2024.03.11.584533](https://doi.org/10.1101/2024.03.11.584533). Concurrent (same group); state of the art for M06 and M12. Later published in Journal of Neural Engineering (2025), 10.1088/1741-2552/adab21. [concurrent] [wiki: doi-10.1101-2024.03.11.584533](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2024.03.11.584533/article.md) [wiki: pmc-10980022-satrans-decode](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10980022-satrans-decode/article.md) [wiki: pmc-10980022-subjagn](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10980022-subjagn/article.md) [wiki: doi-10.1088-1741-2552-adab21](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552-adab21/article.md) [wiki: pmc-11773629-sdtrans](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11773629-sdtrans/article.md) [wiki: pmc-11773629-swintw](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11773629-swintw/article.md)
6. <a id="ref-6"></a>Guenther, F. H., Brumberg, J. S., Wright, E. J., Nieto-Castanon, A., Tourville, J. A., Panko, M., et al. “A wireless brain-machine interface for real-time speech synthesis.” *PLoS ONE*, 2009, 4(12), e8218. doi:[10.1371/journal.pone.0008218](https://doi.org/10.1371/journal.pone.0008218). Prior; interpretable formant parameters driving a synthesizer (M06). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-wireless-brain-machine-interface-for-real-time-speech-synthesis) [wiki: doi-10.1371-journal.pone.0008218](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1371-journal.pone.0008218/article.md) [wiki: pmc-2784218-wirelesssynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wirelesssynth/article.md)
7. <a id="ref-7"></a>Akbari, H., Arora, H., Cao, L., Mesgarani, N. “Lip2AudSpec: Speech reconstruction from silent lip movements video.” *2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2018, 2516-2520. doi:[10.1109/ICASSP.2018.8461856](https://doi.org/10.1109/ICASSP.2018.8461856). arXiv:[1710.09798](https://arxiv.org/abs/1710.09798). Prior; speech-autoencoder bottleneck target (M02). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lip2audspec-speech-reconstruction-from-silent-lip-movements-video) [wiki: arxiv-1710.09798](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1710.09798/article.md)
