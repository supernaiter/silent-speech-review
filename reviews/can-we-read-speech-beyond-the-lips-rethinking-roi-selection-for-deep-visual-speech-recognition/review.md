# Can We Read Speech Beyond the Lips? Rethinking RoI Selection for Deep Visual Speech Recognition

Yuanhang Zhang, Shuang Yang, Jingyun Xiao, Shiguang Shan, Xilin Chen. IEEE FG, 2020. arXiv: [2003.03206](https://arxiv.org/abs/2003.03206)

## Verdict

The paper [[1]](#ref-1) changes the input region (M05) and the training augmentation (M03), and both are ahead at the time: none of the 162 prior decoders in the Appendix population feeds isolated extraoral regions or masked input patches to a lip reader. Upper-face and cheek inputs carry word information on all three benchmarks, but the whole face beats the mouth only on LRW-1000 and GRID, not on LRW (0.2 points lower when aligned, one run), and face-versus-mouth comparison predates it [[2]](#ref-2). The strongest confound is that Cutout is never applied to mouth crops (Tables I–III), so the largest gain (LRW 85.02% against 83.30%) is not tied to extraoral cues. The state-of-the-art claim fails as worded for GRID, where 2.9% WER with a 5-gram character LM ties the uncompared LCANet [[3]](#ref-3). Later work did not keep the face RoI: the same group returned to aligned lip crops without Cutout [[4]](#ref-4), and the best LRW result read is 93.2% [[5]](#ref-5).

## Against the field, component by component

### M05 Sensors: facial region fed to the decoder

**Usual approach:** a mouth or lip RoI, named by 128 of 162 prior decoders (pattern match, mention count, Appendix), as in [[6]](#ref-6); the paper feeds the aligned whole face and, as probes, the upper face or cheeks alone.

**State of the art:** the face RoI is not the default. The best LRW result read (2024) is 93.2% without word boundaries, LRW only, audio-token loss in training, three seeds [[5]](#ref-5), 8.2 points above the paper (inference). Face input pays off mainly with self-supervised pretraining: on LRS3 (2022), 33.8% WER against 40.3% for the lip RoI after AV-HuBERT pretraining, but 57.1% against 57.8% from scratch [[7]](#ref-7).

No prior decoder in the population feeds the whole face (24 mentions read, Appendix), though the authors credit profile lip reading with a whole-face box (§II-A). The one prior coverage comparison found the lower half face 27% relative WER worse than a mouth-plus-margin RoI on an 11-word digit corpus [[8]](#ref-8), and uncited video-to-speech work had found 40% lower error from face input for one GRID speaker [[2]](#ref-2), against "previously overlooked" (§V). New is isolating extraoral regions, repeated over three datasets: the upper face alone gives 48.33% on LRW and 15.84% on LRW-1000 against chance of 0.2% and 0.1% (inference). Verdict: ahead. The whole-face gain is +3.07 points on LRW-1000 and −1.6 points WER on GRID but negative on LRW, which the authors blame on mouth resolution (§IV-C). In [later] masking, hiding the top 30% of the face moves WER only from 42.5% to 42.7% [[7]](#ref-7): upper-face information is real alone but adds little beside the mouth.

### M03 Training: spatial occlusion augmentation

**Usual approach:** no input masking: none of 162 prior decoders masks input patches, the one hit being spatial dropout [[8]](#ref-8), and 12 name crop and flip (pattern match, Appendix) [[6]](#ref-6).

**State of the art:** not kept. The best [later] single LRW model of an augmentation study (2022), 92.8% with word boundaries, uses crop, flip, mixup and time masking on a mouth RoI, citing Cutout only as earlier work [[9]](#ref-9); the same group's [later] recipe (2020) gets 85.0% on LRW and 48.0% on LRW-1000 from aligned lip crops without Cutout [[4]](#ref-4).

On the aligned face, Cutout adds 1.92 points on LRW and 3.53 on LRW-1000 (inference); the authors note a slight loss on the hardest pose subset (§IV-D). Verdict: ahead, a first use in lip reading repeated over three datasets, one run each. The authors read it as curbing overfitting (Fig. 3), as any regulariser would; without mouth-plus-Cutout the extraoral mechanism is untested.

### M12 Evaluation: run repetition

**Usual approach:** one LRW figure per system; none of 26 prior LRW decoders reports a spread over training runs (pattern match, hand-checked, Appendix), and the paper follows this.

**State of the art:** the best LRW result read (2024) averages three seeds, standard deviation 0.1 points [[5]](#ref-5).

At that spread the single-run LRW face-versus-mouth differences (+0.16 and −0.2 points) are uninterpretable (inference). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | LRW, LRW-1000, GRID video | Recorded speech video | – | standard |
| M02 Training-only supervision | Word labels, GRID transcripts | Text labels only | – | standard |
| M03 Training and adaptation | Face Cutout | No input masking, of 162 prior (pattern match 162) | [[9]](#ref-9) (2022): LRW 92.8%, no Cutout | ahead |
| M04 Use-time action | Voiced speech, video only | Voiced speech video | – | standard |
| M05 Sensors | Aligned face; upper face, cheeks | Mouth or lip RoI (mentions), of 162 prior (pattern match 128) | [[5]](#ref-5) (2024): LRW 93.2% | ahead |
| M06 Processing and decoding | 3D-ResNet18 + Bi-GRU; LipNet | 3D conv + ResNet trunk | – | standard |
| M07 Lexicon and LM | GRID: character 5-gram LM | LipNet decoding | – | standard |
| M08 Output | Word class; GRID sentence | Word class or text | – | standard |
| M09 Confirmation | Offline | Offline | – | not applicable |
| M10 Correction | Offline | Offline | – | not applicable |
| M11 Reference construction | Dataset labels, official splits | Corpus labels | – | standard |
| M12 Evaluation | Single runs | No run spread, of 26 prior (pattern match 26) | [[5]](#ref-5) (2024): 3 seeds, ±0.1 | standard |
| M13 Device and cost | 2-3 GPUs, offline | Offline benchmark | – | not applicable |

## Where the claims outrun the evidence

- State of the art on all three benchmarks (§IV-D): LRW 85.02% exceeds the best prior read, 84.07% with ImageNet and Kinetics pre-training [[6]](#ref-6), and LRW-1000 45.24% exceeds the 38.19% baseline [[10]](#ref-10); GRID 2.9% WER equals LCANet under the same 255-sentence protocol [[3]](#ref-3), cited for that protocol (§IV-B) but omitted from Table III, which compares only LipNet [[11]](#ref-11); LCANet states no LM.
- The GRID face gain uses overlapped speakers, which the authors credit to "idiosyncratic speaking styles" (§IV-C); face features carry more speaker identity (EER 0.76% against 1.03%, LRS3 [[7]](#ref-7)), so part may be speaker recognition.
- "Much better" transfer (§IV-C) rests on one validation run per input (40.35% against 38.40%), and "far above chance" states no chance level.

## What the field needs next

- M03 with M05: mouth or face, with or without Cutout, three seeds or more on LRW and LRW-1000.
- M05: region masking on a pretrained front end with the mouth visible, by LRW-1000 pose subset (hard subset 18.36% to 27.21% with face input, Table VI).
- M12: GRID on unseen speakers, no LM.

## Questions for the authors

- How many runs stand behind each entry of Tables I–III, and what is their spread?
- What do mouth crops trained with Cutout score?
- Which GRID beam width and LM weight, tuned on which data, and what WER without the LM?
- Which seed drew the GRID test sentences; was a validation split held out?
- How many LRW-1000 test samples were scored, which checkpoints are reported, and how were pixels normalised?

## Appendix: literature search

Population (all topics): wiki studies whose ledger or title names lip reading, visual speech recognition or AVSR with camera input and a word, sentence, phoneme or command recognition task; dataset-resource and meta-analysis designs, surveys, book chapters, enhancement and separation, video-to-speech synthesis, talking-face generation, synchronisation, keyword-spotting-only, speaker embedding, human perception, neuroimaging and education studies removed; versions merged. 505 unique decoder studies besides the target: 162 prior (first public before 2019-09), 26 [concurrent] (2019-09 to 2020-09), 315 [later], 2 date unresolved. Every prior and [concurrent] title was checked by hand.

- M05 / visual-speech-roi-selection. Inclusion rule: decoders of the population classified by the facial region their own method feeds the front end (mouth or lip RoI, lower face with jaw and cheeks, whole face, isolated extraoral regions) and whether they compare regions; full-face tracking followed by a mouth crop counts as a mouth RoI; mentions and citations are not designs; video-to-speech is outside the population and named as a cross-task prior. Ledger counts: slot-filled 7,329 unique; ledger pattern match 1,108 unique; filtered population as above. Usual design: mouth or lip RoI named by 128 of 162 prior (pattern match, mention count; 23 of 26 [concurrent], 213 of 315 [later]). Whole face as decoder input: 0 of 162 prior (24 mentions read); lower-face RoI with jaw or cheeks: 4; isolated extraoral input: 0; region-coverage comparison: 1 [[8]](#ref-8). [concurrent]: no face-input design (3 mentions read). Whole-wiki full-text pattern: 49 further papers, read as snippets; prior same-design hits only in video-to-speech [[2]](#ref-2). Same-group prior: the LRW-1000 benchmark uses a mouth RoI [[10]](#ref-10). Cited by the target, outside the population: Chung and Zisserman, profile lip reading with a whole-face bounding box, and Shiraishi and Saitoh, optical-flow features in non-rectangular lower-face RoIs (target §II-A, references 10 and 24). Read in full: [[8]](#ref-8), [[2]](#ref-2), [[6]](#ref-6), [[7]](#ref-7), [[4]](#ref-4), [[5]](#ref-5). Known-item recall 1.0 (4 of 4).
- M03 / spatial-occlusion-augmentation-lip-reading. Inclusion rule: the same population, classified by whether training masks or erases spatial patches of the input frames; spatial dropout, time masking, mixup and crop or flip do not count; citations of the target are not designs. Ledger counts: slot-filled 1,526 unique; ledger pattern match 1,108 unique. Usual design: no spatial occlusion of the input, 162 of 162 prior (pattern match, hand-checked; 1 hit read: spatial dropout); crop and flip named by 12 of 162 (mention count). Spatial occlusion of the input: 0 of 26 [concurrent] (3 hits read: two citations of the target, one spatial dropout), 21 [later] mentions. Whole-wiki full-text pattern: 5 further papers, none prior. Read in full: [[6]](#ref-6), [[8]](#ref-8), [[9]](#ref-9), [[4]](#ref-4), [[5]](#ref-5). Known-item recall 1.0 (2 of 2).
- M12 / lrw-word-accuracy (published table reused, counts appended). Inclusion rule: visual-only LRW top-1 accuracy; appended here, the LRW decoders of the population dated against 2020-03. Ledger counts: slot-filled 6,960 unique; pattern match 155 unique (published). LRW decoders of the population: 26 prior, 14 [concurrent], 126 [later]. Spread over training runs: 0 of 26 prior and 0 of 14 [concurrent] after hand check (the two regex hits time inference); 10 of 126 [later] mentions. Significance test named: 2 of 26 prior. Read in full: [[3]](#ref-3), [[11]](#ref-11), [[10]](#ref-10), [[6]](#ref-6), [[5]](#ref-5). Known-item recall 0.75 (published).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Zhang, Y., Yang, S., Xiao, J., Shan, S., Chen, X. “Can We Read Speech Beyond the Lips? Rethinking RoI Selection for Deep Visual Speech Recognition.” *arXiv preprint (published at IEEE FG 2020)*, 2020. doi:[10.48550/arXiv.2003.03206](https://doi.org/10.48550/arXiv.2003.03206). arXiv:[2003.03206](https://arxiv.org/abs/2003.03206). Target. Read as arXiv v2. [wiki: arxiv-2003.03206](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2003.03206/article.md)
2. <a id="ref-2"></a>Ephrat, A., Peleg, S. “Vid2speech: Speech Reconstruction from Silent Video.” *arXiv preprint*, 2017. arXiv:[1701.00495](https://arxiv.org/abs/1701.00495). Prior; cross-task deciding prior for M05 (face versus mouth input, video-to-speech, one GRID speaker). Not cited by the target. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/vid2speech-speech-reconstruction-from-silent-video) [wiki: arxiv-1701.00495](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1701.00495/article.md)
3. <a id="ref-3"></a>Xu, K., Li, D., Cassimatis, N., Wang, X. “LCANet: End-to-End Lipreading with Cascaded Attention-CTC.” *arXiv preprint*, 2018. arXiv:[1803.04988](https://arxiv.org/abs/1803.04988). Prior; GRID comparison for M12. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lcanet-end-to-end-lipreading-with-cascaded-attention-ctc) [wiki: arxiv-1803.04988](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1803.04988/article.md)
4. <a id="ref-4"></a>Feng, D., Yang, S., Shan, S., Chen, X. “Learn an Effective Lip Reading Model without Pains.” *arXiv preprint*, 2020. arXiv:[2011.07557](https://arxiv.org/abs/2011.07557). Later; same group; aligned lip crops without Cutout. [later] [wiki: arxiv-2011.07557](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2011.07557/article.md)
5. <a id="ref-5"></a>Ahn, Y. J., Park, J., Park, S., Choi, J., Kim, K. “SyncVSR: Data-Efficient Visual Speech Recognition with End-to-End Crossmodal Audio Token Synchronization.” *arXiv preprint*, 2024. arXiv:[2406.12233](https://arxiv.org/abs/2406.12233). Later; state of the art on LRW and CAS-VSR-W1K (mean of three seeds). [later] [wiki: arxiv-2406.12233](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2406.12233/article.md)
6. <a id="ref-6"></a>Weng, X., Kitani, K. “Learning Spatio-Temporal Features with Two-Stream Deep 3D CNNs for Lipreading.” *arXiv preprint*, 2019. arXiv:[1905.02540](https://arxiv.org/abs/1905.02540). Prior; best prior LRW result read; mouth crop with crop and flip augmentation. [wiki: arxiv-1905.02540](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1905.02540/article.md)
7. <a id="ref-7"></a>Zhang, J., Wan, G., Pan, J. “Is Lip Region-of-Interest Sufficient for Lipreading?.” *arXiv preprint*, 2022. arXiv:[2205.14295](https://arxiv.org/abs/2205.14295). Later; face versus lip RoI with and without self-supervised pretraining on LRS3. [later] [wiki: arxiv-2205.14295](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2205.14295/article.md)
8. <a id="ref-8"></a>Koumparoulis, A., Potamianos, G., Mroueh, Y., Rennie, S. J. “Exploring ROI size in deep learning based lipreading.” *Proc. International Conference on Auditory-Visual Speech Processing (AVSP 2017)*, 2017. <https://www.isca-archive.org/avsp_2017/koumparoulis17_avsp.html> Prior; deciding prior for M05 (lower-face RoI coverage comparison) and M03 (spatial dropout only). [wiki: isca-koumparoulis17_avsp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-koumparoulis17_avsp/article.md)
9. <a id="ref-9"></a>Ma, P., Wang, Y., Petridis, S., Shen, J., Pantic, M. “Training Strategies for Improved Lip-reading.” *arXiv preprint*, 2022. arXiv:[2209.01383](https://arxiv.org/abs/2209.01383). Later; augmentation study on LRW. [later] [wiki: arxiv-2209.01383](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2209.01383/article.md)
10. <a id="ref-10"></a>Yang, S., Zhang, Y., Feng, D., Yang, M., Wang, C., Xiao, J., et al. “LRW-1000: A Naturally-Distributed Large-Scale Benchmark for Lip Reading in the Wild.” *arXiv preprint*, 2018. arXiv:[1810.06990](https://arxiv.org/abs/1810.06990). Prior; same group; LRW-1000 baseline used in Table VI. [wiki: arxiv-1810.06990](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1810.06990/article.md)
11. <a id="ref-11"></a>Assael, Y. M., Shillingford, B., Whiteson, S., de Freitas, N. “LipNet: End-to-End Sentence-level Lipreading.” *arXiv preprint*, 2016. arXiv:[1611.01599](https://arxiv.org/abs/1611.01599). Prior; GRID baseline of Table III. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lipnet-end-to-end-sentence-level-lipreading) [wiki: arxiv-1611.01599](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1611.01599/article.md)
