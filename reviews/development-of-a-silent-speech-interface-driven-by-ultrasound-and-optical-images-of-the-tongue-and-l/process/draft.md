# Development of a Silent Speech Interface Driven by Ultrasound and Optical Images of the Tongue and Lips

Hueber, Benaroya, Chollet, Denby, Dreyfus, Stone. Speech Communication 52(4), 2010. [doi:10.1016/j.specom.2009.11.004](https://doi.org/10.1016/j.specom.2009.11.004)

## Verdict

The paper [[1]](#ref-1) changes two components. Its visual phone recognizer (M06) is standard, a context-independent HMM-GMM like 10 of the 11 prior articulatory-signal recognizers (Appendix), and weaker than the authors' own [concurrent] context-dependent multi-stream decoder [[2]](#ref-2). Its output route (M08), phone recognition then diphone unit selection, departs from the direct mapping of both prior speech-output studies [[3]](#ref-3), [[4]](#ref-4), but is standard by rule: no direct-mapping baseline is run and synthesis is tested only on oracle phones (§5.3). The main claim, that a visually driven segmental vocoder is "a reasonable approach for making an SSI" (§5.3), rests on that test, while the authors state that about 60% phone accuracy is not enough for intelligible synthesis (§6); system output from recognized phones is not measured, and all data are uttered speech from two speakers (§2).

## Against the field, component by component

### M06 Processing: visual phone recognizer

**Usual approach:** HMMs over frame features: 10 of 11 prior unique studies (pattern match, Appendix), mostly EMG, e.g. context-independent phone HMMs with a trigram language model [[5]](#ref-5) and 3-state phone HMMs [[6]](#ref-6) [concurrent]. The paper follows it with 41 context-independent HMMs on 30+30 PCA coefficients and three dictionary levels (§4.1).

**State of the art:** 6.17% WER on the Silent Speech Challenge benchmark with a 5k-word bigram language model, in 2019 [[7]](#ref-7) [later]; the target reports phone accuracy only, 59.0% to 67.6% for speaker A and 48.3% to 56.0% for speaker B (Table 1); the scales differ.

Verdict standard. The stated reason for staying context-independent, that such models "could not have been efficiently trained" on under one hour (§4.1), is contradicted by the group's [concurrent] 61-minute single-speaker study: context-dependent fusion raised unconstrained phone accuracy from 57.7% to 62.6%, and context-dependent multi-stream HMMs reached 65.6%, an 8-point absolute gain [[2]](#ref-2). The journal cites it only as ongoing fusion work (§4.2).

### M08 Output: recognition, then corpus-based synthesis

**Usual approach:** Both prior studies map EMA frames directly to line spectrum pairs, one speaker each, by database search [[3]](#ref-3) or by linear and neural-network estimation [[4]](#ref-4); the [concurrent] neural BCI maps decoded activity to F1/F2 of a formant synthesizer [[8]](#ref-8). Recognition then synthesis has no prior outside the target's own system, first shown at Interspeech 2008 [[9]](#ref-9) (0 of 2 prior, Appendix).

**State of the art:** Direct mapping to mel spectra with a neural vocoder gives 15.93% ASR WER single-speaker and 31.64% multi-speaker on TaL, in 2026 [[10]](#ref-10) [later]; the target gives no WER for its output.

Verdict standard. The route is a real departure, but the paper compares it with no alternative; HMM-based synthesis appears only as a preliminary study (§5.3). The closest prior already couples a phoneme decision to a database search: restricting the search to the categorized phoneme was preferred for 84% of stimuli by ten listeners [[3]](#ref-3). The target decides per phone sequence, so each recognition error selects a wrong diphone (§5.3). The group's [later] GMM and HMM mappings were not consistently intelligible either [[11]](#ref-11).

### M12 Evaluation: listener test on oracle phones

**Usual approach:** Listener transcription of synthesized speech was not yet practice: apart from the target, the 30 confirmed studies in the published table date from 2014 on (Appendix). Seven listeners transcribe 20 sentences here (§5.3).

**State of the art:** Open listener transcription gives a median 43.75% WER for an intracortical voice neuroprosthesis, in 2025 [[12]](#ref-12) [later]; the group's [later] ultrasound-and-video conversion reached 60% word accuracy [[13]](#ref-13).

Verdict standard: unusual for its time, but with correct phone labels (§5.3) it measures unit selection and HNM, not the interface.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Read CMU-Arctic sentences, two speakers | Read sentences | – | standard |
| M02 Training-only supervision | 41 audio-aligned phone labels | Paired audio labels | – | standard |
| M03 Training and adaptation | Speaker-dependent training, no adaptation | Speaker-dependent training | – | standard |
| M04 Use-time action | Uttered (vocalized) read speech | Overt speech | – | standard |
| M05 Sensors | Ultrasound plus two lip cameras, 29.97 Hz, PCA | Ultrasound and lip video | – | standard |
| M06 Processing and decoding | Context-independent HMM-GMM, three dictionary levels | HMM recognizer (pattern match 10) | 6.17% WER, SSC benchmark, 5k bigram [[7]](#ref-7) | standard |
| M07 Lexicon and LM | Corpus dictionaries; pitch template | Lexicon constraint | – | standard |
| M08 Output | Diphone unit selection, HNM | Direct mapping (pattern match 2) | 15.93% ASR WER, TaL1 single speaker [[10]](#ref-10) | standard |
| M09 Confirmation | Offline | None | – | not applicable |
| M10 Correction | Offline | None | – | not applicable |
| M11 Reference construction | Parallel audio and its forced alignment | Parallel audio | – | standard |
| M12 Evaluation | Within-speaker jackknife; 7 listeners, oracle phones | No listener test before 2014 | 43.75% median listener WER, intracortical [[12]](#ref-12) | standard |
| M13 Device and cost | Laboratory head-and-transducer support | Laboratory | – | standard |

## Where the claims outrun the evidence

- "Reasonably intelligible" output (§5.3) holds only "when the phonetic prediction is correct"; no aggregate synthesized-speech accuracy is given, only listener bars against a 97% ceiling (Fig. 10), and the test speaker is not named.
- The hybrid scheme is said not to limit "the available vocabulary" (§4.2), yet its dictionaries come from the CMU-Arctic sentences that supply all test lists (§4.1), so every test word is covered (inference).
- Speaker A's word-based visual accuracy is 66% in §5.3 but 67.6% in Table 1.
- The two speakers are no clean replication: B's transducer shifted after 240 sentences (§2), the authors focus on A (§4.2), and B is 10.7 points lower in phone-based decoding (Table 1) (inference).
- Two of 26 jackknife experiments tune Gaussian counts and penalties (§4.1), and PCA is fitted on a frame subset (§3); neither is stated to exclude test lists.

## What the field needs next

- M08: compare unit selection with direct mapping on the same data, scored by listener transcription of output from recognized phones.
- M06: use the context-dependent multi-stream decoder [[2]](#ref-2) in the pipeline, with training-only dictionaries.
- M04: test on silent articulation, which the authors name as necessary (Introduction).
- M12: hold out a session or speaker (§2).

## Questions for the authors

- Which speaker supplied the 20 synthesis sentences, and what was their mean word accuracy?
- Were the PCA bases and the two validation experiments kept apart from the test lists?
- How were the cost weights chosen?

## Appendix: literature search

- M06, articulatory-signal-speech-recognizer. Inclusion rule: studies that recognize phones, words or sentences as text from non-acoustic speech-production signals measured on the speaker (ultrasound, EMG, EMA/PMA, EPG, radar, neural), classified by recognizer family by full-text pattern; acoustic test input, lip-video-only lipreading, perception studies and reviews excluded; versions once; earlier versions of the target system merged with it. Ledger counts: slot-filled 7,345 unique studies; pattern match 118 unique studies (all years: neural network 81, HMM 60, SVM 36, DTW 15). At the target's time: 11 prior unique studies, HMM 10 (pattern match), dictionary or language model 5; 4 [concurrent]. Read in full: [[5]](#ref-5), [[6]](#ref-6), [[2]](#ref-2), [[7]](#ref-7). Known-item recall 0.5 (6 seeds, ledger pattern); the dated population was enumerated from the modality field.
- M08, non-acoustic-signal-to-speech-output-route. Inclusion rule: studies that produce audible speech from non-acoustic speech-production signals measured on the speaker, classified as recognition then synthesis or direct mapping; face animation, inversion, model-driven articulatory synthesis, acoustic input and reviews excluded; versions once; earlier versions of the target system merged with it. Ledger counts: slot-filled 3,268 unique studies; pattern match 144 unique studies (all years: direct mapping 60, recognition then synthesis 22). At the target's time: 2 prior unique studies, direct mapping 2, recognition then synthesis 0; 1 [concurrent] study (three folders plus one conference report). Read in full: [[3]](#ref-3), [[4]](#ref-4), [[8]](#ref-8), [[11]](#ref-11), [[10]](#ref-10). Known-item recall 0.17 (6 seeds, ledger pattern); the dated population was enumerated from the modality field.
- M12, listener-intelligibility-test (published table, reused). Inclusion rule: studies that evaluate speech synthesized from non-acoustic signals with listeners transcribing or identifying words or sentences. Ledger counts: slot-filled 6,960 unique studies; pattern match 37 unique studies; confirmed 30 unique studies including the target, added here; 0 confirmed before the target's time, earliest other study 2014. Usual design over all years: crowd workers, 15 (pattern match). Read in full: [[13]](#ref-13), [[12]](#ref-12). Known-item recall 1.0 (2 seeds).

## References

Numbered by first citation. BibTeX in the same order and keys: [development-of-a-silent-speech-interface-driven-by-ultrasound-and-optical-images-of-the-tongue-and-l.bib](development-of-a-silent-speech-interface-driven-by-ultrasound-and-optical-images-of-the-tongue-and-l.bib).

1. <a id="ref-1"></a>Hueber, T., Benaroya, E., Chollet, G., Denby, B., Dreyfus, G., Stone, M. “Development of a Silent Speech Interface Driven by Ultrasound and Optical Images of the Tongue and Lips.” *Speech Communication*, 2010, 52(4), 288. doi:[10.1016/j.specom.2009.11.004](https://doi.org/10.1016/j.specom.2009.11.004). Target. Read as the accepted manuscript. [wiki: doi-10.1016-j.specom.2009.11.004](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1016-j.specom.2009.11.004/article.md)
2. <a id="ref-2"></a>Hueber, T., Benaroya, E., Chollet, G., Denby, B., Dreyfus, G., Stone, M. “Visuo-Phonetic Decoding using Multi-Stream and Context-Dependent Models for an Ultrasound-based Silent Speech Interface.” *Proc. Interspeech 2009*, 2009. doi:[10.21437/Interspeech.2009-226](https://doi.org/10.21437/Interspeech.2009-226). Concurrent; same group and databases. [concurrent] [wiki: isca-hueber09_cdms](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-hueber09_cdms/article.md) [wiki: isca-hueber09_mshmm](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-hueber09_mshmm/article.md) [wiki: isca-hueber09-visuophon](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-hueber09-visuophon/article.md)
3. <a id="ref-3"></a>Kaburagi, T., Honda, M. “Determination of the vocal tract spectrum from the articulatory movements based on the search of an articulatory-acoustic database.” *Proc. ICSLP 1998*, 1998. doi:[10.21437/ICSLP.1998-357](https://doi.org/10.21437/ICSLP.1998-357). Prior; deciding prior for M08. [wiki: isca-kaburagi98_icslp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-kaburagi98_icslp/article.md)
4. <a id="ref-4"></a>Engwall, O. “Articulatory synthesis using corpus-based estimation of line spectrum pairs.” *Proc. Interspeech 2005*, 2005. doi:[10.21437/Interspeech.2005-599](https://doi.org/10.21437/Interspeech.2005-599). Prior; deciding prior for M08. [wiki: isca-engwall05_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-engwall05_interspeech/article.md)
5. <a id="ref-5"></a>Jou, S., Schultz, T., Walliczek, M., Kraft, F., Waibel, A. “Towards Continuous Speech Recognition Using Surface Electromyography.” *Interspeech 2006 - ICSLP*, 2006. doi:[10.21437/Interspeech.2006-212](https://doi.org/10.21437/Interspeech.2006-212). Prior; read (M06 HMM recognizer). [wiki: isca-jou06_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-jou06_interspeech/article.md)
6. <a id="ref-6"></a>Schultz, T., Wand, M. “Modeling Coarticulation in EMG-based Continuous Speech Recognition.” *Speech Communication*, 2010, 52(4), 341. doi:[10.1016/j.specom.2009.12.002](https://doi.org/10.1016/j.specom.2009.12.002). Concurrent; read (M06). [concurrent] [wiki: doi-10.1016-j.specom.2009.12.002](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1016-j.specom.2009.12.002/article.md)
7. <a id="ref-7"></a>Li, B., Xu, K., Feng, D., Mi, H., Wang, H., Zhu, J. “Denoising Convolutional Autoencoder Based B-mode Ultrasound Tongue Image Feature Extraction.” *Proc. IEEE ICASSP 2019*, 2019, 7130-7134. doi:[10.1109/ICASSP.2019.8682806](https://doi.org/10.1109/ICASSP.2019.8682806). arXiv:[1903.00888](https://arxiv.org/abs/1903.00888). Later; state of the art for M06. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/denoising-convolutional-autoencoder-based-b-mode-ultrasound-tongue-image-feature-extraction) [wiki: arxiv-1903.00888](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1903.00888/article.md)
8. <a id="ref-8"></a>Guenther, F. H., Brumberg, J. S., Wright, E. J., Nieto-Castanon, A., Tourville, J. A., Panko, M., et al. “A Wireless Brain-Machine Interface for Real-Time Speech Synthesis.” *PLoS ONE*, 2009, 4(12), e8218. doi:[10.1371/journal.pone.0008218](https://doi.org/10.1371/journal.pone.0008218). Concurrent; direct neural-to-formant mapping. [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-wireless-brain-machine-interface-for-real-time-speech-synthesis) [wiki: pmc-2784218-wireless](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wireless/article.md) [wiki: pmc-2784218-wirelesssynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wirelesssynth/article.md) [wiki: doi-10.1371-journal.pone.0008218](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1371-journal.pone.0008218/article.md)
9. <a id="ref-9"></a>Hueber, T., Chollet, G., Denby, B., Dreyfus, G., Stone, M. “Towards a Segmental Vocoder Driven by Ultrasound and Optical Images of the Tongue and Lips.” *Proc. Interspeech 2008*, 2008. doi:[10.21437/Interspeech.2008-527](https://doi.org/10.21437/Interspeech.2008-527). Earlier conference version of the target system; merged with the target in all counts. [wiki: isca-hueber08_segvocoder](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-hueber08_segvocoder/article.md)
10. <a id="ref-10"></a>Sonkar, Y., Kilaru, Y., Yelimeli, S., Shah, N., Gandhi, V. “Tongue2Speech: Real-Time Speech Synthesis from Tongue Ultrasound Videos via Spatiotemporal Transformers.” *Proc. Interspeech 2026*, 2026, 6856-6860. doi:[10.21437/Interspeech.2026-3023](https://doi.org/10.21437/Interspeech.2026-3023). Later; state of the art for M08. [later] [wiki: isca-sonkar26_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-sonkar26_interspeech/article.md)
11. <a id="ref-11"></a>Hueber, T., Benaroya, E., Denby, B., Chollet, G. “Statistical Mapping between Articulatory and Acoustic Data for an Ultrasound-based Silent Speech Interface.” *Proc. Interspeech 2011*, 2011. doi:[10.21437/Interspeech.2011-239](https://doi.org/10.21437/Interspeech.2011-239). Later; same group, GMM and HMM mapping. [later] [wiki: isca-hueber11-usmapping](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-hueber11-usmapping/article.md) [wiki: doi-10.21437-interspeech.2011-239](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.21437-interspeech.2011-239/article.md)
12. <a id="ref-12"></a>Wairagkar, M., Card, N. S., Singer-Clark, T., Hou, X., Iacobacci, C., Miller, L. M., et al. “An instantaneous voice-synthesis neuroprosthesis.” *Nature*, 2025. doi:[10.1038/s41586-025-09127-3](https://doi.org/10.1038/s41586-025-09127-3). Later; state of the art for M12 (listener open transcription). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/an-instantaneous-voice-synthesis-neuroprosthesis) [wiki: doi-10.1038-s41586-025-09127-3](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-025-09127-3/article.md) [wiki: doi-10.1101-2024.08.14.607690](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2024.08.14.607690/article.md) [wiki: pmc-12369848-voicesynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12369848-voicesynth/article.md) [wiki: pmc-12369848-voice-synth-np](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12369848-voice-synth-np/article.md) [wiki: pmc-11370360-instvoice](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11370360-instvoice/article.md)
13. <a id="ref-13"></a>Hueber, T., Bailly, G. “Statistical Conversion of Silent Articulation into Audible Speech using Full-Covariance HMM.” *Computer Speech & Language*, 2016, 36, 274-293. doi:[10.1016/j.csl.2015.09.008](https://doi.org/10.1016/j.csl.2015.09.008). Later; full-pipeline listener test. [later] [wiki: doi-10.1016-j.csl.2015.09.008](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1016-j.csl.2015.09.008/article.md)
