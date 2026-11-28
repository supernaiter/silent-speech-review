# A Cascade Sequence-to-Sequence Model for Chinese Mandarin Lip Reading

Zhao, Y., Xu, R., Song, M. · ACM Multimedia Asia (MMAsia '19) · 2019 · [doi:10.1145/3338533.3366579](https://doi.org/10.1145/3338533.3366579) · [arXiv:1908.04917](https://arxiv.org/abs/1908.04917)

## Verdict

CSSMCM [[1]](#ref-1) changes the intermediate representation (M06), adding an explicit tone stage between pinyin syllables and characters, and the evaluation reference (M11), the CMLR corpus labelled by an ASR system. The tone stage has no precedent among the 2 prior Mandarin lip-reading decoders (Appendix), but it is standard by our rules: its support is one 1.59-point CER margin over the authors' re-implementation of LipCH-Net [[2]](#ref-2), from one run on one random split (Table 3). The strongest confound is that split: all 11 hosts appear in training and test, and on unseen hosts CSSMCM rises to 50.08% CER [[3]](#ref-3). CMLR's labels are unchecked ASR output (§3). The abstract's state-of-the-art claim rests on re-implemented baselines, and the same group's [concurrent] LIBS reaches 31.27% on CMLR without a tone stage [[4]](#ref-4).

## Against the field, component by component

### M06 Intermediate representation: pinyin syllables, tones, characters

**Usual approach:** the 2 prior Mandarin lip-reading decoders either output characters directly [[5]](#ref-5) or cascade picture-to-pinyin and pinyin-to-Hanzi [[2]](#ref-2) (pattern match, Appendix). CSSMCM keeps the cascade with syllables (§1) and adds a tone sub-network.

**State of the art:** in 2025, VALLR-Pin [[6]](#ref-6) [later] reaches 7.89% CER on CMLR by adding toneless pinyin and LLM refinement to the 9.10% model of Ma et al. [[7]](#ref-7) (9.1±0.05% over ten runs, Mandarin language model, no phonetic intermediate). CSSMCM's 32.48% is greedy with no language model, so the 24.59-point gap (inference) is not a representation effect alone.

LipCH-Net names intonation marks only within pinyin; the visual tone correlates behind the design (§1) come from analyses such as a one-speaker motion-capture study [[8]](#ref-8), and across signals the closest earlier design is sEMG tone classification of Thai monosyllables from one subject [[9]](#ref-9). Of the 53 [later] Mandarin decoders, 10 mention pinyin and 3 tone prediction (pattern match, Appendix). On the same corpus, VALLR-Pin's toneless-pinyin step gains 1.21 points from 9.10 (inference); CSSMCM's tone step gains 1.59 points from 34.07, 4.7% relative (inference), and tone error falls from 6.99% to 6.14% with video (Table 3). The authors report that tone without video is worst overall, 42.23% CER, from error accumulation (§4.3). Verdict: standard; ahead needs repetition across seeds, speakers or datasets, and there is none.

### M11 Reference transcripts: ASR-labelled broadcast corpus

**Usual approach:** LipCH-Net's 20,495-sentence CCTV set used broadcast manuscripts checked by two persons [[2]](#ref-2); of the 2 prior studies, 1 mentions manuscripts and manual checking and 0 ASR-generated labels (pattern match, Appendix). CMLR uses iFLYTEK output and its timestamps (§3).

**State of the art:** CMLR became the shared Mandarin sentence benchmark; Ma et al. (2022) [[7]](#ref-7) report 9.1% CER against its ASR-derived references, as do later studies [[3]](#ref-3), [[6]](#ref-6), with no label audit.

The 102,076-sentence corpus (Table 2) is the paper's lasting contribution, but without a transcript-error rate every CER since, including 7.89%, has an unknown label-noise floor. Verdict: standard; with one prior corpus the behind rule (3 studies) is not met.

### M12 Evaluation: shared hosts, one run, re-implemented baselines

**Usual approach:** LipCH-Net also splits 7:1:2 with every speaker in each partition [[2]](#ref-2); 0 of the 2 prior studies report run-to-run variability (pattern match, Appendix). CSSMCM follows this and does not name the partition behind Table 3.

**State of the art:** LipFormer (2023) [[3]](#ref-3) reports 27.79% CER with overlapping speakers and 43.18% on 2 unseen speakers after training on 9; Ma et al. report spread over ten runs [[7]](#ref-7).

LipFormer's re-run puts CSSMCM at 32.48% on overlapping and 50.08% on unseen hosts, 17.6 points or 54% higher (inference). Verdict: standard for its time; the generalization the abstract implies is not tested.

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
| M11 Reference construction | iFLYTEK ASR transcripts, unchecked | Checked broadcast manuscripts (pattern match 1) | CMLR references reused unchanged by [[7]](#ref-7) (2022) | standard |
| M12 Evaluation | Random 7:1:2, hosts shared, one run | No run-to-run variability (pattern match 2) | [[3]](#ref-3) (2023): unseen-speaker CMLR CER 43.18% | standard |
| M13 Device and cost | No runtime or size report | Not reported | – | not applicable |

## Where the claims outrun the evidence

- "Surpasses the performance of state-of-the-art lip reading frameworks" (Abstract) rests on one run per model against WAS without audio and a LipCH-Net whose CTC loss the authors replaced (§4.2); Ma et al. list that re-implementation's 34.0 as LipCH-Net [[7]](#ref-7).
- The claim that Table 3 "verifies the conjecture" on head motion and tone (§4.3) rests on a 0.85-point tone-error difference (inference) between two sub-networks; the paragraph also says VP2T predicts "the pinyin sequence".
- Table 3 does not say whether the sub-network rows (VPT2C 3.90%) take reference inputs, and the overall PER, 36.22%, exceeds the 27.96% of the V2P row it starts from.
- Tone attention "serves as the language model" (§4.4) is read off one attention map.

## What the field needs next

- M06: explicit-tone versus toneless-pinyin ablation on one modern backbone, on unseen CMLR hosts, with several seeds.
- M11: a human-transcribed sample of CMLR test references with its label error rate.
- M12: overlap and unseen-host CMLR results, as in LipFormer, with run-to-run spread.

## Questions for the authors

- Which partition produced Table 3?
- Do the sub-network rows take reference or predicted inputs, and why is overall PER above V2P PER?
- How were pinyin and tone labels derived (converter, polyphonic characters, tone sandhi, neutral tone)?
- What is the character error of the iFLYTEK labels on a checked sample?
- How many seeds were run, and what is the spread of the 1.59-point margin?

## Appendix: literature search

Population (all three topics): Mandarin lip-reading decoders, i.e. text-output lip-reading, VSR or AVSR systems that take lip or face video at test and report a result on a Mandarin corpus; perception, neuroimaging and education studies, surveys, dataset or challenge descriptions, enhancement, separation, synthesis, cued speech, keyword spotting and non-visual decoders excluded; versions merged by title (titles filled from manifests). 59 unique studies besides the target, dated by first public version against 2019-08: 2 prior, 4 [concurrent], 53 [later]. Ledger selection: 61 unique studies pattern match (target and its versions included).

- M06, mandarin-lipreading-phonetic-intermediate (new). Inclusion rule: the population above, classified from the full text (reference list removed) by intermediate units named: pinyin or syllables, explicit tone prediction, multi-stage cascade; mentions count (upper bound). Prior 2: pinyin 1, cascade 1, tone prediction 0, direct characters 1. [Concurrent] 4: tone prediction 1 (describing the target). [Later] 53: pinyin 10, tone prediction 3, cascade 31 (pattern match). Full-text scan of all texts for tone prediction: 86 folders outside the population; the recall sample holds perception, production, neural and animal studies, none a lip-reading decoder; sEMG Thai tone classification [[9]](#ref-9) is known through a [later] sEMG study's reference list. Read in full: [[2]](#ref-2), [[5]](#ref-5), [[8]](#ref-8), [[4]](#ref-4), [[7]](#ref-7), [[6]](#ref-6). Known-item recall 1.0 (6 seeds).
- M11, mandarin-lipreading-reference-transcripts (new). Inclusion rule: the same population, classified by how corpus references are named: ASR-generated, subtitles or manuscripts, manual checking; mentions count, reused-corpus descriptions included. Prior 2: manuscripts 1, manual check 1, ASR-generated 0. [Concurrent] 4: 0, 0, 0. [Later] 53: subtitles or manuscripts 11, manual check 7, ASR-generated 5 (pattern match). Read in full: [[2]](#ref-2), [[7]](#ref-7), [[3]](#ref-3).
- M12, mandarin-lipreading-speaker-split-and-variability (new). Inclusion rule: the same population, classified by whether an unseen-speaker test is named and whether run-to-run variability is reported; mentions count. Prior 2: unseen-speaker 1 (a related-work mention), variability 0. [Concurrent] 4: unseen-speaker 1, variability 0. [Later] 53: unseen-speaker 16, variability 13 (pattern match). Read in full: [[2]](#ref-2), [[3]](#ref-3), [[7]](#ref-7).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Zhao, Y., Xu, R., Song, M. “A Cascade Sequence-to-Sequence Model for Chinese Mandarin Lip Reading.” *Proceedings of the ACM Multimedia Asia (MMAsia '19)*, 2019. doi:[10.1145/3338533.3366579](https://doi.org/10.1145/3338533.3366579). arXiv:[1908.04917](https://arxiv.org/abs/1908.04917). Target. Read as arXiv:1908.04917v2 (2019-11-28), the camera-ready text with the ACM reference block. [wiki: doi-10.1145-3338533.3366579](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1145-3338533.3366579/article.md) [wiki: arxiv-1908.04917](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1908.04917/article.md)
2. <a id="ref-2"></a>Zhang, X., Gong, H., Dai, X., Yang, F., Liu, N., Liu, M. “Understanding Pictograph with Facial Features: End-to-End Sentence-Level Lip Reading of Chinese.” *Proceedings of the AAAI Conference on Artificial Intelligence*, 2019, 33(01), 9211-9218. doi:[10.1609/aaai.v33i01.33019211](https://doi.org/10.1609/aaai.v33i01.33019211). Prior (LipCH-Net, presented at AAAI-19, January 2019); deciding prior for M06, M11, M12. [wiki: doi-10.1609-aaai.v33i01.33019211](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1609-aaai.v33i01.33019211/article.md)
3. <a id="ref-3"></a>Xue, F., Li, Y., Liu, D., Xie, Y., Wu, L., Hong, R. “LipFormer: Learning to Lipread Unseen Speakers Based on Visual-Landmark Transformers.” *IEEE Transactions on Circuits and Systems for Video Technology*, 2023, 33(9), 4507-4517. doi:[10.1109/TCSVT.2023.3282224](https://doi.org/10.1109/TCSVT.2023.3282224). arXiv:[2302.02141](https://arxiv.org/abs/2302.02141). [Later]; CMLR overlap and unseen-speaker protocols. [later] [wiki: arxiv-2302.02141](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2302.02141/article.md) [wiki: doi-10.1109-tcsvt.2023.3282224](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tcsvt.2023.3282224/article.md)
4. <a id="ref-4"></a>Zhao, Y., Xu, R., Wang, X., Hou, P., Tang, H., Song, M. “Hearing Lips: Improving Lip Reading by Distilling Speech Recognizers.” *Proceedings of the AAAI Conference on Artificial Intelligence*, 2020, 34(04), 6917-6924. doi:[10.1609/aaai.v34i04.6174](https://doi.org/10.1609/aaai.v34i04.6174). arXiv:[1911.11502](https://arxiv.org/abs/1911.11502). [Concurrent]; same group, CMLR without a tone stage. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/hearing-lips-improving-lip-reading-by-distilling-speech-recognizers) [wiki: arxiv-1911.11502](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1911.11502/article.md) [wiki: doi-10.1609-aaai.v34i04.6174](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1609-aaai.v34i04.6174/article.md)
5. <a id="ref-5"></a>Zhou, P., Yang, W., Chen, W., Wang, Y., Jia, J. “Modality Attention for End-to-End Audio-visual Speech Recognition.” *ICASSP 2019 - IEEE International Conference on Acoustics, Speech and Signal Processing*, 2019. doi:[10.1109/ICASSP.2019.8683733](https://doi.org/10.1109/ICASSP.2019.8683733). arXiv:[1811.05250](https://arxiv.org/abs/1811.05250). Prior; deciding prior for M06 (direct Chinese-character output). [wiki: arxiv-1811.05250](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1811.05250/article.md)
6. <a id="ref-6"></a>Sun, C., Xie, D., Xie, W., Qin, B., Yang, H. “VALLR-Pin: Uncertainty-Factorized Visual Speech Recognition for Mandarin with Pinyin Guidance.” *arXiv preprint*, 2025. arXiv:[2512.20032](https://arxiv.org/abs/2512.20032). [Later]; best CMLR CER, toneless pinyin with LLM refinement. [later] [wiki: arxiv-2512.20032](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2512.20032/article.md) [wiki: arxiv-2512-20032-vallrpin](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2512-20032-vallrpin/article.md)
7. <a id="ref-7"></a>Ma, P., Petridis, S., Pantic, M. “Visual speech recognition for multiple languages in the wild.” *Nature Machine Intelligence*, 2022, 4, 930-939. doi:[10.1038/s42256-022-00550-z](https://doi.org/10.1038/s42256-022-00550-z). arXiv:[2202.13084](https://arxiv.org/abs/2202.13084). [Later]; CMLR state of the art without phonetic intermediate, ten runs, Mandarin LM. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/visual-speech-recognition-for-multiple-languages-in-the-wild) [wiki: arxiv-2202.13084](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2202.13084/article.md) [wiki: doi-10.1038-s42256-022-00550-z](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s42256-022-00550-z/article.md) [wiki: doi-10.21203-rs.3.rs-1386805-v1](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.21203-rs.3.rs-1386805-v1/article.md)
8. <a id="ref-8"></a>Attina, V., Gibert, G., Vatikiotis-Bateson, E., Burnham, D. “Production of Mandarin lexical tones: auditory and visual components.” *Proc. Auditory-Visual Speech Processing (AVSP 2010)*, 2010. <https://www.isca-archive.org/avsp_2010/attina10_avsp.html> Prior; production analysis, not a decoder. [wiki: isca-attina10_avsp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-attina10_avsp/article.md)
9. <a id="ref-9"></a>Srisuwan, N., Phukpattaranont, P., Limsakul, C. “Feature selection for Thai tone classification based on surface EMG.” *Procedia Engineering*, 2012, 32, 253-259. doi:[10.1016/j.proeng.2012.01.1265](https://doi.org/10.1016/j.proeng.2012.01.1265). Prior; cross-signal tone classification (sEMG, Thai monosyllables). Read at abstract level.
