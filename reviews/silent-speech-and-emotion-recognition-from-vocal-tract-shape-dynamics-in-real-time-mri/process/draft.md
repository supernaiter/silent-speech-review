# Silent Speech and Emotion Recognition from Vocal Tract Shape Dynamics in Real-Time MRI

Pandey, L., Arif, A. S. · SIGGRAPH 2021 (arXiv preprint) · 2021 · [arXiv:2106.08706](https://arxiv.org/abs/2106.08706)

## Verdict

The paper moves the LipNet decoder onto real-time MRI (M06) and makes sentence text the output of a vocal-tract MRI decoder (M08) [[1]](#ref-1). Both are standard: the decoder is the field's most common articulator-video design [[2]](#ref-2), and the text output, unique among 88 vocal-tract MRI studies (Appendix), follows HMM sequence recognition of continuous rtMRI speech [[3]](#ref-3) and rests on one held-out split. The evaluation (M12) is behind the best comparable work, which repeated splits or folds [[3]](#ref-3), [[4]](#ref-4), [[5]](#ref-5). The strongest confound: every USC-TIMIT speaker reads the same 460 sentences [[6]](#ref-6), so the 40.6% PER most likely measures speaker transfer on a closed list (inference). The title overreaches: the speech is audible (§4.1), and nothing recognizes emotion (§6).

## Against the field, component by component

### M06 Decoder: LipNet on rtMRI

**Usual approach:** Of 1,342 articulator-video decoding studies (pattern match, published table, Appendix), 380 use a 3D convolution front end with a recurrent or temporal back end. The paper uses exactly this, three STCNN layers, two Bi-GRUs and CTC (Fig. 1), from LipNet [[2]](#ref-2); only the input, midsagittal rtMRI at 23.18 frames per second (§4.1), is new.

**State of the art:** Tongue2Speech (2026, [later]) keeps the 3D front end with a Transformer, 15.93% WER on one TaL1 speaker [[7]](#ref-7); on rtMRI, Otani et al. (2026) use EfficientNetV2 frames and an E-Branchformer [[8]](#ref-8).

The "first end-to-end sentence-level" claim (§1) repeats LipNet's own wording [[2]](#ref-2). Saha et al. had chosen a frame-wise ResNet-50 with an LSTM for rtMRI, judging 3D temporal pooling too weak for clips of about 3 seconds [[9]](#ref-9); the paper feeds 75-frame windows of about 3 seconds to a 3D front end (§4.2) with no comparison. Verdict: standard.

### M08 Output: sentence text from vocal-tract MRI

**Usual approach:** Of 75 vocal-tract MRI studies with an output recorded, 16 give a descriptive report (slot-filled); of 88, 21 name class recognition and 18 speech synthesis, and only this paper emits text (pattern match, Appendix).

**State of the art:** No [later] MRI study in the ledger outputs text (Appendix); synthesis replaced it, best speaker-independent at 8.2% to 23.5% dWER over four unseen speakers, against ASR of the original speech (2026) [[8]](#ref-8).

The "first study" claim (Abstract) omits Katsamanis et al., who recognized sequences of 30 articulation classes in 460 TIMIT utterances of one speaker at 49.4% accuracy over 10 random 95/5 splits [[3]](#ref-3). The step to words is new but rests on one split, two pooled speakers and no repeats (§4.1–4.2), short of the ahead rule. Verdict: standard.

### M12 Evaluation: split, repeats and comparison

**Usual approach:** Of 88 vocal-tract MRI studies, 11 name repeated splits or cross-validation, 10 unseen test speakers and 3 sentence-disjoint tests (pattern match, upper bounds, Appendix). The paper holds out two speakers once, with no repeat, seed or interval (§4.1, §5.2).

**State of the art:** Otani et al. (2026) hold out 4 speakers (43/4/4 split) and report each, 8.2% to 23.5% dWER, read speech 4.5% to 11.1% [[8]](#ref-8).

Earlier MRI decoders repeated: 10 random splits [[3]](#ref-3), 9-fold cross-validation [[4]](#ref-4), leave-one-subject-out repeated ten times [[5]](#ref-5). On the same corpus Csapó held out 10 test sentences per speaker [[6]](#ref-6); the paper's 3,680 videos from eight speakers and 920 from two are 460 per speaker (inference), the full shared list. Table 2 ranks sentence PER against error converted from accuracy of a VCV classifier on another corpus [[9]](#ref-9) and a phoneme classifier; the caption concedes the tasks differ, yet the Abstract calls 40.6% "much better". Verdict: behind the best comparable work [[3]](#ref-3), on repetition.

### M05 Emotion geometry (incidental)

**Usual approach:** Of 88 vocal-tract MRI studies, 14 name emotional speech and 4 compare boundary geometry with a neutral reference (pattern match, Appendix); the NEDM follows Kim et al. (2014) (§6).

**State of the art:** No [later] ledger study (Appendix); the prior is Lee et al. (2006): one speaker, five productions of "doctor" per emotion, called preliminary [[10]](#ref-10).

With ten speakers but two words, averages only (Table 3) and no test, the gender claim rests on gaps such as 1.00 against 0.91 (lower boundary, angry, velar, "clock"). Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | USC-TIMIT read speech | Recorded speech (slot-filled 3,882) | – | standard |
| M02 Training-only supervision | CTC on transcripts | Transcripts (slot-filled 31) | – | standard |
| M03 Training and adaptation | Tuning split not named | Training records (slot-filled 1,526) | – | not reported |
| M04 Use-time action | Audible speech | Silent or overt (slot-filled 5,595) | – | standard |
| M05 Sensors | rtMRI 23.18 fps; NEDM | Emotional speech named (pattern match 14) | [[10]](#ref-10) (2006): 1 speaker | standard |
| M06 Processing and decoding | STCNN, Bi-GRU, CTC | 3D conv front end (pattern match 380) | [[7]](#ref-7) (2026): WER 15.93% | standard |
| M07 Lexicon and LM | Character LM, beam 4 | LM in beam search (slot-filled 119) | – | standard |
| M08 Output | Sentence text | Descriptive report (slot-filled 16) | [[8]](#ref-8) (2026): dWER 8.2-23.5% | standard |
| M09 Confirmation | Offline | Offline (slot-filled 82) | – | not applicable |
| M10 Correction | Offline | Offline (slot-filled 82) | – | not applicable |
| M11 Reference construction | Word transcripts | Corpus references (slot-filled 234) | – | standard |
| M12 Evaluation | One speaker split | Repeated splits (pattern match 11) | [[8]](#ref-8) (2026): per-speaker dWER | behind |
| M13 Device and cost | MRI scanner | Laboratory (slot-filled 6,075) | – | standard |

## Where the claims outrun the evidence

- "Silent speech" and "emotion recognition" (title): the speech is audible, with synchronized audio (§4.1), and no emotion classifier exists (§6).
- The character LM's training text is not stated (§3.2); with a closed sentence list, test text may leak through it (inference).
- PER is reported apart from CER (§5.2), though the model emits 28 characters (Table 1) with no grapheme-to-phoneme step; Fig. 3 labels letters as phonemes.
- The LM is a "5-gram" and also a recurrent network of 4 layers of 1,024 LSTM cells (§3.2); §4.2 copies LipNet [[2]](#ref-2).
- §2 says Saha et al. used the same dataset; they used the Vocal Tract Morphology MRI database [[9]](#ref-9).

## What the field needs next

- M12: a USC-TIMIT split disjoint in speakers and sentences, repeated over folds or seeds, with per-speaker errors.
- M08: direct CTC text decoding against ASR on rtMRI-synthesized speech on one split [[8]](#ref-8).
- M04: silent or mouthed articulation recorded in the scanner.

## Questions for the authors

- Which speakers were tested, and did their sentences occur in training?
- On which text was the LM trained, and was it n-gram or LSTM?
- Were references cut with clips at 75 frames?
- Which data selected the hyperparameters?

## Appendix: literature search

- M06, articulator-video-spatiotemporal-front-end (published table, reused). Inclusion rule: studies that decode text, speech or acoustic features from video of the articulators (lip or face camera, ultrasound) with a trained network, classified by how temporal context enters the image front end; hand-crafted features, audio-only models and reviews count only as pattern matches; versions count once. Ledger: 7,345 unique studies slot-filled for M06; 1,342 unique studies pattern match. Usual design: 3D convolution front end 380; CNN followed by a recurrent layer 255; temporal convolution network 146 (pattern match, published counts). Read in full: [[2]](#ref-2), [[9]](#ref-9), [[8]](#ref-8); the published table also read [[7]](#ref-7). Known-item recall 1.0 (published).
- M08, rtmri-decoder-output (new). Inclusion rule: vocal-tract MRI studies (88 unique ledger studies naming rtMRI, real-time or dynamic MRI, MRI-TIMIT, USC-TIMIT or the Vocal Tract Morphology MRI database), classified by output: descriptive analysis, intermediate signal, class label or class sequence, synthesized speech, or text scored by WER, CER or PER; speech scored by ASR counts as speech; versions count once. Ledger: 3,268 unique studies slot-filled for M08; 88 unique studies pattern match. Usual design: descriptive report 16 of 75 slot-filled; class recognition 21, speech synthesis 18, WER or CER named 9, of which only the target outputs text (pattern match). Read in full: [[3]](#ref-3), [[9]](#ref-9), [[8]](#ref-8). Known-item recall 0.83 (6 seeds).
- M12, rtmri-decoding-test-split (new). Inclusion rule: the same 88 studies, counting the test protocols a trained decoder or classifier names: unseen test speakers, sentence-disjoint material, repeated splits, folds or seeds; a study counts under every protocol its full text names (upper bound). Ledger: 6,960 unique studies slot-filled for M12; 88 unique studies pattern match. Repeated splits or cross-validation 11; unseen test speakers 10; sentence-disjoint 3 (pattern match). Read in full: [[3]](#ref-3), [[4]](#ref-4), [[5]](#ref-5), [[6]](#ref-6), [[8]](#ref-8). Known-item recall 1.0 (6 seeds).
- M05, emotion-related-vocal-tract-shape-deviation (new). Inclusion rule: the same 88 studies, counting full texts naming emotional speech and those comparing boundary distances, apertures or constrictions with a neutral reference; related-work mentions match (upper bound). Ledger: 7,329 unique studies slot-filled for M05; 88 unique studies pattern match. Emotional speech 14; neutral-referenced geometry 4 (pattern match). Read in full: [[10]](#ref-10), outside the ledger pattern. Known-item recall 0.5 (2 seeds).

## References

Numbered by first citation. BibTeX in the same order and keys: [silent-speech-and-emotion-recognition-from-vocal-tract-shape-dynamics-in-real-time-mri.bib](silent-speech-and-emotion-recognition-from-vocal-tract-shape-dynamics-in-real-time-mri.bib).

1. <a id="ref-1"></a>Pandey, L., Arif, A. S. “Silent Speech and Emotion Recognition from Vocal Tract Shape Dynamics in Real-Time MRI.” *SIGGRAPH 2021 (arXiv preprint)*, 2021. arXiv:[2106.08706](https://arxiv.org/abs/2106.08706). Target. Read as arXiv v1. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/silent-speech-and-emotion-recognition-from-vocal-tract-shape-dynamics-in-real-time-mri) [wiki: arxiv-2106.08706](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2106.08706/article.md)
2. <a id="ref-2"></a>Assael, Y. M., Shillingford, B., Whiteson, S., de Freitas, N. “LipNet: End-to-End Sentence-level Lipreading.” *arXiv preprint*, 2016. arXiv:[1611.01599](https://arxiv.org/abs/1611.01599). Prior; architecture and LM lineage (M06, M07). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/lipnet-end-to-end-sentence-level-lipreading) [wiki: arxiv-1611.01599](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-1611.01599/article.md)
3. <a id="ref-3"></a>Katsamanis, A., Bresch, E., Ramanarayanan, V., Narayanan, S. “Validating rt-MRI based articulatory representations via articulatory recognition.” *Proc. Interspeech 2011*, 2011, 2841-2844. doi:[10.21437/Interspeech.2011-711](https://doi.org/10.21437/Interspeech.2011-711). Prior; deciding prior for M08 and M12. [wiki: isca-katsamanis11_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-katsamanis11_interspeech/article.md)
4. <a id="ref-4"></a>Prasad, A., Ghosh, P. K., Narayanan, S. S. “Selection of optimal vocal tract regions using real-time magnetic resonance imaging for robust voice activity detection.” *Proc. Interspeech 2014*, 2014. doi:[10.21437/Interspeech.2014-368](https://doi.org/10.21437/Interspeech.2014-368). Prior; repeated folds (M12). [wiki: isca-prasad14_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-prasad14_interspeech/article.md)
5. <a id="ref-5"></a>van Leeuwen, K. G., Bos, P., Trebeschi, S., van Alphen, M. J. A., Voskuilen, L., Smeele, L. E., et al. “CNN-based phoneme classifier from vocal tract MRI learns embedding consistent with articulatory topology.” *Proc. Interspeech 2019*, 2019, 909-913. doi:[10.21437/Interspeech.2019-1173](https://doi.org/10.21437/Interspeech.2019-1173). Prior; repeated leave-one-subject-out (M12). [wiki: isca-leeuwen19_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-leeuwen19_interspeech/article.md)
6. <a id="ref-6"></a>Csapó, T. G. “Speaker dependent articulatory-to-acoustic mapping using real-time MRI of the vocal tract.” *Proc. Interspeech 2020*, 2020. doi:[10.21437/Interspeech.2020-15](https://doi.org/10.21437/Interspeech.2020-15). arXiv:[2008.00889](https://arxiv.org/abs/2008.00889). Prior; USC-TIMIT sentence list and sentence-disjoint split (M12). [wiki: isca-csapo20_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-csapo20_interspeech/article.md) [wiki: arxiv-2008.00889](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2008.00889/article.md)
7. <a id="ref-7"></a>Sonkar, Y., Kilaru, Y., Yelimeli, S., Shah, N., Gandhi, V. “Tongue2Speech: Real-Time Speech Synthesis from Tongue Ultrasound Videos via Spatiotemporal Transformers.” *Proc. Interspeech 2026*, 2026. doi:[10.21437/Interspeech.2026-3023](https://doi.org/10.21437/Interspeech.2026-3023). Later; state of the art of the published M06 table. [later] [wiki: isca-sonkar26_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-sonkar26_interspeech/article.md)
8. <a id="ref-8"></a>Otani, Y., Sawada, S., Ohmura, H., Katsurada, K. “Speaker-Independent Speech Synthesis from Real-time MRI Articulatory Data.” *Proc. Interspeech 2026*, 2026. doi:[10.21437/Interspeech.2026-3379](https://doi.org/10.21437/Interspeech.2026-3379). Later; state of the art for M06, M08 and M12 on rtMRI. [later] [wiki: isca-otani26_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-otani26_interspeech/article.md)
9. <a id="ref-9"></a>Saha, P., Srungarapu, P., Fels, S. “Towards Automatic Speech Identification from Vocal Tract Shape Dynamics in Real-time MRI.” *Proc. Interspeech 2018*, 2018, 1249-1253. doi:[10.21437/Interspeech.2018-2537](https://doi.org/10.21437/Interspeech.2018-2537). Prior; deciding prior for M06 and M08. [wiki: isca-saha18_rtmrivcv](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-saha18_rtmrivcv/article.md) [wiki: isca-saha18-vtmri](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-saha18-vtmri/article.md)
10. <a id="ref-10"></a>Lee, S., Bresch, E., Adams, J., Kazemzadeh, A., Narayanan, S. “A Study of Emotional Speech Articulation using a Fast Magnetic Resonance Imaging Technique.” *Proc. Interspeech 2006 - ICSLP*, 2006, 2234-2237. doi:[10.21437/Interspeech.2006-320](https://doi.org/10.21437/Interspeech.2006-320). Prior; deciding prior for M05. [wiki: isca-lee06d_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-lee06d_interspeech/article.md)
