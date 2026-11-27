# EMG-to-Speech: Direct Generation of Speech from Facial Electromyographic Signals

Matthias Janke, Lorenz Diener. IEEE/ACM Transactions on Audio, Speech, and Language Processing, 2017. [doi:10.1109/TASLP.2017.2738568](https://doi.org/10.1109/TASLP.2017.2738568)

## Verdict

The paper [[1]](#ref-1) changes two components, both standard for 2017. Its mapping comparison (M06) ranks four mappings over the field's usual time-domain EMG features, on 83 evaluation utterances and single runs (Appendix; Table I). Its output route (M08), direct mapping to MFCCs and F0 with an MLSA vocoder, was the route of 11 of 12 prior synthesis studies from non-acoustic signals (Appendix), so its case against recognition followed by synthesis targets a route prior work had barely used. Two incidental components are behind: no silent articulation is tested (M04), as six prior studies did, including the group's own first EMG-to-speech paper [[2]](#ref-2), and intelligibility (M12) has no listener transcription, which five prior synthesis studies ran. The strongest overreach is the label-free claim, while the GMM and one LSTM use an LDA trained on audio-aligned phone sub-states (§III-A); retention of speaker identity and mood is asserted and not measured (§VI).

## Against the field, component by component

### M06 Decoder: EMG-to-acoustic mapping model

**Usual approach:** 20 of 27 prior surface-EMG speech decoders used HMM or GMM models and 12 used TD or E4 time-domain features (pattern match, unique studies, Appendix), the lineage of the paper's GMM baseline [[2]](#ref-2). The DNN was published by the group before (§III-E), Unit Selection in its conference versions [[3]](#ref-3), [[4]](#ref-4).

**State of the art:** GETS (2026) [[5]](#ref-5) [later] reaches 11.89% WER on the Gaddy silent-EMG test under Whisper; the paper's MCD and closed-vocabulary ASR proxy leave the gap unmeasured.

The DNN's mean MCD of 5.21 against 5.42, 5.46 and 5.69 (§V-B) rests on 10 to 20 test utterances per session (Table I) and an unnamed test for p < 0.01. It mixes model and input: GMM and one LSTM see 32 LDA dimensions, the DNN up to 5,425 TD15 dimensions (§V-A). The gain over Toth et al., 6.37 to 5.21 MCD or 18% relative (inference), sets one speaker, five electrodes and 380 training sentences [[2]](#ref-2) against sessions of 450 to 1,771 (Table I); the starting points differ. Verdict standard.

### M08 Output: direct mapping and vocoder

**Usual approach:** direct frame-wise mapping to spectral parameters in 11 of 12 prior synthesis studies; recognition then synthesis in one [[6]](#ref-6), none from EMG (pattern match, Appendix). The paper's regression to 25 MFCCs and F0 is that default.

**State of the art:** Tongue2Speech (2026) [[7]](#ref-7) [later] maps ultrasound to mel spectrograms with a neural vocoder at 15.93% WER (single TaL speaker, Whisper Medium). The vocoder changed, not the route; the authors call MLSA relatively simple (§III).

The claimed vocabulary freedom (§VI) is measured with an ASR using a trigram LM and 108 to 2,111-word vocabularies (§V-C; Fig. 6). Paralinguistic retention is untested; the one prosody test keeps reference MFCCs, where EMG-derived F0 scores 28 against 22 for zero F0 and 41 for resynthesis (Table III). Verdict standard.

### M04 Articulation mode: audible speech only

**Usual approach:** six prior studies applied overt-trained decoders to silent articulation (confirmed, Appendix): Toth et al. at 79.8% to 94.90% WER on silent EMG over 27 sessions from 14 speakers [[2]](#ref-2); Hueber and Bailly, trained on modal speech, at about 30% listener word accuracy [[8]](#ref-8). The article is audible EMG only (Table I), though the authors call a silent system possible (§I).

**State of the art:** GETS (2026) [[5]](#ref-5) [later] reports 11.89% WER on the Gaddy silent-EMG test (Whisper). Verdict behind, yardstick best comparable work: six earlier studies meet the condition, the best read and named [[8]](#ref-8).

### M12 Evaluation: intelligibility of the output

**Usual approach:** five of the 12 prior synthesis studies ran listener transcription or identification (confirmed, Appendix); the best comparable [[8]](#ref-8) had ten naive listeners transcribe 30 sentences, 60.4% word accuracy for GMM mapping. The paper has 10 listeners rank 10 utterances (§V-E).

**State of the art:** Wairagkar et al. (2025) [[9]](#ref-9) [later] report 43.75% median open-transcription WER (intracortical, one participant, naive listeners).

The authors find intelligibility too low for transcription (§V-E), which argues for reporting a low score. The ASR proxy is trained on synthesized training-set output (§V-C), for two speakers (Fig. 6); its 7.3% WER at 108 words against 10.9% for an EMG recognizer on 160 utterances is, the authors concede, not direct (§V-C). Verdict behind, best comparable work.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Audible read sentences, parallel audio | Read sentences, parallel audio | – | standard |
| M02 Training-only supervision | MFCC/F0 targets; LDA on phone labels | Paired audio targets | – | standard |
| M03 Training and adaptation | Session-dependent | Session-dependent | – | standard |
| M04 Use-time action | Audible only | Silent test reported; prior studies (confirmed 6) | 11.89% WER, silent EMG [[5]](#ref-5) | behind |
| M05 Sensors | 35-channel arrays; 6 electrodes | Multi-channel facial EMG | – | standard |
| M06 Processing and decoding | TD15/LDA; GMM, Unit Selection, DNN, BLSTM | HMM/GMM over TD features; 27 prior (pattern match 20) | 11.89% WER, silent EMG [[5]](#ref-5) | standard |
| M07 Lexicon and LM | No LM | No LM | – | standard |
| M08 Output | Direct mapping, MLSA | Direct frame-wise mapping; 12 prior (pattern match 11) | 15.93% WER, TaL [[7]](#ref-7) | standard |
| M09 Confirmation | Offline | – | – | not applicable |
| M10 Correction | Offline | – | – | not applicable |
| M11 Reference construction | Six audible sessions, 83 test utterances | Per-speaker audible corpus | – | standard |
| M12 Evaluation | MCD; ASR proxy; ranking tests | Listener transcription; 12 prior (confirmed 5) | 43.75% median WER [[9]](#ref-9) | behind |
| M13 Device and cost | Batch mapping time | Offline timing | – | standard |

## Where the claims outrun the evidence

- "Label-free" (§I) against LDA on force-aligned phone sub-states (§III-A; Table II).
- Best performance "4.51" (§V-B), while the best evaluation session is 4.56 (Fig. 5).
- DNN "best in naturalness" (§VI), while the naturalness test varies only F0 and names no mapping (§V-D; Table III).
- Real time is batch feature mapping without vocoder or I/O (§V-A); closed-loop synthesis had been run from EMA [[10]](#ref-10).

## What the field needs next

- M04: the four mappings on silent EMG, with the drop per session.
- M12: open transcription of every evaluation utterance, resynthesis as ceiling.
- M06: repeated runs, one input for all models, a cross-session test.
- M08: speaker-verification and emotion scores on converted speech.

## Questions for the authors

- Which test gives p < 0.01, over which units?
- Is the LDA fitted on training data only, and which run gives the MCD of 4.51?
- Which mapping produced the F0 in Table III, and why four speakers (§V-D) in a three-speaker corpus?
- Were faulty channels excluded before evaluation?

## Appendix: literature search

Setting for every count: speech decoding or synthesis from non-acoustic speech-production signals measured on the speaker; lip-video-only systems excluded; prior = first public before 2017-05, [concurrent] = 2017-05 to 2018-05. The group's conference versions [[3]](#ref-3), [[4]](#ref-4) are merged with the target; Toth et al. [[2]](#ref-2) counts as prior.

- M06, emg-speech-encoder-input-and-sequence-model. Inclusion rule: surface-EMG speech decoders (synthesis or recognition) classified by input representation and sequence model; auxiliary-EMG, non-speech EMG and reviews excluded; versions once. Ledger counts (published table): slot-filled 7,345, pattern match 83 unique studies. At the target's time: 27 prior unique studies; full-text pattern counts HMM or GMM 20, TD or E4 features 12, neural-network mention 9 (upper bound). Read in full: [[2]](#ref-2). Known-item recall (published table): 0.5.
- M08, non-acoustic-signal-to-speech-output-route. Inclusion rule: studies producing audible speech from non-acoustic production signals, classified as direct mapping or recognition then synthesis; face animation, acoustic input and reviews excluded. Ledger counts (published table): slot-filled 3,268, pattern match 144 unique studies. At the target's time: 12 prior unique studies, direct mapping 11, recognition then synthesis 1 [[6]](#ref-6); pattern match checked by title and ledger text. Read in full: [[2]](#ref-2), [[7]](#ref-7). Known-item recall (published table): 0.17.
- M04, overt-to-silent-transfer. Inclusion rule: a decoder trained on overt speech applied to silent or covert speech without retraining, results reported; any signal; versions once. Published table: 33 unique candidates. At the target's time: 6 prior unique studies (confirmed), including two read additions [[2]](#ref-2), [[8]](#ref-8); the TASLP article does not meet the rule. Read in full: [[2]](#ref-2), [[8]](#ref-8), [[5]](#ref-5). Known-item recall (published table): 1.0.
- M12, listener-intelligibility-test. Inclusion rule: synthesized speech from non-acoustic signals evaluated by listeners who transcribe or identify words or sentences; naturalness, preference or MOS only excluded. Ledger counts (published table): slot-filled 6,960, pattern match 37 unique studies. At the target's time: 5 of the 12 prior synthesis studies of the M08 count (confirmed); the target does not meet the rule. Read in full: [[8]](#ref-8), [[9]](#ref-9). Known-item recall (published table): 1.0.

## References

Numbered by first citation. BibTeX in the same order and keys: [emg-to-speech-direct-generation-of-speech-from-facial-electromyographic-signals.bib](emg-to-speech-direct-generation-of-speech-from-facial-electromyographic-signals.bib).

1. <a id="ref-1"></a>Janke, M., Diener, L. “EMG-to-Speech: Direct Generation of Speech from Facial Electromyographic Signals.” *IEEE/ACM Transactions on Audio, Speech, and Language Processing*, 2017, 25(12), 2375. doi:[10.1109/TASLP.2017.2738568](https://doi.org/10.1109/TASLP.2017.2738568). Target. Read as the author-hosted journal manuscript. [wiki: doi-10.1109-taslp-2017-2738568](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-taslp-2017-2738568/article.md)
2. <a id="ref-2"></a>Toth, A. R., Wand, M., Schultz, T. “Synthesizing Speech from Electromyography using Voice Transformation Techniques.” *Proc. Interspeech 2009*, 2009. <https://www.isca-archive.org/interspeech_2009/toth09_interspeech.html> Distinct earlier design of the same group; prior. [wiki: isca-toth09_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-toth09_interspeech/article.md)
3. <a id="ref-3"></a>Zahner, M., Janke, M., Wand, M., Schultz, T. “Conversion from Facial Myoelectric Signals to Speech: A Unit Selection Approach.” *Proc. Interspeech 2014*, 2014. doi:[10.21437/Interspeech.2014-164](https://doi.org/10.21437/Interspeech.2014-164). Earlier conference version of the target system; merged with the target in all counts. [wiki: isca-zahner14_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-zahner14_interspeech/article.md)
4. <a id="ref-4"></a>Diener, L., Janke, M., Schultz, T. “Codebook Clustering for Unit Selection based EMG-to-Speech Conversion.” *Proc. Interspeech 2015*, 2015. <https://www.isca-archive.org/interspeech_2015/diener15_interspeech.pdf> Earlier conference version of the target system; merged with the target in all counts. [wiki: isca-diener15_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-diener15_interspeech/article.md)
5. <a id="ref-5"></a>Lee, J., Lee, J., Lee, K. “GETS: Guiding EMG-to-Speech Synthesis via Silent Speech Recognition.” *Proc. Interspeech 2026*, 2026. doi:[10.21437/Interspeech.2026-1938](https://doi.org/10.21437/Interspeech.2026-1938). [later]; state of the art. [later] [wiki: isca-lee26r_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-lee26r_interspeech/article.md)
6. <a id="ref-6"></a>Hueber, T., Benaroya, E., Chollet, G., Denby, B., Dreyfus, G., Stone, M. “Development of a Silent Speech Interface Driven by Ultrasound and Optical Images of the Tongue and Lips.” *Speech Communication*, 2010, 52(4), 288. doi:[10.1016/j.specom.2009.11.004](https://doi.org/10.1016/j.specom.2009.11.004). Prior. [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/development-of-a-silent-speech-interface-driven-by-ultrasound-and-optical-images-of-the-tongue-and-l) [wiki: doi-10.1016-j.specom.2009.11.004](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1016-j.specom.2009.11.004/article.md)
7. <a id="ref-7"></a>Sonkar, Y., Kilaru, Y., Yelimeli, S., Shah, N., Gandhi, V. “Tongue2Speech: Real-Time Speech Synthesis from Tongue Ultrasound Videos via Spatiotemporal Transformers.” *Proc. Interspeech 2026*, 2026, 6856–6860. doi:[10.21437/Interspeech.2026-3023](https://doi.org/10.21437/Interspeech.2026-3023). [later]; state of the art. [later] [wiki: isca-sonkar26_interspeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/isca-sonkar26_interspeech/article.md)
8. <a id="ref-8"></a>Hueber, T., Bailly, G. “Statistical Conversion of Silent Articulation into Audible Speech using Full-Covariance HMM.” *Computer Speech & Language*, 2016, 36, 274–293. doi:[10.1016/j.csl.2015.09.008](https://doi.org/10.1016/j.csl.2015.09.008). Prior. [wiki: doi-10.1016-j.csl.2015.09.008](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1016-j.csl.2015.09.008/article.md)
9. <a id="ref-9"></a>Wairagkar, M., Card, N. S., Singer-Clark, T., Hou, X., Iacobacci, C., Miller, L. M., et al. “An instantaneous voice-synthesis neuroprosthesis.” *Nature*, 2025. doi:[10.1038/s41586-025-09127-3](https://doi.org/10.1038/s41586-025-09127-3). [later]; state of the art. [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/an-instantaneous-voice-synthesis-neuroprosthesis) [wiki: doi-10.1038-s41586-025-09127-3](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-025-09127-3/article.md) [wiki: doi-10.1101-2024.08.14.607690](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2024.08.14.607690/article.md) [wiki: pmc-12369848-voicesynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12369848-voicesynth/article.md) [wiki: pmc-12369848-voice-synth-np](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12369848-voice-synth-np/article.md) [wiki: pmc-11370360-instvoice](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11370360-instvoice/article.md)
10. <a id="ref-10"></a>Bocquelet, F., Hueber, T., Girin, L., Savariaux, C., Yvert, B. “Real-Time Control of an Articulatory-Based Speech Synthesizer for Brain Computer Interfaces.” *PLoS Computational Biology*, 2016, 12(11), e1005119. doi:[10.1371/journal.pcbi.1005119](https://doi.org/10.1371/journal.pcbi.1005119). Prior. [wiki: doi-10.1371-journal.pcbi.1005119](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1371-journal.pcbi.1005119/article.md)
