# Non-Audible Murmur (NAM) Recognition

Yoshitaka Nakajima, Hideki Kashioka, Nick Campbell, Kiyohiro Shikano. IEICE Transactions on Information and Systems E89-D(1), 2006; English version of IEICE Trans. D-II J87-D-II(9), 2004. [doi:10.1093/ietisy/e89-d.1.1](https://doi.org/10.1093/ietisy/e89-d.1.1)

## Verdict

The paper [[1]](#ref-1) changes the sensor (M05), the speaking mode (M04) and the model transfer (M03); all three are standard, being the design of the group's 2003 reports [[2]](#ref-2), [[3]](#ref-3). Rows A–C of Table 1 equal the 2003 table to rounding, although the described training set grew from 2,100 files to about 4,610 utterances (inference). Whispered 20,000-word Japanese dictation with the same decoder existed in 2002 [[4]](#ref-4). The main overreach is noise robustness: no noise level and no air-microphone baseline, while a close-talking microphone kept 91.7–91.9% for audible speech in the group's [concurrent] TV and music conditions [[5]](#ref-5) and [later] live noise at 60 dBA cut NAM accuracy to 53.3% [[6]](#ref-6). What stands is a one-speaker, speaker-dependent 93.3% in quiet, which the best later result on the task, 93.9%, has barely moved (Appendix) [[6]](#ref-6).

## Against the field, component by component

### M05 Sensors: body site of the conducted microphone

**Usual approach:** both prior body-conducted recognizers are the group's own, with this stethoscopic microphone below the mastoid (2 of 2, pattern match, Appendix) [[2]](#ref-2), [[7]](#ref-7); [concurrent] work outside the group uses a throat microphone on the neck [[8]](#ref-8), [[9]](#ref-9), still the most common site over all years (41 of 82 unique studies, slot-filled). The target departs from the throat microphone, not from the 2003 design.

**State of the art:** 93.9% word accuracy with a silicone NAM microphone against 88.9% with the stethoscopic one, one speaker, 20K-word dictation, 2007 [[6]](#ref-6); the target is 0.6 points lower on a different test set (inference).

The site was chosen by listening and spectra (§3.3, Fig. 6); no recognition rate is reported for any other site or sensor. Verdict standard, with no repetition beyond one speaker.

### M04 Use-time action: unvoiced speaking mode

**Usual approach:** 3 of 4 prior unvoiced-speech recognizers run large-vocabulary dictation (pattern match, Appendix): whisper through an air microphone, 74% on 4 speakers, speaker-independent, 20,000 words [[4]](#ref-4), and the group's two NAM studies; the fourth recognizes 5 mimed vowels from EMG [[10]](#ref-10). Murmur departs from whisper by suppressing the audible source; the authors concede the boundary is vague (§3.1).

**State of the art:** murmur dictation at 93.9%, speaker-dependent, 2007 [[6]](#ref-6).

The 19.3-point gap between NAM (93.3%) and whisper (74%) (inference) sets one speaker-dependent speaker against four speaker-independent ones; it says nothing about speaking mode. Verdict standard.

### M03 Training: transfer from normal-speech models

**Usual approach:** 2 of 3 prior studies re-estimate or adapt a normal-speech HMM with target-mode data (pattern match, Appendix): retraining with 2,100 files [[2]](#ref-2) and iterative MLLR with 350 utterances, 88.62% on 72 NAM test utterances [[7]](#ref-7); the third trains a whisper model from scratch after the unadapted normal model gave 27% [[4]](#ref-4). The paper keeps retraining and names MLLR as an alternative it does not run (§3.5).

**State of the art:** iterative MLLR from 350 utterances reaches 93.9%, 2007 [[6]](#ref-6).

Under the same three 2003 conditions, retraining gave a 90.83% mean [[2]](#ref-2) against 88.62% for MLLR [[7]](#ref-7): 6 times the data for 2.21 points (inference), with different initial models. No unadapted baseline is given. Verdict standard.

### M12 Evaluation: noise test

**Usual approach:** both prior studies expose the sensor to noise physically, as here (2 of 2; 44 of 123 unique studies over all years, pattern match, Appendix), and neither states a level or an air-microphone baseline; [concurrent] work records both microphones in played noise [[9]](#ref-9) or adds a close-talking baseline [[5]](#ref-5).

**State of the art:** whispered-phrase WER mostly below 10% with noise calibrated to 80 dB(A) at the ear, one speaker, 2025 [later] [[11]](#ref-11).

Under TV news, Table 1 falls from 93.3% to 89.2%, 62% more errors (inference); a close-talking microphone with audible speech fell from 94.4% to 91.7% in the group's TV-news condition, 48% more errors (inference) [[5]](#ref-5). The NAM degradation is no smaller. Verdict standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | One male speaker, read sentences in NAM | Read sentences, one speaker | – | standard |
| M02 Training-only supervision | Transcripts, no segment times | Transcript labels | – | standard |
| M03 Training and adaptation | Normal-speech HMM retrained with NAM | Normal-speech HMM retrained or adapted (pattern match 2) | 93.9%, MLLR from 350 utterances [[6]](#ref-6) | standard |
| M04 Use-time action | Non-audible murmur | Unvoiced dictation (whisper, murmur) (pattern match 3) | 93.9%, SD 20K murmur dictation [[6]](#ref-6) | standard |
| M05 Sensors | Stethoscopic microphone below the mastoid | Group's 2003 NAM microphone (pattern match 2) | 93.9%, silicone NAM microphone [[6]](#ref-6) | standard |
| M06 Processing and decoding | Monophone HMM, Julius | HMM recognizer | – | standard |
| M07 Lexicon and LM | Toolkit 20K vocabulary and LM | Toolkit LM | – | standard |
| M08 Output | Text | Text | – | standard |
| M09 Confirmation | Offline | None | – | not applicable |
| M10 Correction | Offline | None | – | not applicable |
| M11 Reference construction | Read sentence text | Prompt text | – | standard |
| M12 Evaluation | 4 rooms, one speaker, no level, no air baseline | Noise physically present (pattern match 2) | WER mostly <10% at 80 dB(A) [[11]](#ref-11) | standard |
| M13 Device and cost | Hand-made skin microphone | Skin-contact microphone | – | standard |

## Where the claims outrun the evidence

- Robustness (§3.6, §4). The authors concede that raised gain, incomplete soundproofing and body-transmitted noise let noise in (§3.6), and B–D are described only qualitatively (Table 1). With noise played at 60 dBA during murmuring, the group's later system fell from 83.7% to 53.3%, averaged over four noises [[6]](#ref-6).
- Results versus training data. Rows A–C match the ICASSP 2003 rows (93.33, 90.00, 89.17) [[2]](#ref-2), whose model used only the ATR files, yet §3.5 adds 1,255 JNAS sentences.
- Test independence. Test and training text are both Mainichi sentences, with no disjointness stated (§3.5–3.6); the test speaker is the training speaker [[2]](#ref-2).
- Small test: 24 sentences per room, sentence error 50.0% in quiet (Table 1).

## What the field needs next

- M12: NAM and close-talking microphones recorded together at calibrated 50–80 dBA.
- M04: the same speakers reading the same sentences in whisper and murmur through one sensor.
- M03: unadapted, MLLR and retraining curves against data amount, on disjoint text and several speakers.
- M05: recognition rates for mastoid, neck and bone-conduction sites, same speakers.

## Questions for the authors

- Which model produced rows A–C: the 2003 model or the one with JNAS added?
- Are the 24 test sentences absent from the JNAS training text?
- What were the sound pressure levels in B–D?
- What does the unadapted normal-speech model score?

## Appendix: literature search

Setting: recognizers of whisper, murmur or mimed speech from any signal, and of speech from skin-, bone- or tissue-conducted sensors. Acoustic whisper, throat-microphone and bone-conduction recognition are inside; non-acoustic silent-speech recognizers enter M04 only. Prior = first public before 2004-03 (target first public 2004-09, Japanese version); [concurrent] = 2004-03 to 2005-03. The ICASSP and Eurospeech 2003 reports are one study.

- M05 body-conducted-sensor-speech-recognition. Inclusion rule: recognizers whose test input is a skin-, bone- or tissue-conducted sensor, any speaking mode; design = body site. Ledger: slot-filled 7,329; pattern match 82 unique studies; body_sites neck 41, ear 18, face 16 (slot-filled). Dated: prior 2 (both the group's microphone below the mastoid); [concurrent] 4 (throat microphone 2, NAM microphone 2). Read: [[2]](#ref-2), [[3]](#ref-3), [[7]](#ref-7), [[6]](#ref-6). Known-item recall 1.0.
- M04 unvoiced-speech-recognition. Inclusion rule: recognizers of whisper, murmur or mimed speech from any signal; design = speaking mode and task scale. Ledger: slot-filled 5,595; pattern match 506 unique studies; silent_articulation 154 of 351 labelled (slot-filled). Dated: prior 4 (whisper dictation 1, murmur dictation 2, EMG vowels 1). Read: [[4]](#ref-4), [[10]](#ref-10). Known-item recall 1.0.
- M03 normal-speech-model-transfer-to-unvoiced-or-body-conducted-input. Inclusion rule: recognizers for whispered, murmured or body-conducted speech that retrain, adapt or train from scratch; design = transfer method and data amount. Ledger: slot-filled 1,526; pattern match 155 unique studies (fine-tuning 86, retraining 81, MLLR 36, SAT 17, MAP 10; a study can match several). Dated: prior 3 (retraining 1, MLLR 1, from scratch 1). Read: [[7]](#ref-7), [[4]](#ref-4), [[8]](#ref-8). Known-item recall 0.83.
- M12 body-conducted-sensor-noise-test-protocol (published table, appended). Inclusion rule: conducted-sensor studies; design = noise physically present or added digitally. Ledger: slot-filled 6,960; pattern match 123 unique studies; physically present 44, digital 15. Dated: prior 2, both physical noise without level or air baseline. Read: [[9]](#ref-9), [[5]](#ref-5), [[11]](#ref-11). Known-item recall 0.75.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Nakajima, Y., Kashioka, H., Campbell, N., Shikano, K. “Non-Audible Murmur (NAM) Recognition.” *IEICE Transactions on Information and Systems*, 2006, E89-D(1), 1-8. doi:[10.1093/ietisy/e89-d.1.1](https://doi.org/10.1093/ietisy/e89-d.1.1). Target. English version (2004 IEICE Excellent Paper Award special section) of IEICE Trans. D-II J87-D-II(9):1757-1764, Sept. 2004, whose Table 1 is identical; both versions merged. [wiki: doi-10.1093-ietisy-e89-d.1.1](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1093-ietisy-e89-d.1.1/article.md) [wiki: ieice-e89d-nakajima-nam-2006](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/ieice-e89d-nakajima-nam-2006/article.md) [wiki: ieice2004-nakajima-nam-recognition](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/ieice2004-nakajima-nam-recognition/article.md)
2. <a id="ref-2"></a>Nakajima, Y., Kashioka, H., Shikano, K., Campbell, N. “Non-Audible Murmur Recognition Input Interface Using Stethoscopic Microphone Attached to the Skin.” *Proc. IEEE ICASSP 2003*, 2003, 708-711. doi:[10.1109/ICASSP.2003.1200069](https://doi.org/10.1109/ICASSP.2003.1200069). Same-group prior; one study with the Eurospeech 2003 report. [wiki: doi-10.1109-icassp.2003.1200069](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-icassp.2003.1200069/article.md)
3. <a id="ref-3"></a>Nakajima, Y., Kashioka, H., Shikano, K., Campbell, N. “Non-Audible Murmur Recognition.” *Proc. Eurospeech 2003*, 2003, 2601-2604. doi:[10.21437/Eurospeech.2003-717](https://doi.org/10.21437/Eurospeech.2003-717). Same-group prior; reports the ICASSP 2003 experiment. [wiki: isca-nakajima03_eurospeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-nakajima03_eurospeech/article.md)
4. <a id="ref-4"></a>Tatara, K., Ito, T., Zolfaghari, P., Takeda, K., Itakura, F. “Experiments on Recognition of Lavalier Microphone Speech and Whispered Speech in Real World Environments.” *Proc. ICSLP 2002*, 2002. doi:[10.21437/ICSLP.2002-215](https://doi.org/10.21437/ICSLP.2002-215). Prior; whispered-speech 20K dictation. [wiki: isca-tatara02_icslp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-tatara02_icslp/article.md)
5. <a id="ref-5"></a>Heracleous, P., Nakajima, Y., Lee, A., Saruwatari, H., Shikano, K. “Audible (Normal) Speech and Inaudible Murmur Recognition Using NAM Microphone.” *Proc. EUSIPCO 2004*, 2004. <https://naist.repo.nii.ac.jp/records/4544> Same group; close-talking versus NAM microphone. [concurrent] [wiki: naist-4544](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/naist-4544/article.md)
6. <a id="ref-6"></a>Heracleous, P., Kaino, T., Saruwatari, H., Shikano, K. “Unvoiced Speech Recognition Using Tissue-Conductive Acoustic Sensor.” *EURASIP Journal on Advances in Signal Processing*, 2007, 94068. doi:[10.1155/2007/94068](https://doi.org/10.1155/2007/94068). Same group; state of the art for M03, M04 and M05. [later] [wiki: eurasip2007-heracleous-tissue-conductive](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/eurasip2007-heracleous-tissue-conductive/article.md) [wiki: doi-10.1155-2007-94068](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1155-2007-94068/article.md)
7. <a id="ref-7"></a>Heracleous, P., Nakajima, Y., Lee, A., Saruwatari, H., Shikano, K. “Accurate Hidden Markov Models for Non-Audible Murmur (NAM) Recognition Based on Iterative Supervised Adaptation.” *Proc. IEEE ASRU 2003*, 2003, 73-76. <https://naist.repo.nii.ac.jp/record/4483/files/ASRU_2003_73.pdf> Same-group prior; cited by the target. [wiki: asru2003-heracleous-iterative-mllr-nam](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/asru2003-heracleous-iterative-mllr-nam/article.md)
8. <a id="ref-8"></a>Jou, S., Schultz, T., Waibel, A. “Adaptation for Soft Whisper Recognition Using a Throat Microphone.” *Proc. INTERSPEECH 2004 - ICSLP*, 2004. doi:[10.21437/Interspeech.2004-565](https://doi.org/10.21437/Interspeech.2004-565). Throat-microphone soft whisper with adaptation. [concurrent] [wiki: isca-jou04_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-jou04_interspeech/article.md)
9. <a id="ref-9"></a>Graciarena, M., Franco, H., Myers, G., Cowan, C., Cesari, F., Abrash, V. “Combination of Standard and Throat Microphones for Robust Speech Recognition in Highly Noisy Environments.” *Proc. INTERSPEECH 2004 - ICSLP*, 2004. doi:[10.21437/Interspeech.2004-302](https://doi.org/10.21437/Interspeech.2004-302). Throat plus standard microphone in noise. [concurrent] [wiki: isca-graciarena04_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-graciarena04_interspeech/article.md)
10. <a id="ref-10"></a>Manabe, H., Hiraiwa, A., Sugimura, T. “Speech Recognition Using EMG; Mime Speech Recognition.” *Proc. Eurospeech 2003*, 2003. doi:[10.21437/Eurospeech.2003-524](https://doi.org/10.21437/Eurospeech.2003-524). Prior; EMG mime vowels. [wiki: isca-manabe03_eurospeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-manabe03_eurospeech/article.md)
11. <a id="ref-11"></a>Fukumoto, M. “Whisphone: Whispering Input Earbuds.” *arXiv preprint*, 2025. doi:[10.48550/arXiv.2501.01636](https://doi.org/10.48550/arXiv.2501.01636). arXiv:[2501.01636](https://arxiv.org/abs/2501.01636). State of the art for the M12 noise test. [later] [wiki: arxiv-2501.01636](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2501.01636/article.md)
