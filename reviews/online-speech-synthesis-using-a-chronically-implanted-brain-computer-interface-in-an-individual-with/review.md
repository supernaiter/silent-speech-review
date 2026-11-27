# Online speech synthesis using a chronically implanted brain–computer interface in an individual with ALS

Angrick, Luo, Rabbani, Candrea, Shah, Milsap, Anderson, Gordon, Rosenblatt, Clawson, Tippett, Maragakis, Tenore, Fifer, Hermansky, Ramsey, Crone. Scientific Reports 14, 9617 (2024); first public on medRxiv 2023. [doi:10.1038/s41598-024-60277-2](https://doi.org/10.1038/s41598-024-60277-2)

## Verdict

The paper [[1]](#ref-1) changes two components: a closed-loop decoder that plays each word back after it ends (M06), and a chronic ECoG implant in a speaker with ALS, used 5.5 months after training (M13). Both are standard by our rules: closed-loop neural synthesis existed in 3 of 50 prior studies (Appendix) [[2]](#ref-2), [[3]](#ref-3), [[4]](#ref-4), and one participant with pooled sessions gives no repetition. The main claim holds narrowly: six keywords were identified at 80% against 16.7% chance, the earliest intelligible closed-loop neural synthesis in the prior set (Appendix), bought by dropping the real-time constraint and closing the vocabulary. The stability claim has no pre-gap measurement to compare with (§Results). Synthesized words remain far less intelligible than the participant's own (99.8%).

## Against the field, component by component

### M06 Decoding: closed loop, word-level delayed playback

**Usual approach:** Offline reconstruction; of 50 prior studies pairing synthesis with real-time or closed-loop terms (pattern match, unique studies), 5 played audio back in closed loop, all frame by frame during the attempt (Appendix). The paper decodes each detected word with a bidirectional network and plays it after the word ends.

**State of the art:** Neural closed loops then gave vowel formants within 50 ms (2009) [[2]](#ref-2) or unintelligible words (2021) [[4]](#ref-4). Today, a [later] intracortical system synthesizes sentences causally within 10 ms at 43.75% median listener WER (2025) [[5]](#ref-5), and 5.24% offline with simulated real-time inference (2026) [[6]](#ref-6).

The gain over the 2021 loop [[4]](#ref-4) comes from an easier task, not a better frame-level decoder: the decoder sees the whole word before output (§Approach), and with six keywords it learned word-specific dynamics and did not synthesize unseen words, as the authors state (§Discussion). The experiment therefore cannot separate synthesis from a six-way word classifier plus playback, a baseline it does not run (inference); the same participant's commands were already classified [[7]](#ref-7) ([concurrent]). Verdict: standard.

### M13 Device: chronic implant in a speaker with ALS

**Usual approach:** Acute recordings in people with intact speech: 8 of 10 prior intracranial synthesis studies used epilepsy-monitoring or intraoperative electrodes (pattern match, unique studies; Appendix) [[8]](#ref-8), [[9]](#ref-9), [[10]](#ref-10); two used chronic implants [[2]](#ref-2), [[11]](#ref-11).

**State of the art:** A [later] chronic intracortical implant in a man with ALS and severe dysarthria gives closed-loop sentences at 43.75% median open-transcription WER (2025) [[5]](#ref-5); [concurrent] chronic ECoG in anarthria synthesized cued sentences, as the target describes it [[12]](#ref-12).

This is the component that moves the field: among the 10 prior studies (Appendix), only [[2]](#ref-2) recorded a speech-impaired user, with vowel output. Stability is weaker than stated: the 80% is measured only after the gap, per-session values are not given (§Results), and the cited 3-month result is command classification [[7]](#ref-7). Verdict: standard (one participant).

### M12 Evaluation: six-choice listener identification

**Usual approach:** Closed-set identification, used by all 3 prior intracranial production studies in the listener-test table (confirmed, Appendix) [[8]](#ref-8), [[9]](#ref-9), [[10]](#ref-10); six choices match the six-word task.

**State of the art:** [later] closed-loop sentences reach 94.34% six-choice matching (2025) [[5]](#ref-5); open transcription is now the yardstick (2026) [[6]](#ref-6).

Error is 20% here against 5.66% (inference), but words and sentences differ, so this is not like-for-like. Verdict: standard.

## The 13 components

| Component | This paper | Usual approach (count) | State of the art | Verdict |
|---|---|---|---|---|
| M01 Training-time action | Cued overt keyword reading | Cued overt or attempted speech | – | standard |
| M02 Training-only supervision | Own overt audio, LPCNet features | Paired own audio | – | standard |
| M03 Training and adaptation | Trained once; per-day normalization | Supervised training, per-session normalization | – | standard |
| M04 Use-time action | Overt self-paced words, dysarthric | Overt speech by intact speakers | – | standard |
| M05 Sensors | 2 ECoG grids, 64 selected channels | Clinical ECoG grids | – | standard |
| M06 Processing and decoding | Bidirectional decoding, played after each word | Offline; closed loop in 5 of 50 prior (pattern match 5) | Causal 10 ms closed loop, 43.75% WER [[5]](#ref-5) | standard |
| M07 Lexicon and LM | None | No lexicon in synthesis | – | standard |
| M08 Output | LPCNet, own voice | Vocoder from decoded acoustic features | – | standard |
| M09 Confirmation | None | Confirmation step | – | not applicable |
| M10 Correction | None | Correction loop | – | not applicable |
| M11 Reference construction | Own overt speech | Own overt speech | – | standard |
| M12 Evaluation | Six-choice word identification, 21 listeners | Closed-set identification, 3 of 3 prior intracranial (confirmed 3) | 94.34% six-choice sentences [[5]](#ref-5) | standard |
| M13 Device and cost | Chronic ECoG, ALS, 5.5 months after training | Acute, intact speech: 8 of 10 prior (pattern match 8) | ALS implant, closed loop, 43.75% WER [[5]](#ref-5) | standard |

## Where the claims outrun the evidence

- Stability. "Not significantly changed over this time period" (§Discussion) rests on no test: no pre-gap listener score, no statistic, no per-day accuracy. The authors do ask for longer longitudinal testing (§Discussion).
- Denominator. Of 180 samples, 2 were excluded for no output and "a few" silent false detections without a count (§Results), so the 80% has no stated denominator or interval.
- Usefulness. Listeners identified the participant's own keywords at 99.8% and the synthesized ones at 80%, about 100 times the error (inference); "Back" reached 37.3% (Fig. 2C). The case rests on future speech decline (§Introduction), which is not tested.
- Lineage. The paper calls earlier ECoG synthesis offline except [[12]](#ref-12) (§Discussion) and omits the first author's closed-loop sEEG synthesis [[4]](#ref-4) (References).
- Reproducibility. The replication script and training-script defaults swap test and validation days, and no seed is set (§Materials and methods; repository).

## What the field needs next

- M06: compare synthesis with a word classifier plus own-voice playback, and test unseen words.
- M13: run the same listener test at training time and after the gap, per day, in more than one participant.
- M12: report per-session accuracy with intervals, count false detections as errors, add open transcription.
- M02/M06: train without overt audio (the authors' own caveat, §Discussion) and compare delayed with frame-level feedback.

## Questions for the authors

- What was listener accuracy per session, and the scored count after exclusions?
- How many false nVAD detections occurred per session?
- Which days were test and validation for the released weights?
- What did the pipeline reach before the 5.5-month gap?
- What is the delay from speech offset to playback?

## Appendix: literature search

- M06 causal-closed-loop-speech-synthesis (reused topic table). Inclusion rule: studies that synthesize speech acoustics from a non-acoustic signal online, in real time, with the audio played back while or right after the user speaks; offline studies only when they simulate causal frame-level inference; excluded: offline acausal reconstruction, text decoding read out by TTS, conversion from acoustic input. Ledger counts: 7,345 slot-filled; 87 pattern match (unique studies, all years). At the target's time (prior before 2023-01): 50 prior studies (pattern match, unique studies); 6 meet the rule; 5 played audio back in closed loop; 3 of these are neural (intracortical, EEG, sEEG), all frame-level; none plays a decoded word after it ends. Read in full: [[2]](#ref-2), [[4]](#ref-4) (deciding priors); [[5]](#ref-5), [[6]](#ref-6) (state of the art). Known-item recall 1.0 (4 seeds).
- M13 intracranial-synthesis-participant-and-implant (new topic). Inclusion rule: studies that reconstruct speech acoustics from intracranial recordings during produced, attempted or imagined speech, classified by participant and implant: acute clinical (epilepsy or intraoperative) in people with intact speech versus a chronic implant in a person with impaired speech; excluded: heard-speech reconstruction, text-only decoders, reviews; versions once. Ledger counts: 6,075 slot-filled; 180 pattern match (unique studies, all years); full-text mentions (upper bounds): impaired-speech population 72, epilepsy 60, intraoperative 29, chronic implant or clinical trial 29. At the target's time: 10 prior decoders; acute with intact speech 8; chronic implant 2 [[2]](#ref-2), [[11]](#ref-11); speech-impaired 1. Read in full: [[2]](#ref-2), [[4]](#ref-4) (deciding priors); [[5]](#ref-5) (state of the art). Known-item recall 1.0 (4 seeds).
- M12 listener-intelligibility-test (reused topic table). Inclusion rule as published: human listener transcription or identification of speech synthesized from non-acoustic signals. Ledger counts: 6,960 slot-filled; 37 pattern match (unique studies). At the target's time: 23 prior studies with confirmed include decisions; 3 are intracranial production studies, all with closed-set identification [[8]](#ref-8), [[9]](#ref-9), [[10]](#ref-10). Read in full: [[8]](#ref-8) (prior); [[5]](#ref-5) (state of the art). Known-item recall 1.0 (3 seeds).

## References

Numbered by first citation. BibTeX in the same order and keys: [refs.bib](refs.bib).

1. <a id="ref-1"></a>Angrick, M., Luo, S., Rabbani, Q., Candrea, D. N., Shah, S., Milsap, G. W., et al. “Online speech synthesis using a chronically implanted brain–computer interface in an individual with ALS.” *Scientific Reports*, 2024, 14, 9617. doi:[10.1038/s41598-024-60277-2](https://doi.org/10.1038/s41598-024-60277-2). First public as medRxiv preprint 10.1101/2023.06.30.23291352 (2023-07-01) [wiki: doi-10.1038-s41598-024-60277-2](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41598-024-60277-2/article.md) [wiki: pmc-11053081-als-ecog-synth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11053081-als-ecog-synth/article.md) [wiki: pmc-11053081-onlinesyn](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11053081-onlinesyn/article.md)
2. <a id="ref-2"></a>Guenther, F. H., Brumberg, J. S., Wright, E. J., Nieto-Castanon, A., Tourville, J. A., Panko, M., et al. “A Wireless Brain-Machine Interface for Real-Time Speech Synthesis.” *PLoS ONE*, 2009, 4(12), e8218. doi:[10.1371/journal.pone.0008218](https://doi.org/10.1371/journal.pone.0008218). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-wireless-brain-machine-interface-for-real-time-speech-synthesis) [wiki: pmc-2784218-wireless](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wireless/article.md) [wiki: pmc-2784218-wirelesssynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-2784218-wirelesssynth/article.md) [wiki: doi-10.1371-journal.pone.0008218](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1371-journal.pone.0008218/article.md)
3. <a id="ref-3"></a>Brumberg, J. S., Pitt, K. M., Burnison, J. D. “A Non-Invasive Brain-Computer Interface for Real-Time Speech Synthesis: The Importance of Multimodal Feedback.” *IEEE Transactions on Neural Systems and Rehabilitation Engineering*, 2018, 26(4), 874-881. doi:[10.1109/TNSRE.2018.2808425](https://doi.org/10.1109/TNSRE.2018.2808425). [wiki: doi-10.1109-tnsre.2018.2808425](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1109-tnsre.2018.2808425/article.md) [wiki: pmc-5906041-kennedy](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-5906041-kennedy/article.md)
4. <a id="ref-4"></a>Angrick, M., Ottenhoff, M. C., Diener, L., Ivucic, D., Ivucic, G., Goulis, S., et al. “Real-time synthesis of imagined speech processes from minimally invasive recordings of neural activity.” *Communications Biology*, 2021, 4, 1055. doi:[10.1038/s42003-021-02578-0](https://doi.org/10.1038/s42003-021-02578-0). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/real-time-synthesis-of-imagined-speech-processes-from-minimally-invasive-recordings-of-neural-activi) [wiki: doi-10.1038-s42003-021-02578-0](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s42003-021-02578-0/article.md) [wiki: pmc-8460739-realtimesynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-8460739-realtimesynth/article.md)
5. <a id="ref-5"></a>Wairagkar, M., Card, N. S., Singer-Clark, T., Hou, X., Iacobacci, C., Miller, L. M., et al. “An instantaneous voice-synthesis neuroprosthesis.” *Nature*, 2025. doi:[10.1038/s41586-025-09127-3](https://doi.org/10.1038/s41586-025-09127-3). [later] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/an-instantaneous-voice-synthesis-neuroprosthesis) [wiki: doi-10.1038-s41586-025-09127-3](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-025-09127-3/article.md) [wiki: doi-10.1101-2024.08.14.607690](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1101-2024.08.14.607690/article.md) [wiki: pmc-12369848-voicesynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12369848-voicesynth/article.md) [wiki: pmc-12369848-voice-synth-np](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-12369848-voice-synth-np/article.md) [wiki: pmc-11370360-instvoice](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-11370360-instvoice/article.md)
6. <a id="ref-6"></a>Wairagkar, M., Srinivasan, A., Card, N. S., Singer-Clark, T., Hou, X., Iacobacci, C., et al. “Brain2voice 2.0: High-performance voice synthesis brain-computer interface.” *bioRxiv*, 2026. doi:[10.64898/2026.06.30.735633](https://doi.org/10.64898/2026.06.30.735633). [later] [wiki: doi-10.64898-2026.06.30.735633](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.64898-2026.06.30.735633/article.md)
7. <a id="ref-7"></a>Luo, S., Angrick, M., Coogan, C., Candrea, D. N., Wyse-Sookoo, K., Shah, S., et al. “Stable Decoding from a Speech BCI Enables Control for an Individual with ALS without Recalibration for 3 Months.” *Advanced Science*, 2023, 10(35), 2304853. doi:[10.1002/advs.202304853](https://doi.org/10.1002/advs.202304853). [concurrent] [wiki: doi-10.1002-advs.202304853](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1002-advs.202304853/article.md) [wiki: pmc-10724434-stablebci](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10724434-stablebci/article.md)
8. <a id="ref-8"></a>Anumanchipalli, G. K., Chartier, J., Chang, E. F. “Speech synthesis from neural decoding of spoken sentences.” *Nature*, 2019, 568(7753), 493–498. doi:[10.1038/s41586-019-1119-1](https://doi.org/10.1038/s41586-019-1119-1). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/speech-synthesis-from-neural-decoding-of-spoken-sentences) [wiki: doi-10.1038-s41586-019-1119-1](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-019-1119-1/article.md) [wiki: pmc-9714519-speechsynth](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-9714519-speechsynth/article.md)
9. <a id="ref-9"></a>Herff, C., Diener, L., Angrick, M., Mugler, E., Tate, M. C., Goldrick, M. A., et al. “Generating Natural, Intelligible Speech From Brain Activity in Motor, Premotor, and Inferior Frontal Cortices.” *Frontiers in Neuroscience*, 2019, 13, 1267. doi:[10.3389/fnins.2019.01267](https://doi.org/10.3389/fnins.2019.01267). [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/generating-natural-intelligible-speech-from-brain-activity-in-motor-premotor-and-inferior-frontal-co) [wiki: doi-10.3389-fnins.2019.01267](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.3389-fnins.2019.01267/article.md) [wiki: pmc-6882773-b2speech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-6882773-b2speech/article.md) [wiki: pmc-6882773-braintospeech](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-6882773-braintospeech/article.md)
10. <a id="ref-10"></a>Kohler, J., Ottenhoff, M. C., Goulis, S., Angrick, M., Colon, A. J., Wagner, L., et al. “Synthesizing Speech from Intracranial Depth Electrodes using an Encoder-Decoder Framework.” *arXiv preprint (Neurons, Behavior, Data analysis, and Theory)*, 2022. arXiv:[2111.01457](https://arxiv.org/abs/2111.01457). [wiki: arxiv-2111.01457](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/arxiv-2111.01457/article.md)
11. <a id="ref-11"></a>Wilson, G. H., Stavisky, S. D., Willett, F. R., Avansino, D. T., Kelemen, J. N., Hochberg, L. R., et al. “Decoding spoken English from intracortical electrode arrays in dorsal precentral gyrus.” *Journal of Neural Engineering*, 2020, 17(6), 066007. doi:[10.1088/1741-2552/abbfef](https://doi.org/10.1088/1741-2552/abbfef). bioRxiv 10.1101/2020.06.30.180935 [wiki: doi-10.1088-1741-2552-abbfef](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1088-1741-2552-abbfef/article.md)
12. <a id="ref-12"></a>Metzger, S. L., Littlejohn, K. T., Silva, A. B., Moses, D. A., Seaton, M. P., Wang, R., et al. “A high-performance neuroprosthesis for speech decoding and avatar control.” *Nature*, 2023, 620, 1037–1046. doi:[10.1038/s41586-023-06443-4](https://doi.org/10.1038/s41586-023-06443-4). [concurrent] [review](https://github.com/supernaiter/silent-speech-review/tree/main/reviews/a-high-performance-neuroprosthesis-for-speech-decoding-and-avatar-control) [wiki: doi-10.1038-s41586-023-06443-4](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/doi-10.1038-s41586-023-06443-4/article.md) [wiki: pmc-10826467-avatarnp](https://github.com/supernaiter/deep-research-wiki-for-silent-speech/blob/main/papers/pmc-10826467-avatarnp/article.md)
