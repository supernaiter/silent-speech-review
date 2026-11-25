# LipNet: End-to-End Sentence-level Lipreading

Assael, Y. M., Shillingford, B., Whiteson, S., de Freitas, N. · arXiv preprint · 2016 · [arXiv:1611.01599](https://arxiv.org/abs/1611.01599)

## Verdict

LipNet [[1]](#ref-1) changes one component, the decoder (M06): spatiotemporal convolutions, Bi-GRUs and a character CTC loss in one model. That is ahead: of the 67 earlier sentence-level studies 41 name hidden Markov models and none a CTC or attention decoder (Appendix); the field took both, and the best GRID result today still uses a 3D front end [[2]](#ref-2). The headline comparisons do not hold: the 86.4% "state-of-the-art" is a video-only accuracy from speaker-dependent word HMMs with the full GRID grammar [[3]](#ref-3), so the 2.8× claim crosses task level, split and decoder constraint, and the "experienced human lipreaders" are three hearing-impaired students given ten minutes of annotated video (§4.2). Silent dictation is the named application (§5) although every utterance is overtly spoken, a transfer cost measured in lip video since 2010 [[4]](#ref-4), so M04 is behind; and no Table 2 number carries a seed or an interval, while the study reimplemented as its LSTM baseline reports both [[5]](#ref-5).

## Against the field, component by component

### M06 Decoding: spatiotemporal convolution and a character CTC loss

**Usual approach:** Of 633 sentence-level lip-reading studies (pattern match, Appendix) 291 name an attention decoder and 288 CTC; among the 67 earlier ones 41 name HMMs and none CTC, which no study first public before 2016-05 uses at all.

**State of the art:** visual-only LRS3 WER 17.6% with hybrid CTC/attention over subword units, and 0.99% WER on GRID against 4.8% here overlapped (2026, [later]) [[6]](#ref-6), [[2]](#ref-2).

The comparators classify words: Wand et al. cut single words from the GRID alignments [[5]](#ref-5), and the only [concurrent] study with a spatiotemporal front end classifies 500 clips and concludes "the 2D convolutions are superior to their 3D counterparts" [[7]](#ref-7). The 3D choice ran against that evidence and the gain sits there: 2D convolutions instead of the STCNN cost 11.6% against 4.8% WER overlapped and 26.7% against 11.4% unseen (Table 2); the character 5-gram is worth about 1.2× (§4.3). That CTC was the decisive half is not shown: a [concurrent] attention model reached 3.0% GRID WER under this protocol without it [[8]](#ref-8). Verdict: ahead, on one corpus and one run.

### M04 Use-time action: overt speech standing in for silent dictation

**Usual approach:** Of 33 overt-to-silent studies (pattern match) 23 apply an overt-trained decoder to silent articulation and report the degradation (confirmed, Appendix), four before this paper; GRID is overtly spoken throughout (§2).

**State of the art:** in lip video a normal-speech-trained recogniser falls from 69.7% to 61.2% on silently articulated phrases, where a silent-trained model reaches 64.4% (2018, [later]) [[9]](#ref-9).

Florescu et al. showed in 2010, with lip video and ultrasound, that "vocalized training data cannot be used directly to train the silent speech recognition system" [[4]](#ref-4). This paper names silent dictation as the use that demands video only (§5) and offers nothing on that transfer. Verdict: behind, against the four earlier studies built to measure this gap.

### M12 Evaluation: the GRID protocol it created and its human panel

**Usual approach:** Of 93 GRID lip-reading studies 54 name an unseen-speaker and 41 an overlapped-speaker split (pattern match, Appendix), the protocol defined here and already followed by a [concurrent] paper [[8]](#ref-8); of 62 machine-against-human studies 40 use hearing-impaired panels and 6 professionals.

**State of the art:** professional readers at 92.9% WER without context and 86.4% with it on open-vocabulary clips, against 40.9% for the model, with bootstrap intervals (2018, [later]) [[10]](#ref-10).

The protocol is the paper's second lasting contribution; the reporting is weak. The study reimplemented as Baseline-LSTM gives 79.6% ± 4.3% across speakers and a one-tailed t-test [[5]](#ref-5); Table 2 gives single numbers and the 255-utterance draw no seed or item list (§4.1). The panel is three hearing-impaired students who labelled 300 clips after ten minutes of annotated video (§4.2), against a professional of ten years' experience [[8]](#ref-8). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training action | Overt GRID sentences | Overt speech (slot-filled 4,015) | – | standard |
| M02 Supervision | Transcripts; augmentation | Transcript labels (slot-filled 31) | – | standard |
| M03 Training/adaptation | Scratch; word-first curriculum | Supervised (slot-filled 3,216) | – | standard |
| M04 Use-time action | Overt speech video | Overt-trained, silent tested (pattern match 33) | [[9]](#ref-9) 61.2% | behind |
| M05 Sensors | RGB camera, mouth crop | Mouth crop (slot-filled 8,898) | – | standard |
| M06 Decoding | STCNN, Bi-GRU, character CTC | HMM in 2016; CTC today (pattern match 633) | [[2]](#ref-2) 0.99% GRID | ahead |
| M07 Lexicon/LM | Character 5-gram | Grammar or lexicon (pattern match 633) | – | standard |
| M08 Output | Character transcript | Text (slot-filled 3,760) | – | standard |
| M09 Confirmation | None | Mostly absent (slot-filled 82) | – | not applicable |
| M10 Correction | None | Mostly absent (slot-filled 82) | – | not applicable |
| M11 Reference | GRID transcripts; two splits | Benchmark splits (slot-filled 239) | – | standard |
| M12 Evaluation | WER/CER; human panel | Unseen-speaker split (pattern match 93) | [[10]](#ref-10) 40.9% vs 92.9% | standard |
| M13 Device/cost | Offline; no device | Offline benchmark (slot-filled 6,721) | – | standard |

## Where the claims outrun the evidence

- The Table 1 caption says the [concurrent] GRID system "consider[s] only the simpler case of predicting isolated words", but its composite HMM decodes the whole six-slot sentence [[3]](#ref-3).
- Three ratios stand for two experiments: 2.8× on the overlapped split (§5), 4.1× against humans on the unseen split (§4.3), 1.69× in accuracies (§1).
- The panel was told to pick the most probable answer (§4.2), making it a grammar-prior baseline; no chance or grammar-only baseline is reported for the 64,000 admissible sentences.
- Generalisation rests on 4 held-out speakers of 34 (§4.1).

## What the field needs next

- M06 and M12: a GRID ablation holding data and front end fixed, swapping only CTC for attention over several seeds on a fixed test list, to separate what this paper and [[8]](#ref-8) conflate and make the 54 unseen-speaker and 41 overlapped-speaker studies comparable.
- M04: this architecture trained on vocalised GRID and tested on silent articulation by the same speakers [[9]](#ref-9).

## Questions for the authors

- Which seed and which 255 sentences per speaker define the overlapped split, and what is the spread across runs?
- Was a validation partition held out for checkpoint and hyperparameter selection?
- Do the Table 2 baselines share LipNet's beam width, language model and augmentation?

## Appendix: literature search

- M06, sentence-lipreading-sequence-objective (new). Inclusion rule: studies that decode sentence-level or open-vocabulary speech from lip or face video (ledger names lip reading, VSR, AVSR or an LRS2/LRS3 benchmark together with sentence-level, continuous or open-vocabulary recognition), classified by the sequence objective their full text names; isolated-word classification without a sentence-level result is excluded, audio-only ASR is out of scope, reviews count as pattern matches, every named objective counts (upper bound), versions count once. Ledger: 7,345 unique studies slot-filled for M06; 633 unique studies pattern match. Designs: attention or sequence-to-sequence 291, CTC 288, HMM 196, hybrid CTC/attention 134, transducer 118 (pattern match). Before 2016-11: 67 unique studies, HMM 41, CTC 0, attention 0; wiki-wide, 0 of the 2,048 studies with text first public before 2016-05 uses a CTC decoder in visual or biosignal speech. Front-end counts from the published table components/M06/articulator-video-spatiotemporal-front-end.json: 3D convolution 380 of 1,342 studies today (pattern match), and 4 pattern hits among the 378 studies dated 2016-11 or earlier, 3 of them the C3D motion-capture file format in speech-animation papers, leaving only [[7]](#ref-7) [concurrent]. Read in full: [[5]](#ref-5), [[7]](#ref-7), [[3]](#ref-3), [[8]](#ref-8), [[6]](#ref-6). Known-item recall 1.0.
- M07, use-time-language-model-visual-speech (new). Inclusion rule: the same 633 studies, classified by the use-time language information their full text names (character or word n-gram, neural language model or LLM rescoring, explicit absence of an external model), with grammar, lexicon and dictionary constraints counted separately for the earlier period; M07 is slot-filled for about 1% of the wiki, so every count is pattern match and an upper bound. Ledger: 119 unique studies slot-filled for M07; 633 unique studies pattern match. Designs: neural language model or LLM rescoring 143, n-gram 28, no external model 21. Before 2016-11: 67 unique studies, grammar or lexicon 29, n-gram 1, no external model 1. Read in full: [[3]](#ref-3), [[10]](#ref-10), [[6]](#ref-6). Known-item recall 1.0.
- M04, overt-to-silent-transfer (published table, reused). Inclusion rule: studies that apply a decoder trained only on overt or attempted overt speech to silent, mouthed or imagined speech and report the result, any signal; studies that also train on silent data count when they report an overt-training-only condition; alignment-only use and perception-to-imagery transfer are excluded; versions count once. Ledger: 5,595 unique studies slot-filled for M04; 33 unique studies pattern match, 23 confirmed. Usual design: overt-trained decoder applied to silent speech and reported as a degradation, 23 studies (confirmed). Earlier than 2016-11: [[4]](#ref-4) (2010, lip video and ultrasound), two EMG studies (2010, 2011) and one ECoG study (2014). Read in full: [[4]](#ref-4), [[9]](#ref-9). Known-item recall 1.0.
- M12, grid-sentence-lipreading-protocol (new). Inclusion rule: lip-reading or VSR studies whose ledger names optical-camera input and the GRID corpus, classified by the evaluation partition their full text names (unseen-speaker, overlapped-speaker, explicit reuse of speakers 1, 2, 20 and 22), with a separate count of studies reporting a standard deviation, an interval or a significance test; audio-only GRID work and GRID studies without a decoder are excluded; versions count once. Ledger: 6,960 unique studies slot-filled for M12; 93 unique studies pattern match. Designs: unseen-speaker split 54, overlapped-speaker split 41, variability or significance reporting 26, explicit reuse of the four held-out speakers 3 (pattern match). Before 2016-11: 12 unique studies, unseen-speaker 5, overlapped-speaker 6, variability or significance 3 unique studies of which 2 are decoder studies. Read in full: [[5]](#ref-5), [[3]](#ref-3), [[8]](#ref-8), [[2]](#ref-2). Known-item recall 1.0.
- M12, human-lipreader-baseline (published table, reused). Inclusion rule: studies that put machine lipreading or silent speech recognition and human lipreaders on the same metric over the same data; listener tests of reconstructed speech, literature-only human figures and human-only lipreading studies are excluded; versions count once. Ledger: 6,960 unique studies slot-filled for M12; 64 unique studies pattern match, 7 confirmed. Panels: hearing-impaired or deaf participants 40, untrained or lay participants 12, professional or expert readers 6 of 62 studies (pattern match); two confirmed studies are earlier than this paper. Read in full: [[8]](#ref-8), [[10]](#ref-10). Known-item recall 0.8.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Assael, Y. M., Shillingford, B., Whiteson, S., de Freitas, N. “LipNet: End-to-End Sentence-level Lipreading.” *arXiv preprint*, 2016. arXiv:[1611.01599](https://arxiv.org/abs/1611.01599). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lipnet-end-to-end-sentence-level-lipreading) [wiki: arxiv-1611.01599](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1611.01599/article.md)
2. <a id="ref-2"></a>Xue, F., Zhu, B., Jia, W., Li, S., Li, Y., Zhang, J., et al. “LinProVSR: Linguistics-Knowledge Guided Progressive Disambiguation Network for Visual Speech Recognition.” *AAAI*, 2026. doi:[10.1609/aaai.v40i14.38133](https://doi.org/10.1609/aaai.v40i14.38133). [later] [wiki: aaai-38133-linprovsr](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/aaai-38133-linprovsr/article.md)
3. <a id="ref-3"></a>Gergen, S., Zeiler, S., Hussen Abdelaziz, A., Nickel, R., Kolossa, D. “Dynamic Stream Weighting for Turbo-Decoding-Based Audiovisual ASR.” *Interspeech*, 2016. doi:[10.21437/Interspeech.2016-166](https://doi.org/10.21437/Interspeech.2016-166). [concurrent] [wiki: isca-gergen16-streamw](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-gergen16-streamw/article.md)
4. <a id="ref-4"></a>Florescu, V., Crevier-Buchman, L., Denby, B., Hueber, T., Pillot-Loiseau, C., Roussel, P., et al. “Silent vs Vocalized Articulation for a Portable Ultrasound-Based Silent Speech Interface.” *Interspeech*, 2010. <https://www.isca-archive.org/interspeech_2010/florescu10_interspeech.html> [wiki: isca-florescu10](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-florescu10/article.md)
5. <a id="ref-5"></a>Wand, M., Koutnik, J., Schmidhuber, J. “Lipreading with Long Short-Term Memory.” *ICASSP*, 2016. arXiv:[1601.08188](https://arxiv.org/abs/1601.08188). [wiki: arxiv-1601.08188](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1601.08188/article.md)
6. <a id="ref-6"></a>Haliassos, A., Mira, R., Petridis, S. “Pay Attention to CTC: Fast and Robust Pseudo-Labelling for Unified Speech Recognition.” *ICLR*, 2026. arXiv:[2602.19316](https://arxiv.org/abs/2602.19316). [later] [wiki: arxiv-2602.19316](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2602.19316/article.md)
7. <a id="ref-7"></a>Chung, J. S., Zisserman, A. “Lip Reading in the Wild.” *ACCV*, 2016. doi:[10.1007/978-3-319-54427-4_7](https://doi.org/10.1007/978-3-319-54427-4_7). [concurrent] [wiki: w2594690981-lrw](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/w2594690981-lrw/article.md)
8. <a id="ref-8"></a>Chung, J. S., Senior, A., Vinyals, O., Zisserman, A. “Lip Reading Sentences in the Wild.” *CVPR*, 2017. arXiv:[1611.05358](https://arxiv.org/abs/1611.05358). [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lip-reading-sentences-in-the-wild) [wiki: arxiv-1611.05358](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1611.05358/article.md)
9. <a id="ref-9"></a>Petridis, S., Shen, J., Cetin, D., Pantic, M. “Visual-Only Recognition of Normal, Whispered and Silent Speech.” *ICASSP*, 2018. arXiv:[1802.06399](https://arxiv.org/abs/1802.06399). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/visual-only-recognition-of-normal-whispered-and-silent-speech) [wiki: arxiv-1802.06399](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1802.06399/article.md)
10. <a id="ref-10"></a>Shillingford, B., Assael, Y., Hoffman, M. W., Paine, T., Hughes, C., Prabhu, U., et al. “Large-Scale Visual Speech Recognition.” *arXiv preprint*, 2018. arXiv:[1807.05162](https://arxiv.org/abs/1807.05162). [later] [wiki: arxiv-1807.05162](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1807.05162/article.md)
