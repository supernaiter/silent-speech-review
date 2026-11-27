# Non-Audible Murmur (NAM) Recognition

Yoshitaka Nakajima, Hideki Kashioka, Nick Campbell, Kiyohiro Shikano. IEICE Transactions on Information and Systems E89-D(1), 2006; English version of IEICE Trans. D-II J87-D-II(9), 2004. [doi:10.1093/ietisy/e89-d.1.1](https://doi.org/10.1093/ietisy/e89-d.1.1)

## Verdict

The paper [[1]](#ref-1) changes the sensor (M05), the speaking mode (M04) and the model transfer (M03); the design is the authors' own from their 2003 reports [[2]](#ref-2), [[3]](#ref-3), and before 2004-03 no independent group had used a NAM microphone or recognized murmur (Appendix). All three are standard because one speaker, tested speaker-dependently, gives no repetition. Rows A–C of Table 1 equal the 2003 table to rounding although the described training set grew from 2,100 files to about 4,610 utterances (inference). The noise-robustness claim lacks noise levels and a same-session air-microphone baseline; with noise played live at 60 dBA, a [later] same-group test fell from 83.7% to 53.3% (silicone microphone, one female speaker, 100 adaptation utterances) [[4]](#ref-4). The 93.3% in quiet is close to the best NAM dictation result among the audited studies, 93.9%, first reported in 2005 (Appendix) [[5]](#ref-5).

## Against the field, component by component

### M05 Sensors: body site of the conducted microphone

**Usual approach:** there was none at the time: 2 of 4 prior conducted-sensor recognizers are the group's microphone below the mastoid [[2]](#ref-2), [[6]](#ref-6), while independent groups paired a throat microphone [[7]](#ref-7) or an in-ear earplug [[8]](#ref-8) with a standard microphone in noise (pattern match, Appendix). Outside NAM work, 13 of 19 studies with a recorded site use the neck (slot-filled, Appendix).

**State of the art:** 93.9% word accuracy, speaker-dependent 20K dictation, silicone NAM microphone, one male speaker, 48 test utterances, 2005 [[5]](#ref-5); the stethoscopic microphone gave 88.9% in the 2007 repeat [[4]](#ref-4).

The authors state that other sites gave no numerically evaluable rate and that bone-conduction earphones gave too low an S/N (§3.3, Fig. 6); no recognition comparison across sites is reported. Verdict standard.

### M04 Use-time action: unvoiced speaking mode

**Usual approach:** of 5 prior unvoiced-speech recognizers (pattern match, Appendix), 3 are verified large-vocabulary dictation: whisper through an air microphone, 74% recognition rate on 4 test speakers, 20,000 words [[9]](#ref-9), and the group's two NAM studies; the others are an earlier whisper recognizer [[10]](#ref-10) and 5 mimed vowels from EMG [[11]](#ref-11). The authors concede the NAM–whisper boundary is vague (§3.1).

**State of the art:** murmur dictation at 93.9%, speaker-dependent, 2005 [[5]](#ref-5).

The 19.3-point gap to whisper (inference) sets one speaker-dependent speaker against four test speakers and an undefined rate. Verdict standard.

### M03 Training: transfer from normal-speech models

**Usual approach:** 2 of 3 classified prior studies adapt a normal-speech HMM (pattern match, Appendix): retraining with 2,100 files [[2]](#ref-2) and iterative MLLR [[6]](#ref-6); a third trains a whisper model from scratch after the unadapted normal model gave 27% [[9]](#ref-9). The paper names MLLR as an alternative it does not run, and concedes that NAM-specific models cost data (§3.5).

**State of the art:** iterative MLLR from 350 utterances, 93.9%, 2005 [[5]](#ref-5).

On the same 72 utterances the unadapted normal-speech model scored -0.81% [[6]](#ref-6). Retraining monophones with 2,100 files gave 90.83% [[2]](#ref-2) against 71.09% for monophone MLLR with 200 utterances and 88.62% for tied-mixture MLLR with 350 [[6]](#ref-6): retraining wins only against the same model type. Verdict standard.

### M12 Evaluation: noise test

**Usual approach:** the group's two prior studies play noise live without a level or an air baseline [[2]](#ref-2), [[6]](#ref-6); Graciarena 2003 compared against a standard microphone in tank noise [[12]](#ref-12) (Appendix; mention counts over all years: physically present 44 of 123).

**State of the art:** whispered-phrase WER mostly below 10% with noise calibrated to 80 dB(A) at the ear; 15 fixed phrases, off-the-shelf recognizers, one speaker, ANC earbud, 2025 [later] [[13]](#ref-13).

In the group's [concurrent] test with audible speech, the NAM microphone went from 93.8% to 93.2% and 92.9% under TV news and music, the close-talking microphone from 94.4% to 91.7% and 91.9% [[14]](#ref-14). That supports the sensor, not murmur: the target's own murmur rows fall from 93.3% to 89.2% (TV news) with no level and no air channel. Verdict standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | One male speaker, read sentences in NAM | Read sentences, one speaker | – | standard |
| M02 Training-only supervision | Transcripts, no segment times | Transcript labels | – | standard |
| M03 Training and adaptation | Normal-speech HMM retrained with NAM | Normal-speech HMM retrained or adapted (pattern match 2) | 93.9%, MLLR from 350 utterances, 2005 [[5]](#ref-5) | standard |
| M04 Use-time action | Non-audible murmur | Unvoiced dictation (whisper, murmur) (pattern match 3) | 93.9%, SD 20K murmur dictation, 2005 [[5]](#ref-5) | standard |
| M05 Sensors | Stethoscopic microphone below the mastoid | Group's NAM microphone (authors only) (pattern match 2) | 93.9%, silicone NAM microphone, 2005 [[5]](#ref-5) | standard |
| M06 Processing and decoding | Monophone HMM, Julius | HMM recognizer | – | standard |
| M07 Lexicon and LM | Toolkit 20K vocabulary and LM | Toolkit LM | – | standard |
| M08 Output | Text | Text | – | standard |
| M09 Confirmation | Offline | None | – | not applicable |
| M10 Correction | Offline | None | – | not applicable |
| M11 Reference construction | Read sentence text | Prompt text | – | standard |
| M12 Evaluation | 4 rooms, one speaker, no level, no air baseline | Noise physically present (pattern match 3) | WER mostly <10% at 80 dB(A), 15 fixed whispered phrases [[13]](#ref-13) | standard |
| M13 Device and cost | Hand-made skin microphone | Skin-contact microphone | – | standard |

## Where the claims outrun the evidence

- Robustness (§3.6, §4). The authors concede that gain, soundproofing and body-transmitted noise let noise in (§3.6); B–D are described only in words (§3.6). Superimposed noise left accuracy almost at clean levels [[4]](#ref-4), but live noise did not, which the group's [later] SPECOM paper attributes to the Lombard reflex [[15]](#ref-15).
- Results versus training data. Rows A–C match ICASSP 2003 (93.33, 90.00, 89.17) [[2]](#ref-2), whose model used only the ATR files, yet §3.5 adds 1,255 JNAS sentences.
- Test independence. ICASSP 2003 calls the test open, newly recorded by the training speaker [[2]](#ref-2); if rows A–C use that model, overlap with the Mainichi training text (§3.5–3.6) can affect only row D.
- Small test: 24 sentences per room, sentence error 50.0% in quiet (Table 1).

## What the field needs next

- M12: NAM and close-talking microphones recorded together at calibrated 50–80 dBA, murmur and audible speech.
- M04: the same speakers reading the same sentences in whisper and murmur through one sensor.
- M03: retraining and MLLR curves, same model type, several speakers.

## Questions for the authors

- Which model produced rows A–C: the 2003 model or the one with JNAS added?
- Are the 24 test sentences absent from the JNAS training text?
- What were the sound pressure levels in B–D?

## Appendix: literature search

Setting: recognizers of whisper, murmur or mimed speech from any signal, and of speech from skin-, bone- or tissue-conducted sensors. Acoustic whisper, throat-microphone, earplug and bone-conduction recognition are inside; non-acoustic silent-speech recognizers enter M04 only. Prior = first public before 2004-03 (target first public 2004-09, Japanese version; the design was first public in 2003-04 [[2]](#ref-2), and the target is dated as the journal paper); [concurrent] = 2004-03 to 2005-03. The ICASSP and Eurospeech 2003 reports are one study. Works without a wiki page are described through their citations: [[7]](#ref-7) in [[12]](#ref-12) and [[15]](#ref-15); [[8]](#ref-8) in [[15]](#ref-15); [[10]](#ref-10) in [[9]](#ref-9). Zheng et al. ASRU 2003 (air- and bone-conductive microphones, detection and enhancement) has no recognizer and is excluded.

- M05 body-conducted-sensor-speech-recognition. Inclusion rule: recognizers whose test input is a skin-, bone- or tissue-conducted sensor, any speaking mode; design = body site. Ledger: slot-filled 7,329; pattern match 82 unique studies, 38 NAM-related; of the other 44, 19 record a site, 13 the neck (slot-filled). Dated: prior 4 (group's NAM microphone 2, throat 1, earplug 1); [concurrent] 4. Read: [[2]](#ref-2), [[3]](#ref-3), [[6]](#ref-6), [[5]](#ref-5), [[15]](#ref-15). Known-item recall 1.0.
- M04 unvoiced-speech-recognition. Inclusion rule: recognizers of whisper, murmur or mimed speech from any signal; design = speaking mode and task scale. Ledger: slot-filled 5,595; pattern match 506 unique studies. Dated: prior 5 (whisper 2, murmur 2, EMG vowels 1). Read: [[9]](#ref-9), [[11]](#ref-11). Known-item recall 1.0.
- M03 normal-speech-model-transfer-to-unvoiced-or-body-conducted-input. Inclusion rule: recognizers for whispered, murmured or body-conducted speech that retrain, adapt or train from scratch; design = transfer method and data amount. Ledger: slot-filled 1,526; pattern match 155 unique studies (mention counts: fine-tuning 86, retraining 81, MLLR 36, SAT 17, MAP 10). Dated: prior 3 classified (retraining 1, MLLR 1, from scratch 1); [[10]](#ref-10) unclassified. Read: [[6]](#ref-6), [[9]](#ref-9); [concurrent] [[16]](#ref-16). Known-item recall 0.83.
- M12 body-conducted-sensor-noise-test-protocol (published table, appended). Inclusion rule: conducted-sensor studies; design = noise physically present or added digitally. Ledger: slot-filled 6,960; pattern match 123 unique studies; mention counts: physically present 44, digital 15. Dated: prior 4. Read: [[12]](#ref-12), [[14]](#ref-14), [[4]](#ref-4), [[13]](#ref-13). Known-item recall 0.75.

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Nakajima, Y., Kashioka, H., Campbell, N., Shikano, K. “Non-Audible Murmur (NAM) Recognition.” *IEICE Transactions on Information and Systems*, 2006, E89-D(1), 1-8. doi:[10.1093/ietisy/e89-d.1.1](https://doi.org/10.1093/ietisy/e89-d.1.1). Target. English version (2004 IEICE Excellent Paper Award special section) of IEICE Trans. D-II J87-D-II(9):1757-1764, Sept. 2004, whose Table 1 is identical; both versions merged. [wiki: doi-10.1093-ietisy-e89-d.1.1](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1093-ietisy-e89-d.1.1/article.md) [wiki: ieice-e89d-nakajima-nam-2006](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/ieice-e89d-nakajima-nam-2006/article.md) [wiki: ieice2004-nakajima-nam-recognition](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/ieice2004-nakajima-nam-recognition/article.md)
2. <a id="ref-2"></a>Nakajima, Y., Kashioka, H., Shikano, K., Campbell, N. “Non-Audible Murmur Recognition Input Interface Using Stethoscopic Microphone Attached to the Skin.” *Proc. IEEE ICASSP 2003*, 2003, 708-711. doi:[10.1109/ICASSP.2003.1200069](https://doi.org/10.1109/ICASSP.2003.1200069). Same-group prior; one study with the Eurospeech 2003 report. [wiki: doi-10.1109-icassp.2003.1200069](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-icassp.2003.1200069/article.md)
3. <a id="ref-3"></a>Nakajima, Y., Kashioka, H., Shikano, K., Campbell, N. “Non-Audible Murmur Recognition.” *Proc. Eurospeech 2003*, 2003, 2601-2604. doi:[10.21437/Eurospeech.2003-717](https://doi.org/10.21437/Eurospeech.2003-717). Same-group prior; reports the ICASSP 2003 experiment. [wiki: isca-nakajima03_eurospeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-nakajima03_eurospeech/article.md)
4. <a id="ref-4"></a>Heracleous, P., Kaino, T., Saruwatari, H., Shikano, K. “Unvoiced Speech Recognition Using Tissue-Conductive Acoustic Sensor.” *EURASIP Journal on Advances in Signal Processing*, 2007, 94068. doi:[10.1155/2007/94068](https://doi.org/10.1155/2007/94068). Same group; live-noise test. [later] [wiki: eurasip2007-heracleous-tissue-conductive](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/eurasip2007-heracleous-tissue-conductive/article.md) [wiki: doi-10.1155-2007-94068](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1155-2007-94068/article.md)
5. <a id="ref-5"></a>Heracleous, P., Nakajima, Y., Saruwatari, H., Shikano, K. “A Tissue-Conductive Acoustic Sensor Applied in Speech Recognition for Privacy.” *Proc. Joint sOc-EUSAI Conference 2005*, 2005. <https://naist.repo.nii.ac.jp/records/4824> Same group; first report of 93.9%; state of the art for M03, M04 and M05. [later] [wiki: naist-4824](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/naist-4824/article.md)
6. <a id="ref-6"></a>Heracleous, P., Nakajima, Y., Lee, A., Saruwatari, H., Shikano, K. “Accurate Hidden Markov Models for Non-Audible Murmur (NAM) Recognition Based on Iterative Supervised Adaptation.” *Proc. IEEE ASRU 2003*, 2003, 73-76. <https://naist.repo.nii.ac.jp/record/4483/files/ASRU_2003_73.pdf> Same-group prior; cited by the target. [wiki: asru2003-heracleous-iterative-mllr-nam](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/asru2003-heracleous-iterative-mllr-nam/article.md)
7. <a id="ref-7"></a>Graciarena, M., Franco, H., Sonmez, K., Bratt, H. “Combining Standard and Throat Microphones for Robust Speech Recognition.” *IEEE Signal Processing Letters*, 2003, 10(3), 72-74. doi:[10.1109/LSP.2003.808549](https://doi.org/10.1109/LSP.2003.808549). Prior; described through its citation in [[12]](#ref-12) and SPECOM 2005.
8. <a id="ref-8"></a>Strand, O. M., Holter, T., Egeberg, A., Stensby, S. “On the Feasibility of ASR in Extreme Noise Using the PARAT Earplug Communication Terminal.” *Proc. IEEE ASRU 2003*, 2003, 315-320. doi:[10.1109/ASRU.2003.1318460](https://doi.org/10.1109/ASRU.2003.1318460). Prior; described through its citation in SPECOM 2005.
9. <a id="ref-9"></a>Tatara, K., Ito, T., Zolfaghari, P., Takeda, K., Itakura, F. “Experiments on Recognition of Lavalier Microphone Speech and Whispered Speech in Real World Environments.” *Proc. ICSLP 2002*, 2002. doi:[10.21437/ICSLP.2002-215](https://doi.org/10.21437/ICSLP.2002-215). Prior; whispered-speech 20K dictation. [wiki: isca-tatara02_icslp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-tatara02_icslp/article.md)
10. <a id="ref-10"></a>Itoh, T., Takeda, K., Itakura, F. “Acoustic Analysis and Recognition of Whispered Speech.” *Proc. IEEE ASRU 2001*, 2001, 429-432. doi:[10.1109/ASRU.2001.1034676](https://doi.org/10.1109/ASRU.2001.1034676). Prior; described through its citation in [[9]](#ref-9).
11. <a id="ref-11"></a>Manabe, H., Hiraiwa, A., Sugimura, T. “Speech Recognition Using EMG; Mime Speech Recognition.” *Proc. Eurospeech 2003*, 2003. doi:[10.21437/Eurospeech.2003-524](https://doi.org/10.21437/Eurospeech.2003-524). Prior; EMG mime vowels. [wiki: isca-manabe03_eurospeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-manabe03_eurospeech/article.md)
12. <a id="ref-12"></a>Graciarena, M., Franco, H., Myers, G., Cowan, C., Cesari, F., Abrash, V. “Combination of Standard and Throat Microphones for Robust Speech Recognition in Highly Noisy Environments.” *Proc. INTERSPEECH 2004 - ICSLP*, 2004. doi:[10.21437/Interspeech.2004-302](https://doi.org/10.21437/Interspeech.2004-302). Throat plus standard microphone in noise. [concurrent] [wiki: isca-graciarena04_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-graciarena04_interspeech/article.md)
13. <a id="ref-13"></a>Fukumoto, M. “Whisphone: Whispering Input Earbuds.” *arXiv preprint*, 2025. doi:[10.48550/arXiv.2501.01636](https://doi.org/10.48550/arXiv.2501.01636). arXiv:[2501.01636](https://arxiv.org/abs/2501.01636). State of the art for the M12 noise test. [later] [wiki: arxiv-2501.01636](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2501.01636/article.md)
14. <a id="ref-14"></a>Heracleous, P., Nakajima, Y., Lee, A., Saruwatari, H., Shikano, K. “Audible (Normal) Speech and Inaudible Murmur Recognition Using NAM Microphone.” *Proc. EUSIPCO 2004*, 2004. <https://naist.repo.nii.ac.jp/records/4544> Same group; close-talking versus NAM microphone. [concurrent] [wiki: naist-4544](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/naist-4544/article.md)
15. <a id="ref-15"></a>Heracleous, P., Nakajima, Y., Shikano, K. “Tissue-Conductive Unvoiced Speech Recognition in Clean and Noisy Environments.” *Proc. SPECOM 2005*, 2005. <https://naist.repo.nii.ac.jp/records/4825> Same group; Lombard attribution; cites the 2003 throat-microphone and earplug recognizers. [later] [wiki: naist-4825](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/naist-4825/article.md) [wiki: naist-specom2005-nam](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/naist-specom2005-nam/article.md) [wiki: oa-W2281035153](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/oa-W2281035153/article.md)
16. <a id="ref-16"></a>Jou, S., Schultz, T., Waibel, A. “Adaptation for Soft Whisper Recognition Using a Throat Microphone.” *Proc. INTERSPEECH 2004 - ICSLP*, 2004. doi:[10.21437/Interspeech.2004-565](https://doi.org/10.21437/Interspeech.2004-565). Throat-microphone soft whisper with adaptation. [concurrent] [wiki: isca-jou04_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-jou04_interspeech/article.md)
