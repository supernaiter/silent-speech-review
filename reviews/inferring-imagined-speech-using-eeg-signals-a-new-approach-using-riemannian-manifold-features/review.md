# Inferring imagined speech using EEG signals: a new approach using Riemannian manifold features

Chuong H. Nguyen, George K. Karavas, Panagiotis Artemiadis. Journal of Neural Engineering 15 (2018) 016002, first published December 2017. [doi:10.1088/1741-2552/aa8235](https://doi.org/10.1088/1741-2552/aa8235)

## Verdict

The paper changes one component, the decoder (M06): CSP-filtered EEG as covariance matrices, mapped to tangent space and classified by a multiclass RVM [[1]](#ref-1). None of the 5 prior scalp-EEG imagined-speech decoders used Riemannian features (Appendix), but the pipeline is the Riemannian BCI approach the authors cite (§6.2), and its advantage is not uniform: two of 12 Tangent+RVM comparisons are not significant (Table 4) and RVM trails ELM on short-versus-long (§6.1), so M06 is standard. Evaluation (M12) is the period's usual within-subject random cross-validation with a stated, untested chance level, also standard. The strongest confound is non-speech information: the analysed interval contains the word-specific visual cue (§4.1), and a [later] re-analysis of the released data attributes the best contrast to muscle tension and that cue and reports lower accuracy when segments of one trial share a fold [[2]](#ref-2). The released dataset is the durable contribution; the robustness and word-complexity claims are not supported.

## Against the field, component by component

### M06 Decoder: covariance tangent-space features with an RVM

**Usual approach:** Of the 5 prior scalp-EEG imagined-speech decoders, 3 name CSP, 3 SVM and 2 LDA, and none uses Riemannian or tangent-space features or an RVM (pattern match, Appendix); the closest read prior classifies segment statistics with SVM and ELM variants [[3]](#ref-3). The paper replaces these features with covariance tangent vectors and the classifier with an RVM.

**State of the art:** On the same dataset, a 2019 [later] tangent-space decoder with PCA and a bagged neural-network ensemble reports 58.6% on three vowels and 60.35% on three short words, against 49.0% and 50.1% here [[4]](#ref-4); its ts+rvm column is copied from this paper and its subject sets differ, so the gap of about 10 points (inference) is not a controlled comparison.

The method is not new to BCI, as the authors state (§6.2, §3.2.1). The representation gain holds on vowels, where Tangent+RVM beats log-variance+LDA, DaSalla et al. and Min et al. at p = 6×10⁻⁵, 2×10⁻⁵ and 5×10⁻⁵, t(7) over 8 subjects (Table 4a), but not against log-variance+LDA on short words (p = 0.055) or on short-versus-long with spatial features (p = 0.091), 6 subjects each (Table 4b, c). RVM against ELM: 49.0% vs 45.2% on vowels (p = 0.01), 50.1% vs 46.6% on short words (p = 0.02), 73.3% vs 76.3% on short-versus-long (p = 0.16) (§6.1); the authors prefer RVM for stability (§6.1). Verdict: standard.

### M12 Evaluation: within-subject random cross-validation and chance

**Usual approach:** 4 of the 5 prior decoders state a chance level and 1 uses a permutation or binomial null (pattern match, Appendix). The paper matches this: randomized 10-fold cross-validation per subject (§5.2), chance at 33% and 50% (Fig. 8), no test against chance (Table 4 tests methods only).

**State of the art:** A 2026 [later] re-analysis of this dataset keeps all segments of a trial in one fold and adds a post-imagery window; pooled median accuracy falls from 0.89 to 0.74, and to 0.55 after imagery, and the authors state that the original cross-validation inflated accuracy [[2]](#ref-2). The paper gives trial-level splits (§5.2) but not how its three overlapping epochs per trial are assigned, which leaves that statement open.

The authors ran the most relevant control themselves: blocked vowel recording for one subject gave 99.3 ± 1.4%, which they call erroneously optimistic (§6.1); the field's top ledger value, 96.4% for four classes, comes from one-class runs [[5]](#ref-5) [later]. Repetition is across subjects only: 8, 6, 6 and 6 of 15 per task, one run, no seed (§5.2). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Cued covert pronunciation, no user training | Prompted imagery | – | standard |
| M02 Training-only supervision | Class labels only | Class-label supervision | – | standard |
| M03 Training and adaptation | Per-subject CSP count and kernels; selection data not stated | Per-subject calibration | – | not reported |
| M04 Use-time action | Covert vowels and words; cue in analysed interval | Cued imagined speech | – | standard |
| M05 Sensors | 64-channel scalp EEG, 256 Hz, 8–70 Hz | Scalp EEG | – | standard |
| M06 Processing and decoding | CSP + covariance tangent vectors + multiclass RVM | Non-Riemannian features (CSP or statistics) + SVM/LDA/ELM, of 5 prior (pattern match 5) | 58.6% three vowels, same dataset [[4]](#ref-4) [later] | standard |
| M07 Lexicon and LM | None (closed set) | No lexicon | – | standard |
| M08 Output | Class label with confidence | Class label | – | standard |
| M09 Confirmation | None (offline) | None | – | not applicable |
| M10 Correction | None (offline) | None | – | not applicable |
| M11 Reference construction | Cued class label | Cue as reference | – | standard |
| M12 Evaluation | Within-subject random 10-fold CV, chance stated, not tested | Within-subject CV, chance stated, untested; of 5 prior (pattern match 4) | Trial-grouped CV and post-imagery check, same dataset [[2]](#ref-2) [later] | standard |
| M13 Device and cost | Offline laboratory analysis | Offline | – | standard |

## Where the claims outrun the evidence

- "Accuracy and robustness" (Abstract): no robustness measure is defined in §5–6.
- Selection: CSP count (6 to 14) and kernels were set per subject and condition with no stated selection set (§5.2); comparators are the best mean over a parameter grid, scored with 20 random 90%/10% splits instead of 10 folds (§6.1). Absolute accuracies are optimistic and the comparison mixes protocols.
- Sound versus meaning (§6.3) compares vowels and short words on different subject sets (Table 2).
- Complexity (§6.3): long words reach 66.2% on two classes, short words 50.1% on three; margins over chance are 16.2 and 16.8 points (inference), κ 0.32 and 0.25 (Table 2).
- The abstract's 70% and 95% are single-subject maxima (Fig. 8; Table 3); the best group mean is 80.1% (Table 2).
- In versus cooperate differs in length; one channel and one band reach 0.609 for one participant in the [later] re-analysis [[2]](#ref-2).

## What the field needs next

- M12: trial-grouped folds, nested selection of CSP count and kernels, a permutation null and repeated seeds, applied to tangent+RVM and the [later] decoders on identical subject sets.
- M04: a cue removed before imagery, duration-matched words and EMG channels, to keep visual and muscular differences out of the covariance.
- M06: Riemannian features against log-variance under the same fold-contained selection.

## Questions for the authors

- Were the three epochs of a trial kept in one fold, and how were their predictions combined?
- Which data selected the CSP component count and kernel adjustments?
- Which mRVM variant, standardization setting and random seeds produced the results?
- Do the accuracies exceed a permutation null?

## Appendix: literature search

M06, covariance-tangent-space-features-imagined-speech-eeg. Inclusion rule: studies that classify imagined, covert or inner speech from scalp EEG; design compared is covariance matrices used as features on the SPD manifold or in tangent space, with the RVM classifier tallied separately; Riemannian terms used only for artifact detection, in related work or in reviews are not deciding priors; covariance inside CSP counts as CSP; versions once; motor-imagery-only studies are outside the population. Ledger population: 167 unique studies (pattern match, all years), of which 3 are dated 2017 or earlier. Target-time population (full-text pattern over the whole wiki, triaged by hand; ECoG, fMRI, perception, ERP-only and review papers excluded; versions once): 5 prior unique studies, 1 [concurrent]. Usual design: non-Riemannian features (CSP, statistics or spectra) with SVM, LDA or ELM, 5 of 5 prior; design hits among the 5 prior (pattern match, including mentions): Riemannian or tangent-space 0, RVM 0, CSP 3, SVM 3, LDA 2. Whole-wiki recall check (Riemannian or tangent-space term together with imagined, covert or inner speech): one earlier hit, a 2017 BCI-meeting workshop report naming Riemannian geometry for artifact detection, excluded as off-population. Read in full: [[3]](#ref-3) (prior), [[4]](#ref-4) (state of the art, [later]). Known-item recall 0.25.

M12, imagined-speech-eeg-chance-reference (published table, reused). Inclusion rule: studies that classify imagined, covert or inner speech from scalp EEG; design compared is whether accuracy is referenced against chance (stated chance level or above-chance test, or a permutation null). Ledger population: 167 unique studies (pattern match, all years); 95 with no chance term. Target-time population as above: chance-level term 4 of 5 prior, permutation or binomial null 1 of 5 (pattern match, including mentions). Read: [[2]](#ref-2) and [[5]](#ref-5) (both [later]). Known-item recall 0.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Nguyen, C. H., Karavas, G. K., Artemiadis, P. “Inferring imagined speech using EEG signals: a new approach using Riemannian manifold features.” *Journal of Neural Engineering*, 2018, 15(1), 016002. doi:[10.1088/1741-2552/aa8235](https://doi.org/10.1088/1741-2552/aa8235). Target. Published version read. [wiki: doi-10.1088-1741-2552-aa8235](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552-aa8235/article.md)
2. <a id="ref-2"></a>Tates, A., Matran-Fernandez, A., Halder, S., Daly, I. “Unpacking the Success of Riemannian Tangent Space Decoding for Speech Imagery.” *IEEE MetroXRAINE 2026 (in press)*, 2026. <https://repository.essex.ac.uk/43678/> Later; same-dataset re-evaluation (M12). [later] [wiki: essex-43678-riemann](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/essex-43678-riemann/article.md)
3. <a id="ref-3"></a>Min, B., Kim, J., Park, H., Lee, B. “Vowel Imagery Decoding toward Silent Speech BCI Using Extreme Learning Machine with Electroencephalogram.” *BioMed Research International*, 2016, 2016, 2618265. doi:[10.1155/2016/2618265](https://doi.org/10.1155/2016/2618265). Prior; closest read prior for M06. [wiki: doi-10.1155-2016-2618265](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1155-2016-2618265/article.md) [wiki: pmc-5206788-vowelelm](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-5206788-vowelelm/article.md) [wiki: pmc-5206788-kumar](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-5206788-kumar/article.md)
4. <a id="ref-4"></a>Singh, A., Gumaste, A. “Decoding Imagined Speech and Computer Control using Brain Waves.” *arXiv preprint*, 2019. arXiv:[1911.04255](https://arxiv.org/abs/1911.04255). Later; same dataset; state of the art for M06. Read as arXiv v4. [later] [wiki: arxiv-1911.04255](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1911.04255/article.md)
5. <a id="ref-5"></a>Jahangiri, A., Sepulveda, F. “The Relative Contribution of High-Gamma Linguistic Processing Stages of Word Production, and Motor Imagery of Articulation in Class Separability of Covert Speech Tasks in EEG Data.” *Journal of Medical Systems*, 2019, 43, 20. doi:[10.1007/s10916-018-1137-9](https://doi.org/10.1007/s10916-018-1137-9). Later; top ledger candidate for closed-set covert-speech EEG accuracy; one class per recording run. [later] [wiki: doi-10.1007-s10916-018-1137-9](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1007-s10916-018-1137-9/article.md)
