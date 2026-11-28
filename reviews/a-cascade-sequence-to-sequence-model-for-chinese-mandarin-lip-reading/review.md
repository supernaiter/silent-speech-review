# A Cascade Sequence-to-Sequence Model for Chinese Mandarin Lip Reading

Zhao, Y., Xu, R., Song, M. · ACM Multimedia Asia (MMAsia '19) · 2019 · [doi:10.1145/3338533.3366579](https://doi.org/10.1145/3338533.3366579) · [arXiv:1908.04917](https://arxiv.org/abs/1908.04917)

## Verdict

CSSMCM [[1]](#ref-1) changes the intermediate representation (M06), adding an explicit tone stage between pinyin syllables and characters, and the evaluation reference (M11), the CMLR corpus labelled by an ASR system. Separate tone recognition existed in Mandarin speech recognition [[2]](#ref-2) but not among the 3 prior Mandarin lip-reading studies (Appendix). It is standard: no repeated runs are reported (Table 3). The 1.59-point CER margin is over LipCH-Net-seq, whose V2P row equals CSSMCM's (27.96% PER), so it bundles tone with video attention, the strongest confound; the only tone-without-video variant is worse, 42.23% against 34.07% (§4.3). CMLR's labels are iFLYTEK output with no reported check; the authors concede "some noise" and timestamp errors (§3). The same group's [concurrent] LIBS reaches 31.27% on CMLR without tones, with a teacher trained on extra AISHELL audio [[3]](#ref-3).

## Against the field, component by component

### M06 Intermediate representation: pinyin syllables, tones, characters

**Usual approach:** of 102 prior lip-reading studies, 64 mention phoneme or viseme units and 24 a cascade (pattern match, Appendix). Of the 3 prior Mandarin studies, LipCH-Net cascades picture-to-pinyin and pinyin-to-Hanzi [[4]](#ref-4) and Zhou et al. output characters [[5]](#ref-5). CSSMCM keeps the cascade with syllables (§1) and adds a tone sub-network.

**State of the art:** VALLR-Pin (2025) [[6]](#ref-6) [later], a preprint, reports 7.89% CER on CMLR by adding toneless pinyin and LLM N-best refinement to the 9.10% of Ma et al. [[7]](#ref-7), who reach 8.1±0.05% with LRW, LRS2, LRS3 and AVSpeech pre-training and no phonetic unit.

The design cites Chen and Massaro's perception study "Seeing pitch" (target reference 6) and Mandarin ASR tonal units (§5). LipCH-Net does not say whether its pinyin labels carry tone marks. Of 53 [later] Mandarin decoders, 10 mention pinyin and 3 tone prediction, one describing the target (Appendix). Removing phoneme and viseme supervision from a [later] model raises CMLR CER from 20.38% to 35.25% [[8]](#ref-8), evidence for intermediate units, not tone. Verdict: standard; ahead needs repetition across seeds, speakers or datasets, and there is none.

### M11 Reference transcripts: ASR-labelled broadcast corpus

**Usual approach:** of the 3 prior Mandarin studies, 2 mention subtitles or manuscripts, 2 manual checking and 1 ASR-generated labels (pattern match, Appendix). LipCH-Net used manuscripts checked by two persons [[4]](#ref-4); LRW-1000 checked ASR transcripts over "several rounds of interleaved mannual and automatic check" [[9]](#ref-9).

**State of the art:** –; the papers read, Ma et al. (2022) [[7]](#ref-7), LipFormer [[10]](#ref-10) and VALLR-Pin [[6]](#ref-6), score against the released references with no label audit.

The 102,076-sentence corpus (Table 2) is the lasting contribution. §1 says it comes "together with subtitles"; §3 says there is "no subtitle or text annotation". Without a transcript-error rate every later CMLR CER has an unknown label-noise floor. Verdict: standard; 2 prior corpora were checked by people, short of the 3 the behind rule needs.

### M12 Evaluation: shared hosts, no repeats, re-implemented baselines

**Usual approach:** of 102 prior lip-reading studies, 31 mention an unseen-speaker test (pattern match, Appendix). LipCH-Net splits 7:1:2 with every speaker in each partition [[4]](#ref-4); word-level LRW-1000 splits so "there are no or few overlapped speakers" [[9]](#ref-9). CSSMCM shares hosts and does not name the partition behind Table 3.

**State of the art:** Cascade-Free Mandarin VSR [[8]](#ref-8) (2026, arXiv preprint) reports 38.23% CER with speakers s2 and s6 held out and 20.38% on the official split; Ma et al. report spread over ten runs [[7]](#ref-7).

LipFormer copies CSSMCM's 32.48%; its 50.08% on unseen hosts trains on 9 speakers (81,094 sentences) and tests on 2 (20,978) [[10]](#ref-10), so the 17.6-point rise (inference) mixes unseen speakers with different data. Verdict: standard for its time; the generalization the abstract implies is not tested.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Joint fine-tuning of three stages | Joint optimization of cascade stages | – | standard |
| M02 Training-only supervision | Pinyin and tone labels from ASR text | Derived phonetic labels | – | standard |
| M03 Training and adaptation | Length curriculum, scheduled sampling | WAS training recipe | – | standard |
| M04 Use-time action | Overt broadcast speech, audio removed | Overt speech video | – | standard |
| M05 Sensors | 64x128 grayscale lip crops, VGG | Lip crops from video | – | standard |
| M06 Processing and decoding | Pinyin, tone, then characters | Pinyin cascade, no tone stage (pattern match 1) | [[6]](#ref-6) (2025): CMLR CER 7.89% (toneless pinyin, LLM refinement) | standard |
| M07 Lexicon and LM | Greedy decoding, no LM | No external LM | – | standard |
| M08 Output | Chinese characters (1,779) | Characters | – | standard |
| M09 Confirmation | Offline | Offline | – | not applicable |
| M10 Correction | Offline | Offline | – | not applicable |
| M11 Reference construction | iFLYTEK ASR transcripts, unchecked | Checked transcripts (pattern match 2) | – | standard |
| M12 Evaluation | Random 7:1:2, hosts shared, no repeats | No run-to-run variability (pattern match 2) | [[8]](#ref-8) (2026): unseen-speaker CMLR CER 38.23% | standard |
| M13 Device and cost | No runtime or size report | Not reported | – | not applicable |

## Where the claims outrun the evidence

- "Surpasses the performance of state-of-the-art lip reading frameworks" (Abstract) rests on WAS without audio and a LipCH-Net with its CTC loss replaced (§4.2) and CSSMCM's first stage; Ma et al. list its 34.0 as LipCH-Net [[7]](#ref-7).
- Table 3 "verifies the conjecture" on "the motion of the head" (§4.3) from a 0.85-point tone-error difference (inference) on 64×128 lip crops (§4.1).
- The sub-network rows must take reference inputs: VPT2C reaches 3.90% CER from a stage with 27.96% PER (Table 3; inference). Overall PER exceeds V2P PER for every system (36.22%, 39.52%, 46.67%).
- Tone attention "serves as the language model" (§4.4) is read off one attention map.

## What the field needs next

- M06: explicit-tone versus toneless-pinyin ablation on one modern backbone, on unseen CMLR hosts, with several seeds.
- M11: a human-transcribed sample of CMLR test references with its label error rate.
- M12: unseen-host CMLR results with run-to-run spread.

## Questions for the authors

- Which partition produced Table 3?
- How is overall PER defined, given that it exceeds V2P PER for every system?
- How were pinyin and tone labels derived (converter, polyphonic characters, tone sandhi, neutral tone)?
- What is the character error of the iFLYTEK labels on a checked sample?
- How many seeds were run, and what is the spread of the 1.59-point margin?

## Appendix: literature search

Population (all three topics): Mandarin lip-reading decoders, i.e. text-output lip-reading, VSR or AVSR systems that take lip or face video at test and report a result on a Mandarin corpus, including dataset papers that report decoders (LRW-1000); perception, neuroimaging and education studies, surveys, challenge descriptions, enhancement, separation, synthesis, cued speech, keyword spotting and non-visual decoders excluded; versions merged by title (titles filled from manifests). 60 unique studies besides the target, dated by first public version against 2019-08: 3 prior, 4 [concurrent], 53 [later]. Ledger selection: 62 unique studies pattern match (target and its versions included). Language-independent elements (intermediate units, speaker split, variability) were also counted over the published M06 sentence-lipreading-sequence-objective ledger: 633 groups, 102 dated before 2019-02, 38 undated; prior mentions, upper bounds: phoneme or viseme units 64, cascade 24, unseen-speaker test 31, variability terms 60 (the pattern also matches any ±).

- M06, mandarin-lipreading-phonetic-intermediate (new). Inclusion rule: the population above, classified from the full text (reference list removed) by intermediate units named: pinyin or syllables, explicit tone prediction, multi-stage cascade; mentions count (upper bound). Prior 3: pinyin 1, syllable 2, cascade 2, tone prediction 0, direct characters 1. [Concurrent] 4: pinyin 1, cascade 3, tone prediction 1 (describing the target). [Later] 53: pinyin 10, tone prediction 3 (one describing the target), cascade 31 (pattern match). Full-text scan of all texts for tone prediction: 86 folders outside the population, among them an acoustic tone recognizer for continuous Standard Chinese [[2]](#ref-2); the recall sample holds perception, production, neural-decoding, sEMG (one a [later] Mandarin silent-speech decoder), whispered-Mandarin and animal studies, none a lip-reading decoder; sEMG Thai tone classification [[11]](#ref-11) is known through a [later] sEMG study's reference list. [Later] cascades CTCH and CT-MIR-Net, known through Ma et al. Table 3 and Cascade-Free Table III, are outside the ledger. Read in full: [[4]](#ref-4), [[5]](#ref-5), [[2]](#ref-2), [[3]](#ref-3), [[7]](#ref-7), [[6]](#ref-6), [[8]](#ref-8). Known-item recall 1.0 (7 seeds).
- M11, mandarin-lipreading-reference-transcripts (new). Inclusion rule: the same population, classified by how corpus references are named: ASR-generated, subtitles or manuscripts, manual checking; mentions count, reused-corpus descriptions included. Prior 3: subtitles or manuscripts 2, manual check 2, ASR-generated 1. [Concurrent] 4: 0, 0, 0. [Later] 53: subtitles or manuscripts 11, manual check 7, ASR-generated 5 (pattern match). Read in full: [[4]](#ref-4), [[9]](#ref-9), [[7]](#ref-7), [[10]](#ref-10).
- M12, mandarin-lipreading-speaker-split-and-variability (new). Inclusion rule: the same population, classified by whether an unseen-speaker test is named and whether run-to-run variability is reported; mentions count. Prior 3: unseen-speaker 1 (a related-work mention), variability 1 (a ±15-frame offset, not a run spread). [Concurrent] 4: unseen-speaker 1, variability 0. [Later] 53: unseen-speaker 16, variability 13 (pattern match). Read in full: [[4]](#ref-4), [[9]](#ref-9), [[10]](#ref-10), [[7]](#ref-7), [[8]](#ref-8).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Zhao, Y., Xu, R., Song, M. “A Cascade Sequence-to-Sequence Model for Chinese Mandarin Lip Reading.” *Proceedings of the ACM Multimedia Asia (MMAsia '19)*, 2019, 1-6. doi:[10.1145/3338533.3366579](https://doi.org/10.1145/3338533.3366579). arXiv:[1908.04917](https://arxiv.org/abs/1908.04917). Target. Read as arXiv:1908.04917v2 (2019-11-28), the camera-ready text with the ACM reference block. [wiki: doi-10.1145-3338533.3366579](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1145-3338533.3366579/article.md) [wiki: arxiv-1908.04917](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1908.04917/article.md)
2. <a id="ref-2"></a>Hirose, K., Hu, X., Wang, X., Minematsu, N. “Tone recognition of continuous speech of standard Chinese using neural network and tone nucleus model.” *Proc. Interspeech 2006*, 2006. doi:[10.21437/interspeech.2006-600](https://doi.org/10.21437/interspeech.2006-600). Prior; acoustic tone recognizer for continuous Standard Chinese (M06). [wiki: isca-hirose06b_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-hirose06b_interspeech/article.md)
3. <a id="ref-3"></a>Zhao, Y., Xu, R., Wang, X., Hou, P., Tang, H., Song, M. “Hearing Lips: Improving Lip Reading by Distilling Speech Recognizers.” *Proceedings of the AAAI Conference on Artificial Intelligence*, 2020, 34(04), 6917-6924. doi:[10.1609/aaai.v34i04.6174](https://doi.org/10.1609/aaai.v34i04.6174). arXiv:[1911.11502](https://arxiv.org/abs/1911.11502). Same group; CMLR without a tone stage, speech-recognizer teacher trained with AISHELL audio. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/hearing-lips-improving-lip-reading-by-distilling-speech-recognizers) [wiki: arxiv-1911.11502](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1911.11502/article.md) [wiki: doi-10.1609-aaai.v34i04.6174](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1609-aaai.v34i04.6174/article.md)
4. <a id="ref-4"></a>Zhang, X., Gong, H., Dai, X., Yang, F., Liu, N., Liu, M. “Understanding Pictograph with Facial Features: End-to-End Sentence-Level Lip Reading of Chinese.” *Proceedings of the AAAI Conference on Artificial Intelligence*, 2019, 33(01), 9211-9218. doi:[10.1609/aaai.v33i01.33019211](https://doi.org/10.1609/aaai.v33i01.33019211). Prior: presented at AAAI-19 (27 January to 1 February 2019); online proceedings dated 2019-07-17 (Crossref). Deciding prior for M06, M11, M12. [wiki: doi-10.1609-aaai.v33i01.33019211](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1609-aaai.v33i01.33019211/article.md)
5. <a id="ref-5"></a>Zhou, P., Yang, W., Chen, W., Wang, Y., Jia, J. “Modality Attention for End-to-End Audio-visual Speech Recognition.” *ICASSP 2019 - IEEE International Conference on Acoustics, Speech and Signal Processing*, 2019. doi:[10.1109/ICASSP.2019.8683733](https://doi.org/10.1109/ICASSP.2019.8683733). arXiv:[1811.05250](https://arxiv.org/abs/1811.05250). Prior; direct Chinese-character output (M06). [wiki: arxiv-1811.05250](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1811.05250/article.md)
6. <a id="ref-6"></a>Sun, C., Xie, D., Xie, W., Qin, B., Yang, H. “VALLR-Pin: Uncertainty-Factorized Visual Speech Recognition for Mandarin with Pinyin Guidance.” *arXiv preprint*, 2025. arXiv:[2512.20032](https://arxiv.org/abs/2512.20032). Toneless pinyin with LLM N-best refinement on CMLR. [later] [wiki: arxiv-2512.20032](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2512.20032/article.md) [wiki: arxiv-2512-20032-vallrpin](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2512-20032-vallrpin/article.md)
7. <a id="ref-7"></a>Ma, P., Petridis, S., Pantic, M. “Visual speech recognition for multiple languages in the wild.” *Nature Machine Intelligence*, 2022, 4, 930-939. doi:[10.1038/s42256-022-00550-z](https://doi.org/10.1038/s42256-022-00550-z). arXiv:[2202.13084](https://arxiv.org/abs/2202.13084). CMLR result without a phonetic intermediate, ten runs, Mandarin LM. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/visual-speech-recognition-for-multiple-languages-in-the-wild) [wiki: arxiv-2202.13084](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2202.13084/article.md) [wiki: doi-10.1038-s42256-022-00550-z](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s42256-022-00550-z/article.md) [wiki: doi-10.21203-rs.3.rs-1386805-v1](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.21203-rs.3.rs-1386805-v1/article.md)
8. <a id="ref-8"></a>Yang, L., He, Y., Wu, F., Wang, S. “Cascade-Free Mandarin Visual Speech Recognition via Semantic-Guided Cross-Representation Alignment.” *arXiv preprint*, 2026. arXiv:[2603.21808](https://arxiv.org/abs/2603.21808). CMLR seen and unseen-speaker results; ablation of phoneme and viseme representations. [later] [wiki: arxiv-2603.21808](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2603.21808/article.md) [wiki: arxiv-2603-21808-mandarin](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2603-21808-mandarin/article.md)
9. <a id="ref-9"></a>Yang, S., Zhang, Y., Feng, D., Yang, M., Wang, C., Xiao, J., et al. “LRW-1000: A Naturally-Distributed Large-Scale Benchmark for Lip Reading in the Wild.” *2019 14th IEEE International Conference on Automatic Face & Gesture Recognition (FG 2019)*, 2019, 1-8. doi:[10.1109/FG.2019.8756582](https://doi.org/10.1109/FG.2019.8756582). arXiv:[1810.06990](https://arxiv.org/abs/1810.06990). Prior; Mandarin word-level benchmark with baseline decoders, cited by the target as reference 14. [wiki: arxiv-1810.06990](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1810.06990/article.md)
10. <a id="ref-10"></a>Xue, F., Li, Y., Liu, D., Xie, Y., Wu, L., Hong, R. “LipFormer: Learning to Lipread Unseen Speakers Based on Visual-Landmark Transformers.” *IEEE Transactions on Circuits and Systems for Video Technology*, 2023, 33(9), 4507-4517. doi:[10.1109/TCSVT.2023.3282224](https://doi.org/10.1109/TCSVT.2023.3282224). arXiv:[2302.02141](https://arxiv.org/abs/2302.02141). CMLR overlap and unseen-speaker protocols. [later] [wiki: arxiv-2302.02141](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2302.02141/article.md) [wiki: doi-10.1109-tcsvt.2023.3282224](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tcsvt.2023.3282224/article.md)
11. <a id="ref-11"></a>Srisuwan, N., Phukpattaranont, P., Limsakul, C. “Feature selection for Thai tone classification based on surface EMG.” *Procedia Engineering*, 2012, 32, 253-259. doi:[10.1016/j.proeng.2012.01.1265](https://doi.org/10.1016/j.proeng.2012.01.1265). Prior; cross-signal tone classification (sEMG, Thai monosyllables). Read at abstract level.
